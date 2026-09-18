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
