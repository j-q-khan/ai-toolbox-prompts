# Full code: Claude Design System Tutorial: Make Every Design Match Your Brand

The bakery brand kit and a setup checklist, written from Anthropic's own help pages (checked 2026-11-15). Plain text only; nothing was signed into, generated or run.

### 1. pebble-lane-brand-kit.txt
```
# pebble-lane-brand-kit.txt: a made-up brand kit to build a Claude Design design system from
# Pebble Lane Bakery is not a real business. Use made-up or your own non-confidential files, never client files.
# Attach it in a chat with Claude on a paid plan and ask: Build a design system from this brand kit.
Brand: Pebble Lane Bakery (made up, not a real business).
Logo: a round mark with one wheat stalk, plain shapes only, with the name Pebble Lane Bakery.
Colours: flour cream #F5EBDD, crust brown #8A5A2B, sage green #8FA382.
Colour roles: cream for backgrounds, brown for text and buttons, sage for accents and borders.
Fonts: warm rounded for headings; plain and easy to read for body text.
Primary Button: crust brown fill, cream text, rounded corners.
Card: cream fill, thin sage border, 16-pixel padding.
Layout: an 8-pixel spacing scale and plenty of white space.
Voice: warm, plain and short. No slogans, prices or awards unless the owner gives them.
Always: mark every design as a draft, and don't imitate any real company's brand.
```

### 2. design-system-setup-checklist.txt
```
# design-system-setup-checklist.txt: setting up a design system in Claude, step by step
# Built only from Anthropic's help pages, checked 2026-11-15. Menu names can change: check the pages on your day.
# Sources: support.claude.com articles 14604397 (set up your design system), 14604416 (get started),
# 17440474 (move from standalone), 16994751 (artifacts admin guide); code.claude.com/docs/en/commands
[ ] Plan: design systems are a beta on Pro, Max, Ultra, Team and Enterprise. Not on Free.
[ ] Enterprise: an owner turns on Design systems in Organization settings, then Artifacts.
[ ] Settings, then Capabilities: the switch called Create and edit files is on.
[ ] One source ready: a codebase with your component library, slides or a document in your brand, or brand assets (logo, colours, fonts).
[ ] Add a finished example if you have one, like a landing page: Anthropic's tips say it tells Claude more than a palette alone.
[ ] Privacy: on Pro, Max and Ultra, chats can be used to improve Claude when Model Improvement is on. At work, follow your employer's rules.
[ ] Brand system: in a chat, attach your files and ask Claude to build a design system from them.
[ ] Product system in React: /design-sync in Claude Code. Its command list says it uploads to the standalone site, which closes by December 14, 2026, and a first sync can take a few hours.
[ ] Check the result: it opens as a list of sections; compare each colour and font with your kit.
[ ] Test it: ask for a landing page or a one-pager, and check colours, fonts and buttons.
[ ] Use it: attach it when you start a new design or slides (moved systems also appear in the design system menu).
[ ] Find it again: Settings, then Capabilities, then Manage next to Design systems (or Settings, then Design systems).
[ ] Team or Enterprise: only an Owner or Primary Owner can share it with everyone or choose Set as default.
[ ] Wrong results: upload more or different files, then test again. To change it, ask Claude in a chat.
[ ] Moved from claude.ai/design: click Let Claude clean it up on its banner.
[ ] Keyboard: live component previews can't be reached with Tab; names and notes are still there.
[ ] Tip: name components in prompts, like "Use the Primary Button component".
```
