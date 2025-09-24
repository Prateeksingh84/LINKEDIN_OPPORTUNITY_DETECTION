# src/main_simulation_all.py

import os
from file_store import save_to_csv, save_to_json
from data_loader import load_job_dataset
from qualifier import qualify_posts

def export_all_rows():
    """
    Load the full dataset and export every row after qualification to sample_output CSV and JSON.
    No filtering by score.
    """
    df = load_job_dataset()
    print(f"Dataset contains {len(df)} rows.")

    rows = []
    for _, row in df.iterrows():
        post = {
            "author": row.get("Author", "Unknown"),
            "company": row.get("Company", "Unknown"),
            "content": row.get("Job Description", ""),
            "engagement": row.get("Engagement", 0),
            "date": row.get("Date", "N/A"),
        }
        opp = qualify_posts(post)
        rows.append(opp)

    # Ensure outputs dir exists
    os.makedirs("outputs", exist_ok=True)

    save_to_csv(rows)
    save_to_json(rows)
    print("✅ Exported all rows to sample_output.csv & sample_output.json")
