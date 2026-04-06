import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Simulating Data Lifecycle Flow...")

    # 1. Generate Raw Data
    raw_data_path = "data/raw/grievances_raw.csv"
    raw_data = {
        "complaint_id": [101, 102, 103, 104, 105],
        "category": ["water", "roads", "water", "electricity", "roads"],
        "status": ["open", "closed", "closed", "open", "in-progress"],
        "junk_column": ["null", "NaN", "N/A", "null", "err"] # Needs cleaning
    }
    df_raw = pd.DataFrame(raw_data)
    df_raw.to_csv(raw_data_path, index=False)
    print(f"✅ Raw data saved to {raw_data_path} (DO NOT MODIFY)")

    # 2. Process Data (Cleaning)
    processed_data_path = "data/processed/grievances_cleaned.csv"
    # Drop the junk column to simulate cleaning
    df_processed = df_raw.drop(columns=["junk_column"])
    df_processed.to_csv(processed_data_path, index=False)
    print(f"✅ Processed data saved to {processed_data_path} (Derived from raw)")

    # 3. Generate Output Artifact (Plot)
    output_plot_path = "outputs/complaints_by_status.png"
    status_counts = df_processed["status"].value_counts()
    
    plt.figure(figsize=(6, 4))
    status_counts.plot(kind="bar", color=["#3498db", "#2ecc71", "#e74c3c"])
    plt.title("Complaints by Status")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_plot_path)
    print(f"✅ Output visualization saved to {output_plot_path} (Final artifact)")

    print("\nData organization lifecycle perfectly maintained!")

if __name__ == "__main__":
    # Ensure directories exist (they should from the previous milestone)
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    
    main()
