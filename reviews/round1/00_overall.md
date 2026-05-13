# Holistic review: Building the Democracy Stack

## Verdict

There is one paper here, but it is held together by a single load-bearing claim (the Decidim/Consul divergence) and a single load-bearing literature move (SECO + STS applied to civic tech, "to the best of our knowledge" for the first time). When those hold, the paper works. When you push on them, the seams show.

Strengths: the research question is sharp, the case selection is well-justified for an MSc project of this size, the Decidim analysis is genuinely substantive (engine layering, registry pattern, four interaction mechanisms — this is real architectural work, not a wave at the codebase), and the trade-off framing gives the paper a clear spine. The voice is consistent.

Weaknesses: the central thesis is *demonstrated* in the Decidim/Consul comparison but *assumed* almost everywhere else; the four trade-offs are named inconsistently between abstract, synthesis, and conclusion; the Polis case is doing too much rhetorical work for how little is actually shown; Method (17 lines) is undersized relative to Analysis (~270) for a study that hinges on methodological credibility; and the SECO half of the paper is consistently more cautious and better-cited than the STS/democracy half, which leans on three citations doing very heavy lifting.

Single most important fix: lock down the four trade-off names and use the same four labels in the abstract, the synthesis table, the discussion, and the conclusion. Right now they drift, and a careful reader will notice.

## Lens 1 — Argument & rigor (paper-level)

**One paper or two?** One paper, but two registers running in parallel — an SA/SECO paper and a democracy/STS paper. They share a research question and a case set, which is enough. What is *not* enough is the integration: the SA/SECO half is empirically grounded (gemspec files, registry patterns, contributor counts), the democracy half is mostly assertion plus a small canon (Winner, Lessig, Schneider). The two halves only fuse cleanly in Section 4.2 (Consul fork problem) and Section 5.1. Elsewhere they are stacked rather than woven.

**Does everything answer the same RQ?** Mostly yes — the RQ on line 120 is recovered in §6 line 500. But the *abstract* promises "the strongest evidence that architectural decisions in civic tech function as governance decisions" while the *conclusion* is more careful: "the clearest demonstration." The intro promises the paper "provides the kind of architectural analysis that IDEA's 'democracy stack' framework calls for" (line 122) — but the paper does not actually deliver an architectural specification, it delivers a comparative analysis. That is a real overpromise.

**Central thesis demonstrated or assumed?** Partially demonstrated. The Decidim/Consul half-pair carries the demonstration. Polis is asserted: "Polis shows that architectural decisions about algorithms are also governance decisions" (line 390) — but the demonstration is just the unsurprising observation that PCA + k-means is a classification scheme, which is a Bowker/Star point about *all* algorithms, not a finding about Polis specifically. The architecture-as-governance claim about Polis is the weakest link in the argument.

**Trade-off naming consistency.** This is the worst single drift in the paper. Compare:
- Abstract (line 98): "modifiability versus sustainability, interoperability versus autonomy, deployability versus transparency, and algorithmic depth versus ecosystem extensibility."
- Intro (line 120): "modifiability versus sustainability, interoperability versus autonomy, deployability versus transparency, and algorithmic sophistication versus ecosystem breadth."
- Synthesis table (Tab. tradeoffs, line 442–448): the four rows are *Modifiability*, *Interoperability*, *Deployability*, *Transparency* — each split into democratic benefit vs. architectural cost. The right-hand cost column does not match the abstract's "versus" phrasing.
- Conclusion (line 500): same wording as intro.
The synthesis table is the only place that actually displays the trade-offs analytically, and it uses *different* axes than the abstract claims. Fix this. The table should name the four trade-offs as paired tensions, or the abstract should drop the "X vs. Y" framing.

**Case selection.** The asymmetric design (Decidim deep, Consul comparison, Polis contrast) is defensible and the Method section (line 175) justifies it well. The "same origin, opposite architecture" pairing of Decidim/Consul is the strongest analytical move in the paper. Polis is the weakest link — not because it shouldn't be included, but because the framework strains: PCA/k-means is being analysed as if it were comparable to engine-mounting and registry patterns, and it isn't. Polis is doing different work than the other two cases (algorithmic governance vs. structural governance), and the paper acknowledges this on line 378 but then quietly forgets it when extracting "lessons" in §5.

**Decidim/Consul claim audit.** The claim appears in: abstract (line 98), intro (lines 120, 122), method (line 175), Consul analysis opener (line 335), synthesis (line 452), §5.1 (line 466), §5.4 (line 486), conclusion (line 504). It is substantiated in §4.2 (one paragraph plus the comparison table) and §5.4 (which is admirably honest about the politics-vs-architecture confound — line 486 is the most rigorous moment in the paper). The other six mentions all gesture at the substantiation rather than restating it. This is fine *if* the analysis section is doing the work — and it is — but the repeated invocation in abstract/intro/conclusion/synthesis starts to feel like incantation. Cut at least two mentions.

**One-sentence contribution.** Best attempt: "A multi-case architectural analysis showing that quality-attribute trade-offs in civic tech platforms function as governance choices, with the Decidim/Consul divergence as the clearest demonstration." This is supported. The stronger framing the paper sometimes attempts — that it gives policymakers / IDEA the architectural guidance they need — is overclaimed.

## Lens 2 — Clarity & structure (paper-level)

**Section weights.** Analysis is ~270 lines (4 subsections), Discussion ~50 lines, Method ~17 lines, Background ~35 lines. The Method/Analysis ratio is the structural risk. A multi-case study lives or dies by methodological credibility, and a 17-line method section is short for the genre, even at MSc-project length. The choice of four quality attributes, the "lightweight recovery" definition, and the data-source description all deserve more room. Adding 20–30 lines on what "lightweight recovery" specifically did and did not do, plus a paragraph on validity/reliability, would shift the paper from "plausible" to "defensible."

**Reader handholding.** The argument arc is mostly clear, but Sections 2.1–2.3 try to do four things at once (define SA, define quality attributes, define SECO, define architecture-as-governance) and the reader has to keep four conceptual maps in their head simultaneously. A one-paragraph "what to expect" map at the end of §2 (or beginning of §3) would help. Forward references to specific sections are good (e.g. line 161 "see Section sec:evaluation") — keep them.

**Repetition.** Same point made twice:
- The "shared origin / opposite architecture / different outcomes" sentence appears in some form at lines 98, 120, 122, 335, 452, 466, 486, 504. The reader gets it after the third repetition.
- The "to the best of our knowledge no study has applied SA/SECO to civic tech" appears at lines 98 (abstract), 118 (intro), 153 (background SECO), 161 (background arch-gov). Four times is too many for the same gap-claim.
- The IDEA "democracy stack" framing appears at lines 112, 122, 478, 504. This is acceptable because each instance has a different role, but the §5.3 framing repeats the intro framing nearly verbatim.

**Figures.** Three figures, all earn their place. The tensions diagram (Fig. tradeoffs) is well-placed but does heavy lifting — the caption itself admits the other trade-offs "do not all reduce to the same diagonal," which is an honest acknowledgement that the chosen axes (modifiability × deployability) are not the only ones that could have been plotted. The Decidim dependency figure is the best figure in the paper; the matrix figure is good. None is floating, all are referenced in text.

## Lens 3 — Writing style (paper-level)

Voice is consistent — same author throughout. Register is appropriate for the genre: plain, declarative, occasional first-person plural. The prose does not read AI-generated as a whole. Strong opening (the Denmark stack vs. democracy stack framing on line 110 is excellent).

Recurring patterns to watch:
- **The "X is Y — and Z" em-dash construction** appears repeatedly: lines 98, 116, 122, 161, 452, 504. Used three or four times it lands; used a dozen times it becomes a tic.
- **The "this is not abstract / this is not just X" construction** appears at lines 136, 502, 504. Reads slightly motivational-speech.
- **"What's more / what stands out / what's more important"** are absent (good).
- **Wind-up phrases** are largely absent (good).
- **Hedging-then-asserting** is a pattern: "We hypothesize that…" (line 149), "This supports the hypothesis… though it does not prove it" (line 417), "These are reasoned arguments, not proven causal links" (line 161). This is *intellectually honest* and a strength — keep it — but it appears so often that the cumulative effect is a paper that is constantly walking back its own claims. The fix is not to remove the hedges but to commit harder to the few claims that are actually well-supported.

**Length / padding.** §5.2 ("What SECO Research Gains from Democratic Analysis") feels padded — the core point (architecture-as-governance adds a normative layer to health metrics) is a single paragraph, stretched to three. §5.3 ("Implications for the Democracy Stack") is the section closest to recycling earlier material. Trim 5.2 and 5.3 by ~30% each.

**Length / missing.** The Method section is the obvious shortfall. A clearer "what we did and did not do" paragraph on the boundary of lightweight recovery would buy a lot of credibility.

## Lens 4 — Academic conventions (paper-level)

**Citation balance.** Counting roughly: SA/SECO literature (Bass, Christensen, Manikas, Jansen, Iansiti, Tyree, Knutas, Koskinen, Cobos, Noori) — about 10 sources, well-distributed, all relevant. STS/governance literature (Winner, Lessig, Schneider 2024, Schneider 2021, Zhang, Bowker & Star, DeNardis) — about 7 sources, but Winner-Lessig-Schneider 2024 are doing nearly all the heavy lifting (cited together as a trio on lines 116, 503). Civic tech / participation literature (Barandiaran, Palacin, Aragón, Bono, Weyl & Tang, Roy/Lessig/Tang) — 6 sources, but Barandiaran is the only one used substantively; the others are listed but barely engaged. The SECO side is handled with more care than the STS side.

**"To the best of our knowledge" claims.** Used at lines 98 and 118 (essentially the same claim: no SA or SECO study on civic tech). This is load-bearing: it justifies the paper's contribution. It is defensible *for SECO* (Manikas 2016 review supports it, line 153). It is harder to defend *for software architecture* — there is a sizeable HCI/CSCW literature on civic platforms that could plausibly be called architectural in places (Aragón 2017 is in the bib but uncited; behrendt2025supporting is in the bib but uncited). Tighten the claim: "to the best of our knowledge, no study has applied formal SECO analysis to civic tech, and none has examined civic tech through the lens of software architecture quality attributes." That is more precise and more defensible.

**Self-citation patterns.** None — the author has no prior work to cite.

**Missing seminal works.** DeNardis (`denardis2009protocol`) is in the bib but never cited — surprising given the protocol-politics framing would strengthen §2.3 and §5.1. Weyl & Tang's *Plurality* book is in the bib, uncited — relevant to Polis. Roy/Lessig/Tang on Conversation Networks is in the bib, uncited. Aragón 2017 and Behrendt 2025 are in the bib, uncited. Five orphaned citations is a lot; either use them or drop them. For seminal works *not* in the bib that should be: Bass et al. is well-handled, but there is no engagement with quality-attribute scenario literature (ATAM, utility tree) which would naturally extend the trade-off framing; and for the democracy side, nothing from Pateman, Fung, or the deliberative-democracy literature that the platforms themselves invoke — this paper is about civic tech platforms but engages zero political-theory sources beyond Winner/Lessig.

**Reference list quality.** 30 entries. Mostly recent (15+ from 2024–2026), mix of books / journals / techreports / grey literature. The grey-literature heavy mix (CEPS, OSOR, NTARI, IDEA, Codegram blog, Roskilde index) is appropriate for the topic but should be flagged in the method as a deliberate choice. No embarrassing gaps in the SA/SECO list. Heeks2025three is cited "Richard Heeks and others" — the et al. abbreviation is fine in text but the bib entry should have full author list if you can find it; same for behrendt2025supporting, knutas2020local.

**MSc genre fit.** The paper hits MSc-project conventions: clear RQ, multi-case study, primary and secondary sources, limitations section, GenAI disclosure. The ambition is appropriate to 7.5 ECTS. The risk is the opposite of underclaiming — the abstract and intro reach for impact (European policymakers, democracy stack) that an MSc project cannot fully deliver. Pull those claims back one notch.

## Load-bearing claims audit

| Claim | Where it appears | Support |
|---|---|---|
| Software architecture in civic tech has not been studied with SA/SECO methods | Abstract, §1, §2.2, §2.3 | **Partially supported.** Defensible for SECO (Manikas 2016 review), harder for SA — bib contains uncited HCI/CSCW work on civic platforms. |
| Decidim and Consul share an origin in 15M | §1, §3, §4.2, §5.1 | **Fully supported.** Codegram blog, Barandiaran book corroborate. |
| Decidim is modular, Consul is monolithic | §4.1, §4.2, Table consul-decidim | **Fully supported.** Gemspec / routes.rb evidence is concrete. |
| The architectural divergence produced different ecosystem outcomes (80+ modules vs. 250 forks) | §4.2, §4.4, §5.1, §6 | **Partially supported.** Numbers are real (linaker2025consul, ntari2025consul), but the *causal* link from architecture to ecosystem is one factor among several — §5.4 admits this honestly, but the abstract / intro / conclusion still phrase it causally. |
| In civic tech, software structure shapes organizational and business structures | §2.2, §4.4, §5.1 | **Partially supported.** Three cases, consistent pattern, but n=3 and the paper itself says "does not prove it" (line 417). Honest, but the claim is then re-used as if it were established. |
| Polis embeds an epistemological assumption via PCA/k-means | §4.3, §5.1 | **Partially supported.** True as a general Bowker/Star point about any classification scheme; the paper does not show what *specific* democratic outcomes follow from this in Polis deployments. |
| The four trade-offs apply to all democratic infrastructure | Abstract, §4.4, §5.3, §6 | **Overclaimed.** Derived from three cases; presented as if generalisable. The conclusion's "if Copenhagen wanted to build…" assumes the trade-offs transfer. They might; the paper has not shown it. |
| The paper provides the architectural analysis IDEA's framework "calls for but does not deliver" | §1 line 122 | **Overclaimed.** The paper provides analysis of existing platforms, not architectural guidance for building a democracy stack. |
| Architecture is the governance decision | Abstract, §1, §4.4, §5.1, §6 | **Partially supported.** Demonstrated in Decidim/Consul; asserted in Polis; generalised in the conclusion. |

## Drift map

Places where abstract / intro / analysis / discussion / conclusion say slightly different things about the same idea:

1. **The four trade-offs.** Abstract pairs them as "X vs. Y" (modifiability vs. sustainability, etc.). Synthesis table presents them as "democratic benefit vs. architectural cost" with the four QAs as rows. Conclusion reverts to the abstract phrasing. Pick one framing and stick with it across all five locations.

2. **What the paper delivers to IDEA / European policy.** Intro: "provides the kind of architectural analysis IDEA's framework calls for" (line 122). §5.3: "Our cases point to some concrete lessons" (line 480) — much more modest. Conclusion: "architecture is not a procurement detail — it is a governance choice" (line 504) — back to assertive. The §5.3 framing is the honest one; pull intro and conclusion toward it.

3. **The Decidim/Consul divergence.** Abstract: "the strongest evidence." Intro: "the clearest demonstration." Synthesis: "the clearest evidence." Conclusion: "the clearest demonstration." Four nearly-identical superlative claims in four places. Pick the right adjective once.

4. **What was actually done methodologically.** Method: "lightweight architectural recovery from primary sources" (line 169). Analysis: highly detailed for Decidim, much thinner for Polis. §5.4 admits "the Polis analysis was the thinnest, relying mostly on published descriptions" (line 490). The intro and abstract describe the method as uniform across cases; the analysis is not, and §5.4 says so. Update the method to acknowledge the asymmetry up front, not as a retrospective limitation.

5. **The role of Polis.** Method: "tests whether our framework works beyond the participatory platform genre" (line 175). Synthesis: positioned alongside Decidim and Consul as a third case in a comparative table. §4.3: "evidence of a different trade-off profile" (line 378). Conclusion: lumped in with the other two as if equivalent. Polis is doing different work in different sections; commit to the "different paradigm" framing throughout.

6. **The hypothesis about software-structure dominance in civic tech.** §2.2: "We hypothesize that in civic tech ecosystems, it works differently" (line 149). §4.4: "This supports the hypothesis from Section 2.2, though it does not prove it" (line 417). §5.1: "This relationship is especially strong in civic tech" — asserted, not hedged (line 466). The honest hedge in 4.4 disappears in 5.1.

## Prioritised fix list

1. **Lock down the four trade-off names.** Use one phrasing across abstract, synthesis table, §5, conclusion. The synthesis table is the analytical anchor; align the abstract to it, not vice versa.
2. **Expand Method to ~40–60 lines.** Add: explicit definition of what "lightweight recovery" did and did not do; rationale for the asymmetric depth (Decidim deep vs. Polis thin) *up front*, not in §5.4; one paragraph on validity threats and how you addressed them.
3. **Pull back the IDEA / policymaker framing in intro and conclusion** to match the more modest §5.3 phrasing. The paper analyses existing platforms; it does not deliver an architectural specification.
4. **Tighten the "to the best of our knowledge" claim** to specify "SECO analysis and quality-attribute analysis" rather than the vaguer "software architecture or software ecosystem methods."
5. **Cut redundant invocations of the Decidim/Consul divergence.** Keep it in abstract, in §4.2 (where it earns its keep), in §5.1, and in conclusion. Drop the other 4 mentions.
6. **Use or cut the orphan citations** (denardis2009protocol, weyl2025plurality, roy2025conversation, aragon2017deliberative, behrendt2025supporting). Five unused entries is messy.
7. **Trim §5.2 and §5.3 by ~30%.** Both repeat material from §4.4 and §2 without adding much.
8. **Commit harder on Polis.** Either deepen the analysis (look at the actual algorithm, its parameters, what's exposed to deployers) or commit fully to the "contrasting paradigm, not a third equal case" framing — and have the synthesis table acknowledge it (e.g., a footnote that Polis sits on a different axis).
9. **Rebalance the citation base** on the democracy side. Either engage one or two more STS / political theory sources, or scope the claim to "platform studies" rather than "STS, law, and platform studies" — the latter implies engagement the paper does not have.
10. **One-paragraph roadmap at the end of §2 or start of §3.** Tell the reader: here is the RQ, here is the method, here is the case order, here is where the trade-offs are synthesised.
11. **Honesty about the politics/architecture confound** is excellent in §5.4 — surface this earlier (one sentence in §3 or §4.2). It strengthens the paper rather than weakening it.
12. **Strip one repetition pattern** — the "X is Y — and Z" em-dash construction. Rewrite half the instances as two sentences.
13. **Add a "scope" note** to the abstract's gap-claim. "No SECO study and no quality-attribute analysis" is more defensible than "no SA or SECO study."
14. **Fix Heeks et al. and Knutas et al. bib entries** to full author lists if available; "and others" is a placeholder.
