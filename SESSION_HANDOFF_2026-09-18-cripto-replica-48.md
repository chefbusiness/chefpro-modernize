# Handoff — Réplica de la pasarela cripto NOWPayments a los 48 productos (sesión Claude Code, 18→19 sep 2026)

**Encargo de John (18-sep):** «implementar en todos los productos la pasarela de pago NOWPayments como ya la tenemos
en los dos últimos productos… dejar eso hecho antes de avanzar con nuevos productos o mejoras». Regla térmica
reconfirmada ese mismo día: ralentizar a 65 °C, `istats`, nada de Playwright ni builds locales.

## Estado de partida (medido, no supuesto)
- Botón cripto solo en 3 productos (`CRYPTO_PRODUCTS=kit-tareas-cafeteria,manual-chef-ejecutivo,guia-pasteleria-obrador`).
  Plantillas con las tres puertas: `KitTareasLandingPage` y `GuiaLandingPage`. Sin ellas: `KitExcelLandingPage` (5),
  `PlanNegocioLandingPage` (10), `ProPromptsEbookPage` (1) y `pages/mega-pack-tareas.astro` (1).
- **El pago real de prueba del piloto NO se hizo nunca**: el libro de pedidos (`netlify blobs:list crypto-orders`)
  solo tiene el pedido del preview 78 (5-sep) y los IPN sintéticos `9999999901/02`. La réplica se hizo por decisión
  de John; la entrega con un IPN real de NOWPayments sigue sin verificarse en producción.
- Parche del 6-sep en `scripts/productos-digitales/pendientes/` aplicaba limpio salvo en `GuiaLandingPage` (ya hecho
  el 6-sep) y traía el hero como tarjeta hermana (contra la decisión `ad5bce5`).

## Qué se hizo — PR #81 (`feat/cripto-replica-48`)
1. `KitExcel`, `PlanNegocio`, `ProPromptsEbook` y `mega-pack-tareas` montan las tres puertas (**hero integrado** dentro
   del recuadro de precio, BuyBox hermana, CTA final; el mega-pack tiene 2 puertas y ahora `id="comprar"` en su sección
   final) + la nota de devoluciones bajo la garantía. El eBook monta el componente pero queda **excluido por env**.
2. `CRYPTO_PRODUCTS_EXCLUDE` (CSV, se resta SIEMPRE, también con `all`) en `astro-site/src/lib/crypto-checkout.ts` y
   `netlify/functions/crypto-checkout.ts` (`allowlist()` + `cryptoPermitido()`), misma normalización.
3. `gate-flujo-postpago.py`: sección **E-f** (puertas por landing en el HTML LIVE), flags `--base`, `--crypto-products`,
   `--crypto-exclude`. Tras la revisión: **sin flags toma la expectativa de la env de Netlify** y si los flags no
   coinciden con la env, falla. Contra un preview hay que pasar los flags (su contexto de env no se lee).
4. Nombre del diálogo en Kits Excel y Planes = `productLabel` del registro `zona-app.ts` (el `<h1>` eran titulares de
   venta de hasta 103 caracteres). eBook = «Pro Prompts eBook» (catálogo).
5. Docs: `PAGOS_CRYPTO_NOWPAYMENTS.md` (sección «Estado 18-sep») y sección nueva de gotchas en `CLAUDE.md`;
   `pendientes/` eliminado.

## Verificación
- **Preview 81** (`CRYPTO_PRODUCTS=all` + `CRYPTO_PRODUCTS_EXCLUDE=pro-prompts-ebook` en `deploy-preview`): gate
  48 productos / 694 entregables / **47 landings con botón y 1 sin él** / 0 fallos de E-f. Contratos: eBook →
  `403 product_not_enabled`; `kit-escandallos` → `200` con factura real `iid=5624684884` (pedido `daf470f4…`, email
  `qa-cripto-preview81@aichef.pro`, **sin pagar**; purgar con `crypto-report?purge_unpaid_before=`). Byte-diff
  preview↔prod de 4 páginas que no debían cambiar: idénticas salvo el snippet de Netlify. Visual en el Chrome de
  Windows: Kit Escandallos (3 puertas) y mega-pack (hero integrado, tarjeta hermana, diálogo «89 EUR»).
- **Revisión adversarial** (workflow: 4 lentes opus en tandas de 2 por la térmica + 2 refutadores por hallazgo, 40
  agentes): 18 hallazgos → 5 confirmados (1 medio: el gate comparaba contra lo que tecleaba el operador; 4 bajos:
  recuentos 46→48, `id="comprar"` del mega-pack) y 13 refutados; 48 comprobaciones en verde. Todos los confirmados
  aplicados en `d7911d2`.
- Gate reformado contra producción (antes del merge): sin flags → 3 encendidos / 45 apagados / 0 fallos; con flags
  distintos a la env → lo canta.

## Producción — LIVE desde el 19-sep-2026 00:2x (verificado)
- Orden: `netlify env:set CRYPTO_PRODUCTS all --context production` (conserva el scope builds+functions) → merge de la
  PR #81 (`7ebc64e`, merge commit) → build de `main` con la variable ya puesta → deploy `6aadb9d7…` publicado.
- Gate LIVE **sin flags** (expectativa desde la env): `CRYPTO_PRODUCTS = all` (47 tras restar el eBook), **47 landings
  con botón y 1 sin él**, 48 productos, 697 entregables, **0 fallos, 0 avisos**. Contrato: eBook → `403 product_not_enabled`.
- Contextos: `production` y `deploy-preview` con `CRYPTO_PRODUCTS=all`; `CRYPTO_PRODUCTS_EXCLUDE=pro-prompts-ebook` en todos.
- Gotcha propio de la sesión: el vigilante `scripts/termica/watchdog-termico.sh` arrancado SIN argumento escribe `.temp`
  y `.frozen` en la raíz del repo, y `git add -A` los coló en tres commits de la rama; sacados del índice y añadidos a
  `.gitignore` en el commit de cierre. Arrancarlo siempre con la ruta del log en el scratchpad.

## Pendiente de John (decisiones suyas, no técnicas)
1. **Pago real de prueba** (12 €, USDT-TRC20) desde producción → `/pago-cripto` «confirmado», email de acceso,
   dashboard; logs de `nowpayments-ipn`; qué variante de firma acepta NOWPayments. Cierra la Fase 2.
2. Sección legal de compra de productos digitales en `/terminos` (la casilla del diálogo enlaza ahí).
3. Botón «Continuar al pago» deshabilitado hasta marcar las casillas: sí/no.
4. Moneda de liquidación (re-medir mínimos con `np-api.sh`).
5. Copy del hub y del `WorldwideBanner` («Paga con tarjeta, Apple Pay o Google Pay…»): hoy no mencionan cripto.

Sesión Claude Code · firma de commits `Via: Claude Code`.

---

## Segunda parte de la sesión (19-sep) — tarjeta lateral de Miselup en los 48 productos (PR #82)

- Encargo: el snippet de John (tarjeta flotante de Miselup) «en la landing pública y en la página privada de dashboard
  de cada producto». Autorizó mejoras («si crees que debes hacerle mejoras… decídelo tú»).
- Implementación: `components/MiselupSideCard.astro` + condición en `BaseLayout.astro` por registro `zona-app.ts`
  (48 landing + 48 library; `utm_content=landing|dashboard`). Gate HTTP `scripts/astro-migration/miselup-gate.py`.
- Revisión adversarial (2 lentes opus + 2 refutadores/hallazgo, 32 agentes): 15 hallazgos → 9 confirmados y aplicados
  (`94ba695`): sin `transform` en el fixed, corte 767 px, `visibility` al replegar, `max-height`, sin auto-abrir en
  dashboard ni viewports bajos, `seen` al abrir, `aria-label` alterna, gate por firma y más páginas ajenas.
- Preview 82: gate 96/96 + 13 ajenas limpias; visual en Chrome de Windows (escritorio auto-abre y queda centrada al
  hacer scroll; móvil línea fina → abre → ✕ la elimina; la franja de 700 px no se pudo ver porque la ventana de Windows
  dejó de aceptar el redimensionado). Merge `e22961d`.
- **Producción (19-sep, verificado):** deploy `e22961d` publicado; `miselup-gate.py` LIVE **96/96** (48 landings con
  `utm_content=landing` + 48 dashboards con `utm_content=dashboard`) y 13 páginas ajenas con cero firma; WhatsApp intacto
  (landing 1, precios 1, dashboard 0 en HTML porque lo pinta el island).

## Tercera parte (19-sep) — «Próximamente» del hub y cola de productos nuevos (barrido de 30 días)

- Barrido con 6 lectores + sintetizador (188 menciones, 77 ficheros): de la cola de 5 productos nuevos abierta el 31-ago,
  **4 ya están LIVE** (Food Cost, Manual Manager, Manual Chef Ejecutivo, Pastelería) y queda **la Chocolatería** (A2+B1
  hecha, 9 xlsx en `dl/`; falta B2+C en local). La única tarjeta de «Próximamente» es la suya y decía «Junio 2026»: pasa a
  **«Octubre 2026»** (broadcast previsto 24-oct) en los DOS ficheros del hub (`ProductosDigitalesHubPage.astro` y la SPA).
- No se anuncia nada más sin decisión de John: Churrería-Chocolatería (D3: «no se hace ahora ni se anuncia»), Plan de
  Negocio Heladería (anunciado en CB desde mayo, nunca construido, sin research), inglés nativo (no arranca hasta cerrar
  el ES), banco de 161 ideas de la Hoja 6 (hipótesis, no productos).
- Hallazgo para John: el hub de **ChefBusiness** sigue anunciando 3 productos «en desarrollo» propios (Heladería, Kit Plan
  Financiero y Guía Food Cost — estos dos ya LIVE aquí), contra la tienda única del 31-ago. Se corrige desde la terminal de
  `chefbusiness-astro`, no desde aquí.
- Recordatorio que salió del barrido: el broadcast de lanzamiento de Pastelería (14-oct) era programable desde el 14-sep
  y no consta programado; el del Kit de Tareas Pastelería 2.1 (19-oct) es programable desde hoy.

## Cuarta parte (19-sep) — «Próximos Productos»: de 1 a 23 tarjetas (PR #83)

- John: publicar Churrería-Chocolatería y Plan de Negocio Heladería, elegir las 20 mejores de las 161 ideas y
  mantener el Excel maestro actualizado. Criterio suyo del día: **volumen de búsqueda 0 no descalifica un producto**
  (memoria `feedback_volumen-cero-no-descalifica-un-producto`).
- Selección: panel de 3 jueces opus + síntesis + 2 refutadores (workflow `top20-ideas-productos`); DataForSEO sin saldo
  (402), Search Console sin señal para «montar/plan de negocio», buscador del hub con 32 búsquedas (2 huecos reales:
  hamburguesas, finca de eventos). Lista definitiva, precios y olas en `CALENDARIO-V2-SEMANAL.md` §3.
- Hub: `ProductosDigitalesHubPage.astro` y la SPA en paridad (23 `comingSoon`); sinónimos nuevos en
  `sinonimos-buscador.json` (hamburguesa/burger/smash · pollería/asadero · finca/bodas/eventos).
- Excel maestro: Hojas 4/6/7 actualizadas; backup `…BACKUP-2026-09-19.xlsx`. **Gotcha:** openpyxl 3.1.3 dejó los
  `xfId` de `cellStyles` colgando al compactar `cellStyleXfs`; reparado renumerándolos en `xl/styles.xml`.
- Verificación: preview 83 (23 `data-coming`, 23/23 nombres, contador «48 · 23») → merge `077b72f` → **producción
  verificada**: 23 tarjetas LIVE, contador correcto, `miselup-gate.py` 96/96 y `gate-flujo-postpago.py` 48 productos /
  697 entregables / 0 fallos. Visual en Chrome de Windows sólo parcial (la ventana perdió altura y no aceptó el
  redimensionado): se vieron las 4 columnas y las etiquetas de ola, no la sección entera.

---

## CIERRE DE SESIÓN (19-sep-2026, madrugada) — estado y cómo retomar mañana

**Producción (`aichef.pro`) = `main` = `19413c5`, publicado y verificado.** Árbol limpio, todo pusheado. Cuatro
entregas de la sesión, todas LIVE y con gate en verde:

| Entrega | Commit clave | Verificación LIVE |
|---|---|---|
| Pasarela cripto NOWPayments en los 48 productos (`CRYPTO_PRODUCTS=all` + `EXCLUDE=pro-prompts-ebook`) | `7ebc64e` (PR #81) + `d7911d2` | `gate-flujo-postpago.py` sin flags: 47 con botón / 1 sin él / 0 fallos |
| Tarjeta lateral de Miselup en landing + dashboard de los 48 | `e22961d` (PR #82) | `miselup-gate.py` 96/96 + 13 ajenas limpias |
| «Próximos Productos»: 23 tarjetas (Chocolatería, Churrería, Heladería + top-20) | `077b72f` (PR #83) | hub «48 · 23», 23 `data-coming`, 23/23 nombres |
| Renombre «Cómo Montar una Chocolatería Boutique & Atelier» | `19413c5` | nombre nuevo en el hub LIVE |

Reglas nuevas de John guardadas en memoria y `CLAUDE.md`: todo producto nuevo nace con Stripe + NOWPayments; volumen de
búsqueda 0 no descalifica un producto; térmica reconfirmada (65 °C, `istats`, nada de Playwright).

**Mañana, por orden (sesión PAR = producto nuevo, según la alternancia):**
1. **Broadcast de Pastelería (14-oct) — programarlo ya**: era programable desde el 14-sep y no está. Plantilla en
   `scripts/productos-digitales/emails/`, `resend-broadcast.py --test` a John y luego `--scheduled-at`; slot = último
   programado + 5 días (leer Resend antes; regla `feedback_resend-reprogramar-sin-borrar-a-ciegas`). El del Kit de
   Tareas Pastelería 2.1 (19-oct) y el de la Chocolatería (24-oct) van detrás.
2. **Chocolatería Boutique & Atelier, sesión B2+C en LOCAL** (decisión de John del 12-sep; los siguientes productos en
   el VPS): redactores por bloque desde `guias-v2_0/dump_prompts.py` → `check_bloque.py` → `documentos.py` →
   refutación (tope 2 rondas) → capa de producto (49 en catálogo, payment-links, product-prices, functions, zona app,
   landing `productos/guias/guia-chocolateria-obrador.ts` con las 3 puertas cripto heredadas) → Payment Link de John →
   gates LIVE → quitar su tarjeta de `comingSoon` en los DOS ficheros del hub. Guion y SPEC ya con el nombre nuevo.
3. **Primer producto del top-20: «Tareas Recurrentes: Taquería Mexicana»** (réplica del motor Kit de Tareas v2.4, 1
   sesión, en el VPS). Antes, decisión de John sobre el Mega Pack («13 kits» con 19 vivos): ¿incluye los nuevos?
4. Pendientes de John: pago real de prueba cripto (12 €, USDT-TRC20); sección legal de compra digital en `/terminos`;
   moneda de liquidación; el hub de ChefBusiness anuncia 3 productos propios contra la tienda única (terminal
   `chefbusiness-astro`); research normativo de la Carnicería Boutique antes de comprometer su guion.

**Trampas que dejó la sesión (ya documentadas donde tocan):** `watchdog-termico.sh` sin argumento escribe `.temp`
en la raíz (ya ignorado); openpyxl deja `xfId` colgando al guardar el Excel maestro (reparación en la memoria del
roadmap); el Chrome de Windows dejó de aceptar `resize_window` a mitad de sesión (comprobar móvil por CSS servido).

Sesión Claude Code · firma `Via: Claude Code`.
