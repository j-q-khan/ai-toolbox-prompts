# Full code: Vikunja Review: A Self-Hosted Todoist Alternative

Written from Todoist's CSV help (its columns and its 1-is-highest priority) and Vikunja's import help and priority labels (the same in v2.7.1 and v2.8.0), checked 2026-11-04 and 2026-11-05. Use your own export or test data. We ran the script only on a small fake CSV with meta, section, note, blank and labelled rows (2026-11-05); nothing was imported.

### todoist_to_vikunja.py (Python 3, standard library only. Save it in the same folder as your export, renamed todoist.csv, open a terminal there (PowerShell on Windows, Terminal on a Mac) and type: python todoist_to_vikunja.py todoist.csv vikunja-ready.csv (on a Mac, python3))
```
import csv
import os
import sys

# Todoist: 1 is the highest priority (p1). Vikunja: 1 is Low, 4 Urgent, 5 DO NOW.
# First check one task you know is p1. If its PRIORITY is 4 in your file, use
# FLIP = {"4": "4", "3": "3", "2": "2", "1": "1"} instead.
FLIP = {"1": "4", "2": "3", "3": "2", "4": "1"}

if len(sys.argv) != 3:
    sys.exit("Run: python todoist_to_vikunja.py todoist.csv vikunja-ready.csv")
src, dst = sys.argv[1], sys.argv[2]
if not os.path.isfile(src):
    sys.exit("Can't find " + src + ". Save your Todoist export in this folder first.")
kept, left_out = 0, []

with open(src, newline="", encoding="utf-8-sig") as f, \
     open(dst, "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(["title", "description", "priority", "labels", "todoist_date"])
    for row in csv.DictReader(f):
        kind = (row.get("TYPE") or "").strip()
        content = (row.get("CONTENT") or "").strip()
        if not kind and not content:
            continue  # blank line between sections
        if kind != "task":
            # meta, section and note (comment) rows would import as stray tasks
            left_out.append(kind + ": " + content)
            continue
        # Todoist keeps labels in the task name as @label; move them to their own column
        words = content.split()
        labels = [w[1:].strip(",.;:") for w in words if w.startswith("@") and w[1:].strip(",.;:")]
        title = " ".join(w for w in words if not (w.startswith("@") and w[1:].strip(",.;:")))
        date = (row.get("DATE") or "").strip()
        description = (row.get("DESCRIPTION") or "").strip()
        if date:  # keep the original date text, in case it does not import as a date
            description = (description + " (Todoist date: " + date + ")").strip()
        writer.writerow([
            title,
            description,
            FLIP.get((row.get("PRIORITY") or "").strip(), ""),
            ",".join(labels),
            date,
        ])
        kept += 1

print(kept, "tasks written to", dst)
print(len(left_out), "rows left out:")
for line in left_out:
    print("  -", line)
```

### Then, in Vikunja (Settings, then Import, then CSV), match the columns
```
title         = title
description   = description (it also keeps each task's Todoist date as text)
priority      = priority
labels        = labels (the script moves Todoist's @label words here)
todoist_date  = due date, but only if the preview shows real dates;
                otherwise set it to ignore. Repeating dates like
                "every monday" need setting again by hand
```

### Switch checklist
```
[ ] Exported every Todoist list (three dots, Import and export, Export to CSV)
[ ] Completed tasks: not in the export, so keep a copy elsewhere if you need them
[ ] Checked one known p1 task to confirm the priority direction
[ ] Ran the script; read the list of meta, section and note rows it left out
[ ] Imported one list into a test list first and checked the preview
[ ] Subtasks: they arrive flat, so re-nest the important ones
[ ] Phone: Vikunja's app and CalDAV sync are alpha; try them for a week first
[ ] Backups set up before deleting anything (a 30-day trash exists only from Vikunja 2.8.0)
```
