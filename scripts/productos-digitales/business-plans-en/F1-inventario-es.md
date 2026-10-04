# Planes de negocio Food Truck y Cafetería-Brunch v2.2 (ES): inventario de F1 para las ediciones EN

> Sesión Claude Code, 4-oct-2026. Fuente: los **6 ficheros PUBLICADOS** de `astro-site/public/dl/plan-negocio-food-truck/`
> y `astro-site/public/dl/plan-negocio-cafeteria/`, nunca el generador (`planes-v2_0/`) (lección del piloto:
> el duplicado sale de lo publicado). Los recuentos salen de openpyxl y python-docx, leídos en serie. Celdas citadas
> como `libro:Hoja!celda` (FT = food truck, CAF = cafetería). Los defectos heredados (§4) NO se corrigen en el ES
> desde esta carpeta.

## 0. Totales

| Fichero | Hojas | Texto | Fórmulas | Fx→hoja | DV | CF | Merges | Verdes = desbloq. | Fmt € (≈) | Textos con € | Textos de norma ES |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FT `plan-financiero-food-truck.xlsx` | 9 | 690 | **722** | 419 | 24 | 68 | 5 | 135 | 517 | 63 | 156 |
| FT `checklist-apertura-food-truck.xlsx` | 7 | 403 | 12 | 0 | 6 | 12 | 6 | 68 (= **68 tareas**) | 0 | 2 | 50 |
| CAF `plan-financiero-cafeteria-brunch.xlsx` | 9 | 730 | **742** | 423 | 24 | 70 | 5 | 159 | 531 | 53 | 139 |
| CAF `checklist-apertura-cafeteria-brunch.xlsx` | 7 | 438 | 12 | 0 | 6 | 12 | 6 | 75 (= **75 tareas**) | 0 | 2 | 56 |

| Fichero | Palabras | Párrafos | Estilos | Tablas / imágenes / cabecera-pie | Página |
|---|---|---|---|---|---|
| FT `plan-de-negocio-food-truck.docx` | 6.948 | 131 (121 con texto) | `Normal` + 10 `Heading 1` | 0 / 0 / ninguno | **US Letter** ya (7772400 × 10058400 EMU) |
| CAF `plan-de-negocio-cafeteria-brunch.docx` | 6.508 | 167 (157 con texto) | `Normal` + 10 `Heading 1` | 0 / 0 / ninguno | US Letter |

Todos los párrafos del docx son de **un solo run** (0 párrafos con runs mezclados o negrita parcial): el reensamblado EN
puede sustituir el texto del run párrafo a párrafo y conservar estilo, negrita y tamaño sin tocar el XML.

## 1. Estructura

### 1.1 Plan financiero (motor común `planes-v2_0`, v2.2) — las 9 hojas son las MISMAS en los dos planes

| Hoja ES | Rango FT / CAF | Qué hace | Entradas (verde) |
|---|---|---|---|
| `0. Supuestos` | A1:C68 / A1:C68 | Hoja de mando: actividad, mezcla y coste de mercancía, personal, local, financiación, fiscal, amortización, arranque, cobros/pagos/IVA, umbrales | 50 / 50 |
| `Inversión Inicial` | A1:E33 / A1:E42 | Partidas (col. E «¿Lleva IVA?» Sí/No, DV de lista), fianza, meses previos, imprevistos (% sobre partidas de obra), fondo de maniobra, CAPEX, IVA soportado recuperable, necesidad de caja, bases de amortización | 28 / 46 |
| `PyG 3 Años` | A1:H59 / A1:H58 | P&L 3 años sin IVA, col. G = tipo de IVA por línea, Impuesto de Sociedades con bases negativas y tipo de nueva creación, ratios con umbral (col. E) y semáforo | 15 / 14 |
| `Punto Equilibrio` | A1:F36 / A1:F38 | Equilibrio contable y de caja (con principal), holgura, interpretación (fórmula de texto), tabla de sensibilidad 5×4 | 0 / 1 |
| `Escenarios` | A1:F28 | Pesimista / realista (lee Supuestos) / optimista; saldo de caja estimado | 6 / 6 |
| `Personal` | A1:J25 / A1:J27 | Puestos × jornada × bruto, SS empresa, pagas, horas, crecimiento de plantilla, **cobertura de horas** y suelo SMI/convenio | 18 / 24 |
| `Instrucciones` | A1:E73 / A1:E75 | Uso, ratios auditados (CUMPLE/REVISAR), cifras del plan, **tabla «QUÉ HA CAMBIADO RESPECTO DE LA VERSIÓN 1.1»** (A33:D51 en FT), **«DATOS DE REFERENCIA DEL SECTOR»** con columna «Fuente», firma y versión | 0 |
| `Tesorería 12 meses` | A1:O70 | Estacionalidad × rampa, cobros con IVA, pagos, nóminas con pagas extra, IVA repercutido/soportado, arrastre del IVA de la inversión, **liquidación trimestral (modelo 303)**, saldo, saldo mínimo y mes, flujo libre antes de deuda, payback | 12 |
| `Financiación` | A1:H80 | Origen (propios, préstamo, ICO, ENISA, business angels, subvenciones) y usos, préstamo que cuadraría, cuadro francés con carencia (15 años), DSCR por año y mínimo | 6 |

- Protección: las 9 hojas protegidas **sin contraseña**; verdes `E8F5E9` todas desbloqueadas. Paneles en 6 hojas. Papel **A4
  (`paperSize 9`)**; pie `AI Chef Pro · aichef.pro · Página &P de &N`. Sin gráficos, imágenes ni nombres definidos.
- Formatos: `#,##0 €`, `#,##0.00 €`, `0.0%`, `0%`, `#,##0`, `#,##0.0`, `#,##0.00`. Cabeceras «Mes n (€)», «Año (€)».
- DV: 12-13 decimales, 10-11 enteros, 1 lista `"Sí,No"` (Inversión col. E). Mensajes en español con coma decimal
  («0,35 = 35 %»).
- CF: 64-66 `expression` + 4 `containsText` con literales `Sí`, `No`, `CUMPLE`, `REVISAR`.
- **27-28 fórmulas con literales de texto** (41-44 literales distintos): «Sí», «No», «CUMPLE», «REVISAR», «Más de 3 años»,
  «Convenio Hostelería — … pagas + SS …», «Se amortiza en … años», « € de inversión.», « € de los …», «Renta de los N
  meses…», «Con el ticket medio sin IVA… necesitas…», «Ticket sin IVA más el IVA medio ponderado…». Se traducen como
  literales de fórmula (patrón `FORMULAS_EN`/`CLAVES` del financial-kit), no como textos de celda.
- Mecánica fiscal (clave para la adaptación US): `PyG!G10:G11` tipo repercutido (G10 = `Supuestos!B39`; G11 = mezcla de
  alcohol con B62/B63/B16/B40); **`G13` y `G14` (compras de comida y bebida) usan el tipo REPERCUTIDO B39/B40** como
  soportado; G15:G35 = B41 (soportado general 21 %); seguros, comisiones de pago, personal, amortización e intereses = 0
  literal. `Tesorería!B9:M9` cobra con IVA, `B11:M11` paga compras × (1 + G), filas 16-20 liquidan por trimestre.
- Pagas: `Tesorería!B13:M13` = personal / MAX(12, pagas) × (1 + extras en los meses B60/B61). **Con 12 pagas las extras
  salen 0** (verificado en la fórmula): pasar a 12 no exige tocar fórmulas.
- **Las coordenadas NO coinciden entre FT y CAF** (la CAF tiene 9 filas más en Inversión, una fila de fijos distinta en el
  P&L, filas extra en Personal y PE con rotación activa). La capa EN direcciona por censo de cada libro, no por celda fija.

### 1.2 Checklist de apertura (molde común: 6 fases + Instrucciones)

| Pestaña FT | Tareas | Pestaña CAF | Tareas |
|---|---|---|---|
| `F1 - Constitución` | 11 | `F1 - Constitución` | 11 |
| `F2 - Vehículo` | 13 | `F2 - Local` | 13 |
| `F3 - Equipamiento` | 12 | `F3 - Equipamiento` (título «OBRA Y EQUIPAMIENTO») | 15 |
| `F4 - Personal` | 10 | `F4 - Personal` | 12 |
| `F5 - Marketing` | 12 | `F5 - Marketing` | 14 |
| `F6 - 90 Días` | 10 | `F6 - 90 Días` | 10 |
| `Instrucciones` (A1:A11, 9 textos) | — | `Instrucciones` | — |

Columnas `OK | TRÁMITE / ACCIÓN | RESPONSABLE | PLAZO | NOTAS`; col. A verde con DV `"✓,☐,N/A"`; CF `$A5="✓"` (fila) y
`containsText "✓"`; contador `COUNTIF(A:A,"✓")` de `COUNTIF(B:B,"?*") − COUNTIF(A:A,"N/A")`. Sin literales de texto en
fórmulas: la capa EN solo traduce celdas y pestañas (los símbolos ✓ ☐ N/A se quedan).

### 1.3 Documento Word (10 secciones idénticas en los dos planes)

Portada (PLAN DE NEGOCIO / Food Truck / subtítulo / «ChefBusiness Consultoria Gastronomica» / chefbusiness.co /
«Espana, 2026») · AVISO LEGAL · ÍNDICE · 1 Resumen Ejecutivo · 2 Concepto y Propuesta de Valor · 3 Análisis de Mercado ·
4 Análisis Competitivo · 5 Plan de Marketing y Captación · 6 Plan de Operaciones · 7 Estructura Organizativa y RRHH ·
8 Plan Financiero · 9 Aspectos Legales y Licencias · 10 Conclusiones y Plan de Acción · cierre ChefBusiness con
venta cruzada **en EUR hacia `chefbusiness.co/productos-digitales/`** (FT: Kit de Tareas Food Truck 12 EUR, Kit de
Escandallos 12 EUR, eBook 9 EUR; CAF: + Pack APPCC 14 EUR). Separadores «━━━» como párrafos.

## 2. Qué es idéntico entre los dos planes (la capa EN se construye UNA vez)

- **Plan financiero:** mismas 9 pestañas, mismas fórmulas por patrón (motor 2.2), mismos formatos, DV, CF, protección,
  pie, firma y literales de fórmula. De sus textos, **414 cadenas distintas (4.401 palabras) son literalmente iguales**
  en los dos libros (rótulos y notas del motor). Lo propio de cada plan: ~187 cadenas FT (≈4.200 palabras) y ~216 CAF
  (≈3.200 palabras), las de `contenido_plan_negocio_<x>/a.py` (partidas, notas de supuestos, tabla de referencias).
- **Checklist:** mismo molde y mismas Instrucciones; solo 61 cadenas comunes (cabeceras, contador, instrucciones). Las
  tareas son propias de cada plan (salvo ~15 transversales: RGPD, registro horario, DDD, residuos, música, formación).
- **Docx:** misma plantilla de 10 secciones, misma portada, aviso y cierre; el texto de cada sección es propio.
- Consecuencia: `aplicar_en.py` y `gates_en.py` únicos con `PLANES = {food-truck, coffee-shop}`; un glosario y un
  diccionario de textos del motor compartidos; textos propios y valores de ejemplo por plan.

## 3. Lo específico de España que hay que sustituir

| Ámbito | FT | CAF | Dónde |
|---|---|---|---|
| IVA | 10 % repercutido, 21 % soportado, alcohol 10 % en el acto (art. 91 LIVA), exenciones art. 20.Uno.16/18 LIVA, «sin IVA» en rótulos, modelo 303, «IVA soportado recuperable» de la inversión | ídem | Supuestos B39:B41, B62:B63; PyG col. G y notas; Tesorería 16-20, A34; Inversión E y B28 (FT) / B37 (CAF); Instrucciones línea 4 (divisores 1,10/1,21) |
| Impuesto de Sociedades | 15 % nueva creación + 25 % general (art. 29.1 LIS), bases negativas art. 26 LIS | ídem | Supuestos B37:B38, B42; PyG 42-47; Escenarios 19 |
| Personal | SS empresa 33 %, 14 pagas, SMI 2026 17.094 €, convenio provincial, ET art. 34.1/34.9/38, 30 días de vacaciones (46 semanas) | ídem | Supuestos B20:B22, B60:B61, B68; Personal A2, D:E, J, 16-17, 24-25 |
| Amortización | coeficientes art. 12.1 LIS, vidas 8/10 años (FT) y 10/8 (CAF) | ídem | Supuestos B44:B45 y notas |
| Financiación | ICO, ENISA, subvenciones autonómicas, «carencia», TIN, fondos propios 25-30 % | ídem | Financiación 8-11, Supuestos C30:C34 |
| Administración | SL/autónomo, notaría, Registro Mercantil, 036/037, IAE 672.x, FNMT, Veri*factu (RD 1007/2023), RGPD/LOPDGDD/AEPD, hojas de reclamaciones, ROESB, SGAE/AGEDI-AIE, PRL (art. 30.5 LPRL), carnet de manipulador (RD 109/2010) | + OEPM, LAU, informe urbanístico, licencia inocua/declaración responsable, licencia de terraza, videovigilancia | checklists F1-F6; PyG fijos; docx §7 y §9 |
| Sanidad | registro sanitario autonómico (RGSEAA no aplica, RD 191/2011), autorización sanitaria del vehículo, proyecto técnico sanitario, 14 alérgenos UE | registro sanitario, trampa de grasas, APPCC | checklists; Inversión; docx §9 |
| Vehículo | ITV de reforma, carnet B/C (3.500 kg), venta ambulante municipal, ocupación de vía pública | — | checklist F2; docx §6 y §9 |
| Moneda y unidades | €, «€/mes», m² (CAF «18-28 €/m²», proyecto si > 100 m²), coma decimal | ídem | todos |
| Cifras de mercado | ticket 12 € (PVP 13,20), 45 clientes/día, 250 días; mercados (San Miguel, Boqueria), 2.500-3.500 food trucks en España | ticket 9,80 € (PVP 10,78), 100 clientes/día, 300 días; Federal, Panem, Pret Madrid | Supuestos; docx §1-4 |
| Fuentes | «Fichero v1.1» en TODA la tabla de referencias; «BOE» para el SMI | ídem | Instrucciones A53:D68 (FT) / A52:D70 (CAF) |
| Marca e IDs | docx de ChefBusiness (decisión de John del 22-ago para el ES); xlsx `Instrucciones!A3` del checklist cita el id interno «plan-negocio-food-truck»; enlaces a `aichef.pro/productos-digitales` y `aichef.pro/plan-negocio-*` | ídem | Instrucciones, docx portada y cierre |

## 4. Defectos heredados del ES (la EN nace corregida; el ES se propone para su próxima v2.x)

- **I1 · El docx es el de la v1.1 y contradice al Excel.** FT: inversión «73.000 €» (Excel 81.997 €), equilibrio «27
  clientes» (Excel 41), food cost 30 % (Excel 27,1 %), SS 33,4 %, equipo «2-3 personas» (Excel 1,61 jornadas); §9 dice
  que el **RGSEAA es obligatorio para todos los food trucks** y el checklist y la landing dicen lo contrario. CAF:
  inversión «94.000 €» (Excel 130.176 €), equilibrio «53 clientes a 9,50 €» (Excel 84 a 9,80 €), facturación 190.000 €
  (Excel 294.000 €). El propio Excel lo admite (`Instrucciones!A12`: «el documento Word… es el de la versión 1.1»).
- **I2 · Restos de inglés y erratas en el docx ES:** «fill the gap», «ranging from 45,000 to 85,000 euros»,
  «flujosconstants», «affluencia», «determinantepara» (FT); «brutoss», «recuperase», «se fixa», «spectacles» (CAF).
  Portada, índice y encabezados **sin tildes** («Analisis», «Captacion», «Espana»).
- **I3 · La tabla «DATOS DE REFERENCIA DEL SECTOR» cita como fuente «Fichero v1.1»** (el propio producto) en todas las
  filas, y la landing FT vende el bono 2 como «cada dato con su fuente».
- **I4 · `Financiación!B51` (DSCR del año 1) sale inflado con carencia** (FT 3,81×, CAF 6,27×): la nota C51 lo avisa y
  B54 mide el mínimo del cuadro, pero la cifra visible engaña. EN: carencia 0 por defecto (D17 del SPEC).
- I5 · Checklist `Instrucciones!A3` expone el id interno del producto. EN: nombre comercial.
- I6 · Cafetería: la landing omite el DOCX (entregable de 6.508 palabras) y vende como bono el cuadro de Personal, que ya
  es una tarjeta del grid (doble cómputo). Ver SPEC §6.
