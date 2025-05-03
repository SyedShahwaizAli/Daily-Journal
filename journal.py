import os
import json
from datetime import datetime

class JournalEntry:
    def __init__(self, text, mood="neutral", activities=None, date=None):
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.text = text
        self.mood = mood
        self.activities = activities if activities else []

class Journal:
    def __init__(self):
        self.filename = "entries.json"
        self.entries = self._load_entries()

    def _load_entries(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except:
            return {}

    def _save_entries(self):
        with open(self.filename, 'w') as f:
            json.dump(self.entries, f, indent=4)

    def add_entry(self, text, mood="neutral", activities=None, date=None):
        entry = JournalEntry(text, mood, activities, date)
        self.entries[entry.date] = {
            "text": entry.text,
            "mood": entry.mood,
            "activities": entry.activities
        }
        self._save_entries()
        return f"Entry added for {entry.date}"

    def get_entry(self, date):
        return self.entries.get(date, None)

    def search_entries(self, keyword):
        matches = {}
        for date, entry in self.entries.items():
            if keyword.lower() in entry["text"].lower() or \
               keyword.lower() in entry["mood"].lower() or \
               any(keyword.lower() in activity.lower() for activity in entry["activities"]):
                matches[date] = entry
        return matches

    def list_entries(self):
        return sorted(self.entries.keys(), reverse=True)