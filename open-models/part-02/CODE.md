# Full code: Best Local LLM for 8GB or 16GB: Pick a Model That Fits Your Computer

A checklist and a memory script written for this video from LM Studio's model pages and docs, Ollama's library page and Hugging Face's docs (checked 2026-11-16). Nothing was installed or run on a real model; the output shown is an example. fit_check.py only reads your memory size and makes no network calls. Test only.

### 1. model-fit-checklist.md
```
# Pick a local model that fits your memory: checklist (facts checked 2026-11-16)

## 1. Know your memory
- [ ] Mac (Apple's M-series chip): Apple menu, About This Mac, Memory. Apple calls it one "single pool", so this one number is the one to match.
- [ ] Windows: Ctrl+Shift+Esc, Task Manager, Performance. Memory is your RAM. If you have a graphics card, GPU, Dedicated GPU memory is its VRAM.

## 2. Read a model's name
- [ ] The B is billions of parameters: Qwen3.5-9B has about 9 billion.
- [ ] A3B means 3 billion active parameters. Qwen3.6-35B-A3B still needs room for all 35 billion (Hugging Face's MoE explainer: "all experts are loaded in memory").
- [ ] Q4, Q8 (or 4bit, 8bit for Mac MLX copies) is the quantisation: the lower the number, the smaller the file. LM Studio's docs: "Choose a 4-bit option or higher if your machine is capable enough for running it."
- [ ] Sizes on Ollama's library page for Qwen3.5 9B: 19GB (bf16), 10GB (q8_0), 6.6GB (q4_K_M).

## 3. Check what it needs
- [ ] Go to lmstudio.ai/models, open the model, read "Minimum system memory".
- [ ] Qwen3.5-2B: 2 GB. Qwen3.5-4B: 4 GB. Qwen3.5-9B: 7 GB. Qwen3.6-27B: 16 GB. Qwen3.6-35B-A3B: 20 GB. (Checked 2026-11-16.)
- [ ] Rule of thumb from the video (not LM Studio's): keep about a quarter of your memory free for your system and apps. On 8 GB start with the 4B; on 16 GB the 9B leaves room.
- [ ] LM Studio's docs on 8GB Macs: "stick to smaller models and modest context sizes".

## 4. Download it in LM Studio
- [ ] Discover tab (Ctrl+2 on Windows, Cmd+2 on a Mac). Search for the model, for example Qwen3.5 9B.
- [ ] Pick a 4-bit download option (Q4_K_M, or 4bit on a Mac), click download.
- [ ] Chat tab: load it from the bar that says Select a model to load. A steady reply usually means it fits; a crawl usually means it's too big.
- [ ] Mid level: after downloading, `lms load --estimate-only <model_key>` (key from `lms ls`) prints LM Studio's memory estimate without loading the model.

## 5. Download safely from Hugging Face (mid level)
- [ ] Use the maker's own page: huggingface.co/Qwen for Qwen. The Qwen3.5 and Qwen3.6 sizes above are safetensors files under Apache-2.0.
- [ ] LM Studio's GGUF and MLX copies come from huggingface.co/lmstudio-community; each model page on lmstudio.ai/models names its copy under Sources.
- [ ] Prefer safetensors over pickle files. Hugging Face: "There are dangerous arbitrary code execution attacks that can be perpetrated when you load a pickle file."
- [ ] The verified badge is a domain setting, not a safety rating. When checked, deepseek-ai had it; Qwen and lmstudio-community didn't.
- [ ] Shortcut: LM Studio's Discover search box takes a full Hugging Face link.

Sources: lmstudio.ai/models/qwen/qwen3.5-9b (and the other model pages) ; lmstudio.ai/docs/app/basics/download-model ; lmstudio.ai/docs/app/system-requirements ; lmstudio.ai/docs/cli/local-models/load ; ollama.com/library/qwen3.5/tags ; huggingface.co/docs/hub/security-pickle ; huggingface.co/docs/safetensors ; huggingface.co/docs/hub/enterprise-advanced-security ; huggingface.co/blog/moe ; apple.com/newsroom/2020/11/apple-unleashes-m1
```

### 2. fit_check.py
```
# fit_check.py: compare your computer's memory with the memory LM Studio lists for each Qwen size.
# Test only. Written from LM Studio's model pages (checked 2026-11-16), not run on a real model.
# It only reads your memory size. No network calls, no downloads, nothing written to disk.
# Run: python fit_check.py              (on a Mac: python3 fit_check.py)
# Or:  python fit_check.py 16           (pretend you have 16 GB, to compare)
import ctypes
import math
import platform
import shutil
import subprocess
import sys

# "Minimum system memory" from lmstudio.ai/models/qwen/<model>, checked 2026-11-16.
# Re-check the pages before you rely on them: the figures can change.
MODELS = [
    ("Qwen3.5-2B", 2),
    ("Qwen3.5-4B", 4),
    ("Qwen3.5-9B", 7),
    ("Qwen3.6-27B", 16),
    ("Qwen3.6-35B-A3B", 20),
]
ROOM_SHARE = 0.25  # the video's rule of thumb, not LM Studio's: keep a quarter of memory free


def total_memory_gb():
    system = platform.system()
    if system == "Windows":
        class MemoryStatus(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
            ]
        status = MemoryStatus()
        status.dwLength = ctypes.sizeof(MemoryStatus)
        if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
            return None
        return status.ullTotalPhys / 1024 ** 3
    if system == "Darwin":
        try:
            out = subprocess.run(["sysctl", "-n", "hw.memsize"],
                                 capture_output=True, text=True, timeout=10, check=True)
            return int(out.stdout.strip()) / 1024 ** 3
        except (OSError, ValueError, subprocess.SubprocessError):
            return None
    return None


def nvidia_memory_gb():
    # Only NVIDIA cards report through nvidia-smi; others: read Task Manager, Performance, GPU.
    if not shutil.which("nvidia-smi"):
        return None
    try:
        out = subprocess.run(["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader,nounits"],
                             capture_output=True, text=True, timeout=10, check=True)
        return int(out.stdout.split()[0]) / 1024
    except (OSError, ValueError, IndexError, subprocess.SubprocessError):
        return None


def verdict(need, total):
    left = total - need
    if left < 0:
        return "too big"
    if left < total * ROOM_SHARE:
        return "tight"
    return "leaves room"


def main():
    if len(sys.argv) > 1:
        try:
            total = float(sys.argv[1])
        except ValueError:
            sys.exit("Give your memory as a number of GB, for example: python fit_check.py 16 (python3 on a Mac)")
        if not math.isfinite(total) or total <= 0:
            sys.exit("Give a memory size above 0 GB, for example: python fit_check.py 16 (python3 on a Mac)")
        print(f"Pretending your computer has {total:g} GB of memory.")
    else:
        total = total_memory_gb()
        if not total:
            sys.exit("Couldn't read your memory. Check it by hand (Mac: Apple menu, About This Mac; "
                     "Windows: Task Manager, Performance, Memory), then run: python fit_check.py 16 (python3 on a Mac)")
        print(f"Your computer reports {total:.1f} GB of memory; rounded to {round(total)} GB below.")
        total = round(total)
        vram = nvidia_memory_gb()
        if vram:
            print(f"Your NVIDIA graphics card has about {vram:.1f} GB of its own memory (VRAM).")
        elif platform.system() == "Windows":
            print("Graphics memory: not read. See Task Manager, Performance, GPU, Dedicated GPU memory.")
    print("Minimum system memory from LM Studio's model pages (checked 2026-11-16):")
    for name, need in MODELS:
        print(f"  {name:<16} minimum {need:>2} GB   {verdict(need, total)}")
    print("'Tight' and 'leaves room' are a rule of thumb, not LM Studio's words.")


if __name__ == "__main__":
    main()
```

### 3. example-output.txt
```
Example output (a pretend 16 GB computer; figures from LM Studio's model pages, checked 2026-11-16):
Pretending your computer has 16 GB of memory.
Minimum system memory from LM Studio's model pages (checked 2026-11-16):
  Qwen3.5-2B       minimum  2 GB   leaves room
  Qwen3.5-4B       minimum  4 GB   leaves room
  Qwen3.5-9B       minimum  7 GB   leaves room
  Qwen3.6-27B      minimum 16 GB   tight
  Qwen3.6-35B-A3B  minimum 20 GB   too big
'Tight' and 'leaves room' are a rule of thumb, not LM Studio's words.
```
