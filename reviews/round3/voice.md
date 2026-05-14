# Round 3 voice and concision pass

**Total flags:** 47.
**Most common patterns:** em-dash overload (especially three-dash sentences and dashes used where a comma or period would do); restating a claim across two consecutive sentences; lightly hedged sentences whose hedge could be a clause not a sentence; a small cluster of fancy synonyms ("utilize" is not in here, but "demonstrated", "additionally", "intricate" show up in abstract/intro).
**Sections worst affected:** §1 Introduction (em-dashes, restatement), §4.1 Decidim (em-dashes in dense technical prose), §5.1 Architecture as Governance (longest sentences, most restatement), §5.4 Evaluating the Approach (em-dash sprawl plus rhetorical "where it worked best…").

---

## Abstract (95–106)

**L.98** "Architecture shapes governance --- this idea is well established in science and technology studies (STS) and platform studies --- yet to the best of our knowledge…"
→ "Architecture shapes governance, an idea well established in STS and platform studies; yet to the best of our knowledge…"
Reason: three em-dashes in one sentence; the first two are doing a comma's job.

**L.98** "(deep case with empirical architectural recovery from gemspec files and the commit history), Consul (comparison case --- shared origin with Decidim, opposite architecture, with fork-divergence analysis across 1{,}030 GitHub forks)"
→ replace " --- shared origin" with ", shared origin"
Reason: em-dash where a comma reads cleaner inside a parenthetical.

**L.98** "The two-platform comparison provides the strongest empirical anchor for the architecture-as-governance thesis."
→ cut.
Reason: restates the previous sentence's claim about the trade-offs in different words; the sentence after it already says the paper brings architecture into the policy debate.

---

## §1 Introduction (108–127)

**L.110** "Denmark consistently ranks among the most digitized countries in the world, placing first in the EU's Digital Economy and Society Index (DESI) and near the top of the UN e-government rankings."
→ fine, but the next four sentences ("MitID authenticates… Digital Post… Borger.dk… But if a Danish municipality…") pile into a comma-list rhythm; consider breaking "MitID authenticates millions of citizens." with the ones that follow into a single sentence with semicolons rather than four staccato declaratives. Minor — leave if you like the rhythm.
Reason: stylistic, optional.

**L.112** "Across Europe, the gap between digital government services and digital democratic participation keeps growing. This is happening even as the EU invests in democratic digital infrastructure…"
→ "Across Europe, the gap between digital government services and digital democratic participation keeps growing, even as the EU invests in democratic digital infrastructure…"
Reason: "This is happening even as…" is a wind-up; fold into previous sentence.

**L.114** "Together, their experience shows something that the policy conversation tends to miss: software architecture choices directly shape democratic outcomes."
→ "Together, their experience shows what the policy conversation tends to miss: software architecture choices directly shape democratic outcomes."
Reason: "something that" is filler.

**L.116** "\citet{schneider2024governable} demonstrated that online community platforms encode ``implicit feudalism'' through their default governance structures, and \citet{zhang2020policykit} showed that platform software encodes a narrow set of governance possibilities."
→ change "demonstrated" to "showed".
Reason: fancy synonym; the rest of the paragraph already uses "showed/argued".

**L.116** "This insight --- that architecture is governance --- is well established across STS, law, and platform studies."
→ keep, but consider "This insight, that architecture is governance, is well established across STS, law, and platform studies."
Reason: em-dash pair where commas would suffice; you have several similar already.

**L.118** "But the thesis has not been applied to civic technology using software architecture or software ecosystem methods. \citet{knutas2020local} proposed exactly this --- applying open-source ecosystem analysis to civic tech --- but the empirical work was not done."
→ "…proposed exactly this, applying open-source ecosystem analysis to civic tech, but the empirical work was not done."
Reason: em-dash pair acting as commas.

**L.118** "And borgerforslag.dk --- closed-source, single-purpose, centrally built --- shows what happens when democratic software is built without thinking about architecture at all."
→ leave; this is one of the em-dash pairs that earns its keep (the three adjectives are a tight aside).

**L.120** "Consul (comparison case, sharing an origin with Decidim in the 2011 15M movement but evolving along the opposite architectural trajectory, with fork-divergence analysis across all enumerable GitHub forks), and Polis (contrasting paradigm --- algorithmic rather than structural approach to participation)."
→ change " --- algorithmic" to ", algorithmic"
Reason: em-dash inside a parenthetical; comma is calmer.

**L.122** "The Decidim/Consul comparison is the clearest empirical anchor: a controlled-enough divergence in architectural direction to read consequences off without untangling every confound first."
→ leave but watch: this is the third time the paragraph or the abstract calls Decidim/Consul "the empirical anchor". Consider trimming the abstract version (already flagged) so this one carries it.
Reason: cross-section restatement.

---

## §2 Background (128–166)

**L.134** "High-algorithmic-depth platforms can address problems that purely structural platforms cannot --- finding consensus across thousands of opinion vectors, for instance --- but the same depth tightens internal coupling and narrows the contributor base."
→ "High-algorithmic-depth platforms can address problems purely structural platforms cannot (finding consensus across thousands of opinion vectors, for instance), but the same depth tightens internal coupling and narrows the contributor base."
Reason: em-dash pair where parentheses fit the aside better.

**L.134** "Deployability and transparency surface in the cases as descriptive observations rather than primary axes (Polis is Docker-easy and opaque; Decidim's 27-engine setup is complex but readable), and we return to them where they matter in each case section."
→ leave.

**L.136** "They are design trade-offs, not problems to solve; \citet{heeks2025three} identify similar tensions at the policy level."
→ leave.

**L.149** "In commercial ecosystems like app stores, the business structure usually dominates --- Apple's revenue model shapes what apps get built and who builds them."
→ "In commercial ecosystems like app stores, the business structure usually dominates: Apple's revenue model shapes what apps get built and who builds them."
Reason: em-dash where a colon does the explanatory job better.

**L.149** "This is not a universal law --- Christensen et al.\ do not claim any fixed ordering between the structures --- but it is a pattern we observe across all three cases…"
→ "…This is not a universal law (Christensen et al.\ do not claim any fixed ordering between the structures), but it is a pattern we observe across all three cases…"
Reason: em-dash pair as parenthetical.

**L.151** "These roles map onto civic tech in ways we examine in the analysis: Decidim's technical office operates as a keystone (maintaining shared infrastructure while enabling independent module development), while Consul's Madrid team functioned more as a dominator (controlling the codebase without mechanisms for external contribution). We also draw on ecosystem health dimensions --- productivity, robustness, niche creation \citep{jansen2014measuring} --- as qualitative lenses in the discussion (Section~\ref{sec:disc-seco})."
→ change " --- productivity, robustness, niche creation \citep{jansen2014measuring} --- " to " (productivity, robustness, niche creation; \citealp{jansen2014measuring}) "
Reason: em-dashes around a three-item list inside a sentence that already has parentheses; pick one.

**L.157** "As introduced in Section~\ref{sec:sa}, the idea that architecture functions as governance is well established --- from \citet{winner1980artifacts} through \citet{lessig2006code} to \citet{schneider2024governable}."
→ "…well established, from Winner through Lessig to Schneider."
Reason: em-dash where comma reads cleaner.

**L.161** "Our contribution is to apply architecture-as-governance using software architecture and SECO methods in civic technology --- a combination that has not been tried."
→ "Our contribution is to apply architecture-as-governance using software architecture and SECO methods in civic technology, a combination that has not been tried."
Reason: em-dash as comma.

**L.161** "Our architectural evidence shows that certain designs \emph{make it possible} for democratic outcomes to happen --- for instance, modularity lets diverse communities adapt the platform --- but proving the outcomes actually materialised would require field studies beyond this paper's scope."
→ "…make it possible for democratic outcomes to happen (modularity lets diverse communities adapt the platform, for instance), but proving the outcomes actually materialised would require field studies beyond this paper's scope."
Reason: three-em-dash sentence; the middle aside reads better in parentheses.

---

## §3 Method (167–198)

**L.169** "Not every step is run on every case --- Decidim gets the deepest treatment, Consul gets lighter recovery plus fork divergence, and Polis is included as a contrasting paradigm with lighter analysis."
→ "Not every step is run on every case: Decidim gets the deepest treatment, Consul gets lighter recovery plus fork divergence, and Polis is included as a contrasting paradigm with lighter analysis."
Reason: em-dash where a colon does the introducing.

**L.172** "Other widely deployed civic tech platforms --- Loomio, CitizenLab, vTaiwan, Adhocracy, LiquidFeedback --- are not analysed here; the three we picked were sufficient to identify the trade-offs without exhausting the field."
→ leave; em-dash pair frames a comma-internal list. This is the kind that earns its keep.

**L.175** "Consul's recovery is lighter and focuses on the points where it contrasts with Decidim --- a single Rails monolith with a file-override extension mechanism, recovered from the codebase structure and documentation."
→ "…where it contrasts with Decidim: a single Rails monolith with a file-override extension mechanism, recovered from the codebase structure and documentation."
Reason: colon, not em-dash, for the appositive.

**L.181** "For each non-merge, non-bot commit we identify which top-level engine directories the commit touches, count co-occurrences across all engine pairs, and compute the Jaccard similarity --- commits touching both engines divided by commits touching either --- as the coupling metric."
→ leave; the em-dash pair brackets a working definition.

**L.187** "Each pairs a quality attribute that civic tech platforms compete on against an architectural cost the same attribute imposes."
→ flag for re-check: this sentence reads awkwardly because of the "pairs … against" construction. Consider "Each pairs a quality attribute civic tech platforms compete on with the architectural cost that attribute imposes." Same idea, cleaner.
Reason: phrasing.

**L.187** "For each case we identify the architectural decisions that visibly trade off between these tensions --- modular versus monolithic organisation, plugin versus fork extension, shared versus isolated data, algorithm-as-product versus algorithm-as-feature --- drawing on the architectural decision record tradition…"
→ leave; em-dash pair around a four-item list works.

**L.190** "Its modular monolith --- a Ruby on Rails monorepo of first-party engines organised through a manifest pattern --- offers the most architecturally rich example available in civic tech."
→ leave; appositive earns it.

**L.190** "The Decidim/Consul pair briefly shared early code; the architectural split between them approximates --- though does not constitute --- a natural experiment, shaped by organisational and political factors as well as technical ones \citep{barandiaran2024decidim}, which we revisit in Section~\ref{sec:evaluation}."
→ replace " --- though does not constitute --- " with ", though does not constitute,"
Reason: em-dashes inside an already comma-dense sentence; commas are calmer here.

**L.190** "Polis is a contrasting paradigm rather than a third equal case: algorithmic deliberation through PCA and k-means clustering rather than structured participation. The Polis treatment is shorter --- no fork-divergence analysis, no per-module recovery --- and serves to test whether the trade-off framework extends beyond the participatory-platform pattern."
→ "The Polis treatment is shorter (no fork-divergence analysis, no per-module recovery) and serves to test whether the trade-off framework extends beyond the participatory-platform pattern."
Reason: em-dash pair around two-item list; parentheses scan better mid-sentence.

**L.193** "Primary sources are technical: the public GitHub repositories of all three platforms at pinned snapshots --- \texttt{decidim/decidim} at \texttt{be39c244} (2026-05-12), \texttt{consuldemocracy/consuldemocracy} at \texttt{3c3b5c4a} (2026-05-11), \texttt{compdemocracy/polis} at \texttt{e8c2b46d} (2026-04-26) --- plus gemspec and dependency files for Decidim, application structure for Consul, runtime components for Polis."
→ leave; em-dash pair brackets the SHA list, which has its own commas. This is the right use.

**L.193** "Architectural recovery captures dependency structure but not behaviour at runtime."
→ leave.

---

## §4.1 Decidim (201–304)

**L.203** "The monorepo at \url{github.com/decidim/decidim} contains 27 first-party engines packaged as standalone Ruby gems --- 24 user-facing platform engines and three developer-tooling engines (\texttt{design}, \texttt{dev}, \texttt{generators})."
→ leave; em-dash splits the count from the breakdown.

**L.209** "So far the architecture matches the textbook description of a hub-and-spoke pattern. But the graph is denser than that --- 13 of the 27 engines also have runtime dependencies on other Decidim engines besides core."
→ "But the graph is denser than that: 13 of the 27 engines also have runtime dependencies on other Decidim engines besides core."
Reason: em-dash where colon does the explanatory job.

**L.209** "These two engines are de-facto Layer-2 hubs of the platform rather than peers of the infrastructure engines, even though they are categorised as ``shared services'' alongside \texttt{verifications}."
→ leave.

**L.219** "Almost any component can attach to almost any space, creating an $N \times M$ combinatorial matrix \citep[p.~75]{barandiaran2024decidim}."
→ leave.

**L.279** "Of the 5{,}517 commits that touched at least one engine, $64\%$ stay inside a single engine boundary (mega-commits touching more than eight engines are excluded as refactor or release commits, and bot commits are filtered) --- the architecture provides real, not nominal, isolation."
→ "Of the 5{,}517 commits that touched at least one engine, $64\%$ stay inside a single engine boundary (mega-commits touching more than eight engines are excluded as refactor or release commits, and bot commits are filtered): the architecture provides real, not nominal, isolation."
Reason: em-dash after a long parenthetical does not read; colon or period works.

**L.279** "First, the four participatory spaces (\texttt{processes}, \texttt{assemblies}, \texttt{conferences}, \texttt{initiatives}) co-change at Jaccard up to $0.43$ despite having no gemspec dependencies between them --- the ``space'' abstraction is unified at the source level rather than implemented as four independent realisations of a clean interface."
→ "…no gemspec dependencies between them; the ``space'' abstraction is unified at the source level rather than implemented as four independent realisations of a clean interface."
Reason: semicolon or period reads cleaner; em-dash here is doing too much heavy lifting.

**L.279** "The modularity is at API boundaries, not at implementation."
→ leave.

**L.292** "Multi-tenancy helps --- one installation can serve multiple organizations --- but the initial barrier is still high."
→ "Multi-tenancy helps (one installation can serve multiple organizations), but the initial barrier is still high."
Reason: em-dash pair where parentheses fit the aside.

**L.295** "Mining the commit history (Section~\ref{sec:method}) gives a sharper picture of ecosystem health: 7{,}078 human commits across 183 unique human authors since 2016, with the top three contributors accounting for $36\%$ of commits and the top ten for $68\%$ (Gini coefficient on the per-author distribution: $0.85$)."
→ leave.

**L.295** "Figure~\ref{fig:decidim-engine-activity} plots commits per engine in the last 12 months: all 24 user-facing engines see activity, with \texttt{decidim-core}, \texttt{proposals}, and \texttt{admin} leading and three recently added engines visible at the bottom (\texttt{ai}, \texttt{demographics}, \texttt{collaborative\_texts}) accumulating their first hundreds of commits. The modular architecture is matched by modular maintenance --- no engine is dormant. The ecosystem is productive and diverse but its robustness is fragile."
→ "…accumulating their first hundreds of commits. The modular architecture is matched by modular maintenance: no engine is dormant. The ecosystem is productive and diverse but its robustness is fragile."
Reason: em-dash to colon.

---

## §4.2 Consul (305–358)

**L.310** "Features --- proposals, debates, budgets, legislation, voting, polls --- all share the same codebase, the same \texttt{ApplicationController}, and the same routes file."
→ leave; em-dash pair brackets a six-item list.

**L.310** "Models live in \texttt{app/models/} with functional subdirectories (for example, \texttt{budget/investment.rb}), but there are no module-level namespace boundaries enforced at the code level --- a budget model can freely reference a proposal model without going through any API or registry."
→ "…but there are no module-level namespace boundaries enforced at the code level: a budget model can freely reference a proposal model without going through any API or registry."
Reason: em-dash to colon for the consequence.

**L.316** "Of those, 746 ($73\%$) are unmodified --- ``stars in fork form'', created but never edited."
→ "Of those, 746 ($73\%$) are unmodified: ``stars in fork form'', created but never edited."
Reason: em-dash to colon.

**L.316** "The ``deployer maintains a fully separate codebase'' picture applies to a handful, not to hundreds."
→ leave.

**L.318** "The city that originated the platform ended up maintaining a private copy that drifted away from the public upstream and was eventually abandoned --- the architecture pushed even the originator into the fork pattern that fragmented the wider ecosystem."
→ "…and was eventually abandoned. The architecture pushed even the originator into the fork pattern that fragmented the wider ecosystem."
Reason: em-dash where period reads cleaner; also this is the second time in two paragraphs that you say "Madrid forked its own platform"; the period at least lets the second sentence stand as the punchline rather than smushed onto the first.

**L.320** "The ecosystem did not slowly grow and consolidate --- it ossified."
→ leave; em-dash earns this one (short punchline aside).

**L.356** "The architecture did not just constrain the code --- it constrained who could participate in shaping the platform, and pushed even the originator into the fragmentation pattern."
→ leave; em-dash pivot works here.

---

## §4.3 Polis (359–375)

**L.364** "K-means clustering (a standard machine learning algorithm that groups similar data points, with $k$ selected automatically) then identifies groups of like-minded voters on this landscape."
→ leave.

**L.364** "This algorithm is the product --- everything else is infrastructure around it."
→ leave; punchline em-dash works.

**L.367** "The platform is effectively a one-developer codebase with sporadic external contributions, in contrast to Decidim's 183 authors over a comparable interval."
→ leave.

**L.367** "Deployers can run it without understanding --- or being able to audit --- the PCA algorithm that determines what counts as consensus."
→ leave.

**L.370** "\emph{Transparency} is low to moderate: the code is open source, but the algorithmic core --- dimensionality reduction and clustering --- is opaque to most users and deployers."
→ "…the algorithmic core (dimensionality reduction and clustering) is opaque to most users and deployers."
Reason: em-dash pair as parenthetical.

**L.373** "\citet{bono2025artificial} identify algorithmic transparency as a key design principle for AI in participation platforms --- a concern that Polis predates but does not fully address."
→ "…a key design principle for AI in participation platforms, a concern that Polis predates but does not fully address."
Reason: em-dash as comma.

---

## §4.4 Ecosystem Evolution (376–401)

**L.381** "All three are top-heavy --- this is normal for open-source projects --- but the differences within the comparison are striking."
→ "All three are top-heavy, which is normal for open-source projects, but the differences within the comparison are striking."
Reason: em-dash pair as commas.

**L.381** "Polis is a one-developer codebase: the top three authors did $82\%$ of commits, the top ten did $97\%$, and Mike Bjorkegren alone accounts for $56\%$. Consul is also heavily concentrated --- the Madrid municipal team's signature is visible, with the top three doing $52\%$ and the top ten doing $87\%$."
→ "…Consul is also heavily concentrated: the Madrid municipal team's signature is visible, with the top three doing $52\%$ and the top ten doing $87\%$."
Reason: em-dash to colon, matches the rhythm of the preceding "Polis is a one-developer codebase:" sentence.

**L.391** "This cliff coincides with Ahora Madrid losing the city's mayoralty in May 2019 \citep{barandiaran2024decidim} and is the most dramatic feature of the entire comparison --- the paper's earlier claim that institutional politics affected Consul's trajectory (Section~\ref{sec:evaluation}) is no longer anecdotal."
→ "…the most dramatic feature of the entire comparison: the paper's earlier claim that institutional politics affected Consul's trajectory (Section~\ref{sec:evaluation}) is no longer anecdotal."
Reason: em-dash to colon.

**L.391** "Decidim starts late 2016, ramps to roughly 1{,}200 per year, drops in 2019, then settles into a steady plateau of 600--770 commits per year through 2025 --- an unusual pattern of sustained activity rather than the typical hump-shaped curve."
→ leave; em-dash gloss earns it.

---

## §4.5 Synthesis (402–444)

**L.406** "This is the hypothesis from Section~\ref{sec:seco} delivered as a finding across the three cases, with the caveat that the organisational and political contexts differed too --- the structural arrow we identify runs alongside, not instead of, political and governance differences."
→ "…with the caveat that the organisational and political contexts differed too; the structural arrow we identify runs alongside, not instead of, political and governance differences."
Reason: em-dash to semicolon; the second clause stands as its own thought.

**L.440** "Consul maintained its original monolithic architecture --- whether by choice or inertia --- which lowered the initial barrier to deployment but produced the fork-fragmentation pattern documented in Section~\ref{sec:consul}."
→ leave; em-dash pair brackets a short aside.

**L.440** "The architectural decisions correlate with very different ecosystem outcomes; the political and organisational confounds remain (Section~\ref{sec:evaluation})."
→ leave.

---

## §5.1 Architecture as Governance (447–457)

**L.450** "When the institutional backing collapsed in 2019, the dominator did not transition into a keystone --- it simply withdrew, and no successor keystone emerged."
→ "…the dominator did not transition into a keystone: it simply withdrew, and no successor keystone emerged."
Reason: em-dash to colon.

**L.450** "Polis fits the framework awkwardly: a single-developer keystone with no surrounding ecosystem to anchor. The framework's predictive power is strongest along the Decidim/Consul axis, where the two roles trade off cleanly; Polis is the limit case where the architecture cannot support an ecosystem at all."
→ The two sentences both say "Polis is the awkward case". Consider cutting the first ("Polis fits the framework awkwardly: a single-developer keystone with no surrounding ecosystem to anchor.") and keeping the second.
Reason: restatement.

**L.452** "Decidim's modular architecture did not just make the code flexible --- it made it possible for diverse communities to shape the platform without needing permission from the core team."
→ "Decidim's modular architecture did not just make the code flexible; it made it possible for diverse communities to shape the platform without needing permission from the core team."
Reason: em-dash to semicolon; the parallel is clearer.

**L.452** "The pattern reached its extreme with Madrid itself: the originating city now maintains a fork that is 12{,}725 commits ahead of upstream and was last touched in May 2023 (Section~\ref{sec:consul}). The architecture pushed even the originator into the fragmentation pattern that it forced on every other deployer."
→ This is the third time the paper makes the Madrid-forked-its-own-platform point (L.318, L.356, L.452). Consider trimming one of these three. The L.318 mention is in §4.2 where it's first introduced; the L.356 mention is the §4.2 conclusion; the L.452 mention is in §5.1 calling back. Cutting the L.356 one ("pushed even the originator into the fragmentation pattern") is the easiest because the same point lands again at L.452.
Reason: cross-section restatement.

**L.454** "Polis shows a different version of the same pattern."
→ leave; useful pivot sentence.

**L.454** "It is not technically wrong --- it is a reasonable approach to finding common ground in large groups. But it is also not neutral."
→ "It is not technically wrong; it is a reasonable approach to finding common ground in large groups. But it is also not neutral."
Reason: em-dash to semicolon.

**L.454** "Opinions that do not align with the principal components get compressed away --- they are still there in the raw data, but invisible in the output that decision-makers see."
→ "Opinions that do not align with the principal components get compressed away: they are still there in the raw data, but invisible in the output that decision-makers see."
Reason: em-dash to colon.

**L.456** "Civic tech is no different, except that the stakes are democratic rather than commercial."
→ leave.

---

## §5.2 SECO Research Gains (458–475)

**L.460** "though we apply them as qualitative lenses rather than with their full operationalised measurement frameworks (which would require longitudinal data on application survival rates, revenue flows, and developer retention that we do not have)"
→ leave.

**L.462** "Consul's peak in 2017--2019 generated 14{,}000 commits and 186 unique authors --- the kind of numbers that a productivity-only health assessment would treat as a thriving project."
→ "…generated 14{,}000 commits and 186 unique authors, the kind of numbers a productivity-only health assessment would treat as a thriving project."
Reason: em-dash as comma; also "that" → ø reads tighter.

**L.462** "By productivity measures the ecosystem looked fine; by democratic measures --- whether diverse communities can meaningfully shape the platform --- it had already failed long before the upstream collapsed."
→ leave; em-dash pair brackets a working definition.

**L.465** "We propose \emph{fork-divergence shape} --- the population pattern across the ahead-of-upstream and behind-upstream quadrants of a project's forks --- as a niche-creation diagnostic for civic tech platforms."
→ leave; appositive earns its dashes.

**L.465** "Healthy extension populates the upper-left of the ahead/behind plot: deployers keep up with upstream and add their own work, producing a stream of contributions that the upstream can in principle absorb."
→ leave.

**L.465** "This L-shape is the signature of an ecosystem that fragments instead of extending. The shape, not the count, is the diagnostic."
→ leave; the two sentences make different points (signature vs. claim).

**L.474** "The architecture-as-governance lens adds an evaluative layer beyond shape: not just ``is the ecosystem growing?'' but ``does the architecture enable the participation it claims to support?'' --- what \citet{palacin2024configurations} frame as ``which political values should be enforced by platform design.''"
→ "…but ``does the architecture enable the participation it claims to support?'', which \citet{palacin2024configurations} frame as ``which political values should be enforced by platform design.''"
Reason: em-dash plus comma plus quotation question mark is visually cluttered; "which" as a relative pronoun does the same job.

**L.474** "Any mission-driven ecosystem --- health technology, education, environmental monitoring --- faces similar tensions."
→ leave.

---

## §5.3 Implications (476–485)

**L.478** "International IDEA \citeyearpar{idea2026democracy} calls for a democracy stack but leaves the architectural decisions implicit --- the report frames the stack in terms of services and rights, not in terms of the technical commitments any such infrastructure must make."
→ "…but leaves the architectural decisions implicit; the report frames the stack in terms of services and rights, not in terms of the technical commitments any such infrastructure must make."
Reason: em-dash to semicolon.

**L.481** "the monolith forced Consul deployers to either accept the platform as-is or maintain their own fork, and 280 of them maintain forks today (Section~\ref{sec:disc-gov})."
→ This is the fifth time the paper quotes the "280 modified forks" figure (abstract; §4.2 L.316; §4.4 L.400 has it implicitly; §4.5 L.440; §5.3 L.481). Not a flag for cutting — the figure is the central empirical anchor — but flag for re-checking whether every restatement is doing work.
Reason: cross-section restatement check.

**L.481** "The trade-off is real --- modular maintenance is harder than monolithic maintenance --- but the alternative is fragmentation that the upstream cannot absorb. For a democracy stack that needs to accommodate diverse institutional contexts, the sustainability burden is the price of pluralism. Accept it deliberately."
→ "The trade-off is real (modular maintenance is harder than monolithic maintenance), but the alternative is fragmentation the upstream cannot absorb. For a democracy stack that needs to accommodate diverse institutional contexts, the sustainability burden is the price of pluralism. Accept it deliberately."
Reason: em-dash pair as parenthetical.

**L.483** "If the democratic problem requires deep algorithms --- consensus discovery in large groups, opinion clustering, statistical bridging between divided constituencies --- accept the thin ecosystem and the centralised expertise that comes with maintaining the algorithm."
→ leave; em-dash pair brackets a three-item list.

**L.484** "What is not workable is making one a façade for the other: deep algorithms wrapped in module language do not produce broad participation, and modular platforms with one statistical pipeline bolted on do not produce serious algorithmic capability."
→ leave.

---

## §5.4 Evaluating the Approach (486–502)

**L.488** "The approach worked well in some places and less well in others."
→ leave.

**L.490** "Where it worked best was the two-platform comparison. The causal chain there is unusually clean for a software study: Barcelona proposed modularising Consul, the proposal was rejected, Barcelona rewrote from scratch, and the resulting divergence produced the structural contrast we read consequences off in Section~\ref{sec:consul}. That said, architecture was not the only thing that differed. Barcelona and Madrid also had different governance cultures and different political trajectories --- Madrid's Ahora Madrid government lost power in 2019, which hurt Consul's institutional backing."
→ "…different governance cultures and different political trajectories; Madrid's Ahora Madrid government lost power in 2019, which hurt Consul's institutional backing."
Reason: em-dash to semicolon.

**L.494** "The Consul analysis added a fork-divergence enumeration across all 1{,}030 enumerable GitHub forks but did not perform the same code-level recovery as Decidim --- the monolithic structure makes that recovery harder and lower-value, but it is a real gap and a fair criticism."
→ "…did not perform the same code-level recovery as Decidim; the monolithic structure makes that recovery harder and lower-value, but it is a real gap and a fair criticism."
Reason: em-dash to semicolon.

**L.494** "The asymmetric depth is intentional but should not be papered over: only the Decidim case clears the bar of full Symphony-style architectural recovery."
→ leave.

**L.496** "GitHub metrics --- stars, forks, contributor counts --- are proxies, not direct measures of ecosystem health."
→ leave.

**L.498** "\emph{Single coder.} The architectural and ecosystem judgements --- which engine counts as ``shared service'', which fork counts as ``substantively modified'', which case fits which trade-off pattern --- were made by one author."
→ leave; em-dash pair brackets a three-item list.

**L.498** "The civic tech graveyard --- platforms that were architecturally ambitious but never reached production, or that failed in ways that made them invisible to a GitHub-centric methodology --- is invisible to this study."
→ leave; appositive earns it.

**L.498** "The trade-offs we identify are conditional on survival; they may miss tensions that kill platforms before they generate the empirical material we used."
→ leave.

---

## §6 Conclusion (504–524)

**L.508** "A decade of civic tech experience --- 7{,}000 commits of Decidim modules, 14{,}000 commits of Consul fragmenting into 280 modified forks, 8{,}000 commits of Polis dominated by one developer --- shows what happens when you navigate them in one direction versus another."
→ leave; appositive earns it.

**L.510** "For European policymakers debating democratic digital public infrastructure, this puts architecture on the same shelf as procurement and budgeting --- a governance choice that should be made deliberately rather than left as a procurement default."
→ "…this puts architecture on the same shelf as procurement and budgeting: a governance choice that should be made deliberately rather than left as a procurement default."
Reason: em-dash to colon.

**L.513** "But if Denmark wants participation infrastructure that lets diverse communities deliberate, adapt, and govern, the architectural lessons from a decade of civic tech suggest very different choices. The architecture is the democratic decision."
→ leave; closing punchline is doing real work.

**L.516** "Three platforms, however carefully selected, cannot represent all civic tech architectures --- the field includes at least 25 platforms with genuine architectural variety (from Django-based Adhocracy to LiquidFeedback's database-as-application approach)."
→ "Three platforms, however carefully selected, cannot represent all civic tech architectures; the field includes at least 25 platforms with genuine architectural variety (from Django-based Adhocracy to LiquidFeedback's database-as-application approach)."
Reason: em-dash to semicolon.

---

## §7 GenAI (525–545)

**L.534** "Analytical judgements --- what the data means, where the trade-offs cut, which findings deserve emphasis --- are the author's."
→ leave; appositive earns it.

**L.530** "(3)~drafting prose that the author reviewed, revised, and rewrote into the author's voice"
→ leave.

The GenAI section reads tight already.
