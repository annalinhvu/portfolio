"""Adds John Woo (id 101) to filmmakers.json with enriched film data."""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'filmmakers.json')

JOHN_WOO = {
  "id": 101,
  "name": "John Woo",
  "nationality": "hong kong",
  "birth_year": 1946,
  "death_year": None,
  "era": "contemporary",
  "tagline": "The poet of the bullet — brotherhood, betrayal, and slow-motion grace",
  "bio": "John Woo grew up in Hong Kong's impoverished Shek Kip Mei district, where cinema was both escape and education. After apprenticing under Chang Cheh, he defined a new genre — Heroic Bloodshed — in which the action film became a vehicle for operatic feeling: loyalty tested to destruction, honor maintained in the face of death, and violence choreographed with the precision and beauty of ballet. His Hong Kong films of 1986–1992 are among the most influential genre works in cinema history, reshaping action filmmaking from Hollywood to Bollywood. His Hollywood period produced genre spectacles of genuine craft before he returned to Asia for the epic Red Cliff.",
  "why": "Woo taught a generation of filmmakers that genre movies could carry the weight of tragedy — that a shoot-out could be as emotionally resonant as any drama, and that male loyalty could be a subject worthy of the grandest cinematic treatment.",
  "notable_films": [
    {
      "title": "A Better Tomorrow",
      "year": 1986,
      "synopsis": "Two brothers — one a Triad counterfeiter, one a rising police officer — find their relationship destroyed by criminal entanglement. The film follows their estrangement and painful attempt at reconciliation while their shared world burns around them.",
      "why_watch": "The film that invented Heroic Bloodshed and launched Chow Yun-fat into stardom. The themes of brotherhood and honor that define all of Woo's best work appear here in their purest, most heartbreaking form.",
      "visual_style": "Woo's signature slow-motion sequences make their first appearance — gunfire and suffering rendered lyrical. The film uses Hong Kong's neon-drenched streets as a backdrop for genuine tragedy.",
      "themes": ["brotherhood", "loyalty vs. the law", "redemption", "sacrifice"],
      "runtime": 95
    },
    {
      "title": "A Better Tomorrow II",
      "year": 1987,
      "synopsis": "A direct continuation introducing the twin brother of the first film's fallen hero, who is drawn out of retirement and into an even more operatic cycle of violence and revenge against the men who destroyed his family.",
      "why_watch": "Less coherent than the original but even more excessive — the final shootout remains one of Hong Kong cinema's most deliriously over-the-top set pieces. Woo in pure maximalist mode.",
      "visual_style": "The slow-motion ballet pushed further — the restaurant sequence and the final mansion assault use multiple cameras and pyrotechnic choreography at a scale that strains credibility in the best possible way.",
      "themes": ["revenge", "the double", "masculinity", "operatic excess"],
      "runtime": 104
    },
    {
      "title": "The Killer",
      "year": 1989,
      "synopsis": "A hitman accidentally blinds a singer during an assignment and takes one final contract to pay for her surgery — only to form an unexpected bond with the police inspector hunting him. A film about two men with the same code on opposite sides of the law.",
      "why_watch": "Woo's most formally perfect film and the pinnacle of Heroic Bloodshed. The partnership between Chow Yun-fat and Danny Lee is one of cinema's great male friendships, forged in gunfire.",
      "visual_style": "The church shootout and the final waterfront battle are landmark sequences — slow-motion carnage that somehow achieves genuine emotional catharsis. The white doves appear for the first time as Woo's visual signature.",
      "themes": ["honor among enemies", "sacrifice", "blindness as metaphor", "the code of the killer"],
      "runtime": 111
    },
    {
      "title": "Bullet in the Head",
      "year": 1990,
      "synopsis": "Three lifelong friends from Hong Kong travel to Saigon at the height of the Vietnam War to make quick money and find themselves trapped in a conflict that tests and ultimately destroys their bond in ways none could have imagined.",
      "why_watch": "Woo's most personal and most brutal film — a direct response to Cimino's The Deer Hunter, and a meditation on how war and greed corrode the loyalty that makes life worth living.",
      "visual_style": "The Vietnam sequences have a documentary urgency unlike anything else in Woo's filmography. The film builds its visual grammar of brotherhood before systematically destroying it — each slow-motion shot carries double weight.",
      "themes": ["war's corruption", "friendship destroyed", "Vietnam", "greed vs. loyalty"],
      "runtime": 136
    },
    {
      "title": "Hard Boiled",
      "year": 1992,
      "synopsis": "A reckless Hong Kong detective and an undercover cop embedded in the Triads team up to bring down a gun-running operation in a film that culminates in a hospital siege of almost incomprehensible scale and duration.",
      "why_watch": "The greatest pure action film ever made. The hospital sequence — shot continuously over two weeks — is cinema's most sustained action set piece, and Chow Yun-fat has never been more charismatic.",
      "visual_style": "The teahouse opening establishes Woo's grammar at maximum refinement. The hospital siege uses a two-and-a-half-minute uncut take that follows Chow and Leung through three floors of carnage — a technical and choreographic miracle.",
      "themes": ["duty", "the undercover cop's identity", "collateral damage", "masculine codes"],
      "runtime": 128
    },
    {
      "title": "Hard Target",
      "year": 1993,
      "synopsis": "A drifter in New Orleans helps a woman searching for her missing father and uncovers a hunting operation in which wealthy clients pay to stalk homeless veterans. Woo's Hollywood debut, visibly compromised but unmistakably his.",
      "why_watch": "Fascinating as a transitional artifact — Woo's signature slow-motion and dual-pistol choreography transplanted into an American genre film with Van Damme. The action sequences are still extraordinary.",
      "visual_style": "Woo's visual style collides with Hollywood's commercial demands — the result is uneven but contains sequences of genuine kinetic beauty, particularly the climactic warehouse chase.",
      "themes": ["the hunted vs. the hunter", "class predation", "the veteran as disposable", "survival"],
      "runtime": 97
    },
    {
      "title": "Broken Arrow",
      "year": 1996,
      "synopsis": "A rogue Air Force pilot steals two nuclear warheads from a stealth bomber and holds them for ransom, while his former partner pursues him across the Utah desert. A slick, cheerful mid-90s action film.",
      "why_watch": "The most purely fun of Woo's Hollywood films — John Travolta enjoying his post-Pulp Fiction comeback as a villain, and Woo staging his set pieces with genuine inventiveness in the American landscape.",
      "visual_style": "Utah's red desert and the interior of B-3 bombers give Woo unusual visual material. The mine sequences and train chase show his instinct for spatial choreography adapted to American scale.",
      "themes": ["betrayal", "nuclear threat", "the partner turned enemy", "spectacle"],
      "runtime": 108
    },
    {
      "title": "Face/Off",
      "year": 1997,
      "synopsis": "An FBI agent undergoes experimental face-transplant surgery to impersonate a comatose terrorist — who then wakes, forces the same surgery, and assumes his pursuer's life. A baroque action film about identity, family, and the self.",
      "why_watch": "The peak of Woo's Hollywood career — a film so committed to its absurd premise that it achieves genuine emotional weight. Cage and Travolta playing each other is one of action cinema's great double acts.",
      "visual_style": "Woo's full arsenal deployed at maximum Hollywood budget — boat chases, church shootouts, the signature slow-motion and doves. The film is deliberately operatic, treating its own excess as the subject.",
      "themes": ["identity and the self", "fatherhood", "the enemy's mirror", "transformation"],
      "runtime": 138
    },
    {
      "title": "Mission: Impossible 2",
      "year": 2000,
      "synopsis": "Ethan Hunt is assigned to recover a stolen engineered virus and the antidote from a rogue IMF agent, with the help of a thief he has been tasked to recruit and has fallen in love with.",
      "why_watch": "The most divisive entry in the franchise and Woo's most personal Hollywood film — a Hitchcockian thriller in action film clothing, with slow-motion motorcycle duels and a genuine interest in romantic sacrifice.",
      "visual_style": "Woo saturates the film with his visual tics — doves, masks, dual pistols, slow-motion — at a scale only a Mission: Impossible budget could support. The Spanish mountain opening is pure Woo poetry.",
      "themes": ["trust", "sacrifice", "the thief's code", "romantic obsession"],
      "runtime": 123
    },
    {
      "title": "Red Cliff",
      "year": 2008,
      "synopsis": "The Battle of Red Cliffs in 208 AD — in which the allied forces of Liu Bei and Sun Quan defeated Cao Cao's vastly larger army — rendered as a two-part epic of strategy, loyalty, and mass warfare.",
      "why_watch": "Woo returning to Asia with the largest budget in Chinese film history to make a war epic that reconnects his themes of brotherhood and sacrifice to their historical roots. The battle sequences are staggering.",
      "visual_style": "Wide-format cinematography by Zhang Li that gives the Yangtze River and the massed armies an epic scale last seen in Kurosawa. Woo's slow-motion and choreographic instincts adapted to ancient warfare.",
      "themes": ["strategy and intelligence", "coalition under pressure", "sacrifice", "ancient China"],
      "runtime": 148
    }
  ],
  "style_tags": [
    "heroic bloodshed",
    "action",
    "hong kong cinema"
  ],
  "start_with": {
    "film": "The Killer",
    "year": 1989,
    "note": "The purest expression of everything Woo stands for — honor, sacrifice, and the tragic friendship between men who should be enemies. The white doves say everything."
  },
  "key_themes": [
    "brotherhood and betrayal",
    "honor in violence",
    "sacrifice",
    "loyalty tested to destruction"
  ],
  "quote": "I always put my heart into everything I make. I want the audience to feel something — not just excitement, but emotion."
}

def main():
    with open(DATA_FILE) as f:
        data = json.load(f)

    if any(d['id'] == 101 for d in data):
        print("John Woo already exists — skipping.")
        return

    data.append(JOHN_WOO)

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✓ Added John Woo (id 101) with {len(JOHN_WOO['notable_films'])} films.")

if __name__ == '__main__':
    main()
