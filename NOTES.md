# Site notes — pending decisions

Working notes, kept out of the rendered site (`_quarto.yml` renders `**/*.qmd`
only, so a `.md` file here is not published).

## Brought in line with the CV on 2026-08-30

The site had drifted from `github.com/joshlim789/cv`, which is authoritative.
Fixed in that pass:

- **Publications vs. conference abstracts.** `research.qmd` had listed the two
  *JACI* supplement abstracts under Publications *and* again under Posters and
  presentations — the same work counted twice. Publications now holds only the
  peer-reviewed *AJNR* paper; everything else sits once under "Conference
  abstracts and presentations." **Keep it that way.**
- **Working papers** and **Software** sections added to `research.qmd`.
- **Honors** section added to `index.qmd` (FutureBAProf, Dean's Graduate
  Fellowship, summa cum laude).
- **FutureBAProf** invited pitch added under conference abstracts.
- **Course codes** corrected to STA 199L, STA 199CCL, STA 721L. Note the summer
  and fall entries take *different* codes — 199L for the course Josh taught as
  instructor of record, 199CCL for the fall section he TAs. Not a typo for each
  other; do not find-and-replace them together.
- **Johnson C. Smith workshop** moved out of "Mentoring and service" into its
  own institution heading, matching the CV's placement under teaching, and
  expanded with the NSF funding, the 12 students, and the base-R materials.
- **Research interest tags** on `index.qmd` widened to match the CV.
- `files/Lim_Joshua_CV.pdf` replaced with a fresh build; `cv.qmd` date bumped
  to August 2026.
- **Ph.D. candidate, not student.** The site had this right and the CV had it
  wrong; the CV was corrected on 2026-08-30. Do not change the site to
  "student."
- **No resume is linked, by decision.** Two exist in the `cv` repo —
  `resume-ds.tex` and `resume-rs.tex` — and Josh chose on 2026-08-30 to publish
  neither. Publishing both side by side advertises that the targeting is
  adjustable and puts a reader from one track in front of the version written
  for the other; the resumes go out per application instead. Do not add a
  resume link to the site.

## Still open

### 1. The CV PDF is still a manual copy

`cv.qmd` embeds `files/Lim_Joshua_CV.pdf`, which has to be re-copied by hand
after every CV change. The build in the `cv` repo publishes a rolling release,
so this could point at

```
https://github.com/joshlim789/cv/releases/latest/download/cv.pdf
```

and stop going stale — but that repo is **private**, so the URL 404s for
visitors. Switch to it if and when the repo is made public.
