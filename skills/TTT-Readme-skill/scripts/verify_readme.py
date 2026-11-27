#!/usr/bin/env python3
"""Validate, cache-stamp (`?v=<sha8>`), and render dark/light visual QA sheets for GitHub READMEs."""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path
from PIL import Image

ASSET_ATTR_RE = re.compile(r'((?:src|srcset)=")(\./assets/[^"?]+)(?:\?v=[0-9a-f]+)?(")')
REL_HREF_RE = re.compile(r'(?:href|src|srcset)="(\./[^"#?]+)')
MD_LINK_RE = re.compile(r'\]\((\./[^)#?]+)')
BADGE_RE = re.compile(r'img\.shields\.io/badge/')


def check_links_and_clutter(root: Path, md_file: Path) -> list[str]:
    issues: list[str] = []
    text = md_file.read_text(encoding="utf-8")

    # 1. Verify all relative `./...` targets exist
    rel_targets = set(REL_HREF_RE.findall(text)) | set(MD_LINK_RE.findall(text))
    for rel in sorted(rel_targets):
        target = (root / rel).resolve()
        if not target.exists():
            issues.append(f"[{md_file.name}] Missing relative target: {rel}")

    # 2. Check badge count (anti-clutter: max 5 shields.io badges in opening header)
    top_chunk = "\n".join(text.splitlines()[:45])
    badge_count = len(BADGE_RE.findall(top_chunk))
    if badge_count > 5:
        issues.append(f"[{md_file.name}] Too many shields.io badges in header ({badge_count} > 5). Trim filler badges.")

    # 3. Anti-gray-soup check: flag prose lines/paragraphs with > 3 inline code pills
    in_fence = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or stripped.startswith("|") or stripped.startswith("<!--"):
            continue
        backticks = len(re.findall(r"`[^`]+`", line))
        code_tags = len(re.findall(r"<code>.*?</code>", line))
        pills = backticks + code_tags
        if pills > 3:
            issues.append(
                f"[{md_file.name}:{lineno}] High inline-code pill density ({pills} in one line). "
                "Prefer bold or plain prose to avoid gray-pill clutter."
            )

    return issues


def stamp_assets(root: Path, md_file: Path) -> int:
    text = md_file.read_text(encoding="utf-8")

    def _replace(match: re.Match[str]) -> str:
        rel_path = match.group(2)
        asset = root / rel_path
        if not asset.exists():
            raise FileNotFoundError(f"{md_file.name}: missing asset {rel_path}")
        digest = hashlib.sha256(asset.read_bytes()).hexdigest()[:8]
        return f"{match.group(1)}{rel_path}?v={digest}{match.group(3)}"

    stamped, count = ASSET_ATTR_RE.subn(_replace, text)
    if stamped != text:
        md_file.write_text(stamped, encoding="utf-8")
    return count


def render_qa_previews(root: Path, out_dir: Path) -> list[Path]:
    """Composite transparent PNGs onto GitHub Dark (#0d1117) and Light (#ffffff) backgrounds, and rasterize SVGs."""
    out_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = root / "assets" / "readme"
    if not assets_dir.exists():
        return []

    generated: list[Path] = []
    for png in sorted(assets_dir.rglob("*.png")):
        im = Image.open(png).convert("RGBA")
        is_light = png.stem.endswith("-light")
        bg_hex = "#ffffff" if is_light else "#0d1117"
        pad = 48
        sheet = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), bg_hex)
        sheet.alpha_composite(im, (pad, pad))
        # Downscale to 1200px wide for crisp, fast vision QA
        if sheet.width > 1200:
            ratio = 1200 / sheet.width
            sheet = sheet.resize((1200, round(sheet.height * ratio)), Image.Resampling.LANCZOS)
        target = out_dir / f"qa_{png.stem}.png"
        sheet.convert("RGB").save(target, optimize=True)
        generated.append(target)

    for svg in sorted(assets_dir.rglob("*.svg")):
        try:
            subprocess.run(
                ["qlmanage", "-t", "-s", "1200", "-o", str(out_dir), str(svg)],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            ql_out = out_dir / f"{svg.name}.png"
            if ql_out.exists():
                target = out_dir / f"qa_{svg.stem}.png"
                ql_out.replace(target)
                generated.append(target)
        except Exception:
            pass

    return generated


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify README links, inline-code density, stamp hashes, and render QA sheets.")
    parser.add_argument("repo_root", type=Path, nargs="?", default=Path("."), help="Target repository root.")
    parser.add_argument("--stamp", action="store_true", help="Stamp ./assets/... URLs with ?v=<sha8> content hash.")
    parser.add_argument("--render-qa", type=Path, default=None, help="Directory to output dark/light visual QA PNGs.")
    args = parser.parse_args()

    root = args.repo_root.resolve()
    readme_files = [p for p in [root / "README.md", root / "README.en.md"] if p.exists()]
    if not readme_files:
        print(f"No README.md found in {root}", file=sys.stderr)
        return 1

    if args.stamp:
        for md in readme_files:
            n = stamp_assets(root, md)
            print(f"Stamped {n} asset URL(s) in {md.name}")

    all_issues: list[str] = []
    for md in readme_files:
        all_issues.extend(check_links_and_clutter(root, md))

    if args.render_qa:
        qa_files = render_qa_previews(root, args.render_qa.resolve())
        print(f"Rendered {len(qa_files)} QA preview image(s) to {args.render_qa}:")
        for p in qa_files:
            print(f"  - {p}")

    if all_issues:
        print("\nValidation warnings / errors:", file=sys.stderr)
        for item in all_issues:
            print(f"  ! {item}", file=sys.stderr)
        return 1

    print("OK: All relative links valid and prose inline-code density is clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
