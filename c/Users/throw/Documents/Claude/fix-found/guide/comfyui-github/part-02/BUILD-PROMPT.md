# Claude build prompt: ComfyUI Manager: How to Fix Missing Nodes

A read-only missing node finder for Claude Code: it reads a ComfyUI workflow JSON file and lists the custom node packs and model files it needs, before you install anything. Checked against docs.comfy.org, the Comfy Registry API and the ComfyUI-Manager repo on 2026-11-04. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a read-only missing node finder that reads a ComfyUI workflow JSON file and lists the custom node packs and model files it needs, before anything is installed.
Inputs: a workflow JSON file. For testing, use Comfy's official template templates-9grid_social_media-v2.0.json from github.com/Comfy-Org/workflow_templates (MIT licence), saved into this folder. Optionally, the path of my ComfyUI models folder.
Steps, in order:
1. Show me your plan and every command, and wait for my yes. Ask before downloading the test file.
2. Write a small Python script, find_packs.py, that loads the workflow and collects every node from the top-level nodes list and from every subgraph under definitions, subgraphs, nodes. For each node keep its type and its properties cnr_id, ver and models.
3. Skip nodes whose cnr_id is comfy-core. Group the rest by cnr_id. For each pack, make one read-only GET request to https://api.comfy.org/nodes/ followed by the cnr_id, and record its name, repository, status and latest version. Make at most one request per pack. If a request fails or returns 404, record it, mark the pack "not in the registry: check by hand", and keep going. Show status in plain words: NodeStatusActive means active; flag any other status "check by hand".
4. For nodes with no cnr_id, download the ComfyUI-Manager node map from https://raw.githubusercontent.com/Comfy-Org/ComfyUI-Manager/main/extension-node-map.json and list every repository whose node list contains that node type. Download the map once and read it from the local copy after that. Never pick one for me. If none matches, mark it "maybe a core node: update ComfyUI first".
5. Mark each ver as a registry release if it is a dotted number, or a git commit if it is a long string of letters and digits.
6. For each entry in a node's models list, show name, directory and url. If I gave a models folder, check read-only whether a file with that name exists in the matching folder, and also search that folder's subfolders, reporting "found in a subfolder" with the path (ComfyUI's own check only looks at the top level, so it can flag a model as missing when it sits in a subfolder).
7. Write missing-packs.md: one table of packs (registry id, name, repository, status, version in the workflow, latest version, nodes that use it) and one table of model files (name, folder, found, found in a subfolder or missing, link).
Safety: read-only. Never install a pack, never run the workflow, never call any endpoint except those GET requests, never edit ComfyUI or ComfyUI-Manager settings, and work only inside this folder with the test file or a workflow I choose. Stop and ask me before running anything that changes data.
Output: find_packs.py, missing-packs.md, and a short note on which packs to check by hand before installing.
