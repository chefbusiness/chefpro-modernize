# Plan de Negocio Parrillero-Asador para Eventos (ES) 2.2: revisión adversarial final (1 ronda) · sesión Claude Code 2026-10-12

Rama `feat/parrillero-2-2` @ `b002a225` (PR #125). Los 11 ficheros tienen el mismo sha256 en el Mac y en el VPS. Revisor: 1 Opus, solo lectura. Los xlsx y docx se abrieron solo en el VPS; el scratch `/root/tmp-par-rev` ya está borrado y el worktree no se ha tocado.

**Veredicto: todavía NO está listo. Hay 0 BLOQUEANTE, 4 MAYOR y 12 MENOR.**

Las fórmulas y las cifras del Excel están bien y cuadran al euro con `cifras_caso_es.json`, con el Word y con la landing. La calculadora da lo mismo con pycel que a mano. Casi todo se arregla por texto. Hay dos excepciones:
- **M3** obliga a cambiar los datos de un ejemplo en `calculadora_par_es.py` y rehacer su autotest.
- **M2** obliga a cambiar celdas de dos tablas en `arreglos_d9.py`.

## Cifras recalculadas a mano

Cuadran al euro en el Excel, el json, el docx §1/§8/§10 y la landing. El correo no da cifras.

**Ventas**
- La mezcla da 12×110×42 + 30×70×31 + 45×40×25 + 8×300×10 = **189.540 €** con 7.620 invitados: 80,2 invitados a 24,87 €.
- El Excel calcula 95 × 80 × 25 = **190.000 €** (+0,24 %).
- Empresas y fiestas suman el 47,0 % de las ventas, como dice `Supuestos!C58`.
- Años 2 y 3: 205.200 € y 215.460 €, con 86,4 y 90,7 invitados por evento.
- PVP con IVA: 27,51 €.

**Margen**
- Mercancía: 53.504 (32 % de 167.200) + 6.840 = 60.344 € → **31,8 %**.
- Costes variables: 60.344 + 8.550 + 950 + 950 + 9.500 = **80.294 €**.
- Margen bruto: **109.706 € (57,7 %)**.

**Personal**
- Titular: 1.800 × 1,33 × 14 = 33.516 €.
- Segundo parrillero: 450 × 1,33 × 14 = 8.379 €.
- Cada auxiliar: 432 × 1,33 × 14 = 8.043,84 €.
- Total: **57.982,68 €**, el 30,5 % de las ventas. Las incorporaciones suben el coste a 63.983 € y 69.983 €.

**Fijos y resultado**
- Fijos: 12.000 + 57.982,68 + 13.470 (los propios, con extintores a 170 €) + 4.912 + 4.251 = **92.615,68 €**.
- Año 1: RAI **17.090 €**, neto **14.527 €** (IS 15 %).
- Año 2: RAI 19.867 €, neto 16.887 €.
- Año 3: los intereses bajan a 3.504 €; RAI 20.538 € y neto **15.403 €** con IS al 25 % (7,1 %).

**Inversión y necesidad de caja**
- Las 17 partidas suman **54.596 €**. Los imprevistos son el 8 % de 21.200 € = 1.696 €.
- Fondo de maniobra: 3 × (92.615,68 − 4.912) / 12 = **21.925,92 €**.
- Inversión total: **76.522 €**.
- IVA: 21 % × (54.596 − 3.000) = **10.835 €**.
- Necesidad de caja: **87.357 €**. Con 22.000 + 65.400 sobra **+43 €**.
- Amortización: 22.896 / 8 + 20.500 / 10 = **4.912 €**.

**Préstamo**
- Cuota: 65.400 × 0,065 / (1 − 1,065⁻⁵) = **15.737,50 €**. El año 1 es de carencia: 4.251 € de intereses.
- DSCR del año 2: (16.887 + 4.912 + 4.251) / 15.737 = **1,66**.
- DSCR del año 3: (15.403 + 4.912 + 3.504) / 15.737 = **1,51**, el mínimo del cuadro.

**Equilibrio**
- Coste variable por invitado: 10,565 €. Margen de contribución: 14,435 €.
- Contable: 92.616 / 14,435 = 6.416 invitados = **67,5 → 68 por evento**; 160.401 € = **81 eventos** de 2.000 €.
- Caja año 1: 87.704 € → **64 invitados / 76 eventos**, holgura **25,1 %**.
- Caja año 2: 105.190 € → 182.179 € = **92 eventos** sin crecer, holgura **12,6 %**.
- Caja año 3: 111.190 € → 192.570 € = **97 eventos (más que los 95 del plan)**, holgura **11,9 %**.

**Resto**
- Saldo mínimo: **6.145 € (mes 4)**.
- Payback: 23.690 + 26.050 + 23.820 = 73.559 € < 76.522 € → **«Más de 3 años»**; sobre el CAPEX, **2,2 años**.
- Escenarios: 80 × 75 × 23 = 138.000 € → **−12.934 €**; 110 × 85 × 26 = 243.100 € → **+40.588 €**.

## Calculadora evaluada

Pycel: 144 celdas evaluadas, 0 diferencias con la caché. Las tres cuentas cuadran también a mano.

**Hoja sin tocar** (particular, 100 invitados, asado completo, cortes en mesa)
- Necesita 50 kg crudos, 2 parrillas, 3 parrilleros, 2 ayudantes y 40 kg de carbón.
- Coste: 2.648,05 € → **46,00 € sin IVA / 50,60 € con IVA**; total **5.133,15 €**.
- Cancelación: 1.539,95 / 2.566,58 / 3.849,86 / 5.133,15 €.
- Con Empresa sale 44,50 €, cobro 30/70 y tramos 20/50/75/100 %. Con Ayuntamiento, 0 % de anticipo, 100 % a 30 días y sin tramos.

**(A) Boda particular, 110 invitados**
- Coste de 2.550,66 €: 40,00 € + 2 € de show = **42,00 €** (46,20 € con IVA).
- Total **5.155,15 €**; cobros 1.546,55 / 2.062,06 / 1.546,55 €; margen 44,8 %.

**(B) Empresa, 70 invitados, BBQ texano**
- Coste de 1.260,56 € → **30,50 €**; total **2.400,75 €**.
- Cobro 720,23 € + 1.680,53 €; margen 41,0 %.
- Tramos: 480,15 / 1.200,38 / 1.800,56 / 2.400,75 €.

**(C) Fiesta de ayuntamiento, 300 invitados**
- Con 3 parrillas, 2 parrilleros y 3 ayudantes: **10,00 €**, total **3.362,70 €**.
- Todo a 30 días; margen 41,5 %.

**Desplegables y tablas**
- Desplegables correctos: cliente con 3 valores, formato `A72:A75`, experiencia `A78:A88` (11) y estilo `A67:A69`.
- La tabla de escalado (40 / 80 / 150 / 300 invitados) es idéntica a la tabla 4 del manual, sección 8.
- Los tramos de cancelación coinciden con el contrato B2C/B2B, el docx p82 y las Instrucciones de la calculadora (A17-A18).
- Los precios casan con el Excel (42 / 31 / 10 €; la empresa sale a 30,50 €).
- **Excepción:** el suplemento de show del ejemplo A (M3).

## Integridad

**Ficheros**
- Los 11 ZIP están sanos: `testzip` limpio y abren en openpyxl y python-docx.
- Los 4 xlsx tienen todas las hojas en A4 (paperSize 9): 9, 7, 3 y 11 hojas.
- Los 7 docx están en A4 (21 × 29,7) con autor AI Chef Pro, fechas de 2026, título «· v2.2» y comentario con la URL.

**Contenido**
- Docx del plan: 11 H1, 142 párrafos, 8.120 palabras y 0 tokens.
- Checklist: 12/16/14/10/16/15 = **83** tareas, con las columnas Responsable, Plazo y Notas.
- Proveedores: **93**; 46 «Por verificar» y 47 «Investigar»; 0 «Validado»; score vacío en los 93. El desplegable de estado es correcto.
- Manual: 8 salmueras, 12 marinados, 18 cortes, tabla 8 de escalado y tabla de temperaturas.
- La nota del motor del Word quedó corregida en `Tesorería!D31` («El plan de negocio en Word cita esta cifra»).

## Fuentes abiertas

Se consultaron el BOE consolidado (API de datos abiertos) y el DOUE en el espejo del BOE, porque EUR-Lex no responde desde el VPS ni desde WebFetch.

1. **Reglamento (CE) 853/2004**, anexo III (DO L 226 de 25-6-2004):
   - carne a ≤ 7 °C y despojos a ≤ 3 °C (sección I, cap. VII);
   - aves a ≤ 4 °C (sección II);
   - picada a ≤ 2 °C y preparados a ≤ 4 °C (sección V).

   **Conforme**, citado «como estándar».
2. **RD 1086/2020, art. 26.2**: solo los «puntos de venta al consumidor expresamente autorizados» extraen la columna vertebral del bovino. **Conforme** con «nunca lo deshuesas tú». La regla del «riesgo insignificante o < 30 meses» sale del Reglamento 999/2001, anexo V. Está citada al final de la frase, así que se acepta.
3. **RD 1086/2020, art. 30** (redacción de la DF 2.12 del RD 1021/2022):
   - 30.2 (≥ 63 °C): **conforme**.
   - 30.7 (recalentar a 74 °C durante 15 s): **conforme** (manual p75).
   - 30.10 (100 g, ≤ 4 °C o congelada, 7 días): **conforme**.
   - **30.8**: la comida testigo es obligatoria con «d) Para eventos, cuando esta sea la actividad principal de la empresa» **o** con «e) … más de 40 personas». **M1**.
4. **RIRPF, art. 95.6**: la retención del 1 % es solo para módulos de los epígrafes listados, y no hay ninguno del grupo 6 (tampoco el 677.9). Como la retención del art. 95 es para actividades profesionales, «sin retención» es **conforme**.
5. **LIVA, art. 75.Dos**: devengo por los cobros anticipados. **Conforme** con «factura de cada pago, también de la señal».
6. **TRLGDCU**:
   - art. 90.2 (fuero del domicilio del consumidor): **conforme**;
   - art. 103.l («comida … si los contratos prevén una fecha»): **conforme**.
7. **Ley 7/2012, art. 7** (vigente desde el 11-7-2021): prohíbe pagar en efectivo «igual o superior a 1.000 euros». «Por debajo de 1.000 €» es **conforme** en docx p82/p103, calculadora `Instrucciones!A14` y checklist `F6!E7`.
8. **LCSP**:
   - art. 118.1 (contrato menor de servicios por debajo de 15.000 €): **conforme**;
   - art. 198.4 (pago a 30 días desde la conformidad): **conforme**;
   - art. 198.3 (abonos a cuenta solo por operaciones preparatorias y con garantía): **conforme** con «sin anticipo».

## BLOQUEANTE

Ninguno.

## MAYOR

- **M1 · La comida testigo parece solo para eventos de más de 40 personas, y aquí es obligatoria en todos.**
  - **Dónde.** Docx p81: «Si el evento supera las 40 personas, guardas una comida testigo…».
  - **Por qué está mal.** El art. 30.8.d la exige a quien tiene **los eventos como actividad principal**, que es este negocio. El 30.8.e solo añade el caso de más de 40 personas. Con el texto actual, las **45 celebraciones privadas de 40 invitados** del caso (40 no es «más de 40») quedarían fuera.
  - **El checklist suena ambiguo.** `F2!E9` dice «obligatoria en eventos de más de 40 personas **y** si los eventos son tu actividad principal», y se lee como condición doble.
  - **Arreglo en el docx** (`textos/par_es_b.json`, ranura de §6): → «Como los eventos son tu actividad principal, guardas una comida testigo de cada preparación en todos los eventos, no solo en los de más de 40 personas (RD 1086/2020, art. 30.8): 100 g, identificada y fechada, a 4 °C o menos o congelada, durante 7 días».
  - **Arreglo en el checklist** (`datos_checklist.py`, `F2!E9`): → «… durante 7 días: obligatoria en todos tus eventos, porque son tu actividad principal (art. 30.8.d del RD 1086/2020), y en cualquier encargo de más de 40 personas (30.8.e); conservación según el 30.10».

- **M2 · La tabla de cocción del manual y la carta contradicen la regla de 70 °C del propio kit.**
  - **La regla que fija la 2.2.** El manual (tabla 5 y p76), el docx p80 y el checklist (`F2!E8`, `F6!E15`) dicen: 70 °C en el centro, 74 °C las aves, y «poco hecho» solo en piezas enteras de vacuno o cordero y a petición.
  - **Lo que no se tocó.** La tabla de 18 cortes del manual (t2, heredada de la 1.1) da como objetivo por defecto **cerdo por debajo de 70 °C**:
    - lomo de cerdo a 63 °C (t2r13);
    - pluma ibérica a 62 °C (t2r14);
    - secreto a 60 °C (t2r15).
  - **El cerdo queda fuera de la excepción del vacuno y el cordero.** El vacuno aparece a 52-60 °C sin el «a petición».
  - **La carta hace lo mismo.**
    - Vacío: «60 °C, **jamás bien hecho**» (t2r2), que niega el punto que pida el invitado.
    - Bife: 52-55 °C (t1r2).
    - Picaña: 55-60 °C (t9r2).
    - Tomahawk: 55 °C (t10r2).
  - **Consecuencia.** El APPCC del comprador registraría como no conforme lo que su propio manual le manda hacer.
  - **Arreglo** (`arreglos_d9.py`):
    - Manual p10, añadir: «Los objetivos por debajo de 70 °C son el punto "poco hecho": solo en piezas enteras e intactas de vacuno o cordero y a petición del invitado. Cerdo, aves, picada y embutido, a 70 °C en el centro (74 °C las aves; recomendación de AESAN)».
    - t2r13-t2r15 → «70 °C (APPCC del kit)».
    - Carta p4, la misma frase.
    - Carta t2r2 → «60 °C a petición; 70 °C por defecto».

- **M3 · La boda de ejemplo pone 2 € de show de fuego, y el kit dice 8-15 €.**
  - **Dónde.** `Ejemplos!B4`: «Boda particular **con show de fuego**». `B18` = **2 €**, y `B60` habla de «un suplemento de 2 € por invitado por el show de fuego».
  - **Por qué está mal.** La misma calculadora (`Calculadora!C18`) dice «**De 8 a 15 €** por invitado» si hay show, y la experiencia 09 dice «suplemento de 8-15 €/inv.» (p164). Se puso 2 € para que la boda salga a los 42 € del Excel.
  - **Arreglo** (`calculadora_par_es.py` + autotest): quitar el show y subir la bebida.
    - Datos: `B18` = 0 y `B10` = 5 €. El coste pasa a 2.660,66 €: 41,70 € → **42,00 €**. El subtotal y el total no cambian (4.620 / 5.155,15 €); el margen queda en 42,4 %.
    - Rótulos: `B4`/`B21` → «Boda particular con cortes en mesa».
    - `B60` → «… bebida con vino incluida (5 €). Sin show: con él, súmale de 8 a 15 € por invitado».
    - La landing, el changelog y el correo no citan el show, así que no cambian.

- **M4 · La landing describe un escalado que el manual no trae.**
  - **Dónde.** Ficha `plan-negocio-parrillero-asador-eventos.ts:151` (grid) y `:204` (bonus 1): «escalado … para **50, 100 o 200 invitados**».
  - **Por qué está mal.** La tabla del manual (sección 8) y la de la calculadora son de **40, 80, 150 y 300**.
  - **Arreglo** (`.ts`) → «escalado de carne cruda, parrillas, parrilleros y carbón de 40 a 300 invitados» en las dos líneas. El dashboard y el changelog ya lo dicen bien.

## MENOR

- **m1 · El docx p78 cobra la señal después de la visita técnica del D-21.**
  - **Por qué está mal.** Contradice:
    - el docx p69 («firma meses antes de la fecha») y p73;
    - el checklist `F6!E7` («Sin señal no se bloquea la fecha»);
    - el tramo de cancelación de 60 días o más del contrato.
  - **Es el m2 del paellero, repetido.**
  - **Arreglo** (`par_es_b`) → «Con el presupuesto firmado y la señal del 30 % la fecha queda reservada, a veces meses antes; a D-30 cierras el briefing… A D-21 haces la visita técnica…».

- **m2 · El docx p97 no dice que 97 eventos es más que los 95 del plan.**
  - Hoy: «… y en el tercero al 11,9 % (unos 97)». La pista §8 manda contarlo.
  - **Arreglo** (`par_es_b`) → «(unos 97, más que los 95 del plan: sin el crecimiento de invitados por evento, el tercer año no cubre la cuota)».

- **m3 · FACe aparece sin el matiz de la exención.**
  - **Docx p55** dice «exigen factura electrónica por FACe, salvo en importes de hasta 5.000 €», y p107 lo dice bien. La exención es una opción del ayuntamiento (Ley 25/2013, art. 4).
  - **Arreglo docx** (`par_es_a`) → «… salvo que el ayuntamiento exima las de hasta 5.000 €».
  - **Excel `Instrucciones!D53`** no recoge la exención.
  - **Arreglo Excel** (`a.py`) → añadir «, salvo que exima las de hasta 5.000 €».

- **m4 · `Instrucciones!C54` del Excel atribuye los 70 °C de cocción a normas que no los fijan.**
  - Cita «Reglamento (CE) 853/2004 y RD 1086/2020, art. 30» para los 70 °C en el centro, y ninguno de los dos los fija.
  - **Arreglo** (`a.py`) → «Reglamento (CE) 853/2004 (recepción), AESAN (cocción, recomendación) y RD 1086/2020, art. 30 (mantenimiento)».

- **m5 · El token del payback entra con mayúscula a mitad de frase.**
  - Docx p98: «el payback del proyecto, Más de 3 años». Docx p111: «payback de Más de 3 años».
  - **Arreglo** (`par_es_b`) → «el payback del proyecto supera los 3 años (2,2 sobre las compras)», o pasar el token a minúscula en `docx_par_es.py`.

- **m6 · Las fechas de versión no coinciden dentro del pack.**
  - Dicen «Versión 2.2 · **septiembre** 2026»:
    - docx p16;
    - plan financiero `Instrucciones!A60`;
    - checklist `Instrucciones!A11`;
    - calculadora `Instrucciones!A29`. Esta no la sella el motor: es `calculadora_par_es.py`.
  - Dicen «**octubre** 2026» los proveedores (`Indice`) y la landing.
  - **Arreglo** → «octubre 2026» en los cuatro: `VOCABULARIO` o el post del motor, `docx_par_es.py`/`fuente_par_11.json` y `calculadora_par_es.py`. Es la desviación 11 de F2-NOTAS, pero ahora hay incoherencia dentro del propio pack.

- **m7 · Las celebraciones privadas del Excel quedan por debajo de los tickets de las experiencias.**
  - Las privadas van a 25 € sin IVA.
  - Los tickets «Particular» de 9 de las 10 experiencias empiezan en 28-33 €; solo el llanero (24-40 €) cubre los 25 €.
  - La SPEC D5 pide precios coherentes en los cuatro sitios.
  - **Arreglo** (`arreglos_d9.py`, experiencias p4), añadir: «Las celebraciones privadas sencillas del plan financiero (25 € sin IVA) son una parrillada sin experiencia temática: quedan por debajo de estos rangos».

- **m8 · El orden de partidas del docx p94 deja fuera la tercera más cara.**
  - Dice: «la furgoneta (20.000 €) como la mayor, seguida del remolque (7.000 €), las parrillas (3.200 €) y el plan B de gas (2.200 €)». La marca, la web y el lanzamiento (4.500 €) van antes que las parrillas.
  - **Arreglo** (`par_es_b`) → «… seguida del remolque-parrilla (7.000 €), la marca, la web y el lanzamiento (4.500 €), las parrillas (3.200 €) y el plan B de gas (2.200 €)».

- **m9 · El contrato B2C no encaja con las bodas del caso.**
  - p2 y p7 lo limitan a «bodas **íntimas**», pero las 12 bodas del caso (110 invitados) son de particulares.
  - p27 pone «un (1) parrillero», y la calculadora pide 3 parrilleros para 110 invitados con cortes en mesa.
  - **Arreglo** (`arreglos_d9.py`):
    - p7 → «… BODAS Y CELEBRACIONES EN FINCA O CHALET»;
    - p27 → «Servicio de [N] parrillero(s) y [N] ayudante(s), según la tabla de escalado del manual».
  - La landing también dice «bodas íntimas» (`:72`, `:149`, `:176`, `:236`). Alinearla es opcional.

- **m10 · Los permisos del fuego cambian de responsable según el fichero.**
  - El contrato B2C (p34) y el B2B (p103) se los dejan al CLIENTE.
  - El anexo del docx (p121: «pídela con 30-45 días… aporta el APPCC, el seguro…») y el checklist (`F2!B20`) se los asignan al parrillero.
  - **Arreglo** (`arreglos_d9.py`, B2C p34) → «Permiso del propietario del lugar (CLIENTE). La autorización municipal o autonómica de uso del fuego la tramita el PARRILLERO con los datos del CLIENTE, salvo pacto en contrario».

- **m11 · La guía t11 contradice el anexo autonómico.**
  - t11r1, Madrid: «Eventos privados sin problema». El anexo p121 dice que en la franja forestal rigen las mismas restricciones.
  - t11r8, Castilla y León: «Más permisivo que mediterránea, fincas tradición castellana». El anexo p128 dice: prohibido cocinar con fuego en zona forestal, incluso en barbacoas.
  - **Arreglo** (`arreglos_d9.py`):
    - Madrid → «Eventos privados: autorización municipal; en la franja forestal, las mismas restricciones (plan INFOMA)».
    - Castilla y León → «Época de peligro alto de junio a octubre (INFOCAL): sin fuego para cocinar en zona forestal ni en su franja».

- **m12 · Las cuentas del segundo año del food truck (guía t12) no casan con sus unidades.**
  - Eventos: 50 × 3.800 € = 190.000 €, y la tabla pone **195.000 €**.
  - Mercados: 80 × 700 € = 56.000 €, y la tabla pone **65.000 €**.
  - **Arreglo** (`arreglos_d9.py`): o se cambian las notas a «3.800 € el año 1 y 3.900 € el año 2» y «700-810 €/día», o se recalculan las cifras del año 2.

## Conforme, sin cambios

**Restos y vocabulario**
- Sin restos del FT, del paellero ni del catering en los 4 rehechos.
- Las coincidencias que quedan son legítimas: «roadmap food truck», «vinagrete + arroz» del rodizio y el «catering corporativo» como competidor.
- 0 de: «freelance», «validado», «tarifa plana», «sin licencia», PATRICOVA, INFOCYL, retención del 7/15 % y el sello «España 2026». «Carné» solo aparece en «ya no existe».

**Excel**
- La nota del motor sobre el Word está corregida (`D31`).
- Crecimiento contado como invitados por evento en p42, p95 y p116.
- Fijos discontinuos coherentes: 1 segundo parrillero y 2 auxiliares, más un tercero de la bolsa (`C51`, `J19`, p43, p85).
- Explicación de la cobertura del 157 % correcta (p87).

**Cobro, contratos y nombres**
- Plazos de cobro idénticos en el contrato, la calculadora, el Excel (`C58`) y el docx p82.
- Ayuntamientos sin anticipo.
- Fuerza mayor con plan B en el contrato B2C (SEXTA) y en el B2B (QUINTA BIS).
- No desistimiento (103.l) y fuero del consumidor en el contrato.
- Factura de la señal.
- IGP Lechazo de Castilla y León y Marca de Garantía Cochinillo de Segovia, en la carta y en las experiencias.
- Alioli con ovoproducto pasteurizado.

**Web y correos**
- Hubs ×7: «Word + Excel», 83 tareas, 93 proveedores y 9 hojas; sin «60+», «96» ni «validado», y coherentes entre idiomas.
- Email post-compra (`verify-purchase.ts` = config) y dashboard (sin «España 2026»).
- Changelog 2.2 honesto y verificable.
- Correo con «Hola, colegas» y sin cifras movibles.

**Landing**
- Afirmaciones comprobadas en los ficheros:
  - KGE1200 a 709,99 €, COMPER-M, Arcos y Texfire;
  - Hidalgo, Casa López, Tres Jotas, Ricosan, Brogas, Hiscox y Mapfre;
  - Responsable, Plazo y Nota en el checklist;
  - 30-75 K y 8 CCAA en la guía;
  - picaña y tomahawk en la carta.
- Sin DSCR, payback ni saldos.

**Testimonios**
- Solo se cambiaron Federico Aguirre y Marcos Pérez, en la ficha y en la SPA.
- Sandra Vera («freelance» como rol) sigue intacta, por decisión de John.

## Arreglos aplicados (12-oct)

Sesión Claude Code. 16/16 hallazgos aplicados, ninguna cifra del caso movida (`cifras_caso_es.json` idéntico, sin diff).

- **M1** hecho: docx p81 (`par_es_b`) y checklist `F2!E9` (`datos_checklist.py`) dicen «en todos los eventos, porque son tu actividad principal (30.8.d), y en cualquier encargo de más de 40 personas (30.8.e)». No quedaba otra mención de «40 personas» en el parrillero. Paellero: `paellero-2_2/datos_checklist.py` (F2!E8) con la misma formulación («cada arroz»); el Catering no se toca.
- **M2** hecho (`arreglos_d9.py`): frase de los 70 °C en el manual (intro de la tabla 3) y en la carta; t2r13-r15 del manual → «70 °C (APPCC del kit)»; carta t2r2 → «60 °C a petición; 70 °C por defecto.».
- **M3** hecho (`calculadora_par_es.py`): ejemplo A sin show (`show=0`, `beb=5`), rótulo «Boda particular con cortes en mesa», nota con «Sin show: con él, súmale de 8 a 15 € por invitado». Sale 42,00 €/inv, total 5.155,15 €, margen 42,4 %. Autotest 552/552.
- **M4** hecho (`.ts`): las dos líneas dicen «de 40 a 300 invitados».
- **m1** (señal al firmar, antes del D-30), **m2** (97 eventos, más que los 95 del plan), **m5** (payback entre «…» en p98 y p111), **m8** (marca/web/lanzamiento 4.500 € en el orden de partidas, p94): `par_es_b.json`. **m3**: docx p55 (`par_es_a.json`) y `Instrucciones!D53` (`a.py`). **m4**: `a.py` (853/2004 recepción, AESAN cocción, RD 1086/2020 art. 30 mantenimiento).
- **m6** hecho sin tocar el motor: `par_version.py` parchea `VERSION_MES`/`VERSION_FMT` en el proceso (lo importan `docx_par_es.py`, `calculadora_par_es.py` y el nuevo `main_par.py`, que ahora lanza `ciclo.sh`). Los 4 sellos dicen «octubre 2026» (0 «septiembre»). El Paellero conserva su sello (no se pidió).
- **m7** (experiencias, frase de las privadas a 25 €), **m9** (contrato: «BODAS Y CELEBRACIONES EN FINCA O CHALET», «bodas», parrilleros según la tabla de escalado; la landing sin «bodas íntimas»), **m10** (permiso del fuego: propietario = CLIENTE, autorización de uso del fuego = PARRILLERO), **m11** (Madrid y Castilla y León de la guía t11), **m12** (guía t12: notas «3.800 € el año 1 y 3.900 € el año 2», «700 € el año 1 y unos 810 € el año 2»; cifras de la tabla intactas): `arreglos_d9.py`, ahora 126 arreglos.

**Gates (VPS):** motor TODO VERDE (parrillero y paellero) · `cifras_caso_es.json` idéntico en los dos · docx VERDE (142 párrafos, 11 H1, 8.175 palabras) · calculadora autotest 552/552 · `arreglos_d9` 126 arreglos, HUELLA 9fdef5fd358c02ea, idempotente (2.ª pasada a scratch, misma huella) · restos FT VERDE con `--permitir` ampliado (`foodtruck|food trucks?|vinagrete \+ arroz`; son las coincidencias legítimas de §6: URL del proveedor y bloque 8 de proveedores) · barrido: solo las legítimas de §6 («cubiertos», «Generador», «food truck» de la guía/catálogo/proveedores) · censo `--fail` 0 defectos (ambos productos) · no latinos 0 (ambos). Mac = VPS por sha256 en los 11 del parrillero y los 2 del paellero. VPS limpio.
