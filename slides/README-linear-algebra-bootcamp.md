# Linear Algebra Review — Duke StatSci Ph.D. Bootcamp

Quarto `revealjs` slides, UCLA blue-and-gold, built from last year's Beamer deck
(*Linear Algebra Review*, R. Rossetti, Aug 2025) with the self-assessment packets
interwoven as "Your turn" prompts.

## Files

| File | What it is |
|---|---|
| `linear-algebra-bootcamp.qmd` | The deck. 77 slides across 10 sections, 21 practice prompts. |
| `ucla.scss` | Theme. All colors are variables at the top of the file. |

## Rendering

```bash
quarto render linear-algebra-bootcamp.qmd
# or, while writing:
quarto preview linear-algebra-bootcamp.qmd
```

No extensions and no R execution required — the one R block in the SVD section is
illustrative only, so the deck renders with the markdown engine. `chalkboard: true` is on (press `B` during the talk to
draw), and speaker notes work out of the box (press `S`).

The deck is part of the website project and renders with it. It is excluded from
the site search index (`search: false`) so its slides don't swamp the four real
pages; it still appears in `sitemap.xml`. It is linked from the Ph.D. Bootcamp
entry on `teaching.qmd`.

## Typography and fit

Body and headings are **Atkinson Hyperlegible**, the Braille Institute's
legibility face and the same font the STA 199 site loads.

Sizing, for reference: the root is **35px**, and content slides carry
`{.smaller}`, so body text renders at about **28px** — matching last year's
Beamer deck, which ran roughly 28px equivalent in reveal's 1050×700 canvas (11pt
on a 128×96mm frame). To resize the deck, change `$presentation-font-size-root`
and nothing else; effective body size is that number × 0.8, and overflow scrolls
rather than breaking. Atkinson is wider than a typical sans — if you swap the
font, revisit the root size at the same time.

Overflow is handled in three places, in this order:

1. **Density.** Panel padding, list margins, and display-math margins are all
   tightened in `ucla.scss`. Display math in particular ships with ~1em margins
   top and bottom, which costs a full line of text per equation.
2. **Structure.** Practice slides carrying a long prompt *and* a long answer are
   split in two, with the title repeated verbatim so advancing reads as the
   answer appearing in place.
3. **Scrolling.** `scrollable: true` is set deck-wide, so anything still too tall
   scrolls rather than spilling off the slide. Note how Quarto implements this:
   not by tagging each section, but with `overflow-y: auto` on
   `.reveal .slide:not(.center)`. Style scrollbars against the slide itself; the
   `.scrollable` class is only present on some sections and is not the mechanism.

Nothing shrinks text at runtime — an earlier build did, and it made the deck
unreadable. Text size is fixed and predictable; long slides scroll.

## How the deck is organized

Each concept slide is followed by a `.your-turn` box holding a packet question,
then a `. . .` fragment revealing an `.answer` box. Nothing is hidden from the
rendered HTML — students get the answers when they revisit the slides, which is
what you want for a self-assessment.

Recurring callout classes:

- `.defn` — definitions (blue)
- `.thm` — theorems (dark blue)
- `.your-turn` — practice prompts (gold)
- `.answer` — answer sketches
- `.note` / `.warn` — asides and traps
- `.tier .baseline` / `.bridge` / `.stretch` / `.challenge` — the packet tier badges

## Scope

The 2025 deck's five sections are the spine, extended only where the bootcamp
needed more room:

| Section | Relative to 2025 |
|---|---|
| Vector Spaces | as before |
| Inner Products and Orthogonality | expanded — Pythagoras, orthogonal complements, Gram–Schmidt |
| Linear Maps and Matrices | as before, plus elimination and the four fundamental subspaces |
| Special Matrices and Scalars | as before |
| Projections | as before, plus regression *is* projection |
| Eigenvalues, Eigenvectors, and Diagonalization | expanded — similarity, multiplicities, the diagonalizability criterion, matrix powers, the spectral theorem |
| Positive Definiteness | as before |
| Singular Value Decomposition | expanded — construction, geometry, conditioning, ridge, pseudo-inverse, Eckart–Young, PCA |
| Block Matrices | as before, Schur complement and Kronecker products |

**Deliberately not covered:** quadratic forms and completing the square,
covariance geometry and whitening, and Sherman–Morrison–Woodbury with the
leave-one-out / PRESS payoff. These were drafted and cut to keep the deck to a
bootcamp day; they are recoverable from git history if a future year wants them.

## Questions used

Companion review Q1–Q15 and Q18–Q24; Stage 1 Q2 and Q8(b)–(c); Stage 2 Q2.

**Skipped:** Companion Q16 and Q17 (change-of-coordinates matrices). The
underlying idea is covered conceptually on the *Similarity* slide. If you want
them back, they slot in cleanly right after that slide. Stage 2 Q1, Q3 and Q4
went with the sections listed above.

## Three fixes worth knowing about

Carried over from the 2025 deck and corrected here:

1. The PSD slide said positive semi-definite matrices have "non-negative
   **eigenvectors**" — should be eigenvalues.
2. The SVD slide defined singular values as the positive eigenvalues of `AᵀA`;
   they are the **square roots** of those eigenvalues. Same slide said `U` and
   `V` hold singular *values* rather than singular *vectors*.
3. The Schur complement slide defined `M/A ≜ D − BD⁻¹C`; it should be
   `M/A ≜ D − CA⁻¹B`.

The deck flags #1 and #2 explicitly for students (they're worth pointing at),
and quietly states #3 correctly.
