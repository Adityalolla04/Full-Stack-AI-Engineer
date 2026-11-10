# Microservices

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Split an application into independently deployable services with clear ownership.

## What to understand

Network calls add latency and failure modes; separate data ownership and deployment justify the operational cost.

## Think through this example

An ingestion worker may scale separately from the interactive answer API.

## Common mistake

Splitting a small app into many services before identifying a real boundary.

## Practice yourself

Compare a modular monolith with two services and explain which you would build first.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/microservices-architecture). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
