"""Render Decidim engine dependency graph from recovered data.

Reads data/decidim_engines.json (produced by recover_decidim.py) and
writes figures/decidim_dependency_graph.pdf.

Layered layout: core at bottom, infrastructure / shared services /
spaces / components above. Cross-engine runtime dependencies (the
ones that bypass core) are drawn as dashed edges so they stand out.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "decidim_engines.json"
OUT = ROOT / "figures" / "decidim_dependency_graph.pdf"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "pdf.fonttype": 42,
})

# Manually-chosen role assignment for each engine.
# Core: the foundation everything depends on.
# Infra: low-level cross-cutting services (admin, system, api).
# Shared: engines that other engines runtime-depend on (forms, comments, verifications).
# Spaces: participatory spaces (where participation happens).
# Components: features that attach to spaces (where participation runs).
# Tooling: developer-facing engines, not user-facing features.
ROLES = {
    "decidim-core": "core",
    # Infrastructure
    "decidim-admin": "infra",
    "decidim-api": "infra",
    "decidim-system": "infra",
    # Shared services (de-facto layer-0 — depended on by many)
    "decidim-comments": "shared",
    "decidim-forms": "shared",
    "decidim-verifications": "shared",
    # Participatory spaces
    "decidim-participatory_processes": "space",
    "decidim-assemblies": "space",
    "decidim-conferences": "space",
    "decidim-initiatives": "space",
    # Components
    "decidim-accountability": "component",
    "decidim-blogs": "component",
    "decidim-budgets": "component",
    "decidim-debates": "component",
    "decidim-meetings": "component",
    "decidim-pages": "component",
    "decidim-proposals": "component",
    "decidim-surveys": "component",
    "decidim-ai": "component",
    "decidim-collaborative_texts": "component",
    "decidim-demographics": "component",
    "decidim-elections": "component",
    "decidim-templates": "component",
    # Tooling
    "decidim-design": "tooling",
    "decidim-dev": "tooling",
    "decidim-generators": "tooling",
}


def short(name: str) -> str:
    return name.replace("decidim-", "").replace("participatory_processes", "processes")


def position_engines(roles_for_engines: dict[str, str]) -> dict[str, tuple[float, float]]:
    """Place engines by role on a 2D plane."""
    by_role: dict[str, list[str]] = {}
    for engine, role in roles_for_engines.items():
        by_role.setdefault(role, []).append(engine)
    for role in by_role:
        by_role[role].sort()

    pos: dict[str, tuple[float, float]] = {}

    # Layer 0: core, centered at the bottom
    pos["decidim-core"] = (0.5, 0.05)

    # Layer 1: infrastructure, low cross-row
    infra = by_role.get("infra", [])
    for i, e in enumerate(infra):
        x = 0.1 + 0.8 * (i + 0.5) / max(len(infra), 1)
        pos[e] = (x, 0.22)

    # Layer 2: shared services (de-facto core)
    shared = by_role.get("shared", [])
    for i, e in enumerate(shared):
        x = 0.15 + 0.7 * (i + 0.5) / max(len(shared), 1)
        pos[e] = (x, 0.40)

    # Layer 3: spaces
    spaces = by_role.get("space", [])
    for i, e in enumerate(spaces):
        x = 0.15 + 0.7 * (i + 0.5) / max(len(spaces), 1)
        pos[e] = (x, 0.60)

    # Layer 4: components (two rows of 7 + 6)
    components = by_role.get("component", [])
    half = (len(components) + 1) // 2
    for i, e in enumerate(components):
        row = 0 if i < half else 1
        col = i if row == 0 else i - half
        ncols = half if row == 0 else len(components) - half
        x = 0.08 + 0.84 * (col + 0.5) / max(ncols, 1)
        y = 0.78 + row * 0.10
        pos[e] = (x, y)

    # Tooling engines are not shown — they are developer infrastructure
    # rather than user-facing platform features. Noted in caption.

    return pos


def role_style(role: str) -> dict:
    base = {"linewidth": 0.7, "edgecolor": "0.3"}
    if role == "core":
        return {**base, "facecolor": "black", "textcolor": "white",
                "linewidth": 1.2, "fontweight": "bold"}
    if role == "shared":
        return {**base, "facecolor": "#fde0a3", "textcolor": "black"}
    if role == "infra":
        return {**base, "facecolor": "#dfe7f5", "textcolor": "black"}
    if role == "space":
        return {**base, "facecolor": "#d8e8d8", "textcolor": "black",
                "fontweight": "bold"}
    if role == "component":
        return {**base, "facecolor": "white", "textcolor": "black"}
    if role == "tooling":
        return {**base, "facecolor": "#f4f4f4", "textcolor": "0.4",
                "edgecolor": "0.7"}
    return {**base, "facecolor": "white", "textcolor": "black"}


def main():
    data = json.loads(DATA.read_text())
    engines = {e["name"]: e for e in data["engines"]}
    cross_deps = data["fact_checks"]["cross_engine_runtime_deps"]

    pos = position_engines(ROLES)

    fig, ax = plt.subplots(figsize=(11, 6.5))

    # === Background "all engines depend on core" bar ===
    # Spans the full width just above core; suggests the universal core dep
    # without drawing 26 arrows.
    ax.plot([0.05, 0.95], [0.12, 0.12], color="0.7", linewidth=3,
            solid_capstyle="round", zorder=1)
    ax.annotate("", xy=(0.5, 0.085), xytext=(0.5, 0.115),
                arrowprops=dict(arrowstyle="-|>", color="0.55",
                                lw=0.9, mutation_scale=10), zorder=1)
    ax.text(0.97, 0.12, "all engines\n→ core", fontsize=7.5, color="0.45",
            ha="left", va="center", style="italic")

    # === Cross-engine dependency arrows (the empirically real story) ===
    # Dashed, coloured by target so the "comments" and "forms" hubs pop.
    target_colours = {
        "decidim-comments": "#c44e52",
        "decidim-forms": "#dd8452",
        "decidim-admin": "#4c72b0",
        "decidim-verifications": "#8172b3",
        "decidim-meetings": "#55a868",
        "decidim-api": "#937860",
        "decidim-generators": "#937860",
    }

    for cd in cross_deps:
        src = cd["engine"]
        if ROLES.get(src) == "tooling":
            continue  # skip dev/generators clutter
        for tgt in cd["depends_on"]:
            if tgt not in pos:
                continue
            x1, y1 = pos[src]
            x2, y2 = pos[tgt]
            colour = target_colours.get(tgt, "0.55")
            ax.annotate(
                "", xy=(x2, y2 + 0.018), xytext=(x1, y1 - 0.018),
                arrowprops=dict(
                    arrowstyle="-|>", color=colour, lw=0.9,
                    linestyle=(0, (3, 2)), alpha=0.65,
                    mutation_scale=8,
                    connectionstyle="arc3,rad=0.12",
                ),
                zorder=2,
            )

    # === Engine boxes ===
    for name, (x, y) in pos.items():
        role = ROLES.get(name, "component")
        if role == "tooling":
            continue  # skip dev tooling — not user-facing
        style = role_style(role)
        label = short(name)
        box_w = 0.085 if role == "core" else 0.072
        box_h = 0.045 if role == "core" else 0.035
        box = FancyBboxPatch(
            (x - box_w / 2, y - box_h / 2),
            box_w, box_h,
            boxstyle="round,pad=0.005,rounding_size=0.008",
            linewidth=style["linewidth"],
            edgecolor=style["edgecolor"],
            facecolor=style["facecolor"],
            zorder=3,
        )
        ax.add_patch(box)
        ax.text(
            x, y, label,
            fontsize=8 if role == "core" else 7,
            fontweight=style.get("fontweight", "normal"),
            color=style["textcolor"],
            ha="center", va="center", zorder=4,
        )

    # === Layer labels (right margin) ===
    layer_labels = [
        (0.05, "LAYER 0"),
        (0.22, "INFRASTRUCTURE"),
        (0.40, "SHARED SERVICES"),
        (0.60, "SPACES"),
        (0.83, "COMPONENTS"),
    ]
    for y, txt in layer_labels:
        ax.text(0.01, y, txt, fontsize=7, color="0.4",
                ha="left", va="center", fontweight="bold")

    # === Legend (cross-engine deps) ===
    legend_items = [
        ("decidim-comments (6 dependents)", "#c44e52"),
        ("decidim-forms (5 dependents)", "#dd8452"),
        ("decidim-admin (3 dependents)", "#4c72b0"),
        ("other cross-engine deps", "0.55"),
    ]
    legend_x = 0.02
    legend_y = -0.05
    ax.text(legend_x, legend_y, "Cross-engine runtime dependencies:",
            fontsize=7.5, color="0.3", fontweight="bold",
            ha="left", va="center", transform=ax.transAxes)
    for i, (txt, col) in enumerate(legend_items):
        yi = legend_y - 0.035 - i * 0.025
        ax.annotate("", xy=(legend_x + 0.04, yi),
                    xytext=(legend_x, yi),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=0.9,
                                    linestyle=(0, (3, 2)), mutation_scale=8),
                    xycoords="axes fraction", textcoords="axes fraction")
        ax.text(legend_x + 0.05, yi, txt, fontsize=7, color="0.3",
                ha="left", va="center", transform=ax.transAxes)

    # === Snapshot footnote ===
    sha = data["snapshot"]["sha"][:10]
    date = data["snapshot"]["date"][:10]
    ax.text(0.99, -0.05, f"Snapshot: decidim/decidim @ {sha} ({date})",
            fontsize=6.5, color="0.5", style="italic",
            ha="right", va="center", transform=ax.transAxes)

    # === Frame ===
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.0)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    plt.savefig(OUT, bbox_inches="tight", pad_inches=0.25)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
