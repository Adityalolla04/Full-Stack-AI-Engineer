# Splits Cross Validation and Leakage

[Back to ML-DL-CV](../README.md) · [Your practice space](practice/README.md)

## In simple words

Evaluation should simulate the conditions in which predictions will be used.

## What to understand

Choose random, grouped, stratified, or time-based splits appropriately. Fit preprocessing only on training data within each fold.

## Think through this example

Future records must not inform a model evaluated on past-to-future forecasting.

## Common mistake

Scaling the full dataset before cross-validation.

## Practice yourself

Choose split strategies for patient records, images from the same video, and time-series data.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/ml). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.

## Your existing material

See the [existing-work guide](EXISTING-WORK.md) for imported files, exact notebook sections, coverage, and limitations.
