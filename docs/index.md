# Time Series Analysis Manual

!!! abstract "A Comprehensive, Practical Guide"
    This manual bridges classical econometrics and modern machine learning approaches to time series analysis. It provides rigorous mathematical foundations alongside production-ready Python implementations.

---

## What Makes This Book Different?

<div class="grid cards" markdown>

- :material-chart-line: **Integrated Workflow**

    ---

    Seamlessly move between time domain, frequency domain, and time-frequency representations based on your data characteristics.

- :material-map-marker-path: **Decision Flowcharts**

    ---

    Three complementary flowcharts (general, purpose-based, representation-based) guide every analytical choice with explicit tests and thresholds.

- :material-flask: **Test-Driven Methodology**

    ---

    Every decision determined by hypothesis tests (ADF, KPSS, Ljung-Box) with clear interpretation rules - no guesswork.

- :material-code-braces: **Production-Ready Code**

    ---

    Mathematical theory paired with complete Python implementations. All code is tested, documented, and deployment-ready.

</div>

---

## Quick Start

=== "New to Time Series"

    **Start Here:**
    1. Read [Introduction](00-introduction/overview.md) to understand the philosophy
    2. Skim the [General Flowchart](01-master-flowchart/01-general-flowchart.md) for the big picture
    3. Follow the [Guided Walkthrough](01-master-flowchart/walkthrough.md) for detailed explanations
    4. Work through chapters 3-7 in order

=== "Have Specific Goals"

    **Jump to Purpose:**
    - **Forecasting** → [Purpose-Based Workflow](01-master-flowchart/02-purpose-workflow.md#1-forecasting-workflow)
    - **Causal Analysis** → [Purpose-Based Workflow](01-master-flowchart/02-purpose-workflow.md#2-causal-analysis--structural-inference)
    - **Anomaly Detection** → [Purpose-Based Workflow](01-master-flowchart/02-purpose-workflow.md#5-anomaly--regime-detection)
    - **Feature Engineering** → [Purpose-Based Workflow](01-master-flowchart/02-purpose-workflow.md#7-feature-extraction-for-ml)

=== "Know Your Domain"

    **Domain-Specific Guidance:**
    - **Finance** → [Representation Workflow](01-master-flowchart/03-representation-workflow.md#1-time-domain-representation)
    - **Signal Processing** → [Representation Workflow](01-master-flowchart/03-representation-workflow.md#2-frequency-domain-representation)
    - **Non-stationary Data** → [Representation Workflow](01-master-flowchart/03-representation-workflow.md#3-time-frequency-domain-representation)
    - **Irregular Sampling** → [Representation Workflow](01-master-flowchart/03-representation-workflow.md#4-state-space-representation)

=== "Want Examples"

    **See Code First:**
    - Browse code examples in each chapter
    - Check [Python Setup](appendices/C-python-environment-setup.md) for environment configuration
    - All code is available as standalone files in the `code/` directory

---

## Book Structure

The manual is organized into focused chapters that build progressively:

### Core Content

<div class="annotate" markdown>

1. **[Introduction](00-introduction/overview.md)** - Philosophy, target audience, and comparison with existing textbooks
2. **[Flowcharts](01-master-flowchart/01-general-flowchart.md)** - Three comprehensive decision workflows (1)
3. **[Data Preparation](02-data-preparation/index.md)** - Cleaning, sampling, and quality checks
4. **[Exploratory Analysis](03-exploratory-analysis/index.md)** - Stationarity, distributions, temporal structure
5. **[Frequency Domain](04-frequency-domain/index.md)** - Spectral analysis, periodicities, filtering
6. **[Modelling](05-modelling/index.md)** - ARIMA, VAR, GARCH, state-space, and ML approaches
7. **[Feature Extraction](06-feature-extraction/index.md)** - Engineering features for machine learning
8. **[Validation & Deployment](07-validation-deployment/index.md)** - Testing, monitoring, and production systems

</div>

1.  The three flowcharts provide complementary views:
    - **General**: Complete econometric workflow from data to deployment
    - **Purpose-Based**: Organized by analytical goal (forecasting, causal analysis, etc.)
    - **Representation-Based**: Organized by mathematical domain (time, frequency, state-space, etc.)

### Reference Materials

- **[Appendices](appendices/index.md)** - Mathematical foundations, statistical tests reference, datasets, and resources

---

## Interactive Features

!!! tip "Interactive Glossary"
    Starting from Chapter 3 (Data Preparation), technical terms are **clickable**. Click any highlighted term to see:

    - Clear definition
    - Mathematical formulation
    - Historical context
    - Reference to detailed documentation

    Try clicking on terms like **stationarity**, **ADF test**, or **ARIMA** when you encounter them!

---

## Philosophy

This manual follows five core principles:

1. **Test-Driven Decisions** :material-check-circle:{ .success }

    Every branch in the workflow is determined by hypothesis tests, not intuition. Clear decision rules with explicit p-value thresholds.

2. **Iterative Refinement** :material-reload:{ .info }

    Expect to loop back through sections. Residual diagnostics may reveal model inadequacy → adjust specification → retest. This is normal!

3. **Parsimony** :material-scale-balance:{ .warning }

    Start simple (ARIMA), add complexity only when diagnostics demand it. Simpler models often forecast better.

4. **Reproducibility** :material-code-braces:{ .primary }

    All methods are algorithmically specified with complete code. No "magic" parameters.

5. **Theory + Practice** :material-book-open-variant:{ .accent }

    Mathematical rigor paired with computational implementation. Understand *why* methods work, not just *how* to use them.

---

## Prerequisites

!!! info "Required Background"
    - **Statistics**: Mean, variance, hypothesis testing, confidence intervals
    - **Linear Algebra**: Vectors, matrices, eigenvalues (undergraduate level)
    - **Python**: NumPy, Pandas basics
    - **Calculus**: Derivatives, integrals (undergraduate level)

!!! success "NOT Required"
    - Advanced measure theory or real analysis
    - Prior time series experience
    - Econometric software expertise

---

## Citation

If you use this manual in your research or work, please cite:

```bibtex
@book{timeseries2024,
  title={Time Series Analysis Manual: A Comprehensive Practical Guide},
  author={Yang Shuxin},
  year={2025},
  publisher={[Publisher]},
  url={https://Shuxin-Y.github.io/time-series-analysis-manual}
}
```

---

## Contributing

This manual is open source and welcomes contributions:

- **Found an error?** Open an issue on [GitHub](https://github.com/Shuxin-Y/time-series-analysis-manual/issues)
- **Have a suggestion?** Submit a pull request
- **Want to add examples?** Contribute code to the `code/` directory

---

## License

This work is licensed under [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

---

<div class="text-center" markdown>

**[Get Started →](00-introduction/overview.md){ .md-button .md-button--primary }**
**[View Flowcharts →](01-master-flowchart/01-general-flowchart.md){ .md-button }**

</div>
