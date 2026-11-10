# Semantic and Instance Segmentation

[Back to ML-DL-CV](../README.md) · [Your practice space](practice/README.md)

## In simple words

Semantic segmentation labels pixels; instance segmentation also distinguishes individual objects.

## What to understand

Study masks, pixel/class imbalance, IoU/Dice, boundary quality, and annotation consistency.

## Think through this example

Two adjacent people share a semantic class but require separate instance masks.

## Common mistake

Using overall pixel accuracy on a background-dominated dataset as the only metric.

## Practice yourself

Compare semantic and instance outputs for a crowded scene and choose evaluation measures.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/dl). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.

## Your existing material

See the [existing-work guide](EXISTING-WORK.md) for imported files, exact notebook sections, coverage, and limitations.
