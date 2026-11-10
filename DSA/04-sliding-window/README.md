# Sliding Window

[Back to DSA](../README.md) · [Your practice space](practice/README.md)

## In simple words

Reuse information from a contiguous range as its boundaries move.

## What to understand

A fixed window removes the outgoing item and adds the incoming item; a variable window restores a defined condition.

## Think through this example

The sums of length-two windows in 2, 5, 1 are 7 and 6; only two values change between windows.

## Common mistake

Applying a positive-number sum strategy unchanged when negative values are allowed.

## Practice yourself

Find the longest substring without repeated characters and the maximum sum of K consecutive values.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/dsa/sliding-window-introduction). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
