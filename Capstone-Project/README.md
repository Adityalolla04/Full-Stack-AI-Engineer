# Final Capstone — Learning and Knowledge Assistant

Build this yourself after foundational practice. This folder contains the brief and planning spaces, not an implementation.

A user tracks study sessions, uploads learning documents, and asks questions answered with citations to documents they are authorized to access. Start with synthetic/public data and a small scope.

## Milestones and workspaces

1. [Requirements](01-Requirements/README.md): users, flows, constraints, and acceptance criteria.
2. [Architecture](02-Architecture/README.md): components, interfaces, data ownership, and tradeoffs.
3. [Backend and SQL](03-Backend-and-SQL/README.md): validated CRUD, persistence, and ownership.
4. [React frontend](04-React-Frontend/README.md): accessible forms, lists, navigation, and errors.
5. [AI and retrieval](05-AI-and-Retrieval/README.md): ingestion, authorized retrieval, citations, and abstention.
6. [Tests and evals](06-Tests-and-Evals/README.md): correctness, quality, failures, latency, and cost.
7. [Security and DevOps](07-Security-and-DevOps/README.md): secrets, deployment, monitoring, recovery.
8. [Demo and documentation](08-Demo-and-Documentation/README.md): reproducible evidence and lessons learned.

## Completion criteria

- Users cannot read, edit, delete, or retrieve one another's private material.
- Records persist after restart; invalid data is consistently rejected.
- Job retries do not duplicate logical work; failures are visible and recoverable.
- Citations resolve to actual passages; insufficient evidence produces a clear limitation.
- A versioned evaluation set reports actual quality, latency, and cost.
- Another developer can reproduce setup and a demo.
- You can explain a DSA choice, LLD decision, HLD tradeoff, and security failure prevented.
