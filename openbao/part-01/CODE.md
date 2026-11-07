# Full code: OpenBao vs HashiCorp Vault: What's the Difference?

Ours, built from OpenBao's v2.7.2 docs and HashiCorp's Vault CLI pages (checked 2026-11-06). For a test or staging Vault you can sign in to. Changes nothing on the server. Not run by us.

### inventory.sh (exports what the free build prompt checks)
```
#!/usr/bin/env bash
# Look-up commands only; changes nothing. Run with a test or staging Vault token.
set -euo pipefail
: "${VAULT_ADDR:?Set VAULT_ADDR to your test Vault first}"
vault version | tee version.txt
rc=0
vault status | tee status.txt || rc=$?
case "$rc" in
  0) ;;
  2) echo "Vault is sealed: unseal it, then run this again."; exit 1 ;;
  *) echo "vault status failed: check VAULT_ADDR and your token."; exit 1 ;;
esac
vault secrets list -format=json | tee secrets-list.json
vault auth list -format=json | tee auth-list.json
echo "Now copy your server config file here as vault-config.hcl."
echo "Replace every token, key and password in all five files with XXXX before sharing them."
```

### token-check.sh (finds scripts that expect Vault's token format or VAULT_ settings)
```
#!/usr/bin/env bash
# Run in the folder that holds your scripts. Prints file and line only, never the token.
set -euo pipefail
skip=(--exclude=token-check.sh --exclude=token-hits.txt --exclude=vault-vars.txt --exclude-dir=.git)
grep -rnE "${skip[@]}" 'hvs\.|hvb\.|hvr\.' . | cut -d: -f1,2 | tee token-hits.txt || true
grep -rnoE "${skip[@]}" 'VAULT_[A-Z_]+' . | sort -u | tee vault-vars.txt || true
```
grep exits 1 when nothing matches, so `|| true` keeps the script going. New OpenBao tokens start with s., b. or r. A VAULT_ variable still works in OpenBao when its BAO_ twin isn't set.

### compare-sheet.md (OpenBao v2.7.2 and Vault, checked 2026-11-06)
```
| Topic | Vault | OpenBao |
|---|---|---|
| Licence | BSL 1.1 from 1.15.0 (licensor IBM); internal use allowed | MPL-2.0 |
| Command | vault | bao (the image also has a vault shortcut) |
| Settings | VAULT_ADDR, VAULT_TOKEN | BAO_ADDR, BAO_TOKEN; VAULT_ still read when no BAO_ is set |
| New tokens | hvs., hvb., hvr. | s., b., r. |
| File storage | supported | removed in 2.7.0; use raft, postgresql or pebbledb |
| disable_mlock | a Vault config setting | remove it: no mlock since 2.0.0 |
| AWS, Azure, GCP secrets engines | built in | plugins (openbao-plugins) |
| Cloud KMS auto-unseal | built in | plugins since 2.7.0 |
| PKCS#11 HSM auto-unseal | Enterprise | free plugin |
| Namespaces | Enterprise | built in, its own design |
| Control groups | Enterprise | built in since 2.7.0, its own design |
| Replication between clusters | Enterprise | open feature request |
| Sentinel, Secrets Sync | Enterprise | no page in the docs |
| Paid edition and support | Vault Enterprise, HashiCorp support, HCP Vault Dedicated | none from the project; outside vendors offer services |
| Migration | | tested from Vault Community 1.14.1 only |
```

### policy-example.hcl (the example policy on screen: look-ups only, one app's secrets)
```
path "secret/data/webapp/*" {
  capabilities = ["read"]
}
```
An example in OpenBao's documented policy format, for a KV version 2 store mounted at secret/. Anything not listed is refused.

### kv-get-example.txt (the same look-up in each tool)
```
vault kv get secret/webapp/db
bao kv get secret/webapp/db
```
