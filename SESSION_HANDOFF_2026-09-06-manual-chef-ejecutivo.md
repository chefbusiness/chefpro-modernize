# Handoff — Manual del Chef Ejecutivo (producto nuevo nº 3) · sesión Claude Code 2026-09-06 (Mac)

> Tercer producto nuevo del ciclo alternado, segundo de la línea «Manuales operativos». John dedicó la sesión al
> producto y fijó tres cosas: **precio 65 €** (rompe la paridad con el Manager, 55 €, a propósito), la corrección del
> anisakis en producto vendido va a la **siguiente sesión impar**, y la cola de Resend la decide el orquestador. Y una
> petición personal: **nace con la puerta «Pagar con cripto» activada** aunque el pago de prueba del piloto siga
> pendiente (~8-sep). Método idéntico al del Manual del Manager (SPEC → xlsx → guion → redactores → documentos.py),
> con dos novedades: verificador legal contra fuentes primarias ANTES del guion (D23) y una pasada de
> **desduplicación por capítulo** que cazó un defecto del pipeline (§3).

## 1. Estado al cierre — ver §5 para lo que quedó LIVE y lo que espera a John

| Pieza | Estado |
|---|---|
| Research (6 lentes + síntesis + refutación 28 hallazgos) | ✅ `scripts/productos-digitales/auditorias/manual-chef-ejecutivo-*` (2,1 M tokens, 72 min) |
| SPEC v1.0 (30 decisiones) | ✅ `scripts/productos-digitales/manual-chef-ejecutivo-SPEC.md` (65 €, 7 libros, 20 caps, cripto D22, Resend D28) |
| JSON de research | ✅ `guias-v2-research-sector.json` 162 → **225** ids (CE-01..40 normativa de cocina, CS-01..23 sector) + 13 correcciones del verificador legal + `cifra ""→null` |
| Verificación legal contra fuentes primarias (D23) | ✅ `auditorias/manual-chef-ejecutivo-verificacion-legal-2026-09-06.md/.json` — 26 ids confirmados letra a letra, 5 correcciones bloqueantes (plus de formación de Madrid lo PAGA la empresa; EPI según evaluación de riesgos; alcance del anisakis; ventilación 50 m³/h «casos restantes»; la modificación ALEH 2026 reescribe nombres sin alterar funciones) + 15 hallazgos nuevos (Cataluña art. 41 ropa 15,39 €/mes; manutención 59,21 € = Barcelona; doble comida testigo del art. 30.9…) |
| 7 xlsx | ✅ `astro-site/public/dl/manual-chef-ejecutivo/` (2.581 fórmulas, 0 sin caché, 68 notas «Verificado el 06-09-2026 · norma · URL», censo 0 defectos); refutación de 17 hallazgos aplicada; generadores en `manual-chef-ejecutivo/gen_*.py` + `datos_ejemplo.py` (importa «La Encina» del Manager) + `build/mapa-*.json` |
| Guion | ✅ `guias-v2_0/guion_manual_chef_ejecutivo.py` (20 caps + 12 situaciones, 281 referencias a celda, 54 tablas, 0 rotas) + `manual-chef-ejecutivo/verificar_guion.py` + tabla de frontera `auditorias/manual-chef-ejecutivo-frontera-guion-2026-09-06.md` (⚠️ el conflicto cocina-sala del Manager es su **cap. 16**, no el 18) |
| Documentos | ✅ manual **96 páginas** (52.203 palabras, 42 tablas) · bonus **34 páginas** (15.762 palabras, 12 tablas); 56 bloques por 56 redactores Sonnet (7,7 M tokens); refutación de documentos 27 hallazgos aplicados; desduplicación 41 pares → 0; caché espejada en `manual-chef-ejecutivo/build/docs/` |
| Capa de producto | ✅ landing `productos/manuales/manual-chef-ejecutivo.ts` + wrapper, zona app 47, dashboard (2·7·2), 4 functions + config, catálogo 47, hub ×2 (comingSoon retirado), changelog 1.0, linkify, footerLinks ×5, `productIds` de 5 páginas de rol, `product-prices.ts` 47, desplegable admin al día (47) |
| Cripto (D22) | ✅ `GuiaLandingPage.astro` con las 3 puertas (hero integrado, BuyBox hermana, CTA) + nota de devoluciones; `CRYPTO_PRODUCTS=kit-tareas-cafeteria,manual-chef-ejecutivo` en production (scope conservado) |
| Imágenes | ✅ 6 galería + OG (`067e1ae`) |
| Blog | ✅ `fase8h-manual-chef-blog.py`: 4 banners fijados + 13 enlaces contextuales (mise-en-place sin banner: sus 3 están en NUNCA); `blog-lastmod.json` |
| Email | ✅ `emails/broadcast-manual-chef-ejecutivo-lanzamiento-es.html` (96/34 páginas); **programar el lunes 14-sep 08:00 UTC** tras la prueba a John (§5) |
| Resend (D28) | ✅ cola reprogramada: Manager 7-sep · **Chef 14-sep** · bar 19-sep · cafetería 24-sep · tapas 29-sep · panadería 4-oct · **food truck en BORRADOR** «— PROGRAMAR 9-oct» (Resend no admite >30 días) |
| Stripe | ⏳ **John**: producto + Payment Link 65 € → env `VITE_STRIPE_PAYMENT_LINK_MANUAL_CHEF_EJECUTIVO` (scope builds, todos los contextos) → `sync-payment-links.py` → commit + push |

Descripción de Stripe propuesta (271 caracteres, sin BOE): «Para quien ya dirige una cocina: 20 capítulos en PDF y DOCX
editable, 7 herramientas Excel con fórmulas vivas —brigada, producción, ficha técnica, carta y auditoría— y 12 situaciones
resueltas, para que tu cocina salga igual estés tú o no. Pago único, acceso de por vida.»

## 2. Orden de cierre
1. Deploy `ready` del push `b056abc` → `python3 scripts/productos-digitales/gate-flujo-postpago.py --only manual-chef-ejecutivo`
   (landing 200, access/library 200, 11 descargas binarias, sección E cripto: 3 `data-crypto-open` + 1 `<dialog>`) ·
   `robots-gate.py --live` · `fase6-gate.py https://aichef.pro/manual-chef-ejecutivo`.
2. Email: `python3 scripts/productos-digitales/emails/resend-broadcast.py --html scripts/productos-digitales/emails/broadcast-manual-chef-ejecutivo-lanzamiento-es.html --subject "Nuevo: el Manual del Chef Ejecutivo" --name "Lanzamiento Manual del Chef Ejecutivo (ES)" --test john@chefbusiness.co` → revisar → mismo comando con `--scheduled-at 2026-09-14T08:00:00Z`.
3. John: Payment Link (65 €, `tax_behavior exclusive`, redirect a `-access?session_id={CHECKOUT_SESSION_ID}`, automatic_tax, invoice) → env var → `sync-payment-links.py` → commit + push → gate LIVE de nuevo → compra de prueba real.
4. `sitemap-index.xml` a GSC + petición de indexación de `/manual-chef-ejecutivo`.

## 3. Trampas nuevas de esta sesión (para la memoria)
- 🔴 **`documentos.py` entrega a CADA bloque la lista completa de `puntos` del capítulo** (`prompt_bloque`, ~línea 1012) mientras los epígrafes sí se reparten: los 2-3 redactores del mismo capítulo repiten ideas y frases (41 pares con Jaccard ≥ 0,55 en 15 de 20 capítulos). Medidor: `manual-chef-ejecutivo/build/docs/solape.py`. Se resolvió con una pasada de desduplicación (un sonnet por capítulo). **Para el próximo producto: repartir `puntos` por bloque y decir a cada prompt qué escribe otro tramo.** Medir también la Guía Food Cost y el Manual del Manager en una sesión impar.
- **El detector de erratas del pipeline toma por errata palabras correctas** (gradación, estaño, traición, táper, reunió, «monten», «rodar»…): 30 formas añadidas a `_ERRATAS_OK` en dos ensamblados. Mirar el contexto antes de «corregir».
- **El gate de títulos anclados (`tablas_ancladas`) no encuentra un título con raya «—»**: la sanitización WinAnsi del PDF la convierte en «-». Títulos de capítulo sin raya.
- **El detector de fechas exige la cita entre paréntesis a ±250 caracteres también dentro de la prosa de los redactores** (no sólo en el guion): «2025-2028» como rótulo dispara `rotulo_con_anio_pasado`.
- **El fixer de documentos editó dos xlsx de `dl/` a mano** (puntos de control de la ficha de ejemplo, fechas de revisión, G50 de la auditoría). Se portaron al generador y se comprobó celda a celda; y al mover «documentar» de N1/N2 a agosto había dejado los hitos desordenados (probar en septiembre, documentar en agosto): se corrigió la secuencia entera en `CALENDARIO_TEMPORADA` y se regeneró el libro 5. **Regla: los xlsx nunca se tocan a mano; se regenera.**
- **Resend: un broadcast programado no se edita** (403): reprogramar = `GET` (guardar asunto/nombre) → `DELETE` → `POST`. Borré cuatro sin tener el asunto guardado (el `GET` traía caracteres de control y `json.load` estricto reventó) y hubo que reconstruirlos. Y **no admite `scheduled_at` a más de 30 días** (422): borrador con nombre «— PROGRAMAR <fecha>». Memoria `feedback_resend-reprogramar-sin-borrar-a-ciegas`.
- **`mediaanalysisd` de macOS se pone al 77 % de CPU al añadir imágenes nuevas** al repo: `pkill -STOP mediaanalysisd` (reanudar con `-CONT`). El vigilante térmico se paró solo a media sesión: comprobar `pgrep -f watchdog-termico.sh` entre fases.
- **`netlify env:set` sobre una variable existente conserva su scope** si sólo se pasa `--context`: es la forma segura de cambiar `CRYPTO_PRODUCTS` sin perder `builds`+`functions`.

## 4. Presupuesto real (tokens de subagentes)
Research 2,1 M · B1 (JSON + legal + datos + 3 constructores + refutador + fixer + re-verificación) 3,2 M · capa de producto 0,32 M · guion 0,58 M · 56 redactores 7,7 M · refutación docs + fixer 0,77 M · desduplicación 2,2 M · sync xlsx 0,18 M ≈ **17 M**. Muy por encima del techo del calendario, con la sesión dedicada por John (presupuesto suspendido hasta el 7-sep).

## 5. Seguimientos (no bloquean)
- 🔴 **Anisakis y RD 3484/2000 en producto vendido** (`kit-tareas-sushi-bar/03`, `kit-tareas-marisqueria/03`, `kit-inventario/04`): primera tarea de la próxima sesión impar (calendario §0-ter, punto 0).
- Food truck 2.2: programar el borrador para el **9-oct** a partir del 9-sep.
- Las 20 páginas de rol no enlazan a ningún producto de más de 45 € (decisión de John: añadir Manager y Guía Food Cost).
- Cupón cruzado Manager ↔ Chef; `emailBody` del Manager sin enlace al Chef (no se tocó un transaccional vivo).
- 5-10 minutos de voz de John sobre los cinco dolores sin cita (ficha ignorada, mermas, producción, pase, Sanidad) para la v1.1.
- `documentos.py`: repartir `puntos` por bloque (§3) y medir solape en los dos productos anteriores.
- Piezas de captación del blog con `bridge.py`: organigrama/brigada de cocina (320+880), funciones del jefe de cocina (110), ficha técnica de cocina (90).
- PDF de la AESAN (botulismo) y guía de cocina al vacío de Cataluña: citar el original cuando vuelvan a estar accesibles.

Via: Claude Code
