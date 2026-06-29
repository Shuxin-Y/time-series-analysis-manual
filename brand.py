"""Brand matplotlib styling for the Time Series Analysis Manual.

Apply the house figure style and colour cycle in one call, from any working
directory (the style path resolves relative to this file):

    import brand
    brand.use_brand_style()        # default brand palette
    brand.use_brand_style("cb")    # colorblind-safe (Okabe-Ito) palette

This helper drives the book's own figure-generation pipeline. Code shown to
readers is illustrative and is not expected to import this module.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

_STYLE = Path(__file__).resolve().parent / "docs" / "assets" / "brand.mplstyle"

_BRAND_CYCLE = ["#007BA7", "#800020", "#9B7FA7", "#C9A55E", "#B87D6C"]
_CB_CYCLE = [
    "#E69F00", "#56B4E9", "#009E73", "#F0E442",
    "#0072B2", "#D55E00", "#CC79A7", "#000000",
]


def use_brand_style(palette: str = "brand") -> None:
    """Apply the manual's matplotlib style and colour cycle.

    Args:
        palette: "brand" (default) or "cb" (colorblind-safe Okabe-Ito).
    """
    if palette not in ("brand", "cb"):
        raise ValueError(f"palette must be 'brand' or 'cb', got {palette!r}")
    plt.style.use(str(_STYLE))
    cycle = _CB_CYCLE if palette == "cb" else _BRAND_CYCLE
    mpl.rcParams["axes.prop_cycle"] = cycler(color=cycle)
