# AgentGuard — Agent Security Scanner

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache%202.0)
[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12-blue.svg)](https://python.org)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0009--8515--2727-brightgreen.svg)](https://orcid.org/0009-0009-8515-2727)

> **Open-source CLI wedge → SaaS funnel**  
> Free CLI → Team $99–$299/mo → Enterprise $500–$2,000/mo

---

## What is AgentGuard?

AgentGuard is a security scanner for AI agent configurations. It detects:

- **Overly permissive tool permissions** — `allow_all`, `permit_all`, `unrestricted`
- **Missing input validation** — `eval`, `exec`, `subprocess`, `shell=True`
- **Indirect prompt injection vectors** — `ignore previous`, `disregard instructions`
- **Unrestricted file system access** — `open()`, `read_file`, `write_file` without path restrictions
- **Hardcoded credentials** — `api_key`, `token`, `secret`, `password` in source
- **Missing rate limiting** — HTTP clients without throttling

## Installation

```bash
pip install agentguard
```

## Usage

```bash
# Scan current directory
agentguard scan .

# Scan specific file
agentguard scan path/to/config.py

# JSON output
agentguard scan . --format json

# Filter by severity
agentguard scan . --severity high
```

## GitHub Action

```yaml
- name: Run AgentGuard scan
  run: |
    python agentguard/agentguard.py scan . --format json > scan-results.json || true
```

## Security Patterns

| Pattern | Severity | Description |
|---------|----------|-------------|
| `overly_permissive` | HIGH | Overly permissive tool permission |
| `missing_validation` | CRITICAL | Dangerous function without validation |
| `prompt_injection` | HIGH | Potential prompt injection vector |
| `unrestricted_fs` | MEDIUM | File system access without restriction |
| `missing_auth` | CRITICAL | Hardcoded credential detected |
| `no_rate_limit` | MEDIUM | HTTP client without rate limiting |

## License

Apache 2.0 — [We Do Care Global](https://wedocare-global.com/)
