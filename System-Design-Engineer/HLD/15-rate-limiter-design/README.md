# Rate Limiter Design

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

A rate limiter bounds resource consumption over time.

## What to understand

Compare fixed windows, sliding windows, token buckets, and leaky buckets. Shared state and atomic updates matter across replicas.

## Think through this example

A token bucket permits a short burst while bounding the sustained average.

## Common mistake

Using one in-memory counter per server and calling it a global quota.

## Practice yourself

Design per-user and per-tenant limits with clear behavior if the limiter store fails.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/rate-limiting). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
