// Alemán content for use-case spokes.
// Each entry mirrors the structure of USE_CASES_CONTENT_ES.
// Missing entries fall back to ES at runtime via makeContent() in use-cases.ts.
//
// Generado el 2026-08-15 con scripts/astro-migration/fase10-traducir-spokes.py
// (bridge.py ~deepseek/deepseek-v4-flash-latest, --strict-lang) y el glosario
// de la PLATAFORMA viva fase10-glosario-de.json. Los agentes sin versión
// de se preservan verbatim a propósito (decisión de catálogo pendiente,
// ver CATALOGO_ITALIANO_PENDIENTE.md — aplica a los 5 idiomas).
//
// NO editar a mano campo a campo: productIds, galleryImages, features[].icon,
// seo.ogImage y testimonialAuthor se preservan verbatim desde el ES y el
// validador del script lo comprueba. Regenerar PISA ediciones manuales.

import type { UseCaseContent } from './use-cases';

export const USE_CASES_CONTENT_DE: Record<string, UseCaseContent> = {
  "propietario-restaurante": {
    "h1": "KI für Restaurantbesitzer",
    "heroSubtitle": "Treffen Sie bessere Entscheidungen, gewinnen Sie Verwaltungsstunden zurück und steigern Sie die Rentabilität Ihres Restaurants mit einer Suite spezialisierter KI-Agenten für die Gastronomie.",
    "heroTagline": "Ihr digitaler Partner für datenbasierte Unternehmensführung",
    "badge": "Für Restaurantbesitzer und -inhaber",
    "painsTitle": "Was ein Restaurantbesitzer unbedingt lösen muss",
    "pains": [
      "Enge Marge: Ohne präzise Analyse ist schwer zu erkennen, welche Gerichte profitabel sind und welche die Rentabilität schmälern",
      "Wenig Zeit für die Überprüfung von Kosten, Kalkulationen, Lieferanten und Kommunikation mit dem Team",
      "Menü-, Preis- und Aktionsentscheidungen eher nach Bauchgefühl als nach Daten",
      "Rotierende Teams: Einarbeiten, Überwachen und Schichtmanagement kostet jede Woche Stunden",
      "Finanzberichte an den Steuerberater oder Investoren, die saubere und konsolidierte Dokumente erfordern",
      "Ständiges Marketing und Kommunikation (Social Media, Web, E-Mail), die vom eigentlichen Geschäft ablenken"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Restaurantbesitzer hilft",
    "features": [
      {
        "icon": "BriefcaseBusiness",
        "title": "Profi Restaurantmanager",
        "description": "Spezialisierter Agent zur Unterstützung des Eigentümers bei täglichen Abläufen, Team-Entscheidungen und Reporting an Investoren."
      },
      {
        "icon": "FileText",
        "title": "Professioneller Finanzplan",
        "description": "Kit Plan Financiero: Cashflow, Break-even-Punkt, monatliche P&L und Kennzahlen-Dashboard. Vorlagen bereit für Investoren und Banken."
      },
      {
        "icon": "Calculator",
        "title": "Professionelle Kalkulationen",
        "description": "Kreativküche liefert Rezept + erste CSV-Kalkulation mit Referenzpreisen; das Kit de Escandallos Pro verwaltet es mit Ihren tatsächlichen Preisen."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP und Lebensmittelsicherheit",
        "description": "Pack APPCC mit 19 Vorlagen bereit für Inspektionen, mobile Erfassung und druckfertige A4-Blätter."
      },
      {
        "icon": "Users",
        "title": "Personal- und Schichtmanagement",
        "description": "Kit Gestión de Personal: Einsatzpläne, Stundenkontrolle, Produktivitätskennzahlen und Onboarding neuer Mitarbeiter."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Marketing- und Local-SEO-Suite: Gerichtsbeschreibungen, Blog und KI-Kampagnen zur Gewinnung von organischem Traffic."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Lokale Keyword-Recherche für Gastronomie, um Ihr Restaurant ohne Agenturkosten in Google zu positionieren."
      },
      {
        "icon": "BarChart3",
        "title": "Mitarbeiteressen AI",
        "description": "Generator für Mitarbeitermenüs, der Kosten spart und Küchen- und Serviceteam motiviert hält."
      },
      {
        "icon": "MessageSquare",
        "title": "Mental Coach",
        "description": "Psychologisches Coaching für Gastronomen: Stressmanagement, Work-Life-Balance und Teamführung in Hochdruckbereichen."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Restaurantbesitzers mit AI Chef Pro",
    "workflow": [
      "08:30 · Kaffee und Dashboard – Sie öffnen das Kit Plan Financiero und prüfen die Kennzahlen des Vortags. Sie stellen fest, dass die Food Cost durch Lebensmittelabfälle bei Fisch auf 33 % gestiegen ist.",
      "09:30 · Profi Restaurantmanager – Sie bitten den Agenten um eine Ursachenanalyse und erhalten 3 konkrete Maßnahmen für diese Woche.",
      "10:30 · MenuDish Local SEO – Sie aktualisieren die Beschreibungen der 4 Top-Gerichte in Google Business und auf der Website mit Schlüsselwörtern, die Keyword Discovery AI+ erkannt hat.",
      "12:30 · Mittagsservice – Sie überwachen den Servicebereich mit der Checkliste des Kit de Tareas Restaurante Casual.",
      "15:30 · Meeting mit dem Steuerberater – Sie exportieren monatliche P&L, Kennzahlen-Dashboard und Personaleinsatzplan als PDF direkt aus dem Kit Plan Financiero. Meeting in 30 Minuten abgeschlossen.",
      "17:00 · Kreativküche – Sie bitten um Ideen für die kommende Saisonkarte. Der Agent liefert 8 Gerichte mit Rezept und CSV-Kalkulation.",
      "18:30 · Team-Entscheidung – Sie nutzen Mental Coach, um das schwierige Gespräch mit einem wichtigen Mitarbeiter vorzubereiten. Sie gehen mit Struktur und Argumenten ins Meeting.",
      "21:00 · Feierabend – der Manager sendet Ihnen den automatischen Tagesbericht per WhatsApp. Sie gehen ohne offene Papierkram nach Hause."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Restaurantbesitzer",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Früher verbrachte ich 6 Stunden pro Woche nur damit, Zahlen zwischen Excel und Servietten abzugleichen. Mit AI Chef Pro schließe ich das in einer Stunde mit professionellen Dashboards ab. Ich habe die finanzielle Kontrolle über meine beiden Standorte zurückgewonnen und die Marge ist im ersten Quartal um 3 Punkte gestiegen.",
    "testimonialAuthor": "Carlos Méndez",
    "testimonialRole": "Besitzer, Gruppe mediterraner Bistros (2 Standorte)",
    "faqTitle": "Häufige Fragen von Restaurantbesitzern",
    "faqs": [
      {
        "q": "Welche Restaurantgröße passt zu AI Chef Pro?",
        "a": "Von einem einzelnen Familienbetrieb bis zu Gruppen mit mehr als 10 Restaurants. Die Vorlagen skalieren mit dem Volumen und die Pläne passen sich der tatsächlichen Nutzung an. Es gibt Kunden mit 1 Standort und andere mit 25 aktiven Einheiten."
      },
      {
        "q": "Benötige ich technische Kenntnisse?",
        "a": "Nein. Wenn Sie WhatsApp und Excel auf grundlegendem Niveau nutzen können, können Sie auch AI Chef Pro nutzen. Das Onboarding beginnt mit dem Agenten „Wer sind Sie?“, der das System in 2 Minuten an Sie, Ihr Unternehmen und Ihre geografische Region anpasst. Es gibt kurze Onboarding-Videos und direkten Support per WhatsApp."
      },
      {
        "q": "Ersetzt es meinen Steuerberater oder Berater?",
        "a": "Nein, aber es erleichtert ihnen das Leben erheblich. Ihr Steuerberater erhält saubere Dokumente und Sie kommen mit konsolidierten Daten zu den Meetings. Die meisten Steuerberatungen empfehlen AI Chef Pro schließlich anderen Kunden."
      },
      {
        "q": "Wie lange dauert es, bis ich Ergebnisse sehe?",
        "a": "Die meisten Eigentümer berichten in der ersten Nutzungswoche von 4 bis 6 gewonnenen Wochenstunden. Die Auswirkung auf die Marge liegt in der Regel zwischen 2 und 5 Prozentpunkten in 60-90 Tagen, dank der Neugestaltung von Gerichten mit hoher Food Cost und der Kontrolle von Lebensmittelabfällen."
      },
      {
        "q": "Wie hilft es mir bei Marketing und lokalem SEO?",
        "a": "Die Suite Inhalte und Social Media umfasst MenuDish Local SEO (optimierte Gerichtsbeschreibungen), BlogPost SEO Gen+ (Beiträge zur Gewinnung von organischem Traffic) und Keyword Discovery AI+ (lokale gastronomische Schlüsselwörter). Sie reduzieren Ausgaben für Marketingagenturen und gewinnen direkte Reservierungen."
      },
      {
        "q": "Gibt es Rabatte für Gruppen mit mehreren Standorten?",
        "a": "Ja. Ab 5 aktiven Einheiten gibt es Unternehmenspläne mit personalisiertem Onboarding und konsolidierten Dashboards pro Gruppe."
      }
    ],
    "ctaTitle": "Führen Sie Ihr Restaurant mit Daten, nicht mit Bauchgefühl.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Restaurantbesitzer: Finanzplan, Kalkulationen, SEO | AI Chef Pro",
      "description": "KI-Suite für Restaurantbesitzer: spezialisierte Agenten, Finanzplan, professionelle Kalkulationen, HACCP, Marketing und lokales SEO. Starten Sie noch heute.",
      "keywords": "KI Restaurantbesitzer, Restaurantinhaber KI, Software Restaurantverwaltung Eigentümer, Finanzplan Restaurant KI, Kalkulationen Restaurant, Marketing Restaurant KI, lokales SEO Restaurant, KI-Agent Gastronomie, Restaurantbesitzer Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/propietario-restaurante.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Unternehmen zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational Onboarding, bei dem Sie erzählen, welche Art von Restaurant Sie haben, in welcher Stadt, wie viele Standorte, welchen durchschnittlichen Bon Sie haben und wie Sie arbeiten. Ab diesem Moment antwortet jeder Agent – vom Finanzplan bis zum lokalen SEO – angepasst an Ihren Kontext: Marktpreise Ihrer Region, Vorschriften Ihres Landes und den tatsächlichen Umfang Ihres Betriebs. Es ist kein Formular, sondern ein kurzes Gespräch, das jedes Werkzeug für Ihr Unternehmen wirklich nützlich macht.",
    "appsTitle": "Die KI-Agenten, die Sie als Restaurantbesitzer nutzen werden",
    "apps": [
      {
        "name": "Profi Restaurantmanager",
        "category": "Gastro Profile Pro",
        "description": "Operativer und finanzieller Assistent zur Unterstützung bei Team-Entscheidungen, Reporting und täglichen Abläufen."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Spezialist für Bistros, Gastrobars, Tapas und mediterrane Küche: das komplette Casual-Spektrum mit professioneller Basis."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und Social Media",
        "description": "Optimierte Gerichtsbeschreibungen für lokales SEO in Google Business und auf der Website."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und Social Media",
        "description": "Blogbeiträge, die lokalen organischen Traffic auf Ihr Restaurant lenken."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Inhalte und Social Media",
        "description": "Lokale Keyword-Recherche für Gastronomie nach Postleitzahlgebiet."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Professionelle Gerichtsentwicklung mit Rezept + erster CSV-Kalkulation (Referenzpreise) bereit für das Kit de Escandallos Pro."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Präzise Daten zu Lebensmittelabfällen und Erträgen pro Zutat, essenziell für realistische Kalkulationen."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Rezept und Gericht, bereit für die Regulierung."
      },
      {
        "name": "Mitarbeiteressen AI",
        "category": "Gastro Profile Pro",
        "description": "Generator für Mitarbeitermenüs, der Kosten spart und das Team motiviert hält."
      },
      {
        "name": "Mental Coach",
        "category": "Tools und Utilities",
        "description": "Psychologisches Coaching für Gastronomen: Stress, Teams und schwierige Entscheidungen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und Social Media",
        "description": "Gastronomischer Kalender mit wichtigen Terminen, Ideen und Hashtags für Social Media und Blog."
      },
      {
        "name": "InstaFlow AI Pro + Pinterest Pins Gen",
        "category": "Inhalte und Social Media",
        "description": "Virale Inhalte für Instagram und Pinterest ohne Agentur."
      }
    ],
    "metrics": [
      {
        "value": "+3 pp",
        "label": "Marge in 60-90 Tagen"
      },
      {
        "value": "−6 h",
        "label": "Wochenstunden in der Verwaltung"
      },
      {
        "value": "×2",
        "label": "direkte Reservierungen über lokales SEO"
      },
      {
        "value": "12+",
        "label": "KI-Agenten für Ihre Rolle"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "6 Wochenstunden mit Excel, Servietten und Lieferantennotizen abgleichen",
        "Menü- und Preisentscheidungen nach Bauchgefühl, nicht nach Analyse der tatsächlichen Food Cost",
        "Berichte an den Steuerberater mit verstreuten Dateien in Word, Excel und E-Mail",
        "Improvisiertes oder teuer ausgelagertes Marketing, ohne zu wissen, was funktioniert",
        "Ständiger Stress und Einbruch an Feiertagen, weil Sie die Kontrolle nicht abgeben"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "1 Wochenstunde für professionelle Dashboards mit klaren KPIs",
        "Menü- und Preisentscheidungen mit professioneller Kalkulation und Margenanalyse",
        "Berichte an den Steuerberater als PDF direkt aus dem Kit Plan Financiero",
        "Automatisiertes lokales SEO und KI-Marketing-Suite, die Agenturkosten senken",
        "Gelassenheit: Das Team sendet Ihnen automatische Berichte per WhatsApp"
      ]
    },
    "galleryTitle": "Der Alltag eines Restaurantbesitzers in Bildern",
    "gallerySubtitle": "Was Sie mit AI Chef Pro verwalten können: Finanz-Dashboards, operative Entscheidungen, Team, Service und Reporting.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-tablet.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-meeting.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-numbers.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-dining.jpg"
    ]
  },
  "gerente-restaurante": {
    "h1": "KI für Restaurantleiter und Manager",
    "heroSubtitle": "Optimieren Sie den Tagesbetrieb, kontrollieren Sie Kosten und gewinnen Sie Stunden administrativer Arbeit zurück mit einer Suite von KI-Agenten, die für den Alltag des Restaurantmanagers entwickelt wurden.",
    "heroTagline": "Mehr operative Kontrolle, weniger lose Zettel",
    "badge": "Für Leiter und Manager",
    "painsTitle": "Was ein Restaurantleiter unbedingt lösen muss",
    "pains": [
      "Jede Woche Dienstpläne erstellen unter Einhaltung von Tarifvertrag, gesetzlicher Arbeitszeit und Ruhezeiten ohne Abweichungen oder Mehrkosten",
      "Lebensmittelabfälle, Inventar und Einkäufe bei verschiedenen Lieferanten kontrollieren, die wöchentlich die Preise ändern",
      "APPCC aktuell halten und Inspektionen ohne Stress und Papierstau vorbereiten",
      "Dem Eigentümer mit konsolidierten Daten und professionellen Dashboards berichten, nicht mit improvisierten Excel-Tabellen",
      "Küchen- und Servicepersonal mit klarer Kommunikation koordinieren und neue Mitarbeiter schnell einarbeiten",
      "Den Betrieb während der Service-Spitzen managen, ohne Qualität zu verlieren oder den Saal zu vernachlässigen"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Manager hilft",
    "features": [
      {
        "icon": "BriefcaseBusiness",
        "title": "Profi Restaurantmanager",
        "description": "Spezialisierter Agent zur Unterstützung bei operativen Entscheidungen, Teammanagement und Reporting an den Eigentümer."
      },
      {
        "icon": "Calendar",
        "title": "Dienstpläne und Schichtkontrolle",
        "description": "Kit Gestión de Personal: Dienstpläne in Minuten unter Einhaltung des Tarifvertrags, Stundenkontrolle, Produktivitätskennzahlen."
      },
      {
        "icon": "Package",
        "title": "Inventar und Einkaufskontrolle",
        "description": "Kit Inventario: fertige Excel-Vorlagen, Mindestbestandswarnungen, Lieferantenvergleich und Lebensmittelabfälle."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC und Rückverfolgbarkeit",
        "description": "Pack APPCC mit 17 Aufzeichnungen, Temperaturwarnungen vom Handy und Export bereit für Inspektionen."
      },
      {
        "icon": "BarChart3",
        "title": "KPIs und Reporting an den Eigentümer",
        "description": "Küchen- und Saalkennzahlen, Produktivität, durchschnittlicher Bon. Dashboards direkt aus Excel als PDF exportierbar."
      },
      {
        "icon": "CheckSquare",
        "title": "Wiederkehrende Aufgaben pro Schicht",
        "description": "Fertige Vorlagen nach Konzept: Eröffnung, Abschluss, Mise en Place und Service in einem einzigen Kit pro Geschäftstyp."
      },
      {
        "icon": "Users",
        "title": "Mitarbeiteressen AI",
        "description": "Generator für Personalmenüs, der Kosten spart und das Team motiviert und gut versorgt hält."
      },
      {
        "icon": "MessageSquare",
        "title": "Mental Coach",
        "description": "Psychologisches Coaching für schwierige Gespräche, Stress und Teammotivation."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergen-ID",
        "description": "Automatische Allergenerkennung pro Gericht, bereit für Vorschriften und den Service."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Managers mit AI Chef Pro",
    "workflow": [
      "08:30 · Eröffnung – Sie drucken die Schicht-Checkliste aus dem Kit de Tareas und prüfen das Inventar in 10 Minuten.",
      "09:30 · Profi Restaurantmanager – der Agent fasst die Vorfälle des Vortags und die offenen Aufgaben zusammen.",
      "10:30 · Kit Inventario – Sie validieren Bestellungen bei Lieferanten mit Preisvergleich und Mindestbestandswarnungen.",
      "12:30 · Mittagsservice – das Team erfasst Lebensmittelabfälle und Temperaturen vom Handy aus mit dem Pack APPCC.",
      "15:30 · Dienstplan für die nächste Woche – Sie öffnen das Kit Gestión de Personal und schließen den Dienstplan in 20 Minuten unter Einhaltung des Tarifvertrags.",
      "17:00 · Mitarbeiteressen AI – Sie generieren das Personalmenü für die nächste Woche mit Zutaten, die Sie bereits auf Lager haben.",
      "19:00 · Schwieriges Gespräch – Sie nutzen Mental Coach, um das Gespräch mit einem Koch vorzubereiten, der wiederholt zu spät kommt.",
      "23:30 · Abschluss – Sie erstellen den Tagesbericht mit Kennzahlen und senden ihn dem Eigentümer per WhatsApp mit einem Klick."
    ],
    "productsTitle": "Vorlagen und Kits zum Download für Manager",
    "productIds": [
      "kit-gestion-personal",
      "kit-inventario",
      "pack-appcc",
      "kit-tareas",
      "kit-escandallos",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Früher verbrachte ich 8 Stunden pro Woche nur mit der Planung von Schichten und Bestellungen bei Lieferanten. Jetzt schließe ich das in 2 Stunden mit dem Kit Gestión de Personal und dem Kit Inventario ab. AI Chef Pro hat mir Zeit zurückgegeben, um im Saal beim Team zu sein, wo ein Manager hingehört.",
    "testimonialAuthor": "Marta Ruiz",
    "testimonialRole": "Manager, Casual-Restaurant mit 80 Plätzen",
    "faqTitle": "Häufige Fragen von Managern",
    "faqs": [
      {
        "q": "Funktioniert es, wenn ich 1 Lokal oder mehrere betreibe?",
        "a": "In beiden Fällen. Die Vorlagen skalieren mit dem Volumen und Sie können das Reporting mehrerer Standorte in einem einzigen Dashboard konsolidieren. Es gibt Kunden mit 1 Standort und andere mit mehr als 10 aktiven Einheiten."
      },
      {
        "q": "Ersetzt es die Reservierungssoftware oder das Kassensystem?",
        "a": "Nein, es ergänzt. Cover Manager oder The Fork verwalten Reservierungen und das Kassensystem verwaltet Verkäufe; AI Chef Pro verwaltet Kosten, Personal, APPCC, Inventar und internen Betrieb. Die Daten sind über Excel perfekt kompatibel."
      },
      {
        "q": "Benötigt das Team Schulung?",
        "a": "Minimal. Die Vorlagen und Agenten sind auf Spanisch und alles startet mit dem Agenten „Wer sind Sie?“, der das System in 2 Minuten an Sie anpasst. Die tatsächliche Lernkurve des Teams beträgt 1-2 Tage mit Video-Onboarding und WhatsApp-Support."
      },
      {
        "q": "Kann ich die Daten für meinen Steuerberater oder den Eigentümer exportieren?",
        "a": "Ja. Alles wird im professionellen Format nach Excel und PDF exportiert. Steuerberater erhalten saubere Dokumentation und Eigentümer erhalten Dashboards mit klaren KPIs direkt per WhatsApp."
      },
      {
        "q": "Wie hilft es mir bei schwierigen Gesprächen mit dem Team?",
        "a": "Mental Coach ist ein psychologischer Coaching-Agent für Gastronomen, der Ihnen hilft, schwierige Gespräche (Kündigungen, Zuspätkommen, Konflikte zwischen Küche und Service) mit Argumenten und klarer Struktur vor dem Meeting zu strukturieren."
      },
      {
        "q": "Gibt es spezifische Vorlagen nach Geschäftskonzept?",
        "a": "Ja. Es gibt spezifische Kits de Tareas für Casual, Café, Pizzeria, Burgerladen, Dark Kitchen, Konditorei, Bar, Catering, Hotel, Eisdiele, Schokoladenmanufaktur, kreatives Restaurant und Privatkoch. Jedes mit Vorlagen, die an den tatsächlichen Betrieb angepasst sind."
      }
    ],
    "ctaTitle": "Bringen Sie den Betrieb Ihres Restaurants auf die nächste Stufe.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Restaurantleiter und Manager: Dienstpläne, APPCC und Reporting | AI Chef Pro",
      "description": "KI-Suite für Restaurantmanager: Dienstpläne, Inventar, APPCC, KPIs und Reporting an den Eigentümer mit spezialisierten Agenten für die Gastronomie. Starten Sie noch heute.",
      "keywords": "KI Restaurantleiter, Restaurantmanager KI, Software Restaurantmanager, operative Restaurantverwaltung KI, Dienstpläne Restaurant, APPCC Manager, KPIs Restaurant, KI-Agent Gastronomie, Restaurantleiter Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/gerente-restaurante.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Restaurant zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Konversations-Onboarding, bei dem Sie erzählen, welche Art von Restaurant Sie führen, in welcher Stadt, wie viele Gäste Sie bedienen und wie Sie arbeiten. Ab diesem Moment antwortet jeder Agent – von den Dienstplänen bis zum Reporting – angepasst an Ihren Kontext: Tarifvertrag des Landes, Größe Ihres Teams, echte Service-Spitzen. Es ist kein Formular: Es ist ein kurzes Gespräch, das die Suite für Ihren Alltag als Manager wirklich nützlich macht.",
    "appsTitle": "Die KI-Agenten, die Sie als Manager nutzen werden",
    "apps": [
      {
        "name": "Profi Restaurantmanager",
        "category": "Gastro Profile Pro",
        "description": "Hauptagent: operative Entscheidungen, Teammanagement und Reporting an den Eigentümer."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Spezialist für Bistros, Gastrobars, Tapas und mediterrane Küche: das gesamte Casual-Spektrum."
      },
      {
        "name": "Mitarbeiteressen AI",
        "category": "Gastro Profile Pro",
        "description": "Generator für Personalmenüs, der Kosten spart und das Team motiviert."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Präzise Daten zu Lebensmittelabfällen und Erträgen pro Zutat, essenziell für die Küchenkontrolle."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Automatische Allergenerkennung pro Rezept und Gericht."
      },
      {
        "name": "Conversor Ing",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Umrechner für Gewichte und Maße für die Profiküche."
      },
      {
        "name": "Calcula Pax",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Portionsrechner, der Rezepte auf jede Anzahl von Gästen skaliert."
      },
      {
        "name": "Mental Coach",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Psychologisches Coaching für Gastronomen: Stress, schwierige Gespräche und Teammotivation."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Gerichtsbeschreibungen, optimiert für lokales SEO bei Google und auf der Restaurant-Website."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Gastronomischer Kalender mit wichtigen Daten, Ideen und Hashtags für soziale Medien und Blog."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung professioneller Gerichte mit Rezept + CSV-Kalkulation zum Laden in das Kit de Escandallos Pro."
      }
    ],
    "metrics": [
      {
        "value": "−75 %",
        "label": "Zeit für Dienstpläne und Bestellungen"
      },
      {
        "value": "×4",
        "label": "Geschwindigkeit des Reportings an den Eigentümer"
      },
      {
        "value": "−40 %",
        "label": "Lebensmittelabfälle nach systematischer Kontrolle"
      },
      {
        "value": "11+",
        "label": "KI-Agenten für Ihre Rolle"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "8 Stunden pro Woche für manuelle Dienstplanung in Excel und Lieferantennotizen",
        "APPCC auf Papier, das verloren geht oder unvollständig zur Inspektion kommt",
        "Reporting an den Eigentümer in verstreuten E-Mail-Dateien ohne Struktur",
        "Lebensmittelabfälle nach Augenmaß erfasst, ohne echte Rückverfolgbarkeit oder Warnungen",
        "Improvisiertes Mitarbeiteressen, das die Kosten in die Höhe treibt, ohne dass es jemand bemerkt"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "2 Stunden pro Woche für Dienstpläne mit professioneller Vorlage unter Einhaltung des Tarifvertrags",
        "APPCC vom Handy mit Aufzeichnungen, Temperaturen und Warnungen, bereit für Inspektionen",
        "Reporting an den Eigentümer als PDF direkt aus dem Kit Plan Financiero, mit klaren Dashboards",
        "Systematische Kontrolle der Lebensmittelabfälle mit präzisen Daten und Bestandswarnungen",
        "KI-generiertes Mitarbeiteressen unter Einhaltung des Zielkostenrahmens und mit motiviertem Team"
      ]
    },
    "galleryTitle": "Der Alltag eines Managers in Bildern",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Schichtplanung, Küchen- und Saalmanagement, Inventar, Service und Reporting.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-shifts.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-kitchen.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-inventory.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-service.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-reporting.jpg"
    ]
  },
  "director-operaciones-grupo": {
    "h1": "KI für Betriebsleiter von Gastronomiegruppen",
    "heroSubtitle": "Standardisieren Sie Prozesse, konsolidieren Sie Reporting und vervielfachen Sie die operative Produktivität in Multi-Standort-Gruppen mit einer Suite spezialisierter KI-Agenten für die Gastronomie.",
    "heroTagline": "Gleicher Standard an allen Standorten, konsolidierte Daten mit einem Klick",
    "badge": "Für Betriebsleiter von Gruppen",
    "painsTitle": "Was ein Multi-Standort-Betriebsleiter unbedingt lösen muss",
    "pains": [
      "Den gleichen Qualitäts-, Prozess- und Erlebnisstandard an allen Standorten der Gruppe aufrechterhalten",
      "Finanzielle, operative und Team-KPIs konsolidieren, um die Leistung zwischen den Einheiten zu vergleichen",
      "Betriebshandbücher, Schulungen und Onboarding replizieren, ohne an Qualität zu verlieren, wenn das Netzwerk wächst",
      "Standorte mit Abweichungen bei Foodcost, Personal oder Produktivität frühzeitig erkennen, bevor sie Marge verlieren",
      "Die Manager jedes Standorts mit klarer Kommunikation und konsistentem Reporting koordinieren",
      "Die Gruppe durch Eröffnung neuer Einheiten skalieren, ohne bei jeder Eröffnung das Rad neu zu erfinden"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Betriebsleiter hilft",
    "features": [
      {
        "icon": "Building2",
        "title": "Multi-Standort-Standardisierung",
        "description": "Einheitliche Handbücher, Checklisten und Verfahren, die mit einem Klick auf alle Einheiten der Gruppe repliziert werden."
      },
      {
        "icon": "BarChart3",
        "title": "Konsolidierte Dashboards",
        "description": "Kit Plan Financiero: Vergleichen Sie Foodcost, Produktivität, Verluste und durchschnittlichen Bon aller Ihrer Restaurants in einer einzigen Ansicht."
      },
      {
        "icon": "ChefHat",
        "title": "Executive Chef Pro",
        "description": "Agent, der Rezepte und technische Datenblätter standardisiert, damit dasselbe Gericht in 1, 5 oder 25 Küchen gleich gelingt."
      },
      {
        "icon": "BriefcaseBusiness",
        "title": "Profi Restaurantmanager",
        "description": "Assistent für jeden Standortmanager, der mit konsolidierten Daten an den Betriebsleiter berichtet."
      },
      {
        "icon": "BookOpen",
        "title": "Betriebshandbücher mit KI",
        "description": "Onboarding, Teamschulungen und Verfahren, die von einem einzigen zentralen Repository aus immer aktuell gehalten werden."
      },
      {
        "icon": "ShieldCheck",
        "title": "Einheitliches unternehmensweites HACCP",
        "description": "Ein einziges Dokumentationssystem für alle Einheiten der Gruppe: zentralisierte Rückverfolgbarkeit und Temperaturen."
      },
      {
        "icon": "TrendingDown",
        "title": "Kostenprüfung pro Standort",
        "description": "Lebensmittelabfälle AI und Kit de Escandallos Pro erkennen Foodcost-Abweichungen, bevor sie außer Kontrolle geraten."
      },
      {
        "icon": "Users",
        "title": "Schichtpläne und Teamstruktur",
        "description": "Kit Gestión de Personal: gleiche Schichtstruktur, Kennzahlen und Produktivität in allen Einheiten."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Tiefgehende Recherche zu Trends, Wettbewerbern und Märkten für strategische Expansionsentscheidungen."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Betriebsleiters mit AI Chef Pro",
    "workflow": [
      "08:30 · Kaffee und Kit Plan Financiero – Sie öffnen das konsolidierte Dashboard der 7 Standorte der Gruppe und stellen fest, dass Standort 4 einen Foodcost von 33 % hat (+3 Prozentpunkte über dem Ziel).",
      "09:30 · Profi Restaurantmanager – Sie bitten den Agenten um eine automatisierte Ursachenanalyse pro Standort. Er identifiziert ein Problem bei den Fischverlusten.",
      "10:30 · Videocall mit der Managerin von Standort 4, gestützt auf echte Daten aus dem Kit Plan Financiero, nicht auf Intuition.",
      "12:00 · Executive Chef Pro – Sie aktualisieren das Verfahren zur Fischhandhabung, und es wird als neue Version des Handbuchs auf die 7 Küchen repliziert.",
      "15:30 · Konsolidierte Schichtpläne – Sie prüfen das Kit Gestión de Personal mit Produktivitätskennzahlen aller Standorte und zeichnen das Onboarding der neuen Managerin von Standort 8 ab.",
      "17:00 · Sonar Deep Research – Sie recherchieren den Markt für die nächste Eröffnung in einer anderen Stadt: Analyse von Lagen, durchschnittlichem Bon und Wettbewerb.",
      "19:00 · Besprechung mit dem Gremium – Sie exportieren die Quartals-KPIs direkt aus dem Kit Plan Financiero als PDF. Besprechung in 45 Minuten abgeschlossen.",
      "21:30 · Abschluss – die 7 Manager senden Ihnen den automatischen Tagesbericht per WhatsApp. Sie gehen mit einem vollständigen Überblick über die Gruppe nach Hause."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Gastronomiegruppen",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-tareas"
    ],
    "testimonialQuote": "Wir verwalten 7 Standorte und früher arbeitete jeder anders: verschiedene Excels, verschiedene Handbücher, verschiedene HACCP. Mit AI Chef Pro haben wir überall denselben Standard und konsolidiertes Reporting in einer einzigen Ansicht. Einen Standort mit Problemen zu erkennen, dauerte früher 2 Wochen, heute dauert es 1 Tag.",
    "testimonialAuthor": "Javier Ortega",
    "testimonialRole": "Betriebsleiter, Gastronomiegruppe mit 7 Standorten",
    "faqTitle": "Häufig gestellte Fragen von Betriebsleitern",
    "faqs": [
      {
        "q": "Wie viele Standorte unterstützt AI Chef Pro?",
        "a": "Keine echte Grenze. Es gibt Kunden mit 1 Standort und andere mit mehr als 25 aktiven Einheiten. Die Unternehmenspläne skalieren nach Nutzung und schalten konsolidierte Dashboards, personalisiertes Onboarding und Prioritäts-Support frei."
      },
      {
        "q": "Integriert es sich in unser ERP oder Buchhaltungssystem?",
        "a": "Die Vorlagen exportieren nach Excel, PDF und CSV in Formaten, die mit den meisten ERPs und Buchhaltungssystemen kompatibel sind. Ihr Finanzteam erhält Dokumentation, die bereit für die Integration ist."
      },
      {
        "q": "Ermöglicht es Rollen und Berechtigungen pro Standort?",
        "a": "Ja. Sie können Zugriff pro Standortmanager, pro Regionalleiter oder konsolidiert für den Betriebsleiter vergeben. Jede Ebene sieht nur die Daten, die ihr entsprechen."
      },
      {
        "q": "Wie wird der gleiche Standard in allen Einheiten sichergestellt?",
        "a": "Executive Chef Pro standardisiert Rezepte und technische Datenblätter; das Pack APPCC vereinheitlicht die Rückverfolgbarkeit; das Kit de Escandallos Pro hält in allen Standorten dieselben Berechnungen aufrecht. Die Handbücher werden mit einem Klick repliziert und von einem einzigen Punkt aus aktualisiert."
      },
      {
        "q": "Gibt es Rabatte für Gruppen mit mehreren Standorten?",
        "a": "Ja. Ab 5 aktiven Einheiten gibt es Unternehmenspläne mit personalisiertem Onboarding, konsolidierten Dashboards, Schulung des zentralen Teams und Prioritäts-Support."
      },
      {
        "q": "Hilft es, neue Standorte schneller zu eröffnen?",
        "a": "Ja. Es ist einer der häufigsten Anwendungsfälle: Die Leitfäden «Wie man ... eröffnet» (Dark Kitchen, gehobenes Restaurant, Casual, mexikanisch, japanisch, peruanisch, Nikkei) sind professionelle Roadmaps, die Eröffnungen mit Finanzplan, Businessplan und replizierbaren Handbüchern beschleunigen."
      }
    ],
    "ctaTitle": "Standardisieren Sie Ihre Gruppe. Gleicher Standard an allen Standorten.",
    "ctaSubtitle": "Sprechen Sie mit uns für ein personalisiertes Onboarding für Ihre Gruppe oder starten Sie mit dem Mitgliederplan: 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "KI für Betriebsleiter von Gastronomiegruppen | AI Chef Pro",
      "description": "KI-Suite für Multi-Standort-Gastronomiegruppen: konsolidierte Dashboards, Rezeptstandardisierung, unternehmensweites HACCP, replizierbare Handbücher und Finanzplan pro Einheit.",
      "keywords": "KI Gastronomiegruppe, Multi-Standort-Software Restaurants, Betriebsleiter Restaurant KI, Restaurantprozesse standardisieren, konsolidierte Dashboards Restaurant, Gastronomiegruppe skalieren, Multi-Standort KI Gastronomie",
      "ogImage": "https://aichef.pro/og/use-cases/director-operaciones-grupo.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Gruppe personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten «Wer sind Sie?», einem 2-minütigen Conversational Onboarding, bei dem Sie erzählen, wie viele Standorte Sie verwalten, welche Konzepte Sie betreiben (Casual, gehobene Gastronomie, Dark Kitchen, Hotel), in welchen Ländern und wie Ihre Organisation arbeitet. Ab diesem Moment antwortet jeder Agent – vom Finanzplan bis zu den Betriebshandbüchern – angepasst an die tatsächliche Größe und Struktur der Gruppe. Es ist kein Formular: Es ist ein kurzes Gespräch, das die Suite für Multi-Standort-Betriebsleiter wirklich nützlich macht.",
    "appsTitle": "Die KI-Agenten, die Sie als Betriebsleiter nutzen werden",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standardisierung von Rezepten, technischen Datenblättern und Handbüchern, die auf alle Einheiten der Gruppe replizierbar sind."
      },
      {
        "name": "Profi Restaurantmanager",
        "category": "Gastro Profile Pro",
        "description": "Assistent für jeden Standortmanager mit konsolidiertem Reporting nach oben."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Spezialist für Bistros, Gastrobars und Casual Dining: das häufigste Spektrum in Multi-Standort-Gruppen."
      },
      {
        "name": "Burger Pro AI+",
        "category": "Geschäftskonzepte",
        "description": "Für Gruppen mit Gourmet-Burger- oder Fast-Casual-Marken."
      },
      {
        "name": "Catering AI+",
        "category": "Geschäftskonzepte",
        "description": "Für Gruppen mit Catering-Abteilung und Firmenevents."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Tiefgehende Recherche zu Trends, Wettbewerbern und Märkten für strategische Entscheidungen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Präzise Daten zu Verlusten und Ausbeute pro Zutat, unverzichtbar für Multi-Standort-Audits."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Rezept, vereinheitlicht in allen Einheiten."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und Social Media",
        "description": "Blogbeiträge, um für jede Einheit der Gruppe organischen Traffic zu gewinnen."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Inhalte und Social Media",
        "description": "Keyword-Recherche nach Postleitzahlgebiet jedes Standorts."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Einheitliche gastronomische Fotografie mit KI für die gesamte Marke der Gruppe."
      }
    ],
    "metrics": [
      {
        "value": "−14 d",
        "label": "Standort mit Abweichungen erkennen"
      },
      {
        "value": "×7",
        "label": "Geschwindigkeit des konsolidierten Reportings"
      },
      {
        "value": "+3 pp",
        "label": "Marge nach Standardisierung"
      },
      {
        "value": "11+",
        "label": "Agenten für Multi-Standort"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "7 Standorte mit 7 verschiedenen Excels, heterogenen Handbüchern und inkonsistentem HACCP",
        "Das Erkennen eines Standorts mit Abweichungen dauert 2 Wochen, weil es kein konsolidiertes Reporting gibt",
        "Onboarding eines neuen Managers in 1 Monat mit improvisierten Materialien aus jeder Einheit",
        "Reporting an das Gremium mit verstreuten Dateien und ohne professionelle Dashboards",
        "Expansionsentscheidungen aus dem Bauch heraus, ohne tiefgehende Marktanalyse"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Gleicher Standard in allen 7 Einheiten repliziert: Rezepte, Handbücher und HACCP vereinheitlicht",
        "Standort mit Abweichungen in 1 Tag erkennen mit konsolidiertem Dashboard aus dem Kit Plan Financiero",
        "Onboarding eines neuen Managers in 1 Woche mit replizierbaren Handbüchern und Schulungen",
        "Reporting an das Gremium als PDF direkt aus dem Kit Plan Financiero mit konsolidierten KPIs",
        "Expansionsentscheidungen gestützt auf Sonar Deep Research und professionelle Leitfäden «Wie man ... eröffnet»"
      ]
    },
    "galleryTitle": "Der Alltag eines Betriebsleiters in Bildern",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren werden: Multi-Standort-Dashboards, Strategiebesprechungen, Audits der Einheiten, Unternehmenshandbücher und Onboarding von Managern.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-multilocal.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-meeting.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-audit.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-strategy.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-handover.jpg"
    ]
  },
  "chef-ejecutivo": {
    "h1": "KI für Executive Chef und Corporate Chef",
    "heroSubtitle": "Erstellen Sie standardisierte Rezepte, präzise Kalkulationen und replizierbare Handbücher für 1, 5 oder 25 Küchen. Eine Suite von gastronomischen KI-Agenten, die für eine der anspruchsvollsten Rollen der professionellen Küche entwickelt wurde.",
    "heroTagline": "Ihr kreatives und operatives Team, skaliert in der Geschwindigkeit eines Gesprächs",
    "badge": "Für Executive Chefs und Corporate Chefs",
    "painsTitle": "Was ein Executive Chef unbedingt lösen muss",
    "pains": [
      "Standardisierung von Rezepten in geografisch verteilten Küchen, ohne dass jeder Standort sie auf seine eigene Weise interpretiert",
      "Präzise Kalkulationen für jedes technische Rezeptblatt mit saisonalen Produkten, deren Preise sich wöchentlich ändern",
      "Die Karte alle 6–12 Wochen erneuern, ohne dass das Team im Papierkram untergeht",
      "Küchenhandbücher und Onboarding aktuell halten, wenn es ständige Personalfluktuation gibt",
      "Innovation bei saisonalen Menüs, ohne das Ziel-Food-Cost oder die tatsächliche Marge zu verlieren",
      "Berichterstattung an die Geschäftsleitung mit klaren KPIs: Rentabilität pro Gericht, Produktivität der Brigade und Lebensmittelabfälle"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Executive Chef hilft",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Executive Chef Pro",
        "description": "Spezialisierter KI-Agent für diese Rolle: Multi-Standardisierung, technische Rezeptblätter, Küchenhandbücher und Kartenentscheidungen auf Basis realer Daten."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche + Food Pairing AI",
        "description": "Ideenfindung für Gerichte nach Saison, Zutat oder Technik, mit wissenschaftlich fundierten Kombinationen. Kreativküche liefert außerdem das detaillierte Rezept und eine erste Kalkulation mit Referenzmarktpreisen, als CSV herunterladbar."
      },
      {
        "icon": "Calculator",
        "title": "Professionelle Kalkulationen",
        "description": "Sie laden das CSV von Kreativküche in das Kit de Escandallos Pro und ersetzen die Referenzpreise durch die Ihrer tatsächlichen Lieferanten. Kosten pro Portion, Food-Cost-%, Marge und empfohlener Preis sofort. Berechnet automatisch neu, wenn Sie ein Gramm oder einen Kostenpunkt ändern."
      },
      {
        "icon": "BookOpen",
        "title": "Professionelle technische Rezeptblätter",
        "description": "Rezept, Verfahren, Allergene, Anrichten und Storytelling in einem einzigen Dokument. Bereit zum Versand an alle Küchen der Gruppe."
      },
      {
        "icon": "Layers",
        "title": "Multi-Standardisierung",
        "description": "Dasselbe Gericht, dieselbe Qualität und dieselben Kosten in 1, 5 oder 25 Einheiten. Replizierbare und vollständig nachvollziehbare Handbücher."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+ und fortgeschrittene Techniken",
        "description": "Koji, Kombuchas, Shoyus, Garums und Lactofermente: gastronomische Forschung und Entwicklung mit professioneller Unterstützung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergen-ID und Lebensmittelabfälle AI",
        "description": "Automatische Erkennung von Allergenen pro Gericht und präzise Daten zu Lebensmittelabfällen und Ausbeuten pro Zutat."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Tiefgehende gastronomische Forschung: Trends, aufkommende Techniken, Produzenten und saisonale Produkte."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Mit KI generierte gastronomische Fotografie für technische Rezeptblätter, interne Kommunikation und Pressemitteilungen."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Executive Chefs mit AI Chef Pro",
    "workflow": [
      "Vormittag, 09:00 · Kreativküche – Ideenfindung für 12 Gerichte für die Herbstkarte auf Basis lokaler saisonaler Produkte. Der Agent liefert Ihnen ein detailliertes Rezept und eine erste Kalkulation mit Referenzmarktpreisen, als CSV herunterladbar.",
      "Vormittag, 10:30 · Kit de Escandallos Pro – Sie laden die 12 CSVs von Kreativküche hoch, ersetzen die Referenzpreise durch die Ihrer tatsächlichen Lieferanten und verwerfen 4 Gerichte, die nicht zu Ihrem Ziel-Food-Cost (28 %) passen.",
      "Mittag, 12:00 · Food Pairing AI – Sie arbeiten an der Kombination der 8 Finalisten und validieren unerwartete Harmonien.",
      "Nachmittag, 15:00 · Allergen-ID – Sie generieren das Allergenblatt pro Gericht, bereit für Regulierung und Service.",
      "Nachmittag, 16:30 · Executive Chef Pro – Sie verfassen das vollständige technische Rezeptblatt mit Verfahren, Grammagen, Anrichten und Storytelling.",
      "Nachmittag, 18:00 · GastroIMG Gen+ – Sie generieren die Fotos jedes Gerichts für das interne Handbuch und die Pressemitteilung.",
      "Nachmittag, 18:30 · Sie replizieren das Handbuch an die 5 Küchen der Gruppe. Was ein traditioneller Prozess in 15–30 Tagen abschließt, schließen Sie in 1–3 Arbeitstagen, je nach Umfang der Karte."
    ],
    "productsTitle": "Downloadbare Vorlagen und Kits für Executive Chefs",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-plan-financiero",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Früher brauchte ich zwischen 15 und 20 Tagen, um eine neue Speisekarte zu erstellen – inklusive Ideenfindung, Tests, Kalkulationen, technischen Rezeptblättern und interner Kommunikation. Mit AI Chef Pro schaffe ich das in 2 bis 3 Tagen, je nach Umfang der Karte und ob es sich um eine vollständige oder teilweise Neuaufsetzung handelt. Der Unterschied ist nicht nur zeitlich: Das Team erhält professionelle und reproduzierbare Dokumentation, keine handschriftlichen Notizen.",
    "testimonialAuthor": "Diego Saavedra",
    "testimonialRole": "Executive Chef, Gruppe von 5 mediterranen Restaurants",
    "faqTitle": "Häufig gestellte Fragen von Executive Chefs",
    "faqs": [
      {
        "q": "Verstehen die KI-Agenten von AI Chef Pro professionelle Küche oder sind sie allgemeine Chatbots?",
        "a": "Es sind spezialisierte Agenten. Kreativküche, Food Pairing AI, Fermentus mit AI+ und Executive Chef Pro sind mit professionellem gastronomischem Wissen trainiert: Techniken, echte Kalkulation, Rentabilität, Grammagen und Schnitte. Sie sind kein generisches ChatGPT: Sie sind Werkzeuge, die für jemanden entwickelt wurden, der bereits kochen kann."
      },
      {
        "q": "Kann ich mein bestehendes Rezeptbuch hochladen?",
        "a": "Ja. Das Kit de Escandallos Pro ermöglicht das Hochladen Ihres Rezeptbuchs und die automatisierte Kalkulation in Minuten. Sie können den Agenten Executive Chef Pro auch bitten, technische Rezeptblätter aus freien Beschreibungen zu generieren."
      },
      {
        "q": "Ist es für fortgeschrittene gastronomische Küche geeignet oder nur für Casual Dining?",
        "a": "Für das gesamte Spektrum. Es gibt spezifische Agenten: Kreativküche für Autorenküche, Kreative Patisserie, Fermentus für Avantgarde, VegChef für pflanzliche Küche, sowie über 25 Rezeptbücher pro Land. Reale Fälle bei Michelin und Repsol Soles und in Casual-Gruppen mit bis zu 25 Einheiten."
      },
      {
        "q": "Wie passt sich das System an meine Arbeitsweise an?",
        "a": "Beginnen Sie mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational Onboarding, in dem Sie erzählen, wer Sie sind, wo Sie arbeiten, Ihre Küchenart und in welchem Umfang. Ab diesem Moment passen sich alle Agenten an Ihren Kontext an: lokale Preise, Vorschriften Ihres Landes, regionale Küche und Umfang Ihres Betriebs."
      },
      {
        "q": "Gibt es etwas Spezifisches für Multi-Standort-Gruppen und Restaurantketten?",
        "a": "Ja. Der Agent Executive Chef Pro ist für die Standardisierung gedacht: dasselbe technische Rezeptblatt, dieselbe Kalkulation und dieselben Handbücher, repliziert in allen Einheiten. In Kombination mit dem Kit Plan Financiero können Sie das KPI-Reporting pro Einheit und Gruppe konsolidieren."
      },
      {
        "q": "Gibt es eine Bibliothek mit spezifischen Prompts für Köche?",
        "a": "Ja. Das Pro Prompts eBook enthält über 300 getestete Prompts für Kreativität, Kalkulation, technische Rezeptblätter, Schulung, interne Kommunikation und Küchenbetrieb, organisiert nach Anwendungssituation."
      },
      {
        "q": "Wie schnell amortisiert sich das Abonnement?",
        "a": "Die meisten Executive Chefs berichten von einer Amortisation bei der ersten neuen Karte. Ein traditioneller Menüwechsel dauert zwischen 15 und 30 Tagen, inklusive Ideenfindung, Tests, Kalkulationen, technischen Rezeptblättern und interner Kommunikation. Mit AI Chef Pro und einem guten Workflow in Excel oder Google Workspace reduziert sich derselbe Prozess auf 1 bis 3 Tage, je nach Umfang der Karte und ob es sich um eine vollständige oder teilweise Neuaufsetzung handelt. Bei 4–6 Kartenwechseln pro Jahr gewinnen Sie zwischen 60 und 120 Arbeitstage zurück."
      }
    ],
    "ctaTitle": "Erstellen, kalkulieren und replizieren Sie Rezepte in der Geschwindigkeit eines Gesprächs.",
    "ctaSubtitle": "Beginnen Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für die Nutzung aller Agenten.",
    "seo": {
      "title": "KI für Executive Chef: Rezepte, Kalkulationen und Handbücher | AI Chef Pro",
      "description": "KI-Suite für Executive und Corporate Chef: Agent Executive Chef Pro, automatische Kalkulationen, technische Rezeptblätter und replizierbare Multi-Standort-Handbücher. Beginnen Sie noch heute.",
      "keywords": "KI Executive Chef, Executive Chef KI, Software Corporate Chef, gastronomischer KI-Agent, automatische Kalkulationen, technische Rezeptblätter Restaurant, standardisierte Multi-Standort-Rezepte, Küchenhandbücher KI, Food Pairing KI, KI für Restaurantgruppen, Executive Chef Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/chef-ejecutivo.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Sie personalisiert",
    "personalizationBody": "AI Chef Pro startet mit einem 2-minütigen Conversational Onboarding – dem Agenten „Wer sind Sie?“ –, in dem Sie erzählen, wer Sie sind, wo Sie arbeiten, welche Küche Sie leiten und in welchem Umfang Sie operieren. Ab diesem Moment antwortet jeder Agent – von den Kalkulationen bis zur Kreativität – angepasst an Ihren Kontext: Ihre lokale Küche, Ihre Vorschriften, Ihre Marktpreise und die Größe Ihrer Brigade. Es ist kein Formular, sondern ein kurzes Gespräch, das allem, was danach kommt, Sinn verleiht.",
    "appsTitle": "Die KI-Agenten, die Sie als Executive Chef nutzen werden",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Hauptagent: Multi-Standardisierung, technische Rezeptblätter und Kartenentscheidungen."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung professioneller Gerichte mit detailliertem Rezept und erster Kalkulation, als CSV herunterladbar (Referenzmarktpreise), bereit zum Hochladen in das Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Kombinationen von Zutaten und Pairings mit wissenschaftlicher Basis."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Kreative Fermentation: Koji, Kombucha, Shoyu, Miso, Garum und Lactofermente."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Präzise Daten zu Lebensmittelabfällen und Ausbeuten pro Zutat. Unerlässlich für realistische Kalkulation."
      },
      {
        "name": "Calcula Pax",
        "category": "Werkzeuge und Utilities",
        "description": "Portionsrechner, der Rezepte auf jede Anzahl von Gästen skaliert."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Identifizierung potenzieller Allergene pro Rezept und Gericht."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Kreative Restaurant-Desserts mit professioneller Patisserie-Technik."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für Auswahl und Technik mit dem professionellen Sosa-Katalog."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für den tSpoonLab-Katalog für fortgeschrittene Techniken und Anwendungen."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Tiefgehende Recherche: Trends, Produzenten und aufkommende Techniken."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Mit KI generierte gastronomische Fotografie für technische Rezeptblätter und Presse."
      },
      {
        "name": "Gastro Lexikum",
        "category": "Gastro-Wissen",
        "description": "Tutor mit Definitionen zu Techniken, Prozessen, Zusatzstoffen und gastronomischer Wissenschaft."
      }
    ],
    "metrics": [
      {
        "value": "−90 %",
        "label": "Zeit für die Erstellung einer neuen Karte"
      },
      {
        "value": "×10",
        "label": "Geschwindigkeit technischer Rezeptblätter"
      },
      {
        "value": "+4 pp",
        "label": "Marge durch bessere Kalkulation"
      },
      {
        "value": "13+",
        "label": "KI-Agenten für Ihre Rolle"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Abschluss einer neuen Karte: zwischen 15 und 30 Tagen, abhängig von der Standardisierung des Prozesses",
        "Rezeptbuch in losen Blättern, ungeordnete Word-Dokumente und handschriftliche Notizen",
        "Jeder Standort interpretiert das Rezept auf seine eigene Weise und das Ergebnis variiert",
        "Manuelle Kalkulation mit Taschenrechner: Sie ändern ein Gramm und schreiben alles neu",
        "Handbücher und Onboarding ständig veraltet"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Abschluss einer neuen Karte: zwischen 1 und 3 Tagen, je nach Umfang und ob es sich um eine vollständige oder teilweise Neuaufsetzung handelt",
        "Zentralisiertes Rezeptbuch mit Kalkulation, Allergenen, Technik und Storytelling",
        "Dasselbe Gericht, dieselbe Qualität und dieselben Kosten in 1, 5 oder 25 Küchen",
        "Professionelle Kalkulation, die bei jeder Änderung sofort neu berechnet",
        "Handbücher mit einem Klick aktualisiert und Onboarding bereit für neue Köche"
      ]
    },
    "appUrlPath": "/agents/chef-ejecutivo-pro",
    "galleryTitle": "Der Alltag eines Executive Chefs in Bildern",
    "gallerySubtitle": "Was Sie mit AI Chef Pro verwalten können: Brigade, technische Rezeptblätter, Kreativität, Kalkulationen und interne Kommunikation.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-recipes.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-brigade.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-creativity.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-meeting.jpg"
    ]
  },
  "chef-cocina": {
    "h1": "KI für Küchenchefs und Chefköche",
    "heroSubtitle": "Verwalten Sie Stationen, Kalkulationen, Mise en Place und Schulung des Teams mit einer Suite von KI-Agenten, die auf den Alltag des professionellen Küchenchefs zugeschnitten ist.",
    "heroTagline": "Mehr Küche, weniger Papierkram",
    "badge": "Für Chefköche und Küchenchefs",
    "painsTitle": "Was ein Küchenchef unbedingt lösen muss",
    "pains": [
      "Den präzisen Wareneinsatz jedes Gerichts und der gesamten Karte mit Produkten zu berechnen, deren Preise sich wöchentlich ändern",
      "Mise en Place und Stationen ohne Abstimmungsprobleme in den Service-Spitzenzeiten koordinieren",
      "Das HACCP aktuell halten, ohne dass Papierkram der Küche Zeit stiehlt",
      "Das Team bei häufiger Rotation in standardisierten Techniken und Abläufen schulen und beaufsichtigen",
      "Die Karte jede Saison erneuern, dabei Marge halten und lokale Produkte respektieren",
      "Mit Service, Leitung und Lieferanten mit professioneller Dokumentation kommunizieren, nicht mit Notizen im Notizbuch"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Küchenchef hilft",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Executive Chef Pro",
        "description": "Spezialisierter Agent, der Sie bei der Standardisierung von Rezepten, Rezeptblättern und Küchenhandbüchern unterstützt."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche + Food Pairing AI",
        "description": "Ideenfindung für neue Gerichte mit professioneller Basis. Kreativküche liefert Rezept + Kalkulation als CSV mit Referenzpreisen, bereit für das Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Professionelle Rezeptkalkulationen",
        "description": "Kit de Escandallos Pro: Sie laden die CSV aus Kreativküche, ersetzen Preise durch die realen und erhalten sofort Kosten, Wareneinsatz-% und Marge."
      },
      {
        "icon": "BookOpen",
        "title": "Professionelle Rezeptblätter",
        "description": "Rezept, Verfahren, Allergene, Anrichten und Storytelling in einem einzigen druckfertigen Dokument."
      },
      {
        "icon": "CheckSquare",
        "title": "Aufgaben und Mise en Place",
        "description": "Kit de Tareas mit spezifischen Vorlagen je Konzept: Eröffnung, Abschluss, Stationen und Service."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP und Rückverfolgbarkeit",
        "description": "Pack APPCC mit 19 Vorlagen: Temperaturen, Lebensmittelabfälle, Allergene und Rückverfolgbarkeit über das Handy des Teams."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Gastronomische Forschung & Entwicklung: Koji, Kombucha, Shoyu, Garum und Lactofermente mit professioneller Unterstützung."
      },
      {
        "icon": "GraduationCap",
        "title": "Pro Prompts eBook",
        "description": "Über 300 erprobte Prompts für Kreativität, Kalkulation, Rezeptblätter, Ausbildung und Küchenbetrieb."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergen-ID und Lebensmittelabfälle AI",
        "description": "Automatische Erkennung von Allergenen pro Gericht und präzise Daten zu Lebensmittelabfällen und Ausbeuten pro Zutat."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Küchenchefs mit AI Chef Pro",
    "workflow": [
      "08:00 · Eröffnung – Sie drucken die Mise en Place des Tages aus dem Kit de Tareas und validieren Bestellungen bei Lieferanten mit dem Kit Inventario.",
      "09:00 · Kreativküche – Sie entwickeln ein Gericht außerhalb der Karte für das Wochenende mit Produkten zu günstigem Preis. Sie erhalten Rezept + Kalkulation als CSV.",
      "10:30 · Kit de Escandallos Pro – Sie laden die CSV, wenden Ihre realen Preise an und prüfen, dass der Wareneinsatz bei 28 % stimmt.",
      "12:30 · Service – das Team erfasst Lebensmittelabfälle und Temperaturen vom Handy aus mit dem Pack APPCC. Sie stehen an der Station, nicht im Büro.",
      "15:30 · Kurzes Briefing mit der Brigade, um das Tagesgericht zu besprechen und die Mise en Place anzupassen.",
      "17:00 · Pro Prompts eBook – Sie bitten den Agenten, Ihnen das Skript für die Schulung eines neuen Kochs zu erstellen, der morgen anfängt.",
      "19:30 · Abendservice – Sie koordinieren die Serviceabläufe mit dem Team, gestützt auf die zentralisierten Rezeptblätter.",
      "23:30 · Abschluss – Sie unterschreiben das HACCP des Tages, generieren den Bericht und er geht in 10 Minuten an das WhatsApp des Eigentümers."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Küchenchefs",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "kit-tareas",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Das Kit de Escandallos und das Pack APPCC haben mir 5 Stunden Papierkram pro Woche erspart. Aber was ich am häufigsten nutze, ist Kreativküche für Gerichte außerhalb der Karte am Wochenende: An einem Morgen schließe ich Rezept, Kalkulation und Rezeptblatt ab. Früher war das eine ganze Woche.",
    "testimonialAuthor": "Lucía Romero",
    "testimonialRole": "Küchenchefin, mediterranes Restaurant mit 70 Plätzen",
    "faqTitle": "Häufig gestellte Fragen von Küchenchefs",
    "faqs": [
      {
        "q": "Muss ich ein Excel-Experte sein?",
        "a": "Nein. Die Vorlagen des Kit de Escandallos Pro und des Pack APPCC enthalten vorbefüllte Formeln; Sie geben nur Daten ein. Es gibt ein 5-minütiges Video-Tutorial für den Start."
      },
      {
        "q": "Funktioniert das, wenn sich unsere Karte jeden Monat oder jede Saison ändert?",
        "a": "Das ist der Idealfall. Kreativküche erzeugt neue Gerichte mit Kalkulation als CSV; Sie laden sie mit Ihren Preisen in das Kit de Escandallos Pro und exportieren die Rezeptblätter. Was früher eine Woche Arbeit war, wird zu einem Arbeitstag."
      },
      {
        "q": "Versteht die KI professionelle Kochbegriffe?",
        "a": "Ja. Kreativküche, Food Pairing AI, Fermentus mit AI+ und die Länderrezepturen (italienisch, mexikanisch, japanisch, peruanisch usw.) sind mit professionellem gastronomischem Wissen trainiert: Techniken, Kalkulation, Grammagen, Schnitte, Anrichten und Storytelling. Sie sind kein generisches ChatGPT."
      },
      {
        "q": "Wie passt es sich an Ihre konkrete Küche an?",
        "a": "Sie beginnen mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Gesprächs-Onboarding, in dem Sie erzählen, welche Küche Sie führen, wo Sie arbeiten und in welchem Umfang. Ab diesem Moment antworten alle Agenten passend zu Ihrem realen Kontext."
      },
      {
        "q": "Kann ich alles in Excel und PDF herunterladen?",
        "a": "Ja. Die gesamte Dokumentation ist exportierbar und bearbeitbar: Kalkulationen, Rezeptblätter, HACCP, Mise en Place und Schulung des Teams."
      },
      {
        "q": "Funktioniert es für Küchen mit fortgeschrittenen Techniken (Fermente, Sphärifikationen, langes Garen)?",
        "a": "Ja. Fermentus mit AI+ deckt avantgardistische Fermentation ab (Koji, Kombucha, Shoyu, Miso, Garum, Lactofermente) und Kreativküche versteht Techniken wie Sous vide, Sphärifikation, Gelierung und kontrolliertes langes Garen."
      }
    ],
    "ctaTitle": "Mehr Küche, weniger Papierkram. Gewinnen Sie Stunden für das zurück, was zählt.",
    "ctaSubtitle": "Start mit dem 2-Minuten-Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Küchenchefs und Chefköche: Kalkulationen, Rezeptblätter und HACCP | AI Chef Pro",
      "description": "KI-Suite für professionelle Küchenchefs: spezialisierte Agenten, Kalkulationen, Rezeptblätter, Mise en Place und HACCP mit echter gastronomischer Unterstützung. Starten Sie heute.",
      "keywords": "KI Küchenchef, Software für Küchenchefs, KI für Küchenchefs, Küchenkalkulation, Rezeptblätter KI, HACCP Küche, Mise en Place KI, gastronomischer KI-Agent, Küchenchef Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/chef-cocina.jpg"
    },
    "personalizationTitle": "Von Minute eins an auf Ihre Küche zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Gesprächs-Onboarding, in dem Sie erzählen, welche Küche Sie führen, in welcher Stadt, welche Art von Karte Sie verwalten und in welchem Umfang Sie arbeiten. Ab diesem Moment antwortet jeder Agent – von der Kalkulation bis zur Kreativität – passend zu Ihrem Kontext: lokale Produkte, Vorschriften Ihres Landes, Größe Ihres Teams und reales Budget. Es ist kein Formular: Es ist ein kurzes Gespräch, das die Suite für Ihren Alltag an der Station wirklich nützlich macht.",
    "appsTitle": "Die KI-Agenten, die Sie als Küchenchef nutzen werden",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standardisierung von Rezepten, Rezeptblättern und Küchenhandbüchern."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung professioneller Gerichte mit Rezept + Kalkulation als CSV, bereit für das Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Kombinationen von Zutaten und Pairings auf wissenschaftlicher Basis."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Gastronomische Forschung & Entwicklung: kreative Fermentation von Koji, Kombucha, Shoyu, Miso und Garum."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Kreative Restaurant-Desserts mit professioneller Patisserie-Technik."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Präzise Daten zu Lebensmittelabfällen und Ausbeuten pro Zutat."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools und Utilities",
        "description": "Portionsrechner, der Rezepte auf jede beliebige Personenzahl skaliert."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools und Utilities",
        "description": "Umrechner für Gewichte und Maße für die professionelle Küche."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Rezept und Gericht."
      },
      {
        "name": "Mitarbeiteressen AI",
        "category": "Gastro Profile Pro",
        "description": "Generator für Mitarbeitermenüs, der Kosten spart und das Team motiviert."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Assistent mit dem professionellen Katalog von Sosa für fortgeschrittene Techniken."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für den tSpoonLab-Katalog für technische Anwendungen."
      },
      {
        "name": "Gastro Lexikum",
        "category": "Gastro-Wissen",
        "description": "Tutor mit Definitionen von Techniken, Prozessen und gastronomischer Wissenschaft."
      }
    ],
    "metrics": [
      {
        "value": "−5 h",
        "label": "weniger Papierkram pro Woche"
      },
      {
        "value": "×7",
        "label": "schneller zur neuen Karte"
      },
      {
        "value": "+3 pp",
        "label": "Marge nach realer Kalkulation"
      },
      {
        "value": "13+",
        "label": "KI-Agenten für Ihre Küche"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Rezeptsammlung in Notizbuch und losen Blättern, je nach Koch unterschiedliche Versionen",
        "Manuelle Kalkulation mit dem Taschenrechner bei jedem Preiswechsel",
        "HACCP auf bedrucktem Papier, das sich stapelt und niemand prüft",
        "Die Kartenerneuerung dauert 15 bis 30 Tage mit Ideenfindung, Kalkulationen und Rezeptblättern",
        "Improvisierte Teameinarbeitung bei jedem neuen Mitarbeiter"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Zentralisierte Rezeptsammlung mit Kalkulation, Allergenen, Technik und Storytelling",
        "Automatische Kalkulation, die bei jeder Preisänderung sofort neu berechnet",
        "HACCP vom Handy mit Aufzeichnungen und Warnungen, bereit für Inspektionen",
        "Kartenerneuerung in 1-3 Tagen mit Kreativküche + Kit de Escandallos Pro",
        "Replizierbare Schulungshandbücher mit dem Skript aus dem Pro Prompts eBook"
      ]
    },
    "galleryTitle": "Der Alltag eines Küchenchefs in Bildern",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Brigade, Mise en Place, Rezeptblätter, Pass, Lager und Schulung des Teams.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-recipes.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-pass.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-storage.jpg"
    ]
  },
  "sous-chef": {
    "h1": "KI für Sous Chef",
    "heroSubtitle": "Organisieren Sie Stationen, verwalten Sie die Mise en Place, überwachen Sie das Team und gewinnen Sie administrative Stunden zurück – mit einer Suite von KI-Agenten, die speziell für den Sous Chef in der Profiküche entwickelt wurden.",
    "heroTagline": "Die rechte Hand des Küchenchefs, mit System",
    "badge": "Für Sous Chefs",
    "painsTitle": "Was ein Sous Chef unbedingt lösen muss",
    "pains": [
      "Stationen und Mise en Place präzise koordinieren, wenn das Tempo keine Pause kennt",
      "Den Küchenchef vertreten, wenn er nicht da ist, ohne dass Qualität oder Betrieb darunter leiden",
      "Das Küchenteam mit konsistenten Kriterien schulen und überwachen",
      "Die APPCC-Rückverfolgbarkeit aktuell halten, ohne dass sich Papierkram ansammelt",
      "Während des Service schnellen Zugriff auf aktuelle Rezepturen haben",
      "Kalkulationen validieren, wenn neue Zutaten kommen oder sich ein Lieferant ändert"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Sous Chef hilft",
    "features": [
      {
        "icon": "CheckSquare",
        "title": "Mise en Place und Aufgaben pro Station",
        "description": "Kit de Tareas mit strukturierten Listen nach Schicht und Station, jeden Morgen druckbereit."
      },
      {
        "icon": "BookOpen",
        "title": "Immer aktuelle Rezepturen",
        "description": "Schneller Zugriff vom Handy auf Rezept, Ablauf, Anrichten und Allergene jedes Gerichts während des Service."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC vom Handy aus",
        "description": "Pack APPCC mit Protokollen, Temperaturalarmen und PDF-Export. Das Team erfasst alles vom Handy aus, ohne Papierkram."
      },
      {
        "icon": "Calculator",
        "title": "Schnelle Kalkulationen",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; das Kit de Escandallos Pro verwaltet diese mit Ihren realen Preisen, und Sie validieren die Marge sofort."
      },
      {
        "icon": "GraduationCap",
        "title": "Team-Schulung",
        "description": "Pro Prompts eBook + Executive Chef Pro erstellen Handbücher und Onboarding-Materialien für neue Köche."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Gastronomischer KI-Chat zur Lösung technischer Fragen, Vorschlägen für Gerichte außerhalb der Karte und Validierung von Techniken in Echtzeit."
      },
      {
        "icon": "Users",
        "title": "Mitarbeiteressen AI",
        "description": "Generator für Personalmenüs, der Produkte aus Ihrem Lager nutzt und das Team motiviert."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergen-ID und Lebensmittelabfälle AI",
        "description": "Automatische Allergenerkennung und präzise Daten zu Ausschuss für Station und Durchlauf."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Sous Chefs mit AI Chef Pro",
    "workflow": [
      "07:30 · Eröffnung – Sie öffnen das Kit de Tareas und überprüfen die Mise en Place des Tages. Sie zeichnen das kritische Inventar mit dem Kit Inventario ab.",
      "08:30 · Kurzes Briefing mit der Brigade – Sie besprechen die Tagesstationen mit den zentralisierten Rezepturen in der Hand.",
      "12:00 · Mittagsservice – Sie überwachen die Stationen, das Team erfasst Ausschuss und Temperaturen vom Handy aus mit dem Pack APPCC.",
      "15:30 · Kreativküche – Der Küchenchef bittet Sie um ein Gericht außerhalb der Karte für Samstag. Sie generieren Gericht + CSV-Kalkulation in 20 Minuten.",
      "16:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren realen Preisen, validieren, dass die Food-Cost bei 28 % stimmt, und exportieren das Rezeptblatt.",
      "17:30 · Mitarbeiteressen AI – Sie bereiten das Personalmenü für die nächste Woche vor, unter Berücksichtigung von Zielkosten und Lagerbestand.",
      "20:00 · Abendservice – Sie koordinieren die Stationen mit der Brigade und klären Fragen mit Kreativküche, wenn der Jungkoch eine Technik bestätigt haben möchte.",
      "23:30 · Abschluss – Sie zeichnen APPCC ab, bereiten die Mise en Place für den nächsten Tag vor und senden den Bericht an den Küchenchef."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Sous Chefs",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Sous Chef zu sein bedeutet, an tausend Orten gleichzeitig zu sein. Die Mise-en-Place-Listen des Kit de Tareas und die APPCC-Protokolle vom Handy aus haben das Chaos organisiert. Wenn der Küchenchef nicht da ist, läuft alles weiter, weil die Abläufe dokumentiert sind.",
    "testimonialAuthor": "Nicolás Vega",
    "testimonialRole": "Sous Chef, Restaurant mit 100 Plätzen",
    "faqTitle": "Häufig gestellte Fragen von Sous Chefs",
    "faqs": [
      {
        "q": "Passen sich die Vorlagen an den Stil meiner Küche an?",
        "a": "Ja. Es gibt spezifische Kit de Tareas für jedes Konzept (Casual, Gourmet, Dark Kitchen, Hotel, Pizzeria, Burgerladen, Konditorei, Bar, Catering, Eisdiele, Schokoladenmanufaktur, kreatives Restaurant, Privatkoch) und alle lassen sich an den Stil Ihrer Küche anpassen."
      },
      {
        "q": "Funktioniert es vom Handy aus für die Erfassungen des Teams?",
        "a": "Ja. Die APPCC-Protokolle, Ausschuss, Temperaturen und Aufgaben-Checks werden vom Handy des Teams aus erfasst, ohne Installation. Am Ende des Tages wird ein PDF für den Küchenchef oder den Eigentümer exportiert."
      },
      {
        "q": "Ist es für das Team schwierig zu bedienen?",
        "a": "Nein. Das Team füllt nur Felder aus oder setzt Häkchen. Die tatsächliche Lernkurve beträgt 1 Tag. Es gibt ein 5-minütiges Onboarding-Video."
      },
      {
        "q": "Nützt es, wenn nicht ich über die Werkzeuge in der Küche entscheide?",
        "a": "Sie können mit dem Mitgliederplan beginnen (10 € pro Monat, 10.000 Credits) für Ihre eigenen Listen und Vorschläge. Nach 1–2 Wochen Nutzung schlagen Sie dem Küchenchef konkrete Daten vor: gesparte Zeit, validierte Kalkulationen, organisierte Mise en Place."
      },
      {
        "q": "Wie hilft es mir in Service-Spitzenzeiten?",
        "a": "Die zentralisierten Rezepturen geben Ihnen während des Durchlaufs schnellen Zugriff vom Handy. Bei technischen Fragen antwortet Kreativküche in Sekunden. Mental Coach hilft auch, Stress in Hochdruckküchen zu bewältigen."
      },
      {
        "q": "Gibt es etwas Spezielles für den Aufstieg zum Küchenchef?",
        "a": "Ja. Pro Prompts eBook (300+ professionelle Prompts), Executive Chef Pro (Multi-Standort-Standardisierung) und Gastro Lexikum (Technik-Referenz) sind Schlüsselwerkzeuge, um auf die nächste Stufe zu wachsen."
      }
    ],
    "ctaTitle": "Organisieren Sie Ihre Küche ohne lose Zettel.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für die Nutzung aller Agenten.",
    "seo": {
      "title": "KI für Sous Chef: Mise en Place, Rezepturen und APPCC | AI Chef Pro",
      "description": "KI-Suite für Sous Chefs in der Profiküche: Mise en Place, zentralisierte Rezepturen, Kalkulationen, APPCC vom Handy und Team-Schulung. Starten Sie noch heute.",
      "keywords": "KI Sous Chef, Software Sous Chef, Mise en Place Küche KI, APPCC Sous Chef, Rezepturen Küche, Küchenbrigade Schulung, Sous Chef Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/sous-chef.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Küche personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding-Gespräch, in dem Sie erzählen, welche Küche Sie führen, in welcher Stadt, welche Karte Sie haben und in welchem Umfang. Ab diesem Moment antwortet jeder Agent – von der Mise en Place bis zu den Kalkulationen – angepasst an Ihren Kontext: Serviceart, Größe der Brigade und reale Abläufe. Es ist kein Formular, sondern ein kurzes Gespräch, das die Suite für den Arbeitsrhythmus wirklich nützlich macht.",
    "appsTitle": "Die KI-Agenten, die Sie als Sous Chef nutzen werden",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standardisierung von Rezepten, Rezepturen und zentralisierten Küchenhandbüchern."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung professioneller Gerichte mit Rezept + CSV-Kalkulation, bereit für das Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Wissenschaftlich fundierte Zutatenkombinationen und Pairings."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Kreative Restaurant-Desserts mit professioneller Patisserie-Technik."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools und Utilities",
        "description": "Portionsrechner, der Rezepte auf jede Anzahl von Gästen skaliert."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools und Utilities",
        "description": "Umrechner für Gewichte und Maße für die Profiküche."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Präzise Daten zu Ausschuss und Ausbeute pro Zutat."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Allergenerkennung pro Rezept und Gericht."
      },
      {
        "name": "Mitarbeiteressen AI",
        "category": "Gastro Profile Pro",
        "description": "Generator für Personalmenüs mit Produkten, die Sie bereits auf Lager haben."
      },
      {
        "name": "Mental Coach",
        "category": "Tools und Utilities",
        "description": "Psychologisches Coaching zur Bewältigung von Stress und schwierigen Gesprächen in der Küche."
      },
      {
        "name": "Gastro Lexikum",
        "category": "Gastro-Wissen",
        "description": "Tutor mit Definitionen zu Techniken, Prozessen und gastronomischer Wissenschaft."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "Geschwindigkeit Mise en Place"
      },
      {
        "value": "−4 h",
        "label": "wöchentlich Papierkram"
      },
      {
        "value": "gleich",
        "label": "Standard, wenn der Chef nicht da ist"
      },
      {
        "value": "11+",
        "label": "Agenten für Ihre Rolle"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Mise en Place wird jeden Morgen dem Team diktiert, jeden Tag anders",
        "APPCC auf Papier, das sich am Ende der Woche stapelt",
        "Rezepturen im Notizbuch des Küchenchefs, während des Service unzugänglich",
        "Wenn der Küchenchef nicht da ist, sinken Qualität und Betrieb",
        "Improvisierte und uneinheitliche Schulung neuer Köche"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Täglich druckbare Mise en Place mit dem Kit de Tareas, strukturiert nach Station",
        "APPCC vom Handy mit Protokollen, Alarmen und PDF-Export zum Abschluss",
        "Zentralisierte Rezepturen, während des Service vom Handy aus zugänglich",
        "Dokumentierte Abläufe – der Standard bleibt erhalten, auch wenn sich das Team ändert",
        "Reproduzierbare Schulung mit Skript aus dem Pro Prompts eBook und Handbüchern des Executive Chef Pro"
      ]
    },
    "galleryTitle": "Der Alltag eines Sous Chefs in Bildern",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Mise en Place, Vorbereitung, Teamüberwachung, Service in der Linie und Rückverfolgbarkeit.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-sous-chef-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-cooking.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-supervise.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-clipboard.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-station.jpg"
    ]
  },
  "chef-catering": {
    "h1": "KI für Catering-Köche",
    "heroSubtitle": "Entwerfen Sie Eventmenüs, kalkulieren Sie pro Service und planen Sie Produktion in großem Maßstab mit einer Suite von KI-Agenten für professionelles Catering und Eventköche.",
    "heroTagline": "Produktion in großem Maßstab ohne Marge oder Qualität zu verlieren",
    "badge": "Für Catering-Köche und Eventveranstalter",
    "painsTitle": "Was ein Catering-Koch unbedingt lösen muss",
    "pains": [
      "Menüs mit stark schwankender Gästezahl (50, 200, 500) kalkulieren, wenn die Zutatenpreise jede Woche wechseln",
      "Produktion, Mise en Place und Einkäufe in großem Maßstab ohne Abweichungen planen",
      "Logistik, Transport und Aufbau in der Location des Kunden unter Einhaltung von Zeiten und Temperaturen koordinieren",
      "APPCC und Rückverfolgbarkeit außerhalb der festen Küche, in fremden Locations und Kühlfahrzeugen sicherstellen",
      "Kreative Menüs pro Eventtyp (Hochzeit, Firmenfeier, Cocktail, Gala) entwerfen, ohne jedes Mal das Rad neu zu erfinden",
      "Mit Produktionsteam, Transport und Service über klare Dokumentation kommunizieren"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Catering-Koch hilft",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Spezialisierter Agent für Catering und gastronomische Events: Hochzeiten, Firmenfeiern, Cocktails und Galas mit professionellem Wissen."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche + Food Pairing AI",
        "description": "Ideenfindung für Eventmenüs. Kreativküche liefert Rezept + CSV-Kalkulation, bereit für das Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Event",
        "description": "Kit de Escandallos Pro: Sie laden die CSV mit Ihren echten Preisen, passen die Gästezahl an und erhalten sofort Kosten, Food-Cost-% und Marge."
      },
      {
        "icon": "Layers",
        "title": "Calcula Pax",
        "description": "Portionsrechner, der Rezepte in Sekunden auf 50, 200, 500 oder 1000 Gäste skaliert."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Catering",
        "description": "Spezifische Vorlagen für Produktion, Transport, Aufbau, Service und Abbau in der Location des Kunden."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC außer Haus",
        "description": "Pack APPCC mit Vorlagen, die auf reisende Produkte zugeschnitten sind: Rückverfolgbarkeit, Transporttemperatur und Protokolle in fremden Locations."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Food-Fotografie mit KI für Kundenpräsentationen, Eventvorschläge und Pressemitteilungen."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergen-ID",
        "description": "Automatische Allergenerkennung, entscheidend für Events mit vielen Gästen mit unterschiedlichen Ernährungsprofilen."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients AI",
        "description": "Assistent für die Auswahl technischer Zutaten aus dem Sosa-Katalog, besonders nützlich bei Cocktails und Desserts."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Catering-Kochs mit AI Chef Pro",
    "workflow": [
      "08:30 · Catering AI+ – der Agent hilft Ihnen, den Menüvorschlag für eine Hochzeit mit 180 Gästen gemäß Kundenbriefing abzuschließen.",
      "09:30 · Kreativküche – Sie entwickeln die 12 Gerichte des Menüs mit detailliertem Rezept und CSV-Kalkulation mit Referenzpreisen.",
      "10:30 · Calcula Pax + Kit de Escandallos Pro – Sie skalieren auf 180 Gäste, laden die CSV mit Ihren echten Preisen und validieren die Zielmarge.",
      "12:00 · Validierung mit dem Kunden – Sie exportieren den Vorschlag mit technischen Datenblättern und Food-Fotografie von GastroIMG Gen+.",
      "14:00 · Kit de Tareas Catering – Sie planen Produktion, Transport, Aufbau, Service und Abbau des Events am Samstag.",
      "16:00 · APPCC außer Haus – Sie bereiten Temperaturprotokolle für den Transport und Rückverfolgbarkeit in der fremden Location mit dem Pack APPCC vor.",
      "18:00 · Allergen-ID – Sie erstellen das Allergenblatt pro Gericht, bereit für den Service und für Gäste mit Einschränkungen.",
      "19:30 · Briefing an das Team – Sie erstellen das Service-Briefing mit Küchen- und Serviceteam des Events, alles aus einer einzigen Quelle."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Catering-Köche",
    "productIds": [
      "kit-tareas-catering",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Die Kalkulationen pro Event sparen mir Stunden. Ich schließe ein Menü für 200 Gäste mit validierter Marge in 30 Minuten ab. Früher war das ein halber Nachmittag mit Taschenrechner und Servietten. Und das APPCC, das an Events außer Haus angepasst ist, hat uns bei Firmenkunden einen riesigen Kopfschmerz erspart.",
    "testimonialAuthor": "Andrea Costa",
    "testimonialRole": "Catering-Koch, Spezialist für Firmenevents und Hochzeiten",
    "faqTitle": "Häufige Fragen von Catering-Köchen",
    "faqs": [
      {
        "q": "Funktioniert das für jede Catering-Größe?",
        "a": "Ja. Von Boutique-Caterings mit 50 Gästen pro Monat bis zu Unternehmen mit über 1000 Services pro Monat und Events mit 2000 Gästen."
      },
      {
        "q": "Kann die Schwankung der Gästezahl verwaltet werden?",
        "a": "Ja. Calcula Pax skaliert Rezepte auf jede Gästezahl und das Kit de Escandallos Pro berechnet Kosten, Food-Cost und Marge automatisch neu."
      },
      {
        "q": "Deckt das APPCC außerhalb der festen Küche ab?",
        "a": "Ja. Das Pack APPCC enthält spezifische Vorlagen für Produkte, die im Rucksack, mit dem Motorrad, im Kühltransporter oder aus der Zentralküche reisen, einschließlich Rückverfolgbarkeit in der fremden Location."
      },
      {
        "q": "Gibt es spezifische Catering-Vorlagen?",
        "a": "Ja. Das Kit de Tareas Catering enthält detaillierte Listen für Produktion, Transport, Aufbau vor Ort, Service und Abbau sowie Koordinationsprotokolle mit der Zentralküche."
      },
      {
        "q": "Wie passt es sich an meine Catering-Art an?",
        "a": "Sie starten mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding, bei dem Sie erzählen, welche Eventtypen Sie machen (Hochzeiten, Firmenfeiern, Cocktails, Galas), die durchschnittliche Gästezahl, die Stadt und Ihre Arbeitsweise. Alles passt sich Ihrem Kontext an."
      },
      {
        "q": "Eignet es sich für innovative Menügestaltung?",
        "a": "Ja. Catering AI+ + Kreativküche + Food Pairing AI + Fermentus mit AI+ arbeiten zusammen, um kreative Menüs mit professioneller Basis zu entwerfen – keine kopierten Rezepte aus dem Internet."
      }
    ],
    "ctaTitle": "Gestalten, kalkulieren und produzieren Sie Events ohne lose Zettel.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Catering-Köche: Menüs, Kalkulationen und Event-APPCC | AI Chef Pro",
      "description": "KI-Suite für Catering-Köche: Catering AI+, Kreativküche, Calcula Pax, Kalkulation pro Event, APPCC außer Haus und Produktionsplanung in großem Maßstab. Starten Sie noch heute.",
      "keywords": "KI Catering-Koch, Catering-Koch Software, Catering Kalkulation KI, Catering Event Software, APPCC Catering, Hochzeitsmenü KI, gastronomisches Eventmanagement KI, Catering-Koch Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/chef-catering.jpg"
    },
    "personalizationTitle": "Von Minute eins auf Ihre Catering-Art personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational-Onboarding, bei dem Sie erzählen, welche Eventtypen Sie gestalten (Hochzeiten, Firmenfeiern, Cocktails, Galas), die durchschnittliche Gästezahl, die Stadt und Ihre Arbeitsweise. Ab diesem Moment antwortet jeder Agent – von Catering AI+ bis zu den Kalkulationen – angepasst an Ihren Kontext: Servicearten, Größenordnung Ihrer Zentralküche und reale Abläufe. Das ist kein Formular: Es ist ein kurzes Gespräch, das die Suite für Ihren Alltag als Catering-Koch wirklich nützlich macht.",
    "appsTitle": "Die KI-Agenten, die Sie als Catering-Koch nutzen werden",
    "apps": [
      {
        "name": "Catering AI+",
        "category": "Geschäftskonzepte",
        "description": "Hauptagent: Hochzeiten, Firmenfeiern, Cocktails und Galas mit professionellem Wissen."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung professioneller Gerichte mit Rezept + CSV-Kalkulation, bereit für das Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Zutatenkombinationen und Pairings mit wissenschaftlicher Basis."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Eventdesserts mit professioneller Technik, ideal für Bankette und Galas."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Für avantgardistische Canapés mit Fermenten, Garums und innovativen Techniken."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools und Utilities",
        "description": "Portionsrechner, der Rezepte auf 50, 200 oder 500 Gäste skaliert."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Allergenerkennung pro Gericht, entscheidend für große Events."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Präzise Daten zu Abfällen und Erträgen für Produktion in großem Maßstab."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools und Utilities",
        "description": "Professioneller Gewichts- und Maßeinheiten-Umrechner für die industrielle Produktion."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für technische Zutaten aus dem Sosa-Katalog."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Food-Fotografie mit KI für Kundenangebote und Pressemitteilungen."
      }
    ],
    "metrics": [
      {
        "value": "×10",
        "label": "schnellerer Abschluss von Eventmenüs"
      },
      {
        "value": "+5 Pp.",
        "label": "Marge nach echter Kalkulation"
      },
      {
        "value": "−50 %",
        "label": "Zeit bei der Logistikplanung"
      },
      {
        "value": "11+",
        "label": "Agenten für Ihr Catering"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Eventmenü mit dem Kunden abschließen: halber Nachmittag mit Taschenrechner und Servietten",
        "APPCC außer Haus improvisiert, ohne echte Rückverfolgbarkeit beim Transport",
        "Produktion für 200 Gäste ohne präzise Skalierung, hohe Abfälle",
        "Kundenangebote mit Word-Vorlagen und Stockfotos",
        "Briefing an das Team auf losen Zetteln, die verloren gehen"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Menü mit validierter Marge in 30 Minuten abschließen mit Catering AI+ und Kit de Escandallos Pro",
        "APPCC angepasst an reisende Produkte mit Protokollen vom Handy und Rückverfolgbarkeit pro Event",
        "Produktion skaliert mit Calcula Pax, Abfälle kontrolliert mit Lebensmittelabfälle AI",
        "Kommerzielle Angebote mit GastroIMG Gen+ Fotos und professionellen technischen Datenblättern",
        "Zentralisiertes und reproduzierbares Briefing für Produktion, Transport, Aufbau und Service"
      ]
    },
    "galleryTitle": "Der Alltag eines Catering-Kochs in Bildern",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Menüdesign, Produktion in großem Maßstab, Logistik, Aufbau vor Ort, Service und Rückverfolgbarkeit.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-catering-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-production.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-loading.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-event.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-temp.jpg"
    ]
  },
  "propietario-catering": {
    "h1": "KI für Catering-Unternehmer",
    "heroSubtitle": "Kontrollieren Sie die Rentabilität pro Event, skalieren Sie die Produktion, verwalten Sie Aushilfsteams und lassen Sie Ihr Catering-Unternehmen mit einer Suite spezialisierter KI-Agenten für die Gastronomie wachsen.",
    "heroTagline": "Kontrolliertes Wachstum, echte Margen, Events ohne Chaos",
    "badge": "Für Catering-Unternehmer",
    "painsTitle": "Was ein Catering-Unternehmer unbedingt lösen muss",
    "pains": [
      "Margen bei hoher Variabilität zwischen Events verwalten: Eine Hochzeit, ein Corporate-Cocktail und ein Coffee Break haben sehr unterschiedliche Rentabilitäten",
      "Produktion skalieren, ohne Qualität und Kostenkontrolle zu verlieren, wenn Hochzeits- oder Eventsaison-Spitzen kommen",
      "Aushilfsteams und feste Belegschaft mit Dienstplänen, Verträgen pro Event und klaren Arbeitskosten koordinieren",
      "Finanzreporting an Investoren oder Partner mit konsolidierten Daten, nicht improvisierten Excels",
      "Corporate-Kunden mit professionellen Angeboten gewinnen, die Verträge mit höherem Auftragswert abschließen",
      "Entscheiden, welche Events angenommen und welche abgelehnt werden, basierend auf echten Margendaten, nicht auf Bauchgefühl"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Catering-Unternehmer hilft",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Spezialisierter Agent für gastronomische Events: Hochzeiten, Corporate, Cocktails und Galas mit professionellem Wissen."
      },
      {
        "icon": "FileText",
        "title": "Kit Plan Financiero",
        "description": "Cashflow, monatliche P&L, Kennzahlen-Dashboard und Rentabilität pro Event und pro Kunde. Professionelle, auf Catering zugeschnittene Vorlagen."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulationen pro Event",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet sie mit Ihren realen Preisen und der Zielmarge."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Dienstpläne für festes und Aushilfspersonal, Verträge pro Event, Stundenkontrolle und Arbeitskosten pro Service."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP und Zertifizierungen",
        "description": "Pack APPCC mit auf Catering zugeschnittenen Vorlagen: Rückverfolgbarkeit, Transport und Aufzeichnungen, bereit für Inspektionen und Corporate-Kunden."
      },
      {
        "icon": "Sparkles",
        "title": "BlogPost SEO Gen+ + MenuDish Local SEO",
        "description": "SEO-Suite, um Corporate-Kunden mit organischem Traffic und besserem Ranking zu gewinnen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Gastronomische Fotografie mit KI für Kundenangebote, Präsentationen und Webgalerie."
      },
      {
        "icon": "BarChart3",
        "title": "Operations-Dashboard",
        "description": "Konsolidierte Finanz-KPIs, Auslastungsquote, Rentabilität nach Geschäftsbereich (Hochzeiten, Corporate, Cocktails)."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Tiefgehende Markt-, Wettbewerbs- und Trendforschung für strategische Wachstumsentscheidungen."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Catering-Unternehmers mit AI Chef Pro",
    "workflow": [
      "08:30 · Kit Plan Financiero – Sie öffnen das Dashboard und stellen fest, dass ein Event am Wochenende eine Marge von 18 % hat, unter dem Zielwert (28 %).",
      "09:30 · Kit de Escandallos Pro – Sie analysieren die Kalkulation des Events und passen das Menü oder den Preis an, bevor Sie den Vertrag abschließen.",
      "11:00 · Catering AI+ – Sie schließen ein Angebot für ein Kundenunternehmen mit einer KI-generierten und mit dem Agenten validierten Präsentation ab.",
      "12:30 · GastroIMG Gen+ – Sie generieren die Fotos der Gerichte des vorgeschlagenen Menüs für die Präsentation.",
      "14:00 · Meeting mit Corporate-Kunden – Sie präsentieren ein in 1 Stunde erstelltes Angebot statt der üblichen 3 Tage.",
      "16:30 · Kit Plan Financiero – Sie validieren die Quartalsprognose und exportieren sie als PDF für das Meeting mit Partnern.",
      "18:00 · Kit Gestión de Personal – Sie überprüfen den Dienstplan für das Wochenende mit festem und Aushilfspersonal und unterschreiben Verträge pro Event.",
      "20:00 · BlogPost SEO Gen+ – Sie veröffentlichen einen Beitrag über das letzte große Corporate-Event, um organisch neue Kunden zu gewinnen."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Catering-Unternehmen",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-tareas-catering",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "AI Chef Pro hat mir echte finanzielle Kontrolle gegeben. Ich weiß genau, bei welchen Events ich Geld verdiene und bei welchen nicht, und das hat es mir ermöglicht, Kunden abzusagen, die nicht rentabel waren. Im ersten Quartal haben wir die Marge um 4 Prozentpunkte gesteigert, ohne die Preise anzufassen. Nur durch Anpassung der Menüs und das Ablehnen schlechter Events.",
    "testimonialAuthor": "Roberto Iglesias",
    "testimonialRole": "Inhaber, Corporate-Catering-Unternehmen (2M€ Jahresumsatz)",
    "faqTitle": "Häufig gestellte Fragen von Catering-Unternehmern",
    "faqs": [
      {
        "q": "Eignet es sich für ein Boutique-Catering mit weniger als 5 Mitarbeitern?",
        "a": "Ja. Es ist ideal für Boutique-Betriebe, weil es Betrieb, Finanzen, Marketing und Kundenangebote in einem einzigen Tool konsolidiert. Ein typischer Kunde startet mit 1 persönlichen Plan und wächst zum Unternehmen."
      },
      {
        "q": "Und für große Unternehmen mit 50+ Aushilfskräften?",
        "a": "Auch. Das Kit Gestión de Personal skaliert auf große Teams mit Dienstplänen, Verträgen pro Event und konsolidierten Arbeitskosten. Es gibt Kunden mit 100+ Services pro Monat."
      },
      {
        "q": "Integriert es sich mit meiner Buchhaltungssoftware oder ERP?",
        "a": "Es exportiert Excel, PDF und CSV, die mit den meisten ERPs und Steuerberatern kompatibel sind. Ihr Finanzteam erhält dokumentationsfertige Unterlagen zur Integration."
      },
      {
        "q": "Gibt es einen Unternehmensplan für großes Catering?",
        "a": "Ja. Ab einem bestimmten Umsatz gibt es Unternehmenspläne mit personalisiertem Onboarding, konsolidierten Dashboards, Schulung des Kernteams und Prioritäts-Support."
      },
      {
        "q": "Wie hilft es mir, Corporate-Kunden zu gewinnen?",
        "a": "BlogPost SEO Gen+ und MenuDish Local SEO ziehen organischen Traffic auf Ihre Website; Catering AI+ hilft beim Verfassen professioneller Angebote; GastroIMG Gen+ generiert Fotos für Präsentationen; Keyword Discovery AI+ findet die tatsächlichen Suchanfragen von Unternehmen in Ihrer Region."
      },
      {
        "q": "Ist es sicher, den Finanzplan einer KI anzuvertrauen?",
        "a": "Ja. Das Kit Plan Financiero ist eine professionelle Excel-Vorlage mit vorbefüllten Formeln, keine KI. Sie geben die realen Daten ein und das Tool berechnet. Die KI-Agenten werden nur zur Unterstützung bei Entscheidungen, Angebotserstellung und Analysen eingesetzt, nicht für kritische Finanzberechnungen."
      }
    ],
    "ctaTitle": "Lassen Sie Ihr Catering mit echter Marge wachsen, nicht mit Bauchgefühl.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für die Nutzung aller Agenten.",
    "seo": {
      "title": "KI für Catering-Unternehmer: Rentabilität und Finanzplan | AI Chef Pro",
      "description": "KI-Suite für Catering-Unternehmen: Rentabilität pro Event, skalierte Produktion, Aushilfsteams, Finanzplan und Gewinnung von Corporate-Kunden. Starten Sie noch heute.",
      "keywords": "KI Catering-Unternehmen, Catering-Unternehmer KI, Catering-Software, Catering-Unternehmensführung, Finanzplan Catering, Rentabilität Catering, Gewinnung Corporate-Kunden Catering, Catering-Unternehmen skalieren, Catering-Unternehmer Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/propietario-catering.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Unternehmen zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten «Wer sind Sie?», einem 2-minütigen Conversational Onboarding, bei dem Sie erzählen, welche Art von Catering Sie betreiben (Hochzeiten, Corporate, Cocktails, Galas), durchschnittliche Eventgröße, Stadt und Jahresvolumen. Ab diesem Moment antwortet jeder Agent – von Catering AI+ bis zum Plan Financiero – angepasst an Ihren Kontext: Servicetypen, reale Größenordnung und Zielmarkt. Es ist kein Formular: Es ist ein kurzes Gespräch, das die Suite für Ihr Unternehmen wirklich nützlich macht.",
    "appsTitle": "Die KI-Agenten, die Sie als Catering-Unternehmer nutzen werden",
    "apps": [
      {
        "name": "Catering AI+",
        "category": "Geschäftskonzepte",
        "description": "Hauptagent: Hochzeiten, Corporate, Cocktails und Galas mit professionellem Wissen."
      },
      {
        "name": "Profi Restaurantmanager",
        "category": "Gastro Profile Pro",
        "description": "Operativer und finanzieller Assistent zur Unterstützung bei Entscheidungen und Reporting an Partner."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Event-Menüs mit Rezept + CSV-Kalkulation, bereit für das Kit de Escandallos Pro."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Event- und Bankett-Desserts mit professioneller Technik."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools und Utilities",
        "description": "Portionsrechner, der Rezepte auf 50, 200 oder 500 Gäste skaliert."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Allergenidentifizierung pro Rezept, entscheidend für große Events."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und Social Media",
        "description": "Blogbeiträge, um organischen Traffic auf Ihre Catering-Website zu ziehen."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und Social Media",
        "description": "SEO-Beschreibungen zur Verbesserung des Web-Rankings Ihres Caterings."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Inhalte und Social Media",
        "description": "Keyword-Recherche, um Unternehmen zu gewinnen, die in Ihrer Region Catering suchen."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Gastronomische Fotografie für Kundenangebote und Verkaufspräsentationen."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Markt-, Wettbewerbs- und Trendforschung für die Eventbranche."
      },
      {
        "name": "Mental Coach",
        "category": "Tools und Utilities",
        "description": "Coaching für Stressbewältigung, schwierige Entscheidungen und Gespräche mit Partnern oder Team."
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "Marge im ersten Quartal"
      },
      {
        "value": "×3",
        "label": "Geschwindigkeit beim Abschluss von Angeboten"
      },
      {
        "value": "−40 %",
        "label": "Zeit für Finanzreporting"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihr Unternehmen"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Nicht zu wissen, welches der 50 Events im Monat wirklich rentabel ist",
        "Angebote an Corporate-Kunden in 3 Tagen mit Word-Vorlagen abschließen",
        "Manuelle Excel-Dienstpläne für Aushilfspersonal ohne Kostenkontrolle",
        "Uneinheitliches HACCP zwischen Events, Problem mit anspruchsvollen Corporate-Kunden",
        "Improvisiertes oder teuer ausgelagertes Marketing ohne organische Lead-Gewinnung"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Klare Rentabilität pro Event und pro Kunde, Entscheidungen über Annahme/Ablehnung auf Basis von Daten",
        "Angebote in 1 Stunde abschließen mit Catering AI+ + GastroIMG Gen+ + professioneller Präsentation",
        "Dienstpläne mit Kit Gestión de Personal: konsolidierte Stunden- und Kostenkontrolle",
        "Einheitliches und professionelles HACCP, bereit für jede Inspektion oder jeden Corporate-Kunden",
        "SEO-Suite, die organische Leads ohne Agenturkosten gewinnt"
      ]
    },
    "galleryTitle": "Der Alltag eines Catering-Unternehmers in Bildern",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren werden: Preisgestaltung, Kundenangebote, Großveranstaltungen, Teams, Logistiklager und Finanzreporting.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-event.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-pricing.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-storage.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-presentation.jpg"
    ]
  },
  "bartender-coctelero": {
    "h1": "KI für Barkeeper und Mixologen",
    "heroSubtitle": "Entwerfen Sie Cocktailkarten mit professionellem Kalkulationsblatt, Kalkulation pro Drink mit echten Kosten und Technik, und kreieren Sie Autoren-Drinks mit Storytelling und Pairing – mit einer Suite spezialisierter gastronomischer KI-Agenten für die Cocktailkunst.",
    "heroTagline": "Cocktailkunst mit echtem Gewinn und Autorentechnik",
    "badge": "Für Barkeeper, Mixologen und Cocktailkünstler",
    "painsTitle": "Was ein Barkeeper unbedingt lösen muss",
    "pains": [
      "Komplexe Cocktails mit vielen Zutaten (Spirituosen, Cordials, Infusionen, Garnishes) kalkulieren, ohne Stunden mit dem Taschenrechner zu verlieren",
      "Die Karte jede Saison mit neuen Drinks erneuern und dabei Gewinn und einen kohärenten Food Cost mit dem Rest der Bar beibehalten",
      "Rezepte an der Bar standardisieren, damit jeder Kellner den Drink jedes Mal mit derselben Balance repliziert",
      "Lebensmittelabfälle an der Bar kontrollieren: Glasbruch, Überpouring, Verdunstung, verschwendete Garnishes",
      "Storytelling: Jeder Cocktail braucht einen Namen, eine Geschichte und ein Pairing, das den hohen Preis rechtfertigt",
      "Sich in einem umkämpften Gebiet mit Autoren-Cocktails, visuellem Branding und aktiven sozialen Medien differenzieren"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Barkeeper hilft",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Agent spezialisiert auf professionelle Cocktailkunst, Weinbars, Cocktailbars und Spirituosen mit fortgeschrittener Technik."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Unerwartete Kombinationen für Autoren-Cocktails mit wissenschaftlicher Basis und Pairings mit Küche."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Drink",
        "description": "Bar & Lounge AI+ liefert Rezept + CSV-Kalkulationsblatt mit Technik; Kit de Escandallos Pro verwaltet es mit echten Kosten pro Drink, Food-Cost-Prozentsatz und empfohlenem Preis."
      },
      {
        "icon": "BookOpen",
        "title": "Technische Cocktail-Datenblätter",
        "description": "Rezept, Technik, Garnish, Glas, Pairing und Storytelling in einem einzigen Dokument, bereit für das Team."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Vorlagen: Bar-Mise, Vorbereitung von Cordials und Infusionen, Abläufe pro Schicht, Kassenabschluss, Bestandskontrolle."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Bar",
        "description": "Rückverfolgbarkeit von Eis, frischen Garnishes, hausgemachten Infusionen und kritischen Temperaturen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planung der saisonalen Karte: Sommer-Cocktails, heiße Winterdrinks, Themenkarten für Valentinstag, Weihnachten und Events."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "KI-Referenzfotografie für Cocktails + Instagram-Inhalte mit professionellem redaktionellen Kalender."
      },
      {
        "icon": "BarChart3",
        "title": "Bar-KPIs",
        "description": "Durchschnittlicher Ticketwert, Drink-Rotation, Gewinn pro Kategorie (Klassiker, Signature, Weine, Biere)."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Barkeepers mit AI Chef Pro",
    "workflow": [
      "11:00 · Eröffnung – Checkliste Kit de Tareas Bar: Mise für frische Garnishes, Vorbereitung hausgemachter Cordials, Eis auffüllen, Bestandskontrolle.",
      "12:00 · Bar & Lounge AI+ – Sie entwickeln einen neuen Signature-Drink für die Sommerkarte (Gin mit Erdbeer-Basilikum-Shrub). Kreativküche liefert Rezept + CSV-Kalkulationsblatt.",
      "13:00 · Food Pairing AI – Sie validieren das Pairing mit einem Gericht aus der Küche und verfeinern die Technik.",
      "14:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren echten Preisen für Premium-Spirituosen und Zutaten, validieren Gewinn pro Drink und Food-Cost-Prozentsatz.",
      "17:00 · Service – das Team repliziert den Drink mit dem technischen Datenblatt (Rezept, Technik, Garnish, Glas, Storytelling).",
      "19:00 · Gastro Calendar – Sie aktualisieren den redaktionellen Instagram-Kalender mit dem Launch des neuen Signature-Drinks.",
      "20:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren das Referenzbild des Drinks und die Posts für den Launch.",
      "02:00 · Schließung – gründliche Reinigung, APPCC unterschrieben, Kontrolle der Lebensmittelabfälle und Endbestand."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für die Cocktailbar",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "AI Chef Pro hat meine Art, Cocktailkarten zu erstellen, völlig verändert. Früher war es eine Woche mit Servietten und Taschenrechner; jetzt ist es ein Tag mit professionellem Kalkulationsblatt, technischem Datenblatt mit Storytelling und validiertem Pairing, bereit für mein Team. Wir haben den Gewinn um 5 Punkte gesteigert und das Instagram-Engagement mit GastroIMG verdreifacht.",
    "testimonialAuthor": "Hugo Vázquez",
    "testimonialRole": "Barkeeper, Cocktailbar mit Autorenkonzept",
    "faqTitle": "Häufige Fragen von Barkeepern",
    "faqs": [
      {
        "q": "Funktioniert es für klassische, Autoren- oder Casual-Cocktailbars?",
        "a": "Für alle drei. Bar & Lounge AI+ versteht von IBA-Klassikern bis zur Avantgarde: Shrubs, Infusionen, Fermentiertes, Schäume, kontrolliertes Räuchern, fortgeschrittene Barttechnik."
      },
      {
        "q": "Deckt es auch Weine und Biere ab, nicht nur Cocktails?",
        "a": "Ja. Der Agent deckt das gesamte Barspektrum ab: Cocktails, Weine, Biere, Spirituosen, alkoholfreie Getränke und Pairings."
      },
      {
        "q": "Ermöglicht es, Drinkkarten mit Storytelling und Technik zu erstellen?",
        "a": "Ja. Die Datenblätter enthalten Rezept, Technik, Garnish, Glas, Geschichte und Pairing, bereit für den Service. Ideal, um den durchschnittlichen Ticketwert zu steigern und den Preis zu rechtfertigen."
      },
      {
        "q": "Generiert es visuelle Inhalte für Instagram und die Karte?",
        "a": "Ja. GastroIMG Gen+ generiert professionelle Referenzbilder jedes Drinks für Instagram, Web und Karte; InstaFlow AI Pro plant Inhalte mit redaktionellem Kalender. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie selbst mit Ihrem real angerichteten Cocktail."
      },
      {
        "q": "Wie hilft es mir bei der Saisonalität der Karte?",
        "a": "Gastro Calendar plant die saisonalen Karten (Sommer, Herbst, Weihnachten, Valentinstag) im Voraus. Das Kit Plan Financiero projiziert den realistischen saisonalen Cashflow, damit Sie mit Bestand und Kasse an jedem Peak ankommen."
      }
    ],
    "ctaTitle": "Ihre Cocktailbar mit echtem Gewinn und Autorentechnik.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Barkeeper und Mixologen: Karten, Kalkulationen und Storytelling | AI Chef Pro",
      "description": "KI-Suite für professionelle Barkeeper: Bar & Lounge AI+, Food Pairing AI, Kalkulation pro Drink, technische Datenblätter mit Storytelling und visuellem Branding. Starten Sie noch heute.",
      "keywords": "KI Barkeeper, KI Mixologe, Cocktailbar-Software, Cocktail-Kalkulation, Food Pairing KI, Cocktailkarten KI, Mixologe KI, Signature Cocktail",
      "ogImage": "https://aichef.pro/og/use-cases/bartender-coctelero.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Bar zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen conversational Onboarding, bei dem Sie erzählen, welche Art von Bar Sie betreiben (Cocktailbar mit Autorenkonzept, Weinbar, Hotelbar, Lounge, Restaurant mit Cocktailkarte), Teamgröße, Stadt und Kartenstil. Jeder Agent – von Bar & Lounge AI+ bis Gastro Calendar – antwortet angepasst an Ihr Produkt, Ihren Markt und Ihre reale Betriebsweise.",
    "appsTitle": "Die KI-Agenten, die Sie an Ihrer Bar nutzen werden",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Kulinarische Kreativität",
        "description": "Agent spezialisiert auf professionelle Cocktailkunst, Weine, Biere und Spirituosen mit fortgeschrittener Technik."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Unerwartete Kombinationen mit wissenschaftlicher Basis und Pairings Cocktail + Gericht."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Drinks mit Rezept + CSV-Kalkulationsblatt."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für fortgeschrittene Texturen, Geliermittel und Autoren-Barttechniken."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Assistent des tSpoonLab-Katalogs für fortgeschrittene Mixologie-Anwendungen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Daten zu Lebensmittelabfällen an der Bar: Bruch, Überpouring, Verdunstung, verschwendete Garnishes."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Drink: Sulfite, Milchprodukte, Nüsse, Gluten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Referenzfotografie für Web, soziale Medien und Cocktailkarten."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit professionellem redaktionellen Kalender für Autoren-Cocktailbars."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die bei Google und Maps nach „Cocktailbar in der Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Planung der saisonalen Karte: Sommer, Winter, Valentinstag, Weihnachten."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und soziale Medien",
        "description": "Pinterest generiert stabilen organischen Traffic für Cocktails mit Storytelling."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Gewinn nach Kartenkalkulation"
      },
      {
        "value": "×3",
        "label": "Instagram-Engagement mit GastroIMG"
      },
      {
        "value": "−1 Tag",
        "label": "Abschluss der Saisonkarte (von 7 auf 1)"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Karten in einer Woche mit Servietten und Taschenrechner erstellt",
        "Kalkulationen ohne echten Food Cost pro Drink, Signature-Drinks in Verlust ohne es zu wissen",
        "Keine technischen Datenblätter: Jeder Kellner repliziert, so gut er kann",
        "Lebensmittelabfälle an der Bar ohne echte Rückverfolgbarkeit",
        "Improvisiertes Instagram mit Handyfotos ohne Kontinuität"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Saisonkarte in einem Tag abgeschlossen mit professionellem Kalkulationsblatt und Storytelling",
        "Echter Food Cost pro Drink, Signature-Drinks mit validiertem Gewinn",
        "Technische Datenblätter mit Rezept, Technik, Garnish, Glas, Pairing und Storytelling",
        "Lebensmittelabfälle kontrolliert mit Lebensmittelabfälle AI und spezifischen Bar-Vorlagen",
        "Instagram mit professionellem redaktionellen Kalender und GastroIMG Gen+"
      ]
    },
    "galleryTitle": "So funktioniert eine Autoren-Bar",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Bar, Cocktails, Technik, Mise, Zutaten und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-bartender-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-cocktails.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-technique.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-ingredients.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-team.jpg"
    ]
  },
  "pizzero": {
    "h1": "KI für Pizzabäcker und Pizzaioli",
    "heroSubtitle": "Optimieren Sie Teige und Fermentationen, kalkulieren Sie pro Pizza mit echten Kosten, kontrollieren Sie Ofentechnik und Betrieb mit einer Suite gastronomischer KI-Agenten, spezialisiert auf professionelle italienische Küche.",
    "heroTagline": "Pizza mit authentischer Technik und echtem Gewinn",
    "badge": "Für Pizzabäcker, Pizzaioli und Pizzeria-Inhaber",
    "painsTitle": "Was ein Pizzabäcker unbedingt lösen muss",
    "pains": [
      "Teig, Hydration und Fermentation in jeder Schicht mit technischem Know-how standardisieren (neapolitanisch, römisch, in pala, amerikanisch)",
      "Pizzen mit vielen Topping-Varianten kalkulieren und den Food Cost über alle Kartenoptionen konsistent halten",
      "Lebensmittelabfälle bei Teig (Überfermentation, fehlgeschlagenes Formen), Mozzarella (Feuchtigkeit, Verdunstung) und Saucen",
      "Konstante Qualität im Ofen (Holz, elektrisch, Gas) bei hohen Nachfragespitzen am Wochenende aufrechterhalten",
      "Sich in umkämpften Gebieten mit Signature-Pizzen, Premium-Mehl und visuellem Storytelling differenzieren",
      "Delivery-Bestellungen mit Gewinn anziehen, während der Laden mit Service im Saal betrieben wird"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Pizzabäcker hilft",
    "features": [
      {
        "icon": "Pizza",
        "title": "Italienische Küche",
        "description": "Spezialisierter Agent für professionelle italienische Küche: Teige (neapolitanisch, römisch, in pala, amerikanisch), Saucen, Toppings und Ofentechnik."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Für Sauerteige, Vorteige (Biga, Poolish), hohe Hydrationen und lange kontrollierte Kaltfermentationen."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Pizza",
        "description": "Italienische Küche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet sie mit echten Kosten pro Pizza, Food-Cost-Prozentsatz und empfohlenem Preis."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pizzería",
        "description": "Vorlagen: Teig-Mise-en-Place, Saucenvorbereitung, Topping-Mise-en-Place, Service im Saal, Delivery, Abschluss und Ofenreinigung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC",
        "description": "Rückverfolgbarkeit von Mehlen, Sauerteig, Mozzarella, Saucen und kritischen Temperaturen in Ofen und Kühlung."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planung saisonaler Karten: Sommerpizzen mit frischen Tomaten, Herbst mit Pilzen und Trüffel, Spezialitäten für Valentinstag und Events."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "KI-Referenz-Lebensmittelfotografie + Instagram mit Redaktionskalender: Eine Pizzeria lebt von visueller Wirkung."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Lokale Kunden anziehen, die nach „Pizzeria in der Nähe“ bei Google und Maps suchen, mit optimierten Beschreibungen."
      },
      {
        "icon": "Sparkles",
        "title": "Lebensmittelabfälle AI",
        "description": "Präzise Daten zu Lebensmittelabfällen pro Prozess (Teig, Mozzarella, Abschnitte, Delivery), integriert in die Kalkulation."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Pizzabäckers mit AI Chef Pro",
    "workflow": [
      "08:00 · Eröffnung – Checkliste Kit de Tareas Pizzería: Auffrischen von Sauerteig oder Biga, Vorbereitung von San-Marzano-Tomatensauce, kontrollierte Fermentation der Teiglinge.",
      "10:00 · Italienische Küche – Sie entwickeln eine neue saisonale Pizza (gerösteter Kürbis, Gorgonzola, Honig und Walnuss) mit technischem Know-how. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "11:00 · Fermentus mit AI+ – Sie passen die Hydration auf 70 % und kalte Fermentationszeiten von 48 Stunden für den neapolitanischen Teig an.",
      "12:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren echten Preisen für Caputo-Mehl, Mozzarella di bufala und Toppings hoch, validieren Gewinn und Food-Cost-Prozentsatz.",
      "13:00 · Mittagsservice – Das Team arbeitet mit Mise-en-Place- und Prep-Vorlagen, koordinierte Stoßzeiten.",
      "17:00 · Pause zwischen den Services – Gastro Calendar plant die Herbstkarte und Events.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie erstellen das Referenzbild der neuen Pizza und die Instagram-Posts.",
      "23:00 · Abschluss – Tiefenreinigung des Ofens, APPCC signiert, Teigvorbereitung für morgen."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Pizzerien",
    "productIds": [
      "kit-tareas-pizzeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Wir haben Pizza für Pizza kalkuliert und entdeckt, dass 4 trotz guter Verkaufszahlen Verlust machten. Wir haben sie mit Italienische Küche neu gestaltet, Toppings vereinfacht ohne Identität zu verlieren, und den Gewinn um 4 Punkte gesteigert, ohne die Preise zu ändern. Fermentus hat unseren Teig verändert: 70 % Hydration, 48 Stunden Fermentation, perfekte Porung.",
    "testimonialAuthor": "Giovanni Russo",
    "testimonialRole": "Pizzaiolo und Inhaber, neapolitanische Pizzeria",
    "faqTitle": "Häufige Fragen von Pizzabäckern",
    "faqs": [
      {
        "q": "Funktioniert es für neapolitanische, römische, in pala oder amerikanische Pizza?",
        "a": "Für alle vier. Italienische Küche und Fermentus decken das gesamte Spektrum der Teige (Porung, Hydration, Fermentationen), Backtechniken (Holz, elektrisch, Gas) und italienische sowie amerikanische Stile ab."
      },
      {
        "q": "Deckt es Sauerteig- und Vorteig-Technik ab?",
        "a": "Ja. Fermentus mit AI+ versteht Biga, Poolish, flüssigen und festen Sauerteig, hohe Hydrationen und kontrollierte Kaltfermentationen. Es denkt wie ein professioneller Pizzaiolo, nicht wie YouTube-Rezepte."
      },
      {
        "q": "Deckt es auch Delivery neben dem Laden ab?",
        "a": "Ja. Das Kit de Tareas Pizzería enthält spezifische Vorlagen für Delivery: Temperaturen, Verpackung, die die Garung erhält, Transportverluste und Abholprozeduren."
      },
      {
        "q": "Generiert es visuelle Inhalte für Instagram, Glovo und Uber Eats?",
        "a": "Ja. GastroIMG Gen+ generiert professionelle Referenzbilder für Instagram, Lieferplattformen und Speisekarten; besseres Foto = mehr Klicks und besseres Ranking. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie selbst mit Ihrer frisch gebackenen Pizza."
      },
      {
        "q": "Wie hilft es mir bei Saisonalität und Events?",
        "a": "Gastro Calendar plant saisonale Karten (Sommer, Herbst mit Pilzen und Trüffel, Spezialitäten für Valentinstag, Ostern, Weihnachten). Das Kit Plan Financiero projiziert den realistischen saisonalen Cashflow, damit Sie mit Lager und Kasse an jedem Höhepunkt ankommen."
      }
    ],
    "ctaTitle": "Ihre Pizzeria mit echtem Gewinn und authentischer Technik.",
    "ctaSubtitle": "Beginnen Sie mit dem 2-minütigen Onboarding. Mitgliedsplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Pizzabäcker und Pizzaioli: Teige, Kalkulation und italienische Technik | AI Chef Pro",
      "description": "KI-Suite für professionelle Pizzabäcker: Italienische Küche, Fermentus für Teige und Biga, Kalkulation pro Pizza, Vorlagen und authentische Technik. Starten Sie noch heute.",
      "keywords": "KI Pizzabäcker, KI Pizzaiolo, Pizzeria Software, Pizza-Kalkulation, Sauerteig Pizza, Biga Poolish Pizza, neapolitanische Technik, römische Pizza KI",
      "ogImage": "https://aichef.pro/og/use-cases/pizzero.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Pizzeria personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen konversationellen Onboarding, bei dem Sie erzählen, welche Art von Pizzeria Sie betreiben (authentische neapolitanische, römische al taglio, amerikanische, gemischt mit italienischer Küche, Dark Kitchen für Delivery), Teamgröße, Stadt und Ofentyp. Jeder Agent – von Italienische Küche bis Gastro Calendar – antwortet angepasst an Ihr Produkt, Ihren Markt und Ihre reale Betriebsweise.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrer Pizzeria nutzen werden",
    "apps": [
      {
        "name": "Italienische Küche",
        "category": "Kulinarische Kreativität",
        "description": "Spezialisierter Agent für professionelle italienische Küche: Teige, Saucen, Toppings, Ofentechnik."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Sauerteige, Biga, Poolish, hohe Hydrationen, lange kontrollierte Fermentationen."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Pizzen mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für technische Mehle, Verbesserer und fortgeschrittene Kombinationen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Lebensmittelabfälle bei Teig, Mozzarella, Sauce, Abschnitten und Delivery, integriert in die Kalkulation."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Allergenerkennung pro Pizza: Gluten, Milchprodukte, Nüsse, Ei."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Referenz-Lebensmittelfotografie für Glovo, Uber Eats, Web und soziale Medien."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und Social Media",
        "description": "Instagram mit professionellem Redaktionskalender für die Signature-Pizzeria."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und Social Media",
        "description": "Lokale Kunden anziehen, die nach „Pizzeria in der Nähe“ bei Google und Maps suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und Social Media",
        "description": "Planung saisonaler Karten: Sommer, Herbst, Valentinstag, Weihnachten."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und Social Media",
        "description": "Pinterest generiert stabilen organischen Traffic für Pizzen mit Storytelling."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und Social Media",
        "description": "SEO-Artikel über italienische Technik, Teige und Pairings, um Traffic zu gewinnen."
      }
    ],
    "metrics": [
      {
        "value": "+4 Pp.",
        "label": "Gewinn nach Pizza-Kalkulation"
      },
      {
        "value": "×3",
        "label": "Instagram-Engagement mit GastroIMG"
      },
      {
        "value": "−25 %",
        "label": "Lebensmittelabfälle bei Teig und Mozzarella"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Pizzeria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Teig improvisiert pro Schicht: inkonsistente Porung und ungleichmäßige Knusprigkeit",
        "Kalkulation ohne echten Food Cost, Pizzen mit Verlust ohne es zu wissen",
        "Lebensmittelabfälle bei Teig, Mozzarella und Sauce ohne Rückverfolgbarkeit",
        "Improvisiertes Instagram und Lieferplattformen mit Handyfotos",
        "APPCC auf Papier, verstreut in der Pizzeria"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Teig mit technischem Know-how: konsistente Hydration, Fermentation und Backverhalten",
        "Professionelle Kalkulation pro Pizza mit validiertem Gewinn und Food-Cost-Prozentsatz",
        "Kontrollierte Lebensmittelabfälle mit Lebensmittelabfälle AI und spezifischen Vorlagen",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO ziehen lokale Kunden und Delivery an",
        "APPCC vom Handy mit Registern, bereit für Inspektionen"
      ]
    },
    "galleryTitle": "So funktioniert eine authentische Pizzeria",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Teig, Ofen, Technik, Zutaten, Pizzen und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-pizzero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-masa.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-horno.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-pizza.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-ingredients.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-team.jpg"
    ]
  },
  "panadero": {
    "h1": "KI für den handwerklichen Bäcker",
    "heroSubtitle": "Optimieren Sie Sauerteig und Vorteige, kalkulieren Sie jedes Stück mit Backstuben-Stundensatz, steuern Sie lange Fermentationen und den Betrieb mit einer Suite gastronomischer KI-Agenten, die auf handwerkliche Bäckerei spezialisiert sind.",
    "heroTagline": "Handwerkliche Bäckerei mit Technik und echter Marge",
    "badge": "Für handwerkliche Bäcker und Backstuben",
    "painsTitle": "Was ein handwerklicher Bäcker unbedingt lösen muss",
    "pains": [
      "Sauerteig, Vorteige (Biga, Poolish), Hydratationen und lange Fermentationsprozesse in jeder Schicht standardisieren",
      "Stücke mit echten Kosten kalkulieren, einschließlich Backstuben-Stunden (Auffrischen, Kneten, Formen, Backen kosten Zeit)",
      "Ausschuss bei Teigen, Vorteigen, Formabschnitten und fehlgeschlagenem Backen",
      "Produktion an die tägliche Nachfrage angepasst, ohne Überproduktion oder leere Regale vor Ladenschluss",
      "Sich in einem umkämpften Gebiet mit Premium-Mehlen, Urgetreide und handwerklichem Branding differenzieren",
      "Aufträge der lokalen Gastronomie (Restaurants, Cafés) mit Marge gewinnen, während der Direktverkauf gemanagt wird"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Bäcker hilft",
    "features": [
      {
        "icon": "Wheat",
        "title": "Kreative Boulangerie",
        "description": "Spezialisierter Agent für professionelle handwerkliche Bäckerei: Sauerteige, hohe Hydratationen, Formtechnik und Backen im Etagenofen."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Für flüssige und feste Sauerteige, Vorteige (Biga, Poolish), lange kontrollierte Kaltfermentationen und fortgeschrittene Technik."
      },
      {
        "icon": "Cake",
        "title": "Kreative Patisserie",
        "description": "Für Backstuben, die Bäckerei mit Gebäck und Konditorei kombinieren: Brioche, Croissants, Ensaimadas und handwerkliches Gebäck."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Stück mit Backstuben-Stundensatz",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet sie mit integriertem Backstuben-Stundensatz in der echten Marge pro Brotlaib, Baguette oder Brioche."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Obrador",
        "description": "Vorlagen: Sauerteig auffrischen, Vorteige, Kneten, Fermentationen, Formen, Backen, Vitrine und Lagerung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Bäckerei",
        "description": "Rückverfolgbarkeit von Mehlen, Sauerteig, Vorteigen, Lagerung und kritischen Temperaturen im Gärschrank."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Saisonale Planung mit wichtigen Terminen: Ostern (Monas, Hornazos), Weihnachten (Roscón, Panettone), San Juan, lokale Veranstaltungen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "KI-Referenz-Gastronomiefotografie + Pinterest, wo die handwerkliche Bäckerei stabilen organischen Traffic gewinnt."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Lokale Kunden gewinnen, die bei Google und Maps nach „handwerkliche Bäckerei in der Nähe“ suchen."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Bäckers mit AI Chef Pro",
    "workflow": [
      "04:00 · Eröffnung – Checkliste Kit de Tareas Obrador: Sauerteig auffrischen, Kontrolle der Nachtfermentationen, Einschalten des Etagenofens.",
      "05:30 · Formen und Backen – Formen von Brotlaiben, Baguettes und Brioche mit spezifischen Vorlagen, Kontrolle des Abschnitt-Ausschusses.",
      "08:00 · Vitrine auffüllen – erste Backcharge bereit für den Direktverkauf und Bestellungen an die lokale Gastronomie.",
      "10:00 · Kreative Boulangerie – Sie entwickeln ein neues Brot aus Urgetreide mit flüssigem Sauerteig. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "11:00 · Fermentus mit AI+ – Sie stellen die Hydratation auf 80 % und die Kaltfermentation auf 24 Stunden für das neue Brot ein.",
      "12:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren tatsächlichen Bio-Mehl-Preisen und dem Backstuben-Stundensatz hoch und validieren die Marge.",
      "15:00 · GastroIMG Gen+ + Pinterest Pins Gen – Sie generieren das Referenzbild des neuen Brotes und die Pins, um organischen Traffic zu gewinnen.",
      "20:00 · Abschluss – Reinigung, APPCC unterschrieben, Vorbereitung der Teige für die Nachtfermentation."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für die Bäckerei",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Wir sind von losen Zetteln auf ein System umgestiegen. Wir wissen jetzt genau, welches Stück sich rechnet und welches nicht – inklusive Backstuben-Stundensatz. Der Ausschuss ist in 3 Monaten um 30 % gesunken, und wir haben festgestellt, dass zwei unserer Klassiker ohne Stundensatz nicht rentabel waren – wir haben sie neu gestaltet, den Prozess vereinfacht, ohne Qualität zu verlieren, und die Marge um 5 Punkte gesteigert.",
    "testimonialAuthor": "Ana Iglesias",
    "testimonialRole": "Handwerkliche Bäckerin, eigene Backstube",
    "faqTitle": "Häufige Fragen von Bäckern",
    "faqs": [
      {
        "q": "Deckt es professionelle Sauerteig-Technik ab?",
        "a": "Ja. Kreative Boulangerie und Fermentus denken wie ein professioneller Bäcker: Auffrischen mit Inokulum-Prozentsatz, Hydratationen je nach Brottyp, kontrollierte Kaltfermentationen über 24–48 Stunden, Balance der Kulturen. Keine YouTube-Rezepte."
      },
      {
        "q": "Eignet es sich für kleine handwerkliche Backstuben oder industrielle Produktion?",
        "a": "Für beides. Die Vorlagen skalieren von der Familien-Backstube mit 2 Personen bis zur industriellen Produktion. Die Methodik ist dieselbe: Rezept → CSV-Kalkulation mit Backstuben-Stundensatz → echte Marge."
      },
      {
        "q": "Deckt es neben Bäckerei auch Gebäck und Konditorei ab?",
        "a": "Ja. Kreative Patisserie ergänzt das Sortiment, wenn Sie Brioche, Croissants, Ensaimadas, Ostergebäck oder Feingebäck herstellen. Fermentus mit AI+ deckt den fermentierten Teil mit professioneller Technik ab."
      },
      {
        "q": "Erzeugt es visuelle Inhalte für Vitrine, Instagram und Pinterest?",
        "a": "Ja. GastroIMG Gen+ erzeugt professionelle Referenzbilder des Brotes für Vitrine, Web und soziale Medien; Pinterest Pins Gen gewinnt stabilen organischen Traffic, den die handwerkliche Bäckerei stark nutzt. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie selbst mit Ihrem frisch gebackenen Brotlaib."
      },
      {
        "q": "Wie hilft es mir bei Saisonalität und Veranstaltungen?",
        "a": "Gastro Calendar plant die wichtigsten Saisons (Ostern mit Monas und Hornazos, Weihnachten mit Roscón und Panettone, San Juan, lokale Veranstaltungen) im Voraus. Das Kit Plan Financiero projiziert den realistischen saisonalen Cashflow."
      }
    ],
    "ctaTitle": "Ihre handwerkliche Bäckerei mit klarer Marge und professioneller Technik.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für den handwerklichen Bäcker: Sauerteig, Kalkulationen und professionelle Technik | AI Chef Pro",
      "description": "KI-Suite für handwerkliche Bäcker: Kreative Boulangerie, Fermentus mit AI+ für Sauerteig, Stückkalkulation mit Backstuben-Stundensatz. Starten Sie noch heute.",
      "keywords": "KI Bäcker, handwerkliche Bäckerei KI, Sauerteig KI, Bäckerei Software, Bäckerei Kalkulation, Fermentus, Biga Poolish, professioneller Bäcker",
      "ogImage": "https://aichef.pro/og/use-cases/panadero.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Backstube zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational-Onboarding, bei dem Sie angeben, welche Art von Bäckerei Sie betreiben (handwerklich mit Sauerteig, traditionelle Bäckerei, Backstube mit Gebäck, Bäckerei mit Café, Bio-Bäckerei), Teamgröße, Stadt und Spezialität. Jeder Agent – von Kreative Boulangerie bis Gastro Calendar – antwortet angepasst an Ihr Produkt, Ihren Markt und Ihren tatsächlichen Betrieb.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrer Bäckerei nutzen werden",
    "apps": [
      {
        "name": "Kreative Boulangerie",
        "category": "Kulinarische Kreativität",
        "description": "Spezialisierter Agent für professionelle handwerkliche Bäckerei, Sauerteige, Hydratationen und Technik."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Sauerteige, Biga, Poolish, hohe Hydratationen und lange kontrollierte Fermentationen."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Brioche, Croissants, Ensaimadas und ergänzendes handwerkliches Gebäck."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Broten mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog: technische Mehle, Verbesserungsmittel, Saaten und Urgetreide."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Ausschuss bei Teig, Vorteigen, Formabschnitten und Backen."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Allergen-Identifizierung pro Stück: Gluten, Milchprodukte, Nüsse, Ei."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Referenz-Gastronomiefotografie für Vitrine, Web und soziale Medien."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und soziale Medien",
        "description": "Pinterest gewinnt stabilen organischen Traffic für die handwerkliche Bäckerei."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit professionellem Redaktionskalender für die Autoren-Bäckerei."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die bei Google und Maps nach „handwerkliche Bäckerei in der Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Saisonale Planung: Ostern, Weihnachten, San Juan, lokale Veranstaltungen."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach Stückkalkulation"
      },
      {
        "value": "−30 %",
        "label": "Ausschuss in Backstube und beim Backen"
      },
      {
        "value": "×2",
        "label": "organischer Traffic über Pinterest"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Bäckerei"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierter Sauerteig, inkonsistente Fermentationen von Schicht zu Schicht",
        "Kalkulationen ohne Backstuben-Stundensatz, komplexe Brote unwissentlich mit Verlust",
        "Ausschuss bei Teigen, Vorteigen und Backen ohne Rückverfolgbarkeit",
        "Improvisierte Vitrine und soziale Medien mit Handyfotos",
        "APPCC auf Papier, verstreut in der Backstube"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Sauerteig mit technischem Know-how: konsistente Auffrischungen, Hydratationen und Fermentationen",
        "Professionelle Stückkalkulation mit integriertem Backstuben-Stundensatz",
        "Kontrollierter Ausschuss mit Lebensmittelabfälle AI und spezifischen Vorlagen",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ gewinnen stabilen Traffic",
        "APPCC vom Handy mit prüfungsbereiten Aufzeichnungen"
      ]
    },
    "galleryTitle": "So funktioniert eine handwerkliche Bäckerei",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Vitrine, Sauerteig, Fermentation, Brote, Backen und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-panadero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-masa.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-fermentacion.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-horneado.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-team.jpg"
    ]
  },
  "chocolatero": {
    "h1": "KI für Chocolatier und Pralinenhersteller",
    "heroSubtitle": "Entwerfen Sie Pralinen, Tafeln und Couverturen mit professioneller Kalkulation, Temperiertechnik und saisonaler Planung mit einer Suite von KI-Agenten, die auf handwerkliche Autoren-Schokoladenkunst spezialisiert sind.",
    "heroTagline": "Schokoladenkunst mit authentischer Technik und echter Marge",
    "badge": "Für Chocolatiers, Pralinenhersteller und Schokoladenmeister",
    "painsTitle": "Was ein Chocolatier unbedingt lösen muss",
    "pains": [
      "Kakao mit volatilen Preisen, die die tatsächlichen Kosten jede Woche ohne Vorwarnung ändern und ständige Neuberechnungen der Kalkulationen erfordern",
      "Anspruchsvolle Temperiertechnik: Kristallisation in Form V, präzise Kurven je nach Couverture, konsistenter Glanz und Snap",
      "Abfälle in der Produktion (fehlgeschlagenes Temperieren, Reste, schlecht geformte Formen, Abschrecken), die ohne Kontrolle die Rentabilität untergraben",
      "Extreme Saisonalität: Weihnachten, Valentinstag, Ostern und Roscón konzentrieren einen hohen Prozentsatz des Jahresumsatzes",
      "Sich in einem umkämpften Gebiet mit Autoren-Pralinen, Premium-Verpackung und visuellem Marken-Storytelling differenzieren",
      "Firmenaufträge, Hochzeiten und Events mit Marge gewinnen, während die tägliche Produktion gemanagt wird"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Chocolatier hilft",
    "features": [
      {
        "icon": "Cookie",
        "title": "Kreative Schokolade",
        "description": "Spezialisierter Agent für professionelle Schokoladenkunst: Pralinen, Ganaches, Pralinés, Tafeln, Couverturen, Temperiertechnik und Kristallisationskurven."
      },
      {
        "icon": "Cake",
        "title": "Kreative Patisserie",
        "description": "Für Schokoladendesserts, Häppchen, Brownies, Mousses und fortgeschrittene Kombinationen aus Schokolade und Patisserie."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Stück mit Produktionsstundenkosten",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet diese mit integrierten Produktionsstundenkosten in der echten Marge pro Praline und pro Box."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients AI",
        "description": "Assistent des Sosa-Katalogs für technische Couverturen, konzentrierte Pasten, Nüsse und professionelle Aromen."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chocolatería",
        "description": "Vorlagen: Temperieren, Formen, Ganaches, Montage, Verpackung, Temperaturkontrolle im Kühlraum."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Schokoladenmanufaktur",
        "description": "Rückverfolgbarkeit von Kakao, Milchprodukten, Nüssen, Alkoholen und professioneller Lagerung mit dokumentierten Kurven."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Saisonale Planung mit Schlüsseldaten: Weihnachten, Valentinstag, Ostern, Roscón, Muttertag. Redaktionskalender."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "KI-Referenzfotografie im Autorenstil + Pinterest, wo Premium-Schokolade stabilen organischen Traffic einfängt."
      },
      {
        "icon": "Sparkles",
        "title": "Lebensmittelabfälle AI",
        "description": "Präzise Abfalldaten pro Prozess (Temperieren, Formen, Reste, Ausstellung) integriert in die Kalkulation."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Chocolatiers mit AI Chef Pro",
    "workflow": [
      "07:00 · Öffnung – Checkliste Kit de Tareas Chocolatería: Kühlraumkontrolle, Vorkristallisation der Couverture, Vorbereitung der Polycarbonat-Formen.",
      "08:30 · Kreative Schokolade – Sie entwickeln eine neue Signature-Praline mit karamellisiertem Haselnuss-Praliné und Maldon-Salz. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "09:30 · Sosa Ingredients AI – Sie wählen die technische Couverture mit passendem Kakaogehalt, zusätzlicher Kakaobutter und Qualitätssalz.",
      "10:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren tatsächlichen Kakaopreisen und integrierten Produktionsstundenkosten, validieren die Marge pro Praline und pro 9er-Box.",
      "11:00 · Tagesproduktion – Temperieren auf Marmor, Formen, Ganache, Befüllen, Abschrecken und Entformen.",
      "14:00 · Auffüllen – Vorbereitung professioneller Geschenkboxen, Etikettierung und Abfallkontrolle.",
      "16:00 · Gastro Calendar – Sie bereiten die Weihnachtsplanung mit Firmenkartons vor (Vorlauf 8 Wochen).",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen – Sie generieren ein Referenzbild der neuen Signature-Praline und optimierte Pins für Pinterest.",
      "20:00 · Abschluss – gründliche Reinigung, APPCC unterschrieben, Planung der abzuschreckenden Mischungen."
    ],
    "productsTitle": "Vorlagen und empfohlene Kits für die Schokoladenherstellung",
    "productIds": [
      "kit-tareas-chocolateria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "12.000 Pralinen für Weihnachten ohne System zu produzieren, war Chaos. Mit Kreative Schokolade für das Design, Sosa Ingredients AI für technische Couverture, Kit de Escandallos Pro für die echte Marge mit aktuellem Kakao und Gastro Calendar für die saisonale Planung haben wir die Saison gerettet und die Marge um 7 Punkte gesteigert. Die Firmenkartons werden in einem Anruf mit professionellem Angebot abgeschlossen.",
    "testimonialAuthor": "Mónica Salazar",
    "testimonialRole": "Schokoladenmeisterin und Inhaberin",
    "faqTitle": "Häufige Fragen von Chocolatiers",
    "faqs": [
      {
        "q": "Deckt es professionelle Temperiertechnik und Kristallisationskurven ab?",
        "a": "Ja. Kreative Schokolade denkt wie ein professioneller Chocolatier: Temperieren der Couverture nach Kurven (45-27-31 °C für dunkle Couverture), Tablier-Technik auf Marmor, Impfen, Mikrowelle mit zusätzlicher Kakaobutter. Keine YouTube-Rezepte."
      },
      {
        "q": "Eignet es sich für kleine handwerkliche Schokoladenmanufakturen, Autoren-Ateliers oder Pralinenmanufakturen mit Serienproduktion?",
        "a": "Für alle drei. Die Vorlagen skalieren von der Familien-Produktionsstätte bis zur Produktion für mehrere Verkaufsstellen oder Firmenkartons mit Hunderten von Einheiten."
      },
      {
        "q": "Wie gehen wir mit dem volatilen Kakaopreis um?",
        "a": "Kit de Escandallos Pro berechnet die echte Marge sofort neu, wenn Sie den Preis der Couverture aktualisieren. Lebensmittelabfälle AI ergänzt die Abfallkosten pro Prozess. Die Marge spiegelt immer die aktuellen Kosten wider."
      },
      {
        "q": "Generiert es Inhalte für Vitrine, soziale Medien und Verpackung?",
        "a": "Ja. GastroIMG Gen+ generiert professionelle Referenzbilder jeder Praline für Vitrine, Web und soziale Medien; Pinterest Pins Gen + InstaFlow AI Pro planen visuelle Inhalte; MenuDish Local SEO erfasst lokale Kunden. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie selbst mit Ihrer real angerichteten Praline."
      },
      {
        "q": "Wie hilft es mir bei starker Saisonalität?",
        "a": "Gastro Calendar plant die Schlüsselsaisonen (Weihnachten, Valentinstag, Ostern, Roscón, Muttertag) mit 8-12 Wochen Vorlauf. Das Kit Plan Financiero projiziert den realistischen saisonalen Cashflow, damit Sie mit Produktion und Liquidität jeden Peak erreichen."
      }
    ],
    "ctaTitle": "Ihre Schokoladenmanufaktur mit klarer Marge und Autorentechnik.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Chocolatier und Pralinenhersteller: Temperieren, Kalkulation und Saisonalität | AI Chef Pro",
      "description": "KI-Suite für professionelle Chocolatiers: Kreative Schokolade, Kalkulation pro Stück mit Produktionsstundenkosten, saisonale Planung und APPCC. Starten Sie noch heute.",
      "keywords": "KI Chocolatier, KI Pralinenhersteller, Software Schokoladenmanufaktur, Pralinenkalkulation, handwerkliche Schokolade KI, Temperiertechnik, Kristallisationskurven, Schokoladenmeister",
      "ogImage": "https://aichef.pro/og/use-cases/chocolatero.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Atelier zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen konversationellen Onboarding, bei dem Sie erzählen, welche Art von Schokoladenmanufaktur Sie betreiben (Autoren-Atelier, Pralinenmanufaktur mit Serienproduktion, Schokoladenmanufaktur mit Café, Produktionsstätte für den Verkauf an die Gastronomie, Schokoladenmanufaktur mit Erlebnissen und Verkostungen), Teamgröße, Stadt und Spezialität. Jeder Agent – von Kreative Schokolade bis Gastro Calendar – antwortet angepasst an Ihr Produkt, Ihren Markt und Ihre reale Betriebsweise.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Atelier nutzen werden",
    "apps": [
      {
        "name": "Kreative Schokolade",
        "category": "Kulinarische Kreativität",
        "description": "Spezialisierter Agent für professionelle Schokoladenkunst: Pralinen, Ganaches, Pralinés, Tafeln und Temperiertechnik."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Schokoladendesserts, Häppchen, Brownies, Mousses und fortgeschrittene Kombinationen."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Pralinen mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog: technische Couverturen, konzentrierte Pasten, Nüsse und professionelle Aromen."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Assistent des tSpoonLab-Katalogs für fortgeschrittene Schokoladenanwendungen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Abfälle beim Temperieren, Formen, Reste und Ausstellung integriert in die Kalkulation."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Allergenerkennung pro Praline: Milchprodukte, Nüsse, Gluten, Alkohole."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Referenzfotografie im Autorenstil für Vitrine, Web, Verpackung und soziale Medien."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und soziale Medien",
        "description": "Pinterest erfasst stabilen organischen Traffic für Premium-Schokolade."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit Redaktionskalender für Autoren-Schokoladenmanufakturen."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die bei Google und Maps nach „handwerkliche Schokolade in der Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Saisonale Planung: Weihnachten, Valentinstag, Ostern, Roscón, Muttertag."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "Marge nach Kalkulation der Pralinen"
      },
      {
        "value": "−35 %",
        "label": "Abfälle in Produktion und Vitrine"
      },
      {
        "value": "×2",
        "label": "Firmenaufträge zu Weihnachten"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihr Atelier"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisiertes Temperieren: inkonsistenter Glanz und Snap von Stück zu Stück",
        "Volatiler Kakao, der die Preise durcheinanderbringt, ohne in Echtzeit neu zu berechnen",
        "Abfälle beim Temperieren, Formen und in der Vitrine ohne echte Rückverfolgbarkeit",
        "Reaktive saisonale Produktion: Sie kommen zu spät zu Weihnachten und verlieren Firmenaufträge",
        "APPCC auf gedrucktem Papier, verstreut im Atelier"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Temperieren nach Kurven mit technischem Kriterium, konsistenter Glanz und Snap",
        "Professionelle Kalkulation pro Praline mit aktualisierbarem Kakao und integrierten Stundenkosten",
        "Kontrollierte Abfälle mit Lebensmittelabfälle AI und spezifischen Vorlagen",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ erfassen stabilen Traffic und Aufträge",
        "APPCC vom Handy mit prüfungsbereiten Aufzeichnungen"
      ]
    },
    "galleryTitle": "So funktioniert ein Schokoladen-Atelier",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Temperieren, Formen, Pralinen, Ganache und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chocolatero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-temperado.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-bombones.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-moldeado.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-ganache.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-team.jpg"
    ]
  },
  "chef-privado-personal": {
    "h1": "KI für Privatkoch und Personal Chef",
    "heroSubtitle": "Entwerfen Sie personalisierte Menüs für einzigartige Kunden, kalkulieren Sie jedes private Abendessen mit echten Kosten, planen Sie die Mise en Place in Privathäusern und gewinnen Sie professionelles Branding mit einer Suite von gastronomischen KI-Agenten, die auf Privatkoch und Service in Privathäusern spezialisiert sind.",
    "heroTagline": "Privater Service mit echtem Gewinn und eigener Technik",
    "badge": "Für Privatköche, Personal Chefs und intimes Catering",
    "painsTitle": "Was ein Privatkoch unbedingt lösen muss",
    "pains": [
      "Vollständig personalisierte Menüs pro Kunde entwerfen: Allergien, Unverträglichkeiten, Vorlieben, Diät, Anlass und Ästhetik des Anrichtens",
      "Jedes private Abendessen mit echten Kosten kalkulieren (Tageseinkauf, Premium-Zutaten) und personalisiertem Preis",
      "Mise en Place in Privathäusern mit nicht-professionellen Küchen planen (ohne Ausrüstung, begrenzter Platz, unbekannte Herde)",
      "Technische Datenblätter standardisieren, damit der Kunde das Menü wiederholen oder das Rezept als Erinnerung aufbewahren kann",
      "Sich in einem umkämpften Gebiet mit persönlichem Storytelling, visuellem Branding mit eigener Handschrift und Akquise über soziale Medien differenzieren",
      "Wiederkehrende Premium-Kunden gewinnen (VIP-Familien, Führungskräfte, Prominente) mit professionellen und personalisierten Angeboten"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Privatkoch hilft",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Privatkoch Pro",
        "description": "Spezialisierter Agent aus dem Katalog Gastro Profile Pro: denkt wie ein professioneller Privatkoch mit Erfahrung in Privathäusern und intimen Veranstaltungen."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für die Entwicklung personalisierter Menüs mit fortgeschrittener Technik: Signature-Anrichtungen, kontrollierte Fusionen, Signature-Desserts."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Personalisierte Pairings mit dem Weinkeller des Kunden oder Weinempfehlungen für jedes Gericht des privaten Menüs."
      },
      {
        "icon": "Calculator",
        "title": "Calcula Pax + Kalkulation",
        "description": "Calcula Pax skaliert Rezepte auf 2, 6, 12 Gäste; Kit de Escandallos Pro verwaltet es mit echten Kosten pro privatem Abendessen und personalisiertem Preis."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chef Privado",
        "description": "Vorlagen: Vorbesuch der Kundenküche, Einkaufsliste, transportable Mise en Place, Serviceplan, Reinigung, Rechnung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergen-ID",
        "description": "Automatische Identifizierung von Allergenen pro Kunde: entscheidend, wenn Sie mit Familien mit spezifischen Unverträglichkeiten arbeiten."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planung saisonaler Menüs und für besondere Anlässe: Weihnachten, Valentinstag, Jahrestage, Geburtstage."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Premium-KI-Referenzfotografie + Instagram, um neue Kunden zu gewinnen und eine eigene Reputation aufzubauen."
      },
      {
        "icon": "BookOpen",
        "title": "Technisches Datenblatt + Rechnung",
        "description": "Professionelle Vorlage zur Übergabe an den Kunden: technisches Datenblatt des Menüs mit Rezept + Storytelling + klare Rechnung."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Privatkochs mit AI Chef Pro",
    "workflow": [
      "07:00 · Vorbesuch – Checkliste Kit de Tareas Chef Privado: Überprüfung der Küche des Kunden (Geräte, Platz, Allergien und bestätigte Vorlieben).",
      "08:00 · Privatkoch Pro – Sie entwickeln das personalisierte Menü für ein intimes Abendessen für 6 Personen mit Nussallergie. Kreativküche liefert Rezept + Kalkulation als CSV.",
      "09:00 · Calcula Pax – Sie skalieren die Rezepte von 6 auf 8 Gäste (der Kunde hat zwei Gäste hinzugefügt). Kit de Escandallos Pro berechnet Kosten und Angebot neu.",
      "10:00 · Einkaufsliste – Sie gehen mit der priorisierten Liste zum Markt: Tagesprodukt, spezifische Premium-Zutaten.",
      "14:00 · Ankunft beim Kunden zu Hause – Aufbau der Mise en Place in der Privatküche gemäß dem transportablen Plan, Organisation des Raums.",
      "17:00 · Abendessen-Service – Umsetzung des Menüs mit professioneller Technik, angepasst an die Küche des Kunden, Anrichten auf feinem Porzellan.",
      "21:00 · Abschluss mit dem Kunden – Übergabe des technischen Datenblatts des Menüs mit Storytelling + professioneller Rechnung + Referenzfoto des Menüs.",
      "23:00 · Nach dem Abendessen – InstaFlow AI Pro: Instagram-Post mit dem Referenzbild des Menüs (ohne Gesichter des Kunden), um Reputation aufzubauen."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Privatkoch",
    "productIds": [
      "kit-tareas-chef-privado",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Privatkoch Pro hat mein Geschäftsangebot verändert. Jetzt erhält jeder Kunde ein personalisiertes Menü mit professioneller Kalkulation und Storytelling, und die Kundenakquise über Instagram mit GastroIMG Gen+ hat sich vervielfacht. Ich schließe Angebote in einem Anruf ab, weil ich am selben Tag das technische Datenblatt + die Rechnung übergebe. Wir haben den durchschnittlichen Umsatz pro Abend um 35 % gesteigert.",
    "testimonialAuthor": "Andrea Gómez",
    "testimonialRole": "Freiberufliche Privatköchin, Madrid + Küste",
    "faqTitle": "Häufig gestellte Fragen von Privatköchen",
    "faqs": [
      {
        "q": "Funktioniert es für freiberufliche Privatköche, Personal-Chef-Agenturen oder intimes Catering?",
        "a": "Für alle drei. Privatkoch Pro denkt wie ein professioneller Personal Chef, es funktioniert sowohl für Freiberufler, die ihr Angebot gestalten, als auch für Agenturen mit mehreren Köchen."
      },
      {
        "q": "Wie verwalte ich Allergien und spezielle Diäten pro Kunde?",
        "a": "Allergen-ID identifiziert automatisch Allergene pro Rezept. Privatkoch Pro denkt in Bezug auf Personalisierung: Keto-, vegane, glutenfreie, natriumarme, FODMAP-Diäten, Schwangerschaft. Jeder Kunde erhält ein wirklich angepasstes Menü."
      },
      {
        "q": "Wie skaliere ich Rezepte für verschiedene Gästezahlen?",
        "a": "Calcula Pax skaliert die Rezepte auf 2, 6, 12 oder jede andere Gästezahl ohne Präzisionsverlust. Kit de Escandallos Pro berechnet die Kosten pro Person und das wirtschaftliche Angebot für den Kunden neu."
      },
      {
        "q": "Erzeugt es visuellen Content für Instagram und eine eigene Reputation?",
        "a": "Ja. GastroIMG Gen+ erzeugt professionelle Referenzbilder des Menüs (ohne den Kunden zu zeigen) für Instagram, Web und Portfolio. Denken Sie daran, dass das KI-Bild eine visuelle Referenz ist: Das endgültige Foto machen Sie selbst mit Ihrem tatsächlich angerichteten Teller bei jedem Abendessen."
      },
      {
        "q": "Wie hilft es mir bei der Gewinnung wiederkehrender Kunden?",
        "a": "GastroIMG Gen+ + InstaFlow AI Pro erstellen kontinuierlichen visuellen Content; MenuDish Local SEO gewinnt lokale Kunden, die nach \"Privatkoch in [Stadt]\" suchen; Gastro Calendar hilft, saisonale Menüs vorzuschlagen (intimes Weihnachten, Valentinstag, Jahrestage), um Kunden zu binden."
      }
    ],
    "ctaTitle": "Ihr Privatkoch-Service mit echtem Gewinn und eigener Handschrift.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits, um alle Agenten zu nutzen.",
    "seo": {
      "title": "KI für Privatkoch und Personal Chef: Menüs, Kalkulationen und Service | AI Chef Pro",
      "description": "KI-Suite für professionelle Privatköche: Privatkoch Pro, Kalkulationen pro Abendessen, personalisierte Menüs, Branding und Akquise. Starten Sie noch heute.",
      "keywords": "KI Privatkoch, KI Personal Chef, Software Privatkoch, Kalkulation privates Abendessen, Privatkoch Madrid, Personal Chef Freiberufler",
      "ogImage": "https://aichef.pro/og/use-cases/chef-privado.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Privatkoch-Service zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational Onboarding, bei dem Sie erzählen, welche Art von Service Sie betreiben (freiberuflicher Privatkoch, Agentur mit mehreren Köchen, intimes Catering für Hochzeiten und private Veranstaltungen, Yachtkoch), welche Art von Kundschaft (VIP-Familien, Führungskräfte, Prominente), Stadt und Spezialgebiet. Jeder Agent – vom Privatkoch Pro bis zum Gastro Calendar – antwortet angepasst an Ihr Angebot und Ihre tatsächliche Arbeitsweise.",
    "appsTitle": "Die KI-Agenten, die Sie als Privatkoch nutzen werden",
    "apps": [
      {
        "name": "Privatkoch Pro",
        "category": "Gastro Profile Pro",
        "description": "Spezialisierter Agent aus dem Katalog Gastro Profile Pro: denkt wie ein professioneller Privatkoch."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung personalisierter Menüs mit fortgeschrittener Technik und Rezept + Kalkulation als CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Personalisierte Pairings mit dem Weinkeller des Kunden oder Weinempfehlungen."
      },
      {
        "name": "Calcula Pax",
        "category": "Werkzeuge und Utilities",
        "description": "Skalierung von Rezepten für verschiedene Gästezahlen."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Kunde und Rezept."
      },
      {
        "name": "Conversor Ing",
        "category": "Werkzeuge und Utilities",
        "description": "Umrechner für Gewichte und Maße, entscheidend bei der Arbeit mit nicht-professionellen Küchen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Lebensmittelabfälle bei Tageseinkauf und Premium-Produkten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Premium-KI-Referenzfotografie für Instagram, Portfolio und Akquise."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit professionellem Redaktionskalender, um wiederkehrende Kunden zu gewinnen."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die in Google und Maps nach \"Privatkoch in [Stadt]\" suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Saisonale Menüs: intimes Weihnachten, Valentinstag, Jahrestage, Geburtstage."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Für personalisierte Cocktails bei privaten Abendessen."
      }
    ],
    "metrics": [
      {
        "value": "+35 %",
        "label": "durchschnittlicher Umsatz pro privatem Abendessen"
      },
      {
        "value": "×3",
        "label": "Kundenakquise über Instagram"
      },
      {
        "value": "×5",
        "label": "Geschwindigkeit von Geschäftsangeboten"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihren privaten Service"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Personalisierte Menüs von Hand: eine Woche pro Angebot",
        "Kalkulationen ohne echte Kosten, Geschäftsangebote mit unsicherer Marge",
        "Vorbesuch und Mise en Place jedes Mal improvisiert",
        "Akquise durch Mundpropaganda, ohne konstantes Instagram",
        "Kein technisches Datenblatt für den Kunden als Erinnerung"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Personalisierte Menüs in einer Stunde mit Privatkoch Pro",
        "Professionelle Kalkulation pro Abendessen mit validierter Marge",
        "Vorbesuch und Mise mit transportabler Vorlage Kit de Tareas",
        "Konstante Akquise mit GastroIMG Gen+ + InstaFlow AI Pro",
        "Technisches Datenblatt des Menüs + Rechnung am selben Tag übergeben"
      ]
    },
    "galleryTitle": "So funktioniert der Privatkoch-Service",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren werden: Mise en Place, angerichteter Teller, gedeckter Tisch, Vorratskammer und Service. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-privado-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-plato.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-mesa.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-despensa.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-team.jpg"
    ]
  },
  "fb-manager-hotel": {
    "h1": "KI für F&B-Manager im Hotel",
    "heroSubtitle": "Koordinieren Sie Restaurants, Bankette, Room Service, Frühstücksbuffets und Hotelbars mit übergreifender Kalkulation, professionellen Betriebsvorlagen und integriertem Branding – mit einer Suite gastronomischer KI-Agenten, die auf das ganzheitliche Hotel-F&B-Management spezialisiert sind.",
    "heroTagline": "Hotel-F&B mit echter Marge und professioneller Betriebsführung",
    "badge": "Für F&B-Manager und Direktoren für Speisen und Getränke",
    "painsTitle": "Was ein F&B-Manager unbedingt lösen muss",
    "pains": [
      "Mehrere Outlets gleichzeitig koordinieren (Hauptrestaurant, Room Service, Frühstücksbuffet, Poolbar, Bankette, Café)",
      "Übergreifende Speisekartenkalkulation zwischen Outlets bei gleichbleibender Food-Cost-Konsistenz und integrierter Marge",
      "Hohe Lebensmittelabfälle beim Frühstücksbuffet (reichhaltiges Angebot bei variablem Verbrauch) und bei Banketten (hohes Volumen, logistische Komplexität)",
      "Standardisierung von Abläufen pro Schicht mit rotierenden Teams und drei täglichen Services",
      "Sich in einem umkämpften Hotelmarkt durch ein ganzheitliches gastronomisches Erlebnis, visuelles Branding und Hospitality-Storytelling differenzieren",
      "Gewinnung von Firmenevents, Hochzeiten und Premium-Banketten mit professionellen Angeboten und validierter Marge"
    ],
    "featuresTitle": "Wie AI Chef Pro einem F&B-Manager hilft",
    "features": [
      {
        "icon": "Hotel",
        "title": "Profi Restaurantmanager",
        "description": "Spezialisierter Agent aus dem Katalog Gastro Profile Pro, angepasst an das Multi-Outlet-F&B-Management im Hotel."
      },
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Professionelle Beratung für Bankette, Hochzeiten und Firmenevents des Hotels."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für die Entwicklung integrierter Speisekarten: Hauptrestaurant, Frühstücksbuffet, Room Service und Poolbar mit Konsistenz."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Für die Cocktailkarte der Poolbar, der Lobby-Bar und Pairings im Hauptrestaurant."
      },
      {
        "icon": "Calculator",
        "title": "Übergreifende Kalkulationen",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet sie mit outletübergreifenden Kosten und integrierter Marge."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Hotel Completo",
        "description": "Vorlagen für 5 Outlets: Restaurant, Frühstück, Room Service, Bar, Bankette mit Schichtabläufen."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC hotelero",
        "description": "Rückverfolgbarkeit für Buffet, Bankette, Room Service und Bar mit kritischen Temperaturen und Lagerung."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planung von Firmenevents, Hochzeiten, Saisons (Sommer/Winter), Weihnachten, Valentinstag, Konferenzen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Premium-KI-Referenzfotografie + Instagram für alle Hotel-Outlets mit Markenkonsistenz."
      }
    ],
    "workflowTitle": "Ein echter Tag eines F&B-Managers mit AI Chef Pro",
    "workflow": [
      "06:00 · Frühstückseröffnung – Checkliste Kit de Tareas Hotel: Buffetvorbereitung, Kontrolle der Chafing Dishes, Temperaturen, Mise en Place der Eierstation.",
      "09:00 · Koordination mit der Hauptküche – Kreativküche aktualisiert die Mittagskarte mit saisonalen Produkten. Rezept + CSV-Kalkulation.",
      "10:00 · Catering AI+ – Sie entwickeln den Menüvorschlag für eine Hochzeit mit 120 Personen und drei Gängen. Calcula Pax skaliert Rezepte, Kit de Escandallos Pro validiert Kosten und Marge.",
      "12:00 · Mittagsservice im Hauptrestaurant + Room Service – übergreifende Koordination zwischen den Outlets.",
      "14:00 · Bar & Lounge AI+ – Sie entwickeln die neue Cocktailkarte für die Poolbar in der Sommersaison.",
      "17:00 · Firmenbankett mit 80 Personen – Umsetzung mit der spezifischen Vorlage des Kit de Tareas.",
      "20:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren Referenzbilder für die vier Outlets und konsistente Posts für das Hotel-Instagram.",
      "23:00 · Abschluss – gründliche Reinigung aller Outlets, unterschriebenes APPCC, Planung des Frühstücks und der Services für den nächsten Tag."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für F&B-Manager",
    "productIds": [
      "kit-tareas-hotel",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Fünf Outlets ohne System zu managen, war Chaos. Profi Restaurantmanager + Catering AI+ koordinieren für uns die übergreifende Speisekarte, Bankette und Room Service mit integrierter Kalkulation. Die Planung von Hochzeiten mit 120 Personen, die früher eine Woche dauerte, ist jetzt an einem Tag mit professionellem Angebot erledigt. Wir haben die Marge um 5 Punkte gesteigert, indem wir Outlets verknüpft haben, und schließen Premium-Events viel schneller ab.",
    "testimonialAuthor": "Roberto Castaño",
    "testimonialRole": "F&B-Direktor, 5-Sterne-Hotel",
    "faqTitle": "Häufige Fragen von F&B-Managern",
    "faqs": [
      {
        "q": "Funktioniert es für ein Boutique-Hotel, ein Kettenhotel, All-inclusive oder ein Luxushotel?",
        "a": "Für alle vier. Profi Restaurantmanager + Catering AI+ + Bar & Lounge AI+ decken vom Boutique-Hotel mit einem Restaurant bis zum 5-Sterne-Hotel mit 5+ Outlets, All-inclusive mit großem Buffet oder Ferienresort ab."
      },
      {
        "q": "Wie koordiniere ich die übergreifende Speisekarte zwischen den Outlets?",
        "a": "Kreativküche denkt kohärent zwischen den Outlets: Produkte der Hauptkarte werden im Frühstück, im Room Service und bei Banketten genutzt, wodurch die integrierte Food Cost optimiert und übergreifende Lebensmittelabfälle reduziert werden."
      },
      {
        "q": "Wie skaliere ich Kalkulationen für Bankette mit 50, 100 oder 300 Personen?",
        "a": "Calcula Pax skaliert die Rezepte ohne Präzisionsverlust; Kit de Escandallos Pro berechnet die Kosten pro Person und das wirtschaftliche Angebot für den Firmen- oder Hochzeitskunden neu."
      },
      {
        "q": "Erzeugt es konsistente visuelle Inhalte für das Hotel-Instagram?",
        "a": "Ja. GastroIMG Gen+ erzeugt professionelle Referenzbilder für die vier Outlets mit Markenkonsistenz; InstaFlow AI Pro plant Instagram. Denken Sie daran: Das KI-Bild dient als visuelle Referenz – das endgültige Foto machen Sie mit Ihrem real angerichteten Gericht."
      },
      {
        "q": "Wie hilft es mir bei Firmenevents und Saisons?",
        "a": "Gastro Calendar plant Firmenevents, Hochzeiten, Konferenzen, Saisons (Sommer/Winter), Weihnachten und Valentinstag mit spezifischen Menüs pro Outlet und koordiniertem Redaktionskalender."
      }
    ],
    "ctaTitle": "Ihr Hotel-F&B mit integrierter Marge und professioneller Betriebsführung.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für F&B-Manager im Hotel: Multi-Outlet, Bankette und Kalkulationen | AI Chef Pro",
      "description": "KI-Suite für Hotel-F&B-Manager: Profi Restaurantmanager, Catering AI+, übergreifende Kalkulationen, Multi-Outlet-Branding und integriertes APPCC. Starten Sie noch heute.",
      "keywords": "KI F&B Manager, KI Hotel F&B, Hotel-Restaurant-Software, Hotel-Kalkulationen, Hotel-Bankette KI, Hotel-Frühstücksbuffet",
      "ogImage": "https://aichef.pro/og/use-cases/fb-manager-hotel.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Hotel personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten «Wer sind Sie?», einem 2-minütigen Conversational Onboarding, bei dem Sie uns mitteilen, welche Art von Hotel Sie betreiben (Boutique, Kette, 5-Sterne, All-inclusive, Ferienresort), Anzahl der F&B-Outlets, Teamgröße und Spezialität. Jeder Agent – vom Profi Restaurantmanager bis zu Catering AI+ – antwortet angepasst an Ihr reales Hotel.",
    "appsTitle": "Die KI-Agenten, die Sie als F&B-Manager nutzen werden",
    "apps": [
      {
        "name": "Profi Restaurantmanager",
        "category": "Gastro Profile Pro",
        "description": "Spezialisierter Agent, angepasst an das Multi-Outlet-F&B-Management im Hotel."
      },
      {
        "name": "Catering AI+",
        "category": "Geschäftskonzepte",
        "description": "Bankette, Hochzeiten und Firmenevents des Hotels mit professionellen Angeboten."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Integrierte Speisekarten mit Konsistenz zwischen den Outlets und Rezept + CSV-Kalkulation."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Für die Cocktailkarte der Poolbar, der Lobby-Bar und Pairings im Hauptrestaurant."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Für das Casual-Restaurant und das Café des Hotels."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools und Utilities",
        "description": "Skalierung von Rezepten für Bankette mit 50, 100, 300 oder 500 Personen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Lebensmittelabfälle beim Frühstücksbuffet, bei Banketten und im Room Service."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifikation für Gäste mit Allergien bei Banketten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Premium-KI-Referenzfotografie mit Markenkonsistenz für alle Outlets."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und Social Media",
        "description": "Instagram mit koordiniertem Redaktionskalender für alle Outlets."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und Social Media",
        "description": "Lokale Gäste gewinnen, die bei Google und Maps nach \"Hotelrestaurant\" suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und Social Media",
        "description": "Firmenevents, Hochzeiten, Konferenzen, Weihnachten, Valentinstag, Saisons."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach übergreifender Kalkulation"
      },
      {
        "value": "×7",
        "label": "Geschwindigkeit bei Bankettangeboten"
      },
      {
        "value": "−25 %",
        "label": "Lebensmittelabfälle beim Frühstücksbuffet"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihr F&B"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Outlets manuell koordiniert, übergreifende Food Cost ohne Rückverfolgbarkeit",
        "Bankette manuell kalkuliert: eine Woche pro Hochzeit",
        "Lebensmittelabfälle beim Frühstücksbuffet ohne echte Kontrolle",
        "Visuelles Branding zwischen Outlets verstreut, ohne Konsistenz",
        "APPCC als Ausdruck, verstreut über die Outlets"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Outlets koordiniert mit übergreifender Kalkulation und integrierter Food Cost",
        "Bankette in einem Tag kalkuliert, mit professionellem Angebot",
        "Lebensmittelabfälle kontrolliert mit Lebensmittelabfälle AI bei Frühstück und Banketten",
        "Konsistentes Branding mit GastroIMG Gen+ + InstaFlow AI Pro",
        "APPCC mobil für alle Outlets, mit Aufzeichnungen bereit für Inspektionen"
      ]
    },
    "galleryTitle": "So funktioniert das F&B eines Hotels",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren werden: Restaurant, Bankette, Frühstück, Room Service und Poolbar. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-fb-manager-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-banquet.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-breakfast.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-roomservice.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-bar.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-team.jpg"
    ]
  },
  "maitre-jefe-sala": {
    "h1": "KI für Maître und Serviceleiter",
    "heroSubtitle": "Koordinieren Sie den Service im Saal mit professioneller Technik, verwalten Sie Premium-Reservierungen und Pairings, führen Sie das Team und erfassen Sie Fine-Dining-Branding mit einer Suite von gastronomischen KI-Agenten, die auf hochwertigen Service und Servicebereich spezialisiert sind.",
    "heroTagline": "Servicebereich mit professioneller Technik und unvergesslichem Erlebnis",
    "badge": "Für Maîtres, Serviceleiter und Servicedirektoren",
    "painsTitle": "Was ein Maître unbedingt lösen muss",
    "pains": [
      "Koordinieren Sie den Service im Saal mit perfekter Gangfolge, Gueridon, Dekantieren und professionellem Service Schicht für Schicht",
      "Verwalten Sie Premium-Reservierungen mit Tischplanung, Allergien, besonderen Anlässen und Präferenzen von Stammgästen",
      "Führen Sie das Service-Team mit kontinuierlicher Schulung in Pairings, Besteck, Gerichtsbeschreibungen und Storytelling",
      "Koordinieren Sie mit der Küche Gang für Gang mit perfektem Timing und flüssiger Kommunikation in Stoßzeiten",
      "Heben Sie sich in einem umkämpften Restaurant mit unvergesslichem Erlebnis, visuellem Fine-Dining-Branding und der Gewinnung von Stammgästen ab",
      "Akquirieren Sie private Veranstaltungen und Firmenessen mit professionellen Service- und Pairing-Vorschlägen"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Maître hilft",
    "features": [
      {
        "icon": "Crown",
        "title": "Profi Restaurantmanager",
        "description": "Spezialisierter Agent für Fine-Dining-Servicebereich: Serviceablauf, Gueridon, Dekantieren, Teamtraining."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Für professionelles Weinkeller-Management, Dekantieren, Weinempfehlungen und professionelle Cocktailkunst."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Wissenschaftlich fundierte Pairings für jedes Menügericht, professionelle Begründung für das Service-Team."
      },
      {
        "icon": "Calculator",
        "title": "Calcula Pax + Mise",
        "description": "Calcula Pax für Bankette, Vorlagen für Tischdekoration, Gueridon, Gangfolge."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Vorlagen: Vorbereitung (Mise), Serviceschicht (Gänge), Nachbereitung (Kassenabgleich, Reinigung), Teamtraining."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC sala",
        "description": "Rückverfolgbarkeit des Weinkellers, Weinlagerung, Dekantieren und Serviertemperaturen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Premium-Reservierungen, private Veranstaltungen, Firmenessen, Weihnachten, Valentinstag, Jubiläen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Elegante KI-Referenzfotografie + Instagram mit Service-Storytelling und Pairings zur Gewinnung von Premium-Kunden."
      },
      {
        "icon": "BookOpen",
        "title": "Menü-Storytelling",
        "description": "Generierung von Gerichtsbeschreibungen und Pairings, damit das Service-Team sie professionell vor dem Gast präsentieren kann."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Maître mit AI Chef Pro",
    "workflow": [
      "15:00 Uhr · Eröffnung – Checkliste Kit de Tareas: Überprüfung der Tagesreservierungen, Tischdekoration, Polieren von Gläsern und Besteck, Weinkellerkontrolle.",
      "16:00 Uhr · Briefing für das Team – Erklärung der neuen Tagesgerichte mit generiertem Storytelling und validierten Pairings mit Food Pairing AI.",
      "17:00 Uhr · Koordination mit der Küche – Überprüfung von Kartenänderungen, bestätigte Allergien, Mise en Place der Gänge.",
      "18:30 Uhr · Empfang der ersten Reservierungen – professionelle Betreuung, Aperitif-Service, Beschreibung der Karte.",
      "20:00 Uhr · Abendservice – Gang-für-Gang-Koordination mit der Küche, professionelles Dekantieren, Gueridon am Tisch, wenn zutreffend.",
      "22:00 Uhr · Private Firmenessen – engagierte Betreuung für ein Event mit 12 Personen mit Degustationsmenü und Pairings.",
      "00:00 Uhr · Abschluss – Kassenabgleich, Verabschiedung des Teams, GastroIMG Gen+ generiert ein Referenzbild des Degustationsmenüs + InstaFlow plant den Post.",
      "01:00 Uhr · Abschluss-Briefing – Feedback des Teams, Notieren von Gästekommentaren, Planung des nächsten Tages."
    ],
    "productsTitle": "Vorlagen und empfohlene Kits für Maître",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Profi Restaurantmanager + Bar & Lounge AI+ + Food Pairing AI haben das Niveau meines Service-Teams komplett angehoben. Das tägliche Briefing mit generiertem Storytelling für jedes Gericht und wissenschaftlich validiertem Pairing ist jetzt professionell. Die Gäste merken den Unterschied: Wir haben den durchschnittlichen Ticketwert um 20 % gesteigert und die Quote der Premium-Stammgäste ist in sechs Monaten um 40 % gewachsen.",
    "testimonialAuthor": "Sofía Vega",
    "testimonialRole": "Maître und Serviceleiterin, Fine-Dining-Restaurant",
    "faqTitle": "Häufige Fragen von Maîtres",
    "faqs": [
      {
        "q": "Funktioniert es für Fine Dining, Autorenrestaurants, Michelin-Gastronomie oder Premium-Restaurants?",
        "a": "Für alle vier. Profi Restaurantmanager + Bar & Lounge AI+ decken vom Premium-Restaurant bis zur Michelin-Gastronomie ab – mit tadellosem Service, Gueridon, professionellem Dekantieren und Storytelling."
      },
      {
        "q": "Wie verwalte ich Premium-Reservierungen und Stammgäste?",
        "a": "Profi Restaurantmanager denkt mit professionellem Service-Verständnis: Tischplanung nach Präferenz, Notieren von Allergien und Anlässen, Gewinnung von Stammgästen mit personalisierten Menüs."
      },
      {
        "q": "Wie schule ich mein Service-Team in Pairings und Storytelling?",
        "a": "Food Pairing AI untermauert jedes Pairing mit wissenschaftlicher Basis, die das Team dem Gast kommunizieren kann; Bar & Lounge AI+ vertieft Weinkeller, Dekantieren und Techniken. Das tägliche Briefing ist jetzt professionell."
      },
      {
        "q": "Generiert es elegante visuelle Inhalte für Instagram?",
        "a": "Ja. GastroIMG Gen+ generiert elegante Referenzbilder des Menüs und des gedeckten Tisches für Instagram, Web und die Gewinnung von Premium-Kunden. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie mit Ihrem echten Tisch."
      },
      {
        "q": "Wie hilft es mir bei privaten Veranstaltungen und Firmenessen?",
        "a": "Gastro Calendar plant private Veranstaltungen, Firmenessen, Weihnachten, Valentinstag, Jubiläen mit Degustationsmenüs und Vorschlägen für engagierten Service."
      }
    ],
    "ctaTitle": "Ihr Servicebereich mit professioneller Technik und unvergesslichem Erlebnis.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Maître und Serviceleiter: Service, Pairings und Storytelling | AI Chef Pro",
      "description": "KI-Suite für professionelle Maîtres: Profi Restaurantmanager, Bar & Lounge AI+, Food Pairing AI, Teamtraining und Premium-Akquise. Starten Sie noch heute.",
      "keywords": "KI Maître, KI Serviceleiter, Maître Software, Fine Dining Service, Gueridon Dekantieren KI, Teamtraining Service",
      "ogImage": "https://aichef.pro/og/use-cases/maitre-jefe-sala.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Servicebereich personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen conversational Onboarding, bei dem Sie erzählen, welche Art von Servicebereich Sie leiten (Fine Dining, Autorenrestaurant, Michelin/Repsol-Gastronomie, Premium-Restaurant mit Weinkeller), Teamgröße, Stadt und Spezialität. Jeder Agent antwortet angepasst an Ihren Servicebereich und Ihre tatsächliche Arbeitsweise.",
    "appsTitle": "Die KI-Agenten, die Sie als Maître nutzen werden",
    "apps": [
      {
        "name": "Profi Restaurantmanager",
        "category": "Gastro Profile Pro",
        "description": "Spezialisierter Agent für Fine-Dining-Servicebereich."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Weinkeller-Management, Dekantieren, Weinempfehlungen und professionelle Cocktailkunst."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Wissenschaftlich fundierte Pairings für jedes Menügericht."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Storytelling und Gerichtsbeschreibungen für das Service-Team."
      },
      {
        "name": "Calcula Pax",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Skalierung von Rezepten für private Veranstaltungen und Firmenessen."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Automatische Identifizierung von Allergenen zur Kommunikation an den Gast."
      },
      {
        "name": "Mental Coach",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Coaching für Führung des Service-Teams und Stressmanagement in Stoßzeiten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Elegante KI-Referenzfotografie für Instagram, Web und Premium-Akquise."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit elegantem Redaktionskalender für Fine Dining."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Premium-Kunden gewinnen, die in Google und Maps nach Fine Dining suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Private Veranstaltungen, Firmenessen, Weihnachten, Valentinstag, Jubiläen."
      },
      {
        "name": "Mitarbeiteressen AI",
        "category": "Gastro Profile Pro",
        "description": "Generator für Mitarbeitermenüs vor dem Service."
      }
    ],
    "metrics": [
      {
        "value": "+20 %",
        "label": "durchschnittlicher Ticketwert Fine Dining"
      },
      {
        "value": "×1.4",
        "label": "Quote Stammgäste"
      },
      {
        "value": "×2",
        "label": "Geschwindigkeit der Event-Vorschläge"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihren Servicebereich"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisiertes Team-Briefing, Storytelling ohne Substanz",
        "Empfohlene Pairings ohne wissenschaftliche Fundierung",
        "Premium-Reservierungen ohne Planung von Präferenzen und Allergien",
        "Private Veranstaltungen manuell abgeschlossen, langsame Vorschläge",
        "Improvisiertes Instagram ohne Service-Storytelling"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Tägliches professionelles Briefing mit Storytelling und Pairings",
        "Wissenschaftlich fundierte Pairings von Food Pairing AI",
        "Premium-Reservierungen mit professioneller Planung und Stammgast-Akquise",
        "Private Veranstaltungen in einem Tag abgeschlossen mit Service-Vorschlag",
        "Elegantes Instagram mit GastroIMG Gen+ + InstaFlow AI Pro"
      ]
    },
    "galleryTitle": "So funktioniert der Servicebereich eines Fine-Dining-Restaurants",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren werden: Tischdekoration, Dekantieren, Gueridon, Service und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-maitre-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-mesa.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-pour.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-servicio.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-gueridon.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-team.jpg"
    ]
  },
  "sommelier": {
    "h1": "KI für Sommeliers",
    "heroSubtitle": "Entwerfen Sie Weinkarten mit professionellem Anspruch, validieren Sie Weinbegleitungen mit wissenschaftlicher Basis, verwalten Sie den Keller mit Rückverfolgbarkeit und erfassen Sie wine-driven Branding mit einer Suite von gastronomischen KI-Agenten, die auf professionelle Sommellerie spezialisiert sind.",
    "heroTagline": "Weinkeller mit professionellem Anspruch und wissenschaftlichen Weinbegleitungen",
    "badge": "Für Sommeliers, Head Sommeliers und Weinkellerleiter",
    "painsTitle": "Was ein Sommelier unbedingt lösen muss",
    "pains": [
      "Weinkarte mit Anspruch gestalten: Ausgewogenheit von Regionen, Rebsorten, Preisen, Gläsern und Jahrgängen pro Weingut",
      "Weinbegleitungen mit wissenschaftlicher Basis für jedes Gericht des Degustationsmenüs und die saisonal wechselnde Karte validieren",
      "Keller mit Rückverfolgbarkeit verwalten: Rotation, Kellerbedingungen, Bestellungen, Verluste durch fehlerhafte Korken",
      "Storytelling jedes Weins standardisieren, damit das Serviceteam es dem Gast professionell kommuniziert",
      "Sich in einem umkämpften Restaurant mit kuratiertem Weinkeller, professionellem Entkorken und Wine-driven-Erlebnis differenzieren",
      "Premium-Kunden mit Verkostungen, Kellerevents und speziellen Weinbegleitungen mit hoher Marge gewinnen"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Sommelier hilft",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Agent spezialisiert auf professionelle Sommellerie: Weinkeller, Rebsorten, Regionen, Entkorkungstechnik und Weinservice."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Weinbegleitungen mit wissenschaftlicher Basis für jedes Gericht und jeden Wein: Analyse von Säure, Tanninen, Struktur, Intensität und Harmonie."
      },
      {
        "icon": "BookOpen",
        "title": "Kreativküche + Storytelling",
        "description": "Storytelling jedes Weins für das Serviceteam: Weingut, Terroir, Rebsorte, Vinifikation, Verkostungsnotizen."
      },
      {
        "icon": "Calculator",
        "title": "Kellerkalkulation",
        "description": "Echte Kosten pro Glas, Food Cost des Weins pro Service, Verluste durch fehlerhafte Korken und Kartenvorschläge mit validierter Marge."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bodega",
        "description": "Vorlagen: Kellerkontrolle (Luftfeuchtigkeit, Temperatur), Rotation, Entkorken des Tages, Team-Schulung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Keller",
        "description": "Rückverfolgbarkeit von Weinen, Lagerung, fehlerhafte Korken und Serviertemperaturen pro Typ."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Verkostungen und Kellerevents: Weinbegleitungen mit Degustationsmenü, Lancierungen, Weinmessen, Weihnachten, private Events."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Wine-driven KI-Referenzfotografie + Instagram mit Keller-Storytelling zur Gewinnung von Premium-Kunden."
      },
      {
        "icon": "BarChart3",
        "title": "Lebensmittelabfälle AI",
        "description": "Präzise Daten zu Verlusten bei fehlerhaften Korken, zerbrochenem Glas und Wein am Tisch."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Sommeliers mit AI Chef Pro",
    "workflow": [
      "11:00 · Öffnung — Checkliste Kit de Tareas Bodega: Kellerkontrolle (12-14 °C, 70 % Luftfeuchtigkeit), Bestellprüfung, Rotation der Weine des Tages.",
      "12:00 · Bar & Lounge AI+ — Sie aktualisieren die Karte mit zwei neuen Referenzen (roter Burgunder und deutscher Riesling). Rezept + Storytelling generiert.",
      "13:00 · Food Pairing AI — Sie validieren die Weinbegleitung des neuen Rieslings mit einem fermentierten Fischgericht des Degustationsmenüs. Analyse von Säure und Harmonie.",
      "14:00 · Kit de Escandallos Pro — Sie kalkulieren die beiden neuen Referenzen mit echter Marge pro Glas und pro Flasche, validieren den empfohlenen Preis.",
      "15:00 · Briefing für das Team — Erklärung der beiden neuen Referenzen mit Storytelling und validierten Weinbegleitungen.",
      "17:00 · Private Verkostung für VIP-Kunden — Auswahl von fünf Weinen mit Ad-hoc-Weinbegleitungen, professionelles Entkorken, Dekantieren wenn angebracht.",
      "20:00 · Abendservice — Koordination mit Maître und Küche, Empfehlungen pro Tisch, Gueridon wenn angebracht.",
      "23:00 · Abschluss — Aktualisierung des Bestands, GastroIMG Gen+ generiert ein Referenzbild des neuen Burgunders + InstaFlow plant den Post."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Sommeliers",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "pro-prompts-ebook",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Bar & Lounge AI+ + Food Pairing AI haben mein Angebot verändert. Jede Weinbegleitung des Degustationsmenüs hat jetzt eine dokumentierte wissenschaftliche Basis, die das Serviceteam dem Gast professionell kommuniziert. Die Kellerverwaltung mit Kalkulation pro Glas hat unsere Weinmarge um 6 Punkte gesteigert. Private Verkostungen für VIPs werden in einem Anruf mit professionellem Vorschlag abgeschlossen.",
    "testimonialAuthor": "Eduardo Lara",
    "testimonialRole": "Head Sommelier, Restaurant mit 1 Michelin-Stern",
    "faqTitle": "Häufige Fragen von Sommeliers",
    "faqs": [
      {
        "q": "Gilt das für Fine-Dining-Sommeliers, gastronomische Restaurants, Weinhandlungen oder Hotels?",
        "a": "Für alle vier. Bar & Lounge AI+ deckt vom Sommelier im Premium-Restaurant bis zum Head Sommelier eines Michelin-Restaurants, einer Weinhandlung mit kuratiertem Keller oder einem Hotel mit mehreren Outlets ab."
      },
      {
        "q": "Wie hilft es mir bei wissenschaftlichen Weinbegleitungen?",
        "a": "Food Pairing AI argumentiert mit wissenschaftlicher Basis: Analyse von Säure, Tanninen, Struktur, Intensität, Harmonie und Kontrast. Es untermauert jede Weinbegleitung, damit das Serviceteam sie professionell kommuniziert."
      },
      {
        "q": "Wie verwalte ich die Kalkulation und Marge pro Glas?",
        "a": "Kit de Escandallos Pro berechnet die Marge pro Glas und pro Flasche neu, wenn Sie die Kellerpreise aktualisieren. Lebensmittelabfälle AI fügt die Kosten für fehlerhafte Korken und Verluste im Service hinzu."
      },
      {
        "q": "Generiert es wine-driven visuellen Content für Instagram?",
        "a": "Ja. GastroIMG Gen+ generiert professionelle Referenzbilder von Gläsern, Dekantieren und Keller für Instagram, Web und die Gewinnung von Premium-Kunden. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz; das endgültige Foto machen Sie selbst mit Ihrem echten Glas."
      },
      {
        "q": "Wie hilft es mir bei privaten Verkostungen und Kellerevents?",
        "a": "Gastro Calendar plant private Verkostungen, Kellerevents, Weinmessen, saisonale Lancierungen und Weinbegleitungen mit Degustationsmenüs."
      }
    ],
    "ctaTitle": "Ihr Weinkeller mit professionellem Anspruch und wissenschaftlichen Weinbegleitungen.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Sommeliers: Weinkeller, Weinbegleitungen und professionelle Verkostungen | AI Chef Pro",
      "description": "KI-Suite für professionelle Sommeliers: Bar & Lounge AI+, Food Pairing AI, Kalkulation pro Glas, private Verkostungen und wine-driven Branding. Starten Sie noch heute.",
      "keywords": "KI Sommelier, Software Sommelier, KI Weinbegleitungen, KI Kellerverwaltung, Weinkalkulation, Head Sommelier, private Verkostung KI",
      "ogImage": "https://aichef.pro/og/use-cases/sommelier.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Weinkeller personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational-Onboarding, bei dem Sie erzählen, welche Art von Sommelier Sie sind (Head Sommelier im Fine Dining, freiberuflicher Sommelier, Weinkellerleiter, Hotel-Sommelier, Ausbilder), Größe des Weinkellers, Stadt und Spezialgebiet. Jeder Agent antwortet angepasst an Ihren Weinkeller und Ihren realen Betrieb.",
    "appsTitle": "Die KI-Agenten, die Sie als Sommelier nutzen werden",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Agent spezialisiert auf professionelle Sommellerie: Weinkeller, Rebsorten, Regionen, Technik."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Weinbegleitungen mit wissenschaftlicher Basis: Säure, Tannine, Struktur, Intensität und Harmonie."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Storytelling jedes Weins: Terroir, Vinifikation, Verkostungsnotizen für das Serviceteam."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Verluste durch fehlerhafte Korken, zerbrochenes Glas und Wein am Tisch, integriert in die Kalkulation."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Identifizierung von Sulfiten in Weinen für Kunden mit Empfindlichkeiten."
      },
      {
        "name": "Gastro Lexikum",
        "category": "Gastro-Wissen",
        "description": "Tutor für technische Definitionen: Önologie, Vinifikation, Terroir, Bezeichnungen."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Wine-driven KI-Referenzfotografie für Instagram, Web und Events."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit wine-driven Redaktionskalender zur Gewinnung von Premium-Kunden."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Kunden gewinnen, die in Google und Maps nach Weinhandlung, Verkostung oder Sommelier suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Private Verkostungen, Weinmessen, Lancierungen, Weihnachten, Kellerevents."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und soziale Medien",
        "description": "SEO-Artikel über Weinbegleitungen, Rebsorten und Weingüter zur Gewinnung von organischem Traffic."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Tiefenrecherche über aufstrebende Weingüter, Terroirs, Jahrgänge und Trends."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "Marge nach Kellerkalkulation"
      },
      {
        "value": "×2",
        "label": "Geschwindigkeit der Verkostungsvorschläge"
      },
      {
        "value": "×3",
        "label": "Engagement auf Instagram wine-driven"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihren Weinkeller"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Empfohlene Weinbegleitungen ohne dokumentierte wissenschaftliche Basis",
        "Weinkarte ohne Kalkulation pro Glas und echte Marge",
        "Keller in Tabellen verwaltet, ohne Rückverfolgbarkeit und klare Rotation",
        "Improvisiertes Wein-Storytelling, Serviceteam ohne ständige Schulung",
        "Private Verkostungen manuell abgeschlossen, langsamer Vorschlag"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Weinbegleitungen mit wissenschaftlicher Basis von Food Pairing AI",
        "Kalkulation pro Glas mit in Echtzeit validierter Marge",
        "Keller mit APPCC-Rückverfolgbarkeit und dokumentierter Rotation",
        "Tägliches Briefing für das Team mit Storytelling und Weinbegleitungen",
        "Private Verkostungen in einem Tag abgeschlossen mit wine-driven Vorschlag"
      ]
    },
    "galleryTitle": "So funktioniert der Weinkeller eines Sommeliers",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Keller, Dekantieren, Glas, Verkostung und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-sommelier-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-decanting.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-copa.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-cellar.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-team.jpg"
    ]
  },
  "maestro-asador": {
    "h1": "KI für Grillmeister und Parrillero",
    "heroSubtitle": "Meistern Sie Gluttechnik, Zerlegung und Dry-Aged mit professioneller Kalkulation pro Cut, planen Sie die Proteinproduktion und erfassen Sie Fire-Driven-Branding mit einer Suite spezialisierter gastronomischer KI-Agenten für professionelles Feuerkochen.",
    "heroTagline": "Glut mit authentischer Technik und echter Marge",
    "badge": "Für Grillmeister, Parrilleros und Grillmasters",
    "painsTitle": "Was ein Grillmeister unbedingt lösen muss",
    "pains": [
      "Garpunkt und Gluttechnik Schicht für Schicht standardisieren (Holzkohle, Holz, Marmorierung, Kerntemperatur)",
      "Präzise Zerlegung mit Kosten pro Kilo und Ertrag pro Cut (Chuletón, Picanha, T-Bone, Lomo)",
      "Dry-Aged-Management mit Kammer, Feuchtigkeit, Temperatur, Rotation und dokumentiertem Wochenschwund",
      "Grill und Hauptküche in Service-Spitzen koordinieren, ohne Qualität oder Timing zu verlieren",
      "Storytelling über Viehzüchter-Lieferanten, Rasse, Fütterung und Reifung für den Service",
      "Team aus Junior-Parrilleros mit technischer Kriterien und Konsistenz im Garpunkt ausbilden"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Grillmeister hilft",
    "features": [
      {
        "icon": "Flame",
        "title": "Kreativküche",
        "description": "Für die technische Entwicklung von Signature-Cuts, Marinaden, Saucen und Beilagen des Asador."
      },
      {
        "icon": "UtensilsCrossed",
        "title": "Argentinische + Brasilianische Küche",
        "description": "Spezialisierte Rezeptsammlungen: Parrilla, Chimichurri, Picanha, Churrasco, authentische Technik."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Cut mit Dry-Aged",
        "description": "Rezept + CSV-Kalkulation mit integriertem Dry-Aged-Schwund und Grill-Stundenkosten. Echte Marge pro Cut."
      },
      {
        "icon": "BarChart3",
        "title": "Lebensmittelabfälle AI",
        "description": "Daten pro Prozess: Zerlegung, wöchentliches Dry-Aging, Trimmen, Garverlust."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Vorlagen: Glut anzünden, Zerlegung, Dry-Aged-Kammer-Kontrolle, Mise, Abschluss."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Asador",
        "description": "Rückverfolgbarkeit von Fleisch, Dry-Aging, Kerntemperatur und Konservierung."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Pairings mit kräftigen Rotweinen für die neuen Signature-Cuts."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Vatertag, Weihnachten, Firmenevents und saisonale Lancierungen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Premium-KI-Referenzfotografie + Instagram mit Storytelling über den Viehzüchter-Lieferanten."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Grillmeisters mit AI Chef Pro",
    "workflow": [
      "09:00 · Eröffnung — Checkliste Kit de Tareas: kontrolliertes Anzünden der Glut (3 Stunden bis zum richtigen Punkt), Kontrolle der Dry-Aged-Kammer.",
      "11:00 · Kreativküche + Argentinische Küche — Sie entwickeln einen neuen Signature-Cut aus 60 Tage gereiftem galicischem Chuletón mit geräuchertem Maldon-Salz und Chimichurri. Rezept + CSV-Kalkulation.",
      "12:00 · Kit de Escandallos Pro — Sie laden das CSV mit Ihren realen Fleischpreisen und dem Dry-Aged-Schwund hoch und validieren die echte Marge pro Cut.",
      "13:00 · Mittagsservice — Grill auf Hochtouren mit Premium-Cuts, Chimichurri-Mise und Beilagen.",
      "17:00 · Briefing ans Team — Schulung der Junior-Parrilleros mit technischer Kriterien zum Garpunkt.",
      "20:00 · Abendservice — koordinierte Spitzenzeiten, Grill mit mehreren gleichzeitigen Cuts.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — Sie generieren das Referenzbild des neuen Chuletóns und die Instagram-Posts.",
      "00:00 · Abschluss — gründliche Reinigung der Grills, APPCC unterschrieben, Kontrolle der Dry-Aged-Kammer."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Grillmeister",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Argentinische Küche + Kreativküche haben mein Niveau angehoben. Mein Team reproduziert jetzt den Garpunkt mit dokumentierter technischer Kriterien, die Kalkulationen der Premium-Cuts spiegeln den Schwund des Dry-Aged wider und wir steigern die Marge um 5 Punkte. Die Planung des Vatertags mit Gastro Calendar hat unseren Umsatz verdreifacht.",
    "testimonialAuthor": "Pedro Aguirre",
    "testimonialRole": "Grillmeister, Premium-Asador mit Dry-Aged",
    "faqTitle": "Häufige Fragen von Grillmeistern",
    "faqs": [
      {
        "q": "Funktioniert das für argentinische Parrilla, Churrascaria, Premium-Asador oder Steakhouse?",
        "a": "Für alle vier. Argentinische Küche + Brasilianische Küche + Kreativküche decken von traditioneller Parrilla bis Steakhouse mit Dry-Aged ab."
      },
      {
        "q": "Deckt es Dry-Aged und Kammer-Management ab?",
        "a": "Ja. Es denkt wie ein professioneller Grillmeister: Kammerbedingungen, Zeiten pro Cut, wöchentliche Schwundkontrolle und Rotation."
      },
      {
        "q": "Wie verwalte ich die volatilen Fleischkosten?",
        "a": "Kit de Escandallos Pro berechnet die Marge sofort neu. Lebensmittelabfälle AI addiert die Schwundkosten durch Dry-Aging, Zerlegung und Trimmen."
      },
      {
        "q": "Generiert es visuelle Inhalte für Instagram?",
        "a": "Ja. GastroIMG Gen+ erzeugt professionelle Referenzbilder von Cuts und Glut. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie mit Ihrem echten Cut."
      },
      {
        "q": "Wie hilft es mir bei Firmenevents?",
        "a": "Gastro Calendar plant Vatertag, Weihnachten, Firmenevents und saisonale Cut-Lancierungen."
      }
    ],
    "ctaTitle": "Ihr Grill mit Feuertechnik und echter Marge.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Grillmeister und Parrillero: Cuts, Glut und Dry-Aged | AI Chef Pro",
      "description": "KI-Suite für Grillmeister: Argentinische + Brasilianische Küche, Kalkulation pro Cut, Dry-Aged, Branding und APPCC. Starten Sie heute.",
      "keywords": "KI Grillmeister, KI Parrillero, Software Asador, Kalkulation Chuletón, Dry-Aged, Gluttechnik, argentinische Parrilla KI",
      "ogImage": "https://aichef.pro/og/use-cases/maestro-asador-parrillero.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Grill personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding, bei dem Sie erzählen, welche Art von Grill Sie führen (argentinische Parrilla, brasilianische Churrascaria, Premium-Steakhouse mit Dry-Aged, Casual-Asador im Viertel), Teamgröße, Stadt und Spezialität. Jeder Agent antwortet angepasst an Ihren Grill und Ihren realen Betrieb.",
    "appsTitle": "Die KI-Agenten, die Sie als Grillmeister nutzen werden",
    "apps": [
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Cuts mit Gluttechnik und Beilagen."
      },
      {
        "name": "Argentinische Küche",
        "category": "Lateinamerikanische Rezepte",
        "description": "Asado, Chimichurri, Mollejas und authentische Parrilla-Technik."
      },
      {
        "name": "Brasilianische Küche",
        "category": "Lateinamerikanische Rezepte",
        "description": "Picanha, Churrasco, Farofa und Churrascaria-Technik."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Pairings mit kräftigen Rotweinen und charaktervoller Cocktailkunst."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Für die Bar des Asador mit Premium-Rotweinen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Schwund bei Zerlegung, Dry-Aging, Trimmen und Garen."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Identifizierung pro Cut und Beilage."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Premium-KI-Referenzfotografie für Instagram, Web und Speisekarte."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und Social Media",
        "description": "Instagram mit Fire-Driven-Redaktionskalender."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und Social Media",
        "description": "Kunden gewinnen, die bei Google und Maps nach „Asador in der Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und Social Media",
        "description": "Vatertag, Weihnachten, Firmenevents."
      },
      {
        "name": "Mental Coach",
        "category": "Werkzeuge und Utilities",
        "description": "Coaching für Teamführung und Service-Spitzen."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach Kalkulation der Cuts"
      },
      {
        "value": "×3",
        "label": "Umsatz am Vatertag"
      },
      {
        "value": "−15 %",
        "label": "Schwund bei Zerlegung und Dry-Aging"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihren Grill"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierter Garpunkt zwischen den Parrilleros",
        "Kalkulationen ohne Dry-Aged-Schwund",
        "Dry-Aged-Kammer ohne Rückverfolgbarkeit",
        "Improvisiertes Briefing, variable Schulung",
        "Instagram ohne Storytelling über den Viehzüchter-Lieferanten"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Konsistenter Garpunkt mit technischer Kriterien",
        "Professionelle Kalkulation mit integriertem Dry-Aged-Schwund",
        "Kammer mit dokumentierter APPCC-Rückverfolgbarkeit",
        "Tägliches professionelles Briefing, konstante Schulung",
        "GastroIMG Gen+ + Storytelling über den Viehzüchter-Lieferanten"
      ]
    },
    "galleryTitle": "So funktioniert der Grill eines Grillmeisters",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Glut, Zerlegung, Cuts, Chimichurri und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-tongs.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-cuts.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-fire.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-chimichurri.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-asador-team.jpg"
    ]
  },
  "maestro-heladero": {
    "h1": "KI für Eismeister und Gelatiere",
    "heroSubtitle": "Meistern Sie das technische Gleichgewicht der Grundmischungen, kalkulieren Sie pro Geschmack mit echten Kosten, planen Sie saisonale Produktion und erfassen Sie handwerkliches Branding mit einer Suite gastronomischer KI-Agenten, die auf professionelle Eisherstellung spezialisiert sind.",
    "heroTagline": "Eis mit authentischer Technik und echter Marge",
    "badge": "Für Eismeister, Gelatieri und Eiskunsthandwerker",
    "painsTitle": "Was ein Eismeister unbedingt lösen muss",
    "pains": [
      "Anspruchsvolles technisches Gleichgewicht: Zuckerbalance (Saccharose, Dextrose, Invertzucker), Gesamtfeststoffe und Fette für optimale Textur",
      "Verluste in Eismaschine, Schockfroster und Vitrine bei temperaturempfindlichem Produkt",
      "Extreme Saisonalität: Hochsaison im Sommer, Wintertal, das mit Eistorten und Halbgefrorenem rentabel wird",
      "Standardisierung der Grundmischungsproduktion (weiß, gelb, Frucht, Sorbet) Schicht für Schicht mit technischem Verständnis",
      "Differenzierung in umkämpftem Gebiet mit eigenen Geschmacksrichtungen, Premium-Zutaten (Sosa, Pistazien aus Bronte) und visuellem Branding",
      "Schulung des Teams in professioneller Balance- und Kristallisationstechnik"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Eismeister hilft",
    "features": [
      {
        "icon": "IceCream",
        "title": "Kreative Gelateria",
        "description": "Spezialisierter Agent für professionelle handwerkliche Eisherstellung: weiße, gelbe, Fruchtbasen, Sorbets, technische Zuckerbalance."
      },
      {
        "icon": "Cake",
        "title": "Kreative Patisserie",
        "description": "Für Eistorten, Halbgefrorenes, Löffeldesserts, die das Wintertal rentabel machen."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für die Entwicklung von Signature-Geschmacksrichtungen, kontrollierte Fusionen und Autorenpräsentationen."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Geschmack",
        "description": "Kreative Gelateria liefert Rezept + CSV-Kalkulation mit technischem Gleichgewicht; Kit de Escandallos Pro verwaltet es mit echter Marge pro kg, pro Kugel und pro Hörnchen."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients AI",
        "description": "Sosa-Katalog für professionelle Texturen, Neutralstoffe, Stabilisatoren und konzentrierte Pasten."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Heladería",
        "description": "Vorlagen: Vorbereitung Eismaschine, Schockfrosten, Vitrinenauffüllung, Temperaturkontrolle, Rotation."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Eisdiele",
        "description": "Rückverfolgbarkeit von Milch, frischem Obst, Nüssen und kritischen Temperaturen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Muttertag, Frühling, Sommer, Valentinstag, Eistorten zu Weihnachten."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Handwerkliche KI-Referenzfotografie + Instagram, um lokale Kunden zu gewinnen."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Eismeisters mit AI Chef Pro",
    "workflow": [
      "07:00 · Eröffnung – Checkliste Kit de Tareas: Überprüfung der Kühlung, Schockfrosten der am Vortag vorbereiteten Mischungen.",
      "08:30 · Kreative Gelateria – Sie entwickeln eine neue Signature-Sorte mit Pistazien aus Bronte und Maldon-Salz. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "09:30 · Sosa Ingredients AI – Sie wählen geeignete konzentrierte Paste und Neutralstoffe aus.",
      "10:00 · Kit de Escandallos Pro – Sie laden CSV mit Ihren echten Preisen für Premium-Pistazien und Milch, validieren Marge pro Kugel und pro kg.",
      "11:00 · Tagesproduktion – Sie lassen die Mischungen durch die Eismaschine laufen, schockfrosten auf -18 °C.",
      "13:30 · Auffüllen der Vitrine mit Etiketten und Kontrolle der Ausstellungsverluste.",
      "16:00 · Kreative Patisserie – Sie entwickeln eine Eistorte zum Muttertag mit Pistazien-Halbgefrorenem.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren Referenzbild der neuen Sorte + Posts."
    ],
    "productsTitle": "Vorlagen und empfohlene Kits für Eismeister",
    "productIds": [
      "kit-tareas-heladeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Kreative Gelateria hat unsere Küche verändert. Wir balancieren Zucker und Feststoffe mit technischem Verständnis, die Kalkulationen pro Kugel mit Premium-Pistazien spiegeln echte Marge wider. Kreative Patisserie hat uns die Eistorten eröffnet, die den Winter rentabel machen. Wir sind um 5 Punkte gestiegen.",
    "testimonialAuthor": "Federico Riva",
    "testimonialRole": "Gelatiere-Meister, Premium-Handwerksgelaterie",
    "faqTitle": "Häufige Fragen von Eismeistern",
    "faqs": [
      {
        "q": "Gilt das für italienische Gelateria, handwerkliche Eisdiele oder Kette mit mehreren Standorten?",
        "a": "Für alle drei. Kreative Gelateria denkt wie ein professioneller Eismeister mit dokumentiertem technischem Gleichgewicht."
      },
      {
        "q": "Deckt es Zucker-, Feststoff- und Fettbalance ab?",
        "a": "Ja. Kreative Gelateria denkt wie ein professioneller Eishersteller: Balance mit Saccharose, Dextrose, Invertzucker, Gesamtfeststoffen und Fetten nach technischer Norm."
      },
      {
        "q": "Wie hilft es mir bei der Saisonalität?",
        "a": "Kreative Patisserie eröffnet Eistorten und Halbgefrorenes für das Wintertal; Gastro Calendar plant Spitzenzeiten (Muttertag, Sommer)."
      },
      {
        "q": "Erzeugt es visuellen Content für Instagram?",
        "a": "Ja. GastroIMG Gen+ erzeugt Referenzbilder für Vitrine und soziale Medien. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie mit Ihrer Eistheke und echtem Anrichten."
      },
      {
        "q": "Wie verwalte ich Verluste in Eismaschine und Vitrine?",
        "a": "Lebensmittelabfälle AI liefert Daten pro Prozess (Eismaschine, Schockfrosten, Ausstellung). Sie werden in die Kalkulation des Kit de Escandallos Pro integriert."
      }
    ],
    "ctaTitle": "Ihr Eis mit authentischer Technik und echter Marge.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "KI für Eismeister und Gelatiere: Grundmischungen, Kalkulationen und Saisonalität | AI Chef Pro",
      "description": "KI-Suite für Eismeister: Kreative Gelateria, technisches Gleichgewicht, Kalkulation pro Geschmack, Branding und APPCC. Starten Sie noch heute.",
      "keywords": "KI Eismeister, KI Gelatiere, Eisdielen-Software, Eiskalkulation, technisches Eisgleichgewicht, Eismaschinen-KI",
      "ogImage": "https://aichef.pro/og/use-cases/maestro-heladero.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Eisdiele zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding, in dem Sie erzählen, welche Art von Eisdiele Sie betreiben (italienische Gelateria, spanische Handwerks-Eisdiele, Eisdiele mit Produktionsstätte), Teamgröße, Stadt und Spezialität.",
    "appsTitle": "Die KI-Agenten, die Sie als Eismeister nutzen werden",
    "apps": [
      {
        "name": "Kreative Gelateria",
        "category": "Kulinarische Kreativität",
        "description": "Spezialisierter Agent für handwerkliche Eisherstellung mit technischem Gleichgewicht."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Eistorten, Halbgefrorenes, Löffeldesserts für das Wintertal."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Geschmacksrichtungen mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Neutralstoffe, Stabilisatoren, konzentrierte Pasten und professionelle Texturen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Verluste in Eismaschine, Schockfroster und Vitrine."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Identifizierung pro Geschmack: Milchprodukte, Nüsse, Gluten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Handwerkliche KI-Referenzfotografie für Vitrine, Web und soziale Medien."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit Redaktionskalender für Autoren-Eisdiele."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Kunden gewinnen, die nach „Eisdiele in meiner Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Muttertag, Sommer, Valentinstag, Eistorten zu Weihnachten."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und soziale Medien",
        "description": "Pinterest erfasst organischen Traffic für Eistorten."
      },
      {
        "name": "Mitarbeiteressen AI",
        "category": "Gastro Profile Pro",
        "description": "Generator für Mitarbeitermenüs für die Produktionsstätte."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach Kalkulation der Geschmacksrichtungen"
      },
      {
        "value": "−40 %",
        "label": "Verluste in Produktion und Vitrine"
      },
      {
        "value": "×3",
        "label": "Instagram-Engagement"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Produktionsstätte"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierte Grundmischungen, inkonsistentes Gleichgewicht von Schicht zu Schicht",
        "Kalkulationen ohne dokumentiertes technisches Gleichgewicht",
        "Verluste ohne Rückverfolgbarkeit pro Prozess",
        "Reaktive Saisonalität im Wintertal",
        "Improvisierte Vitrine und soziale Medien"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Grundmischungen mit dokumentiertem technischem Gleichgewicht",
        "Professionelle Kalkulationen pro Kugel und pro kg",
        "Kontrollierte Verluste mit Lebensmittelabfälle AI",
        "Eistorten und Halbgefrorenes machen den Winter rentabel",
        "GastroIMG Gen+ + InstaFlow + Pinterest Pins Gen"
      ]
    },
    "galleryTitle": "So funktioniert die Produktionsstätte eines Eismeisters",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Eismaschine, Grundmischungen, Spatel, Obst und Ausrüstung. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-mantecadora.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-bases.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-spatula.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-fruta.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-team.jpg"
    ]
  },
  "repostero-pastelero": {
    "h1": "KI für Konditoren und Patissiers",
    "heroSubtitle": "Meistern Sie professionelle Patisserie-Technik, kalkulieren Sie jedes Stück mit Backstuben-Stundensatz, planen Sie saisonale Produktion und fangen Sie handwerkliches Branding mit einer Suite von gastronomischen KI-Agenten ein, die auf Konditorei und Patisserie mit eigener Handschrift spezialisiert sind.",
    "heroTagline": "Patisserie mit authentischer Technik und echter Marge",
    "badge": "Für Konditoren, Patissiers und Chef pâtissiers",
    "painsTitle": "Was ein Konditor unbedingt lösen muss",
    "pains": [
      "Anspruchsvolle Technik: Blätterteig, Mürbeteig und Sablée, Biskuits, Ganachen, Glasuren, Mousses mit präziser Balance",
      "Hohe Verluste in der Backstube (Formen, Backen, Dekoration), die ohne Kontrolle die Rentabilität schmälern",
      "Signature-Stücke Schicht für Schicht mit professioneller Konsistenz standardisieren",
      "Sehr starke Saisonalität: Dreikönigskuchen, Ostern, Valentinstag, Weihnachten konzentrieren einen hohen Prozentsatz des Jahres",
      "Sich mit Patisserie mit eigener Handschrift, Premium-Präsentation und Storytelling französischer oder moderner Technik abheben",
      "Aufträge für maßgeschneiderte Torten, private Events und Hochzeiten mit Marge gewinnen, während man die tägliche Konditorei managt"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Konditor hilft",
    "features": [
      {
        "icon": "Cake",
        "title": "Kreative Patisserie",
        "description": "Agent spezialisiert auf professionelle Patisserie, Restaurantdesserts, maßgeschneiderte Torten und Gebäck mit fortgeschrittener Technik."
      },
      {
        "icon": "Cookie",
        "title": "Kreative Schokolade",
        "description": "Für fortgeschrittene Kombinationen aus Patisserie und Schokolade: Ganachen, Cremoso, Glasuren."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für die Entwicklung von Signature-Desserts und Geschmackskombinationen mit technischem Anspruch."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulationen mit Backstuben-Stundensatz",
        "description": "Kreative Patisserie liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet sie mit integriertem Backstuben-Stundensatz in der echten Marge pro Stück."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients AI",
        "description": "Sosa-Katalog für Texturen, Geliermittel, Neutrale und fortgeschrittene Technik."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pastelería",
        "description": "Vorlagen: Teigvorbereitung, Produktion, Formen, Backen, Dekoration, Vitrine, Konservierung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Konditorei",
        "description": "Rückverfolgbarkeit von Ei, Cremes, Nüssen und professioneller Konservierung."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Dreikönigskuchen, Valentinstag, Ostern, Weihnachten, Kommunionen, Muttertag."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Handwerkliche KI-Referenzfotografie + Pinterest, wo Patisserie stabilen organischen Traffic einfängt."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Konditors mit AI Chef Pro",
    "workflow": [
      "06:00 · Eröffnung — Checkliste Kit de Tareas Pastelería: Sauerteig auffrischen, Kuchen schlagen, Cremes vorbereiten.",
      "08:00 · Kreative Patisserie — Sie entwickeln ein neues Dessert für den Valentinstag. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "09:00 · Kit de Escandallos Pro — Sie laden die CSV mit Ihren echten Preisen und Backstuben-Stundensatz hoch und validieren die Marge pro Stück.",
      "11:00 · Tagesproduktion — Formen, Backen, Dekoration mit spezifischen Vorlagen.",
      "14:00 · Vitrine mit Etiketten und Preisen auffüllen.",
      "16:00 · Gastro Calendar — Sie bereiten die Planung für den Dreikönigskuchen 8 Wochen im Voraus vor.",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — Sie generieren ein Referenzbild des neuen Desserts + Pins.",
      "20:00 · Abschluss — gründliche Reinigung, APPCC unterschrieben, Planung für den nächsten Tag."
    ],
    "productsTitle": "Vorlagen und empfohlene Kits für Konditoren",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Kreative Patisserie + Sosa Ingredients AI haben mein Angebot verändert. Meine Signature-Desserts haben jetzt dokumentierte Technik, die mein Team konsistent repliziert, die Kalkulationen mit Backstuben-Stundensatz haben mir 6 Prozentpunkte mehr Marge gebracht, und die Bestellungen für maßgeschneiderte Torten werden in einem Anruf mit professionellem Angebot abgeschlossen.",
    "testimonialAuthor": "Eva Mata",
    "testimonialRole": "Chef pâtissière, Konditorei mit eigener Handschrift",
    "faqTitle": "Häufige Fragen von Konditoren",
    "faqs": [
      {
        "q": "Funktioniert das für Restaurantkonditoren, handwerkliche Patissiers oder Hotel-Chef pâtissiers?",
        "a": "Für alle drei. Kreative Patisserie deckt von handwerklicher Konditorei bis zur gehobenen Restaurantpatisserie mit fortgeschrittener französischer Technik ab."
      },
      {
        "q": "Deckt es fortgeschrittene Technik ab (Blätterteig, Mousses, Glasuren)?",
        "a": "Ja. Kreative Patisserie denkt wie ein professioneller Chef pâtissier: invertierter Blätterteig, technisch ausgearbeitete Teige, Mousses mit Balance, Glasuren mit technischer Deckkraft."
      },
      {
        "q": "Deckt es Konditorei + Schokolade ab?",
        "a": "Ja. Kreative Schokolade ergänzt mit Pralinen, Ganachen, Pralinés und Temperiertechnik für kombinierte Stücke."
      },
      {
        "q": "Generiert es visuelle Inhalte für Vitrine und soziale Medien?",
        "a": "Ja. GastroIMG Gen+ generiert professionelle Referenzbilder; Pinterest Pins Gen fängt stabilen organischen Traffic ein. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie selbst mit Ihrem echten Stück."
      },
      {
        "q": "Wie hilft es mir bei Events und Saisons?",
        "a": "Gastro Calendar plant die wichtigsten Saisons (Dreikönigskuchen, Valentinstag, Ostern, Weihnachten, Kommunionen) im Voraus."
      }
    ],
    "ctaTitle": "Ihre Konditorei mit eigener Technik und echter Marge.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliedsplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "KI für Konditoren und Patissiers: Technik, Kalkulationen und Saisonalität | AI Chef Pro",
      "description": "KI-Suite für professionelle Konditoren: Kreative Patisserie, Kalkulationen mit Backstuben-Stundensatz, saisonale Planung und Branding. Starten Sie heute.",
      "keywords": "KI Konditor, KI Patissier, KI Chef pâtissier, Konditorei-Software, Kalkulationen Konditorei, französische Technik, Patisserie mit eigener Handschrift",
      "ogImage": "https://aichef.pro/og/use-cases/repostero-pastelero.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Konditorei zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding, bei dem Sie uns mitteilen, welche Art von Konditorei Sie betreiben (Chef pâtissier im Restaurant, handwerklicher Konditor, Hotelkonditor, Konditorei für Events), Teamgröße, Stadt und Spezialgebiet.",
    "appsTitle": "Die KI-Agenten, die Sie als Konditor nutzen werden",
    "apps": [
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Agent spezialisiert auf professionelle Patisserie mit fortgeschrittener Technik."
      },
      {
        "name": "Kreative Schokolade",
        "category": "Kulinarische Kreativität",
        "description": "Für Pralinen, Ganachen und fortgeschrittene Kombinationen."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Desserts mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Kreative Boulangerie",
        "category": "Kulinarische Kreativität",
        "description": "Für Brioche, Croissants, Ensaimadas und ergänzendes Gebäck."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für Texturen, Geliermittel und fortgeschrittene Technik."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Assistent des tSpoonLab-Katalogs für fortgeschrittene Anwendungen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Verluste in der Backstube, beim Formen, Backen und in der Vitrine."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Identifizierung pro Stück: Gluten, Milchprodukte, Nüsse, Ei."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Handwerkliche KI-Referenzfotografie für Vitrine, Web und soziale Medien."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit Redaktionskalender für Patisserie mit eigener Handschrift."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und soziale Medien",
        "description": "Pinterest fängt stabilen organischen Traffic für Torten und Desserts ein."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Dreikönigskuchen, Valentinstag, Ostern, Weihnachten, Muttertag."
      }
    ],
    "metrics": [
      {
        "value": "+6 PP",
        "label": "Marge nach Kalkulation der Stücke"
      },
      {
        "value": "−30 %",
        "label": "Verluste in der Backstube"
      },
      {
        "value": "×2",
        "label": "organischer Traffic über Pinterest"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Backstube"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierte Technik, inkonsistente Signature-Desserts",
        "Kalkulationen ohne Backstuben-Stundensatz",
        "Verluste in der Backstube ohne echte Rückverfolgbarkeit",
        "Vitrine und soziale Medien improvisiert mit Handyfotos",
        "Reaktive Saisonalität, Sie kommen zu spät zum Dreikönigskuchen"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Dokumentierte Technik, konsistente Signature-Desserts",
        "Professionelle Kalkulation mit integriertem Backstuben-Stundensatz",
        "Verluste kontrolliert mit Lebensmittelabfälle AI",
        "GastroIMG Gen+ + Pinterest Pins Gen fangen stabilen Traffic ein",
        "Dreikönigskuchen und Saisons 8 Wochen im Voraus geplant"
      ]
    },
    "galleryTitle": "So funktioniert die Backstube eines Konditors",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Spritzen, Torten, Mise en Place, Vitrine und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-repostero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-repostero-decoration.jpg",
      "/lovable-uploads/ai-gallery/use-case-repostero-tartas.jpg",
      "/lovable-uploads/ai-gallery/use-case-repostero-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-repostero-vitrina.jpg",
      "/lovable-uploads/ai-gallery/use-case-repostero-team.jpg"
    ]
  },
  "restaurante-casual": {
    "h1": "KI für Casual-Restaurants",
    "heroSubtitle": "Optimieren Sie den täglichen Betrieb, kontrollieren Sie den Food Cost und gewinnen Sie Stunden an Bürokratie zurück – mit einer Suite spezialisierter KI-Agenten für die Gastronomie in Ihrem Casual-Restaurant.",
    "heroTagline": "Das moderne Casual-Restaurant braucht KI",
    "badge": "Für Casual-Restaurants und Bistros",
    "painsTitle": "Was ein Casual-Restaurant unbedingt lösen muss",
    "pains": [
      "Geringe Marge, die eine millimetergenaue Kontrolle von Kosten und Lebensmittelabfällen in der Küche erfordert",
      "Hohe Personalfluktuation: Die Einarbeitung und Betreuung neuer Köche und Servicekräfte kostet jede Woche Stunden",
      "Umfangreiche Speisekarte mit vielen Gerichten, die kalkuliert werden müssen, wenn sich die Lieferantenpreise ändern",
      "HACCP und Vorschriften immer aktuell, ohne dass Papierkram dem Service wertvolle Zeit raubt",
      "Kunden in einem umkämpften Gebiet gewinnen: lokale SEO, Social Media und Bewertungen sind entscheidend",
      "Küche, Service und Lieferung in den Stoßzeiten ohne Reibungsverluste koordinieren"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem Casual-Restaurant hilft",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Casual Restaurants AI+",
        "description": "Spezialisierter Agent für Bistros, Gastrobars, Tapas und mediterrane Küche: das komplette Casual-Spektrum mit professioneller Basis."
      },
      {
        "icon": "Calculator",
        "title": "Professionelle Rezeptkalkulation",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; das Kit de Escandallos Pro verwaltet sie mit Ihren tatsächlichen Preisen und der Zielmarge."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Fertige Vorlagen: Schichtbeginn, Schichtende, Küchenstationen, Service, Lieferung und Events."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP und Rückverfolgbarkeit",
        "description": "Pack APPCC mit 19 Vorlagen, mobilen Erfassungen, Warnmeldungen und druckfertigen A4-Blättern für die Inspektion."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Dienstpläne in Minuten unter Berücksichtigung von Tarifvertrag, Pausen, Arbeitszeiterfassung und Produktivitätskennzahlen."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Lokale SEO-Suite, um Kunden organisch zu gewinnen, ohne eine Agentur zu bezahlen."
      },
      {
        "icon": "BarChart3",
        "title": "Kit Plan Financiero",
        "description": "Dashboard mit Kennzahlen, Food Cost, Produktivität und durchschnittlichem Bon. Reporting an den Eigentümer als PDF."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "KI-gestützte Food-Fotografie für Web und Social Media, Inhalte für Instagram mit Redaktionskalender."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Lokale Keyword-Recherche für Gastronomie nach Postleitzahlgebiet für echte Rankings."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem Casual-Restaurant mit AI Chef Pro",
    "workflow": [
      "08:30 · Eröffnung – Checkliste des Kit de Tareas Restaurante Casual und Inventurkontrolle in 10 Minuten.",
      "10:00 · Casual Restaurants AI+ – Sie bitten den Agenten um Vorschläge für das Tagesgericht mit Produkten, die Sie auf Lager haben.",
      "10:30 · Kreativküche + Kit de Escandallos Pro – Sie kalkulieren das Tagesgericht mit Ihren Preisen und prüfen die Marge.",
      "12:30 · Mittagsservice – Küche, Service und Lieferung mit Vorlagen koordiniert. Lebensmittelabfälle werden vom Handy aus mit HACCP erfasst.",
      "15:30 · Kit Plan Financiero – Sie prüfen die KPIs des Vortags und stellen fest, dass der Food Cost am Montag auf 32 % gestiegen ist. Sie identifizieren die Ursache.",
      "17:00 · MenuDish Local SEO – Sie aktualisieren die Beschreibungen der 6 Top-Gerichte in Google Business und auf der Website.",
      "18:00 · Kit Inventario – Sie prüfen Lieferantenbestellungen mit Preisvergleich und Mindestbestandswarnungen.",
      "23:30 · Abschluss – HACCP unterschrieben, Tagesbericht an den Eigentümer als PDF direkt aus dem Kit Plan Financiero."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Casual-Restaurants",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Wir haben 80 Plätze und eine hohe Personalfluktuation. Das Kit de Tareas Restaurante Casual und das Pack APPCC haben unsere gesamte Abläufe strukturiert. Wir laufen wie ein Schweizer Uhrwerk und der Food Cost ist im ersten Quartal um 3 Prozentpunkte gesunken – allein durch sorgfältige Rezeptkalkulation.",
    "testimonialAuthor": "Sandra López",
    "testimonialRole": "Geschäftsführer eines mediterranen Casual-Restaurants mit 80 Plätzen",
    "faqTitle": "Häufig gestellte Fragen für Casual-Restaurants",
    "faqs": [
      {
        "q": "Funktioniert es für Restaurants mit 30, 80 oder 150 Plätzen?",
        "a": "Ja. Die Vorlagen skalieren mit dem Volumen und die Pläne passen sich der tatsächlichen Nutzung an. Es gibt Kunden von 30 Plätzen bis hin zu Ketten mit 25 Standorten."
      },
      {
        "q": "Deckt es neben dem Service auch Lieferung ab?",
        "a": "Ja. Das Kit de Tareas Restaurante Casual enthält spezifische Vorlagen für das Liefermanagement, die damit verbundenen Lebensmittelabfälle und die Koordination mit Plattformen wie Glovo, Uber Eats und Just Eat."
      },
      {
        "q": "Ersetzt es mein Kassensystem oder meine Reservierungssoftware?",
        "a": "Nein, es ergänzt. Cover Manager oder The Fork verwalten Reservierungen und das Kassensystem den Verkauf; AI Chef Pro verwaltet Kosten, Personal, HACCP, Inventar und lokales SEO. Die Daten sind über Excel kompatibel."
      },
      {
        "q": "Wie lange braucht das Team, um es zu lernen?",
        "a": "Die tatsächliche Lernkurve beträgt 1-2 Tage. Es gibt ein 5-minütiges Onboarding-Video, WhatsApp-Support und alles beginnt mit dem Agenten «Wer sind Sie?», der das System in 2 Minuten an Ihr Restaurant anpasst."
      },
      {
        "q": "Wie hilft es mir bei lokalem SEO und der Kundengewinnung?",
        "a": "Content- und Social-Media-Suite: MenuDish Local SEO (Gerichtbeschreibungen), BlogPost SEO Gen+ (Blogbeiträge), Keyword Discovery AI+ (Keywords nach Postleitzahlgebiet), InstaFlow AI Pro (Instagram) und Pinterest Pins Gen."
      },
      {
        "q": "Gibt es einen spezifischen Agenten für meinen Casual-Restaurant-Typ?",
        "a": "Ja. Casual Restaurants AI+ deckt Bistros, Gastrobars, Tapas, mediterrane Küche, Wirtshäuser und Casual-Grill ab. Für spezifischere Konzepte gibt es Burger Pro AI+, Food Truck AI+ und länderspezifische Agenten (mexikanisch, peruanisch, japanisch usw.)."
      }
    ],
    "ctaTitle": "Bringen Sie Ordnung in Ihr Casual-Restaurant.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliedsplan für 10 € pro Monat mit 10.000 Credits, um alle Agenten zu nutzen.",
    "seo": {
      "title": "KI für Casual-Restaurants: Abläufe, Rezeptkalkulation und lokales SEO | AI Chef Pro",
      "description": "KI-Suite für Casual-Restaurants und Bistros: spezialisierte Agenten, Rezeptkalkulation, HACCP, Dienstpläne, lokales SEO und professionelles Marketing. Starten Sie noch heute.",
      "keywords": "KI Casual-Restaurant, Software Casual-Restaurant, Bistro-Management KI, Rezeptkalkulation Casual, HACCP Casual-Restaurant, Marketing Casual-Restaurant KI, lokales SEO Restaurant, Casual-Restaurant Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-casual.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Restaurant zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten «Wer sind Sie?», einem 2-minütigen konversationellen Onboarding, bei dem Sie uns mitteilen, welche Art von Casual-Restaurant Sie betreiben (mediterran, Bistro, Gastrobar, Wirtshaus, Tapas), wie viele Plätze, in welcher Stadt und wie Sie arbeiten. Von diesem Moment an antwortet jeder Agent – von Casual Restaurants AI+ bis MenuDish Local SEO – angepasst an Ihren Kontext: durchschnittlicher Bon in Ihrer Region, Vorschriften und reale Abläufe.",
    "appsTitle": "Die KI-Agenten für Ihr Casual-Restaurant",
    "apps": [
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Hauptagent: Bistros, Gastrobars, Tapas und mediterrane Küche mit professioneller Basis."
      },
      {
        "name": "Profi Restaurantmanager",
        "category": "Gastro Profile Pro",
        "description": "Operativer Assistent und Reporting an den Eigentümer."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Professionelle Gerichtentwicklung mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Präzise Daten zu Lebensmittelabfällen und Ausbeuten für die Küchenkontrolle."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Allergenerkennung pro Rezept und Gericht."
      },
      {
        "name": "Mitarbeiteressen AI",
        "category": "Gastro Profile Pro",
        "description": "Generator für Mitarbeitermenüs mit Produkten, die Sie bereits auf Lager haben."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content und Social Media",
        "description": "Für lokales SEO optimierte Gerichtbeschreibungen."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content und Social Media",
        "description": "Blogbeiträge, um lokalen organischen Traffic zu gewinnen."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Content und Social Media",
        "description": "Gastronomie-Keywords nach Postleitzahlgebiet."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content und Social Media",
        "description": "Virale Inhalte für Instagram mit Redaktionskalender."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Food-Fotografie für Web und Social Media."
      },
      {
        "name": "Mental Coach",
        "category": "Tools und Utilities",
        "description": "Coaching für Stressbewältigung unter hohem Druck und schwierige Gespräche."
      }
    ],
    "metrics": [
      {
        "value": "-3 pp",
        "label": "Food Cost im ersten Quartal"
      },
      {
        "value": "×2",
        "label": "Buchungen über lokales SEO"
      },
      {
        "value": "-6 h",
        "label": "pro Woche bei der Verwaltung"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihr Restaurant"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Abläufe auf losen Zetteln, jede Station macht es anders",
        "HACCP auf Papier, das vor der Inspektion verloren geht",
        "Stundenlang manuelle Dienstpläne in Excel erstellen",
        "Improvisiertes Marketing ohne organische Kundengewinnung",
        "Food Cost nach Augenmaß, ohne zu wissen, welches Gericht die Rentabilität schmälert"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Kit de Tareas mit strukturierten Vorlagen nach Schicht und Station",
        "HACCP vom Handy aus mit Erfassungen, Warnmeldungen und PDF-Export",
        "Dienstpläne in Minuten mit dem Kit Gestión de Personal unter Berücksichtigung des Tarifvertrags",
        "Lokale SEO-Suite, die organische Buchungen ohne Agenturkosten generiert",
        "Food Cost pro Gericht detailliert berechnet mit professioneller Rezeptkalkulation"
      ]
    },
    "galleryTitle": "So funktioniert ein modernes Casual-Restaurant",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Service, offene Küche, Terrasse, Tagesgericht, Team und Theke.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-casual-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-kitchen.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-terrace.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-dish.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-bar.jpg"
    ]
  },
  "cafeteria-brunch": {
    "h1": "KI für Café und Brunch",
    "heroSubtitle": "Optimieren Sie Frühstück, Brunch, Specialty Coffee und Konditorei mit einer Suite von KI-Agenten, die für Coffee Shops, Brunch-Lokale und moderne Cafés entwickelt wurde.",
    "heroTagline": "Moderner Coffee Shop mit modernen Abläufen",
    "badge": "Für Specialty-Cafés und Brunch",
    "painsTitle": "Was ein Coffee Shop oder Brunch-Lokal unbedingt lösen muss",
    "pains": [
      "Kurze Karte, aber extrem hohe Rotation in den Morgen- und Mittagsspitzen",
      "Sehr knappe Marge bei Specialty Coffee und Konditorei mit volatilen Milch- und Kakaokosten",
      "Junges, wechselndes Team, das schnelle Schulung an Bar und Service benötigt",
      "Branding und soziale Medien (Instagram, Pinterest) sind der Haupthebel für die Kundenakquise",
      "Sich in einer umkämpften Gegend mit Premium-Preisen, aber dennoch erschwinglich zu differenzieren",
      "Den Brunch-Andrang am Wochenende bewältigen, ohne den Betrieb unter der Woche zu überlasten"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem Brunch-Café hilft",
    "features": [
      {
        "icon": "Coffee",
        "title": "Casual Restaurants AI+",
        "description": "Agent mit Wissen über Coffee Shops, Brunch und Specialty-Cafés: Karten, Preisgestaltung und Betriebsabläufe."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulationen für Kaffee, Brunch und Gebäck",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet es mit Ihren echten Preisen."
      },
      {
        "icon": "Sparkles",
        "title": "Kreative Patisserie + Kreative Boulangerie",
        "description": "Professionelle Rezepte für Konditorei, Brioche, Croissants, Cakes und handwerkliche Bäckerei."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Cafetería",
        "description": "Spezifische Vorlagen: Eröffnung, Schließung, Bar, leichte Küche, Brunch, Service und Reinigung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Vereinfachtes HACCP",
        "description": "Pack APPCC mit minimalen, aber vollständigen Aufzeichnungen für Cafés: Milch, Lagerung, Reinigung, Temperaturen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "KI-Lebensmittelfotografie + Instagram-Content mit Captions, Redaktionskalender und Planung."
      },
      {
        "icon": "Search",
        "title": "Pinterest Pins Gen",
        "description": "Pinterest ist entscheidend für Coffee Shops: Pins zu Brunch, Latte Art und Konditorei, um organischen Traffic zu gewinnen."
      },
      {
        "icon": "BarChart3",
        "title": "KPIs und durchschnittlicher Bon",
        "description": "Kit Plan Financiero: Auslastungsquote, durchschnittlicher Bon, Produktivität und Upselling bei Brunch und Kaffee."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Lokale gastronomische Keywords für „Brunch [Ihr Viertel]“, „Specialty Coffee in der Nähe“ und Ähnliches."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem Brunch-Café mit AI Chef Pro",
    "workflow": [
      "07:00 · Eröffnung – Checkliste des Kit de Tareas Cafetería: Bar gestartet, gemahlener Kaffee, kalte Milch, Vitrine bereit.",
      "08:00 · Morgenservice – Frühstück und Specialty Coffee mit koordiniertem Ablauf zwischen Bar und leichter Küche.",
      "11:00 · Kreativküche – Sie entwickeln ein neues Brunch-Gericht für Samstag: Toasts mit Burrata, Gravlax und Eiern. Sie erhalten eine CSV-Kalkulation.",
      "11:30 · Kit de Escandallos Pro – Sie laden die CSV mit echten Preisen und validieren die Zielmarge (32 %).",
      "13:00 · Mittagsservice – Brunch läuft, Team koordiniert mit spezifischen Vorlagen.",
      "16:00 · GastroIMG Gen+ + Pinterest Pins Gen – Sie generieren Fotos des neuen Brunchs und für Pinterest optimierte Pins.",
      "17:30 · InstaFlow AI Pro – Sie planen Instagram-Posts für die nächste Woche mit Redaktionskalender.",
      "19:30 · Schließung – gründliche Reinigung, HACCP unterschrieben, Planung der Konditorei für den nächsten Tag."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Cafés",
    "productIds": [
      "kit-tareas-cafeteria",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Wir haben am Wochenende Brunch und unter der Woche Specialty Coffee. Das Kit de Tareas Cafetería und die Content-Erstellung für Instagram haben mir die Nachmittage zurückgegeben. Pinterest Pins Gen war eine Entdeckung: Es hat uns organischen Traffic gebracht, den ich noch nie gesehen hatte.",
    "testimonialAuthor": "Marcos Rivera",
    "testimonialRole": "Inhaber, Specialty-Coffee-Shop und Brunch",
    "faqTitle": "Häufig gestellte Fragen für Coffee Shops",
    "faqs": [
      {
        "q": "Funktioniert es für Specialty Coffee oder nur für Casual-Cafés?",
        "a": "Es funktioniert für beides. Es gibt anpassbare Vorlagen sowohl für Specialty-Coffee-Shops (V60, Single-Origin-Espresso, Latte Art) als auch für Casual-Cafés und Brunch."
      },
      {
        "q": "Funktioniert es für Lokale mit sehr leichter Küche?",
        "a": "Ja. Das Kit de Tareas Cafetería hat spezifische Vorlagen für leichte Küche, Brunch und Bar, ohne anzunehmen, dass Sie eine vollständige Brigade haben."
      },
      {
        "q": "Erzeugt es für Instagram und Pinterest optimierten Content?",
        "a": "Ja. InstaFlow AI Pro und Pinterest Pins Gen sind spezifische Agenten für diese Kanäle. Pinterest funktioniert sehr gut für Brunch und Kaffee mit stabilem organischem Traffic."
      },
      {
        "q": "Deckt es Lieferung und erweiterte Öffnungszeiten ab?",
        "a": "Ja. Die Vorlagen sind anpassbar an Öffnungszeiten, Lieferung, Take-away und leichte Verpflegung (Corporate Coffee Break)."
      },
      {
        "q": "Wie optimiert es das lokale SEO für meinen Coffee Shop?",
        "a": "MenuDish Local SEO + BlogPost SEO Gen+ + Keyword Discovery AI+ arbeiten zusammen, um lokale Suchanfragen wie „Brunch in [Ihrer Gegend]“ oder „bester Specialty Coffee in der Nähe“ abzudecken."
      }
    ],
    "ctaTitle": "Ihr Café mit optimierten Abläufen und organischer Kundenakquise.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Café und Brunch: Abläufe, Pinterest und lokales SEO | AI Chef Pro",
      "description": "KI-Suite für Coffee Shops und Brunch-Lokale: spezialisierte Agenten, Kalkulationen, HACCP, Content für Instagram und Pinterest, lokales SEO. Starten Sie noch heute.",
      "keywords": "KI Café, Brunch Software, KI Coffee Shop, Verwaltung Specialty Café, Kaffeekalkulation, KI Café-Marketing, Pinterest Brunch, lokales SEO Café, Coffee Shop Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/cafeteria-brunch.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Coffee Shop personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten «Wer sind Sie?», einem 2-minütigen Conversational-Onboarding, bei dem Sie erzählen, welche Art von Café Sie betreiben (Specialty, Brunch, Casual), Stadt und Arbeitsweise. Ab diesem Moment antwortet jeder Agent – von Kreative Patisserie bis Pinterest Pins Gen – angepasst an Ihren Kontext: durchschnittlicher Bon Ihrer Region, Kundenprofil und reale Betriebsabläufe.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Café nutzen werden",
    "apps": [
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Hauptagent: Coffee Shops, Brunch und Cafés mit professioneller Basis."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Professionelle Rezepte für Café-Konditorei: Brioche, Croissants, Cakes, Torten."
      },
      {
        "name": "Kreative Boulangerie",
        "category": "Kulinarische Kreativität",
        "description": "Für Coffee Shops, die ihr eigenes Brot und Gebäck mit Sauerteig backen."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Brunch-Gerichten mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Rezept."
      },
      {
        "name": "Mitarbeiteressen AI",
        "category": "Gastro Profile Pro",
        "description": "Generator für Mitarbeitermenüs, die das Team motivieren."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content und soziale Medien",
        "description": "Lokale SEO-Beschreibungen zur Verbesserung des Rankings."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content und soziale Medien",
        "description": "Blogbeiträge, um organischen Traffic zum Coffee Shop zu bringen."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Content und soziale Medien",
        "description": "Keywords nach Postleitzahl: Brunch, Specialty Coffee usw."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content und soziale Medien",
        "description": "Viraler Instagram-Content mit Redaktionskalender."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content und soziale Medien",
        "description": "Für Pinterest optimierte Pins: Brunch, Kaffee, Konditorei."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Lebensmittelfotografie für Web, soziale Medien und Speisekarte."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "organischer Traffic über Pinterest"
      },
      {
        "value": "+ €1,80",
        "label": "durchschnittlicher Bon durch Upselling"
      },
      {
        "value": "−4 h",
        "label": "wöchentlich bei Social-Media-Verwaltung"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihr Café"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierte Bar- und Leichtküchen-Abläufe in jeder Schicht",
        "Kalkulationen nach Gefühl bei Kaffee und Konditorei mit unsicherer Marge",
        "Chaotisches Instagram ohne Redaktionskalender und Kontinuität",
        "Keine Präsenz auf Pinterest, wodurch der organische Traffic verloren geht, der für Brunch am besten konvertiert",
        "HACCP im Notizbuch, das bei der Inspektion vergessen wird"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Kit de Tareas Cafetería mit spezifischen Vorlagen pro Schicht und Bereich",
        "Professionelle Kalkulation für jedes Getränk und Gericht mit echter Marge",
        "InstaFlow AI Pro mit Redaktionskalender und optimierten Captions",
        "Pinterest Pins Gen gewinnt stabilen organischen Traffic mit hoher Konversion",
        "HACCP vom Handy mit inspektionsbereiten Aufzeichnungen"
      ]
    },
    "galleryTitle": "So funktioniert ein modernes Brunch-Café",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Specialty und Brunch, Barista, Konditorei, Schichtteam und Content für soziale Medien.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-cafeteria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-brunch.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-barista.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-pastry.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-instagram.jpg"
    ]
  },
  "pizzeria": {
    "h1": "KI für Ihre Pizzeria",
    "heroSubtitle": "Standardisieren Sie Sauerteig, kalkulieren Sie jede Pizza durch, steuern Sie Lieferservice und Multi-Brand mit einer Suite von KI-Agenten, die auf professionelle Pizzerien, neapolitanische, römische und amerikanische Pizza spezialisiert sind.",
    "heroTagline": "Pizza mit echter Marge, Technik mit System",
    "badge": "Für Pizzerien und Pizzaioli",
    "painsTitle": "Was eine Pizzeria unbedingt lösen muss",
    "pains": [
      "Sehr knappe Marge bei Pizza mit millimetergenauer Kontrolle der Grammatur von Teig, Soße, Käse und Belägen",
      "Lebensmittelabfälle bei Sauerteig, Mozzarella und Soßen, die unkontrolliert die Rentabilität schmälern",
      "Nachfragespitzen im Lieferservice (12:30-14:30, 20:30-22:30) ohne Spielraum für Fehler",
      "Umfangreiche Pizzakarte mit individueller Kalkulation pro Variante",
      "Standardisierung von Teig und Technik in Küchen mit wechselndem Pizzaioli-Team",
      "Gewinnung lokaler Kunden durch SEO und Social Media, um die Abhängigkeit von Lieferplattformen zu reduzieren"
    ],
    "featuresTitle": "Wie AI Chef Pro in einer Pizzeria hilft",
    "features": [
      {
        "icon": "Pizza",
        "title": "Italienische Küche",
        "description": "Spezialisierter Agent für professionelle italienische Küche, Teige, Soßen und Techniken neapolitanischer, römischer und amerikanischer Pizzerien."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Für Sauerteige, lange Fermentationen, hohe Hydratationen und Bäckereitechnik für professionelle Pizza."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Pizza",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; das Kit de Escandallos Pro verwaltet es mit Ihren realen Preisen und Zielmarge pro Variante."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pizzería",
        "description": "Vorlagen: Teighydratation, Soßenvorbereitung, Mise en Place der Beläge, Service vor Ort und Lieferservice."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC",
        "description": "Auf Pizzerien abgestimmte Vorlagen: Ofentemperaturen, Aufbewahrung von Sauerteig, Rückverfolgbarkeit für den Lieferservice."
      },
      {
        "icon": "Truck",
        "title": "Burger Pro AI+ + Food Truck AI+",
        "description": "Wenn Sie eine Multi-Brand-Dark Kitchen betreiben, gibt es auch komplementäre Agenten für spezialisierten Lieferservice."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + InstaFlow AI Pro",
        "description": "Lokales Ranking bei Google und viraler Content für Instagram mit Redaktionskalender."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "KI-Food-Fotografie für Glovo, Uber Eats, Just Eat und die Restaurant-Website."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Dienstpläne für Pizzaioli, Service und Lieferservice mit rotierenden Schichten und Service-Spitzen."
      }
    ],
    "workflowTitle": "Ein echter Tag in einer Pizzeria mit AI Chef Pro",
    "workflow": [
      "08:00 · Eröffnung – Checkliste Kit de Tareas Pizzería: Sauerteig-Hydratation, Vorbereitung der Tomatensauce, Mise en Place der Beläge.",
      "10:00 · Italienische Küche + Fermentus mit AI+ – Sie entwickeln eine neue saisonale Pizza mit einem Teig mit 75 % Hydratation und 48 h Fermentation.",
      "11:00 · Kit de Escandallos Pro – Sie kalkulieren die neue Pizza mit Ihren realen Preisen (Mehl, Mozzarella, Prosciutto) und validieren eine Marge von 32 %.",
      "12:30 · Mittagsservice – Pizzaiolo am Ofen, voller Gastraum, aktiver Lieferservice mit spezifischen Vorlagen.",
      "15:30 · Inventar – Sie validieren Bestellungen von italienischem Mehl, Mozzarella di Bufala und Konserven mit dem Kit Inventario.",
      "17:00 · MenuDish Local SEO – Sie aktualisieren die Beschreibungen der Top-Pizzen in Google Business und auf der Website.",
      "20:00 · Abendservice – Lieferpeak, Pizzaiolo am Ofen, koordiniert mit Gastraum und Fahrern.",
      "23:30 · Schließung – Reinigung, APPCC unterschrieben, Tagesbericht an den Inhaber."
    ],
    "productsTitle": "Vorlagen und Kits zum Download für Pizzerien",
    "productIds": [
      "kit-tareas-pizzeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Wir haben mit dem Kit de Escandallos Pro Pizza für Pizza kalkuliert und festgestellt, dass 4 Varianten Verlust machten, weil zu viel Mozzarella gewogen wurde. Wir haben Grammatur und Preis angepasst. Die Marge des Lokals stieg in 2 Monaten um 4 Punkte, ohne die Qualität anzutasten.",
    "testimonialAuthor": "Giovanni Russo",
    "testimonialRole": "Pizzaiolo und Inhaber einer neapolitanischen Pizzeria",
    "faqTitle": "Häufige Fragen für Pizzerien",
    "faqs": [
      {
        "q": "Funktioniert das für neapolitanische, römische, amerikanische Pizza oder Detroit?",
        "a": "Für alle. Italienische Küche und Fermentus mit AI+ decken das gesamte Spektrum an Teigen, Hydratationen, Fermentationen und Techniken jedes Stils ab."
      },
      {
        "q": "Umfasst es neben dem Lokal auch Lieferservice?",
        "a": "Ja. Das Kit de Tareas Pizzería enthält spezifische Vorlagen für den Lieferservice mit Zeiten, zugehörigen Verlusten und Koordination mit Plattformen (Glovo, Uber Eats, Just Eat)."
      },
      {
        "q": "Funktioniert das für ein einzelnes Lokal oder eine Pizzeria-Kette?",
        "a": "Beides. Es gibt Kunden mit 1 Lokal und andere mit mehr als 12 aktiven Standorten. Für Gruppen standardisiert der Executive Chef Pro Rezepte und Handbücher."
      },
      {
        "q": "Generiert es Ideen für Aktionen an schwachen Tagen?",
        "a": "Ja. Gastro Calendar + InstaFlow AI Pro generieren Combos, Angebote, Redaktionskalender und saisonale Kampagnen mit professioneller Kreativität."
      },
      {
        "q": "Wie hilft es mir bei professionellem Sauerteig?",
        "a": "Fermentus mit AI+ ist eine Referenz in der Fermentation: Hydratationen, Vorteige (Poolish, Biga, Tangzhong), Auffrischen von Sauerteig und Techniken der kontrollierten Fermentation."
      }
    ],
    "ctaTitle": "Pizza mit echter Marge, nicht Bauchgefühl.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits, um alle Agenten zu nutzen.",
    "seo": {
      "title": "KI für Pizzerien: Sauerteig, Kalkulation pro Pizza und Lieferservice | AI Chef Pro",
      "description": "KI-Suite für professionelle Pizzerien: Italienische Küche, Fermentus für Teige, Kalkulation pro Pizza, Pizzeria-Vorlagen und lokales SEO. Starten Sie noch heute.",
      "keywords": "KI Pizzeria, Pizzakalkulation, Pizzeria-Software, Sauerteig Pizza KI, neapolitanische Pizza KI, römische Pizza KI, Pizzeria-Lieferservice-Management, Pizzeria Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/pizzeria.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Pizzeria zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding-Gespräch, in dem Sie erzählen, welche Art von Pizzeria Sie betreiben (neapolitanisch, römisch, amerikanisch, Detroit, alla pala), Anzahl der Sitzplätze, Stadt und Betriebsabläufe. Von diesem Moment an antwortet jeder Agent – von Italienische Küche bis MenuDish Local SEO – angepasst an Ihren Teigstil, Ihre Lieferplattformen und Ihren lokalen Markt.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrer Pizzeria nutzen werden",
    "apps": [
      {
        "name": "Italienische Küche",
        "category": "Rezeptsammlungen nach Ländern",
        "description": "Spezialisierter Agent für professionelle italienische Küche mit Fokus auf neapolitanische und römische Pizza."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Sauerteig, hohe Hydratationen und lange Fermentationen mit professioneller Unterstützung."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung kreativer Pizzen mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Zur Koordination des restlichen Casual-Menüs der Pizzeria (Vorspeisen, Desserts)."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Präzise Daten zu Lebensmittelabfällen bei Teig, Mozzarella und Belägen."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Automatische Identifizierung von Allergenen pro Pizza und Gericht."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und Social Media",
        "description": "Lokale SEO-Beschreibungen zur Verbesserung des Website-Rankings und des Lieferservices."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und Social Media",
        "description": "Blogbeiträge zur Gewinnung lokal organischen Traffics."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Inhalte und Social Media",
        "description": "Keywords nach Postleitzahl: „neapolitanische Pizza [Ihr Stadtteil]“."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und Social Media",
        "description": "Viraler Instagram-Content mit Pizzafotos und Redaktionskalender."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Food-Fotografie für Website und Lieferplattformen."
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "Marge nach Pizza-für-Pizza-Kalkulation"
      },
      {
        "value": "×2",
        "label": "Lieferservice-Traffic durch lokales SEO"
      },
      {
        "value": "−25 %",
        "label": "Lebensmittelabfälle durch systematische Kontrolle"
      },
      {
        "value": "11+",
        "label": "Agenten für Ihre Pizzeria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Sauerteig und Technik verstreut im Notizbuch des Chef-Pizzaiolo",
        "Kalkulation nach Augenmaß, Grammaturen variieren zwischen Pizzaioli",
        "Lebensmittelabfälle bei Mozzarella und Teig ohne echte Kontrolle",
        "Schwaches Lieferservice-Ranking durch generische Beschreibungen",
        "Improvisierte Lieferservice-Abläufe in Spitzenzeiten"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Italienische Küche + Fermentus mit AI+ dokumentieren Teig und reproduzierbare Technik",
        "Professionelle Kalkulation pro Pizza mit validierter Marge",
        "Kontrollierte Verluste mit Lebensmittelabfälle AI und spezifischen Vorlagen",
        "Optimiertes lokales SEO mit MenuDish Local SEO + Keyword Discovery",
        "Kit de Tareas Pizzería mit Vorlagen für Lieferservice, Vor-Ort-Betrieb und Spitzenzeiten"
      ]
    },
    "galleryTitle": "So funktioniert eine professionelle Pizzeria",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Ofen, Sauerteig, Pizza im Detail, Topping-Vorbereitung, Team und Lieferservice.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-pizzeria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-oven.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-dough.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-pizza.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-toppings.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-delivery.jpg"
    ]
  },
  "hamburgueseria": {
    "h1": "KI für Burger-Restaurants",
    "heroSubtitle": "Kalkulation pro Burger, Kontrolle der Kosten für Fleisch und Brot, Verwaltung von Lieferung und Multi-Marke mit einer Suite von KI-Agenten, spezialisiert auf Gourmet-Smash-Burger, Fast Casual und Dark Kitchen für Burger.",
    "heroTagline": "Burger mit echter Marge, nicht Intuition",
    "badge": "Für Burger-Restaurants und Burger-Shops",
    "painsTitle": "Was ein Burger-Restaurant unbedingt lösen muss",
    "pains": [
      "Fleisch und Brot: Schlüsselzutaten mit volatilen Kosten, die sich wöchentlich ändern",
      "Lebensmittelabfälle beim Garen von Fleisch, beim Anrichten und Verpacken für den Lieferdienst",
      "Lieferung mit sehr hoher Fluktuation und extremen Spitzen zu bestimmten Zeiten",
      "Umfangreiche Speisekarte mit vielen Burger-Varianten (klassisch, Gourmet, Smash, Plant-based)",
      "Sich in einem gesättigten Markt von Burger-Shops mit lokalem SEO und sozialen Medien abheben",
      "Standardisierung der Grill- und Anrichtetechnik bei wechselndem Team"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem Burger-Restaurant hilft",
    "features": [
      {
        "icon": "Beef",
        "title": "Burger Pro AI+",
        "description": "Spezialisierter Agent für Burger-Restaurants: Gourmet, Smash, Fast Food, Plant-based, handwerklich und thematisch."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Burger",
        "description": "Kreativküche liefert Rezept + Kalkulations-CSV; Kit de Escandallos Pro verwaltet es mit Ihren realen Preisen (Fleisch, Brot, Käse, Toppings, Saucen)."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Hamburguesería",
        "description": "Vorlagen: Vorbereitung von Saucen, Mise en Place der Toppings, Grillplatte, Anrichten, Service und Lieferung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC + Allergen-ID",
        "description": "Rückverfolgbarkeit von Fleisch, Garkontrolle, Temperatur und Allergene pro Burger."
      },
      {
        "icon": "Truck",
        "title": "Multi-Plattform-Lieferverwaltung",
        "description": "Finanzplan mit Margenberechnung nach Provisionen von Glovo, Uber Eats und Just Eat pro virtueller Marke."
      },
      {
        "icon": "Leaf",
        "title": "VegChef Plant-Based",
        "description": "Für vegetarische Burger mit Ernährungstechnik: Beyond Meat, Heura, hochwertige pflanzliche Alternativen."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + InstaFlow AI Pro",
        "description": "Lokale Platzierung bei Google und virale Inhalte für Instagram, wo Burger-Shops am meisten verkaufen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "KI-Lebensmittelfotografie, entscheidend für Glovo, Uber Eats und Just Eat: besseres Foto = mehr Klicks und besseres Ranking."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Schichtpläne für Grillplatte, Anrichten, Saal und Lieferung mit rotierenden Schichten."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem Burger-Restaurant mit AI Chef Pro",
    "workflow": [
      "11:00 · Eröffnung – Checkliste Kit de Tareas Hamburguesería: Vorbereitung hausgemachter Saucen, Mise en Place der Toppings, Grillplatte bereit.",
      "12:00 · Burger Pro AI+ – Sie entwickeln einen neuen Gourmet-Burger mit Ziegenkäse und Zwiebelmarmelade. Kreativküche liefert Rezept + Kalkulations-CSV.",
      "12:30 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren realen Preisen hoch und validieren die Marge von 31 % nach Glovo-Provision (29 %).",
      "13:00 · Mittagsservice – Grillplatte aktiv, koordiniertes Anrichten, Lieferung geht raus, voller Saal.",
      "16:00 · MenuDish Local SEO + GastroIMG Gen+ – Sie aktualisieren den neuen Burger auf Plattformen mit professionellem Foto und optimierter Beschreibung.",
      "17:30 · Inventar – Sie validieren Fleischbestellungen (lokaler Lieferant), Brioche-Brot und Premium-Käse.",
      "20:00 · Abendservice – Lieferungsspitze, Fließbandmontage, Grillplatte auf Maximum.",
      "23:30 · Schließung – Reinigung, HACCP unterschrieben, Tagesbericht und erfasste Lebensmittelabfälle."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Burger-Restaurants",
    "productIds": [
      "kit-tareas-hamburgueseria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Wir senkten den Food Cost von 36 % auf 31 % in 60 Tagen mit präzisen Kalkulationen und systematischer Kontrolle der Lebensmittelabfälle. Die Investition in AI Chef Pro hat sich allein damit in einer Woche amortisiert. Das KI-Foto für Glovo hat unser Ranking von Platz 8 auf Platz 3 verbessert.",
    "testimonialAuthor": "Pablo Hernández",
    "testimonialRole": "Inhaber, Gourmet-Burger-Restaurant mit 2 Marken im Lieferdienst",
    "faqTitle": "Häufig gestellte Fragen für Burger-Restaurants",
    "faqs": [
      {
        "q": "Funktioniert es für Gourmet-, Smash- oder Casual-Burger-Restaurants?",
        "a": "Für alle. Burger Pro AI+ deckt das gesamte Spektrum ab: Gourmet, Smash Burger, Fast Food, Plant-based und thematische."
      },
      {
        "q": "Deckt es auch Lieferung neben dem Lokal ab?",
        "a": "Ja. Spezifische Vorlagen mit Lieferabfällen, gebrandeter Verpackung, Koordination mit Plattformen und Margenberechnung nach Provisionen."
      },
      {
        "q": "Gibt es eine spezifische Kontrolle von Fleisch und Rückverfolgbarkeit?",
        "a": "Ja. Pack APPCC mit Rückverfolgbarkeit von Fleisch, Garkontrolle auf den Punkt, Innentemperatur und Konservierung."
      },
      {
        "q": "Generiert es Ideen für Combos und Aktionen?",
        "a": "Ja. Gastro Calendar + InstaFlow + Pro Prompts eBook generieren Combos, Angebote für schwache Tage, Redaktionskalender und Kampagnen mit KI."
      },
      {
        "q": "Eignet es sich, um eine virtuelle Burger-Marke in einer Dark Kitchen zu eröffnen?",
        "a": "Ja. Burger Pro AI+ + Casual Restaurants AI+ + Food Truck AI+ sind für virtuelle Multi-Marken kombinierbar. Es gibt einen echten Fall unter /usos/concepto/dark-kitchen."
      }
    ],
    "ctaTitle": "Burger mit echter Marge, nicht Intuition.",
    "ctaSubtitle": "Beginnen Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für die Nutzung aller Agenten.",
    "seo": {
      "title": "KI für Burger-Restaurants: Kalkulation, Smash Burger und Lieferung | AI Chef Pro",
      "description": "KI-Suite für professionelle Burger-Restaurants: Burger Pro AI+, Kalkulation pro Burger, Burger-Shop-Vorlagen, APPCC und Multi-Plattform-Lieferung. Starten Sie noch heute.",
      "keywords": "KI Burger-Restaurant, Burger-Kalkulation, Software Burger-Restaurant, Smash Burger KI, Burger-Lieferverwaltung, Gourmet-Burger-Restaurant KI, Burger-Restaurant Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/hamburgueseria.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Burger-Restaurant zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational-Onboarding, bei dem Sie erzählen, welche Art von Burger-Restaurant Sie betreiben (Gourmet, Smash, Fast Casual, Plant-based), Anzahl der Plätze, Stadt, Lieferplattformen und Provisionen. Jeder Agent – von Burger Pro AI+ bis zum Kit de Escandallos Pro – antwortet angepasst an Ihren Stil und Ihren realen Markt.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Burger-Restaurant verwenden werden",
    "apps": [
      {
        "name": "Burger Pro AI+",
        "category": "Geschäftskonzepte",
        "description": "Spezialisierter Agent für Burger-Restaurants: Gourmet, Smash, Fast Food, Plant-based."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung professioneller Burger mit Rezept + Kalkulations-CSV."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Kulinarische Kreativität",
        "description": "Für vegetarische Burger mit professioneller Ernährungstechnik."
      },
      {
        "name": "Food Truck AI+",
        "category": "Geschäftskonzepte",
        "description": "Für mobile Konzepte und Multi-Marken-Dark Kitchens für Burger."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Präzise Daten zu Lebensmittelabfällen beim Garen von Fleisch und beim Anrichten."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Hilfsprogramme",
        "description": "Automatische Identifizierung von Allergenen pro Burger und Sauce."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale SEO-Beschreibungen für Glovo, Uber Eats und Web."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und soziale Medien",
        "description": "Blogbeiträge, um lokale Suchanfragen nach Burgern zu erfassen."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Inhalte und soziale Medien",
        "description": "Keywords nach Postleitzahl: „Smash Burger [Ihr Stadtteil]“."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Virale Instagram-Inhalte für Burger-Restaurants."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Lebensmittelfotografie für Lieferplattformen."
      }
    ],
    "metrics": [
      {
        "value": "−5 pp",
        "label": "Food Cost in 60 Tagen"
      },
      {
        "value": "+5",
        "label": "Plätze im Glovo-Ranking"
      },
      {
        "value": "×3",
        "label": "Geschwindigkeit bei der Einführung neuer Burger"
      },
      {
        "value": "11+",
        "label": "Agenten für Ihren Burger-Shop"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Kalkulation nach Augenmaß mit variablem Gewicht zwischen Köchen",
        "Food Cost bei 36 % durch unkontrollierte Abfälle und Anrichten",
        "Fotos auf Glovo und Uber Eats von geringer Qualität, niedriges Ranking",
        "Fleisch- und Anrichteabfälle ohne Rückverfolgbarkeit",
        "Improvisierter Lieferbetrieb in Stoßzeiten"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Burger Pro AI+ + Kreativküche dokumentieren reproduzierbare Technik",
        "Food Cost bei 31 % mit professioneller Kalkulation und kontrollierten Abfällen",
        "Professionelle Fotos mit GastroIMG Gen+ verbessern das Ranking auf Plattformen",
        "Pack APPCC mit Rückverfolgbarkeit von Fleisch und erfassten Abfällen",
        "Kit de Tareas Hamburguesería mit Vorlagen für Lieferung und Lokal"
      ]
    },
    "galleryTitle": "So funktioniert ein modernes Burger-Restaurant",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Grillplatte, Smash Burger, Anrichten, Vorbereitung, Team und Lieferung.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-grill.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-burger.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-delivery.jpg"
    ]
  },
  "dark-kitchen": {
    "h1": "KI für Dark Kitchens und virtuelle Küchen",
    "heroSubtitle": "Skalieren Sie 1, 4 oder 10 virtuelle Marken in derselben Küche. Kontrollieren Sie den Food Cost pro Marke und Plattform, verbessern Sie Ihre Positionierung in KI-Agenten der Delivery-Plattformen und vervielfachen Sie die Bestellungen, ohne mehr Personal im Service zu benötigen.",
    "heroTagline": "Küche ohne Saal, Marge mit System",
    "badge": "Dark Kitchen und Ghost Kitchen",
    "painsTitle": "Was ein Dark-Kitchen-Betreiber unbedingt lösen muss",
    "pains": [
      "Mehrere Marken in derselben Küche, jede mit eigener Kalkulation und Rohstoffkosten, die sich wöchentlich ändern",
      "Marge unter Druck durch Provisionen von Glovo, Uber Eats und Just Eat (zwischen 25 % und 35 % des Tickets)",
      "Extreme Spitzen im Delivery von 12:30 bis 14:30 und von 20:30 bis 22:30, ohne Spielraum für operative Fehler",
      "Kein physischer Kontakt zum Kunden: Die Marke, die Fotos und der Text der Karte sind alles, was Sie haben",
      "Ständig wechselndes Ranking auf den Plattformen: Verlieren Sie Positionen, brechen die Bestellungen massiv ein.",
      "Es ist schwierig zu erkennen, welche Marke und welches Gericht wirklich rentabel sind, wenn alles in derselben Küche zusammenläuft."
    ],
    "featuresTitle": "Wie AI Chef Pro einer Dark Kitchen hilft",
    "features": [
      {
        "icon": "Layers",
        "title": "Multi-Marken-Kalkulation: Kreativküche → Kit de Escandallos Pro",
        "description": "Die Kreativküche erstellt das Gericht und die anfängliche Kalkulation als CSV mit Marktreferenzpreisen. Sie laden sie in das Kit de Escandallos Pro, ersetzen die Preise durch die Ihrer Lieferanten und erhalten die echten Kosten und Marge pro Marke, pro Gericht und pro Plattform."
      },
      {
        "icon": "Smartphone",
        "title": "Burger Pro AI+, Food Truck AI+ und Casual Restaurants AI+",
        "description": "Drei spezialisierte Agenten, die die rentabelsten virtuellen Konzepte im Liefergeschäft abdecken: Hamburgerrestaurants, Fast Food, Casual Dining und Bistros."
      },
      {
        "icon": "Truck",
        "title": "Berechnung der echten Marge nach Abzug der Kommission",
        "description": "Der Finanzplan von AI Chef Pro zieht automatisch die Kommissionen jeder Plattform ab und zeigt Ihnen die echte Marge pro Marke und pro Kanal."
      },
      {
        "icon": "TrendingUp",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "SEO-Suite, damit Ihre Marken im lokalen Google-Ranking aufsteigen und organischen Traffic gewinnen – zusätzlich zu dem Traffic, der über die KI-Agenten kommt."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Recherche lokaler gastronomischer Keywords, um Marken, Gerichte und Speisekarten zu benennen, die besser ranken."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "KI-generierte Food-Fotografie für die Plattform-Fiches. Bessere Fotos = mehr Klicks und bessere Positionierung."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche + Italienische, Mexikanische, Japanische Küche…",
        "description": "Mehr als 25 KI-Rezeptsamlungen pro Land, um thematische virtuelle Marken mit professioneller Basis zu kreieren – keine von Google kopierten Rezepte."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP + Allergen-ID für Lieferdienste",
        "description": "Rückverfolgbarkeit, Temperatur und Allergene – abgestimmt auf Produkte, die im Rucksack oder auf dem Motorrad transportiert werden."
      },
      {
        "icon": "BarChart3",
        "title": "Multi-Marken- und Multi-Plattform-Dashboard",
        "description": "KPIs pro Marke, durchschnittlicher Bestellwert, Kommission, Ranking-Position und Produktivität – alles konsolidiert in einem einzigen Überblick."
      }
    ],
    "workflowTitle": "Ein echter Tag in einer Dark Kitchen mit AI Chef Pro",
    "workflow": [
      "08:30 · Sie prüfen das Dashboard des Vortags: Marke A liegt vorn, Marke C ist im Ranking um 12 % gefallen. Sie müssen handeln.",
      "09:00 · Keyword Discovery AI+ — Sie recherchieren, wonach Nutzer in Ihrer Postleitzone suchen, und entdecken ein Keyword, das Marke C fehlt.",
      "09:30 · MenuDish Local SEO — Sie aktualisieren die Beschreibungen der 6 Top-Gerichte von Marke C mit diesem Keyword.",
      "10:00 · Kreativküche — Brainstorming für ein neues Signature-Gericht bei Marke A, das Sie nutzen, weil ein Lieferant Ihnen einen guten Preis gegeben hat. Derselbe Agent liefert Ihnen das vollständige Rezept und eine erste Kalkulation mit Referenzmarktpreisen, als CSV-Download.",
      "10:30 · Kit de Escandallos Pro — Sie laden das CSV aus der Kreativküche hoch, ersetzen die Referenzpreise durch Ihre ausgehandelten Lieferantenpreise und validieren die Marge nach Provision bei Glovo (29 %) und Uber Eats (25 %).",
      "11:00 · GastroIMG Gen+ — Sie generieren das Foto des neuen Gerichts und laden es auf die Plattformen hoch.",
      "12:30 · Delivery-Betrieb mit 4 Marken in derselben Küche, unterstützt durch die Dark-Kitchen-Aufgabenvorlagen.",
      "16:00 · HACCP unterschrieben, Lebensmittelabfälle pro Marke erfasst und Mise en Place für das Abendessen fertig.",
      "23:30 · Abschluss: automatischer Bericht pro Marke an das WhatsApp des Eigentümers."
    ],
    "productsTitle": "Vorlagen, Kits und Leitfäden zum Download für Dark Kitchens",
    "productIds": [
      "guia-dark-kitchen",
      "kit-tareas-dark-kitchen",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "kit-inventario"
    ],
    "testimonialQuote": "Wir betreiben 4 virtuelle Marken in einer Küche. Ohne Kalkulationen pro Marke und Plattform verloren wir Marge, ohne zu wissen wo. AI Chef Pro hat das in einer Woche gelöst: Wir entdeckten, dass eine Marke bei Glovo einen Food Cost von 41 % hatte. Wir haben sie neu gestaltet und die Marge um 7 Punkte gesteigert, ohne den Preis anzufassen.",
    "testimonialAuthor": "Iván Domínguez",
    "testimonialRole": "Betreiber, Dark Kitchen mit 4 virtuellen Marken",
    "faqTitle": "Häufige Fragen von Dark-Kitchen-Betreibern",
    "faqs": [
      {
        "q": "Funktioniert das für eine Marke oder für mehrere was in derselben Küche?",
        "a": "Für beides. Es is von Anfang an für Multi-Marken konzipiert: unabhängige Kalkulation pro Marke, getrennte KPIs und Aufgabenlisten, die die Produktion mehrerer Marken in demselben Arbeitsgang koordinieren."
      },
      {
        "q": "Sind die Kommissionen der Plattformen (Glovo, Uber Eats und Just Eat) abgedeckt?",
        "a": "Ja. Die Berechnung der echten Marge zieht automatisch die Kommission jeder Plattform ab – so wissen Sie, was Sie bei jeder Bestellung pro Kanal verdienen, und können Ihre Preisstrategie besser festlegen."
      },
      {
        "q": "Gibt es eine Schritt-für-Schritt-Anleitung zum Eröffnen einer Dark Kitchen?",
        "a": "Ja, die Guía Cómo Montar una Dark Kitchen (24 €): 12 Kapitel mit rechtlichen Anforderungen, Financierungsplan, Küchendesign, Technklore, Technologie, Marketing und Plattformen, plus 3 Excel-Checklisten und ein Rechner."
      },
      {
        "q": "Eignet sich das System zum Skalieren auf mehrere Dark-Kitchen-Standorte?",
        "a": "Ja. Die Multi-Standort-Standardisierung des Agenten Executive Chef Pro und der konsolidierten Dashboards sind für Gruppen mit mehreren virtuellen Einheiten gedacht."
      },
      {
        "q": "Wie hilft mir das, mein Ranking in den KI-Agenten der Lieferplattformen zu verbessern?",
        "a": "Mit drei Hebeln: GastroIMG Gen+ für Fotos in besser Qualität (erhöhen die Klickrate), MenuDish Local SEO für Beschreibungen, die konvertieren, und Keyword Discovery AI+, um zu erkennen, was Nutzer in Ihrer Postleitzahl suchen."
      },
      {
        "q": "Passt sich das System an mein Land und meine Plattformen an?",
        "a": "Ja. Sie starten mit dem Agenten „Wer sind Sie?“ in einem 2-minütigen Onboarding, in dem Sie angeben, wo Sie operieren, welche Plattformen Sie nutzen und welche Kommissionen Sie ausgehandelt haben. Alles Weitere passt sich diesem Kontext an."
      },
      {
        "q": "Und das lokale SEO? Lohnt sich das für eine Dark Kitchen?",
        "a": "Ja, auf jeden Fall. Eine Dark Kitchen lebt davon, online entdeckt zu werden: Wenn Sie zusätzlich zum Traffic der KI-Agenten lokale Suchanfragen in Google abdecken (zum Beispiel „Burger-Lieferung [Ihr Viertel]“), reduzieren Sie Ihre Abhängigkeit von den Provisionen und erzielen direkte Margen. Die SEO-Suite von AI Chef Pro ist genau dafür konzipiert."
      }
    ],
    "ctaTitle": "Ihre Dark Kitchen mit echter Marge und Daten pro Marke.",
    "ctaSubtitle": "Starten Sie mit dem 2-Minuten-Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Dark Kitchens und virtuelle Küchen: Kalkulationen und SEO | AI Chef Pro",
      "description": "KI-Suite für Dark Kitchens und Ghost Kitchens: Multi-Marken-Kalkulationen, Marge nach Provision von Glovo und Uber Eats, lokales SEO, HACCP und Leitfaden zur Eröffnung Ihrer virtuellen Küche.",
      "keywords": "KI Dark Kitchen, Dark Kitchen Software, Ghost Kitchen, virtuelle Küche, Multi-Marken-Kalkulationen, Dark Kitchen eröffnen, KI-Delivery-Management, Sichtbarkeit Glovo Uber Eats, Ghost-Kitchen-Software, virtuelle Delivery-Marke, Dark Kitchen Spanien, lokales SEO Restaurant Delivery",
      "ogImage": "https://aichef.pro/og/use-cases/dark-kitchen.jpg"
    },
    "personalizationTitle": "Angepasst an Ihre Marken, Ihre Zone und Ihre Plattformen",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen konversationellen Onboarding. Sie erzählen, welche Marken Sie betreiben, in welcher Stadt und Postleitzone, welche Plattformen Sie nutzen (Glovo, Uber Eats, Just Eat) und welche Provisionen Sie ausgehandelt haben. Ab diesem Moment werden die Kalkulationen mit Ihrer tatsächlichen Provision berechnet, die lokalen SEO-Empfehlungen zielen auf Ihr Viertel und die KPIs werden pro Marke und Kanal konsolidiert, genau wie Sie es benötigen. Das ist kein Formular: Es ist ein kurzes Gespräch, das jeden Agenten in ein Werkzeug verwandelt, das auf Sie zugeschnitten ist.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrer Dark Kitchen nutzen werden",
    "apps": [
      {
        "name": "Burger Pro AI+",
        "category": "Geschäftskonzepte",
        "description": "Spezialist für virtuelle Burger-Restaurants: Gourmet, Fast Food, Smash Burger und pflanzliche Gerichte."
      },
      {
        "name": "Food Truck AI+",
        "category": "Geschäftskonzepte",
        "description": "Mobile und virtuelle Fast-Food-Konzepte mit schmaler Marge."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Bistros, Gastrobars, Tapas und virtuelle mediterrane Küche: das gesamte Casual-Spektrum."
      },
      {
        "name": "Italienische Küche, Mexikanische Küche, Japanische Küche, Thailändische Küche…",
        "category": "Rezeptsammlungen nach Ländern",
        "description": "Mehr als 25 KI-Rezeptsammlungen, um thematische virtuelle Marken mit professioneller Basis zu erstellen. Jedes Rezept enthält eine erste Kalkulation im CSV-Format, bereit für das Kit de Escandallos Pro."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Dienstprogramme",
        "description": "Präzise Daten zu Lebensmittelabfällen und Ausbeuten. Kritisch für eine realistische Kalkulation im Lieferservice."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Dienstprogramme",
        "description": "Automatische Identifizierung von Allergenen pro Rezept. Obligatorisch für den legalen Verkauf im Lieferservice."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte & Social Media",
        "description": "SEO-optimierte Beschreibungen je Gericht, bereit für Blog und Plattformen."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte & Social Media",
        "description": "Blogbeiträge, die lokalen organischen Traffic auf Ihre virtuellen Marken lenken."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Inhalte & Social Media",
        "description": "Keyword-Recherche für Gastronomie nach Postleitzahl."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Foodfotografie mit KI für Plattform-Profile: besseres Foto, bessere Platzierung."
      },
      {
        "name": "Profi Restaurantmanager",
        "category": "Gastro Profile Pro",
        "description": "Operativer Assistent zur Koordination von Marken, Teams und Lieferanten."
      },
      {
        "name": "InstaFlow AI Pro + Pinterest Pins Gen",
        "category": "Inhalte & Social Media",
        "description": "Virale Inhalte, um über die Lieferplattformen hinaus Publikum zu gewinnen."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "Marge nach Kalkulation pro Marke"
      },
      {
        "value": "×4",
        "label": "virtuelle Marken in einer Küche"
      },
      {
        "value": "−35 %",
        "label": "Zeit für Multi-Marken-Management"
      },
      {
        "value": "12+",
        "label": "KI-Agenten für Dark Kitchens"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Manuelle Kalkulation in Excel mit „durchschnittlicher“ Marge zwischen den Marken",
        "Plattformprovisionen nach Augenmaß abgezogen, ohne zu wissen, welcher Kanal sich mehr lohnt",
        "Plattformfotos von mittlerer Qualität und unbeständige Platzierung",
        "Generische Beschreibungen, die lokales SEO nicht abdecken",
        "Vermischte KPIs: unmöglich zu erkennen, welche Marke wirklich rentabel ist",
        "Operative Abläufe in losen Blättern und Fehler in Spitzenzeiten"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Unabhängige Kalkulation pro Marke und pro Plattform, mit sofortiger realer Marge",
        "Automatische Berechnung nach Provision pro Kanal und datenbasierte Preisentscheidungen",
        "Professionelle Fotografien mit GastroIMG Gen+ und stabilere Platzierung",
        "Beschreibungen und Blog optimiert für das lokale SEO Ihres Postleitzahlengebiets",
        "Multi-Marken-Dashboard mit separaten KPIs nach Marke und Kanal",
        "Spezifische Dark-Kitchen-Aufgabenlisten zur Koordination der Multi-Marken-Produktion"
      ]
    },
    "galleryTitle": "So funktioniert eine moderne Dark Kitchen",
    "gallerySubtitle": "Multi-Marken-Produktion, Branded Packaging pro virtueller Marke, Bildschirme mit Bestellungen von Glovo, Uber Eats und JustEat, Rider beim Pickup und alles, was zu einem 100 %-Delivery-Betrieb gehört.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-cooking.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-packaging.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-orders.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-pickup.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-app.jpg"
    ]
  },
  "pasteleria-obrador": {
    "h1": "KI für Konditorei und Backstube",
    "heroSubtitle": "Kalkulation pro Stück mit Backstuben-Stundensatz, planen Sie saisonale Produktion und erfassen Sie professionelles Branding mit einer Suite von KI-Agenten, die auf handwerkliche Konditorei spezialisiert sind.",
    "heroTagline": "Konditorei mit echter Marge und ohne Papierkram",
    "badge": "Für Konditoreien und handwerkliche Backstuben",
    "painsTitle": "Was eine Konditorei unbedingt lösen muss",
    "pains": [
      "Komplexe Kalkulationen mit Sauerteigen, Vorteigen und langen Zubereitungen, die Stunden in der Backstube erfordern",
      "Hoher Ausschuss in der Backstube (Formen, Backen, Dekorieren), der unkontrolliert die Rentabilität schmälert",
      "APPCC-Rückverfolgbarkeit bei empfindlichen Produkten: Eier, Milchprodukte, Cremes, Nüsse",
      "Starke Saisonalität: Dreikönigskuchen, Valentinstag, Ostern, Weihnachten, Kommunionen",
      "Differenzierung in umkämpftem Gebiet: visuelles Branding, Vitrine und soziale Medien sind entscheidend",
      "Aufträge für maßgefertigte Torten mit Marge gewinnen, während man den täglichen Konditoreibetrieb managt"
    ],
    "featuresTitle": "Wie AI Chef Pro in der Konditorei hilft",
    "features": [
      {
        "icon": "Cake",
        "title": "Kreative Patisserie",
        "description": "Spezialisierter Agent für professionelle Konditorei, Restaurant-Desserts, maßgeschneiderte Torten und Gebäck mit fortgeschrittener Technik."
      },
      {
        "icon": "Cookie",
        "title": "Kreative Schokolade",
        "description": "Für Backstuben, die Konditorei mit Schokoladenherstellung verbinden: Pralinen, Ganachen, Kuvertüren und Kombinationen."
      },
      {
        "icon": "Wheat",
        "title": "Kreative Boulangerie",
        "description": "Für Backstuben, die ihr eigenes Gebäck mit Sauerteig, Brioche, Croissants und handwerklichem Brot herstellen."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Professionelle Sauerteige, kontrollierte Fermentationen und innovative Backprozesse."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulationen mit Backstuben-Stundensatz",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet dies mit integriertem Backstuben-Stundensatz in der echten Marge pro Stück."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pastelería",
        "description": "Vorlagen: Sauerteigvorbereitung, Produktion, Formen, Backen, Vitrine, Konservierung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Konditorei",
        "description": "Rückverfolgbarkeit von Eiern, Milchcremes, Nüssen und professioneller Konservierung."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Saisonale Planung mit wichtigen Terminen: Dreikönigskuchen, Valentinstag, Ostern, Weihnachten. Redaktionskalender für die Vitrine."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "KI-Lebensmittelfotografie + Pinterest, wo Konditoreien mehr stabilen organischen Traffic erzielen."
      }
    ],
    "workflowTitle": "Ein echter Tag in einer Konditorei mit AI Chef Pro",
    "workflow": [
      "06:00 Uhr · Eröffnung – Checkliste Kit de Tareas Pastelería: Sauerteig auffrischen, Teige anrühren, Cremes vorbereiten.",
      "08:00 Uhr · Kreative Patisserie – Sie entwickeln ein neues Dessert zum Valentinstag. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "09:00 Uhr · Kit de Escandallos Pro – Sie laden die CSV mit Ihren tatsächlichen Preisen und integriertem Backstuben-Stundensatz hoch und validieren die Marge.",
      "11:00 Uhr · Tagesproduktion – Formen und Backen mit spezifischen Vorlagen, Ausschuss mit APPCC erfasst.",
      "14:00 Uhr · Vitrine mit Etiketten und Preisen auffüllen, Kontrolle des Ausstellungsausschusses.",
      "16:00 Uhr · Gastro Calendar – Sie bereiten die Produktionsplanung für den Dreikönigskuchen (Weihnachten) vor.",
      "18:00 Uhr · GastroIMG Gen+ + Pinterest Pins Gen – Sie erstellen Fotos und Pins des neuen Desserts, um Traffic zu generieren.",
      "20:00 Uhr · Abschluss – gründliche Reinigung, APPCC unterschrieben, Planung für den nächsten Tag."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Konditoreien",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Die Stückkalkulationen mit Backstuben-Stundensatz haben mir die Augen geöffnet. Ich habe festgestellt, dass einige aufwendige Zubereitungen trotz guter Verkäufe nicht rentabel waren. Wir haben sie mit Kreative Patisserie neu gestaltet, den Prozess vereinfacht, ohne Qualität zu verlieren, und die Marge um 6 Punkte gesteigert.",
    "testimonialAuthor": "Eva Mata",
    "testimonialRole": "Inhaberin, handwerkliche Konditorei mit eigener Backstube",
    "faqTitle": "Häufige Fragen von Konditoreien",
    "faqs": [
      {
        "q": "Eignet es sich für kleine oder große handwerkliche Backstuben?",
        "a": "Für beide. Die Vorlagen skalieren von der 2-Personen-Familienbackstube bis zur industriellen Produktion. Es gibt Kunden mit einem und mit sechs Konditoren."
      },
      {
        "q": "Deckt es neben Konditorei auch Bäckerei ab?",
        "a": "Ja. Kreative Boulangerie + Fermentus mit AI+ decken handwerkliche Bäckerei und professionellen Sauerteig für gemischte Backstuben ab."
      },
      {
        "q": "Gibt es eine Kontrolle der Backstuben-Stundenkosten?",
        "a": "Ja. Backstuben-Stundensatz integriert in die Kalkulation des Kit de Escandallos Pro: Eine aufwendige Zubereitung mit 3 Stunden Arbeitszeit pro Stück hat ihre tatsächlichen Kosten abgebildet."
      },
      {
        "q": "Erstellt es Inhalte für Vitrine und soziale Medien?",
        "a": "Ja. GastroIMG Gen+ für Vitrinenfotos + Pinterest Pins Gen + InstaFlow AI Pro + MenuDish Local SEO, um lokale Kunden zu gewinnen."
      },
      {
        "q": "Wie hilft es mir bei der Saisonalität?",
        "a": "Mit Gastro Calendar planen Sie die wichtigsten Saisons (Roscón, Valentinstag, Ostern, Weihnachten, Kommunionen) rechtzeitig und erhalten einen Finanzplan, der auf Produktionsspitzen abgestimmt ist."
      }
    ],
    "ctaTitle": "Ihre Backstube mit klarer Marge und professionellem Branding.",
    "ctaSubtitle": "Beginnen Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Patisserie & Produktion: Kalkulation, Saisonalität & Branding | AI Chef Pro",
      "description": "KI-Suite für handwerkliche Patisserien: Kreative Patisserie, Stückkalkulation mit Produktionsstundensatz, APPCC, saisonale Planung und Branding. Starten Sie noch heute.",
      "keywords": "KI Patisserie, Produktionssoftware, Patisserie Kalkulation, handwerkliche Patisserie KI, Sauerteig Patisserie, Roscón Weihnachten, Patisserie Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/pasteleria-obrador.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Backstube zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Gesprächs-Onboarding, bei dem Sie angeben, welche Art von Konditorei Sie betreiben (handwerklich, industriell, Restaurant-Patisserie, gemischte Backstube), Teamgröße, Stadt und Spezialgebiet. Jeder Agent – von Kreative Patisserie bis Gastro Calendar – antwortet angepasst an Ihr Produkt, Ihren Markt und Ihren tatsächlichen Betrieb.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrer Konditorei nutzen werden",
    "apps": [
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Spezialisierter Agent für professionelle Patisserie, Desserts und Torten mit fortgeschrittener Technik."
      },
      {
        "name": "Kreative Schokolade",
        "category": "Kulinarische Kreativität",
        "description": "Für Pralinen, Ganachen und Schokoladenkombinationen."
      },
      {
        "name": "Kreative Boulangerie",
        "category": "Kulinarische Kreativität",
        "description": "Für Sauerteig, Brioche, Croissants und handwerkliche Bäckerei."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Fermentationen, Vorteige und fortgeschrittene Bäckereitechniken."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Desserts mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für den Sosa-Katalog für Texturen und fortgeschrittene Techniken."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für den tSpoonLab-Katalog für fortgeschrittene Anwendungen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools & Utilities",
        "description": "Präzise Daten zu Lebensmittelabfällen in der Produktion (Formen, Backen, Vitrine)."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools & Utilities",
        "description": "Automatische Allergenerkennung pro Stück – entscheidend in der Patisserie."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Lebensmittelfotografie für Vitrine, Website und soziale Medien."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content & Social Media",
        "description": "Pinterest ist der Kanal mit dem stabilsten organischen Traffic für Patisserien."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content & Social Media",
        "description": "Saisonale Planung: Roscón, Valentinstag, Ostern, Weihnachten."
      }
    ],
    "metrics": [
      {
        "value": "+6 PP",
        "label": "Marge nach Stückkalkulation"
      },
      {
        "value": "×2",
        "label": "organischer Traffic über Pinterest"
      },
      {
        "value": "−30 %",
        "label": "Lebensmittelabfälle in der Produktion"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Produktion"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Kalkulationen ohne Produktionsstundensatz – lange Herstellungsprozesse erzeugen unbemerkt Verluste",
        "Lebensmittelabfälle in Produktion und Vitrine ohne echte Rückverfolgbarkeit",
        "Vitrine und soziale Medien improvisiert und ohne Kontinuität",
        "Reaktive Saisonproduktion ohne Vorlauf und Planung",
        "APPCC als verstreutes Papierdokument in der Produktion"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Professionelle Stückkalkulation mit integriertem Produktionsstundensatz",
        "Kontrollierte Lebensmittelabfälle mit Lebensmittelabfälle AI und spezifischen Vorlagen",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ generieren stabilen Traffic",
        "Gastro Calendar plant wichtige Saisons rechtzeitig",
        "APPCC mobil mit prüfungsbereiten Aufzeichnungen"
      ]
    },
    "galleryTitle": "So funktioniert eine handwerkliche Konditorei",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Vitrine, Backstube, Auslage der Stücke, Dekoration, Torten und Team.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-pasteleria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-obrador.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-display.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-piping.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-cakes.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-team.jpg"
    ]
  },
  "bar-cocktails": {
    "h1": "KI für Bar und Cocktailkunst",
    "heroSubtitle": "Designen Sie Karten mit Signature-Cocktails, kalkulieren Sie jedes Getränk mit Ihren echten Preisen und schaffen Sie professionelles Branding – mit einer Suite KI-Agenten, entwickelt für Barkeeper, Bartender und Barinhaber.",
    "heroTagline": "Ihre Bar mit echter Marge, Cocktailkunst mit Technik",
    "badge": "Für Cocktailbars",
    "painsTitle": "Was eine Cocktailbar unbedingt lösen muss",
    "pains": [
      "Komplexe Cocktails mit vielen Zutaten, Aufgüssen und Techniken zu kalkülieren",
      "Lebensmittelabfälle und Bruch Glaswaren an der Bar untergraben uncontrollable Rentability",
      "Thema wechselt familiene mit ständigen Innovationen",
      "Sehr geringe Marge bei Spirituosen mit einem leicht schwankenden Preis für Premium Alkohole",
      "Siciz in umkämpften Gebieten durch Stichtwörter und visuelles Branding von Cocktails abheben",
      "Führen einer Cocktailbar mit Bier, Weinen und Tapas Karte"
    ],
    "featuresTitle": "Die Hilfe von AI Chef Pro bei einer Cocktailbar",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Spezialagent für Pubs, Cocktailbars, Weinbars, Sport Bars und Spilscline-Lokale mit Profi-"
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Unerwartete Kombinationen für Signature-Cocktails mit wissenschaftlicher Basis und Pairing mit Tapas."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Fermentationen für anspruchsvolle Cocktails: Kombucha als Basisbasis, Aufgüsse, Zitrusfermente."
      },
      {
        "icon": "Calculator",
        "title": "Getränkekalkulationen",
        "description": "Kreativküche liefert Rezept und CSV-Berechnung; Kit de Escandallos Pro verwaltet es mit Ihren echten Preisen und professioneller Marge pro Cocktail."
      },
      {
        "icon": "BookOpen",
        "title": "Cocktailkarten mit Storytelling",
        "description": "Karte gestaltung undbuilding am saisonalen Karten mit professionellen Storytelling für Service und Presse."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Vorlagen: Vorbereitung von Säften, Sirupen, Garnishes, Aufgüßen, Bar-Mise-En-Place, Service und Intensive Reinigung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Bar",
        "description": "Spezifische Rückverfolgung: frische Säfte, Cremes, Garnishlar, Reinigung von Glaswaren."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "KI Fotografie von Cocktails + Instagram-Inhalte mit professionellen Redaktionskalender."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients AI + tSpoonLab Agent",
        "description": "Assistenten für Auswahl von Premium-präzisen Zutaten, sehr in der Signature-Cocktailkunst."
      }
    ],
    "workflowTitle": "Ein echter Tag in einer Cocktailbar mit AI Chef Pro",
    "workflow": [
      "11:00 · Eröffnung – Check-Liste Kit de Tareas Bar: Vorbereitung von Säften, Sirunen, Aufgüssen und Garnishes.",
      "14:00 · Bar & Lounge AI+ + Food Pairing AI – Sie entwickeln einen neuen Cocktail für die Frühjahrskarte mit dem Pairing im Kopf.",
      "15:00 · Kreativküche liefert Rezept + CSV-Berechnung; Kit de Escandallos Pro verwaltet es mit Ihren echten Preisen (Premium-Gin, Sirup, Garnitur).",
      "16:00 · Test des Cocktails mit dem Team, letzte Anpassung von Balance und Proportionen.",
      "17:00 · Pro Prompts eBook + BlogPost SEO Gen+ – Sie verfassen Storytelling für die neue Karte und eine Information für das Serviceteam.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie erstellen die Fotografie und die Instagram-Beiträge für den Markteintritt.",
      "20:00 · Abendservice – koordinierte Bar, validierte Berechnungen, Cocktails werden punktiv serviert.",
      "02:30 · Abschluss – gründliche Reinigung, HACCP unterschrieben, Tagesbericht der Getränke."
    ],
    "productsTitle": "Vorlagen und Kits zum Download für Bar und Cocktailkunst",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Jeden Cocktail zu berechnen und die Karte an einem Morgen fertig zu haben, hat meine Arbeitsweise verändert. Früher arbeitete ich mit Taschenrechner, Serviette und viel Intuition. Jetzt erstelle ich mit Bar & Lounge AI+ und dem Kit de Escandallos Pro in 2 Stunden eine neue Karte mit validierter Marge.",
    "testimonialAuthor": "Hugo Vázquez",
    "testimonialRole": "Barkeeper und Inhaber einer kreativen Cocktailbar",
    "faqTitle": "Häufige Fragen von Bartendern und Cocktailkünstlern",
    "faqs": [
      {
        "q": "Genügt es für Signature-Cocktails oder auch für ungezwungene Bars?",
        "a": "Für beides. Bar & Lounge AI. + + Food Pairing AI decken von klassischen Cocktails bis hin zur Avantgarde – Cocktailkunst mit professioneller Technik."
      },
      {
        "q": "Abdeckt er auch Bier und Wein zusätzlich zu Cocktails?",
        "a": "Ja. Bar & Lounge AI+ deckt das gesamte Spektrum ab: Brauereien, Weinstuben, Bars, traditionelle Pubs und Sports"
      },
      {
        "q": "Generiert es Ideen für neue Getränke mit Technik?",
        "a": "Ja. Bar & Lounge AI+, Kreativküche + Food Pairing AI + Fermentus mit AI+ arbeiten zusammen, um Cocktails auf professioneller Basis zu entwickeln."
      },
      {
        "q": "Funktioniert es für Hotel Bar oder unabhängiger Betrieb?",
        "a": "Beides. Die Hotel Lobby Bar wird im Anwendungsfall /der Fälle/Konzept/Gesamt-Hotel-F&B verwaltet; unabhängige Bar von Hier."
      },
      {
        "q": "Wie hilft es mir beim visuellen Branding meiner Cocktails?",
        "a": "GastroIMG Gen+ generiert professionelle Fotografie für Instagram, Web und Speisekarte. InstaFlow AI Pro plant Inhalte mit redaktioneller Kalender."
      }
    ],
    "ctaTitle": "Cocktailkunst mit echter Marge und professionellem Branding.",
    "ctaSubtitle": "Beginnen Sie mit dem Onboarding von 2 Minuten. Mitgliederplan für 10 € pro Monat mit 10.000 Krediten für alle Agenten.",
    "seo": {
      "title": "KI für Bar und Cocktail: Signature Cocktails, Preisberechnung und Branding | AI Chef Pro",
      "description": "KI Suite für Bars & Cocktail: Bar & Lounge AI+, Food Pairing AI, Cocktail Kalkulation, Karten, HACCP und visuelle Marken. Start heute.",
      "keywords": "KI für Bar Cocktail, Cocktail kalkülier, Software und Restaurants, KI Bartender, KI Barman, Cocktail Bar der Autor, Bar Management KI",
      "ogImage": "https://aichef.pro/og/use-cases/bar-cocktails.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Bar zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten «Wer sind Sie?», einem Konversations-Onboarding von 2 Minuten, in dem Sie erzählen, welche Art von Bar Sie betreiben (Cocktail, Weinbar, Brauerei, Pub, Bar), Ihre Stadt und Ihre Karte. Jeder Agent – von Bar & Lounge AI+ bis Kit de Escandallos Pro – antwortet auf Ihre Bar und Ihren Markt zugeschnitten.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrer Bar nutzen werden",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Exercise Concepts",
        "description": "Hauptagent: Pubs, Cocktail, Wein Bars, Sports Bars, Trink Bars."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Cocktails mit Rezept + CSV Berechnung."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Wissenschaftliche Kombinationen für Signature Cocktails und Pairing mit Tapas."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Fermentationen für die angewandte Cocktail Welt: Kombucha, Aufgüsse, Lactofermente."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftliche",
        "description": "Für Bars mit Tapas und leichte Küche additionally zu Cocktails."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für technische Zutaten aus dem Sosa-Katalog."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für t Spoon Labor Katalog für Cocktail Techniken."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Toolkit",
        "description": "Automatische Identifizierung von Allergien in Cocktails und Tapas."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Toolkit",
        "description": "Präzise Analyse von Abfällen bei Säften, Garnishes und Glasen."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Gastro-Fotografie für Cocktails: Web, Social Media und Karte."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und Social Media",
        "description": "Virale Instagram-Inhalte für die Cocktailbar mit Kammer Redaktionsk-"
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Gastro-Wissen",
        "description": "300+ Prompts für Cocktail Storytelling, Presse kommunikation und Schulung."
      }
    ],
    "metrics": [
      {
        "value": "×4",
        "label": "Kartendelement Cocktailkart"
      },
      {
        "value": "+5 pp",
        "label": "Marge nach professionellem Nachtrag"
      },
      {
        "value": "×3",
        "label": "Insta-Engagement mit GastroIMG"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Cocktails mit Taschenrechner und Serviette",
        "Getränke Karten ohne professionelles Storytelling für das Service Team",
        "Verluste bei Vendering und Glaswaren ohne Rückverfolgbarkeit",
        "Improvisiertes visuelle Branding auf Instagram mit Handy-Fotos",
        "Kein systematischer Zugriff auf die internationalen Trends in Cocktail"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Bar & Lounge AI+ + Kreativküche + Kit de Escandallos Pro schließen Bar Karten in 2 Stunden",
        "Professionelle Storytelling für jeden Cocktail ready für Service & Presse",
        "Kontrollierte Abfälle mit Lebensmittelabfälle AI und Close",
        "GastroIMG +InstaFlow erzeugen Profi-Fotos und virale Posts",
        "Sonar Deep Research liefert internationale Trends und Referenzen"
      ]
    },
    "galleryTitle": "So funktioniert eine professionelle Cocktailbar",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Hauptbar, Shaker-Technik, finaler Cocktail, Vorbereitung von Garnishes, Ausgießtechnik und Service.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-bar-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-shaker.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-cocktail.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-pour.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-team.jpg"
    ]
  },
  "catering-eventos": {
    "h1": "KI für Catering und Veranstaltungen",
    "heroSubtitle": "Kalkulieren Sie pro Veranstaltung, planen Sie Produktion im großen Maßstab, verwalten Sie Logistik und HACCP außer Haus mit einer Suite von KI-Agenten, die auf professionelles Catering, Hochzeiten, Firmen und Cocktails spezialisiert sind.",
    "heroTagline": "Veranstaltungen mit Gewinn, ohne Chaos",
    "badge": "Für Catering- und Eventunternehmen",
    "painsTitle": "Was ein Catering unbedingt lösen muss",
    "pains": [
      "Menüs mit stark schwankender Gästezahl (50, 200, 500) kalkulieren, wenn die Preise jede Woche wechseln",
      "Produktion und Mise en Place in großem Maßstab aus der Zentralküche planen",
      "Logistik, Kühltransport und Aufbau beim Kunden koordinieren",
      "HACCP und Rückverfolgbarkeit außerhalb des festen Standorts, an fremden Orten und in Fahrzeugen sicherstellen",
      "Firmenkunden mit professionellen Angeboten gewinnen, die Verträge mit höherem Umsatz abschließen",
      "Mehrere Wochenendveranstaltungen gleichzeitig ohne Abstimmungsprobleme managen"
    ],
    "featuresTitle": "Wie AI Chef Pro bei Catering und Veranstaltungen hilft",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Spezialisierter Agent für Catering und gastronomische Veranstaltungen: Hochzeiten, Firmen, Cocktails und Galas mit professionellem Wissen."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche + Food Pairing AI",
        "description": "Ideenfindung für Veranstaltungsmenüs. Kreativküche liefert Rezept + CSV-Kalkulation, bereit für das Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Veranstaltung",
        "description": "Kit de Escandallos Pro: Sie laden die CSV mit Ihren tatsächlichen Preisen hoch, passen die Gästezahl an und erhalten sofort die Marge."
      },
      {
        "icon": "Layers",
        "title": "Calcula Pax",
        "description": "Portionsrechner, der Rezepte in Sekunden auf 50, 200, 500 oder 1000 Gäste skaliert."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Catering",
        "description": "Vorlagen: zentrale Produktion, Kühltransport, Aufbau vor Ort, Service und Abbau."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC außer Haus",
        "description": "Rückverfolgbarkeit bei Transport, fremden Standorten und externem Service mit mobilen Aufzeichnungen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "KI-gastronomische Fotografie für Angebote an Firmenkunden und Eventgalerien."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergen-ID",
        "description": "Automatische Identifizierung, entscheidend für Veranstaltungen mit unterschiedlichen Ernährungsprofilen."
      },
      {
        "icon": "Search",
        "title": "BlogPost SEO Gen+ + Keyword Discovery AI+",
        "description": "Organische Gewinnung von Unternehmen, die Catering in Ihrer Region suchen."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem Cateringunternehmen mit AI Chef Pro",
    "workflow": [
      "08:30 · Catering AI+ – der Agent hilft Ihnen, das vorgeschlagene Menü für eine Hochzeit mit 180 Gästen gemäß Kundenbriefing abzuschließen.",
      "09:30 · Kreativküche – Sie entwickeln die 12 Gerichte des Menüs mit Rezept und CSV-Kalkulation mit Referenzpreisen.",
      "10:30 · Calcula Pax + Kit de Escandallos Pro – Sie skalieren auf 180 Gäste, laden die CSV mit Ihren tatsächlichen Preisen hoch und validieren die Marge.",
      "12:00 · GastroIMG Gen+ – Sie generieren Fotos der Gerichte für die Präsentation an den Kunden.",
      "14:00 · Kundentermin – Angebot mit professioneller Präsentation abgeschlossen, statt der früheren Word-Vorlagen.",
      "16:00 · Kit de Tareas Catering – Sie planen zentrale Produktion, Transport, Aufbau und Service für die Samstagsveranstaltung.",
      "18:00 · Pack APPCC – Sie bereiten Temperaturaufzeichnungen für Transport und Rückverfolgbarkeit am fremden Ort vor.",
      "20:00 · Briefing an das Team – Sie erstellen ein Briefing für Produktion, Transport, Aufbau und Service aus einer einzigen Quelle."
    ],
    "productsTitle": "Vorlagen und Kits zum Download für Catering",
    "productIds": [
      "kit-tareas-catering",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Wir schließen Veranstaltungen in einem Drittel der Zeit ab. Die Kalkulationen pro Veranstaltung passen sich detailliert an die Gästezahl an, die Logistikvorlagen sind Gold wert und die Angebote mit professioneller Fotografie sichern uns Firmenverträge, die uns vorher entgingen. Im ersten Quartal allein durch bessere Kalkulation +5 Prozentpunkte Marge.",
    "testimonialAuthor": "Sara Pérez",
    "testimonialRole": "Cateringunternehmen für Firmen und Hochzeiten (200 Veranstaltungen pro Jahr)",
    "faqTitle": "Häufige Fragen von Cateringunternehmen",
    "faqs": [
      {
        "q": "Funktioniert es für Boutique-Catering oder große Unternehmen?",
        "a": "Für beides. Von Boutique-Caterings mit 50 Gästen pro Monat bis zu Unternehmen mit über 1000 Services pro Monat und Veranstaltungen mit 2000 Gästen."
      },
      {
        "q": "Abgedeckt sind Hochzeiten, Firmen und Cocktails?",
        "a": "Ja. Catering AI+ und das Kit de Tareas Catering haben spezifische Vorlagen für alle drei Formate sowie für Galas/Sonderveranstaltungen."
      },
      {
        "q": "Gibt es spezifisches HACCP außerhalb des festen Standorts?",
        "a": "Ja. Das Pack APPCC hat Vorlagen, die auf Produkte zugeschnitten sind, die im Rucksack, mit dem Motorrad, im Kühltransporter oder aus der Zentralküche transportiert werden, einschließlich Rückverfolgbarkeit am fremden Ort."
      },
      {
        "q": "Erstellt es Geschäftsangebote für Unternehmen?",
        "a": "Ja. Catering AI+ + GastroIMG Gen+ + Pro Prompts eBook ermöglichen die Erstellung professioneller Angebote mit gastronomischer Fotografie und Storytelling."
      },
      {
        "q": "Wie hilft es mir, Firmenkunden zu gewinnen?",
        "a": "BlogPost SEO Gen+ + Keyword Discovery AI+ + MenuDish Local SEO arbeiten zusammen, um Unternehmen zu gewinnen, die über organische Google-Suchen nach Catering in Ihrer Region suchen."
      }
    ],
    "ctaTitle": "Catering mit echtem Gewinn und ohne Chaos.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Catering und Veranstaltungen: Hochzeiten, Firmen und Cocktails | AI Chef Pro",
      "description": "KI-Suite für professionelle Cateringunternehmen: Catering AI+, Kalkulation pro Veranstaltung, Produktion in großem Maßstab, HACCP außer Haus und Geschäftsangebote. Starten Sie noch heute.",
      "keywords": "KI Catering, Catering Software, Eventkalkulation, KI Catering Management, KI Hochzeitscatering, KI Firmencatering, Gastronomie-Event-Software, Catering Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/catering-eventos.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Catering personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten «Wer sind Sie?», einem 2-minütigen Conversational-Onboarding, bei dem Sie erzählen, welche Art von Catering Sie betreiben (Hochzeiten, Firmen, Cocktails, Galas), Durchschnittsgröße, Stadt und Jahresvolumen. Jeder Agent – von Catering AI+ bis zum Kit Plan Financiero – antwortet angepasst an Ihre Veranstaltungsart, Ihren Maßstab und Ihren realen Markt.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Catering nutzen werden",
    "apps": [
      {
        "name": "Catering AI+",
        "category": "Geschäftskonzepte",
        "description": "Hauptagent: Hochzeiten, Firmen, Cocktails und Galas mit professioneller Basis."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Veranstaltungsmenüs mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Kombinationen von Zutaten und Pairings für Cocktails und Canapés."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Event- und Bankettdesserts mit professioneller Technik."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Für avantgardistische Canapés mit Fermenten und innovativen Techniken."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools und Utilities",
        "description": "Portionsrechner, der Rezepte auf 50, 200 oder 500 Gäste skaliert."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Kritische Allergenidentifizierung bei Veranstaltungen mit vielen Gästen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Präzise Daten für Produktion im industriellen Maßstab."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und Social Media",
        "description": "Blogbeiträge zur Gewinnung von Unternehmen über organische Suchen."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und Social Media",
        "description": "SEO-Beschreibungen zur Verbesserung des Rankings der Catering-Website."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-gastronomische Fotografie für Angebote und Webgalerie."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Für technische Zutaten in Cocktails und Canapés."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "Geschwindigkeit beim Abschluss von Angeboten"
      },
      {
        "value": "+5 pp",
        "label": "Marge nach realer Kalkulation"
      },
      {
        "value": "−50 %",
        "label": "Zeit für Logistik"
      },
      {
        "value": "11+",
        "label": "Agenten für Ihr Catering"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Menü mit Kunden abschließen: halber Nachmittag mit Taschenrechner",
        "Produktion für 200 Gäste ohne präzise Skalierung",
        "HACCP außer Haus improvisiert",
        "Angebote mit Word-Vorlagen und Stockfotos",
        "Briefing an das Team auf losen Blättern"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Menü in 30 Minuten mit validierter Marge abschließen",
        "Produktion skaliert mit Calcula Pax und Lebensmittelabfälle AI",
        "HACCP mit Rückverfolgbarkeit bei Transport und fremden Standorten",
        "Angebote mit GastroIMG Gen+ und professionellem Storytelling",
        "Zentrales Briefing mit Kit de Tareas Catering"
      ]
    },
    "galleryTitle": "So funktioniert professionelles Catering",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren werden: zentrale Produktion, elegante Veranstaltungen, Canapés, Firmen-Cocktails, Aufbau und Service.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-canapes.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-corporate.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-cocktail.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-setup.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-banquet.jpg"
    ]
  },
  "hotel-completo": {
    "h1": "KI für das gesamte Hotel (F&B + Housekeeping)",
    "heroSubtitle": "Verwalten Sie Frühstück, Restaurant, Zimmerservice, Bankette, Bar und Housekeeping mit einer Suite von KI-Agenten, die für F&B-Manager und Hoteldirektionen entwickelt wurde.",
    "heroTagline": "Die gesamte Hotelbetriebsabläufe in einem einzigen System koordiniert",
    "badge": "Für Hotel-F&B-Manager",
    "painsTitle": "Was ein Hotel-F&B-Manager unbedingt lösen muss",
    "pains": [
      "Mehrere Verkaufsstellen gleichzeitig koordinieren: Frühstücksbuffet, À-la-carte-Restaurant, Lobby-Bar, Zimmerservice und Bankette",
      "Große Teams mit rotierenden 24/7-Schichten unter Einhaltung von Tarifvertrag und Pausen führen",
      "APPCC über mehrere Küchenbereiche verteilt aufrechterhalten und an den F&B-Direktor konsolidieren",
      "Konsolidiertes Reporting an den Hoteldirektor und an die Zentrale mit KPIs pro F&B-Linie",
      "Saisonale Karten für mehrere Outlets entwerfen, ohne dass das Team im Papierkram untergeht",
      "Hochzeitsbankette und Firmenevents mit dem regulären F&B-Betrieb koordinieren"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem kompletten Hotel hilft",
    "features": [
      {
        "icon": "Hotel",
        "title": "Kit de Tareas Hotel",
        "description": "Spezifische Vorlagen für Frühstücksbuffet, Restaurant, Lobby-Bar, Zimmerservice, Bankette und Housekeeping in einem einzigen Dokumentationssystem."
      },
      {
        "icon": "ChefHat",
        "title": "Executive Chef Pro",
        "description": "Standardisierung von Rezepten und Rezeptblättern in allen Hotel-Outlets. Gleiches Gericht, gleiche Qualität in Restaurant, Zimmerservice und Bankett."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulationen pro Verkaufsstelle",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet diese mit Ihren realen Preisen und trennt die Marge pro Outlet."
      },
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Für die Gestaltung und Produktion von Hochzeitsbanketten, Firmenevents und besonderen Hotelveranstaltungen."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Für die Cocktailkunst der Lobby-Bar, Weine im Restaurant und Spirituosen mit professioneller Kalkulation."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Dienstpläne für große 24/7-Teams mit rotierenden Schichten unter Einhaltung des landesspezifischen Tarifvertrags. Inklusive Mitarbeiteressen AI."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC corporativo",
        "description": "APPCC nach Küchenbereich verteilt, aber in einem einzigen Dashboard für den F&B-Direktor konsolidiert."
      },
      {
        "icon": "BarChart3",
        "title": "Kit Plan Financiero",
        "description": "Dashboard mit KPIs pro Verkaufsstelle: Frühstück, Restaurant, Bar, Zimmerservice, Bankette. Auslastungs- und Produktivitätskennzahlen."
      },
      {
        "icon": "BriefcaseBusiness",
        "title": "Profi Restaurantmanager",
        "description": "Für die Manager jedes Outlets mit konsolidiertem Reporting an den F&B-Manager des Hotels."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Hotel-F&B-Managers mit AI Chef Pro",
    "workflow": [
      "07:00 · Frühstückseröffnung – das Team startet das Buffet mit der Checkliste des Kit de Tareas Hotel; Sie prüfen das Auslastungs-Dashboard des Hotels und passen die Mise en Place an.",
      "09:30 · Catering AI+ – Sie bereiten das Hochzeitsbankett am nächsten Samstag vor: Menü, Kalkulation und Produktion für 220 Gäste.",
      "11:00 · Executive Chef Pro – Sie aktualisieren das Rezeptblatt des neuen Restaurantgerichts, das mit derselben Standardisierung auf Zimmerservice und Bankettmenü übertragen wird.",
      "13:00 · Mittagsservice – À-la-carte-Restaurant + Lobby-Bar + Zimmerservice aktiv. Das Team koordiniert mit spezifischen Vorlagen für jeden Outlet.",
      "15:30 · Kit Plan Financiero – Sie exportieren KPIs pro Outlet für das Quartal für das Meeting mit der Hoteldirektion.",
      "17:00 · Bar & Lounge AI+ – Sie entwerfen die neue Cocktailkarte für die Lobby-Bar mit professioneller Kalkulation.",
      "19:30 · Dienstplan nächste Woche – Kit Gestión de Personal mit rotierenden Schichten unter Einhaltung des Tarifvertrags, Stundenkontrolle und generiertem Mitarbeiteressen AI.",
      "23:00 · APPCC konsolidiert – Registrierungen der 6 Verkaufsstellen unterschrieben und exportiert, Bericht an den F&B-Direktor und an die Zentrale als PDF gesendet."
    ],
    "productsTitle": "Herunterladbare Vorlagen und Kits für Hotels",
    "productIds": [
      "kit-tareas-hotel",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Die Koordination von 6 F&B-Verkaufsstellen in einem Hotel mit 200 Zimmern war ein ständiger Albtraum. AI Chef Pro hat uns alles geordnet. Das Kit de Tareas Hotel ist Gold wert und das Reporting an den Hoteldirektor erfolgt jetzt automatisch als PDF. Wir haben den RevPASH des Restaurants in 4 Monaten um 12 % gesteigert, allein durch bessere Kontrolle.",
    "testimonialAuthor": "Cristina Núñez",
    "testimonialRole": "F&B-Manager, 4-Sterne-Hotel mit 200 Zimmern",
    "faqTitle": "Häufige Fragen von F&B-Managern",
    "faqs": [
      {
        "q": "Funktioniert das für ein Boutique-Hotel oder eine große Kette?",
        "a": "Beides. Die Vorlagen skalieren von Hotels mit 30 Zimmern bis zu Ketten mit Hunderten von Objekten. Für große Ketten gibt es ein Unternehmens-Onboarding."
      },
      {
        "q": "Deckt es neben F&B auch Housekeeping ab?",
        "a": "Ja. Das Kit de Tareas Hotel enthält spezifische Housekeeping-Vorlagen zusätzlich zu den 5 F&B-Verkaufsstellen."
      },
      {
        "q": "Lässt es sich in unser PMS oder Opera integrieren?",
        "a": "Exportieren Sie Excel, PDF und CSV, die mit den meisten PMS und Hotelsystemen kompatibel sind. Die Daten können am Ende jeder Schicht oder jedes Arbeitstags manuell integriert werden."
      },
      {
        "q": "Gibt es einen Unternehmensplan für Hotelketten?",
        "a": "Ja. Ab einer bestimmten Anzahl von Objekten gibt es Unternehmenspläne mit personalisiertem Onboarding, konsolidierten Dashboards pro Kette und Prioritäts-Support."
      },
      {
        "q": "Wie verwaltet es Bankette und besondere Veranstaltungen?",
        "a": "Catering AI+ ist in das Kit de Tareas Hotel integriert, sodass Bankette (Hochzeiten, Firmenevents) mit dem regulären F&B-Betrieb koordiniert werden, ohne Produktion oder Team zu kollidieren."
      },
      {
        "q": "Und die Kostenkontrolle pro Outlet?",
        "a": "Mit dem Kit Plan Financiero können Sie Food Cost, Produktivität und Marge getrennt für Frühstück, Restaurant, Lobby-Bar, Zimmerservice und Bankette analysieren. Das gibt eine echte Sicht darauf, welcher Outlet sich lohnt und welcher nicht."
      }
    ],
    "ctaTitle": "Ihr Hotel-F&B koordiniert und ohne Chaos.",
    "ctaSubtitle": "Sprechen Sie mit uns für ein persönliches Onboarding oder starten Sie mit dem Mitgliederplan: 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "KI für das gesamte Hotel (F&B + Housekeeping): Restaurant, Bar, Bankette | AI Chef Pro",
      "description": "KI-Suite für Hotel-F&B-Manager: Frühstücksbuffet, Restaurant, Lobby-Bar, Zimmerservice, Bankette und Housekeeping mit spezialisierten Agenten. Starten Sie noch heute.",
      "keywords": "KI Hotel F&B, F&B Manager KI, F&B Hotelsoftware, Hotelmanagement KI, Zimmerservice KI, Hotelbankett KI, Housekeeping-Software, Hotelrestaurant-Management KI, F&B Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/hotel-completo.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Hotel zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational-Onboarding, bei dem Sie erzählen, welche Art von Hotel Sie führen (Boutique, 4 Sterne, große Kette, All-inclusive), wie viele Zimmer, welche F&B-Outlets Sie betreiben und in welchem Umfang. Ab diesem Moment reagiert jeder Agent – vom Executive Chef Pro bis zum Kit Plan Financiero – angepasst an die Realität Ihres Hotels: Gästetyp, Auslastungsquote und tatsächlicher Betrieb. Das ist kein Formular: Es ist ein kurzes Gespräch, das die Suite für einen Hotel-F&B-Manager wirklich nützlich macht.",
    "appsTitle": "Die KI-Agenten, die Sie als F&B-Manager nutzen werden",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standardisierung von Rezepten und Rezeptblättern in allen Hotel-Outlets."
      },
      {
        "name": "Profi Restaurantmanager",
        "category": "Gastro Profile Pro",
        "description": "Assistent für die Manager jedes Outlets mit konsolidiertem Reporting an den F&B-Manager."
      },
      {
        "name": "Catering AI+",
        "category": "Geschäftskonzepte",
        "description": "Für Hochzeitsbankette, Firmenevents und Galas im Hotel."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Für die Cocktailkunst der Lobby-Bar, Weine im Restaurant und Spirituosen."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Für das À-la-carte-Restaurant des Hotels und Casual-Optionen im Zimmerservice."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Gerichteentwicklung für alle Outlets mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Hotel-Desserts: Frühstücksbuffet, Restaurant, Zimmerservice und Bankette."
      },
      {
        "name": "Mitarbeiteressen AI",
        "category": "Gastro Profile Pro",
        "description": "Generator für Mitarbeitermenüs für große 24/7-Teams."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Rezept, entscheidend in internationalen Hotels."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Präzise Daten zu Abfällen und Erträgen für die Multi-Outlet-Kontrolle."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Gastro-Fotografie für die Hotel-Website, Zimmerservice-Menü und Bankette."
      }
    ],
    "metrics": [
      {
        "value": "+12 %",
        "label": "RevPASH in 4 Monaten"
      },
      {
        "value": "6",
        "label": "koordinierte Verkaufsstellen"
      },
      {
        "value": "×5",
        "label": "Reporting-Geschwindigkeit an den Direktor"
      },
      {
        "value": "11+",
        "label": "Agenten für Ihr Hotel"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "6 F&B-Outlets mit 6 verschiedenen Systemen: Frühstück, Restaurant, Bar, Zimmerservice, Bankette und Housekeeping ohne Verbindung",
        "APPCC auf Papier gedruckt, in jeder Hotelküche verstreut, Problem bei Inspektionen",
        "Hochzeitsbankette kollidieren mit der Produktion des regulären Restaurants und des Zimmerservice",
        "Reporting an den F&B-Direktor und an die Zentrale mit verstreuten und unstrukturierten Dateien",
        "24/7-Dienstpläne manuell in Excel mit 50+ Mitarbeitern"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Kit de Tareas Hotel mit spezifischen Vorlagen pro Outlet, alles in einem einzigen System koordiniert",
        "APPCC im Dashboard konsolidiert: Registrierungen vom Handy, bereit für Inspektion und Zentrale",
        "Bankette mit Catering AI+ integriert, das die Produktion des regulären F&B-Betriebs respektiert",
        "Reporting an den Direktor und die Zentrale direkt als PDF aus dem Kit Plan Financiero",
        "Dienstpläne mit Kit Gestión de Personal: 24/7-Schichten unter Einhaltung des Tarifvertrags ohne Abweichungen"
      ]
    },
    "galleryTitle": "So funktioniert das F&B eines kompletten Hotels",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Restaurant, Frühstücksbuffet, Bankett, Lobby-Bar, Zimmerservice und F&B-Briefing mit der Küche.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-breakfast.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-banquet.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-bar.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-roomservice.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-fbteam.jpg"
    ]
  },
  "heladeria": {
    "h1": "KI für handwerkliche Eisdielen",
    "heroSubtitle": "Kalkulation pro Sorte mit echten Kosten für Milch, Obst und Nüsse, planen Sie saisonale Produktion und erfassen Sie professionelles Branding mit einer Suite von KI-Agenten, die auf handwerkliche Eisdielen spezialisiert sind.",
    "heroTagline": "Eis mit echter Marge und ohne Papierkram",
    "badge": "Für handwerkliche Eisdielen und Gelaterien",
    "painsTitle": "Was eine handwerkliche Eisdiele unbedingt lösen muss",
    "pains": [
      "Komplexe Kalkulationen mit Milch, Sahne, frischem Obst, Nüssen und professionellen Pasten, die eine Berechnung pro kg und pro Kugel erfordern",
      "Hohe Verluste in der Produktionsstätte (Eismaschine, Schockfroster) und in der Vitrine (lange Exposition, Rotation) ohne echte Kontrolle",
      "APPCC-Rückverfolgbarkeit bei empfindlichen Produkten: Milch, Ei in einigen Basen, Nüsse mit Allergenen und kritische Temperaturen",
      "Extreme Saisonalität: Hochsaison von Mai bis September, Wintertal, das mit Torten und Desserts rentabel gemacht werden muss",
      "Sich in einem umkämpften Gebiet mit eigenen Sorten, visuellem Branding der Vitrine, Verpackung und sozialen Medien differenzieren",
      "Aufträge für Eistorten und maßgeschneiderte Desserts mit Marge gewinnen, während der tägliche Servicebetrieb gemanagt wird"
    ],
    "featuresTitle": "Wie AI Chef Pro in der handwerklichen Eisdiele hilft",
    "features": [
      {
        "icon": "IceCream",
        "title": "Kreative Gelateria",
        "description": "Spezialisierter Agent für handwerkliche Eisdielen: weiße, gelbe, Fruchtbasen, Sorbets, Ausbalancierung von Zucker, Feststoffen und Fetten für optimale Textur."
      },
      {
        "icon": "Cake",
        "title": "Kreative Patisserie",
        "description": "Für Eistorten, Halbgefrorenes, Löffeldesserts und Kombinationen aus Eis + Biskuit, die im Wintertal den Durchschnittsbon erhöhen."
      },
      {
        "icon": "Cookie",
        "title": "Kreative Schokolade",
        "description": "Für Glasuren, Eispralinen, Pralinen und fortgeschrittene Kombinationen aus Eis + Schokolade."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Sorte",
        "description": "Kreative Gelateria liefert Rezept + CSV-Kalkulation mit technischem Abgleich (Zucker, Feststoffe, Fette); Kit de Escandallos Pro verwaltet es mit echter Marge pro kg, pro Kugel und pro Waffel."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Heladería",
        "description": "Vorlagen: Vorbereitung Eismaschine, Schockfrosten, Auffüllen der Vitrine, Temperaturkontrolle, Sortenrotation, Schließung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Eisdiele",
        "description": "Rückverfolgbarkeit von Milch, frischem Obst, Nüssen mit Allergenen und kritischen Temperaturen in Kühlung, Eismaschine und Vitrine."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Saisonale Planung mit wichtigen Spitzen: Muttertag, Frühling, Sommer, Valentinstag und Weihnachts-Eistorten. Redaktionskalender für die Vitrine."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "KI-Lebensmittelfotografie + Inhalte für Instagram: Die handwerkliche Eisdiele lebt von der visuellen Wirkung der Behälter und Waffeln."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients AI",
        "description": "Assistent für den Sosa-Katalog für professionelle Texturen, Neutrale, Stabilisatoren und konzentrierte Pasten für Eisdielen."
      }
    ],
    "workflowTitle": "Ein echter Tag in einer handwerklichen Eisdiele mit AI Chef Pro",
    "workflow": [
      "07:00 · Öffnung – Checkliste Kit de Tareas Heladería: Überprüfung der Kühlung, Schockfrosten der am Vortag vorbereiteten Mischungen, Vorbereitung der Eismaschine.",
      "08:30 · Kreative Gelateria – Sie entwickeln eine neue saisonale Sorte (rote Früchte mit Balsamico). Kreativküche liefert Rezept + CSV-Kalkulation mit technischem Abgleich.",
      "09:30 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren echten Preisen für saisonales Obst und lokale Milch hoch und validieren die Marge pro kg und pro Kugel.",
      "11:00 · Tagesproduktion – Sie lassen die Mischungen durch die Eismaschine laufen, schockfrosten auf -18 °C, etikettieren mit APPCC.",
      "13:30 · Auffüllen der Vitrine mit professionellen Etiketten, Kontrolle der Expositionsverluste pro Sorte.",
      "16:00 · Kreative Patisserie – Sie entwickeln eine Eistorte zum Muttertag mit Pistazien-Halbfrosten, Biskuitboden und Glasur. CSV-Kalkulation fertig.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren das Referenzbild der neuen Sorte und die Instagram-Posts für den Launch.",
      "21:00 · Schließung – gründliche Reinigung, APPCC unterschrieben, Planung der Mischungen, die heute Nacht für morgen schockgefrostet werden."
    ],
    "productsTitle": "Vorlagen und herunterladbare Kits für Eisdielen",
    "productIds": [
      "kit-tareas-heladeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Wir sind von losen Blättern zu einem System übergegangen. Mit Kreative Gelateria balancieren wir Zucker und Feststoffe mit technischem Know-how aus, und das Kit de Escandallos Pro bestätigt mir die echte Marge pro Kugel und pro kg mit den aktuellen Fruchtpreisen. Der Abfall ist in 3 Monaten um 40 % gesunken, und wir haben entdeckt, dass zwei historische Sorten nicht rentabel waren.",
    "testimonialAuthor": "Laura Costa",
    "testimonialRole": "Inhaberin, handwerkliche Eisdiele mit eigener Produktionsstätte",
    "faqTitle": "Häufig gestellte Fragen für Eisdielen",
    "faqs": [
      {
        "q": "Funktioniert es für eine kleine Eisdiele, italienische Gelateria oder Kette?",
        "a": "Für alle drei. Die Vorlagen skalieren von der familiengeführten Eisdiele mit einem Standort bis zur Kette mit mehreren Filialen und zentraler Produktionsstätte. Die Methodik ist dieselbe: ausbalanciertes Rezept → CSV-Kalkulation → echte Marge."
      },
      {
        "q": "Deckt es den technischen Abgleich der Basen ab (Zucker, Feststoffe, Fette)?",
        "a": "Ja. Kreative Gelateria denkt wie ein professioneller Eismacher: Zuckerabgleich mit Saccharose, Dextrose und Invertzucker; Gesamtfeststoffe und Fette nach technischer Norm; Gleichgewicht, um Kristallisation zu vermeiden und Cremigkeit zu erhalten."
      },
      {
        "q": "Wie managen wir die starke Saisonalität der Eisdiele?",
        "a": "Gastro Calendar plant die Spitzen im Voraus (Muttertag, Sommer, Valentinstag, Weihnachten mit Eistorten) und das Wintertal mit Torten, Halbgefrorenem und Löffeldesserts, um den Durchschnittsbon zu halten. Das Kit Plan Financiero projiziert den realistischen saisonalen Cashflow."
      },
      {
        "q": "Gibt es eine Kontrolle der Verluste in Produktionsstätte und Vitrine?",
        "a": "Ja. Lebensmittelabfälle AI liefert Daten pro Prozess (Eismaschine, Schockfrosten, lange Exposition in der Vitrine, Sortenrotation). Sie werden in die Kalkulation des Kit de Escandallos Pro integriert, sodass die echten Kosten die Verluste widerspiegeln, nicht nur die Rohzutat."
      },
      {
        "q": "Erzeugt es Inhalte für Vitrine, soziale Medien und Google Maps?",
        "a": "Ja. GastroIMG Gen+ erzeugt professionelle Referenzbilder jeder Sorte für Vitrine, Web und soziale Medien; InstaFlow AI Pro plant Instagram mit Redaktionskalender; MenuDish Local SEO erfasst lokale Kunden, die nach „Eisdiele in meiner Nähe“ suchen. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie selbst mit Ihrem Behälter und echtem Anrichten."
      }
    ],
    "ctaTitle": "Ihre Eisdiele mit klarer Marge und professionellem Branding.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für die Nutzung aller Agenten.",
    "seo": {
      "title": "KI für handwerkliche Eisdielen: Kalkulation pro Sorte, Saisonalität und Branding | AI Chef Pro",
      "description": "KI-Suite für handwerkliche Eisdielen: Kreative Gelateria, Kalkulation pro Sorte mit technischem Abgleich, APPCC, saisonale Planung und visuelles Branding. Starten Sie noch heute.",
      "keywords": "KI Eisdiele, Software Eisdiele, Eiskalkulation, handwerkliche Eisdiele KI, technischer Abgleich Eis, Gelateria KI, Eisdiele Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/heladeria.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Eisdiele personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational-Onboarding, bei dem Sie erzählen, welche Art von Eisdiele Sie betreiben (italienische Gelateria, spanische handwerkliche Eisdiele, Eisdiele mit eigener Produktionsstätte oder ohne, gemischt mit Konditorei), Teamgröße, Stadt und Stil. Jeder Agent – von Kreative Gelateria bis Gastro Calendar – antwortet angepasst an Ihr Produkt, Ihren Markt und Ihre reale Betriebsweise.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrer Eisdiele nutzen werden",
    "apps": [
      {
        "name": "Kreative Gelateria",
        "category": "Kulinarische Kreativität",
        "description": "Spezialisierter Agent für handwerkliche Eisdielen mit technischem Abgleich von Basen, Zucker, Feststoffen und Fetten."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Eistorten, Halbgefrorenes, Löffeldesserts und Kombinationen aus Eis + Biskuit."
      },
      {
        "name": "Kreative Schokolade",
        "category": "Kulinarische Kreativität",
        "description": "Glasuren, Eispralinen, Pralinen und fortgeschrittene Kombinationen mit Schokolade."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Sorten und Rezepten mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog: Neutrale, Stabilisatoren, konzentrierte Pasten und professionelle Texturen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Präzise Daten zu Verlusten in Eismaschine, Schockfroster und Vitrinen-Exposition."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Sorte: Milchprodukte, Nüsse, Gluten, Ei."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Lebensmittelfotografie als Referenz für Vitrine, Web und soziale Medien."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit Redaktionskalender: Die Eisdiele lebt von der visuellen Wirkung."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die bei Google und Maps nach „Eisdiele in meiner Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Saisonale Planung: Muttertag, Sommer, Valentinstag, Weihnachts-Eistorten."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und soziale Medien",
        "description": "Pinterest erfasst stabilen organischen Traffic für Eistorten und Halbgefrorenes."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach Kalkulation der Sorten"
      },
      {
        "value": "−40 %",
        "label": "Verluste in Produktionsstätte und Vitrine"
      },
      {
        "value": "×3",
        "label": "Instagram-Engagement mit GastroIMG"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Eisdiele"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Kalkulationen ohne technischen Abgleich, Sorten kristallisieren oder verlieren Cremigkeit, ohne zu wissen warum",
        "Verluste in Eismaschine, Schockfroster und Vitrine ohne echte Rückverfolgbarkeit",
        "Improvisierte Vitrine und soziale Medien: Handyfotos, ohne Kontinuität",
        "Reaktive Saisonalität: Der Winter senkt den Bon ohne Alternativen",
        "APPCC auf Papier, verstreut in der Produktionsstätte"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Professionelle Kalkulationen pro Sorte mit technischem Abgleich und echter Marge pro Kugel und pro kg",
        "Verluste kontrolliert mit Lebensmittelabfälle AI und spezifischen Eisdielen-Vorlagen",
        "GastroIMG Gen+ + InstaFlow AI Pro erzeugen stabilen und professionellen visuellen Inhalt",
        "Gastro Calendar plant Spitzen und Täler mit Eistorten, Halbgefrorenem und Löffeldesserts",
        "APPCC vom Handy mit Protokollen, die für Inspektionen bereit sind"
      ]
    },
    "galleryTitle": "Wie eine handwerkliche Eisdiele funktioniert",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Vitrine, Eismaschine, Produktionsstätte, Sorten, Waffeln und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-heladeria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-vitrine.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-mantecadora.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-flavors.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-conos.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-team.jpg"
    ]
  },
  "chocolateria": {
    "h1": "KI für Schokoladenmanufaktur und Pralinenmanufaktur",
    "heroSubtitle": "Kalkulation pro Praline mit echten Kakaokosten und Manufaktur-Stundensatz, planen Sie saisonale Produktion und sichern Sie sich professionelles Branding mit einer Suite spezialisierter KI-Agenten für handwerkliche Schokoladenherstellung.",
    "heroTagline": "Praline mit echter Marge und ohne Papierkram",
    "badge": "Für handwerkliche Schokoladenmanufakturen und Pralinenmanufakturen",
    "painsTitle": "Was eine Schokoladenmanufaktur unbedingt lösen muss",
    "pains": [
      "Kakao mit volatilen Preisen, die die echten Kosten jede Woche ohne Vorwarnung ändern und ständige Neuberechnung der Kalkulationen erzwingen",
      "Verluste in der Manufaktur (fehlgeschlagenes Temperieren, schlecht ausgeformte Formen, Verschnitt) und in der Vitrine (Rotation, lange Auslage)",
      "Extreme Saisonalität: Weihnachten, Valentinstag, Ostern, Dreikönigskuchen konzentrieren einen hohen Prozentsatz des Jahresumsatzes",
      "APPCC-Rückverfolgbarkeit bei empfindlichen Produkten: Kakao, Milchprodukte, Nüsse, Alkohol und kritische Temperaturen in jedem Schritt",
      "Sich in einem umkämpften Gebiet mit Autoren-Pralinen, Premium-Verpackung und visuellem Marken-Storytelling differenzieren",
      "Firmenaufträge und Hochzeiten mit Marge gewinnen, während Sie die tägliche Schokoladenmanufaktur managen"
    ],
    "featuresTitle": "Wie AI Chef Pro in der Schokoladenmanufaktur hilft",
    "features": [
      {
        "icon": "Cookie",
        "title": "Kreative Schokolade",
        "description": "Spezialisierter Agent für professionelle Schokoladenherstellung: Pralinen, Ganaches, Pralinés, Tafeln, Kuvertüren und Temperiertechnik."
      },
      {
        "icon": "Cake",
        "title": "Kreative Patisserie",
        "description": "Für Schokoladendesserts, Häppchen, Brownies und fortgeschrittene Kombinationen Schokolade + Patisserie, die das Sortiment erweitern."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Stück mit Manufaktur-Stundensatz",
        "description": "Kreative Schokolade liefert Rezept + Kalkulations-CSV; Kit de Escandallos Pro verwaltet es mit integriertem Manufaktur-Stundensatz in der echten Marge pro Praline und pro Box."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chocolatería",
        "description": "Vorlagen: Temperieren, Formen, Ganache-Füllen, Zusammenbau, Verpackung, Temperaturkontrolle im Kühlraum."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Schokoladenmanufaktur",
        "description": "Rückverfolgbarkeit von Kakao, Milchprodukten, Nüssen, Alkohol und professioneller Lagerung mit dokumentierten Temperierkurven."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Saisonale Planung mit Schlüsseldaten: Weihnachten, Valentinstag, Ostern, Dreikönigskuchen, Muttertag. Redaktionskalender für die Vitrine."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "KI-Lebensmittelfotografie + Pinterest, wo Premium-Schokoladenmanufakturen stabilen organischen Traffic gewinnen."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients AI",
        "description": "Assistent des Sosa-Katalogs für technische Kuvertüren, konzentrierte Pasten, Nüsse und professionelle Aromen."
      },
      {
        "icon": "Sparkles",
        "title": "Lebensmittelabfälle AI",
        "description": "Präzise Daten zu Verlusten pro Prozess (Temperieren, Formen, Verschnitt, Vitrinenauslage) integriert in die Kalkulation."
      }
    ],
    "workflowTitle": "Ein echter Tag in einer Schokoladenmanufaktur mit AI Chef Pro",
    "workflow": [
      "07:00 · Öffnung – Checkliste Kit de Tareas Chocolatería: Kühlraumkontrolle, Vorkristallisation der Kuvertüre, Formenvorbereitung.",
      "08:30 · Kreative Schokolade – Sie entwickeln eine neue Praline für Valentinstag mit Himbeer-Vanille-Ganache. Kreativküche liefert Rezept + Kalkulations-CSV.",
      "09:30 · Kit de Escandallos Pro – Sie laden das CSV mit Ihren echten Kakaopreisen und integriertem Manufaktur-Stundensatz hoch, validieren die Marge pro Praline und pro 12er-Box.",
      "11:00 · Tagesproduktion – Temperieren auf Marmor, Formen, Ganache-Füllen mit Spritzbeutel, Schockfrosten und Entformen.",
      "14:00 · Vitrinenauffüllung mit professionellen Boxen und Etiketten, Kontrolle der Auslageverluste.",
      "16:00 · Gastro Calendar – Sie bereiten die Produktionsplanung für Weihnachten vor (Firmengeschenkboxen mit 8 Wochen Vorlauf).",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen – Sie generieren Referenzfotos der neuen Praline und für Pinterest optimierte Pins.",
      "20:00 · Schließung – gründliche Reinigung, APPCC unterschrieben, Planung der Mischungen zum Schockfrosten heute Nacht."
    ],
    "productsTitle": "Vorlagen und Kits zum Download für die Schokoladenherstellung",
    "productIds": [
      "kit-tareas-chocolateria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "12.000 Pralinen für Weihnachten ohne System zu produzieren, war Chaos. Mit Kreative Schokolade für das Design, Kit de Escandallos Pro für die echte Marge mit aktuellem Kakao und Gastro Calendar für die saisonale Planung haben wir die Saison gerettet und die Marge um 7 Punkte gesteigert. Die Firmenkartons schließen wir jetzt in einem Anruf mit professionellem Angebot ab.",
    "testimonialAuthor": "Mónica Salazar",
    "testimonialRole": "Meisterin der Schokoladenherstellung und Inhaberin",
    "faqTitle": "Häufige Fragen von Schokoladenmanufakturen",
    "faqs": [
      {
        "q": "Funktioniert es für kleine handwerkliche Schokoladenmanufakturen oder Ketten?",
        "a": "Für beide. Die Vorlagen skalieren von der Familienmanufaktur mit 2 Personen bis zur Produktion für mehrere Verkaufsstellen. Die Methodik ist dieselbe: Rezept → Kalkulations-CSV → echte Marge mit Manufaktur-Stundensatz."
      },
      {
        "q": "Deckt es Pralinenmanufaktur, Tafeln, Kuvertüren und Pralinés ab?",
        "a": "Ja. Kreative Schokolade denkt wie ein professioneller Chocolatier: Kuvertüren-Temperieren nach Kurven, Ganaches mit Wasser-Fett-Balance, Pralinés mit Nussröstaromen, gefüllte Tafeln mit Kristallisationstechnik."
      },
      {
        "q": "Wie gehen wir mit dem volatilen Kakaopreis um?",
        "a": "Kit de Escandallos Pro berechnet die echte Marge sofort neu, wenn Sie den Kuvertürenpreis aktualisieren. Lebensmittelabfälle AI ergänzt die Prozessverlustkosten. So spiegelt die Marge immer die aktuellen Kosten wider, nicht die von vor drei Monaten."
      },
      {
        "q": "Generiert es Inhalte für Vitrine, soziale Medien und Verpackung?",
        "a": "Ja. GastroIMG Gen+ generiert professionelle Referenzbilder jeder Praline für Vitrine, Website und soziale Medien; Pinterest Pins Gen + InstaFlow AI Pro planen visuelle Inhalte; MenuDish Local SEO gewinnt lokale Kunden. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie selbst mit Ihrer real angerichteten Praline."
      },
      {
        "q": "Wie hilft es mir bei starker Saisonalität?",
        "a": "Gastro Calendar plant die Schlüsselsaisonen (Weihnachten, Valentinstag, Ostern, Dreikönigskuchen, Muttertag) mit 8–12 Wochen Vorlauf. Das Kit Plan Financiero projiziert einen realistischen saisonalen Cashflow, damit Sie mit Produktion und Liquidität zu jedem Peak ankommen."
      }
    ],
    "ctaTitle": "Ihre Schokoladenmanufaktur mit klarer Marge und professionellem Branding.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Schokoladenmanufaktur und Pralinenmanufaktur: Kalkulationen, Saisonalität und Branding | AI Chef Pro",
      "description": "KI-Suite für handwerkliche Schokoladenmanufakturen: Kreative Schokolade, Pralinenkalkulation mit Manufaktur-Stundensatz, APPCC, saisonale Planung und Branding. Starten Sie noch heute.",
      "keywords": "KI Schokoladenmanufaktur, Software Schokoladenmanufaktur, Pralinenkalkulation, handwerkliche Schokoladenmanufaktur KI, Temperiertechnik, Pralinenmanufaktur Spanien, Weihnachtsplanung Schokoladenmanufaktur",
      "ogImage": "https://aichef.pro/og/use-cases/chocolateria.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Schokoladenmanufaktur zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen conversationalen Onboarding, bei dem Sie uns mitteilen, welche Art von Schokoladenmanufaktur Sie betreiben (handwerklich, Autoren-Pralinenmanufaktur, Schokoladenmanufaktur mit Café, Manufaktur für den Verkauf an die Gastronomie), Teamgröße, Stadt und Spezialität. Jeder Agent – von Kreative Schokolade bis Gastro Calendar – antwortet angepasst an Ihr Produkt, Ihren Markt und Ihre reale Arbeitsweise.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrer Schokoladenmanufaktur nutzen werden",
    "apps": [
      {
        "name": "Kreative Schokolade",
        "category": "Kulinarische Kreativität",
        "description": "Spezialisierter Agent für professionelle Schokoladenherstellung: Pralinen, Ganaches, Pralinés, Tafeln und Temperiertechnik."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Schokoladendesserts, Häppchen, Brownies und fortgeschrittene Kombinationen."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung neuer Stücke mit Rezept + Kalkulations-CSV."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog: technische Kuvertüren, konzentrierte Pasten, Nüsse und professionelle Aromen."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Assistent des tSpoonLab-Katalogs für fortgeschrittene Schokoladenanwendungen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Verluste pro Prozess (Temperieren, Formen, Verschnitt, Vitrinenauslage) in der Kalkulation."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Allergenerkennung pro Praline: Milchprodukte, Nüsse, Gluten, Alkohol."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Lebensmittelfotografie als Referenz für Vitrine, Website, Verpackung und soziale Medien."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und soziale Medien",
        "description": "Pinterest gewinnt stabilen organischen Traffic für Premium-Schokoladenmanufakturen."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit Redaktionskalender für Autoren-Schokoladenmanufakturen."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die bei Google und Maps nach „handwerkliche Schokoladenmanufaktur in der Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Saisonale Planung: Weihnachten, Valentinstag, Ostern, Dreikönigskuchen, Muttertag."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "Marge nach Pralinenkalkulation"
      },
      {
        "value": "−35 %",
        "label": "Verluste in Manufaktur und Vitrine"
      },
      {
        "value": "×2",
        "label": "Firmenaufträge zu Weihnachten"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Schokoladenmanufaktur"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Kalkulationen ohne Manufaktur-Stundensatz, komplexe Pralinen mit Verlust ohne es zu wissen",
        "Volatiler Kakao, der die Preise durcheinanderbringt, ohne in Echtzeit neu zu berechnen",
        "Verluste beim Temperieren, Formen und in der Vitrine ohne echte Rückverfolgbarkeit",
        "Reaktive saisonale Produktion: Sie kommen zu spät zu Weihnachten und verlieren Firmenaufträge",
        "APPCC auf verstreutem Papier in der Manufaktur"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Professionelle Kalkulation pro Praline mit integriertem Manufaktur-Stundensatz und aktualisierbarem Kakao",
        "Kontrollierte Verluste mit Lebensmittelabfälle AI und spezifischen Schokoladenmanufaktur-Vorlagen",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ gewinnen stabilen Traffic und Aufträge",
        "Gastro Calendar plant Weihnachten und Valentinstag mit 8–12 Wochen Vorlauf",
        "APPCC vom Handy mit prüfungsbereiten Aufzeichnungen"
      ]
    },
    "galleryTitle": "So funktioniert eine handwerkliche Schokoladenmanufaktur",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Vitrine, Manufaktur, Temperieren, Pralinen, Präsentation und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chocolateria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-obrador.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-bonbons.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-temperado.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-display.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-team.jpg"
    ]
  },
  "restaurante-creativo": {
    "h1": "KI für kreative Restaurants und Restaurants mit Autorenküche",
    "heroSubtitle": "Gastronomisches Brainstorming, avantgardistische F&E, Kalkulationen für fortgeschrittene Techniken, Premium-Rezeptkarten und Storytelling für Restaurants mit Autorenküche – mit einer Suite professioneller KI-Agenten für die Gastronomie.",
    "heroTagline": "Kreativität mit System, Avantgarde mit Marge",
    "badge": "Für kreative Restaurants und Restaurants mit Autorenküche",
    "painsTitle": "Was ein kreatives Restaurant unbedingt lösen muss",
    "pains": [
      "Speisekarten, die alle 6–12 Wochen wechseln, mit kontinuierlicher F&E und viel Experimentieren",
      "Komplexe Kalkulationen mit fortschrittlichen Techniken (Sphärisierung, Fermentation, lange Garzeiten, Dehydrierung)",
      "Kleine Teams mit hohem Einsatz, die professionelle Dokumentation brauchen, keine Improvisation",
      "Storytelling und Kommunikation mit Gästen, Presse und sozialen Medien sind ein zentraler Hebel für die Marke",
      "Lange Degustationsmenüs mit vollständiger Kalkulation und schlüssiger Gängefolge",
      "Sich in einer Nische voller kreativer Angebote abheben und anspruchsvolle Gäste gewinnen"
    ],
    "featuresTitle": "So hilft AI Chef Pro in einem kreativen Restaurant",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Kreativküche + Food Pairing AI",
        "description": "Ideenfindung für kreative Gerichte nach Saison, Zutat oder Technik auf wissenschaftlicher Basis. Kreativküche liefert Rezept + CSV-Kalkulation."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Avantgardistische gastronomische F&E: Koji, Kombucha, Shoyu, Garum, Lactofermentation und innovative Techniken mit professioneller Unterstützung."
      },
      {
        "icon": "Leaf",
        "title": "VegChef Plant-Based",
        "description": "Fortgeschrittene pflanzliche, vegane und vegetarische Küche für kreative Gerichte – professionell und ernährungsbewusst."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulationen für fortgeschrittene Techniken",
        "description": "Kit de Escandallos Pro: Sie laden die CSV von Kreativküche mit Ihren tatsächlichen Preisen hoch – für Gerichte mit aufwendigen Techniken und langen Prozessen."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Tiefgreifende Recherche zu Trends, handwerklichen Produzenten, aufkommenden Techniken und Referenzen der weltweiten Avantgarde."
      },
      {
        "icon": "MessageSquare",
        "title": "BlogPost SEO Gen+",
        "description": "Storytelling für den Restaurant-Blog, Pressemappe und Kommunikation mit Gastronomie-Medien."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Hochwertige KI-Lebensmittelfotografie für Rezeptkarten, Presse, Restaurant-Website und soziale Medien."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients AI + tSpoonLab Agent",
        "description": "Assistenten für die Auswahl technischer Zutaten von Sosa und tSpoonLab – essenziell für die Autorenküche."
      },
      {
        "icon": "GraduationCap",
        "title": "Gastro Lexikum + Pro Prompts eBook",
        "description": "Tutor für technische und wissenschaftliche Definitionen + 300+ professionelle Prompts für Kreativität und Kommunikation."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem kreativen Restaurant mit AI Chef Pro",
    "workflow": [
      "08:30 · Sonar Deep Research – Sie recherchieren Trends und saisonale Produkte auf europäischen Märkten als Inspiration für den nächsten Menüwechsel.",
      "10:00 · Kreativküche + Food Pairing AI – Sie entwickeln 14 Gerichte für das neue Degustationsmenü mit Technik und anfänglicher CSV-Kalkulation.",
      "12:00 · Fermentus mit AI+ – Sie arbeiten an der Basis einer Schlüsselfermentation des Menüs: inokulierter Gersten-Koji für 4 Gerichte.",
      "14:00 · Sosa Ingredients AI + tSpoonLab Agent – Sie wählen technische Zutaten für Texturen und Anwendungen aus.",
      "15:30 · Kit de Escandallos Pro – Sie laden die CSVs mit Ihren tatsächlichen Preisen hoch und verwerfen 4 Gerichte, die nicht zur Zielmarge (32 %) passen.",
      "17:00 · Pro Prompts eBook – Sie schreiben das Storytelling für die 10 finalen Gerichte: Name, Story und vollständige Rezeptkarte.",
      "18:30 · GastroIMG Gen+ – Sie generieren Fotos jedes Gerichts für die Pressemappe und die Restaurant-Website.",
      "19:30 · Service – koordiniertes Team mit zentralisierten Rezeptkarten, Gänge des Degustationsmenüs mit validierter Gängefolge."
    ],
    "productsTitle": "Vorlagen und Kits zum Download für kreative Restaurants",
    "productIds": [
      "kit-tareas-restaurante-creativo",
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "Ich wechsle die Speisekarte alle 6 Wochen. Früher bedeutete das eine Woche Papierkram – Kalkulationen, Rezeptkarten und Storytelling. Jetzt erledige ich das mit AI Chef Pro in 2 Tagen: Kreativküche macht Vorschläge, Fermentus unterstützt mich bei F&E, Sonar Deep Research liefert Trends, und das Kit de Escandallos Pro sichert die Marge. Es ist, als hätte ich ein zusätzliches F&E-Team.",
    "testimonialAuthor": "Adrián Lago",
    "testimonialRole": "Koch und Inhaber, Restaurant mit Autorenküche mit 30 Plätzen",
    "faqTitle": "Häufig gestellte Fragen für kreative Restaurants",
    "faqs": [
      {
        "q": "Versteht die KI fortgeschrittene Techniken der Autorenküche?",
        "a": "Ja. Kreativküche, Fermentus mit AI+, Food Pairing AI, VegChef und die Länder-Rezeptsammlungen sind mit professionellem Wissen trainiert: Techniken wie Sphärisierung, lange Fermentation, kontrolliertes Garen, Gelierung, Schäume, Dehydrierung und avantgardistische Prozesse."
      },
      {
        "q": "Gibt es spezielle Degustationsmenüs?",
        "a": "Ja. Das Kit de Tareas Restaurante Creativo und das Kit de Escandallos Pro bieten Vorlagen für Degustationsmenüs mit vollständiger Kalkulation, Gängereihenfolge und Weinbegleitung."
      },
      {
        "q": "Deckt es F&E und Verkostung ab?",
        "a": "Ja. Sonar Deep Research liefert Trends und Referenzen; Kreativküche + Fermentus entwickeln Gerichte; Pro Prompts eBook bietet 300+ spezifische Prompts für iterative F&E."
      },
      {
        "q": "Erzeugt es Storytelling für Presse und Restaurantführer?",
        "a": "Ja. Mit BlogPost SEO Gen+ + Pro Prompts eBook + GastroIMG Gen+ können Sie Pressemappen erstellen, mit Guide Michelin, Repsol und 50 Best kommunizieren und Beiträge für Gastronomie-Medien verfassen."
      },
      {
        "q": "Funktioniert es für avantgardistische Fermentation?",
        "a": "Fermentus mit AI+ ist der am häufigsten genutzte Agent von Köchen der Autorenküche: Es deckt Koji, Kombucha, Shoyu, Miso, Garum, Lactofermentation und innovative Prozesse mit wissenschaftlicher Unterstützung ab."
      },
      {
        "q": "Wie lässt es sich mit Sosa und anderen technischen Anbietern integrieren?",
        "a": "Sosa Ingredients AI und tSpoonLab Agent sind spezifische Assistenten für den Katalog des jeweiligen Anbieters: Sie helfen bei der Auswahl von Texturen, Zusatzstoffen und technischen Anwendungen mit professionellem Anspruch."
      }
    ],
    "ctaTitle": "Kreativität mit System, Avantgarde mit Marge.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits zur Nutzung aller Agenten.",
    "seo": {
      "title": "KI für kreative Restaurants und Autorenküche: F&E, Avantgarde und Storytelling | AI Chef Pro",
      "description": "KI-Suite für kreative Restaurants und Autorenküche: Kreativküche, Fermentus, Sonar Deep Research, fortgeschrittene Kalkulationen, Rezeptkarten und professionelles Storytelling.",
      "keywords": "KI kreatives Restaurant, Autorenrestaurant KI, Software kreatives Restaurant, kreative Kalkulationen, gastronomische KI Autorenküche, kreative Fermentation KI, Fermentus, Autorenrestaurant Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-creativo.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Kreativküche personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen conversational Onboarding, bei dem Sie erzählen, welche Art von kreativer Küche Sie führen (Autorenküche, Gastrobotanik, Fermentation, Avantgarde, Fusion), Ihre Stadt und Ihre Vorbilder. Ab diesem Moment antwortet jeder Agent – von Kreativküche bis Sonar Deep Research – passend zu Ihrer kreativen Sprache, Ihren üblichen Techniken und Ihrer tatsächlichen Positionierung in der Branche.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem kreativen Restaurant einsetzen werden",
    "apps": [
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung professioneller Gerichte mit Rezept + CSV-Kalkulation, bereit für das Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Kombinationen von Zutaten und Pairings auf wissenschaftlicher Basis."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Avantgardistische F&E: Fermentationen, Koji, Kombucha, Garum, Miso."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Kulinarische Kreativität",
        "description": "Fortgeschrittene pflanzliche, vegane und vegetarische Küche für die Autorenküche."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Kreative Desserts mit professioneller Patisserie-Technik."
      },
      {
        "name": "Executive Chef Pro",
        "category": "Gastro-Profil Pro",
        "description": "Standardisierung von Rezeptkarten und Küchenhandbüchern."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Tiefgreifende Recherche: Trends, Produzenten, weltweite Avantgarde."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für den Sosa-Katalog mit Texturen und fortgeschrittenen Techniken."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für den tSpoonLab-Katalog für technische Anwendungen."
      },
      {
        "name": "Gastro Lexikum",
        "category": "Gastro-Wissen",
        "description": "Tutor mit Definitionen zu Techniken, Prozessen und Gastronomiewissenschaft."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Hochwertige Lebensmittelfotografie für Presse und Web."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte & Social Media",
        "description": "Blogbeiträge mit Storytelling für organischen Traffic."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "Schnellerer Abschluss neuer Speisekarten"
      },
      {
        "value": "14",
        "label": "Gerichte im Degustationsmenü"
      },
      {
        "value": "+5 pp",
        "label": "Marge nach realer Kalkulation"
      },
      {
        "value": "13+",
        "label": "Agenten für die Autorenküche"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Abschluss neuer Speisekarte: 15–30 Tage für F&E, Kalkulationen, Rezeptkarten und Storytelling",
        "Improvisierte F&E ohne Dokumentation, Techniken geraten in Vergessenheit",
        "Storytelling für die Presse, das bei jedem Wechsel in letzter Minute verfasst wird",
        "Rezeptkarten in Notizbüchern, während des Service nicht zugänglich",
        "Trendrecherche aus dem Bauchgefühl ohne Zugang zu Quellen"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Abschluss neuer Speisekarte: 1–3 Tage mit Kreativküche, Fermentus und Kit de Escandallos Pro",
        "Dokumentierte F&E mit iterativen Rezeptkarten, nachvollziehbaren und reproduzierbaren Techniken",
        "Professionelles Storytelling in Stunden generiert mit BlogPost SEO Gen+",
        "Zentralisierte Rezeptkarten, während des Services mobil zugänglich",
        "Sonar Deep Research liefert Trends und professionelle Referenzen"
      ]
    },
    "galleryTitle": "So funktioniert ein kreatives Restaurant mit Autorenküche",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: F&E, Fermentation, kreatives Anrichten, Vorbereitung spezieller Zutaten und intimes Restaurantambiente.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-creativo-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-creativo-ferment.jpg",
      "/lovable-uploads/ai-gallery/use-case-creativo-plating.jpg",
      "/lovable-uploads/ai-gallery/use-case-creativo-rd.jpg",
      "/lovable-uploads/ai-gallery/use-case-creativo-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-creativo-room.jpg"
    ]
  },
  "restaurante-gastronomico": {
    "h1": "KI für Gourmetrestaurants (Michelin/Repsol)",
    "heroSubtitle": "Premium-Kalkulationen, lange Degustationsmenüs, erweiterte Brigade, rigoroses HACCP und Kommunikation mit Guides und Presse – mit einer Suite von KI-Agenten, die für die professionelle gehobene Gastronomie entwickelt wurde.",
    "heroTagline": "Haute Cuisine mit System, Avantgarde mit Führung",
    "badge": "Für Gourmetrestaurants mit Michelin- und Repsol-Auszeichnung",
    "painsTitle": "Was ein Gourmetrestaurant unbedingt lösen muss",
    "pains": [
      "Anspruchsvolle Marge bei Premium-Produkten, deren Kosten sich jede Woche auf dem Fischmarkt und am Markt ändern",
      "Große, hochkoordinierte Brigade mit strenger Hierarchie und Rotation von Juniorköchen",
      "Lange Degustationsmenüs (8-15 Gänge) mit vollständiger Kalkulation, Weinbegleitung und schlüssiger Erzählung",
      "Kommunikation mit Michelin/Repsol/50Best-Guides und Fachpresse als kritischer Hebel",
      "Kontinuierliche avantgardistische F&E mit fortschrittlichen Techniken und saisonalen Produkten",
      "Reservierungen Monate im Voraus mit schwierig zu verwaltenden Stornierungen und tadellosem Serviceablauf"
    ],
    "featuresTitle": "Wie AI Chef Pro in der gehobenen Gastronomie hilft",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Executive Chef Pro",
        "description": "Standardisierung von technischen Rezepturen und Handbüchern für eine erweiterte Brigade mit strenger Hierarchie."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche + Food Pairing AI",
        "description": "Brainstorming für Gerichte des Degustationsmenüs mit Technik und Weinbegleitung. Kreativküche liefert Rezept + CSV-Kalkulation."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Avantgardistische F&E: Koji, Kombuchas, Shoyus, Garums, Lactofermente – essenziell in der zeitgenössischen Haute Cuisine."
      },
      {
        "icon": "Calculator",
        "title": "Premium-Kalkulationen",
        "description": "Kit de Escandallos Pro: Sie laden die CSV aus der Kreativküche mit Ihren tatsächlichen Preisen für Premium-Produkte hoch und erhalten eine präzise Marge pro Gang und pro vollständigem Degustationsmenü."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients AI + tSpoonLab Agent",
        "description": "Assistenten für die in der Haute Cuisine am häufigsten verwendeten professionellen Kataloge für fortgeschrittene Techniken und Anwendungen."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Tiefgreifende Recherche zu globalen Trends, handwerklichen Produzenten, aufkommenden Techniken und Referenzen der internationalen Avantgarde."
      },
      {
        "icon": "MessageSquare",
        "title": "BlogPost SEO Gen+ + Pro Prompts eBook",
        "description": "Professionelle Kommunikation für Michelin/Repsol/50Best-Guides, Pressedossier und Storytelling für Degustationsmenüs."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Hochwertige gastronomische KI-Fotografie für Website, Fachpresse und Bewerbungsdossiers für Guides."
      },
      {
        "icon": "GraduationCap",
        "title": "Gastro Lexikum",
        "description": "Tutor mit technischen Definitionen, Prozessen und gastronomischer Wissenschaft für Premium-Rezepturen und die Ausbildung der Brigade."
      }
    ],
    "workflowTitle": "Ein realer Tag in einem Gourmetrestaurant mit AI Chef Pro",
    "workflow": [
      "08:30 Uhr · Sonar Deep Research – Sie recherchieren Trends und saisonale Produkte auf europäischen Märkten als Inspiration für die nächste Änderung des Degustationsmenüs.",
      "10:00 Uhr · Kreativküche + Food Pairing AI – Sie entwickeln 14 Gänge für das neue Degustationsmenü mit fortgeschrittener Technik und CSV-Kalkulation.",
      "12:00 Uhr · Fermentus mit AI+ – Sie arbeiten an der Basis einer Schlüsselfermentation des Menüs: Fischgarum für 4 Gänge.",
      "14:00 Uhr · Sosa Ingredients AI + tSpoonLab Agent – Sie wählen technische Zutaten für Texturen und Premium-Anwendungen aus.",
      "15:30 Uhr · Kit de Escandallos Pro – Sie laden die CSVs mit Ihren Marktpreisen hoch und validieren die Marge des gesamten Degustationsmenüs (28 €/Gang durchschnittliche Kosten).",
      "17:00 Uhr · Pro Prompts eBook + BlogPost SEO Gen+ – Sie erstellen Storytelling für die 14 Gänge, ein Dossier für Michelin/Repsol-Guides und eine Pressemitteilung.",
      "18:30 Uhr · GastroIMG Gen+ – Sie generieren Fotos von jedem Gang für die Website des Restaurants und das Bewerbungsdossier für die Guides.",
      "19:30 Uhr · Abendservice – koordinierte Brigade mit zentralisierten technischen Rezepturen, Gänge des Degustationsmenüs mit validierter Reihenfolge und mit dem Sommelier synchronisierte Weinbegleitung."
    ],
    "productsTitle": "Vorlagen, Kits und herunterladbare Guides für die gehobene Gastronomie",
    "productIds": [
      "guia-restaurante-gastronomico",
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "Dank der Bündelung von Kalkulation, technischen Rezepturen, dokumentierten Fermenten und der Kommunikation mit den Guides in einem einzigen System haben wir das kreative Chaos, das jede Haute Cuisine mit sich bringt, in den Griff bekommen. Der Guía Restaurante Gastronómico war bei der Eröffnung des zweiten Projekts entscheidend: ein professioneller Businessplan, der die Bewerbung untermauert. Und die jüngste Auszeichnung – mit belastbaren Daten.",
    "testimonialAuthor": "David Aramburu",
    "testimonialRole": "Executive Chef, Gourmetrestaurant mit Michelin/Repsol-Auszeichnung",
    "faqTitle": "Häufig gestellte Fragen von Gourmetrestaurants",
    "faqs": [
      {
        "q": "Ist es für ein Restaurant mit Michelin-Stern oder für aufstrebende Restaurants geeignet?",
        "a": "Für beides. Die Vorlagen und Agenten sind auf höchste Ansprüche ausgelegt: rigorose Standardisierung, Premium-Rezepturen, professionelle Kalkulation und Kommunikation mit Guides."
      },
      {
        "q": "Gibt es eine Schritt-für-Schritt-Anleitung für die Eröffnung eines Gourmetrestaurants?",
        "a": "Ja, der Guía Restaurante Gastronómico (85 €): 65 Plätze, Muster-Businessplan für die Bewerbung, Finanzplan, Küchenplan, Brigade, Sommelier, operative Handbücher und Kommunikation mit Guides. Mehr als 20 Arbeitsmaterialien."
      },
      {
        "q": "Deckt es lange Degustationsmenüs mit 14-18 Gängen ab?",
        "a": "Ja. Das Kit de Escandallos Pro und das Kit de Tareas Restaurante Creativo enthalten spezifische Vorlagen für Degustationsmenüs mit Gängen, vollständiger Kalkulation, Reihenfolge und mit dem Sommelier synchronisierter Weinbegleitung."
      },
      {
        "q": "Erstellt es professionelle Kommunikation für Michelin, Repsol und 50Best?",
        "a": "Ja. BlogPost SEO Gen+ + Pro Prompts eBook + GastroIMG Gen+ ermöglichen das Verfassen von Bewerbungsdossiers, die Kommunikation mit Inspektoren, Pressemitteilungen und Materialien für die Redaktionen der Guides."
      },
      {
        "q": "Funktioniert es für avantgardistische Fermentation?",
        "a": "Fermentus mit AI+ ist einer der am häufigsten von Michelin-Köchen genutzten Agenten: Es deckt Koji, Kombucha, Shoyu, Miso, Garum und Lactofermente mit wissenschaftlicher Untermauerung und realen Anwendungen in Gängen der Haute Cuisine ab."
      },
      {
        "q": "Wie funktioniert die Integration mit Premium-Lieferanten?",
        "a": "Sosa Ingredients AI und tSpoonLab Agent sind spezifische Assistenten für professionelle Kataloge, die in der gehobenen Gastronomie weit verbreitet sind. Sie helfen bei der Auswahl von Texturen, Zusatzstoffen und technischen Anwendungen mit dem Anspruch der Kreativküche."
      }
    ],
    "ctaTitle": "Haute Cuisine mit System, Avantgarde mit Führung.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für die Nutzung aller Agenten.",
    "seo": {
      "title": "KI für Gourmetrestaurants (Michelin/Repsol): Degustationsmenü, F&E und Kommunikation | AI Chef Pro",
      "description": "KI-Suite für die gehobene Gastronomie: Kreativküche, Fermentus, Sonar Deep Research, Premium-Kalkulationen, technische Rezepturen, Kommunikation mit Michelin- und Repsol-Guides. Starten Sie noch heute.",
      "keywords": "KI Gourmetrestaurant, Michelin-Software, Haute-Cuisine-Restaurant KI, Premium-Kalkulationen, KI Repsol Soles, KI 50Best, kreative Fermentation, Fermentus, Degustationsmenü KI, Gastronomie Spanien",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-gastronomico.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Gourmetrestaurant personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational-Onboarding, bei dem Sie erzählen, welche Art von Küche Sie leiten (Michelin, Repsol Soles, aufstrebend, zeitgenössische Haute Cuisine, avantgardistische Fusionsküche), Anzahl der Plätze, Stadt und Vorbilder. Ab diesem Moment antwortet jeder Agent – von der Kreativküche bis Sonar Deep Research – passend zu Ihrer Sprache, Ihrer üblichen Technik und Ihrer tatsächlichen Positionierung in der Branche.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Gourmetrestaurant nutzen werden",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standardisierung von technischen Rezepturen und Handbüchern für die erweiterte Brigade."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Gängen für das Degustationsmenü mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Wissenschaftlich fundierte Zutatenkombinationen und Pairings."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Avantgardistische F&E: Koji, Kombucha, Shoyu, Miso, Garum, Lactofermente."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Kulinarische Kreativität",
        "description": "Hochwertige pflanzliche Küche für pflanzenbasierte Optionen im Degustationsmenü."
      },
      {
        "name": "Kreative Patisserie + Kreative Schokolade",
        "category": "Kulinarische Kreativität",
        "description": "Haute-Cuisine-Desserts und Petit Fours zum Abschluss."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Tiefgreifende Recherche zu globalen Trends und Avantgarde."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für den Sosa-Katalog für Texturen und fortgeschrittene Techniken."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Assistent für den tSpoonLab-Katalog für technische Anwendungen."
      },
      {
        "name": "Gastro Lexikum",
        "category": "Gastro-Wissen",
        "description": "Tutor mit technischen und wissenschaftlichen Definitionen."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Hochwertige gastronomische Fotografie für Presse und Guides."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte & Social Media",
        "description": "Storytelling und professionelle Kommunikation mit Guides und Fachpresse."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "Schnelligkeit beim Abschluss neuer Menüs"
      },
      {
        "value": "14-18",
        "label": "Gänge im Degustationsmenü"
      },
      {
        "value": "+5 pp",
        "label": "Marge nach rigoroser Kalkulation"
      },
      {
        "value": "13+",
        "label": "Agenten für die gehobene Gastronomie"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Abschluss eines neuen Degustationsmenüs: 15-30 Tage für F&E, Kalkulationen, Rezepturen und Kommunikation mit Guides",
        "F&E für Fermente ohne Dokumentation, Techniken, die sich nicht reproduzieren lassen",
        "Storytelling für Presse und Guides jedes Mal unter Zeitdruck, wenn sich etwas ändert",
        "Technische Rezepturen im Notizbuch des Chefs, während des Services unzugänglich",
        "Trendrecherche nach Bauchgefühl und in Magazinen, ohne systematischen Zugang"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Abschluss des Degustationsmenüs: 1-3 Tage mit Kreativküche, Fermentus und Kit de Escandallos Pro",
        "Dokumentierte F&E mit iterativen Rezepturen, nachvollziehbaren und für die Brigade reproduzierbaren Fermentationen",
        "In Stunden generiertes professionelles Storytelling für Michelin/Repsol/50Best",
        "Zentralisierte technische Rezepturen, während des Services mobil zugänglich",
        "Sonar Deep Research liefert sofort Trends der internationalen Avantgarde"
      ]
    },
    "galleryTitle": "So funktioniert ein Gourmetrestaurant der Haute Cuisine",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren werden: elegantes Restaurant, Plating der Degustationsgänge, Premium-Küche, Sommelier und tadelloser Service.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-gastronomico-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-kitchen.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-pase.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-sommelier.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-cellar.jpg"
    ]
  },
  "restaurante-mexicano": {
    "h1": "KI für mexikanische Restaurants",
    "heroSubtitle": "Entwickeln Sie Salsas mit präziser Balance, kalkulieren Sie Taco für Taco und Menü mit echten Kosten, planen Sie die Massenproduktion und Nixtamalisierung und sichern Sie sich professionelles Branding mit einer Suite gastronomischer KI-Agenten, die auf authentische mexikanische Küche spezialisiert sind.",
    "heroTagline": "Mexikanischer Geschmack mit echter Marge und authentischer Technik",
    "badge": "Für mexikanische Restaurants und Taquerías",
    "painsTitle": "Was ein mexikanisches Restaurant unbedingt lösen muss",
    "pains": [
      "Komplexe Salsas mit vielen Chilis, Röstung und präziser Balance (Mole, Salsa Macha, Adobos), die Schicht für Schicht Konsistenz erfordern",
      "Kalkulation von Tacos, Antojitos und Gerichten mit vielen Varianten bei Tortilla, Füllung, Salsas und Beilagen bei gleichbleibendem Food Cost",
      "Lebensmittelabfälle bei Masa, Tortillas, Marinaden und langsam gegarten Proteinen (Carnitas, Barbacoa, Cochinita)",
      "Standardisierung der Nixtamalisierung und Masa-Technik für Tortillas, Sopes und Huaraches mit gleichbleibender Qualität",
      "Differenzierung in einem umkämpften Gebiet mit authentischem Menü, visuellem Branding für Antojitos und regionalem Storytelling (Oaxaca, Yucatán, Puebla)",
      "Aufträge für Events und mexikanisches Catering (Hochzeiten, Nationalfeiertage) mit Marge gewinnen, während der Tagesbetrieb läuft"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem mexikanischen Restaurant hilft",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Mexikanische Küche",
        "description": "Spezialisierter Agent für authentische mexikanische Küche: Salsas, Moles, Marinaden, Antojitos, Masa-Technik und regionale Küche."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für zeitgenössische und kreative Gerichte mit mexikanischer Basis: Signature-Tacos, kontrollierte Fusionen, moderne mexikanische Desserts."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Taco und pro Gericht",
        "description": "Mexikanische Küche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet sie mit echten Kosten pro Taco, Food-Cost-Prozentsatz und empfohlenem Preis."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Anpassbare Vorlagen: Masa-Vorbereitung, Chili-Rösten, Marinaden, Comal, Mise en Place pro Station und Abschluss."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC mexicano",
        "description": "Rückverfolgbarkeit von Chilis, nixtamalisiertem Masa-Teig, langsam gegarten Proteinen und kritischen Temperaturen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planung mit wichtigen Terminen: 5. Mai, Día de Muertos, Nationalfeiertage 16. September, Día de la Candelaria mit Tamales."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "KI-Referenzfotografie für Gastronomie + Instagram mit Redaktionskalender: Das mexikanische Restaurant lebt von visueller Wirkung und Storytelling."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients AI",
        "description": "Assistent für den Sosa-Katalog mit fortgeschrittenen Texturen, Verdickungsmitteln, Trockenprodukten und Techniken für die mexikanische Küche."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Mexicano",
        "description": "Premium-Download-Guide mit 80 Plätzen, Kalkulationen, technischen Datenblättern, Finanzplan und spezifischer Betriebsführung für die mexikanische Küche."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem mexikanischen Restaurant mit AI Chef Pro",
    "workflow": [
      "08:00 · Eröffnung – Checkliste Kit de Tareas: Rösten von Chilis für Salsa Macha, Vorbereitung von nixtamalisiertem Masa-Teig, Marinade für Cochinita Pibil, Mise en Place für frische Toppings.",
      "10:00 · Mexikanische Küche – Sie entwickeln einen neuen Signature-Barbacoa-Taco mit Cascabel-Chilisoße und Avocado. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "11:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren tatsächlichen Preisen für getrocknete Chilis, Fleisch, Masa und Avocado hoch, validieren die Marge pro Taco und den Food-Cost-Prozentsatz.",
      "13:00 · Mittagsservice – das Team arbeitet mit Mise-en-Place-Vorlagen; der Comal läuft auf Hochtouren.",
      "17:00 · Pause zwischen den Services – Gastro Calendar plant das spezielle Día-de-Muertos-Menü mit Pan de Muerto und Mole Negro.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren das Referenzbild des neuen Tacos und die Posts für Instagram.",
      "21:00 · Abendservice – koordinierte Spitzenzeiten mit Mitarbeiteressen AI für das Team vor dem Ansturm.",
      "00:00 · Schließung – gründliche Reinigung, APPCC unterschrieben, Masa-Teig für morgen vorbereiten."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für mexikanische Restaurants",
    "productIds": [
      "guia-restaurante-mexicano",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Wir haben Taco für Taco kalkuliert und festgestellt, dass drei Signature-Gerichte trotz hoher Verkaufszahlen Verluste machten. Wir haben sie mit Mexikanische Küche neu gestaltet, Marinade und Fleischertrag angepasst, ohne den Preis zu ändern, und die Marge um 5 Punkte gesteigert. Die Planung des Día de Muertos mit Gastro Calendar hat unseren Umsatz in dieser Woche verdreifacht.",
    "testimonialAuthor": "María José Hernández",
    "testimonialRole": "Köchin und Inhaberin, zeitgenössisches mexikanisches Restaurant",
    "faqTitle": "Häufig gestellte Fragen für mexikanische Restaurants",
    "faqs": [
      {
        "q": "Funktioniert es für eine lockere Taquería, ein zeitgenössisches mexikanisches Restaurant oder regionale Küche?",
        "a": "Für alle drei. Mexikanische Küche deckt von der traditionellen Taquería bis zur gehobenen mexikanischen Autorenküche ab, einschließlich regionaler Küche (Oaxaca, Yucatán, Puebla, Michoacán) mit authentischer Technik."
      },
      {
        "q": "Deckt es Nixtamalisierung und Masa-Technik ab?",
        "a": "Ja. Mexikanische Küche denkt wie ein professioneller mexikanischer Koch: Nixtamalisierung mit Kalk, Masa-Balance für Tortilla, Sope, Huarache, Gordita und Tlacoyo. Keine YouTube-Rezepte."
      },
      {
        "q": "Wie hilft es mir bei der Komplexität mexikanischer Salsas?",
        "a": "Mexikanische Küche liefert Salsas mit technischer Chili-Balance (Rösten, Hydratisieren, Schärfe-Süße-Säure-Balance), komplexe Moles in Schichten und professionelle Marinaden. Lebensmittelabfälle AI addiert die Kosten der getrockneten Chilis zur endgültigen Kalkulation."
      },
      {
        "q": "Erzeugt es visuelle Inhalte für Instagram, Glovo und Uber Eats?",
        "a": "Ja. GastroIMG Gen+ erzeugt professionelle Referenzbilder für soziale Netzwerke und Lieferdienste; besseres Foto = mehr Klicks und besseres Ranking. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie mit Ihrem real angerichteten Gericht."
      },
      {
        "q": "Wie hilft es mir bei mexikanischen Feiertagen?",
        "a": "Gastro Calendar plant die wichtigsten Termine (Día de Muertos, Día de la Candelaria mit Tamales, Nationalfeiertage, 5. Mai) mit speziellen Menüs und Redaktionskalender."
      }
    ],
    "ctaTitle": "Ihr mexikanisches Restaurant mit echter Marge und authentischer Technik.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für mexikanische Restaurants: Salsas, Kalkulationen und authentische Technik | AI Chef Pro",
      "description": "KI-Suite für mexikanische Restaurants: Mexikanische Küche, Taco-Kalkulationen, Feiertagsplanung, Branding und APPCC. Starten Sie noch heute.",
      "keywords": "KI mexikanisches Restaurant, Taquería-Software, Taco-Kalkulation, mexikanische Küche KI, Nixtamalisierung, mexikanische Salsas, Día de Muertos Restaurant",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-mexicano.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr mexikanisches Restaurant zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational Onboarding, bei dem Sie erzählen, welche Art von mexikanischem Betrieb Sie führen (lockere Taquería, zeitgenössisches mexikanisches Restaurant, regionale Küche, Cantina, Gourmet-Taquería, mexikanischer Food Truck), Teamgröße, Stadt und Spezialität. Jeder Agent – von Mexikanische Küche bis Gastro Calendar – antwortet angepasst an Ihr Produkt, Ihren Markt und Ihre reale Betriebsweise.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem mexikanischen Restaurant nutzen werden",
    "apps": [
      {
        "name": "Mexikanische Küche",
        "category": "Rezeptsammlungen Lateinamerika",
        "description": "Spezialisierter Agent für authentische mexikanische Küche: Salsas, Moles, Marinaden, Antojitos, regionale Technik."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Tacos und zeitgenössischen Gerichten mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Operative Beratung für lockere Restaurants und professionelle Taquerías."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für Texturen, Verdickungsmittel und Techniken für die mexikanische Autorenküche."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Lebensmittelabfälle bei Masa, Chilis, Marinaden und langsam gegarten Proteinen."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Allergenerkennung pro Gericht: Gluten, Milchprodukte, Nüsse, Soja."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Referenzfotografie für Gastronomie für Instagram, Web, Speisekarte und Lieferdienste."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit professionellem Redaktionskalender für die Taquería de Autor."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die bei Google und Maps nach „Tacos in der Nähe“ oder „mexikanisches Restaurant“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Día de Muertos, Día de la Candelaria, Nationalfeiertage, 5. Mai."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und soziale Medien",
        "description": "Pinterest gewinnt organischen Traffic für Tacos und Antojitos mit Storytelling."
      },
      {
        "name": "Mitarbeiteressen AI",
        "category": "Gastro Profile Pro",
        "description": "Generator für Mitarbeiter-/Familienmenüs, konzeptübergreifend für alle Bereiche."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach Taco-Kalkulation"
      },
      {
        "value": "×3",
        "label": "Umsatz an Día de Muertos"
      },
      {
        "value": "−20 %",
        "label": "Lebensmittelabfälle bei Masa und Marinaden"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre mexikanische Küche"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierte Salsas und Moles, inkonsistente Balance Schicht für Schicht",
        "Kalkulationen ohne echten Food Cost, Signature-Gerichte machen unbemerkt Verluste",
        "Lebensmittelabfälle bei Masa, Chilis und langsam gegarten Proteinen ohne Rückverfolgbarkeit",
        "Reaktive Feiertage: Sie sind zu spät zu Día de Muertos ohne spezielles Menü",
        "Improvisiertes Instagram und Lieferplattformen mit Handyfotos"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Salsas und Moles mit technischem Anspruch, Konsistenz Schicht für Schicht",
        "Professionelle Kalkulation pro Taco und Gericht mit validiertem Food Cost",
        "Kontrollierte Lebensmittelabfälle mit Lebensmittelabfälle AI und spezifischen Vorlagen",
        "Feiertage mit 8 Wochen Vorlauf mit Gastro Calendar geplant",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO gewinnen lokale Kunden"
      ]
    },
    "galleryTitle": "So funktioniert ein mexikanisches Restaurant",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Salsas, Tacos, Comal, Zutaten und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-mexicano-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-salsas.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-tacos.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-comal.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-ingredientes.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-team.jpg"
    ]
  },
  "restaurante-peruano": {
    "h1": "KI für peruanische Restaurants",
    "heroSubtitle": "Entwickeln Sie Ceviches, Tiraditos und Causas mit technischer Balance, Kalkulation pro Gericht mit echten Kosten für Fisch und Chili, planen Sie die Produktion und erfassen Sie professionelles Branding mit einer Suite von gastronomischen KI-Agenten, die auf authentische peruanische Küche spezialisiert sind.",
    "heroTagline": "Peruanische Küche mit echter Marge und authentischer Technik",
    "badge": "Für peruanische Restaurants und Cevicherías",
    "painsTitle": "Was ein peruanisches Restaurant unbedingt lösen muss",
    "pains": [
      "Ceviches und Tiraditos mit täglich frischem Fisch und Leche de tigre, die Schicht für Schicht in Säure, Schärfe und Salz ausbalanciert ist",
      "Gerichte mit importierten peruanischen Zutaten (gelbe Chilis, Rocoto, Panca, Huacatay) kalkulieren, deren Kosten je nach Saison variieren",
      "Lebensmittelabfälle bei frischem Fisch, Meeresfrüchten, Choclo, peruanischen Kartoffeln und Limetten bei intensiver Nutzung",
      "Die Gartechnik von Proteinen (Anticucho, Pollo a la Brasa, Pachamanca) und Beilagen (Causa, Papa a la Huancaína) standardisieren",
      "Sich in einem umkämpften Gebiet mit authentischem Menü (Criolla, Costeña, Andina, Amazónica), visuellem Branding und regionalem Storytelling differenzieren",
      "Liefer- und Eventbestellungen gewinnen, während die Qualität des Ceviche außerhalb seines optimalen Verzehrfensters erhalten bleibt"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem peruanischen Restaurant hilft",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Peruanische Küche",
        "description": "Spezialisierter Agent für authentische peruanische Küche: Ceviches, Tiraditos, Causas, Anticuchos, Pachamanca, Criolla-, Costeña-, Andina- und Amazónica-Technik."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für zeitgenössische und Autorengerichte mit peruanischer Basis: Signature-Causas, kontrollierte Fusionen, moderne peruanische Desserts."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Pairings mit Pisco, chilenischen Weinen und Bier für Ihre peruanische Karte auf wissenschaftlicher Basis."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Gericht",
        "description": "Die Peruanische Küche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet sie mit echten Kosten pro Ceviche, Food-Cost-% und empfohlenem Preis."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Vorlagen: Vorbereitung der Leche de tigre, Anticucho-Marinaden, Mise en Place für Meeresfrüchte, Papa a la Huancaína, Schließung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC peruano",
        "description": "Rückverfolgbarkeit von frischem Fisch, Meeresfrüchten, Chilis und kritischen Temperaturen bei Ceviche und Tiradito."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planung mit wichtigen Terminen: Unabhängigkeitstag 28. Juli, Tag des Ceviche, Mistura, Tag des Pisco Sour."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "KI-Referenzfotografie für Ceviches und Tiraditos + Instagram: Das peruanische Restaurant lebt von der visuellen Wirkung der Farbe."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Peruano",
        "description": "Premium-Download-Guide für 80 Plätze, Kalkulationen, technischen Datenblättern, Finanzplan und spezifischer Betriebsführung für die peruanische Küche."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem peruanischen Restaurant mit AI Chef Pro",
    "workflow": [
      "08:00 · Eröffnung – Checkliste Kit de Tareas: Annahme von täglich frischem Fisch, Vorbereitung der Basis-Leche de tigre, Marinade für Anticucho, Einweichen von getrockneten Chilis.",
      "10:00 · Peruanische Küche – Sie entwickeln einen neuen Tiradito vom Tagesfang mit Leche de tigre aus Rocoto und Mango. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "11:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren tatsächlichen Preisen für frischen Fisch, Chilis, Choclo und Kartoffeln hoch und validieren die Marge pro Gericht.",
      "12:00 · Food Pairing AI – Sie validieren das Pairing des neuen Tiraditos mit einem in Kräutern mazerierten Pisco Sour.",
      "13:00 · Mittagsservice – Hauptzeit des Ceviche-Kochs, einwandfreie Mise en Place.",
      "17:00 · Pause zwischen den Services – Gastro Calendar plant das Menü zum 28. Juli (Unabhängigkeitstag) mit Causa, Anticuchos und Pisco.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren das Referenzbild des neuen Tiraditos und die Posts für Instagram.",
      "23:00 · Schließung – gründliche Reinigung, APPCC unterschrieben, kontrollierte Entsorgung des Tagesfischs."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für peruanische Restaurants",
    "productIds": [
      "guia-restaurante-peruano",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Die Peruanische Küche hat unsere Küche verändert. Die Leche de tigre hat jetzt eine dokumentierte technische Balance, die Ceviches gelingen in jeder Schicht gleich, und die Kalkulationen mit frischem Fisch zum Tagespreis funktionieren in Echtzeit. Die Vorbereitung des Spezialmenüs zum 28. Juli mit Gastro Calendar hat unseren Umsatz verdreifacht.",
    "testimonialAuthor": "Carlos Fernández",
    "testimonialRole": "Koch und Inhaber, zeitgenössische peruanische Cevichería",
    "faqTitle": "Häufig gestellte Fragen für peruanische Restaurants",
    "faqs": [
      {
        "q": "Funktioniert es für eine lockere Cevichería, ein zeitgenössisches peruanisches Restaurant oder regionale Küche?",
        "a": "Für alle drei. Die Peruanische Küche deckt von der traditionellen Cevichería bis zur gehobenen Autorenküche ab, einschließlich regionaler Küche (Criolla, Costeña, Andina, Amazónica) mit authentischer Technik."
      },
      {
        "q": "Deckt es professionelle Ceviche- und Leche-de-tigre-Technik ab?",
        "a": "Ja. Die Peruanische Küche denkt wie ein professioneller Ceviche-Koch: Balance der Leche de tigre mit Säure, Schärfe und Salz; optimales Marinierfenster je nach Fischart; technische Integration der Chilis."
      },
      {
        "q": "Wie hilft es mir bei den schwankenden Kosten für frischen Fisch?",
        "a": "Kit de Escandallos Pro berechnet die echte Marge sofort neu, wenn Sie den Tagespreis für Fisch aktualisieren. Lebensmittelabfälle AI addiert die Prozessabfallkosten. So spiegelt das Ceviche immer die aktuellen Kosten wider."
      },
      {
        "q": "Erzeugt es visuelle Inhalte für Instagram, Glovo und Uber Eats?",
        "a": "Ja. GastroIMG Gen+ erzeugt professionelle Referenzbilder des Ceviche und Tiradito für Instagram, Web und Lieferdienste; besseres Foto = mehr Klicks. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz; das endgültige Foto machen Sie mit Ihrem real angerichteten Ceviche."
      },
      {
        "q": "Wie hilft es mir bei peruanischen Feiertagen und Veranstaltungen?",
        "a": "Gastro Calendar plant die wichtigsten Termine (28. Juli Unabhängigkeitstag, Tag des Ceviche, Tag des Pisco Sour, Mistura) mit speziellen Menüs und Redaktionskalender."
      }
    ],
    "ctaTitle": "Ihr peruanisches Restaurant mit echter Marge und authentischer Technik.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits, um alle Agenten zu nutzen.",
    "seo": {
      "title": "KI für peruanische Restaurants: Ceviches, Kalkulationen und authentische Technik | AI Chef Pro",
      "description": "KI-Suite für peruanische Restaurants: Peruanische Küche, Kalkulationen pro Ceviche, Planung von Feiertagen, Branding und APPCC. Starten Sie noch heute.",
      "keywords": "KI peruanisches Restaurant, Software Cevichería, Kalkulation Ceviche, peruanische Küche KI, Leche de tigre, gelbe Chili, 28. Juli peruanisch",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-peruano.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr peruanisches Restaurant zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen konversationellen Onboarding, bei dem Sie erzählen, welche Art von peruanischem Restaurant Sie betreiben (lockere Cevichería, zeitgenössisches peruanisches Restaurant, regionale Küche, andine Picantería, Polleria, Autorenrestaurant), Teamgröße, Stadt und Spezialität. Jeder Agent – von „Peruanische Küche“ bis „Gastro Calendar“ – antwortet angepasst an Ihr Produkt, Ihren Markt und Ihre reale Betriebsführung.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem peruanischen Restaurant nutzen werden",
    "apps": [
      {
        "name": "Peruanische Küche",
        "category": "Rezeptsammlungen Lateinamerika",
        "description": "Spezialisierter Agent für authentische peruanische Küche: Ceviches, Tiraditos, Causas, Anticuchos, Pachamanca."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Tiraditos und zeitgenössischen Gerichten mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Pairings mit Pisco, Weinen und Bier für Ihre peruanische Karte."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Operative Beratung für Cevicherías und peruanische Restaurants."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für Texturen und Technik, angewendet auf die peruanische Autorenküche."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Lebensmittelabfälle bei frischem Fisch, Meeresfrüchten, Chilis und Limetten."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung von Allergenen: Fisch, Meeresfrüchte, Gluten, Milchprodukte."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-Referenzfotografie für Gastronomie für Instagram, Web, Karte und Lieferdienste."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit professionellem Redaktionskalender für eine Autoren-Cevichería."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die nach „Cevichería in der Nähe“ oder „peruanisches Restaurant“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "28. Juli, Tag des Ceviche, Mistura, Tag des Pisco Sour."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Für die Pisco-Sour-Bar und peruanische Autoren-Cocktails."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "Marge nach Kalkulation der Ceviches"
      },
      {
        "value": "×3",
        "label": "Umsatz am 28. Juli"
      },
      {
        "value": "−25 %",
        "label": "Lebensmittelabfälle bei frischem Fisch"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre peruanische Küche"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierte Leche de tigre, inkonsistente Balance Schicht für Schicht",
        "Kalkulationen nicht an den Tagespreis für frischen Fisch angepasst",
        "Lebensmittelabfälle bei Fisch, Chilis und Meeresfrüchten ohne echte Rückverfolgbarkeit",
        "Reaktive Feiertage: Sie kommen am 28. Juli zu spät, ohne spezielles Menü",
        "Improvisiertes Instagram und Lieferplattformen mit Handyfotos"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Leche de tigre mit dokumentierter technischer Balance, konsistente Ceviches",
        "Echtzeit-Kalkulation mit dem Tagespreis für Fisch",
        "Kontrollierte Lebensmittelabfälle mit Lebensmittelabfälle AI und spezifischen Vorlagen",
        "Feiertage mit 8 Wochen Vorlauf geplant",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO gewinnen lokale Kunden"
      ]
    },
    "galleryTitle": "So funktioniert ein peruanisches Restaurant",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren werden: Ceviche, Tiradito, Anticucho, Chilis und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-peruano-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-ceviche.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-tiradito.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-anticucho.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-ajies.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-team.jpg"
    ]
  },
  "restaurante-japones": {
    "h1": "KI für japanische Restaurants",
    "heroSubtitle": "Entwickeln Sie Sushi, Ramen, Robata und Kaiseki mit authentischer Technik, kalkulieren Sie pro Stück mit echten Fischkosten, planen Sie die Fermentproduktion und erfassen Sie minimalistisches Branding mit einer Suite von gastronomischen KI-Agenten, die auf professionelle japanische Küche spezialisiert sind.",
    "heroTagline": "Japanische Küche mit echter Marge und authentischer Technik",
    "badge": "Für japanische Restaurants, Sushi-Bars und Ramen-Ya",
    "painsTitle": "Was ein japanisches Restaurant unbedingt lösen muss",
    "pains": [
      "Täglicher frischer Fisch für Sashimi und Sushi mit volatilen Kosten und strengen Verlusten durch Filetierprozess",
      "Shari (Sushi-Reis), Nigiri und Maki in jeder Schicht mit technischer Balance aus Essig, Zucker und Salz standardisieren",
      "Lange Brühen (Tonkotsu, Dashi, Shoyu, Miso), die stundenlanges Kochen und nächtliche Planung erfordern",
      "Professionelle Fermente (Koji, Miso, hausgemachtes Shoyu, Tsukemono), die Zeit und Rückverfolgbarkeit erfordern",
      "Sich in einem umkämpften Gebiet mit authentischer Technik vs. industriellem Sushi differenzieren, minimalistisches Branding und japanisches Storytelling",
      "Lieferbestellungen erfassen, ohne die Sushi-Qualität zu verlieren (optimales Zeitfenster 1-2 Stunden) und Omakase-Events mit Marge"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem japanischen Restaurant hilft",
    "features": [
      {
        "icon": "Fish",
        "title": "Japanische Küche",
        "description": "Spezialisierter Agent für authentische japanische Küche: Sushi, Sashimi, Ramen, Robata, Tempura, Kaiseki, Itamae-Technik und Fermentation."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Für Koji, Miso, hausgemachtes Shoyu, Amazake und fortgeschrittene Fermente der japanischen Küche."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für zeitgenössische Gerichte und Omakase mit japanischer Basis: Signature-Nigiri, kontrollierte Fusionen."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Stück",
        "description": "Japanische Küche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet es mit echten Kosten pro Nigiri, Ramen und Omakase."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Vorlagen: Fischfiletieren, Shari-Vorbereitung, nächtliche lange Brühen, Robata-Mise, Abschluss."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC japanisch",
        "description": "Rückverfolgbarkeit von Fisch für Sushi, Fermente, kritische Temperaturen und Konservierung."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planung mit wichtigen Daten: Hanami (Kirschblüte), japanisches Neujahr, Hina Matsuri, Tag des Sushi."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Minimalistische KI-Referenzfotografie + Instagram: Das japanische Restaurant lebt von der zen-artigen und klaren visuellen Wirkung."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Japonés",
        "description": "Premium-Download-Guide für 60 Plätze mit Kalkulationen, technischen Datenblättern, Finanzplan und spezifischer Betriebsführung."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem japanischen Restaurant mit AI Chef Pro",
    "workflow": [
      "07:00 · Eröffnung – Checkliste Kit de Tareas: Annahme von frischem Fisch, Filetieren von Sashimi-Blöcken, Kontrolle der über Nacht gekochten Tonkotsu-Brühe.",
      "09:00 · Japanische Küche – Sie entwickeln ein neues Signature-Nigiri mit Hamachi und Yuzu Kosho. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "10:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren tagesaktuellen Fischpreisen und frischem Wasabi hoch und validieren die Marge pro Nigiri und Omakase.",
      "11:00 · Fermentus mit AI+ – Sie überprüfen den Fortschritt des hausgemachten Miso (Monat 6 von 12) und das neue Koji in der Fermentationskammer.",
      "13:00 · Mittagsservice – Sushi-Bar in vollem Betrieb mit Itamae, der vor dem Gast arbeitet.",
      "17:00 · Pause zwischen den Services – Gastro Calendar plant das spezielle Hanami-Menü mit Sakura Mochi und Kirschblüten-Bento.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren das Referenzbild des neuen Nigiri und die minimalistischen Posts für Instagram.",
      "23:00 · Abschluss – gründliche Reinigung, APPCC unterschrieben, Tonkotsu-Vorbereitung für morgen (12 Stunden Kochzeit)."
    ],
    "productsTitle": "Vorlagen und empfohlene Kits für japanische Restaurants",
    "productIds": [
      "guia-restaurante-japones",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Japanische Küche hat unseren Betrieb verändert. Die Shari-Balance ist jetzt konsistent, das Tonkotsu gelingt jeden Tag gleich, und das Omakase hat eine professionelle Kalkulation mit validierter Marge Stück für Stück. Fermentus hat uns geholfen, das hausgemachte Miso-Programm aufzubauen, das unser Angebot völlig differenziert.",
    "testimonialAuthor": "Hiroshi Tanaka",
    "testimonialRole": "Itamae und Inhaber, zeitgenössisches japanisches Restaurant",
    "faqTitle": "Häufig gestellte Fragen für japanische Restaurants",
    "faqs": [
      {
        "q": "Funktioniert es für Sushi-Bar, Ramen-ya, Izakaya oder Kaiseki?",
        "a": "Für alle. Japanische Küche deckt von traditionellem Sushi bis zur gehobenen Kaiseki-Küche ab, einschließlich Ramen-ya, Robata und Izakaya mit authentischer Technik."
      },
      {
        "q": "Deckt es Itamae-Technik und japanische Fermentation ab?",
        "a": "Ja. Japanische Küche denkt wie ein professioneller Itamae: Filetiertechnik, Shari-Balance, Neta und Kombinationen; Fermentus deckt Koji, Miso, hausgemachtes Shoyu und Amazake mit professioneller Technik ab."
      },
      {
        "q": "Wie hilft es mir bei den variablen Kosten für Sashimi-Fisch?",
        "a": "Kit de Escandallos Pro berechnet die Marge sofort neu, wenn Sie den Tagespreis für Fisch aktualisieren. Lebensmittelabfälle AI addiert die Kosten für Verluste durch Filetieren. Das Nigiri spiegelt immer die aktuellen Kosten wider."
      },
      {
        "q": "Erzeugt es visuelle Inhalte für Instagram, Glovo und Uber Eats?",
        "a": "Ja. GastroIMG Gen+ erzeugt professionelle Referenzbilder des Sushi für Instagram, Web und Lieferung; besseres Foto = mehr Klicks. Denken Sie daran, dass das KI-Bild eine visuelle Referenz ist: Das endgültige Foto machen Sie mit Ihrem real angerichteten Stück."
      },
      {
        "q": "Wie hilft es mir bei japanischen Festlichkeiten?",
        "a": "Gastro Calendar plant die wichtigsten Daten (Hanami mit Sakura, japanisches Neujahr mit Osechi Ryori, Hina Matsuri, Tag des Sushi) mit speziellen Menüs und einem minimalistischen Redaktionskalender."
      }
    ],
    "ctaTitle": "Ihr japanisches Restaurant mit echter Marge und authentischer Technik.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für japanische Restaurants: Sushi, Kalkulation und Itamae-Technik | AI Chef Pro",
      "description": "KI-Suite für japanische Restaurants: Japanische Küche, Fermentus für Koji und Miso, Kalkulation pro Stück, Planung von Festlichkeiten. Starten Sie noch heute.",
      "keywords": "KI japanisches Restaurant, Sushi-Bar-Software, Sushi-Kalkulation, japanische Küche KI, Koji Miso Shoyu, Ramen Tonkotsu, professioneller Itamae",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-japones.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr japanisches Restaurant personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen konversationellen Onboarding, bei dem Sie uns mitteilen, welche Art von japanischem Restaurant Sie betreiben (Sushi-Bar, Ramen-ya, Izakaya, Kaiseki, Omakase, zeitgenössische japanische Autorenküche), Teamgröße, Stadt und Spezialität. Jeder Agent – von Japanische Küche bis Gastro Calendar – antwortet angepasst an Ihr Produkt, Ihren Markt und Ihre reale Betriebsweise.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem japanischen Restaurant einsetzen werden",
    "apps": [
      {
        "name": "Japanische Küche",
        "category": "Asiatische Rezeptsammlungen",
        "description": "Spezialisierter Agent für authentische japanische Küche: Sushi, Sashimi, Ramen, Robata, Kaiseki."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Koji, Miso, hausgemachtes Shoyu, Amazake und fortgeschrittene Fermente."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Nigiri und Omakase mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Pairings mit Sake, japanischem Whisky, Bier und Weinen für Ihre Speisekarte."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für Texturen und Technik, angewendet auf japanische Autorenküche."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Verluste beim Filetieren von Fisch, Sashimi und langen Brühen."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung von Allergenen: Fisch, Meeresfrüchte, Soja, Gluten, Sesam."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Minimalistische KI-Referenzfotografie für Instagram, Web, Speisekarte und Lieferung."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit minimalistischen Redaktionskalender für eine Autoren-Sushi-Bar."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die nach \"Sushi in der Nähe\" oder \"Ramen in der Nähe\" suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Hanami, japanisches Neujahr, Hina Matsuri, Tag des Sushi."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Für die Sake-Bar, japanischen Whisky und Cocktails mit japanischer Basis."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "Marge nach Kalkulation von Omakase"
      },
      {
        "value": "×3",
        "label": "Instagram-Engagement mit GastroIMG"
      },
      {
        "value": "−20 %",
        "label": "Verluste beim Filetieren von Fisch"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre japanische Küche"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierte Shari und Technik, inkonsistente Balance zwischen Itamae",
        "Kalkulationen nicht an den Tagespreis für Fisch angepasst",
        "Lange Brühen (Tonkotsu) ohne Rückverfolgbarkeit und strenge Planung",
        "Hausgemachte Fermente (Miso, Shoyu) ohne dokumentiertes Programm",
        "Improvisiertes Instagram und Lieferplattformen mit Handyfotos"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Shari, Neta und Technik mit professionellem Anspruch, Konsistenz Schicht für Schicht",
        "Echtzeit-Kalkulation mit Tagespreis für Fisch",
        "Lange Brühen mit spezifischen Vorlagen geplant und APPCC unterschrieben",
        "Fermentprogramm mit Fermentus mit AI+ professionell dokumentiert",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO gewinnen lokale Kunden"
      ]
    },
    "galleryTitle": "So funktioniert ein japanisches Restaurant",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Sushi, Ramen, Robata, Zutaten und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-japones-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-sushi.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-ramen.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-robata.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-ingredientes.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-team.jpg"
    ]
  },
  "restaurante-nikkei": {
    "h1": "KI für Nikkei-Restaurants",
    "heroSubtitle": "Entwickeln Sie Nikkei-Tiraditos, Fusions-Sushi und Robata mit authentischer peruanisch-japanischer Technik, kalkulieren Sie jedes Gericht mit echten Kosten und sichern Sie sich professionelles Branding mit einer Suite spezialisierter gastronomischer KI-Agenten für die Nikkei-Küche.",
    "heroTagline": "Nikkei-Küche mit echter Marge und authentischer Technik",
    "badge": "Für Nikkei-Restaurants und peruanisch-japanische Fusionsküche",
    "painsTitle": "Was ein Nikkei-Restaurant unbedingt lösen muss",
    "pains": [
      "Komplexe peruanisch-japanische Kombinationen mit präziser Balance von Ají Amarillo, Yuzu, Miso, Ponzu und Shoyu",
      "Täglich frischer Fisch für Tiraditos und Sushi mit volatilen Kosten, rigoroses Filetieren und Itamae-Technik angewendet auf die peruanische Küche",
      "Standardisierung von Signature-Tiraditos, Nikkei-Sushi und Anticuchos mit Miso-Ají-Panca-Marinade Schicht für Schicht",
      "Kalkulation von Gerichten mit importierten Zutaten (Ají Amarillo, Ají Panca, Yuzu, Dashi), deren Kosten saisonal variieren",
      "Abhebung von traditioneller japanischer oder reiner peruanischer Küche durch authentisches Fusions-Storytelling und visuelles Autoren-Branding",
      "Gewinnung von Nikkei-Omakase-Bestellungen und Events bei gleichbleibender Qualität des rohen Produkts"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem Nikkei-Restaurant hilft",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Japanische Küche + Peruanische Küche",
        "description": "Kombination spezialisierter Agenten für beide Kulturen: Itamae-Technik angewendet auf peruanische Tiraditos, Ají Amarillo in Nigiri, Miso-Anticuchos."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Für hausgemachtes Koji, Miso, Shoyu, angepasst an die Nikkei-Fusion mit Ají Panca und Huacatay."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Pairings mit Sake, Pisco, chilenischen Weinen und japanischem Bier für Ihre Nikkei-Karte."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Gericht",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet es mit echten Kosten pro Tiradito und Nikkei-Omakase."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Vorlagen: Filetieren von Fisch, Vorbereitung von Leche de Tigre mit Yuzu, Nikkei-Marinade, Robata-Mise-en-Place, Abschluss."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Nikkei",
        "description": "Rückverfolgbarkeit von Fisch, Fermenten, Ajíes und kritischen Temperaturen bei rohem Produkt."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Kreuzplanung: japanische und peruanische Feiertage, Fusions-Events, saisonales Nikkei-Omakase."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Redaktionelle KI-Referenzfotografie + Instagram: Nikkei lebt von der visuellen Wirkung von Farbe und Komposition."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Nikkei",
        "description": "Premium-Guía zum Download für 60 Plätze mit Kalkulationen, technischen Datenblättern, Finanzplan und nikkei-spezifischer Betriebsführung."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem Nikkei-Restaurant mit AI Chef Pro",
    "workflow": [
      "07:00 · Eröffnung – Checkliste Kit de Tareas: Annahme von frischem Fisch, Filetieren für Tiraditos und Nigiri, Vorbereitung von Leche de Tigre mit Yuzu, Marinade für Miso-Panca-Anticuchos.",
      "09:00 · Japanische Küche + Peruanische Küche – Sie entwickeln ein neues Hamachi-Tiradito mit Yuzu-Leche-de-Tigre und Ají Amarillo. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "10:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren tagesaktuellen Fischpreisen, Ají Amarillo und Yuzu hoch und validieren die Marge pro Tiradito und Nikkei-Omakase.",
      "11:00 · Fermentus mit AI+ – Sie überprüfen den Fortschritt des hausgemachten Miso mit Ají Panca (Monat 4 von 8).",
      "12:00 · Food Pairing AI – Sie validieren das Pairing des neuen Tiraditos mit einem Junmai-Sake und einem in Shiso-Blättern mazerierten Pisco.",
      "13:00 · Mittagsservice – Robata in vollem Betrieb mit Miso-Anticuchos, Sushi-Bar arbeitet an Signature-Tiraditos.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren das Referenzbild des neuen Nikkei-Tiraditos und die redaktionellen Posts für Instagram.",
      "23:00 · Abschluss – gründliche Reinigung, APPCC unterschrieben, kontrollierte Entsorgung, Vorbereitung für morgen."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Nikkei-Restaurants",
    "productIds": [
      "guia-restaurante-nikkei",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Japanische Küche + Peruanische Küche im Agentenverbund hat unser Konzept verändert. Die Tiraditos haben jetzt ein dokumentiertes technisches Gleichgewicht, das Nikkei-Omakase kommt mit Stück für Stück validiertem Kalkulationsblatt heraus, und das hausgemachte Miso-Programm mit Ají Panca von Fermentus macht uns völlig einzigartig. Wir haben die Marge um 7 Punkte gesteigert.",
    "testimonialAuthor": "Yui Sato",
    "testimonialRole": "Köchin und Inhaberin, Nikkei-Restaurant mit Autorenküche",
    "faqTitle": "Häufig gestellte Fragen zu Nikkei-Restaurants",
    "faqs": [
      {
        "q": "Funktioniert es für zeitgenössisches Nikkei, Nikkei-Sushi-Bar oder Cevichería mit japanischer Technik?",
        "a": "Für alle drei. Japanische Küche + Peruanische Küche ergänzen sich, um von Nikkei-Sushi bis zu Tiraditos mit mit Yuzu oder Ponzu fusionierter Leche de Tigre abzudecken."
      },
      {
        "q": "Wie hilft es mir bei der Balance zwischen peruanischer und japanischer Technik?",
        "a": "Kreativküche orchestriert die beiden Agenten: Es denkt in authentischer Fusion (keine verworrene Fusion), respektiert die Itamae-Technik für rohes Produkt und die peruanische Balance für Leche de Tigre und Marinaden."
      },
      {
        "q": "Wie verwalte ich die variablen Kosten von Fisch und importierten peruanischen Zutaten?",
        "a": "Kit de Escandallos Pro berechnet die Marge sofort neu, wenn Sie die Preise für Tagesfisch und Ajíes/Yuzu aktualisieren. Lebensmittelabfälle AI addiert die Kosten für Prozessabfälle."
      },
      {
        "q": "Erzeugt es visuelle Inhalte für Instagram und Lieferung?",
        "a": "Ja. GastroIMG Gen+ erzeugt professionelle Referenzbilder des Nikkei-Tiraditos für Instagram, Web und Lieferung. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie selbst mit Ihrem real angerichteten Gericht."
      },
      {
        "q": "Wie hilft es mir bei peruanisch-japanischen Feiertagen?",
        "a": "Gastro Calendar plant die Schlüsseldaten beider Kulturen (peruanischer 28. Juli, japanisches Hanami, Ceviche-Tag, japanisches Neujahr) mit saisonalem Nikkei-Omakase und Fusions-Storytelling."
      }
    ],
    "ctaTitle": "Ihr Nikkei-Restaurant mit echter Marge und authentischer Technik.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für die Nutzung aller Agenten.",
    "seo": {
      "title": "KI für Nikkei-Restaurants: Tiraditos, Kalkulationen und Fusionstechnik | AI Chef Pro",
      "description": "KI-Suite für Nikkei-Restaurants: Japanische + Peruanische Küche, Kalkulation pro Tiradito, Nikkei-Omakase, Branding und APPCC. Starten Sie noch heute.",
      "keywords": "KI Nikkei-Restaurant, Nikkei-Software, Kalkulation Nikkei-Tiradito, Nikkei-Küche KI, Ají Amarillo Yuzu, Nikkei-Sushi, peruanisch-japanische Fusion",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-nikkei.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Nikkei-Restaurant personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational Onboarding, bei dem Sie erzählen, welche Art von Nikkei Sie betreiben (zeitgenössisches Nikkei mit eigener Handschrift, Nikkei-Sushi-Bar, Cevichería mit japanischer Technik, Nikkei-Omakase), Teamgröße, Stadt und Spezialität. Jeder Agent antwortet angepasst an Ihr Produkt, Ihren Markt und Ihren realen Betrieb.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Nikkei-Restaurant nutzen werden",
    "apps": [
      {
        "name": "Japanische Küche",
        "category": "Rezeptsammlungen Asien",
        "description": "Itamae-Technik, Filetieren, Sushi, Sashimi und Robata, angewendet auf die Nikkei-Fusion."
      },
      {
        "name": "Peruanische Küche",
        "category": "Rezeptsammlungen Lateinamerika",
        "description": "Cebiches, Tiraditos, Anticuchos und peruanische Technik, angewendet auf die Nikkei-Fusion."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Fusions-Orchestrator: Signature-Tiraditos, Nikkei-Sushi, Omakase mit authentischer Basis."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Koji, hausgemachtes Miso mit Ají Panca, Shoyu und gekreuzte Fermente."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Pairings mit Sake, Pisco, chilenischen Weinen und japanischem Bier."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für Texturen und Technik, angewendet auf die autorenorientierte Nikkei-Küche."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Abfälle beim Filetieren von Fisch, bei Ajíes und langen Marinaden."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung von Allergenen: Fisch, Meeresfrüchte, Soja, Gluten, Sesam, Nüsse."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Redaktionelle KI-Referenzfotografie für Instagram, Web, Speisekarte und Lieferung."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit professionellem Redaktionskalender für autorenorientiertes Nikkei."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die bei Google und Maps nach „Nikkei in der Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Gekreuzte Feiertage: Hanami, 28. Juli, Ceviche-Tag, japanisches Neujahr."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "Marge nach Kalkulation des Nikkei-Omakase"
      },
      {
        "value": "×3",
        "label": "Instagram-Engagement mit GastroIMG"
      },
      {
        "value": "−25 %",
        "label": "Abfälle bei Fisch und Ajíes"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Nikkei-Küche"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierte Fusion ohne technische Balance zwischen den Kulturen",
        "Kalkulationen nicht aktualisiert auf die Preise von Fisch und Ajíes",
        "Nikkei-Sushi und Tiraditos mit schwankender Konsistenz zwischen den Schichten",
        "Hausgemachtes Fermentprogramm ohne professionelle Dokumentation",
        "Improvisiertes Instagram ohne authentisches Fusions-Storytelling"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Authentische Fusion mit dokumentierter Technik beider Kulturen",
        "Echtzeit-Kalkulation mit aktualisierten Preisen",
        "Nikkei-Sushi und Tiraditos mit konsistenter technischer Balance",
        "Fermentus-Programm mit professionell dokumentiertem Miso-Ají-Panca",
        "GastroIMG Gen+ + InstaFlow + authentisches Nikkei-Fusions-Storytelling"
      ]
    },
    "galleryTitle": "So funktioniert ein Nikkei-Restaurant",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren werden: Tiraditos, Nikkei-Sushi, Miso-Anticuchos, Zutaten und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-nikkei-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-tiradito.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-sushi.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-anticucho.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-ingredientes.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-team.jpg"
    ]
  },
  "restaurante-plant-based": {
    "h1": "KI für Plant-Based- und vegane Restaurants",
    "heroSubtitle": "Entwickeln Sie Plant-Based-Menüs mit Nährstoffbalance, kalkulieren Sie Bowls und vegane Burger mit echten Kosten, planen Sie pflanzliche Fermente und gewinnen Sie frisches Branding mit einer Suite gastronomischer KI-Agenten, die auf professionelle Plant-Based-Küche spezialisiert sind.",
    "heroTagline": "Pflanzliche Küche mit echter Marge und fortgeschrittener Technik",
    "badge": "Für Plant-Based-, vegane und Healthy-Restaurants",
    "painsTitle": "Was ein Plant-Based-Restaurant unbedingt lösen muss",
    "pains": [
      "Tiefes Umami in 100% pflanzlicher Küche mit Fermenten, Räucheraromen, Koji und fortgeschrittener Technik (ohne industrielle Abkürzungen)",
      "Bowls, vegane Burger und Plant-Based-Gerichte mit vielen Topping-Varianten und pflanzlichen Proteinen kalkulieren",
      "Hohe Verluste bei frischen Produkten (saisonales Gemüse, Obst, Kräuter, Microgreens) mit kurzer Haltbarkeit",
      "Hausgemachte pflanzliche Proteine (Seitan, Tempeh, marinierten Tofu, Mock Meats) und Plant-Based-Toppings/Saucen standardisieren",
      "Sich in einem umkämpften Gebiet mit kreativem Plant-Based-Menü, frischem visuellem Branding und nachhaltigem Storytelling differenzieren",
      "Delivery-Bestellungen mit frischen Produkten gewinnen und dabei Präsentation und Qualität des Bowls erhalten"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem Plant-Based-Restaurant hilft",
    "features": [
      {
        "icon": "Sprout",
        "title": "VegChef Plant-Based",
        "description": "Spezialisierter Agent für professionelle Plant-Based-, vegane und vegetarische Küche: Bowls, Burger, pflanzliche Proteine, fortgeschrittene Technik."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Für pflanzliches Koji, hausgemachtes Miso, Shoyu, Kimchi, Kombucha, Lactofermente und tiefes Umami ohne tierische Produkte."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für zeitgenössische und kreative Plant-Based-Gerichte mit pflanzlicher Basis: Signature Bowls, vegane Desserts, Fusionen."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Kombinationen mit veganen Weinen, Kombucha und funktionellen Getränken für Ihre Plant-Based-Karte."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation für Bowls und Burger",
        "description": "VegChef liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet es mit echten Kosten pro Bowl, Food-Cost-Prozentsatz und empfohlenem Preis."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Vorlagen: Vorbereitung pflanzlicher Proteine, Fermente, Mise en Place frischer Toppings, Marinaden, Abschluss."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC plant-based",
        "description": "Rückverfolgbarkeit von Fermenten, hausgemachten pflanzlichen Proteinen, frischen Kräutern und kritischen Temperaturen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planung mit wichtigen Terminen: Veganuary (Januar), Weltvegantag, Earth Day, Saisonzeiten lokaler Gemüsesorten."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Lebendige KI-Referenzfotografie + Instagram: Plant-Based lebt von der visuellen Wirkung der Farbe."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem Plant-Based-Restaurant mit AI Chef Pro",
    "workflow": [
      "07:00 · Eröffnung – Checkliste Kit de Tareas: Überprüfung der Fermente im Kühlraum, Vorbereitung pflanzlicher Proteine (Seitan, Tempeh), Tofu-Marinaden, Mise en Place von Microgreens und essbaren Blüten.",
      "09:00 · VegChef Plant-Based – Sie entwickeln einen neuen Signature Bowl mit Quinoa, Grünkohl, mariniertem Tempeh, hausgemachtem Kimchi und Kurkuma-Tahini. Kreativküche liefert Rezept + CSV-Kalkulation.",
      "10:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren echten Preisen für Quinoa, Grünkohl, Tempeh und Tahini hoch, validieren Marge pro Bowl und Food-Cost-Prozentsatz.",
      "11:00 · Fermentus mit AI+ – Sie überprüfen den Fortschritt des hausgemachten Miso (Monat 6 von 12), des pflanzlichen Koji und des neuen Kimchi in der Fermentationskammer.",
      "12:00 · Food Pairing AI – Sie validieren die Kombination des neuen Bowls mit Ingwer-Kombucha und einem veganen Weißwein.",
      "13:00 · Mittagsservice – Bowls in vollem Betrieb, vegane Burger auf dem Grill, Mise en Place frischer Toppings.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren das Referenzbild des neuen Bowls und die lebendigen Posts für Instagram.",
      "22:00 · Abschluss – gründliche Reinigung, APPCC unterschrieben, Vorbereitung der Fermente für die nächtliche Fermentation."
    ],
    "productsTitle": "Vorlagen und empfohlene Kits für Plant-Based-Restaurants",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "VegChef + Fermentus haben unser Angebot verändert. Wir erreichen tiefes Umami ohne industrielle Abkürzungen dank hausgemachtem Miso und pflanzlichem Koji, und die Bowl-Kalkulationen mit mariniertem Tempeh bestätigen uns, dass Plant-Based eine hohe Marge haben kann. Wir sind um 6 Punkte gestiegen und die Instagram-Akquise mit GastroIMG ist x3.",
    "testimonialAuthor": "Lucía Ferrer",
    "testimonialRole": "Köchin und Inhaberin, kreatives Plant-Based-Restaurant",
    "faqTitle": "Häufige Fragen von Plant-Based-Restaurants",
    "faqs": [
      {
        "q": "Gilt das für Casual Healthy Bowls, veganes Fine Dining oder kreative Plant-Based-Küche?",
        "a": "Für alle drei. VegChef deckt von Casual Bowls bis zur veganen Haute Cuisine ab, einschließlich Plant-Based-Burgerläden, Küche mit fortgeschrittener Technik und professionellen veganen Desserts."
      },
      {
        "q": "Wie erreicht man tiefes Umami in 100% pflanzlicher Küche?",
        "a": "Fermentus mit AI+ deckt pflanzliches Koji, hausgemachtes Miso, Shoyu, Kimchi, Kombucha und Lactofermente mit professioneller Technik ab. VegChef integriert kontrollierte Räucheraromen, Dehydriertes, Pilzkrusten und lange pflanzliche Brühen."
      },
      {
        "q": "Deckt es hausgemachte pflanzliche Proteine ab (Seitan, Tempeh, marinierten Tofu)?",
        "a": "Ja. VegChef denkt wie ein professioneller Plant-Based-Koch: Techniken für gekneteten Seitan, fermentierten Tempeh, marinierten und gepressten Tofu, Mock Meats mit Texturtechnik."
      },
      {
        "q": "Erzeugt es visuelle Inhalte für Instagram, Glovo und Uber Eats?",
        "a": "Ja. GastroIMG Gen+ erzeugt lebendige Referenzbilder der Bowls für Instagram, Web und Delivery; Plant-Based lebt von der Farbe. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie mit Ihrem real angerichteten Bowl."
      },
      {
        "q": "Wie hilft es mir bei Veganuary und Plant-Based-Events?",
        "a": "Gastro Calendar plant Veganuary (Januar), Weltvegantag, Earth Day und Saisonzeiten lokaler Gemüsesorten mit speziellen Menüs und Redaktionskalender."
      }
    ],
    "ctaTitle": "Ihr Plant-Based-Restaurant mit echter Marge und kreativer Technik.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Plant-Based- und vegane Restaurants: Bowls, Kalkulationen und Fermente | AI Chef Pro",
      "description": "KI-Suite für Plant-Based-Restaurants: VegChef, Fermentus für pflanzliches Umami, Bowl-Kalkulationen, Branding und APPCC. Starten Sie noch heute.",
      "keywords": "KI veganes Restaurant, Plant-Based-Software, vegane Bowl-Kalkulation, vegane KI-Küche, pflanzliche Fermente, pflanzliches Umami, Veganuary",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-plant-based.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Plant-Based-Restaurant personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational-Onboarding, bei dem Sie erzählen, welche Art von Plant-Based Sie betreiben (casual healthy bowls, veganes Fine Dining, Plant-Based-Burgerladen, veganes Autoren-Restaurant, veganes Café, vegane Dark Kitchen), Teamgröße, Stadt und Spezialität. Jeder Agent antwortet angepasst an Ihr Produkt, Ihren Markt und Ihren realen Betrieb.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Plant-Based-Restaurant nutzen werden",
    "apps": [
      {
        "name": "VegChef Plant-Based",
        "category": "Kulinarische Kreativität",
        "description": "Spezialisierter Agent für professionelle Plant-Based-, vegane und vegetarische Küche mit fortgeschrittener Technik."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Pflanzliches Koji, hausgemachtes Miso, Shoyu, Kimchi, Kombucha und Lactofermente für tiefes Umami."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature Bowls und zeitgenössischen Plant-Based-Gerichten."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Kombinationen mit veganen Weinen, Kombucha und funktionellen Getränken."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Operative Beratung für Casual Plant-Based-Restaurants."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für pflanzliche Texturen, Plant-Based-Geliermittel und Technik."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Verluste bei frischen pflanzlichen Produkten, Microgreens und hausgemachten Proteinen."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung: Gluten, Nüsse, Soja, Sesam (frei von tierischen Produkten)."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Lebendige KI-Referenzfotografie für Instagram, Web, Speisekarte und Delivery."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit lebendigem Redaktionskalender für kreatives Plant-Based."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die nach \"vegan in der Nähe\" oder \"Plant-Based in der Nähe\" suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Veganuary, Weltvegantag, Earth Day, Gemüsesaisonen."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "Marge nach Bowl-Kalkulation"
      },
      {
        "value": "×3",
        "label": "Instagram-Engagement mit GastroIMG"
      },
      {
        "value": "−30 %",
        "label": "Verluste bei frischen Produkten"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Plant-Based-Küche"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Oberflächliches Umami ohne professionelle Fermentationstechnik",
        "Kalkulationen ohne echte Food Costs, Signature Bowls unwissentlich mit Verlust",
        "Verluste bei frischen pflanzlichen Produkten ohne Rückverfolgbarkeit",
        "Improvisierte hausgemachte pflanzliche Proteine ohne Standardisierung",
        "Improvisiertes Instagram und Delivery-Plattformen mit Handyfotos"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Tiefes Umami mit Fermentus: dokumentiertes hausgemachtes Miso, Koji, Kimchi",
        "Professionelle Bowl-Kalkulation mit validierter Marge",
        "Kontrollierte Verluste mit Lebensmittelabfälle AI und spezifischen Vorlagen",
        "Pflanzliche Proteine mit dokumentierter Technik (Seitan, Tempeh, Tofu)",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO gewinnen lokale Kunden"
      ]
    },
    "galleryTitle": "Wie ein Plant-Based-Restaurant funktioniert",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Bowls, vegane Burger, Fermente, Markt und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-plantbased-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-burger.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-bowl.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-fermentos.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-mercado.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-team.jpg"
    ]
  },
  "asador-parrilla": {
    "h1": "KI für Grillrestaurant, Parrilla und Steakhouse",
    "heroSubtitle": "Entwickeln Sie Grillrestaurant-Karten mit Gluttechnik, Kalkulation pro Schnitt mit echten Kosten, verwalten Sie Dry-Aged und planen Sie die Produktion mit einer Suite von gastronomischen KI-Agenten, die auf Feuerküche, Grillrestaurant und professionelles Steakhouse spezialisiert sind.",
    "heroTagline": "Grillrestaurant mit echter Marge und Feuertechnik",
    "badge": "Für Grillrestaurants, Parrillas, Steakhäuser und Churrascarias",
    "painsTitle": "Was ein Grillrestaurant unbedingt lösen muss",
    "pains": [
      "Volatile Fleischkosten (Chuletón, Picanha, Ribeye, T-Bone), die die Kalkulation jede Woche ändern",
      "Standardisierung von Garstufe und Gluttechnik Schicht für Schicht (Zerlegung, Dry-Aged, Marmorierung, Kerntemperatur)",
      "Schwund bei Zerlegung, Dry-Aging (3-12 % pro Woche), Trimmen und Beilagen",
      "Verwaltung des Dry-Aged mit Kammer, Feuchtigkeit, Temperatur und Rotation der Schnitte",
      "Differenzierung in umkämpfter Gegend mit Premium-Schnitten, Gluttechnik und Storytelling von Viehzuchtlieferanten",
      "Gewinnung von Firmenkunden und privaten Veranstaltungen mit margenstarken Grillrestaurant-Menüs"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem Grillrestaurant hilft",
    "features": [
      {
        "icon": "Flame",
        "title": "Kreativküche",
        "description": "Agent zur Entwicklung von Grillrestaurant-Karten mit Gluttechnik, Marinaden, Saucen und professionellen Beilagen."
      },
      {
        "icon": "UtensilsCrossed",
        "title": "Argentinische Küche + Brasilianische Küche",
        "description": "Spezialisierte Rezeptsammlungen: argentinisches Asado mit grobem Salz, brasilianische Picanha, Churrasco, authentisches Chimichurri, Farofa, Vinaigretten."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Weinbegleitungen mit Premium-Rotweinen, Whisky und charaktervoller Cocktailkultur für Ihr Grillrestaurant."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Schnitt",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet es mit echten Kosten für Chuletón, Picanha und T-Bone."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Vorlagen: Anzünden der Glut, Zerlegung, Dry-Aged-Kontrolle, Mise-en-place für Beilagen, Schließung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC für Grillrestaurants",
        "description": "Rückverfolgbarkeit von Fleisch, Dry-Aging, kritische Temperaturen in der Kammer und Kerntemperatur beim Garen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planung mit wichtigen Terminen: Vatertag (Chuletón), Weihnachten, Firmenveranstaltungen, Einführung saisonaler Spezialschnitte."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Premium-KI-Referenzfotografie + Instagram: Das Grillrestaurant lebt von der visuellen Wirkung von Glut und Schnitt."
      },
      {
        "icon": "BarChart3",
        "title": "Lebensmittelabfälle AI",
        "description": "Präzise Daten zu Schwund bei Zerlegung, Dry-Aging und Trimmen, integriert in die Kalkulation."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem Grillrestaurant mit AI Chef Pro",
    "workflow": [
      "09:00 · Öffnung – Checkliste Kit de Tareas: kontrolliertes Anzünden der Glut (3 Stunden bis zum richtigen Punkt), Kontrolle der Dry-Aged-Kammer, Zerlegung der Schnitte für den Service.",
      "11:00 · Kreativküche + Argentinische Küche – Sie entwickeln einen neuen Signature-Cut aus galicischem Dry-Aged-Chuletón (60 Tage) mit geräuchertem Maldon-Salz und Chimichurri aus frischen Kräutern. Rezept + CSV-Kalkulation.",
      "12:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren echten Fleisch- und Dry-Aged-Preisen hoch, berechnen den Schwund durch Aging und validieren die Marge pro Schnitt.",
      "13:00 · Mittagsservice – Grill auf Hochtouren mit Premium-Schnitten, Mise-en-place für Chimichurri, Saucen und Beilagen.",
      "17:00 · Pause zwischen den Services – Bar & Lounge AI+ validiert Weinbegleitungen mit Rotweinen für die neuen Schnitte; Gastro Calendar plant das spezielle Vatertagsmenü.",
      "20:00 · Abendservice – koordinierte Spitzenzeiten, Grill mit mehreren Schnitten gleichzeitig.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren das Referenzbild des neuen Chuletón und die Posts für Instagram.",
      "00:00 · Schließung – gründliche Reinigung der Grills, APPCC unterschrieben, Kontrolle der Dry-Aged-Kammer."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Grillrestaurants",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Wir haben Schnitt für Schnitt kalkuliert und festgestellt, dass das T-Bone, das wir am meisten verkauften, tatsächlich Verluste machte, weil wir den Schwund des Dry-Aged nicht berechnet hatten. Wir haben es mit Kreativküche neu gestaltet, Portion und Beilagen angepasst, ohne den Preis zu ändern, und die Marge um 5 Punkte erhöht. Die Planung des Vatertags mit Gastro Calendar hat unseren Umsatz in dieser Woche verdreifacht.",
    "testimonialAuthor": "Pedro Aguirre",
    "testimonialRole": "Grillmeister und Inhaber, Premium-Grillrestaurant",
    "faqTitle": "Häufig gestellte Fragen von Grillrestaurant-Betreibern",
    "faqs": [
      {
        "q": "Funktioniert es für lockeres Grillrestaurant, argentinische Parrilla, brasilianische Churrascaria oder Premium-Steakhouse?",
        "a": "Für alle vier. Kreativküche + Argentinische Küche + Brasilianische Küche decken vom lockeren Grillrestaurant bis zum Premium-Steakhouse mit Dry-Aged-Schnitten ab, einschließlich traditioneller argentinischer Parrilla und brasilianischer Churrascaria mit Spießen."
      },
      {
        "q": "Deckt es Dry-Aged-Technik und Kammerverwaltung ab?",
        "a": "Ja. Kreativküche denkt wie ein professioneller Grillmeister: Dry-Aged-Kammerbedingungen (1-3 °C, 75-85 % Luftfeuchtigkeit), Zeiten pro Schnitt, wöchentliche Schwundkontrolle, Erkennung von Pellicle und Rotation."
      },
      {
        "q": "Wie verwalte ich die volatilen Fleischkosten?",
        "a": "Kit de Escandallos Pro berechnet die Marge sofort neu, wenn Sie den Fleischpreis aktualisieren. Lebensmittelabfälle AI fügt die Kosten für Schwund durch Dry-Aging, Zerlegung und Trimmen hinzu. Der Schnitt spiegelt immer die aktuellen Kosten wider."
      },
      {
        "q": "Erzeugt es visuelle Inhalte für Instagram und Firmenveranstaltungen?",
        "a": "Ja. GastroIMG Gen+ erzeugt professionelle Referenzbilder von Schnitten und Glut für Instagram, Web und Speisekarte; das Grillrestaurant lebt von der visuellen Wirkung. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie mit Ihrem echten Schnitt."
      },
      {
        "q": "Wie hilft es mir bei Veranstaltungen und Feiertagen?",
        "a": "Gastro Calendar plant Vatertag, Weihnachten, Firmenveranstaltungen und Einführungen spezieller Schnitte mit Grillrestaurant-Menüs und Redaktionskalender."
      }
    ],
    "ctaTitle": "Ihr Grillrestaurant mit echter Marge und Feuertechnik.",
    "ctaSubtitle": "Beginnen Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits für alle Agenten.",
    "seo": {
      "title": "KI für Grillrestaurant, Parrilla und Steakhouse: Schnitte, Kalkulationen und Dry-Aged | AI Chef Pro",
      "description": "KI-Suite für Grillrestaurants und Steakhäuser: Argentinische + Brasilianische Küche, Kalkulation pro Schnitt, Dry-Aged, Branding und APPCC. Starten Sie noch heute.",
      "keywords": "KI Grillrestaurant, Steakhouse-Software, Chuletón-Kalkulation, argentinische Parrilla KI, Dry-Aged, Churrascaria, Premium-Grillrestaurant",
      "ogImage": "https://aichef.pro/og/use-cases/asador-parrilla-steakhouse.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Grillrestaurant personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Conversational-Onboarding, bei dem Sie erzählen, welche Art von Grillrestaurant Sie betreiben (argentinische Parrilla, brasilianische Churrascaria, Premium-Steakhouse mit Dry-Aged, lockeres Grillrestaurant im Viertel, Grillrestaurant mit Autorenküche), Teamgröße, Stadt und Spezialität. Jeder Agent antwortet angepasst an Ihr Produkt, Ihren Markt und Ihre reale Betriebsweise.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Grillrestaurant verwenden werden",
    "apps": [
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Grillrestaurant-Karten mit Gluttechnik, Marinaden und professionellen Beilagen."
      },
      {
        "name": "Argentinische Küche",
        "category": "Rezeptsammlungen Lateinamerika",
        "description": "Argentinisches Asado, Chimichurri, Provolone, Mollejas und authentische Parrilla-Technik."
      },
      {
        "name": "Brasilianische Küche",
        "category": "Rezeptsammlungen Lateinamerika",
        "description": "Picanha, Churrasco, Farofa, Vinagrete und brasilianische Churrascaria-Technik."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Weinbegleitungen mit kräftigen Rotweinen, Whisky und charaktervoller Cocktailkultur für Grillrestaurants."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Für die Bar des Grillrestaurants mit Premium-Rotweinen und charaktervoller Cocktailkultur."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für Texturen, Gewürzsalze und Techniken für Saucen und Marinaden."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Schwund bei Zerlegung, Dry-Aging, Trimmen und Garen."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Schnitt und Beilage."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Premium-KI-Referenzfotografie für Instagram, Web, Speisekarte und Lieferung."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit professionellem Redaktionskalender für Premium-Grillrestaurants."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die nach „Grillrestaurant in der Nähe“ oder „argentinische Parrilla“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Vatertag, Weihnachten, Firmenveranstaltungen, saisonale Einführungen."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach Kalkulation der Schnitte"
      },
      {
        "value": "×3",
        "label": "Umsatz am Vatertag"
      },
      {
        "value": "−15 %",
        "label": "Schwund bei Zerlegung und Dry-Aging"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihr Grillrestaurant"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierter Garzustand, variable Konsistenz zwischen Grillmeister und Schicht",
        "Kalkulationen ohne Dry-Aged-Schwund, Premium-Schnitte mit Verlust, ohne es zu wissen",
        "Dry-Aged-Kammer ohne echte Rückverfolgbarkeit und dokumentierte Kontrolle",
        "Schwund bei Zerlegung und Trimmen ohne Rückverfolgbarkeit",
        "Improvisiertes Instagram, ohne Storytelling des Viehzuchtlieferanten"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Konsistenter Garzustand mit dokumentiertem technischem Kriterium",
        "Professionelle Kalkulation pro Schnitt mit integriertem Dry-Aged-Schwund",
        "Dry-Aged-Kammer mit APPCC-Rückverfolgbarkeit und dokumentierter Rotation",
        "Schwund kontrolliert mit Lebensmittelabfälle AI und spezifischen Vorlagen",
        "GastroIMG Gen+ + InstaFlow + Storytelling des Viehzuchtlieferanten"
      ]
    },
    "galleryTitle": "So funktioniert ein Grillrestaurant",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Grill, Glut, Dry-Aged, Schnitte und Ausrüstung. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-asador-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-brasas.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-dryaged.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-chuleton.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-despiece.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-team.jpg"
    ]
  },
  "coffee-shop-specialty": {
    "h1": "KI für Coffee Shop und Specialty Coffee",
    "heroSubtitle": "Entwerfen Sie eine Spezialitätenkaffee-Karte mit Third-Wave-Anspruch, kalkulieren Sie jedes Getränk mit echten Kosten, planen Sie die Produktion eigener Konditoreiwaren und gestalten Sie minimalistisches Branding mit einer Suite gastronomischer KI-Agenten, die auf professionellen Specialty Coffee spezialisiert sind.",
    "heroTagline": "Spezialitätenkaffee mit echter Marge und Third-Wave-Technik",
    "badge": "Für Coffee Shops, Specialty Cafés und Third-Wave-Coffee",
    "painsTitle": "Was ein Coffee Shop unbedingt lösen muss",
    "pains": [
      "Eine Spezialitätenkaffee-Karte mit Fachkenntnis kuratieren: Single Origins, Blends, Zubereitungsmethoden (Espresso, V60, Aeropress, Chemex)",
      "Jedes Getränk mit echten Kosten kalkulieren (Grammatur, Premium-Milch, pflanzliche Alternativen) und stimmiger Food-Cost",
      "Verluste bei gemahlenem Kaffee (schneller Qualitätsverlust), Milch und frischen Konditoreiprodukten",
      "Barista-Technik Schicht für Schicht standardisieren: Extraktion, Latte Art, Dosierung, Kalibrierung",
      "Sich in einem umkämpften Gebiet mit rückverfolgbarem Herkunftskaffee, minimalistischem visuellem Branding und kontinuierlicher Schulung differenzieren",
      "Lokale Stammkunden gewinnen und Bohnen für zu Hause mit hoher Marge verkaufen"
    ],
    "featuresTitle": "Wie AI Chef Pro einem Coffee Shop hilft",
    "features": [
      {
        "icon": "Coffee",
        "title": "Kreativküche",
        "description": "Für die Entwicklung von Signature-Getränken: infundierte Cold Brews, Lattes mit hausgemachtem Sirup, saisonale Spezialitäten."
      },
      {
        "icon": "Cake",
        "title": "Kreative Patisserie",
        "description": "Für die eigene Konditorei, die den Coffee Shop differenziert: Croissants, Brownies, Cookies, Banana Bread, Kuchen des Tages."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Getränk",
        "description": "Kreativküche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet sie mit echten Kosten für Kaffee und Milch, validierter Food-Cost-Prozentsatz."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Cafetería / Brunch",
        "description": "Vorlagen: Bar-Vorbereitung, Espresso-Kalibrierung, Vorbereitung pflanzlicher Alternativen, Mise en Place Konditorei, Abschluss."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC für Coffee Shops",
        "description": "Rückverfolgbarkeit von gemahlenem Kaffee, Milch, pflanzlichen Alternativen und eigener Konditorei."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Saisonale Lancierungen: Pumpkin Spice Latte (Herbst), Cold Brew (Sommer), gewürzter Weihnachtskaffee."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Minimalistische KI-Referenzfotografie + Instagram: Specialty Coffee lebt von der visuellen Wirkung der Latte Art."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Lokale Kunden gewinnen, die bei Google und Maps nach „Specialty Coffee in der Nähe“ suchen."
      },
      {
        "icon": "BookOpen",
        "title": "BlogPost SEO Gen+",
        "description": "SEO-Artikel über Kaffeeherkunft, Filtermethoden und Pairing mit Konditorei, um organischen Traffic zu gewinnen."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem Coffee Shop mit AI Chef Pro",
    "workflow": [
      "07:00 · Eröffnung – Checkliste Kit de Tareas: Espresso-Kalibrierung, Vorbereitung von Milch und pflanzlichen Alternativen, Mise en Place für die Konditorei des Tages.",
      "08:00 · Morgenservice – morgendliche Spitzenzeit mit konstant hochwertigem Kaffee und professioneller Latte Art.",
      "11:00 · Kreativküche – Sie entwickeln ein neues Herbst-Signature-Getränk: Pumpkin Spice Latte mit hausgemachtem Sirup. Rezept + CSV-Kalkulation.",
      "12:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren tatsächlichen Preisen für Kaffee, Milch und Sirupe hoch und validieren Marge und Food-Cost-Prozentsatz.",
      "14:00 · Kreative Patisserie – Sie entwickeln ein neues veganes Banana Bread, um die Karte zu ergänzen.",
      "17:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren das Referenzbild für das neue Signature-Getränk und die minimalistischen Posts für Instagram.",
      "19:00 · Abschluss – gründliche Maschinenreinigung, Kalibrierung für morgen, Bestandskontrolle von Kaffee und Milch.",
      "20:00 · BlogPost SEO Gen+ – Sie planen einen Artikel über Filtermethoden, um organischen Traffic zu gewinnen."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Coffee Shops",
    "productIds": [
      "kit-tareas-cafeteria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Kreativküche + Kreative Patisserie haben unser Angebot verändert. Wir bringen saisonale Signature-Getränke mit professioneller Kalkulation auf den Markt, die eigene Konditorei hat den durchschnittlichen Warenkorb um 30 % gesteigert, und die Barista-Schulung ist jetzt konsistent. Die lokale Kundenakquise mit MenuDish + GastroIMG Gen+ hat sich in 4 Monaten verdoppelt.",
    "testimonialAuthor": "Marta Esteve",
    "testimonialRole": "Inhaberin, Specialty Coffee Third Wave",
    "faqTitle": "Häufig gestellte Fragen zu Coffee Shops",
    "faqs": [
      {
        "q": "Funktioniert es für Casual Coffee Shops, Specialty Coffee Third Wave oder Röstereien mit Laden?",
        "a": "Für alle drei. Kreativküche deckt alles ab, von einfachen Signature-Getränken bis zur Specialty-Karte mit fortgeschrittenen Filtermethoden."
      },
      {
        "q": "Wie kalkuliere ich Getränke mit Milch und pflanzlichen Alternativen?",
        "a": "Kreativküche denkt wie ein professioneller Barista: exakte Grammatur des Kaffees, Milchverhältnis, Kosten für Premium-Hafer vs. Soja. Kit de Escandallos Pro berechnet sofort neu."
      },
      {
        "q": "Deckt es auch eigene Konditorei zur Differenzierung ab?",
        "a": "Ja. Kreative Patisserie liefert Croissants, Brownies, Banana Bread, Cookies und saisonale Spezialitäten mit professioneller Kalkulation."
      },
      {
        "q": "Erzeugt es minimalistische visuelle Inhalte für Instagram?",
        "a": "Ja. GastroIMG Gen+ erzeugt Referenzbilder mit Cream- und Warm-Wood-Palette. Denken Sie daran: Das KI-Bild dient als visuelle Referenz – das endgültige Foto machen Sie mit Ihrem echten Latte."
      },
      {
        "q": "Wie hilft es mir bei saisonalen Lancierungen?",
        "a": "Gastro Calendar plant Pumpkin Spice Latte (Herbst), Cold Brew (Sommer), gewürzten Weihnachtskaffee und Signature-Getränke pro Saison."
      }
    ],
    "ctaTitle": "Ihr Coffee Shop mit echter Marge und Third-Wave-Technik.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "KI für Coffee Shop und Specialty Coffee: Karten, Kalkulationen und Branding | AI Chef Pro",
      "description": "KI-Suite für Coffee Shops: Kreativküche, eigene Konditorei, Getränkekalkulation, minimalistisches Branding und lokale Kundenakquise. Starten Sie noch heute.",
      "keywords": "KI Coffee Shop, Software Specialty Coffee, Kaffeekalkulation, Third-Wave-Coffee KI, Latte Art, Spezialitätenkaffee",
      "ogImage": "https://aichef.pro/og/use-cases/coffee-shop-specialty.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Coffee Shop zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding, bei dem Sie uns mitteilen, welche Art von Coffee Shop Sie betreiben (Specialty Third Wave, Casual Coffee Shop, Rösterei mit Laden, Café mit eigener Konditorei), Teamgröße, Stadt und Spezialgebiet.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Coffee Shop nutzen werden",
    "apps": [
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Entwicklung von Signature-Getränken: Cold Brews, gewürzte Lattes, saisonale Spezialitäten."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Eigene Konditorei: Croissants, Brownies, Banana Bread, Cookies."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Operative Beratung für Cafés und Brunches."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für Sirupe, Texturen und spezielle Anwendungen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Verluste bei gemahlenem Kaffee und Milch."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung für pflanzliche Alternativen und Konditorei."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Minimalistische KI-Referenzfotografie für Instagram, Web und Speisekarte."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit minimalistischem Redaktionskalender."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Lokale Kunden gewinnen, die nach „Specialty Coffee in der Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Saisonale Lancierungen und Signature-Getränke pro Saison."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und soziale Medien",
        "description": "SEO-Artikel über Kaffeeherkunft und Zubereitungsmethoden."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und soziale Medien",
        "description": "Pinterest gewinnt Traffic für Latte Art und eigene Konditorei."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach Getränkekalkulation"
      },
      {
        "value": "+30 %",
        "label": "durchschnittlicher Warenkorb mit eigener Konditorei"
      },
      {
        "value": "×2",
        "label": "lokale Kundenakquise mit MenuDish"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihren Coffee Shop"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierte saisonale Karten, Signature-Getränke ohne Kalkulation",
        "Externe Konditorei mit unsicherer Marge",
        "Unterschiedliche Kalibrierung zwischen Baristas",
        "Improvisiertes Instagram ohne minimalistische Palette",
        "Lokale Kundenakquise ohne Maps-SEO"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Saisonale Signature-Getränke mit professioneller Kalkulation",
        "Eigene Konditorei mit Kreative Patisserie und hoher Marge",
        "Konsistente Kalibrierung mit Vorlagen von Kit de Tareas",
        "Minimalistische GastroIMG Gen+ + InstaFlow",
        "MenuDish Local SEO gewinnt „Specialty Coffee in der Nähe“"
      ]
    },
    "galleryTitle": "So funktioniert ein Coffee Shop",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Latte Art, Herkunftskaffee, Konditorei, Bar und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-pour.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-beans.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-pastries.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-bar.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-team.jpg"
    ]
  },
  "sushi-bar": {
    "h1": "KI für Sushi-Bars",
    "heroSubtitle": "Meistern Sie Itamae-Technik mit rigoroser Kalkulation pro Nigiri, verwalten Sie täglich frischen Fisch, entwerfen Sie Signature-Omakase und setzen Sie minimalistisches Branding um – mit einer Suite gastronomischer KI-Agenten, die auf professionelle Sushi-Bars spezialisiert ist.",
    "heroTagline": "Sushi-Bar mit authentischer Technik und echter Marge",
    "badge": "Für Sushi-Bars, Omakase und Sushi-Shops",
    "painsTitle": "Was eine Sushi-Bar unbedingt lösen muss",
    "pains": [
      "Täglich frischer Fisch für Nigiri und Sashimi mit volatilen Kosten und strengem Abfall durch den Filetiervorgang",
      "Shari (Sushi-Reis) in jeder Schicht mit technischer Balance aus Essig, Zucker und Salz standardisieren",
      "Itamae-Technik konsistent koordinieren: Schnitt, Druck, Reistemperatur, Neta bei optimaler Temperatur",
      "Sich in einem umkämpften Gebiet mit Signature-Omakase, Fish of the Day und Lieferanten-Storytelling differenzieren",
      "Premium-Kunden mit einem Erlebnis direkt am Itamae an der Bar gewinnen (nicht am Tisch)",
      "Lieferbestellungen annehmen, ohne die Sushi-Qualität zu verlieren (optimales Zeitfenster 1–2 Stunden)"
    ],
    "featuresTitle": "Wie AI Chef Pro in einer Sushi-Bar hilft",
    "features": [
      {
        "icon": "Fish",
        "title": "Japanische Küche",
        "description": "Spezialisierter Agent für professionelles Sushi: Itamae-Technik, Shari-Balance, Filetieren, Neta bei optimaler Temperatur."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für Signature-Nigiri und zeitgenössisches Omakase mit authentischer Basis."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Für Fermentation und fortgeschrittene Techniken der japanischen Küche."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Nigiri und Omakase",
        "description": "Japanische Küche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet sie mit echten Kosten pro Stück und Omakase."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Vorlagen: Filetieren, Shari-Vorbereitung, Itamae-Mise, Abschluss."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Sushi",
        "description": "Fisch-Rückverfolgbarkeit für Sushi und kritische Temperaturen."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Für Sake, japanischen Whisky und professionelle Pairings."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Hanami, japanisches Neujahr, Tag des Sushi, Premium-Events."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Minimalistische KI-Referenzfotografie + Instagram für Premium-Sushi-Bars."
      }
    ],
    "workflowTitle": "Ein echter Tag in einer Sushi-Bar mit AI Chef Pro",
    "workflow": [
      "08:00 · Eröffnung – Checkliste Kit de Tareas: Annahme von täglich frischem Fisch, Filetieren der Blöcke, Shari-Vorbereitung (Essig + Zucker + Salz ausbalanciert).",
      "10:00 · Japanische Küche – Sie entwickeln ein neues Signature-Nigiri mit Hamachi, Yuzu Kosho und frischem Wasabi. Rezept + CSV-Kalkulation.",
      "11:00 · Kit de Escandallos Pro – Sie laden die CSV mit Ihren tatsächlichen Tagesfischpreisen hoch und validieren die Marge pro Nigiri und Omakase.",
      "13:00 · Mittagsservice – Sushi-Bar in vollem Betrieb, der Itamae arbeitet direkt vor dem Gast.",
      "17:00 · Team-Briefing – Erklärung des neuen Nigiri und Sake-Begleitungen.",
      "20:00 · Abendservice – Signature-Omakase, koordinierte Stoßzeiten.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro – Sie generieren ein minimalistisches Referenzbild des neuen Nigiri.",
      "23:00 · Abschluss – gründliche Reinigung, APPCC unterschrieben."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Sushi-Bars",
    "productIds": [
      "guia-restaurante-japones",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Japanische Küche hat unseren Betrieb verändert. Die Shari-Balance ist jetzt konsistent, das Omakase hat eine professionelle Kalkulation mit stückweise validierter Marge. Die Gewinnung von Premium-Kunden mit GastroIMG Gen+ ist in 6 Monaten um 40 % gestiegen.",
    "testimonialAuthor": "Akio Yamamoto",
    "testimonialRole": "Itamae und Inhaber, zeitgenössische Sushi-Bar",
    "faqTitle": "Häufig gestellte Fragen zu Sushi-Bars",
    "faqs": [
      {
        "q": "Eignet es sich für eine lockere Sushi-Bar oder Premium-Omakase?",
        "a": "Für beides. Japanische Küche deckt von traditionellem Sushi bis hin zu Omakase mit eigener Handschrift ab."
      },
      {
        "q": "Deckt es Itamae-Technik ab?",
        "a": "Ja. Japanische Küche denkt wie ein professioneller Itamae: Filetiertechnik, Shari-Balance, Neta und Kombinationen."
      },
      {
        "q": "Wie verwalte ich die Kosten für frischen Fisch?",
        "a": "Kit de Escandallos Pro berechnet die Marge sofort neu, sobald Sie die Tagespreise aktualisieren."
      },
      {
        "q": "Erzeugt es minimalistische visuelle Inhalte?",
        "a": "Ja. GastroIMG Gen+ erzeugt Referenzbilder. Denken Sie daran: Das KI-Bild dient als visuelle Referenz – das endgültige Foto machen Sie mit Ihrem echten Stück."
      },
      {
        "q": "Wie hilft es mir bei Omakase und Premium-Events?",
        "a": "Gastro Calendar plant saisonales Omakase, Hanami und japanisches Neujahr mit Premium-Degustationsmenüs."
      }
    ],
    "ctaTitle": "Ihre Sushi-Bar mit authentischer Technik und echter Marge.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "KI für Sushi-Bars: Itamae, Omakase und Kalkulation | AI Chef Pro",
      "description": "KI-Suite für Sushi-Bars: Japanische Küche, Fermentus, Kalkulation pro Nigiri, Omakase und minimalistisches Branding. Starten Sie noch heute.",
      "keywords": "KI Sushi-Bar, Sushi-Software, Sushi-Kalkulation, professioneller Itamae, Omakase KI, japanische Technik",
      "ogImage": "https://aichef.pro/og/use-cases/sushi-bar.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Sushi-Bar zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding, bei dem Sie angeben, welche Art von Sushi-Bar Sie betreiben (lockere Sushi-Bar, Premium-Omakase, Kaiten, Sushi-Bar mit warmer Küche), Teamgröße, Stadt und Spezialgebiet.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrer Sushi-Bar einsetzen werden",
    "apps": [
      {
        "name": "Japanische Küche",
        "category": "Asiatische Rezeptsammlungen",
        "description": "Professionelles Sushi: Itamae-Technik, Sashimi, Omakase."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Signature-Nigiri und Omakase mit Rezept + CSV-Kalkulation."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Fermentation für fortgeschrittene Techniken."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Pairings mit Sake, japanischem Whisky und Bier."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Sake- und japanische Whisky-Bar."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Abfälle beim Filetieren von Fisch."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Identifizierung von Fisch, Meeresfrüchten, Soja, Gluten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Minimalistische KI-Referenzfotografie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und Social Media",
        "description": "Minimalistisches Instagram für Premium-Sushi-Bars."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und Social Media",
        "description": "Kunden gewinnen, die nach „Sushi in der Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und Social Media",
        "description": "Hanami, japanisches Neujahr, saisonales Omakase."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für fortgeschrittene Texturen."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "Marge nach Kalkulation des Omakase"
      },
      {
        "value": "+40 %",
        "label": "Premium-Gewinnung in 6 Monaten"
      },
      {
        "value": "−20 %",
        "label": "Abfälle beim Filetieren"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Sushi-Bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierter Shari, inkonsistente Balance",
        "Kalkulation ohne Tagesfischpreis",
        "Improvisiertes Omakase ohne Kalkulation",
        "Instagram ohne minimalistische Palette",
        "Lokale Kundengewinnung ohne SEO"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Shari und Technik mit professionellem Anspruch",
        "Echtzeit-Kalkulation mit Tagespreis",
        "Omakase mit stückweise validierter Kalkulation",
        "Minimalistisches GastroIMG Gen+ + InstaFlow",
        "MenuDish Local SEO erfasst „Sushi in der Nähe“"
      ]
    },
    "galleryTitle": "So funktioniert eine Sushi-Bar",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Counter, Omakase, Fisch, Sake und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-counter.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-omakase.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-fish.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-sake.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-team.jpg"
    ]
  },
  "gastrobar-tapas": {
    "h1": "KI für Gastrobar und Tapas-Bar",
    "heroSubtitle": "Entwerfen Sie Tapas- und Pintxos-Karten mit professioneller Kalkulation, verwalten Sie Vermut und Weine pro Glas, planen Sie Events und erfassen Sie authentisches spanisches Branding mit einer Suite von gastronomischen KI-Agenten, die auf Gastrobar und spanische Küche spezialisiert sind.",
    "heroTagline": "Tapas mit authentischer Technik und echter Marge",
    "badge": "Für Gastrobars, Tapas-Bars, Pintxos und Weinbars",
    "painsTitle": "Was ein Gastrobar unbedingt lösen muss",
    "pains": [
      "Tapas-Karte mit vielen Varianten (kalt, warm, Pintxos, Raciones) bei konsistenten Lebensmittelkosten",
      "Verluste bei frischen Produkten (Anchovis, Schinken, Meeresfrüchte), Brot und Wurstwaren mit kurzer Haltbarkeit",
      "Signature-Tapas Schicht für Schicht mit Konsistenz und Servicetempo standardisieren",
      "Verwaltung von Vermut, Weinen pro Glas und Bieren mit hoher Marge und korrektem Umschlag",
      "Sich mit Qualitätsprodukten, authentischem spanischem Branding und Storytelling über handwerkliche Lieferanten differenzieren",
      "Private Events und Verkostungen mit professionellen Weinbegleitungen gewinnen"
    ],
    "featuresTitle": "Wie AI Chef Pro in einem Gastrobar hilft",
    "features": [
      {
        "icon": "Wine",
        "title": "Casual Restaurants AI+",
        "description": "Operative Beratung für Gastrobars und Tapas-Bars."
      },
      {
        "icon": "Sparkles",
        "title": "Spanische Küche + Kreativküche",
        "description": "Spezialisierte Rezeptsammlungen: traditionelle Tapas, baskische Pintxos, Marktportionen, Fusionen."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Tapa und Portion",
        "description": "Kreativküche liefert Rezept + Kalkulation als CSV; Kit de Escandallos Pro verwaltet es mit echten Kosten pro Tapa und Lebensmittelkosten %."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Vermuts, spanische Weine pro Glas, Craft-Biere und Weinbegleitungen zu Tapas."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Vorlagen: Tapas-Vorbereitung, Bar-Mise, Vermut, Schließung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC bar",
        "description": "Rückverfolgbarkeit von Schinken, Wurstwaren, Anchovis, frischen Meeresfrüchten."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Welt-Tapas-Tag, San Fermín, lokale Feste, private Events."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "KI-generierte spanische Handwerksfotografie + Instagram, um Einheimische und Touristen zu gewinnen."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Kunden gewinnen, die nach \"Tapas in der Nähe\" oder \"Gastrobar [Stadt]\" suchen."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem Gastrobar mit AI Chef Pro",
    "workflow": [
      "11:00 · Eröffnung — Checkliste Kit de Tareas: Vorbereitung kalter Tapas, Aufbau des Schinkenständers, Mise en Place der Bar, Kontrolle des Vermut-Hahns.",
      "12:30 · Spanische Küche + Kreativküche — Sie entwickeln eine neue Signature-Tapa mit hausgereiftem Anchovis, Piparra und Tomatenöl. Rezept + Kalkulation als CSV.",
      "13:30 · Kit de Escandallos Pro — Sie laden die CSV mit Ihren realen Preisen, validieren Marge pro Tapa und Lebensmittelkosten %.",
      "14:00 · Mittagsservice — starker Ansturm mit Vermut und Tapas, einwandfreie Mise en Place.",
      "17:00 · Pause — Bar & Lounge AI+ validiert Weinbegleitungen mit Albariño- und Verdejo-Weinen für neue Tapas.",
      "19:00 · Abendservice — Spitzenzeiten mit Craft-Bieren und Weinen pro Glas.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — Sie generieren Referenzbilder und Posts.",
      "00:00 · Schließung — Reinigung, APPCC unterschrieben, Bestandskontrolle."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Gastrobar",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Spanische Küche + Bar & Lounge AI+ haben unser Niveau angehoben. Die Signature-Tapas haben jetzt professionelle Kalkulation mit validierter Marge, die Weinbegleitungen pro Glas sind konsistent und wir haben den durchschnittlichen Bon in 4 Monaten um 15% gesteigert. Die lokale Kundenakquise mit MenuDish + GastroIMG ist x2.",
    "testimonialAuthor": "Iñaki Etxeberria",
    "testimonialRole": "Inhaber, zeitgenössischer Gastrobar in Donostia",
    "faqTitle": "Häufige Fragen für Gastrobars",
    "faqs": [
      {
        "q": "Funktioniert es für einen lockeren Gastrobar, eine traditionelle Tapas-Bar, baskische Pintxos oder eine Weinbar mit Tapas?",
        "a": "Für alle vier. Spanische Küche + Casual Restaurants AI+ decken von traditionellen Tapas bis zu zeitgenössischen Gastrobars ab."
      },
      {
        "q": "Deckt es Vermut, Weine und Biere mit Weinbegleitungen ab?",
        "a": "Ja. Bar & Lounge AI+ deckt Vermut, spanische Weine pro Glas, Craft-Biere und Weinbegleitungen zu Tapas ab."
      },
      {
        "q": "Wie verwaltet man Verluste bei Schinken und frischen Produkten?",
        "a": "Lebensmittelabfälle AI liefert Daten pro Prozess (Schneiden von Schinken, Anchovis, Meeresfrüchte). Sie werden in die Kalkulation integriert."
      },
      {
        "q": "Generiert es visuelle Inhalte für Instagram?",
        "a": "Ja. GastroIMG Gen+ generiert Referenzbilder. Denken Sie daran, dass das KI-Bild eine visuelle Referenz ist: Das endgültige Foto machen Sie mit Ihrer echten Tapa."
      },
      {
        "q": "Wie hilft es mir bei privaten Events und Verkostungen?",
        "a": "Gastro Calendar plant Verkostungen mit Weingütern, private Events, San Fermín und lokale Feste."
      }
    ],
    "ctaTitle": "Ihr Gastrobar mit echter Marge und authentischer Technik.",
    "ctaSubtitle": "Beginnen Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "KI für Gastrobar und Tapas-Bar: Tapas, Kalkulationen und Weinbegleitungen | AI Chef Pro",
      "description": "KI-Suite für Gastrobars: Spanische Küche, Bar & Lounge AI+, Kalkulation pro Tapa, Vermut und Weine pro Glas. Beginnen Sie heute.",
      "keywords": "KI Gastrobar, Software Tapas-Bar, Kalkulation Tapa, Pintxos KI, Vermut Tapas, zeitgenössischer Gastrobar",
      "ogImage": "https://aichef.pro/og/use-cases/gastrobar-tapas.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Gastrobar personalisiert",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding, in dem Sie erzählen, welche Art von Gastrobar Sie betreiben (zeitgenössischer Gastrobar, traditionelle Tapas-Bar, baskische Pintxos, Weinbar mit Tapas), Teamgröße, Stadt und Spezialität.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Gastrobar verwenden werden",
    "apps": [
      {
        "name": "Spanische Küche",
        "category": "Rezeptsammlungen aus Europa",
        "description": "Traditionelle Tapas, Pintxos, Marktportionen."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Zeitgenössische Signature-Tapas mit Rezept + Kalkulation als CSV."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Vermut, spanische Weine, Biere und Weinbegleitungen."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Operative Beratung für Gastrobars."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Weinbegleitungen mit Weinen und Bieren für Tapas."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für Texturen und fortgeschrittene Technik."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Verluste bei Schinken, Anchovis, Meeresfrüchten und Wurstwaren."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Identifikation pro Tapa: Gluten, Milchprodukte, Meeresfrüchte, Sulfite."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "KI-generierte spanische Handwerksfotografie als Referenz."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram, um Einheimische und Touristen zu gewinnen."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Kunden gewinnen, die nach \"Tapas in der Nähe\" suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Tapas-Tag, San Fermín, lokale Feste."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach Kalkulation der Tapas"
      },
      {
        "value": "+15 %",
        "label": "durchschnittlicher Bon in 4 Monaten"
      },
      {
        "value": "×2",
        "label": "lokale Kundenakquise mit MenuDish"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihren Gastrobar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierte Signature-Tapas ohne Kalkulation",
        "Weinbegleitungen ohne wissenschaftliche Basis",
        "Verluste bei Schinken und frischen Produkten ohne Rückverfolgbarkeit",
        "Improvisiertes Instagram",
        "Lokale Kundenakquise ohne SEO"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Signature-Tapas mit professioneller Kalkulation",
        "Weinbegleitungen mit Bar & Lounge AI+ und Food Pairing AI",
        "Kontrollierte Verluste mit Lebensmittelabfälle AI",
        "GastroIMG Gen+ + InstaFlow handwerklich",
        "MenuDish Local SEO erfasst \"Tapas in der Nähe\""
      ]
    },
    "galleryTitle": "Wie ein Gastrobar funktioniert",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Tapas, Vermut, Schinken, Weine und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-gastrobar-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-tapas.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-vermut.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-jamon.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-vinos.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-team.jpg"
    ]
  },
  "food-truck": {
    "h1": "KI für Foodtrucks",
    "heroSubtitle": "Entwerfen Sie eine kompakte Karte mit präziser Kalkulation, verwalten Sie die Vorbereitung angepasst an den begrenzten Platz, planen Sie Events und Routen und erzielen Sie virales Branding mit einer Suite von gastronomischen KI-Agenten, die auf professionelle Foodtrucks spezialisiert sind.",
    "heroTagline": "Foodtruck mit echter Marge und angepasstem Betrieb",
    "badge": "Für Foodtrucks, mobile Küchen und Street Food",
    "painsTitle": "Was ein Foodtruck unbedingt lösen muss",
    "pains": [
      "Kompakte und kuratierte Karte (max. 5-10 Gerichte) mit optimierten Kosten durch effiziente Prozesse",
      "Begrenzter Platz: angepasste Vorbereitung, kompakte Mise en Place, gemeinsame Geräte, minimale Lagerung",
      "Kontrollierte Lebensmittelabfälle bei frischen Produkten mit Einkauf angepasst an das Veranstaltungsvolumen",
      "Technik Schicht für Schicht standardisieren mit wechselndem Personal und wechselnden Teams",
      "Sich durch ikonisches visuelles Branding, aktive soziale Medien und Hand-Painted-Storytelling differenzieren",
      "Eventrouten planen (Festivals, Messen, Märkte, private Events) mit hoher Marge"
    ],
    "featuresTitle": "Wie AI Chef Pro bei einem Foodtruck hilft",
    "features": [
      {
        "icon": "Truck",
        "title": "Food Truck AI+",
        "description": "Spezialisierter Agent für Foodtrucks und mobile Küchen: Betrieb, Vorbereitung, Events, Branding und Routen."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für Foodtruck-Signatures: Smash-Burger, Baos, Tacos, knusprige Hähnchen mit professioneller Kalkulation."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulationen pro Gericht",
        "description": "Kreativküche liefert Rezept + Kalkulation als CSV; Kit de Escandallos Pro verwaltet es mit echten Kosten, angepasst an den mobilen Betrieb."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Vorlagen: Pre-Event, angepasste Vorbereitung, Aufbau, schneller Service, Abschluss, Auffüllen."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Foodtruck",
        "description": "Rückverfolgbarkeit angepasst an den mobilen Betrieb: Temperaturen, Wasser, Abfälle."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Festivals, Messen, Märkte, private Firmenevents."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Virale KI-Street-Food-Fotografie + Instagram mit aktivem Redaktionskalender."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Kunden gewinnen, die nach \"Foodtruck in der Nähe\" oder \"Street Food in [Stadt]\" suchen."
      },
      {
        "icon": "Sparkles",
        "title": "Lebensmittelabfälle AI",
        "description": "Lebensmittelabfälle bei frischen Produkten mit Einkauf angepasst an das Veranstaltungsvolumen."
      }
    ],
    "workflowTitle": "Ein echter Tag eines Foodtrucks mit AI Chef Pro",
    "workflow": [
      "08:00 · Eröffnung – Checkliste Kit de Tareas: Geräteprüfung, Aufbau der kompakten Mise en Place, Vorbereitung angepasst an das Veranstaltungsvolumen.",
      "10:00 · Food Truck AI+ – Sie entwickeln einen neuen Signature-Smash-Burger mit amerikanischem Käse und geräuchertem Bacon. Rezept + Kalkulation als CSV.",
      "11:00 · Kit de Escandallos Pro – Sie laden CSV mit echten Preisen und geschätztem Veranstaltungsvolumen hoch und validieren die Marge.",
      "12:00 · Ankunft am Event (Musikfestival) – Aufbau, Stromanschluss, APPCC-Kontrolle.",
      "13:00 · Mittagsservice – starker Andrang mit kontrollierten Warteschlangen, effiziente Vorbereitung.",
      "17:00 · Pause – Auffüllen des Lagers, Kontrolle der Lebensmittelabfälle und Kasse des ersten Services.",
      "20:00 · Abendservice – größerer Andrang, GastroIMG Gen+ hat bereits das Foto des Tages für Instagram geplant.",
      "00:00 · Abschluss – Reinigung, APPCC unterschrieben, Planung des nächsten Events mit Gastro Calendar."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Foodtrucks",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Food Truck AI+ + Kreativküche haben unseren Betrieb verändert. Die Karte ist kompakter, die Kalkulationen pro Gericht spiegeln die echte Marge wider, mit Einkauf angepasst an das Veranstaltungsvolumen, und die Akquise mit InstaFlow + GastroIMG hat unsere Reservierungen für private Events in 6 Monaten verdreifacht.",
    "testimonialAuthor": "Marcos Bermúdez",
    "testimonialRole": "Inhaber, handwerklicher Foodtruck",
    "faqTitle": "Häufig gestellte Fragen zu Foodtrucks",
    "faqs": [
      {
        "q": "Funktioniert es für Casual-Foodtrucks, Gourmet-Foodtrucks oder mobile Küchen für private Events?",
        "a": "Für alle drei. Food Truck AI+ deckt von Casual bis Gourmet ab, einschließlich mobiler Küchen für Hochzeiten und Firmenevents."
      },
      {
        "q": "Wie kalkuliere ich mit Einkauf angepasst an das Event?",
        "a": "Kit de Escandallos Pro berechnet die Marge sofort neu basierend auf dem geschätzten Veranstaltungsvolumen."
      },
      {
        "q": "Deckt es den mobilen Betrieb mit begrenztem Platz ab?",
        "a": "Ja. Food Truck AI+ denkt wie ein professioneller Betreiber: kompakte Vorbereitung, effiziente Mise en Place, gemeinsame Geräte."
      },
      {
        "q": "Erzeugt es virale Inhalte für Instagram und TikTok?",
        "a": "Ja. GastroIMG Gen+ + InstaFlow AI Pro erzeugen virale Inhalte mit aktivem Redaktionskalender. Denken Sie daran, dass das KI-Bild als visuelle Referenz dient: Das endgültige Foto machen Sie mit Ihrem echten Gericht."
      },
      {
        "q": "Wie hilft es mir bei Events und Routen?",
        "a": "Gastro Calendar plant Festivals, Messen, Märkte und private Events mit Routenplanung."
      }
    ],
    "ctaTitle": "Ihr Foodtruck mit echter Marge und angepasstem Betrieb.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "KI für Foodtrucks: Karte, Kalkulationen und Events | AI Chef Pro",
      "description": "KI-Suite für Foodtrucks: Food Truck AI+, Kalkulationen pro Gericht, Eventplanung, virales Branding und APPCC. Starten Sie noch heute.",
      "keywords": "KI Foodtruck, Software Foodtruck, Kalkulationen Foodtruck, Street Food KI, mobile Küche, Events Foodtruck",
      "ogImage": "https://aichef.pro/og/use-cases/food-truck.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Foodtruck zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding, in dem Sie uns mitteilen, welche Art von Foodtruck Sie betreiben (Casual, Gourmet, private Events, Markt, Festivals), Teamgröße, Spezialität und Einsatzgebiete.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem Foodtruck verwenden werden",
    "apps": [
      {
        "name": "Food Truck AI+",
        "category": "Geschäftskonzepte",
        "description": "Spezialisierter Agent für Foodtrucks und mobile Küchen."
      },
      {
        "name": "Burger Pro AI+",
        "category": "Geschäftskonzepte",
        "description": "Für Foodtrucks mit Smash-Burgern und Gourmet-Burgerläden."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Signatures mit Rezept + Kalkulation als CSV."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Geschäftskonzepte",
        "description": "Operative Beratung für Casual Dining."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Lebensmittelabfälle mit Einkauf angepasst an das Event."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung pro Gericht."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Virale KI-Street-Food-Fotografie als Referenz."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit aktivem Redaktionskalender."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Kunden gewinnen, die nach \"Foodtruck in der Nähe\" suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Festivals, Messen, Märkte, private Events."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte und soziale Medien",
        "description": "Pinterest generiert Traffic für Street Food."
      },
      {
        "name": "Mental Coach",
        "category": "Tools und Utilities",
        "description": "Coaching für Stressmanagement bei Großveranstaltungen."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach Kalkulation der Karte"
      },
      {
        "value": "×3",
        "label": "Reservierungen für private Events in 6 Monaten"
      },
      {
        "value": "−20 %",
        "label": "Lebensmittelabfälle mit angepasstem Einkauf"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihren Foodtruck"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Umfangreiche Karte mit unsicheren Lebensmittelkosten",
        "Produkteinkauf ohne Anpassung an das Veranstaltungsvolumen",
        "Hohe Lebensmittelabfälle bei frischen Produkten",
        "Improvisiertes Instagram, ohne virale Inhalte",
        "Private Events manuell organisiert"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Kompakte Karte mit professioneller Kalkulation",
        "Einkauf angepasst an das geschätzte Veranstaltungsvolumen",
        "Kontrollierte Lebensmittelabfälle mit Lebensmittelabfälle AI",
        "GastroIMG Gen+ + InstaFlow virale Inhalte",
        "Private Events mit professionellem Angebot abgeschlossen"
      ]
    },
    "galleryTitle": "So funktioniert ein Foodtruck",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Truck, Vorbereitung, Plancha, Service und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-food-truck-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-counter.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-grill.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-line.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-team.jpg"
    ]
  },
  "restaurante-italiano": {
    "h1": "KI für italienische Restaurants",
    "heroSubtitle": "Meistern Sie authentische italienische Technik mit strenger Kalkulation pro Gericht, verwalten Sie frische Pasta und traditionelle Saucen, entwerfen Sie saisonale Karten und erfassen Sie Trattoria-Branding mit einer Suite gastronomischer KI-Agenten, die auf professionelle italienische Küche spezialisiert sind.",
    "heroTagline": "Italienische Küche mit authentischer Technik und echter Marge",
    "badge": "Für Trattorien, Ristoranti und italienische Restaurants",
    "painsTitle": "Was ein italienisches Restaurant unbedingt lösen muss",
    "pains": [
      "Tägliche frische Pasta mit präziser Balance aus Grieß, Ei und Wasser, Extrusionstechnik und regionalen Formen",
      "Traditionelle Saucen (Ragù, Carbonara, Cacio e Pepe, Pesto), die Schicht für Schicht technische Konsistenz erfordern",
      "Lebensmittelabfälle bei frischer Pasta, Käse, italienischen Wurstwaren (Mortadella, Prosciutto), San-Marzano-Tomaten",
      "Standardisierung regionaler Signature-Gerichte (Rom, Toskana, Emilia, Sizilien) mit authentischer Technik",
      "Differenzierung in umkämpften Gebieten mit importierten italienischen Produkten, Trattoria-Branding und regionalem Storytelling",
      "Aufträge für private Events, Firmenessen und italienische Hochzeiten mit hoher Marge gewinnen"
    ],
    "featuresTitle": "Wie AI Chef Pro einem italienischen Restaurant hilft",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Italienische Küche",
        "description": "Spezialisierter Agent für authentische italienische Küche: Pasta, Saucen, Risotto, Ossobuco, regionale Technik."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Für italienische Sauerteige (Focaccia, Pane Casareccio, Pizza alla Pala) und Fermentationstechnik."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Für zeitgenössische Signature-Gerichte und Degustationsmenüs mit authentischer italienischer Basis."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Italienische Weine im Glas und Weinbegleitungen zur regionalen Küche (Chianti, Barolo, Amarone, Prosecco)."
      },
      {
        "icon": "Calculator",
        "title": "Kalkulation pro Gericht",
        "description": "Italienische Küche liefert Rezept + CSV-Kalkulation; Kit de Escandallos Pro verwaltet sie mit echten Kosten pro Gericht und Food-Cost-Prozentsatz."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Vorlagen: Vorbereitung frischer Pasta, traditionelle Saucen, Mise en Place Pizza, Service, Abschluss."
      },
      {
        "icon": "ShieldCheck",
        "title": "Italienisches Pack APPCC",
        "description": "Rückverfolgbarkeit von frischer Pasta, italienischem Käse, Wurstwaren und Saucen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Italienische Feiertage (Ferragosto, Carnevale, Pasqua, Natale), private Events und italienische Hochzeiten."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Redaktionelle Trattoria-Fotografie KI + Instagram mit regionalem Storytelling."
      }
    ],
    "workflowTitle": "Ein echter Tag in einem italienischen Restaurant mit AI Chef Pro",
    "workflow": [
      "08:00 · Öffnung — Checkliste Kit de Tareas: Vorbereitung der täglichen frischen Pasta (Tagliatelle, Ravioli, Pappardelle), Vorbereitung traditioneller Saucen.",
      "10:00 · Italienische Küche — Sie entwickeln ein neues Signature-Gericht: Tagliolini al limone mit Scampi vom Tagesfang. Rezept + CSV-Kalkulation.",
      "11:00 · Kit de Escandallos Pro — Sie laden CSV mit echten Preisen für Scampi und italienische Produkte hoch, validieren Marge und Food-Cost-Prozentsatz.",
      "12:00 · Bar & Lounge AI+ — Sie validieren die Weinbegleitung mit einem Vermentino di Sardegna.",
      "13:00 · Mittagsservice — Spitzenzeiten mit frischer Pasta, traditionellen Saucen und italienischen Weinen im Glas.",
      "17:00 · Briefing an das Team — Erklärung des neuen Gerichts und der Weinbegleitungen.",
      "19:00 · Abendservice — koordinierte Spitzenzeiten mit der Hauptküche.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — Sie generieren redaktionelle Trattoria-Bilder und Posts."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für italienische Restaurants",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Italienische Küche + Bar & Lounge AI+ haben unser Restaurant verändert. Konsistente frische Pasta, traditionelle Saucen mit technischer Balance, dokumentierte Weinbegleitungen zu italienischen Weinen im Glas. Wir haben die Marge um 5 Punkte gesteigert und die Stammgäste sind in 6 Monaten um 30 % gewachsen.",
    "testimonialAuthor": "Lorenzo Bianchi",
    "testimonialRole": "Koch und Inhaber, zeitgenössische Trattoria",
    "faqTitle": "Häufige Fragen italienischer Restaurants",
    "faqs": [
      {
        "q": "Funktioniert es für eine lockere Trattoria, ein zeitgenössisches Ristorante oder regionale italienische Küche?",
        "a": "Für alle drei. Italienische Küche deckt von der traditionellen Trattoria bis zur gehobenen italienischen Autorenküche mit authentischer regionaler Technik ab."
      },
      {
        "q": "Deckt es frische Pasta und traditionelle Saucen ab?",
        "a": "Ja. Italienische Küche denkt wie ein professioneller italienischer Koch: Teigbalance, regionale Formen, Technik traditioneller Saucen."
      },
      {
        "q": "Deckt es italienische Weine und Weinbegleitungen ab?",
        "a": "Ja. Bar & Lounge AI+ deckt Chianti, Barolo, Amarone, Prosecco und Weinbegleitungen zur regionalen Küche ab."
      },
      {
        "q": "Generiert es visuelle Inhalte für Instagram?",
        "a": "Ja. GastroIMG Gen+ generiert redaktionelle Trattoria-Bilder. Denken Sie daran: Das KI-Bild dient als visuelle Referenz – das endgültige Foto machen Sie mit Ihrem echten Gericht."
      },
      {
        "q": "Wie hilft es mir bei Events und italienischen Feiertagen?",
        "a": "Gastro Calendar plant Ferragosto, Carnevale, Pasqua, Natale und private Events mit italienischen Menüs."
      }
    ],
    "ctaTitle": "Ihr italienisches Restaurant mit authentischer Technik und echter Marge.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "KI für italienische Restaurants: Pasta, Kalkulation und Weine | AI Chef Pro",
      "description": "KI-Suite für italienische Restaurants: Italienische Küche, Kalkulationen, frische Pasta, italienische Weine und Trattoria-Branding. Starten Sie noch heute.",
      "keywords": "KI italienisches Restaurant, Trattoria-Software, Pasta-Kalkulation, italienische Küche KI, italienische Weine, zeitgenössisches Ristorante",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-italiano.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr italienisches Restaurant zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding, bei dem Sie erzählen, welche Art von italienischem Restaurant Sie betreiben (Trattoria, zeitgenössisches Ristorante, regionale Küche, italienische Autorenküche), Teamgröße, Stadt und regionale Spezialität.",
    "appsTitle": "Die KI-Agenten, die Sie in Ihrem italienischen Restaurant nutzen werden",
    "apps": [
      {
        "name": "Italienische Küche",
        "category": "Europäische Rezeptsammlungen",
        "description": "Pasta, Saucen, Risotto, Ossobuco mit authentischer regionaler Technik."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Zeitgenössische italienische Signature-Gerichte."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Italienische Sauerteige (Focaccia, Pane Casareccio)."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Italienische Weine und regionale Weinbegleitungen."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Weinbegleitungen mit authentischer italienischer Technik."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für Texturen und fortgeschrittene Technik."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Lebensmittelabfälle bei frischer Pasta, Käse, Wurstwaren."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Identifikation pro Gericht."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Redaktionelle Trattoria-Fotografie KI als Referenz."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und soziale Medien",
        "description": "Instagram mit italienischem Redaktionskalender."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Inhalte und soziale Medien",
        "description": "Kunden gewinnen, die nach „italienisch in der Nähe“ suchen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und soziale Medien",
        "description": "Italienische Feiertage und private Events."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "Marge nach Kalkulation der Gerichte"
      },
      {
        "value": "+30 %",
        "label": "Stammgäste in 6 Monaten"
      },
      {
        "value": "−20 %",
        "label": "Lebensmittelabfälle bei Pasta und Wurstwaren"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Trattoria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Improvisierte frische Pasta, variable Balance",
        "Traditionelle Saucen ohne technische Konsistenz",
        "Weinbegleitungen zu italienischen Weinen ohne professionelle Basis",
        "Lebensmittelabfälle bei importierten italienischen Produkten ohne Rückverfolgbarkeit",
        "Instagram ohne regionales Storytelling"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Frische Pasta mit dokumentierter technischer Balance",
        "Traditionelle Saucen konsistent mit professionellem Anspruch",
        "Dokumentierte Weinbegleitungen mit Bar & Lounge AI+",
        "Kontrollierte Lebensmittelabfälle mit Lebensmittelabfälle AI",
        "GastroIMG Gen+ + InstaFlow redaktionelle Trattoria"
      ]
    },
    "galleryTitle": "So funktioniert ein italienisches Restaurant",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: frische Pasta, Gerichte, Küche, Weine und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-italiano-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-pasta.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-platos.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-cocina.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-vinos.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-team.jpg"
    ]
  },
  "task-escandallos-con-ia": {
    "h1": "So erstellen Sie Kalkulationen mit KI",
    "heroSubtitle": "Berechnen Sie echte Kosten pro Gericht, Food-Cost-Prozentsatz und empfohlenen Preis in Minuten statt Tagen: Rezept + automatische Kalkulations-CSV mit Backstuben-Stundensatz, integrierten Lebensmittelabfällen und validierter Marge in Echtzeit mit einer Suite gastronomischer KI-Agenten.",
    "heroTagline": "Professionelle Kalkulationen in Minuten statt Stunden",
    "badge": "Aufgabe: Kalkulation und Costing",
    "painsTitle": "Was die manuelle Kalkulation kostet",
    "pains": [
      "Eine Woche Taschenrechner und Servietten, um eine neue Karte mit 30 Gerichten zu kalkulieren",
      "Ohne integrierten Backstuben-Stundensatz verlieren komplexe Gerichte Geld, ohne dass Sie es wissen",
      "Lebensmittelabfälle grob geschätzt (30 % bei manchen Schnitten), keine echten Daten pro Prozess",
      "Wenn sich der Lieferantenpreis ändert, gerät alles aus dem Gleichgewicht und wird nicht aktualisiert",
      "Fehlendes Kriterium für die Festlegung des Ziel-Food-Costs je nach Gerichtstyp (Signature, Vorspeise, Dessert)",
      "Keine Nachvollziehbarkeit der Berechnung: Wenn Sie geprüft werden, wissen Sie nicht, woher jede Zahl stammt"
    ],
    "featuresTitle": "So löst AI Chef Pro die Kalkulation",
    "features": [
      {
        "icon": "Calculator",
        "title": "Kreativküche + Kalkulations-CSV",
        "description": "Jeder kreative Agent (Küche, Patisserie, Gelateria, Schokolade) liefert Rezept + Kalkulations-CSV mit technischer Balance und integriertem Backstuben-Stundensatz."
      },
      {
        "icon": "BarChart3",
        "title": "Lebensmittelabfälle AI",
        "description": "Präzise Daten zu Lebensmittelabfällen pro Prozess (Zerlegung, Rösten, Abschrecken, Vitrine, Formen) automatisch in die CSV integriert."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients AI",
        "description": "Sosa-Katalog mit Referenzpreisen für professionelle technische Zutaten."
      },
      {
        "icon": "Sparkles",
        "title": "Calcula Pax + Conversor Ing",
        "description": "Skaliert Rezepte auf 2, 6, 12, 100 Personen ohne Präzisionsverlust; automatischer Umrechner für Gewichte und Maße."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Escandallos Pro",
        "description": "Herunterladbare Excel-Vorlagen, die die CSV empfangen und sofort echte Marge, Food-Cost-Prozentsatz und empfohlenen Preis berechnen."
      },
      {
        "icon": "BookOpen",
        "title": "Technische Blätter mit Kosten",
        "description": "Jedes Rezept liefert ein vollständiges technisches Blatt mit Kosten, Allergenen, Technik und Storytelling für den Service."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "KI-generiertes Referenzbild des kalkulierten Gerichts zur Visualisierung vor dem Kochen (nicht das endgültige Foto)."
      },
      {
        "icon": "BookOpen",
        "title": "Pro Prompts eBook",
        "description": "eBook mit über 300 professionellen Prompts zum Kalkulieren, Validieren und Optimieren von Kosten mit gastronomischer KI."
      },
      {
        "icon": "Wine",
        "title": "Auf jedes Konzept anwendbar",
        "description": "Restaurant, Café, Patisserie, Eisdiele, Schokoladenmanufaktur, Pizzeria, Bar, Catering, Hotel: Der Ablauf ist derselbe."
      }
    ],
    "workflowTitle": "So kalkulieren Sie mit KI in 4 Schritten",
    "workflow": [
      "1. Kreativküche (oder der kreative Agent Ihres Konzepts: Patisserie, Gelateria, Schokolade, Italienische Küche, Mexikanische Küche, Peruanische Küche, Japanische Küche) – Sie entwickeln oder laden das Rezept. Der KI-Agent liefert Rezept + Kalkulations-CSV mit technischer Balance, geschätzten Lebensmittelabfällen und Storytelling.",
      "2. Sosa Ingredients AI + Lebensmittelabfälle AI – die KI reichert die CSV mit Referenzpreisen und echten Lebensmittelabfällen pro Prozess Ihrer Küchenart an.",
      "3. Kit de Escandallos Pro (herunterladbare Excel-Vorlage, 12 €) – Sie laden die CSV mit Ihren echten Lieferantenpreisen. Die Excel berechnet echte Marge, Food-Cost-Prozentsatz, empfohlenen Preis pro Kanal (Saal, Lieferung, Events) und wirtschaftlichen Vorschlag.",
      "4. Calcula Pax + Conversor Ing – wenn Sie das Rezept für Bankette (50, 100, 300 Personen) skalieren oder Einheiten umrechnen müssen, erledigen die KI-Agenten das sofort, während die Kalkulation erhalten bleibt."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für Kalkulationen",
    "productIds": [
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-inventario",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Was früher eine Woche Taschenrechner war, sind jetzt 30 Minuten. Kreativküche liefert die Kalkulations-CSV, Lebensmittelabfälle AI reichert sie mit echten Daten an, und das Kit de Escandallos Pro gibt mir eine validierte Marge. Wir haben die Karte mit 28 Gerichten an einem Tag erneuert und die Marge um 6 Punkte gesteigert, indem wir Gerichte mit Verlust entdeckt haben, von denen wir nichts wussten.",
    "testimonialAuthor": "Pablo Ruiz",
    "testimonialRole": "Koch und Inhaber, Casual-Restaurant mit 4 Punkten",
    "faqTitle": "Häufige Fragen zur Kalkulation mit KI",
    "faqs": [
      {
        "q": "Funktioniert das für jede Küchenart?",
        "a": "Ja. Der Ablauf ist derselbe für Kreativküche, Patisserie, Gelateria, Schokolade, Pizzeria, mexikanische, peruanische, japanische, italienische Küche, pflanzenbasiert oder jedes andere Konzept. Nur der Ausgangs-Kreativagent ändert sich."
      },
      {
        "q": "Wie wird der Backstuben-Stundensatz verwaltet?",
        "a": "Die CSV enthält ein Feld für die Bearbeitungszeit pro Prozess (Mischen, Formen, Backen, Dekorieren). Das Kit de Escandallos Pro multipliziert mit Ihrem echten Stundensatz (Gehalt + Nebenkosten) und integriert ihn in die echte Marge."
      },
      {
        "q": "Wie bilde ich variable Lieferantenpreise ab (Kakao, Fisch, Fleisch)?",
        "a": "Das Kit de Escandallos Pro berechnet die Marge sofort neu, wenn Sie Preise aktualisieren. Lebensmittelabfälle AI fügt die Kosten der Lebensmittelabfälle pro Prozess hinzu. Das Gericht spiegelt immer die aktuellen Kosten wider, nicht die von vor drei Monaten."
      },
      {
        "q": "Deckt es die Skalierung für Bankette und Events ab?",
        "a": "Ja. Calcula Pax skaliert Rezepte auf jede Personenzahl ohne Präzisionsverlust; das Kit de Escandallos Pro berechnet Kosten pro Person und den wirtschaftlichen Vorschlag für den Firmenkunden neu."
      },
      {
        "q": "Erzeugt es ein Referenzbild des kalkulierten Gerichts?",
        "a": "Ja. GastroIMG Gen+ erzeugt ein visuelles Referenzbild des Gerichts. Denken Sie daran: Das KI-Bild ist eine Referenz; das endgültige Kalkulationsfoto machen Sie selbst mit Ihrem real angerichteten Gericht."
      }
    ],
    "ctaTitle": "Ihre Kalkulationen in Minuten mit validierter Marge.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "So erstellen Sie Kalkulationen mit KI: echte Kosten, Marge und Food Cost | AI Chef Pro",
      "description": "KI-Suite für professionelle Kalkulationen: Rezept + CSV mit Backstuben-Stundensatz, integrierten Lebensmittelabfällen, validierter Marge. Starten Sie noch heute.",
      "keywords": "Kalkulation mit KI, Food Cost berechnen, echte Gerichtskosten, Kalkulations-CSV, Kalkulations-Kit, Food Cost Restaurant",
      "ogImage": "https://aichef.pro/og/use-cases/task-escandallos-con-ia.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Küche zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit dem Agenten „Wer sind Sie?“, einem 2-minütigen Onboarding, bei dem Sie erzählen, welche Küche Sie betreiben, und der Kalkulationsablauf passt sich Ihrem Konzept an: Kreativküche für Restaurants, Kreative Patisserie für die Backstube, Kreative Gelateria für die Eisdiele usw.",
    "appsTitle": "Die KI-Agenten, die Sie zum Kalkulieren nutzen",
    "apps": [
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Rezepte + Kalkulations-CSV mit technischer Balance und geschätzten Lebensmittelabfällen."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Süße Rezepte mit integriertem Backstuben-Stundensatz."
      },
      {
        "name": "Kreative Gelateria",
        "category": "Kulinarische Kreativität",
        "description": "Rezepte mit technischer Balance von Zucker, Feststoffen und Fetten."
      },
      {
        "name": "Kreative Schokolade",
        "category": "Kulinarische Kreativität",
        "description": "Rezepte mit Couverturen, Ganachen und Temperiertechnik."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Präzise Daten zu Lebensmittelabfällen pro Prozess, in die Kalkulation integriert."
      },
      {
        "name": "Calcula Pax",
        "category": "Werkzeuge und Utilities",
        "description": "Skalierung von Rezepten für jede Personenzahl."
      },
      {
        "name": "Conversor Ing",
        "category": "Werkzeuge und Utilities",
        "description": "Automatischer Umrechner für Gewichte und Maße."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Zutat."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Referenzpreise und Technik mit Sosa-Katalog."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "Preise und Technik mit tSpoonLab-Katalog."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Referenzbild des kalkulierten Gerichts."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Tiefgehende Recherche zu Lieferanten und Marktpreisen."
      }
    ],
    "metrics": [
      {
        "value": "×30",
        "label": "schneller als mit dem Taschenrechner"
      },
      {
        "value": "+6 pp",
        "label": "Marge nach der Kartenerstellung"
      },
      {
        "value": "−25 %",
        "label": "Lebensmittelabfälle mit echten Daten"
      },
      {
        "value": "12+",
        "label": "Agenten zum Kalkulieren"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Eine Woche für eine neue Karte mit 30 Gerichten",
        "Ohne Backstuben-Stundensatz verlieren komplexe Gerichte Geld",
        "Lebensmittelabfälle grob geschätzt, keine echten Daten",
        "Geänderte Lieferantenpreise ohne Margenaktualisierung",
        "Keine Nachvollziehbarkeit der Berechnung"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Eine neue Karte mit 30 Gerichten an einem Tag kalkuliert",
        "Backstuben-Stundensatz automatisch integriert",
        "Echte Lebensmittelabfälle mit Lebensmittelabfälle AI und Vorlagen",
        "Aktualisierbare Preise: Marge wird sofort neu berechnet",
        "Nachvollziehbare CSV + technisches Blatt mit Kosten für die Prüfung"
      ]
    },
    "galleryTitle": "So funktioniert der Kalkulationsablauf mit KI",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Rezept, CSV, Lebensmittelabfälle, digitales Rezeptbuch und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-csv.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-recipe.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-merma.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-team.jpg"
    ]
  },
  "task-menu-degustacion-con-ia": {
    "h1": "So entwerfen Sie ein Degustationsmenü mit KI",
    "heroSubtitle": "Entwerfen Sie Degustationsmenüs mit kohärenter Sequenz, validierter Gesamtkalkulation, wissenschaftlich fundierten Pairings und Storytelling für den Service – mit einer Suite gastronomischer KI-Agenten, die auf Haute Cuisine spezialisiert sind.",
    "heroTagline": "Professionelles Degustationsmenü in Stunden, nicht in Wochen",
    "badge": "Aufgabe: Degustationsmenü",
    "painsTitle": "Was es kostet, ein Degustationsmenü von Hand zu entwerfen",
    "pains": [
      "Eine Woche Iterationen für eine kohärente 7–10-Gänge-Sequenz ohne Übersättigung",
      "Ohne validierte Gesamtkalkulation pro Menü und unsichere Preisgestaltung",
      "Vorgeschlagene Weinbegleitungen ohne fundierte wissenschaftliche Basis",
      "Improvisiertes Storytelling für jeden Gang, Serviceteam ohne kontinuierliche Schulung",
      "Änderungen an Gängen erfordern eine komplette manuelle Neukalkulation",
      "Fehlendes System, um Textur, Temperatur, Intensität und Technik zwischen den Gängen auszubalancieren"
    ],
    "featuresTitle": "Wie AI Chef Pro das Degustationsmenü meistert",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Kreativküche mit technischer Sequenz",
        "description": "Durchdenkt die gesamte Sequenz: leichter Auftakt, Gemüsegang, Fischgang, Fleischgang, Gaumenreiniger, Dessert. Gleichgewicht von Textur, Temperatur und Intensität."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Wissenschaftlich fundierte Weinbegleitungen für jeden Gang: Analyse von Säure, Tanninen, Struktur, Intensität und Harmonie mit der Küche."
      },
      {
        "icon": "Calculator",
        "title": "Integrierte Gesamtkalkulation",
        "description": "CSV mit Kalkulation jedes Gangs + Gesamtmenü; Kit de Escandallos Pro validiert Kosten pro Person und Preisvorschlag."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling für den Service",
        "description": "Beschreibung jedes Gangs mit Technik, Produkt, Lieferant und Geschichte; das Serviceteam trägt es professionell vor."
      },
      {
        "icon": "Sparkles",
        "title": "Bar & Lounge AI+",
        "description": "Auswahl von Weinen pro Glas für das Pairing des Degustationsmenüs mit professioneller Sommelier-Kompetenz."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Vorlagen für das Mise-en-Place jedes Gangs, Service-Sequenz und Koordination mit dem Service."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Referenzbild jedes Gangs, um die Sequenz vor dem Probieren zu visualisieren und die visuelle Kohärenz zu validieren."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Saisonale Degustationsmenüs und private Veranstaltungen mit professioneller Planung."
      },
      {
        "icon": "BarChart3",
        "title": "Calcula Pax",
        "description": "Skalierung von Rezepten für Bankette und private Veranstaltungen, ohne an Präzision zu verlieren."
      }
    ],
    "workflowTitle": "So entwerfen Sie ein Degustationsmenü in 5 Schritten",
    "workflow": [
      "1. Kreativküche – Sie definieren das Thema (Jahreszeit, lokales Produkt, Anlass) und der KI-Agent liefert eine 7–10-Gänge-Sequenz mit technischem Gleichgewicht (Textur, Intensität, Temperatur).",
      "2. Jeder Gang mit Rezept + individueller CSV-Kalkulation + Storytelling für den Service mit Technik, Produkt und Lieferant.",
      "3. Food Pairing AI – validiert für jeden Gang eine Wein- oder Sake-Begleitung auf wissenschaftlicher Basis. Bar & Lounge AI+ schlägt eine konkrete Auswahl aus dem Weinkeller vor.",
      "4. Kit de Escandallos Pro – Sie laden die einzelnen CSVs hoch, die Excel berechnet die Gesamtkosten pro Person, den Preisvorschlag und die validierte Marge.",
      "5. Calcula Pax – Wenn das Menü für eine private Veranstaltung oder ein Bankett gedacht ist (50, 100, 300 Pax), skaliert es die Rezepte und berechnet die Kosten für das Geschäftsangebot neu."
    ],
    "productsTitle": "Vorlagen und empfohlene Kits für das Degustationsmenü",
    "productIds": [
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "guia-restaurante-gastronomico",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Kreativküche + Food Pairing AI haben unsere Entwicklung von Degustationsmenüs revolutioniert. Die 9-Gänge-Sequenz kommt bereits mit dokumentiertem technischem Gleichgewicht, die Weinbegleitungen pro Glas sind konsistent und die Gesamtkalkulation mit Kit de Escandallos Pro liefert uns eine validierte Marge. Was früher eine Woche dauerte, ist jetzt ein Tag.",
    "testimonialAuthor": "Joan Mestre",
    "testimonialRole": "Executive Chef, Restaurant mit 1 Michelin-Stern",
    "faqTitle": "Häufige Fragen zum Degustationsmenü mit KI",
    "faqs": [
      {
        "q": "Funktioniert es für Michelin-Restaurants, Autorenküche oder Casual-Restaurants mit Degustationsmenü?",
        "a": "Für alle drei. Kreativküche denkt wie ein professioneller Chef: technisches Gleichgewicht, kohärente Sequenz, eine an das Niveau angepasste Menü-Erzählung."
      },
      {
        "q": "Wie hilft es mir bei der Kohärenz zwischen den Gängen?",
        "a": "Kreativküche durchdenkt die gesamte Sequenz mit Balance von Textur (knusprig, seidig, cremig), Temperatur (kalt, Zimmertemperatur, warm), Intensität (dezent bis kräftig) und Technik (Garen, Fermentation, Räuchern)."
      },
      {
        "q": "Umfasst es Weinbegleitungen pro Glas für das Menü?",
        "a": "Ja. Food Pairing AI validiert jede Begleitung auf wissenschaftlicher Basis; Bar & Lounge AI+ schlägt eine konkrete Auswahl aus dem Weinkeller und Storytelling für den Service vor."
      },
      {
        "q": "Erzeugt es ein Referenzbild für jeden Gang?",
        "a": "Ja. GastroIMG Gen+ erzeugt ein Referenzbild, um die visuelle Kohärenz des Menüs zu visualisieren. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto machen Sie selbst mit Ihrem real angerichteten Teller."
      },
      {
        "q": "Skalierbar für Bankette und private Veranstaltungen?",
        "a": "Ja. Calcula Pax skaliert das Menü auf jede beliebige Personenzahl; Kit de Escandallos Pro berechnet die Kosten pro Person und das Angebot für den Kunden neu."
      }
    ],
    "ctaTitle": "Ihr professionelles Degustationsmenü in Stunden, nicht in Wochen.",
    "ctaSubtitle": "Beginnen Sie mit dem 2-minütigen Onboarding. Mitgliedsplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "So entwerfen Sie ein Degustationsmenü mit KI: Sequenz, Kalkulation und Pairings | AI Chef Pro",
      "description": "KI-Suite für Degustationsmenüs: technische Sequenz, Gesamtkalkulation, wissenschaftlich fundierte Pairings und Storytelling. Starten Sie noch heute.",
      "keywords": "Degustationsmenü KI, Degustationsmenü entwerfen, Gangfolge, Menü-Pairing, Kalkulation Degustationsmenü, Haute Cuisine KI",
      "ogImage": "https://aichef.pro/og/use-cases/task-menu-degustacion-con-ia.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Restaurant zugeschnitten",
    "personalizationBody": "AI Chef Pro beginnt mit „Wer sind Sie?“: Sie beschreiben den Restauranttyp (Michelin-Restaurant, Fine Dining, Casual-Restaurant mit Degustationsmenü, Autorenküche), die bevorzugte Anzahl der Gänge, den Markt und den Kochstil. Jeder Agent antwortet passend zu Ihrem Niveau.",
    "appsTitle": "Die KI-Agenten, die Sie für das Degustationsmenü nutzen",
    "apps": [
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Denkt die technische Sequenz eines Degustationsmenüs mit Balance durch."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Wissenschaftlich fundierte Begleitungen für jeden Gang."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Auswahl von Weinen pro Glas mit Sommelier-Kompetenz."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Für Desserts und Gaumenreiniger des Menüs."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog für Texturen und fortgeschrittene Technik."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-Lieferanten",
        "description": "tSpoonLab-Katalog für fortgeschrittene Anwendungen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Dienstprogramme",
        "description": "Lebensmittelabfälle pro Gang, integriert in die Gesamtkalkulation."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools und Dienstprogramme",
        "description": "Skalierung für Bankette und private Veranstaltungen."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Dienstprogramme",
        "description": "Allergenidentifizierung pro Gang für den Service."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Referenzbild für jeden Gang des Menüs."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und Social Media",
        "description": "Saisonale Degustationsmenüs und private Veranstaltungen."
      },
      {
        "name": "Mental Coach",
        "category": "Tools und Dienstprogramme",
        "description": "Coaching für Führung und Management des Degustationsservices."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "Geschwindigkeit gegenüber manuellem Prozess"
      },
      {
        "value": "+8 pp",
        "label": "Marge nach der Menükalkulation"
      },
      {
        "value": "×3",
        "label": "Geschwindigkeit bei Pairings mit Sommelier"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihr Degustationsmenü"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Eine Woche Iterationen für jedes neue Menü",
        "Improvisierte Sequenz ohne technisches Gleichgewicht",
        "Pairings ohne wissenschaftliche Basis",
        "Gesamtkalkulation mit unsicherer Preisgestaltung",
        "Improvisiertes Storytelling, Serviceteam ohne Schulung"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Degustationsmenü in einem Tag abgeschlossen mit kohärenter Sequenz",
        "Dokumentiertes technisches Gleichgewicht zwischen den Gängen",
        "Wissenschaftlich fundierte Pairings mit Food Pairing AI",
        "Validierte Gesamtkalkulation und klares Angebot an den Kunden",
        "Professionelles Storytelling für das Service-Briefing"
      ]
    },
    "galleryTitle": "So funktioniert die Erstellung eines Degustationsmenüs mit KI",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Sequenz, Gänge, Pairings, Mise en Place und Team. Mit KI generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-pase.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-secuencia.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-pairing.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-team.jpg"
    ]
  },
  "task-fichas-tecnicas-con-ia": {
    "h1": "So erstellen Sie Rezeptblätter mit KI",
    "heroSubtitle": "Dokumentieren Sie jedes Gericht mit professionellem Rezeptblatt: Zutaten, Grammatur, Schritt-für-Schritt-Technik, Allergene, Food Cost, Plating-Foto und Storytelling für den Service. Die Suite gastronomischer KI-Agenten erstellt in Minuten ein vollständiges Rezeptblatt.",
    "heroTagline": "Professionelle Rezeptblätter in Minuten, nicht in Stunden",
    "badge": "Aufgabe: Rezeptblätter",
    "painsTitle": "Was es kostet, Rezeptblätter von Hand zu erstellen",
    "pains": [
      "Das Dokumentieren von 30 Gerichten mit professionellem Rezeptblatt kann 2 Wochen dauern",
      "Ohne Standardisierung kocht jeder Koch seine eigene Version nach, und die Konsistenz geht verloren",
      "Allergene werden pro Rezept von Hand berechnet – rechtliches und lebensmittelsicherheitsrelevantes Risiko",
      "Ohne Storytelling für den Service beschreibt das Team das Gericht improvisiert",
      "Wenn eine Zutat geändert wird, muss das Rezeptblatt aktualisiert und die Allergene neu berechnet werden",
      "Fehlende professionelle Vorlage mit allen kritischen Feldern (Technik, Grammatur, Abfall, Kosten)"
    ],
    "featuresTitle": "Wie AI Chef Pro Rezeptblätter erstellt",
    "features": [
      {
        "icon": "BookOpen",
        "title": "Kreativküche mit vollständigem Rezeptblatt",
        "description": "Jedes Rezept liefert ein professionelles Rezeptblatt: Zutaten, Grammatur, Technik, Allergene, Abfall, Kosten, Storytelling, Plating."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergen-ID",
        "description": "Automatische Identifizierung von Allergenen pro Rezept: Milchprodukte, Gluten, Nüsse, Soja, Meeresfrüchte, Sulfite usw."
      },
      {
        "icon": "Calculator",
        "title": "Integrierte Kosten",
        "description": "Das Rezeptblatt enthält Food-Cost-% und Kosten pro Portion, automatisch berechnet mit den Stundensätzen der Produktionsküche."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Referenzbild des angerichteten Gerichts, um es als visuelle Anleitung in das Rezeptblatt aufzunehmen."
      },
      {
        "icon": "Sparkles",
        "title": "Storytelling für den Service",
        "description": "Jedes Rezeptblatt enthält eine professionelle Beschreibung, damit das Serviceteam technisch korrekt präsentiert."
      },
      {
        "icon": "CheckSquare",
        "title": "Standardisierte Vorlage",
        "description": "Einheitliches Format für alle Rezeptblätter: Technik, Konservierung, Allergene, Präsentation, Kosten."
      },
      {
        "icon": "BarChart3",
        "title": "Conversor Ing + Calcula Pax",
        "description": "Umrechner für Gewichte und Maße; automatische Skalierung für Bankette und Veranstaltungen."
      },
      {
        "icon": "BookOpen",
        "title": "Pro Prompts eBook",
        "description": "eBook mit 300+ professionellen Prompts für Rezeptblätter, Allergene und Beschreibungen für den Service."
      },
      {
        "icon": "Wine",
        "title": "Weinbegleitung im Rezeptblatt",
        "description": "Food Pairing AI schlägt die empfohlene Weinbegleitung vor, um sie in das Rezeptblatt aufzunehmen."
      }
    ],
    "workflowTitle": "So erstellen Sie Rezeptblätter in 4 Schritten",
    "workflow": [
      "1. Kreativküche (oder Ihr kreativer Agent) – Sie entwickeln oder laden das Rezept hoch. Der KI-Agent liefert Rezept + vollständiges Rezeptblatt mit allen professionellen Feldern.",
      "2. Allergen-ID – identifiziert automatisch die Allergene pro Rezept und integriert sie in das Rezeptblatt; wenn Sie eine Zutat ändern, berechnet es sofort neu.",
      "3. GastroIMG Gen+ – generiert ein Referenzbild des angerichteten Gerichts, um es als visuelle Anleitung für den Koch in das Rezeptblatt aufzunehmen.",
      "4. Food Pairing AI + Storytelling für den Service – das Rezeptblatt enthält empfohlene Weinbegleitung und professionelle Beschreibung für das Team-Briefing."
    ],
    "productsTitle": "Vorlagen und empfohlene Kits für technische Rezeptblätter",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-tareas",
      "guia-restaurante-gastronomico"
    ],
    "testimonialQuote": "Das Dokumentieren von 28 Gerichten mit professionellem Rezeptblatt dauerte uns 2 Wochen. Kreativküche liefert jetzt jedes vollständige Rezeptblatt in Minuten: Zutaten, Technik, automatische Allergene, Kosten und Storytelling für den Service. Jetzt kann jeder Koch konsistent nachkochen, und bei Inspektionen ist alles nachvollziehbar.",
    "testimonialAuthor": "Carla Mendoza",
    "testimonialRole": "Küchenchefin, Casual-Restaurant mit 3 Standorten",
    "faqTitle": "Häufige Fragen zu Rezeptblättern mit KI",
    "faqs": [
      {
        "q": "Was enthält ein professionelles Rezeptblatt?",
        "a": "Zutaten mit exakter Grammatur, Schritt-für-Schritt-Technik, automatische Allergene, Food-Cost-%, Kosten pro Portion, Konservierung, Präsentation, empfohlene Weinbegleitung und Beschreibung für den Service."
      },
      {
        "q": "Wie verwaltet es Allergene automatisch?",
        "a": "Allergen-ID identifiziert die Allergene pro Zutat und integriert sie in das Rezeptblatt. Wenn Sie eine Zutat ändern, berechnet es sofort neu und aktualisiert die Informationen für den Service."
      },
      {
        "q": "Funktioniert es für jede Küchenart?",
        "a": "Ja. Der Ablauf ist derselbe für Kreativküche, Patisserie, Gelateria, Schokoladenwerkstatt, Pizzeria, jede Art nationaler Küche oder jedes Konzept."
      },
      {
        "q": "Erzeugt es ein Bild des Gerichts, um es in das Rezeptblatt aufzunehmen?",
        "a": "Ja. GastroIMG Gen+ erzeugt ein Referenzbild. Denken Sie daran: Das KI-Bild ist eine visuelle Referenz – das endgültige Foto im Rezeptblatt machen Sie mit Ihrem real angerichteten Gericht."
      },
      {
        "q": "Wie hilft es mir bei Audits und Zertifizierungen?",
        "a": "Jedes Rezeptblatt ist nachvollziehbar: Zutaten, Grammatur, Allergene, Kosten und Technik. Bereit für Audits, ISO 22000, BRC und Lebensmittelsicherheits-Zertifizierungen."
      }
    ],
    "ctaTitle": "Ihre professionellen Rezeptblätter in Minuten.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "So erstellen Sie Rezeptblätter mit KI: Allergene, Kosten und Storytelling | AI Chef Pro",
      "description": "KI-Suite für Rezeptblätter: automatische Allergene, integrierte Kosten, Plating-Foto und Storytelling. Starten Sie noch heute.",
      "keywords": "Rezeptblätter KI, Rezeptblatt Gericht, automatische Allergene, Kosten pro Portion, Rezeptblatt Restaurant",
      "ogImage": "https://aichef.pro/og/use-cases/task-fichas-tecnicas-con-ia.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihre Küche zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit «Wer sind Sie?»: Sie geben Küchenart, Spezialität und Volumen an. Die Struktur des Rezeptblatts passt sich Ihrem Konzept an: Casual-Restaurant, Fine Dining, Patisserie, Gelateria usw.",
    "appsTitle": "Die KI-Agenten, die Sie für Rezeptblätter verwenden",
    "apps": [
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Rezepte + vollständiges Rezeptblatt mit allen Feldern."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Süße Rezeptblätter mit Stundensätzen der Produktionsküche."
      },
      {
        "name": "Kreative Gelateria",
        "category": "Kulinarische Kreativität",
        "description": "Rezeptblätter mit technischem Gleichgewicht von Zucker, Feststoffen und Fetten."
      },
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Rezept."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools und Utilities",
        "description": "Automatischer Umrechner für Gewichte und Maße."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools und Utilities",
        "description": "Skalierung von Rezepten für Bankette und Veranstaltungen."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Abfalldaten pro Prozess, integriert in das Rezeptblatt."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Empfohlene Weinbegleitung zur Aufnahme in das Rezeptblatt."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Referenzbild des angerichteten Gerichts."
      },
      {
        "name": "Gastro Lexikum",
        "category": "Gastro-Wissen",
        "description": "Tutor für technische Definitionen zur Validierung der Terminologie."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Inhalte und Social Media",
        "description": "300+ Prompts für Rezeptblätter und Beschreibungen."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog zur Validierung von Technik und Zutaten."
      }
    ],
    "metrics": [
      {
        "value": "×20",
        "label": "Geschwindigkeit vs. manuelles Rezeptblatt"
      },
      {
        "value": "100 %",
        "label": "Allergene automatisch identifiziert"
      },
      {
        "value": "ISO",
        "label": "Rezeptblätter bereit für Audit 22000"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihre Rezeptblätter"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "2 Wochen, um 28 Gerichte zu dokumentieren",
        "Allergene von Hand berechnet (rechtliches Risiko)",
        "Improvisiertes Storytelling im Service",
        "Zutatenänderungen ohne Aktualisierung der Rezeptblätter",
        "Keine standardisierte professionelle Vorlage"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "28 Gerichte an einem Tag mit professioneller Vorlage dokumentiert",
        "Automatische Allergene mit Allergen-ID",
        "Professionelles Storytelling für das Service-Briefing",
        "Änderungen aktualisieren Rezeptblatt und Allergene sofort",
        "Einheitliche Vorlage, bereit für Audits und Zertifizierungen"
      ]
    },
    "galleryTitle": "So funktionieren Rezeptblätter mit KI",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Rezeptblatt, Binder, Plating-Foto, Tablet und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-document.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-binder.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-photo.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-tablet.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-team.jpg"
    ]
  },
  "task-maridajes-con-ia": {
    "h1": "So validieren Sie Pairings mit KI",
    "heroSubtitle": "Validieren Sie Pairings mit wissenschaftlicher Basis: Analyse von Säure, Tanninen, Struktur, Intensität und Harmonie. Eine Suite gastronomischer KI-Agenten mit professioneller Sommelier-Technik.",
    "heroTagline": "Wissenschaftliche Pairings in Minuten für jede Speisekarte",
    "badge": "Aufgabe: Professionelle Pairings",
    "painsTitle": "Was es kostet, Pairings von Hand zu erstellen",
    "pains": [
      "Intuitiv empfohlene Pairings ohne fundamentierte wissenschaftliche Basis",
      "Serviceteam ohne laufende Schulung, um Pairings fachgerecht zu kommunizieren",
      "Änderungen an Karte oder Weinkeller ohne Neuvalidierung der Pairings – Empfehlungen werden veraltet",
      "Nur Wein-Pairings: Bier-, Sake-, Kombucha-, Tee- und alkoholfreie Optionen fehlen",
      "Improvisiertes Storytelling je Pairing ohne fachliche Tiefe",
      "Ad-hoc-Pairings bei privaten Veranstaltungen ohne professionelles Konzept"
    ],
    "featuresTitle": "So meistert AI Chef Pro Pairings",
    "features": [
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Spezialisierter Agent für Pairings auf wissenschaftlicher Basis: Analyse von Säure, Tanninen, Struktur, Intensität, Harmonie und Kontrast."
      },
      {
        "icon": "Sparkles",
        "title": "Bar & Lounge AI+",
        "description": "Konkrete Kellerauswahl für jedes Pairing mit professionellem Sommelier-Fachwissen: Weine, Sake, Biere, Schaumweine."
      },
      {
        "icon": "BookOpen",
        "title": "Professionelles Storytelling",
        "description": "Jedes Pairing enthält eine technische Beschreibung, damit das Serviceteam professionell kommuniziert."
      },
      {
        "icon": "Calculator",
        "title": "Pairing-Kalkulation",
        "description": "Echte Kosten pro Glas, Food Cost des Weins und Preisvorschlag für das Pairing im Degustationsmenü."
      },
      {
        "icon": "Sparkles",
        "title": "Alkoholfreie Pairings",
        "description": "Vorschläge mit Kombucha, Tee, Essen aus, Kaffee und hausgemachtem Tonic für Gäste, die keinen Alkohol trinken."
      },
      {
        "icon": "CheckSquare",
        "title": "Pack APPCC Weinkeller",
        "description": "Rückverfolgbarkeit im Weinkeller und Serviertemperatur je nach Weinstyp."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Verkostungen und Events mit Pairing, saisonale Produkteinführungen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Referenzbild des Pairings (Glas + Gericht) für Instagram und Speisekarte."
      },
      {
        "icon": "BookOpen",
        "title": "Gastro Lexikum",
        "description": "Tutor für Fachbegriffe: Önologie, Vinifikation, Terroir, Herkunftsbezeichnungen."
      }
    ],
    "workflowTitle": "So validieren Sie Pairings in 4 Schritten",
    "workflow": [
      "1. Food Pairing AI – Laden Sie das Gericht mit Technik und Zutaten. Die KI analysiert Säure, Tannine, Intensität, Struktur hoch schlägt die Weinsorte wissenschaftlich begründet vor.",
      "2. Bar & Lounge AI+ – schlägt eine konkrete Auswahl aus Ihrem Weinkeller vor: Jahrgänge, Erzeuger, Glas oder Flasche. Für alkoholfreie Optionen schlägt es Kombuchas, Tees oder hausgemachte Tonic vor.",
      "3. Storytelling für den Service – jedes Pairing erzeugt eine professionelle Beschreibung für das B Briefing des Teams und die Kommunikation mit dem Gast.",
      "4. Kit de Escandallos Pro – kalkulieren Sie die realen Kosten pro Glas, den Food Cost des Weins und einen Preisvorschlag für das Pairing."
    ],
    "productsTitle": "Vorlagen und empfohlene Kits für Pairings",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Food Pairing AI hat meine Art, Pairings zu finalisieren, verändert. Jedes Gericht des Degustationsmenüs hat jetzt ein wissenschaftlich fundiertes Pairing, das mein Serviceteam mit Fachkompetenz kommuniziert. Wir haben die Marge im Weinkeller um 6 Prozentpunkte gesteigert, und die Premium-Stammgäste sind in 6 Monaten um 35 % gewachsen.",
    "testimonialAuthor": "Eduardo Lara",
    "testimonialRole": "Head Sommelier, Restaurant mit 1 Michelin-Stern",
    "faqTitle": "Häufige Fragen zu KI-gestützten Pairings",
    "faqs": [
      {
        "q": "Passt das für jeden Restauranttyp?",
        "a": "Ja. Food Pairing AI deckt alles ab – vom Casual Dining bis zum Fine-Dining-Michelin, inklusive Gastrobars, Weinbars und ethnischen Restaurants."
      },
      {
        "q": "Hat das wirklich eine wissenschaftliche Basis?",
        "a": "Ja. Sie arbeitet wie professionelle Sommeliers mit fachlichem Wissen aus Önologie und Bromatologie: Säure, Tannine, Struktur, Intensität, Harmonie und Kontrast."
      },
      {
        "q": "Sind auch alkoholfreie Pairings abgedeckt?",
        "a": "Ja. Sie schlägt Kombuchas, Tees, Kaffee, hausgemachte Tonics und Funktionsgetränke mit professionellem Anspruch für Gäste vor, die keinen Alkohol trinken."
      },
      {
        "q": "Berücksichtigt sie Packungen mit Bier, Sake, Schaumwein?",
        "a": "Ja. Bar & Lounge AI+ deckt das gesamte Bar-Spektrum ab: Weine, Sakes, Craft-Biere, Schaumweine und Spirituosen."
      },
      {
        "q": "Erzeugt sie visuelle Inhalte für das Pairing auf Instagram?",
        "a": "Ja. GastroIMG Gen+ erzeugt ein Referenzbild. Denken Sie daran: Das KI-Bild dient nur als visuelle Referenz – das finale Foto machen Sie selbst mit Ihrem echten Glas und Gericht."
      }
    ],
    "ctaTitle": "Ihre Pairings mit wissenschaftlicher Basis in Minuten.",
    "ctaSubtitle": "Starten Sie mit dem 2-Minuten-Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "Pairings mit KI validieren: Weine, Sake und alkoholfreie Optionen | AI Chef Pro",
      "description": "KI-Suite für Pairings: Food Pairing AI mit wissenschaftlicher Basis, Kellerauswahl und Storytelling für Service. Noch heute starten.",
      "keywords": "Pairings mit KI, Food Pairing KI, Wein-Gericht-Pairing, Sommelier-KI, alkoholfreie Pairings KI, wissenschaftliches Pairing",
      "ogImage": "https://aichef.pro/og/use-cases/task-maridajes-con-ia.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Weinkeller zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit «Wer sind Sie?»: Sie geben Restauranttyp, Weinkellergröße, Schwerpunkt und Niveau an. Jedes Pairing wird auf Ihren realen Inventar abgestimmt, nicht auf einen generischen Weinkeller.",
    "appsTitle": "KI-Agenten für Pairings",
    "apps": [
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Pairings auf wissenschaftlicher Basis für jedes Gericht."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Konkrete Kellerauswahl mit Sommelier-Kompetenz."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Professionelles Pairing-Storytelling für den Service."
      },
      {
        "name": "Gastro Lexikum",
        "category": "Gastro-Wissen",
        "description": "Tutor für Definitionen aus Önologie und Vinbereitung."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge und Utilities",
        "description": "Integrierte Verlustanalyse für fehlgeschlagenes Korkenziehen."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge und Utilities",
        "description": "Sulfiterkennung für empfindliche Gäste."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Referenzbild des Pairings."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Tiefenanalyse von Weinkellern und Jahrgängen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte und Social Media",
        "description": "Verkostungen und Events mit Pairing."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und Social Media",
        "description": "SEO-Artikel zu Pairings und Weinkellern."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Inhalte und Social Media",
        "description": "Instagram mit propsierten Pairings."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Inhalte und Social Media",
        "description": "300+ Prompts für Pairing-Beschreibungen."
      }
    ],
    "metrics": [
      {
        "value": "×10",
        "label": "Schnelligkeit vs. manuelle Validierung"
      },
      {
        "value": "+6 pp",
        "label": "Marge nach Weinkostenkalkulation"
      },
      {
        "value": "+35 %",
        "label": "Premium-Stammgäste"
      },
      {
        "value": "12+",
        "label": "KI-Agenten für Pairings"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Intuitive Pairings ohne wissenschaftliche Basis",
        "Keine professionellen alkoholfreien Optionen",
        "Serviceteam ohne dokumentierte Schulung",
        "Kelleränderungen ohne Neuvalidierung der Pairings",
        "Ad-hoc-Pairings für private Veranstaltungen"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Wissenschaftlich fundierte Pairings von Food Pairing AI",
        "Optionen mit Kombucha, Tee und hausgemachtem Tonic",
        "Team-Briefing mit professionellem Storytelling",
        "Kelleränderungen validieren Pairings sofort neu",
        "Pairings für geschlossene Events mit professionellem Konzept"
      ]
    },
    "galleryTitle": "So funktioniert die Pairing-Validierung mit KI",
    "gallerySubtitle": "Das koordinieren Sie mit AI Chef Pro: Gläser, Gerichte, Notizen, Weinkeller und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-glasses.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-plate.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-notes.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-bottles.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-team.jpg"
    ]
  },
  "task-reducir-mermas-con-ia": {
    "h1": "So reduzieren Sie Lebensmittelabfälle in der Küche mit KI",
    "heroSubtitle": "Identifizieren, messen und reduzieren Sie Lebensmittelabfälle pro Prozess (Zerlegung, Formen, Backen, Vitrine, Lieferung) mit echten Daten, die in die Rezepturkalkulation integriert sind. Suite spezialisierter gastronomischer KI-Agenten für den Zero-Waste-Betrieb.",
    "heroTagline": "Weniger Lebensmittelabfälle mit echten Daten pro Prozess",
    "badge": "Aufgabe: Reduzierung von Lebensmittelabfällen",
    "painsTitle": "Was unkontrollierte Lebensmittelabfälle kosten",
    "pains": [
      "Geschätzte Lebensmittelabfälle nach Augenmaß (15-30 % bei einigen Schnitten), keine echten Daten pro Prozess",
      "Fehlende Daten nach Küchenart (Eisdiele, Bäckerei, Grill, Sushi haben unterschiedliche Abfälle)",
      "Kein System zur Wiederverwertung von Abschnitten und Schalen (Brühen, angesetzte Essige, Trockenprodukte)",
      "Wenn der Lieferant wechselt, ändern sich die Abfälle, ohne dass die Marge neu berechnet wird",
      "Team ohne kontinuierliche Schulung in professioneller Verwertungstechnik",
      "Keine Rückverfolgbarkeit für Nachhaltigkeitsaudits und Zero-Waste-Zertifizierungen"
    ],
    "featuresTitle": "So reduziert AI Chef Pro Lebensmittelabfälle",
    "features": [
      {
        "icon": "BarChart3",
        "title": "Lebensmittelabfälle AI",
        "description": "Präzise Daten zu Lebensmittelabfällen pro Prozess und Küchenart: Zerlegung, Dry-Aging, Formen, Backen, Vitrine, Lieferung."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche",
        "description": "Entwickelt Wiederverwertungstechniken: Abschnitte zu Brühen, Schalen zu angesetzten Essigen, Reste zu Trockenprodukten – mit professionellem Anspruch."
      },
      {
        "icon": "Calculator",
        "title": "Lebensmittelabfälle in der Rezepturkalkulation",
        "description": "Tatsächliche Abfälle pro Prozess, integriert in die Rezepturkalkulation des Kit de Escandallos Pro: Die Kosten pro Gericht bilden den tatsächlichen, nicht den geschätzten Abfall ab."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Vorlagen mit Verwertungsabläufen pro Station, wöchentliche Kontrolle der Lebensmittelabfälle, Teamschulung."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC nachvollziehbar",
        "description": "Rückverfolgbarkeit von Lebensmittelabfällen pro Prozess für Nachhaltigkeitsaudits und Zero-Waste-Zertifizierungen."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus mit AI+",
        "description": "Fermente zur Wiederverwertung von Produkten: Sauerkraut aus Kohlresten, Kombucha aus Obstschalen, Garum aus Fischgräten."
      },
      {
        "icon": "Sparkles",
        "title": "VegChef Plant-Based",
        "description": "Für die professionelle pflanzliche Wiederverwertung: vollständige Verwertung des Gemüses, Stems-to-Roots-Technik."
      },
      {
        "icon": "BarChart3",
        "title": "Calcula Pax",
        "description": "Einkauf, abgestimmt auf das tatsächliche Event- oder Servicevolumen, um Überschüsse von vornherein zu reduzieren."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Produktionsplanung, abgestimmt auf die historische Nachfrage, um Überproduktion zu reduzieren."
      }
    ],
    "workflowTitle": "So reduzieren Sie Lebensmittelabfälle in 4 Schritten",
    "workflow": [
      "1. Lebensmittelabfälle AI – der KI-Agent liefert echte Daten pro Prozess und Küchenart (Fleischzerlegung, Pastateig, Brotbacken, Eistheke, Pizzalieferservice). Sie erfassen die echten Daten Ihres Betriebs.",
      "2. Kreativküche + Fermentus mit AI+ – Sie entwickeln Wiederverwertungstechniken: Abschnitte zu Brühen, Schalen zu Essigen, Reste zu Trockenprodukten, Überschüsse zu Fermenten.",
      "3. Kit de Escandallos Pro – Die Rezepturkalkulation bildet den tatsächlichen, nicht den geschätzten Abfall ab. Die Kosten pro Gericht steigen leicht, bilden aber die wahren Kosten ab und verhindern so böse Überraschungen bei der Marge.",
      "4. Calcula Pax + Gastro Calendar – Einkauf, abgestimmt auf das tatsächliche Service- oder Eventvolumen, um Überschüsse von vornherein zu reduzieren, anstatt Abfälle erst später zu verarbeiten."
    ],
    "productsTitle": "Vorlagen und Kits zur Reduzierung von Lebensmittelabfällen",
    "productIds": [
      "kit-escandallos",
      "kit-inventario",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-tareas",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Lebensmittelabfälle AI + Kreativküche haben unseren Betrieb verändert. Wir sind von geschätzten Abfällen (wir kalkulierten 12-15 %) zu echten Daten von 22-28 % bei einigen Prozessen übergegangen. Wir haben Zerlegung und Verwertung mit dokumentierter Technik neu organisiert und die Abfälle in 4 Monaten um 35 % reduziert. Die Rezepturkalkulation bildet jetzt die echten Kosten ab, nicht die idealen.",
    "testimonialAuthor": "Sofía Cano",
    "testimonialRole": "Souschef, ungezwungenes Restaurant mit Zero-Waste-Engagement",
    "faqTitle": "Häufige Fragen zur Reduzierung von Lebensmittelabfällen mit KI",
    "faqs": [
      {
        "q": "Funktioniert das für jede Küchenart?",
        "a": "Ja. Lebensmittelabfälle AI deckt Daten pro Prozess und Küchenart ab: Grill, Sushi, Pasta, Brot, Eis, Schokolade, Soßen, Marinade. Jede Küche hat andere Abfälle."
      },
      {
        "q": "Wie integriere ich echte Abfälle in die Rezepturkalkulation?",
        "a": "Das Kit de Escandallos Pro hat ein Feld für Abfall pro Zutat und Prozess. Lebensmittelabfälle AI liefert die echten Daten, damit die Kosten pro Gericht die Realität widerspiegeln."
      },
      {
        "q": "Sind professionelle Wiederverwertungstechniken abgedeckt?",
        "a": "Ja. Kreativküche liefert Verwertungstechniken: pflanzliche Stems-to-Roots-Verwertung, Abschnitte zu Brühen, Schalen zu Essigen, Fermente aus Resten. Fermentus vertieft fortgeschrittene Techniken."
      },
      {
        "q": "Erzeugt es eine Rückverfolgbarkeit für Zero-Waste-Zertifizierungen?",
        "a": "Ja. Pack APPCC + Lebensmittelabfälle AI liefern eine dokumentierte Rückverfolgbarkeit für Nachhaltigkeitsaudits und Zero-Waste- oder B-Corp-Zertifizierungen."
      },
      {
        "q": "Wie hilft es mir bei einem abgestimmten Einkauf?",
        "a": "Calcula Pax + Gastro Calendar planen Produktion und Einkauf abgestimmt auf das tatsächliche Servicevolumen, um Überschüsse von vornherein zu reduzieren."
      }
    ],
    "ctaTitle": "Ihre Küche mit weniger Abfall und echten Daten.",
    "ctaSubtitle": "Beginnen Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "So reduzieren Sie Lebensmittelabfälle in der Küche mit KI: Echte Daten und Wiederverwertung | AI Chef Pro",
      "description": "KI-Suite zur Reduzierung von Lebensmittelabfällen: Lebensmittelabfälle AI mit echten Daten, professionelle Wiederverwertung, nachvollziehbare Rezepturkalkulation. Legen Sie heute los.",
      "keywords": "Lebensmittelabfälle Restaurant reduzieren, Lebensmittelabfälle KI, Food Waste KI, Zero Waste Küche, Abfälle Produktion, Verschwendung reduzieren",
      "ogImage": "https://aichef.pro/og/use-cases/task-reducir-mermas-con-ia.jpg"
    },
    "personalizationTitle": "Ab der ersten Minute auf Ihre Küche zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit «Wer sind Sie?»: Sie geben die Art der Küche und das Volumen an. Lebensmittelabfälle AI liefert datenbasierte Werte pro Prozess, abgestimmt auf Ihr Konzept: Grill, Sushi, Pasta, Brot, Eis, Schokolade.",
    "appsTitle": "Die KI-Agenten, die Sie zur Reduzierung von Lebensmittelabfällen einsetzen",
    "apps": [
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Werkzeuge & Dienstprogramme",
        "description": "Echte Daten zu Lebensmittelabfällen pro Prozess und Küchenart."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Professionelle Wiederverwertungstechniken für Abschnitte und Reste."
      },
      {
        "name": "Fermentus mit AI+",
        "category": "Kulinarische Kreativität",
        "description": "Fermente zur Wiederverwertung von Resten (Sauerkraut, Kombucha, Garum)."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Kulinarische Kreativität",
        "description": "Vollständige Verwertung von Gemüse (Stems-to-Roots)."
      },
      {
        "name": "Calcula Pax",
        "category": "Werkzeuge & Dienstprogramme",
        "description": "Einkauf, abgestimmt auf das tatsächliche Servicevolumen."
      },
      {
        "name": "Conversor Ing",
        "category": "Werkzeuge & Dienstprogramme",
        "description": "Umrechner für Gewichte und Maße für Präzision."
      },
      {
        "name": "Allergen-ID",
        "category": "Werkzeuge & Dienstprogramme",
        "description": "Kennzeichnung bei wiederverwerteten Produkten."
      },
      {
        "name": "Gastro Calendar",
        "category": "Inhalte & Soziale Medien",
        "description": "Produktionsplanung, abgestimmt auf die historische Nachfrage."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte & Soziale Medien",
        "description": "SEO-Artikel über Nachhaltigkeit, um Traffic zu generieren."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Referenzbilder für Zero-Waste-Gerichte."
      },
      {
        "name": "Mental Coach",
        "category": "Werkzeuge & Dienstprogramme",
        "description": "Coaching für die Teamführung im Zero-Waste-Bereich."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Recherche zu Zero-Waste-Techniken von Vorbildern."
      }
    ],
    "metrics": [
      {
        "value": "−35 %",
        "label": "Lebensmittelabfälle in 4 Monaten"
      },
      {
        "value": "+4 %-Punkte",
        "label": "Marge nach Integration der tatsächlichen Abfälle"
      },
      {
        "value": "×3",
        "label": "Geschwindigkeit vs. manuelle Schätzung"
      },
      {
        "value": "12+",
        "label": "Agenten zur Reduzierung von Lebensmittelabfällen"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Lebensmittelabfälle nach Augenmaß geschätzt, Rezepturkalkulation mit zu niedrigen Kosten",
        "Keine dokumentierte Wiederverwertungstechnik",
        "Allgemeiner Einkauf ohne Anpassung an das tatsächliche Volumen",
        "Team ohne Schulung in professioneller Verwertung",
        "Keine Rückverfolgbarkeit für Nachhaltigkeitsaudits"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Tatsächliche Lebensmittelabfälle pro Prozess dokumentiert",
        "Wiederverwertungstechniken mit Kreativküche + Fermentus",
        "Einkauf, abgestimmt auf das tatsächliche Volumen mit Calcula Pax",
        "Teameinweisung mit dokumentierter Technik",
        "APPCC-Rückverfolgbarkeit für Zero-Waste-Audits"
      ]
    },
    "galleryTitle": "So funktioniert die Reduzierung von Lebensmittelabfällen mit KI",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Wiegen, Tracking, Organisation, Wiederverwertung und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-mermas-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-scale.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-tracking.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-bins.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-recovery.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-team.jpg"
    ]
  },
  "task-appcc-digital-con-ia": {
    "h1": "So verwalten Sie digitales APPCC mit KI",
    "heroSubtitle": "Ersetzen Sie verstreutes Papier durch APPCC vom Handy mit professionellen Vorlagen: Temperaturen, Reinigung, Rückverfolgbarkeit, Allergene, Schädlinge, Öl und Wasser. Suite gastronomischer KI-Agenten mit regulatorischer Grundlage.",
    "heroTagline": "Professionelles APPCC vom Handy ohne Papier",
    "badge": "Aufgabe: APPCC und Lebensmittelsicherheit",
    "painsTitle": "Was die APPCC-Verwaltung auf Papier kostet",
    "pains": [
      "Verstreutes Papier in der Küche, unvollständige Aufzeichnungen bei Inspektionen",
      "Keine Standardisierung nach Konzept (Eisdiele, Bäckerei, Grill, Sushi haben unterschiedliche Aufzeichnungen)",
      "Allergene manuell pro Rezept berechnet, rechtliches und Sicherheitsrisiko",
      "Änderungen der Vorschriften ohne Aktualisierung von Vorlagen und Verfahren",
      "Wechselndes Team ohne ständige Schulung in Lebensmittelsicherheit",
      "Keine Rückverfolgbarkeit für Audits nach ISO 22000, BRC, IFS oder Qualitätszertifizierungen"
    ],
    "featuresTitle": "Wie AI Chef Pro das APPCC löst",
    "features": [
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC mit Excel-Vorlagen",
        "description": "17 herunterladbare Excel-Vorlagen: Temperaturen, Reinigung, Rückverfolgbarkeit, Allergene, Schädlinge, Öl und Wasser."
      },
      {
        "icon": "Sparkles",
        "title": "Allergen-ID",
        "description": "Automatische Identifizierung von Allergenen nach Zutat und Rezept. Wenn Sie eine Zutat ändern, wird sofort neu berechnet."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas mit APPCC",
        "description": "Aufgabenvorlagen mit integriertem APPCC pro Schicht: Eröffnung, Service, Schließung."
      },
      {
        "icon": "BarChart3",
        "title": "Rückverfolgbarkeit von Produkten",
        "description": "Rückverfolgbarkeit von frischem Fisch, Milchprodukten, Nüssen, Fermenten, Konserven mit kritischen Temperaturen."
      },
      {
        "icon": "BookOpen",
        "title": "Kreativküche mit APPCC",
        "description": "Rezepte mit integrierten APPCC-Verfahren in der technischen Karte: Temperatur, Lagerung, Allergene."
      },
      {
        "icon": "Calendar",
        "title": "Geplante Reinigung",
        "description": "Kalender für gründliche Reinigung nach Station und Schicht mit spezifischen Vorlagen und digitaler Signatur."
      },
      {
        "icon": "Sparkles",
        "title": "Pro Prompts eBook",
        "description": "300+ professionelle Prompts für APPCC-Verwaltung, Team-Schulung und Kommunikation mit Inspektoren."
      },
      {
        "icon": "Wine",
        "title": "Pack APPCC für den Weinkeller",
        "description": "Rückverfolgbarkeit von Weinen, Entkorken, Lagerung und Serviertemperaturen nach Typ."
      },
      {
        "icon": "BarChart3",
        "title": "Sonar Deep Research",
        "description": "Tiefgehende Recherche zu Gesundheitsvorschriften nach Land, autonomer Region und Betriebsart."
      }
    ],
    "workflowTitle": "So implementieren Sie digitales APPCC in 4 Schritten",
    "workflow": [
      "1. Pack APPCC (14 €, herunterladbare Excel-Vorlagen) – Sie laden die 17 professionellen Vorlagen herunter, die an Ihre Küchenart angepasst sind (Patisserie, Eisdiele, Restaurant usw.).",
      "2. Allergen-ID – scannt automatisch Rezepte und Vorlagen Ihrer Speisekarte, um Allergene pro Gericht zu identifizieren. Es integriert sie in die technischen Karten und in den Service.",
      "3. Kreativküche mit integriertem APPCC – jedes neue Rezept liefert APPCC-Verfahren (kritische Temperatur, Lagerung, Allergene, Aufbewahrung) integriert in die technische Karte.",
      "4. Kit de Tareas mit APPCC – Schichtvorlagen (Eröffnung, Service, Schließung) mit integriertem APPCC. Das Team signiert jede Schicht digital vom Handy aus."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für APPCC",
    "productIds": [
      "pack-appcc",
      "kit-tareas",
      "pro-prompts-ebook",
      "kit-escandallos",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Pack APPCC + Allergen-ID haben unsere Lebensmittelsicherheit transformiert. Wir sind von verstreutem Papier zu 17 digitalen Vorlagen mit integriertem APPCC pro Schicht und automatischen Allergenen pro Rezept übergegangen. Die Hygienekontrolle läuft einwandfrei und das rechtliche Risiko ist auf null gesunken.",
    "testimonialAuthor": "Roberto Castaño",
    "testimonialRole": "F&B Director, 5-Sterne-Hotel mit 4 Outlets",
    "faqTitle": "Häufige Fragen zu APPCC mit KI",
    "faqs": [
      {
        "q": "Gilt das für jede Art von Betrieb?",
        "a": "Ja. Pack APPCC passt Vorlagen an Restaurant, Café, Patisserie, Eisdiele, Schokoladenmanufaktur, Pizzeria, Dark Kitchen, Bar, Catering, Hotel an."
      },
      {
        "q": "Wie verwalte ich Allergene automatisch?",
        "a": "Allergen-ID identifiziert Allergene nach Zutat und Rezept, integriert sie in technische Karten und APPCC-Vorlagen. Wenn Sie eine Zutat ändern, wird sofort neu berechnet."
      },
      {
        "q": "Deckt es europäische und lateinamerikanische Vorschriften ab?",
        "a": "Ja. Pack APPCC deckt europäische Vorschriften ab (EU 852/2004 + 178/2002 + 1169/2011 Allergene) und Anpassungen für Lateinamerika. Sonar Deep Research ermöglicht die Abfrage spezifischer Vorschriften nach Land."
      },
      {
        "q": "Erzeugt es Rückverfolgbarkeit für ISO-Audits?",
        "a": "Ja. APPCC vom Handy mit digitaler Signatur + Rückverfolgbarkeit von Produkten + Reinigungskalender, bereit für Audits nach ISO 22000, BRC, IFS, FSSC 22000."
      },
      {
        "q": "Wie hilft es mir bei regulatorischen Änderungen?",
        "a": "Sonar Deep Research fragt aktuelle Vorschriften nach Land und autonomer Region ab. Kreativküche aktualisiert technische Karten und Verfahren, wenn sich die Normen ändern."
      }
    ],
    "ctaTitle": "Ihr professionelles APPCC vom Handy aus ohne Papier.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliedsplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "So verwalten Sie digitales APPCC mit KI: Vorlagen, Allergene und Rückverfolgbarkeit | AI Chef Pro",
      "description": "KI-Suite für digitales APPCC: Excel-Vorlagen, automatische Allergene, ISO-Rückverfolgbarkeit. Starten Sie noch heute.",
      "keywords": "digitales APPCC KI, APPCC-Vorlagen, automatische Allergene, ISO 22000 KI, Lebensmittelsicherheit KI, digitales HACCP",
      "ogImage": "https://aichef.pro/og/use-cases/task-appcc-digital-con-ia.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Betrieb zugeschnitten",
    "personalizationBody": "AI Chef Pro startet mit «Wer sind Sie?»: Sie geben Art des Betriebs und Land an. Pack APPCC passt Vorlagen an Ihr Konzept und lokale Vorschriften an.",
    "appsTitle": "Die KI-Agenten, die Sie für APPCC nutzen",
    "apps": [
      {
        "name": "Allergen-ID",
        "category": "Tools und Utilities",
        "description": "Automatische Identifizierung von Allergenen pro Rezept."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Rezepte mit integrierten APPCC-Verfahren."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Spezifisches APPCC für Patisserie und Backstuben."
      },
      {
        "name": "Kreative Gelateria",
        "category": "Kulinarische Kreativität",
        "description": "Spezifisches APPCC für Eisdielen mit empfindlichem Produkt."
      },
      {
        "name": "Kreative Schokolade",
        "category": "Kulinarische Kreativität",
        "description": "Spezifisches APPCC für Schokoladenmanufaktur und Pralinenherstellung."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools und Utilities",
        "description": "Rückverfolgbarkeit von Lebensmittelabfällen integriert in das APPCC."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools und Utilities",
        "description": "Umrechner für Gewichte und Maße."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Tiefgehende Recherche zu Vorschriften nach Land."
      },
      {
        "name": "Gastro Lexikum",
        "category": "Gastro-Wissen",
        "description": "Tutor für technische regulatorische Definitionen."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Inhalte und soziale Medien",
        "description": "300+ Prompts für APPCC-Verwaltung."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte und soziale Medien",
        "description": "Artikel über Lebensmittelsicherheit für organischen Traffic."
      },
      {
        "name": "Mental Coach",
        "category": "Tools und Utilities",
        "description": "Coaching für Stressmanagement bei Inspektionen."
      }
    ],
    "metrics": [
      {
        "value": "ISO",
        "label": "Vorlagen bereit für 22000, BRC, IFS"
      },
      {
        "value": "100 %",
        "label": "Allergene automatisch identifiziert"
      },
      {
        "value": "0 %",
        "label": "rechtliches Risiko durch nicht deklarierte Allergene"
      },
      {
        "value": "12+",
        "label": "Agenten für Ihr APPCC"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Verstreutes Papier in der Küche",
        "Allergene manuell berechnet (rechtliches Risiko)",
        "Keine an die Küchenart angepasste Vorlagen",
        "Wechselndes Team ohne dokumentierte Schulung",
        "Keine Rückverfolgbarkeit für ISO-Audits"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "APPCC vom Handy mit digitaler Signatur",
        "Automatische Allergene mit Allergen-ID",
        "Excel-Vorlagen nach Konzept angepasst",
        "Briefing mit integriertem APPCC im Kit de Tareas",
        "Rückverfolgbarkeit bereit für ISO 22000, BRC, IFS"
      ]
    },
    "galleryTitle": "Wie digitales APPCC mit KI funktioniert",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Thermometer, Tablet, Kamera, Reinigung und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-appcc-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-appcc-thermometer.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-appcc-tablet.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-appcc-fridge.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-appcc-cleaning.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-appcc-team.jpg"
    ]
  },
  "task-carta-estacional-con-ia": {
    "h1": "So entwerfen Sie eine Saisonkarte mit KI",
    "heroSubtitle": "Entwerfen Sie eine Saisonkarte mit saisonalen lokalen Produkten, professioneller Kalkulation, vorausschauender Planung und Erzeuger-Storytelling. Suite gastronomischer KI-Agenten mit Kalender nach Hemisphäre und Region.",
    "heroTagline": "Saisonkarte mit professionellem Anspruch in Stunden",
    "badge": "Aufgabe: Saisonkarte",
    "painsTitle": "Was es kostet, eine Saisonkarte von Hand zu entwerfen",
    "pains": [
      "Eine Woche oder mehr für Iteration und Finalisierung der Saisonkarte mit validierter Kalkulation",
      "Kein klares Konzept für lokale Produkte nach Saison und Region (unterschiedlich je nach Hemisphäre)",
      "Produkte außerhalb der Saison mit hohen Kosten und hohem Verderb (Import, Kühlung)",
      "Kein Storytelling für lokale Erzeuger für Service und Kommunikation",
      "Abrupte Wechsel zwischen den Saisons ohne vorausschauende Planung",
      "Keine Koordination mit Feiertagskalender (Ostern, Weihnachten, Muttertag, lokale Veranstaltungen)"
    ],
    "featuresTitle": "Wie AI Chef Pro die Saisonkarte löst",
    "features": [
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Saisonale Planung nach Hemisphäre und Region mit saisonalen lokalen Produkten und wichtigen Feiertagen."
      },
      {
        "icon": "Sparkles",
        "title": "Saisonale Kreativküche",
        "description": "Entwickelt Signature-Gerichte mit saisonalen lokalen Produkten: Herbstpilze, Frühlingsspargel, Sommergemüse, Winterwurzeln."
      },
      {
        "icon": "Calculator",
        "title": "Saisonale Kalkulation",
        "description": "Rezept + CSV-Kalkulation mit lokalen Produkten; Kit de Escandallos Pro berechnet die Marge bei Saisonwechsel neu."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling der Erzeuger",
        "description": "Jedes Gericht enthält Storytelling über lokale Erzeuger: Viehzüchter, Landwirt, Bäcker, Fischer – für die Kommunikation mit Service und Gästen."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Saisonale Weine und auf saisonale Produkte abgestimmte Pairings für Ihre Karte."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Saisonale KI-Fotografie + Pinterest gewinnt organischen Traffic für saisonale Produkte."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Vorlagen für den Übergang zwischen den Saisons: Lagerrotation, Teameinarbeitung, Kartenlaunch."
      },
      {
        "icon": "Sparkles",
        "title": "VegChef Plant-Based",
        "description": "Für saisonales Gemüse mit fortgeschrittenen Techniken (Fermente, Trocknung, Konserven)."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients AI",
        "description": "Sosa-Katalog, um lokale Produkte mit professioneller Technik zu ergänzen."
      }
    ],
    "workflowTitle": "So entwerfen Sie eine Saisonkarte in 5 Schritten",
    "workflow": [
      "1. Gastro Calendar – Sie definieren Hemisphäre, Region und Saison (z. B. Herbst Nordhalbkugel, Madrid). Der KI-Agent liefert saisonale lokale Produkte und wichtige Feiertage (Muttertag, Weihnachten, Valentinstag).",
      "2. Kreativküche – Sie entwickeln Signature-Gerichte mit lokalen Produkten. Jedes Rezept liefert Rezept + CSV-Kalkulation + Erzeuger-Storytelling.",
      "3. Kit de Escandallos Pro – Sie laden die CSVs mit Ihren realen Preisen lokaler Lieferanten hoch, validieren Marge und Food-Cost-Prozentsatz pro Gericht und Gesamtkarte.",
      "4. Bar & Lounge AI+ + Food Pairing AI – Sie aktualisieren saisonale Weine und passende Pairings für saisonale Produkte.",
      "5. GastroIMG Gen+ + Pinterest Pins Gen – Sie generieren Referenzbilder der neuen Karte und optimierte Pins, um saisonalen organischen Traffic zu gewinnen."
    ],
    "productsTitle": "Empfohlene Vorlagen und Kits für die Saisonkarte",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Gastro Calendar + Kreativküche haben unsere Saisonkarten-Erstellung revolutioniert. Was früher eine Woche dauerte, ist jetzt ein Tag mit professioneller Kalkulation, nachvollziehbaren lokalen Produkten und Storytelling der Erzeuger für den Service. Unsere Marge stieg um 6 Punkte und die Akquise mit Pinterest Pins Gen für saisonale Produkte hat sich verdoppelt.",
    "testimonialAuthor": "Marina Lozano",
    "testimonialRole": "Küchenchefin, gehobenes Restaurant mit regionalen Produkten",
    "faqTitle": "Häufige Fragen zur Saisonkarte mit KI",
    "faqs": [
      {
        "q": "Funktioniert es für Nord- und Südhalbkugel?",
        "a": "Ja. Gastro Calendar passt lokale Produkte und Saison je nach Hemisphäre und Region an. Was in Spanien Herbst ist, ist in Argentinien Frühling."
      },
      {
        "q": "Wie verwaltet es lokale Produkte mit variablen Kosten?",
        "a": "Kit de Escandallos Pro berechnet sofort die Marge neu, wenn Sie Preise aktualisieren. Lebensmittelabfälle AI fügt die Kosten saisonaler Lebensmittelverluste hinzu (höher bei Produkten außerhalb der Saison)."
      },
      {
        "q": "Berücksichtigt es Feiertage nach Region?",
        "a": "Ja. Gastro Calendar plant wichtige Feiertage nach Land und Region: Ostern, Weihnachten, Muttertag, Valentinstag, lokale Feste (San Fermín, Fallas, usw.)."
      },
      {
        "q": "Erstellt es saisonale visuelle Inhalte?",
        "a": "Ja. GastroIMG Gen+ + Pinterest Pins Gen erstellen Referenzbilder und Pins, um saisonalen organischen Traffic zu gewinnen. Denken Sie daran: Das KI-Bild ist nur eine visuelle Referenz – das endgültige Foto machen Sie mit Ihrem echten Gericht."
      },
      {
        "q": "Wie hilft es mir beim Storytelling der Erzeuger?",
        "a": "Kreativküche denkt in lokalen Produktkategorien: Viehzüchter einheimischer Rassen, Bio-Landwirt, handwerklicher Fischer, lokaler Bäcker. Jedes Gericht enthält professionelles Storytelling für Service und Kommunikation."
      }
    ],
    "ctaTitle": "Ihre Saisonkarte mit lokalen Produkten und realer Marge.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliederplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "Saisonkarte mit KI entwerfen: Lokale Produkte, Kalkulation und Storytelling | AI Chef Pro",
      "description": "KI-Suite für Saisonkarten: Gastro Calendar, lokale Produkte, Kalkulation und Erzeuger-Storytelling. Starten Sie noch heute.",
      "keywords": "Saisonkarte KI, saisonale Speisekarte, lokale Produkte Restaurant, Gastro Calendar, Herbst-Frühling-Karte KI",
      "ogImage": "https://aichef.pro/og/use-cases/task-carta-estacional-con-ia.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihr Restaurant zugeschnitten",
    "personalizationBody": "AI Chef Pro beginnt mit „Wer sind Sie?“: Sie geben Restauranttyp, Hemisphäre, Region und Schwerpunkt an (kurze Wege, lokale Produkte, Autorenküche). Jeder Agent antwortet auf Ihre tatsächliche Marktsituation zugeschnitten.",
    "appsTitle": "Die KI-Agenten, die Sie für die Saisonkarte verwenden",
    "apps": [
      {
        "name": "Gastro Calendar",
        "category": "Inhalte & Social Media",
        "description": "Saisonale Planung nach Hemisphäre und Region."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Signature-Gerichte mit saisonalen lokalen Produkten."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Desserts mit saisonalen Früchten und Produkten."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Kulinarische Kreativität",
        "description": "Saisongemüse mit fortgeschrittenen Techniken."
      },
      {
        "name": "Food Pairing AI",
        "category": "Kulinarische Kreativität",
        "description": "Pairings, die auf saisonale Produkte abgestimmt sind."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Geschäftskonzepte",
        "description": "Saisonale Weine für Ihre Karte."
      },
      {
        "name": "Sosa Ingredients AI",
        "category": "Gastro-Lieferanten",
        "description": "Sosa-Katalog zur Ergänzung lokaler Produkte."
      },
      {
        "name": "Lebensmittelabfälle AI",
        "category": "Tools & Dienstprogramme",
        "description": "Saisonale Lebensmittelverluste, in die Kalkulation integriert."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools & Dienstprogramme",
        "description": "Skalierung für private Saisonveranstaltungen."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Referenz-KI-Fotografie für Saison."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Inhalte & Social Media",
        "description": "Pinterest gewinnt saisonalen organischen Traffic."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Inhalte & Social Media",
        "description": "SEO-Artikel über saisonale lokale Produkte."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "Geschwindigkeit im Vergleich zum manuellen Prozess"
      },
      {
        "value": "+6 pp",
        "label": "Marge nach Kalkulation der Karte"
      },
      {
        "value": "×2",
        "label": "saisonaler organischer Traffic"
      },
      {
        "value": "12+",
        "label": "Agenten für die Saisonkarte"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Eine Woche Iterationen pro neuer Karte",
        "Produkte außerhalb der Saison mit hohen Kosten",
        "Kein Storytelling lokaler Erzeuger",
        "Reaktive Feiertage ohne Planung",
        "Keine visuellen Inhalte für saisonale Akquise"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "Saisonkarte an einem Tag abgeschlossen",
        "Saisonale lokale Produkte mit optimierten Kosten",
        "Professionelles Erzeuger-Storytelling",
        "Feiertage vorausschauend mit 8 Wochen Vorlauf geplant",
        "GastroIMG Gen+ + Pinterest gewinnen saisonalen Traffic"
      ]
    },
    "galleryTitle": "So funktioniert die Gestaltung der Saisonkarte mit KI",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Herbst- und Frühlingsprodukte, Kalender, Verkostung und Team. KI-generierte Bilder als visuelle Referenz zum Konzept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-otono.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-primavera.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-calendar.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-team.jpg"
    ]
  },
  "task-foto-gastronomica-con-ia": {
    "h1": "Foodfotografie mit KI",
    "heroSubtitle": "Generieren Sie professionelle Referenzbilder des Gerichts, bevor Sie kochen, um Anrichtung, Palette und Komposition zu validieren. Danach machen Sie das endgültige Foto des echten Gerichts mit klarer Zielvorstellung.",
    "heroTagline": "Erst das Referenzbild, dann das endgültige Foto",
    "badge": "Aufgabe: Foodfotografie",
    "painsTitle": "Was traditionelle Foodfotografie kostet",
    "pains": [
      "Food-Styling-Sessions ohne klares Referenzbild, teure Iterationen",
      "Kein gemeinsamer Standard zwischen Koch, Fotograf und Stylist bei Komposition und Palette",
      "Frische Produkte verlieren während der Session an Qualität, das Foto erfasst nicht den optimalen Moment",
      "Kartenänderungen erfordern eine neue, teure Session",
      "Bilder für Instagram, Glovo, Web und Speisekarte erfordern unterschiedliche Formate",
      "Industrielles vs. künstlerisches Bild: inkonsistenter Standard zwischen den Kanälen"
    ],
    "featuresTitle": "So löst AI Chef Pro die Foodfotografie",
    "features": [
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Spezialisierter Agent für KI-Foodfotografie: generiert professionelle Referenzbilder des Gerichts."
      },
      {
        "icon": "Sparkles",
        "title": "Kreativküche mit Anrichtung",
        "description": "Jedes Rezept liefert professionelle Anrichte-Anweisungen: Komposition, Palette, Garnitur, Geschirr, Perspektive (Draufsicht, 3/4, frontal)."
      },
      {
        "icon": "BookOpen",
        "title": "Bild als Referenz, nicht als Endfoto",
        "description": "Das KI-Bild ist die visuelle Orientierung: Farbkontrast, Volumen, Textur, Geschirr. Das endgültige Foto für die Kalkulation machen Sie selbst mit Ihrem echten Gericht."
      },
      {
        "icon": "Calendar",
        "title": "Pinterest Pins Gen",
        "description": "Pinterest liefert stabilen organischen Traffic für Foodfotografie."
      },
      {
        "icon": "Sparkles",
        "title": "InstaFlow AI Pro",
        "description": "Instagram mit Redaktionskalender und auf den Feed abgestimmten Kompositionen."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Bilder für Glovo, Uber Eats, Just Eat und Plattformen mit professionellem Anspruch für mehr Klicks."
      },
      {
        "icon": "CheckSquare",
        "title": "Pro Prompts eBook",
        "description": "300+ professionelle Prompts für Foodfotografie: Stil, Palette, Komposition, Stimmung."
      },
      {
        "icon": "Image",
        "title": "Varianten und Vorbereitungen",
        "description": "GastroIMG generiert Bilder von Varianten: alternative Anrichtungen, Vorbereitungen, Mise en Place, nicht nur das Endgericht."
      },
      {
        "icon": "BookOpen",
        "title": "BlogPost SEO Gen+",
        "description": "SEO-Artikel über Fototechnik mit Referenzbildern für organischen Traffic."
      }
    ],
    "workflowTitle": "Foodfotografie in 4 Schritten",
    "workflow": [
      "1. Kreativküche – Sie entwickeln das Gericht. Der KI-Agent liefert Rezept + Kalkulation + professionelle Anrichte-Anweisungen (Komposition, Palette, Geschirr, Perspektive).",
      "2. GastroIMG Gen+ – Sie generieren ein professionelles Referenzbild mit optimiertem Prompt: warme Palette, rustikales Geschirr, Draufsicht, Microgreens. Sie iterieren, bis das Zielbild klar ist.",
      "3. Sie kochen das echte Gericht mit dem Referenzbild vor Augen: gleiche Anrichtung, Palette, Garnitur. Das endgültige Foto für Kalkulation und Speisekarte machen Sie selbst mit Ihrem echten angerichteten Gericht.",
      "4. InstaFlow AI Pro + MenuDish + Pinterest Pins Gen – Sie passen das endgültige Bild an jeden Kanal an (Instagram, Glovo, Web, Speisekarte) mit professionellem Anspruch."
    ],
    "productsTitle": "Vorlagen und Kits für Foodfotografie",
    "productIds": [
      "pro-prompts-ebook",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-tareas",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "GastroIMG Gen+ hat meinen Fotografie-Workflow komplett verändert. Früher machte ich Food-Styling-Sessions ohne klare Referenz, jetzt generiere ich das professionelle Referenzbild mit KI, validiere Palette und Komposition mit dem Team und mache dann das endgültige Foto mit meinem echten Gericht. Die Sessions dauern 70 % weniger Zeit und die visuelle Konsistenz auf Instagram + Glovo + Web ist jetzt professionell.",
    "testimonialAuthor": "Carmen Vera",
    "testimonialRole": "Köchin und Inhaberin, Restaurant mit starker digitaler Präsenz",
    "faqTitle": "Häufige Fragen zur Foodfotografie mit KI",
    "faqs": [
      {
        "q": "Ist das KI-Bild das endgültige Foto des Gerichts?",
        "a": "Nein. Das KI-Bild dient als visuelle Referenz, um Anrichtung, Palette, Geschirr und Komposition vor dem Kochen zu validieren. Das endgültige Foto für Kalkulation, Speisekarte oder Rezeptblatt machen Sie selbst mit Ihrem echten angerichteten Gericht."
      },
      {
        "q": "Funktioniert das für jeden Kochstil?",
        "a": "Ja. GastroIMG Gen+ passt den Stil an: Fine Dining mit Minimalismus, Casual mit Wärme, mediterran, asiatisch, lateinamerikanisch, Premium-Fine-Dining."
      },
      {
        "q": "Deckt es Formate für Instagram, Glovo, Web und Speisekarte ab?",
        "a": "Ja. Das Basisbild wird auf 1:1 (Instagram), 4:5 (Feed), 16:9 (digitale Speisekarte), 9:16 (Stories), 4:3 (Glovo, Uber Eats) mit professionellem Anspruch angepasst."
      },
      {
        "q": "Generiert es Varianten und Vorbereitungen, nicht nur das Endgericht?",
        "a": "Ja. GastroIMG Gen+ generiert Bilder von Varianten: alternative Anrichtungen, Mise en Place, Vorbereitungen, rohe Zutaten, nicht nur das Endgericht. Ideal für Prozess-Storytelling."
      },
      {
        "q": "Wie hilft es mir bei lokaler Kundenakquise im Delivery?",
        "a": "MenuDish Local SEO + GastroIMG Gen+ generieren professionelle Bilder für Glovo, Uber Eats, Just Eat mit einem Anspruch, der die CTR erhöht. Besseres Foto = mehr Klicks und besseres Ranking."
      }
    ],
    "ctaTitle": "Ihre Foodfotografie mit professionellem Anspruch.",
    "ctaSubtitle": "Starten Sie mit dem 2-minütigen Onboarding. Mitgliedsplan für 10 € pro Monat mit 10.000 Credits.",
    "seo": {
      "title": "Foodfotografie mit KI: Referenzbild und Endfoto | AI Chef Pro",
      "description": "KI-Suite für Foodfotografie: GastroIMG Gen+ generiert das Referenzbild, danach machen Sie das endgültige Foto mit Ihrem echten Gericht. Starten Sie heute.",
      "keywords": "Foodfotografie KI, GastroIMG Gen+, Food Photography KI, Referenzbild Gericht, Gerichtsfoto Delivery",
      "ogImage": "https://aichef.pro/og/use-cases/task-foto-gastronomica-con-ia.jpg"
    },
    "personalizationTitle": "Von der ersten Minute an auf Ihren Stil personalisiert",
    "personalizationBody": "AI Chef Pro startet mit „Wer sind Sie?“: Sie beschreiben Kochstil, Markenpalette, Geschirr und bevorzugte Kanäle (Instagram, Glovo, Web, Speisekarte). GastroIMG Gen+ passt den visuellen Stil an Ihre Marke an.",
    "appsTitle": "Die KI-Agenten für Foodfotografie",
    "apps": [
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-Wissen",
        "description": "Spezialisierter Agent für KI-Foodfotografie."
      },
      {
        "name": "Kreativküche",
        "category": "Kulinarische Kreativität",
        "description": "Professionelle Anrichte-Anweisungen für jedes Rezept."
      },
      {
        "name": "Kreative Patisserie",
        "category": "Kulinarische Kreativität",
        "description": "Dessert-Anrichtung mit französischer Technik."
      },
      {
        "name": "Kreative Gelateria",
        "category": "Kulinarische Kreativität",
        "description": "Anrichtung von Eis und Halbgefrorenem mit Technik."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Content & Social Media",
        "description": "300+ professionelle Prompts für Foodfotografie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content & Social Media",
        "description": "Instagram mit Redaktionskalender und angepassten Formaten."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content & Social Media",
        "description": "Optimierte Bilder für Glovo, Uber Eats, Just Eat."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content & Social Media",
        "description": "Pinterest liefert stabilen organischen Traffic."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content & Social Media",
        "description": "SEO-Artikel mit Referenzbildern."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content & Social Media",
        "description": "Planung von Sessions nach Saison."
      },
      {
        "name": "Sonar Deep Research",
        "category": "KI-Modelle + LLM",
        "description": "Research zu visuellen Trends von Referenzmarken."
      },
      {
        "name": "Mental Coach",
        "category": "Tools & Utilities",
        "description": "Coaching für kreative Führung."
      }
    ],
    "metrics": [
      {
        "value": "−70 %",
        "label": "Zeit für Food-Styling-Sessions"
      },
      {
        "value": "×3",
        "label": "Instagram-Engagement mit GastroIMG"
      },
      {
        "value": "+CTR",
        "label": "Besseres Foto = mehr Klicks im Delivery"
      },
      {
        "value": "12+",
        "label": "Agenten für Foodfotografie"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Ohne AI Chef Pro",
      "beforeItems": [
        "Food-Styling-Sessions ohne klares Referenzbild",
        "Kein gemeinsamer Standard zwischen Koch und Fotograf",
        "Kartenänderungen erfordern eine neue komplette Session",
        "Inkonsistentes Bild zwischen Instagram, Glovo und Web",
        "Keine Varianten oder Vorbereitungen für Storytelling"
      ],
      "afterTitle": "Mit AI Chef Pro",
      "afterItems": [
        "GastroIMG Gen+ generiert professionelles Referenzbild",
        "Gemeinsamer Standard, vor dem Kochen validiert",
        "Kartenänderungen: neues KI-Bild in Minuten",
        "Konsistentes Bild über alle Kanäle",
        "Varianten und Vorbereitungen für vollständiges Storytelling"
      ]
    },
    "galleryTitle": "So funktioniert Foodfotografie mit KI",
    "gallerySubtitle": "Was Sie mit AI Chef Pro koordinieren: Hero, Gericht, Kamera, Werkzeuge und Team. KI-generierte Bilder als visuelle Referenz des Konzepts.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-plato.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-camera.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-tools.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-comparison.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-team.jpg"
    ]
  }
};
