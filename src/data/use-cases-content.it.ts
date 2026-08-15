// Italian content for use-case spokes.
// Each entry mirrors the structure of USE_CASES_CONTENT_ES.
// Missing entries fall back to ES at runtime via makeContent() in use-cases.ts.
//
// Generado el 2026-08-08 traduciendo los 51 spokes ES con bridge.py
// (~deepseek/deepseek-v4-flash-latest, --strict-lang). Antes de esto,
// use-cases.ts:114 hacía backfill al español y 52 de las 83 URLs italianas
// servían título, meta description y cuerpo en CASTELLANO bajo <html lang="it">,
// con index,follow y hreflang recíproco con su gemela española.
//
// Los nombres de agente van con el glosario de la PLATAFORMA italiana viva
// (itapp.aichef.pro/ospite): Gerente de Restaurante Pro → Manager Ristorante Pro,
// Mermas GenCal → Sprechi GenCal, Casual Restaurants AI+ → Ristoranti Casual AI+,
// ¿Quién Soy? → Chi sono?, ID Alérgenos → ID Allergeni, etc.
// Los 7 agentes que NO existen en italiano se dejan con su nombre original a
// propósito: ver CATALOGO_ITALIANO_PENDIENTE.md.
//
// NO editar a mano campo a campo: productIds, galleryImages y features[].icon
// se preservan verbatim desde el ES y hay un validador que lo comprueba.

import type { UseCaseContent } from './use-cases';

export const USE_CASES_CONTENT_IT: Partial<Record<string, UseCaseContent>> = {
  "asador-parrilla": {
    "h1": "IA per Griglieria, Braseria e Steakhouse",
    "heroSubtitle": "Sviluppa menu da griglia con tecnica della brace, schede tecniche per taglio con costo reale, gestisci il dry-aged e pianifica la produzione con una suite di agenti IA gastronomici specializzati in cucina al fuoco, griglieria e steakhouse professionale.",
    "heroTagline": "Griglieria con margine reale e tecnica del fuoco",
    "badge": "Per griglierie, braserie, steakhouse e churrascherie",
    "painsTitle": "Cosa una Griglieria Non Può Evitare di Risolvere",
    "pains": [
      "Costo volatile della carne (chuleton, picanha, ribeye, T-bone) che cambia la scheda tecnica ogni settimana",
      "Standardizzare il punto di cottura e la tecnica della brace turno dopo turno (sezionamento, dry-aged, marezzatura, temperatura interna)",
      "Cali in sezionamento, dry-aging (3-12 % a settimana), sgrassatura e contorni",
      "Gestione del dry-aged con cella, umidità, temperatura e rotazione dei tagli",
      "Differenziarsi in una zona competitiva con tagli premium, tecnica della brace e storytelling dei fornitori di bestiame",
      "Catturare clienti corporate ed eventi privati con menu da griglia ad alto margine"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in una Griglieria",
    "features": [
      {
        "title": "Cucina Creativa",
        "description": "Agente per sviluppare menu da griglia con tecnica della brace, marinate, salse e contorni professionali.",
        "icon": "Flame"
      },
      {
        "title": "Cucina Argentina + Brasiliana",
        "description": "Ricettari specializzati: asado argentino con sale grosso, picanha brasiliana, churrasco, chimichurri autentico, farofa, vinaigrette.",
        "icon": "UtensilsCrossed"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Abbinamenti con vini rossi premium, whisky e cocktail di carattere per la tua griglieria.",
        "icon": "Wine"
      },
      {
        "title": "Schede tecniche per taglio",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica CSV; Kit Escandallos Pro la gestisce con costo reale per chuleton, picanha e T-bone.",
        "icon": "Calculator"
      },
      {
        "title": "Kit di Attività Ristorante Casual",
        "description": "Modelli: accensione della brace, sezionamento, controllo dry-aged, mise dei contorni, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack HACCP griglieria",
        "description": "Tracciabilità della carne, dry-aging, temperature critiche in cella e temperatura interna in cottura.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione con date chiave: Festa del Papà (chuleton), Natale, eventi corporate, lancio di tagli speciali di stagione.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia premium IA di riferimento + Instagram: la griglieria vive dell'impatto visivo della brace e del taglio.",
        "icon": "Image"
      },
      {
        "title": "Sprechi GenCal",
        "description": "Dati precisi sui cali in sezionamento, dry-aging e sgrassatura integrati nella scheda tecnica.",
        "icon": "BarChart3"
      }
    ],
    "workflowTitle": "Una Giornata Reale in una Griglieria con AI Chef Pro",
    "workflow": [
      "09:00 · Apertura — checklist Kit di Attività: accensione controllata della brace (3 ore per arrivare a punto), controllo cella dry-aged, sezionamento dei tagli per il servizio.",
      "11:00 · Cucina Creativa + Cucina Argentina — sviluppi un nuovo taglio signature di chuleton galiziano dry-aged 60 giorni con sale di Maldon affumicato e chimichurri di erbe fresche. Ricetta + scheda tecnica CSV.",
      "12:00 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali della carne e del dry-aged, calcoli il calo per aging, validi il margine per taglio.",
      "13:00 · Servizio mezzogiorno — griglia a pieno regime con tagli premium, mise di chimichurri, salse e contorni.",
      "17:00 · Pausa tra i servizi — Bar & Lounge AI+ valida abbinamenti con rossi per i nuovi tagli; Gastro Calendar pianifica il menu speciale per la Festa del Papà.",
      "20:00 · Servizio cena — picchi coordinati, griglia con più tagli simultanei.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento del nuovo chuleton e i post per Instagram.",
      "00:00 · Chiusura — pulizia profonda delle griglie, HACCP firmato, controllo cella dry-aged."
    ],
    "productsTitle": "Modelli e Kit Consigliati per la Griglieria",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Abbiamo fatto la scheda tecnica taglio per taglio e abbiamo scoperto che il T-bone che vendevamo di più in realtà era in perdita per il calo del dry-aged che non calcolavamo. L'abbiamo ridisegnato con Cucina Creativa aggiustando porzione e contorni, senza toccare il prezzo, e abbiamo alzato il margine di 5 punti. La pianificazione della Festa del Papà con Gastro Calendar ci ha triplicato il fatturato di quella settimana.",
    "testimonialAuthor": "Pedro Aguirre",
    "testimonialRole": "Maestro brasatore e proprietario, griglieria premium",
    "faqTitle": "Domande Frequenti delle Griglierie",
    "faqs": [
      {
        "q": "Va bene per griglieria casual, parrilla argentina, churrascaria brasiliana o steakhouse premium?",
        "a": "Per tutte e quattro. Cucina Creativa + Cucina Argentina + Cucina Brasiliana coprono dalla griglieria casual alla steakhouse premium con tagli dry-aged, passando per la parrilla argentina tradizionale e la churrascaria brasiliana con spiedoni."
      },
      {
        "q": "Copre la tecnica del dry-aged e la gestione della cella?",
        "a": "Sì. Cucina Creativa ragiona come un maestro brasatore professionista: condizioni della cella dry-aged (1-3 °C, 75-85 % di umidità), tempi per taglio, controllo del calo settimanale, identificazione della pellicola e rotazione."
      },
      {
        "q": "Come gestisco il costo volatile della carne?",
        "a": "Kit Escandallos Pro ricalcola all'istante il margine quando aggiorni il prezzo della carne. Sprechi GenCal aggiunge il costo dei cali per dry-aging, sezionamento e sgrassatura. Il taglio riflette sempre il costo attuale."
      },
      {
        "q": "Genera contenuti visivi per Instagram ed eventi corporate?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali di tagli e brace per Instagram, web e menu; la griglieria vive dell'impatto visivo. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo taglio reale."
      },
      {
        "q": "Come mi aiuta con eventi e festività?",
        "a": "Gastro Calendar pianifica Festa del Papà, Natale, eventi corporate e lanci di tagli speciali con menu da griglia e calendario editoriale."
      }
    ],
    "ctaTitle": "La tua griglieria con margine reale e tecnica del fuoco.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Griglieria, Braseria e Steakhouse: Tagli, Schede Tecniche e Dry-Aged | AI Chef Pro",
      "description": "Suite IA per griglierie e steakhouse: Cucina Argentina + Brasiliana, schede tecniche per taglio, dry-aged, branding e HACCP. Inizia oggi.",
      "keywords": "IA griglieria, software steakhouse, schede tecniche chuleton, parrilla argentina IA, dry-aged, churrascaria, griglieria premium",
      "ogImage": "https://aichef.pro/og/use-cases/asador-parrilla-steakhouse.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Griglieria dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di griglieria gestisci (parrilla argentina, churrascaria brasiliana, steakhouse premium con dry-aged, griglieria casual di quartiere, griglieria con cucina d'autore), dimensione del team, città e specialità. Ogni agente risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nella Tua Griglieria",
    "apps": [
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di menu da griglia con tecnica della brace, marinate e contorni professionali.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Argentina",
        "description": "Asado argentino, chimichurri, provolone, animelle e tecnica della parrilla autentica.",
        "category": "Ricettari Latinoamericani"
      },
      {
        "name": "Cucina Brasiliana",
        "description": "Picanha, churrasco, farofa, vinaigrette e tecnica della churrascaria brasiliana.",
        "category": "Ricettari Latinoamericani"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con rossi potenti, whisky e cocktail di carattere per griglieria.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Per il bancone della griglieria con vini rossi premium e cocktail di carattere.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture, sali speziati e tecniche applicate a salse e marinate.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Cali in sezionamento, dry-aging, sgrassatura e cottura.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per taglio e contorno.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia premium IA di riferimento per Instagram, web, menu e delivery.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale professionale per griglieria premium.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"griglieria vicino a me\" o \"parrilla argentina\".",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Festa del Papà, Natale, eventi corporate, lanci di stagione.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo le schede tecniche dei tagli"
      },
      {
        "value": "×3",
        "label": "fatturato per la Festa del Papà"
      },
      {
        "value": "−15 %",
        "label": "cali in sezionamento e dry-aging"
      },
      {
        "value": "12+",
        "label": "agenti per la tua griglieria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Punto di cottura improvvisato, consistenza variabile tra brasatore e turno",
        "Schede tecniche senza calo del dry-aged, tagli premium in perdita senza saperlo",
        "Cella dry-aged senza tracciabilità reale né controllo documentato",
        "Cali in sezionamento e sgrassatura senza tracciabilità",
        "Instagram improvvisato, senza storytelling del fornitore di bestiame"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Punto di cottura consistente con criterio tecnico documentato",
        "Scheda tecnica professionale per taglio con calo del dry-aged integrato",
        "Cella dry-aged con tracciabilità HACCP e rotazione documentata",
        "Cali controllati con Sprechi GenCal e modelli specifici",
        "GastroIMG Gen+ + InstaFlow + storytelling del fornitore di bestiame"
      ]
    },
    "galleryTitle": "Come Funziona una Griglieria",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: griglia, brace, dry-aged, tagli e team. Immagini generate con IA come riferimento visivo del concept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-asador-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-brasas.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-dryaged.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-chuleton.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-despiece.jpg",
      "/lovable-uploads/ai-gallery/use-case-asador-team.jpg"
    ]
  },
  "bar-cocktails": {
    "h1": "IA per Bar e Cocktail d'Autore",
    "heroSubtitle": "Progetta carte di cocktail d'autore, calcola il food cost di ogni drink con i tuoi prezzi reali e ottieni un branding professionale con una suite di agenti IA pensati per bartender, cocktail maker e titolari di bar.",
    "heroTagline": "Il tuo bancone con margine reale, cocktail con tecnica",
    "badge": "Per cocktail bar e locali di mixology",
    "painsTitle": "Cosa un Cocktail Bar Non Può Non Risolvere",
    "pains": [
      "Calcolare il food cost di cocktail complessi con molti ingredienti, infusioni e tecniche",
      "Sprechi e rotture di vetreria al bancone che intaccano la redditività senza controllo",
      "Carte di drink che cambiano stagionalmente con ricerca e sviluppo continui",
      "Margine molto ridotto sugli spiriti con costo degli alcolici premium volatile",
      "Differenziarsi in una zona competitiva con storytelling e branding visivo dei cocktail",
      "Gestire cocktail d'autore combinati con birreria, vini e carta di tapas"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Cocktail Bar",
    "features": [
      {
        "title": "Bar & Lounge AI+",
        "description": "Agente specializzato in pub, cocktail bar, enoteche, sports bar e locali notturni con conoscenza professionale.",
        "icon": "Wine"
      },
      {
        "title": "Food Pairing AI",
        "description": "Abbinamenti inaspettati per cocktail d'autore con base scientifica e pairing con tapas.",
        "icon": "Sparkles"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Fermentazioni per cocktail avanzati: kombucha come base, infusioni, lattofermentati agli agrumi.",
        "icon": "Beaker"
      },
      {
        "title": "Food cost per drink",
        "description": "Cucina Creativa fornisce ricetta + food cost in CSV; Kit de Escandallos Pro lo gestisce con i tuoi prezzi reali e margine professionale per cocktail.",
        "icon": "Calculator"
      },
      {
        "title": "Carte cocktail con storytelling",
        "description": "Progettazione di carte e rotazione stagionale con storytelling professionale per sala e stampa.",
        "icon": "BookOpen"
      },
      {
        "title": "Kit de Tareas Bar",
        "description": "Modelli: preparazione di succhi, sciroppi, guarnizioni, infusioni, mise del bancone, servizio e pulizia profonda.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC Bar",
        "description": "Tracciabilità specifica: succhi freschi, creme, conservazione delle guarnizioni, lavaggio della vetreria.",
        "icon": "ShieldCheck"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia di cocktail con IA + contenuti per Instagram con calendario editoriale professionale.",
        "icon": "Image"
      },
      {
        "title": "Sosa Ingredients AI + tSpoonLab Agent",
        "description": "Assistenti per la selezione di ingredienti tecnici premium molto usati nella cocktaileria d'autore.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Cocktail Bar con AI Chef Pro",
    "workflow": [
      "11:00 · Apertura — checklist Kit de Tareas Bar: preparazione di succhi, sciroppi, infusioni e guarnizioni.",
      "14:00 · Bar & Lounge AI+ + Food Pairing AI — sviluppi un nuovo cocktail per la carta di primavera pensando all'abbinamento.",
      "15:00 · Cucina Creativa fornisce ricetta + food cost in CSV; Kit de Escandallos Pro lo gestisce con i tuoi prezzi reali (gin premium, sciroppi, guarnizioni).",
      "16:00 · Testing del cocktail con il team, aggiustamenti finali di equilibrio e proporzioni.",
      "17:00 · Pro Prompts eBook + BlogPost SEO Gen+ — scrivi lo storytelling per la nuova carta e la nota per la sala.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi la fotografia e i post di Instagram per il lancio.",
      "20:00 · Servizio serale — bancone coordinato, food cost validati, cocktail serviti con precisione.",
      "02:30 · Chiusura — pulizia profonda, HACCP firmato, report dei drink del giorno."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Bar e Cocktail Bar",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Avere ogni cocktail con il food cost calcolato e la carta pronta in una mattinata ha cambiato il mio modo di lavorare. Prima era con calcolatrice, tovagliolo e molta intuizione. Ora con Bar & Lounge AI+ e il Kit de Escandallos Pro esce una carta nuova con margine validato in 2 ore.",
    "testimonialAuthor": "Hugo Vázquez",
    "testimonialRole": "Bartender e titolare, cocktail bar d'autore",
    "faqTitle": "Domande Frequenti di Bartender e Cocktail Maker",
    "faqs": [
      {
        "q": "Serve per cocktail d'autore o casual?",
        "a": "Per entrambe. Bar & Lounge AI+ + Food Pairing AI coprono dai cocktail classici alla mixology d'avanguardia con tecnica professionale."
      },
      {
        "q": "Copre birreria e vini oltre alla cocktaileria?",
        "a": "Sì. Bar & Lounge AI+ copre tutto lo spettro del bancone: birrerie, enoteche, locali notturni, pub tradizionali e sports bar."
      },
      {
        "q": "Genera idee di nuovi drink con tecnica?",
        "a": "Sì. Bar & Lounge AI+ + Cucina Creativa + Food Pairing AI + Fermentus Con AI+ lavorano insieme per creare cocktail con base professionale."
      },
      {
        "q": "Funziona per bar d'hotel o locale indipendente?",
        "a": "Entrambi. Il bar lobby dell'hotel si gestisce dal caso /usos/concepto/hotel-completo-fb; il bar indipendente da qui."
      },
      {
        "q": "Come mi aiuta con il branding visivo dei miei cocktail?",
        "a": "GastroIMG Gen+ genera fotografie professionali di ogni drink per Instagram, web e carta. InstaFlow AI Pro programma i contenuti con calendario editoriale."
      }
    ],
    "ctaTitle": "Mixology con margine reale e branding professionale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Bar e Cocktail d'Autore: Food Cost e Branding",
      "description": "Suite di IA per bar e cocktail bar professionali: Bar & Lounge AI+, Food Pairing AI, food cost per cocktail, carte, HACCP e branding visivo. Inizia oggi.",
      "keywords": "IA bar cocktail, food cost cocktail, software bar, IA bartender, IA cocktail maker, cocktail bar IA, bar d'autore Italia, gestione cocktail bar IA",
      "ogImage": "https://aichef.pro/og/use-cases/bar-cocktails.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Bar dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di bar gestisci (cocktail bar, enoteca, birreria, pub, locale notturno), città e carta. Ogni agente —da Bar & Lounge AI+ fino al Kit de Escandallos Pro— risponde adattato al tuo stile di bancone e al tuo mercato.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Bar",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "description": "Agente principale: pub, cocktail bar, enoteche, sports bar, locali notturni.",
        "category": "Concetti di Business"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di cocktail con ricetta + food cost in CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Combinazioni scientifiche per cocktail d'autore e abbinamenti con tapas.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Fermentazioni per cocktaileria avanzata: kombucha, infusioni, lattofermentati.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Per bar con carta di tapas e cucina leggera oltre alla cocktaileria.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Assistente per ingredienti tecnici del catalogo Sosa.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Assistente del catalogo tSpoonLab per la cocktaileria tecnica.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni in cocktail e tapas.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi sugli sprechi in succhi, guarnizioni e vetreria.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA per cocktail: web, social e carta.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Contenuti virali Instagram per la cocktaileria con calendario editoriale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pro Prompts eBook",
        "description": "300+ prompt per storytelling di cocktail, comunicazione con la stampa e formazione.",
        "category": "Gastro Conoscenza"
      }
    ],
    "metrics": [
      {
        "value": "×4",
        "label": "velocità chiusura carta cocktail"
      },
      {
        "value": "+5 pp",
        "label": "margine dopo food cost professionale"
      },
      {
        "value": "×3",
        "label": "engagement Instagram con GastroIMG"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Cocktail con food cost calcolato con calcolatrice e tovagliolo",
        "Carte di drink senza storytelling professionale per la sala",
        "Sprechi al bancone e vetreria senza tracciabilità",
        "Branding visivo improvvisato su Instagram con foto dal telefono",
        "Senza accesso sistematico alle tendenze della cocktaileria internazionale"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Bar & Lounge AI+ + Cucina Creativa + Kit de Escandallos Pro chiudono le carte in 2 ore",
        "Storytelling professionale per ogni cocktail pronto per sala e stampa",
        "Sprechi controllati con Sprechi GenCal e modelli specifici",
        "GastroIMG Gen+ + InstaFlow generano foto professionali e post virali",
        "Sonar Deep Research fornisce tendenze e riferimenti internazionali"
      ]
    },
    "galleryTitle": "Come Funziona un Cocktail Bar Professionale",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: bancone principale, tecnica di shaker, cocktail finale, preparazione delle guarnizioni, tecnica di versata e servizio.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-bar-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-shaker.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-cocktail.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-pour.jpg",
      "/lovable-uploads/ai-gallery/use-case-bar-team.jpg"
    ]
  },
  "bartender-coctelero": {
    "h1": "IA per Bartender e Cocktail Maker",
    "heroSubtitle": "Progetta carte di cocktail con food cost professionale, food cost per drink con costo reale e tecnica, e crea drink d'autore con storytelling e abbinamenti con una suite di agenti IA gastronomici specializzati in cocktaileria.",
    "heroTagline": "Cocktaileria con margine reale e tecnica d'autore",
    "badge": "Per barman, cocktail maker e mixologist",
    "painsTitle": "Cosa un Barman Non Può Evitare di Risolvere",
    "pains": [
      "Calcolare il food cost di cocktail complessi con molti ingredienti (distillati, cordial, infusioni, garnish) senza perdere ore con la calcolatrice",
      "Rinnovare la carta ogni stagione con nuovi drink mantenendo margine e un food cost coerente con il resto del bar",
      "Standardizzare le ricette al banco affinché ogni cameriere replichi il drink con lo stesso equilibrio ogni volta",
      "Controllare gli sprechi al banco: rottura di bicchieri, over-pour, evaporazione, garnish che si buttano",
      "Storytelling: ogni cocktail necessita di un nome, una storia e un abbinamento che giustifichi il prezzo alto",
      "Differenziarsi in una zona competitiva con cocktaileria d'autore, branding visivo e social media attivi"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Barman",
    "features": [
      {
        "title": "Bar & Lounge AI+",
        "description": "Agente specializzato in cocktaileria professionale, enoteche, bar e distillati con tecnica avanzata.",
        "icon": "Wine"
      },
      {
        "title": "Food Pairing AI",
        "description": "Combinazioni inaspettate per cocktail d'autore con base scientifica e abbinamenti con la cucina.",
        "icon": "Sparkles"
      },
      {
        "title": "Food cost per drink",
        "description": "Bar & Lounge AI+ fornisce ricetta + food cost CSV con tecnica; Kit Escandallos Pro lo gestisce con costo reale per drink, food cost % e prezzo suggerito.",
        "icon": "Calculator"
      },
      {
        "title": "Schede tecniche del cocktail",
        "description": "Ricetta, tecnica, garnish, bicchiere, abbinamento e storytelling in un unico documento pronto per il team.",
        "icon": "BookOpen"
      },
      {
        "title": "Kit di Attività Bar",
        "description": "Modelli: mise del banco, preparazione di cordial e infusioni, procedure per turno, chiusura di cassa, controllo scorte.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack HACCP bar",
        "description": "Tracciabilità di ghiaccio, garnish freschi, infusioni fatte in casa e temperature critiche.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione della carta stagionale: cocktail estivi, caldi invernali, carte a tema per San Valentino, Natale ed eventi.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia di cocktail con IA di riferimento + contenuti per Instagram con calendario editoriale professionale.",
        "icon": "Image"
      },
      {
        "title": "KPI del banco",
        "description": "Scontrino medio, rotazione dei drink, margine per categoria (classici, signature, vini, birre).",
        "icon": "BarChart3"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Barman con AI Chef Pro",
    "workflow": [
      "11:00 · Apertura — checklist Kit di Attività Bar: mise di garnish freschi, preparazione di cordial fatti in casa, caricare il ghiaccio, revisione scorte.",
      "12:00 · Bar & Lounge AI+ — sviluppi un nuovo signature per la carta estiva (gin con shrub di fragole e basilico). Cucina Creativa consegna ricetta + food cost CSV.",
      "13:00 · Food Pairing AI — validi l'abbinamento con un piatto della cucina e affini la tecnica.",
      "14:00 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali di distillato premium e ingredienti, validi margine per drink e food cost %.",
      "17:00 · Servizio — il team replica il drink con la scheda tecnica (ricetta, tecnica, garnish, bicchiere, storytelling).",
      "19:00 · Gastro Calendar — aggiorni il calendario editoriale di Instagram con il lancio del nuovo signature.",
      "20:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento del drink e i post per il lancio.",
      "02:00 · Chiusura — pulizia profonda, HACCP firmato, controllo sprechi e scorte finali."
    ],
    "productsTitle": "Modelli e Kit Consigliati per la Cocktaileria",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "AI Chef Pro mi ha cambiato il modo di chiudere le carte dei cocktail. Prima era una settimana di tovaglioli e calcolatrice; ora è un giorno con food cost professionale, scheda tecnica con storytelling e abbinamento validato, pronta per essere replicata dal mio team. Abbiamo aumentato il margine di 5 punti e triplicato l'engagement su Instagram con GastroIMG.",
    "testimonialAuthor": "Hugo Vázquez",
    "testimonialRole": "Barman, cocktail bar d'autore",
    "faqTitle": "Domande Frequenti dei Barman",
    "faqs": [
      {
        "q": "Funziona per cocktaileria classica, d'autore o casual?",
        "a": "Per tutte e tre. Bar & Lounge AI+ comprende dai classici IBA fino all'avanguardia: shrub, infusioni, fermentati, schiume, affumicati controllati, tecnica avanzata del banco."
      },
      {
        "q": "Copre vini e birre oltre alla cocktaileria?",
        "a": "Sì. L'agente copre tutto lo spettro del banco: cocktail, vini, birre, distillati, analcolici e abbinamenti."
      },
      {
        "q": "Permette di creare carte di drink con storytelling e tecnica?",
        "a": "Sì. Le schede includono ricetta, tecnica, garnish, bicchiere, storia e abbinamento pronti per la sala. Ideale per alzare lo scontrino medio giustificando il prezzo."
      },
      {
        "q": "Genera contenuti visivi per Instagram e carta?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali di ogni drink per Instagram, web e carta; InstaFlow AI Pro programma contenuti con calendario editoriale. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo cocktail impiattato reale."
      },
      {
        "q": "Come mi aiuta con la stagionalità della carta?",
        "a": "Gastro Calendar pianifica le carte stagionali (estate, autunno, Natale, San Valentino) in anticipo. Il Kit Plan Finanziario proietta il cash flow stagionale realistico per arrivare con scorte e cassa a ogni picco."
      }
    ],
    "ctaTitle": "La tua cocktaileria con margine reale e tecnica d'autore.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Barman e Cocktail Maker: Carte, Food Cost e Storytelling | AI Chef Pro",
      "description": "Suite di IA per barman professionisti: Bar & Lounge AI+, Food Pairing AI, food cost per drink, schede tecniche con storytelling e branding visivo. Inizia oggi.",
      "keywords": "IA barman, IA cocktail maker, software cocktaileria, food cost cocktail, food pairing IA, carta cocktail IA, mixologist IA, signature cocktail",
      "ogImage": "https://aichef.pro/og/use-cases/bartender-coctelero.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Bar dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di bar gestisci (cocktail bar d'autore, enoteca, bar d'hotel, lounge, ristorante con cocktaileria), dimensione del team, città e stile di carta. Ogni agente —da Bar & Lounge AI+ a Gastro Calendar— risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Bar",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "description": "Agente specializzato in cocktaileria professionale, vini, birre e distillati con tecnica avanzata.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Combinazioni inaspettate con base scientifica e abbinamenti cocktail + piatto.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di drink signature con ricetta + food cost CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture avanzate, gelificanti e tecniche di bar d'autore.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Assistente del catalogo tSpoonLab per applicazioni avanzate di mixologia.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati sugli sprechi al banco: rottura, over-pour, evaporazione, garnish buttati.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per drink: solfiti, latticini, frutta secca, glutine.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA di riferimento per web, social e carta dei cocktail.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale professionale per cocktaileria d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"cocktail bar vicino\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Pianificazione della carta stagionale: estate, inverno, San Valentino, Natale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico stabile per cocktail con storytelling.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo il food cost della carta"
      },
      {
        "value": "×3",
        "label": "engagement Instagram con GastroIMG"
      },
      {
        "value": "−1 giorno",
        "label": "chiusura carta di stagione (da 7 a 1)"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Carte chiuse in una settimana di tovaglioli e calcolatrice",
        "Food cost senza costo reale per drink, signature in perdita senza saperlo",
        "Schede tecniche inesistenti: ogni cameriere replica come può",
        "Sprechi al banco senza tracciabilità reale",
        "Instagram improvvisato con foto dal telefono senza continuità"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Carta di stagione chiusa in un giorno con food cost professionale e storytelling",
        "Food cost reale per drink, signature con margine validato",
        "Schede tecniche con ricetta, tecnica, garnish, bicchiere, abbinamento e storytelling",
        "Sprechi controllati con Sprechi GenCal e modelli specifici per il banco",
        "Instagram con calendario editoriale professionale e GastroIMG Gen+"
      ]
    },
    "galleryTitle": "Come Funziona un Bar d'Autore",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: bar, cocktail, tecnica, mise, ingredienti e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-bartender-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-cocktails.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-technique.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-ingredients.jpg",
      "/lovable-uploads/ai-gallery/use-case-bartender-team.jpg"
    ]
  },
  "cafeteria-brunch": {
    "h1": "IA per Caffetteria e Brunch",
    "heroSubtitle": "Ottimizza colazioni, brunch, caffè specialty e pasticceria con una suite di agenti IA pensati per coffee shop, locali di brunch e caffetterie moderne.",
    "heroTagline": "Coffee shop moderno con operativa moderna",
    "badge": "Per caffetterie specialty e brunch",
    "painsTitle": "Ciò che un Coffee Shop o un Locale di Brunch Non Può Non Risolvere",
    "pains": [
      "Carta corta ma rotazione altissima nelle ore di punta del mattino e di mezzogiorno",
      "Margine molto stretto su caffè specialty e pasticceria con costo di latte e cacao volatile",
      "Team giovane e rotativo che necessita di formazione rapida al banco e al servizio",
      "Branding e social media (Instagram, Pinterest) sono la leva principale di acquisizione",
      "Differenziarsi in una zona competitiva con pricing premium ma accessibile",
      "Gestire il flusso del brunch nei fine settimana senza far collassare l'operatività durante la settimana"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in una Caffetteria di Brunch",
    "features": [
      {
        "title": "Ristoranti Casual AI+",
        "description": "Agente con conoscenza di coffee shop, brunch e caffetteria specialty: menu, pricing e operatività.",
        "icon": "Coffee"
      },
      {
        "title": "Schede tecniche di caffè, brunch e pasticceria",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica CSV; Kit de Escandallos Pro lo gestisce con i tuoi prezzi reali.",
        "icon": "Calculator"
      },
      {
        "title": "Pasticceria Creativa + Panificazione Creativa",
        "description": "Ricette professionali per pasticceria, brioche, croissant, cake e panificazione artigianale.",
        "icon": "Sparkles"
      },
      {
        "title": "Kit de Tareas Cafetería",
        "description": "Modelli specifici: apertura, chiusura, banco, cucina leggera, brunch, servizio e pulizia.",
        "icon": "CheckSquare"
      },
      {
        "title": "HACCP semplificato",
        "description": "Pack HACCP con registri minimi ma completi per caffetteria: latte, conservazione, lavaggio, temperature.",
        "icon": "ShieldCheck"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia gastronomica IA + contenuti Instagram con caption, calendario editoriale e pianificazione.",
        "icon": "Image"
      },
      {
        "title": "Pinterest Pins Gen",
        "description": "Pinterest è fondamentale per i coffee shop: pin di brunch, caffè latte art e pasticceria per attrarre traffico organico.",
        "icon": "Search"
      },
      {
        "title": "KPI e scontrino medio",
        "description": "Kit Plan Financiero: tasso di occupazione, scontrino medio, produttività e upselling di brunch e caffè.",
        "icon": "BarChart3"
      },
      {
        "title": "Keyword Discovery AI+",
        "description": "Parole chiave gastronomiche locali per «brunch [il tuo quartiere]», «caffè specialty vicino» e simili.",
        "icon": "Search"
      }
    ],
    "workflowTitle": "Una Giornata Reale in una Caffetteria di Brunch con AI Chef Pro",
    "workflow": [
      "07:00 · Apertura — checklist del Kit de Tareas Cafetería: banco avviato, caffè macinato, latte freddo, vetrina pronta.",
      "08:00 · Servizio mattina — colazioni e caffè specialty con flusso coordinato tra banco e cucina leggera.",
      "11:00 · Cucina Creativa — sviluppi un nuovo brunch per sabato: toast con burrata, gravlax e uova. Ricevi scheda tecnica CSV.",
      "11:30 · Kit de Escandallos Pro — carichi il CSV con prezzi reali e validi il margine obiettivo (32%).",
      "13:00 · Servizio mezzogiorno — brunch in corso, team coordinato con modelli specifici.",
      "16:00 · GastroIMG Gen+ + Pinterest Pins Gen — generi fotografie del nuovo brunch e pin ottimizzati per Pinterest.",
      "17:30 · InstaFlow AI Pro — programmi post di Instagram per la prossima settimana con calendario editoriale.",
      "19:30 · Chiusura — pulizia profonda, HACCP firmato, pianificazione della pasticceria per il giorno successivo."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Caffetterie",
    "productIds": [
      "kit-tareas-cafeteria",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Facciamo brunch nei fine settimana e caffè specialty durante la settimana. Il Kit de Tareas Cafetería e la generazione di contenuti per Instagram mi hanno restituito i pomeriggi. Pinterest Pins Gen è stata una scoperta: ci ha portato traffico organico che non avevo mai visto.",
    "testimonialAuthor": "Marcos Rivera",
    "testimonialRole": "Proprietario, coffee shop specialty e brunch",
    "faqTitle": "Domande Frequenti dei Coffee Shop",
    "faqs": [
      {
        "q": "Serve per caffè specialty o solo caffetteria casual?",
        "a": "Serve per entrambi. Ci sono modelli adattabili sia a coffee shop specialty (V60, espresso di origine, latte art) che a caffetterie casual e brunch."
      },
      {
        "q": "Funziona per locali con cucina molto leggera?",
        "a": "Sì. Il Kit de Tareas Cafetería ha modelli specifici per cucina leggera, brunch e banco, senza presupporre che tu abbia una brigata completa."
      },
      {
        "q": "Genera contenuti ottimizzati per Instagram e Pinterest?",
        "a": "Sì. InstaFlow AI Pro e Pinterest Pins Gen sono agenti specifici per quei canali. Pinterest funziona molto bene per brunch e caffè con traffico organico stabile."
      },
      {
        "q": "Copre delivery e orari estesi?",
        "a": "Sì. I modelli sono adattabili a orari, delivery, take-away e catering leggero (coffee break aziendale)."
      },
      {
        "q": "Come ottimizza la SEO locale per il mio coffee shop?",
        "a": "MenuDish Local SEO + BlogPost SEO Gen+ + Keyword Discovery AI+ lavorano insieme per catturare ricerche locali come «brunch a [la tua zona]» o «miglior caffè specialty vicino»."
      }
    ],
    "ctaTitle": "La tua caffetteria con operatività curata e acquisizione organica.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Caffetteria e Brunch: Operatività, Pinterest e SEO",
      "description": "Suite IA per coffee shop e locali di brunch: agenti specializzati, schede tecniche, HACCP, contenuti per Instagram e Pinterest, SEO locale. Inizia oggi.",
      "keywords": "IA caffetteria, software brunch, IA coffee shop, gestione caffetteria specialty, schede tecniche caffè, marketing caffetteria IA, Pinterest brunch, SEO locale caffetteria, coffee shop Italia",
      "ogImage": "https://aichef.pro/og/use-cases/cafeteria-brunch.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Coffee Shop dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di caffetteria gestisci (specialty, brunch, casual), città e modo di lavorare. Da quel momento, ogni agente —da Pasticceria Creativa a Pinterest Pins Gen— risponde adattato al tuo contesto: scontrino medio della tua zona, profilo cliente e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nella Tua Caffetteria",
    "apps": [
      {
        "name": "Ristoranti Casual AI+",
        "description": "Agente principale: coffee shop, brunch e caffetteria con base professionale.",
        "category": "Concetti di Business"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Ricette professionali per pasticceria di caffetteria: brioche, croissant, cake, torte.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Panificazione Creativa",
        "description": "Per coffee shop che sfornano il proprio pane e lievitati con pasta madre.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di piatti brunch con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Pasto del Personale",
        "description": "Generatore di menu per lo staff che motivano il team.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Descrizioni SEO locale per migliorare il posizionamento.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Post di blog per attrarre traffico organico verso il coffee shop.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Keyword Discovery AI+",
        "description": "Parole chiave per zona postale: brunch, caffè specialty, ecc.",
        "category": "Contenuti e Social"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Contenuti virali Instagram con calendario editoriale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pin ottimizzati per Pinterest: brunch, caffè, pasticceria.",
        "category": "Contenuti e Social"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA per web, social e menu.",
        "category": "Gastro Conoscenza"
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "traffico organico via Pinterest"
      },
      {
        "value": "+ €1,80",
        "label": "scontrino medio per upselling"
      },
      {
        "value": "−4 h",
        "label": "settimanali in gestione social"
      },
      {
        "value": "12+",
        "label": "agenti per la tua caffetteria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Operatività di banco e cucina leggera improvvisata a ogni turno",
        "Schede tecniche a occhio su caffè e pasticceria con margine incerto",
        "Instagram caotico senza calendario editoriale né continuità",
        "Senza presenza su Pinterest, perdendo il traffico organico che converte di più per il brunch",
        "HACCP su quaderno che si dimentica durante l'ispezione"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Kit de Tareas Cafetería con modelli specifici per turno e partita",
        "Scheda tecnica professionale per ogni bevanda e piatto con margine reale",
        "InstaFlow AI Pro con calendario editoriale e caption ottimizzate",
        "Pinterest Pins Gen che cattura traffico organico stabile e ad alta conversione",
        "HACCP da mobile con registri pronti per l'ispezione"
      ]
    },
    "galleryTitle": "Come Funziona una Caffetteria di Brunch Moderna",
    "gallerySubtitle": "Ciò che coordinerai con AI Chef Pro: specialty e brunch, barista, pasticceria, team di turno e contenuti per i social.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-cafeteria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-brunch.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-barista.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-pastry.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-cafeteria-instagram.jpg"
    ]
  },
  "catering-eventos": {
    "h1": "IA per Catering ed Eventi",
    "heroSubtitle": "Scheda tecnica per evento, pianifica la produzione su larga scala, gestisci logistica e HACCP fuori sede con una suite di agenti IA specializzati in catering professionale, matrimoni, eventi aziendali e cocktail.",
    "heroTagline": "Eventi con margine, senza caos",
    "badge": "Per aziende di catering ed eventi",
    "painsTitle": "Ciò che un Catering Non Può Non Risolvere",
    "pains": [
      "Calcolare il food cost di menu con alta variabilità di ospiti (50, 200, 500) quando i prezzi cambiano ogni settimana",
      "Pianificare produzione e mise en place su larga scala dalla cucina centrale",
      "Coordinare logistica, trasporto refrigerato e allestimento presso la sede del cliente",
      "Mantenere HACCP e tracciabilità fuori dal locale fisso, in sedi esterne e veicoli",
      "Attrarre clienti aziendali con proposte professionali che chiudano contratti di maggiore valore",
      "Gestire simultaneamente più eventi del fine settimana senza errori"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta nel Catering e negli Eventi",
    "features": [
      {
        "title": "Catering AI+",
        "description": "Agente specializzato in catering ed eventi gastronomici: matrimoni, eventi aziendali, cocktail e galà con conoscenza professionale.",
        "icon": "PartyPopper"
      },
      {
        "title": "Cucina Creativa + Food Pairing AI",
        "description": "Brainstorming per menu di evento. Cucina Creativa fornisce ricetta + scheda tecnica CSV pronta per il Kit de Escandallos Pro.",
        "icon": "Sparkles"
      },
      {
        "title": "Food cost per evento",
        "description": "Kit de Escandallos Pro: carichi il CSV con i tuoi prezzi reali, regoli il numero di ospiti e ottieni il margine all'istante.",
        "icon": "Calculator"
      },
      {
        "title": "Calcula Pax",
        "description": "Calcolatore di porzioni che scala le ricette a 50, 200, 500 o 1000 commensali in pochi secondi.",
        "icon": "Layers"
      },
      {
        "title": "Kit de Tareas Catering",
        "description": "Modelli: produzione centrale, trasporto refrigerato, allestimento in sede, servizio e smontaggio.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC fuori dal locale",
        "description": "Tracciabilità in trasporto, sede esterna e servizio esterno con registrazioni da mobile.",
        "icon": "ShieldCheck"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA per proposte a clienti aziendali e galleria di eventi.",
        "icon": "Image"
      },
      {
        "title": "ID Allergeni",
        "description": "Identificazione automatica critica per eventi con profili alimentari vari.",
        "icon": "ShieldCheck"
      },
      {
        "title": "BlogPost SEO Gen+ + Keyword Discovery AI+",
        "description": "Acquisizione organica di aziende che cercano catering nella tua zona.",
        "icon": "Search"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un'Impresa di Catering con AI Chef Pro",
    "workflow": [
      "08:30 · Catering AI+ — l'agente ti aiuta a finalizzare il menu proposto per un matrimonio di 180 invitati in base al briefing del cliente.",
      "09:30 · Cucina Creativa — sviluppi i 12 piatti del menu con ricetta e scheda tecnica CSV con prezzi di riferimento.",
      "10:30 · Calcula Pax + Kit de Escandallos Pro — scalì a 180 commensali, carichi il CSV con i tuoi prezzi reali e validi il margine.",
      "12:00 · GastroIMG Gen+ — generi fotografie dei piatti da includere nella presentazione al cliente.",
      "14:00 · Riunione con il cliente — proposta chiusa con presentazione professionale invece dei vecchi modelli Word.",
      "16:00 · Kit de Tareas Catering — pianifichi produzione centrale, trasporto, allestimento e servizio dell'evento di sabato.",
      "18:00 · Pack APPCC — prepari registrazioni di temperatura per il trasporto e la tracciabilità in sede esterna.",
      "20:00 · Brief al team — prepari il brief di produzione, trasporto, allestimento e servizio da un'unica fonte."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Catering",
    "productIds": [
      "kit-tareas-catering",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Chiudiamo eventi in un terzo del tempo. Le schede tecniche per evento si adattano al dettaglio in base al numero di ospiti, i modelli di logistica sono oro e le proposte con fotografia professionale chiudono contratti aziendali che prima ci sfuggivano. Margine +5 punti nel primo trimestre solo grazie a un migliore food cost.",
    "testimonialAuthor": "Sara Pérez",
    "testimonialRole": "Azienda di catering aziendale e matrimoni (200 eventi all'anno)",
    "faqTitle": "Domande Frequenti delle Aziende di Catering",
    "faqs": [
      {
        "q": "Va bene per catering boutique o grande?",
        "a": "Per entrambi. Dai catering boutique con 50 ospiti al mese fino ad aziende con oltre 1000 servizi al mese ed eventi con 2000 commensali."
      },
      {
        "q": "Copre matrimoni, eventi aziendali e cocktail?",
        "a": "Sì. Catering AI+ e il Kit de Tareas Catering hanno modelli specifici per i tre formati e per galà/eventi speciali."
      },
      {
        "q": "C'è un HACCP specifico fuori dal locale fisso?",
        "a": "Sì. Il Pack APPCC ha modelli adattati al prodotto che viaggia in zaino, moto, furgone refrigerato o cucina centrale, inclusa la tracciabilità in sede esterna."
      },
      {
        "q": "Genera proposte commerciali per aziende?",
        "a": "Sì. Catering AI+ + GastroIMG Gen+ + Pro Prompts eBook permettono di redigere proposte professionali con fotografia gastronomica e storytelling."
      },
      {
        "q": "Come mi aiuta ad attrarre clienti aziendali?",
        "a": "BlogPost SEO Gen+ + Keyword Discovery AI+ + MenuDish Local SEO lavorano insieme per attrarre aziende che cercano catering nella tua zona tramite ricerche organiche su Google."
      }
    ],
    "ctaTitle": "Catering con margine reale e senza caos.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Catering ed Eventi: Matrimoni, Aziendali e Cocktail | AI Chef Pro",
      "description": "Suite IA per aziende di catering professionale: Catering AI+, food cost per evento, produzione su larga scala, HACCP fuori sede e proposte commerciali. Inizia oggi.",
      "keywords": "IA catering, software catering, food cost eventi, gestione catering IA, catering matrimoni IA, catering aziendale IA, eventi gastronomici software, catering Italia",
      "ogImage": "https://aichef.pro/og/use-cases/catering-eventos.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Catering dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di catering gestisci (matrimoni, aziendali, cocktail, galà), dimensione media, città e volume annuale. Ogni agente — da Catering AI+ fino al Kit Plan Finanziario — risponde adattato al tuo tipo di evento, scala e mercato reale.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Catering",
    "apps": [
      {
        "name": "Catering AI+",
        "description": "Agente principale: matrimoni, aziendali, cocktail e galà con base professionale.",
        "category": "Concetti di Business"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di menu per eventi con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Combinazioni di ingredienti e abbinamenti per cocktail e canapè.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dolci per eventi e banchetti con tecnica professionale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Per canapè d'avanguardia con fermentazioni e tecniche innovative.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Calcula Pax",
        "description": "Calcolatore di porzioni che scala le ricette a 50, 200 o 500 commensali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione degli allergeni critica in eventi con molti ospiti.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi per la produzione su scala industriale.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Articoli per attrarre aziende tramite ricerche organiche.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Descrizioni SEO per migliorare il posizionamento del sito del catering.",
        "category": "Contenuti e Social"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA per proposte e galleria web.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Per ingredienti tecnici in cocktail e canapè.",
        "category": "Fornitori Gastro"
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "velocità chiusura proposte"
      },
      {
        "value": "+5 pp",
        "label": "margine dopo food cost reale"
      },
      {
        "value": "−50 %",
        "label": "tempo in logistica"
      },
      {
        "value": "11+",
        "label": "agenti per il tuo catering"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Chiudere il menu con il cliente: mezza giornata con la calcolatrice",
        "Produzione per 200 ospiti senza scalatura precisa",
        "HACCP fuori sede improvvisato",
        "Proposte con modelli Word e foto stock",
        "Brief al team su fogli sparsi"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Chiudere il menu in 30 minuti con margine validato",
        "Produzione scalata con Calcula Pax e Sprechi GenCal",
        "HACCP con tracciabilità in trasporto e sede esterna",
        "Proposte con GastroIMG Gen+ e storytelling professionale",
        "Brief centralizzato con Kit de Tareas Catering"
      ]
    },
    "galleryTitle": "Come Funziona un Catering Professionale",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: produzione centrale, eventi eleganti, canapè, cocktail aziendali, allestimento e servizio.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-canapes.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-corporate.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-cocktail.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-setup.jpg",
      "/lovable-uploads/ai-gallery/use-case-catering-eventos-banquet.jpg"
    ]
  },
  "chef-catering": {
    "h1": "IA per Chef di Catering",
    "heroSubtitle": "Progetta menù per eventi, calcola il food cost per servizio e pianifica la produzione su larga scala con una suite di agenti IA pensati per il catering professionale e gli chef di eventi.",
    "heroTagline": "Produzione su larga scala senza perdere margine né qualità",
    "badge": "Per chef di catering ed eventi",
    "painsTitle": "Cosa un Chef di Catering Non Può Lasciare Irrisolto",
    "pains": [
      "Calcolare il food cost di menù con alta variabilità di ospiti (50, 200, 500) quando i prezzi degli ingredienti cambiano ogni settimana",
      "Pianificare produzione, mise en place e acquisti su larga scala senza sforamenti",
      "Coordinare logistica, trasporto e allestimento presso il cliente rispettando tempi e temperature",
      "Mantenere HACCP e tracciabilità fuori dalla sede fissa, in location esterne e veicoli refrigerati",
      "Progettare menù creativi per ogni tipo di evento (matrimonio, corporate, cocktail, gala) senza reinventare ogni volta",
      "Comunicare con il team di produzione, trasporto e servizio con documentazione chiara"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Chef di Catering",
    "features": [
      {
        "title": "Catering AI+",
        "description": "Agente specializzato in catering ed eventi gastronomici: matrimoni, corporate, cocktail e gala con conoscenza professionale.",
        "icon": "PartyPopper"
      },
      {
        "title": "Cucina Creativa + Food Pairing AI",
        "description": "Brainstorming per menù di evento. Cucina Creativa fornisce ricetta + food cost CSV pronto per il Kit Escandallos Pro.",
        "icon": "Sparkles"
      },
      {
        "title": "Food cost per evento",
        "description": "Kit Escandallos Pro: carichi il CSV con i tuoi prezzi reali, regoli il numero di ospiti e ottieni costo, food cost % e margine all'istante.",
        "icon": "Calculator"
      },
      {
        "title": "Calcula Pax",
        "description": "Calcolatore di porzioni che scala le ricette a 50, 200, 500 o 1000 commensali in pochi secondi.",
        "icon": "Layers"
      },
      {
        "title": "Kit di Attività Catering",
        "description": "Template specifici per produzione, trasporto, allestimento, servizio e smontaggio presso la sede del cliente.",
        "icon": "CheckSquare"
      },
      {
        "title": "HACCP fuori sede",
        "description": "Pack APPCC con template adattati a prodotto che viaggia: tracciabilità, temperatura in trasporto e registri in sede esterna.",
        "icon": "ShieldCheck"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronomica con IA per presentazioni ai clienti, proposte di evento e comunicati stampa.",
        "icon": "Image"
      },
      {
        "title": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni, critica per eventi con molti ospiti con profili alimentari diversi.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Sosa Ingredients AI",
        "description": "Assistente per la selezione di ingredienti tecnici del catalogo Sosa, particolarmente utile in cocktail e dessert.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Chef di Catering con AI Chef Pro",
    "workflow": [
      "08:30 · Catering AI+ — l'agente ti aiuta a finalizzare la proposta di menù per un matrimonio di 180 invitati secondo il briefing del cliente.",
      "09:30 · Cucina Creativa — sviluppi i 12 piatti del menù con ricetta dettagliata e food cost CSV con prezzi di riferimento.",
      "10:30 · Calcula Pax + Kit Escandallos Pro — scalì a 180 commensali, carichi il CSV con i tuoi prezzi reali e validi il margine obiettivo.",
      "12:00 · Validazione con il cliente — esporti la proposta con schede tecniche e fotografia gastronomica di GastroIMG Gen+.",
      "14:00 · Kit di Attività Catering — pianifichi produzione, trasporto, allestimento, servizio e smontaggio dell'evento di sabato.",
      "16:00 · HACCP fuori sede — prepari i registri di temperatura in trasporto e tracciabilità in sede esterna con il Pack APPCC.",
      "18:00 · ID Allergeni — generi la scheda allergeni per piatto, pronta per la sala e per gli ospiti con restrizioni.",
      "19:30 · Brief al team — prepari il brief di servizio con il team di cucina e sala dell'evento, tutto da un'unica fonte."
    ],
    "productsTitle": "Template e Kit Scaricabili per Chef di Catering",
    "productIds": [
      "kit-tareas-catering",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "I food cost per evento mi fanno risparmiare ore. Chiudo un menù per 200 invitati con margine validato in 30 minuti. Prima era mezza giornata con calcolatrice e tovaglioli. E avere l'HACCP adattato a eventi fuori sede ci ha tolto un enorme mal di testa con i clienti corporate.",
    "testimonialAuthor": "Andrea Costa",
    "testimonialRole": "Chef di Catering, specializzato in eventi corporate e matrimoni",
    "faqTitle": "Domande Frequenti dei Chef di Catering",
    "faqs": [
      {
        "q": "Va bene per qualsiasi dimensione di catering?",
        "a": "Sì. Dai catering boutique con 50 invitati al mese fino ad aziende con più di 1000 servizi mensili ed eventi con 2000 commensali."
      },
      {
        "q": "Permette di gestire la variabilità degli invitati?",
        "a": "Sì. Calcula Pax scala le ricette a qualsiasi numero di commensali e il Kit Escandallos Pro ricalcola automaticamente costo, food cost e margine."
      },
      {
        "q": "Copre l'HACCP fuori dalla sede fissa?",
        "a": "Sì. Il Pack APPCC ha template specifici per prodotto che viaggia in zaino, moto, furgone refrigerato o cucina centrale, inclusa la tracciabilità in sede esterna."
      },
      {
        "q": "Ci sono template specifici per il catering?",
        "a": "Sì. Il Kit di Attività Catering include liste dettagliate di produzione, trasporto, allestimento in sede, servizio e smontaggio, oltre a protocolli di coordinamento con la cucina centrale."
      },
      {
        "q": "Come si adatta al mio tipo di catering?",
        "a": "Inizi con l'agente «Chi sono?», un onboarding di 2 minuti in cui racconti che tipo di eventi fai (matrimoni, corporate, cocktail, gala), dimensione media, città e operatività. Tutto si adatta al tuo contesto."
      },
      {
        "q": "Serve per progettare menù innovativi?",
        "a": "Sì. Catering AI+ + Cucina Creativa + Food Pairing AI + Fermentus Con AI+ lavorano insieme per progettare menù creativi con base professionale, non ricette copiate da internet."
      }
    ],
    "ctaTitle": "Progetta, calcola il food cost e produci eventi senza fogli sparsi.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Chef di Catering: Menù, Food Cost e HACCP per Eventi | AI Chef Pro",
      "description": "Suite IA per chef di catering: Catering AI+, Cucina Creativa, Calcula Pax, food cost per evento, HACCP fuori sede e pianificazione della produzione su larga scala. Inizia oggi.",
      "keywords": "IA chef catering, software chef catering, food cost catering IA, software catering eventi, HACCP catering, menù matrimonio IA, gestione evento gastronomico IA, chef catering Italia",
      "ogImage": "https://aichef.pro/og/use-cases/chef-catering.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Tipo di Catering dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di eventi progetti (matrimoni, corporate, cocktail, gala), dimensione media, città e modo di lavorare. Da quel momento, ogni agente — da Catering AI+ ai food cost — risponde adattato al tuo contesto: tipi di servizio, scala della tua cucina centrale e operatività reale. Non è un modulo: è una breve conversazione che rende la suite davvero utile per la tua giornata da chef di catering.",
    "appsTitle": "Gli Agenti IA che Userai come Chef di Catering",
    "apps": [
      {
        "name": "Catering AI+",
        "description": "Agente principale: matrimoni, corporate, cocktail e gala con conoscenza professionale.",
        "category": "Concetti di Business"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di piatti professionali con ricetta + food cost CSV pronto per il Kit Escandallos Pro.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Combinazioni di ingredienti e abbinamenti con base scientifica.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dessert per eventi con tecnica professionale, ideali per banchetti e gala.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Per canapè all'avanguardia con fermenti, garum e tecniche innovative.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Calcula Pax",
        "description": "Calcolatore di porzioni che scala le ricette a 50, 200 o 500 commensali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per piatto, critica per eventi grandi.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi su sprechi e rese per la produzione su larga scala.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Conversor Ing",
        "description": "Convertitore di pesi e misure professionale per la produzione industriale.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Assistente per ingredienti tecnici del catalogo Sosa.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica con IA per proposte ai clienti e comunicati stampa.",
        "category": "Gastro Conoscenza"
      }
    ],
    "metrics": [
      {
        "value": "×10",
        "label": "velocità chiusura menù evento"
      },
      {
        "value": "+5 pp",
        "label": "margine dopo food cost reale"
      },
      {
        "value": "−50 %",
        "label": "tempo in pianificazione logistica"
      },
      {
        "value": "11+",
        "label": "agenti per il tuo catering"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Chiudere un menù evento con il cliente: mezza giornata con calcolatrice e tovaglioli",
        "HACCP fuori sede improvvisato, senza tracciabilità reale in trasporto",
        "Produzione per 200 invitati senza scalatura precisa, sprechi elevati",
        "Proposte ai clienti con template Word e foto stock",
        "Brief al team su fogli sparsi che si perdono"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Chiudere un menù con margine validato in 30 minuti con Catering AI+ e Kit Escandallos Pro",
        "HACCP adattato a prodotto che viaggia con registri da mobile e tracciabilità per evento",
        "Produzione scalata con Calcula Pax, sprechi controllati con Sprechi GenCal",
        "Proposte commerciali con foto GastroIMG Gen+ e schede tecniche professionali",
        "Brief centralizzato e replicabile per produzione, trasporto, allestimento e servizio"
      ]
    },
    "galleryTitle": "La Giornata di un Chef di Catering, in Immagini",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: progettazione del menù, produzione su larga scala, logistica, allestimento in sede esterna, servizio e tracciabilità.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-catering-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-production.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-loading.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-event.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-catering-temp.jpg"
    ]
  },
  "chef-cocina": {
    "h1": "IA per Chef di Cucina e Capo Cucina",
    "heroSubtitle": "Gestisci postazioni, food cost, mise en place e formazione del team con una suite di agenti IA pensati per la giornata tipo del capo cucina professionale.",
    "heroTagline": "Più cucina, meno scartoffie",
    "badge": "Per chef di cucina e capi cucina",
    "painsTitle": "Cosa un Capo Cucina Non Può Evitare di Risolvere",
    "pains": [
      "Calcolare il food cost preciso di ogni piatto e dell'intero menu con prodotti che cambiano prezzo ogni settimana",
      "Coordinare mise en place e postazioni senza intoppi nei momenti di punta del servizio",
      "Mantenere l'HACCP aggiornato senza che la burocrazia rubi tempo alla cucina",
      "Formare e supervisionare il team su tecniche e procedure standardizzate con rotazione frequente",
      "Rinnovare il menu ogni stagione mantenendo il margine e rispettando i prodotti locali",
      "Comunicare con sala, direzione e fornitori con documentazione professionale, non appunti su un quaderno"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Capo Cucina",
    "features": [
      {
        "title": "Chef Esecutivo Pro",
        "description": "Agente specializzato per supportarti nella standardizzazione di ricette, schede tecniche e manuali di cucina.",
        "icon": "ChefHat"
      },
      {
        "title": "Cucina Creativa + Food Pairing AI",
        "description": "Brainstorming per nuovi piatti con base professionale. Cucina Creativa fornisce ricetta + food cost CSV con prezzi di riferimento, pronto per il Kit de Escandallos Pro.",
        "icon": "Sparkles"
      },
      {
        "title": "Food cost professionale",
        "description": "Kit de Escandallos Pro: carichi il CSV di Cucina Creativa, sostituisci i prezzi con quelli reali e ottieni costo, food cost % e margine all'istante.",
        "icon": "Calculator"
      },
      {
        "title": "Schede tecniche professionali",
        "description": "Ricetta, procedimento, allergeni, impiattamento e storytelling in un unico documento pronto da stampare.",
        "icon": "BookOpen"
      },
      {
        "title": "Attività e mise en place",
        "description": "Kit de Tareas con modelli specifici per concetto: apertura, chiusura, postazioni e servizio.",
        "icon": "CheckSquare"
      },
      {
        "title": "HACCP e tracciabilità",
        "description": "Pack APPCC con 17 modelli: temperature, sprechi, allergeni e tracciabilità dal cellulare del team.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "R&D gastronomico: koji, kombucha, shoyu, garum e lattofermenti con supporto professionale.",
        "icon": "Beaker"
      },
      {
        "title": "Pro Prompts eBook",
        "description": "Più di 300 prompt testati per creatività, food cost, schede tecniche, formazione e operatività di cucina.",
        "icon": "GraduationCap"
      },
      {
        "title": "ID Allergeni e Sprechi GenCal",
        "description": "Rilevamento automatico degli allergeni per piatto e dati precisi su sprechi e rese per ingrediente.",
        "icon": "ShieldCheck"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Capo Cucina con AI Chef Pro",
    "workflow": [
      "08:00 · Apertura — stampi la mise en place del giorno dal Kit de Tareas e valuti gli ordini ai fornitori con il Kit Inventario.",
      "09:00 · Cucina Creativa — sviluppi un piatto fuori menu per il weekend con prodotto arrivato a buon prezzo. Ricevi ricetta + food cost CSV.",
      "10:30 · Kit de Escandallos Pro — carichi il CSV, applichi i tuoi prezzi reali e verifichi che il food cost sia al 28%.",
      "12:30 · Servizio — il team registra sprechi e temperature dal cellulare con il Pack APPCC. Tu sei in postazione, non in ufficio.",
      "15:30 · Briefing breve con la brigata per rivedere il piatto del giorno e regolare la mise.",
      "17:00 · Pro Prompts eBook — chiedi all'agente di generare la scaletta per la formazione di un nuovo cuoco che entra domani.",
      "19:30 · Servizio serale — coordini le uscite con il team supportato dalle schede tecniche centralizzate.",
      "23:30 · Chiusura — firmi l'HACCP del giorno, generi il report e lo invii al WhatsApp del proprietario in 10 minuti."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Capi Cucina",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "kit-tareas",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Il Kit de Escandallos e il Pack APPCC mi hanno tolto 5 ore di burocrazia a settimana. Ma ciò che uso di più è Cucina Creativa per i piatti fuori menu del weekend: in una mattina chiudo ricetta, food cost e scheda tecnica. Prima era una settimana intera.",
    "testimonialAuthor": "Lucía Romero",
    "testimonialRole": "Capo Cucina, ristorante mediterraneo da 70 coperti",
    "faqTitle": "Domande Frequenti dei Capi Cucina",
    "faqs": [
      {
        "q": "Devo essere esperto di Excel?",
        "a": "No. I modelli del Kit de Escandallos Pro e del Pack APPCC hanno formule precompilate, inserisci solo i dati. C'è un video tutorial di 5 minuti per iniziare."
      },
      {
        "q": "Funziona se il nostro menu cambia ogni mese o ogni stagione?",
        "a": "È il caso ideale. Cucina Creativa genera nuovi piatti con food cost in CSV, lo carichi nel Kit de Escandallos Pro con i tuoi prezzi ed esporti le schede tecniche. Quello che era una settimana di lavoro, diventa una giornata."
      },
      {
        "q": "L'IA capisce i termini professionali di cucina?",
        "a": "Sì. Cucina Creativa, Food Pairing AI, Fermentus Con AI+ e i ricettari per paese (italiana, messicana, giapponese, peruviana, ecc.) sono addestrati con conoscenza gastronomica professionale: tecniche, food cost, grammature, tagli, impiattamento e storytelling. Non sono ChatGPT generico."
      },
      {
        "q": "Come si adatta alla mia cucina specifica?",
        "a": "Inizi con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di cucina guidi, dove lavori e su che scala. Da quel momento, tutti gli agenti rispondono adattati al tuo contesto reale."
      },
      {
        "q": "Posso scaricare tutto in Excel e PDF?",
        "a": "Sì. Tutta la documentazione è esportabile e modificabile: food cost, schede tecniche, HACCP, mise en place e formazione del team."
      },
      {
        "q": "Funziona per cucine con tecniche avanzate (fermenti, sferificazioni, cotture lunghe)?",
        "a": "Sì. Fermentus Con AI+ copre la fermentazione d'avanguardia (koji, kombucha, shoyu, miso, garum, lattofermenti) e Cucina Creativa comprende tecniche come sous vide, sferificazioni, gelificazioni e cotture lunghe controllate."
      }
    ],
    "ctaTitle": "Più cucina, meno scartoffie. Recupera ore per ciò che conta.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Chef e Capo Cucina: Food Cost, Schede e HACCP | AI Chef Pro",
      "description": "Suite di IA per capi cucina professionisti: agenti specializzati, food cost, schede tecniche, mise en place e HACCP con supporto gastronomico reale. Inizia oggi.",
      "keywords": "IA chef cucina, capo cucina software, IA capo cucina, food cost cucina, schede tecniche IA, HACCP cucina, mise en place IA, agente IA gastronomico, capo cucina Italia",
      "ogImage": "https://aichef.pro/og/use-cases/chef-cocina.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Cucina dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di cucina guidi, in quale città, che tipo di menu gestisci e su che scala operi. Da quel momento, ogni agente —dal food cost alla creatività— risponde adattato al tuo contesto: prodotto locale, normative del tuo paese, dimensione della tua brigata e budget reale. Non è un modulo: è una breve conversazione che rende la suite davvero utile per la tua giornata in postazione.",
    "appsTitle": "Gli Agenti IA che Userai come Capo Cucina",
    "apps": [
      {
        "name": "Chef Esecutivo Pro",
        "description": "Standardizzazione di ricette, schede tecniche e manuali di cucina.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di piatti professionali con ricetta + food cost CSV pronto per il Kit de Escandallos Pro.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Combinazioni di ingredienti e abbinamenti con base scientifica.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "R&D gastronomico: fermentazione creativa di koji, kombucha, shoyu, miso e garum.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dessert di ristorante creativi con tecnica di pasticceria professionale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi su sprechi e rese per ingrediente.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Calcula Pax",
        "description": "Calcolatrice di porzioni che scala ricette a qualsiasi numero di commensali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Conversor Ing",
        "description": "Convertitore di pesi e misure per cucina professionale.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta e piatto.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Pasto del Personale",
        "description": "Generatore di menu per lo staff che risparmia costi e motiva il team.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Assistente con il catalogo professionale di Sosa per tecniche avanzate.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Assistente del catalogo tSpoonLab per applicazioni tecniche.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Gastro Lexicum",
        "description": "Tutor con definizioni di tecniche, processi e scienza gastronomica.",
        "category": "Gastro Conoscenza"
      }
    ],
    "metrics": [
      {
        "value": "−5 h",
        "label": "settimanali di burocrazia"
      },
      {
        "value": "×7",
        "label": "velocità di chiusura nuovo menu"
      },
      {
        "value": "+3 pp",
        "label": "margine dopo food cost reale"
      },
      {
        "value": "13+",
        "label": "agenti IA per la tua cucina"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Ricettario su quaderno e fogli sparsi, versioni diverse a seconda del cuoco",
        "Food cost manuale con calcolatrice ogni volta che cambia un prezzo",
        "HACCP su carta stampata che si accumula e nessuno controlla",
        "Rinnovare il menu richiede da 15 a 30 giorni tra brainstorming, food cost e schede",
        "Formazione del team improvvisata ogni volta che entra qualcuno di nuovo"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Ricettario centralizzato con food cost, allergeni, tecnica e storytelling",
        "Food cost automatico che ricalcola all'istante con qualsiasi cambio di prezzo",
        "HACCP da cellulare con registri e alert, pronto per l'ispezione",
        "Rinnovare il menu in 1-3 giorni con Cucina Creativa + Kit de Escandallos Pro",
        "Manuali di formazione replicabili con scaletta del Pro Prompts eBook"
      ]
    },
    "galleryTitle": "La Giornata Tipo di un Capo Cucina, in Immagini",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: brigata, mise en place, schede tecniche, uscite, magazzino e formazione del team.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-recipes.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-pass.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-cocina-storage.jpg"
    ]
  },
  "chef-ejecutivo": {
    "h1": "IA per Chef Esecutivo e Chef Aziendale",
    "heroSubtitle": "Crea ricette standardizzate, food cost precisi e manuali replicabili per 1, 5 o 25 cucine. Una suite di agenti IA gastronomici progettata per uno dei ruoli più esigenti della cucina professionale.",
    "heroTagline": "Il tuo team creativo e operativo, scalato alla velocità di una conversazione",
    "badge": "Per chef esecutivi e aziendali",
    "painsTitle": "Quello che un Chef Esecutivo non può smettere di risolvere",
    "pains": [
      "Standardizzare ricette in cucine geograficamente disperse senza che ogni locale le interpreti a modo suo",
      "Chiudere food cost precisi per ogni scheda tecnica con prodotto di stagione il cui prezzo cambia ogni settimana",
      "Rinnovare il menu ogni 6-12 settimane senza che il team anneghi nella burocrazia",
      "Mantenere aggiornati manuali di cucina e onboarding con un turnover costante del personale",
      "Innovare nel menu stagionale senza perdere il food cost obiettivo né il margine reale",
      "Riportare alla direzione con KPI chiari: redditività per piatto, produttività della brigata e sprechi"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Chef Esecutivo",
    "features": [
      {
        "title": "Chef Esecutivo Pro",
        "description": "Agente IA specializzato nel ruolo: standardizzazione multi-locale, schede tecniche, manuali di cucina e decisioni di menu basate su dati reali.",
        "icon": "ChefHat"
      },
      {
        "title": "Cucina Creativa + Food Pairing AI",
        "description": "Brainstorming di piatti per stagione, ingrediente o tecnica, con combinazioni supportate da base scientifica. Cucina Creativa fornisce inoltre la ricetta dettagliata e un food cost iniziale con prezzi di riferimento di mercato, scaricabile in CSV.",
        "icon": "Sparkles"
      },
      {
        "title": "Food cost professionali",
        "description": "Carichi il CSV di Cucina Creativa nel Kit de Escandallos Pro e sostituisci i prezzi di riferimento con quelli dei tuoi fornitori reali. Costo per porzione, food cost %, margine e prezzo suggerito all'istante. Ricalcola automaticamente quando cambi una grammatura o un costo.",
        "icon": "Calculator"
      },
      {
        "title": "Schede tecniche professionali",
        "description": "Ricetta, procedimento, allergeni, impiattamento e storytelling in un unico documento. Pronto per essere inviato a tutte le cucine del gruppo.",
        "icon": "BookOpen"
      },
      {
        "title": "Standardizzazione multi-locale",
        "description": "Stesso piatto, stessa qualità e stesso costo in 1, 5 o 25 unità. Manuali replicabili e completamente tracciabili.",
        "icon": "Layers"
      },
      {
        "title": "Fermentus Con AI+ e tecniche avanzate",
        "description": "Koji, kombucha, shoyu, garum e lattofermenti: R&D gastronomico con supporto professionale.",
        "icon": "Beaker"
      },
      {
        "title": "ID Allergeni e Sprechi GenCal",
        "description": "Rilevazione automatica degli allergeni per piatto e dati precisi su sprechi e rese per ingrediente.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Sonar Deep Research",
        "description": "Ricerca gastronomica approfondita: tendenze, tecniche emergenti, produttori e prodotti di stagione.",
        "icon": "Search"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronomica generata con IA per schede tecniche, comunicazione interna e comunicati stampa.",
        "icon": "Image"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Chef Esecutivo con AI Chef Pro",
    "workflow": [
      "Mattina, 09:00 · Cucina Creativa — brainstorming di 12 piatti per il menu autunnale a partire da prodotto di stagione locale. L'agente ti consegna ricetta dettagliata e un food cost iniziale con prezzi di riferimento di mercato, scaricabile in CSV.",
      "Mattina, 10:30 · Kit de Escandallos Pro — carichi i 12 CSV di Cucina Creativa, sostituisci i prezzi di riferimento con quelli dei tuoi fornitori reali e scarti 4 piatti che non rientrano nel tuo food cost obiettivo (28%).",
      "Mezzogiorno, 12:00 · Food Pairing AI — lavori sull'abbinamento degli 8 finalisti e valuti armonie inaspettate.",
      "Pomeriggio, 15:00 · ID Allergeni — generi la scheda allergeni per piatto, pronta per la normativa e per la sala.",
      "Pomeriggio, 16:30 · Chef Esecutivo Pro — redigi la scheda tecnica completa con procedimento, grammature, impiattamento e storytelling.",
      "Pomeriggio, 18:00 · GastroIMG Gen+ — generi le foto di ogni piatto per il manuale interno e il comunicato stampa.",
      "Pomeriggio, 18:30 · Replichi il manuale alle 5 cucine del gruppo. Ciò che un processo tradizionale chiude in 15-30 giorni, tu lo chiudi in 1-3 giornate a seconda delle dimensioni del menu."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Chef Esecutivi",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-plan-financiero",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Prima mi ci volevano tra 15 e 20 giorni per chiudere un nuovo menu tra brainstorming, prove, food cost, schede tecniche e comunicazione interna. Con AI Chef Pro lo faccio in 2 o 3 giorni a seconda delle dimensioni del menu e se si tratta di reingegnerizzazione completa o parziale. La differenza non è solo di tempo: il team riceve documentazione professionale e replicabile, non appunti manoscritti.",
    "testimonialAuthor": "Diego Saavedra",
    "testimonialRole": "Chef Esecutivo, gruppo di 5 ristoranti mediterranei",
    "faqTitle": "Domande Frequenti dei Chef Esecutivi",
    "faqs": [
      {
        "q": "Gli agenti IA di AI Chef Pro capiscono la cucina professionale o sono chatbot generici?",
        "a": "Sono agenti specializzati. Cucina Creativa, Food Pairing AI, Fermentus Con AI+ e Chef Esecutivo Pro sono addestrati con conoscenza gastronomica professionale: tecniche, food cost reale, redditività, grammature e tagli. Non sono ChatGPT generico: sono strumenti progettati per chi sa già cucinare."
      },
      {
        "q": "Posso caricare il mio ricettario esistente?",
        "a": "Sì. Il Kit de Escandallos Pro consente di caricare il tuo ricettario e applicare food cost automatizzato in pochi minuti. Puoi anche chiedere all'agente Chef Esecutivo Pro di generare schede tecniche a partire da descrizioni libere."
      },
      {
        "q": "Serve per cucina gastronomica avanzata o solo per cucina casual?",
        "a": "Per tutto lo spettro. Ci sono agenti specifici: Cucina Creativa per cucina d'autore, Pasticceria Creativa, Fermentus per l'avanguardia, VegChef per plant-based, oltre a più di 25 ricettari per paese. Casi reali in Michelin e Gambero Rosso e in gruppi casual fino a 25 unità."
      },
      {
        "q": "Come si adatta il sistema al mio modo di lavorare?",
        "a": "Inizia con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti chi sei, dove lavori, il tuo tipo di cucina e a che scala. Da quel momento, tutti gli agenti si adattano al tuo contesto: prezzi locali, normative del tuo paese, cucina del territorio e scala della tua operazione."
      },
      {
        "q": "C'è qualcosa di specifico per gruppi multi-locale e catene di ristorazione?",
        "a": "Sì. L'agente Chef Esecutivo Pro è pensato per la standardizzazione: stessa scheda tecnica, stesso food cost e stessi manuali replicati in tutte le unità. Combinato con il Kit Plan Financiero, puoi consolidare il reporting dei KPI per unità e per gruppo."
      },
      {
        "q": "C'è una libreria di prompt specifici per chef?",
        "a": "Sì. Il Pro Prompts eBook include più di 300 prompt testati per creatività, food cost, schede tecniche, formazione, comunicazione interna e operatività di cucina, organizzati per situazione d'uso."
      },
      {
        "q": "Quanto tempo ci vuole per ripagare l'abbonamento?",
        "a": "La maggior parte dei chef esecutivi riporta un ritorno già con il primo nuovo menu. Un cambio di menu tradizionale richiede tra 15 e 30 giorni tra brainstorming, prove, food cost, schede tecniche e comunicazione interna. Con AI Chef Pro e un buon flusso in Excel o Google Workspace, lo stesso processo passa a 1-3 giorni a seconda delle dimensioni del menu e se si tratta di reingegnerizzazione totale o parziale. Con 4-6 cambi di menu all'anno, recuperi tra 60 e 120 giornate di lavoro."
      }
    ],
    "ctaTitle": "Crea, calcola il food cost e replica ricette alla velocità di una conversazione.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Chef Esecutivo: Ricette, Costi e Manuali|AI Chef Pro",
      "description": "Suite di IA per chef esecutivo e aziendale: agente Chef Esecutivo Pro, food cost automatici, schede tecniche e manuali replicabili multi-locale. Inizia oggi.",
      "keywords": "IA chef esecutivo, chef esecutivo IA, software chef aziendale, agente IA gastronomico, food cost automatici, schede tecniche ristorante, ricette standardizzate multi-locale, manuali di cucina IA, food pairing IA, IA per gruppi di ristorazione, chef esecutivo Italia",
      "ogImage": "https://aichef.pro/og/use-cases/chef-ejecutivo.jpg"
    },
    "personalizationTitle": "Personalizzato per Te dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con un onboarding conversazionale di 2 minuti —l'agente «Chi sono?»— in cui gli racconti chi sei, dove lavori, che tipo di cucina guidi e a che scala operi. Da quel momento, ogni agente —dal food cost alla creatività— risponde adattato al tuo contesto: la tua cucina locale, le tue normative, i tuoi prezzi di mercato e la dimensione della tua brigata. Non è un modulo: è una breve conversazione che dà senso a tutto ciò che viene dopo.",
    "appsTitle": "Gli Agenti IA che Userai come Chef Esecutivo",
    "apps": [
      {
        "name": "Chef Esecutivo Pro",
        "description": "Agente principale: standardizzazione multi-locale, schede tecniche e decisioni di menu.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di piatti professionali con ricetta dettagliata e food cost iniziale scaricabile in CSV (prezzi di riferimento di mercato), pronto per essere caricato nel Kit de Escandallos Pro.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Combinazioni di ingredienti e abbinamenti con base scientifica.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Fermentazione creativa: koji, kombucha, shoyu, miso, garum e lattofermenti.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi su sprechi e rese per ingrediente. Essenziale per un food cost realistico.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Calcula Pax",
        "description": "Calcolatrice di porzioni che scala ricette a qualsiasi numero di commensali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica di allergeni potenziali per ricetta e per piatto.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dolci da ristorante creativi con tecnica di pasticceria professionale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Assistente di selezione e tecnica con il catalogo professionale di Sosa.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Assistente del catalogo tSpoonLab per tecniche e applicazioni avanzate.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca approfondita: tendenze, produttori e tecniche emergenti.",
        "category": "Modelli IA + LLM"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica generata con IA per schede tecniche e stampa.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Gastro Lexicum",
        "description": "Tutor con definizioni di tecniche, processi, additivi e scienza gastronomica.",
        "category": "Gastro Conoscenza"
      }
    ],
    "metrics": [
      {
        "value": "−90 %",
        "label": "tempo per chiudere un nuovo menu"
      },
      {
        "value": "×10",
        "label": "velocità delle schede tecniche"
      },
      {
        "value": "+4 pp",
        "label": "margine per un food cost migliore"
      },
      {
        "value": "13+",
        "label": "agenti IA per il tuo ruolo"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Chiusura di un nuovo menu: tra 15 e 30 giorni, a seconda della standardizzazione del processo",
        "Ricettario in fogli sparsi, documenti Word disordinati e appunti manoscritti",
        "Ogni locale interpreta la ricetta a modo suo e il risultato varia",
        "Food cost manuale con calcolatrice: cambi una grammatura e riscrivi tutto",
        "Manuali e onboarding costantemente obsoleti"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Chiusura di un nuovo menu: tra 1 e 3 giorni a seconda delle dimensioni e se si tratta di reingegnerizzazione totale o parziale",
        "Ricettario centralizzato con food cost, allergeni, tecnica e storytelling",
        "Stesso piatto, stessa qualità e stesso costo in 1, 5 o 25 cucine",
        "Food cost professionale che ricalcola all'istante con qualsiasi modifica",
        "Manuali aggiornati con un clic e onboarding pronto per nuovi chef"
      ]
    },
    "appUrlPath": "/agents/chef-ejecutivo-pro",
    "galleryTitle": "La Giornata Tipo di un Chef Esecutivo, in Immagini",
    "gallerySubtitle": "Cosa potrai gestire con AI Chef Pro: brigata, schede tecniche, creatività, food cost e comunicazione interna.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-recipes.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-brigade.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-creativity.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-ejecutivo-meeting.jpg"
    ]
  },
  "chef-privado-personal": {
    "h1": "IA per Chef Privato e Personal Chef",
    "heroSubtitle": "Progetta menu personalizzati per clienti unici, calcola il food cost di ogni cena privata con costi reali, pianifica la mise en place in case private e crea un branding professionale con una suite di agenti IA gastronomici specializzati in chef privato e servizio in case private.",
    "heroTagline": "Servizio privato con margine reale e tecnica d'autore",
    "badge": "Per chef privati, personal chef e catering intimo",
    "painsTitle": "Cosa un Chef Privato Non Può Evitare di Risolvere",
    "pains": [
      "Progettare menu totalmente personalizzati per ogni cliente: allergie, intolleranze, preferenze, dieta, occasione ed estetica dell'impiattamento",
      "Calcolare il food cost di ogni cena privata con costi reali (acquisto del giorno, ingredienti premium) e prezzo personalizzato",
      "Pianificare la mise en place in case private con cucine non professionali (senza attrezzature, spazio limitato, fornelli sconosciuti)",
      "Standardizzare le schede tecniche affinché il cliente possa ripetere il menu o conservare la ricetta come ricordo",
      "Differenziarsi in una zona competitiva con storytelling personale, branding visuale d'autore e acquisizione tramite social",
      "Attrarre clienti premium ricorrenti (famiglie VIP, dirigenti, celebrità) con proposte professionali e personalizzate"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Chef Privato",
    "features": [
      {
        "title": "Chef Privato Pro",
        "description": "Agente specializzato del catalogo Gastro Profile Pro: ragiona come un personal chef professionista con esperienza in case private ed eventi intimi.",
        "icon": "ChefHat"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per lo sviluppo di menu personalizzati con tecnica avanzata: impiattamenti d'autore, fusioni controllate, dessert signature.",
        "icon": "Sparkles"
      },
      {
        "title": "Food Pairing AI",
        "description": "Abbinamenti personalizzati con la cantina del cliente o proposte di vini per ogni piatto del menu privato.",
        "icon": "Wine"
      },
      {
        "title": "Calcula Pax + Schede Tecniche",
        "description": "Calcula Pax scala le ricette a 2, 6, 12 commensali; il Kit Escandallos Pro lo gestisce con costo reale per cena privata e prezzo personalizzato.",
        "icon": "Calculator"
      },
      {
        "title": "Kit di Attività per Chef Privato",
        "description": "Modelli: pre-visita alla cucina del cliente, lista della spesa, mise trasportabile, piano di servizio, pulizia, fattura.",
        "icon": "CheckSquare"
      },
      {
        "title": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per cliente: fondamentale quando lavori con famiglie con intolleranze specifiche.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione di menu stagionali e per date speciali: Natale, San Valentino, anniversari, compleanni.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia premium IA di riferimento + Instagram per attrarre nuovi clienti e costruire una reputazione d'autore.",
        "icon": "Image"
      },
      {
        "title": "Scheda tecnica + fattura",
        "description": "Modello professionale da consegnare al cliente: scheda tecnica del menu con ricetta + storytelling + fattura chiara.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Chef Privato con AI Chef Pro",
    "workflow": [
      "07:00 · Pre-visita — checklist Kit di Attività Chef Privato: revisione della cucina del cliente (attrezzature, spazio, allergie e preferenze confermate).",
      "08:00 · Chef Privato Pro — sviluppi il menu personalizzato per una cena intima di 6 pax con allergia alla frutta secca. Cucina Creativa consegna ricetta + food cost CSV.",
      "09:00 · Calcula Pax — ridimensioni le ricette da 6 a 8 commensali (il cliente ha aggiunto due ospiti). Kit Escandallos Pro ricalcola il costo e la proposta.",
      "10:00 · Lista della spesa — vai al mercato con la lista prioritaria: prodotto del giorno, ingredienti premium specifici.",
      "14:00 · Arrivo a casa del cliente — allestimento della mise en place in cucina privata seguendo il piano trasportabile, organizzazione dello spazio.",
      "17:00 · Servizio cena — esecuzione del menu con tecnica professionale adattata alla cucina del cliente, impiattamento su porcellana fine.",
      "21:00 · Chiusura con il cliente — consegna della scheda tecnica del menu con storytelling + fattura professionale + foto di riferimento del menu.",
      "23:00 · Post-cena — InstaFlow AI Pro: post su Instagram con l'immagine di riferimento del menu (senza volti del cliente) per costruire reputazione."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Chef Privato",
    "productIds": [
      "kit-tareas-chef-privado",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Chef Privato Pro mi ha cambiato la proposta commerciale. Ora ogni cliente riceve un menu personalizzato con food cost professionale e storytelling, e l'acquisizione tramite Instagram con GastroIMG Gen+ è aumentata. Chiudo proposte in una chiamata perché consegno scheda tecnica + fattura lo stesso giorno. Abbiamo alzato lo scontrino medio del 35% per cena.",
    "testimonialAuthor": "Andrea Gómez",
    "testimonialRole": "Chef privata freelance, Madrid + costa",
    "faqTitle": "Domande Frequenti degli Chef Privati",
    "faqs": [
      {
        "q": "Funziona per chef privato freelance, agenzia di personal chef o catering intimo?",
        "a": "Per tutti e tre. Chef Privato Pro ragiona come un personal chef professionista, adatto sia per il freelance che progetta la sua proposta sia per agenzie con più chef."
      },
      {
        "q": "Come gestisco allergie e diete speciali per cliente?",
        "a": "ID Allergeni identifica automaticamente gli allergeni per ricetta. Chef Privato Pro ragiona in ottica di personalizzazione: diete keto, vegana, senza glutine, a basso contenuto di sodio, FODMAP, gravidanza. Ogni cliente riceve un menu realmente adattato."
      },
      {
        "q": "Come scalare le ricette per diversi numeri di commensali?",
        "a": "Calcula Pax scala le ricette a 2, 6, 12 o qualsiasi numero di commensali senza perdere precisione. Kit Escandallos Pro ricalcola il costo per persona e la proposta economica al cliente."
      },
      {
        "q": "Genera contenuti visivi per Instagram e reputazione d'autore?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali del menu (senza mostrare il cliente) per Instagram, web e portfolio. Ricorda che l'immagine IA è un riferimento visivo: la foto definitiva la fai tu con il tuo piatto impiattato reale in ogni cena."
      },
      {
        "q": "Come mi aiuta con l'acquisizione di clienti ricorrenti?",
        "a": "GastroIMG Gen+ + InstaFlow AI Pro costruiscono contenuti visivi costanti; MenuDish Local SEO cattura clienti locali che cercano \"chef privato a [città]\"; Gastro Calendar aiuta a proporre menu stagionali (Natale intimo, San Valentino, anniversari) per fidelizzare."
      }
    ],
    "ctaTitle": "Il tuo servizio di chef privato con margine reale e proposta d'autore.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Chef Privato e Personal Chef: Menu, Food Cost e Servizio | AI Chef Pro",
      "description": "Suite IA per chef privati professionisti: Chef Privato Pro, food cost per cena, menu personalizzati, branding e acquisizione. Inizia oggi.",
      "keywords": "IA chef privato, IA personal chef, software chef privato, food cost cena privata, chef privato milano, personal chef freelance",
      "ogImage": "https://aichef.pro/og/use-cases/chef-privado.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Servizio di Chef Privato dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di servizio offri (chef privato freelance, agenzia con più chef, catering intimo per matrimoni ed eventi privati, chef su yacht), tipo di clientela (famiglie VIP, dirigenti, celebrità), città e specialità. Ogni agente — da Chef Privato Pro a Gastro Calendar — risponde adattato alla tua proposta e alla tua operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai come Chef Privato",
    "apps": [
      {
        "name": "Chef Privato Pro",
        "description": "Agente specializzato del catalogo Gastro Profile Pro: ragiona come un personal chef professionista.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di menu personalizzati con tecnica avanzata e ricetta + food cost CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti personalizzati con la cantina del cliente o proposte di vini.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Calcula Pax",
        "description": "Ridimensionamento delle ricette per diversi numeri di commensali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per cliente e ricetta.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Conversor Ing",
        "description": "Convertitore di pesi e misure, fondamentale quando si lavora con cucine non professionali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Calo peso e sprechi nell'acquisto del giorno e con ingredienti premium.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia premium IA di riferimento per Instagram, portfolio e acquisizione.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale professionale per attrarre clienti ricorrenti.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Attrarre clienti locali che cercano \"chef privato a [città]\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Menu stagionali: Natale intimo, San Valentino, anniversari, compleanni.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Per cocktail personalizzati nelle cene private.",
        "category": "Concetti di Business"
      }
    ],
    "metrics": [
      {
        "value": "+35 %",
        "label": "scontrino medio per cena privata"
      },
      {
        "value": "×3",
        "label": "acquisizione clienti via Instagram"
      },
      {
        "value": "×5",
        "label": "velocità di proposte commerciali"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo servizio privato"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Menu personalizzati a mano: una settimana per proposta",
        "Food cost senza costi reali, proposte commerciali con margine incerto",
        "Pre-visita e mise en place improvvisata ogni volta",
        "Acquisizione tramite passaparola, senza Instagram costante",
        "Nessuna scheda tecnica consegnabile al cliente come ricordo"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Menu personalizzato in un'ora con Chef Privato Pro",
        "Food cost professionale per cena con margine validato",
        "Pre-visita e mise con modello trasportabile Kit di Attività",
        "Acquisizione costante con GastroIMG Gen+ + InstaFlow AI Pro",
        "Scheda tecnica del menu + fattura consegnata lo stesso giorno"
      ]
    },
    "galleryTitle": "Come Funziona il Servizio di Chef Privato",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: mise en place, piatto impiattato, tavola apparecchiata, dispensa e servizio. Immagini generate con IA come riferimento visivo del concept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chef-privado-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-plato.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-mesa.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-despensa.jpg",
      "/lovable-uploads/ai-gallery/use-case-chef-privado-team.jpg"
    ]
  },
  "chocolateria": {
    "h1": "IA per Cioccolateria e Bomboneria",
    "heroSubtitle": "Food cost per cioccolatino con costo reale del cacao e costo orario del laboratorio, pianifica la produzione stagionale e cattura branding professionale con una suite di agenti IA specializzati in cioccolateria artigianale.",
    "heroTagline": "Cioccolatino con margine reale e senza scartoffie",
    "badge": "Per cioccolaterie e bombonerie artigianali",
    "painsTitle": "Cosa una Cioccolateria Non Può Non Risolvere",
    "pains": [
      "Cacao con prezzo volatile che cambia il costo reale ogni settimana senza preavviso e obbliga a ricalcolare i food cost costantemente",
      "Scarti in laboratorio (temperaggio fallito, stampi non ben solidificati, ritagli) e in vetrina (rotazione, esposizione prolungata)",
      "Stagionalità estrema: Natale, San Valentino, Pasqua, Epifania concentrano una percentuale elevata del fatturato annuale",
      "Tracciabilità HACCP con prodotto delicato: cacao, latticini, frutta secca, alcolici e temperature critiche in ogni passaggio",
      "Differenziarsi in zona competitiva con cioccolatini d'autore, packaging premium e storytelling visivo del marchio",
      "Catturare ordini corporate e matrimoni con margine mentre si gestisce la cioccolateria quotidiana"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta nella Cioccolateria",
    "features": [
      {
        "title": "Cioccolateria Creativa",
        "description": "Agente specializzato in cioccolateria professionale: cioccolatini, ganache, praline, tavolette, coperture e tecnica di temperaggio.",
        "icon": "Cookie"
      },
      {
        "title": "Pasticceria Creativa",
        "description": "Per dessert al cioccolato, bocconcini, brownies e combinazioni avanzate cioccolato + pasticceria che diversificano il catalogo.",
        "icon": "Cake"
      },
      {
        "title": "Food cost per pezzo con costo orario laboratorio",
        "description": "Cioccolateria Creativa consegna ricetta + food cost CSV; Kit Escandallos Pro lo gestisce con costo orario laboratorio integrato nel margine reale per cioccolatino e per scatola.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Chocolatería",
        "description": "Modelli: temperaggio, stampaggio, farcitura con ganache, assemblaggio, packaging, controllo temperature in cella.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC Cioccolateria",
        "description": "Tracciabilità di cacao, latticini, frutta secca, alcolici e conservazione professionale con curve di temperaggio documentate.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione stagionale con date chiave: Natale, San Valentino, Pasqua, Epifania, Festa della Mamma. Calendario editoriale per vetrina.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Fotografia gastronomica IA + Pinterest, dove la cioccolateria premium cattura traffico organico stabile.",
        "icon": "Image"
      },
      {
        "title": "Sosa Ingredients AI",
        "description": "Assistente del catalogo Sosa per coperture tecniche, paste concentrate, frutta secca e aromi professionali.",
        "icon": "BarChart3"
      },
      {
        "title": "Sprechi GenCal",
        "description": "Dati precisi di scarti per processo (temperaggio, stampaggio, ritagli, esposizione vetrina) integrati nel food cost.",
        "icon": "Sparkles"
      }
    ],
    "workflowTitle": "Una Giornata Reale in una Cioccolateria con AI Chef Pro",
    "workflow": [
      "07:00 · Apertura — checklist Kit de Tareas Chocolatería: revisione cella, pre-cristallizzazione del cioccolato di copertura, preparazione stampi.",
      "08:30 · Cioccolateria Creativa — sviluppi un nuovo cioccolatino per San Valentino con ganache al lampone e vaniglia. Cucina Creativa consegna ricetta + food cost CSV.",
      "09:30 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali del cacao e costo orario laboratorio integrato, validi il margine per cioccolatino e per scatola da 12.",
      "11:00 · Produzione del giorno — temperaggio su marmo, stampaggio, farcitura con ganache con sac à poche, abbattimento e sformatura.",
      "14:00 · Rifornimento vetrina con scatole professionali ed etichette, controllo scarti di esposizione.",
      "16:00 · Gastro Calendar — prepari la pianificazione della produzione di Natale (scatole regalo corporate con 8 settimane di anticipo).",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — generi fotografie di riferimento del nuovo cioccolatino e pin ottimizzati per Pinterest.",
      "20:00 · Chiusura — pulizia profonda, HACCP firmato, pianificazione miscele per abbattere stasera."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Cioccolateria",
    "productIds": [
      "kit-tareas-chocolateria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Produrre 12.000 cioccolatini per Natale senza sistema era caos. Con Cioccolateria Creativa per il design, Kit Escandallos Pro per il margine reale con cacao aggiornato e Gastro Calendar per la pianificazione stagionale, abbiamo salvato la stagione e aumentato il margine di 7 punti. Le scatole corporate ora si chiudono in una chiamata con proposta professionale.",
    "testimonialAuthor": "Mónica Salazar",
    "testimonialRole": "Maestra cioccolatiera e proprietaria",
    "faqTitle": "Domande Frequenti delle Cioccolaterie",
    "faqs": [
      {
        "q": "Serve per cioccolateria artigianale piccola o catena?",
        "a": "Per entrambe. I modelli scalano da laboratorio familiare di 2 persone fino a produzione per più punti vendita. La metodologia è la stessa: ricetta → food cost CSV → margine reale con costo orario laboratorio."
      },
      {
        "q": "Copre bomboneria, tavolette, coperture e praline?",
        "a": "Sì. Cioccolateria Creativa ragiona come un cioccolatiere professionale: temperaggio della copertura per curve, ganache con bilanciamento acqua e grassi, praline con tostatura della frutta secca, tavolette farcite con tecnica di cristallizzazione."
      },
      {
        "q": "Come gestiamo il prezzo volatile del cacao?",
        "a": "Kit Escandallos Pro ricalcola all'istante il margine reale quando aggiorni il prezzo della copertura. Sprechi GenCal aggiunge il costo degli scarti per processo. Così il margine riflette sempre il costo attuale, non quello di tre mesi fa."
      },
      {
        "q": "Genera contenuti per vetrina, social e packaging?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali di ogni cioccolatino per vetrina, web e social; Pinterest Pins Gen + InstaFlow AI Pro programmano contenuti visivi; MenuDish Local SEO cattura clienti locali. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo cioccolatino impiattato reale."
      },
      {
        "q": "Come mi aiuta con la forte stagionalità?",
        "a": "Gastro Calendar pianifica le stagioni chiave (Natale, San Valentino, Pasqua, Epifania, Festa della Mamma) con 8-12 settimane di anticipo. Il Kit Plan Financiero proietta il cash flow stagionale realistico per arrivare con produzione e cassa a ogni picco."
      }
    ],
    "ctaTitle": "La tua cioccolateria con margine chiaro e branding professionale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Cioccolateria: Food Cost e Branding | AI Chef Pro",
      "description": "Suite di IA per cioccolaterie artigianali: Cioccolateria Creativa, food cost, HACCP, pianificazione stagionale e branding. Inizia oggi.",
      "keywords": "IA cioccolateria, software cioccolateria, food cost cioccolatino, cioccolateria artigianale IA, tecnica temperaggio, bomboneria Italia, pianificazione Natale cioccolateria",
      "ogImage": "https://aichef.pro/og/use-cases/chocolateria.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Cioccolateria dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di cioccolateria gestisci (artigianale, bomboneria d'autore, cioccolateria con caffetteria, laboratorio per vendita all'ospitalità), dimensione del team, città e specialità. Ogni agente —da Cioccolateria Creativa a Gastro Calendar— risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nella Tua Cioccolateria",
    "apps": [
      {
        "name": "Cioccolateria Creativa",
        "description": "Agente specializzato in cioccolateria professionale: cioccolatini, ganache, praline, tavolette e tecnica di temperaggio.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dessert al cioccolato, bocconcini, brownies e combinazioni avanzate.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di nuovi pezzi con ricetta + food cost CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa: coperture tecniche, paste concentrate, frutta secca e aromi professionali.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Assistente del catalogo tSpoonLab per applicazioni avanzate di cioccolateria.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Scarti per processo (temperaggio, stampaggio, ritagli, esposizione vetrina) nel food cost.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per cioccolatino: latticini, frutta secca, glutine, alcolici.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA di riferimento per vetrina, web, packaging e social.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico stabile per cioccolateria premium.",
        "category": "Contenuti e Social"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale per cioccolateria d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"cioccolateria artigianale vicino\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Pianificazione stagionale: Natale, San Valentino, Pasqua, Epifania, Festa della Mamma.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "margine dopo il food cost dei cioccolatini"
      },
      {
        "value": "−35 %",
        "label": "scarti in laboratorio e vetrina"
      },
      {
        "value": "×2",
        "label": "ordini corporate Natale"
      },
      {
        "value": "12+",
        "label": "agenti per la tua cioccolateria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Food cost senza costo orario laboratorio, cioccolatini complessi in perdita senza saperlo",
        "Cacao volatile che sballa i prezzi senza ricalcolare in tempo reale",
        "Scarti in temperaggio, stampaggio e vetrina senza tracciabilità reale",
        "Produzione stagionale reattiva: arrivi tardi a Natale e perdi ordini corporate",
        "HACCP su carta stampata sparsa per il laboratorio"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Food cost professionale per cioccolatino con costo orario laboratorio integrato e cacao aggiornabile",
        "Scarti controllati con Sprechi GenCal e modelli specifici di cioccolateria",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ catturano traffico stabile e ordini",
        "Gastro Calendar pianifica Natale e San Valentino con 8-12 settimane di anticipo",
        "HACCP da mobile con registri pronti per ispezione"
      ]
    },
    "galleryTitle": "Come Funziona una Cioccolateria Artigianale",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: vetrina, laboratorio, temperaggio, cioccolatini, esposizione e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chocolateria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-obrador.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-bonbons.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-temperado.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-display.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolateria-team.jpg"
    ]
  },
  "chocolatero": {
    "h1": "IA per Cioccolatiere e Bomboniere",
    "heroSubtitle": "Progetta praline, tavolette e coperture con food cost professionale, tecnica di temperaggio e pianificazione stagionale con una suite di agenti IA specializzati in cioccolateria artigianale d'autore.",
    "heroTagline": "Cioccolateria con tecnica autentica e margine reale",
    "badge": "Per cioccolatieri, bombonieri e maestri cioccolatieri",
    "painsTitle": "Ciò che un Cioccolatiere Non Può Non Risolvere",
    "pains": [
      "Cacao con prezzo volatile che cambia il costo reale ogni settimana senza preavviso e obbliga a ricalcolare i food cost costantemente",
      "Tecnica di temperaggio esigente: cristallizzazione in forma V, curve precise secondo copertura, brillantezza e snap consistenti",
      "Sprechi in laboratorio (temperaggio fallito, ritagli, stampi non ben formati, abbattimento) che erodono la redditività senza controllo",
      "Stagionalità estrema: Natale, San Valentino, Pasqua e Roscón concentrano un'alta percentuale del fatturato annuale",
      "Differenziarsi in zona competitiva con praline d'autore, packaging premium e storytelling visivo del marchio",
      "Catturare ordini corporate, matrimoni ed eventi con margine mentre si gestisce la produzione quotidiana"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Cioccolatiere",
    "features": [
      {
        "title": "Cioccolateria Creativa",
        "description": "Agente specializzato in cioccolateria professionale: praline, ganache, pralinati, tavolette, coperture, tecnica di temperaggio e curve di cristallizzazione.",
        "icon": "Cookie"
      },
      {
        "title": "Pasticceria Creativa",
        "description": "Per dessert al cioccolato, bocconcini, brownies, mousse e combinazioni avanzate cioccolato + pasticceria.",
        "icon": "Cake"
      },
      {
        "title": "Food cost per pezzo con costo ora laboratorio",
        "description": "Cucina Creativa fornisce ricetta + food cost CSV; Kit de Escandallos Pro lo gestisce con costo ora laboratorio integrato nel margine reale per pralina e per scatola.",
        "icon": "Calculator"
      },
      {
        "title": "Sosa Ingredients AI",
        "description": "Assistente del catalogo Sosa per coperture tecniche, paste concentrate, frutta secca e aromi professionali.",
        "icon": "Beaker"
      },
      {
        "title": "Kit di Attività Cioccolateria",
        "description": "Modelli: temperaggio, stampaggio, ganache, assemblaggio, packaging, controllo temperature in cella.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC cioccolateria",
        "description": "Tracciabilità di cacao, latticini, frutta secca, alcolici e conservazione professionale con curve documentate.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione stagionale con date chiave: Natale, San Valentino, Pasqua, Roscón, Festa della Mamma. Calendario editoriale.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Fotografia d'autore IA di riferimento + Pinterest, dove la cioccolateria premium cattura traffico organico stabile.",
        "icon": "Image"
      },
      {
        "title": "Sprechi GenCal",
        "description": "Dati precisi sugli sprechi per processo (temperaggio, stampaggio, ritagli, esposizione) integrati nel food cost.",
        "icon": "Sparkles"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Cioccolatiere con AI Chef Pro",
    "workflow": [
      "07:00 · Apertura — checklist Kit di Attività Cioccolateria: revisione cella, pre-cristallizzazione copertura, preparazione stampi in policarbonato.",
      "08:30 · Cioccolateria Creativa — sviluppi una nuova pralina signature con pralinato di nocciola caramellata e sale Maldon. Cucina Creativa fornisce ricetta + food cost CSV.",
      "09:30 · Sosa Ingredients AI — selezioni copertura tecnica con percentuale di cacao adeguata, burro di cacao aggiuntivo e sale di qualità.",
      "10:00 · Kit de Escandallos Pro — carichi il CSV con i tuoi prezzi reali del cacao e costo ora laboratorio integrato, validi il margine per pralina e per scatola da 9 pezzi.",
      "11:00 · Produzione del giorno — temperaggio su marmo, stampaggio, ganache, riempimento, abbattimento e sformatura.",
      "14:00 · Rifornimento — preparazione di scatole regalo professionali, etichettatura e controllo sprechi.",
      "16:00 · Gastro Calendar — prepari la pianificazione di Natale con scatole corporate (anticipo 8 settimane).",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — generi immagine di riferimento del nuovo signature e pin ottimizzati per Pinterest.",
      "20:00 · Chiusura — pulizia profonda, HACCP firmato, pianificazione miscele da abbattere."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Cioccolateria",
    "productIds": [
      "kit-tareas-chocolateria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Produrre 12.000 praline per Natale senza sistema era caos. Con Cioccolateria Creativa per il design, Sosa Ingredients AI per la copertura tecnica, Kit de Escandallos Pro per il margine reale con cacao aggiornato e Gastro Calendar per la pianificazione stagionale, abbiamo salvato la stagione e aumentato il margine di 7 punti. Le scatole corporate si chiudono in una chiamata con proposta professionale.",
    "testimonialAuthor": "Mónica Salazar",
    "testimonialRole": "Maestra cioccolatiera e proprietaria",
    "faqTitle": "Domande Frequenti dei Cioccolatieri",
    "faqs": [
      {
        "q": "Copre la tecnica di temperaggio professionale e le curve di cristallizzazione?",
        "a": "Sì. Cioccolateria Creativa ragiona come un cioccolatiere professionale: temperaggio della copertura per curve (45-27-31 °C per copertura fondente), tecnica di tabling su marmo, semina, microonde con burro di cacao aggiuntivo. Non ricette da YouTube."
      },
      {
        "q": "Serve per cioccolateria artigianale piccola, atelier d'autore o bomboneria con produzione su scala?",
        "a": "Per tutte e tre. I modelli scalano da laboratorio familiare fino a produzione per più punti vendita o scatole corporate con centinaia di unità."
      },
      {
        "q": "Come gestiamo il prezzo volatile del cacao?",
        "a": "Kit de Escandallos Pro ricalcola all'istante il margine reale quando aggiorni il prezzo della copertura. Sprechi GenCal aggiunge il costo degli sprechi per processo. Il margine riflette sempre il costo attuale."
      },
      {
        "q": "Genera contenuti per vetrina, social e packaging?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali di ogni pralina per vetrina, web e social; Pinterest Pins Gen + InstaFlow AI Pro programmano contenuti visivi; MenuDish Local SEO cattura clienti locali. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con la tua pralina impiattata reale."
      },
      {
        "q": "Come mi aiuta con la forte stagionalità?",
        "a": "Gastro Calendar pianifica le stagioni chiave (Natale, San Valentino, Pasqua, Roscón, Festa della Mamma) con anticipo di 8-12 settimane. Il Kit Plan Financiero proietta il cash flow stagionale realistico per arrivare con produzione e cassa a ogni picco."
      }
    ],
    "ctaTitle": "La tua cioccolateria con margine chiaro e tecnica d'autore.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Cioccolatiere e Bomboniere: Temperaggio, Food Cost e Stagionalità | AI Chef Pro",
      "description": "Suite di IA per cioccolatieri professionisti: Cioccolateria Creativa, food cost per pezzo con costo ora laboratorio, pianificazione stagionale e HACCP. Inizia oggi.",
      "keywords": "IA cioccolatiere, IA bomboniere, software cioccolateria, food cost praline, cioccolateria artigianale IA, tecnica temperaggio, curve cristallizzazione, maestro cioccolatiere",
      "ogImage": "https://aichef.pro/og/use-cases/chocolatero.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Atelier dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di cioccolateria gestisci (atelier d'autore, bomboneria con produzione su scala, cioccolateria con caffetteria, laboratorio per vendita all'ospitalità, cioccolateria con esperienze e degustazioni), dimensione del team, città e specialità. Ogni agente —da Cioccolateria Creativa a Gastro Calendar— risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Atelier",
    "apps": [
      {
        "name": "Cioccolateria Creativa",
        "description": "Agente specializzato in cioccolateria professionale: praline, ganache, pralinati, tavolette e tecnica di temperaggio.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dessert al cioccolato, bocconcini, brownies, mousse e combinazioni avanzate.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di praline signature con ricetta + food cost CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa: coperture tecniche, paste concentrate, frutta secca e aromi professionali.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Assistente del catalogo tSpoonLab per applicazioni avanzate di cioccolateria.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi in temperaggio, stampaggio, ritagli ed esposizione integrati nel food cost.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per pralina: latticini, frutta secca, glutine, alcolici.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia d'autore IA di riferimento per vetrina, web, packaging e social.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico stabile per cioccolateria premium.",
        "category": "Contenuti e Social"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale per cioccolateria d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"cioccolateria artigianale vicino\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Pianificazione stagionale: Natale, San Valentino, Pasqua, Roscón, Festa della Mamma.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "margine dopo il food cost delle praline"
      },
      {
        "value": "−35 %",
        "label": "sprechi in laboratorio e vetrina"
      },
      {
        "value": "×2",
        "label": "ordini corporate Natale"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo atelier"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Temperaggio improvvisato: brillantezza e snap inconsistenti pezzo per pezzo",
        "Cacao volatile che sballa i prezzi senza ricalcolare in tempo reale",
        "Sprechi in temperaggio, stampaggio e vetrina senza tracciabilità reale",
        "Produzione stagionale reattiva: arrivi tardi a Natale e perdi ordini corporate",
        "HACCP su carta stampata sparsa per l'atelier"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Temperaggio per curve con criterio tecnico, brillantezza e snap consistenti",
        "Food cost professionale per pralina con cacao aggiornabile e costo ora integrato",
        "Sprechi controllati con Sprechi GenCal e modelli specifici",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ catturano traffico stabile e ordini",
        "HACCP da mobile con registri pronti per ispezione"
      ]
    },
    "galleryTitle": "Come Funziona un Atelier di Cioccolateria",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: temperaggio, stampaggio, praline, ganache e attrezzatura. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-chocolatero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-temperado.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-bombones.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-moldeado.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-ganache.jpg",
      "/lovable-uploads/ai-gallery/use-case-chocolatero-team.jpg"
    ]
  },
  "coffee-shop-specialty": {
    "h1": "IA per Coffee Shop e Specialty Coffee",
    "heroSubtitle": "Progetta la carta di caffè specialty con criterio third-wave, scheda tecnica per bevanda con costo reale, pianifica la produzione di pasticceria propria e cattura branding minimalista con una suite di agenti IA gastronomici specializzati in specialty coffee professionale.",
    "heroTagline": "Caffè specialty con margine reale e tecnica third-wave",
    "badge": "Per coffee shop, specialty café e third-wave coffee",
    "painsTitle": "Quello che un Coffee Shop non può non risolvere",
    "pains": [
      "Curare la carta di caffè specialty con criterio: single origin, blend, metodi (espresso, V60, Aeropress, Chemex)",
      "Fare la scheda tecnica di ogni bevanda con costo reale (grammatura, latte premium, alternative vegetali) e food cost coerente",
      "Sprechi nel caffè macinato (degradazione rapida), latte e prodotto fresco di pasticceria",
      "Standardizzare la tecnica del barista turno dopo turno: estrazione, latte art, dosaggio, calibrazione",
      "Differenziarsi in una zona competitiva con caffè di origine tracciata, branding visivo minimalista e formazione costante",
      "Catturare clienti locali ricorrenti e vendere grani per casa con margine alto"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Coffee Shop",
    "features": [
      {
        "title": "Cucina Creativa",
        "description": "Per lo sviluppo di signature: cold brew infusionati, latte con sciroppo fatto in casa, specialità stagionali.",
        "icon": "Coffee"
      },
      {
        "title": "Pasticceria Creativa",
        "description": "Per la pasticceria propria che differenzia il coffee shop: croissant, brownies, cookie, banana bread, torta del giorno.",
        "icon": "Cake"
      },
      {
        "title": "Scheda tecnica per bevanda",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica CSV; Kit de Escandallos Pro lo gestisce con costo reale per caffè e latte, food cost % validato.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Caffetteria / Brunch",
        "description": "Template: preparazione banco, calibrazione espresso, preparazione alternative vegetali, mise en place pasticceria, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC caffetteria",
        "description": "Tracciabilità di caffè macinato, latte, alternative vegetali e pasticceria propria.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Lanci stagionali: pumpkin spice latte (autunno), cold brew (estate), caffè speziato Natale.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia minimalista IA di riferimento + Instagram: lo specialty coffee vive dell'impatto visivo del latte art.",
        "icon": "Image"
      },
      {
        "title": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"specialty coffee vicino\" su Google e Maps.",
        "icon": "BarChart3"
      },
      {
        "title": "BlogPost SEO Gen+",
        "description": "Articoli SEO sull'origine del caffè, metodi di filtrazione e abbinamenti con pasticceria per catturare traffico organico.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Coffee Shop con AI Chef Pro",
    "workflow": [
      "07:00 · Apertura — checklist Kit de Tareas: calibrazione espresso, preparazione latte e alternative vegetali, mise en place pasticceria del giorno.",
      "08:00 · Servizio mattina — picco del mattino con caffè di qualità costante, latte art professionale.",
      "11:00 · Cucina Creativa — sviluppi un nuovo signature autunnale: latte di zucca con sciroppo fatto in casa. Ricetta + scheda tecnica CSV.",
      "12:00 · Kit de Escandallos Pro — carichi il CSV con i tuoi prezzi reali di caffè, latte e sciroppi, validi margine e food cost %.",
      "14:00 · Pasticceria Creativa — sviluppi un nuovo banana bread vegano per completare la carta.",
      "17:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento del nuovo signature e i post minimalisti per Instagram.",
      "19:00 · Chiusura — pulizia profonda della macchina, calibrazione per domani, controllo scorte di caffè e latte.",
      "20:00 · BlogPost SEO Gen+ — programmi un articolo sui metodi di filtrazione per catturare traffico organico."
    ],
    "productsTitle": "Template e Kit Consigliati per Coffee Shop",
    "productIds": [
      "kit-tareas-cafeteria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cucina Creativa + Pasticceria Creativa ci hanno cambiato la proposta. Abbiamo lanciato signature stagionali con scheda tecnica professionale, la pasticceria propria ha alzato il 30% dello scontrino medio e la formazione dei baristi è ora costante. La cattura locale con MenuDish + GastroIMG Gen+ è raddoppiata in 4 mesi.",
    "testimonialAuthor": "Marta Esteve",
    "testimonialRole": "Proprietaria, specialty coffee third-wave",
    "faqTitle": "Domande Frequenti dei Coffee Shop",
    "faqs": [
      {
        "q": "Serve per coffee shop casual, specialty coffee third-wave o roastery con negozio?",
        "a": "Per tutti e tre. Cucina Creativa copre dalle signature semplici fino alla carta di specialty con metodi di filtrazione avanzati."
      },
      {
        "q": "Come fare la scheda tecnica di bevande con latte e alternative vegetali?",
        "a": "Cucina Creativa ragiona come un barista professionista: grammatura esatta di caffè, rapporto di latte, costo di avena premium vs. soia. Kit de Escandallos Pro ricalcola all'istante."
      },
      {
        "q": "Copre la pasticceria propria per differenziarsi?",
        "a": "Sì. Pasticceria Creativa fornisce croissant, brownies, banana bread, cookie e specialità di stagione con scheda tecnica professionale."
      },
      {
        "q": "Genera contenuti visivi minimalisti per Instagram?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento con palette cream e warm wood. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo latte reale."
      },
      {
        "q": "Come mi aiuta con i lanci stagionali?",
        "a": "Gastro Calendar pianifica pumpkin spice latte (autunno), cold brew (estate), caffè speziato di Natale e signature per stagione."
      }
    ],
    "ctaTitle": "Il tuo coffee shop con margine reale e tecnica third-wave.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "IA per Coffee Shop e Specialty Coffee: Carte e Food Cost",
      "description": "Suite di IA per coffee shop: Cucina Creativa, Pasticceria propria, schede tecniche per bevanda, branding minimalista e cattura locale. Inizia oggi.",
      "keywords": "IA coffee shop, software specialty coffee, schede tecniche caffè, third-wave coffee IA, latte art, caffè specialty",
      "ogImage": "https://aichef.pro/og/use-cases/coffee-shop-specialty.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Coffee Shop dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding di 2 minuti in cui gli racconti che tipo di coffee shop gestisci (specialty third-wave, coffee shop casual, roastery con negozio, caffè con pasticceria propria), dimensione del team, città e specialità.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Coffee Shop",
    "apps": [
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di signature: cold brew, latte speziati, specialità stagionali.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Pasticceria propria: croissant, brownies, banana bread, cookie.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Consulenza operativa per caffè e brunch.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per sciroppi, texture e applicazioni speciali.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi nel caffè macinato e latte.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica per alternative vegetali e pasticceria.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia minimalista IA di riferimento per Instagram, web e carta.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale minimalista.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"specialty coffee vicino\".",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Lanci stagionali e signature per stagione.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Articoli SEO sull'origine del caffè e metodi.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico per latte art e pasticceria propria.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo la scheda tecnica delle bevande"
      },
      {
        "value": "+30 %",
        "label": "scontrino medio con pasticceria propria"
      },
      {
        "value": "×2",
        "label": "cattura locale con MenuDish"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo coffee shop"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Carte stagionali improvvisate, signature senza scheda tecnica",
        "Pasticceria esterna con margine incerto",
        "Calibrazione variabile tra baristi",
        "Instagram improvvisato senza palette minimalista",
        "Cattura locale senza SEO di Maps"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Signature stagionali con scheda tecnica professionale",
        "Pasticceria propria con Pasticceria Creativa e margine alto",
        "Calibrazione costante con template di Kit de Tareas",
        "GastroIMG Gen+ + InstaFlow minimalisti",
        "MenuDish Local SEO cattura \"specialty coffee vicino\""
      ]
    },
    "galleryTitle": "Come Funziona un Coffee Shop",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: latte art, caffè di origine, pasticceria, banco e attrezzatura. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-pour.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-beans.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-pastries.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-bar.jpg",
      "/lovable-uploads/ai-gallery/use-case-coffee-shop-team.jpg"
    ]
  },
  "dark-kitchen": {
    "h1": "IA per Dark Kitchen e Cucine Virtuali",
    "heroSubtitle": "Scala 1, 4 o 10 marchi virtuali nella stessa cucina. Controlla il food cost per marchio e per piattaforma, migliora il tuo posizionamento negli agenti IA di delivery e moltiplica i ticket senza assumere altro personale.",
    "heroTagline": "Cucina senza sala, margine con sistema",
    "badge": "Dark Kitchen e Ghost Kitchen",
    "painsTitle": "Le Sfide Che un Operatore di Dark Kitchen Non Può Lasciare Irrisolte",
    "pains": [
      "Più marchi nella stessa cucina, ognuno con la propria scheda tecnica e con costi delle materie prime che cambiano ogni settimana",
      "Margine compresso dalle commissioni di Glovo, Uber Eats e Just Eat (tra il 25% e il 35% del ticket)",
      "Picchi enormi nel delivery, dalle 12:30 alle 14:30 e dalle 20:30 alle 22:30, senza margine per errori operativi",
      "Nessun contatto fisico con il cliente: il marchio, le foto e il copy della scheda sono tutto ciò che hai",
      "Posizionamento sulle piattaforme che cambia continuamente: se perdi posizioni, gli ordini crollano",
      "Difficile sapere quale marchio e quale piatto stanno davvero rendendo quando tutto si mescola nella stessa cucina"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta una Dark Kitchen",
    "features": [
      {
        "title": "Schede tecniche multi-marchio: Cucina Creativa → Kit de Escandallos Pro",
        "description": "Cucina Creativa genera il piatto e la scheda tecnica iniziale in CSV con prezzi di riferimento di mercato. La carichi nel Kit de Escandallos Pro, sostituisci i prezzi con quelli dei tuoi fornitori e ottieni costo reale e margine per marchio, per piatto e per piattaforma.",
        "icon": "Layers"
      },
      {
        "title": "Burger Pro AI+, Food Truck AI+ e Ristoranti Casual AI+",
        "description": "Tre agenti specializzati che coprono i concept virtuali più redditizi nel delivery: hamburgeria, fast food, casual e bistrot.",
        "icon": "Smartphone"
      },
      {
        "title": "Calcolo del margine reale dopo la commissione",
        "description": "Il piano finanziario di AI Chef Pro sconta automaticamente le commissioni di ogni piattaforma e ti mostra il margine reale per marchio e per canale.",
        "icon": "Truck"
      },
      {
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Suite SEO per far scalare i tuoi marchi su Google locale e catturare traffico organico, oltre a quello che arriva dagli agenti IA.",
        "icon": "TrendingUp"
      },
      {
        "title": "Keyword Discovery AI+",
        "description": "Ricerca di parole chiave gastronomiche locali per nominare marchi, piatti e menu che si posizionino meglio.",
        "icon": "Search"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronomica generata con IA per le schede delle piattaforme. Foto migliore = più clic e miglior posizionamento.",
        "icon": "Image"
      },
      {
        "title": "Cucina Creativa + Cucina Italiana, Messicana, Giapponese…",
        "description": "Più di 25 ricettari IA per paese per creare marchi virtuali tematici con base professionale, non ricette copiate da Google.",
        "icon": "Sparkles"
      },
      {
        "title": "HACCP + ID Allergeni per delivery",
        "description": "Tracciabilità, temperatura e allergeni pensati per prodotti che viaggiano in zaino o in moto.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Dashboard multi-marchio e multi-piattaforma",
        "description": "KPI per marchio, ticket medio, commissione, posizione in classifica e produttività. Tutto consolidato in un'unica vista.",
        "icon": "BarChart3"
      }
    ],
    "workflowTitle": "Una Giornata Reale in una Dark Kitchen con AI Chef Pro",
    "workflow": [
      "08:30 · Controlli la dashboard del giorno precedente: il marchio A è in testa, il marchio C è sceso del 12% nel posizionamento. Bisogna agire.",
      "09:00 · Keyword Discovery AI+ — indaghi cosa cercano gli utenti della tua zona postale e individui una parola chiave che manca al marchio C.",
      "09:30 · MenuDish Local SEO — aggiorni le descrizioni dei 6 piatti top del marchio C con quella parola chiave.",
      "10:00 · Cucina Creativa — brainstorming per un piatto forte nel marchio A, approfittando del buon prezzo di un fornitore. Lo stesso agente ti restituisce la ricetta completa e una scheda tecnica iniziale con prezzi di riferimento di mercato, scaricabile in CSV.",
      "10:30 · Kit de Escandallos Pro — carichi il CSV di Cucina Creativa, sostituisci i prezzi di riferimento con quelli dei tuoi fornitori negoziati e validi il margine dopo la commissione su Glovo (29%) e Uber Eats (25%).",
      "11:00 · GastroIMG Gen+ — generi la fotografia del nuovo piatto e la carichi sulle piattaforme.",
      "12:30 · Servizio delivery, con 4 marchi operativi nella stessa cucina supportati dai modelli di attività Dark Kitchen.",
      "16:00 · HACCP firmato, sprechi registrati per marchio e mise en place della cena pronta.",
      "23:30 · Chiusura: report automatico per marchio inviato al WhatsApp del proprietario."
    ],
    "productsTitle": "Modelli, Kit e Guide Scaricabili per Dark Kitchen",
    "productIds": [
      "guia-dark-kitchen",
      "kit-tareas-dark-kitchen",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "kit-inventario"
    ],
    "testimonialQuote": "Operiamo 4 marchi virtuali in una cucina. Senza schede tecniche per marchio e per piattaforma, stavamo perdendo margine senza sapere dove. AI Chef Pro ci ha risolto il problema in una settimana: abbiamo scoperto che un marchio aveva un food cost del 41% su Glovo. L'abbiamo ridisegnato e abbiamo guadagnato 7 punti di margine senza toccare il prezzo.",
    "testimonialAuthor": "Iván Domínguez",
    "testimonialRole": "Operatore, dark kitchen con 4 marchi virtuali",
    "faqTitle": "Domande Frequenti degli Operatori di Dark Kitchen",
    "faqs": [
      {
        "q": "Funziona per 1 marchio o per più marchi nella stessa cucina?",
        "a": "Per entrambi. È pensato fin dall'inizio per il multi-marchio: scheda tecnica indipendente per marchio, KPI separati e liste di attività che coordinano la produzione di più marchi nella stessa partita."
      },
      {
        "q": "Copre le commissioni delle piattaforme (Glovo, Uber Eats e Just Eat)?",
        "a": "Sì. Il calcolo del margine reale sconta automaticamente la commissione di ogni piattaforma, così sai quanto guadagni su ogni ordine per canale e puoi decidere meglio la tua politica dei prezzi."
      },
      {
        "q": "C'è una guida passo passo per aprire una dark kitchen?",
        "a": "Sì, la Guida Come Aprire una Dark Kitchen (24 €): 12 capitoli con requisiti legali, piano finanziario, design della cucina, tecnologia, marketing e piattaforme, oltre a 3 checklist in Excel e una calcolatrice."
      },
      {
        "q": "Serve per scalare a più sedi di dark kitchen?",
        "a": "Sì. La standardizzazione multi-sede dell'agente Chef Esecutivo Pro e le dashboard consolidate sono pensate per gruppi con più unità virtuali."
      },
      {
        "q": "Come mi aiuta a migliorare il posizionamento negli agenti IA di delivery?",
        "a": "Con tre leve: GastroIMG Gen+ per foto di qualità superiore (che aumentano il CTR), MenuDish Local SEO per descrizioni che convertono e Keyword Discovery AI+ per individuare cosa cercano gli utenti della tua zona postale."
      },
      {
        "q": "Il sistema si adatta al mio paese e alle mie piattaforme?",
        "a": "Sì. Inizi con l'agente «Chi sono?» in un onboarding di 2 minuti dove gli racconti dove operi, quali piattaforme usi e quali commissioni hai negoziato. Tutto il resto si adatta al tuo contesto."
      },
      {
        "q": "E la SEO locale? Vale la pena per una dark kitchen?",
        "a": "Sì, molto. Una dark kitchen vive di scoperta online: se oltre al traffico degli agenti IA catturi ricerche locali su Google (ad esempio, «hamburger delivery [il tuo quartiere]»), riduci la dipendenza dalle commissioni e aggiungi margine diretto. La suite SEO di AI Chef Pro è pensata esattamente per questo."
      }
    ],
    "ctaTitle": "La tua dark kitchen, con margine reale e dati per marchio.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Dark Kitchen: Schede Tecniche e SEO | AI Chef Pro",
      "description": "Suite IA per dark kitchen: schede tecniche multi-marchio, margine dopo commissioni, SEO locale, HACCP e guida per aprire la tua cucina virtuale.",
      "keywords": "IA dark kitchen, dark kitchen software, ghost kitchen, cucina virtuale, schede tecniche multi-marchio, aprire dark kitchen, gestione delivery IA, posizionamento Glovo Uber Eats, software cucina fantasma, marchio virtuale delivery, dark kitchen Italia, SEO locale ristorante delivery",
      "ogImage": "https://aichef.pro/og/use-cases/dark-kitchen.jpg"
    },
    "personalizationTitle": "Personalizzato per i Tuoi Marchi, la Tua Zona e le Tue Piattaforme",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti. Gli racconti quali marchi operi, in quale città e zona postale, quali piattaforme utilizzi (Glovo, Uber Eats, Just Eat) e quali commissioni hai negoziato. Da quel momento, le schede tecniche vengono calcolate con la tua commissione reale, le raccomandazioni di SEO locale puntano al tuo quartiere e i KPI si consolidano per marchio e per canale come ti servono. Non è un modulo: è una conversazione breve che trasforma ogni agente in uno strumento su misura.",
    "appsTitle": "Gli Agenti IA che Userai nella Tua Dark Kitchen",
    "apps": [
      {
        "name": "Burger Pro AI+",
        "description": "Specialista in hamburgerie virtuali: gourmet, fast food, smash burger e plant-based.",
        "category": "Concetti di Business"
      },
      {
        "name": "Food Truck AI+",
        "description": "Concept mobili e virtuali di fast food con margine ridotto.",
        "category": "Concetti di Business"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Bistrot, gastropub, tapas e mediterraneo virtuale: tutto lo spettro casual.",
        "category": "Concetti di Business"
      },
      {
        "name": "Cucina Italiana, Messicana, Giapponese, Thailandese…",
        "description": "Più di 25 ricettari IA per creare marchi virtuali tematici con base professionale. Ogni ricetta arriva con scheda tecnica iniziale in CSV pronta per il Kit de Escandallos Pro.",
        "category": "Ricettari per Paese"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi su sprechi e rese. Critico per una scheda tecnica realistica nel delivery.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta. Obbligatorio per vendere nel delivery in modo legale.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Descrizioni ottimizzate per SEO per piatto, pronte per il blog e per le piattaforme.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Post di blog che catturano traffico organico locale verso i tuoi marchi virtuali.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Keyword Discovery AI+",
        "description": "Ricerca di parole chiave gastronomiche per zona postale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica con IA per le schede delle piattaforme: foto migliore, posizionamento migliore.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Manager Ristorante Pro",
        "description": "Assistente operativo per coordinare marchi, team e fornitori.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "InstaFlow AI Pro + Pinterest Pins Gen",
        "description": "Contenuti virali per attirare pubblico oltre le piattaforme di delivery.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "margine dopo aver fatto le schede tecniche per marchio"
      },
      {
        "value": "×4",
        "label": "marchi virtuali in una cucina"
      },
      {
        "value": "−35 %",
        "label": "tempo nella gestione multi-marchio"
      },
      {
        "value": "12+",
        "label": "agenti IA per dark kitchen"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Scheda tecnica manuale in Excel con margine «medio» tra marchi",
        "Commissioni delle piattaforme sottratte a occhio, senza sapere quale canale conviene di più",
        "Foto di piattaforma di qualità media e posizionamento erratico",
        "Descrizioni generiche che non catturano la SEO locale",
        "KPI mescolati: impossibile sapere quale marchio rende davvero",
        "Operatività su fogli sparsi ed errori nelle ore di punta"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Scheda tecnica indipendente per marchio e per piattaforma, con margine reale all'istante",
        "Calcolo automatico dopo la commissione per canale e decisioni di prezzo con dati",
        "Fotografie professionali con GastroIMG Gen+ e posizionamento più stabile",
        "Descrizioni e blog ottimizzati per la SEO locale della tua zona postale",
        "Dashboard multi-marchio con KPI separati per marchio e per canale",
        "Liste di attività Dark Kitchen specifiche per coordinare la produzione multi-marchio"
      ]
    },
    "galleryTitle": "Come Funziona una Dark Kitchen Moderna",
    "gallerySubtitle": "Produzione multi-marchio, packaging branded per marchio virtuale, schermi con ordini da Glovo, Uber Eats e JustEat, rider in pickup e tutto ciò che circonda un'operatività 100% delivery.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-cooking.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-packaging.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-orders.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-pickup.jpg",
      "/lovable-uploads/ai-gallery/use-case-dark-kitchen-app.jpg"
    ]
  },
  "director-operaciones-grupo": {
    "h1": "IA per Direttori Operativi di Gruppi di Ristorazione",
    "heroSubtitle": "Standardizza processi, consolida il reporting e moltiplica la produttività operativa in gruppi multi-locale con una suite di agenti IA specializzati nell'ospitalità.",
    "heroTagline": "Stesso standard in tutti i locali, dati consolidati in un clic",
    "badge": "Per direttori operativi di gruppi",
    "painsTitle": "Cosa un Direttore Operativo Multi-Locale Non Può Ignorare",
    "pains": [
      "Mantenere lo stesso standard di qualità, processi ed esperienza in tutti i locali del gruppo",
      "Consolidare KPI finanziari, operativi e di team per confrontare le performance tra le unità",
      "Replicare manuali operativi, formazione e onboarding senza perdere qualità quando la rete cresce",
      "Individuare in tempo i locali con scostamenti di food cost, personale o produttività prima che erodano il margine",
      "Coordinare i manager di ogni locale con comunicazione chiara e reporting coerente",
      "Scalare il gruppo aprendo nuove unità senza dover reinventare la ruota a ogni apertura"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Direttore Operativo",
    "features": [
      {
        "title": "Standardizzazione multi-locale",
        "description": "Manuali, checklist e procedure uniformi che si replicano a tutte le unità del gruppo con un clic.",
        "icon": "Building2"
      },
      {
        "title": "Dashboard consolidati",
        "description": "Kit Plan Finanziario: confronta food cost, produttività, sprechi e scontrino medio tra tutti i tuoi ristoranti in un'unica vista.",
        "icon": "BarChart3"
      },
      {
        "title": "Chef Esecutivo Pro",
        "description": "Agente che standardizza ricette e schede tecniche affinché lo stesso piatto esca uguale in 1, 5 o 25 cucine.",
        "icon": "ChefHat"
      },
      {
        "title": "Manager Ristorante Pro",
        "description": "Assistente per ogni manager locale che riporta verso l'alto con dati consolidati al direttore operativo.",
        "icon": "BriefcaseBusiness"
      },
      {
        "title": "Manuali operativi con IA",
        "description": "Onboarding, formazione del team e procedure sempre aggiornate da un unico repository centrale.",
        "icon": "BookOpen"
      },
      {
        "title": "HACCP aziendale unificato",
        "description": "Un unico sistema documentale per tutte le unità del gruppo: tracciabilità e temperature centralizzate.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Audit dei costi per locale",
        "description": "Sprechi GenCal e Kit Escandallos Pro individuano scostamenti di food cost prima che sfuggano di mano.",
        "icon": "TrendingDown"
      },
      {
        "title": "Turni e struttura del team",
        "description": "Kit Gestione Personale: stessa struttura di turni, rapporti e produttività in tutte le unità.",
        "icon": "Users"
      },
      {
        "title": "Sonar Deep Research",
        "description": "Ricerca approfondita di trend, competitor e mercati per decisioni strategiche di espansione.",
        "icon": "Search"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Direttore Operativo con AI Chef Pro",
    "workflow": [
      "08:30 · Caffè e Kit Plan Finanziario — apri la dashboard consolidata dei 7 locali del gruppo e noti che il locale 4 ha un food cost al 33% (+3 pp rispetto all'obiettivo).",
      "09:30 · Manager Ristorante Pro — chiedi all'agente un'analisi automatizzata della causa per locale. Identifica un problema negli sprechi di pesce.",
      "10:30 · Videochiamata con la manager del locale 4 supportata da dati reali del Kit Plan Finanziario, non dall'intuito.",
      "12:00 · Chef Esecutivo Pro — aggiorni la procedura di manipolazione del pesce e si replica alle 7 cucine come nuova versione del manuale.",
      "15:30 · Turni consolidati — rivedi il Kit Gestione Personale con i rapporti di produttività di tutti i locali e firmi l'onboarding della nuova manager del locale 8.",
      "17:00 · Sonar Deep Research — studi il mercato per la prossima apertura in un'altra città: analisi delle zone, scontrino medio e concorrenza.",
      "19:00 · Riunione con il comitato — esporti i KPI del trimestre in PDF direttamente dal Kit Plan Finanziario. Riunione chiusa in 45 minuti.",
      "21:30 · Chiusura — i 7 manager ti inviano il report automatico della giornata via WhatsApp. Torna a casa con una visione completa del gruppo."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Gruppi di Ristorazione",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-tareas"
    ],
    "testimonialQuote": "Gestiamo 7 locali e prima ognuno lavorava in modo diverso: diversi Excel, diversi manuali, diversi HACCP. Con AI Chef Pro abbiamo lo stesso standard ovunque e reporting consolidato in un'unica vista. Individuare il locale con problemi è passato da 2 settimane a 1 giorno.",
    "testimonialAuthor": "Javier Ortega",
    "testimonialRole": "Direttore Operativo, gruppo di ristorazione con 7 locali",
    "faqTitle": "Domande Frequenti dei Direttori Operativi",
    "faqs": [
      {
        "q": "Quanti locali supporta AI Chef Pro?",
        "a": "Nessun limite reale. Ci sono clienti con 1 locale e altri con più di 25 unità attive. I piani aziendali scalano per utilizzi e sbloccano dashboard consolidati, onboarding personalizzato e supporto prioritario."
      },
      {
        "q": "Si integra con il nostro ERP o sistema contabile?",
        "a": "I modelli esportano in Excel, PDF e CSV in formati compatibili con la maggior parte degli ERP e dei sistemi contabili. Il tuo team finanziario riceve documentazione pronta per l'integrazione."
      },
      {
        "q": "Consente ruoli e permessi per locale?",
        "a": "Sì. Puoi dare accesso per manager locale, per direttore regionale o consolidato al direttore operativo. Ogni livello vede solo i dati che gli competono."
      },
      {
        "q": "Come si garantisce lo stesso standard in tutte le unità?",
        "a": "Chef Esecutivo Pro standardizza ricette e schede tecniche; il Pack HACCP unifica la tracciabilità; il Kit Escandallos Pro mantiene gli stessi calcoli in tutti i locali. I manuali si replicano con un clic e si aggiornano da un unico punto."
      },
      {
        "q": "Ci sono sconti per gruppi con più locali?",
        "a": "Sì. A partire da 5 unità attive ci sono piani aziendali con onboarding personalizzato, dashboard consolidati, formazione del team centrale e supporto prioritario."
      },
      {
        "q": "Serve per aprire nuove sedi più velocemente?",
        "a": "Sì. È uno dei casi d'uso più ricorrenti: le guide Come Aprire… (dark kitchen, ristorante gastronomico, casual, messicano, giapponese, peruviano, nikkei) sono roadmap professionali che accelerano le aperture con piano finanziario, business plan e manuali replicabili."
      }
    ],
    "ctaTitle": "Standardizza il tuo gruppo. Stesso standard in tutti i locali.",
    "ctaSubtitle": "Parla con noi per un onboarding personalizzato per il tuo gruppo o inizia con il piano Membro: 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "IA per Direttori Operativi di Gruppi di Ristorazione | AI Chef Pro",
      "description": "Suite IA per gruppi di ristorazione multi-locale: dashboard consolidati, standardizzazione ricette, HACCP aziendale, manuali replicabili e piano finanziario per unità.",
      "keywords": "IA gruppo ristorazione, software multi-locale ristoranti, direttore operativo ristoranti IA, standardizzare processi ristorante, dashboard consolidati ristorante, scalare gruppo ristorazione, multi-locale IA ospitalità",
      "ogImage": "https://aichef.pro/og/use-cases/director-operaciones-grupo.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Gruppo dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti quanti locali gestisci, quali concept operate (casual, gastronomico, dark kitchen, hotel), in quali paesi e come lavora la tua organizzazione. Da quel momento, ogni agente — dal Piano Finanziario ai manuali operativi — risponde adattato alla scala e alla struttura reale del gruppo. Non è un modulo: è una conversazione breve che rende la suite davvero utile per i direttori operativi multi-locale.",
    "appsTitle": "Gli Agenti IA che Userai come Direttore Operativo",
    "apps": [
      {
        "name": "Chef Esecutivo Pro",
        "description": "Standardizzazione di ricette, schede tecniche e manuali replicabili a tutte le unità del gruppo.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Manager Ristorante Pro",
        "description": "Assistente per ogni manager locale con reporting consolidato verso l'alto.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Specialista in bistrot, gastropub e casual: lo spettro più comune nei gruppi multi-locale.",
        "category": "Concetti di Business"
      },
      {
        "name": "Burger Pro AI+",
        "description": "Per gruppi con marchi di hamburgeria gourmet o fast casual.",
        "category": "Concetti di Business"
      },
      {
        "name": "Catering AI+",
        "description": "Per gruppi con divisione catering ed eventi aziendali.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca approfondita di trend, competitor e mercati per decisioni strategiche.",
        "category": "Modelli IA + LLM"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi su sprechi e rese per ingrediente, essenziali per l'audit multi-locale.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta, unificata in tutte le unità.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Articoli per il blog per attirare traffico organico per ogni unità del gruppo.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Keyword Discovery AI+",
        "description": "Ricerca di parole chiave per zona postale di ogni locale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica con IA unificata per tutto il marchio del gruppo.",
        "category": "Gastro Conoscenza"
      }
    ],
    "metrics": [
      {
        "value": "−14 g",
        "label": "per individuare un locale con scostamenti"
      },
      {
        "value": "×7",
        "label": "velocità di reporting consolidato"
      },
      {
        "value": "+3 pp",
        "label": "margine dopo la standardizzazione"
      },
      {
        "value": "11+",
        "label": "agenti per multi-locale"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "7 locali con 7 Excel diversi, manuali eterogenei e HACCP incoerente",
        "Individuare un locale con scostamenti richiede 2 settimane perché non c'è reporting consolidato",
        "Onboarding di un nuovo manager in 1 mese con materiali improvvisati da ogni unità",
        "Reporting al comitato con file sparsi e senza dashboard professionali",
        "Decisioni di espansione per intuizione, senza analisi di mercato approfondita"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Stesso standard replicato nelle 7 unità: ricette, manuali e HACCP unificati",
        "Individuare un locale con scostamenti in 1 giorno con la dashboard consolidata del Kit Plan Finanziario",
        "Onboarding di un nuovo manager in 1 settimana con manuali e formazione replicabili",
        "Reporting al comitato in PDF diretto dal Kit Plan Finanziario con KPI consolidati",
        "Decisioni di espansione supportate da Sonar Deep Research e guide Come Aprire… professionali"
      ]
    },
    "galleryTitle": "La Giornata di un Direttore Operativo, in Immagini",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: dashboard multi-locale, riunioni di strategia, audit alle unità, manuali aziendali e onboarding dei manager.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-multilocal.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-meeting.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-audit.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-strategy.jpg",
      "/lovable-uploads/ai-gallery/use-case-director-operaciones-handover.jpg"
    ]
  },
  "fb-manager-hotel": {
    "h1": "IA per F&B Manager di Hotel",
    "heroSubtitle": "Coordina ristoranti, banchetti, room service, breakfast buffet e bar dell'hotel con food cost incrociato, modelli operativi professionali e branding integrato con una suite di agenti IA gastronomici specializzati nella gestione integrata F&B alberghiera.",
    "heroTagline": "F&B alberghiero con margine reale e operatività professionale",
    "badge": "Per F&B Manager, Direttori di Alimenti e Bevande",
    "painsTitle": "Cosa un F&B Manager non può lasciare irrisolto",
    "pains": [
      "Coordinare più outlet simultaneamente (ristorante principale, room service, breakfast buffet, bar piscina, banchetti, caffetteria)",
      "Calcolare il food cost incrociato del menu tra outlet mantenendo coerenza di food cost e margine integrato",
      "Alti sprechi nel breakfast buffet (offerta abbondante con consumo variabile) e nei banchetti (volume elevato, complessità logistica)",
      "Standardizzare le procedure per turno con squadre rotanti e tre servizi giornalieri",
      "Differenziarsi in un hotel competitivo con esperienza gastronomica integrale, branding visivo e storytelling di hospitality",
      "Catturare eventi aziendali, matrimoni e banchetti premium con proposte professionali e margine validato"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un F&B Manager",
    "features": [
      {
        "title": "Manager Ristorante Pro",
        "description": "Agente specializzato del catalogo Gastro Profile Pro adattato alla gestione F&B alberghiera multi-outlet.",
        "icon": "Hotel"
      },
      {
        "title": "Catering AI+",
        "description": "Consulenza professionale per banchetti, matrimoni ed eventi aziendali dell'hotel.",
        "icon": "PartyPopper"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per lo sviluppo di menu integrati: ristorante principale, breakfast buffet, room service e bar piscina con coerenza.",
        "icon": "Sparkles"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Per la cocktaileria del bar piscina, lobby bar e abbinamenti del ristorante principale.",
        "icon": "Wine"
      },
      {
        "title": "Food cost incrociati",
        "description": "Cucina Creativa fornisce ricetta + food cost CSV; Kit de Escandallos Pro lo gestisce con costo incrociato tra outlet e margine integrato.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Hotel Completo",
        "description": "Modelli per 5 outlet: ristorante, breakfast, room service, bar, banchetti con procedure per turno.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC alberghiero",
        "description": "Tracciabilità di buffet, banchetti, room service e bar con temperature critiche e conservazione.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione di eventi aziendali, matrimoni, stagioni (estate/inverno), Natale, San Valentino, conferenze.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia premium IA di riferimento + Instagram per tutti gli outlet dell'hotel con coerenza di marca.",
        "icon": "Image"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un F&B Manager con AI Chef Pro",
    "workflow": [
      "06:00 · Apertura breakfast — checklist Kit de Tareas Hotel: preparazione buffet, controllo chafing dish, temperature, mise en place stazione uova.",
      "09:00 · Coordinamento con cucina principale — Cucina Creativa aggiorna il menu del pranzo con prodotto di stagione. Ricetta + food cost CSV.",
      "10:00 · Catering AI+ — sviluppi la proposta di menu per matrimonio di 120 pax con tre portate. Calcula Pax scala le ricette, Kit de Escandallos Pro valida costo e margine.",
      "12:00 · Servizio pranzo al ristorante principale + room service — coordinamento incrociato tra outlet.",
      "14:00 · Bar & Lounge AI+ — sviluppi il nuovo menu di cocktail per il bar piscina stagione estiva.",
      "17:00 · Banchetto aziendale di 80 pax — esecuzione con modello specifico del Kit de Tareas.",
      "20:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi immagini di riferimento per i quattro outlet e i post coerenti per l'Instagram dell'hotel.",
      "23:00 · Chiusura — pulizia profonda multi-outlet, HACCP firmato, pianificazione breakfast e servizi del giorno successivo."
    ],
    "productsTitle": "Modelli e Kit Consigliati per F&B Manager",
    "productIds": [
      "kit-tareas-hotel",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Gestire cinque outlet senza sistema era caos. Manager Ristorante Pro + Catering AI+ ci coordinano menu incrociato, banchetti e room service con food cost integrato. La pianificazione di matrimoni di 120 pax che prima era una settimana ora è un giorno con proposta professionale. Abbiamo aumentato il margine di 5 punti incrociando gli outlet e chiuso eventi premium molto più velocemente.",
    "testimonialAuthor": "Roberto Castaño",
    "testimonialRole": "F&B Director, hotel 5 stelle",
    "faqTitle": "Domande Frequenti dei F&B Manager",
    "faqs": [
      {
        "q": "È adatto per hotel boutique, hotel di catena, all-inclusive o hotel di lusso?",
        "a": "Per tutti e quattro. Manager Ristorante Pro + Catering AI+ + Bar & Lounge AI+ coprono dall'hotel boutique con un ristorante all'hotel 5 stelle con 5+ outlet, all-inclusive con buffet massiccio o resort vacanziero."
      },
      {
        "q": "Come coordino il menu incrociato tra outlet?",
        "a": "Cucina Creativa ragiona con coerenza tra outlet: prodotto del menu principale riutilizzato nel breakfast, nel room service e nei banchetti, ottimizzando il food cost integrato e riducendo gli sprechi incrociati."
      },
      {
        "q": "Come scaldo le schede tecniche per banchetti di 50, 100 o 300 pax?",
        "a": "Calcula Pax scala le ricette senza perdere precisione; Kit de Escandallos Pro ricalcola il costo per pax e la proposta economica al cliente aziendale o di matrimoni."
      },
      {
        "q": "Genera contenuto visivo coerente per l'Instagram dell'hotel?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali per i quattro outlet con coerenza di marca; InstaFlow AI Pro programma Instagram. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo piatto impiattato reale."
      },
      {
        "q": "Come mi aiuta con eventi aziendali e stagioni?",
        "a": "Gastro Calendar pianifica eventi aziendali, matrimoni, conferenze, stagioni (estate/inverno), Natale e San Valentino con menu specifici per outlet e calendario editoriale coordinato."
      }
    ],
    "ctaTitle": "Il tuo F&B alberghiero con margine integrato e operatività professionale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per F&B Manager: Multi-outlet, Banchetti | AI Chef Pro",
      "description": "Suite IA per F&B Manager di hotel: Manager Ristorante Pro, Catering AI+, food cost incrociato, branding multi-outlet e HACCP integrato. Inizia oggi.",
      "keywords": "IA F&B manager, IA hotel F&B, software hotel ristorante, food cost hotel, banchetti hotel IA, breakfast buffet hotel",
      "ogImage": "https://aichef.pro/og/use-cases/fb-manager-hotel.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Hotel dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di hotel gestisci (boutique, catena, 5 stelle, all-inclusive, resort vacanziero), numero di outlet F&B, dimensione del team e specialità. Ogni agente — da Manager Ristorante Pro a Catering AI+ — risponde adattato al tuo hotel reale.",
    "appsTitle": "Gli Agenti IA che Userai come F&B Manager",
    "apps": [
      {
        "name": "Manager Ristorante Pro",
        "description": "Agente specializzato adattato alla gestione F&B alberghiera multi-outlet.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Catering AI+",
        "description": "Banchetti, matrimoni ed eventi aziendali dell'hotel con proposte professionali.",
        "category": "Concetti di Business"
      },
      {
        "name": "Cucina Creativa",
        "description": "Menu integrati con coerenza tra outlet e ricetta + food cost CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Per la cocktaileria del bar piscina, lobby bar e abbinamenti del ristorante principale.",
        "category": "Concetti di Business"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Per il ristorante casual e la caffetteria dell'hotel.",
        "category": "Concetti di Business"
      },
      {
        "name": "Calcula Pax",
        "description": "Scalatura delle ricette per banchetti di 50, 100, 300 o 500 pax.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi nel breakfast buffet, banchetti e room service.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica per clienti con allergie nei banchetti.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia premium IA di riferimento con coerenza di marca per tutti gli outlet.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale coordinato per tutti gli outlet.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"ristorante hotel\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Eventi aziendali, matrimoni, conferenze, Natale, San Valentino, stagioni.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo food cost incrociato"
      },
      {
        "value": "×7",
        "label": "velocità di proposte di banchetto"
      },
      {
        "value": "−25 %",
        "label": "sprechi nel breakfast buffet"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo F&B"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Outlet coordinati manualmente, food cost incrociato senza tracciabilità",
        "Banchetti calcolati a mano: una settimana per matrimonio",
        "Sprechi nel breakfast buffet senza controllo reale",
        "Branding visivo disperso tra outlet senza coerenza",
        "HACCP su carta stampata disperso tra gli outlet"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Outlet coordinati con food cost incrociato e margine integrato",
        "Banchetti calcolati in un giorno con proposta professionale",
        "Sprechi controllati con Sprechi GenCal in breakfast e banchetti",
        "Branding coerente con GastroIMG Gen+ + InstaFlow AI Pro",
        "HACCP da mobile multi-outlet con registri pronti per ispezione"
      ]
    },
    "galleryTitle": "Come Funziona l'F&B di un Hotel",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: ristorante, banchetti, breakfast, room service e bar piscina. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-fb-manager-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-banquet.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-breakfast.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-roomservice.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-bar.jpg",
      "/lovable-uploads/ai-gallery/use-case-fb-manager-team.jpg"
    ]
  },
  "food-truck": {
    "h1": "IA per Food Truck",
    "heroSubtitle": "Progetta un menu compatto con scheda tecnica rigorosa, gestisci la preparazione adattata allo spazio limitato, pianifica eventi e percorsi e cattura branding virale con una suite di agenti di IA gastronomica specializzati in food truck professionale.",
    "heroTagline": "Food truck con margine reale e operatività snella",
    "badge": "Per food truck, cucine mobili e street food",
    "painsTitle": "Cosa un Food Truck Non Può Non Risolvere",
    "pains": [
      "Menu compatto e curato (5-10 piatti max) con costo ottimizzato per processo efficiente",
      "Spazio limitato: preparazione adattata, mise en place compatta, attrezzature condivise, stoccaggio minimo",
      "Sprechi controllati su prodotto fresco con acquisto adattato al volume dell'evento",
      "Standardizzare la tecnica turno per turno con personale rotativo e attrezzature variabili",
      "Differenziarsi con branding visivo iconico, social media attivi e storytelling di hand-painted",
      "Pianificare percorsi di eventi (festival, fiere, mercati, eventi privati) con margine alto"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Food Truck",
    "features": [
      {
        "title": "Food Truck AI+",
        "description": "Agente specializzato in food truck e cucine mobili: operatività, preparazione, eventi, branding e percorsi.",
        "icon": "Truck"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per signature di food truck: smash burger, bao, taco, pollo croccante con scheda tecnica professionale.",
        "icon": "Sparkles"
      },
      {
        "title": "Scheda tecnica per piatto",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica CSV; Kit de Escandallos Pro lo gestisce con costo reale adattato all'operatività mobile.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelli: pre-evento, preparazione adattata, montaggio, servizio rapido, chiusura, ricarica.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC food truck",
        "description": "Tracciabilità adattata all'operatività mobile: temperature, acqua, rifiuti.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Festival, fiere, mercati, eventi aziendali privati.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia street food virale IA + Instagram con calendario editoriale attivo.",
        "icon": "Image"
      },
      {
        "title": "MenuDish Local SEO",
        "description": "Catturare clienti che cercano \"food truck vicino\" o \"street food a [città]\".",
        "icon": "BarChart3"
      },
      {
        "title": "Sprechi GenCal",
        "description": "Sprechi su prodotto fresco con acquisto adattato al volume dell'evento.",
        "icon": "Sparkles"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Food Truck con AI Chef Pro",
    "workflow": [
      "08:00 · Apertura — checklist Kit de Tareas: revisione attrezzature, montaggio mise en place compatta, preparazione adattata al volume dell'evento.",
      "10:00 · Food Truck AI+ — sviluppi una nuova smash burger signature con formaggio americano e bacon affumicato. Ricetta + scheda tecnica CSV.",
      "11:00 · Kit de Escandallos Pro — carichi CSV con prezzi reali e volume stimato dell'evento, validi il margine.",
      "12:00 · Arrivo all'evento (festival musicale) — montaggio, collegamento elettrico, controllo HACCP.",
      "13:00 · Servizio di mezzogiorno — picco forte con code controllate, preparazione efficiente.",
      "17:00 · Pausa — ricarica scorte, controllo sprechi e cassa del primo servizio.",
      "20:00 · Servizio serale — picco maggiore, GastroIMG Gen+ ha già la foto del giorno programmata su Instagram.",
      "00:00 · Chiusura — pulizia, HACCP firmato, pianificazione del prossimo evento con Gastro Calendar."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Food Truck",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Food Truck AI+ + Cucina Creativa ci hanno cambiato l'operatività. Il menu è più compatto, le schede tecniche per piatto riflettono margine reale con acquisto adattato al volume dell'evento, e l'acquisizione con InstaFlow + GastroIMG ci ha triplicato le prenotazioni per eventi privati in 6 mesi.",
    "testimonialAuthor": "Marcos Bermúdez",
    "testimonialRole": "Proprietario, food truck artigianale",
    "faqTitle": "Domande Frequenti dei Food Truck",
    "faqs": [
      {
        "q": "Serve per food truck casual, gourmet o cucina mobile per eventi privati?",
        "a": "Per tutti e tre. Food Truck AI+ copre da casual a gourmet, passando per cucina mobile per matrimoni ed eventi aziendali."
      },
      {
        "q": "Come calcolare la scheda tecnica con acquisto adattato all'evento?",
        "a": "Kit de Escandallos Pro ricalcola all'istante il margine in base al volume stimato dell'evento."
      },
      {
        "q": "Copre l'operatività mobile con spazio limitato?",
        "a": "Sì. Food Truck AI+ ragiona come operatore professionale: preparazione compatta, mise en place efficiente, attrezzature condivise."
      },
      {
        "q": "Genera contenuti virali per Instagram e TikTok?",
        "a": "Sì. GastroIMG Gen+ + InstaFlow AI Pro generano contenuti virali con calendario editoriale attivo. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo piatto reale."
      },
      {
        "q": "Come mi aiuta con eventi e percorsi?",
        "a": "Gastro Calendar pianifica festival, fiere, mercati ed eventi privati con pianificazione dei percorsi."
      }
    ],
    "ctaTitle": "Il tuo food truck con margine reale e operatività snella.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "IA per Food Truck: Menu, Food Cost e Eventi | AI Chef Pro",
      "description": "Suite di IA per food truck: Food Truck AI+, schede tecniche per piatto, pianificazione eventi, branding virale e HACCP. Inizia oggi.",
      "keywords": "IA food truck, software food truck, schede tecniche food truck, street food IA, cucina mobile, eventi food truck",
      "ogImage": "https://aichef.pro/og/use-cases/food-truck.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Food Truck dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding di 2 minuti in cui racconti che tipo di food truck gestisci (casual, gourmet, eventi privati, mercato, festival), dimensione del team, specialità e zone di operazione.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Food Truck",
    "apps": [
      {
        "name": "Food Truck AI+",
        "description": "Agente specializzato in food truck e cucine mobili.",
        "category": "Concetti di Business"
      },
      {
        "name": "Burger Pro AI+",
        "description": "Per food truck di smash burger e hamburgheria gourmet.",
        "category": "Concetti di Business"
      },
      {
        "name": "Cucina Creativa",
        "description": "Signature con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Consulenza operativa casual.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi con acquisto adattato all'evento.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica per piatto.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia street food virale IA di riferimento.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale attivo.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti che cercano \"food truck vicino\".",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Festival, fiere, mercati, eventi privati.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico per street food.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching per gestione dello stress in eventi di massa.",
        "category": "Strumenti e Utility"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo food cost del menu"
      },
      {
        "value": "×3",
        "label": "prenotazioni eventi privati in 6 mesi"
      },
      {
        "value": "−20 %",
        "label": "sprechi con acquisto adattato"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo food truck"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Menu esteso con food cost incerto",
        "Acquisto di prodotto senza adattamento al volume dell'evento",
        "Sprechi elevati su prodotto fresco",
        "Instagram improvvisato, senza contenuti virali",
        "Eventi privati chiusi manualmente"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Menu compatto con scheda tecnica professionale",
        "Acquisto adattato al volume stimato dell'evento",
        "Sprechi controllati con Sprechi GenCal",
        "GastroIMG Gen+ + InstaFlow contenuti virali",
        "Eventi privati chiusi con proposta professionale"
      ]
    },
    "galleryTitle": "Come Funziona un Food Truck",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: truck, preparazione, piastra, servizio e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-food-truck-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-counter.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-grill.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-line.jpg",
      "/lovable-uploads/ai-gallery/use-case-food-truck-team.jpg"
    ]
  },
  "gastrobar-tapas": {
    "h1": "IA per Gastrobar e Tapas Bar",
    "heroSubtitle": "Progetta carta di tapas e pintxos con scheda tecnica professionale, gestisci vermut e vini al calice, pianifica eventi e cattura branding spagnolo autentico con una suite di agenti IA gastronomici specializzati in gastrobar e cucina spagnola.",
    "heroTagline": "Tapas con tecnica autentica e margine reale",
    "badge": "Per gastrobar, tapas bar, pintxos e enoteche",
    "painsTitle": "Cosa un Gastrobar Non Può Non Risolvere",
    "pains": [
      "Carta di tapas con molte varianti (fredde, calde, pintxos, porzioni) mantenendo un food cost coerente",
      "Perdite su prodotto fresco (acciughe, prosciutto, frutti di mare), pane e salumi con scadenza breve",
      "Standardizzare tapas signature turno per turno con consistenza e velocità di servizio",
      "Gestione di vermut, vini al calice e birre con margine alto e rotazione corretta",
      "Differenziarsi con prodotto di qualità, branding spagnolo autentico e storytelling di fornitori artigianali",
      "Catturare eventi privati e degustazioni con abbinamenti professionali"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Gastrobar",
    "features": [
      {
        "title": "Ristoranti Casual AI+",
        "description": "Consulenza operativa per gastrobar e tapas bar.",
        "icon": "Wine"
      },
      {
        "title": "Cucina Spagnola + Cucina Creativa",
        "description": "Ricettari specializzati: tapas tradizionali, pintxos baschi, porzioni di mercato, fusioni.",
        "icon": "Sparkles"
      },
      {
        "title": "Scheda tecnica per tapa e porzione",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica CSV; Kit Escandallos Pro lo gestisce con costo reale per tapa e food cost %.",
        "icon": "Calculator"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Vermut, vini spagnoli al calice, birre artigianali e abbinamenti con tapas.",
        "icon": "Wine"
      },
      {
        "title": "Kit de Tareas Bar",
        "description": "Modelli: preparazione tapas, mise en place bar, vermut, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack HACCP bar",
        "description": "Tracciabilità di prosciutto, salumi, acciughe, frutti di mare freschi.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Giornata Mondiale della Tapa, San Fermín, feste locali, eventi privati.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia artigianale spagnola IA + Instagram per attirare locali e turisti.",
        "icon": "Image"
      },
      {
        "title": "MenuDish Local SEO",
        "description": "Catturare clienti che cercano \"tapas vicino\" o \"gastrobar [città]\".",
        "icon": "BarChart3"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Gastrobar con AI Chef Pro",
    "workflow": [
      "11:00 · Apertura — checklist Kit de Tareas: preparazione tapas fredde, allestimento del portaprosciutto, mise en place bar, controllo del rubinetto del vermut.",
      "12:30 · Cucina Spagnola + Cucina Creativa — sviluppi una nuova tapa signature di acciuga marinata in casa con piparra e olio di pomodoro. Ricetta + scheda tecnica CSV.",
      "13:30 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali, validi il margine per tapa e il food cost %.",
      "14:00 · Servizio di mezzogiorno — picco forte con vermut e tapas, mise en place impeccabile.",
      "17:00 · Pausa — Bar & Lounge AI+ valida abbinamenti con vini Albariño e Verdejo per nuove tapas.",
      "19:00 · Servizio serale — picchi con birre artigianali e vini al calice.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi immagine di riferimento e post.",
      "00:00 · Chiusura — pulizia, HACCP firmato, controllo scorte."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Gastrobar",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cucina Spagnola + Bar & Lounge AI+ ci hanno alzato il livello. Le tapas signature ora hanno scheda tecnica professionale con margine validato, gli abbinamenti con vini al calice sono consistenti e abbiamo aumentato lo scontrino medio del 15% in 4 mesi. La cattura locale con MenuDish + GastroIMG è x2.",
    "testimonialAuthor": "Iñaki Etxeberria",
    "testimonialRole": "Proprietario, gastrobar contemporaneo a Donostia",
    "faqTitle": "Domande Frequenti dei Gastrobar",
    "faqs": [
      {
        "q": "Serve per gastrobar casual, tapas bar tradizionale, pintxos baschi o enoteca con tapas?",
        "a": "Per tutti e quattro. Cucina Spagnola + Ristoranti Casual AI+ coprono dalle tapas tradizionali ai gastrobar contemporanei."
      },
      {
        "q": "Copre vermut, vini e birre con abbinamenti?",
        "a": "Sì. Bar & Lounge AI+ copre vermut, vini spagnoli al calice, birre artigianali e abbinamenti con tapas."
      },
      {
        "q": "Come gestire le perdite su prosciutto e prodotto fresco?",
        "a": "Sprechi GenCal fornisce dati per processo (taglio del prosciutto, acciughe, frutti di mare). Si integrano nella scheda tecnica."
      },
      {
        "q": "Genera contenuti visivi per Instagram?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con la tua tapa reale."
      },
      {
        "q": "Come mi aiuta con eventi privati e degustazioni?",
        "a": "Gastro Calendar pianifica degustazioni con cantine, eventi privati, San Fermín e feste locali."
      }
    ],
    "ctaTitle": "Il tuo gastrobar con margine reale e tecnica autentica.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "IA per Gastrobar: Tapas, Schede e Abbinamenti | AI Chef Pro",
      "description": "Suite IA per gastrobar: Cucina Spagnola, Bar & Lounge AI+, schede tecniche per tapa, vermut e vini al calice. Inizia oggi.",
      "keywords": "IA gastrobar, software tapas bar, schede tecniche tapa, pintxos IA, vermut tapas, gastrobar contemporaneo",
      "ogImage": "https://aichef.pro/og/use-cases/gastrobar-tapas.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Gastrobar dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding di 2 minuti in cui gli racconti che tipo di gastrobar gestisci (gastrobar contemporaneo, tapas bar tradizionale, pintxos baschi, enoteca con tapas), dimensione del team, città e specialità.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Gastrobar",
    "apps": [
      {
        "name": "Cucina Spagnola",
        "description": "Tapas tradizionali, pintxos, porzioni di mercato.",
        "category": "Ricettari Europei"
      },
      {
        "name": "Cucina Creativa",
        "description": "Tapas signature contemporanee con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Vermut, vini spagnoli, birre e abbinamenti.",
        "category": "Concetti di Business"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Consulenza operativa per gastrobar.",
        "category": "Concetti di Business"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con vini e birre per tapas.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture e tecnica avanzata.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi su prosciutto, acciughe, frutti di mare e salumi.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione per tapa: glutine, latticini, crostacei, solfiti.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia artigianale spagnola IA di riferimento.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram per attirare locali e turisti.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti che cercano \"tapas vicino\".",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Giornata della Tapa, San Fermín, feste locali.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo scheda tecnica tapas"
      },
      {
        "value": "+15 %",
        "label": "scontrino medio in 4 mesi"
      },
      {
        "value": "×2",
        "label": "cattura locale con MenuDish"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo gastrobar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Tapas signature improvvisate senza scheda tecnica",
        "Abbinamenti con vini senza base scientifica",
        "Perdite su prosciutto e prodotto fresco senza tracciabilità",
        "Instagram improvvisato",
        "Cattura locale senza SEO"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Tapas signature con scheda tecnica professionale",
        "Abbinamenti con Bar & Lounge AI+ e Food Pairing AI",
        "Perdite controllate con Sprechi GenCal",
        "GastroIMG Gen+ + InstaFlow artigianale",
        "MenuDish Local SEO cattura \"tapas vicino\""
      ]
    },
    "galleryTitle": "Come Funziona un Gastrobar",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: tapas, vermut, prosciutto, vini e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-gastrobar-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-tapas.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-vermut.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-jamon.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-vinos.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastrobar-team.jpg"
    ]
  },
  "gerente-restaurante": {
    "h1": "IA per Manager e Gestori di Ristorante",
    "heroSubtitle": "Ottimizza le operazioni quotidiane, controlla i costi e recupera ore di lavoro amministrativo con una suite di agenti IA pensati per la giornata tipo del manager di ristorante.",
    "heroTagline": "Più controllo operativo, meno fogli sparsi",
    "badge": "Per manager e gestori",
    "painsTitle": "Quello che un Manager di Ristorante Non Può Lasciare Irrisolto",
    "pains": [
      "Organizzare i turni ogni settimana rispettando il contratto collettivo, l'orario legale e i riposi senza errori né costi extra",
      "Controllare sprechi, inventario e acquisti con fornitori diversi che cambiano prezzo ogni settimana",
      "Mantenere l'HACCP aggiornato e preparare le ispezioni senza stress né accumulo di scartoffie",
      "Riportare al proprietario con dati consolidati e dashboard professionali, non in Excel improvvisati",
      "Coordinare il team di cucina e sala con comunicazione chiara e formazione rapida del nuovo personale",
      "Gestire l'operatività dei picchi di servizio senza perdere qualità né trascurare la sala"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Manager",
    "features": [
      {
        "title": "Manager Ristorante Pro",
        "description": "Agente specializzato per supportarti nelle decisioni operative, nella gestione del team e nel reporting al proprietario.",
        "icon": "BriefcaseBusiness"
      },
      {
        "title": "Turni e controllo orari",
        "description": "Kit Gestione Personale: turni in pochi minuti rispettando il contratto collettivo, controllo ore, indici di produttività.",
        "icon": "Calendar"
      },
      {
        "title": "Inventario e controllo acquisti",
        "description": "Kit Inventario: modelli Excel pronti, avvisi di scorta minima, confronto fornitori e sprechi.",
        "icon": "Package"
      },
      {
        "title": "HACCP e tracciabilità",
        "description": "Pack HACCP con 17 registri, avvisi di temperatura da mobile ed esportazione pronta per l'ispezione.",
        "icon": "ShieldCheck"
      },
      {
        "title": "KPI e reporting al proprietario",
        "description": "Indici di cucina e sala, produttività, scontrino medio. Dashboard esportabili in PDF direttamente da Excel.",
        "icon": "BarChart3"
      },
      {
        "title": "Attività ricorrenti per turno",
        "description": "Modelli pronti per tipologia: apertura, chiusura, mise en place e servizio in un unico kit per tipo di attività.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pasto del Personale",
        "description": "Generatore di menu per lo staff che risparmia costi mantenendo il team motivato e ben nutrito.",
        "icon": "Users"
      },
      {
        "title": "Mental Coach",
        "description": "Coaching psicologico per gestire conversazioni difficili, stress e motivazione del team.",
        "icon": "MessageSquare"
      },
      {
        "title": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per piatto, pronta per la normativa e per la sala.",
        "icon": "ShieldCheck"
      }
    ],
    "workflowTitle": "Una Giornata Tipo di un Manager con AI Chef Pro",
    "workflow": [
      "08:30 · Apertura — stampi la checklist del turno dal Kit Attività e controlli l'inventario in 10 minuti.",
      "09:30 · Manager Ristorante Pro — l'agente ti riassume le criticità del giorno precedente e le azioni in sospeso.",
      "10:30 · Kit Inventario — validi gli ordini ai fornitori con confronto prezzi e avvisi di scorta minima.",
      "12:30 · Servizio di mezzogiorno — il team registra sprechi e temperature dal mobile con il Pack HACCP.",
      "15:30 · Turni della prossima settimana — apri il Kit Gestione Personale e chiudi i turni in 20 minuti rispettando il contratto collettivo.",
      "17:00 · Pasto del Personale — generi il menu dello staff per la prossima settimana con ingredienti che hai già in dispensa.",
      "19:00 · Conversazione difficile — usi Mental Coach per preparare il colloquio con un cuoco che arriva in ritardo ripetutamente.",
      "23:30 · Chiusura — generi il report giornaliero con gli indici e lo invii al proprietario via WhatsApp con un tocco."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Manager",
    "productIds": [
      "kit-gestion-personal",
      "kit-inventario",
      "pack-appcc",
      "kit-tareas",
      "kit-escandallos",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Prima passavo 8 ore a settimana solo a organizzare turni e ordini ai fornitori. Ora chiudo tutto in 2 ore con il Kit Gestione Personale e il Kit Inventario. AI Chef Pro mi ha restituito tempo per stare in sala con il team, che è dove un manager deve stare.",
    "testimonialAuthor": "Marta Ruiz",
    "testimonialRole": "Manager, ristorante casual da 80 coperti",
    "faqTitle": "Domande Frequenti dei Manager",
    "faqs": [
      {
        "q": "Funziona se gestisco un solo locale o se ne ho più?",
        "a": "In entrambi i casi. I modelli si adattano al volume e puoi consolidare il reporting di più locali in un'unica dashboard. Ci sono clienti con 1 locale e altri con più di 10 unità attive."
      },
      {
        "q": "Sostituisce il software di prenotazione o il POS?",
        "a": "No, lo integra. Cover Manager o The Fork gestiscono le prenotazioni e il POS gestisce le vendite; AI Chef Pro gestisce costi, personale, HACCP, inventario e operatività interna. I dati sono perfettamente compatibili via Excel."
      },
      {
        "q": "Il team ha bisogno di formazione?",
        "a": "Minima. I modelli e gli agenti sono in italiano e tutto parte con l'agente «Chi sono?», che adatta il sistema a te in 2 minuti. La curva reale del team è di 1-2 giorni con l'onboarding video e supporto via WhatsApp."
      },
      {
        "q": "Posso esportare i dati per il mio commercialista o il proprietario?",
        "a": "Sì. Tutto si esporta in Excel e PDF in formato professionale. I commercialisti ricevono documentazione pulita e i proprietari ricevono dashboard con KPI chiari direttamente su WhatsApp."
      },
      {
        "q": "Come mi aiuta con le conversazioni difficili del team?",
        "a": "Mental Coach è un agente di coaching psicologico per operatori della ristorazione che ti aiuta a strutturare conversazioni difficili (licenziamenti, ritardi, conflitti tra cucina e sala) con argomenti e struttura chiara prima del colloquio."
      },
      {
        "q": "Ci sono modelli specifici per tipologia di attività?",
        "a": "Sì. Ci sono Kit Attività specifici per casual, caffetteria, pizzeria, hamburgheria, dark kitchen, pasticceria, bar, catering, hotel, gelateria, cioccolateria, ristorante creativo e chef privato. Ognuno con modelli adattati all'operatività reale."
      }
    ],
    "ctaTitle": "Porta l'operatività del tuo ristorante al livello successivo.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Manager: Turni, HACCP e Reporting | AI Chef Pro",
      "description": "Suite di IA per manager di ristorante: turni, inventario, HACCP, KPI e reporting al proprietario con agenti specializzati nella ristorazione. Inizia oggi.",
      "keywords": "IA manager ristorante, manager ristorante IA, software manager ristorante, gestione operativa ristorante IA, turni ristorante, HACCP manager, KPI ristorante, agente IA ristorazione, manager ristorante Italia",
      "ogImage": "https://aichef.pro/og/use-cases/gerente-restaurante.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Ristorante dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di ristorante gestisci, in quale città, quanti coperti servi e come lavori. Da quel momento, ogni agente —dai turni al reporting— risponde adattato al tuo contesto: contratto collettivo del paese, dimensione del team, picchi di servizio reali. Non è un modulo: è una conversazione breve che rende la suite davvero utile per la tua giornata da manager.",
    "appsTitle": "Gli Agenti IA che Userai come Manager",
    "apps": [
      {
        "name": "Manager Ristorante Pro",
        "description": "Agente principale: decisioni operative, gestione del team e reporting al proprietario.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Specialista in bistrot, gastropub, tapas e mediterraneo: lo spettro casual completo.",
        "category": "Concetti di Business"
      },
      {
        "name": "Pasto del Personale",
        "description": "Generatore di menu per lo staff che risparmia costi e motiva il team.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi su sprechi e rese per ingrediente, essenziali per il controllo di cucina.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta e piatto.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Conversor Ing",
        "description": "Convertitore di pesi e misure per cucina professionale.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Calcula Pax",
        "description": "Calcolatrice di porzioni che scala le ricette a qualsiasi numero di coperti.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching psicologico per operatori della ristorazione: stress, conversazioni difficili e motivazione del team.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Descrizioni dei piatti ottimizzate per la SEO locale su Google e sul sito del ristorante.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Calendario gastronomico con date chiave, idee e hashtag per social e blog.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di piatti professionali con ricetta + scheda tecnica CSV da caricare nel Kit Escandallos Pro.",
        "category": "Creatività Culinaria"
      }
    ],
    "metrics": [
      {
        "value": "−75 %",
        "label": "tempo in turni e ordini"
      },
      {
        "value": "×4",
        "label": "velocità di reporting al proprietario"
      },
      {
        "value": "−40 %",
        "label": "sprechi dopo controllo sistematico"
      },
      {
        "value": "11+",
        "label": "agenti IA per il tuo ruolo"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "8 ore settimanali a organizzare turni in Excel manuale e note dei fornitori",
        "HACCP su carta stampata che si perde o arriva incompleto all'ispezione",
        "Reporting al proprietario in file sparsi via email senza struttura",
        "Sprechi registrati a occhio, senza tracciabilità reale né avvisi",
        "Pasto del personale improvvisato che fa lievitare i costi senza che nessuno se ne accorga"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "2 ore settimanali per chiudere i turni con modello professionale rispettando il contratto collettivo",
        "HACCP da mobile con registri, temperature e avvisi pronto per l'ispezione",
        "Reporting al proprietario in PDF diretto dal Kit Plan Financiero, con dashboard chiare",
        "Controllo sistematico degli sprechi con dati precisi e avvisi di scorta",
        "Pasto del personale generato con IA rispettando il costo obiettivo e la motivazione del team"
      ]
    },
    "galleryTitle": "La Giornata Tipo di un Manager, in Immagini",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: pianificazione turni, gestione di cucina e sala, inventario, servizio e reporting.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-shifts.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-kitchen.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-inventory.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-service.jpg",
      "/lovable-uploads/ai-gallery/use-case-gerente-restaurante-reporting.jpg"
    ]
  },
  "hamburgueseria": {
    "h1": "IA per Hamburgeria",
    "heroSubtitle": "Scheda tecnica per burger, controlla il costo di carne e pane, gestisci delivery e multi-marca con una suite di agenti IA specializzati in smash burger gourmet, fast casual e dark kitchen di hamburger.",
    "heroTagline": "Burger con margine reale, non intuizione",
    "badge": "Per hamburgerie e burger shop",
    "painsTitle": "Ciò che una Hamburgeria Non Può Non Risolvere",
    "pains": [
      "Carne e pane: ingredienti chiave con costo volatile che cambia ogni settimana",
      "Perdite in cottura della carne, assemblaggio e confezionamento per il delivery",
      "Delivery con altissima rotazione e picchi brutali in ore specifiche",
      "Menu ampio con molte varianti di burger (classica, gourmet, smash, plant-based)",
      "Differenziarsi in un mercato saturo di burger shop con SEO locale e social",
      "Standardizzare la tecnica di piastra e assemblaggio quando il team ruota"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in una Hamburgeria",
    "features": [
      {
        "title": "Burger Pro AI+",
        "description": "Agente specializzato in hamburgerie: gourmet, smash, fast food, plant-based, artigianale e tematiche.",
        "icon": "Beef"
      },
      {
        "title": "Scheda tecnica per burger",
        "description": "Cucina Creativa consegna ricetta + scheda tecnica CSV; Kit Escandallos Pro lo gestisce con i tuoi prezzi reali (carne, pane, formaggio, topping, salse).",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Hamburguesería",
        "description": "Modelli: prep di salse, mise en place di topping, piastra, assemblaggio, servizio e delivery.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack HACCP + ID Allergeni",
        "description": "Tracciabilità della carne, controllo di cottura, temperatura e allergeni per burger.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gestione multi-piattaforma delivery",
        "description": "Piano finanziario con calcolo del margine dopo commissioni di Glovo, Uber Eats e Just Eat per marca virtuale.",
        "icon": "Truck"
      },
      {
        "title": "VegChef Plant-Based",
        "description": "Per burger vegetali con tecnica nutrizionale: Beyond Meat, Heura, alternative plant-based di qualità.",
        "icon": "Leaf"
      },
      {
        "title": "MenuDish Local SEO + InstaFlow AI Pro",
        "description": "Posizionamento locale su Google e contenuti virali per Instagram, dove i burger shop vendono di più.",
        "icon": "Sparkles"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA critica per Glovo, Uber Eats e Just Eat: migliore foto = più clic e miglior ranking.",
        "icon": "Image"
      },
      {
        "title": "Kit Gestión de Personal",
        "description": "Quadranti per piastra, assemblaggio, sala e delivery con turni rotativi.",
        "icon": "Users"
      }
    ],
    "workflowTitle": "Una Giornata Reale in una Hamburgeria con AI Chef Pro",
    "workflow": [
      "11:00 · Apertura — checklist Kit de Tareas Hamburguesería: prep di salse fatte in casa, mise en place di topping, piastra pronta.",
      "12:00 · Burger Pro AI+ — sviluppi una nuova burger gourmet con formaggio di capra e marmellata di cipolle. Cucina Creativa consegna ricetta + scheda tecnica CSV.",
      "12:30 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali e validi margine al 31% dopo commissione Glovo (29%).",
      "13:00 · Servizio mezzogiorno — piastra attiva, assemblaggio coordinato, delivery in uscita, sala piena.",
      "16:00 · MenuDish Local SEO + GastroIMG Gen+ — aggiorni la nuova burger sulle piattaforme con foto professionale e descrizione ottimizzata.",
      "17:30 · Inventario — verifichi ordini di carne (fornitore locale), pane brioche e formaggio premium.",
      "20:00 · Servizio sera — picco di delivery, assemblaggio a catena, piastra al massimo.",
      "23:30 · Chiusura — pulizia, HACCP firmato, report del giorno e perdite registrate."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Hamburgeria",
    "productIds": [
      "kit-tareas-hamburgueseria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Abbassiamo il food cost dal 36% al 31% in 60 giorni con schede tecniche precise e controllo sistematico delle perdite. L'investimento in AI Chef Pro si è ripagato in una settimana solo con questo. La foto IA per Glovo ha alzato il nostro ranking dalla posizione 8 alla 3.",
    "testimonialAuthor": "Pablo Hernández",
    "testimonialRole": "Proprietario, hamburgeria gourmet con 2 brand in delivery",
    "faqTitle": "Domande Frequenti delle Hamburgerie",
    "faqs": [
      {
        "q": "Funziona per hamburgeria gourmet, smash o casual?",
        "a": "Per tutte. Burger Pro AI+ copre l'intero spettro: gourmet, smash burger, fast food, plant-based e tematiche."
      },
      {
        "q": "Copre delivery oltre al locale?",
        "a": "Sì. Modelli specifici con perdite di delivery, packaging brandizzato, coordinamento con piattaforme e calcolo del margine dopo commissioni."
      },
      {
        "q": "C'è controllo specifico della carne e tracciabilità?",
        "a": "Sì. Pack HACCP con tracciabilità della carne, controllo di cottura al punto, temperatura interna e conservazione."
      },
      {
        "q": "Genera idee di combo e promozioni?",
        "a": "Sì. Gastro Calendar + InstaFlow + Pro Prompts eBook generano combo, offerte per giorni deboli, calendario editoriale e campagne con IA."
      },
      {
        "q": "Serve per aprire un marchio virtuale di burger in dark kitchen?",
        "a": "Sì. Burger Pro AI+ + Ristoranti Casual AI+ + Food Truck AI+ sono combinabili per multi-marca virtuale. C'è un caso reale in /usos/concepto/dark-kitchen."
      }
    ],
    "ctaTitle": "Burger con margine reale, non intuizione.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Hamburgeria: Schede Tecniche, Smash Burger e Delivery",
      "description": "Suite di IA per hamburgerie professionali: Burger Pro AI+, schede tecniche per burger, modelli burger-shop, HACCP e delivery multi-piattaforma. Inizia oggi.",
      "keywords": "IA hamburgeria, schede tecniche burger, software hamburgeria, smash burger IA, gestione burger delivery, hamburgeria gourmet IA, hamburgeria Italia",
      "ogImage": "https://aichef.pro/og/use-cases/hamburgueseria.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Hamburgeria dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di hamburgeria gestisci (gourmet, smash, fast casual, plant-based), numero di coperti, città, piattaforme di delivery e commissioni. Ogni agente —da Burger Pro AI+ fino al Kit Escandallos Pro— risponde adattato al tuo stile e mercato reale.",
    "appsTitle": "Gli Agenti IA che Userai nella Tua Hamburgeria",
    "apps": [
      {
        "name": "Burger Pro AI+",
        "description": "Agente specializzato in hamburgerie: gourmet, smash, fast food, plant-based.",
        "category": "Concetti di Business"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di burger professionali con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "VegChef Plant-Based",
        "description": "Per burger vegetali con tecnica nutrizionale professionale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Truck AI+",
        "description": "Per concept mobili e dark kitchen multi-marca di hamburger.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi sugli sprechi in cottura della carne e assemblaggio.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per burger e salsa.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Descrizioni SEO locale per Glovo, Uber Eats e web.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Post di blog per catturare ricerche locali di hamburger.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Keyword Discovery AI+",
        "description": "Parole chiave per zona postale: «smash burger [il tuo quartiere]».",
        "category": "Contenuti e Social"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Contenuti virali Instagram per hamburgerie.",
        "category": "Contenuti e Social"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA per piattaforme di delivery.",
        "category": "Gastro Conoscenza"
      }
    ],
    "metrics": [
      {
        "value": "−5 pp",
        "label": "food cost in 60 giorni"
      },
      {
        "value": "+5",
        "label": "posizioni in ranking Glovo"
      },
      {
        "value": "×3",
        "label": "velocità di creazione nuova burger"
      },
      {
        "value": "11+",
        "label": "agenti per il tuo burger shop"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Schede tecniche a occhio con grammatura variabile tra cuochi",
        "Food cost al 36% per perdite e assemblaggio senza controllo",
        "Foto su Glovo e Uber Eats di bassa qualità, ranking basso",
        "Perdite di carne e assemblaggio senza tracciabilità",
        "Operativa di delivery improvvisata nelle ore di punta"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Burger Pro AI+ + Cucina Creativa documentano tecnica replicabile",
        "Food cost al 31% con scheda tecnica professionale e perdite controllate",
        "Foto professionali con GastroIMG Gen+ che alzano il ranking sulle piattaforme",
        "Pack HACCP con tracciabilità della carne e perdite registrate",
        "Kit de Tareas Hamburguesería con modelli per delivery e locale"
      ]
    },
    "galleryTitle": "Come Funziona una Hamburgeria Moderna",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: piastra, smash burger, assemblaggio, prep, team e delivery.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-grill.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-burger.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-hamburgueseria-delivery.jpg"
    ]
  },
  "heladeria": {
    "h1": "IA per Gelateria Artigianale",
    "heroSubtitle": "Scheda tecnica per gusto con costo reale di latte, frutta e frutta secca, pianifica la produzione stagionale e cattura un branding professionale con una suite di agenti IA specializzati in gelateria artigianale.",
    "heroTagline": "Gelato con margine reale e senza carta",
    "badge": "Per gelaterie artigianali",
    "painsTitle": "Cosa una Gelateria Artigianale Non Può Evitare di Risolvere",
    "pains": [
      "Schede tecniche complesse con latte, panna, frutta fresca, frutta secca e paste professionali che richiedono calcolo per kg e per pallina",
      "Sprechi elevati in laboratorio (mantecatore, abbattitore) e in vetrina (esposizione prolungata, rotazione) senza controllo reale",
      "Tracciabilità HACCP con prodotti sensibili: latte, uova in alcune basi, frutta secca con allergeni e temperature critiche",
      "Stagionalità estrema: alta stagione da maggio a settembre, valle invernale da rendere redditizia con torte e dessert",
      "Differenziarsi in zona competitiva con gusti propri, branding visivo della vetrina, packaging e social media",
      "Catturare ordini di torte gelato e dessert su misura con margine mentre si gestisce il servizio quotidiano"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta nella Gelateria Artigianale",
    "features": [
      {
        "title": "Gelateria Creativa",
        "description": "Agente specializzato in gelateria artigianale: basi bianca, gialla, frutta, sorbetti, bilanciamento di zuccheri, solidi e grassi per una texture ottimale.",
        "icon": "IceCream"
      },
      {
        "title": "Pasticceria Creativa",
        "description": "Per torte gelato, semifreddi, dessert al cucchiaio e combinazioni gelato + pan di Spagna che alzano lo scontrino medio nella valle invernale.",
        "icon": "Cake"
      },
      {
        "title": "Cioccolateria Creativa",
        "description": "Per coperture, bonbon gelato, praline e combinazioni avanzate gelato + cioccolato.",
        "icon": "Cookie"
      },
      {
        "title": "Schede tecniche per gusto",
        "description": "Gelateria Creativa fornisce ricetta + scheda tecnica CSV con bilanciamento tecnico (zuccheri, solidi, grassi); il Kit Escandallos Pro lo gestisce con margine reale per kg, per pallina e per cono.",
        "icon": "Calculator"
      },
      {
        "title": "Kit di Attività Gelateria",
        "description": "Modelli: preparazione mantecatore, abbattimento, riassortimento vetrina, controllo temperature, rotazione gusti, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pacchetto HACCP gelateria",
        "description": "Tracciabilità di latte, frutta fresca, frutta secca con allergeni e temperature critiche in cella, mantecatore e vetrina.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione stagionale con picchi chiave: Festa della Mamma, primavera, estate, San Valentino e torte gelato di Natale. Calendario editoriale per la vetrina.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia gastronomica IA + contenuti per Instagram: la gelateria artigianale vive dell'impatto visivo di vaschette e coni.",
        "icon": "Image"
      },
      {
        "title": "Sosa Ingredients AI",
        "description": "Assistente del catalogo Sosa per texture professionali, neutri, stabilizzanti e paste concentrate per gelateria.",
        "icon": "BarChart3"
      }
    ],
    "workflowTitle": "Una Giornata Reale in una Gelateria Artigianale con AI Chef Pro",
    "workflow": [
      "07:00 · Apertura — checklist Kit di Attività Gelateria: controllo cella, abbattimento miscele preparate il giorno prima, preparazione mantecatore.",
      "08:30 · Gelateria Creativa — sviluppi un nuovo gusto di stagione (frutti di bosco con balsamico). Cucina Creativa fornisce ricetta + scheda tecnica CSV con bilanciamento tecnico.",
      "09:30 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali di frutta di stagione e latte locale, validi il margine per kg e per pallina.",
      "11:00 · Produzione del giorno — passi le miscele nel mantecatore, abbatti a -18 °C, etichetti con HACCP.",
      "13:30 · Riassortimento vetrina con etichette professionali, controllo sprechi di esposizione per gusto.",
      "16:00 · Pasticceria Creativa — sviluppi una torta gelato per la Festa della Mamma con semifreddo al pistacchio, base di pan di Spagna e copertura. Scheda tecnica CSV pronta.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento del nuovo gusto e i post Instagram per il lancio.",
      "21:00 · Chiusura — pulizia profonda, HACCP firmato, pianificazione miscele da abbattere stasera per domani."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Gelateria",
    "productIds": [
      "kit-tareas-heladeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Siamo passati da fogli sparsi a un sistema. Con Gelateria Creativa bilanciamo zuccheri e solidi con criterio tecnico, e il Kit Escandallos Pro mi conferma il margine reale per pallina e per kg con i prezzi attuali della frutta. Lo spreco è calato del 40% in 3 mesi e abbiamo scoperto che due gusti storici non erano redditizi.",
    "testimonialAuthor": "Laura Costa",
    "testimonialRole": "Titolare, gelateria artigianale con laboratorio proprio",
    "faqTitle": "Domande Frequenti delle Gelaterie",
    "faqs": [
      {
        "q": "Va bene per una piccola gelateria, una gelateria italiana o una catena?",
        "a": "Per tutte e tre. I modelli scalano da gelateria familiare a punto singolo fino a catena con più locali e laboratorio centralizzato. La metodologia è la stessa: ricetta bilanciata → scheda tecnica CSV → margine reale."
      },
      {
        "q": "Copre il bilanciamento tecnico delle basi (zuccheri, solidi, grassi)?",
        "a": "Sì. Gelateria Creativa ragiona come un gelatiere professionista: bilanciamento degli zuccheri con saccarosio, destrosio e zucchero invertito; solidi totali e grassi secondo norma tecnica; equilibrio per evitare cristallizzazione e mantenere cremosità."
      },
      {
        "q": "Come gestiamo la forte stagionalità della gelateria?",
        "a": "Gastro Calendar pianifica in anticipo i picchi (Festa della Mamma, estate, San Valentino, Natale con torte gelato) e la valle invernale con torte, semifreddi e dessert al cucchiaio per mantenere lo scontrino medio. Il Kit Plan Finanziario proietta il cash flow stagionale realistico."
      },
      {
        "q": "C'è controllo degli sprechi in laboratorio e in vetrina?",
        "a": "Sì. Sprechi GenCal fornisce dati per processo (mantecatore, abbattimento, esposizione prolungata in vetrina, rotazione gusti). Si integrano nella scheda tecnica del Kit Escandallos Pro affinché il costo reale rifletta gli sprechi, non solo l'ingrediente lordo."
      },
      {
        "q": "Genera contenuti per vetrina, social e Google Maps?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali di ogni gusto per vetrina, web e social; InstaFlow AI Pro programma Instagram con calendario editoriale; MenuDish Local SEO cattura clienti locali che cercano \"gelateria vicino a me\". Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con la tua vaschetta e il tuo impiattamento reale."
      }
    ],
    "ctaTitle": "La tua gelateria con margine chiaro e branding professionale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Gelateria Artigianale: Schede Tecniche per Gusto, Stagionalità e Branding | AI Chef Pro",
      "description": "Suite IA per gelaterie artigianali: Gelateria Creativa, schede tecniche per gusto con bilanciamento tecnico, HACCP, pianificazione stagionale e branding visivo. Inizia oggi.",
      "keywords": "IA gelateria, software gelateria, schede tecniche gelato, gelateria artigianale IA, bilanciamento tecnico gelato, gelateria IA, gelateria Italia",
      "ogImage": "https://aichef.pro/og/use-cases/heladeria.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Gelateria dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di gelateria gestisci (gelateria italiana, gelateria artigianale spagnola, gelateria con laboratorio proprio o senza, mista con pasticceria), dimensione del team, città e stile. Ogni agente —da Gelateria Creativa a Gastro Calendar— risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nella Tua Gelateria",
    "apps": [
      {
        "name": "Gelateria Creativa",
        "description": "Agente specializzato in gelateria artigianale con bilanciamento tecnico di basi, zuccheri, solidi e grassi.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Torte gelato, semifreddi, dessert al cucchiaio e combinazioni gelato + pan di Spagna.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cioccolateria Creativa",
        "description": "Coperture, bonbon gelato, praline e combinazioni avanzate con cioccolato.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di gusti e ricette con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa: neutri, stabilizzanti, paste concentrate e texture professionali.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi sugli sprechi in mantecatore, abbattimento ed esposizione in vetrina.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per gusto: latticini, frutta secca, glutine, uova.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA di riferimento per vetrina, web e social media.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale: la gelateria vive dell'impatto visivo.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"gelateria vicino a me\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Pianificazione stagionale: Festa della Mamma, estate, San Valentino, torte gelato Natale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico stabile per torte gelato e semifreddi.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo le schede tecniche dei gusti"
      },
      {
        "value": "−40 %",
        "label": "sprechi in laboratorio e vetrina"
      },
      {
        "value": "×3",
        "label": "engagement Instagram con GastroIMG"
      },
      {
        "value": "12+",
        "label": "agenti per la tua gelateria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Schede tecniche senza bilanciamento tecnico, gusti che cristallizzano o perdono cremosità senza sapere perché",
        "Sprechi in mantecatore, abbattimento e vetrina senza tracciabilità reale",
        "Vetrina e social improvvisati: foto dal telefono, senza continuità",
        "Stagionalità reattiva: l'inverno affonda lo scontrino senza alternative",
        "HACCP su carta stampata sparsa per il laboratorio"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Schede tecniche professionali per gusto con bilanciamento tecnico e margine reale per pallina e per kg",
        "Sprechi controllati con Sprechi GenCal e modelli specifici per gelateria",
        "GastroIMG Gen+ + InstaFlow AI Pro generano contenuto visivo stabile e professionale",
        "Gastro Calendar pianifica picchi e valli con torte gelato, semifreddi e dessert al cucchiaio",
        "HACCP da mobile con registri pronti per l'ispezione"
      ]
    },
    "galleryTitle": "Come Funziona una Gelateria Artigianale",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: vetrina, mantecatore, laboratorio, gusti, coni e team. Immagini generate con IA come riferimento visivo del concept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-heladeria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-vitrine.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-mantecadora.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-flavors.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-conos.jpg",
      "/lovable-uploads/ai-gallery/use-case-heladeria-team.jpg"
    ]
  },
  "hotel-completo": {
    "h1": "IA per Hotel Completo (F&B + Housekeeping)",
    "heroSubtitle": "Gestisci colazioni, ristorante, room service, banchetti, bar e housekeeping con una suite di agenti IA pensati per F&B Manager e direzioni alberghiere.",
    "heroTagline": "Tutta l'operatività alberghiera coordinata in un unico sistema",
    "badge": "Per F&B Manager di hotel",
    "painsTitle": "I problemi che un F&B Manager di hotel non può lasciare irrisolti",
    "pains": [
      "Coordinare più punti vendita contemporaneamente: colazione a buffet, ristorante à la carte, bar lobby, room service e banchetti",
      "Gestire team numerosi con turni rotativi 24/7 rispettando CCNL e riposi",
      "Mantenere l'HACCP distribuito in più aree di cucina con consolidamento al F&B Director",
      "Reporting consolidato al direttore dell'hotel e alla corporate con KPI per linea di F&B",
      "Progettare menu stagionali per più outlet senza che il team affoghi nella burocrazia",
      "Gestire banchetti di matrimoni ed eventi aziendali coordinandoli con il F&B regolare"
    ],
    "featuresTitle": "Come AI Chef Pro aiuta in un hotel completo",
    "features": [
      {
        "title": "Kit de Tareas Hotel",
        "description": "Modelli specifici per colazione a buffet, ristorante, bar lobby, room service, banchetti e housekeeping in un unico sistema documentale.",
        "icon": "Hotel"
      },
      {
        "title": "Chef Esecutivo Pro",
        "description": "Standardizzazione di ricette e schede tecniche in tutti gli outlet dell'hotel. Stesso piatto, stessa qualità in ristorante, room service e banchetto.",
        "icon": "ChefHat"
      },
      {
        "title": "Food cost per punto vendita",
        "description": "Cucina Creativa consegna ricetta + scheda tecnica CSV; il Kit Escandallos Pro la gestisce con i tuoi prezzi reali separando il margine per outlet.",
        "icon": "Calculator"
      },
      {
        "title": "Catering AI+",
        "description": "Per la progettazione e produzione di banchetti di matrimonio, eventi aziendali e eventi speciali dell'hotel.",
        "icon": "PartyPopper"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Per la cocktaileria del bar lobby, vini del ristorante e spirits con scheda tecnica professionale.",
        "icon": "Wine"
      },
      {
        "title": "Kit Gestión de Personal",
        "description": "Quadranti per team numerosi 24/7 con turni rotativi rispettando il CCNL. Pasto del Personale incluso.",
        "icon": "Users"
      },
      {
        "title": "Pack APPCC aziendale",
        "description": "HACCP distribuito per area di cucina ma consolidato in un unico dashboard per il F&B Director.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Kit Plan Financiero",
        "description": "Dashboard con KPI per punto vendita: colazione, ristorante, bar, room service, banchetti. Indici di occupazione e produttività.",
        "icon": "BarChart3"
      },
      {
        "title": "Manager Ristorante Pro",
        "description": "Per i manager di ogni outlet con reporting consolidato verso il F&B Manager dell'hotel.",
        "icon": "BriefcaseBusiness"
      }
    ],
    "workflowTitle": "Una giornata tipo di un F&B Manager di hotel con AI Chef Pro",
    "workflow": [
      "07:00 · Apertura colazione — il team avvia il buffet con la checklist del Kit de Tareas Hotel; tu controlli il dashboard di occupazione dell'hotel e regoli la mise en place.",
      "09:30 · Catering AI+ — prepari il banchetto di matrimonio del prossimo sabato: menu, scheda tecnica e produzione per 220 invitati.",
      "11:00 · Chef Esecutivo Pro — aggiorni la scheda tecnica del nuovo piatto del ristorante e si replica al room service e al menu del banchetto con la stessa standardizzazione.",
      "13:00 · Servizio di mezzogiorno — ristorante à la carte + bar lobby + room service attivi. Il team coordina con modelli specifici di ogni outlet.",
      "15:30 · Kit Plan Financiero — esporti i KPI per outlet del trimestre per la riunione con la direzione dell'hotel.",
      "17:00 · Bar & Lounge AI+ — progetti la nuova carta dei cocktail per il bar lobby con scheda tecnica professionale.",
      "19:30 · Quadrante settimana prossima — Kit Gestión de Personal con turni rotativi rispettando il CCNL, controllo ore e pasto del personale generato.",
      "23:00 · HACCP consolidato — registri dei 6 punti vendita firmati ed esportati, report al F&B Director e alla corporate inviato in PDF."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Hotel",
    "productIds": [
      "kit-tareas-hotel",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Coordinare 6 punti vendita di F&B in un hotel di 200 camere era un incubo costante. AI Chef Pro ci ha messo tutto in ordine. Il Kit de Tareas Hotel è oro e il reporting al direttore dell'hotel è ora automatico in PDF. Abbiamo aumentato il RevPASH del ristorante del 12% in 4 mesi solo per avere un controllo migliore.",
    "testimonialAuthor": "Cristina Núñez",
    "testimonialRole": "F&B Manager, hotel 4 stelle con 200 camere",
    "faqTitle": "Domande Frequenti dei F&B Manager",
    "faqs": [
      {
        "q": "Funziona per hotel boutique o grande catena?",
        "a": "Entrambi. I modelli scalano da hotel di 30 camere fino a catene con centinaia di proprietà. C'è onboarding aziendale per le grandi catene."
      },
      {
        "q": "Copre il housekeeping oltre al F&B?",
        "a": "Sì. Il Kit de Tareas Hotel include modelli specifici per il housekeeping oltre ai 5 punti vendita di F&B."
      },
      {
        "q": "Si integra con il nostro PMS o Opera?",
        "a": "Esporta Excel, PDF e CSV compatibili con la maggior parte dei PMS e sistemi alberghieri. I dati possono essere integrati manualmente alla chiusura di ogni turno o giornata."
      },
      {
        "q": "Esiste un piano aziendale per catene alberghiere?",
        "a": "Sì. A partire da un certo numero di proprietà ci sono piani aziendali con onboarding personalizzato, dashboard consolidati per catena e supporto prioritario."
      },
      {
        "q": "Come gestisce i banchetti e gli eventi speciali?",
        "a": "Catering AI+ è integrato con il Kit Tareas Hotel affinché i banchetti (matrimoni, eventi aziendali) si concilino con il F&B regolare senza far collidere produzione né team."
      },
      {
        "q": "E il controllo dei costi per outlet?",
        "a": "Il Kit Plan Financiero permette di analizzare food cost, produttività e margine separatamente per colazione, ristorante, bar lobby, room service e banchetti. Questo dà una visione reale di quale outlet rende e quale no."
      }
    ],
    "ctaTitle": "Il tuo F&B di hotel coordinato e senza caos.",
    "ctaSubtitle": "Parla con noi per un onboarding personalizzato per il tuo gruppo o inizia con il piano Membro: 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "IA per Hotel: F&B, Housekeeping, Banchetti | AI Chef Pro",
      "description": "Suite di IA per F&B Manager di hotel: colazione a buffet, ristorante, bar lobby, room service, banchetti e housekeeping con agenti specializzati. Inizia oggi.",
      "keywords": "IA hotel F&B, F&B Manager IA, software F&B hotel, gestione hotel IA, room service IA, banchetto hotel IA, housekeeping software, gestione ristorante hotel IA, F&B Italia",
      "ogImage": "https://aichef.pro/og/use-cases/hotel-completo.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Hotel dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di hotel gestisci (boutique, 4 stelle, grande catena, tutto incluso), numero di camere, quali outlet di F&B gestisci e a che scala. Da quel momento, ogni agente —da Chef Esecutivo Pro al Plan Financiero— risponde adattato alla realtà del tuo hotel: tipo di ospite, tasso di occupazione e operatività reale. Non è un modulo: è una conversazione breve che rende la suite davvero utile per un F&B Manager di hotel.",
    "appsTitle": "Gli Agenti IA che Userai come F&B Manager",
    "apps": [
      {
        "name": "Chef Esecutivo Pro",
        "description": "Standardizzazione di ricette e schede tecniche in tutti gli outlet dell'hotel.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Manager Ristorante Pro",
        "description": "Assistente per i manager di ogni outlet con reporting consolidato al F&B Manager.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Catering AI+",
        "description": "Per banchetti di matrimonio, eventi aziendali e galà dell'hotel.",
        "category": "Concetti di Business"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Per la cocktaileria del bar lobby, vini del ristorante e spirits.",
        "category": "Concetti di Business"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Per il ristorante à la carte dell'hotel e le opzioni casual del room service.",
        "category": "Concetti di Business"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di piatti per tutti gli outlet con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dolci per hotel: colazione a buffet, ristorante, room service e banchetti.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasto del Personale",
        "description": "Generatore di menu per lo staff per team numerosi 24/7.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta, critica negli hotel internazionali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi su sprechi e rese per il controllo multi-outlet.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica per il sito web dell'hotel, menu del room service e banchetti.",
        "category": "Gastro Conoscenza"
      }
    ],
    "metrics": [
      {
        "value": "+12 %",
        "label": "RevPASH in 4 mesi"
      },
      {
        "value": "6",
        "label": "punti vendita coordinati"
      },
      {
        "value": "×5",
        "label": "velocità di reporting al direttore"
      },
      {
        "value": "11+",
        "label": "agenti per il tuo hotel"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "6 outlet di F&B con 6 sistemi diversi: colazione, ristorante, bar, room service, banchetti e housekeeping scollegati",
        "HACCP su carta stampata disperso in ogni cucina dell'hotel, problema nelle ispezioni",
        "I banchetti di matrimonio collidono con la produzione del ristorante regolare e del room service",
        "Reporting al F&B Director e alla corporate con file sparsi e senza struttura",
        "Quadranti 24/7 fatti a mano in Excel con 50+ dipendenti"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Kit de Tareas Hotel con modelli specifici per outlet, tutto coordinato in un unico sistema",
        "HACCP consolidato in dashboard: registri da mobile, pronto per ispezione e per la corporate",
        "Banchetti integrati con Catering AI+ che rispetta la produzione del F&B regolare",
        "Reporting al direttore e alla corporate in PDF diretto dal Kit Plan Financiero",
        "Quadranti con Kit Gestión de Personal: turni 24/7 rispettando il CCNL senza sforamenti"
      ]
    },
    "galleryTitle": "Come Funziona il F&B di un Hotel Completo",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: ristorante, colazione a buffet, banchetto, bar lobby, room service e briefing F&B con cucina.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-breakfast.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-banquet.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-bar.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-roomservice.jpg",
      "/lovable-uploads/ai-gallery/use-case-hotel-completo-fbteam.jpg"
    ]
  },
  "maestro-asador": {
    "h1": "IA per Maestro Brasaiolo e Grigliatore",
    "heroSubtitle": "Domina la tecnica delle braci, la scomposizione dei tagli e il dry-aged con scheda tecnica professionale per taglio, pianifica la produzione di proteine e cattura un branding fire-driven con una suite di agenti IA gastronomica specializzati in cucina al fuoco professionale.",
    "heroTagline": "Braci con tecnica autentica e margine reale",
    "badge": "Per maestri brasaioli, grigliatori e grillmaster",
    "painsTitle": "Cosa un Maestro Brasaiolo Non Può Lasciare Irrisolto",
    "pains": [
      "Standardizzare il punto di cottura e la tecnica delle braci turno dopo turno (carbone vegetale, legna, marezzatura, temperatura interna)",
      "Scomposizione rigorosa con costo al chilo e resa per taglio (chuletón, picanha, T-bone, lombo)",
      "Gestione del dry-aged con camera, umidità, temperatura, rotazione e calo settimanale documentato",
      "Coordinare la griglia con la cucina principale nei picchi di servizio senza perdere qualità né timing",
      "Storytelling dei fornitori di carne, razza, alimentazione e maturazione per la sala",
      "Formare il team di grigliatori junior con criterio tecnico e costanza nel punto di cottura"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Maestro Brasaiolo",
    "features": [
      {
        "title": "Cucina Creativa",
        "description": "Per lo sviluppo tecnico di tagli signature, marinature, salse e contorni da braseria.",
        "icon": "Flame"
      },
      {
        "title": "Cucina Argentina + Brasiliana",
        "description": "Ricettari specializzati: parrilla, chimichurri, picanha, churrasco, tecnica autentica.",
        "icon": "UtensilsCrossed"
      },
      {
        "title": "Schede tecniche per taglio con dry-aged",
        "description": "Ricetta + scheda tecnica CSV con calo del dry-aged integrato e costo ora della griglia. Margine reale per taglio.",
        "icon": "Calculator"
      },
      {
        "title": "Sprechi GenCal",
        "description": "Dati per processo: scomposizione, dry-aging settimanale, trimming, calo di cottura.",
        "icon": "BarChart3"
      },
      {
        "title": "Kit di Attività Ristorante Casual",
        "description": "Template: accensione braci, scomposizione, controllo camera dry-aged, mise, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pacchetto HACCP braseria",
        "description": "Tracciabilità della carne, dry-aging, temperatura interna e conservazione.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Abbinamenti con rossi potenti per i nuovi tagli signature.",
        "icon": "Wine"
      },
      {
        "title": "Gastro Calendar",
        "description": "Festa del Papà, Natale, eventi aziendali e lanci di stagione.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia premium IA di riferimento + Instagram con storytelling del fornitore di carne.",
        "icon": "Image"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Maestro Brasaiolo con AI Chef Pro",
    "workflow": [
      "09:00 · Apertura — checklist Kit di Attività: accensione controllata delle braci (3 ore per arrivare a punto), controllo camera dry-aged.",
      "11:00 · Cucina Creativa + Cucina Argentina — sviluppi un nuovo taglio signature di chuletón galiziano dry-aged 60 giorni con sale Maldon affumicato e chimichurri. Ricetta + scheda tecnica CSV.",
      "12:00 · Kit Schede Tecniche Pro — carichi il CSV con i tuoi prezzi reali della carne e il calo del dry-aged, validi il margine reale per taglio.",
      "13:00 · Servizio di mezzogiorno — griglia a pieno regime con tagli premium, mise di chimichurri e contorni.",
      "17:00 · Briefing al team — formazione dei grigliatori junior con criterio tecnico sul punto di cottura.",
      "20:00 · Servizio cena — picchi coordinati, griglia con più tagli simultanei.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento del nuovo chuletón e i post per Instagram.",
      "00:00 · Chiusura — pulizia profonda delle griglie, HACCP firmato, controllo camera dry-aged."
    ],
    "productsTitle": "Template e Kit Consigliati per Maestro Brasaiolo",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cucina Argentina + Cucina Creativa mi hanno alzato il livello. Il mio team ora replica il punto di cottura con criterio tecnico documentato, le schede tecniche dei tagli premium riflettono il calo del dry-aged e abbiamo alzato il margine di 5 punti. La pianificazione della Festa del Papà con Gastro Calendar ci ha triplicato il fatturato.",
    "testimonialAuthor": "Pedro Aguirre",
    "testimonialRole": "Maestro brasaiolo, braseria premium con dry-aged",
    "faqTitle": "Domande Frequenti dei Maestri Brasaioli",
    "faqs": [
      {
        "q": "Va bene per parrilla argentina, churrascaria, braseria premium o steakhouse?",
        "a": "Per tutti e quattro. Cucina Argentina + Cucina Brasiliana + Cucina Creativa coprono dalla parrilla tradizionale alla steakhouse con dry-aged."
      },
      {
        "q": "Copre il dry-aged e la gestione della camera?",
        "a": "Sì. Ragiona come un maestro brasaiolo professionista: condizioni della camera, tempi per taglio, controllo del calo settimanale e rotazione."
      },
      {
        "q": "Come gestisco il costo volatile della carne?",
        "a": "Kit Schede Tecniche Pro ricalcola il margine all'istante. Sprechi GenCal aggiunge il costo degli scarti per dry-aging, scomposizione e trimming."
      },
      {
        "q": "Genera contenuti visivi per Instagram?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali di tagli e braci. Ricorda che l'immagine IA è un riferimento visivo: la foto definitiva la fai tu con il tuo taglio reale."
      },
      {
        "q": "Come mi aiuta con gli eventi aziendali?",
        "a": "Gastro Calendar pianifica Festa del Papà, Natale, eventi aziendali e lanci di tagli di stagione."
      }
    ],
    "ctaTitle": "La tua griglia con tecnica del fuoco e margine reale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Maestro Brasaiolo e Grigliatore: Tagli, Braci e Dry-Aged | AI Chef Pro",
      "description": "Suite IA per maestri brasaioli: Cucina Argentina + Brasiliana, schede tecniche per taglio, dry-aged, branding e HACCP. Inizia oggi.",
      "keywords": "IA maestro brasaiolo, IA grigliatore, software braseria, schede tecniche chuletón, dry-aged, tecnica braci, parrilla argentina IA",
      "ogImage": "https://aichef.pro/og/use-cases/maestro-asador-parrillero.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Griglia dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding di 2 minuti in cui racconti che tipo di griglia dirigi (parrilla argentina, churrascaria brasiliana, steakhouse premium con dry-aged, braseria casual di quartiere), dimensione del team, città e specialità. Ogni agente risponde adattato alla tua griglia e alla tua operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai come Maestro Brasaiolo",
    "apps": [
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di tagli signature con tecnica delle braci e contorni.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Argentina",
        "description": "Asado, chimichurri, mollejas e tecnica di parrilla autentica.",
        "category": "Ricettari Latinoamericani"
      },
      {
        "name": "Cucina Brasiliana",
        "description": "Picanha, churrasco, farofa e tecnica di churrascaria.",
        "category": "Ricettari Latinoamericani"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con rossi potenti e cocktail di carattere.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Per il bancone della braseria con vini rossi premium.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Cali in scomposizione, dry-aging, trimming e cottura.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica per taglio e contorno.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia premium IA di riferimento per Instagram, web e menu.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale fire-driven.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti che cercano \"braseria vicino a me\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Festa del Papà, Natale, eventi aziendali.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching per la leadership del team e i picchi di servizio.",
        "category": "Strumenti e Utility"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo le schede tecniche dei tagli"
      },
      {
        "value": "×3",
        "label": "fatturato alla Festa del Papà"
      },
      {
        "value": "−15 %",
        "label": "cali in scomposizione e dry-aging"
      },
      {
        "value": "12+",
        "label": "agenti per la tua griglia"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Punto di cottura improvvisato tra i grigliatori",
        "Schede tecniche senza calo del dry-aged",
        "Camera dry-aged senza tracciabilità",
        "Briefing improvvisato, formazione variabile",
        "Instagram senza storytelling del fornitore di carne"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Punto di cottura costante con criterio tecnico",
        "Scheda tecnica professionale con calo del dry-aged integrato",
        "Camera con tracciabilità HACCP documentata",
        "Briefing giornaliero professionale, formazione costante",
        "GastroIMG Gen+ + storytelling del fornitore di carne"
      ]
    },
    "galleryTitle": "Come Funziona la Griglia di un Maestro Brasaiolo",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: braci, scomposizione, tagli, chimichurri e team. Immagini generate con IA come riferimento visivo del concept.",
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
    "h1": "IA per Maestro Gelatiere",
    "heroSubtitle": "Domina il bilanciamento tecnico delle basi, scheda tecnica per gusto con costo reale, pianifica la produzione stagionale e cattura il branding artigianale con una suite di agenti di IA gastronomica specializzati in gelateria professionale.",
    "heroTagline": "Gelato con tecnica autentica e margine reale",
    "badge": "Per maestri gelatieri e artigiani del gelato",
    "painsTitle": "Quello che un Maestro Gelatiere non può non risolvere",
    "pains": [
      "Bilanciamento tecnico impegnativo: equilibrio degli zuccheri (saccarosio, destrosio, zucchero invertito), solidi totali e grassi per una texture ottimale",
      "Perdite in mantecatore, abbattimento e vetrina con prodotto sensibile alla temperatura",
      "Stagionalità estrema: alta stagione estiva, valle invernale da rendere redditizia con torte gelato e semifreddi",
      "Standardizzare la produzione di basi (bianca, gialla, frutta, sorbetto) turno per turno con criterio tecnico",
      "Differenziarsi in zona competitiva con gusti propri, ingredienti premium (Sosa, Pistacchio di Bronte) e branding visivo",
      "Formare il team sulla tecnica professionale di bilanciamento e cristallizzazione"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Maestro Gelatiere",
    "features": [
      {
        "title": "Gelateria Creativa",
        "description": "Agente specializzato in gelateria artigianale professionale: basi bianca, gialla, frutta, sorbetti, bilanciamento tecnico degli zuccheri.",
        "icon": "IceCream"
      },
      {
        "title": "Pasticceria Creativa",
        "description": "Per torte gelato, semifreddi, dessert al cucchiaio che rendono redditizia la valle invernale.",
        "icon": "Cake"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per lo sviluppo di gusti signature, fusioni controllate e presentazioni d'autore.",
        "icon": "Sparkles"
      },
      {
        "title": "Scheda tecnica per gusto",
        "description": "Gelateria Creativa fornisce ricetta + scheda tecnica CSV con bilanciamento tecnico; Kit de Escandallos Pro lo gestisce con margine reale per kg, per pallina e per cono.",
        "icon": "Calculator"
      },
      {
        "title": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture professionali, neutri, stabilizzanti e paste concentrate.",
        "icon": "Beaker"
      },
      {
        "title": "Kit de Tareas Heladería",
        "description": "Modelli: preparazione mantecatore, abbattimento, rifornimento vetrina, controllo temperature, rotazione.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC gelateria",
        "description": "Tracciabilità di latte, frutta fresca, frutta secca e temperature critiche.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Festa della Mamma, primavera, estate, San Valentino, torte gelato di Natale.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia artigianale IA di riferimento + Instagram per attirare clienti locali.",
        "icon": "Image"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Maestro Gelatiere con AI Chef Pro",
    "workflow": [
      "07:00 · Apertura — checklist Kit di Attività: revisione della cella, abbattimento delle miscele preparate il giorno prima.",
      "08:30 · Gelateria Creativa — sviluppi un nuovo gusto signature di pistacchio di Bronte con sale Maldon. Cucina Creativa fornisce ricetta + scheda tecnica CSV.",
      "09:30 · Sosa Ingredients AI — selezioni pasta concentrata e neutro adeguati.",
      "10:00 · Kit de Escandallos Pro — carichi CSV con i tuoi prezzi reali di pistacchio premium e latte, validi il margine per pallina e per kg.",
      "11:00 · Produzione del giorno — passi le miscele nel mantecatore, abbatti a -18 °C.",
      "13:30 · Rifornimento vetrina con etichette e controllo delle perdite di esposizione.",
      "16:00 · Pasticceria Creativa — sviluppi una torta gelato per la Festa della Mamma con semifreddo al pistacchio.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi immagine di riferimento del nuovo gusto + post."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Maestro Gelatiere",
    "productIds": [
      "kit-tareas-heladeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Gelateria Creativa ci ha cambiato la cucina. Abbiamo bilanciato zuccheri e solidi con criterio tecnico, le schede tecniche per pallina con pistacchio premium riflettono margine reale. Pasticceria Creativa ci ha aperto le torte gelato che rendono redditizio l'inverno. Abbiamo guadagnato 5 punti.",
    "testimonialAuthor": "Federico Riva",
    "testimonialRole": "Maestro gelatiere, gelateria artigianale premium",
    "faqTitle": "Domande Frequenti dei Maestri Gelatieri",
    "faqs": [
      {
        "q": "Serve per gelateria italiana, gelateria artigianale o catena con più punti vendita?",
        "a": "Per tutte e tre. Gelateria Creativa ragiona come un maestro gelatiere professionale con bilanciamento tecnico documentato."
      },
      {
        "q": "Copre il bilanciamento di zuccheri, solidi e grassi?",
        "a": "Sì. Gelateria Creativa ragiona come un gelatiere professionale: bilanciamento con saccarosio, destrosio, zucchero invertito, solidi totali e grassi secondo norma tecnica."
      },
      {
        "q": "Come mi aiuta con la stagionalità?",
        "a": "Pasticceria Creativa apre torte gelato e semifreddi per la valle invernale; Gastro Calendar pianifica i picchi (Festa della Mamma, estate)."
      },
      {
        "q": "Genera contenuti visivi per Instagram?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento per vetrina e social. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con la tua vaschetta e l'impiattamento reale."
      },
      {
        "q": "Come gestisco le perdite in mantecatore e vetrina?",
        "a": "Sprechi GenCal fornisce dati per processo (mantecatore, abbattimento, esposizione). Si integrano nella scheda tecnica del Kit de Escandallos Pro."
      }
    ],
    "ctaTitle": "Il tuo gelato con tecnica autentica e margine reale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "IA per Gelatiere: Basi, Schede e Stagionalità | AI Chef Pro",
      "description": "Suite di IA per maestri gelatieri: Gelateria Creativa, bilanciamento tecnico, schede tecniche per gusto, branding e HACCP. Inizia oggi.",
      "keywords": "IA maestro gelatiere, IA gelatiere, software gelateria, schede tecniche gelato, bilanciamento tecnico gelato, mantecatore IA",
      "ogImage": "https://aichef.pro/og/use-cases/maestro-heladero.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Gelateria dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding di 2 minuti in cui racconti che tipo di gelateria gestisci (gelateria italiana, gelateria artigianale spagnola, gelateria con laboratorio), dimensione del team, città e specialità.",
    "appsTitle": "Gli Agenti IA che Userai come Maestro Gelatiere",
    "apps": [
      {
        "name": "Gelateria Creativa",
        "description": "Agente specializzato in gelateria artigianale con bilanciamento tecnico.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Torte gelato, semifreddi, dessert al cucchiaio per la valle invernale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di gusti signature con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Neutri, stabilizzanti, paste concentrate e texture professionali.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Perdite in mantecatore, abbattimento e vetrina.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica per gusto: latticini, frutta secca, glutine.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia artigianale IA di riferimento per vetrina, web e social.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale per gelateria d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Attirare clienti che cercano \"gelateria vicino a me\".",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Festa della Mamma, estate, San Valentino, torte gelato di Natale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico per torte gelato.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pasto del Personale",
        "description": "Generatore di menu per lo staff per il laboratorio.",
        "category": "Gastro Profile Pro"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo la schedatura dei gusti"
      },
      {
        "value": "−40 %",
        "label": "perdite in laboratorio e vetrina"
      },
      {
        "value": "×3",
        "label": "engagement Instagram"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo laboratorio"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Basi improvvisate, bilanciamento incoerente turno per turno",
        "Schede tecniche senza bilanciamento tecnico documentato",
        "Perdite senza tracciabilità per processo",
        "Stagionalità reattiva nella valle invernale",
        "Vetrina e social media improvvisati"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Basi con bilanciamento tecnico documentato",
        "Schede tecniche professionali per pallina e per kg",
        "Perdite controllate con Sprechi GenCal",
        "Torte gelato e semifreddi rendono redditizio l'inverno",
        "GastroIMG Gen+ + InstaFlow + Pinterest Pins Gen"
      ]
    },
    "galleryTitle": "Come Funziona il Laboratorio di un Maestro Gelatiere",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: mantecatore, basi, spatola, frutta e attrezzatura. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-mantecadora.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-bases.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-spatula.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-fruta.jpg",
      "/lovable-uploads/ai-gallery/use-case-maestro-heladero-team.jpg"
    ]
  },
  "maitre-jefe-sala": {
    "h1": "IA per Maître e Capo Sala",
    "heroSubtitle": "Coordina il servizio in sala con tecnica professionale, gestisci prenotazioni premium e abbinamenti, guida il team e cattura branding fine dining con una suite di agenti IA gastronomica specializzati in sala e servizio di alto livello.",
    "heroTagline": "Sala con tecnica professionale ed esperienza memorabile",
    "badge": "Per maître, capi sala e direttori di servizio",
    "painsTitle": "Cosa un Maître Non Può Evitare di Risolvere",
    "pains": [
      "Coordinare il servizio in sala con sequenza perfetta di portate, guéridon, stappatura e servizio professionale turno dopo turno",
      "Gestire prenotazioni premium con planning dei tavoli, allergie, occasioni speciali e preferenze del cliente abituale",
      "Guidare il team di sala con formazione costante su abbinamenti, posateria, descrizione dei piatti e storytelling",
      "Coordinare con la cucina portata per portata con timing perfetto e comunicazione fluida nei picchi di servizio",
      "Differenziarsi in un ristorante competitivo con esperienza memorabile, branding visuale fine dining e acquisizione di clienti abituali",
      "Catturare eventi privati e cene aziendali con proposte professionali di servizio e abbinamento"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Maître",
    "features": [
      {
        "title": "Manager Ristorante Pro",
        "description": "Agente specializzato adattato alla gestione di sala fine dining: sequenza di servizio, guéridon, stappatura, formazione del team.",
        "icon": "Crown"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Per la gestione professionale della cantina, stappature, raccomandazioni di vino e cocktaileria professionale.",
        "icon": "Wine"
      },
      {
        "title": "Food Pairing AI",
        "description": "Abbinamenti con base scientifica per ogni piatto del menù, fondamento professionale per il team di sala.",
        "icon": "Sparkles"
      },
      {
        "title": "Calcula Pax + Mise",
        "description": "Calcula Pax per banchetti, template di mise en place dei tavoli, guéridon, sequenza delle portate.",
        "icon": "Calculator"
      },
      {
        "title": "Kit di Attività Ristorante",
        "description": "Template: pre-servizio (mise en place), turno di servizio (portate), post-servizio (chiusura, pulizia), formazione del team.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pacchetto HACCP sala",
        "description": "Tracciabilità della cantina, conservazione dei vini, stappature e temperature di servizio.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Prenotazioni premium, eventi privati, cene aziendali, Natale, San Valentino, anniversari.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia elegante IA di riferimento + Instagram con storytelling di servizio e abbinamenti per attrarre clienti premium.",
        "icon": "Image"
      },
      {
        "title": "Storytelling del menù",
        "description": "Generazione di descrizioni di piatti e abbinamenti affinché il team di sala le reciti con professionalità davanti al cliente.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Maître con AI Chef Pro",
    "workflow": [
      "15:00 · Apertura — checklist Kit di Attività: revisione delle prenotazioni del giorno, mise en place dei tavoli, lucidatura di cristalleria e posateria, controllo cantina.",
      "16:00 · Briefing al team — spiegazione dei nuovi piatti del giorno con storytelling generato e abbinamenti validati con Food Pairing AI.",
      "17:00 · Coordinamento con la cucina — verifica dei cambi di menù, allergie confermate, mise en place delle portate.",
      "18:30 · Accoglienza delle prime prenotazioni — attenzione professionale, servizio di aperitivi, descrizione del menù.",
      "20:00 · Servizio cena — coordinamento portata per portata con la cucina, stappature professionali, guéridon al tavolo quando previsto.",
      "22:00 · Cene aziendali private — attenzione dedicata a evento da 12 coperti con menù degustazione e abbinamenti.",
      "00:00 · Chiusura — quadratura, saluto del team, GastroIMG Gen+ genera immagine di riferimento del menù degustazione + InstaFlow programma il post.",
      "01:00 · Briefing di chiusura — feedback del team, annotazione dei commenti dei clienti, pianificazione del giorno successivo."
    ],
    "productsTitle": "Template e Kit Raccomandati per Maître",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Manager Ristorante Pro + Bar & Lounge AI+ + Food Pairing AI hanno alzato completamente il livello del mio team di sala. Il briefing quotidiano con storytelling generato di ogni piatto e abbinamento validato scientificamente è ora professionale. I clienti notano la differenza: abbiamo aumentato lo scontrino medio del 20% e il tasso di clienti abituali premium è cresciuto del 40% in sei mesi.",
    "testimonialAuthor": "Sofía Vega",
    "testimonialRole": "Maître e Capo Sala, ristorante fine dining",
    "faqTitle": "Domande Frequenti dei Maître",
    "faqs": [
      {
        "q": "Funziona per fine dining, ristorante d'autore, gastronomico Michelin o ristorante premium?",
        "a": "Per tutti e quattro. Manager Ristorante Pro + Bar & Lounge AI+ coprono dal ristorante premium al gastronomico Michelin con servizio impeccabile, guéridon, stappatura professionale e storytelling."
      },
      {
        "q": "Come gestire prenotazioni premium e clienti abituali?",
        "a": "Manager Ristorante Pro ragiona con criterio professionale di sala: planning dei tavoli per preferenza, annotazione di allergie e occasioni, acquisizione di clienti abituali con menù personalizzati."
      },
      {
        "q": "Come formare il team di sala su abbinamenti e storytelling?",
        "a": "Food Pairing AI fonda ogni abbinamento su base scientifica che il team può comunicare al cliente; Bar & Lounge AI+ approfondisce cantina, stappatura e tecniche. Il briefing quotidiano è ora professionale."
      },
      {
        "q": "Genera contenuti visuali eleganti per Instagram?",
        "a": "Sì. GastroIMG Gen+ genera immagini eleganti di riferimento del menù e della tavola apparecchiata per Instagram, sito web e acquisizione di clienti premium. Ricorda che l'immagine IA è un riferimento visuale: la foto definitiva la scatti tu con il tuo tavolo reale."
      },
      {
        "q": "Come mi aiuta con eventi privati e cene aziendali?",
        "a": "Gastro Calendar pianifica eventi privati, cene aziendali, Natale, San Valentino, anniversari con menù degustazione e proposte di servizio dedicato."
      }
    ],
    "ctaTitle": "La tua sala con tecnica professionale ed esperienza memorabile.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Maître e Capo Sala: Servizio, Abbinamenti e Storytelling | AI Chef Pro",
      "description": "Suite IA per maître professionisti: Manager Pro, Bar & Lounge AI+, Food Pairing AI, formazione del team e acquisizione premium. Inizia oggi.",
      "keywords": "IA maître, IA capo sala, software maître, fine dining sala, guéridon stappatura IA, formazione team sala",
      "ogImage": "https://aichef.pro/og/use-cases/maitre-jefe-sala.jpg"
    },
    "personalizationTitle": "Personalizzato alla Tua Sala dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di sala dirigi (fine dining, ristorante d'autore, gastronomico Michelin/Guida Espresso, ristorante premium con cantina), dimensione del team, città e specialità. Ogni agente risponde adattato alla tua sala e alla tua operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai come Maître",
    "apps": [
      {
        "name": "Manager Ristorante Pro",
        "description": "Agente specializzato adattato alla gestione di sala fine dining.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Gestione cantina, stappature, raccomandazioni di vino e cocktaileria professionale.",
        "category": "Concetti di Business"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con base scientifica per ogni piatto del menù.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Storytelling e descrizioni dei piatti per il team di sala.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Calcula Pax",
        "description": "Scalatura delle ricette per eventi privati e cene aziendali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni da comunicare al cliente.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching per la leadership del team di sala e gestione dello stress nei picchi di servizio.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia elegante IA di riferimento per Instagram, sito web e acquisizione premium.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale elegante per fine dining.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Attrarre clienti premium che cercano fine dining su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Eventi privati, cene aziendali, Natale, San Valentino, anniversari.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pasto del Personale",
        "description": "Generatore di menù per lo staff prima del servizio.",
        "category": "Gastro Profile Pro"
      }
    ],
    "metrics": [
      {
        "value": "+20 %",
        "label": "scontrino medio fine dining"
      },
      {
        "value": "×1.4",
        "label": "tasso clienti abituali"
      },
      {
        "value": "×2",
        "label": "velocità proposte eventi"
      },
      {
        "value": "12+",
        "label": "agenti per la tua sala"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Briefing al team improvvisato, storytelling dei piatti senza rigore",
        "Abbinamenti consigliati senza base scientifica fondata",
        "Prenotazioni premium senza planning con preferenze e allergie",
        "Eventi privati chiusi a mano, proposta lenta",
        "Instagram improvvisato senza storytelling di servizio"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Briefing quotidiano professionale con storytelling e abbinamenti",
        "Abbinamenti con base scientifica di Food Pairing AI",
        "Prenotazioni premium con planning professionale e acquisizione di clienti abituali",
        "Eventi privati chiusi in un giorno con proposta di servizio",
        "Instagram elegante con GastroIMG Gen+ + InstaFlow AI Pro"
      ]
    },
    "galleryTitle": "Come Funziona la Sala di un Fine Dining",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: mise en place del tavolo, stappatura, guéridon, servizio e team. Immagini generate con IA come riferimento visuale del concept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-maitre-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-mesa.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-pour.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-servicio.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-gueridon.jpg",
      "/lovable-uploads/ai-gallery/use-case-maitre-team.jpg"
    ]
  },
  "panadero": {
    "h1": "IA per Panettiere Artigianale",
    "heroSubtitle": "Ottimizza lievito madre e prefermenti, scheda tecnica per pezzo con costo ora di laboratorio, controlla fermentazioni lunghe e operatività con una suite di agenti IA gastronomica specializzati in panificazione artigianale.",
    "heroTagline": "Panificazione artigianale con tecnica e margine reale",
    "badge": "Per panettieri artigianali e laboratori",
    "painsTitle": "Cosa un Panettiere Artigianale Non Può Lasciare Irrisolto",
    "pains": [
      "Standardizzare lievito madre, prefermenti (biga, poolish), idratazioni e processi di fermentazione lunga in ogni turno",
      "Calcolare la scheda tecnica dei pezzi con costo reale includendo le ore di laboratorio (rinfresco, impasto, formatura, cottura richiedono tempo)",
      "Misure in impasti, prefermenti, ritagli di formatura e cottura fallita",
      "Produzione adeguata alla domanda giornaliera senza sovrapproduzione né rottura di stock prima della chiusura",
      "Differenziarsi in zona competitiva con farine premium, cereali antichi e branding artigianale",
      "Catturare ordini dalla ristorazione locale (ristoranti, caffetterie) con margine mentre si gestisce la vendita diretta"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Panettiere",
    "features": [
      {
        "title": "Panificazione Creativa",
        "description": "Agente specializzato in panificazione artigianale professionale: lieviti madre, idratazioni alte, tecnica di formatura e cottura su pietra.",
        "icon": "Wheat"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Per lieviti madre liquidi e solidi, prefermenti (biga, poolish), fermentazioni lunghe controllate a freddo e tecnica avanzata.",
        "icon": "Beaker"
      },
      {
        "title": "Pasticceria Creativa",
        "description": "Per laboratori che combinano panificazione con pasticceria e lievitati: brioche, croissant, ensaimadas e pasticceria artigianale.",
        "icon": "Cake"
      },
      {
        "title": "Scheda tecnica per pezzo con costo ora laboratorio",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica CSV; Kit Escandallos Pro lo gestisce con costo ora laboratorio integrato nel margine reale per pagnotta, baguette o brioche.",
        "icon": "Calculator"
      },
      {
        "title": "Kit di Attività Laboratorio",
        "description": "Modelli: rinfresco lievito madre, prefermenti, impasti, fermentazioni, formatura, cottura, vetrina e conservazione.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack HACCP panificazione",
        "description": "Tracciabilità delle farine, lievito madre, prefermenti, conservazione e temperature critiche in cella di fermentazione.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione stagionale con date chiave: Pasqua (monas, hornazos), Natale (Roscón, panettone), San Giovanni, eventi locali.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Fotografia gastronomica IA di riferimento + Pinterest, dove la panificazione artigianale cattura traffico organico stabile.",
        "icon": "Image"
      },
      {
        "title": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"panetteria artigianale vicino a me\" su Google e Maps.",
        "icon": "BarChart3"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Panettiere con AI Chef Pro",
    "workflow": [
      "04:00 · Apertura — checklist Kit di Attività Laboratorio: rinfresco lievito madre, controllo fermentazioni della notte, accensione del forno a pietra.",
      "05:30 · Formatura e cottura — formatura di pagnotte, baguette e brioche con modelli specifici, controllo degli scarti di formatura.",
      "08:00 · Rifornimento vetrina — prima infornata pronta per vendita diretta e ordini alla ristorazione locale.",
      "10:00 · Panificazione Creativa — sviluppi un nuovo pane di cereali antichi con lievito madre liquido. Cucina Creativa fornisce ricetta + scheda tecnica CSV.",
      "11:00 · Fermentus Con AI+ — regoli l'idratazione all'80% e la fermentazione a freddo di 24 ore per il nuovo pane.",
      "12:00 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali di farina biologica e costo ora laboratorio, validi il margine.",
      "15:00 · GastroIMG Gen+ + Pinterest Pins Gen — generi l'immagine di riferimento del nuovo pane e i pin per catturare traffico organico.",
      "20:00 · Chiusura — pulizia, HACCP firmato, preparazione impasti per fermentazione notturna."
    ],
    "productsTitle": "Modelli e Kit Consigliati per la Panificazione",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Siamo passati da fogli sparsi a un sistema. Sappiamo esattamente quale pezzo rende e quale no, incluso il costo ora di laboratorio. Lo spreco è calato del 30% in 3 mesi e abbiamo scoperto che due pani storici non erano redditizi senza costo ora — li abbiamo ridisegnati semplificando il processo senza perdere qualità e abbiamo alzato il margine di 5 punti.",
    "testimonialAuthor": "Ana Iglesias",
    "testimonialRole": "Panettiera artigianale, laboratorio proprio",
    "faqTitle": "Domande Frequenti dei Panettieri",
    "faqs": [
      {
        "q": "Copre la tecnica del lievito madre professionale?",
        "a": "Sì. Panificazione Creativa e Fermentus ragionano come un panettiere professionista: rinfreschi con percentuale di inoculo, idratazioni per tipo di pane, fermentazioni controllate a freddo 24-48 ore, bilanciamento dei ceppi. Niente ricette da YouTube."
      },
      {
        "q": "Va bene per un laboratorio artigianale piccolo o industriale?",
        "a": "Per entrambi. I modelli scalano da laboratorio familiare di 2 persone a produzione industriale. La metodologia è la stessa: ricetta → scheda tecnica CSV con costo ora laboratorio → margine reale."
      },
      {
        "q": "Copre anche pasticceria e lievitati oltre alla panificazione?",
        "a": "Sì. Pasticceria Creativa completa il catalogo se fai brioche, croissant, ensaimadas, lievitati di Pasqua o paste. Fermentus Con AI+ copre la parte fermentata con tecnica professionale."
      },
      {
        "q": "Genera contenuti visivi per vetrina, Instagram e Pinterest?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali del pane per vetrina, web e social; Pinterest Pins Gen cattura traffico organico stabile che la panificazione artigianale sfrutta molto. Ricorda che l'immagine IA è un riferimento visivo: la foto definitiva la fai tu con la tua pagnotta appena sfornata."
      },
      {
        "q": "Come mi aiuta con stagionalità ed eventi?",
        "a": "Gastro Calendar pianifica le stagioni chiave (Pasqua con monas e hornazos, Natale con Roscón e panettone, San Giovanni, eventi locali) con anticipo. Il Kit Plan Finanziario proietta il cash flow stagionale realistico."
      }
    ],
    "ctaTitle": "La tua panificazione artigianale con margine chiaro e tecnica professionale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Panettiere Artigianale: Lievito Madre, Schede Tecniche e Tecnica Professionale | AI Chef Pro",
      "description": "Suite IA per panettieri artigianali: Panificazione Creativa, Fermentus Con AI+ per lievito madre, schede tecniche per pezzo con costo ora laboratorio. Inizia oggi.",
      "keywords": "IA panettiere, panificazione artigianale IA, lievito madre IA, software panificazione, schede tecniche panificazione, fermentus, biga poolish, panettiere professionale",
      "ogImage": "https://aichef.pro/og/use-cases/panadero.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Laboratorio dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di panificazione gestisci (artigianale con lievito madre, panetteria tradizionale, laboratorio con pasticceria, panetteria con caffetteria, panetteria biologica), dimensione del team, città e specialità. Ogni agente —da Panificazione Creativa a Gastro Calendar— risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nella Tua Panetteria",
    "apps": [
      {
        "name": "Panificazione Creativa",
        "description": "Agente specializzato in panificazione artigianale professionale, lieviti madre, idratazioni e tecnica.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Lieviti madre, biga, poolish, idratazioni alte e fermentazioni lunghe controllate.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Brioche, croissant, ensaimadas e pasticceria artigianale complementare.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di pani signature con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa: farine tecniche, miglioratori, semi e cereali antichi.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi in impasto, prefermenti, ritagli di formatura e cottura.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per pezzo: glutine, lattosio, frutta a guscio, uova.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA di riferimento per vetrina, web e social.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico stabile per la panificazione artigianale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale professionale per panetteria d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"panetteria artigianale vicino a me\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Pianificazione stagionale: Pasqua, Natale, San Giovanni, eventi locali.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo la scheda tecnica dei pezzi"
      },
      {
        "value": "−30 %",
        "label": "sprechi in laboratorio e cottura"
      },
      {
        "value": "×2",
        "label": "traffico organico via Pinterest"
      },
      {
        "value": "12+",
        "label": "agenti per la tua panetteria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Lievito madre improvvisato, fermentazioni inconsistenti turno dopo turno",
        "Schede tecniche senza costo ora laboratorio, pani complessi in perdita senza saperlo",
        "Sprechi in impasti, prefermenti e cottura senza tracciabilità",
        "Vetrina e social improvvisati con foto dal telefono",
        "HACCP su carta stampata sparsa per il laboratorio"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Lievito madre con criterio tecnico: rinfreschi, idratazioni e fermentazioni consistenti",
        "Scheda tecnica professionale per pezzo con costo ora laboratorio integrato",
        "Sprechi controllati con Sprechi GenCal e modelli specifici",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ catturano traffico stabile",
        "HACCP da smartphone con registri pronti per l'ispezione"
      ]
    },
    "galleryTitle": "Come Funziona una Panificazione Artigianale",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: vetrina, lievito madre, fermentazione, pani, cottura e team. Immagini generate con IA come riferimento visivo del concept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-panadero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-masa.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-fermentacion.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-horneado.jpg",
      "/lovable-uploads/ai-gallery/use-case-panadero-team.jpg"
    ]
  },
  "pasteleria-obrador": {
    "h1": "IA per Pasticceria e Laboratorio",
    "heroSubtitle": "Scheda tecnica per pezzo con costo orario del laboratorio, pianifica la produzione stagionale e cattura branding professionale con una suite di agenti IA specializzati in pasticceria artigianale.",
    "heroTagline": "Pasticceria con margine reale e senza carta",
    "badge": "Per pasticcerie e laboratori artigianali",
    "painsTitle": "Cosa una Pasticceria Non Può Lasciare Irrisolto",
    "pains": [
      "Schede tecniche complesse con lievito madre, prefermenti e lavorazioni lunghe che richiedono ore di laboratorio",
      "Sprechi elevati in laboratorio (formatura, cottura, decorazione) che erodono la redditività senza controllo",
      "Tracciabilità HACCP con prodotti sensibili: uova, latticini, creme, frutta secca",
      "Stagionalità molto forte: Roscone dei Re Magi, San Valentino, Pasqua, Natale, comunioni",
      "Differenziarsi in zona competitiva: branding visivo, vetrina e social sono fondamentali",
      "Gestire ordini di torte su misura con margine mentre si gestisce la pasticceria quotidiana"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in Pasticceria",
    "features": [
      {
        "title": "Pasticceria Creativa",
        "description": "Agente specializzato in pasticceria professionale, dessert da ristorante, torte su misura e lievitati con tecnica avanzata.",
        "icon": "Cake"
      },
      {
        "title": "Cioccolateria Creativa",
        "description": "Per laboratori che combinano pasticceria e cioccolateria: praline, ganache, coperture e abbinamenti.",
        "icon": "Cookie"
      },
      {
        "title": "Panificazione Creativa",
        "description": "Per laboratori che producono i propri lievitati con pasta madre, brioche, croissant e panificazione artigianale.",
        "icon": "Wheat"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Pasta madre professionale, fermentazioni controllate e processi di panificazione all'avanguardia.",
        "icon": "Beaker"
      },
      {
        "title": "Schede tecniche con costo orario laboratorio",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica CSV; Kit Escandallos Pro la gestisce con costo orario laboratorio integrato nel margine reale per pezzo.",
        "icon": "Calculator"
      },
      {
        "title": "Kit di Attività Pasticceria",
        "description": "Modelli: preparazione pasta madre, produzione, formatura, cottura, vetrina, conservazione.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack HACCP pasticceria",
        "description": "Tracciabilità di uova, creme con latticini, frutta secca e conservazione professionale.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione stagionale con date chiave: Roscone, San Valentino, Pasqua, Natale. Calendario editoriale per la vetrina.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Fotografia gastronomica IA + Pinterest, dove le pasticcerie catturano più traffico organico stabile.",
        "icon": "Image"
      }
    ],
    "workflowTitle": "Una Giornata Reale in una Pasticceria con AI Chef Pro",
    "workflow": [
      "06:00 · Apertura — checklist Kit di Attività Pasticceria: rinfresco pasta madre, impasto torte, preparazione creme.",
      "08:00 · Pasticceria Creativa — sviluppi un nuovo dessert per San Valentino. Cucina Creativa fornisce ricetta + scheda tecnica CSV.",
      "09:00 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali e costo orario laboratorio integrato, validi il margine.",
      "11:00 · Produzione del giorno — formatura e cottura con modelli specifici, sprechi registrati con HACCP.",
      "14:00 · Rifornimento vetrina con etichette e prezzi, controllo sprechi di esposizione.",
      "16:00 · Gastro Calendar — prepari la pianificazione della produzione del Roscone dei Re Magi (Natale).",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — generi fotografie e pin del nuovo dessert per catturare traffico.",
      "20:00 · Chiusura — pulizia profonda, HACCP firmato, pianificazione del giorno successivo."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Pasticceria",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Le schede tecniche per pezzo con costo orario del laboratorio mi hanno aperto gli occhi. Ho scoperto che alcune lavorazioni complesse non erano redditizie nonostante si vendessero bene. Le abbiamo ridisegnate con Pasticceria Creativa semplificando il processo senza perdere qualità e abbiamo aumentato il margine di 6 punti.",
    "testimonialAuthor": "Eva Mata",
    "testimonialRole": "Titolare, pasticceria artigianale con laboratorio proprio",
    "faqTitle": "Domande Frequenti delle Pasticcerie",
    "faqs": [
      {
        "q": "Funziona per un laboratorio artigianale piccolo o grande?",
        "a": "Per entrambi. I modelli scalano da laboratorio familiare di 2 persone a produzione industriale. Ci sono clienti con uno e con sei pasticceri."
      },
      {
        "q": "Copre anche la panificazione oltre alla pasticceria?",
        "a": "Sì. Panificazione Creativa + Fermentus Con AI+ coprono panificazione artigianale e pasta madre professionale per laboratori misti."
      },
      {
        "q": "C'è il controllo del costo orario del laboratorio?",
        "a": "Sì. Costo orario laboratorio integrato nella scheda tecnica del Kit Escandallos Pro: una lavorazione complessa con 3 ore di lavoro per pezzo ha il suo costo reale riflesso."
      },
      {
        "q": "Genera contenuti per vetrina e social?",
        "a": "Sì. GastroIMG Gen+ per foto della vetrina + Pinterest Pins Gen + InstaFlow AI Pro + MenuDish Local SEO per attirare clienti locali."
      },
      {
        "q": "Come mi aiuta con la stagionalità?",
        "a": "Gastro Calendar pianifica le stagioni chiave (Roscone, San Valentino, Pasqua, Natale, comunioni) con anticipo e piano finanziario adattato ai picchi di produzione."
      }
    ],
    "ctaTitle": "Il tuo laboratorio con margine chiaro e branding professionale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Pasticceria e Laboratorio: Schede Tecniche, Stagionalità e Branding | AI Chef Pro",
      "description": "Suite IA per pasticcerie artigianali: Pasticceria Creativa, schede tecniche per pezzo con costo orario laboratorio, HACCP, pianificazione stagionale e branding. Inizia oggi.",
      "keywords": "IA pasticceria, software laboratorio, schede tecniche pasticceria, pasticceria artigianale IA, pasta madre pasticceria, Roscone Natale, pasticceria Italia",
      "ogImage": "https://aichef.pro/og/use-cases/pasteleria-obrador.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Laboratorio dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di pasticceria gestisci (artigianale, industriale, pasticceria da ristorante, laboratorio misto), dimensione del team, città e specialità. Ogni agente —da Pasticceria Creativa a Gastro Calendar— risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nella Tua Pasticceria",
    "apps": [
      {
        "name": "Pasticceria Creativa",
        "description": "Agente specializzato in pasticceria professionale, dessert e torte con tecnica avanzata.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cioccolateria Creativa",
        "description": "Per praline, ganache e abbinamenti di cioccolato.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Panificazione Creativa",
        "description": "Per pasta madre, brioche, croissant e panificazione artigianale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Fermentazioni, prefermenti e tecniche avanzate di panificazione.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di dessert con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Assistente del catalogo Sosa per texture e tecnica avanzata.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Assistente del catalogo tSpoonLab per applicazioni avanzate.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi sugli sprechi in laboratorio (formatura, cottura, vetrina).",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per pezzo, critica in pasticceria.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA per vetrina, web e social.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest è il canale con più traffico organico stabile per la pasticceria.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Pianificazione stagionale: Roscone, San Valentino, Pasqua, Natale.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margine dopo le schede tecniche"
      },
      {
        "value": "×2",
        "label": "traffico organico via Pinterest"
      },
      {
        "value": "−30 %",
        "label": "sprechi in laboratorio"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo laboratorio"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Schede tecniche senza costo orario laboratorio, lavorazioni lunghe in perdita senza saperlo",
        "Sprechi in laboratorio e vetrina senza tracciabilità reale",
        "Vetrina e social improvvisati senza continuità",
        "Produzione stagionale reattiva, senza anticipo né pianificazione",
        "HACCP su carta stampata sparsa per il laboratorio"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Scheda tecnica professionale per pezzo con costo orario laboratorio integrato",
        "Sprechi controllati con Sprechi GenCal e modelli specifici",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ catturano traffico stabile",
        "Gastro Calendar pianifica le stagioni chiave con anticipo",
        "HACCP da smartphone con registri pronti per l'ispezione"
      ]
    },
    "galleryTitle": "Come Funziona una Pasticceria Artigianale",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: vetrina, laboratorio, esposizione dei pezzi, decorazione, torte e team.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-pasteleria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-obrador.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-display.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-piping.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-cakes.jpg",
      "/lovable-uploads/ai-gallery/use-case-pasteleria-team.jpg"
    ]
  },
  "pizzeria": {
    "h1": "IA per Pizzeria",
    "heroSubtitle": "Standardizza la pasta madre, calcola le schede tecniche per pizza, gestisci delivery e multi-marca con una suite di agenti IA specializzati in pizzeria professionale, pizza napoletana, romana e americana.",
    "heroTagline": "Pizza con margine reale, tecnica con sistema",
    "badge": "Per pizzerie e pizzaioli",
    "painsTitle": "Cosa una Pizzeria Non Può Evitare di Risolvere",
    "pains": [
      "Margine molto ridotto sulla pizza con controllo millimetrico del grammage in impasto, salsa, formaggio e topping",
      "Sprechi in pasta madre, mozzarella e salse che erodono la redditività senza controllo",
      "Picchi di domanda nel delivery (12:30-14:30, 20:30-22:30) senza margine per errori",
      "Menu ampio di pizze con scheda tecnica individualizzata per variante",
      "Standardizzare impasto e tecnica in cucine dove ruota il team di pizzaioli",
      "Attirare clienti locali con SEO e social per ridurre la dipendenza dalle piattaforme di delivery"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in una Pizzeria",
    "features": [
      {
        "title": "Cucina Italiana",
        "description": "Agente specializzato in cucina italiana professionale, impasti, salse e tecnica di pizzeria napoletana, romana e americana.",
        "icon": "Pizza"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Per pasta madre, fermentazioni lunghe, idratazioni elevate e tecnica di panificazione applicata alla pizza professionale.",
        "icon": "Beaker"
      },
      {
        "title": "Schede tecniche per pizza",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica CSV; Kit Escandallos Pro lo gestisce con i tuoi prezzi reali e margine obiettivo per variante.",
        "icon": "Calculator"
      },
      {
        "title": "Kit Attività Pizzeria",
        "description": "Template: idratazione impasto, prep salse, mise dei topping, servizio in sala e delivery.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack HACCP",
        "description": "Template adattati alla pizzeria: temperature del forno, conservazione della pasta madre, tracciabilità per il delivery.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Burger Pro AI+ + Food Truck AI+",
        "description": "Se gestisci una dark kitchen multi-marca, agenti complementari per delivery specializzato.",
        "icon": "Truck"
      },
      {
        "title": "MenuDish Local SEO + InstaFlow AI Pro",
        "description": "Posizionamento locale su Google e contenuti virali per Instagram con calendario editoriale.",
        "icon": "Sparkles"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA per Glovo, Uber Eats, Just Eat e sito del ristorante.",
        "icon": "Image"
      },
      {
        "title": "Kit Gestione Personale",
        "description": "Turni per pizzaioli, sala e delivery con rotazioni e picchi di servizio.",
        "icon": "Users"
      }
    ],
    "workflowTitle": "Una Giornata Reale in una Pizzeria con AI Chef Pro",
    "workflow": [
      "08:00 · Apertura — checklist Kit Attività Pizzeria: idratazione pasta madre, prep salsa di pomodoro, mise dei topping.",
      "10:00 · Cucina Italiana + Fermentus Con AI+ — sviluppi una nuova pizza di stagione con impasto a idratazione 75% e fermentazione 48 h.",
      "11:00 · Kit Escandallos Pro — calcoli la scheda tecnica della nuova pizza con i tuoi prezzi reali (farina, mozzarella, prosciutto) e validi il margine al 32%.",
      "12:30 · Servizio mezzogiorno — pizzaiolo al forno, sala piena, delivery attivo con template specifici.",
      "15:30 · Inventario — validi ordini di farina italiana, mozzarella di bufala e conserve con il Kit Inventario.",
      "17:00 · MenuDish Local SEO — aggiorni le descrizioni delle pizze top su Google Business e sul sito.",
      "20:00 · Servizio sera — picco di delivery, pizzaiolo al forno coordinato con sala e rider.",
      "23:30 · Chiusura — pulizia, HACCP firmato, report del giorno al proprietario."
    ],
    "productsTitle": "Template e Kit Scaricabili per Pizzeria",
    "productIds": [
      "kit-tareas-pizzeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Abbiamo calcolato la scheda tecnica pizza per pizza con il Kit Escandallos Pro e scoperto che 4 varianti erano in perdita perché pesavamo troppa mozzarella. Abbiamo regolato grammature e prezzo. Il margine del locale è salito di 4 punti in 2 mesi senza toccare la qualità.",
    "testimonialAuthor": "Giovanni Russo",
    "testimonialRole": "Pizzaiolo e proprietario, pizzeria napoletana",
    "faqTitle": "Domande Frequenti delle Pizzerie",
    "faqs": [
      {
        "q": "Funziona per pizza napoletana, romana, americana o Detroit?",
        "a": "Per tutte. Cucina Italiana e Fermentus Con AI+ coprono l'intero spettro di impasti, idratazioni, fermentazioni e tecniche di ogni stile."
      },
      {
        "q": "Copre anche il delivery oltre al locale?",
        "a": "Sì. Il Kit Attività Pizzeria include template specifici per il delivery con tempi, sprechi associati e coordinamento con le piattaforme (Glovo, Uber Eats, Just Eat)."
      },
      {
        "q": "Funziona per 1 locale o per una catena di pizzerie?",
        "a": "Entrambi. Ci sono clienti con 1 locale e altri con più di 12 unità attive. Per i gruppi, Chef Esecutivo Pro standardizza ricette e manuali."
      },
      {
        "q": "Genera idee per promozioni nei giorni morti?",
        "a": "Sì. Gastro Calendar + InstaFlow AI Pro generano combo, offerte, calendario editoriale e campagne stagionali con creatività professionale."
      },
      {
        "q": "Come mi aiuta con la pasta madre professionale?",
        "a": "Fermentus Con AI+ è il riferimento per la fermentazione: idratazioni, prefermenti (poolish, biga, tang zhong), rinfreschi della pasta madre e tecniche di fermentazione controllata."
      }
    ],
    "ctaTitle": "Pizza con margine reale, non intuizione.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Pizzeria: Pasta Madre, Schede Tecniche per Pizza e Delivery | AI Chef Pro",
      "description": "Suite IA per pizzerie professionali: Cucina Italiana, Fermentus per impasti, schede tecniche per pizza, template pizzeria e SEO locale. Inizia oggi.",
      "keywords": "IA pizzeria, schede tecniche pizza, software pizzeria, pasta madre pizza IA, pizza napoletana IA, pizza romana IA, gestione pizzeria delivery, pizzeria Italia",
      "ogImage": "https://aichef.pro/og/use-cases/pizzeria.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Pizzeria dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di pizzeria gestisci (napoletana, romana, americana, Detroit, alla pala), numero di coperti, città e operatività. Da quel momento, ogni agente —da Cucina Italiana a MenuDish Local SEO— risponde adattato al tuo stile di impasto, piattaforme di delivery e mercato locale.",
    "appsTitle": "Gli Agenti IA che Userai nella Tua Pizzeria",
    "apps": [
      {
        "name": "Cucina Italiana",
        "description": "Agente specializzato in cucina italiana professionale con base di pizzeria napoletana e romana.",
        "category": "Ricettari per Paese"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Pasta madre, idratazioni elevate e fermentazioni lunghe con supporto professionale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di pizze creative con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Per coordinare il resto del menu casual della pizzeria (antipasti, dessert).",
        "category": "Concetti di Business"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi sugli sprechi in impasto, mozzarella e topping.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per pizza e piatto.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Descrizioni SEO locali per migliorare posizionamento web e delivery.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Post per blog per attirare traffico organico locale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Keyword Discovery AI+",
        "description": "Parole chiave per zona: «pizza napoletana [il tuo quartiere]».",
        "category": "Contenuti e Social"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Contenuti virali Instagram con foto di pizza e calendario editoriale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA per sito e piattaforme di delivery.",
        "category": "Gastro Conoscenza"
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "margine dopo scheda tecnica pizza per pizza"
      },
      {
        "value": "×2",
        "label": "traffico delivery via SEO locale"
      },
      {
        "value": "−25 %",
        "label": "sprechi con controllo sistematico"
      },
      {
        "value": "11+",
        "label": "agenti per la tua pizzeria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Pasta madre e tecnica dispersi nel quaderno del pizzaiolo principale",
        "Schede tecniche a occhio, grammature che variano tra pizzaioli",
        "Sprechi di mozzarella e impasto senza controllo reale",
        "Posizionamento debole nel delivery per descrizioni generiche",
        "Operatività delivery improvvisata nelle ore di punta"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Cucina Italiana + Fermentus Con AI+ documentano impasto e tecnica replicabile",
        "Scheda tecnica professionale per pizza con margine validato",
        "Sprechi controllati con Sprechi GenCal e template specifici",
        "SEO locale ottimizzato con MenuDish Local SEO + Keyword Discovery",
        "Kit Attività Pizzeria con template per delivery, sala e picchi"
      ]
    },
    "galleryTitle": "Come Funziona una Pizzeria Professionale",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: forno, pasta madre, pizza al dettaglio, prep topping, team e delivery.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-pizzeria-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-oven.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-dough.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-pizza.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-toppings.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzeria-delivery.jpg"
    ]
  },
  "pizzero": {
    "h1": "IA per Pizzaiolo",
    "heroSubtitle": "Ottimizza impasti e fermentazioni, calcola il food cost per pizza con costo reale, controlla la tecnica del forno e l'operatività con una suite di agenti di IA gastronomica specializzati in cucina italiana professionale.",
    "heroTagline": "Pizza con tecnica autentica e margine reale",
    "badge": "Per pizzaioli e titolari di pizzerie",
    "painsTitle": "Quello che un pizzaiolo non può ignorare",
    "pains": [
      "Standardizzare impasto, idratazione e fermentazione in ogni turno con criterio tecnico (napoletana, romana, in pala, americana)",
      "Calcolare il food cost delle pizze con molte varianti di topping e mantenere un food cost coerente tra tutte le opzioni del menu",
      "Sprechi di impasto (sovrafermentazione, formatura fallita), mozzarella (umidità, evaporazione) e salse",
      "Mantenere una qualità costante al forno (legna, elettrico, gas) con picchi di domanda nel fine settimana",
      "Differenziarsi in una zona competitiva con pizze gourmet, farine premium e storytelling visivo",
      "Catturare ordini di delivery con margine mentre si gestisce il locale con servizio in sala"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Pizzaiolo",
    "features": [
      {
        "title": "Cucina Italiana",
        "description": "Agente specializzato in cucina italiana professionale: impasti (napoletana, romana, in pala, americana), salse, topping e tecnica del forno.",
        "icon": "Pizza"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Per lievito madre, prefermenti (biga, poolish), alte idratazioni e lunghe fermentazioni controllate a freddo.",
        "icon": "Beaker"
      },
      {
        "title": "Food cost per pizza",
        "description": "Cucina Italiana fornisce ricetta + CSV del food cost; Kit de Escandallos Pro lo gestisce con costo reale per pizza, food cost % e prezzo suggerito.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Pizzería",
        "description": "Template: mise en place dell'impasto, preparazione salse, mise en place dei topping, servizio in sala, delivery, chiusura e pulizia del forno.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack HACCP pizzeria",
        "description": "Tracciabilità di farine, lievito madre, mozzarella, salse e temperature critiche in forno e cella.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione del menu stagionale: pizze estive con pomodoro fresco, autunnali con funghi e tartufo, speciali per San Valentino ed eventi.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia gastronomica IA di riferimento + Instagram con calendario editoriale: la pizzeria vive di impatto visivo.",
        "icon": "Image"
      },
      {
        "title": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"pizzeria vicino a me\" su Google e Maps con descrizioni ottimizzate.",
        "icon": "BarChart3"
      },
      {
        "title": "Sprechi GenCal",
        "description": "Dati precisi sugli sprechi per processo (impasto, mozzarella, ritagli, delivery) integrati nel food cost.",
        "icon": "Sparkles"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Pizzaiolo con AI Chef Pro",
    "workflow": [
      "08:00 · Apertura — checklist Kit de Tareas Pizzería: rinfresco del lievito madre o biga, preparazione della salsa di pomodoro San Marzano, fermentazione controllata dei panetti.",
      "10:00 · Cucina Italiana — sviluppi una nuova pizza stagionale (zucca arrosto, gorgonzola, miele e noci) con criterio tecnico. Cucina Creativa fornisce ricetta + CSV del food cost.",
      "11:00 · Fermentus Con AI+ — regoli l'idratazione al 70% e i tempi di fermentazione a freddo di 48 ore per l'impasto napoletano.",
      "12:00 · Kit de Escandallos Pro — carichi il CSV con i tuoi prezzi reali di farina Caputo, mozzarella di bufala e topping, valuti margine e food cost %.",
      "13:00 · Servizio di mezzogiorno — il team replica con template di mise en place e preparazione, picchi coordinati.",
      "17:00 · Pausa tra i servizi — Gastro Calendar pianifica il menu autunnale e gli eventi.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento della nuova pizza e i post per Instagram.",
      "23:00 · Chiusura — pulizia profonda del forno, HACCP firmato, preparazione dell'impasto per domani."
    ],
    "productsTitle": "Template e Kit Consigliati per la Pizzeria",
    "productIds": [
      "kit-tareas-pizzeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Abbiamo calcolato il food cost pizza per pizza e scoperto che 4 erano in perdita nonostante vendessero bene. Le abbiamo ridisegnate con Cucina Italiana semplificando i topping senza perdere identità e abbiamo aumentato il margine di 4 punti senza toccare il prezzo. Fermentus ci ha cambiato l'impasto: idratazione 70%, fermentazione 48 ore, alveolatura perfetta.",
    "testimonialAuthor": "Giovanni Russo",
    "testimonialRole": "Pizzaiolo e titolare, pizzeria napoletana",
    "faqTitle": "Domande Frequenti dei Pizzaioli",
    "faqs": [
      {
        "q": "Funziona per pizza napoletana, romana, in pala o americana?",
        "a": "Per tutte e quattro. Cucina Italiana e Fermentus coprono l'intero spettro degli impasti (alveolatura, idratazione, fermentazioni), le tecniche di cottura (legna, elettrico, gas) e gli stili italiani e americani."
      },
      {
        "q": "Copre la tecnica del lievito madre e dei prefermenti?",
        "a": "Sì. Fermentus Con AI+ comprende biga, poolish, lievito madre liquido e solido, alte idratazioni e fermentazioni controllate a freddo. Ragiona come un pizzaiolo professionista, non come le ricette di YouTube."
      },
      {
        "q": "Copre il delivery oltre al locale?",
        "a": "Sì. Il Kit de Tareas Pizzería include template specifici per il delivery: temperature, packaging che mantiene la cottura, sprechi di trasporto e procedure di ritiro."
      },
      {
        "q": "Genera contenuti visivi per Instagram, Glovo e Uber Eats?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali per Instagram, piattaforme di delivery e menu; migliore foto = più clic e miglior ranking. Ricorda che l'immagine IA è un riferimento visivo: la foto definitiva la fai tu con la tua pizza appena sfornata."
      },
      {
        "q": "Come mi aiuta con la stagionalità e gli eventi?",
        "a": "Gastro Calendar pianifica i menu stagionali (estate, autunno con funghi e tartufo, speciali per San Valentino, Pasqua, Natale). Il Kit Plan Financiero proietta il cash flow stagionale realistico per arrivare a ogni picco con scorte e liquidità."
      }
    ],
    "ctaTitle": "La tua pizzeria con margine reale e tecnica autentica.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Pizzaiolo: Impasti, Food Cost e Tecnica | AI Chef Pro",
      "description": "Suite di IA per pizzaioli professionisti: Cucina Italiana, Fermentus per impasti e biga, food cost per pizza, template e tecnica autentica. Inizia oggi.",
      "keywords": "IA pizzaiolo, software pizzeria, food cost pizza, lievito madre pizza, biga poolish pizza, tecnica napoletana, pizza romana IA",
      "ogImage": "https://aichef.pro/og/use-cases/pizzero.jpg"
    },
    "personalizationTitle": "Personalizzato sulla Tua Pizzeria dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di pizzeria gestisci (napoletana autentica, romana al taglio, americana, mista con cucina italiana, dark kitchen per delivery), dimensione del team, città e tipo di forno. Ogni agente —da Cucina Italiana a Gastro Calendar— risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nella Tua Pizzeria",
    "apps": [
      {
        "name": "Cucina Italiana",
        "description": "Agente specializzato in cucina italiana professionale: impasti, salse, topping, tecnica del forno.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Lievito madre, biga, poolish, alte idratazioni, lunghe fermentazioni controllate.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di pizze signature con ricetta + CSV del food cost.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per farine tecniche, miglioratori e combinazioni avanzate.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi di impasto, mozzarella, salsa, ritagli e delivery integrati nel food cost.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per pizza: glutine, lattosio, frutta secca, uova.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA di riferimento per Glovo, Uber Eats, web e social media.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale professionale per pizzeria d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"pizzeria vicino a me\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Pianificazione del menu stagionale: estate, autunno, San Valentino, Natale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico stabile per pizze con storytelling.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Articoli SEO su tecnica italiana, impasti e abbinamenti per catturare traffico.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "margine dopo il calcolo del food cost delle pizze"
      },
      {
        "value": "×3",
        "label": "engagement Instagram con GastroIMG"
      },
      {
        "value": "−25 %",
        "label": "sprechi di impasto e mozzarella"
      },
      {
        "value": "12+",
        "label": "agenti per la tua pizzeria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Impasto improvvisato a ogni turno: alveolatura incoerente e croccantezza irregolare",
        "Food cost non calcolato, pizze in perdita senza saperlo",
        "Sprechi di impasto, mozzarella e salsa senza tracciabilità",
        "Instagram improvvisato e piattaforme di delivery con foto dal telefono",
        "HACCP su carta stampata sparsa per la pizzeria"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Impasto con criterio tecnico: idratazione, fermentazione e cottura costanti",
        "Food cost professionale per pizza con margine validato e food cost %",
        "Sprechi controllati con Sprechi GenCal e template specifici",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO catturano clienti locali e delivery",
        "HACCP dal telefono con registri pronti per l'ispezione"
      ]
    },
    "galleryTitle": "Come Funziona una Pizzeria Autentica",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: impasto, forno, tecnica, ingredienti, pizze e team. Immagini generate con IA come riferimento visivo del concept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-pizzero-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-masa.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-horno.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-pizza.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-ingredients.jpg",
      "/lovable-uploads/ai-gallery/use-case-pizzero-team.jpg"
    ]
  },
  "propietario-catering": {
    "h1": "IA per Proprietari di Aziende di Catering",
    "heroSubtitle": "Controlla la redditività per evento, scala la produzione, gestisci team temporanei e fai crescere la tua azienda di catering con una suite di agenti IA specializzati in ristorazione.",
    "heroTagline": "Crescita controllata, margine reale, eventi senza caos",
    "badge": "Per proprietari di aziende di catering",
    "painsTitle": "Cosa un Proprietario di Catering Non Può Trascurare",
    "pains": [
      "Gestire margini con alta variabilità tra eventi: un matrimonio, un cocktail aziendale e una pausa caffè hanno redditività molto diverse",
      "Scalare la produzione senza perdere qualità né controllo dei costi quando arrivano picchi di matrimoni o stagione di eventi",
      "Coordinare team temporanei e personale fisso con turni, contratti per evento e costi del lavoro chiari",
      "Reporting finanziario a investitori o soci con dati consolidati, non Excel improvvisati",
      "Acquisire clienti aziendali con proposte professionali che chiudano contratti di maggiore valore",
      "Decidere quali eventi accettare e quali rifiutare con dati di margine reale, non per sensazione"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Proprietario di Catering",
    "features": [
      {
        "title": "Catering AI+",
        "description": "Agente specializzato in eventi gastronomici: matrimoni, aziendali, cocktail e galà con conoscenza professionale.",
        "icon": "PartyPopper"
      },
      {
        "title": "Kit Plan Financiero",
        "description": "Cash flow, P&L mensile, dashboard di indicatori e redditività per evento e per cliente. Modelli professionali adattati al catering.",
        "icon": "FileText"
      },
      {
        "title": "Schede Tecniche per Evento",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica CSV; Kit de Escandallos Pro lo gestisce con i tuoi prezzi reali e margine obiettivo.",
        "icon": "Calculator"
      },
      {
        "title": "Kit Gestión de Personal",
        "description": "Turni per personale fisso e temporaneo, contratti per evento, controllo ore e costi del lavoro per servizio.",
        "icon": "Users"
      },
      {
        "title": "HACCP e certificazioni",
        "description": "Pack APPCC con modelli adattati al catering: tracciabilità, trasporto e registri pronti per ispezioni e clienti aziendali.",
        "icon": "ShieldCheck"
      },
      {
        "title": "BlogPost SEO Gen+ + MenuDish Local SEO",
        "description": "Suite SEO per acquisire clienti aziendali con traffico organico e migliore posizionamento.",
        "icon": "Sparkles"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronomica con IA per proposte ai clienti, presentazioni e galleria web.",
        "icon": "Image"
      },
      {
        "title": "Dashboard delle operazioni",
        "description": "KPI finanziari consolidati, tasso di occupazione, redditività per linea di business (matrimoni, aziendali, cocktail).",
        "icon": "BarChart3"
      },
      {
        "title": "Sonar Deep Research",
        "description": "Ricerca approfondita di mercato, concorrenti e tendenze per decisioni strategiche di crescita.",
        "icon": "Search"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Proprietario di Catering con AI Chef Pro",
    "workflow": [
      "08:30 · Kit Plan Financiero — apri la dashboard e rilevi che un evento del fine settimana ha margine al 18%, sotto l'obiettivo (28%).",
      "09:30 · Kit de Escandallos Pro — analizzi la scheda tecnica dell'evento e aggiusti il menù o il prezzo prima di chiudere il contratto.",
      "11:00 · Catering AI+ — chiudi proposta per azienda cliente con presentazione generata con IA e validata con l'agente.",
      "12:30 · GastroIMG Gen+ — generi le fotografie dei piatti del menù proposto da includere nella presentazione.",
      "14:00 · Riunione con cliente aziendale — presenti proposta chiusa in 1 ora invece dei 3 giorni tradizionali.",
      "16:30 · Kit Plan Financiero — validi il previsional del trimestre, esporti in PDF per riunione con soci.",
      "18:00 · Kit Gestión de Personal — rivedi i turni del fine settimana con personale fisso e temporaneo, firmi contratti per evento.",
      "20:00 · BlogPost SEO Gen+ — pubblichi un post sull'ultimo grande evento aziendale per acquisire nuovi clienti organicamente."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Aziende di Catering",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-tareas-catering",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "AI Chef Pro mi ha dato controllo finanziario reale. So esattamente in quali eventi guadagno e in quali no, e questo mi ha permesso di dire no a clienti che non erano redditizi. Nel primo trimestre abbiamo alzato 4 punti di margine senza toccare i prezzi. Solo aggiustando i menù e rifiutando eventi sbagliati.",
    "testimonialAuthor": "Roberto Iglesias",
    "testimonialRole": "Proprietario, azienda di catering aziendale (2M€ fatturato annuo)",
    "faqTitle": "Domande Frequenti dei Proprietari di Catering",
    "faqs": [
      {
        "q": "È adatto per catering boutique con meno di 5 dipendenti?",
        "a": "Sì. È ideale per boutique perché consolida operatività, finanza, marketing e proposte ai clienti in un unico strumento. Il cliente tipico inizia con 1 piano personale e cresce fino a diventare azienda."
      },
      {
        "q": "E per aziende grandi con 50+ dipendenti temporanei?",
        "a": "Anche. Il Kit Gestión de Personal scala a team grandi con turni, contratti per evento e consolidamento dei costi del lavoro. Ci sono clienti con 100+ servizi al mese."
      },
      {
        "q": "Si integra con il mio software contabile o ERP?",
        "a": "Esporta Excel, PDF e CSV compatibili con la maggior parte degli ERP e dei commercialisti. Il tuo team finanziario riceve documentazione pronta da integrare."
      },
      {
        "q": "Esiste un piano aziendale per catering grande?",
        "a": "Sì. A partire da un certo fatturato ci sono piani aziendali con onboarding personalizzato, dashboard consolidate, formazione del team centrale e supporto prioritario."
      },
      {
        "q": "Come mi aiuta ad acquisire clienti aziendali?",
        "a": "BlogPost SEO Gen+ e MenuDish Local SEO catturano traffico organico verso il tuo sito; Catering AI+ aiuta a redigere proposte professionali; GastroIMG Gen+ genera fotografie per presentazioni; Keyword Discovery AI+ trova le ricerche reali delle aziende nella tua zona."
      },
      {
        "q": "È sicuro affidare il piano finanziario a un'IA?",
        "a": "Sì. Il Kit Plan Financiero è un modello Excel professionale con formule precaricate, non IA. Tu inserisci i dati reali e lo strumento calcola. Gli agenti IA vengono usati solo per supportare decisioni, redazione di proposte e analisi, non per calcoli finanziari critici."
      }
    ],
    "ctaTitle": "Fai crescere il tuo catering con margine reale, non intuizione.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Aziende di Catering: Redditività e Piano Finanziario",
      "description": "Suite di IA per aziende di catering: redditività per evento, produzione su scala, team temporanei, piano finanziario e acquisizione clienti aziendali. Inizia oggi.",
      "keywords": "IA azienda catering, proprietario catering IA, software catering, gestione azienda catering, piano finanziario catering, redditività catering, acquisizione clienti aziendali catering, scalare azienda catering, proprietario catering Italia",
      "ogImage": "https://aichef.pro/og/use-cases/propietario-catering.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Azienda dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di catering gestisci (matrimoni, aziendali, cocktail, galà), dimensione media dell'evento, città e volume annuo. Da quel momento, ogni agente —da Catering AI+ al Piano Finanziario— risponde adattato al tuo contesto: tipi di servizio, scala reale e mercato di riferimento. Non è un modulo: è una breve conversazione che rende la suite davvero utile per la tua azienda.",
    "appsTitle": "Gli Agenti IA che Userai come Proprietario di Catering",
    "apps": [
      {
        "name": "Catering AI+",
        "description": "Agente principale: matrimoni, aziendali, cocktail e galà con conoscenza professionale.",
        "category": "Concetti di Business"
      },
      {
        "name": "Manager Ristorante Pro",
        "description": "Assistente operativo e finanziario per supportarti nelle decisioni e nel reporting ai soci.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di menù per eventi con ricetta + scheda tecnica CSV pronta per il Kit de Escandallos Pro.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dolci per eventi e banchetti con tecnica professionale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Calcula Pax",
        "description": "Calcolatrice di porzioni che scala ricette a 50, 200 o 500 commensali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta, critica per eventi grandi.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Post di blog per catturare traffico organico verso il tuo sito di catering.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Descrizioni SEO per migliorare il posizionamento web del tuo catering.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Keyword Discovery AI+",
        "description": "Ricerca di parole chiave per acquisire aziende che cercano catering nella tua zona.",
        "category": "Contenuti e Social"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica per proposte ai clienti e presentazioni commerciali.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca di mercato, concorrenti e tendenze del settore eventi.",
        "category": "Modelli IA + LLM"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching per gestione dello stress, decisioni difficili e conversazioni con soci o team.",
        "category": "Strumenti e Utility"
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "margine nel primo trimestre"
      },
      {
        "value": "×3",
        "label": "velocità chiusura proposte"
      },
      {
        "value": "−40 %",
        "label": "tempo nel reporting finanziario"
      },
      {
        "value": "12+",
        "label": "agenti per la tua azienda"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Non sapere quale dei 50 eventi del mese è realmente redditizio",
        "Chiudere proposte a clienti aziendali in 3 giorni con modelli Word",
        "Turni di personale temporaneo in Excel manuale senza controllo dei costi",
        "HACCP disomogeneo tra eventi, problema con clienti aziendali esigenti",
        "Marketing improvvisato o esternalizzato a prezzo alto senza acquisire lead organici"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Redditività per evento e per cliente chiara, decisioni di accettare/rifiutare con dati",
        "Chiudere proposte in 1 ora con Catering AI+ + GastroIMG Gen+ + presentazione professionale",
        "Turni con Kit Gestión de Personal: controllo ore e costi consolidati",
        "HACCP unificato e professionale, pronto per qualsiasi ispezione o cliente aziendale",
        "Suite SEO che acquisisce lead organici senza spese in agenzie"
      ]
    },
    "galleryTitle": "La Giornata Tipo di un Proprietario di Catering, in Immagini",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: pricing, proposte ai clienti, eventi su larga scala, team, magazzino logistico e reporting finanziario.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-event.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-pricing.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-storage.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-catering-presentation.jpg"
    ]
  },
  "propietario-restaurante": {
    "h1": "IA per Proprietari di Ristorante",
    "heroSubtitle": "Prendi decisioni migliori, recupera ore amministrative e aumenta la redditività del tuo ristorante con una suite di agenti IA specializzati nella ristorazione.",
    "heroTagline": "Il tuo partner digitale per gestire il business con i dati",
    "badge": "Per proprietari e titolari di ristorante",
    "painsTitle": "Ciò che un proprietario di ristorante non può evitare di risolvere",
    "pains": [
      "Margine ristretto: è difficile sapere quali piatti rendono e quali drenano la redditività senza un'analisi precisa",
      "Poco tempo per rivedere costi, schede tecniche, fornitori e comunicazione con il team",
      "Decisioni su menu, prezzi e promozioni prese più per intuizione che per dati",
      "Team a rotazione: formare, supervisionare e gestire i turni consuma ore ogni settimana",
      "Reporting finanziario al commercialista o agli investitori che richiede documenti puliti e consolidati",
      "Marketing e comunicazione costanti (social, web, email) che distraggono dal business vero e proprio"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Proprietario",
    "features": [
      {
        "title": "Manager Ristorante Pro",
        "description": "Agente specializzato per supportare il proprietario nelle operazioni quotidiane, nelle decisioni di team e nel reporting agli investitori.",
        "icon": "BriefcaseBusiness"
      },
      {
        "title": "Piano finanziario professionale",
        "description": "Kit Plan Financiero: cash flow, punto di pareggio, P&L mensile e dashboard di indicatori. Modelli pronti per investitori e banche.",
        "icon": "FileText"
      },
      {
        "title": "Schede tecniche professionali",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica iniziale CSV con prezzi di riferimento; il Kit Escandallos Pro lo gestisce con i tuoi prezzi reali.",
        "icon": "Calculator"
      },
      {
        "title": "HACCP e sicurezza alimentare",
        "description": "Pack APPCC con 17 modelli pronti per l'ispezione, registrazioni da mobile ed esportazione in PDF.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gestione del personale e dei turni",
        "description": "Kit Gestione del Personale: quadranti, controllo ore, indicatori di produttività e onboarding di nuovi dipendenti.",
        "icon": "Users"
      },
      {
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Suite di marketing e SEO locale: descrizioni dei piatti, blog e campagne con IA per attirare traffico organico.",
        "icon": "Sparkles"
      },
      {
        "title": "Keyword Discovery AI+",
        "description": "Ricerca di parole chiave gastronomiche locali per posizionare il tuo ristorante su Google senza pagare un'agenzia.",
        "icon": "Search"
      },
      {
        "title": "Pasto del Personale",
        "description": "Generatore di menu per lo staff che risparmia costi mantenendo motivato il team di cucina e sala.",
        "icon": "BarChart3"
      },
      {
        "title": "Mental Coach",
        "description": "Coaching psicologico per ristoratori: gestione dello stress, equilibrio lavoro-vita e direzione di team in settori ad alta pressione.",
        "icon": "MessageSquare"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Proprietario con AI Chef Pro",
    "workflow": [
      "08:30 · Caffè e dashboard — apri il Kit Plan Financiero e rivedi gli indicatori del giorno precedente. Rilevi che il food cost è salito al 33% a causa degli sprechi di pesce.",
      "09:30 · Manager Ristorante Pro — chiedi un'analisi della causa all'agente e ottieni 3 azioni concrete per questa settimana.",
      "10:30 · MenuDish Local SEO — aggiorni la descrizione dei 4 piatti top su Google Business e sul web con parole chiave rilevate da Keyword Discovery AI+.",
      "12:30 · Servizio di mezzogiorno — supervisioni la sala supportato dalla checklist del Kit di Attività Ristorante Casual.",
      "15:30 · Riunione con il commercialista — esporti P&L mensile, dashboard di indicatori e quadrante del personale in PDF direttamente dal Kit Plan Financiero. Riunione chiusa in 30 minuti.",
      "17:00 · Cucina Creativa — chiedi idee per il menu di stagione in arrivo. L'agente fornisce 8 piatti con ricetta e scheda tecnica CSV.",
      "18:30 · Decisione di team — usi Mental Coach per preparare la conversazione difficile con un dipendente chiave. Porti struttura e argomenti alla riunione.",
      "21:00 · Chiusura — il manager ti invia il report automatico del giorno via WhatsApp. Vai a casa senza scartoffie in sospeso."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Proprietari",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Prima passavo 6 ore a settimana solo a quadrare i numeri tra Excel e tovaglioli. Con AI Chef Pro lo chiudo in un'ora con dashboard professionali. Ho recuperato il controllo finanziario dei miei due locali e il margine è salito di 3 punti nel primo trimestre.",
    "testimonialAuthor": "Carlos Méndez",
    "testimonialRole": "Proprietario, gruppo di bistrot mediterranei (2 locali)",
    "faqTitle": "Domande Frequenti dei Proprietari",
    "faqs": [
      {
        "q": "Quale dimensione di ristorante si adatta ad AI Chef Pro?",
        "a": "Da un singolo locale familiare fino a gruppi con più di 10 ristoranti. I modelli scalano in base al volume e i piani si adattano all'uso reale. Ci sono clienti con 1 locale e altri con 25 unità attive."
      },
      {
        "q": "Ho bisogno di competenze tecniche?",
        "a": "No. Se sai usare WhatsApp ed Excel a livello base, sai già usare AI Chef Pro. L'onboarding inizia con l'agente «Chi sono?», che in 2 minuti adatta il sistema a te, al tuo business e alla tua zona geografica. Ci sono video brevi di onboarding e supporto diretto via WhatsApp."
      },
      {
        "q": "Sostituisce il mio commercialista o consulente?",
        "a": "No, ma rende la vita molto più facile. Il tuo commercialista riceve documenti puliti e tu arrivi alle riunioni con dati consolidati. La maggior parte degli studi commerciali finisce per raccomandare AI Chef Pro ad altri clienti."
      },
      {
        "q": "Quanto tempo ci metto per vedere i risultati?",
        "a": "La maggior parte dei proprietari riporta tra 4 e 6 ore settimanali recuperate nella prima settimana di utilizzo. L'impatto sul margine è di solito tra 2 e 5 punti percentuali in 60-90 giorni, grazie alla riprogettazione dei piatti con food cost alto e al controllo degli sprechi."
      },
      {
        "q": "Come mi aiuta con il marketing e la SEO locale?",
        "a": "La suite Contenuti e Social include MenuDish Local SEO (descrizioni dei piatti ottimizzate), BlogPost SEO Gen+ (post per attirare traffico organico) e Keyword Discovery AI+ (parole chiave gastronomiche locali). Riduci la spesa in agenzie di marketing e catturi prenotazioni dirette."
      },
      {
        "q": "Ci sono sconti per gruppi con più locali?",
        "a": "Sì. A partire da 5 unità attive ci sono piani aziendali con onboarding personalizzato e dashboard consolidate per gruppo."
      }
    ],
    "ctaTitle": "Gestisci il tuo ristorante con i dati, non con l'intuizione.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Proprietari di Ristorante: Piano, Food Cost, SEO",
      "description": "Suite di IA per proprietari di ristorante: agenti specializzati, piano finanziario, schede tecniche professionali, HACCP, marketing e SEO locale. Inizia oggi.",
      "keywords": "IA proprietario ristorante, titolare ristorante IA, software gestione ristorante proprietari, piano finanziario ristorante IA, schede tecniche ristorante, marketing ristorante IA, SEO locale ristorante, agente IA ristorazione, proprietario ristorante Italia",
      "ogImage": "https://aichef.pro/og/use-cases/propietario-restaurante.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Business dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di ristorante hai, in quale città, quanti locali, quale ticket medio gestisci e come lavori. Da quel momento, ogni agente —dal Piano Finanziario alla SEO locale— risponde adattato al tuo contesto: prezzi di mercato della tua zona, normative del tuo paese e scala reale della tua operazione. Non è un modulo: è una conversazione breve che rende ogni strumento davvero utile per il tuo business.",
    "appsTitle": "Gli Agenti IA che Userai come Proprietario",
    "apps": [
      {
        "name": "Manager Ristorante Pro",
        "description": "Assistente operativo e finanziario per supportarti nelle decisioni di team, nel reporting e nelle operazioni quotidiane.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Specialista in bistrot, gastropub, tapas e cucina mediterranea: lo spettro casual completo con base professionale.",
        "category": "Concetti di Business"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Descrizioni dei piatti ottimizzate per la SEO locale su Google Business e web.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Post di blog che attirano traffico organico locale verso il tuo ristorante.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Keyword Discovery AI+",
        "description": "Ricerca di parole chiave gastronomiche locali per zona postale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di piatti professionali con ricetta + scheda tecnica iniziale CSV (prezzi di riferimento) pronto per il Kit Escandallos Pro.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi su sprechi e rese per ingrediente, essenziali per una scheda tecnica realistica.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta e piatto, pronta per la normativa.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Pasto del Personale",
        "description": "Generatore di menu per lo staff che risparmia costi mantenendo motivato il team.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching psicologico per ristoratori: stress, team e decisioni difficili.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Gastro Calendar",
        "description": "Calendario gastronomico con date chiave, idee e hashtag per social e blog.",
        "category": "Contenuti e Social"
      },
      {
        "name": "InstaFlow AI Pro + Pinterest Pins Gen",
        "description": "Contenuto virale per Instagram e Pinterest senza agenzia.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+3 pp",
        "label": "margine in 60-90 giorni"
      },
      {
        "value": "−6 h",
        "label": "settimanali in gestione"
      },
      {
        "value": "×2",
        "label": "prenotazioni dirette via SEO locale"
      },
      {
        "value": "12+",
        "label": "agenti IA per il tuo ruolo"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "6 ore settimanali a quadrare Excel, tovaglioli e note dei fornitori",
        "Decisioni su menu e pricing per intuizione, non per analisi del food cost reale",
        "Reporting al commercialista con file sparsi in Word, Excel ed email",
        "Marketing improvvisato o esternalizzato a prezzi elevati senza sapere cosa funziona",
        "Stress costante e calo nei festivi per non mollare il controllo"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "1 ora settimanale chiudendo dashboard professionali con KPI chiari",
        "Decisioni su menu e pricing con scheda tecnica professionale e analisi del margine",
        "Reporting al commercialista in PDF direttamente dal Kit Plan Financiero",
        "SEO locale automatizzata e suite di marketing IA riducendo la spesa in agenzie",
        "Tranquillità: il team ti invia report automatici via WhatsApp"
      ]
    },
    "galleryTitle": "La Giornata Tipo di un Proprietario, in Immagini",
    "gallerySubtitle": "Quello che potrai gestire con AI Chef Pro: dashboard finanziari, decisioni operative, team, sala e reporting.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-tablet.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-meeting.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-numbers.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-propietario-restaurante-dining.jpg"
    ]
  },
  "repostero-pastelero": {
    "h1": "IA per Pasticcere e Pasticciere",
    "heroSubtitle": "Domina la tecnica di pasticceria professionale, scheda tecnica per pezzo con costo ora laboratorio, pianifica la produzione stagionale e cattura il branding artigianale con una suite di agenti IA gastronomici specializzati in pasticceria e pasticceria d'autore.",
    "heroTagline": "Pasticceria con tecnica autentica e margine reale",
    "badge": "Per pasticceri, pasticcieri e chef pâtissier",
    "painsTitle": "Quello che un Pasticciere Non Può Evitare di Risolvere",
    "pains": [
      "Tecnica avanzata impegnativa: sfoglia, paste brisée e sablée, biscuit, ganache, glassature, mousse con bilanciamento preciso",
      "Scarti elevati in laboratorio (formatura, cottura, decorazione) che intaccano la redditività senza controllo",
      "Standardizzare i pezzi signature turno dopo turno con consistenza professionale",
      "Stagionalità molto forte: Panettone, Pasqua, San Valentino, Natale concentrano un'alta percentuale dell'anno",
      "Differenziarsi con pasticceria d'autore, presentazione premium e storytelling di tecnica francese o moderna",
      "Gestire ordini di torte personalizzate, eventi privati e matrimoni con margine mentre si gestisce la pasticceria quotidiana"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Pasticciere",
    "features": [
      {
        "title": "Pasticceria Creativa",
        "description": "Agente specializzato in pasticceria professionale, dessert da ristorante, torte personalizzate e pasticceria da forno con tecnica avanzata.",
        "icon": "Cake"
      },
      {
        "title": "Cioccolateria Creativa",
        "description": "Per combinazioni avanzate pasticceria + cioccolato: ganache, cremosi, glassature.",
        "icon": "Cookie"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per lo sviluppo di dessert signature e combinazioni di sapori con criterio tecnico.",
        "icon": "Sparkles"
      },
      {
        "title": "Schede tecniche con costo ora laboratorio",
        "description": "Pasticceria Creativa fornisce ricetta + scheda tecnica CSV; il Kit Escandallos Pro lo gestisce con costo ora laboratorio integrato nel margine reale per pezzo.",
        "icon": "Calculator"
      },
      {
        "title": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture, gelificanti, neutri e tecnica avanzata.",
        "icon": "Beaker"
      },
      {
        "title": "Kit di Attività Pasticceria",
        "description": "Modelli: preparazione impasti, produzione, formatura, cottura, decorazione, vetrina, conservazione.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pacchetto HACCP pasticceria",
        "description": "Tracciabilità di uova, creme, frutta secca e conservazione professionale.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Panettone, San Valentino, Pasqua, Natale, comunioni, Festa della Mamma.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Fotografia artigianale IA di riferimento + Pinterest, dove la pasticceria cattura traffico organico stabile.",
        "icon": "Image"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Pasticciere con AI Chef Pro",
    "workflow": [
      "06:00 · Apertura — checklist Kit di Attività Pasticceria: rinfresco lievito madre, montaggio torte, preparazione creme.",
      "08:00 · Pasticceria Creativa — sviluppi un nuovo dessert per San Valentino. Cucina Creativa fornisce ricetta + scheda tecnica CSV.",
      "09:00 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali e costo ora laboratorio, validi il margine per pezzo.",
      "11:00 · Produzione del giorno — formatura, cottura, decorazione con modelli specifici.",
      "14:00 · Rifornimento vetrina con etichette e prezzi.",
      "16:00 · Gastro Calendar — prepari la pianificazione del Panettone con 8 settimane di anticipo.",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — generi immagine di riferimento del nuovo dessert + pin.",
      "20:00 · Chiusura — pulizia profonda, HACCP firmato, pianificazione del giorno successivo."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Pasticciere",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Pasticceria Creativa + Sosa Ingredients AI mi hanno cambiato la proposta. I miei dessert signature ora hanno una tecnica documentata che il mio team replica con consistenza, le schede tecniche con costo ora laboratorio mi hanno dato 6 punti in più di margine e gli ordini di torte personalizzate si chiudono in una chiamata con proposta professionale.",
    "testimonialAuthor": "Eva Mata",
    "testimonialRole": "Chef pâtissière, pasticceria d'autore",
    "faqTitle": "Domande Frequenti dei Pasticcieri",
    "faqs": [
      {
        "q": "Va bene per pasticciere di ristorante, pasticciere artigianale o chef pâtissier d'hotel?",
        "a": "Per tutti e tre. Pasticceria Creativa copre dalla pasticceria artigianale all'alta pasticceria da ristorante con tecnica francese avanzata."
      },
      {
        "q": "Copre la tecnica avanzata (sfoglia, mousse, glassature)?",
        "a": "Sì. Pasticceria Creativa ragiona come uno chef pâtissier professionista: sfoglia invertita, paste lavorate con tecnica, mousse bilanciate, glassature con copertura tecnica."
      },
      {
        "q": "Copre pasticceria + cioccolateria?",
        "a": "Sì. Cioccolateria Creativa integra con praline, ganache, pralinati e tecnica di temperaggio per pezzi combinati."
      },
      {
        "q": "Genera contenuti visivi per vetrina e social?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali; Pinterest Pins Gen cattura traffico organico stabile. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo pezzo reale."
      },
      {
        "q": "Come mi aiuta con eventi e stagioni?",
        "a": "Gastro Calendar pianifica le stagioni chiave (Panettone, San Valentino, Pasqua, Natale, comunioni) con anticipo."
      }
    ],
    "ctaTitle": "La tua pasticceria con tecnica d'autore e margine reale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "IA per Pasticciere: Tecnica, Schede Tecniche e Stagionalità | AI Chef Pro",
      "description": "Suite IA per pasticcieri professionisti: Pasticceria Creativa, schede tecniche con costo ora laboratorio, pianificazione stagionale e branding. Inizia oggi.",
      "keywords": "IA pasticciere, IA pasticciere, IA chef pâtissier, software pasticceria, schede tecniche pasticceria, tecnica francese, pasticceria d'autore",
      "ogImage": "https://aichef.pro/og/use-cases/repostero-pastelero.jpg"
    },
    "personalizationTitle": "Personalizzato alla Tua Pasticceria dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding di 2 minuti in cui racconti che tipo di pasticceria lavori (chef pâtissier di ristorante, pasticciere artigianale, pasticciere d'hotel, pasticceria per eventi), dimensione del team, città e specialità.",
    "appsTitle": "Gli Agenti IA che Userai come Pasticciere",
    "apps": [
      {
        "name": "Pasticceria Creativa",
        "description": "Agente specializzato in pasticceria professionale con tecnica avanzata.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cioccolateria Creativa",
        "description": "Per praline, ganache e combinazioni avanzate.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di dessert signature con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Panificazione Creativa",
        "description": "Per brioche, croissant, ensaimadas e pasticceria da forno complementare.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture, gelificanti e tecnica avanzata.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Assistente del catalogo tSpoonLab per applicazioni avanzate.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Scarti in laboratorio, formatura, cottura e vetrina.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica per pezzo: glutine, lattosio, frutta secca, uova.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia artigianale IA di riferimento per vetrina, web e social.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale per pasticceria d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico stabile per torte e dessert.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Panettone, San Valentino, Pasqua, Natale, Festa della Mamma.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margine dopo schede tecniche pezzi"
      },
      {
        "value": "−30 %",
        "label": "scarti laboratorio"
      },
      {
        "value": "×2",
        "label": "traffico organico via Pinterest"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo laboratorio"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Tecnica improvvisata, dessert signature inconsistenti",
        "Schede tecniche senza costo ora laboratorio",
        "Scarti in laboratorio senza tracciabilità reale",
        "Vetrina e social improvvisati con foto dal telefono",
        "Stagionalità reattiva, arrivi tardi al Panettone"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Tecnica documentata, dessert signature consistenti",
        "Scheda tecnica professionale con costo ora laboratorio integrato",
        "Scarti controllati con Sprechi GenCal",
        "GastroIMG Gen+ + Pinterest Pins Gen catturano traffico stabile",
        "Panettone e stagioni pianificate con 8 settimane di anticipo"
      ]
    },
    "galleryTitle": "Come Funziona il Laboratorio di un Pasticciere",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: piping, torte, mise en place, vetrina e team. Immagini generate con IA come riferimento visivo del concetto.",
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
    "h1": "IA per Ristorante Casual",
    "heroSubtitle": "Ottimizza l'operatività quotidiana, controlla il food cost e recupera ore di burocrazia nel tuo ristorante casual con una suite di agenti IA specializzati nel settore della ristorazione.",
    "heroTagline": "Il ristorante casual moderno ha bisogno di IA",
    "badge": "Per ristoranti casual e bistrot",
    "painsTitle": "Cosa un Ristorante Casual Non Può Evitare di Risolvere",
    "pains": [
      "Margine ridotto che richiede controllo millimetrico di costi e sprechi in cucina",
      "Alta rotazione del personale: formare e supervisionare nuovi cuochi e camerieri richiede ore ogni settimana",
      "Menu ampio con molti piatti da ricalcolare quando i prezzi dei fornitori cambiano",
      "HACCP e normative sempre aggiornati senza che la burocrazia rubi tempo alla sala",
      "Attrarre clienti in una zona competitiva: SEO locale, social e recensioni sono fondamentali",
      "Coordinare cucina, sala e delivery nei picchi di servizio senza intoppi"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Ristorante Casual",
    "features": [
      {
        "title": "Ristoranti Casual AI+",
        "description": "Agente specializzato in bistrot, gastropub, tapas e cucina mediterranea: lo spettro casual completo con base professionale.",
        "icon": "UtensilsCrossed"
      },
      {
        "title": "Scheda tecnica professionale",
        "description": "Cucina Creativa fornisce ricetta + scheda tecnica CSV; Kit de Escandallos Pro lo gestisce con i tuoi prezzi reali e margine obiettivo.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelli pronti: apertura, chiusura, partite di cucina, sala, delivery ed eventi.",
        "icon": "CheckSquare"
      },
      {
        "title": "HACCP e tracciabilità",
        "description": "Pack APPCC con 17 modelli, registri dal cellulare, alert e esportazione in PDF pronta per l'ispezione.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Kit Gestión de Personal",
        "description": "Turni in minuti rispettando il contratto collettivo, pause, controllo delle ore e indici di produttività.",
        "icon": "Users"
      },
      {
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Suite SEO locale per attrarre clienti organicamente senza pagare agenzie.",
        "icon": "Sparkles"
      },
      {
        "title": "Kit Plan Financiero",
        "description": "Dashboard di indicatori, food cost, produttività e ticket medio. Reporting al proprietario in PDF.",
        "icon": "BarChart3"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia gastronomica IA per web e social, contenuti per Instagram con calendario editoriale.",
        "icon": "Image"
      },
      {
        "title": "Keyword Discovery AI+",
        "description": "Ricerca di parole chiave gastronomiche locali per zona postale per un posizionamento reale.",
        "icon": "Search"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Ristorante Casual con AI Chef Pro",
    "workflow": [
      "08:30 · Apertura — checklist del Kit de Tareas Restaurante Casual e controllo inventario in 10 minuti.",
      "10:00 · Ristoranti Casual AI+ — chiedi all'agente suggerimenti per il piatto del giorno con il prodotto che hai in cella.",
      "10:30 · Cucina Creativa + Kit de Escandallos Pro — calcoli il food cost del piatto del giorno con i tuoi prezzi e verifichi il margine.",
      "12:30 · Servizio di mezzogiorno — cucina, sala e delivery coordinati con modelli. Sprechi registrati dal cellulare con HACCP.",
      "15:30 · Kit Plan Financiero — rivedi i KPI del giorno precedente e rilevi che il food cost del lunedì è salito al 32%, identifichi la causa.",
      "17:00 · MenuDish Local SEO — aggiorni le descrizioni dei 6 piatti top su Google Business e sul web.",
      "18:00 · Kit Inventario — validi gli ordini ai fornitori con confronto prezzi e alert di stock minimo.",
      "23:30 · Chiusura — HACCP firmato, report giornaliero al proprietario in PDF direttamente dal Kit Plan Financiero."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Ristorante Casual",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Abbiamo 80 coperti e alta rotazione del personale. Il Kit de Tareas Restaurante Casual e il Pack APPCC ci hanno ordinato tutta l'operatività. Andiamo come un orologio svizzero e il food cost è sceso di 3 punti nel primo trimestre solo grazie a un buon calcolo dei costi.",
    "testimonialAuthor": "Sandra López",
    "testimonialRole": "Manager, ristorante casual mediterraneo da 80 coperti",
    "faqTitle": "Domande Frequenti dei Ristoranti Casual",
    "faqs": [
      {
        "q": "Funziona per ristoranti da 30, 80 o 150 coperti?",
        "a": "Sì. I modelli scalano in base al volume e i piani si adattano all'uso reale. Ci sono clienti da 30 coperti fino a catene di 25 unità."
      },
      {
        "q": "Copre anche il delivery oltre alla sala?",
        "a": "Sì. Il Kit de Tareas Restaurante Casual include modelli specifici per la gestione del delivery, sprechi associati e coordinamento con piattaforme come Glovo, Uber Eats e Just Eat."
      },
      {
        "q": "Sostituisce il mio POS o software di prenotazioni?",
        "a": "No, integra. Cover Manager o The Fork gestiscono le prenotazioni e il POS gestisce le vendite; AI Chef Pro gestisce costi, personale, HACCP, inventario e SEO locale. I dati sono compatibili tramite Excel."
      },
      {
        "q": "Quanto tempo impiega il team per impararlo?",
        "a": "Curva reale di 1-2 giorni. C'è un video di onboarding di 5 minuti, supporto via WhatsApp e tutto parte con l'agente «Chi sono?» che adatta il sistema al tuo ristorante in 2 minuti."
      },
      {
        "q": "Come mi aiuta con la SEO locale e l'acquisizione clienti?",
        "a": "Suite Contenuti e Social: MenuDish Local SEO (descrizioni dei piatti), BlogPost SEO Gen+ (post del blog), Keyword Discovery AI+ (parole chiave per zona postale), InstaFlow AI Pro (Instagram) e Pinterest Pins Gen."
      },
      {
        "q": "C'è un agente specifico per il mio tipo di ristorante casual?",
        "a": "Sì. Ristoranti Casual AI+ copre bistrot, gastropub, tapas, mediterraneo, mesones, braseria casual. Per concetti più specifici ci sono Burger Pro AI+, Food Truck AI+ e agenti per paese (messicana, peruviana, giapponese, ecc.)."
      }
    ],
    "ctaTitle": "Metti ordine nel tuo ristorante casual.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Ristorante Casual: Operatività, Food Cost e SEO Locale",
      "description": "Suite di IA per ristoranti casual e bistrot: agenti specializzati, food cost, HACCP, turni, SEO locale e marketing con base professionale. Inizia oggi.",
      "keywords": "IA ristorante casual, software ristorante casual, gestione bistrot IA, food cost casual, HACCP ristorante casual, marketing ristorante casual IA, SEO locale ristorante, ristorante casual Italia",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-casual.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Ristorante dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di casual gestisci (mediterraneo, bistrot, gastropub, mesón, tapas), numero di coperti, città e modo di lavorare. Da quel momento, ogni agente —da Ristoranti Casual AI+ a MenuDish Local SEO— risponde adattato al tuo contesto: ticket medio della tua zona, normative e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Ristorante Casual",
    "apps": [
      {
        "name": "Ristoranti Casual AI+",
        "description": "Agente principale: bistrot, gastropub, tapas e cucina mediterranea con base professionale.",
        "category": "Concetti di Business"
      },
      {
        "name": "Manager Ristorante Pro",
        "description": "Assistente operativo e reporting al proprietario.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di piatti professionali con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi su sprechi e rese per il controllo di cucina.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta e piatto.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Pasto del Personale",
        "description": "Generatore di menu per lo staff con il prodotto che hai già in cella.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Descrizioni dei piatti ottimizzate per la SEO locale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Post del blog per attrarre traffico organico locale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Keyword Discovery AI+",
        "description": "Parole chiave gastronomiche per zona postale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Contenuti virali per Instagram con calendario editoriale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA per web e social media.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching per la gestione dello stress in alta pressione e conversazioni difficili.",
        "category": "Strumenti e Utility"
      }
    ],
    "metrics": [
      {
        "value": "−3 pp",
        "label": "food cost nel primo trimestre"
      },
      {
        "value": "×2",
        "label": "prenotazioni via SEO locale"
      },
      {
        "value": "−6 h",
        "label": "settimanali in gestione"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo ristorante"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Operatività su fogli sparsi con ogni partita che funziona a modo suo",
        "HACCP su carta stampata che si perde prima dell'ispezione",
        "Turni in Excel manuali fatti a mano per ore",
        "Marketing improvvisato senza acquisizione organica di clienti",
        "Food cost a occhio, senza sapere quale piatto perde redditività"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Kit de Tareas con modelli strutturati per turno e partita",
        "HACCP dal cellulare con registri, alert e esportazione in PDF",
        "Turni in minuti con il Kit Gestión de Personal rispettando il contratto collettivo",
        "Suite SEO locale che cattura prenotazioni organiche senza spese in agenzie",
        "Food cost per piatto calcolato in dettaglio con scheda tecnica professionale"
      ]
    },
    "galleryTitle": "Come Funziona un Ristorante Casual Moderno",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: sala, cucina aperta, terrazza, piatto del giorno, team e bancone.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-casual-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-kitchen.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-terrace.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-dish.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-team.jpg",
      "/lovable-uploads/ai-gallery/use-case-casual-bar.jpg"
    ]
  },
  "restaurante-creativo": {
    "h1": "IA per Ristorante Creativo e d'Autore",
    "heroSubtitle": "Brainstorming gastronomico, R&S d'avanguardia, food cost di tecnica avanzata, schede tecniche premium e storytelling per ristoranti d'autore con una suite di agenti di IA gastronomica di livello professionale.",
    "heroTagline": "Creatività con sistema, avanguardia con margine",
    "badge": "Per ristoranti creativi e d'autore",
    "painsTitle": "Cosa un Ristorante Creativo Non Può Evitare di Risolvere",
    "pains": [
      "Menu che cambiano ogni 6-12 settimane con R&S continua e molta sperimentazione",
      "Food cost complessi con tecniche avanzate (sferificazioni, fermentazioni, cotture lunghe, disidratazioni)",
      "Team piccoli con dedizione intensa che necessitano di documentazione professionale, non improvvisazione",
      "Storytelling e comunicazione con clienti, stampa e social sono leve chiave del brand",
      "Menu degustazione lunghi con food cost totale e sequenza coerente di portate",
      "Differenziarsi in una nicchia satura di proposte creative e attrarre il commensale esigente"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Ristorante Creativo",
    "features": [
      {
        "title": "Cucina Creativa + Food Pairing AI",
        "description": "Brainstorming per piatti d'autore per stagione, ingrediente o tecnica con base scientifica. Cucina Creativa fornisce ricetta + food cost CSV.",
        "icon": "Sparkles"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "R&S gastronomica d'avanguardia: koji, kombucha, shoyu, garum, lattofermenti e tecniche innovative con supporto professionale.",
        "icon": "Beaker"
      },
      {
        "title": "VegChef Plant-Based",
        "description": "Cucina plant-based, vegana e vegetariana avanzata per piatti d'autore con tecnica professionale e nutrizionale.",
        "icon": "Leaf"
      },
      {
        "title": "Food cost di tecnica avanzata",
        "description": "Kit de Escandallos Pro: carichi il CSV di Cucina Creativa con i tuoi prezzi reali per piatti con tecniche costose e processi lunghi.",
        "icon": "Calculator"
      },
      {
        "title": "Sonar Deep Research",
        "description": "Ricerca approfondita di tendenze, produttori artigianali, tecniche emergenti e riferimenti dell'avanguardia mondiale.",
        "icon": "Search"
      },
      {
        "title": "BlogPost SEO Gen+",
        "description": "Storytelling per il blog del ristorante, dossier stampa e comunicazione con media gastronomici.",
        "icon": "MessageSquare"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA di alto livello per schede tecniche, stampa, web del ristorante e social.",
        "icon": "Image"
      },
      {
        "title": "Sosa Ingredients AI + tSpoonLab Agent",
        "description": "Assistenti per la selezione di ingredienti tecnici di Sosa e tSpoonLab, essenziali per la cucina d'autore.",
        "icon": "BookOpen"
      },
      {
        "title": "Gastro Lexicum + Pro Prompts eBook",
        "description": "Tutor di definizioni tecniche e scientifiche + 300+ prompt professionali per creatività e comunicazione.",
        "icon": "GraduationCap"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Ristorante Creativo con AI Chef Pro",
    "workflow": [
      "08:30 · Sonar Deep Research — indaghi tendenze e prodotti di stagione nei mercati europei per ispirazione del prossimo cambio di menu.",
      "10:00 · Cucina Creativa + Food Pairing AI — sviluppi 14 piatti per il nuovo menu degustazione con tecnica e food cost CSV iniziale.",
      "12:00 · Fermentus Con AI+ — lavori la base di una fermentazione chiave del menu: koji d'orzo inoculato per 4 piatti.",
      "14:00 · Sosa Ingredients AI + tSpoonLab Agent — selezioni ingredienti tecnici per texture e applicazioni.",
      "15:30 · Kit de Escandallos Pro — carichi i CSV con i tuoi prezzi reali e scarti 4 piatti che non rientrano nel margine obiettivo (32%).",
      "17:00 · Pro Prompts eBook — redigi storytelling per i 10 piatti finali: nome, narrativa e scheda tecnica completa.",
      "18:30 · GastroIMG Gen+ — generi fotografie di ogni piatto per dossier stampa e web del ristorante.",
      "19:30 · Servizio — team coordinato con schede tecniche centralizzate, portate del menu degustazione con sequenza validata."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Ristorante Creativo",
    "productIds": [
      "kit-tareas-restaurante-creativo",
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "Cambio il menu ogni 6 settimane e prima era una settimana di scartoffie di chiusura solo tra food cost, schede tecniche e storytelling. Ora con AI Chef Pro quella chiusura si fa in 2 giorni: Cucina Creativa propone, Fermentus mi dà supporto di R&S, Sonar Deep Research porta tendenze, e il Kit de Escandallos Pro chiude il margine. È letteralmente come avere un team di R&S extra.",
    "testimonialAuthor": "Adrián Lago",
    "testimonialRole": "Chef e proprietario, ristorante d'autore con 30 coperti",
    "faqTitle": "Domande Frequenti dei Ristoranti Creativi",
    "faqs": [
      {
        "q": "L'IA capisce la tecnica d'autore avanzata?",
        "a": "Sì. Cucina Creativa, Fermentus Con AI+, Food Pairing AI, VegChef e i ricettari per paese sono addestrati con conoscenza professionale: tecniche come sferificazioni, fermentazioni lunghe, cotture controllate, gelificazioni, schiume, disidratazioni e processi d'avanguardia."
      },
      {
        "q": "Ci sono menu degustazione specifici?",
        "a": "Sì. Il Kit de Tareas Restaurante Creativo e il Kit de Escandallos Pro hanno modelli per menu degustazione con food cost totale, sequenza di portate e abbinamenti."
      },
      {
        "q": "Copre R&S e prova dei piatti?",
        "a": "Sì. Sonar Deep Research porta tendenze e riferimenti; Cucina Creativa + Fermentus sviluppano piatti; Pro Prompts eBook ha 300+ prompt specifici per R&S iterativa."
      },
      {
        "q": "Genera storytelling per stampa e guide?",
        "a": "Sì. BlogPost SEO Gen+ + Pro Prompts eBook + GastroIMG Gen+ permettono di redigere dossier stampa, comunicazione con guide Michelin/Repsol/50Best e note per media gastronomici."
      },
      {
        "q": "Funziona per la fermentazione d'avanguardia?",
        "a": "Fermentus Con AI+ è l'agente più usato dagli chef d'autore: copre koji, kombucha, shoyu, miso, garum, lattofermenti e processi innovativi con supporto scientifico."
      },
      {
        "q": "Come si integra con Sosa e altri fornitori tecnici?",
        "a": "Sosa Ingredients AI e tSpoonLab Agent sono assistenti specifici del catalogo di ogni fornitore: aiutano a selezionare texture, additivi e applicazioni tecniche con criterio professionale."
      }
    ],
    "ctaTitle": "Creatività con sistema, avanguardia con margine.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Ristorante Creativo e d'Autore: R&S, Avanguardia e Storytelling | AI Chef Pro",
      "description": "Suite di IA per ristoranti creativi e d'autore: Cucina Creativa, Fermentus, Sonar Deep Research, food cost avanzati, schede tecniche e storytelling professionale.",
      "keywords": "IA ristorante creativo, ristorante d'autore IA, software ristorante creativo, food cost creativi, IA gastronomica d'autore, fermentazione creativa IA, Fermentus, ristorante d'autore Italia",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-creativo.jpg"
    },
    "personalizationTitle": "Personalizzato sulla Tua Cucina Creativa dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di cucina creativa guidi (d'autore, gastrobotanica, fermenti, avanguardia, fusione), città e riferimenti. Da quel momento, ogni agente —da Cucina Creativa a Sonar Deep Research— risponde adattato al tuo linguaggio creativo, tecnica abituale e posizionamento reale nel settore.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Ristorante Creativo",
    "apps": [
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di piatti professionali con ricetta + food cost CSV pronto per il Kit de Escandallos Pro.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Combinazioni di ingredienti e abbinamenti con base scientifica.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "R&S d'avanguardia: fermentazioni, koji, kombucha, garum, miso.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "VegChef Plant-Based",
        "description": "Cucina plant-based, vegana e vegetariana avanzata per piatti d'autore.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dessert d'autore con tecnica di pasticceria professionale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Chef Esecutivo Pro",
        "description": "Standardizzazione di schede tecniche e manuali di cucina.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca approfondita: tendenze, produttori, avanguardia mondiale.",
        "category": "Modelli IA + LLM"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Assistente del catalogo Sosa per texture e tecniche avanzate.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Assistente del catalogo tSpoonLab per applicazioni tecniche.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Gastro Lexicum",
        "description": "Tutor con definizioni di tecniche, processi e scienza gastronomica.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica di alto livello per stampa e web.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Post di blog con storytelling per attrarre traffico organico.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "velocità chiusura nuovo menu"
      },
      {
        "value": "14",
        "label": "piatti nel menu degustazione"
      },
      {
        "value": "+5 pp",
        "label": "margine dopo food cost reale"
      },
      {
        "value": "13+",
        "label": "agenti per cucina d'autore"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Chiusura nuovo menu: 15-30 giorni tra R&S, food cost, schede tecniche e storytelling",
        "R&S improvvisata senza documentazione, tecniche che si dimenticano",
        "Storytelling per la stampa redatto di corsa a ogni cambio",
        "Schede tecniche su quaderno inaccessibili durante il servizio",
        "Ricerca di tendenze per intuizione senza accesso a fonti"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Chiusura nuovo menu: 1-3 giorni con Cucina Creativa, Fermentus e Kit de Escandallos Pro",
        "R&S documentata con schede iterative, tecniche tracciate e replicabili",
        "Storytelling professionale generato in ore con BlogPost SEO Gen+",
        "Schede tecniche centralizzate accessibili dal cellulare durante il servizio",
        "Sonar Deep Research porta tendenze e riferimenti professionali"
      ]
    },
    "galleryTitle": "Come Funziona un Ristorante Creativo d'Autore",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: R&S, fermenti, impiattamento d'autore, preparazione di ingredienti speciali e sala intima.",
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
    "h1": "IA per Ristorante Gastronomico (Michelin/Repsol)",
    "heroSubtitle": "Schede tecniche premium, menu degustazione lunghi, brigata estesa, HACCP rigoroso e comunicazione con guide e stampa con una suite di agenti IA pensati per l'alta gastronomia professionale.",
    "heroTagline": "Alta cucina con sistema, avanguardia con direzione",
    "badge": "Per ristoranti gastronomici Michelin e Repsol",
    "painsTitle": "Quello che un Ristorante Gastronomico Non Può Non Risolvere",
    "pains": [
      "Margine esigente con prodotto premium il cui costo cambia ogni settimana in pescheria e mercato",
      "Brigata estesa e altamente coordinata con gerarchia rigorosa e rotazione di chef junior",
      "Menu degustazione lunghi (8-15 portate) con scheda tecnica completa, abbinamento e narrativa coerente",
      "Comunicazione con guide Michelin/Repsol/50Best e stampa specializzata come leva critica",
      "R&D continuo di avanguardia con tecniche avanzate e prodotto di stagione",
      "Prenotazioni con mesi di anticipo con cancellazioni difficili da gestire e operatività di sala impeccabile"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta nell'Alta Gastronomia",
    "features": [
      {
        "title": "Chef Esecutivo Pro",
        "description": "Standardizzazione di schede tecniche e manuali per una brigata estesa con gerarchia rigorosa.",
        "icon": "ChefHat"
      },
      {
        "title": "Cucina Creativa + Food Pairing AI",
        "description": "Brainstorming per piatti del menu degustazione con tecnica e abbinamento. Cucina Creativa fornisce ricetta + scheda tecnica CSV.",
        "icon": "Sparkles"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "R&D di avanguardia: koji, kombucha, shoyu, garum, lattofermenti essenziali nell'alta gastronomia contemporanea.",
        "icon": "Beaker"
      },
      {
        "title": "Schede tecniche premium",
        "description": "Kit de Escandallos Pro: carichi il CSV di Cucina Creativa con i tuoi prezzi reali per prodotto premium con margine calibrato per portata e per menu degustazione completo.",
        "icon": "Calculator"
      },
      {
        "title": "Sosa Ingredients AI + tSpoonLab Agent",
        "description": "Assistenti dei cataloghi professionali più usati in alta cucina per tecniche e applicazioni avanzate.",
        "icon": "BookOpen"
      },
      {
        "title": "Sonar Deep Research",
        "description": "Ricerca approfondita di tendenze mondiali, produttori artigianali, tecniche emergenti e riferimenti dell'avanguardia internazionale.",
        "icon": "Search"
      },
      {
        "title": "BlogPost SEO Gen+ + Pro Prompts eBook",
        "description": "Comunicazione professionale per guide Michelin/Repsol/50Best, dossier stampa e storytelling del menu degustazione.",
        "icon": "MessageSquare"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA di alto livello per web, stampa specializzata e dossier di candidatura alle guide.",
        "icon": "Image"
      },
      {
        "title": "Gastro Lexicum",
        "description": "Tutor con definizioni tecniche, processi e scienza gastronomica per schede tecniche premium e formazione della brigata.",
        "icon": "GraduationCap"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Ristorante Gastronomico con AI Chef Pro",
    "workflow": [
      "08:30 · Sonar Deep Research — indaghi tendenze e prodotto di stagione nei mercati europei per ispirazione del prossimo cambio del menu degustazione.",
      "10:00 · Cucina Creativa + Food Pairing AI — sviluppi 14 portate per il nuovo menu degustazione con tecnica avanzata e scheda tecnica CSV.",
      "12:00 · Fermentus Con AI+ — lavori sulla base di un fermentato chiave del menu: garum di pesce per 4 portate.",
      "14:00 · Sosa Ingredients AI + tSpoonLab Agent — selezioni ingredienti tecnici per texture e applicazioni premium.",
      "15:30 · Kit de Escandallos Pro — carichi i CSV con i tuoi prezzi di mercato e validi il margine del menu degustazione completo (28 €/portata costo medio).",
      "17:00 · Pro Prompts eBook + BlogPost SEO Gen+ — redigi storytelling per le 14 portate, dossier per guide Michelin/Repsol e comunicato stampa.",
      "18:30 · GastroIMG Gen+ — generi fotografie di ogni portata per il sito del ristorante e dossier di candidatura alle guide.",
      "19:30 · Servizio serale — brigata coordinata con schede tecniche centralizzate, portate del menu degustazione con sequenza validata e abbinamento sincronizzato con sommelier."
    ],
    "productsTitle": "Modelli, Kit e Guide Scaricabili per l'Alta Gastronomia",
    "productIds": [
      "guia-restaurante-gastronomico",
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "Avere food cost, scheda tecnica, fermenti documentati e comunicazione con le guide in un unico sistema ci ha ordinato il caos creativo di qualsiasi alta cucina. La Guida Ristorante Gastronomico è stata fondamentale nell'apertura del secondo progetto: business plan professionale che sostiene la candidatura. Premiazione recente con dati alla mano.",
    "testimonialAuthor": "David Aramburu",
    "testimonialRole": "Chef esecutivo, ristorante gastronomico con riconoscimento Michelin/Repsol",
    "faqTitle": "Domande Frequenti dei Ristoranti Gastronomici",
    "faqs": [
      {
        "q": "È adatto per ristorante con stella Michelin o aspirante?",
        "a": "Per entrambi. I modelli e gli agenti sono pensati per alta esigenza: standardizzazione rigorosa, schede tecniche premium, food cost professionale e comunicazione con le guide."
      },
      {
        "q": "Esiste una guida passo passo per aprire un gastronomico?",
        "a": "Sì, la Guida Ristorante Gastronomico (85 €): 65 coperti, business plan modello per candidatura, piano finanziario, piano cucina, brigata, sommelier, manuali operativi e comunicazione con le guide. 20+ deliverable."
      },
      {
        "q": "Copre menu degustazione lunghi da 14-18 portate?",
        "a": "Sì. Il Kit de Escandallos Pro e il Kit de Tareas Restaurante Creativo hanno modelli specifici per menu degustazione con portate, food cost totale, sequenza e abbinamento sincronizzato con sommelier."
      },
      {
        "q": "Genera comunicazione professionale per Michelin, Repsol e 50Best?",
        "a": "Sì. BlogPost SEO Gen+ + Pro Prompts eBook + GastroIMG Gen+ permettono di redigere dossier di candidatura, comunicazione con ispettori, comunicati stampa e materiali per gli uffici delle guide."
      },
      {
        "q": "Funziona per fermentazione d'avanguardia?",
        "a": "Fermentus Con AI+ è uno degli agenti più usati dagli chef Michelin: copre koji, kombucha, shoyu, miso, garum e lattofermenti con supporto scientifico e applicazioni reali nelle portate di alta gastronomia."
      },
      {
        "q": "Come si integra con fornitori premium?",
        "a": "Sosa Ingredients AI e tSpoonLab Agent sono assistenti specifici di cataloghi professionali molto usati in alta gastronomia. Aiutano a selezionare texture, additivi e applicazioni tecniche con criterio di cucina creativa."
      }
    ],
    "ctaTitle": "Alta cucina con sistema, avanguardia con direzione.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Ristorante Gastronomico: Menu Degustazione, R&D | AI Chef Pro",
      "description": "Suite di IA per alta gastronomia: Cucina Creativa, Fermentus, Sonar Deep Research, schede tecniche premium, comunicazione con guide Michelin e Repsol. Inizia oggi.",
      "keywords": "IA ristorante gastronomico, software Michelin, ristorante alta cucina IA, schede tecniche premium, IA Repsol Soles, IA 50Best, fermentazione creativa, Fermentus, menu degustazione IA, gastronomia Spagna",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-gastronomico.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Ristorante Gastronomico dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di cucina guidi (Michelin, Repsol Soles, aspirante, alta cucina contemporanea, fusione d'avanguardia), numero di coperti, città e riferimenti. Da quel momento, ogni agente —da Cucina Creativa a Sonar Deep Research— risponde adattato al tuo linguaggio, tecnica abituale e posizionamento reale nel settore.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Ristorante Gastronomico",
    "apps": [
      {
        "name": "Chef Esecutivo Pro",
        "description": "Standardizzazione di schede tecniche e manuali per brigata estesa.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di portate del menu degustazione con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Combinazioni di ingredienti e abbinamenti con base scientifica.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "R&D di avanguardia: koji, kombucha, shoyu, miso, garum, lattofermenti.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "VegChef Plant-Based",
        "description": "Cucina vegetale di alta gamma per opzioni plant-based del menu degustazione.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa + Cioccolateria Creativa",
        "description": "Dolci di alta cucina e petit fours di chiusura.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca approfondita di tendenze e avanguardia mondiale.",
        "category": "Modelli IA + LLM"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Assistente del catalogo Sosa per texture e tecniche avanzate.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Assistente del catalogo tSpoonLab per applicazioni tecniche.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Gastro Lexicum",
        "description": "Tutor con definizioni tecniche e scientifiche.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica di alto livello per stampa e guide.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Storytelling e comunicazione professionale con guide e stampa specializzata.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "velocità chiusura nuovo menu"
      },
      {
        "value": "14-18",
        "label": "portate nel menu degustazione"
      },
      {
        "value": "+5 pp",
        "label": "margine dopo food cost rigoroso"
      },
      {
        "value": "13+",
        "label": "agenti per alta gastronomia"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Chiusura del nuovo menu degustazione: 15-30 giorni tra R&D, food cost, schede tecniche e comunicazione con le guide",
        "R&D di fermenti senza documentazione, tecniche che non si replicano",
        "Storytelling per stampa e guide contro il tempo ad ogni cambio",
        "Schede tecniche nel taccuino dello chef, inaccessibili durante il servizio",
        "Ricerca di tendenze per intuizione e riviste, senza accesso sistematico"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Chiusura del menu degustazione: 1-3 giorni con Cucina Creativa, Fermentus e Kit de Escandallos Pro",
        "R&D documentato con schede tecniche iterative, fermentazioni tracciate e replicabili dalla brigata",
        "Storytelling professionale per Michelin/Repsol/50Best generato in ore",
        "Schede tecniche centralizzate, accessibili dal cellulare durante il servizio",
        "Sonar Deep Research fornisce tendenze dell'avanguardia mondiale all'istante"
      ]
    },
    "galleryTitle": "Come Funziona un Ristorante Gastronomico di Alta Cucina",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: sala elegante, plating delle portate del menu degustazione, cucina premium, sommelier e servizio impeccabile.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-gastronomico-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-kitchen.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-pase.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-sommelier.jpg",
      "/lovable-uploads/ai-gallery/use-case-gastronomico-cellar.jpg"
    ]
  },
  "restaurante-italiano": {
    "h1": "IA per Ristorante Italiano",
    "heroSubtitle": "Domina la tecnica italiana autentica con scheda tecnica rigorosa per piatto, gestisci pasta fresca e salse tradizionali, progetta menu stagionali e cattura il branding della trattoria con una suite di agenti di IA gastronomica specializzati in cucina italiana professionale.",
    "heroTagline": "Cucina italiana con tecnica autentica e margine reale",
    "badge": "Per trattorie, ristoranti e locali italiani",
    "painsTitle": "Cosa un Ristorante Italiano Non Può Lasciare di Risolvere",
    "pains": [
      "Pasta fresca quotidiana con bilanciamento preciso di semola, uova e acqua, tecnica di estrusione e formati regionali",
      "Salse tradizionali (ragù, carbonara, cacio e pepe, pesto) che richiedono consistenza tecnica turno dopo turno",
      "Sprechi in pasta fresca, formaggio, salumi italiani (mortadella, prosciutto), pomodoro San Marzano",
      "Standardizzare piatti signature regionali (Roma, Toscana, Emilia, Sicilia) con tecnica autentica",
      "Differenziarsi in zona competitiva con prodotto italiano importato, branding trattoria e storytelling regionale",
      "Catturare ordini per eventi privati, cene aziendali e matrimoni italiani con margine alto"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Ristorante Italiano",
    "features": [
      {
        "title": "Cucina Italiana",
        "description": "Agente specializzato in cucina italiana autentica: pasta, salse, risotto, ossobuco, tecnica regionale.",
        "icon": "UtensilsCrossed"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Per lieviti madre italiani (focaccia, pane casareccio, pizza alla pala) e tecnica di fermentazione.",
        "icon": "Beaker"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per piatti signature contemporanei e degustazione con base italiana autentica.",
        "icon": "Sparkles"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Vini italiani al calice e abbinamenti con cucina regionale (Chianti, Barolo, Amarone, Prosecco).",
        "icon": "Wine"
      },
      {
        "title": "Scheda tecnica per piatto",
        "description": "Cucina Italiana fornisce ricetta + scheda tecnica CSV; Kit Escandallos Pro lo gestisce con costo reale per piatto e food cost %.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelli: prep pasta fresca, salse tradizionali, mise pizza, servizio, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack HACCP italiano",
        "description": "Tracciabilità di pasta fresca, formaggi italiani, salumi e salse.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Festività italiane (Ferragosto, Carnevale, Pasqua, Natale), eventi privati e matrimoni italiani.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia editoriale trattoria IA + Instagram con storytelling regionale.",
        "icon": "Image"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Ristorante Italiano con AI Chef Pro",
    "workflow": [
      "08:00 · Apertura — checklist Kit de Tareas: prep di pasta fresca quotidiana (tagliatelle, ravioli, pappardelle), prep di salse tradizionali.",
      "10:00 · Cucina Italiana — sviluppi un nuovo piatto signature di tagliolini al limone con scampi del pescato del giorno. Ricetta + scheda tecnica CSV.",
      "11:00 · Kit Escandallos Pro — carichi CSV con prezzi reali di scampi e prodotto italiano, validi margine e food cost %.",
      "12:00 · Bar & Lounge AI+ — validi l'abbinamento con un Vermentino di Sardegna.",
      "13:00 · Servizio mezzogiorno — picco con pasta fresca, salse tradizionali e vini italiani al calice.",
      "17:00 · Briefing al team — spiegazione del nuovo piatto e abbinamenti.",
      "19:00 · Servizio cena — picchi coordinati con cucina principale.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi immagine editoriale trattoria e post."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Ristorante Italiano",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cucina Italiana + Bar & Lounge AI+ ci hanno cambiato il ristorante. Pasta fresca consistente, salse tradizionali con bilanciamento tecnico, abbinamenti con vini italiani al calice documentati. Abbiamo aumentato il margine di 5 punti e i clienti abituali sono cresciuti del 30% in 6 mesi.",
    "testimonialAuthor": "Lorenzo Bianchi",
    "testimonialRole": "Chef e proprietario, trattoria contemporanea",
    "faqTitle": "Domande Frequenti dei Ristoranti Italiani",
    "faqs": [
      {
        "q": "Serve per trattoria casual, ristorante contemporaneo o cucina regionale italiana?",
        "a": "Per tutti e tre. Cucina Italiana copre dalla trattoria tradizionale all'alta cucina italiana d'autore con tecnica regionale autentica."
      },
      {
        "q": "Copre pasta fresca e salse tradizionali?",
        "a": "Sì. Cucina Italiana ragiona come uno chef italiano professionista: bilanciamento dell'impasto, formati regionali, tecnica delle salse tradizionali."
      },
      {
        "q": "Copre vini italiani e abbinamenti?",
        "a": "Sì. Bar & Lounge AI+ copre Chianti, Barolo, Amarone, Prosecco e abbinamenti con cucina regionale."
      },
      {
        "q": "Genera contenuti visivi per Instagram?",
        "a": "Sì. GastroIMG Gen+ genera immagini editoriali trattoria. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo piatto reale."
      },
      {
        "q": "Come mi aiuta con eventi e festività italiane?",
        "a": "Gastro Calendar pianifica Ferragosto, Carnevale, Pasqua, Natale ed eventi privati con menu italiani."
      }
    ],
    "ctaTitle": "Il tuo ristorante italiano con tecnica autentica e margine reale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "IA per Ristorante Italiano: Pasta, Costi e Vini|AI Chef Pro",
      "description": "Suite di IA per ristoranti italiani: Cucina Italiana, schede tecniche, pasta fresca, vini italiani e branding trattoria. Inizia oggi.",
      "keywords": "IA ristorante italiano, software trattoria, schede tecniche pasta, cucina italiana IA, vini italiani, ristorante contemporaneo",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-italiano.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Ristorante Italiano dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding di 2 minuti in cui racconti che tipo di italiano gestisci (trattoria, ristorante contemporaneo, cucina regionale, italiano d'autore), dimensione del team, città e specialità regionale.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Ristorante Italiano",
    "apps": [
      {
        "name": "Cucina Italiana",
        "description": "Pasta, salse, risotto, ossobuco con tecnica regionale autentica.",
        "category": "Ricettari Europei"
      },
      {
        "name": "Cucina Creativa",
        "description": "Piatti signature contemporanei italiani.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Lieviti madre italiani (focaccia, pane casareccio).",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Vini italiani e abbinamenti regionali.",
        "category": "Concetti di Business"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con tecnica autentica italiana.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture e tecnica avanzata.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi in pasta fresca, formaggio, salumi.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione per piatto.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia editoriale trattoria IA di riferimento.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale italiano.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti che cercano \"italiano vicino\".",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Festività italiane ed eventi privati.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo la schedatura dei piatti"
      },
      {
        "value": "+30 %",
        "label": "clienti abituali in 6 mesi"
      },
      {
        "value": "−20 %",
        "label": "sprechi in pasta e salumi"
      },
      {
        "value": "12+",
        "label": "agenti per la tua trattoria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Pasta fresca improvvisata, bilanciamento variabile",
        "Salse tradizionali senza consistenza tecnica",
        "Abbinamenti con vini italiani senza base professionale",
        "Sprechi in prodotto italiano importato senza tracciabilità",
        "Instagram senza storytelling regionale"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Pasta fresca con bilanciamento tecnico documentato",
        "Salse tradizionali consistenti con criterio professionale",
        "Abbinamenti con Bar & Lounge AI+ documentati",
        "Sprechi controllati con Sprechi GenCal",
        "GastroIMG Gen+ + InstaFlow editoriale trattoria"
      ]
    },
    "galleryTitle": "Come Funziona un Ristorante Italiano",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: pasta fresca, piatti, cucina, vini e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-italiano-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-pasta.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-platos.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-cocina.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-vinos.jpg",
      "/lovable-uploads/ai-gallery/use-case-italiano-team.jpg"
    ]
  },
  "restaurante-japones": {
    "h1": "IA per Ristorante Giapponese",
    "heroSubtitle": "Sviluppa sushi, ramen, robata e kaiseki con tecnica autentica, scheda tecnica per pezzo con costo reale del pesce, pianifica la produzione di fermenti e cattura branding minimalista con una suite di agenti IA gastronomica specializzati in cucina giapponese professionale.",
    "heroTagline": "Cucina giapponese con margine reale e tecnica autentica",
    "badge": "Per ristoranti giapponesi, sushi bar e ramen-ya",
    "painsTitle": "Cosa un Ristorante Giapponese Non Può Lasciare di Risolvere",
    "pains": [
      "Pesce fresco quotidiano per sashimi e sushi con costo volatile e scarti rigorosi per il processo di sfilettatura",
      "Standardizzare shari (riso per sushi), nigiri e maki in ogni turno con equilibrio tecnico di aceto, zucchero e sale",
      "Brodi lunghi (tonkotsu, dashi, shoyu, miso) che richiedono ore di cottura e pianificazione notturna",
      "Fermenti professionali (koji, miso, shoyu fatto in casa, tsukemono) che richiedono tempo e tracciabilità",
      "Differenziarsi in zona competitiva con tecnica autentica vs. sushi industriale, branding minimalista e storytelling giapponese",
      "Catturare ordini di delivery senza perdere qualità del sushi (finestra ottimale 1-2 ore) e eventi omakase con margine"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Ristorante Giapponese",
    "features": [
      {
        "title": "Cucina Giapponese",
        "description": "Agente specializzato in cucina giapponese autentica: sushi, sashimi, ramen, robata, tempura, kaiseki, tecnica di itamae e fermentazione.",
        "icon": "Fish"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Per koji, miso, shoyu fatto in casa, amazake e fermenti avanzati di cucina giapponese.",
        "icon": "Beaker"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per piatti contemporanei e omakase con base giapponese: nigiri signature, fusioni controllate.",
        "icon": "Sparkles"
      },
      {
        "title": "Scheda tecnica per pezzo",
        "description": "Cucina Giapponese fornisce ricetta + scheda tecnica CSV; Kit de Escandallos Pro lo gestisce con costo reale per nigiri, ramen e omakase.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelli: sfilettatura del pesce, prep di shari, brodi lunghi notturni, mise di robata, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack HACCP giapponese",
        "description": "Tracciabilità del pesce per sushi, fermenti, temperature critiche e conservazione.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione con date chiave: Hanami (fioritura dei ciliegi), Capodanno giapponese, Hina Matsuri, Giornata del Sushi.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia minimalista IA di riferimento + Instagram: il ristorante giapponese vive di impatto visivo zen e pulito.",
        "icon": "Image"
      },
      {
        "title": "Guía Restaurante Japonés",
        "description": "Guida premium scaricabile di 60 posti con schede tecniche, piano finanziario e operativa specifica.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Ristorante Giapponese con AI Chef Pro",
    "workflow": [
      "07:00 · Apertura — checklist Kit de Tareas: ricezione del pesce fresco, sfilettatura dei blocchi di sashimi, controllo del brodo tonkotsu cotto tutta la notte.",
      "09:00 · Cucina Giapponese — sviluppi un nuovo nigiri signature di hamachi con yuzu kosho. Cucina Creativa fornisce ricetta + scheda tecnica CSV.",
      "10:00 · Kit de Escandallos Pro — carichi il CSV con i tuoi prezzi reali del pesce del giorno e wasabi fresco, validi il margine per nigiri e omakase.",
      "11:00 · Fermentus Con AI+ — controlli il progresso del miso fatto in casa (mese 6 di 12) e il nuovo koji in camera di fermentazione.",
      "13:00 · Servizio di mezzogiorno — sushi bar al completo con itamae che lavora davanti al cliente.",
      "17:00 · Pausa tra i servizi — Gastro Calendar pianifica il menù speciale di Hanami con sakura mochi e bento di ciliegio.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento del nuovo nigiri e i post minimalisti per Instagram.",
      "23:00 · Chiusura — pulizia profonda, HACCP firmato, prep di tonkotsu per domani (12 ore di cottura)."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Ristorante Giapponese",
    "productIds": [
      "guia-restaurante-japones",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cucina Giapponese ci ha cambiato l'operatività. L'equilibrio dello shari è ora consistente, il tonkotsu esce uguale ogni giorno, e l'omakase ha una scheda tecnica professionale con margine validato pezzo per pezzo. Fermentus ci ha aiutato a creare il programma di miso fatto in casa che differenzia totalmente la nostra proposta.",
    "testimonialAuthor": "Hiroshi Tanaka",
    "testimonialRole": "Itamae e proprietario, ristorante giapponese contemporaneo",
    "faqTitle": "Domande Frequenti dei Ristoranti Giapponesi",
    "faqs": [
      {
        "q": "Serve per sushi bar, ramen-ya, izakaya o kaiseki?",
        "a": "Per tutti. Cucina Giapponese copre dal sushi tradizionale all'alta cucina kaiseki, passando per ramen-ya, robata e izakaya con tecnica autentica."
      },
      {
        "q": "Copre la tecnica di itamae e la fermentazione giapponese?",
        "a": "Sì. Cucina Giapponese ragiona come un itamae professionista: tecnica di sfilettatura, equilibrio dello shari, neta e combinazioni; Fermentus copre koji, miso, shoyu fatto in casa e amazake con tecnica professionale."
      },
      {
        "q": "Come mi aiuta con il costo variabile del pesce per sashimi?",
        "a": "Kit de Escandallos Pro ricalcola all'istante il margine quando aggiorni il prezzo del pesce del giorno. Sprechi GenCal aggiunge il costo degli scarti per sfilettatura. Il nigiri riflette sempre il costo attuale."
      },
      {
        "q": "Genera contenuti visivi per Instagram, Glovo e Uber Eats?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali del sushi per Instagram, web e delivery; migliore foto = più clic. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo piatto impiattato reale."
      },
      {
        "q": "Come mi aiuta con le festività giapponesi?",
        "a": "Gastro Calendar pianifica le date chiave (Hanami con sakura, Capodanno giapponese con osechi ryori, Hina Matsuri, Giornata del Sushi) con menù speciali e calendario editoriale minimalista."
      }
    ],
    "ctaTitle": "Il tuo ristorante giapponese con margine reale e tecnica autentica.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Ristorante Giapponese: Sushi e Itamae | AI Chef Pro",
      "description": "Suite di IA per ristoranti giapponesi: Cucina Giapponese, Fermentus per koji e miso, schede tecniche per pezzo, pianificazione delle festività. Inizia oggi.",
      "keywords": "IA ristorante giapponese, software sushi bar, schede tecniche sushi, cucina giapponese IA, koji miso shoyu, ramen tonkotsu, itamae professionale",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-japones.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Ristorante Giapponese dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di giapponese gestisci (sushi bar, ramen-ya, izakaya, kaiseki, omakase, giapponese contemporaneo d'autore), dimensione del team, città e specialità. Ogni agente —da Cucina Giapponese a Gastro Calendar— risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Ristorante Giapponese",
    "apps": [
      {
        "name": "Cucina Giapponese",
        "description": "Agente specializzato in cucina giapponese autentica: sushi, sashimi, ramen, robata, kaiseki.",
        "category": "Ricettari Asiatici"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Koji, miso, shoyu fatto in casa, amazake e fermenti avanzati.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di nigiri signature e omakase con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con sake, whisky giapponese, birra e vini per il tuo menù.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture e tecnica applicata alla cucina giapponese d'autore.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Scarti nella sfilettatura del pesce, sashimi e brodi lunghi.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni: pesce, crostacei, soia, glutine, sesamo.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia minimalista IA di riferimento per Instagram, web, menù e delivery.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale minimalista per sushi bar d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"sushi vicino\" o \"ramen vicino\".",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Hanami, Capodanno giapponese, Hina Matsuri, Giornata del Sushi.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Per il banco di sake, whisky giapponese e cocktaileria con base giapponese.",
        "category": "Concetti di Business"
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margine dopo scheda tecnica omakase"
      },
      {
        "value": "×3",
        "label": "engagement Instagram con GastroIMG"
      },
      {
        "value": "−20 %",
        "label": "scarti nella sfilettatura del pesce"
      },
      {
        "value": "12+",
        "label": "agenti per la tua cucina giapponese"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Shari e tecnica improvvisati, equilibrio inconsistente tra itamae",
        "Schede tecniche non aggiornate al prezzo giornaliero del pesce",
        "Brodi lunghi (tonkotsu) senza tracciabilità né pianificazione rigorosa",
        "Fermenti fatti in casa (miso, shoyu) senza programma documentato",
        "Instagram improvvisato e piattaforme di delivery con foto del telefono"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Shari, neta e tecnica con criterio professionale, consistenza turno dopo turno",
        "Scheda tecnica in tempo reale con prezzo del pesce del giorno",
        "Brodi lunghi pianificati con modelli specifici e HACCP firmato",
        "Programma di fermenti con Fermentus Con AI+ documentato professionalmente",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO catturano clienti locali"
      ]
    },
    "galleryTitle": "Come Funziona un Ristorante Giapponese",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: sushi, ramen, robata, ingredienti e team. Immagini generate con IA come riferimento visivo del concept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-japones-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-sushi.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-ramen.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-robata.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-ingredientes.jpg",
      "/lovable-uploads/ai-gallery/use-case-japones-team.jpg"
    ]
  },
  "restaurante-mexicano": {
    "h1": "IA per Ristorante Messicano",
    "heroSubtitle": "Sviluppa salse con equilibrio preciso, scheda tecnica per taco e per menù con costo reale, pianifica la produzione di masa e nixtamalizzazione, e cattura branding professionale con una suite di agenti IA gastronomici specializzati in cucina messicana autentica.",
    "heroTagline": "Sapore messicano con margine reale e tecnica autentica",
    "badge": "Per ristoranti messicani e taquerías",
    "painsTitle": "Ciò che un Ristorante Messicano Non Può Lasciare di Risolvere",
    "pains": [
      "Salse complesse con molti peperoncini, tostatura e equilibrio preciso (mole, salsa macha, adobos) che richiedono consistenza turno dopo turno",
      "Schedare i taco, gli antojitos e i piatti con molte varianti di tortilla, ripieno, salse e guarnizioni mantenendo un food cost coerente",
      "Perdite in masa, tortillas, marinate e proteine con lunga cottura (carnitas, barbacoa, cochinita)",
      "Standardizzare la nixtamalizzazione e la tecnica della masa per tortillas, sopes e huaraches con qualità costante",
      "Differenziarsi in una zona competitiva con menù autentico, branding visivo degli antojitos e storytelling regionale (Oaxaca, Yucatán, Puebla)",
      "Catturare ordini di eventi e catering messicano (matrimoni, feste nazionali) con margine mentre si gestisce il servizio quotidiano"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Ristorante Messicano",
    "features": [
      {
        "title": "Cucina Messicana",
        "description": "Agente specializzato in cucina messicana autentica: salse, mole, marinate, antojitos, tecnica della masa e cucina regionale.",
        "icon": "UtensilsCrossed"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per piatti contemporanei e d'autore con base messicana: taco signature, fusioni controllate, dessert messicani moderni.",
        "icon": "Sparkles"
      },
      {
        "title": "Schede tecniche per taco e per piatto",
        "description": "Cucina Messicana fornisce ricetta + scheda tecnica CSV; Kit de Escandallos Pro lo gestisce con costo reale per taco, food cost % e prezzo suggerito.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelli adattabili: prep della masa, tostatura dei peperoncini, marinate, comal, mise per stazione e chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC messicano",
        "description": "Tracciabilità di peperoncini, masa nixtamalizzata, proteine con lunga cottura e temperature critiche.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione con date chiave: 5 maggio, Giorno dei Morti, Feste Nazionali 16 settembre, Giorno della Candelora con tamales.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia gastronomica IA di riferimento + Instagram con calendario editoriale: il ristorante messicano vive di impatto visivo e storytelling.",
        "icon": "Image"
      },
      {
        "title": "Sosa Ingredients AI",
        "description": "Assistente del catalogo Sosa per texture avanzate, addensanti, disidratati e tecnica applicata alla cucina messicana.",
        "icon": "BarChart3"
      },
      {
        "title": "Guía Restaurante Mexicano",
        "description": "Guida premium scaricabile di 80 pagine con schede tecniche, food cost, piano finanziario e operativa specifica della cucina messicana.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Ristorante Messicano con AI Chef Pro",
    "workflow": [
      "08:00 · Apertura — checklist Kit de Tareas: tostatura dei peperoncini per salsa macha, prep della masa nixtamalizzata, marinata di cochinita pibil, mise di topping freschi.",
      "10:00 · Cucina Messicana — sviluppi un nuovo taco signature di barbacoa con salsa di peperoncino cascabel e avocado. Cucina Creativa fornisce ricetta + scheda tecnica CSV.",
      "11:00 · Kit de Escandallos Pro — carichi il CSV con i tuoi prezzi reali di peperoncini secchi, carne, masa e avocado, validi il margine per taco e il food cost %.",
      "13:00 · Servizio di mezzogiorno — il team replica con modelli di mise; il comal funziona a pieno regime.",
      "17:00 · Pausa tra i servizi — Gastro Calendar pianifica il menù speciale del Giorno dei Morti con pan de muerto e mole negro.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento del nuovo taco e i post per Instagram.",
      "21:00 · Servizio cena — picchi coordinati con Pasto del Personale per lo staff prima del rush.",
      "00:00 · Chiusura — pulizia profonda, HACCP firmato, prep della masa per domani."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Ristorante Messicano",
    "productIds": [
      "guia-restaurante-mexicano",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Abbiamo fatto la scheda tecnica taco per taco e abbiamo scoperto che tre signature erano in perdita nonostante fossero i più venduti. Li abbiamo ridisegnati con Cucina Messicana aggiustando la marinata e la resa della carne, senza toccare il prezzo, e abbiamo alzato il margine di 5 punti. La pianificazione del Giorno dei Morti con Gastro Calendar ci ha triplicato il fatturato di quella settimana.",
    "testimonialAuthor": "María José Hernández",
    "testimonialRole": "Chef e proprietaria, ristorante messicano contemporaneo",
    "faqTitle": "Domande Frequenti dei Ristoranti Messicani",
    "faqs": [
      {
        "q": "Serve per taquería casual, ristorante messicano contemporaneo o cucina regionale?",
        "a": "Per tutti e tre. Cucina Messicana copre dalla taquería tradizionale all'alta cucina messicana d'autore, passando per la cucina regionale (Oaxaca, Yucatán, Puebla, Michoacán) con tecnica autentica."
      },
      {
        "q": "Copre la nixtamalizzazione e la tecnica della masa?",
        "a": "Sì. Cucina Messicana ragiona come un cuoco messicano professionista: nixtamalizzazione con calce, equilibrio della masa per tortilla, sope, huarache, gordita e tlacoyo. Niente ricette da YouTube."
      },
      {
        "q": "Come mi aiuta con la complessità delle salse messicane?",
        "a": "Cucina Messicana fornisce salse con equilibrio tecnico dei peperoncini (tostatura, idratazione, equilibrio piccante-dolce-acido), mole complessi a strati e marinate professionali. Sprechi GenCal aggiunge il costo dei peperoncini secchi alla scheda tecnica finale."
      },
      {
        "q": "Genera contenuti visivi per Instagram, Glovo e Uber Eats?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali per social e delivery; migliore foto = più clic e miglior ranking. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo piatto reale impiattato."
      },
      {
        "q": "Come mi aiuta con le festività messicane?",
        "a": "Gastro Calendar pianifica le date chiave (Giorno dei Morti, Giorno della Candelora con tamales, Feste Nazionali, 5 maggio) con menù speciali e calendario editoriale."
      }
    ],
    "ctaTitle": "Il tuo ristorante messicano con margine reale e tecnica autentica.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Ristorante Messicano: Salse e Schede Tecniche",
      "description": "Suite di IA per ristoranti messicani: Cucina Messicana, schede tecniche per taco, pianificazione delle festività, branding e HACCP. Inizia oggi.",
      "keywords": "IA ristorante messicano, software taquería, schede tecniche taco, cucina messicana IA, nixtamalizzazione, salse messicane, Giorno dei Morti ristorante",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-mexicano.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Ristorante Messicano dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di ristorante messicano gestisci (taquería casual, ristorante messicano contemporaneo, cucina regionale, cantina, taquería gourmet, food truck messicano), dimensione del team, città e specialità. Ogni agente —da Cucina Messicana a Gastro Calendar— risponde adattato al tuo prodotto, mercato e operativa reale.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Ristorante Messicano",
    "apps": [
      {
        "name": "Cucina Messicana",
        "description": "Agente specializzato in cucina messicana autentica: salse, mole, marinate, antojitos, tecnica regionale.",
        "category": "Ricettari Latinoamericani"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di taco signature e piatti contemporanei con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Consulenza operativa per ristoranti casual e taquerías professionali.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture, addensanti e tecnica applicata alla cucina messicana d'autore.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Perdite in masa, peperoncini, marinate e proteine con lunga cottura.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per piatto: glutine, latticini, frutta a guscio, soia.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA di riferimento per Instagram, web, menù e delivery.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale professionale per taquería d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"taco vicino\" o \"ristorante messicano\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Giorno dei Morti, Giorno della Candelora, Feste Nazionali, 5 maggio.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico per taco e antojitos con storytelling.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pasto del Personale",
        "description": "Generatore di menù per staff/famiglia trasversale a tutti i concetti.",
        "category": "Gastro Profile Pro"
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "margine dopo aver schedato i taco"
      },
      {
        "value": "×3",
        "label": "fatturato nel Giorno dei Morti"
      },
      {
        "value": "−20 %",
        "label": "perdite in masa e marinate"
      },
      {
        "value": "12+",
        "label": "agenti per la tua cucina messicana"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Salse e mole improvvisate, equilibrio incoerente turno dopo turno",
        "Schede tecniche senza food cost reale, signature in perdita senza saperlo",
        "Perdite in masa, peperoncini e proteine lunghe senza tracciabilità",
        "Festività reattive: arrivi tardi al Giorno dei Morti senza menù speciale",
        "Instagram improvvisato e piattaforme di delivery con foto dal telefono"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Salse e mole con criterio tecnico, consistenza turno dopo turno",
        "Scheda tecnica professionale per taco e piatto con food cost validato",
        "Perdite controllate con Sprechi GenCal e modelli specifici",
        "Festività pianificate con 8 settimane di anticipo con Gastro Calendar",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO catturano clienti locali"
      ]
    },
    "galleryTitle": "Come Funziona un Ristorante Messicano",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: salse, taco, comal, ingredienti e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-mexicano-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-salsas.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-tacos.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-comal.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-ingredientes.jpg",
      "/lovable-uploads/ai-gallery/use-case-mexicano-team.jpg"
    ]
  },
  "restaurante-nikkei": {
    "h1": "IA per Ristorante Nikkei",
    "heroSubtitle": "Sviluppa tiraditos nikkei, sushi di fusione e robata con tecnica autentica peruviano-giapponese, scandaglia per piatto con costo reale e ottieni branding professionale con una suite di agenti IA gastronomici specializzati in cucina nikkei.",
    "heroTagline": "Cucina Nikkei con margine reale e tecnica autentica",
    "badge": "Per ristoranti Nikkei e fusione peruviano-giapponese",
    "painsTitle": "Ciò che un ristorante nikkei non può lasciare in sospeso",
    "pains": [
      "Combinazioni complesse peruviano-giapponesi con equilibrio preciso di aji amarillo, yuzu, miso, ponzu e shoyu",
      "Pesce fresco quotidiano per tiraditos e sushi con costo volatile, sfilettatura rigorosa e tecnica itamae applicata alla cucina peruviana",
      "Standardizzare tiraditos signature, sushi nikkei e anticuchos con marinatura miso-aji panca turno dopo turno",
      "Scandagliare i piatti con ingredienti importati (aji amarillo, aji panca, yuzu, dashi) il cui costo varia di stagione in stagione",
      "Differenziarsi dal giapponese tradizionale o dal peruviano puro con storytelling di fusione autentica e branding visivo d'autore",
      "Catturare ordini di omakase nikkei ed eventi mantenendo la qualità del prodotto crudo"
    ],
    "featuresTitle": "Come AI Chef Pro aiuta un ristorante nikkei",
    "features": [
      {
        "title": "Cucina Giapponese + Cucina Peruviana",
        "description": "Combinazione di agenti specializzati in entrambe le culture: tecnica itamae applicata ai tiraditos peruviani, aji amarillo nel nigiri, anticuchos al miso.",
        "icon": "Sparkles"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Per koji, miso, shoyu fatti in casa adattati alla fusione nikkei con aji panca e huacatay.",
        "icon": "Beaker"
      },
      {
        "title": "Food Pairing AI",
        "description": "Abbinamenti con sake, pisco, vini cileni e birra giapponese per il tuo menu nikkei.",
        "icon": "Wine"
      },
      {
        "title": "Scandagli per piatto",
        "description": "Cucina Creativa fornisce ricetta + scandaglio CSV; Kit di Scandagli Pro lo gestisce con costo reale per tiradito e omakase nikkei.",
        "icon": "Calculator"
      },
      {
        "title": "Kit di Attività Ristorante Casual",
        "description": "Template: sfilettatura del pesce, preparazione di leche de tigre con yuzu, marinatura nikkei, mise en place robata, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pacchetto HACCP nikkei",
        "description": "Tracciabilità di pesce, fermenti, aji e temperature critiche nel prodotto crudo.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione incrociata: festività giapponesi e peruviane, eventi di fusione, omakase nikkei stagionale.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia editoriale IA di riferimento + Instagram: il nikkei vive di impatto visivo, colore e composizione.",
        "icon": "Image"
      },
      {
        "title": "Guida Ristorante Nikkei",
        "description": "Guida premium scaricabile da 60 coperti con scandagli, schede tecniche, piano finanziario e operatività specifica nikkei.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Una giornata reale in un ristorante nikkei con AI Chef Pro",
    "workflow": [
      "07:00 · Apertura — checklist Kit di Attività: ricezione del pesce fresco, sfilettatura per tiraditos e nigiri, preparazione di leche de tigre con yuzu, marinatura degli anticuchos miso-panca.",
      "09:00 · Cucina Giapponese + Cucina Peruviana — sviluppi un nuovo tiradito di hamachi con leche de tigre allo yuzu e aji amarillo. Cucina Creativa fornisce ricetta + scandaglio CSV.",
      "10:00 · Kit di Scandagli Pro — carichi il CSV con i tuoi prezzi reali del pesce del giorno, aji amarillo e yuzu, validi il margine per tiradito e omakase nikkei.",
      "11:00 · Fermentus Con AI+ — controlli l'avanzamento del miso fatto in casa con aji panca (mese 4 di 8).",
      "12:00 · Food Pairing AI — validi l'abbinamento del nuovo tiradito con un sake junmai e un pisco macerato in foglie di shiso.",
      "13:00 · Servizio di mezzogiorno — robata a pieno ritmo con anticuchos al miso, sushi bar al lavoro sui tiraditos signature.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento del nuovo tiradito nikkei e i post editoriali per Instagram.",
      "23:00 · Chiusura — pulizia profonda, HACCP firmato, scarto controllato, preparazione per il giorno dopo."
    ],
    "productsTitle": "Template e kit consigliati per ristorante nikkei",
    "productIds": [
      "guia-restaurante-nikkei",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cucina Giapponese + Cucina Peruviana incrociando gli agenti ci ha cambiato la proposta. I tiraditos ora hanno un equilibrio tecnico documentato, l'omakase nikkei esce con scandaglio validato pezzo per pezzo, e il programma di miso fatto in casa con aji panca di Fermentus ci differenzia totalmente. Abbiamo alzato il margine di 7 punti.",
    "testimonialAuthor": "Yui Sato",
    "testimonialRole": "Chef e proprietaria, ristorante nikkei d'autore",
    "faqTitle": "Domande frequenti dei ristoranti nikkei",
    "faqs": [
      {
        "q": "Va bene per nikkei contemporaneo, sushi bar nikkei o cevicheria con tecnica giapponese?",
        "a": "Per tutti e tre. Cucina Giapponese + Cucina Peruviana si completano a vicenda per coprire dal sushi nikkei ai tiraditos con leche de tigre fusa con yuzu o ponzu."
      },
      {
        "q": "Come mi aiuta con l'equilibrio tra tecniche peruviana e giapponese?",
        "a": "Cucina Creativa orchestra i due agenti: ragiona in chiave di fusione autentica (non fusione confusa), rispettando la tecnica itamae per il prodotto crudo e l'equilibrio peruviano per leche de tigre e marinature."
      },
      {
        "q": "Come gestisco il costo variabile del pesce e degli ingredienti peruviani importati?",
        "a": "Kit di Scandagli Pro ricalcola all'istante il margine quando aggiorni i prezzi del pesce del giorno e di aji/yuzu. Sprechi GenCal aggiunge il costo degli scarti per processo."
      },
      {
        "q": "Genera contenuti visivi per Instagram e delivery?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali del tiradito nikkei per Instagram, web e delivery. Ricorda che l'immagine IA è un riferimento visivo: la foto definitiva la fai tu con il tuo piatto impiattato reale."
      },
      {
        "q": "Come mi aiuta con le festività incrociate peruviano-giapponesi?",
        "a": "Gastro Calendar pianifica le date chiave di entrambe le culture (28 luglio peruviano, Hanami giapponese, Giorno del Ceviche, Capodanno giapponese) con omakase nikkei stagionale e storytelling di fusione."
      }
    ],
    "ctaTitle": "Il tuo ristorante nikkei con margine reale e tecnica autentica.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per ristorante nikkei: tiraditos, scandagli e tecnica di fusione | AI Chef Pro",
      "description": "Suite IA per ristoranti nikkei: Cucina Giapponese + Peruviana, scandagli per tiradito, omakase nikkei, branding e HACCP. Inizia oggi.",
      "keywords": "IA ristorante nikkei, software nikkei, scandagli tiradito nikkei, cucina nikkei IA, aji amarillo yuzu, sushi nikkei, fusione peruviano giapponese",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-nikkei.jpg"
    },
    "personalizationTitle": "Personalizzato per il tuo ristorante nikkei dal primo minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di nikkei gestisci (nikkei contemporaneo d'autore, sushi bar nikkei, cevicheria con tecnica giapponese, omakase nikkei), dimensione del team, città e specialità. Ogni agente risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli agenti IA che userai nel tuo ristorante nikkei",
    "apps": [
      {
        "name": "Cucina Giapponese",
        "description": "Tecnica itamae, sfilettatura, sushi, sashimi e robata applicati alla fusione nikkei.",
        "category": "Ricettari Asiatici"
      },
      {
        "name": "Cucina Peruviana",
        "description": "Ceviche, tiraditos, anticuchos e tecnica peruviana applicati alla fusione nikkei.",
        "category": "Ricettari Latinoamericani"
      },
      {
        "name": "Cucina Creativa",
        "description": "Orchestratore di fusione: tiraditos signature, sushi nikkei, omakase con base autentica.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Koji, miso fatto in casa con aji panca, shoyu e fermenti incrociati.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con sake, pisco, vini cileni e birra giapponese.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture e tecnica applicata alla cucina nikkei d'autore.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi nella sfilettatura del pesce, aji e marinature lunghe.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni: pesce, crostacei, soia, glutine, sesamo, frutta a guscio.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia editoriale IA di riferimento per Instagram, web, menu e delivery.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale professionale per nikkei d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"nikkei vicino a me\" su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Festività incrociate: Hanami, 28 luglio, Giorno del Ceviche, Capodanno giapponese.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "margine dopo aver scandagliato l'omakase nikkei"
      },
      {
        "value": "×3",
        "label": "engagement Instagram con GastroIMG"
      },
      {
        "value": "−25 %",
        "label": "sprechi su pesce e aji"
      },
      {
        "value": "12+",
        "label": "agenti per la tua cucina nikkei"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Fusione improvvisata senza equilibrio tecnico tra culture",
        "Scandagli non aggiornati al prezzo del pesce e degli aji",
        "Sushi nikkei e tiraditos con consistenza variabile tra i turni",
        "Programma di fermenti fatto in casa senza documentazione professionale",
        "Instagram improvvisato, senza storytelling di fusione autentica"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Fusione autentica con tecnica documentata di entrambe le culture",
        "Scandaglio in tempo reale con prezzi aggiornati",
        "Sushi nikkei e tiraditos con equilibrio tecnico consistente",
        "Programma Fermentus con miso aji panca documentato professionalmente",
        "GastroIMG Gen+ + InstaFlow + storytelling di fusione nikkei autentica"
      ]
    },
    "galleryTitle": "Come funziona un ristorante nikkei",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: tiraditos, sushi nikkei, anticuchos al miso, ingredienti e team. Immagini generate con IA come riferimento visivo del concept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-nikkei-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-tiradito.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-sushi.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-anticucho.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-ingredientes.jpg",
      "/lovable-uploads/ai-gallery/use-case-nikkei-team.jpg"
    ]
  },
  "restaurante-peruano": {
    "h1": "IA per Ristorante Peruviano",
    "heroSubtitle": "Sviluppa ceviche, tiraditos e cause con equilibrio tecnico, scheda tecnica per piatto con costo reale di pesce e ají, pianifica la produzione e cattura branding professionale con una suite di agenti IA gastronomica specializzati in cucina peruviana autentica.",
    "heroTagline": "Cucina peruviana con margine reale e tecnica autentica",
    "badge": "Per ristoranti peruviani e cevicherie",
    "painsTitle": "Cosa un Ristorante Peruviano Non Può Evitare di Risolvere",
    "pains": [
      "Ceviche e tiraditos con pesce fresco quotidiano e leche de tigre bilanciata in acidità, piccante e sale turno dopo turno",
      "Calcolare il food cost dei piatti con ingredienti peruviani importati (ají amarillo, rocoto, panca, huacatay) il cui costo varia stagionalmente",
      "Merce in eccesso di pesce fresco, frutti di mare, choclo, patate peruviane e lime con uso intensivo",
      "Standardizzare la tecnica di cottura delle proteine (anticucho, pollo alla brasa, pachamanca) e dei contorni (causa, papa a la huancaína)",
      "Differenziarsi in zone competitive con menu autentico (criolla, costeña, andina, amazzonica), branding visivo e storytelling regionale",
      "Gestire ordini delivery ed eventi mantenendo la qualità del ceviche fuori dalla sua finestra ottimale di consumo"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Ristorante Peruviano",
    "features": [
      {
        "title": "Cucina Peruviana",
        "description": "Agente specializzato in cucina peruviana autentica: ceviche, tiraditos, cause, anticuchos, pachamanca, tecnica criolla, costeña, andina e amazzonica.",
        "icon": "UtensilsCrossed"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per piatti contemporanei e d'autore con base peruviana: cause signature, fusioni controllate, dessert peruviani moderni.",
        "icon": "Sparkles"
      },
      {
        "title": "Food Pairing AI",
        "description": "Abbinamenti con pisco, vini cileni e birra per il tuo menu peruviano con base scientifica.",
        "icon": "Wine"
      },
      {
        "title": "Scheda tecnica per piatto",
        "description": "Cucina Peruviana fornisce ricetta + scheda tecnica CSV; Kit Escandallos Pro la gestisce con costo reale per ceviche, food cost % e prezzo suggerito.",
        "icon": "Calculator"
      },
      {
        "title": "Kit di Attività Ristorante Casual",
        "description": "Modelli: prep di leche de tigre, marinate di anticucho, mise di frutti di mare, papa a la huancaína, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pacchetto HACCP peruviano",
        "description": "Tracciabilità di pesce fresco, frutti di mare, ajíes e temperature critiche in ceviche e tiradito.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione con date chiave: Giorno dell'Indipendenza 28 luglio, Giorno del Ceviche, Mistura, Giorno del Pisco Sour.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia di ceviche e tiraditos IA di riferimento + Instagram: il ristorante peruviano vive dell'impatto visivo del colore.",
        "icon": "Image"
      },
      {
        "title": "Guida Ristorante Peruviano",
        "description": "Guida premium scaricabile di 80 pagine con schede tecniche, food cost, piano finanziario e operatività specifica della cucina peruviana.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Ristorante Peruviano con AI Chef Pro",
    "workflow": [
      "08:00 · Apertura — checklist Kit di Attività: ricezione del pesce fresco quotidiano, prep della leche de tigre base, marinata di anticucho, idratazione degli ajíes secchi.",
      "10:00 · Cucina Peruviana — sviluppi un nuovo tiradito del giorno con leche de tigre di rocoto e mango. Cucina Creativa fornisce ricetta + scheda tecnica CSV.",
      "11:00 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali di pesce fresco, ajíes, choclo e patate, validi il margine per piatto.",
      "12:00 · Food Pairing AI — validi l'abbinamento del nuovo tiradito con un pisco sour macerato alle erbe.",
      "13:00 · Servizio di mezzogiorno — picco del cebichero, mise impeccabile.",
      "17:00 · Pausa tra i servizi — Gastro Calendar pianifica il menu del 28 luglio (Indipendenza) con causa, anticuchos e pisco.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento del nuovo tiradito e i post per Instagram.",
      "23:00 · Chiusura — pulizia profonda, HACCP firmato, scarto controllato del pesce del giorno."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Ristorante Peruviano",
    "productIds": [
      "guia-restaurante-peruano",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cucina Peruviana ci ha cambiato la cucina. La leche de tigre ha ora un equilibrio tecnico documentato, i ceviche escono uguali in qualsiasi turno, e le schede tecniche con pesce fresco al prezzo del giorno funzionano in tempo reale. La preparazione del menu speciale del 28 luglio con Gastro Calendar ci ha triplicato il fatturato.",
    "testimonialAuthor": "Carlos Fernández",
    "testimonialRole": "Chef e proprietario, cevicheria peruviana contemporanea",
    "faqTitle": "Domande Frequenti dei Ristoranti Peruviani",
    "faqs": [
      {
        "q": "Va bene per cevicheria informale, ristorante peruviano contemporaneo o cucina regionale?",
        "a": "Per tutti e tre. Cucina Peruviana copre dalla cevicheria tradizionale all'alta cucina d'autore, passando per la cucina regionale (criolla, costeña, andina, amazzonica) con tecnica autentica."
      },
      {
        "q": "Copre la tecnica del ceviche e della leche de tigre professionale?",
        "a": "Sì. Cucina Peruviana ragiona come un cebichero professionista: equilibrio della leche de tigre con acidità, piccante e sale; finestra ottimale di marinatura per specie; integrazione degli ajíes con tecnica."
      },
      {
        "q": "Come mi aiuta con il costo variabile del pesce fresco?",
        "a": "Kit Escandallos Pro ricalcola all'istante il margine reale quando aggiorni il prezzo del pesce del giorno. Sprechi GenCal aggiunge il costo degli scarti per processo. Così il ceviche riflette sempre il costo attuale."
      },
      {
        "q": "Genera contenuti visivi per Instagram, Glovo e Uber Eats?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali del ceviche e del tiradito per Instagram, web e delivery; migliore foto = più clic. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo ceviche impiattato reale."
      },
      {
        "q": "Come mi aiuta con le festività peruviane e gli eventi?",
        "a": "Gastro Calendar pianifica le date chiave (28 luglio Giorno dell'Indipendenza, Giorno del Ceviche, Giorno del Pisco Sour, Mistura) con menu speciali e calendario editoriale."
      }
    ],
    "ctaTitle": "Il tuo ristorante peruviano con margine reale e tecnica autentica.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Ristorante Peruviano: Ceviche, Schede Tecniche e Tecnica Autentica | AI Chef Pro",
      "description": "Suite IA per ristoranti peruviani: Cucina Peruviana, schede tecniche per ceviche, pianificazione festività, branding e HACCP. Inizia oggi.",
      "keywords": "IA ristorante peruviano, software cevicheria, schede tecniche ceviche, cucina peruviana IA, leche de tigre, ají amarillo, 28 luglio peruviano",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-peruano.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Ristorante Peruviano dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di peruviano gestisci (cevicheria informale, ristorante peruviano contemporaneo, cucina regionale, picanteria andina, polleria, ristorante d'autore), dimensione del team, città e specialità. Ogni agente —da Cucina Peruviana a Gastro Calendar— risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Ristorante Peruviano",
    "apps": [
      {
        "name": "Cucina Peruviana",
        "description": "Agente specializzato in cucina peruviana autentica: ceviche, tiraditos, cause, anticuchos, pachamanca.",
        "category": "Ricettari Latinoamericani"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di tiraditos signature e piatti contemporanei con ricetta + scheda tecnica CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con pisco, vini e birra per il tuo menu peruviano.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Consulenza operativa per cevicherie e ristoranti peruviani.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture e tecnica applicata alla cucina peruviana d'autore.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Scarti di pesce fresco, frutti di mare, ajíes e lime.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni: pesce, crostacei, glutine, lattosio.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia gastronomica IA di riferimento per Instagram, web, menu e delivery.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale professionale per cevicheria d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Attirare clienti locali che cercano \"cevicheria vicino\" o \"ristorante peruviano\".",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "28 luglio, Giorno del Ceviche, Mistura, Giorno del Pisco Sour.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Per il bancone del pisco sour e la cocktaileria peruviana d'autore.",
        "category": "Concetti di Business"
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margine dopo aver calcolato il food cost dei ceviche"
      },
      {
        "value": "×3",
        "label": "fatturato il 28 luglio"
      },
      {
        "value": "−25 %",
        "label": "scarti di pesce fresco"
      },
      {
        "value": "12+",
        "label": "agenti per la tua cucina peruviana"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Leche de tigre improvvisata, equilibrio inconsistente turno dopo turno",
        "Schede tecniche non aggiornate al prezzo giornaliero del pesce fresco",
        "Scarti di pesce, ajíes e frutti di mare senza tracciabilità reale",
        "Festività reattive: arrivi tardi al 28 luglio senza menu speciale",
        "Instagram improvvisato e piattaforme di delivery con foto dal telefono"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Leche de tigre con equilibrio tecnico documentato, ceviche consistenti",
        "Scheda tecnica in tempo reale con prezzo del pesce del giorno",
        "Scarti controllati con Sprechi GenCal e modelli specifici",
        "Festività pianificate con 8 settimane di anticipo",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO attirano clienti locali"
      ]
    },
    "galleryTitle": "Come Funziona un Ristorante Peruviano",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: ceviche, tiradito, anticucho, ajíes e team. Immagini generate con IA come riferimento visivo del concept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-peruano-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-ceviche.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-tiradito.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-anticucho.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-ajies.jpg",
      "/lovable-uploads/ai-gallery/use-case-peruano-team.jpg"
    ]
  },
  "restaurante-plant-based": {
    "h1": "IA per Ristorante Plant-Based e Vegano",
    "heroSubtitle": "Sviluppa menù plant-based con equilibrio nutrizionale, scheda tecnica per bowl e burger vegana con costo reale, pianifica fermenti vegetali e cattura branding fresco con una suite di agenti di IA gastronomica specializzati in cucina plant-based professionale.",
    "heroTagline": "Cucina vegetale con margine reale e tecnica avanzata",
    "badge": "Per ristoranti plant-based, vegani e healthy",
    "painsTitle": "Ciò che un Ristorante Plant-Based Non Può Non Risolvere",
    "pains": [
      "Ottenere umami profondo in cucina 100% vegetale con fermenti, affumicati, koji e tecnica avanzata (senza scorciatoie industriali)",
      "Fare la scheda tecnica di bowl, burger vegane e piatti plant-based con molte varianti di topping e proteine vegetali",
      "Alti sprechi su prodotto fresco (verdure di stagione, frutta, erbe, microgreens) con scadenza breve",
      "Standardizzare proteine vegetali fatte in casa (seitan, tempeh, tofu marinato, mock meats) e coperture/salse plant-based",
      "Differenziarsi in zona competitiva con menù d'autore plant-based, branding visivo fresco e storytelling sostenibile",
      "Catturare ordini di delivery con prodotti freschi mantenendo presentazione e qualità del bowl"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Ristorante Plant-Based",
    "features": [
      {
        "title": "VegChef Plant-Based",
        "description": "Agente specializzato in cucina plant-based, vegana e vegetariana professionale: bowl, burger, proteine vegetali, tecnica avanzata.",
        "icon": "Sprout"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Per koji vegetale, miso fatto in casa, shoyu, kimchi, kombucha, lattofermenti e umami profondo senza prodotti animali.",
        "icon": "Beaker"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per piatti plant-based contemporanei e d'autore a base vegetale: bowl signature, dessert vegani, fusioni.",
        "icon": "Sparkles"
      },
      {
        "title": "Food Pairing AI",
        "description": "Abbinamenti con vini vegani, kombucha e bevande funzionali per la tua carta plant-based.",
        "icon": "Wine"
      },
      {
        "title": "Scheda tecnica per bowl e burger",
        "description": "VegChef fornisce ricetta + scheda tecnica CSV; Kit Escandallos Pro lo gestisce con costo reale per bowl, food cost % e prezzo suggerito.",
        "icon": "Calculator"
      },
      {
        "title": "Kit di Attività Ristorante Casual",
        "description": "Modelli: prep di proteine vegetali, fermenti, mise en place di topping freschi, marinate, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC plant-based",
        "description": "Tracciabilità di fermenti, proteine vegetali fatte in casa, erbe fresche e temperature critiche.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione con date chiave: Veganuary (gennaio), Giornata Mondiale Vegana, Earth Day, stagioni di verdure locali.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia vibrante IA di riferimento + Instagram: il plant-based vive dell'impatto visivo del colore.",
        "icon": "Image"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Ristorante Plant-Based con AI Chef Pro",
    "workflow": [
      "07:00 · Apertura — checklist Kit di Attività: revisione dei fermenti in camera, prep di proteine vegetali (seitan, tempeh), marinate di tofu, mise en place di microgreens e fiori eduli.",
      "09:00 · VegChef Plant-Based — sviluppi un nuovo bowl signature di quinoa, cavolo riccio, tempeh marinato, kimchi fatto in casa e tahini di curcuma. Cucina Creativa fornisce ricetta + scheda tecnica CSV.",
      "10:00 · Kit Escandallos Pro — carichi il CSV con i tuoi prezzi reali di quinoa, cavolo riccio, tempeh e tahini, valuti il margine per bowl e il food cost %.",
      "11:00 · Fermentus Con AI+ — controlli il progresso del miso fatto in casa (mese 6 di 12), il koji vegetale e il nuovo kimchi in camera di fermentazione.",
      "12:00 · Food Pairing AI — valuti l'abbinamento del nuovo bowl con kombucha allo zenzero e un vino bianco vegano.",
      "13:00 · Servizio di mezzogiorno — bowl a pieno ritmo, burger vegane alla piastra, mise en place di topping freschi.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi l'immagine di riferimento del nuovo bowl e i post vibranti per Instagram.",
      "22:00 · Chiusura — pulizia profonda, HACCP firmato, prep di fermenti per fermentazione notturna."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Ristorante Plant-Based",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "VegChef + Fermentus ci hanno cambiato la proposta. Otteniamo umami profondo senza scorciatoie industriali grazie al miso fatto in casa e al koji vegetale, e le schede tecniche per bowl con tempeh marinato ci confermano che il plant-based può avere un margine alto. Siamo saliti di 6 punti e l'acquisizione su Instagram con GastroIMG è x3.",
    "testimonialAuthor": "Lucía Ferrer",
    "testimonialRole": "Chef e proprietaria, ristorante plant-based d'autore",
    "faqTitle": "Domande Frequenti dei Ristoranti Plant-Based",
    "faqs": [
      {
        "q": "Serve per casual healthy bowls, vegan fine dining o cucina plant-based d'autore?",
        "a": "Per tutti e tre. VegChef copre dai bowl casuali all'alta cucina vegana, passando per hamburgerie plant-based, cucina con tecnica avanzata e dessert vegani professionali."
      },
      {
        "q": "Come ottenere umami profondo in cucina 100% vegetale?",
        "a": "Fermentus Con AI+ copre koji vegetale, miso fatto in casa, shoyu, kimchi, kombucha e lattofermenti con tecnica professionale. VegChef integra affumicati controllati, disidratati, croste di funghi e brodi lunghi vegetali."
      },
      {
        "q": "Copre proteine vegetali fatte in casa (seitan, tempeh, tofu marinato)?",
        "a": "Sì. VegChef ragiona come chef plant-based professionale: tecniche di seitan impastato, tempeh fermentato, tofu marinato e pressato, mock meats con tecnica di texture."
      },
      {
        "q": "Genera contenuti visivi per Instagram, Glovo e Uber Eats?",
        "a": "Sì. GastroIMG Gen+ genera immagini vibranti di riferimento dei bowl per Instagram, web e delivery; il plant-based vive del colore. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo bowl impiattato reale."
      },
      {
        "q": "Come mi aiuta con Veganuary e eventi plant-based?",
        "a": "Gastro Calendar pianifica Veganuary (gennaio), Giornata Mondiale Vegana, Earth Day e stagioni di verdure locali con menù speciali e calendario editoriale."
      }
    ],
    "ctaTitle": "Il tuo ristorante plant-based con margine reale e tecnica d'autore.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Ristoranti Plant-Based: Bowl, Food Cost e Fermenti",
      "description": "Suite di IA per ristoranti plant-based: VegChef, Fermentus per umami vegetale, schede tecniche per bowl, branding e HACCP. Inizia oggi.",
      "keywords": "IA ristorante vegano, software plant-based, schede tecniche bowl vegano, cucina vegana IA, fermenti vegetali, umami vegetale, Veganuary",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-plant-based.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Ristorante Plant-Based dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di plant-based gestisci (casual healthy bowls, vegan fine dining, hamburgeria plant-based, ristorante vegano d'autore, caffè vegano, dark kitchen vegana), dimensione del team, città e specialità. Ogni agente risponde adattato al tuo prodotto, mercato e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Ristorante Plant-Based",
    "apps": [
      {
        "name": "VegChef Plant-Based",
        "description": "Agente specializzato in cucina plant-based, vegana e vegetariana professionale con tecnica avanzata.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Koji vegetale, miso fatto in casa, shoyu, kimchi, kombucha e lattofermenti per umami profondo.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di bowl signature e piatti plant-based contemporanei.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con vini vegani, kombucha e bevande funzionali.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Ristoranti Casual AI+",
        "description": "Consulenza operativa per ristoranti plant-based casual.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture vegetali, gelificanti plant-based e tecnica.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi su prodotto fresco vegetale, microgreens e proteine fatte in casa.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica: glutine, frutta a guscio, soia, sesamo (senza prodotti animali).",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia vibrante IA di riferimento per Instagram, web, menu e delivery.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale vibrante per plant-based d'autore.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Catturare clienti locali che cercano \"vegano vicino\" o \"plant-based vicino\".",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Veganuary, Giornata Mondiale Vegana, Earth Day, stagioni di verdure.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margine dopo food cost dei bowl"
      },
      {
        "value": "×3",
        "label": "engagement Instagram con GastroIMG"
      },
      {
        "value": "−30 %",
        "label": "sprechi su prodotto fresco"
      },
      {
        "value": "12+",
        "label": "agenti per la tua cucina plant-based"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Umami superficiale senza tecnica di fermentazione professionale",
        "Schede tecniche senza food cost reale, bowl signature in perdita senza saperlo",
        "Sprechi su prodotto fresco vegetale senza tracciabilità",
        "Proteine vegetali fatte in casa improvvisate senza standardizzazione",
        "Instagram improvvisato e piattaforme di delivery con foto del telefono"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Umami profondo con Fermentus: miso, koji, kimchi fatti in casa documentati",
        "Scheda tecnica professionale per bowl con margine validato",
        "Sprechi controllati con Sprechi GenCal e modelli specifici",
        "Proteine vegetali con tecnica documentata (seitan, tempeh, tofu)",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO catturano clienti locali"
      ]
    },
    "galleryTitle": "Come Funziona un Ristorante Plant-Based",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: bowl, burger vegane, fermenti, mercato e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-plantbased-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-burger.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-bowl.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-fermentos.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-mercado.jpg",
      "/lovable-uploads/ai-gallery/use-case-plantbased-team.jpg"
    ]
  },
  "sommelier": {
    "h1": "IA per Sommelier",
    "heroSubtitle": "Progetta carte dei vini con criterio professionale, valida abbinamenti con base scientifica, gestisci la cantina con tracciabilità e cattura branding wine-driven con una suite di agenti IA gastronomica specializzati in sommellerie professionale.",
    "heroTagline": "Cantina con criterio professionale e abbinamenti scientifici",
    "badge": "Per sommelier, head sommelier e direttori di cantina",
    "painsTitle": "Le Questioni che un Sommelier Non Può Lasciare Irrisolte",
    "pains": [
      "Progettare la carta dei vini con criterio: equilibrio di regioni, vitigni, prezzi, calici e verticali per cantina",
      "Validare abbinamenti con base scientifica per ogni piatto del menù degustazione e carta che cambia con la stagione",
      "Gestire la cantina con tracciabilità: rotazione, condizioni della cantina, ordini, perdite per stappatura fallita",
      "Standardizzare lo storytelling di ogni vino affinché il team di sala lo comunichi con professionalità al cliente",
      "Differenziarsi in un ristorante competitivo con cantina curata, stappatura professionale ed esperienza wine-driven",
      "Attrarre clienti premium con degustazioni, eventi in cantina e abbinamenti speciali con margine elevato"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Sommelier",
    "features": [
      {
        "title": "Bar & Lounge AI+",
        "description": "Agente specializzato in sommellerie professionale: cantina, vitigni, regioni, tecnica di stappatura e servizio del vino.",
        "icon": "Wine"
      },
      {
        "title": "Food Pairing AI",
        "description": "Abbinamenti con base scientifica per ogni piatto e vino: analisi di acidità, tannini, struttura, intensità e armonia.",
        "icon": "Sparkles"
      },
      {
        "title": "Cucina Creativa + Storytelling",
        "description": "Storytelling di ogni vino per il team di sala: cantina, terroir, vitigno, vinificazione, note di degustazione.",
        "icon": "BookOpen"
      },
      {
        "title": "Food cost della cantina",
        "description": "Costo reale per calice, food cost del vino per servizio, perdite per stappatura e proposte di carta con margine validato.",
        "icon": "Calculator"
      },
      {
        "title": "Kit di Attività Cantina",
        "description": "Modelli: controllo della cantina (umidità, temperatura), rotazione, stappatura del giorno, formazione del team.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC Cantina",
        "description": "Tracciabilità dei vini, conservazione, stappatura fallita e temperature di servizio per tipo.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Gastro Calendar",
        "description": "Degustazioni ed eventi in cantina: abbinamenti con menù degustazione, lanci, fiere del vino, Natale, eventi privati.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia wine-driven IA di riferimento + Instagram con storytelling di cantina per attrarre clienti premium.",
        "icon": "Image"
      },
      {
        "title": "Sprechi GenCal",
        "description": "Dati precisi sulle perdite per stappatura fallita, calice rotto e vino in tavola.",
        "icon": "BarChart3"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Sommelier con AI Chef Pro",
    "workflow": [
      "11:00 · Apertura — checklist Kit di Attività Cantina: controllo della cantina (12-14 °C, 70 % umidità), revisione degli ordini, rotazione dei vini del giorno.",
      "12:00 · Bar & Lounge AI+ — aggiorni la carta con due nuove referenze (Borgogna rosso e Riesling tedesco). Ricetta + storytelling generato.",
      "13:00 · Food Pairing AI — valuti l'abbinamento del nuovo Riesling con un piatto di pesce fermentato del menù degustazione. Analisi di acidità e armonia.",
      "14:00 · Kit de Escandallos Pro — calcoli il food cost delle due nuove referenze con margine reale per calice e per bottiglia, validi il prezzo suggerito.",
      "15:00 · Briefing al team — spiegazione delle due nuove referenze con storytelling e abbinamenti validati.",
      "17:00 · Degustazione privata per cliente VIP — selezione di cinque vini con abbinamenti ad hoc, stappatura professionale, decanting quando applicabile.",
      "20:00 · Servizio cena — coordinamento con maître e cucina, raccomandazioni per tavolo, guéridon quando applicabile.",
      "23:00 · Chiusura — aggiornamento dello stock, GastroIMG Gen+ genera immagine di riferimento del nuovo Borgogna + InstaFlow programma il post."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Sommelier",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "pro-prompts-ebook",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Bar & Lounge AI+ + Food Pairing AI mi hanno cambiato la proposta. Ogni abbinamento del menù degustazione ha ora una base scientifica documentata che il team di sala comunica al cliente con professionalità. La gestione della cantina con food cost per calice ci ha alzato il margine dei vini di 6 punti. Le degustazioni private per VIP si chiudono in una chiamata con proposta professionale.",
    "testimonialAuthor": "Eduardo Lara",
    "testimonialRole": "Head Sommelier, ristorante con 1 stella Michelin",
    "faqTitle": "Domande Frequenti dei Sommelier",
    "faqs": [
      {
        "q": "È adatto per sommelier di fine dining, ristorante gastronomico, enoteca o hotel?",
        "a": "Per tutti e quattro. Bar & Lounge AI+ copre dal sommelier di ristorante premium fino a head sommelier di gastronomico Michelin, enoteca con cantina curata o hotel con multi-outlet."
      },
      {
        "q": "Come mi aiuta con gli abbinamenti scientifici?",
        "a": "Food Pairing AI ragiona con base scientifica: analisi di acidità, tannini, struttura, intensità, armonia e contrasto. Fonda ogni abbinamento affinché il team di sala lo comunichi con professionalità."
      },
      {
        "q": "Come gestisco il food cost e il margine per calice?",
        "a": "Kit de Escandallos Pro ricalcola il margine per calice e per bottiglia quando aggiorni i prezzi della cantina. Sprechi GenCal aggiunge il costo della stappatura fallita e le perdite in servizio."
      },
      {
        "q": "Genera contenuti visivi wine-driven per Instagram?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento professionali di calici, decanting e cantina per Instagram, web e acquisizione di clienti premium. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo calice reale."
      },
      {
        "q": "Come mi aiuta con degustazioni private ed eventi in cantina?",
        "a": "Gastro Calendar pianifica degustazioni private, eventi in cantina, fiere del vino, lanci di stagione e abbinamenti con menù degustazione."
      }
    ],
    "ctaTitle": "La tua cantina con criterio professionale e abbinamenti scientifici.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Sommelier: Cantina, Abbinamenti e Degustazioni Professionali | AI Chef Pro",
      "description": "Suite di IA per sommelier professionisti: Bar & Lounge AI+, Food Pairing AI, food cost per calice, degustazioni private e branding wine-driven. Inizia oggi.",
      "keywords": "IA sommelier, software sommelier, abbinamenti IA, gestione cantina IA, food cost vino, head sommelier, degustazione privata IA",
      "ogImage": "https://aichef.pro/og/use-cases/sommelier.jpg"
    },
    "personalizationTitle": "Personalizzato sulla Tua Cantina dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui gli racconti che tipo di sommelier sei (head sommelier di fine dining, sommelier freelance, direttore di enoteca, sommelier di hotel, formatore), dimensione della cantina, città e specialità. Ogni agente risponde adattato alla tua cantina e operatività reale.",
    "appsTitle": "Gli Agenti IA che Userai come Sommelier",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "description": "Agente specializzato in sommellerie professionale: cantina, vitigni, regioni, tecnica.",
        "category": "Concetti di Business"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con base scientifica: acidità, tannini, struttura, intensità e armonia.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cucina Creativa",
        "description": "Storytelling di ogni vino: terroir, vinificazione, note di degustazione per il team di sala.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Perdite per stappatura fallita, calice rotto e vino in tavola integrate nel food cost.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione dei solfiti nei vini per clienti con sensibilità.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Gastro Lexicum",
        "description": "Tutor di definizioni tecniche: enologia, vinificazione, terroir, denominazioni.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia wine-driven IA di riferimento per Instagram, web ed eventi.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale wine-driven per attrarre clienti premium.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Attrarre clienti che cercano enoteca, degustazione o sommelier su Google e Maps.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Degustazioni private, fiere del vino, lanci, Natale, eventi in cantina.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Articoli SEO su abbinamenti, vitigni e cantine per attrarre traffico organico.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca approfondita su cantine emergenti, terroir, annate e tendenze.",
        "category": "Modelli IA + LLM"
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margine dopo il food cost della cantina"
      },
      {
        "value": "×2",
        "label": "velocità delle proposte di degustazione"
      },
      {
        "value": "×3",
        "label": "engagement Instagram wine-driven"
      },
      {
        "value": "12+",
        "label": "agenti per la tua cantina"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Abbinamenti consigliati senza base scientifica documentata",
        "Carta dei vini senza food cost per calice e margine reale",
        "Cantina gestita su fogli, senza tracciabilità né rotazione chiara",
        "Storytelling del vino improvvisato, team di sala senza formazione costante",
        "Degustazioni private chiuse a mano, proposta lenta"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Abbinamenti con base scientifica di Food Pairing AI",
        "Food cost per calice con margine validato in tempo reale",
        "Cantina con tracciabilità HACCP e rotazione documentata",
        "Briefing giornaliero al team con storytelling e abbinamenti",
        "Degustazioni private chiuse in un giorno con proposta wine-driven"
      ]
    },
    "galleryTitle": "Come Funziona la Cantina di un Sommelier",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: cantina, decanting, calice, degustazione e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-sommelier-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-decanting.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-copa.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-cellar.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-sommelier-team.jpg"
    ]
  },
  "sous-chef": {
    "h1": "IA per Sous Chef",
    "heroSubtitle": "Organizza le partite, gestisci la mise en place, supervisiona il team e libera ore amministrative con una suite di agenti IA pensati per lo sous chef in cucina professionale.",
    "heroTagline": "Il braccio destro del capo cucina, con sistema",
    "badge": "Per sous chef",
    "painsTitle": "Le cose che un Sous Chef non può lasciare irrisolte",
    "pains": [
      "Coordinare le partite e la mise en place con precisione quando il ritmo non aspetta",
      "Sostituire il capo cucina quando non c'è senza che cali la qualità né l'operatività",
      "Formare e supervisionare il team di cucina con criteri coerenti",
      "Mantenere la tracciabilità HACCP aggiornata senza che si accumuli la burocrazia",
      "Avere accesso rapido a schede tecniche aggiornate durante il servizio",
      "Validare i food cost quando entrano nuovi ingredienti o cambia un fornitore"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta un Sous Chef",
    "features": [
      {
        "title": "Mise en place e compiti per partita",
        "description": "Kit de Tareas con liste strutturate per turno e per partita, pronte da stampare ogni mattina.",
        "icon": "CheckSquare"
      },
      {
        "title": "Schede tecniche sempre aggiornate",
        "description": "Accesso rapido da mobile a ricetta, procedimento, impiattamento e allergeni di ogni piatto durante il servizio.",
        "icon": "BookOpen"
      },
      {
        "title": "HACCP da mobile",
        "description": "Pack APPCC con registri, allerte di temperatura ed esportazione in PDF. Il team registra dal mobile senza burocrazia.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Food cost rapidi",
        "description": "Cucina Creativa consegna ricetta + food cost CSV; il Kit de Escandallos Pro lo gestisce con i tuoi prezzi reali e validi il margine all'istante.",
        "icon": "Calculator"
      },
      {
        "title": "Formazione del team",
        "description": "Pro Prompts eBook + Chef Esecutivo Pro generano manuali e onboarding pronti per nuovi cuochi.",
        "icon": "GraduationCap"
      },
      {
        "title": "Cucina Creativa",
        "description": "Chat IA gastronomica per risolvere dubbi tecnici, proporre piatti fuori menù e validare tecniche in tempo reale.",
        "icon": "Sparkles"
      },
      {
        "title": "Pasto del Personale",
        "description": "Generatore di menù per lo staff che sfrutta il prodotto che hai già in camera e motiva il team.",
        "icon": "Users"
      },
      {
        "title": "ID Allergeni e Sprechi GenCal",
        "description": "Rilevazione automatica degli allergeni e dati precisi sugli sprechi per passaggio e partita.",
        "icon": "ShieldCheck"
      }
    ],
    "workflowTitle": "Una Giornata Reale di un Sous Chef con AI Chef Pro",
    "workflow": [
      "07:30 · Apertura — apri il Kit de Tareas e controlli la mise en place del giorno. Firmi l'inventario critico con il Kit Inventario.",
      "08:30 · Briefing breve con la brigata — ripassi i passaggi del giorno con schede tecniche centralizzate in mano.",
      "12:00 · Servizio di mezzogiorno — supervisioni le partite, il team registra sprechi e temperature dal mobile con il Pack APPCC.",
      "15:30 · Cucina Creativa — il capo cucina ti chiede un fuori menù per sabato. Generi piatto + food cost CSV in 20 minuti.",
      "16:00 · Kit de Escandallos Pro — carichi il CSV con i tuoi prezzi reali, verifichi che il food cost quadri al 28% ed esporti la scheda tecnica.",
      "17:30 · Pasto del Personale — prepari il menù dello staff della prossima settimana rispettando il costo obiettivo e lo stock di camera.",
      "20:00 · Servizio serale — coordini i passaggi con la brigata, gestisci i dubbi con Cucina Creativa quando il cuoco junior deve confermare una tecnica.",
      "23:30 · Chiusura — firmi HACCP, lasci la mise en place del giorno successivo pronta e report inviato al capo cucina."
    ],
    "productsTitle": "Modelli e Kit Scaricabili per Sous Chef",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Essere sous chef significa essere in mille posti contemporaneamente. Le liste di mise en place del Kit de Tareas e i registri HACCP da mobile mi hanno organizzato il caos. Quando il capo cucina non c'è, tutto continua a funzionare perché le procedure sono documentate.",
    "testimonialAuthor": "Nicolás Vega",
    "testimonialRole": "Sous Chef, ristorante da 100 coperti",
    "faqTitle": "Domande Frequenti dei Sous Chef",
    "faqs": [
      {
        "q": "I modelli si adattano allo stile della mia cucina?",
        "a": "Sì. Ci sono Kit de Tareas specifici per concetto (casual, gastronomico, dark kitchen, hotel, pizzeria, hamburgeria, pasticceria, bar, catering, gelateria, cioccolateria, ristorante creativo, chef privato) e tutti possono essere personalizzati allo stile della tua cucina."
      },
      {
        "q": "Funziona da mobile per i registri del team?",
        "a": "Sì. I registri HACCP, sprechi, temperature e check delle attività si fanno dal mobile dello staff senza installare nulla. A fine giornata si esporta in PDF per il capo cucina o il proprietario."
      },
      {
        "q": "È complicato da usare per il team?",
        "a": "No. Il team compila solo caselle o spunta check. La curva reale è di 1 giorno. C'è un video di onboarding di 5 minuti."
      },
      {
        "q": "Serve se non sono io a decidere gli strumenti in cucina?",
        "a": "Puoi iniziare con il piano Membro (10 € al mese, 10.000 crediti) per le tue liste e proposte. Dopo 1-2 settimane di utilizzo, proponi al capo cucina con dati concreti: tempo risparmiato, food cost validati, mise organizzata."
      },
      {
        "q": "Come mi aiuta nei picchi di servizio?",
        "a": "Le schede tecniche centralizzate ti danno accesso rapido dal mobile durante il passaggio. Se sorge un dubbio tecnico, Cucina Creativa risponde in pochi secondi. Mental Coach aiuta anche a gestire lo stress in cucine ad alta pressione."
      },
      {
        "q": "C'è qualcosa di specifico per la promozione a capo cucina?",
        "a": "Sì. Pro Prompts eBook (300+ prompt professionali), Chef Esecutivo Pro (standardizzazione multi-locale) e Gastro Lexicum (riferimento di tecnica) sono strumenti chiave per crescere verso il livello successivo."
      }
    ],
    "ctaTitle": "Organizza la tua cucina senza fogli sparsi.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti per usare tutti gli agenti.",
    "seo": {
      "title": "IA per Sous Chef: Schede Tecniche e HACCP | AI Chef Pro",
      "description": "Suite di IA per sous chef in cucina professionale: mise en place, schede tecniche, food cost, HACCP da mobile e formazione del team. Inizia oggi.",
      "keywords": "IA sous chef, software sous chef, mise en place cucina IA, HACCP sous chef, schede tecniche cucina, formazione brigata cucina, sous chef Italia",
      "ogImage": "https://aichef.pro/og/use-cases/sous-chef.jpg"
    },
    "personalizationTitle": "Personalizzato alla Tua Cucina dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding conversazionale di 2 minuti in cui racconti che tipo di cucina gestisci, in quale città, che menù hai e a che scala. Da quel momento, ogni agente —dalla mise en place ai food cost— risponde adattato al tuo contesto: tipo di servizio, dimensione della brigata e operatività reale. Non è un modulo: è una conversazione breve che rende la suite davvero utile per il ritmo della partita.",
    "appsTitle": "Gli Agenti IA che Userai come Sous Chef",
    "apps": [
      {
        "name": "Chef Esecutivo Pro",
        "description": "Standardizzazione di ricette, schede tecniche e manuali di cucina centralizzati.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Cucina Creativa",
        "description": "Sviluppo di piatti professionali con ricetta + food cost CSV pronto per il Kit de Escandallos Pro.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Combinazioni di ingredienti e abbinamenti con base scientifica.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dolci da ristorante creativi con tecnica di pasticceria professionale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Calcula Pax",
        "description": "Calcolatore di porzioni che scala le ricette a qualsiasi numero di commensali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Conversor Ing",
        "description": "Convertitore di pesi e misure per cucina professionale.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi su sprechi e rese per ingrediente.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta e piatto.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Pasto del Personale",
        "description": "Generatore di menù per lo staff con prodotto che hai già in camera.",
        "category": "Gastro Profile Pro"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching psicologico per gestire stress e conversazioni difficili in cucina.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Gastro Lexicum",
        "description": "Tutor con definizioni di tecniche, processi e scienza gastronomica.",
        "category": "Gastro Conoscenza"
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "velocità mise en place"
      },
      {
        "value": "−4 h",
        "label": "settimanali in burocrazia"
      },
      {
        "value": "stesso",
        "label": "standard quando il capo non c'è"
      },
      {
        "value": "11+",
        "label": "agenti per il tuo ruolo"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Mise en place dettata ogni mattina al team, diversa ogni giorno",
        "HACCP su carta stampata che si accumula a fine settimana",
        "Schede tecniche nel taccuino del capo cucina, inaccessibili durante il servizio",
        "Quando il capo cucina non c'è, qualità e operatività calano",
        "Formazione dei nuovi cuochi improvvisata e disomogenea"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Mise en place stampabile ogni giorno con il Kit de Tareas strutturato per partita",
        "HACCP da mobile con registri, allerte ed esportazione in PDF alla chiusura",
        "Schede tecniche centralizzate accessibili dal mobile durante il servizio",
        "Procedure documentate — lo standard si mantiene anche se cambia il team",
        "Formazione replicabile con copione del Pro Prompts eBook e manuali del Chef Esecutivo Pro"
      ]
    },
    "galleryTitle": "La Giornata Tipo di un Sous Chef, in Immagini",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: mise en place, prep, supervisione del team, servizio in linea e tracciabilità.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-sous-chef-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-prep.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-cooking.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-supervise.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-clipboard.jpg",
      "/lovable-uploads/ai-gallery/use-case-sous-chef-station.jpg"
    ]
  },
  "sushi-bar": {
    "h1": "IA per Sushi Bar",
    "heroSubtitle": "Domina la tecnica itamae con food cost rigoroso per nigiri, gestisci pesce fresco quotidiano, progetta omakase signature e cattura branding minimalista con una suite di agenti di IA gastronomica specializzati in sushi bar professionale.",
    "heroTagline": "Sushi bar con tecnica autentica e margine reale",
    "badge": "Per sushi bar, omakase e sushi shop",
    "painsTitle": "Ciò che un Sushi Bar Non Può Non Risolvere",
    "pains": [
      "Pesce fresco quotidiano per nigiri e sashimi con costo volatile e sprechi rigorosi per processo di sfilettatura",
      "Standardizzare lo shari (riso per sushi) in ogni turno con bilanciamento tecnico di aceto, zucchero e sale",
      "Coordinare la tecnica itamae con consistenza: taglio, pressione, temperatura del riso, neta a temperatura ottimale",
      "Differenziarsi in zona competitiva con omakase signature, fish-of-the-day e storytelling dei fornitori",
      "Attrarre clienti premium con esperienza davanti all'itamae al banco (non al tavolo)",
      "Gestire ordini di delivery senza perdere qualità del sushi (finestra ottimale 1-2 ore)"
    ],
    "featuresTitle": "Come AI Chef Pro Aiuta in un Sushi Bar",
    "features": [
      {
        "title": "Cucina Giapponese",
        "description": "Agente specializzato in sushi professionale: tecnica itamae, bilanciamento dello shari, sfilettatura, neta a temperatura ottimale.",
        "icon": "Fish"
      },
      {
        "title": "Cucina Creativa",
        "description": "Per nigiri signature e omakase contemporaneo con base autentica.",
        "icon": "Sparkles"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Per fermentazioni e tecniche avanzate di cucina giapponese.",
        "icon": "Beaker"
      },
      {
        "title": "Food cost per nigiri e omakase",
        "description": "Cucina Giapponese fornisce ricetta + food cost CSV; Kit de Escandallos Pro lo gestisce con costo reale per pezzo e omakase.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelli: sfilettatura, prep shari, mise itamae, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC sushi",
        "description": "Tracciabilità del pesce per sushi e temperature critiche.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Per sake, whisky giapponese e abbinamenti professionali.",
        "icon": "Wine"
      },
      {
        "title": "Gastro Calendar",
        "description": "Hanami, Capodanno giapponese, Giornata del Sushi, eventi premium.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Fotografia minimalista IA di riferimento + Instagram per sushi bar premium.",
        "icon": "Image"
      }
    ],
    "workflowTitle": "Una Giornata Reale in un Sushi Bar con AI Chef Pro",
    "workflow": [
      "08:00 · Apertura — checklist Kit de Tareas: ricezione pesce fresco quotidiano, sfilettatura dei blocchi, prep shari (aceto + zucchero + sale bilanciati).",
      "10:00 · Cucina Giapponese — sviluppi un nuovo nigiri signature di hamachi con yuzu kosho e wasabi fresco. Ricetta + food cost CSV.",
      "11:00 · Kit de Escandallos Pro — carichi il CSV con i tuoi prezzi reali del pesce del giorno, validi il margine per nigiri e per omakase.",
      "13:00 · Servizio mezzogiorno — sushi bar al completo con itamae che lavora davanti al cliente.",
      "17:00 · Briefing al team — spiegazione del nuovo nigiri e abbinamenti con sake.",
      "20:00 · Servizio cena — omakase signature, picchi coordinati.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — generi immagine di riferimento minimalista del nuovo nigiri.",
      "23:00 · Chiusura — pulizia profonda, HACCP firmato."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Sushi Bar",
    "productIds": [
      "guia-restaurante-japones",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cucina Giapponese ci ha cambiato l'operatività. Il bilanciamento dello shari è ora consistente, l'omakase ha un food cost professionale con margine validato pezzo per pezzo. L'attrazione di clienti premium con GastroIMG Gen+ è salita del 40% in 6 mesi.",
    "testimonialAuthor": "Akio Yamamoto",
    "testimonialRole": "Itamae e proprietario, sushi bar contemporaneo",
    "faqTitle": "Domande Frequenti dei Sushi Bar",
    "faqs": [
      {
        "q": "Serve per sushi bar casual o omakase premium?",
        "a": "Per entrambi. Cucina Giapponese copre dal sushi tradizionale all'omakase d'autore."
      },
      {
        "q": "Copre la tecnica itamae?",
        "a": "Sì. Cucina Giapponese ragiona come un itamae professionale: tecnica di sfilettatura, bilanciamento dello shari, neta e combinazioni."
      },
      {
        "q": "Come gestisco il costo del pesce fresco?",
        "a": "Kit de Escandallos Pro ricalcola all'istante il margine quando aggiorni i prezzi del giorno."
      },
      {
        "q": "Genera contenuti visual minimalisti?",
        "a": "Sì. GastroIMG Gen+ genera immagini di riferimento. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo pezzo reale."
      },
      {
        "q": "Come mi aiuta con omakase ed eventi premium?",
        "a": "Gastro Calendar pianifica omakase stagionale, Hanami, Capodanno giapponese con menù degustazione premium."
      }
    ],
    "ctaTitle": "Il tuo sushi bar con tecnica autentica e margine reale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "IA per Sushi Bar: Itamae, Omakase e Food Cost | AI Chef Pro",
      "description": "Suite di IA per sushi bar: Cucina Giapponese, Fermentus, food cost per nigiri, omakase e branding minimalista. Inizia oggi.",
      "keywords": "IA sushi bar, software sushi, food cost sushi, itamae professionale, omakase IA, tecnica giapponese",
      "ogImage": "https://aichef.pro/og/use-cases/sushi-bar.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Sushi Bar dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding di 2 minuti in cui gli racconti che tipo di sushi bar gestisci (sushi bar casual, omakase premium, kaiten, sushi bar con cucina calda), dimensione del team, città e specialità.",
    "appsTitle": "Gli Agenti IA che Userai nel Tuo Sushi Bar",
    "apps": [
      {
        "name": "Cucina Giapponese",
        "description": "Sushi professionale: tecnica itamae, sashimi, omakase.",
        "category": "Ricettari Asiatici"
      },
      {
        "name": "Cucina Creativa",
        "description": "Nigiri signature e omakase con ricetta + food cost CSV.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Fermentazioni per tecniche avanzate.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con sake, whisky giapponese e birra.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Banco di sake e whisky giapponese.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi nella sfilettatura del pesce.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione di pesce, crostacei, soia, glutine.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia minimalista IA di riferimento.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram minimalista per sushi bar premium.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Attrarre clienti che cercano \"sushi vicino\".",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Hanami, Capodanno giapponese, omakase stagionale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture avanzate.",
        "category": "Fornitori Gastro"
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "margine dopo food cost omakase"
      },
      {
        "value": "+40 %",
        "label": "attrazione premium in 6 mesi"
      },
      {
        "value": "−20 %",
        "label": "sprechi in sfilettatura"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo sushi bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Shari improvvisato, bilanciamento inconsistente",
        "Food cost senza prezzo del pesce del giorno",
        "Omakase improvvisato senza food cost",
        "Instagram senza palette minimalista",
        "Attrazione locale senza SEO"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Shari e tecnica con criterio professionale",
        "Food cost in tempo reale con prezzo del giorno",
        "Omakase con food cost validato pezzo per pezzo",
        "GastroIMG Gen+ + InstaFlow minimalisti",
        "MenuDish Local SEO cattura \"sushi vicino\""
      ]
    },
    "galleryTitle": "Come Funziona un Sushi Bar",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: banco, omakase, pesce, sake e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-counter.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-omakase.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-fish.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-sake.jpg",
      "/lovable-uploads/ai-gallery/use-case-sushi-bar-team.jpg"
    ]
  },
  "task-appcc-digital-con-ia": {
    "h1": "Come Gestire l'HACCP Digitale con IA",
    "heroSubtitle": "Sostituisci la carta sparsa con HACCP da smartphone con modelli professionali: temperature, pulizia, tracciabilità, allergeni, parassiti, olio e acqua. Suite di agenti IA gastronomica con base normativa.",
    "heroTagline": "HACCP professionale da smartphone senza carta",
    "badge": "Compito: HACCP e sicurezza alimentare",
    "painsTitle": "Quanto Costa Gestire l'HACCP su Carta",
    "pains": [
      "Carta stampata sparsa per la cucina, registri incompleti durante le ispezioni",
      "Nessuna standardizzazione per tipo di attività (gelateria, panificazione, griglia, sushi hanno registri diversi)",
      "Allergeni calcolati a mano per ricetta, rischio legale e di sicurezza",
      "Cambi normativi senza aggiornamento di modelli e procedure",
      "Team turnante senza formazione costante sulla sicurezza alimentare",
      "Nessuna tracciabilità per audit ISO 22000, BRC, IFS o certificazioni di qualità"
    ],
    "featuresTitle": "Come AI Chef Pro Risolve l'HACCP",
    "features": [
      {
        "title": "Pack HACCP con modelli Excel",
        "description": "17 modelli Excel scaricabili: temperature, pulizia, tracciabilità, allergeni, parassiti, olio e acqua.",
        "icon": "ShieldCheck"
      },
      {
        "title": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ingrediente e ricetta. Quando cambi un ingrediente, ricalcola all'istante.",
        "icon": "Sparkles"
      },
      {
        "title": "Kit di Attività con HACCP",
        "description": "Modelli di attività con HACCP integrato per turno: apertura, servizio, chiusura.",
        "icon": "CheckSquare"
      },
      {
        "title": "Tracciabilità dei prodotti",
        "description": "Tracciabilità di pesce fresco, latticini, frutta secca, fermentati, conserve con temperature critiche.",
        "icon": "BarChart3"
      },
      {
        "title": "Cucina Creativa con HACCP",
        "description": "Ricette che includono procedure HACCP integrate nella scheda tecnica: temperatura, conservazione, allergeni.",
        "icon": "BookOpen"
      },
      {
        "title": "Pulizia programmata",
        "description": "Calendario di pulizia profonda per stazione e turno con modelli specifici e firma digitale.",
        "icon": "Calendar"
      },
      {
        "title": "Pro Prompts eBook",
        "description": "300+ prompt professionali per gestione HACCP, formazione del team e comunicazione con gli ispettori.",
        "icon": "Sparkles"
      },
      {
        "title": "Pack HACCP per cantina",
        "description": "Tracciabilità dei vini, stappatura, conservazione e temperature di servizio per tipo.",
        "icon": "Wine"
      },
      {
        "title": "Sonar Deep Research",
        "description": "Ricerca approfondita della normativa sanitaria per paese, regione e tipo di attività.",
        "icon": "BarChart3"
      }
    ],
    "workflowTitle": "Come Implementare l'HACCP Digitale in 4 Passi",
    "workflow": [
      "1. Pack HACCP (€14, modelli Excel scaricabili) — scarichi i 17 modelli professionali adattati al tuo tipo di cucina (pasticceria, gelateria, ristorante, ecc.).",
      "2. ID Allergeni — scansiona automaticamente le ricette e i modelli del tuo menu per identificare gli allergeni per piatto. Lo integra nelle schede tecniche e in sala.",
      "3. Cucina Creativa con HACCP integrato — ogni nuova ricetta fornisce procedure HACCP (temperatura critica, conservazione, allergeni, stoccaggio) integrate nella scheda tecnica.",
      "4. Kit di Attività con HACCP — modelli di turno (apertura, servizio, chiusura) con HACCP integrato. Il team firma digitalmente ogni turno da smartphone."
    ],
    "productsTitle": "Modelli e Kit Consigliati per l'HACCP",
    "productIds": [
      "pack-appcc",
      "kit-tareas",
      "pro-prompts-ebook",
      "kit-escandallos",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Pack HACCP + ID Allergeni ci hanno trasformato la sicurezza alimentare. Siamo passati da carta stampata sparsa a 17 modelli digitali con HACCP integrato per turno e allergeni automatici per ricetta. L'ispezione sanitaria è impeccabile e il rischio legale è sceso a zero.",
    "testimonialAuthor": "Roberto Castaño",
    "testimonialRole": "F&B Director, hotel 5 stelle con 4 punti vendita",
    "faqTitle": "Domande Frequenti sull'HACCP con IA",
    "faqs": [
      {
        "q": "Va bene per qualsiasi tipo di attività?",
        "a": "Sì. Pack HACCP adatta i modelli a ristorante, caffetteria, pasticceria, gelateria, cioccolateria, pizzeria, dark kitchen, bar, catering, hotel."
      },
      {
        "q": "Come gestisco gli allergeni automaticamente?",
        "a": "ID Allergeni identifica gli allergeni per ingrediente e ricetta, li integra nelle schede tecniche e nei modelli HACCP. Quando cambi un ingrediente ricalcola all'istante."
      },
      {
        "q": "Copre la normativa europea e latinoamericana?",
        "a": "Sì. Pack HACCP copre la normativa europea (UE 852/2004 + 178/2002 + 1169/2011 allergeni) e gli adattamenti per il Latam. Sonar Deep Research consente di consultare la normativa specifica per paese."
      },
      {
        "q": "Genera tracciabilità per audit ISO?",
        "a": "Sì. HACCP da smartphone con firma digitale + tracciabilità dei prodotti + calendario di pulizia pronti per audit ISO 22000, BRC, IFS, FSSC 22000."
      },
      {
        "q": "Come mi aiuta con i cambi normativi?",
        "a": "Sonar Deep Research consulta la normativa aggiornata per paese e regione. Cucina Creativa aggiorna le schede tecniche e le procedure quando cambiano le regole."
      }
    ],
    "ctaTitle": "Il tuo HACCP professionale da smartphone senza carta.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "Come Gestire l'HACCP Digitale con IA: Modelli, Allergeni e Tracciabilità | AI Chef Pro",
      "description": "Suite IA per HACCP digitale: modelli Excel, allergeni automatici, tracciabilità ISO. Inizia oggi.",
      "keywords": "HACCP digitale IA, modelli HACCP, allergeni automatici, ISO 22000 IA, sicurezza alimentare IA, HACCP digitale",
      "ogImage": "https://aichef.pro/og/use-cases/task-appcc-digital-con-ia.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Attività dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con «Chi sono?»: racconti il tipo di attività e il paese. Pack HACCP adatta i modelli al tuo concetto e alla normativa locale.",
    "appsTitle": "Gli Agenti IA che Usi per l'HACCP",
    "apps": [
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Cucina Creativa",
        "description": "Ricette con procedure HACCP integrate.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "HACCP specifico per pasticceria e laboratori.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Gelateria Creativa",
        "description": "HACCP specifico per gelateria con prodotto sensibile.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cioccolateria Creativa",
        "description": "HACCP specifico per cioccolateria e bomboneria.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Tracciabilità degli sprechi integrata all'HACCP.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Conversor Ing",
        "description": "Convertitore di pesi e misure.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca approfondita della normativa per paese.",
        "category": "Modelli IA + LLM"
      },
      {
        "name": "Gastro Lexicum",
        "description": "Tutor di definizioni tecniche normative.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Pro Prompts eBook",
        "description": "300+ prompt per la gestione HACCP.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Articoli sulla sicurezza alimentare per traffico organico.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching per la gestione dello stress nelle ispezioni.",
        "category": "Strumenti e Utility"
      }
    ],
    "metrics": [
      {
        "value": "ISO",
        "label": "modelli pronti per 22000, BRC, IFS"
      },
      {
        "value": "100 %",
        "label": "allergeni identificati automaticamente"
      },
      {
        "value": "0 %",
        "label": "rischio legale per allergeni non dichiarati"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo HACCP"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Carta stampata sparsa per la cucina",
        "Allergeni calcolati a mano (rischio legale)",
        "Nessun modello adattato al tipo di cucina",
        "Team turnante senza formazione documentata",
        "Nessuna tracciabilità per audit ISO"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "HACCP da smartphone con firma digitale",
        "Allergeni automatici con ID Allergeni",
        "Modelli Excel adattati per concetto",
        "Briefing con HACCP integrato nel Kit di Attività",
        "Tracciabilità pronta per ISO 22000, BRC, IFS"
      ]
    },
    "galleryTitle": "Come Funziona l'HACCP Digitale con IA",
    "gallerySubtitle": "Cosa coordinerai con AI Chef Pro: termometro, tablet, fotocamera, pulizia e team. Immagini generate con IA come riferimento visivo del concetto.",
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
    "h1": "Come Progettare un Menù Stagionale con l'IA",
    "heroSubtitle": "Progetta un menù stagionale con prodotti locali di stagione, scheda tecnica professionale, pianificazione anticipata e storytelling dei produttori. Suite di agenti IA gastronomici con calendario per emisfero e regione.",
    "heroTagline": "Menù di stagione con criterio professionale in poche ore",
    "badge": "Attività: Menù stagionale",
    "painsTitle": "Quanto Costa Progettare un Menù Stagionale a Mano",
    "pains": [
      "Una settimana o più per iterare e chiudere il menù di stagione con scheda tecnica validata",
      "Senza un criterio chiaro di prodotto locale per stagione e regione (cambia tra emisferi)",
      "Prodotto fuori stagione con costi elevati e sprechi alti (importazione, refrigerazione)",
      "Senza storytelling dei produttori locali per sala e comunicazione",
      "Cambi bruschi tra stagioni senza pianificazione anticipata",
      "Senza coordinamento con il calendario delle festività (Pasqua, Natale, Festa della Mamma, eventi locali)"
    ],
    "featuresTitle": "Come AI Chef Pro Risolve il Menù Stagionale",
    "features": [
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione stagionale per emisfero e regione con prodotto locale di stagione e festività chiave.",
        "icon": "Calendar"
      },
      {
        "title": "Cucina Creativa stagionale",
        "description": "Ragiona piatti signature con prodotto locale di stagione: funghi autunno, asparagi primavera, ortaggi estate, radici inverno.",
        "icon": "Sparkles"
      },
      {
        "title": "Scheda tecnica stagionale",
        "description": "Ricetta + scheda tecnica CSV con prodotto locale; Kit Escandallos Pro ricalcola il margine al cambio di stagione.",
        "icon": "Calculator"
      },
      {
        "title": "Storytelling dei produttori",
        "description": "Ogni piatto include storytelling del produttore locale: allevatore, agricoltore, panettiere, pescatore, per la comunicazione con sala e cliente.",
        "icon": "BookOpen"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Vini di stagione e abbinamenti adattati al prodotto stagionale per il tuo menù.",
        "icon": "Wine"
      },
      {
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Fotografia stagionale IA + Pinterest cattura traffico organico per prodotto di stagione.",
        "icon": "Image"
      },
      {
        "title": "Kit de Tareas Restaurante",
        "description": "Modelli di transizione tra stagioni: rotazione scorte, formazione del team, lancio del menù.",
        "icon": "CheckSquare"
      },
      {
        "title": "VegChef Plant-Based",
        "description": "Per verdure di stagione con tecnica avanzata (fermenti, disidratati, conserve).",
        "icon": "Sparkles"
      },
      {
        "title": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per completare il prodotto locale con tecnica professionale.",
        "icon": "BarChart3"
      }
    ],
    "workflowTitle": "Come Progettare un Menù Stagionale in 5 Passi",
    "workflow": [
      "1. Gastro Calendar — definisci emisfero, regione e stagione (es. autunno Emisfero Nord, Milano). L'agente IA fornisce prodotto locale di stagione e festività chiave (Festa della Mamma, Natale, San Valentino).",
      "2. Cucina Creativa — sviluppi piatti signature con prodotto locale. Ogni ricetta fornisce ricetta + scheda tecnica CSV + storytelling del produttore.",
      "3. Kit Escandallos Pro — carichi i CSV con i tuoi prezzi reali dei fornitori locali, validi margine e food cost % per piatto e menù totale.",
      "4. Bar & Lounge AI+ + Food Pairing AI — aggiorni vini di stagione e abbinamenti adattati al prodotto stagionale.",
      "5. GastroIMG Gen+ + Pinterest Pins Gen — generi immagini di riferimento del nuovo menù e pin ottimizzati per catturare traffico organico stagionale."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Menù Stagionale",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Gastro Calendar + Cucina Creativa ci hanno cambiato la chiusura dei menù stagionali. Quello che prima era una settimana ora è un giorno con scheda tecnica professionale, prodotto locale tracciato e storytelling dei produttori per la sala. Abbiamo aumentato il margine di 6 punti e l'acquisizione con Pinterest Pins Gen per il prodotto di stagione è raddoppiata.",
    "testimonialAuthor": "Giulia Bianchi",
    "testimonialRole": "Chef esecutiva, ristorante d'autore con prodotto locale",
    "faqTitle": "Domande Frequenti sul Menù Stagionale con l'IA",
    "faqs": [
      {
        "q": "Funziona per emisfero nord e sud?",
        "a": "Sì. Gastro Calendar adatta prodotto locale e stagione per emisfero e regione. Quello che è autunno in Italia è primavera in Argentina."
      },
      {
        "q": "Come gestisce il prodotto locale con costo variabile?",
        "a": "Kit Escandallos Pro ricalcola all'istante il margine quando aggiorni i prezzi. Sprechi GenCal aggiunge il costo degli sprechi stagionali (maggiore per prodotto fuori stagione)."
      },
      {
        "q": "Copre le festività per regione?",
        "a": "Sì. Gastro Calendar pianifica festività chiave per paese e regione: Pasqua, Natale, Festa della Mamma, San Valentino, feste locali (Carnevale, Ferragosto, ecc.)."
      },
      {
        "q": "Genera contenuti visivi stagionali?",
        "a": "Sì. GastroIMG Gen+ + Pinterest Pins Gen generano immagini di riferimento e pin per catturare traffico organico stagionale. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo piatto reale."
      },
      {
        "q": "Come mi aiuta con lo storytelling dei produttori?",
        "a": "Cucina Creativa ragiona in chiave di prodotto locale: allevatore di razza autoctona, agricoltore biologico, pescatore artigianale, panettiere locale. Ogni piatto include storytelling professionale per sala e comunicazione."
      }
    ],
    "ctaTitle": "Il tuo menù stagionale con prodotto locale e margine reale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "Menù Stagionale con IA: Prodotto Locale e Scheda Tecnica",
      "description": "Suite IA per menù stagionale: Gastro Calendar, prodotto locale, scheda tecnica e storytelling dei produttori. Inizia oggi.",
      "keywords": "menù stagionale IA, menù stagionale, prodotto locale ristorante, gastro calendar, menù autunno primavera IA",
      "ogImage": "https://aichef.pro/og/use-cases/task-carta-estacional-con-ia.jpg"
    },
    "personalizationTitle": "Personalizzato per il Tuo Ristorante dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con «Chi sono?»: racconti tipo di ristorante, emisfero, regione e approccio (km 0, prodotto locale, cucina d'autore). Ogni agente risponde adattato al tuo mercato reale.",
    "appsTitle": "Gli Agenti IA che Usi per il Menù Stagionale",
    "apps": [
      {
        "name": "Gastro Calendar",
        "description": "Pianificazione stagionale per emisfero e regione.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Cucina Creativa",
        "description": "Piatti signature con prodotto locale di stagione.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Dolci con frutta e prodotto stagionale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "VegChef Plant-Based",
        "description": "Verdure di stagione con tecnica avanzata.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti adattati al prodotto stagionale.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Vini di stagione per il tuo menù.",
        "category": "Concetti di Business"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per completare il prodotto locale.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi stagionali integrati nella scheda tecnica.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Calcula Pax",
        "description": "Scalabilità per eventi privati di stagione.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Fotografia stagionale IA di riferimento.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico stagionale.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Articoli SEO su prodotto locale di stagione.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "velocità vs. processo manuale"
      },
      {
        "value": "+6 pp",
        "label": "margine dopo scheda tecnica del menù"
      },
      {
        "value": "×2",
        "label": "traffico organico stagionale"
      },
      {
        "value": "12+",
        "label": "agenti per menù stagionale"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Una settimana di iterazioni per ogni nuovo menù",
        "Prodotto fuori stagione con costi elevati",
        "Senza storytelling dei produttori locali",
        "Festività reattive, senza pianificazione",
        "Senza contenuti visivi per l'acquisizione stagionale"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Menù stagionale chiuso in un giorno",
        "Prodotto locale di stagione con costi ottimizzati",
        "Storytelling professionale dei produttori",
        "Festività pianificate con 8 settimane di anticipo",
        "GastroIMG Gen+ + Pinterest catturano traffico stagionale"
      ]
    },
    "galleryTitle": "Come Funziona la Progettazione del Menù Stagionale con l'IA",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: prodotto autunno, primavera, calendario, tasting e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-otono.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-primavera.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-calendar.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-tasting.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-carta-estacional-team.jpg"
    ]
  },
  "task-escandallos-con-ia": {
    "h1": "Come Fare il Food Cost con IA",
    "heroSubtitle": "Calcola il costo reale per piatto, food cost % e prezzo suggerito in minuti invece che in giorni: ricetta + scheda tecnica CSV automatica con costo orario laboratorio, sfridi integrati e margine validato in tempo reale con una suite di agenti di IA gastronomica.",
    "heroTagline": "Schede tecniche professionali in minuti, non in ore",
    "badge": "Attività: Schede tecniche e costing",
    "painsTitle": "Quanto Costa Fare le Schede Tecniche a Mano",
    "pains": [
      "Una settimana di calcolatrice e tovaglioli per fare le schede tecniche di un nuovo menu di 30 piatti",
      "Senza costo orario laboratorio integrato, piatti complessi in perdita senza saperlo",
      "Sfridi stimati a occhio (30% in alcuni tagli), non dati reali per processo",
      "Quando il prezzo del fornitore cambia, tutto si squilibra e non si aggiorna",
      "Mancanza di criterio per decidere il food cost obiettivo in base al tipo di piatto (signature, antipasto, dessert)",
      "Senza tracciabilità del calcolo: se ti chiedono di auditare, non sai da dove viene ogni numero"
    ],
    "featuresTitle": "Come AI Chef Pro Risolve le Schede Tecniche",
    "features": [
      {
        "title": "Cucina Creativa + scheda tecnica CSV",
        "description": "Qualsiasi agente creativo (Cucina, Pasticceria, Gelateria, Cioccolateria) consegna ricetta + scheda tecnica CSV con bilanciamento tecnico e costo orario laboratorio integrato.",
        "icon": "Calculator"
      },
      {
        "title": "Sprechi GenCal",
        "description": "Dati precisi sugli sfridi per processo (sezionamento, tostatura, abbattimento, vetrina, formatura) integrati automaticamente nel CSV.",
        "icon": "BarChart3"
      },
      {
        "title": "Sosa Ingredients AI",
        "description": "Catalogo Sosa con prezzi di riferimento per ingredienti tecnici professionali.",
        "icon": "Beaker"
      },
      {
        "title": "Calcula Pax + Conversor Ing",
        "description": "Scala ricette a 2, 6, 12, 100 pax senza perdere precisione; convertitore automatico di pesi e misure.",
        "icon": "Sparkles"
      },
      {
        "title": "Kit de Escandallos Pro",
        "description": "Modelli Excel scaricabili che ricevono il CSV e calcolano margine reale, food cost % e prezzo suggerito all'istante.",
        "icon": "CheckSquare"
      },
      {
        "title": "Schede Tecniche con Costo",
        "description": "Ogni ricetta consegna scheda tecnica completa con costo, allergeni, tecnica e storytelling per la sala.",
        "icon": "BookOpen"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Immagine di riferimento generata con IA del piatto con scheda tecnica per visualizzare prima di cucinare (non la foto definitiva).",
        "icon": "Image"
      },
      {
        "title": "Pro Prompts eBook",
        "description": "eBook con 300+ prompt professionali per fare schede tecniche, validare e ottimizzare i costi con IA gastronomica.",
        "icon": "BookOpen"
      },
      {
        "title": "Applicabile a Qualsiasi Concetto",
        "description": "Ristorante, caffetteria, pasticceria, gelateria, cioccolateria, pizzeria, bar, catering, hotel: il flusso è lo stesso.",
        "icon": "Wine"
      }
    ],
    "workflowTitle": "Come Fare le Schede Tecniche con IA in 4 Passi",
    "workflow": [
      "1. Cucina Creativa (o l'agente creativo del tuo concetto: Pasticceria, Gelateria, Cioccolateria, Cucina Italiana, Messicana, Peruviana, Giapponese) — sviluppi o carichi la ricetta. L'agente IA consegna ricetta + scheda tecnica CSV con bilanciamento tecnico, sfridi stimati e storytelling.",
      "2. Sosa Ingredients AI + Sprechi GenCal — l'IA arricchisce il CSV con prezzi di riferimento e sfridi reali per processo del tuo tipo di cucina.",
      "3. Kit de Escandallos Pro (modello Excel scaricabile, €12) — carichi il CSV con i tuoi prezzi reali dei fornitori. L'Excel calcola margine reale, food cost %, prezzo suggerito per canale (sala, delivery, eventi) e proposta economica.",
      "4. Calcula Pax + Conversor Ing — se devi scalare la ricetta per banchetti (50, 100, 300 pax) o convertire unità, gli agenti IA lo fanno all'istante mantenendo la scheda tecnica."
    ],
    "productsTitle": "Modelli e Kit Consigliati per le Schede Tecniche",
    "productIds": [
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-inventario",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Quello che prima era una settimana di calcolatrice ora sono 30 minuti. Cucina Creativa consegna la scheda tecnica CSV, Sprechi GenCal la arricchisce con dati reali e il Kit de Escandallos Pro mi dà margine validato. Abbiamo rinnovato il menu di 28 piatti in un solo giorno e aumentato il margine di 6 punti scoprendo piatti in perdita che non sapevamo.",
    "testimonialAuthor": "Pablo Ruiz",
    "testimonialRole": "Chef e proprietario, ristorante casual con 4 punti",
    "faqTitle": "Domande Frequenti sulle Schede Tecniche con IA",
    "faqs": [
      {
        "q": "Funziona per qualsiasi tipo di cucina?",
        "a": "Sì. Il flusso è lo stesso per cucina creativa, pasticceria, gelateria, cioccolateria, pizzeria, cucina messicana, peruviana, giapponese, italiana, plant-based o qualsiasi concetto. Cambia solo l'agente creativo di partenza."
      },
      {
        "q": "Come gestisce il costo orario del laboratorio?",
        "a": "Il CSV include un campo di tempo di lavorazione per processo (miscelazione, formatura, cottura, decorazione). Il Kit de Escandallos Pro moltiplica per il tuo costo orario reale (stipendio + oneri) e lo integra nel margine reale."
      },
      {
        "q": "Come rifletto il prezzo variabile dei fornitori (cacao, pesce, carne)?",
        "a": "Il Kit de Escandallos Pro ricalcola all'istante il margine quando aggiorni i prezzi. Sprechi GenCal aggiunge il costo degli sfridi per processo. Il piatto riflette sempre il costo attuale, non quello di tre mesi fa."
      },
      {
        "q": "Copre il ridimensionamento per banchetti ed eventi?",
        "a": "Sì. Calcula Pax scala le ricette a qualsiasi numero di commensali senza perdere precisione; il Kit de Escandallos Pro ricalcola il costo per persona e la proposta economica al cliente aziendale."
      },
      {
        "q": "Genera un'immagine di riferimento del piatto con scheda tecnica?",
        "a": "Sì. GastroIMG Gen+ genera un'immagine di riferimento visiva del piatto. Ricorda che l'immagine IA è di riferimento: la foto definitiva della scheda tecnica la fai tu con il tuo piatto reale impiattato."
      }
    ],
    "ctaTitle": "Le tue schede tecniche in minuti con margine reale validato.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "Come Fare il Food Cost con IA: Costo, Margine | AI Chef Pro",
      "description": "Suite di IA per food cost professionale: ricetta + CSV con costo orario laboratorio, sfridi integrati, margine validato. Inizia oggi.",
      "keywords": "schede tecniche con IA, calcolare food cost, costo reale piatto, scheda tecnica CSV, kit schede tecniche, food cost ristorante",
      "ogImage": "https://aichef.pro/og/use-cases/task-escandallos-con-ia.jpg"
    },
    "personalizationTitle": "Personalizzato per la Tua Cucina dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con l'agente «Chi sono?», un onboarding di 2 minuti in cui racconti che tipo di cucina fai e il flusso delle schede tecniche si adatta al tuo concetto: Cucina Creativa per ristorante, Pasticceria Creativa per laboratorio, Gelateria Creativa per gelateria, ecc.",
    "appsTitle": "Gli Agenti IA che Usi per le Schede Tecniche",
    "apps": [
      {
        "name": "Cucina Creativa",
        "description": "Ricette + scheda tecnica CSV con bilanciamento tecnico e sfridi stimati.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Ricette dolci con costo orario laboratorio integrato.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Gelateria Creativa",
        "description": "Ricette con bilanciamento tecnico di zuccheri, solidi e grassi.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Cioccolateria Creativa",
        "description": "Ricette con coperture, ganache e tecnica di temperaggio.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati precisi sugli sfridi per processo integrati nella scheda tecnica.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Calcula Pax",
        "description": "Ridimensionamento delle ricette per qualsiasi numero di commensali.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Conversor Ing",
        "description": "Convertitore automatico di pesi e misure.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ingrediente.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Prezzi di riferimento e tecnica con catalogo Sosa.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Prezzi e tecnica con catalogo tSpoonLab.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Immagine di riferimento del piatto con scheda tecnica.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca approfondita su fornitori e prezzi di mercato.",
        "category": "Modelli IA + LLM"
      }
    ],
    "metrics": [
      {
        "value": "×30",
        "label": "velocità vs. calcolatrice a mano"
      },
      {
        "value": "+6 pp",
        "label": "margine dopo il food cost del menu"
      },
      {
        "value": "−25 %",
        "label": "sfridi con dati reali"
      },
      {
        "value": "12+",
        "label": "agenti per le schede tecniche"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Una settimana per un nuovo menu di 30 piatti",
        "Senza costo orario laboratorio, piatti complessi in perdita",
        "Sfridi stimati a occhio, non dati reali",
        "Prezzi dei fornitori cambiati senza aggiornare il margine",
        "Senza tracciabilità del calcolo"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Un nuovo menu di 30 piatti con schede tecniche in un giorno",
        "Costo orario laboratorio integrato automaticamente",
        "Sfridi reali con Sprechi GenCal e modelli",
        "Prezzi aggiornabili: margine ricalcolato all'istante",
        "CSV tracciabile + scheda tecnica con costo per audit"
      ]
    },
    "galleryTitle": "Come Funziona il Flusso delle Schede Tecniche con IA",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: ricetta, CSV, sfridi, ricettario digitale e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-csv.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-recipe.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-merma.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-escandallos-team.jpg"
    ]
  },
  "task-fichas-tecnicas-con-ia": {
    "h1": "Come Creare Schede Tecniche con IA",
    "heroSubtitle": "Documenta ogni piatto con scheda tecnica professionale: ingredienti, grammatura, tecnica passo passo, allergeni, food cost, foto dell'impiattamento e storytelling per la sala. La suite di agenti IA gastronomici genera la scheda completa in pochi minuti.",
    "heroTagline": "Schede tecniche professionali in minuti, non in ore",
    "badge": "Compito: Schede tecniche",
    "painsTitle": "Quanto Costa Fare Schede Tecniche a Mano",
    "pains": [
      "Documentare 30 piatti con scheda tecnica professionale può richiedere 2 settimane",
      "Senza standardizzazione, ogni cuoco replica la sua versione e perde coerenza",
      "Allergeni calcolati a mano per ricetta, rischio legale e di sicurezza alimentare",
      "Senza storytelling per la sala, il team descrive il piatto improvvisando",
      "Quando si cambia un ingrediente, bisogna aggiornare la scheda e ricalcolare gli allergeni",
      "Mancanza di un modello professionale con tutti i campi critici (tecnica, grammatura, sprechi, costo)"
    ],
    "featuresTitle": "Come AI Chef Pro Risolve le Schede Tecniche",
    "features": [
      {
        "title": "Cucina Creativa con scheda completa",
        "description": "Ogni ricetta fornisce scheda tecnica professionale: ingredienti, grammatura, tecnica, allergeni, sprechi, costo, storytelling, impiattamento.",
        "icon": "BookOpen"
      },
      {
        "title": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta: latticini, glutine, frutta a guscio, soia, crostacei, solfiti, ecc.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Costo integrato",
        "description": "La scheda tecnica include food cost % e costo per porzione calcolato automaticamente con costo ora laboratorio.",
        "icon": "Calculator"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Immagine di riferimento del piatto impiattato da includere nella scheda tecnica come guida visiva.",
        "icon": "Image"
      },
      {
        "title": "Storytelling per la sala",
        "description": "Ogni scheda include una descrizione professionale affinché il team di sala la descriva con tecnica.",
        "icon": "Sparkles"
      },
      {
        "title": "Modello standardizzato",
        "description": "Formato uniforme per tutte le schede: tecnica, conservazione, allergeni, presentazione, costo.",
        "icon": "CheckSquare"
      },
      {
        "title": "Conversor Ing + Calcula Pax",
        "description": "Convertitore di pesi e misure; scalatura automatica per banchetti ed eventi.",
        "icon": "BarChart3"
      },
      {
        "title": "Pro Prompts eBook",
        "description": "eBook con 300+ prompt professionali per schede tecniche, allergeni e descrizioni per la sala.",
        "icon": "BookOpen"
      },
      {
        "title": "Abbinamento nella scheda",
        "description": "Food Pairing AI suggerisce l'abbinamento consigliato da includere nella scheda tecnica.",
        "icon": "Wine"
      }
    ],
    "workflowTitle": "Come Creare Schede Tecniche in 4 Passi",
    "workflow": [
      "1. Cucina Creativa (o il tuo agente creativo) — sviluppi o carichi la ricetta. L'agente IA fornisce ricetta + scheda tecnica completa con tutti i campi professionali.",
      "2. ID Allergeni — identifica automaticamente gli allergeni per ricetta e li integra nella scheda; quando cambi un ingrediente, ricalcola all'istante.",
      "3. GastroIMG Gen+ — genera un'immagine di riferimento del piatto impiattato da includere nella scheda come guida visiva per il cuoco.",
      "4. Food Pairing AI + storytelling per la sala — la scheda include abbinamento consigliato e descrizione professionale per il briefing del team."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Schede Tecniche",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-tareas",
      "guia-restaurante-gastronomico"
    ],
    "testimonialQuote": "Documentare 28 piatti con scheda tecnica professionale ci richiedeva 2 settimane. Cucina Creativa fornisce già ogni scheda completa in pochi minuti: ingredienti, tecnica, allergeni automatici, costo e storytelling per la sala. Ora qualsiasi cuoco replica con coerenza e quando ispezionano abbiamo tutto tracciato.",
    "testimonialAuthor": "Carla Mendoza",
    "testimonialRole": "Capo cuoca, ristorante casual con 3 punti",
    "faqTitle": "Domande Frequenti sulle Schede Tecniche con IA",
    "faqs": [
      {
        "q": "Cosa include una scheda tecnica professionale?",
        "a": "Ingredienti con grammatura esatta, tecnica passo passo, allergeni automatici, food cost %, costo per porzione, conservazione, presentazione, abbinamento suggerito e descrizione per la sala."
      },
      {
        "q": "Come gestisce gli allergeni automaticamente?",
        "a": "ID Allergeni identifica gli allergeni per ingrediente e li integra nella scheda. Quando cambi un ingrediente, ricalcola all'istante e aggiorna le informazioni per la sala."
      },
      {
        "q": "Funziona per qualsiasi tipo di cucina?",
        "a": "Sì. Il flusso è lo stesso per cucina creativa, pasticceria, gelateria, cioccolateria, pizzeria, qualsiasi tipo di cucina nazionale o concetto."
      },
      {
        "q": "Genera un'immagine del piatto da includere nella scheda?",
        "a": "Sì. GastroIMG Gen+ genera un'immagine di riferimento. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva nella scheda la fai tu con il tuo piatto reale impiattato."
      },
      {
        "q": "Come mi aiuta con audit e certificazioni?",
        "a": "Ogni scheda tecnica è tracciabile: ingredienti, grammatura, allergeni, costo e tecnica. Pronte per audit, ISO 22000, BRC e certificazioni di sicurezza alimentare."
      }
    ],
    "ctaTitle": "Le tue schede tecniche professionali in pochi minuti.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "Schede Tecniche con IA: Allergeni, Costo e Storytelling",
      "description": "Suite IA per schede tecniche: allergeni automatici, costo integrato, foto dell'impiattamento e storytelling. Inizia oggi.",
      "keywords": "schede tecniche IA, scheda tecnica piatto, allergeni automatici, costo per porzione, scheda tecnica ristorante",
      "ogImage": "https://aichef.pro/og/use-cases/task-fichas-tecnicas-con-ia.jpg"
    },
    "personalizationTitle": "Personalizzato alla Tua Cucina dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con «Chi sono?»: racconti tipo di cucina, specialità e volume. La struttura della scheda tecnica si adatta al tuo concetto: ristorante casual, fine dining, pasticceria, gelateria, ecc.",
    "appsTitle": "Gli Agenti IA che Usi per le Schede Tecniche",
    "apps": [
      {
        "name": "Cucina Creativa",
        "description": "Ricette + scheda tecnica completa con tutti i campi.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Schede tecniche dolci con costo ora laboratorio.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Gelateria Creativa",
        "description": "Schede con bilanciamento tecnico di zuccheri, solidi e grassi.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione automatica degli allergeni per ricetta.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Conversor Ing",
        "description": "Convertitore automatico di pesi e misure.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Calcula Pax",
        "description": "Scalatura di ricette per banchetti ed eventi.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Dati sugli sprechi per processo integrati nella scheda.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamento suggerito da includere nella scheda.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Immagine di riferimento del piatto impiattato.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Gastro Lexicum",
        "description": "Tutor di definizioni tecniche per validare la terminologia.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Pro Prompts eBook",
        "description": "300+ prompt per schede tecniche e descrizioni.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per validare tecnica e ingredienti.",
        "category": "Fornitori Gastro"
      }
    ],
    "metrics": [
      {
        "value": "×20",
        "label": "velocità vs. scheda a mano"
      },
      {
        "value": "100 %",
        "label": "allergeni identificati automaticamente"
      },
      {
        "value": "ISO",
        "label": "schede pronte per audit 22000"
      },
      {
        "value": "12+",
        "label": "agenti per le tue schede tecniche"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "2 settimane per documentare 28 piatti",
        "Allergeni calcolati a mano (rischio legale)",
        "Storytelling improvvisato in sala",
        "Cambi di ingrediente senza aggiornare le schede",
        "Senza modello professionale standardizzato"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "28 piatti documentati in un giorno con modello professionale",
        "Allergeni automatici con ID Allergeni",
        "Storytelling professionale per il briefing di sala",
        "I cambi aggiornano scheda e allergeni all'istante",
        "Modello uniforme pronto per audit e certificazioni"
      ]
    },
    "galleryTitle": "Come Funzionano le Schede Tecniche con IA",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: scheda, binder, foto dell'impiattamento, tablet e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-document.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-binder.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-photo.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-tablet.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-fichas-tecnicas-team.jpg"
    ]
  },
  "task-foto-gastronomica-con-ia": {
    "h1": "Come Fare Fotografia Gastronomica con IA",
    "heroSubtitle": "Genera immagini di riferimento professionali del piatto prima di cucinare per validare impiattamento, palette e composizione. Dopo fai la foto definitiva del piatto reale con criterio chiaro dell'immagine obiettivo.",
    "heroTagline": "Immagine di riferimento prima, foto definitiva dopo",
    "badge": "Compito: Fotografia gastronomica",
    "painsTitle": "Quanto Costa la Fotografia Gastronomica Tradizionale",
    "pains": [
      "Sessioni di food styling senza immagine di riferimento chiara, iterazioni costose",
      "Senza criterio condiviso tra chef, fotografo e stylist su composizione e palette",
      "Il prodotto fresco si degrada durante la sessione, la foto non cattura il momento ottimale",
      "I cambi di menu richiedono una nuova sessione completa e costosa",
      "Le immagini per Instagram, Glovo, web e menu richiedono formati diversi",
      "Immagine industriale vs. immagine d'autore: criterio incoerente tra canali"
    ],
    "featuresTitle": "Come AI Chef Pro Risolve la Fotografia Gastronomica",
    "features": [
      {
        "title": "GastroIMG Gen+",
        "description": "Agente specializzato in fotografia gastronomica con IA: genera immagine di riferimento professionale del piatto.",
        "icon": "Image"
      },
      {
        "title": "Cucina Creativa con impiattamento",
        "description": "Ogni ricetta fornisce istruzioni di impiattamento professionale: composizione, palette, garnish, stoviglie, vista (zenitale, 3/4, frontale).",
        "icon": "Sparkles"
      },
      {
        "title": "Immagine come riferimento, non foto finale",
        "description": "L'immagine IA è la guida visiva: contrasto di palette, volume, texture, stoviglie. La foto definitiva della scheda tecnica la fai tu con il tuo piatto reale.",
        "icon": "BookOpen"
      },
      {
        "title": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico stabile per la fotografia gastronomica.",
        "icon": "Calendar"
      },
      {
        "title": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale e composizioni adattate al feed.",
        "icon": "Sparkles"
      },
      {
        "title": "MenuDish Local SEO",
        "description": "Immagini adattate a Glovo, Uber Eats, Just Eat e piattaforme con criterio professionale per più clic.",
        "icon": "BarChart3"
      },
      {
        "title": "Pro Prompts eBook",
        "description": "300+ prompt professionali per fotografia gastronomica: stile, palette, composizione, mood.",
        "icon": "CheckSquare"
      },
      {
        "title": "Varianti e prelavorazioni",
        "description": "GastroIMG genera immagini di varianti: impiattamenti alternativi, prelavorazioni, mise en place, non solo piatto finale.",
        "icon": "Image"
      },
      {
        "title": "BlogPost SEO Gen+",
        "description": "Articoli SEO su tecnica fotografica con immagini di riferimento per traffico organico.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Come Fare Fotografia Gastronomica in 4 Passi",
    "workflow": [
      "1. Cucina Creativa — sviluppi il piatto. L'agente IA fornisce ricetta + scheda tecnica + istruzioni di impiattamento professionale (composizione, palette, stoviglie, vista).",
      "2. GastroIMG Gen+ — generi immagine di riferimento professionale con prompt ottimizzato: palette calda, stoviglie rustiche, vista zenitale, microgreens. Iteri fino ad avere l'immagine obiettivo chiara.",
      "3. Cucini il piatto reale con l'immagine di riferimento davanti: stesso impiattamento, palette, garnish. La foto definitiva della scheda tecnica e del menu la fai tu con il tuo piatto impiattato reale.",
      "4. InstaFlow AI Pro + MenuDish + Pinterest Pins Gen — adatti l'immagine finale a ogni canale (Instagram, Glovo, web, menu) con criterio professionale."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Fotografia Gastronomica",
    "productIds": [
      "pro-prompts-ebook",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-tareas",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "GastroIMG Gen+ mi ha cambiato il flusso di fotografia. Prima facevo sessioni di food styling senza criterio chiaro, ora genero l'immagine di riferimento professionale con IA, valido palette e composizione con il team, e dopo faccio la foto definitiva con il mio piatto reale. Le sessioni calano del 70% in tempo e la consistenza visiva di Instagram + Glovo + web è ora professionale.",
    "testimonialAuthor": "Carmen Vera",
    "testimonialRole": "Chef e proprietaria, ristorante con presenza digitale forte",
    "faqTitle": "Domande Frequenti sulla Fotografia Gastronomica con IA",
    "faqs": [
      {
        "q": "L'immagine IA è la foto definitiva del piatto?",
        "a": "No. L'immagine IA è di riferimento visivo per validare impiattamento, palette, stoviglie e composizione prima di cucinare. La foto definitiva della scheda tecnica, del menu o della scheda tecnica la fai tu con il tuo piatto reale impiattato."
      },
      {
        "q": "Serve per qualsiasi stile di cucina?",
        "a": "Sì. GastroIMG Gen+ adatta lo stile: alta cucina con minimalismo, casual con calore, mediterraneo, asiatico, latinoamericano, fine dining premium."
      },
      {
        "q": "Copre formati per Instagram, Glovo, web e menu?",
        "a": "Sì. L'immagine base si adatta a 1:1 (Instagram), 4:5 (feed), 16:9 (menu digitale), 9:16 (Stories), 4:3 (Glovo, Uber Eats) con criterio professionale."
      },
      {
        "q": "Genera varianti e prelavorazioni, non solo piatto finale?",
        "a": "Sì. GastroIMG Gen+ genera immagini di varianti: impiattamenti alternativi, mise en place, prelavorazioni, ingredienti grezzi, non solo piatto finale. Utile per storytelling di processo."
      },
      {
        "q": "Come mi aiuta con l'acquisizione locale nel delivery?",
        "a": "MenuDish Local SEO + GastroIMG Gen+ generano immagini professionali per Glovo, Uber Eats, Just Eat con criterio che aumenta il CTR. Migliore foto = più clic e miglior ranking."
      }
    ],
    "ctaTitle": "La tua fotografia gastronomica con criterio professionale.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "Come Fare Fotografia Gastronomica con IA: Immagine di Riferimento e Foto Finale | AI Chef Pro",
      "description": "Suite di IA per fotografia gastronomica: GastroIMG Gen+ genera immagine di riferimento, poi fai la foto definitiva con il tuo piatto reale. Inizia oggi.",
      "keywords": "fotografia gastronomica IA, GastroIMG Gen+, food photography IA, immagine riferimento piatto, foto piatto delivery",
      "ogImage": "https://aichef.pro/og/use-cases/task-foto-gastronomica-con-ia.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Stile dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con «Chi sono?»: racconti stile di cucina, palette del brand, stoviglie e canali prioritari (Instagram, Glovo, web, menu). GastroIMG Gen+ adatta lo stile visivo al tuo brand.",
    "appsTitle": "Gli Agenti IA che Usi per Fotografia Gastronomica",
    "apps": [
      {
        "name": "GastroIMG Gen+",
        "description": "Agente specializzato in fotografia gastronomica IA.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Cucina Creativa",
        "description": "Istruzioni di impiattamento professionale per ogni ricetta.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Impiattamento di dolci con tecnica francese.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Gelateria Creativa",
        "description": "Impiattamento di gelati e semifreddi con tecnica.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Pro Prompts eBook",
        "description": "300+ prompt professionali per fotografia gastronomica.",
        "category": "Contenuti e Social"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con calendario editoriale e formati adattati.",
        "category": "Contenuti e Social"
      },
      {
        "name": "MenuDish Local SEO",
        "description": "Immagini per Glovo, Uber Eats, Just Eat ottimizzate.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pinterest Pins Gen",
        "description": "Pinterest cattura traffico organico stabile.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Articoli SEO con immagini di riferimento.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Gastro Calendar",
        "description": "Pianificazione di sessioni per stagione.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca su tendenze visive di riferimenti.",
        "category": "Modelli IA + LLM"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching per leadership creativa.",
        "category": "Strumenti e Utility"
      }
    ],
    "metrics": [
      {
        "value": "−70 %",
        "label": "tempo di sessioni food styling"
      },
      {
        "value": "×3",
        "label": "engagement Instagram con GastroIMG"
      },
      {
        "value": "+CTR",
        "label": "migliore foto = più clic nel delivery"
      },
      {
        "value": "12+",
        "label": "agenti per fotografia gastronomica"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Sessioni food styling senza immagine di riferimento chiara",
        "Senza criterio condiviso tra chef e fotografo",
        "Cambi di menu richiedono nuova sessione completa",
        "Immagine incoerente tra Instagram, Glovo e web",
        "Senza varianti né prelavorazioni per storytelling"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "GastroIMG Gen+ genera immagine di riferimento professionale",
        "Criterio condiviso validato prima di cucinare",
        "Cambi di menu: nuova immagine IA in minuti",
        "Immagine coerente tra tutti i canali",
        "Varianti e prelavorazioni per storytelling completo"
      ]
    },
    "galleryTitle": "Come Funziona la Fotografia Gastronomica con IA",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: hero, piatto, camera, strumenti e attrezzatura. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-plato.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-camera.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-tools.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-comparison.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-foto-gastronomica-team.jpg"
    ]
  },
  "task-maridajes-con-ia": {
    "h1": "Come Validare gli Abbinamenti con l'IA",
    "heroSubtitle": "Valida abbinamenti con base scientifica: analisi di acidità, tannini, struttura, intensità e armonia. Suite di agenti di IA gastronomica con tecnica sommelier professionale.",
    "heroTagline": "Abbinamenti scientifici in minuti per qualsiasi carta",
    "badge": "Compito: Abbinamenti professionali",
    "painsTitle": "Quanto Costa Fare Abbinamenti a Mano",
    "pains": [
      "Abbinamenti consigliati per intuizione senza base scientifica fondata",
      "Personale di sala senza formazione costante per comunicare abbinamenti con criterio",
      "Cambiamenti nel menù o in cantina senza rivalidare gli abbinamenti (la raccomandazione diventa obsoleta)",
      "Abbinamenti solo con vino: mancano opzioni con birra, sake, kombucha, tè e senza alcol",
      "Storytelling di ogni abbinamento improvvisato, senza profondità tecnica",
      "Eventi privati con abbinamenti ad hoc senza proposta professionale chiara"
    ],
    "featuresTitle": "Come AI Chef Pro Risolve gli Abbinamenti",
    "features": [
      {
        "title": "Food Pairing AI",
        "description": "Agente specializzato in abbinamenti con base scientifica: analisi di acidità, tannini, struttura, intensità, armonia e contrasto.",
        "icon": "Wine"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Selezione concreta di cantina per ogni abbinamento con criterio sommelier professionale: vini, sake, birre, spumanti.",
        "icon": "Sparkles"
      },
      {
        "title": "Storytelling professionale",
        "description": "Ogni abbinamento include descrizione tecnica affinché il personale di sala lo comunichi con base professionale.",
        "icon": "BookOpen"
      },
      {
        "title": "Food cost degli abbinamenti",
        "description": "Costo reale per calice, food cost del vino e proposta di prezzo per l'abbinamento del menù degustazione.",
        "icon": "Calculator"
      },
      {
        "title": "Abbinamenti senza alcol",
        "description": "Proposte con kombucha, tè, caffè, acqua tonica fatta in casa per clienti che non consumano alcol.",
        "icon": "Sparkles"
      },
      {
        "title": "Pack APPCC bodega",
        "description": "Tracciabilità di cantina e temperature di servizio per tipo di vino.",
        "icon": "CheckSquare"
      },
      {
        "title": "Gastro Calendar",
        "description": "Degustazioni ed eventi con abbinamenti, lanci di stagione.",
        "icon": "Calendar"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Immagine di riferimento dell'abbinamento (calice + piatto) per Instagram e menù.",
        "icon": "Image"
      },
      {
        "title": "Gastro Lexicum",
        "description": "Tutor di definizioni tecniche: enologia, vinificazione, terroir, denominazioni.",
        "icon": "BookOpen"
      }
    ],
    "workflowTitle": "Come Validare gli Abbinamenti in 4 Passi",
    "workflow": [
      "1. Food Pairing AI — carichi il piatto con tecnica e ingredienti. L'IA analizza acidità, tannini, intensità, struttura e propone tipo di vino con base scientifica.",
      "2. Bar & Lounge AI+ — propone selezione concreta della tua cantina: annate, produttori, calice o bottiglia. Per opzioni senza alcol propone kombucha, tè o tonic fatti in casa.",
      "3. Storytelling per la sala — ogni abbinamento genera descrizione professionale per il briefing del team e comunicazione al cliente.",
      "4. Kit de Escandallos Pro — calcoli il costo reale per calice, food cost del vino e proposta di prezzo per l'abbinamento."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Abbinamenti",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Food Pairing AI mi ha cambiato il modo di chiudere gli abbinamenti. Ogni piatto del menù degustazione ora ha un abbinamento fondato scientificamente che il mio team di sala comunica con base professionale. Abbiamo aumentato il margine di 6 punti in cantina e i clienti ricorrenti premium sono cresciuti del 35% in 6 mesi.",
    "testimonialAuthor": "Eduardo Lara",
    "testimonialRole": "Head Sommelier, ristorante con 1 stella Michelin",
    "faqTitle": "Domande Frequenti sugli Abbinamenti con l'IA",
    "faqs": [
      {
        "q": "Serve per qualsiasi stile di ristorante?",
        "a": "Sì. Food Pairing AI copre dal casual al fine dining Michelin, passando per gastropub, enoteche e ristoranti etnici."
      },
      {
        "q": "Ha una base scientifica reale?",
        "a": "Sì. Ragiona come un sommelier professionale con fondamento tecnico di enologia e bromatologia: acidità, tannini, struttura, intensità, armonia e contrasto."
      },
      {
        "q": "Copre abbinamenti senza alcol?",
        "a": "Sì. Propone kombucha, tè, caffè, tonic fatti in casa e bevande funzionali con criterio professionale per clienti che non consumano alcol."
      },
      {
        "q": "Copre abbinamenti con birra, sake, spumanti?",
        "a": "Sì. Bar & Lounge AI+ copre tutto lo spettro del banco: vini, sake, birre artigianali, spumanti e bevande spiritose."
      },
      {
        "q": "Genera contenuto visivo dell'abbinamento per Instagram?",
        "a": "Sì. GastroIMG Gen+ genera immagine di riferimento. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo calice e piatto reale."
      }
    ],
    "ctaTitle": "I tuoi abbinamenti con base scientifica in minuti.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "Abbinamenti con IA: Vini, Sake e Senza Alcol | AI Chef Pro",
      "description": "Suite di IA per abbinamenti: Food Pairing AI con base scientifica, selezione di cantina, storytelling per la sala. Inizia oggi.",
      "keywords": "abbinamenti con IA, food pairing IA, abbinamento vino piatto, IA sommelier, abbinamenti senza alcol IA, abbinamento scientifico",
      "ogImage": "https://aichef.pro/og/use-cases/task-maridajes-con-ia.jpg"
    },
    "personalizationTitle": "Personalizzato sulla Tua Cantina dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con «Chi sono?»: racconti tipo di ristorante, dimensione della cantina, specialità e livello. Ogni abbinamento si adatta al tuo inventario reale, non a una cantina generica.",
    "appsTitle": "Gli Agenti IA che Usi per gli Abbinamenti",
    "apps": [
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con base scientifica per ogni piatto.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Selezione concreta di cantina con criterio sommelier.",
        "category": "Concetti di Business"
      },
      {
        "name": "Cucina Creativa",
        "description": "Storytelling professionale dell'abbinamento per la sala.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Gastro Lexicum",
        "description": "Tutor di definizioni di enologia e vinificazione.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi per stappatura fallita integrati.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione dei solfiti per clienti sensibili.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Immagine di riferimento dell'abbinamento.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca approfondita di cantine e annate.",
        "category": "Modelli IA + LLM"
      },
      {
        "name": "Gastro Calendar",
        "description": "Degustazioni ed eventi con abbinamenti.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Articoli SEO su abbinamenti e cantine.",
        "category": "Contenuti e Social"
      },
      {
        "name": "InstaFlow AI Pro",
        "description": "Instagram con abbinamenti in evidenza.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Pro Prompts eBook",
        "description": "300+ prompt per descrizioni di abbinamenti.",
        "category": "Contenuti e Social"
      }
    ],
    "metrics": [
      {
        "value": "×10",
        "label": "velocità vs. validazione manuale"
      },
      {
        "value": "+6 pp",
        "label": "margine dopo il food cost della cantina"
      },
      {
        "value": "+35 %",
        "label": "clienti ricorrenti premium"
      },
      {
        "value": "12+",
        "label": "agenti per abbinamenti"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Abbinamenti per intuizione senza base scientifica",
        "Senza opzioni senza alcol professionali",
        "Personale di sala senza formazione documentata",
        "Cambiamenti in cantina senza rivalidare gli abbinamenti",
        "Abbinamenti per eventi privati ad hoc"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Abbinamenti con base scientifica di Food Pairing AI",
        "Opzioni con kombucha, tè, tonic fatti in casa",
        "Briefing giornaliero al team con storytelling professionale",
        "Cambiamenti in cantina rivalidano gli abbinamenti all'istante",
        "Abbinamenti per eventi chiusi con proposta professionale"
      ]
    },
    "galleryTitle": "Come Funziona la Validazione degli Abbinamenti con l'IA",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: calici, piatti, note, cantina e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-glasses.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-plate.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-notes.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-bottles.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-maridajes-team.jpg"
    ]
  },
  "task-menu-degustacion-con-ia": {
    "h1": "Come Progettare un Menù Degustazione con IA",
    "heroSubtitle": "Progetta menù degustazione con sequenza coerente, food cost totale validato, abbinamenti scientifici e storytelling per la sala con una suite di agenti di IA gastronomica specializzati in alta cucina.",
    "heroTagline": "Menù degustazione professionale in ore, non in settimane",
    "badge": "Attività: Menù degustazione",
    "painsTitle": "Quanto Costa Progettare un Menù Degustazione a Mano",
    "pains": [
      "Una settimana di iterazioni per una sequenza di 7-10 portate coerente senza saturazione",
      "Senza food cost totale validato per menù, proposta a prezzo incerto",
      "Abbinamenti con vino proposti senza base scientifica fondata",
      "Storytelling di ogni portata improvvisato, team di sala senza formazione costante",
      "Cambi di portata richiedono rifare il food cost completo a mano",
      "Mancanza di criterio per bilanciare texture, temperatura, intensità e tecnica tra le portate"
    ],
    "featuresTitle": "Come AI Chef Pro Risolve il Menù Degustazione",
    "features": [
      {
        "title": "Cucina Creativa con sequenza tecnica",
        "description": "Ragiona la sequenza completa: antipasto leggero, vegetale, pesce, carne, palate cleanser, dessert. Bilanciamento di texture, temperatura e intensità.",
        "icon": "Sparkles"
      },
      {
        "title": "Food Pairing AI",
        "description": "Abbinamenti con base scientifica per ogni portata: analisi di acidità, tannini, struttura, intensità e armonia con la cucina.",
        "icon": "Wine"
      },
      {
        "title": "Food cost totale integrato",
        "description": "CSV con food cost di ogni portata + totale del menù; Kit de Escandallos Pro valida costo per coperto e proposta di prezzo.",
        "icon": "Calculator"
      },
      {
        "title": "Storytelling per la sala",
        "description": "Descrizione di ogni portata con tecnica, prodotto, fornitore e storia; il team di sala lo racconta con professionalità.",
        "icon": "BookOpen"
      },
      {
        "title": "Bar & Lounge AI+",
        "description": "Selezione di vini al calice per l'abbinamento del menù degustazione con criterio sommelier professionale.",
        "icon": "Sparkles"
      },
      {
        "title": "Kit de Tareas Restaurante",
        "description": "Template per la mise en place di ogni portata, sequenza di servizio e coordinamento con la sala.",
        "icon": "CheckSquare"
      },
      {
        "title": "GastroIMG Gen+",
        "description": "Immagine di riferimento di ogni portata per visualizzare la sequenza prima di provare e validare la coerenza visiva.",
        "icon": "Image"
      },
      {
        "title": "Gastro Calendar",
        "description": "Menù degustazione stagionali ed eventi privati con pianificazione professionale.",
        "icon": "Calendar"
      },
      {
        "title": "Calcula Pax",
        "description": "Scalatura di ricette per banchetti ed eventi privati senza perdere precisione.",
        "icon": "BarChart3"
      }
    ],
    "workflowTitle": "Come Progettare un Menù Degustazione in 5 Passi",
    "workflow": [
      "1. Cucina Creativa — definisci il tema (stagione, prodotto locale, occasione) e l'agente IA consegna una sequenza di 7-10 portate con bilanciamento tecnico (texture, intensità, temperatura).",
      "2. Ogni portata con ricetta + food cost CSV individuale + storytelling per la sala con tecnica, prodotto e fornitore.",
      "3. Food Pairing AI — per ogni portata valida l'abbinamento con vino o sake su base scientifica. Bar & Lounge AI+ propone una selezione concreta di cantina.",
      "4. Kit de Escandallos Pro — carichi i CSV individuali, l'Excel calcola il costo totale per coperto, la proposta di prezzo e il margine validato.",
      "5. Calcula Pax — se il menù è per evento privato o banchetto (50, 100, 300 coperti), scala le ricette e ricalcola il costo per la proposta commerciale."
    ],
    "productsTitle": "Template e Kit Consigliati per Menù Degustazione",
    "productIds": [
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "guia-restaurante-gastronomico",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Cucina Creativa + Food Pairing AI ci hanno cambiato lo sviluppo dei menù degustazione. La sequenza di 9 portate esce già con bilanciamento tecnico documentato, gli abbinamenti con vini al calice sono coerenti e il food cost totale con Kit de Escandallos Pro ci dà un margine validato. Quello che prima era una settimana ora è un giorno.",
    "testimonialAuthor": "Joan Mestre",
    "testimonialRole": "Chef esecutivo, ristorante con 1 stella Michelin",
    "faqTitle": "Domande Frequenti sul Menù Degustazione con IA",
    "faqs": [
      {
        "q": "Funziona per Michelin, ristorante d'autore o casual con menù degustazione?",
        "a": "Per tutti e tre. Cucina Creativa ragiona come uno chef professionista: bilanciamento tecnico, sequenza coerente, narrativa del menù adattata al livello."
      },
      {
        "q": "Come mi aiuta con la coerenza tra le portate?",
        "a": "Cucina Creativa ragiona l'intera sequenza con bilanciamento di texture (croccante, setosa, cremosa), temperatura (freddo, ambiente, caldo), intensità (da delicata a potente) e tecnica (cottura, fermentazione, affumicatura)."
      },
      {
        "q": "Copre abbinamenti con vini al calice per il menù?",
        "a": "Sì. Food Pairing AI valida ogni abbinamento su base scientifica; Bar & Lounge AI+ propone una selezione concreta di cantina e storytelling per la sala."
      },
      {
        "q": "Genera un'immagine di riferimento per ogni portata?",
        "a": "Sì. GastroIMG Gen+ genera un'immagine di riferimento per visualizzare la coerenza visiva del menù. Ricorda che l'immagine IA è di riferimento visivo: la foto definitiva la fai tu con il tuo piatto impiattato reale."
      },
      {
        "q": "È scalabile a banchetti ed eventi privati?",
        "a": "Sì. Calcula Pax scala il menù a qualsiasi numero di commensali; Kit de Escandallos Pro ricalcola il costo per coperto e la proposta economica al cliente."
      }
    ],
    "ctaTitle": "Il tuo menù degustazione professionale in ore, non in settimane.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "Menù Degustazione con IA: Sequenza, Food Cost, Abbinamenti",
      "description": "Suite di IA per menù degustazione: sequenza tecnica, food cost totale, abbinamenti scientifici e storytelling. Inizia oggi.",
      "keywords": "menù degustazione IA, progettare menù degustazione, sequenza portate, abbinamenti menù, food cost menù degustazione, alta cucina IA",
      "ogImage": "https://aichef.pro/og/use-cases/task-menu-degustacion-con-ia.jpg"
    },
    "personalizationTitle": "Personalizzato al Tuo Ristorante dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con «Chi sono?»: racconti il tipo di ristorante (gastronomico Michelin, fine dining, casual con menù degustazione, ristorante d'autore), numero di portate preferito, mercato e stile di cucina. Ogni agente risponde adattato al tuo livello.",
    "appsTitle": "Gli Agenti IA che Usi per il Menù Degustazione",
    "apps": [
      {
        "name": "Cucina Creativa",
        "description": "Ragiona la sequenza tecnica del menù degustazione con bilanciamento.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Food Pairing AI",
        "description": "Abbinamenti con base scientifica per ogni portata.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Bar & Lounge AI+",
        "description": "Selezione di vini al calice con criterio sommelier.",
        "category": "Concetti di Business"
      },
      {
        "name": "Pasticceria Creativa",
        "description": "Per dessert e palate cleanser del menù.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Sosa Ingredients AI",
        "description": "Catalogo Sosa per texture e tecnica avanzata.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "tSpoonLab Agent",
        "description": "Catalogo tSpoonLab per applicazioni avanzate.",
        "category": "Fornitori Gastro"
      },
      {
        "name": "Sprechi GenCal",
        "description": "Sprechi per portata integrati al food cost totale.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Calcula Pax",
        "description": "Scalatura per banchetti ed eventi privati.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione degli allergeni per portata per la sala.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Immagine di riferimento di ogni portata del menù.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Gastro Calendar",
        "description": "Menù degustazione stagionali ed eventi privati.",
        "category": "Contenuti e Social"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching per leadership e gestione del servizio degustazione.",
        "category": "Strumenti e Utility"
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "velocità vs. processo manuale"
      },
      {
        "value": "+8 pp",
        "label": "margine dopo aver calcolato il food cost del menù"
      },
      {
        "value": "×3",
        "label": "velocità abbinamenti con sommelier"
      },
      {
        "value": "12+",
        "label": "agenti per il tuo menù degustazione"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Una settimana di iterazioni per ogni nuovo menù",
        "Sequenza improvvisata senza bilanciamento tecnico",
        "Abbinamenti senza base scientifica",
        "Food cost totale con proposta a prezzo incerto",
        "Storytelling improvvisato, team di sala senza formazione"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Menù degustazione chiuso in un giorno con sequenza coerente",
        "Bilanciamento tecnico documentato tra le portate",
        "Abbinamenti con Food Pairing AI fondati",
        "Food cost totale validato e proposta chiara al cliente",
        "Storytelling professionale per il briefing di sala"
      ]
    },
    "galleryTitle": "Come Funziona la Progettazione del Menù Degustazione con IA",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: sequenza, portate, abbinamenti, mise en place e team. Immagini generate con IA come riferimento visivo del concetto.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-pase.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-secuencia.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-pairing.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-mise.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-menu-degustacion-team.jpg"
    ]
  },
  "task-reducir-mermas-con-ia": {
    "h1": "Come Ridurre gli Sprechi in Cucina con l'IA",
    "heroSubtitle": "Identifica, misura e riduci gli sprechi per processo (disosso, formatura, cottura al forno, vetrina, delivery) con dati reali integrati nella scheda tecnica. Suite di agenti di IA gastronomica specializzati in operativa zero-waste.",
    "heroTagline": "Sprechi ridotti con dati reali per processo",
    "badge": "Compito: Riduzione degli sprechi",
    "painsTitle": "Quanto Costano gli Sprechi Senza Controllo",
    "pains": [
      "Sprechi stimati a occhio (15-30% in alcuni tagli), non dati reali per processo",
      "Mancanza di dati per tipo di cucina (gelateria, panificazione, griglia, sushi hanno sprechi diversi)",
      "Senza sistema per riutilizzare rifili e bucce (brodi, aceti infusi, disidratati)",
      "Quando un fornitore cambia, gli sprechi cambiano senza ricalcolare il margine",
      "Team senza formazione costante sulla tecnica di recupero professionale",
      "Senza tracciabilità per audit di sostenibilità e certificazioni zero-waste"
    ],
    "featuresTitle": "Come AI Chef Pro Riduce gli Sprechi",
    "features": [
      {
        "title": "Sprechi GenCal",
        "description": "Dati precisi sugli sprechi per processo per tipo di cucina: disosso, dry-aging, formatura, cottura al forno, vetrina, delivery.",
        "icon": "BarChart3"
      },
      {
        "title": "Cucina Creativa",
        "description": "Ragiona tecniche di riutilizzo: rifili in brodi, bucce in aceti infusi, avanzi in disidratati con criterio professionale.",
        "icon": "Sparkles"
      },
      {
        "title": "Sprechi nella scheda tecnica",
        "description": "Sprechi reali per processo integrati nella scheda tecnica del Kit de Escandallos Pro: il costo per piatto riflette lo spreco reale, non stimato.",
        "icon": "Calculator"
      },
      {
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modelli con procedure di recupero per stazione, controllo settimanale degli sprechi, formazione del team.",
        "icon": "CheckSquare"
      },
      {
        "title": "Pack APPCC tracciabile",
        "description": "Tracciabilità degli sprechi per processo per audit di sostenibilità e certificazioni zero-waste.",
        "icon": "ShieldCheck"
      },
      {
        "title": "Fermentus Con AI+",
        "description": "Fermenti per riutilizzare prodotto: crauti con avanzi di cavolo, kombucha con bucce di frutta, garum con lische di pesce.",
        "icon": "Beaker"
      },
      {
        "title": "VegChef Plant-Based",
        "description": "Per riutilizzo professionale vegetale: recupero integrale della verdura, tecnica stems-to-roots.",
        "icon": "Sparkles"
      },
      {
        "title": "Calcula Pax",
        "description": "Acquisti adeguati al volume reale dell'evento o del servizio per ridurre gli avanzi alla fonte.",
        "icon": "BarChart3"
      },
      {
        "title": "Gastro Calendar",
        "description": "Pianificazione della produzione adeguata alla domanda storica per ridurre la sovrapproduzione.",
        "icon": "Calendar"
      }
    ],
    "workflowTitle": "Come Ridurre gli Sprechi in 4 Passi",
    "workflow": [
      "1. Sprechi GenCal — l'agente IA fornisce dati reali per processo per tipo di cucina (disosso carne, formatura pasta, cottura al forno pane, vetrina gelato, delivery pizza). Carichi il dato reale della tua operazione.",
      "2. Cucina Creativa + Fermentus Con AI+ — sviluppi tecniche di riutilizzo: rifili in brodi, bucce in aceti, avanzi in disidratati, eccedenze in fermenti.",
      "3. Kit de Escandallos Pro — la scheda tecnica riflette lo spreco reale, non stimato. Il costo per piatto sale leggermente ma riflette il costo vero, evitando sorprese nel margine.",
      "4. Calcula Pax + Gastro Calendar — acquisti adeguati al volume reale del servizio o dell'evento per ridurre gli avanzi alla fonte, non solo processare gli sprechi successivamente."
    ],
    "productsTitle": "Modelli e Kit Consigliati per Ridurre gli Sprechi",
    "productIds": [
      "kit-escandallos",
      "kit-inventario",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-tareas",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Sprechi GenCal + Cucina Creativa ci hanno cambiato l'operatività. Siamo passati da sprechi stimati (assumevamo 12-15%) a dati reali del 22-28% in alcuni processi. Abbiamo riorganizzato disosso e recupero con tecnica documentata e ridotto gli sprechi del 35% in 4 mesi. La scheda tecnica ora riflette il costo reale, non quello ideale.",
    "testimonialAuthor": "Sofía Cano",
    "testimonialRole": "Sous chef, ristorante casual con impegno zero-waste",
    "faqTitle": "Domande Frequenti su Ridurre gli Sprechi con l'IA",
    "faqs": [
      {
        "q": "Funziona per qualsiasi tipo di cucina?",
        "a": "Sì. Sprechi GenCal copre dati per processo per tipo di cucina: griglia, sushi, pasta, pane, gelato, cioccolato, salsa, marinatura. Ogni cucina ha sprechi diversi."
      },
      {
        "q": "Come integro gli sprechi reali nella scheda tecnica?",
        "a": "Kit de Escandallos Pro ha un campo per lo spreco per ingrediente e per processo. Sprechi GenCal fornisce i dati reali affinché il costo per piatto rifletta la realtà."
      },
      {
        "q": "Copre tecniche di riutilizzo professionale?",
        "a": "Sì. Cucina Creativa fornisce tecniche di recupero: stems-to-roots vegetale, rifili in brodi, bucce in aceti, fermenti con avanzi. Fermentus approfondisce tecniche avanzate."
      },
      {
        "q": "Genera tracciabilità per certificazioni zero-waste?",
        "a": "Sì. Pack APPCC + Sprechi GenCal forniscono tracciabilità documentata per audit di sostenibilità e certificazioni zero-waste o B-Corp."
      },
      {
        "q": "Come mi aiuta con acquisti adeguati?",
        "a": "Calcula Pax + Gastro Calendar pianificano produzione e acquisti adeguati al volume reale del servizio per ridurre gli avanzi alla fonte."
      }
    ],
    "ctaTitle": "La tua cucina con sprechi ridotti e dati reali.",
    "ctaSubtitle": "Inizia con l'onboarding di 2 minuti. Piano Membro a 10 € al mese con 10.000 crediti.",
    "seo": {
      "title": "Come Ridurre gli Sprechi in Cucina con l'IA: Dati Reali e Riutilizzo | AI Chef Pro",
      "description": "Suite di IA per ridurre gli sprechi: Sprechi GenCal con dati reali, riutilizzo professionale, scheda tecnica tracciabile. Inizia oggi.",
      "keywords": "ridurre sprechi ristorante, sprechi con IA, food waste IA, zero waste cucina, sprechi laboratorio, ridurre scarti",
      "ogImage": "https://aichef.pro/og/use-cases/task-reducir-mermas-con-ia.jpg"
    },
    "personalizationTitle": "Personalizzato alla Tua Cucina dal Primo Minuto",
    "personalizationBody": "AI Chef Pro parte con «Chi sono?»: racconti tipo di cucina e volume. Sprechi GenCal fornisce dati per processo adattati al tuo concept: griglia, sushi, pasta, pane, gelato, cioccolato.",
    "appsTitle": "Gli Agenti IA che Usi per Ridurre gli Sprechi",
    "apps": [
      {
        "name": "Sprechi GenCal",
        "description": "Dati reali sugli sprechi per processo per tipo di cucina.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Cucina Creativa",
        "description": "Tecniche di riutilizzo professionale di rifili e avanzi.",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Fermentus Con AI+",
        "description": "Fermenti per riutilizzare avanzi (crauti, kombucha, garum).",
        "category": "Creatività Culinaria"
      },
      {
        "name": "VegChef Plant-Based",
        "description": "Recupero integrale della verdura (stems-to-roots).",
        "category": "Creatività Culinaria"
      },
      {
        "name": "Calcula Pax",
        "description": "Acquisti adeguati al volume reale del servizio.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Conversor Ing",
        "description": "Convertitore di pesi e misure per precisione.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "ID Allergeni",
        "description": "Identificazione nei prodotti riutilizzati.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Gastro Calendar",
        "description": "Pianificazione della produzione adeguata alla domanda storica.",
        "category": "Contenuti e Social"
      },
      {
        "name": "BlogPost SEO Gen+",
        "description": "Articoli SEO sulla sostenibilità per attrarre traffico.",
        "category": "Contenuti e Social"
      },
      {
        "name": "GastroIMG Gen+",
        "description": "Immagine di riferimento di piatti zero-waste.",
        "category": "Gastro Conoscenza"
      },
      {
        "name": "Mental Coach",
        "description": "Coaching per la leadership del team nello zero-waste.",
        "category": "Strumenti e Utility"
      },
      {
        "name": "Sonar Deep Research",
        "description": "Ricerca su tecniche zero-waste di riferimenti.",
        "category": "Modelli IA + LLM"
      }
    ],
    "metrics": [
      {
        "value": "−35 %",
        "label": "sprechi in 4 mesi"
      },
      {
        "value": "+4 pp",
        "label": "margine dopo aver integrato gli sprechi reali"
      },
      {
        "value": "×3",
        "label": "velocità vs. stima manuale"
      },
      {
        "value": "12+",
        "label": "agenti per ridurre gli sprechi"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Senza AI Chef Pro",
      "beforeItems": [
        "Sprechi stimati a occhio, scheda tecnica con costo sottostimato",
        "Senza tecnica documentata di riutilizzo",
        "Acquisti generici senza adeguamento al volume reale",
        "Team senza formazione sul recupero professionale",
        "Senza tracciabilità per audit di sostenibilità"
      ],
      "afterTitle": "Con AI Chef Pro",
      "afterItems": [
        "Sprechi reali documentati per processo",
        "Tecniche di riutilizzo con Cucina Creativa + Fermentus",
        "Acquisti adeguati al volume reale con Calcula Pax",
        "Briefing al team con tecnica documentata",
        "Tracciabilità HACCP per audit zero-waste"
      ]
    },
    "galleryTitle": "Come Funziona la Riduzione degli Sprechi con l'IA",
    "gallerySubtitle": "Quello che coordinerai con AI Chef Pro: pesatura, tracking, organizzazione, riutilizzo e team. Immagini generate con IA come riferimento visivo del concept.",
    "galleryImages": [
      "/lovable-uploads/ai-gallery/use-case-task-mermas-hero.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-scale.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-tracking.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-bins.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-recovery.jpg",
      "/lovable-uploads/ai-gallery/use-case-task-mermas-team.jpg"
    ]
  }
};
