# Composition over Inheritance

[Back to LLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Build objects from collaborators when behavior should vary independently.

## What to understand

Delegation lets you swap parts without a deep hierarchy; inheritance still fits genuine substitutable relationships.

## Think through this example

An assistant has a retriever and a generator rather than inheriting from both.

## Common mistake

Assuming composition means every tiny operation needs a new class.

## Practice yourself

Draw two interchangeable retrieval strategies composed into an assistant.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/lld/composition). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
