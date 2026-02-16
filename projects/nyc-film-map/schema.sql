CREATE TABLE IF NOT EXISTS venues (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    category      TEXT NOT NULL,
    address       TEXT,
    neighborhood  TEXT,
    borough       TEXT,
    lat           REAL NOT NULL,
    lng           REAL NOT NULL,
    url           TEXT,
    description   TEXT,
    highlight     TEXT,
    status        TEXT DEFAULT 'active',
    created_at    TEXT DEFAULT (datetime('now'))
);
