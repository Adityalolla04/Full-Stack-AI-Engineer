# Event Driven Architecture

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Services react to events representing completed facts.

## What to understand

Specify event schemas, ownership, delivery semantics, observability, and eventual consistency. Events differ from direct commands.

## Think through this example

An ingestion-completed event updates search availability and a notification view.

## Common mistake

Hiding business dependencies in undocumented event chains.

## Practice yourself

Draw an upload-to-index event flow with retries and dead-letter handling.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/event-driven-architecture). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
