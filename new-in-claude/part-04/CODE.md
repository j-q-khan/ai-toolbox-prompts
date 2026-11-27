# Full code: Claude Update: Claude Data (Formerly Claude Dashboards), Build a Dashboard From Your Data

The question prompt, the made-up sales table, the example query and the setup checklist, written from Anthropic's help pages "Get started with Claude Data", "Use connectors to extend Claude's capabilities", "Artifacts admin guide for Team and Enterprise plans" and "Share artifacts", and the article "Introducing Claude Whiteboards, Claude Sheets, and Claude Data" (checked 2026-11-26). They were written from the docs, not run for this video.

### 1. claude-data-question-prompt.txt
```
# Paste the question below into any Claude chat, or go to the Artifacts tab, select Data, and paste it there.
# Claude Data is generally available on Pro, Max, Ultra, Team and Enterprise plans. Written from Anthropic's help page, Get started with Claude Data, checked 2026-11-26.
# The lines starting with # are notes for you: don't paste them.
# Connect your data source first: a data warehouse (such as Amazon Redshift, BigQuery, ClickHouse, Databricks or Snowflake) or another app you've connected to Claude.
# Anthropic's tip: say what you want to know, not just what to chart, and if the data is in a specific table or app, name it.
# Fill in the parts in brackets. Use a test warehouse or numbers you're allowed to use, never private data you shouldn't share.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

How do this month's [what you measure] by [what you split it by] compare with last month's? Use the [table name] table in the [warehouse or app name].

# Example, made up (the one in the video):
# How do this month's sales by item compare with last month's? Use the sales table in the Test Bakery warehouse.

# Then, to change it, ask in the chat. For example:
Add a filter for item.
# Or ask for another format: a Scrollyteller, a Visual short or a Visual analysis. For example:
Turn this month's sales numbers into a data story.

# Before you trust a number: open the chart's query and check what it's counting. If it's wrong, tell Claude what to change.
# Before you share: everything starts private to you. With live sharing (beta), people see results from your access, so check what the dashboard shows first.
```

### 2. test-bakery-sales.csv
```
month,item,units_sold
2026-10,Bread,1200
2026-10,Cakes,800
2026-10,Cookies,500
2026-11,Bread,1350
2026-11,Cakes,720
2026-11,Cookies,610
```

### 3. example-chart-query.sql
```
-- Example output, written for the made-up sales table above; not run, and not Claude's own output.
-- Each Claude Data chart shows its own query: open it to check what the chart is counting.
SELECT month, item, SUM(units_sold)
FROM sales
WHERE month IN ('2026-10', '2026-11')
GROUP BY month, item
```

### 4. claude-data-setup-checklist.md
```
# Claude Data (formerly Claude Dashboards): setup checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Can you use it?
- [ ] Your plan is Pro, Max, Ultra, Team or Enterprise. Anthropic: "Claude Data is available on Pro, Max, Ultra, Team, and Enterprise plans." It isn't on the Free plan.
- [ ] Generally available since November 10, 2026, when Claude Dashboards was renamed Claude Data. "Certified queries and live sharing are in beta." Dashboards you already made keep working.
- [ ] Where: Anthropic's launch article says Claude Whiteboards, Sheets and Data "work on web, desktop, and mobile". The artifacts help page's mobile line names designs, decks and docs only, so start on the web or in Claude Desktop.
- [ ] HIPAA-ready organizations: an Owner can turn on Data after accepting the terms, but it isn't covered under the Business Associate Agreement, so keep protected health information out of it. Most artifact types aren't covered by zero data retention (admin guide).

## Connect a data source first
- [ ] A data warehouse, "such as Amazon Redshift, BigQuery, ClickHouse, Databricks, or Snowflake", or another app you've connected to Claude (Anthropic's example: your Salesforce opportunities).
- [ ] Pro, Max and Ultra: Customize, then Connectors, then the + button next to Connectors.
- [ ] Team and Enterprise: an Owner or Primary Owner goes to Organization settings, then Connectors, clicks Browse connectors, selects the connector and clicks Add to your team. Then each person authenticates individually.
- [ ] "Claude inherits each person's permissions from the connected service." Claude sees only what your account can see.
- [ ] Use a test warehouse or numbers you're allowed to use. Never real company data in a test.

## For the owner (Owners and Primary Owners, Team and Enterprise)
- [ ] Organization settings, then Artifacts, under Templates: Data is on. Team default: on. Enterprise: "turns on by default on November 20, 2026, unless an owner has already saved a setting."
- [ ] Under Data in Templates: Certified queries and Live sharing (both beta). These settings are hidden when Data is off. Team default: on. Enterprise default: off.
- [ ] Certified queries: when you turn it on, pick the marketplace and plugin that store your certified queries. If you clear that choice, existing certifications go away (they come back if you select the same plugin again).
- [ ] Live sharing off: people who open a dashboard are asked to connect the data source themselves.
- [ ] Enterprise: owners can limit Claude Data to specific groups with custom roles.
- [ ] Published Claude Data artifacts: Organization settings, then Artifacts, under Published artifacts, filter Type to Data. The Compliance API records when Claude Data artifacts are created, viewed, edited or deleted, but not their content.

## Make a dashboard
- [ ] In any chat, ask your question (claude-data-question-prompt.txt). Or: go to the Artifacts tab, select Data, and describe what you want to make.
- [ ] Say what you want to know, not just what to chart. If the data lives in a specific table or app, name it.
- [ ] Formats: dashboards, Scrollyteller (scrolling stories built from your numbers), Visual short (short videos that walk through your numbers) and Visual analysis (written summaries of your numbers). The help page's first line also names "letters".
- [ ] Dashboards are made for quick, exploratory questions. For deeper analysis, send the dashboard to another tool and continue there.

## Check and change it
- [ ] Each chart shows its query and when its data was last refreshed. Open a chart's query to see how Claude got the number. If it isn't counting what you meant, tell Claude what to change.
- [ ] Ask for changes in the chat ("Add a filter for item"), or click a title, caption or chart to change it yourself.
- [ ] A bad edit: open the dashboard's version history, select a version to preview it, and click Restore. It returns to that version for everyone who opens it. People with view-only access can't edit or restore.

## Refresh, in Anthropic's words
- [ ] Help page: "Claude refreshes a dashboard's data when someone opens it and the data is due for a refresh. It doesn't refresh on a schedule, but Refresh data intelligently re-queries for data based on specified interval and user access patterns."
- [ ] Launch article: "dashboards support caching, and refresh cadences can be set on a per-dashboard basis."
- [ ] The two pages don't fully agree. Trust each chart's last-refreshed time.

## Certified queries (beta)
- [ ] "Certified queries are the official queries your data team has approved." Charts built on them carry a badge. Definitions can also come from dbt, Looker or Cube through existing connectors.
- [ ] Anyone with write access to a Data artifact can certify: open a chart's query and edit it, turn on Certify query, add any instructions in Additional context, click Test, then click Publish. The query shows as certified after a check finishes.
- [ ] To remove a certification: turn off Certify query and click Save. Dashboards that use that query lose their badge.

## Share it safely
- [ ] Everything starts private to you. To share, open it and click Share. Dashboards can also be shared outside your organization, if your plan and owner allow it.
- [ ] Without live sharing, a shared dashboard loads its data with each person's own connections. A viewer who can't access the source sees an error in that part.
- [ ] Live sharing (beta): people in your organization see results from your connection, limited to the exact queries the dashboard needs, which can't change without an editor's approval.
- [ ] To turn it on: open the Sources menu on the dashboard and select Your access next to each connector.
- [ ] Anthropic: "Live sharing runs on your access to the data source. Anyone you share the dashboard with sees those results, even if they don't have access to that source. Check what a dashboard shows before you share it this way."

## Usage and what's kept
- [ ] "Claude Data counts toward your plan's usage limits, like the rest of your work with Claude."
- [ ] Everything you create is saved in the Artifacts tab. How long it's kept: not stated on the Data help page (2026-11-26). On Enterprise, a custom retention period can cover artifacts (admin guide).
- [ ] Not stated on any Anthropic page we checked: limits on query size, number of charts or refreshes.

## If the Data tile isn't there
- [ ] Check the plan (not Free), then the owner's switch above, then custom roles on Enterprise.
- [ ] It works when each chart shows its query and its last-refreshed time, and the dashboard is in the Artifacts tab afterwards.

Sources: support.claude.com/en/articles/17454700 ; support.claude.com/en/articles/11176164 ; support.claude.com/en/articles/16994751 ; support.claude.com/en/articles/17153992 ; support.claude.com/en/articles/9547008 ; claude.com/resources/articles/sheets-whiteboards-data
```
