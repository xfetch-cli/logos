# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in the **logo catalog** (e.g. malformed art files
that could crash parsers, or a compromised index), please report it responsibly by contacting:

**Email:** `x@xscriptor.com`

### What to Include

When reporting a security issue, please provide:

1. **Description** — A clear explanation of the vulnerability
2. **Type** — What kind of security issue is it? (e.g., malformed file, injection, parser crash, supply-chain)
3. **Steps to Reproduce** — Detailed steps to trigger the vulnerability
4. **Impact** — How severe is the issue? What could an attacker do?
5. **Affected Versions** — Which artifacts or commits are affected?
6. **Proposed Fix** (optional) — If you have a suggestion for how to fix it

### Guidelines

- **Do not** open public GitHub issues for security vulnerabilities
- **Do not** disclose the vulnerability publicly until a fix is released
- **Do** give the maintainers reasonable time to address the issue before public disclosure
- Typically, we aim to respond within **7 days** and release a fix within **30 days** for critical issues

## Scope

The catalog is consumed by **xfetch** through `--gen-config`: the index and art files are
fetched over HTTPS, validated (size cap, no NUL bytes, sane line width) and written as plain
text into the user's config directory. Any content that bypasses those checks or exploits the
download path is in scope.
