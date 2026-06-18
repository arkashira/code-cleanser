# Roadmap for **code‑cleanser**
*AI‑powered refactoring tool to simplify complex codebases and boost developer productivity*  

---  

## Vision
Provide developers with a seamless, AI‑driven experience that automatically detects, suggests, and applies clean‑code transformations across any supported language, reducing technical debt and accelerating delivery cycles.

---

## MVP (Must‑Have for Launch) – **Release 0.1.0**  

| Milestone | Description | Success Criteria |
|-----------|-------------|------------------|
| **Core AI Engine Integration** | Embed a **vLLM**‑based inference server (verified production engine) to run our fine‑tuned refactoring model. | Latency ≤ 200 ms per 200‑line snippet; > 90 % inference uptime in CI. |
| **Language Support – Python & C++** | Implement parsers & AST walkers for Python (via `ast`) and C++ (via `libclang`). | Detect ≥ 95 % of syntactic constructs; no crashes on large repos (> 10 k files). |
| **Refactoring Suggestions UI** | Minimal VS Code extension panel showing suggestions with “Accept / Reject” actions. | 80 % of displayed suggestions are accepted in user testing. |
| **Safety Guardrails** | - Diff preview before applying changes.<br>- “Undo” stack per file.<br>- Configurable rule whitelist/blacklist. | Zero data‑loss incidents in beta; rollback < 1 s. |
| **CI/CD Pipeline** | Automated tests (unit, integration, performance) + Docker image publishing. | 90 % test coverage; successful build on every push to `main`. |
| **Documentation & Quick‑Start** | README, installation guide, and sample repo walkthrough. | New user can run `code-cleanser` on a sample project within 5 min. |

> **MVP‑Critical**: Core AI Engine, Language Support, Safety Guardrails, and VS Code UI. Without these the product cannot deliver value or be trusted.

---

## Phase 1 – **Version 1.0** (Quarter 2 2026)

| Theme | Features | Target Release |
|-------|----------|----------------|
| **Expanded Language Coverage** | Add JavaScript/TypeScript (via `acorn`), Java (via `javaparser`). | 2026‑07‑15 |
| **Batch Refactoring Mode** | CLI mode to process entire repo with parallel workers; generate PRs automatically. | 2026‑08‑01 |
| **Custom Rule Engine** | Users can author YAML‑based refactor rules (e.g., rename patterns, enforce naming conventions). | 2026‑08‑20 |
| **Metrics Dashboard** | Web UI showing debt reduction stats, refactor count, and performance per repo. | 2026‑09‑05 |
| **Enterprise Auth** | SSO (SAML/OIDC) for corporate environments, role‑based permission to approve changes. | 2026‑09‑30 |
| **Performance Optimizations** | Model quantization & caching; target ≤ 100 ms latency for 500‑line snippets. | 2026‑10‑10 |

---

## Phase 2 – **Version 2.0** (Quarter 3 2026)

| Theme | Features | Target Release |
|-------|----------|----------------|
| **Interactive Chat‑Assist** | In‑IDE chat powered by **SGLang** for on‑the‑fly explanations & “why this refactor?” | 2026‑11‑01 |
| **Multi‑Repo Dependency Awareness** | Detect cross‑module impacts; suggest coordinated changes across repos. | 2026‑11‑20 |
| **Continuous Integration Hook** | GitHub/GitLab Action that runs code‑cleanser on PRs and posts suggestions as review comments. | 2026‑12‑05 |
| **Learning Loop** | Capture accepted/rejected suggestions to fine‑tune the model (active learning). | 2026‑12‑20 |
| **Marketplace for Plugins** | SDK for third‑party rule packs (e.g., security hardening, performance patterns). | 2027‑01‑15 |
| **Compliance Mode** | Pre‑built rule sets for GDPR, PCI‑DSS, and internal coding standards. | 2027‑01‑30 |

---

## Phase 3 – **Version 3.0** (2027 and beyond)

| Theme | Planned Enhancements |
|-------|----------------------|
| **Full‑Stack Language Support** – Go, Rust, Kotlin, Swift |
| **AI‑Generated Tests** – Auto‑create unit tests for refactored code |
| **Explainable AI** – Visual trace of model decisions for auditability |
| **Cloud SaaS Offering** – Managed service with usage‑based billing |
| **Integration with Axentx Knowledge Graph** – Leverage company‑wide code‑base patterns for smarter suggestions |

---

## Success Metrics (Post‑Launch)

| Metric | Target |
|--------|--------|
| **Adoption** | 5 k active developers within 6 months |
| **Acceptance Rate** | ≥ 85 % of suggestions accepted |
| **Technical Debt Reduction** | Avg. 30 % reduction in cyclomatic complexity per repo |
| **Revenue** | $150 k ARR by Q4 2026 (subscription model) |
| **Customer NPS** | ≥ 70 |

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Model Hallucination (unsafe refactor) | High – could break builds | Strict safety guardrails, diff preview, automated test suite before apply |
| Language Parser Incompatibility | Medium | Use well‑maintained open‑source parsers; contribute back fixes |
| Performance at scale | Medium | Quantization, caching, batch inference, horizontal scaling of vLLM |
| Data Privacy (code leakage) | High | Run inference on‑premise Docker image; no telemetry of raw code |

---

*Prepared by the senior product/engineering lead, aligned with Axentx’s validated‑need pipeline.*
