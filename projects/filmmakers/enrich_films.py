"""
Enriches notable_films for 10 selected directors in filmmakers.json.
Adds: synopsis, why_watch, visual_style, themes (list), runtime (int).
Run: python3 enrich_films.py
"""
import json, os, time
import anthropic

SELECTED_IDS = {1, 5, 7, 8, 12, 22, 26, 55, 57, 8}  # Varda, Akerman, Bergman, WKW, Kurosawa, Park, Lynch, Kubrick, Coppola
SELECTED_IDS = {1, 5, 7, 8, 12, 22, 26, 55, 57, 20}  # + Miyazaki instead of duplicate

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'filmmakers.json')

client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

def enrich_film(director_name: str, film_title: str, film_year: int) -> dict:
    prompt = f"""You are a film critic writing for a personal cinephile portfolio.
For the film "{film_title}" ({film_year}) by {director_name}, return ONLY a JSON object with exactly these fields:
- synopsis: 2-3 sentence description of the film (what it's about, not a spoiler)
- why_watch: 1-2 sentences on what makes it essential or special
- visual_style: 1-2 sentences on the cinematography or visual approach
- themes: array of 3-4 short theme strings (e.g. "memory", "isolation", "female gaze")
- runtime: integer minutes

Return only valid JSON, no markdown, no extra text."""

    resp = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}]
    )
    text = resp.content[0].text.strip()
    return json.loads(text)

def main():
    with open(DATA_FILE) as f:
        data = json.load(f)

    for director in data:
        if director['id'] not in SELECTED_IDS:
            continue
        print(f"\n── {director['name']} ──")
        for film in director['notable_films']:
            if 'synopsis' in film:
                print(f"  skip (already enriched): {film['title']}")
                continue
            print(f"  enriching: {film['title']} ({film['year']})...")
            try:
                enriched = enrich_film(director['name'], film['title'], film['year'])
                film.update(enriched)
                print(f"    ✓ themes: {enriched.get('themes', [])}")
            except Exception as e:
                print(f"    ✗ error: {e}")
            time.sleep(0.3)  # gentle rate limit

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("\n✓ Done — filmmakers.json updated.")

if __name__ == '__main__':
    main()
