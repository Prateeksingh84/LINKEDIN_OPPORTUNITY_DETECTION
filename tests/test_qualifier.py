import sys
import os
import pytest

# Add project root so we can import src modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.qualifier import score_opportunity, qualify_posts
from src.file_store import save_to_csv, save_to_json

def test_score_opportunity_high_score(capsys):
    post = {
        "content": "We are looking for a digital agency to handle our marketing. Budget $50k.",
        "likes": 20,
        "comments": 5,
        "shares": 2,
        "date": "2025-09-01"
    }
    company_info = {"employee_count": 500, "revenue": 5_000_000}
    result = score_opportunity(post, company_info)
    print("High score result:", result)
    captured = capsys.readouterr()
    # Print out what was captured, so it appears in the test log
    sys.stdout.write("Captured: " + captured.out)
    assert result["score"] > 70
    assert result["priority"] in ["high", "medium", "low"]

def test_score_opportunity_low_score(capsys):
    post = {"content": "Hiring intern for marketing", "likes": 1, "comments": 0, "shares": 0}
    company_info = {"employee_count": 5, "revenue": 50_000}
    result = score_opportunity(post, company_info)
    print("Low score result:", result)
    captured = capsys.readouterr()
    sys.stdout.write("Captured: " + captured.out)
    assert result["score"] < 40
    assert result["status"] in ["qualified", "unqualified"]

def test_qualify_posts_basic(capsys):
    post = {"content": "Looking for agency support in branding"}
    result = qualify_posts(post)
    print("Qualified post:", result)
    captured = capsys.readouterr()
    sys.stdout.write("Captured: " + captured.out)
    assert "score" in result
    assert "priority" in result
    assert "status" in result
