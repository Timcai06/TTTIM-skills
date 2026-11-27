# SVG & Editorial Visual Specification (`TTT-Readme-skill`)

All README visuals should feel native to GitHub in both dark and light modes, with zero clashing backgrounds and a color accent derived from the **target project**.

## 1. Canvas & Adaptive Palette Rules

Always pair `*-dark.svg` and `*-light.svg` on a fixed **840px** logical width (`viewBox="0 0 840 <height>"`, `width="840" height="<height>"`).

### Fixed GitHub-Native Neutrals
| Role | Dark Mode (`*-dark.svg`) | Light Mode (`*-light.svg`) |
| :--- | :--- | :--- |
| Canvas background | `#0d1117` | `#ffffff` |
| Primary card fill | `#121820` | `#f6f8fa` |
| Secondary card fill | `#161d26` | `#f0f4f7` |
| Hairline / border | `#26303c` | `#d8dee4` |
| Primary ink | `#f0f3f6` | `#1f2328` |
| Secondary ink | `#9da7b3` | `#57606a` |
| Muted / metadata ink | `#6e7885` | `#768390` |

### Project-Derived Accent Color (Do NOT hardcode one brand color)
Before authoring SVGs, determine the accent pair from the target repository:
1. **Check the repo first**: look for CSS variables (`tokens.css`, `globals.css`), Tailwind `theme.extend.colors`, design docs, logo SVGs, or existing UI screenshots.
2. **Derive a dark/light pair** from that primary hue:
   - **Dark accent**: brighter, medium-high lightness (WCAG-readable on `#0d1117`), with a soft tint fill `rgba(R,G,B,0.10)` and stroke `rgba(R,G,B,0.42)`.
   - **Light accent**: deeper, richer shade of the same hue (WCAG-readable on `#ffffff`), with subtle tint fill `rgba(R,G,B,0.08)` and stroke `rgba(R,G,B,0.36)`.
3. **Fallback when repo has no brand color**: choose a restrained monochrome/slate or domain-appropriate accent (e.g., cool blue for systems/CLI, amber for creative/media, emerald/teal for data/science) and keep it consistent across all SVGs in that repo.

## 2. Hero SVG Spec (`hero-dark.svg` / `hero-light.svg`)

- **Dimensions**: `viewBox="0 0 840 184"` (compact, editorial banner; never tall billboard art).
- **Layer order**:
  1. Solid canvas rect (`#0d1117` or `#ffffff`).
  2. Subtle radial glow (`opacity: 0.08–0.10`) using the project's accent color.
  3. Subtle background motif matching the project (e.g., fine dot/coordinate grid, geometric waves, contour lines, or clean minimal rails) clipped to `840×184` and softened by horizontal (`edgeFade`) and vertical (`vertFade`) gradients to the canvas color.
  4. Top eyebrow pill (`rx="4"`, monospace `10.5px`, uppercase, `letter-spacing="1.4"`, tinted accent fill + border).
  5. Centered title (`y="106"`, `font-size="36–42"`, clean typographic contrast such as italic serif brand + `/` + semibold sans module, or bold sans project title).
  6. 1-line subtitle (`y="142"`, `font-size="14"`, secondary ink).
  7. Bottom hairline rule (`x1="120" x2="720" y="172"`).

## 3. Architecture & Flow SVG Spec (`arch-*.svg` / `flow-*.svg`)

- **Dimensions**: `width="840"`, `height="220–290"` depending on rows.
- **Horizontal track**: centered `780px` content zone (`x="30"` to `x="810"`, `30px` margins left/right).
- **Header eyebrow**: centered monospace uppercase label at `y="24"` (`font-size="10.5"`, `letter-spacing="1.4"`, muted ink).
- **Cards**: `rx="10"`, `stroke-width="1.1–1.2"`, crisp internal divider lines, 2–3 levels of typography (`14–15px` semibold title, `11px` monospace path/tag in accent color, `11.5–12px` secondary body).
- **Motion & Accessibility**:
  - Subtle CSS animations (e.g., dashed flow arrows or a slow scanning highlight bar) are optional.
  - **Mandatory**: include `@media (prefers-reduced-motion: reduce) { .anim { animation: none !important; } }` inside `<style>`, and provide `<title>` inside every `<svg role="img">`.

## 4. Editorial Screenshot Posters (Optional, for UI Projects)

When raw UI screenshots look cluttered on GitHub:
- Composite 2–4 real screenshots onto a clean transparent or dark/light canvas (e.g., `1800px` wide) with consistent padding, subtle `1px` frames, rounded corners, and short monospace captions.
- Export paired `poster-<name>.png` (dark) and `poster-<name>-light.png` (light) and embed via `<picture>`.
- Never fabricate UI screens; always crop/composite from real captures.
