Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new folder holding only test-weekly-tasks.txt from this video's files (or a plain-text list of your own tasks, one per line). It builds a small Python script that turns a list of weekly tasks into a job and tool table. It reads only the file you name, writes one new file beside it, and changes nothing else. Written for this video, checked 2026-11-21. Nothing here was run for the video.

Goal: write one Python script, pick_tools.py, that reads a plain-text list of tasks and writes a table matching each task to a job and the tools named in this video.
Input: a task file I name on the command line, for example python pick_tools.py test-weekly-tasks.txt. One task per line. Skip blank lines and lines starting with #. NAME below means the input file's name without .txt.
Steps, in order:
1. Tell me in two sentences what the script will do and which file it will create, then wait for me to say go.
2. Use only Python's standard library. No installs, no internet, no other files read.
3. Put these five jobs and their tools at the top of the script, in a dictionary I can edit: Writing and questions: one chat app (ChatGPT, Claude, Gemini or Microsoft Copilot). Facts you can check: Perplexity, or Gemini Deep Research. Your own files: Gemini Notebook (was NotebookLM), or Notion Agent if your notes are in Notion. Pictures: ChatGPT Images, or Gemini Images. Design: Canva.
4. Give each job a short list of keywords, also editable at the top: Writing and questions: write, draft, email, reply, letter, plan, explain, summarise. Facts you can check: check, fact, research, compare, find out, source. Your own files: notes, manual, document, pdf, my files, lease, minutes. Pictures: picture, image, photo, illustration. Design: flyer, poster, design, social post, banner, menu card.
5. Match each task to the first job whose keyword appears in it, ignoring capitals. If no keyword matches, use the job "Not sure: try one chat app first". If more than one job matches, list the first in the table and the others in a column called Also.
6. Write NAME-tools.md, a Markdown table with the columns Task, Job, Tools, Also, one line per task in the file's order, with a first line saying "Made from NAME.txt on" and today's date, and a last line saying "Check each tool's own page before you rely on it."
7. Never overwrite a file that already exists: if NAME-tools.md is there, stop and tell me.
8. If the file has no tasks, write nothing and print a short message saying so.
9. Then run it once on the task file I named and show me the table.
Safety: read only the file I name. Don't change, move or delete it or anything else. Don't upload anything or call any website or API.
Output: pick_tools.py, the new table, and a three-line note saying what you created.
