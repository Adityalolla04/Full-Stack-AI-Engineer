# SOLID Principles

[Back to LLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

SOLID provides questions for keeping designs understandable and changeable.

## What to understand

Learn single responsibility, open/closed, Liskov substitution, interface segregation, and dependency inversion. Apply them to concrete changes, not class counts.

## Think through this example

An email sender can depend on a transport contract so tests use a fake transport.

## Common mistake

Adding abstractions without a real variation or breaking a parent's behavioral contract.

## Practice yourself

Review a single all-purpose service and propose a smaller responsibility boundary.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Reading reference; supplementary original study notes](https://blog.algomaster.io/p/solid-principles-explained-with-code). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
