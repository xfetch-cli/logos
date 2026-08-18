# Changelog

## 2026-08-18 — v0.1.0

### Initial Catalog

- New catalog repo: 127 logo entries (Linux distributions, version-specific macOS and Windows logos) under `defaults/{linux,macos,windows}/`.
- `logos.json` index: schema `1.0.0` with `defaults` per category, `categories`, `families` and `logos` entries (id, name, category, family, aliases, file, colors, url, ansi).
- Consumed by **xfetch** `--gen-config`: automatic distro detection (os-release `ID`/`ID_LIKE` resolution), `--logo <id>` override, `XFETCH_LOGOS_URL` override for forks, and full fallback when offline.
- Standard sizing: rectangular art of ~12 rows, UTF-8, LF endings, no control characters.
- Documentation: README, CONTRIBUTING (logo + index entry rules), SECURITY.
- Linux Mint entry got `linuxmint` added to its aliases (the real os-release ID, resolving the only gap among common distro IDs).
