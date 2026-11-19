-- Run SQL/setup.sql and this file in the same PostgreSQL session.

-- 1. Preserve users with no sessions in a per-user report.
SELECT u.user_id, u.display_name, COUNT(s.session_id) AS session_count,
       COALESCE(SUM(s.duration_minutes), 0) AS total_minutes
FROM users AS u
LEFT JOIN topics AS t ON t.user_id = u.user_id
LEFT JOIN study_sessions AS s ON s.topic_id = t.topic_id
GROUP BY u.user_id, u.display_name
ORDER BY u.user_id;

-- 2. Find each user's most recent session with a deterministic tie-breaker.
WITH ranked_sessions AS (
    SELECT t.user_id, s.session_id, s.started_at, s.duration_minutes,
           ROW_NUMBER() OVER (
               PARTITION BY t.user_id
               ORDER BY s.started_at DESC, s.session_id DESC
           ) AS position
    FROM topics AS t
    JOIN study_sessions AS s ON s.topic_id = t.topic_id
)
SELECT user_id, session_id, started_at, duration_minutes
FROM ranked_sessions
WHERE position = 1
ORDER BY user_id;

-- 3. Report topics whose total study time exceeds the threshold.
SELECT t.user_id, t.title, SUM(s.duration_minutes) AS total_minutes
FROM topics AS t
JOIN study_sessions AS s ON s.topic_id = t.topic_id
GROUP BY t.user_id, t.title
HAVING SUM(s.duration_minutes) > 25
ORDER BY total_minutes DESC, t.user_id;

-- 4. Show documents for users who have studied at least one topic.
SELECT d.document_id, d.title, u.display_name
FROM documents AS d
JOIN users AS u ON u.user_id = d.user_id
WHERE EXISTS (
    SELECT 1
    FROM topics AS t
    JOIN study_sessions AS s ON s.topic_id = t.topic_id
    WHERE t.user_id = d.user_id
)
ORDER BY d.user_id, d.document_id;

-- 5. Compare this plan with and without the index.
CREATE INDEX idx_case_study_user_started
    ON study_sessions (topic_id, started_at DESC);

EXPLAIN (ANALYZE, BUFFERS)
SELECT session_id, started_at
FROM study_sessions
WHERE topic_id IN (101, 102)
ORDER BY topic_id, started_at DESC;
