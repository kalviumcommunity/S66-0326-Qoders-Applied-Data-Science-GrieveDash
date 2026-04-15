"""Milestone demo: creating Pandas DataFrames from dictionaries and files."""

from pathlib import Path

import pandas as pd


def dataframe_from_dictionary() -> pd.DataFrame:
    print("\n1) DataFrame from dictionary")
    grievance_dict = {
        "complaint_id": [101, 102, 103],
        "issue_type": ["water", "roads", "garbage"],
        "status": ["pending", "resolved", "in_progress"],
    }
    df_dict = pd.DataFrame(grievance_dict)

    print(df_dict)
    print(f"Shape: {df_dict.shape}")
    print(f"Columns: {df_dict.columns.tolist()}")
    print(df_dict.dtypes)
    return df_dict


def dataframe_from_file() -> pd.DataFrame:
    print("\n2) DataFrame from CSV file")
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        raise FileNotFoundError(
            f"CSV not found at {csv_path}. Place the file in data/raw/ first."
        )

    df_file = pd.read_csv(csv_path)

    print(df_file.head(5))
    print(f"Shape: {df_file.shape}")
    print(f"Columns: {df_file.columns.tolist()}")
    print(df_file.dtypes)
    return df_file


def run_demo() -> None:
    dataframe_from_dictionary()
    dataframe_from_file()


if __name__ == "__main__":
    run_demo()
