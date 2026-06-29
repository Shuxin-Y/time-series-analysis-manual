"""Audit design-system colour tokens: WCAG AA contrast + hex drift.

Run: python scripts/audit_palette.py
Exits non-zero if any documented colour drifts from extra.css: the decision-matrix
fills, or the brand colour cycle baked into brand.mplstyle.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "docs" / "stylesheets" / "extra.css"
MPLSTYLE = ROOT / "docs" / "assets" / "brand.mplstyle"

# Semantic / structural fills that carry body text (must pass AA against text).
FILLS = {
    "terminator": "#E6F2F7", "decision": "#EFE7F0", "data": "#FFF4E0",
    "good": "#DCEFD8", "escalate": "#FFE9C2", "problem": "#F2D9DE",
}
TEXT_DARK = "#1A1A1A"  # default body text in light mode (approx)


def _lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_):
    r, g, b = (int(hex_[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(fg, bg):
    l1, l2 = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def main():
    print("WCAG contrast of body text on tinted fills (AA body >= 4.5):")
    for name, fill in FILLS.items():
        ratio = contrast(TEXT_DARK, fill)
        flag = "PASS" if ratio >= 4.5 else "FLAG (large-text/bold only)"
        print(f"  {name:11s} {fill}  {ratio:5.2f}:1  {flag}")

    css = CSS.read_text().lower()
    failed = False

    cell = {"#DCEFD8", "#FFE9C2", "#F2D9DE"}
    drift = [h for h in cell if h.lower() not in css]
    if drift:
        print(f"\nDRIFT: decision-matrix colours missing from extra.css: {drift}")
        failed = True
    else:
        print("\nDecision-matrix cell colours present in extra.css: OK")

    # The brand colour cycle lives in brand.mplstyle (its source of truth). Guard
    # it against drift from the CSS :root tokens, which Python cannot read directly.
    mpl_text = MPLSTYLE.read_text()
    match = re.search(r"prop_cycle:.*\[([^\]]*)\]", mpl_text)
    brand = ["#" + h.strip().strip("'\"") for h in match.group(1).split(",")]
    brand_drift = [h for h in brand if h.lower() not in css]
    if brand_drift:
        print(f"Brand cycle colours in brand.mplstyle missing from extra.css: {brand_drift}")
        failed = True
    else:
        print("Brand cycle (brand.mplstyle) present in extra.css: OK")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
