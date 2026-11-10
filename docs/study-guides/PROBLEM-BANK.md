# Practice sequence

Attempt each problem before searching for a solution. After 25–40 focused minutes, take one hint, implement again independently, and record the insight. Do not count copied solutions as completed.

## DSA: twenty patterns

Follow this order; roughly one row/week, stretching dynamic programming and graphs as needed. For every row complete the seed problem, a boundary-case variant, and a delayed re-solve. Then add one unfamiliar transfer problem. Aim for about 60–80 distinct problems plus re-solves, not an arbitrary large streak.

| Pattern | Seed problem | Variant / required edge case |
|---|---|---|
| Arrays/strings | Merge sorted arrays | Empty array, repeated values; state in-place versus new-output contract |
| Hashing | Two-sum | Duplicate values; two distinct indices; no solution |
| Two pointers | Sorted pair sum | Return unique value pairs; avoid duplicate pairs |
| Sliding window | Longest substring without repeats | Empty string; all-identical input |
| Prefix sum | Range-sum queries | Inclusive endpoints; validate indices; extend to sum-K subarrays |
| Binary search | First occurrence of target | Missing target and duplicates; explain loop invariant |
| Stack/queue | Balanced brackets | Ignore non-bracket characters; mismatched nesting |
| Monotonic stack | Next greater element to right | Equal elements do not count as greater |
| Linked list | Reverse a singly linked list | Empty/single-node; extend to cycle detection |
| Recursion | Generate all subsets | Explain base case and exponential output size |
| Backtracking | Combinations summing to target | Positive candidates, no duplicate combinations; define reuse rule |
| Trees/BST | Validate a BST | Violations deep below root; define duplicate policy |
| Heap | Top-K frequent words | Deterministic alphabetical tie-break; K exceeds unique words |
| Trie | Prefix autocomplete | Exact match, missing prefix, empty prefix |
| Graph BFS/DFS | Count islands | Empty grid; four-neighbor adjacency; iterative traversal |
| Topological sort | Course prerequisites | Detect cycles and disconnected components |
| Dijkstra | Weighted shortest paths | Non-negative weights, unreachable nodes, zero-weight edges |
| Union find | Connectivity after edge insertions | Repeated edges; path compression and rank/size |
| Greedy | Maximum non-overlapping intervals | Define whether touching endpoints overlap; justify choice |
| Dynamic programming | Minimum coins for amount | Unreachable amount; compare memoization/tabulation; add longest common subsequence |

For each solution write: contract, brute force, invariant/recurrence, improved approach, complexity, tests, and mistake log. Ask whether complexity counts output size and whether input mutation is allowed.

## Backend and SQL labs

1. Design a schema for users, topics, and study sessions; explain primary/foreign keys and constraints.
2. Query total study time by week and topic. Include topics with zero sessions using an outer join.
3. Implement stable pagination with a deterministic tie-breaker; demonstrate inserts between pages.
4. Create a transaction that updates two records; inject failure and prove rollback.
5. Compare a query before/after an index with representative data and EXPLAIN; record read/write tradeoffs.
6. Prevent user B from reading, editing, or deleting user A's session. Test every operation.
7. Implement an idempotent background job; deliver the same message twice and verify one logical result.
8. Cache a summary and define invalidation behavior after edits. Test stale-cache and unavailable-cache behavior.
9. Limit requests and return a useful retry response. Explain per-process versus shared limits.
10. Validate file size/type and store metadata separately from bytes; test failed uploads and cleanup.

## Frontend labs

1. Build an accessible study-session form with labels, validation, and keyboard navigation.
2. Render server data with separate loading, empty, success, and failure states.
3. Prevent duplicate submissions and surface a server-side field error.
4. Add responsive layout and URL-based navigation; reload a detail page directly.
5. Test login → add session → inspect total → logout; verify expired-session handling.

## LLD labs

1. Model a library checkout system using composition; diagram classes and test overdue/duplicate checkout cases.
2. Build interchangeable retrieval strategies and model-provider adapters. Show the simplest implementation first.
3. Add decorators for timing and caching; explain ordering effects.
4. Model ingestion job states with legal transitions; reject an invalid transition.
5. Implement a thread-safe bounded cache; write a concurrent invariant test and compare with a single-owner design.
6. Write tiny examples of factory/abstract factory/builder/prototype, facade/proxy, observer/command, and singleton. For each, name one reason not to use it. Finish with a timed machine-coding implementation of a job scheduler.

## AI reliability labs

1. Validate structured outputs and handle malformed, refused, and incomplete responses explicitly.
2. Compare two chunk sizes on the same evaluation questions. Measure retrieval recall@K and citation correctness separately.
3. Add reranking; retain it only if measured quality improves enough to justify latency/cost.
4. Build a 30-question starter evaluation set: answerable, unanswerable, ambiguous, and malicious-document cases. Separate development examples from held-out evaluation.
5. Implement a bounded tool loop with argument validation, timeouts, retries, step limits, and a budget.
6. Attempt to retrieve another user's documents; verify isolation before and after retrieval.
7. Feed a document saying to ignore system rules and export data. Confirm it cannot authorize a tool action.
8. Connect a small MCP tool and explain its permissions, schema, errors, and trust boundary.
9. Compare a deterministic workflow, a single agent, and a multi-agent design on the same tasks; report completion rate, latency, and cost.
10. Design or run a small LoRA experiment with a baseline, train/validation/test split, resource budget, and stopping rule. Do not train on evaluation examples.

## Operations, HLD, and security labs

1. Containerize API + database, then recreate from documented commands. Keep credentials outside image layers.
2. Run checks in CI and deliberately break a check to confirm it blocks success.
3. Add request IDs, latency/error metrics, a dashboard, and a log query. Redact sensitive fields.
4. Restore a database backup into a new instance and verify known records.
5. Load-test a declared workload; measure p50/p95 latency, throughput, errors, and saturation.
6. Estimate storage and request rates for 1,000 then 100,000 users; label assumptions and compare with measurements.
7. Simulate cache, queue, model-provider, and database failures; record timeout/retry/circuit-breaker behavior.
8. Design replica lag, shard routing, consistent hashing, Bloom filter false positives, and saga compensation examples. Explain CAP and PACELC under explicit failure/latency assumptions.
9. Run a local Kubernetes deployment/Helm lab; compare provisioning with Terraform and configuration with Ansible. Describe blue-green rollback and autoscaling signals.
10. In a local lab, demonstrate SQL injection, XSS, CSRF, and SSRF prevention. Explain why CORS is not authorization. Add dependency scanning, least-privilege policies, and a threat model.
