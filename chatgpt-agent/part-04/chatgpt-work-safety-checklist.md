# ChatGPT Work safety: logins, permissions and take over, checklist (facts checked 2026-11-19, from OpenAI's own pages)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## What you need
- [ ] A ChatGPT account. OpenAI: "Cloud browsing is available in all regions on paid plans other than Free and Go." And: "The ability for ChatGPT Work to navigate to websites that need authentication is available on web and mobile on Plus and Pro plans." Availability depends on rollout, and website sign-in isn't available for Enterprise or Edu workspaces. https://learn.chatgpt.com/docs/browser
- [ ] For the browser extension and permission modes: the ChatGPT desktop app (macOS, Windows or Linux): https://learn.chatgpt.com/docs/app

## Website permissions (cloud browser)
- [ ] ChatGPT settings, then Cloud browser. Three choices: Always ask (review every request yourself), Auto approve (it checks the site fits your task first), Always allow.
- [ ] Leave Always allow off. OpenAI: "We offer this option for minimal friction, but do not recommend this option."
- [ ] You can also allow or block individual websites there.
- [ ] Allowing a website doesn't approve every action on it.

## Logins
- [ ] At a login screen, Work pauses and asks you to sign in. An extra review model checks the request for signs of phishing (a fake page made to steal a login) first.
- [ ] Type your details only into the sign-in form ChatGPT gives you. OpenAI: "Use the sign-in form provided by ChatGPT. Don't send passwords in the chat."
- [ ] If offered, Sign in on web page instead lets you sign in on the page itself; the task pauses, and I'm done hands control back.
- [ ] Your sign-in stays active for future tasks.

## What's safe to paste
- [ ] No passwords, card numbers or codes in the chat.
- [ ] OpenAI: "Avoid sending secrets or highly sensitive data through browser tasks unless they're required and you are present to review each prompt."
- [ ] On an employer's or school's account: ChatGPT Work follows that workspace's privacy, security and data-handling policies. Check what your employer allows first.
- [ ] Your data controls: ChatGPT web or mobile, Settings, then Data controls.

## Pages can carry instructions (prompt injection)
- [ ] OpenAI, at the top of the browser page: "Treat page content as untrusted context." Its Work section: "We test the agent against risks including prompt injection, phishing, and unintended actions." Its section on the desktop app's built-in browser adds: "Instructions on a page can be misleading or malicious."
- [ ] If a page seems to steer Work somewhere you didn't ask, don't approve the request.

## Safety nets
- [ ] Confirmation: OpenAI: "ChatGPT Work will always ask for confirmation before consequential actions, such as submitting your information to book an appointment or completing a payment."
- [ ] Take over: "If ChatGPT is ever blocked for any reason, you can take over its computer and use it yourself on mobile and desktop."
- [ ] Safety review: if a task pauses for one, follow the notice and review any findings before continuing.

## Desktop app: browser extension (Chrome, Edge, Brave, Opera, Vivaldi)
- [ ] Before each new website it asks: Allow once, Allow for this site, Allow for all sites, Decline.
- [ ] Allow for all sites is marked Elevated Risk: "Only choose this option if you trust ChatGPT to use any website open in the browser."
- [ ] Browser history access is also marked Elevated Risk, and has no always-allow option.
- [ ] Allowed and blocked sites: desktop app, Settings, then Computer Use, then Manage next to your browser.

## Desktop app: permission modes
- [ ] The permissions control below the message box: Ask for approval, Approve for me, Full access, Custom (config.toml). OpenAI: "A mode can be disabled or omitted when it isn't available."
- [ ] OpenAI: "For most work, start with Ask for approval."
- [ ] Full access is "Unrestricted access to the internet and any file on your computer".
- [ ] Computer Use asks before it uses each app. "Use Always allow only for apps you trust ChatGPT to use automatically in future tasks." Remove apps in Settings, then Computer Use, then Always allow.
- [ ] The desktop app's built-in browser has its own settings: Settings, then Browser, then Agent permissions.

## Check it worked
- [ ] Settings, then Cloud browser: not set to Always allow.
- [ ] The permissions control in your current chat says Ask for approval. OpenAI: "Check the selected mode for the current chat; having a mode available doesn't mean it's selected."
- [ ] Desktop app, Settings, then Computer Use, then Manage: only sites you meant to allow.

## Afterwards
- [ ] Settings, then Cloud browser, then Browser data: delete one site (signs you out of it) or Clear all (signs you out of every site in Work's browser).
- [ ] Desktop app built-in browser: Settings, then Browser, then Clear browsing data.

Sources: learn.chatgpt.com/docs/browser ; /docs/chrome-extension ; /docs/permission-modes ; /docs/computer-use ; /docs/enterprise/chatgpt-work-overview ; /docs/get-started-with-work ; /docs/app
