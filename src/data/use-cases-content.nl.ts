// Neerlandés content for use-case spokes.
// Each entry mirrors the structure of USE_CASES_CONTENT_ES.
// Missing entries fall back to ES at runtime via makeContent() in use-cases.ts.
//
// Generado el 2026-08-15 con scripts/astro-migration/fase10-traducir-spokes.py
// (bridge.py ~deepseek/deepseek-v4-flash-latest, --strict-lang) y el glosario
// de la PLATAFORMA viva fase10-glosario-nl.json. Los agentes sin versión
// nl se preservan verbatim a propósito (decisión de catálogo pendiente,
// ver CATALOGO_ITALIANO_PENDIENTE.md — aplica a los 5 idiomas).
//
// NO editar a mano campo a campo: productIds, galleryImages, features[].icon,
// seo.ogImage y testimonialAuthor se preservan verbatim desde el ES y el
// validador del script lo comprueba. Regenerar PISA ediciones manuales.

import type { UseCaseContent } from './use-cases';

export const USE_CASES_CONTENT_NL: Record<string, UseCaseContent> = {
  "propietario-restaurante": {
    "h1": "AI voor Restaurant Eigenaren",
    "heroSubtitle": "Neem betere beslissingen, win administratieve uren terug en verhoog de winstgevendheid van uw restaurant met een suite van AI-agenten gespecialiseerd in horeca.",
    "heroTagline": "Uw digitale partner om het bedrijf met data te runnen",
    "badge": "Voor restauranteigenaren en -houders",
    "painsTitle": "Wat een Restaurant Eigenaar Niet Kan Nalaten op te Lossen",
    "pains": [
      "Krappe marge: het is moeilijk te weten welke gerechten renderen en welke winstgevendheid verliezen zonder nauwkeurige analyse",
      "Weinig tijd om kosten, foodcost, leveranciers en communicatie met het team te beoordelen",
      "Menu-, prijs- en promotiebeslissingen meer op intuïtie dan op data gebaseerd",
      "Roterende teams: trainen, superviseren en roosters beheren kost elke week uren",
      "Financiële rapportage aan de beheerder of investeerders die schone en geconsolideerde documenten vereist",
      "Constante marketing en communicatie (sociale media, web, e-mail) die afleiden van het bedrijf zelf"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Eigenaar Helpt",
    "features": [
      {
        "icon": "BriefcaseBusiness",
        "title": "Pro Restaurant Manager",
        "description": "Gespecialiseerde agent om de eigenaar te ondersteunen bij dagelijkse operaties, teambeslissingen en rapportage aan de investeerder."
      },
      {
        "icon": "FileText",
        "title": "Professioneel financieel plan",
        "description": "Kit Plan Financiero: cashflow, break-evenpunt, maandelijkse P&L en ratio-dashboard. Sjablonen klaar voor investeerders en banken."
      },
      {
        "icon": "Calculator",
        "title": "Professionele foodcost",
        "description": "Creatieve Keuken levert recept + initiële foodcost CSV met referentieprijzen; het Kit de Escandallos Pro beheert dit met uw werkelijke prijzen."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP en voedselveiligheid",
        "description": "Pack APPCC met 19 registraties klaar voor inspectie, registraties vanaf mobiel en afdrukklare A4-bladen."
      },
      {
        "icon": "Users",
        "title": "Personeels- en roosterbeheer",
        "description": "Kit Gestión de Personal: roosters, urenregistratie, productiviteitsratio's en onboarding van nieuwe medewerkers."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Lokale SEO + BlogPost SEO Gen+",
        "description": "Marketing- en lokale SEO-suite: gerechtbeschrijvingen, blog en campagnes met AI om organisch verkeer aan te trekken."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Onderzoek naar lokale gastronomische zoekwoorden om uw restaurant in Google te positioneren zonder een bureau te betalen."
      },
      {
        "icon": "BarChart3",
        "title": "Personeelsmaaltijden",
        "description": "Generator voor personeelsmenu's die kosten bespaart terwijl het keuken- en zaalteam gemotiveerd blijft."
      },
      {
        "icon": "MessageSquare",
        "title": "Mentale Coach",
        "description": "Psychologische coaching voor horecaondernemers: stressbeheer, werk-privébalans en teamleiding in sectoren met hoge druk."
      }
    ],
    "workflowTitle": "Een Echte Dag van een Eigenaar met AI Chef Pro",
    "workflow": [
      "08:30 · Koffie en dashboard — u opent het Kit Plan Financiero en bekijkt de ratio's van de vorige dag. U detecteert dat de foodcost is gestegen naar 33 % door verliezen bij vis.",
      "09:30 · Pro Restaurant Manager — u vraagt de agent om een oorzaakanalyse en krijgt 3 concrete acties voor deze week.",
      "10:30 · MenuDish Lokale SEO — u actualiseert de beschrijving van de 4 topgerechten in Google Business en op de website met zoekwoorden die Keyword Discovery AI+ heeft gedetecteerd.",
      "12:30 · Middagdienst — u superviseert de zaal ondersteund door de checklist van het Kit de Tareas Restaurante Casual.",
      "15:30 · Overleg met beheerder — u exporteert maandelijkse P&L, ratio-dashboard en personeelsrooster als PDF rechtstreeks uit het Kit Plan Financiero. Overleg afgerond in 30 minuten.",
      "17:00 · Creatieve Keuken — u vraagt ideeën voor het komende seizoensmenu. De agent levert 8 gerechten met recept en foodcost CSV.",
      "18:30 · Team beslissing — u gebruikt Mentale Coach om het moeilijke gesprek met een sleutelmedewerker voor te bereiden. U gaat met structuur en argumenten naar het overleg.",
      "21:00 · Afsluiting — de manager stuurt u het automatische dagrapport via WhatsApp. U gaat naar huis zonder openstaand papierwerk."
    ],
    "productsTitle": "Downloadbare Sjablonen en Kits voor Eigenaren",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Vroeger besteedde ik 6 uur per week alleen aan het kloppend maken van cijfers tussen Excel en servetten. Met AI Chef Pro sluit ik het af in een uur met professionele dashboards. Ik heb de financiële controle over mijn twee zaken terug en de marge steeg 3 punten in het eerste kwartaal.",
    "testimonialAuthor": "Carlos Méndez",
    "testimonialRole": "Eigenaar, groep mediterrane bistro's (2 zaken)",
    "faqTitle": "Veelgestelde Vragen van Eigenaren",
    "faqs": [
      {
        "q": "Welke restaurantgrootte past bij AI Chef Pro?",
        "a": "Van een enkel familiebedrijf tot groepen met meer dan 10 restaurants. De sjablonen schalen mee met het volume en de abonnementen passen zich aan het werkelijke gebruik aan. Er zijn klanten met 1 zaak en anderen met 25 actieve units."
      },
      {
        "q": "Heb ik technische kennis nodig?",
        "a": "Nee. Als u WhatsApp en Excel op basisniveau kunt gebruiken, kunt u ook AI Chef Pro gebruiken. De onboarding begint met de agent «Wie Ben Ik?», die in 2 minuten het systeem aanpast aan u, uw bedrijf en uw geografische regio. Er zijn korte onboardingvideo's en directe ondersteuning via WhatsApp."
      },
      {
        "q": "Vervangt het mijn beheerder of adviseur?",
        "a": "Nee, maar het maakt hun leven veel gemakkelijker. Uw beheerder ontvangt schone documenten en u komt met geconsolideerde data naar overleggen. De meeste administratiekantoren raden AI Chef Pro uiteindelijk aan bij andere klanten."
      },
      {
        "q": "Hoe snel zie ik resultaten?",
        "a": "De meeste eigenaren melden tussen 4 en 6 uur per week teruggewonnen in de eerste week van gebruik. De impact op de marge ligt meestal tussen 2 en 5 procentpunten in 60-90 dagen, dankzij het herontwerpen van gerechten met hoge foodcost en het beheersen van verliezen."
      },
      {
        "q": "Hoe helpt het mij met marketing en lokale SEO?",
        "a": "De suite Content en Social Media omvat MenuDish Lokale SEO (geoptimaliseerde gerechtbeschrijvingen), BlogPost SEO Gen+ (posts om organisch verkeer aan te trekken) en Keyword Discovery AI+ (lokale gastronomische zoekwoorden). U verlaagt uitgaven aan marketingbureaus en trekt directe reserveringen aan."
      },
      {
        "q": "Zijn er kortingen voor groepen met meerdere zaken?",
        "a": "Ja. Vanaf 5 actieve units zijn er bedrijfsabonnementen met gepersonaliseerde onboarding en geconsolideerde dashboards per groep."
      }
    ],
    "ctaTitle": "Beheer uw restaurant met data, niet met intuïtie.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor 10 € per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Restaurant Eigenaren: Financieel Plan, Foodcost, SEO | AI Chef Pro",
      "description": "AI-suite voor restauranteigenaren: gespecialiseerde agenten, financieel plan, professionele foodcost, HACCP, marketing en lokale SEO. Start vandaag.",
      "keywords": "AI restauranteigenaar, restaurant eigenaar AI, software restaurantbeheer eigenaren, financieel plan restaurant AI, foodcost restaurant, marketing restaurant AI, lokale SEO restaurant, AI-agent horeca, restauranteigenaar Nederland",
      "ogImage": "https://aichef.pro/og/use-cases/propietario-restaurante.jpg"
    },
    "personalizationTitle": "Vanaf Minuut Eén Afgestemd op Uw Bedrijf",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor restaurant u heeft, in welke stad, hoeveel zaken, welk gemiddeld ticket u hanteert en hoe u werkt. Vanaf dat moment reageert elke agent — van het Financieel Plan tot lokale SEO — afgestemd op uw context: marktprijzen in uw regio, wetgeving van uw land en de werkelijke schaal van uw operatie. Het is geen formulier: het is een kort gesprek dat elk hulpmiddel echt nuttig maakt voor uw bedrijf.",
    "appsTitle": "De AI-agenten die u als Eigenaar Zult Gebruiken",
    "apps": [
      {
        "name": "Pro Restaurant Manager",
        "category": "Gastro Profile Pro",
        "description": "Operationele en financiële assistent om u te ondersteunen bij teambeslissingen, rapportage en dagelijkse operaties."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Specialist in bistro's, gastrobars, tapas en mediterraan: het complete casual spectrum met professionele basis."
      },
      {
        "name": "MenuDish Lokale SEO",
        "category": "Content en Social Media",
        "description": "Gerechtbeschrijvingen geoptimaliseerd voor lokale SEO in Google Business en op de website."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "Blogposts die lokaal organisch verkeer naar uw restaurant trekken."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Content en Social Media",
        "description": "Onderzoek naar lokale gastronomische zoekwoorden per postcodegebied."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Professionele gerechtontwikkeling met recept + initiële foodcost CSV (referentieprijzen) klaar voor het Kit de Escandallos Pro."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Nauwkeurige gegevens over verliezen en opbrengsten per ingrediënt, essentieel voor realistische foodcost."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per recept en gerecht, klaar voor regelgeving."
      },
      {
        "name": "Personeelsmaaltijden",
        "category": "Gastro Profile Pro",
        "description": "Generator voor personeelsmenu's die kosten bespaart terwijl het team gemotiveerd blijft."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en Utilities",
        "description": "Psychologische coaching voor horecaondernemers: stress, teams en moeilijke beslissingen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Gastronomische kalender met belangrijke data, ideeën en hashtags voor sociale media en blog."
      },
      {
        "name": "InstaFlow AI Pro + Pinterest Pins Gen",
        "category": "Content en Social Media",
        "description": "Viral content voor Instagram en Pinterest zonder bureau."
      }
    ],
    "metrics": [
      {
        "value": "+3 pp",
        "label": "marge in 60-90 dagen"
      },
      {
        "value": "−6 u",
        "label": "wekelijks aan beheer"
      },
      {
        "value": "×2",
        "label": "directe reserveringen via lokale SEO"
      },
      {
        "value": "12+",
        "label": "AI-agenten voor uw rol"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "6 uur per week Excel, servetten en leveranciersnotities kloppend maken",
        "Menu- en prijsbeslissingen op intuïtie, niet op analyse van werkelijke foodcost",
        "Rapportage aan de beheerder met verspreide bestanden in Word, Excel en e-mail",
        "Geïmproviseerde of uitbestede marketing tegen hoge prijzen zonder te weten wat werkt",
        "Constante stress en dip in feestdagen omdat u de controle niet loslaat"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "1 uur per week om professionele dashboards met duidelijke KPI's af te sluiten",
        "Menu- en prijsbeslissingen met professionele foodcost en margeanalyse",
        "Rapportage aan de beheerder in PDF rechtstreeks vanuit het Kit Plan Financiero",
        "Geautomatiseerde lokale SEO en AI-marketing suite die uitgaven aan bureaus verlaagt",
        "Gemoedsrust: het team stuurt u automatische rapporten via WhatsApp"
      ]
    },
    "galleryTitle": "De Dagelijkse Praktijk van een Eigenaar, in Beeld",
    "gallerySubtitle": "Wat u met AI Chef Pro kunt beheren: financiële dashboards, operationele beslissingen, team, zaal en reporting.",
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
    "h1": "AI voor Restaurantmanagers en -leidinggevenden",
    "heroSubtitle": "Optimaliseer uw dagelijkse operaties, beheers uw kosten en win uren administratief werk terug met een suite van AI-agenten die zijn ontworpen voor de dagelijkse praktijk van de restaurantmanager.",
    "heroTagline": "Meer operationele controle, minder losse papieren",
    "badge": "Voor managers en leidinggevenden",
    "painsTitle": "Wat een Restaurantmanager Niet Kan Laten Liggen",
    "pains": [
      "Elke week roosters opstellen met inachtneming van de cao, wettelijke arbeidstijd en rusttijden, zonder fouten of meerkosten",
      "Verlies, voorraad en inkoop beheersen bij verschillende leveranciers die elke week van prijs veranderen",
      "HACCP up-to-date houden en inspecties voorbereiden zonder stress of papierwerkstapels",
      "Rapporteren aan de eigenaar met geconsolideerde data en professionele dashboards, niet in geïmproviseerde Excel-bestanden",
      "Het keuken- en bedieningsteam coördineren met duidelijke communicatie en snelle inwerking van nieuw personeel",
      "De operatie tijdens servicepieken managen zonder kwaliteitsverlies en zonder de bediening te verwaarlozen"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Manager Helpt",
    "features": [
      {
        "icon": "BriefcaseBusiness",
        "title": "Pro Restaurant Manager",
        "description": "Gespecialiseerde agent om u te ondersteunen bij operationele beslissingen, teammanagement en rapportage aan de eigenaar."
      },
      {
        "icon": "Calendar",
        "title": "Roosters en controle op diensten",
        "description": "Kit Gestión de Personal: roosters in minuten met inachtneming van de cao, urenregistratie, productiviteitsratio's."
      },
      {
        "icon": "Package",
        "title": "Voorraad en inkoopbeheer",
        "description": "Kit Inventario: kant-en-klare Excel-sjablonen, meldingen bij minimale voorraad, leveranciersvergelijking en verlies."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP en traceerbaarheid",
        "description": "Pack APPCC met 17 registers, temperatuuralerts via mobiel en export die klaar is voor inspectie."
      },
      {
        "icon": "BarChart3",
        "title": "KPI's en rapportage aan de eigenaar",
        "description": "Ratio's voor keuken en bediening, productiviteit, gemiddelde besteding. Dashboards die direct vanuit Excel naar PDF kunnen worden geëxporteerd."
      },
      {
        "icon": "CheckSquare",
        "title": "Terugkerende taken per dienst",
        "description": "Kant-en-klare sjablonen per concept: opening, sluiting, mise-en-place en service in één kit per type bedrijf."
      },
      {
        "icon": "Users",
        "title": "Personeelsmaaltijden",
        "description": "Generator voor personeelsmenu's die kosten bespaart en het team gemotiveerd en goed gevoed houdt."
      },
      {
        "icon": "MessageSquare",
        "title": "Mentale Coach",
        "description": "Psychologische coaching voor het omgaan met moeilijke gesprekken, stress en teammotivatie."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergenen ID",
        "description": "Automatische identificatie van allergenen per gerecht, klaar voor de regelgeving en voor de bediening."
      }
    ],
    "workflowTitle": "Een Echte Dag van een Manager met AI Chef Pro",
    "workflow": [
      "08:30 · Opening — u print de checklist voor de dienst vanuit de Kit de Tareas en controleert in 10 minuten de voorraad.",
      "09:30 · Pro Restaurant Manager — de agent vat de incidenten van de vorige dag en de openstaande acties voor u samen.",
      "10:30 · Kit Inventario — u valideert bestellingen bij leveranciers met een prijsvergelijking en meldingen bij minimale voorraad.",
      "12:30 · Middagservice — het team registreert verlies en temperaturen via de mobiele telefoon met de Pack APPCC.",
      "15:30 · Rooster voor volgende week — u opent de Kit Gestión de Personal en sluit het rooster in 20 minuten af met inachtneming van de cao.",
      "17:00 · Personeelsmaaltijden — u genereert het personeelsmenu voor de komende week met ingrediënten die u al op voorraad heeft.",
      "19:00 · Moeilijk gesprek — u gebruikt Mentale Coach om het gesprek voor te bereiden met een kok die herhaaldelijk te laat komt.",
      "23:30 · Sluiting — u genereert het dagelijkse rapport met ratio's en stuurt het met één tik naar de eigenaar via WhatsApp."
    ],
    "productsTitle": "Downloadbare Sjablonen en Kits voor Managers",
    "productIds": [
      "kit-gestion-personal",
      "kit-inventario",
      "pack-appcc",
      "kit-tareas",
      "kit-escandallos",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Vroeger was ik 8 uur per week bezig met het opstellen van roosters en bestellingen bij leveranciers. Nu doe ik dat in 2 uur met de Kit Gestión de Personal en de Kit Inventario. AI Chef Pro heeft me tijd teruggegeven om in de zaal met het team te zijn, waar een manager hoort te zijn.",
    "testimonialAuthor": "Marta Ruiz",
    "testimonialRole": "Manager, casual restaurant met 80 zitplaatsen",
    "faqTitle": "Veelgestelde Vragen van Managers",
    "faqs": [
      {
        "q": "Werkt het als u 1 locatie beheert of meerdere?",
        "a": "In beide gevallen. De sjablonen schalen mee met het volume en u kunt de rapportage van meerdere locaties consolideren in één dashboard. Er zijn klanten met 1 locatie en anderen met meer dan 10 actieve eenheden."
      },
      {
        "q": "Vervangt het de reserveringssoftware of de kassa?",
        "a": "Nee, het vult aan. Cover Manager of The Fork beheren reserveringen en de kassa beheert verkopen; AI Chef Pro beheert kosten, personeel, HACCP, voorraad en interne operatie. De gegevens zijn perfect compatibel via Excel."
      },
      {
        "q": "Heeft het team training nodig?",
        "a": "Minimaal. De sjablonen en de agenten zijn in het Spaans en alles start met de agent «Wie Ben Ik?», die het systeem in 2 minuten aan u aanpast. De echte leercurve voor het team is 1-2 dagen met de video-introductie en ondersteuning via WhatsApp."
      },
      {
        "q": "Kan ik de gegevens exporteren voor mijn boekhouder of de eigenaar?",
        "a": "Ja. Alles wordt geëxporteerd naar Excel en PDF in professioneel formaat. Boekhoudkantoren ontvangen nette documentatie en eigenaren ontvangen dashboards met duidelijke KPI's rechtstreeks via WhatsApp."
      },
      {
        "q": "Hoe helpt het mij bij moeilijke gesprekken met het team?",
        "a": "Mentale Coach is een agent voor psychologische coaching voor horecaondernemers die u helpt moeilijke gesprekken te structureren (ontslagen, te laat komen, conflicten tussen keuken en bediening) met argumenten en een duidelijke structuur vóór het gesprek."
      },
      {
        "q": "Zijn er specifieke sjablonen per bedrijfsconcept?",
        "a": "Ja. Er zijn specifieke Kits de Tareas voor casual dining, cafetaria, pizzeria, hamburgerrestaurant, dark kitchen, banketbakkerij, bar, catering, hotel, ijssalon, chocolaterie, creatief restaurant en privéchef. Elk met sjablonen die zijn afgestemd op de dagelijkse praktijk."
      }
    ],
    "ctaTitle": "Breng de operatie van uw restaurant naar een hoger niveau.",
    "ctaSubtitle": "Start met de kennismaking van 2 minuten. Lidmaatschapsplan voor 10 € per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Restaurantmanagers: Roosters, HACCP en Rapportage | AI Chef Pro",
      "description": "AI-suite voor restaurantmanagers: roosters, voorraad, HACCP, KPI's en rapportage aan de eigenaar met gespecialiseerde agenten voor de horeca. Begin vandaag.",
      "keywords": "AI restaurantmanager, restaurantmanager AI, software restaurantmanager, operationeel restaurantbeheer AI, roosters restaurant, HACCP manager, KPI's restaurant, AI-agent horeca, restaurantmanager Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/gerente-restaurante.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor Uw Restaurant vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een interactieve kennismaking van 2 minuten waarin u vertelt welk type restaurant u beheert, in welke stad, hoeveel gasten u bedient en hoe u werkt. Vanaf dat moment reageert elke agent — van de roosters tot de rapportage — aangepast aan uw context: cao van het land, schaal van uw team, echte servicepieken. Het is geen formulier: het is een kort gesprek dat de suite echt nuttig maakt voor uw dagelijkse werk als manager.",
    "appsTitle": "De AI-agenten die u als Manager zult gebruiken",
    "apps": [
      {
        "name": "Pro Restaurant Manager",
        "category": "Gastro Profile Pro",
        "description": "Hoofdagent: operationele beslissingen, teammanagement en rapportage aan de eigenaar."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Specialist in bistro's, gastrobars, tapas en mediterraan: het complete casual spectrum."
      },
      {
        "name": "Personeelsmaaltijden",
        "category": "Gastro Profile Pro",
        "description": "Generator voor personeelsmenu's die kosten bespaart en het team motiveert."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Nauwkeurige gegevens over verlies en opbrengst per ingrediënt, essentieel voor keukenbeheersing."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per recept en gerecht."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools en Utilities",
        "description": "Omzetter van gewichten en maten voor de professionele keuken."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en Utilities",
        "description": "Portiecalculator die recepten opschaalt naar elk aantal gasten."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en Utilities",
        "description": "Psychologische coaching voor horecaondernemers: stress, moeilijke gesprekken en teammotivatie."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Gerechtbeschrijvingen geoptimaliseerd voor lokale SEO in Google en op de website van het restaurant."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Gastronomische kalender met belangrijke data, ideeën en hashtags voor social media en blog."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van professionele gerechten met recept + CSV-kostprijsberekening om te laden in de Kit de Escandallos Pro."
      }
    ],
    "metrics": [
      {
        "value": "−75 %",
        "label": "tijd aan roosters en bestellingen"
      },
      {
        "value": "×4",
        "label": "snelheid van rapportage aan de eigenaar"
      },
      {
        "value": "−40 %",
        "label": "verlies na systematische controle"
      },
      {
        "value": "11+",
        "label": "AI-agenten voor uw rol"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "8 uur per week roosters opstellen in handmatig Excel en leveranciersnotities",
        "HACCP op uitgeprint papier dat kwijtraakt of onvolledig bij de inspectie aankomt",
        "Rapportage aan de eigenaar in verspreide e-mailbestanden zonder structuur",
        "Verlies op het oog geregistreerd, zonder echte traceerbaarheid of meldingen",
        "Geïmproviseerde personeelsmaaltijden die de kosten opdrijven zonder dat iemand het merkt"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "2 uur per week roosters afsluiten met een professioneel sjabloon met inachtneming van de cao",
        "HACCP via mobiel met registers, temperaturen en meldingen, klaar voor inspectie",
        "Rapportage aan de eigenaar in PDF rechtstreeks vanuit de Kit Plan Financiero, met duidelijke dashboards",
        "Systematische controle van verlies met nauwkeurige gegevens en voorraadmeldingen",
        "Personeelsmaaltijden gegenereerd met AI, met respect voor de doelstelling op kosten en teammotivatie"
      ]
    },
    "galleryTitle": "De Dagelijkse Praktijk van een Manager, in Beeld",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: roosterplanning, aansturing van keuken en bediening, voorraadbeheer, service en rapportage.",
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
    "h1": "AI voor operationeel directeuren van restaurantgroepen",
    "heroSubtitle": "Standaardiseer processen, consolideer rapportages en vermenigvuldig de operationele productiviteit in multi-locatiegroepen met een suite van AI-agenten gespecialiseerd in horeca.",
    "heroTagline": "Dezelfde standaard in alle locaties, geconsolideerde gegevens met één klik",
    "badge": "Voor operationeel directeuren van groepen",
    "painsTitle": "Wat een operationeel directeur van meerdere locaties niet kan negeren",
    "pains": [
      "Dezelfde kwaliteits-, proces- en ervaringsstandaard handhaven in alle locaties van de groep",
      "Financiële, operationele en team-KPI's consolideren om prestaties tussen units te vergelijken",
      "Operationele handleidingen, training en onboarding repliceren zonder kwaliteitsverlies wanneer het netwerk groeit",
      "Tijdig locaties detecteren met afwijkingen in foodcost, personeel of productiviteit voordat ze marge verliezen",
      "Managers van elke locatie coördineren met duidelijke communicatie en consistente rapportage",
      "De groep opschalen door nieuwe units te openen zonder bij elke opening het wiel opnieuw uit te vinden"
    ],
    "featuresTitle": "Hoe AI Chef Pro een operationeel directeur helpt",
    "features": [
      {
        "icon": "Building2",
        "title": "Multi-locatie standaardisatie",
        "description": "Uniforme handleidingen, checklists en procedures die met één klik naar alle units van de groep worden gerepliceerd."
      },
      {
        "icon": "BarChart3",
        "title": "Geconsolideerde dashboards",
        "description": "Kit Plan Financiero: vergelijk foodcost, productiviteit, verliezen en gemiddeld besteedbaar bedrag tussen al uw restaurants in één overzicht."
      },
      {
        "icon": "ChefHat",
        "title": "Executive Chef Pro",
        "description": "Agent die recepten en technische fiches standaardiseert zodat hetzelfde gerecht er hetzelfde uitziet in 1, 5 of 25 keukens."
      },
      {
        "icon": "BriefcaseBusiness",
        "title": "Pro Restaurant Manager",
        "description": "Assistent voor elke lokale manager die naar boven rapporteert met geconsolideerde gegevens aan de operationeel directeur."
      },
      {
        "icon": "BookOpen",
        "title": "Operationele handleidingen met AI",
        "description": "Onboarding, teamtraining en procedures altijd up-to-date vanuit één centrale repository."
      },
      {
        "icon": "ShieldCheck",
        "title": "Uniforme HACCP voor de groep",
        "description": "Eén documentair systeem voor alle units van de groep: gecentraliseerde traceerbaarheid en temperaturen."
      },
      {
        "icon": "TrendingDown",
        "title": "Kostenaudit per locatie",
        "description": "Mermas GenCal en Kit de Escandallos Pro detecteren afwijkingen in foodcost voordat ze uit de hand lopen."
      },
      {
        "icon": "Users",
        "title": "Roosters en teamstructuur",
        "description": "Kit Gestión de Personal: dezelfde structuur van diensten, ratio's en productiviteit in alle units."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Diepgaand onderzoek naar trends, concurrenten en markten voor strategische expansiebeslissingen."
      }
    ],
    "workflowTitle": "Een echte dag van een operationeel directeur met AI Chef Pro",
    "workflow": [
      "08:30 · Koffie en Kit Plan Financiero — u opent het geconsolideerde dashboard van de 7 locaties van de groep en detecteert dat locatie 4 een foodcost van 33% heeft (+3 pp boven doel).",
      "09:30 · Pro Restaurant Manager — u vraagt de agent om een geautomatiseerde analyse van de oorzaak per locatie. Het identificeert een probleem met visverliezen.",
      "10:30 · Videogesprek met de manager van locatie 4, ondersteund door echte gegevens uit het Kit Plan Financiero, niet op intuïtie.",
      "12:00 · Executive Chef Pro — u werkt de procedure voor het hanteren van vis bij en deze wordt gerepliceerd naar de 7 keukens als nieuwe versie van de handleiding.",
      "15:30 · Geconsolideerde roosters — u bekijkt het Kit Gestión de Personal met productiviteitsratio's van alle locaties en ondertekent de onboarding van de nieuwe manager van locatie 8.",
      "17:00 · Sonar Deep Research — u onderzoekt de markt voor de volgende opening in een andere stad: analyse van gebieden, gemiddeld besteedbaar bedrag en concurrentie.",
      "19:00 · Vergadering met het comité — u exporteert de KPI's van het kwartaal naar PDF rechtstreeks vanuit het Kit Plan Financiero. Vergadering afgerond in 45 minuten.",
      "21:30 · Afsluiting — de 7 managers sturen u het automatische dagrapport via WhatsApp. U gaat naar huis met een volledig beeld van de groep."
    ],
    "productsTitle": "Downloadbare sjablonen en kits voor restaurantgroepen",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-tareas"
    ],
    "testimonialQuote": "We beheren 7 locaties en voorheen werkte elke locatie anders: verschillende Excel-bestanden, verschillende handleidingen, verschillende HACCP. Met AI Chef Pro hebben we dezelfde standaard overal en geconsolideerde rapportage in één overzicht. Het detecteren van de locatie met problemen ging van 2 weken naar 1 dag.",
    "testimonialAuthor": "Javier Ortega",
    "testimonialRole": "Operationeel directeur, restaurantgroep met 7 locaties",
    "faqTitle": "Veelgestelde vragen van operationeel directeuren",
    "faqs": [
      {
        "q": "Hoeveel locaties ondersteunt AI Chef Pro?",
        "a": "Geen echte limiet. Er zijn klanten met 1 locatie en anderen met meer dan 25 actieve units. De bedrijfsplannen schalen op basis van gebruik en ontgrendelen geconsolideerde dashboards, gepersonaliseerde onboarding en prioritaire ondersteuning."
      },
      {
        "q": "Integreert het met ons ERP- of boekhoudsysteem?",
        "a": "De sjablonen exporteren naar Excel, PDF en CSV in formaten die compatibel zijn met de meeste ERP- en boekhoudsystemen. Uw financiële team ontvangt documentatie die klaar is voor integratie."
      },
      {
        "q": "Biedt het rollen en rechten per locatie?",
        "a": "Ja. U kunt toegang geven per lokale manager, per regionaal directeur of geconsolideerd aan de operationeel directeur. Elk niveau ziet alleen de gegevens die voor hem of haar relevant zijn."
      },
      {
        "q": "Hoe wordt dezelfde standaard in alle units gegarandeerd?",
        "a": "Executive Chef Pro standaardiseert recepten en technische fiches; het Pack APPCC verenigt traceerbaarheid; het Kit de Escandallos Pro handhaaft dezelfde berekeningen in alle locaties. De handleidingen worden met één klik gerepliceerd en vanuit één punt bijgewerkt."
      },
      {
        "q": "Zijn er kortingen voor groepen met meerdere locaties?",
        "a": "Ja. Vanaf 5 actieve units zijn er bedrijfsplannen met gepersonaliseerde onboarding, geconsolideerde dashboards, training van het centrale team en prioritaire ondersteuning."
      },
      {
        "q": "Is het geschikt om sneller nieuwe locaties te openen?",
        "a": "Ja. Het is een van de meest voorkomende use cases: de gidsen Cómo Montar… (dark kitchen, gastronomisch restaurant, casual, Mexicaans, Japans, Peruaans, nikkei) zijn professionele roadmaps die openingen versnellen met financieel plan, businessplan en repliceerbare handleidingen."
      }
    ],
    "ctaTitle": "Standaardiseer uw groep. Dezelfde standaard in alle locaties.",
    "ctaSubtitle": "Neem contact met ons op voor een gepersonaliseerde onboarding voor uw groep of start met het lidmaatschapsplan: €10 per maand met 10.000 credits.",
    "seo": {
      "title": "AI voor operationeel directeuren van restaurantgroepen | AI Chef Pro",
      "description": "AI-suite voor multi-locatie restaurantgroepen: geconsolideerde dashboards, standaardisatie van recepten, HACCP voor de groep, repliceerbare handleidingen en financieel plan per unit.",
      "keywords": "AI restaurantgroep, software multi-locatie restaurants, operationeel directeur restaurants AI, processen standaardiseren restaurant, geconsolideerde dashboards restaurant, restaurantgroep opschalen, multi-locatie AI horeca",
      "ogImage": "https://aichef.pro/og/use-cases/director-operaciones-grupo.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw groep vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt hoeveel locaties u beheert, welke concepten u exploiteert (casual, gastronomisch, dark kitchen, hotel), in welke landen en hoe uw organisatie werkt. Vanaf dat moment reageert elke agent – van het Plan Financiero tot de operationele handleidingen – afgestemd op de schaal en structuur van de groep. Het is geen formulier: het is een kort gesprek dat de suite echt nuttig maakt voor operationeel directeuren van meerdere locaties.",
    "appsTitle": "De AI-agenten die u als operationeel directeur gaat gebruiken",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standaardisatie van recepten, technische fiches en handleidingen die repliceerbaar zijn naar alle units van de groep."
      },
      {
        "name": "Pro Restaurant Manager",
        "category": "Gastro Profile Pro",
        "description": "Assistent voor elke lokale manager met geconsolideerde rapportage naar boven."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Specialist in bistro's, gastrobars en casual: het meest voorkomende spectrum in multi-locatiegroepen."
      },
      {
        "name": "Burger Pro AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor groepen met gourmetburger- of fast casual-merken."
      },
      {
        "name": "Catering AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor groepen met een catering- en evenementenafdeling."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI-modellen + LLM",
        "description": "Diepgaand onderzoek naar trends, concurrenten en markten voor strategische beslissingen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpprogramma's",
        "description": "Nauwkeurige gegevens over verliezen en opbrengsten per ingrediënt, essentieel voor multi-locatie audits."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpprogramma's",
        "description": "Automatische identificatie van allergenen per recept, uniform in alle units."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en sociale media",
        "description": "Blogposts om organisch verkeer aan te trekken voor elke unit van de groep."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Content en sociale media",
        "description": "Zoekwoordonderzoek per postcodegebied van elke locatie."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-gegenereerde foodfotografie, uniform voor het hele merk van de groep."
      }
    ],
    "metrics": [
      {
        "value": "−14 d",
        "label": "locatie met afwijkingen detecteren"
      },
      {
        "value": "×7",
        "label": "snelheid van geconsolideerde rapportage"
      },
      {
        "value": "+3 pp",
        "label": "marge na standaardisatie"
      },
      {
        "value": "11+",
        "label": "agenten voor multi-locatie"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "7 locaties met 7 verschillende Excel-bestanden, heterogene handleidingen en inconsistente HACCP",
        "Het detecteren van een locatie met afwijkingen duurt 2 weken omdat er geen geconsolideerde rapportage is",
        "Onboarding van een nieuwe manager in 1 maand met geïmproviseerd materiaal van elke unit",
        "Rapportage aan het comité met verspreide bestanden en zonder professionele dashboards",
        "Expansiebeslissingen op basis van intuïtie, zonder diepgaand marktonderzoek"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Dezelfde standaard gerepliceerd in alle 7 units: recepten, handleidingen en HACCP uniform",
        "Locatie met afwijkingen detecteren in 1 dag met geconsolideerd dashboard van het Kit Plan Financiero",
        "Onboarding van een nieuwe manager in 1 week met repliceerbare handleidingen en training",
        "Rapportage aan het comité in PDF rechtstreeks uit het Kit Plan Financiero met geconsolideerde KPI's",
        "Expansiebeslissingen ondersteund door Sonar Deep Research en professionele Cómo Montar…-gidsen"
      ]
    },
    "galleryTitle": "De dagelijkse praktijk van een operationeel directeur, in beeld",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: dashboards voor meerdere locaties, strategievergaderingen, audits van units, bedrijfshandleidingen en onboarding van managers.",
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
    "h1": "AI voor Executive Chef en Corporate Chef",
    "heroSubtitle": "Creeër standaardiseerde recepten, precise escandallos en repliceerbare manuals for 1, 5 oder 25 keukens. Een suite van gastronomische AI-agents designed for een van de me exigeerende rollen in de professioneel keuken.",
    "heroTagline": "Uw creatief en operatief team, gescaleerd op de snelheid van een conversatie",
    "badge": "Voor executive chefs en corporate chefs",
    "painsTitle": "Wat een Executive Chef Niet Kan Laaten Onopgelost",
    "pains": [
      "Recepten standaardisearje in geografisch verspreide keukens, zonder dat elke locatie se op uw eigen wijze interpreteert",
      "Precise escandallos sluiten for elke technische fiche met seizoensproduct waarvan de prijs elke week verandert",
      "De kaart elke 6-12 weken vernieuwen zonder dat het team in papieren ondergaat",
      "Keukenmanuals and onboarding up-to-date houden bij constante personeelrotatie",
      "Seizoenmenu innovieren zonder de doel-food cost oder de echte marge te verliezen",
      "Rapporteren aan de leiding met duidelijke KPIs: rentabiliteit per gerecht, productiviteit van de brigade en mermas"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Executive Chef Helpt",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Executive Chef Pro",
        "description": "AI-agent specialiseerd in de rol: multi-locale standaardisatie, technische fiches, keukenmanuals and kaartbesluiten op basis van echte data."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken + Food Pairing AI",
        "description": "Ideeënstorm for gerechten per seizoen, ingrediente oder techniek, met combinaties ondersteund door wetenschappelijk basis. Creatieve Keuken levert bovendien de gedetailleerde recept and een initiële escandallo met referentie-marktprijzen, downloadbaar as CSV."
      },
      {
        "icon": "Calculator",
        "title": "Professioneel escandallos",
        "description": "U laad de CSV van Creatieve Keuken in de Kit de Escandallos Pro and substitueert de referentieprijzen door die van uw echte leveranciers. Cost per portie, food cost %, marge and suggested prijs instant. Recalculiert automatisch als u een grammage oder een cost verandert."
      },
      {
        "icon": "BookOpen",
        "title": "Professioneel technische fiches",
        "description": "Recept, procedure, allergenen, emplating and storytelling in een enkel document. Klaar om aan alle keukens van de groep te senden."
      },
      {
        "icon": "Layers",
        "title": "Multi-locale standaardisatie",
        "description": "Hetzelfde gerecht, hetzelfde kwaliteit and hetzelfde cost in 1, 5 oder 25 eenheden. Repliceerbare and voll traceerbare manuals."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+ and geavanceerde techniken",
        "description": "Koji, kombuchas, shoyus, garums and lactofermentos: gastronomische I+D met professioneel ondersteuning."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergenen ID and Mermas GenCal",
        "description": "Automatische detectie van allergenen per gerecht and precise data over mermas and rendements per ingrediente."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Diepe gastronomische onderzoek: trends, opkomende techniken, producenten and seizoensproducten."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "AI-generated gastronomische fotografie for technische fiches, interne communicatie and persreleases."
      }
    ],
    "workflowTitle": "Een Echte Dag van een Executive Chef met AI Chef Pro",
    "workflow": [
      "Morgen, 09:00 · Creatieve Keuken — ideeënstorm van 12 gerechten for the herfstmenu op basis van lokale seizoensproduct. De agent levert u een gedetailleerd recept and een initiële escandallo met referentie-marktprijzen, downloadbaar as CSV.",
      "Morgen, 10:30 · Kit de Escandallos Pro — u laad de 12 CSV's van Creatieve Keuken, substitueert de referentieprijzen door die van uw echte leveranciers and discarteert 4 gerechten die niet passen met uw doel-food cost (28 %).",
      "Middag, 12:00 · Food Pairing AI — u werkt aan de pairing van de 8 finalisten and valideert onverwachte harmonien.",
      "Namiddag, 15:00 · Allergenen ID — u genereert de allergenenfiche per gerecht, klaar for regulatie and for de zaal.",
      "Namiddag, 16:30 · Executive Chef Pro — u schrijft de complete technische fiche met procedure, grammages, emplating and storytelling.",
      "Namiddag, 18:00 · GastroIMG Gen+ — u genereert de fotos van elke gerecht for the interne manual and the persrelease.",
      "Namiddag, 18:30 · U repliceert de manual aan de 5 keukens van de groep. Wat een traditioneel process in 15-30 dagen sluit, sluit u in 1-3 werkdagen, afhangig van de grootte van de kaart."
    ],
    "productsTitle": "Downloadbare Sjabloneen en Kits voor Executive Chefs",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-plan-financiero",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Vroeger nam het me tussen 15 en 20 dagen om een nieuwe kaart te sluiten tussen ideeënstorm, tests, escandallos, technische fiches en interne communicatie. Met AI Chef Pro doe ik het in 2 oder 3 dagen, afhangig van de grootte van de kaart en of het totale oder partielle reengineering is. De verschil is niet alleen tijd: de team ontvangt professioneel en repliceerbare documentatie, geen handgeschreven notizen.",
    "testimonialAuthor": "Diego Saavedra",
    "testimonialRole": "Executive Chef, groep van 5 mediterraanse restaurants",
    "faqTitle": "Veelgestelde Vragen van Executive Chefs",
    "faqs": [
      {
        "q": "Verstaan de AI-agents van AI Chef Pro professioneel keuken oder binne se generalistische chatbots?",
        "a": "Se binne specialiseerde agents. Creatieve Keuken, Food Pairing AI, Fermentus Con AI+ and Executive Chef Pro binne getrained met professioneel gastronomische kennis: techniken, echte escandallo, rentabiliteit, grammages and cuts. Se binne geen generisch ChatGPT: se binne tools designed for iemand die al kan kooken."
      },
      {
        "q": "Kan ik mijn bestaand receptbook opladen?",
        "a": "Ja. De Kit de Escandallos Pro maakt het mogelijk uw receptbook te laden and escandallo automatiseerd in minuten toe te passen. U kan ook de agent Executive Chef Pro vraagen om technische fiches te genereren op basis of vrije beschrijvingen."
      },
      {
        "q": "Is het for geavanceerde gastronomische keuken oder alleen for casual keuken?",
        "a": "For het hele spectrum. Er zijn specifieke agents: Creatieve Keuken for autor keuken, Creatieve Patisserie, Fermentus for avant-garde, VegChef Plantaardig for plant-based, naast meer dan 25 receptbooks per land. Echte cases in Michelin and Repsol Soles and in casual groups up to 25 eenheden."
      },
      {
        "q": "Hoe adapteert het system aan uw werkwijze?",
        "a": "Start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wie u binne, waar u werkt, uw type keuken and op wat für een schaal. Van dat moment an adapteeren alle agents aan uw context: lokale prijzen, normativa van uw land, keuken van de territorium and schaal van uw operatie."
      },
      {
        "q": "Is er iets specifisch for multi-locale groups and restaurantketens?",
        "a": "Ja. De agent Executive Chef Pro is gedacht for standaardisatie: hetzelfde technische fiche, hetzelfde escandallo and hetzelfde manuals repliceerd in alle eenheden. Gecombineerd met de Kit Plan Financiero kan u de KPI-reporting per eenheid and per group consolideeren."
      },
      {
        "q": "Is er een bibliotheek van specifische prompts for chefs?",
        "a": "Ja. De Pro Prompts eBook bevat meer dan 300 getest prompts for creativiteit, escandallo, technische fiches, vorming, interne communicatie and keukenoperatie, georganiseerd per gebruikssituatie."
      },
      {
        "q": "Hoe lang dauert het voordat de abonnement zich terugbetaalt?",
        "a": "De meiste executive chefs rapporteren return in de eerste nieuwe kaart. Een traditioneel menuverandering neemt 15-30 dagen in ideeënstorm, tests, escandallos, technische fiches and interne communicatie. Met AI Chef Pro and een good flow in Excel oder Google Workspace, gaat hetzelfde process naar 1-3 dagen, afhangig van de grootte de kaart and of het totale oder partielle reengineering is. Met 4-6 kaartveranderingen per jaar, recupereert u tussen 60 and 120 werkdagen."
      }
    ],
    "ctaTitle": "Creeër, escandalleer en repliceer recepten op de snelheid van een conversatie.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Plan Lidmaat for 10 € per maand met 10.000 crédits om alle agents te gebruiken.",
    "seo": {
      "title": "AI for Executive Chef: Recepten, Escandallos and Manuals | AI Chef Pro",
      "description": "AI-suite for executive and corporate chef: Executive Chef Pro agent, automatische escandallos, technische fiches and repliceerbare multi-locale manuals. Start heute.",
      "keywords": "AI executive chef, executive chef AI, corporate chef software, gastronomische AI-agent, automatische escandallos, technische fiches restaurant, standaardiseerde multi-locale recepten, keukenmanuals AI, food pairing AI, AI for restaurant groups, executive chef Nederland",
      "ogImage": "https://aichef.pro/og/use-cases/chef-ejecutivo.jpg"
    },
    "personalizationTitle": "Personaliseerd aan U vanaf Minut Een",
    "personalizationBody": "AI Chef Pro start met een conversationele onboarding van 2 minuten —de agent «Wie Ben Ik?»— waarin u vertelt wie u binne, waar u werkt, wat für een keuken u leidt en op wat für een schaal u opereert. Van dat moment an reageert elke agent —van escandallos tot creativiteit— aangepast aan uw context: uw lokale keuken, uw normativa, uw marktprijzen en de grootte van uw brigade. Het is geen formulier: het is een korte conversatie die alles wat daarna komt betekenis geeft.",
    "appsTitle": "De AI-Agents die U als Executive Chef Zal Gebruiken",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Hoofdagent: multi-locale standaardisatie, technische fiches and kaartbesluiten."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Professioneel gerechtontwikkeling met gedetailleerd recept and initiële escandallo downloadbaar as CSV (referentie-marktprijzen), klaar om in de Kit de Escandallos Pro te laden."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Ingredientecombinaties and pairings met wetenschappelijk basis."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Creatieve fermentatie: koji, kombucha, shoyu, miso, garum and lactofermentos."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools and Utilities",
        "description": "Precise data over mermas and rendements per ingrediente. Essentieel for realistisch escandallo."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools and Utilities",
        "description": "Portiecalculator die recepten scaleert to any number of gasten."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools and Utilities",
        "description": "Automatische identificatie van potentielle allergenen per recept and per gerecht."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Creatieve restaurantdesserts met professioneel patisserietechniek."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Selectie- and techniekassistent met the professioneel catalog van Sosa."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de tSpoonLab catalog for geavanceerde techniken and applicaties."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI Models + LLM",
        "description": "Diepe onderzoek: trends, producenten and opkomende techniken."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-generated gastronomische fotografie for technische fiches and pers."
      },
      {
        "name": "Gastro Lexicon",
        "category": "Gastro Kennis",
        "description": "Tutor met definities van techniken, processen, additiven and gastronomische wetenschap."
      }
    ],
    "metrics": [
      {
        "value": "−90 %",
        "label": "tijd om nieuwe kaart te sluiten"
      },
      {
        "value": "×10",
        "label": "snelheid van technische fiches"
      },
      {
        "value": "+4 pp",
        "label": "marge door bettere escandallo"
      },
      {
        "value": "13+",
        "label": "AI-agents for uw rol"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Sluiten van een nieuwe kaart: tussen 15 and 30 dagen, afhangig van de standaardisatie van de process",
        "Receptbook in losse bladen, rommelige Word-documenten and handgeschrieben notizen",
        "Elke locatie interpreteert de recept op uw eigen wijze and the resultaat varieert",
        "Handmatig escandallo met calculator: u verandert een grammage and herschrijft alles",
        "Manuals and onboarding continueel verouderd"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Sluiten van een nieuwe kaart: tussen 1 and 3 dagen, afhangig van de grootte and of het totale oder partielle reengineering is",
        "Centraliseerd receptbook met escandallo, allergenen, techniek and storytelling",
        "Hetzelfde gerecht, hetzelfde kwaliteit and hetzelfde cost in 1, 5 oder 25 keukens",
        "Professioneel escandallo that instant recalculiert met any verandering",
        "Manuals up-to-date met een klik and onboarding klaar for nieuwe chefs"
      ]
    },
    "appUrlPath": "/agents/chef-ejecutivo-pro",
    "galleryTitle": "De Dag-tot-Dag van een Executive Chef, in Beelden",
    "gallerySubtitle": "Wat u met AI Chef Pro kan beheere: brigade, technische fiches, creativiteit, escandallos en interne communicatie.",
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
    "h1": "AI voor chef-kok en keukenchef",
    "heroSubtitle": "Beheert stations, kostprijsberekeningen, mise en place en teamtraining met een suite van AI-agenten ontworpen voor de dagelijkse praktijk van de professionele keukenchef.",
    "heroTagline": "Meer koken, minder administratie",
    "badge": "Voor chef-koks en keukenchefs",
    "painsTitle": "Waar een keukenchef niet omheen kan",
    "pains": [
      "Het nauwkeurig berekenen van de foodcost van elk gerecht en van de volledige menukaart met producten waarvan de prijs elke week verandert",
      "Het coördineren van mise en place en stations zonder verstoringen tijdens servicepieken",
      "Het up-to-date houden van APPCC zonder dat de administratie tijd van de keuken steelt",
      "Het trainen en begeleiden van het team in gestandaardiseerde technieken en procedures met frequente wisselingen",
      "Het vernieuwen van de menukaart elk seizoen met behoud van marge en respect voor lokale producten",
      "Het communiceren met bediening, directie en leveranciers met professionele documentatie, niet met aantekeningen in een notitieboekje"
    ],
    "featuresTitle": "Hoe AI Chef Pro een keukenchef helpt",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Executive Chef Pro",
        "description": "Gespecialiseerde agent om u te ondersteunen bij het standaardiseren van recepten, technische fiches en kookhandleidingen."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken + Food Pairing AI",
        "description": "Brainstorm voor nieuwe gerechten met professionele basis. Creatieve Keuken levert recept + kostprijsberekening CSV met referentieprijzen, klaar voor het Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Professionele kostprijsberekeningen",
        "description": "Kit de Escandallos Pro: u laadt de CSV van Creatieve Keuken, vervangt prijzen door de reële en verkrijgt direct kosten, foodcost % en marge."
      },
      {
        "icon": "BookOpen",
        "title": "Professionele technische fiches",
        "description": "Recept, procedure, allergenen, presentatie en storytelling in één document, klaar om af te drukken."
      },
      {
        "icon": "CheckSquare",
        "title": "Taken en mise en place",
        "description": "Kit de Tareas met specifieke sjablonen per concept: opening, afsluiting, stations en service."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC en traceerbaarheid",
        "description": "Pack APPCC met 19 registraties: temperaturen, verliezen, allergenen en traceerbaarheid vanaf de mobiel van het team."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Gastronomisch onderzoek en ontwikkeling: koji, kombucha's, shoyu's, garums en lactofermenten met professionele ondersteuning."
      },
      {
        "icon": "GraduationCap",
        "title": "Pro Prompts eBook",
        "description": "Meer dan 300 geteste prompts voor creativiteit, kostprijsberekening, technische fiches, training en keukenoperaties."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergenen ID en Mermas GenCal",
        "description": "Automatische detectie van allergenen per gerecht en nauwkeurige gegevens over verliezen en opbrengsten per ingrediënt."
      }
    ],
    "workflowTitle": "Een echte dag van een keukenchef met AI Chef Pro",
    "workflow": [
      "08:00 · Opening — u print de mise en place van de dag vanuit het Kit de Tareas en valideert bestellingen bij leveranciers met het Kit Inventario.",
      "09:00 · Creatieve Keuken — u ontwikkelt een gerecht buiten de kaart voor het weekend met product dat goed geprijsd was. U ontvangt recept + kostprijsberekening CSV.",
      "10:30 · Kit de Escandallos Pro — u laadt de CSV, past uw reële prijzen toe en valideert dat de foodcost klopt op 28 %.",
      "12:30 · Service — het team registreert verliezen en temperaturen vanaf de mobiel met het Pack APPCC. U bent in de keuken, niet op kantoor.",
      "15:30 · Korte briefing met de brigade om het gerecht van de dag door te nemen en de mise aan te passen.",
      "17:00 · Pro Prompts eBook — u vraagt de agent om het script te genereren voor de training van een nieuwe kok die morgen begint.",
      "19:30 · Avondservice — u coördineert de service met het team, ondersteund door de gecentraliseerde technische fiches.",
      "23:30 · Afsluiting — u ondertekent de APPCC van de dag, genereert het rapport en het gaat naar de WhatsApp van de eigenaar binnen 10 minuten."
    ],
    "productsTitle": "Downloadbare sjablonen en kits voor keukenchefs",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "kit-tareas",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Het Kit de Escandallos en het Pack APPCC hebben mij 5 uur administratie per week bespaard. Maar wat ik het meest gebruik is Creatieve Keuken voor gerechten buiten de kaart in het weekend: in één ochtend rond ik recept, kostprijsberekening en technische fiche af. Vroeger was dat een hele week.",
    "testimonialAuthor": "Lucía Romero",
    "testimonialRole": "Keukenchef, mediterraan restaurant met 70 plaatsen",
    "faqTitle": "Veelgestelde vragen van keukenchefs",
    "faqs": [
      {
        "q": "Moet u een Excel-expert zijn?",
        "a": "Nee. De sjablonen van het Kit de Escandallos Pro en het Pack APPCC hebben vooraf geladen formules, u voert alleen gegevens in. Er is een video-tutorial van 5 minuten om te starten."
      },
      {
        "q": "Werkt het als onze menukaart elke maand of elk seizoen verandert?",
        "a": "Dat is het ideale geval. Creatieve Keuken genereert nieuwe gerechten met kostprijsberekening in CSV, u laadt het in het Kit de Escandallos Pro met uw prijzen en exporteert de technische fiches. Wat een week werk was, wordt een dag."
      },
      {
        "q": "Begrijpt de AI professionele keukentermen?",
        "a": "Ja. Creatieve Keuken, Food Pairing AI, Fermentus Con AI+ en de receptenboeken per land (Italiaans, Mexicaans, Japans, Peruaans, enz.) zijn getraind met professionele gastronomische kennis: technieken, kostprijsberekening, grammages, snijtechnieken, presentatie en storytelling. Het is geen generieke ChatGPT."
      },
      {
        "q": "Hoe past het zich aan mijn specifieke keuken aan?",
        "a": "U begint met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type keuken u leidt, waar u werkt en op welke schaal. Vanaf dat moment reageren alle agenten aangepast aan uw reële context."
      },
      {
        "q": "Kan ik alles downloaden in Excel en PDF?",
        "a": "Ja. Alle documentatie is exporteerbaar en bewerkbaar: kostprijsberekeningen, technische fiches, APPCC, mise en place en teamtraining."
      },
      {
        "q": "Werkt het voor keukens met geavanceerde technieken (fermenten, sferificaties, lang garen)?",
        "a": "Ja. Fermentus Con AI+ dekt geavanceerde fermentatie (koji, kombucha, shoyu, miso, garum, lactofermenten) en Creatieve Keuken begrijpt technieken zoals sous vide, sferificaties, gelificaties en gecontroleerd lang garen."
      }
    ],
    "ctaTitle": "Meer koken, minder administratie. Win uren terug voor wat er toe doet.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor chef-kok en keukenchef: Kostprijsberekeningen, Fiches en APPCC | AI Chef Pro",
      "description": "AI-suite voor professionele keukenchefs: gespecialiseerde agenten, kostprijsberekeningen, technische fiches, mise en place en APPCC met echte gastronomische ondersteuning. Begin vandaag.",
      "keywords": "AI chef keuken, keukenchef software, AI keukenchef, kostprijsberekening keuken, technische fiches AI, APPCC keuken, mise en place AI, gastronomische AI-agent, keukenchef Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/chef-cocina.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw keuken vanaf de eerste minuut",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type keuken u leidt, in welke stad, welk type menu u beheert en op welke schaal u opereert. Vanaf dat moment reageert elke agent — van kostprijsberekeningen tot creativiteit — aangepast aan uw context: lokale producten, regelgeving van uw land, omvang van uw brigade en reëel budget. Het is geen formulier: het is een kort gesprek dat de suite echt nuttig maakt voor uw dagelijkse praktijk in de keuken.",
    "appsTitle": "De AI-agenten die u als keukenchef gaat gebruiken",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standaardisatie van recepten, technische fiches en kookhandleidingen."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van professionele gerechten met recept + kostprijsberekening CSV, klaar voor het Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Combinaties van ingrediënten en pairing op wetenschappelijke basis."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Gastronomisch onderzoek en ontwikkeling: creatieve fermentatie van koji, kombucha, shoyu, miso en garum."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Creatieve restaurantdesserts met professionele patisserietechniek."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Nauwkeurige gegevens over verliezen en opbrengsten per ingrediënt."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en Utilities",
        "description": "Portiecalculator die recepten schaalt naar elk aantal gasten."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools en Utilities",
        "description": "Omzetter van gewichten en maten voor professionele keuken."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per recept en gerecht."
      },
      {
        "name": "Personeelsmaaltijden",
        "category": "Gastro Profile Pro",
        "description": "Generator van personeelsmenu's die kosten bespaart en het team motiveert."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent met de professionele catalogus van Sosa voor geavanceerde technieken."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de tSpoonLab-catalogus voor technische toepassingen."
      },
      {
        "name": "Gastro Lexicon",
        "category": "Gastro Kennis",
        "description": "Tutor met definities van technieken, processen en gastronomische wetenschap."
      }
    ],
    "metrics": [
      {
        "value": "−5 h",
        "label": "wekelijks aan administratie"
      },
      {
        "value": "×7",
        "label": "snelheid afronden nieuwe menukaart"
      },
      {
        "value": "+3 pp",
        "label": "marge na reële kostprijsberekening"
      },
      {
        "value": "13+",
        "label": "AI-agenten voor uw keuken"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Receptenverzameling in een notitieboek en losse vellen, verschillende versies per kok",
        "Handmatige kostprijsberekening met rekenmachine telkens wanneer een prijs verandert",
        "APPCC op gedrukt papier dat zich opstapelt en niemand controleert",
        "Het vernieuwen van de menukaart duurt 15 tot 30 dagen tussen brainstorm, kostprijsberekeningen en fiches",
        "Geïmproviseerde teamtraining telkens wanneer iemand nieuw komt"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Gecentraliseerd receptenboek met kostprijsberekening, allergenen, techniek en storytelling",
        "Automatische kostprijsberekening die direct herberekent bij elke prijswijziging",
        "APPCC vanaf mobiel met registraties en meldingen, klaar voor inspectie",
        "Menukaart vernieuwen in 1-3 dagen met Creatieve Keuken + Kit de Escandallos Pro",
        "Herbruikbare trainingshandleidingen met script van het Pro Prompts eBook"
      ]
    },
    "galleryTitle": "De dagelijkse praktijk van een keukenchef, in beeld",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: brigade, mise en place, technische fiches, service, magazijn en teamtraining.",
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
    "h1": "AI voor Sous Chef",
    "heroSubtitle": "Organiseer partijen, beheer mise en place, superviseer het team en bespaar administratieve uren met een suite van AI-agenten ontworpen voor de sous chef in de professionele keuken.",
    "heroTagline": "De rechterhand van de chef-kok, met systeem",
    "badge": "Voor sous chefs",
    "painsTitle": "Wat een Sous Chef Moet Oplossen",
    "pains": [
      "Partijen en mise en place nauwkeurig coördineren wanneer het tempo niet wacht",
      "De chef-kok vervangen wanneer hij er niet is, zonder dat kwaliteit of operatie achteruitgaan",
      "Het keukenteam opleiden en begeleiden met consistente criteria",
      "APPCC-traceerbaarheid up-to-date houden zonder dat het papierwerk zich opstapelt",
      "Snelle toegang hebben tot actuele technische fiches tijdens de service",
      "Kostprijsberekeningen valideren wanneer nieuwe ingrediënten binnenkomen of een leverancier verandert"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Sous Chef Helpt",
    "features": [
      {
        "icon": "CheckSquare",
        "title": "Mise en place en taken per partij",
        "description": "Kit de Tareas met gestructureerde lijsten per dienst en per partij, klaar om elke ochtend af te drukken."
      },
      {
        "icon": "BookOpen",
        "title": "Altijd actuele technische fiches",
        "description": "Snelle toegang vanaf de mobiel tot recept, procedure, opmaak en allergenen van elk gerecht tijdens de service."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC vanaf de mobiel",
        "description": "Pack APPCC met registraties, temperatuuralarmen en PDF-export. Het team registreert vanaf de mobiel zonder papierwerk."
      },
      {
        "icon": "Calculator",
        "title": "Snelle kostprijsberekeningen",
        "description": "Creatieve Keuken levert recept + kostprijs-CSV; het Kit de Escandallos Pro beheert dit met uw werkelijke prijzen en u valideert direct de marge."
      },
      {
        "icon": "GraduationCap",
        "title": "Teamopleiding",
        "description": "Pro Prompts eBook + Executive Chef Pro genereren handleidingen en onboarding klaar voor nieuwe koks."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Gastronomische AI-chat voor het oplossen van technische vragen, het voorstellen van speciale gerechten en het valideren van technieken in realtime."
      },
      {
        "icon": "Users",
        "title": "Personeelsmaaltijden",
        "description": "Generator voor personeelsmenu's die gebruikmaakt van het product dat u al in de koeling heeft en het team motiveert."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergenen ID en Mermas GenCal",
        "description": "Automatische detectie van allergenen en nauwkeurige verliesgegevens voor gang en partij."
      }
    ],
    "workflowTitle": "Een Echte Dag van een Sous Chef met AI Chef Pro",
    "workflow": [
      "07:30 · Opening – u opent het Kit de Tareas en controleert de mise en place van de dag. U tekent de kritieke voorraad met het Kit Inventario.",
      "08:30 · Korte briefing met de brigade – u doorloopt de gangen van de dag met gecentraliseerde technische fiches in de hand.",
      "12:00 · Middagservice – u superviseert de partijen, het team registreert verliezen en temperaturen vanaf de mobiel met het Pack APPCC.",
      "15:30 · Creatieve Keuken – de chef-kok vraagt u om een speciaal gerecht voor zaterdag. U genereert gerecht + kostprijs-CSV in 20 minuten.",
      "16:00 · Kit de Escandallos Pro – u laadt de CSV met uw werkelijke prijzen, valideert dat de foodcost op 28% klopt en exporteert het technische fiche.",
      "17:30 · Personeelsmaaltijden – u bereidt het personeelsmenu voor de komende week, rekening houdend met de doelkost en de voorraad in de koeling.",
      "20:00 · Avondservice – u coördineert de gangen met de brigade, u lost twijfels op met Creatieve Keuken wanneer de junior-kok een techniek moet bevestigen.",
      "23:30 · Afsluiting – u tekent APPCC, laat de mise en place voor de volgende dag klaar en stuurt het rapport naar de chef-kok."
    ],
    "productsTitle": "Downloadbare Sjablonen en Kits voor Sous Chefs",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Sous chef zijn is op honderd plaatsen tegelijk zijn. De mise en place-lijsten van het Kit de Tareas en de APPCC-registraties vanaf de mobiel hebben mijn chaos georganiseerd. Wanneer de chef-kok er niet is, blijft alles werken omdat de procedures zijn gedocumenteerd.",
    "testimonialAuthor": "Nicolás Vega",
    "testimonialRole": "Sous Chef, restaurant met 100 zitplaatsen",
    "faqTitle": "Veelgestelde Vragen van Sous Chefs",
    "faqs": [
      {
        "q": "Passen de sjablonen zich aan de stijl van mijn keuken aan?",
        "a": "Ja. Er zijn specifieke Kits de Tareas per concept (casual, gastronomisch, dark kitchen, hotel, pizzeria, hamburgerrestaurant, patisserie, bar, catering, ijssalon, chocolaterie, creatief restaurant, privé chef) en ze kunnen allemaal worden aangepast aan de stijl van uw keuken."
      },
      {
        "q": "Werkt het vanaf de mobiel voor teamregistraties?",
        "a": "Ja. De APPCC-registraties, verliezen, temperaturen en taakcontroles worden vanaf de mobiel van het personeel gedaan zonder iets te installeren. Aan het einde van de dag wordt het geëxporteerd naar PDF voor de chef-kok of de eigenaar."
      },
      {
        "q": "Is het ingewikkeld voor het team om te gebruiken?",
        "a": "Nee. Het team vult alleen vakjes in of vinkt aan. De echte leercurve is 1 dag. Er is een onboardingvideo van 5 minuten."
      },
      {
        "q": "Werkt het als ik niet degene ben die over de tools in de keuken beslist?",
        "a": "U kunt beginnen met het Lidmaatschapsplan (€10 per maand, 10.000 credits) voor uw eigen lijsten en voorstellen. Wanneer u het 1-2 weken heeft gebruikt, stel het dan voor aan de chef-kok met concrete gegevens: bespaarde tijd, gevalideerde kostprijsberekeningen, georganiseerde mise en place."
      },
      {
        "q": "Hoe helpt het mij tijdens servicepieken?",
        "a": "De gecentraliseerde technische fiches geven u snelle toegang vanaf de mobiel tijdens de service. Als er een technische vraag ontstaat, reageert Creatieve Keuken binnen enkele seconden. Mentale Coach helpt ook bij het beheersen van stress in keukens met hoge druk."
      },
      {
        "q": "Is er iets specifieks voor promotie naar chef-kok?",
        "a": "Ja. Pro Prompts eBook (300+ professionele prompts), Executive Chef Pro (multi-locatie standaardisatie) en Gastro Lexicon (techniekreferentie) zijn belangrijke tools om door te groeien naar het volgende niveau."
      }
    ],
    "ctaTitle": "Organiseer uw keuken zonder losse papieren.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Sous Chef: Mise en Place, Technische Fiches en APPCC | AI Chef Pro",
      "description": "AI-suite voor sous chef in de professionele keuken: mise en place, gecentraliseerde technische fiches, kostprijsberekeningen, APPCC vanaf de mobiel en teamopleiding. Begin vandaag.",
      "keywords": "AI sous chef, software sous chef, mise en place keuken AI, APPCC sous chef, technische fiches keuken, opleiding keukenbrigade, sous chef Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/sous-chef.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd naar Uw Keuken vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent 'Wie Ben Ik?', een conversationele onboarding van 2 minuten waarin u vertelt welk type keuken u leidt, in welke stad, welke kaart u hanteert en op welke schaal. Vanaf dat moment reageert elke agent – van mise en place tot kostprijsberekeningen – afgestemd op uw context: type service, grootte van de brigade en de werkelijke operatie. Het is geen formulier: het is een kort gesprek dat de suite echt nuttig maakt voor het partijritme.",
    "appsTitle": "De AI-agenten die u als Sous Chef zult gebruiken",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standaardisatie van recepten, technische fiches en gecentraliseerde keukenhandleidingen."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van professionele gerechten met recept + kostprijs-CSV klaar voor het Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Combinaties van ingrediënten en pairing op wetenschappelijke basis."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Creatieve restaurantdesserts met professionele patisserie-techniek."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en Utilities",
        "description": "Portiecalculator die recepten schaalt naar elk aantal gasten."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools en Utilities",
        "description": "Omzetter van gewichten en maten voor de professionele keuken."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Nauwkeurige verlies- en rendementsgegevens per ingrediënt."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per recept en gerecht."
      },
      {
        "name": "Personeelsmaaltijden",
        "category": "Gastro Profile Pro",
        "description": "Generator voor personeelsmenu's met product dat u al in de koeling heeft."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en Utilities",
        "description": "Psychologische coaching voor het beheersen van stress en moeilijke gesprekken in de keuken."
      },
      {
        "name": "Gastro Lexicon",
        "category": "Gastro Kennis",
        "description": "Tutor met definities van technieken, processen en gastronomische wetenschap."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "mise en place-snelheid"
      },
      {
        "value": "−4 h",
        "label": "wekelijks aan papierwerk"
      },
      {
        "value": "zelfde",
        "label": "standaard wanneer de chef er niet is"
      },
      {
        "value": "11+",
        "label": "agenten voor uw rol"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Mise en place elke ochtend aan het team gedicteerd, elke dag anders",
        "APPCC op geprint papier dat aan het einde van de week opstapelt",
        "Technische fiches in het notitieboekje van de chef-kok, ontoegankelijk tijdens de service",
        "Wanneer de chef-kok er niet is, dalen kwaliteit en operatie",
        "Opleiding van nieuwe koks geïmproviseerd en inconsistent"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Mise en place elke dag afdrukbaar met het Kit de Tareas gestructureerd per partij",
        "APPCC vanaf de mobiel met registraties, alarmen en PDF-export bij afsluiting",
        "Gecentraliseerde technische fiches toegankelijk vanaf de mobiel tijdens de service",
        "Gedocumenteerde procedures – de standaard blijft behouden, zelfs als het team verandert",
        "Herhaalbare opleiding met script van het Pro Prompts eBook en handleidingen van de Executive Chef Pro"
      ]
    },
    "galleryTitle": "De Dagelijkse Routine van een Sous Chef, in Beeld",
    "gallerySubtitle": "Wat u met AI Chef Pro zult coördineren: mise en place, prep, teambegeleiding, service en traceerbaarheid.",
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
    "h1": "AI voor cateringchefs",
    "heroSubtitle": "Ontwerp evenementmenu's, bereken kosten per service en plan productie op schaal met een suite van AI-agenten ontworpen voor professionele catering en evenementchefs.",
    "heroTagline": "Productie op schaal zonder marge of kwaliteit te verliezen",
    "badge": "Voor catering- en evenementchefs",
    "painsTitle": "Wat een cateringchef absoluut moet oplossen",
    "pains": [
      "Kosten berekenen voor menu's met sterk wisselende aantallen gasten (50, 200, 500) terwijl de ingrediëntenprijzen elke week veranderen",
      "Productie, mise en place en inkoop op grote schaal plannen zonder fouten",
      "Logistiek, transport en opbouw op de locatie van de klant coördineren met respect voor tijden en temperaturen",
      "APPCC en traceerbaarheid handhaven buiten de vaste locatie, op externe locaties en in gekoelde voertuigen",
      "Creatieve menu's ontwerpen per evenementtype (bruiloft, zakelijk, cocktail, gala) zonder elke keer opnieuw te beginnen",
      "Communiceren met het productie-, transport- en serviceteam met duidelijke documentatie"
    ],
    "featuresTitle": "Hoe AI Chef Pro een cateringchef helpt",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Gespecialiseerde agent voor catering en culinaire evenementen: bruiloften, zakelijk, cocktails en galas met professionele kennis."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken + Food Pairing AI",
        "description": "Brainstormen voor evenementmenu's. Creatieve Keuken levert recept + kostenberekening CSV klaar voor de Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Kostenberekeningen per evenement",
        "description": "Kit de Escandallos Pro: u laadt de CSV met uw werkelijke prijzen, past het aantal gasten aan en krijgt direct kosten, foodcost % en marge."
      },
      {
        "icon": "Layers",
        "title": "Calcula Pax",
        "description": "Portiecalculator die recepten in seconden opschaalt naar 50, 200, 500 of 1000 gasten."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Catering",
        "description": "Specifieke sjablonen voor productie, transport, opbouw, service en afbouw op de locatie van de klant."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC buiten de locatie",
        "description": "Pack APPCC met sjablonen aangepast aan product dat onderweg is: traceerbaarheid, temperatuur tijdens transport en registraties op externe locatie."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Gastronomische fotografie met AI voor presentaties aan klanten, evenementvoorstellen en persberichten."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergenen ID",
        "description": "Automatische identificatie van allergenen, cruciaal voor evenementen met veel gasten met verschillende voedingsprofielen."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients Agent",
        "description": "Assistent voor het selecteren van technische ingrediënten uit de Sosa-catalogus, vooral nuttig bij cocktails en desserts."
      }
    ],
    "workflowTitle": "Een echte dag van een cateringchef met AI Chef Pro",
    "workflow": [
      "08:30 · Catering AI+ — de agent helpt u de menuvoorstel voor een bruiloft met 180 gasten af te ronden volgens de briefing van de klant.",
      "09:30 · Creatieve Keuken — u ontwikkelt de 12 gerechten van het menu met gedetailleerd recept en kostenberekening CSV met referentieprijzen.",
      "10:30 · Calcula Pax + Kit de Escandallos Pro — u schaalt op naar 180 gasten, laadt de CSV met uw werkelijke prijzen en valideert de doelwinstmarge.",
      "12:00 · Validatie met klant — u exporteert het voorstel met technische fiches en gastronomische fotografie van GastroIMG Gen+.",
      "14:00 · Kit de Tareas Catering — u plant productie, transport, opbouw, service en afbouw van het evenement van zaterdag.",
      "16:00 · APPCC buiten de locatie — u bereidt temperatuurregistraties tijdens transport en traceerbaarheid op externe locatie voor met het Pack APPCC.",
      "18:00 · Allergenen ID — u genereert het allergenenoverzicht per gerecht, klaar voor de zaal en voor gasten met beperkingen.",
      "19:30 · Brief aan het team — u stelt de servicebrief samen met het keuken- en zaalteam van het evenement, alles vanuit één bron."
    ],
    "productsTitle": "Downloadbare sjablonen en kits voor cateringchefs",
    "productIds": [
      "kit-tareas-catering",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "De kostenberekeningen per evenement besparen mij uren. Ik sluit een menu voor 200 gasten af met gevalideerde marge in 30 minuten. Vroeger was ik een halve middag bezig met rekenmachine en servetten. En het hebben van APPCC aangepast aan evenementen buiten de locatie heeft ons een enorme hoofdpijn bespaard met zakelijke klanten.",
    "testimonialAuthor": "Andrea Costa",
    "testimonialRole": "Cateringchef, specialist in zakelijke evenementen en bruiloften",
    "faqTitle": "Veelgestelde vragen van cateringchefs",
    "faqs": [
      {
        "q": "Is het geschikt voor elk cateringformaat?",
        "a": "Ja. Van boutique-catering met 50 gasten per maand tot bedrijven met meer dan 1000 services per maand en evenementen met 2000 gasten."
      },
      {
        "q": "Kunt u hiermee de wisselende aantallen gasten beheren?",
        "a": "Ja. Calcula Pax schaalt recepten op naar elk aantal gasten en de Kit de Escandallos Pro herberekent automatisch kosten, foodcost en marge."
      },
      {
        "q": "Deckt het APPCC buiten de vaste locatie?",
        "a": "Ja. Het Pack APPCC heeft specifieke sjablonen voor product dat reist in rugzak, motor, gekoelde bestelwagen of centrale keuken, inclusief traceerbaarheid op externe locatie."
      },
      {
        "q": "Zijn er specifieke sjablonen voor catering?",
        "a": "Ja. De Kit de Tareas Catering bevat gedetailleerde lijsten voor productie, transport, opbouw op locatie, service en afbouw, plus coördinatieprotocollen met de centrale keuken."
      },
      {
        "q": "Hoe past het zich aan uw type catering aan?",
        "a": "U begint met de agent «Wie Ben Ik?», een onboarding van 2 minuten waarin u vertelt welke soorten evenementen u doet (bruiloften, zakelijk, cocktails, galas), gemiddelde grootte, stad en werkwijze. Alles past zich aan uw context aan."
      },
      {
        "q": "Is het geschikt voor het ontwerpen van innovatieve menu's?",
        "a": "Ja. Catering AI+ + Creatieve Keuken + Food Pairing AI + Fermentus Con AI+ werken samen om creatieve menu's te ontwerpen met een professionele basis, geen recepten gekopieerd van internet."
      }
    ],
    "ctaTitle": "Ontwerp, bereken kosten en produceer evenementen zonder losse papieren.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor cateringchefs: menu's, kostenberekeningen en evenement-APPCC | AI Chef Pro",
      "description": "AI-suite voor cateringchefs: Catering AI+, Creatieve Keuken, Calcula Pax, kostenberekeningen per evenement, APPCC buiten de locatie en productieplanning op schaal. Begin vandaag.",
      "keywords": "AI cateringchef, cateringchef software, kostenberekeningen catering AI, software catering evenementen, APPCC catering, bruiloftmenu AI, beheer culinair evenement AI, cateringchef Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/chef-catering.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd naar uw type catering vanaf de eerste minuut",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welke soorten evenementen u ontwerpt (bruiloften, zakelijk, cocktails, galas), gemiddelde grootte, stad en manier van werken. Vanaf dat moment reageert elke agent —van Catering AI+ tot de kostenberekeningen— aangepast aan uw context: servicetypes, schaal van uw centrale keuken en de werkelijke operatie. Het is geen formulier: het is een kort gesprek dat de suite echt nuttig maakt voor uw dagelijkse werk als cateringchef.",
    "appsTitle": "De AI-agenten die u als cateringchef gaat gebruiken",
    "apps": [
      {
        "name": "Catering AI+",
        "category": "Bedrijfsconcepten",
        "description": "Hoofdagent: bruiloften, zakelijk, cocktails en galas met professionele kennis."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire creativiteit",
        "description": "Ontwikkeling van professionele gerechten met recept + kostenberekening CSV klaar voor de Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire creativiteit",
        "description": "Combinaties van ingrediënten en pairing op wetenschappelijke basis."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire creativiteit",
        "description": "Evenementdesserts met professionele techniek, ideaal voor banketten en galas."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire creativiteit",
        "description": "Voor avant-gardistische canapés met fermenten, garums en innovatieve technieken."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en hulpprogramma's",
        "description": "Portiecalculator die recepten opschaalt naar 50, 200 of 500 gasten."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpprogramma's",
        "description": "Automatische identificatie van allergenen per gerecht, cruciaal voor grote evenementen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpprogramma's",
        "description": "Nauwkeurige gegevens over verliezen en opbrengsten voor productie op schaal."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools en hulpprogramma's",
        "description": "Professionele omzetter van gewichten en maten voor industriële productie."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro-leveranciers",
        "description": "Assistent voor technische ingrediënten uit de Sosa-catalogus."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-kennis",
        "description": "Gastronomische fotografie met AI voor voorstellen aan klanten en persberichten."
      }
    ],
    "metrics": [
      {
        "value": "×10",
        "label": "snelheid afronden evenementmenu"
      },
      {
        "value": "+5 pp",
        "label": "marge na werkelijke kostenberekening"
      },
      {
        "value": "−50 %",
        "label": "tijd in logistieke planning"
      },
      {
        "value": "11+",
        "label": "agenten voor uw catering"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Evenementmenu afronden met klant: een halve middag met rekenmachine en servetten",
        "Geïmproviseerd APPCC buiten de locatie, zonder echte traceerbaarheid tijdens transport",
        "Productie voor 200 gasten zonder nauwkeurige opschaling, hoge verliezen",
        "Voorstellen aan klanten met Word-sjablonen en stockfoto's",
        "Brief aan het team op losse vellen die verloren raken"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Menu afronden met gevalideerde marge in 30 minuten met Catering AI+ en Kit de Escandallos Pro",
        "APPCC aangepast aan product dat reist, met registraties vanaf mobiel en traceerbaarheid per evenement",
        "Productie opgeschaald met Calcula Pax, verliezen gecontroleerd met Mermas GenCal",
        "Commerciële voorstellen met foto's van GastroIMG Gen+ en professionele technische fiches",
        "Gecentraliseerde en herbruikbare brief voor productie, transport, opbouw en service"
      ]
    },
    "galleryTitle": "De dagelijkse praktijk van een cateringchef, in beeld",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: menuontwerp, productie op schaal, logistiek, opbouw op externe locatie, service en traceerbaarheid.",
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
    "h1": "AI voor eigenaren van cateringbedrijven",
    "heroSubtitle": "Beheer de winstgevendheid per evenement, schaal de productie op, beheer tijdelijke teams en laat uw cateringbedrijf groeien met een suite van AI-agenten gespecialiseerd in horeca.",
    "heroTagline": "Gecontroleerde groei, echte marge, evenementen zonder chaos",
    "badge": "Voor eigenaren van cateringbedrijven",
    "painsTitle": "Wat een cateringondernemer niet kan negeren",
    "pains": [
      "Marges beheren met grote variabiliteit tussen evenementen: een bruiloft, een zakelijke cocktail en een koffiepauze hebben zeer verschillende rendementen",
      "Productie opschalen zonder kwaliteit of kostenbeheersing te verliezen wanneer er pieken zijn in bruiloften of evenementenseizoen",
      "Tijdelijke teams en vast personeel coördineren met roosters, contracten per evenement en duidelijke arbeidskosten",
      "Financiële rapportage aan investeerders of partners met geconsolideerde gegevens, niet geïmproviseerde Excel-bestanden",
      "Zakelijke klanten aantrekken met professionele voorstellen die contracten met een hogere waarde afsluiten",
      "Beslissen welke evenementen u accepteert en welke u afwijst op basis van echte margegegevens, niet op gevoel"
    ],
    "featuresTitle": "Hoe AI Chef Pro een cateringondernemer helpt",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Agent gespecialiseerd in culinaire evenementen: bruiloften, zakelijk, cocktails en galabals met professionele kennis."
      },
      {
        "icon": "FileText",
        "title": "Kit Plan Financiero",
        "description": "Cashflow, maandelijkse P&L, dashboard met ratio's en winstgevendheid per evenement en per klant. Professionele sjablonen aangepast aan catering."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekeningen per evenement",
        "description": "Creatieve Keuken levert recept + CSV-kostprijsberekening; Kit de Escandallos Pro beheert dit met uw werkelijke prijzen en doelstelling voor marge."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Roosters voor vast en tijdelijk personeel, contracten per evenement, urenregistratie en arbeidskosten per dienst."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP en certificeringen",
        "description": "Pack APPCC met sjablonen aangepast aan catering: traceerbaarheid, transport en registraties klaar voor inspectie en zakelijke klanten."
      },
      {
        "icon": "Sparkles",
        "title": "BlogPost SEO Gen+ + MenuDish Local SEO",
        "description": "SEO-suite om zakelijke klanten aan te trekken met organisch verkeer en betere posities."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Culinaire fotografie met AI voor voorstellen aan klanten, presentaties en webgalerij."
      },
      {
        "icon": "BarChart3",
        "title": "Operatiedashboard",
        "description": "Geconsolideerde financiële KPI's, bezettingsgraad, winstgevendheid per bedrijfslijn (bruiloften, zakelijk, cocktails)."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Diepgaand onderzoek naar markt, concurrenten en trends voor strategische groeibeslissingen."
      }
    ],
    "workflowTitle": "Een echte dag van een cateringondernemer met AI Chef Pro",
    "workflow": [
      "08:30 · Kit Plan Financiero — u opent het dashboard en ontdekt dat een evenement van het weekend een marge heeft van 18%, onder de doelstelling (28%).",
      "09:30 · Kit de Escandallos Pro — u analyseert de kostprijsberekening van het evenement en past het menu of de prijs aan voordat u het contract sluit.",
      "11:00 · Catering AI+ — u sluit een voorstel voor een zakelijke klant met een door AI gegenereerde presentatie die met de agent is gevalideerd.",
      "12:30 · GastroIMG Gen+ — u genereert de foto's van de gerechten van het voorgestelde menu om in de presentatie op te nemen.",
      "14:00 · Overleg met zakelijke klant — u presenteert een voorstel dat in 1 uur is afgerond in plaats van de traditionele 3 dagen.",
      "16:30 · Kit Plan Financiero — u valideert de kwartaalprognose en exporteert naar PDF voor overleg met partners.",
      "18:00 · Kit Gestión de Personal — u controleert het weekendrooster met vast en tijdelijk personeel en ondertekent contracten per evenement.",
      "20:00 · BlogPost SEO Gen+ — u publiceert een bericht over het laatste grote zakelijke evenement om organisch nieuwe klanten aan te trekken."
    ],
    "productsTitle": "Downloadbare sjablonen en kits voor cateringbedrijven",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-tareas-catering",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "AI Chef Pro heeft mij echte financiële controle gegeven. Ik weet precies bij welke evenementen ik geld verdien en bij welke niet, en dat heeft mij in staat gesteld om nee te zeggen tegen klanten die niet rendabel waren. In het eerste kwartaal zijn we 4 punten marge gestegen zonder prijzen te wijzigen. Alleen door menu's aan te passen en slechte evenementen te weigeren.",
    "testimonialAuthor": "Roberto Iglesias",
    "testimonialRole": "Eigenaar, zakelijk cateringbedrijf (€2M jaarlijkse omzet)",
    "faqTitle": "Veelgestelde vragen van cateringondernemers",
    "faqs": [
      {
        "q": "Is het geschikt voor een boutique-catering met minder dan 5 medewerkers?",
        "a": "Ja. Het is ideaal voor boutique omdat het operaties, financiën, marketing en klantvoorstellen in één tool consolideert. Een typische klant begint met 1 persoonlijk plan en groeit naar een bedrijf."
      },
      {
        "q": "En voor grote bedrijven met 50+ tijdelijke medewerkers?",
        "a": "Ook. Het Kit Gestión de Personal schaalt naar grote teams met roosters, contracten per evenement en consolidatie van arbeidskosten. Er zijn klanten met 100+ diensten per maand."
      },
      {
        "q": "Integreert het met mijn boekhoudsoftware of ERP?",
        "a": "Exporteert Excel, PDF en CSV die compatibel zijn met de meeste ERP's en administratiekantoren. Uw financiële team ontvangt documentatie die klaar is om te integreren."
      },
      {
        "q": "Is er een bedrijfsplan voor grote catering?",
        "a": "Ja. Vanaf een bepaalde omzet zijn er bedrijfsplannen met persoonlijke onboarding, geconsolideerde dashboards, training van het kernteam en prioritaire ondersteuning."
      },
      {
        "q": "Hoe helpt het mij om zakelijke klanten aan te trekken?",
        "a": "BlogPost SEO Gen+ en MenuDish Local SEO trekken organisch verkeer naar uw website; Catering AI+ helpt bij het opstellen van professionele voorstellen; GastroIMG Gen+ genereert foto's voor presentaties; Keyword Discovery AI+ vindt de echte zoekopdrachten van bedrijven in uw regio."
      },
      {
        "q": "Is het veilig om het financiële plan aan een AI toe te vertrouwen?",
        "a": "Ja. Het Kit Plan Financiero is een professionele Excel-sjabloon met vooraf geladen formules, geen AI. U voert de werkelijke gegevens in en de tool berekent. De AI-agenten worden alleen gebruikt om beslissingen te ondersteunen, voorstellen op te stellen en analyses uit te voeren, niet voor kritieke financiële berekeningen."
      }
    ],
    "ctaTitle": "Laat uw catering groeien met echte marge, niet met intuïtie.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor eigenaren van cateringbedrijven: winstgevendheid en financieel plan | AI Chef Pro",
      "description": "AI-suite voor cateringbedrijven: winstgevendheid per evenement, productie op schaal, tijdelijke teams, financieel plan en het aantrekken van zakelijke klanten. Begin vandaag.",
      "keywords": "AI cateringbedrijf, cateringondernemer AI, cateringsoftware, cateringbedrijfsbeheer, financieel plan catering, winstgevendheid catering, zakelijke klanten werven catering, cateringbedrijf opschalen, cateringondernemer Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/propietario-catering.jpg"
    },
    "personalizationTitle": "Vanaf de eerste minuut afgestemd op uw bedrijf",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type catering u uitvoert (bruiloften, zakelijk, cocktails, galabals), gemiddelde evenementgrootte, stad en jaarlijks volume. Vanaf dat moment reageert elke agent — van Catering AI+ tot het Financieel Plan — afgestemd op uw context: servicetypes, werkelijke schaal en doelmarkt. Het is geen formulier: het is een kort gesprek dat de suite echt nuttig maakt voor uw bedrijf.",
    "appsTitle": "De AI-agenten die u als cateringondernemer gaat gebruiken",
    "apps": [
      {
        "name": "Catering AI+",
        "category": "Bedrijfsconcepten",
        "description": "Hoofdagent: bruiloften, zakelijk, cocktails en galabals met professionele kennis."
      },
      {
        "name": "Pro Restaurant Manager",
        "category": "Gastro Profile Pro",
        "description": "Operationele en financiële assistent om u te ondersteunen bij beslissingen en rapportage aan partners."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire creativiteit",
        "description": "Ontwikkeling van evenementmenu's met recept + CSV-kostprijsberekening klaar voor het Kit de Escandallos Pro."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire creativiteit",
        "description": "Desserts voor evenementen en banketten met professionele techniek."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en hulpprogramma's",
        "description": "Portiecalculator die recepten opschaalt naar 50, 200 of 500 gasten."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpprogramma's",
        "description": "Automatische identificatie van allergenen per recept, cruciaal voor grote evenementen."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en sociale media",
        "description": "Blogberichten om organisch verkeer naar uw cateringwebsite te trekken."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en sociale media",
        "description": "SEO-beschrijvingen om de webpositie van uw catering te verbeteren."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Content en sociale media",
        "description": "Trefwoordonderzoek om bedrijven aan te trekken die catering in uw regio zoeken."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-kennis",
        "description": "Culinaire fotografie voor klantvoorstellen en commerciële presentaties."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI-modellen + LLM",
        "description": "Onderzoek naar markt, concurrenten en trends in de evenementensector."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en hulpprogramma's",
        "description": "Coaching voor stressbeheersing, moeilijke beslissingen en gesprekken met partners of team."
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "marge in het eerste kwartaal"
      },
      {
        "value": "×3",
        "label": "snelheid van het afsluiten van voorstellen"
      },
      {
        "value": "−40 %",
        "label": "tijd aan financiële rapportage"
      },
      {
        "value": "12+",
        "label": "agenten voor uw bedrijf"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Niet weten welke van de 50 evenementen van de maand echt winstgevend is",
        "Voorstellen aan zakelijke klanten in 3 dagen afsluiten met Word-sjablonen",
        "Handmatige Excel-roosters voor tijdelijk personeel zonder kostenbeheersing",
        "Versnipperde HACCP tussen evenementen, een probleem met veeleisende zakelijke klanten",
        "Geïmproviseerde of uitbestede marketing tegen hoge kosten zonder organische leads te genereren"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Duidelijke winstgevendheid per evenement en per klant, beslissingen om te accepteren/afwijzen op basis van gegevens",
        "Voorstellen in 1 uur afsluiten met Catering AI+ + GastroIMG Gen+ + professionele presentatie",
        "Roosters met Kit Gestión de Personal: urenregistratie en geconsolideerde kosten",
        "Uniforme en professionele HACCP, klaar voor elke inspectie of zakelijke klant",
        "SEO-suite die organische leads genereert zonder uitgaven aan bureaus"
      ]
    },
    "galleryTitle": "De dagelijkse praktijk van een cateringondernemer, in beeld",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: prijsstelling, voorstellen aan klanten, grootschalige evenementen, teams, logistiek magazijn en financiële rapportage.",
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
    "h1": "AI voor bartenders en mixologen",
    "heroSubtitle": "Ontwerp cocktailkaarten met professionele kostprijsberekening, kostprijs per drankje met reële kosten en techniek, en creëer signature cocktails met storytelling en pairing met een suite van gespecialiseerde gastronomische AI-agenten voor cocktails.",
    "heroTagline": "Cocktails met reële marge en signature techniek",
    "badge": "Voor bartenders, mixologen en cocktailmakers",
    "painsTitle": "Wat een Bartender Niet Kan Nalaten op te Lossen",
    "pains": [
      "Complexe cocktails met veel ingrediënten (sterke drank, cordials, infusies, garnishes) kostprijsberekenen zonder uren met de rekenmachine te verliezen",
      "De kaart elk seizoen vernieuwen met nieuwe drankjes met behoud van marge en een food cost die consistent is met de rest van de bar",
      "Recepten in de bar standaardiseren zodat elke barman het drankje elke keer met dezelfde balans kan repliceren",
      "Mermen in de bar beheersen: breuk van glaswerk, over-pour, verdamping, garnishes die verspild worden",
      "Storytelling: elke cocktail heeft een naam, een verhaal en een pairing nodig die de hoge prijs rechtvaardigt",
      "Zich onderscheiden in een competitief gebied met signature cocktails, visuele branding en actieve sociale media"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Bartender Helpt",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Agent gespecialiseerd in professionele cocktails, wijnbars, cocktailbars en sterke drank met geavanceerde techniek."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Onverwachte combinaties voor signature cocktails met wetenschappelijke basis en pairings met keuken."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijs per drankje",
        "description": "Bar & Lounge AI+ levert recept + kostprijs CSV met techniek; Kit de Escandallos Pro beheert het met reële kosten per drankje, food cost % en voorgestelde prijs."
      },
      {
        "icon": "BookOpen",
        "title": "Technische fiches van cocktails",
        "description": "Recept, techniek, garnish, glaswerk, pairing en storytelling in één document klaar voor het team."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Sjablonen: mise van de bar, prep van cordials en infusies, procedures per dienst, kasafsluiting, voorraadbeheer."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC bar",
        "description": "Traceerbaarheid van ijs, verse garnishes, zelfgemaakte infusies en kritische temperaturen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planning van seizoenskaarten: zomercocktails, warme winterdrankjes, thematische kaarten voor Valentijn, Kerst en evenementen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Cocktailfotografie met AI-referentie + content voor Instagram met professionele redactionele kalender."
      },
      {
        "icon": "BarChart3",
        "title": "KPIs bar",
        "description": "Gemiddelde ticket, rotatie van drankjes, marge per categorie (klassiekers, signature, wijnen, bieren)."
      }
    ],
    "workflowTitle": "Een Echte Dag van een Bartender met AI Chef Pro",
    "workflow": [
      "11:00 · Opening — checklist Kit de Tareas Bar: mise van verse garnishes, prep van zelfgemaakte cordials, ijs laden, voorraad controleren.",
      "12:00 · Bar & Lounge AI+ — u ontwikkelt een nieuwe signature voor de zomerkaart (gin met aardbeien-basilicum shrub). Creatieve Keuken levert recept + kostprijs CSV.",
      "13:00 · Food Pairing AI — u valideert de pairing met een gerecht uit de keuken en verfijnt de techniek.",
      "14:00 · Kit de Escandallos Pro — u laadt de CSV met uw reële prijzen van premium sterke drank en ingrediënten, valideert marge per drankje en food cost %.",
      "17:00 · Service — het team repliceert het drankje met de technische fiche (recept, techniek, garnish, glaswerk, storytelling).",
      "19:00 · Gastro Calendar — u actualiseert de redactionele kalender van Instagram met de lancering van de nieuwe signature.",
      "20:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de referentieafbeelding van het drankje en de posts voor de lancering.",
      "02:00 · Sluiting — grondige reiniging, APPCC ondertekend, mermenbeheersing en eindvoorraad."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor cocktails",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "AI Chef Pro heeft mijn manier van het afronden van cocktailkaarten veranderd. Vroeger was het een week van servetten en rekenmachine; nu is het een dag met professionele kostprijsberekening, technische fiche met storytelling en gevalideerde pairing, klaar voor mijn team om te repliceren. We verhoogden de marge met 5 punten en verdrievoudigden de engagement op Instagram met GastroIMG.",
    "testimonialAuthor": "Hugo Vázquez",
    "testimonialRole": "Bartender, signature cocktailbar",
    "faqTitle": "Veelgestelde vragen van bartenders",
    "faqs": [
      {
        "q": "Is het geschikt voor klassieke, signature of casual cocktails?",
        "a": "Voor alle drie. Bar & Lounge AI+ begrijpt van IBA-klassiekers tot avant-garde: shrubs, infusies, fermentaties, schuimen, gecontroleerde rook, geavanceerde barttechniek."
      },
      {
        "q": "Deckt het ook wijnen en bieren naast cocktails?",
        "a": "Ja. De agent dekt het hele spectrum van de bar: cocktails, wijnen, bieren, sterke drank, alcoholvrij en pairings."
      },
      {
        "q": "Maakt het mogelijk om drankkaarten met storytelling en techniek te creëren?",
        "a": "Ja. De fiches bevatten recept, techniek, garnish, glaswerk, verhaal en pairing klaar voor de zaal. Ideaal om de gemiddelde ticket te verhogen door de prijs te rechtvaardigen."
      },
      {
        "q": "Genereert het visuele content voor Instagram en de kaart?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van elk drankje voor Instagram, web en kaart; InstaFlow AI Pro plant content met een redactionele kalender. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echt gepresenteerde cocktail."
      },
      {
        "q": "Hoe helpt het mij met de seizoensgebondenheid van de kaart?",
        "a": "Gastro Calendar plant de seizoenskaarten (zomer, herfst, kerst, Valentijn) vooraf. Het Kit Plan Financiero projecteert een realistische seizoenscashflow zodat u met voorraad en kas bij elke piek aankomt."
      }
    ],
    "ctaTitle": "Uw cocktailbar met reële marge en signature techniek.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Bartenders en Mixologen: Kaarten, Kostprijsberekeningen en Storytelling | AI Chef Pro",
      "description": "AI-suite voor professionele bartenders: Bar & Lounge AI+, Food Pairing AI, kostprijs per drankje, technische fiches met storytelling en visuele branding. Start vandaag.",
      "keywords": "AI bartender, AI mixoloog, cocktailsoftware, cocktail kostprijsberekening, food pairing AI, cocktailkaart AI, mixoloog AI, signature cocktail",
      "ogImage": "https://aichef.pro/og/use-cases/bartender-coctelero.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw bar vanaf de eerste minuut",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type bar u runt (signature cocktailbar, wijnbar, hotelbar, lounge, restaurant met cocktails), teamgrootte, stad en kaartstijl. Elke agent — van Bar & Lounge AI+ tot Gastro Calendar — reageert aangepast aan uw product, markt en reële operatie.",
    "appsTitle": "De AI-agenten die u in uw bar gaat gebruiken",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Culinaire Creativiteit",
        "description": "Agent gespecialiseerd in professionele cocktails, wijnen, bieren en sterke drank met geavanceerde techniek."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Onverwachte combinaties met wetenschappelijke basis en cocktail + gerecht pairings."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van signature drankjes met recept + kostprijs CSV."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus voor geavanceerde texturen, geleermiddelen en signature barttechnieken."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de tSpoonLab-catalogus voor geavanceerde mixologietoepassingen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Mermengegevens in de bar: breuk, over-pour, verdamping, verspilde garnishes."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per drankje: sulfieten, zuivel, noten, gluten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-gastronomische referentiefotografie voor web, sociale media en cocktailkaart."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met professionele redactionele kalender voor signature cocktails."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Lokale klanten aantrekken die zoeken naar \"cocktailbar in de buurt\" op Google en Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Planning van seizoenskaarten: zomer, winter, Valentijn, Kerst."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Social Media",
        "description": "Pinterest genereert stabiel organisch verkeer voor cocktails met storytelling."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na kostprijsberekening van de kaart"
      },
      {
        "value": "×3",
        "label": "engagement Instagram met GastroIMG"
      },
      {
        "value": "−1 dag",
        "label": "afronding van seizoenskaart (van 7 naar 1)"
      },
      {
        "value": "12+",
        "label": "agenten voor uw bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Kaarten afgerond in een week van servetten en rekenmachine",
        "Kostprijsberekeningen zonder reële food cost per drankje, signatures met verlies zonder het te weten",
        "Technische fiches bestaan niet: elke barman repliceert zo goed als hij kan",
        "Mermen in de bar zonder echte traceerbaarheid",
        "Geïmproviseerde Instagram met mobiele foto's zonder continuïteit"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Seizoenskaart afgerond in één dag met professionele kostprijsberekening en storytelling",
        "Reële food cost per drankje, signatures met gevalideerde marge",
        "Technische fiches met recept, techniek, garnish, glaswerk, pairing en storytelling",
        "Mermen beheerst met Mermas GenCal en specifieke barsjablonen",
        "Instagram met professionele redactionele kalender en GastroIMG Gen+"
      ]
    },
    "galleryTitle": "Hoe een Signature Bar Werkt",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: bar, cocktails, techniek, mise, ingrediënten en team. Afbeeldingen gegenereerd met AI als visuele referentie van het concept.",
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
    "h1": "AI voor pizzabakkers en pizzaioli",
    "heroSubtitle": "Optimaliseer deeg en fermentaties, bereken elke pizza met werkelijke kosten, beheers oventechniek en operatie met een suite van gastronomische AI-agenten gespecialiseerd in professionele Italiaanse keuken.",
    "heroTagline": "Pizza met authentieke techniek en echte marge",
    "badge": "Voor pizzabakkers, pizzaioli en pizzeriaeigenaren",
    "painsTitle": "Waar een pizzabakker niet omheen kan",
    "pains": [
      "Het standaardiseren van deeg, hydratatie en fermentatie in elke dienst met technisch inzicht (napoletana, romana, in pala, Amerikaans)",
      "Het doorrekenen van pizza's met veel toppingvarianten en het consistent houden van de foodcost tussen alle menuopties.",
      "Verliezen in deeg (overfermentatie, mislukt vormen), mozzarella (vocht, verdamping) en sauzen.",
      "Het handhaven van consistente kwaliteit in de oven (hout, elektrisch, gas) met hoge pieken in de vraag in het weekend.",
      "Zich onderscheiden in een competitieve omgeving met signature pizza's, premium meel en visuele storytelling.",
      "Het binnenhalen van delivery-bestellingen met marge terwijl u de zaak met bediening in de eetzaal beheert."
    ],
    "featuresTitle": "Hoe AI Chef Pro een pizzabakker helpt",
    "features": [
      {
        "icon": "Pizza",
        "title": "Italiaanse Keuken",
        "description": "Agent gespecialiseerd in professionele Italiaanse keuken: deeg (napoletana, romana, in pala, Amerikaans), sauzen, toppings en oventechniek."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Voor zuurdesem, prefermenten (biga, poolish), hoge hydrataties en lange, gecontroleerde koude fermentaties."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening per pizza",
        "description": "Italiaanse Keuken levert recept + CSV-kostprijsberekening; Kit de Escandallos Pro beheert dit met werkelijke kosten per pizza, foodcost % en adviesprijs."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pizzería",
        "description": "Sjablonen: mise-en-place van deeg, prep van sauzen, mise-en-place van toppings, bediening in de eetzaal, delivery, sluiting en ovenreiniging."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC pizzeria",
        "description": "Traceerbaarheid van meel, zuurdesem, mozzarella, sauzen en kritische temperaturen in oven en koelcel."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planning van seizoenskaart: zomerpizza's met verse tomaat, herfst met paddenstoelen en truffel, speciaal voor Valentijnsdag en evenementen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "AI-referentiefotografie voor gastronomie + Instagram met redactionele kalender: de pizzeria leeft van visuele impact."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Lokale klanten aantrekken die \"pizzeria in de buurt\" zoeken op Google en Maps met geoptimaliseerde beschrijvingen."
      },
      {
        "icon": "Sparkles",
        "title": "Mermas GenCal",
        "description": "Nauwkeurige verliesgegevens per proces (deeg, mozzarella, restjes, delivery) geïntegreerd in de kostprijsberekening."
      }
    ],
    "workflowTitle": "Een echte dag van een pizzabakker met AI Chef Pro",
    "workflow": [
      "08:00 · Opening — checklist Kit de Tareas Pizzería: verfrissen van zuurdesem of biga, prep van San Marzano tomatensaus, gecontroleerde fermentatie van deegballen.",
      "10:00 · Italiaanse Keuken — u ontwikkelt een nieuwe seizoenspizza (geroosterde pompoen, gorgonzola, honing en walnoot) met technisch inzicht. Creatieve Keuken levert recept + CSV-kostprijsberekening.",
      "11:00 · Fermentus Con AI+ — u stelt de hydratatie in op 70 % en koude fermentatietijden van 48 uur voor het napolitaanse deeg.",
      "12:00 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke prijzen van caputo-meel, mozzarella di bufala en toppings, valideert marge en foodcost %.",
      "13:00 · Middagdienst — het team werkt met mise-en-place- en prep-sjablonen, gecoördineerde pieken.",
      "17:00 · Pauze tussen diensten — Gastro Calendar plant de herfstkaart en evenementen.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de referentieafbeelding van de nieuwe pizza en de berichten voor Instagram.",
      "23:00 · Sluiting — grondige reiniging van de oven, APPCC ondertekend, deegvoorbereiding voor morgen."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor pizzeria's",
    "productIds": [
      "kit-tareas-pizzeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "We hebben pizza voor pizza doorgerekend en ontdekt dat 4 verliesgevend waren ondanks dat ze goed verkochten. We hebben ze opnieuw ontworpen met Italiaanse Keuken, toppings vereenvoudigd zonder identiteit te verliezen en de marge met 4 punten verhoogd zonder de prijs te wijzigen. Fermentus veranderde ons deeg: 70 % hydratatie, 48 uur fermentatie, perfecte kruimstructuur.",
    "testimonialAuthor": "Giovanni Russo",
    "testimonialRole": "Pizzaiolo en eigenaar, Napolitaanse pizzeria",
    "faqTitle": "Veelgestelde vragen van pizzabakkers",
    "faqs": [
      {
        "q": "Werkt het voor napoletana, romana, in pala of Amerikaanse pizza?",
        "a": "Voor alle vier. Italiaanse Keuken en Fermentus dekken het hele spectrum van deeg (kruimstructuur, hydratatie, fermentaties), oventechnieken (hout, elektrisch, gas) en Italiaanse en Amerikaanse stijlen."
      },
      {
        "q": "Deckt het techniek van zuurdesem en prefermenten?",
        "a": "Ja. Fermentus Con AI+ begrijpt biga, poolish, vloeibaar en vast zuurdesem, hoge hydrataties en gecontroleerde koude fermentaties. Het redeneert als een professionele pizzaiolo, niet als YouTube-recepten."
      },
      {
        "q": "Deckt het ook delivery naast de eetzaal?",
        "a": "Ja. De Kit de Tareas Pizzería bevat specifieke sjablonen voor delivery: temperaturen, verpakking die de garing behoudt, transportverliezen en pickup-procedures."
      },
      {
        "q": "Genereert het visuele content voor Instagram, Glovo en Uber Eats?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen voor Instagram, deliveryplatforms en de menukaart; betere foto = meer klikken en betere ranking. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw versgebakken pizza."
      },
      {
        "q": "Hoe helpt het mij met seizoensgebondenheid en evenementen?",
        "a": "Gastro Calendar plant de seizoenskaarten (zomer, herfst met paddenstoelen en truffel, speciaal voor Valentijnsdag, Pasen, Kerstmis). Het Kit Plan Financiero projecteert de realistische seizoenscashflow zodat u met voldoende voorraad en kasgeld elke piek haalt."
      }
    ],
    "ctaTitle": "Uw pizzeria met echte marge en authentieke techniek.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor 10 € per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor pizzabakkers en pizzaioli: Deeg, Kostprijsberekeningen en Italiaanse Techniek | AI Chef Pro",
      "description": "AI-suite voor professionele pizzabakkers: Italiaanse Keuken, Fermentus voor deeg en biga, kostprijsberekeningen per pizza, sjablonen en authentieke techniek. Begin vandaag.",
      "keywords": "AI pizzabakker, AI pizzaiolo, pizzeria software, pizza kostprijsberekening, zuurdesem pizza, biga poolish pizza, napolitaanse techniek, pizza romana AI",
      "ogImage": "https://aichef.pro/og/use-cases/pizzero.jpg"
    },
    "personalizationTitle": "Vanaf de eerste minuut afgestemd op uw pizzeria",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type pizzeria u runt (authentieke napoletana, romana al taglio, Amerikaans, gemengd met Italiaanse keuken, dark kitchen voor delivery), teamgrootte, stad en type oven. Elke agent — van Italiaanse Keuken tot Gastro Calendar — reageert afgestemd op uw product, markt en werkelijke operatie.",
    "appsTitle": "De AI-agenten die u in uw pizzeria gaat gebruiken",
    "apps": [
      {
        "name": "Italiaanse Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Agent gespecialiseerd in professionele Italiaanse keuken: deeg, sauzen, toppings, oventechniek."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Zuurdesem, biga, poolish, hoge hydrataties, lange gecontroleerde fermentaties."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van signature pizza's met recept + CSV-kostprijsberekening."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus voor technische meelsoorten, verbeteraars en geavanceerde combinaties."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen in deeg, mozzarella, saus, restjes en delivery geïntegreerd in de kostprijsberekening."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per pizza: gluten, zuivel, noten, ei."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-referentiefotografie voor gastronomie voor Glovo, Uber Eats, website en sociale media."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met professionele redactionele kalender voor een signature pizzeria."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Lokale klanten aantrekken die \"pizzeria in de buurt\" zoeken op Google en Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Planning van seizoenskaart: zomer, herfst, Valentijnsdag, Kerstmis."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Social Media",
        "description": "Pinterest genereert stabiel organisch verkeer voor pizza's met storytelling."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "SEO-artikelen over Italiaanse techniek, deeg en pairing om verkeer aan te trekken."
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "marge na het doorrekenen van pizza's"
      },
      {
        "value": "×3",
        "label": "Instagram-engagement met GastroIMG"
      },
      {
        "value": "−25 %",
        "label": "verliezen in deeg en mozzarella"
      },
      {
        "value": "12+",
        "label": "agenten voor uw pizzeria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerd deeg per dienst: inconsistente kruimstructuur en ongelijke knapperigheid",
        "Kostprijsberekeningen zonder echte foodcost, pizza's verliesgevend zonder dat u het weet",
        "Verliezen in deeg, mozzarella en saus zonder traceerbaarheid",
        "Geïmproviseerde Instagram en deliveryplatforms met mobiele foto's",
        "APPCC op losse printpapieren verspreid door de pizzeria"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Deeg met technisch inzicht: consistente hydratatie, fermentatie en bakproces",
        "Professionele kostprijsberekening per pizza met gevalideerde marge en foodcost %",
        "Gecontroleerde verliezen met Mermas GenCal en specifieke sjablonen",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO trekken lokale klanten en delivery aan",
        "APPCC vanaf mobiel met registraties klaar voor inspectie"
      ]
    },
    "galleryTitle": "Hoe een authentieke pizzeria werkt",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: deeg, oven, techniek, ingrediënten, pizza's en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor de Ambachtelijke Bakker",
    "heroSubtitle": "Optimaliseer zuurdesem en preferments, kostenberekening per stuk met uurtarief van de bakkerij, beheers lange fermentaties en de dagelijkse gang van zaken met een pakket van gespecialiseerde culinaire AI-agenten voor ambachtelijk brood.",
    "heroTagline": "Ambachtelijk bakken met techniek en echte marge",
    "badge": "Voor ambachtelijke bakkers en bakkerijen",
    "painsTitle": "Wat een Ambachtelijke Bakker Niet Kan Nalaten Op te Lossen",
    "pains": [
      "Het standaardiseren van zuurdesem, preferments (biga, poolish), hydrataties en lange fermentatieprocessen in elke dienst",
      "Het berekenen van stukken met werkelijke kosten inclusief uren van de bakkerij (verversen, kneden, vormen, bakken kost tijd)",
      "Verspilling bij deeg, preferments, vormresten en mislukt gebak",
      "Productie afgestemd op de dagelijkse vraag zonder overproductie of voorraadtekorten voor sluitingstijd",
      "Je onderscheiden in een concurrerende omgeving met premium meel, oude granen en ambachtelijke branding",
      "Het binnenhalen van opdrachten van lokale horeca (restaurants, lunchrooms) met marge terwijl u de directe verkoop beheert"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Bakker Helpt",
    "features": [
      {
        "icon": "Wheat",
        "title": "Creatieve Bakkerij",
        "description": "Gespecialiseerde agent voor professioneel ambachtelijk brood: zuurdesems, hoge hydrataties, vlechttechniek en bakken op de ovenbodem."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Voor vloeibare en vaste zuurdesems, preferments (biga, poolish), gecontroleerde koude lange fermentaties en geavanceerde techniek."
      },
      {
        "icon": "Cake",
        "title": "Creatieve Patisserie",
        "description": "Voor bakkerijen die brood combineren met banket en gebak: brioche, croissants, ensaimadas en ambachtelijk banket."
      },
      {
        "icon": "Calculator",
        "title": "Kostenberekening per stuk met uurtarief van de bakkerij",
        "description": "Creatieve Keuken levert recept + kostenberekening CSV; Kit de Escandallos Pro beheert dit met het uurtarief van de bakkerij, verwerkt in de werkelijke marge per brood, stokbrood of brioche."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Obrador",
        "description": "Sjablonen: zuurdesem verversen, preferments, kneden, fermentaties, vormen, bakken, vitrine en conservering."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC bakkerij",
        "description": "Traceerbaarheid van meel, zuurdesem, preferments, conservering en kritische temperaturen in de rijsruimte."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Seizoensplanning met belangrijke data: Pasen (mona's, paasbrood), Kerst (Roscón, panettone), Sint-Jan, lokale evenementen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "AI-referentiefoodfotografie + Pinterest, waar ambachtelijk brood stabiel organisch verkeer oplevert."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Lokale SEO",
        "description": "Lokale klanten aantrekken die op Google en Maps zoeken naar \"ambachtelijke bakkerij in de buurt\"."
      }
    ],
    "workflowTitle": "Een Echte Dag van een Bakker met AI Chef Pro",
    "workflow": [
      "04:00 · Opening — checklist Kit de Tareas Obrador: zuurdesem verversen, controle van de fermentatie van de afgelopen nacht, het aanzetten van de oven.",
      "05:30 · Vormen en bakken — vormen van broden, stokbroden en brioches met specifieke mallen, controle van restverspilling.",
      "08:00 · Vitrine bijvullen — eerste batch klaar voor directe verkoop en bestellingen voor lokale horeca.",
      "10:00 · Creatieve Bakkerij — u ontwikkelt een nieuw brood met oude granen en vloeibare zuurdesem. Creatieve Keuken levert recept + kostenberekening CSV.",
      "11:00 · Fermentus Con AI+ — u past de hydratatie aan naar 80% en koude fermentatie van 24 uur voor het nieuwe brood.",
      "12:00 · Kit de Escandallos Pro — u uploadt de CSV met uw werkelijke prijzen voor biologisch meel en het uurtarief van de bakkerij, valideert de marge.",
      "15:00 · GastroIMG Gen+ + Pinterest Pins Gen — u genereert de referentieafbeelding van het nieuwe brood en de pins om organisch verkeer aan te trekken.",
      "20:00 · Sluiting — schoonmaken, HACCP ondertekend, deeg voorbereiden voor de nachtelijke fermentatie."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor de Bakkerij",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "We zijn overgestapt van losse vellen naar een systeem. We weten precijk welk stuk rendeert en welk niet, inclusief het uurtarief van de bakkerij. De verspilling daalde met 30% in 3 maanden en we ontdekten dat twee historische broden niet rendabel waren zonder uurtarief — we hebben ze opnieuw ontworpen door het proces te vereenvoudigen zonder kwaliteitsverlies en de marge met 5 punten verhoogd.",
    "testimonialAuthor": "Ana Iglesias",
    "testimonialRole": "Ambachtelijk bakker, eigen bakkerij",
    "faqTitle": "Veelgestelde Vragen van Bakkers",
    "faqs": [
      {
        "q": "Deckt het professionele zuurdesemtechniek?",
        "a": "Ja. Creatieve Bakkerij en Fermentus redeneren als een professionele bakker: verversen met inoculatiepercentage, hydrataties per broodingrediënt, gecontroleerde koude fermentaties van 24-48 uur, balans van stammen. Geen YouTube-recepten."
      },
      {
        "q": "Is het geschikt voor een kleine of industriële bakkerij?",
        "a": "Voor beide. De sjablonen schalen op van een familiebedrijf met 2 personen tot industriële productie. De methodiek is hetzelfde: recept → kostenberekening CSV met uurtarief van de bakkerij → werkelijke marge."
      },
      {
        "q": "Deckt het ook banket en gebak naast brood?",
        "a": "Ja. Creatieve Patisserie vult de catalogus aan als u brioche, croissants, ensaimadas, paasbrood of koekjes maakt. Fermentus Con AI+ dekt het gefermenteerde deel met professionele techniek."
      },
      {
        "q": "Genereert het visuele content voor vitrine, Instagram en Pinterest?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van het brood voor vitrine, website en sociale media; Pinterest Pins Gen trekt stabiel organisch verkeer aan waar de ambachtelijke bakkerij veel profijt van heeft. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw versgebakken brood."
      },
      {
        "q": "Hoe helpt het mij met seizoensgebondenheid en evenementen?",
        "a": "Gastro Calendar plant de belangrijkste seizoenen (Pasen met mona's en paasbrood, Kerst met Roscón en panettone, Sint-Jan, lokale evenementen) ruim van tevoren. Het Kit Plan Financiero projecteert een realistische seizoensgebonden cashflow."
      }
    ],
    "ctaTitle": "Uw ambachtelijke bakkerij met duidelijke marge en professionele techniek.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschap voor 10 € per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor de Ambachtelijke Bakker: Zuurdesem, Kostenberekeningen en Professionele Techniek | AI Chef Pro",
      "description": "AI-suite voor ambachtelijke bakkers: Creatieve Bakkerij, Fermentus Con AI+ voor zuurdesem, kostenberekeningen per stuk met uurtarief van de bakkerij. Begin vandaag.",
      "keywords": "AI bakker, ambachtelijke bakkerij AI, zuurdesem AI, bakkerijsoftware, kostenberekeningen bakkerij, fermentus, biga poolish, professionele bakker",
      "ogImage": "https://aichef.pro/og/use-cases/panadero.jpg"
    },
    "personalizationTitle": "Vanaf Minuut Eén Aangepast aan Uw Bakkerij",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversatiegerichte onboarding van 2 minuten waarin u vertelt wat voor soort bakkerij u runt (ambachtelijk met zuurdesem, traditionele bakkerij, bakkerij met banket, bakkerij met lunchroom, biologische bakkerij), teamgrootte, stad en specialiteit. Elke agent — van Creatieve Bakkerij tot Gastro Calendar — reageert afgestemd op uw product, markt en dagelijkse praktijk.",
    "appsTitle": "De AI-agenten die U in Uw Bakkerij Zult Gebruiken",
    "apps": [
      {
        "name": "Creatieve Bakkerij",
        "category": "Culinaire Creativiteit",
        "description": "Gespecialiseerde agent voor professioneel ambachtelijk brood, zuurdesems, hydrataties en techniek."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Zuurdesems, biga, poolish, hoge hydrataties en gecontroleerde lange fermentaties."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Brioche, croissants, ensaimadas en aanvullend ambachtelijk banket."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van signature broden met recept + kostenberekening CSV."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus: technische meelsoorten, verbetermiddelen, zaden en oude granen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Hulpmiddelen",
        "description": "Verspilling bij deeg, preferments, vormresten en bakken."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Hulpmiddelen",
        "description": "Automatische identificatie van allergenen per stuk: gluten, zuivel, noten, ei."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-referentiefoodfotografie voor vitrine, website en sociale media."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Sociale Media",
        "description": "Pinterest trekt stabiel organisch verkeer aan voor ambachtelijk brood."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Sociale Media",
        "description": "Instagram met professionele redactionele kalender voor ambachtelijke bakkerijen."
      },
      {
        "name": "MenuDish Lokale SEO",
        "category": "Content en Sociale Media",
        "description": "Lokale klanten aantrekken die op Google en Maps zoeken naar \"ambachtelijke bakkerij in de buurt\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Sociale Media",
        "description": "Seizoensplanning: Pasen, Kerst, Sint-Jan, lokale evenementen."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na het berekenen van stukken"
      },
      {
        "value": "−30 %",
        "label": "verspilling in de bakkerij en bij het bakken"
      },
      {
        "value": "×2",
        "label": "organisch verkeer via Pinterest"
      },
      {
        "value": "12+",
        "label": "agenten voor uw bakkerij"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerd zuurdesem, inconsistente fermentaties per dienst",
        "Kostenberekeningen zonder uurtarief van de bakkerij, complexe broden verlieslatend zonder het te weten",
        "Verspilling bij deeg, preferments en bakken zonder traceerbaarheid",
        "Geïmproviseerde vitrine en sociale media met telefoonfoto's",
        "HACCP op losse vellen verspreid door de bakkerij"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Zuurdesem met technisch inzicht: consistente verversingen, hydrataties en fermentaties",
        "Professionele kostenberekening per stuk met geïntegreerd uurtarief van de bakkerij",
        "Gecontroleerde verspilling met Mermas GenCal en specifieke sjablonen",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ trekken stabiel verkeer aan",
        "HACCP via de mobiele telefoon met registers klaar voor inspectie"
      ]
    },
    "galleryTitle": "Hoe een Ambachtelijke Bakkerij Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: vitrine, zuurdesem, fermentatie, broden, bakken en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor chocolatier en bonbonmaker",
    "heroSubtitle": "Ontwerp bonbons, repen en couverture met professionele kostprijsberekening, tempereertechniek en seizoensplanning met een suite van AI-agenten gespecialiseerd in ambachtelijke chocolaterie van de auteur.",
    "heroTagline": "Chocolaterie met authentieke techniek en echte marge",
    "badge": "Voor chocolatiers, bonbonmakers en meester-chocolatiers",
    "painsTitle": "Wat een chocolatier niet kan nalaten op te lossen",
    "pains": [
      "Cacao met een volatiele prijs die de werkelijke kostprijs elke week verandert zonder waarschuwing en dwingt om constant kostprijzen te herberekenen",
      "Veeleisende tempereertechniek: kristallisatie in V-vorm, precieze curven afhankelijk van de couverture, consistente glans en snap",
      "Verliezen in de werkplaats (mislukt tempereren, restjes, slecht uitgeharde mallen, schokken) die de winstgevendheid zonder controle laten bloeden",
      "Extreme seizoensgebondenheid: Kerst, Valentijnsdag, Pasen en Driekoningen concentreren een hoog percentage van de jaaromzet",
      "Zich onderscheiden in een concurrerend gebied met bonbons van de auteur, premium verpakking en visuele merkverhalen",
      "Bedrijfsopdrachten, bruiloften en evenementen binnenhalen met marge terwijl de dagelijkse productie wordt beheerd"
    ],
    "featuresTitle": "Hoe AI Chef Pro een chocolatier helpt",
    "features": [
      {
        "icon": "Cookie",
        "title": "Creatieve Chocolaterie",
        "description": "Agent gespecialiseerd in professionele chocolaterie: bonbons, ganaches, pralinés, repen, couvertures, tempereertechniek en kristallisatiecurven."
      },
      {
        "icon": "Cake",
        "title": "Creatieve Patisserie",
        "description": "Voor chocoladedesserts, hapjes, brownies, mousses en geavanceerde combinaties chocolade + patisserie."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijs per stuk met werkplaatsuurtarief",
        "description": "Creatieve Keuken levert recept + kostprijs-CSV; Kit de Escandallos Pro beheert dit met geïntegreerd werkplaatsuurtarief in de werkelijke marge per bonbon en per doos."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients Agent",
        "description": "Assistent van de Sosa-catalogus voor technische couvertures, geconcentreerde pasta's, noten en professionele aroma's."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chocolatería",
        "description": "Sjablonen: tempereren, vormen, ganaches, assemblage, verpakking, temperatuurcontrole in de koeling."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC chocolaterie",
        "description": "Traceerbaarheid van cacao, zuivel, noten, alcohol en professionele bewaring met gedocumenteerde curven."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Seizoensplanning met belangrijke data: Kerst, Valentijnsdag, Pasen, Driekoningen, Moederdag. Redactionele kalender."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "AI-referentiefotografie van de auteur + Pinterest, waar premium chocolaterie stabiel organisch verkeer vastlegt."
      },
      {
        "icon": "Sparkles",
        "title": "Mermas GenCal",
        "description": "Precieze verliesgegevens per proces (tempereren, vormen, restjes, expositie) geïntegreerd in de kostprijs."
      }
    ],
    "workflowTitle": "Een echte dag van een chocolatier met AI Chef Pro",
    "workflow": [
      "07:00 · Opening — checklist Kit de Tareas Chocolatería: controle van de koeling, pre-kristallisatie van couverture, voorbereiding van polycarbonaat mallen.",
      "08:30 · Creatieve Chocolaterie — u ontwikkelt een nieuwe signature bonbon met gekarameliseerde hazelnootpraliné en Maldon-zout. Creatieve Keuken levert recept + kostprijs-CSV.",
      "09:30 · Sosa Ingredients Agent — u selecteert technische couverture met het juiste cacaopercentage, extra cacaoboter en kwaliteitszout.",
      "10:00 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke cacaoprijzen en geïntegreerd werkplaatsuurtarief, valideert de marge per bonbon en per doos van 9 stuks.",
      "11:00 · Productie van de dag — tempereren op marmer, vormen, ganache, vullen, schokken en ontvormen.",
      "14:00 · Aanvulling — voorbereiding van professionele cadeauverpakkingen, etikettering en verliescontrole.",
      "16:00 · Gastro Calendar — u bereidt de kerstplanning voor met bedrijfsdozen (8 weken van tevoren).",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — u genereert een referentieafbeelding van de nieuwe signature en geoptimaliseerde pins voor Pinterest.",
      "20:00 · Afsluiting — grondige reiniging, APPCC ondertekend, planning van mengsels om te schokken."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor chocolaterie",
    "productIds": [
      "kit-tareas-chocolateria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "12.000 bonbons produceren voor Kerst zonder systeem was chaos. Met Creatieve Chocolaterie voor ontwerp, Sosa Ingredients Agent voor technische couverture, Kit de Escandallos Pro voor echte marge met actuele cacao en Gastro Calendar voor seizoensplanning, hebben we het seizoen gered en de marge met 7 punten verhoogd. De bedrijfsdozen worden afgesloten in één gesprek met een professioneel voorstel.",
    "testimonialAuthor": "Mónica Salazar",
    "testimonialRole": "Meester-chocolatier en eigenaresse",
    "faqTitle": "Veelgestelde vragen van chocolatiers",
    "faqs": [
      {
        "q": "Omvat het professionele tempereertechniek en kristallisatiecurven?",
        "a": "Ja. Creatieve Chocolaterie redeneert als een professionele chocolatier: tempereren van couverture volgens curven (45-27-31 °C voor donkere couverture), tabling-techniek op marmer, enten, magnetron met extra cacaoboter. Geen YouTube-recepten."
      },
      {
        "q": "Is het geschikt voor kleine ambachtelijke chocolaterie, atelier van de auteur of bonbonfabriek met productie op schaal?",
        "a": "Voor alle drie. De sjablonen schalen van een familiebedrijf tot productie voor meerdere verkooppunten of bedrijfsdozen met honderden eenheden."
      },
      {
        "q": "Hoe beheert u de volatiele cacaoprijs?",
        "a": "Kit de Escandallos Pro herberekent onmiddellijk de werkelijke marge wanneer u de prijs van de couverture bijwerkt. Mermas GenCal voegt de kosten van verliezen per proces toe. De marge weerspiegelt altijd de actuele kostprijs."
      },
      {
        "q": "Genereert het inhoud voor vitrine, sociale media en verpakking?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van elke bonbon voor vitrine, web en sociale media; Pinterest Pins Gen + InstaFlow AI Pro plannen visuele inhoud; MenuDish Local SEO trekt lokale klanten aan. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte bonbon op het bord."
      },
      {
        "q": "Hoe helpt het u met de sterke seizoensgebondenheid?",
        "a": "Gastro Calendar plant de belangrijkste seizoenen (Kerst, Valentijnsdag, Pasen, Driekoningen, Moederdag) met 8-12 weken vooruit. Het Kit Plan Financiero projecteert de realistische seizoenscashflow zodat u met productie en kas bij elke piek aankomt."
      }
    ],
    "ctaTitle": "Uw chocolaterie met duidelijke marge en authentieke techniek.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Chocolatier en Bonbonmaker: Tempereren, Kostprijzen en Seizoensgebondenheid | AI Chef Pro",
      "description": "AI-suite voor professionele chocolatiers: Creatieve Chocolaterie, kostprijs per stuk met werkplaatsuurtarief, seizoensplanning en APPCC. Begin vandaag.",
      "keywords": "AI chocolatier, AI bonbonmaker, software chocolaterie, kostprijs bonbon, ambachtelijke chocolaterie AI, tempereertechniek, kristallisatiecurven, meester-chocolatier",
      "ogImage": "https://aichef.pro/og/use-cases/chocolatero.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd naar uw atelier vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor soort chocolaterie u runt (ambachtelijk atelier, bonbonfabriek met productie op schaal, chocolaterie met café, werkplaats voor verkoop aan de horeca, chocolaterie met ervaringen en proeverijen), teamgrootte, stad en specialiteit. Elke agent —van Creatieve Chocolaterie tot Gastro Calendar— reageert aangepast aan uw product, markt en werkelijke operatie.",
    "appsTitle": "De AI-agenten die u in uw atelier gaat gebruiken",
    "apps": [
      {
        "name": "Creatieve Chocolaterie",
        "category": "Culinaire Creativiteit",
        "description": "Agent gespecialiseerd in professionele chocolaterie: bonbons, ganaches, pralinés, repen en tempereertechniek."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Chocoladedesserts, hapjes, brownies, mousses en geavanceerde combinaties."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van signature bonbons met recept + kostprijs-CSV."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus: technische couvertures, geconcentreerde pasta's, noten en professionele aroma's."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de tSpoonLab-catalogus voor geavanceerde chocolatietoepassingen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen bij tempereren, vormen, restjes en expositie geïntegreerd in de kostprijs."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per bonbon: zuivel, noten, gluten, alcohol."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-referentiefotografie van de auteur voor vitrine, web, verpakking en sociale media."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Sociale Media",
        "description": "Pinterest legt stabiel organisch verkeer vast voor premium chocolaterie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Sociale Media",
        "description": "Instagram met redactionele kalender voor chocolaterie van de auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Sociale Media",
        "description": "Lokale klanten aantrekken die zoeken naar \"ambachtelijke chocolaterie in de buurt\" op Google en Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Sociale Media",
        "description": "Seizoensplanning: Kerst, Valentijnsdag, Pasen, Driekoningen, Moederdag."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "marge na kostprijsberekening van bonbons"
      },
      {
        "value": "−35 %",
        "label": "verliezen in werkplaats en vitrine"
      },
      {
        "value": "×2",
        "label": "bedrijfsopdrachten Kerst"
      },
      {
        "value": "12+",
        "label": "agenten voor uw atelier"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerd tempereren: inconsistente glans en snap per stuk",
        "Volatiele cacao die de prijzen ontregelt zonder realtime herberekening",
        "Verliezen bij tempereren, vormen en vitrine zonder echte traceerbaarheid",
        "Reactieve seizoensproductie: u komt te laat voor Kerst en verliest bedrijfsopdrachten",
        "APPCC op los papier verspreid door het atelier"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Tempereren volgens curven met technisch inzicht, consistente glans en snap",
        "Professionele kostprijs per bonbon met bijwerkbare cacao en geïntegreerd uurtarief",
        "Verliezen gecontroleerd met Mermas GenCal en specifieke sjablonen",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ trekken stabiel verkeer en opdrachten aan",
        "APPCC vanaf mobiel met registraties klaar voor inspectie"
      ]
    },
    "galleryTitle": "Hoe een chocolaterie-atelier werkt",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: tempereren, vormen, bonbons, ganache en apparatuur. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Privé Chef en Personal Chef",
    "heroSubtitle": "Ontwerp gepersonaliseerde menu's voor unieke klanten, bereken elk privédiner met werkelijke kostprijs, plan de mise in particuliere woningen en verwerf professionele branding met een suite van culinaire AI-agenten gespecialiseerd in privékoks en service in particuliere woningen.",
    "heroTagline": "Privédienst met reële marge en signatuurtechniek",
    "badge": "Voor privékoks, personal chefs en intieme catering",
    "painsTitle": "Wat een Privé Chef Niet Kan Nalaten op te Lossen",
    "pains": [
      "Volledig gepersonaliseerde menu's per klant ontwerpen: allergieën, intoleranties, voorkeuren, dieet, gelegenheid en esthetiek van de opmaak",
      "Elk privédiner berekenen met werkelijke kostprijs (dagelijkse aankoop, premium ingrediënten) en gepersonaliseerde prijs",
      "Mise plannen in particuliere woningen met niet-professionele keukens (geen apparatuur, beperkte ruimte, onbekende kookplaten)",
      "Technische fiches standaardiseren zodat de klant het menu kan herhalen of het recept als aandenken kan bewaren",
      "Zich onderscheiden in een competitief gebied met persoonlijke storytelling, visuele signatuur-branding en acquisitie via sociale media",
      "Terugkerende premium klanten aantrekken (VIP-families, directieleden, beroemdheden) met professionele en gepersonaliseerde voorstellen"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Privé Chef Helpt",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Privé Chef Pro",
        "description": "Gespecialiseerde agent uit de catalogus Gastro Profile Pro: redeneert als een professionele personal chef met ervaring in particuliere woningen en intieme evenementen."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor het ontwikkelen van gepersonaliseerde menu's met geavanceerde techniek: signatuuropmaken, gecontroleerde fusies, signature desserts."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Gepersonaliseerde combinaties met de wijnkelder van de klant of wijnvoorstellen voor elk gerecht van het privémodel."
      },
      {
        "icon": "Calculator",
        "title": "Calcula Pax + Escandallos",
        "description": "Calcula Pax schaalt recepten op naar 2, 6, 12 gasten; Kit de Escandallos Pro beheert dit met werkelijke kostprijs per privédiner en gepersonaliseerde prijs."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chef Privé",
        "description": "Sjablonen: voorbezoek aan de keuken van de klant, boodschappenlijst, verplaatsbare mise, serviceplan, schoonmaak, factuur."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergenen ID",
        "description": "Automatische identificatie van allergenen per klant: cruciaal wanneer u werkt met gezinnen met specifieke intoleranties."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planning van seizoensmenu's en voor speciale gelegenheden: Kerst, Valentijn, jubilea, verjaardagen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Premium AI-referentiefotografie + Instagram om nieuwe klanten aan te trekken en een signaturereputatie op te bouwen."
      },
      {
        "icon": "BookOpen",
        "title": "Technisch blad + factuur",
        "description": "Professioneel sjabloon om aan de klant te overhandigen: technisch blad van het menu met recept + storytelling + duidelijke factuur."
      }
    ],
    "workflowTitle": "Een Echte Dag van een Privé Chef met AI Chef Pro",
    "workflow": [
      "07:00 · Voorbezoek — checklist Kit de Tareas Chef Privé: controle van de keuken van de klant (apparatuur, ruimte, bevestigde allergieën en voorkeuren).",
      "08:00 · Privé Chef Pro — u ontwikkelt het gepersonaliseerde menu voor een intiem diner voor 6 personen met notenallergie. Creatieve Keuken levert recept + kostprijsberekening CSV.",
      "09:00 · Calcula Pax — u schaalt de recepten op van 6 naar 8 gasten (klant voegde twee gasten toe). Kit de Escandallos Pro herberekent de kosten en het voorstel.",
      "10:00 · Boodschappenlijst — u gaat naar de markt met de geprioriteerde lijst: product van de dag, specifieke premium ingrediënten.",
      "14:00 · Aankomst bij de klant thuis — opbouwen van de mise in de particuliere keuken volgens het verplaatsbare plan, organisatie van de ruimte.",
      "17:00 · Dienstdiner — uitvoering van het menu met professionele techniek aangepast aan de keuken van de klant, opgemaakt op fijn porselein.",
      "21:00 · Afsluiting met de klant — overhandiging van het technisch blad van het menu met storytelling + professionele factuur + referentiefoto van het menu.",
      "23:00 · Na het diner — InstaFlow AI Pro: Instagram-post met de referentieafbeelding van het menu (zonder gezichten van de klant) om reputatie op te bouwen."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Privé Chef",
    "productIds": [
      "kit-tareas-chef-privado",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Privé Chef Pro heeft mijn commerciële voorstel veranderd. Nu krijgt elke klant een gepersonaliseerd menu met professionele kostprijsberekening en storytelling, en de acquisitie via Instagram met GastroIMG Gen+ is vermenigvuldigd. Ik sluit voorstellen af in één gesprek omdat ik dezelfde dag het technisch blad + factuur lever. We verhoogden de gemiddelde besteding met 35 % per diner.",
    "testimonialAuthor": "Andrea Gómez",
    "testimonialRole": "Freelance privékok, Madrid + kust",
    "faqTitle": "Veelgestelde Vragen van Privékoks",
    "faqs": [
      {
        "q": "Is het geschikt voor een freelance privékok, een personal chef-agentschap of intieme catering?",
        "a": "Voor alle drie. Privé Chef Pro redeneert als een professionele personal chef, het dient zowel voor de freelancer die zijn voorstel ontwerpt als voor agentschappen met meerdere koks."
      },
      {
        "q": "Hoe ga ik om met allergieën en speciale diëten per klant?",
        "a": "Allergenen ID identificeert automatisch allergenen per recept. Privé Chef Pro redeneert in termen van personalisatie: keto-, veganistische, glutenvrije, natriumarme, FODMAP-dieeten, zwangerschap. Elke klant krijgt een echt aangepast menu."
      },
      {
        "q": "Hoe schaal ik recepten op voor verschillende aantallen gasten?",
        "a": "Calcula Pax schaalt de recepten op naar 2, 6, 12 of elk ander aantal gasten zonder aan precisie in te boeten. Kit de Escandallos Pro herberekent de kostprijs per persoon en het financiële voorstel aan de klant."
      },
      {
        "q": "Genereert het visuele content voor Instagram en signaturereputatie?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van het menu (zonder de klant te tonen) voor Instagram, website en portfolio. Onthoud dat het AI-beeld een visuele referentie is: de definitieve foto maakt u zelf met uw echte opgemaakte gerecht tijdens elk diner."
      },
      {
        "q": "Hoe helpt het mij bij het aantrekken van terugkerende klanten?",
        "a": "GastroIMG Gen+ + InstaFlow AI Pro bouwen constante visuele content op; MenuDish Local SEO trekt lokale klanten aan die zoeken naar \"privékok in [stad]\"; Gastro Calendar helpt bij het voorstellen van seizoensmenu's (intiem kerstdiner, Valentijn, jubilea) voor klantenbinding."
      }
    ],
    "ctaTitle": "Uw privé chef-dienst met reële marge en een voorstel met signatuur.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor € 10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Privé Chef en Personal Chef: Menu's, Kostprijsberekeningen en Service | AI Chef Pro",
      "description": "AI-suite voor professionele privékoks: Privé Chef Pro, kostprijsberekeningen per diner, gepersonaliseerde menu's, branding en acquisitie. Begin vandaag.",
      "keywords": "AI privékok, AI personal chef, software privékok, kostprijsberekening privédiner, privékok, personal chef freelance",
      "ogImage": "https://aichef.pro/og/use-cases/chef-privado.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd naar Uw Privé Chef Dienst vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversatie-onboarding van 2 minuten waarin u vertelt welk type dienst u aanbiedt (freelance privékok, agentschap met meerdere koks, intieme catering voor bruiloften en privé-evenementen, scheepskok), type klantenkring (VIP-families, directieleden, beroemdheden), stad en specialiteit. Elke agent — van Privé Chef Pro tot Gastro Calendar — reageert afgestemd op uw voorstel en reële werkwijze.",
    "appsTitle": "De AI-agenten die u als Privé Chef zult gebruiken",
    "apps": [
      {
        "name": "Privé Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Gespecialiseerde agent uit de catalogus Gastro Profile Pro: redeneert als een professionele personal chef."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van gepersonaliseerde menu's met geavanceerde techniek en recept + kostprijsberekening CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Gepersonaliseerde combinaties met de wijnkelder van de klant of wijnvoorstellen."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en Hulpprogramma's",
        "description": "Opschalen van recepten voor verschillende aantallen gasten."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Hulpprogramma's",
        "description": "Automatische identificatie van allergenen per klant en recept."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools en Hulpprogramma's",
        "description": "Omzetter van gewichten en maten, cruciaal bij het werken met niet-professionele keukens."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Hulpprogramma's",
        "description": "Verliezen bij dagelijkse aankoop en premium product."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Premium AI-referentiefotografie voor Instagram, portfolio en acquisitie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Sociale Media",
        "description": "Instagram met professionele contentkalender om terugkerende klanten aan te trekken."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Sociale Media",
        "description": "Lokale klanten aantrekken die zoeken naar \"privékok in [stad]\" op Google en Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Sociale Media",
        "description": "Seizoensmenu's: intiem kerstdiner, Valentijn, jubilea, verjaardagen."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Zakelijke Concepten",
        "description": "Voor gepersonaliseerde cocktails tijdens privédiners."
      }
    ],
    "metrics": [
      {
        "value": "+35 %",
        "label": "gemiddelde besteding per privédiner"
      },
      {
        "value": "×3",
        "label": "klantenwerving via Instagram"
      },
      {
        "value": "×5",
        "label": "snelheid van commerciële voorstellen"
      },
      {
        "value": "12+",
        "label": "agenten voor uw privédienst"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Handmatig gepersonaliseerde menu's: een week per voorstel",
        "Kostprijsberekeningen zonder werkelijke kosten, commerciële voorstellen met onzekere marge",
        "Voorbezoek en mise elke keer geïmproviseerd thuis",
        "Acquisitie via mond-tot-mond, zonder consistente Instagram",
        "Geen technisch blad als aandenken voor de klant"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Gepersonaliseerd menu in een uur met Privé Chef Pro",
        "Professionele kostprijsberekening per diner met gevalideerde marge",
        "Voorbezoek en mise met verplaatsbaar sjabloon Kit de Tareas",
        "Constante acquisitie met GastroIMG Gen+ + InstaFlow AI Pro",
        "Technisch blad van het menu + factuur dezelfde dag overhandigd"
      ]
    },
    "galleryTitle": "Hoe de Privé Chef Dienst Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro zult coördineren: mise, opgemaakt bord, gedekte tafel, voorraadkast en service. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor de F&B-manager van het hotel",
    "heroSubtitle": "Coördineer restaurants, banketten, roomservice, ontbijtbuffetten en hotelbars met kruislingse kostprijsberekening, professionele operationele sjablonen en geïntegreerde branding met een suite van culinaire AI-agenten die gespecialiseerd zijn in integraal F&B-beheer voor de horeca.",
    "heroTagline": "Hotel-F&B met echte marge en professionele bedrijfsvoering",
    "badge": "Voor F&B-managers en directeuren van Food & Beverage",
    "painsTitle": "Waar een F&B-manager niet omheen kan",
    "pains": [
      "Het gelijktijdig coördineren van meerdere outlets (hoofdrestaurant, roomservice, ontbijtbuffet, zwembadbar, banketten, café)",
      "Het kruislings doorrekenen van de menukaart tussen outlets met behoud van consistentie in foodcost en geïntegreerde marge",
      "Hoog verlies in ontbijtbuffet (ruim aanbod met wisselende consumptie) en banketten (groot volume, logistieke complexiteit)",
      "Het standaardiseren van procedures per dienst met wisselende teams en drie dagelijkse services",
      "Je onderscheiden in een competitief hotel met een complete culinaire ervaring, visuele branding en hospitality-storytelling",
      "Het binnenhalen van zakelijke evenementen, bruiloften en premium banketten met professionele voorstellen en gevalideerde marge"
    ],
    "featuresTitle": "Hoe AI Chef Pro een F&B-manager helpt",
    "features": [
      {
        "icon": "Hotel",
        "title": "Pro Restaurant Manager",
        "description": "Gespecialiseerde agent uit de Gastro Profile Pro-catalogus, aangepast aan multi-outlet F&B-beheer in de hotellerie."
      },
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Professioneel advies voor banketten, bruiloften en zakelijke evenementen van het hotel."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor de ontwikkeling van geïntegreerde menu's: hoofdrestaurant, ontbijtbuffet, roomservice en zwembadbar met samenhang."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Voor de cocktails van de zwembadbar, de lobbybar en de wijn-spijscombinaties van het hoofdrestaurant."
      },
      {
        "icon": "Calculator",
        "title": "Kruislingse kostprijsberekening",
        "description": "Creatieve Keuken levert recept + kostprijsberekening CSV; Kit de Escandallos Pro beheert dit met kruislingse kosten tussen outlets en geïntegreerde marge."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Hotel Completo",
        "description": "Sjablonen voor 5 outlets: restaurant, ontbijt, roomservice, bar, banketten met procedures per dienst."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC hotelero",
        "description": "Traceerbaarheid van buffet, banketten, roomservice en bar met kritische temperaturen en bewaring."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planning van zakelijke evenementen, bruiloften, seizoenen (zomer/winter), Kerst, Valentijnsdag, conferenties."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Premium AI-referentiefotografie + Instagram voor alle hoteloutlets met merkconsistentie."
      }
    ],
    "workflowTitle": "Een Echte Dag van een F&B-manager met AI Chef Pro",
    "workflow": [
      "06:00 · Ontbijtopening — checklist Kit de Tareas Hotel: buffet voorbereiden, chafing dishes controleren, temperaturen, mise-en-place van het eierstation.",
      "09:00 · Afstemming met de hoofdkeuken — Creatieve Keuken werkt de lunchkaart bij met seizoensproducten. Recept + kostprijsberekening CSV.",
      "10:00 · Catering AI+ — u ontwikkelt het menuvoorstel voor een bruiloft voor 120 personen met drie gangen. Calcula Pax schaalt recepten, Kit de Escandallos Pro valideert kosten en marge.",
      "12:00 · Lunchservice in het hoofdrestaurant + roomservice — kruislingse coördinatie tussen outlets.",
      "14:00 · Bar & Lounge AI+ — u ontwikkelt de nieuwe cocktailkaart voor de zwembadbar van het zomerseizoen.",
      "17:00 · Zakelelijk banket voor 80 personen — uitvoering met het specifieke sjabloon van de Kit de Tareas.",
      "20:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert referentieafbeeldingen voor de vier outlets en consistente berichten voor de Instagram van het hotel.",
      "23:00 · Sluiting — grondige schoonmaak voor meerdere outlets, APPCC ondertekend, planning van ontbijt en services voor de volgende dag."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor F&B-managers",
    "productIds": [
      "kit-tareas-hotel",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Vijf outlets beheren zonder systeem was chaos. Pro Restaurant Manager + Catering AI+ coördineren voor ons de kruislingse menukaart, banketten en roomservice met geïntegreerde kostprijsberekening. De planning van bruiloften voor 120 personen die voorheen een week duurde, is nu een dag met een professioneel voorstel. We hebben de marge met 5 punten verhoogd door outlets te kruisen en sluiten premium evenementen veel sneller af.",
    "testimonialAuthor": "Roberto Castaño",
    "testimonialRole": "F&B-directeur, 5-sterrenhotel",
    "faqTitle": "Veelgestelde vragen van F&B-managers",
    "faqs": [
      {
        "q": "Is het geschikt voor een boetiekhotel, hotelketen, all-inclusive of luxehotel?",
        "a": "Voor alle vier. Pro Restaurant Manager + Catering AI+ + Bar & Lounge AI+ dekken alles af, van boetiekhotel met één restaurant tot 5-sterrenhotel met 5+ outlets, all-inclusive met uitgebreid buffet of vakantieresort."
      },
      {
        "q": "Hoe coördineer ik de kruislingse menukaart tussen outlets?",
        "a": "Creatieve Keuken redeneert samenhangend tussen outlets: product uit het hoofdmenu wordt benut bij het ontbijt, de roomservice en banketten, waardoor de geïntegreerde foodcost wordt geoptimaliseerd en kruislingse verliezen worden verminderd."
      },
      {
        "q": "Hoe schaal ik kostprijsberekeningen op voor banketten van 50, 100 of 300 personen?",
        "a": "Calcula Pax schaalt recepten op zonder aan precisie in te boeten; Kit de Escandallos Pro herberekent de kosten per persoon en het financiële voorstel voor de zakelijke of bruiloftsklant."
      },
      {
        "q": "Genereert het consistente visuele content voor de Instagram van het hotel?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen voor de vier outlets met merkconsistentie; InstaFlow AI Pro plant Instagram. Onthoud dat het AI-beeld een visuele referentie is: de uiteindelijke foto maakt u zelf met uw echte opgemaakte gerecht."
      },
      {
        "q": "Hoe helpt het mij met zakelijke evenementen en seizoenen?",
        "a": "Gastro Calendar plant zakelijke evenementen, bruiloften, conferenties, seizoenen (zomer/winter), Kerst en Valentijnsdag met specifieke menu's per outlet en een gecoördineerde redactionele kalender."
      }
    ],
    "ctaTitle": "Uw hotel-F&B met geïntegreerde marge en professionele bedrijfsvoering.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor € 10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor hotel-F&B-managers: multi-outlet, banketten en kostprijsberekening | AI Chef Pro",
      "description": "AI-suite voor hotel-F&B-managers: Pro Manager, Catering AI+, kruislingse kostprijsberekening, multi-outlet branding en geïntegreerde APPCC. Begin vandaag.",
      "keywords": "AI F&B manager, AI hotel F&B, software hotel restaurant, kostprijsberekening hotel, banketten hotel AI, ontbijtbuffet hotel",
      "ogImage": "https://aichef.pro/og/use-cases/fb-manager-hotel.jpg"
    },
    "personalizationTitle": "Vanaf minuut één afgestemd op uw hotel",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversatiegerichte onboarding van 2 minuten waarin u vertelt wat voor hotel u runt (boutique, keten, 5 sterren, all-inclusive, vakantieresort), aantal F&B-outlets, teamgrootte en specialisatie. Elke agent – van Pro Restaurant Manager tot Catering AI+ – reageert afgestemd op uw eigen hotel.",
    "appsTitle": "De AI-agenten die u als F&B-manager gaat gebruiken",
    "apps": [
      {
        "name": "Pro Restaurant Manager",
        "category": "Gastro Profile Pro",
        "description": "Gespecialiseerde agent aangepast aan multi-outlet F&B-beheer in de hotellerie."
      },
      {
        "name": "Catering AI+",
        "category": "Bedrijfsconcepten",
        "description": "Banketten, bruiloften en zakelijke evenementen van het hotel met professionele voorstellen."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Geïntegreerde menu's met samenhang tussen outlets en recept + kostprijsberekening CSV."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor de cocktails van de zwembadbar, lobbybar en wijn-spijscombinaties van het hoofdrestaurant."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor het casual restaurant en het café van het hotel."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en hulpprogramma's",
        "description": "Het opschalen van recepten voor banketten van 50, 100, 300 of 500 personen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpprogramma's",
        "description": "Verliezen in ontbijtbuffet, banketten en roomservice."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpprogramma's",
        "description": "Automatische identificatie voor gasten met allergieën bij banketten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Premium AI-referentiefotografie met merkconsistentie voor alle outlets."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en sociale media",
        "description": "Instagram met een gecoördineerde redactionele kalender voor alle outlets."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en sociale media",
        "description": "Lokale klanten aantrekken die op Google en Maps zoeken naar 'hotelrestaurant'."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en sociale media",
        "description": "Zakelijke evenementen, bruiloften, conferenties, Kerst, Valentijnsdag, seizoenen."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na kruislingse kostprijsberekening"
      },
      {
        "value": "×7",
        "label": "snelheid van banketvoorstellen"
      },
      {
        "value": "−25 %",
        "label": "verliezen in ontbijtbuffet"
      },
      {
        "value": "12+",
        "label": "agenten voor uw F&B"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Handmatig gecoördineerde outlets, kruislingse foodcost zonder traceerbaarheid",
        "Met de hand doorgerekende banketten: een week per bruiloft",
        "Verliezen in ontbijtbuffet zonder echte controle",
        "Verspreide visuele branding tussen outlets zonder samenhang",
        "APPCC op losse printjes verspreid over de outlets"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Outlets gecoördineerd met kruislingse kostprijsberekening en geïntegreerde foodcost",
        "Banketten in één dag doorgerekend met professioneel voorstel",
        "Verliezen gecontroleerd met Mermas GenCal bij ontbijt en banketten",
        "Consistente branding met GastroIMG Gen+ + InstaFlow AI Pro",
        "APPCC vanaf mobiel voor meerdere outlets met registraties klaar voor inspectie"
      ]
    },
    "galleryTitle": "Hoe de F&B van een hotel werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: restaurant, banketten, ontbijt, roomservice en zwembadbar. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Maître en Restaurantleider",
    "heroSubtitle": "Coördineer de service in de zaal met professionele techniek, beheer premium reserveringen en pairing, leid het team en creëer fine dining branding met een suite van gastronomische AI-agenten gespecialiseerd in zaal en hoogwaardige service.",
    "heroTagline": "Zaal met professionele techniek en memorabele ervaring",
    "badge": "Voor maîtres, restaurantleiders en servicechefs",
    "painsTitle": "Wat een Maître Niet Mag Missen om Op te Lossen",
    "pains": [
      "Coördineren van de service in de zaal met perfecte volgorde van gangen, gueridon, decanteren en professionele service per dienst",
      "Beheren van premium reserveringen met tafelplanning, allergieën, speciale gelegenheden en voorkeuren van terugkerende gasten",
      "Leiden van het zaalteam met continue training in pairing, bestek, gerechtbeschrijvingen en storytelling",
      "Coördineren met de keuken gang na gang met perfecte timing en vlotte communicatie tijdens servicepieken",
      "Differentiëren in een concurrerend restaurant met memorabele ervaring, fine dining visuele branding en het aantrekken van terugkerende gasten",
      "Binnenhalen van privé-evenementen en zakelijke diners met professionele service- en pairingvoorstellen"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Maître Helpt",
    "features": [
      {
        "icon": "Crown",
        "title": "Pro Restaurant Manager",
        "description": "Gespecialiseerde agent aangepast aan fine dining zaalmanagement: servicevolgorde, gueridon, decanteren, teamtraining."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Voor professioneel beheer van de wijnkelder, decanteren, wijnadvies en professionele cocktailbereiding."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Wetenschappelijk onderbouwde pairing voor elk gerecht op de kaart, professionele onderbouwing voor het zaalteam."
      },
      {
        "icon": "Calculator",
        "title": "Calcula Pax + Mise",
        "description": "Calcula Pax voor banketten, sjablonen voor mise en place, gueridon, volgorde van gangen."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Sjablonen: pre-service (mise en place), service (gangen), post-service (afrekening, schoonmaak), teamtraining."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC zaal",
        "description": "Traceerbaarheid van de wijnkelder, conservering van wijnen, decanteren en serveertemperaturen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Premium reserveringen, privé-evenementen, zakelijke diners, Kerst, Valentijnsdag, jubilea."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Elegante AI-referentiefotografie + Instagram met storytelling van service en pairing om premium gasten aan te trekken."
      },
      {
        "icon": "BookOpen",
        "title": "Menu Storytelling",
        "description": "Genereren van gerechtbeschrijvingen en pairing zodat het zaalteam ze professioneel aan de gast kan presenteren."
      }
    ],
    "workflowTitle": "Een Echte Dag van een Maître met AI Chef Pro",
    "workflow": [
      "15:00 · Opening — checklist Kit de Tareas: controle van reserveringen van de dag, mise en place van tafels, polijsten van glaswerk en bestek, controle van de wijnkelder.",
      "16:00 · Briefing aan het team — uitleg van de nieuwe gerechten van de dag met gegenereerde storytelling en gevalideerde pairing met Food Pairing AI.",
      "17:00 · Coördinatie met de keuken — controle van wijzigingen in de kaart, bevestigde allergieën, mise en place van gangen.",
      "18:30 · Ontvangst van eerste reserveringen — professionele aandacht, service van aperitieven, beschrijving van de kaart.",
      "20:00 · Dienstdiner — coördinatie gang na gang met de keuken, professioneel decanteren, gueridon aan tafel waar van toepassing.",
      "22:00 · Privé zakelijke diners — toegewijde aandacht voor een evenement van 12 personen met proefmenu en pairing.",
      "00:00 · Sluiting — afrekening, afscheid van het team, GastroIMG Gen+ genereert referentiebeeld van het proefmenu + InstaFlow plant een post.",
      "01:00 · Afsluitende briefing — feedback van het team, noteren van opmerkingen van gasten, planning voor de volgende dag."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Maître",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Pro Restaurant Manager + Bar & Lounge AI+ + Food Pairing AI hebben het niveau van mijn zaalteam compleet verhoogd. De dagelijkse briefing met gegenereerde storytelling van elk gerecht en wetenschappelijk gevalideerde pairing is nu professioneel. Klanten merken het verschil: we verhoogden de gemiddelde ticketwaarde met 20% en het aandeel terugkerende premium gasten groeide met 40% in zes maanden.",
    "testimonialAuthor": "Sofía Vega",
    "testimonialRole": "Maître en Restaurantleider, fine dining restaurant",
    "faqTitle": "Veelgestelde Vragen van Maîtres",
    "faqs": [
      {
        "q": "Is dit geschikt voor fine dining, chef's restaurant, Michelin-sterrenrestaurant of premium restaurant?",
        "a": "Voor alle vier. Pro Restaurant Manager + Bar & Lounge AI+ dekken van premium restaurant tot Michelin-sterrenrestaurant met onberispelijke service, gueridon, professioneel decanteren en storytelling."
      },
      {
        "q": "Hoe beheer ik premium reserveringen en terugkerende gasten?",
        "a": "Pro Restaurant Manager redeneert met professionele zaalcriteria: tafelplanning op basis van voorkeur, noteren van allergieën en gelegenheden, aantrekken van terugkerende gasten met gepersonaliseerde menu's."
      },
      {
        "q": "Hoe train ik mijn zaalteam in pairing en storytelling?",
        "a": "Food Pairing AI onderbouwt elke pairing met wetenschappelijke basis die het team aan de gast kan communiceren; Bar & Lounge AI+ gaat dieper in op wijnkelder, decanteren en technieken. De dagelijkse briefing is nu professioneel."
      },
      {
        "q": "Genereert het elegante visuele content voor Instagram?",
        "a": "Ja. GastroIMG Gen+ genereert elegante referentiebeelden van het menu en gedekte tafel voor Instagram, website en het aantrekken van premium gasten. Onthoud dat het AI-beeld een visuele referentie is: de definitieve foto maakt u zelf met uw echte tafel."
      },
      {
        "q": "Hoe helpt het mij met privé-evenementen en zakelijke diners?",
        "a": "Gastro Calendar plant privé-evenementen, zakelijke diners, Kerst, Valentijnsdag, jubilea met proefmenu's en voorstellen voor toegewijde service."
      }
    ],
    "ctaTitle": "Uw Zaal met Professionele Techniek en Memorabele Ervaring.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschap voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Maître en Restaurantleider: Service, Pairing en Storytelling | AI Chef Pro",
      "description": "AI-suite voor professionele maîtres: Pro Manager, Bar & Lounge AI+, Food Pairing AI, teamtraining en premium acquisitie. Start vandaag.",
      "keywords": "AI maître, AI restaurantleider, software maître, fine dining zaal, gueridon decanteren AI, teamtraining zaal",
      "ogImage": "https://aichef.pro/og/use-cases/maitre-jefe-sala.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd naar Uw Zaal vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor soort restaurant u leidt (fine dining, chef's restaurant, Michelin-sterrenrestaurant, premium restaurant met wijnkelder), teamgrootte, stad en specialiteit. Elke agent reageert aangepast aan uw restaurant en dagelijkse praktijk.",
    "appsTitle": "De AI-agenten die u als Maître zult gebruiken",
    "apps": [
      {
        "name": "Pro Restaurant Manager",
        "category": "Gastro Profile Pro",
        "description": "Gespecialiseerde agent aangepast aan fine dining zaalmanagement."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Beheer van wijnkelder, decanteren, wijnadvies en professionele cocktailbereiding."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Wetenschappelijk onderbouwde pairing voor elk gerecht op de kaart."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Storytelling en gerechtbeschrijvingen voor het zaalteam."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en Utilities",
        "description": "Opschalen van recepten voor privé-evenementen en zakelijke diners."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen om aan de gast te communiceren."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en Utilities",
        "description": "Coaching voor leiderschap van het zaalteam en stressmanagement tijdens servicepieken."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Elegante AI-referentiefotografie voor Instagram, website en premium acquisitie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met elegante redactionele kalender voor fine dining."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Aantrekken van premium gasten die op Google en Maps zoeken naar fine dining."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Privé-evenementen, zakelijke diners, Kerst, Valentijnsdag, jubilea."
      },
      {
        "name": "Personeelsmaaltijden",
        "category": "Gastro Profile Pro",
        "description": "Generator voor personeelsmenu's vóór de service."
      }
    ],
    "metrics": [
      {
        "value": "+20 %",
        "label": "gemiddelde ticketwaarde fine dining"
      },
      {
        "value": "×1.4",
        "label": "ratio terugkerende gasten"
      },
      {
        "value": "×2",
        "label": "snelheid van evenementvoorstellen"
      },
      {
        "value": "12+",
        "label": "agenten voor uw zaal"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde briefing aan het team, storytelling van gerechten zonder onderbouwing",
        "Pairing aanbevolen zonder wetenschappelijke basis",
        "Premium reserveringen zonder planning met voorkeuren en allergieën",
        "Privé-evenementen handmatig afgesloten, traag voorstel",
        "Geïmproviseerde Instagram zonder storytelling van service"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Dagelijkse professionele briefing met storytelling en pairing",
        "Pairing met wetenschappelijke basis van Food Pairing AI",
        "Premium reserveringen met professionele planning en terugkerende acquisitie",
        "Privé-evenementen binnen één dag afgesloten met servicevoorstel",
        "Elegante Instagram met GastroIMG Gen+ + InstaFlow AI Pro"
      ]
    },
    "galleryTitle": "Hoe de Zaal van een Fine Dining Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro coördineert: mise en place, gueridon, decanteren, service en team. AI-gegenereerde referentiebeelden als visuele leidraad voor het concept.",
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
    "h1": "AI voor sommeliers",
    "heroSubtitle": "Ontwerp wijnkaarten met professionele criteria, valideer pairings op wetenschappelijke basis, beheer uw wijnkelder met traceerbaarheid en creëer een wine-driven branding met een suite van gastronomische AI-agenten gespecialiseerd in professionele sommelierkunst.",
    "heroTagline": "Wijnkelder met professionele criteria en wetenschappelijke pairings",
    "badge": "Voor sommeliers, head sommeliers en wijnkelderdirecteuren",
    "painsTitle": "Wat een sommelier absoluut moet oplossen",
    "pains": [
      "Een wijnkaart ontwerpen met criteria: balans van regio's, druivenrassen, prijzen, glazen en verticals per wijnhuis",
      "Pairings wetenschappelijk valideren voor elk gerecht van het proefmenu en de wisselende seizoenskaart",
      "Wijnkelder beheren met traceerbaarheid: rotatie, kelderomstandigheden, bestellingen, verliezen door mislukte ontkurking",
      "Het verhaal van elke wijn standaardiseren zodat het bedieningsteam het professioneel aan de gast communiceert",
      "Zich onderscheiden in een concurrerend restaurant met een gecureerde wijnkelder, professioneel ontkurken en een wine-driven ervaring",
      "Premium klanten aantrekken met proeverijen, wijnevenementen en speciale pairings met hoge marge"
    ],
    "featuresTitle": "Hoe AI Chef Pro een sommelier helpt",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Agent gespecialiseerd in professionele sommelierkunst: wijnkelder, druivenrassen, regio's, ontkurkingstechniek en wijnservering."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Pairings op wetenschappelijke basis voor elk gerecht en elke wijn: analyse van zuurgraad, tannines, structuur, intensiteit en harmonie."
      },
      {
        "icon": "BookOpen",
        "title": "Creatieve Keuken + Storytelling",
        "description": "Verhaal van elke wijn voor het bedieningsteam: wijnhuis, terroir, druivenras, vinificatie, proefnotities."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening wijnkelder",
        "description": "Echte kostprijs per glas, food cost van wijn per service, verliezen door ontkurking en kaartvoorstellen met gevalideerde marge."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bodega",
        "description": "Sjablonen: keldercontrole (vochtigheid, temperatuur), rotatie, ontkurking van de dag, teamtraining."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC wijnkelder",
        "description": "Traceerbaarheid van wijnen, conservering, mislukte ontkurking en serveertemperaturen per type."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Proeverijen en wijnevenementen: pairings met proefmenu, lanceringen, wijnbeurzen, Kerst, privé-evenementen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "AI-wijnfotografie als referentie + Instagram met wijnverhaal om premium klanten aan te trekken."
      },
      {
        "icon": "BarChart3",
        "title": "Mermas GenCal",
        "description": "Nauwkeurige gegevens over verliezen bij mislukte ontkurking, gebroken glas en gemorste wijn."
      }
    ],
    "workflowTitle": "Een echte dag van een sommelier met AI Chef Pro",
    "workflow": [
      "11:00 · Opening — checklist Kit de Tareas Bodega: keldercontrole (12-14 °C, 70% luchtvochtigheid), bestellingen controleren, wijnrotatie van de dag.",
      "12:00 · Bar & Lounge AI+ — u werkt de kaart bij met twee nieuwe referenties (rode Bourgogne en Duitse Riesling). Recept + gegenereerd verhaal.",
      "13:00 · Food Pairing AI — u valideert de pairing van de nieuwe Riesling met een gefermenteerd visgerecht van het proefmenu. Analyse van zuurgraad en harmonie.",
      "14:00 · Kit de Escandallos Pro — u berekent de kostprijs van de twee nieuwe referenties met echte marge per glas en per fles, en valideert de adviesprijs.",
      "15:00 · Briefing aan het team — uitleg over de twee nieuwe referenties met verhaal en gevalideerde pairings.",
      "17:00 · Privéproeverij voor VIP-klant — selectie van vijf wijnen met ad hoc pairings, professioneel ontkurken, decanteren indien van toepassing.",
      "20:00 · Dinerdienst — coördinatie met maître en keuken, aanbevelingen per tafel, gueridon indien van toepassing.",
      "23:00 · Afsluiting — voorraad bijwerken, GastroIMG Gen+ genereert een referentieafbeelding van de nieuwe Bourgogne + InstaFlow plant een post."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor sommeliers",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "pro-prompts-ebook",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Bar & Lounge AI+ en Food Pairing AI hebben mijn aanbod veranderd. Elke pairing in het proefmenu heeft nu een gedocumenteerde wetenschappelijke basis die het bedieningsteam professioneel aan de gast communiceert. Het wijnmagazijnbeheer met kostprijs per glas heeft onze wijnmarge met 6 punten verhoogd. Privéproeverijen voor VIP's worden afgesloten in één gesprek met een professioneel voorstel.",
    "testimonialAuthor": "Eduardo Lara",
    "testimonialRole": "Head sommelier, restaurant met 1 Michelinster",
    "faqTitle": "Veelgestelde vragen van sommeliers",
    "faqs": [
      {
        "q": "Is het geschikt voor een sommelier van fine dining, gastronomisch restaurant, wijnwinkel of hotel?",
        "a": "Voor alle vier. Bar & Lounge AI+ dekt van sommelier van een premium restaurant tot head sommelier van een Michelin-gastronomisch restaurant, wijnwinkel met gecureerde kelder of hotel met meerdere outlets."
      },
      {
        "q": "Hoe helpt het mij met wetenschappelijke pairings?",
        "a": "Food Pairing AI redeneert op wetenschappelijke basis: analyse van zuurgraad, tannines, structuur, intensiteit, harmonie en contrast. Het onderbouwt elke pairing zodat het bedieningsteam het professioneel kan communiceren."
      },
      {
        "q": "Hoe beheer ik de kostprijs en marge per glas?",
        "a": "Kit de Escandallos Pro herberekent de marge per glas en per fles wanneer u de wijnkelderprijzen bijwerkt. Mermas GenCal voegt de kosten van mislukte ontkurking en verliezen tijdens de service toe."
      },
      {
        "q": "Genereert het wine-driven visuele content voor Instagram?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van glazen, decanteren en wijnkelder voor Instagram, website en het aantrekken van premium klanten. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte glas."
      },
      {
        "q": "Hoe helpt het mij met privéproeverijen en wijnevenementen?",
        "a": "Gastro Calendar plant privéproeverijen, wijnevenementen, wijnbeurzen, seizoenslanceringen en pairings met proefmenu's."
      }
    ],
    "ctaTitle": "Uw wijnkelder met professionele criteria en wetenschappelijke pairings.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor € 10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor sommeliers: wijnkelder, pairings en professionele proeverijen | AI Chef Pro",
      "description": "AI-suite voor professionele sommeliers: Bar & Lounge AI+, Food Pairing AI, kostprijs per glas, privéproeverijen en wine-driven branding. Begin vandaag.",
      "keywords": "AI sommelier, software sommelier, pairings AI, wijnkelderbeheer AI, kostprijs wijn, head sommelier, privéproeverij AI",
      "ogImage": "https://aichef.pro/og/use-cases/sommelier.jpg"
    },
    "personalizationTitle": "Vanaf de eerste minuut gepersonaliseerd voor uw wijnkelder",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor soort sommelier u bent (head sommelier van fine dining, freelance sommelier, directeur van een wijnwinkel, hotelsommelier, trainer), de grootte van de wijnkelder, stad en specialiteit. Elke agent reageert afgestemd op uw wijnkelder en daadwerkelijke bedrijfsvoering.",
    "appsTitle": "De AI-agenten die u als sommelier gaat gebruiken",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Agent gespecialiseerd in professionele sommelierkunst: wijnkelder, druivenrassen, regio's, techniek."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Pairings op wetenschappelijke basis: zuurgraad, tannines, structuur, intensiteit en harmonie."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Verhaal van elke wijn: terroir, vinificatie, proefnotities voor het bedieningsteam."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen bij mislukte ontkurking, gebroken glas en gemorste wijn geïntegreerd in de kostprijsberekening."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Identificatie van sulfieten in wijnen voor klanten met gevoeligheid."
      },
      {
        "name": "Gastro Lexicon",
        "category": "Gastro Kennis",
        "description": "Tutor voor technische definities: oenologie, vinificatie, terroir, herkomstbenamingen."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-wijnfotografie als referentie voor Instagram, website en evenementen."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met een wine-driven redactionele kalender om premium klanten aan te trekken."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Klanten aantrekken die op Google en Maps zoeken naar wijnwinkel, proeverij of sommelier."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Privéproeverijen, wijnbeurzen, lanceringen, Kerst, wijnevenementen."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "SEO-artikelen over pairings, druivenrassen en wijnhuizen om organisch verkeer aan te trekken."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI-modellen + LLM",
        "description": "Diepgaand onderzoek naar opkomende wijnhuizen, terroirs, jaargangen en trends."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge na kostprijsberekening wijnkelder"
      },
      {
        "value": "×2",
        "label": "snelheid van proeverijvoorstellen"
      },
      {
        "value": "×3",
        "label": "engagement Instagram wine-driven"
      },
      {
        "value": "12+",
        "label": "agenten voor uw wijnkelder"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Aanbevolen pairings zonder gedocumenteerde wetenschappelijke basis",
        "Wijnkaart zonder kostprijs per glas en echte marge",
        "Wijnkelder beheerd in spreadsheets, zonder traceerbaarheid of duidelijke rotatie",
        "Geïmproviseerd wijnverhaal, bedieningsteam zonder constante training",
        "Privéproeverijen handmatig afgesloten, traag voorstel"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Pairings op wetenschappelijke basis van Food Pairing AI",
        "Kostprijs per glas met realtime gevalideerde marge",
        "Wijnkelder met APPCC-traceerbaarheid en gedocumenteerde rotatie",
        "Dagelijkse briefing aan het team met verhaal en pairings",
        "Privéproeverijen binnen één dag afgesloten met een wine-driven voorstel"
      ]
    },
    "galleryTitle": "Zo werkt de wijnkelder van een sommelier",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: kelder, decanteren, glas, proeverij en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Meester Grillmeester en Barbecuechef",
    "heroSubtitle": "Beheers vuurtechniek, uitsnijden en dry-aged met professionele kostprijsberekening per cut, plan de productie van eiwitten en leg fire-driven branding vast met een suite van gespecialiseerde culinaire AI-agenten voor professioneel vuurkoken.",
    "heroTagline": "Vuur met authentieke techniek en echte marge",
    "badge": "Voor meester grillmeesters, barbecuechefs en grillmasters",
    "painsTitle": "Wat een Meester Grillmeester Niet Kan Nalaten Op te Lossen",
    "pains": [
      "Standaardiseren van gaarheid en vuurtechniek per dienst (houtskool, hout, marbling, kerntemperatuur)",
      "Rigoristisch uitsnijden met kosten per kilo en opbrengst per cut (chuletón, picaña, T-bone, lende)",
      "Beheer van dry-aged met kamer, vochtigheid, temperatuur, rotatie en wekelijks gedocumenteerd verlies",
      "Coördineren van grill met hoofdkeuken tijdens servicepieken zonder kwaliteits- of timingverlies",
      "Storytelling over veeleveranciers, ras, voeding en rijping voor de bediening",
      "Opleiden van junior grillkoks met technische criteria en consistentie in gaarheid"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Meester Grillmeester Helpt",
    "features": [
      {
        "icon": "Flame",
        "title": "Creatieve Keuken",
        "description": "Voor technische ontwikkeling van signature cuts, marinades, sauzen en bijgerechten van de grill."
      },
      {
        "icon": "UtensilsCrossed",
        "title": "Argentijnse + Braziliaanse Keuken",
        "description": "Gespecialiseerde recepten: parrilla, chimichurri, picaña, churrasco, authentieke techniek."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening per cut met dry-aged",
        "description": "Recept + kostprijsberekening CSV met geïntegreerd dry-aged verlies en uurkosten van de grill. Echte marge per cut."
      },
      {
        "icon": "BarChart3",
        "title": "Mermas GenCal",
        "description": "Gegevens per proces: uitsnijden, wekelijkse dry-aging, trimming, kookverlies."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Sjablonen: aansteken vuur, uitsnijden, controle dry-aged kamer, mise, sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC grill",
        "description": "Traceerbaarheid van vlees, dry-aging, kerntemperatuur en conservering."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Pairings met krachtige rode wijnen voor de nieuwe signature cuts."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Vaderdag, Kerst, zakelijke evenementen en seizoenslanceringen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Premium AI-referentiefotografie + Instagram met storytelling over de veeleverancier."
      }
    ],
    "workflowTitle": "Een Echte Dag van een Meester Grillmeester met AI Chef Pro",
    "workflow": [
      "09:00 · Opening — checklist Kit de Tareas: gecontroleerd aansteken van het vuur (3 uur om op punt te komen), controle dry-aged kamer.",
      "11:00 · Creatieve Keuken + Argentijnse Keuken — u ontwikkelt een nieuw signature cut van Galicische chuletón dry-aged 60 dagen met gerookt Maldon-zout en chimichurri. Recept + kostprijsberekening CSV.",
      "12:00 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke vleesprijzen en dry-aged verlies, valideert de echte marge per cut.",
      "13:00 · Middagdienst — grill op vol vermogen met premium cuts, mise van chimichurri en bijgerechten.",
      "17:00 · Briefing aan het team — opleiding van junior grillkoks met technische criteria voor gaarheid.",
      "20:00 · Avonddienst — gecoördineerde pieken, grill met meerdere cuts tegelijk.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de referentieafbeelding van de nieuwe chuletón en de posts voor Instagram.",
      "00:00 · Sluiting — grondige reiniging van grills, APPCC ondertekend, controle dry-aged kamer."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Meester Grillmeester",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Argentijnse Keuken + Creatieve Keuken hebben mijn niveau verhoogd. Mijn team reproduceert nu de gaarheid met gedocumenteerde technische criteria, de kostprijsberekeningen van premium cuts weerspiegelen het verlies van de dry-aged en we hebben de marge met 5 punten verhoogd. De planning voor Vaderdag met Gastro Calendar heeft onze omzet verdrievoudigd.",
    "testimonialAuthor": "Pedro Aguirre",
    "testimonialRole": "Meester grillmeester, premium grill met dry-aged",
    "faqTitle": "Veelgestelde Vragen van Meester Grillmeesters",
    "faqs": [
      {
        "q": "Is het geschikt voor Argentijnse parrilla, churrascaria, premium grill of steakhouse?",
        "a": "Voor alle vier. Argentijnse Keuken + Braziliaanse Keuken + Creatieve Keuken dekken van traditionele parrilla tot steakhouse met dry-aged."
      },
      {
        "q": "Deckt het dry-aged en kamerbeheer?",
        "a": "Ja. Het redeneert als een professionele meester grillmeester: kamervoorwaarden, tijden per cut, controle van wekelijks verlies en rotatie."
      },
      {
        "q": "Hoe beheer ik de volatiele vleeskosten?",
        "a": "Kit de Escandallos Pro herberekent de marge direct. Mermas GenCal voegt de kosten van verliezen door dry-aging, uitsnijden en trimming toe."
      },
      {
        "q": "Genereert het visuele content voor Instagram?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van cuts en vuur. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte cut."
      },
      {
        "q": "Hoe helpt het mij met zakelijke evenementen?",
        "a": "Gastro Calendar plant Vaderdag, Kerst, zakelijke evenementen en seizoenslanceringen van cuts."
      }
    ],
    "ctaTitle": "Uw grill met vuurtechniek en echte marge.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidplan voor 10 € per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Meester Grillmeester en Barbecuechef: Cuts, Vuur en Dry-Aged | AI Chef Pro",
      "description": "AI-suite voor meester grillmeesters: Argentijnse + Braziliaanse Keuken, kostprijsberekening per cut, dry-aged, branding en APPCC. Begin vandaag.",
      "keywords": "AI meester grillmeester, AI barbecuechef, grillsoftware, kostprijsberekening chuletón, dry-aged, vuurtechniek, Argentijnse parrilla AI",
      "ogImage": "https://aichef.pro/og/use-cases/maestro-asador-parrillero.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd naar Uw Grill vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een onboarding van 2 minuten waarin u vertelt welk type grill u leidt (Argentijnse parrilla, Braziliaanse churrascaria, premium steakhouse met dry-aged, casual buurtgrill), teamgrootte, stad en specialiteit. Elke agent reageert aangepast aan uw grill en werkelijke operatie.",
    "appsTitle": "De AI-agenten die u als Meester Grillmeester zult gebruiken",
    "apps": [
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van signature cuts met vuurtechniek en bijgerechten."
      },
      {
        "name": "Argentijnse Keuken",
        "category": "Latam-recepten",
        "description": "Asado, chimichurri, zwezerik en authentieke parrilla-techniek."
      },
      {
        "name": "Braziliaanse Keuken",
        "category": "Latam-recepten",
        "description": "Picaña, churrasco, farofa en churrascaria-techniek."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Pairings met krachtige rode wijnen en karaktervolle cocktails."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor de bar van de grill met premium rode wijnen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen bij uitsnijden, dry-aging, trimming en koken."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie per cut en bijgerecht."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Premium AI-referentiefotografie voor Instagram, website en menu."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met fire-driven redactionele kalender."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Klanten aantrekken die zoeken naar \"grill in de buurt\" op Google en Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Vaderdag, Kerst, zakelijke evenementen."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en Utilities",
        "description": "Coaching voor teamleiderschap en servicepieken."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na kostprijsberekening van cuts"
      },
      {
        "value": "×3",
        "label": "omzet op Vaderdag"
      },
      {
        "value": "−15 %",
        "label": "verliezen bij uitsnijden en dry-aging"
      },
      {
        "value": "12+",
        "label": "agenten voor uw grill"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde gaarheid tussen grillkoks",
        "Kostprijsberekeningen zonder dry-aged verlies",
        "Dry-aged kamer zonder traceerbaarheid",
        "Geïmproviseerde briefing, wisselende opleiding",
        "Instagram zonder storytelling over veeleverancier"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Consistente gaarheid met technische criteria",
        "Professionele kostprijsberekening met geïntegreerd dry-aged verlies",
        "Kamer met gedocumenteerde APPCC-traceerbaarheid",
        "Dagelijkse professionele briefing, constante opleiding",
        "GastroIMG Gen+ + storytelling over veeleverancier"
      ]
    },
    "galleryTitle": "Hoe de Grill van een Meester Grillmeester Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro zult coördineren: vuur, uitsnijden, cuts, chimichurri en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor meester-ijsbereider en gelatiere",
    "heroSubtitle": "Beheers de technische balans van bases, bereken per smaak met reële kosten, plan seizoensproductie en leg ambachtelijke branding vast met een suite van AI-agenten voor gastronomie, gespecialiseerd in professionele ijsbereiding.",
    "heroTagline": "Ijs met authentieke techniek en reële marge",
    "badge": "Voor meester-ijsbereiders, gelatieri en ambachtelijke ijsmakers",
    "painsTitle": "Wat een meester-ijsbereider moet oplossen",
    "pains": [
      "Veeleisende technische balans: balans van suikers (sacharose, dextrose, invertsuiker), totale vaste stoffen en vetten voor optimale textuur",
      "Verliezen in ijsmachine, schokkoeling en vitrine met temperatuurgevoelig product",
      "Extreme seizoensgebondenheid: hoogseizoen in de zomer, winterdal dat rendabel moet worden met ijsgebakken en semifreddo's",
      "Productie van bases (wit, geel, fruit, sorbet) per ploeg standaardiseren met technisch inzicht",
      "Differentiëren in een concurrerende omgeving met eigen smaken, premium ingrediënten (Sosa, Pistache di Bronte) en visuele branding",
      "Het team trainen in professionele techniek van balans en kristallisatie"
    ],
    "featuresTitle": "Hoe AI Chef Pro een meester-ijsbereider helpt",
    "features": [
      {
        "icon": "IceCream",
        "title": "Creatief IJs",
        "description": "Gespecialiseerde agent voor professionele ambachtelijke ijsbereiding: witte, gele, fruitbases, sorbets, technische suikerbalans."
      },
      {
        "icon": "Cake",
        "title": "Creatieve Patisserie",
        "description": "Voor ijsgebakken, semifreddo's, lepeldesserts die het winterdal rendabel maken."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor ontwikkeling van signature-smaken, gecontroleerde fusies en chef-presentaties."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening per smaak",
        "description": "Creatief IJs levert recept + CSV-kostprijsberekening met technische balans; Kit de Escandallos Pro beheert dit met reële marge per kg, per bol en per hoorntje."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients Agent",
        "description": "Sosa-catalogus voor professionele texturen, neutrale middelen, stabilisatoren en geconcentreerde pasta's."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Heladería",
        "description": "Sjablonen: voorbereiding ijsmachine, schokkoeling, vitrine aanvullen, temperatuurcontrole, rotatie."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC ijsbereiding",
        "description": "Traceerbaarheid van melk, vers fruit, noten en kritische temperaturen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Moederdag, lente, zomer, Valentijnsdag, ijsgebakken voor Kerst."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Ambachtelijke AI-fotografie als referentie + Instagram om lokale klanten te trekken."
      }
    ],
    "workflowTitle": "Een echte dag van een meester-ijsbereider met AI Chef Pro",
    "workflow": [
      "07:00 · Opening — checklist Kit de Tareas: controle van koeling, schokkoeling van mengsels die de vorige dag zijn bereid.",
      "08:30 · Creatief IJs — u ontwikkelt een nieuwe signature-smaak van pistache di Bronte met Maldon-zout. Creatieve Keuken levert recept + CSV-kostprijsberekening.",
      "09:30 · Sosa Ingredients Agent — u selecteert geschikte geconcentreerde pasta en neutraal middel.",
      "10:00 · Kit de Escandallos Pro — u laadt CSV met uw reële prijzen van premium pistache en melk, valideert marge per bol en per kg.",
      "11:00 · Productie van de dag — u laat mengsels door de ijsmachine lopen, schokkoelt tot -18 °C.",
      "13:30 · Vitrine aanvullen met etiketten en controle van expositieverliezen.",
      "16:00 · Creatieve Patisserie — u ontwikkelt een ijsgebak voor Moederdag met semifreddo van pistache.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert referentiebeeld van de nieuwe smaak + posts."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor meester-ijsbereider",
    "productIds": [
      "kit-tareas-heladeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Creatief IJs heeft onze keuken veranderd. We balanceren suikers en vaste stoffen met technisch inzicht, de berekeningen per bol met premium pistache weerspiegelen reële marge. Creatieve Patisserie opende de ijsgebakken die de winter rendabel maken. We stegen 5 punten.",
    "testimonialAuthor": "Federico Riva",
    "testimonialRole": "Meester-gelatiere, premium ambachtelijke gelateria",
    "faqTitle": "Veelgestelde vragen van meester-ijsbereiders",
    "faqs": [
      {
        "q": "Werkt het voor Italiaanse gelateria, ambachtelijke ijssalon of een keten met meerdere locaties?",
        "a": "Voor alle drie. Creatief IJs redeneert als een professionele meester-ijsbereider met gedocumenteerde technische balans."
      },
      {
        "q": "Deckt het de balans van suikers, vaste stoffen en vetten?",
        "a": "Ja. Creatief IJs redeneert als een professionele ijsbereider: balans met sacharose, dextrose, invertsuiker, totale vaste stoffen en vetten volgens technische norm."
      },
      {
        "q": "Hoe helpt het mij met seizoensgebondenheid?",
        "a": "Creatieve Patisserie opent ijsgebakken en semifreddo's voor het winterdal; Gastro Calendar plant pieken (Moederdag, zomer)."
      },
      {
        "q": "Genereert het visuele content voor Instagram?",
        "a": "Ja. GastroIMG Gen+ genereert referentiebeelden voor vitrine en sociale media. Onthoud dat het AI-beeld een visuele referentie is: de definitieve foto maakt u zelf met uw bak en echte presentatie."
      },
      {
        "q": "Hoe beheer ik verliezen in ijsmachine en vitrine?",
        "a": "Mermas GenCal levert gegevens per proces (ijsmachine, schokkoeling, expositie). Deze worden geïntegreerd in de kostprijsberekening van Kit de Escandallos Pro."
      }
    ],
    "ctaTitle": "Uw ijs met authentieke techniek en reële marge.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor 10 € per maand met 10.000 credits.",
    "seo": {
      "title": "AI voor meester-ijsbereider en gelatiere: Bases, kostprijsberekeningen en seizoensgebondenheid | AI Chef Pro",
      "description": "AI-suite voor meester-ijsbereiders: Creatief IJs, technische balans, kostprijsberekeningen per smaak, branding en APPCC. Start vandaag.",
      "keywords": "AI meester-ijsbereider, AI gelatiere, software ijsbereiding, kostprijsberekening ijs, technische balans ijs, ijsmachine AI",
      "ogImage": "https://aichef.pro/og/use-cases/maestro-heladero.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw ijssalon vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een onboarding van 2 minuten waarin u vertelt wat voor soort ijssalon u runt (Italiaanse gelateria, Spaanse ambachtelijke ijssalon, ijssalon met productieatelier), teamgrootte, stad en specialiteit.",
    "appsTitle": "De AI-agenten die u als meester-ijsbereider gaat gebruiken",
    "apps": [
      {
        "name": "Creatief IJs",
        "category": "Culinaire Creativiteit",
        "description": "Gespecialiseerde agent voor ambachtelijke ijsbereiding met technische balans."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "IJsgebakken, semifreddo's, lepeldesserts voor het winterdal."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van signature-smaken met recept + CSV-kostprijsberekening."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Neutrale middelen, stabilisatoren, geconcentreerde pasta's en professionele texturen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen in ijsmachine, schokkoeling en vitrine."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie per smaak: zuivel, noten, gluten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Ambachtelijke AI-fotografie als referentie voor vitrine, website en sociale media."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met redactionele kalender voor ambachtelijke ijsbereiding."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Klanten aantrekken die zoeken naar \"ijssalon bij mij in de buurt\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Moederdag, zomer, Valentijnsdag, ijsgebakken voor Kerst."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Social Media",
        "description": "Pinterest trekt organisch verkeer voor ijsgebakken."
      },
      {
        "name": "Personeelsmaaltijden",
        "category": "Gastro Profile Pro",
        "description": "Generator voor personeelsmenu's voor het productieatelier."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na kostprijsberekening van smaken"
      },
      {
        "value": "−40 %",
        "label": "verliezen in atelier en vitrine"
      },
      {
        "value": "×3",
        "label": "engagement Instagram"
      },
      {
        "value": "12+",
        "label": "agenten voor uw productieatelier"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde bases, inconsistente balans per ploeg",
        "Kostprijsberekeningen zonder gedocumenteerde technische balans",
        "Verliezen zonder traceerbaarheid per proces",
        "Reactieve seizoensgebondenheid in winterdal",
        "Vitrine en sociale media geïmproviseerd"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Bases met gedocumenteerde technische balans",
        "Professionele kostprijsberekeningen per bol en per kg",
        "Verliezen beheerd met Mermas GenCal",
        "IJsgebakken en semifreddo's maken de winter rendabel",
        "GastroIMG Gen+ + InstaFlow + Pinterest Pins Gen"
      ]
    },
    "galleryTitle": "Hoe het productieatelier van een meester-ijsbereider werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: ijsmachine, bases, spatel, fruit en apparatuur. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Banketbakkers en Patissiers",
    "heroSubtitle": "Beheers professionele patisserietechniek, bereken elk stuk met werkplaatsuurtarief, plan seizoensproductie en creëer ambachtelijke branding met een suite van gastronomische AI-agenten gespecialiseerd in banket en signatuurpatisserie.",
    "heroTagline": "Patisserie met authentieke techniek en echte marge",
    "badge": "Voor banketbakkers, patissiers en chefs pâtissiers",
    "painsTitle": "Wat een Banketbakker Niet Mag Negeren",
    "pains": [
      "Veeleisende geavanceerde techniek: bladerdeeg, brisée- en sablédeeg, biscuits, ganaches, glazuren, mousses met precieze balans",
      "Hoge verliezen in de werkplaats (vormen, bakken, decoreren) die zonder controle de winstgevendheid uithollen",
      "Signature-stukken ploeg na ploeg standaardiseren met professionele consistentie",
      "Zeer sterke seizoensgebondenheid: Driekoningentaart, Pasen, Valentijnsdag en Kerstmis vormen een groot deel van het jaar",
      "Zich onderscheiden met signatuurpatisserie, premium presentatie en storytelling over Franse of moderne techniek",
      "Op maat gemaakte taartbestellingen, privé-evenementen en bruiloften binnenhalen met marge terwijl u de dagelijkse patisserie beheert"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Banketbakker Helpt",
    "features": [
      {
        "icon": "Cake",
        "title": "Creatieve Patisserie",
        "description": "Agent gespecialiseerd in professionele patisserie, restaurantdesserts, op maat gemaakte taarten en banket met geavanceerde techniek."
      },
      {
        "icon": "Cookie",
        "title": "Creatieve Chocolaterie",
        "description": "Voor geavanceerde combinaties patisserie + chocolade: ganaches, cremeux, glazuren."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor de ontwikkeling van signature-desserts en smaakcombinaties met technisch inzicht."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekeningen met werkplaatsuurtarief",
        "description": "Creatieve Patisserie levert recept + kostprijs CSV; Kit de Escandallos Pro beheert dit met geïntegreerd werkplaatsuurtarief in de echte marge per stuk."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients Agent",
        "description": "Sosa-catalogus voor texturen, geleermiddelen, neutrale producten en geavanceerde techniek."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pastelería",
        "description": "Sjablonen: deegvoorbereiding, productie, vormen, bakken, decoreren, vitrine, conservering."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Patisserie",
        "description": "Traceerbaarheid van ei, crèmes, noten en professionele bewaring."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Driekoningentaart, Valentijnsdag, Pasen, Kerstmis, communies, Moederdag."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Ambachtelijke AI-referentiefotografie + Pinterest, waar patisserie stabiel organisch verkeer oplevert."
      }
    ],
    "workflowTitle": "Een Echte Dag van een Banketbakker met AI Chef Pro",
    "workflow": [
      "06:00 · Opening — checklist Kit de Tareas Pastelería: zuurdesem voeden, taartbeslag, bereiding van crèmes.",
      "08:00 · Creatieve Patisserie — u ontwikkelt een nieuw dessert voor Valentijnsdag. Creatieve Keuken levert recept + kostprijs CSV.",
      "09:00 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke prijzen en werkplaatsuurtarief, u valideert de marge per stuk.",
      "11:00 · Productie van de dag — vormen, bakken, decoreren met specifieke sjablonen.",
      "14:00 · Vitrine bijvullen met etiketten en prijzen.",
      "16:00 · Gastro Calendar — u bereidt de planning van Driekoningentaart 8 weken van tevoren voor.",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — u genereert referentiebeeld van het nieuwe dessert + pins.",
      "20:00 · Sluiting — grondige reiniging, HACCP ondertekend, planning voor de volgende dag."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Banketbakkers",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Creatieve Patisserie + Sosa Ingredients Agent hebben mijn aanbod veranderd. Mijn signature-desserts hebben nu gedocumenteerde techniek die mijn team consistent repliceert, de kostprijsberekeningen met werkplaatsuurtarief gaven mij 6 punten meer marge en op maat gemaakte taartbestellingen worden afgesloten in één gesprek met een professioneel voorstel.",
    "testimonialAuthor": "Eva Mata",
    "testimonialRole": "Chef pâtissière, signatuurpatisserie",
    "faqTitle": "Veelgestelde Vragen van Banketbakkers",
    "faqs": [
      {
        "q": "Is het geschikt voor een restaurantbanketbakker, ambachtelijke banketbakker of hotelchef pâtissier?",
        "a": "Voor alle drie. Creatieve Patisserie dekt van ambachtelijke patisserie tot haute restaurantpatisserie met geavanceerde Franse techniek."
      },
      {
        "q": "Deckt het geavanceerde techniek (bladerdeeg, mousses, glazuren)?",
        "a": "Ja. Creatieve Patisserie redeneert als een professionele chef pâtissier: omgekeerd bladerdeeg, technisch bewerkte degen, mousses met balans, glazuren met technische afwerking."
      },
      {
        "q": "Deckt het banket + chocolaterie?",
        "a": "Ja. Creatieve Chocolaterie vult aan met bonbons, ganaches, pralines en tempereertechiechniek voor gecombineerde stukken."
      },
      {
        "q": "Genereert het visuele content voor vitrine en social media?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen; Pinterest Pins Gen trekt stabiel organisch verkeer aan. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte stuk."
      },
      {
        "q": "Hoe helpt het mij met evenementen en seizoenen?",
        "a": "Gastro Calendar plant de belangrijkste seizoenen (Driekoningentaart, Valentijnsdag, Pasen, Kerstmis, communies) van tevoren."
      }
    ],
    "ctaTitle": "Uw banketbakkerij met signatuurtechniek en echte marge.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Ledenplan voor € 10 per maand met 10.000 credits.",
    "seo": {
      "title": "AI voor Banketbakkers en Patissiers: Techniek, Kostprijsberekeningen en Seizoensplanning | AI Chef Pro",
      "description": "AI-suite voor professionele banketbakkers: Creatieve Patisserie, kostprijsberekeningen met werkplaatsuurtarief, seizoensplanning en branding. Begin vandaag.",
      "keywords": "AI banketbakker, AI patissier, AI chef pâtissier, patisserie software, kostprijsberekening patisserie, Franse techniek, signatuurpatisserie",
      "ogImage": "https://aichef.pro/og/use-cases/repostero-pastelero.jpg"
    },
    "personalizationTitle": "Vanaf Minuut Eén Afgestemd op Uw Banketbakkerij",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een onboarding van 2 minuten waarin u vertelt welk type banketbakkerij u doet (restaurantpatissier, ambachtelijke banketbakker, hotelbanketbakker, banket voor evenementen), teamgrootte, stad en specialiteit.",
    "appsTitle": "De AI-agenten die u als Banketbakker Zult Gebruiken",
    "apps": [
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Agent gespecialiseerd in professionele patisserie met geavanceerde techniek."
      },
      {
        "name": "Creatieve Chocolaterie",
        "category": "Culinaire Creativiteit",
        "description": "Voor bonbons, ganaches en geavanceerde combinaties."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van signature-desserts met recept + kostprijs CSV."
      },
      {
        "name": "Creatieve Bakkerij",
        "category": "Culinaire Creativiteit",
        "description": "Voor brioche, croissants, ensaimadas en aanvullend banket."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus voor texturen, geleermiddelen en geavanceerde techniek."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de tSpoonLab-catalogus voor geavanceerde toepassingen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen in de werkplaats, vormen, bakken en vitrine."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie per stuk: gluten, zuivel, noten, ei."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Ambachtelijke AI-referentiefotografie voor vitrine, web en social media."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met redactionele kalender voor signatuurpatisserie."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Social Media",
        "description": "Pinterest trekt stabiel organisch verkeer aan voor taarten en desserts."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Driekoningentaart, Valentijnsdag, Pasen, Kerstmis, Moederdag."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge na kostprijsberekening per stuk"
      },
      {
        "value": "−30 %",
        "label": "werkplaatsverliezen"
      },
      {
        "value": "×2",
        "label": "organisch verkeer via Pinterest"
      },
      {
        "value": "12+",
        "label": "agenten voor uw werkplaats"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde techniek, inconsistente signature-desserts",
        "Kostprijsberekeningen zonder werkplaatsuurtarief",
        "Werkplaatsverliezen zonder echte traceerbaarheid",
        "Vitrine en social media geïmproviseerd met mobiele foto's",
        "Reactieve seizoensplanning, u komt te laat voor Driekoningentaart"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Gedocumenteerde techniek, consistente signature-desserts",
        "Professionele kostprijsberekening met geïntegreerd werkplaatsuurtarief",
        "Verliezen gecontroleerd met Mermas GenCal",
        "GastroIMG Gen+ + Pinterest Pins Gen trekken stabiel verkeer aan",
        "Driekoningentaart en seizoenen 8 weken van tevoren gepland"
      ]
    },
    "galleryTitle": "Zo Werkt de Banketbakkerij",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: piping, taarten, mise-en-place, vitrine en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Casual Restaurant",
    "heroSubtitle": "Optimaliseer de dagelijkse operatie, beheers de foodcost en win uren administratie terug in uw casual restaurant met een suite van AI-agenten gespecialiseerd in horeca.",
    "heroTagline": "Het moderne casual restaurant heeft AI nodig",
    "badge": "Voor casual restaurants en bistro's",
    "painsTitle": "Wat een casual restaurant moet oplossen",
    "pains": [
      "Kleine marge die nauwkeurige controle van kosten en verliezen in de keuken vereist",
      "Hoog personeelsverloop: het opleiden en begeleiden van nieuwe koks en obers kost elke week uren",
      "Uitgebreide menukaart met veel gerechten om te calculeren wanneer leveranciersprijzen veranderen",
      "APPCC en regelgeving altijd up-to-date zonder dat administratie tijd van de bediening steelt",
      "Klanten aantrekken in een concurrerend gebied: lokale SEO, social media en recensies zijn cruciaal",
      "Keuken, bediening en delivery coördineren tijdens servicepieken zonder fouten"
    ],
    "featuresTitle": "Hoe AI Chef Pro helpt in een casual restaurant",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Casual Restaurants AI+",
        "description": "Agent gespecialiseerd in bistro's, gastrobars, tapas en mediterraan: het complete casual spectrum met professionele basis."
      },
      {
        "icon": "Calculator",
        "title": "Professionele kostprijsberekeningen",
        "description": "Creatieve Keuken levert recept + kostprijsberekening CSV; Kit de Escandallos Pro beheert dit met uw werkelijke prijzen en doelstelling voor de marge."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Kant-en-klare sjablonen: opening, sluiting, keukenposten, bediening, delivery en evenementen."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC en traceerbaarheid",
        "description": "Pack APPCC met 19 registraties, registraties via mobiel, meldingen en afdrukklare A4-bladen voor de inspectie."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Roosters in minuten, met respect voor de cao, pauzes, urenregistratie en productiviteitsratio's."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Lokale SEO-suite om organisch klanten te werven zonder een bureau te betalen."
      },
      {
        "icon": "BarChart3",
        "title": "Kit Plan Financiero",
        "description": "Dashboard met ratio's, foodcost, productiviteit en gemiddeld ticket. Rapportage aan de eigenaar in PDF."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "AI-gastronomiefotografie voor web en socials, content voor Instagram met redactionele kalender."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Onderzoek naar lokale gastronomische zoekwoorden per postcodegebied voor echte vindbaarheid."
      }
    ],
    "workflowTitle": "Een echte dag in een casual restaurant met AI Chef Pro",
    "workflow": [
      "08:30 · Opening — checklist van de Kit de Tareas Restaurante Casual en voorraadcontrole in 10 minuten.",
      "10:00 · Casual Restaurants AI+ — u vraagt de agent om suggesties voor de dagschotel met producten die u op voorraad heeft.",
      "10:30 · Creatieve Keuken + Kit de Escandallos Pro — u calculeert de dagschotel met uw prijzen en valideert de marge.",
      "12:30 · Middagdienst — keuken, bediening en delivery gecoördineerd met sjablonen. Verliezen geregistreerd via de mobiel met APPCC.",
      "15:30 · Kit Plan Financiero — u bekijkt de KPI's van de vorige dag en ontdekt dat de foodcost op maandag is gestegen naar 32%, u identificeert de oorzaak.",
      "17:00 · MenuDish Local SEO — u werkt de beschrijvingen van de 6 topgerechten bij in Google Business en op de website.",
      "18:00 · Kit Inventario — u valideert bestellingen bij leveranciers met prijsvergelijking en meldingen voor minimale voorraad.",
      "23:30 · Sluiting — APPCC ondertekend, dagelijks rapport aan de eigenaar in PDF direct vanuit het Kit Plan Financiero."
    ],
    "productsTitle": "Downloadbare sjablonen en kits voor casual restaurants",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "We hebben 80 zitplaatsen en een hoog personeelsverloop. De Kit de Tareas Restaurante Casual en de Pack APPCC hebben onze hele operatie op orde gebracht. We lopen als een Zwitserse klok en de foodcost is in het eerste kwartaal met 3 punten gedaald, alleen al door nauwkeurige kostprijsberekening.",
    "testimonialAuthor": "Sandra López",
    "testimonialRole": "Manager, mediterraan casual restaurant met 80 zitplaatsen",
    "faqTitle": "Veelgestelde vragen over casual restaurants",
    "faqs": [
      {
        "q": "Werkt het voor restaurants met 30, 80 of 150 zitplaatsen?",
        "a": "Ja. De sjablonen schalen mee met het volume en de abonnementen passen zich aan het werkelijke gebruik aan. Er zijn klanten van 30 zitplaatsen tot ketens met 25 vestigingen."
      },
      {
        "q": "Deckt het ook delivery naast bediening?",
        "a": "Ja. De Kit de Tareas Restaurante Casual bevat specifieke sjablonen voor deliverybeheer, bijbehorende verliezen en coördinatie met platforms zoals Glovo, Uber Eats en Just Eat."
      },
      {
        "q": "Vervangt het mijn kassasysteem of reserveringssoftware?",
        "a": "Nee, het vult aan. Cover Manager of The Fork beheren reserveringen en het kassasysteem beheert verkopen; AI Chef Pro beheert kosten, personeel, APPCC, voorraad en lokale SEO. De gegevens zijn compatibel via Excel."
      },
      {
        "q": "Hoe lang duurt het voordat het team het leert?",
        "a": "Echte leercurve van 1-2 dagen. Er is een onboardingvideo van 5 minuten, ondersteuning via WhatsApp en alles start met de agent «Wie Ben Ik?» die het systeem in 2 minuten aanpast aan uw restaurant."
      },
      {
        "q": "Hoe helpt het mij met lokale SEO en klantenwerving?",
        "a": "Content- en social media-suite: MenuDish Local SEO (gerechtbeschrijvingen), BlogPost SEO Gen+ (blogposts), Keyword Discovery AI+ (zoekwoorden per postcodegebied), InstaFlow AI Pro (Instagram) en Pinterest Pins Gen."
      },
      {
        "q": "Is er een specifieke agent voor mijn type casual restaurant?",
        "a": "Ja. Casual Restaurants AI+ dekt bistro's, gastrobars, tapas, mediterraan, eetcafés, casual grillrestaurants. Voor specifiekere concepten zijn er Burger Pro AI+, Food Truck AI+ en agenten per land (Mexicaans, Peruaans, Japans, enz.)."
      }
    ],
    "ctaTitle": "Breng orde in uw casual restaurant.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Casual Restaurant: Operatie, Kostprijsberekeningen en Lokale SEO | AI Chef Pro",
      "description": "AI-suite voor casual restaurants en bistro's: gespecialiseerde agenten, kostprijsberekeningen, APPCC, roosters, lokale SEO en marketing met professionele basis. Begin vandaag.",
      "keywords": "AI casual restaurant, software casual restaurant, bistro management AI, kostprijsberekening casual, APPCC casual restaurant, marketing casual restaurant AI, lokale SEO restaurant, casual restaurant Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-casual.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw restaurant vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor casual u beheert (mediterraan, bistro, gastrobar, eetcafé, tapas), aantal zitplaatsen, stad en werkwijze. Vanaf dat moment reageert elke agent —van Casual Restaurants AI+ tot MenuDish Local SEO— aangepast aan uw context: gemiddelde ticketprijs in uw regio, regelgeving en werkelijke operatie.",
    "appsTitle": "De AI-agenten die u in uw casual restaurant zult gebruiken",
    "apps": [
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Hoofdagent: bistro's, gastrobars, tapas en mediterraan met professionele basis."
      },
      {
        "name": "Pro Restaurant Manager",
        "category": "Gastro Profile Pro",
        "description": "Operationele assistent en rapportage aan de eigenaar."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van professionele gerechten met recept + kostprijsberekening CSV."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Nauwkeurige gegevens over verliezen en opbrengsten voor keukencontrole."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per recept en gerecht."
      },
      {
        "name": "Personeelsmaaltijden",
        "category": "Gastro Profile Pro",
        "description": "Generator voor personeelsmenu's met producten die u al op voorraad heeft."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Gerechtbeschrijvingen geoptimaliseerd voor lokale SEO."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "Blogposts om lokaal organisch verkeer te trekken."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Content en Social Media",
        "description": "Gastronomische zoekwoorden per postcodegebied."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Virale content voor Instagram met redactionele kalender."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-gastronomiefotografie voor web en sociale media."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en Utilities",
        "description": "Coaching voor stressmanagement onder hoge druk en moeilijke gesprekken."
      }
    ],
    "metrics": [
      {
        "value": "−3 pp",
        "label": "foodcost in het eerste kwartaal"
      },
      {
        "value": "×2",
        "label": "reserveringen via lokale SEO"
      },
      {
        "value": "−6 h",
        "label": "wekelijks aan beheer"
      },
      {
        "value": "12+",
        "label": "agenten voor uw restaurant"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Operatie op losse vellen met elke post op zijn eigen manier",
        "APPCC op papier dat vóór de inspectie verloren raakt",
        "Handmatige roosters in Excel die uren kosten",
        "Geïmproviseerde marketing zonder organische klantenwerving",
        "Foodcost op gevoel, zonder te weten welk gerecht verliesgevend is"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Kit de Tareas met gestructureerde sjablonen per dienst en post",
        "APPCC via mobiel met registraties, meldingen en export naar PDF",
        "Roosters in minuten met de Kit Gestión de Personal, met respect voor de cao",
        "Lokale SEO-suite die organische reserveringen oplevert zonder uitgaven aan bureaus",
        "Foodcost per gerecht tot in detail berekend met professionele kostprijsberekening"
      ]
    },
    "galleryTitle": "Hoe een modern casual restaurant werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: bediening, open keuken, terras, dagschotel, team en bar.",
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
    "h1": "AI voor Koffiebar en Brunch",
    "heroSubtitle": "Optimaliseer ontbijt, brunch, specialty koffie en patisserie met een suite van AI-agents ontworpen voor coffee shops, brunchlocaties en moderne koffiebars.",
    "heroTagline": "Moderne coffee shop met moderne bedrijfsvoering",
    "badge": "Voor specialty koffiebars en brunch",
    "painsTitle": "Wat een Coffee Shop of Brunchlokal niet kan laten onopgelöst",
    "pains": [
      "Korte menu maar zeer hoge rotatie in piekuren in de ochtend en middag",
      "Zeer krappe marge in specialty koffie en patisserie met volatiele melk- en cacaokosten",
      "Jong en rotative team dat snelle training in bar en service nodig heeft",
      "Branding en social media (Instagram, Pinterest) zijn de belangrijkste hefboom for acquisitie",
      "Zich onderscheiden in een competetive buurt met premium maar toegankelijke pricing",
      "Beheeren de brunchflow in het weekend zonder de bedrijfsvoering door de week te laten collapsen"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Brunchcafé Helpt",
    "features": [
      {
        "icon": "Coffee",
        "title": "Casual Restaurants AI+",
        "description": "Agent met kennis van coffee shops, brunch en specialty koffiebar: menu, pricing en bedrijfsvoering."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijs for koffie, brunch en gebak",
        "description": "Creatieve Keuken levert recept + kostprijs CSV; Kit de Escandallos Pro beheert het met uw echte prijzen."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Patisserie + Creatieve Bakkerij",
        "description": "Professionele recepten for patisserie, brioche, croissants, cakes en ambachtelijke bakkerij."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Cafetería",
        "description": "Specifische sjablonen: opening, closing, bar, lichte keuken, brunch, service en reinigung."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC vereenvoudigd",
        "description": "Pack APPCC met minimale maar complete registraties for koffiebar: melk, conservatie, waschen, temperaturen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "AI gastronomische fotografie + Instagram content met captions, editorial kalender en planning."
      },
      {
        "icon": "Search",
        "title": "Pinterest Pins Gen",
        "description": "Pinterest is key for coffee shops: pins for brunch, koffie latte art en patisserie om organische traffic te krijgen."
      },
      {
        "icon": "BarChart3",
        "title": "KPIs en gemiddelde ticket",
        "description": "Kit Plan Financiero: bezetting ratio, gemiddelde ticket, productiviteit en upselling van brunch en koffie."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Lokale gastronomische keywords for «brunch [uw buurt]», «specialty koffie in de buurt» en similar."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Brunchcafé met AI Chef Pro",
    "workflow": [
      "07:00 · Opening — checklist van de Kit de Tareas Cafetería: bar gestart, gemalen koffie, koude melk, vitrine klaar.",
      "08:00 · Morning service — ontbijt en specialty koffie met coördineerde flow tussen bar en lichte keuken.",
      "11:00 · Creatieve Keuken — u ontwikkelt een nieuw brunch for zaterdag: toast met burrata, gravlax en eieren. U ontvangt kostprijs CSV.",
      "11:30 · Kit de Escandallos Pro — u laad de CSV met echte prijzen en valideert doel marge (32%).",
      "13:00 · Middag service — brunch in gang, team coördineerd met specifische sjablonen.",
      "16:00 · GastroIMG Gen+ + Pinterest Pins Gen — u genereert fotos van de nieuw brunch en optimaliseerde pins for Pinterest.",
      "17:30 · InstaFlow AI Pro — u programmeert Instagram posts for de volgende week met editorial kalender.",
      "19:30 · Closing — diepe reinigung, APPCC ondertekend, planning van de patisserie for de volgende dag."
    ],
    "productsTitle": "Sjablonen en Downloadbare Kits voor Koffiebars",
    "productIds": [
      "kit-tareas-cafeteria",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "We hebben brunch in het weekend en specialty koffie door de week. De Kit de Tareas Cafetería en de contentgeneration for Instagram hebben me de middagen teruggegeven. Pinterest Pins Gen was een ontdekking: het heeft ons organische traffic gebracht dat ik nog nooit gezien had.",
    "testimonialAuthor": "Marcos Rivera",
    "testimonialRole": "Eigenaar, specialty coffee shop en brunch",
    "faqTitle": "Veelgestelde Vragen van Coffee Shops",
    "faqs": [
      {
        "q": "Is het geschikt for specialty koffie or only casual koffiebar?",
        "a": "Het is geschikt for beide. Er zijn aanpasbare sjablonen for zowel specialty coffee shops (V60, single-origin espresso, latte art) as casual koffiebars en brunch."
      },
      {
        "q": "Werkt het for locaties met zeer lichte keuken?",
        "a": "Ja. De Kit de Tareas Cafetería heeft specifische sjablonen for lichte keuken, brunch en bar, zonder te assumen dat u een complete brigade heeft."
      },
      {
        "q": "Genereert het optimaliseerde content for Instagram en Pinterest?",
        "a": "Ja. InstaFlow AI Pro en Pinterest Pins Gen zijn specifische agents for die kanalen. Pinterest werkt zeer goed for brunch en koffie met stabiele organische traffic."
      },
      {
        "q": "Deckt het delivery en verlengde uren?",
        "a": "Ja. De sjablonen zijn aanpasbaar aan uren, delivery, take-away en lichte catering (corporate coffee break)."
      },
      {
        "q": "Hoe optimaliseert het de lokale SEO for uw coffee shop?",
        "a": "MenuDish Local SEO + BlogPost SEO Gen+ + Keyword Discovery AI+ werken samen om lokale zoekopdragen te krijgen zoals «brunch in [uw buurt]» or «beste specialty koffie in de buurt»."
      }
    ],
    "ctaTitle": "Uw koffiebar met gepolijste bedrijfsvoering en organische klantenwerving.",
    "ctaSubtitle": "Start met de 2-minuten onboarding. Lidplan for €10 per maand met 10.000 credits om alle agents te gebruiken.",
    "seo": {
      "title": "AI for Koffiebar en Brunch: Bedrijfsvoering, Pinterest en Lokale SEO | AI Chef Pro",
      "description": "AI-suite for coffee shops en brunchlocaties: gespecialiseerde agents, kostprijs, APPCC, content for Instagram en Pinterest, lokale SEO. Start vandaag.",
      "keywords": "AI koffiebar, brunch software, AI coffee shop, specialty koffiebar beheer, koffie kostprijs, AI koffiebar marketing, Pinterest brunch, lokale SEO koffiebar, coffee shop Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/cafeteria-brunch.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd op Uw Coffee Shop vanaf de Eerste Minut",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor soort koffiebar u beheert (specialty, brunch, casual), stad en werkwijze. Vanaf dat moment reageert elke agent —van Creatieve Patisserie tot Pinterest Pins Gen— aangepast aan uw context: gemiddelde ticket in uw buurt, klantprofil en echte bedrijfsvoering.",
    "appsTitle": "De AI-Agents die U zult Gebruiken in Uw Koffiebar",
    "apps": [
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfskoncepten",
        "description": "Hoofdagent: coffee shops, brunch en koffiebar met professionele basis."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinarische Creativiteit",
        "description": "Professionele recepten for koffiebar patisserie: brioche, croissants, cakes, taarten."
      },
      {
        "name": "Creatieve Bakkerij",
        "category": "Culinarische Creativiteit",
        "description": "For coffee shops die hun eigen brood en gebak bakken met zuurdeeg."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinarische Creativiteit",
        "description": "Ontwikkeling van brunchgerechten met recept + kostprijs CSV."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per recept."
      },
      {
        "name": "Personeelsmaaltijden",
        "category": "Gastro Profile Pro",
        "description": "Generator for staff menu's die het team motiveren."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Lokale SEO-beschrijvingen om de ranking te verbeteren."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "Blog posts om organische traffic naar de coffee shop te krijgen."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Content en Social Media",
        "description": "Keywords per postcode: brunch, specialty koffie, etc."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Virale Instagram content met editorial kalender."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Social Media",
        "description": "Optimaliseerde pins for Pinterest: brunch, koffie, patisserie."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI gastronomische fotografie for web, social media en menu."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "organische traffic via Pinterest"
      },
      {
        "value": "+ €1,80",
        "label": "gemiddelde ticket per upselling"
      },
      {
        "value": "−4 h",
        "label": "wekelijks in social media management"
      },
      {
        "value": "12+",
        "label": "agents for uw koffiebar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Bedrijfsvoering van bar en lichte keuken geïmproviseerd elke shift",
        "Kostprijs op gevoel in koffie en patisserie met onzekere marge",
        "Chaotische Instagram zonder editorial kalender en zonder continuïteit",
        "Zonder aanwezigheid on Pinterest, verliezen de organische traffic dat de meeste converteert for brunch",
        "APPCC in notitieboek dat vergeten wordt bij de inspectie"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Kit de Tareas Cafetería met specifische sjablonen per shift en per station",
        "Professionele kostprijs in elke drank en gerecht met echte marge",
        "InstaFlow AI Pro met editorial kalender en optimaliseerde captions",
        "Pinterest Pins Gen dat stabiele organische traffic en hoge conversie krijgt",
        "APPCC via mobiel met registraties klaar for inspectie"
      ]
    },
    "galleryTitle": "Hoe een Moderne Brunchcafé Werkt",
    "gallerySubtitle": "Wat u zult coördineren met AI Chef Pro: specialty en brunch, barista, patisserie, ploeg en social media content.",
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
    "h1": "AI voor Pizzeria",
    "heroSubtitle": "Standaardiseer zuurdesem, berekken escandalls per pizza, beheer delivery en multi-brand mei een suite van AI-agente gespecialiseerd in professionnel pizzeria, napoletana, romana en amerikaanse pizza.",
    "heroTagline": "Pizza mei echte marge, techniek mei systeem",
    "badge": "Voor pizzerias en pizzaioli",
    "painsTitle": "Wat Een Pizzeria Neet Kan Late Ongeleet",
    "pains": [
      "Marge heel knaap in pizza mei millimètre controle van grammage in deeg, saus, kaas en toppings",
      "Verleies in zuurdesem, mozzarella en sausen die rentabiliteit bluide zonder controle",
      "Pieken in delivery-vraog (12:30-14:30, 20:30-22:30) zonder ruim voor fouten",
      "Breet pizzakaart mei individuel escandall voor elke variante",
      "Standaardiseer deeg en techniek in keukens wor de pizzaioli-team roteert",
      "Lokale kliente te kape mei SEO en social media om afhaankegeet van delivery-platforms te verminderen"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt in Een Pizzeria",
    "features": [
      {
        "icon": "Pizza",
        "title": "Italiaanse Keuken",
        "description": "Agint gespecialiseerd in professionnel Italiaanse keuken, deege, sausen en techniek van napoletana, romana en amerikaanse pizzeria."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Voor zuurdesem, lange fermentaties, hoge hydrataties en baktechniek toegepast op professionnel pizza."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos per pizza",
        "description": "Creatieve Keuken levert recept + escandall CSV; Kit de Escandallos Pro beheert het mei uw echte prizen en doel-marge per variante."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pizzería",
        "description": "Sjablonen: deeg-hydratatie, saus-prep, toppings-mise en place, service in lokaal en delivery."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC",
        "description": "Sjablonen aangepast aan pizzeria: ovetemperature, conservering van zuurdesem, traceerbaarheid voor delivery."
      },
      {
        "icon": "Truck",
        "title": "Burger Pro AI+ + Food Truck AI+",
        "description": "Als u een dark kitchen multi-brand operiert, ook complementaire agente voor gespecialiseerd delivery."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + InstaFlow AI Pro",
        "description": "Lokale posicionering in Google en viral content voor Instagram mei redactionel kalender."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "AI-gastronomische fotografie voor Glovo, Uber Eats, Just Eat en de restaurant-website."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Roosters voor pizzaioli, zaal en delivery mei roterende diensten en service-pieken."
      }
    ],
    "workflowTitle": "In Echte Dei in een Pizzeria mei AI Chef Pro",
    "workflow": [
      "08:00 · Opening — checklist Kit de Tareas Pizzería: hydratatie van zuurdesem, prep van tomatensaus, mise en place van toppings.",
      "10:00 · Italiaanse Keuken + Fermentus Con AI+ — u ontwikkelt een nuie seizoenspizza mei deeg van 75 % hydratatie en 48 h fermentatie.",
      "11:00 · Kit de Escandallos Pro — u escandalt de nuie pizza mei uw echte prizen (mael, mozzarella, prosciutto) en valideert marge op 32 %.",
      "12:30 · Middagsservice — pizzaiolo aan de oven, zaal vol, delivery actief mei specifieke sjablonen.",
      "15:30 · Inventaire — u valideert bestellinge van Italiaanse mael, mozzarella di bufala en conserven mei de Kit Inventario.",
      "17:00 · MenuDish Local SEO — u updateert de beschrijvinge van de top pizza in Google Business en de website.",
      "20:00 · Aovendservice — delivery-piek, pizzaiolo aan de oven coördineert mei zaal en koeriers.",
      "23:30 · Sluite — reinig, APPCC gesigned, deagverslaag aan de eigenaar."
    ],
    "productsTitle": "Sjablonen en Kits voor Pizzeria te Downloaden",
    "productIds": [
      "kit-tareas-pizzeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Wei maakte escandall pizza voor pizza mei de Kit de Escandallos Pro en ontdekte dat 4 variante in verleies ware omdat wei te veul mozzarella wooge. Wei pasten grammage en prijs aan. De marge van de lokaal steeg 4 punten in 2 maanden zonder de kwaliteit te raken.",
    "testimonialAuthor": "Giovanni Russo",
    "testimonialRole": "Pizzaiolo en eigenaar, napoletana pizzeria",
    "faqTitle": "Fais Vraogen van Pizzerias",
    "faqs": [
      {
        "q": "Is het voor napoletana, romana, amerikaanse of detroit pizza?",
        "a": "Voor alle. Italiaanse Keuken en Fermentus Con AI+ dekke de volle spectrum van deege, hydrataties, fermentaties en technike van elke stijl."
      },
      {
        "q": "Dekt het delivery naist lokaal?",
        "a": "Jao. De Kit de Tareas Pizzería bevat specifieke delivery-sjablonen mei tijden, bijbehorende verleies en coördinatie mei platforms (Glovo, Uber Eats, Just Eat)."
      },
      {
        "q": "Werkt het voor 1 lokaal of een keten van pizzerias?",
        "a": "Beide. D'r binne kliente mei 1 lokaal en andere mei meer as 12 actieve eenheite. Voor groepe standaardiseert Executive Chef Pro recepte en handboeke."
      },
      {
        "q": "Genereert het idee voor promoties op slappe dege?",
        "a": "Jao. Gastro Calendar + InstaFlow AI Pro genereere combos, aanbiede, redactionel kalender en seizoenscampagnes mei professionnel creativiteit."
      },
      {
        "q": "Hoe helpt het mei professionnel zuurdesem?",
        "a": "Fermentus Con AI+ is referens in fermentatie: hydrataties, prefermente (poolish, biga, tang zhong), zuurdesem-verfrisschen en technike van gecontrolleerde fermentatie."
      }
    ],
    "ctaTitle": "Pizza mei echte marge, neet intuïtie.",
    "ctaSubtitle": "Start mei de 2-minuten onboarding. Lidmaan Plan voor 10 € per maand mei 10.000 crédits om alle agente te gebruken.",
    "seo": {
      "title": "AI voor Pizzeria: Zuurdesem, Escandallos per Pizza en Delivery | AI Chef Pro",
      "description": "AI-suite voor professionnel pizzerias: Italiaanse Keuken, Fermentus voor deege, escandallos per pizza, pizza-shop sjablonen en lokaal SEO. Start vandaag.",
      "keywords": "AI pizzeria, escandallos pizza, software pizzeria, zuurdesem pizza AI, napoletana pizza AI, romana pizza AI, pizzeria delivery beheer, pizzeria Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/pizzeria.jpg"
    },
    "personalizationTitle": "Aangepast aan Uw Pizzeria van Minut Een",
    "personalizationBody": "AI Chef Pro start mei de agint «Wie Ben Ik?», een conversacional onboarding van 2 minuten worin u vertelt wat voor soort pizzeria u operiert (napoletana, romana, amerikaanse, detroit, alla pala), aantal zitplaatsen, stad en operativa. Van dat moment aan reageert elke agint —van Italiaanse Keuken tot MenuDish Local SEO— aangepast aan uw deegstijl, delivery-platforms en lokaal markt.",
    "appsTitle": "De AI-Agente Die U Zal Gebruken in Uw Pizzeria",
    "apps": [
      {
        "name": "Italiaanse Keuken",
        "category": "Recepte per land",
        "description": "Agint gespecialiseerd in professionnel Italiaanse keuken mei basis van napoletana en romana pizzeria."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinair Creativiteit",
        "description": "Zuurdesem, hoge hydrataties en lange fermentaties mei professionnel ondersteuning."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinair Creativiteit",
        "description": "Ontwikkeling van creatieve pizza mei recept + escandall CSV."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Business Concepte",
        "description": "Voor de rest van de casual menü van de pizzeria te coördineren (veurgerechte, dessert)."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Precise data van verleies in deeg, mozzarella en toppings."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergene per pizza en gerecht."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Lokale SEO-beschrijvinge om webposicionering en delivery te verbeteren."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "Blog-posts om lokaal organisch traffic te kape."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Content en Social Media",
        "description": "Sleutelweurd per postcode: «napoletana pizza [uw buurt]»."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Viral Instagram-content mei pizzafoto en redactionel kalender."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-gastronomische fotografie voor web en delivery-platforms."
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "marge nao escandall pizza voor pizza"
      },
      {
        "value": "×2",
        "label": "delivery-traffic via lokaal SEO"
      },
      {
        "value": "−25 %",
        "label": "verleies mei systematische controle"
      },
      {
        "value": "11+",
        "label": "agente voor uw pizzeria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Zuurdesem en techniek verspreid in de notizboek van de hoofdpizzaiolo",
        "Escandalls op oog, grammages die variëre tussen pizzaioli",
        "Verleies van mozzarella en deeg zonder echte controle",
        "Zwake posicionering in delivery door generische beschrijvinge",
        "Delivery-operativa geimproviseerd in piekure"
      ],
      "afterTitle": "Mei AI Chef Pro",
      "afterItems": [
        "Italiaanse Keuken + Fermentus Con AI+ documenteere deeg en techniek die repliceerbaar is",
        "Professionnel escandall per pizza mei valideerde marge",
        "Verleies gecontrolleerd mei Mermas GenCal en specifieke sjablonen",
        "Lokaal SEO geoptimaliseerd mei MenuDish Local SEO + Keyword Discovery",
        "Kit de Tareas Pizzería mei sjablonen voor delivery, lokaal en pieken"
      ]
    },
    "galleryTitle": "Hoe Een Professioneel Pizzeria Werkt",
    "gallerySubtitle": "Wat u mei AI Chef Pro zal coördineren: oven, zuurdesem, pizza op detail, prep van toppings, team en delivery.",
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
    "h1": "AI voor Burgerrestaurants",
    "heroSubtitle": "Kostprijs per burger, beheers de kosten van vlees en brood, beheer delivery en multi-merk met een suite van AI-agenten gespecialiseerd in gourmet smash burger, fast casual en dark kitchen voor hamburgers.",
    "heroTagline": "Burger met echte marge, geen intuïtie",
    "badge": "Voor burgerrestaurants en burgerzaken",
    "painsTitle": "Wat een Burgerrestaurant Moet Oplossen",
    "pains": [
      "Vlees en brood: belangrijke grondstoffen met volatiele kosten die elke week veranderen",
      "Verliezen bij het garen van vlees, montage en verpakking voor delivery",
      "Delivery met zeer hoge rotatie en extreme pieken op specifieke uren",
      "Uitgebreide menukaart met veel burgervarianten (klassiek, gourmet, smash, plantaardig)",
      "Zich onderscheiden in een verzadigde markt van burgerzaken met lokale SEO en social media",
      "De grilltechniek en montage standaardiseren wanneer het team wisselt"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt in een Burgerrestaurant",
    "features": [
      {
        "icon": "Beef",
        "title": "Burger Pro AI+",
        "description": "Agent gespecialiseerd in burgerrestaurants: gourmet, smash, fastfood, plantaardig, ambachtelijk en thematisch."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijzen per burger",
        "description": "Creatieve Keuken levert recept + kostprijs-CSV; Kit de Escandallos Pro beheert dit met uw reële prijzen (vlees, brood, kaas, toppings, sauzen)."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Hamburguesería",
        "description": "Sjablonen: prep van sauzen, mise van toppings, grillplaat, montage, service en delivery."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC + Allergenen ID",
        "description": "Traceerbaarheid van vlees, garingcontrole, temperatuur en allergenen per burger."
      },
      {
        "icon": "Truck",
        "title": "Multi-platform deliverybeheer",
        "description": "Financieel plan met margeberekening na commissies van Glovo, Uber Eats en Just Eat per virtueel merk."
      },
      {
        "icon": "Leaf",
        "title": "VegChef Plantaardig",
        "description": "Voor vegetarische burgers met nutritionele techniek: Beyond Meat, Heura, kwalitatieve plantaardige alternatieven."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + InstaFlow AI Pro",
        "description": "Lokale positionering in Google en virale content voor Instagram, waar burgerzaken het meest verkopen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "AI-gastronomiefotografie, cruciaal voor Glovo, Uber Eats en Just Eat: betere foto = meer klikken en betere ranking."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Roosters voor grillplaat, montage, bediening en delivery met roulerende diensten."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Burgerrestaurant met AI Chef Pro",
    "workflow": [
      "11:00 · Opening — checklist Kit de Tareas Hamburguesería: prep van huisgemaakte sauzen, mise van toppings, grillplaat klaar.",
      "12:00 · Burger Pro AI+ — u ontwikkelt een nieuwe gourmet burger met geitenkaas en uienjam. Creatieve Keuken levert recept + kostprijs-CSV.",
      "12:30 · Kit de Escandallos Pro — u laadt de CSV met uw reële prijzen en valideert een marge van 31% na Glovo-commissie (29%).",
      "13:00 · Middagdienst — grillplaat actief, gecoördineerde montage, delivery gaat uit, volle eetzaal.",
      "16:00 · MenuDish Local SEO + GastroIMG Gen+ — u werkt de nieuwe burger bij op platforms met professionele foto en geoptimaliseerde beschrijving.",
      "17:30 · Inventaris — u valideert bestellingen van vlees (lokale leverancier), briochebrood en premium kaas.",
      "20:00 · Avonddienst — deliverypiek, montage aan de lijn, grillplaat op volle kracht.",
      "23:30 · Sluiting — schoonmaak, HACCP ondertekend, dagrapport en geregistreerde verliezen."
    ],
    "productsTitle": "Downloadbare Sjablonen en Kits voor Burgerrestaurants",
    "productIds": [
      "kit-tareas-hamburgueseria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "We verlaagden de foodcost van 36% naar 31% in 60 dagen met nauwkeurige kostprijzen en systematische controle van verliezen. De investering in AI Chef Pro was in één week terugverdiend, alleen al hiermee. De AI-foto voor Glovo bracht onze ranking van plaats 8 naar 3.",
    "testimonialAuthor": "Pablo Hernández",
    "testimonialRole": "Eigenaar, gourmet burgerrestaurant met 2 merken in delivery",
    "faqTitle": "Veelgestelde Vragen voor Burgerrestaurants",
    "faqs": [
      {
        "q": "Werkt het voor gourmet, smash of casual burgerrestaurants?",
        "a": "Voor alle. Burger Pro AI+ dekt het volledige spectrum: gourmet, smash burger, fastfood, plantaardig en thematisch."
      },
      {
        "q": "Deckt het delivery naast de fysieke locatie?",
        "a": "Ja. Specifieke sjablonen met deliveryverliezen, branded verpakking, coördinatie met platforms en margeberekening na commissies."
      },
      {
        "q": "Is er specifieke controle van vlees en traceerbaarheid?",
        "a": "Ja. Pack APPCC met traceerbaarheid van vlees, garingcontrole op punt, interne temperatuur en bewaring."
      },
      {
        "q": "Genereert het ideeën voor combo's en promoties?",
        "a": "Ja. Gastro Calendar + InstaFlow + Pro Prompts eBook genereren combo's, aanbiedingen voor rustige dagen, redactionele kalender en campagnes met AI."
      },
      {
        "q": "Is het geschikt voor het openen van een virtueel burgermerk in een dark kitchen?",
        "a": "Ja. Burger Pro AI+ + Casual Restaurants AI+ + Food Truck AI+ zijn combineerbaar voor virtueel multi-merk. Er is een reële case op /usos/concepto/dark-kitchen."
      }
    ],
    "ctaTitle": "Burger met echte marge, geen intuïtie.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Burgerrestaurants: Kostprijzen, Smash Burger en Delivery | AI Chef Pro",
      "description": "AI-suite voor professionele burgerrestaurants: Burger Pro AI+, kostprijzen per burger, burger-shop sjablonen, HACCP en multi-platform delivery. Begin vandaag.",
      "keywords": "AI burgerrestaurant, kostprijzen burger, software burgerrestaurant, smash burger AI, burger delivery beheer, gourmet burgerrestaurant AI, burgerrestaurant Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/hamburgueseria.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor Uw Burgerrestaurant vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor soort burgerrestaurant u runt (gourmet, smash, fast casual, plantaardig), aantal zitplaatsen, stad, deliveryplatforms en commissies. Elke agent —van Burger Pro AI+ tot het Kit de Escandallos Pro— reageert afgestemd op uw stijl en echte markt.",
    "appsTitle": "De AI-agenten die U in Uw Burgerrestaurant Zult Gebruiken",
    "apps": [
      {
        "name": "Burger Pro AI+",
        "category": "Bedrijfsconcepten",
        "description": "Agent gespecialiseerd in burgerrestaurants: gourmet, smash, fastfood, plantaardig."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van professionele burgers met recept + kostprijs-CSV."
      },
      {
        "name": "VegChef Plantaardig",
        "category": "Culinaire Creativiteit",
        "description": "Voor vegetarische burgers met professionele nutritionele techniek."
      },
      {
        "name": "Food Truck AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor mobiele concepten en multi-merk dark kitchen voor hamburgers."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Nauwkeurige gegevens over verliezen bij het garen van vlees en montage."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per burger en saus."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Lokale SEO-beschrijvingen voor Glovo, Uber Eats en web."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "Blogposts om lokale zoekopdrachten naar hamburgers aan te trekken."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Content en Social Media",
        "description": "Trefwoorden per postcodegebied: «smash burger [uw buurt]»."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Virale Instagram-content voor burgerrestaurants."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-gastronomiefotografie voor deliveryplatforms."
      }
    ],
    "metrics": [
      {
        "value": "−5 pp",
        "label": "foodcost in 60 dagen"
      },
      {
        "value": "+5",
        "label": "plaatsen in Glovo-ranking"
      },
      {
        "value": "×3",
        "label": "snelheid bij lanceren nieuwe burger"
      },
      {
        "value": "11+",
        "label": "agenten voor uw burgerzaak"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Kostprijzen op het oog met wisselend gewicht tussen koks",
        "Foodcost op 36% door verliezen en montage zonder controle",
        "Foto's van lage kwaliteit op Glovo en Uber Eats, lage ranking",
        "Vlees- en montageverliezen zonder traceerbaarheid",
        "Geïmproviseerde deliveryoperatie tijdens piekuren"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Burger Pro AI+ + Creatieve Keuken documenteren reproduceerbare techniek",
        "Foodcost op 31% met professionele kostprijs en gecontroleerde verliezen",
        "Professionele foto's met GastroIMG Gen+ die de ranking op platforms verhogen",
        "Pack APPCC met traceerbaarheid van vlees en geregistreerde verliezen",
        "Kit de Tareas Hamburguesería met sjablonen voor delivery en locatie"
      ]
    },
    "galleryTitle": "Hoe een Modern Burgerrestaurant Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: grillplaat, smash burger, montage, prep, team en delivery.",
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
    "h1": "AI voor Dark Kitchen en Virtuele Keukens",
    "heroSubtitle": "Schaal 1, 4 of 10 virtuele merken in dezelfde keuken. Beheer de foodcost per merk en per platform, verbeter uw positie in AI-deliveryagenten en vermenigvuldig de tickets zonder extra zaal aan te nemen.",
    "heroTagline": "Koken zonder eetzaal, marge met systeem",
    "badge": "Dark Kitchen en Ghost Kitchen",
    "painsTitle": "Wat een Dark Kitchen-operator niet kan nalaten op te lossen",
    "pains": [
      "Meerdere merken in dezelfde keuken, elk met zijn eigen kostprijsberekening en met grondstofkosten die elke week veranderen",
      "Marge onder druk door commissies van Glovo, Uber Eats en Just Eat (tussen 25% en 35% van het ticket)",
      "Brutale pieken in delivery, van 12:30 tot 14:30 en van 20:30 tot 22:30, zonder ruimte voor operationele fouten",
      "Zonder fysiek contact met de klant: het merk, de foto's en de copy van de vermelding zijn alles wat u heeft",
      "Positie op platforms die constant verandert: als u posities verliest, dalen de bestellingen sterk",
      "Moeilijk te weten welk merk en welk gerecht echt presteren wanneer alles in dezelfde keuken door elkaar loopt"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Dark Kitchen helpt",
    "features": [
      {
        "icon": "Layers",
        "title": "Multi-merk kostprijsberekening: Creatieve Keuken → Kit de Escandallos Pro",
        "description": "Creatieve Keuken genereert het gerecht en de initiële kostprijsberekening in CSV met marktreferentieprijzen. U laadt het in de Kit de Escandallos Pro, vervangt de prijzen door die van uw leveranciers en verkrijgt de werkelijke kosten en marge per merk, per gerecht en per platform."
      },
      {
        "icon": "Smartphone",
        "title": "Burger Pro AI+, Food Truck AI+ en Casual Restaurants AI+",
        "description": "Drie gespecialiseerde agenten die de meest winstgevende virtuele concepten in delivery dekken: hamburgerrestaurant, fastfood, casual en bistro."
      },
      {
        "icon": "Truck",
        "title": "Berekening van de werkelijke marge na commissie",
        "description": "Het financiële plan van AI Chef Pro trekt automatisch de commissies van elk platform af en toont u de werkelijke marge per merk en per kanaal."
      },
      {
        "icon": "TrendingUp",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "SEO-suite zodat uw merken stijgen in lokale Google en u organisch verkeer aantrekt, naast dat wat via de AI-agenten binnenkomt."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Onderzoek naar lokale gastronomische zoekwoorden om merken, gerechten en menu's te benoemen die beter scoren."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Gastronomische fotografie gegenereerd met AI voor platformvermeldingen. Betere foto = meer klikken en betere positie."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken + Italiaanse, Mexicaanse, Japanse Keuken…",
        "description": "Meer dan 25 AI-receptboeken per land om thematische virtuele merken te creëren met een professionele basis, geen recepten gekopieerd van Google."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC + Allergenen ID voor delivery",
        "description": "Traceerbaarheid, temperatuur en allergenen ontworpen voor product dat in een rugzak of op een motor reist."
      },
      {
        "icon": "BarChart3",
        "title": "Multi-merk en multi-platform dashboard",
        "description": "KPI's per merk, gemiddeld ticket, commissie, rangschikkingspositie en productiviteit. Alles geconsolideerd in één weergave."
      }
    ],
    "workflowTitle": "Een echte dag in een Dark Kitchen met AI Chef Pro",
    "workflow": [
      "08:30 · U bekijkt het dashboard van de vorige dag: merk A staat aan de leiding, merk C is 12% gedaald in positie. Er moet actie worden ondernomen.",
      "09:00 · Keyword Discovery AI+ — u onderzoekt wat gebruikers in uw postcodezone zoeken en ontdekt een zoekwoord dat ontbreekt in merk C.",
      "09:30 · MenuDish Local SEO — u werkt de beschrijvingen van de top 6 gerechten van merk C bij met dat zoekwoord.",
      "10:00 · Creatieve Keuken — brainstorm voor een sterrengerecht bij merk A, profiterend van een goede prijs van een leverancier. Dezelfde agent geeft u het volledige recept en een initiële kostprijsberekening met marktreferentieprijzen, downloadbaar als CSV.",
      "10:30 · Kit de Escandallos Pro — u laadt de CSV van Creatieve Keuken, vervangt de referentieprijzen door die van uw onderhandelde leveranciers en valideert de marge na commissie op Glovo (29%) en Uber Eats (25%).",
      "11:00 · GastroIMG Gen+ — u genereert de foto van het nieuwe gerecht en uploadt deze naar de platforms.",
      "12:30 · Delivery-service, met 4 merken die in dezelfde keuken opereren, ondersteund door de Dark Kitchen-taaksjablonen.",
      "16:00 · APPCC ondertekend, verliezen geregistreerd per merk en mise en place van het diner klaar.",
      "23:30 · Afsluiting: automatisch rapport per merk verzonden naar de WhatsApp van de eigenaar."
    ],
    "productsTitle": "Sjablonen, kits en downloadbare gidsen voor Dark Kitchen",
    "productIds": [
      "guia-dark-kitchen",
      "kit-tareas-dark-kitchen",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "kit-inventario"
    ],
    "testimonialQuote": "We exploiteren 4 virtuele merken in één keuken. Zonder kostprijsberekening per merk en per platform verloren we marge zonder te weten waar. AI Chef Pro heeft het voor ons opgelost in een week: we ontdekten dat één merk een foodcost van 41% had op Glovo. We hebben het herontworpen en de marge steeg met 7 punten zonder de prijs te wijzigen.",
    "testimonialAuthor": "Iván Domínguez",
    "testimonialRole": "Operator, dark kitchen met 4 virtuele merken",
    "faqTitle": "Veelgestelde vragen van Dark Kitchen-operators",
    "faqs": [
      {
        "q": "Werkt het voor 1 merk of voor meerdere in dezelfde keuken?",
        "a": "Voor beide. Het is vanaf de basis ontworpen voor multi-merk: onafhankelijke kostprijsberekening per merk, gescheiden KPI's en takenlijsten die de productie van meerdere merken in dezelfde partij coördineren."
      },
      {
        "q": "Deckt het de commissies van de platforms (Glovo, Uber Eats en Just Eat)?",
        "a": "Ja. De berekening van de werkelijke marge trekt automatisch de commissie van elk platform af, zodat u weet wat u per bestelling per kanaal verdient en u uw prijsbeleid beter kunt bepalen."
      },
      {
        "q": "Is er een stapsgewijze gids om een dark kitchen te openen?",
        "a": "Ja, de gids Hoe een Dark Kitchen op te zetten (€24): 12 hoofdstukken met wettelijke vereisten, financieel plan, keukenontwerp, technologie, marketing en platforms, plus 3 checklists in Excel en een rekenmachine."
      },
      {
        "q": "Is het geschikt om op te schalen naar meerdere dark kitchen-locaties?",
        "a": "Ja. De multi-lokale standaardisatie van de agent Executive Chef Pro en de geconsolideerde dashboards zijn ontworpen voor groepen met meerdere virtuele eenheden."
      },
      {
        "q": "Hoe helpt het mij om de positie in AI-deliveryagenten te verbeteren?",
        "a": "Met drie hefbomen: GastroIMG Gen+ voor foto's van betere kwaliteit (die de CTR verhogen), MenuDish Local SEO voor beschrijvingen die converteren en Keyword Discovery AI+ om te detecteren wat gebruikers in uw postcodezone zoeken."
      },
      {
        "q": "Past het systeem zich aan aan mijn land en mijn platforms?",
        "a": "Ja. U start met de agent «Wie Ben Ik?» in een onboarding van 2 minuten waarin u vertelt waar u opereert, welke platforms u gebruikt en welke commissies u heeft onderhandeld. Al de rest past zich aan uw context aan."
      },
      {
        "q": "En lokale SEO? Is het de moeite waard voor een dark kitchen?",
        "a": "Ja, heel erg. Een dark kitchen leeft van online ontdekking: als u naast het verkeer van de AI-agenten ook lokale zoekopdrachten op Google aantrekt (bijvoorbeeld 'hamburger delivery [uw buurt]'), verlaagt u uw afhankelijkheid van commissies en voegt u directe marge toe. De SEO-suite van AI Chef Pro is precies hiervoor ontworpen."
      }
    ],
    "ctaTitle": "Uw dark kitchen, met echte marge en gegevens per merk.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Dark Kitchen en Virtuele Keukens: Kostprijsberekening en SEO | AI Chef Pro",
      "description": "AI-suite voor dark kitchen en ghost kitchen: multi-merk kostprijsberekening, marge na commissie van Glovo en Uber Eats, lokale SEO, APPCC en gids om uw virtuele keuken te openen.",
      "keywords": "AI dark kitchen, dark kitchen software, ghost kitchen, virtuele keuken, multi-merk kostprijsberekening, dark kitchen openen, AI deliverybeheer, positie Glovo Uber Eats, ghost kitchen software, virtueel deliverymerk, dark kitchen Spanje, lokale SEO restaurant delivery",
      "ogImage": "https://aichef.pro/og/use-cases/dark-kitchen.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd naar uw merken, uw zone en uw platforms",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten. U vertelt welke merken u exploiteert, in welke stad en postcode, welke platforms u gebruikt (Glovo, Uber Eats, Just Eat) en welke commissies u heeft onderhandeld. Vanaf dat moment worden de kostprijzen berekend met uw werkelijke commissie, wijzen de lokale SEO-aanbevelingen naar uw buurt en worden de KPI's geconsolideerd per merk en per kanaal zoals u ze nodig heeft. Het is geen formulier: het is een kort gesprek dat elke agent omzet in een tool die op uw maat is gemaakt.",
    "appsTitle": "De AI-agenten die u zult gebruiken in uw Dark Kitchen",
    "apps": [
      {
        "name": "Burger Pro AI+",
        "category": "Bedrijfsconcepten",
        "description": "Specialist in virtuele hamburgerrestaurants: gourmet, fastfood, smashburger en plantaardig."
      },
      {
        "name": "Food Truck AI+",
        "category": "Bedrijfsconcepten",
        "description": "Mobiele en virtuele fastfoodconcepten met een krappe marge."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Bistro's, gastrobars, tapas en virtueel mediterraan: het hele casual spectrum."
      },
      {
        "name": "Italiaanse, Mexicaanse, Japanse, Thaise keuken…",
        "category": "Receptboeken per land",
        "description": "Meer dan 25 AI-receptboeken om thematische virtuele merken te creëren met een professionele basis. Elk recept wordt geleverd met een initiële kostprijsberekening in CSV, klaar voor de Kit de Escandallos Pro."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpprogramma's",
        "description": "Nauwkeurige gegevens over verliezen en opbrengsten. Kritiek voor een realistische kostprijsberekening in delivery."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpprogramma's",
        "description": "Automatische identificatie van allergenen per recept. Verplicht om legaal in delivery te verkopen."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en sociale media",
        "description": "SEO-geoptimaliseerde beschrijvingen per gerecht, klaar voor de blog en voor de platforms."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en sociale media",
        "description": "Blogposts die lokaal organisch verkeer naar uw virtuele merken trekken."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Content en sociale media",
        "description": "Onderzoek naar gastronomische zoekwoorden per postcodezone."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Gastronomische fotografie met AI voor platformvermeldingen: betere foto, betere positie."
      },
      {
        "name": "Pro Restaurant Manager",
        "category": "Gastro Profile Pro",
        "description": "Operationele assistent om merken, teams en leveranciers te coördineren."
      },
      {
        "name": "InstaFlow AI Pro + Pinterest Pins Gen",
        "category": "Content en sociale media",
        "description": "Virale content om een publiek aan te trekken buiten de deliveryplatforms."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "marge na kostprijsberekening per merk"
      },
      {
        "value": "×4",
        "label": "virtuele merken in één keuken"
      },
      {
        "value": "−35 %",
        "label": "tijd in multi-merkbeheer"
      },
      {
        "value": "12+",
        "label": "AI-agenten voor dark kitchen"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Handmatige kostprijsberekening in Excel met 'gemiddelde' marge tussen merken",
        "Commissies van platforms op het oog afgetrokken, zonder te weten welk kanaal meer oplevert",
        "Platformfoto's van gemiddelde kwaliteit en wisselvallige positie",
        "Generieke beschrijvingen die geen lokale SEO aantrekken",
        "KPI's door elkaar: onmogelijk te weten welk merk echt presteert",
        "Operatie in losse vellen en fouten tijdens piekuren"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Onafhankelijke kostprijsberekening per merk en per platform, met directe werkelijke marge",
        "Automatische berekening na commissie per kanaal en prijsbeslissingen met data",
        "Professionele foto's met GastroIMG Gen+ en stabielere positie",
        "Beschrijvingen en blog geoptimaliseerd voor de lokale SEO van uw postcodezone",
        "Multi-merk dashboard met gescheiden KPI's per merk en per kanaal",
        "Specifieke Dark Kitchen-takenlijsten om multi-merkproductie te coördineren"
      ]
    },
    "galleryTitle": "Hoe een moderne Dark Kitchen werkt",
    "gallerySubtitle": "Multi-merkproductie, branded verpakking per virtueel merk, schermen met bestellingen van Glovo, Uber Eats en JustEat, riders bij pickup en alles wat een 100% delivery-operatie omvat.",
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
    "h1": "AI voor patisserie en bakkerij",
    "heroSubtitle": "Receptcalculatie per stuk met uurkosten van de bakkerij, plan seizoensproductie en realiseer professionele branding met een suite van AI-agenten gespecialiseerd in ambachtelijke patisserie.",
    "heroTagline": "Patisserie met echte marge en zonder papierwerk",
    "badge": "Voor patisserieën en ambachtelijke bakkerijen",
    "painsTitle": "Wat een patisserie absoluut moet oplossen",
    "pains": [
      "Complexe receptcalculaties met zuurdesem, prefermenten en lange bereidingen die uren in de bakkerij vereisen",
      "Hoog verlies in de bakkerij (vormen, bakken, decoreren) dat de winstgevendheid zonder controle doet bloeden",
      "HACCP-traceerbaarheid met gevoelige producten: ei, zuivel, crèmes, noten",
      "Zeer sterke seizoensgebondenheid: Driekoningenrol, Valentijnsdag, Pasen, Kerstmis, communies",
      "Zich onderscheiden in een concurrerende omgeving: visuele branding, vitrine en sociale media zijn cruciaal",
      "Op maat gemaakte taartbestellingen binnenhalen met marge terwijl de dagelijkse patisserie wordt beheerd"
    ],
    "featuresTitle": "Hoe AI Chef Pro helpt in de patisserie",
    "features": [
      {
        "icon": "Cake",
        "title": "Creatieve Patisserie",
        "description": "Agent gespecialiseerd in professionele patisserie, restaurantdesserts, op maat gemaakte taarten en banket met geavanceerde techniek."
      },
      {
        "icon": "Cookie",
        "title": "Creatieve Chocolaterie",
        "description": "Voor bakkerijen die patisserie combineren met chocolaterie: bonbons, ganaches, couvertures en combinaties."
      },
      {
        "icon": "Wheat",
        "title": "Creatieve Bakkerij",
        "description": "Voor bakkerijen die hun eigen banket maken met zuurdesem, brioche, croissants en ambachtelijk brood."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Professionele zuurdesems, gecontroleerde fermentaties en geavanceerde bakprocessen."
      },
      {
        "icon": "Calculator",
        "title": "Receptcalculaties met uurkosten van de bakkerij",
        "description": "Creatieve Keuken levert recept + receptcalculatie CSV; Kit de Escandallos Pro beheert dit met geïntegreerde uurkosten van de bakkerij in de werkelijke marge per stuk."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pastelería",
        "description": "Sjablonen: zuurdesem voorbereiding, productie, vormen, bakken, vitrine, conservering."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC patisserie",
        "description": "Traceerbaarheid van ei, crèmes met zuivel, noten en professionele conservering."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Seizoensplanning met belangrijke data: Driekoningenrol, Valentijnsdag, Pasen, Kerstmis. Redactionele kalender voor de vitrine."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "AI-gastronomiefotografie + Pinterest, waar patisserieën meer stabiel organisch verkeer aantrekken."
      }
    ],
    "workflowTitle": "Een echte dag in een patisserie met AI Chef Pro",
    "workflow": [
      "06:00 · Opening — checklist Kit de Tareas Pastelería: zuurdesem verfrissen, taarten kloppen, crèmes voorbereiden.",
      "08:00 · Creatieve Patisserie — u ontwikkelt een nieuw dessert voor Valentijnsdag. Creatieve Keuken levert recept + receptcalculatie CSV.",
      "09:00 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke prijzen en geïntegreerde uurkosten van de bakkerij, u valideert de marge.",
      "11:00 · Productie van de dag — vormen en bakken met specifieke sjablonen, verliezen geregistreerd met HACCP.",
      "14:00 · Vitrine bijvullen met etiketten en prijzen, controle van expositieverliezen.",
      "16:00 · Gastro Calendar — u bereidt de productieplanning van Driekoningenrol (Kerstmis) voor.",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — u genereert foto's en pins van het nieuwe dessert om verkeer aan te trekken.",
      "20:00 · Sluiting — grondige reiniging, HACCP ondertekend, planning voor de volgende dag."
    ],
    "productsTitle": "Downloadbare sjablonen en kits voor patisserie",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "De receptcalculaties per stuk met uurkosten van de bakkerij hebben mijn ogen geopend. Ik ontdekte dat sommige complexe bereidingen niet rendabel waren, ondanks dat ze goed verkochten. We hebben ze opnieuw ontworpen met Creatieve Patisserie door het proces te vereenvoudigen zonder kwaliteitsverlies en we hebben de marge met 6 punten verhoogd.",
    "testimonialAuthor": "Eva Mata",
    "testimonialRole": "Eigenaresse, ambachtelijke patisserie met eigen bakkerij",
    "faqTitle": "Veelgestelde vragen van patisserieën",
    "faqs": [
      {
        "q": "Is het geschikt voor een kleine of grote ambachtelijke bakkerij?",
        "a": "Voor beide. De sjablonen schalen van een familiebedrijf met 2 personen tot industriële productie. Er zijn klanten met één en met zes patissiers."
      },
      {
        "q": "Deckt het ook brood naast patisserie?",
        "a": "Ja. Creatieve Bakkerij + Fermentus Con AI+ dekken ambachtelijk brood en professioneel zuurdesem voor gemengde bakkerijen."
      },
      {
        "q": "Is er controle over de uurkosten van de bakkerij?",
        "a": "Ja. Uurkosten van de bakkerij geïntegreerd in de receptcalculatie van Kit de Escandallos Pro: een complexe bereiding met 3 uur werk per stuk heeft de werkelijke kosten weerspiegeld."
      },
      {
        "q": "Genereert het inhoud voor vitrine en sociale media?",
        "a": "Ja. GastroIMG Gen+ voor vitrinefoto's + Pinterest Pins Gen + InstaFlow AI Pro + MenuDish Local SEO om lokale klanten aan te trekken."
      },
      {
        "q": "Hoe helpt het mij met seizoensgebondenheid?",
        "a": "Gastro Calendar plant de belangrijkste seizoenen (Driekoningenrol, Valentijnsdag, Pasen, Kerstmis, communies) vooraf en een financieel plan aangepast aan productiepieken."
      }
    ],
    "ctaTitle": "Uw bakkerij met duidelijke marge en professionele branding.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor 10 € per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor patisserie en bakkerij: Receptcalculaties, Seizoensgebondenheid en Branding | AI Chef Pro",
      "description": "AI-suite voor ambachtelijke patisserieën: Creatieve Patisserie, receptcalculaties per stuk met uurkosten van de bakkerij, HACCP, seizoensplanning en branding. Begin vandaag.",
      "keywords": "AI patisserie, software bakkerij, receptcalculaties patisserie, ambachtelijke patisserie AI, zuurdesem patisserie, Driekoningenrol Kerstmis, patisserie Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/pasteleria-obrador.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw bakkerij vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversatie-onboarding van 2 minuten waarin u vertelt welk type patisserie u runt (ambachtelijk, industrieel, restaurantpatisserie, gemengde bakkerij), teamgrootte, stad en specialiteit. Elke agent —van Creatieve Patisserie tot Gastro Calendar— reageert aangepast aan uw product, markt en dagelijkse praktijk.",
    "appsTitle": "De AI-agenten die u gaat gebruiken in uw patisserie",
    "apps": [
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Agent gespecialiseerd in professionele patisserie, desserts en taarten met geavanceerde techniek."
      },
      {
        "name": "Creatieve Chocolaterie",
        "category": "Culinaire Creativiteit",
        "description": "Voor bonbons, ganaches en chocoladecombinaties."
      },
      {
        "name": "Creatieve Bakkerij",
        "category": "Culinaire Creativiteit",
        "description": "Voor zuurdesem, brioche, croissants en ambachtelijk brood."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Fermentaties, prefermenten en geavanceerde baktechnieken."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van desserts met recept + receptcalculatie CSV."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de Sosa-catalogus voor texturen en geavanceerde techniek."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de tSpoonLab-catalogus voor geavanceerde toepassingen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Nauwkeurige gegevens over verliezen in de bakkerij (vormen, bakken, vitrine)."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per stuk, cruciaal in de patisserie."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-gastronomiefotografie voor vitrine, web en sociale media."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Sociale Media",
        "description": "Pinterest is het kanaal met het meeste stabiele organische verkeer voor patisserie."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Sociale Media",
        "description": "Seizoensplanning: Driekoningenrol, Valentijnsdag, Pasen, Kerstmis."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge na het calculeren van stukken"
      },
      {
        "value": "×2",
        "label": "organisch verkeer via Pinterest"
      },
      {
        "value": "−30 %",
        "label": "verlies in de bakkerij"
      },
      {
        "value": "12+",
        "label": "agenten voor uw bakkerij"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Receptcalculaties zonder uurkosten van de bakkerij, lange bereidingen in verlies zonder het te weten",
        "Verliezen in bakkerij en vitrine zonder echte traceerbaarheid",
        "Geïmproviseerde vitrine en sociale media zonder continuïteit",
        "Reactieve seizoensproductie, zonder voorafgaande planning",
        "HACCP op verspreid printpapier in de bakkerij"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Professionele receptcalculatie per stuk met geïntegreerde uurkosten van de bakkerij",
        "Verliezen gecontroleerd met Mermas GenCal en specifieke sjablonen",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ trekken stabiel verkeer aan",
        "Gastro Calendar plant belangrijke seizoenen vooraf",
        "HACCP vanaf mobiel met registraties klaar voor inspectie"
      ]
    },
    "galleryTitle": "Hoe een ambachtelijke patisserie werkt",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: vitrine, bakkerij, presentatie van stukken, decoratie, taarten en team.",
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
    "h1": "AI voor Bar en Cocktails",
    "heroSubtitle": "Ontwerp cocktailkaarten met eigen signatuur, bereken de kostprijs van elk drankje met uw werkelijke prijzen en creëer professionele branding met een suite van AI-agenten die zijn ontwikkeld voor bartenders, cocktailmakers en bar-eigenaren.",
    "heroTagline": "Uw bar met echte marge, cocktails met techniek",
    "badge": "Voor cocktailbars en cocktailzaken",
    "painsTitle": "Wat een cocktailbar absoluut moet oplossen",
    "pains": [
      "Complexe cocktails doorrekenen met veel ingrediënten, infusies en technieken",
      "Verliezen en breuk van glaswerk achter de bar die de winstgevendheid zonder controle uithollen",
      "Drankkaarten die seizoensgebonden veranderen met continu R&D",
      "Zeer krappe marge op sterke dranken met volatiele kosten voor premium alcoholen",
      "Zich onderscheiden in een concurrerend gebied met storytelling en visuele branding van cocktails",
      "Een cocktailbar met eigen signatuur combineren met biercafé, wijnen en een borrelkaart"
    ],
    "featuresTitle": "Hoe AI Chef Pro helpt in een cocktailbar",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Gespecialiseerde agent voor pubs, cocktailbars, wijnbars, sportbars en lounges met professionele kennis."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Onverwachte combinaties voor cocktails met eigen signatuur op wetenschappelijke basis en pairing met borrelhapjes."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Fermentaties voor gevorderde cocktails: kombucha's als basis, infusies, citruslactofermenten."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening per drankje",
        "description": "Creatieve Keuken levert recept + kostprijsberekening CSV; Kit de Escandallos Pro verwerkt dit met uw werkelijke prijzen en professionele marge per cocktail."
      },
      {
        "icon": "BookOpen",
        "title": "Cocktailkaarten met storytelling",
        "description": "Kaartontwerp en seizoensgebonden rotatie met professionele storytelling voor de bediening en de pers."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Templates: voorbereiding van sappen, siropen, garnituren, infusies, bar-mise-en-place, service en dieptereiniging."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Bar",
        "description": "Specifieke traceerbaarheid: verse sappen, crèmes, bewaring van garnituren, reiniging van glaswerk."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Cocktailfotografie met AI + Instagram-content met een professionele redactiekalender."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients Agent + tSpoonLab Agent",
        "description": "Assistenten voor de selectie van premium technische ingrediënten die veel worden gebruikt in cocktails met eigen signatuur."
      }
    ],
    "workflowTitle": "Een echte dag in een cocktailbar met AI Chef Pro",
    "workflow": [
      "11:00 · Opening — checklist Kit de Tareas Bar: voorbereiding van sappen, siropen, infusies en garnituren.",
      "14:00 · Bar & Lounge AI+ + Food Pairing AI — u ontwikkelt een nieuwe cocktail voor de voorjaarskaart met foodpairing in gedachten.",
      "15:00 · Creatieve Keuken levert recept + kostprijsberekening CSV; Kit de Escandallos Pro verwerkt dit met uw werkelijke prijzen (premium gin, siropen, garnering).",
      "16:00 · Testen van de cocktail met het team, laatste aanpassingen aan balans en verhoudingen.",
      "17:00 · Pro Prompts eBook + BlogPost SEO Gen+ — u schrijft storytelling voor de nieuwe kaart en een notitie voor de bediening.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de fotografie en Instagramposts voor de lancering.",
      "20:00 · Avondservice — gecoördineerde bar, gevalideerde kostprijzen, cocktails die met precisie worden geserveerd.",
      "02:30 · Sluiting — dieptereiniging, HACCP ondertekend, rapportage van de drankjes van de dag."
    ],
    "productsTitle": "Downloadbare sjablonen en kits voor bar en cocktails",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Dat elke cocktail is doorberekend en de kaart in één ochtend klaar is, heeft mijn manier van werken veranderd. Voorheen deed ik dat met een rekenmachine, een servet en veel intuïtie. Nu stel ik met Bar & Lounge AI+ en Kit de Escandallos Pro in 2 uur een nieuwe kaart samen met gevalideerde marge.",
    "testimonialAuthor": "Hugo Vázquez",
    "testimonialRole": "Bartender en eigenaar, cocktailbar met eigen signatuur",
    "faqTitle": "Veelgestelde vragen van bartenders en cocktailmakers",
    "faqs": [
      {
        "q": "Is het geschikt voor cocktails met eigen signatuur of casual cocktailbars?",
        "a": "Voor beide. Bar & Lounge AI+ + Food Pairing AI bestrijken alles, van klassieke cocktails tot avant-garde cocktails, met professionele techniek."
      },
      {
        "q": "Bestrijkt het naast cocktails ook biercafés en wijnen?",
        "a": "Ja. Bar & Lounge AI+ bestrijkt het volledige barspektrum: biercafés, wijnbars, lounges, traditionele pubs en sportbars."
      },
      {
        "q": "Genereert het ideeën voor nieuwe cocktails met techniek?",
        "a": "Ja. Bar & Lounge AI+ + Creatieve Keuken + Food Pairing AI + Fermentus Con AI+ werken samen om cocktails met een professionele basis te creëren."
      },
      {
        "q": "Werkt het voor een hotelbar of een zelfstandige horecazaak?",
        "a": "Beide. De hotellobbybar wordt beheerd via de use case /usos/concepto/hotel-completo-fb; de zelfstandige bar van hieruit."
      },
      {
        "q": "Hoe helpt het u met de visuele branding van uw cocktails?",
        "a": "GastroIMG Gen+ genereert professionele foto's van elk drankje voor Instagram, website en kaart. InstaFlow AI Pro plant de content volgens een redactionele kalender."
      }
    ],
    "ctaTitle": "Cocktailbar met echte marge en professionele branding.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor 10 € per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Bar en Cocktails: Cocktails met eigen signatuur, kostprijsberekening en branding | AI Chef Pro",
      "description": "AI-suite voor professionele bars en cocktailbars: Bar & Lounge AI+, Food Pairing AI, kostprijsberekening per cocktail, kaarten, HACCP en visuele branding. Begin vandaag.",
      "keywords": "AI cocktailbar, cocktail kostprijsberekening, bar software, AI bartender, AI cocktailmaker, cocktailbar AI, cocktailbar met eigen signatuur, AI beheer voor cocktailbars",
      "ogImage": "https://aichef.pro/og/use-cases/bar-cocktails.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw bar vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor bar u beheert (cocktailbar, wijnbar, biercafé, pub of loungebar), de stad en uw kaart. Elke agent — van Bar & Lounge AI+ tot Kit de Escandallos Pro — reageert afgestemd op uw barstijl en markt.",
    "appsTitle": "De AI-agenten die u in uw bar gaat gebruiken",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Hoofdagent: pubs, cocktailbars, wijnbars, sportbars, lounges."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire creativiteit",
        "description": "Ontwikkeling van cocktails met recept + kostprijsberekening CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire creativiteit",
        "description": "Wetenschappelijke combinaties voor cocktails met eigen signatuur en pairing met borrelhapjes."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire creativiteit",
        "description": "Fermentaties voor gevorderde cocktailbereiding: kombucha's, infusies, lactofermenten."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor bars met een borrelkaart en lichte keuken naast cocktails."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro-leveranciers",
        "description": "Assistent voor technische ingrediënten uit de Sosa-catalogus."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro-leveranciers",
        "description": "Assistent voor de tSpoonLab-catalogus voor technische cocktailbereiding."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpprogramma's",
        "description": "Automatische identificatie van allergenen in cocktails en borrelhapjes."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpprogramma's",
        "description": "Precieze gegevens over verliezen bij sappen, garnituren en glaswerk."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-kennis",
        "description": "AI-gastrofotografie voor cocktails: website, socials en kaart."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en social media",
        "description": "Virale Instagram-content voor cocktailbars met een redactionele kalender."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Gastro-kennis",
        "description": "300+ prompts voor cocktailstorytelling, perscommunicatie en training."
      }
    ],
    "metrics": [
      {
        "value": "×4",
        "label": "snelheid afronden cocktailkaart"
      },
      {
        "value": "+5 pp",
        "label": "marge na professionele kostprijsberekening"
      },
      {
        "value": "×3",
        "label": "Instagram-engagement met GastroIMG"
      },
      {
        "value": "12+",
        "label": "agenten voor uw bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Cocktails doorberekend met rekenmachine en servet",
        "Drankkaarten zonder professionele storytelling voor de bediening",
        "Verliezen achter de bar en glaswerk zonder traceerbaarheid",
        "Geïmproviseerde visuele branding op Instagram met mobielfoto's",
        "Geen systematische toegang tot internationale cocktailtrends"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Bar & Lounge AI+ + Creatieve Keuken + Kit de Escandallos Pro ronden kaarten in 2 uur af",
        "Professionele storytelling voor elke cocktail, klaar voor bediening en pers",
        "Verliezen onder controle met Mermas GenCal en specifieke templates",
        "GastroIMG Gen+ + InstaFlow genereren professionele foto's en virale posts",
        "Sonar Deep Research levert internationale trends en referenties"
      ]
    },
    "galleryTitle": "Hoe een professionele cocktailbar werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: de hoofdbar, shakertechniek, de afgewerkte cocktail, voorbereiding van garnituren, pourtechniek en service.",
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
    "h1": "AI voor Catering en Evenementen",
    "heroSubtitle": "Bereken de kostprijs per evenement, plan productie op schaal, beheer logistiek en HACCP buiten de locatie met een suite van AI-agenten gespecialiseerd in professionele catering, bruiloften, zakelijke evenementen en cocktails.",
    "heroTagline": "Evenementen met marge, zonder chaos",
    "badge": "Voor catering- en evenementenbedrijven",
    "painsTitle": "Wat een Cateringbedrijf Moet Oplossen",
    "pains": [
      "Menukosten berekenen met grote variatie in het aantal gasten (50, 200, 500) terwijl de prijzen elke week veranderen",
      "Productie en mise en place op schaal plannen vanuit de centrale keuken",
      "Logistiek, gekoeld transport en opbouw op de locatie van de klant coördineren",
      "HACCP en traceerbaarheid handhaven buiten de vaste locatie, op externe locaties en in voertuigen",
      "Zakelijke klanten aantrekken met professionele voorstellen die contracten met een hogere waarde afsluiten",
      "Gelijktijdig meerdere weekendevenementen beheren zonder fouten"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt bij Catering en Evenementen",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Agent gespecialiseerd in catering en culinaire evenementen: bruiloften, zakelijke evenementen, cocktails en gala's met professionele kennis."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken + Food Pairing AI",
        "description": "Brainstormen voor evenementmenu's. Creatieve Keuken levert recept + kostprijs-CSV klaar voor het Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekeningen per evenement",
        "description": "Kit de Escandallos Pro: u laadt de CSV met uw reële prijzen, past het aantal gasten aan en krijgt direct de marge."
      },
      {
        "icon": "Layers",
        "title": "Calcula Pax",
        "description": "Portiecalculator die recepten in seconden opschaalt naar 50, 200, 500 of 1000 gasten."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Catering",
        "description": "Sjablonen: centrale productie, gekoeld transport, opbouw op locatie, service en afbouw."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC buiten de vaste locatie",
        "description": "Traceerbaarheid tijdens transport, op externe locaties en externe service met registraties vanaf mobiel."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "AI-gastronomiefotografie voor voorstellen aan zakelijke klanten en een evenementengalerij."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergenen ID",
        "description": "Automatische identificatie, cruciaal voor evenementen met uiteenlopende voedingsprofielen."
      },
      {
        "icon": "Search",
        "title": "BlogPost SEO Gen+ + Keyword Discovery AI+",
        "description": "Organische acquisitie van bedrijven die catering in uw regio zoeken."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Cateringbedrijf met AI Chef Pro",
    "workflow": [
      "08:30 · Catering AI+ — de agent helpt u het voorgestelde menu voor een bruiloft met 180 gasten af te ronden op basis van de briefing van de klant.",
      "09:30 · Creatieve Keuken — u ontwikkelt de 12 gerechten van het menu met recept en kostprijs-CSV met referentieprijzen.",
      "10:30 · Calcula Pax + Kit de Escandallos Pro — u schaalt op naar 180 gasten, laadt de CSV met uw reële prijzen en valideert de marge.",
      "12:00 · GastroIMG Gen+ — u genereert foto's van de gerechten om op te nemen in de presentatie aan de klant.",
      "14:00 · Overleg met klant — voorstel afgerond met een professionele presentatie in plaats van de oude Word-sjablonen.",
      "16:00 · Kit de Tareas Catering — u plant centrale productie, transport, opbouw en service voor het evenement van zaterdag.",
      "18:00 · Pack APPCC — u bereidt temperatuurregistraties voor voor transport en traceerbaarheid op externe locaties.",
      "20:00 · Brief aan het team — u stelt een productie-, transport-, opbouw- en servicebrief samen vanuit één bron."
    ],
    "productsTitle": "Downloadbare Sjablonen en Kits voor Catering",
    "productIds": [
      "kit-tareas-catering",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "We sluiten evenementen af in een derde van de tijd. De kostprijsberekeningen per evenement passen zich tot in detail aan op het aantal gasten, de logistieke sjablonen zijn goud waard en de voorstellen met professionele fotografie sluiten zakelijke contracten die ons eerder ontgingen. Marge +5 punten in het eerste kwartaal alleen al door betere kostprijsberekening.",
    "testimonialAuthor": "Sara Pérez",
    "testimonialRole": "Cateringbedrijf voor zakelijke evenementen en bruiloften (200 evenementen per jaar)",
    "faqTitle": "Veelgestelde Vragen van Cateringbedrijven",
    "faqs": [
      {
        "q": "Is het geschikt voor boutique-catering of grote catering?",
        "a": "Voor beide. Van boutique-catering met 50 gasten per maand tot bedrijven met meer dan 1000 services per maand en evenementen met 2000 gasten."
      },
      {
        "q": "Deckt het bruiloften, zakelijke evenementen en cocktails?",
        "a": "Ja. Catering AI+ en het Kit de Tareas Catering hebben specifieke sjablonen voor de drie formaten en voor gala's/speciale evenementen."
      },
      {
        "q": "Is er specifieke HACCP buiten de vaste locatie?",
        "a": "Ja. Het Pack APPCC heeft sjablonen aangepast aan product dat reist in rugzak, motor, gekoelde bestelwagen of centrale keuken, inclusief traceerbaarheid op externe locaties."
      },
      {
        "q": "Genereert het commerciële voorstellen voor bedrijven?",
        "a": "Ja. Catering AI+ + GastroIMG Gen+ + Pro Prompts eBook maken het mogelijk professionele voorstellen op te stellen met gastronomische fotografie en storytelling."
      },
      {
        "q": "Hoe helpt het u om zakelijke klanten aan te trekken?",
        "a": "BlogPost SEO Gen+ + Keyword Discovery AI+ + MenuDish Local SEO werken samen om bedrijven aan te trekken die catering in uw regio zoeken via organische zoekopdrachten in Google."
      }
    ],
    "ctaTitle": "Catering met echte marge en zonder chaos.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor 10 € per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Catering en Evenementen: Bruiloften, Zakelijke Evenementen en Cocktails | AI Chef Pro",
      "description": "AI-suite voor professionele cateringbedrijven: Catering AI+, kostprijsberekeningen per evenement, productie op schaal, HACCP buiten de locatie en commerciële voorstellen. Begin vandaag.",
      "keywords": "AI catering, catering software, kostprijsberekening evenementen, AI cateringbeheer, AI catering bruiloften, AI zakelijke catering, gastronomische evenementen software, catering Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/catering-eventos.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor Uw Catering vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type catering u runt (bruiloften, zakelijke evenementen, cocktails, gala's), gemiddelde grootte, stad en jaarlijks volume. Elke agent —van Catering AI+ tot het Kit Plan Financiero— reageert aangepast aan uw type evenement, schaal en reële markt.",
    "appsTitle": "De AI-agenten die U in Uw Catering Zult Gebruiken",
    "apps": [
      {
        "name": "Catering AI+",
        "category": "Bedrijfsconcepten",
        "description": "Hoofdagent: bruiloften, zakelijke evenementen, cocktails en gala's met professionele basis."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van evenementmenu's met recept + kostprijs-CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Ingrediëntcombinaties en pairing voor cocktails en canapés."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Desserts voor evenementen en banketten met professionele techniek."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Voor avant-gardistische canapés met fermenten en innovatieve technieken."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en Utilities",
        "description": "Portiecalculator die recepten opschaalt naar 50, 200 of 500 gasten."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Kritieke identificatie van allergenen bij evenementen met veel gasten."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Nauwkeurige gegevens voor productie op industriële schaal."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "Blogposts om bedrijven aan te trekken via organische zoekopdrachten."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "SEO-beschrijvingen om de positie van de cateringwebsite te verbeteren."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-gastronomiefotografie voor voorstellen en webgalerij."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Voor technische ingrediënten in cocktails en canapés."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "snelheid bij het afronden van voorstellen"
      },
      {
        "value": "+5 pp",
        "label": "marge na reële kostprijsberekening"
      },
      {
        "value": "−50 %",
        "label": "tijd in logistiek"
      },
      {
        "value": "11+",
        "label": "agenten voor uw catering"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Menu met klant afronden: halve middag met rekenmachine",
        "Productie voor 200 gasten zonder nauwkeurige opschaling",
        "HACCP buiten de locatie geïmproviseerd",
        "Voorstellen met Word-sjablonen en stockfoto's",
        "Brief aan het team op losse vellen"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Menu in 30 minuten afronden met gevalideerde marge",
        "Productie opgeschaald met Calcula Pax en Mermas GenCal",
        "HACCP met traceerbaarheid tijdens transport en op externe locaties",
        "Voorstellen met GastroIMG Gen+ en professionele storytelling",
        "Gecentraliseerde brief met Kit de Tareas Catering"
      ]
    },
    "galleryTitle": "Hoe een Professioneel Cateringbedrijf Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: centrale productie, elegante evenementen, canapés, zakelijke cocktails, opbouw en service.",
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
    "h1": "AI voor Compleet Hotel (F&B + Housekeeping)",
    "heroSubtitle": "Beheer ontbijten, restaurant, roomservice, banketten, bar en housekeeping met een suite van AI-agenten ontworpen voor F&B Managers en hoteldirecties.",
    "heroTagline": "De volledige hoteloperatie gecoördineerd in één systeem",
    "badge": "Voor F&B Managers van hotels",
    "painsTitle": "Wat een F&B Manager van een Hotel Niet Kan Nalaten op te Lossen",
    "pains": [
      "Meerdere verkooppunten tegelijk coördineren: ontbijtbuffet, à-la-carterestaurant, lobbybar, roomservice en banketten",
      "Grote teams beheren met roterende 24/7-diensten met respect voor cao en rusttijden",
      "HACCP verspreid over meerdere keukenafdelingen onderhouden met consolidatie naar de F&B Director",
      "Geconsolideerde rapportage aan de hoteldirecteur en aan corporate met KPI's per F&B-lijn",
      "Seizoensmenu's voor meerdere outlets ontwerpen zonder dat het team verdrinkt in papierwerk",
      "Banketten voor bruiloften en zakelijke evenementen beheren in combinatie met de reguliere F&B"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt in een Compleet Hotel",
    "features": [
      {
        "icon": "Hotel",
        "title": "Kit de Tareas Hotel",
        "description": "Specifieke templates voor ontbijtbuffet, restaurant, lobbybar, roomservice, banketten en housekeeping in één documentair systeem."
      },
      {
        "icon": "ChefHat",
        "title": "Executive Chef Pro",
        "description": "Standaardisatie van recepten en technische bladen in alle hoteloutlets. Hetzelfde gerecht, dezelfde kwaliteit in restaurant, roomservice en banket."
      },
      {
        "icon": "Calculator",
        "title": "Kostenberekeningen per verkooppunt",
        "description": "Creatieve Keuken levert recept + kostenberekening CSV; Kit de Escandallos Pro beheert dit met uw werkelijke prijzen en splitst de marge per outlet."
      },
      {
        "icon": "PartyPopper",
        "title": "Catering AI+",
        "description": "Voor het ontwerp en de productie van bruiloftsbanketten, zakelijke evenementen en speciale hotelactiviteiten."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Voor de cocktails van de lobbybar, restaurantwijnen en sterke dranken met professionele kostenberekening."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Roosters voor grote 24/7-teams met roterende diensten met respect voor de cao van het land. Personeelsmaaltijden inbegrepen."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC corporativo",
        "description": "HACCP verdeeld over de keukenafdelingen maar geconsolideerd in één dashboard voor de F&B Director."
      },
      {
        "icon": "BarChart3",
        "title": "Kit Plan Financiero",
        "description": "Dashboard met KPI's per verkooppunt: ontbijt, restaurant, bar, roomservice, banketten. Bezetting en productiviteitsratio's."
      },
      {
        "icon": "BriefcaseBusiness",
        "title": "Pro Restaurant Manager",
        "description": "Voor de managers van elke outlet met geconsolideerde rapportage naar de F&B Manager van het hotel."
      }
    ],
    "workflowTitle": "Een Echte Dag van een F&B Manager van een Hotel met AI Chef Pro",
    "workflow": [
      "07:00 · Opening ontbijt — het team start het buffet met de checklist van de Kit de Tareas Hotel; u controleert het dashboard met de hotelbezetting en past de mise-en-place aan.",
      "09:30 · Catering AI+ — u bereidt het bruiloftsbanket van komende zaterdag voor: menu, kostenberekening en productie voor 220 gasten.",
      "11:00 · Executive Chef Pro — u werkt het technisch blad van het nieuwe restaurantgerecht bij en het wordt gerepliceerd naar de roomservice en het banketmenu met dezelfde standaardisatie.",
      "13:00 · Middagdienst — à-la-carterestaurant + lobbybar + roomservice actief. Het team coördineert met specifieke templates per outlet.",
      "15:30 · Kit Plan Financiero — u exporteert de KPI's per outlet van het kwartaal voor de vergadering met de hoteldirectie.",
      "17:00 · Bar & Lounge AI+ — u ontwerpt de nieuwe cocktailkaart voor de lobbybar met professionele kostenberekening.",
      "19:30 · Rooster volgende week — Kit Gestión de Personal met roterende diensten met respect voor de cao, urenregistratie en gegenereerde personeelsmaaltijden.",
      "23:00 · HACCP geconsolideerd — registers van de 6 verkooppunten ondertekend en geëxporteerd, rapport aan de F&B Director en aan corporate verzonden in PDF."
    ],
    "productsTitle": "Downloadbare Templates en Kits voor Hotels",
    "productIds": [
      "kit-tareas-hotel",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Het coördineren van 6 F&B-verkooppunten in een hotel met 200 kamers was een constante nachtmerrie. AI Chef Pro heeft alles voor ons geordend. De Kit de Tareas Hotel is goud waard en de rapportage aan de hoteldirecteur is nu automatisch in PDF. We hebben de RevPASH van het restaurant in 4 maanden met 12 % verhoogd, alleen al door betere controle.",
    "testimonialAuthor": "Cristina Núñez",
    "testimonialRole": "F&B Manager, hotel 4 sterren met 200 kamers",
    "faqTitle": "Veelgestelde Vragen van F&B Managers",
    "faqs": [
      {
        "q": "Werkt het voor een boutiquehotel of een grote keten?",
        "a": "Beide. De templates schalen van hotels met 30 kamers tot ketens met honderden eigendommen. Er is een bedrijfsonboarding voor grote ketens."
      },
      {
        "q": "Deckt het naast F&B ook housekeeping?",
        "a": "Ja. De Kit de Tareas Hotel bevat specifieke housekeeping-templates naast de 5 F&B-verkooppunten."
      },
      {
        "q": "Integreert het met ons PMS of Opera?",
        "a": "Het exporteert Excel, PDF en CSV die compatibel zijn met de meeste PMS- en hotelsystemen. De gegevens kunnen handmatig worden geïntegreerd bij de afsluiting van elke dienst of dag."
      },
      {
        "q": "Is er een bedrijfsplan voor hotelketens?",
        "a": "Ja. Vanaf een bepaald aantal eigendommen zijn er bedrijfsplannen met gepersonaliseerde onboarding, geconsolideerde dashboards per keten en prioritaire ondersteuning."
      },
      {
        "q": "Hoe beheert het de banketten en speciale evenementen?",
        "a": "Catering AI+ is geïntegreerd met de Kit de Tareas Hotel zodat banketten (bruiloften, zakelijk) samengaan met de reguliere F&B zonder dat productie of team botsen."
      },
      {
        "q": "En de kostenbeheersing per outlet?",
        "a": "De Kit Plan Financiero maakt het mogelijk om foodcost, productiviteit en marge afzonderlijk te analyseren voor ontbijt, restaurant, lobbybar, roomservice en banketten. Dat geeft een reëel beeld van welke outlet presteert en welke niet."
      }
    ],
    "ctaTitle": "Uw hotel-F&B gecoördineerd en zonder chaos.",
    "ctaSubtitle": "Praat met ons voor een gepersonaliseerde onboarding of start met het Lid-plan: € 10 per maand met 10.000 credits.",
    "seo": {
      "title": "AI voor Compleet Hotel (F&B + Housekeeping): Restaurant, Bar, Banketten | AI Chef Pro",
      "description": "AI-suite voor F&B Managers van hotels: ontbijtbuffet, restaurant, lobbybar, roomservice, banketten en housekeeping met gespecialiseerde agenten. Begin vandaag.",
      "keywords": "AI hotel F&B, F&B Manager AI, software F&B hotel, hotelbeheer AI, roomservice AI, hotelbanket AI, housekeeping software, hotel restaurant management AI, F&B Nederland",
      "ogImage": "https://aichef.pro/og/use-cases/hotel-completo.jpg"
    },
    "personalizationTitle": "Vanaf Minuut Eén Gepersonaliseerd voor Uw Hotel",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type hotel u beheert (boutique, 4 sterren, grote keten, all-inclusive), aantal kamers, welke F&B-outlets u exploiteert en op welke schaal. Vanaf dat moment reageert elke agent — van Executive Chef Pro tot het Financieel Plan — afgestemd op de realiteit van uw hotel: type gast, bezettingsgraad en daadwerkelijke operatie. Het is geen formulier: het is een kort gesprek dat de suite echt nuttig maakt voor een F&B Manager van een hotel.",
    "appsTitle": "De AI-Agenten die U als F&B Manager Gaat Gebruiken",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standaardisatie van recepten en technische bladen in alle hoteloutlets."
      },
      {
        "name": "Pro Restaurant Manager",
        "category": "Gastro Profile Pro",
        "description": "Assistent voor de managers van elke outlet met geconsolideerde rapportage naar de F&B Manager."
      },
      {
        "name": "Catering AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor bruiloftsbanketten, zakelijke evenementen en hotelgala's."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor de cocktails van de lobbybar, restaurantwijnen en sterke dranken."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor het à-la-carterestaurant van het hotel en casual opties van de roomservice."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van gerechten voor alle outlets met recept + kostenberekening CSV."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Hotel desserts: ontbijtbuffet, restaurant, roomservice en banketten."
      },
      {
        "name": "Personeelsmaaltijden",
        "category": "Gastro Profile Pro",
        "description": "Generator van personeelsmenu's voor grote 24/7-teams."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per recept, cruciaal in internationale hotels."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Nauwkeurige gegevens over verliezen en opbrengsten voor multi-outletcontrole."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Foodfotografie voor de hotelwebsite, roomservicemenu en banketten."
      }
    ],
    "metrics": [
      {
        "value": "+12 %",
        "label": "RevPASH in 4 maanden"
      },
      {
        "value": "6",
        "label": "gecoördineerde verkooppunten"
      },
      {
        "value": "×5",
        "label": "rapportagesnelheid aan de directeur"
      },
      {
        "value": "11+",
        "label": "agenten voor uw hotel"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "6 F&B-outlets met 6 verschillende systemen: ontbijt, restaurant, bar, roomservice, banketten en housekeeping zonder onderlinge samenhang",
        "HACCP op los printpapier verspreid over elke hotelkeuken, probleem bij inspecties",
        "Bruiloftsbanketten botsen met de productie van het reguliere restaurant en de roomservice",
        "Rapportage aan de F&B Director en aan corporate met verspreide en ongestructureerde bestanden",
        "24/7-roosters handmatig in Excel met 50+ medewerkers"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Kit de Tareas Hotel met specifieke templates per outlet, alles gecoördineerd in één systeem",
        "HACCP geconsolideerd in dashboard: registers vanaf mobiel, klaar voor inspectie en voor corporate",
        "Banketten geïntegreerd met Catering AI+ dat de productie van de reguliere F&B respecteert",
        "Rapportage aan de directeur en corporate in PDF rechtstreeks vanuit de Kit Plan Financiero",
        "Roosters met Kit Gestión de Personal: 24/7-diensten met respect voor de cao zonder verschuivingen"
      ]
    },
    "galleryTitle": "Hoe de F&B van een Compleet Hotel Werkt",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: restaurant, ontbijtbuffet, banket, lobbybar, roomservice en F&B-briefing met de keuken.",
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
    "h1": "AI voor Ambachtelijke IJssalons",
    "heroSubtitle": "Kostprijs per smaak met werkelijke kosten van melk, fruit en noten, plan seizoensproductie en creëer professionele branding met een suite van AI-agenten gespecialiseerd in ambachtelijke ijssalons.",
    "heroTagline": "IJs met echte marge en zonder papierwerk",
    "badge": "Voor ambachtelijke ijssalons en gelateria's",
    "painsTitle": "Wat een Ambachtelijke IJssalon Absoluut Moet Oplossen",
    "pains": [
      "Complexe kostprijsberekeningen met melk, room, vers fruit, noten en professionele pasta's die berekening per kg en per bol vereisen",
      "Hoge uitval in het productieatelier (ijsmachine, schokkoeling) en in de vitrine (langdurige blootstelling, rotatie) zonder echte controle",
      "APPCC-traceerbaarheid met gevoelige producten: melk, ei in sommige bases, noten met allergenen en kritieke temperaturen",
      "Extreme seizoensgebondenheid: hoogseizoen van mei tot september, winterdal dat rendabel gemaakt moet worden met taarten en desserts",
      "Zich onderscheiden in een concurrerende omgeving met eigen smaken, visuele branding van de vitrine, verpakking en sociale media",
      "Bestellingen binnenhalen voor ijstaarten en desserts op maat met marge terwijl de dagelijkse service wordt beheerd"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt bij een Ambachtelijke IJssalon",
    "features": [
      {
        "icon": "IceCream",
        "title": "Creatief IJs",
        "description": "Agent gespecialiseerd in ambachtelijk ijs: witte basis, gele basis, fruitbasis, sorbets, balancering van suikers, vaste stoffen en vetten voor een optimale textuur."
      },
      {
        "icon": "Cake",
        "title": "Creatieve Patisserie",
        "description": "Voor ijstaarten, semifreddo's, lepeldesserts en combinaties van ijs + biscuit die de gemiddelde besteding verhogen in het winterdal."
      },
      {
        "icon": "Cookie",
        "title": "Creatieve Chocolaterie",
        "description": "Voor toppings, ijsbonbons, pralines en geavanceerde combinaties van ijs + chocolade."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening per smaak",
        "description": "Creatief IJs levert recept + CSV-kostprijsberekening met technische balans (suikers, vaste stoffen, vetten); Kit de Escandallos Pro beheert dit met werkelijke marge per kg, per bol en per hoorntje."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Heladería",
        "description": "Sjablonen: voorbereiding ijsmachine, schokkoeling, vitrine bijvullen, temperatuurcontrole, rotatie van smaken, sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC ijssalon",
        "description": "Traceerbaarheid van melk, vers fruit, noten met allergenen en kritieke temperaturen in koelcel, ijsmachine en vitrine."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Seizoensplanning met belangrijke pieken: Moederdag, lente, zomer, Valentijnsdag en ijstaarten voor Kerst. Redactionele kalender voor de vitrine."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "AI-gastronomiefotografie + content voor Instagram: de ambachtelijke ijssalon leeft van de visuele impact van bakken en hoorntjes."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients Agent",
        "description": "Assistent voor de Sosa-catalogus voor professionele texturen, neutrale middelen, stabilisatoren en geconcentreerde pasta's voor ijsbereiding."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Ambachtelijke IJssalon met AI Chef Pro",
    "workflow": [
      "07:00 · Opening — checklist Kit de Tareas Heladería: controle van de koelcel, schokkoelen van mengsels die de vorige dag zijn bereid, voorbereiding van de ijsmachine.",
      "08:30 · Creatief IJs — u ontwikkelt een nieuwe seizoenssmaak (rode vruchten met balsamico). Creatieve Keuken levert recept + CSV-kostprijsberekening met technische balans.",
      "09:30 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke prijzen voor seizoensfruit en lokale melk, valideert de marge per kg en per bol.",
      "11:00 · Dagproductie — u laat de mengsels door de ijsmachine lopen, schokkoelt tot -18 °C, labelt met APPCC.",
      "13:30 · Vitrine bijvullen met professionele labels, controle van uitval door blootstelling per smaak.",
      "16:00 · Creatieve Patisserie — u ontwikkelt een ijstaart voor Moederdag met pistachesemifreddo, biscuitbodem en topping. CSV-kostprijsberekening klaar.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de referentieafbeelding van de nieuwe smaak en de Instagramposts voor de lancering.",
      "21:00 · Sluiting — grondige reiniging, APPCC ondertekend, planning van mengsels om vanavond te schokkoelen voor morgen."
    ],
    "productsTitle": "Downloadbare Sjablonen en Kits voor de IJssalon",
    "productIds": [
      "kit-tareas-heladeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "We gingen van losse vellen naar een systeem. Met Creatief IJs balanceren we suikers en vaste stoffen met technisch inzicht, en de Kit de Escandallos Pro bevestigt de werkelijke marge per bol en per kg met de actuele fruitprijzen. De uitval daalde met 40 % in 3 maanden en we ontdekten dat twee klassieke smaken niet rendabel waren.",
    "testimonialAuthor": "Laura Costa",
    "testimonialRole": "Eigenaresse, ambachtelijke ijssalon met eigen productieatelier",
    "faqTitle": "Veelgestelde Vragen van IJssalons",
    "faqs": [
      {
        "q": "Is het geschikt voor een kleine ijssalon, Italiaanse gelateria of keten?",
        "a": "Voor alle drie. De sjablonen schalen van een familie-ijssalon met één vestiging tot een keten met meerdere locaties en een gecentraliseerd productieatelier. De methodologie is dezelfde: gebalanceerd recept → CSV-kostprijsberekening → werkelijke marge."
      },
      {
        "q": "Deckt het de technische balans van bases (suikers, vaste stoffen, vetten)?",
        "a": "Ja. Creatief IJs redeneert als een professionele ijsbereider: suikerbalans met sucrose, dextrose en invertsuiker; totale vaste stoffen en vetten volgens technische norm; evenwicht om kristallisatie te voorkomen en romigheid te behouden."
      },
      {
        "q": "Hoe beheren we de sterke seizoensgebondenheid van de ijssalon?",
        "a": "Gastro Calendar plant de pieken vooraf (Moederdag, zomer, Valentijnsdag, Kerst met ijstaarten) en het winterdal met taarten, semifreddo's en lepeldesserts om de gemiddelde besteding op peil te houden. De Kit Plan Financiero projecteert de realistische seizoenscashflow."
      },
      {
        "q": "Is er controle op uitval in het productieatelier en de vitrine?",
        "a": "Ja. Mermas GenCal levert gegevens per proces (ijsmachine, schokkoeling, langdurige blootstelling in de vitrine, rotatie van smaken). Deze worden geïntegreerd in de kostprijsberekening van de Kit de Escandallos Pro, zodat de werkelijke kostprijs de uitval weerspiegelt, niet alleen het brute ingrediënt."
      },
      {
        "q": "Genereert het content voor vitrine, sociale media en Google Maps?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van elke smaak voor vitrine, web en sociale media; InstaFlow AI Pro plant Instagram met een redactionele kalender; MenuDish Local SEO trekt lokale klanten aan die zoeken naar \"ijssalon in de buurt\". Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw eigen bak en echte presentatie."
      }
    ],
    "ctaTitle": "Uw ijssalon met duidelijke marge en professionele branding.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor 10 € per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Ambachtelijke IJssalons: Kostprijsberekening per Smaak, Seizoensgebondenheid en Branding | AI Chef Pro",
      "description": "AI-suite voor ambachtelijke ijssalons: Creatief IJs, kostprijsberekening per smaak met technische balans, APPCC, seizoensplanning en visuele branding. Begin vandaag.",
      "keywords": "AI ijssalon, software ijssalon, kostprijsberekening ijs, ambachtelijke ijssalon AI, technische balans ijs, gelateria AI, ijssalon Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/heladeria.jpg"
    },
    "personalizationTitle": "Vanaf Minuut Eén Afgestemd op Uw IJssalon",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversatie-onboarding van 2 minuten waarin u vertelt welk type ijssalon u exploiteert (Italiaanse gelateria, Spaanse ambachtelijke ijssalon, ijssalon met eigen productieatelier of zonder atelier, gemengd met patisserie), teamgrootte, stad en stijl. Elke agent —van Creatief IJs tot Gastro Calendar— reageert afgestemd op uw product, markt en daadwerkelijke bedrijfsvoering.",
    "appsTitle": "De AI-agenten die U in Uw IJssalon Zult Gebruiken",
    "apps": [
      {
        "name": "Creatief IJs",
        "category": "Culinaire Creativiteit",
        "description": "Agent gespecialiseerd in ambachtelijk ijs met technische balans van bases, suikers, vaste stoffen en vetten."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Ijstaarten, semifreddo's, lepeldesserts en combinaties van ijs + biscuit."
      },
      {
        "name": "Creatieve Chocolaterie",
        "category": "Culinaire Creativiteit",
        "description": "Toppings, ijsbonbons, pralines en geavanceerde combinaties met chocolade."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van smaken en recepten met recept + CSV-kostprijsberekening."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus: neutrale middelen, stabilisatoren, geconcentreerde pasta's en professionele texturen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Nauwkeurige uitvalgegevens in ijsmachine, schokkoeling en vitrineblootstelling."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per smaak: zuivel, noten, gluten, ei."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-gastronomiefotografie als referentie voor vitrine, web en sociale media."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met redactionele kalender: de ijssalon leeft van visuele impact."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Lokale klanten aantrekken die zoeken naar \"ijssalon in de buurt\" op Google en Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Seizoensplanning: Moederdag, zomer, Valentijnsdag, ijstaarten voor Kerst."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Social Media",
        "description": "Pinterest trekt stabiel organisch verkeer aan voor ijstaarten en semifreddo's."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na het doorrekenen van smaken"
      },
      {
        "value": "−40 %",
        "label": "uitval in productieatelier en vitrine"
      },
      {
        "value": "×3",
        "label": "Instagram-engagement met GastroIMG"
      },
      {
        "value": "12+",
        "label": "agenten voor uw ijssalon"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Kostprijsberekeningen zonder technische balans, smaken die kristalliseren of romigheid verliezen zonder te weten waarom",
        "Uitval in ijsmachine, schokkoeling en vitrine zonder echte traceerbaarheid",
        "Geïmproviseerde vitrine en sociale media: mobiele foto's, zonder continuïteit",
        "Reactieve seizoensgebondenheid: de winter drukt de omzet zonder alternatieven",
        "APPCC op losse vellen papier verspreid door het productieatelier"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Professionele kostprijsberekeningen per smaak met technische balans en werkelijke marge per bol en per kg",
        "Uitval gecontroleerd met Mermas GenCal en specifieke ijssalon-sjablonen",
        "GastroIMG Gen+ + InstaFlow AI Pro genereren stabiele en professionele visuele content",
        "Gastro Calendar plant pieken en dalen met ijstaarten, semifreddo's en lepeldesserts",
        "APPCC vanaf mobiel met registraties klaar voor inspectie"
      ]
    },
    "galleryTitle": "Hoe een Ambachtelijke IJssalon Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: vitrine, ijsmachine, productieatelier, smaken, hoorntjes en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor chocolaterie en bonbonnerie",
    "heroSubtitle": "Kostprijsberekening per bonbon met echte cacaokosten en uurkosten van het atelier, plan seizoensproductie en leg professionele branding vast met een suite van AI-agenten gespecialiseerd in ambachtelijke chocolaterie.",
    "heroTagline": "Bonbon met echte marge en zonder papierwerk",
    "badge": "Voor ambachtelijke chocolaterieën en bonbonnerieën",
    "painsTitle": "Wat een chocolaterie niet kan negeren",
    "pains": [
      "Cacao met een volatiele prijs die elke week de werkelijke kost verandert zonder waarschuwing en dwingt om constant kostprijzen te herberekenen",
      "Verliezen in het atelier (mislukt tempereren, slecht gestolde mallen, restjes) en in de vitrine (rotatie, langdurige presentatie)",
      "Extreme seizoensgebondenheid: Kerst, Valentijnsdag, Pasen, Driekoningen concentreren een hoog percentage van de jaarlijkse omzet",
      "HACCP-traceerbaarheid met delicaat product: cacao, zuivel, noten, alcohol en kritische temperaturen bij elke stap",
      "Zich onderscheiden in een concurrerend gebied met auteur-bonbons, premium verpakking en visuele merkverhalen",
      "Bedrijfsopdrachten en bruiloften binnenhalen met marge terwijl de dagelijkse chocolaterie wordt beheerd"
    ],
    "featuresTitle": "Hoe AI Chef Pro helpt bij chocolaterie",
    "features": [
      {
        "icon": "Cookie",
        "title": "Creatieve Chocolaterie",
        "description": "Agent gespecialiseerd in professionele chocolaterie: bonbons, ganaches, pralines, tabletten, couverture en tempereertechniek."
      },
      {
        "icon": "Cake",
        "title": "Creatieve Patisserie",
        "description": "Voor chocoladedesserts, hapjes, brownies en geavanceerde combinaties chocolade + patisserie die het assortiment diversifiëren."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijs per stuk met uurkosten atelier",
        "description": "Creatieve Chocolaterie levert recept + kostprijs CSV; Kit de Escandallos Pro beheert dit met geïntegreerde uurkosten van het atelier in de echte marge per bonbon en per doos."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chocolatería",
        "description": "Sjablonen: tempereren, vormen, vullen met ganache, assemblage, verpakking, temperatuurcontrole in de koeling."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC chocolaterie",
        "description": "Traceerbaarheid van cacao, zuivel, noten, alcohol en professionele bewaring met gedocumenteerde temperatuurcurves."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Seizoensplanning met belangrijke data: Kerst, Valentijnsdag, Pasen, Driekoningen, Moederdag. Redactionele kalender voor de vitrine."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "AI-gastronomiefotografie + Pinterest, waar premium chocolaterie stabiel organisch verkeer vastlegt."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients Agent",
        "description": "Assistent voor de Sosa-catalogus voor technische couvertures, geconcentreerde pasta's, noten en professionele aroma's."
      },
      {
        "icon": "Sparkles",
        "title": "Mermas GenCal",
        "description": "Nauwkeurige verliesgegevens per proces (tempereren, vormen, restjes, vitrinepresentatie) geïntegreerd in de kostprijs."
      }
    ],
    "workflowTitle": "Een echte dag in een chocolaterie met AI Chef Pro",
    "workflow": [
      "07:00 · Opening — checklist Kit de Tareas Chocolatería: controle van de koeling, voorkristallisatie van de couverture, voorbereiding van mallen.",
      "08:30 · Creatieve Chocolaterie — u ontwikkelt een nieuwe bonbon voor Valentijnsdag met frambozen-vanilleganache. Creatieve Keuken levert recept + kostprijs CSV.",
      "09:30 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke cacaoprijzen en geïntegreerde uurkosten van het atelier, valideert de marge per bonbon en per doos van 12.",
      "11:00 · Productie van de dag — tempereren op marmer, vormen, vullen met ganache met spuitzak, snelkoelen en ontvormen.",
      "14:00 · Aanvullen van de vitrine met professionele dozen en etiketten, controle van presentatieverliezen.",
      "16:00 · Gastro Calendar — u bereidt de productieplanning voor Kerst voor (bedrijfsgeschenkdozen met 8 weken vooruit).",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — u genereert referentiefoto's van de nieuwe bonbon en geoptimaliseerde pins voor Pinterest.",
      "20:00 · Sluiting — grondige reiniging, HACCP ondertekend, planning van mengsels om vanavond te snelkoelen."
    ],
    "productsTitle": "Downloadbare sjablonen en kits voor de chocolaterie",
    "productIds": [
      "kit-tareas-chocolateria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "12.000 bonbons produceren voor Kerst zonder systeem was chaos. Met Creatieve Chocolaterie voor ontwerp, Kit de Escandallos Pro voor echte marge met actuele cacao en Gastro Calendar voor seizoensplanning, hebben we het seizoen gered en de marge met 7 punten verhoogd. De bedrijfsdozen worden nu afgesloten in één gesprek met een professioneel voorstel.",
    "testimonialAuthor": "Mónica Salazar",
    "testimonialRole": "Chocolatier en eigenaresse",
    "faqTitle": "Veelgestelde vragen over chocolaterieën",
    "faqs": [
      {
        "q": "Is het geschikt voor kleine ambachtelijke chocolaterie of een keten?",
        "a": "Voor beide. De sjablonen schalen van een familieatelier van 2 personen tot productie voor meerdere verkooppunten. De methodologie is hetzelfde: recept → kostprijs CSV → echte marge met uurkosten van het atelier."
      },
      {
        "q": "Deckt het bonbonnerie, tabletten, couverture en pralines?",
        "a": "Ja. Creatieve Chocolaterie redeneert als een professionele chocolatier: couverture tempereren volgens curves, ganaches met water- en vetbalans, pralines met geroosterde noten, gevulde tabletten met kristallisatietechniek."
      },
      {
        "q": "Hoe beheert u de volatiele cacaoprijs?",
        "a": "Kit de Escandallos Pro herberekent onmiddellijk de echte marge wanneer u de prijs van de couverture bijwerkt. Mermas GenCal voegt de kosten van verliezen per proces toe. Zo weerspiegelt de marge altijd de actuele kost, niet die van drie maanden geleden."
      },
      {
        "q": "Genereert het inhoud voor vitrine, sociale media en verpakking?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van elke bonbon voor vitrine, web en sociale media; Pinterest Pins Gen + InstaFlow AI Pro plannen visuele inhoud; MenuDish Local SEO trekt lokale klanten aan. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte bonbon op een bord."
      },
      {
        "q": "Hoe helpt het mij met de sterke seizoensgebondenheid?",
        "a": "Gastro Calendar plant de belangrijkste seizoenen (Kerst, Valentijnsdag, Pasen, Driekoningen, Moederdag) met 8-12 weken vooruit. Het Kit Plan Financiero projecteert de realistische seizoenscashflow zodat u met productie en kasgeld bij elke piek aankomt."
      }
    ],
    "ctaTitle": "Uw chocolaterie met duidelijke marge en professionele branding.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Chocolaterie en Bonbonnerie: Kostprijzen, Seizoensgebondenheid en Branding | AI Chef Pro",
      "description": "AI-suite voor ambachtelijke chocolaterieën: Creatieve Chocolaterie, kostprijzen per bonbon met uurkosten van het atelier, HACCP, seizoensplanning en branding. Begin vandaag.",
      "keywords": "AI chocolaterie, software chocolaterie, kostprijs bonbon, ambachtelijke chocolaterie AI, tempereertechniek, bonbonnerie Spanje, Kerstplanning chocolaterie",
      "ogImage": "https://aichef.pro/og/use-cases/chocolateria.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw chocolaterie vanaf de eerste minuut",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type chocolaterie u runt (ambachtelijk, bonbonnerie de auteur, chocolaterie met café, atelier voor verkoop aan horeca), teamgrootte, stad en specialiteit. Elke agent —van Creatieve Chocolaterie tot Gastro Calendar— reageert aangepast aan uw product, markt en werkelijke operatie.",
    "appsTitle": "De AI-agenten die u in uw chocolaterie gaat gebruiken",
    "apps": [
      {
        "name": "Creatieve Chocolaterie",
        "category": "Culinaire Creativiteit",
        "description": "Agent gespecialiseerd in professionele chocolaterie: bonbons, ganaches, pralines, tabletten en tempereertechniek."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Chocoladedesserts, hapjes, brownies en geavanceerde combinaties."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van nieuwe stukken met recept + kostprijs CSV."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus: technische couvertures, geconcentreerde pasta's, noten en professionele aroma's."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent voor de tSpoonLab-catalogus voor geavanceerde chocolatietoepassingen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen per proces (tempereren, vormen, restjes, vitrinepresentatie) in kostprijs."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per bonbon: zuivel, noten, gluten, alcohol."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-gastronomiefotografie als referentie voor vitrine, web, verpakking en sociale media."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Sociale Media",
        "description": "Pinterest legt stabiel organisch verkeer vast voor premium chocolaterie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Sociale Media",
        "description": "Instagram met redactionele kalender voor auteur-chocolaterie."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Sociale Media",
        "description": "Lokale klanten aantrekken die zoeken naar \"ambachtelijke chocolaterie in de buurt\" op Google en Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Sociale Media",
        "description": "Seizoensplanning: Kerst, Valentijnsdag, Pasen, Driekoningen, Moederdag."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "marge na het berekenen van bonbons"
      },
      {
        "value": "−35 %",
        "label": "verliezen in atelier en vitrine"
      },
      {
        "value": "×2",
        "label": "bedrijfsopdrachten Kerst"
      },
      {
        "value": "12+",
        "label": "agenten voor uw chocolaterie"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Kostprijzen zonder uurkosten van het atelier, complexe bonbons met verlies zonder het te weten",
        "Volatiele cacao die prijzen ontwricht zonder realtime herberekening",
        "Verliezen bij tempereren, vormen en vitrine zonder echte traceerbaarheid",
        "Reactieve seizoensproductie: u komt te laat voor Kerst en verliest bedrijfsopdrachten",
        "HACCP op los papier verspreid over het atelier"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Professionele kostprijs per bonbon met geïntegreerde uurkosten van het atelier en bijwerkbare cacao",
        "Verliezen beheerd met Mermas GenCal en specifieke chocolaterie-sjablonen",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ trekken stabiel verkeer en opdrachten aan",
        "Gastro Calendar plant Kerst en Valentijnsdag met 8-12 weken vooruit",
        "HACCP vanaf mobiel met registraties klaar voor inspectie"
      ]
    },
    "galleryTitle": "Hoe een ambachtelijke chocolaterie werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: vitrine, atelier, tempereren, bonbons, presentatie en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Creatief en Auteur Restaurant",
    "heroSubtitle": "Gastronomische brainstorm, avant-garde R&D, geavanceerde technische kostprijsberekeningen, premium technische fiches en storytelling voor auteur restaurants met een suite van professionele gastronomische AI-agenten.",
    "heroTagline": "Creativiteit met systeem, avant-garde met marge",
    "badge": "Voor creatieve en auteur restaurants",
    "painsTitle": "Wat een Creatief Restaurant Niet Kan Nalaten op te Lossen",
    "pains": [
      "Menu's die elke 6-12 weken veranderen met continu R&D en veel experimentatie",
      "Complexe kostprijsberekeningen met geavanceerde technieken (sferificaties, fermentaties, lange garingen, gedehydrateerde producten)",
      "Kleine teams met intense toewijding die professionele documentatie nodig hebben, geen improvisatie",
      "Storytelling en communicatie met klant, pers en sociale media zijn een belangrijke hefboom voor het merk",
      "Lange proeverijmenu's met volledige kostprijsberekening en coherente volgorde van gangen",
      "Zich onderscheiden in een niche verzadigd met creatieve voorstellen en de veeleisende gast aantrekken"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt in een Creatief Restaurant",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken + Food Pairing AI",
        "description": "Brainstorm voor auteur gerechten per seizoen, ingrediënt of techniek met wetenschappelijke basis. Creatieve Keuken levert recept + CSV-kostprijsberekening."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Avant-garde gastronomisch R&D: koji, kombucha's, shoyu's, garums, lactofermenten en innovatieve technieken met professionele ondersteuning."
      },
      {
        "icon": "Leaf",
        "title": "VegChef Plantaardig",
        "description": "Geavanceerde plantaardige, veganistische en vegetarische keuken voor auteur gerechten met professionele en nutritionele techniek."
      },
      {
        "icon": "Calculator",
        "title": "Geavanceerde technische kostprijsberekeningen",
        "description": "Kit de Escandallos Pro: u laadt de CSV van Creatieve Keuken met uw werkelijke prijzen voor gerechten met dure technieken en lange processen."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Diepgaand onderzoek naar trends, ambachtelijke producenten, opkomende technieken en referenties van de wereldwijde avant-garde."
      },
      {
        "icon": "MessageSquare",
        "title": "BlogPost SEO Gen+",
        "description": "Storytelling voor de blog van het restaurant, persdossier en communicatie met gastronomische media."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Hoogwaardige AI-gastronomische fotografie voor technische fiches, pers, restaurantwebsite en sociale media."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients Agent + tSpoonLab Agent",
        "description": "Assistenten voor de selectie van technische ingrediënten van Sosa en tSpoonLab, essentieel voor auteur keuken."
      },
      {
        "icon": "GraduationCap",
        "title": "Gastro Lexicon + Pro Prompts eBook",
        "description": "Tutor voor technische en wetenschappelijke definities + 300+ professionele prompts voor creativiteit en communicatie."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Creatief Restaurant met AI Chef Pro",
    "workflow": [
      "08:30 · Sonar Deep Research — u onderzoekt trends en seizoensproducten op Europese markten ter inspiratie voor de volgende menuwijziging.",
      "10:00 · Creatieve Keuken + Food Pairing AI — u ontwikkelt 14 gerechten voor het nieuwe proeverijmenu met techniek en initiële CSV-kostprijsberekening.",
      "12:00 · Fermentus Con AI+ — u werkt aan de basis van een belangrijk ferment in het menu: geïnoculeerde gerst koji voor 4 gerechten.",
      "14:00 · Sosa Ingredients Agent + tSpoonLab Agent — u selecteert technische ingrediënten voor texturen en toepassingen.",
      "15:30 · Kit de Escandallos Pro — u laadt de CSV's met uw werkelijke prijzen en schrapt 4 gerechten die niet passen binnen de doelwinstmarge (32%).",
      "17:00 · Pro Prompts eBook — u schrijft storytelling voor de 10 uiteindelijke gerechten: naam, verhaal en volledige technische fiche.",
      "18:30 · GastroIMG Gen+ — u genereert foto's van elk gerecht voor het persdossier en de website van het restaurant.",
      "19:30 · Service — team gecoördineerd met gecentraliseerde technische fiches, gangen van het proeverijmenu met gevalideerde volgorde."
    ],
    "productsTitle": "Downloadbare Sjablonen en Kits voor Creatief Restaurant",
    "productIds": [
      "kit-tareas-restaurante-creativo",
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "Ik verander het menu elke 6 weken en vroeger was het een week administratief afsluitwerk alleen al tussen kostprijsberekeningen, fiches en storytelling. Nu met AI Chef Pro gebeurt die afsluiting in 2 dagen: Creatieve Keuken stelt voor, Fermentus geeft mij R&D-ondersteuning, Sonar Deep Research levert trends op, en de Kit de Escandallos Pro sluit de marge. Het is letterlijk alsof u een extra R&D-team heeft.",
    "testimonialAuthor": "Adrián Lago",
    "testimonialRole": "Chef en eigenaar, auteur restaurant met 30 zitplaatsen",
    "faqTitle": "Veelgestelde Vragen van Creatieve Restaurants",
    "faqs": [
      {
        "q": "Begrijpt de AI geavanceerde auteur techniek?",
        "a": "Ja. Creatieve Keuken, Fermentus Con AI+, Food Pairing AI, VegChef en de receptenboeken per land zijn getraind met professionele kennis: technieken zoals sferificaties, lange fermentaties, gecontroleerde garingen, gelificaties, schuimen, gedehydrateerde producten en avant-garde processen."
      },
      {
        "q": "Zijn er specifieke proeverijmenu's?",
        "a": "Ja. De Kit de Tareas Restaurante Creativo en de Kit de Escandallos Pro hebben sjablonen voor proeverijmenu's met volledige kostprijsberekening, gangenvolgorde en pairing."
      },
      {
        "q": "Deckt het R&D en het testen van gerechten?",
        "a": "Ja. Sonar Deep Research levert trends en referenties; Creatieve Keuken + Fermentus ontwikkelen gerechten; Pro Prompts eBook heeft 300+ specifieke prompts voor iteratief R&D."
      },
      {
        "q": "Genereert het storytelling voor pers en gidsen?",
        "a": "Ja. BlogPost SEO Gen+ + Pro Prompts eBook + GastroIMG Gen+ maken het mogelijk om een persdossier op te stellen, communicatie met Michelin/Repsol/50Best-gidsen en notities voor gastronomische media."
      },
      {
        "q": "Werkt het voor avant-garde fermentatie?",
        "a": "Fermentus Con AI+ is de meest gebruikte agent door auteur chefs: het dekt koji, kombucha, shoyu, miso, garum, lactofermenten en innovatieve processen met wetenschappelijke ondersteuning."
      },
      {
        "q": "Hoe integreert het met Sosa en andere technische leveranciers?",
        "a": "Sosa Ingredients Agent en tSpoonLab Agent zijn specifieke assistenten van de catalogus van elke leverancier: ze helpen bij het selecteren van texturen, additieven en technische toepassingen met professioneel inzicht."
      }
    ],
    "ctaTitle": "Creativiteit met systeem, avant-garde met marge.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Creatief en Auteur Restaurant: R&D, Avant-garde en Storytelling | AI Chef Pro",
      "description": "AI-suite voor creatieve en auteur restaurants: Creatieve Keuken, Fermentus, Sonar Deep Research, geavanceerde kostprijsberekeningen, technische fiches en professionele storytelling.",
      "keywords": "AI creatief restaurant, auteur restaurant AI, software creatief restaurant, creatieve kostprijsberekeningen, gastronomische AI auteur, creatieve fermentatie AI, Fermentus, auteur restaurant Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-creativo.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd naar Uw Creatieve Keuken vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type creatieve keuken u leidt (auteur, gastrobotanie, fermenten, avant-garde, fusie), stad en referenties. Vanaf dat moment reageert elke agent —van Creatieve Keuken tot Sonar Deep Research— aangepast aan uw creatieve taal, gebruikelijke techniek en werkelijke positionering in de sector.",
    "appsTitle": "De AI-agenten die u in uw Creatief Restaurant gaat gebruiken",
    "apps": [
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van professionele gerechten met recept + CSV-kostprijsberekening klaar voor de Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Ingrediëntcombinaties en pairings met wetenschappelijke basis."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Avant-garde R&D: fermentaties, koji, kombucha, garum, miso."
      },
      {
        "name": "VegChef Plantaardig",
        "category": "Culinaire Creativiteit",
        "description": "Geavanceerde plantaardige, veganistische en vegetarische keuken voor auteur."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Auteur desserts met professionele patisserie techniek."
      },
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standaardisatie van technische fiches en keukenhandleidingen."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI-modellen + LLM",
        "description": "Diepgaand onderzoek: trends, producenten, wereldwijde avant-garde."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de Sosa-catalogus voor texturen en geavanceerde technieken."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de tSpoonLab-catalogus voor technische toepassingen."
      },
      {
        "name": "Gastro Lexicon",
        "category": "Gastro Kennis",
        "description": "Tutor met definities van technieken, processen en gastronomische wetenschap."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Hoogwaardige gastronomische fotografie voor pers en web."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "Blogposts met storytelling om organisch verkeer aan te trekken."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "snelheid afsluiten nieuw menu"
      },
      {
        "value": "14",
        "label": "gerechten in proeverijmenu"
      },
      {
        "value": "+5 pp",
        "label": "marge na werkelijke kostprijsberekening"
      },
      {
        "value": "13+",
        "label": "agenten voor auteur keuken"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Afsluiten nieuw menu: 15-30 dagen tussen R&D, kostprijsberekeningen, fiches en storytelling",
        "Geïmproviseerd R&D zonder documentatie, technieken die vergeten worden",
        "Storytelling voor pers op het laatste moment geschreven bij elke wijziging",
        "Technische fiches in een notitieboekje ontoegankelijk tijdens de service",
        "Trendonderzoek op intuïtie zonder toegang tot bronnen"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Afsluiten nieuw menu: 1-3 dagen met Creatieve Keuken, Fermentus en Kit de Escandallos Pro",
        "Gedocumenteerd R&D met iteratieve fiches, getraceerde en repliceerbare technieken",
        "Professionele storytelling in uren gegenereerd met BlogPost SEO Gen+",
        "Gecentraliseerde technische fiches toegankelijk vanaf de mobiel tijdens de gang",
        "Sonar Deep Research levert trends en professionele referenties"
      ]
    },
    "galleryTitle": "Hoe een Creatief Auteur Restaurant Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: R&D, fermenten, auteur plating, voorbereiding van speciale ingrediënten en intieme eetzaal.",
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
    "h1": "AI voor Gastronomisch Restaurant (Michelin/Repsol)",
    "heroSubtitle": "Premium kostprijsberekeningen, lange degustatiemenu's, uitgebreide brigade, rigoureuze HACCP en communicatie met gidsen en pers met een suite van AI-agenten ontworpen voor professionele haute cuisine.",
    "heroTagline": "Haute cuisine met systeem, avant-garde met richting",
    "badge": "Voor gastronomische restaurants Michelin en Repsol",
    "painsTitle": "Wat een Gastronomisch Restaurant Moet Oplossen",
    "pains": [
      "Veeleisende marge met premium product waarvan de kostprijs elke week verandert op de vismarkt en de markt",
      "Uitgebreide en sterk gecoördineerde brigade met strikte hiërarchie en rotatie van junior chefs",
      "Lange degustatiemenu's (8-15 gangen) met volledige kostprijsberekening, pairing en coherente verhaallijn",
      "Communicatie met Michelin/Repsol/50Best-gidsen en gespecialiseerde pers als kritieke hefboom",
      "Continu R&D van avant-garde met geavanceerde technieken en seizoensproducten",
      "Reserveringen maanden van tevoren met moeilijk te beheren annuleringen en onberispelijke service in de zaal"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt bij Haute Cuisine",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Executive Chef Pro",
        "description": "Standaardisatie van technische fiches en handleidingen voor een uitgebreide brigade met strikte hiërarchie."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken + Food Pairing AI",
        "description": "Brainstormen voor gerechten van het degustatiemenu met techniek en pairing. Creatieve Keuken levert recept + CSV-kostprijsberekening."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Avant-garde R&D: koji, kombucha's, shoyu's, garums, lactofermenten essentieel in de hedendaagse haute cuisine."
      },
      {
        "icon": "Calculator",
        "title": "Premium kostprijsberekeningen",
        "description": "Kit de Escandallos Pro: u laadt de CSV van Creatieve Keuken met uw werkelijke prijzen voor premium product met marge berekend per gang en per volledig degustatiemenu."
      },
      {
        "icon": "BookOpen",
        "title": "Sosa Ingredients Agent + tSpoonLab Agent",
        "description": "Assistenten van de meest gebruikte professionele catalogi in de haute cuisine voor geavanceerde technieken en toepassingen."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Diepgaand onderzoek naar wereldwijde trends, ambachtelijke producenten, opkomende technieken en referenties van de internationale avant-garde."
      },
      {
        "icon": "MessageSquare",
        "title": "BlogPost SEO Gen+ + Pro Prompts eBook",
        "description": "Professionele communicatie voor Michelin/Repsol/50Best-gidsen, persdossier en storytelling van het degustatiemenu."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "AI-gastronomiefotografie van hoog niveau voor website, gespecialiseerde pers en kandidatuurdossiers voor gidsen."
      },
      {
        "icon": "GraduationCap",
        "title": "Gastro Lexicon",
        "description": "Tutor met technische definities, processen en gastronomische wetenschap voor premium fiches en opleiding van de brigade."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Gastronomisch Restaurant met AI Chef Pro",
    "workflow": [
      "08:30 · Sonar Deep Research — u onderzoekt trends en seizoensproducten op Europese markten ter inspiratie voor de volgende wijziging van het degustatiemenu.",
      "10:00 · Creatieve Keuken + Food Pairing AI — u ontwikkelt 14 gangen voor het nieuwe degustatiemenu met geavanceerde techniek en CSV-kostprijsberekening.",
      "12:00 · Fermentus Con AI+ — u werkt aan de basis van een belangrijk ferment in het menu: vissengarum voor 4 gangen.",
      "14:00 · Sosa Ingredients Agent + tSpoonLab Agent — u selecteert technische ingrediënten voor texturen en premium toepassingen.",
      "15:30 · Kit de Escandallos Pro — u laadt de CSV's met uw marktprijzen en valideert de marge van het volledige degustatiemenu (€28/gang gemiddelde kostprijs).",
      "17:00 · Pro Prompts eBook + BlogPost SEO Gen+ — u schrijft storytelling voor de 14 gangen, dossier voor Michelin/Repsol-gidsen en een persbericht.",
      "18:30 · GastroIMG Gen+ — u genereert foto's van elke gang voor de website van het restaurant en het kandidatuurdossier voor gidsen.",
      "19:30 · Avondservice — gecoördineerde brigade met gecentraliseerde technische fiches, gangen van het degustatiemenu met gevalideerde volgorde en pairing gesynchroniseerd met de sommelier."
    ],
    "productsTitle": "Sjablonen, Kits en Downloadbare Gidsen voor Haute Cuisine",
    "productIds": [
      "guia-restaurante-gastronomico",
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "Het hebben van kostprijsberekening, technische fiche, gedocumenteerde fermenten en communicatie met gidsen in één systeem heeft de creatieve chaos van elke haute cuisine geordend. De Guía Restaurante Gastronómico was essentieel bij de opening van het tweede project: een professioneel businessplan dat de kandidatuur ondersteunt. Recente bekroning met gegevens in de hand.",
    "testimonialAuthor": "David Aramburu",
    "testimonialRole": "Executive Chef, gastronomisch restaurant met Michelin/Repsol-erkenning",
    "faqTitle": "Veelgestelde Vragen van Gastronomische Restaurants",
    "faqs": [
      {
        "q": "Is het geschikt voor een restaurant met een Michelinster of een aspirant-restaurant?",
        "a": "Voor beide. De sjablonen en agenten zijn ontworpen voor hoge eisen: rigoureuze standaardisatie, premium technische fiches, professionele kostprijsberekening en communicatie met gidsen."
      },
      {
        "q": "Is er een stapsgewijze gids voor het openen van een gastronomisch restaurant?",
        "a": "Ja, de Guía Restaurante Gastronómico (€85): 65 zitplaatsen, model businessplan voor kandidatuur, financieel plan, keukenplan, brigade, sommelier, operationele handleidingen en communicatie met gidsen. 20+ deliverables."
      },
      {
        "q": "Deckt het lange degustatiemenu's van 14-18 gangen?",
        "a": "Ja. De Kit de Escandallos Pro en de Kit de Tareas Restaurante Creativo hebben specifieke sjablonen voor degustatiemenu's met gangen, volledige kostprijsberekening, volgorde en pairing gesynchroniseerd met de sommelier."
      },
      {
        "q": "Genereert het professionele communicatie voor Michelin, Repsol en 50Best?",
        "a": "Ja. BlogPost SEO Gen+ + Pro Prompts eBook + GastroIMG Gen+ maken het mogelijk om een kandidatuurdossier op te stellen, communicatie met inspecteurs, persberichten en materialen voor de redacties van de gidsen."
      },
      {
        "q": "Werkt het voor avant-garde fermentatie?",
        "a": "Fermentus Con AI+ is een van de meest gebruikte agenten door Michelin-chefs: het dekt koji, kombucha, shoyu, miso, garum en lactofermenten met wetenschappelijke onderbouwing en echte toepassingen in haute cuisine-gangen."
      },
      {
        "q": "Hoe integreert het met premium leveranciers?",
        "a": "Sosa Ingredients Agent en tSpoonLab Agent zijn specifieke assistenten van professionele catalogi die veel worden gebruikt in de haute cuisine. Ze helpen bij het selecteren van texturen, additieven en technische toepassingen met een creatieve keukenbenadering."
      }
    ],
    "ctaTitle": "Haute cuisine met systeem, avant-garde met richting.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Gastronomisch Restaurant (Michelin/Repsol): Degustatiemenu, R&D en Communicatie | AI Chef Pro",
      "description": "AI-suite voor haute cuisine: Creatieve Keuken, Fermentus, Sonar Deep Research, premium kostprijsberekeningen, technische fiches, communicatie met Michelin- en Repsol-gidsen. Begin vandaag.",
      "keywords": "AI gastronomisch restaurant, Michelin-software, haute cuisine restaurant AI, premium kostprijsberekeningen, AI Repsol Soles, AI 50Best, creatieve fermentatie, Fermentus, degustatiemenu AI, gastronomie Spanje",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-gastronomico.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor Uw Gastronomisch Restaurant vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type keuken u leidt (Michelin, Repsol Soles, aspirant, hedendaagse haute cuisine, avant-gardistische fusie), aantal zitplaatsen, stad en referenties. Vanaf dat moment reageert elke agent — van Creatieve Keuken tot Sonar Deep Research — aangepast aan uw taal, gebruikelijke techniek en werkelijke positionering in de sector.",
    "appsTitle": "De AI-agenten die u in uw gastronomisch restaurant gaat gebruiken",
    "apps": [
      {
        "name": "Executive Chef Pro",
        "category": "Gastro Profile Pro",
        "description": "Standaardisatie van technische fiches en handleidingen voor uitgebreide brigade."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van gangen van het degustatiemenu met recept + CSV-kostprijsberekening."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Combinaties van ingrediënten en pairings met wetenschappelijke basis."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Avant-garde R&D: koji, kombucha, shoyu, miso, garum, lactofermenten."
      },
      {
        "name": "VegChef Plantaardig",
        "category": "Culinaire Creativiteit",
        "description": "Hoogwaardige plantaardige keuken voor plantaardige opties in het degustatiemenu."
      },
      {
        "name": "Creatieve Patisserie + Creatieve Chocolaterie",
        "category": "Culinaire Creativiteit",
        "description": "Haute cuisine desserts en petit fours als afsluiting."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI-modellen + LLM",
        "description": "Diepgaand onderzoek naar trends en wereldwijde avant-garde."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de Sosa-catalogus voor texturen en geavanceerde technieken."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro Leveranciers",
        "description": "Assistent van de tSpoonLab-catalogus voor technische toepassingen."
      },
      {
        "name": "Gastro Lexicon",
        "category": "Gastro Kennis",
        "description": "Tutor met technische en wetenschappelijke definities."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Hoogwaardige gastronomische fotografie voor pers en gidsen."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "Storytelling en professionele communicatie met gidsen en gespecialiseerde pers."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "snelheid afronden nieuw menu"
      },
      {
        "value": "14-18",
        "label": "gangen in degustatiemenu"
      },
      {
        "value": "+5 pp",
        "label": "marge na rigoureuze kostprijsberekening"
      },
      {
        "value": "13+",
        "label": "agenten voor haute cuisine"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Afronden van nieuw degustatiemenu: 15-30 dagen tussen R&D, kostprijsberekeningen, fiches en communicatie met gidsen",
        "R&D van fermenten zonder documentatie, technieken die niet worden gerepliceerd",
        "Storytelling voor pers en gidsen onder tijdsdruk bij elke wijziging",
        "Technische fiches in het notitieboekje van de chef, ontoegankelijk tijdens de gang",
        "Trendonderzoek op intuïtie en tijdschriften, zonder systematische toegang"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Afronden van degustatiemenu: 1-3 dagen met Creatieve Keuken, Fermentus en Kit de Escandallos Pro",
        "Gedocumenteerde R&D met iteratieve fiches, gevolgde en repliceerbare fermentaties door de brigade",
        "Professionele storytelling voor Michelin/Repsol/50Best gegenereerd in uren",
        "Gecentraliseerde technische fiches, toegankelijk via de mobiele telefoon tijdens de gang",
        "Sonar Deep Research levert direct trends van de wereldwijde avant-garde"
      ]
    },
    "galleryTitle": "Hoe een Gastronomisch Restaurant van Haute Cuisine Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: elegante eetzaal, plating van het degustatiemenu, premium keuken, sommelier en onberispelijke service.",
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
    "h1": "AI voor Mexicaans Restaurant",
    "heroSubtitle": "Ontwikkel sauzen met een precieze balans, bereken de kostprijs per taco en per menu met echte kosten, plan de productie van masa en nixtamalisatie, en creëer professionele branding met een suite van AI-agenten gespecialiseerd in authentieke Mexicaanse keuken.",
    "heroTagline": "Mexicaanse smaak met echte marge en authentieke techniek",
    "badge": "Voor Mexicaanse restaurants en taquerías",
    "painsTitle": "Waar een Mexicaans restaurant niet omheen kan",
    "pains": [
      "Complexe sauzen met veel chili's, roosteren en precieze balans (mole, salsa macha, adobos) die consistentie vereisen per dienst",
      "Het berekenen van de kostprijs van taco's, antojitos en gerechten met veel varianten van tortilla, vulling, sauzen en bijgerechten terwijl de foodcost coherent blijft",
      "Verliezen in masa, tortilla's, marinades en langzaam gegaarde eiwitten (carnitas, barbacoa, cochinita)",
      "Het standaardiseren van nixtamalisatie en massatechniek voor tortilla's, sopes en huaraches met consistente kwaliteit",
      "Zich onderscheiden in een competitieve omgeving met een authentiek menu, visuele branding van antojitos en regionale storytelling (Oaxaca, Yucatán, Puebla)",
      "Het binnenhalen van evenementen en Mexicaanse catering (bruiloften, nationale feestdagen) met marge terwijl de dagelijkse service wordt beheerd"
    ],
    "featuresTitle": "Hoe AI Chef Pro helpt in een Mexicaans restaurant",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Mexicaanse Keuken",
        "description": "Agent gespecialiseerd in authentieke Mexicaanse keuken: sauzen, mollen, marinades, antojitos, massatechniek en regionale keuken."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor hedendaagse en fusiongerechten met Mexicaanse basis: signature taco's, gecontroleerde fusies, moderne Mexicaanse desserts."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening per taco en per gerecht",
        "description": "Mexicaanse Keuken levert recept + kostprijs-CSV; Kit de Escandallos Pro beheert dit met werkelijke kosten per taco, foodcost % en adviesprijs."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Aanpasbare sjablonen: voorbereiding van masa, roosteren van chili's, marinades, comal, mise per station en sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC mexicano",
        "description": "Traceerbaarheid van chili's, nixtamalized masa, langzaam gegaarde eiwitten en kritische temperaturen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planning met belangrijke data: 5 mei, Día de Muertos, nationale feestdagen 16 september, Día de la Candelaria met tamales."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "AI-referentiefotografie voor gastronomie + Instagram met redactionele kalender: het Mexicaanse restaurant leeft van visuele impact en storytelling."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients Agent",
        "description": "Assistent van de Sosa-catalogus voor geavanceerde texturen, verdikkingsmiddelen, gedehydrateerde producten en techniek toegepast op de Mexicaanse keuken."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Mexicano",
        "description": "Premium downloadbare gids van 80 plaatsen met kostprijsberekeningen, technische fiches, financieel plan en specifieke operationele aspecten van de Mexicaanse keuken."
      }
    ],
    "workflowTitle": "Een echte dag in een Mexicaans restaurant met AI Chef Pro",
    "workflow": [
      "08:00 · Opening – checklist Kit de Tareas: roosteren van chili's voor salsa macha, voorbereiding van nixtamalized masa, marinade van cochinita pibil, mise van verse toppings.",
      "10:00 · Mexicaanse Keuken – u ontwikkelt een nieuwe signature taco van barbacoa met cascabel chilisaus en avocado. Creatieve Keuken levert recept + kostprijs-CSV.",
      "11:00 · Kit de Escandallos Pro – u laadt de CSV met uw werkelijke prijzen van gedroogde chili's, vlees, masa en avocado, valideert de marge per taco en foodcost %.",
      "13:00 · Middagdienst – het team repliceert met mise-sjablonen; de comal draait op volle toeren.",
      "17:00 · Pauze tussen diensten – Gastro Calendar plant het speciale Día de Muertos-menu met pan de muerto en mole negro.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro – u genereert de referentieafbeelding van de nieuwe taco en de berichten voor Instagram.",
      "21:00 · Avonddienst – pieken gecoördineerd met Personeelsmaaltijden voor het personeel vóór de rush.",
      "00:00 · Sluiting – grondige reiniging, APPCC ondertekend, voorbereiding van masa voor morgen."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor Mexicaans restaurant",
    "productIds": [
      "guia-restaurante-mexicano",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "We hebben taco voor taco doorgerekend en ontdekten dat drie signature-gerechten verliesgevend waren ondanks dat ze het best verkochten. We hebben ze opnieuw ontworpen met Mexicaanse Keuken, de marinade en de vleesopbrengst aangepast zonder de prijs te wijzigen, en de marge steeg met 5 punten. De planning van Día de Muertos met Gastro Calendar verdrievoudigde de omzet van die week.",
    "testimonialAuthor": "María José Hernández",
    "testimonialRole": "Chef en eigenaresse, hedendaags Mexicaans restaurant",
    "faqTitle": "Veelgestelde vragen over Mexicaanse restaurants",
    "faqs": [
      {
        "q": "Is het geschikt voor een casual taquería, een hedendaags Mexicaans restaurant of regionale keuken?",
        "a": "Voor alle drie. Mexicaanse Keuken dekt van traditionele taquería tot Mexicaanse haute cuisine, inclusief regionale keuken (Oaxaca, Yucatán, Puebla, Michoacán) met authentieke techniek."
      },
      {
        "q": "Deckt het nixtamalisatie en massatechniek?",
        "a": "Ja. Mexicaanse Keuken redeneert als een professionele Mexicaanse kok: nixtamalisatie met kalk, massabalans voor tortilla, sope, huarache, gordita en tlacoyo. Geen YouTube-recepten."
      },
      {
        "q": "Hoe helpt het mij met de complexiteit van Mexicaanse sauzen?",
        "a": "Mexicaanse Keuken levert sauzen met technische balans van chili's (roosteren, hydratatie, pittig-zoet-zuur balans), complexe gelaagde mollen en professionele marinades. Mermas GenCal voegt de kosten van gedroogde chili's toe aan de uiteindelijke kostprijs."
      },
      {
        "q": "Genereert het visuele inhoud voor Instagram, Glovo en Uber Eats?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen voor sociale media en bezorging; betere foto = meer klikken en betere ranking. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u met uw echt opgemaakte gerecht."
      },
      {
        "q": "Hoe helpt het mij met Mexicaanse feestdagen?",
        "a": "Gastro Calendar plant de belangrijkste data (Día de Muertos, Día de la Candelaria met tamales, nationale feestdagen, 5 mei) met speciale menu's en een redactionele kalender."
      }
    ],
    "ctaTitle": "Uw Mexicaans restaurant met echte marge en authentieke techniek",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Mexicaans restaurant: sauzen, kostprijsberekening en authentieke techniek | AI Chef Pro",
      "description": "AI-suite voor Mexicaanse restaurants: Mexicaanse Keuken, kostprijs per taco, planning van feestdagen, branding en APPCC. Begin vandaag.",
      "keywords": "AI Mexicaans restaurant, taquería software, taco kostprijs, Mexicaanse keuken AI, nixtamalisatie, Mexicaanse sauzen, Día de Muertos restaurant",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-mexicano.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw Mexicaans restaurant vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met de agent 'Wie Ben Ik?', een conversationele onboarding van 2 minuten waarin u vertelt wat voor soort Mexicaans restaurant u runt (casual taquería, hedendaags Mexicaans restaurant, regionale keuken, cantina, gourmet taquería, Mexicaanse food truck), teamgrootte, stad en specialiteit. Elke agent – van Mexicaanse Keuken tot Gastro Calendar – reageert aangepast aan uw product, markt en operationele realiteit.",
    "appsTitle": "De AI-agenten die u zult gebruiken in uw Mexicaans restaurant",
    "apps": [
      {
        "name": "Mexicaanse Keuken",
        "category": "Latam-recepten",
        "description": "Agent gespecialiseerd in authentieke Mexicaanse keuken: sauzen, mollen, marinades, antojitos, regionale techniek."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire creativiteit",
        "description": "Ontwikkeling van signature taco's en hedendaagse gerechten met recept + kostprijs-CSV."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Operationeel advies voor casual restaurants en professionele taquerías."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro-leveranciers",
        "description": "Sosa-catalogus voor texturen, verdikkingsmiddelen en techniek toegepast op de Mexicaanse keuken van de auteur."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpprogramma's",
        "description": "Verliezen in masa, chili's, marinades en langzaam gegaarde eiwitten."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpprogramma's",
        "description": "Automatische identificatie van allergenen per gerecht: gluten, zuivel, noten, soja."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-kennis",
        "description": "AI-referentiefotografie voor gastronomie voor Instagram, website, menu en bezorging."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en sociale media",
        "description": "Instagram met professionele redactionele kalender voor een taquería van de auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en sociale media",
        "description": "Lokale klanten aantrekken die zoeken naar 'taco's in de buurt' of 'Mexicaans restaurant' op Google en Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en sociale media",
        "description": "Día de Muertos, Día de la Candelaria, nationale feestdagen, 5 mei."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en sociale media",
        "description": "Pinterest trekt organisch verkeer aan voor taco's en antojitos met storytelling."
      },
      {
        "name": "Personeelsmaaltijden",
        "category": "Gastro Profile Pro",
        "description": "Generator van personeels-/familie-menu's die alle concepten doorkruist."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na het berekenen van taco's"
      },
      {
        "value": "×3",
        "label": "omzet op Día de Muertos"
      },
      {
        "value": "−20 %",
        "label": "verliezen in masa en marinades"
      },
      {
        "value": "12+",
        "label": "agenten voor uw Mexicaanse keuken"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde sauzen en mollen, inconsistente balans per dienst",
        "Kostprijsberekeningen zonder echte foodcost, signature-gerechten verliesgevend zonder het te weten",
        "Verliezen in masa, chili's en lang gegaarde eiwitten zonder traceerbaarheid",
        "Reactieve feestdagen: u komt te laat voor Día de Muertos zonder speciaal menu",
        "Geïmproviseerde Instagram en bezorgplatforms met mobiele foto's"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Sauzen en mollen met technisch inzicht, consistent per dienst",
        "Professionele kostprijs per taco en gerecht met gevalideerde foodcost",
        "Gecontroleerde verliezen met Mermas GenCal en specifieke sjablonen",
        "Feestdagen gepland met 8 weken vooruit met Gastro Calendar",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO trekken lokale klanten aan"
      ]
    },
    "galleryTitle": "Hoe een Mexicaans restaurant werkt",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: sauzen, taco's, comal, ingrediënten en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Peruaans Restaurant",
    "heroSubtitle": "Ontwikkel ceviches, tiraditos en causa's met technisch evenwicht, kostenberekening per gerecht met echte kosten van vis en ají, plan productie en creëer professionele branding met een suite van gastronomische AI-agenten gespecialiseerd in authentieke Peruaanse keuken.",
    "heroTagline": "Peruaanse keuken met echte marge en authentieke techniek",
    "badge": "Voor Peruaanse restaurants en cevicherieën",
    "painsTitle": "Wat een Peruaans restaurant absoluut moet oplossen",
    "pains": [
      "Ceviches en tiraditos met dagelijkse verse vis en tijgermelk gebalanceerd in zuurgraad, pittigheid en zout, dienst na dienst",
      "Kostenberekening van gerechten met geïmporteerde Peruaanse ingrediënten (gele ají, rocoto, panca, huacatay) waarvan de kosten per seizoen variëren",
      "Verliezen bij verse vis, zeevruchten, choclo, Peruaanse aardappelen en limoenen bij intensief gebruik",
      "Standaardiseren van kooktechniek voor eiwitten (anticucho, gegrilde kip, pachamanca) en bijgerechten (causa, aardappelen Huancaína-stijl)",
      "Zich onderscheiden in een concurrerend gebied met authentiek menu (criollo, costeño, Andes, Amazone), visuele branding en regionale storytelling",
      "Binnenhalen van delivery- en evenementbestellingen terwijl de kwaliteit van de ceviche buiten het optimale consumptievenster behouden blijft"
    ],
    "featuresTitle": "Hoe AI Chef Pro helpt in een Peruaans restaurant",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Peruaanse Keuken",
        "description": "Agent gespecialiseerd in authentieke Peruaanse keuken: ceviches, tiraditos, causa's, anticuchos, pachamanca, criollo-techniek, costeño, Andes en Amazone."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor hedendaagse en auteur-gerechten met Peruaanse basis: signature causa's, gecontroleerde fusies, moderne Peruaanse desserts."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Pairings met pisco, Chileense wijnen en bier voor uw Peruaanse kaart op wetenschappelijke basis."
      },
      {
        "icon": "Calculator",
        "title": "Kostenberekening per gerecht",
        "description": "Peruaanse Keuken levert recept + kostenberekening CSV; Kit de Escandallos Pro beheert dit met echte kosten per ceviche, foodcost % en voorgestelde prijs."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Sjablonen: voorbereiding van tijgermelk, marinades van anticucho, mise van zeevruchten, aardappelen Huancaína-stijl, sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC peruano",
        "description": "Traceerbaarheid van verse vis, zeevruchten, ajíes en kritische temperaturen in ceviche en tiradito."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planning met belangrijke data: Onafhankelijkheidsdag 28 juli, Dag van de Ceviche, Mistura, Dag van de Pisco Sour."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "AI-referentiefotografie van ceviches en tiraditos + Instagram: het Peruaanse restaurant leeft van de visuele impact van kleur."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Peruano",
        "description": "Premium downloadbare gids van 80 plaatsen met kostenberekeningen, technische fiches, financieel plan en specifieke operatie van de Peruaanse keuken."
      }
    ],
    "workflowTitle": "Een echte dag in een Peruaans restaurant met AI Chef Pro",
    "workflow": [
      "08:00 · Opening — checklist Kit de Tareas: ontvangst van dagelijkse verse vis, voorbereiding van basistijgermelk, marinade van anticucho, hydratatie van gedroogde ajíes.",
      "10:00 · Peruaanse Keuken — u ontwikkelt een nieuwe tiradito van de vangst van de dag met tijgermelk van rocoto en mango. Creatieve Keuken levert recept + kostenberekening CSV.",
      "11:00 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke prijzen van verse vis, ajíes, choclo en aardappelen, en valideert de marge per gerecht.",
      "12:00 · Food Pairing AI — u valideert de pairing van de nieuwe tiradito met een pisco sour gemacereerd in kruiden.",
      "13:00 · Middagdienst — piek van de ceviche-kok, vlekkeloze mise.",
      "17:00 · Pauze tussen diensten — Gastro Calendar plant het menu van 28 juli (Onafhankelijkheid) met causa, anticuchos en pisco.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de referentieafbeelding van de nieuwe tiradito en de posts voor Instagram.",
      "23:00 · Sluiting — grondige reiniging, APPCC ondertekend, gecontroleerde afvoer van de vis van de dag."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor Peruaans restaurant",
    "productIds": [
      "guia-restaurante-peruano",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Peruaanse Keuken veranderde onze keuken. De tijgermelk heeft nu een gedocumenteerd technisch evenwicht, de ceviches komen in elke dienst hetzelfde uit, en de kostenberekeningen met verse vis tegen de dagprijs werken in realtime. De voorbereiding van het speciale menu van 28 juli met Gastro Calendar verdrievoudigde onze omzet.",
    "testimonialAuthor": "Carlos Fernández",
    "testimonialRole": "Chef en eigenaar, hedendaagse Peruaanse cevicherie",
    "faqTitle": "Veelgestelde vragen over Peruaanse restaurants",
    "faqs": [
      {
        "q": "Is het geschikt voor een casual cevicherie, een hedendaags Peruaans restaurant of regionale keuken?",
        "a": "Voor alle drie. Peruaanse Keuken dekt van traditionele cevicherie tot haute cuisine van de auteur, inclusief regionale keuken (criollo, costeño, Andes, Amazone) met authentieke techniek."
      },
      {
        "q": "Omvat het professionele ceviche-techniek en tijgermelk?",
        "a": "Ja. Peruaanse Keuken redeneert als een professionele ceviche-kok: balans van tijgermelk met zuurgraad, pittigheid en zout; optimaal marinadevenster per soort; integratie van ajíes met techniek."
      },
      {
        "q": "Hoe helpt het u met de variabele kosten van verse vis?",
        "a": "Kit de Escandallos Pro herberekent onmiddellijk de werkelijke marge wanneer u de prijs van de vis van de dag bijwerkt. Mermas GenCal voegt de kosten van verliezen per proces toe. Zo weerspiegelt de ceviche altijd de actuele kosten."
      },
      {
        "q": "Genereert het visuele content voor Instagram, Glovo en Uber Eats?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van de ceviche en tiradito voor Instagram, web en delivery; betere foto = meer klikken. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte opgemaakte ceviche."
      },
      {
        "q": "Hoe helpt het u met Peruaanse feestdagen en evenementen?",
        "a": "Gastro Calendar plant de belangrijkste data (28 juli Onafhankelijkheidsdag, Dag van de Ceviche, Dag van de Pisco Sour, Mistura) met speciale menu's en redactionele kalender."
      }
    ],
    "ctaTitle": "Uw Peruaans restaurant met echte marge en authentieke techniek.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Peruaans Restaurant: Ceviches, Kostenberekeningen en Authentieke Techniek | AI Chef Pro",
      "description": "AI-suite voor Peruaanse restaurants: Peruaanse Keuken, kostenberekeningen per ceviche, planning van feestdagen, branding en APPCC. Begin vandaag.",
      "keywords": "AI Peruaans restaurant, software cevicherie, kostenberekeningen ceviche, Peruaanse keuken AI, tijgermelk, gele ají, 28 juli Peruaans",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-peruano.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw Peruaans restaurant vanaf de eerste minuut",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt welk type Peruaans restaurant u runt (casual cevicherie, hedendaags Peruaans restaurant, regionale keuken, Andes-picanterie, kiprestaurant, auteurrestaurant), teamgrootte, stad en specialiteit. Elke agent — van Peruaanse Keuken tot Gastro Calendar — reageert aangepast aan uw product, markt en werkelijke operatie.",
    "appsTitle": "De AI-agenten die u in uw Peruaans restaurant gaat gebruiken",
    "apps": [
      {
        "name": "Peruaanse Keuken",
        "category": "Recepten uit Latam",
        "description": "Agent gespecialiseerd in authentieke Peruaanse keuken: ceviches, tiraditos, causa's, anticuchos, pachamanca."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire creativiteit",
        "description": "Ontwikkeling van signature tiraditos en hedendaagse gerechten met recept + kostenberekening CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire creativiteit",
        "description": "Pairings met pisco, wijnen en bier voor uw Peruaanse kaart."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Operationeel advies voor cevicherieën en Peruaanse restaurants."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro-leveranciers",
        "description": "Sosa-catalogus voor texturen en techniek toegepast op Peruaanse auteurkeuken."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpprogramma's",
        "description": "Verliezen bij verse vis, zeevruchten, ajíes en limoenen."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpprogramma's",
        "description": "Automatische identificatie van allergenen: vis, zeevruchten, gluten, zuivel."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-kennis",
        "description": "AI-referentiefotografie voor gastronomie voor Instagram, web, kaart en delivery."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en sociale media",
        "description": "Instagram met professionele redactionele kalender voor auteur-cevicherie."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en sociale media",
        "description": "Lokale klanten aantrekken die zoeken naar \"cevicherie in de buurt\" of \"Peruaans restaurant\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en sociale media",
        "description": "28 juli, Dag van de Ceviche, Mistura, Dag van de Pisco Sour."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor de pisco sour-bar en Peruaanse auteurcocktails."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge na het berekenen van ceviches"
      },
      {
        "value": "×3",
        "label": "omzet op 28 juli"
      },
      {
        "value": "−25 %",
        "label": "verliezen bij verse vis"
      },
      {
        "value": "12+",
        "label": "agenten voor uw Peruaanse keuken"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde tijgermelk, inconsistente balans dienst na dienst",
        "Kostenberekeningen niet bijgewerkt naar de dagprijs van verse vis",
        "Verliezen bij vis, ajíes en zeevruchten zonder echte traceerbaarheid",
        "Reactieve feestdagen: u komt te laat voor 28 juli zonder speciaal menu",
        "Geïmproviseerde Instagram en deliveryplatforms met mobiele foto's"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Tijgermelk met gedocumenteerd technisch evenwicht, consistente ceviches",
        "Realtime kostenberekening met de prijs van de vis van de dag",
        "Gecontroleerde verliezen met Mermas GenCal en specifieke sjablonen",
        "Feestdagen gepland met 8 weken vooruit",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO trekken lokale klanten aan"
      ]
    },
    "galleryTitle": "Hoe een Peruaans restaurant werkt",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: ceviche, tiradito, anticucho, ajíes en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Japans Restaurant",
    "heroSubtitle": "Ontwikkel sushi, ramen, robata en kaiseki met authentieke techniek, kostenberekening per stuk met echte viskosten, plan fermentatieproductie en leg minimalistische branding vast met een suite van culinaire AI-agenten gespecialiseerd in professionele Japanse keuken.",
    "heroTagline": "Japanse keuken met echte marge en authentieke techniek",
    "badge": "Voor Japanse restaurants, sushi bars en ramen-yas",
    "painsTitle": "Wat een Japans Restaurant Niet Kan Nalaten op te Lossen",
    "pains": [
      "Dagelijkse verse vis voor sashimi en sushi met volatiele kosten en strikte verliezen door het fileerproces",
      "Het standaardiseren van shari (sushirijst), nigiri en maki in elke dienst met technische balans van azijn, suiker en zout",
      "Lange bouillons (tonkotsu, dashi, shoyu, miso) die uren koken en nachtelijke planning vereisen",
      "Professionele fermentaties (koji, miso, zelfgemaakte shoyu, tsukemono) die tijd en traceerbaarheid vereisen",
      "Onderscheiden in een concurrerend gebied met authentieke techniek versus industriële sushi, minimalistische branding en Japanse storytelling",
      "Bestellingen voor bezorging aantrekken zonder kwaliteitsverlies van de sushi (optimaal venster 1-2 uur) en omakase-evenementen met marge"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt in een Japans Restaurant",
    "features": [
      {
        "icon": "Fish",
        "title": "Japanse Keuken",
        "description": "Agent gespecialiseerd in authentieke Japanse keuken: sushi, sashimi, ramen, robata, tempura, kaiseki, itamae-techniek en fermentatie."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Voor koji, miso, zelfgemaakte shoyu, amazake en geavanceerde fermentaties uit de Japanse keuken."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor hedendaagse gerechten en omakase met Japanse basis: signature nigiri, gecontroleerde fusies."
      },
      {
        "icon": "Calculator",
        "title": "Kostenberekening per stuk",
        "description": "Japanse Keuken levert recept + kostenberekening CSV; Kit de Escandallos Pro beheert dit met werkelijke kosten per nigiri, ramen en omakase."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Sjablonen: vis fileren, shari-prep, lange nachtbouillons, robata-mise, sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC",
        "description": "Traceerbaarheid van vis voor sushi, fermentaties, kritische temperaturen en conservering."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planning met belangrijke data: Hanami (kersenbloesem), Japans Nieuwjaar, Hina Matsuri, Sushi-dag."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Minimalistische AI-referentiefotografie + Instagram: het Japanse restaurant leeft van zen en schone visuele impact."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Japonés",
        "description": "Premium downloadbare gids voor 60 plaatsen met kostenberekeningen, technische fiches, financieel plan en specifieke operatie."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Japans Restaurant met AI Chef Pro",
    "workflow": [
      "07:00 · Opening — checklist Kit de Tareas: ontvangst van verse vis, fileerblokken voor sashimi, controle van de tonkotsu-bouillon die de hele nacht heeft gekookt.",
      "09:00 · Japanse Keuken — u ontwikkelt een nieuwe signature nigiri van hamachi met yuzu kosho. Creatieve Keuken levert recept + kostenberekening CSV.",
      "10:00 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke visprijzen van de dag en verse wasabi, valideert de marge per nigiri en omakase.",
      "11:00 · Fermentus Con AI+ — u controleert de voortgang van de zelfgemaakte miso (maand 6 van 12) en de nieuwe koji in de fermentatiekamer.",
      "13:00 · Middagdienst — sushi bar op volle toeren met itamae die voor de klant werkt.",
      "17:00 · Pauze tussen diensten — Gastro Calendar plant het speciale Hanami-menu met sakura mochi en kersenbloesem bento.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de referentieafbeelding van de nieuwe nigiri en de minimalistische posts voor Instagram.",
      "23:00 · Sluiting — grondige reiniging, APPCC ondertekend, prep van tonkotsu voor morgen (12 uur koken)."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Japans Restaurant",
    "productIds": [
      "guia-restaurante-japones",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Japanse Keuken heeft onze operatie veranderd. De balans van de shari is nu consistent, de tonkotsu komt elke dag hetzelfde uit, en de omakase heeft professionele kostenberekening met gevalideerde marge per stuk. Fermentus heeft ons geholpen bij het opzetten van het programma voor zelfgemaakte miso dat ons aanbod volledig onderscheidt.",
    "testimonialAuthor": "Hiroshi Tanaka",
    "testimonialRole": "Itamae en eigenaar, hedendaags Japans restaurant",
    "faqTitle": "Veelgestelde Vragen van Japanse Restaurants",
    "faqs": [
      {
        "q": "Is het geschikt voor sushi bar, ramen-ya, izakaya of kaiseki?",
        "a": "Voor allemaal. Japanse Keuken dekt van traditionele sushi tot haute cuisine kaiseki, inclusief ramen-ya, robata en izakaya met authentieke techniek."
      },
      {
        "q": "Deckt het itamae-techniek en Japanse fermentatie?",
        "a": "Ja. Japanse Keuken redeneert als een professionele itamae: fileertechniek, shari-balans, neta en combinaties; Fermentus dekt koji, miso, zelfgemaakte shoyu en amazake met professionele techniek."
      },
      {
        "q": "Hoe helpt het mij met de variabele kosten van vis voor sashimi?",
        "a": "Kit de Escandallos Pro herberekent onmiddellijk de marge wanneer u de visprijs van de dag bijwerkt. Mermas GenCal voegt de kosten van verliezen door het fileren toe. De nigiri weerspiegelt altijd de actuele kosten."
      },
      {
        "q": "Genereert het visuele content voor Instagram, Glovo en Uber Eats?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van de sushi voor Instagram, web en bezorging; betere foto = meer klikken. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echt opgemaakte gerecht."
      },
      {
        "q": "Hoe helpt het mij met Japanse feestdagen?",
        "a": "Gastro Calendar plant de belangrijkste data (Hanami met sakura, Japans Nieuwjaar met osechi ryori, Hina Matsuri, Sushi-dag) met speciale menu's en een minimalistische redactionele kalender."
      }
    ],
    "ctaTitle": "Uw Japanse restaurant met echte marge en authentieke techniek.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Japans Restaurant: Sushi, Kostenberekening en Itamae-techniek | AI Chef Pro",
      "description": "AI-suite voor Japanse restaurants: Japanse Keuken, Fermentus voor koji en miso, kostenberekening per stuk, planning van feestdagen. Begin vandaag.",
      "keywords": "AI Japans restaurant, sushi bar software, sushi kostenberekening, Japanse keuken AI, koji miso shoyu, ramen tonkotsu, professionele itamae",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-japones.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor Uw Japanse Restaurant vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversatie-onboarding van 2 minuten waarin u vertelt welk type Japans restaurant u runt (sushi bar, ramen-ya, izakaya, kaiseki, omakase, hedendaagse Japanse keuken), teamgrootte, stad en specialiteit. Elke agent —van Japanse Keuken tot Gastro Calendar— reageert afgestemd op uw product, markt en werkelijke operatie.",
    "appsTitle": "De AI-agenten die u gaat gebruiken in uw Japanse restaurant",
    "apps": [
      {
        "name": "Japanse Keuken",
        "category": "Aziatische Recepten",
        "description": "Agent gespecialiseerd in authentieke Japanse keuken: sushi, sashimi, ramen, robata, kaiseki."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Koji, miso, zelfgemaakte shoyu, amazake en geavanceerde fermentaties."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van signature nigiri en omakase met recept + kostenberekening CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Pairings met sake, Japanse whisky, bier en wijnen voor uw kaart."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus voor texturen en techniek toegepast op Japanse fusionkeuken."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Hulpprogramma's",
        "description": "Verliezen bij het fileren van vis, sashimi en lange bouillons."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Hulpprogramma's",
        "description": "Automatische identificatie van allergenen: vis, schaaldieren, soja, gluten, sesam."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Minimalistische AI-referentiefotografie voor Instagram, web, kaart en bezorging."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met minimalistische redactionele kalender voor een sushi bar van de auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Lokale klanten aantrekken die zoeken naar \"sushi in de buurt\" of \"ramen in de buurt\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Hanami, Japans Nieuwjaar, Hina Matsuri, Sushi-dag."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor de sakebar, Japanse whisky en cocktails met Japanse basis."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge na kostenberekening van omakase"
      },
      {
        "value": "×3",
        "label": "Instagram-engagement met GastroIMG"
      },
      {
        "value": "−20 %",
        "label": "verliezen bij het fileren van vis"
      },
      {
        "value": "12+",
        "label": "agenten voor uw Japanse keuken"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Shari en techniek geïmproviseerd, inconsistente balans tussen itamae",
        "Kostenberekeningen niet bijgewerkt naar de dagelijkse visprijs",
        "Lange bouillons (tonkotsu) zonder traceerbaarheid of rigoureuze planning",
        "Zelfgemaakte fermentaties (miso, shoyu) zonder gedocumenteerd programma",
        "Geïmproviseerde Instagram en bezorgplatforms met mobiele foto's"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Shari, neta en techniek met professioneel inzicht, consistentie per dienst",
        "Realtime kostenberekening met de visprijs van de dag",
        "Lange bouillons gepland met specifieke sjablonen en ondertekende APPCC",
        "Fermentatieprogramma met Fermentus Con AI+ professioneel gedocumenteerd",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO trekken lokale klanten aan"
      ]
    },
    "galleryTitle": "Hoe een Japans Restaurant Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: sushi, ramen, robata, ingrediënten en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Nikkei-restaurants",
    "heroSubtitle": "Ontwikkel nikkei-tiradito's, fusion-sushi en robata met authentieke Peruaans-Japanse techniek, bereken de kostprijs per gerecht op basis van de werkelijke kosten en creëer professionele branding met een suite van gastronomische AI-agenten gespecialiseerd in de nikkei-keuken.",
    "heroTagline": "Nikkei-keuken met echte marge en authentieke techniek",
    "badge": "Voor nikkei-restaurants en Peruaans-Japanse fusion",
    "painsTitle": "Wat een Nikkei-restaurant absoluut moet oplossen",
    "pains": [
      "Complexe Peruaans-Japanse combinaties met een precieze balans van gele Peruaanse peper, yuzu, miso, ponzu en shoyu",
      "Dagelijkse verse vis voor tiradito's en sushi met een wisselende kostprijs, zorgvuldig fileren en itamae-techniek toegepast op de Peruaanse keuken",
      "Signature-tiradito's, nikkei-sushi en anticucho's met miso-panca-marinade per dienst standaardiseren",
      "De kostprijs berekenen van gerechten met geïmporteerde ingrediënten (gele Peruaanse peper, panca-peper, yuzu, dashi) waarvan de prijs per seizoen varieert",
      "Zich onderscheiden van traditioneel Japans of puur Peruaans met authentieke fusion-storytelling en visuele signatuur-branding",
      "Omakase-nikkei-bestellingen en evenementen binnenhalen terwijl de kwaliteit van de rauwe producten behouden blijft"
    ],
    "featuresTitle": "Hoe AI Chef Pro een Nikkei-restaurant helpt",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Japanse Keuken + Peruaanse Keuken",
        "description": "Combinatie van AI-agenten gespecialiseerd in beide culturen: itamae-techniek toegepast op Peruaanse tiradito's, gele Peruaanse peper in nigiri, miso-anticucho's."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Voor koji, miso en zelfgemaakte shoyu, aangepast aan nikkei-fusion met panca-peper en huacatay."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Pairings met sake, pisco, Chileense wijnen en Japans bier voor uw nikkei-menu."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening per gerecht",
        "description": "Creatieve Keuken levert recept + kostprijs-CSV; Kit de Escandallos Pro beheert dit met de werkelijke kostprijs per tiradito en omakase-nikkei."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Sjablonen: vis fileren, voorbereiding van tijgermelk met yuzu, nikkei-marinade, mise-en-place voor de robata, sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC nikkei",
        "description": "Traceerbaarheid van vis, fermenten, pepers en kritische temperaturen bij rauwe producten."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Crossplanning: Japanse en Peruaanse feestdagen, fusion-evenementen, seizoensgebonden omakase-nikkei."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Redactionele AI-fotografie als referentie + Instagram: nikkei leeft van de visuele impact van kleur en compositie."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Nikkei",
        "description": "Premium-downloadbare gids voor 60 zitplaatsen met kostprijsberekeningen, technische fiches, financieel plan en specifieke nikkei-werkwijze."
      }
    ],
    "workflowTitle": "Een echte dag in een Nikkei-restaurant met AI Chef Pro",
    "workflow": [
      "07:00 · Opening — checklist Kit de Tareas: ontvangst van verse vis, fileren voor tiradito's en nigiri, voorbereiding van tijgermelk met yuzu, marinade voor miso-panca-anticucho's.",
      "09:00 · Japanse Keuken + Peruaanse Keuken — u ontwikkelt een nieuwe hamachi-tiradito met tijgermelk van yuzu en gele Peruaanse peper. Creatieve Keuken levert recept + kostprijs-CSV.",
      "10:00 · Kit de Escandallos Pro — u laadt de CSV met uw actuele prijzen voor de vis van de dag, gele Peruaanse peper en yuzu en valideert de marge per tiradito en omakase-nikkei.",
      "11:00 · Fermentus Con AI+ — u controleert de voortgang van de zelfgemaakte miso met panca-peper (maand 4 van 8).",
      "12:00 · Food Pairing AI — u valideert de pairing van de nieuwe tiradito met een junmai-sake en een pisco die is gemacereerd in shisobladeren.",
      "13:00 · Middagdienst — robata op volle toeren met miso-anticucho's, de sushibar werkt met signature-tiradito's.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de referentieafbeelding van de nieuwe nikkei-tiradito en de redactionele posts voor Instagram.",
      "23:00 · Sluiting — grondige reiniging, APPCC ondertekend, gecontroleerde afvalverwerking, voorbereiding voor morgen."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor uw Nikkei-restaurant",
    "productIds": [
      "guia-restaurante-nikkei",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "De combinatie van de AI-agenten Japanse Keuken en Peruaanse Keuken heeft onze propositie veranderd. De tiradito's hebben nu een gedocumenteerd technisch evenwicht, de omakase-nikkei gaat uit met een per stuk gevalideerde kostprijs, en het programma voor zelfgemaakte miso met panca-peper van Fermentus onderscheidt ons volledig. We hebben de marge met 7 procentpunten verhoogd.",
    "testimonialAuthor": "Yui Sato",
    "testimonialRole": "Chef en eigenaresse, signatuur-nikkei-restaurant",
    "faqTitle": "Veelgestelde vragen over Nikkei-restaurants",
    "faqs": [
      {
        "q": "Is het geschikt voor hedendaagse nikkei, een nikkei-sushibar of een Peruaans visrestaurant met Japanse techniek?",
        "a": "Voor alle drie. Japanse Keuken + Peruaanse Keuken vullen elkaar aan om alles te dekken, van nikkei-sushi tot tiradito's met tijgermelk met yuzu of ponzu."
      },
      {
        "q": "Hoe helpt het mij met de balans tussen Peruaanse en Japanse technieken?",
        "a": "Creatieve Keuken orkestreert de twee AI-agenten: het redeneert vanuit authentieke fusion (geen verwarrende fusion), met respect voor itamae-techniek voor rauwe producten en Peruaanse balans voor tijgermelk en marinades."
      },
      {
        "q": "Hoe beheer ik de wisselende kostprijs van vis en geïmporteerde Peruaanse ingrediënten?",
        "a": "Kit de Escandallos Pro herberekent direct de marge zodra u de prijzen van de dagvis en de pepers/yuzu bijwerkt. Mermas GenCal voegt de kosten van verliezen per proces toe."
      },
      {
        "q": "Genereert het visuele content voor Instagram en bezorging?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentiebeelden van de nikkei-tiradito voor Instagram, web en bezorging. Houd er rekening mee dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw werkelijk opgemaakte gerecht."
      },
      {
        "q": "Hoe helpt het mij met de combinatie van Peruaanse en Japanse feestdagen?",
        "a": "Gastro Calendar plant de belangrijkste data van beide culturen (Peruaanse 28 juli, Japanse Hanami, Ceviche-dag, Japans Nieuwjaar) met seizoensgebonden omakase-nikkei en fusion-storytelling."
      }
    ],
    "ctaTitle": "Uw nikkei-restaurant met echte marge en authentieke techniek.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor € 10 per maand met 10.000 credits om alle AI-agenten te gebruiken.",
    "seo": {
      "title": "AI voor Nikkei-restaurants: Tiradito's, kostprijsberekening en fusiontechniek | AI Chef Pro",
      "description": "AI-suite voor nikkei-restaurants: Japanse Keuken + Peruaanse Keuken, kostprijsberekening per tiradito, omakase-nikkei, branding en APPCC. Begin vandaag.",
      "keywords": "AI nikkei-restaurant, nikkei-software, kostprijsberekening nikkei-tiradito, nikkei-keuken AI, gele Peruaanse peper yuzu, nikkei-sushi, Peruaans-Japanse fusion",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-nikkei.jpg"
    },
    "personalizationTitle": "Vanaf de eerste minuut gepersonaliseerd voor uw Nikkei-restaurant",
    "personalizationBody": "AI Chef Pro start met de AI-agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor soort nikkei u runt (hedendaagse signatuur-nikkei, nikkei-sushibar, Peruaans visrestaurant met Japanse techniek, omakase-nikkei), teamgrootte, stad en specialiteit. Elke AI-agent reageert afgestemd op uw product, markt en daadwerkelijke werkwijze.",
    "appsTitle": "De AI-agenten die u in uw Nikkei-restaurant gaat gebruiken",
    "apps": [
      {
        "name": "Japanse Keuken",
        "category": "Aziatische receptencollecties",
        "description": "Itamae-techniek, fileren, sushi, sashimi en robata toegepast op nikkei-fusion."
      },
      {
        "name": "Peruaanse Keuken",
        "category": "Receptencollecties Latijns-Amerika",
        "description": "Ceviches, tiradito's, anticucho's en Peruaanse techniek toegepast op nikkei-fusion."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Fusie-orkestrator: signature-tiradito's, nikkei-sushi, omakase met authentieke basis."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Koji, zelfgemaakte miso met panca-peper, shoyu en gecombineerde fermenten."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Pairings met sake, pisco, Chileense wijnen en Japans bier."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro-leveranciers",
        "description": "Sosa-catalogus voor texturen en techniek toegepast op signatuur-nikkei-keuken."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpprogramma's",
        "description": "Verliezen bij het fileren van vis, pepers en langdurige marinades."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpprogramma's",
        "description": "Automatische identificatie van allergenen: vis, schelpdieren, soja, gluten, sesam, noten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro-kennis",
        "description": "Redactionele AI-fotografie als referentie voor Instagram, web, menu en bezorging."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en sociale media",
        "description": "Instagram met een professionele redactionele kalender voor signatuur-nikkei."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en sociale media",
        "description": "Lokale klanten aantrekken die op Google en Maps zoeken naar \"nikkei in de buurt\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en sociale media",
        "description": "Feestdagen in samenhang: Hanami, 28 juli, Ceviche-dag, Japans Nieuwjaar."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "marge na kostprijsberekening van omakase-nikkei"
      },
      {
        "value": "×3",
        "label": "Instagram-engagement met GastroIMG"
      },
      {
        "value": "−25 %",
        "label": "mindere verliezen bij vis en pepers"
      },
      {
        "value": "12+",
        "label": "AI-agenten voor uw nikkei-keuken"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde fusion zonder technische balans tussen culturen",
        "Kostprijsberekeningen die niet zijn aangepast aan de prijs van vis en pepers",
        "Nikkei-sushi en tiradito's met wisselende consistentie tussen diensten",
        "Zelfgemaakt fermentenprogramma zonder professionele documentatie",
        "Geïmproviseerde Instagram zonder authentieke fusion-storytelling"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Authentieke fusion met gedocumenteerde techniek uit beide culturen",
        "Realtime kostprijsberekening met actuele prijzen",
        "Nikkei-sushi en tiradito's met consistent technisch evenwicht",
        "Fermentus-programma met professioneel gedocumenteerde miso-panca",
        "GastroIMG Gen+ + InstaFlow + authentieke nikkei-fusion-storytelling"
      ]
    },
    "galleryTitle": "Zo werkt een Nikkei-restaurant",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: tiradito's, nikkei-sushi, miso-anticucho's, ingrediënten en team. Afbeeldingen gegenereerd met AI als visuele referentie van het concept.",
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
    "h1": "AI voor plantaardige en veganistische restaurants",
    "heroSubtitle": "Ontwikkel uw plantaardige menu's met nutritioneel evenwicht, kostprijsberekening per bowl en vegan burger met reële kosten, plan plantaardige fermenten en creëer frisse branding met een suite van gastronomische AI-agenten gespecialiseerd in professionele plantaardige keuken.",
    "heroTagline": "Plantaardige keuken met reële marge en geavanceerde techniek",
    "badge": "Voor plantaardige, veganistische en gezonde restaurants",
    "painsTitle": "Wat een plantaardig restaurant absoluut moet oplossen",
    "pains": [
      "Diepe umami bereiken in 100% plantaardige keuken met fermenten, gerookte producten, koji en geavanceerde techniek (zonder industriële shortcuts)",
      "Kostprijsberekeningen maken voor bowls, vegan burgers en plantaardige gerechten met veel variaties aan toppings en plantaardige eiwitten",
      "Hoge verliezen bij verse producten (seizoensgroenten, fruit, kruiden, microgreens) met korte houdbaarheid",
      "Het standaardiseren van zelfgemaakte plantaardige eiwitten (seitan, tempeh, gemarineerde tofu) en plantaardige toppings/sauzen",
      "Zich onderscheiden in een competitieve omgeving met een plantaardig auteurstmenu, frisse visuele branding en duurzaam storytelling",
      "Delivery-orders aantrekken met verse producten terwijl de presentatie en kwaliteit van de bowl behouden blijven"
    ],
    "featuresTitle": "Hoe AI Chef Pro helpt in een plantaardig restaurant",
    "features": [
      {
        "icon": "Sprout",
        "title": "VegChef Plantaardig",
        "description": "Agent gespecialiseerd in professionele plantaardige, veganistische en vegetarische keuken: bowls, burgers, plantaardige eiwitten, geavanceerde techniek."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Voor plantaardige koji, zelfgemaakte miso, shoyu, kimchi, kombucha, lactofermenten en diepe umami zonder dierlijke producten."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor hedendaagse plantaardige en auteurstgerechten met plantaardige basis: signature bowls, vegan desserts, fusies."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Pairings met vegan wijnen, kombucha en functionele dranken voor uw plantaardige menu."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening per bowl en burger",
        "description": "VegChef levert recept + kostprijsberekening CSV; Kit de Escandallos Pro beheert het met reële kosten per bowl, food cost % en voorgestelde prijs."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Sjablonen: voorbereiding van plantaardige eiwitten, fermenten, mise van verse toppings, marinades, sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC plantaardig",
        "description": "Traceerbaarheid van fermenten, zelfgemaakte plantaardige eiwitten, verse kruiden en kritische temperaturen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planning met belangrijke data: Veganuary (januari), Wereld Vegan Dag, Earth Day, seizoenen van lokale groenten."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Levendige AI-referentiefotografie + Instagram: plantaardig leeft van de visuele impact van kleur."
      }
    ],
    "workflowTitle": "Een echte dag in een plantaardig restaurant met AI Chef Pro",
    "workflow": [
      "07:00 · Opening — checklist Kit de Tareas: controle van fermenten in de koeling, prep van plantaardige eiwitten (seitan, tempeh), marinades van tofu, mise van microgreens en eetbare bloemen.",
      "09:00 · VegChef Plantaardig — u ontwikkelt een nieuw signature bowl met quinoa, boerenkool, gemarineerde tempeh, zelfgemaakte kimchi en kurkuma-tahini. Creatieve Keuken levert recept + kostprijsberekening CSV.",
      "10:00 · Kit de Escandallos Pro — u laadt de CSV met uw reële prijzen voor quinoa, boerenkool, tempeh en tahini, valideert de marge per bowl en food cost %.",
      "11:00 · Fermentus Con AI+ — u controleert de voortgang van de zelfgemaakte miso (maand 6 van 12), de plantaardige koji en de nieuwe kimchi in de fermentatiekamer.",
      "12:00 · Food Pairing AI — u valideert de pairing van de nieuwe bowl met gemberkombucha en een vegan witte wijn.",
      "13:00 · Middagdienst — bowls volop, vegan burgers op de grill, mise van verse toppings.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de referentieafbeelding van de nieuwe bowl en de levendige posts voor Instagram.",
      "22:00 · Sluiting — grondige reiniging, APPCC ondertekend, voorbereiding van fermenten voor nachtelijke fermentatie."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor plantaardige restaurants",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "VegChef + Fermentus hebben onze propositie veranderd. We bereiken diepe umami zonder industriële shortcuts dankzij zelfgemaakte miso en plantaardige koji, en de kostprijsberekeningen per bowl met gemarineerde tempeh bevestigen dat plantaardig een hoge marge kan hebben. We stegen 6 punten en de acquisitie via Instagram met GastroIMG is x3.",
    "testimonialAuthor": "Lucía Ferrer",
    "testimonialRole": "Chef en eigenaresse, plantaardig auteurrestaurant",
    "faqTitle": "Veelgestelde vragen voor plantaardige restaurants",
    "faqs": [
      {
        "q": "Is het geschikt voor casual healthy bowls, vegan fine dining of plantaardige auteurstkeuken?",
        "a": "Voor alle drie. VegChef dekt van casual bowls tot vegan haute cuisine, inclusief plantaardige hamburgerzaken, keuken met geavanceerde techniek en professionele vegan desserts."
      },
      {
        "q": "Hoe bereikt u diepe umami in een 100% plantaardige keuken?",
        "a": "Fermentus Con AI+ dekt plantaardige koji, zelfgemaakte miso, shoyu, kimchi, kombucha en lactofermenten met professionele techniek. VegChef integreert gecontroleerd roken, gedehydrateerde producten, paddenstoelencorsten en lange plantaardige bouillons."
      },
      {
        "q": "Deckt het zelfgemaakte plantaardige eiwitten (seitan, tempeh, gemarineerde tofu)?",
        "a": "Ja. VegChef redeneert als een professionele plantaardige chef: technieken voor gekneed seitan, gefermenteerde tempeh, gemarineerde en geperste tofu, mock meats met textuurtechniek."
      },
      {
        "q": "Genereert het visuele content voor Instagram, Glovo en Uber Eats?",
        "a": "Ja. GastroIMG Gen+ genereert levendige referentieafbeeldingen van de bowls voor Instagram, web en delivery; plantaardig leeft van kleur. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte opgemaakte bowl."
      },
      {
        "q": "Hoe helpt het u met Veganuary en plantaardige evenementen?",
        "a": "Gastro Calendar plant Veganuary (januari), Wereld Vegan Dag, Earth Day en seizoenen van lokale groenten met speciale menu's en een redactionele kalender."
      }
    ],
    "ctaTitle": "Uw plantaardige restaurant met reële marge en auteursttechniek.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor plantaardige en veganistische restaurants: Bowls, Kostprijsberekeningen en Fermenten | AI Chef Pro",
      "description": "AI-suite voor plantaardige restaurants: VegChef, Fermentus voor plantaardige umami, kostprijsberekeningen per bowl, branding en APPCC. Begin vandaag.",
      "keywords": "AI vegan restaurant, plantaardige software, kostprijsberekening vegan bowl, vegan keuken AI, plantaardige fermenten, plantaardige umami, Veganuary",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-plant-based.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw plantaardige restaurant vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor soort plantaardig bedrijf u runt (casual healthy bowls, vegan fine dining, plantaardige hamburgerzaak, veganistisch auteurrestaurant, vegan café, vegan dark kitchen), teamgrootte, stad en specialiteit. Elke agent reageert aangepast aan uw product, markt en werkelijke operatie.",
    "appsTitle": "De AI-agenten die u gaat gebruiken in uw plantaardige restaurant",
    "apps": [
      {
        "name": "VegChef Plantaardig",
        "category": "Culinaire Creativiteit",
        "description": "Agent gespecialiseerd in professionele plantaardige, veganistische en vegetarische keuken met geavanceerde techniek."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Plantaardige koji, zelfgemaakte miso, shoyu, kimchi, kombucha en lactofermenten voor diepe umami."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van signature bowls en hedendaagse plantaardige gerechten."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Pairings met vegan wijnen, kombucha en functionele dranken."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Operationeel advies voor casual plantaardige restaurants."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus voor plantaardige texturen, plantaardige geleermiddelen en techniek."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen bij verse plantaardige producten, microgreens en zelfgemaakte eiwitten."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie: gluten, noten, soja, sesam (vrij van dierlijke producten)."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Levendige AI-referentiefotografie voor Instagram, web, menu en delivery."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met levendige redactionele kalender voor plantaardig auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Lokale klanten aantrekken die zoeken naar \"vegan in de buurt\" of \"plantaardig in de buurt\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Veganuary, Wereld Vegan Dag, Earth Day, seizoenen van groenten."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge na kostprijsberekening van bowls"
      },
      {
        "value": "×3",
        "label": "Instagram-engagement met GastroIMG"
      },
      {
        "value": "−30 %",
        "label": "verliezen bij verse producten"
      },
      {
        "value": "12+",
        "label": "agenten voor uw plantaardige keuken"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Oppervlakkige umami zonder professionele fermentatietechniek",
        "Kostprijsberekeningen zonder reële food cost, signature bowls met verlies zonder het te weten",
        "Verliezen bij verse plantaardige producten zonder traceerbaarheid",
        "Geïmproviseerde zelfgemaakte plantaardige eiwitten zonder standaardisatie",
        "Geïmproviseerde Instagram en deliveryplatforms met mobiele foto's"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Diepe umami met Fermentus: zelfgemaakte miso, koji, kimchi gedocumenteerd",
        "Professionele kostprijsberekening per bowl met gevalideerde marge",
        "Gecontroleerde verliezen met Mermas GenCal en specifieke sjablonen",
        "Plantaardige eiwitten met gedocumenteerde techniek (seitan, tempeh, tofu)",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO trekken lokale klanten aan"
      ]
    },
    "galleryTitle": "Hoe een plantaardig restaurant werkt",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: bowls, vegan burgers, fermenten, markt en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Grill, Parrilla en Steakhouse",
    "heroSubtitle": "Ontwikkel grillmenu's met vlamtechniek, kostenberekening per snede met werkelijke kosten, beheer dry-aged en plan productie met een suite van gastronomische AI-agenten gespecialiseerd in vuurkoken, grill en professioneel steakhouse.",
    "heroTagline": "Grill met echte marge en vuurtechniek",
    "badge": "Voor grillrestaurants, grills, steakhouses en churrascaria's",
    "painsTitle": "Wat een Grill Moet Oplossen",
    "pains": [
      "Volatiele vleeskosten (chuletón, picanha, ribeye, T-bone) die de kostenberekening elke week verandert",
      "Het standaardiseren van gaarheid en vlamtechniek per dienst (uitsnijden, dry-aged, marmering, kerntemperatuur)",
      "Verliezen bij uitsnijden, dry-aging (3-12% per week), trimmen en bijgerechten",
      "Beheer van dry-aged met kamer, vochtigheid, temperatuur en rotatie van sneden",
      "Differentiëren in een concurrerend gebied met premium sneden, vlamtechniek en storytelling van veeleveranciers",
      "Aantrekken van zakelijke klanten en privé-evenementen met grillmenu's met hoge marge"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt bij een Grill",
    "features": [
      {
        "icon": "Flame",
        "title": "Creatieve Keuken",
        "description": "Agent voor het ontwikkelen van grillmenu's met vlamtechniek, marinades, sauzen en professionele bijgerechten."
      },
      {
        "icon": "UtensilsCrossed",
        "title": "Argentijnse + Braziliaanse Keuken",
        "description": "Gespecialiseerde recepten: Argentijnse asado met grof zout, Braziliaanse picanha, churrasco, authentieke chimichurri, farofa, vinaigrettes."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Pairings met premium rode wijnen, whisky en karaktervolle cocktails voor uw grill."
      },
      {
        "icon": "Calculator",
        "title": "Kostenberekening per snede",
        "description": "Creatieve Keuken levert recept + kostenberekening CSV; Kit de Escandallos Pro beheert dit met werkelijke kosten per chuletón, picanha en T-bone."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Sjablonen: aansteken van vlammen, uitsnijden, dry-aged controle, mise van bijgerechten, sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC grill",
        "description": "Traceerbaarheid van vlees, dry-aging, kritische temperaturen in de kamer en kerntemperatuur bij het koken."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planning met belangrijke data: Vaderdag (chuletón), Kerst, zakelijke evenementen, lancering van speciale sneden per seizoen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Premium AI-referentiefotografie + Instagram: de grill leeft van de visuele impact van vlammen en de snede."
      },
      {
        "icon": "BarChart3",
        "title": "Mermas GenCal",
        "description": "Nauwkeurige gegevens over verliezen bij uitsnijden, dry-aging en trimmen, geïntegreerd in de kostenberekening."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Grill met AI Chef Pro",
    "workflow": [
      "09:00 · Opening — checklist Kit de Tareas: gecontroleerd aansteken van de vlammen (3 uur om op punt te komen), controle van de dry-aged kamer, uitsnijden van sneden voor de service.",
      "11:00 · Creatieve Keuken + Argentijnse Keuken — u ontwikkelt een nieuw signature snede van Galicische chuletón dry-aged 60 dagen met gerookt Maldon-zout en chimichurri van verse kruiden. Recept + kostenberekening CSV.",
      "12:00 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke vlees- en dry-aged prijzen, berekent het verlies door aging, valideert de marge per snede.",
      "13:00 · Middagservice — grill op volle toeren met premium sneden, mise van chimichurri, sauzen en bijgerechten.",
      "17:00 · Pauze tussen services — Bar & Lounge AI+ valideert pairing met rode wijnen voor de nieuwe sneden; Gastro Calendar plant het speciale Vaderdagmenu.",
      "20:00 · Diner service — gecoördineerde pieken, grill met meerdere sneden tegelijk.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de referentieafbeelding van de nieuwe chuletón en de posts voor Instagram.",
      "00:00 · Sluiting — grondige reiniging van grills, HACCP ondertekend, controle van de dry-aged kamer."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Grill",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "We hebben de kosten per snede berekend en ontdekten dat de T-bone die we het meest verkochten eigenlijk verliesgevend was vanwege het dry-aged verlies dat we niet berekenden. We hebben het opnieuw ontworpen met Creatieve Keuken door portie en bijgerechten aan te passen, zonder de prijs te wijzigen, en de marge steeg met 5 punten. De planning voor Vaderdag met Gastro Calendar verdrievoudigde onze omzet van die week.",
    "testimonialAuthor": "Pedro Aguirre",
    "testimonialRole": "Meester-grillmeester en eigenaar, premium grill",
    "faqTitle": "Veelgestelde Vragen van Grillrestaurants",
    "faqs": [
      {
        "q": "Is het geschikt voor casual grill, Argentijnse parrilla, Braziliaanse churrascaria of premium steakhouse?",
        "a": "Voor alle vier. Creatieve Keuken + Argentijnse Keuken + Braziliaanse Keuken dekken van casual grill tot premium steakhouse met dry-aged sneden, inclusief traditionele Argentijnse parrilla en Braziliaanse churrascaria met spiesen."
      },
      {
        "q": "Deckt het dry-aged techniek en kamerbeheer?",
        "a": "Ja. Creatieve Keuken redeneert als een professionele grillmeester: dry-aged kamercondities (1-3 °C, 75-85% luchtvochtigheid), tijden per snede, wekelijkse verliescontrole, identificatie van pellicle en rotatie."
      },
      {
        "q": "Hoe beheer ik de volatiele vleeskosten?",
        "a": "Kit de Escandallos Pro herberekent direct de marge wanneer u de vleesprijs bijwerkt. Mermas GenCal voegt de kosten van verliezen door dry-aging, uitsnijden en trimmen toe. De snede weerspiegelt altijd de actuele kosten."
      },
      {
        "q": "Genereert het visuele content voor Instagram en zakelijke evenementen?",
        "a": "Ja. GastroIMG Gen+ genereert professionele referentieafbeeldingen van sneden en vlammen voor Instagram, web en menu; de grill leeft van visuele impact. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte snede."
      },
      {
        "q": "Hoe helpt het mij met evenementen en feestdagen?",
        "a": "Gastro Calendar plant Vaderdag, Kerst, zakelijke evenementen en lanceringen van speciale sneden met grillmenu's en een redactionele kalender."
      }
    ],
    "ctaTitle": "Uw grill met echte marge en vuurtechniek.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits om alle agenten te gebruiken.",
    "seo": {
      "title": "AI voor Grill, Parrilla en Steakhouse: Sneden, Kostenberekening en Dry-Aged | AI Chef Pro",
      "description": "AI-suite voor grillrestaurants en steakhouses: Argentijnse + Braziliaanse Keuken, kostenberekening per snede, dry-aged, branding en HACCP. Begin vandaag.",
      "keywords": "AI grill, steakhouse software, kostenberekening chuletón, Argentijnse parrilla AI, dry-aged, churrascaria, premium grill",
      "ogImage": "https://aichef.pro/og/use-cases/asador-parrilla-steakhouse.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor Uw Grill vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een conversationele onboarding van 2 minuten waarin u vertelt wat voor soort grill u exploiteert (Argentijnse parrilla, Braziliaanse churrascaria, premium steakhouse met dry-aged, casual buurtgrill, grill met chef's cuisine), teamgrootte, stad en specialiteit. Elke agent reageert aangepast aan uw product, markt en werkelijke operatie.",
    "appsTitle": "De AI-agenten die u in uw grill zult gebruiken",
    "apps": [
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van grillmenu's met vlamtechniek, marinades en professionele bijgerechten."
      },
      {
        "name": "Argentijnse Keuken",
        "category": "Recepten uit Latam",
        "description": "Argentijnse asado, chimichurri, provolone, mollejas en authentieke grilltechniek."
      },
      {
        "name": "Braziliaanse Keuken",
        "category": "Recepten uit Latam",
        "description": "Picanha, churrasco, farofa, vinagrete en Braziliaanse churrascaria-techniek."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Pairings met krachtige rode wijnen, whisky en karaktervolle cocktails voor grill."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor de bar van de grill met premium rode wijnen en karaktervolle cocktails."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus voor texturen, gekruide zouten en technieken toegepast op sauzen en marinades."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen bij uitsnijden, dry-aging, trimmen en koken."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per snede en bijgerecht."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Premium AI-referentiefotografie voor Instagram, web, menu en bezorging."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met professionele redactionele kalender voor premium grill."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Lokale klanten aantrekken die zoeken naar \"grill in de buurt\" of \"Argentijnse parrilla\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Vaderdag, Kerst, zakelijke evenementen, seizoenslanceringen."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na het berekenen van sneden"
      },
      {
        "value": "×3",
        "label": "omzet op Vaderdag"
      },
      {
        "value": "−15 %",
        "label": "verliezen bij uitsnijden en dry-aging"
      },
      {
        "value": "12+",
        "label": "agenten voor uw grill"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde gaarheid, wisselende consistentie tussen grillmeester en dienst",
        "Kostenberekening zonder dry-aged verlies, premium sneden in verlies zonder het te weten",
        "Dry-aged kamer zonder echte traceerbaarheid of gedocumenteerde controle",
        "Verliezen bij uitsnijden en trimmen zonder traceerbaarheid",
        "Geïmproviseerde Instagram, zonder storytelling van veeleverancier"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Consistente gaarheid met gedocumenteerd technisch criterium",
        "Professionele kostenberekening per snede met geïntegreerd dry-aged verlies",
        "Dry-aged kamer met HACCP-traceerbaarheid en gedocumenteerde rotatie",
        "Verliezen gecontroleerd met Mermas GenCal en specifieke sjablonen",
        "GastroIMG Gen+ + InstaFlow + storytelling van veeleverancier"
      ]
    },
    "galleryTitle": "Hoe een Grill Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro zult coördineren: grill, vlammen, dry-aged, sneden en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Coffee Shop en Specialty Coffee",
    "heroSubtitle": "Ontwerp een menu met specialty koffie met third-wave inzicht, bereken de kostprijs per drankje met werkelijke kosten, plan de productie van eigen banket en creëer minimalistische branding met een suite van AI-agenten voor de gastronomie, gespecialiseerd in professionele specialty coffee.",
    "heroTagline": "Specialty koffie met reële marge en third-wave werkwijze",
    "badge": "Voor coffee shops, specialty cafés en third-wave coffee",
    "painsTitle": "Wat een Coffee Shop Moet Oplossen",
    "pains": [
      "Een specialty koffiemenu samenstellen met kennis: single origins, blends, zetmethoden (espresso, V60, Aeropress, Chemex)",
      "Elk drankje doorrekenen met werkelijke kosten (grammage, premium melk, plantaardige alternatieven) en een coherente foodcost",
      "Verliezen bij gemalen koffie (snelle achteruitgang), melk en verse banketproducten",
      "Baristatechniek per dienst standaardiseren: extractie, latte art, dosering, kalibratie",
      "Zich onderscheiden in een concurrerend gebied met traceerbare single-origin koffie, minimalistische visuele branding en doorlopende training",
      "Terugkerende lokale klanten aantrekken en bonen voor thuis verkopen met hoge marge"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt in een Coffee Shop",
    "features": [
      {
        "icon": "Coffee",
        "title": "Creatieve Keuken",
        "description": "Voor de ontwikkeling van signatures: infused cold brews, lattes met zelfgemaakte siroop, seizoensspecialiteiten."
      },
      {
        "icon": "Cake",
        "title": "Creatieve Patisserie",
        "description": "Voor eigen banket dat het coffee shop onderscheidt: croissants, brownies, cookies, bananenbrood, taart van de dag."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening per drankje",
        "description": "Creatieve Keuken levert recept + kostprijsberekening CSV; Kit de Escandallos Pro beheert dit met werkelijke kosten per koffie en melk, gevalideerde foodcost %."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Cafetería / Brunch",
        "description": "Sjablonen: barvoorbereiding, espressokalibratie, voorbereiding plantaardige alternatieven, mise-en-place banket, sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC cafetaria",
        "description": "Traceerbaarheid van gemalen koffie, melk, plantaardige alternatieven en eigen banket."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Seizoenslanceringen: pumpkin spice latte (herfst), cold brew (zomer), gekruide kerstkoffie."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Minimalistische AI-referentiefotografie + Instagram: specialty coffee leeft van de visuele impact van latte art."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Lokale klanten aantrekken die op Google en Maps zoeken naar \"specialty coffee in de buurt\"."
      },
      {
        "icon": "BookOpen",
        "title": "BlogPost SEO Gen+",
        "description": "SEO-artikelen over de oorsprong van koffie, zetmethoden en pairing met banket om organisch verkeer aan te trekken."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Coffee Shop met AI Chef Pro",
    "workflow": [
      "07:00 · Opening — checklist Kit de Tareas: espressokalibratie, voorbereiding van melk en plantaardige alternatieven, mise-en-place van het banket van de dag.",
      "08:00 · Ochtenddienst — ochtendpiek met koffies van consistente kwaliteit, professionele latte art.",
      "11:00 · Creatieve Keuken — u ontwikkelt een nieuwe herfstsignature: pompoenlatte met zelfgemaakte siroop. Recept + kostprijsberekening CSV.",
      "12:00 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke prijzen voor koffie, melk en siropen, valideert marge en foodcost %.",
      "14:00 · Creatieve Patisserie — u ontwikkelt een nieuw vegan bananenbrood om het menu aan te vullen.",
      "17:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert de referentieafbeelding van de nieuwe signature en de minimalistische posts voor Instagram.",
      "19:00 · Sluiting — grondige reiniging van de machine, kalibratie voor morgen, voorraadcontrole van koffie en melk.",
      "20:00 · BlogPost SEO Gen+ — u plant een artikel over zetmethoden om organisch verkeer aan te trekken."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Coffee Shop",
    "productIds": [
      "kit-tareas-cafeteria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Creatieve Keuken + Creatieve Patisserie hebben ons aanbod veranderd. We lanceren seizoensgebonden signatures met professionele kostprijsberekening, het eigen banket verhoogde de gemiddelde besteding met 30% en de barista-opleiding is nu consistent. Lokale acquisitie met MenuDish + GastroIMG Gen+ is in 4 maanden verdubbeld.",
    "testimonialAuthor": "Marta Esteve",
    "testimonialRole": "Eigenaresse, specialty coffee third-wave",
    "faqTitle": "Veelgestelde Vragen van Coffee Shops",
    "faqs": [
      {
        "q": "Is het geschikt voor een casual coffee shop, specialty coffee third-wave of roastery met winkel?",
        "a": "Voor alle drie. Creatieve Keuken dekt alles af, van eenvoudige signatures tot een specialty-menu met geavanceerde zetmethoden."
      },
      {
        "q": "Hoe bereken ik de kostprijs van drankjes met melk en plantaardige alternatieven?",
        "a": "Creatieve Keuken redeneert als een professionele barista: exacte grammage koffie, melkverhouding, kosten van premium haver vs. soja. Kit de Escandallos Pro herberekent direct."
      },
      {
        "q": "Ondersteunt het ook eigen banket om u te onderscheiden?",
        "a": "Ja. Creatieve Patisserie levert croissants, brownies, bananenbrood, cookies en seizoensspecialiteiten met professionele kostprijsberekening."
      },
      {
        "q": "Genereert het minimalistische visuele content voor Instagram?",
        "a": "Ja. GastroIMG Gen+ genereert referentieafbeeldingen met een cream en warm wood palet. Onthoudt u dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte latte."
      },
      {
        "q": "Hoe helpt het mij met seizoenslanceringen?",
        "a": "Gastro Calendar plant pumpkin spice latte (herfst), cold brew (zomer), gekruide kerstkoffie en signatures per seizoen."
      }
    ],
    "ctaTitle": "Uw coffee shop met reële marge en third-wave werkwijze.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor € 10 per maand met 10.000 credits.",
    "seo": {
      "title": "AI voor Coffee Shop en Specialty Coffee: Menu's, Kostprijsberekeningen en Branding | AI Chef Pro",
      "description": "AI-suite voor coffee shops: Creatieve Keuken, eigen banket, kostprijsberekening per drankje, minimalistische branding en lokale acquisitie. Begin vandaag.",
      "keywords": "AI coffee shop, specialty coffee software, koffie kostprijsberekening, third-wave coffee AI, latte art, specialty koffie",
      "ogImage": "https://aichef.pro/og/use-cases/coffee-shop-specialty.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor Uw Coffee Shop vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een onboarding van 2 minuten waarin u vertelt wat voor soort coffee shop u runt (specialty third-wave, casual coffee shop, roastery met winkel, café met eigen banket), teamgrootte, stad en specialiteit.",
    "appsTitle": "De AI-agenten die U in Uw Coffee Shop Gaat Gebruiken",
    "apps": [
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Ontwikkeling van signatures: cold brews, gekruide lattes, seizoensspecialiteiten."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Eigen banket: croissants, brownies, bananenbrood, cookies."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Zakelijke Concepten",
        "description": "Operationeel advies voor cafés en brunches."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus voor siropen, texturen en speciale toepassingen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen bij gemalen koffie en melk."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie voor plantaardige alternatieven en banket."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Minimalistische AI-referentiefotografie voor Instagram, web en menu."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Sociale Media",
        "description": "Instagram met minimalistische redactionele kalender."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Sociale Media",
        "description": "Lokale klanten aantrekken die zoeken naar \"specialty coffee in de buurt\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Sociale Media",
        "description": "Seizoenslanceringen en signatures per seizoen."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Sociale Media",
        "description": "SEO-artikelen over de oorsprong van koffie en zetmethoden."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Sociale Media",
        "description": "Pinterest trekt verkeer aan voor latte art en eigen banket."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na het doorrekenen van drankjes"
      },
      {
        "value": "+30 %",
        "label": "gemiddelde besteding met eigen banket"
      },
      {
        "value": "×2",
        "label": "lokale acquisitie met MenuDish"
      },
      {
        "value": "12+",
        "label": "agenten voor uw coffee shop"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde seizoensmenu's, signatures zonder kostprijsberekening",
        "Extern banket met onzekere marge",
        "Wisselende kalibratie tussen barista's",
        "Geïmproviseerde Instagram zonder minimalistisch palet",
        "Lokale acquisitie zonder Maps-SEO"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Seizoensgebonden signatures met professionele kostprijsberekening",
        "Eigen banket met Creatieve Patisserie en hoge marge",
        "Consistente kalibratie met Kit de Tareas-sjablonen",
        "Minimalistische GastroIMG Gen+ + InstaFlow",
        "MenuDish Local SEO legt \"specialty coffee in de buurt\" vast"
      ]
    },
    "galleryTitle": "Hoe een Coffee Shop Werkt",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: latte art, single-origin koffie, banket, bar en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Sushi Bar",
    "heroSubtitle": "Beheers itamae-techniek met rigoureuze kostenberekening per nigiri, beheer dagelijkse verse vis, ontwerp signature omakase en creëer minimalistische branding met een suite van culinaire AI-agenten gespecialiseerd in professionele sushi bars.",
    "heroTagline": "Sushi bar met authentieke techniek en echte marge",
    "badge": "Voor sushi bars, omakase en sushi shops",
    "painsTitle": "Wat een Sushi Bar Moet Oplossen",
    "pains": [
      "Dagelijkse verse vis voor nigiri en sashimi met volatiele kosten en strikte verliezen door het fileerproces",
      "Shari (sushirijst) standaardiseren in elke dienst met technische balans van azijn, suiker en zout",
      "Itamae-techniek coördineren met consistentie: snijden, druk, temperatuur van de rijst, neta op optimale temperatuur",
      "Zich onderscheiden in een concurrerend gebied met signature omakase, vis van de dag en storytelling over leveranciers",
      "Premium klanten aantrekken met ervaring aan de itamae-barra (niet aan tafel)",
      "Delivery-bestellingen aantrekken zonder kwaliteit van de sushi te verliezen (optimaal venster 1-2 uur)"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt in een Sushi Bar",
    "features": [
      {
        "icon": "Fish",
        "title": "Japanse Keuken",
        "description": "Agent gespecialiseerd in professionele sushi: itamae-techniek, shari-balans, fileren, neta op optimale temperatuur."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor signature nigiri en hedendaagse omakase met authentieke basis."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Voor fermentatie en geavanceerde technieken van de Japanse keuken."
      },
      {
        "icon": "Calculator",
        "title": "Kostenberekening per nigiri en omakase",
        "description": "Japanse Keuken levert recept + kostenberekening CSV; Kit de Escandallos Pro beheert dit met echte kosten per stuk en omakase."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Sjablonen: fileren, shari-prep, mise itamae, sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC sushi",
        "description": "Traceerbaarheid van vis voor sushi en kritische temperaturen."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Voor sake, Japanse whisky en professionele pairings."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Hanami, Japans Nieuwjaar, Sushi-dag, premium evenementen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Minimalistische AI-referentiefotografie + Instagram voor premium sushi bar."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Sushi Bar met AI Chef Pro",
    "workflow": [
      "08:00 · Opening — checklist Kit de Tareas: ontvangst van dagelijkse verse vis, fileerblokken, shari-prep (azijn + suiker + zout gebalanceerd).",
      "10:00 · Japanse Keuken — u ontwikkelt een nieuwe signature nigiri van hamachi met yuzu kosho en verse wasabi. Recept + kostenberekening CSV.",
      "11:00 · Kit de Escandallos Pro — u laadt de CSV met uw actuele visprijzen van de dag, valideert marge per nigiri en per omakase.",
      "13:00 · Middagdienst — sushi bar op volle toeren met itamae die voor de klant werkt.",
      "17:00 · Briefing aan het team — uitleg over de nieuwe nigiri en sake-pairings.",
      "20:00 · Avonddienst — signature omakase, gecoördineerde pieken.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert een minimalistische referentieafbeelding van de nieuwe nigiri.",
      "23:00 · Sluiting — grondige reiniging, HACCP ondertekend."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Sushi Bar",
    "productIds": [
      "guia-restaurante-japones",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Japanse Keuken veranderde onze operatie. De balans van de shari is nu consistent, de omakase heeft professionele kostenberekening met per stuk gevalideerde marge. De acquisitie van premium klanten met GastroIMG Gen+ steeg 40% in 6 maanden.",
    "testimonialAuthor": "Akio Yamamoto",
    "testimonialRole": "Itamae en eigenaar, hedendaagse sushi bar",
    "faqTitle": "Veelgestelde Vragen van Sushi Bars",
    "faqs": [
      {
        "q": "Is het geschikt voor casual sushi bar of premium omakase?",
        "a": "Voor beide. Japanse Keuken dekt van traditionele sushi tot signature omakase."
      },
      {
        "q": "Deckt het itamae-techniek?",
        "a": "Ja. Japanse Keuken redeneert als professionele itamae: fileertechniek, shari-balans, neta en combinaties."
      },
      {
        "q": "Hoe beheer ik de kosten van verse vis?",
        "a": "Kit de Escandallos Pro herberekent direct de marge wanneer u de dagprijzen bijwerkt."
      },
      {
        "q": "Genereert het minimalistische visuele content?",
        "a": "Ja. GastroIMG Gen+ genereert referentieafbeeldingen. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte stuk."
      },
      {
        "q": "Hoe helpt het mij met omakase en premium evenementen?",
        "a": "Gastro Calendar plant seizoensgebonden omakase, Hanami, Japans Nieuwjaar met premium proeverijen."
      }
    ],
    "ctaTitle": "Uw sushi bar met authentieke techniek en echte marge.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor 10 € per maand met 10.000 credits.",
    "seo": {
      "title": "AI voor Sushi Bar: Itamae, Omakase en Kostenberekening | AI Chef Pro",
      "description": "AI-suite voor sushi bars: Japanse Keuken, Fermentus, kostenberekening per nigiri, omakase en minimalistische branding. Begin vandaag.",
      "keywords": "AI sushi bar, sushi software, sushi kostenberekening, professionele itamae, omakase AI, Japanse techniek",
      "ogImage": "https://aichef.pro/og/use-cases/sushi-bar.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor Uw Sushi Bar vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een onboarding van 2 minuten waarin u vertelt wat voor soort sushi bar u runt (casual sushi bar, premium omakase, kaiten, sushi bar met warme keuken), teamgrootte, stad en specialiteit.",
    "appsTitle": "De AI-Agenten die U Gaat Gebruiken in Uw Sushi Bar",
    "apps": [
      {
        "name": "Japanse Keuken",
        "category": "Aziatische Recepten",
        "description": "Professionele sushi: itamae-techniek, sashimi, omakase."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Signature nigiri en omakase met recept + kostenberekening CSV."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Fermentatie voor geavanceerde technieken."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Pairings met sake, Japanse whisky en bier."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Sake- en Japanse whiskybar."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen bij het fileren van vis."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Identificatie van vis, schaaldieren, soja, gluten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Minimalistische AI-referentiefotografie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Minimalistische Instagram voor premium sushi bar."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Klanten aantrekken die zoeken naar \"sushi in de buurt\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Hanami, Japans Nieuwjaar, seizoensgebonden omakase."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus voor geavanceerde texturen."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge na kostenberekening van omakase"
      },
      {
        "value": "+40 %",
        "label": "premium acquisitie in 6 maanden"
      },
      {
        "value": "−20 %",
        "label": "verliezen bij fileren"
      },
      {
        "value": "12+",
        "label": "agenten voor uw sushi bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde shari, inconsistente balans",
        "Kostenberekeningen zonder prijs van de vis van de dag",
        "Geïmproviseerde omakase zonder kostenberekening",
        "Instagram zonder minimalistisch palet",
        "Lokale acquisitie zonder SEO"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Shari en techniek met professioneel criterium",
        "Realtime kostenberekening met dagprijs",
        "Omakase met per stuk gevalideerde kostenberekening",
        "Minimalistische GastroIMG Gen+ + InstaFlow",
        "MenuDish Local SEO vangt \"sushi in de buurt\""
      ]
    },
    "galleryTitle": "Hoe een Sushi Bar Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: counter, omakase, vis, sake en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor gastrobar en tapasbar",
    "heroSubtitle": "Ontwerp een tapas- en pintxoskaart met professionele kostprijsberekening, beheer vermout en wijnen per glas, plan evenementen en leg authentieke Spaanse branding vast met een suite van gastronomische AI-agenten gespecialiseerd in gastrobar en Spaanse keuken.",
    "heroTagline": "Tapas met authentieke techniek en echte marge",
    "badge": "Voor gastrobars, tapasbars, pintxos en wijnbars",
    "painsTitle": "Wat een gastrobar niet kan nalaten op te lossen",
    "pains": [
      "Tapaskaart met veel varianten (koud, warm, pintxos, porties) met een coherente foodcost",
      "Verlies bij verse producten (ansjovis, ham, zeevruchten), brood en vleeswaren met korte houdbaarheid",
      "Signature tapas per dienst standaardiseren met consistentie en serveersnelheid",
      "Beheer van vermout, wijnen per glas en bieren met hoge marge en juiste rotatie",
      "Zich onderscheiden met kwaliteitsproducten, authentieke Spaanse branding en storytelling over ambachtelijke leveranciers",
      "Privé-evenementen en proeverijen aantrekken met professionele pairing"
    ],
    "featuresTitle": "Hoe AI Chef Pro helpt in een gastrobar",
    "features": [
      {
        "icon": "Wine",
        "title": "Casual Restaurants AI+",
        "description": "Operationeel advies voor gastrobars en tapasbars."
      },
      {
        "icon": "Sparkles",
        "title": "Spaanse Keuken + Creatieve Keuken",
        "description": "Gespecialiseerde recepten: traditionele tapas, Baskische pintxos, marktporties, fusion."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijs per tapa en portie",
        "description": "Creatieve Keuken levert recept + kostprijs CSV; Kit de Escandallos Pro beheert dit met werkelijke kost per tapa en foodcost %."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Vermout, Spaanse wijnen per glas, ambachtelijke bieren en pairing met tapas."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Sjablonen: tapasvoorbereiding, bar-mise-en-place, vermout, sluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC bar",
        "description": "Traceerbaarheid van ham, vleeswaren, ansjovis, verse zeevruchten."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Wereld Tapasdag, San Fermín, lokale feesten, privé-evenementen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Spaanse ambachtelijke AI-fotografie + Instagram om locals en toeristen aan te trekken."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Klanten aantrekken die zoeken naar \"tapas in de buurt\" of \"gastrobar [stad]\"."
      }
    ],
    "workflowTitle": "Een echte dag in een gastrobar met AI Chef Pro",
    "workflow": [
      "11:00 · Opening — checklist Kit de Tareas: voorbereiding koude tapas, opzetten van de hamhouder, mise-en-place van de bar, controle van de vermout tap.",
      "12:30 · Spaanse Keuken + Creatieve Keuken — u ontwikkelt een nieuwe signature tapa van zelfgecurde ansjovis met piparra en tomatenolie. Recept + kostprijs CSV.",
      "13:30 · Kit de Escandallos Pro — u laadt de CSV met uw werkelijke prijzen, valideert de marge per tapa en foodcost %.",
      "14:00 · Middagdienst — drukke piek met vermout en tapas, perfecte mise-en-place.",
      "17:00 · Pauze — Bar & Lounge AI+ valideert pairing met Albariño- en Verdejo-wijnen voor nieuwe tapas.",
      "19:00 · Avonddienst — pieken met ambachtelijke bieren en wijnen per glas.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert referentieafbeeldingen en posts.",
      "00:00 · Sluiting — schoonmaak, APPCC ondertekend, voorraadcontrole."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor gastrobar",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Spaanse Keuken + Bar & Lounge AI+ hebben ons niveau verhoogd. De signature tapas hebben nu professionele kostprijsberekening met gevalideerde marge, de pairing met wijnen per glas is consistent en we hebben het gemiddelde ticket met 15% verhoogd in 4 maanden. De lokale acquisitie met MenuDish + GastroIMG is x2.",
    "testimonialAuthor": "Iñaki Etxeberria",
    "testimonialRole": "Eigenaar, eigentijdse gastrobar in Donostia",
    "faqTitle": "Veelgestelde vragen over gastrobars",
    "faqs": [
      {
        "q": "Is het geschikt voor een casual gastrobar, traditionele tapasbar, Baskische pintxos of wijnbar met tapas?",
        "a": "Voor alle vier. Spaanse Keuken + Casual Restaurants AI+ dekken van traditionele tapas tot eigentijdse gastrobars."
      },
      {
        "q": "Deckt het vermout, wijnen en bieren met pairing?",
        "a": "Ja. Bar & Lounge AI+ dekt vermout, Spaanse wijnen per glas, ambachtelijke bieren en pairing met tapas."
      },
      {
        "q": "Hoe beheert u verlies bij ham en verse producten?",
        "a": "Mermas GenCal levert gegevens per proces (snijden van ham, ansjovis, zeevruchten). Deze worden geïntegreerd in de kostprijsberekening."
      },
      {
        "q": "Genereert het visuele content voor Instagram?",
        "a": "Ja. GastroIMG Gen+ genereert referentieafbeeldingen. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte tapa."
      },
      {
        "q": "Hoe helpt het mij met privé-evenementen en proeverijen?",
        "a": "Gastro Calendar plant proeverijen met wijnhuizen, privé-evenementen, San Fermín en lokale feesten."
      }
    ],
    "ctaTitle": "Uw gastrobar met echte marge en authentieke techniek.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits.",
    "seo": {
      "title": "AI voor gastrobar en tapasbar: tapas, kostprijsberekeningen en pairing | AI Chef Pro",
      "description": "AI-suite voor gastrobars: Spaanse Keuken, Bar & Lounge AI+, kostprijs per tapa, vermout en wijnen per glas. Begin vandaag.",
      "keywords": "AI gastrobar, software tapasbar, kostprijs tapa, pintxos AI, vermout tapas, eigentijdse gastrobar",
      "ogImage": "https://aichef.pro/og/use-cases/gastrobar-tapas.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw gastrobar vanaf de eerste minuut",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een onboarding van 2 minuten waarin u vertelt wat voor type gastrobar u runt (eigentijdse gastrobar, traditionele tapasbar, Baskische pintxos, wijnbar met tapas), teamgrootte, stad en specialiteit.",
    "appsTitle": "De AI-agenten die u gaat gebruiken in uw gastrobar",
    "apps": [
      {
        "name": "Spaanse Keuken",
        "category": "Recepten uit Europa",
        "description": "Traditionele tapas, pintxos, marktporties."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire creativiteit",
        "description": "Eigentijdse signature tapas met recept + kostprijs CSV."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Vermout, Spaanse wijnen, bieren en pairing."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Operationeel advies voor gastrobars."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire creativiteit",
        "description": "Pairing met wijnen en bieren voor tapas."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro leveranciers",
        "description": "Sosa-catalogus voor texturen en geavanceerde techniek."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpprogramma's",
        "description": "Verlies bij ham, ansjovis, zeevruchten en vleeswaren."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpprogramma's",
        "description": "Identificatie per tapa: gluten, zuivel, schaaldieren, sulfieten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro kennis",
        "description": "Spaanse ambachtelijke AI-referentiefotografie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en sociale media",
        "description": "Instagram om locals en toeristen aan te trekken."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en sociale media",
        "description": "Klanten aantrekken die zoeken naar \"tapas in de buurt\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en sociale media",
        "description": "Tapasdag, San Fermín, lokale feesten."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na het berekenen van tapas"
      },
      {
        "value": "+15 %",
        "label": "gemiddeld ticket in 4 maanden"
      },
      {
        "value": "×2",
        "label": "lokale acquisitie met MenuDish"
      },
      {
        "value": "12+",
        "label": "agenten voor uw gastrobar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde signature tapas zonder kostprijsberekening",
        "Wijnpairing zonder wetenschappelijke basis",
        "Verlies bij ham en verse producten zonder traceerbaarheid",
        "Geïmproviseerde Instagram",
        "Lokale acquisitie zonder SEO"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Signature tapas met professionele kostprijsberekening",
        "Pairing met Bar & Lounge AI+ en Food Pairing AI",
        "Verlies gecontroleerd met Mermas GenCal",
        "GastroIMG Gen+ + ambachtelijke InstaFlow",
        "MenuDish Local SEO vangt \"tapas in de buurt\""
      ]
    },
    "galleryTitle": "Hoe een gastrobar werkt",
    "gallerySubtitle": "Wat u gaat coördineren met AI Chef Pro: tapas, vermout, ham, wijnen en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor food trucks",
    "heroSubtitle": "Ontwerp een compacte menukaart met nauwkeurige kostprijsberekening, beheer prep afgestemd op de beperkte ruimte, plan evenementen en routes en creëer virale branding met een suite van gastronomische AI-agenten gespecialiseerd in professionele food trucks.",
    "heroTagline": "Food truck met echte marge en strakke operatie",
    "badge": "Voor food trucks, mobiele keukens en streetfood",
    "painsTitle": "Wat een food truck niet kan nalaten op te lossen",
    "pains": [
      "Compacte en samengestelde menukaart (max. 5-10 gerechten) met geoptimaliseerde kosten door efficiënt proces",
      "Beperkte ruimte: aangepaste prep, compacte mise, gedeelde apparatuur, minimale opslag",
      "Gecontroleerde verspilling bij verse producten met inkoop afgestemd op het evenementsvolume",
      "Techniek per shift standaardiseren met wisselend personeel en veranderende teams",
      "Differentiëren met iconische visuele branding, actieve sociale media en storytelling van hand-painted",
      "Evenementroutes plannen (festivals, beurzen, markten, privé-evenementen) met hoge marge"
    ],
    "featuresTitle": "Hoe AI Chef Pro helpt bij een food truck",
    "features": [
      {
        "icon": "Truck",
        "title": "Food Truck AI+",
        "description": "Agent gespecialiseerd in food trucks en mobiele keukens: operatie, prep, evenementen, branding en routes."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor food truck signatures: smash burgers, bao's, taco's, knapperige kip met professionele kostprijsberekening."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijsberekening per gerecht",
        "description": "Creatieve Keuken levert recept + kostprijsberekening CSV; Kit de Escandallos Pro beheert dit met reële kosten afgestemd op mobiele operatie."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Sjablonen: pre-evenement, aangepaste prep, opbouw, snelle service, sluiting, aanvulling."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC food truck",
        "description": "Traceerbaarheid aangepast aan mobiele operatie: temperaturen, water, afval."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Festivals, beurzen, markten, privé zakelijke evenementen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Virale streetfood fotografie AI + Instagram met actieve redactionele kalender."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Klanten aantrekken die zoeken naar \"food truck in de buurt\" of \"streetfood in [stad]\"."
      },
      {
        "icon": "Sparkles",
        "title": "Mermas GenCal",
        "description": "Verspilling bij verse producten met inkoop afgestemd op het evenementsvolume."
      }
    ],
    "workflowTitle": "Een echte dag van een food truck met AI Chef Pro",
    "workflow": [
      "08:00 · Opening — checklist Kit de Tareas: controle apparatuur, opzet compacte mise, prep afgestemd op het evenementsvolume.",
      "10:00 · Food Truck AI+ — u ontwikkelt een nieuwe signature smash burger met Amerikaanse kaas en gerookte bacon. Recept + kostprijsberekening CSV.",
      "11:00 · Kit de Escandallos Pro — u laadt CSV met reële prijzen en geschat evenementsvolume, valideert marge.",
      "12:00 · Aankomst op het evenement (muziekfestival) — opbouw, elektrische aansluiting, APPCC-controle.",
      "13:00 · Middagdienst — drukke piek met gecontroleerde rijen, efficiënte prep.",
      "17:00 · Pauze — aanvulling voorraad, controle verspilling en kas van de eerste dienst.",
      "20:00 · Avonddienst — grootste piek, GastroIMG Gen+ heeft al een foto van de dag gepland op Instagram.",
      "00:00 · Sluiting — schoonmaak, APPCC ondertekend, planning van het volgende evenement met Gastro Calendar."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor food trucks",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Food Truck AI+ + Creatieve Keuken hebben onze operatie veranderd. De menukaart is compacter, de kostprijsberekeningen per gerecht weerspiegelen de echte marge met inkoop afgestemd op het evenementsvolume, en de acquisitie met InstaFlow + GastroIMG heeft onze reserveringen voor privé-evenementen in 6 maanden verdrievoudigd.",
    "testimonialAuthor": "Marcos Bermúdez",
    "testimonialRole": "Eigenaar, ambachtelijke food truck",
    "faqTitle": "Veelgestelde vragen over food trucks",
    "faqs": [
      {
        "q": "Is dit geschikt voor casual food trucks, gourmet of mobiele keukens voor privé-evenementen?",
        "a": "Voor alle drie. Food Truck AI+ dekt van casual tot gourmet, inclusief mobiele keukens voor bruiloften en zakelijke evenementen."
      },
      {
        "q": "Hoe bereken ik kostprijzen met inkoop afgestemd op het evenement?",
        "a": "Kit de Escandallos Pro herberekent direct de marge op basis van het geschatte evenementsvolume."
      },
      {
        "q": "Dekt dit mobiele operatie met beperkte ruimte?",
        "a": "Ja. Food Truck AI+ redeneert als een professionele operator: compacte prep, efficiënte mise, gedeelde apparatuur."
      },
      {
        "q": "Genereert het virale content voor Instagram en TikTok?",
        "a": "Ja. GastroIMG Gen+ + InstaFlow AI Pro genereren virale content met een actieve redactionele kalender. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte gerecht."
      },
      {
        "q": "Hoe helpt het mij met evenementen en routes?",
        "a": "Gastro Calendar plant festivals, beurzen, markten en privé-evenementen met routeplanning."
      }
    ],
    "ctaTitle": "Uw food truck met echte marge en strakke operatie.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits.",
    "seo": {
      "title": "AI voor Food Trucks: Menukaart, Kostprijzen en Evenementen | AI Chef Pro",
      "description": "AI-suite voor food trucks: Food Truck AI+, kostprijsberekening per gerecht, evenementplanning, virale branding en APPCC. Begin vandaag.",
      "keywords": "AI food truck, software food truck, kostprijsberekening food truck, streetfood AI, mobiele keuken, food truck evenementen",
      "ogImage": "https://aichef.pro/og/use-cases/food-truck.jpg"
    },
    "personalizationTitle": "Vanaf minuut één gepersonaliseerd voor uw food truck",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een onboarding van 2 minuten waarin u vertelt welk type food truck u exploiteert (casual, gourmet, privé-evenementen, markt, festivals), teamgrootte, specialiteit en werkgebieden.",
    "appsTitle": "De AI-agenten die u in uw food truck gaat gebruiken",
    "apps": [
      {
        "name": "Food Truck AI+",
        "category": "Bedrijfsconcepten",
        "description": "Agent gespecialiseerd in food trucks en mobiele keukens."
      },
      {
        "name": "Burger Pro AI+",
        "category": "Bedrijfsconcepten",
        "description": "Voor food trucks met smash burgers en gourmet hamburgerzaken."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Signatures met recept + kostprijsberekening CSV."
      },
      {
        "name": "Casual Restaurants AI+",
        "category": "Bedrijfsconcepten",
        "description": "Operationeel advies voor casual dining."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verspilling met inkoop afgestemd op het evenement."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie per gerecht."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Virale streetfood fotografie AI als referentie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met actieve redactionele kalender."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Klanten aantrekken die zoeken naar \"food truck in de buurt\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Festivals, beurzen, markten, privé-evenementen."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Social Media",
        "description": "Pinterest trekt verkeer aan voor streetfood."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en Utilities",
        "description": "Coaching voor stressbeheer bij drukke evenementen."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na kostprijsberekening menukaart"
      },
      {
        "value": "×3",
        "label": "reserveringen privé-evenementen in 6 maanden"
      },
      {
        "value": "−20 %",
        "label": "verspilling met aangepaste inkoop"
      },
      {
        "value": "12+",
        "label": "agenten voor uw food truck"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Uitgebreide menukaart met onzekere foodcost",
        "Inkoop zonder afstemming op het evenementsvolume",
        "Hoge verspilling bij verse producten",
        "Geïmproviseerde Instagram, zonder virale content",
        "Privé-evenementen handmatig afgesloten"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Compacte menukaart met professionele kostprijsberekening",
        "Inkoop afgestemd op het geschatte evenementsvolume",
        "Gecontroleerde verspilling met Mermas GenCal",
        "GastroIMG Gen+ + InstaFlow virale content",
        "Privé-evenementen afgesloten met professioneel voorstel"
      ]
    },
    "galleryTitle": "Hoe een food truck werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: truck, prep, plancha, service en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "AI voor Italiaans Restaurant",
    "heroSubtitle": "Beheers authentieke Italiaanse techniek met rigoureuze kostprijsberekening per gerecht, beheer verse pasta en traditionele sauzen, ontwerp seizoensgebonden menu's en verover trattoria-branding met een suite van AI-agenten gespecialiseerd in professionele Italiaanse keuken.",
    "heroTagline": "Italiaanse keuken met authentieke techniek en echte marge",
    "badge": "Voor trattoria's, ristoranti en Italiaanse restaurants",
    "painsTitle": "Wat een Italiaans Restaurant Niet Kan Nalaten Op te Lossen",
    "pains": [
      "Dagelijkse verse pasta met precieze balans van griesmeel, ei en water, extrusietechniek en regionale vormen",
      "Traditionele sauzen (ragù, carbonara, cacio e pepe, pesto) die technische consistentie vereisen per dienst",
      "Verliezen bij verse pasta, kaas, Italiaanse vleeswaren (mortadella, prosciutto), San Marzano-tomaten",
      "Standaardiseren van regionale signature-gerechten (Rome, Toscane, Emilia, Sicilië) met authentieke techniek",
      "Differentiëren in een concurrerende omgeving met geïmporteerd Italiaans product, trattoria-branding en regionale storytelling",
      "Binnenhalen van opdrachten voor privé-evenementen, bedrijfsdiners en Italiaanse bruiloften met hoge marge"
    ],
    "featuresTitle": "Hoe AI Chef Pro Helpt in een Italiaans Restaurant",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Italiaanse Keuken",
        "description": "Agent gespecialiseerd in authentieke Italiaanse keuken: pasta, sauzen, risotto, ossobuco, regionale techniek."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Voor Italiaanse zuurdesems (focaccia, pane casareccio, pizza alla pala) en fermentatietechniek."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Voor hedendaagse signature-gerechten en degustatie met authentieke Italiaanse basis."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Italiaanse wijnen per glas en wijnspijscombinaties met regionale keuken (Chianti, Barolo, Amarone, Prosecco)."
      },
      {
        "icon": "Calculator",
        "title": "Kostprijs per gerecht",
        "description": "Italiaanse Keuken levert recept + kostprijs CSV; Kit de Escandallos Pro beheert dit met reële kosten per gerecht en foodcost %."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Sjablonen: voorbereiding verse pasta, traditionele sauzen, mise-en-place pizza, service, afsluiting."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Italiaans",
        "description": "Traceerbaarheid van verse pasta, Italiaanse kazen, vleeswaren en sauzen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Italiaanse feestdagen (Ferragosto, Carnevale, Pasqua, Natale), privé-evenementen en Italiaanse bruiloften."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "AI-redactionele trattoriafotografie + Instagram met regionale storytelling."
      }
    ],
    "workflowTitle": "Een Echte Dag in een Italiaans Restaurant met AI Chef Pro",
    "workflow": [
      "08:00 · Opening — checklist Kit de Tareas: voorbereiding van dagelijkse verse pasta (tagliatelle, ravioli, pappardelle), voorbereiding van traditionele sauzen.",
      "10:00 · Italiaanse Keuken — u ontwikkelt een nieuw signature-gerecht van tagliolini al limone met scampi van de dagvangst. Recept + kostprijs CSV.",
      "11:00 · Kit de Escandallos Pro — u laadt CSV met reële prijzen van scampi en Italiaans product, valideert marge en foodcost %.",
      "12:00 · Bar & Lounge AI+ — u valideert de wijnspijscombinatie met een Vermentino di Sardegna.",
      "13:00 · Middagdienst — piek met verse pasta, traditionele sauzen en Italiaanse wijnen per glas.",
      "17:00 · Briefing aan het team — uitleg van het nieuwe gerecht en wijnspijscombinaties.",
      "19:00 · Avonddienst — pieken gecoördineerd met de hoofdkeuken.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — u genereert redactionele trattoria-afbeeldingen en posts."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Italiaans Restaurant",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Italiaanse Keuken + Bar & Lounge AI+ hebben ons restaurant veranderd. Consistente verse pasta, traditionele sauzen met technische balans, gedocumenteerde wijnspijscombinaties met Italiaanse wijnen per glas. We verhoogden de marge met 5 punten en het aantal terugkerende klanten groeide met 30% in 6 maanden.",
    "testimonialAuthor": "Lorenzo Bianchi",
    "testimonialRole": "Chef en eigenaar, hedendaagse trattoria",
    "faqTitle": "Veelgestelde Vragen van Italiaanse Restaurants",
    "faqs": [
      {
        "q": "Is het geschikt voor een casual trattoria, hedendaags ristorante of regionale Italiaanse keuken?",
        "a": "Voor alle drie. Italiaanse Keuken dekt van traditionele trattoria tot hoogwaardige Italiaanse auteurkeuken met authentieke regionale techniek."
      },
      {
        "q": "Deckt het verse pasta en traditionele sauzen?",
        "a": "Ja. Italiaanse Keuken redeneert als een professionele Italiaanse kok: deegbalans, regionale vormen, techniek van traditionele sauzen."
      },
      {
        "q": "Deckt het Italiaanse wijnen en wijnspijscombinaties?",
        "a": "Ja. Bar & Lounge AI+ dekt Chianti, Barolo, Amarone, Prosecco en wijnspijscombinaties met regionale keuken."
      },
      {
        "q": "Genereert het visuele content voor Instagram?",
        "a": "Ja. GastroIMG Gen+ genereert redactionele trattoria-afbeeldingen. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte gerecht."
      },
      {
        "q": "Hoe helpt het mij met evenementen en Italiaanse feestdagen?",
        "a": "Gastro Calendar plant Ferragosto, Carnevale, Pasqua, Natale en privé-evenementen met Italiaanse menu's."
      }
    ],
    "ctaTitle": "Uw Italiaanse restaurant met authentieke techniek en echte marge.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits.",
    "seo": {
      "title": "AI voor Italiaans Restaurant: Pasta, Kostprijs en Wijnen | AI Chef Pro",
      "description": "AI-suite voor Italiaanse restaurants: Italiaanse Keuken, kostprijsberekening, verse pasta, Italiaanse wijnen en trattoria-branding. Begin vandaag.",
      "keywords": "AI Italiaans restaurant, trattoria software, kostprijs pasta, Italiaanse keuken AI, Italiaanse wijnen, hedendaags ristorante",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-italiano.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor Uw Italiaanse Restaurant vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een onboarding van 2 minuten waarin u vertelt welk type Italiaans u exploiteert (trattoria, hedendaags ristorante, regionale keuken, Italiaanse auteurkeuken), teamgrootte, stad en regionale specialiteit.",
    "appsTitle": "De AI-agenten die u gaat gebruiken in uw Italiaanse restaurant",
    "apps": [
      {
        "name": "Italiaanse Keuken",
        "category": "Receptenboeken van Europa",
        "description": "Pasta, sauzen, risotto, ossobuco met authentieke regionale techniek."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Hedendaagse Italiaanse signature-gerechten."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Italiaanse zuurdesems (focaccia, pane casareccio)."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Italiaanse wijnen en regionale wijnspijscombinaties."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Wijnspijscombinaties met authentieke Italiaanse techniek."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus voor texturen en geavanceerde techniek."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen bij verse pasta, kaas, vleeswaren."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Identificatie per gerecht."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "AI-redactionele trattoriafotografie als referentie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met Italiaanse redactionele kalender."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Klanten aantrekken die zoeken naar \"Italiaans in de buurt\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Italiaanse feestdagen en privé-evenementen."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge na het berekenen van gerechten"
      },
      {
        "value": "+30 %",
        "label": "terugkerende klanten in 6 maanden"
      },
      {
        "value": "−20 %",
        "label": "verliezen bij pasta en vleeswaren"
      },
      {
        "value": "12+",
        "label": "agenten voor uw trattoria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Geïmproviseerde verse pasta, variabele balans",
        "Traditionele sauzen zonder technische consistentie",
        "Wijnspijscombinaties met Italiaanse wijnen zonder professionele basis",
        "Verliezen bij geïmporteerd Italiaans product zonder traceerbaarheid",
        "Instagram zonder regionale storytelling"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Verse pasta met gedocumenteerde technische balans",
        "Consistente traditionele sauzen met professioneel criterium",
        "Gedocumenteerde wijnspijscombinaties met Bar & Lounge AI+",
        "Gecontroleerde verliezen met Mermas GenCal",
        "GastroIMG Gen+ + InstaFlow redactionele trattoria"
      ]
    },
    "galleryTitle": "Hoe een Italiaans Restaurant Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: verse pasta, gerechten, keuken, wijnen en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "Zo maakt u kostprijsberekeningen met AI",
    "heroSubtitle": "Bereken de werkelijke kostprijs per gerecht, foodcost % en adviesprijs in minuten in plaats van dagen: recept + automatische CSV-kostprijsberekening met uurkostprijs atelier, geïntegreerde verliezen en realtime gevalideerde marge met een suite van culinaire AI-agenten.",
    "heroTagline": "Professionele kostprijsberekeningen in minuten, niet in uren",
    "badge": "Taak: kostprijsberekening en costing",
    "painsTitle": "Wat het kost om handmatig kostprijzen te berekenen",
    "pains": [
      "Een week rekenen en kladblaadjes om een nieuwe kaart van 30 gerechten te calculeren",
      "Zonder geïntegreerde uurkostprijs atelier, complexe gerechten die verliesgevend zijn zonder het te weten",
      "Verliezen op het oog geschat (30% bij sommige sneden), geen echte gegevens per proces",
      "Wanneer de leveranciersprijs verandert, klopt alles niet meer en wordt het niet bijgewerkt",
      "Gebrek aan criteria om de beoogde foodcost te bepalen op basis van het type gerecht (signature, voorgerecht, dessert)",
      "Geen traceerbaarheid van de berekening: als u gecontroleerd moet worden, weet u niet waar elk cijfer vandaan komt"
    ],
    "featuresTitle": "Hoe AI Chef Pro kostprijsberekeningen oplost",
    "features": [
      {
        "icon": "Calculator",
        "title": "Creatieve Keuken + CSV-kostprijsberekening",
        "description": "Elke creatieve agent (Keuken, Patisserie, IJs, Chocolade) levert recept + CSV-kostprijsberekening met technische balans en geïntegreerde uurkostprijs atelier."
      },
      {
        "icon": "BarChart3",
        "title": "Mermas GenCal",
        "description": "Nauwkeurige verliesgegevens per proces (uitsnijden, braden, koelen, vitrine, vormen) automatisch geïntegreerd in de CSV."
      },
      {
        "icon": "Beaker",
        "title": "Sosa Ingredients Agent",
        "description": "Sosa-catalogus met referentieprijzen voor professionele technische ingrediënten."
      },
      {
        "icon": "Sparkles",
        "title": "Calcula Pax + Conversor Ing",
        "description": "Schaal recepten op naar 2, 6, 12, 100 personen zonder aan precisie in te boeten; automatische omrekening van gewichten en maten."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Escandallos Pro",
        "description": "Downloadbare Excel-sjablonen die de CSV ontvangen en direct werkelijke marge, foodcost % en adviesprijs berekenen."
      },
      {
        "icon": "BookOpen",
        "title": "Technische fiches met kostprijs",
        "description": "Elk recept levert een volledige technische fiche op met kostprijs, allergenen, techniek en storytelling voor de bediening."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "AI-gegenereerde referentieafbeelding van het gecalculeerde gerecht om te visualiseren vóór het koken (niet de definitieve foto)."
      },
      {
        "icon": "BookOpen",
        "title": "Pro Prompts eBook",
        "description": "EBook met 300+ professionele prompts om kostprijzen te berekenen, te valideren en te optimaliseren met culinaire AI."
      },
      {
        "icon": "Wine",
        "title": "Toepasbaar op elk concept",
        "description": "Restaurant, café, banketbakkerij, ijssalon, chocolaterie, pizzeria, bar, catering, hotel: de stroom is hetzelfde."
      }
    ],
    "workflowTitle": "Zo berekent u in 4 stappen kostprijzen met AI",
    "workflow": [
      "1. Creatieve Keuken (of de creatieve agent van uw concept: Patisserie, IJs, Chocolade, Italiaanse Keuken, Mexicaanse, Peruaanse, Japanse) — u ontwikkelt of uploadt het recept. De AI-agent levert recept + CSV-kostprijsberekening met technische balans, geschatte verliezen en storytelling.",
      "2. Sosa Ingredients Agent + Mermas GenCal — de AI verrijkt de CSV met referentieprijzen en werkelijke verliezen per proces van uw type keuken.",
      "3. Kit de Escandallos Pro (downloadbaar Excel-sjabloon, €12) — u uploadt de CSV met uw werkelijke leveranciersprijzen. De Excel berekent werkelijke marge, foodcost %, adviesprijs per kanaal (zaal, bezorging, evenementen) en economisch voorstel.",
      "4. Calcula Pax + Conversor Ing — als u het recept wilt opschalen voor banketten (50, 100, 300 personen) of eenheden wilt omrekenen, doen de AI-agenten dit direct terwijl de kostprijsberekening behouden blijft."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor kostprijsberekening",
    "productIds": [
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-inventario",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Wat vroeger een week rekenen was, is nu 30 minuten. Creatieve Keuken levert de CSV-kostprijsberekening, Mermas GenCal verrijkt deze met echte gegevens en het Kit de Escandallos Pro geeft me een gevalideerde marge. We hebben de kaart van 28 gerechten in één dag vernieuwd en de marge met 6 punten verhoogd door gerechten te ontdekken die verliesgevend waren zonder dat we het wisten.",
    "testimonialAuthor": "Pablo Ruiz",
    "testimonialRole": "Chef en eigenaar, casual restaurant met 4 vestigingen",
    "faqTitle": "Veelgestelde vragen over kostprijsberekening met AI",
    "faqs": [
      {
        "q": "Werkt het voor elk type keuken?",
        "a": "Ja. De stroom is hetzelfde voor creatieve keuken, banketbakkerij, ijssalon, chocolaterie, pizzeria, Mexicaanse, Peruaanse, Japanse, Italiaanse keuken, plantaardig of elk ander concept. Alleen de uitgangs-creatieve agent verschilt."
      },
      {
        "q": "Hoe wordt de uurkostprijs van het atelier beheerd?",
        "a": "De CSV bevat een veld voor bereidingstijd per proces (mengen, vormen, bakken, decoreren). Het Kit de Escandallos Pro vermenigvuldigt dit met uw werkelijke uurtarief (salaris + lasten) en neemt dit op in de werkelijke marge."
      },
      {
        "q": "Hoe verwerk ik wisselende leveranciersprijzen (cacao, vis, vlees)?",
        "a": "Kit de Escandallos Pro herberekent direct de marge wanneer u prijzen bijwerkt. Mermas GenCal voegt de verlieskosten per proces toe. Het gerecht weerspiegelt altijd de actuele kostprijs, niet die van drie maanden geleden."
      },
      {
        "q": "Deckt het opschalen voor banketten en evenementen?",
        "a": "Ja. Calcula Pax schaalt recepten op naar elk aantal gasten zonder aan precisie in te boeten; het Kit de Escandallos Pro herberekent de kostprijs per persoon en het economisch voorstel voor de zakelijke klant."
      },
      {
        "q": "Wordt er een referentieafbeelding gegenereerd van het gecalculeerde gerecht?",
        "a": "Ja. GastroIMG Gen+ genereert een visuele referentieafbeelding van het gerecht. Onthoud dat de AI-afbeelding ter referentie is: de definitieve foto van de kostprijsberekening maakt u zelf met uw echte opgemaakte gerecht."
      }
    ],
    "ctaTitle": "Uw kostprijsberekeningen in minuten met gevalideerde marge.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits.",
    "seo": {
      "title": "Kostprijsberekening met AI: werkelijke kostprijs, marge en foodcost | AI Chef Pro",
      "description": "AI-suite voor professionele kostprijsberekening: recept + CSV met uurkostprijs atelier, geïntegreerde verliezen, gevalideerde marge. Begin vandaag.",
      "keywords": "kostprijsberekening met AI, foodcost berekenen, werkelijke kostprijs gerecht, kostprijs CSV, kostprijskit, foodcost restaurant",
      "ogImage": "https://aichef.pro/og/use-cases/task-escandallos-con-ia.jpg"
    },
    "personalizationTitle": "Vanaf minuut één afgestemd op uw keuken",
    "personalizationBody": "AI Chef Pro start met de agent «Wie Ben Ik?», een onboarding van 2 minuten waarin u vertelt welk type keuken u hanteert en de stroom voor kostprijsberekening past zich aan uw concept aan: Creatieve Keuken voor een restaurant, Creatieve Patisserie voor een ambachtelijk atelier, Creatief IJs voor een ijssalon, enz.",
    "appsTitle": "De AI-agenten die u gebruikt voor kostprijsberekening",
    "apps": [
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Recepten + CSV-kostprijsberekening met technische balans en geschatte verliezen."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Zoete recepten met geïntegreerde uurkostprijs atelier."
      },
      {
        "name": "Creatief IJs",
        "category": "Culinaire Creativiteit",
        "description": "Recepten met technische balans van suikers, vaste stoffen en vetten."
      },
      {
        "name": "Creatieve Chocolaterie",
        "category": "Culinaire Creativiteit",
        "description": "Recepten met couverture, ganache en tempereertechieken."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpmiddelen",
        "description": "Nauwkeurige verliesgegevens per proces geïntegreerd in de kostprijsberekening."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en hulpmiddelen",
        "description": "Recepten opschalen voor elk aantal gasten."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools en hulpmiddelen",
        "description": "Automatische omrekening van gewichten en maten."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en hulpmiddelen",
        "description": "Automatische identificatie van allergenen per ingrediënt."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastropartners",
        "description": "Referentieprijzen en techniek met Sosa-catalogus."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastropartners",
        "description": "Prijzen en techniek met tSpoonLab-catalogus."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Referentieafbeelding van het gecalculeerde gerecht."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI-modellen + LLM",
        "description": "Diepgaand onderzoek naar leveranciers en marktprijzen."
      }
    ],
    "metrics": [
      {
        "value": "×30",
        "label": "sneller dan handmatig rekenen"
      },
      {
        "value": "+6 pp",
        "label": "marge na het calculeren van de kaart"
      },
      {
        "value": "−25 %",
        "label": "verliezen met echte gegevens"
      },
      {
        "value": "12+",
        "label": "agenten om te calculeren"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Een week per nieuwe kaart van 30 gerechten",
        "Zonder uurkostprijs atelier, complexe gerechten verliesgevend",
        "Verliezen op het oog geschat, geen echte gegevens",
        "Leveranciersprijzen gewijzigd zonder marge bij te werken",
        "Geen traceerbaarheid van de berekening"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Een nieuwe kaart van 30 gerechten in één dag gecalculeerd",
        "Uurkostprijs atelier automatisch geïntegreerd",
        "Werkelijke verliezen met Mermas GenCal en sjablonen",
        "Prijzen bijwerkbaar: marge wordt direct herberekend",
        "Traceerbare CSV + technische fiche met kostprijs voor controle"
      ]
    },
    "galleryTitle": "Hoe de stroom voor kostprijsberekening met AI werkt",
    "gallerySubtitle": "Wat u coördineert met AI Chef Pro: recept, CSV, verliezen, digitaal receptenboek en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "Hoe Ontwerpt U een Degustatiemenu met AI",
    "heroSubtitle": "Ontwerp degustatiemenu's met een coherente gangenvolgorde, gevalideerde totale kostprijsberekening, wetenschappelijke pairings en storytelling voor de bediening met een suite van gastronomische AI-agenten gespecialiseerd in de haute cuisine.",
    "heroTagline": "Professioneel degustatiemenu in uren, niet in weken",
    "badge": "Taak: Degustatiemenu",
    "painsTitle": "Wat Het Kost om een Degustatiemenu Handmatig te Ontwerpen",
    "pains": [
      "Een week iteraties voor een coherente reeks van 7-10 gangen zonder verzadiging",
      "Zonder gevalideerde totale kostprijsberekening per menu, voorstel tegen onzekere prijs",
      "Wijnarrangementen voorgesteld zonder wetenschappelijke onderbouwing",
      "Geïmproviseerde storytelling per gang, bediening zonder consistente training",
      "Wijzigingen in gangen vereisen dat de volledige kostprijsberekening handmatig opnieuw wordt gedaan",
      "Gebrek aan criterium om textuur, temperatuur, intensiteit en techniek tussen gangen in evenwicht te brengen"
    ],
    "featuresTitle": "Hoe AI Chef Pro het Degustatiemenu Oplost",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken met technische gangenvolgorde",
        "description": "Beredeneert de volledige reeks: lichte starter, groente, vis, vlees, palate cleanser, dessert. Evenwicht van textuur, temperatuur en intensiteit."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Wetenschappelijk onderbouwde pairings voor elke gang: analyse van zuurgraad, tannines, structuur, intensiteit en harmonie met de keuken."
      },
      {
        "icon": "Calculator",
        "title": "Geïntegreerde totale kostprijsberekening",
        "description": "CSV met kostprijsberekening van elke gang + totaal van het menu; Kit de Escandallos Pro valideert de kosten per pax en het prijsvoorstel."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling voor de bediening",
        "description": "Beschrijving van elke gang met techniek, product, leverancier en verhaal; het bedieningsteam presenteert het professioneel."
      },
      {
        "icon": "Sparkles",
        "title": "Bar & Lounge AI+",
        "description": "Selectie van wijnen per glas voor de pairing van het degustatiemenu met professioneel sommeliercriterium."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Sjablonen voor de mise en place van elke gang, servicevolgorde en coördinatie met de bediening."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Referentieafbeelding van elke gang om de reeks te visualiseren voordat u proeft en de visuele samenhang valideert."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Seizoensgebonden degustatiemenu's en privé-evenementen met professionele planning."
      },
      {
        "icon": "BarChart3",
        "title": "Calcula Pax",
        "description": "Opschalen van recepten voor banketten en privé-evenementen zonder verlies van precisie."
      }
    ],
    "workflowTitle": "Hoe Ontwerpt U een Degustatiemenu in 5 Stappen",
    "workflow": [
      "1. Creatieve Keuken — u bepaalt het thema (seizoen, lokaal product, gelegenheid) en de AI-agent levert een reeks van 7-10 gangen met technisch evenwicht (textuur, intensiteit, temperatuur).",
      "2. Elke gang met recept + individuele CSV-kostprijsberekening + storytelling voor de bediening met techniek, product en leverancier.",
      "3. Food Pairing AI — voor elke gang valideert het de pairing met wijn of sake op wetenschappelijke basis. Bar & Lounge AI+ stelt een concrete wijnselectie voor.",
      "4. Kit de Escandallos Pro — u laadt de individuele CSV's, de Excel berekent de totale kosten per pax, prijsvoorstel en gevalideerde marge.",
      "5. Calcula Pax — als het menu voor een privé-evenement of banket is (50, 100, 300 pax), schaalt het recepten op en herberekent het de kosten voor een commercieel voorstel."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Degustatiemenu",
    "productIds": [
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "guia-restaurante-gastronomico",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Creatieve Keuken + Food Pairing AI hebben de ontwikkeling van onze degustatiemenu's veranderd. De reeks van 9 gangen wordt nu al opgeleverd met gedocumenteerd technisch evenwicht, de wijnarrangementen per glas zijn consistent en de totale kostprijsberekening met Kit de Escandallos Pro levert ons een gevalideerde marge op. Wat voorheen een week was, is nu een dag.",
    "testimonialAuthor": "Joan Mestre",
    "testimonialRole": "Executive chef, restaurant met 1 Michelinster",
    "faqTitle": "Veelgestelde Vragen over Degustatiemenu met AI",
    "faqs": [
      {
        "q": "Is het geschikt voor Michelin, auteurre restaurants of casual met degustatiemenu?",
        "a": "Voor alle drie. Creatieve Keuken redeneert als een professionele chef: technisch evenwicht, coherente gangenvolgorde, menuverhaal afgestemd op het niveau."
      },
      {
        "q": "Hoe helpt het u met de samenhang tussen gangen?",
        "a": "Creatieve Keuken beredeneert de volledige reeks met evenwicht van textuur (knapperig, zijdeachtig, romig), temperatuur (koud, kamertemperatuur, warm), intensiteit (zacht tot krachtig) en techniek (garing, fermentatie, roken)."
      },
      {
        "q": "Deckt het wijnarrangementen per glas voor het menu?",
        "a": "Ja. Food Pairing AI valideert elke pairing op wetenschappelijke basis; Bar & Lounge AI+ stelt een concrete wijnselectie en storytelling voor de bediening voor."
      },
      {
        "q": "Genereert het een referentieafbeelding van elke gang?",
        "a": "Ja. GastroIMG Gen+ genereert een referentieafbeelding om de visuele samenhang van het menu te visualiseren. Houd er rekening mee dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echt opgemaakte gerecht."
      },
      {
        "q": "Opschaalbaar naar banketten en privé-evenementen?",
        "a": "Ja. Calcula Pax schaalt het menu op naar elk aantal gasten; Kit de Escandallos Pro herberekent de kosten per pax en het financiële voorstel aan de klant."
      }
    ],
    "ctaTitle": "Uw professionele degustatiemenu in uren, niet in weken.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor € 10 per maand met 10.000 credits.",
    "seo": {
      "title": "Hoe Ontwerpt U een Degustatiemenu met AI: Gangenvolgorde, Kostprijsberekening en Pairings | AI Chef Pro",
      "description": "AI-suite voor degustatiemenu: technische gangenvolgorde, totale kostprijsberekening, wetenschappelijke pairings en storytelling. Begin vandaag.",
      "keywords": "degustatiemenu AI, degustatiemenu ontwerpen, gangenvolgorde, menu pairings, kostprijsberekening degustatiemenu, haute cuisine AI",
      "ogImage": "https://aichef.pro/og/use-cases/task-menu-degustacion-con-ia.jpg"
    },
    "personalizationTitle": "Vanaf Minuut Eén Aangepast aan Uw Restaurant",
    "personalizationBody": "AI Chef Pro start met «Wie Ben Ik?»: u geeft het type restaurant op (Michelin-gastronomisch, fine dining, casual met degustatiemenu, auteurre restaurant), het gewenste aantal gangen, de markt en de kookstijl. Elke agent reageert afgestemd op uw niveau.",
    "appsTitle": "De AI-agenten die u gebruikt voor het Degustatiemenu",
    "apps": [
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Beredeneert technische gangenvolgorde van degustatiemenu met evenwicht."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Wetenschappelijk onderbouwde pairings voor elke gang."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Selectie van wijnen per glas met sommeliercriterium."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Voor desserts en palate cleansers van het menu."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus voor texturen en geavanceerde techniek."
      },
      {
        "name": "tSpoonLab Agent",
        "category": "Gastro Leveranciers",
        "description": "tSpoonLab-catalogus voor geavanceerde toepassingen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Verliezen per gang geïntegreerd in de totale kostprijsberekening."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en Utilities",
        "description": "Opschaling voor banketten en privé-evenementen."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Identificatie van allergenen per gang voor de bediening."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Referentieafbeelding van elke gang van het menu."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Seizoensgebonden degustatiemenu's en privé-evenementen."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en Utilities",
        "description": "Coaching voor leiderschap en management van degustatieservice."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "snelheid vs. handmatig proces"
      },
      {
        "value": "+8 pp",
        "label": "marge na kostprijsberekening van menu"
      },
      {
        "value": "×3",
        "label": "snelheid pairings met sommelier"
      },
      {
        "value": "12+",
        "label": "agenten voor uw degustatiemenu"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Een week iteraties per nieuw menu",
        "Geïmproviseerde gangenvolgorde zonder technisch evenwicht",
        "Pairings zonder wetenschappelijke basis",
        "Totale kostprijsberekening met onzeker prijsvoorstel",
        "Geïmproviseerde storytelling, bediening zonder training"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Degustatiemenu in één dag afgerond met coherente gangenvolgorde",
        "Gedocumenteerd technisch evenwicht tussen gangen",
        "Onderbouwde pairings met Food Pairing AI",
        "Gevalideerde totale kostprijsberekening en duidelijk voorstel aan de klant",
        "Professionele storytelling voor de briefing van de bediening"
      ]
    },
    "galleryTitle": "Hoe Werkt het Ontwerpen van een Degustatiemenu met AI",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: gangenvolgorde, gangen, pairing, mise en place en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "Technische Fiches Maken met AI",
    "heroSubtitle": "Documenteer elk gerecht met een professionele technische fiche: ingrediënten, grammage, stap-voor-stap techniek, allergenen, food cost, plating photo en storytelling voor de bediening. De suite van gastronomische AI-agenten genereert in minuten een volledige fiche.",
    "heroTagline": "Professionele technische fiches in minuten, niet in uren",
    "badge": "Taak: Technische fiches",
    "painsTitle": "Wat het kost om technische fiches handmatig te maken",
    "pains": [
      "Het documenteren van 30 gerechten met een professionele technische fiche kan 2 weken duren",
      "Zonder standaardisatie repliceert elke kok zijn eigen versie en verliest de consistentie",
      "Allergenen handmatig berekend per recept, juridisch en voedselveiligheidsrisico",
      "Zonder storytelling voor de bediening beschrijft het team het gerecht geïmproviseerd",
      "Wanneer een ingrediënt wordt gewijzigd, moet de fiche worden bijgewerkt en moeten de allergenen opnieuw worden berekend",
      "Gebrek aan een professioneel sjabloon met alle kritieke velden (techniek, grammage, verliezen, kostprijs)"
    ],
    "featuresTitle": "Hoe AI Chef Pro technische fiches oplost",
    "features": [
      {
        "icon": "BookOpen",
        "title": "Creatieve Keuken met volledige fiche",
        "description": "Elk recept levert een professionele technische fiche: ingrediënten, grammage, techniek, allergenen, verliezen, kostprijs, storytelling, plating."
      },
      {
        "icon": "ShieldCheck",
        "title": "Allergenen ID",
        "description": "Automatische identificatie van allergenen per recept: zuivel, gluten, noten, soja, schaaldieren, sulfieten, enz."
      },
      {
        "icon": "Calculator",
        "title": "Geïntegreerde kostprijs",
        "description": "Technische fiche bevat food cost % en kostprijs per portie automatisch berekend met uurprijs van de werkplaats."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Referentieafbeelding van het opgemaakte gerecht om in de technische fiche op te nemen als visuele gids."
      },
      {
        "icon": "Sparkles",
        "title": "Storytelling voor de bediening",
        "description": "Elke fiche bevat een professionele beschrijving zodat het bedieningsteam met techniek kan voordragen."
      },
      {
        "icon": "CheckSquare",
        "title": "Gestandaardiseerd sjabloon",
        "description": "Uniform formaat voor alle fiches: techniek, conservering, allergenen, presentatie, kostprijs."
      },
      {
        "icon": "BarChart3",
        "title": "Conversor Ing + Calcula Pax",
        "description": "Omzetter van gewichten en maten; automatisch schalen voor banketten en evenementen."
      },
      {
        "icon": "BookOpen",
        "title": "Pro Prompts eBook",
        "description": "eBook met 300+ professionele prompts voor technische fiches, allergenen en beschrijvingen voor de bediening."
      },
      {
        "icon": "Wine",
        "title": "Pairing in de fiche",
        "description": "Food Pairing AI stelt de aanbevolen pairing voor om in de technische fiche op te nemen."
      }
    ],
    "workflowTitle": "Technische Fiches in 4 Stappen Maken",
    "workflow": [
      "1. Creatieve Keuken (of uw creatieve agent) — u ontwikkelt of laadt het recept. De AI-agent levert recept + volledige technische fiche met alle professionele velden.",
      "2. Allergenen ID — identificeert automatisch de allergenen per recept en integreert ze in de fiche; wanneer u een ingrediënt wijzigt, herberekent het onmiddellijk.",
      "3. GastroIMG Gen+ — genereert een referentieafbeelding van het opgemaakte gerecht om in de fiche op te nemen als visuele gids voor de kok.",
      "4. Food Pairing AI + storytelling voor de bediening — de fiche bevat een aanbevolen pairing en een professionele beschrijving voor de briefing van het team."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor technische fiches",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-tareas",
      "guia-restaurante-gastronomico"
    ],
    "testimonialQuote": "Het documenteren van 28 gerechten met een professionele technische fiche kostte ons 2 weken. Creatieve Keuken levert nu elke volledige fiche in minuten op: ingrediënten, techniek, automatische allergenen, kostprijs en storytelling voor de bediening. Nu kan elke kok consistent repliceren en bij inspecties hebben we alles getraceerd.",
    "testimonialAuthor": "Carla Mendoza",
    "testimonialRole": "Chef-kok, casual restaurant met 3 locaties",
    "faqTitle": "Veelgestelde vragen over technische fiches met AI",
    "faqs": [
      {
        "q": "Wat bevat een professionele technische fiche?",
        "a": "Ingrediënten met exacte grammage, stap-voor-stap techniek, automatische allergenen, food cost %, kostprijs per portie, conservering, presentatie, voorgestelde pairing en beschrijving voor de bediening."
      },
      {
        "q": "Hoe beheert het allergenen automatisch?",
        "a": "Allergenen ID identificeert de allergenen per ingrediënt en integreert ze in de fiche. Wanneer u een ingrediënt wijzigt, herberekent het onmiddellijk en werkt het de informatie voor de bediening bij."
      },
      {
        "q": "Is het geschikt voor elk type keuken?",
        "a": "Ja. De workflow is hetzelfde voor creatieve keuken, patisserie, ijssalon, chocolaterie, pizzeria, elk type nationale keuken of concept."
      },
      {
        "q": "Genereert het een afbeelding van het gerecht om in de fiche op te nemen?",
        "a": "Ja. GastroIMG Gen+ genereert een referentieafbeelding. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto in de fiche maakt u zelf met uw echt opgemaakte gerecht."
      },
      {
        "q": "Hoe helpt het u met audits en certificeringen?",
        "a": "Elke technische fiche is traceerbaar: ingrediënten, grammage, allergenen, kostprijs en techniek. Klaar voor audits, ISO 22000, BRC en certificeringen voor voedselveiligheid."
      }
    ],
    "ctaTitle": "Uw professionele technische fiches in minuten.",
    "ctaSubtitle": "Start met de onboarding van 2 minuten. Lidmaatschapsplan voor 10 € per maand met 10.000 credits.",
    "seo": {
      "title": "Technische Fiches Maken met AI: Allergenen, Kostprijs en Storytelling | AI Chef Pro",
      "description": "AI-suite voor technische fiches: automatische allergenen, geïntegreerde kostprijs, plating photo en storytelling. Start vandaag.",
      "keywords": "technische fiches AI, technische fiche gerecht, automatische allergenen, kostprijs per portie, technische fiche restaurant",
      "ogImage": "https://aichef.pro/og/use-cases/task-fichas-tecnicas-con-ia.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw keuken vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met «Wie Ben Ik?»: u geeft het type keuken, specialiteit en volume op. De structuur van de technische fiche past zich aan uw concept aan: casual restaurant, fine dining, patisserie, ijssalon, enz.",
    "appsTitle": "De AI-agenten die u gebruikt voor technische fiches",
    "apps": [
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Recepten + volledige technische fiche met alle velden."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Zoete technische fiches met uurprijs van de werkplaats."
      },
      {
        "name": "Creatief IJs",
        "category": "Culinaire Creativiteit",
        "description": "Fiches met technische balans van suikers, vaste stoffen en vetten."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Automatische identificatie van allergenen per recept."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools en Utilities",
        "description": "Automatische omzetter van gewichten en maten."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en Utilities",
        "description": "Schalen van recepten voor banketten en evenementen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Gegevens over verliezen per proces geïntegreerd in de fiche."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Voorgestelde pairing om in de fiche op te nemen."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Referentieafbeelding van het opgemaakte gerecht."
      },
      {
        "name": "Gastro Lexicon",
        "category": "Gastro Kennis",
        "description": "Tutor voor technische definities om terminologie te valideren."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Content en Social Media",
        "description": "300+ prompts voor technische fiches en beschrijvingen."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro Leveranciers",
        "description": "Sosa-catalogus om techniek en ingrediënten te valideren."
      }
    ],
    "metrics": [
      {
        "value": "×20",
        "label": "snelheid vs. handmatige fiche"
      },
      {
        "value": "100 %",
        "label": "allergenen automatisch geïdentificeerd"
      },
      {
        "value": "ISO",
        "label": "fiches klaar voor audit 22000"
      },
      {
        "value": "12+",
        "label": "agenten voor uw technische fiches"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "2 weken om 28 gerechten te documenteren",
        "Allergenen handmatig berekend (juridisch risico)",
        "Geïmproviseerde storytelling in de bediening",
        "Ingrediëntwijzigingen zonder fiches bij te werken",
        "Zonder professioneel gestandaardiseerd sjabloon"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "28 gerechten in één dag gedocumenteerd met professioneel sjabloon",
        "Automatische allergenen met Allergenen ID",
        "Professionele storytelling voor de briefing van de bediening",
        "Wijzigingen werken fiche en allergenen onmiddellijk bij",
        "Uniform sjabloon klaar voor audits en certificeringen"
      ]
    },
    "galleryTitle": "Hoe technische fiches met AI werken",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: fiche, binder, plating photo, tablet en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "Wijn-spijscombinaties valideren met AI",
    "heroSubtitle": "Valideer wijn-spijscombinaties op wetenschappelijke basis: analyse van zuurgraad, tannines, structuur, intensiteit en harmonie. Suite van gastronomische AI-agenten met professionele sommeliertechniek.",
    "heroTagline": "Wetenschappelijk onderbouwde wijn-spijscombinaties in minuten voor elke menukaart",
    "badge": "Taak: Professionele wijn-spijscombinaties",
    "painsTitle": "Wat Het Kost om Wijn-spijscombinaties Handmatig te Maken",
    "pains": [
      "Wijn-spijscombinaties aanbevolen op intuïtie zonder gefundeerde wetenschappelijke basis",
      "Bedieningsteam zonder voortdurende opleiding om wijn-spijscombinaties met kennis van zaken te communiceren",
      "Wijzigingen in menu of wijnkelder zonder wijn-spijscombinaties opnieuw te valideren (verouderde aanbeveling blijft staan)",
      "Alleen wijn-spijscombinaties met wijn: opties met bier, sake, kombucha, thee en alcoholvrij ontbreken",
      "Storytelling van elke wijn-spijscombinatie geïmproviseerd, zonder technische diepgang",
      "Privé-evenementen met ad-hoc wijn-spijscombinaties zonder duidelijk professioneel voorstel"
    ],
    "featuresTitle": "Hoe AI Chef Pro Wijn-spijscombinaties Oplost",
    "features": [
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Gespecialiseerde agent in wetenschappelijk onderbouwde wijn-spijscombinaties: analyse van zuurgraad, tannines, structuur, intensiteit, harmonie en contrast."
      },
      {
        "icon": "Sparkles",
        "title": "Bar & Lounge AI+",
        "description": "Concrete wijnkelderselectie voor elke wijn-spijscombinatie met professioneel sommelierinzicht: wijnen, sake's, bieren, mousserende wijnen."
      },
      {
        "icon": "BookOpen",
        "title": "Professionele storytelling",
        "description": "Elke wijn-spijscombinatie bevat een technische beschrijving zodat het bedieningsteam dit professioneel kan communiceren."
      },
      {
        "icon": "Calculator",
        "title": "Kostenberekening van wijn-spijscombinaties",
        "description": "Werkelijke kostprijs per glas, foodcost van de wijn en prijsvoorstel voor de wijn-spijscombinatie van het proefmenu."
      },
      {
        "icon": "Sparkles",
        "title": "Alcoholvrije wijn-spijscombinaties",
        "description": "Voorstellen met kombucha, thee, koffie, zelfgemaakt tonicwater voor klanten die geen alcohol drinken."
      },
      {
        "icon": "CheckSquare",
        "title": "Pack APPCC wijnkelder",
        "description": "Traceerbaarheid van de wijnkelder en serveertemperaturen per wijnsoort."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Proeverijen en evenementen met wijn-spijscombinaties, seizoensgebonden lanceringen."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Referentiebeeld van de wijn-spijscombinatie (glas + gerecht) voor Instagram en de menukaart."
      },
      {
        "icon": "BookOpen",
        "title": "Gastro Lexicon",
        "description": "Tutor voor technische definities: oenologie, vinificatie, terroir, herkomstbenamingen."
      }
    ],
    "workflowTitle": "Zo Valideert u Wijn-spijscombinaties in 4 Stappen",
    "workflow": [
      "1. Food Pairing AI — u laadt het gerecht met techniek en ingrediënten. De AI analyseert zuurgraad, tannines, intensiteit, structuur en stelt op wetenschappelijke basis een wijnsoort voor.",
      "2. Bar & Lounge AI+ — stelt een concrete selectie uit uw wijnkelder voor: jaargangen, producenten, glas of fles. Voor alcoholvrije opties stelt het kombucha's, theeën of zelfgemaakte tonics voor.",
      "3. Storytelling voor de bediening — elke wijn-spijscombinatie genereert een professionele beschrijving voor de briefing van het team en de communicatie naar de klant.",
      "4. Kit de Escandallos Pro — u berekent de werkelijke kostprijs per glas, de foodcost van de wijn en een prijsvoorstel voor de wijn-spijscombinatie."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor wijn-spijscombinaties",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Food Pairing AI heeft de manier waarop ik wijn-spijscombinaties afrond veranderd. Elk gerecht van het proefmenu heeft nu een wetenschappelijk onderbouwde wijn-spijscombinatie die mijn bedieningsteam met professionele basis communiceert. We hebben de marge in de wijnkelder met 6 punten verhoogd en het aantal vaste premiumklanten is in 6 maanden met 35 % gestegen.",
    "testimonialAuthor": "Eduardo Lara",
    "testimonialRole": "Head Sommelier, restaurant met 1 Michelinster",
    "faqTitle": "Veelgestelde Vragen over Wijn-spijscombinaties met AI",
    "faqs": [
      {
        "q": "Werkt het voor elke restaurantstijl?",
        "a": "Ja. Food Pairing AI dekt alles af van casual tot Michelin-fine dining, inclusief gastrobars, wijnbars en etnische restaurants."
      },
      {
        "q": "Heeft het een echte wetenschappelijke basis?",
        "a": "Ja. Het redeneert als een professionele sommelier met technische kennis van oenologie en levensmiddelenwetenschap: zuurgraad, tannines, structuur, intensiteit, harmonie en contrast."
      },
      {
        "q": "Deckt het alcoholvrije wijn-spijscombinaties?",
        "a": "Ja. Het stelt kombucha's, theeën, koffie, zelfgemaakte tonics en functionele dranken voor met professionele kennis voor klanten die geen alcohol drinken."
      },
      {
        "q": "Deckt het wijn-spijscombinaties met bier, sake en mousserende wijnen?",
        "a": "Ja. Bar & Lounge AI+ bestrijkt het volledige bardomein: wijnen, sake's, speciaalbieren, mousserende wijnen en gedistilleerde dranken."
      },
      {
        "q": "Genereert het visuele content van de wijn-spijscombinatie voor Instagram?",
        "a": "Ja. GastroIMG Gen+ genereert een referentiebeeld. Onthoud dat de AI-afbeelding een visuele referentie is: de uiteindelijke foto maakt u zelf met uw eigen glas en gerecht."
      }
    ],
    "ctaTitle": "Uw wetenschappelijk onderbouwde wijn-spijscombinaties binnen enkele minuten.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor € 10 per maand met 10.000 credits.",
    "seo": {
      "title": "Wijn-spijscombinaties valideren met AI: Wijn, Sake en Alcoholvrij | AI Chef Pro",
      "description": "AI-suite voor wijn-spijscombinaties: Food Pairing AI met wetenschappelijke basis, wijnkelderselectie, storytelling voor de bediening. Begin vandaag.",
      "keywords": "wijn-spijscombinaties met AI, food pairing AI, wijn-spijscombinatie, AI-sommelier, alcoholvrije wijn-spijscombinaties AI, wetenschappelijk onderbouwde wijn-spijscombinaties",
      "ogImage": "https://aichef.pro/og/use-cases/task-maridajes-con-ia.jpg"
    },
    "personalizationTitle": "Vanaf de Eerste Minuut Afgestemd op Uw Wijnkelder",
    "personalizationBody": "AI Chef Pro start met «Wie Ben Ik?»: u geeft het type restaurant, de grootte van de wijnkelder, specialiteit en niveau op. Elke wijn-spijscombinatie wordt afgestemd op uw werkelijke voorraad, niet op een generieke wijnkelder.",
    "appsTitle": "De AI-agenten die u gebruikt voor wijn-spijscombinaties",
    "apps": [
      {
        "name": "Food Pairing AI",
        "category": "Culinaire Creativiteit",
        "description": "Wetenschappelijk onderbouwde wijn-spijscombinaties voor elk gerecht."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Concrete wijnkelderselectie met sommelierinzicht."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Professionele storytelling van de wijn-spijscombinatie voor de bediening."
      },
      {
        "name": "Gastro Lexicon",
        "category": "Gastro Kennis",
        "description": "Tutor voor definities van oenologie en vinificatie."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en Hulpprogramma's",
        "description": "Geïntegreerde verliezen door mislukte ontkurking."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Hulpprogramma's",
        "description": "Identificatie van sulfieten voor gevoelige klanten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Referentiebeeld van de wijn-spijscombinatie."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI-modellen + LLM",
        "description": "Diepgaand onderzoek naar wijnhuizen en jaargangen."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Sociale Media",
        "description": "Proeverijen en evenementen met wijn-spijscombinaties."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Sociale Media",
        "description": "SEO-artikelen over wijn-spijscombinaties en wijnkelders."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Sociale Media",
        "description": "Instagram met uitgelichte wijn-spijscombinaties."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Content en Sociale Media",
        "description": "300+ prompts voor beschrijvingen van wijn-spijscombinaties."
      }
    ],
    "metrics": [
      {
        "value": "×10",
        "label": "snelheid vs. handmatige validatie"
      },
      {
        "value": "+6 pp",
        "label": "marge na kostenberekening wijnkelder"
      },
      {
        "value": "+35 %",
        "label": "vaste premiumklanten"
      },
      {
        "value": "12+",
        "label": "agenten voor wijn-spijscombinaties"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Wijn-spijscombinaties op intuïtie zonder wetenschappelijke basis",
        "Geen professionele alcoholvrije opties",
        "Bedieningsteam zonder gedocumenteerde opleiding",
        "Wijzigingen in wijnkelder zonder wijn-spijscombinaties opnieuw te valideren",
        "Ad-hoc wijn-spijscombinaties voor privé-evenementen"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Wetenschappelijk onderbouwde wijn-spijscombinaties van Food Pairing AI",
        "Opties met kombucha, thee, zelfgemaakte tonics",
        "Dagelijkse briefing aan het team met professionele storytelling",
        "Wijzigingen in wijnkelder valideren wijn-spijscombinaties direct opnieuw",
        "Wijn-spijscombinaties voor besloten evenementen met professioneel voorstel"
      ]
    },
    "galleryTitle": "Hoe de Validatie van Wijn-spijscombinaties met AI Werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: glazen, gerechten, notities, wijnkelder en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "Hoe u verspilling in de keuken vermindert met AI",
    "heroSubtitle": "Identificeer, meet en verminder verspilling per proces (uitsnijden, vormen, bakken, vitrine, delivery) met echte gegevens geïntegreerd in de kostprijsberekening. Suite van gastronomische AI-agenten gespecialiseerd in zero-waste-operaties.",
    "heroTagline": "Minder verspilling met echte gegevens per proces",
    "badge": "Taak: Verspillingsreductie",
    "painsTitle": "Wat ongecontroleerde verspilling kost",
    "pains": [
      "Verspilling op het oog geschat (15-30% bij sommige sneden), geen echte gegevens per proces",
      "Gebrek aan gegevens per keukentype (ijssalon, bakkerij, grill, sushi hebben verschillende verspilling)",
      "Geen systeem om trimmings en schillen te hergebruiken (bouillons, geïnfuseerde azijnen, gedehydrateerde producten)",
      "Wanneer een leverancier wisselt, verandert de verspilling zonder dat de marge opnieuw wordt berekend",
      "Team zonder voortdurende training in professionele benuttingstechnieken",
      "Geen traceerbaarheid voor duurzaamheidsaudits en zero-waste-certificeringen"
    ],
    "featuresTitle": "Hoe AI Chef Pro verspilling vermindert",
    "features": [
      {
        "icon": "BarChart3",
        "title": "Mermas GenCal",
        "description": "Nauwkeurige verspillingsgegevens per proces per keukentype: uitsnijden, dry-aging, vormen, bakken, vitrine, delivery."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken",
        "description": "Beredeneert hergebruiktechnieken: trimmings tot bouillons, schillen tot geïnfuseerde azijnen, resten tot gedehydrateerde producten met professioneel inzicht."
      },
      {
        "icon": "Calculator",
        "title": "Verspilling in kostprijsberekening",
        "description": "Werkelijke verspilling per proces geïntegreerd in de kostprijsberekening van de Kit de Escandallos Pro: de kostprijs per gerecht weerspiegelt de werkelijke verspilling, niet de geschatte."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Sjablonen met benuttingsprocedures per station, wekelijkse verspillingscontrole, teamtraining."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC traceerbaar",
        "description": "Traceerbaarheid van verspilling per proces voor duurzaamheidsaudits en zero-waste-certificeringen."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Con AI+",
        "description": "Fermenten om producten te hergebruiken: zuurkool met koolresten, kombucha met fruitschillen, garum met visgraten."
      },
      {
        "icon": "Sparkles",
        "title": "VegChef Plantaardig",
        "description": "Voor professioneel plantaardig hergebruik: volledige benutting van de groente, stems-to-roots-techniek."
      },
      {
        "icon": "BarChart3",
        "title": "Calcula Pax",
        "description": "Inkopen afgestemd op het werkelijke volume van het evenement of de service om overschotten aan de bron te verminderen."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Productieplanning afgestemd op historische vraag om overproductie te verminderen."
      }
    ],
    "workflowTitle": "Hoe u verspilling in 4 stappen vermindert",
    "workflow": [
      "1. Mermas GenCal — de AI-agent levert echte gegevens per proces per keukentype (uitsnijden vlees, vormen pasta, bakken brood, vitrine ijs, delivery pizza). U laadt het werkelijke gegeven van uw operatie.",
      "2. Creatieve Keuken + Fermentus Con AI+ — u ontwikkelt hergebruiktechnieken: trimmings tot bouillons, schillen tot azijnen, resten tot gedehydrateerde producten, overschotten tot fermenten.",
      "3. Kit de Escandallos Pro — de kostprijsberekening weerspiegelt de werkelijke verspilling, niet de geschatte. De kostprijs per gerecht stijgt licht, maar weerspiegelt de werkelijke kostprijs, waardoor verrassingen in de marge worden voorkomen.",
      "4. Calcula Pax + Gastro Calendar — inkopen afgestemd op het werkelijke volume van de service of het evenement om overschotten aan de bron te verminderen, niet alleen om verspilling achteraf te verwerken."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits om verspilling te verminderen",
    "productIds": [
      "kit-escandallos",
      "kit-inventario",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-tareas",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Mermas GenCal + Creatieve Keuken hebben onze werkwijze veranderd. We gingen van geschatte verspilling (we gingen uit van 12-15%) naar echte gegevens van 22-28% in sommige processen. We reorganiseerden het uitsnijden en de benutting met gedocumenteerde techniek en verminderden de verspilling met 35% in 4 maanden. De kostprijsberekening weerspiegelt nu de werkelijke kostprijs, niet de ideale.",
    "testimonialAuthor": "Sofía Cano",
    "testimonialRole": "Sous-chef, casual restaurant met zero-waste-engagement",
    "faqTitle": "Veelgestelde vragen over het verminderen van verspilling met AI",
    "faqs": [
      {
        "q": "Werkt het voor elk type keuken?",
        "a": "Ja. Mermas GenCal dekt gegevens per proces per keukentype: grill, sushi, pasta, brood, ijs, chocolade, saus, marinade. Elke keuken heeft andere verspilling."
      },
      {
        "q": "Hoe integreer ik werkelijke verspilling in de kostprijsberekening?",
        "a": "Kit de Escandallos Pro heeft een verspillingsveld per ingrediënt en per proces. Mermas GenCal levert de werkelijke gegevens zodat de kostprijs per gerecht de realiteit weerspiegelt."
      },
      {
        "q": "Omvat het professionele hergebruiktechnieken?",
        "a": "Ja. Creatieve Keuken levert benuttingstechnieken: plantaardige stems-to-roots, trimmings tot bouillons, schillen tot azijnen, fermenten met overschotten. Fermentus gaat dieper in op geavanceerde technieken."
      },
      {
        "q": "Genereert het traceerbaarheid voor zero-waste-certificeringen?",
        "a": "Ja. Pack APPCC + Mermas GenCal leveren gedocumenteerde traceerbaarheid voor duurzaamheidsaudits en zero-waste- of B-Corp-certificeringen."
      },
      {
        "q": "Hoe helpt het mij met afgestemde inkopen?",
        "a": "Calcula Pax + Gastro Calendar plannen productie en inkopen afgestemd op het werkelijke volume van de service om overschotten aan de bron te verminderen."
      }
    ],
    "ctaTitle": "Uw keuken met minder verspilling en echte gegevens.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits.",
    "seo": {
      "title": "Hoe u verspilling in de keuken vermindert met AI: Echte gegevens en hergebruik | AI Chef Pro",
      "description": "AI-suite om verspilling te verminderen: Mermas GenCal met echte gegevens, professioneel hergebruik, traceerbare kostprijsberekening. Begin vandaag.",
      "keywords": "verspilling restaurant verminderen, verspilling met AI, food waste AI, zero waste keuken, verspilling ambachtelijke bakkerij, afval verminderen",
      "ogImage": "https://aichef.pro/og/use-cases/task-reducir-mermas-con-ia.jpg"
    },
    "personalizationTitle": "Vanaf minuut één gepersonaliseerd voor uw keuken",
    "personalizationBody": "AI Chef Pro start met «Wie Ben Ik?»: u vertelt het type keuken en volume. Mermas GenCal levert gegevens per proces, afgestemd op uw concept: grill, sushi, pasta, brood, ijs, chocolade.",
    "appsTitle": "De AI-agenten die u gebruikt om verspilling te verminderen",
    "apps": [
      {
        "name": "Mermas GenCal",
        "category": "Tools en Utilities",
        "description": "Echte verspillingsgegevens per proces per keukentype."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Professionele hergebruiktechnieken voor trimmings en overschotten."
      },
      {
        "name": "Fermentus Con AI+",
        "category": "Culinaire Creativiteit",
        "description": "Fermenten om overschotten te hergebruiken (zuurkool, kombucha, garum)."
      },
      {
        "name": "VegChef Plantaardig",
        "category": "Culinaire Creativiteit",
        "description": "Volledige benutting van de groente (stems-to-roots)."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en Utilities",
        "description": "Inkopen afgestemd op het werkelijke volume van de service."
      },
      {
        "name": "Conversor Ing",
        "category": "Tools en Utilities",
        "description": "Omzetter van gewichten en maten voor precisie."
      },
      {
        "name": "Allergenen ID",
        "category": "Tools en Utilities",
        "description": "Identificatie bij hergebruikte producten."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Productieplanning afgestemd op historische vraag."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "SEO-artikelen over duurzaamheid om verkeer aan te trekken."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Referentiebeeld van zero-waste-gerechten."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en Utilities",
        "description": "Coaching voor teamleiderschap in zero-waste."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI-modellen + LLM",
        "description": "Onderzoek naar zero-waste-technieken van referenties."
      }
    ],
    "metrics": [
      {
        "value": "−35 %",
        "label": "verspilling in 4 maanden"
      },
      {
        "value": "+4 pp",
        "label": "marge na integratie van werkelijke verspilling"
      },
      {
        "value": "×3",
        "label": "snelheid vs. handmatige schatting"
      },
      {
        "value": "12+",
        "label": "agenten om verspilling te verminderen"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Verspilling op het oog geschat, kostprijsberekening met onderschatte kosten",
        "Zonder gedocumenteerde hergebruiktechniek",
        "Generieke inkopen zonder afstemming op het werkelijke volume",
        "Team zonder training in professionele benutting",
        "Zonder traceerbaarheid voor duurzaamheidsaudits"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Werkelijke verspilling gedocumenteerd per proces",
        "Hergebruiktechnieken met Creatieve Keuken + Fermentus",
        "Inkopen afgestemd op het werkelijke volume met Calcula Pax",
        "Briefing aan het team met gedocumenteerde techniek",
        "APPCC-traceerbaarheid voor zero-waste-audits"
      ]
    },
    "galleryTitle": "Hoe AI-gestuurde verspillingsreductie werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: wegen, tracking, organisatie, hergebruik en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "Hoe u digitale APPCC met AI beheert",
    "heroSubtitle": "Vervang verspreid bedrukt papier door APPCC vanaf mobiel met professionele sjablonen: temperaturen, reiniging, traceerbaarheid, allergenen, ongedierte, olie en water. Suite van gastronomische AI-agenten met regelgevingsbasis.",
    "heroTagline": "Professionele APPCC vanaf mobiel zonder papier",
    "badge": "Taak: APPCC en voedselveiligheid",
    "painsTitle": "Wat het kost om APPCC op papier te beheren",
    "pains": [
      "Verspreid bedrukt papier in de keuken, onvolledige registraties bij inspecties",
      "Geen standaardisatie per concept (ijssalon, bakkerij, grill, sushi hebben verschillende registraties)",
      "Allergenen handmatig berekend per recept, juridisch en veiligheidsrisico",
      "Wijzigingen in regelgeving zonder sjablonen en procedures bij te werken",
      "Roulerend team zonder continue training in voedselveiligheid",
      "Zonder traceerbaarheid voor ISO 22000, BRC, IFS-audits of kwaliteitscertificeringen"
    ],
    "featuresTitle": "Hoe AI Chef Pro APPCC oplost",
    "features": [
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC met Excel-sjablonen",
        "description": "17 downloadbare Excel-sjablonen: temperaturen, reiniging, traceerbaarheid, allergenen, ongedierte, olie en water."
      },
      {
        "icon": "Sparkles",
        "title": "Allergenen ID",
        "description": "Automatische identificatie van allergenen per ingrediënt en recept. Wanneer u een ingrediënt wijzigt, herberekent het onmiddellijk."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas met APPCC",
        "description": "Taaksjablonen met geïntegreerde APPCC per dienst: opening, service, sluiting."
      },
      {
        "icon": "BarChart3",
        "title": "Traceerbaarheid van producten",
        "description": "Traceerbaarheid van verse vis, zuivel, noten, fermenten, conserven met kritische temperaturen."
      },
      {
        "icon": "BookOpen",
        "title": "Creatieve Keuken met APPCC",
        "description": "Recepten met APPCC-procedures geïntegreerd in de technische fiche: temperatuur, bewaring, allergenen."
      },
      {
        "icon": "Calendar",
        "title": "Geplande reiniging",
        "description": "Kalender voor grondige reiniging per station en dienst met specifieke sjablonen en digitale handtekening."
      },
      {
        "icon": "Sparkles",
        "title": "Pro Prompts eBook",
        "description": "300+ professionele prompts voor APPCC-beheer, teamtraining en communicatie met inspecteurs."
      },
      {
        "icon": "Wine",
        "title": "Pack APPCC voor wijnkelder",
        "description": "Traceerbaarheid van wijnen, ontkurking, bewaring en servicetemperaturen per type."
      },
      {
        "icon": "BarChart3",
        "title": "Sonar Deep Research",
        "description": "Diepgaand onderzoek naar gezondheidsregelgeving per land, autonome gemeenschap en type horecagelegenheid."
      }
    ],
    "workflowTitle": "Hoe implementeert u digitale APPCC in 4 stappen",
    "workflow": [
      "1. Pack APPCC (€14, downloadbare Excel-sjablonen) — u downloadt de 17 professionele sjablonen aangepast aan uw type keuken (patisserie, ijssalon, restaurant, enz.).",
      "2. Allergenen ID — scant automatisch de recepten en sjablonen van uw menu om allergenen per gerecht te identificeren. Het integreert ze in de technische fiches en de zaal.",
      "3. Creatieve Keuken met geïntegreerde APPCC — elk nieuw recept levert APPCC-procedures (kritische temperatuur, bewaring, allergenen, opslag) geïntegreerd in de technische fiche.",
      "4. Kit de Tareas met APPCC — dienstsjablonen (opening, service, sluiting) met geïntegreerde APPCC. Het team ondertekent elke dienst digitaal vanaf mobiel."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor APPCC",
    "productIds": [
      "pack-appcc",
      "kit-tareas",
      "pro-prompts-ebook",
      "kit-escandallos",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Pack APPCC + Allergenen ID hebben onze voedselveiligheid getransformeerd. We zijn overgestapt van verspreid bedrukt papier naar 17 digitale sjablonen met geïntegreerde APPCC per dienst en automatische allergenen per recept. De hygiëne-inspectie is vlekkeloos en het juridisch risico is naar nul gedaald.",
    "testimonialAuthor": "Roberto Castaño",
    "testimonialRole": "F&B-directeur, 5-sterrenhotel met 4 outlets",
    "faqTitle": "Veelgestelde vragen over APPCC met AI",
    "faqs": [
      {
        "q": "Is het geschikt voor elk type horecagelegenheid?",
        "a": "Ja. Pack APPCC past sjablonen aan voor restaurant, cafetaria, patisserie, ijssalon, chocolaterie, pizzeria, dark kitchen, bar, catering, hotel."
      },
      {
        "q": "Hoe beheert u allergenen automatisch?",
        "a": "Allergenen ID identificeert allergenen per ingrediënt en recept, integreert ze in technische fiches en APPCC-sjablonen. Wanneer u een ingrediënt wijzigt, herberekent het onmiddellijk."
      },
      {
        "q": "Deckt u Europese en Latijns-Amerikaanse regelgeving?",
        "a": "Ja. Pack APPCC dekt Europese regelgeving (EU 852/2004 + 178/2002 + 1169/2011 allergenen) en aanpassingen voor Latijns-Amerika. Sonar Deep Research maakt het mogelijk om specifieke regelgeving per land te raadplegen."
      },
      {
        "q": "Genereert het traceerbaarheid voor ISO-audits?",
        "a": "Ja. APPCC vanaf mobiel met digitale handtekening + traceerbaarheid van producten + reinigingskalender klaar voor ISO 22000, BRC, IFS, FSSC 22000-audits."
      },
      {
        "q": "Hoe helpt het u bij wijzigingen in regelgeving?",
        "a": "Sonar Deep Research raadpleegt actuele regelgeving per land en autonome gemeenschap. Creatieve Keuken werkt technische fiches en procedures bij wanneer de normen veranderen."
      }
    ],
    "ctaTitle": "Uw professionele APPCC vanaf mobiel zonder papier.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits.",
    "seo": {
      "title": "Hoe u digitale APPCC met AI beheert: Sjablonen, Allergenen en Traceerbaarheid | AI Chef Pro",
      "description": "AI-suite voor digitale APPCC: Excel-sjablonen, automatische allergenen, ISO-traceerbaarheid. Begin vandaag.",
      "keywords": "digitale APPCC AI, APPCC-sjablonen, automatische allergenen, ISO 22000 AI, voedselveiligheid AI, digitale HACCP",
      "ogImage": "https://aichef.pro/og/use-cases/task-appcc-digital-con-ia.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw horecagelegenheid vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met «Wie Ben Ik?»: u vertelt het type horecagelegenheid en het land. Pack APPCC past sjablonen aan uw concept en lokale regelgeving aan.",
    "appsTitle": "De AI-agenten die u gebruikt voor APPCC",
    "apps": [
      {
        "name": "Allergenen ID",
        "category": "Hulpmiddelen en Utilities",
        "description": "Automatische identificatie van allergenen per recept."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Recepten met geïntegreerde APPCC-procedures."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Specifieke APPCC voor patisserie en bakkerijen."
      },
      {
        "name": "Creatief IJs",
        "category": "Culinaire Creativiteit",
        "description": "Specifieke APPCC voor ijssalon met gevoelig product."
      },
      {
        "name": "Creatieve Chocolaterie",
        "category": "Culinaire Creativiteit",
        "description": "Specifieke APPCC voor chocolaterie en bonbonnerie."
      },
      {
        "name": "Mermas GenCal",
        "category": "Hulpmiddelen en Utilities",
        "description": "Traceerbaarheid van verliezen geïntegreerd in APPCC."
      },
      {
        "name": "Conversor Ing",
        "category": "Hulpmiddelen en Utilities",
        "description": "Omzetter van gewichten en maten."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI-modellen + LLM",
        "description": "Diepgaand onderzoek naar regelgeving per land."
      },
      {
        "name": "Gastro Lexicon",
        "category": "Gastro Kennis",
        "description": "Tutor voor technische regelgevingsdefinities."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Content en Sociale Media",
        "description": "300+ prompts voor APPCC-beheer."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Sociale Media",
        "description": "Artikelen over voedselveiligheid voor organisch verkeer."
      },
      {
        "name": "Mentale Coach",
        "category": "Hulpmiddelen en Utilities",
        "description": "Coaching voor stressbeheer bij inspecties."
      }
    ],
    "metrics": [
      {
        "value": "ISO",
        "label": "sjablonen klaar voor 22000, BRC, IFS"
      },
      {
        "value": "100 %",
        "label": "allergenen automatisch geïdentificeerd"
      },
      {
        "value": "0 %",
        "label": "juridisch risico door niet-vermelde allergenen"
      },
      {
        "value": "12+",
        "label": "agenten voor uw APPCC"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Verspreid bedrukt papier in de keuken",
        "Allergenen handmatig berekend (juridisch risico)",
        "Geen sjablonen aangepast aan het type keuken",
        "Roulerend team zonder gedocumenteerde training",
        "Zonder traceerbaarheid voor ISO-audits"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "APPCC vanaf mobiel met digitale handtekening",
        "Automatische allergenen met Allergenen ID",
        "Excel-sjablonen aangepast per concept",
        "Briefing met APPCC geïntegreerd in Kit de Tareas",
        "Traceerbaarheid klaar voor ISO 22000, BRC, IFS"
      ]
    },
    "galleryTitle": "Hoe digitale APPCC met AI werkt",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: thermometer, tablet, camera, reiniging en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "Hoe ontwerpt u een seizoensmenu met AI",
    "heroSubtitle": "Ontwerp een seizoensmenu met lokaal seizoensproduct, professionele kostenberekening, vooruit planning en storytelling van producenten. Suite van gastronomische AI-agenten met kalender per halfrond en regio.",
    "heroTagline": "Seizoensmenu met professioneel inzicht in uren",
    "badge": "Taak: Seizoensmenu",
    "painsTitle": "Wat het kost om handmatig een seizoensmenu te ontwerpen",
    "pains": [
      "Een week of meer om te itereren en een seizoensmenu af te sluiten met gevalideerde kostenberekening",
      "Zonder duidelijk criterium voor lokaal product per seizoen en regio (verschilt per halfrond)",
      "Product buiten het seizoen met hoge kosten en hoge verliezen (import, koeling)",
      "Zonder storytelling van lokale producenten voor bediening en communicatie",
      "Abrupte overgangen tussen seizoenen zonder vooruit planning",
      "Zonder coördinatie met feestdagenkalender (Pasen, Kerst, Moederdag, lokale evenementen)"
    ],
    "featuresTitle": "Hoe AI Chef Pro het seizoensmenu oplost",
    "features": [
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Seizoensplanning per halfrond en regio met lokaal product in het seizoen en belangrijke feestdagen."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken seizoensgebonden",
        "description": "Redeneert signature gerechten met lokaal product in het seizoen: herfstpaddenstoelen, lentasperges, zomergroenten, winterwortels."
      },
      {
        "icon": "Calculator",
        "title": "Seizoenskostenberekening",
        "description": "Recept + kostenberekening CSV met lokaal product; Kit de Escandallos Pro herberekent de marge bij seizoenswisseling."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling van producenten",
        "description": "Elk gerecht bevat storytelling van de lokale producent: veehouder, boer, bakker, visser, voor communicatie met bediening en klant."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Seizoenswijnen en pairing afgestemd op het seizoensproduct voor uw menu."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "AI-seizoensfotografie + Pinterest trekt organisch verkeer voor seizoensproduct."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Sjablonen voor overgang tussen seizoenen: voorraadrotatie, teamtraining, menulancering."
      },
      {
        "icon": "Sparkles",
        "title": "VegChef Plantaardig",
        "description": "Voor seizoensgroenten met geavanceerde techniek (fermentatie, gedroogd, conserven)."
      },
      {
        "icon": "BarChart3",
        "title": "Sosa Ingredients Agent",
        "description": "Sosa-catalogus om lokaal product aan te vullen met professionele techniek."
      }
    ],
    "workflowTitle": "Hoe ontwerpt u een seizoensmenu in 5 stappen",
    "workflow": [
      "1. Gastro Calendar — u definieert halfrond, regio en seizoen (bijv. herfst Noordelijk halfrond, Madrid). De AI-agent levert lokaal product in het seizoen en belangrijke feestdagen (Moederdag, Kerst, Valentijnsdag).",
      "2. Creatieve Keuken — u ontwikkelt signature gerechten met lokaal product. Elk recept levert recept + kostenberekening CSV + storytelling van de producent.",
      "3. Kit de Escandallos Pro — u uploadt de CSV's met uw echte prijzen van lokale leveranciers, valideert marge en food cost % per gerecht en totale menu.",
      "4. Bar & Lounge AI+ + Food Pairing AI — u actualiseert seizoenswijnen en pairing afgestemd op het seizoensproduct.",
      "5. GastroIMG Gen+ + Pinterest Pins Gen — u genereert referentieafbeeldingen van het nieuwe menu en geoptimaliseerde pins om seizoensgebonden organisch verkeer te trekken."
    ],
    "productsTitle": "Aanbevolen sjablonen en kits voor seizoensmenu",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Gastro Calendar + Creatieve Keuken hebben onze seizoensmenu-afsluiting veranderd. Wat vroeger een week was, is nu een dag met professionele kostenberekening, getraceerd lokaal product en storytelling van producenten voor de bediening. We verhoogden de marge met 6 punten en de acquisitie met Pinterest Pins Gen voor seizoensproduct verdubbelde.",
    "testimonialAuthor": "Marina Lozano",
    "testimonialRole": "Executive chef, auteur restaurant met lokaal product",
    "faqTitle": "Veelgestelde vragen over seizoensmenu met AI",
    "faqs": [
      {
        "q": "Werkt het voor het noordelijk en zuidelijk halfrond?",
        "a": "Ja. Gastro Calendar past lokaal product en seizoen aan per halfrond en regio. Wat herfst is in Spanje, is lente in Argentinië."
      },
      {
        "q": "Hoe beheert het lokaal product met variabele kosten?",
        "a": "Kit de Escandallos Pro herberekent direct de marge wanneer u prijzen bijwerkt. Mermas GenCal voegt de kosten van seizoensverliezen toe (hoger bij product buiten het seizoen)."
      },
      {
        "q": "Deckt het feestdagen per regio?",
        "a": "Ja. Gastro Calendar plant belangrijke feestdagen per land en regio: Pasen, Kerst, Moederdag, Valentijnsdag, lokale feesten (San Fermín, Fallas, enz.)."
      },
      {
        "q": "Genereert het seizoensgebonden visuele content?",
        "a": "Ja. GastroIMG Gen+ + Pinterest Pins Gen genereren referentieafbeeldingen en pins om seizoensgebonden organisch verkeer te trekken. Onthoud dat de AI-afbeelding een visuele referentie is: de definitieve foto maakt u zelf met uw echte gerecht."
      },
      {
        "q": "Hoe helpt het mij met storytelling van producenten?",
        "a": "Creatieve Keuken redeneert vanuit lokaal product: veehouder van een autochtoon ras, biologische boer, ambachtelijke visser, lokale bakker. Elk gerecht bevat professionele storytelling voor bediening en communicatie."
      }
    ],
    "ctaTitle": "Uw seizoensmenu met lokaal product en echte marge.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits.",
    "seo": {
      "title": "Hoe ontwerpt u een seizoensmenu met AI: lokaal product, kostenberekening en storytelling | AI Chef Pro",
      "description": "AI-suite voor seizoensmenu: Gastro Calendar, lokaal product, kostenberekening en storytelling van producenten. Begin vandaag.",
      "keywords": "seizoensmenu AI, seizoensmenu, lokaal product restaurant, gastro calendar, herfst lente menu AI",
      "ogImage": "https://aichef.pro/og/use-cases/task-carta-estacional-con-ia.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd voor uw restaurant vanaf minuut één",
    "personalizationBody": "AI Chef Pro start met «Wie Ben Ik?»: u vertelt het type restaurant, halfrond, regio en focus (km 0, lokaal product, auteurschap). Elke agent reageert aangepast aan uw echte markt.",
    "appsTitle": "De AI-agenten die u gebruikt voor het seizoensmenu",
    "apps": [
      {
        "name": "Gastro Calendar",
        "category": "Content en sociale media",
        "description": "Seizoensplanning per halfrond en regio."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire creativiteit",
        "description": "Signature gerechten met lokaal product in het seizoen."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire creativiteit",
        "description": "Desserts met fruit en seizoensproduct."
      },
      {
        "name": "VegChef Plantaardig",
        "category": "Culinaire creativiteit",
        "description": "Seizoensgroenten met geavanceerde techniek."
      },
      {
        "name": "Food Pairing AI",
        "category": "Culinaire creativiteit",
        "description": "Pairing afgestemd op het seizoensproduct."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Bedrijfsconcepten",
        "description": "Seizoenswijnen voor uw menu."
      },
      {
        "name": "Sosa Ingredients Agent",
        "category": "Gastro leveranciers",
        "description": "Sosa-catalogus om lokaal product aan te vullen."
      },
      {
        "name": "Mermas GenCal",
        "category": "Tools en hulpprogramma's",
        "description": "Seizoensverliezen geïntegreerd in de kostenberekening."
      },
      {
        "name": "Calcula Pax",
        "category": "Tools en hulpprogramma's",
        "description": "Opschaling voor seizoensgebonden privé-evenementen."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro kennis",
        "description": "AI-referentie seizoensfotografie."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en sociale media",
        "description": "Pinterest trekt seizoensgebonden organisch verkeer."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en sociale media",
        "description": "SEO-artikelen over lokaal seizoensproduct."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "snelheid vs. handmatig proces"
      },
      {
        "value": "+6 pp",
        "label": "marge na kostenberekening van het menu"
      },
      {
        "value": "×2",
        "label": "seizoensgebonden organisch verkeer"
      },
      {
        "value": "12+",
        "label": "agenten voor seizoensmenu"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Een week iteraties per nieuw menu",
        "Product buiten het seizoen met hoge kosten",
        "Zonder storytelling van lokale producenten",
        "Reactieve feestdagen, zonder planning",
        "Zonder visuele content voor seizoensacquisitie"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "Seizoensmenu afgesloten in één dag",
        "Lokaal product in het seizoen met geoptimaliseerde kosten",
        "Professionele storytelling van producenten",
        "Feestdagen gepland met 8 weken vooruit",
        "GastroIMG Gen+ + Pinterest trekken seizoensverkeer"
      ]
    },
    "galleryTitle": "Hoe werkt het ontwerpen van een seizoensmenu met AI",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: herfstproduct, lente, kalender, tasting en team. AI-gegenereerde afbeeldingen als visuele referentie van het concept.",
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
    "h1": "Hoe Maakt U Foodfotografie met AI",
    "heroSubtitle": "Genereer professionele referentiebeelden van het gerecht voordat u gaat koken om de presentatie, het palet en de compositie te valideren. Daarna maakt u de definitieve foto van het echte gerecht met een duidelijke richtlijn van het doelbeeld.",
    "heroTagline": "Referentiebeeld eerst, definitieve foto daarna",
    "badge": "Taak: Foodfotografie",
    "painsTitle": "Wat Traditionele Foodfotografie Kost",
    "pains": [
      "Food styling-sessies zonder duidelijk referentiebeeld, dure iteraties",
      "Geen gedeelde richtlijn tussen chef, fotograaf en stylist over compositie en palet",
      "Vers product degradeert tijdens de sessie, foto legt het optimale moment niet vast",
      "Menuwijzigingen vereisen een volledige en dure nieuwe sessie",
      "Beelden voor Instagram, Glovo, web en menu vereisen verschillende formaten",
      "Industrieel beeld vs. auteurbeeld: inconsistente richtlijn tussen kanalen"
    ],
    "featuresTitle": "Hoe AI Chef Pro Foodfotografie Oplost",
    "features": [
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Gespecialiseerde agent in foodfotografie met AI: genereert professioneel referentiebeeld van het gerecht."
      },
      {
        "icon": "Sparkles",
        "title": "Creatieve Keuken met plating",
        "description": "Elk recept levert professionele plating-instructies: compositie, palet, garnering, servies, aanzicht (bovenaanzicht, 3/4, frontaal)."
      },
      {
        "icon": "BookOpen",
        "title": "Beeld als referentie, geen definitieve foto",
        "description": "Het AI-beeld is de visuele gids: paletcontrast, volume, textuur, servies. De definitieve foto voor de kostprijsberekening maakt u zelf met uw echte gerecht."
      },
      {
        "icon": "Calendar",
        "title": "Pinterest Pins Gen",
        "description": "Pinterest genereert stabiel organisch verkeer voor foodfotografie."
      },
      {
        "icon": "Sparkles",
        "title": "InstaFlow AI Pro",
        "description": "Instagram met redactionele kalender en composities aangepast aan de feed."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Beelden aangepast aan Glovo, Uber Eats, Just Eat en platforms met professionele richtlijn voor meer klikken."
      },
      {
        "icon": "CheckSquare",
        "title": "Pro Prompts eBook",
        "description": "300+ professionele prompts voor foodfotografie: stijl, palet, compositie, mood."
      },
      {
        "icon": "Image",
        "title": "Varianten en voorbereidingen",
        "description": "GastroIMG genereert beelden van varianten: alternatieve presentaties, voorbereidingen, mise en place, niet alleen het eindgerecht."
      },
      {
        "icon": "BookOpen",
        "title": "BlogPost SEO Gen+",
        "description": "SEO-artikelen over fotografietechniek met referentiebeelden voor organisch verkeer."
      }
    ],
    "workflowTitle": "Hoe Maakt U Foodfotografie in 4 Stappen",
    "workflow": [
      "1. Creatieve Keuken — u ontwikkelt het gerecht. De AI-agent levert recept + kostprijsberekening + professionele plating-instructies (compositie, palet, servies, aanzicht).",
      "2. GastroIMG Gen+ — u genereert een professioneel referentiebeeld met geoptimaliseerde prompt: warm palet, rustiek servies, bovenaanzicht, microgroenten. U itereert totdat u een duidelijk doelbeeld heeft.",
      "3. U kookt het echte gerecht met het referentiebeeld voor u: zelfde plating, palet, garnering. De definitieve foto voor de kostprijsberekening en het menu maakt u zelf met uw echt opgemaakte gerecht.",
      "4. InstaFlow AI Pro + MenuDish + Pinterest Pins Gen — u past het uiteindelijke beeld aan elk kanaal aan (Instagram, Glovo, web, menu) met professionele richtlijn."
    ],
    "productsTitle": "Aanbevolen Sjablonen en Kits voor Foodfotografie",
    "productIds": [
      "pro-prompts-ebook",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-tareas",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "GastroIMG Gen+ heeft mijn fotografie-workflow veranderd. Voorheen deed ik food styling-sessies zonder duidelijke richtlijn, nu genereer ik het professionele referentiebeeld met AI, valideer ik het palet en de compositie met het team, en daarna maak ik de definitieve foto met mijn echte gerecht. De sessies kosten 70% minder tijd en de visuele consistentie van Instagram + Glovo + web is nu professioneel.",
    "testimonialAuthor": "Carmen Vera",
    "testimonialRole": "Chef en eigenaresse, restaurant met sterke digitale aanwezigheid",
    "faqTitle": "Veelgestelde Vragen over Foodfotografie met AI",
    "faqs": [
      {
        "q": "Is het AI-beeld de definitieve foto van het gerecht?",
        "a": "Nee. Het AI-beeld is een visuele referentie om presentatie, palet, servies en compositie te valideren voordat u gaat koken. De definitieve foto voor de kostprijsberekening, het menu of de technische fiche maakt u zelf met uw echt opgemaakte gerecht."
      },
      {
        "q": "Werkt het voor elke kookstijl?",
        "a": "Ja. GastroIMG Gen+ past de stijl aan: haute cuisine met minimalisme, casual met warmte, mediterraan, Aziatisch, Latijns-Amerikaans, premium fine dining."
      },
      {
        "q": "Deckt het formaten voor Instagram, Glovo, web en menu?",
        "a": "Ja. Het basisbeeld wordt aangepast aan 1:1 (Instagram), 4:5 (feed), 16:9 (digitaal menu), 9:16 (Stories), 4:3 (Glovo, Uber Eats) met professionele richtlijn."
      },
      {
        "q": "Genereert het varianten en voorbereidingen, niet alleen het eindgerecht?",
        "a": "Ja. GastroIMG Gen+ genereert beelden van varianten: alternatieve presentaties, mise en place, voorbereidingen, rauwe ingrediënten, niet alleen het eindgerecht. Handig voor proces-storytelling."
      },
      {
        "q": "Hoe helpt het mij met lokale acquisitie in delivery?",
        "a": "MenuDish Local SEO + GastroIMG Gen+ genereren professionele beelden voor Glovo, Uber Eats, Just Eat met een richtlijn die de CTR verhoogt. Betere foto = meer klikken en betere ranking."
      }
    ],
    "ctaTitle": "Uw foodfotografie met professionele richtlijn.",
    "ctaSubtitle": "Begin met de onboarding van 2 minuten. Lidmaatschapsplan voor €10 per maand met 10.000 credits.",
    "seo": {
      "title": "Hoe Maakt U Foodfotografie met AI: Referentiebeeld en Definitieve Foto | AI Chef Pro",
      "description": "AI-suite voor foodfotografie: GastroIMG Gen+ genereert een referentiebeeld, daarna maakt u de definitieve foto met uw echte gerecht. Begin vandaag.",
      "keywords": "foodfotografie AI, GastroIMG Gen+, food photography AI, referentiebeeld gerecht, foto gerecht delivery",
      "ogImage": "https://aichef.pro/og/use-cases/task-foto-gastronomica-con-ia.jpg"
    },
    "personalizationTitle": "Gepersonaliseerd naar Uw Stijl vanaf Minuut Eén",
    "personalizationBody": "AI Chef Pro start met «Wie Ben Ik?»: u vertelt uw kookstijl, merkpalet, servies en prioritaire kanalen (Instagram, Glovo, web, menu). GastroIMG Gen+ past de visuele stijl aan uw merk aan.",
    "appsTitle": "De AI-Agents die U Gebruikt voor Foodfotografie",
    "apps": [
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Kennis",
        "description": "Gespecialiseerde agent in AI-foodfotografie."
      },
      {
        "name": "Creatieve Keuken",
        "category": "Culinaire Creativiteit",
        "description": "Professionele plating-instructies voor elk recept."
      },
      {
        "name": "Creatieve Patisserie",
        "category": "Culinaire Creativiteit",
        "description": "Plating van desserts met Franse techniek."
      },
      {
        "name": "Creatief IJs",
        "category": "Culinaire Creativiteit",
        "description": "Plating van ijs en halfbevroren desserts met techniek."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Content en Social Media",
        "description": "300+ professionele prompts voor foodfotografie."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Content en Social Media",
        "description": "Instagram met redactionele kalender en aangepaste formaten."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Content en Social Media",
        "description": "Geoptimaliseerde beelden voor Glovo, Uber Eats, Just Eat."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Content en Social Media",
        "description": "Pinterest genereert stabiel organisch verkeer."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Content en Social Media",
        "description": "SEO-artikelen met referentiebeelden."
      },
      {
        "name": "Gastro Calendar",
        "category": "Content en Social Media",
        "description": "Planning van sessies per seizoen."
      },
      {
        "name": "Sonar Deep Research",
        "category": "AI-modellen + LLM",
        "description": "Onderzoek naar visuele trends van referenties."
      },
      {
        "name": "Mentale Coach",
        "category": "Tools en Utilities",
        "description": "Coaching voor creatief leiderschap."
      }
    ],
    "metrics": [
      {
        "value": "−70 %",
        "label": "tijd van food styling-sessies"
      },
      {
        "value": "×3",
        "label": "Instagram-engagement met GastroIMG"
      },
      {
        "value": "+CTR",
        "label": "betere foto = meer klikken in delivery"
      },
      {
        "value": "12+",
        "label": "agents voor foodfotografie"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Zonder AI Chef Pro",
      "beforeItems": [
        "Food styling-sessies zonder duidelijk referentiebeeld",
        "Geen gedeelde richtlijn tussen chef en fotograaf",
        "Menuwijzigingen vereisen een volledige nieuwe sessie",
        "Inconsistent beeld tussen Instagram, Glovo en web",
        "Geen varianten of voorbereidingen voor storytelling"
      ],
      "afterTitle": "Met AI Chef Pro",
      "afterItems": [
        "GastroIMG Gen+ genereert professioneel referentiebeeld",
        "Gedeelde richtlijn gevalideerd voordat u gaat koken",
        "Menuwijzigingen: nieuw AI-beeld in minuten",
        "Consistent beeld tussen alle kanalen",
        "Varianten en voorbereidingen voor volledige storytelling"
      ]
    },
    "galleryTitle": "Hoe Werkt Foodfotografie met AI",
    "gallerySubtitle": "Wat u met AI Chef Pro gaat coördineren: hero, gerecht, camera, tools en team. AI-gegenereerde beelden als visuele referentie van het concept.",
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
