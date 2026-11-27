# Claude for Outlook: a dated setup checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.
Written for the video from Anthropic's and Microsoft's own pages. Nothing was signed up for, installed or run for it. Plans, prices and screens change, so open each source before you rely on a line. Prices are what the page showed when checked, in US dollars, before tax.

## 1. Check your plan
- [ ] "Claude for Outlook is generally available to Pro, Max, Team, and Enterprise plans. It is not available on the Free plan." (Anthropic)
- [ ] On Free: "You can install the add-in, but you cannot finish signing in." (Anthropic)
- [ ] Pro was $20 a month billed monthly, or $17 a month with the yearly plan ($200 billed up front).
- [ ] Sources: https://claude.com/docs/office-agents/outlook and https://claude.com/pricing (checked 2026-11-26)

## 2. Check your Outlook
- [ ] Supported: Outlook on the web; Outlook on Windows, both new Outlook and classic Outlook, with a Microsoft 365 subscription; Outlook on Mac with a Microsoft 365 subscription.
- [ ] Not supported: Outlook on iOS, Outlook on Android, Outlook 2016 and 2019 perpetual or volume-licensed editions, mailboxes hosted on Exchange on-premises, shared mailboxes and mailboxes you open as a delegate.
- [ ] "Gmail, Yahoo, iCloud, IMAP, and POP accounts added to Outlook are not supported." "Exchange Online through Microsoft 365 is required." (Anthropic)

## 3. Install it
- [ ] Open the Claude for Outlook listing on Microsoft AppSource: https://marketplace.microsoft.com/en-us/product/office/WA200010724
- [ ] Sign in to the listing with the same Microsoft account you use in Outlook ("Add-ins are installed on a mailbox, not on a device.")
- [ ] Select "Get it now". If it does nothing or returns to the same page, sign in with that same account and select "Get it now" again.
- [ ] On a work account: "Your organization's Microsoft 365 administrator may need to let you install store add-ins, or deploy Claude for Outlook for you."

## 4. Find the Claude button and sign in
- [ ] Open Outlook, then open or select an email.
- [ ] Outlook on the web and new Outlook on Windows: select Apps on the message's action bar, or More apps on the ribbon, then select Claude.
- [ ] Classic Outlook on Windows: set the Reading Pane to Right or Bottom (View tab), select a message, then select Claude on the Home tab. If it isn't there: All Apps, then Claude.
- [ ] Outlook on Mac: set the Reading Pane to Right or Below (View menu), select a message, then select Claude on the toolbar. If it isn't there: the ellipsis button, then Claude.
- [ ] No Claude button in desktop Outlook? Restart Outlook.
- [ ] Select Claude and sign in with your Claude account.

## 5. Mailbox access: know what it can see
- [ ] Claude works on the email you have open. "Features that look beyond the open email or event, such as search, triage, reading a whole thread, free/busy lookups, and move or flag actions, need Microsoft Graph consent." (a one-time approval)
- [ ] Screen says "Your admin needs to approve access"? Select "Copy link for your admin" and send it to your Microsoft 365 administrator. After they approve, select "I've been approved".
- [ ] Not waiting? "Continue without mailbox access" lets Claude work on the email you have open.
- [ ] The four permissions the administrator approves, in Microsoft's words (https://learn.microsoft.com/en-us/graph/permissions-reference):
  - Mail.ReadWrite: "Allows the app to create, read, update, and delete email in user mailboxes. Does not include permission to send mail."
  - Calendars.Read: "Allows the app to read events in user calendars."
  - User.Read: "Sign in and read user profile"
  - offline_access: "Maintain access to data you have given it access to"
- [ ] "The add-in never sends mail or invites. It does not request the Mail.Send permission." (Anthropic)

## 6. Review before send
- [ ] Drafts land unsent in Outlook's compose pane; invites in Outlook's appointment form. "Nothing is saved or sent until you click Save or Send in Outlook."
- [ ] "Review every draft and inbox action before accepting it, especially when working with email from external or untrusted senders." (Anthropic)
- [ ] "Email bodies and attachments are untrusted input and may contain instructions intended to manipulate Claude rather than you." (Anthropic: prompt injection)
- [ ] "Review drafted replies and invites before sending, especially recipient lists."
- [ ] Want a second look? "To have a draft checked, ask Claude to review it before you send."
- [ ] Try it first on a test mailbox with made-up mail, before your real customers.
- [ ] All-day events are not supported.

## 7. Not the same thing: the Microsoft 365 connector
- [ ] "Connectors are separate from the add-in's own access. A connector, such as Microsoft 365, can send mail, messages, or invites. Claude asks for your approval before each connector action, unless you selected the "Always allow" button for that connector" (Anthropic)
- [ ] The connector, set up: Claude Cowork Part 6, https://youtu.be/nPW_upDIM9Y

## 8. Make drafts sound like you
- [ ] Settings, then Writing style, then "Learn my writing style": Claude goes through your recent sent mail once and writes a style guide.

## Data
- [ ] "For Claude for Outlook use, inputs and outputs are deleted on Anthropic's backend within 30 days of receipt or generation, except as described in How long do you store my organization's data?" (Anthropic)
- [ ] "Chat history is stored locally in your browser using IndexedDB. It is not synced across devices or browsers." (Anthropic)
- [ ] "Clearing chat history removes only the copy in your browser. It does not delete the messages or attached files that Anthropic keeps." (Anthropic)
