# OAuth 2.0

[Back to Backend](../README.md) · [Your practice space](practice/README.md)

## In simple words

OAuth delegates access to resources without sharing the user's password with every application.

## What to understand

Separate client, authorization server, resource server, scopes, and grants. OIDC adds an identity layer; OAuth alone is not a login protocol.

## Think through this example

A study app requests limited access to a user's calendar through an authorization flow.

## Common mistake

Confusing access tokens with ID tokens or accepting arbitrary redirect destinations.

## Practice yourself

Diagram authorization code with PKCE and label who validates each value.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/backend). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
