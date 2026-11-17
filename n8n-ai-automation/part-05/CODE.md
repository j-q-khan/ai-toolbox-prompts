# Full code: n8n Claude Code Tutorial: Build Workflows by Asking

The commands to connect Claude Code to your own n8n, the request from this video, a checklist for before you publish, the skills plugin's install lines, and a reference copy of the workflow the request describes, written from n8n's docs, the n8n-io/skills README, n8n's node source at n8n@2.47.7 and Anthropic's Claude Code docs (checked 2026-11-16). The JSON was checked to parse and to match n8n's export layout and node versions; nothing was imported or run for this video.

### 1. connect-claude-code.txt
```
# Connect Claude Code to your own test n8n through n8n's built-in MCP server.
# n8n 2.13 or later (Part 1 runs 2.47.7). Written from n8n's and Anthropic's docs, checked 2026-11-16.
# Use your test n8n only (Part 1's), never one that runs real work: Claude Code acts with your account.

# 1. In n8n: Settings, Instance-level MCP, Enable MCP access (owner or admin only).
#    Then Connect, the OAuth (recommended) tab, Your client: Claude Code.
#    n8n shows the add command (step 2) with your Server URL already in it: copy it from there.
#    For Part 1's local install the Server URL is:
http://localhost:5678/mcp-server/http
#    Plain http is right for a local install. It is NOT the editor's address from your browser bar.

# 2. In PowerShell (Windows) or Terminal (Mac), in the folder you'll work in:
claude mcp add --transport http n8n http://localhost:5678/mcp-server/http
#    This adds n8n for this folder only (Claude Code's default scope), so start Claude Code here.

# 3. Start Claude Code in the same folder, then sign in:
claude
/mcp
#    Pick n8n and choose Authenticate. On the n8n page that opens, every scope starts ticked;
#    tick "I recognize and trust this URL", then click Allow access.
#    "You do not have sufficient permissions to authorize this request" = MCP access is off in n8n.
#    New workflows Claude Code creates are open to it automatically. To let it edit an existing one:
#    open that workflow, the Workflow menu (...), Settings, and switch on Available in MCP.

# 4. Before you ask for anything: press Shift+Tab until the status bar says manual mode on,
#    so Claude Code asks before every n8n tool call. Answer Yes one call at a time.

# Check it from PowerShell or Terminal:
claude mcp list

# Switch it off: in PowerShell or Terminal, sign out and remove it from Claude Code ...
claude mcp logout n8n
claude mcp remove n8n
#    ... or in n8n: Settings, Instance-level MCP, the MCP status control, Disable, then confirm
#    Disable MCP access (this disconnects every client). To drop one client only: Connected clients, Revoke access.

# Instead of OAuth, n8n's docs also give an API key route (the API key tab in the same dialog).
# OAuth is used here because an API key can't be limited to some tools: it reaches every tool.
# n8n's docs name this server n8n-mcp; it's named n8n here so the commands above still match it,
# and so it can't be confused with the skills plugin's n8n-mcp connection.
# Replace PASTE-YOUR-N8N-MCP-TOKEN with the token n8n shows once, and never share or commit it:
# claude mcp add --transport http n8n http://localhost:5678/mcp-server/http --header "Authorization: Bearer PASTE-YOUR-N8N-MCP-TOKEN"
```

### 2. build-request.txt
```
Build a new n8n workflow called Weather for three cities.
Every day at 8 AM, get the weather for Berlin, Paris and Lisbon
from n8n's Mockingbird practice service (no key needed),
write one sentence per city, and save each one to my weather log data table.
Don't publish it, don't run it, and don't change any other workflow.
Ask me before every n8n tool call, and when you're done, give me the link
and list any credentials n8n assigned to the nodes.
```

### 3. review-checklist.txt
```
# Before you publish a workflow Claude Code built (n8n 2.47.7, checked 2026-11-16)
# 1. Open the link Claude Code gave you. The workflow should be unpublished.
# 2. Click each node and check its settings against what you asked for.
# 3. Check every credential box: n8n assigns credentials you already have to new nodes
#    by itself (HTTP Request nodes are skipped). This workflow needs none: remove any it got.
# 4. Check the trigger's time, and the workflow's time zone in its Settings
#    (Part 1's docker run sets none, so n8n uses New York time).
# 5. Check where it writes: the data table weather log, column report.
# 6. Click Execute under the canvas and look in Personal, Data tables, weather log:
#    three new rows, one per city.
# 7. Only then click Publish yourself.
# Undo: unpublish it, then archive it from the workflow menu.
```

### 4. skills-plugin.txt
```
# Optional: n8n's own skills plugin for Claude Code (n8n-io/skills, Apache 2.0), from its README, checked 2026-11-16.
# Type these inside a claude session:
/plugin marketplace add n8n-io/skills
/plugin install n8n-skills@n8n-io
#    When asked, enter your n8n instance's base URL only; the plugin adds /mcp-server/http itself.
/reload-plugins
/mcp
#    Pick n8n-mcp and choose Authenticate.
# This n8n-mcp is n8n's own connection; a third-party server shares the name, so check which one you have.
# The plugin adds a second connection to the same n8n: turn the first one (n8n) off in /mcp,
# so the tools aren't doubled.
```

### 5. weather-three-cities-workflow.json
```
{
  "name": "Weather for three cities",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "days",
              "triggerAtHour": 8
            }
          ]
        }
      },
      "id": "29358cf6-1246-4d16-a335-a5368803e42a",
      "name": "Every day at 8 AM",
      "type": "n8n-nodes-base.scheduleTrigger",
      "typeVersion": 1.2,
      "position": [
        0,
        0
      ]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "9bbde47f-a36a-445c-bb32-a2c57a4fd9f5",
              "name": "city",
              "value": "={{ ['berlin', 'paris', 'lisbon'] }}",
              "type": "array"
            }
          ]
        },
        "options": {}
      },
      "id": "2c50bdf0-c622-4746-9d48-b74d98d16520",
      "name": "List the cities",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        220,
        0
      ]
    },
    {
      "parameters": {
        "fieldToSplitOut": "city",
        "options": {}
      },
      "id": "fdfb94b6-6e3a-4c37-b9ad-870edb8b03b0",
      "name": "One item per city",
      "type": "n8n-nodes-base.splitOut",
      "typeVersion": 1,
      "position": [
        440,
        0
      ]
    },
    {
      "parameters": {
        "url": "=https://mockingbird.n8n.io/v1/weather/{{ $json.city }}",
        "options": {}
      },
      "id": "29d5c568-4f92-4495-8a57-f3cafc8e625f",
      "name": "Get the weather",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        660,
        0
      ]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "cc69cb78-6102-46e5-8a65-5a96ce382697",
              "name": "report",
              "value": "=The temperature in {{ $json.city }} is {{ $json.temp_c }}°C. It's currently {{ $json.condition }}.",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "0416d73b-fe21-4137-89b0-0de769aa6093",
      "name": "Add weather report",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        880,
        0
      ]
    },
    {
      "parameters": {
        "resource": "row",
        "operation": "insert",
        "dataTableId": {
          "__rl": true,
          "mode": "name",
          "value": "weather log"
        },
        "columns": {
          "mappingMode": "autoMapInputData",
          "value": {},
          "matchingColumns": [],
          "schema": [
            {
              "id": "report",
              "displayName": "report",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "type": "string",
              "canBeUsedToMatch": true
            }
          ]
        },
        "options": {}
      },
      "id": "d36775dd-0158-475b-b6cb-655b450cfcbc",
      "name": "Save weather log",
      "type": "n8n-nodes-base.dataTable",
      "typeVersion": 1.1,
      "position": [
        1100,
        0
      ]
    }
  ],
  "pinData": {},
  "connections": {
    "Every day at 8 AM": {
      "main": [
        [
          {
            "node": "List the cities",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "List the cities": {
      "main": [
        [
          {
            "node": "One item per city",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "One item per city": {
      "main": [
        [
          {
            "node": "Get the weather",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get the weather": {
      "main": [
        [
          {
            "node": "Add weather report",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Add weather report": {
      "main": [
        [
          {
            "node": "Save weather log",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```
