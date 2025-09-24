# src/save_all_simulation.py

import os
from data_loader import load_job_dataset
from qualifier import qualify_posts
from file_store import save_to_csv, save_to_json

def process_and_save_all():
    # Load data
    df = load_job_dataset()
    print(f"🚀 Loaded dataset with {len(df)} rows")

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
    print(f"✅ After qualification: {len(all_opps)} opportunities")

    # Ensure output directory exists
    os.makedirs(os.path.join(os.path.dirname(__file__), "..", "outputs"), exist_ok=True)

    # Save everything
    save_to_csv(all_opps)
    save_to_json(all_opps)
    print("✅ Saved to outputs/sample_output.csv and sample_output.json")

if __name__ == "__main__":
    process_and_save_all()
    # test saving empty list
    save_to_csv([])
    save_to_json([])
    print("✅ Tested saving empty lists")
    print("✅ All done!")
    