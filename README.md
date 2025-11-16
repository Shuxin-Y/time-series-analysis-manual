# Time Series Analysis Manual

A comprehensive, practical guide to time series analysis that bridges classical econometrics and modern machine learning approaches.

[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue)](https://yourusername.github.io/time-series-analysis-manual)
[![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 🎯 What Makes This Manual Different?

- **Decision Flowcharts as First-Class Citizens**: Three comprehensive flowcharts (general, purpose-based, representation-based) guide every analytical choice
- **Test-Driven Methodology**: Every decision based on explicit hypothesis tests with clear interpretation rules
- **Integrated Workflow**: Seamlessly move between time domain, frequency domain, and time-frequency representations
- **Production-Ready Code**: Complete Python implementations with all dependencies and examples
- **Interactive Glossary**: Clickable technical terms with definitions, mathematical formulations, and historical context

---

## 📚 Content Overview

### Core Chapters

1. **Introduction** - Who this book is for, how to use it, and comparison with existing textbooks
2. **Flowcharts** - Three complementary decision workflows
   - General: Complete econometric workflow from data to deployment
   - Purpose-Based: Organized by goal (forecasting, causal analysis, etc.)
   - Representation-Based: Organized by domain (time, frequency, state-space, etc.)
3. **Data Preparation** - Cleaning, sampling, missing data, outliers
4. **Exploratory Analysis** - Distributions, stationarity, ACF/PACF
5. **Frequency Domain** - Spectral analysis, FFT, periodicities, filtering
6. **Modelling** - ARIMA, VAR, GARCH, state-space, ML approaches
7. **Feature Extraction** - Engineering features for machine learning
8. **Validation & Deployment** - Testing, monitoring, production systems

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Basic knowledge of statistics, linear algebra, and Python

### Installation

\`\`\`bash
# Clone the repository
git clone https://github.com/yourusername/time-series-analysis-manual.git
cd time-series-analysis-manual

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
\`\`\`

### Local Development

\`\`\`bash
# Serve documentation locally
mkdocs serve

# Open browser to http://127.0.0.1:8000
\`\`\`

### Building

\`\`\`bash
# Build static site
mkdocs build
\`\`\`

---

## 📖 How to Use

Visit the live documentation at: **[https://yourusername.github.io/time-series-analysis-manual](https://yourusername.github.io/time-series-analysis-manual)**

Or build locally and explore the `code/` directory for standalone examples.

---

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

---

## 📜 License

Documentation: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)  
Code: [MIT License](LICENSE-CODE)

---

**[Read Online](https://yourusername.github.io/time-series-analysis-manual)** | **[Get Started](docs/00-introduction/overview.md)**
