# Handoff — Guía «Cómo Montar una Pastelería» (producto nuevo nº 4) · sesión Claude Code 2026-09-09/10 (Mac)

> Producto nuevo nº 4 del ciclo alternado, primero de la línea «Cómo Montar» que entrega lo que promete. John eligió el
> producto a las 23:50 del 9-sep, fijó a las 02:30 **65 €, 8 libros de Excel, dos sesiones y arreglar el libro 13 del
> kit de pastelería**, y a las 02:35 cambió el ritmo: «me voy a dormir, avanza con todo hasta completar el producto y
> déjame los datos de Stripe». Todo lo de abajo está commiteado en `main` LOCAL; **no se ha hecho push de la capa de
> producto ni de los entregables** porque sin Payment Link la landing saldría con el botón de compra roto.

## ⚠️ CIERRE DE URGENCIA (06:55 del 10-sep): PUSH HECHO (`5de0125`), John apaga el Mac para una reunión

- **Payment Link creado por John** (`https://buy.stripe.com/7sY00c5Sk64e1MPejH6oo1r`), env var puesta (scope builds, todos
  los contextos), `CRYPTO_PRODUCTS` = `kit-tareas-cafeteria,manual-chef-ejecutivo,guia-pasteleria-obrador`,
  `payment-links.ts` regenerado (48). **Push a `main` a las 06:52 → Netlify desplegando.** NO se ha podido correr ningún
  gate LIVE ni enviar el sitemap a GSC (el Mac se apaga): **primera tarea de la próxima sesión** →
  `gate-flujo-postpago.py --only guia-pasteleria-obrador` (landing con `buy.stripe.com`, 13 descargas binarias, sección E
  cripto: 3 `data-crypto-open` + 1 `<dialog>`), `robots-gate.py --live`, `whatsapp-gate.py`, `fase6-gate.py`, sitemap a GSC.
- 🔴 **Los PDF/DOCX en producción son la versión 1 (antes del fixer):** llevan los **11 hallazgos altos** de
  `auditorias/guia-pasteleria-docs-refutacion-2026-09-10.md` (dos referencias de celda desplazadas → «veinte semanas» donde
  son 9; «fondo de maniobra 15.562 €» que es el fijo mensual; punto de equilibrio invertido en 3 sitios; bebida
  reutilizable «ya exigible» cuando es 1-ene-2027; Reyes > enero; una tabla con «4,0 %» donde va 4 °C por el regex de
  porcentajes; las tres vías del huevo sin explicar). **El fixer (opus) estaba a mitad al apagar**: `git status` mostrará
  sus ediciones SIN commitear (8 xlsx regenerados en `dl/` y `build/`, JSON de research, y quizá generadores/txt/guion).
  **Próxima sesión: NO descartar ese árbol a ciegas** — leer `git diff --stat`, pasar `gate_libros.py`, `verificar_guion.py`
  y `censo-entregables.py --only guia-pasteleria-obrador --fail`; si está en verde, terminar los pasos 4-7 del encargo del
  fixer (prosa, reensamblado, gates, páginas) y desplegar la v1.0.1 de los documentos; si no, `git checkout -- .` y relanzar
  el fixer desde el JSON de la refutación. Hasta entonces, **no anunciar el producto** (el correo del 14-oct sigue sin crear).
- Pendientes de Resend (borradores, ambos a más de 30 días): lanzamiento de la guía (14-oct, HTML en `emails/`) y Kit de
  Tareas Pastelería 2.1 (19-oct). Compra de prueba real de John tras el gate LIVE.

## 0. Lo que John tiene que hacer por la mañana (5 minutos) — HECHO a las 06:45 (Payment Link)

1. **Crear el producto y el Payment Link en Stripe** con estos datos:

| Campo | Valor |
|---|---|
| Nombre del producto | **Cómo Montar una Pastelería** |
| Precio | **65,00 €** · pago único · `tax_behavior: exclusive` · `automatic_tax: on` · `tax_code: txcd_10000000` · `invoice_creation: on` |
| Descripción (prosa, ~260 caracteres, sin viñetas, sin «BOE») | Para quien va a abrir una pastelería en España: 20 capítulos en PDF y DOCX editable, 8 herramientas Excel con fórmulas vivas —capacidad de obrador, CAPEX, campañas, escandallo, licencias y personal—, un business plan modelo relleno y 12 decisiones de apertura resueltas. Pago único, acceso de por vida. |
| Imagen del producto (opcional) | `https://aichef.pro/og-guia-pasteleria-obrador.jpg` (estará en producción tras el push) |
| Redirección tras el pago | `https://aichef.pro/guia-pasteleria-obrador-access?session_id={CHECKOUT_SESSION_ID}` |
| Recoger email | sí (lo usa `verify-purchase` para el magic link) |

2. **Pegar la URL `https://buy.stripe.com/…` en el chat.** Claude hace el resto, en este orden: env var
   `VITE_STRIPE_PAYMENT_LINK_GUIA_PASTELERIA_OBRADOR` en Netlify (scope builds, todos los contextos) →
   `sync-payment-links.py` (48) → `CRYPTO_PRODUCTS` += `guia-pasteleria-obrador` (scope builds+functions) → push →
   deploy → gates LIVE (`gate-flujo-postpago.py --only guia-pasteleria-obrador`, `robots-gate.py --live`,
   `whatsapp-gate.py`, `fase6-gate.py https://aichef.pro/guia-pasteleria-obrador`) → sitemap a GSC → borradores de
   Resend (lanzamiento 14-oct y kit 2.1 19-oct; los dos a más de 30 días: se programan a partir del 14-sep / 19-sep).
3. **Compra de prueba real** cuando esté LIVE (o `aichef.pro/admin/generar-acceso`).

## 1. Estado al cierre de la noche (06:15) — todo en `main` local, sin push

| Pieza | Estado |
|---|---|
| Research (6 lentes + síntesis 1.003 líneas + refutación 8/16/8) | ✅ `auditorias/guia-pasteleria-research-*`, `guia-pasteleria-RESEARCH-2026-09-09.md`, `…-REFUTACION-…` (2,06 M tokens) |
| SPEC v1.0 (36 decisiones, 32/32 hallazgos resueltos) | ✅ `scripts/productos-digitales/guia-pasteleria-SPEC.md` |
| Verificación legal contra el BOE (72 fichas: 36 confirmadas, 14 corregidas, 12 nuevas; gate de literalidad 0 fallos) | ✅ `auditorias/guia-pasteleria-verificacion-legal-2026-09-10.md/.json` (+ `-EXCLUIDOS.json` con las 9 sin URL) |
| JSON de research | ✅ 225 → **411** entradas (63 `PA-*` + 123 `PS-*`), gate de recuento en verde |
| Juego de datos «La Clara» | ✅ `guia-pasteleria/datos_ejemplo.py` (3.229 líneas; 90 m², 5 personas/3,5 jornadas, 30 refs con vía legal del huevo, 3 escandallos copiados exactos del Kit de Escandallos, `nota_legal()` 25/25) |
| 8 libros de Excel | ✅ `astro-site/public/dl/guia-pasteleria-obrador/*.xlsx` (4.556 fórmulas, 0 sin caché, 0 verdes vacías, 0 funciones prohibidas; refutación 23 hallazgos → 19 fixes en generadores; `guia-pasteleria/gate_libros.py` 8/8 verde) |
| Guion | ✅ `guias-v2_0/guion_guia_pasteleria_obrador.py` (21 caps + 6 secciones de business plan + 12 decisiones; 315 referencias a celda, 64 tablas, 439 puntos por epígrafe con `puntos_por_epigrafe`, 125 ids) + `guia-pasteleria/verificar_guion.py` en verde |
| Redacción | ✅ 47 bloques por 47 subagentes Sonnet en 16 min (4,9 M tokens), `check_bloque.py` 47/47; caché en `guia-pasteleria/build/docs/txt/` |
| Documentos | ✅ guía **104 páginas** (54.850 palabras, 43 tablas) · bonus **38** (16.594, 12 tablas) · business plan **19** (7.707, 9 tablas); todos los gates de `documentos.py` en verde; PDF + DOCX en `dl/` |
| Refutación de documentos | ⏳ en curso al cerrar este handoff (opus, tres lentes); sus fixes van a los `.txt` → reensamblar → recopiar → censo |
| Capa de producto | ✅ landing `productos/guias/guia-pasteleria-obrador.ts` (sin tachado, sin testimonios, 10 piezas en bonus, 12 FAQ), wrapper con `whatsapp={false}` y cripto, zona app 48 (generada, `--check` byte a byte), dashboard 2·8·3, 4 functions con las 13 claves, catálogo y `product-prices.ts` (48), hub ×2 (tarjeta «Nuevo», `comingSoon` solo Chocolatería, kit «15 plantillas»), alias del buscador, linkify, footerLinks ×4, roles (3 + `guia-panaderia-obrador` en panadero), admin (48), changelog 1.0, `nombre-gate.py` en verde |
| Páginas en la landing | ✅ tokens sustituidos por las MEDIDAS (104 / 38); `paginas-gate.py --only` OK y detecta tokens sin sustituir |
| Imágenes | ✅ 6 galería + OG (Nano Banana 2, $0,60, revisadas a ojo) |
| Blog | ✅ `fase8i-guia-pasteleria-blog.py --aplicar`: 3 posts con banner + 8 enlaces contextuales («la guía Cómo Montar una Pastelería») + miswiring kit-tareas-pasteleria → kit-tareas-panaderia en 2 posts de panadería; `blog-lastmod.json` regenerado |
| Email de lanzamiento | ✅ `emails/broadcast-guia-pasteleria-lanzamiento-es.html` con 104/38 páginas. **No creado en Resend** (slot 14-oct, a más de 30 días) |
| Gates offline | ✅ censo 0 defectos (13 ficheros), no-latinos 0, Bug #2 `MISSING: 0`, `fase5 --check` 144/144, `gate-flujo-postpago --offline` sin fallos estructurales (solo el Payment Link) |
| Stripe | ⏳ John (§0) |

### Colaterales cerrados en la misma noche
- **Kit de Tareas Pastelería 2.1** (producto vendido): vidas útiles y vitrina ajustadas al RD 1021/2022 en los libros 01, 02, 08 y 13 (24 h para lo elaborado con huevo por la vía 70 °C/2 s o con ovoproducto; ≤4 °C en relleno). Corregido en los GENERADORES con reproducción previa celda a celda; changelog 2.1; correo `emails/broadcast-kit-tareas-pasteleria-v2.1-es.html` **sin programar** (slot 19-oct). Commits `938d61f` y el de ampliación. ⚠️ El barrido de los otros 18 kits y del Pack APPCC salió limpio.
- **`documentos.py`: reparto de `puntos` por tramo** (`repartir_puntos()`, `puntos_por_epigrafe`, sección «lo que escriben los otros tramos»), `solape.py` generalizado como gate, test de regresión byte a byte (`3c1444d`). El guion de pastelería es el primero que lo usa.
- **`paginas-gate.py`** (landing ↔ PDF/DOCX): hoy fallan las 8 guías «Cómo Montar» antiguas (119 vs 10 en la gastronómica); pasan Food Cost, los dos manuales y la pastelería.
- Correo **Food Truck 2.2 programado** para el 9-oct (aprobado por John).
- Página de rol `panadero` vendía `kit-tareas-pasteleria` (ES y EN): corregido.

## 2. Trampas nuevas de esta sesión (para la memoria)
- **El art. 9.3 del RD 1021/2022 se lee al revés en el research:** las 24 h aplican a lo elaborado por la vía **70 °C/2 s** y con **ovoproducto** (no estable a ambiente), no a lo que «no alcanza» esa temperatura. El agente del kit lo cazó leyendo el PDF; con la lectura del encargo la crema pastelera se habría quedado fuera.
- **El `grep` sobre `sharedStrings.xml` no encuentra «°C»**: el XML escapa `°` como `&#176;`; decodificar entidades antes de buscar (un barrido dio cero y era falso).
- **El post-proceso v2.0 del kit reescribe título y versión** (`--skip` no basta) y el libro 08 lo EXIGE (recalcula rangos del contador): mapa de versión por fichero en el post-proceso.
- **`inject_cache`/`data_only`: una fórmula que devuelve `""` se lee como `None`**, igual que una sin caché. `gate_libros.py` distingue con pycel; el censo de la casa no se confunde (0 sin caché en los 8).
- **pycel: evaluar la salida ANTES de `set_value()` sobre la entrada**, o la demo lee el caché viejo y pasa por casualidad.
- **`motor.dv_lista()` crea la DV con lista de comas** (prohibida por la SPEC) y `motor.NOTA_DESPROTEGER` lleva una flecha U+2192 no WinAnsi: los constructores de pastelería usan `_comun_pasteleria.py` con `dv_rango()`.
- **`construir_tabla`: un `%` en la SEGUNDA columna reformatea la fila entera** (`es_fila_porcentual()` mira `fila[:2]`).
- **`documentos.py --min-palabras-cap` (default 900) PISA el `min_palabras_cap` del guion**: pasar 1300 explícito.
- **El detector de fechas exige la cita a ±250 caracteres** también cuando la fuente está al final del párrafo; y un año en una columna de tabla (1967, fundación de Sosa) dispara el gate: quitar la columna en el guion.
- **La ampliación de la 2.1 a los libros 01/02/08 fue decisión de John** (preguntado), no del orquestador: un dictado = solo ese cambio.

## 3. Presupuesto real (tokens de subagentes)
Research 2,06 M · verificación legal 0,50 M · ids PS 0,30 M · SPEC 0,38 M · datos_ejemplo 0,42 M · 8 libros (4 constructores + refutador + fixer) 2,37 M · guion 0,60 M · 47 redactores 4,90 M · capa de producto 0,71 M · imágenes 0,13 M · blog 0,34 M · kit 2.1 0,54 M · documentos.py fix 0,15 M · paginas-gate 0,21 M · refutación de documentos (en curso) ≈ 0,5 M → **≈ 14,1 M** (dentro de la estimación de la SPEC; John suspendió el techo para esta noche).

## 4. Seguimientos (no bloquean)
- `nombre-gate.py` sin `--only` sale en rojo en 43 productos antiguos (`schema.productName` es un título SEO largo): sesión impar.
- «9 checklists» del hub en las otras 5 verticales de kits (sesión impar).
- Business plan: el pipeline lo emite también en PDF (`business-plan-modelo-pasteleria.pdf`), no incluido en las 13 claves (la SPEC dice DOCX); si se quiere, añadir la clave y el fichero.
- Las 7 guías «Cómo Montar» antiguas siguen sin entregar lo prometido (cola v2.0 S4-S9 del calendario); el copy de pastelería no las enlaza (D19).
- Cupón cruzado con el Kit de Tareas Pastelería; garantía de devolución en portada (decisión de John).
- 5-10 minutos de voz de John para la v1.1 (precios, mermas de vitrina, encargos, madrugón).

Via: Claude Code
