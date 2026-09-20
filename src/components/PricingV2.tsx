/**
 * PricingV2 — gemelo React de astro-site/src/components/Pricing.astro (v2
 * «Pricing cards reordered around role», CRO Keak 20-sep-2026).
 * Spec literal: CRO_HOME_KEAK_2026-09-20.md §1 «Cambio 3» + §4 + §5.
 *
 * POR QUÉ EXISTE: las 8 landings de marketing y las 6 herramientas gratuitas
 * viven en la SPA y se sirven como islands `client:load` (SSR + hidratación),
 * así que su tabla de precios no puede ser el .astro. Este componente reproduce
 * el MISMO markup, las MISMAS clases y los MISMOS marcadores (`data-keak`,
 * `data-plan`, `data-popular`, `data-role-chip`) para que
 * scripts/cro-home/keak-dist-gate.py valide portadas, páginas de precios e
 * islands con el mismo código.
 *
 * Diferencias deliberadas con el .astro, y sólo estas:
 *   · i18n por react-i18next (el .astro usa t()/tList() de astro-site) — MISMAS claves.
 *   · URL de plataforma por useLanguage().getAppUrl() (el .astro usa appCtaUrl()).
 *   · SIN JSON-LD Product: lo emite ya la página Astro que monta el island.
 *   · El resalte de los chips es un onClick de React en vez de un <script>.
 *
 * Tailwind: 'ring-4' y 'ring-accent/50' sólo aparecen dentro del handler. El
 * escáner lee este fichero como TEXTO (astro-site/tailwind.config.ts incluye
 * ../src/components/*.tsx), así que las genera igual; si alguien reescribe el
 * handler, que no pierda esas dos cadenas literales.
 */
import { Fragment, useCallback, useEffect, useRef, type MouseEvent } from 'react';
import { useTranslation } from 'react-i18next';
import { ArrowRight, Check } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

interface PlanV2 {
  id: string;
  /** utm_content del CTA. */
  slug: string;
  name: string;
  eyebrow: string;
  description: string;
  price: string;
  period?: string;
  originalPrice?: string;
  discount?: string;
  credits: string;
  /** '∞ ' delante de los créditos en los dos planes ilimitados. */
  creditsPrefix?: string;
  hint: string;
  cta: string;
  features: string[];
  popular?: boolean;
  unlimitedBadge?: string;
}

interface PricingV2Props {
  /** utm_medium del CTA: 'landing-…' (landings) | 'tool-…' (herramientas gratuitas). */
  medium: string;
}

const cardClass = (plan: PlanV2) =>
  `relative flex h-full flex-col rounded-xl p-6 scroll-mt-28 transition-shadow ${
    plan.popular
      ? 'border-2 border-accent bg-accent/5 shadow-xl'
      : 'border border-border bg-card shadow-sm hover:shadow-md'
  }`;

const ctaClass = (plan: PlanV2) =>
  `mt-5 inline-flex h-11 w-full items-center justify-center gap-1 rounded-md px-4 text-sm font-semibold transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 ${
    plan.popular ? 'btn-gold' : 'bg-primary text-primary-foreground hover:bg-primary/90'
  }`;

export default function PricingV2({ medium }: PricingV2Props) {
  const { t, i18n } = useTranslation();
  const { getAppUrl } = useLanguage();
  const timers = useRef<Record<string, number>>({});

  // Chips de rol: sin JS siguen siendo anclas (#plan-…). Con JS, scroll suave y
  // resalte de 2 s sobre la tarjeta destino (mismo comportamiento que el .astro).
  const highlight = useCallback((event: MouseEvent<HTMLAnchorElement>, planId: string) => {
    const card = document.getElementById(`plan-${planId}`);
    if (!card) return;
    event.preventDefault();
    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
    card.classList.add('ring-4', 'ring-accent/50');
    window.clearTimeout(timers.current[planId]);
    timers.current[planId] = window.setTimeout(() => {
      card.classList.remove('ring-4', 'ring-accent/50');
    }, 2000);
  }, []);

  useEffect(() => {
    const pending = timers.current;
    return () => Object.values(pending).forEach((id) => window.clearTimeout(id));
  }, []);

  const p = (id: string, key: string) => t(`pricing.plans.${id}.${key}`) as string;

  // features.0..n son claves numéricas de objeto en los JSON (igual que en el .astro).
  const feat = (id: string, n: number) =>
    Array.from({ length: n }, (_, i) => t(`pricing.plans.${id}.features.${i}`) as string);

  // Sólo para campos ESTRUCTURALES opcionales (period): i18next devuelve la
  // propia clave cuando no existe en ningún idioma. El COPY no se oculta: una
  // clave v2_ sin traducir tiene que verse para que el gate la cace.
  const opt = (id: string, key: string) => {
    const full = `pricing.plans.${id}.${key}`;
    const value = t(full) as string;
    return value === full ? undefined : value;
  };

  // member es el único con lista propia v2 (v2_features[4]); si un idioma aún no
  // la tiene, cae a sus features de siempre en vez de quedarse sin lista.
  const rawMemberFeatures = t('pricing.plans.member.v2_features', {
    returnObjects: true,
  }) as unknown as string[];
  const memberFeatures = Array.isArray(rawMemberFeatures) ? rawMemberFeatures : [];

  const member: PlanV2 = {
    id: 'member',
    slug: 'member',
    name: p('member', 'name'),
    eyebrow: p('member', 'v2_eyebrow'),
    description: p('member', 'v2_description'),
    price: p('member', 'price'),
    period: opt('member', 'period'),
    credits: p('member', 'v2_credits'),
    hint: p('member', 'v2_hint'),
    cta: p('member', 'v2_cta'),
    features: memberFeatures.length ? memberFeatures : feat('member', 4),
  };

  const premiumPro: PlanV2 = {
    id: 'premium_pro',
    slug: 'premium-pro',
    name: p('premium_pro', 'name'),
    eyebrow: p('premium_pro', 'v2_eyebrow'),
    description: p('premium_pro', 'v2_description'),
    price: p('premium_pro', 'price'),
    period: p('premium_pro', 'period'),
    credits: p('premium_pro', 'v2_credits'),
    hint: p('premium_pro', 'v2_hint'),
    cta: p('premium_pro', 'v2_cta'),
    features: feat('premium_pro', 5),
  };

  const premiumPlus: PlanV2 = {
    id: 'premium_plus',
    slug: 'premium-plus',
    name: p('premium_plus', 'name'),
    eyebrow: p('premium_plus', 'v2_eyebrow'),
    description: p('premium_plus', 'v2_description'),
    price: p('premium_plus', 'price'),
    period: p('premium_plus', 'period'),
    credits: p('premium_plus', 'v2_credits'),
    hint: p('premium_plus', 'v2_hint'),
    cta: p('premium_plus', 'v2_cta'),
    features: feat('premium_plus', 5),
    popular: true,
  };

  const premiumMax: PlanV2 = {
    id: 'premium_max',
    slug: 'premium-max',
    name: p('premium_max', 'name'),
    eyebrow: p('premium_max', 'v2_eyebrow'),
    description: p('premium_max', 'v2_description'),
    price: p('premium_max', 'price'),
    period: p('premium_max', 'period'),
    credits: p('premium_max', 'v2_credits'),
    creditsPrefix: '∞ ',
    hint: p('premium_max', 'v2_hint'),
    cta: p('premium_max', 'v2_cta'),
    features: feat('premium_max', 7),
    unlimitedBadge: t('pricing.unlimited_badge') as string,
  };

  const premiumPlusAnnual: PlanV2 = {
    id: 'premium_plus_annual',
    slug: 'premium-max-annual',
    name: p('premium_plus_annual', 'name'),
    eyebrow: p('premium_plus_annual', 'v2_eyebrow'),
    description: p('premium_plus_annual', 'v2_description'),
    price: p('premium_plus_annual', 'price'),
    period: p('premium_plus_annual', 'period'),
    originalPrice: p('premium_plus_annual', 'original_price'),
    discount: p('premium_plus_annual', 'discount'),
    credits: p('premium_plus_annual', 'v2_credits'),
    creditsPrefix: '∞ ',
    hint: p('premium_plus_annual', 'v2_hint'),
    cta: p('premium_plus_annual', 'v2_cta'),
    features: feat('premium_plus_annual', 6),
  };

  // Fila 1 = los 3 planes mensuales de entrada; fila 2 = ilimitado y compromiso anual.
  const rows = [
    { grid: 'mx-auto grid max-w-5xl gap-6 md:grid-cols-3', plans: [member, premiumPro, premiumPlus] },
    { grid: 'mx-auto grid max-w-3xl gap-6 md:grid-cols-2', plans: [premiumMax, premiumPlusAnnual] },
  ];

  // Chips de rol → plan. Sólo los 4 mensuales (el anual no es un «rol»).
  const roleChips = [
    { plan: member, role: t('pricing.v2_role_member') as string, short: p('member', 'v2_short') },
    { plan: premiumPro, role: t('pricing.v2_role_premium_pro') as string, short: p('premium_pro', 'v2_short') },
    { plan: premiumPlus, role: t('pricing.v2_role_premium_plus') as string, short: p('premium_plus', 'v2_short') },
    { plan: premiumMax, role: t('pricing.v2_role_premium_max') as string, short: p('premium_max', 'v2_short') },
  ];

  const appUrl = getAppUrl();
  const ctaHref = (plan: PlanV2) =>
    `${appUrl}/?utm_source=web&utm_medium=${medium}&utm_content=${plan.slug}`;

  // «Talk to us for an enterprise plan»: sólo hay página de contacto en español.
  const lang = (i18n.language || 'es').slice(0, 2);
  const enterpriseHref = lang === 'es' ? '/contacto' : 'mailto:info@aichef.pro';

  return (
    <section id="pricing" data-keak="pricing-v2" className="container py-8 md:py-12 lg:py-24 scroll-mt-28">
      <div className="mx-auto flex max-w-[58rem] flex-col items-center justify-center gap-4 text-center">
        <h2 className="text-3xl font-bold leading-[1.1] text-balance md:text-5xl">{t('pricing.v2_title')}</h2>
        <p className="max-w-[48rem] text-balance leading-normal text-muted-foreground sm:text-lg sm:leading-7">
          {t('pricing.v2_description')}
        </p>
      </div>

      <div className="mx-auto mt-8 flex max-w-4xl flex-wrap justify-center gap-2">
        {roleChips.map((chip) => (
          <a
            key={chip.plan.id}
            href={`#plan-${chip.plan.id}`}
            data-role-chip=""
            onClick={(event) => highlight(event, chip.plan.id)}
            className="inline-flex items-center gap-1 rounded-full border border-border bg-background px-3 py-1.5 text-xs text-muted-foreground transition-colors hover:border-accent hover:text-foreground"
          >
            <span>{chip.role} →</span>
            <strong className="font-semibold text-foreground">{chip.short} {chip.plan.price}</strong>
          </a>
        ))}
      </div>

      {rows.map((row, i) => (
        // <Fragment> y no un <div>: el .astro no envuelve la fila, y un div
        // extra cambiaría el DOM que compara la paridad visual.
        <Fragment key={i}>
          {i === 1 && (
            <div className="mx-auto mt-12 flex max-w-3xl items-center gap-4">
              <span className="h-px flex-1 bg-border" aria-hidden="true"></span>
              <span className="text-center text-xs font-semibold uppercase tracking-[0.2em] text-muted-foreground">
                {t('pricing.v2_divider')}
              </span>
              <span className="h-px flex-1 bg-border" aria-hidden="true"></span>
            </div>
          )}

          <div className={`${row.grid} ${i === 0 ? 'mt-10' : 'mt-8'}`}>
            {row.plans.map((plan) => (
              <article
                key={plan.id}
                id={`plan-${plan.id}`}
                data-plan={plan.id}
                data-popular={plan.popular ? 'true' : undefined}
                className={cardClass(plan)}
              >
                {plan.popular && (
                  <span className="absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap rounded-full bg-accent px-3 py-1 text-xs font-semibold text-black shadow">
                    🔥 {t('pricing.most_popular')}
                  </span>
                )}

                {plan.unlimitedBadge && (
                  <span className="absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap rounded-full bg-primary px-3 py-1 text-xs font-semibold text-primary-foreground shadow">
                    ∞ {plan.unlimitedBadge}
                  </span>
                )}

                {plan.discount && (
                  <span className="absolute -top-3 right-4 whitespace-nowrap rounded-full bg-emerald-600 px-2.5 py-1 text-xs font-bold text-white shadow">
                    {plan.discount}
                  </span>
                )}

                <span className="inline-flex w-fit rounded-full bg-accent/15 px-2.5 py-1 text-[11px] font-semibold uppercase tracking-wider text-accent-dark">
                  {plan.eyebrow}
                </span>

                <h3 className="mt-3 text-lg font-bold text-foreground">{plan.name}</h3>
                <p className="mt-2 text-sm text-muted-foreground">{plan.description}</p>

                <div className="mt-4">
                  {plan.originalPrice && (
                    <span className="block text-sm text-muted-foreground line-through">{plan.originalPrice}</span>
                  )}
                  <div className="flex items-baseline gap-1">
                    <span className="text-4xl font-bold text-foreground">{plan.price}</span>
                    {plan.period && <span className="text-muted-foreground">{plan.period}</span>}
                  </div>
                </div>

                <div className="mt-4 rounded-md border-l-4 border-accent bg-muted/60 px-3 py-2">
                  <strong className="text-sm text-foreground">{plan.creditsPrefix}{plan.credits}</strong>
                  <span className="block text-xs text-muted-foreground">{plan.hint}</span>
                </div>

                <a
                  href={ctaHref(plan)}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={ctaClass(plan)}
                >
                  {plan.cta} →
                </a>

                <ul className="mt-5 space-y-2.5 text-sm">
                  {plan.features.map((feature, fi) => (
                    <li key={fi} className="flex items-start gap-2 text-foreground">
                      <Check
                        className="mt-0.5 h-4 w-4 flex-shrink-0 text-accent"
                        strokeWidth={2.5}
                        aria-hidden="true"
                      />
                      <span>{feature}</span>
                    </li>
                  ))}
                </ul>
              </article>
            ))}
          </div>
        </Fragment>
      ))}

      <div className="mt-12 text-center">
        <p className="text-balance text-sm text-muted-foreground">
          {t('pricing.v2_enterprise_question')}{' '}
          <a href={enterpriseHref} className="inline-flex items-center gap-1 font-semibold text-accent-dark hover:underline">
            {t('pricing.v2_enterprise_link')}
            <ArrowRight className="h-4 w-4" aria-hidden="true" />
          </a>
        </p>
      </div>
    </section>
  );
}
