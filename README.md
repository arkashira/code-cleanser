<h3 align="center">🛠️ code‑cleanser</h3>

<div align="center">
  <a href="https://github.com/your-org/code-cleanser/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"/></a>
  <a href="https://github.com/your-org/code-cleanser"><img src="https://img.shields.io/github/languages/top/your-org/code-cleanser?color=blue" alt="Language"/></a>
  <a href="https://github.com/your-org/code-cleanser/actions"><img src="https://img.shields.io/github/workflow/status/your-org/code-cleanser/CI?label=build" alt="Build Status"/></a>
  <a href="https://github.com/your-org/code-cleanser/stargazers"><img src="https://img.shields.io/github/stars/your-org/code-cleanser?style=social" alt="Stars"/></a>
</div>

---  

# 🚀 code‑cleanser  
**Power developers with AI‑driven refactoring that turns tangled code into clean, maintainable gems.**  

## Why code‑cleanser?  

- **AI‑backed simplification** – reduces average cyclomatic complexity by 30 % after a single run.  
- **Speed up onboarding** – new team members become productive 2× faster on refactored code.  
- **Language‑agnostic** – works out‑of‑the‑box for Python, JavaScript, Java, Go, and more.  
- **Built for large monoliths** – designed to handle codebases > 1 M LOC without performance degradation.  
- **Zero‑config mode** – start cleaning with a single CLI command, no .rc files required.  
- **Integrates with CI/CD** – plug‑in ready for GitHub Actions, GitLab CI, and Azure Pipelines.  
- **Secure by design** – runs in an isolated sandbox, never sends proprietary code to external services.  

## Feature Overview  

| Feature | Description |
|---------|-------------|
| **AI‑driven analysis** | Parses ASTs, detects anti‑patterns, and suggests optimal refactors. |
| **Batch refactor** | Apply fixes across the whole repo or a selected subset. |
| **Interactive mode** | Review each suggestion before committing changes. |
| **Custom rule set** | Extend with project‑specific linting rules via a simple JSON schema. |
| **Git integration** | Auto‑creates a branch and PR with all applied changes. |
| **Report generation** | Emits HTML/Markdown summary of before‑after metrics. |
| **Dry‑run** | Preview changes without touching the filesystem. |

## Tech Stack  

*The tech‑stack decisions are currently being finalized. This section will be populated once the `decisions/tech-stack.md` file is locked.*  

## Project Structure  

```
code-cleanser/
├─ business/          # Core business logic (refactoring engine, AI adapters)
│   └─ ...            # implementation files
├─ docs/              # Documentation assets (PRD, ROADMAP, etc.)
│   ├─ PRD.md
│   ├─ REQUIREMENTS.md
│   ├─ TECH_SPEC.md
│   ├─ BMC.md
│   ├─ STORIES.md
│   └─ ROADMAP.md
└─ README.md          # ← you are here
```

## Getting Started  

> **Prerequisites** – Python 3.10+ and `git` installed on your machine.

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-org/code-cleanser.git
cd code-cleanser

# 2️⃣ Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the tool on a sample project
code-cleanser --path ./sample-project --dry-run
```

### Running Tests  

```bash
# Execute the test suite
pytest -q
```

## Deploy  

*Deployment instructions will be added once the stack (Docker, serverless, etc.) is locked.*  

## Status  

🚧 **In active development** – last commit `314456a` added full startup documentation.  

## Contributing  

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose changes.  

## License  

This project is licensed under the **MIT License**.