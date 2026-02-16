-- Analog Film Stock Database – schema

-- Film stocks (the core entity)
CREATE TABLE IF NOT EXISTS stocks (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,          -- "Portra 400"
    brand         TEXT NOT NULL,          -- "Kodak"
    type          TEXT NOT NULL,          -- "color_negative" | "bw_negative" | "color_reversal" | "bw_reversal"
    format        TEXT NOT NULL,          -- "35mm" | "120" | "4x5" | "8mm" | "super8"
    iso           INTEGER,               -- 400
    process       TEXT,                   -- "C-41" | "E-6" | "BW" | "ECN-2"
    description   TEXT,
    grain         TEXT,                   -- "fine" | "medium" | "heavy"
    tone          TEXT,                   -- "warm" | "neutral" | "cool"
    saturation    TEXT,                   -- "vivid" | "moderate" | "muted"
    latitude      TEXT,                   -- "wide" | "moderate" | "narrow"
    status        TEXT DEFAULT 'available', -- "available" | "discontinued" | "limited"
    best_for      TEXT,                   -- short tagline
    created_at    TEXT DEFAULT (datetime('now'))
);

-- Vendors (online/physical stores)
CREATE TABLE IF NOT EXISTS vendors (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    url           TEXT,
    country       TEXT,
    ships_intl    INTEGER DEFAULT 1       -- boolean
);

-- Prices (stock x vendor)
CREATE TABLE IF NOT EXISTS prices (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id      INTEGER NOT NULL REFERENCES stocks(id),
    vendor_id     INTEGER NOT NULL REFERENCES vendors(id),
    price_usd     REAL NOT NULL,
    per_unit      TEXT DEFAULT 'roll',    -- "roll" | "pack" | "sheet"
    in_stock      INTEGER DEFAULT 1,      -- boolean
    last_checked  TEXT DEFAULT (datetime('now')),
    UNIQUE(stock_id, vendor_id)
);

-- Labs (development/scanning facilities)
CREATE TABLE IF NOT EXISTS labs (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    city          TEXT,
    country       TEXT,
    url           TEXT,
    turnaround    TEXT,                   -- "1-3 days" | "5-7 days" | "2-3 weeks"
    mail_in       INTEGER DEFAULT 0       -- boolean
);

-- Lab services (what processes/formats each lab supports)
CREATE TABLE IF NOT EXISTS lab_services (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    lab_id        INTEGER NOT NULL REFERENCES labs(id),
    process       TEXT NOT NULL,          -- "C-41" | "E-6" | "BW" | "ECN-2"
    format        TEXT NOT NULL,          -- "35mm" | "120" | "4x5"
    dev_price     REAL,                   -- development price USD
    scan_price    REAL,                   -- scanning price USD
    UNIQUE(lab_id, process, format)
);
