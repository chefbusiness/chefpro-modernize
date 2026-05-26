import { Sparkles } from 'lucide-react';
import type { LangCode } from '@/data/use-cases';

type BlurbParts = {
  intro: string;
  beforeLink: string;
  linkText: string;
  afterLink: string;
};

const BLURBS: Record<LangCode, BlurbParts> = {
  es: {
    intro: 'Respaldados por consultores reales',
    beforeLink: 'Agentes de IA desarrollados y entrenados junto al equipo de consultores gastronómicos de ',
    linkText: 'Chefbusiness Consultoría Gastronómica',
    afterLink: ', una de las agencias de referencia en consultoría y asesoría para restaurantes y negocios de hostelería en España y Latinoamérica.',
  },
  en: {
    intro: 'Backed by real-world consultants',
    beforeLink: 'AI agents developed and trained alongside the team of gastronomy consultants at ',
    linkText: 'Chefbusiness Gastronomy Consulting',
    afterLink: ', one of the leading consulting and advisory agencies for restaurants and hospitality businesses across Spain and Latin America.',
  },
  fr: {
    intro: 'Adossés à de vrais consultants du terrain',
    beforeLink: 'Agents IA développés et entraînés aux côtés de l\'équipe de consultants gastronomiques de ',
    linkText: 'Chefbusiness Conseil Gastronomique',
    afterLink: ', l\'une des agences de référence en conseil et accompagnement pour restaurants et entreprises de l\'hôtellerie-restauration en Espagne et Amérique latine.',
  },
  de: {
    intro: 'Unterstützt von echten Beratern aus der Praxis',
    beforeLink: 'KI-Agenten, entwickelt und trainiert gemeinsam mit dem Team gastronomischer Berater von ',
    linkText: 'Chefbusiness Gastronomieberatung',
    afterLink: ', einer der führenden Beratungsagenturen für Restaurants und Gastronomiebetriebe in Spanien und Lateinamerika.',
  },
  it: {
    intro: 'Sostenuti da consulenti reali del settore',
    beforeLink: 'Agenti IA sviluppati e addestrati insieme al team di consulenti gastronomici di ',
    linkText: 'Chefbusiness Consulenza Gastronomica',
    afterLink: ', una delle agenzie di riferimento per la consulenza e l\'assistenza a ristoranti e attività della ristorazione in Spagna e America Latina.',
  },
  pt: {
    intro: 'Respaldados por consultores reais do setor',
    beforeLink: 'Agentes de IA desenvolvidos e treinados junto à equipa de consultores gastronômicos da ',
    linkText: 'Chefbusiness Consultoria Gastronómica',
    afterLink: ', uma das agências de referência em consultoria e assessoria para restaurantes e negócios de restauração na Espanha e América Latina.',
  },
  nl: {
    intro: 'Ondersteund door echte consultants uit het vak',
    beforeLink: 'AI-agenten ontwikkeld en getraind samen met het team van gastronomisch adviseurs van ',
    linkText: 'Chefbusiness Gastronomisch Advies',
    afterLink: ', een van de toonaangevende adviesbureaus voor restaurants en horeca-ondernemingen in Spanje en Latijns-Amerika.',
  },
};

interface Props {
  lang: LangCode;
}

export default function AuthorityBackedBy({ lang }: Props) {
  const b = BLURBS[lang] || BLURBS.es;
  return (
    <section className="py-10 bg-gradient-to-r from-indigo-500/5 via-background to-purple-500/5 border-y border-border/40">
      <div className="container mx-auto px-4">
        <div className="max-w-4xl mx-auto flex flex-col sm:flex-row items-center gap-4 text-center sm:text-left">
          <div className="flex items-center gap-2 flex-shrink-0">
            <Sparkles className="h-5 w-5 text-indigo-600" />
            <span className="text-xs font-semibold uppercase tracking-wider text-indigo-700">
              {b.intro}
            </span>
          </div>
          <p className="text-sm md:text-base text-foreground/85 leading-relaxed">
            {b.beforeLink}
            <a
              href="https://chefbusiness.co"
              target="_blank"
              rel="noopener noreferrer"
              className="font-semibold text-indigo-700 hover:text-indigo-900 underline underline-offset-2 decoration-indigo-300 hover:decoration-indigo-600 transition-colors"
            >
              {b.linkText}
            </a>
            {b.afterLink}
          </p>
        </div>
      </div>
    </section>
  );
}
