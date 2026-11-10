# CSRF

[Back to Security](../README.md) · [Your practice space](practice/README.md)

## In simple words

CSRF abuses credentials that a browser sends automatically to perform unwanted actions.

## What to understand

Use suitable anti-CSRF tokens, SameSite cookies, origin checks, and safe method semantics for the authentication design.

## Think through this example

A logged-in browser must not accept an unrelated site's forged change request.

## Common mistake

Assuming CORS alone prevents every cross-site request.

## Practice yourself

Diagram a state-changing cookie-authenticated request and its CSRF checks.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Official OWASP reference; supplementary original security notes](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
