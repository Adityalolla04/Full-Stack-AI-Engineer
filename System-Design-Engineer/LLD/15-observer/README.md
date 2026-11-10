# Observer

[Back to LLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Notify interested listeners when an object's state changes.

## What to understand

Define subscription lifetime, event payload, notification order, and failure handling.

## Think through this example

When a task completes, a progress view and audit recorder both receive a notification.

## Common mistake

Leaking listeners or allowing one listener failure to block every other one.

## Practice yourself

Design completion notifications and explain unsubscribe behavior.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/lld/observer). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
