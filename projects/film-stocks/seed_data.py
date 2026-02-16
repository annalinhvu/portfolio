"""Seed the Analog Film Stock Database with realistic data."""

import db

STOCKS = [
    # Kodak (~14)
    {"name": "Portra 160", "brand": "Kodak", "type": "color_negative", "format": "35mm", "iso": 160, "process": "C-41",
     "grain": "fine", "tone": "warm", "saturation": "moderate", "latitude": "wide", "status": "available",
     "best_for": "Portraits with natural skin tones", "description": "Professional color negative with exceptionally smooth grain and natural color reproduction."},
    {"name": "Portra 400", "brand": "Kodak", "type": "color_negative", "format": "35mm", "iso": 400, "process": "C-41",
     "grain": "fine", "tone": "warm", "saturation": "moderate", "latitude": "wide", "status": "available",
     "best_for": "Versatile portrait and wedding work", "description": "The gold standard for portrait photography. Unmatched skin tones with wide exposure latitude."},
    {"name": "Portra 800", "brand": "Kodak", "type": "color_negative", "format": "35mm", "iso": 800, "process": "C-41",
     "grain": "medium", "tone": "warm", "saturation": "moderate", "latitude": "wide", "status": "available",
     "best_for": "Low-light portraits and events", "description": "High-speed portrait film with warm tones. Great for indoor and low-light shooting."},
    {"name": "Ektar 100", "brand": "Kodak", "type": "color_negative", "format": "35mm", "iso": 100, "process": "C-41",
     "grain": "fine", "tone": "cool", "saturation": "vivid", "latitude": "moderate", "status": "available",
     "best_for": "Landscapes and nature with vivid color", "description": "World's finest grain color negative film. Ultra-vivid colors ideal for landscapes."},
    {"name": "Gold 200", "brand": "Kodak", "type": "color_negative", "format": "35mm", "iso": 200, "process": "C-41",
     "grain": "medium", "tone": "warm", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Everyday shooting with warm golden tones", "description": "Consumer classic with warm, golden color rendering. Great for sunny outdoor shooting."},
    {"name": "ColorPlus 200", "brand": "Kodak", "type": "color_negative", "format": "35mm", "iso": 200, "process": "C-41",
     "grain": "medium", "tone": "warm", "saturation": "moderate", "latitude": "wide", "status": "available",
     "best_for": "Budget-friendly everyday color", "description": "Affordable color negative film with pleasant warm tones and reliable results."},
    {"name": "UltraMax 400", "brand": "Kodak", "type": "color_negative", "format": "35mm", "iso": 400, "process": "C-41",
     "grain": "medium", "tone": "warm", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "All-purpose consumer shooting", "description": "Versatile consumer film with punchy colors. Works well in varied lighting conditions."},
    {"name": "Vision3 50D", "brand": "Kodak", "type": "color_negative", "format": "35mm", "iso": 50, "process": "ECN-2",
     "grain": "fine", "tone": "neutral", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Daylight cinema-look stills", "description": "Motion picture film stock respooled for still cameras. Incredible color and dynamic range."},
    {"name": "Vision3 250D", "brand": "Kodak", "type": "color_negative", "format": "35mm", "iso": 250, "process": "ECN-2",
     "grain": "fine", "tone": "neutral", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Daylight cinema versatility", "description": "Medium-speed motion picture stock with wide latitude. Beautiful for daylight shooting."},
    {"name": "Vision3 500T", "brand": "Kodak", "type": "color_negative", "format": "35mm", "iso": 500, "process": "ECN-2",
     "grain": "medium", "tone": "cool", "saturation": "moderate", "latitude": "wide", "status": "available",
     "best_for": "Tungsten-balanced night shooting", "description": "Tungsten-balanced cinema stock. Creates iconic blue-shifted tones under daylight."},
    {"name": "Tri-X 400", "brand": "Kodak", "type": "bw_negative", "format": "35mm", "iso": 400, "process": "BW",
     "grain": "medium", "tone": "neutral", "saturation": "muted", "latitude": "wide", "status": "available",
     "best_for": "Classic photojournalism and street", "description": "The legendary B&W film. Rich tonal range with distinctive grain character."},
    {"name": "T-Max 100", "brand": "Kodak", "type": "bw_negative", "format": "35mm", "iso": 100, "process": "BW",
     "grain": "fine", "tone": "neutral", "saturation": "muted", "latitude": "moderate", "status": "available",
     "best_for": "Fine detail B&W work", "description": "Tabular grain B&W film with extremely fine grain and high sharpness."},
    {"name": "T-Max 400", "brand": "Kodak", "type": "bw_negative", "format": "35mm", "iso": 400, "process": "BW",
     "grain": "fine", "tone": "neutral", "saturation": "muted", "latitude": "wide", "status": "available",
     "best_for": "Versatile B&W with fine grain", "description": "High-speed tabular grain film combining speed with remarkably fine grain."},
    {"name": "Ektachrome E100", "brand": "Kodak", "type": "color_reversal", "format": "35mm", "iso": 100, "process": "E-6",
     "grain": "fine", "tone": "cool", "saturation": "vivid", "latitude": "narrow", "status": "available",
     "best_for": "Slides with vivid, clean color", "description": "Revived slide film with clean color, fine grain, and classic reversal pop."},
    # Ilford (~8)
    {"name": "HP5 Plus 400", "brand": "Ilford", "type": "bw_negative", "format": "35mm", "iso": 400, "process": "BW",
     "grain": "medium", "tone": "neutral", "saturation": "muted", "latitude": "wide", "status": "available",
     "best_for": "All-around B&W workhorse", "description": "Classic high-speed B&W film. Extremely versatile with wide push/pull latitude."},
    {"name": "FP4 Plus 125", "brand": "Ilford", "type": "bw_negative", "format": "35mm", "iso": 125, "process": "BW",
     "grain": "fine", "tone": "neutral", "saturation": "muted", "latitude": "moderate", "status": "available",
     "best_for": "Medium-speed B&W with fine grain", "description": "Medium-speed B&W with excellent sharpness and fine grain. Great for controlled lighting."},
    {"name": "Delta 100", "brand": "Ilford", "type": "bw_negative", "format": "35mm", "iso": 100, "process": "BW",
     "grain": "fine", "tone": "cool", "saturation": "muted", "latitude": "moderate", "status": "available",
     "best_for": "High-resolution B&W detail", "description": "Core-shell crystal technology for extremely fine grain and high resolution."},
    {"name": "Delta 400", "brand": "Ilford", "type": "bw_negative", "format": "35mm", "iso": 400, "process": "BW",
     "grain": "fine", "tone": "neutral", "saturation": "muted", "latitude": "wide", "status": "available",
     "best_for": "Modern B&W with fine grain at speed", "description": "Modern tabular grain B&W film. Fine grain for its speed with smooth tonality."},
    {"name": "Delta 3200", "brand": "Ilford", "type": "bw_negative", "format": "35mm", "iso": 3200, "process": "BW",
     "grain": "heavy", "tone": "neutral", "saturation": "muted", "latitude": "wide", "status": "available",
     "best_for": "Ultra-low-light and high-grain aesthetic", "description": "Ultra-high-speed B&W film for available-light photography. Beautiful heavy grain."},
    {"name": "Pan F Plus 50", "brand": "Ilford", "type": "bw_negative", "format": "35mm", "iso": 50, "process": "BW",
     "grain": "fine", "tone": "cool", "saturation": "muted", "latitude": "narrow", "status": "available",
     "best_for": "Ultra-fine grain B&W in bright light", "description": "Exceptionally fine grain B&W film for maximum sharpness in good light."},
    {"name": "XP2 Super 400", "brand": "Ilford", "type": "bw_negative", "format": "35mm", "iso": 400, "process": "C-41",
     "grain": "fine", "tone": "neutral", "saturation": "muted", "latitude": "wide", "status": "available",
     "best_for": "B&W processed at any lab (C-41)", "description": "Chromogenic B&W film processed in C-41 chemistry. Develop anywhere color film is processed."},
    {"name": "SFX 200", "brand": "Ilford", "type": "bw_negative", "format": "35mm", "iso": 200, "process": "BW",
     "grain": "medium", "tone": "neutral", "saturation": "muted", "latitude": "moderate", "status": "available",
     "best_for": "Near-infrared creative effects", "description": "Extended red sensitivity B&W film. Creates striking infrared-like effects with deep red filter."},
    # Fujifilm (~4)
    {"name": "Superia X-TRA 400", "brand": "Fujifilm", "type": "color_negative", "format": "35mm", "iso": 400, "process": "C-41",
     "grain": "medium", "tone": "cool", "saturation": "vivid", "latitude": "moderate", "status": "available",
     "best_for": "Vivid everyday color with cool tones", "description": "Consumer color film known for punchy greens and blues. A Fuji signature look."},
    {"name": "C200", "brand": "Fujifilm", "type": "color_negative", "format": "35mm", "iso": 200, "process": "C-41",
     "grain": "medium", "tone": "cool", "saturation": "moderate", "latitude": "moderate", "status": "limited",
     "best_for": "Budget color with Fuji tones", "description": "Affordable color negative with characteristic Fuji greens. Increasingly hard to find."},
    {"name": "Provia 100F", "brand": "Fujifilm", "type": "color_reversal", "format": "35mm", "iso": 100, "process": "E-6",
     "grain": "fine", "tone": "neutral", "saturation": "vivid", "latitude": "narrow", "status": "available",
     "best_for": "Reference-grade color slides", "description": "Professional slide film with faithful color reproduction and ultra-fine grain."},
    {"name": "Velvia 50", "brand": "Fujifilm", "type": "color_reversal", "format": "35mm", "iso": 50, "process": "E-6",
     "grain": "fine", "tone": "warm", "saturation": "vivid", "latitude": "narrow", "status": "limited",
     "best_for": "Ultra-saturated landscape slides", "description": "Legendary slide film with extreme color saturation. The landscape photographer's choice."},
    # CineStill (~4)
    {"name": "800T", "brand": "CineStill", "type": "color_negative", "format": "35mm", "iso": 800, "process": "C-41",
     "grain": "medium", "tone": "cool", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Night photography with halation glow", "description": "Modified Kodak Vision3 500T. Iconic red halation around highlights. Made for night."},
    {"name": "50D", "brand": "CineStill", "type": "color_negative", "format": "35mm", "iso": 50, "process": "C-41",
     "grain": "fine", "tone": "neutral", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Daylight cinema look in C-41", "description": "Modified Kodak Vision3 50D for C-41 processing. Fine grain with cinema colors."},
    {"name": "400D", "brand": "CineStill", "type": "color_negative", "format": "35mm", "iso": 400, "process": "C-41",
     "grain": "fine", "tone": "neutral", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Versatile cinema-style color", "description": "Daylight-balanced versatile film based on motion picture stock. Subtle halation."},
    {"name": "BwXX", "brand": "CineStill", "type": "bw_negative", "format": "35mm", "iso": 250, "process": "BW",
     "grain": "medium", "tone": "neutral", "saturation": "muted", "latitude": "wide", "status": "available",
     "best_for": "Cinema-style B&W", "description": "Based on Kodak Double-X motion picture stock. Classic noir-style B&W rendering."},
    # Lomography (~5)
    {"name": "Color Negative 100", "brand": "Lomography", "type": "color_negative", "format": "35mm", "iso": 100, "process": "C-41",
     "grain": "medium", "tone": "warm", "saturation": "vivid", "latitude": "moderate", "status": "available",
     "best_for": "Saturated daylight fun", "description": "Punchy, saturated color film for bright conditions. Great for experimental shooting."},
    {"name": "Color Negative 400", "brand": "Lomography", "type": "color_negative", "format": "35mm", "iso": 400, "process": "C-41",
     "grain": "medium", "tone": "warm", "saturation": "vivid", "latitude": "moderate", "status": "available",
     "best_for": "Versatile experimental color", "description": "All-purpose color film with vivid rendering. Works well in varied conditions."},
    {"name": "Color Negative 800", "brand": "Lomography", "type": "color_negative", "format": "35mm", "iso": 800, "process": "C-41",
     "grain": "heavy", "tone": "warm", "saturation": "vivid", "latitude": "moderate", "status": "available",
     "best_for": "Low-light experimental shooting", "description": "High-speed color film with heavy grain and saturated colors. Embrace the grain."},
    {"name": "Lady Grey 400", "brand": "Lomography", "type": "bw_negative", "format": "35mm", "iso": 400, "process": "BW",
     "grain": "medium", "tone": "neutral", "saturation": "muted", "latitude": "moderate", "status": "available",
     "best_for": "Accessible B&W with character", "description": "Affordable B&W film with pleasing grain structure and smooth tonal range."},
    {"name": "Potsdam 100", "brand": "Lomography", "type": "bw_negative", "format": "35mm", "iso": 100, "process": "BW",
     "grain": "fine", "tone": "cool", "saturation": "muted", "latitude": "moderate", "status": "available",
     "best_for": "High-contrast B&W with German cine feel", "description": "Based on ORWO film stock. High contrast with a unique vintage cinema look."},
    # Fomapan (~3)
    {"name": "Fomapan 100", "brand": "Fomapan", "type": "bw_negative", "format": "35mm", "iso": 100, "process": "BW",
     "grain": "fine", "tone": "neutral", "saturation": "muted", "latitude": "moderate", "status": "available",
     "best_for": "Budget fine-grain B&W", "description": "Czech-made B&W film. Great value with classic rendering and fine grain."},
    {"name": "Fomapan 200", "brand": "Fomapan", "type": "bw_negative", "format": "35mm", "iso": 200, "process": "BW",
     "grain": "medium", "tone": "neutral", "saturation": "muted", "latitude": "moderate", "status": "available",
     "best_for": "Versatile budget B&W", "description": "Medium-speed B&W with pleasant tonality. Excellent value for students and experimenters."},
    {"name": "Fomapan 400", "brand": "Fomapan", "type": "bw_negative", "format": "35mm", "iso": 400, "process": "BW",
     "grain": "heavy", "tone": "neutral", "saturation": "muted", "latitude": "wide", "status": "available",
     "best_for": "Gritty high-speed budget B&W", "description": "High-speed B&W with distinctive heavy grain. Popular for street and documentary work."},
    # Others (~2)
    {"name": "Ortho Plus 80", "brand": "Ilford", "type": "bw_negative", "format": "35mm", "iso": 80, "process": "BW",
     "grain": "fine", "tone": "cool", "saturation": "muted", "latitude": "narrow", "status": "available",
     "best_for": "Orthochromatic B&W portraits", "description": "Orthochromatic B&W film. Blind to red light, creating unique skin tones and landscapes."},
    {"name": "Washi Z", "brand": "Film Washi", "type": "bw_negative", "format": "35mm", "iso": 400, "process": "BW",
     "grain": "heavy", "tone": "cool", "saturation": "muted", "latitude": "narrow", "status": "limited",
     "best_for": "Extreme contrast aerial surveillance look", "description": "Repurposed aerial surveillance film. Extreme contrast with unique texture."},
    # ── 16mm Stocks ──
    {"name": "Vision3 50D 16mm", "brand": "Kodak", "type": "color_negative", "format": "16mm", "iso": 50, "process": "ECN-2",
     "grain": "fine", "tone": "neutral", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Daylight 16mm filmmaking", "description": "100ft roll of 7203 motion picture stock. The standard for daylight 16mm cinematography."},
    {"name": "Vision3 200T 16mm", "brand": "Kodak", "type": "color_negative", "format": "16mm", "iso": 200, "process": "ECN-2",
     "grain": "fine", "tone": "neutral", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Versatile tungsten 16mm", "description": "100ft roll of 7213 tungsten-balanced stock. Great for mixed and interior lighting."},
    {"name": "Vision3 250D 16mm", "brand": "Kodak", "type": "color_negative", "format": "16mm", "iso": 250, "process": "ECN-2",
     "grain": "fine", "tone": "neutral", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Daylight 16mm with extra speed", "description": "100ft roll of 7207 daylight stock. Versatile medium-speed option for 16mm."},
    {"name": "Vision3 500T 16mm", "brand": "Kodak", "type": "color_negative", "format": "16mm", "iso": 500, "process": "ECN-2",
     "grain": "medium", "tone": "cool", "saturation": "moderate", "latitude": "wide", "status": "available",
     "best_for": "Low-light 16mm cinematography", "description": "100ft roll of 7219 tungsten stock. The go-to for night scenes and available-light 16mm work."},
    {"name": "Double-X 7222 16mm", "brand": "Kodak", "type": "bw_negative", "format": "16mm", "iso": 250, "process": "BW",
     "grain": "medium", "tone": "neutral", "saturation": "muted", "latitude": "wide", "status": "available",
     "best_for": "Classic cinema B&W 16mm", "description": "100ft roll of legendary Double-X B&W stock. Used in countless classic films and music videos."},
    {"name": "Tri-X Reversal 7266 16mm", "brand": "Kodak", "type": "bw_reversal", "format": "16mm", "iso": 200, "process": "BW",
     "grain": "medium", "tone": "neutral", "saturation": "muted", "latitude": "moderate", "status": "available",
     "best_for": "B&W reversal projection and scanning", "description": "100ft roll of B&W reversal film. Projects directly without printing. High contrast with rich blacks."},
    {"name": "Ektachrome 100D 7294 16mm", "brand": "Kodak", "type": "color_reversal", "format": "16mm", "iso": 100, "process": "E-6",
     "grain": "fine", "tone": "cool", "saturation": "vivid", "latitude": "narrow", "status": "available",
     "best_for": "Color reversal 16mm projection", "description": "100ft roll of color reversal motion picture film. Vibrant colors, projects directly."},
    {"name": "Fomapan R100 16mm", "brand": "Fomapan", "type": "bw_reversal", "format": "16mm", "iso": 100, "process": "BW",
     "grain": "fine", "tone": "neutral", "saturation": "muted", "latitude": "narrow", "status": "available",
     "best_for": "Budget B&W reversal 16mm", "description": "100ft roll of affordable B&W reversal film. Great for students and experimental filmmakers."},
    # ── Super 8 Stocks ──
    {"name": "Vision3 50D Super 8", "brand": "Kodak", "type": "color_negative", "format": "super8", "iso": 50, "process": "ECN-2",
     "grain": "fine", "tone": "neutral", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Daylight Super 8 with cinema color", "description": "Super 8 cartridge of 7203 stock. Stunning detail and color for the format."},
    {"name": "Vision3 200T Super 8", "brand": "Kodak", "type": "color_negative", "format": "super8", "iso": 200, "process": "ECN-2",
     "grain": "fine", "tone": "neutral", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Tungsten Super 8 for interiors", "description": "Super 8 cartridge of 7213 tungsten stock. Ideal for indoor and mixed lighting."},
    {"name": "Vision3 500T Super 8", "brand": "Kodak", "type": "color_negative", "format": "super8", "iso": 500, "process": "ECN-2",
     "grain": "medium", "tone": "cool", "saturation": "moderate", "latitude": "wide", "status": "available",
     "best_for": "Low-light Super 8 shooting", "description": "Super 8 cartridge of 7219 stock. Maximum speed for available-light Super 8 filmmaking."},
    {"name": "Tri-X Reversal 7266 Super 8", "brand": "Kodak", "type": "bw_reversal", "format": "super8", "iso": 200, "process": "BW",
     "grain": "medium", "tone": "neutral", "saturation": "muted", "latitude": "moderate", "status": "available",
     "best_for": "B&W Super 8 with classic texture", "description": "Super 8 cartridge of Tri-X reversal. Iconic B&W look for home movies and art film."},
    {"name": "Ektachrome 100D Super 8", "brand": "Kodak", "type": "color_reversal", "format": "super8", "iso": 100, "process": "E-6",
     "grain": "fine", "tone": "cool", "saturation": "vivid", "latitude": "narrow", "status": "available",
     "best_for": "Vibrant color Super 8 projection", "description": "Super 8 cartridge of Ektachrome. Beautiful for projection with vivid, saturated colors."},
    {"name": "Gold 200 Super 8", "brand": "Kodak", "type": "color_negative", "format": "super8", "iso": 200, "process": "C-41",
     "grain": "medium", "tone": "warm", "saturation": "vivid", "latitude": "wide", "status": "available",
     "best_for": "Affordable Super 8 color", "description": "Super 8 cartridge loaded with Gold 200. Warm, nostalgic look at a consumer price point."},
]

VENDORS = [
    {"name": "B&H Photo", "url": "https://www.bhphotovideo.com", "country": "USA", "ships_intl": 1},
    {"name": "Adorama", "url": "https://www.adorama.com", "country": "USA", "ships_intl": 1},
    {"name": "Freestyle Photo", "url": "https://www.freestylephoto.biz", "country": "USA", "ships_intl": 1},
    {"name": "Film Photography Project", "url": "https://filmphotographyproject.com", "country": "USA", "ships_intl": 1},
    {"name": "Analogue Wonderland", "url": "https://analoguewonderland.co.uk", "country": "UK", "ships_intl": 1},
    {"name": "Macodirect", "url": "https://www.macodirect.de", "country": "Germany", "ships_intl": 1},
    {"name": "Japan Camera Hunter", "url": "https://www.japancamerahunter.com", "country": "Japan", "ships_intl": 1},
    {"name": "Moment", "url": "https://www.shopmoment.com", "country": "USA", "ships_intl": 1},
    {"name": "Lomography Shop", "url": "https://shop.lomography.com", "country": "Austria", "ships_intl": 1},
    {"name": "Film Supply Club", "url": "https://filmsupplyclub.com", "country": "USA", "ships_intl": 0},
    {"name": "Pro8mm", "url": "https://www.pro8mm.com", "country": "USA", "ships_intl": 1},
    {"name": "Spectra Film & Video", "url": "https://www.spectrafilmandvideo.com", "country": "USA", "ships_intl": 1},
]

LABS = [
    {"name": "The Darkroom", "city": "San Clemente", "country": "USA", "url": "https://thedarkroom.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Richard Photo Lab", "city": "Hollywood", "country": "USA", "url": "https://richardphotolab.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Indie Film Lab", "city": "Montgomery", "country": "USA", "url": "https://www.indiefilmlab.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "The FIND Lab", "city": "Orem", "country": "USA", "url": "https://thefindlab.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Memphis Film Lab", "city": "Memphis", "country": "USA", "url": "https://www.memphisfilmlab.org", "turnaround": "3-5 days", "mail_in": 1},
    {"name": "Gelatin Labs", "city": "Salt Lake City", "country": "USA", "url": "https://gelatinlabs.com", "turnaround": "3-5 days", "mail_in": 1},
    {"name": "Process One", "city": "Los Angeles", "country": "USA", "url": "https://www.processone.com", "turnaround": "1-3 days", "mail_in": 0},
    {"name": "Carmencita Film Lab", "city": "Valencia", "country": "Spain", "url": "https://carmencitafilmlab.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Mori Film Lab", "city": "Tokyo", "country": "Japan", "url": "https://morifilmlab.com", "turnaround": "3-5 days", "mail_in": 1},
    {"name": "Take It Easy Lab", "city": "Tokyo", "country": "Japan", "url": "https://www.tielab.jp", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Silverpan Lab", "city": "Berlin", "country": "Germany", "url": "https://silverpan.de", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Metro Lab", "city": "Sydney", "country": "Australia", "url": "https://metrolab.com.au", "turnaround": "3-5 days", "mail_in": 1},
    {"name": "Old School Photo Lab", "city": "Dover", "country": "USA", "url": "https://oldschoolphotolab.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Photo Palace", "city": "London", "country": "UK", "url": "https://photopalace.co.uk", "turnaround": "3-5 days", "mail_in": 1},
    {"name": "Canadiana Lab", "city": "Toronto", "country": "Canada", "url": "https://canadianalab.com", "turnaround": "5-7 days", "mail_in": 1},
    # Motion picture / cine labs (US-focused)
    {"name": "Cinelab", "city": "New Bedford", "country": "USA", "url": "https://www.cinelab.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Spectra Film & Video", "city": "North Hollywood", "country": "USA", "url": "https://www.spectrafilmandvideo.com", "turnaround": "3-5 days", "mail_in": 1},
    {"name": "Pro8mm", "city": "Burbank", "country": "USA", "url": "https://www.pro8mm.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Dwayne's Photo", "city": "Parsons", "country": "USA", "url": "https://dwaynesphoto.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Gamma Ray Digital", "city": "Chicago", "country": "USA", "url": "https://gammaraydigital.com", "turnaround": "3-5 days", "mail_in": 1},
    {"name": "Frame Discreet", "city": "Brooklyn", "country": "USA", "url": "https://framediscreet.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Negative Supply Lab", "city": "Rochester", "country": "USA", "url": "https://www.negativesupply.com", "turnaround": "5-7 days", "mail_in": 1},
    {"name": "Yale Film & Video", "city": "Burbank", "country": "USA", "url": "https://yalefilmandvideo.com", "turnaround": "3-5 days", "mail_in": 1},
    {"name": "Mono No Aware", "city": "New York", "country": "USA", "url": "https://mononoawarefilm.com", "turnaround": "5-7 days", "mail_in": 0},
    {"name": "Metropolis Post", "city": "New York", "country": "USA", "url": "http://metpostny.com", "turnaround": "3-5 days", "mail_in": 1},
]

# Prices: map (stock_name, vendor_name) -> (price_usd, in_stock)
# Not every stock at every vendor – a realistic subset
PRICES = [
    # Portra 400 – widely available
    ("Portra 400", "B&H Photo", 11.49, 1), ("Portra 400", "Adorama", 11.49, 1),
    ("Portra 400", "Freestyle Photo", 11.99, 1), ("Portra 400", "Analogue Wonderland", 13.50, 1),
    ("Portra 400", "Moment", 12.99, 1), ("Portra 400", "Macodirect", 12.90, 1),
    # Portra 160
    ("Portra 160", "B&H Photo", 11.49, 1), ("Portra 160", "Adorama", 11.49, 1),
    ("Portra 160", "Freestyle Photo", 11.99, 1), ("Portra 160", "Analogue Wonderland", 13.50, 1),
    # Portra 800
    ("Portra 800", "B&H Photo", 13.99, 1), ("Portra 800", "Adorama", 13.99, 1),
    ("Portra 800", "Analogue Wonderland", 15.50, 1),
    # Ektar 100
    ("Ektar 100", "B&H Photo", 11.49, 1), ("Ektar 100", "Adorama", 11.49, 1),
    ("Ektar 100", "Freestyle Photo", 11.99, 1),
    # Gold 200
    ("Gold 200", "B&H Photo", 8.99, 1), ("Gold 200", "Adorama", 8.99, 1),
    ("Gold 200", "Moment", 9.99, 1), ("Gold 200", "Film Supply Club", 8.50, 1),
    # ColorPlus 200
    ("ColorPlus 200", "B&H Photo", 7.49, 1), ("ColorPlus 200", "Adorama", 7.49, 1),
    ("ColorPlus 200", "Macodirect", 6.90, 1),
    # UltraMax 400
    ("UltraMax 400", "B&H Photo", 8.99, 1), ("UltraMax 400", "Adorama", 8.99, 1),
    ("UltraMax 400", "Moment", 9.99, 1),
    # Vision3 stocks
    ("Vision3 50D", "Film Photography Project", 12.99, 1), ("Vision3 50D", "Freestyle Photo", 13.99, 1),
    ("Vision3 250D", "Film Photography Project", 12.99, 1),
    ("Vision3 500T", "Film Photography Project", 12.99, 1), ("Vision3 500T", "Freestyle Photo", 13.99, 1),
    # Tri-X 400
    ("Tri-X 400", "B&H Photo", 10.49, 1), ("Tri-X 400", "Adorama", 10.49, 1),
    ("Tri-X 400", "Freestyle Photo", 10.99, 1), ("Tri-X 400", "Analogue Wonderland", 12.50, 1),
    # T-Max 100 / 400
    ("T-Max 100", "B&H Photo", 10.49, 1), ("T-Max 100", "Adorama", 10.49, 1),
    ("T-Max 400", "B&H Photo", 10.49, 1), ("T-Max 400", "Adorama", 10.49, 1),
    # Ektachrome E100
    ("Ektachrome E100", "B&H Photo", 16.99, 1), ("Ektachrome E100", "Adorama", 16.99, 1),
    ("Ektachrome E100", "Freestyle Photo", 17.49, 1),
    # HP5 Plus 400
    ("HP5 Plus 400", "B&H Photo", 8.99, 1), ("HP5 Plus 400", "Adorama", 8.99, 1),
    ("HP5 Plus 400", "Freestyle Photo", 8.99, 1), ("HP5 Plus 400", "Analogue Wonderland", 9.50, 1),
    ("HP5 Plus 400", "Macodirect", 8.50, 1),
    # FP4 Plus 125
    ("FP4 Plus 125", "B&H Photo", 8.99, 1), ("FP4 Plus 125", "Adorama", 8.99, 1),
    ("FP4 Plus 125", "Freestyle Photo", 8.99, 1),
    # Delta series
    ("Delta 100", "B&H Photo", 9.49, 1), ("Delta 100", "Freestyle Photo", 9.49, 1),
    ("Delta 400", "B&H Photo", 9.49, 1), ("Delta 400", "Adorama", 9.49, 1),
    ("Delta 3200", "B&H Photo", 12.49, 1), ("Delta 3200", "Adorama", 12.49, 1),
    # Pan F Plus 50
    ("Pan F Plus 50", "B&H Photo", 9.99, 1), ("Pan F Plus 50", "Freestyle Photo", 9.99, 1),
    # XP2 Super 400
    ("XP2 Super 400", "B&H Photo", 10.99, 1), ("XP2 Super 400", "Adorama", 10.99, 1),
    # SFX 200
    ("SFX 200", "B&H Photo", 10.99, 1), ("SFX 200", "Freestyle Photo", 10.99, 1),
    # Fuji Superia X-TRA 400
    ("Superia X-TRA 400", "B&H Photo", 9.99, 1), ("Superia X-TRA 400", "Adorama", 9.99, 0),
    # Fuji C200
    ("C200", "Analogue Wonderland", 11.99, 0), ("C200", "Macodirect", 10.90, 0),
    # Provia 100F / Velvia 50
    ("Provia 100F", "B&H Photo", 14.99, 1), ("Provia 100F", "Adorama", 14.99, 1),
    ("Velvia 50", "B&H Photo", 14.99, 1), ("Velvia 50", "Adorama", 14.99, 0),
    # CineStill
    ("800T", "B&H Photo", 15.99, 1), ("800T", "Adorama", 15.99, 1),
    ("800T", "Freestyle Photo", 15.99, 1), ("800T", "Moment", 16.99, 1),
    ("50D", "B&H Photo", 14.99, 1), ("50D", "Adorama", 14.99, 1),
    ("400D", "B&H Photo", 14.99, 1), ("400D", "Adorama", 14.99, 1),
    ("BwXX", "B&H Photo", 13.99, 1), ("BwXX", "Freestyle Photo", 13.99, 1),
    # Lomography
    ("Color Negative 100", "Lomography Shop", 10.90, 1), ("Color Negative 100", "Freestyle Photo", 11.49, 1),
    ("Color Negative 400", "Lomography Shop", 10.90, 1), ("Color Negative 400", "B&H Photo", 11.49, 1),
    ("Color Negative 800", "Lomography Shop", 11.90, 1), ("Color Negative 800", "B&H Photo", 12.49, 1),
    ("Lady Grey 400", "Lomography Shop", 9.90, 1),
    ("Potsdam 100", "Lomography Shop", 9.90, 1),
    # Fomapan
    ("Fomapan 100", "B&H Photo", 5.99, 1), ("Fomapan 100", "Freestyle Photo", 5.99, 1),
    ("Fomapan 100", "Macodirect", 4.90, 1),
    ("Fomapan 200", "B&H Photo", 5.99, 1), ("Fomapan 200", "Freestyle Photo", 5.99, 1),
    ("Fomapan 400", "B&H Photo", 5.99, 1), ("Fomapan 400", "Freestyle Photo", 5.99, 1),
    # Others
    ("Ortho Plus 80", "B&H Photo", 10.99, 1), ("Ortho Plus 80", "Freestyle Photo", 10.99, 1),
    ("Washi Z", "Japan Camera Hunter", 14.00, 1), ("Washi Z", "Film Photography Project", 15.00, 0),
    # 16mm stocks
    ("Vision3 50D 16mm", "B&H Photo", 54.99, 1), ("Vision3 50D 16mm", "Freestyle Photo", 56.99, 1),
    ("Vision3 50D 16mm", "Spectra Film & Video", 52.00, 1),
    ("Vision3 200T 16mm", "B&H Photo", 54.99, 1), ("Vision3 200T 16mm", "Freestyle Photo", 56.99, 1),
    ("Vision3 250D 16mm", "B&H Photo", 54.99, 1), ("Vision3 250D 16mm", "Freestyle Photo", 56.99, 1),
    ("Vision3 500T 16mm", "B&H Photo", 54.99, 1), ("Vision3 500T 16mm", "Freestyle Photo", 56.99, 1),
    ("Vision3 500T 16mm", "Spectra Film & Video", 52.00, 1),
    ("Double-X 7222 16mm", "B&H Photo", 44.99, 1), ("Double-X 7222 16mm", "Freestyle Photo", 46.99, 1),
    ("Double-X 7222 16mm", "Film Photography Project", 45.00, 1),
    ("Tri-X Reversal 7266 16mm", "B&H Photo", 49.99, 1), ("Tri-X Reversal 7266 16mm", "Freestyle Photo", 51.99, 1),
    ("Ektachrome 100D 7294 16mm", "B&H Photo", 64.99, 1), ("Ektachrome 100D 7294 16mm", "Freestyle Photo", 66.99, 1),
    ("Fomapan R100 16mm", "B&H Photo", 29.99, 1), ("Fomapan R100 16mm", "Freestyle Photo", 29.99, 1),
    ("Fomapan R100 16mm", "Macodirect", 24.90, 1),
    # Super 8 cartridges
    ("Vision3 50D Super 8", "B&H Photo", 34.99, 1), ("Vision3 50D Super 8", "Pro8mm", 36.99, 1),
    ("Vision3 50D Super 8", "Spectra Film & Video", 33.00, 1),
    ("Vision3 200T Super 8", "B&H Photo", 34.99, 1), ("Vision3 200T Super 8", "Pro8mm", 36.99, 1),
    ("Vision3 500T Super 8", "B&H Photo", 34.99, 1), ("Vision3 500T Super 8", "Pro8mm", 36.99, 1),
    ("Vision3 500T Super 8", "Spectra Film & Video", 33.00, 1),
    ("Tri-X Reversal 7266 Super 8", "B&H Photo", 32.99, 1), ("Tri-X Reversal 7266 Super 8", "Pro8mm", 34.99, 1),
    ("Ektachrome 100D Super 8", "B&H Photo", 39.99, 1), ("Ektachrome 100D Super 8", "Pro8mm", 41.99, 1),
    ("Gold 200 Super 8", "B&H Photo", 29.99, 1), ("Gold 200 Super 8", "Pro8mm", 31.99, 1),
]

# Lab services: (lab_name, process, format, dev_price, scan_price)
LAB_SERVICES = [
    # The Darkroom
    ("The Darkroom", "C-41", "35mm", 11.0, 8.0), ("The Darkroom", "C-41", "120", 11.0, 8.0),
    ("The Darkroom", "BW", "35mm", 14.0, 8.0), ("The Darkroom", "BW", "120", 14.0, 8.0),
    ("The Darkroom", "E-6", "35mm", 16.0, 8.0), ("The Darkroom", "E-6", "120", 16.0, 8.0),
    # Richard Photo Lab
    ("Richard Photo Lab", "C-41", "35mm", 14.0, 12.0), ("Richard Photo Lab", "C-41", "120", 14.0, 12.0),
    ("Richard Photo Lab", "BW", "35mm", 16.0, 12.0), ("Richard Photo Lab", "E-6", "35mm", 18.0, 12.0),
    # Indie Film Lab
    ("Indie Film Lab", "C-41", "35mm", 13.0, 11.0), ("Indie Film Lab", "C-41", "120", 13.0, 11.0),
    ("Indie Film Lab", "BW", "35mm", 15.0, 11.0), ("Indie Film Lab", "BW", "120", 15.0, 11.0),
    ("Indie Film Lab", "E-6", "35mm", 17.0, 11.0),
    # The FIND Lab
    ("The FIND Lab", "C-41", "35mm", 14.0, 13.0), ("The FIND Lab", "C-41", "120", 14.0, 13.0),
    ("The FIND Lab", "BW", "35mm", 16.0, 13.0),
    # Memphis Film Lab
    ("Memphis Film Lab", "C-41", "35mm", 10.0, 8.0), ("Memphis Film Lab", "C-41", "120", 10.0, 8.0),
    ("Memphis Film Lab", "BW", "35mm", 12.0, 8.0), ("Memphis Film Lab", "BW", "120", 12.0, 8.0),
    ("Memphis Film Lab", "E-6", "35mm", 15.0, 8.0),
    # Gelatin Labs
    ("Gelatin Labs", "C-41", "35mm", 12.0, 10.0), ("Gelatin Labs", "C-41", "120", 12.0, 10.0),
    ("Gelatin Labs", "BW", "35mm", 14.0, 10.0), ("Gelatin Labs", "E-6", "35mm", 16.0, 10.0),
    # Process One
    ("Process One", "C-41", "35mm", 9.0, 9.0), ("Process One", "C-41", "120", 9.0, 9.0),
    ("Process One", "E-6", "35mm", 14.0, 9.0), ("Process One", "E-6", "120", 14.0, 9.0),
    ("Process One", "BW", "35mm", 12.0, 9.0),
    # Carmencita Film Lab
    ("Carmencita Film Lab", "C-41", "35mm", 12.0, 10.0), ("Carmencita Film Lab", "C-41", "120", 12.0, 10.0),
    ("Carmencita Film Lab", "BW", "35mm", 14.0, 10.0), ("Carmencita Film Lab", "E-6", "35mm", 16.0, 10.0),
    ("Carmencita Film Lab", "ECN-2", "35mm", 18.0, 10.0),
    # Mori Film Lab
    ("Mori Film Lab", "C-41", "35mm", 8.0, 7.0), ("Mori Film Lab", "C-41", "120", 8.0, 7.0),
    ("Mori Film Lab", "BW", "35mm", 10.0, 7.0), ("Mori Film Lab", "E-6", "35mm", 12.0, 7.0),
    # Take It Easy Lab
    ("Take It Easy Lab", "C-41", "35mm", 9.0, 8.0), ("Take It Easy Lab", "C-41", "120", 9.0, 8.0),
    ("Take It Easy Lab", "BW", "35mm", 11.0, 8.0),
    # Silverpan Lab
    ("Silverpan Lab", "BW", "35mm", 10.0, 8.0), ("Silverpan Lab", "BW", "120", 10.0, 8.0),
    ("Silverpan Lab", "C-41", "35mm", 11.0, 8.0),
    # Metro Lab
    ("Metro Lab", "C-41", "35mm", 11.0, 9.0), ("Metro Lab", "C-41", "120", 11.0, 9.0),
    ("Metro Lab", "BW", "35mm", 13.0, 9.0), ("Metro Lab", "E-6", "35mm", 15.0, 9.0),
    # Old School Photo Lab
    ("Old School Photo Lab", "C-41", "35mm", 10.0, 7.0), ("Old School Photo Lab", "C-41", "120", 10.0, 7.0),
    ("Old School Photo Lab", "BW", "35mm", 12.0, 7.0), ("Old School Photo Lab", "BW", "120", 12.0, 7.0),
    ("Old School Photo Lab", "E-6", "35mm", 14.0, 7.0), ("Old School Photo Lab", "ECN-2", "35mm", 16.0, 7.0),
    # Photo Palace
    ("Photo Palace", "C-41", "35mm", 10.0, 8.0), ("Photo Palace", "C-41", "120", 10.0, 8.0),
    ("Photo Palace", "BW", "35mm", 12.0, 8.0), ("Photo Palace", "E-6", "35mm", 14.0, 8.0),
    # Canadiana Lab
    ("Canadiana Lab", "C-41", "35mm", 11.0, 9.0), ("Canadiana Lab", "C-41", "120", 11.0, 9.0),
    ("Canadiana Lab", "BW", "35mm", 13.0, 9.0), ("Canadiana Lab", "E-6", "35mm", 15.0, 9.0),
    # Cinelab – full motion picture lab
    ("Cinelab", "ECN-2", "16mm", 45.0, 55.0), ("Cinelab", "ECN-2", "super8", 35.0, 45.0),
    ("Cinelab", "ECN-2", "35mm", 55.0, 65.0),
    ("Cinelab", "BW", "16mm", 40.0, 55.0), ("Cinelab", "BW", "super8", 30.0, 45.0),
    ("Cinelab", "E-6", "16mm", 50.0, 55.0), ("Cinelab", "E-6", "super8", 40.0, 45.0),
    # Spectra Film & Video
    ("Spectra Film & Video", "ECN-2", "16mm", 40.0, 50.0), ("Spectra Film & Video", "ECN-2", "super8", 30.0, 40.0),
    ("Spectra Film & Video", "BW", "16mm", 35.0, 50.0), ("Spectra Film & Video", "BW", "super8", 28.0, 40.0),
    ("Spectra Film & Video", "E-6", "16mm", 45.0, 50.0), ("Spectra Film & Video", "E-6", "super8", 35.0, 40.0),
    ("Spectra Film & Video", "C-41", "super8", 28.0, 40.0),
    # Pro8mm – Super 8 specialists
    ("Pro8mm", "ECN-2", "super8", 28.0, 38.0), ("Pro8mm", "C-41", "super8", 25.0, 38.0),
    ("Pro8mm", "BW", "super8", 25.0, 38.0), ("Pro8mm", "E-6", "super8", 32.0, 38.0),
    ("Pro8mm", "ECN-2", "16mm", 42.0, 52.0), ("Pro8mm", "BW", "16mm", 38.0, 52.0),
    # Dwayne's Photo
    ("Dwayne's Photo", "C-41", "35mm", 9.0, 7.0), ("Dwayne's Photo", "C-41", "120", 9.0, 7.0),
    ("Dwayne's Photo", "BW", "35mm", 11.0, 7.0), ("Dwayne's Photo", "E-6", "35mm", 13.0, 7.0),
    ("Dwayne's Photo", "ECN-2", "super8", 30.0, 42.0),
    # Gamma Ray Digital
    ("Gamma Ray Digital", "ECN-2", "16mm", 42.0, 50.0), ("Gamma Ray Digital", "ECN-2", "super8", 32.0, 40.0),
    ("Gamma Ray Digital", "BW", "16mm", 38.0, 50.0), ("Gamma Ray Digital", "BW", "super8", 28.0, 40.0),
    ("Gamma Ray Digital", "C-41", "35mm", 10.0, 8.0), ("Gamma Ray Digital", "BW", "35mm", 12.0, 8.0),
    # Frame Discreet
    ("Frame Discreet", "ECN-2", "16mm", 48.0, 55.0), ("Frame Discreet", "ECN-2", "super8", 35.0, 42.0),
    ("Frame Discreet", "BW", "16mm", 42.0, 55.0), ("Frame Discreet", "BW", "super8", 30.0, 42.0),
    ("Frame Discreet", "E-6", "16mm", 52.0, 55.0),
    ("Frame Discreet", "C-41", "35mm", 12.0, 10.0), ("Frame Discreet", "BW", "35mm", 14.0, 10.0),
    # Negative Supply Lab
    ("Negative Supply Lab", "C-41", "35mm", 11.0, 9.0), ("Negative Supply Lab", "C-41", "120", 11.0, 9.0),
    ("Negative Supply Lab", "BW", "35mm", 13.0, 9.0), ("Negative Supply Lab", "E-6", "35mm", 15.0, 9.0),
    # Yale Film & Video
    ("Yale Film & Video", "ECN-2", "16mm", 44.0, 52.0), ("Yale Film & Video", "ECN-2", "super8", 34.0, 42.0),
    ("Yale Film & Video", "BW", "16mm", 40.0, 52.0), ("Yale Film & Video", "BW", "super8", 30.0, 42.0),
    ("Yale Film & Video", "E-6", "16mm", 48.0, 52.0), ("Yale Film & Video", "E-6", "super8", 38.0, 42.0),
    # Add 16mm/super8 services to The Darkroom (they accept it)
    ("The Darkroom", "ECN-2", "super8", 32.0, 40.0), ("The Darkroom", "C-41", "super8", 28.0, 40.0),
    # Mono No Aware
    ("Mono No Aware", "ECN-2", "16mm", 45.0, 52.0), ("Mono No Aware", "ECN-2", "super8", 35.0, 42.0),
    ("Mono No Aware", "BW", "16mm", 40.0, 52.0), ("Mono No Aware", "BW", "super8", 30.0, 42.0),
    ("Mono No Aware", "E-6", "16mm", 48.0, 52.0),
    # Metropolis Post
    ("Metropolis Post", "ECN-2", "16mm", 46.0, 55.0), ("Metropolis Post", "ECN-2", "super8", 34.0, 44.0),
    ("Metropolis Post", "ECN-2", "35mm", 56.0, 65.0),
    ("Metropolis Post", "BW", "16mm", 42.0, 55.0), ("Metropolis Post", "BW", "super8", 32.0, 44.0),
    ("Metropolis Post", "E-6", "16mm", 50.0, 55.0), ("Metropolis Post", "E-6", "super8", 40.0, 44.0),
    ("Metropolis Post", "C-41", "35mm", 12.0, 10.0),
]


def seed():
    conn = db.init_db()

    # Insert stocks
    stock_ids = {}  # name -> id
    for s in STOCKS:
        cur = conn.execute(
            """INSERT OR IGNORE INTO stocks
               (name, brand, type, format, iso, process, description, grain, tone, saturation, latitude, status, best_for)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (s["name"], s["brand"], s["type"], s["format"], s["iso"], s["process"],
             s["description"], s["grain"], s["tone"], s["saturation"], s["latitude"],
             s["status"], s["best_for"]),
        )
        stock_ids[s["name"]] = cur.lastrowid

    # Insert vendors
    vendor_ids = {}
    for v in VENDORS:
        cur = conn.execute(
            "INSERT OR IGNORE INTO vendors (name, url, country, ships_intl) VALUES (?, ?, ?, ?)",
            (v["name"], v["url"], v["country"], v["ships_intl"]),
        )
        vendor_ids[v["name"]] = cur.lastrowid

    # Insert prices
    for stock_name, vendor_name, price, in_stock in PRICES:
        sid = stock_ids.get(stock_name)
        vid = vendor_ids.get(vendor_name)
        if sid and vid:
            conn.execute(
                "INSERT OR IGNORE INTO prices (stock_id, vendor_id, price_usd, in_stock) VALUES (?, ?, ?, ?)",
                (sid, vid, price, in_stock),
            )

    # Insert labs
    lab_ids = {}
    for l in LABS:
        cur = conn.execute(
            "INSERT OR IGNORE INTO labs (name, city, country, url, turnaround, mail_in) VALUES (?, ?, ?, ?, ?, ?)",
            (l["name"], l["city"], l["country"], l["url"], l["turnaround"], l["mail_in"]),
        )
        lab_ids[l["name"]] = cur.lastrowid

    # Insert lab services
    for lab_name, process, fmt, dev_price, scan_price in LAB_SERVICES:
        lid = lab_ids.get(lab_name)
        if lid:
            conn.execute(
                "INSERT OR IGNORE INTO lab_services (lab_id, process, format, dev_price, scan_price) VALUES (?, ?, ?, ?, ?)",
                (lid, process, fmt, dev_price, scan_price),
            )

    conn.commit()
    conn.close()
    print("Database seeded successfully!")
    print(f"  Stocks:       {len(STOCKS)}")
    print(f"  Vendors:      {len(VENDORS)}")
    print(f"  Prices:       {len(PRICES)}")
    print(f"  Labs:         {len(LABS)}")
    print(f"  Lab services: {len(LAB_SERVICES)}")


if __name__ == "__main__":
    seed()
