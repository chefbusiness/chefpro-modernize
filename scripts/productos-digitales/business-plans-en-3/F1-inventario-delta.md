# Bar Business Plan Kit (EN) — inventario DELTA de F1 (frente a FT/CAF + REST/PAN)

> Sesión Claude Code, 11-oct-2026. Fuente: los **3 ficheros ES PUBLICADOS** de `astro-site/public/dl/plan-negocio-tapas-bar/`
> (v2.2), leídos con openpyxl / python-docx **en el VPS** (`/root/wt-bar`, venv `/root/venv-guias`). Script
> reproducible: `inventario_delta.py` → `inventario_delta.json` (cadenas clasificadas con su EN reutilizable, estructura,
> parecido celda a celda con los 8 libros ya traducidos, fórmulas con texto, caso ES, tokens del docx, docx). Base
> heredada (solo lectura): `../business-plans-en/` (BP: GM, GFT, GCAF) y `../business-plans-en-2/` (BP2: GN, GREST, GPAN).
> Libros: **BARP** (plan financiero) y **BARC** (checklist). sha256 de las fuentes medidas:
> BARP `a757e15d7edb0c8d48b991da382162fbbb89fa40c3ac4c96979e0ac389f40a52` ·
> BARC `ead943337ddbde7fdee5e085e8d65dd07c0959588a680612f08c5a0be001927f` ·
> docx `73103bb9fe4629ce9d9daace333a053e85f46f596ff97fefaedf7a4ad5e8d2c8` (Mac y VPS iguales).
>
>     ssh vps 'cd /root/wt-bar/scripts/productos-digitales/business-plans-en-3 && /root/venv-guias/bin/python inventario_delta.py'
>
> Corre en ~2 s. Salida idéntica (sha256 `d74f3591…`) en el VPS y en la copia commiteada.

## 0. El hallazgo que manda: el Bar es un GEMELO ESTRUCTURAL DE LA CAFETERÍA, no del restaurante

| Comparación (hojas normalizadas) | Pestañas | Fórmulas idénticas en la misma celda | Rótulos col. A en la misma fila |
|---|---|---|---|
| BARP vs **CAFP** | 9/9 | **631/742 (85 %)** | 252/385 |
| BARP vs FTP · PANP | 9/9 | 482 · 484 /742 | 220 · 222 /385 |
| BARP vs RESTP (pestañas numeradas) | 9/9 | **137/742** | 145/385 |
| BARC vs **CAFC** | **7/7** (`F1 - Constitución` … `F6 - 90 Días`, mismo nombre) | 10/12 | **92/100** |
| BARC vs RESTC (una hoja) · PANC (`F1`…`F6`) | 1/7 · 1/7 | 0/12 | 6 · 7 /100 |

Consecuencias para F2: **el código es el del molde FT/CAF** (`_HOJAS_PLAN`, checklist de 6 hojas con OK en la col. A,
`MOLDE_CHECK = 'hojas'`, `COL_OK = 1`), sin el resolutor de pestañas numeradas ni el molde de una hoja de RESTC. Del
restaurante se reutiliza **el contenido** (alcohol, cubiertos, propinas, licencia de alcohol, 66 cadenas ya en EN), no la
estructura. Tampoco aplica E3 (pan exento): no hay columna H en el P&L.

## 1. Totales (comparables con BP2 `F1-inventario-delta.md` §0)

| Libro | Hojas | Textos | Fórmulas | Fx→hoja | DV | CF | Merges | Verdes = desbloq. | Tareas | Papel |
|---|---|---|---|---|---|---|---|---|---|---|
| BARP `plan-financiero-tapas-bar.xlsx` | 9 | 721 | **742** | 425 | 24 | 70 | 5 | 154 | — | A4 |
| BARC `checklist-apertura-tapas-bar.xlsx` | 7 | 428 | 12 | 0 | 6 (`"✓,☐,N/A"`) | 12 | 6 | 73 | **73** (11/13/13/12/14/10) | A4 |

Las 16 hojas, protegidas **sin contraseña**. docProps: `creator` AI Chef Pro, título ES «Plan financiero — Tapas Bar /
Gastrobar · v2.2» y «Checklist de apertura — …», `keywords` «plan negocio tapas bar, AI Chef Pro», `description`
`aichef.pro/plan-negocio-tapas-bar`. Fila de versión: **BARP `Instrucciones!A74`**, **BARC `Instrucciones!A11`** (E1 del
aviso D21 debajo: A75 / A12). Firma en BARP A73; «Más plantillas…» en A72.

| Docx | Párrafos | Con texto | Estilos | Palabras | Encabezados (índice de párrafo) | Página |
|---|---|---|---|---|---|---|
| `plan-de-negocio-tapas-bar.docx` | **133** | 111 | Normal 123 + 10 Heading 1 | 6.853 | 37 · 45 · 52 · 60 · 69 · 79 · 86 · 96 · 104 · 111 | US Letter |

0 tablas, 0 imágenes, 0 runs con formatos distintos, 0 en rojo, ningún «pendiente». **42-43 párrafos idénticos** a los
docx FT/CAF/REST/PAN (portada, aviso, índice, separadores): los escribe `ensamblar_docx.py` (`DOCX_FIJOS`). Palabras por
sección: §1 622 · §2 550 · §3 680 · §4 823 · §5 882 (**bar_a ≈ 3.560**, 42 párrafos) · §6 540 · §7 803 · §8 671 · §9 545 ·
§10 586 (**bar_b ≈ 3.150**, 47 párrafos, de ellos ~9 de cierre fijo: 124-132).

## 2. Cadenas: qué ya está traducido y qué es nuevo

Cada cadena única de los 2 libros (celdas, DV, pestañas, pie, docProps) contra el EN ya escrito de BP y BP2 (comparación
exacta; prioridad GM → REST → CAF → PAN → FT):

| Grupo | Cadenas | Palabras | Plan / check / ambos | Qué es |
|---|---|---|---|---|
| **GM** (EN en `../business-plans-en/textos_en/GM.json`) | 407 | 4.293 | 349 / 56 / 2 | Motor 2.2 + molde de checklist: se reutiliza sin traducir |
| **REST** reutilizable (BP2 GREST/GN) | 66 | 886 | 51 / 15 / 0 | Notas de cubiertos, rotaciones, alcohol, Veri*factu→POS, videovigilancia, PE «cubiertos» |
| **CAF** reutilizable (BP GCAF) | 57 | 362 | 23 / 34 / 0 | Trámites de local y constitución, filas de Instrucciones |
| PAN · FT reutilizables | 7 · 6 | 51 · 43 | — | Música (SGAE→ASCAP/BMI), «no existía», alta 036 |
| **BAR (nuevas)** | **263** | **3.463** | **153 (2.803) / 109 (652) / 1 (8)** | Partidas de inversión, fijos del P&L, puestos, tabla D19 del sector, notas del checklist, títulos |
| GX (no se traduce: pestañas, CLAVES, versión, pie, docProps) | 71 | 279 | 57 / 7 / 7 | Lo escribe `mapas` (D20) |
| Sin letras / invariables | 20 | — | — | `✓ ☐ — N/A`, rangos («28-32 %») que se localizan celda a celda |

- **Reutilizables a revisar = 25**, todos en las tablas D18/D19 de `Instrucciones` (EN «por celda» en BP/BP2: valen solo
  para su celda de origen). El resto de los 136 reutilizables (REST/CAF/PAN/FT) entran del diccionario con marca «revisar
  contexto» (como las 85 de BP2).
- Zonas celda a celda de `Instrucciones`: **D18 filas 34-50** (cabecera A33 «QUÉ HA CAMBIADO RESPECTO DE LA VERSIÓN 1.1»),
  **D19 filas 53-69** (cabecera A52 «DATOS DE REFERENCIA DEL SECTOR»): 122 cadenas / 1.243 palabras (68 BAR).
- Para los traductores: **≈ 3,5 K palabras nuevas** en xlsx (frente a 3,0 K GREST y 4,8 K GPAN de BP2) + 2 docx-tandas.

## 3. Diferencias de estructura frente a la CAF (lo que F2 tiene que mapear)

1. **Inversión Inicial más corta**: 18 partidas tecleadas (filas 7-24) + fianza B25, alquiler previo B26, imprevistos B27
   (fórmulas), fondo de maniobra B28-B29, **INVERSIÓN TOTAL B30, CAPEX B31**, IVA soportado B32, necesidad de caja B33,
   bases de amortización B35 (obra = B9+B10+B11+B12+B16+B20+B21+B27) / B36 (equipo = B13+B14+B15+B17+B18+B19+B24),
   amortización B37. Son las 46 fórmulas «sin gemela» de esta hoja (desplazamiento de filas, misma lógica). El resto sin
   gemela: PyG B23:D23 y B35 (apuntan a `Personal!G12/B16/B17` e `Inversión!B37`), Escenarios B24:D25, Personal H5/I5,
   Supuestos C50 y PE A28 (gemela en RESTP A29).
2. **Fórmulas con texto: 17**. 14 tienen gemela con los mismos literales (C9, D25, D26, D29, D30, D32, D35, D36, F13, F14,
   F18, PE A28, Personal A2, Tesorería O11 → EN derivable como BP2 `derivar_formulas.py`). **3 nuevas**: `0. Supuestos!C50`
   (rotaciones: «El documento de este plan pide 1,8 servicios por…»), `Inversión!D27` (lista de partidas de obra) e
   `Inversión!D37` (lista de lo que no se amortiza). Van escritas a mano (patrón `formulas_rp_manual.py`).
3. **E2 en las mismas celdas que la CAF**: `PyG 3 Años!G13,G14` (fórmula idéntica) → `'0. Supuestos'!$B$41`.
4. **E4 aplica** (como REST/PAN): `Personal!C12` = `SUM(C5:C11)`; en cuanto una fila tenga más de 1 persona el total de FTE
   miente → `SUMPRODUCT(B5:B11,C5:C11)`.
5. **Personal con turno de producción** (como PAN): `B19` jornada 40 · `B20` semanas 46 · `B21` horas de servicio 9,5 ×
   `B22` personas 2 · **`B23` horas de producción 3,5 × `B24` personas 2**; 7 puestos (B5:B11), total fila 12.
6. **Rótulos propios** (nuevos frente a los 8 libros): Inversión 13 (filas 1, 3, 8, 12-17, 19, 20, 23, 24), PyG 5 (A2, A10,
   A11, A27, A29), PE 2, Personal 3 (A5, A7, A8), Instrucciones 19 (A1, A11, A12, D18/D19), checklist 8 (A1 de las 6 hojas
   «CHECKLIST APERTURA — TAPAS BAR / GASTROBAR», `Instrucciones!A3` con el id, A11 versión). `0. Supuestos`, Escenarios,
   Tesorería y Financiación: **0 rótulos nuevos** (la fila 4 dice «Cubiertos/día (media del año 1)» como REST).
7. **Umbrales del P&L**: `PyG!E50` 0,68 (margen bruto ≥) · `E52` 0,30 (mercancía ≤) · `E53` 0,36 (personal ≤) · `E54` 0,12
   (alquiler ≤) · `E55` 0,05 (neto ≥). PE: techo de rotaciones `B25` = 3 (verde).
8. **Checklist**: mismo molde CAFC (A1 título, A2 fase, cabecera fila 4 `OK | TRÁMITE / ACCIÓN | RESPONSABLE | PLAZO |
   NOTAS`, contador por hoja); solo cambia el nº de tareas de F3 (13 frente a 15 → `C19/E19` del contador). **No hay
   ninguna tarea de licencia de alcohol** (en España no existe como trámite propio): ver SPEC D52.
9. `Instrucciones!A12` (BARP) **admite que el Word es el de la v1.1** («las cifras válidas son las de este Excel»).

## 4. Caso ES (celdas verdes y salidas en caché)

| Volumen · ticket sin IVA · días | 56 cubiertos · 18,00 € · 300 | Aforo · rotaciones implícitas | 45 · 1,24 |
|---|---|---|---|
| Comida/bebida · coste mercancía | 55,6 / 44,4 · 30 % / 25 % | Alcohol sobre bebida · delivery | 85 % · 0 % |
| Alquiler · suministros · seguros | 2.500 €/mes · 800 · 2.400/año | SS · pagas · SMI | 33 % · 14 · 17.094 € |
| Propios · préstamo · tipo · plazo · carencia | 50.000 · 129.000 · 6 % · 7 · 1 | Vidas obra / equipo | 10 / 8 |
| Ventas año 1 · CAPEX · inversión total · caja | **302.400** · 109.450 · 153.327 · 174.317 | Neto año 1 · margen neto | 20.637 · 6,8 % |
| Margen bruto · mercancía · personal · alquiler | 69,4 % · 27,8 % · **35,8 %** · 9,9 % | Plantilla · cobertura | 7 / 4,3 FTE · 101 % |
| Equilibrio contable / caja · holgura | 49,5 / 46,8 cubiertos · 19,6 % | DSCR año 1 / mínimo | **4,98** (carencia, I4) / 2,29 |
| Payback proyecto / CAPEX | 2,8 / 2,2 años | Escenarios pes./opt. | 42 × 16 € / 70 × 20 €, 300 días |

Tokens del docx (`mapas.TOKENS_DOCX` con los rótulos de la CAF): **74 resueltos**; faltan 12 que F2 resuelve con rótulos
del Bar: `clientes_dia/_a2/_a3`, `equilibrio_*_clientes_dia`, `pesimista/optimista_clientes` (el Bar dice «Cubiertos…»
como REST), `inv_lanzamiento` («Marketing lanzamiento», el rótulo del FT), `inv_stock`, `inv_mobiliario`, `inv_barra`
(rótulos propios) e `inv_espresso` (no aplica). Tokens nuevos propuestos: `inv_licencia` (fila 8), `inv_grifos` (16),
`inv_cocina` (13), `inv_frio` (14), `bebida_pct` (B12) y `prime_cost_pct` (derivado, como REST).

## 5. Defectos del ES que NO pasan al EN

- **I1-BAR · Docx v1.1 contra el Excel**: inversión «115.000 €» (§1 [41], §8 [98], con desglose que suma otra cosa) y
  «100.000-140.000 € habituales» ([41], [59]) frente a 153.327 € (CAPEX 109.450 €); facturación «270.000 €» ([42], [99])
  frente a 302.400 €; años 2-3 «320.000 / 370.000» frente a 347.760 / 382.536; equilibrio «34 clientes a 18 €» ([101])
  frente a 49,5; «1,8 servicios por cubierto» ([42]) frente a 1,24; fondo de maniobra «12.000 €» frente a 43.877 €.
  Retorno «18-30 meses» frente a payback 2,8 años. Restos: «raw material» en inglés ([48]), «lokal» ([116]), encabezados
  e índice sin tildes («Analisis», «Captacion», «Accion»). Cierre ChefBusiness con 3 productos en EUR y `chefbusiness.co`.
- **I3 · «Fuente: Fichero v1.1»** en las 15 filas de D19 (A54-A68). D18 con columnas «v1.1 | v2.2 | Por qué».
- **I4 · DSCR del año 1 inflado por la carencia**: 4,98× (mínimo 2,29×). EN: interest-only 0 (D17).
- **I5 · Checklist `Instrucciones!A3`** con el id interno («plan-negocio-tapas-bar»).
- **I9 · «España 2026»** en `Inversión!A2/A3` («Rangos mercado español actual»), `PyG!A2` «40-50 plazas», `Personal!A2`
  «Convenio Hostelería — 14 pagas + SS 33 %» (fórmula con texto).
- **I10 · D19** con ratios sin fuente («Ocupación fin de semana 80-95 %», «Merma 3-5 %», «Consumiciones de barra
  35-45 %», «EBITDA 15-22 %», «Retorno 18-30 meses») y convenio PROVINCIAL: el EN solo cita lo que tiene fuente (D19).
- **Ficha ES** (para F3): «73 trámites» (correcto), «742 fórmulas» (correcto), equilibrio «50 / 47 / 19,6 %» (correcto),
  pero testimonios con «63 trámites», «break-even de 34 clientes», «préstamo ICO», «licencia clasificada» y
  `aggregateRating` 4,9 (capa ES).
