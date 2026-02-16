"""NYC Film Scene Map — FastAPI application."""

import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

import db

app = FastAPI(title="NYC Film Scene Map")

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


@app.get("/venues")
def list_venues(
    category: str | None = None,
    borough: str | None = None,
    neighborhood: str | None = None,
    status: str | None = None,
    search: str | None = None,
    conn=Depends(get_conn),
):
    clauses = []
    params = []
    if category:
        clauses.append("category = ?")
        params.append(category)
    if borough:
        clauses.append("borough = ?")
        params.append(borough)
    if neighborhood:
        clauses.append("neighborhood = ?")
        params.append(neighborhood)
    if status:
        clauses.append("status = ?")
        params.append(status)
    if search:
        clauses.append("(name LIKE ? OR neighborhood LIKE ? OR description LIKE ?)")
        params.extend([f"%{search}%", f"%{search}%", f"%{search}%"])

    sql = "SELECT * FROM venues"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY category, name"

    rows = db.query(conn, sql, params)
    return [dict(r) for r in rows]


@app.get("/venues/{venue_id}")
def get_venue(venue_id: int, conn=Depends(get_conn)):
    rows = db.query(conn, "SELECT * FROM venues WHERE id = ?", (venue_id,))
    if not rows:
        raise HTTPException(status_code=404, detail="Venue not found")
    return dict(rows[0])


@app.get("/categories")
def list_categories(conn=Depends(get_conn)):
    rows = db.query(
        conn,
        "SELECT category, COUNT(*) as count FROM venues GROUP BY category ORDER BY category",
    )
    return [dict(r) for r in rows]


@app.get("/boroughs")
def list_boroughs(conn=Depends(get_conn)):
    rows = db.query(
        conn,
        "SELECT borough, COUNT(*) as count FROM venues WHERE borough IS NOT NULL GROUP BY borough ORDER BY borough",
    )
    return [dict(r) for r in rows]


@app.get("/neighborhoods")
def list_neighborhoods(conn=Depends(get_conn)):
    rows = db.query(
        conn,
        "SELECT DISTINCT neighborhood FROM venues WHERE neighborhood IS NOT NULL ORDER BY neighborhood",
    )
    return [r["neighborhood"] for r in rows]


@app.get("/")
def serve_frontend():
    return FileResponse(
        os.path.join(os.path.dirname(__file__), "index.html"),
        headers={"Cache-Control": "no-cache"},
    )
