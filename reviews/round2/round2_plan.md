# Round 2 review plan

Plan for the second review pass. Round 1 (reviews `00`–`06` in this folder) was run before the empirical work on the `empirical-rework` branch. Round 2 reviews the paper after Sessions 1–4 have been folded in and the Method section has been rewritten.

## Three-phase workflow

1. **Phase 1 — Substantive review.** 9 agents in parallel (sections, citations, figures, overall). Harsh examiner tone. Output to `reviews/round2/`.
2. **Phase 2 — Implementation.** LSA + agents fold the Phase 1 feedback into the paper. Paper changes significantly.
3. **Phase 3 — Voice and compliance pass.** 2 agents in parallel — voice/concision copy-edit, and ITU formal-requirements check. Runs *after* Phase 2 so we're not copy-editing prose that's about to change.

This document covers all three phases. Readiness criteria below apply to Phase 1.

## Readiness criteria — three checkboxes before launch

Don't launch mid-edit. Round 2 starts when all three are true:

- [ ] Sessions 2, 3, 4 findings folded into Section 4 (the Decidim §4.1 fold is in progress; Consul §4.2, Polis §4.3, and synthesis §4.4 still ahead).
- [ ] The four trade-offs are named identically across abstract, §2, §4.4 table, §5, and §6.§2, §4.4 table, §5, and §6.
- [ ] FAccT 2025 cite resolved — either added to `references.bib` or the Method reference to it is removed.

LSA gives the explicit "go" signal once these hold.

## Phase 1 — Substantive review (9 agents in parallel)

| # | Owner | Section | Output file |
|---|---|---|---|
| 1 | Introduction reviewer | §1 (intro) | `reviews/round2/01_introduction.md` |
| 2 | Background reviewer | §2 (background) | `reviews/round2/02_background.md` |
| 3 | Method reviewer | §3 (method) | `reviews/round2/03_method.md` |
| 4 | Analysis reviewer | §4 (analysis, all subsections) | `reviews/round2/04_analysis.md` |
| 5 | Discussion reviewer | §5 (discussion) | `reviews/round2/05_discussion.md` |
| 6 | Conclusion reviewer | §6 (conclusion) | `reviews/round2/06_conclusion.md` |
| 7 | Citations / claims-to-citations reviewer | whole doc, citation-level | `reviews/round2/07_citations.md` |
| 8 | Figures reviewer | every figure + caption + figure↔prose match | `reviews/round2/08_figures.md` |
| 9 | Overall reviewer | whole doc, paper-level | `reviews/round2/00_overall.md` |

All 9 run in parallel, no agent reads another's review during their pass.

## Shared briefing block — every agent gets this

Each agent's prompt opens with this context (paraphrase, not boilerplate):

- Master's student Research Project (7.5 ECTS, MSc Software Design, IT University of Copenhagen).
- Supervisor is Konstantinos Manikas, who teaches Software Ecosystems at ITU. SECO health is the centre of gravity, not architectural recovery. Don't critique against an architecture-recovery dissertation.
- The paper has been through one round of revision since the round-1 reviews. Substantial empirical work was added on the `empirical-rework` branch:
  - **Session 1** (`logs/session_1_decidim_recovery.md`) — Decidim gemspec recovery, 27 engines not 23, cross-engine deps, sortitions removed.
  - **Session 2** (`logs/session_2_evolutionary.md`) — contributor concentration + commit timelines for all three repos; Madrid 2019 cliff visible.
  - **Session 3** (`logs/session_3_logical_coupling.md`) — coupling heatmap, shared-DB tension empirically.
  - **Session 4** (`logs/session_4_consul_forks.md`) — Consul fork divergence, Madrid as most-diverged fork.
- Tone: harsh examiner. Same as round 1. Don't soften.

## Round-1 comparison protocol — read in this order

To get fresh eyes plus continuity without anchoring:

1. Read the section assigned, form an independent assessment, draft the review.
2. *Then* open the round-1 review file (`reviews/0N_*.md`).
3. For each round-1 finding, mark one of: **addressed**, **unaddressed**, or **obsolete** (paper changed underneath it).
4. Add a short "Round-1 follow-up" section at the bottom of the round-2 review with the marked list.

## Cross-reference checklist — the new piece this round

Each section agent gets the subset of these that applies to them. The overall agent runs all of them.

- **Four trade-offs naming.** Identical names in abstract, §2 (where introduced), §4.4 (synthesis table), §5 (discussion), §6 (conclusion)?
- **Promise → delivery → reflection → return.** Claims raised in §1 delivered in §4, reflected in §5, returned in §6?
- **Method ↔ Analysis match.** Does each procedure described in §3 produce the artefacts §4 cites? Does §4 use a move §3 doesn't describe?
- **Snapshot dates and SHAs.** Decidim `be39c244` (2026-05-12), Consul on `consuldemocracy/consuldemocracy`, Polis SHA — consistent everywhere they're mentioned (Method, §4, captions, log references)?
- **Figure references.** Every `\ref{fig:...}` resolves, every figure is referenced in prose, prose around each figure actually describes what the figure shows.
- **Session log findings ↔ paper claims.** Does the paper accurately reflect what the logs actually measured? No invented numbers, no exaggeration.
- **Repo rename.** Consul → `consuldemocracy/consuldemocracy` everywhere. The old `consul/consul` name flagged in Session 4 log should not survive in §4.2 or Table 5.
- **Stale entity names.** `sortitions` should be gone except where the paper explicitly notes "removed 2025-11-19" as a finding.

## Per-section brief outlines (skeleton)

These are skeletons — each one becomes a full prompt when we launch. Each brief follows the same shape: section + line range, four review lenses (argument & rigor, clarity & structure, writing style, academic conventions) + the cross-reference subset relevant to that section.

### 1. Introduction (§1)
Focus: does the intro promise things the empirical work now delivers? Are the platform stats (Decidim's 450 institutions, Polis's 200k participants, Consul's 250 cities) properly cited? Does the RQ still match the paper, or has the paper drifted past it? Borgerforslag.dk strawman from round 1 — addressed?

### 2. Background (§2)
Focus: does §2.3 perform the SA + SECO + STS synthesis or just announce it (round-1 finding)? Are the SECO concepts the analysis now uses (logical coupling, fork divergence, contributor concentration) introduced here? Is Christensen 2014 used substantively, not just dropped? Is the four-trade-offs framing introduced consistently with how §4.4 names them?

### 3. Method (§3)
Focus: each of the 8 `\paragraph` blocks describes a real procedure that §4 actually uses. SHAs and dates current and match §4. Asymmetric-depth acknowledged up front (round-1 critical issue). Logical coupling, fork divergence, evolutionary procedures cited to their methodological tradition.

### 4. Analysis (§4)
Focus: each subsection uses the Session 1–4 findings appropriately. Causal claims hedged. Shared-DB tension engaged as a finding, not skipped. §4.4 trade-offs framed as "specified up front, observed in cases" not "discovered." §4.2 Consul presented honestly as literature-based comparison + fork divergence empirical (not pretending to Decidim's depth). §4.3 Polis asymmetric depth flagged.

### 5. Discussion (§5)
Focus: does it interpret what §4 produced, or restate it? §5.1 governance-in-practice — earned from data, not assumed? §5.2 SECO contribution — concrete? §5.3 policy implications — grounded in findings, or unsupported leaps? §5.4 limitations — honest about Madrid political confound, single-coder, anglophone bias?

### 6. Conclusion (§6)
Focus: does it answer the §1 RQ? Does it introduce claims not earned in the body? Future work concrete or generic? GenAI disclosure honest and specific?

### 7. Citations (whole doc)
Focus: every empirical claim cited where appropriate. Session log findings cited correctly when paraphrased into the paper. Orphan citations in `references.bib` (DeNardis, Weyl, Roy, Aragon, Behrendt per round 1) — used or dropped. FAccT 2025 cite resolved. Repo URLs use current names. No grey-lit paraphrased without source.

### 8. Figures (whole doc)
Focus: every figure earns its place. For each figure: caption tells a complete-enough story to read standalone; prose around the figure describes what the figure actually shows (not a vague gesture); every `\ref{fig:...}` resolves; legends and axes readable. Specifically check the empirical figures from Sessions 1–4: dependency graph (Session 1), evolutionary plots (Session 2), coupling heatmap (Session 3), fork-divergence + fork-activity (Session 4). Flag any decorative figure not pulling argumentative weight.

### 9. Overall (whole doc, paper-level)
Focus: argument arc end to end. The full cross-reference checklist (all items, not subset). One-sentence contribution. Voice consistency. Paper-level AI-slop patterns. Drift map (anywhere the abstract, intro, analysis, discussion, conclusion say slightly different things about the same idea). Honest assessment: what is the paper *now*, vs round 1?

## Output structure (each round 2 review file)

Standard shape, same across all 8:

1. **Verdict** (3–8 lines) — the most important takeaway.
2. **Four lens findings** — argument & rigor, clarity & structure, writing style, academic conventions. Line-numbered quotes.
3. **Cross-reference findings** — the subset of the checklist that applies. Each one resolved or flagged.
4. **Round-1 follow-up** — marked list of round-1 findings: addressed / unaddressed / obsolete.
5. **Prioritized fix list** — top 5–12 items ordered by impact.

Target length: same as round 1 — 400–900 words for most sections, 1000–1600 for Analysis, 1200–2000 for Overall.

## Phase 1 launch sequence (when LSA says go)

1. Verify the three readiness checkboxes hold.
2. Read main.tex once, capture current state to brief the agents accurately (line ranges, current SHAs in the doc, current trade-off names, current synthesis table layout).
3. Build the 9 agent prompts from the skeletons above + current-state info.
4. Launch all 9 in parallel in one message.
5. Wait for results, summarize headline findings to LSA.

## Phase 3 — Voice and compliance pass

Runs *after* LSA implements the Phase 1 feedback (Phase 2). Two agents in parallel — they check orthogonal things.

### A. Voice and concision agent

**Purpose:** copy-edit pass for register, AI-slop detection, and verbosity cuts. NOT substance review.

**Calibration target:** the writing memory at [[feedback-writing-style]]. The existing main.tex prose is the register to match — plain, direct, student voice. No fancy synonyms when a plain word fits.

**What to flag — quote line and offer a replacement:**

- AI-slop adjectives doing no work: *comprehensive*, *robust*, *seamless*, *powerful*, *carefully crafted*, *intuitive*, *intricate*, *significant* when it just means "real," *novel* when the thing isn't.
- Wind-ups: *It is worth noting that*, *Let me walk you through*, *I would like to highlight*.
- Wrap-ups: *In summary*, *To conclude*, *Hopefully this helps*, *This paper has shown*.
- Em-dash overuse as a generic punctuation crutch (especially three em-dashes in one sentence).
- Bolded-bullet labels (`- **The Thing**: did the thing`).
- Triple-nested bullets for points that fit in one sentence.
- Comma-spliced paragraphs piling three ideas in one line.
- Fancy words where a plain one would do (*utilize* → use, *leverage* → use, *facilitate* → help, *demonstrate* → show, *indicate* → show).
- Restating the same idea in different words across sentences.

**Output format:** `reviews/round3/voice.md`. For each flagged passage:
- Line number
- Quote the offending phrase
- Suggested replacement (or "cut")
- One-line reason

Aim for surgical edits, not full rewrites. The paper's voice is mostly already good — this is a cleanup pass, not a translation.

### B. ITU formal-requirements / compliance agent

**Purpose:** check the paper against the formal requirements of the MSc Software Design Research Project (KIREPRO1PE) at ITU.

**Inputs to read (all under `/home/leos/Nextcloud/Leo/ITU/4th Semester - Research Project/Andet/Guidelines-and-requirements/`):**

- `Especially about the Research project.pdf` — the most important document; format, scope, deliverables for the Research Project specifically.
- `project_guide.pdf` — general project guide.
- `Workload and Project Size.pdf` — page-count and workload expectations.
- `Submitting written work.pdf` — submission format requirements.
- `Checklist and advice for project and theses.pdf` — explicit checklist items.
- `Problem Statement.pdf` — what counts as a well-formed problem statement.
- `Curriculum-for-MSc-in-Software-Design...pdf` — program-level requirements (Section on Research Project).
- `Section_ Research Project Spring 2026 ... learnIT.pdf` — the course page for Spring 2026 specifically.
- `howto_research.md` — methodological expectations (markdown version, easier for the agent to digest than the PDF).

**What to check:**

- Page count or word count against stated limits (7.5 ECTS Research Project size).
- Required sections present and properly named.
- Problem statement / research question form (checked against the *Problem Statement* guide).
- Bibliographic format and citation style.
- Submission format requirements (PDF, file naming, deadline format).
- Use-of-AI declaration form and content.
- Supervisor and contact-information fields.
- Anything explicitly required that the paper currently misses.

**Output format:** `reviews/round3/compliance.md`. Pass-fail-fix per requirement:

- Each requirement on one line: ✓ / ✗ / partial.
- For each ✗ or partial: what the requirement is, where the paper falls short, what the fix is.
- A short top-level verdict: how close to compliant is the paper, what's the single most important thing to fix.

**Tone:** factual, not harsh. This is checking against a rubric, not making judgements.

## Phase 3 launch sequence

1. LSA signals Phase 2 implementation is complete and paper is near-final.
2. Launch the two Phase 3 agents in parallel in one message.
3. Wait for results, summarize to LSA, queue Phase 4 (final fixes + submission).

## Decision log

- 2026-05-12 — Plan drafted. 8 agents originally, parallel, harsh examiner tone. Round-1 comparison protocol = read section first, then check against round 1 (avoid anchoring). Overall agent runs in parallel, not first or last.
- 2026-05-12 — Added 9th agent for figures (separate from per-section). Resolves the round-1 open question.
- 2026-05-12 — Three-phase workflow added. Phase 3 = voice/concision agent + ITU compliance agent, runs after LSA implements Phase 1 feedback. Voice agent uses the [[feedback-writing-style]] memory as calibration target. Compliance agent reads the ITU guidelines folder.
