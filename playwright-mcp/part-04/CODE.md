# Full code: Playwright MCP Server: Test Your Web App with Claude Code



### 1. Re-add Playwright MCP with its test tools (your first window, in playground; type /exit first if Claude Code is open. The same lines in PowerShell and Mac Terminal. If you removed the server at the end of Part 3, skip the first line)
```
claude mcp remove playwright
claude mcp add playwright -- npx -y @playwright/mcp@0.0.85 --isolated --caps=testing
```

### 2. Start the page and Claude Code (the page in a second window, Claude in the first, both in playground; then type /mcp and playwright should say connected)
```
node serve.js
claude
```

### 3. todo.spec.js (from the link in the description; save it in playground, next to serve.js)
```
// todo.spec.js: a Playwright test for the playground to-do page, from the link in the description.
// Save it in playground, next to serve.js. Windows: Notepad, Save as type: All files.
// Mac: TextEdit, Make Plain Text BEFORE pasting, Shift-Command-G, ~/playground (keep .js).
// It runs without Claude: start the page first (node serve.js), then run it from playground with
// npx playwright test todo.spec.js
// It needs @playwright/test 1.65.0 in playground, and uses the Google Chrome already on your computer.
const { test, expect } = require("@playwright/test");

test.use({ channel: "chrome" });

test("adds a task to the to-do list", async ({ page }) => {
  await page.goto("http://localhost:8080");
  await page.getByRole("textbox", { name: "New task" }).fill("Buy milk");
  await page.getByRole("button", { name: "Add" }).click();
  await expect(page.getByRole("listitem")).toHaveText(["Buy milk"]);
  await expect(page.getByRole("textbox", { name: "New task" })).toHaveValue("");
});
```

### 4. Run the test without Claude (first window, in playground, after /exit; node serve.js still running in the second window. You should see "1 passed". Windows: if PowerShell says running scripts is disabled on this system, type npm.cmd and npx.cmd instead of npm and npx)
```
npm install --save-dev @playwright/test@1.65.0
npx playwright test todo.spec.js
```

### 5. check-site.js (from the link in the description; save it inside playground/.claude, next to settings.json)
```
// check-site.js: a PreToolUse hook for Playwright MCP, from the link in the description.
// Save it as check-site.js inside playground/.claude, next to settings.json.
// Windows: paste into Notepad, Save as type: All files. Mac: TextEdit, Format menu, Make Plain Text
// BEFORE pasting, then in the save box press Shift-Command-G and type ~/playground/.claude (keep .js).
// Claude Code runs it with node before each browser_navigate or browser_tabs call, and hands it the
// call as JSON. Exit 0 lets the call go on to your normal permission rules; exit 2 blocks it, and
// Claude sees the message. It checks ONLY the address in the call. It can't see a click on a link,
// a redirect, or a page's own scripts, so it is not a wall around the browser.
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

  if (typeof input.url !== "string" || input.url === "") return block("no address was given.");
  let origin;
  try { origin = new URL(input.url).origin; } catch (e) { origin = "null"; }
  if (origin === "null") return block("that is not a full web address, like http://localhost:8080.");
  if (ALLOWED.indexOf(origin) !== -1) process.exit(0);
  block(origin + " is not on the allowed list. Only " + ALLOWED.join(" and ") + " are allowed.");
});
```

### 6. .claude/settings.json, the new version (from the link in the description; it replaces Part 3's file in playground/.claude, keeping its deny and ask lists and adding the hook. Windows: Notepad, Save as type: All files. Mac: TextEdit set to plain text before pasting, then Shift-Command-G and type ~/playground/.claude; keep .json. onFailure needs Claude Code 2.1.295 or newer. Check it with /hooks)
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
      }
    ]
  }
}
```

### 7. Test the hook (in Claude Code, in playground: this prompt should come back blocked, with the script's message)
```
Use playwright to open https://example.com
```

### 8. Optional: the Docker image instead of npx (needs Docker Desktop. Headless Chromium only, and localhost inside the container is the container, so it can't open your playground page; add each test site's address to ALLOWED in check-site.js. The image is fixed to v0.0.85, and the port is published to 127.0.0.1 only, so only this computer can reach it. --no-sandbox comes from the README's own command. Mac Terminal: as written. Windows PowerShell: put the whole command on one line, without the backslashes)
```
docker run -d -i --rm --init \
  --entrypoint node \
  --name playwright \
  -p 127.0.0.1:8931:8931 \
  mcr.microsoft.com/playwright/mcp:v0.0.85 \
  /app/cli.js --headless --browser chromium --no-sandbox --port 8931 --host 0.0.0.0 --isolated --caps=testing
```

### 9. Point Claude Code at the Docker server, under the same name (first window, in playground, after /exit; the deny rules and the hook only match a server called playwright)
```
claude mcp remove playwright
claude mcp add --transport http playwright http://127.0.0.1:8931/mcp
```

### 10. Switch it all off (in Claude Code: /mcp, pick playwright, choose Disable. Ctrl+C in the second window stops the page. For Docker, this stops the container, and --rm deletes it)
```
docker stop playwright
```
