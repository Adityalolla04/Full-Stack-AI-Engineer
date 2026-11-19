-- Run SQL/setup.sql and this file in the same PostgreSQL session.

-- Recent sessions for one user. The session ID makes ties deterministic.
SELECT s.session_id, t.title AS topic, s.started_at, s.duration_minutes
FROM study_sessions AS s
JOIN topics AS t ON t.topic_id = s.topic_id
WHERE t.user_id = 1
ORDER BY s.started_at DESC, s.session_id DESC;

-- Long sessions, including a stable order for equal durations.
SELECT session_id, duration_minutes
FROM study_sessions
WHERE duration_minutes >= 25
ORDER BY duration_minutes DESC, session_id;

-- Incomplete sessions: NULL needs IS NULL, not = NULL.
SELECT session_id, topic_id, started_at
FROM study_sessions
WHERE completed_at IS NULL
ORDER BY started_at, session_id;
