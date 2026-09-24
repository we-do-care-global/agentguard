# AgentGuard

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![ORCID](https://img.shields.io/badge/orcid-0000-0002-1825-0097-brightgreen.svg)](https://orcid.org/0000-0002-1825-0097)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)](https://www.python.org/)
[![Tests](https://github.com/we-do-care-global/agentguard/actions/workflows/ci.yml/badge.svg)](https://github.com/we-do-care-global/agentguard/actions/workflows/ci.yml)

**Security & governance control plane for autonomous AI agents**  
Policy engine • Tool‑call proxy • Append‑only audit log • Human‑in‑the‑loop approvals • One‑click kill switch

---

## 🚀 Live prototype  
https://command-center-agentguard-wallet-os-lz1sg2.v2.appdeploy.ai/

## 📦 Production repository  
https://github.com/we-do-care-global/agentguard

## 🌐 Landing page (GitHub Pages)  
https://we-do-care-global.github.io/agentguard/

---

## Quickstart

```bash
# Install
pip install agentguard

# Initialise a new agent
agentguard init --agent research-bot

# Run with a policy file (see policy.yaml.example)
agentguard run --policy policy.yaml
```

### Example `policy.yaml`

```yaml
agent: research-bot
allowed_tools: [web_search, read_file]
denied_tools: [send_email, transfer_funds]
limits:
  max_usd_per_day: 5.00
  max_tokens_per_call: 4000
```

---

## Architecture  

```
[LangChain] [LangGraph] [MCP Client]
          \      |      /
           \     |     /
            ▼    ▼    ▼
        ┌─────────────┐
        │ AgentGuard  │
        │ (proxy)     │
        └─────┬───────┘
              │
   ┌──────────┼──────────┐
   │          │          │
Policy Engine  Risk Scorer  Approval Queue
   │          │          │
   ▼          ▼          ▼
[Tools/APIs] [Wallets] [Databases] …
          │
          ▼
   Append‑only audit log (SQLite)
```

---

## Development

```bash
git clone https://github.com/we-do-care-global/agentguard.git
cd agentguard

# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Lint
ruff check .

# Type check
mypy agentguard
```

---

## Docker compose

```bash
docker compose up -d   # starts API, Postgres, Redis
```

API will be available at `http://localhost:8000`.

---

## License  

Apache 2.0 – see `LICENSE` file.

---

## Contact  

Open an issue or reach out to Emir Perla (@we-do-care-global) for questions, feedback, or collaboration.
