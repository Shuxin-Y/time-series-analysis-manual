# Appendix C: Python Environment Setup

This guide will help you set up a Python environment to run all code examples in this book.

---

## Prerequisites

- **Python 3.9 or higher** (3.10 or 3.11 recommended)
- **pip** (Python package manager, included with Python)
- **Git** (for cloning the repository)

---

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/time-series-analysis-manual.git
cd time-series-analysis-manual
```

### 2. Create Virtual Environment

**Why?** Isolates dependencies, prevents conflicts with other projects.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs all required packages (numpy, pandas, statsmodels, etc.).

**Installation time**: 5-10 minutes depending on connection speed.

### 4. Verify Installation

```bash
python -c "import numpy, pandas, statsmodels, matplotlib; print('All imports successful!')"
```

If you see `All imports successful!`, you're ready!

---

## Using Jupyter Notebooks

### Launch Jupyter

```bash
jupyter notebook
```

This opens Jupyter in your browser at `http://localhost:8888`.

### Navigate to Code Examples

In Jupyter interface:
1. Click on `code-examples/`
2. Click on `notebooks/`
3. Open any `.ipynb` file (e.g., `04_stationarity.ipynb`)

### Running Notebooks

- **Shift + Enter**: Run current cell and move to next
- **Ctrl + Enter**: Run current cell, stay on it
- **Cell → Run All**: Run entire notebook

---

## Package Overview

### Core Libraries

| Package | Purpose | Used For |
|---------|---------|----------|
| **numpy** | Numerical arrays | Data manipulation, linear algebra |
| **pandas** | DataFrames | Time series data structures, resampling |
| **scipy** | Scientific functions | FFT, signal processing, optimization |
| **statsmodels** | Statistical models | ARIMA, VAR, VECM, statistical tests |
| **arch** | Volatility models | GARCH, EGARCH, GJR-GARCH |
| **matplotlib** | Plotting | Time series plots, ACF/PACF |
| **seaborn** | Statistical plots | Distribution plots, heatmaps |

### Testing Imports

<details>
<summary><b>💻 Click to see comprehensive import test script</b></summary>

```python
import sys

def test_imports():
    """Test all required packages"""
    packages = {
        'numpy': 'Numerical computing',
        'pandas': 'Data structures',
        'scipy': 'Scientific computing',
        'statsmodels': 'Time series models',
        'arch': 'GARCH models',
        'sklearn': 'Machine learning',
        'xgboost': 'Gradient boosting',
        'matplotlib': 'Plotting',
        'seaborn': 'Statistical plots',
    }

    print("Testing package imports...\n")
    print(f"Python version: {sys.version}\n")

    failed = []
    for package, description in packages.items():
        try:
            __import__(package)
            print(f"✓ {package:20s} - {description}")
        except ImportError as e:
            print(f"✗ {package:20s} - {description} (FAILED)")
            failed.append((package, str(e)))

    if failed:
        print(f"\n{len(failed)} package(s) failed to import:")
        for pkg, error in failed:
            print(f"  - {pkg}: {error}")
        print("\nRun: pip install -r requirements.txt")
    else:
        print("\n✓ All packages imported successfully!")
        print("You're ready to start!")

if __name__ == '__main__':
    test_imports()
```

Save as `test_environment.py` and run:
```bash
python test_environment.py
```

</details>

---

## Troubleshooting

### Issue: `ModuleNotFoundError`

**Problem**: Package not installed

**Solution**:
```bash
pip install <package-name>
```

Or reinstall all:
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: Version Conflicts

**Problem**: Incompatible package versions

**Solution**: Create fresh environment:
```bash
deactivate  # Exit current venv
rm -rf venv  # Delete old environment
python3 -m venv venv  # Create new
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: Jupyter Kernel Not Found

**Problem**: Virtual environment not registered with Jupyter

**Solution**:
```bash
python -m ipykernel install --user --name=ts-analysis --display-name="Time Series Analysis"
```

Then in Jupyter: **Kernel → Change Kernel → Time Series Analysis**

### Issue: matplotlib Plots Not Showing

**Problem**: Backend not configured

**Solution**: Add to notebook:
```python
%matplotlib inline
import matplotlib.pyplot as plt
```

### Issue: Slow Installation

**Problem**: Downloading large packages

**Solutions**:
1. Use a better mirror:
   ```bash
   pip install -r requirements.txt -i https://pypi.org/simple
   ```
2. Install without deep learning (faster):
   ```bash
   # Edit requirements.txt and comment out torch/tensorflow lines
   pip install -r requirements.txt
   ```

---

## Alternative: Using Conda

If you prefer Conda over pip:

### Install Miniconda

Download from: https://docs.conda.io/en/latest/miniconda.html

### Create Environment

```bash
conda create -n ts-analysis python=3.11
conda activate ts-analysis
```

### Install Packages

```bash
conda install numpy pandas scipy matplotlib seaborn jupyter
conda install -c conda-forge statsmodels arch scikit-learn xgboost
```

---

## Using Google Colab (No Installation)

**For cloud-based execution:**

1. Go to https://colab.research.google.com
2. **File → Open Notebook → GitHub**
3. Enter: `yourusername/time-series-analysis-manual`
4. Select a notebook from `code-examples/notebooks/`

**Install packages in Colab**:
```python
!pip install statsmodels arch
```

**Pros**: No local installation, free GPU
**Cons**: Files not persistent, slower for small tasks

---

## IDE Recommendations

### 1. VS Code (Recommended)
- Install: https://code.visualstudio.com/
- Extensions:
  - Python (Microsoft)
  - Jupyter (Microsoft)
  - Pylance (Microsoft)

### 2. PyCharm
- Community Edition: https://www.jetbrains.com/pycharm/
- Built-in Jupyter support
- Great debugging

### 3. JupyterLab
- Enhanced Jupyter interface
- Install: `pip install jupyterlab`
- Run: `jupyter lab`

---

## Dataset Setup

Some examples use real datasets. Download them:

```bash
cd code-examples/datasets
# Scripts will be provided to download sample data
python download_datasets.py
```

Or manually download from [Appendix D: Datasets](D-datasets-and-resources.md).

---

## Updating Dependencies

### Check for Updates

```bash
pip list --outdated
```

### Update Specific Package

```bash
pip install --upgrade <package-name>
```

### Update All Packages

```bash
pip install --upgrade -r requirements.txt
```

**Warning**: Major updates may break compatibility. Test after updating.

---

## Uninstalling

When done with the environment:

```bash
deactivate  # Exit virtual environment
rm -rf venv  # Delete environment folder
```

---

## Summary

**Quick start command sequence:**
```bash
# Clone, setup, and run
git clone https://github.com/yourusername/time-series-analysis-manual.git
cd time-series-analysis-manual
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
jupyter notebook
```

**You're all set!** Proceed to [Chapter 1: Master Flowchart](../01-master-flowchart/flowchart.md) or start with [code examples](../code-examples/notebooks/).

---

**[Back to Contents](../README.md)** | **[Next: Datasets →](D-datasets-and-resources.md)**
