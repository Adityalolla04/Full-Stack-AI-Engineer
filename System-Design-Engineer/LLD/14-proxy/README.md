# Proxy

[Back to LLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

Stand in for another object while controlling access, location, or creation.

## What to understand

A proxy can provide authorization, lazy loading, or remote access while retaining the expected interface.

## Think through this example

A document proxy checks the current user's permission before fetching bytes.

## Common mistake

Caching a prior authorization decision without considering permission changes.

## Practice yourself

Design an access-checking proxy and describe denial and dependency-failure behavior.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/lld/proxy). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
