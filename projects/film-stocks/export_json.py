"""Export film stock and lab data from SQLite to static JSON."""

import json
import os

import db
import seed_data

DB_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(DB_DIR, "data")
DB_PATH = os.path.join(DB_DIR, "film_stocks.db")


def export():
    os.makedirs(DATA_DIR, exist_ok=True)

    # Seed fresh database
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    seed_data.seed()

    conn = db.get_db(DB_PATH)

    # ── Stocks with embedded prices (vendor info joined in) ──
    stock_rows = db.query(conn, "SELECT * FROM stocks ORDER BY brand, name")
    stocks = []
    for r in stock_rows:
        s = dict(r)
        prices = db.query(
            conn,
            """SELECT p.price_usd, p.per_unit, p.in_stock, p.last_checked,
                      v.name AS vendor_name, v.url AS vendor_url, v.country AS vendor_country
               FROM prices p
               JOIN vendors v ON v.id = p.vendor_id
               WHERE p.stock_id = ?
               ORDER BY p.price_usd""",
            (s["id"],),
        )
        s["prices"] = [dict(p) for p in prices]
        stocks.append(s)

    # ── Labs with embedded services and processes list ──
    lab_rows = db.query(conn, "SELECT * FROM labs ORDER BY name")
    labs = []
    for r in lab_rows:
        lab = dict(r)
        services = db.query(
            conn,
            "SELECT * FROM lab_services WHERE lab_id = ? ORDER BY process, format",
            (lab["id"],),
        )
        lab["services"] = [dict(s) for s in services]

        processes = db.query(
            conn,
            "SELECT DISTINCT process FROM lab_services WHERE lab_id = ?",
            (lab["id"],),
        )
        lab["processes"] = [p["process"] for p in processes]
        labs.append(lab)

    conn.close()

    stocks_path = os.path.join(DATA_DIR, "stocks.json")
    with open(stocks_path, "w") as f:
        json.dump(stocks, f, indent=2)
    print(f"Wrote {len(stocks)} stocks to {stocks_path}")

    labs_path = os.path.join(DATA_DIR, "labs.json")
    with open(labs_path, "w") as f:
        json.dump(labs, f, indent=2)
    print(f"Wrote {len(labs)} labs to {labs_path}")


if __name__ == "__main__":
    export()
