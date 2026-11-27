<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/hero-dark.svg?v=213b0d26">
    <source media="(prefers-color-scheme: light)" srcset="./assets/readme/hero-light.svg?v=cc293846">
    <img src="./assets/readme/hero-light.svg?v=cc293846" width="100%" alt="TTTIM / skills — 面向主流编码 Agent 的出版级设计与文档技能合集">
  </picture>
</p>

<p align="center">
  <kbd>中文</kbd> · <a href="./README.en.md"><kbd>English ↗</kbd></a>
</p>

<p align="center">
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Agent_Skills-Open_Spec-111827?style=flat-square" alt="Agent Skills Open Spec"></a>
  <img src="https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/Gemini_·_Codex_·_Cursor-24292f?style=flat-square" alt="Gemini, Codex, and Cursor">
</p>

<p align="center">
  <b>把经过实测的设计规范、排版脚本与视觉质检打包成可复用的 Agent 技能。</b><br>
  <sub>遵循开放技能规范，一行命令安装至 Claude Code、Antigravity / Gemini、Codex 与 Cursor。</sub>
</p>

<p align="center">
  <a href="#showcase"><kbd>作品画廊 ↓</kbd></a>
  <a href="#quickstart"><kbd>快速安装 ↓</kbd></a>
  <a href="#catalog"><kbd>技能目录 ↓</kbd></a>
  <a href="./AGENTS.md"><kbd>开发指南 ↗</kbd></a>
</p>

<br>

<h1 id="showcase" align="center"><sub><samp>01</samp></sub><br>作品与能力预览<br><sub>Selected skills</sub></h1>

<p align="center">
  <a href="./skills/TTT-MonoPDF-skill/SKILL.md">
    <picture>
      <source media="(prefers-color-scheme: light)" srcset="./assets/readme/poster-monopdf-light.png?v=7f07e1e9">
      <img src="./assets/readme/poster-monopdf.png?v=275f4dc3" width="100%" alt="TTT-MonoPDF-skill 真实编译样张：纯黑单页封面、黑白扁平 TikZ 拓扑图与极简三线表">
    </picture>
  </a>
</p>
<p align="center">
  <sub><b>瑞士编辑风中英文汇报 PDF</b> — 纯黑封面、黑白灰版式系统、扁平矢量图与逐页渲染视觉质检。</sub><br>
  <a href="./skills/TTT-MonoPDF-skill/SKILL.md"><kbd>查看 TTT-MonoPDF-skill ↗</kbd></a>
</p>

<br>

<p align="center">
  <a href="./skills/TTT-Readme-skill/SKILL.md">
    <picture>
      <source media="(prefers-color-scheme: light)" srcset="./assets/readme/poster-readme-light.png?v=2f0c59fe">
      <img src="./assets/readme/poster-readme.png?v=52838182" width="100%" alt="TTT-Readme-skill 视觉规范展示：GitHub 明暗原生画布自适应、全透明杂志展板与极简三节点流程图">
    </picture>
  </a>
</p>
<p align="center">
  <sub><b>杂志级 GitHub 仓库门面</b> — 内置开源展示字体与透明展板合成脚本，自动适配明暗主题并完成视觉验收。</sub><br>
  <a href="./skills/TTT-Readme-skill/SKILL.md"><kbd>查看 TTT-Readme-skill ↗</kbd></a>
</p>

<br>

<h1 id="quickstart" align="center"><sub><samp>02</samp></sub><br>快速安装<br><sub>Quick install</sub></h1>

```sh
# 跨主流 Agent 一键安装全部技能（推荐）
npx skills add Timcai06/TTTIM-skills -g

# 仅安装单个指定技能
npx skills add Timcai06/TTTIM-skills --skill TTT-Readme-skill -g
```

<details>
<summary><kbd>更多安装方式</kbd> &nbsp;Claude Code 插件市场与本机源码软链</summary>

```sh
# 在 Claude Code 会话中添加插件市场
/plugin marketplace add Timcai06/TTTIM-skills

# 本机持续开发：克隆仓库并软链至本地 Agent 目录
git clone https://github.com/Timcai06/TTTIM-skills.git
cd TTTIM-skills && ./install.sh
```

</details>

<br>

<h1 id="catalog" align="center"><sub><samp>03</samp></sub><br>技能目录<br><sub>Catalog</sub></h1>

| 技能 | 核心产物与适用场景 | 入口 |
| :--- | :--- | :--- |
| **TTT-MonoPDF-skill** | 基于 XeLaTeX 生成极简黑白瑞士编辑风汇报方案、技术白皮书与执行摘要 PDF，内置双次编译与逐页视觉自查流程 | [技能说明](./skills/TTT-MonoPDF-skill/SKILL.md) · [LaTeX 模板](./skills/TTT-MonoPDF-skill/references/template.tex) |
| **TTT-Readme-skill** | 设计与重构出版级中英双语 GitHub README，附带全透明杂志展板合成脚本、开源展示字体与明暗双底色质检工具 | [技能说明](./skills/TTT-Readme-skill/SKILL.md) · [展板脚本](./skills/TTT-Readme-skill/scripts/editorial_panel.py) |

<br>

<h1 id="notes" align="center"><sub><samp>04</samp></sub><br>运行前提与说明<br><sub>Prerequisites &amp; notes</sub></h1>

- **PDF 排版环境**：运行 **TTT-MonoPDF-skill** 需本机已安装 XeLaTeX（MacTeX 或 TeX Live）、Poppler 渲染工具以及 macOS 系统字体（PingFang SC 与 Helvetica Neue）。
- **展板合成环境**：运行 **TTT-Readme-skill** 的海报与质检脚本需 Python 3 与 Pillow；展示排版所需的 3 款 SIL OFL 开源字体已随技能内置，无需额外安装字体。
- **扩展与维护**：本机软链脚本默认面向 macOS 与 Linux 环境；新增或修改技能的目录规范见 [开发指南](./AGENTS.md)。

<hr>
<p align="center"><sub>TTTIM-skills &nbsp;·&nbsp; <a href="./README.en.md">English</a> &nbsp;·&nbsp; <a href="./AGENTS.md">Authoring Guide</a></sub></p>
