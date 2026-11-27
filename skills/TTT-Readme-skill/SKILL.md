---
name: TTT-Readme-skill
description: Create or refactor publication-grade, Swiss-editorial GitHub READMEs (README.md and optional README.en.md) with transparent dark/light magazine exhibition posters, project-adaptive SVG heroes, visitor-first hierarchy, and visual QA. Use when the user asks to write, redesign, polish, or bilingualize a GitHub repository README or profile README. Do NOT use for internal API specs, changelogs, ADRs, or one-paragraph quick notes.
---

# Swiss-Editorial GitHub README (`TTT-Readme-skill`)

Act as an editorial design director crafting publication-grade GitHub READMEs. A great README feels like opening a crisp design monograph—never a cluttered wiki, maintainer changelog, or generic AI template.

## Anti-Slop Rules (Non-Negotiable)

1. **Visitor-First Filtering**: A first-time visitor only cares about three things in the first 15 seconds: **(1) What does it look like / do? (2) How do I run or install it in one step? (3) What are the real prerequisites or limits?** Never pollute main sections or product tables with internal maintainer plumbing (`AGENTS.md` checklists, symlink mechanics, CI wishlists). Tuck contributor internals into a bottom `<details>` or a single footer link.
2. **Zero "Gray-Pill Soup"**: Every `` `inline code` `` renders a gray pill on GitHub. Keep narrative prose clean: **at most 1–2 inline code spans per paragraph**. Use **bold** or links for module names and concepts; reserve backticks strictly for literal CLI commands/flags.
3. **Zero Fake Filler Badges**: Never invent gray text badges (`Skills-2`, `Sync-script`, `Targets-A·B·C`). Use **2–5 recognizable icon/status badges** (`style=flat-square`), or omit badges entirely.
4. **Show Real Artifacts, Not Box-in-Box PPT Charts**:
   - Whenever a repo produces UI, web pages, PDFs, terminal views, or visual outputs (including skill/tool collections!), **compose a `1800px` transparent magazine exhibition poster** using `scripts/editorial_panel.py` instead of hand-coding a boxy architecture SVG.
   - Only draw an architecture/flow SVG for headless engines/algorithms, and obey strict minimalism: **3–4 flat nodes max, zero nested boxes, ≤ 2 short lines per node, ≥ 40% whitespace**. Never draw "circuit-board" nodes or multi-bend connector spaghetti.
5. **Project-Adaptive Palette**: Never copy a hardcoded brand color from another project. Inspect the target repo (`tokens.css`, Tailwind config, brand docs, or screenshots) to derive a fitting dark/light accent pair, while anchoring SVG canvases to GitHub's native `#0d1117` (dark) and `#ffffff` (light).

## Mandatory Three-Pass Workflow

### Pass 1 — Editorial Brief (Think Before Writing)
Before writing any SVG or Markdown, inspect the target repository (entrypoints, `Makefile`/`package.json`/`pyproject.toml`, `docs/`, tests, design tokens) and decide:
1. **Archetype** (read `references/archetypes.md`):
   - *Showcase / Collection* (UI apps, websites, skill/plugin collections): `01` Magazine exhibition posters of real outputs → `02` 1-step install/run → `03` Clean product catalog → `04` Real prerequisites & limits.
   - *Engine / Agent / Algorithm* (headless runtimes, CLIs, ML): `01` How one turn/request/frame executes (minimal 3–4 node SVG + 3 invariants) → `02` Quick start & self-checks → `03` Entrypoints & verified metrics → `04` Honest boundaries.
   - *Profile / Portfolio*: Hero + contact badges → Bilingual intro → Lead exhibition posters (`<details open>`) + compact featured table + folded archive → Toolbox visual → Live/footer.
2. **Visual Proof Plan**: Identify the real screenshots, rendered PDF pages, or terminal captures to frame inside `scripts/editorial_panel.py` (read `references/visual-spec.md`).
3. **Cut List**: Explicitly drop maintainer-only files and verbose prose (keep project root `README.md` around **85–135 lines**; one primary visual container per section).

### Pass 2 — Asset Generation & Authoring
1. **Magazine Exhibition Posters** (`assets/readme/poster-<name>.png` & `poster-<name>-light.png`):
   - Use bundled SIL OFL fonts (`BigShoulders-Bold`, `CrimsonPro-Italic`, `DMMono-Regular`) via `scripts/editorial_panel.py`.
   - Generates a **transparent RGBA `1800px` canvas** with top metadata rail, `164px` display headline, italic serif pull-quote, and `3x`-supersampled `1px` rounded/chamfered (`cut=18..24`) frames around real screenshots/renders.
   - Embed with `<picture>` so light and dark modes swap cleanly:
     ```html
     <picture>
       <source media="(prefers-color-scheme: light)" srcset="./assets/readme/poster-demo-light.png">
       <img src="./assets/readme/poster-demo.png" width="100%" alt="Descriptive summary of the real output shown">
     </picture>
     ```
2. **Hero SVG** (`assets/readme/hero-dark.svg` & `hero-light.svg`):
   - Follow `references/visual-spec.md` (`840×176`, native `#0d1117` / `#ffffff` canvas, restrained editorial hairlines or subtle domain motif, short uppercase eyebrow ≤ 22 chars, serif-italic + grotesque title contrast, 1-line subtitle).
   - For animated SVGs, always provide `@media (prefers-reduced-motion: reduce)` and a 4-branch `<picture>` with light/dark static fallbacks.
3. **Markdown Authoring**:
   - Follow the chosen skeleton in `references/archetypes.md`.
   - If bilingual (`README.md` + `README.en.md`), keep identical `#id` anchors, identical assets, idiomatic English (not literal translation), and inverted `<kbd>` language toggles.

### Pass 3 — Deterministic Validation & Visual QA (Mandatory)
Never finish without inspecting rendered visuals:
1. Run the bundled validator, hash stamper, and QA sheet generator:
   ```bash
   python3 "<skill-dir>/scripts/verify_readme.py" "<target-repo>" --stamp --render-qa /tmp/readme_qa
   ```
2. Open every `/tmp/readme_qa/qa_*.png` image with your file/image reading tool and **visually inspect both dark (`#0d1117`) and light (`#ffffff`) renders**:
   - Check that display titles, pull-quotes, captions, and frames never collide or touch edges.
   - Check that aspect ratios of framed screenshots/pages are natural (use `fit="contain"` or portrait grids for portrait documents; never awkwardly decapitate UI or A4 pages).
   - Check that SVGs feel airy (≥ 40% whitespace) with crisp contrast in both modes.
3. Fix any visual flaw or `verify_readme.py` warning and re-run until clean. Remove temporary `/tmp` files when done.
