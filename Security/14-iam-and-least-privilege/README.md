# IAM and Least Privilege

[Back to Security](../README.md) · [Your practice space](practice/README.md)

## In simple words

IAM assigns identities and permissions; least privilege limits actions and resources to what is needed.

## What to understand

Separate human and workload identities, avoid broad wildcards, and review permission changes.

## Think through this example

An ingestion worker can read its input objects but cannot administer the entire cloud account.

## Common mistake

Using an administrator identity for normal application operations.

## Practice yourself

Build a role/resource/action matrix for API, worker, developer, and deployment jobs.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Official OWASP reference; supplementary original security notes](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
