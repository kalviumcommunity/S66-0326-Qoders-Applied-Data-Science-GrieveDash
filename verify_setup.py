"""
Environment Setup Verification Script
======================================
Run this script to verify that Python, Conda, Jupyter, and core
Data Science packages are properly installed and accessible.

Usage:
    python verify_setup.py
"""

import sys
import shutil
import subprocess


def check_python():
    """Verify Python version."""
    version = sys.version
    print(f"✅ Python Version: {version.split()[0]}")
    print(f"   Path: {sys.executable}")
    return True


def check_conda():
    """Verify Conda is accessible."""
    conda_path = shutil.which("conda")
    if conda_path:
        result = subprocess.run(
            ["conda", "--version"], capture_output=True, text=True
        )
        version = result.stdout.strip()
        print(f"✅ Conda: {version}")
        print(f"   Path: {conda_path}")
        return True
    else:
        print("❌ Conda: Not found in PATH")
        return False


def check_jupyter():
    """Verify Jupyter is installed and accessible."""
    jupyter_path = shutil.which("jupyter")
    if jupyter_path:
        result = subprocess.run(
            ["jupyter", "notebook", "--version"], capture_output=True, text=True
        )
        version = result.stdout.strip()
        print(f"✅ Jupyter Notebook: v{version}")
        print(f"   Path: {jupyter_path}")

        # Also check JupyterLab
        result_lab = subprocess.run(
            ["jupyter", "lab", "--version"], capture_output=True, text=True
        )
        lab_version = result_lab.stdout.strip()
        if lab_version:
            print(f"✅ JupyterLab: v{lab_version}")

        return True
    else:
        print("❌ Jupyter: Not found in PATH")
        print("   Install with: conda install jupyter notebook")
        return False


def check_packages():
    """Check availability of core Data Science packages."""
    packages = [
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("matplotlib", "Matplotlib"),
        ("seaborn", "Seaborn"),
        ("sklearn", "Scikit-learn"),
    ]

    all_ok = True
    for module, name in packages:
        try:
            mod = __import__(module)
            version = getattr(mod, "__version__", "unknown")
            print(f"✅ {name}: v{version}")
        except ImportError:
            print(f"⚠️  {name}: Not installed (install with: conda install {module})")
            all_ok = False
    return all_ok


def main():
    print("=" * 55)
    print("  GrieveDash — Environment Setup Verification")
    print("=" * 55)
    print()

    print("--- Python ---")
    check_python()
    print()

    print("--- Conda ---")
    conda_ok = check_conda()
    print()

    print("--- Jupyter ---")
    jupyter_ok = check_jupyter()
    print()

    print("--- Data Science Packages ---")
    packages_ok = check_packages()
    print()

    print("=" * 55)
    all_ok = conda_ok and jupyter_ok and packages_ok
    if all_ok:
        print("✅ Environment is fully ready for Data Science work!")
    else:
        print("⚠️  Some components need attention. See above.")
    print("=" * 55)


if __name__ == "__main__":
    main()
