# Full code: n8n AI Agent Tutorial: Build an AI Agent with Claude

The workflow file from this video, the values to paste when you build it by hand, and the steps to import it, written from n8n's docs (AI Agent, Tools Agent, Human-in-the-loop for AI tool calls, Chat Trigger, Chat node), n8n's node source and its own test fixtures at n8n@2.47.7, and Anthropic's docs (checked 2026-11-16). The JSON was checked to parse and to match n8n's export layout and node versions; it was not imported or run for this video.

### 1. weather-agent-workflow.json
```
{
  "name": "Weather Agent",
  "nodes": [
    {
      "parameters": {
        "options": {
          "responseMode": "responseNodes"
        }
      },
      "id": "021f5955-b768-4b8b-93a2-f185647baa9c",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "typeVersion": 1.4,
      "position": [
        0,
        0
      ],
      "webhookId": "50f5f40a-84ae-4753-b92d-3182535c0442"
    },
    {
      "parameters": {
        "options": {
          "systemMessage": "You answer questions about today's weather in European cities. Use the Get weather tool to look it up, with the city in lower case. Only when the user asks you to save, write one sentence with the city, the temperature in C and the conditions, and save it with the Save to weather log tool. Saving needs a person's approval first. If the save is denied, tell the user it was not saved and do not try again.",
          "maxIterations": 5
        }
      },
      "id": "7e8fc814-6f8d-48d1-80ad-d134209196f2",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 3.1,
      "position": [
        260,
        0
      ]
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "claude-sonnet-5-5",
          "cachedResultName": "Claude Sonnet 5.5"
        },
        "options": {}
      },
      "id": "43329805-7da5-45f7-90a8-81c0194d0fcc",
      "name": "Anthropic Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatAnthropic",
      "typeVersion": 1.6,
      "position": [
        120,
        240
      ]
    },
    {
      "parameters": {
        "descriptionType": "manual",
        "toolDescription": "Gets today's sample weather for one European city from n8n's Mockingbird practice service: the city, the temperature in C and the conditions. Supported cities, in lower case: amsterdam, athens, barcelona, bergen, berlin, bordeaux, brussels, budapest, cologne, copenhagen, dublin, edinburgh, frankfurt, geneva, gothenburg, hamburg, helsinki, krakow, lisbon, london, lyon, madrid, marseille, milan, munich, naples, nice, oslo, paris, porto, prague, rome, seville, stockholm, turin, valencia, vienna, warsaw, zurich.",
        "url": "=https://mockingbird.n8n.io/v1/weather/{{ $fromAI('city', 'One supported European city, in lower case, for example berlin', 'string') }}",
        "options": {}
      },
      "id": "aae81364-1c8b-486b-bc11-588f0c831bb2",
      "name": "Get weather",
      "type": "n8n-nodes-base.httpRequestTool",
      "typeVersion": 4.2,
      "position": [
        320,
        240
      ]
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "9f712229-24b2-49dc-901f-94c128d23ed6",
      "name": "Human review",
      "type": "@n8n/n8n-nodes-langchain.chatHitlTool",
      "typeVersion": 1.3,
      "position": [
        520,
        240
      ],
      "webhookId": "a5c2a38f-0e3e-4bae-8a08-37c56b9c91f1"
    },
    {
      "parameters": {
        "descriptionType": "manual",
        "toolDescription": "Saves one sentence about the weather as a new row in the weather log data table, in its report column.",
        "resource": "row",
        "operation": "insert",
        "dataTableId": {
          "__rl": true,
          "mode": "name",
          "value": "weather log"
        },
        "columns": {
          "mappingMode": "defineBelow",
          "value": {
            "report": "={{ $fromAI('report', 'One sentence with the city, the temperature in C and the conditions', 'string') }}"
          },
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
      "id": "f8d50d40-eb5e-4f78-bdcb-3e624ab32a82",
      "name": "Save to weather log",
      "type": "n8n-nodes-base.dataTableTool",
      "typeVersion": 1.1,
      "position": [
        520,
        460
      ]
    },
    {
      "parameters": {
        "operation": "send",
        "message": "={{ $json.output }}",
        "options": {}
      },
      "id": "4fb6c8c6-9344-481a-9ed8-88db93419cdc",
      "name": "Send reply",
      "type": "@n8n/n8n-nodes-langchain.chat",
      "typeVersion": 1.3,
      "position": [
        620,
        0
      ],
      "webhookId": "82f898e8-0bec-4876-89b0-3ab1bd79254a"
    }
  ],
  "pinData": {},
  "connections": {
    "When chat message received": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent": {
      "main": [
        [
          {
            "node": "Send reply",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Anthropic Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Get weather": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Human review": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "Save to weather log": {
      "ai_tool": [
        [
          {
            "node": "Human review",
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

### 2. agent-values.txt
```
# The values to paste while building the Weather Agent by hand (n8n 2.47.7).
# Written from n8n's docs, checked 2026-11-16. Sample data only (Mockingbird).

# AI Agent, Options, System Message:
You answer questions about today's weather in European cities. Use the Get weather tool to look it up, with the city in lower case. Only when the user asks you to save, write one sentence with the city, the temperature in C and the conditions, and save it with the Save to weather log tool. Saving needs a person's approval first. If the save is denied, tell the user it was not saved and do not try again.

# AI Agent, Options, Max Iterations (default 10):
5

# Get weather (HTTP Request tool), the box called URL: set it to Expression, then paste
https://mockingbird.n8n.io/v1/weather/{{ $fromAI('city', 'One supported European city, in lower case, for example berlin', 'string') }}

# Get weather, Description: Set Manually, then paste
Gets today's sample weather for one European city from n8n's Mockingbird practice service: the city, the temperature in C and the conditions. Supported cities, in lower case: amsterdam, athens, barcelona, bergen, berlin, bordeaux, brussels, budapest, cologne, copenhagen, dublin, edinburgh, frankfurt, geneva, gothenburg, hamburg, helsinki, krakow, lisbon, london, lyon, madrid, marseille, milan, munich, naples, nice, oslo, paris, porto, prague, rome, seville, stockholm, turin, valencia, vienna, warsaw, zurich.

# Save to weather log (Data table tool, Insert row, table: weather log), Description: Set Manually, then paste
Saves one sentence about the weather as a new row in the weather log data table, in its report column.

# Save to weather log, the report column: set it to Expression, then paste
{{ $fromAI('report', 'One sentence with the city, the temperature in C and the conditions', 'string') }}

# Send reply (Chat node, Send Message), the box called Message: set it to Expression, then paste
{{ $json.output }}
```

### 3. IMPORT-STEPS.txt
```
# Import the Weather Agent into your own test n8n (n8n 2.47.7, from Parts 1 and 2).
# Written from n8n's and Anthropic's docs, checked 2026-11-16. Sample data only.

# 1. Make a throwaway Anthropic key (Claude Console, platform.claude.com)
#    Settings, API keys, Create key: name it n8n test, leave Linked account on yourself,
#    pick a short expiration, and choose one workspace for it (a key with no workspace must
#    send a workspace ID on every request; n8n's credential sends only the key by default).
#    Settings, Spend limits: set a low Monthly spend limit for your organization.
#    The key is shown only once. Paste it only into n8n's credential store (step 4).
#    If the key ever leaks: Disable it (reversible) or Delete it on the API keys page.

# 2. Check the table it writes to (from Part 2)
#    In n8n: Personal, then the Data tables tab: a table named weather log with a column report.
#    No table yet? Create it: name weather log, then Add Column: report

# 3. Import the workflow
#    Download weather-agent-workflow.json from this GitHub folder.
#    Or copy its text into Notepad and save it as weather-agent-workflow.json,
#    with the box called Save as type set to All files.
#    Mac: in TextEdit, choose Format, Make Plain Text first, then save with the .json name.
#    In n8n: Personal, Create workflow, then the workflow menu (the three dots in the canvas header),
#    then Import from File, and choose weather-agent-workflow.json

# 4. Add your key
#    Open Anthropic Chat Model, then in its credential box choose Create new credential,
#    paste the key into API Key and save. Pick a model from the list if you want another one.

# 5. Test it in the editor
#    Click Open chat under the canvas and type, for example:
#    What's the weather in Lisbon, and please save it to my log?
#    The chat pauses on the review message: Approve saves the sentence, Deny cancels it.
#    Check Personal, Data tables, weather log for the new line.
#    Leave Make Chat Publicly Available off in the Chat Trigger.
#    If a run stops with "Max iterations (5) reached", raise Max Iterations a little
#    in the AI Agent's options (the default is 10).

# 6. When you're done
#    Delete the key in the Claude Console (Settings, API keys).
#    Delete this workflow in n8n if you don't need it.

# Keys never go in a node, a prompt or this file. Every message and tool result goes to Anthropic
# to be answered: keep work data out unless your employer allows it.
```
