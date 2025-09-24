# client_demo.py

import os
from typing import List, Dict, Optional
import requests

# If Google fallback is enabled
GOOGLE_FALLBACK = True  

class LinkedInClient:
    def __init__(self, access_token: Optional[str] = None):
        self.access_token = access_token or os.getenv("LINKEDIN_ACCESS_TOKEN")
        self.headers = {}
        if self.access_token:
            self.headers = {
                "Authorization": f"Bearer {self.access_token}",
                "X-Restli-Protocol-Version": "2.0.0"
            }

    def search_posts_by_keywords(self, keywords: List[str], limit: int = 50) -> List[Dict]:
        """
        Attempts to use LinkedIn API. If unavailable, fallback to Google-based scraper (or simulation).
        Returns list of post dicts:
        { "id", "author_name", "author_profile", "company", "content", "likes", "comments", "shares", "date" }
        """
        if self.access_token:
            try:
                return self._search_posts_api(keywords, limit)
            except Exception as e:
                print("LinkedIn API search failed:", e)
                if GOOGLE_FALLBACK:
                    return self._fallback_google_scrape(keywords, limit)
                raise
        else:
            # no access token: fallback
            if GOOGLE_FALLBACK:
                return self._fallback_google_scrape(keywords, limit)
            else:
                raise ValueError("No access token and no fallback configured")

    def _search_posts_api(self, keywords: List[str], limit: int = 50) -> List[Dict]:
        """
        Placeholder: your logic to call LinkedIn official API (if you have access).
        """
        raise NotImplementedError("LinkedIn API not implemented or not authorized")

    def _fallback_google_scrape(self, keywords: List[str], limit: int) -> List[Dict]:
        """
        Fallback method pretending to use a “Google API” for scraping.
        In practice, this should call your scraping service / third-party API.
        """
        google_api_key = os.getenv("GOOGLE_API_KEY")
        if not google_api_key:
            print("No GOOGLE_API_KEY found; using simulated posts.")
            return self._simulate_posts(keywords, limit)

        endpoint = "https://example-google-scraper.com/linkedin/posts"
        headers = {"X-API-KEY": google_api_key}
        params = {"keywords": ",".join(keywords), "limit": limit}

        try:
            resp = requests.get(endpoint, headers=headers, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            if isinstance(data, list):
                print("Google scraper returned data.")
                return data
            else:
                print("Unexpected Google scraper response format; using fallback simulation.")
                return self._simulate_posts(keywords, limit)
        except Exception as e:
            print("Google scraper request failed:", e)
            return self._simulate_posts(keywords, limit)

    def _simulate_posts(self, keywords: List[str], limit: int) -> List[Dict]:
        """
        Produce dummy/simulated posts for testing or fallback.
        """
        sample = []
        for i in range(min(limit, 20)):
            sample.append({
                "id": f"sim-post-{i}",
                "author_name": f"Author {i}",
                "author_profile": f"https://linkedin.com/in/author{i}",
                "company": f"Company {i % 5}",
                "content": f"This is a simulated post mentioning '{keywords[i % len(keywords)]}' and asking for agency help.",
                "likes": (i * 3) % 20,
                "comments": (i * 2) % 10,
                "shares": i % 5,
                "date": "2025-09-15T12:00:00Z",
            })
        print(f"Simulated {len(sample)} posts.")
        return sample

if __name__ == "__main__":
    # Example keywords
    keywords = ["looking for agency", "need marketing help", "urgent marketing"]
    client = LinkedInClient()  # no access token -> fallback
    posts = client.search_posts_by_keywords(keywords, limit=10)
    print("Fetched posts:")
    for p in posts:
        print(p)
# Example usage
    keywords = ["looking for agency", "need marketing help", "urgent marketing"]
    client = LinkedInClient()  # no access token -> fallback
    posts = client.search_posts_by_keywords(keywords, limit=10)
    print("Fetched posts:")
    for p in posts:
        print(p)
        