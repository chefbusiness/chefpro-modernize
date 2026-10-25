# SESSION HANDOFF — 25-oct-2026 (noche) · Plan de Negocio: Pizzería Napolitana (ES, 35 €) + Pizza Shop Business Plan Kit (EN, $39) (sesión Claude Code, Mac + VPS)

## 0. Estado en una línea
John (25-oct, noche): «luz verde, decide tú» → Claude eligió la **Pizzería Napolitana**; luego John: «la idea en esta sesión es dejar
la versión en los dos idiomas en producción para la venta». Hecho en una sesión (≈ 5 h de reloj):
- **ES LIVE** — PR #165 → merge `2e7a3af5`. Link `plink_1UUXG84CcdRGidmEsDF3iCG4` (35 EUR), env `VITE_STRIPE_PAYMENT_LINK_PLAN_PIZZERIA`.
- **EN LIVE** — PR #166 (apilado) → merge `64ace831`. Link `plink_1UUXZ54CcdRGidmEovs56WB3` ($39, nombre en Stripe «Neapolitan-style
  Pizza Shop Business Plan Kit»), env `VITE_STRIPE_PAYMENT_LINK_PIZZA_SHOP_BUSINESS_PLAN`.

## 1. Por qué este producto
ES «plan de negocio pizzeria» 10/mes (igual que hamburguesería), pero **EN «pizza shop business plan» 320/mes en EE. UU. (×6,5 en 6
meses)** y «pizzeria napolitana» 4.400/mes en ES. La Hamburguesería Smash (Q4 en el hub) queda como siguiente candidata ES.

## 2. ES (`scripts/productos-digitales/plan-pizzeria/`: F1-research, F1-camino, SPEC D1-D19, F2-NOTAS, REVISION-FINAL)
- Motor de planes 2.2, versión 1.0, **semilla del Tapas Bar 2.2** (molde A-β + checklist C2), cero código común, pid fuera de `PRODUCTOS`.
- Caso: 66 comensales (51 sala + 15 llevar/domicilio) × 19,50 € × 300 días → 386.100 €; neto 8,5 / 10,0 / 9,6 %; préstamo 159.000 € a
  7 años; DSCR mín. 1,88; holgura de caja A1 24,3 %. **Mes 1 = septiembre.** Bebida para llevar al 21 % con la línea partida del motor.
- 5 entregables: plan financiero (9 hojas) · Word (10 secciones, ≈ 7.150 palabras) · checklist (80 tareas) · **calculadora de masa y
  escandallo** (pliego ETG + % panadero, 8 pizzas; autotest 422) · guía de equivalencias (75 términos, censo 53 → 54).
- **Hallazgo legal que vende**: «Pizza Napoletana» es ETG **con reserva de nombre** desde el 18-12-2022 (Reg. de Ejecución (UE)
  2022/2313; Reg. (UE) 2024/1143 arts. 68, 72-73). El título se mantiene; el producto enseña qué poner en la carta.
- Revisión final opus: 1 B · 8 M · 17 m → aplicados B + M + 15 m. Gotchas cazados: «Campaña» por «Campana» (`motor.TILDES`) sacaba la
  campana de la amortización → guarda `RX_CAMPANA`; «publica» → «pública» → guarda `RX_PUBLICA`.
- LIVE: postpago 0/0 · tienda verde · robots · Miselup 108/108 · hub PASS · fase 6 = sus 3 congelados · cripto 200 (pedido QA
  `qa-pizzeria@aichef.pro`, purgar con `ADMIN_PASSWORD`) · sitemap reenviado. `whatsapp-gate` no corre en el Mac (pide `dist`).
- **Correo ES 8-dic 08:00Z**: borrador `92c8a19f` (prueba a John enviada) → routine `trig_011hWcNXXF55pgXjW7iGCMjF` (8-nov 15:07Z).
  **Siguiente hueco ES: 13-dic 08:00Z.**
- **Arreglo colateral LIVE**: la finca estaba ANIDADA dentro de la heladería en `products-catalog.ts` y `productos-digitales-config.ts`
  (sintaxis válida: esbuild no lo ve). Desanidada en #165.

## 3. EN (`scripts/productos-digitales/business-plans-en-8/`: F1-research-us-delta, F1-inventario-delta, SPEC-delta D133-D155, F2-NOTAS, REVISION-FINAL)
- Conjunto `piz` (clon del Bar EN, porque el ES sale de la semilla del tapas bar); único cambio en código común: `elif CONJUNTO == 'piz'`
  en `business-plans-en/mapas.py`. Regresión de los 7 conjuntos EN: 27/27 sha256 iguales.
- Caso US: 62 covers × $36 × 300 → $669,600; neto 5.9 % → 9.0 %; préstamo SBA $200,000; DSCR 2.62. Versión **2.2** (numeración de la
  familia EN, como la Paella).
- «Neapolitan-style vs VPN-certified» sustituye el bloque ETG (en EE. UU. el nombre no está protegido; la AVPN admite gas donde la leña
  está prohibida). Calculadora EN: masa en gramos con eco oz/lb, $/lb (autotest 434).
- Revisión final opus: 4 B · 6 M · 23 m → todo aplicado.
- LIVE: postpago 0/0 · tienda verde · robots · Miselup 108/108 · hub PASS · cripto 200 (pedido QA `qa-pizzashop@aichef.pro`) ·
  hreflang ES↔EN recíproco · sitemap reenviado.
- **Correo EN 18-feb-2027 14:00Z** (segmento EN, `hello@news.aichef.pro`): borrador `c6290aee` (prueba a John enviada) → routine
  `trig_01Htsk9cNWagXEsLcdM4B6hZ` (19-ene-2027 15:07Z). **Siguiente hueco EN: 23-feb 14:00Z.**

## 4. Deuda (no bloquea)
- **DV del checklist ES** «✓,—,N/A» con celdas «☐» en los planes ES 2.2 (pizzería, heladería, finca, paellero, parrillero): el motor
  lo genera así. El EN lo corrige en su circuito (`mapas_piz`). Arreglar en el motor ES.
- Nota `O20` de los planes EN («settles quarterly (April, July, October, January)»): solo exacta con apertura en enero; afecta a los 8 EN
  anteriores (en el Pizza Shop ya corregida).
- `extraer_docx.py` exige fuente US Letter: falso rojo con fuentes ES en A4 (el ensamblado fuerza Letter). Relajar el chequeo.
- Deuda heredada del motor: `PyG!G14` (10 % fijo) y `Personal!C11`; guía de equivalencias en Letter.
- Pedidos cripto QA sin pagar por purgar (shell de John, `ADMIN_PASSWORD`): `qa-heladeria`, `qa-finca`, `qa-pizzeria` (+ `qa-pizzashop` si se creó).

## 5. Carril Cursor (nota para John)
- FAQ 2 de `/usos/pizzero-consultor` (`src/data/use-cases-content.es.consultor.ts:619`) promete «neto 15-25 %»: cambiar SOLO esa frase
  (7 idiomas); el plan medido da 8,5-10 %.
- `productIds` de las `/usos/` de pizzería → añadir `plan-negocio-pizzeria`; enlaces desde los posts ES de pizzería
  (`ia-para-pizzerias.md` y los que enlazan el Kit de Tareas Pizzería) y al EN desde los posts EN de pizza.
