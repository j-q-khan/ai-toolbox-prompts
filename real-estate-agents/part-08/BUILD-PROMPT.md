# Claude build prompt: How to Make Real Estate Videos with AI (Part 8 of 10)

**What you need:** Claude Code on a paid Claude plan (Pro or higher, at the time of checking), a test folder, and made-up test data. Never use real client details. Claude should ask you before it changes anything.

From the AI for Real Estate Agents series. Use test data only, never real client data. Claude should ask before it changes anything.

Goal: a Remotion template that renders a wide and a vertical pan-and-zoom video per listing in a CSV, with Whisper captions.
Inputs: a new test folder with listings.csv (ListingId, ListPrice, BedroomsTotal, BathroomsTotalInteger, LivingArea, PhotoFolder), one folder of photo01.jpg, photo02.jpg and so on per listing in showing order, and a voiceover.mp3 per listing.
Steps, in order:
1. Run npx create-video --yes --blank listing-video, then npx remotion skills add.
2. Build one composition, ListingVideo, with a zod schema for photos, facts and captions: a [3]-second slow push-in per photo, short crossfades, a closing fact card, laid out by width and height so text is never cut off.
3. Run whisper voiceover.mp3 --model turbo --output_format srt, and load it with parseSrt from @remotion/captions.
4. Send each SRT plus my names list to claude-haiku-5-5 for JSON only: wrong and right word pairs. Apply them in Python so timestamps never change, and log them.
5. Write props/ListingId.json per row (files, not inline JSON, for Windows). Render npx remotion render ListingVideo out/ListingId-wide.mp4 --props=props/ListingId.json, then again with --width=1080 --height=1920 to out/ListingId-vertical.mp4.
6. Save this bash fallback, from FFmpeg's documented examples, as fallback.sh: ffmpeg -i photo%02d.jpg -vf "scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='min(zoom+0.0015,1.5)':d=100:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=25" -c:v libx264 -pix_fmt yuv420p wide.mp4
Safety rails: dummy listings and my own test photos, with no client names, phone numbers or finances. No MLS login, no uploads, writes only in the test folder. Check Remotion's license for my company size. Stop and ask me before running anything that changes data.
Output: the project, two videos per listing in out/, captions_fixes.csv and a README.
