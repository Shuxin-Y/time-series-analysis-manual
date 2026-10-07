# Time Series Analysis Manual

A comprehensive, practical guide to time series analysis that bridges classical econometrics and modern machine learning approaches.

[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue)](https://shuxin-y.github.io/time-series-analysis-manual)
[![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 🎯 What Makes This Manual Different?

- **Flowcharts as the framework**: every section of the book is a leaf node of a workflow sub-diagram; follow the arrows, run the named test, land on the method
- **Derivation chains**: every method traces back to first principles through the glossary drawer
- **Test-Driven Methodology**: Every decision based on explicit hypothesis tests with clear interpretation rules
- **Integrated Workflow**: Seamlessly move between time domain, frequency domain, and time-frequency representations
- **Production-Ready Code**: Complete Python implementations with all dependencies and examples
- **Interactive Glossary**: Clickable technical terms with definitions, mathematical formulations, and historical context

---

## 📚 Content Overview

### Three axes

1. **Foundations** (`docs/00-foundations/`) - The model / estimator / test framework, OLS assumptions and how time series violates them, stochastic processes, asymptotics for dependent data; the roots of every derivation chain
2. **Workflow** (`docs/01-workflow/`) - The general flowchart: twelve phases P0 to P11 from raw data to a deployed model, with two decision indexes
   - Purpose (P2): ten analytical goals
   - Representation (P5): six mathematical representations
3. **Reference** (`docs/reference/`) - Thirty-four areas, each with its own chapter group; every leaf node of a workflow sub-diagram opens one reference section

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Basic knowledge of statistics, linear algebra, and Python

### Installation

```{bash}
# Clone the repository
git clone https://github.com/Shuxin-Y/time-series-analysis-manual.git
cd time-series-analysis-manual

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Local Development

```{bash}
# Serve documentation locally
mkdocs serve

# Open browser to http://127.0.0.1:8000
```

### Building

```{bash}
# Build static site
mkdocs build
```

---

## 📖 How to Use

Visit the live documentation at: **[https://shuxin-y.github.io/time-series-analysis-manual](https://shuxin-y.github.io/time-series-analysis-manual)**

Or build locally with `mkdocs serve`.

---

## 🤝 Contributing

Issues and pull requests are welcome. Pull requests must pass the tests, the flowchart audit and the strict build (see CLAUDE.md).

---

## 📜 License

Documentation: CC BY-SA 4.0. Code: MIT.

---

**[Read Online](https://shuxin-y.github.io/time-series-analysis-manual)** | **[Get Started](docs/00-foundations/ols-assumptions.md)**
