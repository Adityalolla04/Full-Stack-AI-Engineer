# SQL

Read one concept, explain the example, then run its SQL script against the shared temporary sample data.

## Running the examples

The scripts use PostgreSQL. From the repository root, load the setup and one concept script in the same `psql` session. The setup creates only temporary tables, so the sample data disappears when the session ends.

```powershell
psql -X -v ON_ERROR_STOP=1 -f .\SQL\setup.sql -f .\SQL\01-relational-basics-and-data-types\examples.sql
```

Replace the final path with another concept's `examples.sql` file. Each concept README links to its script.

## Concept index

1. [Relational Basics and Data Types](01-relational-basics-and-data-types/README.md)
2. [SELECT Filtering and Ordering](02-select-filtering-and-ordering/README.md)
3. [Aggregations GROUP BY and HAVING](03-aggregations-group-by-and-having/README.md)
4. [Joins](04-joins/README.md)
5. [Subqueries CTEs and Set Operations](05-subqueries-ctes-and-set-operations/README.md)
6. [Window Functions](06-window-functions/README.md)
7. [Keys Constraints and Normalization](07-keys-constraints-and-normalization/README.md)
8. [Transactions Isolation and Locks](08-transactions-isolation-and-locks/README.md)
9. [Indexes and Query Plans](09-indexes-and-query-plans/README.md)
10. [NULL CASE Dates and Strings](10-null-case-dates-and-strings/README.md)
11. [Views Migrations and Permissions](11-views-migrations-and-permissions/README.md)
12. [SQL Practice Case Study](12-sql-practice-case-study/README.md)

## How to study

Start with the README, write a short explanation from memory, then run and modify the SQL example. Revisit after 1, 7, and 30 days. Mark progress only after you can explain and apply the idea.
