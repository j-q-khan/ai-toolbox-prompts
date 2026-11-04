# Claude build prompt: Best AI Tools for Real Estate Agents (Part 2)

- **What it builds:** A private document-to-draft pipeline: Docling turns a dummy HOA or disclosure PDF into Markdown, and a local Ollama model lists the dues and rules, each quoted from the source, with a checklist to verify.
- **What you need:** Claude Code, which needs a paid Claude plan (Pro or higher; Pro was $20 a month billed monthly at the time of checking, 2026-11-03, claude.com/pricing). Python 3.10 or later, Docling and Ollama (Claude checks and tells you what's missing; it doesn't install). An empty test folder and a dummy PDF you make yourself.
- **Safety:** Test data only: made-up listings or a dummy file, never real client, seller or showing details. Work in an empty test folder. Claude looks first and asks before changing anything: it must stop and ask you before running anything that changes data, installs software or writes outside the folder. Check every output yourself; this is not legal advice.

Copy everything below the line into Claude Code.

---

Use this in Claude Code (Pro or higher), in an empty test folder, with a dummy PDF only.

Goal: in a new test folder, set up a private document-to-draft pipeline that turns an HOA or disclosure PDF into a checked summary, using Docling and a local Ollama model, without sending files to the cloud. Inputs: one dummy PDF I'll put in the folder as sample-hoa.pdf, with made-up dues, rules and a table; no real client file. Steps: 1) Check that Python 3.10 or later, Docling and Ollama are installed, and that Ollama's cloud features are off (OLLAMA_NO_CLOUD=1 or disable_ollama_cloud); list anything missing and how to fix it, and don't install or change settings yourself. 2) Run docling on sample-hoa.pdf to make sample-hoa.md and show me any table it found. 3) Write a Modelfile named hoa-check with a SYSTEM line: list dues, assessments, rental, pet and parking rules, quote each source line with its heading, write "not found" for gaps, never guess. 4) Send sample-hoa.md to hoa-check and save summary.md. 5) Show me how to add Docling's MCP server to Claude Desktop's claude_desktop_config.json, but don't edit the file. Safety: work only in the test folder, use only the dummy PDF, never real client data, read-only first, and stop and ask me before running anything that changes data, installs software or creates a model. Output: sample-hoa.md, the Modelfile, summary.md, and a checklist of every summary line to verify against the PDF.
