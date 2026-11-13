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
