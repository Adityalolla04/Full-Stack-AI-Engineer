# Load Balancing

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

A load balancer routes requests among healthy backends.

## What to understand

Compare round robin, least connections, and hashing. Health checks, connection duration, and session state affect routing.

## Think through this example

Three API instances can share traffic, but an unhealthy instance should stop receiving new requests.

## Common mistake

Ignoring the balancer's own availability or uneven request cost.

## Practice yourself

Sketch routing for short API calls and long-lived WebSockets; compare failure behavior.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/load-balancers). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
