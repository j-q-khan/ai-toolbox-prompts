# Full code: Meshy AI Free vs Paid: Pricing, Credits and Who Owns Your 3D Models



### credits-planner.py
```
#!/usr/bin/env python3
# Meshy credits-and-licence planner. Offline: no network calls, no API key.
# Numbers as checked on 2026-11-07 (meshy.ai/pricing, docs.meshy.ai/en/webapp/pricing,
# Meshy Terms of Use last updated 2026-09-19). Plans and costs change: check
# meshy.ai/pricing before you rely on a number. Not legal advice.
#
# Run:  python credits-planner.py                   every plan, every model choice
#       python credits-planner.py --plan pro        one plan
#       python credits-planner.py --want 30 --model standard --texture
#                                                   cheapest plan for 30 models a month
import argparse
import sys

CHECKED = "2026-11-07"

# Credits per Image to 3D try (web app). Texture at generation adds 10.
COSTS = {"lite": 10, "standard": 20, "ultra2k": 25}
NAMES = {"lite": "Meshy 6 Lite", "standard": "Meshy 7.1, Standard", "ultra2k": "Meshy 7.1, Ultra 2K"}
TEXTURE = 10

FREE_LICENCE = ("CC BY 4.0. Meshy owns the models; you may use them, even commercially, "
                "if you credit Meshy (Terms 3.2). Credit line: "
                "Model created with Meshy - CC BY 4.0 License, plus a link to "
                "https://creativecommons.org/licenses/by/4.0/ and a note if you changed it")
PAID_LICENCE = ("You own your models, to the extent possible under applicable law, "
                "and can keep them private (Terms 3.2). No credit line needed.")

PLANS = {
    "free":    {"name": "Free",    "usd": 0,   "credits": 100,  "paid": False},
    "pro":     {"name": "Pro",     "usd": 20,  "credits": 1000, "paid": True},
    "premium": {"name": "Premium", "usd": 40,  "credits": 3000, "paid": True},
    "ultra":   {"name": "Ultra",   "usd": 100, "credits": 8000, "paid": True},
    "studio":  {"name": "Studio (team, shared pool, +$10 a month per extra seat)", "usd": 70, "credits": 5500, "paid": True},
}
FREE_DOWNLOADS = 10  # untextured Meshy 6 Lite only


def per_model(model, texture):
    return COSTS[model] + (TEXTURE if texture else 0)


def free_problem(model, texture):
    # Why a free account couldn't download this model, or "" if it could.
    if model != "lite":
        return "Free downloads only Meshy 6 Lite"
    if texture:
        return "Free downloads only untextured models"
    return ""


def plan_report(key):
    p = PLANS[key]
    print(f"\n{p['name']}: ${p['usd']} a month, {p['credits']:,} credits a month")
    for model in COSTS:
        for texture in (False, True):
            cost = per_model(model, texture)
            count = p["credits"] // cost
            label = NAMES[model] + (" + texture" if texture else "")
            note = ""
            if not p["paid"]:
                problem = free_problem(model, texture)
                if problem:
                    note = f"  (no download: {problem})"
                else:
                    count = min(count, FREE_DOWNLOADS)
                    note = f"  (max {FREE_DOWNLOADS} downloads a month)"
            price = f"  about ${p['usd'] / count:.2f} a model" if p["usd"] and count else ""
            print(f"  {label.ljust(32)} {cost:3d} credits = {count:4d} a month{price}{note}")
    print("  Licence: " + (PAID_LICENCE if p["paid"] else FREE_LICENCE))


def cheapest(want, model, texture):
    cost = per_model(model, texture)
    for key in ("free", "pro", "premium", "ultra"):
        p = PLANS[key]
        # Free only fits untextured Meshy 6 Lite, and at most 10 downloads a month.
        if not p["paid"] and (free_problem(model, texture) or want not in range(1, FREE_DOWNLOADS + 1)):
            continue
        if want * cost in range(p["credits"] + 1):
            return key, cost
    return None, cost


def main():
    ap = argparse.ArgumentParser(description="Meshy credits-and-licence planner (offline)")
    ap.add_argument("--plan", choices=PLANS)
    ap.add_argument("--want", type=int, help="models you want to download a month")
    ap.add_argument("--model", choices=COSTS, default="standard")
    ap.add_argument("--texture", action="store_true")
    a = ap.parse_args()
    if a.want is not None:
        if a.want not in range(1, 1000000):
            sys.exit("--want must be a whole number from 1 to 999999")
        key, cost = cheapest(a.want, a.model, a.texture)
        print(f"{a.want} x {NAMES[a.model]}{' + texture' if a.texture else ''} = "
              f"{a.want * cost:,} credits a month")
        if key is None:
            print("More than Ultra's monthly credits: buy permanent credits, or ask about Enterprise.")
        else:
            plan_report(key)
    else:
        for key in ([a.plan] if a.plan else PLANS):
            plan_report(key)
    print(f"\nAs checked on {CHECKED}. Failed generations cost nothing. Monthly credits reset each "
          "month (Free on the 1st, paid plans on your billing date) and don't roll over; bought "
          "credits never expire but don't unlock downloads. Not legal advice.")


if __name__ == "__main__":
    main()
```

### licence-checklist.txt
```
LICENCE CHECKLIST before you sell a print or a model from Meshy
(Meshy Terms of Use, last updated 2026-09-19; help centre and creativecommons.org,
checked 2026-11-07. Not legal advice. Re-check https://www.meshy.ai/terms-of-use
and https://docs.meshy.ai/en/webapp/pricing on the day you sell: they disagree
about who owns free-plan models, and the Terms are what you agree to.)

WHICH PLAN WAS THE MODEL MADE ON?
[ ] Paid plan (Pro, Premium, Ultra, Studio): you own it (Terms 3.2).
    Still true after you cancel, for models made while you paid (help centre).
[ ] Free plan: Meshy owns it and licenses it to you under CC BY 4.0.

IF IT WAS MADE ON THE FREE PLAN
[ ] Credit line in the listing (Meshy's suggested wording):
      Model created with Meshy - CC BY 4.0 License
[ ] Link to the licence: https://creativecommons.org/licenses/by/4.0/
[ ] Say if you changed it (for example: smoothed, resized, split into parts)
[ ] Don't imply Meshy endorses you or your shop
[ ] Selling the FILE? Your buyer gets the same CC BY licence and may share it on.
    You can't add terms that stop them. Not exclusive: consider a paid plan.

EVERY PLAN
[ ] Never published it to the Meshy Community (published models are CC0,
    public domain: anyone may copy and sell them; paid ownership doesn't cover them)
[ ] The photo was yours, or you had the rights (your own dog: fine;
    a character, logo or someone else's art: don't)
[ ] Don't remove any metadata or watermark Meshy put in the file to mark it
    as AI-generated (Terms 2.4)
[ ] Not using the models to train a rival AI (Terms 2.6)
[ ] Kept your own copy: models on inactive accounts can be deleted (Terms 2.5);
    API models are kept 3 days on Pro, Premium and Ultra
[ ] Training opt-out, if you want it: email support@meshy.ai,
    subject "Request to opt out of Meshy data training", with your account's email
```
