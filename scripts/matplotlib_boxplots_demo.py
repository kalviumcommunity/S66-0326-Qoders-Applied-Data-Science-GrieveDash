"""Milestone demo: visualizing data distributions using boxplots."""

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
            "Region": ["North", "South", "East", "West"] * 50,
            "Score": np.random.normal(70, 15, 200)
        }
        return pd.DataFrame(data)
    return pd.read_csv(csv_path)


def plot_boxplot(df: pd.DataFrame) -> None:
    print("\n1) Generating Boxplot with Matplotlib")
    
    # Using 'Ward' as a categorical and 'ComplaintID' as a numeric for demo
    # In a real scenario, we'd use something like 'DaysToResolve' vs 'ComplaintType'
    if 'Ward' in df.columns and 'ComplaintID' in df.columns:
        plt.figure(figsize=(10, 6))
        
        # Prepare data for matplotlib (list of arrays)
        wards = df['Ward'].unique()
        data_to_plot = [df[df['Ward'] == ward]['ComplaintID'] for ward in wards]
        
        plt.boxplot(data_to_plot, labels=wards)
        
        plt.title('Boxplot of ComplaintID by Ward (Matplotlib)')
        plt.xlabel('Ward')
        plt.ylabel('ComplaintID')
        
        # Save output
        output_path = Path("outputs/boxplot_matplotlib.png")
        plt.savefig(output_path)
        print(f"Boxplot saved to {output_path}")
        plt.close()


def plot_seaborn_boxplot(df: pd.DataFrame) -> None:
    print("\n2) Generating Boxplot with Seaborn")
    
    if 'ComplaintType' in df.columns and 'ComplaintID' in df.columns:
        plt.figure(figsize=(12, 6))
        
        # Seaborn makes it much easier to plot categorical vs numeric
        sns.boxplot(x='ComplaintType', y='ComplaintID', data=df, palette='Set3')
        
        plt.title('Boxplot of ComplaintID by Complaint Type (Seaborn)')
        plt.xticks(rotation=45)
        
        # Save output
        output_path = Path("outputs/boxplot_seaborn.png")
        plt.savefig(output_path)
        print(f"Seaborn boxplot saved to {output_path}")
        plt.close()


def run_demo() -> None:
    # Ensure output directory exists
    Path("outputs").mkdir(parents=True, exist_ok=True)
    
    df = load_dataframe()
    plot_boxplot(df)
    plot_seaborn_boxplot(df)


if __name__ == "__main__":
    run_demo()
