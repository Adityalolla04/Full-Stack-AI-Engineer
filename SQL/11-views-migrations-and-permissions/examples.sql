-- Run SQL/setup.sql and this file in the same PostgreSQL session.

-- This DDL affects only the temporary sample table for this connection.
ALTER TABLE topics
    ADD COLUMN IF NOT EXISTS summary TEXT;

COMMENT ON COLUMN topics.summary IS 'Optional short description';

CREATE TEMP VIEW topic_session_summary AS
SELECT t.topic_id, t.user_id, t.title,
       COUNT(s.session_id) AS session_count,
       COALESCE(SUM(s.duration_minutes), 0) AS total_minutes
FROM topics AS t
LEFT JOIN study_sessions AS s ON s.topic_id = t.topic_id
GROUP BY t.topic_id, t.user_id, t.title;

SELECT *
FROM topic_session_summary
ORDER BY user_id, topic_id;

-- In a real migration, apply DDL in a reviewed, versioned migration file.
-- Grant only the required access to a pre-created reporting role, for example:
-- GRANT SELECT ON topic_session_summary TO reporting_role;
