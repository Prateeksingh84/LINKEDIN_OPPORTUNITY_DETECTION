import os
import csv
import json
from data_loader import load_job_dataset
from qualifier import qualify_posts

HIGH_PRIORITY_THRESHOLD = 70

def process_simulated_posts():
    """
    Use Kaggle dataset as simulated LinkedIn posts for testing.
    Save all opportunities to CSV and JSON.
    """
    df = load_job_dataset()

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

    # Save to CSV
    with open('outputs/sample_output.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=all_opps[0].keys())
        writer.writeheader()
        writer.writerows(all_opps)
    print("Saved all opportunities to 'sample_output.csv'.")

    # Save to JSON
    with open('outputs/sample_output.json', mode='w') as file:
        json.dump(all_opps, file, indent=2)
    print("Saved all opportunities to 'sample_output.json'.")

    # Notify high-priority opportunities
    for opp in all_opps:
        if opp["score"] >= HIGH_PRIORITY_THRESHOLD:
            notify_high_priority(opp)

def notify_high_priority(opportunity):
    """
    Notify about high-priority opportunities.
    For simplicity, we print to console. This could be extended to send emails or Slack messages.
    """
    print(f"🚨 High-priority opportunity: {opportunity['company']} by {opportunity['author']} (score {opportunity['score']})")

# Run the function
process_simulated_posts()
