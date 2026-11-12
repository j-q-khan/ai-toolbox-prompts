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