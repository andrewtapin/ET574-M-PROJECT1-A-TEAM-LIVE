"""Main menu and program flow. Primary developer: Andrew Kirk (Student A)."""

from tracker import add_entry, view_all, view_summary


def main():
    print("Welcome to Sleep Log Tracker!")
    while True:
        print("\n1. Add Sleep Entry")
        print("2. View Summary")
        print("3. View All Entries")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            view_all()
        elif choice == "4":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
