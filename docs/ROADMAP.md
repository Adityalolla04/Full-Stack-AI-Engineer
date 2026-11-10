# Step-by-step learning strategy

## Find each track

[Python](../Python/README.md) · [ML/DL/CV](../ML-DL-CV/README.md) · [LLM](../LLM/README.md) · [DSA](../DSA/README.md) · [SQL](../SQL/README.md) · [Backend](../Backend/README.md) · [React](../React/README.md) · [LLD](../System-Design-Engineer/LLD/README.md) · [HLD](../System-Design-Engineer/HLD/README.md) · [DevOps](../DevOps/README.md) · [Security](../Security/README.md) · [Capstone](../Capstone-Project/README.md).

The numbered screenshot folders preserve the requested topic order. Follow the phases below for prerequisites. Notes and practice prompts are provided; you write the implementations yourself.

## Your starting point

You report completing Python, ML/DL/CV, and LLM Mastery. Use those as prior learning and validate with short practical tasks rather than repeat entire courses. Local inspection found Python notebooks, substantial ML/DL/CV material, and a mostly scaffolded LLM curriculum. This distinguishes documented implementation from your knowledge; it does not assume you have forgotten or never studied a topic.

The seven images contain 140 topic entries: backend, DSA, high-level design (HLD), low-level design (LLD), agentic AI, DevOps, and cybersecurity. They are useful inventories, not a prerequisite order. They omit frontend development, hands-on SQL foundations, accessibility, and much of the practical delivery workflow. This plan adds those and integrates repeated topics such as caching, rate limiting, and secrets management.

## Working stack

Use Python with FastAPI for APIs; PostgreSQL for relational data; HTML/CSS, JavaScript, TypeScript, and React for the UI; Redis when a measured cache/queue need appears; Docker Compose for local services; and GitHub Actions for CI. Add one cloud environment after the local application works. For AI, start with the model/provider tools you already know, simple explicit workflows, and a measured retrieval baseline. Choose framework and model versions at implementation time and record them in project dependency files.

This is a proposed learning stack, not a requirement to learn every competing framework. The official [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) supplies a sequential API reference, and [React Learn](https://react.dev/learn) covers components, events, state, and sharing data. Read the relevant section and immediately build the corresponding feature.

## Schedule and exit checkpoints

The estimate assumes 12–15 focused hours/week, roughly 336–420 hours total. At 6–8 hours/week, roughly double the calendar duration. Weeks are planning ranges, not promises of mastery. Advance when you pass the checkpoint; shorten a phase when you can demonstrate its outcomes independently.

| Phase | Weeks | Learn and practice in order | Deliverable and exit checkpoint |
|---|---|---|---|
| 0: Baseline | 1 | Audit earlier work; Python functions/classes, exceptions, modules, typing, environments, pytest; Git and shell basics | Turn a notebook routine into an importable CLI with validation and tests; explain one ML and one LLM implementation without notes |
| 1: HTTP and databases | 2–4 | DNS/TCP/TLS overview → HTTP → REST → SQL SELECT/JOIN/GROUP BY → schemas/constraints → transactions → indexes → ORM/migrations | Learning Tracker API backed by PostgreSQL; explain a query plan, rollback, pagination, invalid requests, and a migration |
| 2: Reliable backend | 5–7 | Sessions/cookies → JWT and OAuth/OIDC distinction → authorization → uploads → background jobs → queues → Redis → rate limits → streaming/WebSockets | Two-user API with ownership checks, idempotent job handling, integration tests, request logs, and failure recovery |
| 3: Frontend and integration | 8–10 | Semantic HTML → CSS/layout/responsiveness → JS async/fetch → TypeScript → React state/forms/routing → API integration → UI tests | Accessible Learning Tracker UI with login, loading/empty/error states, keyboard navigation, and tested user flow |
| 4: Python design | 11–12 | OOP → composition → SOLID pragmatically → diagrams → strategy/factory/adapter → remaining pattern comparisons → thread safety | Refactor model/retriever providers behind interfaces; add a provider without changing callers; test concurrency-sensitive state |
| 5: Applied AI | 13–16 | LLM checkpoint → structured output → embeddings → chunking/retrieval → reranking → evals → tool calling → bounded agent loop → MCP | Knowledge Assistant with source citations, abstention, persistent ingestion, evaluation dataset, cost/latency report, and tool authorization |
| 6: Delivery and operations | 17–20 | Linux/networking refresh → Docker → Compose → CI → secrets → reverse proxy/TLS → cloud deployment → logs/metrics → rollback | Reproducible deployment, passing CI, backup/restore drill, health checks, dashboard, load test, and rollback demonstration |
| 7: System design | 21–24 | Workload estimates → bottlenecks → cache/load balance/storage → replication/consistency → queues/events → sharding → failure patterns | Design and benchmark the Knowledge Assistant; produce two architecture decisions and a failure-recovery report |
| 8: Advanced topics and portfolio | 25–28 | Kubernetes/Helm overview and lab → Terraform/Ansible comparison → advanced events/sagas → multi-agent comparison → LoRA experiment if useful → security review | Polished capstone, demo, runbook, threat model, reproducible evals, and three mock interviews; advanced lab notes even when not used in capstone |

Throughout phases 1–8: spend 2–3 hours/week on DSA, following [the practice sequence](study-guides/PROBLEM-BANK.md). Apply security and test failure cases in every phase. Do not postpone authentication/authorization or input validation until the security review.

## A sustainable weekly routine

- Two sessions: learn a small concept, write a short note, complete a focused lab.
- Two sessions: implement project features and meaningful tests.
- One session: solve/revisit DSA problems and explain complexity.
- One session: integrate, demonstrate, review failures, and plan next week.
- Keep one day free or use it for recovery. Allocate about 60% of learning time to implementation, 20% to reading/notes, and 20% to revision/debugging.

For each 90-minute session: 10 minutes retrieval from memory, 20 minutes reading, 45 minutes coding, 15 minutes explaining/testing/recording mistakes. Longer project sessions can combine two blocks.

## Definition of learned

1. Explain the concept in your own words, including when not to use it.
2. Implement a small example without copying a tutorial.
3. Test at least one normal, boundary, and failure case.
4. Apply it to the current project or explain why the project does not need it.
5. Repeat the essential task after a week and record what you forgot.

Use status values `not-started`, `learning`, `practiced`, `validated`, and `revisit`. Reading alone does not set `validated`. Prior coursework starts as `reported-complete / checkpoint-pending` until you choose to demonstrate it.

## Priorities and tradeoffs

Build a modular application before splitting into microservices. Learn SQL before ORM shortcuts, HTTP before auth libraries, one working deployment before Kubernetes, retrieval evaluation before increasingly complex agents, and simple patterns before memorizing 20 design-pattern names. Multi-agent orchestration and LoRA are advanced exercises: compare against a simpler baseline and retain only measured improvements.

Add explicit AI reliability work missing from the images: document-level access controls, retrieval leakage checks, evaluation-set separation, model/prompt/data versioning, tool timeouts and budgets, untrusted retrieved content, and deletion/reindexing behavior.

For cybersecurity, use the current [OWASP Top 10](https://owasp.org/projects/top-ten?lang=en) as the awareness baseline (2025 edition at planning time). Practice exploit-and-fix exercises only in your own local lab; write the mitigation and regression test for each issue.

## What to do today

Open the imported Python notebook, choose one small data-cleaning routine, and implement the first session in [START-HERE](study-guides/START-HERE.md). Save one note, one executable solution, and one test result before moving to another topic.
