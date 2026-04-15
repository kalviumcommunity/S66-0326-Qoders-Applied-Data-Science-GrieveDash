"""Milestone demo: inspecting DataFrames with head(), info(), and describe()."""

from pathlib import Path

import pandas as pd


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    return pd.read_csv(csv_path)


def inspect_with_head(df: pd.DataFrame) -> None:
    print("\n1) head() preview")
    print(df.head())
    print("\nhead(3):")
    print(df.head(3))


def inspect_with_info(df: pd.DataFrame) -> None:
    print("\n2) info() structure")
    df.info()


def inspect_with_describe(df: pd.DataFrame) -> None:
    print("\n3) describe() numeric summary")
    print(df.describe())

    print("\nOptional: include all columns")
    print(df.describe(include="all"))


def run_demo() -> None:
    df = load_dataframe()
    inspect_with_head(df)
    inspect_with_info(df)
    inspect_with_describe(df)


if __name__ == "__main__":
    run_demo()
