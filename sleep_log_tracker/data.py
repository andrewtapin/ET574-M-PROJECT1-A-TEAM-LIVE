"""Shared in-memory storage for sleep sessions.

The same index in all four lists identifies one complete session:
dates[index], hours_slept[index], sleep_qualities[index], and notes[index].

Validate every field before appending. Append one value to each list
in the same session order so all four lists keep equal lengths.
"""

dates = []
hours_slept = []
sleep_qualities = []
notes = []

def lists_are_synchronized():
    """Return whether all four lists contain the same number of fields."""
    return (
        len(dates)
        == len(hours_slept)
        == len(sleep_qualities)
        == len(notes)
    )
