-- Run SQL/setup.sql and this file in the same PostgreSQL session.

-- A junction table models a many-to-many relationship.
CREATE TEMP TABLE topic_tags (
    topic_id INTEGER NOT NULL REFERENCES topics (topic_id) ON DELETE CASCADE,
    tag TEXT NOT NULL CHECK (length(trim(tag)) > 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (topic_id, tag)
);

INSERT INTO topic_tags (topic_id, tag) VALUES
    (101, 'database'),
    (101, 'fundamentals'),
    (102, 'performance');

SELECT t.title, tt.tag
FROM topic_tags AS tt
JOIN topics AS t ON t.topic_id = tt.topic_id
ORDER BY t.topic_id, tt.tag;

-- Inspect primary, unique, foreign-key, and check constraints in this session.
SELECT conrelid::regclass AS table_name, conname, contype
FROM pg_constraint
WHERE connamespace = pg_my_temp_schema()
ORDER BY table_name, conname;
