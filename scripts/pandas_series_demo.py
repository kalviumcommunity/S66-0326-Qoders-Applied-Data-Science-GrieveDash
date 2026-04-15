"""Milestone demo: creating Pandas Series from lists and NumPy arrays."""

import numpy as np
import pandas as pd


def series_from_list() -> None:
    print("\n1) Series from Python list")
    complaints = [12, 18, 9, 15]
    complaints_series = pd.Series(complaints)

    print("Series:")
    print(complaints_series)
    print(f"Index: {complaints_series.index}")
    print(f"Values: {complaints_series.values}")


def series_from_array() -> None:
    print("\n2) Series from NumPy array")
    response_times = np.array([2.5, 1.8, 3.2, 2.1])
    response_series = pd.Series(response_times)

    print("Series:")
    print(response_series)
    print(f"dtype: {response_series.dtype}")


def index_and_access_demo() -> None:
    print("\n3) Index and value access")
    issue_counts = pd.Series(
        [40, 25, 15],
        index=["water", "roads", "electricity"],
    )

    print("Labeled Series:")
    print(issue_counts)

    print(f"Label-based access ['roads']: {issue_counts['roads']}")
    print(f"Position-based access .iloc[1]: {issue_counts.iloc[1]}")
    print(f"Index labels: {issue_counts.index.tolist()}")
    print(f"Raw values: {issue_counts.values}")


def run_demo() -> None:
    series_from_list()
    series_from_array()
    index_and_access_demo()


if __name__ == "__main__":
    run_demo()
