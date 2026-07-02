"""Generate sample figures for the design-system showcase page.

Run: python scripts/generate_showcase_figures.py

Renders three figures via the brand matplotlib style (brand.py) and writes them
to docs/assets/figures/ for embedding in docs/design-system-showcase.md:
  - showcase_lines_brand.png  multi-series line plot, brand palette
  - showcase_lines_cb.png     same data, colorblind-safe palette
  - showcase_heatmap.png      sequential single-hue (Cerulean) heatmap
"""
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: write files without a display

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import brand  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

OUT = ROOT / "docs" / "assets" / "figures"

# Reader-facing palette names, keyed by the internal palette argument.
_PALETTE_TITLE = {"brand": "brand palette", "cb": "colorblind-safe palette"}


def line_plot(path: Path, palette: str) -> None:
    brand.use_brand_style(palette)
    rng = np.random.default_rng(42)
    t = np.arange(60)
    fig, ax = plt.subplots()
    for offset, label in enumerate(["Actual", "Forecast", "Lower band", "Upper band"]):
        series = np.cumsum(rng.normal(0.15, 1.0, size=t.size)) + offset * 4
        ax.plot(t, series, label=label)
    ax.set_title(f"Multi-series line plot ({_PALETTE_TITLE[palette]})")
    ax.set_xlabel("Time index $t$")
    ax.set_ylabel("Value")
    ax.legend()
    fig.savefig(path)
    plt.close(fig)


def heatmap(path: Path) -> None:
    brand.use_brand_style()
    cmap = brand.cerulean_cmap()
    rng = np.random.default_rng(7)
    data = rng.random((12, 12))
    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap=cmap, aspect="auto")
    ax.set_title("Sequential heatmap (Cerulean ramp)")
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")
    fig.colorbar(im, ax=ax, label="Value (illustrative)")
    fig.savefig(path)
    plt.close(fig)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    line_plot(OUT / "showcase_lines_brand.png", "brand")
    line_plot(OUT / "showcase_lines_cb.png", "cb")
    heatmap(OUT / "showcase_heatmap.png")
    print("wrote:", ", ".join(sorted(p.name for p in OUT.glob("showcase_*.png"))))
