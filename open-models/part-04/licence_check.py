# licence_check.py: look up a model's licence on Hugging Face and write it into MODEL-LICENCE.md
# in this folder, with the maker's page and today's date.
# Test only. Written from the Hugging Face Hub docs and API (checked 2026-11-17), not run against a real model.
# Standard library only. No key needed; it makes one request to huggingface.co and writes one file.
# It reads the licence field the maker set. It is not legal advice: open the LICENSE file and check it yourself.
#
# Run: python licence_check.py Qwen/Qwen3.5-4B      (on a Mac: python3 licence_check.py Qwen/Qwen3.5-4B)
import datetime
import json
import re
import sys
import urllib.error
import urllib.request

API = "https://huggingface.co/api/models/"  # the Hub's public model API
OUT = "MODEL-LICENCE.md"
DEFAULT_MODEL = "Qwen/Qwen3.5-4B"  # a small Qwen model under Apache-2.0 (checked 2026-11-17)


def fetch(model):
    req = urllib.request.Request(API + model, headers={"User-Agent": "licence-check"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        sys.exit(f"Hugging Face answered HTTP {err.code} for {model}. Check the name, e.g. Qwen/Qwen3.5-4B.")
    except (urllib.error.URLError, TimeoutError, ValueError) as err:
        sys.exit(f"Couldn't reach Hugging Face: {err}")


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODEL
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*", model):
        sys.exit("Give the model as maker/name, e.g. Qwen/Qwen3.5-4B")
    data = fetch(model)
    card = data.get("cardData") or {}
    licence = card.get("license") or "not stated"
    if isinstance(licence, list):  # the field can hold a list
        licence = ", ".join(str(x) for x in licence)
    licence = str(licence)
    name = card.get("license_name")
    link = card.get("license_link")
    page = "https://huggingface.co/" + model
    if link and not str(link).startswith("http"):
        link = f"{page}/blob/main/{link}"  # a link like "LICENSE" points to the file in the repo
    lines = [
        f"# {OUT}",
        "",
        f"- Model: {model}",
        f"- Licence field on Hugging Face: {licence}",
    ]
    if name:
        lines.append(f"- Licence name: {name}")
    lines.append(f"- Licence file: {link or page + '/blob/main/LICENSE'}")
    lines.append(f"- Maker's page: {page}")
    lines.append(f"- Checked: {datetime.date.today().isoformat()}")
    lines.append("")
    if "other" in licence.split(", "):
        lines.append("This is a custom licence. Open the licence file and look for Model as a Service and for")
        lines.append("a rule about showing the model's name before you build a product on it.")
    elif licence == "not stated":
        lines.append("No licence field is set. Don't use the model until you've found its licence file.")
    else:
        lines.append("This is the licence the maker set in the model card. Open the licence file to confirm it.")
    lines.append("Not legal advice: check the licence file yourself.")
    text = "\n".join(lines) + "\n"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"Saved {OUT} in this folder.")


if __name__ == "__main__":
    main()
