# Claude build prompt: How to Install ComfyUI (Windows and Mac)

A ComfyUI install checker for Claude Code. Read-only: it looks at your computer and writes one report file. Rules checked against docs.comfy.org on 2026-11-04. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a read-only ComfyUI install checker that looks at this computer and recommends Comfy Desktop, ComfyUI Portable (which build) or a manual install, with the reason.
Inputs: this computer's operating system and version, CPU architecture, graphics card name, graphics memory and driver version, RAM, free disk space, and Python version. No files from me.
Steps, in order:
1. Show me every command you plan to run and wait for my yes. Use only commands that look, never ones that change settings or install anything.
2. On Windows, run nvidia-smi if it exists, and nvidia-smi --help-query-gpu to find the field names for the card's name, total memory and driver version. If there is no NVIDIA card, list the display adapters instead.
3. On macOS, check the chip with uname -m (arm64 means Apple Silicon) and the version with sw_vers.
4. Check python --version, total RAM and free disk space.
5. Apply these rules from docs.comfy.org, checked 2026-11-04: Desktop needs Windows 10 or later, or macOS 13 or later on Apple Silicon, at least 4.85 GB of disk and 8 GB of RAM (16 recommended). Portable is Windows only; the standard NVIDIA build is for 20 series and newer, the CUDA 12.6 build for 10 series and older, and there are separate AMD and Intel Portable builds. AMD on Windows needs an RDNA 2 or newer card (RDNA 2, 3, 3.5 or 4). Desktop asks for an NVIDIA driver of 580 or newer. Python 3.13 is recommended for a manual install. Comfy's guide: 24 GB of graphics memory or more handles most things including video, 8 to 24 GB is fine for images, under 8 GB use Comfy Cloud. On a Mac, Comfy says big open models won't run at a workable speed.
6. Write install-check.md with what you found, the recommended install, the download page to use, and anything to fix first, such as an old driver.
Safety: read-only checks only, in this folder, with no installs, downloads, driver changes or settings changes. Never send the results anywhere. Stop and ask me before running anything that changes data.
Output: install-check.md and a three-line summary.
