# Full code: ComfyUI Manager: How to Fix Missing Nodes

These start-up lines come from ComfyUI's official docs (docs.comfy.org), checked 2026-11-04. Run them from the ComfyUI_windows_portable folder for Portable, or from the ComfyUI folder with its virtual environment active for a manual install.

### Portable: turn on the Manager (first line once, then start ComfyUI with the second)
```
.\python_embeded\python.exe -m pip install -r ComfyUI\manager_requirements.txt
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --enable-manager
```

### Manual install: turn on the Manager
```
pip install -r manager_requirements.txt
python main.py --enable-manager
```

### Portable: start with every custom node switched off, to test whether a pack is the problem
```
.\python_embeded\python.exe -s ComfyUI\main.py --disable-all-custom-nodes --windows-standalone-build
```

### Manual install: the same test
```
python main.py --disable-all-custom-nodes
```
