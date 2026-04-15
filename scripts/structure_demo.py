"""Milestone demo: structuring Python code for readability and reuse."""

from typing import List


# -----------------------------
# Configuration
# -----------------------------
DEFAULT_STATUSES = ["pending", "in_progress", "resolved"]


# -----------------------------
# Helper functions
# -----------------------------
def normalize_status(status: str) -> str:
    cleaned = status.strip().lower()
    if cleaned in {"in progress", "in-progress"}:
        return "in_progress"
    if cleaned not in DEFAULT_STATUSES:
        return "pending"
    return cleaned


def count_by_value(values: List[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


def format_report(counts: dict[str, int]) -> List[str]:
    lines = []
    for key, count in counts.items():
        lines.append(f"{key}: {count}")
    return lines


# -----------------------------
# Core logic
# -----------------------------
def build_status_report(raw_statuses: List[str]) -> List[str]:
    normalized = [normalize_status(status) for status in raw_statuses]
    counts = count_by_value(normalized)
    return format_report(counts)


# -----------------------------
# Execution
# -----------------------------
def run_demo() -> None:
    raw_statuses = [
        "Pending",
        "Resolved",
        "In-Progress",
        "resolved",
        "pending",
    ]

    report_lines = build_status_report(raw_statuses)

    print("\nStructured Status Report")
    for line in report_lines:
        print(line)


if __name__ == "__main__":
    run_demo()
