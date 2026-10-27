# Ice Cream Shop Business Plan Kit (EN, $39) — inventario DELTA de F1 (frente a la panadería ES, la pizzería ES y sus EN)

> Sesión Claude Code, 27-oct-2026. Fuente medida: los 3 ficheros ES **FINALES y LIVE** de `astro-site/public/dl/plan-negocio-heladeria/`
> (merge `cbdcccd6`, revisión Opus aplicada; plan `a99b1686…`, checklist `d8ec6c6f…`, Word `04739dfe…`) contra la **panadería
> ES 2.2** (`dl/plan-negocio-panaderia/`, la semilla del ES: plan `d5b54dd7…`, checklist `0b5872ce…`), la **pizzería ES**, el tapas bar,
> FT, CAF y REST, y contra los EN publicados de **Pizza Shop** (`dl/pizza-shop-business-plan/`), **Bakery** (`dl/bakery-business-plan/`)
> y **Bar**. openpyxl/python-docx en el VPS (worktree `/root/wt-icecream`, venv `/root/venv-guias`), solo lectura:
> `inventario_delta.py` (clon del de la pizza, ampliado) → `inventario_delta.json`. A diferencia de la pizza, **el ES ya está
> cerrado**: estas cifras valen para la estructura Y para el gate de cifras (`../plan-heladeria/cifras_caso_es.json`, 119 valores).
> Precedentes: `../business-plans-en-8/` (= **PIZ**: código, checklist C2 de 80 tareas, docx de 131 ranuras) y `../business-plans-en-2/`
> (= **BAKERY**: EN de la gemela del libro).

## 0. Lo que manda: libro GEMELO de la panadería 2.2, código y Word de la PIZZA, checklist casi todo nuevo

| Comparación | Pestañas | Fórmulas idénticas en la misma celda | Texto ES idéntico en la misma celda (con EN publicado en esa celda) |
|---|---|---|---|
| HELP (plan heladería) vs **panadería ES** | 9/9, mismos nombres y orden | **727/736** (7 sin gemela, 0 nuevas) | 429/638 (EN Bakery 429) |
| HELP vs pizzería ES | 9/9 | 484/736 | 362/638 (EN Pizza 362) |
| HELP vs tapas bar ES | 9/9 | 485/736 | 341/638 |
| HELC (checklist) vs pizzería ES | 7/7 con el molde C2, **6 pestañas renombradas** | 2/12 (contadores en otras filas) | 138/383 (cabeceras, plazos, responsables) |
| HELC vs panadería ES | 7/7 | 0/12 | 51/383 |

Consecuencias: (1) el libro es la panadería (727/736), pero **ninguna cadena nueva sale del EN de la Bakery por celda**: de las
312 cadenas sin EN (§6), **0** casan en la misma celda con la panadería, la pizza o el bar; lo que la Bakery comparte con la
heladería es motor común, que ya está en los GM. (2) Por eso **el código es el de la PIZZA EN** (`mapas_piz.py` y compañía: molde
`_HOJAS_PLAN` con los mismos 9 nombres de hoja, checklist C2 de 6 fases + Instrucciones, `COL_OK 1`, arreglo G4 de la DV, versión
en A52/A11, zona D19 en 34-47, docx de 131 ranuras) y **el diccionario va en cadena**: PIZ por celda → PIZ por texto → BAKERY
(GPAN/GN, con sus `overrides_`) → BAR → BP. (3) El Word ES nace en las **131 ranuras del FT ES**, con los mismos H1 e índices que la
pizza y la paella (`docx_es_piz.json`): config de docx **idéntica a la de PIZ**. (4) No hay calculadora (el ES no la tiene): 3
ficheros + guía común. **Cero código común nuevo** salvo la rama `elif CONJUNTO == 'ice'` de `../business-plans-en/mapas.py`.

## 1. Totales

| Libro | Hojas | Fórmulas | Textos | DV | CF | Merges | Verdes = desbloq. | Tareas | Papel |
|---|---|---|---|---|---|---|---|---|---|
| HELP `plan-financiero-heladeria.xlsx` | 9 | **736** | 642 | 23 | 68 | 5 | 154 | — | A4 |
| HELC `checklist-apertura-heladeria.xlsx` | 7 | 12 | 463 | 6 | 6 | 6 | 80 | **80** (12/15/15/12/13/13) | A4 |
| ref. PIZP / PIZC (pizzería ES) | 9 · 7 | 741 · 12 | — | 24 · 6 | 70 · 6 | 5 · 6 | 156 · 80 | — · 80 | A4 |

docProps ES: «Plan financiero — Heladería Artesanal · v1.0», keywords «plan de negocio heladería artesanal, AI Chef Pro»,
description `aichef.pro/plan-negocio-heladeria` (los cambia D20). Protegidas sin contraseña. Rangos: Supuestos A1:C68 ·
Inversión A1:E38 · PyG A1:H59 · Punto Equilibrio A1:F56 · Escenarios A1:F28 · Personal A1:J29 · Instrucciones A1:E72 · Tesorería
A1:O70 · Financiación A1:H80.

| Docx | Párrafos | Con texto | Estilos | Palabras | Encabezados (índice de párrafo) | Página |
|---|---|---|---|---|---|---|
| `plan-de-negocio-heladeria.docx` | **131** | 110 | Normal 121 + 10 Heading 1 | 6.896 | **37 · 44 · 51 · 59 · 67 · 76 · 83 · 91 · 100 · 109** | A4 |

0 tablas, 0 imágenes, 0 multi-run, 0 rojos, 0 «pendiente». Ranuras de cuerpo = las de PIZ: **`ice_a`** §1-5 = 39-43, 46-50,
53-58, 61-66, 69-75 (**29**, ≈ 2.990 palabras) · **`ice_b`** §6-10 = 78-82, 85-90, 93-99, 102-108, 111-117 (**32**, ≈ 3.750).
`FIJOS[35]` «Anexos: Plan Financiero Excel + Checklist de Apertura Excel + Guía de Equivalencias» · 123-126 ChefBusiness · **127-129
venta cruzada ES** (→ Kit de Tareas Recurrentes: Heladería Artesanal · → Kit de Escandallos Pro · → Pack Plantillas APPCC) · 130
URL. 44 párrafos idénticos a la pizza ES (portada, aviso, índice, separadores, cierre).

## 2. Delta del libro, celda a celda (lo que F2 mapea)

1. **Fórmulas sin gemela (7)**, todas del caso o de texto: `0. Supuestos!C9` (texto del PVP con IVA: «En el local todo va al 10 %…»),
   `Inversión Inicial!B28` (imprevistos = 10 % de **B7-B11**, fila **28**), `D28` (lista de partidas de obra), `B36` (obra = B7-B11
   + B28), `B37` (maquinaria = **B12-B21**), `D38` (lista de lo que no se amortiza) y `PyG 3 Años!F13` (IVA soportado al 4/10 % y
   el 8,2 %). Con texto nuevo: **C9, D28, D38, F13** → `formulas_ice_manual.py`; con gemela en PANP/PIZP: D26, D27, D30, D31,
   D33, D36, D37, F14, F18, `Punto Equilibrio!A26`, `Personal!A2`, `Tesorería!O11` → `derivar_formulas_ice.py`. **Ojo**: `B37` es
   `IF(B12="","",…)`: la fila 12 tiene que llevar un número (§9 de la SPEC: lleva $4,500).
2. **`PyG!G13` es VALOR** (0,082 = IVA soportado ponderado, verde) → `VALORES_EN` 0 (sin crédito de compras en EE. UU.).
   **`G14`** = fórmula del molde (E2 la ata a `$B$41`). **`G10`** = `B39`. **`G11`** = fórmula con `B62`/`B63`/`B40`/`B39`: con
   `B62` = 0 (sin alcohol) da `B39` → neutra; **no hay línea partida**: la columna H está vacía (`H4`/`H10` los vació la semilla
   ES) → **sin E3 ni E5**.
3. **Supuestos** (valor ES): `B4` «Clientes/día (media del año 1)» 143 · `B5` 4,90 · `B6` 310 · `B7`/`B8` 0,08/0,05 · `B11` 0,9 ·
   `B13`/`B14` 0,20/0,25 · `B15` 0,04 · `B16`/`B17` 0,03/0,30 · `B18` 0,008 · `B20` 0,33 · `B21` 14 · `B22` 17.094 · `B24` 1.700 ·
   `B25` 3 · `B26` 700 · `B27` 1.500 · `B28` 0,02 · `B30`/`B31` 55.000/129.000 · `B32` 6 % · `B33` 7 · `B34` 1 · `B35` 3 ·
   `B37`/`B38` 15/25 % · `B39`/`B40`/`B41` 10/21/21 % · `B42` 0 · `B44`/`B45` 10/10 · `B48` 0 · `B51` 20 · `B52`/`B53` 0,7/4 · `B54` 2 ·
   `B55` 0,10 · `B58`/`B59` 2/30 · **`B60`/`B61` = 5/10** (pagas extra en julio y diciembre con Mes 1 = marzo) · `B62` **0** ·
   `B63` 0,10 · `B65`/`B66`/`B67` 1/1,25/0,15 · `B68` «convenio provincial» 0. Mismas filas que la panadería y la pizza (el
   rótulo de `B62` cambia: aquí «Bebida ALCOHÓLICA sobre el total de bebida»).
4. **Inversión** (A1 «PLAN DE NEGOCIO: HELADERÍA ARTESANAL», A2 «…con obrador propio», A3; **19 partidas filas 7-25**, A/B/D/E):
   7 proyecto técnico · 8 obra del obrador y la tienda · 9 eléctrica trifásica (30 kW) · 10 fontanería, desagües, clima ·
   11 rótulo y escaparate · **12 pasteurizador de 30 l** (14.600) · 13 mantecadora (14.000) · 14 abatidor · 15 armarios de
   conservación y maduración · 16 mesas inox, básculas, refractómetro, cubetas · 17 vitrina de 18 cubetas (10.500) · 18 mostrador,
   lavaporcionador, cafetera, crepera, gofrera, chocolatera · 19 mobiliario y terraza · 20 TPV Veri\*factu · 21 menaje y cartelería
   de alérgenos · 22 formación técnica · 23 marca y lanzamiento · 24 constitución, licencia, registro y APPCC (E = «No») · 25 stock.
   26 fianza · 27 renta previa · 28 imprevistos. **B36 = B7…B11 + B28 y B37 = B12…B21: sin el defecto «Campaña» de la pizza**;
   22-25 no se amortizan (D38). 117.150 € de partidas.
5. **PyG**: `A2` «Escenario realista — heladería artesanal» · `A10` «Ventas de helado y obrador (mostrador, para llevar, tartas,
   invierno y…)» · `A11` «Ventas de cafetería y bebidas (sin alcohol)» · `F10`/`F11` reparto de la venta · fijos **26-35 (10)**:
   gestoría 1.800 · mantenimiento del frío 1.500 · marketing de temporada 2.500 · software 700 · limpieza, EPI y análisis 800 ·
   **tasa de terraza** 1.200 · residuos 350 · DDD 450 · SGAE/AGEDI 500 · PRL 450 (= 10.250). Ratios **50-56**: `E51` margen bruto
   0,70 · `E53` mercancía 0,25 · `E54` personal 0,40 · `E55` alquiler 0,12 · `E56` neto 0,05.
6. **Personal**: **6 filas 5-10**, **1 persona por fila** (titular-maestro heladero 1,0 · dependiente/encargado de turno 1,0 ·
   dependiente de temporada 0,5 · dependiente de verano 0,25 · ayudante de obrador 0,2 · suplencias 0,1 = **3,05**); `C11 =
   SUM(C5:C10)`: con una persona por fila **no hace falta E4** (en la pizza era `C12`: si F2 clona `PARCHES_FORMULA` de PIZ tal
   cual, **escribiría en `C12`, que aquí es la cabecera «CRECIMIENTO DE LA PLANTILLA»**). Incorporaciones `B13`/`B14` 6.000/6.000.
   Cobertura `B18`-`B23` = 40 · **46** · 9,5 · 1,6 · **2,75 h de producción** · 1.
7. **Instrucciones** (formato de la pizza): uso 1-8 (A4-A12; el 8 «el Word… usa las cifras de este Excel»), ratios A14-A22, «CIFRAS
   DE ESTE PLAN» A24-A31, **D19 en A33-A47** (cabecera 34 + **13 filas 35-47**: Mes 1 = marzo · 81,6 % de abril a septiembre
   (MAPA) · coste del helado de mostrador · precio de la bola · 430 g/l (RD 618) · −18 °C (RD 1021/2022) · huevo 70 °C 2 s (art. 9;
   **D41 dice «yemas, nata y grasas ANTES de pasteurizar»: bien**) · personal 34-40 % · alquiler 8-12 % · merma 5-8 % · 30 kW ·
   IVA 10 % · convenio), sin D18, firma A51, **versión A52** (E1 en A53).
8. **Tesorería**: pesos `B5:M5` = **Mes 1 = marzo** (0,05 · 0,075 · 0,10 · 0,135 · **0,165** · 0,15 · 0,11 · 0,065 · 0,035 · 0,06 ·
   0,025 · 0,03) con nota **`O5`**; `O13` pagas extra (meses 5 y 10); filas 16-20 de IVA (repercutido, soportado, **arrastre con la
   inversión**, liquidación trimestral, modelo 303) y **`A34`** «trimestres del plan (marzo-mayo, junio-agosto, septiembre-noviembre)».
   Frente a la pizza EN (Mes 1 = septiembre): `O5`, `A34` y **`O20`** son textos nuevos (§6).
9. **Escenarios**: `B5:D7` = 120/143/165 · 4,60/4,90/5,20 · 300/310/320 (verdes B y D).

## 3. IVA → sales tax: cómo se neutraliza (patrón Bar EN D9/D57 + PIZ D141, sin E5)

- `B39` = `B40` = `B63` = **8 %** (ejemplo), `B41` = **0**, `B62` = **0** (sin alcohol: `G11` = `B39`).
- **`G13`** (valor): `VALORES_EN` = **0** con su rótulo «no input credit». **`G14`**: E2 (→ `$B$41`). Columna H vacía: nada que parchear.
- `Inversión!B33` (IVA soportado de la inversión) = SUMIF × `B41` = 0 → rótulo y nota de la Bar/Pizza EN (en EE. UU. el sales tax
  de la compra es coste: va dentro del presupuesto de cada partida).
- Tesorería 16-20: rótulos de la Bar/Pizza EN (sales tax collected / remitted); el arrastre de la fila 18 queda en 0 con `B41` = 0.
  `A34` y `O20` **nuevos para Mes 1 = marzo** (liquidación en los meses 4, 7 y 10 = **junio, septiembre y diciembre**).

## 4. Checklist (HELC)

Molde C2 de la pizza (A1 título, A2 fase con semanas, cabecera fila 4 `OK | TRÁMITE | RESPONSABLE | PLAZO | NOTAS`, contador por
hoja, versión **A11** en Instrucciones, E1 en A12) con **80 tareas 12/15/15/12/13/13** (filas 5-16 · 5-19 · 5-19 · 5-16 · 5-17 ·
5-17; contadores en las filas 18 · 21 · 21 · 18 · 19 · 19). Pestañas ES: «F1 - Constitución» · «F2 - Local y licencia» · «F3 -
Obrador y sanidad» · «F4 - Personal y APPCC» · «F5 - Marca y carta» · «F6 - Apertura y temporada». A1 «CHECKLIST DE APERTURA —
HELADERÍA ARTESANAL»; `Instrucciones!A3` con el **id** «plan-negocio-heladeria» (en EN, el nombre comercial). **DV `"✓,—,N/A"`
con las 80 celdas OK en `☐`** (el defecto sistémico del motor nuevo, F2-NOTAS PIZ §5.1): lo arregla el `instalar` clonado de PIZ
(`CLAVES['—'] = '☐'`). **Ojo**: el texto de la DV (`dv-error`/`dv-prompt`) casa con el EN de PIZ-GR «Use the dropdown: ✓, —, N/A…
— = pending» → **tiene que decir ☐** (revisar en la tanda; posible deuda también en la Pizza EN LIVE).

## 5. Docx

Mismo molde que PIZ: `DOCX_N_PARRAFOS` 131, H1 37…109, `DOCX_ULTIMO_9` '108', `FIJOS[35]`, 127-130. Lo que **no cruza** (bloques
ES por ranura): [64] y [102]-[103] (IAE 644.4/676, Ley 12/2012, declaración responsable, 750 m²) · [104] (registro autonómico,
RGSEAA, art. 3 RD 1021/2022) · [105] (APPCC, huevo 70 °C 2 s, −18 °C) · [106] (RD 618/1998, «artesano», «ELABORACIÓN PROPIA») ·
[107] (RD 126/2015, IVA 10 %) · [108] (ET, convenio, Veri\*factu) · [87]-[88] (fijo discontinuo, ALEH VI) · [53]-[56] (MAPA y
DataForSEO España) · [50] y [113] (crepes con salida de humos por ordenanza) · [47]/[78] (proceso con pasteurizador: en EN, base
comprada; el pasteurizador a la variante de [99]). Cifras en € del texto: 50+ (tokens de `cifras_caso.json`). Paso 1 de la F2-EN:
`bp10.py extraer_docx` sobre este Word (ya final).

## 6. Diccionario: cobertura medida (864 cadenas únicas de HELP + HELC)

| Grupo (primera fuente con EN) | Cadenas | Palabras | Qué es | Va a |
|---|---|---|---|---|
| **PIZ-GM** (mismo ES que la Pizza EN, cadena GM) | 349 | 3.467 | motor común (plan 332 · checklist 16 · ambos 1) | nadie (GM; ver los 2 de abajo) |
| GM (BP) · BAR-GM | 22 · 3 | 317 · 9 | motor común antiguo | nadie |
| **PIZ** (EN de GPIZ-plan/GPIZ-check por texto) | 84 | 550 | plazos, responsables, cabeceras de fase, notas de Supuestos (C18, C30, C31, A51, J10…) | **GR** (revisión en la tanda): llevan contexto de pizzería; 10 son celdas D19 (C35, C37…) que van **sin propuesta** |
| PIZ-GR · PAN · REST | 8 · 9 · 1 | 56 · 96 · 10 | «Pest control», «Accountant», «IRS and state tax portal…», «Sign and storefront window», ASCAP/BMI/SESAC… | GR |
| **HEL** (sin EN en ninguna fuente) | **312** | **5.896** | plan 155 (**3.472** palabras: Supuestos 1.222 · Inversión 559 · PyG 434 · Personal 317 · Instrucciones 620 · Tesorería 315) · checklist 156 (**2.424**) · ambos 1 | **GICE-plan** · **GICE-check** |
| GX · sin letras | 70 · 6 | 297 | pestañas, CLAVES, versión, pie, docProps | nadie |

Normalizar el VOCABULARIO de la heladería (`cliente(s)` → `comensal(es)` / `cubierto(s)` / `transacción(es)`) casa **1** cadena
más (con PIZ): no merece la normalización de la pizza. **Dos EN de PIZ-GM con texto de la revisión de la pizza** (`GM.revision.json`,
aplicado encima del GM): **c0387** → `Personal!J19` («46 weeks: 52 minus about six weeks for vacation, holidays, the January closure…»:
vale, la heladería también cierra en enero) y **c0531** → `Tesorería!O20` («…Months 4, 7 and 10: **December, March and June with
Month 1 in September**…»: **FALSO aquí**) → `POR_CELDA` o `GM.revision.json` propio con «June, September and December with Month 1
in March» (SPEC D195).

## 7. Código que se clona (todo en `business-plans-en-10/`)

| Nuevo | Origen | Cambios |
|---|---|---|
| rama `elif CONJUNTO == 'ice'` en `../business-plans-en/mapas.py` | `:1240-1247` (piz) | único cambio en código común (+ mensaje de `:1249`). **Choque de merge** con la otra F1 paralela (D156-D185), que añade su `elif` en el mismo sitio: trivial, se resuelve a mano |
| `mapas_ice.py` | `mapas_piz.py` | `PLANES` (D186), `LIBROS` HELP/HELC, `A_PIZ` (gemela por celda = PIZP/PIZC y su EN publicado), pestañas D199, `TAREAS_POR_FASE` 12/15/15/12/13/13, `PARCHES_FORMULA` **solo E2 `G14`** (fuera E4 y E5), `FILA_VERSION` HELP 52 · HELC 11, `ZONAS_CELDA` D19 35-47, docx de PIZ (131, `ice_a`/`ice_b`), `PRESTAMO_SEMILLA` 162,000, `AUTOTEST` con las pestañas ES, `SHA_PIZ` (sha256 del diccionario de `-8/`), G4 heredado, grupos `GM · GR · GICE-plan · GICE-check`, diccionario PIZ → BAKERY → BAR → BP sin normalizar |
| `datos_ice.py` | `datos_piz.py` (sin `REGLA_UNIDADES` de masa) | FIJOS (D193-D194), POR_CELDA (`O5`, `A34`, `O20`, `C62`/`C63`, `Startup Costs!D12`), `VALORES_EN` (D191), tokens (D200), pistas, glosario research §9, `cifras_prohibidas()` (D202) + `RX_ICE_NO` |
| `bp10.py` | `bp8.py` sin el subcomando `calculadora` | `verificar` con los sha256 del ES final (arriba) y de la Pizza EN |
| `derivar_formulas_ice.py` · `formulas_ice_manual.py` | los de PIZ | gemela = celda de PIZP (o PANP: B28/D28/D38 van una fila más abajo que en la pizza); manuales C9, D28, D38, F13 |
| `calibracion_ice.py` · `barrido_ice.py` · `resumen_entregables.py` · `BRIEF-TRADUCTORES.md` | los de PIZ | D15 de D191 · D202 · 3 entregables · glosario research §9 pegado entero (F2, paso 1a, como la pizza) |

## 8. Defectos del ES detectados (no bloquean: el ES está LIVE; para la cola del ES)

- **DV del checklist `"✓,—,N/A"` con las celdas en `☐`** (sistémico; F2-NOTAS PIZ §5.1). El EN lo corrige en `instalar` (G4).
- `Checklist Instrucciones!A3` con el id interno «plan-negocio-heladeria» (cosmético en ES; el EN pone el nombre comercial).
- **Errata de seguridad del Kit de Tareas ES (24-oct, grasas/yemas tras pasteurizar): NO está en el plan ES.** Comprobado en
  `Instrucciones!D41`, checklist `F3!E10`/`E11`/`E12` y Word [47], [78], [105]: grasas, yemas y emulsionantes ANTES de
  pasteurizar; mezcla con huevo, mantecada en 24 h. Nada que heredar.
- Hub EN (`DigitalProductsHubPage.astro:643-656`): tarjeta «Business Plan: **Artisan Gelato Shop**» → `/plan-negocio-heladeria`
  (el ES), con «Equivalents Guide for Latin America» y «gelato seasonality». En F3 **se sustituye** por la del EN (no se añade al
  lado: B1 de la revisión de la pizza).
- `plan-negocio-heladeria.astro:28` `locales={['es']}` (comentario l. 5-6: «si nace el gemelo EN, pasar a `alternatesFamilia`»).

## 9. Paso 1 de la F2-EN (VPS, worktree `/root/wt-icecream`, ya creado)

```bash
cd /root/wt-icecream && git pull -q && cd scripts/productos-digitales/business-plans-en-10 && PY=/root/venv-guias/bin/python
$PY inventario_delta.py > /tmp/ice-inv.txt                       # re-medición (debe dar lo mismo: el ES está cerrado)
BP_CONJUNTO=ice $PY bp10.py extraer_textos > /tmp/ice-ext.txt && BP_CONJUNTO=ice $PY bp10.py extraer_docx > /tmp/ice-ed.txt
BP_CONJUNTO=ice $PY bp10.py mapas                                 # autotest + censo + verificar
```
Si el ES cambia antes de la F2 (sha256 distintos de los de arriba), manda el ES nuevo: re-medir y avisar.
