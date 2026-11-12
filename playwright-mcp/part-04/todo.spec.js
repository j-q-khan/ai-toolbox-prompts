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
