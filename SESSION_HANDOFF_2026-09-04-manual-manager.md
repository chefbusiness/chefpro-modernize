# Handoff — Manual del Manager de Restaurante (producto nuevo nº 2) · sesión Claude Code 2026-09-04 → 05 (Mac)

> Segundo producto nuevo del ciclo alternado. John pidió «hoy de nuevo un producto nuevo» tras la primera venta
> de la Guía Food Cost (66 € con IVA, salida del mailing de las 10:00) y eligió el Manual entre los cuatro
> «próximamente» del hub. Método idéntico al de ayer, con dos mejoras: los textos los escriben 24 redactores
> Sonnet en paralelo (regla «bridge no para productos») y el bloque legal lleva refutador propio con el BOE.

## 1. Estado al cierre (02:10 del 5-sep) — **LIVE COMPLETO**: `gate-flujo-postpago.py --only manual-manager-restaurante` = 0 fallos, 0 avisos (landing con `buy.stripe.com` en sus 4 CTA, access/library 200, 11 descargas binarias con tamaño de disco, webhook armado)

| Pieza | Estado |
|---|---|
| Research (5 lentes + síntesis + refutación) | ✅ `scripts/productos-digitales/auditorias/manual-manager-*` · 32 hallazgos (10 altos) resueltos en la SPEC §1 |
| SPEC v1.0 | ✅ `scripts/productos-digitales/manual-manager-SPEC.md` (22 decisiones) |
| Datos únicos | ✅ `scripts/productos-digitales/manual-manager/datos_ejemplo.py` (La Encina: 12 personas, 6 estaciones, 52 semanas ISO, 4 semanas malas; `checks()` cuadra con la Guía Food Cost al −0,58 %) |
| 7 xlsx | ✅ `astro-site/public/dl/manual-manager-restaurante/` (1.885 fórmulas, 0 prohibidas, 0 constantes, 45 notas legales «Verificado el 04-09-2026»; refutación de 19 hallazgos aplicada) · generadores `manual-manager/gen_*.py` + `mapa-*.json` |
| Guion | ✅ `guias-v2_0/guion_manual_manager_restaurante.py` (20 caps + 12 situaciones; 251 referencias a celda, 0 rotas; 42 tablas; 42 prohibiciones) + `manual-manager/verificar_guion.py` |
| Documentos | ✅ manual **77 páginas** (41.235 palabras, 30 tablas) · bonus **28 páginas** (11.530 palabras, 12 tablas); todos los gates en verde al tercer ensamblado. Texto: 54 bloques por 24 agentes Sonnet (`check_bloque.py` en verde), caché espejada en `manual-manager/build/docs/txt/` |
| Capa de producto | ✅ landing `astro-site/src/data/productos/manuales/manual-manager-restaurante.ts` (carpeta nueva de la línea), wrapper, zona app generada (46), 4 functions + config, catálogo 46, hub con «Nuevo» y `comingSoon` retirado, changelog 1.0, linkify, footerLinks cruzados |
| Prefijo `manual-` | ✅ `robots.txt` con sus 10 reglas; `robots-gate.py --live` verde (1.188 públicas / 92 privadas) |
| Imágenes | ✅ 6 galería + OG (`e884a8d`), revisadas a ojo |
| Blog | ✅ 5 posts con banner fijado + enlace contextual (`fase8g-manual-manager-blog.py`, gate de reversibilidad) + `blog-lastmod.json` |
| Email | ✅ `emails/broadcast-manual-manager-lanzamiento-es.html` · prueba enviada a John (`a97f3d1f…`) · **broadcast `3749f084-138d-459b-a027-f377a6d10d0c` programado para el lunes 2026-09-07 08:00 UTC (10:00 Madrid)**, segmento «AI Chef Pro ES», asunto «Nuevo: el Manual del Manager de Restaurante» (lunes por decisión de John; ayer ya salió un mailing a la misma lista) |
| Stripe | ✅ Payment Link creado por John (`https://buy.stripe.com/3cIcMY1C4csC635ejH6oo1p`) · env `VITE_STRIPE_PAYMENT_LINK_MANUAL_MANAGER` puesta por Claude (scope builds, todos los contextos) · `payment-links.ts` regenerado (46) · redeploy `b2957ab` |
| Hotfix colateral | ✅ la landing de la Guía Food Cost servía DOS botones de WhatsApp (faltaba `whatsapp={false}` en el wrapper); corregido en el mismo push |

Descripción de Stripe (John pidió quitar la verificación contra el BOE del copy corto; se mantiene en landing, email y producto): «Manual del Manager de Restaurante: 20 capítulos (77 páginas) para dirigir el día a día del local —operaciones, equipo, números, servicio y obligaciones legales—, 7 plantillas Excel con fórmulas vivas y un bonus de 12 situaciones reales resueltas paso a paso. Pago único, acceso vitalicio y actualizaciones incluidas.»

## 2. Cierre (hecho en el orden previsto; queda solo el punto 4 para John)

1. John: Payment Link + env var (fila «Stripe» de la tabla). 2. `python3 scripts/productos-digitales/sync-payment-links.py` → `netlify/shared/payment-links.ts` (46) → commit + push → build `ready`.
3. `python3 scripts/productos-digitales/gate-flujo-postpago.py --only manual-manager-restaurante` → 0 fallos (landing con `buy.stripe.com`, access/library 200, 11 descargas binarias con el tamaño de disco).
4. Compra de prueba real (o `aichef.pro/admin/generar-acceso`) — **pendiente de John**; el gate LIVE verifica todo lo demás.
5. Email: `python3 scripts/productos-digitales/emails/resend-broadcast.py --html scripts/productos-digitales/emails/broadcast-manual-manager-lanzamiento-es.html --subject "Verificado contra el BOE (convenio incluido)" --name "Lanzamiento Manual del Manager (ES)" --test john@chefbusiness.co` → revisar → mismo comando con `--scheduled-at <día>T08:00:00Z` (10:00 Madrid).
6. `sitemap-index.xml` reenviado a GSC; pedir indexación de `/manual-manager-restaurante`.

## 3. Trampas nuevas de esta sesión (para la memoria)

- **La calibración de páginas era falsa**: la refutación C4 dijo «330 palabras/página»; la plantilla mete **~530** (Food Cost: 50.265 palabras → 95 págs; manual: 41.235 → 77). El gate de páginas se calibra midiendo, nunca estimando.
- **El guion sobrescribe `erratas_permitidas` al final** (`GUIA['gates']['erratas_permitidas'] = _ERRATAS_OK`): añadir palabras a la tupla del diccionario no sirve; se añaden a `_ERRATAS_OK`. Sin lista blanca, **el reparador automático convierte «cantó» en «cuánto» y «ocurrió» en «ocurrido»** en el texto ensamblado (la caché queda intacta).
- **El detector de fechas exime el año solo si hay una cita entre paréntesis a ±250 caracteres**: una fuente entre comillas «…» o una cita larga fuera de la ventana no cuenta. Se resuelve con un paréntesis corto junto al año.
- **`RX_META` («me piden», «se me pide»…) caza texto legítimo de tablas** («Me piden permisos y no sé qué contestar»). Reformular.
- **`postprocess-transversal.py` en modo real pone «Versión 1.1 · agosto 2026» a fuego** (es de la Fase A): NO aplicarlo a productos nacidos después; solo `--dry-run` como comprobación.
- **`bloque_research` trataba una regla legal con fuente pero sin cifra como «HUECO SIN FUENTE»** y prohibía citarla: parcheado (C2) → «REGLA SIN CIFRA».
- **`fase8f` no vale para un producto nuevo cuyos cross-sell ya están en los posts**: borraría los banners del kit de personal/tareas/APPCC. `fase8g` lleva `NUNCA` propio.
- **`COUNTIF(rango,"< 30 días")` se interpreta como comparación** por empezar en `<`: devolvía 0. Los contadores van sobre la columna numérica.
- **`RANK` y `NETWORKDAYS` no evalúan en pycel** (libro sin caché): `SUMPRODUCT(--(rango>propia))+1` y días naturales.
- **`motor.dv_lista` parte las opciones con coma** («Quejas, reclamaciones y reseñas» → 3 opciones): DV contra rango.
- **DataForSEO en el Mac**: credenciales en `~/chefbusiness-astro/.env` (no chefbusiness-ai) y TLS del python3 3.7 arreglado con `Install Certificates.command`.
- **Bash del tool: `cd` a un directorio en el que ya estás falla** con `&&` y el resto de la cadena no corre; rutas absolutas siempre.

## 4. Presupuesto real (tokens de subagentes)
Research 1,47 M + síntesis 0,39 M + refutación 0,52 M + corrector JSON 0,31 M + datos 0,29 M + constructores 0,94 M + refutador xlsx 0,38 M + fixer 0,44 M + guion 0,40 M + capa de producto 0,29 M + blog 0,17 M + email 0,13 M + imágenes 0,32 M + 24 redactores ≈ 4,4 M ≈ **10,5 M**. Segundo producto nuevo en dos días; muy por encima del techo del calendario, con petición expresa de John.

## 5. Seguimientos (no bloquean)
Los del §9 de la SPEC: «60 % cierra» vivo en 3 sitios del repo · gate de FAQ para las 45 landings · `fase8c-enlaces-vivos.py` a landings · 4 piezas de captación del blog (Verifactu 74.000/mes…) · medir canales con GSC · RD del registro horario → changelog 1.1 · Guía Food Cost v1.1 (`FC-PRIME-01/02` atribuyen a Toast el 60-65 %; `SMI-02` sin acotar) · URL de CaixaBankLab caída (`ECONNREFUSED`) · renombrar la hoja «Plan de Cross-Training» (B3 de la refutación xlsx, no aplicado por la regla de no renombrar hojas).

Via: Claude Code

---

## 6. Segunda mitad de la noche (02:00 → 03:15, John dormido): buscador del hub y fin del «prueba gratis»

### 6.1 Buscador de /productos-digitales — commit `8f8ff75` (workflow de 7 agentes, 38 hallazgos, 37 fixes)

- **Front** (`ProductosDigitalesHubPage.astro`): input entre el subtítulo y los chips; busca por nombre, descripción, features, tags y etiquetas (`data-search` generado en servidor desde `products`/`comingSoon`, normalizado sin acentos); coincidencia por inicio de palabra y AND de términos; sinónimos ES/LATAM en `astro-site/src/lib/sinonimos-buscador.json` (escandallo/costeo, appcc/haccp, manager/gerente/administrador, nómina/planilla, inventario/stock, rentabilidad/margen, food cost/foodcost, food truck…) con **gate de build** que aborta si un grupo no apunta a ningún producto; combina con el chip activo; con búsqueda activa se ven todos los resultados y «Cargar más» se aparca; `/` enfoca, Esc limpia; panel «fuera de categoría» cuando hay resultados pero el chip los tapa; panel «sin resultados» con mini-formulario (detalle + email opcional + honeypot + aviso de privacidad) y WhatsApp con la consulta.
- **Registro** (`netlify/functions/log-search.ts`, POST, `navigator.sendBeacon`): 1,2 s tras dejar de teclear / Enter / blur, ≥ 3 caracteres, dedup por sesión (con prefijos). Guarda en Netlify Blobs (store `search-queries`, un blob por evento) `{q, q_norm, n (global), n_filtrado, coming, tag, lang, path, sin_resultados, detalle, email, origen, country, ts}`. **Sin IP ni user-agent.** Cupo 120 eventos/min. Dependencia nueva: `@netlify/blobs ^10.7.13` en el `package.json` de la RAÍZ (+ lockfile).
- **Informe** (`netlify/functions/search-report.ts`, GET con cabecera `x-admin-password` = `ADMIN_PASSWORD`, comparación en tiempo constante, 5 intentos/min): `?days=30` → total, por_dia, top_queries, sin_resultados (con detalles y emails), por_pais; `?raw=1`; `?purge=1&before=YYYY-MM-DD` borra días completos.
- **Script**: `python3 scripts/productos-digitales/buscador-report.py --days 30` (coge `ADMIN_PASSWORD` de `netlify env:get`, curl) → tabla consulta · veces · resultados medios · ¿existe? · ¿en cola? · países, con ⚠ en lo demandado (≥ 2 veces, 0 resultados) que no está ni en producción ni en la cola del CALENDARIO §3. Doc de operación: `scripts/productos-digitales/BUSCADOR-HUB.md` (incluye los curl de verificación tras el deploy y el gotcha de que Blobs solo existe desplegado).
- **Verificación en producción**: ver §6.3.

### 6.2 Fin del «prueba AI Chef Pro gratis» (John: el plan gratis murió el 15-ago; el de entrada es Miembro, 10 €/mes, 10.000 créditos)

Workflow de 5 censadores + 5 aplicadores + 2 verificadores + corrector sobre 5 zonas: plantillas Astro (GuiaLandingPage y hermanas: Kit, Tareas, Plan, ProPrompts; Pricing.astro), i18n 7 idiomas (`landing*.hero.no_card` «Sin tarjeta de crédito» → «Desde 10 € al mes · Sin permanencia · Acceso inmediato»), datos pSEO/casos de uso (`pseo-cities-content.es.ts`: «Empieza Gratis con AI Chef Pro»), FAQ de librerías de prompts («plan gratuito»), banners `SaasCrossSellBanners.tsx` («Plan gratis sin tarjeta») y ~80 CTA del blog ES/EN/FR/DE. Copy aprobado por idioma en la memoria `feedback_aichef-pro-sin-plan-gratis-desde-10-euros`. Lo que sigue siendo gratis y NO se tocó: las 8 herramientas, la micro-sesión de mentoría, «2 meses gratis» anual, «ChatGPT gratis», otras marcas. Resultado: ver §6.3.

### 6.3 Estado a las 03:00 del 5-sep (John dormido; el Mac se apaga hacia las 03:20)

**Buscador — LIVE y verificado** (commits `8f8ff75` → `9556ac4`): el hub sirve el input con `data-search` en las 49
cards y el bundle incluye el script; `log-search` responde 204 al POST y 405 al GET, y sus logs muestran invocaciones
de ~330 ms sin errores de Blobs; `search-report` responde 401 sin auth. Retoques de John ya desplegados: borde dorado
fijo, placeholder animado en bucle (sin prefijo, ejemplos ≤ 22 caracteres para no cortarse en móvil), lupa a la
derecha, padding derecho reducido, y el botón de WhatsApp del hub a `bottom-6` en móvil (llevaba desde julio el
`bottom-20` de las landings). **No verificado**: la lectura del informe con la contraseña real (es SECRETA en
Netlify y el CLI devuelve un relleno). Primer paso de la próxima sesión: `ADMIN_PASSWORD='…' python3
scripts/productos-digitales/buscador-report.py --days 7` debe listar las 3 búsquedas de prueba («prueba buscador
claude», «prueba blobs uno/dos»); si sale a 0, Blobs no está habilitado en el site → panel de Netlify.

**Fin del «prueba gratis» — EN CURSO, NO en `main`.** Workflow `wf_b211e5b7-323` (script en
`~/.claude/projects/-Users-johnguerrero-chefpro-modernize/b83df144-…/workflows/scripts/fin-plan-gratis-restos-wf_b211e5b7-323.js`):
censo 68 a cambiar / 253 mantener, 84 sustituciones aplicadas por zona, verificadores con 156 restos (el censo del
blog se quedó corto) + 35 defectos, y el corrector final trabajando sobre ~169 ficheros del árbol (plantillas de
landing, Pricing.astro, i18n ×7, pSEO, blog ES/EN/FR/DE, `blog-lastmod.json`). El vigilante térmico lo congeló 11
minutos (umbral mal calibrado; corregido a 66/63 °C). **El árbol de trabajo con esos cambios a medias está en la rama
`wip/manual-manager-2026-09-04` (instantáneas `ea43853`, `ac27f99`; la última prevalece).** Cómo retomar: (1) `git
checkout main && git checkout wip/manual-manager-2026-09-04 -- .` NO (mezclaría el WIP del buscador ya en main):
mejor `git diff main wip/manual-manager-2026-09-04 --stat` y aplicar solo los ficheros del barrido; (2) o relanzar el
workflow con `Workflow({scriptPath, resumeFromRunId: 'wf_b211e5b7-323'})`, que reutiliza censo y aplicadores desde caché y
solo repite verificación + corrector; (3) verificar: 7 JSON de i18n con el mismo conjunto de claves que en `main`,
`grep -rn -i "prueba.\{0,30\}gratis\|plan gratuito\|sin tarjeta\|free trial\|free plan" astro-site/src src/i18n src/data src/components`
= solo lo legítimo (herramientas gratuitas, micro-sesión, 2 meses gratis, ChatGPT gratis, otras marcas), `fase8b-regen-lastmod.py`,
commit, push y `fase6-gate.py` sobre una landing y `/precios`. Copy aprobado por idioma: memoria
`feedback_aichef-pro-sin-plan-gratis-desde-10-euros`.

**Lección de la noche para el toolkit térmico:** un vigilante que congela procesos a 65 °C y reanuda a 60 se bloquea si
el suelo ambiental está en 62; congelar a 66 y reanudar a 63 mantuvo el Mac por debajo de 68 con dos workflows en
paralelo. El script vive en el scratchpad (`watchdog.sh`); merece pasar al repo (`scripts/termica/`).

Via: Claude Code
