# Background (Section 2) — harsh review

## Verdict

The Background is three competent mini-reviews glued together, not a built foundation. §2.1 (SA) and §2.2 (SECO) each do their job in isolation; §2.3 is supposed to fuse them with the "architecture is governance" thesis but in its current 3-paragraph form it just restates the gap from the Introduction and asserts the contribution. The integration the paper needs — *how* SA quality attributes and SECO structures jointly operationalize "architecture as governance" — is missing. Several Method/Analysis concepts (architectural recovery, ADRs, ecosystem health metrics, three-structure framework) are used as load-bearing tools but never set up in Background. Writing is mostly plain; a handful of em-dash piles and one or two slop phrases.

## 1. Argument & rigor

- §2.3 does not integrate the three strands. It announces a synthesis ("Our contribution is to apply architecture-as-governance using software architecture and SECO methods", l.161) without performing one. There is no paragraph that says: *quality attributes are the unit at which architecture-as-governance becomes empirically observable, and SECO structures are how those attributes propagate into governance outcomes*. That is the thesis the paper actually argues — Background should state it.
- The four-attribute selection (modifiability, interoperability, deployability, transparency) is justified twice — once in §2.1 (l.134) and again in Method (l.173). In §2.1 the justification is rhetorical, not principled: "especially important for democratic infrastructure" (l.134) is asserted, not argued. Why these four and not, e.g., security (ballot integrity), availability (election-day load), usability (access)? The reader should leave Background convinced; instead the convincing is deferred to Method.
- Transparency is smuggled in as a quality attribute. "Transparency or auditability does not appear in Bass et al.'s standard taxonomy but is essential here" (l.134). Fine, but then it deserves a real definition tied to literature (auditability in security engineering, algorithmic transparency in FAccT — Bono is cited later but not here). Right now it is the weakest-defined of the four.
- "We hypothesize that in civic tech ecosystems, it works differently: the software structure shapes the other two" (l.149). This is a real, falsifiable claim and the most interesting sentence in §2.2 — but it is half a sentence buried in a paragraph. It should be set up as the hypothesis that §2.2 motivates and Analysis tests. Currently it reads as an aside.
- Concepts used in Method/Analysis that Background never introduces:
  - **Architectural recovery** (Method l.169, l.171). This is the core methodological move on Decidim. Background never says what architectural recovery is, who developed it, or what counts as "lightweight". A one-sentence pointer in §2.1 would close this.
  - **Architectural decision records** (Tyree 2005, Method l.171). The Bass paragraph in §2.1 could mention ADRs in one line.
  - **SECO health metrics — productivity, robustness, niche creation.** Mentioned in passing in §2.2 l.151 as "qualitative lenses" but never defined. They reappear in Analysis l.330 ("robustness is fragile") and the synthesis without the reader knowing what robustness means in SECO terms.
  - **Three-structure framework as analytical apparatus.** §2.2 lists the three structures (l.149) but does not signal that Table~\ref{tab:threestructure} (Analysis l.421) will be the central comparative artifact. The reader meets that table cold.
  - **Comparative case methodology.** The paper leans hard on Decidim/Consul as "approximating a natural experiment" (Method l.175). Background never discusses comparative case method, controlled comparison, or what makes two cases comparable. Even a sentence pointing to Yin or Flyvbjerg would help.
- Concepts introduced in Background that Analysis never uses:
  - **Iansiti & Levien keystone/dominator/niche-creator roles** (l.151) are named in §2.2 and applied once in §2.2 itself, but the typology is not used as a lens anywhere in Analysis or Synthesis. Either Analysis should use it (the keystone vs. dominator framing is genuinely useful for the Decidim/Consul contrast) or §2.2 should drop it.
- Undersourced/overclaimed:
  - "Architecture shapes governance — this idea is well established in science and technology studies (STS) and platform studies" (Abstract, l.98; restated §2.3 l.157). The Background backs this with Winner, Lessig, Schneider, Zhang. That is a reasonable spine, but "platform studies" as a field is not cited at all — no Gillespie, no Plantin et al., no van Dijck. If the claim is "platform studies have shown this," cite platform studies. DeNardis 2009 is in the bib but unused; she is the obvious cite for infrastructure-as-governance.
  - "this literature has focused mostly on online communities (Reddit, Discord, DAOs) and internet infrastructure" (l.157) — no citation, treated as common knowledge. Either drop the specificity or cite.

## 2. Clarity & structure

- Subsection ordering is fine (SA → SECO → synthesis). The problem is that §2.3 is too thin to carry the synthesis weight — currently 3 short paragraphs (l.155–161) where 2 are gap-restatement and 1 is contribution. The actual conceptual bridge is missing.
- §2.1 paragraph 2 (l.134) is list-shaped (four attribute definitions back-to-back). It is the right shape for definitions, but the prose runs them together instead of using a defs list or italicized lead-ins consistently — \emph{Modifiability}, \emph{Interoperability}, \emph{Deployability}, \emph{Transparency} are italicized but the paragraph still reads as one block. A short bullet list would be more honest about what this paragraph is doing.
- §2.1 paragraph 3 (l.136) introduces the trade-offs concept and points to Figure 1 and Table 5. Heeks et al. 2025 ("similar tensions at the policy level") is dropped in without explanation of what those tensions are. Either expand or drop.
- "SECO" is introduced l.147; "OSSECO" appears l.153 without expansion. Minor but real.
- Term "modular monolith" is central to Analysis (l.189, l.405, l.427) and to the whole Decidim/Consul contrast. Background never defines it. A sentence in §2.1 would help.

## 3. Writing style

- "Yet to the best of our knowledge, no study has applied software architecture or software ecosystem methods to civic technology platforms" (Abstract l.98) and "But to the best of our knowledge, it has not been applied to civic technology" (l.118) and "a combination that has not been tried" (l.161). Three near-restatements of the same gap claim across abstract, intro, and Background §2.3. Once is enough; preferably in the contribution paragraph.
- Em-dash piles: l.118 has four em-dashes in one paragraph; l.134 has three in one sentence ("if they cannot, the platform can only accommodate one way of doing things, which limits how many different communities can use it meaningfully"). The l.134 sentence also runs long — break it.
- "radically modularity" — not in Background but in Method (l.175). Flagging because it sets up the SA section's vocabulary and reads slightly hype-y. "Radical" appears nowhere in §2.1. Pick one register.
- "diverse communities" (l.134), "diverse participation designs" (Analysis l.264), "diverse communities can adapt the platform" (l.161, Table 5 l.444). "Diverse" is doing decorative work; in §2.1 l.134 it could just be "communities".
- "powerful deliberation tool" (Analysis l.452) — slop adjective. Not in Background but flagging because it's the kind of phrase to avoid.
- "Despite the clear relevance of ecosystem thinking to civic technology" (l.153) — mild wind-up. Cut "Despite the clear relevance" and start with the gap.
- "Our contribution is to apply architecture-as-governance using software architecture and SECO methods in civic technology — a combination that has not been tried" (l.161). The dash-clause repeats the gap claim from two paragraphs earlier. Cut everything after "civic technology".
- "These mappings are reasoned arguments, not proven causal links" (l.161). Good hedge — keep. But the same hedge appears in Method l.179 and the abstract implies the same. Pick the strongest location.
- No bolded-bullet-label slop in Background. No "various", no "comprehensive", no "robust" as filler (note: "robustness" appears l.151 as the SECO term, which is fine).

## 4. Academic conventions

- Citation density is adequate for §2.1 and §2.2, thin in §2.3 (3 paragraphs, 4 citations, two of which are self-references inside the Decidim project).
- Seminal works: Bass, Manikas, Christensen, Winner, Lessig present. Good.
- Conspicuous absences:
  - **DeNardis 2009** is in the bib but not cited in Background. She is the cleanest citation for infrastructure-as-governance and would strengthen §2.3.
  - **SECO governance literature.** Jansen et al. have multiple papers on SECO governance specifically; the bib only has Jansen 2014 on health. Baars & Jansen, or Alves et al. on SECO governance, would belong here given the paper's title.
  - **Bowker & Star 1999** is cited in Discussion (l.464) for classification politics but would also strengthen §2.3's "architecture is governance" spine.
  - **Schneider 2021 "Modular Politics"** is cited in Discussion (l.462) and is the single most relevant prior work — a paper about modularity as governance for online communities. It belongs in §2.3 as well; that is where the conceptual bridge between modularity (SA) and governance lives.
  - **Comparative case method / case study methodology.** No citation anywhere (Yin, Flyvbjerg, Eisenhardt). The paper rests on a comparative case design without grounding it.
- Recency: most non-seminal cites are 2020–2025. Good.
- Hedging: §2.2 hypothesis is correctly hedged ("This is not a universal law", l.149). §2.3 contribution claim ("a combination that has not been tried", l.161) is mildly overclaimed — softer "we have not found prior work combining" would match the rest of the paper's tone.

## Subsection notes

### §2.1 Software Architecture for Public Infrastructure (l.130–143)
Best of the three subsections. The Bass definition (l.132) is properly anchored. Pivot from commercial → democratic ("the same reasoning applies but the goal is different", l.132) is well done. Problems: four-attribute selection is asserted not argued; transparency definition is loose; no introduction of architectural recovery or ADRs that Method then uses; "modular monolith" never defined. The figure callout and Heeks reference (l.136) are awkwardly compressed.

### §2.2 Software Ecosystems and Democratic Governance (l.145–153)
Solid SECO summary. The hypothesis at l.149 ("the software structure shapes the other two") is the real conceptual contribution of this subsection and is buried. Iansiti & Levien roles (l.151) are introduced but barely used downstream. SECO health metrics (productivity, robustness, niche creation) mentioned but not defined; they are used as load-bearing vocabulary in Analysis. The Manikas 2016 gap claim (l.153) is well-supported and clearly motivated.

### §2.3 Architecture as Governance: Applying the Thesis to Civic Tech (l.155–161)
Weakest subsection. Three short paragraphs. Paragraph 1 (l.157) names Winner→Lessig→Schneider but does not say what the *thesis* is in operational terms. Paragraph 2 (l.159) covers Decidim-internal work. Paragraph 3 (l.161) states the contribution. Missing: the actual conceptual bridge — a paragraph that explains, in this paper's terms, *how* SA quality attributes operationalize the architecture-as-governance thesis, and *how* SECO three-structure analysis traces that operationalization into governance outcomes. Schneider 2021 ("Modular Politics"), DeNardis, and Bowker & Star belong here, not in Discussion.

## Prioritized fix list

1. **Rewrite §2.3 as a real synthesis.** Add a paragraph that says: quality attributes are where architecture-as-governance becomes observable; SECO structures are how it propagates. Pull Schneider 2021 and DeNardis 2009 forward from Discussion/bib. Drop the third gap-restatement.
2. **Argue the four-attribute selection in §2.1, don't assert it.** Tie each attribute to a democratic concern with a citation. Currently the work is deferred to Method l.173, which is too late.
3. **Promote the §2.2 hypothesis** ("software structure shapes the other two") to a labeled hypothesis the paper tests. Currently it reads as an aside; in Analysis l.417 it is treated as a tested claim.
4. **Introduce architectural recovery and ADRs in §2.1.** One sentence each. Right now Method uses both as load-bearing without Background setup.
5. **Define SECO health dimensions** (productivity, robustness, niche creation) where they are introduced (l.151), not just name them. Analysis depends on them.
6. **Define "modular monolith"** in §2.1 — it is the term that does the most work in Analysis and Synthesis.
7. **Add a comparative case method citation** (Yin / Flyvbjerg / Eisenhardt). The Decidim/Consul comparison rests on it.
8. **Cut the gap-restatement.** Pick one location for "this combination has not been tried" — preferably Intro — and drop the duplicates in Abstract and §2.3.
