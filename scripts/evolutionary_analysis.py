"""Evolutionary analysis of Decidim, Consul, Polis — Session 2.

For each repo:
- Total commits (no merges)
- Unique contributors, with bots filtered out separately
- First / last commit dates
- Per-author commit counts
- Top-10 contributor share (bus-factor proxy)
- Gini coefficient on commit distribution
- Commits per year

For Decidim only:
- Per-engine commit counts (which engines are alive vs dormant)

Writes data/evolutionary.json. Plots in a separate script.

Run:
    python scripts/evolutionary_analysis.py \\
        /home/leos/Dev/decidim \\
        /home/leos/Dev/consul \\
        /home/leos/Dev/polis
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

# Bot detection — emails that we treat as automation, not human contributors.
# Conservative: only obvious bots. We list them separately rather than discarding
# the data outright.
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


def git_log_authors(repo: Path) -> list[tuple[str, str, str]]:
    """Return list of (author_name, author_email, iso_date) for each non-merge commit."""
    out = subprocess.run(
        ["git", "-C", str(repo), "log", "--no-merges",
         "--pretty=format:%an%x09%ae%x09%aI"],
        capture_output=True, text=True, check=True,
    ).stdout
    rows = []
    for line in out.split("\n"):
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        rows.append(tuple(parts))
    return rows


def gini(values: list[int]) -> float:
    """Gini coefficient on a list of non-negative values."""
    if not values:
        return 0.0
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    cum = 0.0
    total = float(sum(sorted_vals))
    if total == 0:
        return 0.0
    for i, v in enumerate(sorted_vals, start=1):
        cum += i * v
    return (2 * cum) / (n * total) - (n + 1) / n


def analyse_repo(repo: Path) -> dict:
    rows = git_log_authors(repo)

    sha = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()

    head_date = subprocess.run(
        ["git", "-C", str(repo), "log", "-1", "--format=%aI"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()

    # Classify each commit's author as bot or human.
    human_commits = []
    bot_commits = []
    for name, email, date in rows:
        target = bot_commits if is_bot(email, name) else human_commits
        target.append((name, email, date))

    # Per-author counts (humans only)
    author_counts = Counter()
    author_names = {}  # email → most common name
    for name, email, _ in human_commits:
        key = email.lower()
        author_counts[key] += 1
        author_names.setdefault(key, name)

    # Bot author counts (separately)
    bot_counts = Counter(email.lower() for _, email, _ in bot_commits)

    # Commits per year (humans only)
    commits_per_year = Counter()
    for _, _, date in human_commits:
        year = date[:4]
        commits_per_year[year] += 1

    # Top-N concentration
    total_human = sum(author_counts.values())
    top_authors = author_counts.most_common(20)
    top10_share = (
        sum(c for _, c in top_authors[:10]) / total_human if total_human else 0.0
    )
    top3_share = (
        sum(c for _, c in top_authors[:3]) / total_human if total_human else 0.0
    )

    # First/last
    dates = sorted(d for _, _, d in human_commits)
    first = dates[0] if dates else None
    last = dates[-1] if dates else None

    return {
        "repo": repo.name,
        "snapshot_sha": sha,
        "snapshot_date": head_date,
        "total_commits_no_merges": len(rows),
        "human_commits": len(human_commits),
        "bot_commits": len(bot_commits),
        "unique_human_authors": len(author_counts),
        "unique_bot_authors": len(bot_counts),
        "first_human_commit": first,
        "last_human_commit": last,
        "top_authors": [
            {"email": e, "name": author_names[e], "commits": c}
            for e, c in top_authors[:20]
        ],
        "top_bots": [
            {"email": e, "commits": c} for e, c in bot_counts.most_common(10)
        ],
        "top10_share": top10_share,
        "top3_share": top3_share,
        "gini": gini(list(author_counts.values())),
        "commits_per_year": dict(sorted(commits_per_year.items())),
    }


def decidim_per_engine(repo: Path) -> dict:
    """For Decidim only: commit counts per first-party engine."""
    engines = sorted(p.name for p in repo.glob("decidim-*") if p.is_dir())
    counts = {}
    for eng in engines:
        out = subprocess.run(
            ["git", "-C", str(repo), "rev-list", "--no-merges",
             "--count", "HEAD", "--", eng],
            capture_output=True, text=True, check=True,
        )
        counts[eng] = int(out.stdout.strip() or 0)

    # Recent activity: commits in last 12 months
    cutoff = "2025-05-12"
    recent_counts = {}
    for eng in engines:
        out = subprocess.run(
            ["git", "-C", str(repo), "rev-list", "--no-merges",
             "--count", f"--since={cutoff}", "HEAD", "--", eng],
            capture_output=True, text=True, check=True,
        )
        recent_counts[eng] = int(out.stdout.strip() or 0)

    return {
        "all_time_commits_per_engine": counts,
        "recent_12mo_commits_per_engine": recent_counts,
        "recent_cutoff": cutoff,
    }


def main():
    if len(sys.argv) < 2:
        print("usage: evolutionary_analysis.py <repo-path> [<repo-path> ...]",
              file=sys.stderr)
        sys.exit(1)

    results = {}
    for arg in sys.argv[1:]:
        repo = Path(arg).resolve()
        if not (repo / ".git").exists():
            print(f"  skip (not a git repo): {repo}", file=sys.stderr)
            continue
        print(f"analysing {repo.name}...")
        analysis = analyse_repo(repo)
        if repo.name == "decidim":
            analysis["per_engine"] = decidim_per_engine(repo)
        results[repo.name] = analysis

    out_path = Path(__file__).resolve().parent.parent / "data" / "evolutionary.json"
    out_path.write_text(json.dumps(results, indent=2))
    print(f"\nwrote {out_path}")

    # Console summary
    print("\n=== Summary ===")
    for name, r in results.items():
        print(f"\n{name}")
        print(f"  HEAD: {r['snapshot_sha'][:10]} ({r['snapshot_date'][:10]})")
        print(f"  Commits (no merges): {r['total_commits_no_merges']:,}")
        print(f"    Human: {r['human_commits']:,}  Bot: {r['bot_commits']:,}")
        print(f"  Unique human authors: {r['unique_human_authors']:,}")
        print(f"  First human commit: {r['first_human_commit'][:10] if r['first_human_commit'] else '?'}")
        print(f"  Last human commit:  {r['last_human_commit'][:10] if r['last_human_commit'] else '?'}")
        print(f"  Top-3 share:  {r['top3_share']:.1%}")
        print(f"  Top-10 share: {r['top10_share']:.1%}")
        print(f"  Gini:         {r['gini']:.2f}")


if __name__ == "__main__":
    main()
