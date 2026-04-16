"""Milestone demo: identifying trends over time using line plots."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def load_dataframe() -> pd.DataFrame:
    csv_path = Path("data/raw/municipal_grievance_full_200.csv")
    if not csv_path.exists():
        # Fallback dummy time-series data
        import numpy as np
        dates = pd.date_range(start="2023-01-01", periods=100)
        data = {
            "ComplaintDate": dates,
            "ComplaintID": range(1, 101)
        }
        return pd.DataFrame(data)
    return pd.read_csv(csv_path)


def plot_trend_line(df: pd.DataFrame) -> None:
    print("\n1) Processing Time-Series Data")
    
    # Ensure ComplaintDate is datetime
    if 'ComplaintDate' in df.columns:
        df['ComplaintDate'] = pd.to_datetime(df['ComplaintDate'])
        
        # Aggregate complaints by date
        trend_data = df.groupby('ComplaintDate').size()
        
        print("\n2) Generating Line Plot with Matplotlib")
        plt.figure(figsize=(12, 6))
        
        plt.plot(trend_data.index, trend_data.values, marker='o', linestyle='-', color='teal')
        
        plt.title('Trend of Complaints Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Complaints')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save output
        output_path = Path("outputs/line_plot_trend.png")
        plt.savefig(output_path)
        print(f"Line plot saved to {output_path}")
        plt.close()


def run_demo() -> None:
    # Ensure output directory exists
    Path("outputs").mkdir(parents=True, exist_ok=True)
    
    df = load_dataframe()
    plot_trend_line(df)


if __name__ == "__main__":
    run_demo()
