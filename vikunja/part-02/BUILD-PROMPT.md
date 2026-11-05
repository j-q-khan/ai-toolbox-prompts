# Claude build prompt: How to Install Vikunja with Docker Compose

A compose file checker for Claude Code. Read-only: it never starts Docker; it checks one file and writes one report. Rules checked against the vikunja.io docs on 2026-11-04 (Vikunja v2.7.1). Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a read-only checker for a Vikunja docker-compose.yml that lists every unsafe or broken setting before the file is ever started.
Inputs: one file, docker-compose.yml, in this folder. If I don't have one, first write a deliberately broken test copy based on the "Example without any proxy" from vikunja.io/docs/full-docker-example, with changeme passwords, an empty secret and a tab on one line, and use that.
Steps, in order:
1. Tell me which files you'll open and what you'll write, and wait for my yes. Never run docker, docker compose or any container.
2. Parse the file as YAML with a library only if one is already installed (for example Python's yaml module); otherwise ask me before installing one, or fall back to careful line-by-line checks and say so in the report. Before parsing, report any line that contains a tab character, with its line number, because YAML forbids tabs for indentation.
3. Check the vikunja service: the image has a fixed version tag (for example vikunja/vikunja:2.7.1), not latest or no tag; VIKUNJA_SERVICE_SECRET (or VIKUNJA_SERVICE_SECRET_FILE) is set, not empty and not the docs placeholder, and at least 32 characters; VIKUNJA_SERVICE_PUBLICURL is set, starts with http:// or https://, and includes the port when it isn't 80 or 443; VIKUNJA_SERVICE_ENABLEREGISTRATION is "false" once the first user exists (ask me whether it does); remind me that docker compose restart does not apply environment changes, so after any change I must run docker compose up -d; the ports line: if it is bound to 127.0.0.1, ask me whether I browse from other devices (then PUBLICURL must use the server's network address, not localhost); if it is not bound, remind me to limit the port with a firewall and to put HTTPS in front before any internet access; ./files is mounted at /app/vikunja/files.
4. Check the db service: POSTGRES_PASSWORD is not changeme and matches VIKUNJA_DATABASE_PASSWORD (compare them without printing either value); the db service publishes no ports; the data volume is mounted at /var/lib/postgresql for the postgres:18 image; a healthcheck exists and the vikunja service waits for it with condition service_healthy.
5. Flag any password or secret written in plain text, and suggest the _FILE form instead, for example VIKUNJA_DATABASE_PASSWORD_FILE pointing at a Docker secret.
6. Write compose-check.md: a table with each check, pass or fail, the line number and the fix, quoting the vikunja.io page each rule comes from. Never print secret values; show only their length.
7. Ask me before changing anything. Only if I say yes, write a fixed copy as docker-compose.fixed.yml, and never overwrite the original.
Safety: this folder and test data only. No docker commands, no network calls, no installs. Never send the file anywhere. Stop and ask me before running anything that changes data.
Output: compose-check.md and a three-line summary.
