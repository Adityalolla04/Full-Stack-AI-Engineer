# Sessions and Cookies

[Back to Backend](../README.md) · [Your practice space](practice/README.md)

## In simple words

A cookie transports browser state; a server session maps an opaque identifier to stored state.

## What to understand

Study Secure, HttpOnly, SameSite, expiration, rotation after login, and server-side invalidation.

## Think through this example

The browser sends a session ID while the server keeps the user identity and permissions.

## Common mistake

Putting sensitive session data in an unsigned browser-controlled value.

## Practice yourself

Compare server sessions and bearer tokens, including logout and CSRF implications.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/backend). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
