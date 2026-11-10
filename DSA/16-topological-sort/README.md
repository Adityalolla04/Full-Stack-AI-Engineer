# Topological Sort

[Back to DSA](../README.md) · [Your practice space](practice/README.md)

## In simple words

Order directed dependencies so every prerequisite appears first.

## What to understand

Only directed acyclic graphs have a complete topological order. Indegree removal and DFS finishing order are two approaches.

## Think through this example

Python before API before deployment is valid; API requiring deployment while deployment requires API is a cycle.

## Common mistake

Returning a partial ordering without reporting the cycle.

## Practice yourself

Order course prerequisites and detect cycles, including isolated courses.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/dsa/topological-sort-introduction). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
