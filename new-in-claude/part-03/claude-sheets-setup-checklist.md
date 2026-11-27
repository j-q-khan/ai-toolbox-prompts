# Claude Sheets (beta): setup checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Can you use it?
- [ ] Your plan is Pro, Max, Ultra, Team or Enterprise. Anthropic: "Claude Sheets is available in beta on Pro, Max, Ultra, Team, and Enterprise plans." It isn't on the Free plan.
- [ ] Platforms: web, desktop, Claude for iOS and Claude for Android.
- [ ] Not yet for organizations with HIPAA-ready configurations or with zero data retention for Claude Code. Anthropic: "Sheets aren't covered by zero data retention."

## For the owner (Owners and Primary Owners, Team and Enterprise)
- [ ] Organization settings, then Capabilities: "Cloud code execution and file creation" is on (the admin guide says this comes first).
- [ ] Organization settings, then Artifacts: Artifacts is on.
- [ ] Organization settings, then Artifacts, under Templates: Sheets (beta) is on. Team default: on. Enterprise default: off.
- [ ] Organization settings, then Capabilities: an admin can also turn off Sheets here. Check it hasn't been turned off.
- [ ] Enterprise: once Sheets is on, custom roles can limit it to specific groups. Check that the people who need it are included.

## Make a sheet
- [ ] In any chat: ask for the sheet (claude-sheets-budget-prompt.txt).
- [ ] Or: go to the Artifacts tab, select the "Sheets" tile, and describe the sheet you want, or start with a blank sheet.
- [ ] Say what the sheet is for and what you want to track, and give Claude the numbers you already have. Use made-up or approved numbers only.
- [ ] Check: each edit Claude makes is outlined as it lands, and the formulas stay in the cells.
- [ ] If a change isn't what you wanted: when the card says what Claude updated and shows "Undo", select it to take back only that change. After that, use Version history to restore an earlier version (this also removes edits made after it).

## Work in the sheet
- [ ] Type in cells and write formulas yourself: "Claude Sheets includes over 250 functions."
- [ ] A formula in plain words: type = in a cell, describe it, select "Write this formula", then "Keep" or "Discard".
- [ ] An error: select the cell, then "Fix with Claude", then "Keep" or "Discard".
- [ ] A chart: select cells with numbers, select "Insert chart" in the toolbar (or right-click and select "Make chart"), or describe it and select "Make this chart". Bar, line and pie charts, plus other types Claude can generate.
- [ ] A rule: select "Conditional formatting", type a rule like "red if over budget", and select "Write rules".
- [ ] Ask about cells: select cells, right-click, and select "Ask Claude". In a comment, check "Send to Claude".
- [ ] Also there: sort and filter (right-click), find and replace (Ctrl+H, or Cmd+Shift+H on a Mac), dropdowns, checkboxes and dates (right-click, then Insert), number formats, cell history (right-click, then View history), and on Team and Enterprise, @ to add a person to a cell. Ctrl+/ (Cmd+/ on a Mac) lists the keyboard shortcuts.

## Import, export and share
- [ ] Import a CSV file (such as test-bakery-budget.csv), import from Google Sheets or Excel, start blank, or paste from Excel or Google Sheets.
- [ ] Export: "To download a sheet, export it as an .xlsx or CSV file." To keep working in another tool, use "Send to". PDF export isn't available yet.
- [ ] Sheets start private to you. To share one, open it and click "Share". People with "Can edit" access work on it alongside you and Claude.
- [ ] Pro, Max and Ultra: "Only you" or "Anyone with the link", or invite people by email. Team and Enterprise: "Only people invited", "Anyone at" your organization, or "Anyone with the link" (only when an Owner has turned on External sharing or allowed that artifact).
- [ ] "Anyone with the link": the sheet opens only for people signed in to Claude, who can only view it. People from outside your organization can't add comments to a sheet.

## What it can't do (yet)
- [ ] "Sheets can't pull live data from connected apps, and docs, decks, and dashboards can't use a sheet as a data source." Import or paste the numbers again when they change.
- [ ] Not supported: macros, VBA, Power Query, DAX and print layout. Not available yet: multi-select dropdowns and PDF export.
- [ ] Size: "A sheet can hold over 500,000 filled cells."
- [ ] Install as app (beta, November 24, 2026): "Some artifacts can't be installed, including Claude Docs, Slides, and Sheets."
- [ ] File has to stay in Excel or Google Sheets? Anthropic: "Claude for Excel and Claude for Google Workspace bring Claude to the files you already keep in those apps."

## Usage and what's kept
- [ ] "Claude Sheets counts toward your plan's usage limits, like the rest of your work with Claude." When Claude does the work, it counts toward usage limits.
- [ ] Every sheet you create is saved in the Artifacts tab. How long sheets are kept: not stated on the Sheets help page (2026-11-26).
- [ ] Admin guide: "Uploaded assets are stored persistently, and fall under the same data retention and deletion policies as other Anthropic products for organizations." On Enterprise, a custom retention period can cover artifacts.

## If the Sheets tile isn't there
- [ ] Check the plan (not Free), then the owner's switches above, in order, then custom roles on Enterprise.
- [ ] It works when your sheet opens beside the chat, its formulas show in the cells, and it's in the Artifacts tab afterwards.

Sources: support.claude.com/en/articles/18324300 ; support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans ; support.claude.com/en/articles/9547008 ; claude.com/resources/articles/sheets-whiteboards-data ; claude.com/resources/articles/install-as-app
