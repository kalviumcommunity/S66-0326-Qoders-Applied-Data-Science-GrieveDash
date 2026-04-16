"""Milestone demo: exploring relationships between variables using scatter plots."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        # Fallback dummy data for relationship exploration
        import numpy as np
        n = 100
        x = np.linspace(0, 10, n)
        y = 2 * x + np.random.normal(0, 2, n)
        data = {
            "Variable_X": x,
            "Variable_Y": y,
            "Category": np.random.choice(["A", "B"], n)
        }
        return pd.DataFrame(data)
    
    df = pd.read_csv(csv_path)
    # Since raw data lacks multiple continuous numeric columns, 
    # we'll create a derived numeric column for demonstration
    if 'ComplaintType' in df.columns:
        df['TypeLength'] = df['ComplaintType'].apply(len)
        df['RowIndex'] = range(len(df))
    return df


def plot_scatter(df: pd.DataFrame) -> None:
    print("\n1) Generating Scatter Plot with Matplotlib")
    
    # Using derived columns if available, else generic ones
    x_col = 'RowIndex' if 'RowIndex' in df.columns else df.columns[0]
    y_col = 'TypeLength' if 'TypeLength' in df.columns else df.columns[1]

    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col], alpha=0.6, color='indigo')
    
    plt.title(f'Relationship between {x_col} and {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True, alpha=0.3)
    
    # Save output
    output_path = Path("outputs/scatter_plot_matplotlib.png")
    plt.savefig(output_path)
    print(f"Scatter plot saved to {output_path}")
    plt.close()


def plot_seaborn_scatter(df: pd.DataFrame) -> None:
    print("\n2) Generating Scatter Plot with Seaborn (with Hue)")
    
    x_col = 'RowIndex' if 'RowIndex' in df.columns else df.columns[0]
    y_col = 'TypeLength' if 'TypeLength' in df.columns else df.columns[1]
    hue_col = 'Status' if 'Status' in df.columns else None

    plt.figure(figsize=(12, 7))
    sns.scatterplot(x=x_col, y=y_col, hue=hue_col, data=df, palette='viridis', s=100)
    
    plt.title(f'Scatter Plot of {y_col} vs {x_col} (Colored by {hue_col})')
    
    # Save output
    output_path = Path("outputs/scatter_plot_seaborn.png")
    plt.savefig(output_path)
    print(f"Seaborn scatter plot saved to {output_path}")
    plt.close()


def run_demo() -> None:
    # Ensure output directory exists
    Path("outputs").mkdir(parents=True, exist_ok=True)
    
    df = load_dataframe()
    plot_scatter(df)
    plot_seaborn_scatter(df)


if __name__ == "__main__":
    run_demo()
