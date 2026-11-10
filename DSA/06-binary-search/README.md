# Binary Search

[Back to DSA](../README.md) · [Your practice space](practice/README.md)

## In simple words

Discard half a sorted or otherwise monotonic search space at each step.

## What to understand

Define the interval and invariant first. Standard lookup uses O(log n) comparisons; boundary searches handle duplicates explicitly.

## Think through this example

In 2, 4, 4, 9, the first position at least 4 is index 1.

## Common mistake

Assuming all sorted-search variants use the same boundary updates.

## Practice yourself

Find the first and last occurrence, including an absent target and an empty list.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/dsa/binary-search-introduction). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
