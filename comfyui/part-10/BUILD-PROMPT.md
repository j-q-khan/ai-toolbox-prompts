# Claude build prompt: ComfyUI Custom Nodes and Subgraphs

A tested starter custom node in ComfyUI's V3 style, for Claude Code to build. V3 names checked against docs.comfy.org and ComfyUI v0.44.0 (nodes.py loader order, comfy_api) on 2026-11-04. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder outside my ComfyUI install. Start in plan mode.

Goal: build a small, tested starter custom node in ComfyUI's V3 style, Seconds to Frames, that turns a video length in seconds into a valid frame count.
Inputs: ComfyUI's docs pages on docs.comfy.org: custom-nodes/v3_migration, custom-nodes/walkthrough, custom-nodes/backend/lifecycle and registry/specifications. ComfyUI's source at tag v0.44.0 on github.com/Comfy-Org/ComfyUI, especially comfy_api/latest/_io.py. The rule: frames are seconds times FPS plus one, snapped up to 1 plus a whole number of steps (Wan's length moves in steps of 4, LTX's in steps of 8). Optional: the ComfyUI Custom Node Skills plugin (community-made, MIT), which I may install myself with /plugin marketplace add jtydhr88/comfyui-custom-node-skills and then /plugin install comfyui-custom-nodes@comfyui-custom-node-skills, after looking through it.
Steps, in order:
1. Show me your plan and every command, and wait for my yes. Look up every io class and argument you use in comfy_api/latest/_io.py at v0.44.0 and quote the line; don't guess names.
2. Create a folder seconds-to-frames with logic.py holding one plain function, frames_for(seconds, fps, step), with no ComfyUI imports. It returns seconds times fps plus one, rounded up to the next valid count (a deliberate choice, so the clip is at least as long as asked; the Wan and LTX nodes themselves round down, making ((length - 1) // step) + 1 latent frames), and raises a clear error for zero or negative values.
3. Write nodes.py with a thin V3 node: a class SecondsToFrames based on io.ComfyNode, define_schema with node_id SecondsToFrames, display name Seconds to Frames, category utils/video, inputs seconds (float, default 5), fps (int, default 16) and step (int, default 4), and one integer output named frames; a class method execute that calls frames_for and returns io.NodeOutput; a ComfyExtension with an async get_node_list; and comfy_entrypoint. Import from comfy_api.latest only.
4. Write __init__.py that exports comfy_entrypoint and does not define NODE_CLASS_MAPPINGS, with a comment explaining that ComfyUI checks NODE_CLASS_MAPPINGS first and would skip the V3 entrypoint.
5. Write tests with pytest: tests/test_logic.py for 5 seconds at 16 FPS (81), 5 seconds at 24 FPS (121), 4.9 seconds at 16 FPS (snaps up to 81), step 8 for LTX, and the error cases. Add tests/test_node.py that uses pytest.importorskip on comfy_api, so it is skipped outside ComfyUI.
6. Write pyproject.toml following the registry specification, with name seconds-to-frames, version 0.1.0, a licence file, and PublisherId left as a TODO. Write README.md: copy the folder into ComfyUI/custom_nodes, restart ComfyUI, and find the node under utils/video.
7. Create a virtual environment in this folder and install only pytest, after I agree, then run the tests and show me the result.
Safety: test data only. Never copy anything into my ComfyUI folder, never run comfy node publish or any registry command, never use eval or exec, make no network calls from the node, and work only inside this folder. Stop and ask me before running anything that changes data.
Output: logic.py, nodes.py, __init__.py, the tests, pyproject.toml, README.md, and the pytest result.
