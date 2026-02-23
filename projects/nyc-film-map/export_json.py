"""Export NYC Film Scene Map data from SQLite to static JSON."""

import json
import os

import db
import seed_data

DB_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(DB_DIR, "data")


def export():
    os.makedirs(DATA_DIR, exist_ok=True)

    # Seed the database first to ensure data is fresh
    seed_data.seed()

    conn = db.get_db()
    rows = db.query(conn, "SELECT * FROM venues ORDER BY category, name")
    venues = [dict(r) for r in rows]
    conn.close()

    out = os.path.join(DATA_DIR, "venues.json")
    with open(out, "w") as f:
        json.dump(venues, f, indent=2)
    print(f"Wrote {len(venues)} venues to {out}")


if __name__ == "__main__":
    export()
