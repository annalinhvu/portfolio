-- Film Festival Submission Tracker — Schema

-- Core festival info
CREATE TABLE IF NOT EXISTS festivals (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    city          TEXT,
    country       TEXT,
    website       TEXT,
    filmfreeway   TEXT,
    description   TEXT,
    focus         TEXT,
    tier          TEXT,
    event_month   TEXT,
    premiere_req  TEXT,
    created_at    TEXT DEFAULT (datetime('now')),
    updated_at    TEXT DEFAULT (datetime('now'))
);

-- Deadline tiers per festival per year
CREATE TABLE IF NOT EXISTS deadlines (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    festival_id   INTEGER NOT NULL REFERENCES festivals(id),
    year          INTEGER NOT NULL,
    tier          TEXT NOT NULL,
    deadline      TEXT NOT NULL,
    fee_usd       REAL,
    UNIQUE(festival_id, year, tier)
);

-- Accepted categories per festival
CREATE TABLE IF NOT EXISTS categories (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    festival_id   INTEGER NOT NULL REFERENCES festivals(id),
    name          TEXT NOT NULL,
    min_runtime   INTEGER,
    max_runtime   INTEGER,
    UNIQUE(festival_id, name)
);
