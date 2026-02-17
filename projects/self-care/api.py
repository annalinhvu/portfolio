"""Only Good Things — Self-Care Activity Catalog API."""

import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

import db

app = FastAPI(title="Only Good Things")

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


@app.get("/activities")
def list_activities(
    category: str | None = None,
    season: str | None = None,
    setting: str | None = None,
    difficulty: str | None = None,
    benefit: str | None = None,
    moon_phase: str | None = None,
    search: str | None = None,
    conn=Depends(get_conn),
):
    clauses = []
    params = []
    if category:
        clauses.append("category = ?")
        params.append(category)
    if season:
        clauses.append("(season = ? OR season = 'all')")
        params.append(season)
    if setting:
        clauses.append("(setting = ? OR setting = 'either')")
        params.append(setting)
    if difficulty:
        clauses.append("difficulty = ?")
        params.append(difficulty)
    if benefit:
        clauses.append("benefit = ?")
        params.append(benefit)
    if moon_phase:
        clauses.append("(moon_phase = ? OR moon_phase = 'any')")
        params.append(moon_phase)
    if search:
        clauses.append("(name LIKE ? OR description LIKE ? OR tagline LIKE ?)")
        params.extend([f"%{search}%", f"%{search}%", f"%{search}%"])

    sql = "SELECT * FROM activities"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY category, name"

    rows = db.query(conn, sql, params)
    return [dict(r) for r in rows]


@app.get("/activities/{activity_id}")
def get_activity(activity_id: int, conn=Depends(get_conn)):
    rows = db.query(conn, "SELECT * FROM activities WHERE id = ?", (activity_id,))
    if not rows:
        raise HTTPException(status_code=404, detail="Activity not found")
    return dict(rows[0])


@app.get("/categories")
def list_categories(conn=Depends(get_conn)):
    rows = db.query(
        conn,
        "SELECT category, COUNT(*) as count FROM activities GROUP BY category ORDER BY category",
    )
    return [dict(r) for r in rows]


@app.get("/seasons")
def list_seasons(conn=Depends(get_conn)):
    rows = db.query(
        conn,
        "SELECT season, COUNT(*) as count FROM activities GROUP BY season ORDER BY season",
    )
    return [dict(r) for r in rows]


@app.get("/benefits")
def list_benefits(conn=Depends(get_conn)):
    rows = db.query(
        conn,
        "SELECT benefit, COUNT(*) as count FROM activities GROUP BY benefit ORDER BY benefit",
    )
    return [dict(r) for r in rows]


@app.get("/")
def serve_frontend():
    return FileResponse(
        os.path.join(os.path.dirname(__file__), "index.html"),
        headers={"Cache-Control": "no-cache"},
    )
