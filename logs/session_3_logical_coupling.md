# Session 3 log — Logical coupling on Decidim

**Snapshot:** `decidim/decidim @ be39c244035485e2eba7181252aea487f5897cef` (2026-05-12)
**Script:** `scripts/logical_coupling.py`, `scripts/make_coupling_heatmap.py`
**Data:** `data/decidim_coupling.json`
**Figure:** `figures/decidim_coupling.pdf`

## Method

Gall et al. 1998 — logical coupling. For each non-merge, non-bot commit,
identify which top-level `decidim-*` engines it touches. For every engine pair
(A, B):

- `co_changes` = number of commits touching both
- `jaccard` = co_changes / |commits touching A ∪ B|
- `p_b_given_a` = co_changes / |commits touching A| (asymmetric)

Filters: bots excluded (same rules as Session 2); mega-commits touching more
than 8 engines excluded (375 of 7,078, mostly release / refactor commits);
tooling engines excluded (`decidim-design`, `decidim-dev`, `decidim-generators`).

The hypothesis going in was the **shared-DB tension** the paper flags but
buries (line 298): if the manifest pattern fully isolates engines, gem-level
boundaries should produce module-level change patterns. If the shared
database, shared ActiveRecord associations, and shared base classes leak
through, engines should co-change despite the gemspec isolation.

## Headline stats

- 7,078 human commits (non-merge), 5,517 touched an engine.
- **3,525 commits (64%) are single-engine.** A clear majority of work stays
  inside one engine boundary. The architecture provides real, not nominal,
  isolation.
- 1,992 commits (36%) cross engine boundaries.
- 375 commits excluded as mega-commits (>8 engines touched). Sanity-checked
  by spot-reading: mostly version bumps and refactors that touch every
  gemspec.

## Findings

### The SPACES block: spaces are not independent

The strongest coupling in the entire matrix is among the four participatory
spaces:

| Pair                       | Jaccard | Co-changes |
|----------------------------|---------|------------|
| processes ↔ assemblies     | **0.43**| 264        |
| assemblies ↔ conferences   | 0.24    | 127        |
| processes ↔ conferences    | 0.19    | 119        |
| processes ↔ initiatives    | 0.13    | 101        |
| assemblies ↔ initiatives   | 0.14    | 100        |
| conferences ↔ initiatives  | 0.14    | 87         |

All six pairs of the four space engines co-change together at Jaccard ≥ 0.13.
The space abstraction (participatory_processes, assemblies, conferences,
initiatives) is **not implemented as a clean interface with four
independent realisations**. Common changes to one space type propagate
across the others — likely shared base classes, copy-pasted patterns, or
shared admin views.

This is a real architectural finding the paper currently misses. The
"space" concept is unified at the implementation level, even though it's
presented in the paper (Section 4.1, "the space/component matrix") as
four parallel spaces that components plug into. The four spaces look more
like four variants of one space, not four independent ones.

### The flagship component cluster

| Pair                       | Jaccard | Co-changes |
|----------------------------|---------|------------|
| proposals ↔ meetings       | 0.20    | 297        |
| budgets ↔ meetings         | 0.14    | 133        |
| proposals ↔ budgets        | 0.135   | 168        |
| debates ↔ meetings         | 0.12    | 103        |
| proposals ↔ debates        | 0.11    | (mid)      |
| blogs ↔ debates            | 0.15    | 40         |

The four most-used components (proposals, meetings, budgets, debates)
co-evolve. These are the components real deployments use together, and
they share UI patterns and notification flows. blogs ↔ debates is a smaller
but visible cluster.

These engines are NOT gemspec-related to each other (Session 1) yet
they co-change. This is the shared-DB tension empirically: gem-level
independence does not produce change-level independence when engines
share the same Rails application and the same database schema.

### Core and admin are the glue

- core ↔ admin: J=0.18, 647 co-changes
- core ↔ proposals: J=0.16, 580 co-changes
- core ↔ meetings: J=0.12, 437 co-changes
- admin ↔ proposals: J=0.10
- admin ↔ initiatives: J=0.11

Expected. Core API changes drive admin and flagship-component updates.
Admin is the centralised glue layer that touches every feature.

### What the gemspec deps do NOT predict

This is the counter-intuitive part. Session 1 found that `decidim-comments`
has 6 runtime dependents (accountability, blogs, budgets, debates,
initiatives, proposals) and `decidim-forms` has 5 (demographics, elections,
meetings, surveys, templates). But the coupling heatmap shows comments and
forms barely co-changing with most of their dependents:

- comments ↔ proposals: J=0.04 (low)
- comments ↔ debates: J=0.06
- forms ↔ surveys: J=0.16 (visible but moderate)
- forms ↔ meetings: J=0.05

This is **good architectural news**. comments and forms are real APIs that
their consumers call without needing to modify. The gemspec dependency
expresses "I rely on this gem", not "we evolve together". The fact that
proposals depends on comments at the gem level but rarely touches comments
in commits means the comments API boundary is stable and well-isolated.

### Refined picture

Three different mechanisms produce coupling, and the manifest pattern
handles them differently:

1. **API consumption** (comments, forms, verifications used by many engines)
   — gemspec deps high, logical coupling low. The pattern WORKS here:
   shared services with stable APIs.

2. **Shared implementation across siblings** (the four spaces)
   — no gemspec deps between siblings, but high logical coupling. The
   pattern FAILS here: the abstraction is unified at the source level.

3. **Use-together-in-deployments** (proposals/meetings/budgets/debates)
   — no gemspec deps, moderate logical coupling. The pattern partially
   works: features evolve together because real deployments combine them.

## What this means for the paper

### Strong new findings to write up

**Add a "Logical coupling" paragraph or short subsection** in Section 4.1
(after the dependency-graph paragraph) or as part of the Synthesis. ~half
a page plus the heatmap figure.

Key claims:

- The manifest pattern delivers real isolation for **API consumers**: 64%
  of human commits are single-engine; engines that depend on comments or
  forms via gemspec do not generally co-change with them.

- The manifest pattern does NOT deliver isolation across **sibling
  abstractions**. The four spaces (processes / assemblies / conferences /
  initiatives) co-change at Jaccard up to 0.43 — they share implementation
  at the source-code level despite being separate gems.

- The "space/component matrix" framing (line 263, "any component can
  attach to any space") is overstated. At runtime, components do attach
  freely via the manifest. But at the source level, the four "spaces"
  themselves are not independent realisations of a clean interface;
  they're variants of one shared implementation.

### Refines the paper's argument

- The **"modular monolith"** framing is still correct, but with a sharper
  characterisation: the modularity is at API boundaries, not at
  implementation. This is a more honest description than "23 isolated
  engines".

- The **shared-DB tension** (line 298) — currently a one-sentence
  observation — gets backed by data. Specifically: even when engines
  don't share a gemspec dependency, they share a database schema and
  shared base classes, which produces co-evolution that bypasses the
  module interface.

- The **trade-off framing** sharpens: Decidim trades full modular
  isolation for a unified-enough implementation that the four spaces
  remain consistent with each other. Pure modularity would mean four
  independent space implementations that could drift apart in behaviour.
  The current design accepts implementation coupling to keep behaviour
  consistent.

### Figure to add

`figures/decidim_coupling.pdf`. Heatmap, 24 engines × 24 engines, grouped
by role (core / infra / shared / spaces / components). The two visible
clusters on the diagonal (the SPACES block and the flagship-component
block) carry the story.

## Reproducibility

```
cd ~/Dev/report
python scripts/logical_coupling.py /home/leos/Dev/decidim
python scripts/make_coupling_heatmap.py
```

Outputs: `data/decidim_coupling.json`, `figures/decidim_coupling.pdf`.
