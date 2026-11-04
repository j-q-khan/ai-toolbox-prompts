# Full code: ComfyUI Low VRAM: Run Big Models on a Small GPU

These start-up lines come from ComfyUI's official code and docs (cli_args.py at v0.44.0 and docs.comfy.org), checked 2026-11-04. Run them from the ComfyUI_windows_portable folder for Portable, or from the ComfyUI folder with its virtual environment active for a manual install. On Desktop, put the flag in Manage, then Startup Args.

### Portable: keep 2 GB of VRAM free for other apps
```
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --reserve-vram 2
```

### Manual install: the same
```
python main.py --reserve-vram 2
```

### Manual install: minimal VRAM, when nothing else fits (turns dynamic VRAM off)
```
python main.py --novram
```

### See ComfyUI's own memory report: open this address in your browser on the same computer while ComfyUI runs (8188 is the default port; if Comfy Desktop picked another, use the port in its address bar)
```
http://127.0.0.1:8188/system_stats
```
