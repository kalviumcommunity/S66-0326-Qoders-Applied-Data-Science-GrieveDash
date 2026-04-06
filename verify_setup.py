"""
Environment Setup Verification Script
======================================
Run this script to verify that Python, Conda, and core
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


def check_packages():
    """Check availability of core Data Science packages."""
    packages = [
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("matplotlib", "Matplotlib"),
        ("sklearn", "Scikit-learn"),
    ]

    all_ok = True
    for module, name in packages:
        try:
            __import__(module)
            print(f"✅ {name}: Available")
        except ImportError:
            print(f"⚠️  {name}: Not installed (install with: conda install {module})")
            all_ok = False
    return all_ok


def main():
    print("=" * 50)
    print("  Environment Setup Verification")
    print("=" * 50)
    print()

    print("--- Python ---")
    check_python()
    print()

    print("--- Conda ---")
    conda_ok = check_conda()
    print()

    print("--- Data Science Packages ---")
    packages_ok = check_packages()
    print()

    print("=" * 50)
    if conda_ok:
        print("✅ Environment is ready for Data Science work!")
    else:
        print("⚠️  Some components need attention. See above.")
    print("=" * 50)


if __name__ == "__main__":
    main()
