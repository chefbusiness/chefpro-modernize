# Restaurant + Bakery Business Plan Kit (EN) — inventario DELTA de F1 (frente a food truck / coffee shop)

> Sesión Claude Code, 4-oct-2026. Fuente: los **6 ficheros ES PUBLICADOS** de `astro-site/public/dl/plan-negocio-bar-restaurante/`
> (REST) y `…/plan-negocio-panaderia/` (PAN), leídos con openpyxl / python-docx **en el VPS** (`/root/wt-bp2`, ya
> borrado). Script reproducible: `inventario_delta.py` → `inventario_delta.json` (cadenas clasificadas, estructura,
> rótulos, tokens, docx). Base heredada (solo lectura): `../business-plans-en/` (SPEC D1-D29, `textos_es.json`,
> `mapas.py`, `textos_en/GM.json`). Libros: **RESTP / RESTC** (plan financiero / checklist REST), **PANP / PANC**.
> Las celdas verdes se cuentan también vacías (en RESTC la col. E de OK está vacía).

## 0. Totales (comparables con F1-inventario-es.md §0)

| Libro | Hojas | Textos | Fórmulas | Fx→hoja | DV | CF | Merges | Verdes = desbloq. | Tareas | Papel |
|---|---|---|---|---|---|---|---|---|---|---|
| RESTP `plan-financiero-bar-restaurante.xlsx` | 9 | 729 | **772** | 430 | 24 | 70 | **15** | 180 | — | A4 |
| RESTC `checklist-apertura-bar-restaurante.xlsx` | **2** | 333 | 2 | 0 | **1** | 2 | 10 | 64 | **64** (7 fases) | A4 |
| PANP `plan-financiero-panaderia.xlsx` | 9 | 709 | **737** | 423 | **23** | 68 | 5 | 154 | — | A4 |
| PANC `checklist-apertura-panaderia.xlsx` | 7 | 383 | 12 | 0 | 6 | 12 | 6 | 66 | **66** (11/12/12/10/11/10) | A4 |

Las 18 hojas, protegidas **sin contraseña**. docProps de los 4 xlsx: `creator` AI Chef Pro, título ES «Plan financiero —
Bar-Restaurante / Restaurante Casual · v2.2» y gemelos; versión «2.2 · septiembre 2026».

| Docx | Párrafos | Con texto | Estilos | Palabras | Encabezados (índice de párrafo) | Página |
|---|---|---|---|---|---|---|
| REST `plan-de-negocio-bar-restaurante.docx` | **148** | 126 | Normal 138 + 10 Heading 1 | 6.973 | 37 · 45 · 53 · 61 · 69 · 78 · 97 · 104 · 113 · 123 | US Letter |
| PAN `plan-de-negocio-panaderia.docx` | **131** | 110 | Normal 121 + 10 Heading 1 | 6.906 | 37 · 45 · 52 · 59 · 68 · 76 · 84 · 94 · 104 · 111 | US Letter |

0 tablas, 0 imágenes, 0 párrafos multi-run con formatos distintos, 0 runs en rojo, **ningún «[Contenido pendiente»**
(el defecto I7 de la CAF no existe aquí; los aciertos de «pendiente» eran «independientemente» y «dependienta»).
Coinciden con los docx FT/CAF 47 (REST) y 44 (PAN) párrafos: portada, aviso, índice, separadores y fórmulas de cierre,
que escribe `ensamblar_docx.py` (`DOCX_FIJOS`). Palabras por tanda: **rest_a** §1-5 ≈ 3.180 (41 párrafos) ·
**rest_b** §6-10 ≈ 3.610 (63, de ellos ~9 de cierre fijo) · **pan_a** §1-5 ≈ 3.260 (39) · **pan_b** §6-10 ≈ 3.540 (49,
~6 de cierre fijo).

## 1. Cadenas: qué ya está traducido y qué es nuevo

Clasificación de cada cadena única de los 4 libros contra `../business-plans-en/textos_es.json` (comparación exacta):

| Grupo | Cadenas | Palabras | Plan / checklist / ambos | Qué es |
|---|---|---|---|---|
| **GM** (ya traducido en `textos_en/GM.json`) | 391 (REST usa 372, PAN 379) | 4.258 | 341 / 47 / 3 | Motor 2.2 + molde de checklist: se reutiliza sin traducir |
| GCAF reutilizable (EN en `textos_en/GCAF.json`) | 75 | 788 | 51 / 24 / 0 | Notas de supuestos (fianza, carencia, rotaciones, aforo, meses previos…) y trámites comunes; revisar contexto |
| GFT reutilizable (`textos_en/GFT.json`) | 10 | 77 | 5 / 5 / 0 | «Menaje y utensilios cocina», plazos («1-2 meses»), «Certificado digital»… |
| **GN** (nuevas comunes REST + PAN) | 6 | 22 | 4 / 0 / 2 | «Extra de fin de semana», «Coste de personal imputado al P&L», «Suministros», «Gestoría», «Marketing»… |
| **GREST** (nuevas, solo restaurante) | **344** | **2.989** | 208 / 134 / 2 | Partidas de inversión, fijos del P&L, puestos, «Cubiertos…», tablas D18/D19, checklist de una hoja |
| **GPAN** (nuevas, solo panadería) | **340** | **4.754** | 198 / 137 / 5 | Partidas de obrador, columna H, producción, «Transacciones…», tablas D18/D19 (notas largas), checklist |
| GX (no se traduce: pestaña, clave, FIJO, versión, pie, docProps) | 61 | 244 | — | Pestañas (las de REST son NUEVAS, §2.1), «Sí/No», rótulos que fija la SPEC |
| Sin letras | 23 | — | — | `✓ ☐ — N/A`, rangos numéricos (los de D18/D19 se localizan celda a celda) |

Para los traductores: **GREST ≈ 3,0 K palabras** y **GPAN ≈ 4,8 K** (más GN y los 85 reutilizables a revisar), frente a
5,2 K (GFT) y 4,5 K (GCAF). Las tablas D18/D19 de `Instrucciones` van celda a celda (REST D18 filas 34-45 + D19 49-58;
PAN D18 35-51 + D19 55-67; 4 columnas), como en FT/CAF.

## 2. Diferencias de estructura que obligan a generalizar (por orden de impacto)

1. **RESTP usa pestañas NUMERADAS** (molde v2.0 original del bar-restaurante): `1. Inversión Inicial`, `2. P&L 3 Años`,
   `3. Punto Equilibrio`, `4. Escenarios`, `5. Personal`, `6. Tesorería 12 meses`, `7. Financiación` (+ `0. Supuestos`,
   `Instrucciones`). Todo lo que en `mapas.py` direcciona por nombre ES fijo (`_P = 'PyG 3 Años'`, `_I`, `_E`, `_T`, `_F`,
   `_R`, `_ES`) necesita un resolutor por libro (`norm_hoja()` de `inventario_delta.py`: quita «N. » y `P&L 3 Años` →
   `PyG 3 Años`). Con él, `TOKENS_DOCX` resuelve 73 tokens en REST y 70 en PAN (§5).
2. **RESTC es otro molde de checklist**: UNA hoja `Checklist Apertura` (A1:G77) + `Instrucciones`; columnas `Fase |
   Trámite / Tarea | Responsable | Plazo | OK | Notas` (la col. A es la CATEGORÍA: Legal, Fiscal, Laboral, Local,
   Licencia, Obra, Equipo, APPCC, RRHH, Marca, Digital, Lanzamiento, Seguros, RGPD, Operación, Financiero, Marketing);
   **7 fases como filas-cabecera fusionadas** (A4, A15, A24, A33, A41, A50, A66 → tareas 10/8/8/7/8/15/8 = 64); OK en la
   **col. E** (verde, desbloqueada, vacía) con DV `"✓,—,N/A"` (no `☐`); CF `$E4="✓"` sobre A4:F74 + `containsText "✓"`;
   contador en B77/E77/F77/G77. `TAREAS_POR_FASE` y el G1 cuentan por hoja: hay que contar por fila-cabecera.
3. **PANC: pestañas `F1`…`F6`** sin sufijo (título de fase en A2: «FASE 1: CONSTITUCIÓN»…). Mismo molde que FT/CAF
   (`OK | TRÁMITE | RESPONSABLE | PLAZO | NOTAS`, A verde con `☐`, contador por hoja); solo cambia el mapa de pestañas.
4. **PANP lleva una columna H en el P&L**: `H4` «Pan común sobre la línea (%)», `H10` = 0,76 (verde, en la DV de umbrales
   `E51 E53:E56 H10`), y `G10` / `G13` = `$H$10*0.04+(1-$H$10)*'0. Supuestos'!$B$39`: el **IVA superreducido del pan común
   (4 %) escrito como literal**. Es el único sitio del motor con un tipo fiscal dentro de una fórmula → excepción E3 de la
   SPEC delta. `G13` (soportado de compras de comida) cae además dentro de E2.
5. **E2 en otras coordenadas**: soportado de compras en REST `2. P&L 3 Años!G14,G15`; en PAN `PyG 3 Años!G13,G14` (FT/CAF
   G13/G14 en su hoja). REST tiene una fila más arriba (A7 «Cubiertos/día» empieza en la fila 7).
6. **Marca ChefBusiness DENTRO del xlsx REST** (FT/CAF/PAN no la llevan en celdas): `A1` «ChefBusiness Consultoría
   Gastronómica» y última fila «ChefBusiness.co — Plan de Negocio: Bar-Restaurante» en 5 hojas (Inversión A1/A58, P&L
   A1/A62, PE A1/A41, Escenarios A1/A31, Personal A1/A30), más RESTC A1 y A76; de ahí los **15 merges** (A1:A3 × 5 hojas).
   `Inversión!A57`: «estimaciones basadas en precios de mercado en España 2026».
7. **Coordenadas propias**: `FILA_VERSION` RESTP 63 · PANP 72 · RESTC 11 · PANC 11. Umbrales del P&L: REST `E53,E55:E58`;
   PAN `E51,E53:E56` (+H10). PE: REST tiene techo de rotaciones en `B26` (verde) y tabla de sensibilidad A34:E39 con
   fórmulas en la col. A; **PANP no tiene ninguna DV en `Punto Equilibrio`** (23 DV, una menos). Personal: REST 7 puestos
   (B6:B12), jornada `B20`=40, semanas `B21`=46, horas de servicio `B22`=13 × personas `B23`=2; PAN 6 puestos (B5:B10),
   `B18`=40, `B19`=46, servicio `B20`=13 × `B21`=1,7 **+ turno de producción `B22`=3,5 h × `B23`=1 persona** (filas
   propias). Inversión: REST 38 partidas (filas 7-45, bloques local / cocina / sala y barra / marketing / legal /
   existencias), CAPEX en B49; PAN 19 partidas (7-25), CAPEX B32.
8. **Fórmulas con literales de texto fuera de `CLAVES`**: 16 en RESTP (Supuestos C9, C50; Inversión D11-D13, D47, D48,
   D50, D53-D55; P&L F14, F15, F19; PE A29; Tesorería O11) y 16 en PANP (Supuestos C9; Inversión D26-D28, D30, D31, D33,
   D36-D38; PyG F13, F14, F18; PE A26; **Personal A2**; Tesorería O11). Mismos textos que las 33 de `formulas_en.py` con
   otras referencias → 32 entradas nuevas de `FORMULAS_EN`, copiando la redacción EN de FT/CAF.
9. `Instrucciones` RESTP **no tiene la línea «8. El documento Word… versión 1.1»** (7 líneas numeradas); PANP sí (A12).
10. Docx: mismas 10 secciones; REST tiene la §6 larga (19 párrafos) y el cierre con 4 productos y precios en EUR
    (143-146 → `chefbusiness.co/productos-digitales/`); PAN cierre con 2 (128-129). Nada que mover (sin I7).

Lo que **sí es idéntico** (comprobado por rótulos): `0. Supuestos` (66/65 rótulos, 1-2 distintos: «Cubiertos/día» /
«Transacciones/día» y PAN B63 «…servida en mostrador»), `Tesorería 12 meses` y `Financiación` (0 rótulos nuevos), la
mecánica IVA/mezcla por canal (delivery B16/B17, alcohol B62/B63/B40, ya común al motor 2.2: la «mezcla de ventas por
canal» del RD-17 NO es estructura propia del REST, es un valor: REST alcohol 60 % de la bebida, PAN 0 %).

## 3. Caso ES (valores de partida, `0. Supuestos` y salidas en caché)

| | REST | PAN |
|---|---|---|
| Volumen · ticket sin IVA · días | 80 cubiertos · 18,20 € · 310 | 180 transacciones · 5,50 € · 310 |
| Mezcla comida/bebida · coste de mercancía | 65/35 · 30 % / 22 % | 92,5/7,5 · 29 % / 27 % |
| Alcohol sobre bebida · delivery | 60 % · 0 % (comisión 28 %) | 0 % · 0 % (30 %) |
| Alquiler · suministros · seguros | 3.000 €/mes · 1.800 · 2.000/año | 2.100 · 875 · 2.100 |
| Propios · préstamo · tipo · plazo · carencia | 75.000 · 128.000 · 6 % · 7 · 1 | 50.000 · 120.000 · 6 % · 7 · 1 |
| Ventas año 1 · CAPEX · inversión total · necesidad de caja | 451.360 · 118.210 · 179.015 · 201.718 | 306.900 · 101.600 · 145.215 · 164.808 |
| Neto año 1 · margen neto · personal % | 48.621 · 10,8 % · 33,7 % | 16.893 · 5,5 % · 37,1 % |
| DSCR año 1 / mínimo · holgura de caja · payback | **8,47** / 3,31 · 27,1 % · 2,3 años | **4,64** / 2,01 · 16,7 % · «Más de 3 años» |
| Plantilla · cobertura de horas | 7 puestos / 5,4 jornadas · 123 % | 6 / 4,39 · 101,8 % |

## 4. Defectos del ES que NO pasan al EN

- **I1-R · Docx REST contradice al Excel y a sí mismo**: inversión «80.000-150.000» (§1) y «133.000 €» (§8) frente a
  179.015 €; facturación «350.000 €» (§1, §8) frente a 451.360 €; equilibrio «40 cubiertos a 22 €» frente a ~65 a 18,20 €;
  préstamo «80.000 €» con «ICO» frente a 128.000 €; retorno «30-40 meses» frente a payback 2,3 años. Restos: comas sin
  espacio («hostelera,capacidad», «franjas:el»), portada/índice/encabezados sin tildes («Analisis», «Captacion»,
  «Espana»). Cierre con precios EUR y `chefbusiness.co`.
- **I1-P · Docx PAN**: inversión «105.000», «100.000-110.000», «75.000-130.000» (tres cifras) frente a 145.215 €;
  facturación «200.000 €» frente a 306.900 €; «110 transacciones a 5 €» frente a 180 a 5,50 €; equilibrio «114 a 4,5 €»
  frente a 162; personal «4-5 personas, 75-80 K €» frente a 6 puestos y 113.861 €; retorno «24-36 meses» frente a «Más de
  3 años»; mayorista «40 %» (§1) frente a «25-35 %» (§8). `Instrucciones!A12` lo admite («el Word es el de la v1.1»).
- **I3 · «Fuente»** de las tablas D19: REST «Fichero v1.1»; PAN «Versión anterior de este kit — contrástalo en tu zona».
  D18 de los dos con columnas «v1.1 | v2.2 | Por qué» (→ D18 de la SPEC heredada).
- **I4 · DSCR del año 1 inflado por la carencia**: REST 8,47× (mínimo 3,31×), PAN 4,64× (2,01×). EN: interest-only 0 (D17).
- **I5 · Checklist `Instrucciones!A3`** con el id interno («plan-negocio-bar-restaurante», «plan-negocio-panaderia»).
- **I8 · RESTC: las instrucciones contradicen al libro**: A5 dice «elige ✓, ☐ o N/A» y la DV ofrece `✓, —, N/A`.
- **I9 · Marca ChefBusiness y «España 2026» dentro del xlsx REST** (§2.6) y en PAN `Inversión!A2` «Inversión Inicial —
  España 2026».
- **I10 · PAN `Instrucciones` D19** incluye «Epígrafe de IAE», «Registro sanitario» y «PROVINCIAL de hostelería/
  alimentación»; REST «Tasa de cierre de restaurantes 25 % / 50 %» con fuente «Fichero v1.1» (sin fuente real: el EN no
  la cita salvo con fuente).

## 5. Tokens del docx (`mapas.TOKENS_DOCX`) en los dos planes

Con el resolutor de pestañas y rótulo por plan: **REST 73 / PAN 70** tokens resueltos. Hay que añadir claves `rest` /
`pan` a los rótulos por plan: `clientes_*` → «Cubiertos/día (media del año 1)» / «Transacciones/día (media del año 1)»
(y «…(media)», «Cubiertos/día» / «Transacciones/día» en Escenarios); PE «Cubiertos necesarios al día (caja)» /
«Transacciones necesarias al día (caja)»; PAN `marketing_anual` → «Marketing»; `ocupacion_*` → «Alquiler del local» /
«Alquiler / Ventas» (como CAF); `aforo` y `rotaciones_dia` solo REST (PANP no tiene B50); `inv_*` nuevos por plan
(REST: obra, cocina, campana, barra, sala, licencias; PAN: horno, amasadora, cámara de fermentación, vitrina, obra,
instalación eléctrica). Los tokens FT-only (vehículo, generador) no aplican.
