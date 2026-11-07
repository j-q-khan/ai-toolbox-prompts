# Full code: OpenBao Tutorial: Install with Docker Compose

Our compose file, built from OpenBao's documented image, entrypoint and config stanzas (checked 2026-11-07 against v2.7.2). OpenBao publishes no official compose file. For a local test on one computer, with test data only. Not run by us.

### Folder layout
```
bao/
  docker-compose.yml
  config/
    openbao.hcl
```
Keep nothing else in config: the server loads every file in that folder as server config. Never put unseal keys or the root token in this folder, and never commit them to Git.

### docker-compose.yml
```
services:
  openbao:
    image: openbao/openbao:2.7.2        # pinned
    command: server                     # no command = dev mode
    ports:
      - 127.0.0.1:8200:8200             # this computer only
    environment:
      BAO_ADDR: http://127.0.0.1:8200   # TLS is off for this local test
    volumes:
      - ./config:/openbao/config:ro     # a "Could not chown /openbao/config" log line is harmless
      - bao-data:/openbao/file          # folder the image already owns
    mem_swappiness: 0                   # install page: --memory-swappiness=0
    healthcheck:
      test: ["CMD-SHELL", "bao status || exit 1"]   # bao: 0 unsealed, 2 sealed; Docker wants 0 or 1
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s
    restart: unless-stopped
volumes:
  bao-data:
```
If Docker refuses mem_swappiness on your computer, delete that line and follow the install page's swap advice instead.

### config/openbao.hcl
```
ui           = true
api_addr     = "http://127.0.0.1:8200"
cluster_addr = "http://127.0.0.1:8201"

storage "raft" {
  path    = "/openbao/file"
  node_id = "bao-1"
}

listener "tcp" {
  address     = "0.0.0.0:8200"
  tls_disable = 1   # local test only: with no certificate and TLS on, OpenBao would try Let's Encrypt
}

audit "file" "to-stdout" {
  description = "Write audit information to standard output."
  options {
    file_path = "stdout"
  }
}
```

### Start, initialize and unseal
```
cd bao
docker compose up -d
docker compose exec openbao bao status
docker compose exec openbao bao operator init
docker compose exec openbao bao operator unseal
docker compose exec openbao bao operator unseal
docker compose exec openbao bao operator unseal
docker compose exec openbao bao status
```
Run these lines one at a time. The first status shows Initialized false and Sealed true. Run init only once: copy the five unseal keys and the root token into a password manager straight away, never into this folder or Git. Run unseal three times and paste a different key at each hidden prompt. The last status shows Sealed false. Then open http://localhost:8200/ui in your browser.

### Sign in with the root token (for setup only)
```
docker compose exec openbao bao login -no-print
```
Paste the root token at the hidden prompt. -no-print keeps it off the screen: no output means it worked, and an error means the token was wrong.

### admin-policy.hcl (in the bao folder, not in ./config)
```
# As powerful as root, but auditable and revocable. Narrow it to the paths you manage.
path "*" {
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}
```

### Admin login, then revoke the root token
```
cat admin-policy.hcl | docker compose exec -T openbao bao policy write admin -
docker compose exec openbao bao auth enable userpass
printf 'New admin password: '; stty -echo; read -r PW; stty echo; echo
printf '%s' "$PW" | docker compose exec -T openbao bao write auth/userpass/users/admin policies=admin password=-
unset PW
docker compose exec openbao bao login -no-store -field=token_policies -method=userpass username=admin && docker compose exec openbao bao token revoke -self
docker compose exec openbao bao login -no-print -method=userpass username=admin
```
Run these lines one at a time, in a bash terminal (on Windows, Git Bash): each prompt would take the next pasted line as its answer. The third line reads the password without showing it, and printf passes it on with no newline at the end (password=- keeps every character it's given, newline too). The -no-store login only tests the admin password and keeps you signed in as root; -field=token_policies makes it print only the policy names, so the admin token is never shown (a note that the token wasn't stored also appears; that's expected), and -no-store can't be combined with -no-print. The && runs the revoke only if that test login succeeded, and the revoke cancels the root token, because root is still the stored login. The last line signs you in as admin from now on, without printing the new token.

### Back up Raft (run as the admin login)
```
docker compose exec openbao bao operator raft snapshot save /tmp/bao.snap
docker compose cp openbao:/tmp/bao.snap ./bao-backup.snap
docker compose exec openbao rm /tmp/bao.snap
```
Keep the snapshot and the unseal keys in different places. To restore on this server: docker compose cp ./bao-backup.snap openbao:/tmp/bao.snap, then docker compose exec openbao bao operator raft snapshot restore /tmp/bao.snap.

### Check health
```
docker compose ps
docker compose exec openbao bao status
```
bao status exits 0 when unsealed and 2 when sealed. The health check turns any non-zero code into 1, the code Docker reads as unhealthy, so a sealed server shows unhealthy after every restart until you unseal it.

### Before other machines connect: TLS
```
listener "tcp" {
  address       = "0.0.0.0:8200"
  tls_cert_file = "/openbao/tls/bao.crt"
  tls_key_file  = "/openbao/tls/bao.key"
}
```
Put your certificate and key in ./tls and add - ./tls:/openbao/tls:ro under volumes. The key file must be readable by the container's openbao user. Then change the listener as shown above, set BAO_ADDR and api_addr to https://bao.test.example:8200, and only then publish the port beyond 127.0.0.1. Never put it on the internet without TLS. The health check then also needs BAO_CACERT and a name that resolves inside the container, or it reports unhealthy.

### Pre-flight checklist (before the first docker compose up -d)
```
[ ] Image pinned: openbao/openbao:2.7.2, not latest
[ ] command: server is there (no command = dev mode, for learning only)
[ ] Port bound to 127.0.0.1 while TLS is off
[ ] Data on the named volume bao-data at /openbao/file
[ ] storage "raft", not "file" (removed in 2.7)
[ ] Only openbao.hcl in ./config
[ ] Test data only until TLS is on
[ ] After init: five keys and the root token in a password manager, not here, not in Git
[ ] Admin login made and tested before the root token is revoked
[ ] Backup: snapshot saved, copied out, kept apart from the unseal keys
```
