# Replication

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Replication maintains copies for resilience and sometimes read scaling.

## What to understand

Synchronous acknowledgment can increase latency; asynchronous copying can expose lag and failover data loss.

## Think through this example

A newly saved note appears on the primary before a lagging read replica sees it.

## Common mistake

Assuming a replica always contains the latest committed write.

## Practice yourself

Explain read-after-write behavior and define recovery objectives for an outage.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/database-replication). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
