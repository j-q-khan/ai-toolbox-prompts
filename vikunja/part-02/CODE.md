# Full code: How to Install Vikunja with Docker Compose

From Vikunja's official Full Docker example (no proxy), checked 2026-11-04, with three changes marked in comments. Example values only: replace them before first start. Not run by us.

### docker-compose.yml
```
services:
  vikunja:
    image: vikunja/vikunja:2.7.1                # pinned (docs: vikunja/vikunja)
    environment:
      VIKUNJA_SERVICE_PUBLICURL: http://localhost:3456/
      VIKUNJA_DATABASE_HOST: db
      VIKUNJA_DATABASE_PASSWORD: same-long-password-in-both-places
      VIKUNJA_DATABASE_TYPE: postgres
      VIKUNJA_DATABASE_USER: vikunja
      VIKUNJA_DATABASE_DATABASE: vikunja
      VIKUNJA_SERVICE_SECRET: paste-openssl-output-here
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
      POSTGRES_PASSWORD: same-long-password-in-both-places
      POSTGRES_USER: vikunja
    volumes:
      - ./db:/var/lib/postgresql
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -h localhost -U $$POSTGRES_USER"]
      interval: 30s
      start_period: 15s
      start_interval: 5s
```

### First start (Linux; on macOS skip the chown line)
```
openssl rand -hex 32
mkdir files db
chown 1000 files
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
