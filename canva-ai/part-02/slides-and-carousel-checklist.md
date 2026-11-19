# Claude Canva: slides and carousel checklist (facts checked 2026-11-17)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Before you start
- [ ] The Canva connector is connected (Part 1 of this series), and switched on in this chat: plus button, Connectors.
- [ ] A work account: follow your employer's rules first. Each person signs in to Canva for themselves.

## The prompt shape
- [ ] Canva's list for a brief: purpose, audience, key copy (the exact words), tone, format, brand constraints.
- [ ] Our two additions for slides or a carousel: how many pages, and one idea on each.
- [ ] Canva's advice: "Don't replace a detailed outline with a short summary."
- [ ] Made-up or approved details only. Don't paste anything private.

## The slides
- [ ] Paste slides-outline-prompt.txt. Generating can take up to 60 seconds (Canva's docs).
- [ ] If you're shown candidates, choose one yourself. Either way, open the link to the design in Canva's editor.
- [ ] Check: "How many slides are in my workshop presentation?" The answer should match your outline.

## The carousel
- [ ] Paste carousel-prompt.txt. The format name in Canva's docs is Instagram Post; the docs don't use the word carousel.
- [ ] Check: "How many pages are in my carousel?" The docs don't promise a page count. If it's short, finish it by hand in Canva's editor.

## Changes
- [ ] Ask in the chat ("Change the headline on slide 1 to ...").
- [ ] Don't type in the same design in a Canva tab while Claude is changing it: Canva's docs say a save can fail when a person is editing in the browser.
- [ ] Wait until Claude says the change is saved. Unsaved draft edits are discarded (Canva's docs).
- [ ] If Claude can't make a change, open the link and make it by hand. Claude can only take actions the connector's developer has made available (Anthropic's help page).

## The files
- [ ] Ask which formats the design can be downloaded in. Canva's docs name PDF, PNG, JPG, GIF, PowerPoint, video and CSV, and say which pages are available can differ by format.
- [ ] Slides: a PowerPoint file, and a PDF.
- [ ] Carousel: every page as a PNG (or JPG).
- [ ] Download links expire: use them straight away, and don't share the link itself.
- [ ] Free plans export at standard quality. Canva Pro and above: "Pro quality with lossless PNG, transparent backgrounds, and premium element export".
- [ ] The connector doesn't post to Instagram. Post the pictures yourself.

## Limits (Canva's developer docs, 2026-11-17)
- [ ] Canva's credit model applies to design generation. No amount is given in the developer docs; see https://www.canva.com/pricing/
- [ ] Pro and above (Canva Pro, Business and Enterprise): Brand Kits and brand templates, resizing, autofill. Otherwise, put your colours and fonts in the prompt (our suggestion).
- [ ] Anthropic's listing shows fewer tools than Canva's table, so Claude may not offer every step here. Nothing here was tested.

Sources: canva.dev/docs/apps/mcp/tools/create-design ; canva.dev/docs/apps/mcp/tools/generate-design ; canva.dev/docs/apps/mcp/best-practices ; canva.dev/docs/apps/mcp/tools/get-design-pages ; canva.dev/docs/apps/mcp/tools/commit-editing-transaction ; canva.dev/docs/apps/mcp/tools/get-export-formats ; canva.dev/docs/apps/mcp/tools/export-design ; canva.dev/docs/apps/mcp/tools ; canva.dev/docs/apps/mcp/usage-policy ; support.claude.com/en/articles/13454812
