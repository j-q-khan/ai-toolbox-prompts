# Your first Replit app, step by step (checklist, facts checked 2026-11-24)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as replit-first-app-checklist.md. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every fact below is from Replit's own docs, blog or pricing page on 2026-11-24. Nothing was signed up for, installed, run, built or published. Prices, plans and terms change: check each page before you pay.

## Before you start: the plan
- [ ] Replit's help page says "Starter is free"; its pricing page listed only Core ($20 a month, or $18 a month billed annually), Pro ($100, or $90 billed annually) and Enterprise. The two disagree; this checklist follows Core. https://replit.com/pricing
- [ ] Replit's docs say Starter gets "1 free published app" whose link "will automatically go down after 30 days", and Lite build only. https://docs.replit.com/billing/plans/starter-plan
- [ ] "Credits apply to Replit AI usage, publishing, storage, and other usage-based services." "Replit asks for confirmation before a paid action starts." https://docs.replit.com/help/pricing-and-plans Planning can cost too: "Paid requests can incur charges even when they only produce an explanation or plan." https://docs.replit.com/features/agent/plan-mode
- [ ] Training: "We use content you provide, including your prompts ... to help develop and improve our models". Pro users opt out at Settings, Personalization, Model Improvement; the page says nothing about Core. Keep real customer names and passwords out of every prompt. https://docs.replit.com/legal-and-security-info/model-improvement

## 1. Prompt and plan
- [ ] Describe the app in the chat box: the pages, what a user does, what to save, made-up test data only.
- [ ] End with: Plan this first, and wait for my OK before you build. (The Plan toggle is gone: "You can simply ask Replit to plan".) https://docs.replit.com/features/agent/plan-mode
- [ ] Approve the task list only when every page is on it.
- [ ] Agent 4: you can open a new chat to plan the next piece while it builds. https://replit.com/blog/whats-changed-agent3-to-agent4

## 2. Preview and fix
- [ ] The preview opens when the app runs (Preview tab, beside Tools). It's private: only you can use it. https://docs.replit.com/features/editor/preview
- [ ] Do every user step in order; check each button does something.
- [ ] Something wrong? Describe that one thing and ask for only that fix.
- [ ] Check phone size with the Screen size presets in the preview bar.

## 3. Sign-ins with Replit Auth
- [ ] Ask the agent: "...and it should feature Replit Auth." "The only way to implement Replit Auth is by using Agent." https://docs.replit.com/replit-workspace/replit-auth
- [ ] Know this: your app's users sign in with a Replit account, on a Replit-branded login page. For accounts not tied to Replit, Replit's docs name Clerk Auth.
- [ ] Sign in the way a customer would; check the account appears under Tools, Users & Auth, Users tab.

## 4. Publish
- [ ] Publish (top right of the workspace), check the replit.app name, set who can open it to Public, then Publish in the pane. Keep the tab open. https://docs.replit.com/build/publish-your-app
- [ ] Two databases: development (you and the agent) and production (your published app, made when you publish, billed for compute and storage). "Agent is not able to modify the production database." Only copy development data into production if it's safe for real customers. https://docs.replit.com/cloud-services/storage-and-databases/create-production-database-when-publishing
- [ ] Share the replit.app link, never the preview link ("private by default, temporary").
- [ ] Open the published link yourself, sign in the way a customer would and do every step again.
- [ ] Changed something? Click Republish: same link, new version.

## 5. iPhone
- [ ] Ask the agent to add a mobile app to the same build ("You're not locked into one type"). https://docs.replit.com/replitai/agent
- [ ] Install Expo Go on your phone; Preview panel, Open in Expo Go; scan the code. https://docs.replit.com/replitai/building-mobile-apps
- [ ] Apple Developer Program membership "with two-factor authentication". https://docs.replit.com/build/mobile-app
- [ ] Publish the web app first; then Publishing, Start publishing to the App Store; Launch: sign in with Apple, choose your app's name and bundle ID (permanent once you've published), Launch to App Store. "Publishing can take up to 45 minutes." https://docs.replit.com/build/mobile-upload-ios
- [ ] TestFlight, then finish the listing in App Store Connect and click Add for Review (top right). Apple reviews every submission. https://docs.replit.com/build/mobile-publish-ios
- [ ] "Publishing to Google Play is not yet supported by Replit." Android users can open your web link.

## If a change breaks it
- [ ] Agent tab, history icon, roll back to the last good checkpoint. "By default, rollbacks do not change your database." https://docs.replit.com/replitai/checkpoints-and-rollbacks

## Take your files with you
- [ ] Three-dot menu at the top of the file tree, Download as zip. https://docs.replit.com/help/projects-and-files
