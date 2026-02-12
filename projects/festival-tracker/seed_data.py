"""Seed the festival tracker database with curated experimental film festivals."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import db

FESTIVALS = [
    {
        "name": "Ann Arbor Film Festival",
        "city": "Ann Arbor, MI",
        "country": "USA",
        "website": "https://www.aafilmfest.org",
        "filmfreeway": "https://filmfreeway.com/AnnArborFilmFestival",
        "description": "The oldest avant-garde and experimental film festival in North America, running since 1963.",
        "focus": "experimental",
        "tier": "major",
        "event_month": "March",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "early", "deadline": "2024-09-15", "fee_usd": 35.0},
            {"year": 2025, "tier": "regular", "deadline": "2024-11-01", "fee_usd": 50.0},
            {"year": 2025, "tier": "late", "deadline": "2025-01-05", "fee_usd": 65.0},
            {"year": 2026, "tier": "early", "deadline": "2025-09-15", "fee_usd": 40.0},
            {"year": 2026, "tier": "regular", "deadline": "2025-11-01", "fee_usd": 55.0},
        ],
        "categories": [
            {"name": "experimental short", "max_runtime": 30},
            {"name": "experimental feature", "min_runtime": 40},
            {"name": "animation", "max_runtime": 30},
            {"name": "music video", "max_runtime": 15},
        ],
    },
    {
        "name": "International Film Festival Rotterdam (IFFR)",
        "city": "Rotterdam",
        "country": "Netherlands",
        "website": "https://iffr.com",
        "filmfreeway": None,
        "description": "One of the largest audience-driven film festivals in the world, known for championing independent and experimental cinema.",
        "focus": "experimental",
        "tier": "major",
        "event_month": "January-February",
        "premiere_req": "international",
        "deadlines": [
            {"year": 2026, "tier": "regular", "deadline": "2025-09-01", "fee_usd": None},
        ],
        "categories": [
            {"name": "short film", "max_runtime": 60},
            {"name": "feature film", "min_runtime": 60},
            {"name": "mid-length", "min_runtime": 30, "max_runtime": 60},
        ],
    },
    {
        "name": "FIDMarseille",
        "city": "Marseille",
        "country": "France",
        "website": "https://fidmarseille.org",
        "filmfreeway": None,
        "description": "International cinema festival focused on documentary, fiction, and experimental work that pushes boundaries.",
        "focus": "experimental",
        "tier": "major",
        "event_month": "June",
        "premiere_req": "international",
        "deadlines": [
            {"year": 2026, "tier": "regular", "deadline": "2026-02-15", "fee_usd": None},
        ],
        "categories": [
            {"name": "short film", "max_runtime": 60},
            {"name": "feature film", "min_runtime": 60},
        ],
    },
    {
        "name": "New York Film Festival — Projections",
        "city": "New York, NY",
        "country": "USA",
        "website": "https://www.filmlinc.org/nyff/projections/",
        "filmfreeway": None,
        "description": "NYFF's dedicated sidebar for avant-garde and experimental moving image work.",
        "focus": "avant-garde",
        "tier": "major",
        "event_month": "September-October",
        "premiere_req": "north_american",
        "deadlines": [
            {"year": 2025, "tier": "regular", "deadline": "2025-05-01", "fee_usd": None},
            {"year": 2026, "tier": "regular", "deadline": "2026-05-01", "fee_usd": None},
        ],
        "categories": [
            {"name": "experimental short", "max_runtime": 45},
            {"name": "experimental feature", "min_runtime": 45},
        ],
    },
    {
        "name": "Toronto International Film Festival — Wavelengths",
        "city": "Toronto",
        "country": "Canada",
        "website": "https://www.tiff.net",
        "filmfreeway": None,
        "description": "TIFF's programme for avant-garde cinema, named after Michael Snow's landmark 1967 film.",
        "focus": "avant-garde",
        "tier": "major",
        "event_month": "September",
        "premiere_req": "world",
        "deadlines": [
            {"year": 2025, "tier": "regular", "deadline": "2025-04-15", "fee_usd": None},
            {"year": 2026, "tier": "regular", "deadline": "2026-04-15", "fee_usd": None},
        ],
        "categories": [
            {"name": "short film", "max_runtime": 50},
            {"name": "feature film", "min_runtime": 50},
        ],
    },
    {
        "name": "FRACTO",
        "city": "Berlin",
        "country": "Germany",
        "website": "https://www.fracto.org",
        "filmfreeway": "https://filmfreeway.com/FRACTO",
        "description": "Berlin-based experimental film encounter dedicated to artist-run film culture and the materiality of cinema.",
        "focus": "experimental",
        "tier": "mid",
        "event_month": "November",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "regular", "deadline": "2025-07-31", "fee_usd": None},
            {"year": 2026, "tier": "regular", "deadline": "2026-07-31", "fee_usd": None},
        ],
        "categories": [
            {"name": "experimental short", "max_runtime": 30},
            {"name": "experimental feature", "min_runtime": 30},
            {"name": "expanded cinema"},
        ],
    },
    {
        "name": "Lausanne Underground Film & Music Festival",
        "city": "Lausanne",
        "country": "Switzerland",
        "website": "https://www.lfrancais.ch",
        "filmfreeway": "https://filmfreeway.com/LUFF",
        "description": "Festival celebrating underground, experimental, and outsider film alongside extreme and avant-garde music.",
        "focus": "underground",
        "tier": "mid",
        "event_month": "October",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "regular", "deadline": "2025-06-30", "fee_usd": None},
            {"year": 2026, "tier": "regular", "deadline": "2026-06-30", "fee_usd": None},
        ],
        "categories": [
            {"name": "short film", "max_runtime": 30},
            {"name": "feature film", "min_runtime": 40},
            {"name": "music video", "max_runtime": 15},
        ],
    },
    {
        "name": "Videoex",
        "city": "Zurich",
        "country": "Switzerland",
        "website": "https://www.videoex.ch",
        "filmfreeway": "https://filmfreeway.com/Videoex",
        "description": "International festival for experimental film and video art in Zurich.",
        "focus": "experimental",
        "tier": "mid",
        "event_month": "May-June",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "regular", "deadline": "2025-01-31", "fee_usd": None},
            {"year": 2026, "tier": "regular", "deadline": "2026-01-31", "fee_usd": None},
        ],
        "categories": [
            {"name": "experimental short", "max_runtime": 30},
            {"name": "experimental feature", "min_runtime": 30},
            {"name": "video art"},
        ],
    },
    {
        "name": "Onion City Experimental Film Festival",
        "city": "Chicago, IL",
        "country": "USA",
        "website": "https://www.chicagofilmmakers.org/onion-city",
        "filmfreeway": "https://filmfreeway.com/OnionCity",
        "description": "Chicago's premier experimental film festival, presented by Chicago Filmmakers.",
        "focus": "experimental",
        "tier": "mid",
        "event_month": "June",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "early", "deadline": "2025-01-15", "fee_usd": 15.0},
            {"year": 2025, "tier": "regular", "deadline": "2025-03-01", "fee_usd": 25.0},
            {"year": 2025, "tier": "late", "deadline": "2025-04-01", "fee_usd": 35.0},
        ],
        "categories": [
            {"name": "experimental short", "max_runtime": 30},
            {"name": "experimental feature", "min_runtime": 40},
            {"name": "animation", "max_runtime": 15},
        ],
    },
    {
        "name": "VAEFF — Video Art & Experimental Film Festival",
        "city": "New York, NY",
        "country": "USA",
        "website": "https://www.vaeff.org",
        "filmfreeway": "https://filmfreeway.com/VAEFF",
        "description": "New York-based festival showcasing video art and experimental film from around the world.",
        "focus": "experimental",
        "tier": "mid",
        "event_month": "November",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "early", "deadline": "2025-04-15", "fee_usd": 15.0},
            {"year": 2025, "tier": "regular", "deadline": "2025-06-15", "fee_usd": 25.0},
            {"year": 2025, "tier": "late", "deadline": "2025-08-15", "fee_usd": 35.0},
        ],
        "categories": [
            {"name": "experimental short", "max_runtime": 20},
            {"name": "video art", "max_runtime": 20},
            {"name": "experimental feature", "min_runtime": 40},
        ],
    },
    {
        "name": "Bucharest International Experimental Film Festival",
        "city": "Bucharest",
        "country": "Romania",
        "website": "https://www.bieff.ro",
        "filmfreeway": "https://filmfreeway.com/BIEFF",
        "description": "Romania's leading experimental film festival, championing innovative visual language.",
        "focus": "experimental",
        "tier": "mid",
        "event_month": "November",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "regular", "deadline": "2025-07-15", "fee_usd": None},
            {"year": 2026, "tier": "regular", "deadline": "2026-07-15", "fee_usd": None},
        ],
        "categories": [
            {"name": "experimental short", "max_runtime": 30},
            {"name": "experimental feature", "min_runtime": 30},
        ],
    },
    {
        "name": "ARKIPEL Jakarta",
        "city": "Jakarta",
        "country": "Indonesia",
        "website": "https://arkipel.org",
        "filmfreeway": None,
        "description": "Jakarta international documentary and experimental film festival exploring the boundaries of cinema.",
        "focus": "experimental",
        "tier": "mid",
        "event_month": "August",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "regular", "deadline": "2025-04-30", "fee_usd": None},
            {"year": 2026, "tier": "regular", "deadline": "2026-04-30", "fee_usd": None},
        ],
        "categories": [
            {"name": "short film", "max_runtime": 30},
            {"name": "feature film", "min_runtime": 50},
        ],
    },
    {
        "name": "Bogotá Experimental Film Festival (CineAutopsia)",
        "city": "Bogotá",
        "country": "Colombia",
        "website": "https://www.cineautopsia.com",
        "filmfreeway": "https://filmfreeway.com/CineAutopsia",
        "description": "Colombia's experimental film festival celebrating radical and non-narrative cinema.",
        "focus": "experimental",
        "tier": "emerging",
        "event_month": "October",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "regular", "deadline": "2025-06-30", "fee_usd": None},
            {"year": 2026, "tier": "regular", "deadline": "2026-06-30", "fee_usd": None},
        ],
        "categories": [
            {"name": "experimental short", "max_runtime": 30},
            {"name": "experimental feature", "min_runtime": 40},
            {"name": "video art", "max_runtime": 15},
        ],
    },
    {
        "name": "Experiments in Cinema",
        "city": "Albuquerque, NM",
        "country": "USA",
        "website": "https://www.experimentsincinema.org",
        "filmfreeway": "https://filmfreeway.com/ExperimentsInCinema",
        "description": "Albuquerque-based festival devoted to experimental, avant-garde, and no-budget cinema.",
        "focus": "experimental",
        "tier": "emerging",
        "event_month": "April",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "early", "deadline": "2024-10-01", "fee_usd": 10.0},
            {"year": 2025, "tier": "regular", "deadline": "2024-12-01", "fee_usd": 20.0},
            {"year": 2025, "tier": "late", "deadline": "2025-01-15", "fee_usd": 30.0},
            {"year": 2026, "tier": "early", "deadline": "2025-10-01", "fee_usd": 10.0},
            {"year": 2026, "tier": "regular", "deadline": "2025-12-01", "fee_usd": 20.0},
        ],
        "categories": [
            {"name": "experimental short", "max_runtime": 30},
            {"name": "experimental feature", "min_runtime": 40},
            {"name": "animation", "max_runtime": 20},
            {"name": "music video", "max_runtime": 10},
        ],
    },
    {
        "name": "Paris Festival for Different and Experimental Cinema",
        "city": "Paris",
        "country": "France",
        "website": "https://cjcinema.org",
        "filmfreeway": None,
        "description": "Long-running Parisian festival organized by Collectif Jeune Cinéma, France's oldest artist-run film cooperative.",
        "focus": "experimental",
        "tier": "mid",
        "event_month": "October",
        "premiere_req": "none",
        "deadlines": [
            {"year": 2025, "tier": "regular", "deadline": "2025-05-31", "fee_usd": None},
            {"year": 2026, "tier": "regular", "deadline": "2026-05-31", "fee_usd": None},
        ],
        "categories": [
            {"name": "experimental short", "max_runtime": 30},
            {"name": "experimental feature", "min_runtime": 30},
            {"name": "expanded cinema"},
        ],
    },
]


def seed(db_path=None):
    """Seed the database with curated festival data."""
    conn = db.init_db(db_path)

    festival_count = 0
    deadline_count = 0
    category_count = 0

    for entry in FESTIVALS:
        # Separate relational data from festival fields
        deadlines = entry.pop("deadlines", [])
        categories = entry.pop("categories", [])

        fid = db.upsert_festival(conn, entry)
        festival_count += 1

        for dl in deadlines:
            conn.execute(
                "INSERT OR IGNORE INTO deadlines (festival_id, year, tier, deadline, fee_usd) "
                "VALUES (?, ?, ?, ?, ?)",
                (fid, dl["year"], dl["tier"], dl["deadline"], dl.get("fee_usd")),
            )
            deadline_count += 1

        for cat in categories:
            conn.execute(
                "INSERT OR IGNORE INTO categories (festival_id, name, min_runtime, max_runtime) "
                "VALUES (?, ?, ?, ?)",
                (fid, cat["name"], cat.get("min_runtime"), cat.get("max_runtime")),
            )
            category_count += 1

    conn.commit()
    conn.close()

    print(f"Seeded {festival_count} festivals")
    print(f"Seeded {deadline_count} deadlines")
    print(f"Seeded {category_count} categories")


if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(__file__), "festivals.db")
    # Remove existing DB so we start fresh
    if os.path.exists(db_path):
        os.remove(db_path)
    seed(db_path)
