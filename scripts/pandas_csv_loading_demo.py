"""Milestone demo: loading CSV data into Pandas DataFrames."""

from pathlib import Path

import pandas as pd


EXPECTED_COLUMNS = {
    "complaint_id",
    "date",
    "location",
    "issue_type",
    "status",
    "priority",
    "resolution_time",
}


def load_csv(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    return pd.read_csv(csv_path)


def inspect_dataframe(df: pd.DataFrame) -> None:
    print("\n1) Preview loaded data")
    print(df.head(5))

    print("\n2) Structure checks")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(df.dtypes)

    print("\n3) Row count")
    print(f"Total rows: {len(df)}")


def check_common_loading_issues(df: pd.DataFrame) -> None:
    loaded_columns = set(df.columns)

    missing_columns = sorted(EXPECTED_COLUMNS - loaded_columns)
    extra_columns = sorted(loaded_columns - EXPECTED_COLUMNS)

    print("\n4) Common loading issue checks")
    if missing_columns:
        print(f"Missing expected columns: {missing_columns}")
    else:
        print("Missing expected columns: none")

    if extra_columns:
        print(f"Extra columns detected: {extra_columns}")
    else:
        print("Extra columns detected: none")


def run_demo() -> None:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    df = load_csv(csv_path)
    inspect_dataframe(df)
    check_common_loading_issues(df)


if __name__ == "__main__":
    run_demo()
