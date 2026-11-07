# Full code: Vikunja API Tutorial: Automate Your Tasks

Written from Vikunja's API v2 docs and the v2.8.0 route code, checked 2026-11-06. Use a test server with made-up tasks. VIKUNJA_TOKEN is a look-only token (Read All under Tasks and under Projects); VIKUNJA_WRITE_TOKEN has only Create and Update under Tasks, for a test list. overdue.py was run by us only against a fake local server with dummy tasks (2026-11-06), never a real Vikunja; the other lines were not run.

### vikunja.env (save it next to overdue.py; keep it private: chmod 600 vikunja.env on macOS or Linux; on macOS or Linux save it with Unix line endings, while Git Bash and overdue.py also read a Notepad-saved copy)
```
export VIKUNJA_URL=http://localhost:3456
export VIKUNJA_TOKEN=tk_paste_the_look_only_token_here
export VIKUNJA_WRITE_TOKEN=tk_paste_the_task_writer_token_here
```

### Load it (macOS or Linux terminal, or Git Bash on Windows, in the folder with vikunja.env)
```
. ./vikunja.env
```

### Call 1: your lists (needs Projects: Read All)
```
curl -H "Authorization: Bearer $VIKUNJA_TOKEN" \
  "$VIKUNJA_URL/api/v2/projects"
```

### Call 2: overdue tasks (needs Tasks: Read All; the filter is done = false && due_date before now, in percent codes)
```
curl -H "Authorization: Bearer $VIKUNJA_TOKEN" \
  "$VIKUNJA_URL/api/v2/tasks?filter=done%20%3D%20false%20%26%26%20due_date%20%3C%20now"
```

### Call 3: add a task to your test list (needs Tasks: Create; change 7 to your test list's ID)
```
LIST_ID=7
curl -i -X POST -H "Authorization: Bearer $VIKUNJA_WRITE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Test task from the API"}' \
  "$VIKUNJA_URL/api/v2/projects/$LIST_ID/tasks"
```

### Call 4: tick it off (needs Tasks: Update; change 43 to the new task's ID)
```
TASK_ID=43
curl -X PATCH -H "Authorization: Bearer $VIKUNJA_WRITE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"done": true}' \
  "$VIKUNJA_URL/api/v2/tasks/$TASK_ID"
```

### overdue.py (Python 3, standard library only; run: python overdue.py, or python overdue.py overdue-today.txt to save a copy; on a Mac, python3)
```
import json
import os
import sys
import urllib.error
import urllib.request

# Optional: a file name to save a copy of the list to, e.g. overdue-today.txt
OUT = sys.argv[1] if sys.argv[1:] else None
HERE = os.path.dirname(os.path.abspath(__file__))
# done = false && due_date before now, in percent codes (the API docs use snake_case)
FILTER = "done%20%3D%20false%20%26%26%20due_date%20%3C%20now"


def finish(lines, code=0):
    text = "\n".join(lines)
    print(text)
    if OUT:
        with open(OUT, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    sys.exit(code)


def settings():
    # The environment wins; otherwise read vikunja.env next to this script.
    found = {}
    env_file = os.path.join(HERE, "vikunja.env")
    if os.path.exists(env_file):
        with open(env_file, encoding="utf-8-sig") as f:
            for line in f:
                line = line.strip()
                if line.startswith("export "):
                    line = line[len("export "):]
                if "=" in line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    found[key.strip()] = value.strip().strip('"')
    url = os.environ.get("VIKUNJA_URL") or found.get("VIKUNJA_URL", "")
    token = os.environ.get("VIKUNJA_TOKEN") or found.get("VIKUNJA_TOKEN", "")
    return url.rstrip("/"), token


def get(base, token, page):
    url = (base + "/api/v2/tasks?filter=" + FILTER
           + "&sort_by=due_date&order_by=asc&per_page=50&page=" + str(page))
    request = urllib.request.Request(url, headers={"Authorization": "Bearer " + token})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as e:
        if e.code == 401:
            finish(["Token not accepted (401): it's wrong, expired, or lacks tasks read all."], 1)
        if e.code == 403:
            finish(["Not allowed (403): the token's account can't see those tasks."], 1)
        finish(["Vikunja answered " + str(e.code) + ". Check VIKUNJA_URL."], 1)
    except (urllib.error.URLError, OSError) as e:
        finish(["Can't reach " + base + ": " + str(getattr(e, "reason", e))], 1)
    except ValueError:
        finish(["That answer wasn't Vikunja's API. Check VIKUNJA_URL."], 1)


sys.stdout.reconfigure(errors="replace")
BASE, TOKEN = settings()
if not BASE or not TOKEN:
    finish(["Set VIKUNJA_URL and VIKUNJA_TOKEN, or put them in vikunja.env next to this script."], 1)

first = get(BASE, TOKEN, 1)
tasks = list(first.get("items") or [])
for page in range(2, first.get("total_pages", 1) + 1):
    tasks += get(BASE, TOKEN, page).get("items") or []

lines = [(task.get("due_date") or "")[:10] + "  " + task["title"] for task in tasks]
finish(lines + [str(len(tasks)) + " overdue"])
```

### Every weekday at 8 a.m. on Linux or macOS (crontab -e, then add this line; use your own folder; the list lands in overdue-today.txt)
```
0 8 * * 1-5 cd /home/you/vikunja && /usr/bin/python3 overdue.py overdue-today.txt
```

### Every weekday at 8 a.m. on Windows (type once in PowerShell or Command Prompt; use your own folder; if py isn't found, use the full path to python.exe)
```
schtasks /Create /TN "Vikunja overdue" /SC WEEKLY /D "MON,TUE,WED,THU,FRI" /ST 08:00 /TR "py C:\Users\you\vikunja\overdue.py C:\Users\you\vikunja\overdue-today.txt"
```

### Token checklist
```
[ ] Look-only token: Settings, then API Tokens, only Read All under Tasks and Projects
[ ] Not the Read only preset: it ticks every group, and the script needs two boxes
[ ] An expiry date set (30, 60 or 90 days); Vikunja emails you before it ends
[ ] Saved in a password manager; you only see it once
[ ] Writing gets its own token: Create and Update under Tasks, a test list only
[ ] A 401 means wrong, expired or missing that permission: check the boxes
[ ] Small changes with PATCH, never PUT (a PUT replaces the whole task)
[ ] For automations: a bot user's token (Settings, then Bot Users), sharing only the lists it checks
[ ] Webhooks at home: blocked for private addresses by default, so poll on a schedule
```
