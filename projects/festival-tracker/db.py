"""Database helper for the Film Festival Submission Tracker."""

import os
import sqlite3

SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")
DEFAULT_DB = os.path.join(os.path.dirname(__file__), "festivals.db")


def get_db(path=None):
    """Return a connection with row_factory = sqlite3.Row."""
    path = path or DEFAULT_DB
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(path=None):
    """Run schema.sql to create tables. Returns the connection."""
    conn = get_db(path)
    with open(SCHEMA_PATH) as f:
        conn.executescript(f.read())
    return conn


def query(conn, sql, params=None):
    """Convenience wrapper for SELECT queries. Returns a list of Rows."""
    cur = conn.execute(sql, params or ())
    return cur.fetchall()


def upsert_festival(conn, data):
    """Insert or update a festival dict. Returns the festival id."""
    # Check if a festival with this name already exists
    existing = query(conn, "SELECT id FROM festivals WHERE name = ?", (data["name"],))
    if existing:
        fid = existing[0]["id"]
        fields = []
        values = []
        for key in ("city", "country", "website", "filmfreeway", "description",
                     "focus", "tier", "event_month", "premiere_req",
                     "prestige", "acceptance", "known_for"):
            if key in data:
                fields.append(f"{key} = ?")
                values.append(data[key])
        if fields:
            fields.append("updated_at = datetime('now')")
            values.append(fid)
            conn.execute(
                f"UPDATE festivals SET {', '.join(fields)} WHERE id = ?",
                values,
            )
            conn.commit()
        return fid

    cols = []
    placeholders = []
    values = []
    for key in ("name", "city", "country", "website", "filmfreeway",
                 "description", "focus", "tier", "event_month", "premiere_req",
                 "prestige", "acceptance", "known_for"):
        if key in data:
            cols.append(key)
            placeholders.append("?")
            values.append(data[key])

    cur = conn.execute(
        f"INSERT INTO festivals ({', '.join(cols)}) VALUES ({', '.join(placeholders)})",
        values,
    )
    conn.commit()
    return cur.lastrowid
