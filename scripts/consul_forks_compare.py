"""For each Consul fork, compute ahead/behind vs upstream.

Reads data/consul_forks.json (produced by consul_forks_list.py).
For each fork, calls the GitHub compare API:

    /repos/consuldemocracy/consuldemocracy/compare/master...{forkowner}:{forkbranch}

GitHub returns ahead_by (commits in fork not upstream) and behind_by
(commits upstream not in fork). We save these plus timing data.

Saves data/consul_forks_compare.json. Resumable: re-running picks up
where it left off.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

UPSTREAM = "consuldemocracy/consuldemocracy"
UPSTREAM_BRANCH = "master"
ROOT = Path(__file__).resolve().parent.parent
IN_FILE = ROOT / "data" / "consul_forks.json"
OUT_FILE = ROOT / "data" / "consul_forks_compare.json"


def compare(fork_owner: str, fork_branch: str) -> dict | None:
    """Return {ahead_by, behind_by, status} or None on error."""
    basehead = f"{UPSTREAM_BRANCH}...{fork_owner}:{fork_branch}"
    cmd = [
        "gh", "api",
        f"/repos/{UPSTREAM}/compare/{basehead}",
        "--jq", "{ahead_by, behind_by, status, total_commits}",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        return {"error": proc.stderr.strip()[:200]}
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"error": "unparseable"}


def main():
    data = json.loads(IN_FILE.read_text())
    forks = data["forks"]

    # Resume support
    done: dict[str, dict] = {}
    if OUT_FILE.exists():
        prev = json.loads(OUT_FILE.read_text())
        done = {r["full_name"]: r for r in prev.get("results", [])}
        print(f"resuming: {len(done)} forks already processed")

    results = list(done.values())
    total = len(forks)
    start = time.time()
    save_every = 50

    for i, fork in enumerate(forks, start=1):
        full = fork["full_name"]
        if full in done:
            continue
        cmp = compare(fork["owner_login"], fork["default_branch"])
        rec = {
            "full_name": full,
            "owner_login": fork["owner_login"],
            "owner_type": fork["owner_type"],
            "default_branch": fork["default_branch"],
            "pushed_at": fork["pushed_at"],
            "created_at": fork["created_at"],
            "size_kb": fork["size"],
            "archived": fork["archived"],
        }
        if cmp:
            rec.update(cmp)
        results.append(rec)

        if i % 25 == 0:
            elapsed = time.time() - start
            rate = i / elapsed if elapsed > 0 else 0
            remaining_s = (total - i) / rate if rate > 0 else 0
            print(f"  [{i}/{total}] {full[:50]:50s}  "
                  f"rate {rate:.1f}/s  eta {remaining_s/60:.1f} min")

        if i % save_every == 0:
            OUT_FILE.write_text(json.dumps(
                {"upstream": UPSTREAM, "results": results}, indent=2))

    OUT_FILE.write_text(json.dumps(
        {"upstream": UPSTREAM, "results": results}, indent=2))

    # Summary
    ok = [r for r in results if "ahead_by" in r]
    err = [r for r in results if "error" in r]
    print(f"\ndone: {len(ok)} ok, {len(err)} errors")
    if ok:
        ahead = [r["ahead_by"] for r in ok]
        behind = [r["behind_by"] for r in ok]
        print(f"ahead_by  median: {sorted(ahead)[len(ahead)//2]}, "
              f"max: {max(ahead)}, mean: {sum(ahead)/len(ahead):.1f}")
        print(f"behind_by median: {sorted(behind)[len(behind)//2]}, "
              f"max: {max(behind)}, mean: {sum(behind)/len(behind):.1f}")
        n_diverged = sum(1 for r in ok if r["ahead_by"] > 0)
        n_synced = sum(1 for r in ok if r["ahead_by"] == 0 and r["behind_by"] == 0)
        n_unmodified = sum(1 for r in ok if r["ahead_by"] == 0 and r["behind_by"] > 0)
        print(f"diverged (ahead > 0):           {n_diverged}")
        print(f"in sync (ahead = 0, behind = 0): {n_synced}")
        print(f"unmodified (ahead = 0, behind > 0): {n_unmodified}")


if __name__ == "__main__":
    main()
