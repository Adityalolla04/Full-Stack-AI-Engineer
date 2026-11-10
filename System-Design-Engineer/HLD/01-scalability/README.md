# Scalability

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Scalability is the ability to handle increased load while meeting service targets.

## What to understand

Vertical scaling enlarges a machine; horizontal scaling adds machines. Identify the bottleneck before choosing either.

## Think through this example

Adding API replicas helps CPU load but not a single overloaded database.

## Common mistake

Equating scalability with availability or assuming replicas remove every bottleneck.

## Practice yourself

Estimate a study app's load for 1,000 and 100,000 users and identify the first limit.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/scalability). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
