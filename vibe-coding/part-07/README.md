# Vibe Coding Part 7: Vibe Coding Security: Make Your Lovable App Production Ready

The files for Part 7 of 7 of the Vibe Coding series. Written from Lovable's and Supabase's official docs, checked 2026-11-17, and not run for the video. Use them on an app with made-up data only.

- `BUILD-PROMPT.md`: the copy-paste prompt for your Lovable app's chat (Build picked). It checks every table's Row Level Security, looks for a secret key in the front-end code, runs both scans and lists fixes, changing nothing until you agree.
- `security-check-prompt.txt`: the same prompt as a plain text file.
- `fix-new-row-prompt.txt`: the prompt for the error "new row violates row-level security policy for table".
- `insert-policy-example.sql`: Supabase's own example of a policy for adding rows, for reading only.
- `production-ready-checklist.md`: the checklist from the video.
- `CODE.md`: every file above, as shown in the video's Full code.
- `SOURCES.md`: the pages each fact comes from, with the date checked.

To keep a copy of any file: paste it into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Prompts in this folder are free to use (MIT licence). Not affiliated with Lovable, Supabase, Google, Framer, Anthropic or Claude.
