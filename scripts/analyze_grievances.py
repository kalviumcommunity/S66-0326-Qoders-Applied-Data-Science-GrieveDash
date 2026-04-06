"""
GrieveDash — First Python Data Analysis Script
================================================
This standalone script performs simple data analysis on the sample
grievance dataset. It demonstrates that Python scripts execute
top-to-bottom, produce consistent terminal output, and are ideal
for repeatable, automation-friendly workflows.

Usage:
    python scripts/analyze_grievances.py
"""

import csv
import os
from collections import Counter

# ─────────────────────────────────────────────
# 1. CONFIGURATION
# ─────────────────────────────────────────────
RAW_DATA_PATH = "data/raw/grievances_raw.csv"

SEPARATOR = "=" * 55

# ─────────────────────────────────────────────
# 2. LOAD RAW DATA
# ─────────────────────────────────────────────
def load_data(filepath):
    """Read a CSV file and return a list of row dictionaries."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Raw data not found at: {filepath}\n"
            "Run scripts/generate_dummy_data.py first."
        )
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


# ─────────────────────────────────────────────
# 3. ANALYSIS FUNCTIONS
# ─────────────────────────────────────────────
def count_by_field(records, field):
    """Return a sorted Counter for a given field across all records."""
    return Counter(row[field] for row in records)


def resolution_rate(records):
    """Calculate the percentage of complaints with status 'closed'."""
    total = len(records)
    closed = sum(1 for r in records if r["status"] == "closed")
    return round((closed / total) * 100, 1) if total else 0


# ─────────────────────────────────────────────
# 4. PRINT REPORT
# ─────────────────────────────────────────────
def print_report(records):
    """Print a formatted analysis report to the terminal."""
    print(SEPARATOR)
    print("  GrieveDash — Grievance Analysis Report")
    print(SEPARATOR)

    print(f"\n📋 Total Complaints : {len(records)}")

    print("\n📊 Complaints by Category:")
    for category, count in count_by_field(records, "category").most_common():
        bar = "█" * count
        print(f"   {category:<15} {bar}  ({count})")

    print("\n📊 Complaints by Status:")
    for status, count in count_by_field(records, "status").most_common():
        bar = "█" * count
        print(f"   {status:<15} {bar}  ({count})")

    rate = resolution_rate(records)
    print(f"\n✅ Resolution Rate  : {rate}%")

    print("\n" + SEPARATOR)
    print("  Script completed successfully — top to bottom.")
    print(SEPARATOR)


# ─────────────────────────────────────────────
# 5. ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    records = load_data(RAW_DATA_PATH)
    print_report(records)
