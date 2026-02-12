# Film Festival Submission Tracker

A searchable database of experimental film festivals. Data layer built with SQLite and Python.

## Setup

```bash
python seed_data.py
```

This creates `festivals.db` with 15 curated experimental film festivals, their submission deadlines, and accepted categories.

## Usage

```python
import db

conn = db.get_db()

# List all festivals
rows = db.query(conn, "SELECT name, city, country FROM festivals ORDER BY name")
for r in rows:
    print(f"{r['name']} — {r['city']}, {r['country']}")

# Find festivals by tier
majors = db.query(conn, "SELECT name FROM festivals WHERE tier = ?", ("major",))

# Upcoming deadlines
upcoming = db.query(conn, """
    SELECT f.name, d.tier, d.deadline, d.fee_usd
    FROM deadlines d
    JOIN festivals f ON f.id = d.festival_id
    WHERE d.deadline >= date('now')
    ORDER BY d.deadline
""")
```

## Schema

- **festivals** — core info (name, city, country, tier, focus, premiere requirements)
- **deadlines** — submission deadlines per festival per year (with fees)
- **categories** — accepted submission categories (with runtime limits)
