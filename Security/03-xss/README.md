# XSS

[Back to Security](../README.md) · [Your practice space](practice/README.md)

## In simple words

Cross-site scripting makes attacker-controlled content execute in another user's browser.

## What to understand

Use context-appropriate output encoding, safe rendering APIs, sanitization where HTML is necessary, and defense-in-depth CSP.

## Think through this example

A note containing markup should display as text unless trusted sanitization explicitly permits it.

## Common mistake

Assuming one generic escaping rule works in HTML, JavaScript, CSS, and URLs.

## Practice yourself

Identify rendering contexts in a notes UI and specify safe handling for each.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Official OWASP reference; supplementary original security notes](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
