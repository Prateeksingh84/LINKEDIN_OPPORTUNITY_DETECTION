# run_simulation.py

import os
import csv
import json
from data_loader import load_job_dataset
from qualifier import qualify_posts

HIGH_PRIORITY_THRESHOLD = 70

def notify_high_priority(opportunity):
    """
    Notify about high-priority opportunities.
    Here we just print to console.
    """
    print(
        f"🚨 High-priority opportunity: {opportunity['company']} by {opportunity.get('author', opportunity.get('author_name'))} "
        f"(score {opportunity['score']})"
    )

def process_simulated_posts():
    """
    Use Kaggle dataset as simulated LinkedIn posts for testing.
    Save all opportunities to CSV and JSON. Also print notifications for high-priority ones.
    """
    df = load_job_dataset()
    print(f"Loaded dataset, number of rows: {len(df)}")

    posts = []
    for _, row in df.iterrows():
        posts.append({
            "author": row.get("Author", "Unknown"),
            "company": row.get("Company", "Unknown"),
            "content": row.get("Job Description", ""),
            "engagement": row.get("Engagement", 0),
            "date": row.get("Date", "N/A"),
        })

    all_opps = [qualify_posts(p) for p in posts]
    print(f"Computed {len(all_opps)} opportunities")

    # Ensure outputs directory exists
    os.makedirs("outputs", exist_ok=True)

    # Write CSV
    csv_path = os.path.join("outputs", "sample_output.csv")
    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=all_opps[0].keys())
        writer.writeheader()
        writer.writerows(all_opps)
    print(f"Saved CSV to {csv_path}")

    # Write JSON
    json_path = os.path.join("outputs", "sample_output.json")
    with open(json_path, mode='w', encoding='utf-8') as file:
        json.dump(all_opps, file, indent=2, ensure_ascii=False)
    print(f"Saved JSON to {json_path}")

    # Print high priority notifications
    for opp in all_opps:
        if opp.get("score", 0) >= HIGH_PRIORITY_THRESHOLD:
            notify_high_priority(opp)


if __name__ == "__main__":
    process_simulated_posts()
