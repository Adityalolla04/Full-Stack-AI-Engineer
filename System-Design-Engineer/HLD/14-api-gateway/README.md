# API Gateway

[Back to HLD](../README.md) · [Your practice space](practice/README.md)

## In simple words

A gateway is an entry point that routes external requests and applies shared edge policies.

## What to understand

Common duties include authentication checks, rate limits, and request routing. Services still enforce resource authorization.

## Think through this example

A browser calls one gateway that routes document and profile requests to different services.

## Common mistake

Treating gateway authentication as sufficient document-level authorization.

## Practice yourself

Draw request processing and decide which checks belong at the gateway versus the service.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[AlgoMaster reading reference; concise original study notes](https://algomaster.io/learn/system-design/api-gateway-pattern). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
