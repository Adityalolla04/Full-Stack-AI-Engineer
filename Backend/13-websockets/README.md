# WebSockets

[Back to Backend](../README.md) · [Your practice space](practice/README.md)

## In simple words

WebSockets support ongoing bidirectional messages over a persistent connection.

## What to understand

Plan authentication, heartbeat, reconnect, backpressure, and message ordering. Compare with SSE for server-only streams.

## Think through this example

A collaborative editor needs client-to-server updates while a generated answer may only need server-to-client streaming.

## Common mistake

Ignoring slow clients or losing events silently on reconnect.

## Practice yourself

Choose WebSockets or SSE for three use cases and describe reconnection behavior.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/backend). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
