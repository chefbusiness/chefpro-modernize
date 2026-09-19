# SESSION HANDOFF — 19-sep-2026 (sesión PAR, Claude Code en el Mac): correos de Pastelería programados · «Cómo Montar una Chocolatería Boutique & Atelier» B2+C

> Sesión Claude Code · firma `Via: Claude Code`. Rama de trabajo **`feat/guia-chocolateria-obrador`** (PR **#84**, borrador, deploy preview `https://deploy-preview-84--aichefpro.netlify.app`). Producción sigue en `main` = `083263b` + nada de esta sesión: **no se ha mergeado nada**.
> Térmica: `istats` leído antes de cada paso pesado; CPU entre 42 y 58 °C toda la sesión; `photolibraryd` (95 %) congelado al arrancar y añadido al filtro del vigilante; `mediaanalysisd` congelado por el agente de imágenes. **Reanudar ambos al cerrar** (`pkill -CONT photolibraryd mediaanalysisd`).

## 1. Resend — dos correos programados (cola de 5 días)

`GET /broadcasts` antes de programar: el último programado era Food Truck 2.2 (9-oct). Prueba enviada a John y luego programado:

| Correo | `scheduled_at` | Id |
|---|---|---|
| Lanzamiento «Cómo Montar una Pastelería» | **2026-10-14 08:00 UTC** | `476bf7fa-8cf1-441d-a49a-ce70c4fb080b` |
| Actualización Kit de Tareas Pastelería 2.1 | **2026-10-19 08:00 UTC** | `ec87d4a8-5ea6-4fec-a9d1-eb48d64c6c13` |

Siguiente hueco: **24-oct** para la Chocolatería (**29-oct si John aprueba el kit de chocolatería 2.1, D53**, que iría delante). Programable desde el **24-sep**. Plantilla ya escrita: `scripts/productos-digitales/emails/broadcast-guia-chocolateria-lanzamiento-es.html` (con tokens de páginas hasta el cierre).

DataForSEO vuelve a tener saldo (John): «taquería mexicana» 210/mes ES.

## 2. Chocolatería — qué se hizo (B2 + C), commit a commit

| Commit | Qué |
|---|---|
| `7172a3c` | `watchdog-termico.sh` congela también `photolibraryd` |
| `1a2c242` | calendario: correos y arranque de B2+C |
| `376e1c4` | **Capa de producto del 49** (54 ficheros): réplica del molde `8457077` en 3 lotes opus (landing+correo · SPA+functions+zona app · hub+buscador+roles+34 FAQ de consultoría ×7 idiomas) + `fase8x-sustituir-banner.py` GENÉRICO (config JSON por producto) con 4 banners + 2 enlaces + 7 imágenes + revisor adversarial (11 hallazgos, 9 aplicados) |
| `df45163` | **45 bloques redactados** (Sonnet, `check_bloque` 45/45, 60.467 palabras) + documentos ensamblados en verde (punto de control ANTES de la refutación) |
| `7f77895` | **Refutación ronda 1** (63 únicos, 60 aplicados) + **ortografía restaurada en origen** (C16: `datos_ejemplo.py` en ASCII → 1.380 literales, 9 libros regenerados, 0 cambios numéricos) |
| `2a921b9` | informe de la ronda 2 |
| `bd1e3de` | **Documentos FINALES en `dl/`**, páginas medidas, fixer final de la ronda 2 |

Documentos (tras `bd1e3de`): **guía 111 páginas** (59.334 palabras, 51 tablas) · **business plan 19** · **bonus «12 decisiones» 34**. Los tres con `documentos.py` en verde, 0 llamadas a bridge (regla del 4-sep: productos digitales sin bridge).

### 2.1 Trampas nuevas de esta sesión (ya documentadas donde tocan)

- **Las «reparaciones» automáticas de `documentos.py` eran erróneas las 4** («no sé si podré»→«poder», «reposo de levado»→«llevado», «Selmi Cento EX»→«Ciento», «Elche»→«Leche»). El build sale verde y sólo lo lista `_meta.erratas_reparadas`. Regla: leerlas una a una tras cada ensamblado y meter las correctas en `erratas_permitidas` del guion. Los 44 «erratas» del gate `sin_erratas` fueron todos falsos positivos (imperativos con tilde, nombres propios).
- **El gate de fechas exige la FUENTE entre paréntesis junto a la cifra** (`RX_CITA`), no basta con nombrarla en la frase («El informe IPMARK… cuenta» no vale; «(IPMARK, 2026)» sí). Y el EUDR citado con «de 31 de mayo de 2023» dispara el gate porque «Reglamento» queda a más de 60 caracteres: se cita sin la fecha de firma.
- **`datos_ejemplo.py` en ASCII**: los constructores del 12-sep lo escribieron sin tildes y ningún gate lo mide (censo, no-latinos y WinAnsi miran otra cosa). Comprobación barata para el siguiente producto: `python3 -c "print(sum(open('datos_ejemplo.py').read().count(c) for c in 'áéíóúñ'))"` y compararlo con el hermano. Al acentuar aparecieron **dos bugs latentes**: un `startswith('Amortizacion')` que dejaba caer la amortización de los gastos fijos al cambiar el dato (lo cazó `comprobar()` por la banda de margen) y un regex de plazos que sólo aceptaba «dias».
- Las citas `fichero.xlsx!Hoja` en celdas de TEXTO llegan al PDF por las tablas del guion y tumban `citas_legibles`; se corrigen en las constantes de `datos_ejemplo.py` (`F_KIT_*`), no en el .md.
- `fase6-gate.py <url>` toma la URL como **BASE del sitio**, no como página; contra un preview da 3-4 fallos de sitemap/hreflang que son artefactos del preview (hreflang 8 = producción 8).
- `fase8i`/`fase8x`: `elegir_ancla()` sólo miraba `<div>` y los banners son `<aside>`; en un post sin `<h2>` habría partido un banner. Arreglado en `fase8x` (`CONTENEDORES`), más `ancla_n` por post y los gates `esperado`/`prohibidos`.
- Colaterales arreglados: coma doble en el import de `src/pages/ProductosDigitales.tsx` (PR #83, SyntaxError latente: la SPA ya no se construye) y el U+300B «》» vivo en producción en `libreria-de-prompts-para-chocolatero-consultor-pro-ai`.

### 2.2 Verificado sobre el deploy preview (PR #84)

`miselup-gate.py --base` 98/98 · sección cripto del `gate-flujo-postpago.py` con su botón (los 13 fallos son los 5 documentos aún no copiados a `dl/` y el Payment Link) · JSON-LD `Product` 65,00 sin ratings + `FAQPage` 12 + breadcrumb · canonical y OG · hub «49 · 22» con la tarjeta nueva · dashboard sin botón duplicado de WhatsApp · 7 imágenes 200.

## 3. Ronda 2 CERRADA y documentos FINALES en `dl/` (commit `bd1e3de`, 15:45)

- **Ronda 2** (`verificar-fixer-guia-chocolateria`: 3 verificadores por lente + lector de regresiones + 17 segundos votos, 21 agentes opus, 2,9 M tokens): 46/63 resueltos, 17 residuos confirmados, **3 regresiones del fixer de la ronda 1** (título «publicados» frente a prosa «verificados», remisión al propio capítulo, «tres veces» del EUDR a medias) y 18 contradicciones nuevas. Informe: `auditorias/guia-chocolateria-docs-verificacion-r2-2026-09-19.json`.
- **Fixer final** (1 opus en serie, 49 min): todo aplicado; 9 libros regenerados con **0 cambios numéricos** (234 celdas de texto + columna «Precio tal como se publica» para el rango de los moldes), gate 9/9, md5 build = dl; `documentos.py` verde en los tres, 0 bridge, 0 reparaciones automáticas.
- **Entregables finales**: guía **111 páginas** (59.334 palabras, 51 tablas) · business plan **19** · bonus **34**; 14 ficheros en `astro-site/public/dl/guia-chocolateria-obrador/` trackeados. Tokens de páginas sustituidos por 111/34 en ficha, config, functions y correo.
- **Gates offline, todos en verde**: `paginas-gate` 5/5 · `nombre-gate` OK · `censo-entregables --fail` 0 defectos (14) · `gate-no-latinos` 0 · `postprocess-transversal --dry-run` OK · `fase5 --check` 147/147 · `sync-product-prices --check` 49 · `gate-flujo-postpago --offline`: **sólo falta el Payment Link**.
- **Residuos deliberados** (no bloquean; motivo en el informe del fixer final): el semáforo de tres estados de «¿ES RESTRINGIDO?» (mueve totales de dos libros: los libros 8 y 9 declaran la limitación en nota y la prosa lo advierte en los tres sitios) · los destinatarios sembrados difieren entre el libro 8 (3) y el 9 (4, todos «No lo sé») — alinearlos toca datos de dos libros y una frase del bonus: **decisión de John** · el estilo «ap. 6.a)» en ~6 celdas de `datos_ejemplo.py` (sistémico y anterior a esta sesión) · «°C» con espacio normal y fino mezclados (cosmético) · «m2» sólo en el NOMBRE de hoja «Zonas y m2».

### 3.1 Preview final (PR #84, tras `bd1e3de`)

`gate-flujo-postpago.py --base <preview> --only guia-chocolateria-obrador`: **14/14 descargas servidas con el tamaño de disco**, landing 200 con «111 páginas» y «34 páginas», `-access` y `-library` 200, sección cripto con botón; **los 3 fallos restantes son el Payment Link** (landing `#comprar`, `payment-links.ts`, env). `photolibraryd` y `mediaanalysisd` reanudados al cerrar (16:05).

## 4. Lo que queda para John (bloqueante para el LIVE) — datos de Stripe entregados en el chat a las 15:15

1. **Payment Link de Stripe** (65 €, `tax_code txcd_10000000`, `tax_behavior exclusive`, automatic tax on, invoice creation on, redirect a `https://aichef.pro/guia-chocolateria-obrador-access?session_id={CHECKOUT_SESSION_ID}`) y la env **`VITE_STRIPE_PAYMENT_LINK_GUIA_CHOCOLATERIA_OBRADOR`** en Netlify, scope **builds**, todos los contextos. Después: `sync-payment-links.py` → commit → merge de la PR #84 → gates LIVE. Descripción del producto en Stripe (prosa, **254 caracteres**, medida; la de la SPEC pasaba de 400): *«Para abrir una chocolatería o bombonería con obrador en España: 20 capítulos en PDF y DOCX, 9 Excel con fórmulas vivas (obrador, CAPEX, cacao, escandallo, campañas, plan financiero, licencias), business plan relleno y 12 decisiones resueltas. Pago único.»* Imagen: `https://aichef.pro/og-guia-chocolateria-obrador.jpg`. Recoger email: sí.
2. **D53**: ¿regenerar el Kit de Tareas Chocolatería a 2.1 (≈0,15 M; ocho alérgenos en las tres celdas de declaración y humedad 50-60 %)? Si sí: kit 24-oct y guía 29-oct; si no, guía 24-oct.
3. Compra de prueba tras el LIVE (o `aichef.pro/admin/generar-acceso`). El pago cripto real de prueba sigue pendiente desde el 6-sep.
4. Colaterales detectados, para una sesión impar: la FAQ de «cuánto cuesta abrir un cocktail bar» (`it`/`pt` `.consultor.ts:958`) publica el mismo rango inventado de 80.000-250.000 € (séptima vertical, fuera del censo de D27); el alias inglés «Financial Plan Kit» no enlaza en 48 menciones EN; `guia-panaderia-obrador` se llama distinto en catálogo y hub (homologación pendiente); `guia-restaurante-peruano` sigue de banner en `chocolateria-artesanal-e-ia…` (un hueco).
