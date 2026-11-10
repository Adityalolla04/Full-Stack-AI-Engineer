# Evals

[Back to LLM](../README.md) · [Your practice space](practice/README.md)

## In simple words

Evaluations measure whether changes improve the intended task.

## What to understand

Use representative versioned cases, held-out tests, explicit rubrics, and calibrated judging. Separate correctness, retrieval, safety, latency, and cost.

## Think through this example

A new retriever can improve recall yet produce worse answers if it adds distracting context.

## Common mistake

Tuning repeatedly on the final test set or trusting an uncalibrated model judge.

## Practice yourself

Draft an evaluation set covering answerable, unanswerable, ambiguous, and hostile-document inputs.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/genai). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
