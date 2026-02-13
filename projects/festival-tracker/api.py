"""Film Festival Tracker — FastAPI application."""

from datetime import date

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

import db

app = FastAPI(title="Film Festival Tracker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_conn():
    """Yield a DB connection, closing it after the request."""
    conn = db.get_db()
    try:
        yield conn
    finally:
        conn.close()


@app.get("/festivals")
def list_festivals(
    tier: str | None = None,
    country: str | None = None,
    focus: str | None = None,
    search: str | None = None,
    conn=Depends(get_conn),
):
    clauses = []
    params = []
    if tier:
        clauses.append("tier = ?")
        params.append(tier)
    if country:
        clauses.append("country = ?")
        params.append(country)
    if focus:
        clauses.append("focus = ?")
        params.append(focus)
    if search:
        clauses.append("name LIKE ?")
        params.append(f"%{search}%")

    sql = "SELECT id, name, city, country, website, filmfreeway, description, focus, tier, event_month, premiere_req FROM festivals"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY name"

    rows = db.query(conn, sql, params)
    return [dict(r) for r in rows]


@app.get("/festivals/{festival_id}")
def get_festival(festival_id: int, conn=Depends(get_conn)):
    rows = db.query(
        conn,
        "SELECT id, name, city, country, website, filmfreeway, description, focus, tier, event_month, premiere_req FROM festivals WHERE id = ?",
        (festival_id,),
    )
    if not rows:
        raise HTTPException(status_code=404, detail="Festival not found")

    festival = dict(rows[0])

    deadlines = db.query(
        conn,
        "SELECT year, tier, deadline, fee_usd FROM deadlines WHERE festival_id = ? ORDER BY year, deadline",
        (festival_id,),
    )
    festival["deadlines"] = [dict(d) for d in deadlines]

    categories = db.query(
        conn,
        "SELECT name, min_runtime, max_runtime FROM categories WHERE festival_id = ? ORDER BY name",
        (festival_id,),
    )
    festival["categories"] = [dict(c) for c in categories]

    return festival


@app.get("/deadlines")
def list_deadlines(
    year: int | None = None,
    upcoming: bool = Query(False),
    conn=Depends(get_conn),
):
    clauses = []
    params = []
    if year:
        clauses.append("d.year = ?")
        params.append(year)
    if upcoming:
        clauses.append("d.deadline >= ?")
        params.append(date.today().isoformat())

    sql = (
        "SELECT d.id, d.festival_id, f.name AS festival_name, d.year, d.tier, d.deadline, d.fee_usd "
        "FROM deadlines d JOIN festivals f ON f.id = d.festival_id"
    )
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY d.deadline"

    rows = db.query(conn, sql, params)
    return [dict(r) for r in rows]


@app.get("/categories")
def list_categories(
    festival_id: int | None = None,
    conn=Depends(get_conn),
):
    if festival_id:
        rows = db.query(
            conn,
            "SELECT id, festival_id, name, min_runtime, max_runtime FROM categories WHERE festival_id = ? ORDER BY name",
            (festival_id,),
        )
    else:
        rows = db.query(
            conn,
            "SELECT id, festival_id, name, min_runtime, max_runtime FROM categories ORDER BY name",
        )
    return [dict(r) for r in rows]
