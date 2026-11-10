# CAP Theorem

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

During a network partition, a distributed system cannot guarantee both linearizable consistency and availability for every request.

## What to understand

CAP consistency is a precise single-copy ordering guarantee; availability means responses from nonfailed nodes, not an uptime percentage.

## Think through this example

Disconnected replicas cannot both accept conflicting writes while guaranteeing one immediate agreed order.

## Common mistake

Saying choose any two without specifying a partition or the formal guarantees.

## Practice yourself

Compare responses for balance reads and social likes during a partition.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/cap-theorem). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
