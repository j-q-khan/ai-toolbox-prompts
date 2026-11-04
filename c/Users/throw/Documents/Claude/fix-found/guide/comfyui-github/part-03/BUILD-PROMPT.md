# Claude build prompt: ComfyUI Workflow Explained

A read-only workflow explainer for Claude Code: it turns a ComfyUI workflow JSON file into a plain-English, numbered step list. Node meanings and setting orders checked against docs.comfy.org, the official classic workflow and the shipped default graph (frontend v1.57.6) on 2026-11-04. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a read-only workflow explainer that turns a ComfyUI workflow JSON file into a plain-English, numbered step list.
Inputs: a workflow JSON file. For testing, use the classic text-to-image workflow from Comfy's docs, text-to-image.json at github.com/Comfy-Org/docs (public folder), saved into this folder. Later, any workflow I export with the File menu, then Export.
Steps, in order:
1. Show me your plan and every command, and wait for my yes. Ask before downloading the test file.
2. Write a small Python script, explain_workflow.py, that loads the file and reads its nodes, links and groups. Also read the nodes inside any subgraphs under definitions, subgraphs.
3. Order the nodes by following the links from the loaders to the outputs, so each step comes after the steps it depends on.
4. Name each node's widgets_values using these documented orders: KSampler is seed, control after generate, steps, cfg, sampler name, scheduler, denoise. EmptyLatentImage is width, height, batch size. CLIPTextEncode is the prompt text, and say whether it feeds the positive or the negative input of the sampler. CheckpointLoaderSimple is the checkpoint file name. SaveImage is the filename prefix. UNETLoader is the diffusion model file name and weight type. CLIPLoader is the text encoder file name, its type and device. VAELoader is the VAE file name. EmptySD3LatentImage is width, height, batch size. ModelSamplingAuraFlow is shift. For any other node type, or if a node's widgets_values is not a list, print the raw values and mark it "check this node's docs page". Accept links both as lists [id, from node, from slot, to node, to slot, type] and as objects.
5. For each step, write one plain-English line with the node's job, using these meanings from docs.comfy.org: Load Checkpoint gives MODEL, CLIP and VAE; UNETLoader, CLIPLoader and VAELoader load those three parts from separate files; CLIP Text Encode turns a prompt into conditioning; Empty Latent Image sets the canvas size; KSampler removes noise step by step; VAE Decode turns the latent into pixels; Save Image writes to the output folder.
6. List any groups by title, and the nodes inside each group's box.
7. Write workflow-steps.md with the numbered steps, then a short "settings to try with a fixed seed" list for the sampler.
Safety: read-only. Never edit or overwrite the workflow file, never run it, never connect to a running ComfyUI, and work only inside this folder with the test file or a workflow I choose. Stop and ask me before running anything that changes data.
Output: explain_workflow.py, workflow-steps.md, and a three-line summary of the workflow.
