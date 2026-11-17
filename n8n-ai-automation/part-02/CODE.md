# Full code: n8n Workflow Tutorial: Build Your First Automation

The workflow file from this video, the values to paste when you build it by hand, and the steps to import it, written from n8n's Build your first workflow guide, its export-and-import page and n8n's node source at n8n@2.47.7 (checked 2026-11-16). The JSON was checked to parse and to match n8n's export layout; it was not imported or run for this video.

### 1. weather-log-workflow.json
```
{
  "name": "Weather Log",
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
      "id": "26b8f018-40e0-413a-a71f-b63052b14d57",
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
        "url": "https://mockingbird.n8n.io/v1/weather/berlin",
        "options": {}
      },
      "id": "77429890-2626-4ee4-bdbd-d46882b56ac6",
      "name": "Get Berlin weather",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        240,
        0
      ]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "27550e17-2b6b-4228-9073-b8d68c923e4f",
              "name": "report",
              "value": "=The temperature in {{ $json.city }} is {{ $json.temp_c }}°C. It's currently {{ $json.condition }}.",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "4c155f31-8e40-460b-8201-5002b9b2ed6f",
      "name": "Add weather report",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        480,
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
      "id": "7d4399a5-635c-496f-930b-2260fbb71fec",
      "name": "Save weather log",
      "type": "n8n-nodes-base.dataTable",
      "typeVersion": 1.1,
      "position": [
        720,
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
            "node": "Get Berlin weather",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Berlin weather": {
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

### 2. build-values.txt
```
# The three things to paste while building the Weather Log workflow by hand.
# From n8n's Build your first workflow guide (docs.n8n.io), checked 2026-11-16.

# Get Berlin weather (the HTTP Request node), the box called URL:
https://mockingbird.n8n.io/v1/weather/berlin

# Add weather report (the Edit Fields node), Add Field, the Name box:
report

# The same field's Value box: set it to Expression first, then paste this whole line
The temperature in {{ $json.city }} is {{ $json.temp_c }}°C. It's currently {{ $json.condition }}.
```

### 3. IMPORT-STEPS.txt
```
# Import the Weather Log workflow into your own test n8n (n8n 2.47.7, from Part 1).
# Written from n8n's docs, checked 2026-11-16. Sample data only: no account, no API key, no AI.

# 1. Save the workflow file
#    Quickest: download weather-log-workflow.json from this GitHub folder.
#    Or copy its text into Notepad and save it as weather-log-workflow.json,
#    with the box called Save as type set to All files.
#    Mac: in TextEdit, choose Format, Make Plain Text first, then save with the .json name.

# 2. Make the table it writes to (the workflow finds it by name)
#    In n8n: Personal, then the Data tables tab, then create a data table
#    named weather log, then Add Column: report
#    Skip this and the last node stops with: Data table with name "weather log" not found

# 3. Import it
#    Personal, Create workflow, then the workflow menu (the three dots in the canvas header),
#    then Import from File, and choose weather-log-workflow.json
#    Or open the file, copy all its text, click the empty canvas and press Ctrl+V (Mac: Cmd+V)

# 4. Test it
#    Select Execute under the canvas: four green ticks, 1 item on each wire,
#    and a new line in Personal, Data tables, weather log

# 5. Set your time zone before you publish
#    Workflow menu, Settings, Timezone: pick yours, then Save
#    (self-hosted n8n uses America/New_York unless you set one)

# 6. Publish, so the schedule runs it every day at 8 AM
#    Select Publish in the canvas header. Runs show in the Executions tab.
#    It runs only while n8n is running (the Docker window from Part 1).
#    Changed the hour after publishing? Unpublish, then publish again.

# 7. Stop it
#    The arrow next to Publish, then Unpublish

# Keys and logins: never paste them into a node or this file. Use n8n's credential store
# (Personal, Credentials). Exported workflow files include credential names and IDs:
# check a file before you share it.
```
