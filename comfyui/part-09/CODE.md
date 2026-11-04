# Full code: ComfyUI API Tutorial: Run Workflows from Python

Adapted from ComfyUI's official script_examples/websockets_api_example.py (ComfyUI v0.44.0, tag commit 2c75dc1b, 2026-11-03) and the docs pages API Examples and Server Routes, checked 2026-11-04. Written from the official code and docs, not run by us. Start ComfyUI first, open your workflow, rename the positive prompt node to PROMPT (if your prompt box is on a folded subgraph, click Enter Subgraph and rename the CLIP Text Encode node inside), then use the main menu, File, then Export (API), and save the file as workflow_api.json next to this script.

### Install the one library it needs (Python 3.10 or later)
```
pip install websocket-client==1.9.2
```

### Start ComfyUI with no browser window (Portable, from the ComfyUI_windows_portable folder)
```
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --disable-auto-launch
```

### Start ComfyUI with no browser window (manual install, from the ComfyUI folder)
```
python main.py --disable-auto-launch
```

### comfy_client.py
```
# comfy_client.py: run a ComfyUI workflow from Python and save its outputs.
# Adapted from ComfyUI's script_examples/websockets_api_example.py (v0.44.0).
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid

import websocket  # pip install websocket-client==1.9.2

SERVER = "127.0.0.1:8188"  # Portable and manual installs; copy yours from the browser's address bar, without http://
WORKFLOW_FILE = "workflow_api.json"  # saved with File, then Export (API)
PROMPT_TITLE = "PROMPT"  # the title you gave your positive prompt node
SEEDS = [1, 2, 3]
CLIENT_ID = str(uuid.uuid4())


def get_json(path):
    with urllib.request.urlopen(f"http://{SERVER}{path}") as response:
        return json.loads(response.read())


def queue_prompt(workflow, prompt_id):
    body = {"prompt": workflow, "client_id": CLIENT_ID, "prompt_id": prompt_id}
    request = urllib.request.Request(
        f"http://{SERVER}/prompt",
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as error:
        print("ComfyUI refused the workflow:", error.read().decode("utf-8"))
        sys.exit(1)


def find_node(workflow, title):
    for node_id, node in workflow.items():
        if node.get("_meta", {}).get("title") == title:
            return node_id
    sys.exit(f'No node titled "{title}". Rename your prompt node, then export again.')


def set_seed(workflow, seed):
    changed = 0
    for node in workflow.values():
        inputs = node.get("inputs", {})
        for key in ("seed", "noise_seed"):
            if isinstance(inputs.get(key), int):
                inputs[key] = seed
                changed += 1
    if changed == 0:
        sys.exit("No seed or noise_seed number found, so every run would be the same.")


def wait_until_done(ws, prompt_id):
    while True:
        message = ws.recv()
        if isinstance(message, str):
            data = json.loads(message)
            if data["type"] == "executing":
                info = data["data"]
                if info["node"] is None and info["prompt_id"] == prompt_id:
                    return


def save_outputs(prompt_id, seed):
    entry = get_json(f"/history/{prompt_id}")[prompt_id]
    status = entry.get("status") or {}
    if status.get("status_str") != "success":
        print("Run failed:", json.dumps(status.get("messages", []), indent=2))
        return []
    saved = []
    for node_output in entry["outputs"].values():
        for items in node_output.values():
            if not isinstance(items, list):
                continue
            for item in items:
                if not isinstance(item, dict) or item.get("type") != "output":
                    continue
                if "filename" not in item:
                    continue
                query = urllib.parse.urlencode({
                    "filename": item["filename"],
                    "subfolder": item.get("subfolder", ""),
                    "type": "output",
                })
                with urllib.request.urlopen(f"http://{SERVER}/view?{query}") as response:
                    data = response.read()
                name = f"seed{seed}_" + os.path.basename(item["filename"])
                with open(name, "wb") as file:
                    file.write(data)
                saved.append(name)
    return saved


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) or "a lighthouse at dawn, watercolour"
    with open(WORKFLOW_FILE, encoding="utf-8") as file:
        workflow = json.load(file)
    inputs = workflow[find_node(workflow, PROMPT_TITLE)]["inputs"]
    if not isinstance(inputs.get("text"), str):
        sys.exit("The PROMPT node has no text box. Rename a CLIP Text Encode node instead.")
    inputs["text"] = text

    ws = websocket.WebSocket()
    ws.connect(f"ws://{SERVER}/ws?clientId={CLIENT_ID}")
    try:
        for seed in SEEDS:
            set_seed(workflow, seed)
            prompt_id = str(uuid.uuid4())
            reply = queue_prompt(workflow, prompt_id)
            print("Queued", prompt_id, "seed", seed, "position", reply.get("number"))
            print("Waiting for", prompt_id)
            wait_until_done(ws, prompt_id)
            print("Saved:", save_outputs(prompt_id, seed))
    finally:
        ws.close()
```

### Run it (ComfyUI must already be running)
```
python comfy_client.py a lighthouse at dawn, watercolour
```
