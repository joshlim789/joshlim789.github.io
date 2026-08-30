# Site notes — pending updates

Working notes for things the site needs, kept out of the rendered site
(`_quarto.yml` renders `**/*.qmd` only, so a `.md` file here is not published).

## The site and the CV disagree; the CV is right

The CV (github.com/joshlim789/cv) was reorganized around the methods work, and
`research.qmd` has not caught up. When you next touch the site, bring it in
line with `cv.tex` rather than the other way around.

### 1. Publications vs. conference abstracts — the important one

`research.qmd` lists three items under **Publications**, but two of them are
supplement abstracts, not peer-reviewed papers:

- Tirumalasetty et al. (2025), *JACI* 155(2 Suppl.), AB309 — AAAAI/WAO abstract
- Lim et al. (2023), *JACI* 151(2) — AAAAI abstract

Both are *also* listed again under **Posters and presentations**, so the same
work is counted twice on one page. The CV fixes this: one
`Peer-Reviewed Publications` section holding only the *AJNR* paper, and a
separate `Conference Abstracts and Presentations` section holding everything
else, with each item appearing exactly once.

Do the same here: leave only the *AJNR* paper under Publications, rename the
other section to "Conference abstracts and presentations," and delete the
duplicate entries.

### 2. Missing since the site was last updated

- **Working papers** — no section for them at all. Two are in preparation:
  *Bayesian Treatment Imputation for CATE Estimation Under Missing Binary
  Treatments* (with Reiter), and *Bayesian Causal Inference: A Practical Guide*
  (with Li), targeted at *JSS*.
- **Software** — no section. The `BayesCausal` R package belongs here once the
  repo is public.
- **FutureBAProf** (Tippie College of Business, Aug 2026) — selected from 117
  applicants; the invited pitch is not listed under presentations.
- **Honors** — no section for FutureBAProf, the Dean's Graduate Fellowship, or
  summa cum laude.
- `teaching.qmd` has the STA 199 TA (Fall 2026) and M.S.S. Bootcamp TA
  (Summer 2026) roles that were missing from the CV; those are now on the CV.

### 3. Course codes are wrong in four places

Confirmed correct on the CV; the site has the bare numbers. Fix these:

| File | Line | Currently | Should be |
|---|---|---|---|
| `index.qmd` | 37 | STA 199 | **STA 199L** |
| `teaching.qmd` | 10 | STA 199 (Summer 2026, Instructor of Record) | **STA 199L** |
| `teaching.qmd` | 21 | STA 721: Linear Models | **STA 721L: Linear Models** |
| `teaching.qmd` | 28 | STA 199 (Fall 2026, Teaching Assistant) | **STA 199CCL** |

Note the summer and fall entries take *different* codes — 199L for the course
Josh taught as instructor of record, 199CCL for the fall section he TAs. They
are not a typo for each other.

### 4. Small inconsistencies

- `index.qmd` says "third year Ph.D. candidate"; the CV says Ph.D. student.
  Pick one.
- `teaching.qmd` files the Johnson C. Smith workshop under "Mentoring and
  service"; the CV has it under Teaching Experience, which fits better.
- `cv.qmd` says "Last updated April 2026" and embeds `files/Lim_Joshua_CV.pdf`,
  a stale copy. The build in the `cv` repo publishes a rolling release, so this
  can point at
  `https://github.com/joshlim789/cv/releases/latest/download/cv.pdf`
  and stop going out of date — once that repo is public.
