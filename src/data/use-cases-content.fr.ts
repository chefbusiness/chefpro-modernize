// Francés content for use-case spokes.
// Each entry mirrors the structure of USE_CASES_CONTENT_ES.
// Missing entries fall back to ES at runtime via makeContent() in use-cases.ts.
//
// Generado el 2026-08-15 con scripts/astro-migration/fase10-traducir-spokes.py
// (bridge.py ~deepseek/deepseek-v4-flash-latest, --strict-lang) y el glosario
// de la PLATAFORMA viva fase10-glosario-fr.json. Los agentes sin versión
// fr se preservan verbatim a propósito (decisión de catálogo pendiente,
// ver CATALOGO_ITALIANO_PENDIENTE.md — aplica a los 5 idiomas).
//
// NO editar a mano campo a campo: productIds, galleryImages, features[].icon,
// seo.ogImage y testimonialAuthor se preservan verbatim desde el ES y el
// validador del script lo comprueba. Regenerar PISA ediciones manuales.

import type { UseCaseContent } from './use-cases';

export const USE_CASES_CONTENT_FR: Record<string, UseCaseContent> = {
  "propietario-restaurante": {
    "h1": "IA pour Propriétaires de Restaurant",
    "heroSubtitle": "Prenez de meilleures décisions, récupérez des heures administratives et augmentez la rentabilité de votre restaurant avec une suite d'agents d'IA spécialisés dans l'hôtellerie-restauration.",
    "heroTagline": "Votre partenaire numérique pour gérer votre entreprise avec des données",
    "badge": "Pour propriétaires et gérants de restaurant",
    "painsTitle": "Ce Qu'un Propriétaire de Restaurant Ne Peut Pas Laisser de Résoudre",
    "pains": [
      "Marge étroite : il est difficile de savoir quels plats sont rentables et lesquels saignent la rentabilité sans une analyse précise",
      "Temps limité pour examiner les coûts, les fiches techniques, les fournisseurs et la communication avec l'équipe",
      "Décisions de menu, de prix et de promotions prises plus par intuition que par des données",
      "Équipes en rotation : former, superviser et gérer les horaires consomme des heures chaque semaine",
      "Reporting financier au gestionnaire ou aux investisseurs qui exige des documents propres et consolidés",
      "Marketing et communication constants (réseaux sociaux, web, email) qui distraient de l'activité elle-même"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Propriétaire",
    "features": [
      {
        "icon": "BriefcaseBusiness",
        "title": "Manager de Restaurant Pro",
        "description": "Agent spécialisé pour accompagner le propriétaire dans les opérations quotidiennes, les décisions d'équipe et le reporting aux investisseurs."
      },
      {
        "icon": "FileText",
        "title": "Plan financier professionnel",
        "description": "Kit Plan Financiero : cash flow, seuil de rentabilité, P&L mensuel et tableau de bord des ratios. Modèles prêts pour les investisseurs et les banques."
      },
      {
        "icon": "Calculator",
        "title": "Fiches techniques professionnelles",
        "description": "Cuisine Créative fournit recette + fiche technique initiale CSV avec prix de référence ; le Kit de Escandallos Pro le gère avec vos prix réels."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP et sécurité alimentaire",
        "description": "Pack APPCC avec 19 registres prêts pour l'inspection, enregistrements depuis mobile et feuilles prêtes à imprimer en A4."
      },
      {
        "icon": "Users",
        "title": "Gestion du personnel et des horaires",
        "description": "Kit Gestión de Personal : plannings, contrôle des heures, ratios de productivité et intégration des nouveaux employés."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Suite de marketing et de SEO local : descriptions de plats, blog et campagnes avec IA pour attirer du trafic organique."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Recherche de mots-clés gastronomiques locaux pour positionner votre restaurant sur Google sans payer d'agence."
      },
      {
        "icon": "BarChart3",
        "title": "Repas du Personnel",
        "description": "Générateur de menus du personnel qui économise les coûts tout en gardant motivée l'équipe de cuisine et de salle."
      },
      {
        "icon": "MessageSquare",
        "title": "Coach Mental",
        "description": "Coaching psychologique pour les professionnels de l'hôtellerie-restauration : gestion du stress, équilibre travail-vie et direction d'équipes dans des secteurs à haute pression."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Propriétaire avec AI Chef Pro",
    "workflow": [
      "08:30 · Café et tableau de bord — vous ouvrez le Kit Plan Financiero et examinez les ratios de la veille. Vous détectez que le food cost est monté à 33 % à cause des pertes sur le poisson.",
      "09:30 · Manager de Restaurant Pro — vous demandez une analyse de la cause à l'agent et obtenez 3 actions concrètes pour cette semaine.",
      "10:30 · MenuDish Local SEO — vous mettez à jour la description des 4 plats top sur Google Business et sur le web avec des mots-clés détectés par Keyword Discovery AI+.",
      "12:30 · Service de midi — vous supervisez la salle en vous appuyant sur la checklist du Kit de Tareas Restaurante Casual.",
      "15:30 · Réunion avec le gestionnaire — vous exportez le P&L mensuel, le tableau de bord des ratios et le planning du personnel en PDF directement depuis le Kit Plan Financiero. Réunion bouclée en 30 minutes.",
      "17:00 · Cuisine Créative — vous demandez des idées pour le menu de la saison à venir. L'agent livre 8 plats avec recette et fiche technique CSV.",
      "18:30 · Décision d'équipe — vous utilisez Coach Mental pour préparer la conversation difficile avec un employé clé. Vous apportez structure et arguments à la réunion.",
      "21:00 · Clôture — le manager vous envoie le rapport automatique du jour par WhatsApp. Vous rentrez chez vous sans paperasse en attente."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Propriétaires",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Avant, je passais 6 heures par semaine à jongler avec les chiffres entre Excel et des serviettes. Avec AI Chef Pro, je le boucle en une heure avec des tableaux de bord professionnels. J'ai retrouvé le contrôle financier de mes deux établissements et la marge a augmenté de 3 points au premier trimestre.",
    "testimonialAuthor": "Carlos Méndez",
    "testimonialRole": "Propriétaire, groupe de bistrots méditerranéens (2 établissements)",
    "faqTitle": "Questions Fréquentes des Propriétaires",
    "faqs": [
      {
        "q": "Quelle taille de restaurant convient à AI Chef Pro ?",
        "a": "D'un seul établissement familial à des groupes de plus de 10 restaurants. Les modèles s'adaptent au volume et les plans s'ajustent à l'utilisation réelle. Il y a des clients avec 1 établissement et d'autres avec 25 unités actives."
      },
      {
        "q": "Ai-je besoin de compétences techniques ?",
        "a": "Non. Si vous savez utiliser WhatsApp et Excel à un niveau basique, vous savez déjà utiliser AI Chef Pro. L'onboarding commence avec l'agent «Qui suis-je ?», qui en 2 minutes adapte le système à vous, votre entreprise et votre zone géographique. Il y a des vidéos courtes d'onboarding et un support direct par WhatsApp."
      },
      {
        "q": "Remplace-t-il mon gestionnaire ou conseiller ?",
        "a": "Non, mais il leur facilite grandement la vie. Votre gestionnaire reçoit des documents propres et vous arrivez aux réunions avec des données consolidées. La plupart des cabinets de gestion finissent par recommander AI Chef Pro à d'autres clients."
      },
      {
        "q": "Combien de temps pour voir des résultats ?",
        "a": "La plupart des propriétaires rapportent entre 4 et 6 heures hebdomadaires récupérées dès la première semaine d'utilisation. L'impact sur la marge se situe généralement entre 2 et 5 points de pourcentage en 60-90 jours, grâce à la refonte des plats à food cost élevé et au contrôle des pertes."
      },
      {
        "q": "Comment m'aide-t-il avec le marketing et le SEO local ?",
        "a": "La suite Contenus et Réseaux Sociaux comprend MenuDish Local SEO (descriptions de plats optimisées), BlogPost SEO Gen+ (posts pour attirer du trafic organique) et Keyword Discovery AI+ (mots-clés gastronomiques locaux). Vous réduisez les dépenses en agences de marketing et captez des réservations directes."
      },
      {
        "q": "Y a-t-il des réductions pour les groupes avec plusieurs établissements ?",
        "a": "Oui. À partir de 5 unités actives, il existe des plans entreprise avec onboarding personnalisé et tableaux de bord consolidés par groupe."
      }
    ],
    "ctaTitle": "Gérez votre restaurant avec des données, pas avec l'intuition.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Propriétaires de Restaurant : Plan Financier, Fiches Techniques, SEO | AI Chef Pro",
      "description": "Suite d'IA pour propriétaires de restaurant : agents spécialisés, plan financier, fiches techniques professionnelles, HACCP, marketing et SEO local. Commencez aujourd'hui.",
      "keywords": "IA propriétaire restaurant, gérant restaurant IA, logiciel gestion restaurant propriétaires, plan financier restaurant IA, fiches techniques restaurant, marketing restaurant IA, SEO local restaurant, agent IA hôtellerie-restauration, propriétaire restaurant Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/propietario-restaurante.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Entreprise dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes dans lequel vous lui racontez quel type de restaurant vous avez, dans quelle ville, combien d'établissements, quel ticket moyen vous gérez et comment vous travaillez. À partir de ce moment, chaque agent — du Plan Financier au SEO local — répond adapté à votre contexte : prix du marché de votre zone, réglementation de votre pays et échelle réelle de votre opération. Ce n'est pas un formulaire : c'est une conversation courte qui rend chaque outil véritablement utile pour votre entreprise.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser en tant que Propriétaire",
    "apps": [
      {
        "name": "Manager de Restaurant Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistant opérationnel et financier pour vous accompagner dans les décisions d'équipe, le reporting et les opérations quotidiennes."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'Entreprise",
        "description": "Spécialiste des bistrots, gastrobars, tapas et méditerranéen : tout le spectre décontracté avec une base professionnelle."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Descriptions de plats optimisées pour le SEO local sur Google Business et le web."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles de blog qui attirent du trafic organique local vers votre restaurant."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Recherche de mots-clés gastronomiques locaux par zone postale."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de plats professionnels avec recette + fiche technique initiale CSV (prix de référence) prête pour le Kit de Escandallos Pro."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises sur les pertes et rendements par ingrédient, essentielles pour une fiche technique réaliste."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette et plat, prête pour la réglementation."
      },
      {
        "name": "Repas du Personnel",
        "category": "Gastro Profile Pro",
        "description": "Générateur de menus du personnel qui économise les coûts tout en gardant l'équipe motivée."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching psychologique pour les professionnels de l'hôtellerie-restauration : stress, équipes et décisions difficiles."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Calendrier gastronomique avec dates clés, idées et hashtags pour les réseaux sociaux et le blog."
      },
      {
        "name": "InstaFlow AI Pro + Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Contenu viral pour Instagram et Pinterest sans agence."
      }
    ],
    "metrics": [
      {
        "value": "+3 pp",
        "label": "marge en 60-90 jours"
      },
      {
        "value": "−6 h",
        "label": "hebdomadaires en gestion"
      },
      {
        "value": "×2",
        "label": "réservations directes via SEO local"
      },
      {
        "value": "12+",
        "label": "agents d'IA pour votre rôle"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "6 heures hebdomadaires à jongler avec Excel, des serviettes et des notes de fournisseurs",
        "Décisions de menu et de pricing par intuition, pas par analyse du food cost réel",
        "Reporting au gestionnaire avec des fichiers dispersés dans Word, Excel et email",
        "Marketing improvisé ou externalisé à des prix élevés sans savoir ce qui fonctionne",
        "Stress constant et coup de blues pendant les jours fériés à cause de ne pas lâcher le contrôle"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "1 heure hebdomadaire à boucler des tableaux de bord professionnels avec des KPI clairs",
        "Décisions de menu et de pricing avec fiche technique professionnelle et analyse de marge",
        "Reporting au gestionnaire en PDF directement depuis le Kit Plan Financiero",
        "SEO local automatisé et suite de marketing IA réduisant les dépenses en agences",
        "Tranquillité : l'équipe vous envoie des rapports automatiques par WhatsApp"
      ]
    },
    "galleryTitle": "Le Quotidien d'un Propriétaire, en Images",
    "gallerySubtitle": "Ce que vous pourrez gérer avec AI Chef Pro : tableaux de bord financiers, décisions opérationnelles, équipe, salle et reporting.",
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
    "h1": "IA pour Managers et Gérants de Restaurant",
    "heroSubtitle": "Optimisez les opérations quotidiennes, contrôlez les coûts et récupérez des heures de travail administratif avec une suite d'agents IA conçus pour le quotidien du manager de restaurant.",
    "heroTagline": "Plus de contrôle opérationnel, moins de feuilles volantes",
    "badge": "Pour les managers et gérants",
    "painsTitle": "Ce qu'un Manager de Restaurant Ne Peut Pas Laisser de Côté",
    "pains": [
      "Établir les plannings chaque semaine en respectant la convention, la durée légale du travail et les repos, sans erreurs ni surcoûts",
      "Contrôler les pertes, l'inventaire et les achats avec des fournisseurs différents qui changent de prix chaque semaine",
      "Tenir l'APPCC à jour et préparer les inspections sans stress ni accumulation de paperasse",
      "Rendre compte au propriétaire avec des données consolidées et des dashboards professionnels, pas dans des Excel improvisés",
      "Coordonner l'équipe de cuisine et de salle avec une communication claire et une formation rapide du nouveau personnel",
      "Gérer l'opérationnel des pics de service sans perdre en qualité ni négliger la salle"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Manager",
    "features": [
      {
        "icon": "BriefcaseBusiness",
        "title": "Manager de Restaurant Pro",
        "description": "Agent spécialisé pour vous accompagner dans les décisions opérationnelles, la gestion d'équipe et le reporting au propriétaire."
      },
      {
        "icon": "Calendar",
        "title": "Plannings et contrôle des horaires",
        "description": "Kit Gestión de Personal : plannings en quelques minutes en respectant la convention, contrôle des heures, ratios de productivité."
      },
      {
        "icon": "Package",
        "title": "Inventaire et contrôle des achats",
        "description": "Kit Inventario : modèles Excel prêts à l'emploi, alertes de stock minimum, comparatif fournisseurs et pertes."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC et traçabilité",
        "description": "Pack APPCC avec 19 registres, alertes de température depuis le mobile et feuilles prêtes pour l'inspection."
      },
      {
        "icon": "BarChart3",
        "title": "KPI et reporting au propriétaire",
        "description": "Ratios de cuisine et de salle, productivité, ticket moyen. Dashboards exportables en PDF directement depuis Excel."
      },
      {
        "icon": "CheckSquare",
        "title": "Tâches récurrentes par service",
        "description": "Modèles prêts par concept : ouverture, fermeture, mise en place et service dans un kit unique par type d'établissement."
      },
      {
        "icon": "Users",
        "title": "Repas du Personnel",
        "description": "Générateur de menus du staff qui réduit les coûts tout en gardant l'équipe motivée et bien nourrie."
      },
      {
        "icon": "MessageSquare",
        "title": "Coach Mental",
        "description": "Coaching psychologique pour gérer les conversations difficiles, le stress et la motivation de l'équipe."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Allergènes",
        "description": "Identification automatique des allergènes par plat, prête pour la réglementation et pour la salle."
      }
    ],
    "workflowTitle": "Une journée réelle d'un manager avec AI Chef Pro",
    "workflow": [
      "08:30 · Ouverture — vous imprimez la checklist du service depuis le Kit de Tareas et vérifiez l'inventaire en 10 minutes.",
      "09:30 · Manager de Restaurant Pro — l'agent vous résume les incidents de la veille et les actions en attente.",
      "10:30 · Kit Inventario — vous validez les commandes fournisseurs avec comparatif des prix et alertes de stock minimum.",
      "12:30 · Service du midi — l'équipe enregistre les pertes et les températures depuis le mobile avec le Pack APPCC.",
      "15:30 · Planning de la semaine prochaine — vous ouvrez le Kit Gestión de Personal et bouclez le planning en 20 minutes en respectant la convention.",
      "17:00 · Repas du Personnel — vous générez le menu du staff de la semaine prochaine avec des ingrédients que vous avez déjà en chambre froide.",
      "19:00 · Conversation difficile — vous utilisez Coach Mental pour préparer l'entretien avec un cuisinier qui arrive régulièrement en retard.",
      "23:30 · Fermeture — vous générez le rapport quotidien avec les ratios et l'envoyez au propriétaire par WhatsApp en un clin d'œil."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Managers",
    "productIds": [
      "kit-gestion-personal",
      "kit-inventario",
      "pack-appcc",
      "kit-tareas",
      "kit-escandallos",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Avant, je passais 8 heures par semaine à faire les plannings et les commandes fournisseurs. Maintenant, je boucle tout en 2 heures avec le Kit Gestión de Personal et le Kit Inventario. AI Chef Pro m'a rendu du temps pour être en salle avec l'équipe, là où un manager doit être.",
    "testimonialAuthor": "Marta Ruiz",
    "testimonialRole": "Manager, restaurant décontracté de 80 couverts",
    "faqTitle": "Questions Fréquentes des Managers",
    "faqs": [
      {
        "q": "Est-ce que ça fonctionne si je gère 1 établissement ou si j'en ai plusieurs ?",
        "a": "Dans les deux cas. Les modèles s'adaptent au volume et vous pouvez consolider le reporting de plusieurs établissements dans un seul dashboard. Certains clients ont 1 établissement, d'autres plus de 10 unités actives."
      },
      {
        "q": "Remplace-t-il le logiciel de réservation ou le logiciel de caisse ?",
        "a": "Non, il complète. Cover Manager ou The Fork gèrent les réservations et le logiciel de caisse gère les ventes ; AI Chef Pro gère les coûts, le personnel, l'APPCC, l'inventaire et l'opérationnel interne. Les données sont parfaitement compatibles via Excel."
      },
      {
        "q": "L'équipe a-t-elle besoin de formation ?",
        "a": "Minimale. Les modèles et les agents sont en espagnol et tout démarre avec l'agent « Qui suis-je ? », qui adapte le système à vous en 2 minutes. La courbe d'apprentissage réelle de l'équipe est de 1 à 2 jours avec l'onboarding en vidéo et le support par WhatsApp."
      },
      {
        "q": "Puis-je exporter les données pour mon gestionnaire ou le propriétaire ?",
        "a": "Oui. Tout s'exporte en Excel et PDF au format professionnel. Les cabinets comptables reçoivent une documentation propre et les propriétaires reçoivent des dashboards avec des KPI clairs directement sur WhatsApp."
      },
      {
        "q": "Comment m'aide-t-il avec les conversations difficiles de l'équipe ?",
        "a": "Coach Mental est un agent de coaching psychologique pour les professionnels de la restauration qui vous aide à structurer les conversations difficiles (licenciements, retards, conflits entre cuisine et salle) avec des arguments et une structure claire avant la réunion."
      },
      {
        "q": "Existe-t-il des modèles spécifiques par concept d'établissement ?",
        "a": "Oui. Il existe des Kits de Tareas spécifiques pour le décontracté, la cafétéria, la pizzeria, le burger, la dark kitchen, la pâtisserie, le bar, le traiteur, l'hôtel, la glacerie, la chocolaterie, le restaurant créatif et le chef privé. Chacun avec des modèles adaptés à l'opérationnel réel."
      }
    ],
    "ctaTitle": "Faites passer l'exploitation de votre restaurant au niveau supérieur.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10.000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Managers et Gérants de Restaurant : Plannings, APPCC et Reporting | AI Chef Pro",
      "description": "Suite IA pour managers de restaurant : plannings, inventaire, APPCC, KPI et reporting au propriétaire avec des agents spécialisés en restauration. Commencez dès aujourd'hui.",
      "keywords": "IA manager restaurant, manager restaurant IA, logiciel manager restaurant, gestion opérationnelle restaurant IA, plannings horaires restaurant, APPCC manager, KPI restaurant, agent IA restauration, manager restaurant Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/gerente-restaurante.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre restaurant dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes dans lequel vous lui expliquez quel type de restaurant vous gérez, dans quelle ville, combien de convives vous recevez et comment vous travaillez. À partir de ce moment, chaque agent — des plannings au reporting — répond adapté à votre contexte : convention du pays, taille de votre équipe, pics de service réels. Ce n'est pas un formulaire : c'est une conversation courte qui rend la suite véritablement utile pour votre quotidien de manager.",
    "appsTitle": "Les Agents IA que vous allez utiliser en tant que manager",
    "apps": [
      {
        "name": "Manager de Restaurant Pro",
        "category": "Gastro Profile Pro",
        "description": "Agent principal : décisions opérationnelles, gestion d'équipe et reporting au propriétaire."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'Entreprise",
        "description": "Spécialiste des bistrots, gastrobars, tapas et méditerranéen : tout le spectre décontracté."
      },
      {
        "name": "Repas du Personnel",
        "category": "Gastro Profile Pro",
        "description": "Générateur de menus du staff qui réduit les coûts et motive l'équipe."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises sur les pertes et les rendements par ingrédient, essentielles pour le contrôle en cuisine."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette et par plat."
      },
      {
        "name": "Conversor Ing",
        "category": "Outils et Utilitaires",
        "description": "Convertisseur de poids et mesures pour la cuisine professionnelle."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Calculatrice de portions qui adapte les recettes à n'importe quel nombre de convives."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching psychologique pour les professionnels de la restauration : stress, conversations difficiles et motivation de l'équipe."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Descriptions de plats optimisées pour le SEO local sur Google et le site web du restaurant."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Calendrier gastronomique avec dates clés, idées et hashtags pour les réseaux sociaux et le blog."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de plats professionnels avec recette + fiche technique CSV à charger dans le Kit de Escandallos Pro."
      }
    ],
    "metrics": [
      {
        "value": "−75 %",
        "label": "temps sur les plannings et les commandes"
      },
      {
        "value": "×4",
        "label": "vitesse de reporting au propriétaire"
      },
      {
        "value": "−40 %",
        "label": "pertes après contrôle systématique"
      },
      {
        "value": "11+",
        "label": "agents IA pour votre rôle"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "8 heures par semaine à faire les plannings dans Excel à la main et avec des notes de fournisseurs",
        "APPCC sur papier imprimé qui se perd ou arrive incomplet à l'inspection",
        "Reporting au propriétaire dans des fichiers dispersés par e-mail sans structure",
        "Pertes enregistrées au jugé, sans traçabilité réelle ni alertes",
        "Repas du personnel improvisé qui fait exploser les coûts sans que personne ne s'en aperçoive"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "2 heures par semaine à boucler les plannings avec un modèle professionnel en respectant la convention",
        "APPCC depuis le mobile avec registres, températures et alertes, prêt pour l'inspection",
        "Reporting au propriétaire en PDF direct depuis le Kit Plan Financiero, avec des dashboards clairs",
        "Contrôle systématique des pertes avec des données précises et des alertes de stock",
        "Repas du personnel généré avec l'IA en respectant le coût cible et la motivation de l'équipe"
      ]
    },
    "galleryTitle": "Le Quotidien d'un Manager, en Images",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : planification des horaires, gestion de la cuisine et de la salle, inventaire, service et reporting.",
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
    "h1": "IA pour Directeurs des Opérations de Groupes de Restauration",
    "heroSubtitle": "Standardisez les processus, consolidez le reporting et multipliez la productivité opérationnelle dans les groupes multi-établissements avec une suite d'agents IA spécialisés en hôtellerie-restauration.",
    "heroTagline": "Même standard dans tous les établissements, données consolidées en un clic",
    "badge": "Pour les directeurs des opérations de groupes",
    "painsTitle": "Ce qu'un Directeur des Opérations Multi-Établissements Ne Peut Pas Ignorer",
    "pains": [
      "Maintenir le même standard de qualité, de processus et d'expérience dans tous les établissements du groupe",
      "Consolider les KPIs financiers, opérationnels et d'équipe pour comparer les performances entre unités",
      "Répliquer les manuels opérationnels, la formation et l'onboarding sans perdre en qualité lorsque le réseau grandit",
      "Détecter à temps les établissements avec des écarts de food cost, de personnel ou de productivité avant qu'ils ne saignent la marge",
      "Coordonner les managers de chaque établissement avec une communication claire et un reporting cohérent",
      "Faire évoluer le groupe en ouvrant de nouvelles unités sans avoir à réinventer la roue à chaque ouverture"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Directeur des Opérations",
    "features": [
      {
        "icon": "Building2",
        "title": "Standardisation multi-établissements",
        "description": "Manuels, checklists et procédures uniformes qui se répliquent à toutes les unités du groupe en un clic."
      },
      {
        "icon": "BarChart3",
        "title": "Dashboards consolidés",
        "description": "Kit Plan Financiero : comparez le food cost, la productivité, les pertes et le ticket moyen entre tous vos restaurants dans une seule vue."
      },
      {
        "icon": "ChefHat",
        "title": "Chef Exécutif Pro",
        "description": "Agent qui standardise les recettes et les fiches techniques pour que le même plat sorte identique dans 1, 5 ou 25 cuisines."
      },
      {
        "icon": "BriefcaseBusiness",
        "title": "Manager de Restaurant Pro",
        "description": "Assistant pour chaque manager local qui remonte des données consolidées au directeur des opérations."
      },
      {
        "icon": "BookOpen",
        "title": "Manuels opérationnels avec IA",
        "description": "Onboarding, formation des équipes et procédures toujours à jour depuis un référentiel central unique."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC corporatif unifié",
        "description": "Un seul système documentaire pour toutes les unités du groupe : traçabilité et températures centralisées."
      },
      {
        "icon": "TrendingDown",
        "title": "Audit des coûts par établissement",
        "description": "Rendement GenCal et Kit de Escandallos Pro détectent les écarts de food cost avant qu'ils ne deviennent incontrôlables."
      },
      {
        "icon": "Users",
        "title": "Quadrants et structure d'équipe",
        "description": "Kit Gestión de Personal : même structure de quarts, ratios et productivité dans toutes les unités."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Recherche approfondie des tendances, concurrents et marchés pour les décisions stratégiques d'expansion."
      }
    ],
    "workflowTitle": "Une journée réelle d'un Directeur des Opérations avec AI Chef Pro",
    "workflow": [
      "08:30 · Café et Kit Plan Financiero — vous ouvrez le dashboard consolidé des 7 établissements du groupe et vous détectez que l'établissement 4 a un food cost à 33 % (+3 pp par rapport à l'objectif).",
      "09:30 · Manager de Restaurant Pro — vous demandez à l'agent une analyse automatisée de la cause par établissement. Il identifie un problème de rendement du poisson.",
      "10:30 · Visioconférence avec la manager de l'établissement 4, appuyée sur des données réelles du Kit Plan Financiero, pas sur l'intuition.",
      "12:00 · Chef Exécutif Pro — vous mettez à jour la procédure de manipulation du poisson et elle est répliquée dans les 7 cuisines comme nouvelle version du manuel.",
      "15:30 · Quadrants consolidés — vous révisez le Kit Gestión de Personal avec les ratios de productivité de tous les établissements et vous signez l'onboarding de la nouvelle manager de l'établissement 8.",
      "17:00 · Sonar Deep Research — vous étudiez le marché pour la prochaine ouverture dans une autre ville : analyse des zones, ticket moyen et concurrence.",
      "19:00 · Réunion avec le comité — vous exportez les KPIs du trimestre en PDF directement depuis le Kit Plan Financiero. Réunion terminée en 45 minutes.",
      "21:30 · Clôture — les 7 managers vous envoient le rapport automatique du jour par WhatsApp. Vous rentrez chez vous avec une vision complète du groupe."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Groupes de Restauration",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-tareas"
    ],
    "testimonialQuote": "Nous gérons 7 établissements et avant, chacun fonctionnait différemment : des Excel différents, des manuels différents, des APPCC différents. Avec AI Chef Pro, nous avons le même standard partout et un reporting consolidé dans une seule vue. Détecter l'établissement à problèmes est passé de 2 semaines à 1 jour.",
    "testimonialAuthor": "Javier Ortega",
    "testimonialRole": "Directeur des Opérations, groupe de restauration avec 7 établissements",
    "faqTitle": "Questions Fréquentes des Directeurs des Opérations",
    "faqs": [
      {
        "q": "Combien d'établissements AI Chef Pro prend-il en charge ?",
        "a": "Sans limite réelle. Il y a des clients avec 1 établissement et d'autres avec plus de 25 unités actives. Les plans entreprise évoluent selon les usages et débloquent des dashboards consolidés, un onboarding personnalisé et un support prioritaire."
      },
      {
        "q": "S'intègre-t-il avec notre ERP ou système comptable ?",
        "a": "Les modèles exportent en Excel, PDF et CSV dans des formats compatibles avec la plupart des ERP et systèmes comptables. Votre équipe financière reçoit une documentation prête à intégrer."
      },
      {
        "q": "Permet-il des rôles et des permissions par établissement ?",
        "a": "Oui. Vous pouvez donner un accès par manager local, par directeur régional ou consolidé au directeur des opérations. Chaque niveau ne voit que les données qui le concernent."
      },
      {
        "q": "Comment garantit-on le même standard dans toutes les unités ?",
        "a": "Chef Exécutif Pro standardise les recettes et les fiches techniques ; le Pack APPCC unifie la traçabilité ; le Kit de Escandallos Pro maintient les mêmes calculs dans tous les établissements. Les manuels se répliquent en un clic et se mettent à jour depuis un point unique."
      },
      {
        "q": "Y a-t-il des réductions pour les groupes avec plusieurs établissements ?",
        "a": "Oui. À partir de 5 unités actives, il existe des plans entreprise avec onboarding personnalisé, dashboards consolidés, formation de l'équipe centrale et support prioritaire."
      },
      {
        "q": "Cela sert-il à ouvrir de nouveaux emplacements plus rapidement ?",
        "a": "Oui. C'est l'un des cas d'usage les plus récurrents : les guides Comment Monter… (dark kitchen, restaurant gastronomique, casual, mexicain, japonais, péruvien, nikkei) sont des roadmaps professionnelles qui accélèrent les ouvertures avec plan financier, business plan et manuels réplicables."
      }
    ],
    "ctaTitle": "Standardisez votre groupe. Même standard dans tous les établissements.",
    "ctaSubtitle": "Parlez-nous pour un onboarding personnalisé pour votre groupe ou commencez avec le plan Membre : 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "IA pour Directeurs des Opérations de Groupes de Restauration | AI Chef Pro",
      "description": "Suite IA pour groupes de restauration multi-établissements : dashboards consolidés, standardisation des recettes, APPCC corporatif, manuels réplicables et plan financier par unité.",
      "keywords": "IA groupe restauration, logiciel multi-établissements restaurants, directeur opérations restaurants IA, standardiser processus restaurant, dashboards consolidés restaurant, faire évoluer groupe restauration, multi-établissements IA hôtellerie-restauration",
      "ogImage": "https://aichef.pro/og/use-cases/director-operaciones-grupo.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre groupe dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous lui indiquez combien d'établissements vous gérez, quels concepts vous exploitez (casual, gastronomique, dark kitchen, hôtel), dans quels pays et comment votre organisation fonctionne. À partir de ce moment, chaque agent — du Plan Financier aux manuels opérationnels — répond adapté à l'échelle et à la structure réelle du groupe. Ce n'est pas un formulaire : c'est une conversation courte qui rend la suite véritablement utile pour les directeurs des opérations multi-établissements.",
    "appsTitle": "Les Agents IA que vous allez utiliser en tant que Directeur des Opérations",
    "apps": [
      {
        "name": "Chef Exécutif Pro",
        "category": "Gastro Profile Pro",
        "description": "Standardisation des recettes, fiches techniques et manuels réplicables à toutes les unités du groupe."
      },
      {
        "name": "Manager de Restaurant Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistant pour chaque manager local avec reporting consolidé vers le haut."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'Affaires",
        "description": "Spécialiste des bistrots, gastrobars et casual : le spectre le plus courant dans les groupes multi-établissements."
      },
      {
        "name": "Burger Pro AI+",
        "category": "Concepts d'Affaires",
        "description": "Pour les groupes avec des marques de hamburger gourmet ou fast casual."
      },
      {
        "name": "Traiteur IA+",
        "category": "Concepts d'Affaires",
        "description": "Pour les groupes avec une division traiteur et événements d'entreprise."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche approfondie des tendances, concurrents et marchés pour les décisions stratégiques."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises sur les pertes et rendements par ingrédient, essentielles pour l'audit multi-établissements."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette, unifiée dans toutes les unités."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles de blog pour attirer du trafic organique pour chaque unité du groupe."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Recherche de mots-clés par zone postale de chaque établissement."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie gastronomique avec IA unifiée pour toute la marque du groupe."
      }
    ],
    "metrics": [
      {
        "value": "−14 j",
        "label": "détecter un établissement avec des écarts"
      },
      {
        "value": "×7",
        "label": "vitesse de reporting consolidé"
      },
      {
        "value": "+3 pp",
        "label": "marge après standardisation"
      },
      {
        "value": "11+",
        "label": "agents pour multi-établissements"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "7 établissements avec 7 Excel différents, des manuels hétérogènes et un APPCC incohérent",
        "Détecter un établissement avec des écarts prend 2 semaines car il n'y a pas de reporting consolidé",
        "Onboarding d'un nouveau manager en 1 mois avec des matériaux improvisés de chaque unité",
        "Reporting au comité avec des fichiers dispersés et sans dashboards professionnels",
        "Décisions d'expansion par intuition, sans analyse de marché approfondie"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Même standard répliqué dans les 7 unités : recettes, manuels et APPCC unifiés",
        "Détecter un établissement avec des écarts en 1 jour avec le dashboard consolidé du Kit Plan Financiero",
        "Onboarding d'un nouveau manager en 1 semaine avec des manuels et une formation réplicables",
        "Reporting au comité en PDF direct depuis le Kit Plan Financiero avec des KPIs consolidés",
        "Décisions d'expansion appuyées sur Sonar Deep Research et des guides Comment Monter… professionnels"
      ]
    },
    "galleryTitle": "Le Quotidien d'un Directeur des Opérations, en Images",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : dashboards multi-établissements, réunions de stratégie, audits d'unités, manuels corporatifs et onboarding des managers.",
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
    "h1": "IA pour Chef Exécutif et Chef Corporate",
    "heroSubtitle": "Créez des recettes standardisées, des fiches de coût précises et des manuels réplicables pour 1, 5 ou 25 cuisines. Une suite d'agents d'IA gastronomique conçus pour l'un des rôles les plus exigeants de la cuisine professionnelle.",
    "heroTagline": "Votre équipe créative et opérationnelle, amplifiée à la vitesse d'une conversation",
    "badge": "Pour chefs exécutifs et corporate",
    "painsTitle": "Ce qu'un Chef Exécutif doit absolument résoudre",
    "pains": [
      "Standardiser des recettes dans des cuisines géographiquement dispersées sans que chaque établissement les interprète à sa manière",
      "Finaliser des fiches de coût précises pour chaque fiche technique avec des produits de saison dont le prix change chaque semaine",
      "Renouveler la carte toutes les 6-12 semaines sans que l'équipe se noie dans la paperasse",
      "Maintenir les manuels de cuisine et l'onboarding à jour quand il y a une rotation constante du personnel",
      "Innover dans le menu saisonnier sans perdre le food cost cible ni la marge réelle",
      "Rendre compte à la direction avec des KPIs clairs : rentabilité par plat, productivité de la brigade et pertes"
    ],
    "featuresTitle": "Comment AI Chef Pro aide un Chef Exécutif",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Chef Exécutif Pro",
        "description": "Agent d'IA spécialisé dans le rôle : standardisation multi-site, fiches techniques, manuels de cuisine et décisions de carte basées sur des données réelles."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative + Food Pairing AI",
        "description": "Brainstorming de plats par saison, ingrédient ou technique, avec des combinaisons appuyées sur une base scientifique. Cuisine Créative fournit également la recette détaillée et une fiche de coût initiale avec des prix de référence du marché, téléchargeable en CSV."
      },
      {
        "icon": "Calculator",
        "title": "Fiches de coût professionnelles",
        "description": "Vous chargez le CSV de Cuisine Créative dans le Kit de Escandallos Pro et remplacez les prix de référence par ceux de vos fournisseurs réels. Coût par portion, food cost %, marge et prix suggéré instantanément. Recalcule automatiquement lorsque vous modifiez un grammage ou un coût."
      },
      {
        "icon": "BookOpen",
        "title": "Fiches techniques professionnelles",
        "description": "Recette, procédure, allergènes, dressage et storytelling dans un document unique. Prêt à envoyer à toutes les cuisines du groupe."
      },
      {
        "icon": "Layers",
        "title": "Standardisation multi-site",
        "description": "Même plat, même qualité et même coût dans 1, 5 ou 25 unités. Manuels réplicables et entièrement traçables."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+ et techniques avancées",
        "description": "Koji, kombuchas, shoyus, garums et lactofermentations : R&D gastronomique avec un soutien professionnel."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Allergènes et Rendement GenCal",
        "description": "Détection automatique des allergènes par plat et données précises sur les pertes et les rendements par ingrédient."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Recherche gastronomique approfondie : tendances, techniques émergentes, producteurs et produits de saison."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Photographie gastronomique générée par IA pour les fiches techniques, la communication interne et les communiqués de presse."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Chef Exécutif avec AI Chef Pro",
    "workflow": [
      "Matin, 09:00 · Cuisine Créative — brainstorming de 12 plats pour le menu d'automne à partir de produits de saison locaux. L'agent vous remet une recette détaillée et une fiche de coût initiale avec des prix de référence du marché, téléchargeable en CSV.",
      "Matin, 10:30 · Kit de Escandallos Pro — vous chargez les 12 CSV de Cuisine Créative, remplacez les prix de référence par ceux de vos fournisseurs réels et écartez 4 plats qui ne correspondent pas à votre food cost cible (28 %).",
      "Midi, 12:00 · Food Pairing AI — vous travaillez les accords des 8 finalistes et validez des harmonies inattendues.",
      "Après-midi, 15:00 · ID Allergènes — vous générez la fiche d'allergènes par plat, prête pour la réglementation et pour la salle.",
      "Après-midi, 16:30 · Chef Exécutif Pro — vous rédigez la fiche technique complète avec procédure, grammages, dressage et storytelling.",
      "Après-midi, 18:00 · GastroIMG Gen+ — vous générez les photos de chaque plat pour le manuel interne et le communiqué de presse.",
      "Après-midi, 18:30 · Vous répliquez le manuel aux 5 cuisines du groupe. Ce qu'un processus traditionnel boucle en 15-30 jours, vous le bouclez en 1-3 journées selon la taille de la carte."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Chefs Exécutifs",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-plan-financiero",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Avant, il me fallait entre 15 et 20 jours pour finaliser une nouvelle carte entre brainstorming, tests, fiches de coût, fiches techniques et communication interne. Avec AI Chef Pro, je le fais en 2 ou 3 jours selon la taille de la carte et s'il s'agit d'une réingénierie complète ou partielle. La différence n'est pas seulement une question de temps : l'équipe reçoit une documentation professionnelle et réplicable, pas des notes manuscrites.",
    "testimonialAuthor": "Diego Saavedra",
    "testimonialRole": "Chef Exécutif, groupe de 5 restaurants méditerranéens",
    "faqTitle": "Questions Fréquentes des Chefs Exécutifs",
    "faqs": [
      {
        "q": "Les agents d'IA d'AI Chef Pro comprennent-ils la cuisine professionnelle ou sont-ils des chatbots généralistes ?",
        "a": "Ce sont des agents spécialisés. Cuisine Créative, Food Pairing AI, Fermentus Avec AI+ et Chef Exécutif Pro sont entraînés avec des connaissances gastronomiques professionnelles : techniques, fiches de coût réelles, rentabilité, grammages et découpes. Ce ne sont pas des ChatGPT génériques : ce sont des outils conçus pour quelqu'un qui sait déjà cuisiner."
      },
      {
        "q": "Puis-je télécharger mon recueil de recettes existant ?",
        "a": "Oui. Le Kit de Escandallos Pro permet de charger votre recueil de recettes et d'appliquer un calcul de coût automatisé en quelques minutes. Vous pouvez également demander à l'agent Chef Exécutif Pro de générer des fiches techniques à partir de descriptions libres."
      },
      {
        "q": "Est-ce que cela convient à la cuisine gastronomique avancée ou seulement à la cuisine décontractée ?",
        "a": "Pour tout le spectre. Il existe des agents spécifiques : Cuisine Créative pour la cuisine d'auteur, Pâtisserie Créative, Fermentus pour l'avant-garde, VegChef pour le plant-based, en plus de plus de 25 recueils de recettes par pays. Des cas réels au Michelin et aux Soles Repsol, ainsi que dans des groupes décontractés allant jusqu'à 25 unités."
      },
      {
        "q": "Comment le système s'adapte-t-il à ma façon de travailler ?",
        "a": "Commencez avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes dans lequel vous lui racontez qui vous êtes, où vous travaillez, votre type de cuisine et à quelle échelle. À partir de ce moment, tous les agents s'adaptent à votre contexte : prix locaux, réglementation de votre pays, cuisine du territoire et échelle de votre opération."
      },
      {
        "q": "Y a-t-il quelque chose de spécifique pour les groupes multi-site et les chaînes de restauration ?",
        "a": "Oui. L'agent Chef Exécutif Pro est conçu pour la standardisation : même fiche technique, même fiche de coût et mêmes manuels répliqués dans toutes les unités. Combiné avec le Kit Plan Financiero, vous pouvez consolider le reporting des KPIs par unité et par groupe."
      },
      {
        "q": "Y a-t-il une bibliothèque de prompts spécifiques pour les chefs ?",
        "a": "Oui. Le Pro Prompts eBook comprend plus de 300 prompts éprouvés pour la créativité, le calcul de coût, les fiches techniques, la formation, la communication interne et l'opérationnel de cuisine, organisés par situation d'utilisation."
      },
      {
        "q": "Combien de temps faut-il pour que l'abonnement soit rentabilisé ?",
        "a": "La plupart des chefs exécutifs constatent un retour sur investissement dès la première nouvelle carte. Un changement de menu traditionnel prend entre 15 et 30 jours entre brainstorming, tests, fiches de coût, fiches techniques et communication interne. Avec AI Chef Pro et un bon flux dans Excel ou Google Workspace, ce même processus passe à entre 1 et 3 jours selon la taille de la carte et s'il s'agit d'une réingénierie totale ou partielle. Avec 4-6 changements de carte par an, vous récupérez entre 60 et 120 journées de travail."
      }
    ],
    "ctaTitle": "Créez, chiffrez et répliquez des recettes à la vitesse d'une conversation.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10.000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Chef Exécutif : Recettes, Fiches de Coût et Manuels | AI Chef Pro",
      "description": "Suite d'IA pour chef exécutif et corporate : agent Chef Exécutif Pro, fiches de coût automatiques, fiches techniques et manuels réplicables multi-site. Commencez dès aujourd'hui.",
      "keywords": "IA chef exécutif, chef exécutif IA, logiciel chef corporate, agent IA gastronomique, fiches de coût automatiques, fiches techniques restaurant, recettes standardisées multi-site, manuels de cuisine IA, food pairing IA, IA pour groupes de restauration, chef exécutif Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/chef-ejecutivo.jpg"
    },
    "personalizationTitle": "Personnalisé pour Vous dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec un onboarding conversationnel de 2 minutes — l'agent « Qui suis-je ? » — dans lequel vous lui racontez qui vous êtes, où vous travaillez, quel type de cuisine vous dirigez et à quelle échelle vous opérez. À partir de ce moment, chaque agent — des fiches de coût à la créativité — répond en s'adaptant à votre contexte : votre cuisine locale, votre réglementation, vos prix de marché et la taille de votre brigade. Ce n'est pas un formulaire : c'est une conversation courte qui donne du sens à tout ce qui suit.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser en tant que Chef Exécutif",
    "apps": [
      {
        "name": "Chef Exécutif Pro",
        "category": "Gastro Profile Pro",
        "description": "Agent principal : standardisation multi-site, fiches techniques et décisions de carte."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de plats professionnels avec recette détaillée et fiche de coût initiale téléchargeable en CSV (prix de référence du marché), prête à charger dans le Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Combinaisons d'ingrédients et accords avec une base scientifique."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "Fermentation créative : koji, kombucha, shoyu, miso, garum et lactofermentations."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises sur les pertes et les rendements par ingrédient. Essentiel pour un calcul de coût réaliste."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Calculatrice de portions qui adapte les recettes à n'importe quel nombre de convives."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes potentiels par recette et par plat."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Desserts de restaurant créatifs avec une technique de pâtisserie professionnelle."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Assistant de sélection et de technique avec le catalogue professionnel de Sosa."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue tSpoonLab pour les techniques et applications avancées."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche approfondie : tendances, producteurs et techniques émergentes."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie gastronomique générée par IA pour les fiches techniques et la presse."
      },
      {
        "name": "Gastro Lexicum",
        "category": "Gastro Connaissance",
        "description": "Tuteur avec des définitions de techniques, processus, additifs et science gastronomique."
      }
    ],
    "metrics": [
      {
        "value": "−90 %",
        "label": "temps pour finaliser une nouvelle carte"
      },
      {
        "value": "×10",
        "label": "vitesse de création des fiches techniques"
      },
      {
        "value": "+4 pp",
        "label": "marge grâce à un meilleur calcul de coût"
      },
      {
        "value": "13+",
        "label": "agents d'IA pour votre rôle"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Finalisation d'une nouvelle carte : entre 15 et 30 jours, selon la standardisation du processus",
        "Recueil de recettes sur feuilles volantes, documents Word désordonnés et notes manuscrites",
        "Chaque établissement interprète la recette à sa manière et le résultat varie",
        "Calcul de coût manuel avec calculatrice : vous modifiez un grammage et vous réécrivez tout",
        "Manuels et onboarding constamment obsolètes"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Finalisation d'une nouvelle carte : entre 1 et 3 jours selon la taille et s'il s'agit d'une réingénierie totale ou partielle",
        "Recueil de recettes centralisé avec calcul de coût, allergènes, technique et storytelling",
        "Même plat, même qualité et même coût dans 1, 5 ou 25 cuisines",
        "Calcul de coût professionnel qui recalcule instantanément à chaque modification",
        "Manuels mis à jour en un clic et onboarding prêt pour les nouveaux chefs"
      ]
    },
    "appUrlPath": "/agents/chef-ejecutivo-pro",
    "galleryTitle": "Le Quotidien d'un Chef Exécutif, en Images",
    "gallerySubtitle": "Ce que vous allez pouvoir gérer avec AI Chef Pro : brigade, fiches techniques, créativité, fiches de coût et communication interne.",
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
    "h1": "IA pour Chef de Cuisine et Chef Exécutif",
    "heroSubtitle": "Gérez les postes, les fiches techniques, la mise en place et la formation de l'équipe avec une suite d'agents IA conçus pour le quotidien du chef de cuisine professionnel.",
    "heroTagline": "Plus de cuisine, moins de paperasse",
    "badge": "Pour les chefs de cuisine et les chefs exécutifs",
    "painsTitle": "Ce Qu'un Chef de Cuisine Doit Absolument Résoudre",
    "pains": [
      "Calculer le food cost précis de chaque plat et de la carte complète avec un produit qui change de prix chaque semaine",
      "Coordonner la mise en place et les postes sans accrocs aux heures de pointe",
      "Maintenir l'APPCC à jour sans que la paperasse ne vole du temps à la cuisine",
      "Former et superviser l'équipe aux techniques et procédures standardisées avec une rotation fréquente",
      "Renouveler la carte chaque saison en maintenant la marge et en respectant le produit local",
      "Communiquer avec la salle, la direction et les fournisseurs avec une documentation professionnelle, pas des notes dans un carnet"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Chef de Cuisine",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Chef Exécutif Pro",
        "description": "Agent spécialisé pour vous accompagner dans la standardisation des recettes, des fiches techniques et des manuels de cuisine."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative + Food Pairing AI",
        "description": "Brainstorming pour de nouveaux plats avec une base professionnelle. Cuisine Créative fournit recette + coût CSV avec prix de référence, prêt pour le Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Coûts professionnels",
        "description": "Kit de Escandallos Pro : vous chargez le CSV de Cuisine Créative, remplacez les prix par les réels et obtenez coût, food cost % et marge instantanément."
      },
      {
        "icon": "BookOpen",
        "title": "Fiches techniques professionnelles",
        "description": "Recette, procédure, allergènes, dressage et storytelling dans un document unique prêt à imprimer."
      },
      {
        "icon": "CheckSquare",
        "title": "Tâches et mise en place",
        "description": "Kit de Tareas avec des modèles spécifiques par concept : ouverture, fermeture, postes et service."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC et traçabilité",
        "description": "Pack APPCC avec 19 registres : températures, pertes, allergènes et traçabilité depuis le mobile de l'équipe."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "R&D gastronomique : koji, kombuchas, shoyus, garums et lactofermentations avec un appui professionnel."
      },
      {
        "icon": "GraduationCap",
        "title": "Pro Prompts eBook",
        "description": "Plus de 300 prompts testés pour la créativité, le coût, les fiches techniques, la formation et l'exploitation de cuisine."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Allergènes et Rendement GenCal",
        "description": "Détection automatique des allergènes par plat et données précises sur les pertes et rendements par ingrédient."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Chef de Cuisine avec AI Chef Pro",
    "workflow": [
      "08:00 · Ouverture — vous imprimez la mise en place du jour depuis le Kit de Tareas et validez les commandes fournisseurs avec le Kit Inventario.",
      "09:00 · Cuisine Créative — vous développez un plat hors carte pour le week-end avec un produit bien placé en prix. Vous recevez recette + coût CSV.",
      "10:30 · Kit de Escandallos Pro — vous chargez le CSV, appliquez vos prix réels et validez que le food cost correspond à 28 %.",
      "12:30 · Service — l'équipe enregistre les pertes et les températures depuis le mobile avec le Pack APPCC. Vous êtes en cuisine, pas au bureau.",
      "15:30 · Briefing rapide avec la brigade pour revoir le plat du jour et ajuster la mise en place.",
      "17:00 · Pro Prompts eBook — vous demandez à l'agent de générer le script de la formation d'un nouveau cuisinier qui arrive demain.",
      "19:30 · Service du soir — vous coordonnez les passes avec l'équipe en vous appuyant sur les fiches techniques centralisées.",
      "23:30 · Fermeture — vous signez l'APPCC du jour, générez le rapport et il part sur le WhatsApp du propriétaire en 10 minutes."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Chefs de Cuisine",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "kit-tareas",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Le Kit de Escandallos et le Pack APPCC m'ont fait gagner 5 heures de paperasse par semaine. Mais ce que j'utilise le plus, c'est Cuisine Créative pour les plats hors carte du week-end : en une matinée, je finalise recette, coût et fiche technique. Avant, c'était une semaine entière.",
    "testimonialAuthor": "Lucía Romero",
    "testimonialRole": "Chef de Cuisine, restaurant méditerranéen de 70 couverts",
    "faqTitle": "Questions Fréquentes des Chefs de Cuisine",
    "faqs": [
      {
        "q": "Devez-vous être expert en Excel ?",
        "a": "Non. Les modèles du Kit de Escandallos Pro et du Pack APPCC ont des formules préchargées, vous n'avez qu'à saisir les données. Il y a un tutoriel vidéo de 5 minutes pour démarrer."
      },
      {
        "q": "Est-ce utile si notre carte change chaque mois ou chaque saison ?",
        "a": "C'est le cas idéal. Cuisine Créative génère de nouveaux plats avec coût en CSV, vous le chargez dans le Kit de Escandallos Pro avec vos prix et exportez les fiches techniques. Ce qui était une semaine de travail devient une journée."
      },
      {
        "q": "L'IA comprend-elle les termes professionnels de cuisine ?",
        "a": "Oui. Cuisine Créative, Food Pairing AI, Fermentus Avec AI+ et les recueils de recettes par pays (italienne, mexicaine, japonaise, péruvienne, etc.) sont entraînés avec des connaissances gastronomiques professionnelles : techniques, coûts, grammages, découpes, dressage et storytelling. Ce ne sont pas des ChatGPT génériques."
      },
      {
        "q": "Comment s'adapte-t-il à ma cuisine spécifique ?",
        "a": "Vous commencez avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes où vous lui racontez quel type de cuisine vous dirigez, où vous travaillez et à quelle échelle. À partir de ce moment, tous les agents répondent adaptés à votre contexte réel."
      },
      {
        "q": "Pouvez-vous tout télécharger en Excel et PDF ?",
        "a": "Oui. Toute la documentation est exportable et modifiable : coûts, fiches techniques, APPCC, mise en place et formation de l'équipe."
      },
      {
        "q": "Est-ce adapté aux cuisines avec des techniques avancées (fermentations, sphérifications, cuissons longues) ?",
        "a": "Oui. Fermentus Avec AI+ couvre la fermentation de pointe (koji, kombucha, shoyu, miso, garum, lactofermentations) et Cuisine Créative comprend des techniques comme le sous-vide, les sphérifications, les gélifications et les cuissons longues contrôlées."
      }
    ],
    "ctaTitle": "Plus de cuisine, moins de paperasse. Récupérez des heures pour ce qui compte.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Chef de Cuisine et Chef Exécutif : Coûts, Fiches et APPCC | AI Chef Pro",
      "description": "Suite IA pour chefs de cuisine professionnels : agents spécialisés, coûts, fiches techniques, mise en place et APPCC avec un véritable appui gastronomique. Commencez aujourd'hui.",
      "keywords": "IA chef cuisine, chef de cuisine logiciel, IA chef de cuisine, coûts cuisine, fiches techniques IA, APPCC cuisine, mise en place IA, agent IA gastronomique, chef cuisine Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/chef-cocina.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Cuisine dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes où vous lui racontez quel type de cuisine vous dirigez, dans quelle ville, quel type de carte vous gérez et à quelle échelle vous opérez. À partir de ce moment, chaque agent — des fiches techniques à la créativité — répond adapté à votre contexte : produit local, réglementation de votre pays, taille de votre brigade et budget réel. Ce n'est pas un formulaire : c'est une conversation courte qui rend la suite véritablement utile pour votre quotidien en cuisine.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser en tant que Chef de Cuisine",
    "apps": [
      {
        "name": "Chef Exécutif Pro",
        "category": "Gastro Profile Pro",
        "description": "Standardisation des recettes, des fiches techniques et des manuels de cuisine."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de plats professionnels avec recette + coût CSV prêt pour le Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Combinaisons d'ingrédients et accords avec une base scientifique."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "R&D gastronomique : fermentation créative de koji, kombucha, shoyu, miso et garum."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Desserts de restaurant créatifs avec une technique de pâtisserie professionnelle."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises sur les pertes et rendements par ingrédient."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Calculatrice de portions qui adapte les recettes à n'importe quel nombre de convives."
      },
      {
        "name": "Conversor Ing",
        "category": "Outils et Utilitaires",
        "description": "Convertisseur de poids et mesures pour la cuisine professionnelle."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette et par plat."
      },
      {
        "name": "Repas du Personnel",
        "category": "Gastro Profile Pro",
        "description": "Générateur de menus pour le personnel qui économise des coûts et motive l'équipe."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Assistant avec le catalogue professionnel de Sosa pour les techniques avancées."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue tSpoonLab pour les applications techniques."
      },
      {
        "name": "Gastro Lexicum",
        "category": "Gastro Connaissance",
        "description": "Tuteur avec des définitions de techniques, de processus et de science gastronomique."
      }
    ],
    "metrics": [
      {
        "value": "−5 h",
        "label": "hebdomadaires en paperasse"
      },
      {
        "value": "×7",
        "label": "vitesse de finalisation de nouvelle carte"
      },
      {
        "value": "+3 pp",
        "label": "marge après coût réel"
      },
      {
        "value": "13+",
        "label": "agents IA pour votre cuisine"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Recettes dans un carnet et des feuilles volantes, différentes versions selon le cuisinier",
        "Coût manuel avec calculatrice à chaque changement de prix",
        "APPCC sur papier imprimé qui s'accumule et que personne ne vérifie",
        "Renouveler la carte prend entre 15 et 30 jours entre brainstorming, coûts et fiches",
        "Formation de l'équipe improvisée à chaque arrivée d'un nouveau"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Recettes centralisées avec coût, allergènes, technique et storytelling",
        "Coût automatique qui recalcule instantanément à tout changement de prix",
        "APPCC depuis le mobile avec enregistrements et alertes, prêt pour l'inspection",
        "Renouveler la carte en 1-3 jours avec Cuisine Créative + Kit de Escandallos Pro",
        "Manuels de formation réplicables avec le script du Pro Prompts eBook"
      ]
    },
    "galleryTitle": "Le Quotidien d'un Chef de Cuisine, en Images",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : brigade, mise en place, fiches techniques, passe, stock et formation de l'équipe.",
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
    "h1": "IA pour Sous-Chef",
    "heroSubtitle": "Organisez les postes, gérez la mise en place, supervisez l'équipe et libérez des heures administratives avec une suite d'agents IA conçus pour le sous-chef en cuisine professionnelle.",
    "heroTagline": "Le bras droit du chef de cuisine, avec système",
    "badge": "Pour sous-chefs",
    "painsTitle": "Ce qu'un Sous-Chef ne peut pas manquer de résoudre",
    "pains": [
      "Coordonner les postes et la mise en place avec précision quand le rythme ne laisse aucun répit",
      "Remplacer le chef de cuisine quand il n'est pas là sans que la qualité ni l'opérationnel ne baissent",
      "Former et superviser l'équipe de cuisine avec des critères cohérents",
      "Maintenir la traçabilité HACCP à jour sans que la paperasse ne s'accumule",
      "Avoir un accès rapide aux fiches techniques à jour pendant le service",
      "Valider les calculs de coûts quand de nouveaux ingrédients arrivent ou qu'un fournisseur change"
    ],
    "featuresTitle": "Comment AI Chef Pro aide un Sous-Chef",
    "features": [
      {
        "icon": "CheckSquare",
        "title": "Mise en place et tâches par poste",
        "description": "Kit de Tareas avec des listes structurées par service et par poste, prêtes à imprimer chaque matin."
      },
      {
        "icon": "BookOpen",
        "title": "Fiches techniques toujours à jour",
        "description": "Accès rapide depuis le mobile à la recette, la procédure, le dressage et les allergènes de chaque plat pendant le service."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP depuis le mobile",
        "description": "Pack APPCC avec registres, alertes de température et feuilles prêtes à imprimer en A4. L'équipe enregistre depuis le mobile sans paperasse."
      },
      {
        "icon": "Calculator",
        "title": "Calculs de coûts rapides",
        "description": "Cuisine Créative fournit recette + calcul de coût CSV ; le Kit de Escandallos Pro le gère avec vos prix réels et vous validez la marge instantanément."
      },
      {
        "icon": "GraduationCap",
        "title": "Formation de l'équipe",
        "description": "Pro Prompts eBook + Chef Exécutif Pro génèrent des manuels et un onboarding prêts pour les nouveaux cuisiniers."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Chat IA gastronomique pour résoudre les doutes techniques, proposer des plats hors menu et valider des techniques en temps réel."
      },
      {
        "icon": "Users",
        "title": "Repas du Personnel",
        "description": "Générateur de menus pour le staff qui exploite le produit que vous avez déjà en chambre froide et motive l'équipe."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Allergènes et Rendement GenCal",
        "description": "Détection automatique des allergènes et données précises de pertes pour le passe et le poste."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Sous-Chef avec AI Chef Pro",
    "workflow": [
      "07:30 · Ouverture — vous ouvrez le Kit de Tareas et révisez la mise en place du jour. Vous signez l'inventaire critique avec le Kit Inventario.",
      "08:30 · Briefing rapide avec la brigade — vous passez en revue les services du jour avec les fiches techniques centralisées en main.",
      "12:00 · Service de midi — vous supervisez les postes, l'équipe enregistre les pertes et les températures depuis le mobile avec le Pack APPCC.",
      "15:30 · Cuisine Créative — le chef de cuisine vous demande un plat hors menu pour samedi. Vous générez plat + calcul de coût CSV en 20 minutes.",
      "16:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels, vous validez que le food cost correspond à 28 % et vous exportez la fiche technique.",
      "17:30 · Repas du Personnel — vous préparez le menu du staff de la semaine prochaine en respectant le coût cible et le stock de la chambre froide.",
      "20:00 · Service du soir — vous coordonnez les passes avec la brigade, vous gérez les doutes avec Cuisine Créative quand le cuisinier junior a besoin de confirmer une technique.",
      "23:30 · Fermeture — vous signez HACCP, vous laissez la mise en place du lendemain prête et le rapport envoyé au chef de cuisine."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Sous-Chefs",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Être sous-chef, c'est être à mille endroits à la fois. Les listes de mise en place du Kit de Tareas et les registres HACCP depuis le mobile m'ont organisé le chaos. Quand le chef de cuisine n'est pas là, tout continue de fonctionner parce que les procédures sont documentées.",
    "testimonialAuthor": "Nicolás Vega",
    "testimonialRole": "Sous-Chef, restaurant de 100 couverts",
    "faqTitle": "Questions Fréquentes des Sous-Chefs",
    "faqs": [
      {
        "q": "Les modèles s'adaptent-ils au style de ma cuisine ?",
        "a": "Oui. Il existe des Kits de Tareas spécifiques par concept (casual, gastronomique, dark kitchen, hôtel, pizzeria, burger, pâtisserie, bar, traiteur, glacier, chocolaterie, restaurant créatif, chef privé) et tous peuvent être personnalisés au style de votre cuisine."
      },
      {
        "q": "Fonctionne-t-il depuis le mobile pour les enregistrements de l'équipe ?",
        "a": "Oui. Les registres HACCP, pertes, températures et check des tâches se font depuis le mobile du staff sans rien installer. En fin de journée, on exporte en PDF pour le chef de cuisine ou le propriétaire."
      },
      {
        "q": "Est-ce compliqué à utiliser pour l'équipe ?",
        "a": "Non. L'équipe ne fait que remplir des cases ou cocher. La courbe réelle est de 1 jour. Il y a une vidéo d'onboarding de 5 minutes."
      },
      {
        "q": "Est-ce utile si ce n'est pas moi qui décide des outils en cuisine ?",
        "a": "Vous pouvez commencer avec le plan Membre (10 € par mois, 10 000 crédits) pour vos propres listes et propositions. Après 1 à 2 semaines d'utilisation, proposez au chef de cuisine avec des données concrètes : temps gagné, calculs de coûts validés, mise organisée."
      },
      {
        "q": "Comment m'aide-t-il pendant les pics de service ?",
        "a": "Les fiches techniques centralisées vous donnent un accès rapide depuis le mobile pendant le passe. Si un doute technique surgit, Cuisine Créative répond en quelques secondes. Coach Mental aide également à gérer le stress dans les cuisines à haute pression."
      },
      {
        "q": "Y a-t-il quelque chose de spécifique pour évoluer vers chef de cuisine ?",
        "a": "Oui. Pro Prompts eBook (300+ prompts professionnels), Chef Exécutif Pro (standardisation multi-site) et Gastro Lexicum (référence technique) sont des outils clés pour progresser vers le niveau suivant."
      }
    ],
    "ctaTitle": "Organisez votre cuisine sans paperasse.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Sous-Chef : Mise en Place, Fiches Techniques et HACCP | AI Chef Pro",
      "description": "Suite d'IA pour sous-chef en cuisine professionnelle : mise en place, fiches techniques centralisées, calculs de coûts, HACCP depuis le mobile et formation de l'équipe. Commencez dès aujourd'hui.",
      "keywords": "IA sous-chef, logiciel sous-chef, mise en place cuisine IA, HACCP sous-chef, fiches techniques cuisine, formation brigade cuisine, sous-chef Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/sous-chef.jpg"
    },
    "personalizationTitle": "Personnalisé à votre cuisine dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes dans lequel vous lui dites quel type de cuisine vous avez, dans quelle ville, quelle carte vous gérez et à quelle échelle. À partir de ce moment, chaque agent — de la mise en place aux fiches techniques — répond adapté à votre contexte : type de service, taille de la brigade et opération réelle. Ce n'est pas un formulaire : c'est une conversation courte qui rend la suite véritablement utile pour le rythme de départ.",
    "appsTitle": "Les Agents IA que vous allez utiliser en tant que Sous-Chef",
    "apps": [
      {
        "name": "Chef Exécutif Pro",
        "category": "Gastro Profile Pro",
        "description": "Standardisation des recettes, fiches techniques et manuels de cuisine centralisés."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de plats professionnels avec recette + calcul de coût CSV prêt pour le Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Combinaisons d'ingrédients et accords à base scientifique."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Desserts de restaurant créatifs avec une technique de pâtisserie professionnelle."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Calculatrice de portions qui adapte les recettes à n'importe quel nombre de convives."
      },
      {
        "name": "Conversor Ing",
        "category": "Outils et Utilitaires",
        "description": "Convertisseur de poids et mesures pour la cuisine professionnelle."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises de pertes et rendements par ingrédient."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette et par plat."
      },
      {
        "name": "Repas du Personnel",
        "category": "Gastro Profile Pro",
        "description": "Générateur de menus pour le staff avec le produit que vous avez déjà en chambre froide."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching psychologique pour gérer le stress et les conversations difficiles en cuisine."
      },
      {
        "name": "Gastro Lexicum",
        "category": "Gastro Connaissance",
        "description": "Tuteur avec des définitions de techniques, processus et science gastronomique."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "vitesse de mise en place"
      },
      {
        "value": "−4 h",
        "label": "hebdomadaires en paperasse"
      },
      {
        "value": "même",
        "label": "standard quand le chef n'est pas là"
      },
      {
        "value": "11+",
        "label": "agents pour votre rôle"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Mise en place dictée chaque matin à l'équipe, différente chaque jour",
        "HACCP sur papier imprimé qui s'accumule en fin de semaine",
        "Fiches techniques dans le carnet du chef de cuisine, inaccessibles pendant le service",
        "Quand le chef de cuisine n'est pas là, la qualité et l'opérationnel baissent",
        "Formation des nouveaux cuisiniers improvisée et inégale"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Mise en place imprimable chaque jour avec le Kit de Tareas structuré par poste",
        "HACCP depuis le mobile avec registres, alertes et exportation en PDF à la fermeture",
        "Fiches techniques centralisées accessibles depuis le mobile pendant le service",
        "Procédures documentées — le standard se maintient même si l'équipe change",
        "Formation reproductible avec le script du Pro Prompts eBook et les manuels du Chef Exécutif Pro"
      ]
    },
    "galleryTitle": "Le Quotidien d'un Sous-Chef, en Images",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : mise en place, préparation, supervision de l'équipe, service en ligne et traçabilité.",
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
    "h1": "IA pour Chef Traiteur",
    "heroSubtitle": "Concevez des menus d'événement, chiffrez par service et planifiez la production à grande échelle avec une suite d'agents IA pensés pour la restauration événementielle professionnelle et les chefs traiteurs.",
    "heroTagline": "Production à grande échelle sans perdre marge ni qualité",
    "badge": "Pour chefs traiteurs et événementiel",
    "painsTitle": "Ce Qu'un Chef Traiteur Ne Peut Pas Ignorer",
    "pains": [
      "Chiffrer des menus avec une forte variabilité d'invités (50, 200, 500) quand les prix des ingrédients changent chaque semaine",
      "Planifier production, mise en place et achats à grande échelle sans déséquilibres",
      "Coordonner logistique, transport et montage sur site client en respectant délais et températures",
      "Maintenir l'APPCC et la traçabilité hors du local fixe, sur sites externes et véhicules réfrigérés",
      "Concevoir des menus créatifs par type d'événement (mariage, corporate, cocktail, gala) sans réinventer à chaque fois",
      "Communiquer avec l'équipe de production, transport et service avec une documentation claire"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Chef Traiteur",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Traiteur IA+",
        "description": "Agent spécialisé en traiteur et événementiel gastronomique : mariages, corporate, cocktails et galas avec connaissance professionnelle."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative + Food Pairing AI",
        "description": "Brainstorming pour menus d'événement. Cuisine Créative livre recette + fiche de coûts CSV prête pour le Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Fiches de coûts par événement",
        "description": "Kit de Escandallos Pro : chargez le CSV avec vos prix réels, ajustez le nombre d'invités et obtenez coût, food cost % et marge instantanément."
      },
      {
        "icon": "Layers",
        "title": "Calcula Pax",
        "description": "Calculateur de portions qui adapte les recettes à 50, 200, 500 ou 1000 convives en quelques secondes."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Catering",
        "description": "Modèles spécifiques pour production, transport, montage, service et démontage sur site client."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC hors site",
        "description": "Pack APPCC avec modèles adaptés au produit qui voyage : traçabilité, température en transport et registres sur site externe."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Photographie culinaire par IA pour présentations clients, propositions d'événement et communiqués de presse."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Allergènes",
        "description": "Identification automatique des allergènes, critique pour les événements avec de nombreux invités aux profils alimentaires variés."
      },
      {
        "icon": "BookOpen",
        "title": "Agent Sosa Ingredients",
        "description": "Assistant pour la sélection d'ingrédients techniques du catalogue Sosa, particulièrement utile pour cocktails et desserts."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Chef Traiteur avec AI Chef Pro",
    "workflow": [
      "08:30 · Traiteur IA+ — l'agent vous aide à finaliser la proposition de menu pour un mariage de 180 invités selon le brief du client.",
      "09:30 · Cuisine Créative — vous développez les 12 plats du menu avec recette détaillée et fiche de coûts CSV avec prix de référence.",
      "10:30 · Calcula Pax + Kit de Escandallos Pro — vous passez à 180 convives, chargez le CSV avec vos prix réels et validez la marge cible.",
      "12:00 · Validation avec le client — vous exportez la proposition avec fiches techniques et photographie culinaire de GastroIMG Gen+.",
      "14:00 · Kit de Tareas Catering — vous planifiez production, transport, montage, service et démontage de l'événement de samedi.",
      "16:00 · APPCC hors site — vous préparez les registres de température en transport et la traçabilité sur site externe avec le Pack APPCC.",
      "18:00 · ID Allergènes — vous générez la fiche d'allergènes par plat prête pour la salle et pour les invités avec restrictions.",
      "19:30 · Brief à l'équipe — vous montez le brief de service avec l'équipe de cuisine et de salle de l'événement, tout depuis une source unique."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Chefs Traiteurs",
    "productIds": [
      "kit-tareas-catering",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Les fiches de coûts par événement me font gagner des heures. Je boucle un menu pour 200 invités avec marge validée en 30 minutes. Avant, c'était une demi-journée avec calculatrice et serviettes. Et l'APPCC adapté aux événements hors site nous a enlevé une énorme épine du pied avec les clients corporate.",
    "testimonialAuthor": "Andrea Costa",
    "testimonialRole": "Chef traiteur, spécialiste des événements corporate et mariages",
    "faqTitle": "Questions Fréquentes des Chefs Traiteurs",
    "faqs": [
      {
        "q": "Est-ce adapté à toute taille de traiteur ?",
        "a": "Oui. Des traiteurs boutique de 50 invités par mois aux entreprises de plus de 1000 services mensuels et événements de 2000 convives."
      },
      {
        "q": "Permet-il de gérer la variabilité des invités ?",
        "a": "Oui. Calcula Pax adapte les recettes à tout nombre de convives et le Kit de Escandallos Pro recalcule coût, food cost et marge automatiquement."
      },
      {
        "q": "Couvre-t-il l'APPCC hors du local fixe ?",
        "a": "Oui. Le Pack APPCC a des modèles spécifiques pour le produit qui voyage en sac, moto, fourgon réfrigéré ou cuisine centrale, incluant la traçabilité sur site externe."
      },
      {
        "q": "Y a-t-il des modèles spécifiques traiteur ?",
        "a": "Oui. Le Kit de Tareas Catering inclut des listes détaillées de production, transport, montage sur site, service et démontage, ainsi que des protocoles de coordination avec la cuisine centrale."
      },
      {
        "q": "Comment s'adapte-t-il à mon type de traiteur ?",
        "a": "Vous commencez avec l'agent « Qui suis-je ? », un onboarding de 2 minutes où vous décrivez le type d'événements que vous faites (mariages, corporate, cocktails, galas), la taille moyenne, la ville et l'opérationnel. Tout s'adapte à votre contexte."
      },
      {
        "q": "Sert-il à concevoir des menus innovants ?",
        "a": "Oui. Traiteur IA+ + Cuisine Créative + Food Pairing AI + Fermentus Avec AI+ travaillent ensemble pour concevoir des menus créatifs à base professionnelle, pas des recettes copiées d'Internet."
      }
    ],
    "ctaTitle": "Concevez, chiffrez et produisez des événements sans papiers volants.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Chef Traiteur : Menus, Fiches de Coûts et APPCC d'Événement | AI Chef Pro",
      "description": "Suite IA pour chef traiteur : Traiteur IA+, Cuisine Créative, Calcula Pax, fiches de coûts par événement, APPCC hors site et planification de production à grande échelle. Commencez dès aujourd'hui.",
      "keywords": "IA chef traiteur, logiciel chef traiteur, fiches de coûts traiteur IA, logiciel traiteur événementiel, APPCC traiteur, menu mariage IA, gestion événement gastronomique IA, chef traiteur France",
      "ogImage": "https://aichef.pro/og/use-cases/chef-catering.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Type de Traiteur dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous décrivez le type d'événements que vous concevez (mariages, corporate, cocktails, galas), la taille moyenne, la ville et votre façon de travailler. À partir de ce moment, chaque agent — du Traiteur IA+ aux fiches de coûts — répond adapté à votre contexte : types de service, échelle de votre cuisine centrale et opérationnel réel. Ce n'est pas un formulaire : c'est une conversation courte qui rend la suite véritablement utile pour votre quotidien de chef traiteur.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser comme Chef Traiteur",
    "apps": [
      {
        "name": "Traiteur IA+",
        "category": "Concepts d'Entreprise",
        "description": "Agent principal : mariages, corporate, cocktails et galas avec connaissance professionnelle."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de plats professionnels avec recette + fiche de coûts CSV prête pour le Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Combinaisons d'ingrédients et accords à base scientifique."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Desserts d'événement avec technique professionnelle, idéaux pour banquets et galas."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "Pour canapés avant-gardistes avec ferments, garums et techniques innovantes."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Calculateur de portions qui adapte les recettes à 50, 200 ou 500 convives."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par plat, critique pour les grands événements."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises de pertes et rendements pour la production à grande échelle."
      },
      {
        "name": "Conversor Ing",
        "category": "Outils et Utilitaires",
        "description": "Convertisseur de poids et mesures professionnel pour la production industrielle."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Assistant pour ingrédients techniques du catalogue Sosa."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie culinaire par IA pour propositions clients et communiqués de presse."
      }
    ],
    "metrics": [
      {
        "value": "×10",
        "label": "vitesse de finalisation du menu événement"
      },
      {
        "value": "+5 pp",
        "label": "marge après chiffrage réel"
      },
      {
        "value": "−50 %",
        "label": "temps en planification logistique"
      },
      {
        "value": "11+",
        "label": "agents pour votre traiteur"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Finaliser un menu d'événement avec le client : une demi-journée avec calculatrice et serviettes",
        "APPCC hors site improvisé, sans traçabilité réelle en transport",
        "Production pour 200 invités sans mise à l'échelle précise, pertes élevées",
        "Propositions clients avec modèles Word et photos de stock",
        "Brief à l'équipe sur des feuilles volantes qui se perdent"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Finaliser un menu avec marge validée en 30 minutes avec Traiteur IA+ et Kit de Escandallos Pro",
        "APPCC adapté au produit qui voyage avec registres depuis mobile et traçabilité par événement",
        "Production mise à l'échelle avec Calcula Pax, pertes contrôlées avec Rendement GenCal",
        "Propositions commerciales avec photos GastroIMG Gen+ et fiches techniques professionnelles",
        "Brief centralisé et réplicable pour production, transport, montage et service"
      ]
    },
    "galleryTitle": "Le Quotidien d'un Chef Traiteur, en Images",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : conception de menu, production à grande échelle, logistique, montage sur site, service et traçabilité.",
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
    "h1": "IA pour Propriétaires d'Entreprise de Traiteur",
    "heroSubtitle": "Contrôlez la rentabilité par événement, passez la production à l'échelle, gérez les équipes temporaires et faites croître votre entreprise de traiteur avec une suite d'agents d'IA spécialisés en restauration.",
    "heroTagline": "Croissance maîtrisée, marge réelle, événements sans chaos",
    "badge": "Pour les propriétaires d'entreprise de traiteur",
    "painsTitle": "Ce Qu'un Propriétaire de Traiteur Ne Peut Pas Ignorer",
    "pains": [
      "Gérer des marges très variables entre les événements : un mariage, un cocktail d'entreprise et une pause-café ont des rentabilités très différentes",
      "Faire passer la production à l'échelle sans perdre en qualité ni en contrôle des coûts lors des pics de mariages ou de la saison des événements",
      "Coordonner les équipes temporaires et le personnel permanent avec des plannings, des contrats par événement et des coûts salariaux clairs",
      "Reporting financier aux investisseurs ou associés avec des données consolidées, pas des Excel improvisés",
      "Attirer des clients d'entreprise avec des propositions professionnelles qui concluent des contrats à plus forte valeur",
      "Décider quels événements accepter et lesquels refuser avec des données de marge réelle, pas par intuition"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Propriétaire de Traiteur",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Traiteur IA+",
        "description": "Agent spécialisé dans les événements gastronomiques : mariages, entreprises, cocktails et galas avec une connaissance professionnelle."
      },
      {
        "icon": "FileText",
        "title": "Kit Plan Financiero",
        "description": "Cash flow, P&L mensuel, tableau de bord de ratios et rentabilité par événement et par client. Modèles professionnels adaptés à la restauration événementielle."
      },
      {
        "icon": "Calculator",
        "title": "Fiches techniques par événement",
        "description": "Cuisine Créative fournit la recette + la fiche technique CSV ; Kit de Escandallos Pro la gère avec vos prix réels et votre marge cible."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Plannings pour le personnel permanent et temporaire, contrats par événement, suivi des heures et coûts salariaux par service."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP et certifications",
        "description": "Pack APPCC avec des modèles adaptés à la restauration événementielle : traçabilité, transport et enregistrements prêts pour l'inspection et les clients d'entreprise."
      },
      {
        "icon": "Sparkles",
        "title": "BlogPost SEO Gen+ + MenuDish Local SEO",
        "description": "Suite SEO pour attirer des clients d'entreprise avec du trafic organique et un meilleur référencement."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Photographie culinaire par IA pour les propositions clients, présentations et galerie web."
      },
      {
        "icon": "BarChart3",
        "title": "Tableau de bord des opérations",
        "description": "KPI financiers consolidés, taux d'occupation, rentabilité par ligne de métier (mariages, entreprises, cocktails)."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Recherche approfondie sur le marché, les concurrents et les tendances pour des décisions stratégiques de croissance."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Propriétaire de Traiteur avec AI Chef Pro",
    "workflow": [
      "08:30 · Kit Plan Financiero — vous ouvrez le tableau de bord et constatez qu'un événement du week-end a une marge de 18 %, en dessous de l'objectif (28 %).",
      "09:30 · Kit de Escandallos Pro — vous analysez la fiche technique de l'événement et ajustez le menu ou le prix avant de signer le contrat.",
      "11:00 · Traiteur IA+ — vous finalisez une proposition pour une entreprise cliente avec une présentation générée par IA et validée avec l'agent.",
      "12:30 · GastroIMG Gen+ — vous générez les photographies des plats du menu proposé à inclure dans la présentation.",
      "14:00 · Réunion avec un client d'entreprise — vous présentez une proposition finalisée en 1 heure au lieu des 3 jours habituels.",
      "16:30 · Kit Plan Financiero — vous validez les prévisions du trimestre, exportez en PDF pour la réunion avec les associés.",
      "18:00 · Kit Gestión de Personal — vous révisez le planning du week-end avec le personnel permanent et temporaire, signez les contrats par événement.",
      "20:00 · BlogPost SEO Gen+ — vous publiez un article sur le dernier grand événement d'entreprise pour attirer de nouveaux clients de manière organique."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Entreprises de Traiteur",
    "productIds": [
      "kit-plan-financiero",
      "kit-escandallos",
      "pack-appcc",
      "kit-tareas-catering",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "AI Chef Pro m'a donné un véritable contrôle financier. Je sais exactement sur quels événements je gagne de l'argent et sur lesquels je n'en gagne pas, et cela m'a permis de dire non à des clients qui n'étaient pas rentables. Au premier trimestre, nous avons gagné 4 points de marge sans toucher aux prix. En ajustant simplement les menus et en refusant les mauvais événements.",
    "testimonialAuthor": "Roberto Iglesias",
    "testimonialRole": "Propriétaire, entreprise de traiteur d'entreprise (2 M€ de chiffre d'affaires annuel)",
    "faqTitle": "Questions Fréquentes des Propriétaires de Traiteur",
    "faqs": [
      {
        "q": "Convient-il pour un traiteur de niche de moins de 5 employés ?",
        "a": "Oui. C'est idéal pour une petite structure car cela consolide les opérations, les finances, le marketing et les propositions clients dans un seul outil. Un client type commence avec 1 plan personnel et évolue vers l'entreprise."
      },
      {
        "q": "Et pour les grandes entreprises de 50+ employés temporaires ?",
        "a": "Aussi. Le Kit Gestión de Personal s'adapte aux grandes équipes avec des plannings, des contrats par événement et une consolidation des coûts salariaux. Certains clients gèrent 100+ services par mois."
      },
      {
        "q": "S'intègre-t-il à mon logiciel comptable ou ERP ?",
        "a": "Il exporte en Excel, PDF et CSV compatibles avec la plupart des ERP et cabinets comptables. Votre équipe financière reçoit une documentation prête à intégrer."
      },
      {
        "q": "Existe-t-il un plan entreprise pour les grands traiteurs ?",
        "a": "Oui. À partir d'un certain chiffre d'affaires, des plans entreprise sont disponibles avec un onboarding personnalisé, des tableaux de bord consolidés, la formation de l'équipe centrale et un support prioritaire."
      },
      {
        "q": "Comment cela m'aide-t-il à attirer des clients d'entreprise ?",
        "a": "BlogPost SEO Gen+ et MenuDish Local SEO attirent du trafic organique vers votre site web ; Traiteur IA+ aide à rédiger des propositions professionnelles ; GastroIMG Gen+ génère des photographies pour les présentations ; Keyword Discovery AI+ trouve les recherches réelles des entreprises dans votre région."
      },
      {
        "q": "Est-il sûr de confier le plan financier à une IA ?",
        "a": "Oui. Le Kit Plan Financiero est un modèle Excel professionnel avec des formules préchargées, pas une IA. Vous saisissez les données réelles et l'outil calcule. Les agents IA ne sont utilisés que pour soutenir les décisions, la rédaction de propositions et l'analyse, pas pour le calcul financier critique."
      }
    ],
    "ctaTitle": "Faites croître votre entreprise de traiteur avec une marge réelle, pas de l'intuition.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Propriétaires d'Entreprise de Traiteur : Rentabilité et Plan Financier | AI Chef Pro",
      "description": "Suite d'IA pour les entreprises de traiteur : rentabilité par événement, production à l'échelle, équipes temporaires, plan financier et acquisition de clients d'entreprise. Commencez dès aujourd'hui.",
      "keywords": "IA entreprise traiteur, propriétaire traiteur IA, logiciel traiteur, gestion entreprise traiteur, plan financier traiteur, rentabilité traiteur, acquisition clients d'entreprise traiteur, faire évoluer entreprise traiteur, propriétaire traiteur France",
      "ogImage": "https://aichef.pro/og/use-cases/propietario-catering.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Entreprise dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes au cours duquel vous décrivez le type de traiteur que vous exploitez (mariages, entreprises, cocktails, galas), la taille moyenne des événements, la ville et le volume annuel. À partir de ce moment, chaque agent — du Traiteur IA+ au Plan Financier — répond en s'adaptant à votre contexte : types de service, échelle réelle et marché cible. Ce n'est pas un formulaire : c'est une courte conversation qui rend la suite véritablement utile pour votre entreprise.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser en Tant que Propriétaire de Traiteur",
    "apps": [
      {
        "name": "Traiteur IA+",
        "category": "Concepts d'Entreprise",
        "description": "Agent principal : mariages, entreprises, cocktails et galas avec une connaissance professionnelle."
      },
      {
        "name": "Manager de Restaurant Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistant opérationnel et financier pour vous soutenir dans les décisions et le reporting aux associés."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de menus d'événement avec recette + fiche technique CSV prête pour le Kit de Escandallos Pro."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Desserts d'événement et de banquet avec une technique professionnelle."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Calculateur de portions qui adapte les recettes à 50, 200 ou 500 convives."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette, essentielle pour les grands événements."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles de blog pour attirer du trafic organique vers votre site de traiteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Descriptions SEO pour améliorer le référencement web de votre traiteur."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Recherche de mots-clés pour attirer les entreprises qui cherchent un traiteur dans votre région."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie culinaire pour les propositions clients et les présentations commerciales."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche sur le marché, les concurrents et les tendances du secteur de l'événementiel."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching pour la gestion du stress, les décisions difficiles et les conversations avec les associés ou l'équipe."
      }
    ],
    "metrics": [
      {
        "value": "+4 pts",
        "label": "de marge au premier trimestre"
      },
      {
        "value": "×3",
        "label": "de rapidité en plus pour finaliser les propositions"
      },
      {
        "value": "−40 %",
        "label": "de temps en reporting financier"
      },
      {
        "value": "12+",
        "label": "agents pour votre entreprise"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Ne pas savoir lequel des 50 événements du mois est réellement rentable",
        "Finaliser des propositions pour des clients d'entreprise en 3 jours avec des modèles Word",
        "Plannings du personnel temporaire sur Excel manuel sans contrôle des coûts",
        "HACCP incohérent entre les événements, un problème avec les clients d'entreprise exigeants",
        "Marketing improvisé ou externalisé à prix élevé sans capter de leads organiques"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Rentabilité par événement et par client claire, des décisions d'accepter/refuser basées sur les données",
        "Finaliser des propositions en 1 heure avec Traiteur IA+ + GastroIMG Gen+ + présentation professionnelle",
        "Plannings avec Kit Gestión de Personal : suivi des heures et coûts consolidés",
        "HACCP unifié et professionnel, prêt pour toute inspection ou client d'entreprise",
        "Suite SEO captant des leads organiques sans dépenses en agences"
      ]
    },
    "galleryTitle": "Le Quotidien d'un Propriétaire de Traiteur, en Images",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : tarification, propositions clients, événements à grande échelle, équipes, entrepôt logistique et reporting financier.",
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
    "h1": "IA pour Barman et Cocktailier",
    "heroSubtitle": "Concevez des cartes de cocktails avec un calcul de coût professionnel, un coût réel par verre et la technique, et créez des cocktails d'auteur avec storytelling et accords, grâce à une suite d'agents d'IA gastronomique spécialisés en cocktail.",
    "heroTagline": "Mixologie avec marge réelle et technique d'auteur",
    "badge": "Pour barmans, cocktailiers et mixologues",
    "painsTitle": "Ce Qu'un Barman Ne Peut Pas Laisser de Côté",
    "pains": [
      "Calculer le coût de cocktails complexes avec de nombreux ingrédients (spiritueux, cordiaux, infusions, garnitures) sans perdre des heures avec la calculatrice",
      "Renouveler la carte chaque saison avec de nouveaux cocktails tout en maintenant la marge et un food cost cohérent avec le reste du bar",
      "Standardiser les recettes au bar pour que tout serveur réplique le verre avec le même équilibre à chaque fois",
      "Contrôler les pertes au bar : casse de la verrerie, sur-versement, évaporation, garnitures gaspillées",
      "Storytelling : chaque cocktail a besoin d'un nom, d'une histoire et d'un accord qui justifie le ticket élevé",
      "Se différencier dans une zone concurrentielle avec une cocktailerie d'auteur, un branding visuel et des réseaux sociaux actifs"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Barman",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Agent spécialisé en cocktail professionnel, caves à vins, bars à cocktails et spiritueux avec une technique avancée."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Combinaisons inattendues pour cocktails d'auteur avec une base scientifique et des accords avec la cuisine."
      },
      {
        "icon": "Calculator",
        "title": "Calculs de coût par verre",
        "description": "Bar & Lounge AI+ fournit la recette + le calcul de coût CSV avec la technique ; Kit de Escandallos Pro le gère avec le coût réel par verre, le food cost % et le prix suggéré."
      },
      {
        "icon": "BookOpen",
        "title": "Fiches techniques de cocktail",
        "description": "Recette, technique, garniture, verrerie, accord et storytelling dans un document unique prêt pour l'équipe."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Modèles : mise en place du bar, préparation des cordiaux et infusions, procédures par service, clôture de caisse, contrôle des stocks."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC bar",
        "description": "Traçabilité de la glace, garnitures fraîches, infusions maison et températures critiques."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification de la carte saisonnière : cocktails d'été, cocktails chauds d'hiver, cartes thématiques pour la Saint-Valentin, Noël et les événements."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie de cocktails avec IA de référence + contenu pour Instagram avec calendrier éditorial professionnel."
      },
      {
        "icon": "BarChart3",
        "title": "KPIs bar",
        "description": "Ticket moyen, rotation des verres, marge par catégorie (classiques, signatures, vins, bières)."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Barman avec AI Chef Pro",
    "workflow": [
      "11:00 · Ouverture — checklist Kit de Tareas Bar : mise en place des garnitures fraîches, préparation des cordiaux maison, chargement de la glace, vérification des stocks.",
      "12:00 · Bar & Lounge AI+ — vous développez un nouveau signature pour la carte d'été (gin avec shrub de fraises et basilic). Cuisine Créative fournit la recette + le calcul de coût CSV.",
      "13:00 · Food Pairing AI — vous validez l'accord avec un plat de la cuisine et vous affinez la technique.",
      "14:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels de spiritueux premium et d'ingrédients, vous validez la marge par verre et le food cost %.",
      "17:00 · Service — l'équipe réplique le verre avec la fiche technique (recette, technique, garniture, verrerie, storytelling).",
      "19:00 · Gastro Calendar — vous mettez à jour le calendrier éditorial d'Instagram avec le lancement du nouveau signature.",
      "20:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence du verre et les posts pour le lancement.",
      "02:00 · Fermeture — nettoyage en profondeur, APPCC signé, contrôle des pertes et stock final."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour la Mixologie",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "AI Chef Pro a changé ma façon de finaliser les cartes de cocktails. Avant, c'était une semaine de serviettes et de calculatrice ; maintenant, c'est une journée avec un calcul de coût professionnel, une fiche technique avec storytelling et accords validés, prête à être répliquée par mon équipe. Nous avons augmenté la marge de 5 points et triplé l'engagement sur Instagram avec GastroIMG.",
    "testimonialAuthor": "Hugo Vázquez",
    "testimonialRole": "Barman, bar à cocktails d'auteur",
    "faqTitle": "Questions Fréquentes des Barmans",
    "faqs": [
      {
        "q": "Est-ce adapté à la cocktailerie classique, d'auteur ou décontractée ?",
        "a": "Pour les trois. Bar & Lounge AI+ comprend aussi bien les classiques de l'IBA que l'avant-garde : shrubs, infusions, fermentations, mousses, fumés contrôlés, technique avancée de bar."
      },
      {
        "q": "Couvre-t-il les vins et les bières en plus de la cocktailerie ?",
        "a": "Oui. L'agent couvre tout le spectre du bar : cocktails, vins, bières, spiritueux, sans alcool et accords."
      },
      {
        "q": "Permet-il de créer des cartes de cocktails avec storytelling et technique ?",
        "a": "Oui. Les fiches incluent recette, technique, garniture, verrerie, histoire et accord, prêtes pour la salle. Idéal pour augmenter le ticket moyen en justifiant le prix."
      },
      {
        "q": "Génère-t-il du contenu visuel pour Instagram et la carte ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles de chaque verre pour Instagram, le web et la carte ; InstaFlow AI Pro planifie le contenu avec un calendrier éditorial. Rappelez-vous que l'image IA est une référence visuelle : la photo finale, c'est vous qui la réalisez avec votre cocktail réellement dressé."
      },
      {
        "q": "Comment m'aide-t-il avec la saisonnalité de la carte ?",
        "a": "Gastro Calendar planifie les cartes saisonnières (été, automne, Noël, Saint-Valentin) à l'avance. Le Kit Plan Financiero projette un cash flow saisonnier réaliste pour que vous arriviez avec les stocks et la trésorerie nécessaires à chaque pic."
      }
    ],
    "ctaTitle": "Votre cocktailerie avec marge réelle et technique d'auteur.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Barman et Cocktailier : Cartes, Calculs de Coût et Storytelling | AI Chef Pro",
      "description": "Suite d'IA pour barmans professionnels : Bar & Lounge AI+, Food Pairing AI, calculs de coût par verre, fiches techniques avec storytelling et branding visuel. Commencez dès aujourd'hui.",
      "keywords": "IA barman, IA cocktailier, logiciel cocktail, calcul de coût cocktail, food pairing IA, carte cocktails IA, mixologue IA, signature cocktail",
      "ogImage": "https://aichef.pro/og/use-cases/bartender-coctelero.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Bar dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes dans lequel vous lui décrivez le type de bar que vous exploitez (bar à cocktails d'auteur, cave à vins, bar d'hôtel, lounge, restaurant avec cocktail), la taille de l'équipe, la ville et le style de carte. Chaque agent — de Bar & Lounge AI+ à Gastro Calendar — répond en s'adaptant à votre produit, votre marché et votre exploitation réelle.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Bar",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Créativité Culinaire",
        "description": "Agent spécialisé en cocktail professionnel, vins, bières et spiritueux avec une technique avancée."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Combinaisons inattendues avec une base scientifique et des accords cocktail + plat."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de cocktails signatures avec recette + calcul de coût CSV."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour textures avancées, gélifiants et techniques de bar d'auteur."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue tSpoonLab pour les applications avancées de mixologie."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données de pertes au bar : casse, sur-versement, évaporation, garnitures gaspillées."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par verre : sulfites, produits laitiers, fruits à coque, gluten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie gastronomique IA de référence pour le web, les réseaux sociaux et la carte de cocktails."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial professionnel pour la cocktailerie d'auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients locaux qui recherchent « cocktail bar près de moi » sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Planification de la carte saisonnière : été, hiver, Saint-Valentin, Noël."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capture un trafic organique stable pour les cocktails avec storytelling."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge après calcul des coûts de la carte"
      },
      {
        "value": "×3",
        "label": "engagement Instagram avec GastroIMG"
      },
      {
        "value": "−1 jour",
        "label": "finalisation de la carte de saison (de 7 à 1)"
      },
      {
        "value": "12+",
        "label": "agents pour votre bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Cartes finalisées en une semaine de serviettes et de calculatrice",
        "Calculs de coût sans food cost réel par verre, signatures à perte sans le savoir",
        "Fiches techniques inexistantes : chaque serveur réplique comme il peut",
        "Pertes au bar sans traçabilité réelle",
        "Instagram improvisé avec des photos du mobile sans continuité"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Carte de saison finalisée en un jour avec calcul de coût professionnel et storytelling",
        "Food cost réel par verre, signatures avec marge validée",
        "Fiches techniques avec recette, technique, garniture, verrerie, accord et storytelling",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques au bar",
        "Instagram avec calendrier éditorial professionnel et GastroIMG Gen+"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Bar d'Auteur",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : bar, cocktails, technique, mise en place, ingrédients et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Pizzaiolo et Pizzaïolo",
    "heroSubtitle": "Optimisez pâtes et fermentations, calculez chaque pizza avec un coût réel, maîtrisez la cuisson et l'exploitation avec une suite d'agents IA gastronomiques spécialisés en cuisine italienne professionnelle.",
    "heroTagline": "Pizza à la technique authentique et à la marge réelle",
    "badge": "Pour pizzaioli, pizzaïolos et propriétaires de pizzeria",
    "painsTitle": "Ce qu'un Pizzaiolo Ne Peut Pas Ignorer",
    "pains": [
      "Standardiser pâte, hydratation et fermentation à chaque service avec un critère technique (napoletana, romana, in pala, américaine)",
      "Calculer les coûts des pizzas avec de nombreuses variantes de toppings et maintenir un food cost cohérent entre toutes les options de la carte",
      "Pertes sur pâte (surfermentation, formage raté), mozzarella (humidité, évaporation) et sauces",
      "Maintenir une qualité constante au four (bois, électrique, gaz) avec des pics de demande élevés le week-end",
      "Se différencier dans une zone concurrentielle avec des pizzas signature, des farines premium et un storytelling visuel",
      "Attirer les commandes de livraison avec marge tout en gérant le restaurant en salle"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Pizzaiolo",
    "features": [
      {
        "icon": "Pizza",
        "title": "Cuisine Italienne",
        "description": "Agent spécialisé en cuisine italienne professionnelle : pâtes (napoletana, romana, in pala, américaine), sauces, toppings et technique de four."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Pour levains, préferments (biga, poolish), hydratations élevées et fermentations longues contrôlées à froid."
      },
      {
        "icon": "Calculator",
        "title": "Calculs par pizza",
        "description": "Cuisine Italienne fournit recette + fichier CSV de coût ; Kit de Escandallos Pro le gère avec coût réel par pizza, food cost % et prix suggéré."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pizzería",
        "description": "Modèles : mise en place de la pâte, préparation des sauces, mise en place des toppings, service en salle, livraison, fermeture et nettoyage du four."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC pizzeria",
        "description": "Traçabilité des farines, levain, mozzarella, sauces et températures critiques au four et en chambre froide."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification de la carte saisonnière : pizzas d'été avec tomate fraîche, automne avec champignons et truffe, spéciales pour la Saint-Valentin et événements."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie gastronomique IA de référence + Instagram avec calendrier éditorial : la pizzeria vit de l'impact visuel."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Attirer les clients locaux qui cherchent « pizzeria près de moi » sur Google et Maps avec des descriptions optimisées."
      },
      {
        "icon": "Sparkles",
        "title": "Rendement GenCal",
        "description": "Données précises sur les pertes par processus (pâte, mozzarella, chutes, livraison) intégrées au calcul des coûts."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Pizzaiolo avec AI Chef Pro",
    "workflow": [
      "08:00 · Ouverture — checklist Kit de Tareas Pizzería : rafraîchissement du levain ou de la biga, préparation de la sauce tomate San Marzano, fermentation contrôlée des pâtons.",
      "10:00 · Cuisine Italienne — vous développez une nouvelle pizza saisonnière (courge rôtie, gorgonzola, miel et noix) avec un critère technique. Cuisine Créative fournit recette + fichier CSV de coût.",
      "11:00 · Fermentus Avec AI+ — vous ajustez l'hydratation à 70 % et les temps de fermentation à froid de 48 heures pour la pâte napoletana.",
      "12:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels de farine Caputo, mozzarella di bufala et toppings, validez marge et food cost %.",
      "13:00 · Service de midi — l'équipe réplique avec des modèles de mise en place et de préparation, pics coordonnés.",
      "17:00 · Pause entre services — Gastro Calendar planifie la carte d'automne et les événements.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence de la nouvelle pizza et les posts pour Instagram.",
      "23:00 · Fermeture — nettoyage en profondeur du four, HACCP signé, préparation de la pâte pour demain."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Pizzeria",
    "productIds": [
      "kit-tareas-pizzeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Nous avons fait le calcul pizza par pizza et découvert que 4 étaient en perte malgré de bonnes ventes. Nous les avons redessinées avec Cuisine Italienne en simplifiant les toppings sans perdre en identité et avons augmenté la marge de 4 points sans toucher au prix. Fermentus a transformé notre pâte : hydratation 70 %, fermentation 48 heures, alvéolage parfait.",
    "testimonialAuthor": "Giovanni Russo",
    "testimonialRole": "Pizzaiolo et propriétaire, pizzeria napoletana",
    "faqTitle": "Questions Fréquentes des Pizzaioli",
    "faqs": [
      {
        "q": "Est-ce adapté à la pizza napoletana, romana, in pala ou américaine ?",
        "a": "Pour les quatre. Cuisine Italienne et Fermentus couvrent tout le spectre des pâtes (alvéolage, hydratation, fermentations), les techniques de cuisson (bois, électrique, gaz) et les styles italiens et américains."
      },
      {
        "q": "Couvre-t-il la technique du levain et des préferments ?",
        "a": "Oui. Fermentus Avec AI+ comprend la biga, le poolish, le levain liquide et solide, les hydratations élevées et les fermentations contrôlées à froid. Il raisonne comme un pizzaiolo professionnel, pas comme des recettes de YouTube."
      },
      {
        "q": "Couvre-t-il la livraison en plus du restaurant ?",
        "a": "Oui. Le Kit de Tareas Pizzería inclut des modèles spécifiques pour la livraison : températures, emballages qui maintiennent la cuisson, pertes de transport et procédures de retrait."
      },
      {
        "q": "Génère-t-il du contenu visuel pour Instagram, Glovo et Uber Eats ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles pour Instagram, les plateformes de livraison et la carte ; meilleure photo = plus de clics et un meilleur classement. Rappelez-vous que l'image IA est une référence visuelle : la photo finale, c'est vous qui la faites avec votre pizza fraîchement cuite."
      },
      {
        "q": "Comment m'aide-t-il avec la saisonnalité et les événements ?",
        "a": "Gastro Calendar planifie les cartes saisonnières (été, automne avec champignons et truffe, spéciales pour la Saint-Valentin, Pâques, Noël). Le Kit Plan Financiero projette le cash flow saisonnier réaliste pour que vous arriviez avec stock et trésorerie à chaque pic."
      }
    ],
    "ctaTitle": "Votre pizzeria avec une marge réelle et une technique authentique.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Pizzaiolo et Pizzaïolo : Pâtes, Calculs et Technique Italienne | AI Chef Pro",
      "description": "Suite IA pour pizzaioli professionnels : Cuisine Italienne, Fermentus pour pâtes et biga, calculs par pizza, modèles et technique authentique. Commencez aujourd'hui.",
      "keywords": "IA pizzaiolo, IA pizzaïolo, logiciel pizzeria, calculs pizza, levain pizza, biga poolish pizza, technique napoletana, pizza romana IA",
      "ogImage": "https://aichef.pro/og/use-cases/pizzero.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Pizzeria dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous décrivez votre type de pizzeria (napoletana authentique, romana al taglio, américaine, mixte avec cuisine italienne, dark kitchen pour la livraison), la taille de l'équipe, la ville et le type de four. Chaque agent — de Cuisine Italienne à Gastro Calendar — s'adapte à votre produit, votre marché et votre exploitation réelle.",
    "appsTitle": "Les Agents IA que Vous Utiliserez dans Votre Pizzeria",
    "apps": [
      {
        "name": "Cuisine Italienne",
        "category": "Créativité Culinaire",
        "description": "Agent spécialisé en cuisine italienne professionnelle : pâtes, sauces, toppings, technique de four."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "Levains, biga, poolish, hydratations élevées, fermentations longues contrôlées."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de pizzas signature avec recette + fichier CSV de coût."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour farines techniques, améliorants et combinaisons avancées."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes sur pâte, mozzarella, sauce, chutes et livraison intégrées au calcul des coûts."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par pizza : gluten, produits laitiers, fruits à coque, œuf."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie gastronomique IA de référence pour Glovo, Uber Eats, site web et réseaux sociaux."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial professionnel pour pizzeria de spécialité."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients locaux qui cherchent « pizzeria près de moi » sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Planification de la carte saisonnière : été, automne, Saint-Valentin, Noël."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capte un trafic organique stable pour les pizzas avec storytelling."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles SEO sur la technique italienne, les pâtes et les accords pour attirer du trafic."
      }
    ],
    "metrics": [
      {
        "value": "+4 pts",
        "label": "de marge après calcul des pizzas"
      },
      {
        "value": "×3",
        "label": "d'engagement Instagram avec GastroIMG"
      },
      {
        "value": "−25 %",
        "label": "de pertes sur pâte et mozzarella"
      },
      {
        "value": "12+",
        "label": "agents pour votre pizzeria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Pâte improvisée à chaque service : alvéolage incohérent et croquant irrégulier",
        "Calculs sans food cost réel, pizzas en perte sans le savoir",
        "Pertes sur pâte, mozzarella et sauce sans traçabilité",
        "Instagram improvisé et plateformes de livraison avec photos du téléphone",
        "HACCP sur papier imprimé dispersé dans la pizzeria"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Pâte avec critère technique : hydratation, fermentation et cuisson cohérentes",
        "Calcul professionnel par pizza avec marge validée et food cost %",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO attirent clients locaux et livraison",
        "HACCP depuis le mobile avec enregistrements prêts pour l'inspection"
      ]
    },
    "galleryTitle": "Comment Fonctionne une Pizzeria Authentique",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : pâte, four, technique, ingrédients, pizzas et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Boulanger Artisanal",
    "heroSubtitle": "Optimisez le levain et les préferments, calculez le coût par pièce avec le coût horaire d'atelier, contrôlez les fermentations longues et l'exploitation avec une suite d'agents IA gastronomiques spécialisés en boulangerie artisanale.",
    "heroTagline": "Boulangerie artisanale avec technique et marge réelle",
    "badge": "Pour les boulangers artisanaux et les ateliers",
    "painsTitle": "Ce qu'un boulanger artisanal doit absolument résoudre",
    "pains": [
      "Standardiser le levain, les préferments (biga, poolish), les hydratations et les processus de fermentation longue à chaque équipe",
      "Calculer le coût des pièces avec le coût réel incluant les heures d'atelier (rafraîchissement, pétrissage, façonnage, cuisson prennent du temps)",
      "Pertes dans les pâtes, préferments, chutes de façonnage et cuisson ratée",
      "Production ajustée à la demande quotidienne sans surproduction ni rupture de stock avant la fermeture",
      "Se différencier dans une zone concurrentielle avec des farines premium, des céréales anciennes et un branding artisanal",
      "Capter des commandes de la restauration locale (restaurants, cafés) avec marge tout en gérant la vente directe"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Boulanger",
    "features": [
      {
        "icon": "Wheat",
        "title": "Boulangerie Créative",
        "description": "Agent spécialisé en boulangerie artisanale professionnelle : levains, hydratations élevées, technique de façonnage et cuisson au four."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Pour levains liquides et solides, préferments (biga, poolish), fermentations longues contrôlées à froid et technique avancée."
      },
      {
        "icon": "Cake",
        "title": "Pâtisserie Créative",
        "description": "Pour les ateliers qui combinent boulangerie avec viennoiserie et pâtisserie : brioche, croissants, ensaïmadas et viennoiserie artisanale."
      },
      {
        "icon": "Calculator",
        "title": "Calcul de coût par pièce avec coût horaire d'atelier",
        "description": "Cuisine Créative fournit recette + calcul de coût CSV ; Kit de Escandallos Pro le gère avec coût horaire d'atelier intégré dans la marge réelle par miche, baguette ou brioche."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Obrador",
        "description": "Modèles : rafraîchissement du levain, préferments, pétrissages, fermentations, façonnage, cuisson, vitrine et conservation."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC boulangerie",
        "description": "Traçabilité des farines, levain, préferments, conservation et températures critiques en chambre de fermentation."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification saisonnière avec dates clés : Pâques (monas, hornazos), Noël (Roscón, panettone), Saint-Jean, événements locaux."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Photographie gastronomique IA de référence + Pinterest, où la boulangerie artisanale capte un trafic organique stable."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Capter des clients locaux qui recherchent \"boulangerie artisanale près de moi\" sur Google et Maps."
      }
    ],
    "workflowTitle": "Une journée réelle d'un boulanger avec AI Chef Pro",
    "workflow": [
      "04:00 · Ouverture — checklist Kit de Tareas Obrador : rafraîchissement du levain, contrôle des fermentations de la nuit, allumage du four.",
      "05:30 · Façonnage et cuisson — façonnage de miches, baguettes et brioches avec des modèles spécifiques, contrôle des pertes de chutes.",
      "08:00 · Réapprovisionnement de la vitrine — première fournée prête pour la vente directe et les commandes pour la restauration locale.",
      "10:00 · Boulangerie Créative — vous développez un nouveau pain aux céréales anciennes avec levain liquide. Cuisine Créative fournit recette + calcul de coût CSV.",
      "11:00 · Fermentus Avec AI+ — vous ajustez l'hydratation à 80 % et la fermentation à froid de 24 heures pour le nouveau pain.",
      "12:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels de farine bio et le coût horaire d'atelier, vous validez la marge.",
      "15:00 · GastroIMG Gen+ + Pinterest Pins Gen — vous générez l'image de référence du nouveau pain et les épingles pour capter du trafic organique.",
      "20:00 · Fermeture — nettoyage, APPCC signé, préparation des pâtes pour fermentation nocturne."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Boulangerie",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Nous sommes passés de feuilles volantes à un système. Nous savons exactement quelle pièce est rentable et laquelle ne l'est pas, en incluant le coût horaire d'atelier. Les pertes ont chuté de 30 % en 3 mois et nous avons découvert que deux pains historiques n'étaient pas rentables sans coût horaire — nous les avons redessinés en simplifiant le processus sans perdre en qualité et avons augmenté la marge de 5 points.",
    "testimonialAuthor": "Ana Iglesias",
    "testimonialRole": "Boulangère artisanale, atelier propre",
    "faqTitle": "Questions Fréquentes des Boulangers",
    "faqs": [
      {
        "q": "Couvre-t-il la technique du levain professionnel ?",
        "a": "Oui. Boulangerie Créative et Fermentus raisonnent comme un boulanger professionnel : rafraîchissements avec pourcentage d'inoculation, hydratations par type de pain, fermentations contrôlées à froid 24-48 heures, équilibre des souches. Pas de recettes de YouTube."
      },
      {
        "q": "Convient-il pour un atelier artisanal petit ou industriel ?",
        "a": "Pour les deux. Les modèles évoluent de l'atelier familial de 2 personnes à la production industrielle. La méthodologie est la même : recette → calcul de coût CSV avec coût horaire d'atelier → marge réelle."
      },
      {
        "q": "Couvre-t-il la viennoiserie et la pâtisserie en plus de la boulangerie ?",
        "a": "Oui. Pâtisserie Créative complète le catalogue si vous faites des brioches, croissants, ensaïmadas, viennoiseries de Pâques ou des pâtisseries. Fermentus Avec AI+ couvre la partie fermentée avec une technique professionnelle."
      },
      {
        "q": "Génère-t-il du contenu visuel pour la vitrine, Instagram et Pinterest ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles du pain pour la vitrine, le web et les réseaux ; Pinterest Pins Gen capte un trafic organique stable que la boulangerie artisanale exploite beaucoup. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre miche fraîchement cuite."
      },
      {
        "q": "Comment m'aide-t-il avec la saisonnalité et les événements ?",
        "a": "Gastro Calendar planifie les saisons clés (Pâques avec monas et hornazos, Noël avec Roscón et panettone, Saint-Jean, événements locaux) à l'avance. Le Kit Plan Financiero projette le cash flow saisonnier réaliste."
      }
    ],
    "ctaTitle": "Votre boulangerie artisanale avec une marge claire et une technique professionnelle.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Boulanger Artisanal : Levain, Calculs de Coût et Technique Professionnelle | AI Chef Pro",
      "description": "Suite IA pour boulangers artisanaux : Boulangerie Créative, Fermentus Avec AI+ pour le levain, calculs de coût par pièce avec coût horaire d'atelier. Commencez aujourd'hui.",
      "keywords": "IA boulanger, boulangerie artisanale IA, levain IA, logiciel boulangerie, calculs de coût boulangerie, fermentus, biga poolish, boulanger professionnel",
      "ogImage": "https://aichef.pro/og/use-cases/panadero.jpg"
    },
    "personalizationTitle": "Personnalisé à votre atelier dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes dans lequel vous racontez quel type de boulangerie vous exploitez (artisanale avec levain, boulangerie traditionnelle, atelier avec viennoiserie, boulangerie avec café, boulangerie bio), taille de l'équipe, ville et spécialité. Chaque agent — de Boulangerie Créative à Gastro Calendar — répond adapté à votre produit, marché et exploitation réelle.",
    "appsTitle": "Les agents IA que vous allez utiliser dans votre boulangerie",
    "apps": [
      {
        "name": "Boulangerie Créative",
        "category": "Créativité Culinaire",
        "description": "Agent spécialisé en boulangerie artisanale professionnelle, levains, hydratations et technique."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "Levains, biga, poolish, hydratations élevées et fermentations longues contrôlées."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Brioche, croissants, ensaïmades et viennoiserie artisanale complémentaire."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de pains signature avec recette + calcul de coût CSV."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa : farines techniques, améliorants, graines et céréales anciennes."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes en pâte, préferments, chutes de façonnage et cuisson."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par pièce : gluten, produits laitiers, fruits à coque, œuf."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie gastronomique IA de référence pour vitrine, web et réseaux sociaux."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capte un trafic organique stable pour la boulangerie artisanale."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial professionnel pour boulangerie de créateur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Capter des clients locaux qui recherchent \"boulangerie artisanale près de moi\" sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Planification saisonnière : Pâques, Noël, Saint-Jean, événements locaux."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge après calcul de coût des pièces"
      },
      {
        "value": "−30 %",
        "label": "pertes en atelier et cuisson"
      },
      {
        "value": "×2",
        "label": "trafic organique via Pinterest"
      },
      {
        "value": "12+",
        "label": "agents pour votre boulangerie"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Levain improvisé, fermentations incohérentes d'une équipe à l'autre",
        "Calculs de coût sans coût horaire d'atelier, pains complexes en perte sans le savoir",
        "Pertes en pâtes, préferments et cuisson sans traçabilité",
        "Vitrine et réseaux sociaux improvisés avec des photos du téléphone",
        "APPCC sur papier imprimé dispersé dans l'atelier"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Levain avec critère technique : rafraîchissements, hydratations et fermentations cohérentes",
        "Calcul de coût professionnel par pièce avec coût horaire d'atelier intégré",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ captent un trafic stable",
        "APPCC depuis le mobile avec des registres prêts pour l'inspection"
      ]
    },
    "galleryTitle": "Comment Fonctionne une Boulangerie Artisanale",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : vitrine, levain, fermentation, pains, cuisson et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Chocolatier et Confiseur",
    "heroSubtitle": "Concevez chocolats, tablettes et couvertures avec fiche technique professionnelle, technique de tempérage et planification saisonnière grâce à une suite d'agents IA spécialisés en chocolaterie artisanale de créateur.",
    "heroTagline": "Chocolaterie avec technique authentique et marge réelle",
    "badge": "Pour chocolatiers, confiseurs et maîtres chocolatiers",
    "painsTitle": "Ce Qu'un Chocolatier Ne Peut Pas Ignorer",
    "pains": [
      "Cacao au prix volatil qui change le coût réel chaque semaine sans prévenir et oblige à recalculer constamment les fiches techniques",
      "Technique de tempérage exigeante : cristallisation en forme V, courbes précises selon la couverture, brillance et cassure nette constantes",
      "Pertes en laboratoire (tempérage raté, chutes, moules mal pris, refroidissement) qui saignent la rentabilité sans contrôle",
      "Saisonnalité extrême : Noël, Saint-Valentin, Pâques et Galette des Rois concentrent un pourcentage élevé du chiffre d'affaires annuel",
      "Se différencier dans une zone concurrentielle avec des chocolats de créateur, un packaging premium et un storytelling visuel de marque",
      "Attirer les commandes d'entreprise, mariages et événements avec marge tout en gérant la production quotidienne"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Chocolatier",
    "features": [
      {
        "icon": "Cookie",
        "title": "Chocolaterie Créative",
        "description": "Agent spécialisé en chocolaterie professionnelle : chocolats, ganaches, pralinés, tablettes, couvertures, technique de tempérage et courbes de cristallisation."
      },
      {
        "icon": "Cake",
        "title": "Pâtisserie Créative",
        "description": "Pour les desserts au chocolat, bouchées, brownies, mousses et combinaisons avancées chocolat + pâtisserie."
      },
      {
        "icon": "Calculator",
        "title": "Fiches techniques par pièce avec coût horaire du laboratoire",
        "description": "Cuisine Créative fournit recette + fiche technique CSV ; Kit de Escandallos Pro la gère avec le coût horaire du laboratoire intégré dans la marge réelle par chocolat et par boîte."
      },
      {
        "icon": "Beaker",
        "title": "Agent Sosa Ingredients",
        "description": "Assistant du catalogue Sosa pour couvertures techniques, pâtes concentrées, fruits secs et arômes professionnels."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chocolatería",
        "description": "Modèles : tempérage, moulage, ganaches, assemblage, packaging, contrôle des températures en chambre froide."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC chocolaterie",
        "description": "Traçabilité du cacao, des produits laitiers, fruits secs, alcools et conservation professionnelle avec courbes documentées."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification saisonnière avec dates clés : Noël, Saint-Valentin, Pâques, Galette des Rois, Fête des Mères. Calendrier éditorial."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Photographie de créateur IA de référence + Pinterest, où la chocolaterie premium capte un trafic organique stable."
      },
      {
        "icon": "Sparkles",
        "title": "Rendement GenCal",
        "description": "Données précises des pertes par processus (tempérage, moulage, chutes, exposition) intégrées dans la fiche technique."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Chocolatier avec AI Chef Pro",
    "workflow": [
      "07:00 · Ouverture — checklist Kit de Tareas Chocolatería : vérification de la chambre froide, pré-cristallisation de la couverture, préparation des moules en polycarbonate.",
      "08:30 · Chocolaterie Créative — vous développez un nouveau chocolat signature avec praliné de noisette caramélisée et sel de Maldon. Cuisine Créative fournit recette + fiche technique CSV.",
      "09:30 · Agent Sosa Ingredients — vous sélectionnez une couverture technique avec le pourcentage de cacao approprié, du beurre de cacao supplémentaire et du sel de qualité.",
      "10:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels du cacao et le coût horaire du laboratoire intégré, vous validez la marge par chocolat et par boîte de 9 pièces.",
      "11:00 · Production du jour — tempérage sur marbre, moulage, ganache, remplissage, refroidissement et démoulage.",
      "14:00 · Réassort — préparation des coffrets cadeaux professionnels, étiquetage et contrôle des pertes.",
      "16:00 · Gastro Calendar — vous préparez la planification de Noël avec les coffrets d'entreprise (anticipation de 8 semaines).",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — vous générez une image de référence du nouveau signature et des épingles optimisées pour Pinterest.",
      "20:00 · Fermeture — nettoyage en profondeur, APPCC signé, planification des mélanges à refroidir."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour la Chocolaterie",
    "productIds": [
      "kit-tareas-chocolateria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Produire 12 000 chocolats pour Noël sans système était le chaos. Avec Chocolaterie Créative pour le design, Agent Sosa Ingredients pour le support technique, Kit de Escandallos Pro pour la marge réelle avec cacao actualisé et Gastro Calendar pour la planification saisonnière, nous avons sauvé la saison et augmenté la marge de 7 points. Les coffrets d'entreprise se concluent en un appel avec une proposition professionnelle.",
    "testimonialAuthor": "Mónica Salazar",
    "testimonialRole": "Maître chocolatière et propriétaire",
    "faqTitle": "Questions Fréquentes des Chocolatiers",
    "faqs": [
      {
        "q": "Couvre-t-il la technique de tempérage professionnelle et les courbes de cristallisation ?",
        "a": "Oui. Chocolaterie Créative raisonne comme un chocolatier professionnel : tempérage de la couverture par courbes (45-27-31 °C pour la couverture noire), technique de tablage sur marbre, ensemencement, micro-ondes avec beurre de cacao supplémentaire. Pas de recettes YouTube."
      },
      {
        "q": "Convient-il à une petite chocolaterie artisanale, un atelier de créateur ou une chocolaterie avec production à échelle ?",
        "a": "Pour les trois. Les modèles évoluent du laboratoire familial à la production pour plusieurs points de vente ou coffrets d'entreprise avec des centaines d'unités."
      },
      {
        "q": "Comment gérons-nous le prix volatil du cacao ?",
        "a": "Kit de Escandallos Pro recalcule instantanément la marge réelle lorsque vous mettez à jour le prix de la couverture. Rendement GenCal ajoute le coût des pertes par processus. La marge reflète toujours le coût actuel."
      },
      {
        "q": "Génère-t-il du contenu pour la vitrine, les réseaux sociaux et le packaging ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles de chaque chocolat pour la vitrine, le site web et les réseaux sociaux ; Pinterest Pins Gen + InstaFlow AI Pro programment le contenu visuel ; MenuDish Local SEO capte les clients locaux. Rappelez-vous que l'image IA est une référence visuelle : la photo finale, c'est vous qui la faites avec votre chocolat réellement dressé."
      },
      {
        "q": "Comment m'aide-t-il avec la forte saisonnalité ?",
        "a": "Gastro Calendar planifie les saisons clés (Noël, Saint-Valentin, Pâques, Galette des Rois, Fête des Mères) avec 8 à 12 semaines d'anticipation. Le Kit Plan Financiero projette le cash flow saisonnier réaliste pour arriver à chaque pic avec production et trésorerie."
      }
    ],
    "ctaTitle": "Votre chocolaterie avec une marge claire et une technique de créateur.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Chocolatier et Confiseur : Tempérage, Fiches Techniques et Saisonnalité | AI Chef Pro",
      "description": "Suite IA pour chocolatiers professionnels : Chocolaterie Créative, fiches techniques par pièce avec coût horaire du laboratoire, planification saisonnière et APPCC. Commencez aujourd'hui.",
      "keywords": "IA chocolatier, IA confiseur, logiciel chocolaterie, fiches techniques chocolat, chocolaterie artisanale IA, technique tempérage, courbes cristallisation, maître chocolatier",
      "ogImage": "https://aichef.pro/og/use-cases/chocolatero.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Atelier dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous racontez quel type de chocolaterie vous exploitez (atelier de créateur, chocolaterie avec production à échelle, chocolaterie avec café, laboratoire pour vente aux professionnels de la restauration, chocolaterie avec expériences et dégustations), taille de l'équipe, ville et spécialité. Chaque agent — de Chocolaterie Créative à Gastro Calendar — répond adapté à votre produit, marché et opération réelle.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser dans Votre Atelier",
    "apps": [
      {
        "name": "Chocolaterie Créative",
        "category": "Créativité Culinaire",
        "description": "Agent spécialisé en chocolaterie professionnelle : chocolats, ganaches, pralinés, tablettes et technique de tempérage."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Desserts au chocolat, bouchées, brownies, mousses et combinaisons avancées."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de chocolats signature avec recette + fiche technique CSV."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa : couvertures techniques, pâtes concentrées, fruits secs et arômes professionnels."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue tSpoonLab pour applications avancées en chocolaterie."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes en tempérage, moulage, chutes et exposition intégrées dans la fiche technique."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par chocolat : produits laitiers, fruits secs, gluten, alcools."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie de créateur IA de référence pour vitrine, site web, packaging et réseaux sociaux."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capte un trafic organique stable pour la chocolaterie premium."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial pour chocolaterie de créateur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients locaux qui recherchent \"chocolaterie artisanale près de moi\" sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Planification saisonnière : Noël, Saint-Valentin, Pâques, Galette des Rois, Fête des Mères."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "marge après fiche technique des chocolats"
      },
      {
        "value": "−35 %",
        "label": "pertes en laboratoire et vitrine"
      },
      {
        "value": "×2",
        "label": "commandes d'entreprise à Noël"
      },
      {
        "value": "12+",
        "label": "agents pour votre atelier"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Tempérage improvisé : brillance et cassure incohérentes pièce par pièce",
        "Cacao volatil qui déséquilibre les prix sans recalcul en temps réel",
        "Pertes en tempérage, moulage et vitrine sans traçabilité réelle",
        "Production saisonnière réactive : vous arrivez en retard à Noël et perdez des commandes d'entreprise",
        "APPCC sur papier imprimé dispersé dans l'atelier"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Tempérage par courbes avec critère technique, brillance et cassure constantes",
        "Fiche technique professionnelle par chocolat avec cacao actualisable et coût horaire intégré",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ captent un trafic stable et des commandes",
        "APPCC depuis le mobile avec registres prêts pour inspection"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Atelier de Chocolaterie",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : tempérage, moulage, chocolats, ganache et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Chef Privé et Personal Chef",
    "heroSubtitle": "Concevez des menus personnalisés pour des clients uniques, calculez chaque dîner privé avec un coût réel, planifiez la mise en place dans des maisons particulières et capturez un branding professionnel avec une suite d'agents IA gastronomiques spécialisés en chef privé et service en maisons particulières.",
    "heroTagline": "Service privé avec marge réelle et technique d'auteur",
    "badge": "Pour chefs privés, personal chefs et traiteur intime",
    "painsTitle": "Ce qu'un Chef Privé ne peut pas manquer de résoudre",
    "pains": [
      "Concevoir des menus entièrement personnalisés par client : allergies, intolérances, préférences, régime, occasion et esthétique du dressage",
      "Calculer le coût de chaque dîner privé avec un coût réel (achat du jour, ingrédients premium) et un prix personnalisé",
      "Planifier la mise en place dans des maisons particulières avec des cuisines non professionnelles (sans équipement, espace limité, feux inconnus)",
      "Standardiser les fiches techniques pour que le client puisse répéter le menu ou préserver la recette comme souvenir",
      "Se différencier dans une zone concurrentielle avec un storytelling personnel, un branding visuel d'auteur et une acquisition via les réseaux",
      "Attirer des clients premium récurrents (familles VIP, cadres, célébrités) avec des propositions professionnelles et personnalisées"
    ],
    "featuresTitle": "Comment AI Chef Pro aide un Chef Privé",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Chef Privé Pro",
        "description": "Agent spécialisé du catalogue Gastro Profile Pro : raisonne comme un personal chef professionnel avec de l'expérience dans les maisons particulières et les événements intimes."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour le développement de menus personnalisés avec une technique avancée : dressages d'auteur, fusions contrôlées, desserts signature."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Accords personnalisés avec la cave du client ou propositions de vins pour chaque plat du menu privé."
      },
      {
        "icon": "Calculator",
        "title": "Calcula Pax + Escandallos",
        "description": "Calcula Pax escalade les recettes à 2, 6, 12 convives ; Kit de Escandallos Pro le gère avec un coût réel par dîner privé et un prix personnalisé."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chef Privado",
        "description": "Modèles : pré-visite de la cuisine du client, liste de courses, mise en place transportable, plan de service, nettoyage, facture."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Allergènes",
        "description": "Identification automatique des allergènes par client : critique lorsque vous travaillez avec des familles ayant des intolérances spécifiques."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification de menus saisonniers et pour des dates spéciales : Noël, Saint-Valentin, anniversaires, fêtes."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie premium IA de référence + Instagram pour attirer de nouveaux clients et construire une réputation d'auteur."
      },
      {
        "icon": "BookOpen",
        "title": "Fiche technique + facture",
        "description": "Modèle professionnel à remettre au client : fiche technique du menu avec recette + storytelling + facture claire."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Chef Privé avec AI Chef Pro",
    "workflow": [
      "07:00 · Pré-visite — checklist Kit de Tareas Chef Privé : révision de la cuisine du client (équipements, espace, allergies et préférences confirmées).",
      "08:00 · Chef Privé Pro — vous développez le menu personnalisé pour un dîner intime de 6 couverts avec allergie aux fruits à coque. Cuisine Créative livre recette + calcul de coût CSV.",
      "09:00 · Calcula Pax — vous escaladez les recettes de 6 à 8 convives (le client a ajouté deux invités). Kit de Escandallos Pro recalcule le coût et la proposition.",
      "10:00 · Liste de courses — vous allez au marché avec la liste priorisée : produit du jour, ingrédients premium spécifiques.",
      "14:00 · Arrivée au domicile du client — montage de la mise en place dans une cuisine particulière en suivant le plan transportable, organisation de l'espace.",
      "17:00 · Service du dîner — exécution du menu avec une technique professionnelle adaptée à la cuisine du client, dressage sur porcelaine fine.",
      "21:00 · Clôture avec le client — remise de la fiche technique du menu avec storytelling + facture professionnelle + photo de référence du menu.",
      "23:00 · Post-dîner — InstaFlow AI Pro : post Instagram avec l'image de référence du menu (sans visages du client) pour construire une réputation."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Chef Privé",
    "productIds": [
      "kit-tareas-chef-privado",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Chef Privé Pro a changé ma proposition commerciale. Maintenant, chaque client reçoit un menu personnalisé avec un calcul de coût professionnel et un storytelling, et l'acquisition via Instagram avec GastroIMG Gen+ a été multipliée. Je conclus des propositions en un appel car je livre une fiche technique + une facture le même jour. Nous avons augmenté le ticket moyen de 35 % par dîner.",
    "testimonialAuthor": "Andrea Gómez",
    "testimonialRole": "Chef privée freelance, Madrid + côte",
    "faqTitle": "Questions Fréquentes des Chefs Privés",
    "faqs": [
      {
        "q": "Est-ce que cela convient pour un chef privé freelance, une agence de personal chef ou un traiteur intime ?",
        "a": "Pour les trois. Chef Privé Pro raisonne comme un personal chef professionnel, il convient aussi bien pour un freelance qui conçoit sa proposition que pour des agences avec plusieurs chefs."
      },
      {
        "q": "Comment gérer les allergies et les régimes spéciaux par client ?",
        "a": "ID Allergènes identifie automatiquement les allergènes par recette. Chef Privé Pro raisonne en termes de personnalisation : régimes keto, végétalien, sans gluten, faible en sodium, FODMAP, grossesse. Chaque client reçoit un menu réellement adapté."
      },
      {
        "q": "Comment escalader les recettes pour différents nombres de convives ?",
        "a": "Calcula Pax escalade les recettes à 2, 6, 12 ou tout autre nombre de convives sans perdre en précision. Kit de Escandallos Pro recalcule le coût par personne et la proposition économique au client."
      },
      {
        "q": "Génère-t-il du contenu visuel pour Instagram et une réputation d'auteur ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles du menu (sans montrer le client) pour Instagram, le web et le portfolio. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre plat réellement dressé à chaque dîner."
      },
      {
        "q": "Comment m'aide-t-il à attirer des clients récurrents ?",
        "a": "GastroIMG Gen+ + InstaFlow AI Pro construisent un contenu visuel constant ; MenuDish Local SEO capture les clients locaux qui recherchent \"chef privé à [ville]\" ; Gastro Calendar aide à proposer des menus saisonniers (Noël intime, Saint-Valentin, anniversaires) pour fidéliser."
      }
    ],
    "ctaTitle": "Votre service de chef privé avec une marge réelle et une proposition d'auteur.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Chef Privé et Personal Chef : Menus, Calculs de coût et Service | AI Chef Pro",
      "description": "Suite IA pour chefs privés professionnels : Chef Privé Pro, calculs de coût par dîner, menus personnalisés, branding et acquisition. Commencez aujourd'hui.",
      "keywords": "IA chef privé, IA personal chef, logiciel chef privé, calculs de coût dîner privé, chef privé madrid, personal chef freelance",
      "ogImage": "https://aichef.pro/og/use-cases/chef-privado.jpg"
    },
    "personalizationTitle": "Personnalisé à votre service de Chef Privé dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes dans lequel vous lui racontez quel type de service vous opérez (chef privé freelance, agence avec plusieurs chefs, traiteur intime pour mariages et événements privés, chef de yacht), type de clientèle (familles VIP, cadres, célébrités), ville et spécialité. Chaque agent — du Chef Privé Pro au Gastro Calendar — répond adapté à votre proposition et à votre opération réelle.",
    "appsTitle": "Les Agents IA que vous allez utiliser en tant que Chef Privé",
    "apps": [
      {
        "name": "Chef Privé Pro",
        "category": "Gastro Profile Pro",
        "description": "Agent spécialisé du catalogue Gastro Profile Pro : raisonne comme un personal chef professionnel."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de menus personnalisés avec une technique avancée et recette + calcul de coût CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords personnalisés avec la cave du client ou propositions de vins."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Escalade de recettes pour différents nombres de convives."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par client et recette."
      },
      {
        "name": "Conversor Ing",
        "category": "Outils et Utilitaires",
        "description": "Convertisseur de poids et mesures, critique lorsqu'on travaille avec des cuisines non professionnelles."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Rendement sur l'achat du jour et produit premium."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie premium IA de référence pour Instagram, portfolio et acquisition."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial professionnel pour attirer des clients récurrents."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients locaux qui recherchent \"chef privé à [ville]\" sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Menus saisonniers : Noël intime, Saint-Valentin, anniversaires, fêtes."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'Affaires",
        "description": "Pour une mixologie personnalisée lors de dîners privés."
      }
    ],
    "metrics": [
      {
        "value": "+35 %",
        "label": "ticket moyen par dîner privé"
      },
      {
        "value": "×3",
        "label": "acquisition de clients via Instagram"
      },
      {
        "value": "×5",
        "label": "vitesse des propositions commerciales"
      },
      {
        "value": "12+",
        "label": "agents pour votre service privé"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Menus personnalisés à la main : une semaine par proposition",
        "Calculs de coût sans coût réel, propositions commerciales avec une marge incertaine",
        "Pré-visite et mise en place improvisée à chaque fois",
        "Acquisition par bouche-à-oreille, sans Instagram constant",
        "Sans fiche technique remise au client comme souvenir"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Menu personnalisé en une heure avec Chef Privé Pro",
        "Calcul de coût professionnel par dîner avec marge validée",
        "Pré-visite et mise en place avec modèle transportable Kit de Tareas",
        "Acquisition constante avec GastroIMG Gen+ + InstaFlow AI Pro",
        "Fiche technique du menu + facture remise le même jour"
      ]
    },
    "galleryTitle": "Comment fonctionne le service de Chef Privé",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : mise en place, plat dressé, table dressée, garde-manger et service. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour F&B Manager d'hôtel",
    "heroSubtitle": "Coordonnez restaurants, banquets, room service, breakfast buffet et bars d'hôtel avec un calcul des coûts croisé, des modèles opérationnels professionnels et une intégration de marque avec une suite d'agents d'IA gastronomique spécialisés en gestion intégrée F&B hôtelière.",
    "heroTagline": "F&B hôtelier avec une marge réelle et une opération professionnelle",
    "badge": "Pour les F&B Managers, Directeurs des Aliments et Boissons",
    "painsTitle": "Ce qu'un F&B Manager doit impérativement résoudre",
    "pains": [
      "Coordonner plusieurs points de vente simultanés (restaurant principal, room service, breakfast buffet, bar de piscine, banquets, cafétéria)",
      "Calculer les coûts d'une carte croisée entre points de vente tout en maintenant la cohérence du food cost et une marge intégrée",
      "Pertes élevées au breakfast buffet (offre abondante avec consommation variable) et dans les banquets (volume élevé, complexité logistique)",
      "Standardiser les procédures par équipe avec des équipes tournantes et trois services par jour",
      "Se différencier dans un hôtel concurrentiel avec une expérience gastronomique intégrale, un branding visuel et un storytelling d'hospitalité",
      "Attirer les événements corporatifs, mariages et banquets premium avec des propositions professionnelles et une marge validée"
    ],
    "featuresTitle": "Comment AI Chef Pro aide un F&B Manager",
    "features": [
      {
        "icon": "Hotel",
        "title": "Manager de Restaurant Pro",
        "description": "Agent spécialisé du catalogue Gastro Profile Pro adapté à la gestion F&B hôtelière multi-points de vente."
      },
      {
        "icon": "PartyPopper",
        "title": "Traiteur IA+",
        "description": "Conseil professionnel pour les banquets, mariages et événements corporatifs de l'hôtel."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour le développement de cartes intégrées : restaurant principal, breakfast buffet, room service et bar de piscine avec cohérence."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Pour la cocktailerie du bar de piscine, du lobby bar et les accords mets du restaurant principal."
      },
      {
        "icon": "Calculator",
        "title": "Calcul des coûts croisé",
        "description": "Cuisine Créative fournit la recette + le calcul des coûts CSV ; Kit de Escandallos Pro le gère avec un coût croisé entre points de vente et une marge intégrée."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Hotel Completo",
        "description": "Modèles pour 5 points de vente : restaurant, breakfast, room service, bar, banquets avec procédures par équipe."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC hôtelier",
        "description": "Traçabilité du buffet, des banquets, du room service et du bar avec températures critiques et conservation."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification d'événements corporatifs, mariages, saisons (été/hiver), Noël, Saint-Valentin, conférences."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie premium IA de référence + Instagram pour tous les points de vente de l'hôtel avec cohérence de marque."
      }
    ],
    "workflowTitle": "Une journée réelle d'un F&B Manager avec AI Chef Pro",
    "workflow": [
      "06:00 · Ouverture du breakfast — checklist Kit de Tareas Hotel : préparation du buffet, contrôle des chafing dishes, températures, mise en place de la station d'œufs.",
      "09:00 · Coordination avec la cuisine principale — Cuisine Créative met à jour la carte du déjeuner avec des produits de saison. Recette + calcul des coûts CSV.",
      "10:00 · Traiteur IA+ — vous développez la proposition de menu pour un mariage de 120 pax en trois plats. Calcula Pax ajuste les recettes, Kit de Escandallos Pro valide le coût et la marge.",
      "12:00 · Service déjeuner au restaurant principal + room service — coordination croisée entre les points de vente.",
      "14:00 · Bar & Lounge AI+ — vous développez la nouvelle carte de cocktails pour le bar de piscine saison estivale.",
      "17:00 · Banquet corporatif de 80 pax — exécution avec le modèle spécifique du Kit de Tareas.",
      "20:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez des images de référence pour les quatre points de vente et les publications cohérentes pour l'Instagram de l'hôtel.",
      "23:00 · Fermeture — nettoyage approfondi multi-points de vente, APPCC signé, planification du breakfast et des services du lendemain."
    ],
    "productsTitle": "Modèles et kits recommandés pour F&B Manager",
    "productIds": [
      "kit-tareas-hotel",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Gérer cinq points de vente sans système était un chaos. Le Manager de Restaurant Pro + Traiteur IA+ coordonnent notre carte croisée, les banquets et le room service avec un calcul des coûts intégré. La planification des mariages pour 120 pax qui prenait une semaine prend désormais une journée avec une proposition professionnelle. Nous avons augmenté la marge de 5 points en croisant les points de vente et nous remportons des événements premium beaucoup plus rapidement.",
    "testimonialAuthor": "Roberto Castaño",
    "testimonialRole": "Directeur F&B, hôtel 5 étoiles",
    "faqTitle": "Questions Fréquentes des F&B Managers",
    "faqs": [
      {
        "q": "Est-ce que cela convient pour un hôtel boutique, un hôtel de chaîne, all-inclusive ou un hôtel de luxe ?",
        "a": "Pour les quatre. Manager de Restaurant Pro + Traiteur IA+ + Bar & Lounge IA+ couvrent depuis un hôtel boutique avec un restaurant jusqu'à un hôtel 5 étoiles avec 5+ points de vente, all-inclusive avec buffet massif ou resort vacancier."
      },
      {
        "q": "Comment coordonner la carte croisée entre les points de vente ?",
        "a": "Cuisine Créative raisonne avec cohérence entre les points de vente : produit du menu principal utilisé au breakfast, au room service et dans les banquets, optimisant le food cost intégré et réduisant les pertes croisées."
      },
      {
        "q": "Comment adapter les calculs de coûts pour des banquets de 50, 100 ou 300 pax ?",
        "a": "Calcula Pax ajuste les recettes sans perdre en précision ; Kit de Escandallos Pro recalcule le coût par pax et la proposition économique pour le client corporatif ou de mariage."
      },
      {
        "q": "Génère-t-il un contenu visuel cohérent pour l'Instagram de l'hôtel ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles pour les quatre points de vente avec cohérence de marque ; InstaFlow AI Pro programme Instagram. N'oubliez pas que l'image IA est une référence visuelle : la photo finale, c'est vous qui la faites avec votre plat réellement dressé."
      },
      {
        "q": "Comment cela m'aide-t-il avec les événements corporatifs et les saisons ?",
        "a": "Gastro Calendar planifie les événements corporatifs, les mariages, les conférences, les saisons (été/hiver), Noël et la Saint-Valentin avec des menus spécifiques par point de vente et un calendrier éditorial coordonné."
      }
    ],
    "ctaTitle": "Votre F&B hôtelier avec une marge intégrée et une opération professionnelle.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour F&B Manager d'Hôtel : Multi-points de vente, Banquets et Calcul des coûts | AI Chef Pro",
      "description": "Suite IA pour les F&B Managers d'hôtel : Manager de Restaurant Pro, Traiteur IA+, calcul des coûts croisé, branding multi-points de vente et APPCC intégré. Commencez dès aujourd'hui.",
      "keywords": "IA F&B manager, IA hôtel F&B, logiciel hôtel restaurant, calcul des coûts hôtel, banquets hôtel IA, breakfast buffet hôtel",
      "ogImage": "https://aichef.pro/og/use-cases/fb-manager-hotel.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre hôtel dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes où vous racontez quel type d'hôtel vous gérez (boutique, chaîne, 5 étoiles, all-inclusive, resort vacancier), le nombre de points de vente F&B, la taille de l'équipe et la spécialité. Chaque agent — du Manager de Restaurant Pro au Traiteur IA+ — répond adapté à votre hôtel réel.",
    "appsTitle": "Les agents IA que vous allez utiliser en tant que F&B Manager",
    "apps": [
      {
        "name": "Manager de Restaurant Pro",
        "category": "Gastro Profile Pro",
        "description": "Agent spécialisé adapté à la gestion F&B hôtelière multi-points de vente."
      },
      {
        "name": "Traiteur IA+",
        "category": "Concepts d'Affaires",
        "description": "Banquets, mariages et événements corporatifs de l'hôtel avec des propositions professionnelles."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Cartes intégrées avec cohérence entre points de vente et recette + calcul des coûts CSV."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'Affaires",
        "description": "Pour la cocktailerie du bar de piscine, du lobby bar et les accords mets du restaurant principal."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'Affaires",
        "description": "Pour le restaurant décontracté et la cafétéria de l'hôtel."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Ajustement des recettes pour des banquets de 50, 100, 300 ou 500 pax."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes au breakfast buffet, dans les banquets et au room service."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique pour les clients avec allergies dans les banquets."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie premium IA de référence avec cohérence de marque pour tous les points de vente."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial coordonné pour tous les points de vente."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients locaux qui recherchent \"restaurant hôtel\" sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Événements corporatifs, mariages, conférences, Noël, Saint-Valentin, saisons."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge après calcul des coûts croisé"
      },
      {
        "value": "×7",
        "label": "vitesse des propositions de banquet"
      },
      {
        "value": "−25 %",
        "label": "pertes au breakfast buffet"
      },
      {
        "value": "12+",
        "label": "agents pour votre F&B"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Points de vente coordonnés manuellement, food cost croisé sans traçabilité",
        "Banquets calculés à la main : une semaine par mariage",
        "Pertes au breakfast buffet sans contrôle réel",
        "Branding visuel dispersé entre les points de vente sans cohérence",
        "APPCC sur papier imprimé dispersé dans les points de vente"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Points de vente coordonnés avec calcul des coûts croisé et food cost intégré",
        "Banquets calculés en un jour avec proposition professionnelle",
        "Pertes contrôlées avec Rendement GenCal au breakfast et dans les banquets",
        "Branding cohérent avec GastroIMG Gen+ + InstaFlow AI Pro",
        "APPCC depuis mobile multi-points de vente avec enregistrements prêts pour inspection"
      ]
    },
    "galleryTitle": "Comment fonctionne le F&B d'un hôtel",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : restaurant, banquets, breakfast, room service et bar de piscine. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Maître et Chef de Salle",
    "heroSubtitle": "Coordonnez le service en salle avec une technique professionnelle, gérez les réservations premium et les accords mets-vins, menez votre équipe et capturez le branding fine dining avec une suite d'agents d'IA gastronomique spécialisés en salle et en service haut de gamme.",
    "heroTagline": "Salle avec une technique professionnelle et une expérience mémorable",
    "badge": "Pour maîtres, chefs de salle et directeurs de service",
    "painsTitle": "Ce qu'un Maître Ne Peut Pas Manquer de Résoudre",
    "pains": [
      "Coordonner le service en salle avec une séquence parfaite des passes, guéridon, débouchage et un service professionnel à chaque rotation",
      "Gérer les réservations premium avec une planification des tables, les allergies, les occasions spéciales et les préférences des clients réguliers",
      "Mener l'équipe de salle avec une formation continue aux accords mets-vins, à la coutellerie, à la description des plats et au storytelling",
      "Coordonner avec la cuisine passe par passe avec un timing parfait et une communication fluide aux heures de pointe du service",
      "Se différencier dans un restaurant très concurrentiel avec une expérience mémorable, un branding visuel fine dining et l'attraction de clients réguliers",
      "Attirer des événements privés et des dîners d'entreprise avec des propositions professionnelles de service et d'accords mets-vins"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Maître",
    "features": [
      {
        "icon": "Crown",
        "title": "Manager de Restaurant Pro",
        "description": "Agent spécialisé adapté à la gestion de salle fine dining : séquence de service, guéridon, débouchage, formation d'équipe."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Pour une gestion professionnelle de la cave, des débouchages, des recommandations de vin et des cocktails professionnels."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Accords mets-vins à base scientifique pour chaque plat du menu, justification professionnelle pour l'équipe de salle."
      },
      {
        "icon": "Calculator",
        "title": "Calcula Pax + Mise",
        "description": "Calcula Pax pour les banquets, modèles de mise de table, guéridon, séquence des passes."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Modèles : pré-service (mise en place), service (passes), post-service (clôture, nettoyage), formation d'équipe."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC sala",
        "description": "Traçabilité de la cave, conservation des vins, débouchages et températures de service."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Réservations premium, événements privés, dîners d'entreprise, Noël, Saint-Valentin, anniversaires."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie IA élégante de référence + Instagram avec storytelling de service et accords mets-vins pour attirer des clients premium."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling de menu",
        "description": "Génération de descriptions de plats et d'accords mets-vins pour que l'équipe de salle les récite avec professionnalisme devant le client."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Maître avec AI Chef Pro",
    "workflow": [
      "15:00 · Ouverture — checklist Kit de Tareas : révision des réservations du jour, mise de table, polissage de la verrerie et des couverts, contrôle de la cave.",
      "16:00 · Briefing d'équipe — explication des nouveaux plats du jour avec storytelling généré et accords validés avec Food Pairing AI.",
      "17:00 · Coordination avec la cuisine — vérification des changements de carte, allergies confirmées, mise en place des passes.",
      "18:30 · Accueil des premières réservations — attention professionnelle, service d'apéritifs, description de la carte.",
      "20:00 · Service du dîner — coordination passe par passe avec la cuisine, débouchages professionnels, guéridon à table lorsque cela s'applique.",
      "22:00 · Dîners d'entreprise privés — attention dédiée à un événement de 12 couverts avec menu dégustation et accords mets-vins.",
      "00:00 · Fermeture — clôture, départ de l'équipe, GastroIMG Gen+ génère une image de référence du menu dégustation + InstaFlow programme le post.",
      "01:00 · Briefing de clôture — retour de l'équipe, prise de notes des commentaires clients, planification du lendemain."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Maître",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "pro-prompts-ebook",
      "kit-inventario"
    ],
    "testimonialQuote": "Manager de Restaurant Pro + Bar & Lounge AI+ + Food Pairing AI ont complètement élevé le niveau de mon équipe de salle. Le briefing quotidien avec le storytelling généré de chaque plat et des accords validés scientifiquement est désormais professionnel. Les clients remarquent la différence : nous avons augmenté le ticket moyen de 20 % et le taux de clients réguliers premium a progressé de 40 % en six mois.",
    "testimonialAuthor": "Sofía Vega",
    "testimonialRole": "Maître et Chef de Salle, restaurant fine dining",
    "faqTitle": "Questions Fréquentes des Maîtres",
    "faqs": [
      {
        "q": "Est-ce que cela convient au fine dining, au restaurant de chef, au gastronomique Michelin ou au restaurant premium ?",
        "a": "Pour les quatre. Manager de Restaurant Pro + Bar & Lounge AI+ couvrent du restaurant premium au gastronomique Michelin avec un service impeccable, guéridon, débouchage professionnel et storytelling."
      },
      {
        "q": "Comment gérer les réservations premium et les clients réguliers ?",
        "a": "Manager de Restaurant Pro raisonne avec un jugement professionnel de salle : planification des tables par préférence, annotation des allergies et des occasions, attraction des clients réguliers avec des menus personnalisés."
      },
      {
        "q": "Comment former l'équipe de salle aux accords mets-vins et au storytelling ?",
        "a": "Food Pairing AI fonde chaque accord sur une base scientifique que l'équipe peut communiquer au client ; Bar & Lounge AI+ approfondit la cave, le débouchage et les techniques. Le briefing quotidien est désormais professionnel."
      },
      {
        "q": "Génère-t-il un contenu visuel élégant pour Instagram ?",
        "a": "Oui. GastroIMG Gen+ génère des images élégantes de référence du menu et de la table dressée pour Instagram, le web et l'attraction de clients premium. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre vraie table."
      },
      {
        "q": "Comment m'aide-t-il avec les événements privés et les dîners d'entreprise ?",
        "a": "Gastro Calendar planifie les événements privés, les dîners d'entreprise, Noël, la Saint-Valentin, les anniversaires avec des menus dégustation et des propositions de service dédié."
      }
    ],
    "ctaTitle": "Votre salle avec une technique professionnelle et une expérience mémorable.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Maître et Chef de Salle : Service, Accords Mets-Vins et Storytelling | AI Chef Pro",
      "description": "Suite d'IA pour maîtres professionnels : Manager Pro, Bar & Lounge AI+, Food Pairing AI, formation d'équipe et attraction premium. Commencez dès aujourd'hui.",
      "keywords": "IA maître, IA chef de salle, logiciel maître, fine dining salle, guéridon débouchage IA, formation équipe salle",
      "ogImage": "https://aichef.pro/og/use-cases/maitre-jefe-sala.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Salle dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes dans lequel vous décrivez le type de salle que vous dirigez (fine dining, restaurant de chef, gastronomique Michelin/Repsol, restaurant premium avec cave), la taille de l'équipe, la ville et la spécialité. Chaque agent répond en s'adaptant à votre salle et à votre exploitation réelle.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser en tant que Maître",
    "apps": [
      {
        "name": "Manager de Restaurant Pro",
        "category": "Gastro Profile Pro",
        "description": "Agent spécialisé adapté à la gestion de salle fine dining."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'Entreprise",
        "description": "Gestion de cave, débouchages, recommandations de vin et cocktails professionnels."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords mets-vins à base scientifique pour chaque plat du menu."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Storytelling et descriptions de plats pour l'équipe de salle."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Mise à l'échelle des recettes pour les événements privés et les dîners d'entreprise."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes à communiquer au client."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching pour le leadership d'équipe de salle et la gestion du stress aux heures de pointe du service."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie IA élégante de référence pour Instagram, le web et l'attraction premium."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec un calendrier éditorial élégant pour le fine dining."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients premium qui recherchent du fine dining sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Événements privés, dîners d'entreprise, Noël, Saint-Valentin, anniversaires."
      },
      {
        "name": "Repas du Personnel",
        "category": "Gastro Profile Pro",
        "description": "Générateur de menus du personnel avant le service."
      }
    ],
    "metrics": [
      {
        "value": "+20 %",
        "label": "ticket moyen fine dining"
      },
      {
        "value": "×1.4",
        "label": "taux de clients réguliers"
      },
      {
        "value": "×2",
        "label": "rapidité des propositions d'événements"
      },
      {
        "value": "12+",
        "label": "agents pour votre salle"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Briefing d'équipe improvisé, storytelling de plat sans rigueur",
        "Accords mets-vins recommandés sans base scientifique fondée",
        "Réservations premium sans planification des préférences et des allergies",
        "Événements privés conclus manuellement, proposition lente",
        "Instagram improvisé sans storytelling de service"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Briefing quotidien professionnel avec storytelling et accords mets-vins",
        "Accords mets-vins à base scientifique de Food Pairing AI",
        "Réservations premium avec planification professionnelle et attraction de clients réguliers",
        "Événements privés conclus en une journée avec proposition de service",
        "Instagram élégant avec GastroIMG Gen+ + InstaFlow AI Pro"
      ]
    },
    "galleryTitle": "Comment Fonctionne la Salle d'un Fine Dining",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : mise de table, débouchage, guéridon, service et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Sommelier",
    "heroSubtitle": "Concevez des cartes des vins avec une approche professionnelle, validez des accords sur une base scientifique, gérez la cave avec traçabilité et capturez un branding wine-driven avec une suite d'agents IA gastronomiques spécialisés en sommellerie professionnelle.",
    "heroTagline": "Cave avec une approche professionnelle et des accords scientifiques",
    "badge": "Pour sommeliers, chefs sommeliers et directeurs de cave",
    "painsTitle": "Ce qu'un Sommelier Ne Peut Pas Ignorer",
    "pains": [
      "Concevoir une carte des vins avec une approche professionnelle : équilibre des régions, cépages, prix, verres et verticales par cave",
      "Valider des accords sur une base scientifique pour chaque plat du menu dégustation et une carte changeante selon la saison",
      "Gérer la cave avec traçabilité : rotation, conditions de la cave, commandes, pertes dues à un débouchage raté",
      "Standardiser le storytelling de chaque vin pour que l'équipe de salle le communique avec professionnalisme au client",
      "Se différencier dans un restaurant concurrentiel avec une cave soignée, un débouchage professionnel et une expérience wine-driven",
      "Attirer des clients premium avec des dégustations, des événements de cave et des accords spéciaux à forte marge"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Sommelier",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Agent spécialisé en sommellerie professionnelle : cave, cépages, régions, technique de débouchage et service du vin."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Accords sur une base scientifique pour chaque plat et vin : analyse de l'acidité, des tanins, de la structure, de l'intensité et de l'harmonie."
      },
      {
        "icon": "BookOpen",
        "title": "Cuisine Créative + Storytelling",
        "description": "Storytelling de chaque vin pour l'équipe de salle : cave, terroir, cépage, vinification, notes de dégustation."
      },
      {
        "icon": "Calculator",
        "title": "Rendements de cave",
        "description": "Coût réel par verre, food cost du vin par service, pertes dues au débouchage et propositions de carte avec marge validée."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bodega",
        "description": "Modèles : contrôle de la cave (humidité, température), rotation, débouchage du jour, formation de l'équipe."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC cave",
        "description": "Traçabilité des vins, conservation, débouchage raté et températures de service par type."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Dégustations et événements de cave : accords avec menu dégustation, lancements, salons du vin, Noël, événements privés."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie wine-driven IA de référence + Instagram avec storytelling de cave pour attirer des clients premium."
      },
      {
        "icon": "BarChart3",
        "title": "Rendement GenCal",
        "description": "Données précises sur les pertes en débouchage raté, verre cassé et vin à table."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Sommelier avec AI Chef Pro",
    "workflow": [
      "11:00 · Ouverture — checklist Kit de Tareas Bodega : contrôle de la cave (12-14 °C, 70 % d'humidité), vérification des commandes, rotation des vins du jour.",
      "12:00 · Bar & Lounge AI+ — vous mettez à jour la carte avec deux nouvelles références (Bourgogne rouge et Riesling allemand). Recette + storytelling généré.",
      "13:00 · Food Pairing AI — vous validez l'accord du nouveau Riesling avec un plat de poisson fermenté du menu dégustation. Analyse de l'acidité et de l'harmonie.",
      "14:00 · Kit de Escandallos Pro — vous calculez le rendement des deux nouvelles références avec une marge réelle par verre et par bouteille, vous validez le prix suggéré.",
      "15:00 · Briefing à l'équipe — explication des deux nouvelles références avec storytelling et accords validés.",
      "17:00 · Dégustation privée pour client VIP — sélection de cinq vins avec accords ad hoc, débouchage professionnel, décantation si nécessaire.",
      "20:00 · Service du dîner — coordination avec le maître d'hôtel et la cuisine, recommandations par table, guéridon si nécessaire.",
      "23:00 · Clôture — mise à jour du stock, GastroIMG Gen+ génère une image de référence du nouveau Bourgogne + InstaFlow programme le post."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Sommelier",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "pro-prompts-ebook",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Bar & Lounge AI+ + Food Pairing AI ont changé ma proposition. Chaque accord du menu dégustation a maintenant une base scientifique documentée que l'équipe de salle communique au client avec professionnalisme. La gestion de cave avec le rendement par verre a augmenté notre marge sur les vins de 6 points. Les dégustations privées pour VIP se concluent en un appel avec une proposition professionnelle.",
    "testimonialAuthor": "Eduardo Lara",
    "testimonialRole": "Chef Sommelier, restaurant 1 étoile Michelin",
    "faqTitle": "Questions Fréquentes des Sommeliers",
    "faqs": [
      {
        "q": "Est-ce adapté pour un sommelier de fine dining, un restaurant gastronomique, une cave à vin ou un hôtel ?",
        "a": "Pour les quatre. Bar & Lounge AI+ couvre du sommelier de restaurant premium au chef sommelier de restaurant gastronomique Michelin, en passant par la cave à vin avec une cave soignée ou l'hôtel avec multi-outlet."
      },
      {
        "q": "Comment m'aide-t-il avec les accords scientifiques ?",
        "a": "Food Pairing AI raisonne sur une base scientifique : analyse de l'acidité, des tanins, de la structure, de l'intensité, de l'harmonie et du contraste. Il fonde chaque accord pour que l'équipe de salle le communique avec professionnalisme."
      },
      {
        "q": "Comment gérer le rendement et la marge par verre ?",
        "a": "Kit de Escandallos Pro recalcule la marge par verre et par bouteille lorsque vous mettez à jour les prix de la cave. Rendement GenCal ajoute le coût du débouchage raté et les pertes en service."
      },
      {
        "q": "Génère-t-il du contenu visuel wine-driven pour Instagram ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles de verres, de décantation et de cave pour Instagram, le web et l'attraction de clients premium. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre vrai verre."
      },
      {
        "q": "Comment m'aide-t-il avec les dégustations privées et les événements de cave ?",
        "a": "Gastro Calendar planifie des dégustations privées, des événements de cave, des salons du vin, des lancements saisonniers et des accords avec des menus dégustation."
      }
    ],
    "ctaTitle": "Votre cave avec une approche professionnelle et des accords scientifiques.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10.000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Sommelier : Cave, Accords et Dégustations Professionnels | AI Chef Pro",
      "description": "Suite d'IA pour sommeliers professionnels : Bar & Lounge AI+, Food Pairing AI, calcul de rendement par verre, dégustations privées et branding wine-driven. Commencez aujourd'hui.",
      "keywords": "IA sommelier, logiciel sommelier, accords IA, gestion de cave IA, calcul de rendement vin, chef sommelier, dégustation privée IA",
      "ogImage": "https://aichef.pro/og/use-cases/sommelier.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Cave dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes dans lequel vous lui racontez quel type de sommelier vous êtes (chef sommelier de fine dining, sommelier freelance, directeur de cave à vin, sommelier d'hôtel, formateur), la taille de la cave, la ville et la spécialité. Chaque agent répond adapté à votre cave et à votre opération réelle.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser en tant que Sommelier",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'Entreprise",
        "description": "Agent spécialisé en sommellerie professionnelle : cave, cépages, régions, technique."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords sur une base scientifique : acidité, tanins, structure, intensité et harmonie."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Storytelling de chaque vin : terroir, vinification, notes de dégustation pour l'équipe de salle."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes en débouchage raté, verre cassé et vin à table intégrées dans le rendement."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification des sulfites dans les vins pour les clients sensibles."
      },
      {
        "name": "Gastro Lexicum",
        "category": "Gastro Connaissance",
        "description": "Tuteur de définitions techniques : œnologie, vinification, terroir, appellations."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie wine-driven IA de référence pour Instagram, web et événements."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial wine-driven pour attirer des clients premium."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer des clients qui recherchent une cave à vin, une dégustation ou un sommelier sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Dégustations privées, salons du vin, lancements, Noël, événements de cave."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles SEO sur les accords, les cépages et les caves pour attirer du trafic organique."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche approfondie sur les caves émergentes, les terroirs, les millésimes et les tendances."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge après calcul des rendements de la cave"
      },
      {
        "value": "×2",
        "label": "vitesse des propositions de dégustation"
      },
      {
        "value": "×3",
        "label": "engagement Instagram wine-driven"
      },
      {
        "value": "12+",
        "label": "agents pour votre cave"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Accords recommandés sans base scientifique documentée",
        "Carte des vins sans calcul de rendement par verre ni marge réelle",
        "Cave gérée sur des feuilles, sans traçabilité ni rotation claire",
        "Storytelling de vin improvisé, équipe de salle sans formation constante",
        "Dégustations privées conclues à la main, proposition lente"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Accords sur une base scientifique de Food Pairing AI",
        "Calcul de rendement par verre avec marge validée en temps réel",
        "Cave avec traçabilité APPCC et rotation documentée",
        "Briefing quotidien à l'équipe avec storytelling et accords",
        "Dégustations privées conclues en un jour avec une proposition wine-driven"
      ]
    },
    "galleryTitle": "Comment Fonctionne la Cave d'un Sommelier",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : cave, décantation, verre, dégustation et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Maître Grillardin et Parrillero",
    "heroSubtitle": "Maîtrisez la technique des braises, la découpe et le dry-aged avec un calcul de revient professionnel par coupe, planifiez la production de protéines et capturez un branding fire-driven avec une suite d'agents IA gastronomiques spécialisés en cuisine au feu professionnelle.",
    "heroTagline": "Braises avec une technique authentique et une marge réelle",
    "badge": "Pour maîtres grillardins, parrilleros et grillmasters",
    "painsTitle": "Ce Qu'un Maître Grillardin Ne Peut Pas Arrêter de Résoudre",
    "pains": [
      "Standardiser le point de cuisson et la technique des braises tour après tour (charbon de bois, bois, persillage, température interne)",
      "Découpe rigoureuse avec coût au kilo et rendement par coupe (entrecôte, picanha, T-bone, filet)",
      "Gestion du dry-aged avec chambre, humidité, température, rotation et perte hebdomadaire documentée",
      "Coordonner le grill avec la cuisine principale aux pics de service sans perdre en qualité ni en timing",
      "Storytelling des fournisseurs d'élevage, de la race, de l'alimentation et de l'affinage pour la salle",
      "Former une équipe de grillardins juniors avec un critère technique et une constance dans le point de cuisson"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Maître Grillardin",
    "features": [
      {
        "icon": "Flame",
        "title": "Cuisine Créative",
        "description": "Pour le développement technique de coupes signature, marinades, sauces et accompagnements de grill."
      },
      {
        "icon": "UtensilsCrossed",
        "title": "Cuisine Argentine + Brésilienne",
        "description": "Recueils de recettes spécialisés : grill, chimichurri, picanha, churrasco, technique authentique."
      },
      {
        "icon": "Calculator",
        "title": "Calculs de revient par coupe avec dry-aged",
        "description": "Recette + calcul de revient CSV avec perte de dry-aged intégrée et coût horaire du grill. Marge réelle par coupe."
      },
      {
        "icon": "BarChart3",
        "title": "Rendement GenCal",
        "description": "Données par processus : découpe, dry-aging hebdomadaire, parage, perte de cuisson."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles : allumage des braises, découpe, contrôle de la chambre dry-aged, mise en place, fermeture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC grillardin",
        "description": "Traçabilité de la viande, dry-aging, température interne et conservation."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Accords avec des rouges puissants pour les nouvelles coupes signature."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Fête des Pères, Noël, événements d'entreprise et lancements par saison."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie premium IA de référence + Instagram avec storytelling du fournisseur d'élevage."
      }
    ],
    "workflowTitle": "Une Journée Réelle de Maître Grillardin avec AI Chef Pro",
    "workflow": [
      "09:00 · Ouverture — checklist Kit de Tareas : allumage contrôlé des braises (3 heures pour atteindre le point), contrôle de la chambre dry-aged.",
      "11:00 · Cuisine Créative + Cuisine Argentine — vous développez une nouvelle coupe signature d'entrecôte galicienne dry-aged 60 jours avec sel de Maldon fumé et chimichurri. Recette + calcul de revient CSV.",
      "12:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos vrais prix de viande et la perte du dry-aged, vous validez la marge réelle par coupe.",
      "13:00 · Service de midi — grill à plein régime avec coupes premium, mise en place de chimichurri et accompagnements.",
      "17:00 · Briefing à l'équipe — formation des grillardins juniors avec un critère technique de point de cuisson.",
      "20:00 · Service du soir — pics coordonnés, grill avec plusieurs coupes simultanées.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence de la nouvelle entrecôte et les posts pour Instagram.",
      "00:00 · Fermeture — nettoyage en profondeur des grilles, APPCC signé, contrôle de la chambre dry-aged."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Maître Grillardin",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cuisine Argentine + Cuisine Créative ont élevé mon niveau. Mon équipe reproduit désormais le point de cuisson avec un critère technique documenté, les calculs de revient des coupes premium reflètent la perte du dry-aged et nous avons augmenté la marge de 5 points. La planification de la Fête des Pères avec Gastro Calendar a triplé notre chiffre d'affaires.",
    "testimonialAuthor": "Pedro Aguirre",
    "testimonialRole": "Maître grillardin, grill premium avec dry-aged",
    "faqTitle": "Questions Fréquentes de Maîtres Grillardins",
    "faqs": [
      {
        "q": "Est-ce que ça fonctionne pour un grill argentin, une churrascaria, un grill premium ou un steakhouse ?",
        "a": "Pour les quatre. Cuisine Argentine + Cuisine Brésilienne + Cuisine Créative couvrent du grill traditionnel au steakhouse avec dry-aged."
      },
      {
        "q": "Est-ce que ça couvre le dry-aged et la gestion de la chambre ?",
        "a": "Oui. Il raisonne comme un maître grillardin professionnel : conditions de chambre, temps par coupe, contrôle de la perte hebdomadaire et rotation."
      },
      {
        "q": "Comment gérez-vous le coût volatil de la viande ?",
        "a": "Kit de Escandallos Pro recalcule la marge instantanément. Rendement GenCal ajoute le coût des pertes de dry-aging, de découpe et de parage."
      },
      {
        "q": "Est-ce que ça génère du contenu visuel pour Instagram ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles des coupes et des braises. Rappelez-vous que l'image IA est une référence visuelle : la photo finale, c'est vous qui la faites avec votre vraie coupe."
      },
      {
        "q": "Comment est-ce que ça m'aide avec les événements d'entreprise ?",
        "a": "Gastro Calendar planifie la Fête des Pères, Noël, les événements d'entreprise et les lancements de coupes par saison."
      }
    ],
    "ctaTitle": "Votre grill avec une technique de feu et une marge réelle.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Forfait Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Maître Grillardin et Parrillero : Coupes, Braises et Dry-Aged | AI Chef Pro",
      "description": "Suite IA pour maîtres grillardins : Cuisine Argentine + Brésilienne, calculs de revient par coupe, dry-aged, branding et APPCC. Commencez aujourd'hui.",
      "keywords": "IA maître grillardin, IA parrillero, logiciel grillardin, calculs de revient entrecôte, dry-aged, technique des braises, grill argentin IA",
      "ogImage": "https://aichef.pro/og/use-cases/maestro-asador-parrillero.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Grill dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding de 2 minutes où vous nous dites quel type de grill vous dirigez (grill argentin, churrascaria brésilienne, steakhouse premium avec dry-aged, grill casual de quartier), la taille de l'équipe, la ville et la spécialité. Chaque agent répond adapté à votre grill et à votre opération réelle.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser en Tant que Maître Grillardin",
    "apps": [
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de coupes signature avec technique de braises et accompagnements."
      },
      {
        "name": "Cuisine Argentine",
        "category": "Recueils de recettes d'Amérique latine",
        "description": "Asado, chimichurri, ris de veau et technique de grill authentique."
      },
      {
        "name": "Cuisine Brésilienne",
        "category": "Recueils de recettes d'Amérique latine",
        "description": "Picanha, churrasco, farofa et technique de churrascaria."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords avec des rouges puissants et une mixologie de caractère."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'Entreprise",
        "description": "Pour le bar du grill avec des vins rouges premium."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes en découpe, dry-aging, parage et cuisson."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique par coupe et accompagnement."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissances Gastro",
        "description": "Photographie premium IA de référence pour Instagram, le site web et la carte."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec un calendrier éditorial fire-driven."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer des clients qui cherchent \"grill près de chez moi\" sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Fête des Pères, Noël, événements d'entreprise."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching pour le leadership d'équipe et les pics de service."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "de marge après avoir calculé les coupes"
      },
      {
        "value": "×3",
        "label": "de chiffre d'affaires à la Fête des Pères"
      },
      {
        "value": "−15 %",
        "label": "de pertes en découpe et dry-aging"
      },
      {
        "value": "12+",
        "label": "agents pour votre grill"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Point de cuisson improvisé entre grillardins",
        "Calculs de revient sans perte du dry-aged",
        "Chambre dry-aged sans traçabilité",
        "Briefing improvisé, formation variable",
        "Instagram sans storytelling du fournisseur d'élevage"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Point de cuisson constant avec un critère technique",
        "Calcul de revient professionnel avec perte de dry-aged intégrée",
        "Chambre avec traçabilité APPCC documentée",
        "Briefing quotidien professionnel, formation constante",
        "GastroIMG Gen+ + storytelling du fournisseur d'élevage"
      ]
    },
    "galleryTitle": "Comment Fonctionne le Grill d'un Maître Grillardin",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : braises, découpe, coupes, chimichurri et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Maître Glacier et Gelatiere",
    "heroSubtitle": "Maîtrisez l'équilibre technique des bases, le calcul de coût par saveur avec coût réel, planifiez la production saisonnière et capturez une image de marque artisanale avec une suite d'agents IA gastronomiques spécialisés en glacerie professionnelle.",
    "heroTagline": "Glace avec une technique authentique et une marge réelle",
    "badge": "Pour maîtres glaciers, gelatieri et artisans de la glace",
    "painsTitle": "Ce qu'un Maître Glacier ne peut pas manquer de résoudre",
    "pains": [
      "Équilibre technique exigeant : équilibre des sucres (saccharose, dextrose, sucre inverti), solides totaux et matières grasses pour une texture optimale",
      "Pertes à la turbine, au refroidissement et en vitrine avec un produit sensible à la température",
      "Saisonnalité extrême : haute saison en été, creux hivernal à rentabiliser avec des tartes glacées et des semifreddos",
      "Standardiser la production des bases (blanche, jaune, fruit, sorbet) équipe après équipe avec un critère technique",
      "Se différencier dans une zone concurrentielle avec des saveurs propres, des ingrédients premium (Sosa, Pistache de Bronte) et une image de marque visuelle",
      "Former l'équipe à la technique professionnelle d'équilibre et de cristallisation"
    ],
    "featuresTitle": "Comment AI Chef Pro aide un Maître Glacier",
    "features": [
      {
        "icon": "IceCream",
        "title": "Glacerie Créative",
        "description": "Agent spécialisé en glacerie artisanale professionnelle : bases blanche, jaune, fruit, sorbets, équilibrage technique des sucres."
      },
      {
        "icon": "Cake",
        "title": "Pâtisserie Créative",
        "description": "Pour tartes glacées, semifreddos, desserts à la cuillère qui rentabilisent le creux hivernal."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour le développement de saveurs signature, des fusions contrôlées et des présentations d'auteur."
      },
      {
        "icon": "Calculator",
        "title": "Calculs de coût par saveur",
        "description": "Glacerie Créative fournit recette + calcul de coût CSV avec équilibre technique ; Kit de Escandallos Pro le gère avec une marge réelle par kg, par boule et par cornet."
      },
      {
        "icon": "Beaker",
        "title": "Agent Sosa Ingredients",
        "description": "Catalogue Sosa pour textures professionnelles, stabilisants, épaississants et pâtes concentrées."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Heladería",
        "description": "Modèles : préparation turbine, refroidissement, réapprovisionnement vitrine, contrôle des températures, rotation."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Glacerie",
        "description": "Traçabilité du lait, des fruits frais, des fruits secs et des températures critiques."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Fête des Mères, printemps, été, Saint-Valentin, tartes glacées de Noël."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie artisanale IA de référence + Instagram pour attirer les clients locaux."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Maître Glacier avec AI Chef Pro",
    "workflow": [
      "07:00 · Ouverture — checklist Kit de Tareas : vérification de la chambre froide, refroidissement des mélanges préparés la veille.",
      "08:30 · Glacerie Créative — vous développez une nouvelle saveur signature de pistache de Bronte avec sel Maldon. Cuisine Créative fournit recette + calcul de coût CSV.",
      "09:30 · Agent Sosa Ingredients — vous sélectionnez la pâte concentrée et le stabilisant adaptés.",
      "10:00 · Kit de Escandallos Pro — vous chargez un CSV avec vos prix réels de pistache premium et de lait, vous validez la marge par boule et par kg.",
      "11:00 · Production du jour — vous passez les mélanges à la turbine, vous abattez à -18 °C.",
      "13:30 · Réapprovisionnement de la vitrine avec étiquettes et contrôle des pertes d'exposition.",
      "16:00 · Pâtisserie Créative — vous développez une tarte glacée pour la Fête des Mères avec un semifreddo à la pistache.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez une image de référence de la nouvelle saveur + publications."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Maître Glacier",
    "productIds": [
      "kit-tareas-heladeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Glacerie Créative a transformé notre cuisine. Nous équilibrons sucres et solides avec un critère technique, les calculs de coût par boule avec pistache premium reflètent une marge réelle. Pâtisserie Créative nous a ouvert les tartes glacées qui rentabilisent l'hiver. Nous avons gagné 5 points.",
    "testimonialAuthor": "Federico Riva",
    "testimonialRole": "Maître gelatiere, gelateria artisanale premium",
    "faqTitle": "Questions Fréquentes des Maîtres Glaciers",
    "faqs": [
      {
        "q": "Est-ce que cela convient à une gelateria italienne, une glacerie artisanale ou une chaîne avec plusieurs points de vente ?",
        "a": "Pour les trois. Glacerie Créative raisonne comme un maître glacier professionnel avec un équilibre technique documenté."
      },
      {
        "q": "Couvre-t-il l'équilibre des sucres, des solides et des matières grasses ?",
        "a": "Oui. Glacerie Créative raisonne comme un glacier professionnel : équilibre avec saccharose, dextrose, sucre inverti, solides totaux et matières grasses selon la norme technique."
      },
      {
        "q": "Comment m'aide-t-il avec la saisonnalité ?",
        "a": "Pâtisserie Créative ouvre des tartes glacées et des semifreddos pour le creux hivernal ; Gastro Calendar planifie les pics (Fête des Mères, été)."
      },
      {
        "q": "Génère-t-il du contenu visuel pour Instagram ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence pour la vitrine et les réseaux. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre bac et votre dressage réel."
      },
      {
        "q": "Comment gérer les pertes à la turbine et en vitrine ?",
        "a": "Rendement GenCal fournit des données par processus (turbine, refroidissement, exposition). Elles s'intègrent au calcul de coût du Kit de Escandallos Pro."
      }
    ],
    "ctaTitle": "Votre glace avec une technique authentique et une marge réelle.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "IA pour Maître Glacier et Gelatiere : Bases, Calculs de Coût et Saisonnalité | AI Chef Pro",
      "description": "Suite IA pour maîtres glaciers : Glacerie Créative, équilibre technique, calculs de coût par saveur, image de marque et APPCC. Commencez dès aujourd'hui.",
      "keywords": "IA maître glacier, IA gelatiere, logiciel glacerie, calculs de coût glace, équilibre technique glace, turbine IA",
      "ogImage": "https://aichef.pro/og/use-cases/maestro-heladero.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Glacerie dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding de 2 minutes dans lequel vous lui racontez quel type de glacerie vous exploitez (gelateria italienne, glacerie artisanale espagnole, glacerie avec atelier), la taille de l'équipe, la ville et la spécialité.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser en tant que Maître Glacier",
    "apps": [
      {
        "name": "Glacerie Créative",
        "category": "Créativité Culinaire",
        "description": "Agent spécialisé en glacerie artisanale avec équilibre technique."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Tartes glacées, semifreddos, desserts à la cuillère pour le creux hivernal."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de saveurs signature avec recette + calcul de coût CSV."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Stabilisants, épaississants, pâtes concentrées et textures professionnelles."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes à la turbine, au refroidissement et en vitrine."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique par saveur : produits laitiers, fruits à coque, gluten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie artisanale IA de référence pour vitrine, web et réseaux."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial pour glacerie d'auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients qui recherchent \"glacerie près de moi\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Fête des Mères, été, Saint-Valentin, tartes glacées de Noël."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capture du trafic organique pour les tartes glacées."
      },
      {
        "name": "Repas du Personnel",
        "category": "Profil Gastro Pro",
        "description": "Générateur de menus du personnel pour l'atelier."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge après calcul des coûts par saveur"
      },
      {
        "value": "−40 %",
        "label": "pertes en atelier et en vitrine"
      },
      {
        "value": "×3",
        "label": "engagement Instagram"
      },
      {
        "value": "12+",
        "label": "agents pour votre atelier"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Bases improvisées, équilibre incohérent d'une équipe à l'autre",
        "Calculs de coût sans équilibre technique documenté",
        "Pertes sans traçabilité par processus",
        "Saisonnalité réactive en creux hivernal",
        "Vitrine et réseaux sociaux improvisés"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Bases avec équilibre technique documenté",
        "Calculs de coût professionnels par boule et par kg",
        "Pertes contrôlées avec Rendement GenCal",
        "Tartes glacées et semifreddos rentabilisent l'hiver",
        "GastroIMG Gen+ + InstaFlow + Pinterest Pins Gen"
      ]
    },
    "galleryTitle": "Comment Fonctionne l'Atelier d'un Maître Glacier",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : turbine, bases, spatule, fruits et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Pâtissier et Confiseur",
    "heroSubtitle": "Maîtrisez la technique de pâtisserie professionnelle, la fiche technique par pièce avec coût horaire atelier, planifiez la production saisonnière et capturez un branding artisanal avec une suite d'agents IA gastronomiques spécialisés en pâtisserie et en desserts d'auteur.",
    "heroTagline": "Pâtisserie avec technique authentique et marge réelle",
    "badge": "Pour pâtissiers, pâtissiers-confiseurs et chefs pâtissiers",
    "painsTitle": "Ce Qu'un Pâtissier Ne Peut Pas Laisser de Côté",
    "pains": [
      "Technique avancée exigeante : feuilletage, pâtes brisée et sablée, biscuits, ganaches, glaçages, mousses avec équilibre précis",
      "Pertes élevées en atelier (façonnage, cuisson, décoration) qui saignent la rentabilité sans contrôle",
      "Standardiser les pièces signature d'équipe en équipe avec une constance professionnelle",
      "Saisonnalité très forte : Galette des Rois, Pâques, Saint-Valentin, Noël concentrent un fort pourcentage de l'année",
      "Se différencier avec une pâtisserie d'auteur, une présentation premium et un storytelling de technique française ou moderne",
      "Capturer les commandes de gâteaux sur mesure, événements privés et mariages avec marge tout en gérant la pâtisserie quotidienne"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Pâtissier",
    "features": [
      {
        "icon": "Cake",
        "title": "Pâtisserie Créative",
        "description": "Agent spécialisé en pâtisserie professionnelle, desserts de restaurant, gâteaux sur mesure et viennoiserie avec technique avancée."
      },
      {
        "icon": "Cookie",
        "title": "Chocolaterie Créative",
        "description": "Pour les combinaisons avancées pâtisserie + chocolat : ganaches, crémeux, glaçages."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour le développement de desserts signature et les combinaisons de saveurs avec critère technique."
      },
      {
        "icon": "Calculator",
        "title": "Fiches techniques avec coût horaire atelier",
        "description": "Pâtisserie Créative fournit recette + fiche technique CSV ; Kit de Escandallos Pro la gère avec coût horaire atelier intégré dans la marge réelle par pièce."
      },
      {
        "icon": "Beaker",
        "title": "Agent Sosa Ingredients",
        "description": "Catalogue Sosa pour textures, gélifiants, neutres et technique avancée."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pastelería",
        "description": "Modèles : préparation des pâtes, production, façonnage, cuisson, décoration, vitrine, conservation."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC pâtisserie",
        "description": "Traçabilité des œufs, crèmes, fruits secs et conservation professionnelle."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Galette des Rois, Saint-Valentin, Pâques, Noël, communions, Fête des Mères."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Photographie artisanale IA de référence + Pinterest, où la pâtisserie capte un trafic organique stable."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Pâtissier avec AI Chef Pro",
    "workflow": [
      "06:00 · Ouverture — checklist Kit de Tareas Pastelería : rafraîchissement du levain, battage des gâteaux, préparation des crèmes.",
      "08:00 · Pâtisserie Créative — vous développez un nouveau dessert pour la Saint-Valentin. Cuisine Créative fournit recette + fiche technique CSV.",
      "09:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels et coût horaire atelier, vous validez la marge par pièce.",
      "11:00 · Production du jour — façonnage, cuisson, décoration avec des modèles spécifiques.",
      "14:00 · Réapprovisionnement de la vitrine avec étiquettes et prix.",
      "16:00 · Gastro Calendar — vous préparez la planification de la Galette des Rois avec 8 semaines d'avance.",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — vous générez l'image de référence du nouveau dessert + des épingles.",
      "20:00 · Fermeture — nettoyage en profondeur, APPCC signé, planification du lendemain."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Pâtissier",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Pâtisserie Créative + Agent Sosa Ingredients ont transformé mon offre. Mes desserts signature ont désormais une technique documentée que mon équipe reproduit avec constance, les fiches techniques avec coût horaire atelier m'ont apporté 6 points de marge en plus, et les commandes de gâteaux sur mesure se concluent en un appel avec une proposition professionnelle.",
    "testimonialAuthor": "Eva Mata",
    "testimonialRole": "Chef pâtissière, pâtisserie d'auteur",
    "faqTitle": "Questions Fréquentes des Pâtissiers",
    "faqs": [
      {
        "q": "Est-ce adapté pour un pâtissier de restaurant, un pâtissier artisanal ou un chef pâtissier d'hôtel ?",
        "a": "Pour les trois. Pâtisserie Créative couvre de la pâtisserie artisanale à la haute pâtisserie de restaurant avec technique française avancée."
      },
      {
        "q": "Couvre-t-elle la technique avancée (feuilletage, mousses, glaçages) ?",
        "a": "Oui. Pâtisserie Créative raisonne comme un chef pâtissier professionnel : feuilletage inversé, pâtes travaillées avec technique, mousses avec équilibre, glaçages avec couverture technique."
      },
      {
        "q": "Couvre-t-elle la pâtisserie + la chocolaterie ?",
        "a": "Oui. Chocolaterie Créative complète avec bonbons, ganaches, pralinés et technique de tempérage pour les pièces combinées."
      },
      {
        "q": "Génère-t-elle du contenu visuel pour la vitrine et les réseaux ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles ; Pinterest Pins Gen capte un trafic organique stable. Rappelez-vous que l'image IA est une référence visuelle : la photo finale, c'est vous qui la faites avec votre pièce réelle."
      },
      {
        "q": "Comment m'aide-t-elle pour les événements et les saisons ?",
        "a": "Gastro Calendar planifie les saisons clés (Galette des Rois, Saint-Valentin, Pâques, Noël, communions) à l'avance."
      }
    ],
    "ctaTitle": "Votre pâtisserie avec technique d'auteur et marge réelle.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "IA pour Pâtissier et Confiseur : Technique, Fiches Techniques et Saisonnalité | AI Chef Pro",
      "description": "Suite IA pour pâtissiers professionnels : Pâtisserie Créative, fiches techniques avec coût horaire atelier, planification saisonnière et branding. Commencez aujourd'hui.",
      "keywords": "IA pâtissier, IA confiseur, IA chef pâtissier, logiciel pâtisserie, fiches techniques pâtisserie, technique française, pâtisserie d'auteur",
      "ogImage": "https://aichef.pro/og/use-cases/repostero-pastelero.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Pâtisserie dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding de 2 minutes où vous décrivez votre type de pâtisserie (chef pâtissier de restaurant, pâtissier artisanal, pâtissier d'hôtel, pâtisserie pour événements), la taille de l'équipe, la ville et la spécialité.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser comme Pâtissier",
    "apps": [
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Agent spécialisé en pâtisserie professionnelle avec technique avancée."
      },
      {
        "name": "Chocolaterie Créative",
        "category": "Créativité Culinaire",
        "description": "Pour bonbons, ganaches et combinaisons avancées."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de desserts signature avec recette + fiche technique CSV."
      },
      {
        "name": "Boulangerie Créative",
        "category": "Créativité Culinaire",
        "description": "Pour brioche, croissants, ensaïmadas et viennoiserie complémentaire."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour textures, gélifiants et technique avancée."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue tSpoonLab pour applications avancées."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes en atelier, façonnage, cuisson et vitrine."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique par pièce : gluten, produits laitiers, fruits secs, œuf."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie artisanale IA de référence pour vitrine, web et réseaux."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial pour pâtisserie d'auteur."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capte un trafic organique stable pour gâteaux et desserts."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Galette des Rois, Saint-Valentin, Pâques, Noël, Fête des Mères."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge après fiches techniques des pièces"
      },
      {
        "value": "−30 %",
        "label": "pertes atelier"
      },
      {
        "value": "×2",
        "label": "trafic organique via Pinterest"
      },
      {
        "value": "12+",
        "label": "agents pour votre atelier"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Technique improvisée, desserts signature incohérents",
        "Fiches techniques sans coût horaire atelier",
        "Pertes en atelier sans traçabilité réelle",
        "Vitrine et réseaux improvisés avec photos du téléphone",
        "Saisonnalité réactive, vous arrivez en retard pour la Galette des Rois"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Technique documentée, desserts signature cohérents",
        "Fiche technique professionnelle avec coût horaire atelier intégré",
        "Pertes contrôlées avec Rendement GenCal",
        "GastroIMG Gen+ + Pinterest Pins Gen captent un trafic stable",
        "Galette des Rois et saisons planifiées avec 8 semaines d'avance"
      ]
    },
    "galleryTitle": "Comment Fonctionne l'Atelier d'un Pâtissier",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : pochage, gâteaux, mise en place, vitrine et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Restaurant Décontracté",
    "heroSubtitle": "Optimisez l'opération quotidienne, contrôlez le food cost et récupérez des heures de paperasse dans votre restaurant décontracté avec une suite d'agents IA spécialisés en restauration.",
    "heroTagline": "Le restaurant décontracté moderne a besoin d'IA",
    "badge": "Pour restaurants décontractés et bistrots",
    "painsTitle": "Les défis incontournables d'un Restaurant Décontracté",
    "pains": [
      "Marge étroite exigeant un contrôle millimétrique des coûts et des pertes en cuisine",
      "Turnover élevé de l'équipe : former et superviser de nouveaux cuisiniers et serveurs consomme des heures chaque semaine",
      "Carte étendue avec de nombreux plats à calculer lorsque les prix des fournisseurs changent",
      "HACCP et réglementation toujours à jour sans que la paperasse ne vole du temps à la salle",
      "Attirer des clients dans une zone concurrentielle : SEO local, réseaux sociaux et avis sont essentiels",
      "Coordonner cuisine, salle et livraison aux heures de pointe sans accrocs"
    ],
    "featuresTitle": "Comment AI Chef Pro aide un restaurant décontracté",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Restaurants Décontractés AI+",
        "description": "Agent spécialisé dans les bistrots, gastrobars, tapas et méditerranéen : le spectre décontracté complet avec une base professionnelle."
      },
      {
        "icon": "Calculator",
        "title": "Calculs de coûts professionnels",
        "description": "Cuisine Créative fournit recette + calcul CSV ; Kit de Escandallos Pro le gère avec vos prix réels et marge cible."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles prêts : ouverture, fermeture, postes de cuisine, salle, livraison et événements."
      },
      {
        "icon": "ShieldCheck",
        "title": "HACCP et traçabilité",
        "description": "Pack APPCC avec 19 registres, enregistrements depuis le mobile, alertes et feuilles prêtes à imprimer en A4 pour l'inspection."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Plannings en minutes respectant la convention collective, pauses, contrôle des heures et ratios de productivité."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Suite SEO local pour attirer des clients organiquement sans payer d'agence."
      },
      {
        "icon": "BarChart3",
        "title": "Kit Plan Financiero",
        "description": "Tableau de bord des ratios, food cost, productivité et ticket moyen. Reporting au propriétaire en PDF."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie gastronomique IA pour le web et les réseaux, contenu pour Instagram avec calendrier éditorial."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Recherche de mots-clés gastronomiques locaux par zone postale pour un positionnement réel."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Restaurant Décontracté avec AI Chef Pro",
    "workflow": [
      "08:30 · Ouverture — checklist du Kit de Tareas Restaurante Casual et contrôle d'inventaire en 10 minutes.",
      "10:00 · Restaurants Décontractés AI+ — vous demandez à l'agent des suggestions de plat du jour avec le produit que vous avez en chambre froide.",
      "10:30 · Cuisine Créative + Kit de Escandallos Pro — vous calculez le plat du jour avec vos prix et validez la marge.",
      "12:30 · Service de midi — cuisine, salle et livraison coordonnés avec des modèles. Pertes enregistrées depuis le mobile avec HACCP.",
      "15:30 · Kit Plan Financiero — vous révisez les KPIs de la veille et détectez que le food cost du lundi a augmenté à 32 %, vous identifiez la cause.",
      "17:00 · MenuDish Local SEO — vous mettez à jour les descriptions des 6 plats top sur Google Business et le web.",
      "18:00 · Kit Inventario — vous validez les commandes aux fournisseurs avec comparaison des prix et alertes de stock minimum.",
      "23:30 · Fermeture — HACCP signé, rapport quotidien au propriétaire en PDF directement depuis le Kit Plan Financiero."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Restaurant Décontracté",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Nous avons 80 couverts et un fort turnover du personnel. Le Kit de Tareas Restaurante Casual et le Pack APPCC ont structuré toute notre opération. Nous fonctionnons comme une horloge suisse et le food cost a baissé de 3 points au premier trimestre simplement grâce à un bon calcul des coûts.",
    "testimonialAuthor": "Sandra López",
    "testimonialRole": "Gérant, restaurant décontracté méditerranéen de 80 couverts",
    "faqTitle": "Questions Fréquentes sur les Restaurants Décontractés",
    "faqs": [
      {
        "q": "Est-ce que ça fonctionne pour des restaurants de 30, 80 ou 150 couverts ?",
        "a": "Oui. Les modèles s'adaptent au volume et les plans s'ajustent à l'utilisation réelle. Nous avons des clients de 30 couverts jusqu'à des chaînes de 25 établissements."
      },
      {
        "q": "Couvre-t-il la livraison en plus de la salle ?",
        "a": "Oui. Le Kit de Tareas Restaurante Casual inclut des modèles spécifiques pour la gestion de la livraison, les pertes associées et la coordination avec des plateformes comme Glovo, Uber Eats et Just Eat."
      },
      {
        "q": "Remplace-t-il mon logiciel de caisse ou de réservation ?",
        "a": "Non, il complète. Cover Manager ou The Fork gèrent les réservations et le logiciel de caisse gère les ventes ; AI Chef Pro gère les coûts, le personnel, l'HACCP, l'inventaire et le SEO local. Les données sont compatibles via Excel."
      },
      {
        "q": "Combien de temps l'équipe met-elle pour l'apprendre ?",
        "a": "Courbe d'apprentissage réelle de 1 à 2 jours. Il y a une vidéo d'onboarding de 5 minutes, un support par WhatsApp et tout démarre avec l'agent « Qui suis-je ? » qui adapte le système à votre restaurant en 2 minutes."
      },
      {
        "q": "Comment m'aide-t-il avec le SEO local et l'acquisition ?",
        "a": "Suite Contenus et Réseaux Sociaux : MenuDish Local SEO (descriptions de plats), BlogPost SEO Gen+ (articles de blog), Keyword Discovery AI+ (mots-clés par zone postale), InstaFlow AI Pro (Instagram) et Pinterest Pins Gen."
      },
      {
        "q": "Y a-t-il un agent spécifique pour mon type de restaurant décontracté ?",
        "a": "Oui. Restaurants Décontractés AI+ couvre les bistrots, gastrobars, tapas, méditerranéen, auberges, grill décontracté. Pour des concepts plus spécifiques, il y a Burger Pro AI+, Food Truck AI+ et des agents par pays (mexicaine, péruvienne, japonaise, etc.)."
      }
    ],
    "ctaTitle": "Mettez de l'ordre dans votre restaurant décontracté.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Restaurant Décontracté : Opération, Calculs de Coûts et SEO Local | AI Chef Pro",
      "description": "Suite IA pour restaurants décontractés et bistrots : agents spécialisés, calculs de coûts, HACCP, plannings, SEO local et marketing avec base professionnelle. Commencez dès aujourd'hui.",
      "keywords": "IA restaurant décontracté, logiciel restaurant décontracté, gestion bistrot IA, calculs de coûts décontracté, HACCP restaurant décontracté, marketing restaurant décontracté IA, SEO local restaurant, restaurant décontracté Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-casual.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre restaurant dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous lui racontez quel type de restaurant décontracté vous gérez (méditerranéen, bistrot, gastrobar, auberge, tapas), nombre de couverts, ville et façon de travailler. À partir de ce moment, chaque agent — de Restaurants Décontractés AI+ à MenuDish Local SEO — répond adapté à votre contexte : ticket moyen de votre zone, réglementation et opérationnel réel.",
    "appsTitle": "Les Agents IA que vous utiliserez dans votre restaurant décontracté",
    "apps": [
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts de Restauration",
        "description": "Agent principal : bistrots, gastrobars, tapas et méditerranéen avec base professionnelle."
      },
      {
        "name": "Manager de Restaurant Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistant opérationnel et reporting au propriétaire."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de plats professionnels avec recette + calcul CSV."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises sur les pertes et rendements pour le contrôle en cuisine."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette et plat."
      },
      {
        "name": "Repas du Personnel",
        "category": "Gastro Profile Pro",
        "description": "Générateur de menus pour le personnel avec le produit que vous avez déjà en chambre froide."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Descriptions de plats optimisées pour le SEO local."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles de blog pour attirer du trafic organique local."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Mots-clés gastronomiques par zone postale."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Contenu viral pour Instagram avec calendrier éditorial."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie gastronomique IA pour le web et les réseaux sociaux."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching pour la gestion du stress en haute pression et les conversations difficiles."
      }
    ],
    "metrics": [
      {
        "value": "−3 pp",
        "label": "food cost au premier trimestre"
      },
      {
        "value": "×2",
        "label": "réservations via SEO local"
      },
      {
        "value": "−6 h",
        "label": "hebdomadaires en gestion"
      },
      {
        "value": "12+",
        "label": "agents pour votre restaurant"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Opération sur des feuilles volantes avec chaque poste fonctionnant à sa manière",
        "HACCP sur papier imprimé qui se perd avant l'inspection",
        "Plannings manuels sur Excel pendant des heures",
        "Marketing improvisé sans acquisition organique de clients",
        "Food cost au jugé, sans savoir quel plat perd de la rentabilité"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Kit de Tareas avec des modèles structurés par service et poste",
        "HACCP depuis le mobile avec enregistrements, alertes et exportation PDF",
        "Plannings en minutes avec le Kit Gestión de Personal respectant la convention collective",
        "Suite SEO local attirant des réservations organiques sans dépense en agences",
        "Food cost par plat calculé en détail avec un calcul professionnel"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Restaurant Décontracté Moderne",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : salle, cuisine ouverte, terrasse, plat du jour, équipe et bar.",
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
    "h1": "IA pour Café et Brunch",
    "heroSubtitle": "Optimisez petits-déjeuners, brunch, café de spécialité et pâtisserie avec une suite d'agents IA conçus pour les coffee shops, les établissements de brunch et les cafés modernes.",
    "heroTagline": "Coffee shop moderne avec une opération moderne",
    "badge": "Pour cafés de spécialité et brunch",
    "painsTitle": "Ce Qu'un Coffee Shop ou un Établissement de Brunch Ne Peut Pas Ignorer",
    "pains": [
      "Carte courte mais rotation très élevée aux heures de pointe du matin et de midi",
      "Marge très serrée sur le café de spécialité et la pâtisserie avec un coût du lait et du cacao volatil",
      "Équipe jeune et tournante qui a besoin d'une formation rapide au bar et au service",
      "Le branding et les réseaux sociaux (Instagram, Pinterest) sont le principal levier d'acquisition",
      "Se différencier dans une zone concurrentielle avec un pricing premium mais accessible",
      "Gérer le flux du brunch le week-end sans faire s'effondrer l'opération en semaine"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide dans un Café à Brunch",
    "features": [
      {
        "icon": "Coffee",
        "title": "Restaurants Décontractés AI+",
        "description": "Agent avec une connaissance des coffee shops, des brunchs et des cafés de spécialité : cartes, pricing et opération."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos de café, brunch et viennoiseries",
        "description": "Cuisine Créative livre une recette + un escandallo CSV ; Kit de Escandallos Pro le gère avec vos prix réels."
      },
      {
        "icon": "Sparkles",
        "title": "Pâtisserie Créative + Boulangerie Créative",
        "description": "Recettes professionnelles pour pâtisserie, brioche, croissants, cakes et boulangerie artisanale."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Cafetería",
        "description": "Modèles spécifiques : ouverture, fermeture, bar, cuisine légère, brunch, service et nettoyage."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC simplifié",
        "description": "Pack APPCC avec des registres minimaux mais complets pour un café : lait, conservation, lavage, températures."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie culinaire IA + contenu Instagram avec captions, calendrier éditorial et planification."
      },
      {
        "icon": "Search",
        "title": "Pinterest Pins Gen",
        "description": "Pinterest est clé pour les coffee shops : épingles de brunch, café latte art et pâtisserie pour attirer un trafic organique."
      },
      {
        "icon": "BarChart3",
        "title": "KPIs et ticket moyen",
        "description": "Kit Plan Financiero : taux d'occupation, ticket moyen, productivité et upselling du brunch et du café."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Mots-clés culinaires locaux pour « brunch [votre quartier] », « café de spécialité près de chez moi » et similaires."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Café à Brunch avec AI Chef Pro",
    "workflow": [
      "07:00 · Ouverture — checklist du Kit de Tareas Cafetería : bar lancé, café moulu, lait froid, vitrine prête.",
      "08:00 · Service matin — petits-déjeuners et café de spécialité avec un flux coordonné entre le bar et la cuisine légère.",
      "11:00 · Cuisine Créative — vous développez un nouveau brunch pour samedi : tartines à la burrata, gravlax et œufs. Vous recevez un escandallo CSV.",
      "11:30 · Kit de Escandallos Pro — vous chargez le CSV avec les prix réels et validez la marge cible (32 %).",
      "13:00 · Service midi — brunch en cours, équipe coordonnée avec des modèles spécifiques.",
      "16:00 · GastroIMG Gen+ + Pinterest Pins Gen — vous générez des photos du nouveau brunch et des épingles optimisées pour Pinterest.",
      "17:30 · InstaFlow AI Pro — vous programmez les posts Instagram pour la semaine prochaine avec un calendrier éditorial.",
      "19:30 · Fermeture — nettoyage en profondeur, APPCC signé, planification de la pâtisserie pour le lendemain."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Cafés",
    "productIds": [
      "kit-tareas-cafeteria",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Nous proposons un brunch le week-end et du café de spécialité en semaine. Le Kit de Tareas Cafetería et la génération de contenu pour Instagram m'ont rendu mes soirées. Pinterest Pins Gen a été une découverte : il nous a apporté un trafic organique que je n'avais jamais vu.",
    "testimonialAuthor": "Marcos Rivera",
    "testimonialRole": "Propriétaire, coffee shop de spécialité et brunch",
    "faqTitle": "Questions Fréquentes des Coffee Shops",
    "faqs": [
      {
        "q": "Est-ce adapté au café de spécialité ou seulement à la cafétéria casual ?",
        "a": "C'est adapté aux deux. Il y a des modèles adaptables aussi bien aux coffee shops de spécialité (V60, espresso de terroir, latte art) qu'aux cafétérias casual et aux brunchs."
      },
      {
        "q": "Est-ce que ça fonctionne pour les établissements avec une cuisine très légère ?",
        "a": "Oui. Le Kit de Tareas Cafetería a des modèles spécifiques pour cuisine légère, brunch et bar, sans supposer que vous avez une brigade complète."
      },
      {
        "q": "Est-ce que ça génère du contenu optimisé pour Instagram et Pinterest ?",
        "a": "Oui. InstaFlow AI Pro et Pinterest Pins Gen sont des agents spécifiques pour ces canaux. Pinterest fonctionne très bien pour le brunch et le café avec un trafic organique stable."
      },
      {
        "q": "Est-ce que ça couvre la livraison et les horaires étendus ?",
        "a": "Oui. Les modèles sont adaptables à l'horaire, à la livraison, au take-away et au catering léger (pause café d'entreprise)."
      },
      {
        "q": "Comment est-ce que ça optimise le SEO local pour mon coffee shop ?",
        "a": "MenuDish Local SEO + BlogPost SEO Gen+ + Keyword Discovery AI+ travaillent ensemble pour capter les recherches locales comme « brunch dans [votre zone] » ou « meilleur café de spécialité près de chez moi »."
      }
    ],
    "ctaTitle": "Votre café avec une opération rodée et une acquisition organique.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Café et Brunch : Opération, Pinterest et SEO Local | AI Chef Pro",
      "description": "Suite IA pour coffee shops et établissements de brunch : agents spécialisés, escandallos, APPCC, contenu pour Instagram et Pinterest, SEO local. Commencez aujourd'hui.",
      "keywords": "IA café, logiciel brunch, IA coffee shop, gestion café de spécialité, escandallos café, marketing café IA, Pinterest brunch, SEO local café, coffee shop France",
      "ogImage": "https://aichef.pro/og/use-cases/cafeteria-brunch.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Coffee Shop dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous lui décrivez le type de café que vous gérez (spécialité, brunch, casual), la ville et votre façon de travailler. À partir de ce moment, chaque agent — de la Pâtisserie Créative à Pinterest Pins Gen — répond adapté à votre contexte : ticket moyen de votre zone, profil client et opération réelle.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser dans Votre Café",
    "apps": [
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts de Business",
        "description": "Agent principal : coffee shops, brunch et café avec une base professionnelle."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Recettes professionnelles pour la pâtisserie de café : brioche, croissants, cakes, tartes."
      },
      {
        "name": "Boulangerie Créative",
        "category": "Créativité Culinaire",
        "description": "Pour les coffee shops qui cuisent leur propre pain et viennoiseries au levain."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de plats de brunch avec recette + escandallo CSV."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette."
      },
      {
        "name": "Repas du Personnel",
        "category": "Gastro Profile Pro",
        "description": "Générateur de menus pour le personnel qui motivent l'équipe."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Descriptions SEO local pour améliorer le positionnement."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles de blog pour attirer un trafic organique vers le coffee shop."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Mots-clés par zone postale : brunch, café de spécialité, etc."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Contenu viral Instagram avec calendrier éditorial."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Épingles optimisées pour Pinterest : brunch, café, pâtisserie."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie culinaire IA pour le web, les réseaux et la carte."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "trafic organique via Pinterest"
      },
      {
        "value": "+ 1,80 €",
        "label": "ticket moyen grâce à l'upselling"
      },
      {
        "value": "−4 h",
        "label": "hebdomadaires en gestion des réseaux"
      },
      {
        "value": "12+",
        "label": "agents pour votre café"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Opération du bar et de la cuisine légère improvisée à chaque service",
        "Escandallos au doigt mouillé sur le café et la pâtisserie avec une marge incertaine",
        "Instagram chaotique sans calendrier éditorial ni continuité",
        "Aucune présence sur Pinterest, perdant le trafic organique qui convertit le mieux pour le brunch",
        "APPCC sur un carnet qui est oublié lors de l'inspection"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Kit de Tareas Cafetería avec des modèles spécifiques par service et par poste",
        "Escandallo professionnel sur chaque boisson et plat avec une marge réelle",
        "InstaFlow AI Pro avec calendrier éditorial et captions optimisées",
        "Pinterest Pins Gen captant un trafic organique stable et à forte conversion",
        "APPCC depuis le mobile avec des registres prêts pour l'inspection"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Café à Brunch Moderne",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : spécialité et brunch, barista, pâtisserie, équipe de service et contenu pour les réseaux.",
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
    "h1": "IA pour Pizzeria",
    "heroSubtitle": "Standardisez le levain, calculez les coûts par pizza, contrôlez la livraison et la multi-marque avec une suite d'agents IA spécialisés en pizzeria professionnelle, pizza napolitaine, romaine et américaine.",
    "heroTagline": "Pizza avec marge réelle, technique avec système",
    "badge": "Pour les pizzerias et les pizzaioli",
    "painsTitle": "Ce qu'une pizzeria ne peut pas ignorer",
    "pains": [
      "Marge très serrée sur la pizza avec contrôle millimétrique du grammage en pâte, sauce, fromage et toppings",
      "Pertes en levain, mozzarella et sauces qui saignent la rentabilité sans contrôle",
      "Pics de demande en livraison (12:30-14:30, 20:30-22:30) sans marge d'erreur",
      "Carte large de pizzas avec calcul de coût individualisé par variante",
      "Standardiser la pâte et la technique dans des cuisines où l'équipe de pizzaioli tourne",
      "Attirer des clients locaux avec le SEO et les réseaux pour réduire la dépendance aux plateformes de livraison"
    ],
    "featuresTitle": "Comment AI Chef Pro aide une pizzeria",
    "features": [
      {
        "icon": "Pizza",
        "title": "Cuisine Italienne",
        "description": "Agent spécialisé en cuisine italienne professionnelle, pâtes, sauces et technique de pizzeria napolitaine, romaine et américaine."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Pour les levains, fermentations longues, hydratations élevées et technique de boulangerie appliquée à la pizza professionnelle."
      },
      {
        "icon": "Calculator",
        "title": "Calcul de coût par pizza",
        "description": "Cuisine Créative fournit recette + calcul de coût CSV ; Kit de Escandallos Pro le gère avec vos prix réels et marge cible par variante."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pizzería",
        "description": "Modèles : hydratation de la pâte, préparation des sauces, mise en place des toppings, service en salle et livraison."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC",
        "description": "Modèles adaptés à la pizzeria : températures du four, conservation du levain, traçabilité pour la livraison."
      },
      {
        "icon": "Truck",
        "title": "Burger Pro AI+ + Food Truck AI+",
        "description": "Si vous opérez une dark kitchen multi-marques, des agents complémentaires pour la livraison spécialisée sont également disponibles."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + InstaFlow AI Pro",
        "description": "Positionnement local sur Google et contenu viral pour Instagram avec calendrier éditorial."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Photographie gastronomique IA pour Glovo, Uber Eats, Just Eat et le site web du restaurant."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Tableaux de service pour pizzaioli, salle et livraison avec roulement et pics de service."
      }
    ],
    "workflowTitle": "Une journée réelle dans une pizzeria avec AI Chef Pro",
    "workflow": [
      "08:00 · Ouverture — checklist Kit de Tareas Pizzería : hydratation du levain, préparation de la sauce tomate, mise en place des toppings.",
      "10:00 · Cuisine Italienne + Fermentus Avec AI+ — vous développez une nouvelle pizza de saison avec une pâte à hydratation 75 % et fermentation 48 h.",
      "11:00 · Kit de Escandallos Pro — vous calculez le coût de la nouvelle pizza avec vos prix réels (farine, mozzarella, prosciutto) et validez une marge de 32 %.",
      "12:30 · Service de midi — pizzaiolo au four, salle pleine, livraison active avec des modèles spécifiques.",
      "15:30 · Inventaire — vous validez les commandes de farine italienne, mozzarella di bufala et conserves avec le Kit Inventario.",
      "17:00 · MenuDish Local SEO — vous mettez à jour les descriptions des pizzas top sur Google Business et le site web.",
      "20:00 · Service du soir — pic de livraison, pizzaiolo au four coordonné avec la salle et les livreurs.",
      "23:30 · Fermeture — nettoyage, APPCC signé, rapport du jour au propriétaire."
    ],
    "productsTitle": "Modèles et kits téléchargeables pour pizzeria",
    "productIds": [
      "kit-tareas-pizzeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Nous avons fait un calcul de coût pizza par pizza avec le Kit de Escandallos Pro et découvert que 4 variantes étaient en perte parce que nous pesions trop de mozzarella. Nous avons ajusté le grammage et le prix. La marge du restaurant a augmenté de 4 points en 2 mois sans toucher à la qualité.",
    "testimonialAuthor": "Giovanni Russo",
    "testimonialRole": "Pizzaiolo et propriétaire, pizzeria napolitaine",
    "faqTitle": "Questions fréquentes des pizzerias",
    "faqs": [
      {
        "q": "Est-ce que cela fonctionne pour la pizza napolitaine, romaine, américaine ou detroit ?",
        "a": "Pour toutes. Cuisine Italienne et Fermentus Avec AI+ couvrent tout le spectre des pâtes, hydratations, fermentations et techniques de chaque style."
      },
      {
        "q": "Est-ce que cela couvre la livraison en plus du restaurant ?",
        "a": "Oui. Le Kit de Tareas Pizzería inclut des modèles spécifiques de livraison avec temps, pertes associées et coordination avec les plateformes (Glovo, Uber Eats, Just Eat)."
      },
      {
        "q": "Est-ce que cela fonctionne pour 1 restaurant ou une chaîne de pizzerias ?",
        "a": "Les deux. Il y a des clients avec 1 restaurant et d'autres avec plus de 12 unités actives. Pour les groupes, Chef Exécutif Pro standardise les recettes et les manuels."
      },
      {
        "q": "Est-ce que cela génère des idées de promotions pour les jours creux ?",
        "a": "Oui. Gastro Calendar + InstaFlow AI Pro génèrent des combos, offres, calendrier éditorial et campagnes saisonnières avec une créativité professionnelle."
      },
      {
        "q": "Comment cela m'aide-t-il avec le levain professionnel ?",
        "a": "Fermentus Avec AI+ est une référence en fermentation : hydratations, préferments (poolish, biga, tang zhong), rafraîchis de levain et techniques de fermentation contrôlée."
      }
    ],
    "ctaTitle": "Pizza avec marge réelle, pas d'intuition.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Pizzeria : Levain, Calcul de coût par pizza et Livraison | AI Chef Pro",
      "description": "Suite IA pour pizzerias professionnelles : Cuisine Italienne, Fermentus pour les pâtes, calculs de coût par pizza, modèles pizza-shop et SEO local. Commencez dès aujourd'hui.",
      "keywords": "IA pizzeria, calcul de coût pizza, logiciel pizzeria, levain pizza IA, pizza napolitaine IA, pizza romaine IA, gestion pizzeria livraison, pizzeria Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/pizzeria.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre pizzeria dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes dans lequel vous lui expliquez quel type de pizzeria vous exploitez (napolitaine, romaine, américaine, detroit, alla pala), le nombre de couverts, la ville et l'organisation. À partir de ce moment, chaque agent — de Cuisine Italienne à MenuDish Local SEO — répond adapté à votre style de pâte, vos plateformes de livraison et votre marché local.",
    "appsTitle": "Les agents IA que vous utiliserez dans votre pizzeria",
    "apps": [
      {
        "name": "Cuisine Italienne",
        "category": "Recettes par pays",
        "description": "Agent spécialisé en cuisine italienne professionnelle avec base de pizzeria napolitaine et romaine."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité culinaire",
        "description": "Levain, hydratations élevées et fermentations longues avec un soutien professionnel."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité culinaire",
        "description": "Développement de pizzas créatives avec recette + calcul de coût CSV."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'entreprise",
        "description": "Pour coordonner le reste du menu décontracté de la pizzeria (entrées, desserts)."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et utilitaires",
        "description": "Données précises sur les pertes en pâte, mozzarella et toppings."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et utilitaires",
        "description": "Identification automatique des allergènes par pizza et plat."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et réseaux sociaux",
        "description": "Descriptions SEO local pour améliorer le positionnement web et la livraison."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et réseaux sociaux",
        "description": "Articles de blog pour attirer du trafic organique local."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Contenus et réseaux sociaux",
        "description": "Mots-clés par zone postale : « pizza napolitaine [votre quartier] »."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et réseaux sociaux",
        "description": "Contenu viral Instagram avec photos de pizza et calendrier éditorial."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance gastronomique",
        "description": "Photographie gastronomique IA pour le web et les plateformes de livraison."
      }
    ],
    "metrics": [
      {
        "value": "+4 pp",
        "label": "marge après calcul de coût pizza par pizza"
      },
      {
        "value": "×2",
        "label": "trafic de livraison via SEO local"
      },
      {
        "value": "−25 %",
        "label": "pertes avec contrôle systématique"
      },
      {
        "value": "11+",
        "label": "agents pour votre pizzeria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Levain et technique dispersés dans le carnet du pizzaiolo principal",
        "Calculs de coût à l'œil, grammages qui varient entre pizzaioli",
        "Pertes de mozzarella et de pâte sans contrôle réel",
        "Positionnement faible en livraison à cause de descriptions génériques",
        "Opération de livraison improvisée aux heures de pointe"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Cuisine Italienne + Fermentus Avec AI+ documentent la pâte et la technique reproductible",
        "Calcul de coût professionnel par pizza avec marge validée",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques",
        "SEO local optimisé avec MenuDish Local SEO + Keyword Discovery",
        "Kit de Tareas Pizzería avec modèles pour livraison, restaurant et pics"
      ]
    },
    "galleryTitle": "Comment fonctionne une pizzeria professionnelle",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : four, levain, pizza au détail, préparation des toppings, équipe et livraison.",
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
    "h1": "IA pour les restaurants de burgers",
    "heroSubtitle": "Calcul de coût par burger, contrôlez le coût de la viande et du pain, gérez la livraison et la multi-marque avec une suite d'agents IA spécialisés dans le smash burger gourmet, le fast casual et la dark kitchen de burgers.",
    "heroTagline": "Burger avec une marge réelle, pas de l'intuition",
    "badge": "Pour les restaurants de burgers et les burger shops",
    "painsTitle": "Ce Qu'un Restaurant de Burgers Doit Résoudre",
    "pains": [
      "Viande et pain : ingrédients clés au coût volatil qui change chaque semaine",
      "Pertes à la cuisson de la viande, au montage et à l'emballage pour la livraison",
      "Livraison avec une très forte rotation et des pics brutaux à des heures précises",
      "Carte étendue avec de nombreuses variantes de burger (classique, gourmet, smash, plant-based)",
      "Se différencier dans un marché saturé de burger shops grâce au SEO local et aux réseaux sociaux",
      "Standardiser la technique de plancha et de montage quand l'équipe tourne"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Restaurant de Burgers",
    "features": [
      {
        "icon": "Beef",
        "title": "Burger Pro AI+",
        "description": "Agent spécialisé dans les restaurants de burgers : gourmet, smash, fast food, plant-based, artisanal et thématique."
      },
      {
        "icon": "Calculator",
        "title": "Fiches techniques par burger",
        "description": "Cuisine Créative livre recette + fiche technique CSV ; Kit de Escandallos Pro le gère avec vos prix réels (viande, pain, fromage, toppings, sauces)."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Hamburguesería",
        "description": "Modèles : préparation des sauces, mise en place des toppings, plancha, montage, service et livraison."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC + ID Allergènes",
        "description": "Traçabilité de la viande, contrôle de la cuisson, température et allergènes par burger."
      },
      {
        "icon": "Truck",
        "title": "Gestion multi-plateforme de livraison",
        "description": "Plan financier avec calcul de marge après commissions de Glovo, Uber Eats et Just Eat par marque virtuelle."
      },
      {
        "icon": "Leaf",
        "title": "VegChef Plant-Based",
        "description": "Pour les burgers végétaux avec une technique nutritionnelle : Beyond Meat, Heura, alternatives plant-based de qualité."
      },
      {
        "icon": "Sparkles",
        "title": "MenuDish Local SEO + InstaFlow AI Pro",
        "description": "Positionnement local sur Google et contenu viral pour Instagram, où les burger shops vendent le plus."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Photographie gastronomique IA critique pour Glovo, Uber Eats et Just Eat : meilleure photo = plus de clics et meilleur classement."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Tableaux pour plancha, montage, salle et livraison avec horaires rotatifs."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Restaurant de Burgers avec AI Chef Pro",
    "workflow": [
      "11:00 · Ouverture — checklist Kit de Tareas Hamburguesería : préparation des sauces maison, mise en place des toppings, plancha prête.",
      "12:00 · Burger Pro AI+ — vous développez une nouvelle burger gourmet au chèvre et à la confiture d'oignon. Cuisine Créative livre recette + fiche technique CSV.",
      "12:30 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels et validez une marge de 31 % après commission Glovo (29 %).",
      "13:00 · Service de midi — plancha active, montage coordonné, livraisons en cours, salle pleine.",
      "16:00 · MenuDish Local SEO + GastroIMG Gen+ — vous mettez à jour la nouvelle burger sur les plateformes avec une photo professionnelle et une description optimisée.",
      "17:30 · Inventaire — vous validez les commandes de viande (fournisseur local), pain brioché et fromage premium.",
      "20:00 · Service du soir — pic de livraison, montage à la chaîne, plancha au maximum.",
      "23:30 · Fermeture — nettoyage, HACCP signé, rapport du jour et pertes enregistrées."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Restaurant de Burgers",
    "productIds": [
      "kit-tareas-hamburgueseria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Nous avons fait passer le food cost de 36 % à 31 % en 60 jours grâce à des fiches techniques précises et un contrôle systématique des pertes. L'investissement dans AI Chef Pro a été rentabilisé en une semaine rien qu'avec ça. La photo IA pour Glovo a fait passer notre classement de la 8e à la 3e place.",
    "testimonialAuthor": "Pablo Hernández",
    "testimonialRole": "Propriétaire, restaurant de burgers gourmet avec 2 marques en livraison",
    "faqTitle": "Questions Fréquentes des Restaurants de Burgers",
    "faqs": [
      {
        "q": "Est-ce que ça fonctionne pour un restaurant de burgers gourmet, smash ou casual ?",
        "a": "Pour tous. Burger Pro AI+ couvre tout le spectre : gourmet, smash burger, fast food, plant-based et thématique."
      },
      {
        "q": "Est-ce que ça couvre la livraison en plus du sur place ?",
        "a": "Oui. Des modèles spécifiques avec les pertes de livraison, un packaging personnalisé, la coordination avec les plateformes et le calcul de marge après commissions."
      },
      {
        "q": "Y a-t-il un contrôle spécifique de la viande et une traçabilité ?",
        "a": "Oui. Pack APPCC avec traçabilité de la viande, contrôle de la cuisson à point, température interne et conservation."
      },
      {
        "q": "Est-ce que ça génère des idées de combos et de promotions ?",
        "a": "Oui. Gastro Calendar + InstaFlow + Pro Prompts eBook génèrent des combos, des offres pour les jours creux, un calendrier éditorial et des campagnes avec IA."
      },
      {
        "q": "Est-ce que ça sert à ouvrir une marque virtuelle de burger en dark kitchen ?",
        "a": "Oui. Burger Pro AI+ + Restaurants Décontractés AI+ + Food Truck AI+ sont combinables pour une multi-marque virtuelle. Il y a un cas réel sur /usos/concepto/dark-kitchen."
      }
    ],
    "ctaTitle": "Burger avec une marge réelle, pas de l'intuition.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Restaurants de Burgers : Fiches Techniques, Smash Burger et Livraison | AI Chef Pro",
      "description": "Suite IA pour les restaurants de burgers professionnels : Burger Pro AI+, fiches techniques par burger, modèles burger-shop, HACCP et livraison multi-plateforme. Commencez dès aujourd'hui.",
      "keywords": "IA restaurant de burgers, fiches techniques burger, logiciel restaurant de burgers, smash burger IA, gestion livraison burger, restaurant de burgers gourmet IA, restaurant de burgers Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/hamburgueseria.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Restaurant de Burgers dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes dans lequel vous lui racontez quel type de restaurant de burgers vous exploitez (gourmet, smash, fast casual, plant-based), le nombre de couverts, la ville, les plateformes de livraison et les commissions. Chaque agent — de Burger Pro AI+ au Kit de Escandallos Pro — répond adapté à votre style et à votre marché réel.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Restaurant de Burgers",
    "apps": [
      {
        "name": "Burger Pro AI+",
        "category": "Concepts d'Entreprise",
        "description": "Agent spécialisé dans les restaurants de burgers : gourmet, smash, fast food, plant-based."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de burgers professionnels avec recette + fiche technique CSV."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Créativité Culinaire",
        "description": "Pour les burgers végétaux avec une technique nutritionnelle professionnelle."
      },
      {
        "name": "Food Truck AI+",
        "category": "Concepts d'Entreprise",
        "description": "Pour les concepts mobiles et les dark kitchens multi-marques de burgers."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises sur les pertes à la cuisson de la viande et au montage."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par burger et sauce."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Descriptions SEO local pour Glovo, Uber Eats et le web."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles de blog pour capter les recherches locales de burgers."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Mots-clés par zone postale : « smash burger [votre quartier] »."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Contenu viral Instagram pour les restaurants de burgers."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie gastronomique IA pour les plateformes de livraison."
      }
    ],
    "metrics": [
      {
        "value": "−5 pp",
        "label": "food cost en 60 jours"
      },
      {
        "value": "+5",
        "label": "places au classement Glovo"
      },
      {
        "value": "×3",
        "label": "vitesse de lancement d'une nouvelle burger"
      },
      {
        "value": "11+",
        "label": "agents pour votre burger shop"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Fiches techniques au pif avec un grammage variable selon les cuisiniers",
        "Food cost à 36 % à cause des pertes et d'un montage sans contrôle",
        "Photos de mauvaise qualité sur Glovo et Uber Eats, classement bas",
        "Pertes de viande et de montage sans traçabilité",
        "Opérations de livraison improvisées aux heures de pointe"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Burger Pro AI+ + Cuisine Créative documentent une technique reproductible",
        "Food cost à 31 % avec une fiche technique professionnelle et des pertes contrôlées",
        "Photos professionnelles avec GastroIMG Gen+ qui améliorent le classement sur les plateformes",
        "Pack APPCC avec traçabilité de la viande et pertes enregistrées",
        "Kit de Tareas Hamburguesería avec des modèles pour la livraison et le sur place"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Restaurant de Burgers Moderne",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : plancha, smash burger, montage, préparation, équipe et livraison.",
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
    "h1": "IA pour Dark Kitchen et Cuisines Virtuelles",
    "heroSubtitle": "Développez 1, 4 ou 10 marques virtuelles dans une même cuisine. Contrôlez le food cost par marque et par plateforme, améliorez votre positionnement dans les agents IA de livraison et multipliez les tickets sans embaucher de salle.",
    "heroTagline": "Cuisine sans salle, marge avec système",
    "badge": "Dark Kitchen et Ghost Kitchen",
    "painsTitle": "Ce Qu'un Opérateur de Dark Kitchen Ne Peut Pas Ignorer",
    "pains": [
      "Plusieurs marques dans une même cuisine, chacune avec sa propre fiche technique et des coûts de matières premières qui changent chaque semaine",
      "Marge compressée par les commissions de Glovo, Uber Eats et Just Eat (entre 25 % et 35 % du ticket)",
      "Pics brutaux en livraison, de 12:30 à 14:30 et de 20:30 à 22:30, sans marge d'erreur opérationnelle",
      "Aucun contact physique avec le client : la marque, les photos et le texte de la fiche sont tout ce que vous avez",
      "Positionnement sur les plateformes qui change constamment : si vous perdez des positions, les commandes chutent en flèche",
      "Difficile de savoir quelle marque et quel plat performent vraiment quand tout se mélange dans la même cuisine"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide une Dark Kitchen",
    "features": [
      {
        "icon": "Layers",
        "title": "Fiches techniques multi-marques : Cuisine Créative → Kit de Escandallos Pro",
        "description": "Cuisine Créative génère le plat et la fiche technique initiale en CSV avec des prix de référence du marché. Vous la chargez dans le Kit de Escandallos Pro, remplacez les prix par ceux de vos fournisseurs et obtenez le coût réel et la marge par marque, par plat et par plateforme."
      },
      {
        "icon": "Smartphone",
        "title": "Burger Pro AI+, Food Truck AI+ et Restaurants Décontractés AI+",
        "description": "Trois agents spécialisés qui couvrent les concepts virtuels les plus rentables en livraison : burger, fast-food, casual et bistrot."
      },
      {
        "icon": "Truck",
        "title": "Calcul de la marge réelle après commission",
        "description": "Le plan financier d'AI Chef Pro déduit automatiquement les commissions de chaque plateforme et vous affiche la marge réelle par marque et par canal."
      },
      {
        "icon": "TrendingUp",
        "title": "MenuDish Local SEO + BlogPost SEO Gen+",
        "description": "Suite SEO pour que vos marques grimpent dans le SEO local de Google et captent du trafic organique, en plus de celui qui arrive via les agents IA."
      },
      {
        "icon": "Search",
        "title": "Keyword Discovery AI+",
        "description": "Recherche de mots-clés gastronomiques locaux pour nommer marques, plats et cartes qui se positionnent mieux."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Photographie culinaire générée par IA pour les fiches plateforme. Meilleure photo = plus de clics et un meilleur positionnement."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative + Cuisine Italienne, Mexicaine, Japonaise…",
        "description": "Plus de 25 recueils de recettes IA par pays pour créer des marques virtuelles thématiques avec une base professionnelle, pas des recettes copiées sur Google."
      },
      {
        "icon": "ShieldCheck",
        "title": "APPCC + ID Allergènes pour la livraison",
        "description": "Traçabilité, température et allergènes pensés pour un produit qui voyage en sac à dos ou en moto."
      },
      {
        "icon": "BarChart3",
        "title": "Tableau de bord multi-marques et multi-plateformes",
        "description": "KPI par marque, ticket moyen, commission, position dans le classement et productivité. Le tout consolidé dans une seule vue."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans une Dark Kitchen avec AI Chef Pro",
    "workflow": [
      "08:30 · Vous consultez le tableau de bord de la veille : la marque A est en tête, la marque C a chuté de 12 % en positionnement. Il faut agir.",
      "09:00 · Keyword Discovery AI+ — vous recherchez ce que les utilisateurs de votre zone postale tapent et détectez un mot-clé qui manque à la marque C.",
      "09:30 · MenuDish Local SEO — vous mettez à jour les descriptions des 6 plats phares de la marque C avec ce mot-clé.",
      "10:00 · Cuisine Créative — brainstorming pour un plat signature dans la marque A, en profitant d'une bonne affaire d'un fournisseur. Le même agent vous renvoie la recette complète et une fiche technique initiale avec des prix de référence du marché, téléchargeable en CSV.",
      "10:30 · Kit de Escandallos Pro — vous chargez le CSV de Cuisine Créative, remplacez les prix de référence par ceux de vos fournisseurs négociés et validez la marge après commission sur Glovo (29 %) et Uber Eats (25 %).",
      "11:00 · GastroIMG Gen+ — vous générez la photo du nouveau plat et la téléversez sur les plateformes.",
      "12:30 · Service en livraison, avec 4 marques opérant dans la même cuisine, appuyées par les modèles de tâches Dark Kitchen.",
      "16:00 · APPCC signé, pertes enregistrées par marque et mise en place du dîner prête.",
      "23:30 · Clôture : rapport automatique par marque envoyé sur le WhatsApp du propriétaire."
    ],
    "productsTitle": "Modèles, Kits et Guides Téléchargeables pour Dark Kitchen",
    "productIds": [
      "guia-dark-kitchen",
      "kit-tareas-dark-kitchen",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "kit-inventario"
    ],
    "testimonialQuote": "Nous exploitons 4 marques virtuelles dans une seule cuisine. Sans fiches techniques par marque et par plateforme, nous perdions de la marge sans savoir où. AI Chef Pro nous a tout résolu en une semaine : nous avons détecté qu'une marque avait un food cost de 41 % sur Glovo. Nous l'avons repensée et avons gagné 7 points de marge sans toucher au prix.",
    "testimonialAuthor": "Iván Domínguez",
    "testimonialRole": "Opérateur, dark kitchen avec 4 marques virtuelles",
    "faqTitle": "Questions Fréquentes des Opérateurs de Dark Kitchen",
    "faqs": [
      {
        "q": "Est-ce que ça fonctionne pour 1 marque ou pour plusieurs dans la même cuisine ?",
        "a": "Pour les deux. C'est pensé dès la base pour le multi-marques : fiche technique indépendante par marque, KPI séparés et listes de tâches qui coordonnent la production de plusieurs marques dans la même cuisine."
      },
      {
        "q": "Est-ce que ça couvre les commissions des plateformes (Glovo, Uber Eats et Just Eat) ?",
        "a": "Oui. Le calcul de la marge réelle déduit automatiquement la commission de chaque plateforme, pour que vous sachiez ce que vous gagnez sur chaque commande par canal et puissiez mieux décider votre politique de prix."
      },
      {
        "q": "Y a-t-il un guide pas à pas pour ouvrir une dark kitchen ?",
        "a": "Oui, le Guide Comment Monter une Dark Kitchen (24 €) : 12 chapitres avec les exigences légales, le plan financier, la conception de la cuisine, la technologie, le marketing et les plateformes, plus 3 checklists dans Excel et une calculatrice."
      },
      {
        "q": "Est-ce que ça sert à passer à l'échelle sur plusieurs emplacements de dark kitchen ?",
        "a": "Oui. La standardisation multi-sites de l'agent Chef Exécutif Pro et les tableaux de bord consolidés sont pensés pour les groupes avec plusieurs unités virtuelles."
      },
      {
        "q": "Comment ça m'aide à améliorer le positionnement dans les agents IA de livraison ?",
        "a": "Avec trois leviers : GastroIMG Gen+ pour des photos de meilleure qualité (qui augmentent le CTR), MenuDish Local SEO pour des descriptions qui convertissent et Keyword Discovery AI+ pour détecter ce que recherchent les utilisateurs de votre zone postale."
      },
      {
        "q": "Est-ce que le système s'adapte à mon pays et à mes plateformes ?",
        "a": "Oui. Vous commencez avec l'agent « Qui suis-je ? » dans un onboarding de 2 minutes où vous lui dites où vous opérez, quelles plateformes vous utilisez et quelles commissions vous avez négociées. Tout le reste s'adapte à votre contexte."
      },
      {
        "q": "Et le SEO local ? Est-ce que ça vaut le coup pour une dark kitchen ?",
        "a": "Oui, énormément. Une dark kitchen vit de la découverte en ligne : si en plus du trafic des agents IA vous captez des recherches locales sur Google (par exemple, « burger livraison [votre quartier] »), vous réduisez votre dépendance aux commissions et ajoutez de la marge directe. La suite SEO d'AI Chef Pro est pensée exactement pour ça."
      }
    ],
    "ctaTitle": "Votre dark kitchen, avec une marge réelle et des données par marque.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Dark Kitchen et Cuisines Virtuelles : Fiches Techniques et SEO | AI Chef Pro",
      "description": "Suite IA pour dark kitchen et ghost kitchen : fiches techniques multi-marques, marge après commission Glovo et Uber Eats, SEO local, APPCC et guide pour ouvrir votre cuisine virtuelle.",
      "keywords": "IA dark kitchen, logiciel dark kitchen, ghost kitchen, cuisine virtuelle, fiches techniques multi-marques, ouvrir dark kitchen, gestion livraison IA, positionnement Glovo Uber Eats, logiciel cuisine fantôme, marque virtuelle livraison, dark kitchen France, SEO local restaurant livraison",
      "ogImage": "https://aichef.pro/og/use-cases/dark-kitchen.jpg"
    },
    "personalizationTitle": "Personnalisé Selon Vos Marques, Votre Zone et Vos Plateformes",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes. Vous lui racontez quelles marques vous exploitez, dans quelle ville et quelle zone postale, quelles plateformes vous utilisez (Glovo, Uber Eats, Just Eat) et quelles commissions vous avez négociées. À partir de ce moment, les fiches techniques sont calculées avec votre commission réelle, les recommandations de SEO local ciblent votre quartier et les KPI sont consolidés par marque et par canal exactement comme vous en avez besoin. Ce n'est pas un formulaire : c'est une conversation courte qui transforme chaque agent en outil sur mesure.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser dans Votre Dark Kitchen",
    "apps": [
      {
        "name": "Burger Pro AI+",
        "category": "Concepts d'Entreprise",
        "description": "Spécialiste des burger virtuels : gourmet, fast-food, smash burger et plant-based."
      },
      {
        "name": "Food Truck AI+",
        "category": "Concepts d'Entreprise",
        "description": "Concepts mobiles et virtuels de restauration rapide avec une marge maîtrisée."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'Entreprise",
        "description": "Bistrots, gastrobars, tapas et méditerranéen virtuel : tout le spectre casual."
      },
      {
        "name": "Cuisine Italienne, Mexicaine, Japonaise, Thaïlandaise…",
        "category": "Recueils de recettes par pays",
        "description": "Plus de 25 recueils de recettes IA pour créer des marques virtuelles thématiques avec une base professionnelle. Chaque recette arrive avec une fiche technique initiale en CSV prête pour le Kit de Escandallos Pro."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises sur les pertes et les rendements. Essentiel pour une fiche technique réaliste en livraison."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette. Obligatoire pour vendre en livraison en toute légalité."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Descriptions optimisées SEO par plat, prêtes pour le blog et pour les plateformes."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles de blog qui captent du trafic organique local vers vos marques virtuelles."
      },
      {
        "name": "Keyword Discovery AI+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Recherche de mots-clés gastronomiques par zone postale."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie culinaire avec IA pour les fiches plateforme : meilleure photo, meilleur positionnement."
      },
      {
        "name": "Manager de Restaurant Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistant opérationnel pour coordonner les marques, les équipes et les fournisseurs."
      },
      {
        "name": "InstaFlow AI Pro + Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Contenu viral pour capter une audience au-delà des plateformes de livraison."
      }
    ],
    "metrics": [
      {
        "value": "+7 pts",
        "label": "de marge après fiches techniques par marque"
      },
      {
        "value": "×4",
        "label": "marques virtuelles dans une cuisine"
      },
      {
        "value": "−35 %",
        "label": "de temps en gestion multi-marques"
      },
      {
        "value": "12+",
        "label": "agents IA pour dark kitchen"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Fiche technique manuelle dans Excel avec une marge « moyenne » entre les marques",
        "Commissions des plateformes déduites au doigt mouillé, sans savoir quel canal est le plus rentable",
        "Photos de plateforme de qualité moyenne et positionnement erratique",
        "Descriptions génériques qui ne captent pas le SEO local",
        "KPI mélangés : impossible de savoir quelle marque performe vraiment",
        "Opérations sur des feuilles volantes et erreurs aux heures de pointe"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Fiche technique indépendante par marque et par plateforme, avec marge réelle instantanée",
        "Calcul automatique après commission par canal et décisions de prix basées sur les données",
        "Photographies professionnelles avec GastroIMG Gen+ et positionnement plus stable",
        "Descriptions et blog optimisés pour le SEO local de votre zone postale",
        "Tableau de bord multi-marques avec KPI séparés par marque et par canal",
        "Listes de tâches Dark Kitchen spécifiques pour coordonner la production multi-marques"
      ]
    },
    "galleryTitle": "Comment Fonctionne une Dark Kitchen Moderne",
    "gallerySubtitle": "Production multi-marques, packaging personnalisé par marque virtuelle, écrans avec les commandes Glovo, Uber Eats et JustEat, coursiers au pickup et tout ce qui entoure une opération 100 % livraison.",
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
    "h1": "IA pour la Pâtisserie et l'Atelier",
    "heroSubtitle": "Établissez le coût de revient par pièce avec le coût horaire de l'atelier, planifiez la production saisonnière et capturez un branding professionnel avec une suite d'agents IA spécialisés en pâtisserie artisanale.",
    "heroTagline": "Pâtisserie avec une marge réelle et sans paperasse",
    "badge": "Pour les pâtisseries et ateliers artisanaux",
    "painsTitle": "Ce qu'une pâtisserie doit toujours résoudre",
    "pains": [
      "Coûts de revient complexes avec levains, préferments et préparations longues qui nécessitent des heures d'atelier",
      "Pertes élevées en atelier (façonnage, cuisson, décoration) qui érodent la rentabilité sans contrôle",
      "Traçabilité APPCC avec des produits sensibles : œufs, produits laitiers, crèmes, fruits secs",
      "Saisonnalité très forte : couronne des Rois, Saint-Valentin, Pâques, Noël, communions",
      "Se différencier dans une zone concurrentielle : branding visuel, vitrine et réseaux sociaux sont essentiels",
      "Attirer des commandes de gâteaux sur mesure avec marge tout en gérant la pâtisserie quotidienne"
    ],
    "featuresTitle": "Comment AI Chef Pro aide en pâtisserie",
    "features": [
      {
        "icon": "Cake",
        "title": "Pâtisserie Créative",
        "description": "Agent spécialisé en pâtisserie professionnelle, desserts de restaurant, gâteaux sur mesure et viennoiseries avec technique avancée."
      },
      {
        "icon": "Cookie",
        "title": "Chocolaterie Créative",
        "description": "Pour les ateliers qui combinent pâtisserie et chocolaterie : bonbons, ganaches, couvertures et combinaisons."
      },
      {
        "icon": "Wheat",
        "title": "Boulangerie Créative",
        "description": "Pour les ateliers qui font leur propre viennoiserie avec levain, brioche, croissants et boulangerie artisanale."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Levains professionnels, fermentations contrôlées et processus de boulangerie de pointe."
      },
      {
        "icon": "Calculator",
        "title": "Coûts de revient avec coût horaire d'atelier",
        "description": "Cuisine Créative fournit recette + coût de revient CSV ; Kit de Escandallos Pro le gère avec coût horaire d'atelier intégré dans la marge réelle par pièce."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Pastelería",
        "description": "Modèles : préparation du levain, production, façonnage, cuisson, vitrine, conservation."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC pâtisserie",
        "description": "Traçabilité des œufs, crèmes aux produits laitiers, fruits secs et conservation professionnelle."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification saisonnière avec dates clés : couronne des Rois, Saint-Valentin, Pâques, Noël. Calendrier éditorial pour la vitrine."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Photographie gastronomique IA + Pinterest, où les pâtisseries attirent plus de trafic organique stable."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans une Pâtisserie avec AI Chef Pro",
    "workflow": [
      "06:00 · Ouverture — checklist Kit de Tareas Pastelería : rafraîchissement du levain, préparation des gâteaux, préparation des crèmes.",
      "08:00 · Pâtisserie Créative — vous développez un nouveau dessert pour la Saint-Valentin. Cuisine Créative fournit recette + coût de revient CSV.",
      "09:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels et le coût horaire de l'atelier intégré, vous validez la marge.",
      "11:00 · Production du jour — façonnage et cuisson avec des modèles spécifiques, pertes enregistrées avec APPCC.",
      "14:00 · Réapprovisionnement de la vitrine avec étiquettes et prix, contrôle des pertes d'exposition.",
      "16:00 · Gastro Calendar — vous préparez la planification de production de la couronne des Rois (Noël).",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — vous générez des photos et des épingles du nouveau dessert pour attirer du trafic.",
      "20:00 · Fermeture — nettoyage en profondeur, APPCC signé, planification du lendemain."
    ],
    "productsTitle": "Modèles et kits téléchargeables pour la pâtisserie",
    "productIds": [
      "kit-tareas-pasteleria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Les coûts de revient par pièce avec le coût horaire de l'atelier m'ont ouvert les yeux. J'ai découvert que certaines préparations complexes n'étaient pas rentables malgré de bonnes ventes. Nous les avons redessinées avec Pâtisserie Créative en simplifiant le processus sans perdre en qualité et avons augmenté la marge de 6 points.",
    "testimonialAuthor": "Eva Mata",
    "testimonialRole": "Propriétaire, pâtisserie artisanale avec atelier propre",
    "faqTitle": "Questions fréquentes des pâtisseries",
    "faqs": [
      {
        "q": "Convient-il pour un atelier artisanal petit ou grand ?",
        "a": "Pour les deux. Les modèles évoluent d'un atelier familial de 2 personnes à une production industrielle. Il y a des clients avec un et avec six pâtissiers."
      },
      {
        "q": "Couvre-t-il la boulangerie en plus de la pâtisserie ?",
        "a": "Oui. Boulangerie Créative + Fermentus Avec AI+ couvrent la boulangerie artisanale et le levain professionnel pour les ateliers mixtes."
      },
      {
        "q": "Y a-t-il un contrôle du coût horaire d'atelier ?",
        "a": "Oui. Coût horaire d'atelier intégré dans le coût de revient du Kit de Escandallos Pro : une préparation complexe avec 3 heures de travail par pièce a son coût réel reflété."
      },
      {
        "q": "Génère-t-il du contenu pour la vitrine et les réseaux ?",
        "a": "Oui. GastroIMG Gen+ pour les photos de vitrine + Pinterest Pins Gen + InstaFlow AI Pro + MenuDish Local SEO pour attirer des clients locaux."
      },
      {
        "q": "Comment m'aide-t-il avec la saisonnalité ?",
        "a": "Gastro Calendar planifie les saisons clés (couronne des Rois, Saint-Valentin, Pâques, Noël, communions) à l'avance et un plan financier adapté aux pics de production."
      }
    ],
    "ctaTitle": "Votre atelier avec une marge claire et un branding professionnel.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour la Pâtisserie et l'Atelier : Coûts de revient, Saisonnalité et Branding | AI Chef Pro",
      "description": "Suite d'IA pour pâtisseries artisanales : Pâtisserie Créative, coûts de revient par pièce avec coût horaire d'atelier, APPCC, planification saisonnière et branding. Commencez aujourd'hui.",
      "keywords": "IA pâtisserie, logiciel atelier, coûts de revient pâtisserie, pâtisserie artisanale IA, levain pâtisserie, couronne des Rois Noël, pâtisserie Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/pasteleria-obrador.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre atelier dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous racontez quel type de pâtisserie vous exploitez (artisanale, industrielle, pâtisserie de restaurant, atelier mixte), la taille de l'équipe, la ville et la spécialité. Chaque agent — de Pâtisserie Créative à Gastro Calendar — répond adapté à votre produit, marché et opération réelle.",
    "appsTitle": "Les agents IA que vous allez utiliser dans votre pâtisserie",
    "apps": [
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité culinaire",
        "description": "Agent spécialisé en pâtisserie professionnelle, desserts et gâteaux avec technique avancée."
      },
      {
        "name": "Chocolaterie Créative",
        "category": "Créativité culinaire",
        "description": "Pour bonbons, ganaches et combinaisons de chocolat."
      },
      {
        "name": "Boulangerie Créative",
        "category": "Créativité culinaire",
        "description": "Pour levain, brioche, croissants et boulangerie artisanale."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité culinaire",
        "description": "Fermentations, préferments et techniques avancées de boulangerie."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité culinaire",
        "description": "Développement de desserts avec recette + coût de revient CSV."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue Sosa pour les textures et la technique avancée."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue tSpoonLab pour les applications avancées."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et utilitaires",
        "description": "Données précises sur les pertes en atelier (façonnage, cuisson, vitrine)."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et utilitaires",
        "description": "Identification automatique des allergènes par pièce, critique en pâtisserie."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie gastronomique IA pour vitrine, web et réseaux."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest est le canal avec le plus de trafic organique stable pour la pâtisserie."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Planification saisonnière : couronne des Rois, Saint-Valentin, Pâques, Noël."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge après calcul des coûts de revient des pièces"
      },
      {
        "value": "×2",
        "label": "trafic organique via Pinterest"
      },
      {
        "value": "−30 %",
        "label": "pertes en atelier"
      },
      {
        "value": "12+",
        "label": "agents pour votre atelier"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Coûts de revient sans coût horaire d'atelier, préparations longues en perte sans le savoir",
        "Pertes en atelier et en vitrine sans traçabilité réelle",
        "Vitrine et réseaux sociaux improvisés sans continuité",
        "Production saisonnière réactive, sans anticipation ni planification",
        "APPCC sur papier imprimé dispersé dans l'atelier"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Coût de revient professionnel par pièce avec coût horaire d'atelier intégré",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ attirent un trafic stable",
        "Gastro Calendar planifie les saisons clés à l'avance",
        "APPCC depuis le mobile avec des enregistrements prêts pour l'inspection"
      ]
    },
    "galleryTitle": "Comment fonctionne une pâtisserie artisanale",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : vitrine, atelier, exposition des pièces, décoration, gâteaux et équipe.",
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
    "h1": "IA pour Bar et Mixologie",
    "heroSubtitle": "Concevez des cartes de cocktails signatures, chiffrez chaque verre avec vos prix réels et capturez un branding professionnel avec une suite d'agents IA conçus pour les barmans, les mixologues et les propriétaires de bar.",
    "heroTagline": "Votre bar avec une marge réelle, une mixologie technique",
    "badge": "Pour les bars à cocktails et les bars de mixologie",
    "painsTitle": "Ce Qu'un Bar à Cocktails Ne Peut Pas Se Permettre d'Ignorer",
    "pains": [
      "Chiffrer des cocktails complexes avec de nombreux ingrédients, infusions et techniques",
      "Pertes et casse de verrerie au bar qui saignent la rentabilité sans contrôle",
      "Des cartes de boissons qui changent selon les saisons avec une R&D continue",
      "Marge très serrée sur les spiritueux avec un coût des alcools premium volatil",
      "Se différencier dans une zone concurrentielle avec le storytelling et le branding visuel des cocktails",
      "Gérer une mixologie signature combinée à une brasserie, des vins et une carte de tapas"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide dans un Bar à Cocktails",
    "features": [
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Agent spécialisé dans les pubs, la mixologie, les caves à vin, les bars sportifs et les bars de nuit avec des connaissances professionnelles."
      },
      {
        "icon": "Sparkles",
        "title": "Food Pairing AI",
        "description": "Des combinaisons inattendues pour des cocktails signatures à base scientifique et des accords avec des tapas."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Fermentations pour cocktails avancés : kombuchas comme base, infusions, lactofermentations d'agrumes."
      },
      {
        "icon": "Calculator",
        "title": "Chiffrage par verre",
        "description": "Cuisine Créative fournit la recette + le chiffrage CSV ; le Kit de Escandallos Pro le gère avec vos prix réels et une marge professionnelle par cocktail."
      },
      {
        "icon": "BookOpen",
        "title": "Cartes de cocktails avec storytelling",
        "description": "Conception de carte et rotation saisonnière avec un storytelling professionnel pour la salle et la presse."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Modèles : préparation des jus, sirops, garnitures, infusions, mise en place du bar, service et nettoyage en profondeur."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC Bar",
        "description": "Traçabilité spécifique : jus frais, crèmes, conservation des garnitures, lavage de la verrerie."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie de cocktails avec IA + contenu Instagram avec un calendrier éditorial professionnel."
      },
      {
        "icon": "BookOpen",
        "title": "Agent Sosa Ingredients + Agent tSpoonLab",
        "description": "Assistants pour la sélection d'ingrédients techniques premium très utilisés en mixologie signature."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Bar à Cocktails avec AI Chef Pro",
    "workflow": [
      "11:00 · Ouverture — check-list Kit de Tareas Bar : préparation des jus, sirops, infusions et garnitures.",
      "14:00 · Bar & Lounge AI+ + Food Pairing AI — vous développez un nouveau cocktail pour la carte de printemps en gardant l'accord en tête.",
      "15:00 · Cuisine Créative fournit la recette + le chiffrage CSV ; le Kit de Escandallos Pro le gère avec vos prix réels (gin premium, sirops, garniture).",
      "16:00 · Test du cocktail avec l'équipe, ajustements finaux de l'équilibre et des proportions.",
      "17:00 · Pro Prompts eBook + BlogPost SEO Gen+ — vous rédigez le storytelling pour la nouvelle carte et la note pour la salle.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez la photographie et les posts Instagram pour le lancement.",
      "20:00 · Service du soir — bar coordonné, chiffrages validés, cocktails servis avec précision.",
      "02:30 · Fermeture — nettoyage en profondeur, HACCP signé, rapport des verres du jour."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Bar et Mixologie",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Avoir chaque cocktail chiffré et la carte prête en une matinée a changé ma façon de travailler. Avant, c'était à la calculatrice, sur une serviette et beaucoup d'intuition. Maintenant, avec Bar & Lounge AI+ et le Kit de Escandallos Pro, je sors une nouvelle carte avec une marge validée en 2 heures.",
    "testimonialAuthor": "Hugo Vázquez",
    "testimonialRole": "Barman et propriétaire, bar à cocktails signature",
    "faqTitle": "Questions Fréquentes des Barmans et des Mixologues",
    "faqs": [
      {
        "q": "Est-ce que ça convient à la mixologie signature ou décontractée ?",
        "a": "Pour les deux. Bar & Lounge AI+ + Food Pairing AI couvrent des cocktails classiques à la mixologie de pointe avec une technique professionnelle."
      },
      {
        "q": "Est-ce que ça couvre la brasserie et les vins en plus de la mixologie ?",
        "a": "Oui. Bar & Lounge AI+ couvre tout le spectre du bar : brasseries, caves à vin, bars de nuit, pubs traditionnels et bars sportifs."
      },
      {
        "q": "Est-ce que ça génère des idées de nouvelles boissons avec de la technique ?",
        "a": "Oui. Bar & Lounge AI+ + Cuisine Créative + Food Pairing AI + Fermentus Avec AI+ travaillent ensemble pour créer des cocktails à base professionnelle."
      },
      {
        "q": "Est-ce que ça fonctionne pour un bar d'hôtel ou un établissement indépendant ?",
        "a": "Les deux. Le bar du lobby d'hôtel se gère depuis le cas /usos/concepto/hotel-completo-fb ; le bar indépendant depuis ici."
      },
      {
        "q": "Comment est-ce que ça m'aide avec le branding visuel de mes cocktails ?",
        "a": "GastroIMG Gen+ génère des photographies professionnelles de chaque verre pour Instagram, le web et la carte. InstaFlow AI Pro programme le contenu avec un calendrier éditorial."
      }
    ],
    "ctaTitle": "Une mixologie avec une marge réelle et un branding professionnel.",
    "ctaSubtitle": "Commencez avec le parcours de bienvenue de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Bar et Mixologie : Cocktails Signatures, Chiffrages et Branding | AI Chef Pro",
      "description": "Suite IA pour bars et mixologie professionnelle : Bar & Lounge AI+, Food Pairing AI, chiffrages par cocktail, cartes, HACCP et branding visuel. Commencez aujourd'hui.",
      "keywords": "IA bar mixologie, chiffrage cocktail, logiciel bar, IA barman, IA mixologue, cocktail bar IA, bar signature Espagne, gestion mixologie IA",
      "ogImage": "https://aichef.pro/og/use-cases/bar-cocktails.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Bar dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », une intégration conversationnelle de 2 minutes où vous lui dites quel type de bar vous gérez (bar à cocktails, cave à vin, brasserie, pub, bar de nuit), la ville et la carte. Chaque agent — de Bar & Lounge AI+ au Kit de Escandallos Pro — répond en s'adaptant à votre style de bar et à votre marché.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser dans Votre Bar",
    "apps": [
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts Commerciaux",
        "description": "Agent principal : pubs, mixologie, caves à vin, bars sportifs, bars de nuit."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de cocktails avec recette + chiffrage CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Combinaisons scientifiques pour cocktails signatures et accords avec des tapas."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "Fermentations pour une mixologie avancée : kombuchas, infusions, lactofermentations."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts Commerciaux",
        "description": "Pour les bars avec une carte de tapas et une cuisine légère en plus de la mixologie."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Assistant pour les ingrédients techniques du catalogue Sosa."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue tSpoonLab pour la mixologie technique."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes dans les cocktails et les tapas."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises sur les pertes dans les jus, les garnitures et la verrerie."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie culinaire IA pour cocktails : web, réseaux sociaux et carte."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Contenu viral Instagram pour la mixologie avec calendrier éditorial."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Connaissance Gastro",
        "description": "300+ prompts pour le storytelling de cocktails, la communication presse et la formation."
      }
    ],
    "metrics": [
      {
        "value": "×4",
        "label": "vitesse de finalisation de la carte des cocktails"
      },
      {
        "value": "+5 pp",
        "label": "marge après chiffrage professionnel"
      },
      {
        "value": "×3",
        "label": "engagement Instagram avec GastroIMG"
      },
      {
        "value": "12+",
        "label": "agents pour votre bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Cocktails chiffrés à la calculatrice et sur une serviette",
        "Cartes de boissons sans storytelling professionnel pour la salle",
        "Pertes au bar et verrerie sans traçabilité",
        "Branding visuel improvisé sur Instagram avec des photos du téléphone",
        "Pas d'accès systématique aux tendances internationales de la mixologie"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Bar & Lounge AI+ + Cuisine Créative + Kit de Escandallos Pro finalisent les cartes en 2 heures",
        "Storytelling professionnel pour chaque cocktail prêt pour la salle et la presse",
        "Pertes contrôlées avec Rendement GenCal et des modèles spécifiques",
        "GastroIMG Gen+ + InstaFlow génèrent des photos professionnelles et des posts viraux",
        "Sonar Deep Research apporte des tendances et des références internationales"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Bar à Cocktails Professionnel",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : le bar principal, la technique du shaker, le cocktail final, la préparation des garnitures, la technique de coulage et le service.",
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
    "h1": "IA pour le traiteur et les événements",
    "heroSubtitle": "Établissez des fiches techniques par événement, planifiez la production à grande échelle, gérez la logistique et l'APPCC hors site avec une suite d'agents IA spécialisés dans le traiteur professionnel, les mariages, les événements d'entreprise et les cocktails.",
    "heroTagline": "Événements avec marge, sans chaos",
    "badge": "Pour les entreprises de traiteur et d'événements",
    "painsTitle": "Ce qu'un traiteur ne peut pas laisser de résoudre",
    "pains": [
      "Établir des fiches techniques de menus avec une forte variabilité d'invités (50, 200, 500) quand les prix changent chaque semaine",
      "Planifier la production et la mise en place à grande échelle depuis la cuisine centrale",
      "Coordonner la logistique, le transport réfrigéré et le montage sur le site du client",
      "Maintenir l'APPCC et la traçabilité hors du local fixe, sur des sites externes et dans les véhicules",
      "Attirer des clients d'entreprise avec des propositions professionnelles qui concluent des contrats à plus forte valeur",
      "Gérer simultanément plusieurs événements du week-end sans écarts"
    ],
    "featuresTitle": "Comment AI Chef Pro aide dans le traiteur et les événements",
    "features": [
      {
        "icon": "PartyPopper",
        "title": "Traiteur IA+",
        "description": "Agent spécialisé dans le traiteur et les événements gastronomiques : mariages, événements d'entreprise, cocktails et galas avec une connaissance professionnelle."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative + Food Pairing AI",
        "description": "Brainstorming pour les menus d'événement. Cuisine Créative livre une recette + fiche technique CSV prête pour le Kit de Escandallos Pro."
      },
      {
        "icon": "Calculator",
        "title": "Fiches techniques par événement",
        "description": "Kit de Escandallos Pro : vous chargez le CSV avec vos prix réels, ajustez le nombre d'invités et obtenez la marge instantanément."
      },
      {
        "icon": "Layers",
        "title": "Calcula Pax",
        "description": "Calculatrice de portions qui met à l'échelle les recettes à 50, 200, 500 ou 1000 convives en quelques secondes."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Catering",
        "description": "Modèles : production centrale, transport réfrigéré, montage sur site, service et démontage."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC hors du local",
        "description": "Traçabilité dans le transport, sur site externe et service externe avec des registres depuis le mobile."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Photographie gastronomique IA pour les propositions aux clients d'entreprise et la galerie d'événements."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Allergènes",
        "description": "Identification automatique critique pour les événements avec des profils alimentaires variés."
      },
      {
        "icon": "Search",
        "title": "BlogPost SEO Gen+ + Keyword Discovery AI+",
        "description": "Acquisition organique d'entreprises qui recherchent un traiteur dans votre zone."
      }
    ],
    "workflowTitle": "Une journée réelle dans une entreprise de traiteur avec AI Chef Pro",
    "workflow": [
      "08:30 · Traiteur IA+ — l'agent vous aide à finaliser le menu proposé pour un mariage de 180 invités selon le briefing du client.",
      "09:30 · Cuisine Créative — vous développez les 12 plats du menu avec recette et fiche technique CSV avec prix de référence.",
      "10:30 · Calcula Pax + Kit de Escandallos Pro — vous passez à l'échelle de 180 convives, chargez le CSV avec vos prix réels et validez la marge.",
      "12:00 · GastroIMG Gen+ — vous générez des photographies des plats pour les inclure dans la présentation au client.",
      "14:00 · Réunion avec le client — proposition finalisée avec une présentation professionnelle au lieu des modèles Word d'avant.",
      "16:00 · Kit de Tareas Catering — vous planifiez la production centrale, le transport, le montage et le service de l'événement de samedi.",
      "18:00 · Pack APPCC — vous préparez les registres de température pour le transport et la traçabilité sur site externe.",
      "20:00 · Brief à l'équipe — vous montez un brief de production, transport, montage et service à partir d'une source unique."
    ],
    "productsTitle": "Modèles et kits téléchargeables pour traiteur",
    "productIds": [
      "kit-tareas-catering",
      "kit-escandallos",
      "pack-appcc",
      "kit-plan-financiero",
      "kit-inventario",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Nous clôturons les événements en un tiers du temps. Les fiches techniques par événement s'ajustent en détail selon le nombre d'invités, les modèles logistiques sont en or et les propositions avec photographie professionnelle concluent des contrats d'entreprise qui nous échappaient auparavant. Marge +5 points au premier trimestre rien que grâce à une meilleure fiche technique.",
    "testimonialAuthor": "Sara Pérez",
    "testimonialRole": "Entreprise de traiteur corporatif et mariages (200 événements par an)",
    "faqTitle": "Questions fréquentes des entreprises de traiteur",
    "faqs": [
      {
        "q": "Convient-il pour un traiteur boutique ou grand ?",
        "a": "Pour les deux. Des traiteurs boutique de 50 invités par mois aux entreprises avec plus de 1000 services par mois et des événements de 2000 convives."
      },
      {
        "q": "Couvre-t-il les mariages, les événements d'entreprise et les cocktails ?",
        "a": "Oui. Traiteur IA+ et le Kit de Tareas Catering ont des modèles spécifiques pour les trois formats et pour les galas/événements spéciaux."
      },
      {
        "q": "Y a-t-il un APPCC spécifique hors du local fixe ?",
        "a": "Oui. Le Pack APPCC a des modèles adaptés au produit qui voyage en sac à dos, moto, fourgonnette réfrigérée ou cuisine centrale, y compris la traçabilité sur site externe."
      },
      {
        "q": "Génère-t-il des propositions commerciales pour les entreprises ?",
        "a": "Oui. Traiteur IA+ + GastroIMG Gen+ + Pro Prompts eBook permettent de rédiger des propositions professionnelles avec photographie gastronomique et storytelling."
      },
      {
        "q": "Comment m'aide-t-il à attirer des clients d'entreprise ?",
        "a": "BlogPost SEO Gen+ + Keyword Discovery AI+ + MenuDish Local SEO travaillent ensemble pour attirer des entreprises qui recherchent un traiteur dans votre zone via les recherches organiques sur Google."
      }
    ],
    "ctaTitle": "Traiteur avec une vraie marge et sans chaos.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour le traiteur et les événements : mariages, événements d'entreprise et cocktails | AI Chef Pro",
      "description": "Suite IA pour les entreprises de traiteur professionnel : Traiteur IA+, fiches techniques par événement, production à grande échelle, APPCC hors site et propositions commerciales. Commencez aujourd'hui.",
      "keywords": "IA traiteur, logiciel traiteur, fiches techniques événements, gestion traiteur IA, traiteur mariages IA, traiteur corporatif IA, événements gastronomiques logiciel, traiteur Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/catering-eventos.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre traiteur dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous lui expliquez quel type de traiteur vous opérez (mariages, événements d'entreprise, cocktails, galas), la taille moyenne, la ville et le volume annuel. Chaque agent — du Traiteur IA+ au Kit Plan Financiero — répond adapté à votre type d'événement, à votre échelle et à votre marché réel.",
    "appsTitle": "Les agents IA que vous allez utiliser dans votre traiteur",
    "apps": [
      {
        "name": "Traiteur IA+",
        "category": "Concepts d'entreprise",
        "description": "Agent principal : mariages, événements d'entreprise, cocktails et galas avec une base professionnelle."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité culinaire",
        "description": "Développement de menus d'événement avec recette + fiche technique CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité culinaire",
        "description": "Combinaisons d'ingrédients et accords pour cocktails et canapés."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité culinaire",
        "description": "Desserts d'événement et de banquet avec une technique professionnelle."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité culinaire",
        "description": "Pour des canapés avant-gardistes avec des ferments et des techniques innovantes."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et utilitaires",
        "description": "Calculatrice de portions qui met à l'échelle les recettes à 50, 200 ou 500 convives."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et utilitaires",
        "description": "Identification des allergènes critique dans les événements avec de nombreux invités."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et utilitaires",
        "description": "Données précises pour une production à l'échelle industrielle."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et réseaux sociaux",
        "description": "Articles de blog pour attirer des entreprises via les recherches organiques."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et réseaux sociaux",
        "description": "Descriptions SEO pour améliorer le positionnement du site web du traiteur."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance gastronomique",
        "description": "Photographie gastronomique IA pour les propositions et la galerie web."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs gastro",
        "description": "Pour les ingrédients techniques dans les cocktails et canapés."
      }
    ],
    "metrics": [
      {
        "value": "×3",
        "label": "vitesse de clôture des propositions"
      },
      {
        "value": "+5 pp",
        "label": "marge après fiche technique réelle"
      },
      {
        "value": "−50 %",
        "label": "temps en logistique"
      },
      {
        "value": "11+",
        "label": "agents pour votre traiteur"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Finaliser le menu avec le client : une demi-journée avec une calculatrice",
        "Production pour 200 invités sans mise à l'échelle précise",
        "APPCC hors du local improvisé",
        "Propositions avec des modèles Word et des photos de stock",
        "Brief à l'équipe sur des feuilles volantes"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Finaliser le menu en 30 minutes avec une marge validée",
        "Production mise à l'échelle avec Calcula Pax et Rendement GenCal",
        "APPCC avec traçabilité dans le transport et sur site externe",
        "Propositions avec GastroIMG Gen+ et storytelling professionnel",
        "Brief centralisé avec Kit de Tareas Catering"
      ]
    },
    "galleryTitle": "Comment fonctionne un traiteur professionnel",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : production centrale, événements élégants, canapés, cocktails d'entreprise, montage et service.",
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
    "h1": "IA pour hôtel complet (F&B + Housekeeping)",
    "heroSubtitle": "Gérez les petits-déjeuners, le restaurant, le room service, les banquets, le bar et le housekeeping avec une suite d'agents IA conçus pour les F&B Managers et les directions d'hôtel.",
    "heroTagline": "Toute l'exploitation hôtelière coordonnée dans un système unique",
    "badge": "Pour les F&B Managers d'hôtel",
    "painsTitle": "Ce qu'un F&B Manager d'hôtel ne peut pas laisser de côté",
    "pains": [
      "Coordonner plusieurs points de vente à la fois : petit-déjeuner buffet, restaurant à la carte, bar lobby, room service et banquets",
      "Gérer de grandes équipes avec des horaires rotatifs 24/7 en respectant la convention collective et les repos",
      "Maintenir l'APPCC réparti dans plusieurs zones de cuisine avec consolidation vers le F&B Director",
      "Reporting consolidé au directeur de l'hôtel et au corporate avec des KPI par ligne de F&B",
      "Concevoir des cartes saisonnières pour plusieurs points de vente sans que l'équipe se noie dans la paperasse",
      "Gérer les banquets de mariage et les événements d'entreprise en les conciliant avec le F&B régulier"
    ],
    "featuresTitle": "Comment AI Chef Pro aide dans un hôtel complet",
    "features": [
      {
        "icon": "Hotel",
        "title": "Kit de Tareas Hotel",
        "description": "Modèles spécifiques pour le petit-déjeuner buffet, le restaurant, le bar lobby, le room service, les banquets et le housekeeping dans un système documentaire unique."
      },
      {
        "icon": "ChefHat",
        "title": "Chef Exécutif Pro",
        "description": "Standardisation des recettes et des fiches techniques dans tous les points de vente de l'hôtel. Même plat, même qualité au restaurant, au room service et au banquet."
      },
      {
        "icon": "Calculator",
        "title": "Rendements par point de vente",
        "description": "Cuisine Créative fournit la recette + le rendement CSV ; Kit de Escandallos Pro le gère avec vos prix réels en séparant la marge par point de vente."
      },
      {
        "icon": "PartyPopper",
        "title": "Traiteur IA+",
        "description": "Pour la conception et la production de banquets de mariage, d'événements d'entreprise et d'événements spéciaux de l'hôtel."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Pour la mixologie du bar lobby, les vins du restaurant et les spiritueux avec un rendement professionnel."
      },
      {
        "icon": "Users",
        "title": "Kit Gestión de Personal",
        "description": "Plannings pour grandes équipes 24/7 avec horaires rotatifs respectant la convention collective du pays. Repas du Personnel inclus."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC corporatif",
        "description": "APPCC réparti par zone de cuisine mais consolidé dans un tableau de bord unique pour le F&B Director."
      },
      {
        "icon": "BarChart3",
        "title": "Kit Plan Financiero",
        "description": "Tableau de bord avec des KPI par point de vente : petit-déjeuner, restaurant, bar, room service, banquets. Ratios d'occupation et de productivité."
      },
      {
        "icon": "BriefcaseBusiness",
        "title": "Manager de Restaurant Pro",
        "description": "Pour les managers de chaque point de vente avec un reporting consolidé vers le F&B Manager de l'hôtel."
      }
    ],
    "workflowTitle": "Une journée réelle d'un F&B Manager d'hôtel avec AI Chef Pro",
    "workflow": [
      "07:00 · Ouverture du petit-déjeuner — l'équipe démarre le buffet avec la checklist du Kit de Tareas Hotel ; vous consultez le tableau de bord d'occupation de l'hôtel et ajustez la mise en place.",
      "09:30 · Traiteur IA+ — vous préparez le banquet de mariage de samedi prochain : menu, rendement et production pour 220 invités.",
      "11:00 · Chef Exécutif Pro — vous mettez à jour la fiche technique du nouveau plat du restaurant et elle se réplique au room service et au menu de banquet avec la même standardisation.",
      "13:00 · Service de midi — restaurant à la carte + bar lobby + room service actifs. L'équipe coordonne avec des modèles spécifiques à chaque point de vente.",
      "15:30 · Kit Plan Financiero — vous exportez les KPI par point de vente du trimestre pour la réunion avec la direction de l'hôtel.",
      "17:00 · Bar & Lounge AI+ — vous concevez la nouvelle carte de cocktails pour le bar lobby avec un rendement professionnel.",
      "19:30 · Planning semaine prochaine — Kit Gestión de Personal avec des horaires rotatifs respectant la convention collective, contrôle des heures et repas du personnel généré.",
      "23:00 · APPCC consolidé — enregistrements des 6 points de vente signés et exportés, rapport au F&B Director et au corporate envoyé en PDF."
    ],
    "productsTitle": "Modèles et Kits téléchargeables pour hôtels",
    "productIds": [
      "kit-tareas-hotel",
      "kit-escandallos",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Coordonner 6 points de vente F&B dans un hôtel de 200 chambres était un cauchemar constant. AI Chef Pro a tout organisé pour nous. Le Kit de Tareas Hotel est en or et le reporting au directeur de l'hôtel est désormais automatique en PDF. Nous avons augmenté le RevPASH du restaurant de 12 % en 4 mois simplement grâce à un meilleur contrôle.",
    "testimonialAuthor": "Cristina Núñez",
    "testimonialRole": "F&B Manager, hôtel 4 étoiles avec 200 chambres",
    "faqTitle": "Questions fréquentes des F&B Managers",
    "faqs": [
      {
        "q": "Fonctionne-t-il pour un hôtel boutique ou une grande chaîne ?",
        "a": "Les deux. Les modèles évoluent des hôtels de 30 chambres aux chaînes avec des centaines de propriétés. Il existe un onboarding entreprise pour les grandes chaînes."
      },
      {
        "q": "Couvre-t-il le housekeeping en plus du F&B ?",
        "a": "Oui. Le Kit de Tareas Hotel inclut des modèles spécifiques de housekeeping en plus des 5 points de vente F&B."
      },
      {
        "q": "S'intègre-t-il avec notre PMS ou Opera ?",
        "a": "Il exporte Excel, PDF et CSV compatibles avec la plupart des PMS et systèmes hôteliers. Les données peuvent être intégrées manuellement à la clôture de chaque service ou journée."
      },
      {
        "q": "Existe-t-il un plan entreprise pour les chaînes hôtelières ?",
        "a": "Oui. À partir d'un certain nombre de propriétés, il existe des plans entreprise avec onboarding personnalisé, tableaux de bord consolidés par chaîne et support prioritaire."
      },
      {
        "q": "Comment gère-t-il les banquets et les événements spéciaux ?",
        "a": "Traiteur IA+ est intégré au Kit Tareas Hotel pour que les banquets (mariages, événements d'entreprise) se concilient avec le F&B régulier sans collision de production ni d'équipe."
      },
      {
        "q": "Et le contrôle des coûts par point de vente ?",
        "a": "Le Kit Plan Financiero permet d'analyser le food cost, la productivité et la marge séparément pour le petit-déjeuner, le restaurant, le bar lobby, le room service et les banquets. Cela donne une vision réelle de quel point de vente est rentable et lequel ne l'est pas."
      }
    ],
    "ctaTitle": "Votre F&B hôtelier coordonné et sans chaos.",
    "ctaSubtitle": "Parlez-nous pour un onboarding personnalisé ou commencez avec le plan Membre : 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "IA pour hôtel complet (F&B + Housekeeping) : Restaurant, Bar, Banquets | AI Chef Pro",
      "description": "Suite IA pour les F&B Managers d'hôtel : petit-déjeuner buffet, restaurant, bar lobby, room service, banquets et housekeeping avec des agents spécialisés. Commencez dès aujourd'hui.",
      "keywords": "IA hôtel F&B, F&B Manager IA, logiciel F&B hôtel, gestion hôtel IA, room service IA, banquet hôtel IA, housekeeping logiciel, gestion restaurant hôtel IA, F&B Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/hotel-completo.jpg"
    },
    "personalizationTitle": "Personnalisé à votre hôtel dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous lui expliquez quel type d'hôtel vous gérez (boutique, 4 étoiles, grande chaîne, tout inclus), le nombre de chambres, quels points de vente F&B vous exploitez et à quelle échelle. À partir de ce moment, chaque agent — du Chef Exécutif Pro au Plan Financier — répond en s'adaptant à la réalité de votre hôtel : type de client, taux d'occupation et opérations réelles. Ce n'est pas un formulaire : c'est une conversation courte qui rend la suite véritablement utile pour un F&B Manager d'hôtel.",
    "appsTitle": "Les agents IA que vous allez utiliser en tant que F&B Manager",
    "apps": [
      {
        "name": "Chef Exécutif Pro",
        "category": "Gastro Profile Pro",
        "description": "Standardisation des recettes et des fiches techniques dans tous les points de vente de l'hôtel."
      },
      {
        "name": "Manager de Restaurant Pro",
        "category": "Gastro Profile Pro",
        "description": "Assistant pour les managers de chaque point de vente avec un reporting consolidé au F&B Manager."
      },
      {
        "name": "Traiteur IA+",
        "category": "Concepts d'entreprise",
        "description": "Pour les banquets de mariage, les événements d'entreprise et les galas de l'hôtel."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'entreprise",
        "description": "Pour la mixologie du bar lobby, les vins du restaurant et les spiritueux."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'entreprise",
        "description": "Pour le restaurant à la carte de l'hôtel et les options décontractées du room service."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité culinaire",
        "description": "Développement de plats pour tous les points de vente avec recette + rendement CSV."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité culinaire",
        "description": "Desserts d'hôtel : petit-déjeuner buffet, restaurant, room service et banquets."
      },
      {
        "name": "Repas du Personnel",
        "category": "Gastro Profile Pro",
        "description": "Générateur de menus pour le personnel des grandes équipes 24/7."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et utilitaires",
        "description": "Identification automatique des allergènes par recette, essentielle dans les hôtels internationaux."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et utilitaires",
        "description": "Données précises sur les pertes et les rendements pour un contrôle multi-points de vente."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie gastronomique pour le site web de l'hôtel, le menu du room service et les banquets."
      }
    ],
    "metrics": [
      {
        "value": "+12 %",
        "label": "RevPASH en 4 mois"
      },
      {
        "value": "6",
        "label": "points de vente coordonnés"
      },
      {
        "value": "×5",
        "label": "vitesse de reporting au directeur"
      },
      {
        "value": "11+",
        "label": "agents pour votre hôtel"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "6 points de vente F&B avec 6 systèmes différents : petit-déjeuner, restaurant, bar, room service, banquets et housekeeping déconnectés",
        "APPCC sur papier imprimé dispersé dans chaque cuisine de l'hôtel, problème lors des inspections",
        "Les banquets de mariage entrent en collision avec la production du restaurant régulier et du room service",
        "Reporting au F&B Director et au corporate avec des fichiers dispersés et sans structure",
        "Plannings 24/7 construits manuellement dans Excel avec 50+ employés"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Kit de Tareas Hotel avec des modèles spécifiques par point de vente, tout coordonné dans un système unique",
        "APPCC consolidé dans un tableau de bord : enregistrements depuis mobile, prêt pour l'inspection et pour le corporate",
        "Banquets intégrés avec Traiteur IA+ qui respecte la production du F&B régulier",
        "Reporting au directeur et au corporate en PDF directement depuis le Kit Plan Financiero",
        "Plannings avec Kit Gestión de Personal : horaires 24/7 respectant la convention collective sans erreurs"
      ]
    },
    "galleryTitle": "Comment fonctionne le F&B d'un hôtel complet",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : restaurant, petit-déjeuner buffet, banquet, bar lobby, room service et briefing F&B avec la cuisine.",
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
    "h1": "IA pour Glacier Artisanal",
    "heroSubtitle": "Coût de revient par parfum avec coût réel du lait, des fruits et des fruits secs, planifiez la production saisonnière et capturez un branding professionnel avec une suite d'agents IA spécialisés en glacerie artisanale.",
    "heroTagline": "Glace avec une vraie marge et sans paperasse",
    "badge": "Pour les glaciers et gelaterias artisanaux",
    "painsTitle": "Ce qu'un Glacier Artisanal Ne Peut Pas Ignorer",
    "pains": [
      "Coûts de revient complexes avec lait, crème, fruits frais, fruits secs et pâtes professionnelles nécessitant un calcul par kg et par boule",
      "Pertes élevées à l'atelier (turbine, refroidissement rapide) et en vitrine (exposition prolongée, rotation) sans contrôle réel",
      "Traçabilité APPCC avec produits sensibles : lait, œuf dans certaines bases, fruits secs avec allergènes et températures critiques",
      "Saisonnalité extrême : haute saison de mai à septembre, creux hivernal à rentabiliser avec gâteaux et desserts",
      "Se différencier dans une zone concurrentielle avec des parfums propres, un branding visuel de vitrine, packaging et réseaux sociaux",
      "Capturer les commandes de gâteaux glacés et desserts sur mesure avec marge tout en gérant le quotidien du service"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide le Glacier Artisanal",
    "features": [
      {
        "icon": "IceCream",
        "title": "Glacerie Créative",
        "description": "Agent spécialisé en glacerie artisanale : bases blanche, jaune, fruit, sorbets, équilibrage des sucres, solides et matières grasses pour une texture optimale."
      },
      {
        "icon": "Cake",
        "title": "Pâtisserie Créative",
        "description": "Pour gâteaux glacés, semifreddos, desserts à la cuillère et combinaisons glace + génoise qui augmentent le ticket moyen en creux hivernal."
      },
      {
        "icon": "Cookie",
        "title": "Chocolaterie Créative",
        "description": "Pour glaçages, chocolats glacés, pralinés et combinaisons avancées glace + chocolat."
      },
      {
        "icon": "Calculator",
        "title": "Coûts de revient par parfum",
        "description": "La Glacerie Créative fournit la recette + le coût de revient CSV avec équilibre technique (sucres, solides, matières grasses) ; le Kit de Escandallos Pro le gère avec marge réelle par kg, par boule et par cornet."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Heladería",
        "description": "Modèles : préparation turbine, refroidissement rapide, réassort vitrine, contrôle des températures, rotation des parfums, fermeture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC glacier",
        "description": "Traçabilité du lait, des fruits frais, des fruits secs avec allergènes et températures critiques en chambre froide, turbine et vitrine."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification saisonnière avec pics clés : Fête des Mères, printemps, été, Saint-Valentin et gâteaux glacés de Noël. Calendrier éditorial pour la vitrine."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie gastronomique IA + contenu Instagram : le glacier artisanal vit de l'impact visuel des bacs et des cornets."
      },
      {
        "icon": "BarChart3",
        "title": "Agent Sosa Ingredients",
        "description": "Assistant du catalogue Sosa pour textures professionnelles, neutres, stabilisants et pâtes concentrées pour glacerie."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Glacier Artisanal avec AI Chef Pro",
    "workflow": [
      "07:00 · Ouverture — checklist Kit de Tareas Heladería : vérification de la chambre froide, refroidissement rapide des mélanges préparés la veille, préparation de la turbine à glace.",
      "08:30 · Glacerie Créative — vous développez un nouveau parfum de saison (fruits rouges au balsamique). Cuisine Créative fournit la recette + le coût de revient CSV avec équilibre technique.",
      "09:30 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels des fruits de saison et du lait local, validez la marge par kg et par boule.",
      "11:00 · Production du jour — vous passez les mélanges à la turbine, vous refroidissez à -18 °C, vous étiquetez avec l'APPCC.",
      "13:30 · Réassort de la vitrine avec étiquettes professionnelles, contrôle des pertes d'exposition par parfum.",
      "16:00 · Pâtisserie Créative — vous développez un gâteau glacé pour la Fête des Mères avec un semifreddo aux pistaches, une base de génoise et un glaçage. Coût de revient CSV prêt.",
      "18:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence du nouveau parfum et les posts Instagram pour le lancement.",
      "21:00 · Fermeture — nettoyage en profondeur, APPCC signé, planification des mélanges à refroidir cette nuit pour demain."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Glacier",
    "productIds": [
      "kit-tareas-heladeria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Nous sommes passés de feuilles volantes à un système. Avec la Glacerie Créative, nous équilibrons sucres et solides avec un critère technique, et le Kit de Escandallos Pro me confirme la marge réelle par boule et par kg avec les prix actuels des fruits. Le rendement a chuté de 40 % en 3 mois et nous avons découvert que deux parfums historiques n'étaient pas rentables.",
    "testimonialAuthor": "Laura Costa",
    "testimonialRole": "Propriétaire, glacerie artisanale avec atelier de production propre",
    "faqTitle": "Questions Fréquentes des Glaciers",
    "faqs": [
      {
        "q": "Convient-il à une petite glacerie, une gelateria italienne ou une chaîne ?",
        "a": "Aux trois. Les modèles évoluent depuis la glacerie familiale à point de vente unique jusqu'à la chaîne avec plusieurs établissements et un atelier centralisé. La méthodologie est la même : recette équilibrée → coût de revient CSV → marge réelle."
      },
      {
        "q": "Couvre-t-il l'équilibrage technique des bases (sucres, solides, matières grasses) ?",
        "a": "Oui. La Glacerie Créative raisonne comme un glacier professionnel : équilibre des sucres avec saccharose, dextrose et sucre inverti ; solides totaux et matières grasses selon la norme technique ; équilibre pour éviter la cristallisation et maintenir l'onctuosité."
      },
      {
        "q": "Comment gérons-nous la forte saisonnalité de la glacerie ?",
        "a": "Gastro Calendar planifie à l'avance les pics (Fête des Mères, été, Saint-Valentin, Noël avec gâteaux glacés) et le creux hivernal avec gâteaux, semifreddos et desserts à la cuillère pour maintenir le ticket moyen. Le Kit Plan Financiero projette le cash flow saisonnier réaliste."
      },
      {
        "q": "Y a-t-il un contrôle des pertes à l'atelier et en vitrine ?",
        "a": "Oui. Rendement GenCal fournit des données par processus (turbine, refroidissement rapide, exposition prolongée en vitrine, rotation des parfums). Elles sont intégrées au coût de revient du Kit de Escandallos Pro pour que le coût réel reflète les pertes, pas seulement l'ingrédient brut."
      },
      {
        "q": "Génère-t-il du contenu pour la vitrine, les réseaux et Google Maps ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles pour chaque parfum, pour la vitrine, le web et les réseaux ; InstaFlow AI Pro programme Instagram avec calendrier éditorial ; MenuDish Local SEO capte les clients locaux qui cherchent « glacier près de chez moi ». Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre bac et votre vrai dressage."
      }
    ],
    "ctaTitle": "Votre glacier avec une marge claire et un branding professionnel.",
    "ctaSubtitle": "Commencez par l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Glacier Artisanal : Coûts de Revient par Parfum, Saisonnalité et Branding | AI Chef Pro",
      "description": "Suite IA pour glaciers artisanaux : Glacerie Créative, coûts de revient par parfum avec équilibre technique, APPCC, planification saisonnière et branding visuel. Commencez dès aujourd'hui.",
      "keywords": "IA glacier, logiciel glacier, coût de revient glace, glacerie artisanale IA, équilibre technique glace, gelateria IA, glacier Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/heladeria.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Glacier dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous expliquez quel type de glacier vous exploitez (gelateria italienne, glacerie artisanale espagnole, glacier avec atelier de production propre ou sans atelier, mixte avec pâtisserie), la taille de l'équipe, la ville et le style. Chaque agent — de la Glacerie Créative à Gastro Calendar — répond de manière adaptée à votre produit, votre marché et votre réalité opérationnelle.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Glacier",
    "apps": [
      {
        "name": "Glacerie Créative",
        "category": "Créativité Culinaire",
        "description": "Agent spécialisé en glacerie artisanale avec équilibrage technique des bases, sucres, solides et matières grasses."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Gâteaux glacés, semifreddos, desserts à la cuillère et combinaisons glace + génoise."
      },
      {
        "name": "Chocolaterie Créative",
        "category": "Créativité Culinaire",
        "description": "Glaçages, chocolats glacés, pralinés et combinaisons avancées avec chocolat."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de parfums et recettes avec recette + coût de revient CSV."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa : neutres, stabilisants, pâtes concentrées et textures professionnelles."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données précises des pertes en turbine, refroidissement rapide et exposition en vitrine."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par parfum : produits laitiers, fruits secs, gluten, œuf."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie gastronomique IA de référence pour vitrine, web et réseaux sociaux."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial : le glacier vit de l'impact visuel."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Capter les clients locaux qui cherchent « glacier près de chez moi » sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Planification saisonnière : Fête des Mères, été, Saint-Valentin, gâteaux glacés de Noël."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capte un trafic organique stable pour les gâteaux glacés et semifreddos."
      }
    ],
    "metrics": [
      {
        "value": "+5 pts",
        "label": "de marge après avoir établi les coûts de revient des parfums"
      },
      {
        "value": "−40 %",
        "label": "de pertes à l'atelier et en vitrine"
      },
      {
        "value": "×3",
        "label": "d'engagement Instagram avec GastroIMG"
      },
      {
        "value": "12+",
        "label": "agents pour votre glacier"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Coûts de revient sans équilibre technique, parfums qui cristallisent ou perdent leur onctuosité sans savoir pourquoi",
        "Pertes en turbine, refroidissement rapide et vitrine sans traçabilité réelle",
        "Vitrine et réseaux sociaux improvisés : photos au téléphone, sans continuité",
        "Saisonnalité réactive : l'hiver fait chuter le ticket sans alternatives",
        "APPCC sur papier imprimé dispersé dans l'atelier"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Coûts de revient professionnels par parfum avec équilibre technique et marge réelle par boule et par kg",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques à la glacerie",
        "GastroIMG Gen+ + InstaFlow AI Pro génèrent un contenu visuel stable et professionnel",
        "Gastro Calendar planifie pics et creux avec gâteaux glacés, semifreddos et desserts à la cuillère",
        "APPCC depuis le mobile avec enregistrements prêts pour l'inspection"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Glacier Artisanal",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : vitrine, turbine à glace, atelier de production, parfums, cornets et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour la Chocolaterie et la Confiserie",
    "heroSubtitle": "Calcul de coût par chocolat avec coût réel du cacao et coût horaire d'atelier, planifiez la production saisonnière et capturez un branding professionnel avec une suite d'agents IA spécialisés en chocolaterie artisanale.",
    "heroTagline": "Un chocolat avec une marge réelle et sans paperasse",
    "badge": "Pour les chocolateries et confiseries artisanales",
    "painsTitle": "Ce qu'une Chocolaterie Doit Absolument Résoudre",
    "pains": [
      "Cacao au prix volatil qui change le coût réel chaque semaine sans prévenir et oblige à recalculer constamment les calculs de coût",
      "Pertes à l'atelier (tempérage raté, moules mal pris, chutes) et en vitrine (rotation, exposition prolongée)",
      "Saisonnalité extrême : Noël, Saint-Valentin, Pâques, Roscón concentrent un pourcentage élevé du chiffre d'affaires annuel",
      "Traçabilité APPCC avec un produit délicat : cacao, produits laitiers, fruits à coque, alcools et températures critiques à chaque étape",
      "Se différencier dans une zone concurrentielle avec des chocolats d'auteur, un packaging premium et un storytelling visuel de marque",
      "Attirer les commandes d'entreprise et les mariages avec marge tout en gérant la chocolaterie au quotidien"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide en Chocolaterie",
    "features": [
      {
        "icon": "Cookie",
        "title": "Chocolaterie Créative",
        "description": "Agent spécialisé en chocolaterie professionnelle : chocolats, ganaches, pralinés, tablettes, couvertures et technique de tempérage."
      },
      {
        "icon": "Cake",
        "title": "Pâtisserie Créative",
        "description": "Pour les desserts au chocolat, les bouchées, les brownies et les combinaisons avancées chocolat + pâtisserie qui diversifient le catalogue."
      },
      {
        "icon": "Calculator",
        "title": "Calculs de coût par pièce avec coût horaire d'atelier",
        "description": "Chocolaterie Créative fournit recette + fiche technique CSV ; Kit de Escandallos Pro le gère avec coût horaire d'atelier intégré dans la marge réelle par chocolat et par boîte."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Chocolatería",
        "description": "Modèles : tempérage, moulage, remplissage à la ganache, assemblage, packaging, contrôle des températures en chambre."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC chocolaterie",
        "description": "Traçabilité du cacao, des produits laitiers, des fruits à coque, des alcools et conservation professionnelle avec courbes de tempérage documentées."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification saisonnière avec dates clés : Noël, Saint-Valentin, Pâques, Roscón, Fête des Mères. Calendrier éditorial pour la vitrine."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Photographie gastronomique IA + Pinterest, où la chocolaterie premium capte un trafic organique stable."
      },
      {
        "icon": "BarChart3",
        "title": "Agent Sosa Ingredients",
        "description": "Assistant du catalogue Sosa pour les couvertures techniques, les pâtes concentrées, les fruits à coque et les arômes professionnels."
      },
      {
        "icon": "Sparkles",
        "title": "Rendement GenCal",
        "description": "Données précises sur les pertes par processus (tempérage, moulage, chutes, exposition en vitrine) intégrées dans le calcul de coût."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans une Chocolaterie avec AI Chef Pro",
    "workflow": [
      "07:00 · Ouverture — checklist Kit de Tareas Chocolatería : vérification de la chambre, pré-cristallisation du chocolat de couverture, préparation des moules.",
      "08:30 · Chocolaterie Créative — vous développez un nouveau chocolat pour la Saint-Valentin avec une ganache framboise et vanille. Cuisine Créative fournit recette + fiche technique CSV.",
      "09:30 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels du cacao et le coût horaire d'atelier intégré, vous validez la marge par chocolat et par boîte de 12.",
      "11:00 · Production du jour — tempérage sur marbre, moulage, remplissage de ganache à la poche à douille, refroidissement rapide et démoulage.",
      "14:00 · Réassort de la vitrine avec des boîtes professionnelles et des étiquettes, contrôle des pertes d'exposition.",
      "16:00 · Gastro Calendar — vous préparez la planification de production de Noël (coffrets cadeaux d'entreprise avec 8 semaines d'avance).",
      "18:00 · GastroIMG Gen+ + Pinterest Pins Gen — vous générez des photos de référence du nouveau chocolat et des épingles optimisées pour Pinterest.",
      "20:00 · Fermeture — nettoyage en profondeur, APPCC signé, planification des mélanges à refroidir cette nuit."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Chocolaterie",
    "productIds": [
      "kit-tareas-chocolateria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Produire 12 000 chocolats pour Noël sans système, c'était le chaos. Avec Chocolaterie Créative pour le design, Kit de Escandallos Pro pour une marge réelle avec cacao actualisé et Gastro Calendar pour la planification saisonnière, nous avons sauvé la saison et augmenté la marge de 7 points. Les coffrets d'entreprise se concluent désormais en un appel avec une proposition professionnelle.",
    "testimonialAuthor": "Mónica Salazar",
    "testimonialRole": "Maître chocolatière et propriétaire",
    "faqTitle": "Questions Fréquentes des Chocolateries",
    "faqs": [
      {
        "q": "Est-ce que ça convient à une petite chocolaterie artisanale ou à une chaîne ?",
        "a": "Pour les deux. Les modèles évoluent d'un atelier familial de 2 personnes à une production pour plusieurs points de vente. La méthodologie est la même : recette → fiche technique CSV → marge réelle avec coût horaire d'atelier."
      },
      {
        "q": "Est-ce que ça couvre la confiserie, les tablettes, les couvertures et les pralinés ?",
        "a": "Oui. Chocolaterie Créative raisonne comme un chocolatier professionnel : tempérage de couverture par courbes, ganaches avec équilibre eau-grasse, pralinés avec torréfaction des fruits à coque, tablettes fourrées avec technique de cristallisation."
      },
      {
        "q": "Comment gérons-nous le prix volatil du cacao ?",
        "a": "Kit de Escandallos Pro recalcule instantanément la marge réelle lorsque vous mettez à jour le prix de la couverture. Rendement GenCal ajoute le coût des pertes par processus. Ainsi, la marge reflète toujours le coût actuel, pas celui d'il y a trois mois."
      },
      {
        "q": "Est-ce que ça génère du contenu pour la vitrine, les réseaux et le packaging ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles de chaque chocolat pour la vitrine, le web et les réseaux ; Pinterest Pins Gen + InstaFlow AI Pro programment du contenu visuel ; MenuDish Local SEO capte les clients locaux. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre chocolat réellement dressé."
      },
      {
        "q": "Comment ça m'aide avec la forte saisonnalité ?",
        "a": "Gastro Calendar planifie les saisons clés (Noël, Saint-Valentin, Pâques, Roscón, Fête des Mères) avec 8 à 12 semaines d'avance. Le Kit Plan Financiero projette un cash flow saisonnier réaliste pour que vous arriviez à chaque pic avec la production et la trésorerie nécessaires."
      }
    ],
    "ctaTitle": "Votre chocolaterie avec une marge claire et un branding professionnel.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour la Chocolaterie et la Confiserie : Calculs de coût, Saisonnalité et Branding | AI Chef Pro",
      "description": "Suite d'IA pour chocolateries artisanales : Chocolaterie Créative, calculs de coût par chocolat avec coût horaire d'atelier, APPCC, planification saisonnière et branding. Commencez aujourd'hui.",
      "keywords": "IA chocolaterie, logiciel chocolaterie, calcul de coût chocolat, chocolaterie artisanale IA, technique tempérage, confiserie Espagne, planification Noël chocolaterie",
      "ogImage": "https://aichef.pro/og/use-cases/chocolateria.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Chocolaterie dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes dans lequel vous lui racontez quel type de chocolaterie vous exploitez (artisanale, confiserie d'auteur, chocolaterie avec café, atelier pour la vente aux professionnels de l'hôtellerie-restauration), la taille de l'équipe, la ville et la spécialité. Chaque agent — de Chocolaterie Créative à Gastro Calendar — répond adapté à votre produit, votre marché et votre fonctionnement réel.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Chocolaterie",
    "apps": [
      {
        "name": "Chocolaterie Créative",
        "category": "Créativité Culinaire",
        "description": "Agent spécialisé en chocolaterie professionnelle : chocolats, ganaches, pralinés, tablettes et technique de tempérage."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Desserts au chocolat, bouchées, brownies et combinaisons avancées."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de nouvelles pièces avec recette + fiche technique CSV."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa : couvertures techniques, pâtes concentrées, fruits à coque et arômes professionnels."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue tSpoonLab pour les applications avancées de chocolaterie."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes par processus (tempérage, moulage, chutes, exposition en vitrine) dans le calcul de coût."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par chocolat : produits laitiers, fruits à coque, gluten, alcools."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie gastronomique IA de référence pour la vitrine, le web, le packaging et les réseaux."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capte un trafic organique stable pour la chocolaterie premium."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial pour la chocolaterie d'auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients locaux qui recherchent \"chocolaterie artisanale près de moi\" sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Planification saisonnière : Noël, Saint-Valentin, Pâques, Roscón, Fête des Mères."
      }
    ],
    "metrics": [
      {
        "value": "+7 pp",
        "label": "marge après calcul de coût des chocolats"
      },
      {
        "value": "−35 %",
        "label": "pertes à l'atelier et en vitrine"
      },
      {
        "value": "×2",
        "label": "commandes d'entreprise à Noël"
      },
      {
        "value": "12+",
        "label": "agents pour votre chocolaterie"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Calculs de coût sans coût horaire d'atelier, chocolats complexes en perte sans le savoir",
        "Cacao volatil qui fausse les prix sans recalcul en temps réel",
        "Pertes au tempérage, au moulage et en vitrine sans traçabilité réelle",
        "Production saisonnière réactive : vous arrivez trop tard pour Noël et perdez des commandes d'entreprise",
        "APPCC sur papier imprimé dispersé dans l'atelier"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Calcul de coût professionnel par chocolat avec coût horaire d'atelier intégré et cacao actualisable",
        "Pertes maîtrisées avec Rendement GenCal et modèles spécifiques à la chocolaterie",
        "Pinterest Pins Gen + InstaFlow + GastroIMG Gen+ captent un trafic stable et des commandes",
        "Gastro Calendar planifie Noël et la Saint-Valentin avec 8 à 12 semaines d'avance",
        "APPCC depuis le mobile avec des registres prêts pour l'inspection"
      ]
    },
    "galleryTitle": "Comment Fonctionne une Chocolaterie Artisanale",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : vitrine, atelier, tempérage, chocolats, exposition et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Restaurant Créatif et de Chef",
    "heroSubtitle": "Brainstorming gastronomique, R&D avant-gardiste, calculs de coûts de technique avancée, fiches techniques premium et storytelling pour restaurants de chef avec une suite d'agents d'IA gastronomique de niveau professionnel.",
    "heroTagline": "Créativité avec système, avant-garde avec marge",
    "badge": "Pour restaurants créatifs et de chef",
    "painsTitle": "Ce qu'un Restaurant Créatif Ne Peut Pas Manquer de Résoudre",
    "pains": [
      "Cartes qui changent toutes les 6 à 12 semaines avec R&D continue et beaucoup d'expérimentation",
      "Calculs de coûts complexes avec techniques avancées (sphérifications, fermentations, cuissons longues, déshydratations)",
      "Petites équipes avec dévouement intense qui ont besoin de documentation professionnelle, pas d'improvisation",
      "Storytelling et communication avec le client, la presse et les réseaux sont un levier clé de marque",
      "Menus dégustation longs avec calcul de coûts total et séquence cohérente de services",
      "Se différencier dans un créneau saturé de propositions créatives et attirer le convive exigeant"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide dans un Restaurant Créatif",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative + Food Pairing AI",
        "description": "Brainstorming pour des plats de chef par saison, ingrédient ou technique avec base scientifique. Cuisine Créative livre recette + calcul de coûts CSV."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "R&D gastronomique d'avant-garde : koji, kombuchas, shoyus, garums, lactofermentations et techniques innovantes avec un soutien professionnel."
      },
      {
        "icon": "Leaf",
        "title": "VegChef Plant-Based",
        "description": "Cuisine plant-based, végane et végétarienne avancée pour plats de chef avec technique professionnelle et nutritionnelle."
      },
      {
        "icon": "Calculator",
        "title": "Calculs de coûts de technique avancée",
        "description": "Kit de Escandallos Pro : vous chargez le CSV de Cuisine Créative avec vos prix réels pour des plats avec des techniques coûteuses et des processus longs."
      },
      {
        "icon": "Search",
        "title": "Sonar Deep Research",
        "description": "Recherche approfondie des tendances, producteurs artisanaux, techniques émergentes et références de l'avant-garde mondiale."
      },
      {
        "icon": "MessageSquare",
        "title": "BlogPost SEO Gen+",
        "description": "Storytelling pour le blog du restaurant, dossier de presse et communication avec les médias gastronomiques."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Photographie gastronomique IA de haut niveau pour fiches techniques, presse, site web du restaurant et réseaux."
      },
      {
        "icon": "BookOpen",
        "title": "Agent Sosa Ingredients + Agent tSpoonLab",
        "description": "Assistants pour la sélection d'ingrédients techniques de Sosa et tSpoonLab, essentiels pour la cuisine de chef."
      },
      {
        "icon": "GraduationCap",
        "title": "Gastro Lexicum + Pro Prompts eBook",
        "description": "Tuteur de définitions techniques et scientifiques + 300+ prompts professionnels pour la créativité et la communication."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Restaurant Créatif avec AI Chef Pro",
    "workflow": [
      "08:30 · Sonar Deep Research — vous recherchez des tendances et des produits de saison sur les marchés européens pour l'inspiration du prochain changement de carte.",
      "10:00 · Cuisine Créative + Food Pairing AI — vous développez 14 plats pour le nouveau menu dégustation avec technique et calcul de coûts CSV initial.",
      "12:00 · Fermentus Avec AI+ — vous travaillez la base d'une fermentation clé du menu : koji d'orge inoculé pour 4 plats.",
      "14:00 · Agent Sosa Ingredients + Agent tSpoonLab — vous sélectionnez des ingrédients techniques pour les textures et les applications.",
      "15:30 · Kit de Escandallos Pro — vous chargez les CSV avec vos prix réels et vous écartez 4 plats qui ne correspondent pas à la marge cible (32 %).",
      "17:00 · Pro Prompts eBook — vous rédigez le storytelling pour les 10 plats finaux : nom, narration et fiche technique complète.",
      "18:30 · GastroIMG Gen+ — vous générez des photographies de chaque plat pour le dossier de presse et le site web du restaurant.",
      "19:30 · Service — équipe coordonnée avec fiches techniques centralisées, services du menu dégustation avec séquence validée."
    ],
    "productsTitle": "Modèles et Kits Téléchargeables pour Restaurant Créatif",
    "productIds": [
      "kit-tareas-restaurante-creativo",
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "Je change la carte toutes les 6 semaines et avant c'était une semaine de paperasse de clôture rien qu'entre calculs de coûts, fiches techniques et storytelling. Maintenant avec AI Chef Pro, cette clôture se fait en 2 jours : Cuisine Créative propose, Fermentus me donne du support en R&D, Sonar Deep Research apporte des tendances, et le Kit de Escandallos Pro clôture la marge. C'est littéralement comme avoir une équipe de R&D supplémentaire.",
    "testimonialAuthor": "Adrián Lago",
    "testimonialRole": "Chef et propriétaire, restaurant gastronomique de 30 couverts",
    "faqTitle": "Questions Fréquentes des Restaurants Créatifs",
    "faqs": [
      {
        "q": "L'IA comprend-elle la technique de chef avancée ?",
        "a": "Oui. Cuisine Créative, Fermentus Avec AI+, Food Pairing AI, VegChef et les recueils de recettes par pays sont entraînés avec des connaissances professionnelles : techniques comme les sphérifications, fermentations longues, cuissons contrôlées, gélifications, mousses, déshydratations et processus d'avant-garde."
      },
      {
        "q": "Y a-t-il des menus dégustation spécifiques ?",
        "a": "Oui. Le Kit de Tareas Restaurante Creativo et le Kit de Escandallos Pro ont des modèles pour menus dégustation avec calcul de coûts total, séquence de services et accord mets-vins."
      },
      {
        "q": "Couvre-t-il la R&D et le test de plats ?",
        "a": "Oui. Sonar Deep Research apporte des tendances et des références ; Cuisine Créative + Fermentus développent des plats ; Pro Prompts eBook a 300+ prompts spécifiques pour la R&D itérative."
      },
      {
        "q": "Génère-t-il du storytelling pour la presse et les guides ?",
        "a": "Oui. BlogPost SEO Gen+ + Pro Prompts eBook + GastroIMG Gen+ permettent de rédiger un dossier de presse, une communication avec les guides Michelin/Repsol/50Best et des notes pour les médias gastronomiques."
      },
      {
        "q": "Fonctionne-t-il pour la fermentation d'avant-garde ?",
        "a": "Fermentus Avec AI+ est l'agent le plus utilisé par les chefs d'auteur : il couvre le koji, la kombucha, le shoyu, le miso, le garum, les lactofermentations et les processus innovants avec un soutien scientifique."
      },
      {
        "q": "Comment s'intègre-t-il avec Sosa et d'autres fournisseurs techniques ?",
        "a": "Agent Sosa Ingredients et Agent tSpoonLab sont des assistants spécifiques du catalogue de chaque fournisseur : ils aident à sélectionner des textures, des additifs et des applications techniques avec un critère professionnel."
      }
    ],
    "ctaTitle": "Créativité avec système, avant-garde avec marge.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Restaurant Créatif et de Chef : R&D, Avant-garde et Storytelling | AI Chef Pro",
      "description": "Suite d'IA pour restaurants créatifs et de chef : Cuisine Créative, Fermentus, Sonar Deep Research, calculs de coûts avancés, fiches techniques et storytelling professionnel.",
      "keywords": "IA restaurant créatif, restaurant de chef IA, logiciel restaurant créatif, calculs de coûts créatifs, IA gastronomique chef, fermentation créative IA, Fermentus, restaurant de chef Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-creativo.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Cuisine Créative dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes dans lequel vous lui racontez quel type de cuisine créative vous dirigez (auteur, gastrobotanique, fermentations, avant-garde, fusion), votre ville et vos références. À partir de ce moment, chaque agent — de Cuisine Créative à Sonar Deep Research — répond adapté à votre langage créatif, à votre technique habituelle et à votre positionnement réel dans le secteur.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Restaurant Créatif",
    "apps": [
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de plats professionnels avec recette + calcul de coûts CSV prêt pour le Kit de Escandallos Pro."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Combinaisons d'ingrédients et accords mets-vins avec base scientifique."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "R&D d'avant-garde : fermentations, koji, kombucha, garum, miso."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Créativité Culinaire",
        "description": "Cuisine plant-based, végane et végétarienne avancée pour chef."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Desserts de chef avec technique de pâtisserie professionnelle."
      },
      {
        "name": "Chef Exécutif Pro",
        "category": "Profil Gastro Pro",
        "description": "Standardisation des fiches techniques et des manuels de cuisine."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche approfondie : tendances, producteurs, avant-garde mondiale."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue Sosa pour les textures et les techniques avancées."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue tSpoonLab pour les applications techniques."
      },
      {
        "name": "Gastro Lexicum",
        "category": "Connaissance Gastro",
        "description": "Tuteur avec définitions de techniques, processus et science gastronomique."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie gastronomique de haut niveau pour la presse et le web."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles de blog avec storytelling pour attirer du trafic organique."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "vitesse de clôture de nouvelle carte"
      },
      {
        "value": "14",
        "label": "plats dans le menu dégustation"
      },
      {
        "value": "+5 pp",
        "label": "marge après calcul de coûts réel"
      },
      {
        "value": "13+",
        "label": "agents pour cuisine de chef"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Clôture de nouvelle carte : 15 à 30 jours entre R&D, calculs de coûts, fiches techniques et storytelling",
        "R&D improvisée sans documentation, techniques qui s'oublient",
        "Storytelling pour la presse rédigé contre la montre à chaque changement",
        "Fiches techniques dans un carnet inaccessibles pendant le service",
        "Recherche de tendances par intuition sans accès aux sources"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Clôture de nouvelle carte : 1 à 3 jours avec Cuisine Créative, Fermentus et Kit de Escandallos Pro",
        "R&D documentée avec fiches itératives, techniques tracées et réplicables",
        "Storytelling professionnel généré en heures avec BlogPost SEO Gen+",
        "Fiches techniques centralisées accessibles depuis le mobile pendant le service",
        "Sonar Deep Research apporte des tendances et des références professionnelles"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Restaurant Créatif de Chef",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : R&D, fermentations, dressage de chef, préparation d'ingrédients spéciaux et salle intimiste.",
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
    "h1": "IA pour Restaurant Gastronomique (Michelin/Repsol)",
    "heroSubtitle": "Fiches techniques premium, menus dégustation longs, brigade étoffée, HACCP rigoureux et communication avec les guides et la presse grâce à une suite d'agents IA conçus pour la haute gastronomie professionnelle.",
    "heroTagline": "La haute cuisine avec de la méthode, l'avant-garde avec du cap",
    "badge": "Pour les restaurants gastronomiques Michelin et Repsol",
    "painsTitle": "Ce Qu'un Restaurant Gastronomique Doit Absolument Résoudre",
    "pains": [
      "Marge exigeante avec des produits premium dont le coût change chaque semaine au marché et au comptoir",
      "Brigade étendue et hautement coordonnée avec une hiérarchie stricte et une rotation des chefs juniors",
      "Menus dégustation longs (8 à 15 services) avec fiche technique complète, accords mets-vins et narration cohérente",
      "Communication avec les guides Michelin/Repsol/50Best et la presse spécialisée comme levier critique",
      "R&D continue de pointe avec techniques avancées et produit de saison",
      "Réservations à plusieurs mois avec annulations difficiles à gérer et un service en salle impeccable"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide en Haute Gastronomie",
    "features": [
      {
        "icon": "ChefHat",
        "title": "Chef Exécutif Pro",
        "description": "Standardisation des fiches techniques et des manuels pour une brigade étendue avec une hiérarchie stricte."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative + Food Pairing AI",
        "description": "Brainstorming pour les plats de menu dégustation avec technique et accords. Cuisine Créative fournit recette + fiche de coût en CSV."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "R&D de pointe : koji, kombuchas, shoyus, garums, lactoferments essentiels en haute gastronomie contemporaine."
      },
      {
        "icon": "Calculator",
        "title": "Fiches de coût premium",
        "description": "Kit de Escandallos Pro : vous chargez le CSV de Cuisine Créative avec vos prix réels pour un produit premium avec une marge ajustée par temps et par menu dégustation complet."
      },
      {
        "icon": "BookOpen",
        "title": "Agent Sosa Ingredients + Agent tSpoonLab",
        "description": "Assistants des catalogues professionnels les plus utilisés en haute cuisine pour des techniques et applications avancées."
      },
      {
        "icon": "Search",
        "title": "Sonar Recherche Approfondie",
        "description": "Recherche approfondie sur les tendances mondiales, les producteurs artisanaux, les techniques émergentes et les références de l'avant-garde internationale."
      },
      {
        "icon": "MessageSquare",
        "title": "BlogPost SEO Gen+ + Pro Prompts eBook",
        "description": "Communication professionnelle pour les guides Michelin/Repsol/50Best, dossier de presse et storytelling du menu dégustation."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Photographie gastronomique IA de haut niveau pour le web, la presse spécialisée et les dossiers de candidature aux guides."
      },
      {
        "icon": "GraduationCap",
        "title": "Gastro Lexicum",
        "description": "Tuteur avec des définitions techniques, des processus et la science gastronomique pour les fiches premium et la formation de la brigade."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Restaurant Gastronomique avec AI Chef Pro",
    "workflow": [
      "08h30 · Sonar Deep Research — vous étudiez les tendances et les produits de saison sur les marchés européens pour l'inspiration du prochain changement de menu dégustation.",
      "10h00 · Cuisine Créative + Food Pairing AI — vous développez 14 services pour le nouveau menu dégustation avec une technique avancée et une fiche technique CSV.",
      "12h00 · Fermentus Avec AI+ — vous travaillez la base d'une fermentation clé du menu : garum de poisson pour 4 services.",
      "14h00 · Agent Sosa Ingredients + Agent tSpoonLab — vous sélectionnez des ingrédients techniques pour des textures et des applications premium.",
      "15h30 · Kit de Escandallos Pro — vous chargez les CSV avec vos prix de marché et validez la marge du menu dégustation complet (28 €/service en coût moyen).",
      "17h00 · Pro Prompts eBook + BlogPost SEO Gen+ — vous rédigez la narration des 14 services, le dossier pour les guides Michelin/Repsol et le communiqué de presse.",
      "18h30 · GastroIMG Gen+ — vous générez des photographies de chaque service pour le site du restaurant et le dossier de candidature aux guides.",
      "19h30 · Service du soir — brigade coordonnée avec des fiches techniques centralisées, des services du menu dégustation avec une séquence validée et un accord mets-vins synchronisé avec le sommelier."
    ],
    "productsTitle": "Modèles, Kits et Guides Téléchargeables pour la Haute Gastronomie",
    "productIds": [
      "guia-restaurante-gastronomico",
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-gestion-personal",
      "kit-inventario"
    ],
    "testimonialQuote": "Avoir la fiche technique, la fiche recette, les fermentations documentées et la communication avec les guides dans un seul système a mis de l'ordre dans le chaos créatif de toute grande cuisine. La Guía Restaurante Gastronómico a été clé lors de l'ouverture du deuxième projet : un business plan professionnel qui soutient la candidature. Une récompense récente, données à l'appui.",
    "testimonialAuthor": "David Aramburu",
    "testimonialRole": "Chef exécutif, restaurant gastronomique étoilé Michelin/Repsol",
    "faqTitle": "Questions Fréquentes des Restaurants Gastronomiques",
    "faqs": [
      {
        "q": "Pour un restaurant étoilé Michelin ou un restaurant aspirant ?",
        "a": "Pour les deux. Les modèles et les agents sont conçus pour une exigence élevée : standardisation rigoureuse, fiches techniques premium, coût de revient professionnel et communication avec les guides."
      },
      {
        "q": "Existe-t-il un guide pas à pas pour ouvrir un restaurant gastronomique ?",
        "a": "Oui, la Guía Restaurante Gastronómico (85 €) : 65 places, business plan type pour la candidature, plan financier, plan de cuisine, brigade, sommelier, manuels opérationnels et communication avec les guides. 20+ livrables."
      },
      {
        "q": "Couvre-t-il les menus dégustation longs de 14 à 18 temps ?",
        "a": "Oui. Le Kit de Escandallos Pro et le Kit de Tareas Restaurante Creativo ont des modèles spécifiques pour les menus dégustation avec les temps, le coût de revient total, la séquence et les accords synchronisés avec le sommelier."
      },
      {
        "q": "Génère-t-il une communication professionnelle pour Michelin, Repsol et 50Best ?",
        "a": "Oui. BlogPost SEO Gen+ + Pro Prompts eBook + GastroIMG Gen+ permettent de rédiger un dossier de candidature, une communication avec les inspecteurs, des communiqués de presse et des supports pour les services des guides."
      },
      {
        "q": "Fonctionne-t-il pour la fermentation de pointe ?",
        "a": "Fermentus Avec AI+ est l'un des agents les plus utilisés par les chefs étoilés Michelin : il couvre le koji, le kombucha, le shoyu, le miso, le garum et les lactoferments avec un soutien scientifique et des applications réelles dans les plats de haute gastronomie."
      },
      {
        "q": "Comment s'intègre-t-il avec des fournisseurs premium ?",
        "a": "Agent Sosa Ingredients et Agent tSpoonLab sont des assistants spécifiques de catalogues professionnels très utilisés en haute gastronomie. Ils aident à sélectionner des textures, des additifs et des applications techniques avec un critère de cuisine créative."
      }
    ],
    "ctaTitle": "La haute cuisine avec de la méthode, l'avant-garde avec du cap.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Formule Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Restaurant Gastronomique (Michelin/Repsol) : Menu Dégustation, R&D et Communication | AI Chef Pro",
      "description": "Suite d'IA pour haute gastronomie : Cuisine Créative, Fermentus, Sonar Deep Research, analyses de coûts premium, fiches techniques, communication avec les guides Michelin et Repsol. Commencez aujourd'hui.",
      "keywords": "IA restaurant gastronomique, logiciel Michelin, restaurant haute cuisine IA, analyses de coûts premium, IA Repsol Soles, IA 50Best, fermentation créative, Fermentus, menu dégustation IA, gastronomie Espagne",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-gastronomico.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Restaurant Gastronomique dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes au cours duquel vous nous confiez le type de cuisine que vous dirigez (Michelin, Soles Repsol, candidat, haute cuisine contemporaine, fusion avant-gardiste), le nombre de couverts, la ville et vos références. À partir de ce moment, chaque agent — de la Cuisine Créative à Sonar Deep Research — répond en s'adaptant à votre langage, votre technique habituelle et votre positionnement réel dans le secteur.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser dans Votre Restaurant Gastronomique",
    "apps": [
      {
        "name": "Chef Exécutif Pro",
        "category": "Gastro Profile Pro",
        "description": "Standardisation des fiches techniques et des manuels pour la brigade étendue."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement des passes du menu dégustation avec recette et coût de revient CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Combinaisons d'ingrédients et accords à base scientifique."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "R&D de pointe : koji, kombucha, shoyu, miso, garum, lactofermentations."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Créativité Culinaire",
        "description": "Cuisine végétale haut de gamme pour les options plant-based du menu dégustation."
      },
      {
        "name": "Pâtisserie Créative + Chocolaterie Créative",
        "category": "Créativité Culinaire",
        "description": "Desserts de haute cuisine et petits fours de clôture."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche approfondie des tendances et de l'avant-garde mondiale."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue Sosa pour les textures et techniques avancées."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Assistant du catalogue tSpoonLab pour les applications techniques."
      },
      {
        "name": "Gastro Lexicum",
        "category": "Connaissance Gastro",
        "description": "Tuteur avec des définitions techniques et scientifiques."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie gastronomique de haut niveau pour la presse et les guides."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Storytelling et communication professionnelle avec des guides et une presse spécialisée."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "vitesse de finalisation d'un nouveau menu"
      },
      {
        "value": "14-18",
        "label": "services en menu dégustation"
      },
      {
        "value": "+5 pp",
        "label": "marge après épluchage rigoureux"
      },
      {
        "value": "13+",
        "label": "agents pour la haute gastronomie"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Finalisation d'un nouveau menu dégustation : 15-30 jours entre R&D, analyses de coûts, fiches techniques et communication avec les guides.",
        "R&D de ferments sans documentation, techniques qui ne se reproduisent pas.",
        "Storytelling pour la presse et les guides contre la montre à chaque changement.",
        "Fiches techniques dans le carnet du chef, inaccessibles pendant le service.",
        "Recherche de tendances par intuition et magazines, sans accès systématique."
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Finalisation du menu dégustation : 1-3 jours avec Cuisine Créative, Fermentus et Kit de Escandallos Pro.",
        "R&D documenté avec fiches itératives, fermentations tracées et reproductibles par la brigade.",
        "Storytelling professionnel pour Michelin/Repsol/50Best généré en heures.",
        "Fiches techniques centralisées, accessibles depuis le mobile pendant le service.",
        "Sonar Deep Research apporte des tendances de l'avant-garde mondiale instantanément."
      ]
    },
    "galleryTitle": "Comment Fonctionne un Restaurant Gastronomique de Haute Cuisine",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : salle élégante, dressage de menu dégustation, cuisine premium, sommelier et service impeccable.",
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
    "h1": "IA pour Restaurant Mexicain",
    "heroSubtitle": "Développez des sauces avec un équilibre précis, un rendement par taco et par menu avec coût réel, planifiez la production de masa et la nixtamalisation, et capturez un branding professionnel avec une suite d'agents IA gastronomiques spécialisés en cuisine mexicaine authentique.",
    "heroTagline": "Saveur mexicaine avec marge réelle et technique authentique",
    "badge": "Pour restaurants mexicains et taquerias",
    "painsTitle": "Ce Qu'un Restaurant Mexicain Ne Peut Pas Ignorer",
    "pains": [
      "Sauces complexes avec beaucoup de piments, torréfaction et équilibre précis (mole, salsa macha, adobos) qui nécessitent une consistance tour après tour",
      "Calculer le rendement des tacos, antojitos et plats avec de nombreuses variantes de tortilla, garniture, sauces et accompagnements tout en maintenant un food cost cohérent",
      "Pertes en masa, tortillas, marinades et protéines à longue cuisson (carnitas, barbacoa, cochinita)",
      "Standardiser la nixtamalisation et la technique de masa pour tortillas, sopes et huaraches avec une qualité constante",
      "Se différencier dans une zone concurrentielle avec un menu authentique, un branding visuel des antojitos et un storytelling régional (Oaxaca, Yucatán, Puebla)",
      "Attirer des commandes d'événements et de catering mexicain (mariages, fêtes patriotiques) avec marge tout en gérant le service quotidien"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide dans un Restaurant Mexicain",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Cuisine Mexicaine",
        "description": "Agent spécialisé en cuisine mexicaine authentique : sauces, moles, marinades, antojitos, technique de masa et cuisine régionale."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour des plats contemporains et d'auteur à base mexicaine : tacos signature, fusions contrôlées, desserts mexicains modernes."
      },
      {
        "icon": "Calculator",
        "title": "Rendement par taco et par plat",
        "description": "Cuisine Mexicaine fournit recette + rendement CSV ; Kit de Escandallos Pro le gère avec coût réel par taco, food cost % et prix suggéré."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles adaptables : préparation de masa, torréfaction de piments, marinades, comal, mise en place par station et fermeture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC mexicain",
        "description": "Traçabilité des piments, masa nixtamalisée, protéines à longue cuisson et températures critiques."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification avec dates clés : 5 de Mayo, Jour des Morts, Fêtes Patriotiques du 16 septembre, Jour de la Chandeleur avec tamales."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie gastronomique IA de référence + Instagram avec calendrier éditorial : le restaurant mexicain vit de l'impact visuel et du storytelling."
      },
      {
        "icon": "BarChart3",
        "title": "Agent Sosa Ingredients",
        "description": "Assistant du catalogue Sosa pour textures avancées, épaississants, déshydratés et technique appliquée à la cuisine mexicaine."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Mexicano",
        "description": "Guide premium téléchargeable de 80 pages avec rendements, fiches techniques, plan financier et opérations spécifiques de cuisine mexicaine."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Restaurant Mexicain avec AI Chef Pro",
    "workflow": [
      "08:00 · Ouverture — checklist Kit de Tareas : torréfaction de piments pour salsa macha, préparation de masa nixtamalisée, marinade de cochinita pibil, mise en place de toppings frais.",
      "10:00 · Cuisine Mexicaine — vous développez un nouveau taco signature de barbacoa avec sauce au piment cascabel et avocat. Cuisine Créative fournit recette + rendement CSV.",
      "11:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels de piments secs, viande, masa et avocat, validez la marge par taco et le food cost %.",
      "13:00 · Service de midi — l'équipe réplique avec des modèles de mise en place ; le comal fonctionne à plein rendement.",
      "17:00 · Pause entre les services — Gastro Calendar planifie le menu spécial du Jour des Morts avec pan de muerto et mole negro.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence du nouveau taco et les posts pour Instagram.",
      "21:00 · Service du dîner — pics coordonnés avec Repas du Personnel pour le staff avant le rush.",
      "00:00 · Fermeture — nettoyage en profondeur, APPCC signé, préparation de masa pour demain."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Restaurant Mexicain",
    "productIds": [
      "guia-restaurante-mexicano",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Nous avons fait un rendement taco par taco et découvert que trois signatures étaient en perte malgré être les plus vendus. Nous les avons redessinés avec Cuisine Mexicaine en ajustant la marinade et le rendement de la viande, sans toucher au prix, et avons augmenté la marge de 5 points. La planification du Jour des Morts avec Gastro Calendar a triplé notre chiffre d'affaires de cette semaine.",
    "testimonialAuthor": "María José Hernández",
    "testimonialRole": "Chef et propriétaire, restaurant mexicain contemporain",
    "faqTitle": "Questions Fréquentes des Restaurants Mexicains",
    "faqs": [
      {
        "q": "Est-ce que cela convient pour une taqueria décontractée, un restaurant mexicain contemporain ou une cuisine régionale ?",
        "a": "Pour les trois. Cuisine Mexicaine couvre de la taqueria traditionnelle à la haute cuisine mexicaine d'auteur, en passant par la cuisine régionale (Oaxaca, Yucatán, Puebla, Michoacán) avec une technique authentique."
      },
      {
        "q": "Couvre-t-il la nixtamalisation et la technique de masa ?",
        "a": "Oui. Cuisine Mexicaine raisonne comme un cuisinier mexicain professionnel : nixtamalisation à la chaux, équilibre de masa pour tortilla, sope, huarache, gordita et tlacoyo. Pas de recettes de YouTube."
      },
      {
        "q": "Comment m'aide-t-il avec la complexité des sauces mexicaines ?",
        "a": "Cuisine Mexicaine fournit des sauces avec un équilibre technique des piments (torréfaction, hydratation, équilibre piquant-doux-acide), des moles complexes en couches et des marinades professionnelles. Rendement GenCal ajoute le coût des piments secs au rendement final."
      },
      {
        "q": "Génère-t-il du contenu visuel pour Instagram, Glovo et Uber Eats ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles pour les réseaux et la livraison ; meilleure photo = plus de clics et meilleur classement. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre plat réel dressé."
      },
      {
        "q": "Comment m'aide-t-il avec les fêtes mexicaines ?",
        "a": "Gastro Calendar planifie les dates clés (Jour des Morts, Jour de la Chandeleur avec tamales, Fêtes Patriotiques, 5 de Mayo) avec des menus spéciaux et un calendrier éditorial."
      }
    ],
    "ctaTitle": "Votre restaurant mexicain avec marge réelle et technique authentique.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Restaurant Mexicain : Sauces, Rendements et Technique Authentique | AI Chef Pro",
      "description": "Suite IA pour restaurants mexicains : Cuisine Mexicaine, rendements par taco, planification des fêtes, branding et APPCC. Commencez aujourd'hui.",
      "keywords": "IA restaurant mexicain, logiciel taqueria, rendement taco, cuisine mexicaine IA, nixtamalisation, sauces mexicaines, Jour des Morts restaurant",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-mexicano.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Restaurant Mexicain dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes dans lequel vous lui racontez quel type de mexicain vous opérez (taqueria décontractée, restaurant mexicain contemporain, cuisine régionale, cantina, taqueria gourmet, food truck mexicain), taille de l'équipe, ville et spécialité. Chaque agent —de Cuisine Mexicaine à Gastro Calendar— répond adapté à votre produit, marché et opération réelle.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Restaurant Mexicain",
    "apps": [
      {
        "name": "Cuisine Mexicaine",
        "category": "Recettes d'Amérique Latine",
        "description": "Agent spécialisé en cuisine mexicaine authentique : sauces, moles, marinades, antojitos, technique régionale."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de tacos signature et de plats contemporains avec recette + rendement CSV."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'Entreprise",
        "description": "Conseil opérationnel pour restaurants décontractés et taquerias professionnelles."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour textures, épaississants et technique appliquée à la cuisine mexicaine d'auteur."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes en masa, piments, marinades et protéines à longue cuisson."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par plat : gluten, produits laitiers, fruits à coque, soja."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie gastronomique IA de référence pour Instagram, web, carte et livraison."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial professionnel pour taqueria d'auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients locaux qui recherchent \"tacos près de moi\" ou \"restaurant mexicain\" sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Jour des Morts, Jour de la Chandeleur, Fêtes Patriotiques, 5 de Mayo."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capture du trafic organique pour les tacos et antojitos avec storytelling."
      },
      {
        "name": "Repas du Personnel",
        "category": "Gastro Profile Pro",
        "description": "Générateur de menus pour le staff/famille transversal à tous les concepts."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge après rendement des tacos"
      },
      {
        "value": "×3",
        "label": "chiffre d'affaires au Jour des Morts"
      },
      {
        "value": "−20 %",
        "label": "pertes en masa et marinades"
      },
      {
        "value": "12+",
        "label": "agents pour votre cuisine mexicaine"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Sauces et moles improvisés, équilibre incohérent tour après tour",
        "Rendements sans food cost réel, signatures en perte sans le savoir",
        "Pertes en masa, piments et protéines longues sans traçabilité",
        "Fêtes réactives : vous arrivez en retard au Jour des Morts sans menu spécial",
        "Instagram improvisé et plateformes de livraison avec photos du mobile"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Sauces et moles avec critère technique, consistance tour après tour",
        "Rendement professionnel par taco et plat avec food cost validé",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques",
        "Fêtes planifiées 8 semaines à l'avance avec Gastro Calendar",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO attirent les clients locaux"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Restaurant Mexicain",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : sauces, tacos, comal, ingrédients et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Restaurant Péruvien",
    "heroSubtitle": "Développez des cebiches, tiraditos et causas avec un équilibre technique, un coût de revient par plat incluant le coût réel du poisson et du piment, planifiez la production et créez un branding professionnel avec une suite d'agents d'IA culinaire spécialisés en cuisine péruvienne authentique.",
    "heroTagline": "Cuisine péruvienne avec une vraie marge et une technique authentique",
    "badge": "Pour les restaurants péruviens et les cevicherías",
    "painsTitle": "Ce Qu'un Restaurant Péruvien Doit Absolument Résoudre",
    "pains": [
      "Cebiches et tiraditos avec du poisson frais quotidien et une leche de tigre équilibrée en acidité, piquant et sel à chaque service",
      "Calculer le coût de revient de plats avec des ingrédients péruviens importés (piments jaune, rocoto, panca, huacatay) dont le coût varie selon la saison",
      "Pertes en poisson frais, fruits de mer, maïs, pommes de terre péruviennes et citrons verts à usage intensif",
      "Standardiser la technique de cuisson des protéines (anticucho, poulet à la broche, pachamanca) et des accompagnements (causa, pomme de terre à la huancaína)",
      "Se différencier dans une zone concurrentielle avec un menu authentique (criollo, côtier, andin, amazonien), un branding visuel et un storytelling régional",
      "Capter les commandes de livraison et d'événements tout en maintenant la qualité du ceviche en dehors de sa fenêtre de consommation optimale"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Restaurant Péruvien",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Cuisine Péruvienne",
        "description": "Agent spécialisé dans la cuisine péruvienne authentique : ceviches, tiraditos, causas, anticuchos, pachamanca, technique créole, côtière, andine et amazonienne."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour des plats contemporains et signatures à base péruvienne : causas signature, fusions maîtrisées, desserts péruviens modernes."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing IA",
        "description": "Accords avec le pisco, les vins chiliens et la bière pour votre carte péruvienne à base scientifique."
      },
      {
        "icon": "Calculator",
        "title": "Coûts de revient par plat",
        "description": "Cuisine Péruvienne fournit la recette + le coût de revient CSV ; Kit de Escandallos Pro le gère avec le coût réel par ceviche, le food cost % et le prix suggéré."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles : préparation de leche de tigre, marinades d'anticucho, mise en place de fruits de mer, pomme de terre à la huancaína, clôture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC péruvien",
        "description": "Traçabilité du poisson frais, des fruits de mer, des piments et des températures critiques dans le ceviche et le tiradito."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification avec les dates clés : Jour de l'Indépendance le 28 juillet, Journée du Ceviche, Mistura, Journée du Pisco Sour."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie de ceviches et de tiraditos IA de référence + Instagram : le restaurant péruvien vit de l'impact visuel de la couleur."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Peruano",
        "description": "Guide premium téléchargeable de 80 places avec coûts de revient, fiches techniques, plan financier et opérations spécifiques à la cuisine péruvienne."
      }
    ],
    "workflowTitle": "Une Journée Type dans un Restaurant Péruvien avec AI Chef Pro",
    "workflow": [
      "08:00 · Ouverture — check-list Kit de Tareas : réception du poisson frais du jour, préparation de la leche de tigre de base, marinade d'anticucho, réhydratation des piments séchés.",
      "10:00 · Cuisine Péruvienne — vous développez un nouveau tiradito de pêche du jour avec une leche de tigre au rocoto et à la mangue. Cuisine Créative fournit la recette + le coût de revient CSV.",
      "11:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels de poisson frais, piments, maïs et pommes de terre, vous validez la marge par plat.",
      "12:00 · Food Pairing AI — vous validez l'accord du nouveau tiradito avec un pisco sour infusé aux herbes.",
      "13:00 · Service du midi — pic d'activité du cebichero, mise en place impeccable.",
      "17:00 · Pause entre les services — Gastro Calendar planifie le menu du 28 juillet (Indépendance) avec causa, anticuchos et pisco.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence du nouveau tiradito et les posts pour Instagram.",
      "23:00 · Fermeture — nettoyage en profondeur, APPCC signé, élimination contrôlée du poisson du jour."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Restaurant Péruvien",
    "productIds": [
      "guia-restaurante-peruano",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cuisine Péruvienne a transformé notre cuisine. La leche de tigre a désormais un équilibre technique documenté, les cebiches sont identiques à chaque service, et les coûts de revient avec du poisson frais au prix du jour fonctionnent en temps réel. La préparation du menu spécial du 28 juillet avec Gastro Calendar a triplé notre chiffre d'affaires.",
    "testimonialAuthor": "Carlos Fernández",
    "testimonialRole": "Chef et propriétaire, cevichería péruvienne contemporaine",
    "faqTitle": "Questions Fréquentes des Restaurants Péruviens",
    "faqs": [
      {
        "q": "Convient-il pour une cevicherie décontractée, un restaurant péruvien contemporain ou une cuisine régionale ?",
        "a": "Pour les trois. Cuisine Péruvienne couvre de la cevicherie traditionnelle à la haute cuisine signature, en passant par la cuisine régionale (créole, côtière, andine, amazonienne) avec une technique authentique."
      },
      {
        "q": "Couvre-t-il la technique du ceviche et du lait de tigre professionnel ?",
        "a": "Oui. Cuisine Péruvienne raisonne comme un cebichero professionnel : équilibre du lait de tigre avec acidité, piquant et sel ; fenêtre de marinade optimale par espèce ; intégration des piments avec technique."
      },
      {
        "q": "Comment m'aide-t-il avec le coût variable du poisson frais ?",
        "a": "Kit de Escandallos Pro recalcule instantanément la marge réelle lorsque vous mettez à jour le prix du poisson du jour. Rendement GenCal ajoute le coût des pertes par processus. Ainsi, le ceviche reflète toujours le coût actuel."
      },
      {
        "q": "Génère-t-il du contenu visuel pour Instagram, Glovo et Uber Eats ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles du ceviche et du tiradito pour Instagram, le web et la livraison ; meilleure photo = plus de clics. N'oubliez pas que l'image IA est une référence visuelle : la photo finale, c'est vous qui la prenez avec votre vrai ceviche dressé."
      },
      {
        "q": "Comment m'aide-t-il avec les fêtes et événements péruviens ?",
        "a": "Gastro Calendar planifie les dates clés (28 juillet Jour de l'Indépendance, Jour du Ceviche, Jour du Pisco Sour, Mistura) avec des menus spéciaux et un calendrier éditorial."
      }
    ],
    "ctaTitle": "Votre restaurant péruvien avec une vraie marge et une technique authentique.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Restaurant Péruvien : Ceviches, Fiches Techniques et Technique Authentique | AI Chef Pro",
      "description": "Suite d'IA pour restaurants péruviens : Cuisine Péruvienne, fiches techniques par ceviche, planification des festivités, branding et HACCP. Commencez aujourd'hui.",
      "keywords": "IA restaurant péruvien, logiciel de cevicherie, fiches techniques ceviche, cuisine péruvienne IA, lait de tigre, piment jaune, 28 juillet péruvien",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-peruano.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Restaurant Péruvien dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes au cours duquel vous nous expliquez quel type de restaurant péruvien vous exploitez (cevichería décontractée, restaurant péruvien contemporain, cuisine régionale, picantería andine, pollería, restaurant gastronomique), la taille de l'équipe, la ville et la spécialité. Chaque agent — de la Cuisine Péruvienne à Gastro Calendar — répond en s'adaptant à votre produit, votre marché et votre fonctionnement réel.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser dans Votre Restaurant Péruvien",
    "apps": [
      {
        "name": "Cuisine Péruvienne",
        "category": "Recettes d'Amérique latine",
        "description": "Agent spécialisé dans la cuisine péruvienne authentique : ceviches, tiraditos, causas, anticuchos, pachamanca."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de tiraditos signature et de plats contemporains avec recette + fiche technique CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords avec pisco, vins et bière pour votre carte péruvienne."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'affaires",
        "description": "Conseil opérationnel pour les cevicheries et les restaurants péruviens."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour les textures et la technique appliquée à la cuisine péruvienne d'auteur."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et utilitaires",
        "description": "Pertes en poisson frais, fruits de mer, piments et limes."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et utilitaires",
        "description": "Identification automatique des allergènes : poisson, fruits de mer, gluten, produits laitiers."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie gastronomique IA de référence pour Instagram, le web, la carte et la livraison."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et réseaux sociaux",
        "description": "Instagram avec un calendrier éditorial professionnel pour une cevicherie d'auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et réseaux sociaux",
        "description": "Attirer les clients locaux qui recherchent \"restaurant de ceviche à proximité\" ou \"restaurant péruvien\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et réseaux sociaux",
        "description": "28 juillet, Journée du ceviche, Mistura, Journée du Pisco Sour."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'affaires",
        "description": "Pour le bar à pisco sour et la mixologie péruvienne d'auteur."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge après calcul des coûts des ceviches"
      },
      {
        "value": "×3",
        "label": "chiffre d'affaires le 28 juillet"
      },
      {
        "value": "−25 %",
        "label": "pertes en poisson frais"
      },
      {
        "value": "12+",
        "label": "agents pour votre cuisine péruvienne"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Lait de tigre improvisé, équilibre incohérent d'un service à l'autre.",
        "Fiches techniques non actualisées au prix quotidien du poisson frais.",
        "Pertes en poisson, piments et fruits de mer sans traçabilité réelle.",
        "Festivités réactives : vous arrivez en retard au 28 juillet sans menu spécial.",
        "Instagram improvisé et plateformes de livraison avec photos du téléphone."
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Lait de tigre avec équilibre technique documenté, ceviches consistants.",
        "Fiche technique en temps réel avec le prix du poisson du jour.",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques.",
        "Festivités planifiées avec 8 semaines d'avance.",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO attirent les clients locaux."
      ]
    },
    "galleryTitle": "Comment Fonctionne un Restaurant Péruvien",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : cebiche, tiradito, anticucho, piments et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Restaurant Japonais",
    "heroSubtitle": "Développez sushi, ramen, robata et kaiseki avec une technique authentique, un calcul de coût par pièce avec le coût réel du poisson, planifiez la production de ferments et capturez une image de marque minimaliste avec une suite d'agents IA gastronomiques spécialisés en cuisine japonaise professionnelle.",
    "heroTagline": "Cuisine japonaise avec marge réelle et technique authentique",
    "badge": "Pour restaurants japonais, sushi bars et ramen-yas",
    "painsTitle": "Ce Qu'un Restaurant Japonais Doit Absolument Résoudre",
    "pains": [
      "Poisson frais quotidien pour sashimi et sushi avec un coût volatil et des pertes strictes liées au processus de filetage",
      "Standardiser le shari (riz à sushi), les nigiri et les maki à chaque service avec un équilibre technique de vinaigre, de sucre et de sel",
      "Bouillons longs (tonkotsu, dashi, shoyu, miso) qui nécessitent des heures de cuisson et une planification nocturne",
      "Fermentations professionnelles (koji, miso, shoyu fait maison, tsukemono) qui demandent du temps et une traçabilité",
      "Se différencier dans une zone concurrentielle avec une technique authentique vs. sushi industriel, branding minimaliste et storytelling japonais",
      "Capturer les commandes de livraison sans perdre la qualité du sushi (fenêtre optimale de 1 à 2 heures) et les événements omakase avec marge"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide dans un Restaurant Japonais",
    "features": [
      {
        "icon": "Fish",
        "title": "Cuisine Japonaise",
        "description": "Agent spécialisé en cuisine japonaise authentique : sushi, sashimi, ramen, robata, tempura, kaiseki, technique d'itamae et fermentation."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Pour le koji, le miso, le shoyu fait maison, l'amazake et les fermentations avancées de la cuisine japonaise."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour les plats contemporains et l'omakase à base japonaise : nigiri signature, fusions maîtrisées."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos par pièce",
        "description": "Cuisine Japonaise fournit la recette + l'escandallo CSV ; Kit de Escandallos Pro le gère avec le coût réel par nigiri, ramen et omakase."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles : filetage du poisson, préparation du shari, bouillons longs de nuit, mise en place robata, clôture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC japonais",
        "description": "Traçabilité du poisson pour sushi, fermentations, températures critiques et conservation."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification avec dates clés : Hanami (cerisier), Nouvel An japonais, Hina Matsuri, Journée du Sushi."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie minimaliste IA de référence + Instagram : le restaurant japonais vit de l'impact visuel zen et épuré."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Japonés",
        "description": "Guide premium téléchargeable de 60 places avec escandallos, fiches techniques, plan financier et opérations spécifiques."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Restaurant Japonais avec AI Chef Pro",
    "workflow": [
      "07:00 · Ouverture — checklist Kit de Tareas : réception du poisson frais, filetage des blocs de sashimi, contrôle du bouillon tonkotsu cuit toute la nuit.",
      "09:00 · Cuisine Japonaise — vous développez un nouveau nigiri signature de hamachi au yuzu kosho. La Cuisine Créative fournit la recette + le calcul de coût CSV.",
      "10:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels du poisson du jour et du wasabi frais, vous validez la marge pour chaque nigiri et l'omakase.",
      "11:00 · Fermentus Avec AI+ — vous vérifiez la progression du miso maison (mois 6 sur 12) et le nouveau koji en chambre de fermentation.",
      "13:00 · Service de midi — sushi bar à plein avec itamae travaillant devant le client.",
      "17:00 · Pause entre les services — Gastro Calendar planifie le menu spécial Hanami avec sakura mochi et bento aux fleurs de cerisier.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence du nouveau nigiri et les posts minimalistes pour Instagram.",
      "23:00 · Fermeture — nettoyage en profondeur, APPCC signé, préparation du tonkotsu pour demain (12 heures de cuisson)."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Restaurant Japonais",
    "productIds": [
      "guia-restaurante-japones",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "La Cuisine Japonaise a transformé notre fonctionnement. L'équilibre du shari est désormais constant, le tonkotsu sort identique chaque jour, et l'omakase dispose d'un calcul de coût professionnel avec une marge validée pièce par pièce. Fermentus nous a aidés à monter le programme de miso maison qui différencie totalement notre offre.",
    "testimonialAuthor": "Hiroshi Tanaka",
    "testimonialRole": "Itamae et propriétaire, restaurant japonais contemporain",
    "faqTitle": "Questions Fréquentes des Restaurants Japonais",
    "faqs": [
      {
        "q": "Est-ce adapté pour un sushi bar, un ramen-ya, une izakaya ou un kaiseki ?",
        "a": "Pour tous. Cuisine Japonaise couvre du sushi traditionnel à la haute cuisine kaiseki, en passant par le ramen-ya, la robata et l'izakaya avec une technique authentique."
      },
      {
        "q": "Couvre-t-il la technique d'itamae et la fermentation japonaise ?",
        "a": "Oui. Cuisine Japonaise raisonne comme un itamae professionnel : technique de filetage, équilibre du shari, neta et combinaisons ; Fermentus couvre le koji, le miso, le shoyu fait maison et l'amazake avec une technique professionnelle."
      },
      {
        "q": "Comment m'aidez-vous avec le coût variable du poisson pour le sashimi ?",
        "a": "Kit de Escandallos Pro recalcule instantanément la marge lorsque vous mettez à jour le prix du poisson du jour. Rendement GenCal ajoute le coût des pertes liées au filetage. Le nigiri reflète toujours le coût actuel."
      },
      {
        "q": "Génère-t-il du contenu visuel pour Instagram, Glovo et Uber Eats ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles du sushi pour Instagram, le site web et la livraison ; meilleure photo = plus de clics. Rappelez-vous que l'image IA est une référence visuelle : la photo finale, c'est vous qui la faites avec votre pièce réellement dressée."
      },
      {
        "q": "Comment m'aidez-vous avec les festivités japonaises ?",
        "a": "Gastro Calendar planifie les dates clés (Hanami avec sakura, Nouvel An japonais avec osechi ryori, Hina Matsuri, Jour du sushi) avec des menus spéciaux et un calendrier éditorial minimaliste."
      }
    ],
    "ctaTitle": "Votre restaurant japonais avec une marge réelle et une technique authentique.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10.000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour restaurant japonais : sushi, calcul des coûts et technique itamae | AI Chef Pro",
      "description": "Suite IA pour restaurants japonais : Cuisine Japonaise, Fermentus pour koji et miso, fiches techniques à la pièce, planification des fêtes. Commencez aujourd'hui.",
      "keywords": "IA restaurant japonais, logiciel sushi bar, fiches techniques sushi, cuisine japonaise IA, koji miso shoyu, ramen tonkotsu, itamae professionnel",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-japones.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Restaurant Japonais dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes dans lequel vous décrivez quel type de restaurant japonais vous exploitez (sushi bar, ramen-ya, izakaya, kaiseki, omakase, japonais contemporain de créateur), la taille de l'équipe, la ville et la spécialité. Chaque agent — de la Cuisine Japonaise à Gastro Calendar — répond adapté à votre produit, à votre marché et à votre fonctionnement réel.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Restaurant Japonais",
    "apps": [
      {
        "name": "Cuisine Japonaise",
        "category": "Recettes d'Asie",
        "description": "Agent spécialisé en cuisine japonaise authentique : sushi, sashimi, ramen, robata, kaiseki."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité culinaire",
        "description": "Koji, miso, shoyu maison, amazake et fermentations avancées."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité culinaire",
        "description": "Développement de nigiri signature et omakase avec recette + coût de revient CSV."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité culinaire",
        "description": "Accords avec saké, whisky japonais, bière et vins pour votre carte."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour textures et technique appliquée à la cuisine japonaise d'auteur."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et utilitaires",
        "description": "Pertes lors du filetage de poisson, sashimi et bouillons longs."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et utilitaires",
        "description": "Identification automatique des allergènes : poisson, fruits de mer, soja, gluten, sésame."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie minimaliste IA de référence pour Instagram, web, carte et livraison."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et réseaux sociaux",
        "description": "Instagram avec calendrier éditorial minimaliste pour sushi bar d'auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et réseaux sociaux",
        "description": "Attirer les clients locaux qui recherchent « sushi près de chez moi » ou « ramen près de chez moi »."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et réseaux sociaux",
        "description": "Hanami, Nouvel An japonais, Hina Matsuri, Journée du sushi."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts de restauration",
        "description": "Pour le bar à saké, le whisky japonais et les cocktails à base japonaise."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge après calcul du coût matière de l'omakase"
      },
      {
        "value": "×3",
        "label": "engagement Instagram avec GastroIMG"
      },
      {
        "value": "−20 %",
        "label": "pertes lors du filetage du poisson"
      },
      {
        "value": "12+",
        "label": "agents pour votre cuisine japonaise"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Shari et technique improvisés, équilibre irrégulier entre les itamae",
        "Fiches techniques non mises à jour selon le prix journalier du poisson",
        "Bouillons longs (tonkotsu) sans traçabilité ni planification rigoureuse",
        "Fermentations maison (miso, shoyu) sans programme documenté",
        "Instagram improvisé et plateformes de livraison avec des photos prises au téléphone"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Shari, neta et technique avec un savoir-faire professionnel, régularité d'un service à l'autre",
        "Fiche technique en temps réel avec le prix du poisson du jour",
        "Bouillons longs planifiés avec des modèles spécifiques et un plan HACCP signé",
        "Programme de fermentations avec Fermentus Avec AI+ documenté professionnellement",
        "GastroIMG Gen+, InstaFlow et MenuDish Local SEO attirent les clients locaux"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Restaurant Japonais",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : sushi, ramen, robata, ingrédients et équipement. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour restaurant nikkei",
    "heroSubtitle": "Développez des tiraditos nikkei, des sushis de fusion et de la robata avec une technique authentique péruano-japonaise, escandallez chaque plat avec un coût réel et captez une image de marque professionnelle avec une suite d'agents IA gastronomiques spécialisés en cuisine nikkei.",
    "heroTagline": "Cuisine nikkei avec marge réelle et technique authentique",
    "badge": "Pour restaurants nikkei et fusion péruano-japonaise",
    "painsTitle": "Ce qu'un restaurant nikkei ne peut pas laisser de côté",
    "pains": [
      "Combinaisons complexes péruano-japonaises avec équilibre précis de l'ají amarillo, du yuzu, du miso, du ponzu et du shoyu",
      "Poisson frais quotidien pour tiraditos et sushi avec coût volatil, filetage rigoureux et technique itamae appliquée à la cuisine péruvienne",
      "Standardiser les tiraditos signature, le sushi nikkei et les anticuchos avec marinade miso-ají panca tour après tour",
      "Escandaller des plats avec des ingrédients importés (ají amarillo, ají panca, yuzu, dashi) dont le coût varie selon la saison",
      "Se différencier du japonais traditionnel ou du péruvien pur avec un storytelling de fusion authentique et un branding visuel d'auteur",
      "Attirer les commandes d'omakase nikkei et d'événements en maintenant la qualité du produit cru"
    ],
    "featuresTitle": "Comment AI Chef Pro aide un restaurant nikkei",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Cuisine Japonaise + Cuisine Péruvienne",
        "description": "Combinaison d'agents spécialisés dans les deux cultures : technique itamae appliquée aux tiraditos péruviens, ají amarillo dans les nigiri, anticuchos miso."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Pour le koji, le miso, le shoyu maison adaptés à la fusion nikkei avec ají panca et huacatay."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Accords avec saké, pisco, vins chiliens et bière japonaise pour votre carte nikkei."
      },
      {
        "icon": "Calculator",
        "title": "Escandallos par plat",
        "description": "Cuisine Créative livre la recette + l'escandallo CSV ; Kit de Escandallos Pro le gère avec le coût réel par tiradito et par omakase nikkei."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles : filetage du poisson, préparation de la leche de tigre au yuzu, marinade nikkei, mise en place robata, fermeture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC nikkei",
        "description": "Traçabilité du poisson, des fermentations, des ajíes et des températures critiques sur produit cru."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification croisée : fêtes japonaises et péruviennes, événements de fusion, omakase nikkei de saison."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie éditoriale IA de référence + Instagram : le nikkei vit de l'impact visuel de la couleur et de la composition."
      },
      {
        "icon": "BookOpen",
        "title": "Guía Restaurante Nikkei",
        "description": "Guide premium téléchargeable de 60 places avec escandallos, fiches techniques, plan financier et opérations spécifiques nikkei."
      }
    ],
    "workflowTitle": "Une journée réelle dans un restaurant nikkei avec AI Chef Pro",
    "workflow": [
      "07h00 · Ouverture — checklist Kit de Tareas : réception du poisson frais, filetage pour tiraditos et nigiri, préparation de la leche de tigre au yuzu, marinade des anticuchos miso-panca.",
      "09h00 · Cuisine Japonaise + Cuisine Péruvienne — vous développez un nouveau tiradito de hamachi avec leche de tigre au yuzu et ají amarillo. Cuisine Créative livre la recette + l'escandallo CSV.",
      "10h00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels du poisson du jour, de l'ají amarillo et du yuzu, vous validez la marge par tiradito et par omakase nikkei.",
      "11h00 · Fermentus Avec AI+ — vous vérifiez la progression du miso maison à l'ají panca (mois 4 sur 8).",
      "12h00 · Food Pairing AI — vous validez l'accord du nouveau tiradito avec un saké junmai et un pisco macéré aux feuilles de shiso.",
      "13h00 · Service du midi — robata à plein régime avec anticuchos miso, sushi bar qui enchaîne les tiraditos signature.",
      "19h00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence du nouveau tiradito nikkei et les posts éditoriaux pour Instagram.",
      "23h00 · Fermeture — nettoyage en profondeur, HACCP signé, pertes contrôlées, préparation du lendemain."
    ],
    "productsTitle": "Modèles et kits recommandés pour restaurant nikkei",
    "productIds": [
      "guia-restaurante-nikkei",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cuisine Japonaise + Cuisine Péruvienne en croisant les agents, notre proposition a changé. Les tiraditos ont désormais un équilibre technique documenté, l'omakase nikkei sort avec un escandallo validé pièce par pièce, et le programme de miso maison à l'ají panca de Fermentus nous différencie totalement. Nous avons gagné 7 points de marge.",
    "testimonialAuthor": "Yui Sato",
    "testimonialRole": "Cheffe et propriétaire, restaurant nikkei d'auteur",
    "faqTitle": "FAQ des restaurants nikkei",
    "faqs": [
      {
        "q": "Est-ce adapté au nikkei contemporain, au sushi bar nikkei ou à la cevichería à technique japonaise ?",
        "a": "Pour les trois. Cuisine Japonaise + Cuisine Péruvienne se complètent pour couvrir du sushi nikkei aux tiraditos avec leche de tigre fusionnée au yuzu ou au ponzu."
      },
      {
        "q": "Comment m'aidez-vous avec l'équilibre entre techniques péruvienne et japonaise ?",
        "a": "Cuisine Créative orchestre les deux agents : elle raisonne en clé de fusion authentique (pas de fusion confuse), en respectant la technique itamae pour le produit cru et l'équilibre péruvien pour la leche de tigre et les marinades."
      },
      {
        "q": "Comment gérez-vous le coût variable du poisson et des ingrédients péruviens importés ?",
        "a": "Kit de Escandallos Pro recalcule instantanément la marge lorsque vous mettez à jour les prix du poisson du jour et des ajíes/yuzu. Rendement GenCal ajoute le coût des pertes par processus."
      },
      {
        "q": "Générez-vous du contenu visuel pour Instagram et la livraison ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles du tiradito nikkei pour Instagram, le site web et la livraison. Rappel : l'image IA est une référence visuelle ; la photo finale, c'est vous qui la faites avec votre plat réellement dressé."
      },
      {
        "q": "Comment m'aidez-vous avec les fêtes croisées péruano-japonaises ?",
        "a": "Gastro Calendar planifie les dates clés des deux cultures (28 juillet péruvien, Hanami japonais, Jour du Cebiche, Nouvel An japonais) avec omakase nikkei de saison et storytelling de fusion."
      }
    ],
    "ctaTitle": "Votre restaurant nikkei avec marge réelle et technique authentique.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour restaurant nikkei : tiraditos, escandallos et technique de fusion | AI Chef Pro",
      "description": "Suite IA pour restaurants nikkei : Cuisine Japonaise + Cuisine Péruvienne, escandallos par tiradito, omakase nikkei, branding et APPCC. Commencez aujourd'hui.",
      "keywords": "IA restaurant nikkei, logiciel nikkei, escandallos tiradito nikkei, cuisine nikkei IA, ají amarillo yuzu, sushi nikkei, fusion péruano-japonaise",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-nikkei.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre restaurant nikkei dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding conversationnel de 2 minutes où vous décrivez votre type de nikkei (nikkei contemporain d'auteur, sushi bar nikkei, cevichería à technique japonaise, omakase nikkei), la taille de votre équipe, votre ville et votre spécialité. Chaque agent s'adapte à votre produit, votre marché et votre réalité opérationnelle.",
    "appsTitle": "Les agents IA que vous utiliserez dans votre restaurant nikkei",
    "apps": [
      {
        "name": "Cuisine Japonaise",
        "category": "Recettes d'Asie",
        "description": "Technique itamae, filetage, sushi, sashimi et robata appliqués à la fusion nikkei."
      },
      {
        "name": "Cuisine Péruvienne",
        "category": "Recettes d'Amérique latine",
        "description": "Cebiches, tiraditos, anticuchos et technique péruvienne appliqués à la fusion nikkei."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité culinaire",
        "description": "Orchestrateur de fusion : tiraditos signature, sushi nikkei, omakase à base authentique."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité culinaire",
        "description": "Koji, miso maison à l'ají panca, shoyu et fermentations croisées."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité culinaire",
        "description": "Accords avec saké, pisco, vins chiliens et bière japonaise."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour textures et technique appliquée à la cuisine nikkei d'auteur."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et utilitaires",
        "description": "Pertes lors du filetage du poisson, des ajíes et des marinades longues."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et utilitaires",
        "description": "Identification automatique des allergènes : poisson, fruits de mer, soja, gluten, sésame, fruits à coque."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie éditoriale IA de référence pour Instagram, le site web, la carte et la livraison."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et réseaux sociaux",
        "description": "Instagram avec calendrier éditorial professionnel pour nikkei d'auteur."
      },
      {
        "name": "MenuDish SEO Local",
        "category": "Contenus et réseaux sociaux",
        "description": "Attirer les clients locaux qui cherchent « nikkei près de moi » sur Google et Maps."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et réseaux sociaux",
        "description": "Fêtes croisées : Hanami, 28 juillet, Jour du Cebiche, Nouvel An japonais."
      }
    ],
    "metrics": [
      {
        "value": "+7 pts",
        "label": "de marge après escandallage de l'omakase nikkei"
      },
      {
        "value": "×3",
        "label": "d'engagement Instagram avec GastroIMG"
      },
      {
        "value": "−25 %",
        "label": "de pertes sur poisson et ajíes"
      },
      {
        "value": "12+",
        "label": "agents pour votre cuisine nikkei"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Fusion improvisée sans équilibre technique entre les cultures",
        "Escandallos non mis à jour selon le prix du poisson et des ajíes",
        "Sushi nikkei et tiraditos avec une consistance variable entre les services",
        "Programme de fermentations maison sans documentation professionnelle",
        "Instagram improvisé, sans storytelling de fusion authentique"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Fusion authentique avec technique documentée des deux cultures",
        "Escandallo en temps réel avec prix actualisés",
        "Sushi nikkei et tiraditos avec équilibre technique constant",
        "Programme Fermentus avec miso ají panca documenté professionnellement",
        "GastroIMG Gen+ + InstaFlow + storytelling de fusion nikkei authentique"
      ]
    },
    "galleryTitle": "Comment fonctionne un restaurant nikkei",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : tiraditos, sushi nikkei, anticuchos miso, ingrédients et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Restaurant Plant-Based et Végane",
    "heroSubtitle": "Développez des menus plant-based avec équilibre nutritionnel, fiche technique par bol et burger végétal avec coût réel, planifiez des ferments végétaux et capturez un branding frais avec une suite d'agents d'IA gastronomique spécialisés en cuisine plant-based professionnelle.",
    "heroTagline": "Cuisine végétale avec une vraie marge et une technique avancée",
    "badge": "Pour les restaurants plant-based, véganes et healthy",
    "painsTitle": "Ce qu'un Restaurant Plant-Based Ne Doit Pas Manquer de Résoudre",
    "pains": [
      "Obtenir un umami profond en cuisine 100 % végétale avec des ferments, des fumés, du koji et une technique avancée (sans raccourcis industriels)",
      "Établir des fiches techniques pour des bols, des burgers végétaux et des plats plant-based avec de nombreuses variantes de garnitures et de protéines végétales",
      "Pertes élevées sur les produits frais (légumes de saison, fruits, herbes, micro-pousses) à courte date de péremption",
      "Standardiser les protéines végétales maison (seitan, tempeh, tofu mariné, substituts de viande) et les garnitures/sauces plant-based",
      "Se différencier dans une zone concurrentielle avec un menu signature plant-based, un branding visuel frais et un storytelling durable",
      "Attirer les commandes de livraison avec des produits frais tout en maintenant la présentation et la qualité du bol"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide dans un Restaurant Plant-Based",
    "features": [
      {
        "icon": "Sprout",
        "title": "VegChef Plant-Based",
        "description": "Agent spécialisé en cuisine plant-based, végane et végétarienne professionnelle : bols, burgers, protéines végétales, technique avancée."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Pour le koji végétal, le miso maison, le shoyu, le kimchi, la kombucha, les lactofermentations et un umami profond sans produits animaux."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour des plats plant-based contemporains et signatures à base végétale : bols signature, desserts véganes, fusions."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Accords avec des vins véganes, de la kombucha et des boissons fonctionnelles pour votre carte plant-based."
      },
      {
        "icon": "Calculator",
        "title": "Fiches techniques par bol et burger",
        "description": "VegChef fournit la recette + la fiche technique CSV ; Kit de Escandallos Pro la gère avec le coût réel par bol, le % de food cost et le prix suggéré."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles : préparation de protéines végétales, ferments, mise en place de garnitures fraîches, marinades, fermeture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC plant-based",
        "description": "Traçabilité des ferments, des protéines végétales maison, des herbes fraîches et des températures critiques."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification avec des dates clés : Veganuary (janvier), Journée mondiale végane, Earth Day, saisons des légumes locaux."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie IA vibrante de référence + Instagram : le plant-based vit de l'impact visuel de la couleur."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Restaurant Plant-Based avec AI Chef Pro",
    "workflow": [
      "07:00 · Ouverture — checklist Kit de Tareas : vérification des ferments en chambre, préparation de protéines végétales (seitan, tempeh), marinades de tofu, mise en place de micro-pousses et fleurs comestibles.",
      "09:00 · VegChef Plant-Based — vous développez un nouveau bol signature au quinoa, chou frisé, tempeh mariné, kimchi maison et tahini au curcuma. Cuisine Créative fournit la recette + la fiche technique CSV.",
      "10:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels de quinoa, chou frisé, tempeh et tahini, vous validez la marge par bol et le % de food cost.",
      "11:00 · Fermentus Avec AI+ — vous vérifiez la progression du miso maison (mois 6 sur 12), du koji végétal et du nouveau kimchi en chambre de fermentation.",
      "12:00 · Food Pairing AI — vous validez l'accord du nouveau bol avec une kombucha au gingembre et un vin blanc végane.",
      "13:00 · Service de midi — bols à gogo, burgers végétaux à la plancha, mise en place de garnitures fraîches.",
      "19:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence du nouveau bol et les publications vibrantes pour Instagram.",
      "22:00 · Fermeture — nettoyage en profondeur, APPCC signé, préparation des ferments pour la fermentation nocturne."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Restaurant Plant-Based",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "VegChef + Fermentus ont changé la donne. Nous obtenons un umami profond sans raccourcis industriels grâce au miso maison et au koji végétal, et les fiches techniques par bol avec du tempeh mariné nous confirment que le plant-based peut avoir une marge élevée. Nous avons gagné 6 points et l'acquisition sur Instagram avec GastroIMG est x3.",
    "testimonialAuthor": "Lucía Ferrer",
    "testimonialRole": "Chef et propriétaire, restaurant plant-based gastronomique",
    "faqTitle": "Questions Fréquentes sur les Restaurants Plant-Based",
    "faqs": [
      {
        "q": "Est-ce que ça convient aux bols sains décontractés, à la gastronomie végane ou à la cuisine plant-based signature ?",
        "a": "Pour les trois. VegChef couvre des bols décontractés à la haute cuisine végane, en passant par les restaurants de burgers végétaux, la cuisine à technique avancée et les desserts véganes professionnels."
      },
      {
        "q": "Comment obtenir un umami profond en cuisine 100 % végétale ?",
        "a": "Fermentus Avec AI+ couvre le koji végétal, le miso maison, le shoyu, le kimchi, la kombucha et les lactofermentations avec une technique professionnelle. VegChef intègre des fumés contrôlés, des déshydratés, des croûtes de champignons et des bouillons végétaux longs."
      },
      {
        "q": "Couvre-t-il les protéines végétales maison (seitan, tempeh, tofu mariné) ?",
        "a": "Oui. VegChef raisonne comme un chef plant-based professionnel : techniques de seitan pétri, tempeh fermenté, tofu mariné et pressé, substituts de viande avec technique de texture."
      },
      {
        "q": "Génère-t-il du contenu visuel pour Instagram, Glovo et Uber Eats ?",
        "a": "Oui. GastroIMG Gen+ génère des images vibrantes de référence des bols pour Instagram, le web et la livraison ; le plant-based vit de la couleur. N'oubliez pas que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre bol réellement dressé."
      },
      {
        "q": "Comment m'aide-t-il avec le Veganuary et les événements plant-based ?",
        "a": "Gastro Calendar planifie Veganuary (janvier), la Journée mondiale végane, Earth Day et les saisons de légumes locaux avec des menus spéciaux et un calendrier éditorial."
      }
    ],
    "ctaTitle": "Votre restaurant plant-based avec une vraie marge et une technique d'auteur.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Restaurant Végétal et Végane : Bowls, Calculs de Coût et Ferments | AI Chef Pro",
      "description": "Suite d'IA pour restaurants végétaux : VegChef, Fermentus pour umami végétal, calculs de coût par bowl, branding et HACCP. Commencez aujourd'hui.",
      "keywords": "IA restaurant végane, logiciel végétal, calculs de coût bowl végane, cuisine végane IA, ferments végétaux, umami végétal, Veganuary",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-plant-based.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Restaurant Plant-Based dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes où vous nous expliquez quel type de plant-based vous opérez (casual healthy bowls, fine dining végane, restaurant de burgers végétaux, restaurant végane gastronomique, café végane, dark kitchen végane), la taille de l'équipe, la ville et la spécialité. Chaque agent répond adapté à votre produit, marché et opération réelle.",
    "appsTitle": "Les Agents IA Que Vous Allez Utiliser dans Votre Restaurant Plant-Based",
    "apps": [
      {
        "name": "VegChef Plant-Based",
        "category": "Créativité Culinaire",
        "description": "Agent spécialisé en cuisine végétale, végane et végétarienne professionnelle avec une technique avancée."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "Koji végétal, miso maison, shoyu, kimchi, kombucha et lactoferments pour un umami profond."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de bowls signature et de plats végétaux contemporains."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords avec des vins véganes, du kombucha et des boissons fonctionnelles."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'entreprise",
        "description": "Conseil opérationnel pour les restaurants végétaux décontractés."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour textures végétales, gélifiants végétaux et technique."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes sur produits frais végétaux, micro-pousses et protéines maison."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique : gluten, fruits à coque, soja, sésame (sans produits animaux)."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie vibrante IA de référence pour Instagram, web, carte et livraison."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec un calendrier éditorial vibrant pour une cuisine végétale d'auteur."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients locaux qui recherchent \"végane près de moi\" ou \"végétal près de moi\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Veganuary, Journée mondiale végane, Earth Day, saisons de légumes."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge après calcul des bowls"
      },
      {
        "value": "×3",
        "label": "engagement Instagram avec GastroIMG"
      },
      {
        "value": "−30 %",
        "label": "pertes sur produits frais"
      },
      {
        "value": "12+",
        "label": "agents pour votre cuisine végétale"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Umami superficiel sans technique de fermentation professionnelle",
        "Calculs de coût sans coût de revient réel, bowls signature en perte sans le savoir",
        "Pertes sur produits frais végétaux sans traçabilité",
        "Protéines végétales maison improvisées sans standardisation",
        "Instagram improvisé et plateformes de livraison avec des photos du mobile"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Umami profond avec Fermentus : miso, koji, kimchi maison documentés",
        "Calcul de coût professionnel par bowl avec marge validée",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques",
        "Protéines végétales avec technique documentée (seitan, tempeh, tofu)",
        "GastroIMG Gen+ + InstaFlow + MenuDish Local SEO attirent les clients locaux"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Restaurant Plant-Based",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : bols, burgers végétaux, ferments, marché et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Grill, Grillades et Steakhouse",
    "heroSubtitle": "Développez des cartes de grill avec une technique de braises, un calcul des coûts par coupe avec coût réel, gérez le dry-aged et planifiez la production avec une suite d'agents d'IA gastronomique spécialisés dans la cuisine au feu, le grill et le steakhouse professionnel.",
    "heroTagline": "Grill avec marge réelle et technique du feu",
    "badge": "Pour grills, grillades, steakhouses et churrascarias",
    "painsTitle": "Ce Qu'un Grill Ne Peut Pas Manquer de Résoudre",
    "pains": [
      "Coût volatil de la viande (côte de bœuf, picanha, ribeye, T-bone) qui change le calcul des coûts chaque semaine",
      "Standardiser le point de cuisson et la technique de braises d'un service à l'autre (découpe, dry-aged, persillage, température interne)",
      "Pertes en découpe, dry-aging (3-12 % par semaine), parage et accompagnements",
      "Gestion du dry-aged avec chambre, humidité, température et rotation des coupes",
      "Se différencier dans une zone concurrentielle avec des coupes premium, une technique de braises et un storytelling des fournisseurs d'élevage",
      "Attirer les clients corporate et les événements privés avec des menus de grill à forte marge"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Grill",
    "features": [
      {
        "icon": "Flame",
        "title": "Cuisine Créative",
        "description": "Agent pour développer des cartes de grill avec une technique de braises, des marinades, des sauces et des accompagnements professionnels."
      },
      {
        "icon": "UtensilsCrossed",
        "title": "Cuisine Argentine + Brésilienne",
        "description": "Recueils de recettes spécialisés : asado argentin au gros sel, picanha brésilienne, churrasco, chimichurri authentique, farofa, vinaigrettes."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Accords avec des vins rouges premium, du whisky et une cocktailerie de caractère pour votre grill."
      },
      {
        "icon": "Calculator",
        "title": "Calcul des coûts par coupe",
        "description": "Cuisine Créative fournit recette + calcul des coûts CSV ; Kit de Escandallos Pro le gère avec un coût réel par côte de bœuf, picanha et T-bone."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles : allumage des braises, découpe, contrôle dry-aged, mise en place des accompagnements, fermeture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC asador",
        "description": "Traçabilité de la viande, dry-aging, températures critiques en chambre et température interne en cuisson."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification avec les dates clés : Fête des Pères (côte de bœuf), Noël, événements corporate, lancement de coupes spéciales par saison."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie IA premium de référence + Instagram : le grill vit de l'impact visuel des braises et de la coupe."
      },
      {
        "icon": "BarChart3",
        "title": "Rendement GenCal",
        "description": "Données précises sur les pertes en découpe, dry-aging et parage intégrées au calcul des coûts."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Grill avec AI Chef Pro",
    "workflow": [
      "09:00 · Ouverture — checklist Kit de Tareas : allumage contrôlé des braises (3 heures pour atteindre le point), contrôle de la chambre dry-aged, découpe des morceaux pour le service.",
      "11:00 · Cuisine Créative + Cuisine Argentine — vous développez une nouvelle coupe signature de côte de bœuf galicienne dry-aged 60 jours avec sel de Maldon fumé et chimichurri aux herbes fraîches. Recette + calcul des coûts CSV.",
      "12:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels de viande et de dry-aged, vous calculez la perte par affinage, vous validez la marge par coupe.",
      "13:00 · Service de midi — grill à plein régime avec des coupes premium, mise en place du chimichurri, sauces et accompagnements.",
      "17:00 · Pause entre les services — Bar & Lounge AI+ valide les accords avec des vins rouges pour les nouvelles coupes ; Gastro Calendar planifie le menu spécial de la Fête des Pères.",
      "20:00 · Service du dîner — pics coordonnés, grill avec plusieurs coupes simultanées.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence de la nouvelle côte de bœuf et les posts pour Instagram.",
      "00:00 · Fermeture — nettoyage en profondeur des grills, HACCP signé, contrôle de la chambre dry-aged."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Grill",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Nous avons fait un calcul des coûts coupe par coupe et découvert que le T-bone que nous vendions le plus était en réalité déficitaire à cause de la perte du dry-aged que nous ne calculions pas. Nous l'avons redessiné avec Cuisine Créative en ajustant la portion et les accompagnements, sans toucher au prix, et nous avons augmenté la marge de 5 points. La planification de la Fête des Pères avec Gastro Calendar a triplé notre chiffre d'affaires de cette semaine.",
    "testimonialAuthor": "Pedro Aguirre",
    "testimonialRole": "Maître du grill et propriétaire d'un grill premium",
    "faqTitle": "Questions Fréquentes des Grills",
    "faqs": [
      {
        "q": "Est-ce que ça convient pour un grill décontracté, un grill argentin, une churrascaria brésilienne ou un steakhouse premium ?",
        "a": "Pour les quatre. Cuisine Créative + Cuisine Argentine + Cuisine Brésilienne couvrent du grill décontracté au steakhouse premium avec des coupes dry-aged, en passant par le grill argentin traditionnel et la churrascaria brésilienne avec broches."
      },
      {
        "q": "Est-ce que ça couvre la technique du dry-aged et la gestion de la chambre ?",
        "a": "Oui. Cuisine Créative raisonne comme un maître grillardin professionnel : conditions de chambre dry-aged (1-3 °C, 75-85 % d'humidité), temps par coupe, contrôle des pertes hebdomadaires, identification de la pellicule et rotation."
      },
      {
        "q": "Comment gérer le coût volatil de la viande ?",
        "a": "Kit de Escandallos Pro recalcule instantanément la marge lorsque vous mettez à jour le prix de la viande. Rendement GenCal ajoute le coût des pertes liées au dry-aging, à la découpe et au parage. La coupe reflète toujours le coût actuel."
      },
      {
        "q": "Est-ce que ça génère du contenu visuel pour Instagram et les événements corporate ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence professionnelles de coupes et de braises pour Instagram, le web et la carte ; le grill vit de l'impact visuel. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre vraie coupe."
      },
      {
        "q": "Comment m'aide-t-il avec les événements et les fêtes ?",
        "a": "Gastro Calendar planifie la Fête des Pères, Noël, les événements corporate et les lancements de coupes spéciales avec des menus de grill et un calendrier éditorial."
      }
    ],
    "ctaTitle": "Votre grill avec une marge réelle et une vraie technique du feu.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits pour utiliser tous les agents.",
    "seo": {
      "title": "IA pour Grill, Grillades et Steakhouse : Coupes, Calculs des Coûts et Dry-Aged | AI Chef Pro",
      "description": "Suite d'IA pour grills et steakhouses : Cuisine Argentine + Brésilienne, calculs des coûts par coupe, dry-aged, branding et HACCP. Commencez dès aujourd'hui.",
      "keywords": "IA grill, logiciel steakhouse, calcul des coûts côte de bœuf, grill argentin IA, dry-aged, churrascaria, grill premium",
      "ogImage": "https://aichef.pro/og/use-cases/asador-parrilla-steakhouse.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Grill dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding conversationnel de 2 minutes dans lequel vous décrivez le type de grill que vous exploitez (grill argentin, churrascaria brésilienne, steakhouse premium avec dry-aged, grill de quartier décontracté, grill avec cuisine de créateur), la taille de l'équipe, la ville et la spécialité. Chaque agent répond en s'adaptant à votre produit, votre marché et votre exploitation réelle.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Grill",
    "apps": [
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Développement de cartes de grill avec technique de braises, marinades et accompagnements professionnels."
      },
      {
        "name": "Cuisine Argentine",
        "category": "Recueils de recettes d'Amérique latine",
        "description": "Asado argentin, chimichurri, provolone, ris d'agneau et technique de grill authentique."
      },
      {
        "name": "Cuisine Brésilienne",
        "category": "Recueils de recettes d'Amérique latine",
        "description": "Picanha, churrasco, farofa, vinagrete et technique de churrascaria brésilienne."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords avec des rouges puissants, du whisky et une cocktailerie de caractère pour grill."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts Commerciaux",
        "description": "Pour le bar du grill avec des vins rouges premium et une cocktailerie de caractère."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour les textures, les sels épicés et les techniques appliquées aux sauces et marinades."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes en découpe, dry-aging, parage et cuisson."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par coupe et accompagnement."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie IA premium de référence pour Instagram, le web, la carte et la livraison."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec un calendrier éditorial professionnel pour grill premium."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients locaux qui recherchent \"grill près de moi\" ou \"grill argentin\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Fête des Pères, Noël, événements corporate, lancements saisonniers."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge après calcul des coûts des coupes"
      },
      {
        "value": "×3",
        "label": "chiffre d'affaires à la Fête des Pères"
      },
      {
        "value": "−15 %",
        "label": "pertes en découpe et dry-aging"
      },
      {
        "value": "12+",
        "label": "agents pour votre grill"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Point de cuisson improvisé, consistance variable entre grillardin et service",
        "Calculs des coûts sans perte du dry-aged, coupes premium déficitaires sans le savoir",
        "Chambre dry-aged sans traçabilité réelle ni contrôle documenté",
        "Pertes en découpe et parage sans traçabilité",
        "Instagram improvisé, sans storytelling du fournisseur d'élevage"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Point de cuisson constant avec un critère technique documenté",
        "Calcul des coûts professionnel par coupe avec perte de dry-aged intégrée",
        "Chambre dry-aged avec traçabilité HACCP et rotation documentée",
        "Pertes contrôlées avec Rendement GenCal et modèles spécifiques",
        "GastroIMG Gen+ + InstaFlow + storytelling du fournisseur d'élevage"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Grill",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : grill, braises, dry-aged, coupes et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour coffee shop et specialty coffee",
    "heroSubtitle": "Concevez une carte de cafés de spécialité avec une approche third-wave, calculez le coût réel par boisson, planifiez la production de votre pâtisserie maison et créez un branding minimaliste avec une suite d'agents IA gastronomiques spécialisés dans le specialty coffee professionnel.",
    "heroTagline": "Café de spécialité avec une marge réelle et une technique third-wave",
    "badge": "Pour coffee shops, cafés de spécialité et third-wave coffee",
    "painsTitle": "Ce qu'un coffee shop ne peut pas ignorer",
    "pains": [
      "Créer une carte de café de spécialité avec discernement : single origins, blends, méthodes (espresso, V60, Aeropress, Chemex)",
      "Calculer chaque boisson avec un coût réel (grammage, lait premium, alternatives végétales) et un food cost cohérent",
      "Pertes en café moulu (dégradation rapide), lait et produits frais de pâtisserie",
      "Standardiser la technique de barista d'un service à l'autre : extraction, latte art, dosage, calibrage",
      "Se différencier dans une zone concurrentielle avec un café d'origine traçable, un branding visuel minimaliste et une formation continue",
      "Attirer des clients locaux fidèles et vendre des grains pour la maison avec une marge élevée"
    ],
    "featuresTitle": "Comment AI Chef Pro aide dans un coffee shop",
    "features": [
      {
        "icon": "Coffee",
        "title": "Cuisine Créative",
        "description": "Pour le développement de signatures : cold brews infusés, lattes au sirop maison, spécialités saisonnières."
      },
      {
        "icon": "Cake",
        "title": "Pâtisserie Créative",
        "description": "Pour une pâtisserie maison qui différencie le coffee shop : croissants, brownies, cookies, banana bread, gâteau du jour."
      },
      {
        "icon": "Calculator",
        "title": "Calcul par boisson",
        "description": "Cuisine Créative fournit recette + calcul CSV ; Kit de Escandallos Pro le gère avec un coût réel par café et lait, food cost % validé."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Cafetería / Brunch",
        "description": "Modèles : préparation du bar, calibrage espresso, préparation des alternatives végétales, mise en place pâtisserie, fermeture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC café",
        "description": "Traçabilité du café moulu, du lait, des alternatives végétales et de la pâtisserie maison."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Lancements saisonniers : pumpkin spice latte (automne), cold brew (été), café épicé de Noël."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie minimaliste IA de référence + Instagram : le specialty coffee vit de l'impact visuel du latte art."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Attirer les clients locaux qui recherchent « specialty coffee près de chez moi » sur Google et Maps."
      },
      {
        "icon": "BookOpen",
        "title": "BlogPost SEO Gen+",
        "description": "Articles SEO sur l'origine du café, les méthodes de filtration et les accords avec la pâtisserie pour attirer du trafic organique."
      }
    ],
    "workflowTitle": "Une journée réelle dans un coffee shop avec AI Chef Pro",
    "workflow": [
      "07:00 · Ouverture — checklist Kit de Tareas : calibrage de l'espresso, préparation des laits et alternatives végétales, mise en place de la pâtisserie du jour.",
      "08:00 · Service du matin — pic du matin avec des cafés de qualité constante, latte art professionnel.",
      "11:00 · Cuisine Créative — vous développez une nouvelle signature d'automne : latte à la citrouille avec sirop maison. Recette + calcul CSV.",
      "12:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels de café, lait et sirops, vous validez la marge et le food cost %.",
      "14:00 · Pâtisserie Créative — vous développez un nouveau banana bread vegan pour compléter la carte.",
      "17:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez l'image de référence de la nouvelle signature et les posts minimalistes pour Instagram.",
      "19:00 · Fermeture — nettoyage en profondeur de la machine, calibrage pour demain, contrôle du stock de café et de lait.",
      "20:00 · BlogPost SEO Gen+ — vous programmez un article sur les méthodes de filtration pour attirer du trafic organique."
    ],
    "productsTitle": "Modèles et Kits recommandés pour coffee shop",
    "productIds": [
      "kit-tareas-cafeteria",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cuisine Créative + Pâtisserie Créative ont transformé notre offre. Nous avons lancé des signatures saisonnières avec un calcul professionnel, la pâtisserie maison a augmenté de 30 % le ticket moyen et la formation des baristas est désormais cohérente. L'acquisition locale avec MenuDish + GastroIMG Gen+ a doublé en 4 mois.",
    "testimonialAuthor": "Marta Esteve",
    "testimonialRole": "Propriétaire, specialty coffee third-wave",
    "faqTitle": "Questions fréquentes des coffee shops",
    "faqs": [
      {
        "q": "Convient-il pour un coffee shop casual, un specialty coffee third-wave ou un torréfacteur avec boutique ?",
        "a": "Pour les trois. Cuisine Créative couvre des signatures simples jusqu'à une carte de specialty avec des méthodes de filtration avancées."
      },
      {
        "q": "Comment calculer les boissons avec du lait et des alternatives végétales ?",
        "a": "Cuisine Créative raisonne comme un barista professionnel : grammage exact du café, ratio de lait, coût de l'avoine premium vs soja. Kit de Escandallos Pro recalcule instantanément."
      },
      {
        "q": "Couvre-t-il la pâtisserie maison pour se différencier ?",
        "a": "Oui. Pâtisserie Créative fournit croissants, brownies, banana bread, cookies et spécialités de saison avec un calcul professionnel."
      },
      {
        "q": "Génère-t-il du contenu visuel minimaliste pour Instagram ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence avec une palette cream et warm wood. Rappelez-vous que l'image IA est une référence visuelle : la photo finale, c'est vous qui la faites avec votre vrai latte."
      },
      {
        "q": "Comment m'aide-t-il avec les lancements saisonniers ?",
        "a": "Gastro Calendar planifie pumpkin spice latte (automne), cold brew (été), café épicé de Noël et signatures par saison."
      }
    ],
    "ctaTitle": "Votre coffee shop avec une marge réelle et une technique third-wave.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "IA pour coffee shop et specialty coffee : Cartes, Calculs et Branding | AI Chef Pro",
      "description": "Suite IA pour coffee shops : Cuisine Créative, pâtisserie maison, calculs par boisson, branding minimaliste et acquisition locale. Commencez dès aujourd'hui.",
      "keywords": "IA coffee shop, logiciel specialty coffee, calculs café, third-wave coffee IA, latte art, café de spécialité",
      "ogImage": "https://aichef.pro/og/use-cases/coffee-shop-specialty.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre coffee shop dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding de 2 minutes où vous décrivez le type de coffee shop que vous exploitez (specialty third-wave, coffee shop casual, torréfacteur avec boutique, café avec pâtisserie maison), la taille de l'équipe, la ville et la spécialité.",
    "appsTitle": "Les agents IA que vous allez utiliser dans votre coffee shop",
    "apps": [
      {
        "name": "Cuisine Créative",
        "category": "Créativité culinaire",
        "description": "Développement de signatures : cold brews, lattes épicés, spécialités saisonnières."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité culinaire",
        "description": "Pâtisserie maison : croissants, brownies, banana bread, cookies."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts de restauration",
        "description": "Conseil opérationnel pour cafés et brunchs."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour sirops, textures et applications spéciales."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et utilitaires",
        "description": "Pertes en café moulu et lait."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et utilitaires",
        "description": "Identification automatique pour alternatives végétales et pâtisserie."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie minimaliste IA de référence pour Instagram, web et carte."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et réseaux sociaux",
        "description": "Instagram avec calendrier éditorial minimaliste."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et réseaux sociaux",
        "description": "Attirer les clients locaux qui recherchent « specialty coffee près de chez moi »."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et réseaux sociaux",
        "description": "Lancements saisonniers et signatures par saison."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et réseaux sociaux",
        "description": "Articles SEO sur l'origine du café et les méthodes."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et réseaux sociaux",
        "description": "Pinterest attire du trafic pour le latte art et la pâtisserie maison."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "marge après calcul des boissons"
      },
      {
        "value": "+30 %",
        "label": "ticket moyen avec pâtisserie maison"
      },
      {
        "value": "×2",
        "label": "acquisition locale avec MenuDish"
      },
      {
        "value": "12+",
        "label": "agents pour votre coffee shop"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Cartes saisonnières improvisées, signatures sans calcul",
        "Pâtisserie externe avec marge incertaine",
        "Calibrage variable entre baristas",
        "Instagram improvisé sans palette minimaliste",
        "Acquisition locale sans SEO Maps"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Signatures saisonnières avec calcul professionnel",
        "Pâtisserie maison avec Pâtisserie Créative et marge élevée",
        "Calibrage cohérent avec les modèles de Kit de Tareas",
        "GastroIMG Gen+ + InstaFlow minimalistes",
        "MenuDish Local SEO capture « specialty coffee près de chez moi »"
      ]
    },
    "galleryTitle": "Comment fonctionne un coffee shop",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : latte art, café de spécialité, pâtisserie, bar et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Sushi Bar",
    "heroSubtitle": "Maîtrisez la technique itamae avec un calcul de coût rigoureux par nigiri, gérez le poisson frais quotidien, concevez des omakase signature et capturez un branding minimaliste avec une suite d'agents d'IA gastronomique spécialisés dans le sushi bar professionnel.",
    "heroTagline": "Sushi bar avec une technique authentique et une marge réelle",
    "badge": "Pour sushi bars, omakase et sushi shops",
    "painsTitle": "Ce qu'un Sushi Bar Ne Peut Pas Manquer de Résoudre",
    "pains": [
      "Poisson frais quotidien pour nigiri et sashimi avec un coût volatil et des pertes strictes par processus de filetage",
      "Standardiser le shari (riz à sushi) à chaque service avec un équilibre technique de vinaigre, sucre et sel",
      "Coordonner la technique itamae avec cohérence : coupe, pression, température du riz, neta à température optimale",
      "Se différencier dans une zone concurrentielle avec des omakase signature, du fish-of-the-day et un storytelling des fournisseurs",
      "Attirer des clients premium avec une expérience face à l'itamae au comptoir (pas à table)",
      "Attirer les commandes de livraison sans perdre la qualité du sushi (fenêtre optimale de 1 à 2 heures)"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide dans un Sushi Bar",
    "features": [
      {
        "icon": "Fish",
        "title": "Cuisine Japonaise",
        "description": "Agent spécialisé en sushi professionnel : technique itamae, équilibre du shari, filetage, neta à température optimale."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour nigiri signature et omakase contemporain avec une base authentique."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Pour fermentations et techniques avancées de cuisine japonaise."
      },
      {
        "icon": "Calculator",
        "title": "Coûts de revient par nigiri et omakase",
        "description": "Cuisine Japonaise fournit recette + coût de revient CSV ; Kit de Escandallos Pro le gère avec coût réel par pièce et omakase."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles : filetage, préparation shari, mise itamae, fermeture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC sushi",
        "description": "Traçabilité du poisson pour sushi et températures critiques."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Pour saké, whisky japonais et accords professionnels."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Hanami, Nouvel An japonais, Journée du Sushi, événements premium."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie minimaliste IA de référence + Instagram pour sushi bar premium."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Sushi Bar avec AI Chef Pro",
    "workflow": [
      "08:00 · Ouverture — checklist Kit de Tareas : réception du poisson frais quotidien, filetage des blocs, préparation du shari (vinaigre + sucre + sel équilibrés).",
      "10:00 · Cuisine Japonaise — vous développez un nouveau nigiri signature de hamachi avec yuzu kosho et wasabi frais. Recette + coût de revient CSV.",
      "11:00 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels du poisson du jour, vous validez la marge par nigiri et par omakase.",
      "13:00 · Service de midi — sushi bar à plein avec itamae travaillant face au client.",
      "17:00 · Briefing à l'équipe — explication du nouveau nigiri et accords avec saké.",
      "20:00 · Service du soir — omakase signature, pics coordonnés.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez une image de référence minimaliste du nouveau nigiri.",
      "23:00 · Fermeture — nettoyage en profondeur, APPCC signé."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Sushi Bar",
    "productIds": [
      "guia-restaurante-japones",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cuisine Japonaise a changé notre fonctionnement. L'équilibre du shari est désormais cohérent, l'omakase a un coût de revient professionnel avec une marge validée pièce par pièce. L'acquisition de clients premium avec GastroIMG Gen+ a augmenté de 40 % en 6 mois.",
    "testimonialAuthor": "Akio Yamamoto",
    "testimonialRole": "Itamae et propriétaire, sushi bar contemporain",
    "faqTitle": "Questions Fréquentes des Sushi Bars",
    "faqs": [
      {
        "q": "Est-ce que ça convient pour un sushi bar décontracté ou un omakase premium ?",
        "a": "Pour les deux. Cuisine Japonaise couvre du sushi traditionnel à l'omakase d'auteur."
      },
      {
        "q": "Est-ce que ça couvre la technique itamae ?",
        "a": "Oui. Cuisine Japonaise raisonne comme un itamae professionnel : technique de filetage, équilibre du shari, neta et combinaisons."
      },
      {
        "q": "Comment gérer le coût du poisson frais ?",
        "a": "Kit de Escandallos Pro recalcule instantanément la marge lorsque vous mettez à jour les prix du jour."
      },
      {
        "q": "Est-ce que ça génère du contenu visuel minimaliste ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre pièce réelle."
      },
      {
        "q": "Comment m'aide-t-il avec l'omakase et les événements premium ?",
        "a": "Gastro Calendar planifie l'omakase saisonnier, Hanami, Nouvel An japonais avec des menus dégustation premium."
      }
    ],
    "ctaTitle": "Votre sushi bar avec une technique authentique et une marge réelle.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "IA pour Sushi Bar : Itamae, Omakase et Coûts de Revient | AI Chef Pro",
      "description": "Suite d'IA pour sushi bars : Cuisine Japonaise, Fermentus, coûts de revient par nigiri, omakase et branding minimaliste. Commencez dès aujourd'hui.",
      "keywords": "IA sushi bar, logiciel sushi, coûts de revient sushi, itamae professionnel, omakase IA, technique japonaise",
      "ogImage": "https://aichef.pro/og/use-cases/sushi-bar.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Sushi Bar dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding de 2 minutes dans lequel vous lui racontez quel type de sushi bar vous exploitez (sushi bar décontracté, omakase premium, kaiten, sushi bar avec cuisine chaude), la taille de l'équipe, la ville et la spécialité.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Sushi Bar",
    "apps": [
      {
        "name": "Cuisine Japonaise",
        "category": "Recueils de recettes d'Asie",
        "description": "Sushi professionnel : technique itamae, sashimi, omakase."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Nigiri signature et omakase avec recette + coût de revient CSV."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "Fermentations pour techniques avancées."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords avec saké, whisky japonais et bière."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'Entreprise",
        "description": "Comptoir de saké et whisky japonais."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes lors du filetage du poisson."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification du poisson, fruits de mer, soja, gluten."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Photographie minimaliste IA de référence."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram minimaliste pour sushi bar premium."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients qui recherchent \"sushi près de moi\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Hanami, Nouvel An japonais, omakase saisonnier."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour textures avancées."
      }
    ],
    "metrics": [
      {
        "value": "+6 pp",
        "label": "marge après calcul de coût de l'omakase"
      },
      {
        "value": "+40 %",
        "label": "acquisition premium en 6 mois"
      },
      {
        "value": "−20 %",
        "label": "pertes lors du filetage"
      },
      {
        "value": "12+",
        "label": "agents pour votre sushi bar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Shari improvisé, équilibre incohérent",
        "Coûts de revient sans prix du poisson du jour",
        "Omakase improvisé sans coût de revient",
        "Instagram sans palette minimaliste",
        "Acquisition locale sans SEO"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Shari et technique avec un critère professionnel",
        "Coût de revient en temps réel avec le prix du jour",
        "Omakase avec coût de revient validé pièce par pièce",
        "GastroIMG Gen+ + InstaFlow minimalistes",
        "MenuDish Local SEO capture \"sushi près de moi\""
      ]
    },
    "galleryTitle": "Comment Fonctionne un Sushi Bar",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : counter, omakase, poisson, saké et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Gastrobar et Bar à Tapas",
    "heroSubtitle": "Concevez une carte de tapas et pintxos avec une fiche technique professionnelle, gérez le vermouth et les vins au verre, planifiez des événements et intégrez un branding espagnol authentique grâce à une suite d'agents d'IA gastronomique spécialisés en gastrobar et en cuisine espagnole.",
    "heroTagline": "Des tapas avec une technique authentique et une vraie marge",
    "badge": "Pour gastrobars, bars à tapas, pintxos et bars à vins",
    "painsTitle": "Ce qu'un gastrobar doit absolument résoudre",
    "pains": [
      "Carte de tapas avec de nombreuses variantes (froides, chaudes, pintxos, portions) tout en maintenant un food cost cohérent",
      "Pertes sur produits frais (anchois, jambon, fruits de mer), pain et charcuterie à durée de conservation courte",
      "Standardiser les tapas signature d'un service à l'autre avec régularité et rapidité de service",
      "Gestion du vermouth, des vins au verre et des bières avec une marge élevée et une rotation correcte",
      "Se différencier avec un produit de qualité, un branding espagnol authentique et le storytelling de fournisseurs artisanaux",
      "Attirer la clientèle des événements privés et des dégustations avec des accords professionnels"
    ],
    "featuresTitle": "Comment AI Chef Pro aide dans un gastrobar",
    "features": [
      {
        "icon": "Wine",
        "title": "Restaurants Décontractés AI+",
        "description": "Conseils opérationnels pour gastrobars et bars à tapas."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Espagnole + Cuisine Créative",
        "description": "Recueils de recettes spécialisés : tapas traditionnelles, pintxos basques, portions du marché, fusions."
      },
      {
        "icon": "Calculator",
        "title": "Fiches techniques par tapa et par portion",
        "description": "Cuisine Créative fournit recette + fiche technique CSV ; Kit de Escandallos Pro gère le tout avec un coût réel par tapa et un food cost %."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Vermouths, vins espagnols au verre, bières artisanales et accords avec tapas."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Bar",
        "description": "Modèles : préparation des tapas, mise en place du bar, vermouth, fermeture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC bar",
        "description": "Traçabilité du jambon, des charcuteries, des anchois et des fruits de mer frais."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Journée mondiale de la tapa, San Fermín, fêtes locales, événements privés."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie espagnole artisanale par IA + Instagram pour attirer les locaux et les touristes."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Attirer les clients qui recherchent \"tapas à proximité\" ou \"gastrobar [ville]\"."
      }
    ],
    "workflowTitle": "Une journée réelle dans un gastrobar avec AI Chef Pro",
    "workflow": [
      "11:00 · Ouverture — checklist Kit de Tareas : préparation des tapas froides, montage du jambonnier, mise en place du bar, contrôle du vermouth en pression.",
      "12:30 · Cuisine Espagnole + Cuisine Créative — vous développez une nouvelle tapa signature d'anchois marinés maison avec piparra et huile de tomate. Recette + fiche technique CSV.",
      "13:30 · Kit de Escandallos Pro — vous chargez le CSV avec vos prix réels, validez la marge par tapa et le food cost %.",
      "14:00 · Service de midi — pic de fréquentation avec vermouth et tapas, mise en place impeccable.",
      "17:00 · Pause — Bar & Lounge AI+ valide des accords avec des vins Albariño et Verdejo pour de nouvelles tapas.",
      "19:00 · Service du soir — pics d'affluence avec des bières artisanales et des vins au verre.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez une image de référence et des posts.",
      "00:00 · Fermeture — nettoyage, HACCP signé, contrôle des stocks."
    ],
    "productsTitle": "Modèles et Kits recommandés pour un gastrobar",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cuisine Espagnole + Bar & Lounge AI+ ont rehaussé notre niveau. Les tapas signature ont désormais une fiche technique professionnelle avec marge validée, les accords vins au verre sont cohérents et nous avons augmenté le ticket moyen de 15 % en 4 mois. L'acquisition locale avec MenuDish + GastroIMG est multipliée par 2.",
    "testimonialAuthor": "Iñaki Etxeberria",
    "testimonialRole": "Propriétaire, gastrobar contemporain à Donostia",
    "faqTitle": "Questions fréquentes sur les gastrobars",
    "faqs": [
      {
        "q": "Convient-il pour un gastrobar décontracté, un bar à tapas traditionnel, un bar à pintxos basques ou un bar à vins avec tapas ?",
        "a": "Pour les quatre. Cuisine Espagnole + Restaurants Décontractés AI+ couvrent des tapas traditionnelles aux gastrobars contemporains."
      },
      {
        "q": "Couvre-t-il le vermouth, les vins et les bières avec des accords ?",
        "a": "Oui. Bar & Lounge AI+ couvre le vermouth, les vins espagnols au verre, les bières artisanales et les accords avec tapas."
      },
      {
        "q": "Comment gérer les pertes sur jambon et produits frais ?",
        "a": "Rendement GenCal fournit des données par processus (découpe du jambon, anchois, fruits de mer). Elles s'intègrent à la fiche technique."
      },
      {
        "q": "Génère-t-il du contenu visuel pour Instagram ?",
        "a": "Oui. GastroIMG Gen+ génère des images de référence. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre véritable tapa."
      },
      {
        "q": "Comment m'aide-t-il avec les événements privés et les dégustations ?",
        "a": "Gastro Calendar planifie des dégustations avec des vignerons, des événements privés, San Fermín et des fêtes locales."
      }
    ],
    "ctaTitle": "Votre gastrobar avec une vraie marge et une technique authentique.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "IA pour Gastrobar et Bar à Tapas : Tapas, Fiches Techniques et Accords | AI Chef Pro",
      "description": "Suite d'IA pour gastrobars : Cuisine Espagnole, Bar & Lounge AI+, fiches techniques par tapa, vermouth et vins au verre. Commencez dès aujourd'hui.",
      "keywords": "IA gastrobar, logiciel bar à tapas, fiches techniques tapa, pintxos IA, vermouth tapas, gastrobar contemporain",
      "ogImage": "https://aichef.pro/og/use-cases/gastrobar-tapas.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre gastrobar dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding de 2 minutes au cours duquel vous lui indiquez quel type de gastrobar vous exploitez (gastrobar contemporain, bar à tapas traditionnel, bar à pintxos basques, bar à vins avec tapas), la taille de l'équipe, la ville et la spécialité.",
    "appsTitle": "Les agents IA que vous allez utiliser dans votre gastrobar",
    "apps": [
      {
        "name": "Cuisine Espagnole",
        "category": "Recueils de recettes d'Europe",
        "description": "Tapas traditionnelles, pintxos, portions du marché."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Tapas signature contemporaines avec recette + fiche technique CSV."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts de Restauration",
        "description": "Vermouth, vins espagnols, bières et accords."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts de Restauration",
        "description": "Conseils opérationnels pour gastrobars."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords avec vins et bières pour tapas."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour textures et techniques avancées."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes sur jambon, anchois, fruits de mer et charcuteries."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification par tapa : gluten, produits laitiers, fruits de mer, sulfites."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissances Gastro",
        "description": "Photographie espagnole artisanale IA de référence."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram pour attirer locaux et touristes."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients qui recherchent \"tapas à proximité\"."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Journée de la Tapa, San Fermín, fêtes locales."
      }
    ],
    "metrics": [
      {
        "value": "+5 pts",
        "label": "marge après chiffrage des tapas"
      },
      {
        "value": "+15 %",
        "label": "ticket moyen en 4 mois"
      },
      {
        "value": "×2",
        "label": "acquisition locale avec MenuDish"
      },
      {
        "value": "12+",
        "label": "agents pour votre gastrobar"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Tapas signature improvisées sans fiche technique",
        "Accords avec vins sans base scientifique",
        "Pertes sur jambon et produits frais sans traçabilité",
        "Instagram improvisé",
        "Acquisition locale sans SEO"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Tapas signature avec fiche technique professionnelle",
        "Accords avec Bar & Lounge AI+ et Food Pairing AI",
        "Pertes contrôlées avec Rendement GenCal",
        "GastroIMG Gen+ + InstaFlow artisanal",
        "MenuDish Local SEO capture \"tapas à proximité\""
      ]
    },
    "galleryTitle": "Comment fonctionne un gastrobar",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : tapas, vermouth, jambon, vins et équipe. Des images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Food Truck",
    "heroSubtitle": "Concevez une carte compacte avec des fiches techniques rigoureuses, gérez la préparation ajustée à l'espace limité, planifiez des événements et des itinéraires, et créez un branding viral avec une suite d'agents IA gastronomiques spécialisés dans le food truck professionnel.",
    "heroTagline": "Food truck avec marge réelle et opérations ajustées",
    "badge": "Pour food trucks, cuisines mobiles et street food",
    "painsTitle": "Ce Qu'un Food Truck Doit Absolument Résoudre",
    "pains": [
      "Carte compacte et soignée (5-10 plats max) avec coût optimisé grâce à un processus efficace",
      "Espace limité : préparation ajustée, mise en place compacte, équipements partagés, stockage minimal",
      "Pertes contrôlées sur les produits frais avec des achats ajustés au volume de l'événement",
      "Standardiser la technique d'un service à l'autre avec du personnel en rotation et des équipes changeantes",
      "Se différencier avec un branding visuel iconique, des réseaux sociaux actifs et un storytelling centré sur le fait main",
      "Planifier des itinéraires d'événements (festivals, foires, marchés, événements privés) avec une marge élevée"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Food Truck",
    "features": [
      {
        "icon": "Truck",
        "title": "Food Truck AI+",
        "description": "Agent spécialisé dans les food trucks et les cuisines mobiles : exploitation, préparation, événements, branding et itinéraires."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour les signatures de food truck : smash burgers, baos, tacos, poulets croustillants avec une fiche technique professionnelle."
      },
      {
        "icon": "Calculator",
        "title": "Fiches techniques par plat",
        "description": "Cuisine Créative fournit recette + fiche technique CSV ; Kit de Escandallos Pro la gère avec un coût réel ajusté à l'exploitation mobile."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles : pré-événement, préparation ajustée, montage, service rapide, fermeture, réapprovisionnement."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC food truck",
        "description": "Traçabilité adaptée à l'exploitation mobile : températures, eau, déchets."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Festivals, foires, marchés, événements d'entreprise privés."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie street food virale par IA + Instagram avec calendrier éditorial actif."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Attirer les clients qui recherchent « food truck à proximité » ou « street food à [ville] »."
      },
      {
        "icon": "Sparkles",
        "title": "Rendement GenCal",
        "description": "Pertes sur produits frais avec achats ajustés au volume de l'événement."
      }
    ],
    "workflowTitle": "Une Journée Réelle d'un Food Truck avec AI Chef Pro",
    "workflow": [
      "08:00 · Ouverture — checklist Kit de Tareas : vérification des équipements, mise en place compacte, préparation ajustée au volume de l'événement.",
      "10:00 · Food Truck AI+ — vous développez un nouveau smash burger signature avec fromage américain et bacon fumé. Recette + fiche technique CSV.",
      "11:00 · Kit de Escandallos Pro — vous chargez le CSV avec les prix réels et le volume estimé de l'événement, vous validez la marge.",
      "12:00 · Arrivée sur l'événement (festival de musique) — montage, branchement électrique, contrôle HACCP.",
      "13:00 · Service du midi — pic d'activité avec files d'attente maîtrisées, préparation efficace.",
      "17:00 · Pause — réapprovisionnement, contrôle des pertes et caisse du premier service.",
      "20:00 · Service du soir — pic plus important, GastroIMG Gen+ a déjà la photo du jour programmée sur Instagram.",
      "00:00 · Fermeture — nettoyage, HACCP signé, planification du prochain événement avec Gastro Calendar."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Food Truck",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Food Truck AI+ et Cuisine Créative ont transformé notre exploitation. La carte est plus compacte, les fiches techniques par plat reflètent une marge réelle avec des achats ajustés au volume de l'événement, et l'acquisition avec InstaFlow + GastroIMG a triplé nos réservations pour des événements privés en 6 mois.",
    "testimonialAuthor": "Marcos Bermúdez",
    "testimonialRole": "Propriétaire, food truck artisanal",
    "faqTitle": "Questions Fréquentes sur les Food Trucks",
    "faqs": [
      {
        "q": "Est-ce que cela convient pour un food truck décontracté, gastronomique ou une cuisine mobile pour événements privés ?",
        "a": "Pour les trois. Food Truck AI+ couvre du décontracté au gastronomique, en passant par la cuisine mobile pour mariages et événements d'entreprise."
      },
      {
        "q": "Comment établir une fiche technique avec des achats ajustés à l'événement ?",
        "a": "Kit de Escandallos Pro recalcule instantanément la marge selon le volume estimé de l'événement."
      },
      {
        "q": "Est-ce que cela couvre l'exploitation mobile avec un espace limité ?",
        "a": "Oui. Food Truck AI+ raisonne comme un opérateur professionnel : préparation compacte, mise en place efficace, équipements partagés."
      },
      {
        "q": "Est-ce que cela génère du contenu viral pour Instagram et TikTok ?",
        "a": "Oui. GastroIMG Gen+ + InstaFlow AI Pro génèrent du contenu viral avec un calendrier éditorial actif. Rappelez-vous que l'image IA est une référence visuelle : la photo finale, c'est vous qui la faites avec votre plat réel."
      },
      {
        "q": "Comment cela m'aide-t-il avec les événements et les itinéraires ?",
        "a": "Gastro Calendar planifie des festivals, foires, marchés et événements privés avec une planification d'itinéraires."
      }
    ],
    "ctaTitle": "Votre food truck avec une marge réelle et des opérations ajustées.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "IA pour Food Truck : Carte, Fiches Techniques et Événements | AI Chef Pro",
      "description": "Suite d'IA pour food trucks : Food Truck AI+, fiches techniques par plat, planification d'événements, branding viral et HACCP. Commencez aujourd'hui.",
      "keywords": "IA food truck, logiciel food truck, fiches techniques food truck, street food IA, cuisine mobile, événements food truck",
      "ogImage": "https://aichef.pro/og/use-cases/food-truck.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Food Truck dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding de 2 minutes où vous lui décrivez le type de food truck que vous exploitez (décontracté, gastronomique, événements privés, marché, festivals), la taille de l'équipe, la spécialité et les zones d'opération.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Food Truck",
    "apps": [
      {
        "name": "Food Truck AI+",
        "category": "Concepts d'Entreprise",
        "description": "Agent spécialisé dans les food trucks et les cuisines mobiles."
      },
      {
        "name": "Burger Pro AI+",
        "category": "Concepts d'Entreprise",
        "description": "Pour les food trucks de smash burgers et les restaurants de burgers gastronomiques."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Signatures avec recette + fiche technique CSV."
      },
      {
        "name": "Restaurants Décontractés AI+",
        "category": "Concepts d'Entreprise",
        "description": "Conseil opérationnel pour la restauration décontractée."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes avec achats ajustés à l'événement."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique par plat."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastronomique",
        "description": "Photographie street food virale par IA de référence."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial actif."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Attirer les clients qui recherchent « food truck à proximité »."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Festivals, foires, marchés, événements privés."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capte du trafic pour la street food."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching pour la gestion du stress lors d'événements à forte affluence."
      }
    ],
    "metrics": [
      {
        "value": "+5 pts",
        "label": "marge après avoir chiffré la carte"
      },
      {
        "value": "×3",
        "label": "réservations d'événements privés en 6 mois"
      },
      {
        "value": "−20 %",
        "label": "pertes avec achats ajustés"
      },
      {
        "value": "12+",
        "label": "agents pour votre food truck"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Carte étendue avec un coût matière incertain.",
        "Achat de produits sans ajustement au volume de l'événement.",
        "Pertes élevées sur les produits frais.",
        "Instagram improvisé, sans contenu viral.",
        "Événements privés réservés manuellement."
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Carte compacte avec une fiche technique professionnelle.",
        "Achats ajustés au volume estimé de l'événement.",
        "Pertes contrôlées avec Rendement GenCal.",
        "GastroIMG Gen+ + InstaFlow pour du contenu viral.",
        "Événements privés réservés avec une proposition professionnelle."
      ]
    },
    "galleryTitle": "Comment Fonctionne un Food Truck",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : food truck, préparation, plancha, service et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "IA pour Restaurant Italien",
    "heroSubtitle": "Maîtrisez la technique italienne authentique avec un calcul de coût rigoureux par plat, gérez les pâtes fraîches et les sauces traditionnelles, concevez des cartes saisonnières et capturez le branding trattoria avec une suite d'agents d'IA gastronomique spécialisés en cuisine italienne professionnelle.",
    "heroTagline": "Cuisine italienne avec une technique authentique et une marge réelle",
    "badge": "Pour les trattorias, ristoranti et restaurants italiens",
    "painsTitle": "Ce Qu'un Restaurant Italien Ne Peut Pas Manquer de Résoudre",
    "pains": [
      "Pâtes fraîches quotidiennes avec un équilibre précis de semoule, d'œuf et d'eau, technique d'extrusion et formats régionaux",
      "Sauces traditionnelles (ragù, carbonara, cacio e pepe, pesto) qui nécessitent une consistance technique équipe après équipe",
      "Pertes en pâtes fraîches, fromage, charcuteries italiennes (mortadelle, prosciutto), tomates San Marzano",
      "Standardiser les plats signature régionaux (Rome, Toscane, Émilie, Sicile) avec une technique authentique",
      "Se différencier dans une zone concurrentielle avec des produits italiens importés, un branding trattoria et un storytelling régional",
      "Capter les commandes d'événements privés, de dîners d'entreprise et de mariages italiens avec une marge élevée"
    ],
    "featuresTitle": "Comment AI Chef Pro Aide un Restaurant Italien",
    "features": [
      {
        "icon": "UtensilsCrossed",
        "title": "Cuisine Italienne",
        "description": "Agent spécialisé en cuisine italienne authentique : pâtes, sauces, risotto, ossobuco, technique régionale."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Pour les levains italiens (focaccia, pane casareccio, pizza alla pala) et la technique de fermentation."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Pour les plats signature contemporains et la dégustation avec une base italienne authentique."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Vins italiens au verre et accords avec la cuisine régionale (Chianti, Barolo, Amarone, Prosecco)."
      },
      {
        "icon": "Calculator",
        "title": "Calculs de coût par plat",
        "description": "Cuisine Italienne fournit recette + calcul de coût CSV ; Kit de Escandallos Pro le gère avec un coût réel par plat et le food cost %."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles : préparation pâtes fraîches, sauces traditionnelles, mise en place pizza, service, fermeture."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC italien",
        "description": "Traçabilité des pâtes fraîches, des fromages italiens, des charcuteries et des sauces."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Fêtes italiennes (Ferragosto, Carnevale, Pasqua, Natale), événements privés et mariages italiens."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + InstaFlow AI Pro",
        "description": "Photographie éditoriale trattoria IA + Instagram avec storytelling régional."
      }
    ],
    "workflowTitle": "Une Journée Réelle dans un Restaurant Italien avec AI Chef Pro",
    "workflow": [
      "08:00 · Ouverture — checklist Kit de Tareas : préparation de pâtes fraîches quotidiennes (tagliatelle, ravioli, pappardelle), préparation de sauces traditionnelles.",
      "10:00 · Cuisine Italienne — vous développez un nouveau plat signature de tagliolini al limone avec des scampi de la pêche du jour. Recette + calcul de coût CSV.",
      "11:00 · Kit de Escandallos Pro — vous chargez le CSV avec les prix réels des scampi et des produits italiens, vous validez la marge et le food cost %.",
      "12:00 · Bar & Lounge AI+ — vous validez l'accord avec un Vermentino di Sardegna.",
      "13:00 · Service de midi — pic avec pâtes fraîches, sauces traditionnelles et vins italiens au verre.",
      "17:00 · Briefing à l'équipe — explication du nouveau plat et des accords.",
      "19:00 · Service du dîner — pics coordonnés avec la cuisine principale.",
      "22:00 · GastroIMG Gen+ + InstaFlow AI Pro — vous générez une image éditoriale trattoria et des publications."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Restaurant Italien",
    "productIds": [
      "kit-tareas",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-gestion-personal",
      "pro-prompts-ebook"
    ],
    "testimonialQuote": "Cuisine Italienne + Bar & Lounge AI+ ont transformé notre restaurant. Pâtes fraîches constantes, sauces traditionnelles avec un équilibre technique, accords avec des vins italiens au verre documentés. Nous avons augmenté la marge de 5 points et les clients réguliers ont augmenté de 30 % en 6 mois.",
    "testimonialAuthor": "Lorenzo Bianchi",
    "testimonialRole": "Chef et propriétaire, trattoria contemporaine",
    "faqTitle": "Questions Fréquentes des Restaurants Italiens",
    "faqs": [
      {
        "q": "Convient-il à une trattoria décontractée, à un ristorante contemporain ou à une cuisine régionale italienne ?",
        "a": "Pour les trois. Cuisine Italienne couvre de la trattoria traditionnelle à la haute cuisine italienne d'auteur avec une technique régionale authentique."
      },
      {
        "q": "Couvre-t-il les pâtes fraîches et les sauces traditionnelles ?",
        "a": "Oui. Cuisine Italienne raisonne comme un cuisinier italien professionnel : équilibre de la pâte, formats régionaux, technique des sauces traditionnelles."
      },
      {
        "q": "Couvre-t-il les vins italiens et les accords ?",
        "a": "Oui. Bar & Lounge AI+ couvre le Chianti, le Barolo, l'Amarone, le Prosecco et les accords avec la cuisine régionale."
      },
      {
        "q": "Génère-t-il du contenu visuel pour Instagram ?",
        "a": "Oui. GastroIMG Gen+ génère des images éditoriales trattoria. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre plat réel."
      },
      {
        "q": "Comment m'aide-t-il avec les événements et les fêtes italiennes ?",
        "a": "Gastro Calendar planifie Ferragosto, Carnevale, Pasqua, Natale et les événements privés avec des menus italiens."
      }
    ],
    "ctaTitle": "Votre restaurant italien avec une technique authentique et une marge réelle.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "IA pour Restaurant Italien : Pâtes, Calculs de Coût et Vins | AI Chef Pro",
      "description": "Suite d'IA pour restaurants italiens : Cuisine Italienne, calculs de coût, pâtes fraîches, vins italiens et branding trattoria. Commencez aujourd'hui.",
      "keywords": "IA restaurant italien, logiciel trattoria, calcul de coût pâtes, cuisine italienne IA, vins italiens, ristorante contemporain",
      "ogImage": "https://aichef.pro/og/use-cases/restaurante-italiano.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Restaurant Italien dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent « Qui suis-je ? », un onboarding de 2 minutes pendant lequel vous lui racontez quel type de concept italien vous exploitez (trattoria, ristorante contemporain, cuisine régionale, italien d'auteur), la taille de l'équipe, la ville et la spécialité régionale.",
    "appsTitle": "Les Agents IA que Vous Allez Utiliser dans Votre Restaurant Italien",
    "apps": [
      {
        "name": "Cuisine Italienne",
        "category": "Recettes d'Europe",
        "description": "Pâtes, sauces, risotto, ossobuco avec une technique régionale authentique."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Plats signature contemporains italiens."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité Culinaire",
        "description": "Levains italiens (focaccia, pane casareccio)."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts de Restauration",
        "description": "Vins italiens et accords régionaux."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords avec une technique authentique italienne."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour les textures et la technique avancée."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes en pâtes fraîches, fromage, charcuteries."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification par plat."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissances Gastro",
        "description": "Photographie éditoriale trattoria IA de référence."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial italien."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Capter les clients qui recherchent « italien près de chez moi »."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Fêtes italiennes et événements privés."
      }
    ],
    "metrics": [
      {
        "value": "+5 pp",
        "label": "de marge après calcul des coûts des plats"
      },
      {
        "value": "+30 %",
        "label": "de clients réguliers en 6 mois"
      },
      {
        "value": "−20 %",
        "label": "de pertes en pâtes et charcuteries"
      },
      {
        "value": "12+",
        "label": "agents pour votre trattoria"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Pâtes fraîches improvisées, équilibre variable",
        "Sauces traditionnelles sans consistance technique",
        "Accords avec des vins italiens sans base professionnelle",
        "Pertes en produits italiens importés sans traçabilité",
        "Instagram sans storytelling régional"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Pâtes fraîches avec un équilibre technique documenté",
        "Sauces traditionnelles régulières avec un savoir-faire professionnel",
        "Accords avec Bar & Lounge AI+ documentés",
        "Pertes contrôlées avec Rendement GenCal",
        "GastroIMG Gen+ + InstaFlow éditorial trattoria"
      ]
    },
    "galleryTitle": "Comment Fonctionne un Restaurant Italien",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : pâtes fraîches, plats, cuisine, vins et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "Comment faire des calculs de coûts avec l'IA",
    "heroSubtitle": "Calculez le coût réel par plat, le food cost % et le prix suggéré en minutes au lieu de jours : recette + fiche technique CSV automatique avec coût horaire d'atelier, pertes intégrées et marge validée en temps réel avec une suite d'agents d'IA gastronomique.",
    "heroTagline": "Calculs de coûts professionnels en minutes, pas en heures",
    "badge": "Tâche : Calculs de coûts et costing",
    "painsTitle": "Ce que coûte le calcul de coûts à la main",
    "pains": [
      "Une semaine de calculatrice et de serviettes pour calculer les coûts d'une nouvelle carte de 30 plats",
      "Sans coût horaire d'atelier intégré, des plats complexes à perte sans le savoir",
      "Pertes estimées à vue d'œil (30 % sur certaines coupes), pas de données réelles par processus",
      "Quand le prix du fournisseur change, tout est déséquilibré et ne se met pas à jour",
      "Manque de critère pour décider du food cost cible selon le type de plat (signature, entrée, dessert)",
      "Sans traçabilité du calcul : si on vous demande un audit, vous ne savez pas d'où vient chaque chiffre"
    ],
    "featuresTitle": "Comment AI Chef Pro résout les calculs de coûts",
    "features": [
      {
        "icon": "Calculator",
        "title": "Cuisine Créative + fiche technique CSV",
        "description": "Tout agent créatif (Cuisine, Pâtisserie, Glacerie, Chocolaterie) livre recette + fiche technique CSV avec équilibre technique et coût horaire d'atelier intégré."
      },
      {
        "icon": "BarChart3",
        "title": "Rendement GenCal",
        "description": "Données précises de pertes par processus (découpe, torréfaction, refroidissement, vitrine, formage) intégrées automatiquement au CSV."
      },
      {
        "icon": "Beaker",
        "title": "Agent Sosa Ingredients",
        "description": "Catalogue Sosa avec prix de référence pour ingrédients techniques professionnels."
      },
      {
        "icon": "Sparkles",
        "title": "Calcula Pax + Conversor Ing",
        "description": "Adapte les recettes à 2, 6, 12, 100 pax sans perdre en précision ; convertisseur automatique de poids et mesures."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Escandallos Pro",
        "description": "Modèles Excel téléchargeables qui reçoivent le CSV et calculent la marge réelle, le food cost % et le prix suggéré instantanément."
      },
      {
        "icon": "BookOpen",
        "title": "Fiches techniques avec coût",
        "description": "Chaque recette livre une fiche technique complète avec coût, allergènes, technique et storytelling pour la salle."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Image de référence générée par IA du plat calculé pour visualiser avant de cuisiner (pas la photo définitive)."
      },
      {
        "icon": "BookOpen",
        "title": "Pro Prompts eBook",
        "description": "eBook avec 300+ prompts professionnels pour calculer les coûts, valider et optimiser les coûts avec l'IA gastronomique."
      },
      {
        "icon": "Wine",
        "title": "Applicable à tout concept",
        "description": "Restaurant, café, pâtisserie, glacier, chocolaterie, pizzeria, bar, traiteur, hôtel : le flux est le même."
      }
    ],
    "workflowTitle": "Comment réaliser des calculs de coûts avec l'IA en 4 étapes",
    "workflow": [
      "1. Cuisine Créative (ou l'agent créatif de votre concept : Pâtisserie, Glacerie, Chocolaterie, Cuisine Italienne, Mexicaine, Péruvienne, Japonaise) — vous développez ou chargez la recette. L'agent IA livre recette + fiche technique CSV avec équilibre technique, pertes estimées et storytelling.",
      "2. Agent Sosa Ingredients + Rendement GenCal — l'IA enrichit le CSV avec des prix de référence et des pertes réelles par processus de votre type de cuisine.",
      "3. Kit de Escandallos Pro (modèle Excel téléchargeable, 12 €) — vous chargez le CSV avec vos prix réels de fournisseurs. L'Excel calcule la marge réelle, le food cost %, le prix suggéré par canal (salle, livraison, événements) et la proposition économique.",
      "4. Calcula Pax + Conversor Ing — si vous avez besoin d'adapter la recette pour des banquets (50, 100, 300 pax) ou de convertir des unités, les agents IA le font instantanément en maintenant le calcul de coûts."
    ],
    "productsTitle": "Modèles et Kits recommandés pour le calcul de coûts",
    "productIds": [
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "kit-inventario",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Ce qui était autrefois une semaine de calculatrice est maintenant 30 minutes. Cuisine Créative livre la fiche technique CSV, Rendement GenCal l'enrichit avec des données réelles et le Kit de Escandallos Pro me donne une marge validée. Nous avons renouvelé la carte de 28 plats en une seule journée et augmenté la marge de 6 points en découvrant des plats à perte que nous ne savions pas.",
    "testimonialAuthor": "Pablo Ruiz",
    "testimonialRole": "Chef et propriétaire, restaurant décontracté avec 4 points de vente",
    "faqTitle": "Questions fréquentes sur les calculs de coûts avec l'IA",
    "faqs": [
      {
        "q": "Est-ce que cela fonctionne pour tout type de cuisine ?",
        "a": "Oui. Le flux est le même pour la cuisine créative, la pâtisserie, la glacerie, la chocolaterie, la pizzeria, la cuisine mexicaine, péruvienne, japonaise, italienne, végétale ou tout autre concept. Seul l'agent créatif de départ change."
      },
      {
        "q": "Comment gère-t-il le coût horaire d'atelier ?",
        "a": "Le CSV inclut un champ de temps de préparation par processus (mélange, formage, cuisson, décoration). Le Kit de Escandallos Pro multiplie par votre coût horaire réel (salaire + charges) et l'intègre à la marge réelle."
      },
      {
        "q": "Comment refléter le prix variable des fournisseurs (cacao, poisson, viande) ?",
        "a": "Le Kit de Escandallos Pro recalcule instantanément la marge lorsque vous mettez à jour les prix. Rendement GenCal ajoute le coût des pertes par processus. Le plat reflète toujours le coût actuel, pas celui d'il y a trois mois."
      },
      {
        "q": "Couvre-t-il l'adaptation pour les banquets et événements ?",
        "a": "Oui. Calcula Pax adapte les recettes à tout nombre de convives sans perdre en précision ; le Kit de Escandallos Pro recalcule le coût par personne et la proposition économique pour le client corporatif."
      },
      {
        "q": "Génère-t-il une image de référence du plat calculé ?",
        "a": "Oui. GastroIMG Gen+ génère une image de référence visuelle du plat. Rappelez-vous que l'image IA est de référence : la photo définitive du calcul de coûts, vous la faites avec votre plat réel dressé."
      }
    ],
    "ctaTitle": "Vos calculs de coûts en minutes avec une marge réelle validée.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "Comment faire des calculs de coûts avec l'IA : coût réel, marge et food cost | AI Chef Pro",
      "description": "Suite d'IA pour les calculs de coûts professionnels : recette + CSV avec coût horaire d'atelier, pertes intégrées, marge validée. Commencez dès aujourd'hui.",
      "keywords": "calculs de coûts avec IA, calculer le food cost, coût réel plat, fiche technique CSV, kit de calcul de coûts, food cost restaurant",
      "ogImage": "https://aichef.pro/og/use-cases/task-escandallos-con-ia.jpg"
    },
    "personalizationTitle": "Personnalisé pour votre cuisine dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec l'agent «Qui suis-je ?», un onboarding de 2 minutes dans lequel vous lui dites quel type de cuisine vous travaillez et le flux de calcul de coûts s'adapte à votre concept : Cuisine Créative pour restaurant, Pâtisserie Créative pour atelier, Glacerie Créative pour gelateria, etc.",
    "appsTitle": "Les agents IA que vous utilisez pour les calculs de coûts",
    "apps": [
      {
        "name": "Cuisine Créative",
        "category": "Créativité culinaire",
        "description": "Recettes + fiche technique CSV avec équilibre technique et pertes estimées."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité culinaire",
        "description": "Recettes sucrées avec coût horaire d'atelier intégré."
      },
      {
        "name": "Glacerie Créative",
        "category": "Créativité culinaire",
        "description": "Recettes avec équilibre technique des sucres, solides et matières grasses."
      },
      {
        "name": "Chocolaterie Créative",
        "category": "Créativité culinaire",
        "description": "Recettes avec couvertures, ganaches et technique de tempérage."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et utilitaires",
        "description": "Données précises de pertes par processus intégrées au calcul de coûts."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et utilitaires",
        "description": "Adaptation de recettes pour tout nombre de convives."
      },
      {
        "name": "Conversor Ing",
        "category": "Outils et utilitaires",
        "description": "Convertisseur automatique de poids et mesures."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et utilitaires",
        "description": "Identification automatique des allergènes par ingrédient."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Prix de référence et technique avec le catalogue Sosa."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Prix et technique avec le catalogue tSpoonLab."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Image de référence du plat calculé."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche approfondie sur les fournisseurs et les prix du marché."
      }
    ],
    "metrics": [
      {
        "value": "×30",
        "label": "vitesse vs calculatrice à la main"
      },
      {
        "value": "+6 pp",
        "label": "marge après calcul des coûts de la carte"
      },
      {
        "value": "−25 %",
        "label": "pertes avec données réelles"
      },
      {
        "value": "12+",
        "label": "agents pour calculer les coûts"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Une semaine pour une nouvelle carte de 30 plats",
        "Sans coût horaire d'atelier, des plats complexes à perte",
        "Pertes estimées à vue d'œil, pas de données réelles",
        "Prix de fournisseur modifiés sans mise à jour de la marge",
        "Sans traçabilité du calcul"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Une nouvelle carte de 30 plats calculée en un jour",
        "Coût horaire d'atelier intégré automatiquement",
        "Pertes réelles avec Rendement GenCal et modèles",
        "Prix actualisables : marge recalculée instantanément",
        "CSV traçable + fiche technique avec coût pour audit"
      ]
    },
    "galleryTitle": "Comment fonctionne le flux de calcul de coûts avec l'IA",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : recette, CSV, pertes, recueil de recettes numérique et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "Comment Concevoir un Menu Dégustation avec l'IA",
    "heroSubtitle": "Concevez des menus dégustation avec une séquence cohérente, un calcul de coût total validé, des accords mets-vins scientifiques et un storytelling pour la salle avec une suite d'agents d'IA gastronomique spécialisés en haute cuisine.",
    "heroTagline": "Menu dégustation professionnel en heures, pas en semaines",
    "badge": "Tâche : Menu dégustation",
    "painsTitle": "Ce Que Coûte la Conception d'un Menu Dégustation à la Main",
    "pains": [
      "Une semaine d'itérations pour une séquence de 7-10 services cohérente sans saturation",
      "Sans calcul de coût total validé par menu, proposition à prix incertain",
      "Accords mets-vins proposés sans base scientifique fondée",
      "Storytelling de chaque service improvisé, équipe de salle sans formation constante",
      "Les changements de service nécessitent de refaire le calcul de coût complet à la main",
      "Manque de critères pour équilibrer texture, température, intensité et technique entre les services"
    ],
    "featuresTitle": "Comment AI Chef Pro Résout le Menu Dégustation",
    "features": [
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative avec séquence technique",
        "description": "Raisonne la séquence complète : entrée légère, légume, poisson, viande, palate cleanser, dessert. Équilibre de texture, température et intensité."
      },
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Accords mets-vins sur base scientifique pour chaque service : analyse de l'acidité, des tanins, de la structure, de l'intensité et de l'harmonie avec la cuisine."
      },
      {
        "icon": "Calculator",
        "title": "Calcul de coût total intégré",
        "description": "CSV avec calcul de coût de chaque service + total du menu ; Kit de Escandallos Pro valide le coût par pax et la proposition de prix."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling pour la salle",
        "description": "Description de chaque service avec technique, produit, fournisseur et histoire ; l'équipe de salle le récite avec professionnalisme."
      },
      {
        "icon": "Sparkles",
        "title": "Bar & Lounge AI+",
        "description": "Sélection de vins au verre pour l'accord du menu dégustation avec un critère de sommelier professionnel."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Modèles pour la mise en place de chaque service, séquence de service et coordination avec la salle."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Image de référence de chaque service pour visualiser la séquence avant de tester et valider la cohérence visuelle."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Menus dégustation saisonniers et événements privés avec une planification professionnelle."
      },
      {
        "icon": "BarChart3",
        "title": "Calcula Pax",
        "description": "Mise à l'échelle des recettes pour banquets et événements privés sans perdre en précision."
      }
    ],
    "workflowTitle": "Comment Concevoir un Menu Dégustation en 5 Étapes",
    "workflow": [
      "1. Cuisine Créative — vous définissez le thème (saison, produit local, occasion) et l'agent IA livre une séquence de 7-10 services avec un équilibre technique (texture, intensité, température).",
      "2. Chaque service avec recette + calcul de coût CSV individuel + storytelling pour la salle avec technique, produit et fournisseur.",
      "3. Food Pairing AI — pour chaque service, valide l'accord avec du vin ou du saké sur une base scientifique. Bar & Lounge AI+ propose une sélection concrète de cave.",
      "4. Kit de Escandallos Pro — vous chargez les CSV individuels, l'Excel calcule le coût total par pax, la proposition de prix et la marge validée.",
      "5. Calcula Pax — si le menu est pour un événement privé ou un banquet (50, 100, 300 pax), il met à l'échelle les recettes et recalcule le coût pour une proposition commerciale."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Menu Dégustation",
    "productIds": [
      "kit-escandallos",
      "pro-prompts-ebook",
      "pack-appcc",
      "guia-restaurante-gastronomico",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Cuisine Créative + Food Pairing AI ont transformé le développement de menus dégustation. La séquence de 9 services sort déjà avec un équilibre technique documenté, les accords mets-vins au verre sont cohérents et le calcul de coût total avec Kit de Escandallos Pro nous donne une marge validée. Ce qui prenait une semaine est maintenant une journée.",
    "testimonialAuthor": "Joan Mestre",
    "testimonialRole": "Chef exécutif, restaurant avec 1 étoile Michelin",
    "faqTitle": "Questions Fréquentes sur le Menu Dégustation avec l'IA",
    "faqs": [
      {
        "q": "Convient-il pour un restaurant Michelin, un restaurant de chef ou un restaurant décontracté avec menu dégustation ?",
        "a": "Pour les trois. Cuisine Créative raisonne comme un chef professionnel : équilibre technique, séquence cohérente, narration du menu adaptée au niveau."
      },
      {
        "q": "Comment vous aide-t-il avec la cohérence entre les services ?",
        "a": "Cuisine Créative raisonne la séquence complète avec un équilibre de texture (croquant, soyeux, crémeux), de température (froid, ambiant, chaud), d'intensité (doux à puissant) et de technique (cuisson, fermentation, fumage)."
      },
      {
        "q": "Couvre-t-il les accords mets-vins au verre pour le menu ?",
        "a": "Oui. Food Pairing AI valide chaque accord sur une base scientifique ; Bar & Lounge AI+ propose une sélection concrète de cave et un storytelling pour la salle."
      },
      {
        "q": "Génère-t-il une image de référence pour chaque service ?",
        "a": "Oui. GastroIMG Gen+ génère une image de référence pour visualiser la cohérence visuelle du menu. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre plat réellement dressé."
      },
      {
        "q": "Est-il extensible aux banquets et événements privés ?",
        "a": "Oui. Calcula Pax met le menu à l'échelle pour tout nombre de convives ; Kit de Escandallos Pro recalcule le coût par pax et la proposition économique au client."
      }
    ],
    "ctaTitle": "Votre menu dégustation professionnel en heures, pas en semaines.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "Comment Concevoir un Menu Dégustation avec l'IA : Séquence, Calcul de Coût et Accords | AI Chef Pro",
      "description": "Suite d'IA pour menu dégustation : séquence technique, calcul de coût total, accords scientifiques et storytelling. Commencez dès aujourd'hui.",
      "keywords": "menu dégustation IA, concevoir menu dégustation, séquence services, accords menu, calcul de coût menu dégustation, haute cuisine IA",
      "ogImage": "https://aichef.pro/og/use-cases/task-menu-degustacion-con-ia.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Restaurant dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec «Qui suis-je ?» : vous indiquez le type de restaurant (gastronomique Michelin, fine dining, décontracté avec menu dégustation, restaurant de chef), le nombre de services préféré, le marché et le style de cuisine. Chaque agent répond adapté à votre niveau.",
    "appsTitle": "Les Agents IA que Vous Utilisez pour Menu Dégustation",
    "apps": [
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Raisonne la séquence technique du menu dégustation avec équilibre."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords mets-vins sur base scientifique pour chaque service."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'Affaires",
        "description": "Sélection de vins au verre avec un critère de sommelier."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Pour les desserts et le palate cleanser du menu."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour textures et technique avancée."
      },
      {
        "name": "Agent tSpoonLab",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue tSpoonLab pour applications avancées."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes par service intégrées au calcul de coût total."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Mise à l'échelle pour banquets et événements privés."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification des allergènes par service pour la salle."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Image de référence de chaque service du menu."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Menus dégustation saisonniers et événements privés."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching pour le leadership et la gestion du service dégustation."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "vitesse vs. processus manuel"
      },
      {
        "value": "+8 pp",
        "label": "marge après calcul de coût du menu"
      },
      {
        "value": "×3",
        "label": "vitesse des accords avec sommelier"
      },
      {
        "value": "12+",
        "label": "agents pour votre menu dégustation"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Une semaine d'itérations par nouveau menu",
        "Séquence improvisée sans équilibre technique",
        "Accords sans base scientifique",
        "Calcul de coût total, proposition à prix incertain",
        "Storytelling improvisé, équipe de salle sans formation"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Menu dégustation finalisé en un jour avec une séquence cohérente",
        "Équilibre technique documenté entre les services",
        "Accords fondés avec Food Pairing AI",
        "Calcul de coût total validé et proposition claire au client",
        "Storytelling professionnel pour le briefing de salle"
      ]
    },
    "galleryTitle": "Comment Fonctionne la Conception de Menu Dégustation avec l'IA",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : séquence, services, accords, mise en place et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "Comment Créer des Fiches Techniques avec l'IA",
    "heroSubtitle": "Documentez chaque plat avec une fiche technique professionnelle : ingrédients, grammage, technique étape par étape, allergènes, food cost, photo de dressage et storytelling pour la salle. La suite d'agents IA gastronomiques génère une fiche complète en quelques minutes.",
    "heroTagline": "Des fiches techniques professionnelles en quelques minutes, pas en heures",
    "badge": "Tâche : Fiches techniques",
    "painsTitle": "Ce Que Coûte la Création de Fiches Techniques à la Main",
    "pains": [
      "Documenter 30 plats avec une fiche technique professionnelle peut prendre 2 semaines",
      "Sans standardisation, chaque cuisinier réplique sa version et perd en cohérence",
      "Allergènes calculés à la main par recette, risque juridique et de sécurité alimentaire",
      "Sans storytelling pour la salle, l'équipe décrit le plat de manière improvisée",
      "Lorsqu'on change un ingrédient, il faut mettre à jour la fiche et recalculer les allergènes",
      "Manque de modèle professionnel avec tous les champs critiques (technique, grammage, pertes, coût)"
    ],
    "featuresTitle": "Comment AI Chef Pro Résout les Fiches Techniques",
    "features": [
      {
        "icon": "BookOpen",
        "title": "Cuisine Créative avec fiche complète",
        "description": "Chaque recette livre une fiche technique professionnelle : ingrédients, grammage, technique, allergènes, pertes, coût, storytelling, dressage."
      },
      {
        "icon": "ShieldCheck",
        "title": "ID Allergènes",
        "description": "Identification automatique des allergènes par recette : produits laitiers, gluten, fruits à coque, soja, fruits de mer, sulfites, etc."
      },
      {
        "icon": "Calculator",
        "title": "Coût intégré",
        "description": "La fiche technique inclut le food cost % et le coût par portion calculé automatiquement avec le coût horaire de l'atelier."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Image de référence du plat dressé à inclure dans la fiche technique comme guide visuel."
      },
      {
        "icon": "Sparkles",
        "title": "Storytelling pour la salle",
        "description": "Chaque fiche inclut une description professionnelle pour que l'équipe de salle la récite avec technique."
      },
      {
        "icon": "CheckSquare",
        "title": "Modèle standardisé",
        "description": "Format uniforme pour toutes les fiches : technique, conservation, allergènes, présentation, coût."
      },
      {
        "icon": "BarChart3",
        "title": "Conversor Ing + Calcula Pax",
        "description": "Convertisseur de poids et mesures ; mise à l'échelle automatique pour banquets et événements."
      },
      {
        "icon": "BookOpen",
        "title": "Pro Prompts eBook",
        "description": "eBook avec 300+ prompts professionnels pour fiches techniques, allergènes et descriptions pour la salle."
      },
      {
        "icon": "Wine",
        "title": "Accord mets-vins dans la fiche",
        "description": "Food Pairing AI suggère l'accord recommandé à inclure dans la fiche technique."
      }
    ],
    "workflowTitle": "Comment Créer des Fiches Techniques en 4 Étapes",
    "workflow": [
      "1. Cuisine Créative (ou votre agent créatif) — vous développez ou chargez la recette. L'agent IA livre recette + fiche technique complète avec tous les champs professionnels.",
      "2. ID Allergènes — identifie automatiquement les allergènes par recette et les intègre à la fiche ; lorsque vous changez un ingrédient, il recalcule instantanément.",
      "3. GastroIMG Gen+ — génère une image de référence du plat dressé à inclure dans la fiche comme guide visuel du cuisinier.",
      "4. Food Pairing AI + storytelling pour la salle — la fiche inclut un accord mets-vins recommandé et une description professionnelle pour le briefing de l'équipe."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour les Fiches Techniques",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-tareas",
      "guia-restaurante-gastronomico"
    ],
    "testimonialQuote": "Documenter 28 plats avec une fiche technique professionnelle nous prenait 2 semaines. Cuisine Créative livre désormais chaque fiche complète en quelques minutes : ingrédients, technique, allergènes automatiques, coût et storytelling pour la salle. Désormais, n'importe quel cuisinier réplique avec cohérence et lors des inspections, tout est tracé.",
    "testimonialAuthor": "Carla Mendoza",
    "testimonialRole": "Cheffe de cuisine, restaurant décontracté avec 3 points de vente",
    "faqTitle": "Questions Fréquentes sur les Fiches Techniques avec l'IA",
    "faqs": [
      {
        "q": "Que comprend une fiche technique professionnelle ?",
        "a": "Ingrédients avec grammage exact, technique étape par étape, allergènes automatiques, food cost %, coût par portion, conservation, présentation, accord suggéré et description pour la salle."
      },
      {
        "q": "Comment gère-t-il les allergènes automatiquement ?",
        "a": "ID Allergènes identifie les allergènes par ingrédient et les intègre à la fiche. Lorsque vous changez un ingrédient, il recalcule instantanément et met à jour l'information pour la salle."
      },
      {
        "q": "Est-ce que cela fonctionne pour tout type de cuisine ?",
        "a": "Oui. Le flux est le même pour la cuisine créative, la pâtisserie, la glacerie, la chocolaterie, la pizzeria, tout type de cuisine nationale ou concept."
      },
      {
        "q": "Génère-t-il une image du plat à inclure dans la fiche ?",
        "a": "Oui. GastroIMG Gen+ génère une image de référence. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive dans la fiche, c'est vous qui la faites avec votre plat réel dressé."
      },
      {
        "q": "Comment m'aide-t-il avec les audits et les certifications ?",
        "a": "Chaque fiche technique est traçable : ingrédients, grammage, allergènes, coût et technique. Prêtes pour l'audit, ISO 22000, BRC et les certifications de sécurité alimentaire."
      }
    ],
    "ctaTitle": "Vos fiches techniques professionnelles en quelques minutes.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "Comment Créer des Fiches Techniques avec l'IA : Allergènes, Coût et Storytelling | AI Chef Pro",
      "description": "Suite IA pour fiches techniques : allergènes automatiques, coût intégré, photo de dressage et storytelling. Commencez dès aujourd'hui.",
      "keywords": "fiches techniques IA, fiche technique plat, allergènes automatiques, coût par portion, fiche technique restaurant",
      "ogImage": "https://aichef.pro/og/use-cases/task-fichas-tecnicas-con-ia.jpg"
    },
    "personalizationTitle": "Personnalisé pour Votre Cuisine dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec « Qui suis-je ? » : vous indiquez le type de cuisine, la spécialité et le volume. La structure de la fiche technique s'adapte à votre concept : restaurant décontracté, fine dining, pâtisserie, glacerie, etc.",
    "appsTitle": "Les Agents IA que Vous Utilisez pour les Fiches Techniques",
    "apps": [
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Recettes + fiche technique complète avec tous les champs."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Fiches techniques sucrées avec coût horaire d'atelier."
      },
      {
        "name": "Glacerie Créative",
        "category": "Créativité Culinaire",
        "description": "Fiches avec équilibre technique des sucres, solides et matières grasses."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette."
      },
      {
        "name": "Conversor Ing",
        "category": "Outils et Utilitaires",
        "description": "Convertisseur automatique de poids et mesures."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Mise à l'échelle de recettes pour banquets et événements."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Données de rendement par processus intégrées à la fiche."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accord suggéré à inclure dans la fiche."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Gastro Connaissance",
        "description": "Image de référence du plat dressé."
      },
      {
        "name": "Gastro Lexicum",
        "category": "Gastro Connaissance",
        "description": "Tuteur de définitions techniques pour valider la terminologie."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Contenus et Réseaux Sociaux",
        "description": "300+ prompts pour fiches techniques et descriptions."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour valider technique et ingrédients."
      }
    ],
    "metrics": [
      {
        "value": "×20",
        "label": "vitesse vs. fiche manuelle"
      },
      {
        "value": "100 %",
        "label": "allergènes identifiés automatiquement"
      },
      {
        "value": "ISO",
        "label": "fiches prêtes pour l'audit 22000"
      },
      {
        "value": "12+",
        "label": "agents pour vos fiches techniques"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "2 semaines pour documenter 28 plats",
        "Allergènes calculés à la main (risque juridique)",
        "Storytelling improvisé en salle",
        "Changements d'ingrédients sans mise à jour des fiches",
        "Sans modèle professionnel standardisé"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "28 plats documentés en une journée avec un modèle professionnel",
        "Allergènes automatiques avec ID Allergènes",
        "Storytelling professionnel pour le briefing de salle",
        "Les changements mettent à jour la fiche et les allergènes instantanément",
        "Modèle uniforme prêt pour l'audit et les certifications"
      ]
    },
    "galleryTitle": "Comment Fonctionnent les Fiches Techniques avec l'IA",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : fiche, classeur, photo de dressage, tablette et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "Comment Valider des Accords avec l'IA",
    "heroSubtitle": "Validez des accords avec base scientifique : analyse de l'acidité, des tanins, de la structure, de l'intensité et de l'harmonie. Suite d'agents IA gastronomique avec technique de sommelier professionnel.",
    "heroTagline": "Accords scientifiques en quelques minutes pour toute carte",
    "badge": "Tâche : Accords professionnels",
    "painsTitle": "Ce Que Coûte Faire des Accords à la Main",
    "pains": [
      "Accords recommandés par intuition sans base scientifique fondée",
      "Équipe de salle sans formation continue pour communiquer les accords avec discernement",
      "Changements de carte ou de cave sans revalidation des accords (recommandation obsolète)",
      "Accords uniquement avec du vin : il manque des options avec bière, saké, kombucha, thé et sans alcool",
      "Storytelling de chaque accord improvisé, sans profondeur technique",
      "Événements privés avec accords ad hoc sans proposition professionnelle claire"
    ],
    "featuresTitle": "Comment AI Chef Pro Résout les Accords",
    "features": [
      {
        "icon": "Wine",
        "title": "Food Pairing AI",
        "description": "Agent spécialisé dans les accords avec base scientifique : analyse de l'acidité, des tanins, de la structure, de l'intensité, de l'harmonie et du contraste."
      },
      {
        "icon": "Sparkles",
        "title": "Bar & Lounge AI+",
        "description": "Sélection concrète de cave pour chaque accord avec critère de sommelier professionnel : vins, sakés, bières, effervescents."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling professionnel",
        "description": "Chaque accord inclut une description technique pour que l'équipe de salle le communique avec base professionnelle."
      },
      {
        "icon": "Calculator",
        "title": "Calcul de coût des accords",
        "description": "Coût réel par verre, food cost du vin et proposition de prix pour l'accord du menu dégustation."
      },
      {
        "icon": "Sparkles",
        "title": "Accords sans alcool",
        "description": "Propositions avec kombucha, thé, café, eau tonique maison pour les clients qui ne consomment pas d'alcool."
      },
      {
        "icon": "CheckSquare",
        "title": "Pack APPCC bodega",
        "description": "Traçabilité de la cave et températures de service par type de vin."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Dégustations et événements avec accords, lancements par saison."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Image de référence de l'accord (verre + plat) pour Instagram et la carte."
      },
      {
        "icon": "BookOpen",
        "title": "Gastro Lexicum",
        "description": "Tuteur de définitions techniques : œnologie, vinification, terroir, appellations."
      }
    ],
    "workflowTitle": "Comment Valider des Accords en 4 Étapes",
    "workflow": [
      "1. Food Pairing AI — vous chargez le plat avec technique et ingrédients. L'IA analyse acidité, tanins, intensité, structure et propose un type de vin avec base scientifique.",
      "2. Bar & Lounge AI+ — propose une sélection concrète de votre cave : millésimes, producteurs, verre ou bouteille. Pour les options sans alcool, propose kombuchas, thés ou tonics maison.",
      "3. Storytelling pour la salle — chaque accord génère une description professionnelle pour le briefing de l'équipe et la communication au client.",
      "4. Kit de Escandallos Pro — vous calculez le coût réel par verre, le food cost du vin et la proposition de prix pour l'accord."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour Accords Mets-Vins",
    "productIds": [
      "kit-tareas-bar",
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Food Pairing AI a transformé ma façon de finaliser les accords. Chaque plat du menu dégustation a désormais un accord scientifiquement fondé que mon équipe de salle communique avec une base professionnelle. Nous avons augmenté la marge de 6 points sur la cave et les clients récurrents premium ont augmenté de 35 % en 6 mois.",
    "testimonialAuthor": "Eduardo Lara",
    "testimonialRole": "Chef Sommelier, restaurant 1 étoile Michelin",
    "faqTitle": "Questions Fréquentes sur les Accords avec l'IA",
    "faqs": [
      {
        "q": "Est-ce que cela convient à tout style de restaurant ?",
        "a": "Oui. Food Pairing AI couvre du casual au fine dining Michelin, en passant par les gastrobars, cavistes et restaurants ethniques."
      },
      {
        "q": "A-t-il une base scientifique réelle ?",
        "a": "Oui. Il raisonne comme un sommelier professionnel avec un fondement technique d'œnologie et de bromatologie : acidité, tanins, structure, intensité, harmonie et contraste."
      },
      {
        "q": "Couvre-t-il les accords sans alcool ?",
        "a": "Oui. Il propose kombuchas, thés, café, tonics maison et boissons fonctionnelles avec un critère professionnel pour les clients qui ne consomment pas d'alcool."
      },
      {
        "q": "Couvre-t-il les accords avec bière, saké, effervescents ?",
        "a": "Oui. Bar & Lounge AI+ couvre tout le spectre du bar : vins, sakés, bières artisanales, effervescents et spiritueux."
      },
      {
        "q": "Génère-t-il du contenu visuel de l'accord pour Instagram ?",
        "a": "Oui. GastroIMG Gen+ génère une image de référence. Rappelez-vous que l'image IA est une référence visuelle : la photo définitive, c'est vous qui la faites avec votre verre et votre plat réels."
      }
    ],
    "ctaTitle": "Vos accords avec base scientifique en quelques minutes.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "Comment Valider des Accords avec l'IA : Vins, Saké et Sans Alcool | AI Chef Pro",
      "description": "Suite IA pour accords : Food Pairing AI avec base scientifique, sélection de cave, storytelling pour la salle. Commencez dès aujourd'hui.",
      "keywords": "accords avec IA, food pairing IA, accord vin plat, IA sommelier, accords sans alcool IA, accord scientifique",
      "ogImage": "https://aichef.pro/og/use-cases/task-maridajes-con-ia.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Cave dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec « Qui suis-je ? » : vous indiquez le type de restaurant, la taille de la cave, la spécialité et le niveau. Chaque accord s'adapte à votre inventaire réel, pas à une cave générique.",
    "appsTitle": "Les Agents IA que Vous Utilisez pour les Accords",
    "apps": [
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords avec base scientifique pour chaque plat."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'Entreprise",
        "description": "Sélection concrète de cave avec critère de sommelier."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Storytelling professionnel de l'accord pour la salle."
      },
      {
        "name": "Gastro Lexicum",
        "category": "Connaissance Gastro",
        "description": "Tuteur de définitions d'œnologie et de vinification."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes par débouchage raté intégrées."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification des sulfites pour les clients sensibles."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Image de référence de l'accord."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche approfondie des caves et millésimes."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Dégustations et événements avec accords."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles SEO sur les accords et les caves."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec accords en vedette."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Contenus et Réseaux Sociaux",
        "description": "300+ prompts pour descriptions d'accords."
      }
    ],
    "metrics": [
      {
        "value": "×10",
        "label": "vitesse vs validation manuelle"
      },
      {
        "value": "+6 pp",
        "label": "marge après calcul de la cave"
      },
      {
        "value": "+35 %",
        "label": "clients récurrents premium"
      },
      {
        "value": "12+",
        "label": "agents pour accords"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Accords par intuition sans base scientifique",
        "Sans options sans alcool professionnelles",
        "Équipe de salle sans formation documentée",
        "Changements de cave sans revalidation des accords",
        "Accords pour événements privés ad hoc"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Accords avec base scientifique de Food Pairing AI",
        "Options avec kombucha, thé, tonics maison",
        "Briefing quotidien à l'équipe avec storytelling professionnel",
        "Les changements de cave revalident les accords instantanément",
        "Accords pour événements privés avec proposition professionnelle"
      ]
    },
    "galleryTitle": "Comment Fonctionne la Validation des Accords avec l'IA",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : verres, plats, notes, cave et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "Comment réduire les pertes en cuisine avec l'IA",
    "heroSubtitle": "Identifiez, mesurez et réduisez les pertes par processus (découpe, formage, cuisson, vitrine, livraison) avec des données réelles intégrées au rendement. Suite d'agents IA gastronomiques spécialisés dans l'opérationnel zéro déchet.",
    "heroTagline": "Pertes réduites avec des données réelles par processus",
    "badge": "Tâche : Réduction des pertes",
    "painsTitle": "Ce que coûtent les pertes sans contrôle",
    "pains": [
      "Pertes estimées à vue (15-30 % sur certaines découpes), pas de données réelles par processus",
      "Manque de données par type de cuisine (glacerie, boulangerie, grill, sushi ont des pertes différentes)",
      "Sans système pour réutiliser parures et épluchures (bouillons, vinaigres infusés, déshydratés)",
      "Quand un fournisseur change, les pertes changent sans recalculer la marge",
      "Équipe sans formation constante en technique de valorisation professionnelle",
      "Sans traçabilité pour les audits de durabilité et les certifications zéro déchet"
    ],
    "featuresTitle": "Comment AI Chef Pro réduit les pertes",
    "features": [
      {
        "icon": "BarChart3",
        "title": "Rendement GenCal",
        "description": "Données précises de pertes par processus par type de cuisine : découpe, dry-aging, formage, cuisson, vitrine, livraison."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative",
        "description": "Raisonne des techniques de réutilisation : parures en bouillons, épluchures en vinaigres infusés, restes en déshydratés avec un critère professionnel."
      },
      {
        "icon": "Calculator",
        "title": "Pertes dans le rendement",
        "description": "Pertes réelles par processus intégrées au rendement du Kit de Escandallos Pro : le coût par plat reflète la perte réelle, pas estimée."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante Casual",
        "description": "Modèles avec procédures de valorisation par station, contrôle hebdomadaire des pertes, formation d'équipe."
      },
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC traçable",
        "description": "Traçabilité des pertes par processus pour les audits de durabilité et les certifications zéro déchet."
      },
      {
        "icon": "Beaker",
        "title": "Fermentus Avec AI+",
        "description": "Fermentations pour réutiliser les produits : choucroute avec des restes de chou, kombucha avec des épluchures de fruits, garum avec des arêtes de poisson."
      },
      {
        "icon": "Sparkles",
        "title": "VegChef Plant-Based",
        "description": "Pour la réutilisation professionnelle végétale : valorisation intégrale des légumes, technique stems-to-roots."
      },
      {
        "icon": "BarChart3",
        "title": "Calcula Pax",
        "description": "Achats ajustés au volume réel de l'événement ou du service pour réduire les surplus dès l'origine."
      },
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification de production ajustée à la demande historique pour réduire la surproduction."
      }
    ],
    "workflowTitle": "Comment réduire les pertes en 4 étapes",
    "workflow": [
      "1. Rendement GenCal — l'agent IA fournit des données réelles par processus par type de cuisine (découpe de viande, formage de pâtes, cuisson du pain, vitrine de glace, livraison de pizza). Vous chargez la donnée réelle de votre opération.",
      "2. Cuisine Créative + Fermentus Avec AI+ — vous développez des techniques de réutilisation : parures en bouillons, épluchures en vinaigres, restes en déshydratés, surplus en fermentations.",
      "3. Kit de Escandallos Pro — le rendement reflète la perte réelle, pas estimée. Le coût par plat augmente légèrement mais reflète le coût véritable, évitant les surprises sur la marge.",
      "4. Calcula Pax + Gastro Calendar — achats ajustés au volume réel du service ou de l'événement pour réduire les surplus dès l'origine, pas seulement traiter les pertes ensuite."
    ],
    "productsTitle": "Modèles et kits recommandés pour réduire les pertes",
    "productIds": [
      "kit-escandallos",
      "kit-inventario",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-tareas",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Rendement GenCal + Cuisine Créative ont changé notre opérationnel. Nous sommes passés de pertes estimées (nous assumions 12-15 %) à des données réelles de 22-28 % sur certains processus. Nous avons réorganisé la découpe et la valorisation avec une technique documentée et réduit les pertes de 35 % en 4 mois. Le rendement reflète désormais le coût réel, pas l'idéal.",
    "testimonialAuthor": "Sofía Cano",
    "testimonialRole": "Sous-chef, restaurant décontracté avec engagement zéro déchet",
    "faqTitle": "Questions fréquentes sur la réduction des pertes avec l'IA",
    "faqs": [
      {
        "q": "Est-ce que cela fonctionne pour tout type de cuisine ?",
        "a": "Oui. Rendement GenCal couvre les données par processus par type de cuisine : grill, sushi, pâtes, pain, glace, chocolat, sauce, marinade. Chaque cuisine a des pertes différentes."
      },
      {
        "q": "Comment intégrer les pertes réelles au rendement ?",
        "a": "Kit de Escandallos Pro a un champ de perte par ingrédient et par processus. Rendement GenCal fournit les données réelles pour que le coût par plat reflète la réalité."
      },
      {
        "q": "Couvre-t-il les techniques de réutilisation professionnelle ?",
        "a": "Oui. Cuisine Créative fournit des techniques de valorisation : stems-to-roots végétal, parures en bouillons, épluchures en vinaigres, fermentations avec surplus. Fermentus approfondit les techniques avancées."
      },
      {
        "q": "Génère-t-il une traçabilité pour les certifications zéro déchet ?",
        "a": "Oui. Pack APPCC + Rendement GenCal fournissent une traçabilité documentée pour les audits de durabilité et les certifications zéro déchet ou B-Corp."
      },
      {
        "q": "Comment m'aide-t-il avec des achats ajustés ?",
        "a": "Calcula Pax + Gastro Calendar planifient la production et les achats ajustés au volume réel du service pour réduire les surplus dès l'origine."
      }
    ],
    "ctaTitle": "Votre cuisine avec des pertes réduites et des données réelles.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "Comment réduire les pertes en cuisine avec l'IA : données réelles et réutilisation | AI Chef Pro",
      "description": "Suite d'IA pour réduire les pertes : Rendement GenCal avec données réelles, réutilisation professionnelle, rendement traçable. Commencez aujourd'hui.",
      "keywords": "réduire les pertes restaurant, pertes avec IA, gaspillage alimentaire IA, zéro déchet cuisine, pertes atelier, réduire le gaspillage",
      "ogImage": "https://aichef.pro/og/use-cases/task-reducir-mermas-con-ia.jpg"
    },
    "personalizationTitle": "Personnalisé à votre cuisine dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec « Qui suis-je ? » : vous indiquez le type de cuisine et le volume. Rendement GenCal fournit des données par processus adaptées à votre concept : grill, sushi, pâtes, pain, glace, chocolat.",
    "appsTitle": "Les agents IA que vous utilisez pour réduire les pertes",
    "apps": [
      {
        "name": "Rendement GenCal",
        "category": "Outils et utilitaires",
        "description": "Données réelles de pertes par processus par type de cuisine."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité culinaire",
        "description": "Techniques de réutilisation professionnelle de parures et surplus."
      },
      {
        "name": "Fermentus Avec AI+",
        "category": "Créativité culinaire",
        "description": "Fermentations pour réutiliser les surplus (choucroute, kombucha, garum)."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Créativité culinaire",
        "description": "Valorisation intégrale des légumes (stems-to-roots)."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et utilitaires",
        "description": "Achats ajustés au volume réel du service."
      },
      {
        "name": "Conversor Ing",
        "category": "Outils et utilitaires",
        "description": "Convertisseur de poids et mesures pour la précision."
      },
      {
        "name": "ID Allergènes",
        "category": "Outils et utilitaires",
        "description": "Identification dans les produits réutilisés."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et réseaux sociaux",
        "description": "Planification de production ajustée à la demande historique."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et réseaux sociaux",
        "description": "Articles SEO sur la durabilité pour attirer du trafic."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance gastronomique",
        "description": "Image de référence de plats zéro déchet."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et utilitaires",
        "description": "Coaching pour le leadership d'équipe en zéro déchet."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche sur les techniques zéro déchet de références."
      }
    ],
    "metrics": [
      {
        "value": "−35 %",
        "label": "pertes en 4 mois"
      },
      {
        "value": "+4 pp",
        "label": "marge après intégration des pertes réelles"
      },
      {
        "value": "×3",
        "label": "vitesse vs estimation manuelle"
      },
      {
        "value": "12+",
        "label": "agents pour réduire les pertes"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Pertes estimées à vue, rendement avec coût sous-estimé",
        "Sans technique documentée de réutilisation",
        "Achats génériques sans ajustement au volume réel",
        "Équipe sans formation en valorisation professionnelle",
        "Sans traçabilité pour les audits de durabilité"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Pertes réelles documentées par processus",
        "Techniques de réutilisation avec Cuisine Créative + Fermentus",
        "Achats ajustés au volume réel avec Calcula Pax",
        "Briefing à l'équipe avec technique documentée",
        "Traçabilité APPCC pour les audits zéro déchet"
      ]
    },
    "galleryTitle": "Comment fonctionne la réduction des pertes avec l'IA",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : pesage, suivi, organisation, réutilisation et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "Comment gérer l'APPCC numérique avec l'IA",
    "heroSubtitle": "Remplacez le papier imprimé dispersé par l'APPCC depuis mobile avec des modèles professionnels : températures, nettoyage, traçabilité, allergènes, nuisibles, huile et eau. Suite d'agents IA gastronomique avec base réglementaire.",
    "heroTagline": "APPCC professionnel depuis mobile, sans papier",
    "badge": "Tâche : APPCC et sécurité alimentaire",
    "painsTitle": "Ce que coûte la gestion de l'APPCC sur papier",
    "pains": [
      "Papier imprimé dispersé dans la cuisine, registres incomplets lors des inspections",
      "Pas de standardisation par concept (glacerie, boulangerie, grill, sushi ont des registres différents)",
      "Allergènes calculés à la main par recette, risque juridique et de sécurité",
      "Changements de réglementation sans mise à jour des modèles et procédures",
      "Équipe en rotation sans formation constante en sécurité alimentaire",
      "Pas de traçabilité pour les audits ISO 22000, BRC, IFS ou certifications qualité"
    ],
    "featuresTitle": "Comment AI Chef Pro résout l'APPCC",
    "features": [
      {
        "icon": "ShieldCheck",
        "title": "Pack APPCC avec modèles Excel",
        "description": "19 registres Excel téléchargeables : températures, nettoyage, traçabilité, allergènes, nuisibles, huile et eau."
      },
      {
        "icon": "Sparkles",
        "title": "ID Allergènes",
        "description": "Identification automatique des allergènes par ingrédient et recette. Lorsque vous changez un ingrédient, il recalcule instantanément."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas con APPCC",
        "description": "Modèles de tâches avec APPCC intégré par service : ouverture, service, fermeture."
      },
      {
        "icon": "BarChart3",
        "title": "Traçabilité des produits",
        "description": "Traçabilité du poisson frais, produits laitiers, fruits secs, ferments, conserves avec températures critiques."
      },
      {
        "icon": "BookOpen",
        "title": "Cuisine Créative avec APPCC",
        "description": "Recettes incluant des procédures APPCC intégrées à la fiche technique : température, conservation, allergènes."
      },
      {
        "icon": "Calendar",
        "title": "Nettoyage programmé",
        "description": "Calendrier de nettoyage en profondeur par poste et service avec modèles spécifiques et signature numérique."
      },
      {
        "icon": "Sparkles",
        "title": "Pro Prompts eBook",
        "description": "300+ prompts professionnels pour la gestion de l'APPCC, la formation d'équipe et la communication avec les inspecteurs."
      },
      {
        "icon": "Wine",
        "title": "Pack APPCC pour cave",
        "description": "Traçabilité des vins, débouchage, conservation et températures de service par type."
      },
      {
        "icon": "BarChart3",
        "title": "Sonar Deep Research",
        "description": "Recherche approfondie de la réglementation sanitaire par pays, communauté autonome et type d'établissement."
      }
    ],
    "workflowTitle": "Comment mettre en œuvre l'APPCC numérique en 4 étapes",
    "workflow": [
      "1. Pack APPCC (€14, modèles Excel téléchargeables) — vous téléchargez les 19 registres professionnels adaptés à votre type de cuisine (pâtisserie, glacerie, restaurant, etc.).",
      "2. ID Allergènes — scanne automatiquement les recettes et modèles de votre carte pour identifier les allergènes par plat. Il l'intègre aux fiches techniques et en salle.",
      "3. Cuisine Créative avec APPCC intégré — chaque nouvelle recette fournit des procédures APPCC (température critique, conservation, allergènes, stockage) intégrées à la fiche technique.",
      "4. Kit de Tareas con APPCC — modèles de service (ouverture, service, fermeture) avec APPCC intégré. L'équipe signe numériquement chaque service depuis mobile."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour l'APPCC",
    "productIds": [
      "pack-appcc",
      "kit-tareas",
      "pro-prompts-ebook",
      "kit-escandallos",
      "kit-inventario",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "Le Pack APPCC + ID Allergènes ont transformé notre sécurité alimentaire. Nous sommes passés de papier imprimé dispersé à 19 registres numériques avec APPCC intégré par service et allergènes automatiques par recette. L'inspection sanitaire est impeccable et le risque juridique est tombé à zéro.",
    "testimonialAuthor": "Roberto Castaño",
    "testimonialRole": "Directeur F&B, hôtel 5 étoiles avec 4 points de vente",
    "faqTitle": "Questions Fréquentes sur l'APPCC avec l'IA",
    "faqs": [
      {
        "q": "Convient-il à tout type d'établissement ?",
        "a": "Oui. Le Pack APPCC adapte les modèles à restaurant, café, pâtisserie, glacerie, chocolaterie, pizzeria, dark kitchen, bar, traiteur, hôtel."
      },
      {
        "q": "Comment gérez-vous les allergènes automatiquement ?",
        "a": "ID Allergènes identifie les allergènes par ingrédient et recette, les intègre aux fiches techniques et modèles APPCC. Lorsque vous changez un ingrédient, il recalcule instantanément."
      },
      {
        "q": "Couvre-t-il la réglementation européenne, latino-américaine ?",
        "a": "Oui. Le Pack APPCC couvre la réglementation européenne (UE 852/2004 + 178/2002 + 1169/2011 allergènes) et les adaptations pour l'Amérique latine. Sonar Deep Research permet de consulter la réglementation spécifique par pays."
      },
      {
        "q": "Génère-t-il une traçabilité pour les audits ISO ?",
        "a": "Oui. APPCC depuis mobile avec signature numérique + traçabilité des produits + calendrier de nettoyage prêts pour les audits ISO 22000, BRC, IFS, FSSC 22000."
      },
      {
        "q": "Comment m'aide-t-il avec les changements réglementaires ?",
        "a": "Sonar Deep Research consulte la réglementation à jour par pays et communauté autonome. Cuisine Créative met à jour les fiches techniques et procédures lorsque les normes changent."
      }
    ],
    "ctaTitle": "Votre APPCC professionnel depuis mobile, sans papier.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "Comment gérer l'APPCC numérique avec l'IA : Modèles, Allergènes et Traçabilité | AI Chef Pro",
      "description": "Suite d'IA pour l'APPCC numérique : modèles Excel, allergènes automatiques, traçabilité ISO. Commencez dès aujourd'hui.",
      "keywords": "APPCC numérique IA, modèles APPCC, allergènes automatiques, ISO 22000 IA, sécurité alimentaire IA, HACCP numérique",
      "ogImage": "https://aichef.pro/og/use-cases/task-appcc-digital-con-ia.jpg"
    },
    "personalizationTitle": "Personnalisé à votre établissement dès la première minute",
    "personalizationBody": "AI Chef Pro démarre avec « Qui suis-je ? » : vous indiquez le type d'établissement et le pays. Le Pack APPCC adapte les modèles à votre concept et à la réglementation locale.",
    "appsTitle": "Les Agents IA que vous utilisez pour l'APPCC",
    "apps": [
      {
        "name": "ID Allergènes",
        "category": "Outils et Utilitaires",
        "description": "Identification automatique des allergènes par recette."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Recettes avec procédures APPCC intégrées."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "APPCC spécifique pour la pâtisserie et les ateliers de production."
      },
      {
        "name": "Glacerie Créative",
        "category": "Créativité Culinaire",
        "description": "APPCC spécifique pour la glacerie avec produit sensible."
      },
      {
        "name": "Chocolaterie Créative",
        "category": "Créativité Culinaire",
        "description": "APPCC spécifique pour la chocolaterie et la confiserie."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Traçabilité des pertes intégrée à l'APPCC."
      },
      {
        "name": "Conversor Ing",
        "category": "Outils et Utilitaires",
        "description": "Convertisseur de poids et mesures."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche approfondie de la réglementation par pays."
      },
      {
        "name": "Gastro Lexicum",
        "category": "Gastro Connaissance",
        "description": "Tuteur de définitions techniques réglementaires."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Contenus et Réseaux Sociaux",
        "description": "300+ prompts pour la gestion de l'APPCC."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles sur la sécurité alimentaire pour le trafic organique."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching pour la gestion du stress lors des inspections."
      }
    ],
    "metrics": [
      {
        "value": "ISO",
        "label": "modèles prêts pour 22000, BRC, IFS"
      },
      {
        "value": "100 %",
        "label": "allergènes identifiés automatiquement"
      },
      {
        "value": "0 %",
        "label": "risque juridique pour allergènes non déclarés"
      },
      {
        "value": "12+",
        "label": "agents pour votre APPCC"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Papier imprimé dispersé dans la cuisine",
        "Allergènes calculés à la main (risque juridique)",
        "Pas de modèles adaptés au type de cuisine",
        "Équipe en rotation sans formation documentée",
        "Pas de traçabilité pour les audits ISO"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "APPCC depuis mobile avec signature numérique",
        "Allergènes automatiques avec ID Allergènes",
        "Modèles Excel adaptés par concept",
        "Briefing avec APPCC intégré au Kit de Tareas",
        "Traçabilité prête pour ISO 22000, BRC, IFS"
      ]
    },
    "galleryTitle": "Comment fonctionne l'APPCC numérique avec l'IA",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : thermomètre, tablette, caméra, nettoyage et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "Comment Concevoir une Carte Saisonnière avec IA",
    "heroSubtitle": "Concevez une carte saisonnière avec des produits locaux de saison, un escandallo professionnel, une planification anticipée et le storytelling des producteurs. Suite d'agents IA gastronomiques avec calendrier par hémisphère et région.",
    "heroTagline": "Carte de saison avec critère professionnel en quelques heures",
    "badge": "Tâche : Carte saisonnière",
    "painsTitle": "Ce Que Coûte la Conception Manuelle d'une Carte Saisonnière",
    "pains": [
      "Une semaine ou plus pour itérer et finaliser la carte de saison avec un escandallo validé",
      "Pas de critère clair de produits locaux par saison et région (varie selon les hémisphères)",
      "Produits hors saison avec coût élevé et pertes importantes (importation, réfrigération)",
      "Pas de storytelling des producteurs locaux pour la salle et la communication",
      "Changements brusques entre saisons sans planification anticipée",
      "Pas de coordination avec le calendrier des fêtes (Pâques, Noël, Fête des Mères, événements locaux)"
    ],
    "featuresTitle": "Comment AI Chef Pro Résout la Carte Saisonnière",
    "features": [
      {
        "icon": "Calendar",
        "title": "Gastro Calendar",
        "description": "Planification saisonnière par hémisphère et région avec produits locaux de saison et fêtes clés."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative saisonnière",
        "description": "Raisonne des plats signature avec des produits locaux de saison : champignons d'automne, asperges de printemps, légumes d'été, racines d'hiver."
      },
      {
        "icon": "Calculator",
        "title": "Escandallo saisonnier",
        "description": "Recette + escandallo CSV avec produits locaux ; Kit de Escandallos Pro recalcule la marge lors du changement de saison."
      },
      {
        "icon": "BookOpen",
        "title": "Storytelling des producteurs",
        "description": "Chaque plat inclut le storytelling du producteur local : éleveur, agriculteur, boulanger, pêcheur, pour la communication en salle et avec le client."
      },
      {
        "icon": "Wine",
        "title": "Bar & Lounge AI+",
        "description": "Vins de saison et accords ajustés aux produits saisonniers pour votre carte."
      },
      {
        "icon": "Image",
        "title": "GastroIMG Gen+ + Pinterest Pins Gen",
        "description": "Photographie saisonnière IA + Pinterest capte du trafic organique pour les produits de saison."
      },
      {
        "icon": "CheckSquare",
        "title": "Kit de Tareas Restaurante",
        "description": "Modèles de transition entre saisons : rotation des stocks, formation de l'équipe, lancement de la carte."
      },
      {
        "icon": "Sparkles",
        "title": "VegChef Plant-Based",
        "description": "Pour les légumes de saison avec technique avancée (fermentations, déshydratés, conserves)."
      },
      {
        "icon": "BarChart3",
        "title": "Agent Sosa Ingredients",
        "description": "Catalogue Sosa pour compléter les produits locaux avec une technique professionnelle."
      }
    ],
    "workflowTitle": "Comment Concevoir une Carte Saisonnière en 5 Étapes",
    "workflow": [
      "1. Gastro Calendar — vous définissez l'hémisphère, la région et la saison (ex. automne Hémisphère Nord, Madrid). L'agent IA fournit les produits locaux de saison et les fêtes clés (Fête des Mères, Noël, Saint-Valentin).",
      "2. Cuisine Créative — vous développez des plats signature avec des produits locaux. Chaque recette fournit recette + escandallo CSV + storytelling du producteur.",
      "3. Kit de Escandallos Pro — vous chargez les CSV avec vos prix réels de fournisseurs locaux, validez la marge et le food cost % par plat et pour la carte totale.",
      "4. Bar & Lounge AI+ + Food Pairing AI — vous mettez à jour les vins de saison et les accords ajustés aux produits saisonniers.",
      "5. GastroIMG Gen+ + Pinterest Pins Gen — vous générez des images de référence de la nouvelle carte et des épingles optimisées pour capter du trafic organique saisonnier."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour la Carte Saisonnière",
    "productIds": [
      "kit-escandallos",
      "pack-appcc",
      "pro-prompts-ebook",
      "kit-inventario",
      "kit-tareas",
      "kit-plan-financiero"
    ],
    "testimonialQuote": "Gastro Calendar + Cuisine Créative nous ont changé la clôture des cartes saisonnières. Ce qui prenait une semaine prend maintenant une journée avec un escandallo professionnel, des produits locaux tracés et le storytelling des producteurs pour la salle. Nous avons augmenté la marge de 6 points et la captation avec Pinterest Pins Gen pour les produits de saison a doublé.",
    "testimonialAuthor": "Marina Lozano",
    "testimonialRole": "Chef exécutive, restaurant gastronomique avec produits locaux",
    "faqTitle": "Questions Fréquentes sur la Carte Saisonnière avec IA",
    "faqs": [
      {
        "q": "Est-ce adapté à l'hémisphère nord et sud ?",
        "a": "Oui. Gastro Calendar adapte les produits locaux et la saison par hémisphère et région. Ce qui est l'automne en Espagne est le printemps en Argentine."
      },
      {
        "q": "Comment gérez-vous les produits locaux à coût variable ?",
        "a": "Kit de Escandallos Pro recalcule instantanément la marge lorsque vous mettez à jour les prix. Rendement GenCal ajoute le coût des pertes saisonnières (plus élevé pour les produits hors saison)."
      },
      {
        "q": "Couvrez-vous les fêtes par région ?",
        "a": "Oui. Gastro Calendar planifie les fêtes clés par pays et région : Pâques, Noël, Fête des Mères, Saint-Valentin, fêtes locales (San Fermín, Fallas, etc.)."
      },
      {
        "q": "Générez-vous du contenu visuel saisonnier ?",
        "a": "Oui. GastroIMG Gen+ + Pinterest Pins Gen génèrent des images de référence et des épingles pour capter du trafic organique saisonnier. Rappelez-vous que l'image IA est une référence visuelle : la photo finale, c'est vous qui la faites avec votre plat réel."
      },
      {
        "q": "Comment m'aidez-vous avec le storytelling des producteurs ?",
        "a": "Cuisine Créative raisonne en clé de produits locaux : éleveur de race autochtone, agriculteur bio, pêcheur artisanal, boulanger local. Chaque plat inclut un storytelling professionnel pour la salle et la communication."
      }
    ],
    "ctaTitle": "Votre carte saisonnière avec produits locaux et marge réelle.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "Comment Concevoir une Carte Saisonnière avec IA : Produits Locaux, Escandallo et Storytelling | AI Chef Pro",
      "description": "Suite IA pour carte saisonnière : Gastro Calendar, produits locaux, escandallo et storytelling des producteurs. Commencez aujourd'hui.",
      "keywords": "carte saisonnière IA, menu saisonnier, produits locaux restaurant, gastro calendar, carte automne printemps IA",
      "ogImage": "https://aichef.pro/og/use-cases/task-carta-estacional-con-ia.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Restaurant dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec « Qui suis-je ? » : vous indiquez le type de restaurant, l'hémisphère, la région et l'approche (km 0, produits locaux, création). Chaque agent répond en s'adaptant à votre marché réel.",
    "appsTitle": "Les Agents IA que Vous Utilisez pour la Carte Saisonnière",
    "apps": [
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Planification saisonnière par hémisphère et région."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Plats signature avec produits locaux de saison."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Desserts avec fruits et produits de saison."
      },
      {
        "name": "VegChef Plant-Based",
        "category": "Créativité Culinaire",
        "description": "Légumes de saison avec technique avancée."
      },
      {
        "name": "Food Pairing AI",
        "category": "Créativité Culinaire",
        "description": "Accords ajustés aux produits saisonniers."
      },
      {
        "name": "Bar & Lounge AI+",
        "category": "Concepts d'Entreprise",
        "description": "Vins de saison pour votre carte."
      },
      {
        "name": "Agent Sosa Ingredients",
        "category": "Fournisseurs Gastro",
        "description": "Catalogue Sosa pour compléter les produits locaux."
      },
      {
        "name": "Rendement GenCal",
        "category": "Outils et Utilitaires",
        "description": "Pertes saisonnières intégrées à l'escandallo."
      },
      {
        "name": "Calcula Pax",
        "category": "Outils et Utilitaires",
        "description": "Mise à l'échelle pour événements privés de saison."
      },
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Photographie saisonnière IA de référence."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capte du trafic organique saisonnier."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles SEO sur les produits locaux de saison."
      }
    ],
    "metrics": [
      {
        "value": "×7",
        "label": "vitesse vs. processus manuel"
      },
      {
        "value": "+6 pp",
        "label": "marge après escandallo de la carte"
      },
      {
        "value": "×2",
        "label": "trafic organique saisonnier"
      },
      {
        "value": "12+",
        "label": "agents pour carte saisonnière"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Une semaine d'itérations pour chaque nouvelle carte",
        "Produits hors saison avec coût élevé",
        "Pas de storytelling des producteurs locaux",
        "Fêtes réactives, sans planification",
        "Pas de contenu visuel pour la captation saisonnière"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "Carte saisonnière finalisée en une journée",
        "Produits locaux de saison avec coût optimisé",
        "Storytelling professionnel des producteurs",
        "Fêtes planifiées avec 8 semaines d'avance",
        "GastroIMG Gen+ + Pinterest captent le trafic saisonnier"
      ]
    },
    "galleryTitle": "Comment Fonctionne la Conception de Carte Saisonnière avec IA",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : produits d'automne, de printemps, calendrier, dégustation et équipe. Images générées par IA comme référence visuelle du concept.",
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
    "h1": "Comment Faire de la Photographie Culinaire avec l'IA",
    "heroSubtitle": "Générez des images de référence professionnelles du plat avant de cuisiner pour valider le dressage, la palette et la composition. Ensuite, vous prenez la photo finale du plat réel avec un critère clair de l'image cible.",
    "heroTagline": "Image de référence d'abord, photo finale ensuite",
    "badge": "Tâche : Photographie culinaire",
    "painsTitle": "Ce Que Coûte la Photographie Culinaire Traditionnelle",
    "pains": [
      "Séances de food styling sans image de référence claire, itérations coûteuses",
      "Sans critère partagé entre chef, photographe et styliste sur la composition et la palette",
      "Le produit frais se dégrade pendant la séance, la photo ne capture pas le moment optimal",
      "Les changements de carte nécessitent une nouvelle séance complète et coûteuse",
      "Les images pour Instagram, Glovo, web et carte nécessitent des formats différents",
      "Image industrielle vs image d'auteur : critère incohérent entre les canaux"
    ],
    "featuresTitle": "Comment AI Chef Pro Résout la Photographie Culinaire",
    "features": [
      {
        "icon": "Image",
        "title": "GastroIMG Gen+",
        "description": "Agent spécialisé en photographie culinaire avec IA : génère une image de référence professionnelle du plat."
      },
      {
        "icon": "Sparkles",
        "title": "Cuisine Créative avec plating",
        "description": "Chaque recette fournit des instructions de plating professionnel : composition, palette, garniture, vaisselle, vue (zénithale, 3/4, frontale)."
      },
      {
        "icon": "BookOpen",
        "title": "Image comme référence, pas photo finale",
        "description": "L'image IA est le guide visuel : contraste de palette, volume, texture, vaisselle. La photo finale de la fiche technique, vous la prenez avec votre plat réel."
      },
      {
        "icon": "Calendar",
        "title": "Pinterest Pins Gen",
        "description": "Pinterest capture un trafic organique stable pour la photographie culinaire."
      },
      {
        "icon": "Sparkles",
        "title": "InstaFlow AI Pro",
        "description": "Instagram avec calendrier éditorial et compositions adaptées au feed."
      },
      {
        "icon": "BarChart3",
        "title": "MenuDish Local SEO",
        "description": "Images adaptées à Glovo, Uber Eats, Just Eat et plateformes avec un critère professionnel pour plus de clics."
      },
      {
        "icon": "CheckSquare",
        "title": "Pro Prompts eBook",
        "description": "300+ prompts professionnels pour la photographie culinaire : style, palette, composition, ambiance."
      },
      {
        "icon": "Image",
        "title": "Variantes et préparations préliminaires",
        "description": "GastroIMG génère des images de variantes : dressages alternatifs, préparations préliminaires, mise en place, pas seulement le plat final."
      },
      {
        "icon": "BookOpen",
        "title": "BlogPost SEO Gen+",
        "description": "Articles SEO sur la technique photographique avec images de référence pour le trafic organique."
      }
    ],
    "workflowTitle": "Comment Faire de la Photographie Culinaire en 4 Étapes",
    "workflow": [
      "1. Cuisine Créative — vous développez le plat. L'agent IA fournit recette + fiche technique + instructions de plating professionnel (composition, palette, vaisselle, vue).",
      "2. GastroIMG Gen+ — vous générez une image de référence professionnelle avec un prompt optimisé : palette chaude, vaisselle rustique, vue zénithale, microgreens. Vous itérez jusqu'à avoir une image cible claire.",
      "3. Vous cuisinez le plat réel avec l'image de référence devant vous : même plating, palette, garniture. La photo finale de la fiche technique et de la carte, vous la prenez avec votre plat réel dressé.",
      "4. InstaFlow AI Pro + MenuDish + Pinterest Pins Gen — vous adaptez l'image finale à chaque canal (Instagram, Glovo, web, carte) avec un critère professionnel."
    ],
    "productsTitle": "Modèles et Kits Recommandés pour la Photographie Culinaire",
    "productIds": [
      "pro-prompts-ebook",
      "kit-escandallos",
      "pack-appcc",
      "kit-inventario",
      "kit-tareas",
      "kit-gestion-personal"
    ],
    "testimonialQuote": "GastroIMG Gen+ a changé mon flux de photographie. Avant, je faisais des séances de food styling sans critère clair, maintenant je génère l'image de référence professionnelle avec l'IA, je valide la palette et la composition avec l'équipe, puis je prends la photo finale avec mon plat réel. Les séances réduisent de 70 % le temps et la cohérence visuelle sur Instagram + Glovo + web est désormais professionnelle.",
    "testimonialAuthor": "Carmen Vera",
    "testimonialRole": "Chef et propriétaire, restaurant avec une forte présence numérique",
    "faqTitle": "Questions Fréquentes sur la Photographie Culinaire avec l'IA",
    "faqs": [
      {
        "q": "L'image IA est-elle la photo finale du plat ?",
        "a": "Non. L'image IA est une référence visuelle pour valider le dressage, la palette, la vaisselle et la composition avant de cuisiner. La photo finale de la fiche technique, de la carte ou de la fiche technique, vous la prenez avec votre plat réel dressé."
      },
      {
        "q": "Convient-il à tout style de cuisine ?",
        "a": "Oui. GastroIMG Gen+ adapte le style : haute cuisine avec minimalisme, casual avec chaleur, méditerranéen, asiatique, latino-américain, fine dining premium."
      },
      {
        "q": "Couvre-t-il les formats pour Instagram, Glovo, web et carte ?",
        "a": "Oui. L'image de base s'adapte en 1:1 (Instagram), 4:5 (feed), 16:9 (carte numérique), 9:16 (Stories), 4:3 (Glovo, Uber Eats) avec un critère professionnel."
      },
      {
        "q": "Génère-t-il des variantes et des préparations préliminaires, pas seulement le plat final ?",
        "a": "Oui. GastroIMG Gen+ génère des images de variantes : dressages alternatifs, mise en place, préparations préliminaires, ingrédients bruts, pas seulement le plat final. Utile pour le storytelling du processus."
      },
      {
        "q": "Comment m'aide-t-il avec l'acquisition locale en livraison ?",
        "a": "MenuDish Local SEO + GastroIMG Gen+ génèrent des images professionnelles pour Glovo, Uber Eats, Just Eat avec un critère qui augmente le CTR. Meilleure photo = plus de clics et meilleur classement."
      }
    ],
    "ctaTitle": "Votre photographie culinaire avec un standard professionnel.",
    "ctaSubtitle": "Commencez avec l'onboarding de 2 minutes. Plan Membre à 10 € par mois avec 10 000 crédits.",
    "seo": {
      "title": "Comment Faire de la Photographie Culinaire avec l'IA : Image de Référence et Photo Finale | AI Chef Pro",
      "description": "Suite IA pour la photographie culinaire : GastroIMG Gen+ génère une image de référence, puis vous prenez la photo finale avec votre plat réel. Commencez dès aujourd'hui.",
      "keywords": "photographie culinaire IA, GastroIMG Gen+, food photography IA, image référence plat, photo plat livraison",
      "ogImage": "https://aichef.pro/og/use-cases/task-foto-gastronomica-con-ia.jpg"
    },
    "personalizationTitle": "Personnalisé à Votre Style dès la Première Minute",
    "personalizationBody": "AI Chef Pro démarre avec « Qui suis-je ? » : vous décrivez votre style de cuisine, la palette de marque, la vaisselle et les canaux prioritaires (Instagram, Glovo, web, carte). GastroIMG Gen+ adapte le style visuel à votre marque.",
    "appsTitle": "Les Agents IA que Vous Utilisez pour la Photographie Culinaire",
    "apps": [
      {
        "name": "GastroIMG Gen+",
        "category": "Connaissance Gastro",
        "description": "Agent spécialisé en photographie culinaire IA."
      },
      {
        "name": "Cuisine Créative",
        "category": "Créativité Culinaire",
        "description": "Instructions de plating professionnel pour chaque recette."
      },
      {
        "name": "Pâtisserie Créative",
        "category": "Créativité Culinaire",
        "description": "Plating de desserts avec technique française."
      },
      {
        "name": "Glacerie Créative",
        "category": "Créativité Culinaire",
        "description": "Plating de glaces et semi-froids avec technique."
      },
      {
        "name": "Pro Prompts eBook",
        "category": "Contenus et Réseaux Sociaux",
        "description": "300+ prompts professionnels pour la photographie culinaire."
      },
      {
        "name": "InstaFlow AI Pro",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Instagram avec calendrier éditorial et formats adaptés."
      },
      {
        "name": "MenuDish Local SEO",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Images optimisées pour Glovo, Uber Eats, Just Eat."
      },
      {
        "name": "Pinterest Pins Gen",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Pinterest capture un trafic organique stable."
      },
      {
        "name": "BlogPost SEO Gen+",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Articles SEO avec images de référence."
      },
      {
        "name": "Gastro Calendar",
        "category": "Contenus et Réseaux Sociaux",
        "description": "Planification des séances par saison."
      },
      {
        "name": "Sonar Deep Research",
        "category": "Modèles IA + LLM",
        "description": "Recherche sur les tendances visuelles des référents."
      },
      {
        "name": "Coach Mental",
        "category": "Outils et Utilitaires",
        "description": "Coaching pour le leadership créatif."
      }
    ],
    "metrics": [
      {
        "value": "−70 %",
        "label": "temps des séances de food styling"
      },
      {
        "value": "×3",
        "label": "engagement Instagram avec GastroIMG"
      },
      {
        "value": "+CTR",
        "label": "meilleure photo = plus de clics en livraison"
      },
      {
        "value": "12+",
        "label": "agents pour la photographie culinaire"
      }
    ],
    "beforeAfter": {
      "beforeTitle": "Sans AI Chef Pro",
      "beforeItems": [
        "Séances de food styling sans image de référence claire",
        "Sans critère partagé entre chef et photographe",
        "Les changements de carte nécessitent une nouvelle séance complète",
        "Image incohérente entre Instagram, Glovo et web",
        "Sans variantes ni préparations préliminaires pour le storytelling"
      ],
      "afterTitle": "Avec AI Chef Pro",
      "afterItems": [
        "GastroIMG Gen+ génère une image de référence professionnelle",
        "Critère partagé validé avant de cuisiner",
        "Changements de carte : nouvelle image IA en quelques minutes",
        "Image cohérente sur tous les canaux",
        "Variantes et préparations préliminaires pour un storytelling complet"
      ]
    },
    "galleryTitle": "Comment Fonctionne la Photographie Culinaire avec l'IA",
    "gallerySubtitle": "Ce que vous allez coordonner avec AI Chef Pro : hero, plat, caméra, outils et équipe. Images générées par IA comme référence visuelle du concept.",
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
