# Wedding Venue Business Plan Kit (EN, $49) — inventario DELTA de F1 (frente a la finca ES y a los hermanos EN)

> Sesión Claude Code, 27-oct-2026. Fuente medida: los **5 ficheros ES LIVE** de `dl/plan-negocio-finca-eventos-bodas/` (ES 1.0
> con la revisión final aplicada, `main` @ `7a11a0f3`) contra sus orígenes ES (**panadería 2.2** = semilla del libro, **heladería**
> = misma semilla, **parrillero 2.2** = contenido de eventos, **pizzería** = motor 2.2 más reciente, tapas bar y FT) y el EN ya
> escrito de los 8 conjuntos. Script `inventario_delta.py` (esta carpeta; clon del de la pizza) en el VPS (`/root/wt-wedding`,
> venv `/root/venv-guias`, solo lectura, 2,7 s) → `inventario_delta.json`. El docx del contrato y el checklist ES también están
> en texto en el repo (`../plan-finca-eventos/textos/contrato_es.json`, `datos_checklist.py`): F2 los usa como fuente sin xlsx.

## 0. Lo que manda: libro GEMELO de la PANADERÍA ES; texto del motor = el EN de la PIZZA; checklist, calculadora y contrato nuevos

| Comparación (`parecido`) | Pestañas | Fórmulas idénticas en la misma celda | Rótulos col. A en la misma fila |
|---|---|---|---|
| WEDP (plan finca) vs **panadería ES** (PANP) | 9/9 | **724/734** (10 distintas, ver §2) | 233/362 |
| WEDP vs heladería ES | 9/9 | 724/734 | 237/362 |
| WEDP vs parrillero ES | 9/9 | 635/734 (Inversión 0/47, Personal 13/43) | 227/362 |
| WEDP vs pizzería ES / tapas bar ES | 9/9 | 481/734 | 178/362 |
| WEDC (checklist) vs panadería · heladería · parrillero · pizzería | 1-2/7 | 0-2/12 | 7-20/111 |

Consecuencias:
1. **La ESTRUCTURA es la de la panadería** (19 partidas en Inversión 7-25 + A26-A28 fianza/renta previa/imprevistos, 6 filas de
   Personal 5-10, 10 fijos en PyG 26-35, umbrales E51/E53-E56, Instrucciones con D19 en A33-A48, versión A53). Esa estructura **ya
   pasó por el código común EN** con el conjunto `restpan` (Bakery EN LIVE): no hace falta tocar `aplicar_en`, `gates_en` ni `mapas.py`
   más allá de la rama.
2. **El TEXTO no es el de la Bakery EN**: el diccionario por cadena exacta da **308 cadenas del GM de la PIZZA** (motor 2.2, el más
   reciente) frente a 3 del GM de la Bakery (`-2/`, traducida sobre una panadería anterior). Los EN de eventos (cat/bbq/pael)
   **tradujeron el FT ES permutado**, no el parrillero: su ES no contiene «invitado» (0 cadenas) y solo aportan **6** coincidencias.
3. **Código = clon del de la PIZZA** (`mapas_piz`, `datos_piz`, `bp8`, `calculadora_piz`, `barrido_piz`, `inventario_delta`,
   `resumen_entregables`, `derivar_formulas_piz`, `formulas_piz_manual`), con las constantes de fila de la panadería y el
   diccionario **por texto** de la pizza en vez del **por celda** del Bar (`A_BAR` → `A_PIZ` sin celda). **Cero código común nuevo**
   salvo `elif CONJUNTO == 'wed'` en `../business-plans-en/mapas.py` (copia de `:1240-1247` + mensaje de `:1248-1249`).
4. **Motor de eventos SIN permutar** (como el ES, F2-NOTAS ES §2.1): B4 = invitados por evento, B6 = eventos/año; el crecimiento cae
   sobre B4 (= eventos en dólares). **No** se copian los 7 parches de permutación de `mapas_mbar/bbq/pael` (la cobertura de personal
   es `horas × personas × B6` y solo vale sin permutar).
5. **Word = las 131 ranuras del FT ES** (estilos 131/131 iguales a PAEL; H1 en 37·44·51·59·67·76·83·91·100·109; 29 + 32 ranuras):
   config de docx de PAEL/PIZ tal cual. **Calculadora y contrato fuera del motor**, como `calculadora_piz.py`.

## 1. Totales

| Fichero ES | Hojas / párrafos | Fórmulas | Textos (palabras) | DV | CF | Verdes | Tareas | Papel |
|---|---|---|---|---|---|---|---|---|
| WEDP `plan-financiero-finca-eventos-bodas.xlsx` | 9 | **734** | 646 (8.399) | 22 | 68 | 156 | — | A4 |
| WEDC `checklist-apertura-finca-eventos-bodas.xlsx` | 7 | 12 | 483 (3.089) | 6 | 6 | 84 | **84** (12/16/15/13/14/14, filas 5-16 · 5-20 · 5-19 · 5-17 · 5-18 · 5-18) | A4 |
| CALC `calculadora-presupuesto-boda-evento-finca.xlsx` | 3 (Calculadora · Ejemplos · Instrucciones) | 172 (46 + 126) | 318 (2.830) | 11 | — | 85 | — | A4 |
| Word `plan-de-negocio-finca-eventos-bodas.docx` | 131 párr. (110 con texto; 121 Normal + 10 H1) | — | 6.741 pal. (§1-§10: 627 · 540 · 574 · 633 · 637 · 713 · 610 · 698 · 677 · 838) | — | — | — | — | A4, 80 € en texto |
| Contrato `modelo-contrato-reserva-finca-eventos.docx` | 150 párr. (112 Normal + 38 List Bullet; formato por run: Kicker/Title/H1/H2/Firma) | — | 4.660 pal. | — | — | — | — | A4, sin tablas |
| Guía ES↔LatAm | **no cruza** (bonus común EN, como PIZ D135) | | | | | | | |

## 2. Delta del libro (lo que F2 mapea)

1. **Fórmulas distintas de la panadería (10)**, todas de la finca: `0. Supuestos!C9` (PVP equivalente: texto «Precio por invitado
   sin IVA…»), `Inversión Inicial!B28` (imprevistos = `B55` × obra B7, B9, B10, B12, B13, B15, B16, B20, B21, B22), `D28` (texto),
   `B36` (base obra = esas filas + B28), `B37` (equipo = B11, B14, B17, B18, B19), `D38` (lista de lo no amortizable: B8, B23, B24,
   B25), `PyG!F13`/`F14` (notas de coste directo y canon), `Punto Equilibrio!A26` (texto con «invitados por evento») y
   `Tesorería!O11` (texto). Las numéricas (B28, B36, B37) **se copian del ES sin tocar**; las de texto van a la derivación.
2. **Fórmulas con texto fuera de CLAVES: 16**; con gemela por literales en un libro de referencia: **10** (D26, D27, D30, D31, D33,
   D36, D37, F18, A26, Personal!A2) → `derivar_formulas_wed.py` con la gemela de la **pizza EN** (motor 2.2) y, si no, de la Bakery;
   **6 sin gemela** → `formulas_wed_manual.py`: **C9, D28, D38, F13, F14, O11**.
3. **Columna de IVA del P&L** (`pyg_GH`): `G10` y `G11` = **VALOR 0,21** (verdes; «Ventas de alquiler del espacio y servicios del
   evento», «Canon del catering exclusivo») · `G13` = VALOR 0,21 (verde; `IVA_COMPRAS`) · `G14` = fórmula de alcohol
   `B62*B40+(1-B62)*B39` (→ E2) · `G15-G35` → `$B$41` · **columna H vacía** (sin literal: **no hay E5** de la pizza). Se neutraliza
   en SPEC D164.
4. **Supuestos** (50 verdes, `supuestos_es`): B4 82 · B5 37 · B6 120 · B7/B8 8/5 % · B11 0,78 · B13 0,163 · B14 0 · B15 0,02 ·
   B16/B17 0,20/0,125 · B18 0,003 · B20 0,33 · B21 14 · B22 17.094 · B24 3.500 · B25 2 · B26 1.600 · B27 5.500 · B28 0,02 · B30
   100.000 · B31 263.000 · B32 6,5 % · B33 8 · B34 1 · B35 3 · B37/B38 15/25 % · B39/B40/B41 10/21/21 % · B42 0 · B44/B45 15/10 ·
   B48 0 · B51 300 · B52/B53 0,45/12 · B54 1 · B55 8 % · B58/B59 10/30 · B60/B61 5/10 · **B62 0** (la finca no vende alcohol) ·
   B63 21 % · B65/B66/B67 1/1,25/15 % · B68 0. **Verdes de otras hojas**: Inversión B7:B25 + E7:E25 (col. E = «¿lleva IVA?»: el
   motor la reescribe por rótulo, M8 ES) · PyG G10, G11, G13, B26:B35, E51, E53:E56 · Escenarios B5:D7 · Personal B5:D10, B13,
   B14, B18:B23 · **Tesorería B5:M5** (estacionalidad, Mes 1 = marzo) · Financiación B8:B11, B17, B42.
5. **Inversión** (A1-A3 propios; 19 partidas 7-25 + 26-28): clases por fila: **obra** 7, 9, 10, 12, 13, 15, 16, 20, 21, 22 ·
   **equipo** 11, 14, 17, 18, 19 · **no amortizable** 8, 23, 24, 25 (+ 26 fianza, 27 renta previa). El EN cambia **solo rótulo e
   importe** (research §8): ninguna fila se mueve y cada partida US cae en una fila de su misma clase.
6. **PyG**: A10 «Ventas de alquiler del espacio y servicios del evento» · A11 «Canon del catering exclusivo» · A13 «Coste directo
   del evento» · A14 «Coste del canon (no tiene)» · A15 consumibles · A16 «Comisiones de wedding planners y agencias» · fijos **26-35**
   (10) · ratios **51-56** (margen bruto · coste directo · personal · renta · neto).
7. **Personal**: 6 filas 5-10; `C11 = SUM(C5:C10)` = **3,35** con 2 auxiliares al 40 % (la ES no lo pudo arreglar: m13, deuda del
   motor) → **E4** en EN: `SUMPRODUCT(B5:B10,C5:C10)` = 3,75; `A2` fórmula «Convenio Hostelería — 14 pagas + SS 33 %» (gemela
   en la pizza EN). Cobertura `B18:B23` = 40 · 46 · 9,2 · 2,3 · 12 · 3 → 101 %.
8. **Instrucciones**: uso A4-A12, cifras A14-A31, **D19 en A33-A48** (cabecera A34 + 14 filas: Mes 1 · mezcla de eventos · techo
   de fechas · bodas en España 2024 · antelación · coste directo · canon · personal por evento · IVA · autoprotección · ruido ·
   comida testigo · agua de pozo · convenio), A50 desproteger, A51 catálogo, firma A52, **versión A53** (E1 en **A54**).
9. **Tesorería**: pesos `B5:M5` girados a Mes 1 = marzo con nota `O5`; `O13` (pagas extra) y notas de trimestres/303 del VOCABULARIO
   finca (`O16`…); filas 16-20 de IVA → las del Bar EN (sales tax collected / remitted), `A34` «plan quarters…» (texto de la pizza EN).
10. **Checklist**: molde C2 (cabecera `OK | TRÁMITE | RESPONSABLE | PLAZO | NOTAS`, contador por hoja, DV ✓/☐/N/A); pestañas ES
    **«F1 - Constitución» · «F2 - Finca y licencia» · «F3 - Obra y equipamiento» · «F4 - Personal y catering» · «F5 - Marca y
    reservas» · «F6 - Temporada y eventos»**; `Instrucciones!A3` con el **id** (defecto I5 del tapas: en EN, nombre comercial);
    versión **A11** (E1 en A12).

## 3. Clasificación de cadenas (`clasificacion`; 1.ª fuente con EN, exacta y tras normalizar la finca)

| Grupo | Cadenas | Palabras | Qué es | Va a |
|---|---|---|---|---|
| **PIZ-GM** (exacta) | 308 (294 plan · 13 check · 1 ambos) | 3.166 | motor 2.2 genérico, mismo ES que la pizza | **GM** tal cual |
| PAN-GM · PAN (exacta, Bakery EN) | 3 · 7 | 96 | títulos de hoja, «TASK», «Attorney» | GM / GR |
| PIZ · PIZ-GR (exacta, otra celda de la pizza) | 19 · 5 | 218 | rótulos del checklist («Gestoría» → «Accountant»), D19 («Estimación del kit» → «UpMenu»!) | **GR con revisión** (la mitad no vale en su celda) |
| BBQ (exacta) | 6 | 63 | rótulos cortos del checklist («Mes 2», «Proveedor» → «Owner / Pitmaster»!) | GR con revisión |
| **N-PIZ-GM · N-BAR** (tras normalizar invitado→cubierto, finca→local, canon→bebida…) | 20 · 4 | 361 | Supuestos A10-A14, PyG A13-A15/A24/A52, Personal A21-A23, Tesorería O7 | **GR como PROPUESTA**: el EN propuesto dice «FOOD/BEVERAGE», «covers», «shift» y hay que reescribirlo (venue rental & services / caterer commission / guests / event) |
| **WED** (sin fuente) | **436** (207 plan · 224 check · 5 ambos) | **7.045** (plan 4.375 · check 2.648 · ambos 22) | notas de Supuestos (49 · 1.486 pal.), Inversión (42 · 607), PyG (35 · 564), Instrucciones (53 · 871), Personal (17 · 419), Tesorería (4 · 334), checklist entero | **GWED-plan** y **GWED-check** (traductores) |
| GX · SIN-LETRAS | 66 · 3 | 279 | pestañas, docProps, CLAVES | `datos_wed.py` |

**Carga de traducción F2** (frente a la pizza: GPIZ-plan 139 + GPIZ-check 220 ≈ 6,3 K palabras): **xlsx ≈ 7,1 K** (plan ≈ 4,4 K + GR
≈ 0,7 K de revisión · check ≈ 2,65 K) · **Word ≈ 6,5 K** (61 ranuras) · **contrato ≈ 4,5 K** (150 párrafos, nuevo en EN) ·
**calculadora ≈ 2,8 K** (en código, como `calculadora_piz.py`). Total ≈ 21 K palabras ES → EN (pizza ≈ 14 K): el contrato es lo nuevo.

## 4. Docx (Word ES 1.0 final)

131 párrafos, **estilos 131/131 iguales a `docx_es_pael.json`**, 10 H1 en los índices de PAEL/PIZ, índice 24-33, ranuras
`fin_es_a` (29: 39-…, §1-5) y `fin_es_b` (32: …-117, §6-10) en `../plan-finca-eventos/textos/` (ES con `{TOKENS}`, 155 tokens en
`cifras_caso_es.json`). §9 = 102-108 (`DOCX_ULTIMO_9` '108': nota UK), `FIJOS[35]` = «Anexos: Plan Financiero Excel + Checklist de
Apertura Excel + Calculad…» y `FIJOS` 127-129 = venta cruzada ES (Catering & Kit Temático · Kit Gestión de Personal · Kit Plan
Financiero). Párrafos idénticos con los Word de referencia: piz 41, ft/cat/bbq/pael 30 (los FIJOS). **Sin anexo por comunidades**
(proporcionalidad ES): el EN tampoco lleva anexo por estado.

## 5. Calculadora (CALC, verde en ES: autotest 588 comprobaciones)

`calculadora_fin_es.py` (Python, tablas como fuente única): `Calculadora` (16 entradas verdes: canal · tipología · fecha · invitados
· 4 extras · horas y coste/h del personal · SS · coste de extras · redondeo · **canon 12 %** · **IVA 21 %** · IVA del menú 10 %; 41
salidas: temporada y día por tablas de meses/días de la semana, tarifa con ajustes, mínimo de invitados, IVA, total, presupuesto
«con IVA / + IVA», €/invitado, 3 cobros con fechas, menú y canon estimados, presupuesto completo, coste directo, margen, 5 tramos
de cancelación) + tablas visibles (tipologías, temporadas, días, meses, semana, extras, política por canal, tramos 12/6/3/1/0
meses) · `Ejemplos` (3 casos por las mismas fórmulas) · `Instrucciones` (626 palabras). Formatos `#,##0.00 €`, `dd/mm/yyyy`,
A4, protegida sin contraseña. **EN = `calculadora_wed.py`**: el mismo generador traducido y adaptado (SPEC D168), autotest pycel.

## 6. Contrato (nuevo en EN: ningún hermano EN lleva contrato)

`contrato_fin_es.py` (copia el docx del contrato del parrillero como molde físico, vacía el cuerpo y escribe `textos/contrato_es.json`
`[{estilo, texto}]` con `**negrita**`): **Modelo 1** reserva con particulares (Reunidos + 21 cláusulas + «Segunda bis» reserva
condicionada a la licencia) · **Anexo** empresas (7 viñetas) · **Modelo 2** catering exclusivo en concesión (13 cláusulas). EN =
`contrato_wed.py` (clon con **Letter**, docProps EN, aviso legal en cabecera) + `textos_en/contrato_en.json` (1 sonnet). Qué cruza,
cambia o se quita: SPEC D171.

## 7. Código que se clona (todo en `business-plans-en-9/`)

| Nuevo | Origen | Cambios |
|---|---|---|
| rama `elif CONJUNTO == 'wed'` en `../business-plans-en/mapas.py` | `:1240-1247` (piz) | único cambio en código común (+ mensaje de `:1249`) |
| `mapas_wed.py` | `mapas_piz.py` | `PLANES` (D156), `LIBROS` WEDP/WEDC, `FUENTE_ES` (`WED_FUENTE_ES` o `dl/plan-negocio-finca-eventos-bodas`), pestañas checklist (D169), `TAREAS_POR_FASE` 12/16/15/13/14/14, `PARCHES_FORMULA` **E2 `G14` + E4 `Personal!C11`** (sin E5), `FILA_VERSION` WEDP 53 · WEDC 11, `ZONAS_CELDA` D19 (A34-A48), docx `wed` (131, H1 de PAEL, `ULTIMO_9` '108', tandas `wed_a`/`wed_b`), `PRESTAMO_SEMILLA` ≈ 460,000, `AUTOTEST` con las pestañas ES de la finca, grupos `GM · GR · GWED-plan · GWED-check`; **diccionario por TEXTO**: EN de la pizza (GM, GR, GPIZ-plan, GPIZ-check + revisiones) → Bakery/BP (GPAN, GREST, GN, GM, GCAF, GFT) → BBQ/PAEL; normalización = **VOCABULARIO de la finca invertido** (como `normalizadores()` de `inventario_delta.py`), todo lo normalizado a GR |
| `datos_wed.py` | `datos_piz.py` | FIJOS, POR_CELDA, `VALORES_EN` (D160-D167), tokens del Word (los 155 del ES que sobrevivan + los US), pistas, glosario research §9, `CIFRAS_ES` + caso de la pizza EN (D173), `RX_WED_NO` |
| `bp9.py` | `bp8.py` | `verificar` con los sha256 de los 5 ficheros ES LIVE y de la pizza EN; subcomandos `calculadora`, `contrato`, `barrido` |
| `derivar_formulas_wed.py` · `formulas_wed_manual.py` | los de la pizza | gemela = celda con los mismos literales en la pizza EN/Bakery EN; manuales C9, D28, D38, F13, F14, O11 |
| `calculadora_wed.py` | `../plan-finca-eventos/calculadora_fin_es.py` | D168 |
| `contrato_wed.py` | `../plan-finca-eventos/contrato_fin_es.py` | Letter, `contrato_en.json`, docProps EN, gates (0 tokens, 0 español, no latinos, `RX_WED_NO`) |
| `inventario_delta.py` (este) · `resumen_entregables.py` · `barrido_wed.py` · `BRIEF-TRADUCTORES.md` (paso 1a de F2, como la pizza) | los de la pizza | `LIBROS`/`DOCX` de la finca; glosario §9 pegado entero |

## 8. Defectos del ES detectados (no bloquean el EN; para el carril ES)

- `Personal!C11` suma personas sin ponderar (3,35 frente a 3,75): deuda del motor ya anotada en la F2 ES (m13). El EN lo arregla
  con el parche E4 del propio conjunto.
- `PyG!G14` sale al 10 % con coste 0 (M7 ES, sin efecto en cifras): el EN lo lleva a `$B$41` (E2).
- `Checklist Instrucciones!A3` con el id interno: cosmético; el EN pone el nombre comercial.

## 9. Paso 1 de la F2-EN (re-medir solo si el ES cambia)

```bash
# VPS, worktree EN (/root/wt-wedding, rama feat/wedding-venue-business-plan-en); el ES es el LIVE de main
cd /root/wt-wedding/scripts/productos-digitales/business-plans-en-9 && PY=/root/venv-guias/bin/python
$PY inventario_delta.py > /tmp/wed-inv.txt     # → inventario_delta.json (2,7 s)
$PY bp9.py extraer_textos > /tmp/wed-ext.txt && $PY bp9.py extraer_docx > /tmp/wed-ed.txt && $PY bp9.py mapas
```
Si la ES cambia antes de las tandas (p. ej. un arreglo del carril ES), se re-extrae y se rehace `preparar_tandas`.
