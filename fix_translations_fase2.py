import json
import os

LOCALES_DIR = "/Users/johnguerrero/chefpro-modernize/src/i18n/locales"

# ============================================================
# GERMAN (de) TRANSLATIONS
# ============================================================
de_toolScore = {
    "seo": {
        "title": "Digitalisierungstest Restaurant Kostenlos | AI Chef Pro",
        "description": "Entdecken Sie in 2 Minuten den Digitalisierungsgrad Ihres Restaurants. 6 Fragen, sofortiges Ergebnis mit personalisiertem Aktionsplan. Kostenlos, ohne Registrierung.",
        "keywords": "digitalisierungstest restaurant, digitales niveau restaurant, digitalisierung gastronomie, digitale werkzeuge restaurant"
    },
    "breadcrumb": "Digitalisierungstest",
    "hero": {
        "badge": "Kostenlos — Keine Registrierung — 2 Minuten",
        "h1": "Digitalisierungstest für Restaurants",
        "subtitle": "Wie digital ist Ihr Restaurant? Beantworten Sie 6 Fragen und erhalten Sie Ihr digitales Niveau mit einem personalisierten Aktionsplan.",
        "cta_tool": "Test machen ↓",
        "cta_premium": "Premium-Plan →"
    },
    "tool": {
        "title": "Digitalisierungstest",
        "question_label": "Frage {n} von {total}",
        "submit": "Mein Ergebnis sehen",
        "result_title": "Ihr Digitalisierungsgrad",
        "score_label": "Punktzahl",
        "restart": "Test wiederholen",
        "cta_after": "Bereit für den digitalen Sprung mit KI?"
    },
    "questions": [
        {"id": 1, "text": "Haben Sie ein Online-Reservierungssystem?", "options": ["Nein, nur telefonisch", "Ja, über Drittanbieter (TheFork, etc.)", "Ja, auf unserer eigenen Website", "Ja, auf Website + eigener App"]},
        {"id": 2, "text": "Wie verwalten Sie Lieferbestellungen?", "options": ["Wir machen keine Lieferung", "Nur über Plattformen (Lieferando, etc.)", "Plattformen + eigene Website", "Eigenes System integriert mit Küche"]},
        {"id": 3, "text": "Verwenden Sie Verwaltungssoftware (POS)?", "options": ["Nein, wir verwenden Papier/manuelle Kasse", "Einfaches POS ohne Berichte", "POS mit Verkaufsberichten", "POS integriert mit Lager, Buchhaltung und Lieferung"]},
        {"id": 4, "text": "Wie verwalten Sie Ihre Speisekarte?", "options": ["Gedruckte Karte, die selten aktualisiert wird", "PDF oder Bild auf Website/WhatsApp", "Digitale Karte mit aktualisierbarem QR", "Digitale Karte + KI für Vorschläge"]},
        {"id": 5, "text": "Haben Sie eine Präsenz in sozialen Medien?", "options": ["Wir haben keine sozialen Medien", "Profil erstellt, aber ohne regelmäßige Aktivität", "Wir posten 1-2 Mal pro Woche", "Aktive Strategie + digitale Werbung"]},
        {"id": 6, "text": "Verwenden Sie KI-Tools in Ihrem Restaurant?", "options": ["Nein, ich kenne sie nicht", "Ich habe einige ausprobiert, nutze sie aber nicht regelmäßig", "Ich nutze KI gelegentlich (ChatGPT, etc.)", "Ich habe eine KI-Suite in meinen Betrieb integriert"]}
    ],
    "results": [
        {"range": [0, 25], "level": "Analog", "emoji": "📋", "description": "Ihr Restaurant arbeitet auf traditionelle Weise. Es gibt eine große Differenzierungschance mit einfachen Digitalisierungsschritten.", "tips": ["Beginnen Sie mit einem Google Business-Profil", "Fügen Sie eine kostenlose QR-Speisekarte hinzu", "Erstellen Sie ein Profil bei TheFork oder ähnlichem"]},
        {"range": [26, 50], "level": "Digital Basis", "emoji": "📱", "description": "Sie haben erste Schritte unternommen. Sie haben eine digitale Präsenz, aber es gibt wichtige Tools, die Sie noch nicht nutzen.", "tips": ["Aktivieren Sie Online-Reservierungen auf Ihrer Website", "Integrieren Sie Ihr POS mit dem Lieferservice", "Beginnen Sie, KI für Inhalte zu nutzen"]},
        {"range": [51, 75], "level": "Digital Fortgeschritten", "emoji": "🚀", "description": "Ihr Restaurant ist gut digitalisiert. Sie liegen über dem Branchendurchschnitt. Jetzt ist der Moment, KI zu integrieren.", "tips": ["Automatisieren Sie Bewertungsantworten mit KI", "Nutzen Sie KI zur Optimierung von Preisen und Menü", "Zentralisieren Sie alle Kanäle in einem Dashboard"]},
        {"range": [76, 100], "level": "Digital Pro", "emoji": "⭐", "description": "Sie sind ein Digitalisierungsvorbild in der Branche. Sie nutzen Technologie, um Effizienz und Rentabilität zu maximieren.", "tips": ["Erkunden Sie prädiktive KI für den Lagerbestand", "Implementieren Sie erweiterte Datenanalyse", "Erwägen Sie Mentoring für andere Restaurants"]}
    ],
    "how_it_works": {
        "title": "So funktioniert es",
        "steps": [
            {"step": "1", "title": "6 Fragen beantworten", "description": "Fragen zu Reservierungen, Lieferung, POS, Speisekarte, sozialen Medien und KI. Ehrlich, ohne Registrierung."},
            {"step": "2", "title": "Ihre Punktzahl erhalten", "description": "Der Test berechnet Ihren Digitalisierungsgrad: Analog, Basis, Fortgeschritten oder Pro."},
            {"step": "3", "title": "Aktionsplan", "description": "Sie erhalten 3 konkrete Empfehlungen, um auf das nächste Niveau zu gelangen."}
        ]
    },
    "benefits": {
        "title": "Warum diesen Test machen",
        "items": ["Identifizieren Sie genau, wo Sie stehen", "Vergleichen Sie sich mit dem Branchendurchschnitt", "Entdecken Sie die wirkungsvollsten Tools", "Verbesserungsplan in 3 konkreten Schritten"]
    },
    "testimonial": {
        "quote": "Ich dachte, ich sei ziemlich digital aufgestellt. Der Test zeigte mir wichtige Lücken bei der Lieferverwaltung und KI. In 3 Monaten setzte ich die Empfehlungen um und verbesserte meine Marge um 8 %.",
        "name": "Michael Wagner",
        "role": "Inhaber, Gastronomiegruppe Zum Goldenen Anker, München"
    },
    "pricing": {
        "title": "Bringen Sie Ihre Digitalisierung mit AI Chef Pro auf die nächste Stufe",
        "subtitle": "Der Test sagt Ihnen, wo Sie stehen. AI Chef Pro gibt Ihnen die Werkzeuge, um weiter zu kommen.",
        "plans": [
            {"name": "Kostenlos", "price": "0€/Monat", "uses": "5 Nutzungen/Monat", "highlight": False},
            {"name": "Premium Pro", "price": "25€/Monat", "uses": "150 Nutzungen/Monat", "highlight": False},
            {"name": "Premium Plus", "price": "50€/Monat", "uses": "350 Nutzungen/Monat", "highlight": True},
            {"name": "Premium Max", "price": "95€/Monat", "uses": "Unbegrenzt", "highlight": False}
        ]
    },
    "faq_section": {"title": "Häufige Fragen zur Digitalisierung in der Gastronomie"},
    "faq": [
        {"question": "Was bedeutet Digitalisierung in einem Restaurant?", "answer": "Digitalisierung in der Gastronomie ist der Prozess der Einführung technologischer Tools für eine bessere Verwaltung von Reservierungen, Lieferung, POS, Kundenkommunikation und internen Abläufen. Es reicht von einer einfachen QR-Speisekarte bis hin zur Verwaltung mit künstlicher Intelligenz."},
        {"question": "Wie hoch ist der durchschnittliche Digitalisierungsgrad von Restaurants in Deutschland?", "answer": "Laut Branchenstudien haben weniger als 30 % der Restaurants in Deutschland ein fortgeschrittenes Digitalisierungsniveau. Die meisten befinden sich auf einem Basisniveau und verwenden nur einzelne Tools ohne Integration."},
        {"question": "Warum ist es wichtig, mein Restaurant zu digitalisieren?", "answer": "Digitalisierte Restaurants haben eine 20-35 % höhere Betriebseffizienz, geringere Personalfluktuation und ein besseres Kundenerlebnis. Außerdem ermöglicht KI eine deutliche Reduzierung der Food-Cost- und Marketingkosten."},
        {"question": "Wie kann ich mit der Digitalisierung meines Restaurants beginnen?", "answer": "Der erste Schritt ist zu wissen, wo Sie stehen: Dafür gibt es diesen Test. Auf Basis des Ergebnisses können Sie die wirkungsvollsten Tools priorisieren. AI Chef Pro bietet einen sehr zugänglichen Einstieg in die KI für die Gastronomie."}
    ],
    "cta_section": {
        "title": "Digitalisieren Sie Ihr Restaurant noch heute mit KI",
        "subtitle": "AI Chef Pro ist die umfassendste KI-Suite für die Gastronomie: 55+ Tools zur Verwaltung Ihres Restaurants mit künstlicher Intelligenz.",
        "primary": "AI Chef Pro kostenlos testen",
        "secondary": "Alle Pläne ansehen"
    }
}

de_toolAlergenos = {
    "seo": {
        "title": "Allergenkontrolle Restaurant Kostenlos | AI Chef Pro",
        "description": "Erkennen Sie die 14 deklarationspflichtigen Allergene in jedem Gericht sofort. Geben Sie die Zutaten ein und erhalten Sie die Allergendeklaration. Kostenlos, ohne Registrierung.",
        "keywords": "allergenkontrolle restaurant, pflichtallergene restaurant, allergendeklaration gericht, verordnung 1169 2011"
    },
    "breadcrumb": "Allergendetektor",
    "hero": {
        "badge": "Kostenlos — Keine Registrierung — Gesetzlich vorgeschrieben",
        "h1": "Allergendetektor für Restaurants",
        "subtitle": "Identifizieren Sie die 14 deklarationspflichtigen Allergene (EU-Verordnung 1169/2011) in jedem Gericht sofort. Kopieren Sie die Deklaration für Ihre Speisekarte.",
        "cta_tool": "Zum Detektor ↓",
        "cta_premium": "Premium-Plan →"
    },
    "tool": {
        "title": "Allergendetektor",
        "input_label": "Zutaten des Gerichts",
        "input_placeholder": "Schreiben Sie die Zutaten durch Kommas getrennt. Z.B.: Weizenmehl, Ei, Milch, Butter, Hefe, Salz...",
        "dish_name_label": "Name des Gerichts (optional)",
        "dish_name_placeholder": "Z.B.: Zwiebelsuppe",
        "detect": "Allergene erkennen",
        "result_title": "Erkannte Allergene",
        "allergens_found": "Vorhandene Allergene",
        "no_allergens": "✅ Es wurden keine deklarationspflichtigen Allergene erkannt",
        "warning": "⚠️ Immer manuell prüfen — dieses Tool ist orientierend",
        "legal_note": "Pflichtdeklaration gemäß EU-Verordnung 1169/2011",
        "copy": "Deklaration kopieren",
        "copied": "Kopiert!",
        "reset": "Neue Analyse",
        "cta_after": "Möchten Sie die Allergene Ihrer gesamten Speisekarte automatisch verwalten?",
        "allergens_title": "Die 14 deklarationspflichtigen Allergene",
        "allergens_subtitle": "Verordnung (EU) 1169/2011"
    },
    "allergens": [
        {"id": "gluten", "name": "Gluten", "emoji": "🌾", "description": "Getreide, das Gluten enthält: Weizen, Roggen, Gerste, Hafer...", "keywords": ["Weizen", "Mehl", "Weizenmehl", "Brot", "Nudeln", "Pasta", "Roggen", "Gerste", "Hafer", "Dinkel", "Grieß", "Bulgur", "Couscous", "Kamut", "Bier"]},
        {"id": "crustaceos", "name": "Krebstiere", "emoji": "🦐", "description": "Garnelen, Krabben, Hummer, Langusten...", "keywords": ["Garnele", "Shrimp", "Krabbe", "Krebs", "Hummer", "Languste", "Garnelen", "Krebstier"]},
        {"id": "huevos", "name": "Eier", "emoji": "🥚", "description": "Eier und Eiprodukte", "keywords": ["Ei", "Eier", "Eigelb", "Eiweiß", "Mayonnaise", "Omelette", "Rührei"]},
        {"id": "pescado", "name": "Fisch", "emoji": "🐟", "description": "Alle Fischarten und Derivate", "keywords": ["Lachs", "Kabeljau", "Thunfisch", "Dorsch", "Forelle", "Sardine", "Anchovi", "Fisch", "Flunder", "Heilbutt"]},
        {"id": "cacahuetes", "name": "Erdnüsse", "emoji": "🥜", "description": "Erdnüsse und Erdnussprodukte", "keywords": ["Erdnuss", "Erdnüsse", "Erdnussbutter", "Arachide"]},
        {"id": "soja", "name": "Soja", "emoji": "🫘", "description": "Soja und Sojaprodukte", "keywords": ["Soja", "Sojasoße", "Tofu", "Miso", "Edamame", "Sojamilch", "Sojaöl"]},
        {"id": "lacteos", "name": "Milch", "emoji": "🥛", "description": "Milch und Milchprodukte", "keywords": ["Milch", "Käse", "Butter", "Sahne", "Joghurt", "Quark", "Milchpulver", "Laktose", "Mozzarella", "Parmesan", "Frischkäse"]},
        {"id": "frutos_secos", "name": "Schalenfrüchte", "emoji": "🌰", "description": "Mandeln, Haselnüsse, Walnüsse, Cashews, Pistazien...", "keywords": ["Mandel", "Haselnuss", "Walnuss", "Cashew", "Pistazie", "Macadamia", "Pekannuss", "Paranuss", "Nuss", "Nüsse"]},
        {"id": "apio", "name": "Sellerie", "emoji": "🌿", "description": "Sellerie und Sellerieprodukte", "keywords": ["Sellerie", "Staudensellerie", "Knollensellerie", "Selleriesalz"]},
        {"id": "mostaza", "name": "Senf", "emoji": "🌻", "description": "Senf und Senfprodukte", "keywords": ["Senf", "Senfkörner", "Senfmehl", "Senfsauce"]},
        {"id": "sesamo", "name": "Sesam", "emoji": "🌱", "description": "Sesamsamen und Sesamprodukte", "keywords": ["Sesam", "Sesamsamen", "Sesamöl", "Tahin", "Tahini", "Hummus"]},
        {"id": "sulfitos", "name": "Schwefeldioxid und Sulfite", "emoji": "🍷", "description": "Konzentration über 10 mg/kg oder 10 mg/Liter", "keywords": ["Wein", "Essig", "Trockenfrüchte", "Rosinen", "Aprikosen", "Sulfit", "Sulfite", "Schwefel"]},
        {"id": "altramuces", "name": "Lupinen", "emoji": "🌾", "description": "Lupinen und Lupinenprodukte", "keywords": ["Lupine", "Lupinenmehl", "Lupinensamen"]},
        {"id": "moluscos", "name": "Weichtiere", "emoji": "🦑", "description": "Muscheln, Austern, Schnecken, Tintenfisch, Kalmar...", "keywords": ["Muschel", "Auster", "Schnecke", "Tintenfisch", "Kalmar", "Oktopus", "Venusmuschel"]}
    ],
    "how_it_works": {
        "title": "So funktioniert es",
        "steps": [
            {"step": "1", "title": "Zutaten eingeben", "description": "Geben Sie alle Zutaten Ihres Gerichts durch Kommas getrennt ein, so wie Sie sie einkaufen."},
            {"step": "2", "title": "Automatische Erkennung", "description": "Der Detektor identifiziert, welche Allergene der EU-Verordnung 1169/2011 in den Zutaten vorhanden sind."},
            {"step": "3", "title": "Deklaration kopieren", "description": "Erhalten Sie die Allergendeklaration, die Sie in Ihre Speisekarte, Website oder Ihr Verwaltungssystem einfügen können."}
        ]
    },
    "benefits": {
        "title": "Warum den Allergendetektor verwenden",
        "items": ["Erfüllen Sie die EU-Verordnung 1169/2011 (Pflicht)", "Schützen Sie Ihre Kunden mit Allergien", "Vermeiden Sie Bußgelder von bis zu 600.000 €", "Deklaration bereit für Ihre digitale Speisekarte"]
    },
    "testimonial": {
        "quote": "Nach einer Inspektion sagte mir der Inspektor, dass unsere Allergendeklaration vorbildlich sei. Wir verwenden dieses Tool, um jedes Gericht zu überprüfen, bevor wir es in die Speisekarte aufnehmen.",
        "name": "Maria Schneider",
        "role": "Küchenchefin, Restaurant Zur alten Mühle, Hamburg"
    },
    "pricing": {
        "title": "Komplette Allergenverwaltung mit AI Chef Pro",
        "subtitle": "Der Basisdetektor ist kostenlos. Mit AI Chef Pro verwalten Sie die Allergene Ihrer gesamten Speisekarte mit automatischen Warnungen.",
        "plans": [
            {"name": "Kostenlos", "price": "0€/Monat", "uses": "5 Nutzungen/Monat", "highlight": False},
            {"name": "Premium Pro", "price": "25€/Monat", "uses": "150 Nutzungen/Monat", "highlight": False},
            {"name": "Premium Plus", "price": "50€/Monat", "uses": "350 Nutzungen/Monat", "highlight": True},
            {"name": "Premium Max", "price": "95€/Monat", "uses": "Unbegrenzt", "highlight": False}
        ]
    },
    "faq_section": {"title": "Häufige Fragen zu Allergenen in der Gastronomie"},
    "faq": [
        {"question": "Was sagt das Gesetz über Allergene in Restaurants?", "answer": "Die EU-Verordnung 1169/2011 verpflichtet alle Restaurants, Bars und Gaststätten, über die 14 deklarationspflichtigen Allergene in allen Gerichten zu informieren. Verstöße können Bußgelder zwischen 3.000 € und 600.000 € nach sich ziehen."},
        {"question": "Was sind die 14 deklarationspflichtigen Allergene?", "answer": "Gluten, Krebstiere, Eier, Fisch, Erdnüsse, Soja, Milch, Schalenfrüchte (Mandeln, Walnüsse, Haselnüsse...), Sellerie, Senf, Sesam, Schwefeldioxid und Sulfite, Lupinen und Weichtiere."},
        {"question": "Reicht ein allgemeiner Hinweis 'kann Spuren enthalten' aus?", "answer": "Nein. Das Gesetz verlangt spezifische Informationen pro Gericht. Ein allgemeiner Hinweis reicht nicht aus und kann mit einem Bußgeld belegt werden. Sie müssen den Kunden über die in jedem konkreten Gericht enthaltenen Allergene informieren können."},
        {"question": "Ist dieses Tool 100 % rechtlich zuverlässig?", "answer": "Dieses Tool ist orientierend und zur Unterstützung gedacht. Die rechtliche Verantwortung liegt immer beim Betrieb. Sie müssen die Zutaten und mögliche Kreuzkontaminationen manuell überprüfen. Für eine vollständige und geprüfte Verwaltung verwenden Sie AI Chef Pro Premium."}
    ],
    "cta_section": {
        "title": "Verwalten Sie die Allergene Ihrer gesamten Speisekarte mit KI",
        "subtitle": "Mit AI Chef Pro verwalten Sie die Allergene jedes Gerichts automatisch, mit Warnungen bei Zutatenänderungen und exportierbarer Deklaration für Ihre Speisekarte.",
        "primary": "AI Chef Pro kostenlos testen",
        "secondary": "Alle Pläne ansehen"
    }
}

de_toolBrigada = {
    "seo": {
        "title": "Brigaderechner Küche Kostenlos | AI Chef Pro",
        "description": "Berechnen Sie, wie viele Mitarbeiter Sie in Küche und Service benötigen. Kostenlos, ohne Registrierung. Basierend auf echten Gastronomiestandards.",
        "keywords": "brigaderechner küche, wie viele köche brauche ich, personal restaurant, brigade gastronomie"
    },
    "breadcrumb": "Brigaderechner",
    "hero": {
        "badge": "Kostenlos — Keine Registrierung",
        "h1": "Küchenbrigaderechner",
        "subtitle": "Erfahren Sie, wie viele Köche und Kellner Sie je nach Ihrer Gästeanzahl, Schichten und Serviceart benötigen. Basierend auf echten Branchenquoten.",
        "cta_tool": "Zum Rechner ↓",
        "cta_premium": "Premium-Plan →"
    },
    "tool": {
        "title": "Brigaderechner",
        "covers_label": "Gäste pro Service",
        "covers_hint": "Maximale Anzahl der Gäste in einem Service (Mittag- oder Abendessen)",
        "service_type_label": "Serviceart",
        "service_types": ["À la carte (hohe Komplexität)", "Tagesmenü / Bistró", "Buffet / Self-Service", "Catering / Bankette"],
        "services_per_day_label": "Services pro Tag",
        "services_options": ["1 Service (nur Mittag oder Abend)", "2 Services (Mittag + Abend)", "3 Services (Frühstück + Mittag + Abend)"],
        "has_delivery_label": "Machen Sie Lieferung?",
        "delivery_volume_label": "Lieferbestellungen/Tag",
        "calculate": "Brigade berechnen",
        "result_title": "Ihre empfohlene Brigade",
        "kitchen_title": "👨‍🍳 Küche",
        "sala_title": "🍽️ Service",
        "head_chef": "Küchenchef",
        "sous_chef": "Sous-Chef",
        "chef_partida": "Posten-Chef",
        "cocinero": "Koch",
        "ayudante": "Küchenhelfer",
        "kitchen_porter": "Spüler / Office",
        "maitre": "Maître / Oberkellner",
        "jefe_rango": "Stationsleiter",
        "camarero": "Kellner",
        "ayudante_sala": "Servicehilfe",
        "total_kitchen": "Gesamt Küche",
        "total_sala": "Gesamt Service",
        "total_staff": "Gesamtpersonal",
        "ratio_label": "Gäste-Kellner-Verhältnis",
        "reset": "Neue Berechnung",
        "cta_after": "Möchten Sie die Personalkosten Ihres Restaurants optimieren?"
    },
    "how_it_works": {
        "title": "So funktioniert es",
        "steps": [
            {"step": "1", "title": "Ihr Volumen angeben", "description": "Anzahl der Gäste pro Service, Serviceart und Anzahl der täglichen Services."},
            {"step": "2", "title": "Berechnung nach Standards", "description": "Der Rechner wendet die echten Branchenquoten für jede Serviceart an."},
            {"step": "3", "title": "Empfohlene Brigade", "description": "Sie erhalten die Aufschlüsselung der Stellen in Küche und Service mit der empfohlenen Mindestanzahl für jede Rolle."}
        ]
    },
    "benefits": {
        "title": "Warum Ihre Brigade berechnen",
        "items": ["Vermeiden Sie eine überdimensionierte Belegschaft (unnötige Kosten)", "Vermeiden Sie eine unterdimensionierte Belegschaft (schlechter Service)", "Kennen Sie die Standardquoten für Ihren Restauranttyp", "Objektive Grundlage für Verhandlungen mit Ihrem Team"]
    },
    "testimonial": {
        "quote": "Ich hatte 4 Köche für 60 Gäste mit Tagesmenü. Der Rechner zeigte mir, dass 3 gut organisierte Köche ausreichend waren. Ich sparte 1.800 €/Monat an Gehältern.",
        "name": "Klaus Müller",
        "role": "Inhaber, Restaurant Am Marktplatz, Stuttgart"
    },
    "pricing": {
        "title": "Optimieren Sie Ihr Team mit AI Chef Pro",
        "subtitle": "Der Basisrechner ist kostenlos. Mit AI Chef Pro optimieren Sie Schichten, Personalkosten und Produktivität Ihrer Brigade.",
        "plans": [
            {"name": "Kostenlos", "price": "0€/Monat", "uses": "5 Nutzungen/Monat", "highlight": False},
            {"name": "Premium Pro", "price": "25€/Monat", "uses": "150 Nutzungen/Monat", "highlight": False},
            {"name": "Premium Plus", "price": "50€/Monat", "uses": "350 Nutzungen/Monat", "highlight": True},
            {"name": "Premium Max", "price": "95€/Monat", "uses": "Unbegrenzt", "highlight": False}
        ]
    },
    "faq_section": {"title": "Häufige Fragen zur Küchengruppe"},
    "faq": [
        {"question": "Wie viele Köche brauche ich für 50 Gäste?", "answer": "Das hängt von der Serviceart ab. Für À-la-carte (hohe Komplexität) benötigen Sie etwa 4-5 Köche für 50 Gäste. Für Tagesmenü können 2-3 gut organisierte Köche ausreichend sein."},
        {"question": "Was ist die Standardquote von Kellnern pro Gast?", "answer": "Der Branchenstandard ist 1 Kellner pro 10-15 Gäste im À-la-carte-Restaurant und 1 pro 15-20 im Tagesmenü oder Bistró. Für Fine Dining kann es auf 1 pro 6-8 Gäste sinken."},
        {"question": "Was ist eine Küchenbrigade?", "answer": "Die Küchenbrigade ist das hierarchisch organisierte Team, das in einer professionellen Küche arbeitet. Sie wurde von Auguste Escoffier systematisiert. Sie umfasst Rollen wie Küchenchef, Sous-Chef, Posten-Chefs, Köche und Helfer."},
        {"question": "Wie reduziere ich Personalkosten ohne Qualitätsverlust?", "answer": "Der Schlüssel liegt in der Organisation: vielseitige Brigaden, effiziente Mise en Place, gutes Schichtenmanagement und KI-Tools zur Betriebsoptimierung. AI Chef Pro hilft Ihnen, die Engpässe in Ihrem Team zu identifizieren."}
    ],
    "cta_section": {
        "title": "Optimieren Sie das Management Ihres Teams mit KI",
        "subtitle": "AI Chef Pro hilft Ihnen, Schichten zu verwalten, Personalkosten zu berechnen und die Produktivität Ihrer Brigade zu optimieren.",
        "primary": "AI Chef Pro kostenlos testen",
        "secondary": "Alle Pläne ansehen"
    }
}

# ============================================================
# ITALIAN (it) TRANSLATIONS
# ============================================================
it_toolScore = {
    "seo": {
        "title": "Test Digitalizzazione Ristorante Gratis | AI Chef Pro",
        "description": "Scopri in 2 minuti il livello di digitalizzazione del tuo ristorante. 6 domande, risultato immediato con piano d'azione personalizzato. Gratis, senza registrazione.",
        "keywords": "test digitalizzazione ristorante, livello digitale ristorante, digitalizzazione ristorazione, strumenti digitali ristorante"
    },
    "breadcrumb": "Test di Digitalizzazione",
    "hero": {
        "badge": "Gratis — Senza registrazione — 2 minuti",
        "h1": "Test di Digitalizzazione per Ristoranti",
        "subtitle": "Quanto è digitalizzato il tuo ristorante? Rispondi a 6 domande e ottieni il tuo livello digitale con un piano d'azione personalizzato.",
        "cta_tool": "Fai il test ↓",
        "cta_premium": "Piano Premium →"
    },
    "tool": {
        "title": "Test di Digitalizzazione",
        "question_label": "Domanda {n} di {total}",
        "submit": "Vedi il mio risultato",
        "result_title": "Il tuo livello di digitalizzazione",
        "score_label": "Punteggio",
        "restart": "Ripeti il test",
        "cta_after": "Pronto per il salto digitale con l'IA?"
    },
    "questions": [
        {"id": 1, "text": "Hai un sistema di prenotazione online?", "options": ["No, solo telefonicamente", "Sì, tramite terzi (TheFork, ecc.)", "Sì, sul nostro sito web", "Sì, sul sito + app propria"]},
        {"id": 2, "text": "Come gestisci gli ordini di delivery?", "options": ["Non facciamo delivery", "Solo tramite piattaforme (Glovo, Deliveroo...)", "Piattaforme + sito web proprio", "Sistema proprio integrato con la cucina"]},
        {"id": 3, "text": "Usi un software gestionale (POS)?", "options": ["No, usiamo carta/cassa manuale", "POS base senza report", "POS con report di vendita", "POS integrato con magazzino, contabilità e delivery"]},
        {"id": 4, "text": "Come gestisci il tuo menu?", "options": ["Menu stampato che aggiorniamo raramente", "PDF o immagine su sito/WhatsApp", "Menu digitale con QR aggiornabile", "Menu digitale + IA per i suggerimenti"]},
        {"id": 5, "text": "Hai presenza sui social media?", "options": ["Non abbiamo social media", "Profilo creato ma senza attività regolare", "Pubblichiamo 1-2 volte a settimana", "Strategia attiva + pubblicità digitale"]},
        {"id": 6, "text": "Usi strumenti di IA nel tuo ristorante?", "options": ["No, non li conosco", "Ne ho provati alcuni ma non li uso regolarmente", "Uso l'IA occasionalmente (ChatGPT, ecc.)", "Ho una suite IA integrata nella mia operazione"]}
    ],
    "results": [
        {"range": [0, 25], "level": "Analogico", "emoji": "📋", "description": "Il tuo ristorante funziona in modo tradizionale. C'è una grande opportunità di differenziazione con semplici passi di digitalizzazione.", "tips": ["Inizia con un profilo Google Business", "Aggiungi un menu QR gratuito", "Crea un profilo su TheFork o simili"]},
        {"range": [26, 50], "level": "Digitale Base", "emoji": "📱", "description": "Hai fatto i primi passi. Hai una presenza digitale ma ci sono strumenti chiave che non stai ancora sfruttando.", "tips": ["Attiva le prenotazioni online sul tuo sito", "Integra il tuo POS con il delivery", "Inizia a usare l'IA per i contenuti"]},
        {"range": [51, 75], "level": "Digitale Avanzato", "emoji": "🚀", "description": "Il tuo ristorante è ben digitalizzato. Sei sopra la media del settore. Ora è il momento di integrare l'IA.", "tips": ["Automatizza le risposte alle recensioni con l'IA", "Usa l'IA per ottimizzare prezzi e menu", "Centralizza tutti i canali in una dashboard"]},
        {"range": [76, 100], "level": "Digitale Pro", "emoji": "⭐", "description": "Sei un punto di riferimento nella digitalizzazione del settore. Stai usando la tecnologia per massimizzare efficienza e redditività.", "tips": ["Esplora l'IA predittiva per il magazzino", "Implementa analisi dei dati avanzata", "Considera il mentoring per altri ristoranti"]}
    ],
    "how_it_works": {
        "title": "Come funziona",
        "steps": [
            {"step": "1", "title": "Rispondi a 6 domande", "description": "Domande su prenotazioni, delivery, POS, menu, social media e IA. Senza trucchi, senza registrazione."},
            {"step": "2", "title": "Ottieni il tuo punteggio", "description": "Il test calcola il tuo livello di digitalizzazione: Analogico, Base, Avanzato o Pro."},
            {"step": "3", "title": "Piano d'azione", "description": "Ricevi 3 raccomandazioni concrete per passare al livello successivo."}
        ]
    },
    "benefits": {
        "title": "Perché fare questo test",
        "items": ["Identifica esattamente dove ti trovi", "Confrontati con la media del settore", "Scopri gli strumenti con più impatto", "Piano di miglioramento in 3 passi concreti"]
    },
    "testimonial": {
        "quote": "Pensavo di essere abbastanza digitalizzato. Il test mi ha mostrato lacune importanti nella gestione del delivery e nell'IA. In 3 mesi ho implementato le raccomandazioni e migliorato il mio margine dell'8%.",
        "name": "Marco Ricci",
        "role": "Proprietario, Gruppo Gastronomico Il Porto, Napoli"
    },
    "pricing": {
        "title": "Porta la tua digitalizzazione al livello successivo con AI Chef Pro",
        "subtitle": "Il test ti dice dove sei. AI Chef Pro ti dà gli strumenti per andare più lontano.",
        "plans": [
            {"name": "Gratuito", "price": "0€/mese", "uses": "5 utilizzi/mese", "highlight": False},
            {"name": "Premium Pro", "price": "25€/mese", "uses": "150 utilizzi/mese", "highlight": False},
            {"name": "Premium Plus", "price": "50€/mese", "uses": "350 utilizzi/mese", "highlight": True},
            {"name": "Premium Max", "price": "95€/mese", "uses": "Illimitato", "highlight": False}
        ]
    },
    "faq_section": {"title": "Domande frequenti sulla digitalizzazione nella ristorazione"},
    "faq": [
        {"question": "Cosa significa digitalizzazione in un ristorante?", "answer": "La digitalizzazione nella ristorazione è il processo di incorporazione di strumenti tecnologici per gestire meglio prenotazioni, delivery, POS, comunicazione con i clienti e operazioni interne. Va da un semplice menu QR alla gestione con intelligenza artificiale."},
        {"question": "Qual è il livello medio di digitalizzazione dei ristoranti in Italia?", "answer": "Secondo studi del settore, meno del 30% dei ristoranti in Italia ha un livello avanzato di digitalizzazione. La maggior parte si trova a un livello base, usando solo strumenti separati senza integrazione."},
        {"question": "Perché è importante digitalizzare il mio ristorante?", "answer": "I ristoranti digitalizzati hanno una efficienza operativa del 20-35% superiore, minore rotazione del personale e migliore esperienza del cliente. Inoltre, l'IA permette di ridurre significativamente i costi di food cost e marketing."},
        {"question": "Come posso iniziare a digitalizzare il mio ristorante?", "answer": "Il primo passo è sapere dove ti trovi: per questo esiste questo test. Dal risultato, puoi dare priorità agli strumenti con maggior impatto. AI Chef Pro offre un punto di ingresso molto accessibile per l'IA nella gastronomia."}
    ],
    "cta_section": {
        "title": "Digitalizza il tuo ristorante con l'IA oggi stesso",
        "subtitle": "AI Chef Pro è la suite IA più completa per la gastronomia: 55+ strumenti per gestire il tuo ristorante con intelligenza artificiale.",
        "primary": "Prova AI Chef Pro gratis",
        "secondary": "Vedi tutti i piani"
    }
}

it_toolAlergenos = {
    "seo": {
        "title": "Rilevatore Allergeni Ristorante Gratis | AI Chef Pro",
        "description": "Rileva i 14 allergeni a dichiarazione obbligatoria in qualsiasi piatto all'istante. Inserisci gli ingredienti e ottieni la scheda allergeni. Gratis, senza registrazione.",
        "keywords": "rilevatore allergeni ristorante, allergeni obbligatori ristorante, scheda allergeni piatto, regolamento 1169 2011"
    },
    "breadcrumb": "Rilevatore Allergeni",
    "hero": {
        "badge": "Gratis — Senza registrazione — Obbligatorio per legge",
        "h1": "Rilevatore di Allergeni per Ristoranti",
        "subtitle": "Identifica i 14 allergeni a dichiarazione obbligatoria (Regolamento UE 1169/2011) in qualsiasi piatto all'istante. Copia la scheda per il tuo menu.",
        "cta_tool": "Vai al rilevatore ↓",
        "cta_premium": "Piano Premium →"
    },
    "tool": {
        "title": "Rilevatore di Allergeni",
        "input_label": "Ingredienti del piatto",
        "input_placeholder": "Scrivi gli ingredienti separati da virgole. Es: farina di frumento, uovo, latte, burro, lievito, sale...",
        "dish_name_label": "Nome del piatto (opzionale)",
        "dish_name_placeholder": "Es: Pasta al pomodoro",
        "detect": "Rileva Allergeni",
        "result_title": "Allergeni rilevati",
        "allergens_found": "Allergeni presenti",
        "no_allergens": "✅ Non sono stati rilevati allergeni a dichiarazione obbligatoria",
        "warning": "⚠️ Verifica sempre manualmente — questo strumento è orientativo",
        "legal_note": "Dichiarazione obbligatoria ai sensi del Regolamento UE 1169/2011",
        "copy": "Copia scheda",
        "copied": "Copiato!",
        "reset": "Nuova analisi",
        "cta_after": "Vuoi gestire gli allergeni di tutto il tuo menu in modo automatico?",
        "allergens_title": "I 14 allergeni a dichiarazione obbligatoria",
        "allergens_subtitle": "Regolamento (UE) 1169/2011"
    },
    "allergens": [
        {"id": "gluten", "name": "Glutine", "emoji": "🌾", "description": "Cereali contenenti glutine: grano, segale, orzo, avena...", "keywords": ["grano", "frumento", "farina", "pane", "pasta", "segale", "orzo", "avena", "farro", "semola", "couscous", "bulgur", "kamut", "birra"]},
        {"id": "crustaceos", "name": "Crostacei", "emoji": "🦐", "description": "Gamberi, granchi, aragoste, astici...", "keywords": ["gambero", "gamberetto", "granchio", "aragosta", "astice", "scampo", "crostaceo"]},
        {"id": "huevos", "name": "Uova", "emoji": "🥚", "description": "Uova e prodotti derivati", "keywords": ["uovo", "uova", "tuorlo", "albume", "maionese", "frittata", "uovo sodo"]},
        {"id": "pescado", "name": "Pesce", "emoji": "🐟", "description": "Tutti i tipi di pesce e derivati", "keywords": ["salmone", "merluzzo", "tonno", "trota", "sardina", "acciuga", "pesce", "rombo", "platessa"]},
        {"id": "cacahuetes", "name": "Arachidi", "emoji": "🥜", "description": "Arachidi e prodotti derivati", "keywords": ["arachide", "arachidi", "burro di arachidi"]},
        {"id": "soja", "name": "Soia", "emoji": "🫘", "description": "Soia e prodotti derivati", "keywords": ["soia", "salsa di soia", "tofu", "miso", "edamame", "latte di soia"]},
        {"id": "lacteos", "name": "Latte", "emoji": "🥛", "description": "Latte e prodotti lattiero-caseari", "keywords": ["latte", "formaggio", "burro", "panna", "yogurt", "lattosio", "mozzarella", "parmigiano", "ricotta", "besciamella"]},
        {"id": "frutos_secos", "name": "Frutta a guscio", "emoji": "🌰", "description": "Mandorle, nocciole, noci, anacardi, pistacchi...", "keywords": ["mandorla", "nocciola", "noce", "anacardo", "pistacchio", "macadamia", "noci", "frutta secca"]},
        {"id": "apio", "name": "Sedano", "emoji": "🌿", "description": "Sedano e prodotti derivati", "keywords": ["sedano", "sedano rapa", "sale di sedano"]},
        {"id": "mostaza", "name": "Senape", "emoji": "🌻", "description": "Senape e prodotti derivati", "keywords": ["senape", "semi di senape", "salsa di senape"]},
        {"id": "sesamo", "name": "Sesamo", "emoji": "🌱", "description": "Semi di sesamo e prodotti derivati", "keywords": ["sesamo", "semi di sesamo", "olio di sesamo", "tahini", "tahin", "hummus"]},
        {"id": "sulfitos", "name": "Anidride solforosa e solfiti", "emoji": "🍷", "description": "Concentrazione superiore a 10 mg/kg o 10 mg/litro", "keywords": ["vino", "aceto", "frutta secca", "uvetta", "albicocche secche", "solfiti", "anidride solforosa"]},
        {"id": "altramuces", "name": "Lupini", "emoji": "🌾", "description": "Lupini e prodotti derivati", "keywords": ["lupino", "lupini", "farina di lupino"]},
        {"id": "moluscos", "name": "Molluschi", "emoji": "🦑", "description": "Cozze, ostriche, lumache, polpo, calamaro...", "keywords": ["cozza", "ostrica", "lumaca", "polpo", "calamaro", "seppia", "vongola", "mollusco"]}
    ],
    "how_it_works": {
        "title": "Come funziona",
        "steps": [
            {"step": "1", "title": "Inserisci gli ingredienti", "description": "Inserisci tutti gli ingredienti del tuo piatto separati da virgole, così come li acquisti."},
            {"step": "2", "title": "Rilevamento automatico", "description": "Il rilevatore identifica quali allergeni del Regolamento UE 1169/2011 sono presenti negli ingredienti."},
            {"step": "3", "title": "Copia la scheda", "description": "Ottieni la scheda allergeni pronta per aggiungere al tuo menu, sito web o sistema gestionale."}
        ]
    },
    "benefits": {
        "title": "Perché usare il rilevatore di allergeni",
        "items": ["Rispetta il Regolamento UE 1169/2011 (obbligatorio)", "Proteggi i tuoi clienti con allergie", "Evita sanzioni fino a 600.000 €", "Scheda pronta per il tuo menu digitale"]
    },
    "testimonial": {
        "quote": "Dopo un'ispezione, l'ispettore mi ha detto che la nostra dichiarazione degli allergeni era esemplare. Usiamo questo strumento per verificare ogni piatto prima di aggiungerlo al menu.",
        "name": "Giulia Ferretti",
        "role": "Chef Proprietaria, Ristorante La Vigna, Toscana"
    },
    "pricing": {
        "title": "Gestione completa degli allergeni con AI Chef Pro",
        "subtitle": "Il rilevatore base è gratuito. Con AI Chef Pro gestisci gli allergeni di tutto il tuo menu con avvisi automatici.",
        "plans": [
            {"name": "Gratuito", "price": "0€/mese", "uses": "5 utilizzi/mese", "highlight": False},
            {"name": "Premium Pro", "price": "25€/mese", "uses": "150 utilizzi/mese", "highlight": False},
            {"name": "Premium Plus", "price": "50€/mese", "uses": "350 utilizzi/mese", "highlight": True},
            {"name": "Premium Max", "price": "95€/mese", "uses": "Illimitato", "highlight": False}
        ]
    },
    "faq_section": {"title": "Domande frequenti sugli allergeni nella ristorazione"},
    "faq": [
        {"question": "Cosa dice la legge sugli allergeni nei ristoranti?", "answer": "Il Regolamento UE 1169/2011 obbliga tutti i ristoranti, bar e locali di ristorazione a informare sui 14 allergeni a dichiarazione obbligatoria in tutti i piatti. Il mancato rispetto può comportare sanzioni tra 3.000 € e 600.000 € a seconda della gravità."},
        {"question": "Quali sono i 14 allergeni a dichiarazione obbligatoria?", "answer": "Glutine, crostacei, uova, pesce, arachidi, soia, latte, frutta a guscio (mandorle, noci, nocciole...), sedano, senape, sesamo, anidride solforosa e solfiti, lupini e molluschi."},
        {"question": "È sufficiente un avviso generico 'può contenere tracce'?", "answer": "No. La legge richiede informazioni specifiche per piatto. Un avviso generico non è sufficiente e può essere sanzionato. Devi poter informare il cliente di quali allergeni contiene ogni piatto specifico."},
        {"question": "Questo strumento è affidabile al 100% dal punto di vista legale?", "answer": "Questo strumento è orientativo e di supporto. La responsabilità legale ricade sempre sull'esercizio. Devi verificare manualmente gli ingredienti e le possibili contaminazioni crociate. Per una gestione completa e certificata, usa AI Chef Pro Premium."}
    ],
    "cta_section": {
        "title": "Gestisci gli allergeni di tutto il tuo menu con l'IA",
        "subtitle": "Con AI Chef Pro gestisci gli allergeni di ogni piatto automaticamente, con avvisi quando cambi ingredienti e scheda esportabile per il tuo menu.",
        "primary": "Prova AI Chef Pro gratis",
        "secondary": "Vedi tutti i piani"
    }
}

it_toolBrigada = {
    "seo": {
        "title": "Calcolatore Brigata Cucina Gratis | AI Chef Pro",
        "description": "Calcola quanti dipendenti hai bisogno in cucina e in sala in base al tuo volume di servizio. Gratis, senza registrazione. Basato su standard reali della ristorazione.",
        "keywords": "calcolatore brigata cucina, quanti cuochi mi servono, personale ristorante, brigata ristorazione"
    },
    "breadcrumb": "Calcolatore Brigata",
    "hero": {
        "badge": "Gratis — Senza registrazione",
        "h1": "Calcolatore di Brigata di Cucina",
        "subtitle": "Scopri quanti cuochi e camerieri hai bisogno in base ai tuoi coperti, turni e tipo di servizio. Basato su ratio reali del settore.",
        "cta_tool": "Vai al calcolatore ↓",
        "cta_premium": "Piano Premium →"
    },
    "tool": {
        "title": "Calcolatore di Brigata",
        "covers_label": "Coperti per servizio",
        "covers_hint": "Numero massimo di coperti in un servizio (pranzo o cena)",
        "service_type_label": "Tipo di servizio",
        "service_types": ["Alla carta (alta complessità)", "Menu del giorno / Bistrot", "Buffet / Self-service", "Catering / Banchetti"],
        "services_per_day_label": "Servizi al giorno",
        "services_options": ["1 servizio (solo pranzo o cena)", "2 servizi (pranzo + cena)", "3 servizi (colazione + pranzo + cena)"],
        "has_delivery_label": "Fate delivery?",
        "delivery_volume_label": "Ordini delivery/giorno",
        "calculate": "Calcola Brigata",
        "result_title": "La tua brigata consigliata",
        "kitchen_title": "👨‍🍳 Cucina",
        "sala_title": "🍽️ Sala",
        "head_chef": "Chef di Cucina",
        "sous_chef": "Sous Chef",
        "chef_partida": "Chef di Partita",
        "cocinero": "Cuoco",
        "ayudante": "Aiuto Cuoco",
        "kitchen_porter": "Lavapiatti / Office",
        "maitre": "Maître / Responsabile di Sala",
        "jefe_rango": "Capo Rango",
        "camarero": "Cameriere",
        "ayudante_sala": "Aiuto Cameriere",
        "total_kitchen": "Totale cucina",
        "total_sala": "Totale sala",
        "total_staff": "Totale personale",
        "ratio_label": "Rapporto coperti/cameriere",
        "reset": "Nuovo calcolo",
        "cta_after": "Vuoi ottimizzare il costo del personale del tuo ristorante?"
    },
    "how_it_works": {
        "title": "Come funziona",
        "steps": [
            {"step": "1", "title": "Indica il tuo volume", "description": "Numero di coperti per servizio, tipo di servizio e quanti servizi fai al giorno."},
            {"step": "2", "title": "Calcolo secondo gli standard", "description": "Il calcolatore applica i ratio reali del settore della ristorazione per ogni tipo di servizio."},
            {"step": "3", "title": "Brigata consigliata", "description": "Ottieni il dettaglio dei ruoli in cucina e sala con il numero minimo consigliato per ogni ruolo."}
        ]
    },
    "benefits": {
        "title": "Perché calcolare la tua brigata",
        "items": ["Evita di sovradimensionare il personale (costo inutile)", "Evita di sottodimensionarlo (servizio scadente)", "Conosci i ratio standard per il tuo tipo di ristorante", "Base obiettiva per le trattative con il tuo team"]
    },
    "testimonial": {
        "quote": "Avevo 4 cuochi per 60 coperti con menu del giorno. Il calcolatore mi ha mostrato che con 3 ben organizzati era sufficiente. Ho risparmiato 1.800 €/mese in stipendi.",
        "name": "Giuseppe Marino",
        "role": "Proprietario, Ristorante Il Belvedere, Roma"
    },
    "pricing": {
        "title": "Ottimizza il tuo team con AI Chef Pro",
        "subtitle": "Il calcolatore base è gratuito. Con AI Chef Pro ottimizzi turni, costi del personale e produttività della tua brigata.",
        "plans": [
            {"name": "Gratuito", "price": "0€/mese", "uses": "5 utilizzi/mese", "highlight": False},
            {"name": "Premium Pro", "price": "25€/mese", "uses": "150 utilizzi/mese", "highlight": False},
            {"name": "Premium Plus", "price": "50€/mese", "uses": "350 utilizzi/mese", "highlight": True},
            {"name": "Premium Max", "price": "95€/mese", "uses": "Illimitato", "highlight": False}
        ]
    },
    "faq_section": {"title": "Domande frequenti sulla brigata di cucina"},
    "faq": [
        {"question": "Quanti cuochi mi servono per 50 coperti?", "answer": "Dipende dal tipo di servizio. Per la carta (alta complessità) servono circa 4-5 cuochi per 50 coperti. Per il menu del giorno, 2-3 cuochi ben organizzati possono essere sufficienti."},
        {"question": "Qual è il ratio standard di camerieri per coperti?", "answer": "Lo standard del settore è 1 cameriere ogni 10-15 coperti nel ristorante alla carta, e 1 ogni 15-20 nel menu del giorno o bistrot. Per il fine dining può scendere a 1 ogni 6-8 coperti."},
        {"question": "Cos'è una brigata di cucina?", "answer": "La brigata di cucina è il team organizzato gerarchicamente che lavora in una cucina professionale. Fu sistematizzata da Auguste Escoffier. Include ruoli come Chef di Cucina, Sous Chef, Chef di Partita, Cuochi e Aiutanti."},
        {"question": "Come riduco i costi del personale senza abbassare la qualità?", "answer": "La chiave è nell'organizzazione: brigate polivalenti, mise en place efficiente, buona gestione dei turni e uso di strumenti IA per ottimizzare l'operazione. AI Chef Pro ti aiuta a identificare i colli di bottiglia nel tuo team."}
    ],
    "cta_section": {
        "title": "Ottimizza la gestione del tuo team con l'IA",
        "subtitle": "AI Chef Pro ti aiuta a gestire i turni, calcolare i costi del personale e ottimizzare la produttività della tua brigata.",
        "primary": "Prova AI Chef Pro gratis",
        "secondary": "Vedi tutti i piani"
    }
}

# ============================================================
# PORTUGUESE / European (pt) TRANSLATIONS
# ============================================================
pt_toolScore = {
    "seo": {
        "title": "Teste Digitalização Restaurante Grátis | AI Chef Pro",
        "description": "Descubra em 2 minutos o nível de digitalização do seu restaurante. 6 perguntas, resultado imediato com plano de ação personalizado. Grátis, sem registo.",
        "keywords": "teste digitalização restaurante, nível digital restaurante, digitalização restauração, ferramentas digitais restaurante"
    },
    "breadcrumb": "Teste de Digitalização",
    "hero": {
        "badge": "Grátis — Sem registo — 2 minutos",
        "h1": "Teste de Digitalização para Restaurantes",
        "subtitle": "Quão digitalizado está o seu restaurante? Responda a 6 perguntas e obtenha o seu nível digital com um plano de ação personalizado.",
        "cta_tool": "Fazer o teste ↓",
        "cta_premium": "Plano Premium →"
    },
    "tool": {
        "title": "Teste de Digitalização",
        "question_label": "Pergunta {n} de {total}",
        "submit": "Ver o meu resultado",
        "result_title": "O seu nível de digitalização",
        "score_label": "Pontuação",
        "restart": "Repetir teste",
        "cta_after": "Pronto para o salto digital com IA?"
    },
    "questions": [
        {"id": 1, "text": "Tem um sistema de reservas online?", "options": ["Não, apenas por telefone", "Sim, através de terceiros (TheFork, etc.)", "Sim, no nosso próprio website", "Sim, no website + app própria"]},
        {"id": 2, "text": "Como gere os pedidos de entrega ao domicílio?", "options": ["Não fazemos entregas", "Apenas por plataformas (Glovo, Uber Eats...)", "Plataformas + website próprio", "Sistema próprio integrado com a cozinha"]},
        {"id": 3, "text": "Usa algum software de gestão (POS)?", "options": ["Não, usamos papel/caixa manual", "POS básico sem relatórios", "POS com relatórios de vendas", "POS integrado com stock, contabilidade e entrega"]},
        {"id": 4, "text": "Como gere a sua ementa?", "options": ["Ementa impressa que actualizamos raramente", "PDF ou imagem no website/WhatsApp", "Ementa digital com QR actualizável", "Ementa digital + IA para sugestões"]},
        {"id": 5, "text": "Tem presença nas redes sociais?", "options": ["Não temos redes sociais", "Perfil criado mas sem actividade regular", "Publicamos 1-2 vezes por semana", "Estratégia activa + publicidade digital"]},
        {"id": 6, "text": "Usa ferramentas de IA no seu restaurante?", "options": ["Não, não as conheço", "Experimentei algumas mas não as uso regularmente", "Uso IA pontualmente (ChatGPT, etc.)", "Tenho uma suite de IA integrada na minha operação"]}
    ],
    "results": [
        {"range": [0, 25], "level": "Analógico", "emoji": "📋", "description": "O seu restaurante funciona de forma tradicional. Há uma grande oportunidade de diferenciação com passos simples de digitalização.", "tips": ["Comece com um perfil Google Business", "Adicione uma ementa QR gratuita", "Crie um perfil no TheFork ou similar"]},
        {"range": [26, 50], "level": "Digital Básico", "emoji": "📱", "description": "Deu os primeiros passos. Tem presença digital mas há ferramentas-chave que ainda não está a aproveitar.", "tips": ["Active as reservas online no seu website", "Integre o seu POS com a entrega ao domicílio", "Comece a usar IA para conteúdos"]},
        {"range": [51, 75], "level": "Digital Avançado", "emoji": "🚀", "description": "O seu restaurante está bem digitalizado. Está acima da média do sector. Agora é o momento de integrar IA.", "tips": ["Automatize as respostas a avaliações com IA", "Use IA para optimizar preços e ementa", "Centralize todos os canais num dashboard"]},
        {"range": [76, 100], "level": "Digital Pro", "emoji": "⭐", "description": "É uma referência de digitalização no sector. Está a usar a tecnologia para maximizar eficiência e rentabilidade.", "tips": ["Explore IA preditiva para stock", "Implemente análise de dados avançada", "Considere mentoria para outros restaurantes"]}
    ],
    "how_it_works": {
        "title": "Como funciona",
        "steps": [
            {"step": "1", "title": "Responda a 6 perguntas", "description": "Perguntas sobre reservas, entregas, POS, ementa, redes sociais e IA. Sem armadilhas, sem registo."},
            {"step": "2", "title": "Obtenha a sua pontuação", "description": "O teste calcula o seu nível de digitalização: Analógico, Básico, Avançado ou Pro."},
            {"step": "3", "title": "Plano de ação", "description": "Recebe 3 recomendações concretas para subir ao nível seguinte."}
        ]
    },
    "benefits": {
        "title": "Porquê fazer este teste",
        "items": ["Identifique exactamente onde está", "Compare-se com a média do sector", "Descubra as ferramentas de maior impacto", "Plano de melhoria em 3 passos concretos"]
    },
    "testimonial": {
        "quote": "Pensava que estava bastante digitalizado. O teste mostrou-me lacunas importantes na gestão de entregas e IA. Em 3 meses implementei as recomendações e melhorei a minha margem em 8%.",
        "name": "João Ferreira",
        "role": "Proprietário, Grupo Gastronómico O Solar, Porto"
    },
    "pricing": {
        "title": "Leve a sua digitalização ao próximo nível com AI Chef Pro",
        "subtitle": "O teste diz-lhe onde está. AI Chef Pro dá-lhe as ferramentas para ir mais longe.",
        "plans": [
            {"name": "Grátis", "price": "0€/mês", "uses": "5 utilizações/mês", "highlight": False},
            {"name": "Premium Pro", "price": "25€/mês", "uses": "150 utilizações/mês", "highlight": False},
            {"name": "Premium Plus", "price": "50€/mês", "uses": "350 utilizações/mês", "highlight": True},
            {"name": "Premium Max", "price": "95€/mês", "uses": "Ilimitado", "highlight": False}
        ]
    },
    "faq_section": {"title": "Perguntas frequentes sobre digitalização na restauração"},
    "faq": [
        {"question": "O que significa digitalização num restaurante?", "answer": "A digitalização na restauração é o processo de incorporação de ferramentas tecnológicas para gerir melhor reservas, entregas, POS, comunicação com clientes e operações internas. Vai desde uma simples ementa QR até à gestão com inteligência artificial."},
        {"question": "Qual é o nível médio de digitalização dos restaurantes em Portugal?", "answer": "Segundo estudos do sector, menos de 30% dos restaurantes em Portugal têm um nível avançado de digitalização. A maioria está num nível básico, usando apenas ferramentas separadas sem integração."},
        {"question": "Porque é importante digitalizar o meu restaurante?", "answer": "Os restaurantes digitalizados têm uma eficiência operacional 20-35% superior, menor rotação de pessoal e melhor experiência do cliente. Além disso, a IA permite reduzir significativamente os custos de food cost e marketing."},
        {"question": "Como posso começar a digitalizar o meu restaurante?", "answer": "O primeiro passo é saber onde está: para isso existe este teste. A partir do resultado, pode priorizar as ferramentas de maior impacto. AI Chef Pro oferece um ponto de entrada muito acessível para a IA na gastronomia."}
    ],
    "cta_section": {
        "title": "Digitalize o seu restaurante com IA hoje mesmo",
        "subtitle": "AI Chef Pro é a suite de IA mais completa para gastronomia: 55+ ferramentas para gerir o seu restaurante com inteligência artificial.",
        "primary": "Experimentar AI Chef Pro grátis",
        "secondary": "Ver todos os planos"
    }
}

pt_toolAlergenos = {
    "seo": {
        "title": "Detector Alergénios Restaurante Grátis | AI Chef Pro",
        "description": "Detecte os 14 alergénios de declaração obrigatória em qualquer prato instantaneamente. Introduza os ingredientes e obtenha a ficha de alergénios. Grátis, sem registo.",
        "keywords": "detector alergénios restaurante, alergénios obrigatórios restaurante, ficha alergénios prato, regulamento 1169 2011"
    },
    "breadcrumb": "Detector de Alergénios",
    "hero": {
        "badge": "Grátis — Sem registo — Obrigatório por lei",
        "h1": "Detector de Alergénios para Restaurantes",
        "subtitle": "Identifique os 14 alergénios de declaração obrigatória (Regulamento UE 1169/2011) em qualquer prato instantaneamente. Copie a ficha para a sua ementa.",
        "cta_tool": "Ir ao detector ↓",
        "cta_premium": "Plano Premium →"
    },
    "tool": {
        "title": "Detector de Alergénios",
        "input_label": "Ingredientes do prato",
        "input_placeholder": "Escreva os ingredientes separados por vírgulas. Ex: farinha de trigo, ovo, leite, manteiga, fermento, sal...",
        "dish_name_label": "Nome do prato (opcional)",
        "dish_name_placeholder": "Ex: Bacalhau à Brás",
        "detect": "Detectar Alergénios",
        "result_title": "Alergénios detectados",
        "allergens_found": "Alergénios presentes",
        "no_allergens": "✅ Não foram detectados alergénios de declaração obrigatória",
        "warning": "⚠️ Verifique sempre manualmente — esta ferramenta é orientativa",
        "legal_note": "Declaração obrigatória nos termos do Regulamento UE 1169/2011",
        "copy": "Copiar ficha",
        "copied": "Copiado!",
        "reset": "Nova análise",
        "cta_after": "Quer gerir os alergénios de toda a sua ementa de forma automática?",
        "allergens_title": "Os 14 alergénios de declaração obrigatória",
        "allergens_subtitle": "Regulamento (UE) 1169/2011"
    },
    "allergens": [
        {"id": "gluten", "name": "Glúten", "emoji": "🌾", "description": "Cereais que contêm glúten: trigo, centeio, cevada, aveia...", "keywords": ["trigo", "farinha", "pão", "massa", "centeio", "cevada", "aveia", "espelta", "sêmola", "cuscuz", "bulgur", "cerveja", "kamut"]},
        {"id": "crustaceos", "name": "Crustáceos", "emoji": "🦐", "description": "Camarão, caranguejo, lagosta, lagostim...", "keywords": ["camarão", "caranguejo", "lagosta", "lagostim", "gambas", "crustáceo"]},
        {"id": "huevos", "name": "Ovos", "emoji": "🥚", "description": "Ovos e produtos derivados", "keywords": ["ovo", "ovos", "gema", "clara", "maionese", "omeleta", "ovo cozido"]},
        {"id": "pescado", "name": "Peixe", "emoji": "🐟", "description": "Todos os tipos de peixe e derivados", "keywords": ["salmão", "bacalhau", "atum", "truta", "sardinha", "anchova", "peixe", "linguado", "robalo"]},
        {"id": "cacahuetes", "name": "Amendoins", "emoji": "🥜", "description": "Amendoins e produtos derivados", "keywords": ["amendoim", "manteiga de amendoim"]},
        {"id": "soja", "name": "Soja", "emoji": "🫘", "description": "Soja e produtos derivados", "keywords": ["soja", "molho de soja", "tofu", "miso", "edamame", "leite de soja"]},
        {"id": "lacteos", "name": "Leite", "emoji": "🥛", "description": "Leite e produtos lácteos", "keywords": ["leite", "queijo", "manteiga", "natas", "iogurte", "lactose", "mozzarella", "parmesão", "requeijão", "nata", "béchamel"]},
        {"id": "frutos_secos", "name": "Frutos de casca rija", "emoji": "🌰", "description": "Amêndoas, avelãs, nozes, cajus, pistácios...", "keywords": ["amêndoa", "avelã", "noz", "caju", "pistácio", "macadâmia", "nozes", "frutos secos"]},
        {"id": "apio", "name": "Aipo", "emoji": "🌿", "description": "Aipo e produtos derivados", "keywords": ["aipo", "aipo-rábano", "sal de aipo"]},
        {"id": "mostaza", "name": "Mostarda", "emoji": "🌻", "description": "Mostarda e produtos derivados", "keywords": ["mostarda", "sementes de mostarda", "molho de mostarda"]},
        {"id": "sesamo", "name": "Sésamo", "emoji": "🌱", "description": "Sementes de sésamo e produtos derivados", "keywords": ["sésamo", "sementes de sésamo", "óleo de sésamo", "tahini", "tahin", "húmus"]},
        {"id": "sulfitos", "name": "Dióxido de enxofre e sulfitos", "emoji": "🍷", "description": "Concentração superior a 10 mg/kg ou 10 mg/litro", "keywords": ["vinho", "vinagre", "frutos secos", "uvas passas", "damascos secos", "sulfitos", "dióxido de enxofre"]},
        {"id": "altramuces", "name": "Tremoços", "emoji": "🌾", "description": "Tremoços e produtos derivados", "keywords": ["tremoço", "farinha de tremoço", "sementes de tremoço"]},
        {"id": "moluscos", "name": "Moluscos", "emoji": "🦑", "description": "Mexilhão, ostra, caracol, polvo, lula...", "keywords": ["mexilhão", "ostra", "caracol", "polvo", "lula", "choco", "amêijoa", "molusco"]}
    ],
    "how_it_works": {
        "title": "Como funciona",
        "steps": [
            {"step": "1", "title": "Escreva os ingredientes", "description": "Introduza todos os ingredientes do seu prato separados por vírgulas, tal como os compra."},
            {"step": "2", "title": "Detecção automática", "description": "O detector identifica quais os alergénios do Regulamento UE 1169/2011 presentes nos ingredientes."},
            {"step": "3", "title": "Copie a ficha", "description": "Obtenha a ficha de alergénios pronta para adicionar à sua ementa, website ou sistema de gestão."}
        ]
    },
    "benefits": {
        "title": "Porquê usar o detector de alergénios",
        "items": ["Cumpra o Regulamento UE 1169/2011 (obrigatório)", "Proteja os seus clientes com alergias", "Evite coimas de até 600.000 €", "Ficha pronta para incluir na sua ementa digital"]
    },
    "testimonial": {
        "quote": "Após uma inspecção, o inspector disse-me que a nossa declaração de alergénios era exemplar. Usamos esta ferramenta para verificar cada prato antes de o adicionar à ementa.",
        "name": "Ana Sousa",
        "role": "Chef Proprietária, Restaurante Quinta das Flores, Lisboa"
    },
    "pricing": {
        "title": "Gestão completa de alergénios com AI Chef Pro",
        "subtitle": "O detector básico é gratuito. Com AI Chef Pro gere os alergénios de toda a sua ementa com alertas automáticos.",
        "plans": [
            {"name": "Grátis", "price": "0€/mês", "uses": "5 utilizações/mês", "highlight": False},
            {"name": "Premium Pro", "price": "25€/mês", "uses": "150 utilizações/mês", "highlight": False},
            {"name": "Premium Plus", "price": "50€/mês", "uses": "350 utilizações/mês", "highlight": True},
            {"name": "Premium Max", "price": "95€/mês", "uses": "Ilimitado", "highlight": False}
        ]
    },
    "faq_section": {"title": "Perguntas frequentes sobre alergénios na restauração"},
    "faq": [
        {"question": "O que diz a lei sobre alergénios nos restaurantes?", "answer": "O Regulamento UE 1169/2011 obriga todos os restaurantes, bares e estabelecimentos de restauração a informar sobre os 14 alergénios de declaração obrigatória em todos os seus pratos. O incumprimento pode acarretar coimas entre 3.000 € e 600.000 € conforme a gravidade."},
        {"question": "Quais são os 14 alergénios de declaração obrigatória?", "answer": "Glúten, crustáceos, ovos, peixe, amendoins, soja, leite, frutos de casca rija (amêndoas, nozes, avelãs...), aipo, mostarda, sésamo, dióxido de enxofre e sulfitos, tremoços e moluscos."},
        {"question": "É suficiente um aviso genérico 'pode conter vestígios'?", "answer": "Não. A lei exige informação específica por prato. Um aviso genérico não é suficiente e pode ser sancionado. Deve poder informar o cliente sobre quais os alergénios que cada prato concreto contém."},
        {"question": "Esta ferramenta é 100% fiável do ponto de vista legal?", "answer": "Esta ferramenta é orientativa e de apoio. A responsabilidade legal recai sempre sobre o estabelecimento. Deve verificar manualmente os ingredientes e possíveis contaminações cruzadas. Para uma gestão completa e auditada, use AI Chef Pro Premium."}
    ],
    "cta_section": {
        "title": "Gira os alergénios de toda a sua ementa com IA",
        "subtitle": "Com AI Chef Pro gere os alergénios de cada prato automaticamente, com alertas quando muda ingredientes e ficha exportável para a sua ementa.",
        "primary": "Experimentar AI Chef Pro grátis",
        "secondary": "Ver todos os planos"
    }
}

pt_toolBrigada = {
    "seo": {
        "title": "Calculadora Brigada Cozinha Grátis | AI Chef Pro",
        "description": "Calcule quantos funcionários precisa na cozinha e na sala segundo o seu volume de serviço. Grátis, sem registo. Baseado em padrões reais da restauração.",
        "keywords": "calculadora brigada cozinha, quantos cozinheiros preciso, pessoal restaurante, brigada restauração"
    },
    "breadcrumb": "Calculadora de Brigada",
    "hero": {
        "badge": "Grátis — Sem registo",
        "h1": "Calculadora de Brigada de Cozinha",
        "subtitle": "Descubra quantos cozinheiros e empregados de mesa precisa segundo os seus talheres, turnos e tipo de serviço. Baseado em rácios reais do sector.",
        "cta_tool": "Ir à calculadora ↓",
        "cta_premium": "Plano Premium →"
    },
    "tool": {
        "title": "Calculadora de Brigada",
        "covers_label": "Talheres por serviço",
        "covers_hint": "Número máximo de talheres num serviço (almoço ou jantar)",
        "service_type_label": "Tipo de serviço",
        "service_types": ["À la carte (alta complexidade)", "Menu do dia / Bistrô", "Buffet / Self-service", "Catering / Banquetes"],
        "services_per_day_label": "Serviços por dia",
        "services_options": ["1 serviço (só almoço ou jantar)", "2 serviços (almoço + jantar)", "3 serviços (pequeno-almoço + almoço + jantar)"],
        "has_delivery_label": "Faz entregas ao domicílio?",
        "delivery_volume_label": "Pedidos de entrega/dia",
        "calculate": "Calcular Brigada",
        "result_title": "A sua brigada recomendada",
        "kitchen_title": "👨‍🍳 Cozinha",
        "sala_title": "🍽️ Sala",
        "head_chef": "Chefe de Cozinha",
        "sous_chef": "Sous Chef",
        "chef_partida": "Chefe de Partida",
        "cocinero": "Cozinheiro",
        "ayudante": "Ajudante de Cozinha",
        "kitchen_porter": "Lavador / Office",
        "maitre": "Maître / Chefe de Sala",
        "jefe_rango": "Chefe de Rango",
        "camarero": "Empregado de Mesa",
        "ayudante_sala": "Ajudante de Sala",
        "total_kitchen": "Total cozinha",
        "total_sala": "Total sala",
        "total_staff": "Total de pessoal",
        "ratio_label": "Rácio talheres/empregado de mesa",
        "reset": "Novo cálculo",
        "cta_after": "Quer optimizar o custo de pessoal do seu restaurante?"
    },
    "how_it_works": {
        "title": "Como funciona",
        "steps": [
            {"step": "1", "title": "Indique o seu volume", "description": "Número de talheres por serviço, tipo de serviço e quantos serviços faz por dia."},
            {"step": "2", "title": "Cálculo segundo padrões", "description": "A calculadora aplica os rácios reais do sector da restauração para cada tipo de serviço."},
            {"step": "3", "title": "Brigada recomendada", "description": "Obtém a descrição dos postos na cozinha e sala com o número mínimo recomendado para cada função."}
        ]
    },
    "benefits": {
        "title": "Porquê calcular a sua brigada",
        "items": ["Evite sobredimensionar o pessoal (custo desnecessário)", "Evite subdimensioná-lo (serviço deficiente)", "Conheça os rácios padrão para o seu tipo de restaurante", "Base objectiva para negociações com a sua equipa"]
    },
    "testimonial": {
        "quote": "Tinha 4 cozinheiros para 60 talheres com menu do dia. A calculadora mostrou-me que com 3 bem organizados era suficiente. Pousei 1.800 €/mês em salários.",
        "name": "Carlos Silva",
        "role": "Proprietário, Restaurante O Miradouro, Coimbra"
    },
    "pricing": {
        "title": "Optimize a sua equipa com AI Chef Pro",
        "subtitle": "A calculadora básica é gratuita. Com AI Chef Pro optimiza turnos, custos de pessoal e produtividade da sua brigada.",
        "plans": [
            {"name": "Grátis", "price": "0€/mês", "uses": "5 utilizações/mês", "highlight": False},
            {"name": "Premium Pro", "price": "25€/mês", "uses": "150 utilizações/mês", "highlight": False},
            {"name": "Premium Plus", "price": "50€/mês", "uses": "350 utilizações/mês", "highlight": True},
            {"name": "Premium Max", "price": "95€/mês", "uses": "Ilimitado", "highlight": False}
        ]
    },
    "faq_section": {"title": "Perguntas frequentes sobre brigada de cozinha"},
    "faq": [
        {"question": "Quantos cozinheiros preciso para 50 talheres?", "answer": "Depende do tipo de serviço. Para à la carte (alta complexidade) precisa de cerca de 4-5 cozinheiros para 50 talheres. Para menu do dia, com 2-3 cozinheiros bem organizados pode ser suficiente."},
        {"question": "Qual é o rácio padrão de empregados de mesa por talher?", "answer": "O padrão do sector é 1 empregado por cada 10-15 talheres num restaurante à la carte, e 1 por cada 15-20 no menu do dia ou bistrô. Para fine dining pode baixar para 1 por cada 6-8 talheres."},
        {"question": "O que é uma brigada de cozinha?", "answer": "A brigada de cozinha é a equipa organizada hierarquicamente que trabalha numa cozinha profissional. Foi sistematizada por Auguste Escoffier. Inclui funções como Chefe de Cozinha, Sous Chef, Chefes de Partida, Cozinheiros e Ajudantes."},
        {"question": "Como reduzo os custos de pessoal sem baixar a qualidade?", "answer": "A chave está na organização: brigadas polivalentes, mise en place eficiente, boa gestão de turnos e uso de ferramentas de IA para optimizar a operação. AI Chef Pro ajuda-o a identificar os estrangulamentos na sua equipa."}
    ],
    "cta_section": {
        "title": "Optimize a gestão da sua equipa com IA",
        "subtitle": "AI Chef Pro ajuda-o a gerir turnos, calcular custos de pessoal e optimizar a produtividade da sua brigada.",
        "primary": "Experimentar AI Chef Pro grátis",
        "secondary": "Ver todos os planos"
    }
}

# ============================================================
# DUTCH (nl) TRANSLATIONS
# ============================================================
nl_toolScore = {
    "seo": {
        "title": "Digitaliseringstest Restaurant Gratis | AI Chef Pro",
        "description": "Ontdek in 2 minuten het digitaliseringsniveau van uw restaurant. 6 vragen, direct resultaat met gepersonaliseerd actieplan. Gratis, zonder registratie.",
        "keywords": "digitaliseringstest restaurant, digitaal niveau restaurant, digitalisering horeca, digitale tools restaurant"
    },
    "breadcrumb": "Digitaliseringstest",
    "hero": {
        "badge": "Gratis — Geen registratie — 2 minuten",
        "h1": "Digitaliseringstest voor Restaurants",
        "subtitle": "Hoe gedigitaliseerd is uw restaurant? Beantwoord 6 vragen en krijg uw digitaal niveau met een gepersonaliseerd actieplan.",
        "cta_tool": "Test doen ↓",
        "cta_premium": "Premium Plan →"
    },
    "tool": {
        "title": "Digitaliseringstest",
        "question_label": "Vraag {n} van {total}",
        "submit": "Mijn resultaat zien",
        "result_title": "Uw digitaliseringsniveau",
        "score_label": "Score",
        "restart": "Test herhalen",
        "cta_after": "Klaar voor de digitale sprong met AI?"
    },
    "questions": [
        {"id": 1, "text": "Heeft u een online reserveringssysteem?", "options": ["Nee, alleen telefonisch", "Ja, via derden (TheFork, etc.)", "Ja, op onze eigen website", "Ja, op website + eigen app"]},
        {"id": 2, "text": "Hoe beheert u bezorgbestellingen?", "options": ["Wij doen geen bezorging", "Alleen via platforms (Thuisbezorgd, Uber Eats...)", "Platforms + eigen website", "Eigen systeem geïntegreerd met keuken"]},
        {"id": 3, "text": "Gebruikt u beheersoftware (POS)?", "options": ["Nee, wij gebruiken papier/handmatige kassa", "Eenvoudig POS zonder rapporten", "POS met verkooprapportages", "POS geïntegreerd met voorraad, boekhouding en bezorging"]},
        {"id": 4, "text": "Hoe beheert u uw menukaart?", "options": ["Gedrukte kaart die we zelden bijwerken", "PDF of afbeelding op website/WhatsApp", "Digitale kaart met bijwerkbare QR", "Digitale kaart + AI voor suggesties"]},
        {"id": 5, "text": "Heeft u aanwezigheid op sociale media?", "options": ["Wij hebben geen sociale media", "Profiel aangemaakt maar zonder regelmatige activiteit", "Wij posten 1-2 keer per week", "Actieve strategie + digitale reclame"]},
        {"id": 6, "text": "Gebruikt u AI-tools in uw restaurant?", "options": ["Nee, ik ken ze niet", "Ik heb er een paar geprobeerd maar gebruik ze niet regelmatig", "Ik gebruik AI af en toe (ChatGPT, etc.)", "Ik heb een AI-suite geïntegreerd in mijn bedrijfsvoering"]}
    ],
    "results": [
        {"range": [0, 25], "level": "Analoog", "emoji": "📋", "description": "Uw restaurant werkt op traditionele wijze. Er is een grote kans op differentiatie met eenvoudige digitaliseringsstappen.", "tips": ["Begin met een Google Business-profiel", "Voeg een gratis QR-menukaart toe", "Maak een profiel aan op TheFork of vergelijkbaar"]},
        {"range": [26, 50], "level": "Digitaal Basis", "emoji": "📱", "description": "U heeft de eerste stappen gezet. U heeft een digitale aanwezigheid maar er zijn belangrijke tools die u nog niet benut.", "tips": ["Activeer online reserveringen op uw website", "Integreer uw POS met de bezorgdienst", "Begin AI te gebruiken voor content"]},
        {"range": [51, 75], "level": "Digitaal Gevorderd", "emoji": "🚀", "description": "Uw restaurant is goed gedigitaliseerd. U ligt boven het sectorgemiddelde. Nu is het moment om AI te integreren.", "tips": ["Automatiseer reacties op recensies met AI", "Gebruik AI om prijzen en menu te optimaliseren", "Centraliseer alle kanalen in een dashboard"]},
        {"range": [76, 100], "level": "Digitaal Pro", "emoji": "⭐", "description": "U bent een referentie op het gebied van digitalisering in de sector. U gebruikt technologie om efficiëntie en winstgevendheid te maximaliseren.", "tips": ["Verken voorspellende AI voor voorraad", "Implementeer geavanceerde data-analyse", "Overweeg mentoring voor andere restaurants"]}
    ],
    "how_it_works": {
        "title": "Hoe het werkt",
        "steps": [
            {"step": "1", "title": "6 vragen beantwoorden", "description": "Vragen over reserveringen, bezorging, POS, menukaart, sociale media en AI. Zonder trucjes, zonder registratie."},
            {"step": "2", "title": "Uw score ontvangen", "description": "De test berekent uw digitaliseringsniveau: Analoog, Basis, Gevorderd of Pro."},
            {"step": "3", "title": "Actieplan", "description": "U ontvangt 3 concrete aanbevelingen om naar het volgende niveau te gaan."}
        ]
    },
    "benefits": {
        "title": "Waarom deze test doen",
        "items": ["Identificeer precies waar u staat", "Vergelijk uzelf met het sectorgemiddelde", "Ontdek de tools met de meeste impact", "Verbeterplan in 3 concrete stappen"]
    },
    "testimonial": {
        "quote": "Ik dacht dat ik vrij gedigitaliseerd was. De test toonde me belangrijke hiaten in bezorgbeheer en AI. In 3 maanden implementeerde ik de aanbevelingen en verbeterde mijn marge met 8%.",
        "name": "Jan de Vries",
        "role": "Eigenaar, Gastronomiegroep De Gouden Lepel, Amsterdam"
    },
    "pricing": {
        "title": "Breng uw digitalisering naar het volgende niveau met AI Chef Pro",
        "subtitle": "De test vertelt u waar u staat. AI Chef Pro geeft u de tools om verder te gaan.",
        "plans": [
            {"name": "Gratis", "price": "0€/maand", "uses": "5 gebruik/maand", "highlight": False},
            {"name": "Premium Pro", "price": "25€/maand", "uses": "150 gebruik/maand", "highlight": False},
            {"name": "Premium Plus", "price": "50€/maand", "uses": "350 gebruik/maand", "highlight": True},
            {"name": "Premium Max", "price": "95€/maand", "uses": "Onbeperkt", "highlight": False}
        ]
    },
    "faq_section": {"title": "Veelgestelde vragen over digitalisering in de horeca"},
    "faq": [
        {"question": "Wat betekent digitalisering in een restaurant?", "answer": "Digitalisering in de horeca is het proces van het invoeren van technologische tools voor een beter beheer van reserveringen, bezorging, POS, klantcommunicatie en interne processen. Het varieert van een eenvoudige QR-menukaart tot beheer met kunstmatige intelligentie."},
        {"question": "Wat is het gemiddelde digitaliseringsniveau van restaurants in Nederland?", "answer": "Volgens branchestudies heeft minder dan 30% van de restaurants in Nederland een gevorderd digitaliseringsniveau. De meeste bevinden zich op een basisniveau, waarbij alleen losse tools zonder integratie worden gebruikt."},
        {"question": "Waarom is het belangrijk mijn restaurant te digitaliseren?", "answer": "Gedigitaliseerde restaurants hebben een 20-35% hogere operationele efficiëntie, minder personeelsverloop en een betere klantbeleving. Bovendien maakt AI een aanzienlijke verlaging van food cost en marketingkosten mogelijk."},
        {"question": "Hoe kan ik beginnen met het digitaliseren van mijn restaurant?", "answer": "De eerste stap is weten waar u staat: daarvoor bestaat deze test. Op basis van het resultaat kunt u de tools met de meeste impact prioriteren. AI Chef Pro biedt een zeer toegankelijk startpunt voor AI in de gastronomie."}
    ],
    "cta_section": {
        "title": "Digitaliseer uw restaurant vandaag nog met AI",
        "subtitle": "AI Chef Pro is de meest complete AI-suite voor gastronomie: 55+ tools om uw restaurant te beheren met kunstmatige intelligentie.",
        "primary": "AI Chef Pro gratis proberen",
        "secondary": "Alle plannen bekijken"
    }
}

nl_toolAlergenos = {
    "seo": {
        "title": "Allergenendetector Restaurant Gratis | AI Chef Pro",
        "description": "Detecteer de 14 verplicht te vermelden allergenen in elk gerecht direct. Voer de ingrediënten in en krijg de allergenendeclaratie. Gratis, zonder registratie.",
        "keywords": "allergenendetector restaurant, verplichte allergenen restaurant, allergenendeclaratie gerecht, verordening 1169 2011"
    },
    "breadcrumb": "Allergenendetector",
    "hero": {
        "badge": "Gratis — Geen registratie — Wettelijk verplicht",
        "h1": "Allergenendetector voor Restaurants",
        "subtitle": "Identificeer de 14 verplicht te vermelden allergenen (EU-Verordening 1169/2011) in elk gerecht direct. Kopieer de declaratie voor uw menukaart.",
        "cta_tool": "Naar de detector ↓",
        "cta_premium": "Premium Plan →"
    },
    "tool": {
        "title": "Allergenendetector",
        "input_label": "Ingrediënten van het gerecht",
        "input_placeholder": "Schrijf de ingrediënten gescheiden door komma's. Bijv: tarwebloem, ei, melk, boter, gist, zout...",
        "dish_name_label": "Naam van het gerecht (optioneel)",
        "dish_name_placeholder": "Bijv: Hollandse erwtensoep",
        "detect": "Allergenen detecteren",
        "result_title": "Gedetecteerde allergenen",
        "allergens_found": "Aanwezige allergenen",
        "no_allergens": "✅ Er zijn geen verplicht te vermelden allergenen gedetecteerd",
        "warning": "⚠️ Altijd handmatig controleren — dit tool is oriënterend",
        "legal_note": "Verplichte declaratie conform EU-Verordening 1169/2011",
        "copy": "Declaratie kopiëren",
        "copied": "Gekopieerd!",
        "reset": "Nieuwe analyse",
        "cta_after": "Wilt u de allergenen van uw hele menukaart automatisch beheren?",
        "allergens_title": "De 14 verplicht te vermelden allergenen",
        "allergens_subtitle": "Verordening (EU) 1169/2011"
    },
    "allergens": [
        {"id": "gluten", "name": "Gluten", "emoji": "🌾", "description": "Granen die gluten bevatten: tarwe, rogge, gerst, haver...", "keywords": ["tarwe", "meel", "tarwebloem", "brood", "pasta", "rogge", "gerst", "haver", "spelt", "griesmeel", "couscous", "bulgur", "kamut", "bier"]},
        {"id": "crustaceos", "name": "Schaaldieren", "emoji": "🦐", "description": "Garnalen, krabben, kreeften, langoustines...", "keywords": ["garnaal", "kreeft", "krab", "langoustine", "scampi", "schaaldier"]},
        {"id": "huevos", "name": "Eieren", "emoji": "🥚", "description": "Eieren en producten op basis van eieren", "keywords": ["ei", "eieren", "eigeel", "eiwit", "mayonaise", "omelet"]},
        {"id": "pescado", "name": "Vis", "emoji": "🐟", "description": "Alle vissoorten en afgeleide producten", "keywords": ["zalm", "kabeljauw", "tonijn", "forel", "sardine", "ansjovis", "vis", "schol", "heilbot"]},
        {"id": "cacahuetes", "name": "Pinda's", "emoji": "🥜", "description": "Pinda's en producten op basis van pinda's", "keywords": ["pinda", "pindakaas", "pindanoten"]},
        {"id": "soja", "name": "Soja", "emoji": "🫘", "description": "Soja en producten op basis van soja", "keywords": ["soja", "sojasaus", "tofu", "miso", "edamame", "sojamelk"]},
        {"id": "lacteos", "name": "Melk", "emoji": "🥛", "description": "Melk en melkproducten", "keywords": ["melk", "kaas", "boter", "room", "yoghurt", "lactose", "mozzarella", "parmezaan", "kwark", "béchamel"]},
        {"id": "frutos_secos", "name": "Noten", "emoji": "🌰", "description": "Amandelen, hazelnoten, walnoten, cashews, pistaches...", "keywords": ["amandel", "hazelnoot", "walnoot", "cashew", "pistache", "macadamia", "noten", "noot"]},
        {"id": "apio", "name": "Selderij", "emoji": "🌿", "description": "Selderij en producten op basis van selderij", "keywords": ["selderij", "knolselderij", "selderijzout"]},
        {"id": "mostaza", "name": "Mosterd", "emoji": "🌻", "description": "Mosterd en producten op basis van mosterd", "keywords": ["mosterd", "mosterdcorrels", "mosterdzaad"]},
        {"id": "sesamo", "name": "Sesam", "emoji": "🌱", "description": "Sesamzaad en producten op basis van sesam", "keywords": ["sesam", "sesamzaad", "sesamolie", "tahini", "tahin", "hummus"]},
        {"id": "sulfitos", "name": "Zwaveldioxide en sulfieten", "emoji": "🍷", "description": "Concentratie van meer dan 10 mg/kg of 10 mg/liter", "keywords": ["wijn", "azijn", "gedroogde vruchten", "rozijnen", "abrikozen", "sulfieten", "zwaveldioxide"]},
        {"id": "altramuces", "name": "Lupine", "emoji": "🌾", "description": "Lupine en producten op basis van lupine", "keywords": ["lupine", "lupinebloem", "lupinezaad"]},
        {"id": "moluscos", "name": "Weekdieren", "emoji": "🦑", "description": "Mosselen, oesters, slakken, octopus, inktvis...", "keywords": ["mossel", "oester", "slak", "octopus", "inktvis", "zeekat", "venusschelp", "weekdier"]}
    ],
    "how_it_works": {
        "title": "Hoe het werkt",
        "steps": [
            {"step": "1", "title": "Ingrediënten invoeren", "description": "Voer alle ingrediënten van uw gerecht in, gescheiden door komma's, zoals u ze inkoopt."},
            {"step": "2", "title": "Automatische detectie", "description": "De detector identificeert welke allergenen van EU-Verordening 1169/2011 aanwezig zijn in de ingrediënten."},
            {"step": "3", "title": "Declaratie kopiëren", "description": "Ontvang de allergenendeclaratie klaar om toe te voegen aan uw menukaart, website of beheersysteem."}
        ]
    },
    "benefits": {
        "title": "Waarom de allergenendetector gebruiken",
        "items": ["Voldoe aan EU-Verordening 1169/2011 (verplicht)", "Bescherm uw klanten met allergieën", "Vermijd boetes tot 600.000 €", "Declaratie klaar voor uw digitale menukaart"]
    },
    "testimonial": {
        "quote": "Na een inspectie zei de inspecteur dat onze allergenendeclaratie voorbeeldig was. Wij gebruiken dit tool om elk gerecht te controleren voordat we het aan de menukaart toevoegen.",
        "name": "Marieke van den Berg",
        "role": "Chef-eigenaar, Restaurant De Tuinkamer, Utrecht"
    },
    "pricing": {
        "title": "Volledig allergenenmanagement met AI Chef Pro",
        "subtitle": "De basisdetector is gratis. Met AI Chef Pro beheert u de allergenen van uw hele menukaart met automatische waarschuwingen.",
        "plans": [
            {"name": "Gratis", "price": "0€/maand", "uses": "5 gebruik/maand", "highlight": False},
            {"name": "Premium Pro", "price": "25€/maand", "uses": "150 gebruik/maand", "highlight": False},
            {"name": "Premium Plus", "price": "50€/maand", "uses": "350 gebruik/maand", "highlight": True},
            {"name": "Premium Max", "price": "95€/maand", "uses": "Onbeperkt", "highlight": False}
        ]
    },
    "faq_section": {"title": "Veelgestelde vragen over allergenen in de horeca"},
    "faq": [
        {"question": "Wat zegt de wet over allergenen in restaurants?", "answer": "EU-Verordening 1169/2011 verplicht alle restaurants, cafés en horecabedrijven om informatie te verstrekken over de 14 verplicht te vermelden allergenen in al hun gerechten. Niet-naleving kan boetes van 3.000 € tot 600.000 € met zich meebrengen afhankelijk van de ernst."},
        {"question": "Wat zijn de 14 verplicht te vermelden allergenen?", "answer": "Gluten, schaaldieren, eieren, vis, pinda's, soja, melk, noten (amandelen, walnoten, hazelnoten...), selderij, mosterd, sesam, zwaveldioxide en sulfieten, lupine en weekdieren."},
        {"question": "Is een algemene waarschuwing 'kan sporen bevatten' voldoende?", "answer": "Nee. De wet vereist specifieke informatie per gerecht. Een algemene waarschuwing is niet voldoende en kan worden gesanctioneerd. U moet de klant kunnen informeren welke allergenen elk specifiek gerecht bevat."},
        {"question": "Is dit tool 100% juridisch betrouwbaar?", "answer": "Dit tool is oriënterend en ondersteunend bedoeld. De juridische verantwoordelijkheid ligt altijd bij het etablissement. U moet de ingrediënten en mogelijke kruisbesmettingen handmatig controleren. Voor volledig en gecertificeerd beheer, gebruik AI Chef Pro Premium."}
    ],
    "cta_section": {
        "title": "Beheer de allergenen van uw hele menukaart met AI",
        "subtitle": "Met AI Chef Pro beheert u de allergenen van elk gerecht automatisch, met waarschuwingen bij ingrediëntenwijzigingen en exporteerbare declaratie voor uw menukaart.",
        "primary": "AI Chef Pro gratis proberen",
        "secondary": "Alle plannen bekijken"
    }
}

nl_toolBrigada = {
    "seo": {
        "title": "Keukenteamcalculator Gratis | AI Chef Pro",
        "description": "Bereken hoeveel medewerkers u nodig heeft in de keuken en de zaal op basis van uw servicevolume. Gratis, zonder registratie. Gebaseerd op echte horecastandaarden.",
        "keywords": "keukenteamcalculator, hoeveel koks heb ik nodig, personeel restaurant, keukenteam horeca"
    },
    "breadcrumb": "Keukenteamcalculator",
    "hero": {
        "badge": "Gratis — Geen registratie",
        "h1": "Keukenteamcalculator",
        "subtitle": "Ontdek hoeveel koks en obers u nodig heeft op basis van uw couverts, diensten en servicetype. Gebaseerd op echte brancheverhoudingen.",
        "cta_tool": "Naar de calculator ↓",
        "cta_premium": "Premium Plan →"
    },
    "tool": {
        "title": "Keukenteamcalculator",
        "covers_label": "Couverts per service",
        "covers_hint": "Maximum aantal couverts in één service (lunch of diner)",
        "service_type_label": "Servicetype",
        "service_types": ["À la carte (hoge complexiteit)", "Dagmenu / Bistro", "Buffet / Self-service", "Catering / Banketten"],
        "services_per_day_label": "Services per dag",
        "services_options": ["1 service (alleen lunch of diner)", "2 services (lunch + diner)", "3 services (ontbijt + lunch + diner)"],
        "has_delivery_label": "Doet u bezorging?",
        "delivery_volume_label": "Bezorgbestellingen/dag",
        "calculate": "Team berekenen",
        "result_title": "Uw aanbevolen team",
        "kitchen_title": "👨‍🍳 Keuken",
        "sala_title": "🍽️ Zaal",
        "head_chef": "Chef-kok",
        "sous_chef": "Sous-chef",
        "chef_partida": "Partijchef",
        "cocinero": "Kok",
        "ayudante": "Keukenmedewerker",
        "kitchen_porter": "Afwasser / Office",
        "maitre": "Maître / Zaalchef",
        "jefe_rango": "Rangchef",
        "camarero": "Ober",
        "ayudante_sala": "Zaalmedewerker",
        "total_kitchen": "Totaal keuken",
        "total_sala": "Totaal zaal",
        "total_staff": "Totaal personeel",
        "ratio_label": "Verhouding couverts/ober",
        "reset": "Nieuwe berekening",
        "cta_after": "Wilt u de personeelskosten van uw restaurant optimaliseren?"
    },
    "how_it_works": {
        "title": "Hoe het werkt",
        "steps": [
            {"step": "1", "title": "Uw volume opgeven", "description": "Aantal couverts per service, servicetype en hoeveel services u per dag doet."},
            {"step": "2", "title": "Berekening volgens standaarden", "description": "De calculator past de echte brancheverhoudingen toe voor elk servicetype."},
            {"step": "3", "title": "Aanbevolen team", "description": "U ontvangt de uitsplitsing van functies in keuken en zaal met het aanbevolen minimumaantal voor elke rol."}
        ]
    },
    "benefits": {
        "title": "Waarom uw team berekenen",
        "items": ["Vermijd overdimensionering van het personeel (onnodige kosten)", "Vermijd onderdimensionering (slechte service)", "Ken de standaardverhoudingen voor uw restauranttype", "Objectieve basis voor onderhandelingen met uw team"]
    },
    "testimonial": {
        "quote": "Ik had 4 koks voor 60 couverts met dagmenu. De calculator toonde me dat 3 goed georganiseerde koks voldoende was. Ik bespaarde 1.800 €/maand aan salarissen.",
        "name": "Pieter Bakker",
        "role": "Eigenaar, Restaurant Het Uitzicht, Rotterdam"
    },
    "pricing": {
        "title": "Optimaliseer uw team met AI Chef Pro",
        "subtitle": "De basiscalculator is gratis. Met AI Chef Pro optimaliseert u diensten, personeelskosten en productiviteit van uw team.",
        "plans": [
            {"name": "Gratis", "price": "0€/maand", "uses": "5 gebruik/maand", "highlight": False},
            {"name": "Premium Pro", "price": "25€/maand", "uses": "150 gebruik/maand", "highlight": False},
            {"name": "Premium Plus", "price": "50€/maand", "uses": "350 gebruik/maand", "highlight": True},
            {"name": "Premium Max", "price": "95€/maand", "uses": "Onbeperkt", "highlight": False}
        ]
    },
    "faq_section": {"title": "Veelgestelde vragen over keukenteams"},
    "faq": [
        {"question": "Hoeveel koks heb ik nodig voor 50 couverts?", "answer": "Dat hangt af van het servicetype. Voor à la carte (hoge complexiteit) heeft u ongeveer 4-5 koks nodig voor 50 couverts. Voor dagmenu kunnen 2-3 goed georganiseerde koks voldoende zijn."},
        {"question": "Wat is de standaardverhouding van obers per couvert?", "answer": "De branchestandaard is 1 ober per 10-15 couverts in een à la carte restaurant, en 1 per 15-20 bij dagmenu of bistro. Voor fine dining kan dit dalen naar 1 per 6-8 couverts."},
        {"question": "Wat is een keukenteam (brigade)?", "answer": "Het keukenteam is het hiërarchisch georganiseerde team dat werkt in een professionele keuken. Het werd gesystematiseerd door Auguste Escoffier. Het omvat functies als chef-kok, sous-chef, partijchefs, koks en medewerkers."},
        {"question": "Hoe verlaag ik personeelskosten zonder kwaliteitsverlies?", "answer": "De sleutel ligt in organisatie: veelzijdige teams, efficiënte mise en place, goed dienstbeheer en gebruik van AI-tools om de bedrijfsvoering te optimaliseren. AI Chef Pro helpt u de knelpunten in uw team te identificeren."}
    ],
    "cta_section": {
        "title": "Optimaliseer het beheer van uw team met AI",
        "subtitle": "AI Chef Pro helpt u diensten te beheren, personeelskosten te berekenen en de productiviteit van uw team te optimaliseren.",
        "primary": "AI Chef Pro gratis proberen",
        "secondary": "Alle plannen bekijken"
    }
}

# ============================================================
# APPLY TRANSLATIONS
# ============================================================

translations = {
    "de": {
        "toolScore": de_toolScore,
        "toolAlergenos": de_toolAlergenos,
        "toolBrigada": de_toolBrigada,
    },
    "it": {
        "toolScore": it_toolScore,
        "toolAlergenos": it_toolAlergenos,
        "toolBrigada": it_toolBrigada,
    },
    "pt": {
        "toolScore": pt_toolScore,
        "toolAlergenos": pt_toolAlergenos,
        "toolBrigada": pt_toolBrigada,
    },
    "nl": {
        "toolScore": nl_toolScore,
        "toolAlergenos": nl_toolAlergenos,
        "toolBrigada": nl_toolBrigada,
    },
}

for locale, sections in translations.items():
    filepath = os.path.join(LOCALES_DIR, f"{locale}.json")
    print(f"\nProcessing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    for section_key, section_data in sections.items():
        data[section_key] = section_data
        print(f"  Replaced {section_key}")

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  Saved {locale}.json")

# ============================================================
# ADD allergens_title / allergens_subtitle to ES, EN, FR
# ============================================================
fixes = {
    "es": {
        "allergens_title": "Los 14 alérgenos de declaración obligatoria",
        "allergens_subtitle": "Reglamento (UE) 1169/2011"
    },
    "en": {
        "allergens_title": "The 14 mandatory allergens",
        "allergens_subtitle": "EU Regulation 1169/2011"
    },
    "fr": {
        "allergens_title": "Les 14 allergènes à déclaration obligatoire",
        "allergens_subtitle": "Règlement (UE) 1169/2011"
    }
}

for locale, keys in fixes.items():
    filepath = os.path.join(LOCALES_DIR, f"{locale}.json")
    print(f"\nPatching {locale}.json toolAlergenos.tool...")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    for k, v in keys.items():
        if k not in data["toolAlergenos"]["tool"]:
            data["toolAlergenos"]["tool"][k] = v
            print(f"  Added {k}: {v}")
        else:
            print(f"  Already exists: {k}")

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  Saved {locale}.json")

print("\nDone! All translations applied.")
