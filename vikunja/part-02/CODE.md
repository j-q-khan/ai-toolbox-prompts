# Full code: How to Install Vikunja with Docker Compose

From Vikunja's official Full Docker example (no proxy, and the Caddy v2 example for HTTPS), checked 2026-11-04, 2026-11-05 and 2026-11-06, with our changes marked in comments. Example values only: replace them before first start. Not run by us.

### docker-compose.yml
```
services:
  vikunja:
    image: vikunja/vikunja:2.8.0                # pinned (docs: vikunja/vikunja)
    environment:
      VIKUNJA_SERVICE_PUBLICURL: http://localhost:3456/
      VIKUNJA_DATABASE_HOST: db
      VIKUNJA_DATABASE_PASSWORD: CHANGE-ME-same-long-password-in-both-places
      VIKUNJA_DATABASE_TYPE: postgres
      VIKUNJA_DATABASE_USER: vikunja
      VIKUNJA_DATABASE_DATABASE: vikunja
      VIKUNJA_SERVICE_SECRET: CHANGE-ME-paste-openssl-output-here
      # VIKUNJA_SERVICE_ENABLEREGISTRATION: "false"   # remove the # after you register
    ports:
      - 127.0.0.1:3456:3456                     # this computer only (docs: 3456:3456)
      # Browsing from another device on your network? Use 3456:3456, put that
      # machine's network address in PUBLICURL, and limit port 3456 with your firewall.
    volumes:
      - ./files:/app/vikunja/files
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
  db:
    image: postgres:18
    environment:
      POSTGRES_PASSWORD: CHANGE-ME-same-long-password-in-both-places
      POSTGRES_USER: vikunja
    volumes:
      - ./db:/var/lib/postgresql
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -h localhost -U $$POSTGRES_USER"]
      interval: 30s
      start_period: 15s
      # the docs also set start_interval: 5s, which older Docker Compose
      # versions reject; add it back only on Docker Compose 2.20.2 or later
```

### First start (in a terminal, in the folder with docker-compose.yml. Linux; on macOS and Windows skip the sudo chown line, because Docker Desktop handles the folder permissions. On Windows, openssl isn't built in, so run these lines in Git Bash)
```
openssl rand -hex 32
mkdir files db
sudo chown 1000 files
docker compose up -d
docker compose logs vikunja
```

### Turn sign-ups off after you register (in docker-compose.yml, remove the # so the line reads)
```
      VIKUNJA_SERVICE_ENABLEREGISTRATION: "false"
```

### Then recreate the container (docker compose restart does not apply environment changes)
```
docker compose up -d
```

### Backup with Vikunja's dump command
```
docker compose exec vikunja /app/vikunja/vikunja dump -p /tmp -f vikunja-backup
docker compose cp vikunja:/tmp/vikunja-backup.zip ./vikunja-backup.zip
```

### Going online later: Caddyfile (from the docs' Caddy v2 example; use your own domain)
```
tasks.example.com {
    reverse_proxy vikunja:3456
}
```

### Going online later: add this service to docker-compose.yml (from the docs' Caddy v2 example, plus Caddy's data folders)
```
  caddy:
    image: caddy:2
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - vikunja
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - ./caddy/data:/data          # keeps the HTTPS certificates (Caddy's image docs)
      - ./caddy/config:/config
```

### Going online later: then change these
```
1. VIKUNJA_SERVICE_PUBLICURL: https://tasks.example.com/
2. Delete the vikunja service's ports lines (Caddy reaches it inside Docker)
3. Point your domain's DNS at the server
4. docker compose up -d
```

### Pre-flight checklist (before the first docker compose up -d)
```
[ ] Image pinned: vikunja/vikunja:2.8.0, not latest
[ ] No CHANGE-ME left anywhere in the file
[ ] Database password changed, and the same in both places
[ ] VIKUNJA_SERVICE_SECRET set from openssl rand -hex 32
[ ] VIKUNJA_SERVICE_PUBLICURL has the port (http://localhost:3456/)
[ ] No tab characters in the file (YAML needs spaces)
[ ] Linux: files folder owned by user 1000
[ ] After registering: ENABLEREGISTRATION "false", then docker compose up -d
[ ] Database port never published; HTTPS in front before any internet access
[ ] Backup tested: dump, copy the zip off the machine, and try the restore
    command (vikunja.io/docs/cli) on a spare machine, never your only copy
[ ] Going online: Caddy's data folder is kept, so certificates survive updates
```
