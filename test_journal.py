import unittest
from journal import Journal
import os
import json

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.journal = Journal()
        self.journal.filename = "test_entries.json"

    def tearDown(self):
        if os.path.exists(self.journal.filename):
            os.remove(self.journal.filename)

    def test_add_entry(self):
        result = self.journal.add_entry(
            "Test entry",
            mood="happy",
            activities=["coding", "testing"],
            date="2024-01-01"
        )
        self.assertTrue("Entry added" in result)
        
        with open(self.journal.filename, 'r') as f:
            entries = json.load(f)
        
        self.assertEqual(len(entries), 1)
        entry = list(entries.values())[0]
        self.assertEqual(entry["text"], "Test entry")
        self.assertEqual(entry["mood"], "happy")
        self.assertEqual(entry["activities"], ["coding", "testing"])

    def test_search_entries(self):
        self.journal.add_entry("First test entry", "happy", ["coding"], date="2024-01-01")
        self.journal.add_entry("Second test entry", "sad", ["reading"], date="2024-01-02")
        
        results = self.journal.search_entries("First")
        self.assertEqual(len(results), 1)
        
        results = self.journal.search_entries("test")
        self.assertEqual(len(results), 2)

    def test_get_entry(self):
        self.journal.add_entry("Test entry", "neutral", ["writing"], date="2024-01-01")
        entry = self.journal.get_entry("2024-01-01")
        self.assertIsNotNone(entry)
        self.assertEqual(entry["text"], "Test entry")

if __name__ == '__main__':
    unittest.main()