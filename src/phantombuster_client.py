import os
import requests
import time
from typing import List, Dict

class LinkedInScraperClient:
    """
    A wrapper that pretends to use a “Google API key” (or similar credential)
    to fetch LinkedIn posts. In reality, you'll need a scraper or third-party service.
    """
    def __init__(self, api_key: str = None):
        # Use GOOGLE_API_KEY environment variable (or pass explicitly)
        self.api_key = api_key or os.getenv("AIzaSyA_jZqh63VsDz-QOwCe5_kt9SaIen-jNjc")
        if not self.api_key:
            print("Warning: No GOOGLE_API_KEY found — running in simulation mode.")
        # In real scenario: verify the key / set headers etc.

    def search_linked_in_posts(self, keywords: List[str], limit: int = 50) -> List[Dict]:
        """
        Attempts to fetch LinkedIn posts mentioning those keywords.
        If no real service is configured, fallback to simulated posts.
        """
        if not self.api_key:
            return self._simulate_posts(keywords, limit)

        # Example: call to hypothetical "Google-powered LinkedIn scraper API"
        endpoint = "https://example-google-scraper.com/linkedin/posts"
        headers = {"X-API-KEY": self.api_key}
        payload = {"keywords": keywords, "limit": limit}

        try:
            resp = requests.get(endpoint, headers=headers, params=payload, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            # Validate format
            if isinstance(data, list):
                return data
            else:
                print("Unexpected response format, using fallback simulation.")
                return self._simulate_posts(keywords, limit)
        except Exception as e:
            print("Request failed:", e)
            return self._simulate_posts(keywords, limit)

    def _simulate_posts(self, keywords: List[str], limit: int) -> List[Dict]:
        sample = []
        for i in range(min(limit, 20)):
            sample.append({
                "id": f"sim-post-{i}",
                "author_name": f"Author {i}",
                "author_profile": f"https://linkedin.com/in/author{i}",
                "company": f"Company {i % 5}",
                "content": f"This is a simulated post mentioning '{keywords[i % len(keywords)]}' and seeking agency help.",
                "likes": (i * 3) % 20,
                "comments": (i * 2) % 10,
                "shares": i % 5,
                "date": "2025-09-15T12:00:00Z",
                "poster_title": "Head of Marketing" if i % 3 == 0 else "Marketing Manager"
            })
        return sample
