# Photos for the Other page

Drop image files in this folder, then tell Claude which section each one belongs
to — or add them yourself using the commented example at the bottom of
`other.qmd`.

## Read this first

**Everything in this folder is published to the public internet.** `_quarto.yml`
lists `img/other/**` as a site resource, so files here are copied to the live
site whether or not any page links to them. Don't use this folder as a staging
area for photos you haven't decided about — keep those somewhere else until
you're sure.

## What works well

- **JPG** for photographs, **PNG** for anything with text or flat colour.
- **Around 1600px on the long edge** is plenty. The grid displays them at about
  400px wide, and a 6MB phone photo makes the page slow for no visible gain.
- **Landscape (4:3-ish)** fits the grid without cropping. Portrait shots work
  too — they get `class="tall"` so they aren't squeezed into a ribbon.

## Naming

Lowercase, hyphens, no spaces, and say what the photo is:

```
gymnastics-ucla-nationals-2023.jpg
volleyball-team-2026.jpg
chinese-dance-lunar-new-year.jpg
```

Not `IMG_4471.HEIC`. Note that **HEIC files won't display in browsers** — if
they come off an iPhone, export them as JPG first.

## For each photo, jot down

Whatever you can, in `OTHER-IDEAS.md` at the repo root:

- which section it goes under
- a one-line caption, if it needs one
- who else is in it

That last one matters. Photos of other people go on a public site under your
name, and it's worth a moment's thought about whether they'd want that —
especially for anything from a team or a performance.
