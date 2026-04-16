"""Milestone demo: computing basic summary statistics for individual columns in DataFrames."""

from pathlib import Path

import pandas as pd


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        # Fallback dummy data
        data = {
            "ID": range(1, 6),
            "Score": [85, 90, 78, 92, 88],
            "Category": ["A", "B", "A", "C", "B"]
        }
        return pd.DataFrame(data)
    return pd.read_csv(csv_path)


def compute_numeric_stats(df: pd.DataFrame) -> None:
    print("\n1) Basic Numeric Statistics")
    
    # In our raw data, ComplaintID is numeric
    target_col = 'ComplaintID'
    if target_col in df.columns:
        print(f"\nStatistics for '{target_col}':")
        print(f"Mean:   {df[target_col].mean():.2f}")
        print(f"Median: {df[target_col].median()}")
        print(f"Std Dev:{df[target_col].std():.2f}")
        print(f"Min:    {df[target_col].min()}")
        print(f"Max:    {df[target_col].max()}")
        print(f"Sum:    {df[target_col].sum()}")
        print(f"Count:  {df[target_col].count()}")


def compute_categorical_stats(df: pd.DataFrame) -> None:
    print("\n2) Categorical/Frequency Statistics")
    
    # In our raw data, ComplaintType and Status are categorical
    target_col = 'ComplaintType'
    if target_col in df.columns:
        print(f"\nStatistics for '{target_col}':")
        print(f"Unique values:   {df[target_col].unique()}")
        print(f"Number of unique: {df[target_col].nunique()}")
        print("\nValue Counts (Frequency):")
        print(df[target_col].value_counts())


def run_demo() -> None:
    df = load_dataframe()
    
    compute_numeric_stats(df)
    compute_categorical_stats(df)


if __name__ == "__main__":
    run_demo()
