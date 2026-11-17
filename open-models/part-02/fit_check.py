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
