import type { PageCopy, ParityLang } from './types';

const support =
  'Support is fluent in Spanish and English. If you write in another language we will do our best to answer.';

export const CONTACT: Record<ParityLang, PageCopy> = {
  en: {
    title: 'Contact and Support — AI Chef Pro',
    description:
      'Contact AI Chef Pro at info@aichef.pro, from your account on enapp.aichef.pro, or on WhatsApp +34 744 717 942. Indicative reply: 24–48 business hours (Spain).',
    keywords: 'contact AI Chef Pro, AI Chef Pro support, AI Chef Pro email, restaurant AI help',
    eyebrow: 'Contact',
    h1: 'Talk to a person, not a ticket queue',
    lead: 'Questions about a tool, a subscription or a press request go to the same desk. John Guerrero’s team reads info@aichef.pro.',
    answerLabel: 'Direct answer',
    answer:
      'Email info@aichef.pro. If you already have an account, in-app support on enapp.aichef.pro is faster because we can see your plan. Indicative reply time is 24–48 business hours in Spain. WhatsApp +34 744 717 942 is a real person, Spanish business hours, not a bot.',
    homeLabel: 'Home',
    crumb: 'Contact',
    faqHeading: 'Contact questions',
    emailCta: 'Email info@aichef.pro',
    appCta: 'Open the app',
    waText: 'Hello, I have a question about AI Chef Pro.',
    honesty:
      'There is no contact form on this page. Write by email, from your account, or on WhatsApp, and a person answers.',
    channels: [
      {
        icon: 'mail',
        tag: 'Main channel',
        title: 'Email',
        body: 'info@aichef.pro covers product questions, billing, press and partnerships. We read it every working day.',
        meta: 'Indicative reply: 24–48 business hours (Spain)',
        cta: 'info@aichef.pro',
      },
      {
        icon: 'app',
        tag: 'You already have an account',
        title: 'In-app support',
        body: 'Signed-in support on enapp.aichef.pro is the fastest path for a technical or subscription issue: we already see the workspace and the plan.',
        meta: 'English workspace · enapp.aichef.pro',
        cta: 'Open enapp.aichef.pro',
      },
      {
        icon: 'whatsapp',
        tag: 'Short questions',
        title: 'WhatsApp',
        body: 'Use WhatsApp when a purchase is stuck and email feels slow. A person replies during Spanish business hours.',
        meta: '+34 744 717 942 · Spain business hours',
        cta: 'Open WhatsApp',
      },
    ],
    faqs: [
      {
        q: 'How do I get help if something in the platform fails?',
        a: 'Sign in on enapp.aichef.pro and write from in-app support so we can see the account. If you cannot sign in, email info@aichef.pro with the message on screen.',
      },
      {
        q: 'How do I change plan, download an invoice or cancel?',
        a: 'You do it yourself in the account panel: plan changes, tax details and cancellation, with no lock-in. Each subscription generates an invoice with the VAT that applies to your country. For a specific invoice, email info@aichef.pro from the account address.',
      },
      {
        q: 'Who do I write for press or a partnership?',
        a: 'Email info@aichef.pro with a clear subject. AI Chef Pro is John Guerrero — in kitchens since he was 17, gastronomic consultant since 2010 — and the ChefBusiness group.',
      },
      {
        q: 'Which languages do you answer in?',
        a: support + ' The product itself is available in Spanish, English, French, German, Italian, Portuguese and Dutch. Prices on this site stay in euro.',
      },
      {
        q: 'Is there a published refund policy?',
        a: 'There is no published refund policy for the subscription. We look at each case by email. You can cancel any time from the account panel; there is no lock-in. Digital products state their own guarantee on the product page.',
      },
    ],
    blocks: [],
    ctaTitle: 'Try the suite while you decide',
    ctaBody:
      'The Member plan is €10 per month with 10,000 credits. The English pricing page includes the 75+ agents. Cancel any time.',
    ctaPrimary: 'Email info@aichef.pro',
    ctaSecondary: 'See plans and pricing',
  },
  fr: {
    title: 'Contact et assistance — AI Chef Pro',
    description:
      'Contactez AI Chef Pro : info@aichef.pro, l’assistance dans frapp.aichef.pro, ou WhatsApp +34 744 717 942. Réponse indicative sous 24 à 48 heures ouvrées (Espagne).',
    keywords: 'contacter AI Chef Pro, support AI Chef Pro, assistance restauration IA, email AI Chef Pro',
    eyebrow: 'Contact',
    h1: 'Écrivez-nous : une personne vous répond',
    lead: 'Une question sur un outil, un abonnement ou une demande presse arrive au même endroit. L’équipe de John Guerrero lit info@aichef.pro.',
    answerLabel: 'Réponse directe',
    answer:
      'Écrivez à info@aichef.pro. Si vous avez déjà un compte, l’assistance dans frapp.aichef.pro est plus rapide : nous voyons le forfait. Délai indicatif : 24 à 48 heures ouvrées, horaire espagnol. Le WhatsApp +34 744 717 942 est une personne, pas un robot.',
    homeLabel: 'Accueil',
    crumb: 'Contact',
    faqHeading: 'Questions sur le contact',
    emailCta: 'Écrire à info@aichef.pro',
    appCta: 'Ouvrir l’application',
    waText: 'Bonjour, j’ai une question sur AI Chef Pro.',
    honesty:
      'Cette page n’a pas de formulaire. Écrivez par e-mail, depuis votre compte ou sur WhatsApp : une personne répond.',
    channels: [
      {
        icon: 'mail',
        tag: 'Voie principale',
        title: 'E-mail',
        body: 'info@aichef.pro sert pour le produit, la facturation, la presse et les partenariats. Nous le lisons chaque jour ouvré.',
        meta: 'Réponse indicative : 24–48 h ouvrées (Espagne)',
        cta: 'info@aichef.pro',
      },
      {
        icon: 'app',
        tag: 'Vous avez déjà un compte',
        title: 'Assistance dans l’application',
        body: 'Depuis frapp.aichef.pro, l’assistance voit déjà l’espace français et le forfait. C’est le chemin le plus court pour un blocage technique.',
        meta: 'Espace français · frapp.aichef.pro',
        cta: 'Ouvrir frapp.aichef.pro',
      },
      {
        icon: 'whatsapp',
        tag: 'Question courte',
        title: 'WhatsApp',
        body: 'Pour un achat bloqué, le WhatsApp évite d’attendre le mail. Réponse en horaire de bureau espagnol, par une personne.',
        meta: '+34 744 717 942 · horaire espagnol',
        cta: 'Ouvrir WhatsApp',
      },
    ],
    faqs: [
      {
        q: 'Comment obtenir de l’aide si un outil ne répond pas ?',
        a: 'Connectez-vous sur frapp.aichef.pro et écrivez depuis l’assistance intégrée. Si vous ne pouvez pas vous connecter, envoyez à info@aichef.pro le message affiché à l’écran.',
      },
      {
        q: 'Comment changer de forfait, obtenir une facture ou résilier ?',
        a: 'Vous le faites vous-même dans le panneau du compte : changement de forfait, données de facturation et résiliation, sans engagement. Chaque abonnement produit une facture avec la TVA applicable à votre pays. Pour une facture précise, écrivez à info@aichef.pro depuis l’adresse du compte.',
      },
      {
        q: 'Qui contacter pour la presse ou un partenariat ?',
        a: 'Écrivez à info@aichef.pro avec un objet clair. Derrière AI Chef Pro : John Guerrero, en cuisine depuis ses 17 ans, consultant en restauration depuis 2010, et le groupe ChefBusiness.',
      },
      {
        q: 'Dans quelles langues répondez-vous ?',
        a: 'L’assistance est à l’aise en espagnol et en anglais. Dans une autre langue, nous faisons le nécessaire pour vous répondre. Le produit existe en sept langues. Les prix de ce site restent en euros.',
      },
      {
        q: 'Y a-t-il une politique de remboursement publiée ?',
        a: 'Non. Il n’y a pas de politique de remboursement publiée pour l’abonnement : chaque cas se regarde par e-mail. Vous pouvez résilier à tout moment depuis le compte, sans engagement. Les produits numériques indiquent leur propre garantie sur leur page.',
      },
    ],
    blocks: [],
    ctaTitle: 'Essayez la suite avant de trancher',
    ctaBody:
      'Le forfait Membre est à 10 € par mois, avec 10 000 crédits. La page tarifs en français indique aujourd’hui plus de 50 agents : le catalogue français est encore en cours. Vous résiliez quand vous voulez.',
    ctaPrimary: 'Écrire à info@aichef.pro',
    ctaSecondary: 'Voir les tarifs',
  },
  de: {
    title: 'Kontakt und Support — AI Chef Pro',
    description:
      'AI Chef Pro erreichen Sie unter info@aichef.pro, im Support von deapp.aichef.pro oder per WhatsApp +34 744 717 942. Richtwert: Antwort in 24–48 Stunden an Werktagen (Spanien).',
    keywords: 'AI Chef Pro Kontakt, Support Gastronomie KI, AI Chef Pro E-Mail',
    eyebrow: 'Kontakt',
    h1: 'Schreiben Sie uns: Es antwortet ein Mensch',
    lead: 'Fragen zum Werkzeug, zum Abo oder zur Presse landen am selben Tisch. Das Team von John Guerrero liest info@aichef.pro.',
    answerLabel: 'Kurzantwort',
    answer:
      'Schreiben Sie an info@aichef.pro. Mit einem Konto ist der Support in deapp.aichef.pro schneller, weil wir den Tarif sehen. Richtwert: 24–48 Stunden an spanischen Werktagen. WhatsApp +34 744 717 942 ist eine Person, keine Automatik.',
    homeLabel: 'Startseite',
    crumb: 'Kontakt',
    faqHeading: 'Fragen zum Kontakt',
    emailCta: 'E-Mail an info@aichef.pro',
    appCta: 'Zur App',
    waText: 'Guten Tag, ich habe eine Frage zu AI Chef Pro.',
    honesty:
      'Auf dieser Seite gibt es kein Formular. Schreiben Sie per E-Mail, aus dem Konto oder per WhatsApp. Es antwortet eine Person.',
    channels: [
      {
        icon: 'mail',
        tag: 'Hauptweg',
        title: 'E-Mail',
        body: 'info@aichef.pro gilt für Produkt, Rechnung, Presse und Kooperationen. Wir lesen das Postfach an jedem Werktag.',
        meta: 'Richtwert: 24–48 Stunden an Werktagen (Spanien)',
        cta: 'info@aichef.pro',
      },
      {
        icon: 'app',
        tag: 'Sie haben schon ein Konto',
        title: 'Support in der App',
        body: 'Im deutschen Arbeitsbereich deapp.aichef.pro sieht der Support Tarif und Kontext. Das ist der kürzeste Weg bei einer technischen Frage.',
        meta: 'Deutscher Arbeitsbereich · deapp.aichef.pro',
        cta: 'deapp.aichef.pro öffnen',
      },
      {
        icon: 'whatsapp',
        tag: 'Kurze Frage',
        title: 'WhatsApp',
        body: 'Wenn ein Kauf hakt, reicht WhatsApp. Antwort während der spanischen Bürozeiten, durch eine Person.',
        meta: '+34 744 717 942 · spanische Bürozeiten',
        cta: 'WhatsApp öffnen',
      },
    ],
    faqs: [
      {
        q: 'Wie bekomme ich Hilfe, wenn ein Werkzeug nicht läuft?',
        a: 'Melden Sie sich in deapp.aichef.pro an und schreiben Sie aus dem Support dort. Wenn die Anmeldung selbst scheitert, schicken Sie die Bildschirmmeldung an info@aichef.pro.',
      },
      {
        q: 'Wie wechsle ich den Tarif, lade eine Rechnung oder kündige?',
        a: 'Das erledigen Sie selbst im Konto: Tarifwechsel, Rechnungsdaten und Kündigung, ohne Laufzeitbindung. Jedes Abo erzeugt eine Rechnung mit der Mehrwertsteuer, die für Ihr Land gilt. Zu einer konkreten Rechnung schreiben Sie von der Kontoadresse an info@aichef.pro.',
      },
      {
        q: 'Wen erreiche ich für Presse oder eine Kooperation?',
        a: 'Schreiben Sie an info@aichef.pro mit klarem Betreff. Hinter AI Chef Pro steht John Guerrero — seit dem 17. Lebensjahr in der Küche, seit 2010 gastronomischer Berater — und die Gruppe ChefBusiness.',
      },
      {
        q: 'In welchen Sprachen antworten Sie?',
        a: 'Der Support antwortet sicher auf Spanisch und Englisch. In anderen Sprachen versuchen wir, verständlich zu antworten. Das Produkt gibt es in sieben Sprachen. Die Preise auf dieser Website bleiben in Euro.',
      },
      {
        q: 'Gibt es eine veröffentlichte Erstattungsregel?',
        a: 'Nein. Für das Abo ist keine Erstattungsregel veröffentlicht; wir prüfen den Einzelfall per E-Mail. Kündigen können Sie jederzeit im Konto, ohne Bindung. Digitale Produkte nennen ihre eigene Garantie auf der Produktseite.',
      },
    ],
    blocks: [],
    ctaTitle: 'Testen Sie die Suite, bevor Sie entscheiden',
    ctaBody:
      'Der Mitgliedsplan kostet 10 € im Monat mit 10.000 Credits. Die deutsche Preisseite nennt heute mehr als 50 Agenten: der Katalog wird noch ergänzt. Sie kündigen, wann Sie wollen.',
    ctaPrimary: 'E-Mail an info@aichef.pro',
    ctaSecondary: 'Preise ansehen',
  },
  it: {
    title: 'Contatti e assistenza — AI Chef Pro',
    description:
      'Contatta AI Chef Pro: info@aichef.pro, assistenza dentro itapp.aichef.pro, oppure WhatsApp +34 744 717 942. Risposta indicativa in 24–48 ore lavorative (Spagna).',
    keywords: 'contatti AI Chef Pro, assistenza AI Chef Pro, supporto ristorante IA, email AI Chef Pro',
    eyebrow: 'Contatti',
    h1: 'Scrivici: ti risponde una persona',
    lead: 'Dubbio su uno strumento, su un abbonamento o una richiesta stampa: arrivano allo stesso tavolo. Il team di John Guerrero legge info@aichef.pro.',
    answerLabel: 'Risposta diretta',
    answer:
      'Scrivi a info@aichef.pro. Se hai già un account, l’assistenza dentro itapp.aichef.pro è più rapida perché vediamo il piano. Tempo indicativo: 24–48 ore lavorative, orario spagnolo. Il WhatsApp +34 744 717 942 è una persona, non un bot.',
    homeLabel: 'Home',
    crumb: 'Contatti',
    faqHeading: 'Domande sui contatti',
    emailCta: 'Scrivi a info@aichef.pro',
    appCta: 'Apri l’app',
    waText: 'Ciao, ho una domanda su AI Chef Pro.',
    honesty:
      'Questa pagina non ha un modulo. Scrivi via email, dall’account o su WhatsApp: risponde una persona.',
    channels: [
      {
        icon: 'mail',
        tag: 'Canale principale',
        title: 'Email',
        body: 'info@aichef.pro vale per il prodotto, la fatturazione, la stampa e le collaborazioni. Lo leggiamo ogni giorno lavorativo.',
        meta: 'Risposta indicativa: 24–48 ore lavorative (Spagna)',
        cta: 'info@aichef.pro',
      },
      {
        icon: 'app',
        tag: 'Hai già un account',
        title: 'Assistenza nell’app',
        body: 'Da itapp.aichef.pro l’assistenza vede già lo spazio italiano e il piano. È la strada più corta se uno strumento si blocca.',
        meta: 'Spazio italiano · itapp.aichef.pro',
        cta: 'Apri itapp.aichef.pro',
      },
      {
        icon: 'whatsapp',
        tag: 'Domanda breve',
        title: 'WhatsApp',
        body: 'Se un acquisto si inceppa, WhatsApp evita di aspettare la mail. Risposta in orario d’ufficio spagnolo, da una persona.',
        meta: '+34 744 717 942 · orario spagnolo',
        cta: 'Apri WhatsApp',
      },
    ],
    faqs: [
      {
        q: 'Come chiedo aiuto se uno strumento non funziona?',
        a: 'Entra in itapp.aichef.pro e scrivi dall’assistenza integrata. Se non riesci a entrare, manda a info@aichef.pro il messaggio che compare a schermo.',
      },
      {
        q: 'Come cambio piano, scarico una fattura o disdico?',
        a: 'Lo fai tu dal pannello: cambio piano, dati fiscali e disdetta, senza permanenza. Ogni abbonamento genera una fattura con l’IVA del tuo paese. Per una fattura precisa scrivi a info@aichef.pro dall’indirizzo dell’account.',
      },
      {
        q: 'Chi contatto per la stampa o una collaborazione?',
        a: 'Scrivi a info@aichef.pro con un oggetto chiaro. Dietro AI Chef Pro c’è John Guerrero, in cucina dai 17 anni e consulente gastronomico dal 2010, con il gruppo ChefBusiness.',
      },
      {
        q: 'In che lingue rispondete?',
        a: 'L’assistenza è sciolta in spagnolo e in inglese. Nelle altre lingue facciamo il possibile per risponderti. Il prodotto è in sette lingue. I prezzi di questo sito restano in euro.',
      },
      {
        q: 'C’è una politica di rimborso pubblicata?',
        a: 'No. Per l’abbonamento non c’è una politica di rimborso pubblicata: ogni caso si guarda via email. Puoi disdire quando vuoi dal pannello, senza vincolo. I prodotti digitali indicano la propria garanzia nella scheda.',
      },
    ],
    blocks: [],
    ctaTitle: 'Prova la suite mentre decidi',
    ctaBody:
      'Il piano Membro costa 10 € al mese, con 10.000 crediti. La pagina prezzi in italiano indica oggi più di 50 agenti: il catalogo italiano è ancora in completamento. Disdici quando vuoi.',
    ctaPrimary: 'Scrivi a info@aichef.pro',
    ctaSecondary: 'Vedi i prezzi',
  },
  pt: {
    title: 'Contacto e apoio — AI Chef Pro',
    description:
      'Contacta o AI Chef Pro: info@aichef.pro, apoio dentro de ptapp.aichef.pro, ou WhatsApp +34 744 717 942. Resposta indicativa em 24–48 horas úteis (Espanha).',
    keywords: 'contacto AI Chef Pro, apoio AI Chef Pro, suporte restauração IA, email AI Chef Pro',
    eyebrow: 'Contacto',
    h1: 'Escreve-nos: responde uma pessoa',
    lead: 'Dúvida sobre uma ferramenta, uma subscrição ou um pedido de imprensa chega à mesma mesa. A equipa de John Guerrero lê info@aichef.pro.',
    answerLabel: 'Resposta direta',
    answer:
      'Escreve para info@aichef.pro. Se já tens conta, o apoio dentro de ptapp.aichef.pro é mais rápido porque vemos o plano. Prazo indicativo: 24–48 horas úteis, horário de Espanha. O WhatsApp +34 744 717 942 é uma pessoa, não um bot.',
    homeLabel: 'Início',
    crumb: 'Contacto',
    faqHeading: 'Perguntas sobre o contacto',
    emailCta: 'Escrever para info@aichef.pro',
    appCta: 'Abrir a app',
    waText: 'Olá, tenho uma questão sobre o AI Chef Pro.',
    honesty:
      'Esta página não tem formulário. Escreve por email, a partir da conta ou no WhatsApp: responde uma pessoa.',
    channels: [
      {
        icon: 'mail',
        tag: 'Via principal',
        title: 'Email',
        body: 'info@aichef.pro serve para o produto, faturação, imprensa e parcerias. Lemos a caixa todos os dias úteis.',
        meta: 'Resposta indicativa: 24–48 h úteis (Espanha)',
        cta: 'info@aichef.pro',
      },
      {
        icon: 'app',
        tag: 'Já tens conta',
        title: 'Apoio dentro da app',
        body: 'Em ptapp.aichef.pro o apoio já vê o espaço em português e o plano. É o caminho mais curto quando uma ferramenta bloqueia.',
        meta: 'Espaço em português · ptapp.aichef.pro',
        cta: 'Abrir ptapp.aichef.pro',
      },
      {
        icon: 'whatsapp',
        tag: 'Pergunta curta',
        title: 'WhatsApp',
        body: 'Se uma compra encravar, o WhatsApp evita esperar pelo email. Resposta em horário laboral espanhol, por uma pessoa.',
        meta: '+34 744 717 942 · horário de Espanha',
        cta: 'Abrir WhatsApp',
      },
    ],
    faqs: [
      {
        q: 'Como peço ajuda se uma ferramenta falha?',
        a: 'Entra em ptapp.aichef.pro e escreve a partir do apoio integrado. Se não conseguires entrar, envia para info@aichef.pro a mensagem que aparece no ecrã.',
      },
      {
        q: 'Como mudo de plano, descarrego uma fatura ou cancelo?',
        a: 'Fazes tu no painel: mudança de plano, dados fiscais e cancelamento, sem permanência. Cada subscrição gera uma fatura com o IVA do teu país. Para uma fatura concreta, escreve para info@aichef.pro a partir do email da conta.',
      },
      {
        q: 'Quem contacto para imprensa ou uma parceria?',
        a: 'Escreve para info@aichef.pro com um assunto claro. Por trás do AI Chef Pro está John Guerrero, na cozinha desde os 17 anos e consultor gastronómico desde 2010, com o grupo ChefBusiness.',
      },
      {
        q: 'Em que línguas respondem?',
        a: 'O apoio responde com à-vontade em espanhol e em inglês. Nas outras línguas fazemos o possível para te responder. O produto existe em sete línguas. O site em português é de Portugal (não do Brasil) e os preços ficam em euros.',
      },
      {
        q: 'Há uma política de reembolso publicada?',
        a: 'Não. Para a subscrição não há política de reembolso publicada: cada caso vê-se por email. Podes cancelar quando quiseres no painel, sem fidelização. Os produtos digitais indicam a garantia própria na ficha.',
      },
    ],
    blocks: [],
    ctaTitle: 'Experimenta a suite enquanto decides',
    ctaBody:
      'O plano Membro custa 10 € por mês, com 10.000 créditos. A página de preços em português indica hoje mais de 50 agentes: o catálogo ainda está a ser completado. Cancelas quando quiseres.',
    ctaPrimary: 'Escrever para info@aichef.pro',
    ctaSecondary: 'Ver preços',
  },
  nl: {
    title: 'Contact en support — AI Chef Pro',
    description:
      'Neem contact op met AI Chef Pro: info@aichef.pro, support in nlapp.aichef.pro, of WhatsApp +34 744 717 942. Richttijd: antwoord binnen 24–48 werkuren (Spanje).',
    keywords: 'contact AI Chef Pro, support AI Chef Pro, horeca AI hulp, e-mail AI Chef Pro',
    eyebrow: 'Contact',
    h1: 'Schrijf ons: er antwoordt een mens',
    lead: 'Een vraag over een tool, een abonnement of pers komt op dezelfde tafel. Het team van John Guerrero leest info@aichef.pro.',
    answerLabel: 'Kort antwoord',
    answer:
      'Mail info@aichef.pro. Heb je al een account, dan is de support in nlapp.aichef.pro sneller: we zien je abonnement. Richttijd: 24–48 werkuren, Spaanse kantoortijden. WhatsApp +34 744 717 942 is een persoon, geen bot.',
    homeLabel: 'Home',
    crumb: 'Contact',
    faqHeading: 'Vragen over contact',
    emailCta: 'Mail info@aichef.pro',
    appCta: 'Open de app',
    waText: 'Hallo, ik heb een vraag over AI Chef Pro.',
    honesty:
      'Deze pagina heeft geen formulier. Mail, schrijf vanuit je account of app WhatsApp: er antwoordt een persoon.',
    channels: [
      {
        icon: 'mail',
        tag: 'Hoofdkanaal',
        title: 'E-mail',
        body: 'info@aichef.pro is voor het product, facturen, pers en samenwerkingen. We lezen de bus elke werkdag.',
        meta: 'Richttijd: 24–48 werkuren (Spanje)',
        cta: 'info@aichef.pro',
      },
      {
        icon: 'app',
        tag: 'Je hebt al een account',
        title: 'Support in de app',
        body: 'In nlapp.aichef.pro ziet support je Nederlandse werkruimte en je abonnement. Dat is de kortste weg als een tool vastloopt.',
        meta: 'Nederlandse werkruimte · nlapp.aichef.pro',
        cta: 'Open nlapp.aichef.pro',
      },
      {
        icon: 'whatsapp',
        tag: 'Korte vraag',
        title: 'WhatsApp',
        body: 'Loopt een aankoop vast, dan is WhatsApp sneller dan wachten op mail. Antwoord tijdens Spaanse kantoortijden, door een persoon.',
        meta: '+34 744 717 942 · Spaanse kantoortijden',
        cta: 'Open WhatsApp',
      },
    ],
    faqs: [
      {
        q: 'Hoe krijg ik hulp als iets in het platform niet werkt?',
        a: 'Log in op nlapp.aichef.pro en schrijf vanuit de support daar. Lukt inloggen niet, mail de melding op het scherm naar info@aichef.pro.',
      },
      {
        q: 'Hoe wijzig ik mijn abonnement, download ik een factuur of zeg ik op?',
        a: 'Dat doe je zelf in het account: abonnement wisselen, factuurgegevens en opzeggen, zonder contractduur. Elk abonnement krijgt een factuur met de btw die voor jouw land geldt. Voor een concrete factuur mail je info@aichef.pro vanaf het e-mailadres van het account.',
      },
      {
        q: 'Wie mail ik voor pers of een samenwerking?',
        a: 'Mail info@aichef.pro met een duidelijk onderwerp. Achter AI Chef Pro staat John Guerrero — sinds zijn 17e in de keuken, sinds 2010 gastronomisch adviseur — en de groep ChefBusiness.',
      },
      {
        q: 'In welke talen antwoorden jullie?',
        a: 'Support antwoordt vlot in het Spaans en het Engels. In een andere taal doen we ons best. Het product bestaat in zeven talen. Prijzen op deze site blijven in euro.',
      },
      {
        q: 'Staat er een terugbetalingsbeleid online?',
        a: 'Nee. Voor het abonnement is geen terugbetalingsbeleid gepubliceerd; we bekijken elk geval per e-mail. Opzeggen kan op elk moment in het account, zonder binding. Digitale producten noemen hun eigen garantie op de productpagina.',
      },
    ],
    blocks: [],
    ctaTitle: 'Probeer de suite terwijl je nadenkt',
    ctaBody:
      'Het Lid-abonnement kost € 10 per maand, met 10.000 credits. De Nederlandse prijspagina noemt vandaag meer dan 50 agenten: die catalogus wordt nog aangevuld. Je zegt op wanneer je wilt.',
    ctaPrimary: 'Mail info@aichef.pro',
    ctaSecondary: 'Bekijk de prijzen',
  },
};
