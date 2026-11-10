# Indexes and Query Plans

[Back to SQL](../README.md) · [Your practice space](practice/README.md)

## In simple words

Indexes offer alternative access paths; query plans show the chosen execution approach.

## What to understand

Study selectivity, composite order, scans, joins, sorting, and actual versus estimated row counts.

## Think through this example

A small table may be cheaper to scan than to traverse an index.

## Common mistake

Assuming an index is always used or always improves performance.

## Practice yourself

Choose an index for one query, predict its plan, and list measurements to collect.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/sql). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
