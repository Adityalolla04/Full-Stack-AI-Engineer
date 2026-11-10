# Monotonic Stack

[Back to DSA](../README.md) · [Your practice space](practice/README.md)

## In simple words

Keep unresolved elements in increasing or decreasing order.

## What to understand

An arriving value resolves earlier candidates that can no longer remain in the stack. Each item is pushed and popped at most once.

## Think through this example

In 2, 1, 4, the value 4 is the next greater value for both earlier entries.

## Common mistake

Treating equal values as greater when the problem requires strict comparison.

## Practice yourself

Solve next-greater-element and daily-temperatures problems; include duplicate values.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/dsa/monotonic-stack-introduction). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
