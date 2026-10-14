"""Main menu and program flow. Primary developer: Andrew Kirk (Student A)."""

from tracker import add_entry, view_all, view_summary


def main():
    """Repeat the menu and call the selected tracking function."""
    print("Welcome to Sleep Log Tracker!")
    print("Enter dates as YYYY-MM-DD, hours from 0 to 24, and quality from 1 to 5 (5 is best).")
    print("Notes are optional. Decimal hours are allowed.")
    print("Choose 1 to add, 2 for a summary, 3 for all entries, or 4 to exit.")
    print("The summary shows entry count, total and average hours, and best and worst quality.")
    print("Entries are stored only for this run and are cleared when the program closes.")

    while True:
        print("\n1. Add Sleep Entry")
        print("2. View Summary")
        print("3. View All Entries")
        print("4. Exit")

        try:
            choice = input("Choose an option: ").strip()
        except EOFError:
            print("\nGoodbye!")
            break

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            view_all()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
