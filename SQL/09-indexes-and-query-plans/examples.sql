-- Run SQL/setup.sql and this file in the same PostgreSQL session.

CREATE INDEX idx_study_sessions_topic_started
    ON study_sessions (topic_id, started_at DESC);

-- A sequential scan may still be cheaper for this tiny sample dataset.
EXPLAIN (ANALYZE, BUFFERS)
SELECT session_id, started_at, duration_minutes
FROM study_sessions
WHERE topic_id = 101
ORDER BY started_at DESC;
