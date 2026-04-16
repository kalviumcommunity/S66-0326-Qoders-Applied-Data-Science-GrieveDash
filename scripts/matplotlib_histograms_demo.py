"""Milestone demo: visualizing data distributions using histograms."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        # Fallback dummy data
        import numpy as np
        data = {
            "Score": np.random.normal(70, 10, 200),
            "Age": np.random.randint(18, 80, 200)
        }
        return pd.DataFrame(data)
    return pd.read_csv(csv_path)


def plot_histogram(df: pd.DataFrame) -> None:
    print("\n1) Generating Histogram")
    
    # In our raw data, ComplaintID is the only numeric column we can use for a histogram demo
    # even if it's just an ID. If we had real numeric data like 'ProcessingTime', it would be better.
    target_col = 'ComplaintID'
    if target_col in df.columns:
        plt.figure(figsize=(10, 6))
        
        # Using Matplotlib
        plt.hist(df[target_col], bins=20, color='skyblue', edgecolor='black')
        
        plt.title(f'Histogram of {target_col}')
        plt.xlabel(target_col)
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.75)
        
        # Save output
        output_path = Path("outputs/histogram_matplotlib.png")
        plt.savefig(output_path)
        print(f"Histogram saved to {output_path}")
        plt.close()


def plot_seaborn_hist(df: pd.DataFrame) -> None:
    print("\n2) Generating Histogram with Seaborn (KDE)")
    
    target_col = 'ComplaintID'
    if target_col in df.columns:
        plt.figure(figsize=(10, 6))
        
        # Using Seaborn for more advanced visuals (KDE = Kernel Density Estimate)
        sns.histplot(df[target_col], bins=20, kde=True, color='salmon')
        
        plt.title(f'Seaborn Distribution Plot of {target_col}')
        plt.xlabel(target_col)
        plt.ylabel('Frequency')
        
        # Save output
        output_path = Path("outputs/histogram_seaborn.png")
        plt.savefig(output_path)
        print(f"Seaborn histogram saved to {output_path}")
        plt.close()


def run_demo() -> None:
    # Ensure output directory exists
    Path("outputs").mkdir(parents=True, exist_ok=True)
    
    df = load_dataframe()
    plot_histogram(df)
    plot_seaborn_hist(df)


if __name__ == "__main__":
    run_demo()
