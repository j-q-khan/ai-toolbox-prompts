# Full code: AI App Builder: Replit, Bolt or Base44? Which One to Use for Your App

The checklist, the first-prompt template and the test idea file for this video, written from each builder's own docs, help and pricing pages (checked 2026-11-24). They were written from the docs, not run, and nothing was built or published for this video.

### 1. ai-app-builder-checklist.md
```
# Replit, Bolt.new or Base44: which AI app builder fits your app (checklist, facts checked 2026-11-24)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as ai-app-builder-checklist.md. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every fact below is from the maker's own page on 2026-11-24. Nothing was signed up for, installed, run, built or published. Prices, plans and terms change: check each page before you pay.

## The words
- [ ] Prompt: the description you type.
- [ ] Agent: the program that plans the steps and builds the app.
- [ ] Preview: a working copy only you can try. Publish: putting it on the web at its own web address.
- [ ] Database: where the app keeps its information. Login and authentication: the app checking who you are.
- [ ] Credits and tokens: how each builder limits its agent.

## A quick tool you share today: Bolt.new (StackBlitz)
- [ ] Publish (top right) gives "a free bolt.host address". "Custom domains require a paid plan." https://support.bolt.new/bolt-cloud
- [ ] "Bolt creates a database when your project needs one". Email sign-up; Google sign-in needs your own Google Client ID and secret. https://support.bolt.new/cloud/database/authentication
- [ ] Free was $0: "300K tokens daily limit", "1M tokens per month", "Bolt branding on websites". Pro was $25 a month, billed monthly: your own domain, "No Bolt branding on websites", "Start at 10M tokens per month", "Unused tokens roll over to next month". https://bolt.new/pricing

## Logins and saved data: Base44 (owned by Wix)
- [ ] Free plan lists "Authentication, database functionality, analytics", 25 message credits a month, up to 5 apps. https://base44.com/pricing
- [ ] "The AI sets up your tables so the right information is saved and kept up to date for you." https://docs.base44.com/Building-your-app/Managing-your-app-data
- [ ] Sign-in methods: email and password, Google, Microsoft, Facebook, Apple. https://docs.base44.com/Setting-up-your-app/Managing-login-and-registration
- [ ] Starter was $16 and Builder $40 a month, billed annually.

## An iPhone app with native screens: Replit
- [ ] Built with Expo; "renders platform-native UI components (not a webview)". https://docs.replit.com/replitai/building-mobile-apps
- [ ] Builds in the cloud and submits to App Store Connect for TestFlight beta review; needs an Apple Developer Program membership with two-factor authentication. https://docs.replit.com/build/mobile-app
- [ ] "Publishing to Google Play is not yet supported by Replit."
- [ ] Logins: ask Agent for Replit Auth ("...and should feature Replit Auth."). https://docs.replit.com/replit-workspace/replit-auth
- [ ] Plans: the help page says "Starter is free"; the pricing page listed only Core ($20 a month, $18 billed annually), Pro and Enterprise. Go by the pricing page on the day. https://replit.com/pricing

## Both phone stores: Base44 or Bolt.new
- [ ] Base44: "a lightweight native wrapper around your web app"; the store scan runs on the Free plan, the store files need Builder or higher. https://docs.base44.com/documentation/building-your-app/uploading-to-app-stores
- [ ] Bolt.new: both stores through Expo, outside Bolt, by command line; Node.js LTS, Git, an Expo account, Apple and Google developer accounts. https://support.bolt.new/integrations/expo
- [ ] Every store: your own paid developer account, and Apple's or Google's review.
- [ ] Want a phone app? Say "mobile app" in your very first prompt (Bolt); choose Mobile app as the app type (Replit).

## Who can train on what you type
- [ ] Bolt.new: from October 7, 2026, unless you opt out ("at any time, free of charge and regardless of your plan, through your account settings"); Teams and Enterprise are left out. https://stackblitz.com/terms-of-service
- [ ] Base44: "All other plans, including Business: your data can be used to train AI models." "There is no opt-out setting to find or switch on." https://docs.base44.com/Community-and-support/Privacy-and-security
- [ ] Replit: Pro users opt out at Settings, Personalization, Model Improvement; Enterprise not used for training; Core not stated. https://docs.replit.com/legal-and-security-info/model-improvement
- [ ] Keep real customer details and passwords out of every prompt; use made-up test data.

## Taking your app with you
- [ ] Replit: three-dot menu at the top of the file tree, Download as zip. https://docs.replit.com/help/projects-and-files
- [ ] Bolt.new: project title (top left), Download; desktop only. https://support.bolt.new/building/using-bolt/rollback-backup
- [ ] Base44: GitHub 2-way sync, Builder plan or higher. https://docs.base44.com/developers/app-code/local-development/github
- [ ] Ownership: Bolt, "All code that you create with Bolt and StackBlitz is your own code"; Base44, "ownership of an app belongs to the person who created the app on the platform".

## Not covered here
- [ ] Firebase Studio: Google is sunsetting it; open until March 22, 2027. Google points to Google AI Studio or Antigravity. https://firebase.blog/posts/2026/03/announcing-ai-studio-integration/
```

### 2. first-prompt-template.txt
```
# A first prompt for any AI app builder, written for this video (2026-11-24). Not run: nothing was built.
# To keep a copy: paste this into Notepad and save it as first-prompt-template.txt with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Fill in each line, then paste the finished prompt into Replit, Bolt.new or Base44 as one message.
# Keep real customer details and passwords out of it: use made-up test data.

App: [name, e.g. Test Bakery orders]
What it does: [one sentence, e.g. customers order a cake and pick a pickup time]
Who uses it: [e.g. bakery customers on their phones, and the bakery owner]
Pages: [e.g. menu, order form, thank-you page, owner's order list]
Sign-in: [yes or no; if yes, email and password]
Saves: [e.g. each order: name, cake, pickup time]
Phone app: [no / iPhone / both stores; say "mobile app" here if yes]
Test data: Use made-up test data only, like Test Customer and test@example.com.

# Example:
# App: Test Bakery orders. What it does: customers order a cake and pick a pickup time. Who uses it: bakery customers and the owner. Pages: menu, order form, thank-you page, owner's order list. Sign-in: yes, email and password. Saves: each order's name, cake and pickup time. Phone app: no. Use made-up test data only.
```

### 3. app-idea.txt
```
# Test answers for the Claude build prompt: key: answer, one per line.
# To keep a copy: paste this into Notepad and save it as app-idea.txt with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# The lines starting with # are notes for you, and the script skips them. Made-up data only.
name: Test Bakery orders
what_it_does: customers order a cake and pick a pickup time
who_uses_it: bakery customers and the bakery owner
sign_in: yes
saves_data: yes
phone: none
share_today: no
budget_per_month: 20
pages: menu, order form, thank-you page, owner's order list
```
