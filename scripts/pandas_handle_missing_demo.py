"""Milestone demo: handling missing values with drop and fill strategies."""

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


def handle_missing_drop(df: pd.DataFrame) -> None:
    print("\n1) Dropping Missing Values (dropna)")
    
    print("\nDrop rows with ANY missing values:")
    df_dropped_any = df.dropna()
    print(f"Original shape: {df.shape}, New shape: {df_dropped_any.shape}")

    print("\nDrop columns with ANY missing values:")
    df_dropped_cols = df.dropna(axis=1)
    print(f"Original columns count: {len(df.columns)}, New columns count: {len(df_dropped_cols.columns)}")


def handle_missing_fill(df: pd.DataFrame) -> None:
    print("\n2) Filling Missing Values (fillna)")

    print("\nFill all missing values with a constant (e.g., 0 or 'Unknown'):")
    df_filled_constant = df.fillna(0)
    print(df_filled_constant.head())

    print("\nFill specific columns with different values:")
    # For demo, let's assume we want to fill numeric with 0 and strings with "N/A"
    # We'll use a copy to avoid warnings
    df_filled_spec = df.copy()
    for col in df_filled_spec.columns:
        if df_filled_spec[col].dtype == 'object':
            df_filled_spec[col] = df_filled_spec[col].fillna("N/A")
        else:
            df_filled_spec[col] = df_filled_spec[col].fillna(0)
    print(df_filled_spec.head())


def run_demo() -> None:
    df = load_dataframe()
    print(f"Initial Missing Values Count:\n{df.isnull().sum()}")
    
    handle_missing_drop(df)
    handle_missing_fill(df)


if __name__ == "__main__":
    run_demo()
