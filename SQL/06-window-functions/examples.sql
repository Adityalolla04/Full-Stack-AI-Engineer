-- Run SQL/setup.sql and this file in the same PostgreSQL session.

SELECT t.user_id, s.session_id, s.started_at, s.duration_minutes,
       ROW_NUMBER() OVER (
           PARTITION BY t.user_id
           ORDER BY s.started_at, s.session_id
       ) AS session_number,
       SUM(COALESCE(s.duration_minutes, 0)) OVER (
           PARTITION BY t.user_id
           ORDER BY s.started_at, s.session_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_minutes,
       LAG(s.duration_minutes) OVER (
           PARTITION BY t.user_id
           ORDER BY s.started_at, s.session_id
       ) AS previous_duration
FROM study_sessions AS s
JOIN topics AS t ON t.topic_id = s.topic_id
ORDER BY t.user_id, s.started_at, s.session_id;

-- RANK gives tied values the same rank; ROW_NUMBER always distinguishes rows.
SELECT t.user_id, s.session_id, s.duration_minutes,
       RANK() OVER (
           PARTITION BY t.user_id
           ORDER BY s.duration_minutes DESC NULLS LAST
       ) AS duration_rank
FROM study_sessions AS s
JOIN topics AS t ON t.topic_id = s.topic_id
ORDER BY t.user_id, duration_rank, s.session_id;
