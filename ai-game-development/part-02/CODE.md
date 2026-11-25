# Full code: Claude Game Development: Build a Browser Game with Claude Code, Step by Step

The game file and the prompts for this video, written from Anthropic's Claude Code docs, MDN and Phaser's README (checked 2026-11-25). Example output: they were written from the docs and not run for this video, and the game file was only syntax-checked; Claude Code's own file will differ.

### 1. game.html
```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Comet Dodge (Test Arcade)</title>
<!--
  Comet Dodge (game.html): a one-file browser game for the AI Game Development series, Part 2.
  Example output: written from the docs for this video, not run for it. Facts checked 2026-11-25.
  To keep a copy: paste this into Notepad and save it as game.html with the box called
  Save as type set to All files. On a Mac: open TextEdit, choose Format, then Make Plain Text,
  before you paste, then save it as game.html.
  To play: open the file in your web browser. The left and right arrow keys move the ship.
  Comets end the game, stars add 10 points, and R starts again.
  Free to use (MIT licence). Uses nothing from the internet and saves nothing.
-->
<style>
  html, body { margin: 0; height: 100%; background: #0b1020; }
  body { display: flex; align-items: center; justify-content: center; }
  canvas { background: #111a33; border: 2px solid #2b3a6b; max-width: 100%; max-height: 100%; }
</style>
</head>
<body>
<canvas id="game" width="480" height="640"></canvas>
<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const W = canvas.width, H = canvas.height;
const keys = {};
let ship, comets, stars, score, time, speed, nextSpeedUp, cometTimer, starTimer, over;

function reset() {
  ship = { x: W / 2, y: H - 50, r: 16, v: 300 };
  comets = []; stars = [];
  score = 0; time = 0; speed = 160; nextSpeedUp = 10;
  cometTimer = 0; starTimer = 2; over = false;
}

addEventListener("keydown", e => {
  keys[e.key.toLowerCase()] = true;
  if (e.key.startsWith("Arrow")) e.preventDefault();
  if (over && e.key.toLowerCase() === "r") reset();
});
addEventListener("keyup", e => { keys[e.key.toLowerCase()] = false; });

function hit(a, b) { return Math.hypot(a.x - b.x, a.y - b.y) < a.r + b.r; }

function update(dt) {
  if (over) return;
  time += dt;
  score += dt;
  if (time >= nextSpeedUp) { speed *= 1.15; nextSpeedUp += 10; }
  if (keys["arrowleft"]) ship.x -= ship.v * dt;
  if (keys["arrowright"]) ship.x += ship.v * dt;
  ship.x = Math.max(ship.r, Math.min(W - ship.r, ship.x));

  cometTimer -= dt;
  if (cometTimer <= 0) {
    const r = 12 + Math.random() * 16;
    comets.push({ x: r + Math.random() * (W - 2 * r), y: -r, r: r });
    cometTimer = 0.6;
  }
  starTimer -= dt;
  if (starTimer <= 0) {
    stars.push({ x: 20 + Math.random() * (W - 40), y: -10, r: 10 });
    starTimer = 2.5;
  }
  for (const c of comets) c.y += speed * dt;
  for (const s of stars) s.y += 96 * dt;   // stars keep one slow speed; only the comets speed up
  comets = comets.filter(c => c.y - c.r < H);
  stars = stars.filter(s => s.y - s.r < H);

  for (const c of comets) if (hit(ship, c)) over = true;
  stars = stars.filter(s => {
    if (hit(ship, s)) { score += 10; return false; }
    return true;
  });
}

function draw() {
  ctx.clearRect(0, 0, W, H);
  ctx.fillStyle = "#7fd6ff";
  ctx.beginPath();
  ctx.moveTo(ship.x, ship.y - ship.r);
  ctx.lineTo(ship.x - ship.r, ship.y + ship.r);
  ctx.lineTo(ship.x + ship.r, ship.y + ship.r);
  ctx.closePath();
  ctx.fill();
  ctx.fillStyle = "#9aa3b5";
  for (const c of comets) { ctx.beginPath(); ctx.arc(c.x, c.y, c.r, 0, Math.PI * 2); ctx.fill(); }
  ctx.fillStyle = "#ffd84a";
  for (const s of stars) { ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2); ctx.fill(); }
  ctx.fillStyle = "#ffffff";
  ctx.font = "20px sans-serif";
  ctx.textAlign = "left";
  ctx.fillText("Score: " + Math.floor(score), 12, 30);
  if (over) {
    ctx.textAlign = "center";
    ctx.font = "32px sans-serif";
    ctx.fillText("Game over", W / 2, H / 2 - 10);
    ctx.font = "20px sans-serif";
    ctx.fillText("Press R to play again", W / 2, H / 2 + 24);
  }
}

let last = performance.now();
function loop(now) {
  const dt = Math.min((now - last) / 1000, 0.05);
  last = now;
  update(dt);
  draw();
  requestAnimationFrame(loop);
}
reset();
requestAnimationFrame(loop);
</script>
</body>
</html>
```

### 2. prompts.txt
```
# The prompts from this video, in order: paste one, choose Yes, test it in your browser, then the next.
# To keep a copy: paste this into Notepad and save it as prompts.txt with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# The lines starting with # are notes for you, so don't paste them. Written from Anthropic's docs, checked 2026-11-25; not run for the video.

# Before prompt 1, in a fresh PowerShell (Windows) or Terminal (Mac) window, type these three lines, pressing Enter after each:
# mkdir arcade
# cd arcade
# claude

# Prompt 1: the first prompt
Make a browser game called Comet Dodge in one file, game.html.
Use a canvas and plain JavaScript, nothing from the internet.
A ship at the bottom moves left and right with the arrow keys.
Comets fall from the top, and touching one ends the game.
The score goes up every second you survive.
When you lose, show Game over and Press R to play again.
R starts a new game.
Create only game.html, and tell me how to open it.

# To open the game: in a second PowerShell window type  start arcade\game.html
# or in a second Terminal window on a Mac type  open arcade/game.html
# After every change: refresh the browser tab (F5 on Windows, Command and R on a Mac).

# Prompt 2: the first change
Add yellow stars that fall more slowly than the comets.
Catching a star adds 10 points.
Change nothing else.

# Prompt 3: the second change
Make the comets fall 15% faster every 10 seconds.
Change nothing else.

# When something breaks: say what you did, what you expected and what happened. For example:
When I press the left arrow, the ship doesn't move.
It should move left. Please fix only that.

# Going further (optional): this one loads Phaser 4.2.1 from the internet, which the plain game never needed.
Rebuild my game as a new file, game-phaser.html,
using Phaser 4.2.1, loaded from this link:
https://cdn.jsdelivr.net/npm/phaser@4.2.1/dist/phaser.min.js
Keep the same rules: the ship, the comets, stars worth 10,
the speed-up and R to restart. Don't change game.html.

# A change broke the game? In Claude Code, press Esc twice with the input empty (or type /rewind),
# pick the prompt that made the change, then choose Restore code.
```
