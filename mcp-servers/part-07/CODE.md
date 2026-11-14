# Full code: Build Your Own MCP Server in Python (MCP SDK v2)

Written for this video from the MCP Python SDK v2 README and docs (checked 2026-11-14). Use the made-up notes, never your real files. The Python was checked with py_compile and the JSON parsed, for syntax only; nothing was installed or run.

### 1. Make the test folder with two made-up notes, Windows PowerShell (in a new PowerShell window; then save notes_server.py from block 3 into $HOME\notes-server)
```
New-Item -ItemType Directory -Force "$HOME\notes-server\notes", "$HOME\notes-server\.claude" | Out-Null
Set-Location "$HOME\notes-server"
Set-Content -Path notes\welcome.txt -Value "A made-up note for testing the notes server. Nothing private here."
Set-Content -Path notes\ideas.txt -Value "Made-up ideas for testing: try list_notes, then get_note with welcome.txt."
```

### 2. The same on a Mac (in the Terminal app; then save notes_server.py from block 3 into ~/notes-server)
```
mkdir -p "$HOME/notes-server/notes" "$HOME/notes-server/.claude" && cd "$HOME/notes-server"
printf 'A made-up note for testing the notes server. Nothing private here.\n' > notes/welcome.txt
printf 'Made-up ideas for testing: try list_notes, then get_note with welcome.txt.\n' > notes/ideas.txt
```

### 3. notes_server.py, the whole server (Notepad: Save as, the box called Save as type set to All files, name notes_server.py in the notes-server folder; Mac: TextEdit, Format, Make Plain Text, then save it as notes_server.py in notes-server)
```
"""A look-only MCP server for one folder of made-up notes.

MCP Servers, Part 7. Written for the official MCP Python SDK v2 (mcp 2.3.0,
checked 2026-11-14) from the SDK's own docs examples. Checked for syntax only
(py_compile); not run. Use it with dummy notes, never your real files.
"""

import logging
from pathlib import Path

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations

# The only folder this server can see: "notes", next to this file.
NOTES = Path(__file__).parent / "notes"

logger = logging.getLogger(__name__)

mcp = MCPServer("Notes")

LOOK_ONLY = ToolAnnotations(read_only_hint=True, open_world_hint=False)


def note_names() -> list[str]:
    """The .txt files in the notes folder, by name."""
    return sorted(p.name for p in NOTES.glob("*.txt"))


@mcp.tool(annotations=LOOK_ONLY)
def list_notes() -> list[str]:
    """List the notes in the notes folder."""
    return note_names()


@mcp.tool(annotations=LOOK_ONLY)
def get_note(name: str) -> str:
    """Get the text of one note, by its file name, for example ideas.txt."""
    if name not in note_names():
        raise ToolError(f"No note called {name!r}. Call list_notes first.")
    logger.info("Opening note %r", name)
    return (NOTES / name).read_text(encoding="utf-8")


@mcp.resource("notes://index")
def index() -> str:
    """Every note's file name, one per line."""
    return "\n".join(note_names())


if __name__ == "__main__":
    mcp.run()
```

### 4. Test it in the MCP Inspector (in the notes-server folder, Windows or Mac; needs Node.js 22.19.0 or newer; the first time, npx may ask to install the Inspector package, so type y; open the exact address it prints, then stop it with Ctrl+C)
```
uv run --with "mcp[cli]==2.3.0" mcp dev notes_server.py
```

### 5. Add it to Claude Code with the full path (first line Windows PowerShell, second line Mac; then type /mcp inside Claude Code to see notes listed)
```
claude mcp add notes -- uv run --with "mcp[cli]==2.3.0" mcp run "$HOME\notes-server\notes_server.py"
claude mcp add notes -- uv run --with "mcp[cli]==2.3.0" mcp run "$HOME/notes-server/notes_server.py"
```

### 6. notes-server/.claude/settings.json, so Claude Code asks before every call (blocks 1 and 2 already made the .claude folder; Mac: Shift-Command-G to reach the hidden folder)
```
{
  "permissions": {
    "ask": ["mcp__notes__*"]
  }
}
```

### 7. Optional: serve it over Streamable HTTP on your own computer only (the client connects to http://localhost:8000/mcp; don't open it to a network without proper sign-in)
```
uv run --with "mcp[cli]==2.3.0" mcp run notes_server.py --transport streamable-http
```

### 8. Switch it off when you're done
```
# Claude Code, in the notes-server folder:
claude mcp remove notes
# The Inspector or the HTTP line: press Ctrl+C in its terminal window
```
