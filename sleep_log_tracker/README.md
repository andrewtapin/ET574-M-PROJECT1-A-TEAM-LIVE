# Sleep Log Tracker

ET574 section M, Project 1, A-TEAM.
Repository: ET574-M-PROJECT1-A-TEAM-LIVE.

A Python console program for recording sleep sessions and viewing entries and statistics.

## Run

In local VS Code, open sleep_log_tracker/main.py and choose Run Python File in Terminal.
Alternatively, run these commands in a local terminal from the repository root:

```text
cd sleep_log_tracker
python main.py
```

In Codespaces, first run cd sleep_log_tracker from the repository root,
then run python3 main.py from that folder.
Python 3 is required. No third-party packages are needed.

## Menu and inputs

- 1: Add Sleep Entry. Enter a real date as YYYY-MM-DD, hours from 0 through 24,
  whole-number quality from 1 through 5, and optional notes. Decimal hours are accepted.
- 2: View Summary. Shows entry count, total and average hours, best and worst quality.
- 3: View All Entries. Shows each session in entry order with matching fields.
- 4: Exit.

Invalid menu choices repeat the menu. Invalid entry values repeat the relevant prompt.
Surrounding input whitespace is stripped before validation.
Closing input at the menu exits cleanly; closing it during an entry cancels that entry.
No fields are appended until all input is valid. Blank notes display as Notes: None.
On Windows, Ctrl+Z followed by Enter signals closed input.
In Codespaces, use Ctrl+D on an empty input line.

## Parallel lists and storage

data.py stores dates, hours_slept, sleep_qualities and notes in four separate lists.
The same index identifies one session. Session storage does not use dictionaries.
lists_are_synchronized() checks equal lengths. Entry and report functions reject
unequal lengths before changing or reading session data.
Data is held only in memory. Exiting and restarting clears all entries.

## Files and responsibilities

- main.py: Andrew Kirk; menu, routing, startup instructions and exit.
- tracker.py add_entry(): Qingyun Li; date and numeric validation, safe cancellation.
- tracker.py view_all() and view_summary(): Peter Oh; display, calculations and guards.
- data.py: shared storage maintained and reviewed by all three roles.
- README.md: Peter Oh; actual usage, contributions and verification.
- .github/issue_tracking.csv: actual tasks, review findings, commit references and dates.

This practice run uses separate GitHub role accounts with Codex-assisted execution.
Copilot provides review feedback, which is checked against code and actual tests.

## Sample verification

Add 2026-10-07 / 7.5 / 4 / blank notes, 2026-10-08 / 6 / 2 / Woke early,
and 2026-10-09 / 8 / 5 / Rested in one program run.
Expected summary: 3 entries, 21.50 total hours, 7.17 average hours,
best quality 5/5 and worst quality 2/5.
After restart, both reports should say No sleep entries recorded.

## Review and test records

Use three feature pull requests: andrew/menu, qingyun/add-entry and peter/reports.
The last includes final documentation and verification. Actual results and code-review
findings are recorded in the issue tracker. Each student checks Copilot suggestions against the code and actual test results.
Only report passing checks after running them on the current revision.
