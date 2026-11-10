# SQL Injection

[Back to Security](../README.md) · [Your practice space](practice/README.md)

## In simple words

Injection occurs when untrusted input changes the intended structure of a database command.

## What to understand

Use parameterized queries, constrained dynamic identifiers, least-privilege database users, and safe error handling.

## Think through this example

A username containing SQL punctuation must remain data rather than become query syntax.

## Common mistake

Attempting to fix injection solely by stripping quote characters.

## Practice yourself

Describe safe query construction and regression cases in an isolated local lab.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Official OWASP reference; supplementary original security notes](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
