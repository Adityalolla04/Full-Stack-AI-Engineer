# Kafka and Pub Sub

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Publish/subscribe lets producers announce events to independent consumers.

## What to understand

Kafka adds a durable partitioned log, consumer offsets, retention, and consumer groups. Ordering is normally per partition.

## Think through this example

One document-upload event can feed indexing and analytics consumers independently.

## Common mistake

Assuming global ordering or exactly-once business effects without application design.

## Practice yourself

Choose a partition key, replay policy, and duplicate-handling strategy for ingestion.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/pub-sub). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
