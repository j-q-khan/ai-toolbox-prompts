# Full code: Claude for Marketing: Campaign Plans, SEO Audits and Reports



### 1. studio-notes.txt
```
Studio notes: Puddlestone Pottery (an invented business; every name and number is made up)

What we are: a small pottery studio with two teachers. Website: https://puddlestone.example
What we're launching: beginner pottery classes for adults, no experience needed.
When: Saturdays 9, 16, 23 and 30 January 2027, 10:00 to 12:30.
Seats: 6 per class, so 24 in total.
Price: $45 per person, with clay, glazes and firing included. Pieces are ready to collect two weeks later.
Who it's for: adults nearby who want a hands-on, screen-free hobby.
Goal (set by the owner): 24 bookings, every seat filled, by 30 January 2027.
Budget: $600 in total, for search ads, social media ads and printed flyers.
Booking page: https://puddlestone.example/beginner-pottery-classes/book
What we can't claim: we have no awards and no published reviews. Don't invent any, and don't promise results.
```

### 2. class-page.txt
```
Practice page: an invented pottery studio's class page, written out as plain text so you can see each part search engines look at. Every name and number is made up.

Page URL: https://puddlestone.example/beginner-pottery-classes
Title tag: Beginner Pottery Classes on Saturdays | Puddlestone Pottery
Meta description:

H1: Beginner Pottery Classes for Adults
Text: Our beginner pottery classes are for adults who have never touched clay. In two and a half hours on a Saturday morning, you'll learn to centre clay on the wheel, shape a mug or a bowl, and choose a glaze. Our two teachers keep each class to six people, so you get help when the clay won't behave.
Image: wheel.jpg
Alt text: Hands shaping a small bowl on a pottery wheel

H2: What you'll make
Text: Most people make two or three pieces. We glaze and fire them for you, and they're ready to collect two weeks later.
Image: finished-mugs.jpg
Alt text:

H2: Class dates and price
Text: Saturdays 9, 16, 23 and 30 January 2027, 10:00 to 12:30. $45 per person, with clay, glazes and firing included.

H1: Book your Saturday place
Text: Wear clothes you don't mind getting muddy, and bring nothing else.
Link: See class dates and book (goes to https://puddlestone.example/beginner-pottery-classes/book)
```

### 3. ad-results.csv
```
Channel,Spend,Impressions,Clicks,Bookings
Search ads,240,4000,120,8
Social media ads,300,20000,200,5
Flyers,60,,,3
```

### 4. how-to-check.txt
```
Practice files: studio-notes.txt, class-page.txt and ad-results.csv (an invented pottery studio, Puddlestone Pottery; every name and number is made up; the website puddlestone.example is a reserved example name, not a real site)

Open them
- Download each from the link in the description: on the file's page, click "Download raw file".
- Optional: open them in Notepad (Windows) or TextEdit (Mac) first. Plain text, no formulas, nothing hidden.
- In Claude: new chat, the "+" button at the lower left of the message box, "Add files or photos", pick the file.

1. The campaign brief (Prompt 1, studio-notes.txt)
- Goal: 24 bookings (6 seats x 4 classes) by 30 January 2027.
- Classes: Saturdays 9, 16, 23 and 30 January 2027, 10:00 to 12:30. Price $45 per person.
- Budget: $600 in total. The example brief splits it: search ads $240 + social media ads $300 + printed flyers $60 = $600.
- Calendar in the example: week of 14 December, class page ready and flyers printed; then, to the last class on 30 January, search and social ads run.
- Check: every price, date, seat count and budget figure in Claude's brief matches the notes, the channel budgets add up to $600, and there are no reviews, awards or promised results (the notes say there are none).

2. The page check for SEO (Prompt 2, class-page.txt)
- The seo-audit skill's on-page rules: title tag 50-60 characters with the keyword; meta description 150-160 characters; exactly one H1; alt text on every image.
- Title tag: "Beginner Pottery Classes on Saturdays | Puddlestone Pottery" is 59 characters and has the keyword "beginner pottery classes": passes.
- Meta description: the line is empty: an issue.
- Alt text: wheel.jpg has some; finished-mugs.jpg has none: an issue.
- The planted mistake (try to find it before you look): two H1 lines, "Beginner Pottery Classes for Adults" and "Book your Saturday place". The rule is exactly one. Fix: make the second an H2 (a smaller heading).
- Also passes: the keyword is in the first sentence of the page text; the page URL is short and has the keyword; the link text says where it goes.
- Search volumes and rankings: not in the file, so Claude should write "needs data", not a number.
- Check: in Notepad press Control+F, in TextEdit Command+F, search for "H1:" and you'll find 2. Then look at the "Meta description:" line (empty) and the "Alt text:" line under finished-mugs.jpg (empty).

3. The performance report (Prompt 3, ad-results.csv)
- Click-through rate = clicks / impressions. Conversion rate = bookings / clicks. Cost per booking = spend / bookings.
- Search ads: 120 / 4000 = 0.03 = 3%. 8 / 120 = 0.0667, about 6.7%. $240 / 8 = $30.
- Social media ads: 200 / 20000 = 0.01 = 1%. 5 / 200 = 0.025 = 2.5%. $300 / 5 = $60.
- Flyers: impressions and clicks not tracked (blank in the file, and Claude shouldn't fill them in). $60 / 3 = $20.
- Total: 8 + 5 + 3 = 16 bookings of the 24 goal (two thirds). $240 + $300 + $60 = $600. $600 / 16 = $37.50 a booking.
- Check: redo one channel with a calculator (search ads above), then the total bookings and the overall cost per booking. Any reason Claude gives, like "move some social budget to search", is a guess to test, not a promise.

Safety
- What you paste goes to Anthropic. Keep customer lists, contact details and anything personal out, and follow your employer's rules.
- Not legal advice. A person approves anything before it's published. Nothing here guarantees bookings or a higher place in search results.
```
