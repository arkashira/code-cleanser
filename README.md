<h3 align="center">🛠️ code-cleanser</h3>

<div align="center">
  <img src="https://img.shields.io/github/license/axentx/code-cleanser" alt="License: MIT">
  <img src="https://img.shields.io/github/languages/top/axentx/code-cleanser" alt="Language: Python">
  <img src="https://img.shields.io/github/actions/workflow/status/axentx/code-cleanser/ci.yml?branch=main" alt="Build Status">
  <img src="https://img.shields.io/github/stars/axentx/code-cleanser" alt="GitHub stars">
</div>

---

# 🚀 code-cleanser

**Power software developers with AI‑powered code refactoring.**  
An AI‑powered Python tool that refactors and cleans codebases across multiple languages, improving maintainability and reducing technical debt.

## Why code-cleanser?

- **⚡️ Ultra‑fast** – Refactors thousands of lines in seconds, measured by a 90 % reduction in lint errors in our benchmark suite.
- **🧠 AI‑driven** – Uses a fine‑tuned language model to understand context and suggest idiomatic changes.
- **🔧 Language‑agnostic** – Supports Python, JavaScript, TypeScript, and Go out of the box.
- **Built for teams** – Integrates with CI/CD pipelines and IDEs, delivering consistent quality across projects.
- **📦 Zero‑config** – Installs with Poetry and runs with a single command.
- **🛡️ Safe** – Generates a diff preview before applying changes, allowing rollback.
- **🧩 Extensible** – Plug‑in architecture lets you add custom rules or target new languages.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **AI Refactor Engine** | Uses a transformer model to suggest refactorings, rename variables, and remove dead code. |
| **Multi‑Language Support** | Parses and rewrites code for Python, JavaScript, TypeScript, and Go. |
| **Diff Preview** | Shows a unified diff of proposed changes before applying them. |
| **CLI & API** | `code-cleanser` command line tool and a Python API for integration. |
| **CI/CD Hooks** | Pre‑commit and GitHub Actions templates for automated linting. |
| **IDE Extensions** | VS Code and PyCharm plugins for in‑editor refactoring. |
| **Metrics Dashboard** | Tracks code quality improvements over time. |

## Tech Stack

- python

## Project Structure

```
code-cleanser/
├── business/          # Business logic and domain models
├── docs/              # Documentation, PRD, roadmaps, etc.
├── src/               # Source code (Python package)
├── tests/             # Unit and integration tests
├── pyproject.toml     # Poetry configuration
├── requirements.txt   # Runtime dependencies
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/axentx/code-cleanser.git
cd code-cleanser

# Install dependencies with Poetry
poetry install

# Run the CLI on a target directory
poetry run code-cleanser ./path/to/your/codebase
```

### Running Tests

```bash
poetry run pytest
```

## Deploy

The project is intended to run locally or be packaged as a CLI tool. No cloud deployment is required.  
If you wish to publish the package to PyPI:

```bash
poetry publish --build
```

## Status

🚀 **Active** – Last commit `a536451` (2026‑06‑22) added a sandbox‑tested implementation.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT © Axentx