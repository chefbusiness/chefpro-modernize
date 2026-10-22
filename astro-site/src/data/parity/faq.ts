import type { PageCopy, ParityLang } from './types';

const refund = {
  en: 'There is no published refund policy for the subscription. We look at each case by email at info@aichef.pro. You can cancel any time from the account panel; there is no lock-in.',
  fr: 'Il n’y a pas de politique de remboursement publiée pour l’abonnement. Chaque cas se regarde par e-mail à info@aichef.pro. Vous résiliez à tout moment depuis le compte, sans engagement.',
  de: 'Für das Abo ist keine Erstattungsregel veröffentlicht. Wir prüfen den Einzelfall per E-Mail an info@aichef.pro. Sie kündigen jederzeit im Konto, ohne Laufzeitbindung.',
  it: 'Per l’abbonamento non c’è una politica di rimborso pubblicata. Ogni caso si guarda via email a info@aichef.pro. Disdici quando vuoi dal pannello, senza permanenza.',
  pt: 'Para a subscrição não há política de reembolso publicada. Cada caso vê-se por email para info@aichef.pro. Cancelas quando quiseres no painel, sem permanência.',
  nl: 'Voor het abonnement is geen terugbetalingsbeleid gepubliceerd. We bekijken elk geval per e-mail via info@aichef.pro. Opzeggen kan op elk moment in het account, zonder binding.',
};

export const FAQ: Record<ParityLang, PageCopy> = {
  en: {
    title: 'FAQ — AI Chef Pro for Restaurants',
    description:
      'Straight answers on AI Chef Pro: €10/month Member plan, 10,000 credits, 75+ agents on the English workspace, cancellation, invoices and allergen scope (EU 14 vs US FDA major 9).',
    keywords: 'AI Chef Pro FAQ, AI Chef Pro pricing, restaurant AI credits, cancel AI Chef Pro',
    eyebrow: 'FAQ',
    h1: 'Questions operators actually ask',
    lead: 'Prices, credits, cancellation and what the allergen help does — and does not — decide for you.',
    answerLabel: 'Direct answer',
    answer:
      'AI Chef Pro is a browser suite of specialized agents for professional kitchens, not a generic chatbot. The Member plan is €10 per month with 10,000 credits and, on the English pricing page, access to 75+ agents. There is no free plan and no lock-in. Prices on this site are in euro.',
    homeLabel: 'Home',
    crumb: 'FAQ',
    faqHeading: 'FAQ',
    blocks: [
      {
        id: 'product',
        h2: 'What AI Chef Pro is',
        answer:
          'Each agent is built for one kitchen or restaurant task: costing, menus, allergens, content, service. You use it in the browser. Nothing to install.',
        faqs: [
          {
            q: 'What is AI Chef Pro?',
            a: 'A suite of specialized AI agents for cooks and restaurant operators. It is not a general chatbot. The English pricing page states 75+ agents. You start on the Member plan at €10 per month with 10,000 credits.',
          },
          {
            q: 'Who is behind it?',
            a: 'John Guerrero, in professional kitchens since he was 17 and a gastronomic consultant since 2010, with the ChefBusiness group. Personal site: johnguerrero.es.',
          },
          {
            q: 'Does it replace my food-safety consultant or my lawyer?',
            a: 'No. The agents draft and organize kitchen work. Allergen law, permits and tax stay with the authority of the country where you serve. This site is not legal advice.',
          },
        ],
      },
      {
        id: 'price',
        h2: 'Price, credits and VAT',
        answer:
          'Member is €10/month (10,000 credits). Premium Pro is €25 (85,000). Premium Plus is €50 (175,000). Premium Max is €95 with unlimited credits, or €950 per year. Every plan is a card subscription. There is no free plan.',
        faqs: [
          {
            q: 'Is there a free trial?',
            a: 'No. There is no free plan. The entry price is the Member plan at €10 per month, and you can cancel from the account panel.',
          },
          {
            q: 'What is a credit?',
            a: 'A credit is the unit of work. A short prompt spends few credits; a full costing or a full menu spends more. Member includes 10,000 credits each month. They renew monthly. Premium Max removes the cap.',
          },
          {
            q: 'Do prices include VAT?',
            a: 'The prices published on the pricing page are the plan prices in euro. Each subscription generates an invoice with the VAT that applies to your country. We do not publish a single VAT rate for every country on this page.',
          },
          {
            q: 'Why are prices in euro on the English site?',
            a: 'The company sells the subscription in euro on every language of aichef.pro, including English. The English page is not a US-dollar price list.',
          },
        ],
      },
      {
        id: 'account',
        h2: 'Account, cancellation and allergens',
        answer:
          'You change plan or cancel yourself in the account. Refunds are case by case because no subscription refund policy is published.',
        faqs: [
          {
            q: 'Can I cancel any time?',
            a: 'Yes. There is no lock-in. Plan changes and cancellation are in the account panel.',
          },
          {
            q: 'What is the refund policy?',
            a: refund.en,
          },
          {
            q: 'Does the allergen tool follow the EU list of 14 or the US FDA major allergens?',
            a: 'The agent helps you spot allergens in a recipe. The legal list depends on where you serve. In the EU, Regulation (EU) No 1169/2011 Annex II names 14 allergens. In the United States the FDA major allergens are nine, including sesame since 2023. The tool does not replace the declaration your local authority requires.',
          },
          {
            q: 'Which languages can I work in?',
            a: 'The product is in Spanish, English, French, German, Italian, Portuguese and Dutch, each with its own workspace. Support replies fluently in Spanish and English and will try in the other languages. The Spanish catalog is the largest; other workspaces are still being completed.',
          },
        ],
      },
    ],
    ctaTitle: 'See the plans before you write to us',
    ctaBody: 'Member is €10 per month. If a line on this page is wrong, email info@aichef.pro with the URL.',
    ctaPrimary: 'Open the app',
    ctaSecondary: 'See plans and pricing',
  },
  fr: {
    title: 'Questions fréquentes — AI Chef Pro',
    description:
      'Réponses directes sur AI Chef Pro : forfait Membre à 10 €/mois, 10 000 crédits, plus de 50 agents sur l’espace français, résiliation et allergènes INCO (14 allergènes).',
    keywords: 'FAQ AI Chef Pro, tarif AI Chef Pro, crédits IA restauration, résilier AI Chef Pro, allergènes restaurant',
    eyebrow: 'Questions fréquentes',
    h1: 'Les questions que se posent les restaurateurs',
    lead: 'Prix, crédits, résiliation et ce que l’aide aux allergènes couvre — et ne couvre pas.',
    answerLabel: 'Réponse directe',
    answer:
      'AI Chef Pro est une suite d’agents spécialisés pour la cuisine professionnelle, dans le navigateur. Le forfait Membre coûte 10 € par mois avec 10 000 crédits. La page tarifs en français indique aujourd’hui plus de 50 agents : ce catalogue est encore en cours. Pas de forfait gratuit, pas d’engagement. Les prix restent en euros.',
    homeLabel: 'Accueil',
    crumb: 'Questions fréquentes',
    faqHeading: 'Questions fréquentes',
    blocks: [
      {
        id: 'produit',
        h2: 'Ce qu’est AI Chef Pro',
        answer:
          'Chaque agent traite une tâche de cuisine ou de salle : fiche technique, carte, allergènes, contenu, service. Rien à installer.',
        faqs: [
          {
            q: 'Qu’est-ce qu’AI Chef Pro ?',
            a: 'Une suite d’agents d’intelligence artificielle pour les cuisiniers et les exploitants, pas un chatbot généraliste. Le forfait Membre est à 10 € par mois avec 10 000 crédits. L’espace français affiche aujourd’hui plus de 50 agents ; l’espace espagnol en publie 75+.',
          },
          {
            q: 'Qui est derrière le produit ?',
            a: 'John Guerrero, en cuisine depuis ses 17 ans et consultant en restauration depuis 2010, avec le groupe ChefBusiness. Site personnel : johnguerrero.es.',
          },
          {
            q: 'Est-ce que cela remplace mon conseiller hygiène ou mon expert-comptable ?',
            a: 'Non. Les agents préparent le travail de cuisine. Allergènes, autorisations et fiscalité restent ceux du pays où vous servez. Ce site n’est pas un conseil juridique.',
          },
        ],
      },
      {
        id: 'prix',
        h2: 'Prix, crédits et TVA',
        answer:
          'Membre : 10 €/mois (10 000 crédits). Premium Pro : 25 € (85 000). Premium Plus : 50 € (175 000). Premium Max : 95 € avec crédits illimités, ou 950 € par an. Paiement par carte. Pas de forfait gratuit.',
        faqs: [
          {
            q: 'Y a-t-il un essai gratuit ?',
            a: 'Non. Il n’y a pas de forfait gratuit. L’entrée est le forfait Membre à 10 € par mois, résiliable depuis le compte.',
          },
          {
            q: 'C’est quoi un crédit ?',
            a: 'Le crédit est l’unité de travail. Une idée courte en consomme peu ; une fiche complète ou une carte entière en consomme davantage. Le forfait Membre comprend 10 000 crédits par mois, renouvelés chaque mois. Premium Max retire le plafond.',
          },
          {
            q: 'Les prix sont-ils TTC ?',
            a: 'Les prix affichés sur la page tarifs sont les prix des forfaits en euros. Chaque abonnement produit une facture avec la TVA applicable à votre pays. Cette page ne publie pas un taux unique pour tous les pays.',
          },
          {
            q: 'La formation est-elle prise en charge par le CPF ou un OPCO ?',
            a: 'Non. Nous ne revendiquons aucune prise en charge CPF ou OPCO. La formation en présentiel se chiffre à part, sur la page formation, avec des prix de base pour l’Espagne péninsulaire.',
          },
        ],
      },
      {
        id: 'compte',
        h2: 'Compte, résiliation et allergènes',
        answer:
          'Vous changez de forfait ou vous résiliez vous-même dans le compte. Le remboursement de l’abonnement se traite au cas par cas.',
        faqs: [
          {
            q: 'Puis-je résilier quand je veux ?',
            a: 'Oui. Il n’y a pas d’engagement. Le changement de forfait et la résiliation sont dans le panneau du compte.',
          },
          {
            q: 'Quelle est la politique de remboursement ?',
            a: refund.fr,
          },
          {
            q: 'L’outil allergènes suit-il la liste des 14 allergènes INCO ?',
            a: 'L’agent aide à repérer les allergènes dans une recette. En France, l’information du consommateur repose sur les 14 allergènes de l’annexe II du règlement (UE) n° 1169/2011. L’outil ne remplace pas votre affichage ni le plan de maîtrise sanitaire.',
          },
          {
            q: 'Dans quelles langues puis-je travailler ?',
            a: 'Le produit existe en espagnol, anglais, français, allemand, italien, portugais et néerlandais, chacun avec son espace. L’assistance répond aisément en espagnol et en anglais, et fait le nécessaire dans les autres langues.',
          },
        ],
      },
    ],
    ctaTitle: 'Regardez les tarifs avant de nous écrire',
    ctaBody: 'Le forfait Membre est à 10 € par mois. Si une phrase de cette page est fausse, écrivez à info@aichef.pro avec l’URL.',
    ctaPrimary: 'Ouvrir l’application',
    ctaSecondary: 'Voir les tarifs',
  },
  de: {
    title: 'Häufige Fragen — AI Chef Pro',
    description:
      'Direkte Antworten zu AI Chef Pro: Mitglied 10 €/Monat, 10.000 Credits, auf der deutschen Seite mehr als 50 Agenten, Kündigung und Allergene nach VO (EU) Nr. 1169/2011.',
    keywords: 'AI Chef Pro FAQ, Preise AI Chef Pro, Credits Gastronomie KI, AI Chef Pro kündigen, Allergene Gastronomie',
    eyebrow: 'Häufige Fragen',
    h1: 'Fragen, die Betriebe wirklich stellen',
    lead: 'Preis, Credits, Kündigung und was die Allergen-Hilfe leistet — und was nicht.',
    answerLabel: 'Kurzantwort',
    answer:
      'AI Chef Pro ist eine Suite spezialisierter Agenten für die Profiküche, im Browser. Der Mitgliedsplan kostet 10 € im Monat mit 10.000 Credits. Die deutsche Preisseite nennt heute mehr als 50 Agenten; der Katalog wird noch ergänzt. Kein Gratisplan, keine Laufzeitbindung. Preise in Euro.',
    homeLabel: 'Startseite',
    crumb: 'Häufige Fragen',
    faqHeading: 'Häufige Fragen',
    blocks: [
      {
        id: 'produkt',
        h2: 'Was AI Chef Pro ist',
        answer:
          'Jeder Agent bearbeitet eine Aufgabe aus Küche oder Betrieb: Kalkulation, Karte, Allergene, Inhalte, Service. Nichts zu installieren.',
        faqs: [
          {
            q: 'Was ist AI Chef Pro?',
            a: 'Eine Suite spezialisierter KI-Agenten für Köche und Betriebe, kein allgemeiner Chatbot. Der Mitgliedsplan kostet 10 € im Monat mit 10.000 Credits. Der deutsche Arbeitsbereich nennt heute mehr als 50 Agenten; der spanische veröffentlicht 75+.',
          },
          {
            q: 'Wer steht dahinter?',
            a: 'John Guerrero, seit dem 17. Lebensjahr in der Küche und seit 2010 gastronomischer Berater, mit der Gruppe ChefBusiness. Persönliche Seite: johnguerrero.es.',
          },
          {
            q: 'Ersetzt das meinen Hygienberater oder den Steuerberater?',
            a: 'Nein. Die Agenten bereiten Küchenarbeit vor. Allergene, Genehmigungen und Steuer bleiben die des Landes, in dem Sie servieren. Diese Website ist keine Rechtsberatung.',
          },
        ],
      },
      {
        id: 'preis',
        h2: 'Preis, Credits und Mehrwertsteuer',
        answer:
          'Mitglied: 10 €/Monat (10.000 Credits). Premium Pro: 25 € (85.000). Premium Plus: 50 € (175.000). Premium Max: 95 € mit unbegrenzten Credits, oder 950 € im Jahr. Zahlung per Karte. Kein Gratisplan.',
        faqs: [
          {
            q: 'Gibt es eine kostenlose Testphase?',
            a: 'Nein. Es gibt keinen Gratisplan. Der Einstieg ist der Mitgliedsplan für 10 € im Monat, kündbar im Konto.',
          },
          {
            q: 'Was ist ein Credit?',
            a: 'Der Credit ist die Arbeitseinheit. Eine kurze Idee verbraucht wenige Credits; eine volle Kalkulation oder eine ganze Karte verbraucht mehr. Der Mitgliedsplan enthält 10.000 Credits im Monat. Sie erneuern sich monatlich. Premium Max hebt die Grenze auf.',
          },
          {
            q: 'Sind die Preise inklusive Mehrwertsteuer?',
            a: 'Die Preise auf der Preisseite sind die Planpreise in Euro. Jedes Abo erzeugt eine Rechnung mit der Mehrwertsteuer, die für Ihr Land gilt. Diese Seite nennt keinen einheitlichen Satz für alle Länder.',
          },
          {
            q: 'Wird die Schulung über einen Bildungsgutschein gefördert?',
            a: 'Nein. Wir behaupten keine Förderung durch Bildungsgutschein oder ähnliche Träger. Die Präsenzschulung wird getrennt angeboten, mit Basispreisen für das spanische Festland.',
          },
        ],
      },
      {
        id: 'konto',
        h2: 'Konto, Kündigung und Allergene',
        answer:
          'Tarifwechsel und Kündigung erledigen Sie selbst im Konto. Eine Erstattung des Abos wird im Einzelfall geprüft.',
        faqs: [
          {
            q: 'Kann ich jederzeit kündigen?',
            a: 'Ja. Es gibt keine Laufzeitbindung. Tarifwechsel und Kündigung liegen im Konto.',
          },
          {
            q: 'Wie ist die Erstattungsregel?',
            a: refund.de,
          },
          {
            q: 'Folgt die Allergen-Hilfe den 14 Allergenen der LMIV?',
            a: 'Der Agent hilft, Allergene in einem Rezept zu erkennen. In der EU nennt Anhang II der Verordnung (EU) Nr. 1169/2011 vierzehn Allergene. Das Werkzeug ersetzt weder Ihre Kennzeichnung noch die betriebliche Hygiene.',
          },
          {
            q: 'In welchen Sprachen kann ich arbeiten?',
            a: 'Das Produkt gibt es auf Spanisch, Englisch, Französisch, Deutsch, Italienisch, Portugiesisch und Niederländisch, jeweils mit eigenem Arbeitsbereich. Der Support antwortet sicher auf Spanisch und Englisch und versucht es in den anderen Sprachen.',
          },
        ],
      },
    ],
    ctaTitle: 'Lesen Sie die Preise, bevor Sie schreiben',
    ctaBody: 'Der Mitgliedsplan kostet 10 € im Monat. Wenn ein Satz auf dieser Seite falsch ist, schreiben Sie an info@aichef.pro mit der URL.',
    ctaPrimary: 'Zur App',
    ctaSecondary: 'Preise ansehen',
  },
  it: {
    title: 'Domande frequenti — AI Chef Pro',
    description:
      'Risposte dirette su AI Chef Pro: piano Membro a 10 €/mese, 10.000 crediti, più di 50 agenti sullo spazio italiano, disdetta e 14 allergeni del Reg. UE 1169/2011.',
    keywords: 'FAQ AI Chef Pro, prezzi AI Chef Pro, crediti IA ristorante, disdire AI Chef Pro, allergeni ristorante',
    eyebrow: 'Domande frequenti',
    h1: 'Le domande che fa chi ha un locale',
    lead: 'Prezzo, crediti, disdetta e cosa fa — e non fa — l’aiuto sugli allergeni.',
    answerLabel: 'Risposta diretta',
    answer:
      'AI Chef Pro è una suite di agenti specializzati per la cucina professionale, nel browser. Il piano Membro costa 10 € al mese con 10.000 crediti. La pagina prezzi in italiano indica oggi più di 50 agenti: il catalogo è ancora in completamento. Niente piano gratuito, niente permanenza. Prezzi in euro.',
    homeLabel: 'Home',
    crumb: 'Domande frequenti',
    faqHeading: 'Domande frequenti',
    blocks: [
      {
        id: 'prodotto',
        h2: 'Che cos’è AI Chef Pro',
        answer:
          'Ogni agente svolge un compito di cucina o di sala: scheda costo, menu, allergeni, contenuti, servizio. Non installi nulla.',
        faqs: [
          {
            q: 'Che cos’è AI Chef Pro?',
            a: 'Una suite di agenti di intelligenza artificiale per cuochi e gestori, non un chatbot generico. Il piano Membro costa 10 € al mese con 10.000 crediti. Lo spazio italiano indica oggi più di 50 agenti; quello spagnolo ne pubblica 75+.',
          },
          {
            q: 'Chi c’è dietro?',
            a: 'John Guerrero, in cucina dai 17 anni e consulente gastronomico dal 2010, con il gruppo ChefBusiness. Sito personale: johnguerrero.es.',
          },
          {
            q: 'Sostituisce il consulente HACCP o il commercialista?',
            a: 'No. Gli agenti preparano il lavoro di cucina. Allergeni, autorizzazioni e fisco restano quelli del paese in cui servi. Questo sito non è una consulenza legale.',
          },
        ],
      },
      {
        id: 'prezzo',
        h2: 'Prezzo, crediti e IVA',
        answer:
          'Membro: 10 €/mese (10.000 crediti). Premium Pro: 25 € (85.000). Premium Plus: 50 € (175.000). Premium Max: 95 € con crediti illimitati, oppure 950 € l’anno. Pagamento con carta. Niente piano gratuito.',
        faqs: [
          {
            q: 'C’è una prova gratuita?',
            a: 'No. Non c’è un piano gratuito. Si entra con il piano Membro a 10 € al mese, disdicibile dal pannello.',
          },
          {
            q: 'Che cos’è un credito?',
            a: 'Il credito è l’unità di lavoro. Un’idea breve ne consuma pochi; una scheda completa o un menu intero ne consuma di più. Il piano Membro include 10.000 crediti al mese, che si rinnovano ogni mese. Premium Max toglie il tetto.',
          },
          {
            q: 'I prezzi sono IVA inclusa?',
            a: 'I prezzi in pagina prezzi sono i prezzi dei piani in euro. Ogni abbonamento genera una fattura con l’IVA del tuo paese. Questa pagina non pubblica un’aliquota unica per tutti i paesi.',
          },
          {
            q: 'La formazione è finanziata da un fondo interprofessionale?',
            a: 'No. Non dichiariamo finanziamenti da fondi interprofessionali. La formazione in presenza si quota a parte, con prezzi base per la Spagna peninsulare.',
          },
        ],
      },
      {
        id: 'account',
        h2: 'Account, disdetta e allergeni',
        answer:
          'Cambi piano o disdici da solo nel pannello. Il rimborso dell’abbonamento si valuta caso per caso.',
        faqs: [
          {
            q: 'Posso disdire quando voglio?',
            a: 'Sì. Non c’è permanenza. Cambio piano e disdetta stanno nel pannello.',
          },
          {
            q: 'Qual è la politica di rimborso?',
            a: refund.it,
          },
          {
            q: 'Lo strumento allergeni segue i 14 allergeni europei?',
            a: 'L’agente aiuta a individuare gli allergeni in una ricetta. In Italia vale l’allegato II del Reg. (UE) n. 1169/2011: 14 allergeni. Lo strumento non sostituisce il menu allergeni né il piano di autocontrollo.',
          },
          {
            q: 'In che lingue posso lavorare?',
            a: 'Il prodotto è in spagnolo, inglese, francese, tedesco, italiano, portoghese e olandese, ognuno con il proprio spazio. L’assistenza risponde bene in spagnolo e in inglese e ci prova nelle altre lingue.',
          },
        ],
      },
    ],
    ctaTitle: 'Guarda i prezzi prima di scriverci',
    ctaBody: 'Il piano Membro costa 10 € al mese. Se una frase di questa pagina è sbagliata, scrivi a info@aichef.pro con l’URL.',
    ctaPrimary: 'Apri l’app',
    ctaSecondary: 'Vedi i prezzi',
  },
  pt: {
    title: 'Perguntas frequentes — AI Chef Pro',
    description:
      'Respostas diretas sobre o AI Chef Pro: plano Membro a 10 €/mês, 10.000 créditos, mais de 50 agentes no espaço em português, cancelamento e 14 alergénios (Reg. UE 1169/2011).',
    keywords: 'FAQ AI Chef Pro, preços AI Chef Pro, créditos IA restauração, cancelar AI Chef Pro, alergénios restaurante',
    eyebrow: 'Perguntas frequentes',
    h1: 'As perguntas que um restaurante faz mesmo',
    lead: 'Preço, créditos, cancelamento e o que a ajuda de alergénios faz — e não faz.',
    answerLabel: 'Resposta direta',
    answer:
      'O AI Chef Pro é uma suite de agentes especializados para a cozinha profissional, no browser. O plano Membro custa 10 € por mês com 10.000 créditos. A página de preços em português indica hoje mais de 50 agentes: o catálogo ainda está a ser completado. Não há plano grátis nem permanência. Preços em euros. O site é de Portugal.',
    homeLabel: 'Início',
    crumb: 'Perguntas frequentes',
    faqHeading: 'Perguntas frequentes',
    blocks: [
      {
        id: 'produto',
        h2: 'O que é o AI Chef Pro',
        answer:
          'Cada agente trata de uma tarefa de cozinha ou de sala: ficha técnica, carta, alergénios, conteúdo, serviço. Não instalas nada.',
        faqs: [
          {
            q: 'O que é o AI Chef Pro?',
            a: 'Uma suite de agentes de inteligência artificial para cozinheiros e operadores, não um chatbot genérico. O plano Membro custa 10 € por mês com 10.000 créditos. O espaço em português indica hoje mais de 50 agentes; o espaço espanhol publica 75+.',
          },
          {
            q: 'Quem está por trás?',
            a: 'John Guerrero, na cozinha desde os 17 anos e consultor gastronómico desde 2010, com o grupo ChefBusiness. Site pessoal: johnguerrero.es.',
          },
          {
            q: 'Substitui o consultor de HACCP ou o contabilista?',
            a: 'Não. Os agentes preparam o trabalho de cozinha. Alergénios, licenças e fiscalidade são os do país onde serves. Este site não é aconselhamento jurídico. Em Portugal fala-se de alergénios e de HACCP; APPCC é o termo brasileiro e não é a língua desta página.',
          },
        ],
      },
      {
        id: 'preco',
        h2: 'Preço, créditos e IVA',
        answer:
          'Membro: 10 €/mês (10.000 créditos). Premium Pro: 25 € (85.000). Premium Plus: 50 € (175.000). Premium Max: 95 € com créditos ilimitados, ou 950 € por ano. Pagamento com cartão. Não há plano grátis.',
        faqs: [
          {
            q: 'Há um período experimental grátis?',
            a: 'Não. Não há plano grátis. A entrada é o plano Membro a 10 € por mês, cancelável no painel.',
          },
          {
            q: 'O que é um crédito?',
            a: 'O crédito é a unidade de trabalho. Uma ideia curta gasta poucos; uma ficha completa ou uma carta inteira gasta mais. O plano Membro inclui 10.000 créditos por mês, que se renovam todos os meses. O Premium Max tira o teto.',
          },
          {
            q: 'Os preços incluem IVA?',
            a: 'Os preços na página de preços são os preços dos planos em euros. Cada subscrição gera uma fatura com o IVA do teu país. Esta página não publica uma taxa única para todos os países.',
          },
          {
            q: 'A formação é apoiada pelo IEFP ou por um fundo?',
            a: 'Não. Não declaramos apoio do IEFP nem de fundos. A formação presencial orçamenta-se à parte, com preços base para Espanha peninsular.',
          },
        ],
      },
      {
        id: 'conta',
        h2: 'Conta, cancelamento e alergénios',
        answer:
          'Mudanças de plano e cancelamento fazes tu no painel. O reembolso da subscrição avalia-se caso a caso.',
        faqs: [
          {
            q: 'Posso cancelar quando quiser?',
            a: 'Sim. Não há permanência. A mudança de plano e o cancelamento estão no painel.',
          },
          {
            q: 'Qual é a política de reembolso?',
            a: refund.pt,
          },
          {
            q: 'A ferramenta de alergénios segue a lista dos 14?',
            a: 'O agente ajuda a localizar alergénios numa receita. Na União Europeia a lista é o anexo II do Regulamento (UE) n.º 1169/2011: 14 alergénios. A ferramenta não substitui a informação ao cliente nem o teu plano HACCP.',
          },
          {
            q: 'Em que línguas posso trabalhar?',
            a: 'O produto existe em espanhol, inglês, francês, alemão, italiano, português e neerlandês, cada um com o seu espaço. O apoio responde com à-vontade em espanhol e em inglês e tenta nas outras línguas. O português do site é de Portugal.',
          },
        ],
      },
    ],
    ctaTitle: 'Vê os preços antes de nos escreveres',
    ctaBody: 'O plano Membro custa 10 € por mês. Se uma frase desta página estiver errada, escreve para info@aichef.pro com o URL.',
    ctaPrimary: 'Abrir a app',
    ctaSecondary: 'Ver preços',
  },
  nl: {
    title: 'Veelgestelde vragen — AI Chef Pro',
    description:
      'Korte antwoorden over AI Chef Pro: Lid-abonnement € 10 per maand, 10.000 credits, meer dan 50 agenten op de Nederlandse pagina, opzeggen en de 14 allergenen (Verordening (EU) nr. 1169/2011).',
    keywords: 'FAQ AI Chef Pro, prijzen AI Chef Pro, credits horeca AI, AI Chef Pro opzeggen, allergenen horeca',
    eyebrow: 'Veelgestelde vragen',
    h1: 'Vragen die een zaak echt stelt',
    lead: 'Prijs, credits, opzeggen en wat de allergenenhulp wel en niet doet.',
    answerLabel: 'Kort antwoord',
    answer:
      'AI Chef Pro is een suite van gespecialiseerde agenten voor de professionele keuken, in de browser. Het Lid-abonnement kost € 10 per maand met 10.000 credits. De Nederlandse prijspagina noemt vandaag meer dan 50 agenten; die catalogus wordt nog aangevuld. Geen gratis abonnement en geen contractduur. Prijzen in euro.',
    homeLabel: 'Home',
    crumb: 'Veelgestelde vragen',
    faqHeading: 'Veelgestelde vragen',
    blocks: [
      {
        id: 'product',
        h2: 'Wat AI Chef Pro is',
        answer:
          'Elke agent doet één taak uit keuken of zaak: kostprijs, kaart, allergenen, content, service. Je installeert niets.',
        faqs: [
          {
            q: 'Wat is AI Chef Pro?',
            a: 'Een suite van gespecialiseerde AI-agenten voor koks en ondernemers, geen algemene chatbot. Het Lid-abonnement kost € 10 per maand met 10.000 credits. De Nederlandse werkruimte noemt vandaag meer dan 50 agenten; de Spaanse publiceert 75+.',
          },
          {
            q: 'Wie zit erachter?',
            a: 'John Guerrero, sinds zijn 17e in de keuken en sinds 2010 gastronomisch adviseur, met de groep ChefBusiness. Persoonlijke site: johnguerrero.es.',
          },
          {
            q: 'Vervangt dit mijn hygiënecode-adviseur of mijn boekhouder?',
            a: 'Nee. De agenten bereiden keukenwerk voor. Allergenen, vergunningen en belasting blijven die van het land waar je serveert. Deze site is geen juridisch advies.',
          },
        ],
      },
      {
        id: 'prijs',
        h2: 'Prijs, credits en btw',
        answer:
          'Lid: € 10 per maand (10.000 credits). Premium Pro: € 25 (85.000). Premium Plus: € 50 (175.000). Premium Max: € 95 met onbeperkte credits, of € 950 per jaar. Betaling met kaart. Geen gratis abonnement.',
        faqs: [
          {
            q: 'Is er een gratis proefperiode?',
            a: 'Nee. Er is geen gratis abonnement. Je begint met Lid voor € 10 per maand en zegt op in het account.',
          },
          {
            q: 'Wat is een credit?',
            a: 'Een credit is de werkeenheid. Een kort idee kost weinig credits; een volledige kostprijs of een hele kaart kost meer. Lid bevat 10.000 credits per maand. Die vernieuwen elke maand. Premium Max haalt het plafond weg.',
          },
          {
            q: 'Zijn de prijzen inclusief btw?',
            a: 'De prijzen op de prijspagina zijn de abonnementsprijzen in euro. Elk abonnement krijgt een factuur met de btw die voor jouw land geldt. Deze pagina publiceert geen enkel tarief voor alle landen.',
          },
          {
            q: 'Wordt de training vergoed via SLIM of een ander scholingsbudget?',
            a: 'Nee. We claimen geen vergoeding via SLIM of een ander scholingsbudget. De training op locatie wordt apart geciteerd, met basisprijzen voor het Spaanse vasteland.',
          },
        ],
      },
      {
        id: 'account',
        h2: 'Account, opzeggen en allergenen',
        answer:
          'Abonnement wisselen of opzeggen doe je zelf in het account. Een terugbetaling van het abonnement bekijken we per geval.',
        faqs: [
          {
            q: 'Kan ik op elk moment opzeggen?',
            a: 'Ja. Er is geen contractduur. Wisselen en opzeggen zitten in het account.',
          },
          {
            q: 'Wat is het terugbetalingsbeleid?',
            a: refund.nl,
          },
          {
            q: 'Volgt de allergenentool de 14 allergenen?',
            a: 'De agent helpt allergenen in een recept te zien. In de EU noemt bijlage II van Verordening (EU) nr. 1169/2011 veertien allergenen. De tool vervangt niet de informatie aan de gast en ook niet je hygiënecode. De NVWA houdt in Nederland toezicht op die informatie.',
          },
          {
            q: 'In welke talen kan ik werken?',
            a: 'Het product bestaat in het Spaans, Engels, Frans, Duits, Italiaans, Portugees en Nederlands, elk met een eigen werkruimte. Support antwoordt vlot in het Spaans en het Engels en doet zijn best in de andere talen.',
          },
        ],
      },
    ],
    ctaTitle: 'Bekijk de prijzen voordat je mailt',
    ctaBody: 'Het Lid-abonnement kost € 10 per maand. Klopt een zin op deze pagina niet, mail de URL naar info@aichef.pro.',
    ctaPrimary: 'Open de app',
    ctaSecondary: 'Bekijk de prijzen',
  },
};
