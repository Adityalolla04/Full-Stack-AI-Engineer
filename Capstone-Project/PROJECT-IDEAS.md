# Projects that connect the topics

These are earlier incremental project ideas retained for reference. Use the [capstone workspaces](README.md) for the final application; create separate prototypes only when useful. Write your own implementation, tests, and run instructions.

## 1. Learning Tracker — phases 1–4

Build a Python API, PostgreSQL database, and React UI to track topics, study sessions, notes, and review dates.

Milestones: persisted CRUD → SQL summaries → authentication and per-user authorization → background review scheduling → UI → design refactoring. Add caching only after measuring the summary endpoint.

Acceptance criteria:

- Two users cannot access one another's records.
- Invalid input is rejected consistently, and database constraints enforce invariants.
- Pagination is deterministic; failed transactions do not leave partial updates.
- Tests cover API/database integration and one complete browser workflow.
- Setup works from a clean environment using documented commands.

## 2. Knowledge Assistant — phases 5–7

Build on the same engineering skills: upload documents → track ingestion jobs → retrieve authorized chunks → answer with citations → evaluate quality. Start with synthetic/public documents.

Milestones: simple retrieval baseline → cited answers and abstention → evaluation harness → streaming UI → scoped tools/MCP → observability and deployment.

Acceptance criteria:

- Ingestion retries do not duplicate logical documents; deletion removes retrievable content.
- Users cannot retrieve one another's documents; access controls apply to retrieval and source viewing.
- Every displayed citation resolves to a source chunk.
- A versioned evaluation report separates retrieval quality, answer correctness, citation correctness, latency, and cost.
- Unanswerable inputs produce an explicit limitation; malicious document instructions do not grant tool permissions.
- Deployment has health checks, migrations, secret configuration, a backup/restore procedure, and a demonstrated rollback.

Set numerical performance targets before tuning, based on an explicit test dataset and workload. Record baseline and later measurements; do not invent results.

## 3. Portfolio capstone — phase 8

Extend the Knowledge Assistant into a Regulation Navigator or another domain you know. Reuse the existing LLM roadmap as conceptual context. Add advanced infrastructure or agents only where you can explain the benefit; keep optional experiments separate from the default application path.

Deliver: working demo, architecture diagram, reproducible setup, eval report, threat model, operational runbook, load-test results, two design-decision notes, and a short account of a bug and its fix. Present information retrieval as source-backed assistance rather than guaranteed domain advice.
