# The AI engineer roadmap: five skills, in order (facts checked 2026-11-22)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as ai-engineer-roadmap-checklist.md. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every link below is the provider's own page, opened on 2026-11-22. Nothing was signed up for, installed or run. Pages change: check each one before you rely on it. The order is this video's suggestion, not any one provider's list.

## What the job is
- roadmap.sh: "An AI Engineer uses pre-trained models and existing AI tools to improve user experiences." https://roadmap.sh/ai-engineer
- AI Hero: ML engineers focus on "Model training and optimization"; AI engineers on "Building applications with those models". https://www.aihero.dev/what-is-an-ai-engineer

## 1. Python
- [ ] Start here: Python For Beginners, https://www.python.org/about/gettingstarted/
- [ ] Already code in another language? The official tutorial: https://docs.python.org/3/tutorial/index.html
- [ ] Prove it: a script that opens a text file and counts how often a word appears, written without copying.

## 2. Calling a model's API
- [ ] Anthropic's quickstart (key in ANTHROPIC_API_KEY): https://platform.claude.com/docs/en/get-started
- [ ] OpenAI's quickstart (key in OPENAI_API_KEY): https://developers.openai.com/api/docs/quickstart
- [ ] Prove it: one script, one question, one answer, with the key in an environment variable, never in the code.
- [ ] Go further: Prompt Engineering, https://www.youtube.com/playlist?list=PLNO38g3ifrEI
- [ ] Models on your own computer: Run Open Models, https://www.youtube.com/playlist?list=PLHkUmek0E8ZI

## 3. Retrieval (RAG)
- [ ] Anthropic's glossary, RAG: https://platform.claude.com/docs/en/about-claude/glossary
- [ ] OpenAI's embeddings guide: https://developers.openai.com/api/docs/guides/embeddings
- [ ] Anthropic's embeddings page (it uses another provider's models): https://platform.claude.com/docs/en/build-with-claude/embeddings
- [ ] Prove it: answer questions about three made-up documents by finding the nearest paragraph and putting it in the prompt.

## 4. Evaluation (evals)
- [ ] Anthropic, Define success criteria and build evaluations: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- [ ] Prove it: ten test questions, each with a fact the answer must contain, and a script that prints a score.

## 5. Agents and tool calls
- [ ] Anthropic, Building effective AI agents: https://www.anthropic.com/engineering/building-effective-agents
- [ ] Anthropic, Tool use with Claude: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- [ ] Prove it: one tool you write yourself (a made-up order lookup) that the model calls, and you see the call and the result.
- [ ] Go further: Build AI Agents, https://www.youtube.com/playlist?list=PLOUgOGy8Z9Do
- [ ] Tools for models: MCP Servers, https://www.youtube.com/playlist?list=PLcnK26WPsihE

## Before you add a framework
- [ ] Can you make one call to the API by hand?
- [ ] Do you have a test that gives a score?
- [ ] Anthropic: "We suggest that developers start by using LLM APIs directly"
