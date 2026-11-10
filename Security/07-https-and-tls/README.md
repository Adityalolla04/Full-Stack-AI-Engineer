# HTTPS and TLS

[Back to Security](../README.md) · [Your practice space](practice/README.md)

## In simple words

TLS protects transport confidentiality and integrity and authenticates peers according to certificate validation.

## What to understand

Understand certificate trust, hostname checks, termination points, renewal, and traffic after termination.

## Think through this example

Browser-to-proxy TLS does not automatically protect proxy-to-service traffic.

## Common mistake

Disabling certificate verification to make a connection work.

## Practice yourself

Draw every network hop and state where TLS is verified and terminated.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Official OWASP reference; supplementary original security notes](https://cheatsheetseries.owasp.org/). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
