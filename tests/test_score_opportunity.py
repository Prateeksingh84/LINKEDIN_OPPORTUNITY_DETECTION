# demo_qualifier.py

import sys
import os

# Insert project root so “src” import works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.qualifier import score_opportunity, qualify_posts

# Sample post data
post = {
    "content": "Looking for agency help urgently",
    "likes": 50,
    "comments": 10,
    "shares": 5,
    "engagement": 0,  # fallback
}

# Sample company info
company_info = {
    "employee_count": 300,
    "revenue": 5_000_000,
}

def main():
    scored_post = score_opportunity(post, company_info)
    qualified_post = qualify_posts(post)
    print("Scored Opportunity:", scored_post)
    print("Qualified Post:", qualified_post)

if __name__ == "__main__":
    main()
