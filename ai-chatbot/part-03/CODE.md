# Full code: AI Chatbot With Dify: Build One and Put It on Your Website



### 1. dify-selfhost.sh
```
#!/usr/bin/env bash
# Self-host Dify with Docker Compose. From AI Chatbot, Part 3.
# Written from Dify's docs, "Deploy Dify with Docker Compose", and docker/README.md at release 1.20.0:
#   https://docs.dify.ai/en/self-host/deploy/quick-start/docker-compose  (checked 2026-11-22; written from the docs, not run)
# Before you start (the docs' list): Docker with Docker Compose 2.35.0 or later, with Docker running; Git; OpenSSL.
#   At least 2 CPU cores and 4 GiB of RAM. On a Mac, give Docker Desktop's virtual machine at least 2 virtual CPUs
#   and 8 GiB of memory. On Windows, use Docker Desktop with WSL 2, and run this file in a WSL terminal, inside the
#   Linux file system (for example your Linux home folder), not in a Windows folder.
# What it does: downloads Dify 1.20.0 into a folder called dify, copies the settings template to .env, puts a random
#   secret into .env (the docs' openssl step), starts every service, then lists them.
# Lines marked "Not from Dify's docs" are safety steps we added.
# This is for a new install only. For an existing install, the docs say follow their Upgrade steps instead.
# How to save it: on a Mac, open TextEdit, choose Format, Make Plain Text, paste this text and save it as
#   dify-selfhost.sh in an empty folder. On Linux, use any plain text editor. On Windows, don't save it with Notepad
#   (Notepad can add Windows line endings, which bash rejects; this note is not from Dify's docs): in the WSL terminal,
#   type  nano dify-selfhost.sh , paste the text, press Ctrl+O, Enter and Ctrl+X, or download the file from the GitHub folder.
# How to run it: open Terminal (Mac) or your WSL terminal (Windows), go to that folder, type  bash dify-selfhost.sh
#   and press Enter. Then open http://localhost/install in your browser and create the administrator account.
# Before anyone else can reach it, the docs say: configure HTTPS and replace the bundled development credentials
#   in docker/.env (DB_PASSWORD, REDIS_PASSWORD and the others under "Secure the Deployment" on the docs page).
# Licence: Dify is "a modified version of the Apache License 2.0" with extra conditions. Check the LICENSE file in
#   the dify folder before any business use, and ask Dify in writing if you're unsure.
# Test use only: run it on a test machine with made-up documents, like the Test Bakery price list, and keep it
#   off the internet until HTTPS is set up and the development credentials are replaced.
set -euo pipefail

# Not from Dify's docs: stop if a dify folder is already here, so nothing is overwritten.
if [ -e dify ]; then
  echo "A folder called dify already exists here. Run this from an empty folder." >&2
  exit 1
fi

# Not from Dify's docs: if a step fails before Dify starts, remove the half-made dify folder and the temporary
# file, so nothing is left behind and you can run this again.
clone_dir="$(pwd)/dify"
tmp_env=""
started=no
cleanup() {
  status=$?
  if [ -n "$tmp_env" ]; then rm -f "$tmp_env"; fi
  if [ "$status" -ne 0 ] && [ "$started" = no ] && [ -d "$clone_dir" ]; then
    rm -rf "$clone_dir"
    echo "Something failed before Dify started, so the dify folder was removed. Fix the error above and run this again." >&2
  fi
}
trap cleanup EXIT

docker compose version

git clone --branch 1.20.0 --depth 1 https://github.com/langgenius/dify.git
cd dify/docker

cp .env.example .env

# The docs: generate a token with  openssl rand -hex 32  and set DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN in .env to it.
# Not from Dify's docs: this writes it into .env for you, without printing it.
if ! grep -q '^DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN=' .env; then
  echo "DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN wasn't found in .env. Set it by hand, as the docs say." >&2
  exit 1
fi
token="$(openssl rand -hex 32)"
tmp_env="$(mktemp)"
DIFY_TOKEN="$token" awk '/^DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN=/ { print "DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN=" ENVIRON["DIFY_TOKEN"]; next } { print }' .env > "$tmp_env"
mv "$tmp_env" .env
tmp_env=""
unset token

started=yes
docker compose up -d
docker compose ps --all
# The docs: long-running services should show Up or healthy, and init_permissions shows Exited (0) when it's done.
```

### 2. dify-embed-snippet.html
```
<!--
  Dify's chat bubble code, in the shape Dify 1.20.0 writes it under Access Point, Web App, Embed Into Site,
  the second option ("To add a chat app to the bottom right of your website add this code to your html.").
  Source: getEmbeddedScriptSnippet in web/app/components/app/overview/app-card-utils.ts, github.com/langgenius/dify,
  tag 1.20.0, and Dify's docs, Embed Your Web App:
  https://docs.dify.ai/en/cloud/use-dify/publish/webapp/embedding-in-websites  (checked 2026-11-22; written from the code and docs, not run)
  Don't copy these values: Dify writes your real code for you, with your app's own token, address and colour.
  YOUR-APP-TOKEN is a placeholder. https://udify.app is the address Dify's docs show for Dify Cloud; a
  self-hosted Dify uses your own server's address. #155EEF is the docs' default bubble colour.
  Publish your app first: "Your web app must be published before embedding."
  "Web apps are public by default": anyone with this code can chat with your bot. If it leaks, click
  Regenerate on the Web App card and paste the new code into your site.
  No model provider key is in this code, and none should be: your key stays in Dify's settings.
  Paste the whole block into your page's HTML, wherever your site builder lets you add custom code.
-->
<script>
 window.difyChatbotConfig = {
  token: 'YOUR-APP-TOKEN',
  baseUrl: 'https://udify.app',
  inputs: {
    // You can define the inputs from the Start node here
    // key is the variable name
    // e.g.
    // name: "NAME"
  },
  systemVariables: {
    // user_id: 'YOU CAN DEFINE USER ID HERE',
    // conversation_id: 'YOU CAN DEFINE CONVERSATION ID HERE, IT MUST BE A VALID UUID',
  },
  userVariables: {
    // avatar_url: 'YOU CAN DEFINE USER AVATAR URL HERE',
    // name: 'YOU CAN DEFINE USER NAME HERE',
  },
 }
</script>
<script
 src="https://udify.app/embed.min.js"
 id="YOUR-APP-TOKEN"
 defer>
</script>
<style>
  #dify-chatbot-bubble-button {
    background-color: #155EEF !important;
  }
  #dify-chatbot-bubble-window {
    width: 24rem !important;
    height: 40rem !important;
  }
</style>
```

### 3. bot-instructions.txt
```
# The chatbot's Instructions and first message. From AI Chatbot, Part 3. Our wording, for a made-up bakery.
# How to save this file:
#   Windows: open Notepad, paste this text, choose File, Save as, set the box called Save as type to All files,
#   and name it bot-instructions.txt
#   Mac: open TextEdit, choose Format, Make Plain Text, paste this text, and save it as bot-instructions.txt
# How to use it: in your Chatbot app's Orchestrate page, paste the INSTRUCTIONS lines into the Instructions box.
# Then click Features, turn on Conversation Opener, and paste the FIRST MESSAGE line. Swap in your own business
# name and email.

INSTRUCTIONS
You are the website assistant for Test Bakery.
Answer only from the Test Bakery documents in your knowledge.
If the answer is not in them, say you don't know and suggest emailing test@example.com.
Never claim to be a person.
Keep answers short and friendly.

FIRST MESSAGE
Hi, I'm Test Bakery's AI assistant, not a person. Ask me about our cakes, prices or delivery.
```

### 4. dify-embed-checklist.txt
```
# Dify chatbot on your website: an embed checklist. From AI Chatbot, Part 3.
# Facts checked 2026-11-22 from Dify's docs (docs.dify.ai), its pricing page and the Dify 1.20.0 app. Written from the docs, not run.
# How to save this file:
#   Windows: open Notepad, paste this text, choose File, Save as, set the box called Save as type to All files,
#   and name it dify-embed-checklist.txt
#   Mac: open TextEdit, choose Format, Make Plain Text, paste this text, and save it as dify-embed-checklist.txt
# How to use it: tick every line before you paste the bubble code into a real website.

THE PLAN (Dify Cloud, was this when checked on 2026-11-22)
[ ] Sandbox: 200 message credits, a one-time allocation that doesn't renew monthly; 5 apps; 50 knowledge documents
[ ] Sandbox uploads: 1 file per upload, up to 15 MB each; logs kept 30 days
[ ] I know what happens when credits run out: add my own key on the provider's card, billed to my account
[ ] My provider key is only in Dify's settings, never in a web page or the bubble code

THE KNOWLEDGE BASE
[ ] Created under Knowledge, on the Classic tab if the page shows Classic and Agent (the Chatbot app can't search an Agent knowledge base)
[ ] Default Models has an Embedding Model set, or I picked Economical
[ ] My documents show Available, not Indexing or Error

THE CHATBOT
[ ] Instructions: answer only from my documents, say "I don't know" otherwise, never claim to be a person
[ ] Knowledge: my knowledge base is added (Knowledge, Add, Select reference Knowledge)
[ ] Tested 10 real customer questions in Debug & Preview
[ ] Tested a question that isn't in my documents, and it says it doesn't know
[ ] Features: Citations and Attributions is on, so I can see where answers come from
[ ] Features: Conversation Opener says it's an AI, not a person, and how to reach a person

PUBLISHING AND EMBEDDING
[ ] Published ("Your web app must be published before embedding.")
[ ] Access Point, Web App card: the switch is on
[ ] Embed Into Site, the second option (the bubble), copied whole
[ ] Pasted into my site's custom code area, and the bubble shows in the bottom right corner
[ ] I republish after every change ("If you update your app configuration, republish to see changes in embedded versions.")
[ ] I know web apps are "public by default", and Regenerate on the Web App card replaces a leaked address
[ ] My site and the Dify app both use HTTPS (the docs' iframe troubleshooting)

IF I SELF-HOST INSTEAD
[ ] Docker Compose 2.35.0 or later, Git and OpenSSL; at least 2 CPU cores and 4 GiB of RAM
[ ] Before anyone else can reach it: HTTPS, and the bundled development credentials replaced
[ ] Someone looks after the server, its updates and its backups
[ ] I've checked Dify's LICENSE for my own use: "a modified version of the Apache License 2.0", no multi-tenant use
    without written permission, keep the LOGO and copyright in the console and applications
[ ] I've seen that the pricing page calls the free Community edition "For open-source enthusiasts, individual
    developers, and non-commercial projects." and, for business use, I've asked Dify in writing

AFTER IT GOES LIVE
[ ] Someone opens the app's Logs page every week and adds what the documents were missing
```
