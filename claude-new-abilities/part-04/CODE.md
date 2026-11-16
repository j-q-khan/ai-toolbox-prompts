# Full code: Claude Graphify: Turn Your Notes and Code into a Knowledge Graph

A checklist and commands written for this video from Graphify's README and code at release v0.9.109 (read as text), PyPI and Anthropic's Claude Code docs, checked 2026-11-15. Not run by us: try it in a test folder with nothing private in it first.

### 1. graphify-checklist.md
```
# Claude Graphify: checklist (checked 2026-11-15)

## Before you install
- Repo: github.com/Graphify-Labs/graphify (its old link redirects here)
- Package: graphifyy on PyPI (double y). Other graphify* packages are not the project's.
  Type it exactly: look-alike package names are a known trick.
- Licence: Apache-2.0; older contributions keep their MIT terms (NOTICE)
- Latest release: 0.9.109, 2026-11-14
- Real use: about 148,000 stars, 14,000 forks, 1,534 closed and 746 open issues;
  7 closed issues sampled: all completed, a team member replied on 5
- Reaches: the folder you point it at. Code is mapped on your computer.
  Docs, PDFs and images go to your Claude Code session's model, or to Google's
  Gemini if GEMINI_API_KEY or GOOGLE_API_KEY is set.
- Telemetry: none (README). Query log: off unless you turn it on (querylog.py).
- Costs: free. The docs pass uses your Claude plan. Graphify Cloud is paid;
  you don't need it. Hide its tips with the environment variable GRAPHIFY_NO_TIPS=1.

## Setup (one test folder)
1. uv (it fetches Python itself if it's missing; graphifyy needs Python 3.10 to 3.14):
   Windows (PowerShell): winget install astral-sh.uv
     (first use may ask you to agree to source terms: type Y)
   Mac (Terminal, uv's own installer): curl -LsSf https://astral.sh/uv/install.sh | sh
2. Install, fixed to the release checked: uv tool install graphifyy==0.9.109
   Not found afterwards? uv tool update-shell, then open a new window.
   uv says no Python version fits (only 3.15 or newer installed)?
   uv tool install graphifyy==0.9.109 --python 3.12
3. Make a test folder with a copy of code or notes you don't mind sharing.
   cd into it (path in double quotes).
4. Folder-only install: graphify install --project
   Writes, in this folder only: .claude/skills/graphify/SKILL.md (plus a
   references folder beside it), .claude/CLAUDE.md, a graphify section in
   CLAUDE.md, and PreToolUse and SessionStart hooks in .claude/settings.json
   (an existing settings.json is merged and backed up as
   settings.json.graphify-bak).
   Don't run plain graphify install: it copies the skill to
   ~/.claude/skills/graphify and adds a line to ~/.claude/CLAUDE.md, which
   Claude Code loads in every session, in every folder (it adds no hooks).
   graphify claude install also writes CLAUDE.md and hooks in the folder you
   run it in.
5. Start Claude Code here: claude. Say yes to trusting the folder.
   If it says auto mode, press Shift+Tab once: manual mode on.
   To keep Manual mode for this folder, open .claude/settings.json (graphify
   wrote its hooks there) and add "permissions": {"defaultMode": "default"}
   beside "hooks", inside the outer braces, with a comma between them.
   Don't replace the file, or the hooks are gone.
6. Type /graphify . and approve its first command (a setup check that only
   runs uv tool install --upgrade graphifyy if it can't find graphify), the
   commands that run Graphify's own Python (graphify-out/.graphify_python)
   and the files it writes into graphify-out in this folder.
   Say no to any other uv tool install --upgrade or pip install, and to
   anything that reaches outside this folder.
   A tip about GEMINI_API_KEY? Ignore it: without a key, Claude does that part.
7. Open graphify-out in File Explorer or Finder and double-click graph.html.
8. Ask: /graphify path "A" "B" or /graphify query "your question"

## Obsidian
- Leave Claude Code with /exit, then in the same window, in the test folder:
  graphify export obsidian writes graphify-out/obsidian (one note per idea).
- In Obsidian: Vault profile (bottom left), Open beside Open folder as vault,
  then choose graphify-out/obsidian.
- Don't point --obsidian-dir at your real vault; use a new folder.

## Keep it fresh
- Code changed: graphify update .   (code only, no model)
- Notes changed: /graphify . --update   (re-extracts changed files; uses the model)

## Remove it
- In the test folder: graphify uninstall --project
- After a global install: graphify uninstall (removes the global skill and its
  line in ~/.claude/CLAUDE.md, plus Graphify's lines and hooks in the folder you
  run it in)
- The program: uv tool uninstall graphifyy
- graphify-out stays until you delete it (graphify uninstall --purge deletes it).
- If the folder had a settings.json before, graphify's backup
  .claude/settings.json.graphify-bak stays too; delete it when you're done.
```

### 2. Commands (Windows PowerShell)
```
winget install astral-sh.uv
uv tool install graphifyy==0.9.109
cd "C:\Users\you\graphify-test"
graphify install --project
claude
```

### 3. Commands (Mac Terminal)
```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install graphifyy==0.9.109
cd "/Users/you/graphify-test"
graphify install --project
claude
```

### 4. Inside Claude Code, then the terminal
```
/graphify .
/graphify path "LoginPage" "Database"
/exit
graphify export obsidian
graphify update .
```

### 5. Remove it (in the test folder)
```
graphify uninstall --project
uv tool uninstall graphifyy
```
