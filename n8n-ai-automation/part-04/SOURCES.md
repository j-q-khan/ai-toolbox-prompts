# Sources: n8n MCP Server: Connect Claude to Your Workflows

Part 4 of the AI Automation with n8n series.

- n8n latest release, GitHub API (fetched 2026-11-16): https://api.github.com/repos/n8n-io/n8n/releases/latest
- MCP Server Trigger (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger
- MCP Server Trigger source at n8n@2.47.7 (fetched 2026-11-16): https://github.com/n8n-io/n8n/blob/n8n@2.47.7/packages/@n8n/nodes-langchain/nodes/mcp/McpTrigger/McpTrigger.node.ts
- Bearer Auth credential, n8n source at n8n@2.47.7 (fetched 2026-11-16): https://github.com/n8n-io/n8n/blob/n8n@2.47.7/packages/nodes-base/credentials/HttpBearerAuth.credentials.ts
- Call n8n Workflow Tool (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow
- Sub-workflow trigger, n8n source at n8n@2.47.7 (fetched 2026-11-16): https://github.com/n8n-io/n8n/blob/n8n@2.47.7/packages/nodes-base/nodes/ExecuteWorkflow/ExecuteWorkflowTrigger/ExecuteWorkflowTrigger.node.ts
- n8n templates (fetched 2026-11-16, for the JSON shape only): https://n8n.io/workflows/17314
- MCP Client Tool (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp
- n8n licence FAQ (fetched 2026-11-16): https://docs.n8n.io/n8n-community-license/community-license/license-faq
- Get started with custom connectors using remote MCP, Anthropic help (fetched 2026-11-16, page marked "Updated this week"): https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
- Getting started with local MCP servers on Claude Desktop, Anthropic help (fetched 2026-11-16, page marked "Updated over 3 weeks ago"): https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop
- Connect to local MCP servers, MCP docs (fetched 2026-11-16): https://modelcontextprotocol.io/docs/develop/connect-local-servers
- mcp-remote (fetched 2026-11-16): npm: https://registry.npmjs.org/mcp-remote
- Node.js releases (fetched 2026-11-16): https://nodejs.org/dist/index.json
- Mockingbird sample endpoint (as in Part 3, fetched 2026-11-16): https://mockingbird.n8n.io/v1/weather/lisbon

## Images

- oauthmcp.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/changelog/.gitbook/assets/oauthmcp.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
