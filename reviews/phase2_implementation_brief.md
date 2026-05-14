# Phase 2 implementation brief

Output of the Phase 2 planning session (LSA + Peter, 2026-05-13 morning). Round 2 reviews (`reviews/round2/`) surfaced a long list of issues; this brief separates the **judgment calls that LSA already made** from **mechanical fixes the round-2 reviews can drive directly**.

Source of truth for issue details: `reviews/round2/00_overall.md` through `08_figures.md`. This brief does not restate them — it adds the four decisions and sequences the work.

## Four locked decisions

These have been decided. Propagate consistently across the document.

### Decision 1 — drop to **3 trade-offs**

Replace the four-trade-off framework with three. The fourth pair ("deployability vs. transparency / transparency vs. ecosystem breadth") was carrying a tautology ("transparency" doing two jobs as both QA and cost) and the deployability/opacity pair was the weakest of the four. The three remaining trade-offs are clean architectural laws.

**Canonical names (verbatim, do not paraphrase):**

1. **Modifiability ↔ sustainability burden**
2. **Interoperability ↔ reduced autonomy**
3. **Algorithmic depth ↔ ecosystem breadth**

**Where this propagates:**

- Abstract (line 98) — rewrite the trade-offs sentence.
- Introduction (line 120) — rewrite the QA-list sentence.
- Method §3 paragraph 6 (around line 187) — rewrite the QA scope paragraph. Drop "deployability, transparency" from the QA list; frame the three as "architectural tensions specified up front from the architecture-as-governance literature."
- §4.5 synthesis table (lines 441–455, `tab:tradeoffs`) — drop the Deployability and Transparency rows. Replace with a single new row for **Algorithmic depth ↔ ecosystem breadth** (evidence: Polis vs. Decidim — Polis Bjorkegren 56%, Polis 79 authors / 97% top-10 vs. Decidim 183 authors / 68% top-10; coupled with Polis's tightly coupled algorithmic architecture and Decidim's modular but algorithmically shallow architecture).
- §4.5 positioning figure (`fig:tradeoffs`, around line 138 in main.tex, source in `figures/`) — currently plots Modifiability vs. Deployability. Replot as Modifiability vs. Algorithmic depth (this also separates the three cases more cleanly: Decidim modular+shallow, Polis monolithic+deep, Consul monolithic+shallow).
- §5 Discussion — references to "four trade-offs" → "three trade-offs"; the Polis discussion at §5.1 should explicitly reference trade-off 3.
- §6 Conclusion (line 505) — rewrite the trade-offs list sentence; only 3 costs.

**Deployability survives in the body as a descriptive observation** (Polis is Docker-easy, Decidim is 27-gem complex). It is no longer a primary axis. Don't claim it as a trade-off; do mention it as a consequence of architectural choices in the relevant case sections.

**Transparency survives as a downstream concern** (Polis's opaque PCA, Decidim's readable modules) but not as a primary QA. It is now a *consequence* of trade-off 3 (algorithmic depth choices produce opacity downstream).

**Suggested abstract phrasing** (work from this, do not copy verbatim if the prose feels stilted):

> "The analysis surfaces three architectural trade-offs that function as governance decisions: modifiability against sustainability burden, interoperability against reduced autonomy, and algorithmic depth against ecosystem breadth."

### Decision 2 — Decidim/Consul refrain: **3 mentions total**, Madrid 12,725: **2 mentions total**

The "Decidim and Consul, same origin, opposite architecture" claim appears ~10× across the paper after round 2. The Madrid-12,725-commits-ahead detail was added in 4+ more places. Cut to the bone.

**Decidim/Consul "same origin, opposite architecture" — 3 mentions, no more:**

1. Abstract — one-line setup.
2. Introduction (around line 122 currently) — the comparison framing as the central evidentiary claim.
3. §4.2 Consul case — where the evidence is delivered.

After these three, refer to "the divergence we showed" or "the two-platform comparison" without restating "same origin, opposite architecture." Specifically remove or rewrite the appearances in §4.5, §5.1, §6 (currently each restates the refrain).

**Madrid 12,725-commits-ahead — 2 mentions, no more:**

1. §4.2 Consul case — where the evidence is presented and contextualized.
2. §5.1 Discussion — where it neutralizes the "outsider deployers were less capable" objection (the Discussion reviewer flagged this as the strongest single move in §5).

Drop from abstract and §6 conclusion (where it currently appears). The abstract's "Madrid sentence" is also grammatically broken — cut entirely rather than rewrite.

### Decision 3 — §5.2 SECO contribution: **propose fork-divergence shape as a niche-creation diagnostic**

§5.2 currently asserts that SECO health metrics need a normative axis but proposes no concrete metric. Round-2 Discussion reviewer flagged this as "still a slogan."

**The concrete claim to add:**

Standard SECO niche-creation metrics count contributions; they do not distinguish healthy ecosystem extension from silo formation. The Consul fork data shows the shape: 1,030 forks, 280 modified, but the *ahead-only quadrant is empty* — zero forks added work while keeping up with upstream. Healthy niche creation populates the top-left of the ahead/behind plot. Silo formation populates the bottom-right (abandoned) and top-right (diverged, stale).

**Proposed addition to §5.2** (work from this, rewrite in LSA's voice):

> "Standard SECO niche-creation metrics count contributions; they do not distinguish healthy ecosystem extension from silo formation. We propose **fork-divergence shape** — the population pattern across the ahead/behind quadrants — as a niche-creation diagnostic for civic tech platforms. Consul's L-shape (empty top-left, populated bottom-right and top-right) is the signature of an ecosystem that fragments instead of extending."

This grounds the SECO contribution in measurable empirical material the paper already produced. It also speaks the supervisor's language directly (niche-creation is Iansiti/Manikas vocabulary).

Reference `figures/consul_fork_divergence.pdf` from §5.2 (this also resolves one of the orphan figures flagged in `reviews/round2/08_figures.md`).

### Decision 4 — §5.3 cut to **2 lessons** + substantive IDEA/CEPS engagement

Current §5.3 has four lessons; round-2 Discussion reviewer found two unearned, one structurally obsolete (it relied on the deployability/transparency trade-off we just dropped), and one earned. Restructure to two earned lessons that map to two of the three trade-offs.

**The two lessons to keep:**

1. **Modular over monolithic** — earned from trade-off 1 (Decidim/Consul comparison). Modularity let communities adapt the platform; the monolith forced forking and fragmentation. The Madrid 12,725-commits-ahead fork is the strongest single illustration (already cited in §5.1 per Decision 2).

2. **Algorithmic depth vs. ecosystem breadth requires a deliberate choice** — earned from trade-off 3 (Polis vs. Decidim). If the democratic problem requires deep algorithms (consensus discovery in large groups), accept the thin ecosystem and centralised expertise. If it requires broad participation across many institutional contexts, accept simpler computation. The two cannot be optimized simultaneously without making one a façade.

**Cut from §5.3:**

- The "interoperability standards should be open but not ignore local variation" lesson — not demonstrated in §4.
- The "deployability matters but not at cost of transparency" lesson — based on the trade-off pair we just dropped.
- The "governance structure should match architecture" lesson — not demonstrated; would need separate evidence the paper doesn't gather.

**Engage IDEA/CEPS substantively (not just name-drop):**

Current text at line 483 says they "neither specifies what good architecture looks like in this context." Better: name what IDEA leaves implicit and what CEPS doesn't address. Suggested framing (rewrite in LSA's voice):

> "International IDEA calls for a democracy stack but leaves the architectural decisions implicit. CEPS advocates for interoperability but does not engage the modifiability/sustainability trade-off. Our two lessons surface specific architectural commitments any such stack has to make..."

This makes §5.3 a contribution to the policy conversation, not a critique of it.

## Mechanical fixes from the round-2 reviews

Each item below is sourced from a specific round-2 review file. Carla can work down the list. Source file in parentheses.

### Citations (`reviews/round2/07_citations.md`)

- [ ] Polis 200,000 participants / 26 pieces of legislation (intro line 114) — add a vTaiwan or Polis-specific citation, OR remove the specific numbers.
- [ ] DESI / UN E-Gov rankings (line 110) — currently footnote-only. Add proper `references.bib` entries, switch to `\cite{...}`.
- [ ] Five orphan citations in `references.bib`: `denardis2009protocol`, `weyl2025plurality`, `roy2025conversation`, `aragon2017deliberative`, `behrendt2025supporting`. Either use them where they fit (DeNardis would fit in §2.3, Aragón fits in §4.1 on Decidim) or drop from the bib.
- [ ] Symphony attribution at line 495 cites `tyree2005architecture` (ADRs), not the Symphony recovery paper. Either add the Symphony cite or rephrase to "Symphony-style" without the citation.
- [ ] Repo names: scan for any stale `consul/consul` references — currently the only legitimate uses are in the explicit "formerly known as" rename sentences. Other uses should be `consuldemocracy/consuldemocracy`.

### Snapshot SHAs (`reviews/round2/03_method.md`)

- [ ] Add Consul (`3c3b5c4a`) and Polis (`e8c2b46d`) SHAs to §3 paragraph 8 (data sources). The §4.5 table caption currently references "SHAs listed in Section 3" but only Decidim's SHA is there.

### Figures (`reviews/round2/08_figures.md`)

- [ ] `tensions.pdf` — labels say "23 Rails engines" and "~250 diverging forks". Re-render with 27 engines and the corrected fork counts (1,030 total / 280 modified), OR remove the numbers from the figure labels.
- [ ] `decidim_engine_activity.pdf` — orphan figure. Reference it from §4.1 around the "modular architecture, modular maintenance" claim.
- [ ] `consul_fork_divergence.pdf` — orphan figure. Reference it from §5.2 (the new SECO contribution per Decision 3 above) — that single move fixes both the orphan figure and the slogan-level SECO claim.
- [ ] Line 313 fixes the figure-vs-prose mismatch: prose says "fork creation peaked in 2019" but the figure plots last-push year. Either change the prose to "fork *activity* peaked in 2019" (matches the figure) or replot to actual creation-year (matches the prose).
- [ ] `fig:matrix` (around line 270 — the components×spaces filled-circle table) is from the Barandiaran handbook, not measured. Caption should own that ("reproduced from Barandiaran et al. 2024") or cut.
- [ ] `fig:contributor-concentration` caption — name what the three bar segments encode (top-3, top-4-10, rest).
- [ ] `fig:consul-forks` caption — define what each bar counts (forks last-pushed in year X).

### Specific text fixes

- [ ] Abstract Madrid sentence is grammatically broken ("The fact that Madrid ... sharpens the point"). Cut per Decision 2 (Madrid moves to §4.2 + §5.1 only).
- [ ] Intro should name Knutas — §2.2 names him, but intro still hedges as if author hadn't seen Knutas. Either name in intro or drop the "to the best of our knowledge" softener.
- [ ] Intro RQ at line 120 runs on as two questions joined by "and." Pick the primary one and make the second a sub-question or drop.
- [ ] Line 279 denominator: "64% of 7,078 human commits" → "64% of engine-touching commits" (5,517). Same for the surrounding sentences if they repeat the denominator.
- [ ] §4.5 — three sorting tables where round 1 asked to cut one. Pick one to consolidate or cut.
- [ ] §4.5 two causal slips: line 397 ("produced") and line 457 ("the architecture is the governance decision") — hedge to match the explicit confound acknowledgement at line 422.
- [ ] §6 "clearest demonstration" line — currently appears 5×. Cut to ≤2 per Decision 2.
- [ ] §6 introduces two arguments not earned in body: "architecture is not a procurement detail" and the SECO normative-axis upgrade. Either set up in §5.3/§5.2 first, or cut from §6.
- [ ] §7 GenAI: "figure generation" — be specific about the matplotlib code-generation that's visible in commit history; "summarizing arguments" sits in mild tension with the author-only analytical claim — clarify the scope.

### §5.4 limitations to add (`reviews/round2/05_discussion.md`)

Four limitations currently missing:

- [ ] Single coder (no inter-rater check on the case classifications).
- [ ] Anglophone bias (the sources we consulted are mostly English).
- [ ] Decidim-weighted sample (analytical depth biased toward the deep case).
- [ ] Selection on the dependent variable (we chose platforms that exist, not platforms that failed before reaching production).

## Things LSA does, not Carla

- Final voice pass after Carla's implementation (Phase 3 voice agent helps).
- The Iansiti keystone/dominator/niche-creator framing — §2.4 sets it up but §5 never returns. LSA decides whether to (a) close the loop in §5.1 by typing Decidim as keystone-aspirant and Consul as failed-keystone-becoming-dominator, or (b) cut the §2.4 setup. Recommendation: (a) — close the loop in one paragraph at the start of §5.1; it speaks the supervisor's language directly.
- The §2 three-structure hypothesis — currently introduced in §2.2, never gets a verdict. LSA decides whether to (a) add a closing sentence to §4.5 or §5.1 that delivers the verdict, or (b) downgrade the hypothesis to a framing in §2.2.

## Order of operations

Carla's recommended sequence:

1. **Big structural decisions first** — implement Decisions 1, 2, 3, 4 in that order. These touch multiple sections; doing them first means the smaller fixes don't have to be reversed.
2. **Then mechanical citation and SHA fixes** — these are scoped and independent.
3. **Then figure fixes** — some figures reference text that the structural decisions changed (e.g., the `fig:tradeoffs` replot needs the new trade-offs locked first).
4. **Then specific text fixes and §5.4 limitations** — last because they're the smallest items.
5. **Self-review against `reviews/round2/`** — after the implementation pass, walk through each round-2 review file and mark which items are addressed.

LSA does the final voice pass after Carla signals done.

## Source of truth

- Round 2 reviews: `reviews/round2/`
- Round 2 plan and Phase 3 agent specs: `reviews/round2_plan.md`
- Session logs (the empirical work behind every number in the paper): `logs/session_1..4_*.md`
- Writing-style and supervisor-focus context: in the agent's auto-memory, summarized as "plain student voice, no AI-slop, SECO not architectural recovery."
