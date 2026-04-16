"""Milestone demo: selecting rows and columns using indexing and slicing."""

from pathlib import Path

import pandas as pd


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    return pd.read_csv(csv_path)


def select_columns(df: pd.DataFrame) -> None:
    print("\n1) Column Selection")
    print("\nSingle column (as Series):")
    print(df["ComplaintType"].head())

    print("\nMultiple columns (as DataFrame):")
    print(df[["ComplaintType", "Status"]].head())


def select_rows_slicing(df: pd.DataFrame) -> None:
    print("\n2) Row Slicing")
    print("\nRows 0 to 4:")
    print(df[0:5])


def select_with_iloc(df: pd.DataFrame) -> None:
    print("\n3) Selection using .iloc (Position-based)")
    print("\nFirst 3 rows, first 2 columns:")
    print(df.iloc[0:3, 0:2])

    print("\nSpecific row (index 10):")
    print(df.iloc[10])


def select_with_loc(df: pd.DataFrame) -> None:
    print("\n4) Selection using .loc (Label-based)")
    # Since our index is default integer, labels match positions for rows
    print("\nRows with labels 0 to 2, specific columns:")
    print(df.loc[0:2, ["ComplaintType", "Status"]])


def run_demo() -> None:
    df = load_dataframe()
    select_columns(df)
    select_rows_slicing(df)
    select_with_iloc(df)
    select_with_loc(df)


if __name__ == "__main__":
    run_demo()
