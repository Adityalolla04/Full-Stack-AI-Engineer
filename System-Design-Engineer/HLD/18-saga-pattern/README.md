# Saga Pattern

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

A saga coordinates a multi-step business operation using local transactions and compensating actions.

## What to understand

Compensation is a new business action, not a universal database rollback. Steps and compensation must tolerate retries.

## Think through this example

If a reservation succeeds but payment fails, release the reservation through a compensating operation.

## Common mistake

Assuming every external side effect can be perfectly undone.

## Practice yourself

Design an enrollment-and-payment saga with failure at each step.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/saga-pattern). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
