Paste this into Lovable's chat with Build selected, in the Test Bakery app from Part 2, after you've connected your own Supabase account (Settings, General, External Supabase). It adds email logins and one reservations table, on made-up details only. Written from Lovable's Connect to Supabase and security docs and Supabase's API keys docs, checked 2026-11-17.

Goal: add email and password logins and one reservations table to the Test Bakery site, using the Supabase database already connected to this app, with made-up details only.
Steps, in order:
1. First check that More, then Supabase shows a connected Supabase database. If it doesn't, stop and tell me, and don't switch on the built-in backend.
2. Tell me in one sentence what you'll build, and that you'll ask before any change to the database.
3. Add email and password sign-up and sign-in pages, and a Sign in button at the top of the site.
4. Add a Reserve button to each menu item. A signed-in customer picks a pickup day, and a My reservations page shows only that customer's own reservations.
5. Keep reservations in one table, tied to each customer. Show me the database change and wait for my approval before you run it.
6. Set the table's access rules so each customer can only see, add or cancel their own reservations, and list every rule in plain words.
7. Never put a secret key in the app's code. Only the publishable key, or its Legacy name anon, may be in the browser.
8. Check it yourself: a signed-up test customer can reserve an item and see it under My reservations, and a signed-out visitor can't see any reservations. Tell me the result.
Safety: made-up details only (test@example.com), no real customer data, no payments, no emails sent to customers, no outside services. Keep everything else unchanged once it works.
Output: the working app, the list of access rules in plain words, and a three-line summary of what changed.
