# Full code: Claude Canva Connector: Set It Up and Make Your First Design

The words typed in this video and the connector checklist, written from Anthropic's help pages and Canva's developer docs (checked 2026-11-17). They were written from the docs, not run for this video.

### 1. first-design-brief.txt
```
# Paste the brief (the seven lines under this note) into a Claude chat with the Canva connector switched on.
# Made-up details only. The lines starting with # are notes for you: don't paste them.
# Written from Canva's developer docs (generate-design, best practices), checked 2026-11-17.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Using Canva, make a flyer for a made-up shop called Test Bakery.
Purpose: announce a Saturday bake sale.
Audience: families who live nearby.
Exact words: "Saturday Bake Sale" as the headline, "Fresh bread, cakes and cookies" underneath, and "12 Example Street, test@example.com" at the bottom.
Tone: warm and friendly.
Format: a portrait flyer for printing.
Show me the options and let me choose. Don't pick one for me.

# Follow-up 1, sent on its own once the candidates appear (choose the one you like):
Use the second option.

# Follow-up 2, sent on its own when the design is how you want it:
Export this flyer as a PDF.

# The shortcut, in any chat with Canva switched on:
Find my flyer with "Bake Sale" in the title.
```

### 2. canva-connector-checklist.md
```
# Claude Canva connector: setup and fix checklist (facts checked 2026-11-17)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Before you start
- [ ] A Claude account and a Canva account. Same steps on Windows and Mac, on the web or in the desktop app.
- [ ] Anthropic's listing: "Only use connectors from developers you trust." This connector is made by Canva.
- [ ] Connecting grants Claude permission to access and potentially modify data in Canva, based on your account's permissions (Anthropic's help page).
- [ ] A work account: follow your employer's rules first. On Claude's Team and Enterprise plans, an owner enables the connector, and each person still signs in for themselves.

## Connect once
- [ ] In a chat, click the plus button in the lower-left corner (or type /).
- [ ] Hover over Connectors, then choose Manage connectors.
- [ ] Click the plus next to Connectors, click Canva, then Connect.
- [ ] Follow the prompts to sign in to Canva.
- [ ] Check: Canva is in your list under Customize, then Connectors.

## In every chat
- [ ] Click the plus button, hover over Connectors, and switch Canva's toggle on.

## First design
- [ ] Paste the brief from first-design-brief.txt. Made-up details only.
- [ ] If Claude asks to use Canva, approve it. Making candidates can take a little while.
- [ ] Choose a candidate yourself ("Use the second option.").
- [ ] Open the link, and finish the design in Canva's editor.
- [ ] Export ("Export this flyer as a PDF."). Canva's docs name PDF, PNG, JPG, PPTX and MP4. The download link expires: use it straight away, and don't share the link itself.

## What needs Canva Pro and above (Canva's developer docs, 2026-11-17)
- [ ] All plans: making designs, exporting, finding your designs, folders, comments. Free plans export at standard quality.
- [ ] Pro and above (Canva Pro, Business and Enterprise): resizing, Brand Kits and brand templates, and autofill (filling a design's data fields with your text and images).
- [ ] Free plans get a limited trial of resizing.
- [ ] No price is listed here because prices change: https://www.canva.com/pricing/

## Fix it
- [ ] Canva not showing in a chat: check its toggle is on for that chat (plus button, Connectors).
- [ ] Designs still don't appear: start a new chat and ask again.
- [ ] The panel stops responding: refresh the page, or restart the desktop app.
- [ ] It worked before and has stopped: Customize, then Connectors, disconnect Canva, then connect it again.
- [ ] license_required on an export: the design contains premium elements. Canva's docs give no fix; our suggestion is to try swapping them in Canva's editor.
- [ ] quota_exceeded on a resize: your resize allowance has run out. The message includes an upgrade link.
- [ ] Still stuck: check your internet connection.

Sources: support.claude.com/en/articles/11176164 ; support.claude.com/en/articles/13454812 ; claude.com/connectors/canva ; canva.dev/docs/apps/mcp/tools ; canva.dev/docs/apps/mcp/tools/resize-design ; canva.dev/docs/apps/mcp/tools/export-design
```
