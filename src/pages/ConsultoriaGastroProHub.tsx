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
  seoTitle: string;
  seoDescription: string;
  seoKeywords: string;
}> = {
  es: {
    badge: 'Consultoría Gastro Pro',
    h1: 'IA para Consultoría Gastronómica Profesional',
    heroSubtitle: 'Descubre cómo AI Chef Pro potencia el trabajo de consultores, asesores y especialistas independientes que trabajan por proyectos para restaurantes, hoteles, grupos de restauración e inversores del sector gastronómico.',
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
    seoTitle: 'Consultoría Gastro Pro: 10 Agentes de IA para Consultores Gastronómicos | AI Chef Pro',
    seoDescription: 'Módulo de IA especializado para consultores gastronómicos, chefs consultores, sommeliers, bartenders, baristas, pasteleros, panaderos, pizzeros, heladeros y chocolateros que trabajan por proyectos. Empieza gratis.',
    seoKeywords: 'consultor gastronómico IA, chef consultor IA, asesor gastronómico inteligencia artificial, consultoría restaurantes IA, sommelier consultor, bartender consultor, barista consultor, pastelero consultor, panadero consultor, pizzero consultor, heladero consultor, chocolatero consultor, agente IA consultoría hostelería',
  },
  en: {
    badge: 'Gastro Consultancy Pro',
    h1: 'AI for Professional Gastronomic Consulting',
    heroSubtitle: 'See how AI Chef Pro powers the work of consultants, advisors, and independent specialists running project-based engagements for restaurants, hotels, restaurant groups, and food & beverage investors.',
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
    seoTitle: 'Gastro Consultancy Pro: AI for Restaurant & F&B Consultants | AI Chef Pro',
    seoDescription: 'AI module for restaurant & F&B consultants, chef consultants, sommeliers, bar consultants, coffee shop consultants, pastry, bakery, pizza, gelato & chocolate advisors. Start free.',
    seoKeywords: 'restaurant consultant AI, F&B consultant software, chef consultant, sommelier consultant, bar consultant, coffee shop consultant, pastry consultant, bakery consultant, pizza consultant, gelato consultant, chocolate consultant, hospitality consulting AI, consulting chef tool',
  },
  fr: {
    badge: 'Conseil Gastro Pro',
    h1: 'IA pour la Consultance Gastronomique Professionnelle',
    heroSubtitle: 'Découvrez comment AI Chef Pro accompagne consultants en restauration, conseillers CHR, experts en métiers de bouche et professionnels indépendants travaillant par projet pour restaurants, hôtels, groupes de restauration et investisseurs.',
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
    seoTitle: 'Conseil Gastro Pro : 10 Agents IA pour Consultants en Restauration | AI Chef Pro',
    seoDescription: 'Module IA pour consultants en restauration, chef consultants, sommeliers, barmen, baristas, pâtissiers, boulangers, pizzaïolos, glaciers et chocolatiers en CHR. Démarrer gratuitement.',
    seoKeywords: 'consultant en restauration IA, conseil CHR, métiers de bouche, consultant gastronomique, chef consultant, sommelier consultant, consultant cocktail, barista consultant, pâtissier consultant, boulanger consultant, pizzaïolo consultant, MOF, cabinet conseil restauration',
  },
  de: {
    badge: 'Gastro Beratung Pro',
    h1: 'KI für professionelle Gastronomieberatung',
    heroSubtitle: 'Entdecken Sie, wie AI Chef Pro Gastronomieberater, Restaurantberater, IHK-zertifizierte Fachleute und selbstständige Projektberater bei der Arbeit für Restaurants, Hotels, Restaurantgruppen, Investmentfonds und Gastronomie-Unternehmer unterstützt. BAFA-Förderung bis 50–70 % für KMU-Beratung möglich.',
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
    seoTitle: 'Gastro Beratung Pro: KI-Agenten für Gastronomieberater | AI Chef Pro',
    seoDescription: 'KI-Modul für Gastronomieberater, Restaurantberater, Sommeliers, Barberater, Barista-Coaches, Konditor-, Bäcker-, Pizza-, Eisdiele- und Chocolatier-Berater. BAFA-Förderung. Kostenlos starten.',
    seoKeywords: 'Gastronomieberatung KI, Restaurantberatung Software, Gastronomieberater, BAFA-Förderung Beratung, Küchencoaching, Sommelier-Berater, Bar-Consulting, Barista-Coach, Konditorei-Beratung, Bäckereiberatung, Pizzeria-Beratung, KI Gastgewerbe',
  },
  it: {
    badge: 'Consulenza Gastro Pro',
    h1: 'AI per la Consulenza Gastronomica Professionale (IA Ristorazione)',
    heroSubtitle: 'Scopri come AI Chef Pro accompagna consulenti di ristorazione, food consultant, advisor HORECA e professionisti indipendenti che lavorano per progetto al servizio di ristoranti, hotel, gruppi della ristorazione e investitori del settore gastronomico.',
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
    seoTitle: 'Consulenza Gastro Pro: AI per Consulenti Ristorazione | AI Chef Pro',
    seoDescription: 'Modulo AI per consulenti di ristorazione, chef consulenti, sommelier AIS, bartender, barista, pasticcieri, panettieri, pizzaioli AVPN, gelatieri e cioccolatieri artigianali. Inizia gratis.',
    seoKeywords: 'consulente ristorazione AI, consulenza ristorazione, food consultant Italia, AI ristorazione, IA gastronomia, consulenza HORECA, chef consulente, sommelier AIS, consulenza pizzeria AVPN, consulenza gelateria artigianale, pasticceria consulenza, barista consulente, bartender mixology',
  },
  pt: {
    badge: 'Consultoria Gastro Pro',
    h1: 'IA para Consultoria Gastronômica/Gastronómica Profissional',
    heroSubtitle: 'Descubra como o AI Chef Pro potencia consultores gastronômicos, consultores de alimentos e bebidas (A&B), assessores de restaurantes e profissionais independentes que trabalham por projeto ao serviço de restaurantes, hotéis, grupos de restauração e investidores no Brasil e em Portugal.',
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
    seoTitle: 'Consultoria Gastro Pro: 10 Agentes de IA para Consultores Gastronômicos | AI Chef Pro',
    seoDescription: 'Módulo de IA para consultores gastronômicos/gastronómicos, chefs consultores, sommeliers, bartenders, baristas, confeiteiros, padeiros, pizzaiolos, sorveteiros e chocolateiros. Começar grátis.',
    seoKeywords: 'consultor gastronômico IA, consultoria gastronômica, consultor A&B, consultor restaurantes, consultoria HORECA, chef consultor, sommelier consultor, consultor café especialidade, consultor coquetelaria, consultor confeitaria, consultor pastelaria, consultor padaria artesanal, consultor sorveteria, consultor chocolataria, consultor pizzaria',
  },
  nl: {
    badge: 'Gastro Advies Pro',
    h1: 'AI Horeca Adviseur — Gastro Advies Pro voor de Horeca',
    heroSubtitle: 'Ontdek hoe AI Chef Pro horeca-adviseurs, restaurant consultants en zelfstandige professionals ondersteunt die op projectbasis werken voor restaurants, hotels, restaurantgroepen, investeerders en horeca-ondernemers in Nederland en Vlaanderen.',
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
    seoTitle: 'Gastro Advies Pro: AI Horeca Adviseur en Restaurant Consultant | AI Chef Pro',
    seoDescription: 'AI-module voor horeca-adviseurs, restaurant consultants, sommeliers, bartenders, barista coaches, banketbakker- en bakker-adviseurs, pizza chef, ijssalon- en chocolatier-adviseurs.',
    seoKeywords: 'horeca adviseur AI, restaurant consultant Nederland, horeca consultancy, gastronomisch adviseur, chef consultant culinair adviseur, sommelier wijnadviseur, bar consultant cocktail consultant, barista coach specialty coffee, banketbakker adviseur, bakker adviseur NBOV, pizza chef pizzaiolo SVH, ijssalon adviseur, chocolatier adviseur, horeca AI Nederland Vlaanderen',
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
      };
    }),
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
