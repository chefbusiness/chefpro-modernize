import type { PageCopy, ParityLang, PlanRow, Standard } from './types';

const enPlans: PlanRow[] = [
  { name: 'Member', price: '€10/month', detail: '10,000 credits · no lock-in' },
  { name: 'Premium Pro', price: '€25/month', detail: '85,000 credits' },
  { name: 'Premium Plus', price: '€50/month', detail: '175,000 credits' },
  { name: 'Premium Max', price: '€95/month', detail: 'Unlimited credits' },
  { name: 'Max annual', price: '€950/year', detail: 'Unlimited · two months less than 12 × €95' },
];

const standardsEn: Standard[] = [
  { title: 'Research before publishing', body: 'We look at the topic and at what is already published, and we check claims against sources a kitchen can open.' },
  { title: 'A figure has a source, or we say it is an estimate', body: 'If we do not have a source, the page says so. We do not invent local rents, fines or headcounts.' },
  { title: 'A person reviews the draft', body: 'A draft can start with AI. A cook or an editor checks that the step works on a pass, not only on a screen.' },
  { title: 'AI images are labeled as reference', body: 'An image made with AI is marked as a reference image. We do not present it as a photograph of a real plate or a real dining room.' },
  { title: 'Corrections stay visible', body: 'When we fix an error we keep a note of the change and the date instead of silently rewriting history.' },
  { title: 'Write to us about a mistake', body: 'Email info@aichef.pro with the page and the line. A person reads it.' },
];

export const ABOUT: Record<ParityLang, PageCopy> = {
  en: {
    title: 'About AI Chef Pro and Chef John Guerrero',
    description:
      'AI Chef Pro was built by Chef John Guerrero: in kitchens since age 17, gastronomic consultant since 2010, 29 years in hospitality, founder of ChefBusiness. Editorial standards and euro pricing.',
    keywords: 'about AI Chef Pro, John Guerrero chef, ChefBusiness, who made AI Chef Pro',
    eyebrow: 'About',
    h1: 'A kitchen tool built by someone who worked a pass',
    lead: 'AI Chef Pro is John Guerrero’s suite for professional kitchens, inside the ChefBusiness group.',
    answerLabel: 'Direct answer',
    answer:
      'John Guerrero has been in professional kitchens since he was 17 and a gastronomic consultant since 2010. He has 29 years in hospitality and founded the ChefBusiness group. AI Chef Pro is the suite he built for cooks. The English pricing page states 75+ agents, seven languages, and a Member plan at €10 per month with 10,000 credits.',
    homeLabel: 'Home',
    crumb: 'About',
    faqHeading: 'About questions',
    chips: [
      'Founder and CEO of AI Chef Pro',
      'Founder of the ChefBusiness group',
      'In kitchens since age 17',
      'Gastronomic consultant since 2010',
    ],
    stats: [
      { big: '75+', label: 'Agents on the English pricing page' },
      { big: '7', label: 'Languages, Spanish first' },
      { big: '10,000', label: 'Credits on the Member plan' },
      { big: '€10', label: 'Per month, no lock-in' },
    ],
    plans: enPlans,
    plansHeading: 'Plans, in euro',
    standards: standardsEn,
    standardsHeading: 'How we publish',
    blocks: [
      {
        id: 'john',
        h2: 'Who John Guerrero is',
        answer:
          'He learned the job in service, not from a software brief. Twenty-nine years in hospitality, consulting since 2010 through ChefBusiness.',
        paragraphs: [
          'The same operational problems showed up in very different rooms: food cost that nobody owned, a menu that did not match what guests ordered, and a process that lived in one person’s head. AI Chef Pro is his answer to that pattern: agents that speak kitchen tasks, used in the browser.',
          'His personal site is johnguerrero.es. The YouTube channel is @aichefpro. Press and corrections go to info@aichef.pro.',
        ],
      },
    ],
    faqs: [
      {
        q: 'What is AI Chef Pro?',
        a: 'A suite of specialized AI agents for hospitality professionals: costing, menus, allergens, content, local search and the daily paperwork of a kitchen. The English pricing page states 75+ agents. Member is €10 per month with 10,000 credits, with no lock-in.',
      },
      {
        q: 'Who founded it?',
        a: 'John Guerrero, in kitchens since age 17, gastronomic consultant since 2010, founder of ChefBusiness. The suite comes from that work.',
      },
      {
        q: 'How do you write the blog?',
        a: 'We research before publishing, attach a source or mark an estimate, have a person review the draft, and label AI images as reference. Corrections are logged. Email info@aichef.pro if a line is wrong.',
      },
    ],
    ctaTitle: 'Read the pricing page next',
    ctaBody: 'The numbers on this page are the published plan prices. The live list of agents is what you see after you sign in to enapp.aichef.pro.',
    ctaPrimary: 'Open the app',
    ctaSecondary: 'See plans and pricing',
  },
  fr: {
    title: 'À propos d’AI Chef Pro et du chef John Guerrero',
    description:
      'AI Chef Pro est l’outil du chef John Guerrero : en cuisine depuis ses 17 ans, consultant depuis 2010, 29 ans de restauration, fondateur de ChefBusiness.',
    keywords: 'à propos AI Chef Pro, John Guerrero chef, ChefBusiness, qui a créé AI Chef Pro',
    eyebrow: 'À propos',
    h1: 'Un outil de cuisine construit par quelqu’un qui a tenu un passe',
    lead: 'AI Chef Pro est la suite de John Guerrero pour les cuisines professionnelles, dans le groupe ChefBusiness.',
    answerLabel: 'Réponse directe',
    answer:
      'John Guerrero est en cuisine professionnelle depuis ses 17 ans et consultant en restauration depuis 2010. Il a 29 ans de métier et a fondé le groupe ChefBusiness. AI Chef Pro est la suite qu’il a construite pour les cuisiniers. La page tarifs en français indique aujourd’hui plus de 50 agents ; l’espace espagnol en publie 75+. Le forfait Membre est à 10 € par mois avec 10 000 crédits.',
    homeLabel: 'Accueil',
    crumb: 'À propos',
    faqHeading: 'Questions',
    chips: [
      'Fondateur et CEO d’AI Chef Pro',
      'Fondateur du groupe ChefBusiness',
      'En cuisine depuis ses 17 ans',
      'Consultant depuis 2010',
    ],
    stats: [
      { big: '50+', label: 'Agents indiqués sur la page tarifs FR' },
      { big: '7', label: 'Langues, espagnol d’origine' },
      { big: '10 000', label: 'Crédits du forfait Membre' },
      { big: '10 €', label: 'Par mois, sans engagement' },
    ],
    plans: [
      { name: 'Membre', price: '10 €/mois', detail: '10 000 crédits · sans engagement' },
      { name: 'Premium Pro', price: '25 €/mois', detail: '85 000 crédits' },
      { name: 'Premium Plus', price: '50 €/mois', detail: '175 000 crédits' },
      { name: 'Premium Max', price: '95 €/mois', detail: 'Crédits illimités' },
      { name: 'Max annuel', price: '950 €/an', detail: 'Illimités · deux mois de moins que 12 × 95 €' },
    ],
    plansHeading: 'Forfaits, en euros',
    standardsHeading: 'Comment nous publions',
    standards: [
      { title: 'On cherche avant d’écrire', body: 'Nous regardons le sujet et ce qui est déjà publié, et nous vérifions les affirmations avec une source qu’une cuisine peut ouvrir.' },
      { title: 'Un chiffre a une source, ou nous disons que c’est une estimation', body: 'Sans source, la page le dit. Nous n’inventons ni loyers, ni amendes, ni effectifs locaux.' },
      { title: 'Une personne relit', body: 'Un brouillon peut commencer avec l’IA. Un cuisinier ou un éditeur vérifie que le geste tient au passe.' },
      { title: 'Les images d’IA sont des images de référence', body: 'Une image générée est étiquetée comme référence. Nous ne la faisons pas passer pour la photo d’une assiette ou d’une salle réelle.' },
      { title: 'Les corrections restent visibles', body: 'Quand nous corrigeons une erreur, nous notons le changement et la date.' },
      { title: 'Écrivez-nous si une ligne est fausse', body: 'Envoyez la page et la phrase à info@aichef.pro. Une personne lit.' },
    ],
    blocks: [
      {
        id: 'john',
        h2: 'Qui est John Guerrero',
        answer:
          'Il a appris le métier en service, pas dans un cahier des charges logiciel. Vingt-neuf ans de restauration, conseil depuis 2010 avec ChefBusiness.',
        paragraphs: [
          'Les mêmes problèmes revenaient dans des salles très différentes : un food cost dont personne n’était responsable, une carte qui ne suivait pas les ventes, un processus qui tenait dans la tête d’une seule personne. AI Chef Pro est sa réponse : des agents qui parlent les tâches de cuisine, dans le navigateur.',
          'Son site personnel est johnguerrero.es. La chaîne YouTube est @aichefpro. Presse et corrections : info@aichef.pro.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Qu’est-ce qu’AI Chef Pro ?',
        a: 'Une suite d’agents spécialisés pour la restauration : fiches, carte, allergènes, contenu et recherche locale. La page tarifs française indique plus de 50 agents aujourd’hui. Le forfait Membre est à 10 € par mois avec 10 000 crédits, sans engagement.',
      },
      {
        q: 'Qui a fondé le projet ?',
        a: 'John Guerrero, en cuisine depuis ses 17 ans, consultant depuis 2010, fondateur de ChefBusiness.',
      },
      {
        q: 'Comment écrivez-vous le blog ?',
        a: 'Recherche avant publication, source ou mention d’estimation, relecture humaine, images d’IA marquées comme référence, corrections datées. Écrivez à info@aichef.pro si une ligne est fausse.',
      },
    ],
    ctaTitle: 'La page tarifs est la source des prix',
    ctaBody: 'La liste réelle des agents est celle que vous voyez après connexion sur frapp.aichef.pro.',
    ctaPrimary: 'Ouvrir l’application',
    ctaSecondary: 'Voir les tarifs',
  },
  de: {
    title: 'Über AI Chef Pro und Koch John Guerrero',
    description:
      'AI Chef Pro stammt von Koch John Guerrero: seit dem 17. Lebensjahr in der Küche, Berater seit 2010, 29 Jahre Gastronomie, Gründer von ChefBusiness.',
    keywords: 'über AI Chef Pro, John Guerrero Koch, ChefBusiness, Gründer AI Chef Pro',
    eyebrow: 'Über uns',
    h1: 'Ein Küchenwerkzeug von jemandem, der am Pass gestanden hat',
    lead: 'AI Chef Pro ist die Suite von John Guerrero für Profiküchen, in der Gruppe ChefBusiness.',
    answerLabel: 'Kurzantwort',
    answer:
      'John Guerrero arbeitet seit seinem 17. Lebensjahr in der Profiküche und ist seit 2010 gastronomischer Berater. Er hat 29 Jahre Berufserfahrung und hat die Gruppe ChefBusiness gegründet. AI Chef Pro ist die Suite, die er für Köche gebaut hat. Die deutsche Preisseite nennt heute mehr als 50 Agenten; der spanische Arbeitsbereich veröffentlicht 75+. Der Mitgliedsplan kostet 10 € im Monat mit 10.000 Credits.',
    homeLabel: 'Startseite',
    crumb: 'Über uns',
    faqHeading: 'Fragen',
    chips: [
      'Gründer und CEO von AI Chef Pro',
      'Gründer der Gruppe ChefBusiness',
      'Seit dem 17. Lebensjahr in der Küche',
      'Berater seit 2010',
    ],
    stats: [
      { big: '50+', label: 'Agenten auf der deutschen Preisseite' },
      { big: '7', label: 'Sprachen, Spanisch zuerst' },
      { big: '10.000', label: 'Credits im Mitgliedsplan' },
      { big: '10 €', label: 'Im Monat, ohne Bindung' },
    ],
    plans: [
      { name: 'Mitglied', price: '10 €/Monat', detail: '10.000 Credits · ohne Bindung' },
      { name: 'Premium Pro', price: '25 €/Monat', detail: '85.000 Credits' },
      { name: 'Premium Plus', price: '50 €/Monat', detail: '175.000 Credits' },
      { name: 'Premium Max', price: '95 €/Monat', detail: 'Unbegrenzte Credits' },
      { name: 'Max jährlich', price: '950 €/Jahr', detail: 'Unbegrenzt · zwei Monate weniger als 12 × 95 €' },
    ],
    plansHeading: 'Tarife, in Euro',
    standardsHeading: 'Wie wir veröffentlichen',
    standards: [
      { title: 'Zuerst recherchieren', body: 'Wir prüfen das Thema und das, was schon veröffentlicht ist, an einer Quelle, die eine Küche öffnen kann.' },
      { title: 'Eine Zahl hat eine Quelle, oder wir nennen sie Schätzung', body: 'Ohne Quelle steht das auf der Seite. Wir erfinden keine lokalen Mieten, Bußgelder oder Personalzahlen.' },
      { title: 'Ein Mensch liest gegen', body: 'Ein Entwurf darf mit KI beginnen. Ein Koch oder ein Redakteur prüft, ob der Schritt am Pass hält.' },
      { title: 'KI-Bilder sind Referenzbilder', body: 'Ein generiertes Bild ist als Referenz gekennzeichnet. Wir geben es nicht als Foto eines echten Tellers oder Gastraums aus.' },
      { title: 'Korrekturen bleiben sichtbar', body: 'Wenn wir einen Fehler korrigieren, notieren wir Änderung und Datum.' },
      { title: 'Schreiben Sie uns, wenn eine Zeile falsch ist', body: 'Schicken Sie Seite und Satz an info@aichef.pro. Eine Person liest.' },
    ],
    blocks: [
      {
        id: 'john',
        h2: 'Wer John Guerrero ist',
        answer:
          'Er hat den Beruf im Service gelernt, nicht aus einem Software-Lastenheft. Neunundzwanzig Jahre Gastronomie, Beratung seit 2010 mit ChefBusiness.',
        paragraphs: [
          'Dieselben Betriebsprobleme tauchten in sehr verschiedenen Häusern auf: ein Wareneinsatz, für den niemand zuständig war, eine Karte, die nicht zu den Bestellungen passte, ein Ablauf, der nur in einem Kopf steckte. AI Chef Pro ist seine Antwort: Agenten, die Küchenaufgaben sprechen, im Browser.',
          'Seine persönliche Seite ist johnguerrero.es. Der YouTube-Kanal ist @aichefpro. Presse und Korrekturen: info@aichef.pro.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Was ist AI Chef Pro?',
        a: 'Eine Suite spezialisierter Agenten für die Gastronomie: Kalkulation, Karte, Allergene, Inhalte und lokale Suche. Die deutsche Preisseite nennt heute mehr als 50 Agenten. Der Mitgliedsplan kostet 10 € im Monat mit 10.000 Credits, ohne Bindung.',
      },
      {
        q: 'Wer hat das gegründet?',
        a: 'John Guerrero, seit dem 17. Lebensjahr in der Küche, Berater seit 2010, Gründer von ChefBusiness.',
      },
      {
        q: 'Wie entsteht der Blog?',
        a: 'Recherche vor der Veröffentlichung, Quelle oder Hinweis auf eine Schätzung, menschliche Gegenlese, KI-Bilder als Referenz gekennzeichnet, Korrekturen mit Datum. Schreiben Sie an info@aichef.pro, wenn eine Zeile falsch ist.',
      },
    ],
    ctaTitle: 'Die Preisseite ist die Quelle der Preise',
    ctaBody: 'Die tatsächliche Agentenliste ist die, die Sie nach der Anmeldung in deapp.aichef.pro sehen.',
    ctaPrimary: 'Zur App',
    ctaSecondary: 'Preise ansehen',
  },
  it: {
    title: 'Chi siamo: AI Chef Pro e lo chef John Guerrero',
    description:
      'AI Chef Pro è la suite dello chef John Guerrero: in cucina dai 17 anni, consulente dal 2010, 29 anni di ristorazione, fondatore di ChefBusiness.',
    keywords: 'chi siamo AI Chef Pro, John Guerrero chef, ChefBusiness, fondatore AI Chef Pro',
    eyebrow: 'Chi siamo',
    h1: 'Uno strumento di cucina fatto da chi ha tenuto un passe',
    lead: 'AI Chef Pro è la suite di John Guerrero per le cucine professionali, nel gruppo ChefBusiness.',
    answerLabel: 'Risposta diretta',
    answer:
      'John Guerrero è in cucina professionale dai 17 anni e consulente gastronomico dal 2010. Ha 29 anni di mestiere e ha fondato il gruppo ChefBusiness. AI Chef Pro è la suite che ha costruito per i cuochi. La pagina prezzi in italiano indica oggi più di 50 agenti; lo spazio spagnolo ne pubblica 75+. Il piano Membro costa 10 € al mese con 10.000 crediti.',
    homeLabel: 'Home',
    crumb: 'Chi siamo',
    faqHeading: 'Domande',
    chips: [
      'Fondatore e CEO di AI Chef Pro',
      'Fondatore del gruppo ChefBusiness',
      'In cucina dai 17 anni',
      'Consulente dal 2010',
    ],
    stats: [
      { big: '50+', label: 'Agenti indicati sulla pagina prezzi IT' },
      { big: '7', label: 'Lingue, spagnolo d’origine' },
      { big: '10.000', label: 'Crediti del piano Membro' },
      { big: '10 €', label: 'Al mese, senza permanenza' },
    ],
    plans: [
      { name: 'Membro', price: '10 €/mese', detail: '10.000 crediti · senza permanenza' },
      { name: 'Premium Pro', price: '25 €/mese', detail: '85.000 crediti' },
      { name: 'Premium Plus', price: '50 €/mese', detail: '175.000 crediti' },
      { name: 'Premium Max', price: '95 €/mese', detail: 'Crediti illimitati' },
      { name: 'Max annuale', price: '950 €/anno', detail: 'Illimitati · due mesi in meno di 12 × 95 €' },
    ],
    plansHeading: 'Piani, in euro',
    standardsHeading: 'Come pubblichiamo',
    standards: [
      { title: 'Prima si cerca', body: 'Guardiamo il tema e ciò che è già pubblicato, e controlliamo le affermazioni con una fonte che una cucina può aprire.' },
      { title: 'Una cifra ha una fonte, oppure diciamo che è una stima', body: 'Senza fonte, la pagina lo dice. Non inventiamo affitti, sanzioni o organici locali.' },
      { title: 'Una persona rilegge', body: 'Una bozza può partire con l’IA. Un cuoco o un editor verifica che il gesto tenga al passe.' },
      { title: 'Le immagini IA sono di riferimento', body: 'Un’immagine generata è marcata come riferimento. Non la facciamo passare per la foto di un piatto o di una sala veri.' },
      { title: 'Le correzioni restano visibili', body: 'Quando correggiamo un errore annotiamo il cambiamento e la data.' },
      { title: 'Scrivici se una riga è sbagliata', body: 'Manda pagina e frase a info@aichef.pro. Legge una persona.' },
    ],
    blocks: [
      {
        id: 'john',
        h2: 'Chi è John Guerrero',
        answer:
          'Ha imparato il mestiere in servizio, non da un brief software. Ventinove anni di ristorazione, consulenza dal 2010 con ChefBusiness.',
        paragraphs: [
          'Gli stessi problemi tornavano in locali molto diversi: un food cost di cui nessuno era responsabile, un menu che non seguiva le comande, un processo che stava nella testa di una sola persona. AI Chef Pro è la sua risposta: agenti che parlano i compiti di cucina, nel browser.',
          'Il suo sito personale è johnguerrero.es. Il canale YouTube è @aichefpro. Stampa e correzioni: info@aichef.pro.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Che cos’è AI Chef Pro?',
        a: 'Una suite di agenti specializzati per la ristorazione: schede, menu, allergeni, contenuti e ricerca locale. La pagina prezzi italiana indica oggi più di 50 agenti. Il piano Membro costa 10 € al mese con 10.000 crediti, senza permanenza.',
      },
      {
        q: 'Chi l’ha fondato?',
        a: 'John Guerrero, in cucina dai 17 anni, consulente dal 2010, fondatore di ChefBusiness.',
      },
      {
        q: 'Come scrivete il blog?',
        a: 'Ricerca prima di pubblicare, fonte o avviso di stima, rilettura umana, immagini IA marcate come riferimento, correzioni datate. Scrivi a info@aichef.pro se una riga è sbagliata.',
      },
    ],
    ctaTitle: 'La pagina prezzi è la fonte dei prezzi',
    ctaBody: 'L’elenco reale degli agenti è quello che vedi dopo l’accesso su itapp.aichef.pro.',
    ctaPrimary: 'Apri l’app',
    ctaSecondary: 'Vedi i prezzi',
  },
  pt: {
    title: 'Sobre o AI Chef Pro e o chef John Guerrero',
    description:
      'O AI Chef Pro é a suite do chef John Guerrero: na cozinha desde os 17 anos, consultor desde 2010, 29 anos de restauração, fundador da ChefBusiness. Site em português de Portugal.',
    keywords: 'sobre AI Chef Pro, John Guerrero chef, ChefBusiness, fundador AI Chef Pro',
    eyebrow: 'Sobre',
    h1: 'Uma ferramenta de cozinha feita por quem segurou um passe',
    lead: 'O AI Chef Pro é a suite de John Guerrero para cozinhas profissionais, no grupo ChefBusiness.',
    answerLabel: 'Resposta direta',
    answer:
      'John Guerrero está na cozinha profissional desde os 17 anos e é consultor gastronómico desde 2010. Tem 29 anos de ofício e fundou o grupo ChefBusiness. O AI Chef Pro é a suite que construiu para cozinheiros. A página de preços em português indica hoje mais de 50 agentes; o espaço espanhol publica 75+. O plano Membro custa 10 € por mês com 10.000 créditos.',
    homeLabel: 'Início',
    crumb: 'Sobre',
    faqHeading: 'Perguntas',
    chips: [
      'Fundador e CEO do AI Chef Pro',
      'Fundador do grupo ChefBusiness',
      'Na cozinha desde os 17 anos',
      'Consultor desde 2010',
    ],
    stats: [
      { big: '50+', label: 'Agentes na página de preços PT' },
      { big: '7', label: 'Línguas, espanhol de origem' },
      { big: '10.000', label: 'Créditos do plano Membro' },
      { big: '10 €', label: 'Por mês, sem permanência' },
    ],
    plans: [
      { name: 'Membro', price: '10 €/mês', detail: '10.000 créditos · sem permanência' },
      { name: 'Premium Pro', price: '25 €/mês', detail: '85.000 créditos' },
      { name: 'Premium Plus', price: '50 €/mês', detail: '175.000 créditos' },
      { name: 'Premium Max', price: '95 €/mês', detail: 'Créditos ilimitados' },
      { name: 'Max anual', price: '950 €/ano', detail: 'Ilimitados · dois meses a menos do que 12 × 95 €' },
    ],
    plansHeading: 'Planos, em euros',
    standardsHeading: 'Como publicamos',
    standards: [
      { title: 'Primeiro pesquisa-se', body: 'Olhamos o tema e o que já está publicado, e confirmamos as afirmações com uma fonte que uma cozinha consegue abrir.' },
      { title: 'Um número tem fonte, ou dizemos que é uma estimativa', body: 'Sem fonte, a página diz isso. Não inventamos rendas, coimas nem quadros de pessoal locais.' },
      { title: 'Uma pessoa revê', body: 'Um rascunho pode começar com IA. Um cozinheiro ou um editor confirma que o gesto aguenta o passe.' },
      { title: 'Imagens de IA são de referência', body: 'Uma imagem gerada fica marcada como referência. Não a apresentamos como fotografia de um prato ou de uma sala reais.' },
      { title: 'As correções ficam visíveis', body: 'Quando corrigimos um erro, anotamos a alteração e a data.' },
      { title: 'Escreve-nos se uma linha estiver errada', body: 'Envia a página e a frase para info@aichef.pro. Lê uma pessoa.' },
    ],
    blocks: [
      {
        id: 'john',
        h2: 'Quem é John Guerrero',
        answer:
          'Aprendeu o ofício em serviço, não num caderno de encargos de software. Vinte e nove anos de restauração, consultoria desde 2010 com a ChefBusiness.',
        paragraphs: [
          'Os mesmos problemas voltavam em salas muito diferentes: um food cost sem dono, uma carta que não seguia o que se vendia, um processo que vivia na cabeça de uma só pessoa. O AI Chef Pro é a resposta dele: agentes que falam tarefas de cozinha, no browser.',
          'O site pessoal é johnguerrero.es. O canal de YouTube é @aichefpro. Imprensa e correções: info@aichef.pro. O português deste site é de Portugal.',
        ],
      },
    ],
    faqs: [
      {
        q: 'O que é o AI Chef Pro?',
        a: 'Uma suite de agentes especializados para a restauração: fichas, carta, alergénios, conteúdo e pesquisa local. A página de preços em português indica hoje mais de 50 agentes. O plano Membro custa 10 € por mês com 10.000 créditos, sem permanência.',
      },
      {
        q: 'Quem fundou o projeto?',
        a: 'John Guerrero, na cozinha desde os 17 anos, consultor desde 2010, fundador da ChefBusiness.',
      },
      {
        q: 'Como escrevem o blogue?',
        a: 'Pesquisa antes de publicar, fonte ou aviso de estimativa, revisão humana, imagens de IA marcadas como referência, correções com data. Escreve para info@aichef.pro se uma linha estiver errada.',
      },
    ],
    ctaTitle: 'A página de preços é a fonte dos preços',
    ctaBody: 'A lista real de agentes é a que vês depois de entrares em ptapp.aichef.pro.',
    ctaPrimary: 'Abrir a app',
    ctaSecondary: 'Ver preços',
  },
  nl: {
    title: 'Over AI Chef Pro en chef John Guerrero',
    description:
      'AI Chef Pro is de suite van chef John Guerrero: sinds zijn 17e in de keuken, adviseur sinds 2010, 29 jaar horeca, oprichter van ChefBusiness.',
    keywords: 'over AI Chef Pro, John Guerrero chef, ChefBusiness, oprichter AI Chef Pro',
    eyebrow: 'Over ons',
    h1: 'Een keukentool van iemand die op de pass heeft gestaan',
    lead: 'AI Chef Pro is de suite van John Guerrero voor professionele keukens, binnen de groep ChefBusiness.',
    answerLabel: 'Kort antwoord',
    answer:
      'John Guerrero werkt sinds zijn 17e in de professionele keuken en is sinds 2010 gastronomisch adviseur. Hij heeft 29 jaar horeca achter zich en richtte de groep ChefBusiness op. AI Chef Pro is de suite die hij voor koks bouwde. De Nederlandse prijspagina noemt vandaag meer dan 50 agenten; de Spaanse werkruimte publiceert 75+. Het Lid-abonnement kost € 10 per maand met 10.000 credits.',
    homeLabel: 'Home',
    crumb: 'Over ons',
    faqHeading: 'Vragen',
    chips: [
      'Oprichter en CEO van AI Chef Pro',
      'Oprichter van de groep ChefBusiness',
      'Sinds zijn 17e in de keuken',
      'Adviseur sinds 2010',
    ],
    stats: [
      { big: '50+', label: 'Agenten op de Nederlandse prijspagina' },
      { big: '7', label: 'Talen, Spaans als oorsprong' },
      { big: '10.000', label: 'Credits in het Lid-abonnement' },
      { big: '€ 10', label: 'Per maand, zonder contractduur' },
    ],
    plans: [
      { name: 'Lid', price: '€ 10/maand', detail: '10.000 credits · zonder contractduur' },
      { name: 'Premium Pro', price: '€ 25/maand', detail: '85.000 credits' },
      { name: 'Premium Plus', price: '€ 50/maand', detail: '175.000 credits' },
      { name: 'Premium Max', price: '€ 95/maand', detail: 'Onbeperkte credits' },
      { name: 'Max jaar', price: '€ 950/jaar', detail: 'Onbeperkt · twee maanden minder dan 12 × € 95' },
    ],
    plansHeading: 'Abonnementen, in euro',
    standardsHeading: 'Hoe we publiceren',
    standards: [
      { title: 'Eerst uitzoeken', body: 'We bekijken het onderwerp en wat er al staat, en we toetsen beweringen aan een bron die een keuken kan openen.' },
      { title: 'Een cijfer heeft een bron, of we noemen het een schatting', body: 'Zonder bron staat dat op de pagina. We verzinnen geen lokale huren, boetes of bezettingen.' },
      { title: 'Een mens leest na', body: 'Een concept mag met AI beginnen. Een kok of een redacteur controleert of de stap op de pass houdt.' },
      { title: 'AI-beelden zijn referentiebeelden', body: 'Een gegenereerd beeld is als referentie gemarkeerd. We presenteren het niet als foto van een echt bord of een echte zaak.' },
      { title: 'Correcties blijven zichtbaar', body: 'Als we een fout verbeteren, noteren we de wijziging en de datum.' },
      { title: 'Mail ons als een zin niet klopt', body: 'Stuur de pagina en de zin naar info@aichef.pro. Een persoon leest het.' },
    ],
    blocks: [
      {
        id: 'john',
        h2: 'Wie John Guerrero is',
        answer:
          'Hij leerde het vak in de dienst, niet uit een softwarebrief. Negenentwintig jaar horeca, advies sinds 2010 met ChefBusiness.',
        paragraphs: [
          'Dezelfde problemen kwamen terug in heel verschillende zaken: een foodcost waar niemand eigenaar van was, een kaart die niet volgde wat er besteld werd, een proces dat in één hoofd zat. AI Chef Pro is zijn antwoord: agenten die keukentaken spreken, in de browser.',
          'Zijn persoonlijke site is johnguerrero.es. Het YouTube-kanaal is @aichefpro. Pers en correcties: info@aichef.pro.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Wat is AI Chef Pro?',
        a: 'Een suite van gespecialiseerde agenten voor de horeca: kostprijs, kaart, allergenen, content en lokale zoekopdrachten. De Nederlandse prijspagina noemt vandaag meer dan 50 agenten. Lid kost € 10 per maand met 10.000 credits, zonder contractduur.',
      },
      {
        q: 'Wie heeft het opgericht?',
        a: 'John Guerrero, sinds zijn 17e in de keuken, adviseur sinds 2010, oprichter van ChefBusiness.',
      },
      {
        q: 'Hoe schrijven jullie de blog?',
        a: 'Onderzoek vóór publicatie, een bron of het label schatting, een menselijke nalezing, AI-beelden als referentie, correcties met datum. Mail info@aichef.pro als een zin niet klopt.',
      },
    ],
    ctaTitle: 'De prijspagina is de bron van de prijzen',
    ctaBody: 'De echte lijst met agenten is wat je ziet nadat je inlogt op nlapp.aichef.pro.',
    ctaPrimary: 'Open de app',
    ctaSecondary: 'Bekijk de prijzen',
  },
};
