# Bloom Filter

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

A Bloom filter can say definitely absent or possibly present using compact probabilistic state.

## What to understand

Standard insert-only filters have false positives but no false negatives if used correctly. Confirm positives against the real store.

## Think through this example

A crawler skips an expensive lookup when a URL is definitely unseen in a membership-check context.

## Common mistake

Treating a positive as proof of membership or deleting bits from a standard filter.

## Practice yourself

Explain how more inserted keys change false-positive probability and where an exact lookup is still needed.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/bloom-filters). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
