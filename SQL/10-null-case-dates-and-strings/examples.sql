-- Run SQL/setup.sql and this file in the same PostgreSQL session.

SELECT session_id,
       COALESCE(notes, '(no notes recorded)') AS display_notes,
       CASE
           WHEN completed_at IS NULL THEN 'incomplete'
           WHEN duration_minutes = 0 THEN 'completed with zero minutes'
           ELSE 'completed'
       END AS session_status,
       (started_at AT TIME ZONE 'UTC')::date AS utc_day,
       initcap(trim(COALESCE(notes, 'untitled session'))) AS normalized_label
FROM study_sessions
ORDER BY started_at, session_id;

-- NULL comparisons use IS NULL / IS NOT NULL, not = NULL.
SELECT session_id
FROM study_sessions
WHERE completed_at IS NULL
ORDER BY session_id;
