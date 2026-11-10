# Consistency Models

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Consistency models define which writes readers can observe and in what order.

## What to understand

Distinguish linearizability, eventual consistency, causal ordering, and session guarantees such as read-your-writes.

## Think through this example

A user expects to see their own edited note immediately even if others see it slightly later.

## Common mistake

Using the vague word strong without specifying an observable guarantee.

## Practice yourself

Choose guarantees separately for profile edits, analytics, and document permissions.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/consistency-models). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
