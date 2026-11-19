-- Run SQL/setup.sql and this file in the same PostgreSQL session.

-- COUNT(*) counts rows; COUNT(duration_minutes) skips NULL durations.
SELECT t.topic_id, t.title,
       COUNT(s.session_id) AS session_count,
       COUNT(s.duration_minutes) AS known_duration_count,
       COALESCE(SUM(s.duration_minutes), 0) AS total_minutes
FROM topics AS t
LEFT JOIN study_sessions AS s ON s.topic_id = t.topic_id
GROUP BY t.topic_id, t.title
HAVING COALESCE(SUM(s.duration_minutes), 0) >= 25
ORDER BY total_minutes DESC, t.topic_id;

-- Filter individual rows before grouping with WHERE.
SELECT (started_at AT TIME ZONE 'UTC')::date AS utc_day,
       COUNT(*) AS session_count,
       SUM(duration_minutes) AS total_minutes
FROM study_sessions
WHERE started_at >= '2026-10-01 00:00:00+00'
GROUP BY (started_at AT TIME ZONE 'UTC')::date
ORDER BY utc_day;
