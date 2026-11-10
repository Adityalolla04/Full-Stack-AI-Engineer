# Consistent Hashing

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Consistent hashing maps keys and servers into an ordered hash space to reduce reassignment when membership changes.

## What to understand

Virtual nodes improve distribution; replication and failure handling are separate decisions.

## Think through this example

Adding a cache server moves a portion of keys instead of remapping almost everything.

## Common mistake

Expecting perfectly even load or treating hashing as a replication strategy.

## Practice yourself

Draw a hash ring before and after adding a server and track five keys.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/consistent-hashing). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
