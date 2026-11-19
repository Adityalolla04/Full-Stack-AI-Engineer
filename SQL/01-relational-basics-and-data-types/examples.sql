-- Run SQL/setup.sql and this file in the same PostgreSQL session.

SELECT user_id, email, display_name
FROM users
ORDER BY user_id;

SELECT session_id, duration_minutes, pg_typeof(duration_minutes) AS duration_type,
       started_at, pg_typeof(started_at) AS timestamp_type
FROM study_sessions
ORDER BY session_id;
