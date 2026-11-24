# Full code: Bolt.new Tutorial: Build an App From One Prompt and Publish It

The bakery prompt, the Bolt pre-publish checklist and the test idea file for this video, written from Bolt's own help centre, Bolt's pricing page and StackBlitz's terms (checked 2026-11-24). They were written from the docs, not run, and nothing was built or published for this video.

### 1. bolt-bakery-prompts.txt
```
# The prompts from this video, for Bolt.new, written for this video (2026-11-24). Not run: nothing was built.
# To keep a copy: paste this into Notepad and save it as bolt-bakery-prompts.txt with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Before the first prompt: Bolt homepage, your account name, Account settings, General, turn off Model training.
# Keep real customer names and passwords out of every prompt: use made-up test data.

# 1. The one prompt: paste it into the chat box on the Bolt homepage, then click Build now. Give it about five minutes.
Build an order page for Test Bakery. Customers pick a cake and a pickup time and place an order. Create user email sign up and log in, and show signed-in customers only their own orders. Save each order: name, cake, pickup time. Use made-up test data only.

# 2. When one thing in the preview is wrong: describe that one thing, and ask for only that fix.
The pickup times don't show on the order form. Fix only that.

# Want a phone app instead? Start the very first prompt with: Build a mobile app for Test Bakery.
```

### 2. bolt-publish-checklist.md
```
# Your first Bolt.new app, from one prompt to a bolt.host link (checklist, facts checked 2026-11-24)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as bolt-publish-checklist.md. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every fact below is from Bolt's help centre, Bolt's pricing page or StackBlitz's terms and privacy policy on 2026-11-24. Nothing was signed up for, installed, run, built or published. Prices, plans and terms change: check each page before you pay.

## Before your first prompt
- [ ] Open bolt.new in Chrome or a Chromium browser (Edge, Brave, Opera, Vivaldi). Click Get started and sign up. https://support.bolt.new/get-started/quickstart
- [ ] Model training: Bolt homepage, your account name in the sidebar, Account settings, General, Model training: off. "Default is on, except for accounts based in the EU, UK, or Switzerland." https://support.bolt.new/settings/account-settings
- [ ] Why: StackBlitz's terms (section 3.5) let it use what you make in Bolt from October 7, 2026 "to train, fine-tune, evaluate, benchmark, and improve artificial-intelligence models", and license de-identified datasets "to third parties, including for compensation", unless you opt out (account settings, or email privacy@stackblitz.com). Opt-outs take effect within 15 days and don't unwind "models already trained". Teams and Enterprise workspaces are excluded. https://stackblitz.com/terms-of-service and https://stackblitz.com/privacy-policy
- [ ] Bolt Forge (an open-source-model agent on the Lite and Pro plans; after its research preview ends November 30, 2026, existing Lite subscribers only) uses your data for training as a condition, and the opt-out doesn't apply while it's on. https://support.bolt.new/account/bolt-forge
- [ ] Keep real customer names and passwords out of every prompt: made-up test data only.

## Plan and tokens (when checked, 2026-11-24)
- [ ] Free: "$0 /month", "300K tokens daily limit", "1M tokens per month", "Bolt branding on websites", "Up to 333k web requests". Pro: "$25 /month", "Billed monthly", "No daily token limit", "Start at 10M tokens per month", "Custom domain support". Teams: "$30 /month", "Per member, billed monthly". https://bolt.new/pricing
- [ ] Bolt's QuickStart walkthrough "will use just under 300K tokens, which is the daily limit of Bolt's free plan." Free daily tokens reset every day; monthly ones on the 1st. https://support.bolt.new/account/tokens

## 1. One prompt
- [ ] Say what a customer does, ask for email sign up and log in, say what to save, and use made-up data.
- [ ] A phone app? Put the words mobile app in your very first prompt: "Projects created for web do not easily switch over to mobile." https://support.bolt.new/integrations/expo
- [ ] Click Build now. Apps with sign-ups take longer: about five minutes.

## 2. Preview and fix
- [ ] Sign up with a test email and do every customer step in the preview.
- [ ] Something wrong? Describe that one thing and ask for only that fix.

## 3. Database and sign-ups
- [ ] Database icon (top centre): open each table and check your test entries are there. https://support.bolt.new/bolt-cloud/database
- [ ] Database icon, Authentication: "Allow new users to sign up" (on by default); Email; "Prevent leaked passwords" (on by default when Bolt creates the database). https://support.bolt.new/bolt-cloud/database/authentication
- [ ] Bolt's default email service sends at most "2 auth emails per hour for your whole project" (sign-up confirmations, password resets): fine for testing, not for real customers.
- [ ] Google sign-in: your own Google Client ID and Client Secret go into Authentication, Continue with Google. Never paste them into the chat. Test Google sign-in on the published site, not the preview.

## 4. Publish
- [ ] "On the Free plan, all published sites are public", and search engines can list them. https://support.bolt.new/cloud/hosting/publish
- [ ] Publish (top right, not Share), then the second Publish button. Wait about a minute; open the link in the chat.
- [ ] Change the random bolt.host name with the pencil icon (Edit domain) in the Publish menu.
- [ ] Open the link yourself, sign up with a second test email, do every customer step, and find the entry in your table.
- [ ] Changed something? Publish menu, Update. Changes don't reach the published site by themselves.
- [ ] Use the Publish and Update buttons: they "don't use tokens". Prompting Bolt to publish "decreases your token balance".
- [ ] Over your plan's hosting limit, the site "stops displaying publicly" until usage resets. Free plan sites show a Made in Bolt badge. Custom domains need a paid plan. https://support.bolt.new/bolt-cloud/hosting

## 5. Take it with you
- [ ] On a computer: your app's name (top left), Download, a zipped folder. Not on a phone. https://support.bolt.new/managing-projects/rollback-backup
- [ ] GitHub icon (top right), Log in to GitHub, Create repository; it "starts as private", and Bolt commits every change that doesn't break the app. https://support.bolt.new/integrations/git
- [ ] Ownership: "All code that you create with Bolt and StackBlitz is your own code". StackBlitz's terms add that "AI Output may not be protectable by copyright". https://support.bolt.new/account/corporate-commercial

## Phone apps (outside Bolt)
- [ ] App store publishing is by command line with Expo's EAS tools, on a computer with Node.js LTS and Git, plus an Expo account and paid Apple and Google developer accounts. Bolt's Expo page lists the steps. https://support.bolt.new/integrations/expo

## If a change breaks it
- [ ] Version history (clock icon, top menu), pick a version, Restore this version. "Restoring your site to a previous version doesn't use tokens!" and it "will not change your current Bolt or Supabase databases."
```

### 3. bolt-idea.txt
```
# Test answers for the Claude build prompt: key: answer, one per line.
# To keep a copy: paste this into Notepad and save it as bolt-idea.txt with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# The lines starting with # are notes for you, and the script skips them. Made-up data only.
name: Test Bakery
what_it_does: customers order a cake and pick a pickup time
who_uses_it: bakery customers and the bakery owner
customer_steps: sign up, pick a cake, pick a pickup time, place the order, see my orders
saves: name, cake, pickup time
sign_up: yes
kind: web
```
