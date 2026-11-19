-- Run SQL/setup.sql and this file in the same PostgreSQL session.

-- Keep every topic, including topics that have no matching sessions.
SELECT t.topic_id, t.title, COUNT(s.session_id) AS session_count
FROM topics AS t
LEFT JOIN study_sessions AS s ON s.topic_id = t.topic_id
GROUP BY t.topic_id, t.title
ORDER BY t.topic_id;

-- Put right-table conditions in ON when unmatched topics must remain.
SELECT t.topic_id, t.title, s.session_id, s.duration_minutes
FROM topics AS t
LEFT JOIN study_sessions AS s
    ON s.topic_id = t.topic_id
   AND s.duration_minutes >= 25
ORDER BY t.topic_id, s.session_id;

-- Compare with an INNER JOIN, which only returns matching rows.
SELECT t.title, s.session_id
FROM topics AS t
JOIN study_sessions AS s ON s.topic_id = t.topic_id
ORDER BY t.topic_id, s.session_id;
