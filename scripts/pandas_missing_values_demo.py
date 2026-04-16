"""Milestone demo: detecting missing values in DataFrames."""

from pathlib import Path

import pandas as pd


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        # Fallback to creating a dummy dataframe with missing values if CSV is missing or for demo
        data = {
            "A": [1, 2, None, 4],
            "B": [None, 6, 7, 8],
            "C": [9, 10, 11, 12]
        }
        return pd.DataFrame(data)
    return pd.read_csv(csv_path)


def detect_missing_values(df: pd.DataFrame) -> None:
    print("\n1) Detecting Missing Values (isnull / isna)")
    print("\nBoolean mask (first 5 rows):")
    print(df.isnull().head())

    print("\n2) Counting Missing Values per Column")
    print(df.isnull().sum())

    print("\n3) Checking if any Missing Values exist per Column")
    print(df.isnull().any())

    print("\n4) Total count of Missing Values in DataFrame")
    print(df.isnull().sum().sum())

    print("\n5) Detecting Non-Missing Values (notnull / notna)")
    print(df.notnull().head())


def run_demo() -> None:
    df = load_dataframe()
    print(f"DataFrame Shape: {df.shape}")
    print("\nColumn Data Types:")
    print(df.dtypes)
    
    detect_missing_values(df)


if __name__ == "__main__":
    run_demo()
