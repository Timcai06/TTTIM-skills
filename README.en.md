<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/hero-dark.svg?v=213b0d26">
    <source media="(prefers-color-scheme: light)" srcset="./assets/readme/hero-light.svg?v=cc293846">
    <img src="./assets/readme/hero-light.svg?v=cc293846" width="100%" alt="TTTIM / skills — Publication-grade design and document workflows for AI coding agents">
  </picture>
</p>

<p align="center">
  <a href="./README.md"><kbd>中文 ↗</kbd></a> · <kbd>English</kbd>
</p>

<p align="center">
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Agent_Skills-Open_Spec-111827?style=flat-square" alt="Agent Skills Open Spec"></a>
  <img src="https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/Gemini_·_Codex_·_Cursor-24292f?style=flat-square" alt="Gemini, Codex, and Cursor">
</p>

<p align="center">
  <b>Reusable design systems, deterministic layout scripts, and visual QA loops packaged as AI Agent skills.</b><br>
  <sub>Built on the open Agent Skills specification—install in one command across Claude Code, Antigravity / Gemini, Codex, and Cursor.</sub>
</p>

<p align="center">
  <a href="#showcase"><kbd>Showcase ↓</kbd></a>
  <a href="#quickstart"><kbd>Quick install ↓</kbd></a>
  <a href="#catalog"><kbd>Catalog ↓</kbd></a>
  <a href="./AGENTS.md"><kbd>Authoring guide ↗</kbd></a>
</p>

<br>

<h1 id="showcase" align="center"><sub><samp>01</samp></sub><br>Selected skills<br><sub>Visual proof &amp; outputs</sub></h1>

<p align="center">
  <a href="./skills/TTT-MonoPDF-skill/SKILL.md">
    <picture>
      <source media="(prefers-color-scheme: light)" srcset="./assets/readme/poster-monopdf-light.png?v=7f07e1e9">
      <img src="./assets/readme/poster-monopdf.png?v=275f4dc3" width="100%" alt="TTT-MonoPDF-skill compiled specimen: pure black cover page, flat monochrome TikZ diagram, and three-line executive table">
    </picture>
  </a>
</p>
<p align="center">
  <sub><b>Swiss-Editorial Monochrome PDFs</b> — Pure black cover, grayscale typographic hierarchy, flat TikZ diagrams, and page-by-page visual QA.</sub><br>
  <a href="./skills/TTT-MonoPDF-skill/SKILL.md"><kbd>Explore TTT-MonoPDF-skill ↗</kbd></a>
</p>

<br>

<p align="center">
  <a href="./skills/TTT-Readme-skill/SKILL.md">
    <picture>
      <source media="(prefers-color-scheme: light)" srcset="./assets/readme/poster-readme-light.png?v=2f0c59fe">
      <img src="./assets/readme/poster-readme.png?v=52838182" width="100%" alt="TTT-Readme-skill visual system: native GitHub dark and light canvas adaptation, transparent RGBA exhibition panels, and minimal flow rules">
    </picture>
  </a>
</p>
<p align="center">
  <sub><b>Monograph-Grade GitHub READMEs</b> — Bundled SIL OFL display typefaces, transparent exhibition panel composer, and dual-theme visual verification.</sub><br>
  <a href="./skills/TTT-Readme-skill/SKILL.md"><kbd>Explore TTT-Readme-skill ↗</kbd></a>
</p>

<br>

<h1 id="quickstart" align="center"><sub><samp>02</samp></sub><br>Quick install<br><sub>One-line setup</sub></h1>

```sh
# Install all skills globally across supported coding agents (recommended)
npx skills add Timcai06/TTTIM-skills -g

# Or install a single skill
npx skills add Timcai06/TTTIM-skills --skill TTT-Readme-skill -g
```

<details>
<summary><kbd>More options</kbd> &nbsp;Claude Code plugin marketplace &amp; local symlink workflow</summary>

```sh
# Add as a plugin marketplace inside Claude Code
/plugin marketplace add Timcai06/TTTIM-skills

# Local development: clone and symlink into local agent skill directories
git clone https://github.com/Timcai06/TTTIM-skills.git
cd TTTIM-skills && ./install.sh
```

</details>

<br>

<h1 id="catalog" align="center"><sub><samp>03</samp></sub><br>Catalog<br><sub>Included skills</sub></h1>

| Skill | Output &amp; Trigger Scope | Entrypoints |
| :--- | :--- | :--- |
| **TTT-MonoPDF-skill** | Compiles minimalist monochrome Chinese/English executive briefs, proposals, and architecture PDFs via XeLaTeX with mandatory visual QA | [SKILL.md](./skills/TTT-MonoPDF-skill/SKILL.md) · [Template](./skills/TTT-MonoPDF-skill/references/template.tex) |
| **TTT-Readme-skill** | Crafts publication-grade bilingual GitHub READMEs with bundled OFL fonts, transparent exhibition panel scripts, and dark/light QA | [SKILL.md](./skills/TTT-Readme-skill/SKILL.md) · [Panel Script](./skills/TTT-Readme-skill/scripts/editorial_panel.py) |

<br>

<h1 id="notes" align="center"><sub><samp>04</samp></sub><br>Prerequisites &amp; notes<br><sub>Runtime requirements</sub></h1>

- **PDF compilation**: **TTT-MonoPDF-skill** requires a local XeLaTeX distribution (MacTeX or TeX Live), Poppler (`pdftoppm`) for page inspection, and macOS system typefaces (PingFang SC and Helvetica Neue).
- **Exhibition panel scripts**: **TTT-Readme-skill** uses Python 3 and Pillow to compose transparent exhibition panels and QA sheets; all three required SIL OFL display and editorial fonts are bundled directly inside the skill.
- **Authoring & local sync**: The local symlink helper targets macOS and Linux environments; see the [Authoring Guide](./AGENTS.md) for naming conventions and the 5-step release checklist.

<hr>
<p align="center"><sub>TTTIM-skills &nbsp;·&nbsp; <a href="./README.md">中文</a> &nbsp;·&nbsp; <a href="./AGENTS.md">Authoring Guide</a></sub></p>
