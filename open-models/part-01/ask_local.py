# ask_local.py: send one chat message to LM Studio's local server and print the reply.
# Test only. Written from LM Studio's docs (checked 2026-11-16), not run.
# Before running: open LM Studio, load a model, then start the server
# (Developer tab, Start server, or: lms server start --port 1234).
# Run: python ask_local.py            (on a Mac: python3 ask_local.py)
#      uses the first chat model the server lists (it may list downloaded models
#      that LM Studio loads on first use, which can take a while)
# Or:  python ask_local.py model-id   (a model id from: lms ps)
import json
import sys
import urllib.request

BASE = "http://localhost:1234/v1"
QUESTION = "In two sentences, what is a local LLM?"


def call(path, payload=None, timeout=10):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(
        BASE + path, data=data, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def main():
    try:
        models = call("/models").get("data", [])
    except (OSError, ValueError):
        sys.exit("No LM Studio server on localhost:1234. Start it in the Developer tab, "
                 "or run: lms server start --port 1234")
    chat_models = [m["id"] for m in models if "embed" not in m["id"].lower()]
    if len(sys.argv) > 1:
        model = sys.argv[1]
    elif chat_models:
        model = chat_models[0]
    else:
        sys.exit("The server lists no chat models. Load one in LM Studio first.")
    try:
        reply = call(
            "/chat/completions",
            {"model": model, "messages": [{"role": "user", "content": QUESTION}]},
            timeout=300,
        )
        text = reply["choices"][0]["message"]["content"]
    except (OSError, ValueError, KeyError, IndexError, TypeError) as error:
        sys.exit(f"The chat call failed ({error!r}). Pass a model id from lms ps: "
                 "python ask_local.py model-id (python3 on a Mac)")
    print("Model:", model)
    print(text)


if __name__ == "__main__":
    main()
