# S66-0326-Qoders-Applied-Data-Science-GrieveDash

## GrieveDash — Applied Data Science Project

A Data Science project built as part of the Applied Data Science sprint.

---

## 🖥️ Local Environment Setup

### System Information

| Item                | Details                          |
|---------------------|----------------------------------|
| **Operating System**| macOS (Apple Silicon / ARM64)    |
| **Python Version**  | 3.13.12 (via Miniconda)          |
| **Conda Version**   | 26.1.1                           |
| **Installer**       | Miniconda3 (latest, macOS ARM64) |

---

### Installation Steps

#### 1. Install Miniconda

Downloaded and installed **Miniconda** (a minimal Conda installer) using the terminal:

```bash
# Download the Miniconda installer for macOS ARM64
curl -fsSL https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o /tmp/miniconda.sh

# Run the installer in batch (non-interactive) mode
bash /tmp/miniconda.sh -b -p $HOME/miniconda3

# Initialize Conda for the shell
~/miniconda3/bin/conda init zsh
```

After running `conda init`, restart the terminal or run `source ~/.zshrc` for changes to take effect.

#### 2. Verify Installations

```bash
# Check Python version
python --version
# Output: Python 3.13.12

# Check Conda version
conda --version
# Output: conda 26.1.1

# View Conda environment info
conda info
```

#### 3. Create a Project Environment (Optional)

```bash
# Create a new environment from the provided environment.yml
conda env create -f environment.yml

# Activate the environment
conda activate grievedash

# Verify the environment is active
conda info --envs
```

---

### Verification Results

```
$ python --version
Python 3.13.12

$ conda --version
conda 26.1.1

$ conda info --envs
# conda environments:
base                  *  /Users/apple/miniconda3
```

Python and Conda are installed, accessible from the terminal, and the base environment activates correctly. The system is ready for Data Science workflows including notebooks, scripts, ML models, and Streamlit apps.

---

### Environment Reproducibility

An `environment.yml` file is included in this repository to ensure consistent environments across team members. Use it to recreate the exact same environment:

```bash
conda env create -f environment.yml
conda activate grievedash
```

This helps prevent "works on my machine" issues during collaborative development.

---

### Verification Script

A `verify_setup.py` script is included to quickly validate that the environment is properly configured:

```bash
python verify_setup.py
```

This script checks Python version, Conda availability, Jupyter installation, and key Data Science package imports.

---

## ✅ Milestone 2 — Verify Python, Conda & Jupyter

### Python Verification

Python 3.13.12 is installed via Miniconda and accessible from the terminal.

```
$ python --version
Python 3.13.12

$ python -c "import sys; print(sys.executable)"
/Users/apple/miniconda3/bin/python
```

**REPL commands verified:**
- Arithmetic operations (`2 + 3`, `10 / 3`)
- String manipulation (`upper()`, `len()`, f-strings)
- List comprehensions (`[x**2 for x in range(1, 6)]`)

---

### Conda Verification

Conda 26.1.1 is installed and managing environments correctly.

```
$ conda --version
conda 26.1.1

$ conda info --envs
# conda environments:
#  * -> active
base                  *  /Users/apple/miniconda3

$ conda activate base
# Environment activated successfully
```

---

### Jupyter Verification

Jupyter Notebook and JupyterLab are installed and launchable.

```
$ jupyter notebook --version
7.5.5

$ jupyter lab --version
4.5.6

$ jupyter --version
Selected Jupyter core packages...
IPython          : 9.11.0
ipykernel        : 7.2.0
ipywidgets       : 8.1.7
jupyter_client   : 8.8.0
jupyter_core     : 5.9.1
jupyter_server   : 2.17.0
jupyterlab       : 4.5.6
nbclient         : 0.10.4
nbconvert        : 7.17.0
nbformat         : 5.10.4
notebook         : 7.5.5
qtconsole        : 5.7.1
traitlets        : 5.14.3
```

To launch Jupyter Notebook:

```bash
jupyter notebook
```

To launch JupyterLab:

```bash
jupyter lab
```

---

### Data Science Packages

All core libraries are installed and verified:

| Package       | Version  | Status |
|---------------|----------|--------|
| NumPy         | 2.4.4    | ✅     |
| Pandas        | 3.0.1    | ✅     |
| Matplotlib    | 3.10.8   | ✅     |
| Seaborn       | 0.13.2   | ✅     |
| Scikit-learn  | 1.8.0    | ✅     |

---

### Proof-of-Work Notebook

A `proof_of_work.ipynb` notebook is included in this repository that demonstrates:

1. **Python verification** — version info and REPL commands
2. **Conda verification** — version and environment listing
3. **Jupyter verification** — running inside a live notebook
4. **Library imports** — NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
5. **Sample data analysis** — Pandas DataFrame with sample grievance data
6. **Visualization** — Bar chart using Matplotlib comparing complaints vs resolved

---

### Full Verification Script Output

```
=======================================================
  GrieveDash — Environment Setup Verification
=======================================================

--- Python ---
✅ Python Version: 3.13.12
   Path: /Users/apple/miniconda3/bin/python

--- Conda ---
✅ Conda: conda 26.1.1
   Path: /Users/apple/miniconda3/bin/conda

--- Jupyter ---
✅ Jupyter Notebook: v7.5.5
   Path: /Users/apple/miniconda3/bin/jupyter
✅ JupyterLab: v4.5.6

--- Data Science Packages ---
✅ NumPy: v2.4.4
✅ Pandas: v3.0.1
✅ Matplotlib: v3.10.8
✅ Seaborn: v0.13.2
✅ Scikit-learn: v1.8.0

=======================================================
✅ Environment is fully ready for Data Science work!
=======================================================
```

---

## 📁 Project Folder Structure

A standard Data Science directory structure has been implemented to separate concerns, keep the workspace clean, and ensure reproducibility.

```text
S66-0326-Qoders-Applied-Data-Science-GrieveDash/
│
├── data/
│   ├── raw/             # Immutable raw datasets (DO NOT EDIT)
│   └── processed/       # Cleaned and transformed datasets
│
├── notebooks/           # Jupyter notebooks for exploration and analysis
│   ├── proof_of_work.ipynb
│   └── ...
│
├── scripts/             # Standalone Python scripts (.py)
│   ├── verify_setup.py
│   └── ...
│
├── outputs/             # Generated charts, reports, and models
│
├── environment.yml      # Conda environment definition
└── README.md            # Project documentation
```

### Folder Roles
- **`data/raw/`**: The absolute source of truth. Raw data is placed here and is treated as read-only to prevent accidental corruption.
- **`data/processed/`**: Intermediate or finalized clean data that is ready for analysis and modeling.
- **`notebooks/`**: Exploratory Data Analysis (EDA), model training, and visual documentation.
- **`scripts/`**: Reusable utility functions and production code.
- **`outputs/`**: Final artifacts like generated visualizations and trained model binaries.

---

## ✅ Milestone — Conditional Statements for Data Logic

Run the milestone demo script:

```bash
python scripts/conditional_logic_demo.py
```

This script includes:
- Basic `if`
- `if-else`
- `if-elif-else`
- Logical operators (`and`, `or`, `not`)

---

## ✅ Milestone — Loops for Iterative Data Processing

Run the milestone demo script:

```bash
python scripts/loops_demo.py
```

This script includes:
- `for` loops over range and list
- `while` loop with a condition
- `break` and `continue`
- Infinite-loop prevention

---

## ✅ Milestone — Defining and Calling Python Functions

Run the milestone demo script:

```bash
python scripts/functions_demo.py
```

This script includes:
- Defining functions with `def`
- Calling functions and passing arguments
- Parameters and return values
- Basic function scope behavior

---

## 📓 Sprint Notebooks Overview

All proof-of-work notebooks are stored in the `notebooks/` folder:

| Notebook | Topic | Status |
|---|---|---|
| `proof_of_work.ipynb` | Python, Conda & Jupyter verification | ✅ |
| `workspace_navigation_proof.ipynb` | Jupyter Home interface navigation | ✅ |
| `code_vs_markdown_proof.ipynb` | Code vs Markdown cell usage | ✅ |
| `kernel_control_proof.ipynb` | Running, restarting, interrupting kernels | ✅ |
| `markdown_formatting_proof.ipynb` | Headings, lists, and code blocks in Markdown | ✅ |
| `python_data_types.ipynb` | Numeric and string data types | ✅ |
| `python_collections.ipynb` | Lists, tuples, and dictionaries | ✅ |
