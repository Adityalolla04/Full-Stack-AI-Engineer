# Union Find

[Back to DSA](../README.md) · [Your practice space](practice/README.md)

## In simple words

Maintain groups that merge as connections are added.

## What to understand

Find identifies a representative; union merges groups. Path compression and union by size/rank make repeated operations very efficient.

## Think through this example

Connecting A-B then B-C puts A and C in the same group.

## Common mistake

Trying to support arbitrary edge deletion with a basic union-find structure.

## Practice yourself

Count components after edge insertions and detect redundant connections.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/dsa/union-find-introduction). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
