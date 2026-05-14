"""Render Decidim engine logical-coupling heatmap.

Reads data/decidim_coupling.json, writes figures/decidim_coupling.pdf.

Layout: engines grouped by role (core → infrastructure → shared services
→ spaces → components), so the four-space block and the core/admin
co-evolution are immediately visible. Jaccard similarity on the cells.
Cells annotated with co-change count for high-coupling pairs.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "decidim_coupling.json"
OUT = ROOT / "figures" / "decidim_coupling.pdf"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "pdf.fonttype": 42,
})

# Engine ordering: groups visible as blocks on the heatmap diagonal.
ROLE_ORDER = [
    ("core",   ["decidim-core"]),
    ("infra",  ["decidim-admin", "decidim-api", "decidim-system"]),
    ("shared", ["decidim-comments", "decidim-forms", "decidim-verifications"]),
    ("space",  ["decidim-participatory_processes", "decidim-assemblies",
                "decidim-conferences", "decidim-initiatives"]),
    ("component", [
        "decidim-proposals", "decidim-meetings", "decidim-budgets",
        "decidim-debates", "decidim-accountability", "decidim-surveys",
        "decidim-blogs", "decidim-pages",
        "decidim-elections", "decidim-templates",
        "decidim-collaborative_texts", "decidim-demographics", "decidim-ai",
    ]),
]


def short(name: str) -> str:
    return (
        name.replace("decidim-", "")
        .replace("participatory_processes", "processes")
        .replace("collaborative_texts", "collab_texts")
    )


def main():
    data = json.loads(DATA.read_text())
    pairs = data["pairs"]

    order = [e for _, group in ROLE_ORDER for e in group]
    n = len(order)
    idx = {e: i for i, e in enumerate(order)}

    # Build matrix
    M = np.zeros((n, n))
    co_M = np.zeros((n, n), dtype=int)
    for p in pairs:
        if p["a"] not in idx or p["b"] not in idx:
            continue
        i = idx[p["a"]]
        j = idx[p["b"]]
        M[i, j] = p["jaccard"]
        M[j, i] = p["jaccard"]
        co_M[i, j] = p["co_changes"]
        co_M[j, i] = p["co_changes"]

    # Diagonal: 1.0 (engine fully coupled with itself), shown as the
    # max-colour cell to anchor the scale.
    for i in range(n):
        M[i, i] = 1.0

    fig, ax = plt.subplots(figsize=(9.5, 8.5))

    # White-to-dark colourmap; clip so Jaccard up to ~0.45 reaches full
    # colour (anything above is just core itself).
    cmap = mcolors.LinearSegmentedColormap.from_list(
        "white_to_dark",
        ["#ffffff", "#fde0a3", "#dd8452", "#b03a2e", "#3b1f1f"],
    )
    norm = mcolors.Normalize(vmin=0, vmax=0.45)
    im = ax.imshow(M, cmap=cmap, norm=norm, aspect="equal")

    # Cell annotations: print co-change counts for pairs with Jaccard >= 0.10
    # (excluding diagonal); skip otherwise to reduce clutter.
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if M[i, j] >= 0.10:
                colour = "white" if M[i, j] >= 0.25 else "black"
                ax.text(j, i, f"{M[i, j]:.2f}",
                        ha="center", va="center", fontsize=6.5, color=colour)

    # Ticks / labels
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.set_xticklabels([short(e) for e in order], rotation=55, ha="right",
                       fontsize=8)
    ax.set_yticklabels([short(e) for e in order], fontsize=8)

    # Block separators (between role groups)
    boundaries = []
    cum = 0
    for _, group in ROLE_ORDER[:-1]:
        cum += len(group)
        boundaries.append(cum - 0.5)
    for b in boundaries:
        ax.axhline(b, color="0.35", linewidth=0.7)
        ax.axvline(b, color="0.35", linewidth=0.7)

    # Role labels on right edge
    cum = 0
    role_labels = {"core": "CORE", "infra": "INFRA", "shared": "SHARED",
                   "space": "SPACES", "component": "COMPONENTS"}
    for role, group in ROLE_ORDER:
        mid = cum + len(group) / 2 - 0.5
        ax.text(n - 0.3, mid, role_labels[role],
                fontsize=8, color="0.4", fontweight="bold",
                ha="left", va="center", rotation=270)
        cum += len(group)

    cbar = plt.colorbar(im, ax=ax, shrink=0.55, pad=0.08)
    cbar.set_label("Jaccard coupling  (commits touching both / commits touching either)",
                   fontsize=8.5, labelpad=8)
    cbar.ax.tick_params(labelsize=7)

    sha = data["snapshot"]["sha"][:10]
    iso = data["stats"]["isolation_rate"]
    ax.set_title(
        f"Logical coupling between Decidim engines\n"
        f"{data['stats']['human_commits']:,} human commits · "
        f"{iso:.0%} single-engine isolation rate · "
        f"snapshot {sha}",
        fontsize=10, pad=14,
    )

    plt.tight_layout()
    plt.savefig(OUT, bbox_inches="tight", pad_inches=0.2)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
