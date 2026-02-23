"""Export festival data from SQLite to static JSON with nested deadlines and categories."""

import json
import os

import db
import seed_data

DB_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(DB_DIR, "data")
DB_PATH = os.path.join(DB_DIR, "festivals.db")


def export():
    os.makedirs(DATA_DIR, exist_ok=True)

    # Seed fresh database
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    seed_data.seed(DB_PATH)

    conn = db.get_db(DB_PATH)

    # Fetch all festivals
    rows = db.query(
        conn,
        "SELECT id, name, city, country, website, filmfreeway, description, "
        "focus, tier, event_month, premiere_req, prestige, acceptance, known_for "
        "FROM festivals ORDER BY name",
    )
    festivals = []
    for r in rows:
        f = dict(r)
        fid = f["id"]

        # Nest deadlines
        deadlines = db.query(
            conn,
            "SELECT year, tier, deadline, fee_usd FROM deadlines "
            "WHERE festival_id = ? ORDER BY year, deadline",
            (fid,),
        )
        f["deadlines"] = [dict(d) for d in deadlines]

        # Nest categories
        categories = db.query(
            conn,
            "SELECT name, min_runtime, max_runtime FROM categories "
            "WHERE festival_id = ? ORDER BY name",
            (fid,),
        )
        f["categories"] = [dict(c) for c in categories]

        festivals.append(f)

    conn.close()

    out = os.path.join(DATA_DIR, "festivals.json")
    with open(out, "w") as fp:
        json.dump(festivals, fp, indent=2)
    print(f"Wrote {len(festivals)} festivals to {out}")


if __name__ == "__main__":
    export()
