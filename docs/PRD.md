# PRD – Code‑Cleanser
**Product:** `code-cleanser`  
**Team:** Refactoring AI Squad  
**Owner:** Senior Product Lead  
**Date:** 2026‑06‑18  
**Version:** 1.0  

---  

## 1. Problem Statement  

Modern codebases grow organically, accumulating technical debt, duplicated patterns, and inconsistent style. Developers spend ≈ 30 % of their time on manual refactoring, bug‑prone code cleanup, and “finding the right place” to apply a pattern. Existing linters and formatters only enforce style; they cannot restructure logic, extract reusable components, or reduce cognitive load for large, heterogeneous projects.  

**Resulting pain points**

| Pain Point | Impact |
|------------|--------|
| **Time‑consuming manual refactor** | Slows feature delivery, increases cycle time |
| **Hidden technical debt** | Higher defect rate, harder onboarding |
| **Inconsistent architecture** | Reduces maintainability, hampers scaling |
| **Low confidence in large‑scale changes** | Teams avoid necessary clean‑ups, debt compounds |

## 2. Target Users  

| Persona | Primary Need |
|---------|--------------|
| **Full‑stack Engineer** (mid‑senior) | Quickly simplify legacy modules to add features |
| **DevOps / Platform Engineer** | Ensure code quality across many micro‑services without manual review |
| **Tech Lead / Architecture Owner** | Enforce architectural patterns and reduce debt at scale |
| **Junior Engineer** | Learn best‑practice structures while refactoring safely |

## 3. Goals & Success Metrics  

| Goal | Metric | Target (12 mo) |
|------|--------|----------------|
| **Increase developer productivity** | Avg. time spent on manual refactor per sprint | ↓ 30 % |
| **Reduce technical debt** | Number of “code‑smell” tickets after using Code‑Cleanser | ↓ 40 % |
| **Adoption** | Active installations (GitHub Marketplace, internal CI) | 1 000+ orgs |
| **Revenue** | Paid‑tier subscriptions (team seats) | $250 k ARR |
| **Safety** | Refactor‑induced regression rate (post‑merge) | ≤ 0.5 % |

## 4. Key Features (Prioritized)  

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|----------------------|
| **P1** | **AI‑driven refactor suggestions** | Large‑language‑model (LLM) analyses a repository and proposes concrete refactorings (extract method, rename, split class, replace anti‑patterns). | • Given a repo, tool returns ≥ 5 actionable suggestions per 1 k LOC.<br>• Suggestions are syntactically correct and pass `git diff --check`. |
| **P1** | **One‑click apply with preview** | Developers can preview diffs, accept/reject per suggestion, and apply automatically. | • UI shows diff with inline comments.<br>• Applying changes results in a clean commit that compiles/tests successfully. |
| **P2** | **Custom rule library** | Teams can upload JSON/YAML rule sets (e.g., “all services must use repository pattern”). | • Rule engine validates against repo and surfaces violations.<br>• Custom rules are versioned and shareable across orgs. |
| **P2** | **CI/CD integration** | GitHub Action / GitLab CI job that runs Code‑Cleanser in PR mode, posting suggestions as review comments. | • Action runs on PR open, posts ≤ 10 comments per 5 k LOC.<br>• Fails pipeline only on “critical” regressions (configurable). |
| **P3** | **Safety sandbox & rollback** | Refactor runs inside a containerized sandbox; automatically creates a revert commit if tests fail. | • After apply, `npm test` / `cargo test` (detected) runs; on failure, revert commit is auto‑generated. |
| **P3** | **Metrics dashboard** | Org‑level dashboard showing refactor volume, debt reduction, and productivity impact. | • Dashboard updates nightly, shows trend lines for the metrics defined in §3. |
| **P4** | **Language support matrix** | Initial support: Python, JavaScript/TypeScript, Go, Rust, C++. Expand to Java, C# in v2. | • Unit tests cover parsing & transformation for each supported language. |
| **P4** | **IDE plugins** | VS Code & JetBrains plugins to invoke suggestions inline. | • Plugin shows suggestions in the editor gutter; applying updates file in‑place. |

## 5. Scope  

### In‑Scope (MVP – 6 months)

- Core AI suggestion engine using the **vLLM** inference framework (verified repo).  
- Support for Python, TypeScript, and Go (high‑impact languages in our dataset).  
- GitHub Action integration (PR comment workflow).  
- One‑click apply with preview UI (web UI + CLI).  
- Safety sandbox with automatic rollback on test failures.  
- Basic metrics collection (suggestions per repo, acceptance rate).  

### Out‑of‑Scope (Post‑MVP)

- Full IDE plugin suite (deferred to v2).  
- Enterprise SSO / RBAC integration (planned for paid tier).  
- Multi‑repo dependency graph analysis (future roadmap).  
- Real‑time collaborative refactoring sessions.  

## 6. Assumptions & Dependencies  

| Assumption | Rationale |
|------------|-----------|
| **LLM inference cost** can be kept ≤ $0.001 per suggestion using `vLLM` on our GPU fleet. | Based on current usage patterns from the `auto` dataset (13 M pairs). |
| **Developers have CI pipelines** that can run containerized actions. | Standard practice in target market. |
| **Code‑cleanser will be open‑source core** with a paid SaaS layer for CI integration and dashboards. | Aligns with Axentx’s “freemium → revenue‑validated” model. |
| **Dataset coverage** (auto, instr‑resp, messages) provides sufficient examples of refactoring patterns for prompt engineering. | Existing 13 M + 6 M pairs include many refactor dialogues. |

## 7. Risks & Mitigations  

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Incorrect refactor suggestions** leading to regressions. | High (developer trust). | Safety sandbox + automated test run + revert commit. |
| **LLM hallucination** (suggesting non‑existent APIs). | Medium | Prompt engineering + post‑processing validation against language AST. |
| **Performance bottleneck** on large repos (> 1 M LOC). | Medium | Chunked analysis, parallel workers, caching of ASTs. |
| **Licensing / data compliance** for training data. | Low | All datasets are Apache‑2.0 / MIT / permissive; audit pipeline. |
| **Adoption resistance** (developers fear AI takeover). | Medium | Emphasize “assist, not replace”; provide transparent diff preview. |

## 8. Milestones & Timeline  

| Milestone | Deliverable | Owner | Target Date |
|-----------|-------------|-------|-------------|
| **Kickoff & Architecture** | Detailed design doc, LLM prompt library | Lead Architect | 2026‑07‑01 |
| **Prototype Engine** | vLLM‑backed suggestion API (Python only) | ML Engineer | 2026‑08‑15 |
| **CLI & Web Preview UI** | `code-cleanser` CLI, diff UI | Front‑end Lead | 2026‑09‑30 |
| **GitHub Action Integration** | Action publishing, PR comment workflow | DevOps Engineer | 2026‑10‑31 |
| **Safety Sandbox** | Containerized runner + auto‑rollback | QA Lead | 2026‑11‑15 |
| **Beta Release (internal)** | Closed‑beta with 5 partner teams | PM | 2026‑12‑01 |
| **Public MVP Launch** | Open‑source core + SaaS CI tier | PM | 2027‑02‑01 |
| **Metrics Dashboard** | Org‑level analytics UI | Data Engineer | 2027‑03‑15 |
| **Post‑MVP Roadmap Review** | Prioritization for IDE plugins, extra languages | PM | 2027‑04‑01 |

## 9. Success Evaluation  

- **Quantitative**: Meet all metrics in §3 within 12 months post‑launch.  
- **Qualitative**: ≥ 80 % of beta participants report “significant time saved” in post‑survey.  
- **Financial**: Reach $250 k ARR from paid CI integrations by Q4 2027.  

---  

*Prepared by the Code‑Cleanser Product Team – Axentx*
