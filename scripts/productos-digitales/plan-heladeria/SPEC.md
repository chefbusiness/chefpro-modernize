# Plan de Negocio: Heladería Artesanal (ES, 35 €) — SPEC 1.0 (F1 · 25-oct-2026 · sesión Claude Code)

> Base: `F1-camino.md` (cómo se construye y qué se toca, medido en el VPS) y `F1-research-heladeria.md` (caso, normativa leída
> en el BOE, demanda, jerga, riesgos). Producto NUEVO de la familia Planes, línea A, motor 2.2. Tamaño **M**: techo del producto
> entero 5 M (F1 ≈ 0,8 M). Gemelo de construcción: Parrillero ES 2.2 (`../parrillero-2_2/`) con semilla de la Panadería 2.2.
> Decisiones tomadas por Claude con la delegación de John (20-sep). **Lo que no está aquí no se hace.**

## 1. Producto (D1-D4)

| D | Decisión |
|---|---|
| D1 | Slug `plan-negocio-heladeria` · tarjeta y H1 «Plan de Negocio: Heladería Artesanal» · **35 €** (como panadería y tapas-bar) · sale de `comingSoon` y entra en la posición 1 del hub |
| D2 | 4 entregables en `dl/plan-negocio-heladeria/`: `plan-financiero-heladeria.xlsx`, `plan-de-negocio-heladeria.docx`, `checklist-apertura-heladeria.xlsx`, `guia-equivalencias-plan-negocio-heladeria.docx` (claves de `PRODUCT_FILES` = las de la panadería) |
| D3 | **Versión 1.0** (producto nuevo, como la Churrería): `hel_version.py` parchea en el proceso `motor.VERSION` = '1.0' y `VERSION_MES` = mes del merge (previsto «noviembre 2026»), recalculando `VERSION_FMT`; los chequeos de `main.py` (l. 585, 813) leen `motor.VERSION` en tiempo de ejecución. Si algún gate del motor exige '2.2', se vuelve a 2.2 y se anota (no se toca código común). Changelog `'1.0'`, sin «qué ha cambiado» (`RECALIBRADO = ()`) |
| D4 | Construcción = `F1-camino.md` §0-§4 tal cual: `a.py` nuevo clonado de la panadería en el formato compacto del parrillero; `semilla_hel.py` sobre los xlsx LIVE de la panadería; **no** se añade el pid a `PRODUCTOS` de `main.py`; **cero cambios en código común** |

## 2. Caso (D5-D9) — `F1-research-heladeria.md` §3, tal cual salvo calibración

| D | Decisión |
|---|---|
| D5 | Ciudad media, **85 m²** (obrador 20-25 m²), vitrina de **18 cubetas**, 20 plazas + terraza de 5 mesas en temporada, sin traspaso. **143 clientes/día × 4,90 € sin IVA × 310 días** ≈ 217.000 € a régimen; crecimiento 8 % / 5 %; rampa 0,70 en 4 meses. Líneas 90/10 (helado y obrador / cafetería y bebidas), todo al 10 % de IVA; `IVA_COMPRAS` 8,2 %. Mercancía 20 % / 25 %, consumibles 4 %, delivery 3 % al 30 %, TPV 0,8 %, varios 2 %. Alquiler 1.700 €, fianza 3, renta previa 2, suministros 700 €, seguros 1.500 € |
| D6 | **Mes 1 = marzo** (apertura en temporada; abrir en otoño quema el fondo antes del primer verano): tupla `ESTACIONALIDAD` rotada del research §3, con `assert` de suma 1,000. Las Instrucciones, la Tesorería (nota) y el Word dicen «Mes 1 = marzo» de forma explícita |
| D7 | **Invierno abierto con diversificación** (crepes y gofres, chocolate a la taza, tartas y turrón helado por encargo, B2B, catering de helado) y cierre de 3 semanas en enero. El cierre de noviembre a febrero va en el Word como alternativa razonada, **sin Excel**. Crepes y gofres dentro del caso, con la condición explícita en checklist y Word: consulta urbanística previa por la salida de humos; si la ordenanza no lo permite, el invierno va de chocolate, tartas y turrón |
| D8 | Plantilla de 6 filas (3,05 jornadas, research §3), fijos discontinuos de temporada (ET art. 16) y convenio de **hostelería provincial** (ALEH VI art. 4, «heladerías»). Inversión: las **19 partidas** del research (117.150 € con imprevistos del 10 % sobre obra). Fijos: las **10 filas** del research (10.250 €; la tasa de terraza con «pon la de tu ayuntamiento»). B2B **5 %** dentro del art. 3 del RD 1021/2022 |
| D9 | Financiación **CALIBRAR** desde 55.000 € propios + 125.000 € a 7 años al 6 % con 1 de carencia, con las palancas del research §3 en su orden. Gates del caso (como el parrillero D15): DSCR mínimo ≥ 1,25 · saldo mínimo de tesorería > 0 · cobertura ≥ 98 % · holgura de caja ≥ 15 % el año 1 (se informan las de los años 2 y 3) · exceso de financiación 0-5 % · neto a régimen ≤ 9 %. Escenarios y umbrales del research. Máximo 3 vueltas de calibración; si no cuadra, se para y se reporta |

## 3. Lo que el producto afirma (D10-D12) — research §0-§1; nada fuera de ahí

- **D10 Normativa con fuente** (✅ en origen): RD 618/1998 vivo solo en denominaciones (art. 3: «helado crema», «mantecado»
  ≥ 4 % yema, «sorbete», ≥ 430 g/l…); higiene = Reg. 852/2004 + RD 1021/2022; **644.4** (fabricar y vender en el local, Ley
  12/2012 con declaración responsable ≤ 750 m²) frente a **676** (consumo en local, régimen municipal) y la terraza siempre
  aparte; registro sanitario **autonómico** y RGSEAA solo fuera del art. 3 del RD 1021/2022; huevo: ≥ 70 °C 2 s u ovoproducto
  (art. 9), con la mezcla con yema mantecada en ≤ 24 h; conservación ≤ −18 °C, sin recongelar; vitrina según APPCC (ninguna norma
  estatal la fija); alérgenos RD 126/2015; IVA 10 %; «artesano» solo con calificación autonómica, «ELABORACIÓN PROPIA» como
  mención segura (art. 11). Lo marcado 🟡 en el research se dice como «compruébalo con tu gestor / inspector», sin cifra.
- **D11 Orden del proceso** (seguridad, no negociable): grasas, yemas y emulsionantes **ANTES** de pasteurizar (40-50 °C al subir)
  → 85 °C → enfriado rápido ≤ 4 °C → maduración 2-4 °C → mantecación → abatimiento → ≤ −18 °C. Después de pasteurizar solo lo
  que no necesita tratamiento. Va igual en Word, checklist y brief de redactores.
- **D12 Prohibidos** (barrido): «España 2026» como sello, «validad(o)», «freelance», «carné/carnet de manipulador» (salvo «ya no
  existe»), «tarifa plana» con cifra, «CNAE» como trámite, RGSEAA para el minorista, «licencia de apertura» para el 644.4, cifras
  de ordenanzas no leídas, restos del FT y de la panadería (regex de `F1-camino.md` §3), «versión 1.1/2.2» o «versión anterior».

## 4. Ficheros (D13-D15)

- **D13 Excel** (motor): `a.py` + `semilla_hel.py` según `F1-camino.md` §2-§3, `VOCABULARIO` cliente/mostrador, `ROTACION`
  apagada, `COBERTURA` 9,5 h × 1,6 + producción 2,75 h × 1, `AMORTIZABLE` propio. Nota de Tesorería: el personal se reparte
  en 12 meses y los fijos discontinuos cobran en temporada → el invierno sale más caro que en la realidad (prudente).
- **D14 Checklist** `datos_checklist.py` (~80 tareas en 6 bloques, `F1-camino.md` §4) con las tareas que obliga el research §3.
- **D15 Word** 10 H1 en las 131 ranuras del FT ES, A4, docProps AI Chef Pro 2026, ~6.700 palabras, ~60 tokens de
  `cifras_hel_es.py`; 2 redactores Sonnet en paralelo (§1-5 / §6-10) con pistas del research (SERP §4: tipos de heladería,
  local y potencia, maquinaria con precios, trámites, inversión, rentabilidad y sueldo, estacionalidad e invierno, marketing de
  temporada, errores §6; y el hueco que nadie cubre). Venta cruzada (FIJOS 127-129): Kit de Tareas Heladería · Kit de
  Escandallos Pro · Pack Plantillas APPCC.

## 5. Lanzamiento (D16-D18)

- **D16 Capa de producto** = `F1-camino.md` §5 completa (≈ 45 ficheros), landing con las 3 puertas cripto, FAQ del research §6
  (8 preguntas, respuestas con cifras MEDIDAS del Excel), testimonios coherentes (avatar, género, nicho; ninguno contradice el
  caso), sin «España 2026» en SEO, sin cifras movibles (DSCR, payback, saldos) en landing ni correo. Guía de equivalencias:
  censo 51 → 52; términos nuevos en `terminos.json` (mantecadora, cucurucho, tarrina, polo, granizado, horchata) con la jerga
  del research §5. Interenlazado de este carril: hub ×7 + SPA, buscador, `kit-tareas-heladeria` ↔ plan, `footerLinks` de los
  hermanos. **Carril Cursor (nota, no se toca aquí)**: `productIds` de las 3 páginas `/usos/` de heladería, enlaces desde los 3
  posts ES y la FAQ de `heladero-consultor` que promete 12-22 % y 28-35 % de neto (cambiar solo esas frases, en los 7 idiomas).
- **D17 Gates** = `F1-camino.md` §6. **Una** revisión Opus final (cifras · legal · editorial en un prompt) y una ronda de arreglos.
- **D18 Correo** de lanzamiento ES en el hueco **28-nov 08:00Z** (borrador + prueba a John; routine el 29-oct o después para
  programarlo, Resend no programa a > 30 días). Payment Link: John (prosa, sin viñetas; éxito → `/plan-negocio-heladeria-access`).
