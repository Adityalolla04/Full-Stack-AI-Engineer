-- Run SQL/setup.sql and this file in the same PostgreSQL session.

-- A CTE names an intermediate result; it is not necessarily materialized.
WITH daily_totals AS (
    SELECT (started_at AT TIME ZONE 'UTC')::date AS utc_day,
           SUM(duration_minutes) AS total_minutes
    FROM study_sessions
    GROUP BY (started_at AT TIME ZONE 'UTC')::date
)
SELECT utc_day, total_minutes
FROM daily_totals
WHERE total_minutes >= 25
ORDER BY utc_day;

-- Correlated EXISTS returns users who have at least one session.
SELECT u.user_id, u.display_name
FROM users AS u
WHERE EXISTS (
    SELECT 1
    FROM topics AS t
    JOIN study_sessions AS s ON s.topic_id = t.topic_id
    WHERE t.user_id = u.user_id
)
ORDER BY u.user_id;

-- UNION removes duplicates; UNION ALL keeps them.
SELECT user_id FROM topics WHERE title = 'Relational SQL'
UNION
SELECT user_id FROM topics WHERE title = 'Query Planning'
ORDER BY user_id;
