# Sources: n8n AI Agent Tutorial: Build an AI Agent with Claude

Part 3 of the AI Automation with n8n series.

- n8n latest release, GitHub API (fetched 2026-11-16): https://api.github.com/repos/n8n-io/n8n/releases/latest
- AI Agent node (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent
- Tools Agent (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent
- Human-in-the-loop for AI tool calls (fetched 2026-11-16): https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools
- What agents do (fetched 2026-11-16): https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do
- Chat Trigger (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger
- Chat node (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat
- Human review node shape, n8n source at n8n@2.47.7 (fetched 2026-11-16): https://github.com/n8n-io/n8n/blob/n8n@2.47.7/packages/cli/src/tool-generation/hitl-tools.ts
- Tool node shape, n8n source at n8n@2.47.7 (fetched 2026-11-16): https://github.com/n8n-io/n8n/blob/n8n@2.47.7/packages/cli/src/tool-generation/ai-tools.ts
- Max Iterations error, n8n source at n8n@2.47.7 (fetched 2026-11-16): https://github.com/n8n-io/n8n/blob/n8n@2.47.7/packages/@n8n/nodes-langchain/nodes/agents/Agent/agents/ToolsAgent/V3/helpers/checkMaxIterations.ts
- Anthropic Chat Model (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic
- Anthropic credentials in n8n (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/credentials/anthropic
- Create and edit credentials (fetched 2026-11-16, as in Part 2): https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials
- Let AI specify tool parameters (fetched 2026-11-16): https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters
- Simple Memory (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow
- Mockingbird sample endpoint (fetched 2026-11-16, plain web requests, no account): https://mockingbird.n8n.io/v1/weather/lisbon
- Get your Claude API key, Anthropic (fetched 2026-11-16): https://platform.claude.com/docs/en/get-api-key
- Authentication, Anthropic (fetched 2026-11-16): https://platform.claude.com/docs/en/manage-claude/authentication
- Spend limits, Anthropic (fetched 2026-11-16): https://platform.claude.com/docs/en/api/rate-limits
- Models overview, Anthropic (fetched 2026-11-16): https://platform.claude.com/docs/en/about-claude/models/overview
- Is my data used for model training?, Anthropic Privacy Center (fetched 2026-11-16, article dated 2026-08-18): https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
- n8n privacy (fetched 2026-11-16): https://docs.n8n.io/privacy-and-security
- Data tables (as in Part 2, fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable
- Editor labels, n8n source at n8n@2.47.7 (fetched 2026-11-16): https://github.com/n8n-io/n8n/blob/n8n@2.47.7/packages/frontend/@n8n/i18n/src/locales/en.json

## Images

- ai-stars.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/build/.gitbook/assets/ai-stars.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
