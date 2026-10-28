# Coffee Cart Business Plan Kit (EN, $39) — research US DELTA (F1 · 28-oct-2026 · sesión Claude Code)

> UNA pasada. Lo común (sales tax como parámetro, payroll taxes, FLSA, SBA 7(a) / Microloan, DSCR, income tax, NOL, MACRS,
> UK base) = `../business-plans-en/F1-research-us.md` §3-§5 (**BP §n**; trae además el Coffee Shop y el Food Truck EN:
> commissary, health permit + plan review, fire marshal, SharpSheets); service charge vs gratuity, sales tax del caterer,
> W-2 vs 1099 = `../business-plans-en-4/` (**CAT §6**); COI / additional insured, dry hire, motor de eventos = `../business-plans-en-5/`
> (**MBAR**, el hermano más cercano); furgoneta + commissary de eventos = `../business-plans-en-7/` (**PAEL**): **✅ hermano, no se repite**.
> Fuente ES = `../plan-cafeteria-movil/` (vacío a la hora de este F1: el ES se construye hoy en paralelo; cifras ES NO reutilizables, §8).
> Etiquetas: **[medido 28-oct]** = DataForSEO US (`--pais 2840 --idioma en`) o API pública (BLS) · **[leída 28-oct]** = página
> abierta · **(resumen)** = resumen de búsqueda, página no abierta · **Kit estimate** = cálculo a la vista · ❌ = no hallado.

## 0. 🔴 Hallazgo transversal: la serie de DataForSEO va de MÁS RECIENTE a más antiguo

`scripts/dataforseo.py vol` imprime `monthly_searches[:6]` tal cual llega, y la API los da **del mes más reciente hacia atrás**
(comprobado con año/mes en la respuesta: `(2026, 9, 90), (2026, 8, 210) … (2025, 10, 880)`). Por tanto «coffee truck business
plan 90 → 880» **no sube: baja** de 1,300 (ene-2026) a 90 (sep-2026). Lo mismo con «wedding venue business plan» (WV §2 leyó
«×3,8»: en realidad 1,900 oct-25 → 260 sep-26, verificado hoy) y, con la misma salida del script, probablemente con «mobile bar
business plan» (MBAR §2, «90 → 210»; hoy 390 oct-25 → 50 sep-26). Todas las
keywords «… business plan» tienen **pico en enero** y valle en verano-otoño (food truck business plan: 40,500 en ene-26 frente a
2,400 en sep-26). **Consecuencia**: no afirmar «demanda creciente» en ningún sitio; lanzar a finales de octubre deja la landing
indexada antes del pico de enero (bien). Recomendado (fuera de este F1): rotular la columna del script «más reciente primero».

## 1. Concepto: **coffee catering company** con **dos estaciones de espresso** (cart + portable bar), sin camión

Empresa de **café de especialidad para eventos**: un **espresso cart** con fregadero de manos, depósitos de agua limpia y gris y
nevera bajo barra + un **portable espresso bar** para la segunda estación y los salones interiores; los dos viajan en un
**remolque cerrado** que arrastra el vehículo del dueño. Vende **servicio hosted** (paga el anfitrión): baristas W-2, espresso,
batch brew, cold brew, leches (incluida la de avena), siropes, vasos compostables, montaje y recogida; extras: horas, branded
cups / latte printing, desplazamiento, bollería de obrador con licencia. **Tres motores**: **empresa** (entre semana: oficinas,
conferencias, trade shows, brand activations), **bodas** (fin de semana, ticket alto) y **fiestas privadas**; **mercados y
festivales** en modelo **guest-pay con minimum sales guarantee**, como complemento. Base en una **commissary**.

**El dato que manda el posicionamiento**: en 25,860 reservas reales, **69,3 % son corporativas entre semana** y solo ≈ 31 %
fines de semana (bodas y privadas) (Flashquotes, §5) → «events-first», sí, pero **la empresa es el volumen y la boda el ticket**.
Es la diferencia con el Mobile Bar (85 % viernes-domingo, mitad en sábado): aquí la capacidad entre semana existe y se vende.

**Qué cambia vs. ES** (confirmar cuando exista el ES): IVA → **sales tax** como parámetro (`B39`) · licencia y registro sanitario →
**business license** + **mobile food unit permit con plan review** + **commissary agreement** (§6) · baristas autónomos → **W-2 hourly**
· litros/euros → **lb, oz, gal, °F, USD** (gramos solo en la dosis, con su oz) · feria municipal → **festival / farmers market** con
*vendor fee* + **temporary event permit**.

**Fuera de scope (FAQ)**: **coffee shop con local** (Coffee Shop Business Plan Kit), **food truck de ruta diaria** con comida
(Food Truck Business Plan Kit), **espresso martini / alcohol** (licencia; socio con el Mobile Bar Kit), drive-thru coffee stand.

## 2. Demanda (DataForSEO US [medido 28-oct]; vol. = media de 12 meses; serie cronológica oct-25 → sep-26)

| Keyword | Vol. | Comp. | Serie (oct-25 → sep-26) | Uso |
|---|---|---|---|---|
| **coffee truck business plan** | **720** | LOW | 880 · 720 · 590 · **1,300** · 1,000 · 880 · 880 · 880 · 480 · 390 · 210 · 90 | descriptor: H2, FAQ, meta, schema |
| **coffee cart business plan** | **320** | LOW | 720 · 590 · 480 · 590 · 260 · 320 · 390 · 320 · 140 · 140 · 90 · 110 | **cabeza**: slug, H1, title |
| coffee trailer business plan · mobile coffee business plan · coffee truck / cart business plan template | 170 · 40 · 30 · 20 | LOW-MED | 260 → 50 · 30 → 10 (pico ene) | H2 de formato, keywords, title («template») |
| coffee cart business · coffee truck business · mobile coffee business | 880 · 170 · 210 | HIGH · LOW · MED | estables | intro, subtítulo |
| how to start a coffee cart business · … mobile coffee … · … coffee truck … | 140 · 90 · 70 | LOW-MED | estables | H2 + FAQ |
| coffee cart for events · coffee cart catering · coffee bar for wedding · coffee cart for weddings | 720 · 590 · 720 · 210 | HIGH-MED | estables | **intención del cliente del operador**: alt, H2 de precios, no cabeza |
| coffee truck for events · coffee truck catering · espresso catering · coffee bar catering | 170 · 170 · 110 · 210 | MED-HIGH | — | idem: «cart» gana a «truck» ×3-4 en eventos |
| coffee catering · mobile coffee bar · mobile espresso bar | 2,900 · 880 · 260 | MED · HIGH | estables | jerga (§9) y cuerpo |
| coffee truck startup costs · how much does a coffee cart cost · … to start a coffee truck · coffee cart cost · … startup costs | 90 · 50 · 50 · 40 · 20 | LOW-MED | — | H2 de costes, FAQ |
| coffee cart pricing · coffee cart menu | 70 · 110 | HIGH | — | H2 de la calculadora |
| coffee cart permit · … license · … insurance · is a coffee truck profitable · how much do coffee carts make | 90 · 30 · 30 · 20 · 10 | LOW-HIGH | — | FAQ legal y de rentabilidad |
| coffee cart / truck / trailer **for sale** · coffee cart · coffee truck · mobile coffee cart | 3,600 ×3 · 18,100 · 8,100 · 6,600 | HIGH | — | compra de equipo / consumidor: **no se atacan** |

**Lectura**: la cabeza combinada (truck 720 + cart 320 + trailer 170) ≈ **1,200/mes de media**, mayor que el Mobile Bar (210) y
comparable al Wedding Venue; **estacional con pico en enero**, no creciente (§0). En la familia de eventos, **«cart» es la palabra
del evento** (coffee cart for events 720 frente a coffee truck for events 170; coffee cart catering 590 frente a 170).

## 3. SERP y PAA (DataForSEO US [medido 28-oct])

- **«coffee truck business plan»** (141 res.): **AI Overview** — «requires a clear vehicle format, strict health compliance, and
  **separate financial tracking for daily street vending versus private catering**»; formatos con rango («Coffee Cart / Push
  Cart ($5,000 – $20…», truncado). Orgánicos: Reddit, **Toast** (nov-2024), Premierline (UK PDF), SumUp, Taxfyle, Perfect Daily
  Grind, Facebook ×2, Slideshare, Green Joe, Pinterest ×2, Haven, **Financial Models Lab (Word)**, WebstaurantStore. Relacionadas: *template · pdf free download · free · for sale · price · near me*.
- **«coffee cart business plan»** (126 res.): AI Overview asíncrono (sin texto) + vídeo. bizzonwheels («a credible coffee cart
  business plan … sets out capital expenditures, operating costs, pricing…»), Premierline, YouTube ×2, Medium, dmvbarista
  (roadmap, mar-2026), Pinterest, coffeemachinedepot, Slideshare, Facebook, aerobuild, **bizplanner.ai (gratis, generador)**,
  Scribd, Toast, Haven. Relacionadas: *template · business for sale · mobile coffee cart · coffee trailer · **coffee cart business for events***.
- **«how to start a coffee cart business»**: AI Overview «requires a clear business concept, local health permits,
  commercial-grade equipment, and a focused menu… **setup costs between $5,000 and $25,000**» (cita cart-king, torque.coffee).
  Reddit: «Coffee carts require the same city and county permitting as food trucks and a registered commissary because they
  utilize dairy products» (CA). Relacionadas: *in california · in texas · with no money · DIY · plans PDF*.
- **«coffee cart catering»** (local pack + 20 operadores: Coffee Cart Boys LA, Jam'nBean MI «packages start at $675», Poema,
  Goodhart, Yelp Denver, Flipside, Filter & Shot, 1996 Coffee Co, Icon Austin, Big Dipper ABQ «begin at $400», The Ark NYC…).
  **PAA**: «**Do you need a commissary kitchen for a coffee cart?**» (el resto, de consumidor de cafetería: no se atacan).
- **Hueco**: la SERP son guías de pasos, plantillas Word sueltas y generadores gratis. **Nadie junta Word + Excel que recalcula +
  calculadora por invitado/hora + checklist** para el **operador de eventos** (el AI Overview pide separar street vending y
  catering: el kit es el lado catering, y lo dice). **Ángulo**: «price per guest, staff by drinks per hour, survive July».

## 4. Costes de arranque US

### 4.1 Formatos y equipo

| Concepto | Dato | Fuente |
|---|---|---|
| Arranque típico de un carro | **$5,000-$25,000** | AI Overview «how to start a coffee cart business» [medido 28-oct] |
| Carro nuevo básico · custom premium · adaptación | **$4,000-$10,000** · **$15,000-$25,000** · $500-$8,000 | cart-king.com/…/coffee-cart-startup-costs-complete-financial-guide-2025 (15-oct-2025) [leída 28-oct] |
| Total de un carro (típico · premium) | **$24,000** (carro $6,000 + equipo $6,500) · **$49,000**; conclusión «$16,600 to $49,000» | ídem |
| Espresso · molino · agua · frío · POS · licencias | $1,500-8,000 · $300-3,000 · $400-2,000 · $300-2,500 · $300-1,500 · business $50-400, mobile vendor $100-800/año, food handler $10-50, LLC $100-500 | ídem |
| Carro de demostración (Prima, Lucca A53, enchufado sin generador) | **≈ $8,000-$10,000** todo incluido | prima-coffee.com/blog/building-a-coffee-cart (27-ago-2024) [leída 28-oct] |
| Remolque de café | **≈ $15,000 construirlo + ≈ $10,000 equiparlo**; desde $10,000; camión ≈ $20,000; custom truck hasta **$80,000** | greenjoecoffeeschool.com (28-dic-2019, antiguo) [leída 28-oct] |
| Espresso 2 grupos (Nuova Simonelli Appia Life 2 Gr, 220 V, **3,400 W**, 15.5-17 A, NEMA 6-20P) · La Marzocco Linea Classic S 2 Gr | **$8,505-$8,990** · compacta 2 Gr $7,200 (14 A) · Linea **$12,730** (EE) / $16,670 (AV) | webstaurantstore · chefsdeal · katom · espressoparts (resumen) |
| Generador inverter 5,500 W continuos (Honda EU7000is) | MSRP **CAD 5,328** (precio US no leído ❌) | concesionario canadiense (resumen) |

**Lectura (Kit)**: el coste lo mandan **la máquina de 2 grupos** (≈ $8.5K) y **la energía**: una 2 grupos a 220 V/3,400 W + molino
+ nevera pide un generador de ~5.5 kW o el enchufe de la sala (Icon trabaja con «a standard 110V outlet» y máquina compacta).
El caso (§8) sale en **≈ $71,500** por llevar **dos estaciones** y remolque: por encima del carro único ($16.6-49K) y por debajo
de un coffee truck custom ($80K) o un coffee shop con local ($80-300K, ✅ BP §3). **Lean** para la FAQ: un carro, máquina usada, enchufe de sala ≈ **$16,600-$24,000** (cart-king).

### 4.2 Insumos y rendimientos

| Concepto | Dato | Fuente |
|---|---|---|
| Café molido, media nacional retail | **$9.332/lb** (sep-2026; $9.457 jun-2026) | BLS APU0000717311 [medido 28-oct] |
| Café de especialidad mayorista | ≈ **$18/lb** (5 lb a $90, Majesty Coffee); bolsa retail de especialidad mediana $18-20 | (resumen) |
| Leche entera | **$4.106/gal** (sep-2026) | BLS APU0000709112 [medido 28-oct] |
| Coste por bebida (todo incluido) | **$0.75-$1.50**: doble $0.25-0.45 · leche $0.20-0.40 (12 oz) · **avena/almendra $0.60-1.10** · vaso+tapa+funda $0.20-0.45 · sirope $0.05-0.15/pump · +10-15 % merma; objetivo **COGS 20-30 %** del ingreso por bebida | grindkit.app/guides/private-event-pricing (abr-2026) [leída 28-oct] |
| Coste por bebida (ejemplo de operador) | ≈ **$0.70** × 100-170 bebidas = $70-120 por evento | flashquotes.com/blog/coffee-cart-catering-cost (20-abr-2026) [leída 28-oct] |
| Dosis y rendimiento | doble **18 g = 0.63 oz** → 1 lb (453.6 g) = **25 dobles brutos**, ≈ 23 netos con purga y dial-in; ratio 1:2 (18 g → 36 g) | Kit estimate (aritmética) + ratio 1:2 (resumen) |
| **Kit estimate del caso** | café **$14/lb** (entre BLS retail y mayorista de especialidad) = **$0.56/doble** · leche 8 oz = **$0.26** · avena **$0.85** (25 % de las bebidas con leche) · 80 % de bebidas con leche → ingredientes **≈ $1.03/bebida** con 10 % de merma · desechables compostables **$0.30/bebida** + $0.04 servilletas | cálculo a la vista |

**Bebidas por invitado** (GrindKit [leída]): ≤ 2 h **1.0** · 2-4 h **1.3-1.5** · 4-6 h 1.5-1.8 · 6+ h 2.0-2.5; mañana +20-30 %;
Flashquotes: ≈ 1.5 por la mañana, 2+ en eventos de día entero. **Caso: 1.4** → ingredientes **$1.45/invitado (11.5 % de $12.60)**,
desechables **$0.46 (3.7 %)**.

## 5. Mercado y precios US

### 5.1 Benchmark principal: Flashquotes, 25,860 reservas de 578 operadores (abr-2023 → abr-2026, ≈ $42M) [leída 28-oct]

| Dato | Valor |
|---|---|
| Reserva típica | **mediana $1,040** · P25 $764 · P75 $1,697 · P10 $612 · P90 $3,000 · media $1,640; evento típico **100 invitados** |
| Por tamaño (media $/invitado) | < 50 (30 inv.): $913 = **$38.11** · 50-99 (62): $1,074 = **$17.87** · 100-249 (132): $1,746 = **$13.44** · 250-499 (314): $3,384 = $10.65 · 500+: $9.62 |
| Por tipo | drop-off / self-serve cold brew $612-764 · pequeño con barista < 50 inv. $764-1,040 · estándar 2 h 50-100 inv. $1,040 · empresa 100-200 inv. 2-3 h $1,040-1,697 · **boda premium / brand activation $1,697-3,000** · contrato corporativo varios días $3,000-10,000 |
| Duración | **2 h = 55,3 %** (estándar) · 1 h 13,6 % · 3 h 17,7 % · 4 h 7,3 % · 5+ h 6,1 % · multi-día 10,1 % |
| Precio por componentes | base **$300-500** + **$150-200 por hora de servicio**; desplazamiento **$1.25/milla ida y vuelta** |
| Coste del operador (ejemplo) | turno de 8 h × **$25/h** = $200 + bebidas $70-120 + viaje $30 ≈ $300-330 → precio 2-3× → **margen bruto 50-70 %**; «under $250 for a 2+ hour event» = sospechoso; **3 h de evento ≈ 8 h de turno** |
| Capacidad | **1 carro + 1 barista: 50-65 bebidas/h** máx.; 2 + 2 ≈ 100/h; 2-3 baristas para ~250 invitados |
| Conversión · antelación | presupuestos → reservas **20-30 %** (> 30 % = barato) · mediana **41 días** (25 % < 17; 25 % > 116) |
| Mezcla | **69,3 % corporativo entre semana** · ≈ 31 % fines de semana (bodas y privadas) |
| **Estacionalidad** (% reservas/año) | ene 7,0 · feb 8,8 · **mar 11,2** · abr 10,8 · **may 10,9** · jun 5,9 · **jul 3,8** · ago 5,3 · sep 7,3 · oct 9,5 · nov 7,9 · **dic 11,7** |
| Ojo | solo reservas de la plataforma: ≈ **15 reservas/operador/año** de media (25,860 / 3 años / 578), **no** el total del operador (Kit: no se cita como dato de eventos/año) |

### 5.2 Otras fuentes de precio (operadores y guías, 2026)

| Oferta | Precio | Fuente |
|---|---|---|
| GrindKit, rejilla 2 h hosted all-inclusive (metros secundarios) | 50 inv. **$700** · 100 inv. **$950** (1-2 baristas) · 150: $1,350 · 200: $1,800 (objetivos); **$5-11/invitado a 100 inv.** «sano», < $5 = pérdida; hora extra +$175-275; 2.º barista +$250-400; urbano +20-40 % | grindkit (abr-2026) [leída] |
| GrindKit, condiciones | **retainer 30-50 % no reembolsable**; saldo 14 días antes; recuento final 10 días antes; radio gratis 20-30 millas, luego $1-2/milla; generador $100-300/día; GL $1M/$2M ≈ $600-1,800/año | ídem |
| Houston Coffee Cart (Zola) | **$1,000** (1 barista, 2 h) · **$1,500** (2 baristas, 2 h); avena incluida «at no additional cost»; > 30 millas, recargo | zola.com/…/houston-coffee-cart [leída] |
| Sweet Carolinas (Zola) | «Full-Service Espresso Bar» **$500** (2 h, ≤ 75 inv.) + **$5/pp** desde 75; avena incluida; **«additional alternative milk» $50** · cold brew $100 · +½ h $75 | zola.com/…/sweet-carolinas-coffee [leída] |
| Big Dipper (Albuquerque) | Pop-Up desde **$400** (1 h, 1 barista) · Premium Cart **$800** (2 h, ≤ 80 bebidas, 2 baristas) · Airstream $1,800; público: **minimum sales guarantee** (paga el organizador la diferencia) | bigdippercoffee.com/services [leída] |
| Icon Coffee Cart (Austin) | «Packages start at **$850**», all-inclusive, «unlimited made-to-order espresso drinks during your booked service window» | iconcoffeecart.com [leída] |
| Coffee Cart Boys (LA/OC) | «**50 cups per hour**», «1-hour setup», «no hidden generator or setup fees» | coffeecartboys.com [leída] |
| Guía de bodas 2026 | carro con barista **$700-1,800** por boda típica; premium $1,500-2,500+; self-serve $2-5/invitado | affordableweddingvenuesandmenus.com (jul-2026) [leída] |

**Sueldos** (BLS OEWS **May 2025**): **no hay ocupación «barista» propia**: desde SOC 2018 está dentro de **35-3023 Fast Food and Counter
Workers** (O*NET 35-3023.01 Baristas, resumen): 3,854,050 empleos · **mediana $15.00/h** · media $15.46 · p10 $10.98 · p25 $13.32 ·
**p75 $17.34 · p90 $20.51** (api.bls.gov OEUN0000000000000353023{01,03,04,06-10} [medido 28-oct]). El barista de eventos cobra más:
Flashquotes modela **$25/h**, GrindKit **$20-35/h** → caso **$19-22/h** + propinas voluntarias.

**Seguros**: GL de cafetería ≈ **$752/año** ($1M/$2M; resumen insureon/moneygeek); vendor por evento **$49 (1-3 días)** o anual desde
**$25.92/mes**, «Unlimited Additional Insureds» (Insurance Canopy, resumen); commercial auto $600-1,500 y workers' comp $300-800 por
empleado (cart-king [leída]). **Sin liquor liability** (no hay alcohol). Las salas y organizadores piden **COI** con ellos como
**additional insured** (✅ MBAR §6.4; Roaming Hunger, resumen). **Arizona** prohíbe a las ciudades exigirlo salvo eventos municipales o
vía pública (A.R.S. 9-485.02, resumen).

**Umbrales del P&L** (`3-Year P&L!E51:E56`, Kit): margen bruto del motor **≥ 72 %** · mercancía + desechables **≤ 20 %** · personal
**≤ 40 %** (con el sueldo del dueño) · commissary **≤ 6 %** · neto **≥ 5 %**.

## 6. Marco legal y operativo US delta (lo propio del café; el resto = BP §5, CAT §6, MBAR §6)

1. **Permiso sanitario de unidad móvil + plan review (condado)**: un carro es *mobile food unit* (WA, IN) o *mobile food facility* (CA),
   mismo trámite que un food truck. **Snohomish County (WA)**: plan review **$1,100**, permiso anual **$500 / $745 / $1,025** según riesgo,
   aprobación previa de **L&I** (electricidad) [leída]; **Alamance County (NC)**: plan review **$250** para *mobile food units and push
   carts* (resumen). **Leche = TCS** (≤ **41 °F**, Sonoma, resumen) → nevera aprobada a bordo; agua potable + grises y **lavamanos** según
   condado (❌ volúmenes no leídos); máquina en **circuito dedicado** (Prima [leída]), 2 grupos a **220 V / NEMA 6-20** → la checklist
   pregunta a cada sala «110V or 220V, how many amps, how far».
2. **Commissary (la PAA del nicho)**: el **FDA Food Code deja la decisión a la autoridad local** (su *mobile matrix* la condiciona al
   menú, la operación y el equipo a bordo: job aid de Missouri DHSS, resumen; ❌ texto no abierto). **CA**: Health & Safety Code
   **§114295**, las MFF «shall operate in conjunction with» una commissary; Sonoma: volver cada día de operación (resumen). **WA**: «All
   mobile units must have a commissary kitchen» **salvo la exención de RCW 43.20.148**, acuerdo anual y **commissary log** a bordo
   (Snohomish [leída]). → FAQ: «**usually yes**; some counties exempt self-contained units: ask yours before you buy the cart».
3. **Bomberos**: sin vapores grasos → normalmente **sin campana Tipo I** ni el permiso IFC de *mobile food preparation vehicles* (§319;
   105.6.30 en IFC 2018 / 105.5.32 en 2021, ligado a «appliances that produce smoke or grease-laden vapors») (resumen). **Generador y
   propano sí**: generador no montado **≥ 12 ft** (NFPA 96 §17.6.2, checklist de Lenexa KS), 10 ft de edificios (§17.2), extintor; NJ pide
   **Fire Safety Permit** con generador en cada montaje; Tulsa emite carta de «no permit needed» (resumen).
4. **Business license** + **sales tax permit** + **food handler cards** de todo el equipo (Baker County OR, resumen) y, según condado,
   **Certified Food Protection Manager** (✅ BP §5); ferias: **temporary event permit** por evento.
5. **Sales tax**: **hosted** = servicio de catering (gravado en CA aunque no se ponga la comida, y en NY: ✅ CAT §6.2); **guest-pay**
   (mercados) = venta de bebida preparada, se cobra bebida a bebida y puede exigir registro donde se vende. → `B39` = **8 % sobre toda la
   factura** (ejemplo editable) + nota «rate and taxability depend on your state and on who pays». Nunca la regla de un estado como general.
6. **Bollería**: la **cottage food** se vende directa del productor al consumidor; la reventa por un establecimiento suele quedar fuera
   (Texas 2025: HB 520 y SB 541 excluían los *baked goods* de tiendas y mayorista, ❌ texto final no confirmado) → **obrador con licencia**.
7. **Vasos (local)**: **Seattle** exige single-use **compostable** onsite (incluye coffee shops y food trucks), foam prohibido desde 2009;
   WA no da tapas de bebida fría por defecto (RCW 70A.245.080) (seattle.gov, resumen) → el kit presupuesta compostable y lo marca local.
8. **Personal**: **W-2 hourly** (✅ CAT §6.5); bote de propinas sin el riesgo de «venta» del MBAR §6.1 (no hay alcohol); *service charge*
   ≠ gratuity (✅ CAT §6.3). **Alcohol**: el *espresso martini bar* sale entre los *specialty bars* de bodas (✅ MBAR §9e) pero exige
   licencia → **fuera** (`B62` = 0 %), «partner with a licensed mobile bar».
9. **UK (breve)**: registro en el council **28 días antes** de operar (FSA, por verificar) · *street trading licence/consent* (✅ glosario)
   · IVA **20 %** en bebida caliente (HMRC Notice 709/1, por verificar) · guía NCASS del café móvil y «as little as **£5,000**» (Premierline, SERP).

## 7. Competencia y precio

| Oferta | Precio | Qué es | Fuente |
|---|---|---|---|
| Financial Models Lab «Coffee Truck Business Plan Template» | **$59** (antes $79) | solo Word; financieros dentro del Word; Excel aparte; enfoque oficinas/transporte/eventos | financialmodelslab.com/products/coffee-truck-business-plan [leída] |
| Startup Financial Projection «Specialty Coffee Cart Financial Model» | **$99** ($129) | Excel 5 años + pitch deck + plantilla Word | (resumen) |
| Flevy «Food Truck and Coffee Truck Startup Financial Model» | **$99** | XLSX + PDF | (resumen) |
| SharpSheets Coffee Shop (modelo / plan) | $119 / $79 | café con local | ✅ BP §6 |
| bizplanner.ai · Toast · Medium · Slideshare · Pinterest | gratis | generador / guías / ejemplos | SERP §3 |

**Precio $39** (escalera de planes EN): por debajo del Word solo ($59) y de los Excel solos ($99), con lo que nadie junta. Sin tachado,
sin «worth $X», sin ratings.

## 8. Caso de ejemplo US (celdas del libro de eventos EN, conjunto `cat`, como MBAR y PAEL; si el ES 2.2 usa otro libro, F1-inventario remapea)

Todo **Kit estimate** salvo §4-§6. D15 = MBAR §8 (DSCR ≥ 1.25, caja mín > 0, cobertura ≥ 98 %, holgura ≥ 15 %). **A mano** (F2
recalcula): ventas a régimen **$203,490** (170 × 95 × $12.60; 16,150 invitados; **$1,197/evento**, entre la mediana $1,040 y el P75
$1,697 de Flashquotes) · mercancía 13,95 % (85 % × 12 % + 15 % × 25 %) + desechables 4 % + marketplace 1 % + tarjeta 3 % + varios 3 % →
**margen bruto del motor ≈ 75 %** · personal **≈ $74,500 (36,6 %)** · commissary 4,1 % · suministros, seguros y fijos $26,000 (12,8 %) ·
**EBITDA ≈ $43,800 (21,5 %)** · D&A ≈ $10,800 · intereses ≈ $6,900 · antes de impuestos ≈ 12,8 % · **neto ≈ $19,600 (9,6 %)** ·
**CAPEX ≈ $71,500** · necesidad con 3 meses de fijos ≈ **$98,700** → propios **$30,000 (30 %)** + préstamo **≈ $68,700 (CALIBRAR;
SBA 7(a), 10 %, 7 años; no cabe en el Microloan de $50K salvo +$18,700 de propios)** · cuota ≈ $14,100 · **DSCR ≈ 3,1** · break-even ≈
**141 eventos/año** → **holgura ≈ 17 %**. Calibración: holgura < 15 % → `B4` +10 hasta 190; caja mín ≤ 0 en julio → `B35` 3 → 4 meses
antes que tocar precio; anotar en `F2-NOTAS`.

**Mezcla** que sostiene el promedio: **110 empresa** (90 inv. × $12 = $1,080) · **30 bodas** (130 × $15 = $1,950) · **20 fiestas privadas
y showers** (45 × $20 = $900) · **10 mercados/festivales guest-pay** (≈ 150 bebidas × $6.50 = $975, con minimum sales guarantee) =
170 eventos, $205,050, 95,3 invitados, $12.66 (celdas −0,8 %) → empresa **65 % de eventos y 58 % de ventas**; bodas 18 % y 29 %.
**Posición honesta**: un operador **a tiempo completo con venta corporativa activa** y dos estaciones; Flashquotes da ≈ 15 reservas
por operador y año **solo en su plataforma**; el docx dice que el primer año es más lento (rampa) y que **julio vende la tercera parte
de diciembre**. Orden de magnitud: por debajo del Mobile Bar ($212.8K) y de la Paella ($313K), con más margen bruto (café ≈ 12 %
de coste frente a 19-29 %). **Cifras ES prohibidas (gate)**: añadirlas cuando exista `../plan-cafeteria-movil/` + «autónomo» ·
«freelance» · «IVA» · «feria municipal» · «litros» · «€».

| Celda (rótulo catering → coffee cart) | Catering | **Coffee catering US** |
|---|---|---|
| `0. Assumptions!B4` Events per year · `B7`/`B8` crecimiento | 180 · 15 / 10 % | **170** · **10 / 6 %** |
| `B5` Average revenue per guest (excl. sales tax; incl. travel & extras; excl. voluntary gratuity) · `B6` Guests per event | $60 · 60 | **$12.60** · **95** (Flashquotes: evento típico 100) |
| `B11` línea 1 → **Coffee bar packages (baristas, espresso drinks, batch & cold brew, milks, syrups, cups)**; resto → **Add-ons (extra hours, branded cups & latte printing, pastries, travel fees)** | 88 % | **85 / 15 %** |
| `B13` / `B14` coste línea 1 / 2 · `B15` → **Compostable cups, lids, sleeves & napkins** | 30 / 25 % · 3 % | **12 / 25 %** · **4 %** |
| `B16` / `B17` **Marketplaces (GigSalad, Thumbtack, The Bash, Zola)** · `B18` tarjeta | 10 / 15 % · 2,5 % | **20 / 5 %** · **3 %** |
| `B24` → **Commissary, cart storage & trailer parking** · `B25` fianza | $2,500 · 1 | **$700/mes** (cart-king $200-600 + almacén) · 1 |
| `B26` suministros · `B27` seguros · `B28` varios | $250 · $6,000 · 3 % | **$100** · **$3,800/año** (GL $750 · auto/remolque $1,500 · workers' comp $800 · equipo $500 · margen) · **3 %** |
| `B30` · `B31` · `B32`-`B35` | $40,000 · CALIBRAR · 10 % · 7 · 0 · 3 | **$30,000** · CALIBRAR (≈ $68,700) · 10 % · 7 · 0 · 3 |
| `B44` / `B45` vidas (remolque y fit-out / equipo de café) · `B48` | 5 / 7 · 0 | **7 / 5** · 0 |
| `B51` → **Max events a year your stations and baristas can handle** | 250 | **350** (2 estaciones; entre semana libre) |
| `B52`/`B53` rampa · `B54` · `B55` | 0,50 / 8 · 1 · 10 % | **0,45 / 9** · **1** · 10 % |
| `B58` cobro · `B62` alcohol · resto (`B20`-`B22`, `B68`, `B37`-`B42`, `B59`, `B63`, `B65`-`B67`) | 14 · 0 % · … | **14** (empresa net-15/30; bodas prepagadas) · **0 %** · ídem MBAR (W-2; `B39` 8 %, §6.5) |

**Personal** (`Staffing!B5:D8`; D = personas × FTE × 173,33 h × $/h): **Owner / Lead Barista & Sales** 1 × 1.0 **$3,813** ($22/h; > p90
BLS 35-3023) · **lead barista (part-time W-2)** 1 × 0.3 **$1,040** ($20) · **event baristas (hourly W-2)** 3 × 0.08 **$790** ($19 +
propinas) → 5 personas, **1.54 FTE, $5,644/mes** (+10 % cargas = $74,500/año). **`B18` = 7 h** por persona y evento (carga en la
commissary, viaje, montaje ~1 h, **2-2,5 h de servicio**, recogida, limpieza; GrindKit «7-9 h» por un evento de 2 h) · **`B19` = 1,6**
(1 barista por ~50-65 bebidas/h; bodas y empresa grande, 2) → 1,904 h frente a 3,203 (168 %; ≈ 121 % sin ~900 h del dueño en ventas).
Años 2 / 3: $3,000 / $3,000.

**Inversión** (`Startup Costs!B7:B20`): 7 **espresso cart** (NSF, hand sink, fresh/gray water tanks) **$12,000** · 8 **portable espresso
bar** (second station) $4,000 · 9 **espresso machines**: 2-group volumetric 220 V ($8,500) + compact 2-group ($7,200) **$15,700** · 10
**espresso grinders ×4** (house + decaf) $4,800 · 11 **inverter generator (5,500 W) + cords & power distribution** $5,000 · 12 water pumps
& filtration + undercounter fridges $2,800 · 13 **enclosed cargo trailer** 6×12 with ramp door + wrap, hitch & tie-downs $8,000 · 14
batch brewer, airpots, cold brew system & smallwares (pitchers, scales, tampers, knock boxes) $2,500 · 15 LLC, contracts & legal $1,500 ·
16 first-year permits & plan review (health, food handler/manager, fire/generator) $2,500 · 17 POS, card readers & booking software $1,000 ·
18 opening inventory (beans, milks, syrups, compostable cups) $1,500 · 19 website, photos, tastings & launch (corporate open house,
bridal show) $5,000 · 20 commissary storage fit-out $800 → **$67,100** + fianza $700 + 1 mes previo $700 + 10 % sobre 7, 8, 11, 13, 20
($2,980) ≈ **$71,500**. **Vehículo de arrastre = el del dueño ($0)**, nota: si no, furgoneta usada ≈ $18,000 (PAEL). **Fijos**
(`3-Year P&L!B26:B35`, $21,000): permits renewal & event permits $1,500 · vehicle & trailer fuel, maintenance & registration $3,500 ·
marketing (Google Business Profile, corporate outreach, The Knot/Zola, marketplace listings) $8,000 · accounting $2,400 · software
(quotes/booking/CRM, POS, e-sign) $1,500 · **espresso machine service, water filters & grinder burrs** $1,800 · phone & internet $900 ·
staff training & tastings for prospects $800 · linens, signage & smallwares replacement $600 · (fila 10 libre).

**Estacionalidad** (`12-Month Cash Flow!B5:M5`) = **Flashquotes** (ene→dic, mar 11,2 → 11,1 para sumar 100): 7,0 · 8,8 · 11,1 · 10,8 ·
10,9 · 5,9 · **3,8** · 5,3 · 7,3 · 9,5 · 7,9 · **11,7**. Apertura en **marzo** → Mes 1-12 = **11,1 · 10,8 · 10,9 · 5,9 · 3,8 · 5,3 · 7,3
· 9,5 · 7,9 · 11,7 · 7,0 · 8,8 %**. Valle de verano = lo contrario del Mobile Bar → la caja mínima puede caer en julio-agosto (prueba
del D15). **Escenarios** (`Scenarios!B5:D7`, ±25 % / ±10 %): pesimista **128 eventos · $11.34 · 86** (≈ $124.8K: EBITDA ≈ −$15K, el
docx lo dice) · optimista **212 · $13.86 · 105** (≈ $308.5K). `Break-Even!B31/D31/E31`: pasos **±$1 / +$2** por invitado.

## 9. Jerga profesional US (glosario OBLIGATORIO de los redactores; se añade a `../GLOSARIO-JERGA-ES-EN.md`)

**(a) Nombre del negocio.** El operador se llama a sí mismo **coffee catering** + **mobile espresso bar / mobile coffee cart** (Icon:
«Mobile Espresso Bar», «mobile coffee cart»; Big Dipper: «coffee cart and coffee truck services»; Houston: «coffee catering»
[leídas]); DFS: coffee catering 2,900 · coffee cart business 880 · mobile coffee bar 880 · mobile espresso bar 260. **Regla**: «coffee
cart» en nombre, slug, H1 y ficheros; «coffee catering» y «mobile espresso bar» en subtítulo y cuerpo; «coffee truck» y «coffee trailer»
como **formatos** (H2 y FAQ), nunca como nombre. **Falso amigo**: «cafetería» ≠ *cafeteria* (en US = comedor de colegio/empresa): nunca
«mobile cafeteria»; «café» solo en *café* = local.

| # | ES (cafetería móvil para eventos) | Término US | Fuente / estado |
|---|---|---|---|
| 1 | Servicio de café para eventos | **coffee catering** · **coffee cart catering** | Houston, CCB [leídas]; DFS 2,900 / 590 |
| 2 | Barra con baristas · estación sin barista | **full-service espresso bar** · **self-serve coffee station** / **drop-off** (cold brew) | Sweet Carolinas, Flashquotes [leídas] |
| 3 | Carro · remolque · camión · bici · furgoneta | **espresso cart / coffee cart** · **coffee trailer** (Airstream) · **coffee truck** · coffee bike · coffee van | DFS 480 · 4,400 · 8,100 · 590 · 590; Big Dipper [leída] |
| 4 | Barra portátil · barista jefe · de evento | **portable espresso bar** · **lead barista** · **event barista** | por verificar (MBAR «portable bar») |
| 5 | Bebidas sin límite durante el servicio | «**unlimited made-to-order espresso drinks during your booked service window**» | Icon [leída] |
| 6 | Horas de servicio · hora extra · tarifa base | **service hours / service window** · **additional hour / extra time** ($75) · **base fee + hourly rate** | Icon, Flashquotes, Sweet Carolinas, GrindKit [leídas] |
| 7 | Precio por invitado · paquete | **per person (pp) / per guest** («$5/pp after 75 guests») · **package** («100 Guest Package») | Sweet Carolinas, Houston [leídas] |
| 8 | Paga el anfitrión · pagan los invitados · mínimo | **hosted** («host-paid, all-inclusive») · **guest-pay / pop-up** · **minimum sales guarantee** | GrindKit, Big Dipper [leídas] |
| 9 | Leche vegetal (suplemento) | **alt milk / plant-based milk** · **oat milk** («additional alternative milk $50», o incluida) | Sweet Carolinas, Houston [leídas] |
| 10 | Filtro por lotes · frío · nitro | **batch brew** · **drip coffee** («drip only») · **cold brew** ($100 add-on) · **nitro cold brew** | cart-king, Sweet Carolinas, Prima [leídas]; batch brew (resumen) |
| 11 | Bebida de autor · temporada · siropes caseros | **signature drinks** · **seasonal drinks** · **house-made syrups** | Icon, Sweet Carolinas [leídas] |
| 12 | Vasos personalizados · activación de marca | **branded cups** · **custom cup sleeves** · **latte logo printing** · **brand activation** · **trade show** | Icon, Big Dipper, Flashquotes [leídas] |
| 13 | Montaje, servicio y desmontaje | **setup, service & breakdown** · **load-in** | Icon [leída] |
| 14 | Enchufe · circuito propio · sin toma de agua | **standard 110V outlet** · **dedicated circuit** · «**No plumbing connection is required**» (self-contained) | Icon, Prima [leídas] |
| 15 | Ajustar molienda · sacar un café · doble | **dial in** · **pull a shot** · **double shot** (18 g in / 36 g out) | resumen · por verificar · resumen |
| 16 | Capacidad · consumo | **drinks per hour** (50-65 por barista; «50 cups per hour») · **drinks per guest** | Flashquotes, CCB, GrindKit [leídas] |
| 17 | Escandallo de bebida | **cost per drink** («all-in cost per drink») · **COGS %** | GrindKit [leída] (NO «escandallo» ni «recipe costing») |
| 18 | Señal · saldo · recuento final · desplazamiento | **retainer** (30-50 %, non-refundable) · balance due 14 days before · **final guest count** · **travel fee** ($/mile, free radius) | GrindKit, Flashquotes [leídas] |
| 19 | Tasa de cierre | **booking rate** (quotes → bookings) | Flashquotes [leída] |
| 20 | Cocina base · permiso · revisión de planos | **commissary** (+ agreement, log) · **mobile food unit / facility permit** · **plan review** | Snohomish [leída]; CA §114295 (resumen) |
| 21 | Manipulador · seguro y certificado | **food handler card** · CFPM · **general liability $1M/$2M** · **COI** · **additional insured** | resumen · ✅ BP, MBAR |
| 22 | Vasos compostables | **compostable cups** (single-use, onsite) | seattle.gov (resumen) |

**(e) No se traducen literalmente**: «cafetería móvil» → **coffee cart / mobile espresso bar** (nunca *mobile cafeteria*) · «café de
especialidad» → **specialty coffee** · «barra de café» → **espresso bar / coffee bar** · «carrito» → **cart** · «tueste / tostador» →
**roast / roaster** · «leche de avena» → **oat milk** · «feria» → **festival / farmers market / fair** · «evento de empresa» → **corporate
event** · «barista autónomo» → **W-2 event barista** · «IVA» → **sales tax** · «licencia de actividad» → **business license** · «registro
sanitario» → **health permit + plan review** · «señal» → **retainer / deposit** · «manipulador» → **food handler**.

**Capas (1) y (2), propuesta:** **Coffee Cart Business Plan Kit** · slug `coffee-cart-business-plan` (`/en/digital-products/coffee-cart-business-plan`)
· `coffee-cart-business-plan.docx` · `coffee-cart-financial-projections.xlsx` · `coffee-cart-pricing-calculator.xlsx` «Coffee Cart Pricing
Calculator (Cost per Guest to Quote)» · `coffee-cart-startup-checklist.xlsx` · pestaña F2 **«Phase 2 - Cart, Permits & Commissary»** (≤ 31 car.).

### Términos para la landing

- **Por qué «cart» y no «truck»**: «truck» tiene más volumen (720 frente a 320), pero en eventos «cart» gana ×3-4 (§2), el AI Overview
  de «coffee truck business plan» separa street vending de catering (la ruta diaria es del Food Truck kit) y el caso **no tiene camión**.
  **Cobertura de «coffee truck»**: H2 de formatos con la tabla cart / trailer / truck (§4.1), FAQ «Can I use this as a coffee truck
  business plan?» («yes for events and catering; for daily street routes, see the Food Truck kit»), meta y keywords del schema.
- **Title** (≈ 105 car.): «Coffee Cart Business Plan Template for Coffee Catering: Word + Excel Projections + Pricing Calculator | AI Chef Pro».
- **H1 (Forma B)**: `Coffee Cart ` + oro `Business Plan` + «Template for a Mobile Espresso Bar & Coffee Catering Company: Word Plan +
  Excel Projections + Per-Guest Pricing Calculator + Startup Checklist».
- **Meta** (≈ 155 car.): «Coffee cart business plan for coffee catering (cart, trailer or truck): Word plan, 3-year Excel projections,
  per-guest pricing calculator and startup checklist.»
- **H2 (6)**: What's Inside Your Coffee Cart Business Plan Kit · How Much Does It Cost to Start a Coffee Cart Business? (Cart vs. Trailer
  vs. Truck) · Coffee Cart Pricing: What to Charge per Guest and per Service Hour · Is a Coffee Cart Business Profitable? Corporate
  Events, Weddings and the Summer Dip · Coffee Cart Permits: Health Department, Commissary and Fire Marshal · Coffee Truck or Coffee
  Cart: Which Business Plan Do You Need?
- **FAQ (8)**: How much does it cost to start a coffee cart business? ($5-25K un carro; caso ≈ $71.5K) · Is a coffee cart business
  profitable? (EBITDA ≈ 21 %, neto ≈ 10 % a régimen; julio flojo) · How much should I charge for a coffee cart at an event? (mediana
  $1,040; 50 % central $765-1,700) · How many drinks per hour can one barista make? (50-65) · **Do you need a commissary kitchen for a
  coffee cart?** (PAA, §6.2) · What permits do I need? · Can I use this as a coffee truck or trailer business plan? · Can I sell
  pastries or espresso martinis? (§6.6, §6.8).
- **Alt**: «Espresso cart with two baristas serving lattes at a corporate event» · «Mobile espresso bar at an outdoor wedding cocktail
  hour» · «Barista dialing in a two-group espresso machine on a coffee cart». **Keywords**: coffee cart business plan, coffee truck
  business plan, mobile coffee business plan, coffee trailer business plan, how to start a coffee cart business, coffee catering, AI Chef Pro.
- **Interenlazado**: entrantes desde Coffee Shop, Food Truck, Mobile Bar, Catering, Coffee Shop Checklist Templates y el hub EN;
  salientes a Mobile Bar (espresso martinis) y Coffee Shop (siguiente paso: local).

## 10. Lo que el producto EN NO debe afirmar, y riesgos

- **No**: «demanda creciente» (§0) · «coffee truck business plan» como nombre · que un carro no necesita commissary ni permiso en eventos
  privados (depende del condado: «ask in writing before you buy the cart») · «no fire permit needed» (generador/propano sí) · Flashquotes
  como ingresos esperados ni «≈ 15 eventos/año» (solo su plataforma) · «50-65 drinks per hour» como garantía · un «BLS barista wage»
  propio (es 35-3023) · la regla de sales tax de un estado · «cottage food pastries are fine» · «compostable required» salvo ejemplo
  local · espresso martini incluido · «works in Google Sheets» sin test · sellos NSF/SCA · tachados, «worth $X», ratings.
- **Riesgos**: concentración corporativa (≈ 65 % de eventos) · **valle de verano** (jul 3,8 %) al revés que el Mobile Bar · enchufe de
  sala de 110 V frente a máquina de 220 V · competencia por debajo de $612 (Flashquotes: mano de obra mal cobrada) · el comprador de
  «coffee truck business plan» que busca ruta diaria (la landing lo deriva al Food Truck kit).
- **❌ Pendientes**: texto del FDA Food Code (mobile matrix) y de CA §114295 (resúmenes), criterios de RCW 43.20.148, precio US del
  generador, depósitos de agua por condado, texto final de TX HB 520 / SB 541, UK por verificar, cifras ES del caso (ES aún vacío).
