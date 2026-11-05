# Full code: Vikunja API Tutorial: Automate Your Tasks

Written from Vikunja's API v2 docs and the v2.7.1 route code, checked 2026-11-04. Use a test server with made-up tasks and a token with only tasks read_all and projects read_all. Not run by us.

### Three calls with curl (set VIKUNJA_URL and VIKUNJA_TOKEN first)
```
curl -H "Authorization: Bearer $VIKUNJA_TOKEN" "$VIKUNJA_URL/api/v2/projects"
curl -H "Authorization: Bearer $VIKUNJA_TOKEN" "$VIKUNJA_URL/api/v2/tasks?filter=done%20%3D%20false%20%26%26%20due_date%20%3C%20now"
curl -X POST -H "Authorization: Bearer $VIKUNJA_TOKEN" -H "Content-Type: application/json" -d '{"title": "Test task from the API"}' "$VIKUNJA_URL/api/v2/projects/1/tasks"
```

### overdue.py (Python standard library only)
```
import json, os, urllib.request

BASE = os.environ["VIKUNJA_URL"].rstrip("/")
TOKEN = os.environ["VIKUNJA_TOKEN"]
# done = false && due_date before now, URL-encoded
FILTER = "done%20%3D%20false%20%26%26%20due_date%20%3C%20now"
URL = BASE + "/api/v2/tasks?filter=" + FILTER + "&sort_by=due_date&order_by=asc&per_page=50"

req = urllib.request.Request(URL, headers={"Authorization": "Bearer " + TOKEN})
with urllib.request.urlopen(req) as resp:
    page = json.load(resp)

for task in page["items"]:
    print(task["due_date"][:10], task["title"])
print(page["total"], "overdue")
```
