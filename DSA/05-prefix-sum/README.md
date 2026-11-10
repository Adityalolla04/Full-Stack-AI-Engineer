# Prefix Sum

[Back to DSA](../README.md) · [Your practice space](practice/README.md)

## In simple words

Store cumulative totals to answer repeated range questions quickly.

## What to understand

An initial zero simplifies boundaries. Preparation is O(n); a range total is the difference of two prefix entries.

## Think through this example

For 3, 2, 7 the prefixes are 0, 3, 5, 12; the last two values total 12 minus 3.

## Common mistake

Mixing inclusive endpoints with exclusive prefix positions.

## Practice yourself

Answer inclusive range-sum queries and then count subarrays with a target sum.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/dsa/prefix-sum-introduction). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
