# Claude build prompt: Vikunja Tutorial: Projects, Kanban and Gantt

A project template generator for Claude Code. It never connects to Vikunja: it writes a CSV for Vikunja's CSV import and a Quick Add Magic text block. Rules checked against the vikunja.io help center on 2026-11-04 and re-checked on 2026-11-06 (Vikunja v2.8.0). Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a small template generator that turns a plain description of a piece of work into a Vikunja-ready CSV file (for Vikunja's CSV import) and a matching Quick Add Magic text block, without touching any Vikunja instance.
Inputs: a text file called brief.txt in this folder, with a few sentences about the work, its start date, its deadline and the people involved, for example a made-up office move. If it doesn't exist, write a fake one first and show it to me.
Steps, in order:
1. Tell me what you'll write and wait for my yes. Never call any Vikunja server or API, and never ask me for a token.
2. Plan the structure from brief.txt: one parent list, three to six sub-lists, five to fifteen tasks each, with labels, a start date, an end date and a due date, and a priority from 1 (low) to 5 (DO NOW). Show me the plan as a table and wait for my yes or edits.
3. Write template.csv with these columns: title, description, project, labels, start_date, end_date, due_date, priority. The project column holds the sub-list name, because Vikunja's CSV import groups tasks into sub-projects by that column. Put several labels in one cell, separated by commas, as the import expects. Use dates as YYYY-MM-DD.
4. Check the file: every row has a title, every date parses, end dates are not before start dates, priorities are 1 to 5, and no cell contains a line break.
5. Write quickadd.txt with the same tasks as Quick Add Magic lines: one task per line, two-space indents for subtasks, *label for labels (quote labels with spaces, like *"waiting on others"), +ListName only for lists that already exist, and !1 to !5 for priority.
6. Write how-to-import.md: in Vikunja, open Settings, then Import from other services, click the CSV tile, upload template.csv, check that each column maps to the right field (title, description, project, labels, start date, end date, due date, priority), and import. Then open the new list's Gantt tab, which needs the start and end dates. Add: to reuse it later, use Duplicate from the list's three-dot menu.
Safety: made-up test data only, in this folder. No network calls, no installs, no Vikunja logins, no API keys. Stop and ask me before running anything that changes data.
Output: template.csv, quickadd.txt, how-to-import.md and a three-line summary.
