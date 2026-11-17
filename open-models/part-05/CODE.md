# Full code: OpenRouter Tutorial: One API Key for DeepSeek, Qwen, Kimi and Claude

A script and a cheat sheet written for this video from OpenRouter's docs and models API (checked 2026-11-17). The script was not run against OpenRouter; the output shown is an example. ask.py uses Python's standard library only, reads the key from the environment variable OPENROUTER_API_KEY, never prints or saves it, and writes no files. Use a throwaway key with a small credit limit. Test only.

### 1. ask.py
```
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
```

### 2. example-output.txt
```
Example output (not run against OpenRouter: the model is one of the 14 free models listed on 2026-11-17; the reply and token counts are made up to show the layout; the cost field is optional in OpenRouter's docs, which say free models come without cost, so the 0 is assumed, not seen):

python ask.py
Model asked:    openrouter/free
Model answered: google/gemma-4-31b-it:free
Reply:          It's a secret code that identifies you to a service and bills your requests to your account.
Tokens:         16 in, 22 out
Cost (credits): 0

python ask.py qwen/qwen3.8-27b
qwen/qwen3.8-27b isn't a free model, so it spends credits. Add --paid to go ahead.

python ask.py --limits
Free-model requests today (UTC day): 1 used of 50 - 49 left
Credit limit on this key: 5 | left: 5
```

### 3. openrouter-cheatsheet.md
```
# OpenRouter cheat sheet (facts checked 2026-11-17)

Fees, limits, prices and the free model list change. Check each page named below before you rely on a line.

## 1. The key
- [ ] Make a key at openrouter.ai/settings/keys. Give it a name and a credit limit ("We recommend setting a credit limit on every key").
- [ ] Keys start with sk-or-v1-. Keep yours in a password manager. Never put it in code, a file in your folder, a chat or a screenshot.
- [ ] Set it for one window only, then run your script from that same window:
      Windows PowerShell:  $env:OPENROUTER_API_KEY = "sk-or-v1-..."
      Mac Terminal:        export OPENROUTER_API_KEY="sk-or-v1-..."
- [ ] Both last only until you shut that window. Typed this way, the key also lands in the shell's history file.
      To type it without it showing or being saved in history:
      Windows PowerShell:  $env:OPENROUTER_API_KEY = [Net.NetworkCredential]::new('', (Read-Host 'Paste key' -AsSecureString)).Password
      Mac Terminal:        read -rs OPENROUTER_API_KEY && export OPENROUTER_API_KEY
- [ ] If a key leaks, delete it on the keys page and make a new one.

## 2. What it costs (was ... when checked, 2026-11-17)
| Item | OpenRouter's words or figure | Page |
|---|---|---|
| Fee when you buy credits | 5.5% ($0.80 minimum); crypto 5% | openrouter.ai/docs/faq |
| Model prices | "We pass through the pricing of the underlying model providers without any markup" | openrouter.ai/docs/faq |
| Refunds | unused credits within 24 hours; "the platform fees are non-refundable" | openrouter.ai/docs/faq |
| Credits | may expire "after one year of purchase" | openrouter.ai/docs/faq |
| Free models | 50 requests per day; 1000 per day after buying at least 10 credits; 20 requests per minute | openrouter.ai/docs/api/reference/limits |
| Privacy settings | "There are separate settings for paid and free models" (openrouter.ai/settings/privacy) | openrouter.ai/docs/guides/privacy/provider-logging |
| Fallbacks | "a fallback to a paid model incurs charges even though the first model was :free" | openrouter.ai/docs/guides/routing/model-variants/free |

## 3. Model names and list prices, per million tokens in / out (models API, 2026-11-17)
| Model name in your code | In | Out |
|---|---|---|
| openrouter/free (Free Models Router) | $0 | $0 |
| deepseek/deepseek-v4.1-flash | $0.14 | $0.42 |
| deepseek/deepseek-v4-pro | $0.90 | $1.50 |
| qwen/qwen3.8-27b | $0.15 | $1.875 |
| moonshotai/kimi-k3 | $0.192 | $16.00 |
| moonshotai/kimi-k3.1-pro | $0.2403 | $8.4023 |
| anthropic/claude-haiku-5.5 | $0.10 | $0.50 |
| anthropic/claude-sonnet-5.5 | $2.00 | $10.00 |
| anthropic/claude-opus-5.5 | $4.00 | $20.00 |
On 2026-11-17, 14 models ended in :free (two music models were also priced at 0), and none was DeepSeek, Qwen, Kimi or Claude. These are OpenRouter's listed prices; each model's page shows its providers.

## 4. What OpenRouter logs, in its words
- [ ] "We log basic request metadata (timestamps, model used, token counts). Prompt and completion are not logged by default."
- [ ] Opt-in logging of prompts and completions gives "a 1% discount on usage costs".
- [ ] "Providers that do log, or where we have been unable to confirm their policy, will not be routed to unless the model training toggle is switched on." There are "separate settings for paid and free models".
- [ ] Exceptions (data collection page): "OpenRouter retains prompts only when you opt in, or when retention is needed for CSAM review, reporting, and related legal preservation. Requests to Safety Retention endpoints are the exception: OpenRouter or the provider may retain prompts and responses from any request, only to prevent abuse, and not for training."
- [ ] The provider that runs the model still receives your text. Follow your employer's rules on what you paste.

## 5. Claude Code, in each company's words (no setup here)
- [ ] Anthropic: "Anthropic doesn't endorse, maintain, or audit third-party gateway products, and doesn't support routing Claude Code to non-Claude models through any gateway."
- [ ] OpenRouter's Claude Code page: "Claude Code with OpenRouter is only guaranteed to work with the Anthropic first-party provider."

Sources: openrouter.ai/docs/faq ; openrouter.ai/docs/api_reference/authentication ; openrouter.ai/docs/api/reference/limits ; openrouter.ai/docs/guides/routing/model-variants/free ; openrouter.ai/docs/guides/privacy/data-collection ; openrouter.ai/api/v1/models ; openrouter.ai/docs/cookbook/coding-agents/claude-code-integration ; code.claude.com/docs/en/llm-gateway
```
