# Database Sharding

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Sharding divides data across independent database partitions.

## What to understand

Choose a shard key based on access patterns; consider hot keys, cross-shard queries, and rebalancing.

## Think through this example

Sharding documents by tenant keeps tenant-local queries together but large tenants may dominate one shard.

## Common mistake

Confusing sharding with replication, which copies data.

## Practice yourself

Compare tenant-based and hash-based shard keys for a document assistant.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/sharding). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
