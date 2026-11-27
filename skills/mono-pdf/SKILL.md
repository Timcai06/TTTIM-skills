---
name: mono-pdf
description: Generate minimalist Swiss-editorial monochrome Chinese/English executive report PDFs via XeLaTeX (ctexart + PingFang SC / Helvetica Neue + TikZ). Use when the user asks to create a polished executive brief, proposal, technical architecture report, reimbursement summary, or design-grade PDF in monochrome editorial style.
---

# Swiss Editorial Monochrome PDF (`mono-pdf`)

Use this skill to produce publication-grade, minimalist monochrome Chinese/English executive PDFs using XeLaTeX (`ctexart`), inspired by Swiss international typographic style.

## Core Visual System

1. **Monochrome Palette (strictly black, white, and grays — zero rainbow colors)**:
   - `Ink` (`#111111`): primary text, section rules, primary solid fills
   - `Sub` (`#5C5C5C`): secondary descriptions, headers/footers, column headers
   - `Mute` (`#8C8C8C`): hatching patterns, subtle annotations
   - `Hair` (`#D6D6D6`): thin table row dividers
   - `Fill` (`#F2F2F2`) / `Fill2` (`#E4E4E4`): subtle light-gray bands in diagrams
   - `DarkBg` (`#000000`) / `DarkSub` (`#A6A6A6`) / `DarkLine` (`#3A3A3A`): cover page only

2. **Typography (macOS all sans-serif)**:
   - Latin: `Helvetica Neue` (Regular / Bold / Medium / UltraLight)
   - CJK: `PingFang SC` (Regular / Semibold / Medium / Thin)
   - Declare arrow glyphs (`"2192, "2190`) as CJK so `PingFang SC` renders them cleanly (`\xeCJKDeclareCharClass{CJK}{"2192, "2190}`).
   - Use **UltraLight / Thin** selectively on a secondary cover metric to create editorial contrast (e.g., 2 bold columns + 1 ultra-light column).

3. **Cover Page (Pure Black `#000000`, 1 page exact)**:
   - Top bar: bold brand name left, document category + date right, followed by a thin `0.5pt` white rule.
   - Upper title block: concise subtitle + large bold document title (`32pt`).
   - Hero centerpiece: oversized numeric or symbolic motif (`100–124pt`, e.g., `$169.87` or `5 · 4 · 3`).
   - Middle rule (`0.8pt` white) + **3-column `minipage[t]{0.3\linewidth}` KPI summary** (never use `\\` inside `tabularx` cells for multi-line cards).
   - Lower dark rule (`0.5pt`) + clean numbered table of contents (`01`–`06`) with white `\pageref` links (`\hypersetup{linkcolor=white}`).
   - Bottom metadata bar + `共 \pageref{LastPage} 页`.

4. **Interior Pages (Pure White, 1 section per page when possible)**:
   - Top running header: bold brand + gray doc title on left; gray `01 章节名` on right. Bottom running footer: context + date on left; `当前页 / 总页数` on right.
   - Section opener (`\Section{num}{short}{title}{lead}`): `1.3pt` solid black full-width rule → `28pt` bold title → concise 2–3 line executive lead.
   - Tables: minimal three-line style (`\TopRule 0.7pt Ink`, `\HeadRule 0.5pt Hair`, `\RowRule 0.3pt Hair`, `\BotRule 0.7pt Ink`), `8pt` gray column headers (`\ColHead`).
   - Callouts (`\KeyBox{title}{badge}{body}`): crisp `0.9pt` black border on white background, title left + bold badge right.
   - Diagrams (TikZ): flat monochrome architecture/layer/flow diagrams using solid `Ink` blocks (primary), `north east lines` hatched blocks (fallback/savings/secondary), `Fill` gray bands, and solid/hollow dots for primary/secondary ownership.

## Content Guidelines for Executive Reports

- **Keep it scannable**: target **5–8 pages** total including cover; generous whitespace and breathing room on every page.
- **One idea per page**: pair 1 crisp visual diagram or 1 structured table with concise narrative; avoid walls of text.
- **Avoid raw code dumps** unless the user explicitly asks for an engineering spec; prefer diagrams, comparison tables, and crisp bullet takeaways.

## Workflow & Mandatory Visual QA

1. Read the complete reference template at `references/template.tex` (in this skill's directory) and copy its preamble and macros as your starting point.
2. Author the `.tex` file for the user's topic.
3. Compile **twice** with XeLaTeX to resolve `\pageref` and `LastPage`:
   ```bash
   /Library/TeX/texbin/xelatex -interaction=nonstopmode "<file>.tex"
   /Library/TeX/texbin/xelatex -interaction=nonstopmode "<file>.tex"
   ```
4. Check the log for **zero errors, zero undefined references, zero missing glyphs, and zero `Overfull \hbox` / `Overfull \vbox`**.
5. Render every page to PNG and visually inspect each page:
   ```bash
   pdftoppm -png -r 120 "<file>.pdf" /tmp/pdf_qa/page
   ```
   Verify cover fits strictly on page 1, no text overlaps, margins and vertical balance feel airy, and all TikZ labels stay inside their boxes. Fix and recompile if any visual defect is found.
6. Remove `.aux`, `.log`, `.out` temporary files once clean.
