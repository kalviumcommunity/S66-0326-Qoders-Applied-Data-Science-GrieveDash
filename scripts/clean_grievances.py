"""Clean municipal grievance CSV data from raw to processed."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

try:
    import pandas as pd
except ModuleNotFoundError:  # pragma: no cover
    pd = None


EXPECTED_COLUMNS = [
    "complaint_id",
    "date",
    "location",
    "issue_type",
    "status",
    "priority",
    "resolution_time",
]


def _normalize_status(value: str) -> str:
    if value is None:
        return "pending"
    cleaned = value.strip().lower()
    if cleaned in {"in progress", "in-progress"}:
        cleaned = "in_progress"
    if cleaned not in {"pending", "in_progress", "resolved"}:
        return "pending"
    return cleaned


def _normalize_priority(value: str) -> str:
    if value is None:
        return "medium"
    cleaned = value.strip().lower()
    if cleaned not in {"low", "medium", "high"}:
        return "medium"
    return cleaned


def clean_grievances(df: "pd.DataFrame") -> "pd.DataFrame":
    """Apply data cleaning rules and return a cleaned copy."""
    cleaned = df.copy()

    missing_cols = [col for col in EXPECTED_COLUMNS if col not in cleaned.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {', '.join(missing_cols)}")

    cleaned = cleaned[EXPECTED_COLUMNS]

    cleaned["complaint_id"] = pd.to_numeric(cleaned["complaint_id"], errors="coerce")
    cleaned["resolution_time"] = pd.to_numeric(cleaned["resolution_time"], errors="coerce")

    cleaned["date"] = pd.to_datetime(cleaned["date"], errors="coerce")

    for col in ["location", "issue_type", "status", "priority"]:
        cleaned[col] = cleaned[col].astype("string").str.strip().str.lower()

    cleaned["status"] = cleaned["status"].map(_normalize_status)
    cleaned["priority"] = cleaned["priority"].map(_normalize_priority)

    cleaned = cleaned.dropna(subset=["complaint_id", "date", "location", "issue_type"])
    cleaned["complaint_id"] = cleaned["complaint_id"].astype(int)

    cleaned["resolution_time"] = cleaned["resolution_time"].fillna(0).clip(lower=0)
    cleaned.loc[cleaned["status"] != "resolved", "resolution_time"] = 0
    cleaned["resolution_time"] = cleaned["resolution_time"].round().astype(int)

    cleaned = cleaned.drop_duplicates(subset=["complaint_id"], keep="last")
    cleaned = cleaned.sort_values(["date", "complaint_id"]).reset_index(drop=True)
    cleaned["date"] = cleaned["date"].dt.strftime("%Y-%m-%d")
    return cleaned


def clean_grievances_without_pandas(input_path: Path, output_path: Path) -> tuple[int, int]:
    with input_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing_cols = [col for col in EXPECTED_COLUMNS if col not in reader.fieldnames]
        if missing_cols:
            raise ValueError(f"Missing required columns: {', '.join(missing_cols)}")

        rows = list(reader)

    deduped: dict[int, dict[str, str]] = {}
    for row in rows:
        try:
            complaint_id = int(float((row.get("complaint_id") or "").strip()))
        except ValueError:
            continue

        date_str = (row.get("date") or "").strip()
        if len(date_str) != 10:
            continue

        location = (row.get("location") or "").strip().lower()
        issue_type = (row.get("issue_type") or "").strip().lower()
        if not location or not issue_type:
            continue

        try:
            resolution_time = int(round(float((row.get("resolution_time") or "0").strip())))
        except ValueError:
            resolution_time = 0
        if resolution_time < 0:
            resolution_time = 0

        status = _normalize_status(row.get("status"))
        priority = _normalize_priority(row.get("priority"))
        if status != "resolved":
            resolution_time = 0

        deduped[complaint_id] = {
            "complaint_id": complaint_id,
            "date": date_str,
            "location": location,
            "issue_type": issue_type,
            "status": status,
            "priority": priority,
            "resolution_time": resolution_time,
        }

    cleaned_rows = sorted(deduped.values(), key=lambda r: (r["date"], r["complaint_id"]))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=EXPECTED_COLUMNS)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    return len(rows), len(cleaned_rows)


def run(input_path: Path, output_path: Path) -> None:
    if pd is not None:
        df = pd.read_csv(input_path)
        cleaned = clean_grievances(df)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        cleaned.to_csv(output_path, index=False)

        input_rows, output_rows = len(df), len(cleaned)
    else:
        print("Warning: pandas is not installed; using CSV fallback cleaner.")
        input_rows, output_rows = clean_grievances_without_pandas(input_path, output_path)

    print(f"Input rows : {input_rows}")
    print(f"Output rows: {output_rows}")
    print(f"Saved cleaned CSV to {output_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean grievance CSV data")
    parser.add_argument(
        "--input",
        default="municipal_grievance_full_200.csv",
        help="Path to raw input CSV",
    )
    parser.add_argument(
        "--output",
        default="data/processed/municipal_grievance_full_200_cleaned.csv",
        help="Path to cleaned output CSV",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run(Path(args.input), Path(args.output))
