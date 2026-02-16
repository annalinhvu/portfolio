"""Analog Film Stock Database — FastAPI application."""

import os

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import db

app = FastAPI(title="Analog Film Stock Database")

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


@app.get("/stocks")
def list_stocks(
    brand: str | None = None,
    type: str | None = None,
    format: str | None = None,
    process: str | None = None,
    status: str | None = None,
    search: str | None = None,
    conn=Depends(get_conn),
):
    clauses = []
    params = []
    if brand:
        clauses.append("brand = ?")
        params.append(brand)
    if type:
        clauses.append("type = ?")
        params.append(type)
    if format:
        clauses.append("format = ?")
        params.append(format)
    if process:
        clauses.append("process = ?")
        params.append(process)
    if status:
        clauses.append("status = ?")
        params.append(status)
    if search:
        clauses.append("(name LIKE ? OR brand LIKE ? OR best_for LIKE ?)")
        params.extend([f"%{search}%", f"%{search}%", f"%{search}%"])

    sql = "SELECT * FROM stocks"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY brand, name"

    rows = db.query(conn, sql, params)
    return [dict(r) for r in rows]


@app.get("/stocks/{stock_id}")
def get_stock(stock_id: int, conn=Depends(get_conn)):
    rows = db.query(conn, "SELECT * FROM stocks WHERE id = ?", (stock_id,))
    if not rows:
        raise HTTPException(status_code=404, detail="Stock not found")

    stock = dict(rows[0])

    prices = db.query(
        conn,
        """SELECT p.price_usd, p.per_unit, p.in_stock, p.last_checked,
                  v.name AS vendor_name, v.url AS vendor_url, v.country AS vendor_country
           FROM prices p
           JOIN vendors v ON v.id = p.vendor_id
           WHERE p.stock_id = ?
           ORDER BY p.price_usd""",
        (stock_id,),
    )
    stock["prices"] = [dict(p) for p in prices]

    return stock


@app.get("/vendors")
def list_vendors(conn=Depends(get_conn)):
    rows = db.query(conn, "SELECT * FROM vendors ORDER BY name")
    return [dict(r) for r in rows]


@app.get("/labs")
def list_labs(
    country: str | None = None,
    process: str | None = None,
    mail_in: int | None = None,
    conn=Depends(get_conn),
):
    clauses = []
    params = []
    if country:
        clauses.append("l.country = ?")
        params.append(country)
    if mail_in is not None:
        clauses.append("l.mail_in = ?")
        params.append(mail_in)

    if process:
        sql = """SELECT DISTINCT l.* FROM labs l
                 JOIN lab_services ls ON ls.lab_id = l.id"""
        clauses.append("ls.process = ?")
        params.append(process)
    else:
        sql = "SELECT l.* FROM labs l"

    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY l.name"

    rows = db.query(conn, sql, params)
    labs = []
    for r in rows:
        lab = dict(r)
        services = db.query(
            conn,
            "SELECT DISTINCT process FROM lab_services WHERE lab_id = ?",
            (lab["id"],),
        )
        lab["processes"] = [s["process"] for s in services]
        labs.append(lab)
    return labs


@app.get("/labs/{lab_id}")
def get_lab(lab_id: int, conn=Depends(get_conn)):
    rows = db.query(conn, "SELECT * FROM labs WHERE id = ?", (lab_id,))
    if not rows:
        raise HTTPException(status_code=404, detail="Lab not found")

    lab = dict(rows[0])

    services = db.query(
        conn,
        "SELECT * FROM lab_services WHERE lab_id = ? ORDER BY process, format",
        (lab_id,),
    )
    lab["services"] = [dict(s) for s in services]

    return lab


@app.get("/processes")
def list_processes(conn=Depends(get_conn)):
    rows = db.query(conn, "SELECT DISTINCT process FROM stocks WHERE process IS NOT NULL ORDER BY process")
    return [r["process"] for r in rows]


@app.get("/")
def serve_frontend():
    return FileResponse(
        os.path.join(os.path.dirname(__file__), "index.html"),
        headers={"Cache-Control": "no-cache"},
    )
