  # Session 1 log — Decidim architectural recovery

**Snapshot:** `decidim/decidim @ be39c244035485e2eba7181252aea487f5897cef`
**Date:** 2026-05-12 (HEAD at clone time)
**Clone:** `/home/leos/Dev/decidim` (partial clone, `--filter=blob:none`)
**Script:** `scripts/recover_decidim.py`, output `data/decidim_engines.json`

## What we set out to verify

The paper makes three structural claims about Decidim's engine architecture
(Section 4.1, lines 191–196):

1. "23 first-party engines."
2. "Every engine declares `add_dependency "decidim-core"` in its gemspec file."
3. "No engine-to-engine dependency bypasses core."
4. The dependency graph is a "layered star: core at layer 0, infrastructure
   engines at layer 1, and space and component engines at layer 2."

Figure 2 in the paper visualises 23 engines split across these three layers,
and lists `sortitions` as one of nine components.

## What the data says

### Engine count

**27 first-party engines, not 23.** The extra eight are: `ai`,
`collaborative_texts`, `demographics`, `design`, `dev`, `elections`,
`generators`, `templates`. Three of those (`design`, `dev`, `generators`) are
developer tooling — not user-facing platform features, fair to leave out of
the architecture figure. That leaves **24 production engines**.

The paper's "23 engines" figure was probably accurate against an older
snapshot (Barandiaran 2024 was written against ~2023 Decidim). The platform
has added `ai`, `collaborative_texts`, `demographics`, `elections`, and
`templates` since.

### Sortitions

**`decidim-sortitions` was removed from the codebase on 2025-11-19**, via
commit `b86c85a3c4` ("Remove `sortitions` module", PR #15563). The paper
lists it as one of nine components in Figure 2 — that was true against the
Barandiaran 2024 reference and against Decidim ≤ 0.30, but not against the
current `master`. Drop sortitions from the figure caption and from the list
of nine components in Section 4.1.

This is itself a small Lehman-style evolution story: the platform retired a
feature in the six months between when our source material was published
and when we wrote the paper. Worth mentioning in passing — it sharpens the
"as of May 2026" framing.

### "Every engine depends on decidim-core" — TRUE

26 of 27 engines declare `add_dependency "decidim-core"` in their gemspec.
The one exception is `decidim-core` itself, which sensibly does not depend
on itself. ✓ The claim holds.

### "No engine-to-engine dependency bypasses core" — FALSE

13 of 27 engines have runtime `add_dependency` calls on other Decidim
engines besides `decidim-core`. Most notable:

| Target              | Dependents | Engines that depend on it                                      |
| ------------------- | ---------- | -------------------------------------------------------------- |
| `decidim-comments`  | 6          | accountability, blogs, budgets, debates, initiatives, proposals|
| `decidim-forms`     | 5          | demographics, elections, meetings, surveys, templates          |
| `decidim-admin`     | 3 (prod)   | blogs, elections, initiatives (plus dev tooling)               |
| `decidim-verifications` | 1 (prod) | initiatives (plus dev tooling)                                |
| `decidim-meetings`  | 1          | conferences                                                    |

Two implications:

1. **`comments` and `forms` are de-facto core infrastructure**, not just
   layer-1 modules. Half the components hard-depend on `comments`; nearly
   half on `forms`. The paper's classification (placing `comments` and
   `forms` alongside `admin`/`system`/`api`/`verifications` as "infrastructure
   engines") is correct as a label but understates how foundational they
   actually are — they sit between true infrastructure and the
   spaces/components layers.

2. **`decidim-conferences` (a space) runtime-depends on `decidim-meetings`
   (a component).** This breaks the paper's framing that "any component can
   attach to any space" via the manifest pattern (Section 4.1, "the
   space/component matrix"). Conferences hard-requires meetings; you cannot
   run a conferences space without the meetings component installed. The
   manifest-based composition the paper describes (Listing 1) handles
   *runtime* attachment, but here the dependency exists at the gem level.

### "Layered star" — half-true

It is layered, and most engines do depend on core. But the star has multiple
hubs. The accurate framing is something like:

- **Layer 0:** `decidim-core` — universal dependency.
- **Layer 1 (infrastructure):** `decidim-admin`, `decidim-api`, `decidim-system`.
- **Layer 2 (shared services that other engines depend on):**
  `decidim-comments`, `decidim-forms`, `decidim-verifications`.
- **Layer 3 (participatory spaces):** `assemblies`, `conferences`,
  `initiatives`, `participatory_processes`.
- **Layer 4 (components):** the rest.

Cross-engine runtime dependencies bypass core for the dependents in
Layer 2 (comments, forms, verifications) and one Layer 3 → Layer 4 case
(conferences → meetings).

### Manifest pattern — confirmed

`Decidim.register_component(...)` and `Decidim.register_participatory_space(...)`
calls are present in the expected places. `decidim-proposals/lib/decidim/
proposals/component.rb` matches Listing 1 in the paper. The manifest
pattern is real; the paper's description of how components register with
core is accurate.

## What this means for the paper

### Required edits

1. **Update the engine count** in Section 4.1 ("23 first-party engines" →
   "27, of which 24 are production engines"). Update the paragraph at
   line 191–192.

2. **Replace Figure 2** with the recovered version
   (`figures/decidim_dependency_graph.pdf`). The new figure shows 24
   engines across 5 layers and surfaces the cross-engine dependencies the
   old figure asserts do not exist. Caption notes that 3 dev tooling
   engines are omitted.

3. **Rewrite the "Dependency graph" paragraph** (line 194–196). Drop the
   "hub-and-spoke" / "layered star" framing. Replace with the multi-hub
   picture: most engines depend on core, but `decidim-comments` and
   `decidim-forms` are de-facto Layer-2 hubs that several components also
   runtime-depend on.

4. **Drop `sortitions`** from the list of nine components (line 192) — it
   does not exist in the current codebase.

5. **Confront the conferences → meetings dependency** as a paragraph.
   This is the "shared-DB tension" cousin: the manifest pattern is meant
   to make components and spaces independently composable, but at least
   one space hard-requires a specific component. Worth a sentence or two
   in Section 4.1 and a mention in the discussion of trade-offs (the
   "modifiability" claim is real but not absolute).

### Optional edits

- **Update the four interaction mechanisms** paragraph (line 295) if the
  shared-DB framing wants to be made tighter — the gem-level cross-engine
  deps are a fifth mechanism the paper does not name. Or fold them into
  the shared-DB discussion since both are forms of cross-engine coupling.

## Reproducibility

```
git clone --filter=blob:none https://github.com/decidim/decidim.git ~/Dev/decidim
cd ~/Dev/decidim && git checkout be39c244035485e2eba7181252aea487f5897cef
cd ~/Dev/report
python scripts/recover_decidim.py /home/leos/Dev/decidim
python scripts/make_decidim_graph.py
```

Output: `data/decidim_engines.json`, `figures/decidim_dependency_graph.pdf`.
