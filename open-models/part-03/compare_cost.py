# compare_cost.py: send one short, non-private prompt to DeepSeek and to Claude, then print
# each reply's token counts and its cost, worked out from the prices YOU type in.
# Test only. Written from DeepSeek's and Anthropic's API docs (checked 2026-11-16), not run.
# Standard library only. It never prints your keys and writes nothing to disk.
#
# Set the keys ONLY in a new PowerShell or Terminal window, never in the one running Claude Code:
#   Windows PowerShell:  $env:DEEPSEEK_API_KEY = "sk-..."   and   $env:COMPARE_ANTHROPIC_KEY = "sk-ant-..."
#   Mac Terminal:        export DEEPSEEK_API_KEY="sk-..."   and   export COMPARE_ANTHROPIC_KEY="sk-ant-..."
# (Both are gone when the window closes. COMPARE_ANTHROPIC_KEY is named so Claude Code won't pick it up.)
# Optional: COMPARE_ANTHROPIC_WORKSPACE, if Anthropic replies that your key needs a workspace ID.
# Run: python compare_cost.py      (on a Mac: python3 compare_cost.py)
import json
import math
import os
import sys
import urllib.error
import urllib.request

PROMPT = "In two sentences, what is a token in a language model?"  # nothing private
MAX_TOKENS = 200

DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"  # OpenAI format, api-docs.deepseek.com
DEEPSEEK_MODEL = "deepseek-flash"  # or "deepseek-v4-pro"; names from the pricing page, 2026-11-16
CLAUDE_URL = "https://api.anthropic.com/v1/messages"  # docs.claude.com, get started
CLAUDE_MODEL = "claude-haiku-5-5"  # or "claude-sonnet-5-5", "claude-opus-5-5"; models overview, 2026-11-16
CLAUDE_VERSION = "2026-10-21"  # the anthropic-version header, docs.claude.com/en/api/versioning


def ask_price(label):
    # Type the price per 1M tokens from the pricing page, e.g. 0.30 (dollars). Refuses anything else.
    while True:
        raw = input(f"{label} (US dollars per 1M tokens, e.g. 0.30): ").strip().lstrip("$")
        try:
            value = float(raw)
        except ValueError:
            print("  Please type a number, like 0.30")
            continue
        if math.isfinite(value) and value >= 0:
            return value
        print("  Please type a number of 0 or more")


def post(url, headers, body, key):
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        detail = err.read().decode("utf-8", "replace").replace(key, "[your key]")[:300]  # never echo the key
        print(f"  The service answered HTTP {err.code}: {detail}")
    except (urllib.error.URLError, TimeoutError, ValueError) as err:
        print(f"  Couldn't reach it: {err}")
    return None


def ask_deepseek(key):
    body = {
        "model": DEEPSEEK_MODEL,
        "messages": [{"role": "user", "content": PROMPT}],
        "max_tokens": MAX_TOKENS,
        "thinking": {"type": "disabled"},  # thinking is on by default; off keeps this test small
        "stream": False,
    }
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
    data = post(DEEPSEEK_URL, headers, body, key)
    if not data:
        return None
    usage = data.get("usage", {})
    choices = data.get("choices") or [{}]
    text = (choices[0].get("message") or {}).get("content") or ""
    return text, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)


def ask_claude(key):
    body = {
        "model": CLAUDE_MODEL,
        "max_tokens": MAX_TOKENS,
        "messages": [{"role": "user", "content": PROMPT}],
    }
    headers = {"content-type": "application/json", "x-api-key": key, "anthropic-version": CLAUDE_VERSION}
    workspace = os.environ.get("COMPARE_ANTHROPIC_WORKSPACE")
    if workspace:
        headers["anthropic-workspace-id"] = workspace
    data = post(CLAUDE_URL, headers, body, key)
    if not data:
        return None
    usage = data.get("usage", {})
    text = "".join(block.get("text", "") for block in data.get("content", []) if block.get("type") == "text")
    return text, usage.get("input_tokens", 0), usage.get("output_tokens", 0)


def report(name, result, price_in, price_out):
    if not result:
        print(f"{name}: no reply (see the message above).")
        return
    text, tokens_in, tokens_out = result
    cost = tokens_in / 1_000_000 * price_in + tokens_out / 1_000_000 * price_out
    print(f"\n{name}")
    print(f"  Reply: {text.strip()[:300]}")
    print(f"  Tokens: {tokens_in} in, {tokens_out} out")
    print(f"  Cost at the prices you typed: ${cost:.6f}")


def main():
    deepseek_key = os.environ.get("DEEPSEEK_API_KEY")
    claude_key = os.environ.get("COMPARE_ANTHROPIC_KEY")
    if not deepseek_key and not claude_key:
        sys.exit("Set DEEPSEEK_API_KEY and/or COMPARE_ANTHROPIC_KEY in this window first (see the top of this file).")
    print(f"Prompt: {PROMPT}")
    print("Prices: copy them from api-docs.deepseek.com/quick_start/pricing and docs.claude.com (Pricing).")
    if deepseek_key:
        print(f"DeepSeek model {DEEPSEEK_MODEL}: check whether it's peak or off-peak right now.")
        ds_in = ask_price("DeepSeek input (cache miss)")
        ds_out = ask_price("DeepSeek output")
        report(f"DeepSeek ({DEEPSEEK_MODEL})", ask_deepseek(deepseek_key), ds_in, ds_out)
    else:
        print("DEEPSEEK_API_KEY isn't set, so DeepSeek is skipped.")
    if claude_key:
        print(f"\nClaude model {CLAUDE_MODEL}:")
        cl_in = ask_price("Claude input")
        cl_out = ask_price("Claude output")
        report(f"Claude ({CLAUDE_MODEL})", ask_claude(claude_key), cl_in, cl_out)
    else:
        print("COMPARE_ANTHROPIC_KEY isn't set, so Claude is skipped.")
    print("\nInput is priced at the cache-miss rate, so a DeepSeek cache hit would cost a little less.")


if __name__ == "__main__":
    main()
