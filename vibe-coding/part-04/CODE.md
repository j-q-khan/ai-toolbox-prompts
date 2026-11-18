# Full code: Google Stitch Tutorial: Design Your App First, Then Build It

The prompts from this video and a checklist, written from Google's Stitch posts and the Lovable and Claude Code docs (checked 2026-11-17). They were written from the docs, not run for this video.

### 1. stitch-bakery-prompt.txt
```
# Paste the first prompt into Stitch at stitch.google.com, after you sign in with a Google account.
# Then send each edit on its own, after the one before has finished, with the menu screen picked.
# Made-up details only. Written from Google's Stitch posts and prompt guide, checked 2026-11-17.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

# First prompt, three phone screens:
Three phone screens for Test Bakery, a small neighbourhood bakery app: a menu, a sign-in screen and a My reservations list.
The menu shows Sourdough loaf $6, Cinnamon roll $3 and Rye bread $5, each with a Reserve button. Warm, friendly style with large text.

# Edit 1, on the menu screen:
Make the Reserve buttons bigger.

# Edit 2, on the menu screen:
Change primary color to warm brown.
```

### 2. lovable-restyle-prompt.txt
```
# Use this in the Test Bakery app from Part 3, in the chat on the left, with Build picked.
# First drag a screenshot of your Stitch menu screen into the chat (Windows: Windows logo key + Shift + S;
# Mac: Shift + Command + 4), then paste the two lines below into the same message.
# Written from Lovable's Project chat and Prompting best practices docs, checked 2026-11-17.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Restyle the menu and My reservations pages to match the attached design mockup: its colours, fonts, spacing and button style.
Change only the look, and keep the logins and reservations working. Leave the rest of the app unchanged.
```

### 3. claude-code-bakery-prompt.txt
```
# Use this in Claude Code, opened in a new empty folder (install: Claude Code for Beginners, linked in the description).
# First drag the same screenshot into the Claude Code window, then paste the lines below.
# Written from Claude Code's Work with images docs, checked 2026-11-17. Made-up details only.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Build a one-page menu for Test Bakery, a made-up bakery, that matches this design mockup: same colours, fonts, spacing and buttons.
Use plain HTML and CSS in this folder only, with made-up items only, and no sign-in or database.
When you're done, tell me how to open the page in my browser.
```

### 4. stitch-design-first-checklist.md
```
# Design first in Google Stitch, then build: checklist (facts checked 2026-11-17)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Before you start
- [ ] Stitch is at stitch.google.com (the old stitch.withgoogle.com address redirects there). Sign in with a Google account.
- [ ] Google calls Stitch an experiment from Google Labs. Google publishes no prices, limits or data-use terms for it (checked 2026-11-17).
- [ ] Google's service-specific terms list Stitch under the Google Terms of Service and the Generative AI Prohibited Use Policy.
- [ ] Made-up details only (Test Bakery, test@example.com). For work, follow your employer's rules.

## Make the screens
- [ ] Start with one prompt for all the screens, at a high level, then drill down screen by screen (Google's prompt guide).
- [ ] You can type the prompt, say it out loud, or upload a sketch, a screenshot or a rough wireframe (Google's posts).
- [ ] One screen at a time, one or two changes per prompt. Name colours ("Change primary color to forest green" is Google's example).
- [ ] Click Play to tap through your screens as a prototype.

## Ways out of Stitch (Google's words, by post)
- [ ] 2025 launch post: paste to Figma, and front-end code for your design.
- [ ] 2026 posts: Google AI Studio (a shareable link), Google Antigravity, publish to the web with Netlify.
- [ ] DESIGN.md: a file of your design rules that Stitch exports and imports, for other design and coding tools. Its draft specification is open source.
- [ ] Stitch MCP server and SDK, for assistants such as Claude Code. Setup page: stitch.withgoogle.com/docs/mcp/setup (from Google's stitch-skills repo). Mid level: it uses a key, so keep that key private.

## Into Lovable (one way: a screenshot)
- [ ] Screenshot your Stitch screen. Windows: Windows logo key + Shift + S (Windows 11 saves it to your Screenshots folder; otherwise paste it straight into the chat). Mac: Shift + Command + 4 (saved to the desktop).
- [ ] In your app's editor, drag the picture into the chat on the left, or paste it. Free plan files: up to 20 MB each.
- [ ] Say what must stay untouched: lovable-restyle-prompt.txt.
- [ ] Optional: click the attached picture, choose Draw, circle the part you mean, then Save.
- [ ] Check in the preview: sign in as test@example.com, and your reservations are still there.
- [ ] Other routes in Lovable's docs: the Lovable Figma plugin, Figma MCP, or a .fig file (Figma: File, then Save local copy).

## Into Claude Code (one way: a screenshot)
- [ ] Claude's Free plan didn't include Claude Code when checked on 2026-11-17 (claude.com/pricing).
- [ ] Install: Claude Code for Beginners on this channel.
- [ ] Open Claude Code in a new empty folder. Drag the screenshot into the Claude Code window (or paste it: Ctrl+V, or Alt+V on Windows).
- [ ] Paste claude-code-bakery-prompt.txt, or the longer build prompt.

Sources: developers.googleblog.com/stitch-a-new-way-to-design-uis ; blog.google (Stitch posts, Dec 2025 to May 2026) ; discuss.ai.google.dev/t/stitch-prompt-guide/83844 ; policies.google.com/terms/service-specific ; docs.lovable.dev/features/projects/chat ; docs.lovable.dev/prompting/prompting-one ; docs.lovable.dev/integrations/figma ; code.claude.com/docs/en/common-workflows ; claude.com/pricing ; support.microsoft.com (Snipping Tool) ; support.apple.com/en-us/102646
```
