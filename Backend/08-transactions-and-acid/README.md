# Transactions and ACID

[Back to Backend](../README.md) · [Your practice space](practice/README.md)

## In simple words

A transaction groups changes under defined correctness guarantees.

## What to understand

Learn atomicity, consistency of declared invariants, isolation, and durability; isolation levels differ in allowed anomalies.

## Think through this example

Creating a session and updating a related total should not leave only half the intended change.

## Common mistake

Assuming ACID means every operation is serializable.

## Practice yourself

Describe a rollback case and an overselling race under concurrent transactions.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/backend). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
