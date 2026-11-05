# Claude build prompt: Vikunja API Tutorial: Automate Your Tasks

An overdue-task API client for Claude Code. Read-only first: it lists your lists and overdue tasks with a view-only token, and only adds a task after you type yes. Written from the vikunja.io API docs and the v2.7.1 code, checked 2026-11-04. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a small Python client for Vikunja's v2 API that lists my overdue tasks, oldest first, and can later add a task only when I confirm.
Inputs: a test Vikunja server (for example the Docker install from Part 2, with made-up tasks), its base URL in the environment variable VIKUNJA_URL (like http://localhost:3456), and an API token in VIKUNJA_TOKEN. The token is made under Settings, then API Tokens, with only tasks read_all and projects read_all ticked, and a 30-day expiry. Never ask me to paste the token into the chat.
Steps, in order:
1. Show me the files you'll write and the commands you'll run, and wait for my yes. Use only Python's standard library (urllib, json, os), no installs.
2. Write vikunja_client.py with a function that sends GET requests with the header Authorization: Bearer plus the token from the environment, and stops with a clear message on a 401 or 403 (wrong or under-scoped token). Never print the token.
3. Add list_lists(): GET /api/v2/projects, returning id and title from the items field of the response envelope, following total_pages if there is more than one page.
4. Add list_overdue(): GET /api/v2/tasks with the filter done = false && due_date before now, written with the less-than sign and URL-encoded in the code, plus sort_by=due_date and order_by=asc. Use snake_case field names, not the web page's dueDate. Note in a comment that the API leaves out tasks with no due date unless filter_include_nulls=true.
5. Add a command-line entry: python vikunja_client.py overdue prints due date, list name and title, one task per line, then the total. python vikunja_client.py lists prints the lists.
6. Add add_task(list_id, title), sending POST /api/v2/projects/{id}/tasks with a JSON body containing only the title. It must ask "Create this task? (yes/no)" in the terminal before sending, and, if the server answers 403, explain that the token lacks tasks create and stop; never send a test POST to find out. Don't run it yourself; tell me how.
7. Write a test file that runs list_overdue() against a fake response saved in fixtures/tasks.json (no network), and run only that test.
8. Write README.md: how to make the token, the two environment variables, the three commands, and how to switch to a bot user's token (Settings, then Bot Users, share one list with the bot, make the token there).
Safety: a test server with made-up data only, never real client data. Read-only calls first. No calls to any server but VIKUNJA_URL. Stop and ask me before running anything that changes data.
Output: vikunja_client.py, the test, fixtures/tasks.json, README.md, and a three-line summary.
