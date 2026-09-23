# Showcase artwork

The mastheads are original vector compositions extending the visual family of [Epistemic Skills](https://github.com/ZMS-Labs/epistemic-skills). The connecting lines are conceptual artwork. They do not depict infrastructure, a network, or an operational workflow. Both carry the line "What I've been building with AI, and how it's actually going," set on two lines. The phone version, `zms-labs-mobile.svg`, keeps only the wordmark and that line so the profile text starts sooner on a small screen.

Rebuild with Python and `fonttools`:

```bash
python profile/assets/render_assets.py
```

The small SVG drawing helper is adapted from Epistemic Skills' GPL-3.0 [documentation asset generator](https://github.com/ZMS-Labs/epistemic-skills/blob/b2c7270ee53142046e1fda38980053d2dd7906fb/docs/assets/render_assets.py). This repository retains that license for its code and compositions.

The bundled, unmodified Archivo font is distributed under the [SIL Open Font License](fonts/OFL.txt), separately from the repository license. Its source is [Google Fonts / Archivo](https://github.com/google/fonts/tree/main/ofl/archivo), and its SHA-256 is `0e094a7d3c7c4c25cf1310c4b30014f1dae9332220b1c2c88f4fa996f0b05053`.

SVG lettering is converted to paths. Reading the README requires no font installation or remote font request.

## Organization avatar candidates

`avatar-candidates/` holds three candidate marks for the GitHub organization avatar. They use the masthead's palette and type: ink `#152c35`, warm white `#f5f3ed`, accent orange `#ffac70` and Archivo weight 760. Each candidate is a 512x512 SVG with a rasterized 512x512 PNG, because GitHub avatar upload requires a raster format:

| Candidate | Mark |
|---|---|
| `candidate-1-squares` | The 2x2 squares glyph: three warm-white rounded squares and one orange, generous margins |
| `candidate-2-zms-lockup` | A square "ZMS" lockup: Archivo 760 outlined paths on ink, one orange square seated on the baseline |
| `candidate-3-masthead-crop` | A crop-style echo of the masthead: ink field, one muted connector line `#68848f` broken by a small orange square |

Candidate 2, the ZMS lettermark, was selected and applied as the organization avatar on 2026-09-20. Its explicit initials identify the organization while its Archivo typography and ink, warm-white and orange palette match the mastheads. The alternatives remain here as design history: candidate 1 reads clearly at small sizes but is more generic; candidate 3 echoes the masthead but is too abstract to identify the organization on its own.

Each mark was rendered and inspected at 32 px for avatar-size legibility. Contrast against the ink field: warm white 13.1:1, orange 7.9:1, connector 3.7:1.

Regenerate the SVGs and PNGs from `profile/assets/avatar-candidates/generate_avatar_candidates.py` (requires `fonttools`; the PNG pass additionally requires Playwright with its Chromium browser):

```bash
python profile/assets/avatar-candidates/generate_avatar_candidates.py
```

Adding `--preview DIR` also writes 32 px renders, plus a magnified view of those exact pixels, for legibility checks.

Changing these repository assets does not update the GitHub organization avatar. The selected PNG must be uploaded separately in GitHub organization settings; this generator only creates the image files.
