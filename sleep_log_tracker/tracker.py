"""Sleep tracking function starters for Qingyun Li and Peter Oh."""

import data


def valid_date(date):
    """Check that a date uses YYYY-MM-DD and is a real calendar date."""
    if len(date) != 10:
        return False

    if date[4] != "-" or date[7] != "-":
        return False

    year_text = date[:4]
    month_text = date[5:7]
    day_text = date[8:]

    if not date.isascii():
        return False

    if not (
        year_text.isdigit()
        and month_text.isdigit()
        and day_text.isdigit()
    ):
        return False

    year = int(year_text)
    month = int(month_text)
    day = int(day_text)

    if year < 1 or month < 1 or month > 12:
        return False

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        month_lengths[1] = 29

    return 1 <= day <= month_lengths[month - 1]

def add_entry():
    """Validate a complete session before appending its four fields."""
    if not data.lists_are_synchronized():
        print("Error: inconsistent sleep data. Please restart the program.")
        return
    try:
        while True:
            date = input("Date (YYYY-MM-DD): ").strip()
            if valid_date(date):
                break
            print("Invalid date. Enter a real date in YYYY-MM-DD format.")

        while True:
            try:
                hours = float(input("Hours slept (0–24): ").strip())
            except ValueError:
                print("Invalid hours. Enter a number from 0 through 24.")
                continue

            if 0 <= hours <= 24:
                break
            print("Invalid hours. Enter a number from 0 through 24.")

        while True:
            try:
                quality = int(input("Sleep quality (1–5): ").strip())
            except ValueError:
                print("Invalid quality. Enter a whole number from 1 through 5.")
                continue

            if 1 <= quality <= 5:
                break
            print("Invalid quality. Enter a whole number from 1 through 5.")

        entry_notes = input("Notes (optional): ").strip()

    except EOFError:
        print("\nEntry canceled. No data was added.")
        return

    data.dates.append(date)
    data.hours_slept.append(hours)
    data.sleep_qualities.append(quality)
    data.notes.append(entry_notes)

    print("Entry added.")


def view_all():
    """Display sessions using matching indexes in the four lists."""
    if len(data.dates) == 0:
        print("No sleep entries recorded.")
        return

    for index in range(len(data.dates)):
        print(f"\nEntry {index + 1}")
        print(f"Date: {data.dates[index]}")
        print(f"Hours slept: {data.hours_slept[index]:.2f}")
        print(f"Sleep quality: {data.sleep_qualities[index]}/5")

        if data.notes[index] == "":
            print("Notes: None")
        else:
            print(f"Notes: {data.notes[index]}")


def view_summary():
    print("View Summary is awaiting implementation.")
