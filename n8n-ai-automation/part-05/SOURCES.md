# Sources: n8n Claude Code Tutorial: Build Workflows by Asking

Part 5 of the AI Automation with n8n series.

- n8n latest release, GitHub API (fetched 2026-11-16): https://api.github.com/repos/n8n-io/n8n/releases/latest
- Connect to n8n MCP server (fetched 2026-11-16): https://docs.n8n.io/connect/connect-to-n8n-mcp-server
- MCP client connection examples (fetched 2026-11-16): https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples
- MCP server tools reference (fetched 2026-11-16): https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference
- Use n8n MCP server (fetched 2026-11-16): https://docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server
- n8n licence FAQ (fetched 2026-11-16): https://docs.n8n.io/n8n-community-license/community-license/license-faq
- n8n-io/skills README and repo (fetched 2026-11-16): https://github.com/n8n-io/skills
- Connect Claude Code to tools via MCP, Anthropic (fetched 2026-11-16): https://code.claude.com/docs/en/mcp
- n8n's Connect a client dialog and consent page, n8n source at n8n@2.47.7 (fetched 2026-11-16): https://github.com/n8n-io/n8n/blob/n8n@2.47.7/packages/modules/mcp/frontend/src/mcp.clients.catalog.ts
- Claude Code MCP quickstart, Anthropic (fetched 2026-11-16): https://code.claude.com/docs/en/mcp-quickstart
- Claude Code permission modes, Anthropic (fetched 2026-11-16): https://code.claude.com/docs/en/permission-modes
- czlonkowski/n8n-mcp, third-party, README (fetched 2026-11-16, as in the fact sheet §7): https://github.com/czlonkowski/n8n-mcp
- Split Out node, n8n source at n8n@2.47.7 (fetched 2026-11-16, for the reference workflow): https://github.com/n8n-io/n8n/blob/n8n@2.47.7/packages/nodes-base/nodes/Transform/SplitOut/SplitOut.node.ts
- Mockingbird sample endpoint (as in Parts 2 and 3, fetched 2026-11-16): https://mockingbird.n8n.io/v1/weather/paris

## Images

- mcp-enable-screen.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/connect/.gitbook/assets/mcp-enable-screen.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
- mcp-enabled-screen.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/connect/.gitbook/assets/mcp-enabled-screen.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
