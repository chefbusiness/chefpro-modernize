# SEO Audit Consultoría Gastro Pro — FINDINGS CONSOLIDATED 2026-05-26 (v2)

> 7/7 agentes completados. Reescrito tras feedback crítico del user.

---

## 🔒 NOMBRES OFICIALES DE LOS 10 AGENTES (INMUTABLES)

Cada landing del módulo es la página de un **agente IA con nombre propio**. El H1 = nombre del agente = **MARCA REGISTRADA del producto**. NO se cambia bajo ningún concepto. Las recomendaciones de los 7 agentes de keyword research que sugerían renombrar el H1 quedan **DESCARTADAS**.

| # | ES | EN | IT | FR | DE | PT | NL |
|---|---|---|---|---|---|---|---|
| 1 | Consultor Gastronómico | Gastronomy Consultant | Consulente Gastronomico | Consultant Gastronomique | Gastronomie-Berater | Consultor Gastronômico | Gastronomisch Adviseur |
| 2 | Chef Consultor Pro | Chef Consultant Pro | Chef Consulente Pro | Chef Consultant Pro | Chef-Berater Pro | Chef Consultor Pro | Chef Consultant Pro |
| 3 | Heladero Consultor Pro | Gelato & Ice Cream Consultant Pro | Gelatiere Consulente Pro | Glacier Consultant Pro | Eisdiele-Berater Pro | Sorveteiro Consultor Pro | IJssalon Adviseur Pro |
| 4 | Chocolatero Consultor Pro | Chocolatier Consultant Pro | Cioccolatiere Consulente Pro | Chocolatier Consultant Pro | Chocolatier-Berater Pro | Chocolateiro Consultor Pro | Chocolatier Adviseur Pro |
| 5 | Pastelero Consultor Pro | Pastry Chef Consultant Pro | Pasticciere Consulente Pro | Pâtissier Consultant Pro | Konditor-Berater Pro | Confeiteiro Consultor Pro | Banketbakker Adviseur Pro |
| 6 | Pizzero Consultor Pro | Pizza Chef Consultant Pro | Pizzaiolo Consulente Pro | Pizzaïolo Consultant Pro | Pizza-Berater Pro | Pizzaiolo Consultor Pro | Pizza Chef Adviseur Pro |
| 7 | Barista Consultor Pro | Barista Consultant Pro | Barista Consulente Pro | Barista Consultant Pro | Barista-Berater Pro | Barista Consultor Pro | Barista Adviseur Pro |
| 8 | Sommelier Consultor Pro | Sommelier Consultant Pro | Sommelier Consulente Pro | Sommelier Consultant Pro | Sommelier-Berater Pro | Sommelier Consultor Pro | Sommelier Adviseur Pro |
| 9 | Bartender Consultor Pro | Bartender Consultant Pro | Bartender Consulente Pro | Bartender Consultant Pro | Bartender-Berater Pro | Bartender Consultor Pro | Bartender Adviseur Pro |
| 10 | Panadero Consultor Pro | Baker Consultant Pro | Panettiere Consulente Pro | Boulanger Consultant Pro | Bäcker-Berater Pro | Padeiro Consultor Pro | Bakker Adviseur Pro |

→ **Estos H1 son inmutables.** La SEO se gana en:
1. `heroSubtitle` (debajo del H1)
2. H2 de cada sección
3. `seo.title` / `seo.description` (meta tags)
4. `seo.keywords`
5. Body copy + FAQs (PAA verbatim)

---

## 🚨 BUGS TÉCNICOS REALES (del audit transversal del último agente)

### BUGS CRÍTICOS

#### BUG-1 · Hub UI fallback a ES para 5 idiomas (FR/DE/IT/PT/NL)
- **Archivo**: `src/pages/ConsultoriaGastroProHub.tsx:140` — `const ui = UI[lang] || UI.es;`
- **Síntoma**: `UI` solo define `es` y `en`. FR/DE/IT/PT/NL ven badge, métricas, "¿Para quién?", CTAs, **seoTitle/seoDescription/seoKeywords todos en español**.
- **Impacto**: ALTO. Los 5 hubs no-ES tienen `<title>` y meta en español → duplicate title con hub ES + bounce alto + JSON-LD `inLanguage` mismatch.
- **Fix**: Añadir bloques fr/de/it/pt/nl al objeto `UI` (líneas 49-115) con copy localizado.

#### BUG-2 · Spoke UI shell fallback a ES para 50 spokes (5 idiomas × 10)
- **Archivo**: `src/pages/UseCasePage.tsx:138` — mismo patrón.
- **Síntoma**: 50 spokes muestran `ctaPrimary` ("Empezar gratis"), `siblingHeadingConsultor` ("Otros Agentes de Consultoría Gastro Pro"), `beforeAfterTitle`, `galleryAltSuffix` (alt text) y `serviceTypeConsultor` (Service schema) en español.
- **Impacto**: ALTO. Botones/headings ES en páginas FR/DE/IT/PT/NL + alt text parcialmente ES.
- **Fix**: Añadir bloques fr/de/it/pt/nl al objeto `UI` en `UseCasePage.tsx:34-109`.

#### BUG-3 · `app.category` en español en los 60 spokes no-ES
- **Archivos**: `use-cases-content.{en,fr,de,it,pt,nl}.consultor.ts`
- **Síntoma**: Valores `category: 'Conceptos de Negocio' | 'Creatividad Culinaria' | 'Herramientas y Utilities' | 'Contenidos y RRSS' | 'Gastro Profile Pro'` sin traducir.
- **Decisión necesaria del user**: ¿son marcas internas (como "Cocina Creativa") que se mantienen ES en todos los idiomas, o se traducen?
- **Recomendación**: mantener ES porque son **clasificaciones internas del catálogo de agentes IA del módulo Apps** (mismo patrón que `apps[].name`).

#### BUG-4 · Hub no emite hreflang custom; SEOHead genera URLs erróneas
- **Archivos**: `ConsultoriaGastroProHub.tsx:184` + `SEOHead.tsx:81-92`
- **Síntoma**: Hub pasa canonical correcto pero NO pasa `disableAutoHreflang`. SEOHead genera `<link hreflang="en" href="/en/usos/consultoria-gastro-pro">` (URL 404 — la real es `/en/use-cases/gastro-consultancy-pro`).
- **Impacto**: ALTO. Hreflang inválidos en hub contradicen el sitemap (que sí está bien). GSC reportará errores "alternate page is not canonical".
- **Fix**:
  1. Añadir `disableAutoHreflang` a `<SEOHead>` en línea 184.
  2. Añadir bloque `<Helmet>` con loop sobre los 7 idiomas usando los `segments` correctos (igual que `UseCasePage.tsx:252-260`).

#### BUG-5 · Meta titles >60 chars en TODOS los spokes (7 idiomas)
- **Archivos**: `use-cases-content.*.consultor.ts` campo `seo.title`
- **Longitudes actuales**:
  - ES: 78–98 chars
  - EN: 75–95
  - FR: 83–103
  - DE: 78–99
  - IT: 77–96
  - PT: 80–98
  - NL: 81–106
- **Síntoma**: Google trunca a ~580px (≈55-60 chars). Se pierde sufijo " | AI Chef Pro" y a veces keyword secundario.
- **Fix**: Reescribir cada `seo.title` a ≤60 chars manteniendo el nombre del agente al inicio.

#### BUG-6 · Meta descriptions >160 chars en TODOS los spokes
- **Archivos**: `use-cases-content.*.consultor.ts` campo `seo.description`
- **Longitudes actuales**: 168–249 chars (Google muestra ~155-160).
- **Síntoma**: CTAs invisibles ("Empieza gratis" se trunca) → CTR menor.
- **Fix**: Reescribir cada `seo.description` a ≤155 chars. Patrón: `<benefit principal> + <2-3 keywords secundarias del SERP> + <CTA corto>`.

#### BUG-7 · Comentarios de archivo con "Consultoría" en EN/FR/IT/NL
- **Archivos**: `use-cases-content.{en,fr,it,nl}.consultor.ts:1`
- **Impacto**: NULO en SEO (comentario no se renderiza). Cosmético.
- **Fix opcional**: cambiar a "Gastro Consultancy Pro" / "Conseil Gastro Pro" / etc.

### BUGS MEDIOS

#### MED-1 · `apps[].name` en EN traducidos a marcas inexistentes en la plataforma
- **Archivo**: `use-cases-content.en.consultor.ts`
- **Síntoma**: ES usa nombres reales (Cocina Creativa, Mermas GenCal, ID Alérgenos, Gerente de Restaurante Pro). EN los traduce a "Creative Kitchen", "Yield Calculator", "Allergen ID", "Restaurant Manager Pro" — **estos no existen en la plataforma `apps.ts`**.
- **Impacto**: Brand fragmentation + `LinkifyText` no crea enlaces internos a app real.
- **Decisión user requerida**: ¿mantenemos nombres ES en todos los idiomas (recomendado, igual que "Pack APPCC", "Kit Escandallos Pro")? Si sí, revertir las 11 traducciones en EN.

#### MED-2 · `Service.areaServed` incorrecta para FR/DE/IT/PT/NL
- **Archivo**: `UseCasePage.tsx:204` — solo bifurca `en` vs default (ES/EU/LATAM).
- **Fix**: Mapear por idioma:
```ts
const AREA_SERVED = {
  es: ['ES','EU','LATAM'],
  en: ['US','UK','CA','AU','EU'],
  fr: ['FR','BE','CH','LU','CA-QC','EU'],
  de: ['DE','AT','CH','EU'],
  it: ['IT','CH','SM','EU'],
  pt: ['PT','BR','AO','MZ','EU'],
  nl: ['NL','BE','SR','EU'],
};
```

#### MED-3 · `Service.offers.offerCount=4` y `highPrice=95` desactualizados
- **Archivo**: `UseCasePage.tsx:212-219`
- **Fix**: cambiar a `offerCount: '5', lowPrice: '0', highPrice: '950'` (Premium Plus Anual €950).

#### MED-4 · Sitemap: hubs no-ES con `<url>` compacto sin hreflang reciprocal
- **Archivo**: `public/sitemap.xml`
- **Fix**: Expandir los 6 bloques compactos hub i18n con `<xhtml:link>` para los 7 alternates + x-default.

#### MED-5 · `Service.audience.audienceType` usa el badge en lugar de un sustantivo canónico
- Impacto bajo, improvement opportunity.

#### MED-6 · OG hub image única para 7 idiomas (texto ES "Consultoría Gastro Pro")
- Impacto bajo en ranking (afecta CTR en redes).
- Fix opcional: generar 6 variantes localizadas (~$0.40 Nano Banana 2).

### LOW

- **LOW-1**: `seoKeywords` del hub ES tiene 26 keywords (recortar a 8-10).
- **LOW-2**: Precargar `galleryImages[0]` con `rel=preload` (LCP candidate).
- **LOW-3**: `CollectionPage.hasPart` sin `provider`.
- **LOW-4**: Sufijo gallery alt en ES para 5 idiomas (consecuencia del BUG-2).
- **LOW-5**: `LinkifyText` no procesa `apps[].name`.

---

## 🌍 KEYWORDS SERP por idioma (para integrar en SUBTITLE / H2 / META / FAQ / BODY — NO en H1)

### EN — Mercado US/UK/global

Cada spoke necesita en subtítulo / H2 / meta description / FAQs los **head terms del SERP real** (que no son los nombres del agente):

| Spoke (H1 inmutable) | Keywords SERP para SUBTITLE/H2/META/FAQ |
|---|---|
| Gastronomy Consultant | restaurant consultant, F&B consultant, restaurant consulting services, food and beverage consultant |
| Chef Consultant Pro | chef consultant, consulting chef, chef consultant fees, chef consulting services |
| Gelato & Ice Cream Consultant Pro | ice cream consultant, gelato consultant, how to open a gelato shop, ice cream business consulting |
| Chocolatier Consultant Pro | chocolate consultant, bean to bar consulting, chocolate business consultant |
| Pastry Chef Consultant Pro | pastry consultant, dessert menu development, pastry consulting services |
| Pizza Chef Consultant Pro | pizza consultant, pizzeria consultant, how to open a pizza shop, pizza business consultant |
| Barista Consultant Pro | coffee shop consultant, barista consulting, specialty coffee consulting |
| Sommelier Consultant Pro | wine consultant, hire a sommelier, wine list consultant, restaurant wine program |
| Bartender Consultant Pro | bar consultant, cocktail consultant, bar program development, cocktail menu development |
| Baker Consultant Pro | bakery consultant, bread consultant, artisan bread consultant, bakery startup consulting |

### FR — Mercado FR/BE/CH/QC

Términos canónicos en SUBTITLE/H2/META/FAQ (mantener H1 oficial intacto):

- "Consultant en restauration" (head term, >>> "consultant gastronomique")
- "CHR" (no HORECA en FR puro)
- "Métiers de bouche" (paraguas semántico)
- "MOF" (Meilleur Ouvrier de France) — autoridad cultural
- "Artisan" (sello de calidad)
- "Café de spécialité" (cluster barista — secundario)
- Para bartender: añadir también "mixologue/barman" en body (mantener "Bartender" en H1)
- Para bakery: "boulangerie artisanale", "boulanger-pâtissier"
- Para pizza: "pizzeria artisanale", "AVPN"

### DE — Mercado DE/AT/CH-DE

- "Gastronomieberatung" (head term sin guión en body — H1 mantiene guión por brand)
- "BAFA-Förderung" (subvención 50-70% para KMU — hook único)
- Tarifas referencia: "150-200€/h, 1.200-1.600€/Tag" (DEHOGA)
- "IHK-geprüft" (autoridad)
- "Konzeptentwicklung", "Businessplan", "Standortanalyse"
- Para chef: "Küchencoaching", "Küchenchef" en body (H1 mantiene "Chef-Berater Pro")
- Para barista: "Specialty Coffee", "Kaffeebar" en body
- Para bakery: "Bäckerei eröffnen", "Backstube Konzept"

### IT — Mercado IT

- "Consulenza ristorazione" (>>> "consulenza gastronomica") en body
- **Doble sigla "AI/IA"** en meta + body (Italia es híbrida — caso único)
- "Aprire [attività]" cluster secundario (×5-10 volumen)
- "Maestro Gelatiere / Maestro Cioccolatiere / Maestro Pasticcere / Maestro Pizzaiolo" — figuras premium
- "AVPN" (pizza napoletana), "AIS" (sommelier), "Pastry Chef Consultant" (premium)
- Normativa: "ATECO", "SAB", "HACCP", "SCIA al SUAP"
- **Pasticc*e*re** (grafía DOP) en body — pero H1 mantiene "Pasticciere Consulente Pro" oficial

### PT — Mercados PT + BR (estratégico crítico)

- Estrategia **pt-BR-primary + pt-PT-secondary** en body (BR es 20× más grande online)
- Doble grafía en body: "gastronômica/gastronómica", "cafeteria/cafetaria"
- Bloques duales por spoke: "Para Brasil" (SEBRAE, Abrasel, ANVISA, R$) + "Para Portugal" (ASAE, Turismo de Portugal, €)
- Mencionar variantes léxicas: "sorveteiro (BR) / mestre gelateiro (PT)", "confeiteiro (BR) / pasteleiro (PT)", "padaria & pastelaria (PT)"
- Para sommelier: H2 "(também escanção em Portugal)"

### NL — Mercados NL + BE-Flandes

- **"horeca"** = palabra-matriz obligatoria 4× por página (H1/H2/meta/CTA)
- Autoridades a citar: NBOV (panaderos), SVH (Pizzaiolo certificado), KHN, KVK, NVWA, HACCP
- Cluster "starten / openen / overnemen" — 60-70% del volumen B2B
- Diferenciación: NL (KVK, KHN, NVWA) vs BE (Syntra, Horeca Vlaanderen, FAVV)
- Brand wordmark "Gastro Advies Pro" en H1 oficial — meta title pattern: `[Agente Pro] — AI Horeca Adviseur | aichef.pro`

### ES — Mercados ES + LATAM

- H1 = nombre del agente oficial. H2 SEO con keyword canónico hispano.
- Spoke sommelier: **H2 obligatorio "Sommelier o sumiller: el mismo consultor con IA"** (España normativa usa sumiller)
- Para todos: **bloque "Cuánto cobra"** universal (PAA #1 en español)
- Para chef: variante MX "chef ejecutivo" en body
- Para pastelero: "obrador" (ES) / "taller de pastelería" (LATAM) en body
- Para panadero: cross-sell con Guía Panadería con Obrador €65 LIVE
- Para bartender: cross-sell con Kit Escandallos €12 LIVE
- Variante MX "consultor restaurantero" en hub
- Fase 2 (medio plazo): valorar spoke dedicado MX

---

## 📋 PLAN DE IMPLEMENTACIÓN (propuesta — esperar OK del user)

### Fase A — Bugs CRÍTICOS i18n (1 commit grande)
1. BUG-1: traducir UI strings hub a fr/de/it/pt/nl
2. BUG-2: traducir UI strings UseCasePage a fr/de/it/pt/nl
3. BUG-4: hub emite hreflang custom + `disableAutoHreflang`
4. Build verify

### Fase B — Bugs CRÍTICOS meta (1 commit por idioma o uno grande)
5. BUG-5: reescribir 70 `seo.title` a ≤60 chars (10 spokes × 7 idiomas)
6. BUG-6: reescribir 70 `seo.description` a ≤155 chars con CTA
7. BUG-7 (opcional): limpiar comentarios "Consultoría" en archivos EN/FR/IT/NL

### Fase C — Enrichment (1 commit)
8. Integrar keywords SERP por idioma en `heroSubtitle` + `featuresTitle` + FAQs (PAA verbatim) — NO tocar H1
9. MED-2: AREA_SERVED por idioma
10. MED-3: actualizar Service.offers a 5 SKUs / €950
11. MED-4: expandir sitemap hubs no-ES con hreflang reciprocal

### Fase D — Decisiones pendientes
- BUG-3 (categories ES en todos los idiomas): ¿mantener brand o traducir?
- MED-1 (apps[].name EN traducidos a marcas inexistentes): ¿revertir a nombres ES?
- MED-6 (OG hub image localizada): ¿generar 6 variantes ~$0.40?
- ES sommelier "sumiller" H2: confirmar

### Fase E — LOW (opcional, futuro)
- Recortar keywords del hub ES
- LinkifyText procesa app.name
- Preload galleryImages[0]
- CollectionPage.hasPart provider
- AI Overviews / Perplexity optimization (TL;DR snippets, bullets en personalizationBody, internal linking 9 siblings)

---

## Estado de commits LIVE

```
HEAD: ca6471e (backup docs)
ca6471e  docs(seo-audit): backup findings consolidated (6/7 agents back)
f3ecb8d  feat(seo): sitemap +66 URLs i18n (592→658)
93553ca  feat(og-meta): social previews FR/DE/IT/PT/NL (55 entries)
b3128c6  feat(i18n): 6 idiomas adicionales con contenido nativo
553d1e4  feat(seo): sitemap +11 URLs ES
4d4a0f9  fix(security): no API key hardcoded
312e5e6  feat: 8 OG sufijo -consultor
e035e08  feat: 71 imgs Nano Banana 2
755edc0  feat(consultoria): hub + 10 landings ES
```

**Los nombres oficiales de los 10 agentes están INTACTOS en código LIVE.** Ningún H1 fue modificado.

## Restricción térmica

CPU pico hoy: 65.31°C (LÍMITE). Estrategia: Edits ligeros, sin Bash pesado, sin Playwright. Esperar OK del user antes de implementar Fase A-C.
