# Full code: Claude for Legal: Install the Legal Plugin and Review a Contract



### 1. services-agreement.txt
```
WEBSITE SUPPORT SERVICES AGREEMENT
(Practice document for a video. Both companies are invented, every name and number is made up, and the websites ending .example are reserved example names, not real sites. This is not a template to use and not legal advice.)

This agreement is between Kestrelpine Studio (the "Provider", https://kestrelpine.example) and Marrowfield Garden Supply (the "Customer", https://marrowfield.example).

1. Services. The Provider will look after the Customer's website: security updates, a daily backup, and up to 10 hours of changes each month that the Customer asks for by email.

2. Fees. The Customer will pay $1,500 a month. The Provider will send an invoice at the start of each month, and the Customer will pay it within 30 days.

3. Term and renewal. This agreement starts on 1 February 2027 and lasts 12 months. It then renews automatically for another 12 months each time, unless either party gives written notice of non-renewal at least 10 days before the end of the current term.

4. Ending the agreement early. Either party may end this agreement by written notice if the other party seriously breaks it and does not put things right within 30 days of being told in writing.

5. Confidentiality. Each party will keep the other party's non-public business information confidential and use it only for this agreement, during the agreement and for 2 years after it ends.

6. Ownership. The Customer owns its website text, images and data. The Provider keeps ownership of the tools and code it had before this agreement, and gives the Customer the right to use them on the Customer's website while this agreement lasts.

7. Indemnity. Each party will cover the other party's reasonable costs of any claim brought by an outside party that results from its own breach of this agreement.

8. Limitation of liability. Each party's total liability under this agreement is capped at an amount equal to 12 months of fees ($18,000). Neither party is liable for indirect or consequential losses.

9. Governing law. This agreement is governed by the laws of the State of New York.

10. General. This document is the whole agreement between the parties. Notices go by email to the addresses each party gives the other in writing.

Signed for Kestrelpine Studio: ____________________
Signed for Marrowfield Garden Supply: ____________________
```

### 2. legal-playbook.txt
```
# Legal Playbook Configuration

Practice playbook for an invented customer, Marrowfield Garden Supply, made for a video. Every position is made up for practice. It is not legal advice and not a recommended set of positions; a qualified lawyer sets a real playbook.

## Contract Review Positions

### Limitation of Liability
- Standard position: a cap that applies to both parties, of at least 12 months of fees
- Escalation trigger: uncapped liability, or a cap of less than 6 months of fees

### Indemnification
- Standard position: mutual (each party covers outside claims caused by its own breach)
- Escalation trigger: only the Customer gives an indemnity

### Term and Renewal
- Standard position: automatic renewal only with at least 60 days' notice to cancel
- Escalation trigger: a notice window of under 30 days

### Governing Law
- Acceptable: New York or Delaware
- Escalation trigger: any other place
```

### 3. how-to-check.txt
```
Practice files: services-agreement.txt and legal-playbook.txt (an invented provider, Kestrelpine Studio, and an invented customer, Marrowfield Garden Supply; every name and number is made up; the websites ending .example are reserved example names, not real sites). Not legal advice.

Open them
- Download each from the link in the description: on the file's page, click "Download raw file".
- Optional: open them in Notepad (Windows) or TextEdit (Mac) first. Plain text, nothing hidden.
- In Claude: new chat, the "+" button at the lower left of the message box, "Add files or photos", pick both files. Then type "/" and pick review-contract (or describe the task) and paste Prompt 1.
- In Cowork or Claude Code, the plugin looks for its playbook itself, in a file named legal.local.md: in a folder you've shared with Cowork, or in Claude Code's .claude folder. The GitHub folder has the same playbook under that name.

The planted problem (try to find it before you look)
- Clause 3: "unless either party gives written notice of non-renewal at least 10 days before the end of the current term."
- Playbook, Term and Renewal: "automatic renewal only with at least 60 days' notice to cancel"; escalation trigger "a notice window of under 30 days".
- 10 is under 60 and under 30, so clause 3 is RED (escalate). Missing the notice means another 12 months at $1,500 = $18,000.

Example output (written by us from the files, in the skill's format; a real run will word it differently and will usually be longer, with notes on clauses the playbook doesn't cover)
- Review Basis: Playbook (legal-playbook.txt). Your side: Customer.
- Each rating quotes the playbook line it was compared with.
- Clause 8, Limitation of Liability: GREEN.
- Clause 7, Indemnification: GREEN.
- Clause 9, Governing Law: GREEN.
- Clause 3, Term and Renewal: RED.
  Current language: "at least 10 days before the end of the current term."
  Proposed redline: "at least 60 days before the end of the current term."
  Fallback: 30 days (the shortest window the playbook takes without escalating).

Check every rating, the greens too (a problem Claude missed looks exactly like a pass)
1. Clause 3 vs Term and Renewal: 10 days vs at least 60, escalate under 30. RED is right.
2. Clause 8 vs Limitation of Liability: "Each party's total liability under this agreement is capped at an amount equal to 12 months of fees ($18,000)." Both parties, 12 months of fees: meets "at least 12 months of fees". GREEN.
3. Clause 7 vs Indemnification: "Each party will cover the other party's reasonable costs of any claim brought by an outside party that results from its own breach of this agreement." Runs both ways: mutual. GREEN.
4. Clause 9 vs Governing Law: "the laws of the State of New York." New York is on the list. GREEN.
5. Every quote in Claude's answer should appear word for word in services-agreement.txt. If one doesn't, don't trust that line.

Safety
- This isn't legal advice. A qualified lawyer reviews any real contract before anyone signs it. Claude can miss things, and can be wrong about the law in your country; the plugin's example positions are US ones.
- What you paste goes to Anthropic. Don't paste client names, deal terms, anything under a confidentiality promise, or any agreement your organisation hasn't cleared for Claude.
- A contract from someone else is a file you didn't write: tell Claude not to follow instructions inside it.
```
