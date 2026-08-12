#!/usr/bin/env python3
"""Build the instructor solution manual from the deck source.

Reads linear-algebra-bootcamp.qmd, pulls out every practice problem and its
worked solution, and writes solutions.qmd. Problems that span several slides
(prompt on one, answer on the next) are stitched back into a single entry, and
each entry is stamped with the slide number it appears on so you can find it
while presenting.

Run from the project root:  python3 slides/make-solutions.py
"""
import re
import sys
import pathlib

HERE = pathlib.Path(__file__).parent
DECK = HERE / 'linear-algebra-bootcamp.qmd'
OUT = HERE / 'solutions.qmd'

PRESENTATIONAL = {'midi', 'smaller', 'small', 'xsmall', 'large',
                  'columns', 'column', 'incremental'}
LABELS = {'defn': 'Definition', 'thm': 'Theorem',
          'note': 'Note', 'warn': 'Watch out'}
TIERS = {'baseline': 'Baseline', 'bridge': 'Bridge',
         'stretch': 'Proof stretch', 'challenge': 'Challenge'}


def is_open(line):
    s = line.strip()
    return s.startswith(':::') and bool(s.lstrip(':').strip())


def is_close(line):
    s = line.strip()
    return bool(s) and set(s) == {':'}


def div_class(line):
    m = re.match(r'^:::+\s*\{\.([A-Za-z-]+)', line.strip())
    return m.group(1) if m else None


def split_slides(text):
    """Return [(level, title, body_lines)] in document order."""
    body = text.split('---\n', 2)[2]
    slides, cur = [], None
    for line in body.split('\n'):
        if line.startswith('# ') or line.startswith('## '):
            if cur:
                slides.append(cur)
            lvl = 1 if line.startswith('# ') else 2
            # strip only a trailing attribute block ({.smaller}); leave LaTeX
            # braces such as \mathbf{A} alone
            title = re.sub(r'\s*\{\.[^}]*\}\s*$', '', line.split(' ', 1)[1]).strip()
            cur = [lvl, title, []]
        elif cur:
            cur[2].append(line)
    if cur:
        slides.append(cur)
    return slides


def extract_divs(lines, wanted):
    """Pull top-level divs whose class is in `wanted`; return (matched, rest)."""
    matched, rest, i = [], [], 0
    while i < len(lines):
        if is_open(lines[i]) and div_class(lines[i]) in wanted:
            depth, j = 1, i + 1
            while j < len(lines) and depth:
                if is_open(lines[j]):
                    depth += 1
                elif is_close(lines[j]):
                    depth -= 1
                j += 1
            matched.append(lines[i + 1:j - 1])
            i = j
            continue
        rest.append(lines[i])
        i += 1
    return matched, rest


def checkmarks(text):
    """U+2713 has no glyph in the default PDF fonts, so swap in \\checkmark.

    It appears both inside math (`= 0. \\ ✓`) and in running prose, and the
    replacement differs: bare inside math mode, dollar-wrapped outside. Getting
    this backwards produces a nested `$` and a LaTeX failure.
    """
    parts = re.split(r'(\$\$.*?\$\$|\$[^$\n]*\$)', text, flags=re.S)
    for i, part in enumerate(parts):
        if '✓' not in part:
            continue
        inside = part.startswith('$')
        parts[i] = part.replace('✓', r'\checkmark' if inside else r'$\checkmark$')
    return ''.join(parts)


def clean(lines):
    """Flatten presentational divs, relabel callouts, drop fragment markers."""
    out = []
    for line in lines:
        s = line.strip()
        if s == '. . .':
            continue
        cls = div_class(line)
        if cls in PRESENTATIONAL:
            continue
        if cls in LABELS:
            out.append(f'> **{LABELS[cls]}.**')
            continue
        if is_close(line):
            continue
        if is_open(line):
            continue
        out.append(line)
    text = '\n'.join(out)
    # tier badge and packet citation are shown in the entry header instead
    text = re.sub(r'\[([^\]]+)\]\{\.tier[^}]*\}', r'', text)
    text = re.sub(r'\*\([^)]*(?:Companion|Stage)[^)]*\)\*', '', text)
    text = re.sub(r'^[ \t]+$', '', text, flags=re.M)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = checkmarks(text)
    return text.strip()


def tier_of(lines):
    for line in lines:
        m = re.search(r'\[([^\]]+)\]\{\.tier\s+\.([a-z]+)\}', line)
        if m:
            return TIERS.get(m.group(2), m.group(1))
    return None


def source_of(lines):
    for line in lines:
        m = re.search(r'\*\(([^)]*(?:Companion|Stage)[^)]*)\)\*', line)
        if m:
            return m.group(1)
    return None


def main():
    text = DECK.read_text()
    slides = split_slides(text)

    # Reveal numbers the title slide 1, then every heading in order.
    numbered, n = [], 1
    for lvl, title, body in slides:
        n += 1
        numbered.append((n, lvl, title, body))

    # group consecutive level-2 slides sharing a title
    groups, section = [], ''
    for num, lvl, title, body in numbered:
        if lvl == 1:
            section = title
            continue
        if groups and groups[-1]['title'] == title and groups[-1]['section'] == section:
            groups[-1]['body'] += body
            groups[-1]['last'] = num
        else:
            groups.append({'section': section, 'title': title, 'body': list(body),
                           'first': num, 'last': num})

    problems = [g for g in groups if g['title'].lower().startswith('your turn')]
    if not problems:
        sys.exit('no practice problems found -- has the deck changed shape?')

    out = []
    out.append('---')
    out.append('title: "Linear Algebra Review --- Solution Manual"')
    out.append('subtitle: "Duke StatSci Ph.D. Bootcamp · instructor copy"')
    out.append('author: "Josh Lim"')
    out.append('date: today')
    out.append('date-format: long')
    out.append('toc: true')
    out.append('toc-depth: 2')
    out.append('number-sections: false')
    out.append('format:')
    out.append('  pdf:')
    out.append('    pdf-engine: xelatex')
    out.append('    documentclass: article')
    out.append('    geometry: margin=1in')
    out.append('    fontsize: 11pt')
    out.append('    colorlinks: true')
    out.append('  html:')
    out.append('    theme: cosmo')
    out.append('    embed-resources: true')
    out.append('    toc-location: left')
    out.append('---')
    out.append('')
    out.append(f'*Generated from `linear-algebra-bootcamp.qmd` — '
               f'{len(problems)} problems. Regenerate with '
               f'`python3 slides/make-solutions.py`.*')
    out.append('')

    current = None
    for idx, g in enumerate(problems, 1):
        if g['section'] != current:
            current = g['section']
            out.append(f'\n# {current}\n')

        short = re.sub(r'^[Yy]our turn:\s*', '', g['title']).strip()
        if short and short[0].isalpha():
            short = short[0].upper() + short[1:]
        span = (f"slide {g['first']}" if g['first'] == g['last']
                else f"slides {g['first']}–{g['last']}")
        out.append(f'## {idx}. {short}\n')

        prompts, rest = extract_divs(g['body'], {'your-turn'})
        answers, rest = extract_divs(rest, {'answer'})

        meta = [span]
        flat = [l for p in prompts for l in p]
        t = tier_of(flat)
        if t:
            meta.append(t)
        src = source_of(flat)
        if src:
            meta.append(src)
        out.append(f'*{" · ".join(meta)}*\n')

        out.append('**Problem.**\n')
        out.append(clean([l for p in prompts for l in p]) or '*(see slide)*')
        out.append('')
        out.append('**Solution.**\n')
        sol = '\n\n'.join(clean(a) for a in answers if clean(a))
        out.append(sol or '*(worked live)*')
        out.append('')

        commentary = clean(rest)
        if commentary:
            out.append('**Remarks.**\n')
            out.append(commentary)
            out.append('')

    OUT.write_text('\n'.join(out) + '\n')
    print(f'wrote {OUT} — {len(problems)} problems across '
          f'{len(set(g["section"] for g in problems))} sections')
    for i, g in enumerate(problems, 1):
        span = (g['first'] if g['first'] == g['last']
                else f"{g['first']}-{g['last']}")
        print(f'  {i:2d}. [{span:>7}] {g["title"]}')


if __name__ == '__main__':
    main()
