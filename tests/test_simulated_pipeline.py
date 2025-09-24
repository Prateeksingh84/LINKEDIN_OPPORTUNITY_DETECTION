import pytest
import pandas as pd
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.data_loader import load_job_dataset
from src.qualifier import qualify_posts

def test_load_job_dataset(monkeypatch, tmp_path, capsys):
    fake_folder = tmp_path / "data_folder"
    fake_folder.mkdir()
    test_file = fake_folder / "job_descriptions.csv"
    df = pd.DataFrame([
        {"Author": "Alice", "Company": "StartupX", "Job Description": "Looking for agency", "Engagement": 10, "Date": "2025-09-01"},
        {"Author": "Bob", "Company": "SmallBiz", "Job Description": "Hiring intern", "Engagement": 1, "Date": "2025-09-05"},
    ])
    df.to_csv(test_file, index=False)

    # Monkeypatch kagglehub download to point to this folder
    monkeypatch.setattr("src.data_loader.kagglehub.dataset_download", lambda *args, **kwargs: str(fake_folder))

    loaded_df = load_job_dataset()
    print("Loaded DataFrame head:")
    print(loaded_df.head())

    captured = capsys.readouterr()
    # Print what was captured (so it appears in pytest logs)
    print("Captured output:\n", captured.out)

    assert not loaded_df.empty
    assert "Job Description" in loaded_df.columns

def test_pipeline_with_fake_posts(capsys):
    posts = [
        {"author": "Alice", "company": "StartupX", "content": "Looking for agency help urgently", "engagement": 15, "date": "2025-09-01"},
        {"author": "Bob", "company": "SmallBiz", "content": "Hiring intern for marketing", "engagement": 1, "date": "2025-09-02"}
    ]
    qualified = [qualify_posts(p) for p in posts]
    print("Qualified results:", qualified)
    captured = capsys.readouterr()
    print("Captured output:\n", captured.out)

    assert any(q.get("score", 0) > 40 for q in qualified)
