"""Milestone demo: comparing distributions across multiple columns in DataFrames."""

from pathlib import Path

import pandas as pd


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        # Fallback dummy data
        data = {
            "Region": ["North", "South", "North", "East", "South", "North"],
            "Category": ["A", "B", "A", "C", "B", "A"],
            "Score_V1": [85, 90, 78, 92, 88, 82],
            "Score_V2": [80, 85, 82, 90, 85, 79]
        }
        return pd.DataFrame(data)
    return pd.read_csv(csv_path)


def compare_numeric_distributions(df: pd.DataFrame) -> None:
    print("\n1) Comparing Numeric Distributions")
    
    # Selecting multiple numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if len(numeric_cols) >= 2:
        print(f"\nSummary statistics for {numeric_cols}:")
        print(df[numeric_cols].describe())


def compare_categorical_distributions(df: pd.DataFrame) -> None:
    print("\n2) Comparing Categorical Distributions")
    
    # In our raw data, ComplaintType and Status
    cat_cols = ['ComplaintType', 'Status']
    # Filter only those that exist
    cat_cols = [col for col in cat_cols if col in df.columns]
    
    for col in cat_cols:
        print(f"\nFrequency distribution for '{col}':")
        # Normalize=True gives proportions (relative frequency)
        print(df[col].value_counts(normalize=True))


def compare_with_groupby(df: pd.DataFrame) -> None:
    print("\n3) Comparing Distributions using GroupBy")
    
    # Compare Status distribution across different ComplaintTypes
    if 'ComplaintType' in df.columns and 'Status' in df.columns:
        print("\nCross-tabulation of ComplaintType vs Status:")
        print(pd.crosstab(df['ComplaintType'], df['Status']))
        
        print("\nRelative frequency of Status within each ComplaintType:")
        print(pd.crosstab(df['ComplaintType'], df['Status'], normalize='index'))


def run_demo() -> None:
    df = load_dataframe()
    
    compare_numeric_distributions(df)
    compare_categorical_distributions(df)
    compare_with_groupby(df)


if __name__ == "__main__":
    run_demo()
