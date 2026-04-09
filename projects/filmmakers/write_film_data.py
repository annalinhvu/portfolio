"""Write enriched film data directly into filmmakers.json for 10 selected directors."""
import json, os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'filmmakers.json')

FILM_DATA = {
  # ── Agnès Varda (id 1) ──────────────────────────────────────────────────
  1: {
    "La Pointe Courte": {
      "synopsis": "A couple travels to a small fishing village in southern France, where their strained relationship unfolds in parallel with the lives of the local fishermen and their community. The film weaves two distinct registers — intimate drama and documentary observation — into a single work.",
      "why_watch": "Made before the French New Wave had a name, it practically invented the movement. Varda was 26 and had almost no film training, which is exactly why it feels so free.",
      "visual_style": "Shot on location with a mix of nonprofessional villagers and trained actors, the film has a luminous, textured black-and-white look that feels simultaneously classical and radically modern.",
      "themes": ["memory", "estrangement", "documentary realism", "duality"],
      "runtime": 80
    },
    "Cléo from 5 to 7": {
      "synopsis": "A pop singer wanders Paris for two hours while awaiting results of a medical test that may confirm cancer. The film unfolds in near-real time, tracking her transformation from passive object of the male gaze into someone who sees and feels the world on her own terms.",
      "why_watch": "One of cinema's great portraits of female consciousness — Varda turns the city into a mirror of interiority without ever losing the street-level energy of early-60s Paris.",
      "visual_style": "Gorgeous high-contrast black-and-white cinematography by Jean Rabier, mixing studio setups with genuine handheld location work on Paris streets. Faces are photographed with extraordinary tenderness.",
      "themes": ["female subjectivity", "mortality", "the male gaze", "Paris"],
      "runtime": 90
    },
    "Le Bonheur": {
      "synopsis": "A young carpenter leads a seemingly perfect life with his wife and children — until he falls for another woman and decides he can simply expand his happiness to include both. The film watches this with deceptively cheerful colors as something quietly horrifying unfolds.",
      "why_watch": "Varda's most unsettling film: it presents domestic bliss and moral vacancy in the same sunlit palette, leaving you to decide what you've been watching.",
      "visual_style": "Ravishing Impressionist color — the film is saturated with pinks, yellows, and greens that evoke Renoir paintings. The beauty is the critique.",
      "themes": ["male entitlement", "domestic ideology", "happiness as violence", "color"],
      "runtime": 79
    },
    "Lions Love": {
      "synopsis": "Shot in Los Angeles during the summer of Robert Kennedy's assassination, three members of the avant-garde theater scene — Viva, Jim Rado, Jerry Ragni — live together in a rented Hollywood house while Varda observes, interviews, and occasionally intrudes on their communal existence.",
      "why_watch": "A fascinating document of counterculture and Varda's outsider-insider relationship with American cinema and politics. Loose, funny, and unexpectedly sad.",
      "visual_style": "Casual 16mm verité that catches the California light and the performers' easy charisma. Varda appears on screen herself, blurring documentary and fiction.",
      "themes": ["counterculture", "celebrity", "America", "reflexivity"],
      "runtime": 110
    },
    "One Sings, the Other Doesn't": {
      "synopsis": "Spanning over a decade, the film follows the friendship between two women — one an aspiring singer, one a photographer — as they navigate abortion, motherhood, relationships, and the women's liberation movement of 1970s France.",
      "why_watch": "Varda's most explicitly feminist film is also one of her most joyful. It insists that politics and pleasure, solidarity and song, can coexist.",
      "visual_style": "Bright, open cinematography that moves freely across France and Iran. The musical sequences feel organic rather than theatrical — folk songs as political argument.",
      "themes": ["feminism", "female friendship", "reproductive rights", "time"],
      "runtime": 120
    },
    "Vagabond": {
      "synopsis": "A young woman's frozen body is found in a ditch in rural France. Through interviews with people who encountered her in her final weeks of wandering, the film pieces together the life — and deliberate freedom — of Mona Bergeron.",
      "why_watch": "One of the great films about female autonomy and social judgment. Varda never sentimentalizes Mona but demands the viewer reckon with what her freedom cost her and why society couldn't accommodate it.",
      "visual_style": "Cold, grey winter landscapes in southern France. The handheld camera observes rather than prettifies. Sandrine Bonnaire's physical performance is total — she is always unmistakably present.",
      "themes": ["freedom", "marginality", "social judgment", "female autonomy"],
      "runtime": 105
    },
    "Jacquot de Nantes": {
      "synopsis": "A tribute to her dying husband Jacques Demy, Varda recreates scenes from his childhood in Nantes — his first encounters with cinema, his homemade puppet theater — intercut with footage of the elderly Demy watching his own films.",
      "why_watch": "An act of love that is also a meditation on memory, cinema's origins, and mortality. Demy's joy in filmmaking is completely contagious.",
      "visual_style": "The childhood reconstructions have a warm, handmade quality — deliberate artifice honoring Demy's love of theater and color. The intercuts to the aged Demy are deeply tender.",
      "themes": ["memory", "love", "cinephilia", "mortality"],
      "runtime": 118
    },
    "The Gleaners & I": {
      "synopsis": "Using a small digital camera, Varda travels rural and urban France to document gleaners — those who gather what is left behind after harvests or discarded by society — and reflects on her own practice of collecting images as a form of gleaning.",
      "why_watch": "One of the great essay films: intimate, digressive, politically sharp, and unexpectedly moving. Varda on digital video felt entirely liberated.",
      "visual_style": "Shot handheld on a small DV camera that Varda operated herself. Deliberately rough and immediate — she films her own aging hands, her grey hair, with the same curiosity she brings to everything else.",
      "themes": ["gleaning", "waste", "aging", "documentary ethics"],
      "runtime": 82
    },
    "The Beaches of Agnès": {
      "synopsis": "At eighty, Varda returns to the beaches of her life — Sète, Brussels, Los Angeles, Paris — to reconstruct her personal and artistic history through images, installations, performances, and interviews with friends.",
      "why_watch": "A playful, moving, and entirely unique autobiography. Varda treats her own life as found material to be assembled and examined with the same curiosity she's always brought to others.",
      "visual_style": "A collage of archival footage, new location work, and theatrical reconstructions. Varda stages memories as living tableaux on actual beaches — sand, sea, and cinema merged.",
      "themes": ["autobiography", "memory", "aging", "cinema's possibilities"],
      "runtime": 110
    },
    "Faces Places": {
      "synopsis": "In her late eighties, Varda travels rural France with photographer and muralist JR, photographing ordinary people and pasting their giant portraits onto walls, barns, and train cars. Their unlikely friendship becomes the film's beating heart.",
      "why_watch": "Pure joy and pure cinema. Two artists — eighty years apart — discovering what they share. The final scene is one of the most beautiful and devastating in all of Varda's work.",
      "visual_style": "Handheld and observational, catching the warmth between Varda and JR and the genuine surprise on faces when subjects encounter their own enormous portraits.",
      "themes": ["community", "visibility", "friendship", "art in public space"],
      "runtime": 89
    }
  },

  # ── Chantal Akerman (id 5) ──────────────────────────────────────────────
  5: {
    "Je tu il elle": {
      "synopsis": "A young woman (played by Akerman) spends time alone in a room eating sugar and rearranging furniture, then hitchhikes with a truck driver, then visits a former female lover. The film unfolds in three discrete, almost clinical sections.",
      "why_watch": "Akerman's first major statement — a direct, discomfiting film about the body, desire, and solitude. Nothing is explained; everything is felt.",
      "visual_style": "Long, static takes that observe the body without aestheticizing it. The camera is still, patient, and merciless. Shot in high-contrast black-and-white on a minimal budget.",
      "themes": ["desire", "the body", "isolation", "female sexuality"],
      "runtime": 86
    },
    "Jeanne Dielman, 23 quai du Commerce, 1080 Bruxelles": {
      "synopsis": "Over three days, the film observes a widowed Belgian housewife and part-time sex worker perform her domestic routines in real time — cooking, cleaning, receiving clients — until a barely visible crack in the routine leads to an act of violence.",
      "why_watch": "Possibly the most radical feminist film ever made. By showing housework in uncut real time, Akerman makes visible the labor that cinema always elides — and reveals it as a form of imprisonment.",
      "visual_style": "Rigidly formal: every shot is from an identical middle distance, with the camera slightly below eye level. The static frames make every deviation from routine register as seismic.",
      "themes": ["domestic labor", "female imprisonment", "time", "the body as site of control"],
      "runtime": 202
    },
    "News from Home": {
      "synopsis": "Akerman reads letters from her mother in Belgium while the camera observes New York City — subway stations, street corners, expressways — in long, patient shots. The two registers never meet except in the viewer's mind.",
      "why_watch": "A film about distance, guilt, and the gap between what we feel and what we say. The mother's letters are ordinary; the effect is devastating.",
      "visual_style": "Long static and slow tracking shots of 1970s New York. The city is observed with the same formal patience as Jeanne Dielman's kitchen — mundane space made monumental.",
      "themes": ["mother-daughter relationships", "migration", "absence", "New York"],
      "runtime": 85
    },
    "Les Rendez-vous d'Anna": {
      "synopsis": "A female filmmaker travels across Europe — Cologne, Paris, Brussels — promoting her work, meeting people in hotel rooms and trains, and remaining essentially alone in a crowd. Encounters accumulate without resolving.",
      "why_watch": "Akerman's most autobiographical film — a portrait of the artist as perpetual outsider, moving through a world that doesn't quite fit her.",
      "visual_style": "Long corridor shots and static hotel-room frames. The camera observes Anna at a remove, tracking her movements through anonymous European spaces with minimal camera movement.",
      "themes": ["exile", "female artistry", "solitude", "Europe"],
      "runtime": 127
    },
    "Toute une nuit": {
      "synopsis": "Over a single hot summer night in Brussels, dozens of couples meet, separate, reunite, and part. The film presents an anthology of brief encounters with no explanation, no backstory, and no resolution.",
      "why_watch": "A strange, hypnotic puzzle — Akerman strips narrative down to pure gesture and atmosphere, making the night feel endless and full of yearning.",
      "visual_style": "Night cinematography that catches the humid glow of streetlights and the anxious energy of bodies in motion. Each encounter is framed with spare, deliberate precision.",
      "themes": ["desire", "time", "the city at night", "anonymity"],
      "runtime": 90
    },
    "The Eighties": {
      "synopsis": "A film in two movements: first, rehearsal footage of auditions and script read-throughs for a musical about a young woman's loves; then the musical itself, filmed in a shopping mall. Akerman exposes the machinery of fiction before presenting the fiction.",
      "why_watch": "A playful, Brechtian deconstruction of musical cinema that also works as a pure musical. Akerman shows the seams without destroying the pleasure.",
      "visual_style": "Brightly lit rehearsal footage gives way to the artificial splendor of the mall musical — vivid primary colors and theatrical staging that would please Demy.",
      "themes": ["performance", "fabrication", "cinema's construction", "desire"],
      "runtime": 83
    },
    "Window Shopping": {
      "synopsis": "Set in a Brussels shopping mall, the film follows an interconnected web of romantic longings, infidelities, and missed connections among the mall's workers and visitors in a style that blends Akerman's formalism with musical comedy.",
      "why_watch": "Akerman in a playful mode — using a Demy-esque setting and tone to explore her usual themes of desire and disconnection. Charming and melancholy at once.",
      "visual_style": "The mall's escalators, walkways, and shop fronts become a formal playground. Bright artificial light and elegant camera movements give the film an almost otherworldly shimmer.",
      "themes": ["consumer space", "desire", "entrapment", "comedy"],
      "runtime": 96
    },
    "D'Est": {
      "synopsis": "Akerman travels from Germany through Poland to Moscow just after the fall of the Soviet Union, filming people waiting — at bus stops, in queues, in the cold — with a series of slow lateral tracking shots.",
      "why_watch": "A meditation on history, communism's aftermath, and the human face as archive. The tracking shots accumulate into something that feels like collective memory.",
      "visual_style": "Slow, sustained lateral tracking shots following people through snowy streets and grey interiors. The formal consistency creates a cumulative, almost musical effect.",
      "themes": ["Eastern Europe", "waiting", "history", "collective memory"],
      "runtime": 110
    },
    "La Captive": {
      "synopsis": "Loosely adapted from Proust's 'The Prisoner,' the film follows a young man who obsessively surveils and controls his girlfriend, demanding accounts of her movements while she remains unknowable to him.",
      "why_watch": "Akerman translates Proust's jealousy into pure cinema — a film about the impossibility of possessing another person, and the violence of trying.",
      "visual_style": "Cool, glassy cinematography by Sabine Lancelin. Interior spaces feel like beautiful prisons; the Seine at night becomes a site of dread and longing.",
      "themes": ["obsession", "control", "unknowability", "Proust"],
      "runtime": 118
    },
    "No Home Movie": {
      "synopsis": "Akerman films her elderly mother in her Brussels apartment — their conversations, silences, her mother's daily life — in what became, unknowingly, a document of the final months before her mother's death.",
      "why_watch": "Akerman's most personal film and her last. The long static shots of her mother's apartment take on unbearable weight in retrospect. Grief filmed before grief arrived.",
      "visual_style": "Raw, domestic digital video. Deliberately unbeautiful — the camera sometimes placed outside a window, shooting through glass. The roughness feels like honesty.",
      "themes": ["mother and daughter", "memory", "loss", "the Holocaust's long shadow"],
      "runtime": 115
    }
  },

  # ── Ingmar Bergman (id 7) ───────────────────────────────────────────────
  7: {
    "Sawdust and Tinsel": {
      "synopsis": "The aging director of a traveling circus returns to a town where his wife lives, hoping for reconciliation, while his young mistress is humiliated by a soldier. A story of pride, shame, and the cruelty of desire.",
      "why_watch": "Early Bergman at his most raw — the famous dawn prologue with the clown Frost carrying his wife from the sea is one of cinema's great sequences.",
      "visual_style": "Sven Nykvist and Hilding Bladh's cinematography uses harsh contrasts and expressionist compositions. The circus world is both squalid and dreamlike.",
      "themes": ["humiliation", "desire", "pride", "performance"],
      "runtime": 92
    },
    "Smiles of a Summer Night": {
      "synopsis": "Four couples — entangled in desire, jealousy, and mismatched affections — gather at a country estate for a summer weekend. The film is a sophisticated romantic comedy in which everyone eventually ends up with the right person, or the wrong one.",
      "why_watch": "The most purely pleasurable film Bergman ever made — witty, sensual, and perfectly timed. The basis for Sondheim's 'A Little Night Music.'",
      "visual_style": "Luminous summer cinematography — the long Swedish twilight captured by Gunnar Fischer with a warmth unusual for Bergman. Elegant compositions and a light touch throughout.",
      "themes": ["desire", "class", "romantic comedy", "summer"],
      "runtime": 108
    },
    "The Seventh Seal": {
      "synopsis": "A medieval knight returning from the Crusades encounters Death personified on a Swedish beach and challenges him to a chess game, buying time to find meaning before he dies. A philosophical allegory about faith, doubt, and mortality.",
      "why_watch": "Bergman's most iconic film — the chess match with Death is one of cinema's defining images. But beneath the symbolism is a genuinely anguished inquiry into whether God exists.",
      "visual_style": "Gunnar Fischer's stark black-and-white photography — bold graphic compositions that flatten space into allegorical tableaux. The silhouetted figures against sky remain unforgettable.",
      "themes": ["death", "faith", "doubt", "medieval allegory"],
      "runtime": 96
    },
    "Wild Strawberries": {
      "synopsis": "An elderly professor drives to receive an honorary degree, accompanied by his daughter-in-law. Along the way, dreams and memories force him to confront a life of emotional coldness and missed connection.",
      "why_watch": "Bergman's most humane film — a gentle masterpiece about regret and the possibility of grace in old age. Victor Sjöström's performance is irreplaceable.",
      "visual_style": "Fischer's cinematography moves between crisp road-movie daylight and the soft, dissolving light of memory and dream. The flashback sequences have an uncanny stillness.",
      "themes": ["regret", "aging", "emotional isolation", "memory"],
      "runtime": 91
    },
    "Through a Glass Darkly": {
      "synopsis": "On a remote island, a young woman recently released from a psychiatric hospital experiences what she believes are visions of God — while her father, husband, and younger brother watch helplessly as she descends.",
      "why_watch": "The first film in Bergman's 'silence of God' trilogy, and still the most devastating. A chamber drama of extraordinary emotional precision.",
      "visual_style": "Sven Nykvist's breakthrough collaboration with Bergman — stark island light, close close-ups on faces, and a visual austerity that matches the theme.",
      "themes": ["mental illness", "God's silence", "family", "isolation"],
      "runtime": 89
    },
    "Winter Light": {
      "synopsis": "A country pastor who has lost his faith struggles through a single Sunday — unable to comfort a suicidal parishioner, unable to love his devoted mistress, unable to find God in the cold Swedish light.",
      "why_watch": "Bergman's most uncompromisingly bleak film — and perhaps his most honest. The scene in which the pastor reads a letter in real time is one of the bravest moments in cinema.",
      "visual_style": "Nykvist's most austere work: cold grey light, empty churches, bare trees. The film refuses beauty almost entirely, matching the spiritual emptiness of its subject.",
      "themes": ["faith's absence", "duty", "loneliness", "grace"],
      "runtime": 81
    },
    "Persona": {
      "synopsis": "An actress who suddenly stops speaking is placed in the care of a young nurse at a remote island cottage. As time passes, their identities begin to blur, merge, and exchange in ways that destabilize both character and narrative.",
      "why_watch": "The most radical film Bergman ever made — a deconstruction of cinema itself that is also a psychological horror story, a feminist double study, and something that resists all description.",
      "visual_style": "Nykvist's photography is devastatingly precise: two faces filmed in extreme close-up, merged into a single composite image in the film's most famous shot. Cinema reflecting on its own face.",
      "themes": ["identity", "silence", "the double", "cinema's illusion"],
      "runtime": 83
    },
    "Cries and Whispers": {
      "synopsis": "Three sisters and a devoted servant gather in a country house as one of the sisters dies slowly of cancer. The film moves between present agony and memories that reveal the emotional distances the women have constructed between themselves.",
      "why_watch": "Bergman at his most operatic and his most visceral. The red interiors and Harriet Andersson's performance are shattering in a way that bypasses analysis.",
      "visual_style": "Sven Nykvist's crimson cinematography — walls, floors, and costumes soaked in red — creates an atmosphere of bleeding, interior pain made visible. Faces emerge from darkness.",
      "themes": ["death", "sisterhood", "emotional repression", "the body"],
      "runtime": 91
    },
    "Scenes from a Marriage": {
      "synopsis": "Over several years, Marianne and Johan — a seemingly happy married couple — divorce, have affairs, remarry others, and continue to be entangled in a relationship that neither can escape or fully inhabit.",
      "why_watch": "The definitive film about marriage and its discontents. Originally a six-hour television miniseries, it is simply the most honest account of long-term partnership in cinema.",
      "visual_style": "Intimate close-ups and a television-influenced visual style that feels domestic and exposed. The camera rarely leaves faces — Ullmann and Josephson are given almost unbearable space.",
      "themes": ["marriage", "divorce", "love's endurance", "self-deception"],
      "runtime": 169
    },
    "Autumn Sonata": {
      "synopsis": "A concert pianist visits her daughter in Norway after years of absence. Over one night, accumulated grievances, unspoken wounds, and the costs of one woman's artistic ambition are laid bare.",
      "why_watch": "Ingrid Bergman and Liv Ullmann. Two filmmakers' greatest actors, given one night to excavate a lifetime. The film is a duel of extraordinary technique and feeling.",
      "visual_style": "Nykvist's intimate close-ups create an almost unbearable proximity. The film is visually simple — a house, two faces, autumn light — and emotionally overwhelming.",
      "themes": ["mothers and daughters", "artistic ambition", "guilt", "love and damage"],
      "runtime": 99
    },
    "Fanny and Alexander": {
      "synopsis": "Seen through the eyes of young Alexander, the film follows a prosperous Swedish theatrical family through the late nineteenth century — Christmas celebrations, a remarriage to a cold bishop, and eventual escape through imagination and art.",
      "why_watch": "Bergman's farewell to cinema: vast, generous, and full of the joy and terror of childhood. A summation of everything he believed about art, imagination, and the darkness that makes light necessary.",
      "visual_style": "Sven Nykvist's most sumptuous work — candlelit interiors of extraordinary warmth giving way to the cold geometries of the bishop's house. The film lives in color and shadow.",
      "themes": ["childhood imagination", "art vs. religion", "family", "Sweden"],
      "runtime": 188
    }
  },

  # ── Wong Kar-wai (id 8) ─────────────────────────────────────────────────
  8: {
    "As Tears Go By": {
      "synopsis": "A small-time Triad enforcer in Hong Kong tries to look after his reckless younger brother while falling for his ailing cousin. The film borrows the grammar of Scorsese's street films and rewrites it in neon.",
      "why_watch": "Wong Kar-wai's debut already shows his obsessions — longing, loyalty, time running out. The Cantopop soundtrack and Andrew Lau's cinematography are pure early Hong Kong cinema.",
      "visual_style": "Vivid Hong Kong night streets, rain-slicked and neon-drenched. Step-printed slow motion during the action sequences makes violence feel both beautiful and tragic.",
      "themes": ["loyalty", "brotherhood", "fate", "Hong Kong underworld"],
      "runtime": 102
    },
    "Days of Being Wild": {
      "synopsis": "Set in 1960s Hong Kong, a restless young man pursues women without being able to love them, searching for his birth mother in the Philippines while those around him wait for someone who will never return.",
      "why_watch": "The film that established Wong Kar-wai's style — the unreliable memory of love, the poetic use of pop music, the crushing weight of minutes. Leslie Cheung is magnetic.",
      "visual_style": "Christopher Doyle's cinematography captures the languid, sticky heat of 1960s Hong Kong in amber tones. The famous one-minute scene is here.",
      "themes": ["rootlessness", "longing", "memory", "identity"],
      "runtime": 94
    },
    "Ashes of Time": {
      "synopsis": "Set in a mythical ancient China, a swordsman-for-hire lives in the desert at the edge of the world, taking contracts for those who need killing done, while memories of loves lost circle him like the seasons.",
      "why_watch": "The least accessible and most poetic of Wong's films — a wuxia film that barely contains its own disinterest in plot. A film about forgetting as survival.",
      "visual_style": "Christopher Doyle at his most abstract — blazing desert light, whip-pan action sequences, and faces emerging from shadow in extreme close-up. Deliberately disorienting.",
      "themes": ["memory", "forgetting", "solitude", "love's impossibility"],
      "runtime": 93
    },
    "Chungking Express": {
      "synopsis": "Two parallel love stories set in Hong Kong's Chungking Mansions: a lovelorn cop falls for a mysterious drug smuggler; another cop falls for a cheerful snack bar worker who has already fallen for him.",
      "why_watch": "Wong Kar-wai's most exhilarating film — alive with the energy of a city in transition, the joy of being young and confused, and one of cinema's most irresistible screen presences in Faye Wong.",
      "visual_style": "Doyle's step-printing creates streams of motion blur in the city crowds. The Chungking Mansions sequences feel urgent and vertiginous; the second story opens into warm California-dreaming color.",
      "themes": ["urban loneliness", "missed connection", "time", "Hong Kong identity"],
      "runtime": 102
    },
    "Fallen Angels": {
      "synopsis": "A hitman and his female partner who never meet; a mute ex-con who breaks into businesses at night; a woman hung up on a man who's forgotten her. Lives orbit each other in nighttime Hong Kong without touching.",
      "why_watch": "Wong Kar-wai's most formally extreme film — shot on wide-angle lenses that distort space, cut fast, and deliberately refuse the romantic coherence of Chungking Express.",
      "visual_style": "Doyle's widest lenses and most aggressive framing — claustrophobic spaces made hallucinatory. The film is shot almost entirely at night in the neon corridors of Hong Kong.",
      "themes": ["solitude", "violence", "longing", "fragmentation"],
      "runtime": 96
    },
    "Happy Together": {
      "synopsis": "Two gay Hong Kong men — volatile and tender in equal measure — travel to Buenos Aires and spend the film breaking up, getting back together, and ultimately separating in ways that might be final.",
      "why_watch": "Wong Kar-wai's most explicitly political and most emotionally direct film — a love story about two people who cannot be together and cannot be apart, filmed in Argentina at the moment of Hong Kong's handover.",
      "visual_style": "Doyle shoots in black-and-white and vivid color, switching registers to track emotional temperature. The Buenos Aires tango bars and waterfalls are filmed with saturated, bruised color.",
      "themes": ["same-sex love", "exile", "Hong Kong 1997", "turbulent attachment"],
      "runtime": 96
    },
    "In the Mood for Love": {
      "synopsis": "Two neighbors in 1962 Hong Kong gradually realize their spouses are having an affair with each other. In their shared understanding of betrayal, they develop a tender, restrained love that they choose never to consummate.",
      "why_watch": "Perhaps the most beautiful film about unexpressed love ever made. Every detail — the narrow staircase, the cheongsam dresses, Shigeru Umebayashi's score — conspires toward heartbreak.",
      "visual_style": "Christopher Doyle and Mark Lee Ping-bin's cinematography is among cinema's most gorgeous — slow motion in the narrow hallway, warm amber interiors, the discipline of never showing the adulterous spouses' faces.",
      "themes": ["restrained desire", "nostalgia", "betrayal", "1960s Hong Kong"],
      "runtime": 98
    },
    "2046": {
      "synopsis": "A writer living in Hong Kong in the 1960s has a series of relationships with women he cannot love fully, while writing a science-fiction story about a train to a place called 2046 where nothing ever changes.",
      "why_watch": "A more melancholy companion to In the Mood for Love — the same world, five years later, through the eyes of someone who chose freedom over love and finds it hollow.",
      "visual_style": "Mark Lee Ping-bin's cinematography continues the amber palette of In the Mood for Love, adding the cool blue of the science-fiction sequences. Sumptuous and deliberately artificial.",
      "themes": ["loss", "memory", "emotional unavailability", "time"],
      "runtime": 129
    },
    "My Blueberry Nights": {
      "synopsis": "A young New Yorker, recovering from a breakup, embarks on a cross-country journey, working in diners and encountering strangers — a grieving cop, a gambling woman, a drifter's daughter — before returning home.",
      "why_watch": "Wong Kar-wai's American film is his most underrated — strange, overripe, and genuinely moving in its outsider's view of American solitude and the blues.",
      "visual_style": "Darius Khondji's cinematography through rain-streaked windows and neon-lit diner glass. The film has a smeared, impressionistic quality — America seen through a romantic foreigner's lens.",
      "themes": ["heartbreak", "the American road", "solitude", "healing"],
      "runtime": 95
    },
    "The Grandmaster": {
      "synopsis": "The life of Ip Man, the legendary Wing Chun master, traced from the 1930s through the Japanese occupation of China to his eventual exile in Hong Kong, alongside his complicated relationship with the daughter of a rival grandmaster.",
      "why_watch": "Less a martial arts film than a meditation on tradition, loss, and the passing of eras. The restrained love story between Ip Man and Gong Er is devastating.",
      "visual_style": "Philippe Le Sourd's cinematography — rain-soaked night fights, slow-motion snowflakes, the texture of silk and steel. Action sequences filmed with the same languorous beauty as Wong's love scenes.",
      "themes": ["martial arts tradition", "lost China", "sacrifice", "longing"],
      "runtime": 130
    }
  },

  # ── Akira Kurosawa (id 12) ──────────────────────────────────────────────
  12: {
    "Sanshiro Sugata": {
      "synopsis": "A young man comes to the city to study jujitsu and instead discovers judo under a wise master. The film traces his development from headstrong youth to disciplined fighter through a series of matches and moral tests.",
      "why_watch": "Kurosawa's debut already shows his command of space, weather, and physical performance. The final duel in a windswept field is electrifying.",
      "visual_style": "Dynamic compositions that use depth of field and weather conditions with a confidence rare in a first film. Kurosawa already stages action as emotional revelation.",
      "themes": ["discipline", "coming of age", "Meiji Japan", "the martial spirit"],
      "runtime": 79
    },
    "Stray Dog": {
      "synopsis": "A young detective's pistol is stolen on a packed Tokyo streetcar. As he hunts for the weapon through the sweltering city's underworld, he begins to see his own reflection in the suspect he pursues.",
      "why_watch": "A film noir masterpiece set in the ruins of postwar Tokyo. The documentary texture of the city scenes is extraordinary, and Mifune and Shimura are perfect together.",
      "visual_style": "The oppressive summer heat is rendered physically — sweat-soaked shirts, crowds packed into trams, the shimmer of Tokyo pavements. Noir shadow in an entirely different climate.",
      "themes": ["postwar Japan", "crime and conscience", "the double", "poverty"],
      "runtime": 122
    },
    "Rashomon": {
      "synopsis": "In feudal Japan, four people give contradictory accounts of a samurai's murder and his wife's rape. Under a ruined gate in the rain, a woodcutter, a commoner, and a priest debate whether any truth can be known.",
      "why_watch": "The film that introduced world cinema to Kurosawa and Japanese cinema alike. It remains the definitive cinematic statement about the subjectivity of truth.",
      "visual_style": "Kazuo Miyagawa's cinematography — sunlight through forest leaves, the camera pointed directly at the sun — was revolutionary. Light becomes a character, shifting with each account.",
      "themes": ["truth and subjectivity", "ego", "honor", "humanity's nature"],
      "runtime": 88
    },
    "Ikiru": {
      "synopsis": "A mid-level Tokyo bureaucrat discovers he has terminal stomach cancer. After years of meaningless paperwork, he spends his final months fighting to build a children's playground in a poor neighborhood.",
      "why_watch": "Kurosawa's most humanist film — about how to find meaning at the last moment. Takashi Shimura's performance is one of cinema's great acts.",
      "visual_style": "The film shifts registers after its midpoint — from intimate close-ups of a dying man to a formal flashback told by his colleagues. The karaoke bar sequence is sublime.",
      "themes": ["mortality", "bureaucracy", "meaning", "legacy"],
      "runtime": 143
    },
    "Seven Samurai": {
      "synopsis": "A poor farming village, terrorized by bandits, hires seven masterless samurai to protect them during the harvest. The film follows the samurai's preparations, the villagers' ambivalence, and the final battle in the rain.",
      "why_watch": "The foundational action film and ensemble character study. Nearly every subsequent action movie — and many Westerns — is a footnote to what Kurosawa achieved here.",
      "visual_style": "Asakazu Nakai's cinematography uses telephoto lenses and multiple cameras for the battle scenes, creating a density and chaos unprecedented in action cinema. The mud, rain, and slow motion are iconic.",
      "themes": ["class", "duty", "sacrifice", "the samurai code's cost"],
      "runtime": 207
    },
    "The Hidden Fortress": {
      "synopsis": "A princess escapes an enemy clan's territory with the help of her loyal general, using two bumbling peasants as unwitting escorts. A rousing adventure film told largely from the perspective of the cowardly, self-interested peasants.",
      "why_watch": "Pure entertainment from a master — and the direct inspiration for Star Wars. The peasants' bickering is funny, the princess is magnificent, and the final battle dazzling.",
      "visual_style": "Kurosawa's first Cinemascope film — the wide frame used for sweeping landscapes and the chaos of crowds. Asakazu Nakai's photography balances spectacle and intimacy.",
      "themes": ["loyalty", "class inversion", "adventure", "female strength"],
      "runtime": 139
    },
    "Yojimbo": {
      "synopsis": "A wandering samurai arrives in a town controlled by two rival gangs and decides to play them against each other for personal gain. A laconic, sardonic genre masterpiece.",
      "why_watch": "The film that invented the antihero samurai and, via Leone's remake, the Man with No Name. Mifune is at his most charismatic — lazy, violent, and deeply amused.",
      "visual_style": "Wide-angle compositions that flatten the town's main street into a stage. Kurosawa uses long lenses for action and close-ups of Mifune's inscrutable face.",
      "themes": ["moral ambiguity", "corruption", "the outsider", "comedy of violence"],
      "runtime": 110
    },
    "High and Low": {
      "synopsis": "A wealthy shoe company executive receives a ransom note from a kidnapper who has taken the wrong child — the chauffeur's son instead of his own. The film splits into a tense thriller and a documentary procedural investigation of Yokohama's underworld.",
      "why_watch": "Kurosawa's greatest genre film and a savage critique of class inequality. The moment the film descends from the hilltop mansion to the slums below is a structural masterstroke.",
      "visual_style": "Nakai's Cinemascope photography uses compositional contrasts between the air-conditioned luxury of the hilltop and the sweaty, neon-lit underworld below.",
      "themes": ["class inequality", "capitalism", "justice", "procedural investigation"],
      "runtime": 143
    },
    "Red Beard": {
      "synopsis": "A young, arrogant doctor is assigned against his will to a free clinic for the poor in Edo-period Japan, where a gruff master physician challenges his ambitions and values through contact with suffering.",
      "why_watch": "Kurosawa's final film with Mifune and his most explicitly humane statement — a film about medicine, poverty, and what it means to be of service to others.",
      "visual_style": "Gorgeous black-and-white Cinemascope photography — the clinic built as a complete world with extraordinary detail. Kurosawa's most carefully composed studio work.",
      "themes": ["compassion", "coming of age", "poverty", "the teacher-student bond"],
      "runtime": 185
    },
    "Kagemusha": {
      "synopsis": "A petty thief who resembles a powerful warlord is recruited as his double. When the warlord dies, the thief must inhabit his identity completely, experiencing the weight of leadership without its birthright.",
      "why_watch": "Kurosawa's late masterpiece — a film about power, performance, and the emptiness of identity beneath its trappings. The battle sequences are extraordinary.",
      "visual_style": "Restored to big-budget color by Coppola and Lucas's support — the film uses vivid primary color fields in both court scenes and battle sequences. The dream sequences are surreal and magnificent.",
      "themes": ["identity", "power", "performance", "feudal Japan"],
      "runtime": 180
    },
    "Ran": {
      "synopsis": "An aging warlord divides his kingdom among his three sons, precipitating catastrophic civil war. A transposition of King Lear to sixteenth-century Japan, told with the scale of an apocalyptic vision.",
      "why_watch": "The greatest film ever made about old age, hubris, and the ruin that follows. The battle sequence in the third act — armies in colored armor, smoke, and silence — is unlike anything in cinema.",
      "visual_style": "Asakazu Nakai's final collaboration with Kurosawa — color used symbolically and devastatingly. The burning castle sequence used real fire and cost a fortune; it is worth it.",
      "themes": ["hubris", "old age", "filial betrayal", "war's madness"],
      "runtime": 162
    },
    "Dreams": {
      "synopsis": "Eight short films adapting the director's actual dreams — a boy who witnesses foxes' wedding procession, a soldier who cannot believe the war is over, Van Gogh's sunflower fields, a world destroyed by nuclear catastrophe.",
      "why_watch": "Kurosawa unfiltered — pure image, pure feeling, freed from narrative. The Van Gogh episode with Martin Scorsese is joyful; the nuclear episode is genuinely terrifying.",
      "visual_style": "Each segment has its own distinct visual language. The Van Gogh sequence recreates his actual canvases as three-dimensional spaces. Dreams made literal through extraordinary production design.",
      "themes": ["nature", "war", "nuclear fear", "art and vision"],
      "runtime": 119
    }
  },

  # ── Hayao Miyazaki (id 20) ──────────────────────────────────────────────
  20: {
    "Lupin III: The Castle of Cagliostro": {
      "synopsis": "Master thief Lupin III arrives at a tiny European principality to investigate counterfeit currency and ends up rescuing a princess from a forced marriage to the villainous Count Cagliostro. A caper film with extraordinary kinetic energy.",
      "why_watch": "The film that announced Miyazaki as a director of uncommon physical imagination. The rooftop and clocktower chase sequences set a standard for action animation not surpassed for decades.",
      "visual_style": "Miyazaki's characteristic attention to weight and momentum — characters and vehicles move with a tangible sense of mass. The European castle architecture is rendered with loving detail.",
      "themes": ["adventure", "chivalry", "the gentleman thief", "Europe as fantasy"],
      "runtime": 100
    },
    "Nausicaä of the Valley of the Wind": {
      "synopsis": "In a post-apocalyptic world of toxic jungle and giant insects, a young princess navigates the conflicts between warring human kingdoms while seeking to understand — and protect — the dangerous ecosystem others wish to destroy.",
      "why_watch": "Miyazaki's first great statement of his ecological and feminist themes. Nausicaä remains one of animation's most compelling protagonists — brave, curious, and genuinely wise.",
      "visual_style": "The toxic jungle (Sea of Corruption) is rendered with alien beauty — spores drifting like snow, insects as armor and biology. Miyazaki's flying sequences already feel transcendent.",
      "themes": ["ecology", "war", "the outsider who listens", "humanity's relationship to nature"],
      "runtime": 117
    },
    "Castle in the Sky": {
      "synopsis": "A boy and a girl with a mysterious crystal are chased across a steampunk world of airships and flying fortresses toward the legendary floating city of Laputa. Pure adventure cinema for all ages.",
      "why_watch": "The most purely enjoyable film Miyazaki ever made — propulsive, generous, and visually inventive at every turn. The robot guardian in the garden is already iconic.",
      "visual_style": "Industrial age machinery rendered with extraordinary detail and affection. The sky sequences have a freedom and joy that Miyazaki's team would later refine but never surpass.",
      "themes": ["adventure", "technology's double nature", "childhood freedom", "the sky"],
      "runtime": 124
    },
    "My Neighbor Totoro": {
      "synopsis": "Two young sisters move to the countryside while their mother is hospitalized. They encounter forest spirits — including the enormous, gentle Totoro — in a film about childhood wonder, family love, and the living world.",
      "why_watch": "The most tender film Miyazaki ever made. Nothing threatens these children; the world is kind. In a cinema full of darkness, Totoro insists on joy and it earns every moment of it.",
      "visual_style": "Lush, detailed backgrounds of rural Japan — grass that bends in the wind, rain that soaks through. The animation of mundane domestic life (cooking, unpacking) is as loving as the fantastical sequences.",
      "themes": ["childhood wonder", "nature spirits", "family", "the countryside"],
      "runtime": 86
    },
    "Kiki's Delivery Service": {
      "synopsis": "A young witch moves to a new city alone at thirteen, as tradition requires, and starts a delivery service to support herself. The film follows her first year of independence, her loss of magical ability, and its recovery.",
      "why_watch": "Miyazaki's most intimate film about creative work — the loss of confidence, the need for renewal, the particular loneliness of being gifted and young. Every artist understands it.",
      "visual_style": "A lovingly imagined European coastal city, all cobblestones and sea breezes. The flying sequences are graceful rather than spectacular — more like birds than machines.",
      "themes": ["independence", "creative confidence", "young womanhood", "work"],
      "runtime": 102
    },
    "Porco Rosso": {
      "synopsis": "In the Adriatic of the 1930s, a World War I veteran air ace who has been transformed into a pig flies his seaplane for hire, battling air pirates and an American rival, while navigating his feelings for an old friend.",
      "why_watch": "Miyazaki's most personal and most melancholy film — an elegy for a lost Europe, for the romance of flight, and for a kind of masculine honor that the coming war would destroy.",
      "visual_style": "The Adriatic light — late afternoon gold and Tyrrhenian blue — is some of the most beautiful color work Studio Ghibli ever produced. The dogfights move with casual, confident grace.",
      "themes": ["anti-fascism", "melancholy", "honor", "the romance of aviation"],
      "runtime": 94
    },
    "Princess Mononoke": {
      "synopsis": "A young warrior cursed by a dying demon god travels west and becomes caught in the war between an iron-forging human city and the ancient forest gods it is destroying. There are no villains — only interests in fatal conflict.",
      "why_watch": "Miyazaki's most morally complex film refuses easy ecology or easy humanism. Every side has a legitimate claim; the forest and the humans both lose something irreplaceable.",
      "visual_style": "Studio Ghibli's most ambitious production — ancient cedar forests rendered with photographic density alongside the smoke and fire of industrial smelting. The Forest Spirit sequences are purely strange.",
      "themes": ["ecology", "industry vs. nature", "moral ambiguity", "ancient Japan"],
      "runtime": 134
    },
    "Spirited Away": {
      "synopsis": "A sullen ten-year-old girl stumbles into the spirit world when her parents are transformed into pigs. To free them, she must work in a giant bathhouse for spirits, learning patience, empathy, and the value of her own name.",
      "why_watch": "The greatest animated film ever made. It generates awe and wonder with the logic of a dream and the discipline of a master — every frame is alive, every character fully inhabited.",
      "visual_style": "The bathhouse is an architectural and visual wonder — a world of rules and textures and smells you can almost perceive. The train journey across the flooded sea is quietly devastating.",
      "themes": ["identity", "labor", "greed", "growing up"],
      "runtime": 125
    },
    "Howl's Moving Castle": {
      "synopsis": "A young hat-maker is cursed by a witch to inhabit an old woman's body and takes refuge in the moving castle of the wizard Howl, who is himself hiding from a world about to go to war.",
      "why_watch": "Miyazaki's most romantic film and a frank anti-war statement. Sophie's transformation — learning to love herself in an old body — is quietly radical.",
      "visual_style": "The mechanical castle is Miyazaki's most extravagant invention — a lurching, breathing machine that expresses Howl's emotional chaos. The war sequences are deliberately nightmarish.",
      "themes": ["war's absurdity", "self-worth", "transformation", "love"],
      "runtime": 119
    },
    "Ponyo": {
      "synopsis": "A five-year-old boy befriends a magical fish-girl who wants to become human. Her wish unleashes a flood and threatens to upset the balance between the sea and the human world.",
      "why_watch": "Miyazaki returned to hand-drawn animation to make something that feels genuinely ancient — the wave sequences have a prehistoric, Hokusai energy. Pure and strange.",
      "visual_style": "Deliberately childlike drawing — thick outlines and simple colors that evoke children's book illustration. The wave-riding sequence, animated with thousands of hand-drawn water drawings, is extraordinary.",
      "themes": ["childhood love", "the sea", "transformation", "balance"],
      "runtime": 101
    },
    "The Wind Rises": {
      "synopsis": "The life of Jiro Horikoshi, the aeronautical engineer who designed Japan's Zero fighter plane, told as a dream-filled meditation on beauty, ambition, love, and the moral cost of creating instruments of war.",
      "why_watch": "Miyazaki's most adult and most ambivalent film — a love letter to the act of creation that knows the thing created will be used to kill. The dream conversations with Caproni are sublime.",
      "visual_style": "The aircraft designs are rendered with obsessive technical beauty. The 1923 earthquake sequence, using sound design instead of orchestral score, is one of Ghibli's most disturbing achievements.",
      "themes": ["creation and destruction", "engineering as art", "love against mortality", "pre-war Japan"],
      "runtime": 126
    },
    "The Boy and the Heron": {
      "synopsis": "A boy grieving his mother follows a mysterious heron into an abandoned tower and discovers an otherworldly realm built by his great-great-uncle — a world of parakeets, spirits, and choices about inheritance and imagination.",
      "why_watch": "Miyazaki's final film — dense, strange, and deeply personal. A meditation on legacy, grief, and what we leave behind. Like all his best work, it rewards returning to.",
      "visual_style": "The other world has a quality of pure invention — the parakeet army, the wax-block tower, the floating heron. Miyazaki's drawing is looser and stranger than it has ever been, as if freed by finality.",
      "themes": ["grief", "inheritance", "creation", "letting go"],
      "runtime": 124
    }
  },

  # ── Park Chan-wook (id 22) ──────────────────────────────────────────────
  22: {
    "Joint Security Area": {
      "synopsis": "A soldier is shot at the DMZ between North and South Korea. A Swiss investigator uncovers a secret friendship that had formed between soldiers on opposite sides of the border — and the events that destroyed it.",
      "why_watch": "Park's breakthrough film is also his most emotionally direct — a tragedy about the absurdity of Korean division and the friendships it forbids.",
      "visual_style": "Clean, precise cinematography that uses the grey DMZ architecture as a symbol of enforced separation. The flashback sequences have a warm, covert intimacy that makes the final reveal devastating.",
      "themes": ["Korean division", "friendship across borders", "tragedy", "military absurdity"],
      "runtime": 110
    },
    "Sympathy for Mr. Vengeance": {
      "synopsis": "A deaf mute man and his anarchist girlfriend kidnap the daughter of his sister's former employer to pay for a kidney transplant. The plan goes catastrophically wrong, setting off a chain of grief and retribution.",
      "why_watch": "The first and darkest of the Vengeance Trilogy — a film about how misfortune compounds into catastrophe without villains, only people making desperate choices.",
      "visual_style": "Cold, flat cinematography that refuses to aestheticize violence while still composing each image with formal precision. The Nakdong River sequences are hauntingly beautiful.",
      "themes": ["class inequality", "the cycle of revenge", "grief", "capitalism's violence"],
      "runtime": 129
    },
    "Oldboy": {
      "synopsis": "A man is imprisoned without explanation for fifteen years in a private facility, then suddenly released and given five days to discover who imprisoned him and why. The answer is worse than anything he imagined.",
      "why_watch": "The middle and defining film of the Vengeance Trilogy — audacious in its construction, devastating in its revelations, and featuring the corridor fight scene that changed action cinema.",
      "visual_style": "Chung Chung-hoon's cinematography oscillates between claustrophobic interiors and the vertiginous Seoul skyline. Every visual choice — the octopus, the corridor, the ants — carries symbolic weight.",
      "themes": ["memory", "trauma", "fate", "the monster within us"],
      "runtime": 120
    },
    "Lady Vengeance": {
      "synopsis": "A woman falsely imprisoned for thirteen years for the murder of a child is released and begins methodically executing her plan of revenge against the man who framed her — while seeking to reconnect with her daughter.",
      "why_watch": "The most aesthetically refined of the trilogy and Park's most complex treatment of revenge — a film that asks whether justice can be achieved without becoming what you hate.",
      "visual_style": "Chung Chung-hoon's most visually inventive work — a desaturated color palette that slowly reintroduces red as Lee Geum-ja approaches her revenge. Fragmented, fairy-tale imagery.",
      "themes": ["revenge", "motherhood", "guilt", "collective justice"],
      "runtime": 112
    },
    "I'm a Cyborg, But That's OK": {
      "synopsis": "A young woman who believes she is a cyborg is admitted to a psychiatric hospital, where she meets a kleptomaniac who steals people's habits and personalities. A love story between two people defined by their delusions.",
      "why_watch": "Park's most surprising film — pure romantic whimsy from a director known for brutality. The psychiatric hospital becomes a world where the rules of reality are tenderly suspended.",
      "visual_style": "Pastel colors and a floating, dreamlike camera style completely unlike the Vengeance Trilogy. The film looks like a music box — pretty and slightly unreal.",
      "themes": ["mental illness as world-making", "love", "delusion", "tenderness"],
      "runtime": 105
    },
    "Thirst": {
      "synopsis": "A Catholic priest volunteers for a medical experiment and emerges as a vampire. His faith, his celibacy, and ultimately his ethics collapse as he becomes involved with the unhappy wife of a childhood friend.",
      "why_watch": "Park remakes the vampire genre as a film about desire, guilt, and the collapse of moral systems. Song Kang-ho is extraordinary — a man watching himself become what he fears.",
      "visual_style": "Chung Chung-hoon's cinematography moves between the clinical (the hospital) and the baroque (the vampire's nocturnal world), using blood as both horror and beauty.",
      "themes": ["faith and desire", "the vampire as moral parable", "guilt", "transformation"],
      "runtime": 133
    },
    "Stoker": {
      "synopsis": "After her father's death, a teenage girl's enigmatic uncle arrives and insinuates himself into the family. As she discovers what he is capable of, she begins to understand what she herself might become.",
      "why_watch": "Park's English-language debut is a Hitchcock homage with a genuinely unsettling feminist twist — a film about a young woman's awakening to her own capacity for violence.",
      "visual_style": "Chung Chung-hoon's most controlled work — every shot composed like a painting, with nature imagery (spiders, butterflies, soil) woven into a visual language of latent threat.",
      "themes": ["coming of age", "violence as inheritance", "desire", "family as poison"],
      "runtime": 99
    },
    "The Handmaiden": {
      "synopsis": "Set in Japanese-occupied Korea, a young pickpocket is hired as a maid to a secluded Japanese heiress, assisting a con man's plan to seduce and defraud her. Nothing is as it seems, and the film reveals its layers with extraordinary cunning.",
      "why_watch": "Park's most complete and joyful film — a puzzle-box thriller, a lesbian love story, and a feminist revenge fantasy that earns every one of its pleasures.",
      "visual_style": "Chung Chung-hoon's most sumptuous work — the contrast between the Western-style estate and the Japanese pavilion reflects the film's dual perspectives. Erotic, architectural, and precise.",
      "themes": ["colonialism", "female desire", "deception", "freedom"],
      "runtime": 145
    },
    "Decision to Leave": {
      "synopsis": "A detective investigating a man's death on a mountain falls into an obsessive attraction to the victim's widow — a Chinese immigrant whose guilt or innocence he cannot determine and finds he no longer wants to.",
      "why_watch": "Park's most mature and heartbreaking film — a neo-noir about the destructive nature of romantic obsession disguised as a police procedural. The ending is devastating.",
      "visual_style": "Tang Wei and Park Hae-il are filmed with extraordinary delicacy — the film uses smartphone screens and binoculars to embed surveillance into the love story's visual grammar.",
      "themes": ["obsession", "surveillance", "romantic self-destruction", "translation and misunderstanding"],
      "runtime": 138
    }
  },

  # ── David Lynch (id 26) ─────────────────────────────────────────────────
  26: {
    "Eraserhead": {
      "synopsis": "In an industrial wasteland, a meek young man must care for his severely deformed infant with his unstable girlfriend. The film exists at the intersection of waking life and dream, domesticity and horror.",
      "why_watch": "The foundational work of American surrealist cinema — shot over five years on weekends, entirely committed to a single sustained nightmare vision. Nothing before or since sounds quite like it.",
      "visual_style": "Frederick Elmes and Herbert Cardwell's black-and-white cinematography renders an industrial landscape of radiators, curtains, and darkness. The texture of the image is as important as any image within it.",
      "themes": ["fatherhood anxiety", "industrial dread", "the body's monstrousness", "domesticity as nightmare"],
      "runtime": 89
    },
    "The Elephant Man": {
      "synopsis": "A nineteenth-century surgeon discovers John Merrick, a severely deformed man exploited as a sideshow attraction, and attempts to rehabilitate him into Victorian society — but society proves as cruel as the freak show.",
      "why_watch": "Lynch's most emotionally accessible film — a genuine tragedy about humanity and its limits. John Hurt's physical and emotional performance is extraordinary.",
      "visual_style": "The film is shot in black-and-white, evoking both Victorian photography and German Expressionism. The night streets of London are dream-laden and oppressive.",
      "themes": ["humanity", "exploitation", "Victorian hypocrisy", "dignity"],
      "runtime": 124
    },
    "Dune": {
      "synopsis": "The son of a noble house is thrust into the politics of a desert planet whose spice is the most valuable substance in the universe. A massive science-fiction epic that Lynch was never able to make as his own.",
      "why_watch": "A fascinating failure — Lynch's disowned cut still contains remarkable sequences and design work. Essential for understanding what can go wrong when a singular director loses control.",
      "visual_style": "A genuinely alien visual world — the Harkonnen sets are grotesque and baroque, the desert landscapes visually striking. The production design is extraordinary even when the film fails.",
      "themes": ["power", "prophecy", "ecological collapse", "the dangers of messianism"],
      "runtime": 137
    },
    "Blue Velvet": {
      "synopsis": "A college student finds a severed ear in a field in his quiet hometown and is drawn into a world of sadomasochism, kidnapping, and corruption lurking beneath the town's sunny surface.",
      "why_watch": "The film that established Lynch as a master of American darkness — the movie that found the rot beneath the white picket fence and the ants beneath the grass.",
      "visual_style": "Frederick Elmes's cinematography saturates suburbia in impossible colors — the red roses, the white fence, the blue velvet — that feel simultaneously real and constructed. Night sequences are pure noir.",
      "themes": ["suburban darkness", "voyeurism", "sexual violence", "innocence corrupted"],
      "runtime": 120
    },
    "Wild at Heart": {
      "synopsis": "A young couple on the run from the girl's murderous mother travel through a violent, hyper-stylized American South toward a freedom that keeps receding. A Wizard of Oz road movie drenched in sex and violence.",
      "why_watch": "Lynch at his most excessive and purely entertaining — a film that throws everything at the screen and somehow coheres into something exhilarating.",
      "visual_style": "Frederick Francis's cinematography is deliberately artificial — colors cranked to maximum saturation, flames always present, Elvis always on the soundtrack. America as hallucination.",
      "themes": ["transgressive love", "American violence", "fairy-tale darkness", "rock-and-roll freedom"],
      "runtime": 124
    },
    "Twin Peaks: Fire Walk with Me": {
      "synopsis": "The final week in the life of Laura Palmer — the murder whose investigation drove the television series. The film goes where the show could not: into the interior of a young woman's terror and degradation.",
      "why_watch": "Initially reviled, now recognized as a masterpiece — a harrowing, compassionate portrait of abuse and dissociation that reframes everything the series left ambiguous.",
      "visual_style": "Peter Deming's cinematography moves between the familiar Pacific Northwest locations and genuinely terrifying interior spaces — the red room, the train car. The Log Lady's introduction uses darkness as texture.",
      "themes": ["abuse", "dissociation", "the violence beneath small-town life", "female suffering"],
      "runtime": 134
    },
    "Lost Highway": {
      "synopsis": "A jazz musician becomes convinced his wife is unfaithful and finds mysterious videotapes on their doorstep. After an unexplained event, he becomes a different man — a young mechanic with different memories and a different life.",
      "why_watch": "Lynch's most formally radical narrative — a Möbius strip of identity with no psychological explanation offered. The desert highway sequences are some of cinema's most hypnotic imagery.",
      "visual_style": "Peter Deming's compositions emphasize darkness and architectural unease. The house feels alive with menace; the desert highway at night becomes an existential void.",
      "themes": ["identity dissolution", "guilt", "the uncanny double", "psychic self-reinvention"],
      "runtime": 134
    },
    "The Straight Story": {
      "synopsis": "A seventy-three-year-old man rides his lawnmower from Iowa to Wisconsin to visit his ailing estranged brother. The film is a road movie at walking pace — an account of a journey that becomes a meditation on a life.",
      "why_watch": "Lynch's anomalous masterpiece — entirely devoid of the surrealism and darkness that define his work, and all the more powerful for it. A film about age, forgiveness, and endurance.",
      "visual_style": "Freddie Francis's cinematography gives the American Midwest the quality of a landscape painting — long golden light, grain fields, water towers. The slow pace is the form.",
      "themes": ["aging", "reconciliation", "stubbornness as virtue", "rural America"],
      "runtime": 112
    },
    "Mulholland Drive": {
      "synopsis": "An aspiring actress arrives in Los Angeles and befriends a woman with amnesia who is trying to discover her own identity. After a rupture in the film's logic, an entirely different story is revealed — or perhaps the first one is.",
      "why_watch": "The greatest film about Hollywood ever made and Lynch's undisputed masterpiece. The Silencio sequence and the revelation of the blue box are among the most powerful moments in all of cinema.",
      "visual_style": "Peter Deming's cinematography creates a Hollywood that is simultaneously a dream and a nightmare — the same locations lit differently become entirely different spaces. The sequence at Club Silencio uses light as existential statement.",
      "themes": ["Hollywood's illusions", "desire and identity", "the dream turned nightmare", "duality"],
      "runtime": 147
    },
    "Inland Empire": {
      "synopsis": "An actress begins work on a film and loses herself in its story — or its story loses itself in her. Shot on consumer digital video, the film abandons narrative continuity for a three-hour immersion in an actress's dissolving identity.",
      "why_watch": "Lynch's most extreme and uncompromising film — shot on DV, edited over years, entirely intuitive. Difficult and sometimes bewildering, it is also deeply felt.",
      "visual_style": "Consumer digital video shot with a Sony PD-150 — grainy, overexposed, immediate. Lynch deliberately embraces the cheap format's limitations as expressive tool.",
      "themes": ["identity dissolution", "performance and reality", "Hollywood exploitation", "the horror of femininity"],
      "runtime": 180
    }
  },

  # ── Stanley Kubrick (id 55) ─────────────────────────────────────────────
  55: {
    "Paths of Glory": {
      "synopsis": "In World War I France, three soldiers are court-martialed and executed for cowardice after a failed assault that their commanding general ordered knowing it was impossible. A French colonel fights futilely to defend them.",
      "why_watch": "The most uncompromising anti-war film in American cinema up to that point. The tracking shot through the trenches and the final courtroom scenes are perfect in their fury.",
      "visual_style": "Georg Krause's cinematography uses a stark black-and-white that contrasts the geometric luxury of the chateau with the mud-and-shadow chaos of the trenches.",
      "themes": ["military injustice", "class and sacrifice", "the machinery of war", "honor"],
      "runtime": 88
    },
    "Spartacus": {
      "synopsis": "A slave leads a revolt against the Roman Republic that grows into a mass uprising. A Hollywood epic produced by Kirk Douglas with a radical subtext about freedom, solidarity, and the individual against the state.",
      "why_watch": "Kubrick disowned much of it, but Spartacus contains some of his finest work — the battle sequences, the love scenes, and Laurence Olivier's extraordinary villain.",
      "visual_style": "Russell Metty's Technicolor photography gives the film a warm, painted quality that alternates with scenes of harsh military geometry. The scale of the battle sequences was unprecedented.",
      "themes": ["slavery and freedom", "solidarity", "Rome as imperial power", "the individual vs. the state"],
      "runtime": 197
    },
    "Lolita": {
      "synopsis": "A European intellectual becomes obsessed with his landlady's twelve-year-old daughter, marries the mother to stay near the girl, and pursues a degrading and eventually catastrophic relationship across America.",
      "why_watch": "Kubrick adapts Nabokov's unstageable novel by making it a black comedy — withholding the horror in order to reveal it. James Mason's Humbert is fascinatingly repellent.",
      "visual_style": "Oswald Morris's black-and-white cinematography is crisp and clinical — treating the suburban American locations with a cold, anthropological eye that heightens the irony.",
      "themes": ["obsession", "the unreliable narrator", "America's banal surface", "predation disguised as love"],
      "runtime": 153
    },
    "Dr. Strangelove": {
      "synopsis": "A paranoid American general launches a nuclear strike on the Soviet Union, and the men responsible for averting World War III — including a wheelchair-bound ex-Nazi scientist — prove utterly incapable of doing so.",
      "why_watch": "The funniest film ever made about human extinction. Kubrick's decision to play the end of the world as farce remains the most penetrating critique of Cold War military thinking ever committed to film.",
      "visual_style": "Gilbert Taylor's black-and-white photography creates three distinct worlds — the B-52 bomber, the war room, and Burpelson Air Force Base — each with its own visual logic.",
      "themes": ["nuclear madness", "masculine aggression", "bureaucratic absurdity", "the military-industrial complex"],
      "runtime": 95
    },
    "2001: A Space Odyssey": {
      "synopsis": "From the dawn of human tool use through a voyage to Jupiter following a mysterious monolith, a story of evolution, artificial intelligence, and the possibility of something beyond human comprehension.",
      "why_watch": "The most visually influential film ever made. It permanently changed what cinema could aspire to — a film that thinks in images rather than words, at the scale of cosmic time.",
      "visual_style": "Geoffrey Unsworth and John Alcott's cinematography achieved visual effects that remain convincing fifty years later. The match cut from bone to spacecraft is the most famous edit in film history.",
      "themes": ["human evolution", "artificial intelligence", "the monolith as enigma", "transcendence"],
      "runtime": 149
    },
    "A Clockwork Orange": {
      "synopsis": "Alex DeLarge, the charismatic leader of a violent teenage gang in near-future Britain, is imprisoned and subjected to aversion therapy that eliminates his capacity for violence — along with his free will.",
      "why_watch": "Kubrick's most controversial film forces the viewer into uncomfortable proximity with a monster and then asks whether we prefer that monster free or compliant. The central ethical question is never resolved.",
      "visual_style": "John Alcott's cinematography uses wide-angle lenses that distort and comic-book colors — the Korova Milk Bar, the droogs' costumes — to create a world recognizable but alien.",
      "themes": ["free will", "state power", "violence's aestheticization", "behavior modification"],
      "runtime": 136
    },
    "Barry Lyndon": {
      "synopsis": "An Irish rogue rises through eighteenth-century European society by luck, marriage, and cunning, accumulates wealth and title, and is eventually destroyed by the indifference of the same society he conquered.",
      "why_watch": "Kubrick's most misunderstood and possibly greatest film — a meditation on the arbitrary nature of social status, filmed with candlelight and natural light to achieve the quality of period painting.",
      "visual_style": "John Alcott's cinematography used specially modified NASA lenses to shoot by candlelight. Every interior looks like a Gainsborough or Hogarth. The zoom lens creates a distancing, contemplative visual rhythm.",
      "themes": ["social climbing", "the randomness of fate", "eighteenth-century Europe", "the cruelty of class"],
      "runtime": 185
    },
    "The Shining": {
      "synopsis": "A writer takes a job as winter caretaker of a remote Colorado hotel and gradually loses his mind — or encounters the hotel's malevolent supernatural history — while his wife and psychic son grow increasingly terrified.",
      "why_watch": "The most formally controlled horror film ever made. The Steadicam work, the symmetrical compositions, and the score create a sustained state of dread that never relies on cheap shock.",
      "visual_style": "John Alcott's Steadicam work (with Garrett Brown) follows Danny through the hotel's corridors with fluid, predatory grace. The symmetrical compositions of every room create a geometric unease.",
      "themes": ["domestic violence", "alcoholism", "psychic phenomena", "the hotel as labyrinth"],
      "runtime": 144
    },
    "Full Metal Jacket": {
      "synopsis": "In two distinct halves: the brutal transformation of Marine recruits by a sadistic drill instructor; and the experiences of one survivor as a combat journalist in the Tet Offensive's battle for Hué.",
      "why_watch": "The first half remains the most psychologically acute depiction of military dehumanization in cinema. The two halves deliberately refuse to cohere — the point is the rupture.",
      "visual_style": "Douglas Milsome's cinematography uses the flat light of Parris Island and the rubble of Hué (recreated in London's docklands) to create two utterly distinct visual worlds.",
      "themes": ["military dehumanization", "the duality of humanity", "Vietnam", "the creation of killers"],
      "runtime": 116
    },
    "Eyes Wide Shut": {
      "synopsis": "A New York doctor, unsettled by his wife's confession of a fantasy affair, spends a night wandering through a hidden world of privileged, ritualistic sexuality, and returns changed in ways he cannot fully articulate.",
      "why_watch": "Kubrick's final film — a dreamlike investigation of desire, jealousy, and the secret lives of the wealthy. Its slow pace is deliberate; it asks to be inhabited rather than consumed.",
      "visual_style": "Larry Smith's cinematography uses Christmas lights and practical sources to create a warm, artificial glow that makes New York look like a stage set. The mansion orgy sequence is filmed with operatic formality.",
      "themes": ["desire", "marriage's secrets", "class privilege", "the dream state"],
      "runtime": 159
    }
  },

  # ── Sofia Coppola (id 57) ───────────────────────────────────────────────
  57: {
    "The Virgin Suicides": {
      "synopsis": "Five sisters in 1970s suburban Michigan are sequentially confined to their home by their religious parents following a suicide attempt. Their story is narrated by the neighborhood boys who were obsessed with them — and who never understood them.",
      "why_watch": "A beautiful, melancholy debut that established Coppola's central theme: the interior lives of women observed from outside. The narrators' failure to comprehend the sisters is the film's entire point.",
      "visual_style": "Edward Lachman's cinematography bathes the suburban Midwest in the diffused gold of memory — warm, faded, and slightly unreal. The images look like photographs kept in a drawer.",
      "themes": ["female mystery", "suburban suffocation", "male fantasy", "adolescence"],
      "runtime": 97
    },
    "Lost in Translation": {
      "synopsis": "A fading American movie star and a young wife accompany her photographer husband to Tokyo, where the city's alienness draws them into an unexpected friendship — intimate, unspeakable, and brief.",
      "why_watch": "The definitive film about the particular sadness of hotel-room loneliness, the intimacy that forms between people adrift, and what happens when connection must remain unspoken.",
      "visual_style": "Lance Acord's cinematography captures Tokyo's neon and noise with a deliberately low-depth-of-field, intimate quality — the city is spectacle but always filtered through human perception.",
      "themes": ["alienation", "connection between strangers", "Tokyo", "the unspoken"],
      "runtime": 102
    },
    "Marie Antoinette": {
      "synopsis": "The young Austrian archduchess's arrival at Versailles, her marriage to the future Louis XVI, her years of fashionable excess, and her growing awareness of the revolutionary forces gathering outside the palace walls.",
      "why_watch": "A radical interpretation that treats Marie Antoinette as a teenager doing her best in an impossible situation — the anachronistic soundtrack and pastel palette are deliberate, not accidental.",
      "visual_style": "Lance Acord's cinematography uses natural light from Versailles's actual candles and windows — the most expensive candles in cinema history. The pastel colors and obsessive detail of food and fabric are overwhelming.",
      "themes": ["female powerlessness within luxury", "adolescent identity", "history as fashion", "imprisonment in privilege"],
      "runtime": 123
    },
    "Somewhere": {
      "synopsis": "A famous actor lives in the Chateau Marmont in a fog of boredom and disconnection. When his eleven-year-old daughter arrives unexpectedly, her presence briefly disrupts his stupor.",
      "why_watch": "Coppola's most minimal and underrated film — long takes of emptiness that accumulate into a portrait of a particular kind of male numbness. The pole-dancing twins sequence is extraordinary.",
      "visual_style": "Harris Savides's cinematography uses very long, static takes and available light to create an atmosphere of suspension. The Chateau Marmont is filmed as a luxurious purgatory.",
      "themes": ["celebrity's emptiness", "fatherhood", "absence as presence", "Los Angeles"],
      "runtime": 98
    },
    "The Bling Ring": {
      "synopsis": "A group of Los Angeles teenagers obsessed with celebrity culture break into the homes of Paris Hilton, Orlando Bloom, and others to steal and to feel close to fame. Based on a true story.",
      "why_watch": "Coppola's sharpest social film — a deadpan portrait of a generation that believes fame is identity and celebrity possessions are a form of love.",
      "visual_style": "Christopher Blauvelt's photography uses the cold glow of phone screens and security cameras. The real Paris Hilton's actual house was used — the surveillance aesthetic is deliberate.",
      "themes": ["celebrity worship", "social media culture", "emptiness", "the American dream inverted"],
      "runtime": 90
    },
    "The Beguiled": {
      "synopsis": "A wounded Union soldier is taken in by the women and girls of a Confederate Virginia girls' school. As he recovers, his manipulations of the women's desires spiral toward a violent conclusion.",
      "why_watch": "A formally perfect gothic — Coppola reverses Don Siegel's 1971 version by centering the women's perspective. The garden's beauty is the threat.",
      "visual_style": "Philippe Le Sourd's cinematography uses natural light and the deep shade of a Virginia plantation garden to create an atmosphere of dangerous beauty — warm, humid, and enclosed.",
      "themes": ["female desire and power", "the Confederacy's illusions", "manipulation", "enclosed worlds"],
      "runtime": 94
    },
    "On the Rocks": {
      "synopsis": "A writer in New York, worried that her husband might be having an affair, teams up with her charming, womanizing father to investigate. A gentle, bittersweet father-daughter comedy.",
      "why_watch": "Coppola's most relaxed film — a love letter to New York and to a particular kind of father-daughter relationship. Bill Murray is effortlessly charming.",
      "visual_style": "Philippe Le Sourd's New York photography captures the city at its most golden — SoHo lofts and uptown restaurants in warm, lived-in light.",
      "themes": ["marriage doubt", "father-daughter bonds", "New York", "growing older"],
      "runtime": 96
    },
    "Priscilla": {
      "synopsis": "The story of Priscilla Beaulieu's relationship with Elvis Presley, from their first meeting when she was fourteen to her eventual departure from Graceland. Told entirely from her perspective.",
      "why_watch": "A revisionist portrait of a relationship that pop mythology has always told from Elvis's side. Coppola restores Priscilla's interiority — her boredom, her confinement, her quiet resistance.",
      "visual_style": "Philippe Le Sourd's cinematography gives Graceland an oppressive warmth — too much gold, too many mirrors. Priscilla's perspective makes the famous house feel like a beautiful cage.",
      "themes": ["female agency", "age and power", "celebrity relationships", "confined femininity"],
      "runtime": 113
    }
  }
}

def main():
    with open(DATA_FILE) as f:
        data = json.load(f)

    enriched_count = 0
    for director in data:
        if director['id'] not in FILM_DATA:
            continue
        films_dict = FILM_DATA[director['id']]
        print(f"\n── {director['name']}")
        for film in director['notable_films']:
            fd = films_dict.get(film['title'])
            if fd:
                film.update(fd)
                print(f"  ✓ {film['title']}")
                enriched_count += 1
            else:
                print(f"  – {film['title']} (no data)")

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✓ Done — {enriched_count} films enriched.")

if __name__ == '__main__':
    main()
