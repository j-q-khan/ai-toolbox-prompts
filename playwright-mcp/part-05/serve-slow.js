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
