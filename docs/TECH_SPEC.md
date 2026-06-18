# TECH_SPEC.md

## Project: code‑cleanser
**Product Category:** AI‑assisted Refactoring Tool  
**Goal:** Automatically simplify, modernize, and improve the readability of complex codebases while preserving functional behavior, thereby boosting developer productivity and reducing technical debt.

---

## 1. Architecture Overview

```
+-------------------+        +-------------------+        +-------------------+
|   CLI / UI Front  | <----> |   Orchestrator    | <----> |   Worker Pool     |
+-------------------+        +-------------------+        +-------------------+
          |                           |                         |
          |   REST/gRPC API           |   Task Queue (Redis)   |   vLLM Inference
          v                           v                         v
+-------------------+        +-------------------+        +-------------------+
|   Auth Service    |        |   Model Service   |        |   Post‑Processor  |
+-------------------+        +-------------------+        +-------------------+
```

* **CLI / UI Front** – Entry point for users (CLI, VS Code extension, or web UI). Packages request payloads and streams results.  
* **Orchestrator** – Stateless FastAPI service that validates requests, authorizes users, stores job metadata in PostgreSQL, and enqueues tasks to Redis.  
* **Worker Pool** – Horizontal set of Python workers (Celery) that pull jobs, invoke the **Model Service**, and run post‑processing.  
* **Model Service** – Thin wrapper around **vLLM** (verified inference engine) serving a fine‑tuned Code‑LLM (based on StarCoder‑15B). Handles prompt construction, token streaming, and token‑level safety filters.  
* **Post‑Processor** – Applies language‑specific AST transformations, diff generation, and quality scoring. Emits a unified diff and optional formatted code.  
* **Auth Service** – JWT‑based authentication/authorization micro‑service (shared across Axentx products).  
* **Data Stores** –  
  * **PostgreSQL** – Job metadata, user settings, audit logs.  
  * **Redis** – Task queue (Celery broker) + result cache (TTL 24 h).  

All components are containerized (Docker) and orchestrated via Kubernetes (Helm chart provided).

---

## 2. Core Components & Responsibilities

| Component | Language | Key Libraries | Responsibilities |
|-----------|----------|---------------|------------------|
| CLI / UI Front | TypeScript (VS Code) / Python (CLI) | `commander`, `axios`, `vscode-extension-api` | Collect source files, send to Orchestrator, display diffs, apply patches |
| Orchestrator | Python 3.11 | FastAPI, Pydantic, SQLAlchemy, redis‑py | HTTP/gRPC endpoint, request validation, auth, job persistence, queue publishing |
| Worker (Celery) | Python 3.11 | Celery, kombu, structlog | Pull jobs, invoke Model Service, run post‑processor, store results |
| Model Service | Python 3.11 | vLLM, transformers, torch, safetensors | Load fine‑tuned Code‑LLM, generate refactoring suggestions, enforce token‑level safety |
| Post‑Processor | Python 3.11 | lib2to3, astor, black, difflib, pylint | Parse generated code, verify syntax, compute diff, run static analysis, assign quality score |
| Auth Service | Go 1.22 | go‑jwt, chi, pgx | Issue/validate JWTs, role‑based access control |
| Data Stores | — | PostgreSQL 15, Redis 7 | Persistent metadata, queueing, caching |

---

## 3. Data Model

### 3.1 Database Schema (PostgreSQL)

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    role TEXT CHECK (role IN ('admin','user')) DEFAULT 'user',
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE jobs (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    status TEXT CHECK (status IN ('queued','running','completed','failed')) NOT NULL,
    language TEXT NOT NULL,
    input_sha256 BYTEA NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    result_url TEXT,          -- S3 pre‑signed link
    quality_score REAL,
    diff_summary TEXT
);
```

### 3.2 In‑Memory Task Payload (Redis)

```json
{
  "job_id": "uuid",
  "user_id": "uuid",
  "language": "python",
  "files": [
    {"path": "src/module.py", "content": "base64‑encoded source"}
  ],
  "settings": {
    "max_tokens": 2048,
    "temperature": 0.0,
    "refactor_style": "aggressive"
  }
}
```

### 3.3 Model Prompt Template (vLLM)

```
[INST]You are an expert software engineer. Refactor the following {language} code to be more readable, idiomatic, and performant while preserving behavior. Return ONLY the refactored code.[/INST]

<code>
{source}
</code>
```

---

## 4. Key APIs / Interfaces

### 4.1 Public REST API (FastAPI)

| Method | Path | Auth | Request Body | Response |
|--------|------|------|--------------|----------|
| POST | `/v1/jobs` | Bearer JWT | `JobCreateRequest` (language, files, settings) | `JobCreateResponse` (job_id, status) |
| GET | `/v1/jobs/{job_id}` | Bearer JWT | – | `JobStatusResponse` (status, quality_score, diff_url) |
| GET | `/v1/jobs/{job_id}/diff` | Bearer JWT | – | `text/plain` diff |
| POST | `/v1/auth/login` | – | `LoginRequest` | `LoginResponse` (access_token, refresh_token) |
| POST | `/v1/auth/refresh` | – | `RefreshRequest` | `LoginResponse` |

#### Schemas (Pydantic)

```python
class FileDTO(BaseModel):
    path: str
    content: str  # base64

class JobCreateRequest(BaseModel):
    language: Literal["python","javascript","go","java","cpp"]
    files: List[FileDTO]
    settings: Optional[Dict[str, Any]] = {}

class JobCreateResponse(BaseModel):
    job_id: UUID
    status: str

class JobStatusResponse(BaseModel):
    job_id: UUID
    status: str
    quality_score: Optional[float]
    diff_url: Optional[str]
```

### 4.2 Internal Celery Task

```python
@celery_app.task(bind=True, name="code_cleanser.refactor")
def refactor_task(self, payload: dict) -> dict:
    """
    1. Decode files
    2. Call ModelService.generate()
    3. Run PostProcessor.validate_and_diff()
    4. Upload diff & refactored files to S3
    5. Return metadata for DB update
    """
```

### 4.3 Model Service RPC (gRPC)

```proto
service CodeModel {
  rpc Generate (GenerateRequest) returns (GenerateResponse);
}

message GenerateRequest {
  string language = 1;
  string source_code = 2;
  int32 max_tokens = 3;
  float temperature = 4;
}

message GenerateResponse {
  string refactored_code = 1;
  repeated string safety_warnings = 2;
}
```

---

## 5. Technology Stack

| Layer | Technology | Reason |
|-------|------------|--------|
| **API** | FastAPI (Python) | High performance, async, OpenAPI auto‑gen |
| **Task Queue** | Celery + Redis | Proven horizontal scaling, easy retry semantics |
| **LLM Inference** | vLLM (GPU‑accelerated) | Low‑latency serving for 15‑B+ models |
| **Model** | Fine‑tuned StarCoder‑15B (Apache‑2.0) | State‑of‑the‑art code generation, permissive license |
| **Post‑Processing** | AST libraries (lib2to3, astor), Black, Pylint | Guarantees syntactic correctness and style |
| **Auth** | JWT (HS256) + Go microservice | Language‑agnostic, reusable across Axentx |
| **Storage** | PostgreSQL, Redis, S3 (MinIO for dev) | Durable metadata, fast queue, cheap object storage |
| **Containerization** | Docker (multi‑stage) | Reproducible builds |
| **Orchestration** | Kubernetes (Helm) | Auto‑scaling, rolling updates |
| **CI/CD** | GitHub Actions + ArgoCD | Automated testing, canary deployments |
| **Observability** | Prometheus + Grafana, Loki (logs) | End‑to‑end metrics & tracing |

---

## 6. Dependencies (pinned)

```txt
# Python
fastapi==0.110.0
uvicorn[standard]==0.27.0
pydantic==2.6.1
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
redis==5.0.1
celery==5.3.6
vllm==0.4.0
torch==2.2.0
transformers==4.38.2
black==24.2.0
pylint==3.1.0
lib2to3==3.11.0
boto3==1.34.0
python-jose==3.3.0

# Go (auth service)
github.com/golang-jwt/jwt/v5 v5.2.0
github.com/go-chi/chi/v5 v5.0.12
github.com/jackc/pgx/v5 v5.5.2
```

All dependencies are under permissive licenses compatible with commercial distribution.

---

## 7. Deployment Diagram

```
+-------------------+      +-------------------+      +-------------------+
|   Ingress (NGINX) | ---> |  FastAPI Service  | ---> |   Redis (Broker) |
+-------------------+      +-------------------+      +-------------------+
                                 |                         |
                                 v                         v
                         +-------------------+   +-------------------+
                         |   Celery Workers  |   |   Model Service   |
                         +-------------------+   +-------------------+
                                 |                         |
                                 v                         v
                         +-------------------+   +-------------------+
                         |   PostgreSQL DB   |   |   GPU Node (vLLM) |
                         +-------------------+   +-------------------+
                                 |
                                 v
                         +-------------------+
                         |   S3 / MinIO      |
                         +-------------------+
```

* **Ingress** – TLS termination, rate‑limiting, path routing (`/v1/*`).  
* **FastAPI** – 3 replicas behind a Service, autoscaled by CPU < 70 %.  
* **Celery Workers** – 4‑core CPU pods, horizontally scaled based on queue length.  
* **Model Service** – Dedicated GPU node (A100‑40GB) running vLLM; can be replicated for multi‑model serving.  
* **Observability** – Sidecar Prometheus exporters on each pod; logs shipped to Loki.

---

## 8. Security & Compliance

| Concern | Mitigation |
|---------|------------|
| **Authentication** | JWT with short‑lived access tokens (15 min) + refresh tokens (7 days). |
| **Authorization** | Role‑based checks in Orchestrator; only job owners can fetch results. |
| **Data Privacy** | Source code never persisted beyond job lifetime; stored only as encrypted blobs in S3 with TTL 24 h. |
| **Model Safety** | vLLM safety filters + post‑generation static analysis to block unsafe patterns. |
| **Transport Security** | All endpoints exposed via HTTPS (TLS 1.3). |
| **Supply‑Chain** | Dependencies pinned; CI runs `snyk` and `dependabot` scans. |
| **Audit** | Every request logged with user ID, hash of input, and outcome stored in PostgreSQL. |

---

## 9. Testing Strategy

| Layer | Tool | Coverage Goal |
|-------|------|---------------|
| Unit | pytest, hypothesis | 90 % |
| Integration | testcontainers (Postgres, Redis), FastAPI TestClient | 80 % |
| Load | locust (simulate 200 concurrent jobs) | ≤ 2 s latency per job (GPU node) |
| Security | OWASP ZAP, bandit | No critical findings |
| Model | Custom regression suite (10k code snippets) | ≥ 95 % functional equivalence after refactor |

CI pipeline runs all tests on each PR; nightly runs full regression suite.

---

## 10. Roadmap (Post‑Launch)

| Milestone | Target | Description |
|-----------|--------|-------------|
| **MVP** | v0.1 (4 weeks) | Core CLI, API, single‑GPU inference, diff output. |
| **IDE Integration** | v0.2 (8 weeks) | VS Code extension with inline suggestions. |
| **Multi‑Language Support** | v0.3 (12 weeks) | Add JavaScript/TypeScript and Go pipelines. |
| **Batch Mode & CI Hook** | v0.4 (16 weeks) | GitHub Action that auto‑cleans PRs. |
| **Enterprise Auth** | v0.5 (20 weeks) | SSO (SAML/OIDC) and audit‑log export. |
| **Self‑Hosted Option** | v0.6 (24 weeks) | Helm chart with optional on‑prem GPU node. |

---

## 11. Open Issues & Decisions

1. **Model Size vs Latency** – Evaluating 7B vs 15B for cost‑effective scaling.  
2. **Safety Filter Granularity** – Need to define whitelist of allowed refactorings (e.g., no API key insertion).  
3. **Result Storage** – Deciding between per‑job S3 bucket vs shared bucket with object‑level encryption.  

---

## 12. Appendices

### A. Helm Values (excerpt)

```yaml
replicaCount: 2
image:
  repository: ghcr.io/arkashira/code-cleanser
  tag: "v0.1.0"
  pullPolicy: IfNotPresent
resources:
  limits:
    cpu: "2000m"
    memory: "4Gi"
  requests:
    cpu: "500m"
    memory: "1Gi"
gpu:
  enabled: true
  resources:
    limits:
      nvidia.com/gpu: "1"
redis:
  enabled: true
postgres:
  enabled: true
s3:
  endpoint: "https://minio.internal"
  bucket: "code-cleanser-results"
```

### B. Example Diff Output

```diff
--- a/src/utils.py
+++ b/src/utils.py
@@ -1,12 +1,10 @@
-def compute(a,b):
-    # complicated logic
-    result = 0
-    for i in range(a):
-        result += b*i
-    return result
+def compute(a: int, b: int) -> int:
+    """Compute sum of b*i for i in range(a)."""
+    return b * sum(range(a))
```

--- 

*Prepared by:* Senior Product/Engineering Lead – code‑cleanser  
*Date:* 2026‑06‑18  
*Version:* 0.1.0‑draft
