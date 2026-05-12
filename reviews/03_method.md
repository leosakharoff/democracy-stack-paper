# Review: Section 3 — Method

## Verdict

The method is a 17-line gesture, not a procedure. It names the right vocabulary (architectural recovery, decisions, quality attributes, SECO health) but never says what was actually done — no inclusion criteria, no recovery protocol, no coding scheme for "key decisions," no GitHub-metric definitions. Case selection is the strongest part; the "deep + comparison + contrast" design is mostly post-hoc labeling. Replicability is near zero. Limitations are deferred to §7. For a 7.5-ECTS paper this is defensible only if the method is honest about being thin; right now it oversells.

## 1. Argument and rigor

The Decidim/Consul shared-origin angle (l. 175) is the strongest methodological move in the paper. Polis as "contrasting paradigm" also lands. But the section never explains why these three rather than Loomio, CitizenLab, Demos, or vTaiwan. "The most architecturally rich civic tech platform available" (l. 175) is asserted without survey evidence; no inclusion/exclusion criteria exist. "Deep + comparison + contrast" is a label, not a design — Yin, Stake, Eisenhardt are not cited, so the three-tier asymmetry reads as justification for unequal coverage rather than a designed comparison.

Architectural recovery is hand-waved. Line 171 lists "codebase structure, dependency files, extension mechanisms, API boundaries, and official documentation" — *inputs*, not a *procedure*. Nothing on how the codebases were navigated (manual reading? static analysis? commit-log mining?), what counted as a "boundary," or how code/docs conflicts were resolved. The recovery literature (Garcia, Ducasse, Murphy) is absent. Same problem for trade-off identification: "we trace consequences for quality attributes using the framework of \citet{bass2021software}" (l. 171). How? ATAM and SAAM exist for this and are not mentioned.

"To the best of our knowledge" (l. 98, l. 118) is load-bearing for the contribution claim, but the method describes no literature search. At this length unavoidable, perhaps — then soften the scope claim instead of repeating it.

Method/analysis mismatch. The method promises "contributor distribution, fork activity, and module-level commit patterns" (l. 171). The analysis delivers approximate star/fork counts (Table \ref{tab:ecosystem}) and one borrowed Cobos2025 citation (l. 330). No contributor-distribution, no commit-pattern, no bus-factor calculation by the authors. Conversely, the analysis uses moves the method never sets up — the registration listing (Listing 1), the dependency graph (Fig. 2), the polymorphic-association claim (l. 264) — recovery artifacts that should be flagged as outputs of step 1.

## 2. Clarity and structure

A reader cannot extract the procedure in one read. Para 1 (l. 169) lists four steps. Para 2 (l. 171) re-states them with a fifth (SECO metrics). Para 3 (l. 173) is a scoping aside; para 4 (l. 175) case selection; para 5 (l. 177) data sources; para 6 (l. 179) a limitations placeholder. Data sources, analytical procedure, and reporting structure are not cleanly separated. The deep/comparison/contrast reporting structure is implicit in para 4 but never named as a methodological choice.

## 3. Writing style

Plain register, no wind-ups or wrap-ups. Three flags:

- "lightweight architectural recovery" (l. 169, l. 171) — does double duty as hedge and method label. Define it or drop it.
- "the most architecturally rich civic tech platform available" (l. 175) — empty superlative; back with a survey or cut.
- "approximates (but is not) a natural experiment" (l. 175) — safety-blanket hedge; commit to the comparative framing or don't.

## 4. Academic conventions

- Tradition: none for case study (no Yin, Stake, Eisenhardt). One ADR cite (Tyree 2005). Bass 2021 for QAs. No ATAM/SAAM. No recovery literature.
- Unit of analysis: undefined — platform? codebase snapshot? ecosystem? decision? The paper drifts.
- Positionality: not addressed. Single coder, no reflexive note.
- Temporal scope: "as of May 2026" sits in the analysis (l. 330, 384), not the method. No SHAs, no access dates.
- Replication package: not mentioned.

## Method-section essentials checklist

| Item | Status |
|---|---|
| Research design named (multi-case) | Present |
| Case-selection rationale | Partial — Decidim/Consul yes; why-not-others missing |
| Inclusion/exclusion criteria | Missing |
| Unit of analysis defined | Missing |
| Data sources listed | Present (l. 177) |
| Data collection procedure (access, snapshot dates, SHAs) | Missing |
| Architectural recovery procedure | Missing — only inputs listed |
| Coding/identification of "key decisions" | Missing |
| Trade-off procedure (ATAM/SAAM or own) | Missing |
| Cross-case comparison criteria | Partial — appear in Table 2, not pre-registered |
| GitHub-metric operationalization | Missing — promised but undefined |
| Methodological tradition cited (Yin etc.) | Missing |
| Architectural-recovery literature cited | Missing |
| Positionality / researcher bias | Missing |
| Limitations stated in section | Deferred to §7 (l. 179) |
| Replication artifacts | Missing |

## Prioritized fix list

1. Define the recovery procedure — which files were read, what was logged (engines, dependencies, manifest calls, routes), how code/doc conflicts were resolved. Cite at least one recovery source.
2. Operationalize the GitHub metrics or drop them. Define the queries, or scope down to headline indicators (stars, forks, deployments).
3. State case-selection criteria. One paragraph: eligibility, why Loomio/CitizenLab/Demos were excluded, basis for "most architecturally rich."
4. Anchor in a tradition. Cite Yin for case-study design and ATAM/SAAM for trade-off analysis; flag this as a lightweight variant.
5. Pin the snapshot. Record commit SHA or tag and access date per repo. Move "as of May 2026" into the method.
6. Name the unit of analysis, state the reporting structure (deep/comparison/contrast) as a methodological choice, and add a one-sentence positionality note. Surface §7's limitations here in two sentences instead of deferring.
