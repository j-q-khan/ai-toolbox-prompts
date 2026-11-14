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
