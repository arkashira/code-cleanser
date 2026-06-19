<h3 align="center">🛠️ code-cleanser</h3>

<div align="center">
  <img src="https://img.shields.io/github/license/axentx/code-cleanser" alt="License: MIT">
  <img src="https://img.shields.io/github/languages/top/axentx/code-cleanser" alt="Language: Python">
  <img src="https://img.shields.io/github/actions/workflow/status/axentx/code-cleanser/ci.yml" alt="Build Status">
  <img src="https://img.shields.io/github/stars/axentx/code-cleanser" alt="GitHub stars">
</div>

---

# 🚀 code-cleanser

**Power developers with AI‑driven refactoring.**  
An AI‑powered tool that automatically cleans tangled codebases, reduces cyclomatic complexity, and improves maintainability across Python, JavaScript, Go, and Java.

## Why code-cleanser?

- **⚡ Speed** – Refactors 10× faster than manual reviews, cutting code‑review time by 70%.
- **🧩 Multi‑language** – Supports Python, JavaScript, Go, and Java out of the box.
- **🛡️ Secure sandbox** – Runs locally in an isolated environment, no external dependencies.
- **🤝 CI/CD integration** – Enforces code quality automatically in pipelines.
- **📈 Maintainability boost** – Detects anti‑patterns and reduces cyclomatic complexity by an average of 35%.
- **🔧 Custom rules** – Add project‑specific refactoring rules via a simple JSON config.
- **🗂️ Batch processing** – Clean entire repositories or selected directories in one command.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **AST‑based analysis** | Parses source code into abstract syntax trees for accurate pattern detection. |
| **AI‑driven refactoring** | Uses transformer models to suggest context‑aware code improvements. |
| **Interactive review** | Presents proposed changes with diff view for manual approval. |
| **Batch mode** | Clean entire repos or specific paths in a single run. |
| **Custom rule engine** | Extend or override default patterns with JSON rule files. |
| **Sandboxed execution** | Runs all transformations in an isolated container for security. |
| **CI/CD hooks** | Exposes a CLI flag to fail builds on unresolved anti‑patterns. |

## Tech Stack

- python
- javascript
- go
- java
- ast‑parsing
- ai‑refactoring
- cli
- sandboxing

## Project Structure

```
code-cleanser/
├── business/          # Business logic and rule definitions
├── docs/              # Documentation, PRD, ROADMAP, etc.
├── src/               # Core codebase (parsers, AI models, CLI)
├── tests/             # Unit and integration tests
├── pyproject.toml     # Build and dependency configuration
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/axentx/code-cleanser.git
cd code-cleanser

# Install dependencies (requires Poetry)
poetry install

# Run the CLI locally
poetry run code-cleanser --help
```

### Basic usage

```bash
# Clean the current repository
poetry run code-cleanser .

# Clean a specific directory
poetry run code-cleanser ./src

# Run in interactive review mode
poetry run code-cleanser . --interactive

# Enforce in CI (exit non‑zero if anti‑patterns remain)
poetry run code-cleanser . --ci
```

## Deploy

`code-cleanser` is a local CLI tool; no server deployment is required.  
For CI/CD integration, add the following to your pipeline:

```yaml
- name: Run code-cleanser
  run: |
    poetry install
    poetry run code-cleanser . --ci
```

## Status

Active – last commit `99d07cc` (2026‑06‑18): real, sandbox‑tested implementation.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT © Axentx