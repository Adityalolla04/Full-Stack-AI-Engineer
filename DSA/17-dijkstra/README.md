# Dijkstra

[Back to DSA](../README.md) · [Your practice space](practice/README.md)

## In simple words

Find shortest weighted paths by expanding the cheapest known unsettled distance.

## What to understand

Require non-negative weights. A priority queue selects the next candidate; skip stale distances after improvements.

## Think through this example

A direct cost 8 loses to two edges costing 2 and 3, whose total is 5.

## Common mistake

Using Dijkstra on negative edges or assuming unreachable nodes have distance zero.

## Practice yourself

Compute distances and reconstruct paths; include unreachable nodes and zero-weight edges.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/dsa/dijkstras-algorithm). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
