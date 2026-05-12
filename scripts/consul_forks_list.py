"""List all forks of consuldemocracy/consuldemocracy with metadata.

Uses the GitHub REST API via `gh api`. Saves
data/consul_forks.json — one record per fork with fields useful for
filtering (created_at, pushed_at, size, default_branch, archived).

A separate script (`consul_forks_compare.py`) does the per-fork
compare against upstream — that's the expensive call, so we keep the
listing as a cheap cached step.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

UPSTREAM = "consuldemocracy/consuldemocracy"
PER_PAGE = 100

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "consul_forks.json"

FIELDS = [
    "full_name", "owner", "default_branch", "created_at", "pushed_at",
    "size", "archived", "private", "fork", "forks_count",
    "stargazers_count", "html_url",
]


def list_forks() -> list[dict]:
    """Paginate through the forks endpoint, return all records."""
    cmd = [
        "gh", "api",
        "--paginate",
        "-X", "GET",
        f"/repos/{UPSTREAM}/forks?per_page={PER_PAGE}",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    # `--paginate` concatenates pages by stripping the outer array brackets
    # and joining with commas. To handle this robustly, parse line by line:
    # actually `gh api --paginate` returns a single concatenated array.
    raw = proc.stdout.strip()
    if not raw.startswith("["):
        raise SystemExit("unexpected API output format")
    # Sometimes gh emits multiple concatenated JSON arrays — merge.
    parts = []
    decoder = json.JSONDecoder()
    pos = 0
    while pos < len(raw):
        # skip whitespace
        while pos < len(raw) and raw[pos].isspace():
            pos += 1
        if pos >= len(raw):
            break
        value, idx = decoder.raw_decode(raw, pos)
        parts.extend(value)
        pos += idx - pos
    return parts


def slim(fork: dict) -> dict:
    rec = {}
    for f in FIELDS:
        rec[f] = fork.get(f)
    # Flatten owner.login for ease
    owner = fork.get("owner") or {}
    rec["owner_login"] = owner.get("login")
    rec["owner_type"] = owner.get("type")  # User or Organization
    return rec


def main():
    print(f"listing forks of {UPSTREAM}...")
    forks = list_forks()
    print(f"received {len(forks)} fork records")

    slim_forks = [slim(f) for f in forks]
    out = {
        "upstream": UPSTREAM,
        "fork_count_reported": len(slim_forks),
        "forks": slim_forks,
    }
    OUT.write_text(json.dumps(out, indent=2))
    print(f"wrote {OUT}")

    # Quick summary
    pushed_dates = sorted([f["pushed_at"] for f in slim_forks if f["pushed_at"]])
    if pushed_dates:
        print(f"earliest pushed_at: {pushed_dates[0][:10]}")
        print(f"latest pushed_at:   {pushed_dates[-1][:10]}")
    n_archived = sum(1 for f in slim_forks if f.get("archived"))
    n_zero_size = sum(1 for f in slim_forks if f.get("size") == 0)
    print(f"archived forks: {n_archived}")
    print(f"empty (size=0) forks: {n_zero_size}")


if __name__ == "__main__":
    main()
