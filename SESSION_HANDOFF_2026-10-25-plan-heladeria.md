# SESSION HANDOFF — 25-oct-2026 · Plan de Negocio: Heladería Artesanal (ES, 35 €) + normativa derogada (sesión Claude Code, Mac + VPS)

## 0. Estado en una línea
✅ **CERRADO: producto nº 52 LIVE el 25-oct a las 15:52 (Madrid)** — PR #161 → merge `cbdcccd6`. **PR #160 fusionado** (`daf6f28a`).
Los dos merges los aprobó John por escrito («apruebo el merge que necesites»). Lo que queda abierto está en §5 y en la nota al carril Cursor.

## 1. Lo que pidió John y lo que se decidió
- John (25-oct): «revisa cómo estamos en ambos frentes» → revisión hecha → «adelante con tu plan».
- Plan:
  1. Producto ES nuevo = **Plan de Negocio: Heladería Artesanal**. Es el primero de «Próximos» (prometido para Q4), reutiliza el motor de planes 2.2 y su gemelo EN tiene demanda: «ice cream shop business plan» 320/mes en EE. UU., competencia baja.
  2. Después, **Finca de Eventos y Bodas**: «wedding venue business plan» 1.000/mes + «event venue business plan» 720/mes en EE. UU., ambos al alza (confirmar con la SERP que no es estacional).
  3. Arreglo corto de la normativa derogada.
- Demanda en España de todos los candidatos: 0-20/mes (no descalifica). El criterio para elegir el producto ES es su gemelo EN.

## 2. Heladería — qué hay (todo en `scripts/productos-digitales/plan-heladeria/`)
- F1: `F1-research-heladeria.md` (6 textos del BOE leídos en origen), `F1-camino.md`, `SPEC.md` (D1-D18). Commit `5344a48e`.
- F2: `F2-NOTAS.md` (calibración y revisión). Los entregables están en `astro-site/public/dl/plan-negocio-heladeria/`:
  - plan financiero xlsx: 9 hojas.
  - Word: 10 H1, 7.061 palabras, A4.
  - checklist: 80 tareas en 6 fases.
  - guía de equivalencias: 70 términos.
- Caso:
  - Clientela y ventas: 143 clientes/día × 4,90 € × 310 días; Mes 1 = marzo; ventas de 217.217 / 234.594 / 246.324 €.
  - Inversión: 117.150 € en partidas; necesidad 183.170 €.
  - Financiación: 55.000 € propios + 129.000 € de préstamo al 6 % a 7 años con 1 de carencia.
  - Ratios: DSCR mínimo 1,37; saldo mínimo 30.175 € (marzo); holgura de caja 19,5 / 8,7 / 9,9 %; neto 5,8 / 7,7 / 7,6 %.
- Revisión opus final: 0 bloqueantes, 7 mayores y 17 menores, todos aplicados (`45824ce0`, `ab7e42d8`). Los dos que valían dinero:
  - **M1**: un verano malo NO cabe en la holgura de los años 2-3.
  - **M2**: el art. 3.2.b del RD 1021/2022: los 500 kg/semana son de venta TOTAL, no solo lo que se sirve a restaurantes.
- F3:
  - Hecho: landing + `-access`/`-library` + dashboard, entrega (4 functions), catálogo, changelog 1.0, `zona-app` y `product-prices`.
  - Hubs ×7 + SPA: posición 1 con «✨ Nuevo»; sale de «Próximos». El Manual del Chef Ejecutivo pierde el ✨.
  - Buscador, `llms-full` y `sitemap-lastmod`; 7 imágenes; correo `emails/broadcast-plan-negocio-heladeria-lanzamiento-es.html`.
  - Producto nuevo: sin testimonios, rating ni tachado (convención de Chocolatería y Churrería).
- Gates contra el preview: `gate-flujo-postpago --only` solo falla por el Payment Link (#comprar, env, `payment-links.ts`). Cripto, descargas, acceso y dashboard, OK.
- Consumo: ≈ 2,2 M de tokens de subagentes (techo M: 5 M). Mac a 38-57 °C toda la sesión.

## 3. Cierre de la Heladería — HECHO el 25-oct (sesión Claude Code)
- Link de John `https://buy.stripe.com/5kQ28k94w78i2QT8Zn6oo21` (`plink_1UUSdP4CcdRGidmEm3lXcQyH`), comprobado con la CLI: 3500 EUR,
  pago único, *exclusive*, impuesto automático, factura, redirección a `/access`. Env creada (builds, all), `payment-links.ts` → `54cfb41a`.
- Preview: el link en los 4 botones y `gate-flujo-postpago --only` 0 fallos → ready → merge.
- Gates LIVE: postpago 1 producto / 4 entregables / 0 fallos / 0 avisos · `tienda-gate --base https://aichef.pro` verde (slug ya en
  `PLANES_ES`) · `robots-gate --live` verde · Miselup 104/104 · `fase6-gate.py https://aichef.pro` 3/2283, que son los 3 conteos
  congelados de siempre. Sitemap reenviado a GSC (14:59Z).
- Cripto LIVE: `crypto-checkout` → 200 con factura real de prueba (`qa-heladeria@aichef.pro`, pedido `0898e071…`, estado `created`).
  Purgarla con `crypto-report?purge_unpaid_before=` cuando haya `ADMIN_PASSWORD` (shell de John), como la de la Churrería.
- Correo: prueba a John (`01a17393…`) · borrador `3297bad5-26c1-4420-8137-cdfaf11b4067` → routine `trig_0196bsymHKgB8728KxtTmBdk`
  (29-oct 15:07Z) lo programa para el **28-nov 08:00Z**. Siguiente hueco ES: 3-dic.
- Pendiente para el carril Cursor (no se toca desde aquí): `plan-heladeria/NOTA-CARRIL-CURSOR.md`.

Pasos que se siguieron (referencia para el próximo):
1. Ficha de Stripe: `PAYMENT_LINKS_PENDIENTES_JOHN.md` (en la rama). EUR 35, *exclusive*, impuesto automático, factura, redirección a `/plan-negocio-heladeria-access?session_id={CHECKOUT_SESSION_ID}`.
2. Comprobar el link con la CLI: `stripe get /v1/payment_links/<plink> --live` y sus `line_items`.
3. Env `VITE_STRIPE_PAYMENT_LINK_PLAN_HELADERIA` (scope builds) → `sync-payment-links.py` → commit.
4. Sacar el #161 de draft → merge (aprueba John).
5. Gates LIVE:
   - `gate-flujo-postpago.py --only plan-negocio-heladeria`
   - `tienda-gate.py --base https://aichef.pro` (añadir el slug a `PLANES_ES` tras el LIVE)
   - `robots-gate.py --live`
   - `miselup-gate.py`
   - `fase6-gate.py https://aichef.pro` (recibe la URL BASE: con la de la landing da 185 falsos fallos)
6. Reenviar el sitemap en GSC.
7. Correo ES en el hueco **28-nov 08:00Z**: borrador con `resend-broadcast.py` (las guardas piden la landing en 200, o sea, tras el LIVE) + prueba a John + routine que lo programe el 29-oct o después (Resend no programa a más de 30 días).
8. Avisar al carril Cursor: `plan-heladeria/NOTA-CARRIL-CURSOR.md` (páginas `/usos/` de heladería, 3 posts ES y la FAQ de `heladero-consultor` que promete un 12-22 % de neto).

## 4. PR #160 — normativa derogada (fusionado el 25-oct, `daf6f28a`)
- 7 entregables vendidos citaban como vigentes el RD 1420/2006 (anisakis) o el RD 3484/2000. Los dos los derogó el RD 1021/2022.
  - Kits de tareas sushi-bar 03 y marisquería 03: «−20 °C 7 días» → «−20 °C ≥ 24 h o −35 °C ≥ 15 h».
  - Kit de inventario 04.
  - Guía y manual de japonés y nikkei.
- Parche XML: solo las cadenas afectadas, CRC verificado. Generadores corregidos.
- Revisado por el orquestador cadena a cadena; preview servido = rama (md5).

## 5. Hallazgos para la cola (no tocados)
- ✅ **HECHO el 25-oct por la tarde (PR #162 + #163, ver CALENDARIO):** ~~6 guías ES entregan como «guía PDF» una portada de 1 página (~1,8 KB)~~: panadería-obrador, casual, japonés, mexicano, nikkei y peruano. Además la landing promete «60+ páginas» (japonés: 4 veces) con un Word de ~3.000-6.300 palabras.
  - Dos salidas: rápida (PDF real desde el docx en el VPS + cifras de páginas medidas en la landing) o la subida a v2 de cada guía (L), que además desbloquea «How to Open a Restaurant» EN (880/mes).
  - **Decisión de John.**
- Cola de correos EN: llega al 13-feb (22 productos esperando, uno cada 5 días). Proponer a John agrupar kits en un mismo correo.
- Panadería 2.2 LIVE: «España 2026» en `Inversión Inicial!A2` y en `seo.description`; su `emailBody` promete «60+ trámites RGSEAA».
- «036/037» en `plan-negocio-food-truck.ts` (el 037 no vale para una SL).
- Kit Tareas Heladería ES: el BONUS-02 pone el Día de la Madre en junio (en España es en mayo).

## 6. Para retomar
```
cd ~/chefpro-modernize && git fetch && gh pr view 161 && gh pr view 160
# worktree Mac: <scratchpad>/wt-heladeria (se pierde al reiniciar: recrear con git worktree add … feat/plan-negocio-heladeria)
# worktree VPS: /root/wt-heladeria (limpio, en la rama)
```
