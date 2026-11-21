Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new folder holding only test-limits.csv and test-usage.csv from this video's files (or your own two files in the same layout). It builds a small Python script (you'll need Python 3 on your computer, and Claude Code can help you check) that adds up which plan you used for what, and warns you when you're near a limit you typed in. It reads only the two files you name, writes one new file beside them, and changes nothing else. Written for this video, checked 2026-11-21. Nothing here was run for the video.

Goal: write one Python script, limit_tracker.py, that reads a limits file and a usage log, adds up the usage for each limit's period, and writes a short report that warns me when I'm near or over a limit I typed in.
Input: two CSV files I name on the command line, for example python limit_tracker.py test-limits.csv test-usage.csv. Skip blank lines and lines starting with #. The limits file has the columns tool, what, limit, period, note, where period is day, week or month. The usage log has the columns date, tool, what, count, used_for, with dates written as YYYY-MM-DD. NAME below means the usage file's name without .csv.
Steps, in order:
1. Tell me in two sentences what the script will do and which file it will create, then wait for me to say go.
2. Use only Python's standard library. No installs, no internet, no other files read.
3. For each line in the limits file, add up the count of every usage line with the same tool and what, inside the current period: today for day, the last 7 days including today for week, and the current calendar month for month.
4. Mark each limit OK when the total is under 80 percent of the limit, NEAR when it's 80 percent of the limit or more but still under it, and OVER when the total equals or passes the limit.
5. Write NAME-report.md, a Markdown table with the columns Tool, What, Used, Limit, Period, Status, Note, in the limits file's order, then a short list of what I used each tool for this month, taken from used_for. Start it with a line saying "Made from NAME.csv on" and today's date, and end it with "Limits change: check each company's own page."
6. Print the NEAR and OVER lines on the screen as well.
7. If a usage line names a tool and what that aren't in the limits file, list it under "Not tracked" in the report instead of failing.
8. In each file, the first line that isn't blank or a # line is the header: read the columns from it. If any later line has a count or limit that isn't a whole number, or a date that isn't YYYY-MM-DD, stop and tell me the line number, and write nothing.
9. Never overwrite a file that already exists: if NAME-report.md is there, stop and tell me.
10. Then run it once on the two files I named and show me the report.
Safety: read only the two files I name. Don't change, move or delete them or anything else. Don't upload anything or call any website or API.
Output: limit_tracker.py, the new report, and a three-line note saying what you created.
