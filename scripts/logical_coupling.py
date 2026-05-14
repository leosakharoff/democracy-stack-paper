"""Logical coupling between Decidim engines — Session 3.

Method (Gall et al. 1998 — "logical coupling"):
For each non-merge, non-bot commit, identify which engines (top-level
decidim-* dirs) it touches. Count co-occurrences. Compute pairwise
coupling metrics:

- co_changes: number of commits touching both A and B
- jaccard: co_changes / |commits touching A or B|
- conditional: P(B touched | A touched) = co_changes / |commits touching A|
  (asymmetric — useful for hub detection)

Filters:
- exclude merges (--no-merges)
- exclude bots (same author rules as evolutionary_analysis.py)
- exclude "mega-commits" that touch >K engines (likely refactors or
  release commits; including them pollutes the signal)

Hypothesis: if the manifest pattern fully isolates engines, we should
see low coupling between engines that do not share a gemspec
dependency. Cross-engine coupling above a threshold is evidence that
the gem boundary leaks (via the shared DB, shared ActiveRecord
associations, shared base classes, etc.).

Writes data/decidim_coupling.json.

Run:
    python scripts/logical_coupling.py /home/leos/Dev/decidim
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

BOT_PATTERNS = [
    re.compile(r"dependabot", re.IGNORECASE),
    re.compile(r"\+renovate-bot@", re.IGNORECASE),
    re.compile(r"crowdin[-_.]?(bot)?@", re.IGNORECASE),
    re.compile(r"noreply@translate\.", re.IGNORECASE),
    re.compile(r"github-actions(?:\[bot\])?@", re.IGNORECASE),
    re.compile(r"weblate@", re.IGNORECASE),
    re.compile(r"\[bot\]@", re.IGNORECASE),
    re.compile(r"^bot@", re.IGNORECASE),
    re.compile(r"^action@github\.com$", re.IGNORECASE),
]
_BOT_NAME_RE = re.compile(r"\b(bot|crowdin|weblate|github actions)\b", re.IGNORECASE)


def is_bot(email: str, name: str) -> bool:
    if any(p.search(email) for p in BOT_PATTERNS):
        return True
    if _BOT_NAME_RE.search(name):
        return True
    return False


# Excluding tooling engines for the coupling story — match the figure.
TOOLING = {"decidim-design", "decidim-dev", "decidim-generators"}

# Mega-commit threshold: commits touching >K engines are excluded as
# refactors / release commits. Tested values; 8 keeps the signal clean
# without throwing out informative cross-cutting changes.
MEGA_THRESHOLD = 8


def engine_of_path(path: str) -> str | None:
    """Return decidim-<engine> for a file in an engine, else None."""
    if not path.startswith("decidim-"):
        return None
    # decidim-proposals/foo/bar.rb -> decidim-proposals
    return path.split("/", 1)[0]


def iter_commits(repo: Path):
    """Yield (sha, email, name, [paths...]) for each non-merge commit."""
    cmd = [
        "git", "-C", str(repo), "log", "--no-merges",
        "--name-only",
        "--pretty=format:COMMIT%x09%H%x09%ae%x09%an",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    cur_sha = None
    cur_email = None
    cur_name = None
    cur_files: list[str] = []
    for line in proc.stdout.split("\n"):
        if line.startswith("COMMIT\t"):
            if cur_sha is not None:
                yield (cur_sha, cur_email, cur_name, cur_files)
            _, sha, email, name = line.split("\t", 3)
            cur_sha = sha
            cur_email = email
            cur_name = name
            cur_files = []
        elif line.strip():
            cur_files.append(line.strip())
    if cur_sha is not None:
        yield (cur_sha, cur_email, cur_name, cur_files)


def main():
    if len(sys.argv) != 2:
        print("usage: logical_coupling.py <decidim-checkout>", file=sys.stderr)
        sys.exit(1)

    repo = Path(sys.argv[1]).resolve()
    sha = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()

    # Discover engines from the working tree
    engines_all = sorted(p.name for p in repo.glob("decidim-*") if p.is_dir())
    engines = [e for e in engines_all if e not in TOOLING]

    # Commit-touching-engine accumulator
    engine_commits: dict[str, set[str]] = defaultdict(set)
    pair_commits: Counter = Counter()

    total_commits = 0
    human_commits = 0
    bot_commits = 0
    mega_commits = 0
    single_engine_commits = 0
    multi_engine_commits = 0

    for sha_i, email, name, files in iter_commits(repo):
        total_commits += 1
        if is_bot(email, name):
            bot_commits += 1
            continue
        human_commits += 1

        # Map files to engines
        touched: set[str] = set()
        for f in files:
            e = engine_of_path(f)
            if e and e in engines:
                touched.add(e)

        if not touched:
            continue

        if len(touched) > MEGA_THRESHOLD:
            mega_commits += 1
            continue

        if len(touched) == 1:
            single_engine_commits += 1
        else:
            multi_engine_commits += 1

        for e in touched:
            engine_commits[e].add(sha_i)

        # Build pairwise co-occurrences (unordered pairs)
        sorted_t = sorted(touched)
        for i in range(len(sorted_t)):
            for j in range(i + 1, len(sorted_t)):
                pair_commits[(sorted_t[i], sorted_t[j])] += 1

    # Compute coupling per pair
    pairs = []
    for (a, b), co in pair_commits.items():
        a_set = engine_commits[a]
        b_set = engine_commits[b]
        union = len(a_set | b_set)
        jaccard = co / union if union else 0.0
        p_b_given_a = co / len(a_set) if a_set else 0.0
        p_a_given_b = co / len(b_set) if b_set else 0.0
        pairs.append({
            "a": a, "b": b,
            "co_changes": co,
            "a_total": len(a_set),
            "b_total": len(b_set),
            "jaccard": jaccard,
            "p_b_given_a": p_b_given_a,
            "p_a_given_b": p_a_given_b,
        })

    pairs.sort(key=lambda p: -p["jaccard"])

    out = {
        "snapshot": {"repo": "decidim/decidim", "sha": sha},
        "params": {
            "tooling_excluded": sorted(TOOLING),
            "mega_threshold_engines": MEGA_THRESHOLD,
        },
        "stats": {
            "total_commits_no_merges": total_commits,
            "human_commits": human_commits,
            "bot_commits": bot_commits,
            "mega_commits_excluded": mega_commits,
            "single_engine_commits": single_engine_commits,
            "multi_engine_commits": multi_engine_commits,
            "isolation_rate": (
                single_engine_commits / (single_engine_commits + multi_engine_commits)
                if (single_engine_commits + multi_engine_commits) else 0.0
            ),
        },
        "engines": engines,
        "engine_commits_count": {e: len(engine_commits[e]) for e in engines},
        "pairs": pairs,
    }

    out_path = Path(__file__).resolve().parent.parent / "data" / "decidim_coupling.json"
    out_path.write_text(json.dumps(out, indent=2))

    print(f"snapshot: decidim @ {sha[:10]}")
    print(f"total commits (no-merges): {total_commits:,}")
    print(f"  human:  {human_commits:,}")
    print(f"  bot:    {bot_commits:,}")
    print(f"  mega-commits excluded (touching >{MEGA_THRESHOLD} engines): {mega_commits:,}")
    print(f"engine-touching human commits: {single_engine_commits + multi_engine_commits:,}")
    print(f"  single-engine: {single_engine_commits:,}")
    print(f"  multi-engine:  {multi_engine_commits:,}")
    if single_engine_commits + multi_engine_commits:
        rate = single_engine_commits / (single_engine_commits + multi_engine_commits)
        print(f"  isolation rate (single / total): {rate:.1%}")

    print(f"\ntop 15 engine-pair couplings (by Jaccard):")
    for p in pairs[:15]:
        print(f"  {p['a']:35s} <-> {p['b']:35s}  J={p['jaccard']:.3f}  co={p['co_changes']:4d}")

    print(f"\nfull data: {out_path}")


if __name__ == "__main__":
    main()
