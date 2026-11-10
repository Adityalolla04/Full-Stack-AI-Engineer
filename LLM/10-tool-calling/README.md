# Tool Calling

[Back to LLM](../README.md) · [Your practice space](practice/README.md)

## In simple words

A model can propose a structured request to an application tool.

## What to understand

The application validates arguments, permissions, budgets, and results before execution. A proposal is not authorization.

## Think through this example

A read-only search tool can be permitted while a deletion action requires a separately defined policy.

## Common mistake

Executing arbitrary model-provided commands or trusting tool text as instructions.

## Practice yourself

Design two tools with schemas, permission checks, deadlines, and error cases.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/genai). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
