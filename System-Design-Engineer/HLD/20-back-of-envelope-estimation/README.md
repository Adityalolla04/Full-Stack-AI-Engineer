# Back of Envelope Estimation

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Approximate calculations connect requirements to resource needs.

## What to understand

Estimate requests per second, peak multiplier, payload sizes, storage growth, and bandwidth; write units and assumptions.

## Think through this example

10,000 users making 20 requests daily produce 200,000 requests daily, about 2.3 per second on average.

## Common mistake

Sizing only for average traffic or presenting assumptions as measurements.

## Practice yourself

Estimate annual document storage and peak ingestion throughput, then list what you would measure.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Reading reference; supplementary original study notes](https://algomaster.io/learn/system-design-interviews/course-roadmap). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
