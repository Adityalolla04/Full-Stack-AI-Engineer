# Notes workspace

Use one note per concept, with a concrete example and links to executable practice. Start with `python/notebook-to-module.md`, then `backend/http-request-lifecycle.md` and `databases/transactions.md` as those lessons are completed.

Use [the note template](templates/README.md). Existing implementations now live in concept-specific `practice/existing/` folders; link to them rather than copying them into notes. Shared notebook sections are indexed in each subject's `EXISTING-WORK.md`.

## First reference note: learning versus engineering Python

A notebook can depend on cells executed in a previous order. A reusable module makes its inputs, outputs, dependencies, and errors explicit. Move transformation logic into functions and keep file/network access at the boundary. This makes the same logic usable from a CLI, an API endpoint, and a test.

For the study-session exercise, aggregation can be a pure function: the same validated rows produce the same totals. CSV parsing handles malformed input; the CLI reports results. Testing each boundary separately helps identify whether a failure comes from reading data, validating it, or computing totals.

Type hints document expected types and support static analysis; they do not automatically validate arbitrary CSV or HTTP input at runtime. Explicit validation is still required.
