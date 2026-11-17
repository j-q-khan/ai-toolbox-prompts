# Sources: n8n Workflow Tutorial: Build Your First Automation

Part 2 of the AI Automation with n8n series.

- n8n latest release, GitHub API (fetched 2026-11-16): https://api.github.com/repos/n8n-io/n8n/releases/latest
- Build your first workflow (fetched 2026-11-16): https://docs.n8n.io/get-started/build-your-first-workflow
- Mockingbird sample endpoint (fetched 2026-11-16, a plain web request, no account): https://mockingbird.n8n.io/v1/weather/berlin
- How n8n structures data (fetched 2026-11-16): https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure
- Key concept glossary (fetched 2026-11-16): https://docs.n8n.io/get-started/key-concept-glossary
- Save and publish workflows (fetched 2026-11-16): https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows
- Types of executions (fetched 2026-11-16): https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions
- Create and edit credentials (fetched 2026-11-16): https://docs.n8n.io/build/understand-workflows/create-and-edit-credentials
- Encryption key (fact sheet §4, 2026-11-16): https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key
- Export and import (fetched 2026-11-16): https://docs.n8n.io/build/manage-workflows/export-and-import
- Schedule Trigger common issues (fetched 2026-11-16): https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues
- Schedule timezone settings (n8n-docs include timezone-settings.md, fetched 2026-11-16): "The default is America/New York for self-hosted instances."; timezone variable page: "GENERIC_TIMEZONE … America/New_York … Important for schedule nodes": https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/timezone-and-localization
- Data tables (fetched 2026-11-16): https://docs.n8n.io/build/work-with-data/data-tables
- Node sources at n8n@2.47.7 (fetched 2026-11-16), for the workflow file's shape: Schedule Trigger versions 1–1.4 and the `rule.interval[].triggerAtHour` parameter (: https://github.com/n8n-io/n8n/blob/n8n@2.47.7/packages/nodes-base/nodes/Schedule/ScheduleTrigger.node.ts
- Docs example workflow files, for the export layout (fetched 2026-11-16): https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/_workflows/try-it-out/quickstart/tutorial.json

## Images

- build-your-first-workflow.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/get-started/.gitbook/assets/build-your-first-workflow.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
- build-your-first-workflow-optional-01-01.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/get-started/.gitbook/assets/build-your-first-workflow-optional-01-01.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
- build-your-first-workflow-optional-02-01.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/get-started/.gitbook/assets/build-your-first-workflow-optional-02-01.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
- build-your-first-workflow-optional-03-01.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/get-started/.gitbook/assets/build-your-first-workflow-optional-03-01.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
- build-your-first-workflow-optional-06-01.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/get-started/.gitbook/assets/build-your-first-workflow-optional-06-01.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
- build-your-first-workflow-optional-06-03.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/get-started/.gitbook/assets/build-your-first-workflow-optional-06-03.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
- build-your-first-workflow-optional-02-02.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/get-started/.gitbook/assets/build-your-first-workflow-optional-02-02.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
- build-your-first-workflow-optional-03-03.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/get-started/.gitbook/assets/build-your-first-workflow-optional-03-03.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
- build-your-first-workflow-optional-04-03.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/get-started/.gitbook/assets/build-your-first-workflow-optional-04-03.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
- build-your-first-workflow-optional-05-05.png: https://raw.githubusercontent.com/n8n-io/n8n-docs/main/docs/get-started/.gitbook/assets/build-your-first-workflow-optional-05-05.png (Apache-2.0 with Commons Clause, n8n-io/n8n-docs by n8n GmbH)
