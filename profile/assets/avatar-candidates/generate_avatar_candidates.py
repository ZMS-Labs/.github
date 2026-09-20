#!/usr/bin/env python3
"""Build GitHub org avatar candidates from the profile identity system.

Emits three 512x512 SVG marks derived from the masthead vocabulary in
profile/assets/render_assets.py (ink field, warm white, one orange accent)
and rasterizes each to a 512x512 PNG, because GitHub org avatars must be
uploaded in a raster format. Requires fonttools for the SVGs and Playwright
(headless Chromium) for the PNGs.

Candidate 2, the ZMS lettermark, was selected and applied as the organization
avatar on 2026-09-20. This script only produces the image files; changing
repository assets does not update the GitHub organization setting. An
authorized agent with authenticated UI access can upload the selected PNG.

--preview DIR additionally renders each mark at 32 px (plus a pixelated 8x
view of that 32 px raster) so legibility at avatar sizes can be inspected.
"""
# SPDX-License-Identifier: GPL-3.0-only
# Drawing helper reused from profile/assets/render_assets.py, which is
# adapted from ZMS-Labs/epistemic-skills.
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent))

from render_assets import INK, ORANGE, PAPER, Drawing, face  # noqa: E402

SIZE = 512
CONNECTOR = '#68848f'  # muted connector line, review-directed accent for the crop mark
NAMES = ('candidate-1-squares', 'candidate-2-zms-lockup', 'candidate-3-masthead-crop')


class Candidate(Drawing):
    """A Drawing that saves into this directory rather than profile/assets/."""

    def save(self, name):
        (ROOT / name).write_text('\n'.join(self.parts) + '\n</svg>\n', encoding='utf-8')


def squares():
    """Candidate 1: the 2x2 squares glyph, one square orange, rounded, generous margins."""
    d = Candidate(SIZE, SIZE, 'ZMS Labs avatar candidate 1 — squares glyph',
                  'Four rounded squares in a 2x2 grid on the ink field: three warm white, one accent orange.')
    margin, gap = 96, 48
    sq = (SIZE - 2 * margin - gap) // 2  # 136
    for row, y in enumerate((margin, margin + sq + gap)):
        for col, x in enumerate((margin, margin + sq + gap)):
            accent = row == 1 and col == 1
            d.rect(x, y, sq, sq, ORANGE if accent else PAPER, rx=30)
    d.save(NAMES[0] + '.svg')


def zms_lockup():
    """Candidate 2: square ZMS lockup, Archivo 760 outlined paths, one orange square accent."""
    d = Candidate(SIZE, SIZE, 'ZMS Labs avatar candidate 2 — ZMS lockup',
                  'ZMS letterforms in Archivo weight 760 as outlined paths on the ink field, '
                  'with one accent orange square seated on the baseline after the letters.')
    weight, width = 760, 93  # masthead ZMS instance
    font = face(weight, width)
    upem = font['head'].unitsPerEm
    cap_ratio = font['OS/2'].sCapHeight / upem  # 0.686
    advance = sum(font['hmtx'][font.getBestCmap()[ord(c)]][0] for c in 'ZMS') / upem
    square_ratio, gap_ratio = 0.34 * cap_ratio, 0.35  # accent square as a share of type size
    target, margin = 384.0, 64.0  # content width keeps generous side margins
    size = target / (advance + square_ratio * (1 + gap_ratio))
    cap, sq = cap_ratio * size, square_ratio * size
    gap = gap_ratio * sq
    x, baseline = margin, SIZE / 2 + cap / 2
    end = d.text('ZMS', x, baseline, size, weight=weight, width=width)
    d.rect(x + end + gap, baseline - sq, sq, sq, ORANGE)
    d.save(NAMES[1] + '.svg')


def masthead_crop():
    """Candidate 3: crop-style mark echoing the masthead connectors."""
    d = Candidate(SIZE, SIZE, 'ZMS Labs avatar candidate 3 — masthead crop',
                  'A crop-style mark echoing the masthead connectors: ink field, one muted connector '
                  'line broken by a small accent orange square at the center.')
    y, stroke = SIZE / 2, 36
    half, gap = 52, 32  # orange square half-size and breathing room around it
    d.path(f'M112 {y:g} H{SIZE / 2 - half - gap:g}', CONNECTOR, stroke)
    d.path(f'M{SIZE / 2 + half + gap:g} {y:g} H400', CONNECTOR, stroke)
    d.rect(SIZE / 2 - half, SIZE / 2 - half, 2 * half, 2 * half, ORANGE)
    d.save(NAMES[2] + '.svg')


def rasterize():
    """Screenshot each SVG in headless Chromium at exactly 512x512."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': SIZE, 'height': SIZE}, device_scale_factor=1)
        for name in NAMES:
            page.goto((ROOT / f'{name}.svg').as_uri())
            page.screenshot(path=ROOT / f'{name}.png')
        browser.close()


def previews(out_dir: Path):
    """Render each mark at 32 px and an 8x pixelated view of that raster, for legibility checks."""
    from playwright.sync_api import sync_playwright
    out_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        small = browser.new_page(viewport={'width': 32, 'height': 32}, device_scale_factor=1)
        zoom = browser.new_page(viewport={'width': 256, 'height': 256})
        for name in NAMES:
            small.goto((ROOT / f'{name}.svg').as_uri())
            # The SVG roots carry fixed 512px size attributes; scale them to the
            # 32px viewport or the screenshot only captures an ink corner.
            small.eval_on_selector('svg', 'el => {el.style.width="32px";el.style.height="32px";}')
            tiny = out_dir / f'{name}-32.png'
            small.screenshot(path=tiny)
            page_html = out_dir / f'{name}-32.html'
            page_html.write_text(
                '<!doctype html><meta charset="utf-8"><style>img{display:block;width:256px;'
                f'height:256px;image-rendering:pixelated}}</style><img src="{tiny.name}">',
                encoding='utf-8')
            zoom.goto(page_html.as_uri())
            zoom.screenshot(path=out_dir / f'{name}-32-x8.png')
        browser.close()


if __name__ == '__main__':
    squares()
    zms_lockup()
    masthead_crop()
    rasterize()
    print('Rendered 3 avatar candidate SVGs and 512x512 PNGs in', ROOT)
    if '--preview' in sys.argv:
        out = Path(sys.argv[sys.argv.index('--preview') + 1])
        previews(out)
        print('Wrote 32 px legibility previews to', out)
