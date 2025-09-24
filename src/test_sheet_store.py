# src/test_sheet_store.py

import pytest
from src.sheet_store import append_opportunity

class DummySheet:
    def __init__(self):
        self.rows = []

    def append_row(self, values):
        self.rows.append(values)

def test_append_opportunity():
    sheet = DummySheet()
    opportunity = {
        "id": "123",
        "author_name": "Test Author",
        "company": "Test Co",
        "content": "Looking for agency help",
        "score": 80,
        "priority": "high",
        "status": "qualified",
        "date": "2025-09-20",
        "engagement": 10,
        "next_steps": "Reach out via email"
    }
    append_opportunity(sheet, opportunity)
    assert len(sheet.rows) == 1
    saved_row = sheet.rows[0]
    assert saved_row[3] == "Looking for agency help"
    assert saved_row[4] == 80
    assert saved_row[1] == "Test Author"
    assert saved_row[5] == "high"
    assert saved_row[6] == "qualified"
    assert saved_row[7] == "2025-09-20"
    assert saved_row[8] == 10
    assert saved_row[9] == "Reach out via email"
    assert saved_row[2] == "Test Co"
    assert saved_row[0] == "123"
    