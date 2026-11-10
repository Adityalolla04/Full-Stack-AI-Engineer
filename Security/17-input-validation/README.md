# Input Validation

[Back to Security](../README.md) · [Your practice space](practice/README.md)

## In simple words

Validate external input against explicit shape and business constraints.

## What to understand

Set size, range, format, and nesting limits; validate again at trusted boundaries. Validation complements output encoding and parameterized queries.

## Think through this example

A valid document ID still needs ownership authorization.

## Common mistake

Rejecting only known bad strings instead of defining acceptable input.

## Practice yourself

List validation and authorization checks separately for a document-download request.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Official OWASP reference; supplementary original security notes](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
