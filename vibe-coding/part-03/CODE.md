# Full code: Supabase With Lovable: Add Logins and a Database

The prompts from this video and a setup checklist, written from Lovable's and Supabase's official docs (checked 2026-11-17). They were written from the docs, not run for this video.

### 1. bakery-backend-prompts.txt
```
# Use these in the Test Bakery app from Part 2, AFTER you've connected your own Supabase account
# (in the editor: Settings, then General, then External Supabase, then Connect).
# Send each prompt on its own in the chat, with Build picked, after the one before has finished.
# Made-up details only. Written from Lovable's Connect to Supabase docs, checked 2026-11-17.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

# Prompt 1, logins:
Add email and password login, with a Sign in button at the top.

# Prompt 2, one table. Lovable shows the database change and asks you to approve it in the chat.
Add a Reserve button to each menu item. Signed-in customers pick a pickup day, and a My reservations page shows only their own reservations.
Keep reservations in one table, tied to each customer.
```

### 2. backend-setup-checklist.md
```
# Add logins and a database with your own Supabase: checklist (facts checked 2026-11-17)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Decide first
- [ ] Lovable's built-in backend is on by default and built on Supabase's open-source foundation. Lovable's docs say most apps never need their own Supabase account.
- [ ] Pick your own Supabase if you want your own account and billing and the full Supabase dashboard.
- [ ] Switching later isn't automatic, in either direction. Decide before you ask for logins or saved data.
- [ ] Optional: Account settings, Preferences, Agent permissions, Manage, then set Enable Cloud to Ask each time, so Lovable asks before switching the built-in backend on.

## Connect your own Supabase (before any login or data prompt)
- [ ] A Supabase account at supabase.com. The Supabase free plan was $0 a month with a limit of 2 active projects when checked on 2026-11-17 (supabase.com/pricing).
- [ ] Your app has no backend yet (the Part 2 prompt ended with: No login or database yet).
- [ ] In the editor: Settings, then General, then External Supabase, then Connect.
- [ ] First time: Add Organization, then sign in and authorize Lovable in the Supabase window.
- [ ] Click Continue. Pick your database and click Connect next to it. Empty list? Create Project opens the Supabase dashboard: create one there and come back.
- [ ] Check: More, then Supabase shows its name and status.
- [ ] "Let Lovable create your Supabase project" only works where the built-in backend is disabled for the workspace (some Enterprise workspaces), per Lovable's docs.
- [ ] Each Lovable app connects to one Supabase database. A warning icon next to a database means another Lovable app already uses it.

## Logins and one table
- [ ] Prompt 1 from bakery-backend-prompts.txt. New sign-ups appear in the Supabase dashboard under Authentication.
- [ ] While testing only: Supabase dashboard, Authentication, Sign In / Providers, Email, switch off Confirm email. Switch it back on before real customers sign up.
- [ ] Prompt 2. Approve the database change in the chat. The table appears in the Supabase dashboard's Table Editor.
- [ ] Test with made-up details only (test@example.com): sign up, reserve an item, see it under My reservations and as a new entry in the table.

## Keys
- [ ] Publishable key (starts sb_publishable_): safe in your app's code; it only reaches what Row Level Security allows.
- [ ] Secret key (starts sb_secret_): never in a browser, an app you ship, or GitHub. It bypasses Row Level Security.
- [ ] Old names: anon (publishable) and service_role (secret) are Legacy; Supabase is deprecating them by the end of 2026.
- [ ] Your keys are in the Supabase dashboard under Settings, then API Keys.
- [ ] Lovable keeps other secret keys (payments, email) in your Supabase database's secret store, never in the app's code.

## Before real users
- [ ] Lovable sets up basic Row Level Security rules automatically. Review them before any real data (Part 7 of this series).
- [ ] Confirm email switched back on.
- [ ] No real customer data until every table's rules are checked.

## Keep it awake
- [ ] Supabase's free plan paused free projects after 1 week of inactivity, when checked on 2026-11-17. Supabase emails a warning about a week before.
- [ ] Paused: Supabase dashboard, pick the organization and the paused database, Resume project. Data comes back. You can restore for up to 1 year.
- [ ] Lovable can't connect to a paused database: resume it first.

## Trade-offs to know
- [ ] With your own Supabase, these Lovable features need the built-in backend instead: the Database, Users and Storage views in Lovable, Lovable-managed backups, signed-in browser testing, and setting up social logins from the chat.

Sources: docs.lovable.dev/integrations/supabase ; docs.lovable.dev/features/cloud ; docs.lovable.dev/introduction/lovable-account-settings ; docs.lovable.dev/tips-tricks/security-best-practices ; supabase.com/docs/guides/api/api-keys ; supabase.com/docs/guides/database/postgres/row-level-security ; supabase.com/docs/guides/auth/passwords ; supabase.com/docs/guides/platform/project-pausing ; supabase.com/pricing
```
