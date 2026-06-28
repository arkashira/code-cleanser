```markdown
## Tech Spec: code-cleanser (v1)

### Stack
- **Runtime**: Node.js (LTS) with TypeScript
- **AI Core**: Python (3.11) with `llama-index` + `vllm` (OSS inference)
- **Dev Tooling**:
  - `eslint-plugin-react`, `prettier`, `ts-morph` (AST utilities)
  - `@anthropic-ai/sdk`, `@mistralai/client` (multi-model fallback)
- **IaC**: Terraform (AWS/GCP) + Docker (multi-stage)

### Hosting (Free-tier-First)
- **Compute**:
  - Primary: AWS Lambda (Node.js) + EC2 `t4g.small` (Python worker)
  - Free-tier: Supports ~1M invocations/month (Lambda) + ~750 hrs EC2/month
- **Storage**:
  - Ephemeral: `/tmp` + S3 (pre/post-refactor diffs)
  - Primary DB: Neon (serverless Postgres → free 500 MB)
- **CDN**: Cloudflare Workers KV (cache LLM outputs)

---

### Data Model (Postgres)
| Table | Fields | Purpose |
|-------|--------|---------|
| `projects` | `id`, `repo_url`, `github_install_id`, `branch_hash`, `token_hash` (salted) | Track repo state |
| `sessions` | `id`, `project_id`, `user_id`, `status` (`queued`/`running`/`failed`/`completed`), `started_at`, `finished_at` | Session metadata |
| `refactorings` | `id`, `session_id`, `file_path`, `original_code` (JSONB), `simplified_code`, `ai_model`, `diff_url`, `cost_tokens`, `fidelity_score` (1-5) | Refactor artifacts |
| `costs` | `id`, `session_id`, `total_tokens`, `input_tokens`, `output_tokens`, `cached_tokens`, `llm_cost_usd`, `compute_cost_usd` | Usage tracking |
| `user_feedback` | `id`, `refactoring_id`, `rating` (1-5), `comment`, `applied` (bool) | Validation loop |

---

### API Surface
| Method | Path | Purpose | Auth |
|--------|------|---------|------|
| `POST` | `/api/v1/sessions` | Create refactor session | GitHub OAuth |
| `GET` | `/api/v1/sessions/:id` | Get session status | JWT |
| `POST` | `/api/v1/sessions/:id/cancel` | Cancel active session | JWT |
| `GET` | `/api/v1/projects/:id/refactorings` | List refactorings for project | JWT |
| `GET` | `/api/v1/refactorings/:id` | Get refactor diff | JWT |
| `POST` | `/api/v1/refactorings/:id/feedback` | Submit user feedback | JWT |
| `GET` | `/api/v1/costs/:id` | Retrieve cost breakdown | JWT |
| `POST` | `/api/v1/github/hook` | GitHub webhook (install/uninstall) | GitHub Secret |
| `GET` | `/api/v1/health` | Liveness probe | None |

---
### Security Model
- **Auth**:
  - GitHub OAuth → JWT (RS256, 24h expiry)
  - GitHub App install: `permissions: {contents: read, checks: write}`
- **Secrets**:
  - Stored in Hashicorp Vault → AWS Secrets Manager (encrypted at rest)
  - API tokens (LLM providers, GitHub) rotated every 90 days
- **IAM**:
  - Lambda execution role: `lambda_vpc`, `s3_read_write`, `neon_db`, `vault_kv`
  - EC2 worker role: `ec2_ssm`, `redis_cloud` (if used)
- **Secrets in Transit**:
  - TLS 1.3 (AWS ALB + Cloudflare)
  - mTLS for EC2-Lambda communication

---
### Observability
| Signal | Tool | Retention |
|--------|------|-----------|
| **Metrics** | Prometheus (Node Exporter) → Grafana Cloud | 30d |
| **Logs** | CloudWatch (stdout/stderr) → OpenSearch | 7d |
| **Traces** | OpenTelemetry (OTLP→Jaeger) | 14d |
| **Errors** | Sentry (rack-backed) | 30d |
| **Alerts** | Prometheus Alertmanager → Slack/Email | 24/7 |
- **Key Metrics**:
  - `refactor_duration_seconds` (P50, P90)
  - `llm_input_tokens_total`
  - `success_rate` (sessions w/ `completed` status)

---
### Build/CI
- **Local**:
  - `pnpm install && pnpm run dev` (hot-reload)
  - Pre-commit: `lint-staged`, `knip`
- **Pipeline**:
  1. **Lint**: `eslint`, `mypy`, `actionlint`
  2. **Test**: Jest (unit), `vitest` (Vite), `tsc --noEmit`
  3. **Build**: Docker multi-stage → `node:20-alpine` + `python:3.11-slim`
  4. **Security**:
     - Snyk (SAST/SCA)
     - `sbom` generation (Syft)
  5. **Deploy**:
     - `terraform apply` (changes PR → main)
     - Canary: 10% traffic to new Lambda version
```