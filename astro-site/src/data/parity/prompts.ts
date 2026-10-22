import type { PageCopy, PromptLang } from './types';

const catalogs = [
  {
    href: '/libreria-de-prompts',
    title: 'Spanish catalog',
    body: 'The Spanish hub lists the full menu of the Spanish workspace. It is the largest published catalog. Names there are Spanish.',
  },
  {
    href: '/en/prompt-libraries',
    title: 'English catalog: 26 verified libraries',
    body: 'The English hub lists only the 26 prompt libraries whose names were checked one by one. It is not the full Spanish menu, so the two pages are not translations of each other.',
  },
];

export const PROMPTS: Record<PromptLang, PageCopy> = {
  fr: {
    title: 'Agents IA : bibliothèques de prompts | AI Chef Pro',
    description:
      'Agents IA pour la cuisine : la suite en publie 75+. Cette page explique les prompts et ouvre les catalogues en espagnol et en anglais. Consultez-les.',
    keywords: 'bibliothèque de prompts restauration, prompts cuisine professionnelle, prompts IA restaurant, prompt chef',
    eyebrow: 'Prompts',
    h1: 'Des prompts de cuisine, pas un chatbot généraliste',
    lead: 'Une bibliothèque de prompts est un lot de consignes prêtes pour un agent précis : fiche technique, carte, allergènes, contenu.',
    answerLabel: 'Réponse directe',
    answer:
      'Les deux catalogues que vous pouvez lire sans vous connecter sont la bibliothèque espagnole (menu complet de l’espace espagnol) et la bibliothèque anglaise (26 bibliothèques dont les noms ont été vérifiés). Cette page en français n’invente pas une troisième liste d’agents. Après connexion sur frapp.aichef.pro, vous voyez les agents que cet espace contient aujourd’hui. La page tarifs française indique 75+ agents.',
    homeLabel: 'Accueil',
    crumb: 'Bibliothèques de prompts',
    faqHeading: 'Questions',
    catalogs: [
      { ...catalogs[0], title: 'Catalogue espagnol', body: 'Le hub espagnol liste le menu complet de l’espace espagnol. C’est le catalogue publié le plus large. Les noms y sont en espagnol.' },
      { ...catalogs[1], title: 'Catalogue anglais : 26 bibliothèques vérifiées', body: 'Le hub anglais ne liste que les 26 bibliothèques dont le nom a été vérifié une par une. Ce n’est pas le menu espagnol, donc les deux pages ne sont pas des traductions l’une de l’autre.' },
    ],
    blocks: [
      {
        id: 'usage',
        h2: 'À quoi sert un prompt en cuisine',
        answer:
          'Un prompt utile nomme le plat, les portions, le coût matière visé et la contrainte (allergène, matériel, service). Un prompt vague produit une recette de blog.',
        bullets: [
          'Fiche technique et food cost : portions, prix d’achat, rendement.',
          'Carte : intitulé, description, engineering de menu.',
          'Allergènes : les 14 de l’annexe II, pas une liste inventée.',
          'Contenu : un post qui parle du plat du jour, pas d’une marque générique.',
        ],
      },
      {
        id: 'espace',
        h2: 'Ce que vous ouvrez en français',
        answer:
          'L’espace de travail est frapp.aichef.pro. Les noms d’agents y sont localisés. Nous ne recopions pas ici une liste que le dépôt n’a pas vérifiée pour le français.',
        paragraphs: [
          'Si un agent que vous cherchez n’apparaît pas après connexion, il n’est pas encore dans cet espace. L’espace espagnol reste le plus complet.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Pourquoi cette page n’est-elle pas la traduction du hub espagnol ?',
        a: 'Parce que le hub espagnol et le hub anglais n’ont pas le même périmètre. Déclarer un hreflang entre une porte d’entrée française et un catalogue de 26 bibliothèques anglaises serait faux. Les liens vers les deux catalogues sont visibles sur cette page.',
      },
      {
        q: 'Où sont les prompts une fois le compte ouvert ?',
        a: 'Dans frapp.aichef.pro, sur l’agent concerné. Cette page explique le geste. Elle ne vend pas un ebook et ne liste pas des noms d’agents non vérifiés.',
      },
    ],
    ctaTitle: 'Ouvrez l’espace français',
    ctaBody: 'Le forfait Membre est à 10 € par mois avec 10 000 crédits. La liste d’agents est celle de l’espace après connexion.',
    ctaPrimary: 'Ouvrir l’application',
    ctaSecondary: 'Voir les tarifs',
  },
  de: {
    title: 'KI-Agenten: Prompt-Bibliotheken der Küche | AI Chef Pro',
    description:
      'KI-Agenten mit Prompt-Bibliotheken für die Küche: die Suite nennt 75+. Diese Seite erklärt die Prompts und öffnet die Kataloge auf Spanisch und Englisch.',
    keywords: 'Prompt Bibliothek Gastronomie, Prompts Profiküche, KI Prompts Restaurant, Prompt Koch',
    eyebrow: 'Prompts',
    h1: 'Küchen-Prompts, kein allgemeiner Chatbot',
    lead: 'Eine Prompt-Bibliothek ist ein Satz fertiger Anweisungen für einen bestimmten Agenten: Kalkulation, Karte, Allergene, Inhalte.',
    answerLabel: 'Kurzantwort',
    answer:
      'Die zwei Kataloge, die Sie ohne Anmeldung lesen können, sind die spanische Bibliothek (volles Menü des spanischen Arbeitsbereichs) und die englische Bibliothek (26 Bibliotheken, deren Namen einzeln geprüft wurden). Diese deutsche Seite erfindet keine dritte Agentenliste. Nach der Anmeldung in deapp.aichef.pro sehen Sie die Agenten, die dieser Bereich heute enthält. Die deutsche Preisseite nennt 75+ Agenten.',
    homeLabel: 'Startseite',
    crumb: 'Prompt-Bibliotheken',
    faqHeading: 'Fragen',
    catalogs: [
      { ...catalogs[0], title: 'Spanischer Katalog', body: 'Der spanische Hub listet das volle Menü des spanischen Arbeitsbereichs. Das ist der größte veröffentlichte Katalog. Die Namen sind spanisch.' },
      { ...catalogs[1], title: 'Englischer Katalog: 26 geprüfte Bibliotheken', body: 'Der englische Hub listet nur die 26 Bibliotheken, deren Namen einzeln geprüft wurden. Das ist nicht das spanische Menü. Die beiden Seiten sind keine Übersetzungen voneinander.' },
    ],
    blocks: [
      {
        id: 'nutzen',
        h2: 'Wofür ein Prompt in der Küche da ist',
        answer:
          'Ein brauchbarer Prompt nennt das Gericht, die Portionen, den Ziel-Wareneinsatz und die Grenze (Allergen, Gerät, Service). Ein vager Prompt liefert ein Blogrezept.',
        bullets: [
          'Kalkulation: Portionen, Einkaufspreis, Ausbeute.',
          'Karte: Name, Beschreibung, Menu Engineering.',
          'Allergene: die 14 aus Anhang II, keine erfundene Liste.',
          'Inhalte: ein Beitrag über das Tagesgericht, nicht über eine generische Marke.',
        ],
      },
      {
        id: 'bereich',
        h2: 'Was Sie auf Deutsch öffnen',
        answer:
          'Der Arbeitsbereich ist deapp.aichef.pro. Agentennamen sind dort lokalisiert. Wir kopieren hier keine Liste, die das Repository für Deutsch nicht geprüft hat.',
        paragraphs: [
          'Fehlt ein Agent nach der Anmeldung, ist er in diesem Bereich noch nicht enthalten. Der spanische Bereich bleibt der vollständigste.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Warum ist diese Seite nicht die Übersetzung des spanischen Hubs?',
        a: 'Weil der spanische Hub und der englische Hub nicht denselben Umfang haben. Ein hreflang zwischen einem deutschen Einstieg und einem Katalog von 26 englischen Bibliotheken wäre falsch. Die Links zu beiden Katalogen stehen auf dieser Seite.',
      },
      {
        q: 'Wo liegen die Prompts nach dem Login?',
        a: 'In deapp.aichef.pro, beim jeweiligen Agenten. Diese Seite erklärt den Handgriff. Sie verkauft kein E-Book und nennt keine ungeprüften Agentennamen.',
      },
    ],
    ctaTitle: 'Öffnen Sie den deutschen Bereich',
    ctaBody: 'Der Mitgliedsplan kostet 10 € im Monat mit 10.000 Credits. Die Agentenliste ist die nach der Anmeldung.',
    ctaPrimary: 'Zur App',
    ctaSecondary: 'Preise ansehen',
  },
  it: {
    title: 'Agenti IA: librerie di prompt per la cucina | AI Chef Pro',
    description:
      'Agenti IA con librerie di prompt pronte da copiare: la suite pubblica 75+. Questa pagina spiega i prompt e apre i cataloghi in spagnolo e in inglese.',
    keywords: 'libreria di prompt ristorazione, prompt cucina professionale, prompt IA ristorante, prompt chef',
    eyebrow: 'Prompt',
    h1: 'Prompt di cucina, non un chatbot generico',
    lead: 'Una libreria di prompt è un set di consegne pronte per un agente preciso: scheda costo, menu, allergeni, contenuti.',
    answerLabel: 'Risposta diretta',
    answer:
      'I due cataloghi che puoi leggere senza entrare sono la libreria spagnola (menu completo dello spazio spagnolo) e la libreria inglese (26 librerie i cui nomi sono stati verificati uno per uno). Questa pagina italiana non inventa una terza lista di agenti. Dopo l’accesso su itapp.aichef.pro vedi gli agenti che quello spazio contiene oggi. La pagina prezzi italiana indica 75+ agenti.',
    homeLabel: 'Home',
    crumb: 'Librerie di prompt',
    faqHeading: 'Domande',
    catalogs: [
      { ...catalogs[0], title: 'Catalogo spagnolo', body: 'L’hub spagnolo elenca il menu completo dello spazio spagnolo. È il catalogo pubblicato più ampio. I nomi sono in spagnolo.' },
      { ...catalogs[1], title: 'Catalogo inglese: 26 librerie verificate', body: 'L’hub inglese elenca solo le 26 librerie il cui nome è stato verificato una per una. Non è il menu spagnolo, quindi le due pagine non sono traduzioni una dell’altra.' },
    ],
    blocks: [
      {
        id: 'uso',
        h2: 'A che serve un prompt in cucina',
        answer:
          'Un prompt utile nomina il piatto, le porzioni, il food cost obiettivo e il vincolo (allergene, attrezzatura, servizio). Un prompt vago produce una ricetta da blog.',
        bullets: [
          'Scheda tecnica e food cost: porzioni, prezzo d’acquisto, resa.',
          'Menu: nome, descrizione, menu engineering.',
          'Allergeni: i 14 dell’allegato II, non una lista inventata.',
          'Contenuti: un post sul piatto del giorno, non su un marchio generico.',
        ],
      },
      {
        id: 'spazio',
        h2: 'Che cosa apri in italiano',
        answer:
          'Lo spazio di lavoro è itapp.aichef.pro. I nomi degli agenti lì sono localizzati. Qui non copiamo una lista che il repository non ha verificato per l’italiano.',
        paragraphs: [
          'Se un agente che cerchi non compare dopo l’accesso, non è ancora in questo spazio. Lo spazio spagnolo resta il più completo.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Perché questa pagina non è la traduzione dell’hub spagnolo?',
        a: 'Perché l’hub spagnolo e l’hub inglese non hanno lo stesso perimetro. Un hreflang tra una porta italiana e un catalogo di 26 librerie inglesi sarebbe falso. I link ai due cataloghi sono su questa pagina.',
      },
      {
        q: 'Dove stanno i prompt a conto aperto?',
        a: 'In itapp.aichef.pro, sull’agente giusto. Questa pagina spiega il gesto. Non vende un ebook e non elenca nomi di agenti non verificati.',
      },
    ],
    ctaTitle: 'Apri lo spazio italiano',
    ctaBody: 'Il piano Membro costa 10 € al mese con 10.000 crediti. La lista agenti è quella dello spazio dopo l’accesso.',
    ctaPrimary: 'Apri l’app',
    ctaSecondary: 'Vedi i prezzi',
  },
  pt: {
    title: 'Agentes de IA: bibliotecas de prompts | AI Chef Pro',
    description:
      'Agentes de IA com bibliotecas de prompts prontas a copiar: a suite publica 75+. Esta página explica os prompts e abre os catálogos em espanhol e inglês.',
    keywords: 'biblioteca de prompts restauração, prompts cozinha profissional, prompts IA restaurante, prompt chef',
    eyebrow: 'Prompts',
    h1: 'Prompts de cozinha, não um chatbot genérico',
    lead: 'Uma biblioteca de prompts é um conjunto de instruções prontas para um agente concreto: ficha técnica, carta, alergénios, conteúdo.',
    answerLabel: 'Resposta direta',
    answer:
      'Os dois catálogos que podes ler sem entrar são a biblioteca espanhola (menu completo do espaço espanhol) e a biblioteca inglesa (26 bibliotecas cujos nomes foram verificados um a um). Esta página em português não inventa uma terceira lista de agentes. Depois de entrares em ptapp.aichef.pro, vês os agentes que esse espaço tem hoje. A página de preços em português indica 75+ agentes.',
    homeLabel: 'Início',
    crumb: 'Bibliotecas de prompts',
    faqHeading: 'Perguntas',
    catalogs: [
      { ...catalogs[0], title: 'Catálogo espanhol', body: 'O hub espanhol lista o menu completo do espaço espanhol. É o catálogo publicado mais largo. Os nomes estão em espanhol.' },
      { ...catalogs[1], title: 'Catálogo inglês: 26 bibliotecas verificadas', body: 'O hub inglês lista só as 26 bibliotecas cujo nome foi verificado um a um. Não é o menu espanhol, por isso as duas páginas não são traduções uma da outra.' },
    ],
    blocks: [
      {
        id: 'uso',
        h2: 'Para que serve um prompt na cozinha',
        answer:
          'Um prompt útil nomeia o prato, as doses, o food cost alvo e o constrangimento (alergénio, equipamento, serviço). Um prompt vago produz uma receita de blogue.',
        bullets: [
          'Ficha técnica e food cost: doses, preço de compra, rendimento.',
          'Carta: nome, descrição, engenharia de menu.',
          'Alergénios: os 14 do anexo II, não uma lista inventada.',
          'Conteúdo: um post sobre o prato do dia, não sobre uma marca genérica.',
        ],
      },
      {
        id: 'espaco',
        h2: 'O que abres em português',
        answer:
          'O espaço de trabalho é ptapp.aichef.pro. Os nomes dos agentes ali estão localizados. Aqui não copiamos uma lista que o repositório não verificou para português de Portugal.',
        paragraphs: [
          'Se um agente que procuras não aparece depois de entrares, ainda não está neste espaço. O espaço espanhol continua a ser o mais completo.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Porque é que esta página não é a tradução do hub espanhol?',
        a: 'Porque o hub espanhol e o hub inglês não têm o mesmo âmbito. Um hreflang entre uma porta em português e um catálogo de 26 bibliotecas inglesas seria falso. As ligações para os dois catálogos estão nesta página.',
      },
      {
        q: 'Onde ficam os prompts com a conta aberta?',
        a: 'Em ptapp.aichef.pro, no agente certo. Esta página explica o gesto. Não vende um ebook e não lista nomes de agentes por verificar.',
      },
    ],
    ctaTitle: 'Abre o espaço em português',
    ctaBody: 'O plano Membro custa 10 € por mês com 10.000 créditos. A lista de agentes é a do espaço depois de entrares.',
    ctaPrimary: 'Abrir a app',
    ctaSecondary: 'Ver preços',
  },
  nl: {
    title: 'AI-agenten: promptbibliotheken voor de keuken | AI Chef Pro',
    description:
      'AI-agenten met promptbibliotheken voor de keuken: de suite noemt 75+. Deze pagina legt de prompts uit en opent de catalogi in het Spaans en het Engels.',
    keywords: 'promptbibliotheek horeca, prompts professionele keuken, AI prompts restaurant, prompt kok',
    eyebrow: 'Prompts',
    h1: 'Keukenprompts, geen algemene chatbot',
    lead: 'Een promptbibliotheek is een set kant-en-klare opdrachten voor één agent: kostprijs, kaart, allergenen, content.',
    answerLabel: 'Kort antwoord',
    answer:
      'De twee catalogi die je zonder inloggen kunt lezen, zijn de Spaanse bibliotheek (het volledige menu van de Spaanse werkruimte) en de Engelse bibliotheek (26 bibliotheken waarvan de namen één voor één zijn gecontroleerd). Deze Nederlandse pagina verzint geen derde agentenlijst. Na het inloggen op nlapp.aichef.pro zie je de agenten die die werkruimte vandaag bevat. De Nederlandse prijspagina noemt 75+ agenten.',
    homeLabel: 'Home',
    crumb: 'Promptbibliotheken',
    faqHeading: 'Vragen',
    catalogs: [
      { ...catalogs[0], title: 'Spaanse catalogus', body: 'De Spaanse hub toont het volledige menu van de Spaanse werkruimte. Dat is de grootste gepubliceerde catalogus. De namen zijn Spaans.' },
      { ...catalogs[1], title: 'Engelse catalogus: 26 gecontroleerde bibliotheken', body: 'De Engelse hub toont alleen de 26 bibliotheken waarvan de naam één voor één is gecontroleerd. Dat is niet het Spaanse menu. De twee pagina’s zijn geen vertalingen van elkaar.' },
    ],
    blocks: [
      {
        id: 'gebruik',
        h2: 'Waar een prompt in de keuken voor dient',
        answer:
          'Een bruikbare prompt noemt het gerecht, de porties, de gewenste foodcost en de grens (allergeen, apparatuur, service). Een vage prompt levert een blogrecept.',
        bullets: [
          'Kostprijs: porties, inkoopprijs, rendement.',
          'Kaart: naam, omschrijving, menu engineering.',
          'Allergenen: de 14 uit bijlage II, geen verzonnen lijst.',
          'Content: een bericht over het dagmenu, niet over een generiek merk.',
        ],
      },
      {
        id: 'ruimte',
        h2: 'Wat je in het Nederlands opent',
        answer:
          'De werkruimte is nlapp.aichef.pro. Agentnamen zijn daar gelokaliseerd. We kopiëren hier geen lijst die de repository voor het Nederlands niet heeft gecontroleerd.',
        paragraphs: [
          'Staat een agent er na het inloggen niet bij, dan zit hij nog niet in deze werkruimte. De Spaanse werkruimte blijft de meest complete.',
        ],
      },
    ],
    faqs: [
      {
        q: 'Waarom is deze pagina niet de vertaling van de Spaanse hub?',
        a: 'Omdat de Spaanse hub en de Engelse hub niet dezelfde omvang hebben. Een hreflang tussen een Nederlandse ingang en een catalogus van 26 Engelse bibliotheken zou onjuist zijn. De links naar beide catalogi staan op deze pagina.',
      },
      {
        q: 'Waar staan de prompts als je bent ingelogd?',
        a: 'In nlapp.aichef.pro, bij de juiste agent. Deze pagina legt de handeling uit. Ze verkoopt geen ebook en noemt geen ongecontroleerde agentnamen.',
      },
    ],
    ctaTitle: 'Open de Nederlandse werkruimte',
    ctaBody: 'Het Lid-abonnement kost € 10 per maand met 10.000 credits. De agentenlijst is die van de werkruimte na het inloggen.',
    ctaPrimary: 'Open de app',
    ctaSecondary: 'Bekijk de prijzen',
  },
};
