# Plan de Negocio: Hamburguesería Smash ES 1.0 — F3 (producto y lanzamiento)

> Sesión Claude Code, 31-oct-2026 (F3 nocturna, decisiones delegadas). Patrón = la F3 del Sushi Bar (`plan-sushi/F3-NOTAS.md`),
> fichero a fichero. Mac: ficha, páginas, dashboard, imágenes, correo, commits. VPS (`/root/wt-smash`): censo y guía de
> equivalencias, volcados de los 5 entregables con openpyxl/python-docx (`/root/tmp-ham-f3/`, traídos al Mac para la revisión y
> sin commitear). Sin build local (Mac a 45 °C en la revisión).

## 1. Qué se hizo

- **Ficha** `astro-site/src/data/productos/planes/plan-negocio-hamburgueseria.ts` (molde del Sushi Bar, sin testimonios) + páginas
  landing/access/library, isla `PlanNegocioHamburgueseriaLibraryIsland.tsx`, `PlanNegocioHamburgueseria{Dashboard,AccessGate}.tsx`
  (5 tarjetas, clave `calculadora-hamburguesa`).
- **Registros**: functions ×4 (verify-purchase y resend-access con la venta cruzada al Kit de Tareas Hamburguesería, 12 €), config,
  catálogo (EN `Burger Restaurant Business Plan Kit`), changelog 1.0, `AdminGenerateAccess`, `zona-app`, `tienda.ts` (EN
  `burger-restaurant-business-plan`, `vivo: false`), `product-prices.ts` (+1 línea), hubs ×7 + SPA en posición 1 (el Sushi pierde el ✨;
  sale la tarjeta de «Próximos»), buscador, `sitemap-lastmod`, `llms.txt` 58 → 59, `llms-full.txt`, `tienda-gate.py` (`PLANES_ES`).
- **Enlaces entrantes**: Kit de Tareas Hamburguesería (footer; además su «punto de carne (rare a well done)» pasa a «cocción con sonda
  (70 °C en el centro)», que es lo que dice su plantilla `02-partidas-cocina.xlsx` `Plancha Grill!B14`), Guía Dark Kitchen, Kit de
  Escandallos y Plan Sushi Bar (footer), use case `hamburgueseria` (`productIds`, el plan tras el kit; se cae `pro-prompts-ebook`).
- **Imágenes** `ai-gallery/plan-hamburgueseria-{hero,plancha,carne,patatas,delivery,equipo,plan}.jpg` (1376 × 768, 231-302 KB).
- **Guía de Equivalencias**: matriz con 59 productos ES (`e883ebaa`) y `integracion.json` con los ejemplos de la FAQ.
- **Correo** `emails/broadcast-plan-negocio-hamburgueseria-lanzamiento-es.html` (asunto en el comentario `ASUNTO`, «Hola, colegas,»,
  #111111 + #FFD700, venta cruzada al Kit de Tareas con su precio). **Sin programar** (lo programa el lead con el link).
- **`PAYMENT_LINKS_PENDIENTES_JOHN.md`**: entrada ⏳ con nombre, 35,00 EUR *exclusive* + impuesto automático, factura, redirección,
  descripción en prosa de 259 caracteres (medida con python), env `VITE_STRIPE_PAYMENT_LINK_PLAN_HAMBURGUESERIA` y hero.
- **Legal** (`LEGAL-F3.md`, `87161627`): la carne madurada con los plazos del 853/2004 (6 días; 15 en vacuno deshuesado y envasado al
  vacío) y el batido como hipótesis «confírmalo con tu gestoría», en Word, landing, checklist y calculadora.

## 2. Decisiones

1. **Sin testimonios ni rating** (producto sin ventas; la clave `testimonials` se omite).
2. **11 FAQ** (las de R §6 + la del carrito → Plan de Negocio: Food Truck). Las de la franquicia, con las cifras del Word [63].
3. **Equilibrio en la landing = 76 comensales equivalentes (contable) + 73 de caja el primer año y 82 el segundo** (tokens
   `BE_COMENSALES_DIA`, `BE_COMENSALES_DIA_CAJA`, `BE_COMENSALES_DIA_CAJA_A2`; = Word [40] y [96]). El 73 a secas, sin la salvedad de
   la carencia, era la lección del Sushi (§2.3) y aquí se había colado como «los costes se cubren con 73» (ver M1).
4. Tags de los hubs = los de la familia (`hamburgueseria`/`burger`, `plan-negocio`/`business-plan`).
5. Nombre del hub EN provisional «Business Plan: Smash Burger Restaurant» → lo sustituye la tarjeta del gemelo EN en su F3.

## 3. Contraste landing ↔ entregables (volcados del VPS, 31-oct)

Inversión 162.143,59 € (`Inversión Inicial!B30`), partidas + imprevistos 104.350 € (A7-A24 = 99.500 + B27 4.850), CAPEX 110.350 € (B31),
fondo 51.793,59 € (B29), IVA 21.913,50 € (B32), necesidad 184.057,09 € (B33) · 55.000 + 130.000 € (`0. Supuestos!B30/B31`) · local 90 m²,
36 plazas (30 + 6, `Supuestos!C24/B51`) · 95 comensales equivalentes, unos 53 en sala, pedido = 1,7 (`Supuestos!B4/C4`) · ticket 16,00 €
(B5), 17,00 / 29,10 / 33,47 € y carta +15 % en plataforma (C5) · 300 días (B6) · ventas 456.000 € (`PyG 3 Años!B9`) · neto 46.512 € y
10,2 / 11,4 / 10,7 % (`PyG!B47`, `B55:D55`) · comisiones 32.832 € (`PyG!B16`) · plataforma 24 %, comisión 30 % (`Supuestos!B16/B17`) · food
cost 28 % (B13) frente al 24,4 % (`Escandallo!B39`) · equilibrio contable 75,8 (`Punto Equilibrio!B15`), de caja 72,6 / 81,2 / 83,3
(`B20:D20`) · pesimista 359.900 € y −2.440,84 € (`Escenarios!B8/B20`) · calculadora: kilo útil 9,18 € (`Carne!B23`), 10 bolas y 9,7 con
merma (`B30/B31`), 15,2 kg/día (`B34`), umbral de picar 0,58 €/kg (`B36`), simple 1,80 € / 22,2 % y doble 2,90 € / 26,8 %
(`Escandallo!I21:K22`), menú 10,83 / 10,38 / 7,41 € (`N33:P33`), aceite 0,05 € por ración (`Patatas!B28`), 14 productos (`A21:A34`) ·
plancha 4.000 € (100 cm + tostador) y 771-1.399 € la de 60-80 cm (`Inversión Inicial!B12/D12`, Word [79]) · franquicias (Word [63]) ·
IAE [102] · carne picada y madurada [104] [112] · cocción [106] y checklist `F3!E10` · acrilamida y aceite [107] · IVA [108] · «sin
gluten» [50] [105] [113] · variantes del formato [46] · 9 hojas, 10 Heading 1, 80 tareas 12/15/14/13/13/13 con sus pestañas, 4 hojas de la
calculadora · Guía: «carne molida» `T2.2`, «papa» `T2.1`, «malteada» `T2.4`, «tocino/tocineta» `T2.7`, «domicilios»/«delivery» `T4.5`.

## 4. Gates (Mac, ligeros)

esbuild de los .ts tocados (ficha, verify-purchase, resend-access): OK · `sync-product-prices.py --check`: VERDE (99 productos; 59 del
catálogo) · `tienda-gate.py` (estático): VERDE · `nombre-gate.py --only`: ✅ · `gate-flujo-postpago.py --offline --only`: 5 entregables,
único ✗ = «sin Payment Link» (esperado hasta que John lo cree) · fuentes de la landing, dashboard y correo: 0 no latinos · sha256 de los
5 de `dl/` Mac = VPS (calculadora `8c911eea…`, checklist `1d061df4…`, guía `2461b232…`, Word `ec69d114…`, plan `ad0fad74…`).
**Pendiente con preview**: `tienda-gate.py --es-identico --base`, `gate-flujo-postpago.py --base … --crypto-products all
--crypto-exclude pro-prompts-ebook`, JSON-LD y tarjeta del use case `hamburgueseria` en el `dist`.

## 5. Revisión adversarial (Opus, una pasada) · 0 B · 3 M · 9 m, arreglados en la capa (los entregables no se tocan)

- **M1** Equilibrio: «los costes se cubren con unos 73 comensales equivalentes» (FAQ 2) y «para cubrir costes (unos 73 de los 95)»
  (tarjeta Punto de Equilibrio). 73 es el de caja del año de carencia (`Punto Equilibrio!B20`); los costes se cubren con 76 (`B15`) y la
  caja del año 2 pide 82 (`C20`) → 76 contable + 73 de caja el primer año, el de carencia, y 82 el segundo (= Word [40] [96]).
- **M2** FAQ de Latinoamérica con dos ejemplos que la Guía de Equivalencias no trae: «papas a la francesa» y «pan de patata» → «pan de
  papa» (la guía solo tiene «patata» → «papa», `T2.1`) → «la patata de las patatas fritas es papa en toda Latinoamérica» y «el bacon es
  tocino en México y tocineta en Colombia» (`T2.7`). Mismo arreglo en `equivalencias-es/datos/integracion.json`.
- **M3** FAQ de la freidora: «no prometer «patatas sin gluten» si comparten aceite» dejaba abierta la promesa con dos freidoras; el Word
  [50] y [113] dicen que no se promete (pan, plancha y utensilios compartidos) → «no prometer «patatas sin gluten»: el pan, la plancha
  y los utensilios se comparten».
- **m** variantes del formato «hamburguesa gourmet con servicio de mesa» / «solo para llevar o dark kitchen, gourmet de bola gruesa»
  (tarjeta del Word y correo) → «solo reparto a domicilio, servicio de mesa con bola gruesa y carrito» (= Word [46]; [50] evita
  «gourmet») · FAQ franquicia «el Word razona las dos cuentas» → «pone las dos cifras una al lado de la otra para que compares antes
  de firmar» (Word [63]) · 200.000-300.000 € atribuidos a emprendedores.es → «según los portales de franquicias» (Word [63]; R §0.8:
  solo La Pepita es de emprendedores.es), FAQ 1 y FAQ franquicia · cocción «no se usa para consumo crudo» → «no se sirve poco hecha»
  (checklist `F3!E10`) · plancha: la tarjeta de inversión daba solo 771-1.399 € → «el caso cuenta una de 100 cm con el tostador, 4.000 €»
  (`Inversión Inicial!B12/D12`) · «15 en vacuno al vacío» → «vacuno deshuesado y envasado al vacío» (853/2004, `LEGAL-F3.md` §2) · correo:
  «Sin inventar temperaturas legales que no existen y en el checklist» → «…, y con cada paso en el checklist» · venta cruzada con su
  precio «(12 €)» en el correo y en verify-purchase/resend-access (el dashboard ya lo decía).
- **Fuera de la capa, para el lead (no tocado)**: el Kit de Tareas Hamburguesería que se vende como «hermano» manda freír las patatas a
  175-180 °C (`01-apertura-cierre.xlsx` `Apertura Cocina!B16`, `02-partidas-cocina.xlsx` `Freidora!B7`) y cambiar el aceite «si está
  oscuro o huele» (`Freidora!B19`), y este plan dice < 175 °C (acrilamida, Word [107]) y cuenta «cambiar el aceite cuando huele» como el
  error n.º 5 [113]. Es un arreglo del kit (sin correo), no de este producto.
- Comprobado sin hallazgo: el resto de cifras y recuentos del §3, legal (ninguna temperatura legal de cocción; AESAN como
  recomendación; picada del día; polares < 25 % sin prohibir reponer; IVA del 21 % entero), restos de hermanas (solo el comentario del
  molde), nombres de los hubs sin palabras españolas, saludo y colores del correo, claves y ficheros de las functions = `dl/`, enlaces
  internos (`/kit-tareas-hamburgueseria`, `/guia-dark-kitchen`, `/kit-escandallos`, `/plan-negocio-food-truck` existen) y precios de la
  venta cruzada (Kit de Tareas 12 €, Kit de Escandallos 12 €).
