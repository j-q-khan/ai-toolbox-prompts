# Full code: Replace Shopify Apps with Claude Code

The code is built from Shopify's official docs and Anthropic's Claude Code docs, and needs a free Shopify development store to try.

### Setup commands
```
npm install -g @shopify/cli@latest
curl -fsSL https://claude.ai/install.sh | bash
claude plugin install shopify-ai-toolkit@claude-plugins-official
shopify store create dev --name "App swap test" --demo-data
```

### Back up the theme and pull a copy
```
shopify theme duplicate --store your-dev-store --theme "Your theme name" --name 'Backup before Claude'
mkdir my-theme
cd my-theme
shopify theme pull --store your-dev-store --live
git init
git add .
git commit -m "Theme before Claude"
```

### CLAUDE.md
```
# Theme rules
- This folder is a copy of a theme from a development store with demo data.
- Make one small change at a time, and explain it before you make it.
- Prefer a new section or snippet over editing existing files.
- Run shopify theme check after every change and fix any errors.
- Never run shopify theme push, publish or delete. I upload and publish myself.
- Before removing a leftover app snippet, list every file that uses it.
```

### .claude/settings.json
```
{
  "permissions": {
    "deny": [
      "Bash(shopify theme push *)",
      "Bash(shopify theme publish *)",
      "Bash(shopify theme delete *)",
      "Bash(*allow-live*)"
    ]
  }
}
```

### Check and preview
```
shopify theme check
shopify theme dev --store your-dev-store
```

### Upload as a hidden copy (you run this, not Claude)
```
shopify theme push --store your-dev-store --unpublished --theme "Claude test" --strict
```
