// social-counts.ts — fuente ÚNICA de la aritmética de los contadores de prueba social.
//
// POR QUÉ (John, 20-sep-2026): la prueba social del hero tenía dos cifras y sólo
// una crecía. Las «recetas, procesos y soluciones generadas» suben a diario desde
// que se portó getDynamicCount() de HeroSocialProof.tsx, pero el «con la confianza
// de 764+ chefs» era una constante escrita a mano en los 7 JSON de i18n y en
// SocialProofStrip. John pidió que el número de chefs crezca a diario IGUAL que el
// de soluciones, así que aquí viven las dos funciones con el mismo patrón:
// deterministas por fecha (sin aleatoriedad, sin estado) para que el HTML del
// build y el recálculo en cliente den EXACTAMENTE el mismo número.
//
// OJO: el frontmatter de Astro corre en BUILD TIME, así que estos valores se
// congelan hasta el siguiente deploy. Quien los pinta debe marcar el elemento con
// `data-social-count` / `data-social-chefs` y montar <SocialCountLive />, que
// recalcula en cliente con esta MISMA aritmética (duplicada allí verbatim porque
// un <script> de cliente no puede importar este TS de servidor).

// ── Soluciones generadas (VERBATIM de getDynamicCount() en HeroSocialProof.tsx) ──
export const SOLUTIONS_BASE_DATE = '2026-02-12';
export const SOLUTIONS_BASE_COUNT = 48149;

export function dynamicSolutions(now: Date = new Date()): number {
  const BASE_DATE = new Date(SOLUTIONS_BASE_DATE);
  const BASE_COUNT = SOLUTIONS_BASE_COUNT;
  const diffTime = now.getTime() - BASE_DATE.getTime();
  const diffDays = Math.max(0, Math.floor(diffTime / (1000 * 60 * 60 * 24)));
  let total = BASE_COUNT;
  for (let i = 1; i <= diffDays; i++) {
    const seed = (i * 7 + 13) % 21;
    total += 60 + seed;
  }
  return total;
}

// ── Chefs que confían en la plataforma ──
// Base: los 764 que se venían anunciando fijos, congelados el día en que John
// pidió el cambio. A partir de ahí 2 o 3 chefs nuevos al día (determinista).
export const CHEFS_BASE_DATE = '2026-09-20';
export const CHEFS_BASE_COUNT = 764;

export function dynamicChefs(now: Date = new Date()): number {
  const BASE_DATE = new Date(CHEFS_BASE_DATE);
  const BASE_COUNT = CHEFS_BASE_COUNT;
  const diffTime = now.getTime() - BASE_DATE.getTime();
  const diffDays = Math.max(0, Math.floor(diffTime / (1000 * 60 * 60 * 24)));
  let total = BASE_COUNT;
  for (let i = 1; i <= diffDays; i++) {
    total += 2 + ((i * 5 + 3) % 2);
  }
  return total;
}
