-- PostgreSQL sample data shared by the concept scripts.
-- All objects are temporary and disappear when the psql session ends.

CREATE TEMP TABLE users (
    user_id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    display_name TEXT NOT NULL
);

CREATE TEMP TABLE topics (
    topic_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users (user_id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    created_at DATE NOT NULL
);

CREATE TEMP TABLE study_sessions (
    session_id INTEGER PRIMARY KEY,
    topic_id INTEGER NOT NULL REFERENCES topics (topic_id) ON DELETE CASCADE,
    started_at TIMESTAMPTZ NOT NULL,
    duration_minutes INTEGER CHECK (duration_minutes IS NULL OR duration_minutes >= 0),
    completed_at TIMESTAMPTZ,
    notes TEXT
);

CREATE TEMP TABLE documents (
    document_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users (user_id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL
);

INSERT INTO users (user_id, email, display_name) VALUES
    (1, 'ava@example.test', 'Ava'),
    (2, 'ben@example.test', 'Ben'),
    (3, 'cy@example.test', 'Cy');

INSERT INTO topics (topic_id, user_id, title, created_at) VALUES
    (101, 1, 'Relational SQL', '2026-10-01'),
    (102, 1, 'Query Planning', '2026-10-02'),
    (201, 2, 'Python', '2026-10-01'),
    (202, 2, 'React', '2026-10-02'),
    (301, 3, 'No sessions yet', '2026-10-03');

INSERT INTO study_sessions
    (session_id, topic_id, started_at, duration_minutes, completed_at, notes)
VALUES
    (1001, 101, '2026-10-01 09:00:00+00', 25, '2026-10-01 09:25:00+00', 'Keys and relations'),
    (1002, 101, '2026-10-01 10:00:00+00', 30, '2026-10-01 10:30:00+00', 'Filtering practice'),
    (1003, 102, '2026-10-02 09:00:00+00', 0, NULL, NULL),
    (2001, 201, '2026-10-02 11:00:00+00', 45, '2026-10-02 11:45:00+00', 'Functions'),
    (2002, 202, '2026-10-03 11:00:00+00', 60, '2026-10-03 12:00:00+00', 'Components');

INSERT INTO documents (document_id, user_id, title, created_at) VALUES
    (501, 1, 'SQL notes', '2026-10-01 08:00:00+00'),
    (502, 1, 'Query checklist', '2026-10-02 08:00:00+00'),
    (503, 2, 'Python notes', '2026-10-02 10:00:00+00');
