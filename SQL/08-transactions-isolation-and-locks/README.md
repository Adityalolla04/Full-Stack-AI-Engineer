# Transactions Isolation and Locks

[Back to SQL](../README.md) · [Your practice space](practice/README.md)

## In simple words

Transactions coordinate concurrent changes under stated guarantees.

## What to understand

Learn commit/rollback, isolation anomalies, locks, deadlocks, and retryable transaction failures.

## Think through this example

Two concurrent seat reservations require protection of the capacity invariant.

## Common mistake

Assuming a read followed by a write is automatically safe at every isolation level.

## Practice yourself

Draw a lost-update timeline and propose a transaction strategy.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/sql). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
