# Design System Showcase

This page renders every component, pattern, and figure style defined in the book's
design system, so the current settings can be checked visually in one place. It is a
living reference: if a component changes, this page should change with it. The
authoritative catalog is `DESIGN-SYSTEM.md` at the repository root.

Toggle the light/dark switch in the header to confirm each element adapts.

## Foundations

### Colour tokens

The brand palette and the semantic outcome tints, with live swatches.

<table markdown>
<tr><th>Swatch</th><th>Token</th><th>Hex</th><th>Role</th></tr>
<tr><td><span style="display:inline-block;width:2.2em;height:1.1em;background:#007BA7;border:1px solid #8884"></span></td><td><code>--color-cerulean</code></td><td><code>#007BA7</code></td><td>Primary; body links</td></tr>
<tr><td><span style="display:inline-block;width:2.2em;height:1.1em;background:#800020;border:1px solid #8884"></span></td><td><code>--color-burgundy</code></td><td><code>#800020</code></td><td>Accent; theorem</td></tr>
<tr><td><span style="display:inline-block;width:2.2em;height:1.1em;background:#9B7FA7;border:1px solid #8884"></span></td><td><code>--color-thistle-dark</code></td><td><code>#9B7FA7</code></td><td>Definition; blockquote</td></tr>
<tr><td><span style="display:inline-block;width:2.2em;height:1.1em;background:#C9A55E;border:1px solid #8884"></span></td><td><code>--color-navajo-dark</code></td><td><code>#C9A55E</code></td><td>Abstract accent</td></tr>
<tr><td><span style="display:inline-block;width:2.2em;height:1.1em;background:#B87D6C;border:1px solid #8884"></span></td><td><code>--color-sunset</code></td><td><code>#B87D6C</code></td><td>Header</td></tr>
<tr><td><span style="display:inline-block;width:2.2em;height:1.1em;background:#DCEFD8;border:1px solid #8884"></span></td><td><code>--color-good</code></td><td><code>#DCEFD8</code></td><td>Outcome — sufficient</td></tr>
<tr><td><span style="display:inline-block;width:2.2em;height:1.1em;background:#FFE9C2;border:1px solid #8884"></span></td><td><code>--color-escalate</code></td><td><code>#FFE9C2</code></td><td>Outcome — escalate</td></tr>
<tr><td><span style="display:inline-block;width:2.2em;height:1.1em;background:#F2D9DE;border:1px solid #8884"></span></td><td><code>--color-problem</code></td><td><code>#F2D9DE</code></td><td>Outcome — problem</td></tr>
</table>

### Typography

Content headings H1–H3 use Source Serif 4; H4 and below use Inter. This page's own
headings demonstrate the scale: the H1 above, the H2 section headers, and the H3/H4
below.

#### This is an H4 subsection

Body prose uses a 1.75 line-height for readability. A run of running text shows the
body register, with an inline <span class="highlight-text">highlighted phrase</span>
using the `highlight-text` utility.

## Admonitions

!!! theorem "Theorem (Gauss–Markov)"
    Under the classical assumptions, the OLS estimator is the best linear unbiased
    estimator (BLUE).

!!! definition "Definition: Stationarity"
    A series is weakly stationary if its mean and autocovariances do not change over time.

!!! note "Remark"
    Notes and remarks use the Cerulean note admonition for informational asides.

!!! abstract "Chapter summary"
    The abstract admonition, in Navajo, is used for chapter and section overviews.

## Custom boxes

<div class="hypothesis-test" markdown>
<h4>Augmented Dickey–Fuller Test</h4>

<div class="null-hypothesis" markdown>
The series has a unit root (non-stationary): \( \gamma = 0 \).
</div>

<div class="alternative-hypothesis" markdown>
The series is stationary: \( \gamma < 0 \).
</div>

<div class="decision-rule" markdown>
**Decision rule:** reject \( H_0 \) when the p-value falls below \( \alpha = 0.05 \).
</div>
</div>

## Annotations and pronunciation guides

The "common alternative forms" pattern parks equivalent notation in a numbered note.

<div class="annotate" markdown>

!!! theorem "Assumption: Strict Exogeneity"
    $$\EE[\epsilon_t \mid \mathbf{X}] = 0$$

    (Read: the expected value of epsilon-sub-t given X equals zero.)

The error is uncorrelated with the regressors at all leads and lags. (1)

</div>

1.  **Common alternative forms:**
    - \( \text{Cov}(\mathbf{x}_t, \epsilon_t) = 0 \) — the covariance form
    - \( \EE[\epsilon_t \mid \mathbf{x}_t] = 0 \) — contemporaneous exogeneity (weaker)

Every display equation is followed by a pronunciation guide, as above. Acronyms such as
ACF expand on hover via the abbreviation tooltip.

*[ACF]: Autocorrelation Function

## Tables

A plain comparison table:

| Estimator | Closed form | Handles unobservable errors |
|---|---|---|
| OLS | Yes | No |
| MLE | No | Yes |
| GMM | No | Partial |

A colour-coded decision matrix (each cell states its verdict as text, so colour is never
the sole signal):

<table class="decision-matrix" markdown>
<tr><th>ADF</th><th>KPSS</th><th>Verdict</th></tr>
<tr><td>Reject</td><td>Fail to reject</td><td class="good">Stationary</td></tr>
<tr><td>Fail to reject</td><td>Reject</td><td class="problem">Unit root — difference</td></tr>
<tr><td>Reject</td><td>Reject</td><td class="escalate">Inconclusive — inspect</td></tr>
</table>

## Decision-flowchart notation

Brand palette:

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    START([Time-stamped data]) --> ROOT_TEST[Run ADF + KPSS]
    ROOT_TEST --> UNITROOT{Unit root?}
    UNITROOT -->|Yes| DIFF[Difference the series]
    UNITROOT -->|No| OK[Model: OLS<br/>Estimator: OLS]

    class START terminator
    class ROOT_TEST,DIFF process
    class UNITROOT decision
    class OK good

    classDef terminator fill:#E6F2F7,stroke:#007BA7,color:#1A1A1A;
    classDef process fill:#FFFFFF,stroke:#5A6B73,color:#1A1A1A;
    classDef decision fill:#EFE7F0,stroke:#9B7FA7,color:#1A1A1A;
    classDef good fill:#DCEFD8,stroke:#4A7A3F,color:#1A1A1A;
```

Colorblind-safe palette (same diagram):

```mermaid
%%{init: {"flowchart": {"curve": "linear"}}}%%
graph TD
    START([Time-stamped data]) --> ROOT_TEST[Run ADF + KPSS]
    ROOT_TEST --> UNITROOT{Unit root?}
    UNITROOT -->|Yes| DIFF[Difference the series]
    UNITROOT -->|No| OK[Model: OLS<br/>Estimator: OLS]

    class START terminator
    class ROOT_TEST,DIFF process
    class UNITROOT decision
    class OK good

    classDef terminator fill:#56B4E9,stroke:#005A7A,color:#000000;
    classDef process fill:#FFFFFF,stroke:#000000,color:#000000;
    classDef decision fill:#0072B2,stroke:#003D5C,color:#FFFFFF;
    classDef good fill:#009E73,stroke:#005A41,color:#FFFFFF;
```

## Static figures

Generated via `brand.py` and the `brand.mplstyle` style. Regenerate with
`python scripts/generate_showcase_figures.py`.

![Multi-series line plot in the brand palette: four cumulative series labelled Actual, Forecast, Lower band, and Upper band, over a time index from 0 to 60.](assets/figures/showcase_lines_brand.png)

*Figure: multi-series line plot, brand palette.*

![The same multi-series line plot rendered in the colorblind-safe Okabe–Ito palette.](assets/figures/showcase_lines_cb.png)

*Figure: the same plot in the colorblind-safe palette.*

![Sequential heatmap of a 12 by 12 grid using a single-hue Cerulean colour ramp from white to deep cerulean, with an intensity colour bar.](assets/figures/showcase_heatmap.png)

*Figure: sequential heatmap, single-hue Cerulean ramp.*

## Interactive components

The glossary drawer highlights defined terms across the book and opens a right-slide
panel on click; it requires no per-page markup. Tabbed sets group parallel content:

=== "OLS"
    Closed-form estimator; valid under i.i.d. errors.

=== "MLE"
    Required when the model contains unobservable error components.

=== "GMM"
    Matches sample moments to their theoretical counterparts.
