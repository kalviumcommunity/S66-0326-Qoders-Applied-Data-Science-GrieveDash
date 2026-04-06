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

This script checks Python version, Conda availability, and key Data Science package imports.
