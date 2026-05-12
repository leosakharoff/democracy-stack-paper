"""Decidim architectural recovery — Session 1.

Reads all `decidim-*` gemspecs in a Decidim checkout, extracts:
- gem name
- runtime add_dependency calls
- development add_development_dependency calls

Classifies each dependency as either an internal Decidim engine or an
external gem. Writes structured JSON to data/decidim_engines.json so
later scripts can build dependency graphs and check the paper's claim
that "no engine-to-engine dependency bypasses decidim-core".

Run:
    python scripts/recover_decidim.py /home/leos/Dev/decidim
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

# Matches: s.add_dependency "decidim-core", version
# or:      s.add_dependency 'decidim-core'
ADD_DEP_RE = re.compile(
    r"""s\.add_dependency\s+["']([^"']+)["']""",
    re.MULTILINE,
)
ADD_DEV_DEP_RE = re.compile(
    r"""s\.add_development_dependency\s+["']([^"']+)["']""",
    re.MULTILINE,
)


@dataclass
class Engine:
    name: str  # e.g. "decidim-proposals"
    short: str  # e.g. "proposals"
    gemspec_path: str  # relative to repo root
    runtime_deps_internal: list[str] = field(default_factory=list)
    runtime_deps_external: list[str] = field(default_factory=list)
    dev_deps_internal: list[str] = field(default_factory=list)
    dev_deps_external: list[str] = field(default_factory=list)


def is_internal(dep: str) -> bool:
    return dep.startswith("decidim-") or dep == "decidim"


def parse_gemspec(gemspec_path: Path, repo_root: Path) -> Engine:
    text = gemspec_path.read_text(encoding="utf-8")

    name = gemspec_path.stem  # decidim-proposals.gemspec -> decidim-proposals
    short = name.replace("decidim-", "") if name != "decidim" else "umbrella"

    runtime_deps = ADD_DEP_RE.findall(text)
    dev_deps = ADD_DEV_DEP_RE.findall(text)

    engine = Engine(
        name=name,
        short=short,
        gemspec_path=str(gemspec_path.relative_to(repo_root)),
    )
    for dep in runtime_deps:
        bucket = engine.runtime_deps_internal if is_internal(dep) else engine.runtime_deps_external
        bucket.append(dep)
    for dep in dev_deps:
        bucket = engine.dev_deps_internal if is_internal(dep) else engine.dev_deps_external
        bucket.append(dep)

    return engine


def main():
    if len(sys.argv) != 2:
        print("usage: recover_decidim.py <path-to-decidim-checkout>", file=sys.stderr)
        sys.exit(1)

    repo_root = Path(sys.argv[1]).resolve()
    if not (repo_root / ".git").exists():
        print(f"not a git checkout: {repo_root}", file=sys.stderr)
        sys.exit(1)

    sha = subprocess.run(
        ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()

    head_date = subprocess.run(
        ["git", "-C", str(repo_root), "log", "-1", "--format=%ai"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()

    gemspec_paths = sorted(repo_root.glob("decidim-*/*.gemspec"))
    engines = [parse_gemspec(p, repo_root) for p in gemspec_paths]

    # Sanity: paper claims "every engine declares add_dependency decidim-core"
    # Check what proportion actually does.
    has_core_dep = [e for e in engines if "decidim-core" in e.runtime_deps_internal]
    missing_core_dep = [e for e in engines if "decidim-core" not in e.runtime_deps_internal]

    # Sanity: paper claims "no engine-to-engine dependency bypasses core"
    # Find engines with runtime deps on other engines besides decidim-core.
    cross_engine_deps = []
    for e in engines:
        non_core = [d for d in e.runtime_deps_internal if d not in ("decidim-core",)]
        if non_core:
            cross_engine_deps.append({"engine": e.name, "depends_on": non_core})

    result = {
        "snapshot": {
            "repo": "decidim/decidim",
            "sha": sha,
            "date": head_date,
        },
        "engine_count": len(engines),
        "engines": [asdict(e) for e in engines],
        "fact_checks": {
            "engines_depending_on_core": [e.name for e in has_core_dep],
            "engines_missing_core_dep": [e.name for e in missing_core_dep],
            "cross_engine_runtime_deps": cross_engine_deps,
        },
    }

    out_path = Path(__file__).resolve().parent.parent / "data" / "decidim_engines.json"
    out_path.write_text(json.dumps(result, indent=2))

    # Console summary
    print(f"snapshot: decidim/decidim @ {sha[:10]} ({head_date})")
    print(f"engines found: {len(engines)}")
    print(f"engines depending on decidim-core: {len(has_core_dep)}/{len(engines)}")
    if missing_core_dep:
        print(f"engines missing core dep: {[e.name for e in missing_core_dep]}")
    print(f"engines with cross-engine runtime deps (besides core): {len(cross_engine_deps)}")
    for cd in cross_engine_deps:
        print(f"  {cd['engine']} -> {cd['depends_on']}")
    print(f"\nfull data: {out_path}")


if __name__ == "__main__":
    main()
