# AI personal assistant for email and calendar: the privacy checklist (facts checked 2026-11-23)

To keep a copy: paste this into Notepad and save it as privacy-checklist.md with the box called Save as type set to All files. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every line below is from the maker's own help page on 2026-11-23. Menus, plans and prices change: check each page first. If it's a work or school account, follow your employer's rules before you connect anything. Nothing here is legal advice.

## Before you connect anything
- [ ] Work or school email? Ask first: the account belongs to your employer or school.
- [ ] Use the right account: connect the Google or Microsoft account whose email you mean, not a shared one.
- [ ] Claude: click the permission setting in the message box and choose Manual ("Claude pauses and asks for approval for actions"). Auto is rolling out as the default on Pro, Max, Ultra and Team, and its automated check "can miss risky actions". No permission setting in your message box? By default, outside Auto mode, Claude already asks before each send. https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- [ ] In an approval box, choose Allow, not Always allow. On Free, Pro, Max and Ultra, Always allow means Claude "will then use it without asking you each time", and a tool set to Always allow runs without asking even in Manual. https://support.claude.com/en/articles/15183774-connect-to-microsoft-365

## 1. Claude: Gmail and Google Calendar connectors (all users)
- Connect: Plugins in the sidebar (Customize on older screens), filter to connectors, open Gmail, Connect, sign in with Google. Same for Google Calendar. In a chat: the + button, lower left, Connectors, switch each on. https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
- What Gmail can do: search and read emails, open attachments (up to about 12 MB), draft, and "Send, reply to, and forward emails from Gmail. By default, outside Auto mode, Claude asks for your approval before each of these actions."
- What Calendar can do: view events and shared calendars, create, update and delete events, find mutual availability, respond to invitations.
- Data, in Anthropic's words: "Claude only accesses your data when you explicitly ask"; retrieved data "is retained with its associated chat, so you can delete any retrieved data by deleting the chat"; "We do not train our models on your Gmail, Drive, or Calendar connector data". But if Model Improvement is on, text you copy from those emails into a chat "may be used to improve our models". Model Improvement: Claude's Privacy Settings, https://claude.ai/settings/data-privacy-controls (about it: https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training)
- [ ] Per chat: the + button > Connectors > switch Gmail off in chats that don't need it.
- [ ] Paid plans, as it rolls out: Plugins (or Customize) > Connectors > Gmail > Permissions tab > set the send tool to "Always ask".
- [ ] Remove: Plugins (or Customize) > Gmail > Disconnect > Disconnect. Same for Google Calendar.
- [ ] Remove on Google's side: https://myaccount.google.com/connections > Claude > Delete all connections.
- Source: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors

## 2. Claude: Microsoft 365 connector (Outlook)
- Personal Microsoft accounts (Outlook.com, Hotmail, Live, MSN) on Free, Pro, Max and Ultra: Plugins (or Customize) > Connectors > Microsoft 365 > Connect > Personal account. Write tools are included (draft, send, calendar events).
- [ ] Remove: Plugins (or Customize) > Connectors > Microsoft 365 > Disconnect.
- Source: https://support.claude.com/en/articles/15183774-connect-to-microsoft-365

## 3. Gemini in Gmail (Google)
- Help me write: Compose > the prompt bar at the bottom (or Help me write) > Create. Personal accounts without a paid plan: "restricted to the US only". https://support.google.com/mail/answer/13955415
- It "proactively takes details from your other emails and Drive files" for its drafts.
- Ask Gemini side panel (top right): "requires an eligible Google Workspace or Google AI plan". https://support.google.com/mail/answer/14355636
- Google AI Plus was $4.99 a month (US) when checked on 2026-11-23. https://gemini.google/us/subscriptions/
- [ ] Turn Gemini features off: Gmail > Settings > See all settings > General > Google Workspace smart features > Manage Workspace smart feature settings > turn off Smart features in Google Workspace > Save. This also turns off events from Gmail in Calendar. https://support.google.com/mail/answer/10079371

## 4. Copilot in Outlook (Microsoft)
- "Chatting with Copilot in Outlook is only available if you're using a work or school account." At home, Microsoft 365 Personal, Family, Premium or Pro: the Summarize button at the top of a thread. https://support.microsoft.com/en-us/outlook/frequently-asked-questions-about-copilot-in-outlook
- Microsoft 365 Personal was $9.99 a month when checked on 2026-11-23. https://www.microsoft.com/en-us/microsoft-copilot/for-individuals
- Data, in Microsoft's words: "Prompts, responses, and your file contents when using Copilot in Microsoft 365 apps aren't used to train foundation models." https://support.microsoft.com/en-us/topic/6f0d8d80-f4bb-4c9f-989e-64a4adfd62e5
- [ ] Turn off: the Turn on Copilot switch. Web and new Outlook for Windows: Settings > Copilot. Android, iPhone, Mac: Quick Settings > Copilot. Applies to all your devices on that account. Classic Outlook for Windows: not available yet. https://support.microsoft.com/en-us/topic/bc7e530b-152d-4123-8e78-edc06f8b85f1

## 5. ChatGPT apps (OpenAI)
- Gmail and Google Calendar are apps under Settings > Plugins. "App availability depends on the app, your ChatGPT plan, region, workspace, role, model, and ChatGPT interface you use."
- Training, in OpenAI's words: "We do not train our generalized models on data directly from connected Google apps", except feedback (thumbs up or down), data "manually copied, pasted, or uploaded" from a Google app, or data "included in ChatGPT's response"; and with "Improve the model for everyone" off, "app data will not be used to improve our models". If Memory is on, Google app data "may help personalize ChatGPT" (Settings > Personalization).
- [ ] Training setting: Settings > Data controls > Improve the model for everyone > turn it off > Done (web). Phone: sidebar > profile icon > Data controls. https://help.openai.com/en/articles/7730893-data-controls-faq (checked 2026-11-24)
- [ ] Remove: Settings > Plugins > the app > disconnect. Disconnecting doesn't delete existing chats or saved memories.
- Source: https://help.openai.com/en/articles/11487775-connectors-in-chatgpt ; https://help.openai.com/en/articles/10408842-google-connector-for-chatgpt-data-controls-faq
