# Handoff — sesión maratón del 2026-08-16 → 18 (madrugada)

## Lo entregado, en una línea cada cosa

1. **🏁 BLOG ITALIANO COMPLETO (13/13)** — posts 6-13 publicados en racha de 8
   tandas: `mise-en-place` (18.100/mes), `fondo-bruno`, `salse-madri`,
   `frollatura-carne`, `cucina-molecolare`, `brigata-di-cucina`, `food-cost`,
   `dark-kitchen`. Todos interenlazados por clústeres, agente verificado EN
   VIVO en itapp (método formid/formtitle), FAQ del PAA fresco, gates verdes.
   Primer dato GSC: el pilar `lista-allergeni-alimentari` a **posición 11,4**
   con 176 impresiones en 9 días.
2. **BLOG FRANCÉS ABIERTO Y EN 8/14** — árbol `/fr/blog/` (fase 9 FR, commit
   `4ebb928`) + posts 1-8: el clúster higiene ENTERO interenlazado
   (allergènes ↔ contamination ↔ haccp ↔ PMS ↔ marche ↔ hygiène ↔ nettoyage)
   + `fiche-technique-cuisine` (el hallazgo del research). Cesión de Question
   entre FAQPages ejecutada (post 3 cedió «4 règles» → recibió «CCP»).
3. **FR 9-10 LISTOS EN SECO, SIN COMMITEAR** — ver «Pendiente inmediato».
4. **Anuncio de los 3 modelos open source** (GLM-5.2, DeepSeek V4 Flash, Kimi
   K2.5) — par ES↔EN con hreflang (`modelos-open-source-ai-chef-pro` /
   `open-source-models-ai-chef-pro`) + **mailing enviado por Resend** a las
   audiencias AI Chef Pro ES (~222+) y EN (~492+), broadcasts `cc9e5724…` y
   `c3e0a5da…`, estado «sent» 19:11 UTC. Métricas: resend.com/broadcasts.
5. **Fuga del plan gratis cerrada**: `BlogCTA.astro` decía «Probar AI Chef
   Pro gratis» en 4 idiomas al pie de TODOS los posts (escapó de fase11);
   ahora «Planes para todos los bolsillos, desde 10 €/mes» + leitmotiv
   75+/50+. Commit `be5997c`.
6. **Dos bugs de producción cazados de rebote** al abrir el árbol FR: la UI
   de los posts IT salía en castellano y el CTA mandaba a los italianos a la
   app ES → mapa COPY por idioma + `appUrl(lang)`.
7. **Decisión delegada tomada: el blog DE irá de Sie** (documentada en
   `ROADMAP_BLOG_ALEMAN.md`).

## ⏳ Pendiente inmediato (retomar aquí)

**Tanda 9 FR en seco, bloqueada SOLO por la cuota diaria de Gemini** (se
agotó tras ~50 imágenes; resetea ~09:00 Madrid). En el **working tree SIN
commitear** (adrede: empujarlos publicaría posts con imágenes rotas):

- `astro-site/src/content/blog/fr/menu-engineering.md` (matriz cifrada con
  asserts: umbrales 88 ventas / 9,62 €) y
  `astro-site/src/content/blog/fr/tailles-de-decoupe.md` (tabla de mm).
- `fiche-technique-cuisine.md` con el recíproco → menu-engineering (enlazaría
  a un 404 si se empuja antes que el post).
- `blog-lastmod.json` con las 2 URLs nuevas.

**Al retomar:** generar las 6 imágenes (specs exactas en
`.work/post9-fr-menueng/assemble9fr.py` y `.work/post10-fr-tailles/assemble10fr.py`:
menueng-destacada/carta/sala + tailles-destacada/julienne/regle, sin texto
legible) → optimizar → build DOBLE → commit todo junto → deploy → verificar.
~15 minutos. Después: FR 11 `sauces mères` (agente Cuisine Française —
verificar formid en frapp) y 12 `lacto fermentation` (Fermentus Avec AI+).

## Tareas de John (recordárselas)

- **Replicar los 3 modelos open source en itapp/frapp/deapp/ptapp/nlapp** —
  hoy solo están en app/enapp; el anuncio IT/FR/DE/PT/NL espera esa paridad
  (los prompts e imágenes ya existen; réplica en minutos). Mismo patrón que
  el catálogo pentalingüe pendiente (54/89).
- Herencias previas: checkouts ptapp/nlapp sin plan 10 € · conversión de
  COMPRA en Google Ads · cutover de enblog (`CUTOVER_ENBLOG_PENDIENTE.md`).

## Método consolidado esta sesión (ya en memoria)

- **Bridge tiene TRES modos de fallo medidos**: Markdown pidiendo HTML,
  secciones h2 duplicadas hasta agotar tokens, y truncado a 4.096 clavados.
  Antídotos en los ensambladores: línea anti-MD en prompts, asserts de
  h2-únicos/tablas/figuras, conversor MD→HTML generalizado, y anclas
  ajustadas al output real (bridge retitula).
- **Posts con números**: la aritmética se fija a mano en el prompt y el
  ensamblador la RE-VERIFICA con asserts (food-cost IT, fiche FR, matriz FR).
- **Build DOBLE siempre** (la race del content layer mordió 2 veces) +
  recuento de páginas vs esperado + verificación en dist Y en vivo.
- **Imágenes**: texto visible solo el fijado en el prompt; rechazos típicos
  ya catalogados (idioma equivocado ×4, velas, marcas reales inventadas, la
  imagen contando lo contrario del texto). ~6-8 generaciones por tanda de 6.
- **Resend/Cockpit**: cuenta única del grupo; clave utilizable en
  `chefbusiness-prospecting/.env`; POSTs con `curl` (urllib → Cloudflare
  1010); audiencias y remitentes en la memoria `resend-grupo-y-cockpit`.

## Estado del repo

- `main` == `origin/main` tras este handoff; ~20 commits de la maratón
  (desde `4ebb928` hasta aquí). Log por tanda en el plan maestro §8
  (2026-08-16-B → 2026-08-17-G).
- Working tree: los 4 ficheros de la tanda 9 en seco (arriba) — ÚNICO estado
  no commiteado, intencional.
- Build de producción: 1.276 páginas, verde, verificado en vivo.
