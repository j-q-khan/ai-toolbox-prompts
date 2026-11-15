# Full code: Claude Code Login Expired or Error 401/403? Fix Sign-In Problems

A sign-in checklist written for this video from Anthropic's Claude Code docs (checked 2026-11-15, Claude Code 2.1.325). Messages and command names are as the docs gave them that day; check the linked page if one looks different.

### 1. claude-code-sign-in-checklist.md
```
# Claude Code sign-in checklist: login expired, 401, 403 (from Anthropic's docs, checked 2026-11-15)

## First: which sign-in is active?
- [ ] Type /status at the Claude Code prompt. It shows version, model and account, and which credential is active.
- [ ] A Login row saying "Expired — log in again" means your saved sign-in ran out.
- [ ] If a login and an API key are both set up, /status marks the one that isn't in use.

## Expired, revoked or missing: /login
- [ ] "Login expired · Please run /login": the automatic renewal failed and the saved sign-in was cleared. Type /login.
- [ ] "OAuth token revoked · Please run /login": you signed out everywhere or an admin removed access. Type /login.
- [ ] "Please run /login · API Error: 401 OAuth token has expired ...": the renewal failed mid-session. Type /login.
- [ ] "Not logged in · Please run /login": no sign-in at all. Type /login.
- [ ] In the Claude Desktop app it says "Authentication required · Sign in again to continue": sign in again from the app.
- [ ] From a script (claude -p): "Failed to authenticate: OAuth session expired and could not be refreshed". Run claude in the same place, complete /login, then run the script again.
- [ ] "OAuth error: Invalid code. Please make sure the full code was copied": the code timed out or was cut off. Press Enter and sign in soon after the browser opens.
- [ ] Browser doesn't open, or it signs you in but the terminal never finishes: press c to copy the sign-in link, open it in your browser, and paste the code it shows at "Paste code here". If pasting does nothing, exit and run: claude auth login

## 401 Invalid authentication credentials
- [ ] "Please run /login · API Error: 401 Invalid authentication credentials": an expired sign-in isn't the cause. Type /status.
- [ ] /status shows an API key in use? An approved ANTHROPIC_API_KEY takes precedence over your login, so /login doesn't replace it.
      Exit Claude Code, then clear it for this window (nothing in your account is deleted) and start claude again from the same window:
      Windows PowerShell:  Remove-Item Env:ANTHROPIC_API_KEY
      Mac or Linux:        unset ANTHROPIC_API_KEY
- [ ] Stop it coming back: Windows, delete ANTHROPIC_API_KEY from your User environment variables (Environment Variables settings) and from your PowerShell profile ($PROFILE); Mac, delete the export line from ~/.zshrc (or ~/.bashrc, ~/.profile) in a text editor (in Finder, Shift-Command-G and type the path) and save it as plain text. Then open a new window.
- [ ] Interactive Claude Code asks once whether to use a key it finds; to change that choice later, use the "Use custom API key" toggle in /config (it shows only while the key is set).
- [ ] /status shows only your login? Type /login once. Same 401 again on the same account: the account or organization is no longer active. Ask your organization admin.

## 403 Request not allowed (after signing in)
- [ ] Pro, Max or Ultra: check your subscription is active at claude.ai/settings.
- [ ] Claude Console account: you need the "Claude Code" or "Developer" role. An admin assigns it on the Console's Members page (platform.claude.com/settings/members).
- [ ] At work behind a proxy: corporate proxies can interfere. Ask your network admin; setup: code.claude.com/docs/en/network-config

## Asked to log in again and again
- [ ] Check your computer's clock is accurate (sign-in checks depend on correct timestamps). Turn on automatic time in your date and time settings.
- [ ] Update Claude Code: before 2.1.211, waking from sleep could sign every open session out at once. Command: claude update
- [ ] Clean reset: type /logout, exit Claude Code, start claude, sign in again.
      Note: logging out removes all stored credentials, including saved MCP server logins and plugin secrets. Expect to sign in to those again.
- [ ] Mac: run claude doctor in the Terminal. If it warns "macOS Keychain is not writable", unlock it:
      security unlock-keychain ~/Library/Keychains/login.keychain-db
      (asks for your Keychain password), then run claude doctor again. Still warning? Open Keychain Access, select the login keychain, choose Edit, then Change Password for Keychain "login", then claude doctor again. Then /logout and /login.

## Check it worked
- [ ] /status: no Expired row, and your Claude account shown rather than a key.
- [ ] Send a short message: Claude answers without asking you to log in.

## Still stuck?
- [ ] Search or open an issue: github.com/anthropics/claude-code/issues
- [ ] Account problem (login loop, subscription not recognised, disabled organization): sign in at claude.ai, click your initials in the lower left, select Get help.

Docs: code.claude.com/docs/en/errors (Authentication errors) and code.claude.com/docs/en/troubleshoot-install (Login and authentication)
```
