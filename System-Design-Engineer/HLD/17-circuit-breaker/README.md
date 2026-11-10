# Circuit Breaker

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Stop repeatedly calling an unhealthy dependency while allowing controlled recovery probes.

## What to understand

Closed permits calls; open rejects them; half-open tests recovery. Combine with deadlines and bounded retries.

## Think through this example

After repeated model-service failures, fail fast briefly instead of queuing more doomed calls.

## Common mistake

Retrying at several layers until the outage becomes a retry storm.

## Practice yourself

Define transition thresholds, probe limits, and fallback behavior for an answer endpoint.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/circuit-breaker-pattern). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
