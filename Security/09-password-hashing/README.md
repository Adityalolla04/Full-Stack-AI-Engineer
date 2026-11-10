# Password Hashing

[Back to Security](../README.md) · [Your practice space](practice/README.md)

## In simple words

Passwords require a purpose-built slow password-hashing scheme with unique salts.

## What to understand

Use a maintained implementation such as Argon2id with parameters suited to deployment; handle upgrades and verification safely.

## Think through this example

Equal passwords should not produce identical stored hashes when different salts are used.

## Common mistake

Using a fast general-purpose digest as password storage.

## Practice yourself

Explain salt versus optional pepper and plan a hash-parameter upgrade.

Write your own implementation in `practice/` when ready. No solution or starter code is supplied.

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Official OWASP reference; supplementary original security notes](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
