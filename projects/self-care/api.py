"""Only Good Things — Self-Care Activity Catalog API."""

import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

import db


class CompletionIn(BaseModel):
    activity_id: int
    completed_at: str | None = None
    notes: str | None = None

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


@app.get("/completions")
def list_completions(
    activity_id: int | None = None,
    conn=Depends(get_conn),
):
    if activity_id:
        rows = db.query(
            conn,
            "SELECT c.id, c.activity_id, a.name, a.category, c.completed_at, c.notes "
            "FROM completions c JOIN activities a ON a.id = c.activity_id "
            "WHERE c.activity_id = ? ORDER BY c.completed_at DESC",
            (activity_id,),
        )
    else:
        rows = db.query(
            conn,
            "SELECT c.id, c.activity_id, a.name, a.category, c.completed_at, c.notes "
            "FROM completions c JOIN activities a ON a.id = c.activity_id "
            "ORDER BY c.completed_at DESC",
        )
    return [dict(r) for r in rows]


@app.post("/completions")
def add_completion(data: CompletionIn, conn=Depends(get_conn)):
    activity = db.query(conn, "SELECT id FROM activities WHERE id = ?", (data.activity_id,))
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    cur = conn.execute(
        "INSERT INTO completions (activity_id, completed_at, notes) VALUES (?, ?, ?)",
        (data.activity_id, data.completed_at or None, data.notes),
    )
    conn.commit()
    row = db.query(conn, "SELECT * FROM completions WHERE id = ?", (cur.lastrowid,))
    return dict(row[0])


@app.delete("/completions/{completion_id}")
def delete_completion(completion_id: int, conn=Depends(get_conn)):
    rows = db.query(conn, "SELECT id FROM completions WHERE id = ?", (completion_id,))
    if not rows:
        raise HTTPException(status_code=404, detail="Completion not found")
    conn.execute("DELETE FROM completions WHERE id = ?", (completion_id,))
    conn.commit()
    return {"deleted": True}


@app.get("/")
def serve_frontend():
    return FileResponse(
        os.path.join(os.path.dirname(__file__), "index.html"),
        headers={"Cache-Control": "no-cache"},
    )
