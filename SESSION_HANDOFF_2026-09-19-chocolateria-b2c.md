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

Documentos (tras `7f77895`): **guía 110 páginas** (59.049 palabras, 51 tablas) · **business plan 19** · **bonus «12 decisiones» 34**. Los tres con `documentos.py` en verde, 0 llamadas a bridge (regla del 4-sep: productos digitales sin bridge).

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

## 3. EN CURSO al escribir esto — ronda 2 de verificación (tope de 2 rondas, regla del 12-sep)

Workflow `verificar-fixer-guia-chocolateria` (3 verificadores por lente + lector de regresiones + segundo voto, opus). Después: aplicar lo que FALTE de verdad → reensamblar → copiar los 5 documentos a `dl/` → sustituir tokens `__PAGINAS__`/`__PAGINAS_BONUS__` (medidos) → gates offline (`paginas-gate`, `nombre-gate`, `censo-entregables --fail`, `gate-no-latinos`, `postprocess-transversal --dry-run`, `gate-flujo-postpago --offline`) → commit + push → gates sobre el preview → PR lista para John.

Residuo pendiente de la ortografía (4 celdas, no bloquea): cabecera «m2» en dos tablas (el NOMBRE de hoja «Zonas y m2» no se puede tocar), y las unidades «grados C»/«m3» en la tabla de preguntas al fabricante.

## 4. Lo que queda para John (bloqueante para el LIVE)

1. **Payment Link de Stripe** (65 €, `tax_code txcd_10000000`, `tax_behavior exclusive`, automatic tax on, invoice creation on, redirect a `https://aichef.pro/guia-chocolateria-obrador-access?session_id={CHECKOUT_SESSION_ID}`) y la env **`VITE_STRIPE_PAYMENT_LINK_GUIA_CHOCOLATERIA_OBRADOR`** en Netlify, scope **builds**, todos los contextos. Después: `sync-payment-links.py` → commit → merge de la PR #84 → gates LIVE. Descripción del producto en Stripe (prosa, ~260 caracteres, sin «verificado contra el BOE»): *«Para quien va a abrir una chocolatería o bombonería con obrador en España: 20 capítulos en PDF y DOCX editable, 9 herramientas Excel con fórmulas vivas —capacidad y clima del obrador, CAPEX, sensibilidad al precio del cacao, escandallo, vida útil, campañas, plan financiero, licencias y proveedores—, un business plan modelo relleno y 12 decisiones de apertura resueltas. Pago único, acceso de por vida.»*
2. **D53**: ¿regenerar el Kit de Tareas Chocolatería a 2.1 (≈0,15 M; ocho alérgenos en las tres celdas de declaración y humedad 50-60 %)? Si sí: kit 24-oct y guía 29-oct; si no, guía 24-oct.
3. Compra de prueba tras el LIVE (o `aichef.pro/admin/generar-acceso`). El pago cripto real de prueba sigue pendiente desde el 6-sep.
4. Colaterales detectados, para una sesión impar: la FAQ de «cuánto cuesta abrir un cocktail bar» (`it`/`pt` `.consultor.ts:958`) publica el mismo rango inventado de 80.000-250.000 € (séptima vertical, fuera del censo de D27); el alias inglés «Financial Plan Kit» no enlaza en 48 menciones EN; `guia-panaderia-obrador` se llama distinto en catálogo y hub (homologación pendiente); `guia-restaurante-peruano` sigue de banner en `chocolateria-artesanal-e-ia…` (un hueco).
