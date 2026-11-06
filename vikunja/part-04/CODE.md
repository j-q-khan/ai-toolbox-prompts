# Full code: Vikunja vs Todoist vs Plane

Facts from Todoist's, Plane's and Vikunja's own pricing pages and docs, checked 2026-11-06 (prices change: check the pages). The scores 0 to 3 are our starting suggestions from those facts; change any you disagree with. score.py was run by us only on fake sheets.

### scorecard.csv (open in any spreadsheet app; every weight starts at 0: set each from 0 to 5 for how much that need matters to you)
```
need,weight,todoist,vikunja,plane,fact behind the scores
Polished phone apps,0,3,1,2,Vikunja's app is an alpha; Plane has official iOS and Android apps (plane.so/mobile) that we didn't rate and that don't support its Community Edition yet
Nothing to run or update,0,3,2,3,Todoist is hosted; Plane Cloud is free; Vikunja Cloud is from 4 euros a month
Free for one person,0,2,3,3,Todoist free: 5 personal projects and 3 filter views
Free for a team of 5,0,1,3,3,Todoist shares a personal project with up to 5 people on any plan but a team workspace is Business; Plane Cloud free up to 12 users; Vikunja free to self-host
Data on my own server,0,0,3,3,Todoist is hosted only; Vikunja and Plane can be self-hosted
Open-source licence,0,0,3,2,Vikunja is AGPL; Plane's Community Edition is AGPL but its first-listed self-hosted install is closed source
Kanban and Gantt-style views free,0,1,3,3,Todoist puts calendar and table on Pro; Vikunja has List Table Kanban Gantt; Plane Free has five layouts
Sprints and issue tracking,0,0,0,3,Plane has cycles and modules on Free; Vikunja has no sprints
Runs on a small home server,0,0,3,1,Plane needs 2 CPU cores and 4 GB RAM; Vikunja is one program plus a database
Connect Claude (MCP),0,3,3,3,All three have official MCP servers
```

### score.py (Python 3, standard library only; install Python from python.org/downloads if you don't have it. Save this next to scorecard.csv, open a terminal in that folder (PowerShell on Windows, Terminal on a Mac) and type: python score.py scorecard.csv (on a Mac, python3))
```
import csv
import sys

tools = ["todoist", "vikunja", "plane"]
totals = dict.fromkeys(tools, 0)
if len(sys.argv) != 2:
    sys.exit("Run: python score.py scorecard.csv")
# utf-8-sig and the delimiter check let it read a file saved again by Excel
try:
    with open(sys.argv[1], newline="", encoding="utf-8-sig") as f:
        text = f.read()
except FileNotFoundError:
    sys.exit("Can't find " + sys.argv[1] + ". Save scorecard.csv in this folder first.")
delimiter = ";" if text.count(";") and not text.splitlines()[0].count(",") else ","
for row in csv.DictReader(text.splitlines(), delimiter=delimiter):
    try:
        w = float((row["weight"] or "0").replace(",", ".") or 0)
        for t in tools:
            totals[t] += w * float((row[t] or "0").replace(",", ".") or 0)
    except ValueError:
        sys.exit("Row '" + row["need"] + "': weights and scores must be numbers.")

if not any(totals.values()):
    sys.exit("Set the weights first: every weight is still 0.")
for t, n in sorted(totals.items(), key=lambda kv: kv[1], reverse=True):
    print(t.ljust(8), round(n, 1))
```

### Prices, checked 2026-11-06 (from each official pricing page)
```
Todoist   Free: 5 personal projects, 3 filter views
          Pro: US $5 a month billed yearly, $7 monthly
          Business: US $8 per user a month billed yearly, $10 monthly, plus local tax
Plane     Cloud Free: up to 12 users
          Pro: $6 per seat a month billed yearly, $8 monthly
          Business: $13 yearly, $15 monthly
Vikunja   Self-hosted: free
          Cloud Personal: 4 euros a month
          Cloud Family: 10 euros a month, up to 5 users
```
