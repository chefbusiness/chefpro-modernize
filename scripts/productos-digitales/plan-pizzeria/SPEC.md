# Plan de Negocio: Pizzería Napolitana (ES, 35 €) — SPEC 1.0 (F1 · 25-oct-2026 · sesión Claude Code)

> Base: `F1-camino.md` (cómo se construye y qué se toca, medido en el VPS) y `F1-research-pizzeria.md` (caso, normativa leída en
> origen, demanda, jerga, riesgos). Producto NUEVO de la familia Planes, línea A, motor 2.2, nº 54. Tamaño **M**: techo 5 M (F1 ≈ 0,75 M).
> Gemelo de construcción: Heladería 1.0 (`../plan-heladeria/`) con semilla del **Tapas Bar 2.2**. Gemelo EN previsto en la misma
> sesión (`../business-plans-en-8/`, «Pizza Shop Business Plan Kit», $39), duplicado de ESTE producto ya revisado.
> Decisiones tomadas por Claude con la delegación de John (20-sep y 25-oct «decide tú»). **Lo que no está aquí no se hace.**

## 1. Producto (D1-D4)

| D | Decisión |
|---|---|
| D1 | Slug `plan-negocio-pizzeria` · tarjeta y H1 **«Plan de Negocio: Pizzería Napolitana»** · **35 €** · sale de `comingSoon` y entra en la posición 1 del hub. **El título se mantiene** pese a la ETG (research hallazgo 1): es el nombre del tipo de negocio que se busca (4.400/mes) y el producto es un plan, no una pizza. A cambio, el producto **enseña a nombrar la carta** (D11) y lo vende como hallazgo: «desde 2022, “pizza napolitana” es un nombre reservado» |
| D2 | 5 entregables en `dl/plan-negocio-pizzeria/`: `plan-financiero-pizzeria.xlsx` (`plan-financiero`), `plan-de-negocio-pizzeria.docx` (`plan-negocio`), `checklist-apertura-pizzeria.xlsx` (`checklist-apertura`), `calculadora-masa-escandallo-pizzeria.xlsx` (**`calculadora-masa`**, nueva) y `guia-equivalencias-plan-negocio-pizzeria.docx` (`guia-equivalencias`) |
| D3 | **Versión 1.0** como la heladería (`piz_version.py`, `VERSION_MES` = mes del merge, «noviembre 2026» salvo que se fusione en octubre: entonces «octubre 2026»). Changelog `'1.0'`, `RECALIBRADO = ()` |
| D4 | Construcción = `F1-camino.md` §0-§4 tal cual: semilla del tapas bar (A-β + C2), `a.py` nuevo con la mecánica del tapas y el formato de la heladería, **cero código común**, el pid fuera de `PRODUCTOS` de `main.py` |

## 2. Caso (D5-D9) — research §3, tal cual salvo calibración

| D | Decisión |
|---|---|
| D5 | Ciudad media, **130 m²**, 50 plazas + terraza de 24 (abril-octubre), horno de leña de Ø 120-130 cm, sin traspaso. **66 cubiertos equivalentes/día** (51 de sala + 15 de para llevar y domicilio) × **19,50 € sin IVA** × **300 días** = 386.100 € a régimen; crecimiento 6 % / 4 %; rampa 0,75 en 4 meses. Líneas **82/18** (comida / bebida). Mercancía 23,5 % / 27 %, consumibles 3 %, **plataforma 10 % al 30 %** (sin reparto propio; recogida sin comisión), TPV 0,8 %, varios 2 %. Alquiler 2.100 €, fianza 3, renta previa 3, suministros 1.100 €, seguros 1.800 € |
| D6 | **IVA**: comida 10 % (sala, llevar y domicilio, sin partir). Bebida con **línea partida** del motor (`F1-camino.md` §1 y §2): «Bebida para llevar o a domicilio al 21 % (%)» con **H = 0,07** (alcohol y refrescos con azúcar que salen del local ≈ 1,3 % de las ventas ÷ 18 % de bebida); el resto al 10 %. `pct_bebida_alc` con rótulo propio (solo IVA soportado), `iva_bebida` sin efecto con su nota. `IVA_COMPRAS` = **8,9 %** por valor (`G13`). Las 3 frases del motor del §1 del camino, traducidas con `VOCABULARIO` |
| D7 | **Mes 1 = septiembre** (research §3: la rampa cae en meses medios y altos, Navidad con clientela, enero-febrero con el fondo intacto). Tupla `ESTACIONALIDAD` girada del research con `assert` de suma 1,000, como hizo la heladería con marzo (mismo patrón de notas en Instrucciones y Tesorería sobre las pagas extra). Cierre de dos semanas en enero y los lunes |
| D8 | Plantilla = las **6 filas** del research (4,875 jornadas, 7.381 €/mes) + la fila de suplencias si el molde la exige (RC-19); convenio de **hostelería provincial** (ALEH VI nombra «pizzerías»); todos ≥ SMI 2026 (1.221 € × 14, RD 126/2026) a prorrata. Cobertura 8,5 h × 3,0 + producción 2,5 h × 1,5 (≥ 98 %). Inversión = las **19 partidas** del research (130.250 € con imprevistos del 10 % sobre obra) repartidas en las **18 filas** del molde (se funden la 6 «Rótulo y fachada» con la 2 «Obra»). **Fijos = 9 filas** (17.600 €/año): gestoría 2.400 · mantenimiento del horno, campana y frío 2.400 · marketing 4.000 · software y TPV 1.500 · limpieza, lavandería, EPI, DDD y análisis 2.000 · **leña 3.600** (fijo: se quema por hora de fuego, no por pizza) · residuos 600 · SGAE y AGEDI-AIE 600 · PRL 500 |
| D9 | Financiación **CALIBRAR** desde 65.000 € propios + 155.000 € a 7 años al 6 % con 1 de carencia, palancas del research §3 en su orden. Gates del caso: DSCR mínimo ≥ 1,25 · saldo mínimo > 0 · cobertura ≥ 98 % · holgura de caja ≥ 15 % el año 1 (años 2-3 informativas) · exceso de financiación 0-5 % · **neto a régimen 7-12 %** · `pct_delivery` < 25 % · `PyG!G11` = H × 21 % + (1 − H) × 10 %. Escenarios 56·18,50·295 / 76·20,50·305 y umbrales del research. Máximo 3 vueltas; si no cuadra, se para y se reporta |

## 3. Lo que el producto afirma (D10-D12) — research §0-§1; nada fuera de ahí

- **D10 Normativa con fuente** (✅ en origen): IAE **671.x + 677.9**; apertura por régimen municipal (fuera de la Ley 12/2012);
  horno de leña < 1 MW **no** es actividad potencialmente contaminadora (RD 100/2011 con RD 1042/2017) — lo decide la **ordenanza de
  humos** (ejemplo leído: Madrid, Ordenanza 4/2021, conducto exclusivo a cubierta + 1 m en 15 m, limpieza ≥ 1/año, filtro de
  partículas con leña); gas: instaladora habilitada y control cada 5 años (RD 919/2006); registro sanitario autonómico (RD
  1021/2022); **aceite en mesa en envase irrellenable (RD 760/2021 art. 7)** — nunca citar el RD 895/2013 como vigente; alérgenos RD
  126/2015; «sin gluten» ≤ 20 mg/kg (Reg. 828/2014), no prometerlo con harina en el aire; **Ley 1/2025 art. 8** (llevarse lo no
  consumido sin coste, aviso en la carta); Ley 7/2022 (cobro del envase de plástico de un solo uso); IVA de D6; convenio y SMI de D8;
  reparto propio = laboral (ET DA 23.ª). Lo 🟡 del research se dice «compruébalo con tu ayuntamiento / gestor / inspector», sin cifra.
- **D11 El nombre de la carta** (no negociable, va igual en Word, checklist, calculadora, ficha y correo): «Pizza Napoletana» es ETG
  **con reserva de nombre** desde el 18-12-2022 (Reg. de Ejecución (UE) 2022/2313; protección del Reg. (UE) 2024/1143 art. 68.1,
  «aunque esté traducido»). Solo puede llamarse «pizza napolitana» la que cumple el pliego (Reg. 97/2010) **y** pasó la verificación
  oficial (arts. 72-73); la AVPN es privada y no la sustituye. El caso **no** usa el nombre: carta con «Margherita», «Marinara»…; la ETG
  es una opción explicada en el Word (sin Excel). «Estilo napolitano» o «napolitana» en el rótulo: 🟡 posible evocación → «consúltalo».
  Nunca «certificada», «ETG» o «verace» como sello del lector ni del producto.
- **D12 Prohibidos** (barrido): «España 2026» como sello, «validad(o)», «freelance», «carné/carnet de manipulador» (salvo «ya no
  existe»), «tarifa plana» con cifra, «CNAE» como trámite, RGSEAA para el minorista, «licencia de apertura» como única vía, RD 895/2013
  como vigente, RD 393/2007, neto «15-25 %», restos del tapas, de la heladería y del FT (regex de `F1-camino.md` §3, **sin** los restos
  de panadería: harina, masa, levadura y amasado son del oficio), «versión 1.1/2.2» o «versión anterior».

## 4. Ficheros (D13-D16)

- **D13 Excel** (motor): `a.py` + `semilla_piz.py` según `F1-camino.md` §2-§3; `VOCABULARIO` comensal; `ROTACION` encendida (techo 3,
  referencia de que el domicilio no ocupa mesa); `AMORTIZABLE` propio con la chimenea en obra.
- **D14 Checklist** `datos_checklist.py`: ~80 tareas en 6 bloques (`F1-camino.md` §4) con todas las del research §3 «tareas que obliga».
- **D15 Calculadora** `calculadora_piz_es.py` = `F1-camino.md` §4 (hojas `Masa` A pliego / B panadero, `Escandallo` 8 pizzas, `Instrucciones`;
  autotest). Parámetros del pliego del research §0.3 (1 l agua · 1.800 g harina · 50-55 g sal · 3 g levadura; bolas 180-250 g; 2 h + 4-6 h).
  El semáforo dice «dentro de los gramajes del pliego», **nunca** «es pizza napolitana» (D11). Precios de ingredientes = research §2.
- **D16 Word** 10 H1 en las 131 ranuras del FT ES, A4, docProps AI Chef Pro 2026, ≥ 6.000 palabras, tokens de `cifras_piz_es.py`; 2
  redactores Sonnet en paralelo (§1-5 / §6-10) con pistas del research (SERP §4 y su hueco; errores §6; leña/gas/eléctrico con la
  variante eléctrica; plataforma frente a reparto propio; el nombre de la carta D11). Venta cruzada (FIJOS 127-129): Kit de Tareas
  Recurrentes: Pizzería · Kit de Escandallos Pro · Pack Plantillas APPCC.

## 5. Lanzamiento (D17-D19)

- **D17 Capa de producto** = `F1-camino.md` §5 completa: landing con las 3 puertas cripto (plantilla), FAQ del research §6 (8 preguntas,
  incluida «¿Puedo poner “pizza napolitana” en la carta?» y «¿Sirve en México…?»), cifras MEDIDAS del Excel y ninguna movible (DSCR,
  payback, saldos), **sin testimonios** (como la finca), sin «España 2026» en SEO. Guía de equivalencias: censo 53 → 54. Interenlazado:
  hub ×7 + SPA, buscador, `kit-tareas-pizzeria` y `plan-negocio-bar-restaurante` → plan. **Carril Cursor (nota)**: FAQ 2 de
  `/usos/pizzero-consultor` (`src/data/use-cases-content.es.consultor.ts:619`, «neto 15-25 %» → cambiar solo esa frase, 7 idiomas),
  `productIds` de las `/usos/` de pizzería y enlaces desde los posts.
- **D18 Gates** = `F1-camino.md` §6. **Una** revisión Opus final (cifras · legal · editorial) y una ronda de arreglos.
- **D19 Correo** de lanzamiento ES en el hueco **8-dic 08:00Z** (borrador + prueba a John; routine el 8-nov o después). Payment Link:
  John (35 EUR, prosa sin viñetas; éxito → `/plan-negocio-pizzeria-access?session_id={CHECKOUT_SESSION_ID}`).
