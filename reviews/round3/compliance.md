# Phase 3 — ITU formal-requirements compliance check

Course: KIREPRO1PE (Research Project, 7.5 ECTS), MSc Software Design, Spring 2026.
Paper: `main.tex` / `main.pdf`, 31 PDF pages, single author.

## 1. Verdict

**Mostly compliant, with one hard fail on page count.** The paper has the required structural pieces (title page with all the right elements, abstract, intro, method, analysis, discussion, conclusion, references, AI declaration), the supervisor and programme are correctly named, the bibliography format is conventional, and the AI declaration is more detailed than ITU's minimum. The hard fail is size: ITU's table for a 7.5 ECTS, 1-student project gives **15–19 body pages**; the body of this paper measures ~26 PDF pages and ~30 ITU standard pages (2,400 char) — roughly 1.5× the upper limit. Submission deadline is **Friday 15 May 2026 in LearnIT**. One day to fix the size; everything else is fine or can be confirmed with the supervisor.

## 2. Per-requirement table

| # | Requirement | Source | Status |
|---|---|---|---|
| 1 | Body page count within 15–19 pages (7.5 ECTS, 1 student) | Workload and Project Size | **Fail** |
| 2 | Standard-page size (2,400 chars/page) used for the count | Workload and Project Size | **Fail** (~30 std pages) |
| 3 | Title page present | Submitting written work | Pass |
| 4 | Title page: programme name | Submitting written work / Curriculum §1 | Pass |
| 5 | Title page: course / ECTS | Submitting written work | Pass |
| 6 | Title page: student name | Submitting written work | Pass |
| 7 | Title page: supervisor name | Submitting written work | Pass |
| 8 | Title page: date | Submitting written work | Pass |
| 9 | Title page: course code (KIREPRO1PE) | Implicit / good practice | **Partial** (course code not on title page) |
| 10 | Abstract present | Standard academic structure / howto_research | Pass |
| 11 | Table of contents | Implied by ITU's body-exclusion rule | Pass |
| 12 | Introduction | howto_research / project_guide | Pass |
| 13 | Method | project_guide (problem definition + method section) | Pass |
| 14 | Analysis / Results | howto_research | Pass |
| 15 | Discussion | howto_research | Pass |
| 16 | Conclusion | howto_research | Pass |
| 17 | References / bibliography | Checklist and advice | Pass |
| 18 | Citation style (numeric [n] or author-year acceptable) | Checklist and advice | Pass (natbib author-year) |
| 19 | No Wikipedia citations | Checklist and advice | Pass |
| 20 | Web references in the reference list (not footnotes) | Checklist and advice | Pass |
| 21 | Footnotes minimised | Checklist and advice | **Partial** (one footnote on page 1) |
| 22 | Research question / problem statement well-formed | Problem Statement guide | Pass |
| 23 | Language: English | Curriculum §6 | Pass |
| 24 | Use of Generative AI declaration | Checklist and advice (2025 ITU rule) | Pass |
| 25 | Submission format: PDF in LearnIT | Submitting written work | Pass (will export PDF) |
| 26 | Sensible filename (not `main.pdf`) | Checklist and advice | **Fail** (file is `main.pdf`) |
| 27 | Deadline Friday 15 May 2026 | learnIT course page | Author's responsibility |
| 28 | Preliminary Problem Statement submitted (20 Feb deadline) | learnIT course page | Author's responsibility (out of scope here) |

## 3. Failures and partials

### Fail — body page count

> "1 student … 7.5 ECTS project: 15-19 pages" (Workload and Project Size)
> "A standard page is 2,400 units per page, including spaces and notes. … The body does not include: front page, colophon, table of contents, abstract, bibliography, appendices and illustrations and charts."

Two ways to measure, both fail:

- **PDF pages, Introduction (printed p.3) through Conclusion (printed p.28)** = 26 pages. The "Use of Generative AI" section pushes to printed p.29; references run p.29–30 (printed); pp.27 cover, abstract, TOC.
- **ITU standard pages** (2,400 chars/page, body only, measured with `pdftotext` over physical pages 4–28) = 72,707 chars ÷ 2,400 ≈ **30.3 standard pages**.

Either way the body is roughly 1.5× the 15–19 upper limit. The Workload page says the supervisor has the final word, so the cleanest fix is an explicit written approval from Konstantinos Manikas for the extended length. Without that, this is a formal violation. Cutting to size is the alternative; that is a content task and out of scope for this check.

### Fail — filename

> "When you send documents to others, give them a name that makes sense to the recipient. Half the documents I receive are called rapport.docx, draft.pdf, main.pdf or similar." (Checklist and advice, Sestoft)

The compiled PDF is `main.pdf`. Rename to something like `LeoSandvigAndersen_ResearchProject_KIREPRO1PE_May2026.pdf` (or whatever pattern Manikas prefers) before uploading.

### Partial — course code missing on title page

The title page shows "Research Project (7.5 ECTS)" but not the course code **KIREPRO1PE**. ITU's submission guides don't list a strict template, but the course code is the unambiguous identifier and is normally on the front page of ITU written work. Add a single line:

```
Course code   KIREPRO1PE
```

While editing the title page, consider also adding the date in full (e.g. "15 May 2026" instead of "May 2026") — this matches the submission deadline format on the course page.

### Partial — footnote on page 1

> "In general, avoid footnotes: They interrupt the flow of reading, mess up the page layout, and too often contain information that is either completely irrelevant or so important that it ought to be in the running text." (Checklist and advice)

There is one footnote in the introduction ("European Commission, DESI 2022; UN E-Government Survey 2024.") that gives source attribution. ITU's guide says either inline it or move it to the bibliography. Either is a small fix. Not a blocker.

## 4. Things that look fine

- Title page layout, ITU logo, programme name, supervisor name, author name, ECTS, English-language commitment all correct.
- Supervisor name spelled correctly: **Konstantinos Manikas**.
- Abstract on its own page, before TOC; no references in the abstract.
- Section order is the textbook ITU/howto_research structure: Intro → Background → Method → Analysis → Discussion → Conclusion → AI declaration → References.
- Research question is explicitly stated and italicised in §1 ("what software architecture trade-offs must builders of democratic digital infrastructure navigate?"), with context-complication-proposal structure across the introduction. This matches the Problem Statement guide's expected shape.
- Bibliography style `plainnat` with `natbib` is one of the two styles the Sestoft checklist accepts; 32 entries, all properly formatted, no Wikipedia, web sources in the reference list rather than as footnotes.
- AI declaration is unusually thorough — covers tool, models, how used, how prompts were structured, what the author did independently, and copyrighted-material handling. Exceeds the minimum the 2025 ITU rule asks for.
- Figures generated reproducibly from data (figures/ folder), captions present, all referenced from the text.

## 5. Ambiguous — confirm with supervisor or SAP

- **Page-count limit waiver.** Workload page says "Your supervisor has the final word on the workload, page limit and syllabus". If Manikas has approved 25–30 standard pages in writing (email, supervision agreement), the §3 page-count fail becomes a recorded supervisor-approved deviation. Without written approval, it is a deviation from the published table.
- **Course code placement.** No ITU document I read specifies that the course code must be on the title page. Strongly recommended for unambiguity but not formally mandated.
- **AI declaration template.** The 2025 ITU GenAI policy (https://itustudent.itu.dk/Study-Administration/Generative-AI, referenced in the Sestoft checklist) requires a declaration "how you have used generative AI during the project, also for coding etc." There is no fixed template in the documents reviewed. Worth a quick check that the SAP page does not require a specific form/checkbox.
- **Preliminary Project Statement.** The learnIT course page says it was due **Friday 20 February 2026**. This is a separate deliverable from the final report; the present file does not contain or refer to it. Confirm it was submitted.

## 6. Submission-readiness checklist

Before uploading to LearnIT on **Friday 15 May 2026**:

- [ ] **Page count.** Either cut the body to 15–19 pages / ≤19 standard pages, or get written supervisor approval for the extended length. Forward the approval to SAP if asked.
- [ ] **Filename.** Rename `main.pdf` to something descriptive, e.g. `LeoSandvigAndersen_ResearchProject_KIREPRO1PE_2026.pdf`.
- [ ] **Course code on title page.** Add `Course code  KIREPRO1PE` to the title-page table.
- [ ] **Date.** Replace "May 2026" with the exact submission date or "15 May 2026".
- [ ] **Footnote on page 1.** Inline the DESI/UN sources or move to the reference list.
- [ ] **Preliminary Project Statement.** Confirm it was settled by the 20 February deadline; have a copy at hand for the oral defence if applicable.
- [ ] **Final PDF check.** Compile cleanly with no LaTeX warnings; all figures embedded; all `\cite` keys resolve; TOC up to date.
- [ ] **Plagiarism scan.** LearnIT runs an automatic check; nothing to do, but be aware.
- [ ] **Double-submit safety.** The submission cannot be edited after upload — submit a final PDF, not a draft.
