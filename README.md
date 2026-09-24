# AgentGuard – Security & Governance Control Plane for Autonomous AI Agents

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![ORCID](https://img.shields.io/badge/orcid-0009-0009-8515-2727-brightgreen.svg)](https://orcid.org/0009-0009-8515-2727)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)](https://www.python.org())
[![Tests](https://github.com/${ORG}/${repo}/actions/workflows/ci.yml/badge.svg)](https://github.com/${ORG}/${repo}/actions/workflows/ci.yml)

## 🚀 Live prototype
https://command-center-agentguard-wallet-os-lz1sg2.v2.appdeploy.ai/

## 📦 Production repository
https://github.com/${ORG}/${repo}

## 🌐 Landing page (GitHub Pages)
https://we-do-care-global.github.io/${repo}/

---

## Quickstart

\`\`\`bash
# Install
pip install ${repo//-/_}

# Initialise a new agent (example)
${repo//-/_} init --agent research-bot

# Run with a policy file (see policy.yaml.example)
${repo//-/_} run --policy policy.yaml
\`\`\`

### Example \`policy.yaml\` (if applicable)

\`\`\`yaml
agent: example-bot
allowed_tools: [web_search, read_file]
denied_tools: [send_email, transfer_funds]
limits:
  max_usd_per_day: 5.00
  max_tokens_per_call: 4000
\`\`\`

---

## Architecture

*(Add architecture diagram as needed)*

---

## Development

\`\`\`bash
git clone https://github.com/${ORG}/${repo}.git
cd ${repo}

# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Lint
ruff check .

# Type check
mypy ${repo//-/_}
\`\`\`

---

## Docker compose

\`\`\`bash
docker compose up -d   # starts API, Postgres, Redis
\`\`\`

API will be available at \`http://localhost:8000\$.

---

## License
Apache 2.0 – see \`LICENSE\` file.

---

## Contact
Open an issue or reach out to Emir Perla (@we-do-care-global) for questions, feedback, or collaboration.
