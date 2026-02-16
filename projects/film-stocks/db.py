"""Database helper for the Analog Film Stock Database."""

import os
import sqlite3

SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")
DEFAULT_DB = os.path.join(os.path.dirname(__file__), "film_stocks.db")


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
