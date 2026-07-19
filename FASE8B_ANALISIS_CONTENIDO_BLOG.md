# 📊 FASE 8B — Análisis de utilidad del contenido de blog.aichef.pro (2026-07-19)

> Análisis previo a la migración blog.aichef.pro → aichef.pro/blog (multiidioma nativo).
> Fuentes: censo REST API live (408 posts), GSC (blog + enblog, 90d), auditoría de clusters
> 2026-06-15 (`~/aichef-blog/.work/audit-2026-06-15/`), plan maestro del blog
> (`~/aichef-blog/PLAN_MAESTRO_RELANZAMIENTO_SEO_2026.md`).
> Censo crudo de esta sesión: scratchpad `blog-census/` (posts.jsonl, categories.json, pages.jsonl)
> — regenerable con la REST API pública.

## 1. Inventario live (censo 2026-07-19)

**408 posts + 7 páginas** (hub librería de prompts id 234, about, contact, privacidad…).

| Categoría | Posts | Bucket de utilidad |
|---|---:|---|
| IA en Gastronomía | 141 | Comercial/informacional IA (money clusters) |
| Tutoriales | 116 | Mayoría recetas nacionales LATAM/mundo + técnica |
| AI Chef Pro | 104 | Producto + solape pSEO |
| Glosario y Léxico Científico Culinario (+AI) | 72+6 | Autoridad temática / GEO |
| Guias IA Locales | 50 | ⚠️ pSEO programático REPUBLICADO |
| Librería de Prompts | 34 | ⭐ El activo nº1 (24 librerías de agente + hub + posts de prompts) |
| Recetario Pro AI | 17 | Consumo |

(multi-categoría: suma 540 > 408)

**La producción sigue VIVA desde la VM Abacus** (el repo local `~/aichef-blog` está desfasado):
- Librerías de prompts: **24/74 publicadas** (tracking local decía 9/74). Últimas: 2026-07-05 (Chef Privado, Chef Ejecutivo, Gerente de Restaurante).
- Los **50 pSEO** (`ia-fidelizacion-para-…-en-madrid` etc.) despublicados el 2026-05-29 fueron **republicados en goteo** (modified 2026-06-28, dates escalonadas hasta 2026-07-18).
- 358 posts con modified en junio 2026 (retrofit masivo del relanzamiento).

## 2. Realidad de tráfico (GSC)

**blog.aichef.pro (28d):** 423 clics · 27.810 impresiones · posición media 26,0 y **cayendo**
(18→31 dentro de la ventana; clics ~25/día a fin de junio → ~8/día a mediados de julio).
España AUSENTE del top-15 países (top: IT, FR, BR, IR, MX, GE…).

**Causa del desplome de julio — GTranslate MUERTO:**
- Suscripción **INACTIVA** → los 6 idiomas "conservados" (en/fr/de/it/pt/nl) sirven **HTTP 402**
  "GTranslate - Error 402: Subscription Inactive".
- Los idiomas cortados (fa/ka/uz…) hacen 301 a la canónica ES (o 404). Correcto.
- El ~95% del tráfico histórico era MT → hoy el blog es **de facto solo español nativo** (~2-3 clics/día ES).

**Activos ES que SÍ funcionan (90d):**
| URL | Clics | Impr | Pos | Lectura |
|---|---:|---:|---:|---|
| /libreria-de-prompts-para-recetario-cocina-creativa-ai/ | 81 | 1.859 | 6,7 | **Página nº1 del blog** → valida Fase 8C |
| /las-7-mejores-apps-de-ia-para-crear-recetas…2025… | 23 | 722 | 7,5 | Refresh 2026 pendiente (slug dice 2025) |
| /como-calcular-el-costo-de-una-receta-facil-con-la-ia/ | 22 | 382 | 21,4 | Money C1, striking distance |
| /ia-para-panaderias/ | 22 | 287 | 5,8 | Vertical "IA para X" — patrón ganador |
| /chef-gpt-espanol/ + /chef-gpt/ | 8+8 | 2.057+1.270 | 7,3 | **CTR 0,4%** → problema de title/snippet, mucho volumen |
| /que-significa-abocar-en-cocina/ | 4 | 1.555 | 13,0 | Glosario con volumen real |
| /15-herramientas… /151-prompts… /25-prompts… | 15+15+7 | — | 5-8 | Cluster prompts/listicles |

**enblog.aichef.pro:** moribundo (12 clics/28d). Aprovechables como semilla EN:
`best-ai-tools-for-chefs-2026` (19 clics, pos 9,4), `menu-engineering-software-complete-guide`
(2.930 impr, pos 13,4), `cloud-kitchen-business-models` (1.353 impr, pos 33). Su pSEO de ciudades
(`ai-recipe-costing-for-bakers-in-sydney`…) = 0 clics, thin, NO migrar.

## 3. Clasificación por utilidad → orden de migración

**TIER A — ORO (migrar PRIMERO, con refresh REGLA CAPITAL) ≈ 110-130 URLs**
- ~106 posts comerciales de los 5 money clusters (C1 costes 16 · C2 IA restaurantes 53 ·
  C3 operaciones 15 · C4 marketing 11 · C5 modelos 11) + verticales mal clasificadas
  (`ia-para-bares/cafeterias/pizzerias/hamburgueserias`, `como-crear-restaurante-desde-cero`…).
- Striking distance de la tabla de arriba (chef-gpt ×2, 7-mejores-apps, calcular-costo…).
- **24 librerías de prompts + hub → FUSIONAR CON FASE 8C** (ver §5), no migrar como posts sueltos.

**TIER B — AUTORIDAD (migrar en bloque, mejora ligera) ≈ 150 URLs**
- Glosario 78 términos → sección /blog/glosario (o /glosario). Perfecto para llms.txt por idioma
  y GEO. Expandir thin <500w (cocina-molecular 382w, esferificación 447w, mise-en-place 300w…) con bridge.py.
- Técnica profesional (prefermentos, beurre noisette, cortes, 23 moles…).

**TIER C — CONSUMO (migrar AL FINAL, tal cual, port mecánico) ≈ 120-140 URLs**
- Recetas nacionales LATAM/mundo (mofongo, chivito, ropa vieja, pabellón…). Su tráfico era MT
  (muerto); en ES-LATAM pueden aportar goteo. CTA suave a Generador de Recetas. NO borrar (curación).
- 23 posts "futuristas" largos (bioacústica, biomimética, acuaponía…) — activos pagados, port tal cual.

**TIER D — NO MIGRAR (decisión John)**
- **50 pSEO "Guias IA Locales" republicados**: canibalizan el pSEO nativo de aichef.pro
  (76 páginas /abrir-restaurante/{ciudad} LIVE e indexadas) y reactivan el patrón "contenido a
  escala" que devaluó el dominio. Recomendación: volver a draft/noindex y **parar el goteo en la VM**.
- 7 listicles escuelas US (fuera de estrategia) → noindex/no migrar.
- 2 pares de duplicados exactos (1249/1268 y 1424/1612) → consolidar + 301 antes de migrar.
- pSEO de enblog (0 clics).

## 4. Tesis estratégica (por qué la migración SUMA)

1. **El subdominio está tocado** (supresión post-cloaking + devaluación por MT a escala; pos 70 en
   España). aichef.pro acaba de estrenar plataforma Astro con SEO server-side, hreflang 7 idiomas
   nativo, sitemap 696 URLs y llms.txt. Migrar el oro con 301 = conservar contenido y link equity
   **sin heredar el estigma del subdominio**.
2. **Encaje perfecto de funnel**: la auditoría SEO de aichef.pro (2026-07-03) dio 90% clics de marca
   — le falta TOFU/MOFU. El blog ES exactamente eso. Interenlazado blog ↔ use cases (51) ↔
   productos (44) ↔ pSEO ciudades (75) ↔ consultoría, imposible entre subdominios separados.
3. **Multiidioma nativo por fases** (decisión John 2026-07-19): ES primero; luego cada idioma con
   keyword research + intención de búsqueda propios (bridge.py --task translation NO es traducción
   literal: adaptación SEO por mercado), URLs /en/blog/…, hreflang real, llms.txt por idioma.
   La vieja amplificación MT (GTranslate) NO se renueva: muerta y era tóxica.

## 5. Cruce con Fase 8C (páginas de agentes)

La página nº1 del blog es una librería de prompts → el formato está validado con datos. 8C planea
~70 páginas de agente en aichef.pro (screenshot, vídeo, explicaciones, **enlaces a su librería de
prompts**, FAQ). Recomendación: **una sola casa por agente en aichef.pro** — página de agente (8C)
con la librería integrada o como sub-página hermana; las 24 librerías del blog se migran DENTRO de
8C con 301 post→página de agente. Evita duplicar el mismo intent en dos URLs.

## 6. Decisiones que necesita John antes de ejecutar 8B

1. **GTranslate 402**: ¿cancelaste tú la suscripción o caducó sola? Recomendación: no renovar
   (la sustituye el multiidioma nativo). Ideal: que los 6 idiomas den 301 a la ES (como fa/ka), no 402.
2. **Goteo pSEO desde la VM**: ¿lo ordenaste tú? Recomendación: pararlo y devolver los 50 a draft.
3. **Librerías → 8C** (una casa por agente): ¿OK a fusionar?
4. **Tier D** (escuelas US, futuristas 0-tráfico): ¿noindex/no migrar OK?
5. **Producción en paralelo**: mientras dure 8B, ¿congelamos publicación de librerías nuevas en el
   blog (para no migrar un blanco móvil) y las seguimos ya en aichef.pro?

## 7. Esqueleto de ejecución propuesto (para cuando haya luz verde)

- **8B.0 Higiene pre-migración** (WP): parar goteo, Tier D a draft/noindex, consolidar duplicados,
  snapshot definitivo del censo (408 → congelar lista canónica).
- **8B.1 Infra Astro**: content collection blog + template post + hub /blog + categorías + RSS +
  sitemap + estrategia 301 del subdominio (DNS blog.aichef.pro → Netlify con _redirects bulk, o
  301 wildcard desde WP/Hostinger — decidir en diseño técnico).
- **8B.2 Tier A ES** con refresh (research+SERP por cluster, bridge.py, imágenes, FAQ, interlinking
  a money pages de aichef.pro). ≈ $35-40 de bridge.py + imágenes.
- **8B.3 Tier B** (glosario como sección + técnica) · **8B.4 Tier C** port mecánico (script REST→MD).
- **8B.5 Cutover blog**: 301 map completo + GSC (sitemap, vigilancia como Fase 7).
- **8B.6+ Idiomas**: EN primero (absorbe los 2-3 activos de enblog + research nativo), después
  FR → DE → IT → PT → NL, cada uno con research/intención/llms.txt propios.
- **8C** se ejecuta idealmente ANTES o EN PARALELO a 8B.2 (las librerías son Tier A).

## Apéndice — gotchas operativas detectadas hoy

- Sitemap RankMath del blog: 344 URLs vs 408 posts live → riesgo de re-congelación (fix conocido:
  Ajustes Sitemap 200→199→200 + guardar). Irrelevante post-migración.
- WP REST API pública y abierta (sin auth para lectura) — el censo es 100% reproducible.
- `~/aichef-blog` (repo local) desfasado vs la realidad del WP: la fuente de verdad del estado del
  blog es la API live, no los tracking .md locales.
