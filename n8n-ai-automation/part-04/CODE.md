# Full code: n8n MCP Server: Connect Claude to Your Workflows

Both workflow files from this video, the Claude Desktop settings file, and the steps to connect them, written from n8n's docs (MCP Server Trigger, Call n8n Workflow Tool), n8n's node source and test fixtures at n8n@2.47.7, Anthropic's help pages, the MCP docs and mcp-remote's README (checked 2026-11-16). The JSON files were checked to parse and to match n8n's export layout and node versions; nothing was imported or run for this video.

### 1. weather-lookup-workflow.json
```
{
  "name": "Weather lookup",
  "nodes": [
    {
      "parameters": {
        "workflowInputs": {
          "values": [
            {
              "name": "city"
            }
          ]
        }
      },
      "id": "27ddc471-301a-4839-8022-dcceaf233f9e",
      "name": "When Executed by Another Workflow",
      "type": "n8n-nodes-base.executeWorkflowTrigger",
      "typeVersion": 1.1,
      "position": [
        0,
        0
      ]
    },
    {
      "parameters": {
        "url": "=https://mockingbird.n8n.io/v1/weather/{{ $json.city }}",
        "options": {}
      },
      "id": "63396414-3ae6-45d6-b7ea-aa660c39cdc7",
      "name": "Get city weather",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        220,
        0
      ]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "26facb61-9efb-4c34-909d-c9765bd087cb",
              "name": "report",
              "value": "=The temperature in {{ $json.city }} is {{ $json.temp_c }}°C. It's currently {{ $json.condition }}.",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "00571a89-a256-4d3f-acaa-92daf46536a8",
      "name": "Add weather report",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        440,
        0
      ]
    }
  ],
  "pinData": {},
  "connections": {
    "When Executed by Another Workflow": {
      "main": [
        [
          {
            "node": "Get city weather",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get city weather": {
      "main": [
        [
          {
            "node": "Add weather report",
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

### 2. weather-tools-for-claude.json
```
{
  "name": "Weather tools for Claude",
  "nodes": [
    {
      "parameters": {
        "authentication": "bearerAuth",
        "path": "6f45ed78-238f-4b93-851d-b36ed7aa928c"
      },
      "id": "203bec6f-9ce0-477d-8465-28922f2a2772",
      "name": "MCP Server Trigger",
      "type": "@n8n/n8n-nodes-langchain.mcpTrigger",
      "typeVersion": 2.1,
      "position": [
        0,
        0
      ],
      "webhookId": "6f45ed78-238f-4b93-851d-b36ed7aa928c"
    },
    {
      "parameters": {
        "description": "Gets today's sample weather for one European city from n8n's Mockingbird practice service and returns one sentence with the temperature in C and the conditions. Supported cities, in lower case: amsterdam, athens, barcelona, bergen, berlin, bordeaux, brussels, budapest, cologne, copenhagen, dublin, edinburgh, frankfurt, geneva, gothenburg, hamburg, helsinki, krakow, lisbon, london, lyon, madrid, marseille, milan, munich, naples, nice, oslo, paris, porto, prague, rome, seville, stockholm, turin, valencia, vienna, warsaw, zurich.",
        "workflowId": {
          "__rl": true,
          "mode": "list",
          "value": "",
          "cachedResultName": "Weather lookup"
        },
        "workflowInputs": {
          "mappingMode": "defineBelow",
          "value": {
            "city": "={{ /*n8n-auto-generated-fromAI-override*/ $fromAI('city', 'One supported European city, in lower case, for example lisbon', 'string') }}"
          },
          "matchingColumns": [],
          "schema": [
            {
              "id": "city",
              "displayName": "city",
              "required": false,
              "defaultMatch": false,
              "display": true,
              "canBeUsedToMatch": true,
              "type": "string"
            }
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        }
      },
      "id": "8db44708-4a21-4681-a1e4-234093303b25",
      "name": "Get weather",
      "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
      "typeVersion": 2.2,
      "position": [
        0,
        220
      ]
    }
  ],
  "pinData": {},
  "connections": {
    "Get weather": {
      "ai_tool": [
        [
          {
            "node": "MCP Server Trigger",
            "type": "ai_tool",
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

### 3. claude_desktop_config.json
```
{
  "mcpServers": {
    "n8n-weather": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote@0.16.6",
        "PASTE-YOUR-PRODUCTION-URL-HERE",
        "--header",
        "Authorization:${AUTH_HEADER}"
      ],
      "env": {
        "AUTH_HEADER": "Bearer PASTE-YOUR-TOKEN-HERE"
      }
    }
  }
}
```

### 4. IMPORT-STEPS.txt
```
# Connect Claude Desktop to your own test n8n (n8n 2.47.7, from Parts 1 to 3).
# Written from n8n's docs, Anthropic's help, the MCP docs and mcp-remote's README, checked 2026-11-16.
# Sample data only (Mockingbird). Nothing here was run for the video.

# 1. Install what you need
#    Claude Desktop: https://claude.ai/download
#    Node.js, the LTS version: https://nodejs.org/
#    Check it in PowerShell (Windows) or Terminal (Mac):
node --version

# 2. Import the workflow Claude will call
#    Download weather-lookup-workflow.json from this GitHub folder,
#    or copy its text into Notepad and save it as weather-lookup-workflow.json,
#    with the box called Save as type set to All files.
#    Mac: in TextEdit, choose Format, Make Plain Text first, then save with the .json name.
#    In n8n: Personal, Create workflow, then the workflow menu (the three dots in the canvas header),
#    then Import from File, and choose weather-lookup-workflow.json
#    Save it, then Publish it. A tool can't run an unpublished sub-workflow from a published server.

# 3. Import the server workflow
#    Create another workflow and import weather-tools-for-claude.json the same way.
#    Open Get weather. In the box called Workflow, choose Weather lookup from the list
#    (an imported file can't point at your copy by itself).
#    Check that city is still filled in by the model; if it's empty, click the button
#    at the end of the box, "Let the model define this parameter".

# 4. Make a token and lock the trigger
#    In PowerShell or Terminal, run this and copy the long line it prints:
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
#    Open MCP Server Trigger. Authentication: Bearer Auth (never None).
#    In the credential box choose Create new credential, paste the token into
#    the box called Bearer Token, and save.

# 5. Publish and copy the Production URL
#    Publish the server workflow. At the top of the trigger panel, switch to Production URL
#    and copy it. It looks like http://localhost:5678/mcp/ followed by a random path.
#    Don't copy the Test URL: it only listens while you test in the editor.

# 6. Add the server to Claude Desktop
#    Windows: type %APPDATA%\Claude into File Explorer's address bar.
#    Mac: in Finder press Shift-Command-G and paste ~/Library/Application Support/Claude
#    Open claude_desktop_config.json in Notepad or TextEdit (create it if it isn't there).
#    Creating it in Notepad: set the box called Save as type to All files, so it doesn't end in .txt.
#    Creating it in TextEdit: choose Format, Make Plain Text first.
#    Paste the text of claude_desktop_config.json from this folder.
#    Already have an "mcpServers" section? Add only the "n8n-weather" block inside it,
#    with a comma between server blocks.
#    Replace PASTE-YOUR-PRODUCTION-URL-HERE with your Production URL,
#    and PASTE-YOUR-TOKEN-HERE with your token (keep the word Bearer and the space before it).
#    The header is written Authorization:${AUTH_HEADER} with no spaces, because mcp-remote's README
#    says Claude Desktop on Windows mangles spaces inside args; the space lives in the env value instead.
#    This file now holds the token as plain text: use a token made only for this, and never share the file.

# 7. Restart and test
#    Quit Claude Desktop completely (on Windows, also from the tray icon) and open it again.
#    Click the + in the chat box, then Connectors: n8n-weather should list Get_weather.
#    Ask: What's the weather in Lisbon today?
#    Claude asks before it runs the tool. Pick Allow always only for tools you trust to run unsupervised.
#    In n8n, open the server workflow's Executions tab to see the run (production runs don't show on the canvas).

# If it doesn't work
#    Claude says it couldn't get the weather: publish Weather lookup (n8n returns the error to Claude as the tool's answer).
#    401 or Unauthorized in the log: the token in the config doesn't match the Bearer Auth credential.
#    n8n-weather missing: check the file is valid JSON (commas, quotes), then quit and reopen Claude Desktop.
#    Connection status: Settings, Desktop app, Manage next to Extensions, Local MCP servers
#    (older layout: Settings, Developer).
#    Logs: Windows %APPDATA%\Claude\logs\mcp-server-n8n-weather.log, Mac ~/Library/Logs/Claude/mcp-server-n8n-weather.log

# Switch it off
#    Unpublish Weather tools for Claude in n8n, and remove the n8n-weather block from claude_desktop_config.json.
#    To change the token, edit the Bearer Auth credential and the config file, then restart Claude Desktop.

# Keys never go in a node, a prompt or a public file. What Claude fetches goes to Anthropic
# to be answered: keep work data out unless your employer allows it.
```
