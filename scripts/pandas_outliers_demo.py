"""Milestone demo: detecting outliers using visual inspection and simple rules."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        # Fallback dummy data with outliers
        import numpy as np
        data = {
            "Value": [10, 12, 11, 13, 100, 11, 12, 11, 13, 9]
        }
        return pd.DataFrame(data)
    return pd.read_csv(csv_path)


def visual_inspection(df: pd.DataFrame, column: str) -> None:
    print(f"\n1) Visual Inspection for '{column}'")
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(y=df[column], color='lightblue')
    plt.title(f'Boxplot of {column}')
    
    plt.subplot(1, 2, 2)
    plt.scatter(range(len(df)), df[column], alpha=0.5, color='orange')
    plt.title(f'Scatter Plot of {column}')
    
    # Save output
    output_path = Path("outputs/outliers_visual_inspection.png")
    plt.savefig(output_path)
    print(f"Visual inspection plots saved to {output_path}")
    plt.close()


def detect_outliers_iqr(df: pd.DataFrame, column: str) -> None:
    print(f"\n2) Detecting Outliers using IQR (Interquartile Range) for '{column}'")
    
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
    print(f"Bounds for outliers: Below {lower_bound} or Above {upper_bound}")
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"Total outliers detected: {len(outliers)}")
    
    if len(outliers) > 0:
        print("\nDetected Outliers:")
        print(outliers.head())


def run_demo() -> None:
    # Ensure output directory exists
    Path("outputs").mkdir(parents=True, exist_ok=True)
    
    df = load_dataframe()
    
    # Use 'resolution_time' if it exists, otherwise 'complaint_id'
    target_col = 'resolution_time' if 'resolution_time' in df.columns else 'complaint_id'
    
    # If the column has no variation or only 0s, detection might be trivial
    if df[target_col].nunique() <= 1:
         print(f"Warning: '{target_col}' has very low variation. Outlier detection might not show interesting results.")

    visual_inspection(df, target_col)
    detect_outliers_iqr(df, target_col)


if __name__ == "__main__":
    run_demo()
