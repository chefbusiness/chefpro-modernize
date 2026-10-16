# CONFIG-NOTAS — capa numérica EN de los 8 xlsx (`config_en.py`)

> Sesión Claude Code, 17-oct-2026. Solo lectura de los ES; nada recalculado en el Mac.
> **Dry-check**: 175 celdas destino (100 entradas `num`), todas constantes numéricas del ES (ninguna fórmula, ninguna
> vacía); las 150 celdas de `impuesto0` valen exactamente lo que escribe el EN; los valores ES copiados en el config
> (PVP, sueldos, B8) coinciden con los libros. `aplicar_en.py` corrido en seco sobre los 8 ES hacia un directorio
> temporal: 175 entradas cambiadas (24/14/69/3/3/17/36/9), 0 abortos (solo faltan los `textos_en/`).

## 1. Operaciones

| Libro | Hoja!rango | ES | Op → EN | D |
|---|---|---|---|---|
| capex | Parámetros!B6 | 90 m² | ×10.7639 → 968.75 sq ft | D8 |
| capex | Parámetros!B7:B9 | 600 / 900 / 1,200 €/m² | ÷10.7639 → 55.74 / 83.61 / 111.48 $/sq ft | D8 |
| capex | Parámetros!B13:B15 | 0.21 / 0.10 / 0 | set 0 | D7 |
| capex | CAPEX por Bloque!H7:J7 · H8:J8 | 3,354.12 · 2,513.41 (con IVA) | set ÷1.21 → 2,772.00 · 2,077.198… | D7 |
| capex | CAPEX por Bloque!F7:F8 | «Sí» | texto `EN_NO` = 'No' | D7 |
| capex | Traspaso vs Obra Nueva!C26:C30 | 85/69/80/63/63 m² | ×10.7639 (F26:F30 pasan a $/sq ft) | D8 |
| capex | Variante del Formato!K15:L17 | 100k-150k · 3k-30k · 8k-20k (PS-05/01/02) | set 50k-100k · 15k-25k · 75k-150k (Zenind 2026, T01) | PENDIENTES |
| capacidad | Parámetros!B14 · Ficha!F13 | 90 · 92 m² | ×10.7639 → 968.75 · 990.28 | D8 |
| capacidad | Zonas y m2!D6:D12 | 45/22/5/4/3/8/3 m² | ×10.7639 | D8 |
| capacidad | Capacidad por Equipo!E14 · G14 | 0.93 m² · 130 piezas/m² | ×10.7639 → 10.01 · ÷ → 12.08 (H14 igual) | D8 |
| capacidad | Parámetros!B19:B20 · Ficha!F8 | 40 / 50 m³/h·kW · 1,400 m³/h | ÷1.69901 → 23.54 / 29.43 CFM/kW · 824.0 CFM | D8 |
| carta | Parámetros!D6:D8 | 1,427.89 / 1,376.91 / 1,192.42 | ×1.25 | D12 |
| carta | Parámetros!B11 | 15 pagas | set 12 | D12 |
| carta | Parámetros!B19:B21 | 0.10 / 0.04 / 0.10 | set 0 | D7 |
| carta | Parámetros!B28:B29 | 4 °C / 8 °C | set 41 (°F, Food Code) | D15 |
| carta | Coste Hora y Mano de Obra!M6:M35 | 0.10 ×26 · 0.04 (M24:M27, panes) | set 0 | D7 |
| carta | Coste Hora y Mano de Obra!L6:L35 | PVP con IVA | set L/(1+M) (1.60 → 1.4545…; pan 1.20 → 1.1538…) | D7 |
| equip. | Equipamiento!C7 | 0.21 | set 0 | D7 |
| equip. | Equipamiento!I16 · I17 | 3,354.12 · 2,513.41 (con IVA) | set ÷1.21 | D7 |
| equip. | Equipamiento!J16:J17 | «con IVA» | texto `EN_SIN_IVA` = 'pre-tax' | D7 |
| licencias | Ruta Doméstica!B6 · B15 | 12 m² · 8 kg/m²·sem | ×10.7639 → 129.17 · ÷ → 0.743 (B16-B17 igual) | D8 |
| licencias | Cronograma y Ruta Crítica!C49 | 3 | set 5 | D13 |
| picos | Parámetros!B17 · B18 | 1,192.42 · 15 | ×1.25 · set 12 | D12 |
| picos | Parámetros!B25:B26 · Calendario!G6:G11 | 0.10 / 0.04 · 0.10 ×6 | set 0 | D7 |
| picos | Calendario de 6 Picos!H6:H11 | 16.5/2.1/3.6/2.4/3.5/1.6 | set ÷1.1 | D7 |
| picos | Calendario de 6 Picos!D8 | 3 | set 5 (ninguna fórmula, CF ni DV lee la col. D) | D13 |
| plan | 0. Supuestos!B8 | 2.4557 (PVP medio con IVA) | set ÷(1+B20 ES = 1.08792344) → 2.2572360423 (B10 idéntico) | D7 |
| plan | 0. Supuestos!B15:B18 | 0.10 / 0.04 / 0.21 / 0.10 | set 0 (B20 = 0) | D7 |
| plan | 0. Supuestos!B26 · B27 | 15 · 17,094 (SMI anual) | set 12 · set 15,080 | D12 |
| plan | 0. Supuestos!B36 | 201,826.48 | set 167,915.61 (ver §4.2) | D7 |
| plan | 0. Supuestos!B54:B56 | 7 / 12 / 3 (meses de paga extra) | set 0 | D12 |
| plan | Inversión Inicial!E6:E16 | 0.21 ×7 · 0 ×4 | set 0 | D7 |
| plan | Inversión Inicial!D6:D10, D14, D15 | «Sí» | texto 'No' (si no, la comprobación B23 sale 7 y en rojo) | D7 |
| plan | PyG 3 Años!F23:F30 | 0 · 0.21 ×7 | set 0 (F12, F13, F15, F21, F22 son fórmulas a Supuestos) | D7 |
| plan | Personal!E15:E20 | 6 brutos | ×1.25 | D12 |
| plantilla | Parámetros!C8:C13 | 6 brutos | ×1.25 (D8:D13 «anual publicado» se queda: es idéntico) | D12 |
| plantilla | Parámetros!C15 · C17 | 15 · 17,094 | set 12 · set 15,080 (17,886.30 ≥ 15,080: veredicto intacto) | D12 |
| plantilla | Plan de Contratación!D18 | 3 | set 5 (nadie lo lee) | D13 |

Precisión: los PVP se fijan con la misma expresión de la fórmula ES (`v/(1+t)`), bit a bit igual al «sin IVA» del ES;
anual 15 pagas vs 12 pagas × 1.25: diferencia máx. 3.6e-12. `dv` vacío en los 8: ninguna validación lista tipos de IVA
españoles (todas son decimales 0-1, 1-12, 12-16 pagas… compatibles con los valores EN). `FORMATOS`: `#,##0.00 €` →
`#,##0.00`, `dd/mm/yyyy` y `yyyy-mm-dd` → `mm/dd/yyyy` (únicos formatos con € o fecha en los 8 `styles.xml`). `HF`: el
único patrón de pie es «… Página &P de &N»; no hay cabeceras. Papel: los 53 `pageSetup` llevan `paperSize="9"`.

## 2. Literales de fórmula dependientes de España

**Numéricos: ninguno.** Barridos todos los tokens numéricos de fórmulas, formato condicional y validaciones de los 8
libros: solo 0-12 (índices de mes y posición), 7 (días/semana), 30 (días/mes), 60, 100, 365, 1000, tolerancias
(0.005, 0.01, 0.05, 0.5) y `MAX(12, pagas)` (con 12 pagas da 12). Ni `*15`, ni `/1.1`, ni `0.21`, ni `1780`, ni umbrales
en °C: pagas, IVA, horas y techos están siempre en celda.

Fórmula que **sí lee un mes de pico**: `Cronograma y Ruta Crítica!C42` = `COUNTIF($C$47:$C$52,C40)` (aviso «abres dentro
de una campaña»). Con C49 = 5 deja de avisar si abres en marzo (mayo ya avisaba por Comuniones); con la apertura del
caso (mes 9) da «No» en ES y EN.

Literales de TEXTO con cifras de la ley española (paso de textos / D15, no numérico): `Canales y Punto Muerto!B27`
(«Por encima del 25 %: … vía de los 500 kg»), `Suministro a Otros Minoristas!B7, B41, B42` (art. 3), `Ruta
Doméstica!B14, B18, B43` (art. 13.9), `Decisión de Huevo y Temperatura!J6:J35` (art. 4.1 fila 9 / art. 9.3),
`Horas y Coste!N7`, `Parámetros!C18` (plantilla) y `Personal!B25` (plan) (veredictos convenio/SMI).

## 3. Constantes que parecen fiscales, de unidad o laborales y se dejan a propósito

- SS 0.33 (carta B12, picos B19, plantilla C21, plan B25) y 1,780 h (carta B13, picos B20, plantilla C23): D12.
- `capex Parámetros!B23` (3, periodicidad) y `B24` (4 meses hasta recuperar): viven en «VAT-GST & Cash» (UK/CA/AU).
- `plan 0. Supuestos!B19` 0.201276 (peso del pan): reparte ventas (PyG B12/B13); con los tipos a 0 ya no pesa en B20.
- `Equipamiento!O16:O17` 2,772 / 2,077.20 y `C9` 66,980.34; `Inversión Inicial!B6:B16`: ya son base sin IVA.
- `carta Parámetros!B30` 24 h (es el disparador del *date marking* del Food Code, «> 24 h») y `B31` 20 mg/kg (= FDA
  gluten-free < 20 ppm). Gramos, €/kg, kW, kg/semana: D8.
- **Impuesto de Sociedades** `plan 0. Supuestos!B43:B44` (15 % / 25 %): D7 solo cubre el IVA. Se queda. Pasarlos al 21 %
  federal (C-corp) cambiaría resultado neto, ratios y todas las cifras netas del texto: decisión de John/orquestador.
- **Altura (m) y volumen (m³)**, fuera de la lista de D8: `capacidad Parámetros!B22` 3 m y `Ficha!F12` 3.2 m (solo se
  comparan entre sí, H12); `Capacidad por Equipo!E13` 8 m³ y `G13` 70 piezas/m³ (solo H13 = E13×G13). Si se quieren en
  pies: `('mul', 3.280839895013123)` en B22 y F12; `('mul', 35.31466672148859)` en E13 y su inverso en G13 (veredictos
  y capacidades idénticos) + factores al gate + avisar al paso de textos.
- **km** (`Suministro!D11:D16`, `B30` 50 km): D8 no los lista y la hoja se reconcibe (D15).
- **Cifras de la ley española en las hojas de D15** (no son unidades): `Suministro!B20` 25 %, `B23` 500 kg, `B24` 380 kg,
  `B30` 50 km; `Ruta Doméstica!B7` 60 kg, `B13` 100 kg (art. 13.9); `Registro de Formación!D6:D10` 6 h y `B13` 730 días;
  `Checklist Legal!E/F` (plazos y costes por trámite); `Canales!B26` 25 %. El research US no da equivalentes 1:1
  (cottage food usa topes de ventas anuales, la food handler card dura 2-3 años según estado): quien reescriba D15 fija
  sus valores y añade aquí los `set`.
- Precios de ficha y traspasos (Barcelona, PS-69), pedido mínimo 300 € → $300, publicados del sector (PS-0x, 137,000):
  D6 (cifra intacta).

## 4. Decisiones tomadas que conviene validar

1. **Temperaturas 41 °F** y no la conversión exacta (39.2 / 46.4 °F): son techos legales (hoja «Egg & TCS Decision») y
   D15 + DECISIONES §7 mandan la cifra del Food Code. Ninguna fórmula compara con un umbral fijo en °C (G/H/I solo
   arrastran el valor y MIN). Cambiar: `TECHO_TCS_F`.
2. **Recursos propios 167,915.61**: la nota C36 dice que se siembra «necesidad total de caja menos el préstamo». Sin IVA
   adelantado la necesidad baja a 227,915.60 (la parte sin IVA es idéntica). Con 201,826.48 el plan saldría
   sobrefinanciado (+33,910.88 en Financiación!B12) y B14 diría que basta un préstamo de 26,089.12. Solo lo leen
   Financiación!B6→B9, B12-B14 (la caja de Tesorería arranca del fondo de maniobra). Para revertir, quitar la línea de
   `num` y la de `impuesto0`. **Cifra nueva para DECISIONES §3-bis** (texto T10/T11/P01/P02).
3. **Pagas en CUATRO libros**, no tres: también `estacionalidad Parámetros!B18` (con su bruto B17), que da el coste hora
   del refuerzo (B21 queda idéntico).
4. **SMI**: los xlsx guardan el ANUAL (17,094 = 1,221 × 14) → 15,080 = 7.25 × 2,080. Rótulo EN sugerido: «Minimum
   wage, full-time (annual: $7.25 × 2,080 h)»; el $1,256.67/mes va en el texto. Meses de paga extra → 0 (la nota C56
   del ES ya lo indica para 14 pagas); las notas C54-C56 hay que reescribirlas.
5. **Textos de opción fijados** con el cambio numérico: 'No' (capex F7:F8, plan D6:D15) y 'pre-tax' (equipamiento
   J16:J17). `textos_en` debe traducir «No» → 'No' y «sin IVA» (Equipamiento!E61, lista «Base del precio») → **'pre-tax'**
   exactamente, o cambiar `EN_NO` / `EN_SIN_IVA`.

## 5. Avisos para el gate y para el paso de textos

- **Bloqueo (PENDIENTES-XLSX, T01)**: `Variante del Formato!K18:L22` (15k-50k, 60k-100k ×2, 150k-250k, 83k-180k) deberían
  quedar VACÍAS en EN («seven rows carry no published range»). `aplicar_en.py` no tiene op de vaciar (solo `mul`/`set`
  numérico) y el gate G1 exige las mismas celdas con valor en ES y EN. Hace falta una op `('vaciar',)` (cambiar la celda
  por `<c r=".." s=".."/>`) + excepción declarada en el gate; M18:M22 pasan a «» (la fórmula ya contempla K/L vacías).
- **Gate G3 marcará `Inversión Inicial!B23`** (EN 0 ≠ ES-impuesto-0 7): `crear_t0` solo aplica `impuesto0` numéricos, no
  los `texto`. Es la adaptación declarada; aceptarlo o enseñar a `crear_t0` a poner «No» en D6:D16.
- `impuesto0` lleva además los ajustes no fiscales (sueldos, pagas, SMI, meses, temperaturas, recursos propios): el gate
  los listará como «dependen del impuesto». Las conversiones de unidad no van ahí: `FACTORES_UNIDAD` = sq ft/m², su
  inverso y CFM/(m³/h).
- **Comentarios de celda sin tratar**: 23 partes `xl/comments/*.xml` en los 8 libros (citas «Verificado el 10-09-2026 ·
  RD 1021/2022…», BOE, Decreto 26/2026…). Ni `censo_textos.py` ni `aplicar_en.py` las leen y el gate solo busca «€» en
  ellas: saldrían en español. Hay que añadirlas al censo y a `aplicar_en.py` (o vaciarlas).
- Textos que deben acompañar a las cifras: m2 → sq ft (capex 16 cadenas, capacidad 13, licencias 3, plan 2, equip. 1; p.
  ej. capex N6 «600, 900 o 1.200 €/m2 sobre 90 m2» → «$55.74, $83.61 or $111.48 per sq ft over 969 sq ft», plan
  Inversión A6 «(900 €/m² × 90 m²)», capacidad P14 «0,93 m2» → «10.0 sq ft»); m3/h → CFM (3: C19-C21, J8 «40 … 50» →
  «23.5 … 29.4 CFM per kW»); °C → °F en la carta (cabeceras G5:I5, C28:C29); pagas/SMI (plantilla 22, plan 12, picos 6,
  carta 4); mes del pico 3 en filas de texto («Peso sobre el Año» E8/E10, Cuello de Botella A20:B20 y J20, Cronograma B49, Plan
  de Contratación C18).
- Cosmético: `Ruta Doméstica!B15` (0.743) se ve «0.7» con `#,##0.0`.
