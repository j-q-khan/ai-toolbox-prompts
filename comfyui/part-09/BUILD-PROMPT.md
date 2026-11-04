# Claude build prompt: ComfyUI API Tutorial: Run Workflows from Python

A safe Python client for Claude Code to build: it checks your local ComfyUI read-only, plans jobs, and only sends them after you agree. Routes and messages checked against ComfyUI v0.44.0's script_examples, server.py and docs.comfy.org on 2026-11-04. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a small, safe Python client for my own local ComfyUI that queues an exported workflow with new prompts and seeds, waits for each run, checks it worked, and saves the outputs.
Inputs: a workflow I export with the main menu, then File, then Export (API), saved in this folder as workflow_api.json, with my positive prompt node renamed to PROMPT before export (if it sits inside a folded subgraph, I rename the CLIP Text Encode node inside it; API format flattens subgraphs, so that inner node keeps its title). The server address I type in (Portable and manual installs default to 127.0.0.1:8188). A text file prompts.txt with one prompt per line, and a list of seeds. Follow ComfyUI's official script_examples/websockets_api_example.py at tag v0.44.0 and the docs pages API Examples, Server Routes and Server Messages on docs.comfy.org.
Steps, in order:
1. Show me your plan and every command, and wait for my yes. Use Python 3.10 or later and only the standard library plus websocket-client==1.9.2, installed in a virtual environment in this folder after I agree.
2. Write comfy_client.py with a check command that is read-only: GET /system_stats and print the ComfyUI version and devices, then GET /object_info and list any class_type in workflow_api.json that the server doesn't have. Refuse any server that is not 127.0.0.1 or localhost unless I pass --allow-remote, and warn me that ComfyUI's local API has no authentication.
3. Find nodes by _meta.title, never by number. Stop with a clear message if no node is titled PROMPT, if its text input is not plain text, or if no seed or noise_seed number was found. Set seeds only on inputs named seed or noise_seed that hold a number, never on links.
4. Add a plan command that prints every job it would send (prompt, seed) and sends nothing. This is the default.
5. Add a run command that asks me to confirm the batch, then for each job: POST /prompt with a fresh UUID as prompt_id and my client_id; on a 400 reply print node_errors and stop; wait on ws://SERVER/ws?clientId=CLIENT_ID for an executing message whose node is null and whose prompt_id matches; then GET /history/PROMPT_ID and check status, status_str is success. Download every output entry of type output with /view into an outputs folder, named with the prompt's line number and the seed, so files never overwrite each other.
6. Write a log file, runs.csv, with prompt, seed, prompt_id, status and saved files.
7. Write tests with pytest that use a saved sample workflow_api.json and a fake server reply, so they run without ComfyUI.
Safety: test data only. Never call /interrupt, /free, /upload or POST /history, never edit workflow_api.json, never start or stop ComfyUI, never use --listen, never send anything to any other server, and work only inside this folder. Stop and ask me before running anything that changes data.
Output: comfy_client.py, test_comfy_client.py, README.md with the three commands, and a dry-run plan for my prompts.txt.
