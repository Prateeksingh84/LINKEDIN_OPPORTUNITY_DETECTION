# src/file_store.py

import csv
import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSV_FILE = os.path.join(OUTPUT_DIR, "sample_output.csv")
JSON_FILE = os.path.join(OUTPUT_DIR, "sample_output.json")

def save_to_csv(opportunities: list):
    if not opportunities:
        print("⚠️ No opportunities to save in CSV.")
        return

    # Compute the union of all keys across all opportunity dicts
    all_keys = set()
    for opp in opportunities:
        all_keys.update(opp.keys())

    fieldnames = list(all_keys)

    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(opportunities)

    print(f"📂 Saved {len(opportunities)} opportunities to {CSV_FILE}")

def save_to_json(opportunities: list):
    if not opportunities:
        print("⚠️ No opportunities to save in JSON.")
        return

    with open(JSON_FILE, mode="w", encoding="utf-8") as f:
        json.dump(opportunities, f, indent=2, ensure_ascii=False)

    print(f"📂 Saved {len(opportunities)} opportunities to {JSON_FILE}")

if __name__ == "__main__":
    # test saving empty list
    save_to_csv([])
    save_to_json([])
