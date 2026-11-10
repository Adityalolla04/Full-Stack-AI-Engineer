# OAuth Security

[Back to Security](../README.md) · [Your practice space](practice/README.md)

## In simple words

Secure OAuth requires carefully validating the authorization flow and delegated permissions.

## What to understand

Use current guidance for authorization code with PKCE, redirect validation, state/CSRF protection, and token handling; use OIDC when authenticating users.

## Think through this example

A stolen authorization code should not be useful without the verifier bound to its request.

## Common mistake

Using broad scopes or confusing identity and access-token purposes.

## Practice yourself

Trace a login/consent flow and identify substitution and redirect threats.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Official OWASP reference; supplementary original security notes](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
