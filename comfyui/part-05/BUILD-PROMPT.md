# Claude build prompt: ComfyUI Low VRAM: Run Big Models on a Small GPU

A read-only VRAM-fit checker for Claude Code: it lists every model file a ComfyUI workflow needs, with its size, compares them with your graphics memory, and lists smaller official versions from the same Hugging Face repositories. Workflow format checked against the official templates, and the Hugging Face model API checked, on 2026-11-04. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a read-only VRAM-fit checker that lists every model file a ComfyUI workflow needs, with its size, compares the sizes with my graphics memory, and lists smaller official versions of each model.
Inputs: a workflow JSON file and my GPU's VRAM and system RAM in GB, which I type in. For testing, use Comfy's official template flux_dev_full_text_to_image.json from github.com/Comfy-Org/workflow_templates (templates folder, MIT licence), saved into this folder. Optionally, the path of my ComfyUI models folder.
Steps, in order:
1. Show me your plan and every command, and wait for my yes. Ask before downloading the test file.
2. Write a small Python script, vram_fit.py, that loads the workflow and collects every node from the top-level nodes list and from every subgraph under definitions, subgraphs. For each node, keep its type, its widgets_values and its properties models list (name, url, directory).
3. Find each file's size. If I gave a models folder, look for the file there and in its subfolders, read-only, and use its size on disk. Otherwise, for files hosted on huggingface.co, make one read-only GET request per repository to https://huggingface.co/api/models/ followed by the repository name and ?blobs=true, following redirects (some repositories have moved to a new name), cache the reply in a local JSON file, and take the size from the matching file entry. Never download a model file.
4. Group the files by role from their directory or loader: diffusion model, text encoder, VAE, LoRA, other.
5. Compare with my numbers and label each file: "fits in VRAM", "bigger than VRAM: ComfyUI will stream it, expect slower runs", or "bigger than VRAM plus RAM: likely won't run". Say clearly that this is a rough guide, not ComfyUI's own rule.
6. From the same cached repository listing, list other files of the same model whose names contain fp8, int8, nvfp4, Q8, Q6, Q5 or Q4, with their sizes, and the repository's licence from its cardData. Never invent a file that isn't in the listing. GGUF files usually sit in separate third-party repositories: if the diffusion model is FLUX.1 dev or FLUX.1 schnell, also make one read-only GET to the matching city96 repository (city96/FLUX.1-dev-gguf or city96/FLUX.1-schnell-gguf) and label its files "third-party, same licence as the original".
7. Write vram-fit.md with one table of files (name, role, size, label) and one table of smaller versions (name, size, licence, link), plus a note to test any swap with a fixed seed.
Safety: read-only. Never edit the workflow, never download or move a model file, never run the workflow or connect to ComfyUI, make no network calls except those GET requests to huggingface.co/api and the one test download I approve, and work only inside this folder. Stop and ask me before running anything that changes data.
Output: vram_fit.py, vram-fit.md, and a three-line summary of the biggest file and its smallest official alternative.
