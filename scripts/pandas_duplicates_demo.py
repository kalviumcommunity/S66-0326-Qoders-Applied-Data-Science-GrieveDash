"""Milestone demo: identifying and removing duplicate records in DataFrames."""

from pathlib import Path

import pandas as pd


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        # Fallback dummy data with duplicates
        data = {
            "ID": [1, 2, 2, 3, 4, 4],
            "Name": ["Alice", "Bob", "Bob", "Charlie", "David", "David"],
            "City": ["NY", "LA", "LA", "SF", "CHI", "CHI"]
        }
        return pd.DataFrame(data)
    return pd.read_csv(csv_path)


def identify_duplicates(df: pd.DataFrame) -> None:
    print("\n1) Identifying Duplicates (duplicated)")
    
    # Check for complete row duplicates
    duplicates = df.duplicated()
    print(f"Total duplicate rows: {duplicates.sum()}")
    
    if duplicates.any():
        print("\nFirst 5 duplicate rows:")
        print(df[duplicates].head())
    else:
        print("\nNo exact row duplicates found. Let's check specific columns.")
        # Check duplicates in a column that likely has them, e.g., 'ComplaintType'
        if 'ComplaintType' in df.columns:
            print(f"\nDuplicates in 'ComplaintType': {df.duplicated('ComplaintType').sum()}")


def remove_duplicates(df: pd.DataFrame) -> None:
    print("\n2) Removing Duplicates (drop_duplicates)")

    print("\nDrop exact row duplicates (keeping first):")
    df_no_dupes = df.drop_duplicates()
    print(f"Original shape: {df.shape}, New shape: {df_no_dupes.shape}")

    if 'ComplaintType' in df.columns:
        print("\nDrop duplicates based on 'ComplaintType' (keeping last):")
        df_unique_type = df.drop_duplicates(subset=['ComplaintType'], keep='last')
        print(f"Unique 'ComplaintType' count: {len(df_unique_type)}")


def run_demo() -> None:
    df = load_dataframe()
    
    # Create artificial duplicates if none exist in the raw data for demonstration
    if df.duplicated().sum() == 0:
        print("Note: No duplicates found in raw data. Adding artificial duplicates for demo.")
        df = pd.concat([df, df.head(5)], ignore_index=True)

    identify_duplicates(df)
    remove_duplicates(df)


if __name__ == "__main__":
    run_demo()
