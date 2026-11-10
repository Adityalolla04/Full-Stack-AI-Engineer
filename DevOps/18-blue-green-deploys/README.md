# Blue Green Deploys

[Back to DevOps](../README.md) · [Your practice space](practice/README.md)

## In simple words

Keep two environments so traffic can switch from an old version to a tested new version.

## What to understand

Plan health validation, traffic switching, rollback, capacity, and schema compatibility.

## Think through this example

Green is tested before accepting users; blue remains available briefly for rollback.

## Common mistake

Assuming application rollback also reverses incompatible database changes.

## Practice yourself

Describe a release with a backward-compatible schema change and a rollback trigger.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/devops). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
