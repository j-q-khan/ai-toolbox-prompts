# Claude build prompt: How to Use AI for Real Estate Agents

**What you need:** Claude Code on a paid Claude plan (Pro or higher, at the time of checking), a test folder, and made-up test data. Never use real client details. Claude should ask you before it changes anything.

Part 1 of AI for Real Estate Agents. Copy everything below the line into Claude.
Use made-up test data only, never real client details.

---

Use this in Claude Code (Pro or higher), in an empty test folder, with made-up listing data only. Goal: in a new test folder, build a local kit that writes MLS public remarks from RESO fields and checks them for fair housing wording, with no cloud calls. Inputs: create listings-sample.csv with made-up data for 3 homes and the columns ListingId, BedroomsTotal, BathroomsTotalInteger, LivingArea, YearBuilt, LotSizeAcres, InteriorFeatures, PublicRemarks, PrivateRemarks. Steps: 1) Check that Ollama is installed with cloud features off (OLLAMA_NO_CLOUD=1); if not, tell me how, without changing settings. 2) Write a Modelfile named factsheet with a SYSTEM line holding these rules: use only the given fields, write "not provided" for empty ones, describe the home not the buyer, stay under the character limit I give, list each claim with its source field. 3) Write a second Modelfile named fairhousing that flags phrases tied to the seven protected classes in 42 U.S.C. 3604(c) and suggests neutral rewrites. 4) Write a small script that reads the CSV, drops PrivateRemarks, sends each row to factsheet, then to fairhousing, and saves drafts.md. Safety: test folder and sample data only, never real client data, read-only first. Stop and ask me before running anything that changes data, installs software or creates a model. Output: both Modelfiles, the script, drafts.md, and every draft line to check against the MLS.
