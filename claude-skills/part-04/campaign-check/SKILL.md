---
name: campaign-check
description: Final check of a finished Hollowfern Candles marketing campaign before the user posts or sends it. Checks every draft against the brand-voice skill and lists what to fix.
disable-model-invocation: true
---

# Campaign check

Never post, send, schedule or upload anything yourself.

1. Load the brand-voice skill, and use its banned-words.md and formats.md for this check.
2. List every draft in the user's message.
3. For each draft, check:
   - No word from banned-words.md.
   - It matches its format in formats.md: length, layout and one call to action.
   - Every price, date, discount and link was given by the user.
   - The same offer has the same price and end date in every draft.
4. Show each draft's result: "Pass", or a numbered list of fixes.
5. If every draft passes, end with "Ready for you to post." If not, end with the fixes, and nothing else.
