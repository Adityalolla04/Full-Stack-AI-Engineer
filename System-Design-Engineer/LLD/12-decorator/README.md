# Decorator

[Back to LLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Wrap an object to add behavior while preserving its interface.

## What to understand

Wrappers can compose logging, timing, or caching; their order changes behavior.

## Think through this example

Timing outside a cache measures hits too, while timing inside measures only work that reaches the wrapped operation.

## Common mistake

Confusing the design pattern with only Python's decorator syntax.

## Practice yourself

Draw two wrapper orders and explain which calls are logged and timed.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/lld/decorator). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
