#!/usr/bin/env python3
"""Fetch Wikipedia portrait URLs for filmmakers and actors, write back to JSON."""

import json
import urllib.request
import urllib.parse
import time

WIKI_API = "https://en.wikipedia.org/w/api.php"

# Manual overrides for names that differ from Wikipedia page titles
OVERRIDES = {
    "Toshiro Mifune": "Toshirō Mifune",
    "Yasujiro Ozu": "Yasujirō Ozu",
    "Akira Kurosawa": "Akira Kurosawa",
    "Kenji Mizoguchi": "Kenji Mizoguchi",
    "Mikio Naruse": "Mikio Naruse",
    "Nagisa Oshima": "Nagisa Ōshima",
    "Shohei Imamura": "Shōhei Imamura",
    "Jean-Luc Godard": "Jean-Luc Godard",
    "Bela Tarr": "Béla Tarr",
    "Jia Zhangke": "Jia Zhangke",
    "Hou Hsiao-hsien": "Hou Hsiao-hsien",
    "Edward Yang": "Edward Yang",
    "Tsai Ming-liang": "Tsai Ming-liang",
    "Apichatpong Weerasethakul": "Apichatpong Weerasethakul",
    "Carlos Reygadas": "Carlos Reygadas",
    "Lucrecia Martel": "Lucrecia Martel",
    "Ritwik Ghatak": "Ritwik Ghatak",
    "Satyajit Ray": "Satyajit Ray",
    "Ousmane Sembène": "Ousmane Sembène",
    "Djibril Diop Mambéty": "Djibril Diop Mambéty",
    "Abbas Kiarostami": "Abbas Kiarostami",
    "Jafar Panahi": "Jafar Panahi",
    "Tony Leung Chiu-wai": "Tony Leung Chiu-wai",
    "Jean-Paul Belmondo": "Jean-Paul Belmondo",
    "Sophia Loren": "Sophia Loren",
}

def fetch_wiki_photo(name, size=600):
    wiki_name = OVERRIDES.get(name, name)
    title = wiki_name.replace(" ", "_")
    params = urllib.parse.urlencode({
        "action": "query",
        "titles": title,
        "prop": "pageimages",
        "format": "json",
        "pithumbsize": size,
    })
    url = f"{WIKI_API}?{params}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "portfolio-photo-fetch/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        pages = data["query"]["pages"]
        for pid, page in pages.items():
            if pid == "-1":
                return None
            if "thumbnail" in page:
                return page["thumbnail"]["source"]
    except Exception as e:
        print(f"  ERROR {name}: {e}")
    return None

def enrich(path, label):
    data = json.load(open(path))
    found = 0
    for entry in data:
        name = entry["name"]
        if entry.get("photo_url"):
            print(f"  skip (cached): {name}")
            found += 1
            continue
        url = fetch_wiki_photo(name)
        if url:
            entry["photo_url"] = url
            found += 1
            print(f"  OK  {name}")
        else:
            entry["photo_url"] = None
            print(f"  --  {name} (no photo)")
        time.sleep(0.25)
    json.dump(data, open(path, "w"), indent=2, ensure_ascii=False)
    print(f"\n{label}: {found}/{len(data)} photos found\n")

print("=== Directors ===")
enrich("data/filmmakers.json", "Directors")

print("=== Actors ===")
enrich("data/actors.json", "Actors")
