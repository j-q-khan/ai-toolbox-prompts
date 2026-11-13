# Full code: Chrome DevTools MCP with Claude Code: Find Why a Page Is Slow



### 1. Add Chrome DevTools MCP with four flags (your first window, in playground; type /exit first if Claude Code is open. The same line in PowerShell and Mac Terminal)
```
claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@1.13.0 --isolated --no-usage-statistics --no-performance-crux --javascriptEvaluation=false
```

### 2. serve-slow.js (from the link in the description; save it in playground, next to serve.js)
```
// serve-slow.js: Part 3's to-do page, made slow on purpose for a performance trace, from the link in the description.
// Windows: paste into Notepad, Save as type: All files, name it serve-slow.js, save it in playground, next to serve.js.
// Mac: TextEdit, Format menu, Make Plain Text BEFORE pasting, then save as serve-slow.js; in the save box press
// Shift-Command-G and type ~/playground, and if it asks which ending to use, keep .js.
// Stop serve.js first (Ctrl+C in its window), because both answer on port 8080.
// Start it in your second window, inside playground:  node serve-slow.js
// The hidden problem: the page loads /slow.js at the top, and this server holds that script back for 3 seconds.
// It also asks for /logo.png, which doesn't exist, so the browser logs a 404 error.
// It reads no files and only answers on 127.0.0.1. Stop it with Ctrl+C.
const http = require("http");

const page = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Test to-do list</title>
  <script src="/slow.js"></script>
</head>
<body>
  <h1>My test to-do list</h1>
  <img src="/logo.png" alt="">
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

const slowScript = 'console.log("slow.js arrived after a 3 second wait");\n';

const server = http.createServer(function (req, res) {
  if (req.url === "/slow.js") {
    setTimeout(function () {
      res.writeHead(200, { "Content-Type": "text/javascript; charset=utf-8" });
      res.end(slowScript);
    }, 3000);
    return;
  }
  if (req.url === "/" || req.url === "/index.html") {
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    res.end(page);
    return;
  }
  res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
  res.end("Not found");
});

server.on("error", function (err) {
  console.error("Could not start the slow test page: " + err.message);
  console.error("If port 8080 is busy, stop serve.js (Ctrl+C in its window) and try again.");
  process.exit(1);
});

server.listen(8080, "127.0.0.1", function () {
  console.log("Slow test page ready: http://localhost:8080 (press Ctrl+C to stop)");
});
```

### 3. Start the slow page, then Claude Code (the page in your second window after Ctrl+C stops serve.js, Claude in the first, both in playground; then type /mcp and chrome-devtools should say connected)
```
node serve-slow.js
claude
```

### 4. check-site.js, the new version (from the link in the description; it replaces Part 4's file inside playground/.claude)
```
// check-site.js: a PreToolUse hook for Playwright MCP and Chrome DevTools MCP, from the link in the description.
// It replaces Part 4's check-site.js. Save it as check-site.js inside playground/.claude, next to settings.json.
// Windows: paste into Notepad, Save as type: All files. Mac: TextEdit, Format menu, Make Plain Text
// BEFORE pasting, then in the save box press Shift-Command-G and type ~/playground/.claude (keep .js).
// Claude Code runs it with node before each browser_navigate or browser_tabs call (Playwright MCP) and each
// navigate_page or new_page call (Chrome DevTools MCP), and hands it the call as JSON. Exit 0 lets the call go
// on to your normal permission rules; exit 2 blocks it, and Claude sees the message. It checks ONLY the site
// named in the call. It can't see a click on a link, a redirect, or a page's own scripts, so it is not a wall
// around the browser.
// Edit ALLOWED to add a site you test (scheme, host and port, no path).
const ALLOWED = ["http://localhost:8080", "http://127.0.0.1:8080"];

function block(reason) {
  process.stderr.write("Blocked by .claude/check-site.js: " + reason + "\n");
  process.exit(2);
}

let raw = "";
process.stdin.setEncoding("utf8");
process.stdin.on("data", function (chunk) { raw += chunk; });
process.stdin.on("end", function () {
  let call;
  try { call = JSON.parse(raw); } catch (e) { return block("the tool call could not be parsed."); }
  if (!call || typeof call !== "object") return block("the tool call could not be parsed.");
  const input = call.tool_input || {};

  // browser_tabs lists, selects and closes tabs too; only a new tab with an address is checked.
  if (call.tool_name === "mcp__playwright__browser_tabs" && !input.url) process.exit(0);

  // navigate_page also reloads, and goes back or forward; those calls name no site, so they go through.
  if (call.tool_name === "mcp__chrome-devtools__navigate_page" &&
      (input.type === "reload" || input.type === "back" || input.type === "forward") && !input.url) process.exit(0);

  if (typeof input.url !== "string" || input.url === "") return block("no address was given.");
  let origin;
  try { origin = new URL(input.url).origin; } catch (e) { origin = "null"; }
  if (origin === "null") return block("that is not a full web address, like http://localhost:8080.");
  if (ALLOWED.indexOf(origin) !== -1) process.exit(0);
  block(origin + " is not on the allowed list. Only " + ALLOWED.join(" and ") + " are allowed.");
});
```

### 5. .claude/settings.json, the new version (from the link in the description; it replaces Part 4's file in playground/.claude, keeping its rules and hook and adding the chrome-devtools lines. Windows: Notepad, Save as type: All files. Mac: TextEdit set to plain text before pasting, then Shift-Command-G and type ~/playground/.claude; keep .json. The rules only match a server named chrome-devtools. Check the hooks with /hooks)
```
{
  "permissions": {
    "deny": [
      "mcp__playwright__browser_run_code_unsafe",
      "mcp__playwright__browser_file_upload",
      "mcp__chrome-devtools__evaluate_script",
      "mcp__chrome-devtools__set_logpoints",
      "mcp__chrome-devtools__upload_file",
      "mcp__chrome-devtools__install_extension",
      "mcp__chrome-devtools__uninstall_extension",
      "mcp__chrome-devtools__reload_extension",
      "mcp__chrome-devtools__trigger_extension_action",
      "mcp__chrome-devtools__list_extensions"
    ],
    "ask": [
      "mcp__playwright__browser_evaluate",
      "mcp__chrome-devtools__get_network_request"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "^mcp__playwright__browser_(navigate|tabs)$",
        "hooks": [
          {
            "type": "command",
            "command": "node",
            "args": ["${CLAUDE_PROJECT_DIR}/.claude/check-site.js"],
            "onFailure": "block"
          }
        ]
      },
      {
        "matcher": "^mcp__chrome-devtools__(navigate_page|new_page)$",
        "hooks": [
          {
            "type": "command",
            "command": "node",
            "args": ["${CLAUDE_PROJECT_DIR}/.claude/check-site.js"],
            "onFailure": "block"
          }
        ]
      }
    ]
  }
}
```

### 6. The fix, from prompt 3 (in serve-slow.js; Claude Code asks before it saves. Then Ctrl+C and node serve-slow.js again in the second window, and ask Claude for a fresh trace)
```
Before:   <script src="/slow.js"></script>
After:    <script src="/slow.js" defer></script>
```

### 7. Switch it off (in Claude Code: /mcp, pick chrome-devtools, choose Disable. Ctrl+C in the second window stops the page. To delete the server instead, type /exit and run this in the first window)
```
claude mcp remove chrome-devtools
```

### 8. Not our route: the plugin, for comparison (Google's own lines from its README. It runs chrome-devtools-mcp@1.13.0 but with none of the four flags, and its tools are named mcp__plugin_chrome-devtools-mcp_chrome-devtools__..., so the rules above don't match them)
```
/plugin marketplace add ChromeDevTools/chrome-devtools-mcp
/plugin install chrome-devtools-mcp@chrome-devtools-plugins
```
