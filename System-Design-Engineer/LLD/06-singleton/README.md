# Singleton

[Back to LLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

A singleton restricts a class to one managed instance in a particular runtime context.

## What to understand

Understand initialization, concurrency, global state, and test isolation. One process-local singleton is not one instance across a cluster.

## Think through this example

A shared configuration object may be convenient, but tests still need controllable configuration.

## Common mistake

Using hidden global state as a substitute for dependency injection.

## Practice yourself

Compare explicit shared-object injection with a singleton for application settings.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/lld/singleton). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
