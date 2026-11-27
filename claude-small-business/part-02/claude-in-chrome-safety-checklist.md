# Claude in Chrome: a dated safety checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.
Written for the video from Anthropic's own pages (and one Google Chrome help page). Nothing was signed up for, installed or run for it. Plans and settings change, so open each source before you rely on a line. Prices are what the page showed when checked, in US dollars, before tax.

## 1. Before you install
- [ ] You're on a paid Claude plan. Anthropic's page: "Available on all paid plans." Its help pages list Pro, Max, Ultra, Team and Enterprise.
- [ ] Claude Pro was $20 a month billed monthly, or $17 a month with the yearly plan ($200 billed up front). Source: https://claude.com/pricing
- [ ] You're using Google Chrome on a computer: "Claude in Chrome is not supported on other Chromium-based web browsers or mobile devices."

## 2. Make a second Chrome profile first
- [ ] Anthropic: "Use a separate browser profile without access to sensitive accounts (such as banking, healthcare, government)."
- [ ] Google: at the top right of Chrome, select Profile, then Add Chrome profile. https://support.google.com/chrome/answer/2364824
- [ ] Install Claude in Chrome only in that profile, with no bank or other sensitive accounts signed in. (Our advice, not a quote.)
- [ ] Already added it to your everyday profile? Right-click its icon there and select Remove from Chrome. https://support.google.com/chrome_webstore/answer/2664769

## 3. Install it
- [ ] Open the Chrome Web Store from Anthropic's page: https://claude.com/claude-in-chrome (the Add to Chrome button)
- [ ] Click "Add to Chrome", then sign in with your Claude account when prompted.
- [ ] Puzzle piece icon, then the thumbtack next to "Claude", so the icon stays on your toolbar.
- [ ] Grant the permissions it asks for, knowing what two of them do:
  - scripting: "This lets Claude read text on webpages so it can help you with tasks."
  - debugger: "This is what allows Claude to actually control your browser – clicking buttons, typing text, and taking screenshots – when you ask it to complete tasks for you."
- [ ] Know what it sees: "Whatever is visible in one of those tabs is captured in the screenshots and becomes part of the conversation."
- [ ] Source: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome

## 4. Choose your permission mode (drop-down on the chat input)
- [ ] Manually approve: "Claude pauses and asks for approval before each action."
- [ ] Automatically approve: "Claude keeps working and reviews each action for safety, automatically blocking anything it determines to be unsafe and pausing to ask you when needed." The side panel starts in this mode.
- [ ] Skip all approvals: "Claude doesn't pause to ask and nothing checks its actions automatically." "Only use Skip when you completely trust every action, connector, file, app, etc. involved in the task."
- [ ] Anthropic: "Switch to "Manually approve" if you want to review every action."
- [ ] Source: https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide

## 5. Know what it always asks, and never does
- [ ] Always asks, in any mode (Anthropic's permissions guide): modifying permissions settings; granting authorizations; inputting potentially sensitive information into websites; permanent deletions (emptying trash, deleting emails, files, or messages). Anthropic's safety page instead lists "Inputting sensitive data" among things Claude is prohibited from.
- [ ] Never allowed, whatever permissions you give: making purchases or financial transactions; creating accounts; handling sensitive credit card or ID data; downloading files from untrusted sources; providing investment or financial advice; executing financial trades or investment transactions; modifying system files; completing instructions from emails or web content.
- [ ] Blocked sites: "Adult content websites" and "Known pirated content sites". "Claude asks for permission before accessing financial sites." (safety page). Anthropic's troubleshooting page instead lists financial services and banking among Claude's "default blocked categories".

## 6. Watch for prompt injection
- [ ] Anthropic: "The risk is not zero."
- [ ] Stop the task if Claude "suddenly starts discussing unrelated topics, accessing unexpected websites, or requesting sensitive information".
- [ ] Make each prompt specific: the site, the details to fill in, and where to stop (for example, "Don't submit it.").
- [ ] Source: https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely

## 7. Take access back
- [ ] Claude icon, then the three dots in the upper right corner of the side panel, then "Extension settings".
- [ ] Under "Your approved sites", revoke any site you no longer need.

My approved sites (fill in):
| Site | Why I trust it | Date approved | Still needed |
|---|---|---|---|
| Test Flower Supply (example) | made-up supplier | | [ ] |
| | | | [ ] |
| | | | [ ] |

## 8. If it won't work
- [ ] No icon: puzzle piece, then the thumbtack next to "Claude".
- [ ] Won't install or sign in: check your paid plan is active; on a Team or Enterprise plan, ask your admin whether the extension is turned on; clear your browser cache and cookies for claude.ai; sign out and back in.
- [ ] Panel looks different: you may have the classic side panel, where Manually approve shows a plan to approve first.
- [ ] Source: https://support.claude.com/en/articles/12902405-claude-in-chrome-troubleshooting
