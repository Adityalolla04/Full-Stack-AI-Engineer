# Reranking

[Back to LLM](../README.md) · [Your practice space](practice/README.md)

## In simple words

A reranker reorders retrieved candidates using a more expensive relevance judgment.

## What to understand

Use a broad candidate stage followed by a narrower ranking stage; measure quality against added latency and cost.

## Think through this example

Twenty candidate passages can be reduced to a smaller, more relevant context set.

## Common mistake

Expecting reranking to recover evidence absent from the initial candidates.

## Practice yourself

Define an experiment comparing retrieval alone with retrieval plus reranking.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/rag). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
