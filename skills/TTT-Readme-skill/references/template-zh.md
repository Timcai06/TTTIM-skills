<!--
  TTT-Readme-skill Reference Template (Chinese primary; mirror structure for README.en.md)
  Replace all <PLACEHOLDER> values with verified facts from the target repository.
  Target length for a project repo: 100–150 lines.
-->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/hero-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/readme/hero-light.svg">
    <img src="./assets/readme/hero-light.svg" width="100%" alt="<Project Name> — <Concise summary of architecture and purpose>">
  </picture>
</p>

<!-- Optional bilingual switcher; invert highlight in README.en.md -->
<p align="center">
  <kbd>中文</kbd> · <a href="./README.en.md"><kbd>English ↗</kbd></a>
</p>

<!-- 5–6 flat-square badges max; add verified CI / self-test badge when available -->
<p align="center">
  <img src="https://img.shields.io/badge/<Tech_1>-<HEX>?style=flat-square&logo=<slug>&logoColor=white" alt="<Tech 1>">
  <img src="https://img.shields.io/badge/<Tech_2>-<HEX>?style=flat-square&logo=<slug>&logoColor=white" alt="<Tech 2>">
  <img src="https://img.shields.io/badge/<Tech_3>-<HEX>?style=flat-square&logo=<slug>&logoColor=white" alt="<Tech 3>">
</p>

<p align="center">
  <b><One-sentence definition of what this project is.></b><br>
  <sub><One-sentence explanation of core components, mechanism, or target user.></sub>
</p>

<p align="center">
  <a href="#quickstart"><kbd>快速启动 ↓</kbd></a>
  <a href="./docs/README.md"><kbd>文档索引 ↗</kbd></a>
  <a href="<LIVE_OR_SIBLING_URL>"><kbd><External Label> ↗</kbd></a>
</p>

<br>

<!-- 01: Visual Showcase (UI repo) OR Execution Path & Invariants (Engine/Agent/Algo repo) -->
<h1 id="overview" align="center"><sub><samp>01</samp></sub><br><怎么工作 / 界面与架构><br><sub><How it works / Overview></sub></h1>

<!-- Static dual-theme diagram example -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/flow-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/readme/flow-light.svg">
    <img src="./assets/readme/flow-light.svg" width="100%" alt="<Self-contained description of the modules and data flow shown in the diagram>">
  </picture>
</p>

<!-- For animated SVGs, use the 4-branch pattern instead:
<p align="center">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: light)" srcset="./assets/readme/showcase-static-light.png">
    <source media="(prefers-reduced-motion: reduce)" srcset="./assets/readme/showcase-static-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="./assets/readme/showcase-light.svg">
    <img src="./assets/readme/showcase-dark.svg" width="100%" alt="<Self-contained description>">
  </picture>
</p>
-->

<p><One concise paragraph explaining how one request, turn, or frame flows through the system in plain language.></p>

- **<Invariant 1>**：<Concrete deterministic guarantee or architectural boundary.>
- **<Invariant 2>**：<Concrete deterministic guarantee or architectural boundary.>
- **<Invariant 3>**：<Concrete deterministic guarantee or architectural boundary.>

<details>
<summary><kbd><更多视图 / 系统分层></kbd> &nbsp;<Brief summary of what expands here></summary>

<!-- Optional secondary posters, screenshots, or deeper diagrams -->

</details>

<br>

<h1 id="quickstart" align="center"><sub><samp>02</samp></sub><br>本地跑起来<br><sub>Quick start</sub></h1>

> 环境要求：<Runtime versions, e.g., Node 24 / Python 3.12+>. 常用命令以根目录 [`Makefile`](./Makefile) 为准。

```sh
<cmd-1>   # <Install dependencies>
<cmd-2>   # <Start local preview / dev server>
<cmd-3>   # <Run core checks / self-tests>
```

<details>
<summary><kbd>更多命令</kbd> &nbsp;<Full install, E2E, Docker, or benchmark commands></summary>

```sh
<extra-cmd-1>   # <Description>
<extra-cmd-2>   # <Description>
```

</details>

<br>

<h1 id="modules" align="center"><sub><samp>03</samp></sub><br>模块与核心入口<br><sub>Modules &amp; entrypoints</sub></h1>

| 模块 / 文档 | 职责 | 入口 |
| :--- | :--- | :--- |
| <Core Module 1> | <Responsibility> | [`<entry-file-1>`](./path/to/file1) |
| <Core Module 2> | <Responsibility> | [`<entry-file-2>`](./path/to/file2) |
| <Core Module 3> | <Responsibility> | [`<entry-file-3>`](./path/to/file3) |

<details>
<summary><kbd>目录地图</kbd> &nbsp;查看子目录职责与验证口径</summary>

- [`<dir-1>/`](./dir-1/) — <Description>
- [`<dir-2>/`](./dir-2/) — <Description>

<!-- Optional verification summary for algorithm/benchmark repos:
**验证口径（如实标注）**：
- **自检**：`X/X PASS`（本机实测）。
- **基准**：`<metric>`（标明本机实测或历史记录未复跑）。
-->

</details>

<br>

<h1 id="status" align="center"><sub><samp>04</samp></sub><br>当前状态与边界<br><sub>Status &amp; honest boundaries</sub></h1>

<details open>
<summary><kbd>如实说明</kbd> &nbsp;已具备的能力与尚未完成的部分</summary>

- **已跑通**：<Verified local or deployed capabilities.>
- **未上线 / 已知限制**：<Explicitly list mock engines, rule placeholders, un-rerun benchmarks, or non-production constraints.>
- **环境口径**（如适用）：<Clarify hosted demo vs local full-stack differences.>

</details>

<hr>
<p align="center"><sub><Project Name> &nbsp;·&nbsp; <a href="./README.en.md">English</a> &nbsp;·&nbsp; <a href="./docs/README.md">Docs</a></sub></p>
