# ORM and Migrations

[Back to Backend](../README.md) · [Your practice space](practice/README.md)

## In simple words

An ORM maps application objects to database operations; migrations version schema changes.

## What to understand

Understand generated queries, N+1 problems, transaction scope, and backward-compatible schema rollout.

## Think through this example

Adding a nullable column before deploying readers can avoid breaking old application instances.

## Common mistake

Treating an ORM as a replacement for SQL knowledge.

## Practice yourself

Plan an expand-migrate-contract change and inspect the queries a list endpoint would trigger.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/backend). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
