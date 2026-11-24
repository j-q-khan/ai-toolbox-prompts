Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new folder holding only plans.csv and usage.csv from this video's files (or your own two files in the same shape). It builds a small Python script that tells you how many credits you have left on each generator today, warns you before one-time credits expire, and flags any clip you mean to sell on a plan whose terms say no or don't say. It reads only the two files you name, writes one new file beside them, calls no video service or website, and changes nothing else. Written for this video, checked 2026-11-23. Nothing here was run for the video.

Goal: write one Python script, credit_tracker.py, that reads my plans file and my usage file and writes a short report next to them.
Input: two files I name on the command line, for example python credit_tracker.py plans.csv usage.csv. Both are comma-separated with a header row. Skip blank lines and lines starting with #. NAME below means the usage file's name without .csv.
plans.csv columns: generator, plan, allowance, renews, started, expires_after_days, watermark, commercial. allowance is a whole number of credits, or empty when the maker doesn't say. renews is daily, once or trial. started is the date (YYYY-MM-DD) you got the credits, or empty. expires_after_days is a whole number or empty. commercial is yes, no or check.
usage.csv columns: date, generator, credits_spent, for_sale, what. date is YYYY-MM-DD, credits_spent is a whole number, for_sale is yes or no.
Steps, in order:
1. Tell me in two sentences what the script will do and which file it will create, then wait for me to say go.
2. Use only Python's standard library. No installs, no internet, no other files read, no calls to any video or AI service or website.
3. Check every row first. If a usage row names a generator that isn't in plans.csv, or a number, date or yes/no value can't be understood, stop and list each bad row with its line number, and write nothing.
4. For each generator in plans.csv, work out credits left, using today's date from the computer: for daily, the allowance minus what usage.csv spent today; for once and trial, the allowance minus everything spent so far. If allowance is empty, write: amount not stated by the maker, so fill in what your account shows.
5. For once and trial plans with expires_after_days, start counting from the started date, or, if started is empty, from the earliest usage date for that generator and say so, and write the date the credits expire; if that date has passed, write EXPIRED, and if it is today or tomorrow, add the word WARNING.
6. List every usage row with for_sale yes whose plan has commercial no or check, under the heading Check before you sell, with the date, generator and what.
7. Write all of it to NAME-credit-report.txt: one block per generator (generator and plan, credits left, renews, expiry if any, watermark), then the Check before you sell list, then one line saying the report uses only what is in the two files and that plans change, so check each maker's page.
8. Never overwrite a file that already exists: if NAME-credit-report.txt is there, stop and tell me.
9. Then run it once on the files I named and show me the report.
Safety: read only the two files I name. Don't change, move or delete them or anything else. Don't call any website or API.
Output: credit_tracker.py, the new report file, and a three-line note saying what you created.
