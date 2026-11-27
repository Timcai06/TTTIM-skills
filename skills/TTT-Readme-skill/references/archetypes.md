# README Archetype Skeletons (`TTT-Readme-skill`)

Target **85–135 lines** for project repositories. Keep narrative prose crisp and free of inline-code backtick clutter.

---

## Archetype A: Showcase / Collection Repo (Apps, Websites, Consoles, Skill/Plugin Packs)

Use when visitors want to **see real outputs first** and install/run in one command.

```markdown
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/hero-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/readme/hero-light.svg">
    <img src="./assets/readme/hero-light.svg" width="100%" alt="<Project> — <One-line visual and functional summary>">
  </picture>
</p>

<p align="center">
  <kbd>中文</kbd> · <a href="./README.en.md"><kbd>English ↗</kbd></a>
</p>

<p align="center">
  <!-- 2–4 clean, recognizable badges max; zero invented filler text badges -->
  <img src="https://img.shields.io/badge/<Name>-<HEX>?style=flat-square&logo=<slug>&logoColor=white" alt="<Name>">
</p>

<p align="center">
  <b><One crisp sentence stating what this project gives the user.></b><br>
  <sub><One calm sentence on scope or supported environments—zero backticks.></sub>
</p>

<p align="center">
  <a href="#showcase"><kbd>作品画廊 ↓</kbd></a>
  <a href="#quickstart"><kbd>快速安装 ↓</kbd></a>
  <a href="#catalog"><kbd>能力目录 ↓</kbd></a>
  <a href="./docs/README.md"><kbd>文档 ↗</kbd></a>
</p>

<br>

<h1 id="showcase" align="center"><sub><samp>01</samp></sub><br>视觉与能力预览<br><sub>Selected showcase</sub></h1>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="./assets/readme/poster-main-light.png">
    <img src="./assets/readme/poster-main.png" width="100%" alt="<Describe the real screens or rendered artifacts shown in this exhibition panel>">
  </picture>
</p>

<p align="center"><sub><One-sentence caption explaining what is shown above and when it triggers.></sub></p>

<!-- Optional second poster or <details> gallery for multi-item collections -->

<br>

<h1 id="quickstart" align="center"><sub><samp>02</samp></sub><br>快速上手<br><sub>Quick start</sub></h1>

```sh
<1-to-3 primary user commands>
```

<details>
<summary><kbd>更多方式</kbd> &nbsp;<Local dev, single-item install, or Docker options></summary>

```sh
<secondary commands>
```

</details>

<br>

<h1 id="catalog" align="center"><sub><samp>03</samp></sub><br>目录索引<br><sub>Catalog</sub></h1>

<!-- List ONLY user-facing items/modules—never mix internal build scripts or repo config files here -->
| 名称 | 核心产物与适用场景 | 入口 |
| :--- | :--- | :--- |
| **<Item 1>** | <Plain-language summary of output and trigger> | [查看详情](./path/to/item1) |
| **<Item 2>** | <Plain-language summary of output and trigger> | [查看详情](./path/to/item2) |

<br>

<h1 id="notes" align="center"><sub><samp>04</samp></sub><br>运行前提与说明<br><sub>Prerequisites &amp; boundaries</sub></h1>

- **<Runtime requirement>**：<Only prerequisites that affect users running the tool.>
- **<Honest boundary>**：<What is demo-only, macOS-only, or not yet live.>
- **参与开发**：目录规范与新增流程见 [开发指南](./AGENTS.md)。

<hr>
<p align="center"><sub><Project Name> &nbsp;·&nbsp; <a href="./README.en.md">English</a> &nbsp;·&nbsp; <a href="./AGENTS.md">Contributing</a></sub></p>
```

---

## Archetype B: Engine / Agent / Algorithm Repo (Runtimes, CLIs, ML, Benchmarks)

Use when the core value is an **execution pipeline, state machine, or verifiable algorithm**.

- **Header**: Same 5-part centered editorial header (may include a verified `Self_Tests-X/X_PASS` badge).
- **`01` 怎么工作 / How it works**:
  - 1 minimal dual-theme flow SVG (`flow-dark.svg` / `flow-light.svg`, 3–4 flat nodes, ≥ 40% whitespace) OR real terminal/trace exhibition panel.
  - 1 plain-language paragraph explaining **how a single request / turn / frame executes**.
  - 3–4 bullet invariants (`- **确定性裁决**：...`).
- **`02` 跑一遍自检 / Quick start**: 1-line runtime requirement + 3 runnable commands (`self-test`, `baseline`, `dev`).
- **`03` 模块与验证口径 / Modules & verification**: 3-column table (`模块 | 职责 | 入口`) + `<details>` containing **truthful benchmark scope** (explicitly separating locally verified runs from historical/un-rerun numbers).
- **`04` 当前边界 / Honest boundaries**: `<details open>` stating rule placeholders, dataset size limits, or non-production parts.

---

## Archetype C: Profile / Portfolio Repo

- **Opening**: Dual-theme Hero SVG + flat-square social badges + dual-theme tagline SVG + concise bilingual bio (zero clutter) + optional workspace illustration.
- **`01` 重点作品 / Featured work**:
  - `<details open>` **主推 / Lead projects**: 1–2 flagship projects, each presented with a `1800px` transparent exhibition panel (`editorial_panel.py`, using 4-branch `<picture>` if animated), 1-paragraph summary, tech badges, and `<kbd>Repo ↗</kbd>`.
  - `<details>` **精选 / Also featured**: 2-column `<table>` (`44%` compact card visual left, `56%` title + summary + badges right).
- **`02+` Thematic / Toolbox / Live sections**: Centered numbered `<h1>` headers, progressive `<details>` folding for deeper galleries, auto-stamped `?v=<sha8>` URLs.
