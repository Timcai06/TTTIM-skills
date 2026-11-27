# Visual & Typography Specification (`TTT-Readme-skill`)

## 1. Transparent Magazine Exhibition Panels (`scripts/editorial_panel.py`)

Why exhibition panels beat raw screenshots and boxy diagrams:
- A **`1800px` transparent RGBA canvas** has **no outer box**. Display typography, hairlines, and framed images sit directly on GitHub's `#0d1117` (dark) and `#ffffff` (light) backgrounds like a printed Swiss editorial spread.
- Bundled SIL OFL typefaces in `assets/fonts/` guarantee identical rendering across machines:
  - **Display (`BigShoulders-Bold.ttf`, `148–170px`)**: Bold condensed grotesque for left-aligned monumental titles.
  - **Editorial Serif (`CrimsonPro-Italic.ttf`, `46–60px`)**: Literary italic counterpoint placed asymmetrically on the right (`x ≈ 980–1120`) or as an interlude pull-quote.
  - **Metadata & Rails (`DMMono-Regular.ttf`, `21–24px`)**: Top running header (`x=80` left, `x=1720` right, `2px` rail at `y=86`) and crisp figure captions (`S01 / ...`) below each frame.
- **3x-Supersampled `1px` Frames (`draw_frame`)**:
  - Primary hero frame: `HERO_RADIUS = 14`, `cut = 0`.
  - Supporting detail frames: `DETAIL_RADIUS = 10`, optional bottom-right `45°` chamfer `cut = 18..24` for subtle editorial geometry.

### Standard Grid Templates (`WIDTH = 1800`, `MARGIN = 80`, `INNER = 1640`)
1. **Wide Hero + Asymmetric Split (`height ≈ 1500–1600`)**:
   - Top rail (`y=35`, rule `y=86`) + Masthead (`y=108..340`)
   - Full-width hero frame: `(80, 380, 1640, 640)`
   - Bottom split: `(80, 1060, 540, 340)` (`cut=18`) + `(650, 1060, 1070, 340)` (`cut=24`) + captions below.
2. **Three Portrait Pages / Mobile Screens (`height ≈ 1240`)**:
   - Ideal for A4 PDFs (`1 : 1.414`) or mobile screens—**never crop portrait pages into landscape boxes**.
   - 3 columns across `1640px` (`28px` gap): `w = 528`, `h = 747` at `x = 80, 636, 1192`, `y = 380`, captions at `y = 1152`.
3. **Hero + 3-Up Filmstrip (`height ≈ 1920`)**:
   - Wide 16:9 frame `(80, 460, 1640, 922)` + 3 equal `16:9` stills `(80 + i*556, 1480, 528, 297)` with `cut=20`.

Always export dark (`<name>.png`) and light (`<name>-light.png`) together via `export_pair()`.

---

## 2. Hero SVG Spec (`hero-dark.svg` & `hero-light.svg`)

- **Canvas**: `viewBox="0 0 840 176" width="840" height="176"`.
- **GitHub-Native Surfaces**:
  - Dark: canvas `#0d1117`, hairline `#26303c`, primary ink `#f0f3f6`, secondary `#9da7b3`, muted `#6e7885`.
  - Light: canvas `#ffffff`, hairline `#d8dee4`, primary ink `#1f2328`, secondary `#57606a`, muted `#768390`.
- **Project-Adaptive Accent**:
  - Derive from the target repo's own CSS tokens, logo, or domain mood.
  - If the repo is editorial/typographic or monochrome, a **pure monochrome/silver-ink editorial palette** (`#e6edf3` / `#1f2328` accent with subtle warm/cool rule ticks) is cleaner and more timeless than arbitrary neon blue.
- **Restrained Composition (Anti-Circuit-Board)**:
  - Top & bottom fine editorial rules (`x1="60" x2="780"`) with tiny precision tick marks or subtle domain contours faded smoothly at the edges—**never** geeky circuit traces, random polygons, or wide pill boxes (`eyebrow text ≤ 22 chars`).
  - Centered title (`y="98"`, `38–42px`): pair italic serif (`Georgia, 'Times New Roman', serif`) with `/` and crisp sans-serif (`600` weight), followed by a calm `13.5–14px` subtitle at `y="132"`.

---

## 3. Minimal Architecture / Flow SVG Spec (Only When Needed)

Only create `flow-*.svg` / `arch-*.svg` when explaining a headless execution loop or multi-service boundary:
- **Canvas**: `width="840"`, `height="210–250"`, `30px` outer margins (`780px` track).
- **Hard Limits**:
  - **3–4 flat cards maximum** (`rx="10"`, dark `#121820` / light `#f6f8fa`).
  - **Zero nested boxes inside cards**—use a single thin divider line if needed.
  - **≤ 2 short lines of text per card** (`14px` semibold title + `11.5px` secondary summary; never stuff raw filesystem paths that touch card borders).
  - **≥ 40% open canvas whitespace**.
  - Include `@media (prefers-reduced-motion: reduce)` whenever CSS motion is used.
