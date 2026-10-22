import type { OfferCopy, PageCopy, ParityLang } from './types';

function offers(labels: [string, string, string, string, string], popular: string): OfferCopy[] {
  const [talk, workshop, day, program, consult] = labels;
  return [
    {
      name: talk,
      amount: 990,
      priceLabel: '990 €',
      meta: '90–120 min · up to 200 people',
      detail: 'A conference for a team, a school or an event. John shows the suite on real kitchen tasks.',
    },
    {
      name: workshop,
      amount: 1490,
      priceLabel: '1.490 €',
      meta: '4 hours · 12–25 people',
      detail: 'Hands-on: costing, allergens or the menu, on the recipes the team already cooks.',
    },
    {
      name: day,
      amount: 2490,
      priceLabel: '2.490 €',
      meta: '8 hours · 10–20 people',
      detail: popular,
      popular: true,
    },
    {
      name: program,
      amount: 4990,
      priceLabel: '4.990 €',
      meta: '16–24 hours · up to 30 people',
      detail: 'Several sessions for a school, a group or a brigade that needs the same method.',
    },
    {
      name: consult,
      priceLabel: 'from 4.990 €',
      meta: '2–5 days · at your kitchen',
      detail: 'In-house consulting. The quote covers the days; travel and lodging are separate.',
    },
  ];
}

const priceNote =
  'Base prices for peninsular Spain. VAT excluded. Travel and lodging are quoted for the location. Other countries on request. FUNDAE is a Spanish funded-training scheme and is not part of this offer outside Spain.';

export const TRAINING: Record<ParityLang, PageCopy> = {
  en: {
    title: 'In-person AI training for restaurants | AI Chef Pro',
    description:
      'John Guerrero travels to your kitchen for an AI session: conference from 990 €, workshop 1,490 €, full day 2,490 €. Prices are euro, VAT excluded, base for peninsular Spain. Travel quoted.',
    keywords: 'in-person AI training restaurants, restaurant AI workshop, chef AI course, hospitality AI training',
    eyebrow: 'In-person training',
    h1: 'AI training in your kitchen, with the chef who built the suite',
    lead: 'John Guerrero runs the session. Prices below are the ones published for peninsular Spain, in euro, VAT excluded.',
    answerLabel: 'Direct answer',
    answer:
      'Yes. John travels to the restaurant. A conference is 990 € (90–120 minutes, up to 200 people), a 4-hour workshop is 1,490 € (12–25 people), a full day is 2,490 € (10–20 people), a 16–24 hour program is 4,990 €, and in-house consulting starts at 4,990 € for 2–5 days. VAT excluded. Travel and lodging are extra. These are base prices for peninsular Spain; other countries are quoted. The live session is fluent in Spanish and English.',
    homeLabel: 'Home',
    crumb: 'In-person training',
    faqHeading: 'Training questions',
    priceNote,
    offers: offers(
      ['Conference', 'Workshop', 'Full day', 'Multi-day program', 'In-house consulting'],
      'The format most teams book: one working day on their own recipes.',
    ).map((o, i) =>
      i === 0
        ? { ...o, meta: '90–120 min · up to 200 people' }
        : o,
    ),
    howto: {
      name: 'How to book a session',
      description: 'Write with the format, the city and the language the brigade works in. You get a quote before any date is held.',
      steps: [
        { name: 'Email the brief', text: 'Send info@aichef.pro the city, the headcount, the date window and whether the team needs the session in English or Spanish.' },
        { name: 'Receive the quote', text: 'The reply states the format price, plus travel and lodging if the kitchen is outside the peninsular-Spain base. VAT is excluded.' },
        { name: 'Hold the date', text: 'A date is held only after you accept the quote. There is no form and no automatic charge on this page.' },
        { name: 'Run it on your recipes', text: 'The session uses dishes the team already serves, in the AI Chef Pro workspace they will keep using the next day.' },
      ],
    },
    blocks: [
      {
        id: 'language',
        h2: 'Language of the session',
        answer:
          'John delivers the live session fluently in Spanish and English. Say which one the brigade needs when you write.',
        paragraphs: [
          'Slides can follow the language of this page. We will not tell you the day is in a language he does not work in. Support on the product is fluent in Spanish and English and will try in the other five.',
        ],
      },
      {
        id: 'scope',
        h2: 'What the day is, and what it is not',
        answer:
          'It is a working session on costing, allergens, the menu or the content the team posts. It is not a funded-training claim and not a legal opinion.',
        paragraphs: [
          'FUNDAE applies only to the Spanish page’s market and is not offered here. We do not claim CPD, a US state credit, or any public subsidy. The agent catalog you practice on is the one in the workspace you log into. The English pricing page states 75+ agents.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Do you travel outside Spain?',
        a: 'Yes, on request. The published prices are the base for peninsular Spain. Travel and lodging are quoted for the city. Balearic Islands, Canary Islands and other countries are quoted the same way.',
      },
      {
        q: 'Are the prices in dollars?',
        a: 'No. Training prices are in euro, the same currency as the subscription. VAT is excluded.',
      },
      {
        q: 'Is there a public subsidy or FUNDAE credit?',
        a: 'Not on this page. FUNDAE is a Spanish scheme and is not part of the offer for teams outside that scheme. We do not claim any other training credit.',
      },
      {
        q: 'How do I book?',
        a: 'Email info@aichef.pro or WhatsApp +34 744 717 942 during Spanish business hours. A person replies, usually within 24–48 business hours. Nothing is charged from this page.',
      },
    ],
    ctaTitle: 'Ask for a date',
    ctaBody: 'Send the city, the headcount and the language. You get a quote before a date is held.',
    ctaPrimary: 'Email info@aichef.pro',
    ctaSecondary: 'See plans and pricing',
  },
  fr: {
    title: 'Formation IA en restauration, sur place | AI Chef Pro',
    description:
      'John Guerrero se déplace dans votre cuisine : conférence dès 990 €, atelier 1 490 €, journée 2 490 €. Prix en euros, hors TVA, base Espagne péninsulaire. Déplacement en sus. Pas de CPF.',
    keywords: 'formation IA restauration, atelier intelligence artificielle cuisine, formation présentielle restaurant, chef formateur IA',
    eyebrow: 'Formation sur place',
    h1: 'Une formation IA dans votre cuisine, avec le chef qui a construit la suite',
    lead: 'John Guerrero anime la session. Les prix ci-dessous sont ceux publiés pour l’Espagne péninsulaire, en euros, hors TVA.',
    answerLabel: 'Réponse directe',
    answer:
      'Oui, John se déplace. Conférence : 990 € (90–120 minutes, jusqu’à 200 personnes). Atelier de 4 heures : 1 490 € (12–25 personnes). Journée : 2 490 € (10–20 personnes). Programme de 16–24 heures : 4 990 €. Conseil sur place : à partir de 4 990 € pour 2 à 5 jours. Hors TVA. Déplacement et hébergement en sus. Base : Espagne péninsulaire ; les autres pays se chiffrent. La session en direct est à l’aise en espagnol et en anglais. Aucune prise en charge CPF ou OPCO.',
    homeLabel: 'Accueil',
    crumb: 'Formation IA restauration',
    faqHeading: 'Questions sur la formation',
    priceNote: 'Prix de base pour l’Espagne péninsulaire. TVA non comprise. Déplacement et hébergement selon le lieu. Autres pays sur devis. Le FUNDAE est un dispositif espagnol : il ne fait pas partie de cette offre. Pas de prise en charge CPF ni OPCO.',
    offers: [
      { name: 'Conférence', amount: 990, priceLabel: '990 €', meta: '90–120 min · jusqu’à 200 personnes', detail: 'Pour une équipe, une école ou un événement. John montre la suite sur des tâches de cuisine réelles.' },
      { name: 'Atelier', amount: 1490, priceLabel: '1 490 €', meta: '4 heures · 12–25 personnes', detail: 'Pratique : fiche technique, allergènes ou carte, sur les recettes que l’équipe sert déjà.' },
      { name: 'Journée complète', amount: 2490, priceLabel: '2 490 €', meta: '8 heures · 10–20 personnes', detail: 'Le format le plus demandé : une journée de travail sur les recettes de la brigade.', popular: true },
      { name: 'Programme de plusieurs jours', amount: 4990, priceLabel: '4 990 €', meta: '16–24 heures · jusqu’à 30 personnes', detail: 'Plusieurs sessions pour une école, un groupe ou une brigade qui doit partager la même méthode.' },
      { name: 'Conseil sur place', priceLabel: 'à partir de 4 990 €', meta: '2–5 jours · dans votre cuisine', detail: 'Le devis couvre les jours. Déplacement et hébergement sont à part.' },
    ],
    howto: {
      name: 'Comment réserver une session',
      description: 'Écrivez le format, la ville et la langue de la brigade. Vous recevez un devis avant qu’une date soit bloquée.',
      steps: [
        { name: 'Envoyer le brief', text: 'Écrivez à info@aichef.pro : ville, effectif, fenêtre de dates, et si l’équipe a besoin de l’espagnol ou de l’anglais en direct.' },
        { name: 'Recevoir le devis', text: 'La réponse indique le prix du format, plus le déplacement et l’hébergement si la cuisine est hors de la base Espagne péninsulaire. TVA en sus.' },
        { name: 'Bloquer la date', text: 'Une date n’est tenue qu’après acceptation du devis. Cette page n’a pas de formulaire et ne débite rien.' },
        { name: 'Travailler vos recettes', text: 'La session part des plats que l’équipe sert déjà, dans l’espace AI Chef Pro qu’elle gardera le lendemain.' },
      ],
    },
    blocks: [
      {
        id: 'langue',
        h2: 'Langue de la session',
        answer:
          'John anime le direct en espagnol et en anglais. Indiquez laquelle la brigade parle quand vous écrivez.',
        paragraphs: [
          'Les supports peuvent suivre le français de cette page. Nous ne vous dirons pas que la journée se tient dans une langue qu’il ne pratique pas. L’assistance produit est à l’aise en espagnol et en anglais, et fait le nécessaire dans les cinq autres langues.',
        ],
      },
      {
        id: 'perimetre',
        h2: 'Ce que la journée est, et ce qu’elle n’est pas',
        answer:
          'C’est une session de travail sur les coûts, les allergènes, la carte ou les contenus. Ce n’est ni un dossier CPF, ni un avis juridique.',
        paragraphs: [
          'Le catalogue sur lequel vous vous exercez est celui de l’espace où vous vous connectez. La page tarifs en français indique aujourd’hui plus de 50 agents.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Vous déplacez-vous en France ?',
        a: 'Oui, sur devis. Les prix publiés sont la base pour l’Espagne péninsulaire. Déplacement et hébergement se chiffrent pour la ville. Baléares, Canaries et autres pays suivent la même règle.',
      },
      {
        q: 'La formation est-elle éligible au CPF ou à un OPCO ?',
        a: 'Non. Nous ne revendiquons aucune prise en charge CPF ou OPCO, ni aucun autre financement public.',
      },
      {
        q: 'Les prix sont-ils hors taxes ?',
        a: 'Oui. TVA non comprise. La devise est l’euro, la même que l’abonnement.',
      },
      {
        q: 'Comment réserver ?',
        a: 'Écrivez à info@aichef.pro ou sur WhatsApp au +34 744 717 942, en horaire de bureau espagnol. Une personne répond, en général sous 24 à 48 heures ouvrées. Rien n’est débité depuis cette page.',
      },
    ],
    ctaTitle: 'Demander une date',
    ctaBody: 'Indiquez la ville, l’effectif et la langue. Vous recevez un devis avant qu’une date soit bloquée.',
    ctaPrimary: 'Écrire à info@aichef.pro',
    ctaSecondary: 'Voir les tarifs',
  },
  de: {
    title: 'Präsenzschulung KI für die Gastronomie | AI Chef Pro',
    description:
      'John Guerrero kommt in Ihre Küche: Vortrag ab 990 €, Workshop 1.490 €, Tag 2.490 €. Preise in Euro, ohne MwSt., Basis spanisches Festland. Reise extra. Kein Bildungsgutschein.',
    keywords: 'KI Schulung Gastronomie, Präsenzschulung KI Küche, Workshop künstliche Intelligenz Restaurant, Koch Schulung KI',
    eyebrow: 'Präsenzschulung',
    h1: 'KI-Schulung in Ihrer Küche, mit dem Koch, der die Suite gebaut hat',
    lead: 'John Guerrero hält die Session. Die Preise unten sind die veröffentlichten Preise für das spanische Festland, in Euro, ohne Mehrwertsteuer.',
    answerLabel: 'Kurzantwort',
    answer:
      'Ja, John reist an. Vortrag: 990 € (90–120 Minuten, bis 200 Personen). Workshop von 4 Stunden: 1.490 € (12–25 Personen). Ganzer Tag: 2.490 € (10–20 Personen). Programm von 16–24 Stunden: 4.990 €. Beratung vor Ort: ab 4.990 € für 2–5 Tage. Ohne MwSt. Reise und Unterkunft extra. Basis: spanisches Festland; andere Länder werden angeboten. Die Live-Session hält er auf Spanisch und Englisch. Kein Bildungsgutschein.',
    homeLabel: 'Startseite',
    crumb: 'Präsenzschulung KI',
    faqHeading: 'Fragen zur Schulung',
    priceNote: 'Basispreise für das spanische Festland. MwSt. nicht enthalten. Reise und Unterkunft je nach Ort. Andere Länder auf Anfrage. FUNDAE ist ein spanisches Förderprogramm und gehört nicht zu diesem Angebot. Kein Bildungsgutschein.',
    offers: [
      { name: 'Vortrag', amount: 990, priceLabel: '990 €', meta: '90–120 Min. · bis 200 Personen', detail: 'Für ein Team, eine Schule oder eine Veranstaltung. John zeigt die Suite an echten Küchenaufgaben.' },
      { name: 'Workshop', amount: 1490, priceLabel: '1.490 €', meta: '4 Stunden · 12–25 Personen', detail: 'Praxis: Kalkulation, Allergene oder Karte, an den Rezepten, die das Team schon kocht.' },
      { name: 'Ganzer Tag', amount: 2490, priceLabel: '2.490 €', meta: '8 Stunden · 10–20 Personen', detail: 'Das Format, das die meisten Teams buchen: ein Arbeitstag an den eigenen Rezepten.', popular: true },
      { name: 'Mehrtägiges Programm', amount: 4990, priceLabel: '4.990 €', meta: '16–24 Stunden · bis 30 Personen', detail: 'Mehrere Sessions für eine Schule, eine Gruppe oder eine Brigade mit derselben Methode.' },
      { name: 'Beratung vor Ort', priceLabel: 'ab 4.990 €', meta: '2–5 Tage · in Ihrer Küche', detail: 'Das Angebot deckt die Tage. Reise und Unterkunft stehen extra.' },
    ],
    howto: {
      name: 'So buchen Sie eine Session',
      description: 'Schreiben Sie Format, Ort und die Sprache der Brigade. Sie erhalten ein Angebot, bevor ein Termin gehalten wird.',
      steps: [
        { name: 'Das Briefing schicken', text: 'Mailen Sie an info@aichef.pro: Ort, Personenzahl, Zeitfenster und ob das Team die Live-Session auf Englisch oder Spanisch braucht.' },
        { name: 'Das Angebot lesen', text: 'Die Antwort nennt den Formatpreis plus Reise und Unterkunft, wenn die Küche außerhalb der Festland-Basis liegt. MwSt. extra.' },
        { name: 'Den Termin halten', text: 'Ein Termin wird erst nach Ihrer Zusage gehalten. Diese Seite hat kein Formular und bucht nichts ab.' },
        { name: 'An Ihren Rezepten arbeiten', text: 'Die Session nutzt Gerichte, die das Team schon serviert, im AI-Chef-Pro-Arbeitsbereich, den es am nächsten Tag behält.' },
      ],
    },
    blocks: [
      {
        id: 'sprache',
        h2: 'Sprache der Session',
        answer: 'John hält die Live-Session auf Spanisch und Englisch. Schreiben Sie, welche die Brigade braucht.',
        paragraphs: [
          'Unterlagen können dem Deutschen dieser Seite folgen. Wir sagen Ihnen nicht, der Tag laufe in einer Sprache, die er nicht spricht. Der Produktsupport antwortet sicher auf Spanisch und Englisch und versucht es in den anderen Sprachen.',
        ],
      },
      {
        id: 'rahmen',
        h2: 'Was der Tag ist und was er nicht ist',
        answer: 'Es ist eine Arbeitssession zu Wareneinsatz, Allergenen, Karte oder Inhalten. Es ist kein Bildungsgutschein und kein Rechtsrat.',
        paragraphs: [
          'Der Katalog, an dem Sie üben, ist der des Arbeitsbereichs, in dem Sie sich anmelden. Die deutsche Preisseite nennt heute mehr als 50 Agenten.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Kommen Sie nach Deutschland?',
        a: 'Ja, auf Anfrage. Die veröffentlichten Preise sind die Basis für das spanische Festland. Reise und Unterkunft werden für den Ort angeboten. Balearen, Kanaren und andere Länder ebenso.',
      },
      {
        q: 'Gibt es einen Bildungsgutschein?',
        a: 'Nein. Wir behaupten keine Förderung durch Bildungsgutschein oder einen anderen Träger.',
      },
      {
        q: 'Sind die Preise netto?',
        a: 'Ja. Mehrwertsteuer ist nicht enthalten. Die Währung ist der Euro, dieselbe wie beim Abo.',
      },
      {
        q: 'Wie buche ich?',
        a: 'Schreiben Sie an info@aichef.pro oder per WhatsApp an +34 744 717 942 während der spanischen Bürozeiten. Eine Person antwortet, in der Regel innerhalb von 24–48 Stunden an Werktagen. Von dieser Seite wird nichts abgebucht.',
      },
    ],
    ctaTitle: 'Einen Termin anfragen',
    ctaBody: 'Nennen Sie Ort, Personenzahl und Sprache. Sie erhalten ein Angebot, bevor ein Termin gehalten wird.',
    ctaPrimary: 'E-Mail an info@aichef.pro',
    ctaSecondary: 'Preise ansehen',
  },
  it: {
    title: 'Formazione IA in ristorazione, in presenza | AI Chef Pro',
    description:
      'John Guerrero viene in cucina: conferenza da 990 €, workshop 1.490 €, giornata 2.490 €. Prezzi in euro, IVA esclusa, base Spagna peninsulare. Trasferta a parte.',
    keywords: 'formazione IA ristorazione, workshop intelligenza artificiale cucina, corso chef IA, formazione in presenza ristorante',
    eyebrow: 'Formazione in presenza',
    h1: 'Formazione IA nella tua cucina, con lo chef che ha costruito la suite',
    lead: 'John Guerrero tiene la sessione. I prezzi sotto sono quelli pubblicati per la Spagna peninsulare, in euro, IVA esclusa.',
    answerLabel: 'Risposta diretta',
    answer:
      'Sì, John si sposta. Conferenza: 990 € (90–120 minuti, fino a 200 persone). Workshop di 4 ore: 1.490 € (12–25 persone). Giornata: 2.490 € (10–20 persone). Programma di 16–24 ore: 4.990 €. Consulenza in sede: da 4.990 € per 2–5 giorni. IVA esclusa. Trasferta e alloggio a parte. Base: Spagna peninsulare; gli altri paesi si quotano. La sessione dal vivo è sciolta in spagnolo e in inglese. Nessun fondo interprofessionale.',
    homeLabel: 'Home',
    crumb: 'Formazione IA ristorazione',
    faqHeading: 'Domande sulla formazione',
    priceNote: 'Prezzi base per la Spagna peninsulare. IVA esclusa. Trasferta e alloggio secondo la sede. Altri paesi su richiesta. Il FUNDAE è un dispositivo spagnolo e non fa parte di questa offerta. Nessun finanziamento da fondi interprofessionali.',
    offers: [
      { name: 'Conferenza', amount: 990, priceLabel: '990 €', meta: '90–120 min · fino a 200 persone', detail: 'Per una brigata, una scuola o un evento. John mostra la suite su compiti di cucina veri.' },
      { name: 'Workshop', amount: 1490, priceLabel: '1.490 €', meta: '4 ore · 12–25 persone', detail: 'Pratica: scheda costo, allergeni o menu, sulle ricette che la brigata già serve.' },
      { name: 'Giornata intera', amount: 2490, priceLabel: '2.490 €', meta: '8 ore · 10–20 persone', detail: 'Il formato che le brigate prenotano di più: un giorno di lavoro sulle proprie ricette.', popular: true },
      { name: 'Programma di più giorni', amount: 4990, priceLabel: '4.990 €', meta: '16–24 ore · fino a 30 persone', detail: 'Più sessioni per una scuola, un gruppo o una brigata che deve condividere lo stesso metodo.' },
      { name: 'Consulenza in sede', priceLabel: 'da 4.990 €', meta: '2–5 giorni · nella tua cucina', detail: 'Il preventivo copre i giorni. Trasferta e alloggio sono a parte.' },
    ],
    howto: {
      name: 'Come prenotare una sessione',
      description: 'Scrivi formato, città e lingua della brigata. Ricevi un preventivo prima che una data sia tenuta.',
      steps: [
        { name: 'Manda il brief', text: 'Scrivi a info@aichef.pro: città, numero di persone, finestra di date e se la brigata ha bisogno dello spagnolo o dell’inglese dal vivo.' },
        { name: 'Leggi il preventivo', text: 'La risposta indica il prezzo del formato, più trasferta e alloggio se la cucina è fuori dalla base Spagna peninsulare. IVA esclusa.' },
        { name: 'Tieni la data', text: 'Una data si tiene solo dopo che accetti il preventivo. Questa pagina non ha un modulo e non addebita nulla.' },
        { name: 'Lavora sulle tue ricette', text: 'La sessione parte dai piatti che la brigata già serve, nello spazio AI Chef Pro che userà il giorno dopo.' },
      ],
    },
    blocks: [
      {
        id: 'lingua',
        h2: 'Lingua della sessione',
        answer: 'John tiene il vivo in spagnolo e in inglese. Scrivi quale serve alla brigata.',
        paragraphs: [
          'I materiali possono seguire l’italiano di questa pagina. Non ti diremo che la giornata si tiene in una lingua che non parla. L’assistenza prodotto è sciolta in spagnolo e in inglese e ci prova nelle altre lingue.',
        ],
      },
      {
        id: 'perimetro',
        h2: 'Che cosa è la giornata, e che cosa non è',
        answer: 'È una sessione di lavoro su costi, allergeni, menu o contenuti. Non è un finanziamento e non è un parere legale.',
        paragraphs: [
          'Il catalogo su cui ti eserciti è quello dello spazio in cui entri. La pagina prezzi in italiano indica oggi più di 50 agenti.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Vieni in Italia?',
        a: 'Sì, su richiesta. I prezzi pubblicati sono la base per la Spagna peninsulare. Trasferta e alloggio si quotano per la città. Baleari, Canarie e altri paesi allo stesso modo.',
      },
      {
        q: 'La formazione è finanziata?',
        a: 'No. Non dichiariamo fondi interprofessionali né altri contributi pubblici.',
      },
      {
        q: 'I prezzi sono IVA esclusa?',
        a: 'Sì. IVA esclusa. La valuta è l’euro, la stessa dell’abbonamento.',
      },
      {
        q: 'Come prenoto?',
        a: 'Scrivi a info@aichef.pro o su WhatsApp al +34 744 717 942, in orario d’ufficio spagnolo. Risponde una persona, di solito entro 24–48 ore lavorative. Da questa pagina non parte alcun addebito.',
      },
    ],
    ctaTitle: 'Chiedi una data',
    ctaBody: 'Indica città, numero di persone e lingua. Ricevi un preventivo prima che una data sia tenuta.',
    ctaPrimary: 'Scrivi a info@aichef.pro',
    ctaSecondary: 'Vedi i prezzi',
  },
  pt: {
    title: 'Formação de IA na restauração, presencial | AI Chef Pro',
    description:
      'John Guerrero vai à tua cozinha: conferência desde 990 €, workshop 1.490 €, dia 2.490 €. Preços em euros, IVA excluído, base Espanha peninsular. Deslocação à parte. Sem apoio do IEFP.',
    keywords: 'formação IA restauração, workshop inteligência artificial cozinha, formação presencial restaurante, chef formador IA',
    eyebrow: 'Formação presencial',
    h1: 'Formação de IA na tua cozinha, com o chef que construiu a suite',
    lead: 'John Guerrero conduz a sessão. Os preços abaixo são os publicados para Espanha peninsular, em euros, IVA excluído.',
    answerLabel: 'Resposta direta',
    answer:
      'Sim, o John desloca-se. Conferência: 990 € (90–120 minutos, até 200 pessoas). Workshop de 4 horas: 1.490 € (12–25 pessoas). Dia completo: 2.490 € (10–20 pessoas). Programa de 16–24 horas: 4.990 €. Consultoria no local: a partir de 4.990 € por 2–5 dias. IVA excluído. Deslocação e alojamento à parte. Base: Espanha peninsular; outros países sob orçamento. A sessão ao vivo é fluente em espanhol e em inglês. Sem apoio do IEFP.',
    homeLabel: 'Início',
    crumb: 'Formação IA restauração',
    faqHeading: 'Perguntas sobre a formação',
    priceNote: 'Preços base para Espanha peninsular. IVA não incluído. Deslocação e alojamento conforme o local. Outros países sob consulta. O FUNDAE é um regime espanhol e não faz parte desta oferta. Sem apoio do IEFP.',
    offers: [
      { name: 'Conferência', amount: 990, priceLabel: '990 €', meta: '90–120 min · até 200 pessoas', detail: 'Para uma equipa, uma escola ou um evento. O John mostra a suite em tarefas reais de cozinha.' },
      { name: 'Workshop', amount: 1490, priceLabel: '1.490 €', meta: '4 horas · 12–25 pessoas', detail: 'Prática: ficha técnica, alergénios ou carta, nas receitas que a equipa já serve.' },
      { name: 'Dia completo', amount: 2490, priceLabel: '2.490 €', meta: '8 horas · 10–20 pessoas', detail: 'O formato que as equipas mais pedem: um dia de trabalho nas receitas próprias.', popular: true },
      { name: 'Programa de vários dias', amount: 4990, priceLabel: '4.990 €', meta: '16–24 horas · até 30 pessoas', detail: 'Várias sessões para uma escola, um grupo ou uma brigada que precisa do mesmo método.' },
      { name: 'Consultoria no local', priceLabel: 'a partir de 4.990 €', meta: '2–5 dias · na tua cozinha', detail: 'O orçamento cobre os dias. Deslocação e alojamento ficam à parte.' },
    ],
    howto: {
      name: 'Como marcas uma sessão',
      description: 'Escreve o formato, a cidade e a língua da brigada. Recebes um orçamento antes de uma data ficar retida.',
      steps: [
        { name: 'Enviar o brief', text: 'Escreve para info@aichef.pro: cidade, número de pessoas, janela de datas e se a equipa precisa da sessão ao vivo em espanhol ou em inglês.' },
        { name: 'Ler o orçamento', text: 'A resposta indica o preço do formato, mais deslocação e alojamento se a cozinha estiver fora da base de Espanha peninsular. IVA excluído.' },
        { name: 'Reter a data', text: 'Uma data só fica retida depois de aceitares o orçamento. Esta página não tem formulário e não cobra nada.' },
        { name: 'Trabalhar as tuas receitas', text: 'A sessão parte dos pratos que a equipa já serve, no espaço AI Chef Pro que vai usar no dia seguinte.' },
      ],
    },
    blocks: [
      {
        id: 'lingua',
        h2: 'Língua da sessão',
        answer: 'O John conduz o direto em espanhol e em inglês. Diz qual a brigada precisa quando escreveres.',
        paragraphs: [
          'Os materiais podem seguir o português de Portugal desta página. Não te dizemos que o dia decorre numa língua que ele não trabalha. O apoio do produto responde com à-vontade em espanhol e em inglês e tenta nas outras línguas.',
        ],
      },
      {
        id: 'ambito',
        h2: 'O que o dia é, e o que não é',
        answer: 'É uma sessão de trabalho sobre custos, alergénios, carta ou conteúdos. Não é um apoio do IEFP nem um parecer jurídico.',
        paragraphs: [
          'O catálogo em que treinas é o do espaço onde entras. A página de preços em português indica hoje mais de 50 agentes.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Vens a Portugal?',
        a: 'Sim, sob consulta. Os preços publicados são a base para Espanha peninsular. Deslocação e alojamento orçamentam-se para a cidade. Baleares, Canárias e outros países seguem a mesma regra.',
      },
      {
        q: 'A formação tem apoio do IEFP?',
        a: 'Não. Não declaramos apoio do IEFP nem de outro fundo público.',
      },
      {
        q: 'Os preços são sem IVA?',
        a: 'Sim. IVA excluído. A moeda é o euro, a mesma da subscrição.',
      },
      {
        q: 'Como marco?',
        a: 'Escreve para info@aichef.pro ou para o WhatsApp +34 744 717 942, em horário laboral espanhol. Responde uma pessoa, em regra dentro de 24–48 horas úteis. Esta página não cobra nada.',
      },
    ],
    ctaTitle: 'Pede uma data',
    ctaBody: 'Indica a cidade, o número de pessoas e a língua. Recebes um orçamento antes de uma data ficar retida.',
    ctaPrimary: 'Escrever para info@aichef.pro',
    ctaSecondary: 'Ver preços',
  },
  nl: {
    title: 'AI-training voor de horeca, op locatie | AI Chef Pro',
    description:
      'John Guerrero komt naar je keuken: lezing vanaf 990 €, workshop 1.490 €, dag 2.490 €. Prijzen in euro, exclusief btw, basis Spaans vasteland. Reis apart. Geen SLIM-vergoeding.',
    keywords: 'AI training horeca, workshop kunstmatige intelligentie keuken, training op locatie restaurant, chef AI cursus',
    eyebrow: 'Training op locatie',
    h1: 'AI-training in je keuken, met de chef die de suite bouwde',
    lead: 'John Guerrero geeft de sessie. De prijzen hieronder zijn de gepubliceerde prijzen voor het Spaanse vasteland, in euro, exclusief btw.',
    answerLabel: 'Kort antwoord',
    answer:
      'Ja, John reist. Lezing: 990 € (90–120 minuten, tot 200 mensen). Workshop van 4 uur: 1.490 € (12–25 mensen). Hele dag: 2.490 € (10–20 mensen). Programma van 16–24 uur: 4.990 €. Advies op locatie: vanaf 4.990 € voor 2–5 dagen. Exclusief btw. Reis en verblijf extra. Basis: Spaans vasteland; andere landen op offerte. De live sessie geeft hij vloeiend in het Spaans en het Engels. Geen SLIM- of andere scholingsvergoeding.',
    homeLabel: 'Home',
    crumb: 'AI-training horeca',
    faqHeading: 'Vragen over de training',
    priceNote: 'Basisprijzen voor het Spaanse vasteland. Btw niet inbegrepen. Reis en verblijf volgens de locatie. Andere landen op aanvraag. FUNDAE is een Spaanse regeling en hoort niet bij dit aanbod. Geen SLIM-vergoeding.',
    offers: [
      { name: 'Lezing', amount: 990, priceLabel: '990 €', meta: '90–120 min · tot 200 mensen', detail: 'Voor een team, een school of een event. John laat de suite zien op echte keukentaken.' },
      { name: 'Workshop', amount: 1490, priceLabel: '1.490 €', meta: '4 uur · 12–25 mensen', detail: 'Hands-on: kostprijs, allergenen of kaart, op de recepten die het team al kookt.' },
      { name: 'Hele dag', amount: 2490, priceLabel: '2.490 €', meta: '8 uur · 10–20 mensen', detail: 'Het format dat de meeste teams boeken: één werkdag op hun eigen recepten.', popular: true },
      { name: 'Meerdaags programma', amount: 4990, priceLabel: '4.990 €', meta: '16–24 uur · tot 30 mensen', detail: 'Meerdere sessies voor een school, een groep of een brigade die dezelfde methode nodig heeft.' },
      { name: 'Advies op locatie', priceLabel: 'vanaf 4.990 €', meta: '2–5 dagen · in je keuken', detail: 'De offerte dekt de dagen. Reis en verblijf staan apart.' },
    ],
    howto: {
      name: 'Zo boek je een sessie',
      description: 'Mail het format, de stad en de taal van de brigade. Je krijgt een offerte voordat een datum wordt vastgehouden.',
      steps: [
        { name: 'Stuur de briefing', text: 'Mail info@aichef.pro: stad, aantal mensen, datums en of het team de live sessie in het Engels of het Spaans nodig heeft.' },
        { name: 'Lees de offerte', text: 'Het antwoord noemt de formatprijs, plus reis en verblijf als de keuken buiten de basis van het Spaanse vasteland ligt. Btw extra.' },
        { name: 'Houd de datum', text: 'Een datum wordt pas vastgehouden nadat je de offerte accepteert. Deze pagina heeft geen formulier en rekent niets af.' },
        { name: 'Werk op je eigen recepten', text: 'De sessie gebruikt gerechten die het team al serveert, in de AI Chef Pro-werkruimte die ze de volgende dag houden.' },
      ],
    },
    blocks: [
      {
        id: 'taal',
        h2: 'Taal van de sessie',
        answer: 'John geeft de live sessie in het Spaans en het Engels. Schrijf welke de brigade nodig heeft.',
        paragraphs: [
          'Materiaal kan het Nederlands van deze pagina volgen. We zeggen niet dat de dag in een taal is die hij niet spreekt. Productsupport antwoordt vlot in het Spaans en het Engels en doet zijn best in de andere talen.',
        ],
      },
      {
        id: 'kader',
        h2: 'Wat de dag is, en wat hij niet is',
        answer: 'Het is een werksessie over kostprijs, allergenen, kaart of content. Het is geen SLIM-aanvraag en geen juridisch advies.',
        paragraphs: [
          'De catalogus waarop je oefent is die van de werkruimte waar je inlogt. De Nederlandse prijspagina noemt vandaag meer dan 50 agenten.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Komen jullie naar Nederland of Vlaanderen?',
        a: 'Ja, op aanvraag. De gepubliceerde prijzen zijn de basis voor het Spaanse vasteland. Reis en verblijf worden geoffreerd voor de stad. Balearen, Canarische Eilanden en andere landen gaan hetzelfde.',
      },
      {
        q: 'Is er een SLIM-vergoeding?',
        a: 'Nee. We claimen geen SLIM-regeling en geen ander scholingsbudget.',
      },
      {
        q: 'Zijn de prijzen exclusief btw?',
        a: 'Ja. Btw is niet inbegrepen. De valuta is de euro, dezelfde als het abonnement.',
      },
      {
        q: 'Hoe boek ik?',
        a: 'Mail info@aichef.pro of app WhatsApp +34 744 717 942 tijdens Spaanse kantoortijden. Er antwoordt een persoon, meestal binnen 24–48 werkuren. Vanaf deze pagina wordt niets afgeschreven.',
      },
    ],
    ctaTitle: 'Vraag een datum aan',
    ctaBody: 'Noem de stad, het aantal mensen en de taal. Je krijgt een offerte voordat een datum wordt vastgehouden.',
    ctaPrimary: 'Mail info@aichef.pro',
    ctaSecondary: 'Bekijk de prijzen',
  },
};
