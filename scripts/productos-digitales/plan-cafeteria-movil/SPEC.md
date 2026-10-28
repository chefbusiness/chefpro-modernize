# Plan de Negocio: Cafetería Móvil para Eventos (ES, 45 €) — SPEC 1.0 (F1 · 28-oct-2026 · sesión Claude Code)

> Base: `F1-camino.md` (cómo se construye, medido en el VPS: r1 y r4 en verde) y `F1-research-cafeteria-movil.md` (caso, normativa leída
> en origen, demanda, jerga, prohibidos). Producto NUEVO de la familia Planes, línea de eventos, motor 2.2, nº 55. Tamaño **M**: techo 5 M
> (F1 ≈ 0,92 M). Gemelo de construcción: **parrillero 2.2** (`a.py`) sobre la semilla del **Food Truck 2.2**; de la finca, contrato y
> versión 1.0 (y el injerto del Mes 1 girado); de la pizzería, el bloque Escandallo y las herramientas del Word. Gemelo EN en la misma
> sesión (`../business-plans-en-11/`, «Coffee Cart Business Plan Kit», $39), duplicado de ESTE producto ya revisado.
> Decisiones tomadas por Claude con la delegación de John (20-sep; 28-oct «escoge tú»). **Lo que no está aquí no se hace.**

## 1. Producto (D1-D4)

| D | Decisión |
|---|---|
| D1 | Slug `plan-negocio-cafeteria-movil-eventos` · H1 y tarjeta **«Plan de Negocio: Cafetería Móvil para Eventos»** · **45 €** (precio de la tarjeta de «Próximos» y de la línea de eventos) · sale de «Próximamente» del hub y entra en la posición 1. Descriptor SEO: «barra de café de especialidad para bodas, empresas y ferias» (research §6) |
| D2 | 6 entregables en `dl/plan-negocio-cafeteria-movil-eventos/` con los nombres y claves de `F1-camino.md` §4: plan financiero xlsx · Word (10 H1, sin anexo) · checklist (~80 tareas, 6 fases del camino) · **calculadora** `calculadora-escandallo-presupuesto-cafe-eventos.xlsx` (`calculadora-pricing`: Escandallo · Calculadora · Ejemplos · Instrucciones) · **contrato** `modelo-contrato-servicio-cafe-eventos.docx` (`modelos-contrato`) · guía de equivalencias (censo 54 → 55). Si la F2 pasa de 2 h, se cae el contrato (y la landing no lo nombra) |
| D3 | **Versión 1.0** con `caf_version.py`: «octubre 2026» si se fusiona el 28-31 oct; si no, «noviembre 2026» en los 4 ficheros a la vez. Changelog `'1.0'`, `RECALIBRADO = ()` |
| D4 | Construcción = `F1-camino.md` §0-§5 tal cual: **cero código común**, el pid fuera de `PRODUCTOS` de `main.py`, 2 líneas en el P&L, ferias por el canal `delivery`. Slug de PRIMER nivel en `products-catalog.ts` y `productos-digitales-config.ts` (gate: grep = 55 claves, 0 anidadas) |

## 2. Caso (D5-D9) — research §4 tal cual salvo calibración

| D | Decisión |
|---|---|
| D5 | Mapeo **B4 = eventos** (como catering y finca): **130 eventos × 135 invitados × 6,10 € sin IVA** = 107.055 € a régimen; crecimiento 8 % / 5 %. Mezcla del research §4 (30 bodas · 40 empresa · 22 jornadas de congreso o feria · 25 privados y rodajes · 12 jornadas de venta directa) en la nota de B4-B6, en el Word §6 y en `Ejemplos` de la calculadora. Líneas **10 / 90** «Dulces y bollería de obrador» / «Bebidas de café y sin café», las dos al 10 %. `coste_comida` 46 % · `coste_bebida` 16 % (nota: es la media de la mezcla con merma, no una receta) · consumibles 4 % · **`pct_delivery` 8,4 % = venta directa en mercados y ferias, `comision_delivery` 15 % = canon del organizador** · TPV 0,6 % · varios 4 % · `aforo` 350 · cobro 20 días / pago 30 |
| D6 | **IVA**: 10 % todo lo servido (barra y feria); `pct_bebida_alc` = 0 con su nota (la coctelería es otro plan); extras con precio propio al 21 % solo en el Word y el contrato (sin cifra en el P&L). Las 8 celdas del motor que hablan de alcohol (camino §1) se reescriben por `a.py`/`VOCABULARIO`. IVA soportado: leche al 4 % → nota, sin tocar el motor |
| D7 | **Mes 1 = marzo** (research §4: se abre en primavera con empresa y comuniones; enero-febrero son los meses más flojos) con el injerto de la finca (`ESTACIONALIDAD` girada con `assert` de suma 1,000 + notas de Instrucciones y Tesorería). Pesos del research: 8,1 · 8,9 · 11,4 · 11,6 · 6,8 · 3,9 · 11,0 · 11,3 · 9,0 · 6,9 · 4,3 · 6,8. Rampa 0,45 en 9 meses. **Si el injerto da guerra más de 20 min**: Mes 1 = enero sin girar y nota (no se toca código común) |
| D8 | **Plantilla**: titular-barista 1 × 1.800 € × 14 a jornada completa + camarero/a **fijo discontinuo** 1 × 1.400 € × 0,36 (convenio de hostelería, ALEH VI «instalaciones fijas o móviles»; «barista» no es categoría); el resto de filas del molde a 0 o como suplencias si el molde lo exige; todos ≥ SMI 2026 a prorrata. **Inversión 42.000 € en las 14 partidas del molde**: las 15 del research con la rotulación fundida en el vehículo («Furgoneta usada con rotulación y anclajes» 15.200 €, vida 8); imprevistos 8 % sobre el vehículo; base 400 €/mes (fianza 2, mes previo 1); suministros 60 €/mes; seguros 1.300 €/año. **10 fijos (7.700 €/año)**: los 9 del research + «Licencias y tasas de venta en ferias» 300 € (sin IVA: el rótulo empieza por «Licencias», `RX_SIN_IVA`) |
| D9 | Financiación **CALIBRAR** desde 25.000 € propios + ≈ 41.000 € a 6 años al 6,5 % con 1 de carencia, 3 meses de fondo. Gates del caso: DSCR mín. ≥ 1,25 · saldo mínimo > 0 · cobertura ≥ 98 % · holgura de caja A1 ≥ 15 % (A2-A3 informativas) · exceso de financiación 0-5 % · **neto a régimen 7-12 %** · `pct_delivery` < 25 % · demo §2.11.5 verde (fijo ±100 € mirando `ensayos`, luego propios/préstamo: camino §1 r2-r4). Palancas en orden: bodas a 9 € → +5 jornadas de congreso → empresa a 7,50 € (si sobra). Escenarios 110·130·5,70 / 145·140·6,30. Máximo 3 vueltas; si no cuadra, se para y se reporta |

## 3. Lo que el producto afirma (D10-D12) — research §0, §2 y §8; nada fuera de ahí

- **D10 Normativa** (✅ en origen): declaración responsable en el registro sanitario **autonómico** (RD 1021/2022), RGSEAA solo si vende a
  otros negocios; base con fregadero; **comida testigo** (RD 1086/2020 arts. 2.h, 30.8.d, 30.10): bebidas y bollería servida tal cual
  fuera *según nuestra lectura, sin criterio oficial: confírmalo con tu autoridad sanitaria*; con salado, ración ≥ 100 g, 7 días, en
  cada evento. Agua de depósitos (RD 3/2023 arts. 2.a, 65.3, 66.b). Alérgenos (RD 126/2015; avena = gluten salvo certificada; una jarra
  por leche). **Vasos**: el compostable con PE/PLA es plástico (Ley 7/2022 arts. 2.aa, 55.2: precio aparte en el ticket); pajitas y
  agitadores de plástico prohibidos (art. 56); promotores de eventos festivos → reutilizables (RD 1055/2022 art. 7.6) → **loza por
  defecto en bodas y empresa**. Venta en mercados y vía pública = no sedentaria (RD 199/2010, autorización municipal); evento contratado
  en recinto privado = servicio. Remolque ≤ 750 kg (RGV arts. 25-26); furgoneta reformada = informe e ITV; Ape 50 ≤ 45 km/h. IAE 677.9
  (+ 675 si hay venta directa) como criterio de asesoría. Lo 🟡 se dice «compruébalo con tu ayuntamiento / gestor», sin cifra.
- **D11 Electricidad** (va igual en Word, checklist, calculadora, contrato y ficha): cafetera de 2 grupos 2,4-4,5 kW; un enchufe de 16 A
  da ≈ 3,7 kW → máquina ≤ 3,5 kW o toma dedicada; si no, generador inverter o baterías. El contrato pide la toma por escrito.
- **D12 Prohibidos** (gate de texto en F2 y F3): los 12 del research §8 + los del brief de la pizzería («de 22 %», «Comunitat», «15 años»
  → «quince años», «Payback» a mitad de frase, «freelance», «carné de manipulador», «sin licencias», «demanda creciente», precios de la
  competencia como tarifa de mercado). Nada de alcohol en la carta.

## 4. Calculadora, contrato y Word (D13-D15)

- **D13 Calculadora**: camino §4 tal cual. Tabla de escalado (invitados → baristas, grupos, molinos, kg de café, l de leche, vasos, kW,
  agua) = la misma en calculadora, Instrucciones del plan y Word §6. Bebidas por invitado del research §1 (marcadas «estimación del kit,
  ratios de EE. UU.»). Tramos de cancelación «de X a menos de Y», sin huecos. Autotest pycel ±0,01 € con 3 juegos.
- **D14 Contrato**: gemela = `plan-finca-eventos/textos/contrato_es.json` + fuerza mayor y reparto de permisos del parrillero; contenido de
  camino §4. Señal a cuenta del precio (no arras del 1454), 103.l solo a distancia, 90.2, plan B de lluvia ≠ fuerza mayor.
- **D15 Word**: 2 redactores sonnet (`caf_es_a` §1-5, `caf_es_b` §6-10) con las pistas del camino §4; las 3 configuraciones del research
  §4 (mínima 12-15 k · caso 42 k · imagen 55-65 k) en §5-§7; venta cruzada → Kit de Tareas Recurrentes: Cafetería · Kit de Escandallos
  Pro · Pack Plantillas APPCC. Bio: 29 años en alta hostelería, quince en consultoría.

## 5. Orden y presupuesto
F2 y F3 = `F1-camino.md` §7-§8 (≈ 2,1 M, ≈ 3 h). Mac ≤ 3 agentes con `istats` < 60 °C; todo lo que gasta CPU, en el VPS
(`/root/wt-cafemovil`, rama `feat/plan-negocio-cafeteria-movil`). Una revisión opus final + una ronda de arreglos. Correo ES: 13-dic 08:00Z.
