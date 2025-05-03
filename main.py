from journal import Journal
from datetime import datetime
import sys

def print_menu():
    print("\n=== Daily Journal ===")
    print("1. Add new entry")
    print("2. View today's entry")
    print("3. View entry by date")
    print("4. Search entries")
    print("5. List all dates")
    print("6. Exit")
    print("==================")

def get_valid_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            print("Please enter a number between 1 and 6")
        except ValueError:
            print("Please enter a valid number")

def add_entry(journal):
    text = input("Write your journal entry: ")
    mood = input("How are you feeling today? (happy/neutral/sad): ").lower()
    activities = input("Enter activities (comma-separated): ").split(",")
    activities = [a.strip() for a in activities if a.strip()]
    print(journal.add_entry(text, mood, activities))

def view_entry(journal, date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    entry = journal.get_entry(date)
    if entry:
        print(f"\nDate: {date}")
        print(f"Mood: {entry['mood']}")
        print(f"Activities: {', '.join(entry['activities'])}")
        print(f"Entry: {entry['text']}")
    else:
        print(f"No entry found for {date}")

def search_entries(journal):
    keyword = input("Enter search term: ")
    results = journal.search_entries(keyword)
    if results:
        for date, entry in results.items():
            print(f"\nDate: {date}")
            print(f"Entry: {entry['text'][:100]}...")
    else:
        print("No entries found")

def main():
    journal = Journal()
    
    while True:
        print_menu()
        choice = get_valid_choice()
        
        if choice == 1:
            add_entry(journal)
        elif choice == 2:
            view_entry(journal)
        elif choice == 3:
            date = input("Enter date (YYYY-MM-DD): ")
            view_entry(journal, date)
        elif choice == 4:
            search_entries(journal)
        elif choice == 5:
            dates = journal.list_entries()
            if dates:
                print("\nAll entries:")
                for date in dates:
                    print(date)
            else:
                print("No entries yet")
        elif choice == 6:
            print("Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()