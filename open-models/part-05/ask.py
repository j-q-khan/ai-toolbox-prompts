# ask.py: send one question to a model through OpenRouter, then print the reply, the model that
# answered, the tokens used and the cost OpenRouter reports.
# Test only. Written from OpenRouter's API docs (checked 2026-11-17), not run against OpenRouter.
# Standard library only (Python 3.10 or later). No installs.
# The key comes from the environment variable OPENROUTER_API_KEY. The script never prints the key,
# never saves it and writes no files. Use a throwaway key with a small credit limit.
#
# Save this text as ask.py in a new folder. Windows Notepad: File, Save as, set the box called Save as type
# to All files, and name it ask.py. Mac TextEdit: Format, Make Plain Text, before you paste, then save as ask.py.
#
# Set the key first, in the same window you run this from:
#   Windows PowerShell:  $env:OPENROUTER_API_KEY = "sk-or-v1-..."   (gone when you shut the window)
#   Mac Terminal:        export OPENROUTER_API_KEY="sk-or-v1-..."
# Run (on a Mac, type python3 instead of python):
#   python ask.py                                         free: the Free Models Router, openrouter/free
#   python ask.py --limits                                free requests left today, and the key's credit limit
#   python ask.py deepseek/deepseek-v4.1-flash --paid     a paid model: this spends credits
# It sends one model only, never a fallback list: a paid model in a fallback list is billed
# even when the first model was free (OpenRouter's docs).
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

BASE = "https://openrouter.ai/api/v1"
FREE_ROUTER = "openrouter/free"  # picks a free model at random, and falls back only to other free models
QUESTION = "In one sentence, what does an API key do?"


def get_key():
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not key:
        sys.exit("The key isn't set in this window. Set OPENROUTER_API_KEY here (see the top of ask.py), then run it again.")
    # OpenRouter's format: sk-or-v1- and 64 lowercase hex characters. Checking it here also means a stray
    # space or line break can never reach the request header, where Python's error would repeat the key.
    if not re.fullmatch(r"sk-or-v1-[0-9a-f]{64}", key):
        sys.exit("OPENROUTER_API_KEY doesn't look like an OpenRouter key (sk-or-v1- and 64 letters and digits). Copy it again from openrouter.ai/settings/keys.")
    return key


def call(path, key, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(
        BASE + path,
        data=data,
        method="POST" if data else "GET",
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        try:
            error = json.loads(err.read().decode("utf-8")).get("error")
            message = error.get("message", "") if isinstance(error, dict) else str(error or "")
        except (ValueError, AttributeError):
            message = ""
        hints = {  # from OpenRouter's errors page (checked 2026-11-17)
            401: " Check the key at openrouter.ai/settings/keys.",
            402: " Not enough credits for this request.",
            403: " Blocked: the key's own credit limit may be used up, or a guardrail stopped it.",
            404: " That model name wasn't found. Check it at openrouter.ai/models.",
            429: " Rate limited. Free models allow 50 requests a day (1,000 after buying at least 10 credits).",
            503: " No provider fits your routing settings. If you changed them, check openrouter.ai/settings/privacy.",
        }
        sys.exit(f"OpenRouter answered HTTP {err.code}: {message}{hints.get(err.code, '')}")
    except (urllib.error.URLError, TimeoutError, ValueError) as err:
        sys.exit(f"Couldn't reach OpenRouter: {err}")


def show_limits(key):
    data = call("/key", key).get("data") or {}
    free = data.get("free_model_daily_requests") or {}
    print("Free-model requests today (UTC day):", free.get("used", "?"), "used of", free.get("limit", "?"),
          "-", free.get("remaining", "?"), "left")
    limit = data.get("limit")
    print("Credit limit on this key:", "none set" if limit is None else limit,
          "| left:", "no limit" if data.get("limit_remaining") is None else data.get("limit_remaining"))


def ask(key, model):
    # 1000 leaves room for a free model that thinks before it answers; free calls cost nothing
    body = {"model": model, "messages": [{"role": "user", "content": QUESTION}], "max_tokens": 1000}
    reply = call("/chat/completions", key, body)
    choices = reply.get("choices") or [{}]
    text = ((choices[0].get("message") or {}).get("content") or "").strip()
    usage = reply.get("usage") or {}
    print("Model asked:   ", model)
    print("Model answered:", reply.get("model", "?"))
    print("Reply:         ", text or "(no text came back: run it again, and the router may pick another model)")
    print("Tokens:        ", usage.get("prompt_tokens", "?"), "in,", usage.get("completion_tokens", "?"), "out")
    print("Cost (credits):", usage.get("cost", "not reported"))


def main():
    parser = argparse.ArgumentParser(description="One question to one model through OpenRouter.")
    parser.add_argument("model", nargs="?", default=FREE_ROUTER, help="a model name like openrouter/free or qwen/qwen3.8-27b")
    parser.add_argument("--paid", action="store_true", help="allow a model that isn't free (it spends credits)")
    parser.add_argument("--limits", action="store_true", help="show free requests left today and the key's credit limit")
    args = parser.parse_args()
    key = get_key()
    if args.limits:
        show_limits(key)
        return
    is_free = args.model == FREE_ROUTER or args.model.endswith(":free")
    if not is_free and not args.paid:
        sys.exit(f"{args.model} isn't a free model, so it spends credits. Add --paid to go ahead.")
    ask(key, args.model)


if __name__ == "__main__":
    main()
