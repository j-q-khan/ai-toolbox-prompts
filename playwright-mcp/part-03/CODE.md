# Full code: How to Install Playwright MCP in Claude Code (Safely)



### 1. Make the test folder (PowerShell on Windows or Terminal on a Mac, the same three lines in both: they make playground in your home folder, where the window opens, step into it, and make .claude inside it; PowerShell lists each new folder, a Mac shows nothing)
```
mkdir playground
cd playground
mkdir .claude
```

### 2. serve.js (from the link in the description; save it in playground)
```
// serve.js: a tiny to-do page for testing Playwright MCP, reachable from this computer only.
// Windows: paste into Notepad, Save as type: All files, name it serve.js, save it in playground in your home folder.
// Mac: TextEdit, Format menu, Make Plain Text BEFORE pasting, then save as serve.js; in the save box press
// Shift-Command-G and type ~/playground, and if it asks which ending to use, keep .js.
// Start it in a second window, inside playground:  node serve.js
// Stop it with Ctrl+C. It reads no files and only answers on 127.0.0.1.
const http = require("http");

const page = `<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Test to-do list</title></head>
<body>
  <h1>My test to-do list</h1>
  <label for="task">New task</label>
  <input id="task" type="text">
  <button id="add">Add</button>
  <ul id="list"></ul>
  <script>
    document.getElementById("add").addEventListener("click", function () {
      var box = document.getElementById("task");
      var text = box.value.trim();
      if (text === "") return;
      var item = document.createElement("li");
      item.textContent = text;
      document.getElementById("list").appendChild(item);
      box.value = "";
    });
  </script>
</body>
</html>`;

const server = http.createServer(function (req, res) {
  res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  res.end(page);
});

server.on("error", function (err) {
  console.error("Could not start the test page: " + err.message);
  console.error("If port 8080 is busy, stop the other program using it and try again.");
  process.exit(1);
});

server.listen(8080, "127.0.0.1", function () {
  console.log("Test page ready: http://localhost:8080 (press Ctrl+C to stop)");
});
```

### 3. .claude/settings.json (from the link in the description; save it as settings.json inside playground/.claude. Windows: Notepad, Save as type: All files. Mac: TextEdit set to plain text before pasting, then Shift-Command-G and type ~/playground/.claude; if it asks which ending to use, keep .json)
```
{
  "permissions": {
    "deny": [
      "mcp__playwright__browser_run_code_unsafe",
      "mcp__playwright__browser_file_upload"
    ],
    "ask": [
      "mcp__playwright__browser_evaluate"
    ]
  }
}
```

### 4. Start the test page (a second PowerShell or Terminal window; leave it open while you work, and press Ctrl+C to stop the page)
```
cd playground
node serve.js
```

### 5. Add Playwright MCP, fixed to v0.0.85 (your first window, still in playground; the same line in PowerShell and Mac Terminal. Everything after -- starts the server, -y means npx doesn't stop to ask, @0.0.85 is one fixed version, --isolated keeps the browser profile in memory, and with no --port nothing listens on the network)
```
claude mcp add playwright -- npx -y @playwright/mcp@0.0.85 --isolated
```

### 6. Start Claude Code in playground, then type /mcp: playwright should say connected (failed the first time? npx may still be downloading, so wait, then pick Reconnect. When you're done: /mcp, pick playwright, choose Disable, and the setup is kept)
```
claude
```

### 7. Remove it for good (type /exit to leave Claude Code, then run this in that same first window, still in playground)
```
claude mcp remove playwright
```
