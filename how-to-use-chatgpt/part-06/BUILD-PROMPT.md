Paste this into Claude Code, Anthropic's coding assistant, opened in a new empty folder where you've saved chatgpt-plans.csv from this video's GitHub folder and filled in its last column. It reads only that file, makes one new page beside it, and asks before every change. Written from OpenAI's pricing and help pages, not run.

Goal: make me a one-page ChatGPT plan comparison from the file chatgpt-plans.csv in this folder.
Rules:
1. Read only chatgpt-plans.csv. Don't open, change or delete any other file, don't install anything, and don't go online.
2. Before you write anything, show me your plan in three lines and wait for my OK.
3. Read the file as CSV with a header row: need, Free, Go, Plus, Pro, lowest_plan, source, checked, i_need_this. Some fields are in double quotes because they contain commas; keep their words exactly as written.
4. Make one new file beside it, chatgpt-plans.html: a single HTML page with no scripts and no links to other sites, that prints on one or two sides of A4 or Letter paper.
5. Show every row as a table row with the columns need, Free, Go, Plus and Pro, in the file's order, and mark the rows where i_need_this is yes (any capitals) with a bold "I need this" label.
6. At the top, say which plan is the lowest one that covers every row marked yes, using lowest_plan and the order Free, Go, Plus, Pro, and list the rows that decided it. If no row is marked yes, say "Free covers everything you marked." Skip rows where lowest_plan is empty when you work this out.
7. Under the table, print the checked date from the file and this line: "From OpenAI's pricing and help pages. Prices and limits change: check chatgpt.com/pricing before you pay."
8. Use large, high-contrast text (14 point or more), no images, no logos.
9. Ask me before every file change, and change nothing else.
10. When it's done, tell me how to open the page in my browser and print it.
Output: chatgpt-plans.html, and a one-line summary of which plan it picked and why.
