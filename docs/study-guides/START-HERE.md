# Your first seven study sessions

Allow 60–120 minutes per session; split a session if needed. Use synthetic study records, not the imported patient data. Write your own code in the corresponding Python, Backend, SQL, or DSA concept's `practice/` folder. These instructions are exercises for you, not supplied implementations.

## Session 1 — Python from notebook to module

Read a familiar routine in `Python/Previous-Practice/Basics/Python Practice.ipynb` or `Python/Previous-Practice/Basics/Numpy and Pandas.ipynb`. Then implement this independent problem:

**Input:** CSV rows with `topic,minutes,completed`; `completed` accepts only `true` or `false`, and `minutes` must be a non-negative integer. Blank topic names are invalid. Normalize topic names by stripping whitespace and lowercasing.

**Output:** total minutes by normalized topic, count of completed rows, and invalid-row count. Skip invalid rows and report them; raise a clear error if required headers are absent. Empty data produces empty totals and zero counts.

Example rows: `Python,30,true`, `python,20,false`, `SQL,-5,true`. Expected totals: `{"python": 50}`, completed count `1`, invalid count `1`.

Separate CSV reading from aggregation. Add type hints, a CLI entry point, and tests for the example, empty input, missing headers, invalid booleans, and duplicate topics. Explain why catching every exception silently would hide bugs.

**Checkpoint:** run it from a terminal without notebook state. If comfortable, move ahead; otherwise review only the specific missing Python skill.

## Session 2 — Testing and engineering Python

Extract pure functions; use a temporary file in an I/O test. Add a custom validation error where it helps. Explain iterators versus loading all rows, context managers for files, and why mutable default arguments are risky. Record an isolated environment setup and exact test command. Compare I/O concurrency with CPU parallelism in a short note; do not introduce async into pure data aggregation.

**Checkpoint:** a new reader can reproduce the run and see useful errors for invalid input.

## Session 3 — HTTP and the first API

Read the initial [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) sections. Create `GET /health`, `POST /topics`, and `GET /topics`. Define request/response schemas. Return `201` for creation, `200` for retrieval, and validation errors for invalid fields. For this session, an in-memory store is acceptable; document that restarting loses data.

**Checkpoint:** call the endpoints outside the UI and write tests for one successful request and one invalid request.

## Session 4 — SQL and persistence

Design `topics(id, name)` and `study_sessions(id, topic_id, minutes, completed, created_at)`. Add a foreign key, positive/zero minutes check, and a deliberate uniqueness rule for topic names. Write SELECT, JOIN, and GROUP BY queries before adding an ORM. Persist session records in PostgreSQL and create a migration.

**Checkpoint:** restarting the API preserves records. Explain the behavior when a topic referenced by sessions is deleted.

## Session 5 — DSA baseline

Solve two-sum and normalized anagram checking without looking at a solution. For two-sum, return indices of two distinct elements adding to the target, or `None`; `[2,7,11], 9` returns `(0,1)`, `[3,3], 6` returns `(0,1)`. First describe a nested-loop solution, then improve it with a dictionary. Record time/space complexity and test no-match/duplicate cases.

**Checkpoint:** explain the invariant and reproduce the improved solution the next day.

## Session 6 — Validate prior AI learning

Pick one ML notebook and explain split strategy, leakage risks, chosen metric, and how inference receives validated inputs. For LLMs, demonstrate a minimal retrieval example with source IDs and an unanswerable question. If you have that implementation elsewhere, link it; otherwise build a small version. Explain token limits, embeddings, and why retrieved text must not authorize tool actions.

**Checkpoint:** record evidence rather than repeating a full ML/LLM course. List only the gaps that need revisiting.

## Session 7 — Review and plan

Write a one-page note using the template. Demo the API, rerun tests, and redo one DSA problem from memory. Update the progress tracker with working file paths. Schedule reviews after 7 and 30 days. Continue to phase 1 if the baseline is comfortable; spend another week on weak spots if needed.
