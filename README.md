<h3 align="center">🛠️ Code Cleanser</h3>

<div align="center">
  <a href="https://github.com/axentx/code-cleanser/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
  <a href="https://github.com/axentx/code-cleanser">
    <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Language: Python">
  </a>
  <a href="https://github.com/axentx/code-cleanser/actions">
    <img src="https://img.shields.io/github/workflow/status/axentx/code-cleanser/Build/main" alt="Build Status">
  </a>
  <a href="https://github.com/axentx/code-cleanser/stargazers">
    <img src="https://img.shields.io/github/stars/axentx/code-cleanser" alt="Stars">
  </a>
</div>

---
# 🚀 Code Cleanser
**Power developers with AI-driven refactoring to simplify complex codebases and improve productivity.** Code Cleanser is an AI-powered tool that automatically cleans and refactors tangled codebases across multiple programming languages.

## Why Code Cleanser?
* **Improved Code Quality**: Reduces cyclomatic complexity and improves maintainability of codebases.
* **Multi-Language Support**: Supports multiple programming languages, including Python, JavaScript, Go, and Java.
* **Local Execution**: Runs locally in an isolated environment, ensuring security and flexibility.
* **Interactive Review**: Provides interactive review features for precise control over refactoring.
* **Batch Mode**: Offers batch mode for automating refactoring tasks.
* **Custom Rule Engine**: Allows for custom rule engines to adapt to specific project needs.
* **Sandboxed Execution**: Ensures safe execution of refactoring tasks in a sandboxed environment.

## Feature Overview
| Feature | Description |
| --- | --- |
| AST-based Analysis | Analyzes codebases using Abstract Syntax Trees (ASTs) for precise refactoring. |
| AI-driven Refactoring | Utilizes AI algorithms to drive the refactoring process, ensuring optimal results. |
| Interactive Review | Provides an interactive review process for precise control over refactoring. |
| Batch Mode | Offers batch mode for automating refactoring tasks. |
| Custom Rule Engine | Allows for custom rule engines to adapt to specific project needs. |
| Sandboxed Execution | Ensures safe execution of refactoring tasks in a sandboxed environment. |

## Tech Stack
* Python
* JavaScript
* Go
* Java
* Poetry

## Project Structure
* business: Business logic and models
* docs: Documentation and startup artifacts
* src: Source code for the Code Cleanser tool
* tests: Unit tests and integration tests for the tool

## Getting Started
```bash
# Install dependencies
poetry install

# Run the tool
poetry run code-cleanser --help

# Run tests
poetry run pytest tests/
```

## Deploy
```bash
# Build the tool
poetry build

# Deploy to production
# TODO: Add deployment script
```

## Status
Last commit: 6b80c53 - feat(code-cleanser): real, sandbox-tested implementation

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to Code Cleanser.

## License
Code Cleanser is licensed under the MIT License. See [LICENSE](LICENSE) for details.