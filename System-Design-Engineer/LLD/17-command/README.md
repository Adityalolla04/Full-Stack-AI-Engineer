# Command

[Back to LLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Represent an action as an object or record so it can be queued, logged, or retried.

## What to understand

Separate request description from execution. Undo and idempotency require explicit design.

## Think through this example

A reindex command carries document identity rather than a live browser request.

## Common mistake

Assuming every command is reversible or safe to retry.

## Practice yourself

Define create-task and cancel-task commands with retry rules.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/lld/command). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
