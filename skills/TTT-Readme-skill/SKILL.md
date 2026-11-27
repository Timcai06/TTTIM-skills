---
name: TTT-Readme-skill
description: Create or refactor publication-grade, editorial GitHub READMEs (README.md and optional README.en.md) featuring project-adaptive dual-theme SVG heroes/diagrams, centered numbered chapters, progressive <details> disclosure, execution-path architecture explanations, and honest engineering boundaries. Use when the user asks to write, redesign, polish, or bilingualize a GitHub repository README or profile README. Do NOT use for internal API specs, changelogs, ADRs, or one-paragraph quick notes.
---

# Editorial GitHub README (`TTT-Readme-skill`)

Use this skill to craft crisp, scannable, design-grade GitHub READMEs that balance visual craft with ruthless engineering honesty. Every visual choice (accent color, motif, diagram style) must be derived from the **target project itself**—never copy a hardcoded brand color from another project.

## Core Principles

1. **30-Second Scannability**: Keep project root `README.md` within **100–150 lines**. Move long manuals, full command matrices, and secondary galleries into `<details>` blocks or `docs/`.
2. **Project-Adaptive Visual Identity**: Inspect the target repo's UI tokens (`tokens.css`, Tailwind config, brand package, screenshots, or domain mood) to pick its own dark/light accent color and subtle background motif. Anchor SVG canvases to GitHub's native backgrounds (`#0d1117` dark / `#ffffff` light) so graphics blend seamlessly.
3. **Explain via One Execution Path**: For engineering/agent/algorithm repos, replace generic feature lists with 1 clear diagram + 1 plain-language paragraph ("how one request / turn / frame works") + 3–4 deterministic invariants + a `Module | Responsibility | Source` table linking to real files.
4. **Ruthless Honesty**: Only claim commands, features, and metrics verified in the repo. Always separate **locally verified** vs **historical / not re-run** benchmarks, **hosted demo** vs **local dev** behavior, and **working today** vs **not production-ready**.

## Repo Archetypes

Choose the archetype that fits the target repo before writing:

- **UI / Showcase** (web apps, consoles, desktop apps): `01` Visual showcase (editorial screenshot poster or animated showcase SVG) → `02` Quick start → `03` Architecture & module map → `04` Status & boundaries.
- **Engine / Agent / Algorithm** (runtimes, CLIs, ML/research): `01` How it works (pipeline/flow SVG + 3–4 invariants) → `02` Quick start & self-checks → `03` Modules, entrypoints & verification scope → `04` Honest boundaries / known limits.
- **Profile / Portfolio** (GitHub profile README): Dual-theme Hero + contact badges → Bilingual intro → Featured work (`<details open>` lead projects + compact 2-column table + folded archive) → Toolbox visual → Live block / footer.

## Page Structure & Editorial Grammar

Read `references/template-zh.md` for the complete structural skeleton.

1. **Centered 5-Part Opening** (all `<p align="center">`):
   - Dual-theme Hero SVG (`assets/readme/hero-dark.svg` & `hero-light.svg`) inside `<picture>`.
   - Optional bilingual switcher: `<kbd>中文</kbd> · <a href="./README.en.md"><kbd>English ↗</kbd></a>`.
   - Shields.io tech badges (`style=flat-square`, **5–6 max**; include a real self-test/CI badge if verified).
   - 2-line pitch: `<b>One crisp sentence defining what it is.</b><br><sub>One sentence on core components or mechanism.</sub>`.
   - `<kbd>` quick-nav bar: use `↓` for in-page anchors (`#quickstart`) and `↗` for docs, live URLs, or sibling repos.
2. **Centered Numbered Chapters (`01`–`04`)**:
   ```html
   <h1 id="quickstart" align="center"><sub><samp>02</samp></sub><br>本地跑起来<br><sub>Quick start</sub></h1>
   ```
   - `02 Quick start`: 1-line requirements blockquote + **3–4 essential commands** (prefer `Makefile` or zero-dep entrypoints); fold secondary commands into `<details><summary><kbd>更多命令</kbd> &nbsp;...</summary>`.
   - `04 Honest boundaries`: use `<details open>` with `<summary><kbd>如实说明</kbd> ...</summary>` so limitations are transparent without bloating the narrative.
3. **Minimal Footer**: `<hr>` followed by centered `<sub>Project Name · Language Switch · Docs</sub>`.

## Visual, Theme & Asset Rules

Read `references/svg-spec.md` before generating any SVG or poster asset.

- **Derive palette from the target repo**:
  1. Check CSS variables, theme files, Tailwind config, or brand docs in the target repo first.
  2. If none exist, choose a restrained accent pair (bright, readable on `#0d1117` in dark mode; deeper, high-contrast on `#ffffff` in light mode) matching the project's domain.
- **Dual-theme `<picture>` (static assets)**:
  ```html
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/hero-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/readme/hero-light.svg">
    <img src="./assets/readme/hero-light.svg" width="100%" alt="Descriptive summary of the diagram">
  </picture>
  ```
- **4-branch `<picture>` (animated SVGs)**:
  Always include both light and dark `prefers-reduced-motion: reduce` fallbacks before the animated sources so light-mode users with reduced motion do not receive a dark static image:
  ```html
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: light)" srcset="./assets/readme/showcase-static-light.png">
    <source media="(prefers-reduced-motion: reduce)" srcset="./assets/readme/showcase-static-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="./assets/readme/showcase-light.svg">
    <img src="./assets/readme/showcase-dark.svg" width="100%" alt="Descriptive summary">
  </picture>
  ```
- **Cache-busting & Accessibility**:
  - When updating existing README images/SVGs on GitHub, append `?v=<8-char-hash>` to bypass GitHub Camo caching.
  - Write informative, self-contained `alt` text describing the actual modules and flow shown in each visual.

## Bilingual Parity (`README.md` + `README.en.md`)

When maintaining bilingual READMEs:
- Keep identical chapter numbers (`01`–`04`), identical `#id` anchors, and shared asset paths.
- Invert the top language switcher in `README.en.md`: `<a href="./README.md"><kbd>中文 ↗</kbd></a> · <kbd>English</kbd>`.
- Write idiomatic technical English rather than word-for-word translation.

## Workflow

1. **Audit the target repository first**: inspect directory layout, `Makefile` / `package.json` / `pyproject.toml`, core source entrypoints, `docs/`, test suites, and design tokens. Never guess commands or numbers.
2. **Select Archetype & Theme**: pick 1 of the 3 archetypes and derive the project's dark/light accent pair and visual motif.
3. **Read references**: read `references/template-zh.md` and `references/svg-spec.md`.
4. **Produce visual assets**: create paired `*-dark.svg` and `*-light.svg` (plus static fallbacks if animated) under `assets/readme/`.
5. **Write `README.md`** (and `README.en.md` if bilingual).
6. **Verify against the Quality Checklist** below before finishing.

## Quality Checklist

- [ ] Every relative link (`./docs/...`, source files, `./assets/readme/...`) resolves to an existing file.
- [ ] Every dark SVG/poster has a matching light counterpart; animated SVGs include `@media (prefers-reduced-motion: reduce)` and static fallbacks.
- [ ] Every SVG/image has meaningful `alt` text; updated assets carry `?v=<short-hash>` if replacing cached GitHub images.
- [ ] Accent colors and visual motif match the target project (no leftover colors/names from unrelated repos).
- [ ] All commands, ports, env vars, and test/benchmark figures are verified against the repo, with unverified/un-rerun items explicitly labeled.
- [ ] Root project `README.md` is concise (~100–150 lines) with long tables/commands folded in `<details>`.
- [ ] Zero leaked API keys, private internal URLs, or sensitive local paths.
