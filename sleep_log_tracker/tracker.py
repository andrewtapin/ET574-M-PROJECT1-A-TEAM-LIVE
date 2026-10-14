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
    print("Add Sleep Entry is awaiting implementation.")


def view_all():
    print("View All Entries is awaiting implementation.")


def view_summary():
    print("View Summary is awaiting implementation.")
