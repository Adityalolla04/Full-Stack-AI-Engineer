# Prompt Injection

[Back to Security](../README.md) · [Your practice space](practice/README.md)

## In simple words

Untrusted text can attempt to redirect an AI application's behavior.

## What to understand

Treat documents and tool results as data, enforce permissions outside the model, isolate tools, and minimize privileges.

## Think through this example

An uploaded document telling the assistant to export private files must not authorize that action.

## Common mistake

Believing a delimiter or instruction to ignore attacks guarantees protection.

## Practice yourself

Threat-model a malicious retrieved document and define enforceable limits on every tool.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Official OWASP reference; supplementary original security notes](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
