#!/usr/bin/env python3
"""Compose Swiss-editorial transparent exhibition panels (dark + light pairs) for GitHub READMEs.

Features:
- 1800px transparent RGBA canvas so typography and framed visuals float directly on GitHub's dark/light page.
- Bundled SIL OFL fonts: BigShoulders-Bold (display), CrimsonPro-Italic (editorial serif), DMMono-Regular (metadata/rails).
- 3x-supersampled antialiased 1px rounded frames with optional 45-degree bottom-right corner chamfers (`cut`).
- Usable both as a clean Python library (`from editorial_panel import EditorialPanel, export_pair`) and as a JSON CLI.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Callable

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps

SKILL_ROOT = Path(__file__).resolve().parents[1]
FONTS_DIR = SKILL_ROOT / "assets" / "fonts"

WIDTH = 1800
MARGIN = 80
INNER_WIDTH = WIDTH - 2 * MARGIN  # 1640
DISPLAY_SIZE = 164
CAPTION_SIZE = 23
HERO_RADIUS = 14
DETAIL_RADIUS = 10


def palette(light: bool = False, accent_dark: str | None = None, accent_light: str | None = None) -> dict[str, str]:
    if light:
        return {
            "ink": "#24292f",
            "muted": "#57606a",
            "rail": "#d0d7de",
            "frame": "#b7bec6",
            "accent": accent_light or "#24292f",
        }
    return {
        "ink": "#e6edf3",
        "muted": "#9da7b3",
        "rail": "#303943",
        "frame": "#424a54",
        "accent": accent_dark or "#e6edf3",
    }


def load_font(face: str, size: int) -> ImageFont.FreeTypeFont:
    font_map = {
        "display": "BigShoulders-Bold.ttf",
        "serif": "CrimsonPro-Italic.ttf",
        "mono": "DMMono-Regular.ttf",
    }
    filename = font_map.get(face, face)
    return ImageFont.truetype(str(FONTS_DIR / filename), size)


def draw_frame(
    canvas: Image.Image,
    box: tuple[int, int, int, int],
    radius: int = HERO_RADIUS,
    cut: int = 0,
    color: str = "#424a54",
) -> None:
    """Apply rounded/chamfered alpha silhouette and 3x-supersampled 1px antialiased border."""
    x, y, width, height = box
    scale = 3
    size = (width * scale, height * scale)

    def silhouette(inset: int) -> Image.Image:
        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        right, bottom = size[0] - 1, size[1] - 1
        draw.rounded_rectangle(
            (inset, inset, right - inset, bottom - inset),
            radius=max(0, radius * scale - inset),
            fill=255,
        )
        if cut:
            diagonal = cut * scale + round(inset * 1.414)
            draw.polygon(
                [(right, bottom - diagonal), (right - diagonal, bottom), (right, bottom)],
                fill=0,
            )
        return mask

    outer = silhouette(0)
    inner = silhouette(3)  # 1px stroke at final resolution
    alpha = outer.resize((width, height), Image.Resampling.LANCZOS)
    region = canvas.crop((x, y, x + width, y + height))
    region.putalpha(alpha)
    canvas.paste(region, (x, y))

    border = Image.new("RGBA", size, color)
    border.putalpha(ImageChops.subtract(outer, inner))
    canvas.alpha_composite(border.resize((width, height), Image.Resampling.LANCZOS), (x, y))


class EditorialPanel:
    """Builder for a single 1800px-wide transparent magazine exhibition panel."""

    def __init__(
        self,
        height: int,
        light: bool = False,
        accent_dark: str | None = None,
        accent_light: str | None = None,
    ) -> None:
        self.light = light
        self.colors = palette(light, accent_dark=accent_dark, accent_light=accent_light)
        self.canvas = Image.new("RGBA", (WIDTH, height), (0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.canvas)

    def text(
        self,
        xy: tuple[float, float],
        value: str,
        size: int = CAPTION_SIZE,
        face: str = "mono",
        color: str | None = None,
        align: str = "left",
    ) -> None:
        f = load_font(face, size)
        fill = self.colors.get(color, color) if color else self.colors["ink"]
        x, y = xy
        if align == "right":
            x -= f.getlength(value)
        elif align == "center":
            x -= f.getlength(value) / 2
        self.draw.text((x, y), value, font=f, fill=fill)

    def rail_header(self, left: str, right: str, y: int = 35, rule_y: int = 86) -> None:
        self.text((MARGIN, y), left, size=23, face="mono", color="muted")
        self.text((WIDTH - MARGIN, y), right, size=23, face="mono", color="muted", align="right")
        self.draw.line((MARGIN, rule_y, WIDTH - MARGIN, rule_y), fill=self.colors["rail"], width=2)

    def masthead(
        self,
        title: str,
        quote: str | None = None,
        kicker: str | None = None,
        y: int = 108,
        title_size: int = DISPLAY_SIZE,
        title_leading: int = 160,
        quote_x: int = 1040,
        quote_y: int | None = None,
        quote_size: int = 52,
    ) -> None:
        lines = title.split("\n")
        for idx, line in enumerate(lines):
            self.text((MARGIN - 5, y + idx * title_leading), line, size=title_size, face="display", color="ink")

        qy = quote_y if quote_y is not None else (y + 52)
        if quote:
            q_lines = quote.split("\n")
            for idx, q_line in enumerate(q_lines):
                self.text((quote_x, qy + idx * round(quote_size * 1.18)), q_line, size=quote_size, face="serif", color="ink")
            qy += len(q_lines) * round(quote_size * 1.18) + 22
        if kicker:
            for idx, k_line in enumerate(kicker.split("\n")):
                self.text((quote_x, qy + idx * 34), k_line, size=22, face="mono", color="muted")

    def picture(
        self,
        source: Image.Image | str | Path,
        box: tuple[int, int, int, int],
        radius: int = HERO_RADIUS,
        cut: int = 0,
        fit: str = "cover",
        bg: str = "#ffffff",
        centering: tuple[float, float] = (0.5, 0.5),
    ) -> None:
        img = Image.open(source) if isinstance(source, (str, Path)) else source
        x, y, w, h = box
        if fit == "contain":
            tile = Image.new("RGBA", (w, h), bg)
            contained = ImageOps.contain(img.convert("RGBA"), (w, h), method=Image.Resampling.LANCZOS)
            ox = (w - contained.width) // 2
            oy = (h - contained.height) // 2
            tile.alpha_composite(contained, (ox, oy))
        else:
            tile = ImageOps.fit(img.convert("RGBA"), (w, h), method=Image.Resampling.LANCZOS, centering=centering)
        self.canvas.paste(tile, (x, y))
        draw_frame(self.canvas, box, radius=radius, cut=cut, color=self.colors["frame"])

    def caption(self, xy: tuple[float, float], value: str, size: int = 21, align: str = "left") -> None:
        self.text(xy, value, size=size, face="mono", color="muted", align=align)

    def timeline_rail(self, y: int, stages: list[str]) -> None:
        self.draw.line((MARGIN, y, WIDTH - MARGIN, y), fill=self.colors["rail"], width=2)
        if not stages:
            return
        n = len(stages)
        if n == 1:
            self.draw.ellipse((MARGIN, y - 6, MARGIN + 12, y + 6), fill=self.colors["muted"])
            self.caption((MARGIN, y + 24), stages[0], size=21)
            return
        last_w = load_font("mono", 21).getlength(stages[-1])
        end_x = round(WIDTH - MARGIN - max(last_w, 12))
        span = max(200, end_x - MARGIN)
        step = span / (n - 1)
        for idx, label in enumerate(stages):
            x = round(MARGIN + idx * step)
            self.draw.ellipse((x, y - 6, x + 12, y + 6), fill=self.colors["muted"])
            self.caption((x, y + 24), label, size=21)


def export_pair(
    builder: Callable[[bool], EditorialPanel | Image.Image],
    out_dir: str | Path,
    name: str,
) -> tuple[Path, Path]:
    """Render both `<name>.png` (dark) and `<name>-light.png` (light) in one call."""
    dest = Path(out_dir)
    dest.mkdir(parents=True, exist_ok=True)
    outputs = []
    for light, suffix in [(False, ""), (True, "-light")]:
        result = builder(light)
        im = result.canvas if isinstance(result, EditorialPanel) else result
        target = dest / f"{name}{suffix}.png"
        im.save(target, optimize=True)
        outputs.append(target)
    return outputs[0], outputs[1]


def build_from_spec(spec_path: Path) -> None:
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    base = spec_path.parent

    def _build(light: bool) -> EditorialPanel:
        panel = EditorialPanel(
            height=spec["height"],
            light=light,
            accent_dark=spec.get("accent_dark"),
            accent_light=spec.get("accent_light"),
        )
        if "rail_header" in spec:
            rh = spec["rail_header"]
            panel.rail_header(rh["left"], rh["right"], y=rh.get("y", 35), rule_y=rh.get("rule_y", 86))
        if "masthead" in spec:
            mh = spec["masthead"]
            panel.masthead(
                title=mh["title"],
                quote=mh.get("quote"),
                kicker=mh.get("kicker"),
                y=mh.get("y", 108),
                title_size=mh.get("title_size", DISPLAY_SIZE),
                title_leading=mh.get("title_leading", 160),
                quote_x=mh.get("quote_x", 1040),
                quote_y=mh.get("quote_y"),
                quote_size=mh.get("quote_size", 52),
            )
        for pic in spec.get("pictures", []):
            src_key = "src_light" if (light and "src_light" in pic) else "src"
            src = Path(pic[src_key])
            if not src.is_absolute():
                src = base / src
            panel.picture(
                src,
                tuple(pic["box"]),
                radius=pic.get("radius", HERO_RADIUS),
                cut=pic.get("cut", 0),
                fit=pic.get("fit", "cover"),
                bg=pic.get("bg", "#ffffff"),
            )
        for cap in spec.get("captions", []):
            panel.caption(tuple(cap["xy"]), cap["text"], size=cap.get("size", 21), align=cap.get("align", "left"))
        if "timeline_rail" in spec:
            tr = spec["timeline_rail"]
            panel.timeline_rail(tr["y"], tr["stages"])
        return panel

    out_dir = Path(spec["out_dir"])
    if not out_dir.is_absolute():
        out_dir = base / out_dir
    dark_path, light_path = export_pair(_build, out_dir, spec["name"])
    print(f"Exported: {dark_path} & {light_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build dark/light editorial README panels from a JSON spec.")
    parser.add_argument("spec", type=Path, help="Path to JSON panel specification.")
    args = parser.parse_args()
    build_from_spec(args.spec)
