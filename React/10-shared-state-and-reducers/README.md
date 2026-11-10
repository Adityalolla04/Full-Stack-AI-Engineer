# Shared State and Reducers

[Back to React](../README.md) · [Your practice space](practice/README.md)

## In simple words

Shared state needs one clear owner and explicit update rules.

## What to understand

Lift state when siblings coordinate; consider context/reducers for wider needs and distinguish server cache from local UI state.

## Think through this example

A shared filter controls both a list and summary while server data has its own freshness policy.

## Common mistake

Duplicating derived data in several states that can disagree.

## Practice yourself

Choose ownership for filters, login status, form drafts, and fetched documents.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/react). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
