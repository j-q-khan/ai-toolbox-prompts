Paste this into the chat of your Lovable app (with Build picked). Messages in the chat use credits, while running the scans from the Security view is free. It asks Lovable to check every table's Row Level Security and look for any secret key in the app's front-end code, and to change nothing until you agree. Use it on an app with made-up data only. Written from Lovable's and Supabase's docs, checked 2026-11-17.

Goal: check my app's security before real users sign up, and change nothing until I say yes.
Steps, in order:
1. List every table in my database. For each one, tell me whether Row Level Security is on, and list its policies in plain words: who they apply to (signed in or not) and what they allow (seeing, adding, changing, deleting).
2. For each table, say whether every policy checks the row's owner, or only that someone is signed in. Flag any policy that lets everyone through.
3. Search the app's front-end code and the connected GitHub repository for any secret key, any key starting with sb_secret_, and any service_role key. Tell me the file and line, but never show the key's value.
4. Confirm the app's pages use only the publishable key.
5. Run the Quick scan and a Deep scan, and summarise the findings in plain words, most serious first.
6. Give me a numbered list of fixes, each with what it changes and why. Don't change anything, run any database change or publish anything until I reply with the numbers I agree to.
Safety: made-up data only, never print a secret key's value, never turn Row Level Security off, and never move a secret or service_role key into the browser.
Output: the table list, the key search result, the scan summary and the numbered fixes.
