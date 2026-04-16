"""Milestone demo: standardizing column names and data formats in DataFrames."""

from pathlib import Path

import pandas as pd


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        # Fallback dummy data
        data = {
            "First Name": [" Alice ", "BOB", "charlie"],
            "DATE_OF_BIRTH": ["1990-01-01", "1991/02/02", "03-03-1992"],
            "Salary ": [" 50000 ", "60000", " 70000"]
        }
        return pd.DataFrame(data)
    return pd.read_csv(csv_path)


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    print("\n1) Standardizing Column Names")
    print(f"Original columns: {df.columns.tolist()}")
    
    # Lowercase and replace spaces with underscores
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    print(f"Standardized columns: {df.columns.tolist()}")
    return df


def standardize_formats(df: pd.DataFrame) -> pd.DataFrame:
    print("\n2) Standardizing Data Formats")
    
    # Strip whitespace from string columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()
    
    print("\nWhitespace stripped from string columns.")
    
    # Example: Convert a column to datetime if it exists (like 'ComplaintDate' in our raw data)
    # In our raw data, columns are: ComplaintID, ComplaintType, Status, ComplaintDate, Ward
    if 'complaintdate' in df.columns:
        print("\nConverting 'complaintdate' to datetime format:")
        df['complaintdate'] = pd.to_datetime(df['complaintdate'])
        print(df['complaintdate'].head())
    
    # Example: Ensure numeric types
    if 'complaintid' in df.columns:
        df['complaintid'] = pd.to_numeric(df['complaintid'], errors='coerce')
        
    return df


def run_demo() -> None:
    df = load_dataframe()
    
    df = standardize_columns(df)
    df = standardize_formats(df)
    
    print("\nFinal DataFrame Info after Standardization:")
    df.info()
    print("\nHead of Standardized DataFrame:")
    print(df.head())


if __name__ == "__main__":
    run_demo()
