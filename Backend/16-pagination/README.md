# Pagination

[Back to Backend](../README.md) · [Your practice space](practice/README.md)

## In simple words

Pagination limits response size and lets clients navigate results.

## What to understand

Compare offset with cursor/keyset pagination. Use deterministic ordering and a unique tie-breaker.

## Think through this example

Two notes with the same timestamp still need distinct positions, such as timestamp plus ID.

## Common mistake

Using unstable order so items disappear or repeat between pages.

## Practice yourself

Specify pagination while new records are inserted between requests.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/backend). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
