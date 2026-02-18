-- Only Good Things — Self-Care Activity Catalog Schema

CREATE TABLE IF NOT EXISTS activities (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    category      TEXT NOT NULL,
    description   TEXT,
    tagline       TEXT,
    duration_min  INTEGER,
    difficulty    TEXT DEFAULT 'easy',
    season        TEXT DEFAULT 'all',
    setting       TEXT DEFAULT 'indoor',
    supplies      TEXT,
    instructions  TEXT,
    benefit       TEXT,
    moon_phase    TEXT DEFAULT 'any',
    created_at    TEXT DEFAULT (datetime('now')),
    UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS completions (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    activity_id   INTEGER NOT NULL REFERENCES activities(id),
    completed_at  TEXT NOT NULL DEFAULT (date('now')),
    notes         TEXT,
    created_at    TEXT DEFAULT (datetime('now'))
);
