# ReAct Agent Loop

[Back to LLM](../README.md) · [Your practice space](practice/README.md)

## In simple words

An agent alternates selecting an action, receiving an observation, and deciding the next step.

## What to understand

Use explicit step, time, and cost limits; record observable actions and outcomes rather than relying on hidden reasoning.

## Think through this example

An assistant searches, reads a result, and either answers or requests one more targeted lookup.

## Common mistake

Allowing an unbounded loop because each step seems useful.

## Practice yourself

Describe a bounded research loop and its stop conditions.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/genai). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
