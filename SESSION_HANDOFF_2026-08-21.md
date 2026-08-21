# Handoff — 2026-08-21 (sesión VPS 19-20 ago; sustituye a SESSION_HANDOFF_2026-08-19.md como handoff de pista principal)

> Estado al cierre del 2026-08-21 (mañana). Esta sesión NO tocó el blog: fue la
> conexión de la web con las plataformas PT/NL recién lanzadas, el barrido
> «nada gratis» y el fix del mega-menú del header. **La pista de blog PT sigue
> exactamente donde la dejó el handoff del 19**: tanda 1 (posts 1-2) lista para
> escribir. La pista de productos digitales tiene su propio handoff
> (`SESSION_HANDOFF_2026-08-20-productos-digitales.md`, de John).

## Hecho en esta sesión (todo commiteado, desplegado y verificado EN VIVO)

1. **Los árboles /pt/ y /nl/ venden ya en SUS plataformas** (`ptapp.aichef.pro`
   / `nlapp.aichef.pro`, lanzadas por John en Pickaxe el 19-ago). El helper
   `appUrl()` era «fuente única» de nombre: 14 componentes .astro y el
   `getAppUrl` de la SPA conservaban copias del mapa sin pt/nl y mandaban esos
   árboles a la app ES. Erradicadas las 14 y consolidación REAL: **el mapa vive
   en `src/lib/app-urls.ts`** (la SPA no puede importar de astro-site; al revés
   sí — patrón de los locales JSON). Verificado: 0 fugas en los 6 árboles
   no-ES, deep-links de categoría 200. Commit `c3cadd5`. Log: §8 2026-08-19-H.
   Dato vivo: **los 7 subdominios de plataforma están localizados**; el path
   del redirect NO es prueba (todos menos ES/IT van a `/guest`).
2. **«Nada gratis» re-afirmado por John** (Miembro = 10 €/mes, 10.000
   créditos): censo `gratis|free|gratuit` → producción LIMPIA en 7 idiomas;
   borrada la clave MUERTA `free_trial` de los 7 locales (la mina que resucitó
   el BlogCTA el 17-ago). Commit `e6173fc`. Gratis deliberado que queda: free
   tools, micro-sesión mentoría (Calendly) y tier Guest de Pickaxe.
3. **Mega-menú «Agentes IA» arreglado** (cazado por John en /it): los 9 ítems
   (+4 móvil) caían en 3 destinos genéricos desde `970a8e1` (mar-2026). Ahora
   `sectionHref(id)` = ancla CON ruta (`/#seccion` ES, `/{lang}#seccion`
   resto) + `scroll-mt-28` en las 4 secciones (sin él aterrizaban tapadas por
   el sticky de ~90 px — lo cazó el refutador). Commit `c9db422`. Log: §8
   2026-08-20-A. **Tres decisiones abiertas para John**: (a) el hub de free
   tools perdió sus 5 enlaces de header (le quedan footer ×7 + AnnouncementBar
   en fr/de/it/pt/nl — en ES/EN pierde prominencia); (b) los 3 ítems de cada
   columna comparten ancla — hay destino fino por app si se quiere; (c) en ES
   las anclas pasan por `/` y las intercepta `lang-redirect` (= logo).
4. **De John en paralelo (Mac)**: gate de productos con el punto ciego del
   eBook cerrado (`1b531de`) + handoff de productos (`01cc2b8`).

## Siguiente sesión (orden acordado: idiomas → contenidos → SEO)

- **PT posts 1-2 (haccp + alergénios)**: TODO preparado y sin caducar. La
  receta completa —roadmap, research fijado en `.work/post{1,2}-pt-*/`,
  pipeline, asserts PT-PT, CTAs y cola 3-14— está en
  **`SESSION_HANDOFF_2026-08-19.md` §Tanda 1 y §Cola**, que sigue siendo la
  referencia operativa del frente PT (este handoff no la duplica). Esperado
  tras tanda 1: build 1.304.
- **NL después de PT 14/14** (infra COPY.nl + segmentos `categorie`/`pagina`
  ANTES del primer post; ojo dialecto limburgués del piloto fase10).
- **SEO**: maduración GSC de IT (17-ago) / FR (18-ago) / DE (19-ago) — releer
  hacia el 8-15 sept por página+query (trampa de la URL legacy). Las free
  tools SSR (119 URLs) también pendientes de mirar arranque en GSC.

## Pendientes de John (aparcados por orden suya del 19-ago — recordar al cerrar hitos)

- Replicar el anuncio de los 3 modelos open source en itapp/frapp/deapp/ptapp/nlapp.
- Checkouts de ptapp/nlapp con el plan de 10 € (las plataformas ya están
  lanzadas y localizadas; los checkouts son SUYOS — no verificarlos).
- Conversión COMPRA en Google Ads.
- **Cutover de enblog** (`CUTOVER_ENBLOG_PENDIENTE.md`): alias en Netlify +
  DNS, con la trampa de las A records de Hostinger.
- Las 3 decisiones del header del punto 3 de arriba.

## Gotchas nuevos de esta sesión

- **`grep -c` cuenta LÍNEAS, no ocurrencias** — en HTML minificado (todo en
  4-5 líneas) infla falsos negativos/positivos. Mordió DOS veces en un día
  (vigilante de deploy y verificación de scroll-mt). Ocurrencias =
  `grep -o patrón | wc -l`. Y un vigilante de deploy debe esperar la señal
  que DISTINGUE la versión nueva (aquí «0 hrefs a la app ES»), no una que ya
  daba la vieja (el Footer ya emitía ptapp antes del fix).
- `netlify` CLI está autenticada en el VPS (`netlify api listSiteDeploys`,
  site prod `ee5802cf-…`): sirve para confirmar deploy `ready` sin adivinar
  desde el HTML.
- El apex `/` responde 302 por la edge function `lang-redirect` (decisión F6
  viva; a un curl desde Hetzner lo manda a `/de`). No es un bug.
