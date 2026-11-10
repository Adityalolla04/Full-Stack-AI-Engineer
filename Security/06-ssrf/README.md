# SSRF

[Back to Security](../README.md) · [Your practice space](practice/README.md)

## In simple words

SSRF tricks a server into making unintended outbound requests.

## What to understand

Constrain destinations and schemes, enforce network egress policy, and handle redirects and DNS resolution carefully.

## Think through this example

A document-import URL must not let the server fetch internal-only resources.

## Common mistake

Relying on a simple substring denylist for localhost or private addresses.

## Practice yourself

Design a URL-fetch feature's destination checks and network restrictions in a local lab.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Official OWASP reference; supplementary original security notes](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
