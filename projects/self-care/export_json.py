"""Export self-care activity data from SQLite to static JSON."""

import json
import os

import db
import seed_data

DB_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(DB_DIR, "data")
DB_PATH = os.path.join(DB_DIR, "self_care.db")


def export():
    os.makedirs(DATA_DIR, exist_ok=True)

    # Seed fresh database
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    seed_data.seed(DB_PATH)

    conn = db.get_db(DB_PATH)

    rows = db.query(conn, "SELECT * FROM activities ORDER BY category, name")
    activities = [dict(r) for r in rows]

    conn.close()

    out = os.path.join(DATA_DIR, "activities.json")
    with open(out, "w") as f:
        json.dump(activities, f, indent=2)
    print(f"Wrote {len(activities)} activities to {out}")


if __name__ == "__main__":
    export()
