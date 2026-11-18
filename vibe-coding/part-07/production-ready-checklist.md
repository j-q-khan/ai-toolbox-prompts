# Make your Lovable app production ready: checklist (facts checked 2026-11-17)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Production ready here means safe for real users. Use made-up data (Test Bakery, test@example.com) until every box is ticked: Lovable's docs say Row Level Security "is much easier to change before real data exists".

## Row Level Security on every table
- [ ] Every table has Row Level Security switched on. Supabase's docs: "Enable RLS on every table in an exposed schema."
- [ ] Own Supabase: in the Supabase dashboard, open the Security Advisor. No table shows "Table publicly accessible" (Row Level Security off) or "No access rules defined" (on, but no policies, so nothing gets through).
- [ ] Lovable's built-in backend: More, then Database, then Manage, then Policies. Every table you use has its policies. This view is read-only; ask Lovable in the chat to change a policy.
- [ ] One policy for each action you allow: select (seeing), insert (adding), update (changing), delete (deleting). Supabase: "Write a separate policy for select, insert, update, and delete."
- [ ] Each policy checks the row's owner, not only that someone is signed in. Lovable: "If a policy checks only for authenticated, every signed-in user gets the same access to every row that policy covers."
- [ ] No policy lets everyone through (Supabase flags "USING (true)" or "WITH CHECK (true)" as "Security policy allows unrestricted access"), except on data that is meant to be public.
- [ ] Test with two made-up accounts: each one sees only its own entries.

## Keys
- [ ] The app's pages use only the publishable key (sb_publishable_...). Lovable: "Anyone using your app can see the publishable key, and that is intended". Your policies are what protect your data.
- [ ] The secret key (sb_secret_...) is nowhere in the app's code or on GitHub. Supabase: "Never put one in a browser, a shipped application, or source control."
- [ ] Older tutorials call the keys anon (publishable) and service_role (secret). Supabase calls these Legacy and "is deprecating the anon and service_role keys by the end of 2026". Never paste a service_role key into the app. A long key starting with eyJ is a legacy key.
- [ ] Any other secret (payments, email) is stored in Lovable's Secrets, never in the app's code. Lovable: "Secrets stored in frontend code are visible to users and should be considered compromised."
- [ ] If a secret key ever got out, follow Supabase's steps to rotate a leaked key (supabase.com/docs/guides/api/api-keys).

## Lovable's scans
- [ ] Quick scan: runs when you open the publish dialog (click Publish, top right of the editor). The result shows on one line. Click it to open the Security view.
- [ ] Deep scan: in the Security view (More, then Security), click Run deep scan. It reviews all your app's code, including users who can see or change data that isn't theirs and secrets in your code or repository.
- [ ] Running either scan is free. Asking Lovable in the chat to review security uses credits.
- [ ] Every Critical finding is fixed (Try to fix, Fix all, or by hand). Fixing findings uses your account's 10 free fixes first, each available again 24 hours after you use it.
- [ ] Built-in backend: if Review security findings appears when you click Publish, pick Review or Try to fix, not Publish anyway.
- [ ] Workspace admins can switch on Block publishing with critical issues (Workspace settings, Security, Privacy and security, Publishing).

## The error "new row violates row-level security policy for table"
- [ ] The likely cause is that no policy lets that new row in: no policy for adding, the row doesn't name its owner, or nobody is signed in.
- [ ] Fix: ask Lovable for a policy for adding rows (signed-in users only, owner checked) and for the app to fill in the owner. Use fix-new-row-prompt.txt.
- [ ] Never fix it by switching Row Level Security off or by putting the service_role key in the browser. Lovable: "that key skips every policy you have."
- [ ] On a file upload, see Supabase's page for that case: it happens with upsert: true, and the fix is to leave upsert off or add a matching SELECT policy on storage.objects.

## Before real users
- [ ] Logins: switch Confirm email back on in Supabase (Authentication, Sign In / Providers, Email) if you turned it off for testing in Part 3.
- [ ] Leaked password protection is on (built-in backend: More, Users, Settings, Email, Password HIBP check).
- [ ] Lovable's docs say the scans "cannot guarantee complete security". For apps handling sensitive data, consider a professional security review.

Sources: supabase.com/docs/guides/database/postgres/row-level-security ; supabase.com/docs/guides/database/database-advisors ; supabase.com/docs/guides/api/api-keys ; supabase.com/docs/guides/troubleshooting (storage error 403 new row violates row-level security policy on upload) ; docs.lovable.dev/features/security ; docs.lovable.dev/features/publish ; docs.lovable.dev/features/security-view ; docs.lovable.dev/tips-tricks/security-best-practices ; docs.lovable.dev/features/database-access ; docs.lovable.dev/integrations/supabase
