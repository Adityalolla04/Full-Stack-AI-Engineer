-- Run SQL/setup.sql and this file in the same PostgreSQL session.

-- The guarded UPDATE makes the capacity check and reservation one atomic write.
BEGIN;

CREATE TEMP TABLE seat_inventory (
    event_id INTEGER PRIMARY KEY,
    capacity INTEGER NOT NULL CHECK (capacity >= 0),
    reserved INTEGER NOT NULL CHECK (reserved >= 0 AND reserved <= capacity)
);

INSERT INTO seat_inventory (event_id, capacity, reserved)
VALUES (1, 2, 1);

UPDATE seat_inventory
SET reserved = reserved + 1
WHERE event_id = 1
  AND reserved < capacity
RETURNING event_id, capacity, reserved;

COMMIT;

SELECT * FROM seat_inventory;

-- For a multi-step workflow, SELECT ... FOR UPDATE can lock the inventory row
-- before checking it. Applications must still handle deadlocks and retries.
