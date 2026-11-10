# Effects Refs and Custom Hooks

[Back to React](../README.md) · [Your practice space](practice/README.md)

## In simple words

Effects synchronize with external systems; refs retain values without triggering rendering.

## What to understand

Understand dependency tracking, cleanup, stale closures, and separating events from synchronization. Custom hooks share logic, not state instances automatically.

## Think through this example

A subscription must be cleaned up when its dependency or component lifetime changes.

## Common mistake

Using effects to calculate values that can be derived during rendering.

## Practice yourself

Describe a subscription lifecycle and a stale-response race without implementing a solution.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/react). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
