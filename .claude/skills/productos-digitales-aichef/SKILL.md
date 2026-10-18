---
name: productos-digitales-aichef
description: Reglas operativas de los productos digitales de aichef.pro — política de 3 fases y presupuesto, reparto Mac↔VPS, pasarela cripto NOWPayments (3 puertas, env vars, gates) y correos de lanzamiento o actualización en cola de 5 días. Cargarla SIEMPRE antes de crear, actualizar o lanzar un producto digital (guía, kit, plan, manual) o tocar su landing, su pago o su correo.
---

# Productos digitales de aichef.pro — reglas operativas

> Movido literalmente desde el `CLAUDE.md` raíz el 2026-10-12 (/doctor) para no cargarlo en cada sesión. Los no negociables siguen resumidos en la raíz, sección «Detalle bajo demanda».
> La regla 🔴🔴 PROPORCIONALIDAD del `CLAUDE.md` raíz manda sobre todo lo de esta skill. Complementa la skill agnóstica `digital-product-launch`.


### 🔴 Jerga profesional ES → EN (John, 13-oct-2026)

Todo trabajo en otro idioma (producto, landing, hub, blog) consulta y amplía `scripts/productos-digitales/GLOSARIO-JERGA-ES-EN.md`: la jerga del profesional del país manda en tres capas (producto, contenido, SEO de la landing), y la F1 de cada producto lleva su sección «Jerga profesional» con fuente. **Los nombres comerciales, de producto y de marca ya publicados no se cambian**: la keyword va como descriptor, y los calcos se proponen a John caso a caso.

### Pasarela cripto NOWPayments: en los 48 productos desde el 18-sep-2026 (PR #81)

Segunda puerta «Pagar con cripto» (Stripe sigue siendo la principal). Doc canónico: `PAGOS_CRYPTO_NOWPAYMENTS.md`
(leerlo ENTERO antes de tocar nada). Lo que hay que saber para no romperla:

- **Dos variables, las dos en scope `builds` Y `functions`, y NINGUNA surte efecto sin redeploy**: `CRYPTO_PRODUCTS`
  (vacía = apagado en todo el sitio · `all` · CSV) y `CRYPTO_PRODUCTS_EXCLUDE` (CSV que se resta SIEMPRE, también con
  `all`; hoy `pro-prompts-ebook`, 9 € < mínimo de NOWPayments). El build decide si el botón llega al HTML; la function
  vuelve a decidir al pulsarlo. Si una capa ve una variable y la otra no, el botón se pinta y el checkout responde 403.
- **Toda plantilla de landing monta las TRES puertas** (`CryptoPayButton.astro`: `hero` DENTRO del recuadro de precio
  tras el sello de Stripe, `buybox` como tarjeta HERMANA fuera del recuadro dorado, `cta` dentro del CTA final) + la nota
  de devoluciones bajo la garantía. **Solo la variante `buybox` emite el `<dialog>` y el `<script>`**: una página con
  `hero`/`cta` y sin `buybox` deja botones que solo llevan a `#comprar`. El mega-pack solo tiene dos puntos de compra
  (hero y su sección final, que hace de BuyBox y lleva el `id="comprar"`): 2 puertas.
- 🔴 **REGLA DE JOHN (19-sep-2026): todo producto nuevo NACE con los dos sistemas de pago, Stripe principal y
  NOWPayments secundario. Una landing sin las tres puertas cripto no está terminada.** Con `CRYPTO_PRODUCTS=all` no
  hay que tocar la env: el producto las hereda al usar una plantilla (si nace con plantilla o página nueva, montar
  `CryptoPayButton` en hero, BuyBox y CTA + la nota de devoluciones). Lo que SÍ hay que regenerar es
  `netlify/shared/product-prices.ts` (`sync-product-prices.py`): el importe de la factura sale de ahí, nunca del
  cliente. Y darlo de alta en `zona-app.ts`, de donde sale el nombre corto del diálogo. Cierre del producto = gate
  E-f LIVE en verde + curl al checkout.
- Gate: `python3 scripts/productos-digitales/gate-flujo-postpago.py` toma la expectativa de la env de Netlify (sección E-f);
  contra un preview hay que pasar `--base https://deploy-preview-N--aichefpro.netlify.app --crypto-products all
  --crypto-exclude pro-prompts-ebook` (su contexto de env no se lee). Exige 3 botones `data-crypto-open`
  + 1 `<dialog>` + 3 `aria-controls` por landing encendida y CERO rastros de `data-crypto` en las excluidas. Ojo: contra
  un preview, las 4 descargas por env var del eBook «fallan» porque apuntan a `aichef.pro`; es el `--base`, no un bug.
- **El pago real de prueba del piloto sigue sin hacerse** (18-sep): el circuito IPN→email→dashboard está probado con
  IPN sintéticos firmados y 42 tests de firma, no con un pago de NOWPayments. Si un cliente paga y no recibe el enlace:
  `resend-access` y `crypto-report.py` (necesita `ADMIN_PASSWORD` exportada).
- Probar un checkout por curl **crea una factura real y un pedido en el libro** (Blobs, compartido entre preview y
  producción): usar email `qa-…@aichef.pro` y purgar con `crypto-report?purge_unpaid_before=`.

### 🔴 Reparto Mac ↔ VPS en TODOS los productos (John, 3-oct-2026)

«Trabajamos en local lo que da la calidad; en el VPS todo lo que al Mac le supone un esfuerzo innecesario; tú ensamblas en
local hasta pedirme el Payment Link». Probado en la Churrería-Chocolatería (PR #105):
- **Mac**: orquestación, redactores Sonnet (Agent tool, API-bound, 2-3 a la vez con `istats` < 60 °C), ficha de landing, commits, PR.
- **VPS** (`ssh vps`, `/root/chefpro-modernize`, venv `/root/venv-guias`): generadores de Excel + `gate_libros.py`,
  `documentos.py`, gates con openpyxl/PyMuPDF (`paginas-gate`, `censo-entregables`, `gate-no-latinos`) en un `git worktree`
  de la rama; `scp` de vuelta y commit desde el Mac; dejar el árbol del VPS limpio.
- **Netlify** construye el preview; gates contra él con `--base`. **Una** revisión Opus final sobre los `.md` (cazó 9 bloqueantes).
- Lanzar `claude -p` headless en el VPS lo bloquea el modo automático: requiere una regla de permiso que decide John.
- **Scripts Python al VPS: fichero local + stdin** (`ssh vps '/root/venv-guias/bin/python -' < script.py`, con `os.chdir` dentro).
  Un heredoc sin comillas metido en `ssh vps '…'` lo expande el shell remoto (`$?` → `0` dentro de una regex) y el script sale
  limpio con un resultado falso: el 18-oct un escaneo dio «0 kits» y había 4. La `/dev/null` del VPS está rota: redirigir a `/tmp`.

### 🔴 Productos nuevos: POLÍTICA DE 3 FASES + presupuesto proporcional al precio (John, 20-sep-2026)

John delegó la toma de decisiones del proyecto de productos digitales («tú lideras este proyecto conmigo, te delego la
toma de decisiones en todo»); la única no delegable es el Payment Link de Stripe. Texto completo y tablas en
`scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md` §3. Resumen operativo:

- **F1 Fundamentos → F2 Entregables → F3 Producto y lanzamiento.** Cada fase cierra con su gate de salida y `commit +
  push`, y una línea en el handoff con el comando exacto para retomar. Nunca se sigue a la fase siguiente con la anterior
  sin cerrar: lo que faltaba no eran fases sino el corte duro.
- **El tamaño decide las sesiones y el techo de tokens de subagentes**: S (kits réplica 12-14 €) = 1 sesión con 3 cortes,
  ≤ 2,5 M · M (planes 35-45 €, kits de gestión, eBooks) = 2 sesiones, ≤ 5 M · L (guías y manuales 55-65 €) = 3 sesiones,
  ≤ 10 M. Si un producto pasa su techo un 30 %, se para y se reporta. Calidad = gates de script + tope de 2 rondas, no
  más agentes.
- **Máquina**: F1 en el Mac (solo API); F2 en el VPS para L/M y en el Mac en serie con vigilante para S; F3 en cualquiera.
- **Los gates LIVE (`gate-flujo-postpago.py`, `miselup-gate.py`) leen el registro de productos del árbol LOCAL**: desde
  un `main` sin `git pull` cuentan 49 productos y no 50, y parecen verdes. Comprobar el commit local antes de fiarse.
- **Si hay OTRA sesión trabajando en este directorio** (commits ajenos en `main`, rama activa cambiada), no tocar la rama
  activa: `git worktree add <scratchpad>/wt-<tema> <rama>` y `git push origin HEAD:main` desde allí. Pasó el 20-sep.
- **Kit de Tareas nuevo (top-20)**: copiar `scripts/generate-tareas-taqueria.py` + `scripts/productos-digitales/kit-tareas-taqueria/`
  (contrato del molde v2.0, gates F1/F2, comparador). Molde canónico = kit base v2.0, NO el sushi-bar (v1.1 CB);
  `postprocess-transversal.py` NO se corre sobre kits v2.0.
- **Mega Pack congelado en sus 13 kits** (155 ficheros en la function); los kits nuevos se venden aparte y el pack va
  **siempre el último** del hub. **Orden del hub**: novedades primero (la más nueva en 1), luego los más vendidos.

### Correos de producto: uno por cada actualización o lanzamiento, en cola de 5 días (John, 2026-09-05)

Regla de trabajo permanente: **cada vez que un producto digital se actualiza de versión (2.0, 2.1…) o se crea uno
nuevo, se programa en Resend un broadcast individual** que lo anuncia (a los que ya lo tienen: la nueva versión está en
su dashboard sin coste; a los demás: se vende). Los correos forman **una sola cola con 5 días de separación**: el hueco
de cada uno es el `scheduled_at` más tardío que haya en Resend + 5 días, a las 08:00 UTC (10:00 Madrid). Plantillas:
`scripts/productos-digitales/emails/broadcast-kits-tareas-v2-es.html` (actualización) y
`broadcast-manual-manager-lanzamiento-es.html` (lanzamiento); se programan con
`scripts/productos-digitales/emails/resend-broadcast.py` (prueba a John con `--test`, luego `--scheduled-at`). El slot
se anota en el handoff y en `CALENDARIO-V2-SEMANAL.md`. Detalle: skill local `resend-aichef` y memoria
`feedback_correo-por-cada-producto-actualizado-o-nuevo`.

### Guía de Equivalencias ES ↔ Hispanoamérica: todo producto ES nace con la suya (13-oct-2026, PR #130)

Cada producto ES lleva un bonus docx propio, «Guía de Equivalencias para tu país», con los términos de España que usa
ESE producto dichos país por país (21 países) y una ficha de una página por país (impuestos, sanidad, laboral,
licencias, unidades…). Todo vive en `scripts/productos-digitales/equivalencias-es/` (`PLAN.md`, SPECs, `fichas/`,
`glosario/`, `terminos.json`, `textos.json`); la vista legible del glosario es `GLOSARIO-JERGA-ES-LATAM.md`.

**Producto ES nuevo o actualizado (F3), en este orden:**
1. `python3 scripts/productos-digitales/equivalencias-es/censo-terminos-es.py --terms scripts/productos-digitales/equivalencias-es/terminos.json --out scripts/productos-digitales/equivalencias-es/datos/matriz.json` (≈80 s; el registro sale de `PRODUCT_FILES`, así que el producto tiene que estar ya en `get-download-urls.ts`). El gate del script exige el número de productos ES: súbelo.
2. `build_guia_es.py --only <slug>` y `--check --only <slug>` (en el VPS si son muchos).
3. Cablear como los 51: clave `guia-equivalencias` en `PRODUCT_FILES`, tarjeta literal en el dashboard (Globe, `.docx`), BONUS en la ficha de la landing (imagen `es-guia-equivalencias.jpg`, `€15`) y la FAQ «¿Sirve en México, Colombia, Argentina…?» con sus ejemplos (plantilla en `textos.json`, ejemplos en `datos/integracion.json`).
4. Si el producto usa un término de España que no está en `terminos.json` y cambia en América, añádelo con sus variantes en los 21 países (`SPEC-GLOSARIO.md`).

Las fichas caducan: revisión anual en enero (salarios mínimos, tipos, reformas laborales en curso en MX, CL, CO y BR).
