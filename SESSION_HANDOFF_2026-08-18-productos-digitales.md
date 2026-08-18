# Handoff — 2026-08-18 · Productos digitales AICP: flujo post-pago + Kit Pastelería v2.0 (EN CURSO)

> Sesión en el Mac (Fable, ultracode). Se cortó por límite de uso a mitad de la construcción de la v2.0.
> **Estado del repo al cortar:** `main` = `907066e` (LIVE, deploy ready). Trabajo en curso en la rama
> **`wip/kit-pasteleria-v2`** (pusheada). ⚠️ NO mergear a main hasta que existan los 3 .xlsx nuevos
> (10/11/12): el código de la rama ya los referencia (get-download-urls, dashboard, mega pack) y darían 404.

## 1. Lo que ya está LIVE en main (commit `907066e`, deploy ready 11:01 UTC)

- **Diagnóstico del flujo post-pago tras Astro (44 productos, 634 entregables): VERDE.** Gate LIVE:
  landings con Stripe 44/44 (sin `#comprar`), gates `-access` e islands `-library` hidratan 44/44,
  `/dl` sirve 634/634 con Content-Length == disco, verify-purchase/resend-access/get-download-urls
  responden, STRIPE_SECRET_KEY/JWT_SECRET/RESEND_API_KEY presentes en el site (`ee5802cf-…`).
  Verificado además en el Chrome de Windows: gate renderiza (error controlado con sesión falsa) y el
  dashboard de pastelería renderiza (con JWT falso → get-download-urls 403 → «Disponible pronto», que es
  el comportamiento esperado). El 404 de los 524 entregables (19-jul → 8-ago) lo había arreglado el VPS
  en `7e050c5`; el cliente que pagó el 16-ago compró DESPUÉS de ese fix.
- **Bug real corregido**: kit-tareas-cafeteria / pizzeria / hamburgueseria — la 2ª tarjeta del dashboard
  (`barista` / `horno` / `plancha-grill`) no tenía clave en get-download-urls (`partidas`) → «Disponible
  pronto» para siempre. Ahora clave función = TEMPLATES[].key.
- `resend-access`: email normalizado (trim+lower) + consulta a Stripe con variante normalizada y literal.
- **Gate reutilizable**: `scripts/productos-digitales/gate-flujo-postpago.py` (`--offline`, `--only`,
  `--json`); HTTP vía curl (el python3 del sistema no tiene CA bundle). 0 fallos offline tras el fix.

## 2. Trabajo en curso en `wip/kit-pasteleria-v2` (rama)

Ficheros de la rama (todo lo de abajo está commiteado allí):
- `scripts/productos-digitales/kit-tareas-pasteleria-v2-SPEC.md` — **la especificación** (diagnóstico
  v1, correcciones transversales, 3 ficheros nuevos 10/11/12, integración, verificación).
- `scripts/productos-digitales/kit-tareas-pasteleria-v2-AUDIT-V1.json` — **96 hallazgos** de la
  auditoría adversarial v1 (3 lentes opus: obrador 36 · técnica Excel 28 · coherencia/cliente 32).
  ⚠️ LEER ANTES DE CONSTRUIR — hay hallazgos que CAMBIAN la SPEC (ver §3).
- `scripts/productos-digitales/kit-tareas-pasteleria-v2-workflow.js` — script Workflow listo:
  fase Construcción (3 opus en paralelo: generador base 01–09+BONUS, generador extras 10–12, landing
  data) → verificación determinista (sonnet) → auditoría v2 (3 lentes opus). Lanzar con
  `Workflow({scriptPath: ...})` **tras actualizar la SPEC con §3**.
- `scripts/productos-digitales/inject_cache.py` — copiado de CB y **arreglado**: openpyxl 3.1.x escribe
  el cache vacío como `<v />` (autocerrado); la regex de CB solo aceptaba `<v></v>` → inyectaba 0 en
  silencio. Probado: 09-caja 56/56, 01 2/2, `data_only` con valores.
- `scripts/productos-digitales/kit-tareas-pasteleria-v2-EMAIL-CLIENTE.md` — borrador del email al
  cliente (John lo envía cuando la v2.0 esté LIVE; regenerar enlace en /admin/generar-acceso).
- `scripts/productos-digitales/kit-tareas-pasteleria-v1-dump.txt` — volcado en texto de los 11 xlsx v1.
- Código ya adaptado (pendiente de los ficheros): `src/pages/KitTareasPasteleriaDashboard.tsx` (3
  tarjetas nuevas con badge «NUEVO v2.0», `<ProductVersionBadge/>`, `<ProductChangelog/>`,
  `<SaasCrossSellBanners/>` solo Miselup+Timlup; tsc --noEmit OK), `src/components/shared/ProductChangelog.tsx`,
  `src/components/shared/SaasCrossSellBanners.tsx`, `src/data/productos-changelog.ts` (entrada v2.0),
  `src/pages/MegaPackTareasDashboard.tsx` (+3 templates pastelería), `astro-site/src/pages/mega-pack-tareas.astro`
  (pastelería 11→14, total derivado), `netlify/functions/get-download-urls.ts` (+3 claves kit + mega),
  `verify-purchase.ts` / `resend-access.ts` (email «12 checklists + 2 bonus (v2.0)»),
  `src/data/productos-digitales-config.ts` (sync; ese fichero NO está cableado a nada),
  `astro-site/src/data/productos/tareas/types.ts` (+`updateNote?`) y `KitTareasLandingPage.astro` (lo pinta).
- **Pendiente**: generar los 14 xlsx (generador base + extras), landing data
  (`astro-site/src/data/productos/tareas/kit-tareas-pasteleria.ts`), auditoría v2, deploy, verificación LIVE.

## 3. Hallazgos de la auditoría v1 que OBLIGAN a retocar la SPEC antes de construir (resumen)

**Lente obrador (contenido)** — errores objetivos en los ficheros v1 que la SPEC daba por «intactos»:
- **Bug funcional en 8/11 ficheros**: la ☐ visible está en la columna A pero el contador
  `COUNTIF(F…,"✓")` cuenta la columna F «Hecha» (con validación «✓,—» pero sin instrucción) → el
  cliente marca la ☐ y ve «0 de N». Fix v2: quitar la ☐ de A (nº correlativo) y marcar en «✓ Completada»
  con validación, o contar la A; y explicarlo en Instrucciones.
- 02 Partidas: entremets «congelar 4 h» a las 09:30 y «desmoldar congelados/glasear» a las 10:00 (imposible;
  es D+1). 06 Eventos: el roscón se vende la TARDE DEL 5 (hornear madrugada 4→5, no 5→6); torrijas desde
  Cuaresma; y otros ajustes de calendario tradicional español (leer L1-06…L1-1x). Horas/responsables a repasar.
- **Fichero 12 (alérgenos): riesgo legal si se entrega PRE-MARCADO como definitivo** → entregar como
  BORRADOR (● en gris «propuesta — verificar»), columna «Verificado con ficha técnica del proveedor
  (fecha) + firma» y fórmula «NO PUBLICAR» mientras esté vacía, columna «Proveedor / nº ficha técnica»,
  banner rojo en Instrucciones. **Cartel**: la información debe estar disponible POR ESCRITO (RD 126/2015)
  → frase obligatoria «Información de alérgenos disponible por escrito — solicítela a nuestro personal»;
  la contaminación cruzada es complemento, no sustituto; generar además una «Carta de Alérgenos»
  imprimible producto × 14 derivada de la matriz.
**Lente técnica Excel** — validar rangos COUNTIF (cubren filas de sección), validaciones que no cubren
todas las filas, ausencia de page setup, cache; pycel soporta SUMIF/COUNTIF/IFERROR/IF (comprobado por la lente).
**Lente coherencia/cliente** — además del §0 de la SPEC: JSON-LD `aggregateRating 4.9/8` + 3 reviews sin
sistema real de reseñas (8 ≠ 10 testimonios ≠ 3 reviews) → decisión de John (quitar aggregateRating/reviews
del schema o montar recogida real); testimonios con marcas reales (Meliá, Europastry, Hofmann) → ficticios;
**ancla de precio permanente** «€39 tachado / −69 % / precio de lanzamiento, sube pronto» desde marzo →
decisión de John (riesgo de práctica comercial engañosa; propuesta: quitar el tachado o hacerlo real).

## 4. Cómo retomar (orden)
1. `git checkout wip/kit-pasteleria-v2` (o cherry-pick a main cuando esté completo).
2. Leer AUDIT-V1.json completo (96 hallazgos) → actualizar SPEC §1.2/§1.3 con §3 de este handoff.
3. Lanzar `kit-tareas-pasteleria-v2-workflow.js` (Workflow con scriptPath) → revisar auditoría v2 → fixes.
4. `python3 scripts/productos-digitales/gate-flujo-postpago.py --offline` (0 fallos) → merge a main → push
   → deploy ready → gate LIVE completo → descargar los 14 de prod y abrir en `data_only` → dashboard en el
   Chrome de Windows → enviar email al cliente (borrador en la rama).
5. Decisiones que necesitan a John: JSON-LD de reseñas; ancla de precio €39/−69 %; webhook de Stripe y
   validación de producto contra la sesión pagada en verify-purchase (bugs CB §2, no arreglados: no hay
   price IDs en el código y las env VITE_* solo tienen scope builds).
6. Barrido site-wide de la bio «29 años / 15 años» (143 ficheros en astro-site/src + src) → bio anclada
   («desde 2010», «en cocina desde los 17 años»); tarea aparte con sonnet.
