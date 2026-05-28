import { Helmet } from 'react-helmet-async';
import { Link } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import * as LucideIcons from 'lucide-react';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';
import HeroSocialProof from '@/components/HeroSocialProof';
import AuthorityBackedBy from '@/components/AuthorityBackedBy';
import { useLanguage } from '@/hooks/useLanguage';
import { getUseCasesByType, type LangCode } from '@/data/use-cases';
import { ArrowRight, Briefcase, Building2, Sparkles, Users, TrendingUp } from 'lucide-react';

const SITE_URL = 'https://aichef.pro';

const SEGMENTS: Record<string, { hub: string; consultor: string; consultorHubSlug: string; locale: string; hubLabel: string }> = {
  es: { hub: 'usos',             consultor: 'consultoria', consultorHubSlug: 'consultoria-gastro-pro',  locale: 'es-ES', hubLabel: 'Casos de uso' },
  en: { hub: 'use-cases',        consultor: 'consultancy', consultorHubSlug: 'gastro-consultancy-pro',   locale: 'en-US', hubLabel: 'Use Cases' },
  fr: { hub: 'cas-d-usage',      consultor: 'conseil',     consultorHubSlug: 'conseil-gastro-pro',       locale: 'fr-FR', hubLabel: 'Cas d’usage' },
  de: { hub: 'anwendungsfaelle', consultor: 'beratung',    consultorHubSlug: 'gastro-beratung-pro',      locale: 'de-DE', hubLabel: 'Anwendungsfälle' },
  it: { hub: 'casi-uso',         consultor: 'consulenza',  consultorHubSlug: 'consulenza-gastro-pro',    locale: 'it-IT', hubLabel: 'Casi d’uso' },
  pt: { hub: 'casos-uso',        consultor: 'consultoria', consultorHubSlug: 'consultoria-gastro-pro',   locale: 'pt-PT', hubLabel: 'Casos de uso' },
  nl: { hub: 'use-cases',        consultor: 'advies',      consultorHubSlug: 'gastro-advies-pro',        locale: 'nl-NL', hubLabel: 'Use cases' },
};

const UI: Record<string, {
  badge: string;
  h1: string;
  heroSubtitle: string;
  ctaPrimary: string;
  ctaSecondary: string;
  ctaNote: string;
  metricsTitle: string;
  metric1: { value: string; label: string };
  metric2: { value: string; label: string };
  metric3: { value: string; label: string };
  metric4: { value: string; label: string };
  cardsTitle: string;
  cardsSubtitle: string;
  cardCta: string;
  forWhoTitle: string;
  forWho1Title: string;
  forWho1Body: string;
  forWho2Title: string;
  forWho2Body: string;
  forWho3Title: string;
  forWho3Body: string;
  finalH2: string;
  finalBody: string;
  finalCta: string;
  seoIntroTitle: string;
  seoIntroBody: string;
  faqTitle: string;
  faqs: { q: string; a: string }[];
  seoTitle: string;
  seoDescription: string;
  seoKeywords: string;
}> = {
  es: {
    badge: 'Consultoría Gastro Pro',
    h1: 'IA para Consultores y Asesores Gastronómicos',
    heroSubtitle: 'Descubre cómo AI Chef Pro impulsa la consultoría y asesoría gastronómica de consultores, asesores y especialistas independientes que trabajan por proyectos para restaurantes, hoteles, grupos de restauración e inversores del sector. 10 agentes de IA, uno por cada perfil profesional.',
    ctaPrimary: 'Empezar gratis',
    ctaSecondary: 'Ver todos los agentes',
    ctaNote: '5 usos gratis al mes · Sin tarjeta',
    metricsTitle: 'Módulo Consultoría Gastro Pro en AI Chef Pro',
    metric1: { value: '10', label: 'Agentes especializados' },
    metric2: { value: '7', label: 'Idiomas disponibles' },
    metric3: { value: 'HORECA', label: 'Precios en tiempo real' },
    metric4: { value: 'PDF & CSV', label: 'Export profesional' },
    cardsTitle: 'Los 10 Agentes de Consultoría Gastronómica',
    cardsSubtitle: 'Cada perfil es un agente de IA especializado con la profundidad técnica de la disciplina y la visión de negocio que un proyecto de consultoría exige.',
    cardCta: 'Ver caso de uso',
    forWhoTitle: '¿Para Quién es Consultoría Gastro Pro?',
    forWho1Title: 'Consultores independientes',
    forWho1Body: 'Trabaja por proyectos con IA especializada en tu disciplina. Acelera entregables sin perder rigor técnico ni autoridad ante el cliente.',
    forWho2Title: 'Asesores de grupos de restauración',
    forWho2Body: 'Estandariza metodología, replica manuales y acelera procesos de auditoría, formación y onboarding en grupos multi-local.',
    forWho3Title: 'Especialistas sectoriales',
    forWho3Body: 'Profundidad técnica real para masas, fermentaciones, vinos, café, cacao, helados y todas las verticales de alta especialización.',
    finalH2: 'Tu Próximo Proyecto de Consultoría, Acelerado.',
    finalBody: 'Empieza gratis con el onboarding de 2 minutos. 5 usos al mes para probar todos los agentes de Consultoría Gastro Pro. Sin tarjeta.',
    finalCta: 'Probar gratis ahora',
    seoIntroTitle: 'La Primera IA para Consultoría y Asesoría Gastronómica, por Perfil',
    seoIntroBody: 'Si trabajas como consultor o asesor gastronómico independiente, AI Chef Pro reúne 10 agentes de inteligencia artificial especializados, uno por cada disciplina de la consultoría de hostelería. Tanto si eres chef consultor, sommelier, barista, bartender, pastelero, panadero, pizzero, heladero o chocolatero que asesora por proyectos, dispones de una IA con la profundidad técnica de tu oficio y la visión de negocio que cada cliente exige. Acelera escandallos, fichas técnicas, manuales APPCC, cartas, auditorías y formaciones sin perder rigor ni autoridad. Con precios HORECA en tiempo real y export profesional en PDF y CSV, la IA para restaurantes y hostelería se convierte en tu equipo de apoyo para entregar más proyectos en menos tiempo, en España, México, Argentina, Colombia, Chile y toda Latinoamérica.',
    faqTitle: 'Preguntas Frecuentes sobre la IA para Consultores Gastronómicos',
    faqs: [
      { q: '¿Existe una IA para consultores y asesores gastronómicos?', a: 'Sí. AI Chef Pro incluye el módulo Consultoría Gastro Pro, con 10 agentes de inteligencia artificial diseñados específicamente para consultores, asesores y especialistas que trabajan por proyectos en hostelería: chef consultor, sommelier, barista, bartender, pastelero, panadero, pizzero, heladero, chocolatero y consultor de gestión y modelo de negocio.' },
      { q: '¿Cómo ayuda la IA a un consultor gastronómico independiente?', a: 'La IA acelera los entregables habituales de un proyecto de consultoría —escandallos, fichas técnicas, manuales APPCC, cartas, auditorías y planes de formación— manteniendo el rigor técnico. Reduces horas de trabajo operativo y dedicas más tiempo a la estrategia y a la relación con el cliente, atendiendo a más proyectos a la vez.' },
      { q: '¿Sirve AI Chef Pro para asesores de restaurantes y grupos de restauración?', a: 'Sí. Los asesores de restaurantes y de grupos multi-local lo usan para estandarizar metodología, replicar manuales y acelerar auditorías, onboarding y formación. Funciona igual para asesoría gastronómica integral, consultoría restaurantera y proyectos puntuales en España y Latinoamérica.' },
      { q: '¿Hay un agente de IA para cada perfil profesional?', a: 'Sí. Cada uno de los 10 agentes está especializado en una disciplina: hay IA para chefs consultores, sommeliers, pasteleros, panaderos, pizzeros, heladeros, chocolateros, baristas y bartenders, además de un agente de gestión y modelo de negocio para el conjunto del proyecto.' },
      { q: '¿Cuánto cuesta empezar a usar la IA para consultoría gastronómica?', a: 'Puedes empezar gratis: 5 usos al mes para probar todos los agentes de Consultoría Gastro Pro, sin tarjeta de crédito. El onboarding tarda unos 2 minutos.' },
    ],
    seoTitle: 'IA para Consultores y Asesores Gastronómicos | AI Chef Pro',
    seoDescription: 'IA para consultores y asesores gastronómicos: 10 agentes especializados (chef consultor, sommelier, pastelero, pizzero, heladero y más) para acelerar tus proyectos. Empieza gratis.',
    seoKeywords: 'ia para consultores gastronómicos, ia para asesores gastronómicos, consultor gastronómico, asesor gastronómico, consultoría gastronómica, asesoría gastronómica, consultoría restaurantera, consultor de restaurantes, chef consultor, sommelier consultor, ia para restaurantes, ia para hostelería',
  },
  en: {
    badge: 'Gastro Consultancy Pro',
    h1: 'AI for Restaurant & Hospitality Consultants',
    heroSubtitle: 'See how AI Chef Pro powers restaurant, F&B and hospitality consultants, advisors, and independent specialists running project-based engagements for restaurants, hotels, restaurant groups, and food & beverage investors. 10 AI agents, one for every consulting discipline.',
    ctaPrimary: 'Start free',
    ctaSecondary: 'See all agents',
    ctaNote: '5 free uses per month · No credit card',
    metricsTitle: 'Gastro Consultancy Pro module inside AI Chef Pro',
    metric1: { value: '10', label: 'Specialized agents' },
    metric2: { value: '7', label: 'Languages available' },
    metric3: { value: 'HORECA', label: 'Live market pricing' },
    metric4: { value: 'PDF & CSV', label: 'Professional export' },
    cardsTitle: 'The 10 Gastronomic Consultancy Agents',
    cardsSubtitle: 'Every profile is a dedicated AI agent with the technical depth of the discipline and the business sense a consulting project demands.',
    cardCta: 'View use case',
    forWhoTitle: 'Who Is Gastro Consultancy Pro For?',
    forWho1Title: 'Independent consultants',
    forWho1Body: 'Work project by project with AI specialized in your discipline. Speed up deliverables without losing technical rigor or client authority.',
    forWho2Title: 'Restaurant group advisors',
    forWho2Body: 'Standardize methodology, replicate manuals, and accelerate audits, training, and onboarding across multi-location groups.',
    forWho3Title: 'Sector specialists',
    forWho3Body: 'Real technical depth for doughs, fermentations, wines, coffee, cacao, ice cream, and every high-specialization vertical.',
    finalH2: 'Accelerate Your Next Consulting Project.',
    finalBody: 'Start free with our 2-minute onboarding. 5 uses per month to try every Gastro Consultancy Pro agent. No credit card.',
    finalCta: 'Try it free now',
    seoIntroTitle: 'The First AI Built for Restaurant & F&B Consultants — by Discipline',
    seoIntroBody: 'If you work as an independent restaurant, F&B or hospitality consultant, AI Chef Pro brings together 10 specialized AI agents, one for every consulting discipline. Whether you are a chef consultant, sommelier, barista, bartender, pastry, bakery, pizza, gelato or chocolate advisor working project by project, you get AI with the technical depth of your craft and the business sense each client demands. Speed up food costing, technical sheets, HACCP manuals, menus, audits and training without losing rigor or authority. With live HORECA market pricing and professional PDF & CSV export, AI for restaurants becomes your support team to deliver more projects in less time.',
    faqTitle: 'FAQs about AI for Restaurant & Hospitality Consultants',
    faqs: [
      { q: 'Is there an AI for restaurant and hospitality consultants?', a: 'Yes. AI Chef Pro includes the Gastro Consultancy Pro module, with 10 AI agents designed specifically for consultants, advisors and specialists working project by project in hospitality: chef consultant, sommelier, barista, bartender, pastry, bakery, pizza, gelato and chocolate advisors, plus a business-model and management agent.' },
      { q: 'How does AI help an independent restaurant consultant?', a: 'The AI speeds up the deliverables of a consulting project —food costing, technical sheets, HACCP manuals, menus, audits and training plans— while keeping technical rigor. You cut operational hours and spend more time on strategy and the client relationship, handling more projects at once.' },
      { q: 'Does AI Chef Pro work for F&B advisors and restaurant groups?', a: 'Yes. F&B advisors and multi-location group consultants use it to standardize methodology, replicate manuals and accelerate audits, onboarding and training. It works equally well for full hospitality consulting and one-off project engagements.' },
      { q: 'Is there a dedicated AI agent for each professional profile?', a: 'Yes. Each of the 10 agents specializes in one discipline: there is AI for chef consultants, sommeliers, pastry chefs, bakers, pizzaiolos, gelato makers, chocolatiers, baristas and bartenders, plus a management and business-model agent for the whole project.' },
      { q: 'How much does it cost to start?', a: 'You can start free: 5 uses per month to try every Gastro Consultancy Pro agent, no credit card required. Onboarding takes about 2 minutes.' },
    ],
    seoTitle: 'AI for Restaurant & Hospitality Consultants | AI Chef Pro',
    seoDescription: 'AI for restaurant, F&B and hospitality consultants: 10 specialized agents (chef consultant, sommelier, pastry, bakery, pizza, gelato & more) to speed up your projects. Start free.',
    seoKeywords: 'ai for restaurant consultants, restaurant consultant ai, f&b consultant software, hospitality consultant ai, ai for chefs, chef consultant, sommelier consultant, bar consultant, food consultant',
  },
  fr: {
    badge: 'Conseil Gastro Pro',
    h1: "IA pour Consultants et Conseillers en Restauration",
    heroSubtitle: "Découvrez comment AI Chef Pro dynamise votre activité de consultant en restauration : 10 agents IA dédiés aux métiers de bouche (chef consultant, sommelier, barista, bartender, pizzaiolo, chocolatier, pâtissier…) pour vos projets HORECA, avec exports PDF et CSV.",
    ctaPrimary: 'Commencer gratuitement',
    ctaSecondary: 'Voir tous les agents',
    ctaNote: '5 usages gratuits/mois · Sans carte bancaire',
    metricsTitle: 'Module Conseil Gastro Pro dans AI Chef Pro',
    metric1: { value: '10', label: 'Agents spécialisés' },
    metric2: { value: '7', label: 'Langues disponibles' },
    metric3: { value: 'HORECA', label: 'Prix marché temps réel' },
    metric4: { value: 'PDF & CSV', label: 'Export professionnel' },
    cardsTitle: 'Les 10 Agents de Conseil Gastronomique',
    cardsSubtitle: 'Chaque profil est un agent IA spécialisé avec la profondeur technique du métier et la vision business qu\'un projet de consultance CHR exige.',
    cardCta: 'Voir le cas d\'usage',
    forWhoTitle: 'À Qui s\'Adresse Conseil Gastro Pro ?',
    forWho1Title: 'Consultants indépendants',
    forWho1Body: 'Travaillez par projet avec une IA spécialisée dans votre discipline. Accélérez vos livrables sans perdre la rigueur technique ni l\'autorité face au client.',
    forWho2Title: 'Conseillers de groupes de restauration',
    forWho2Body: 'Standardisez votre méthodologie, dupliquez les manuels et accélérez les audits, formations et onboarding dans les groupes multi-sites.',
    forWho3Title: 'Experts sectoriels et métiers de bouche',
    forWho3Body: 'Profondeur technique réelle pour pâtes, fermentations, vins, café, cacao, glaces et toute verticale d\'excellence artisanale (MOF inclus).',
    finalH2: 'Accélérez Votre Prochain Projet de Consultance.',
    finalBody: 'Démarrez gratuitement avec l\'onboarding de 2 minutes. 5 usages par mois pour tester tous les agents de Conseil Gastro Pro. Sans carte bancaire.',
    finalCta: 'Tester gratuitement',
    seoIntroTitle: "La première IA pour le conseil en restauration, spécialisée par métier",
    seoIntroBody: "Que vous soyez consultant en restauration indépendant, chef consultant ou rattaché à un cabinet conseil restauration, AI Chef Pro déploie 10 agents d’intelligence artificielle spécialisés dans les métiers de bouche : sommelier, barista, bartender, pizzaiolo, chocolatier, pâtissier, boulanger, glacier et bien d’autres. Que vous interveniez en conseil en restauration pour des restaurants, hôtels, groupes ou investisseurs HORECA, chaque agent allie savoir-faire technique et vision business. Créez rapidement fiches techniques, manuels APPCC/HACCP, cartes, audits et formations, avec des prix HORECA actualisés et un export professionnel PDF/CSV. Cette IA pour la restauration devient votre bras droit opérationnel, vous permettant de multiplier les missions sans sacrifier la qualité, tout en gagnant en autorité auprès de vos clients, notamment les MOF et établissements exigeants.",
    faqTitle: "Questions fréquentes sur l’IA pour les consultants en restauration",
    faqs: [
      { q: "Existe-t-il une IA pour les consultants et conseillers en restauration ?", a: "Oui, AI Chef Pro propose le module Consultoría Gastro Pro avec 10 agents IA spécifiquement conçus pour les consultants en restauration qui travaillent sur des projets HORECA. Ces agents couvrent les métiers de chef consultant, sommelier, barista, bartender, pizzaiolo, chocolatier, pâtissier, boulanger, glacier et conseil en gestion." },
      { q: "Comment l’IA aide-t-elle un consultant en restauration indépendant ?", a: "L’IA accélère la production des livrables typiques d’une mission de conseil en restauration : fiches techniques, manuels APPCC/HACCP, cartes, audits et plans de formation, tout en conservant votre rigueur professionnelle. Vous réduisez le temps opérationnel et pouvez vous concentrer sur la stratégie, ce qui vous permet de gérer simultanément plus de projets." },
      { q: "AI Chef Pro convient-il aux conseillers de restaurants et groupes de restauration ?", a: "Absolument. Les conseillers en restauration et les cabinets conseil restauration l’utilisent pour standardiser leurs méthodologies, dupliquer les manuels et accélérer les audits, l’onboarding et la formation. Cela fonctionne aussi bien pour le conseil en restauration global, le conseil pour restaurants indépendants ou les projets ponctuels multi-sites." },
      { q: "Y a-t-il un agent IA par métier de bouche ?", a: "Oui. Les 10 agents sont spécialisés dans un métier : chef consultant, sommelier, barista, bartender, pizzaiolo, chocolatier, pâtissier, boulanger, glacier, et un agent dédié au conseil en gestion et modèle économique. Chaque agent maîtrise le savoir-faire technique et les exigences business de son domaine." },
      { q: "Combien coûte l’IA pour le conseil en restauration ?", a: "Vous pouvez commencer gratuitement avec 5 utilisations par mois pour tester tous les agents du module Consultoría Gastro Pro, sans carte bancaire. L’inscription ne prend que 2 minutes. Des forfaits payants sont ensuite disponibles pour un usage intensif." },
    ],
    seoTitle: "Conseil en Restauration IA : 10 Agents | AI Chef Pro",
    seoDescription: "Conseil en restauration : 10 agents IA (chef consultant, sommelier, barista, etc.) pour accélérer vos projets. Lancez-vous gratuitement.",
    seoKeywords: "consultant en restauration, conseil en restauration, ia pour la restauration, cabinet conseil restauration, chef consultant, métiers de bouche, MOF, intelligence artificielle restauration, consultant HORECA, conseil en hôtellerie, projets restauration, AI Chef Pro",
  },
  de: {
    badge: 'Gastro Beratung Pro',
    h1: "KI für Gastronomieberatung – Ihr Partner für erfolgreiche Projekte",
    heroSubtitle: "Entdecken Sie, wie AI Chef Pro die Gastronomieberatung von freiberuflichen Consultants, Beratern und Spezialisten unterstützt, die projektbasiert für Restaurants, Hotels, Gastronomiegruppen und Investoren arbeiten. 10 KI-Agenten, jeweils für ein Fachprofil.",
    ctaPrimary: 'Kostenlos starten',
    ctaSecondary: 'Alle Agenten ansehen',
    ctaNote: '5 kostenlose Anwendungen/Monat · Keine Kreditkarte',
    metricsTitle: 'Modul Gastro Beratung Pro in AI Chef Pro',
    metric1: { value: '10', label: 'Spezialisierte Agenten' },
    metric2: { value: '7', label: 'Verfügbare Sprachen' },
    metric3: { value: 'HORECA', label: 'Echtzeit-Marktpreise' },
    metric4: { value: 'PDF & CSV', label: 'Professioneller Export' },
    cardsTitle: 'Die 10 KI-Agenten der Gastronomieberatung',
    cardsSubtitle: 'Jedes Profil ist ein dedizierter KI-Agent mit der technischen Tiefe der Disziplin und dem Geschäftsverständnis, das ein Beratungsprojekt im Gastgewerbe erfordert.',
    cardCta: 'Anwendungsfall ansehen',
    forWhoTitle: 'Für Wen ist Gastro Beratung Pro?',
    forWho1Title: 'Selbstständige Berater',
    forWho1Body: 'Arbeiten Sie projektbezogen mit einer auf Ihr Fachgebiet spezialisierten KI. Beschleunigen Sie Lieferleistungen ohne Verlust technischer Strenge oder Kundenautorität.',
    forWho2Title: 'Berater von Restaurantgruppen',
    forWho2Body: 'Standardisieren Sie Methodik, replizieren Sie Handbücher und beschleunigen Sie Audits, Schulungen und Onboarding in Multi-Standort-Gruppen.',
    forWho3Title: 'Branchenspezialisten und Gastgewerbe',
    forWho3Body: 'Echte technische Tiefe für Teige, Fermentationen, Weine, Kaffee, Kakao, Eis und jede hochspezialisierte Vertikale (mit BAFA- und IHK-Konformität).',
    finalH2: 'Beschleunigen Sie Ihr nächstes Beratungsprojekt.',
    finalBody: 'Starten Sie kostenlos mit dem 2-Minuten-Onboarding. 5 Anwendungen pro Monat, um alle Agenten von Gastro Beratung Pro auszuprobieren. Keine Kreditkarte.',
    finalCta: 'Jetzt kostenlos testen',
    seoIntroTitle: "Die erste KI für Gastronomieberatung – spezialisiert auf Ihr Profil",
    seoIntroBody: "Als freiberuflicher Gastronomieberater profitieren Sie von KI für Gastronomie, die Ihre Projektarbeit revolutioniert. AI Chef Pro bietet 10 spezialisierte Agenten – vom Chef Consultant über sommelier, barista, bartender, pâtissier, Bäcker, pizzaiolo, Eismacher bis zum chocolatier und Managementberater. Jeder Agent vereint die technische Tiefe Ihres Handwerks mit dem betriebswirtschaftlichen Fokus, den Ihre Kunden erwarten. Sie beschleunigen damit Kalkulationen, technische Datenblätter, HACCP-Handbücher, Speisekarten, Audits und Schulungen, ohne an Präzision oder Autorität einzubüßen. Dank aktueller HORECA-Preisdaten in Echtzeit und professionellem Export als PDF oder CSV wird die KI Gastronomie zu Ihrem unterstützenden Team, das Ihnen hilft, mehr Projekte in kürzerer Zeit auszuliefern. Zusätzlich erleichtert die KI die Beantragung von BAFA-Förderung für Digitalisierung und erfüllt IHK-Anforderungen, sodass Sie auch formale Hürden souverän meistern. Starten Sie kostenlos mit 5 Nutzungen pro Monat – ohne Kreditkarte. Das Onboarding dauert nur 2 Minuten.",
    faqTitle: "Häufige Fragen zur KI für Gastronomieberatung",
    faqs: [
      { q: "Gibt es eine KI für Gastronomieberater?", a: "Ja, AI Chef Pro enthält das Modul Consultoría Gastro Pro mit 10 KI-Agenten, die speziell für Gastronomieberater und Spezialisten wie sommelier, barista, bartender, pizzaiolo, chocolatier, pâtissier und Chef Consultants entwickelt wurden. Es unterstützt projektbasierte Arbeit in der Gastronomie von der Kalkulation bis zur Schulung." },
      { q: "Wie hilft eine KI einem freiberuflichen Gastronomieberater?", a: "Die KI beschleunigt typische Projektergebnisse wie Kalkulationen, HACCP-Handbücher, Speisekarten, Audits und Schulungspläne, ohne Abstriche bei der fachlichen Genauigkeit. So reduzieren Sie operative Arbeitsstunden und gewinnen mehr Zeit für Strategie und Kundenbeziehungen, um parallel mehr Projekte zu betreuen." },
      { q: "Ist AI Chef Pro für Restaurantberatung und Gastronomiegruppen geeignet?", a: "Ja. Restaurantberater und Berater für Multi-Location-Gruppen nutzen AI Chef Pro, um Methodik zu standardisieren, Handbücher zu replizieren und Audits, Onboarding sowie Schulungen zu beschleunigen. Es eignet sich für ganzheitliche Gastronomieberatung ebenso wie für punktuelle Projekte." },
      { q: "Gibt es einen KI-Agenten für jedes Fachprofil?", a: "Ja. Jeder der 10 Agenten ist auf eine Disziplin spezialisiert: Es gibt KI für Chef Consultants, sommelier, pâtissier, Bäcker, pizzaiolo, Eismacher, chocolatier, barista und bartender sowie einen Agenten für Management und Geschäftsmodell, der das Gesamtprojekt im Blick behält." },
      { q: "Was kostet der Einstieg in die KI für Gastronomieberatung?", a: "Sie können kostenlos starten: 5 Nutzungen pro Monat, um alle Agenten des Consultoría Gastro Pro zu testen, ohne Kreditkarte. Das Onboarding dauert etwa 2 Minuten. Danach stehen Ihnen verschiedene Preispläne zur Auswahl, die zu Ihrem Projektvolumen passen." },
    ],
    seoTitle: "KI Gastronomieberatung | AI Chef Pro",
    seoDescription: "KI Gastronomieberatung mit 10 spezialisierten Agenten für Gastronomieberater. Projekte beschleunigen, BAFA-Förderung nutzen. Jetzt kostenlos testen.",
    seoKeywords: "KI Gastronomieberatung, Gastronomieberater, KI für Gastronomie, Restaurantberatung, KI Gastronomie, BAFA-Förderung, IHK, Gastronomieberatung, AI Chef Pro, HORECA, Beratungs-KI, Gastronomie-Consulting",
  },
  it: {
    badge: 'Consulenza Gastro Pro',
    h1: "IA per Consulenti e Consulenza di Ristorazione",
    heroSubtitle: "Scopri come AI Chef Pro potenzia la consulenza di ristorazione per consulenti, advisor e specialisti indipendenti che lavorano a progetto per ristoranti, hotel, gruppi di ristorazione e investitori del settore. 10 agenti IA, uno per ogni profilo professionale.",
    ctaPrimary: 'Inizia gratis',
    ctaSecondary: 'Vedi tutti gli agenti',
    ctaNote: '5 utilizzi gratis/mese · Senza carta',
    metricsTitle: 'Modulo Consulenza Gastro Pro in AI Chef Pro',
    metric1: { value: '10', label: 'Agenti specializzati' },
    metric2: { value: '7', label: 'Lingue disponibili' },
    metric3: { value: 'HORECA', label: 'Prezzi mercato real-time' },
    metric4: { value: 'PDF & CSV', label: 'Export professionale' },
    cardsTitle: 'I 10 Agenti AI di Consulenza Gastronomica',
    cardsSubtitle: 'Ogni profilo è un agente IA dedicato con la profondità tecnica della disciplina e la visione di business che un progetto di consulenza ristorazione richiede.',
    cardCta: 'Vedi caso d\'uso',
    forWhoTitle: 'A Chi si Rivolge Consulenza Gastro Pro?',
    forWho1Title: 'Consulenti indipendenti',
    forWho1Body: 'Lavora per progetto con un\'AI specializzata nella tua disciplina. Accelera i deliverable senza perdere rigore tecnico né autorità di fronte al cliente.',
    forWho2Title: 'Advisor di gruppi della ristorazione',
    forWho2Body: 'Standardizza la metodologia, replica manuali e accelera audit, formazione e onboarding nei gruppi multi-sede HORECA.',
    forWho3Title: 'Specialisti di settore (Maestri di bottega)',
    forWho3Body: 'Profondità tecnica reale per impasti, lievitazioni, vini AIS, caffè di specialità, cacao bean-to-bar, gelato artigianale e ogni verticale ad alta specializzazione. AVPN inclusa.',
    finalH2: 'Accelera il Tuo Prossimo Progetto di Consulenza.',
    finalBody: 'Inizia gratis con l\'onboarding di 2 minuti. 5 utilizzi al mese per provare tutti gli agenti di Consulenza Gastro Pro. Senza carta di credito.',
    finalCta: 'Prova gratis ora',
    seoIntroTitle: "La Prima IA per la Consulenza nella Ristorazione, Personalizzata per Profilo",
    seoIntroBody: "Se lavori come consulente di ristorazione o food consultant indipendente, AI Chef Pro riunisce 10 agenti di intelligenza artificiale specializzati, uno per ogni disciplina della consulenza HORECA. Che tu sia chef consulente, sommelier, barista, bartender, panettiere, pizzaiolo, gelatiere, chocolatier o pâtissier che opera a progetto, hai a disposizione un’IA con la profondità tecnica del tuo mestiere e la visione di business che ogni cliente esige. L’IA per ristoranti accelera la creazione di distinte base, schede tecniche, manuali HACCP/APPCC, menu, audit e piani formativi, senza perdere rigore né autorevolezza. Grazie ai prezzi HORECA in tempo reale e all’export professionale in PDF e CSV, l’ai ristorazione diventa il tuo team di supporto per consegnare più progetti in meno tempo, allineandosi agli standard AVPN per la pizza o ai protocolli AIS per la sommellerie.",
    faqTitle: "Domande Frequenti sull’IA per Consulenti di Ristorazione",
    faqs: [
      { q: "Esiste un’IA per consulenti e consulenza di ristorazione?", a: "Sì. AI Chef Pro include il modulo Consulenza Gastro Pro, con 10 agenti di intelligenza artificiale progettati specificamente per consulenti, advisor e specialisti che lavorano a progetto nella ristorazione: chef consulente, sommelier, barista, bartender, pâtissier, panettiere, pizzaiolo, gelatiere, chocolatier e consulente di gestione e modello di business." },
      { q: "Come può l’IA aiutare un consulente di ristorazione indipendente?", a: "L’IA accelera i deliverable tipici di un progetto di consulenza – distinte base, schede tecniche, manuali HACCP/APPCC, menu, audit e piani formativi – mantenendo il rigore tecnico. Riduci le ore di lavoro operativo e dedichi più tempo alla strategia e alla relazione con il cliente, gestendo più progetti contemporaneamente." },
      { q: "AI Chef Pro è utile per consulenti di ristoranti e gruppi di ristorazione?", a: "Sì. I consulenti di ristoranti e di gruppi multi-sede lo utilizzano per standardizzare la metodologia, replicare i manuali e accelerare audit, onboarding e formazione. Funziona sia per la consulenza di ristorazione integrale, sia per progetti puntuali o di supporto operativo." },
      { q: "C’è un agente IA per ogni profilo professionale?", a: "Sì. Ciascuno dei 10 agenti è specializzato in una disciplina: IA per chef consulenti, sommelier, pâtissier, panettieri, pizzaioli, gelatieri, chocolatier, baristi e bartender, oltre a un agente di gestione e modello di business per l’insieme del progetto." },
      { q: "Quanto costa iniziare a usare l’IA per la consulenza di ristorazione?", a: "Puoi iniziare gratis: 5 utilizzi al mese per provare tutti gli agenti di Consulenza Gastro Pro, senza carta di credito. L’onboarding richiede circa 2 minuti." },
    ],
    seoTitle: "IA per Consulenti Ristorazione | AI Chef Pro",
    seoDescription: "IA per consulenti ristorazione: 10 agenti specializzati (chef consulente, sommelier, pizzaiolo, pâtissier, gelatiere e altri) per accelerare i tuoi progetti. Inizia gratis.",
    seoKeywords: "ia per ristoranti, ai ristorazione, consulente ristorazione, consulenza ristorazione, food consultant, HORECA, AVPN, AIS, chef consulente, pizzaiolo consulente, sommelier consulente, AI Chef Pro",
  },
  pt: {
    badge: 'Consultoria Gastro Pro',
    h1: "IA para Consultores e Assessores Gastronômicos",
    heroSubtitle: "Descubra como o AI Chef Pro impulsiona a consultoria e assessoria gastronômica de consultores, assessores e especialistas independentes que trabalham por projetos para restaurantes, hotéis, grupos de restauração e investidores do setor. 10 agentes de IA, um para cada perfil profissional.",
    ctaPrimary: 'Começar grátis',
    ctaSecondary: 'Ver todos os agentes',
    ctaNote: '5 usos grátis/mês · Sem cartão',
    metricsTitle: 'Módulo Consultoria Gastro Pro no AI Chef Pro',
    metric1: { value: '10', label: 'Agentes especializados' },
    metric2: { value: '7', label: 'Idiomas disponíveis' },
    metric3: { value: 'HORECA', label: 'Preços de mercado em tempo real' },
    metric4: { value: 'PDF & CSV', label: 'Exportação profissional' },
    cardsTitle: 'Os 10 Agentes de Consultoria Gastronômica',
    cardsSubtitle: 'Cada perfil é um agente de IA dedicado com a profundidade técnica da disciplina e a visão de negócio que um projeto de consultoria gastronômica exige (BR e PT).',
    cardCta: 'Ver caso de uso',
    forWhoTitle: 'Para Quem é a Consultoria Gastro Pro?',
    forWho1Title: 'Consultores independentes',
    forWho1Body: 'Trabalhe por projeto com IA especializada na sua disciplina. Acelere entregáveis sem perder rigor técnico nem autoridade diante do cliente, no Brasil ou em Portugal.',
    forWho2Title: 'Assessores de grupos de restauração',
    forWho2Body: 'Padronize a metodologia, replique manuais e acelere auditorias, formações e onboarding em redes multi-unidade (HORECA / A&B).',
    forWho3Title: 'Especialistas setoriais (Mestres artesanais)',
    forWho3Body: 'Profundidade técnica real para massas, fermentações, vinhos, café de especialidade, cacau, sorvete/gelado e toda vertical de alta especialização artesanal.',
    finalH2: 'Acelere o Seu Próximo Projeto de Consultoria.',
    finalBody: 'Comece grátis com o onboarding de 2 minutos. 5 usos por mês para testar todos os agentes de Consultoria Gastro Pro. Sem cartão de crédito.',
    finalCta: 'Testar grátis agora',
    seoIntroTitle: "A Primeira IA para Consultoria e Assessoria Gastronômica, por Perfil",
    seoIntroBody: "Se trabalha como consultor ou assessor gastronômico independente, o AI Chef Pro reúne 10 agentes de inteligência artificial especializados, um para cada disciplina da consultoria gastronômica. Quer seja chef consultor, sommelier, barista, bartender, pâtissier, padeiro, pizzaiolo, sorveteiro ou chocolatier que atua por projetos, dispõe de uma IA com a profundidade técnica do seu ofício e a visão de negócio que cada cliente exige. Acelere cálculos de custos, fichas técnicas, manuais APPCC, cartas, auditorias e formações, sem perder rigor ou autoridade. Com preços HORECA em tempo real e exportação profissional em PDF e CSV, a IA para restaurantes e gastronomia torna-se a sua equipe de apoio para entregar mais projetos em menos tempo.",
    faqTitle: "Perguntas Frequentes sobre a IA para Consultores Gastronômicos",
    faqs: [
      { q: "Existe uma IA para consultores e assessores gastronômicos?", a: "Sim. O AI Chef Pro inclui o módulo Consultoria Gastro Pro, com 10 agentes de inteligência artificial concebidos especificamente para consultores, assessores e especialistas que trabalham por projetos em hotelaria: chef consultor, sommelier, barista, bartender, pâtissier, padeiro, pizzaiolo, sorveteiro, chocolatier e consultor de gestão e modelo de negócio." },
      { q: "Como a IA ajuda um consultor gastronômico independente?", a: "A IA agiliza os entregáveis habituais de um projeto de consultoria — cálculos de custos, fichas técnicas, manuais APPCC, cartas, auditorias e planos de formação — mantendo o rigor técnico. Reduz horas de trabalho operacional e dedica mais tempo à estratégia e ao relacionamento com o cliente, permitindo atender mais projetos ao mesmo tempo. Com o AI Chef Pro, o consultor A&B ganha velocidade sem sacrificar qualidade." },
      { q: "O AI Chef Pro serve para assessores de restaurantes e grupos de restauração?", a: "Sim. Os assessores de restaurantes e de grupos multilocal usam o Consultoria Gastro Pro para padronizar metodologia, replicar manuais e acelerar auditorias, integração e formação. Funciona tanto para assessoria gastronômica integral, consultoria de restaurantes e projetos pontuais. A IA para gastronomia garante consistência em todos os projetos." },
      { q: "Há um agente de IA para cada perfil profissional?", a: "Sim. Cada um dos 10 agentes é especializado numa disciplina: há IA para chefs consultores, sommeliers, pâtissiers, padeiros, pizzaiolos, sorveteiros, chocolatiers, baristas e bartenders, além de um agente de gestão e modelo de negócio para o projeto como um todo. Isso permite que cada tipo de consultor gastronômico tenha assistência precisa e adaptada às suas necessidades." },
      { q: "Quanto custa começar a usar a IA para consultoria gastronômica?", a: "Pode começar gratuitamente: 5 utilizações por mês para experimentar todos os agentes do Consultoria Gastro Pro, sem necessidade de cartão de crédito. O onboarding demora cerca de 2 minutos. Após o período de testes, pode escolher um plano que se ajuste ao volume de projetos." },
    ],
    seoTitle: "IA para Consultores e Assessores Gastronômicos | AI Chef Pro",
    seoDescription: "IA para consultores e assessores gastronômicos: 10 agentes (chef consultor, sommelier, pâtissier e mais) para acelerar seus projetos. Comece grátis.",
    seoKeywords: "consultor gastronômico, consultoria gastronômica, ia para restaurantes, ia para gastronomia, assessoria gastronômica, consultor a&b, ia para consultores gastronômicos, ia para assessores gastronômicos, consultoria de restaurantes, consultor de restaurantes, chef consultor, sommelier consultor",
  },
  nl: {
    badge: 'Gastro Advies Pro',
    h1: "AI voor Horeca Consultants en Culinaire Adviseurs",
    heroSubtitle: "Ontdek hoe AI Chef Pro jouw horeca adviesbureau turbochargeert. Ontworpen voor de zelfstandige horeca consultant en culinaire specialist die op projectbasis werkt voor restaurants, hotels, horecagroepen en investeerders. Nu met 10 gespecialiseerde AI-agenten, één voor elke expertise.",
    ctaPrimary: 'Gratis starten',
    ctaSecondary: 'Alle agenten bekijken',
    ctaNote: '5 gratis gebruiken/maand · Geen creditcard',
    metricsTitle: 'Module Gastro Advies Pro in AI Chef Pro',
    metric1: { value: '10', label: 'Gespecialiseerde agenten' },
    metric2: { value: '7', label: 'Beschikbare talen' },
    metric3: { value: 'HORECA', label: 'Realtime marktprijzen' },
    metric4: { value: 'PDF & CSV', label: 'Professionele export' },
    cardsTitle: 'De 10 AI-Agenten voor Horeca-Advies',
    cardsSubtitle: 'Elk profiel is een toegewijde AI-agent met de technische diepgang van het vakgebied en de business sense die een horeca consulting-project vereist (NL en BE).',
    cardCta: 'Bekijk de use case',
    forWhoTitle: 'Voor Wie is Gastro Advies Pro?',
    forWho1Title: 'Zelfstandige adviseurs',
    forWho1Body: 'Werk op projectbasis met AI gespecialiseerd in jouw vakgebied. Versnel deliverables zonder vakkennis of klantautoriteit te verliezen, in NL of in BE.',
    forWho2Title: 'Adviseurs van restaurantgroepen',
    forWho2Body: 'Standaardiseer methodiek, repliceer handboeken en versnel audits, trainingen en onboarding in multi-locatie horeca-groepen. NBOV, KHN, KVK en NVWA conform.',
    forWho3Title: 'Sector-specialisten en ambachtelijke meesters',
    forWho3Body: 'Echte technische diepgang voor degen, fermentaties, wijnen, specialty coffee SCA, cacao, gelato en elke vertical met hoge specialisatie. Inclusief SVH Pizzaiolo.',
    finalH2: 'Versnel je Volgende Horeca Consulting-Project.',
    finalBody: 'Start gratis met de 2-minuten onboarding. 5 gebruiken per maand om alle agenten van Gastro Advies Pro te testen. Geen creditcard nodig.',
    finalCta: 'Probeer nu gratis',
    seoIntroTitle: "De eerste AI voor culinaire adviesbureaus, per vakgebied",
    seoIntroBody: "Werk jij als zelfstandig horeca adviseur of restaurant consultant? AI Chef Pro bundelt 10 gespecialiseerde AI-agenten, perfect afgestemd op elke discipline binnen de horeca consultancy. Of je nu een chef-consultant bent, of vanuit jouw specialisatie als sommelier, barista, bartender, pâtissier, bakker, pizzaiolo, ijsbereider of chocolatier projectadvies geeft: er is een AI met de vaktechnische diepgang en de commerciële visie die elke opdrachtgever eist. Versnel kostprijsberekeningen, receptuurbeschrijvingen, HACCP-handboeken, menukaarten, audits en trainingen zonder in te leveren op kwaliteit. Met realtime HORECA-prijzen en de mogelijkheid tot professionele export in PDF en CSV, is deze ai voor horeca jouw virtuele supportteam. Van lokale NBOV-standaarden tot SCA-richtlijnen: je levert simpelweg meer projecten in minder tijd op.",
    faqTitle: "Veelgestelde Vragen over AI voor Horeca Consultants",
    faqs: [
      { q: "Bestaat er een AI voor horeca adviseurs en culinaire consultants?", a: "Jazeker. AI Chef Pro omvat de module 'Consultancy Gastro Pro', met 10 AI-agenten die specifiek ontwikkeld zijn voor de horeca adviseur, restaurant consultant en vakspecialist die op projectbasis werkt. Denk aan de chef-consultant, sommelier, barista, bartender, pâtissier, bakker, pizzaiolo, ijsbereider, chocolatier en een specialist voor bedrijfsmodellen en management." },
      { q: "Hoe helpt AI een zelfstandig horeca consultant?", a: "De AI versnelt de standaard deliverables binnen een adviesproject: kostprijscalculaties, technische fiche, APPCC-handboeken, menukaarten, audits en opleidingsplannen. Zo besteed je minder tijd aan operationeel voorwerk en meer aan strategie en klantcontact, waardoor je met gemak meer projecten tegelijk kunt draaien." },
      { q: "Is AI Chef Pro geschikt als ik restaurants of horecagroepen adviseer?", a: "Absoluut. Adviseurs voor restaurants en multi-locatie horecagroepen gebruiken het om methodologieën te standaardiseren, handboeken te reproduceren en audits, onboarding en trainingen te versnellen. Het werkt uitstekend voor zowel integrale culinaire adviestrajecten als losse projectconsultancy." },
      { q: "Is er een AI-agent voor elk professioneel profiel?", a: "Ja. Elk van de 10 agenten is diep gespecialiseerd in één vakgebied. Zo is er AI voor de chef-consultant, sommelier, pâtissier, bakker, pizzaiolo, ijsbereider, chocolatier, barista en bartender. Daarnaast is er nog een management-agent voor het overkoepelende bedrijfsmodel en de financiële haalbaarheid van het hele project." },
      { q: "Wat kost het om te starten met deze AI voor horeca advies?", a: "Je start gratis. Met 5 gratis gebruiken per maand kun jij alle agenten van Consultancy Gastro Pro testen, zonder creditcard en binnen een onboarding van ongeveer 2 minuten." },
    ],
    seoTitle: "Horeca Consultant AI: Adviseer Sneller | AI Chef Pro",
    seoDescription: "Horeca consultant AI met 10 specialisten. Versnel als restaurant consultant of culinair adviseur je projecten. Start nu met 5 gratis gebruiken per maand.",
    seoKeywords: "horeca adviseur, horeca consultant, ai voor horeca, restaurant consultant, culinair adviseur, nbov, sca, horeca adviesbureau, chef consultant, kostprijscalculatie, haccp handboek, culinaire audit",
  },
};

const COLOR_THEMES: Record<string, { bg: string; text: string }> = {
  amber: { bg: 'bg-amber-500/10', text: 'text-amber-600' },
  blue: { bg: 'bg-blue-500/10', text: 'text-blue-600' },
  emerald: { bg: 'bg-emerald-500/10', text: 'text-emerald-600' },
  rose: { bg: 'bg-rose-500/10', text: 'text-rose-600' },
  purple: { bg: 'bg-purple-500/10', text: 'text-purple-600' },
  orange: { bg: 'bg-orange-500/10', text: 'text-orange-600' },
  indigo: { bg: 'bg-indigo-500/10', text: 'text-indigo-600' },
  pink: { bg: 'bg-pink-500/10', text: 'text-pink-600' },
  teal: { bg: 'bg-teal-500/10', text: 'text-teal-600' },
  red: { bg: 'bg-red-500/10', text: 'text-red-600' },
};

function getIconComponent(name: string) {
  const Comp = (LucideIcons as unknown as Record<string, LucideIcons.LucideIcon>)[name];
  return Comp || LucideIcons.Sparkles;
}

export default function ConsultoriaGastroProHub() {
  const { currentLanguage, getAppUrl } = useLanguage();
  const lang = currentLanguage as LangCode;
  const APP_URL = getAppUrl(currentLanguage);

  const ui = UI[lang] || UI.es;
  const segs = SEGMENTS[lang] || SEGMENTS.es;
  const langPrefix = lang === 'es' ? '' : `/${lang}`;
  const canonicalUrl = `${SITE_URL}${langPrefix}/${segs.hub}/${segs.consultorHubSlug}`;

  const consultores = getUseCasesByType('consultor');

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    '@id': `${canonicalUrl}#breadcrumb`,
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: segs.hubLabel, item: `${SITE_URL}${langPrefix}/${segs.hub}` },
      { '@type': 'ListItem', position: 3, name: ui.badge },
    ],
  };

  const collectionSchema = {
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    name: ui.seoTitle,
    description: ui.seoDescription,
    url: canonicalUrl,
    inLanguage: segs.locale,
    isPartOf: {
      '@type': 'WebSite',
      name: 'AI Chef Pro',
      url: SITE_URL,
    },
    hasPart: consultores.map(uc => {
      const content = uc.content[lang] || uc.content.es;
      const slug = uc.slug[lang] || uc.slug.es;
      return {
        '@type': 'Service',
        name: content.h1,
        url: `${SITE_URL}${langPrefix}/${segs.hub}/${segs.consultor}/${slug}`,
        description: content.heroTagline,
        provider: {
          '@type': 'Organization',
          name: 'AI Chef Pro',
          url: SITE_URL,
        },
      };
    }),
  };

  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    '@id': `${canonicalUrl}#faq`,
    inLanguage: segs.locale,
    mainEntity: ui.faqs.map(f => ({
      '@type': 'Question',
      name: f.q,
      acceptedAnswer: { '@type': 'Answer', text: f.a },
    })),
  };

  return (
    <div className="min-h-screen bg-background">
      <SEOHead
        title={ui.seoTitle}
        description={ui.seoDescription}
        keywords={ui.seoKeywords}
        canonical={canonicalUrl}
        ogImage="https://aichef.pro/og/use-cases/consultoria-gastro-pro-hub.jpg"
        disableAutoHreflang
      />
      <Helmet>
        {(['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'] as LangCode[]).map(l => {
          const altSegs = SEGMENTS[l];
          const altPrefix = l === 'es' ? '' : `/${l}`;
          const href = `${SITE_URL}${altPrefix}/${altSegs.hub}/${altSegs.consultorHubSlug}`;
          return <link key={l} rel="alternate" hrefLang={l} href={href} />;
        })}
        <link rel="alternate" hrefLang="x-default" href={`${SITE_URL}/${SEGMENTS.es.hub}/${SEGMENTS.es.consultorHubSlug}`} />
        <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(collectionSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
      </Helmet>

      <ModernHeader />

      <main>
        {/* Hero */}
        <section className="relative overflow-hidden bg-gradient-to-br from-indigo-500/10 via-background to-purple-500/5 py-20 lg:py-28">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <HeroSocialProof />
              <Badge className="mb-6 text-sm px-4 py-2">{ui.badge}</Badge>
              <div className="w-20 h-20 bg-indigo-500/10 rounded-2xl flex items-center justify-center mx-auto mb-6">
                <Briefcase className="h-10 w-10 text-indigo-600" />
              </div>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl mb-6 text-balance">
                {ui.h1}
              </h1>
              <p className="text-xl text-muted-foreground mb-10 max-w-3xl mx-auto text-balance">
                {ui.heroSubtitle}
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                  {ui.ctaPrimary} <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button asChild size="lg" variant="outline">
                  <a href="#agentes-consultoria"><Users className="mr-2 h-4 w-4" /> {ui.ctaSecondary}</a>
                </Button>
              </div>
              <p className="text-sm text-muted-foreground mt-4">{ui.ctaNote}</p>
            </div>
          </div>
        </section>

        {/* Authority — backed by Chefbusiness Consultoría Gastronómica */}
        <AuthorityBackedBy lang={lang} />

        {/* Métricas */}
        <section className="py-16 bg-gradient-to-r from-primary/90 to-primary">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 max-w-5xl mx-auto text-center">
              {[ui.metric1, ui.metric2, ui.metric3, ui.metric4].map((m, i) => (
                <div key={i}>
                  <div className="text-4xl md:text-5xl font-bold text-white mb-2">{m.value}</div>
                  <div className="text-sm text-primary-foreground/80">{m.label}</div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Intro SEO — consultores/asesores por perfil */}
        <section className="py-16">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-3xl">
              <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-6 text-balance">{ui.seoIntroTitle}</h2>
              <p className="text-lg text-muted-foreground leading-relaxed">{ui.seoIntroBody}</p>
            </div>
          </div>
        </section>

        {/* Cards 10 perfiles */}
        <section id="agentes-consultoria" className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-3xl mx-auto">
              <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-4 text-balance">{ui.cardsTitle}</h2>
              <p className="text-muted-foreground">{ui.cardsSubtitle}</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
              {consultores.map(uc => {
                const content = uc.content[lang] || uc.content.es;
                const theme = COLOR_THEMES[uc.colorTheme] || COLOR_THEMES.amber;
                const slug = uc.slug[lang] || uc.slug.es;
                const Icon = getIconComponent(uc.iconKey);
                return (
                  <Link key={uc.id} to={`${langPrefix}/${segs.hub}/${segs.consultor}/${slug}`}>
                    <Card className="h-full border-2 hover:border-primary transition-all hover:shadow-xl">
                      <CardHeader>
                        <div className={`w-14 h-14 ${theme.bg} rounded-xl flex items-center justify-center mb-3`}>
                          <Icon className={`h-7 w-7 ${theme.text}`} />
                        </div>
                        <CardTitle className="text-xl">{content.h1}</CardTitle>
                      </CardHeader>
                      <CardContent>
                        <p className="text-sm text-muted-foreground mb-4">{content.heroTagline}</p>
                        <div className="flex items-center text-primary text-sm font-semibold">
                          {ui.cardCta} <ArrowRight className="ml-1 h-4 w-4" />
                        </div>
                      </CardContent>
                    </Card>
                  </Link>
                );
              })}
            </div>
          </div>
        </section>

        {/* ¿Para quién? */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-3xl mx-auto">
              <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-4 text-balance">{ui.forWhoTitle}</h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto">
              <Card className="border-2 border-indigo-200 shadow-md">
                <CardHeader>
                  <div className="w-14 h-14 bg-indigo-500/10 rounded-xl flex items-center justify-center mb-3">
                    <Users className="h-7 w-7 text-indigo-600" />
                  </div>
                  <CardTitle className="text-xl">{ui.forWho1Title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">{ui.forWho1Body}</p>
                </CardContent>
              </Card>
              <Card className="border-2 border-purple-200 shadow-md">
                <CardHeader>
                  <div className="w-14 h-14 bg-purple-500/10 rounded-xl flex items-center justify-center mb-3">
                    <Building2 className="h-7 w-7 text-purple-600" />
                  </div>
                  <CardTitle className="text-xl">{ui.forWho2Title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">{ui.forWho2Body}</p>
                </CardContent>
              </Card>
              <Card className="border-2 border-amber-200 shadow-md">
                <CardHeader>
                  <div className="w-14 h-14 bg-amber-500/10 rounded-xl flex items-center justify-center mb-3">
                    <TrendingUp className="h-7 w-7 text-amber-600" />
                  </div>
                  <CardTitle className="text-xl">{ui.forWho3Title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">{ui.forWho3Body}</p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* FAQ */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-3xl mx-auto">
              <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-4 text-balance">{ui.faqTitle}</h2>
            </div>
            <div className="max-w-3xl mx-auto space-y-4">
              {ui.faqs.map((f, i) => (
                <details key={i} className="group rounded-xl border-2 bg-card p-6 transition-all hover:border-primary">
                  <summary className="flex cursor-pointer items-center justify-between text-lg font-semibold text-foreground list-none">
                    {f.q}
                    <ArrowRight className="h-5 w-5 shrink-0 text-primary transition-transform group-open:rotate-90" />
                  </summary>
                  <p className="mt-4 text-muted-foreground leading-relaxed">{f.a}</p>
                </details>
              ))}
            </div>
          </div>
        </section>

        {/* CTA final */}
        <section className="py-20 bg-gradient-to-br from-indigo-500/10 via-background to-purple-500/5">
          <div className="container mx-auto px-4 text-center">
            <Sparkles className="h-10 w-10 text-indigo-600 mx-auto mb-4" />
            <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-4 text-balance">{ui.finalH2}</h2>
            <p className="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">{ui.finalBody}</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                {ui.finalCta} <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button asChild size="lg" variant="outline">
                <Link to={`${langPrefix}/${segs.hub}`}>{segs.hubLabel} <ArrowRight className="ml-2 h-4 w-4" /></Link>
              </Button>
            </div>
          </div>
        </section>
      </main>

      <ModernFooter />
      <WhatsAppFloatingButton />
    </div>
  );
}
