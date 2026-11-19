# Subqueries CTEs and Set Operations

[Back to SQL](../README.md) · [SQL example](examples.sql)

## In simple words

Subqueries and CTEs compose query logic; set operations combine result sets.

## What to understand

Compare scalar and correlated subqueries, readable CTE stages, UNION versus UNION ALL, and intersection/difference.

## Think through this example

A CTE can define daily totals before a later calculation without implying stored persistent data.

## Common mistake

Assuming every CTE is always materialized in every database.

## Practice yourself

Plan a multi-stage summary query and explain whether duplicates should remain.

Run the [SQL example](examples.sql) after loading the shared [sample data](../setup.sql).

## Recall check

- Explain the concept without reading the note.
- Explain why it fits the example and when you would choose something else.
- Describe one boundary or failure case before implementing.

## Reference

[Roadmap reference; explanations and exercises are original study notes](https://algomaster.io/roadmaps/sql). Consult the linked material for the full lesson; these are concise original notes, not copied course content. References checked on 2026-11-07.
