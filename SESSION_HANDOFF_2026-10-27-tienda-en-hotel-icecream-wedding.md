# SESSION HANDOFF — 27-oct-2026 · Tienda EN: Hotel Checklists Kit Pro ($29) + Ice Cream Shop Business Plan Kit ($39) + Wedding Venue Business Plan Kit ($49) (sesión Claude Code, Mac + VPS)

## 0. Estado en una línea
John (27-oct): «vamos a trabajar en traducción al inglés de 3 de ellos… escoge los tres que siguen y dale luz verde continua…
completos me dices y creamos los enlaces de pago en Stripe». **Los tres están LISTOS a falta del Payment Link**, en PR apilados:
**#170 Hotel → #171 Ice Cream → #172 Wedding** (abiertos contra `main` para tener preview; el diff de cada uno incluye los de abajo
hasta que se fusionen). Fichas de Stripe: `PAYMENT_LINKS_PENDIENTES_JOHN.md`. ≈ 2 h 30 de reloj (07:30 → 09:55 CET), ≈ 5,4 M tokens
de subagentes para los tres. CPU del Mac 42-57 °C toda la sesión (centinela a 63 °C sin una alerta); todo lo pesado en el VPS.

## 1. Por qué estos tres (DataForSEO US, 27-oct)
| Producto EN | ← ES | Demanda US |
|---|---|---|
| Wedding Venue Business Plan Kit | `plan-negocio-finca-eventos-bodas` (45 €) | «wedding venue business plan» 1.000 LOW (260 → 1.000 en 6 meses) + «event venue business plan» 720 |
| Ice Cream Shop Business Plan Kit | `plan-negocio-heladeria` (35 €) | 320 + «how to open an ice cream shop» 170 |
| Hotel Checklists Kit Pro | `kit-tareas-hotel` (18,50 €) | hotel housekeeping / room cleaning checklist 260 (una serie) + maintenance 70 + template 50 + … ≈ 450 |

Descartados: guía Dark Kitchen (ES v1: hay que subirla a v2 antes), «housekeeping checklist template» 1.900 (doméstica, Pinterest),
el resto < 50/mes. Precios por la escalera del ES: finca 45 € → **$49**, kit hotel 18,50 € → **$29**.

## 2. Hotel Checklists Kit Pro — PR #170 (`checklists-kit/hotel/`)
- 19 xlsx EN (74 hojas, 636 tareas + 24 fechas): FDA Food Code 2022 en °F, MAHC 2024 (piscina/spa), ASHRAE 188/CDC, OSHA 1910.1030,
  NFPA sin intervalos inventados, caja en dólares, festivos US. Código común mínimo (`HOJA_CAJA`, `HOJA_AREA_AUTOTEST`): 10 kits EN
  publicados idénticos byte a byte.
- Revisión opus: 1 B · 3 M · 15 m (B1: el cierre del spa apagaba la filtración del hot tub; M1: simulacro trimestral IFC R-1). Gates 8/0.
- **Parche de seguridad del ES LIVE** (commit `33096bc6`, sin versión ni correo): 15 «Cierre Spa» B7, 15 «Apertura Spa» B6, 09 B13.
  Erratas ES menores pendientes de su próxima v2.x: `checklists-kit/hotel/SPEC.md` §5 (orden del 18, «< 5 °C», «Apertura y Cierre»)
  y la landing ES dice «53 hojas / 11 departamentos» (los libros tienen 74 hojas).
- Testimonios EN sin marcas reales (el ES cita Ritz-Carlton, Four Seasons, Meliá…).

## 3. Ice Cream Shop Business Plan Kit — PR #171 (`business-plans-en-10/`, conjunto `ice`)
- Word 24 págs. · Financial Projections · Startup Checklist (80). Caso: 165 × $7.50 × 310 = $383,625; CAPEX $204,100; SBA $162,000;
  holgura 18.3 %; DSCR 2.26; neto 5.6 / 8.6 %. **Base pasteurizada comprada** (D190); pasteurizar en el local = variante.
- Revisión opus: 0 B · 5 M · 12 m (licencias por estado con fuente, CFPM = person in charge, O13, sin «no hood needed»). Sin erratas ES.

## 4. Wedding Venue Business Plan Kit — PR #172 (`business-plans-en-9/`, conjunto `wed`)
- Word 25 págs. · Financial Projections · Startup Checklist (84) · Pricing Calculator (168 fórmulas, autotest 574) · Venue Rental
  Agreement (12 págs., «template, not legal advice»). Caso: 90 × $68 × 100 = $612,000; CAPEX $570,500; SBA $470,000; holgura 20 %;
  DSCR 1.86; neto 8.9 / 14.2 %.
- Decisiones del orquestador: lease largo ≥ plazo del préstamo con prórrogas («SBA lenders typically require…»), opción de
  compra/ROFR, consentimiento del propietario, TI allowance; FTC Cooling-Off Rule solo «ask your attorney» (16 CFR 429.0(a)(6) excluye
  el alquiler de inmuebles: abierto en la revisión).
- Revisión opus: 2 B · 5 M · 21 m (B1 comisión 1 de 10 al 15 % en el checklist; B2 O20 con meses de la pizza). **Gotcha: `preparar_tandas`
  del wed regenera `GM.json` y desharía el arreglo de O20 (c0529)**: reaplicarlo si se vuelve a correr. Erratas ES (no legales):
  `BP9/ERRATAS-ES.md`.
- Las fotos `plan-finca-*` son de finca mediterránea, no de granero US (la ficha no lo describe como tal). Mejora opcional: hero US.

## 5. Al crear John los links — en este orden
1. Comprobar cada link con la CLI de Stripe (USD, pago único, *exclusive*, impuesto automático, factura, redirección a `/access`).
2. Env de Netlify (builds, all): `VITE_STRIPE_PAYMENT_LINK_HOTEL_CHECKLISTS_KIT`, `VITE_STRIPE_PAYMENT_LINK_ICE_CREAM_SHOP_BUSINESS_PLAN`,
   `VITE_STRIPE_PAYMENT_LINK_WEDDING_VENUE_BUSINESS_PLAN`; `sync-payment-links.py` → `payment-links.ts` (commit en la rama de cada uno).
3. Fusionar **#170 → #171 → #172** (tras cada merge, la rama siguiente queda con el diff limpio; `git` del Mac 2.19: no hay
   `merge-tree --write-tree`, usar `merge-base --is-ancestor`). Gates LIVE: `gate-flujo-postpago --only <slug>` ×3 + completo,
   `tienda-gate`, `robots-gate`, `miselup-gate`, cripto (curl al checkout con `qa-…@aichef.pro`), sitemap reenviado en GSC.
4. Correos EN (14:00Z, segmento EN, `hello@news.aichef.pro`): **Wedding 23-feb-2027 · Ice Cream 28-feb · Hotel 5-mar**; plantillas
   `emails/broadcast-{wedding-venue-business-plan,ice-cream-shop-business-plan,hotel-checklists}-lanzamiento-en.*`; borrador + prueba
   a John + routine ≥ 30 días antes (Resend no programa más lejos). **Siguiente hueco EN: 10-mar-2027.**
5. `PAYMENT_LINKS_PENDIENTES_JOHN.md` → HECHOS; CALENDARIO → ✅ LIVE.

## 6. Deuda (no bloquea)
- Pizza EN LIVE: DV del checklist dice «— = pending» (la lista es ✓/☐/N/A; `business-plans-en-8/textos_en/GR.json` c0659) y O20 con
  meses de septiembre.
- Motor común de planes: la nota de la holgura dice «cuánto puedes caer» y mide ventas/equilibrio − 1 (afecta a todos los planes).
- Worktrees: Mac `<scratchpad>/wt-{hotel,icecream,wedding}`, VPS `/root/wt-{hotel,icecream,wedding}` (limpios): borrarlos tras el merge.

## 7. Método que funcionó (para repetir)
F1 opus por producto en paralelo (research + inventario + SPEC en una pasada) → paso 1a opus (clones, caso, dry-run en el VPS) →
traductores sonnet **reanudados con SendMessage** para mantener terminología → ensamblado y gates en el VPS (el implementador del 1a,
reanudado) → UNA revisión opus nueva y escéptica (cazó B reales en los tres) → F3 sonnet → PR draft → gates contra preview con un
sonnet reanudado. Tope de 3 agentes a la vez; ramas apiladas con conflictos triviales (glosario, `mapas.py`, listas de gates) resueltos
quedándose con los dos lados + regresión de los 10 conjuntos (37/37).
