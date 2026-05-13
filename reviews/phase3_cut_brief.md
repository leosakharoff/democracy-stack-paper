# Phase 3 cut brief — boil to 17–19 body pages

After Phase 2 implementation, the paper is 26 PDF body pages / ~30 ITU standard pages, against an ITU target of 15–19 body pages for 7.5 ECTS solo. LSA has decided to attempt a cut rather than ask for supervisor sign-off on over-length.

**Target:** body word count from ~9,560 → ~7,000 words. Cut ~2,500 words, roughly 26%.

**Source of truth for issue details:** `reviews/round3/voice.md` (47 voice flags, mostly em-dash and restatement — many of these *are* the cuts) and `reviews/round3/compliance.md`.

## Per-section word budgets

| Section | Current | Target | Cut |
|---|---|---|---|
| §1 Introduction | 700 | 550 | -150 |
| §2.1 SA for Democratic Infrastructure | 382 | 280 | -100 |
| §2.2 Software Ecosystems and Civic Tech | 377 | 280 | -100 |
| §2.3 Architecture as Governance | 245 | 190 | -55 |
| §3 Method | 1,175 | 750 | -425 |
| **§4.1 Decidim** | **1,501** | **1,000** | **-500** |
| §4.2 Consul | 899 | 650 | -250 |
| §4.3 Polis | 469 | 450 | -20 |
| §4.4 Ecosystem Evolution | 442 | 400 | -40 |
| §4.5 Synthesis | 526 | 450 | -75 |
| §5.1 Architecture as Governance in Practice | 587 | 450 | -140 |
| §5.2 SECO Research Gains | 464 | 400 | -65 |
| §5.3 Implications | 317 | 300 | -15 |
| §5.4 Evaluating the Approach | 628 | 450 | -180 |
| §6 Conclusion | 847 | 500 | -350 |
| **Total** | **9,559** | **7,100** | **-2,459** |

Word counts are LaTeX-stripped approximations (commands removed). Pad ±10% per section is fine if it preserves the argument.

## What to cut, by priority

### Tier 1 — biggest single targets

**§4.1 Decidim (cut 500 words):**
The longest section. Engine-recovery and dependency-graph prose has mechanical detail that can compress without losing the load-bearing findings. Specifically:
- The engine-list paragraph (line 211 onward) — 27 engines listed by name is fine, but the four-group taxonomy can be a sentence rather than a paragraph each.
- The dependency-graph paragraph naming all 13 cross-engine dependencies — keep the *summary* (comments has 6 dependents, forms has 5, conferences→meetings is the architectural surprise), drop the long enumeration of dependents.
- The Listing 1 explanation can be tighter.
- "Three structural patterns" intro framing — combine paragraphs that restate the same setup.

**Keep:** 27 engines, cross-engine deps with comments/forms as de-facto hubs, conferences→meetings counter-example, shared-DB tension at l.298 area, 64% single-engine commit rate, coupling heatmap finding (4 spaces at J=0.43), three-coupling-mechanisms framing.

**Method (cut 425 words):**
Deliberately expanded in Phase 2 to fix round-1's "too thin" critique. Now overcorrected. Specifically:
- Paragraphs 1 (overview) and 7 (asymmetric design) overlap on the asymmetric-depth point. Merge.
- Paragraph 8 (data sources and limitations) has limitation prose that belongs in §5.4 or is repeated in §5.4. Cut the duplicates.
- Each procedure paragraph can be one tight paragraph rather than verbose. The Logical Coupling paragraph (l.180) is already a good model — emulate that compactness for Architectural Recovery and Evolutionary Analysis.

**Keep:** the eight-paragraph structure (case selection, recovery, evolution, coupling, fork divergence, QA scope, asymmetric design, data sources). Each procedure named with its citation (Gall 1998, Tyree/Akerman, etc.). The "specified up front" framing.

**§6 Conclusion (cut 350 words):**
Should be ~500 words (one tight page). Right now 847w is conference-paper length. Specifically:
- The summary paragraph (line 505) restates the abstract in different words. Compress to 3-4 sentences.
- The borgerforslag.dk paragraph (line 520-ish) restates the intro framing. Cut entirely or to one sentence.
- Future work is the strongest part — keep most of it, but trim the "design science" sentence if it's vague.

### Tier 2 — moderate cuts

**§4.2 Consul (cut 250 words):**
Some grey-lit paraphrasing can be tighter. The fork-history narrative spreads over more paragraphs than needed. The Madrid-12,725 sentence is doing real work — keep. The 1,030 / 280 / 39 / 5 breakdown is doing real work — keep.

Likely cut targets:
- Paragraphs paraphrasing OSOR/NTARI reports — combine.
- Pre-fork timeline narrative — compress.

**§2 Background (cut ~250 words total):**
Each subsection trims ~25%. Specifically:
- §2.1: probably has a citation-heavy paragraph that lists Bass attributes — keep modifiability, interoperability, algorithmic depth (the three we use); cut the rest.
- §2.2: tight already. Trim only redundancy. The Iansiti pre-classification of Decidim-as-keystone and Consul-as-dominator is now closed in §5.1 — keep but compress.
- §2.3: the shortest already. Trim the gap-restatement sentence at the end (the gap is also stated in the intro).

**§5.1 Architecture as Governance in Practice (cut 140 words):**
The new Iansiti opening paragraph (just added) is doing real work. Don't cut that. Likely targets:
- The Schneider modular-politics paragraph — already tight; cut a sentence.
- The SECO-extension paragraph (l.477) — compress.

**§5.4 Evaluating (cut 180 words):**
Six paragraphs is too many. Specifically:
- Architecture-vs-politics confound — keep, this is the strongest §5.4 move.
- QA scope limit — keep but compress.
- Asymmetric depth limit — keep but compress.
- GitHub-metrics-as-proxies limit — already in the fork-divergence section; cut entirely from §5.4 or compress to one sentence.
- The four limitations Carla added (single-coder, anglophone bias, Decidim-weighted, selection on DV) — keep all four but make them a single tight paragraph or list.

### Tier 3 — light cuts

§1 Introduction (-150), §4.5 Synthesis (-75), §5.2 SECO (-65), §4.4 Ecosystem Evolution (-40), §4.3 Polis (-20), §5.3 Implications (-15) — surgical sentence-level cuts. The 47 voice flags in `reviews/round3/voice.md` cover many of these.

## What NOT to cut

Load-bearing findings and framework moves:

- Three trade-offs (canonical names from Phase 2 Decision 1).
- The Decidim/Consul "same origin, opposite architecture" claim — already capped at 3 mentions (abstract, intro, §4.2).
- Madrid-12,725-commits-ahead detail — already capped at 2 mentions (§4.2 + §5.1).
- Iansiti loop closure paragraph at the start of §5.1.
- Fork-divergence shape as a niche-creation diagnostic (the §5.2 SECO contribution).
- Two design lessons in §5.3 (modular over monolithic; depth-vs-breadth deliberate choice).
- Three-structure verdict in §4.5 at line 429.
- All four §5.4 limitations Carla added.
- The 47 commit/contributor/fork numbers — every number is load-bearing for one of the framework moves.
- All session-log citations and references.

## Order of operations

Work the tiers in order — biggest wins first.

1. **Tier 1 first** (§4.1, §3, §6). These are the biggest cuts. Doing them first means the rest of the cut work is informed by the new shape.
2. **Tier 2 next** (§4.2, §2, §5.1, §5.4).
3. **Tier 3 last** (surgical sentence-level fixes everywhere else). The 47 voice flags from round 3 apply throughout — many of those edits also cut words. Folding them in during Tier 3 makes that single pass do double duty.
4. **Word-count check after each tier.** Re-run word counts to track progress against budget.
5. **Final compilation check** — verify no broken refs, page count is in target, all session-log numbers still match.

## How to cut without losing voice

- Combine sentences that say one thing in two breaths.
- Replace clauses with words: "the analysis that we performed using" → "the analysis used."
- Drop dead-weight phrases: "It is important to note that," "In this section we," "It is worth noting."
- Replace em-dashes that don't earn their keep with commas or periods (47 voice flags has the specific candidates).
- Cut "and X" lists where X is the third example after two strong ones.
- Cut second-order qualifications: "though it should be noted that" — usually deletable.

The 47 voice flags are partly compression work. Doing them well takes a meaningful chunk out of the total.

## When done

- Re-compile, re-count, verify 17–19 body pages.
- Re-check no broken references.
- Re-check all session-log numbers still appear correctly.
- Push.

LSA voice pass after Carla finishes.
