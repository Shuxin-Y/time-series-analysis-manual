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
from matplotlib import font_manager
from cycler import cycler

_ROOT = Path(__file__).resolve().parent
_STYLE = _ROOT / "docs" / "assets" / "brand.mplstyle"

# Register the bundled Inter faces (the book's body typeface) so figures use Inter
# regardless of what is installed system-wide, and so regeneration is reproducible.
for _ttf in sorted((_ROOT / "assets" / "fonts" / "inter").glob("*.ttf")):
    try:
        font_manager.fontManager.addfont(str(_ttf))
    except Exception:  # pragma: no cover - font registration is best-effort
        pass

# The brand colour cycle is defined once, in brand.mplstyle (its single source of
# truth). Only the colorblind-safe cycle lives here, because it is a per-call
# alternative rather than the default that the style file already applies.
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
    if palette == "cb":
        mpl.rcParams["axes.prop_cycle"] = cycler(color=_CB_CYCLE)
