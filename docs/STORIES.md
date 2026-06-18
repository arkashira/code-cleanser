# STORIES.md – code‑cleanser

## Overview
**code‑cleanser** is an AI‑powered refactoring tool that automatically simplifies complex codebases, enforces style conventions, and surfaces hidden technical debt.  
The goal of this backlog is to deliver a **Minimum Viable Product (MVP)** that developers can run locally or as a CI step, see concrete improvements, and accept the changes with confidence.

---

## Epics

| Epic | Description | MVP Priority |
|------|-------------|--------------|
| **E1 – Core AI Refactoring Engine** | Build the inference pipeline that parses source files, generates refactoring suggestions, and applies safe transformations. | ✅ |
| **E2 – Language Support** | Provide first‑class support for the most common languages in our dataset (Python, JavaScript, Go). | ✅ |
| **E3 – IDE / CLI Integration** | Expose the engine via a command‑line interface and VS Code extension for interactive use. | ✅ |
| **E4 – Quality Assurance & Safety** | Implement diff preview, rollback, and automated test validation to guarantee no regressions. | ✅ |
| **E5 – CI/CD Automation** | Enable code‑cleanser as a GitHub Action / GitLab CI job that can be gated on pull‑request. | 🌟 |
| **E6 – Configurable Ruleset** | Allow teams to customize which refactorings are enabled (e.g., naming, dead‑code removal, complexity reduction). | 🌟 |
| **E7 – Reporting & Metrics** | Generate a summary report (lines saved, complexity reduced, issues fixed) and export to JSON/HTML. | 🌟 |
| **E8 – Enterprise Governance** | Add role‑based access, audit logs, and policy enforcement for large organizations. | 🚀 |

> **Legend** – ✅ MVP, 🌟 post‑MVP, 🚀 future roadmap.

---

## User Story Backlog

### Epic E1 – Core AI Refactoring Engine

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E1‑01** | **As a developer, I want code‑cleanser to analyze a repository and produce a list of refactoring suggestions, so that I can see where the code can be improved.** | - Run `code-cleanser analyze <path>` → JSON output with file, line range, original snippet, suggested snippet, confidence score.<br>- Confidence ≥ 0.7 for all suggestions in MVP.<br>- Execution time ≤ 2 seconds per 1 k LOC on a typical laptop. |
| **E1‑02** | **As a developer, I want the tool to automatically apply safe refactorings, so that I can quickly clean up my code without manual edits.** | - `code-cleanser apply --dry-run` shows a diff preview.<br>- `code-cleanser apply` writes changes only if all diffs are accepted via `--yes` flag.<br>- No syntax errors introduced (validated by running `python -m py_compile` / `go build` / `node -c`). |
| **E1‑03** | **As a QA engineer, I want the engine to be deterministic given the same input and seed, so that test results are reproducible.** | - Add `--seed <int>` flag; repeated runs with same seed produce identical suggestion sets.<br>- Document default seed value. |
| **E1‑04** | **As a product manager, I want the engine to log processing metrics (tokens consumed, latency), so that we can monitor cost and performance.** | - Logs written to `stdout` and optional `--metrics-file <path>` in JSON format.<br>- Contains `tokens_in`, `tokens_out`, `duration_ms`. |

### Epic E2 – Language Support

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E2‑01** | **As a Python developer, I want code‑cleanser to understand Python 3.8+ syntax, so that it can refactor modern codebases.** | - Parser accepts `.py` files with type hints, f‑strings, async/await.<br>- At least 5 distinct Python refactorings (e.g., `if x is None` → `x is None`, extract method, simplify comprehensions). |
| **E2‑02** | **As a JavaScript developer, I want the tool to handle both CommonJS and ES‑module formats, so that it works across Node projects.** | - Detects `require`/`module.exports` and `import`/`export`.<br>- Provides at least 3 JS refactorings (e.g., convert `var` → `let/const`, arrow function conversion, duplicate import removal). |
| **E2‑03** | **As a Go developer, I want code‑cleanser to respect `gofmt` conventions, so that generated code stays idiomatic.** | - Parses `.go` files, runs `gofmt -d` on output to ensure no formatting differences.<br>- Offers at least 2 Go refactorings (e.g., replace `if err != nil { return err }` with early return helper, simplify `switch` statements). |

### Epic E3 – IDE / CLI Integration

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E3‑01** | **As a developer, I want a CLI that can be invoked from any terminal, so that I can integrate it into my workflow.** | - Installable via `pip install code-cleanser` and `npm i -g code-cleanser` (wrapper script).<br>- `code-cleanser --help` displays all commands and options. |
| **E3‑02** | **As a VS Code user, I want an extension button “Run Code‑Cleanser”, so that I can refactor the current file with one click.** | - Extension contributes command `codeCleanser.runFile`.<br>- Shows a side‑panel with diff preview and “Accept All / Reject All”. |
| **E3‑03** | **As a developer, I want the CLI to accept a list of files or a glob pattern, so that I can target specific parts of a repo.** | - `code-cleanser analyze src/**/*.py` works.<br>- Invalid patterns produce a clear error message. |

### Epic E4 – Quality Assurance & Safety

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E4‑01** | **As a developer, I want to preview a unified diff before applying changes, so that I can review the impact.** | - `--dry-run` prints a standard unified diff to stdout.<br>- Diff includes line numbers and original vs. suggested code. |
| **E4‑02** | **As a CI engineer, I want the tool to abort if any suggestion confidence is below a threshold, so that only high‑quality changes are merged.** | - `--min-confidence <float>` flag; exit code 1 if any suggestion < threshold.<br>- CI job fails with clear message. |
| **E4‑03** | **As a developer, I want an automatic rollback if the post‑apply test suite fails, so that my repo never ends up broken.** | - After `apply`, run `npm test` / `pytest` / `go test` (detectable via `--test-cmd`).<br>- On non‑zero exit, revert all file changes and log the failure. |
| **E4‑04** | **As a security reviewer, I want the tool to run in a sandboxed subprocess, so that malicious model outputs cannot affect the host.** | - All AI inference runs inside a Docker container with read‑only mount of source files.<br>- No network access during inference. |

### Epic E5 – CI/CD Automation (post‑MVP)

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E5‑01** | **As a repo maintainer, I want a GitHub Action that runs code‑cleanser on PRs, so that code quality is enforced automatically.** | - Action `code-cleanser/action` available on Marketplace.<br>- Runs on `pull_request` event, posts a comment with diff summary and pass/fail status. |
| **E5‑02** | **As a DevOps engineer, I want the action to be configurable via `code-cleanser.yml`, so that teams can enable/disable specific rules.** | - Action reads `.code-cleanser.yml` from repo root.<br>- Supports `languages`, `min_confidence`, `enabled_rules`. |

### Epic E6 – Configurable Ruleset (post‑MVP)

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E6‑01** | **As a team lead, I want to enable only “dead‑code removal” and “naming standardization”, so that we can focus on high‑impact refactors.** | - `.code-cleanser.yml` `rules:` list accepts rule identifiers.<br>- Disabled rules produce no suggestions. |
| **E6‑02** | **As a developer, I want to override the confidence threshold per rule, so that I can be stricter on risky changes.** | - YAML supports `rules.<id>.min_confidence`.<br>- Engine respects per‑rule thresholds. |

### Epic E7 – Reporting & Metrics (post‑MVP)

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E7‑01** | **As a manager, I want a summary HTML report after each run, so that I can see productivity gains.** | - `code-cleanser report --output report.html` generates a page with tables: files changed, lines saved, cyclomatic complexity reduction, confidence distribution. |
| **E7‑02** | **As a data analyst, I want the raw metrics exported as JSON, so that I can feed them into dashboards.** | - `--json <path>` writes the same data in machine‑readable format. |

### Epic E8 – Enterprise Governance (future)

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E8‑01** | **As an admin, I want role‑based access to the CI integration, so that only approved users can approve auto‑applied refactors.** | - Integration with OAuth / SSO.<br>- Approvals recorded in audit log. |
| **E8‑02** | **As a compliance officer, I need an immutable audit log of every refactor, so that we can prove change provenance.** | - Log entries include user, timestamp, rule, before/after snippets, confidence, git commit hash. |

---

## MVP Release Plan (Stories to ship in Sprint 1)

1. **E1‑01**, **E1‑02**, **E1‑03**, **E1‑04** – Core engine & deterministic behavior.  
2. **E2‑01**, **E2‑02**, **E2‑03** – Language parsers & baseline refactorings.  
3. **E3‑01**, **E3‑02**, **E3‑03** – CLI + VS Code extension entry point.  
4. **E4‑01**, **E4‑02**, **E4‑03**, **E4‑04** – Safety net (diff preview, confidence gating, test‑backed rollback, sandbox).  

*Post‑MVP* will follow the roadmap through Epics E5‑E8.  

--- 

*Prepared by the product/engineering lead – code‑cleanser*
