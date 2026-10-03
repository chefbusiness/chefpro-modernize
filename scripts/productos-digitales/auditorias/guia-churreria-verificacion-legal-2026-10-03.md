# Verificación legal y de sector — «Cómo Montar una Churrería-Chocolatería» (F1, 3-oct-2026)

**Sesión Claude Code (Mac) · producto nº 51 · hermana: `guia-chocolateria-obrador`.** Ficheros de esta entrega, todos en este directorio:

| Fichero | Contenido | Fichas |
|---|---|---|
| `guia-churreria-verificacion-legal-2026-10-03.json` | normativa y convenios, `CUN-01…CUN-42` + `CUN-V01, V03, V05, V06` | **46** |
| `guia-churreria-ids-CUS.json` | sector: `CUS-01…59` (con sub-ids), `CUS-M01…M31`, `CUS-V01…V20c`, `CUS-D1…D9` | **156** |
| `guia-churreria-verificacion-legal-2026-10-03-EXCLUIDOS.json` | descartadas, sin URL y con el motivo en `nota` | **27** (13 de normativa + 14 de sector) |

**Método.** Textos oficiales descargados con `curl` el 2026-10-03 (BOE consolidado `act.php`, DOUE vía `boe.es/doue`, BOCM, BOP) y extraídos con PyMuPDF, uno cada vez; el INE `DIRCE2025.xlsx`, con openpyxl en solo lectura. Web de sector (lexpress, El Español, Churrofácil, Hosteleria10, Loomis, etc.) descargada y leída del HTML, no de resúmenes. `istats` entre 41 y 55 °C todo el rato; sin builds, navegador ni Playwright; ningún commit; ningún otro fichero tocado. **No se ha fusionado nada en `guias-v2-research-sector.json`** (no se pedía): hace falta un `guia-churreria-json-merge.py` calcado del de la hermana, con baseline 635 + 202.

## 1. Gates (todos en verde)

- JSON válido en los tres ficheros; **12 claves exactas** en las 202 fichas y en las 27 excluidas; `cifra` numérica o `null`.
- **Ids únicos** dentro de cada fichero y entre los tres, y **0 colisiones** con los 635 ids de `guias-v2-research-sector.json` (no hay ningún `CUN-*` ni `CUS-*` previo).
- Regla de la casa: toda ficha sin URL es `baja` (tres fichas de síntesis o cálculo propio —`CUS-04`, `CUS-58`, `CUS-59`— y `CUS-31f`, sin enlace de anuncio, se bajaron de «media» a «baja» y lo dicen en la nota).
- **Gate de literalidad** (cada `cita_literal` se busca en el texto descargado; se normalizan espacios, comillas, guiones de corte de línea de los PDF y mayúsculas; cada fragmento separado por `[…]` debe aparecer; probado con una cita falsa, que falla):

| Fichero | Con cita | **Pasan** | **No pasan** | Sin cita (motivo) |
|---|---|---|---|---|
| CUN | 44 | **44** | **0** | 2: `CUN-16` y `CUN-33` (hallazgos negativos, sin URL) |
| CUS | 106 | **106** | **0** | 50: anuncios de Milanuncios (captcha hoy), foros solo con título, Jooble 403, fichas sin URL, cálculos propios |

Las normas que la refutación daba por «confirmadas letra a letra» (`CUN-01…03`, `09…14`, `19`, `27`, `32`, Ley 12/2012) se volvieron a descargar de todas formas, porque costaba un `curl`: pasan. Una cita pasa contra el texto descargado hoy, no contra su vigencia futura. **No puedo reabrir Milanuncios** (`Pardon Our Interruption`): `CUS-02`, `CUS-31a…i` y `CUS-M06` quedan con datos de la lente L4 y lo dicen.

## 2. Resultado de V-01 … V-06

| V | Resultado | Ficha |
|---|---|---|
| **V-01** | El convenio de hostelería de Madrid (28002085011981, BOCM 06-04-2024) **venció el 31-12-2025** y su art. 5 lo prorroga salvo denuncia. La comisión negociadora del nuevo se **constituyó el 3-12-2025** (nota de CCOO Madrid) y las reuniones empezaban en enero de 2026. **No se localizó ningún texto nuevo en el BOCM** a 3-oct-2026: siguen aplicándose las tablas de 2025 (prórroga o vigencia durante la negociación, ET art. 86.2-3). Ni REGCON ni el buscador del BOCM se pudieron consultar de forma automática y la denuncia formal no está comprobada con texto. | `CUN-V01` (media) |
| **V-02** | **Sin fuente primaria de temperatura de fritura del churro.** La única cifra normativa (Rgto. 2017/2158, anexo II A: «inferiores a 175 °C»; 160-175 °C al usuario final) es de **patatas**, y el churro no está en el art. 1.2. **El producto no da cifra.** | EXCLUIDOS `CUN-V02` |
| **V-03** | Las notas explicativas del INE (descargadas, 873.000 caracteres) clasifican por actividad (56.11, 56.12, 56.30, 47.24, 10.71) y **no contienen «churro», «chocolater» ni «masas fritas»**; no hay tabla oficial 644.6/676/663.1 → CNAE-2025. La correspondencia sigue siendo inferencia con doble código. | `CUN-V03` (alta), `CUN-16` corregida |
| **V-04** | **Sin consulta de la DGT localizada.** El buscador `petete` da `504` a las consultas y Iberley `403`: la ausencia es de este intento. Lo primario es la exclusión de «bebidas refrescantes… con azúcares o edulcorantes añadidos» (AEAT). D11 se mantiene. | EXCLUIDOS `CUN-V04`; `CUN-18` corregida |
| **V-05** | Ámbito funcional literal del convenio de Toledo: «los **obradores** de Confitería, Pastelería, fábricas de Mazapán y/o Turrones **Masas Fritas** y Fábricas de Chocolates». No aparece «churrería», «despacho» ni «venta». Alcanza a un **obrador** de churros; que alcance al despacho con sala es interpretación (nivel C, a un laboralista). Texto 2025-2026 leído en una base jurídica privada (el BOP, no abierto) y el de 2021 en el PDF del BOP. | `CUN-V05` (media) |
| **V-06** | **Interpretación, nivel B/C.** Literal: las denominaciones del apartado 1 «sólo se aplicarán a los productos que en él figuran», con una excepción complementaria para otros productos «que no puedan confundirse», y el 6.b admite 1.11/1.12 con grasas vegetales si se declara. El RD define el **producto** (polvo o tableta). **De ningún artículo sale** que con un preparado que no cumple no se pueda escribir «chocolate a la taza» ni «chocolate» en la carta. Fórmula para el bonus: «qué preparado compras y qué dice su etiqueta», y ante uno por debajo del 35 % o con grasa vegetal, «consulta a tu servicio de consumo». | `CUN-V06` (media), `CUN-42` |

## 3. Correcciones de la refutación aplicadas

A1 → `CUN-29` y `CUN-40` (dos figuras: trabajador nocturno del ET 22-6 h ≥ 3 h o ⅓ anual frente al plus del convenio 0-8 h al 25 %; con entrada a las 5:30 hay media hora legal) · A2 → `CUS-31h/i` (`baja`, «PROHIBIDO: anuncios reeditados») y `CUS-31` (mediana recalculada: **500 €/m²**, no 571) · A3 → `CUN-10` (sin «media cuota del 676»; con `CHN-73`) · A4 → `CUN-35` (Ley 12/2012 art. 3.3-3.4 y 2.2 citados literalmente) · A5 → `CUN-26` (**1,20 m** para filtros de gas o parrilla) · A6 → `CUN-28` (restituido «de utilización móvil») · A7 → `CUN-39`, `CUS-54`, `CUS-55`, `CUS-56` (SMI 2026 como suelo; Jooble fuera) · A8 → `CUS-19` (~×1,5, no ×4) · A9 → `CUS-30` · A10 → `CUS-M05` · A11 → `CUN-V06` · A12 → `CUN-02` y `CUS-38` · A13 → `CUN-09` y `CUN-35` (citan `CHN-49b`) · A14 → `CUN-05` (parte B con las tres condiciones del art. 2.3).

## 4. Hallazgos nuevos que tocan decisiones firmadas (para la SPEC)

1. **D6, atribución.** El «un poquito más del 50 %» no lo dice «una dueña»: lo dice **Javier, hijo de la fundadora y gestor de La Artesana**, y es «rentabilidad» según el periodista (`CUS-30`). Y `CUS-?` de D6 es `CUS-30`.
2. **D3, ancla de precio.** Visto el anuncio de los **290 €**: es un clasificado de **enero de 2016** (`CUS-M05`), peor que «sin fuente vista». Y la ancla que queda, los **1.290 € de `CUS-M06`**, sale de Milanuncios, **bloqueado hoy**: no está re-verificada. Quedan el canon de Churros Factory (12.000 €, lexpress, verificado) y la renta de 910 €/mes (`CUS-02`, no re-verificada).
3. **D15 / FAQ 4.** El techo «82.000-95.000 €» tiene el 82.000 de `CUS-02`; **el 95.000 sale solo de `CHS-37b`**, que `CUS-02` corrige («82.000 € negociable, no 82-95.000»). Con sala, el techo defendible es 82.000 €.
4. **`CUN-26`, matiz omitido por la lente.** En usos distintos de hospitalario y residencial público, las cocinas con **extinción automática no son local de riesgo especial** (nota 2 del CTE), aunque siguen sujetas a la nota 3. El libro 1 debe poder decirlo.
5. **`CUS-33g`.** La ficha del fogón de 80×80 a gas natural (2.890 € sin IVA) **no dice «22 L»**: no se afirma capacidad. **`CUS-40`** (rellenadora 330 €/520 €) no se reencontró: los 5.014,45 € y 9.447,35 € de la dotación incluyen esa línea; sin ella, **4.684,45 € y 9.117,35 €**.
6. **`CUS-38`.** Infoagro muestra **603,79 € con IVA**; el 499 € sin IVA es cálculo (603,79 / 1,21).
7. **Convenio de Madrid.** Dos gratificaciones extraordinarias (art. 26) → el SMI se compara con 14 pagas **suponiendo** una mensualidad cada una (no verificado): nivel V clase C = 17.311,76 €/año frente a 17.094 €.
8. **`CUS-M06`/`CUS-02`/`CUS-31`** y el parche **D7** a la hermana: `CHS-31` (85-90 %) sigue en lista negra (`CUS-01`: «85-90» no aparece en la página de Loomis).

## 5. Tabla de vigencia y riesgo de caducidad (a 3-oct-2026)

| Norma o fuente | Estado | Última actualización vista | Riesgo |
|---|---|---|---|
| Orden 26-01-1989, aceites calentados (`CUN-01…03`) | En vigor; arts. 7, 8, 10-12 derogados; norma básica | 29-03-2013 | Bajo; una norma nueva cambiaría el 25 % |
| Rgto. (UE) 2017/2158 y Rec. 2019/1888 (`CUN-04…06`) | En vigor; **revisión con niveles máximos en consulta** (`CUN-08`, fuente secundaria) | DOUE 2017 / 2019 | **Alto**: mirar EUR-Lex en cada 2.x |
| RDLeg 1175/1990, tarifas IAE (`CUN-09…14`) | En vigor | 21-03-2026 | Medio |
| RD 10/2025, CNAE-2025 (`CUN-15`) | En vigor | 15-01-2025 | Bajo |
| RD 650/2011 (`CUN-17`) y tipos de IVA (`CUN-18`) | En vigor; sin consulta DGT localizada | 04-10-2023 | Medio (zona gris) |
| RD 199/2010, venta ambulante (`CUN-19`) | **DEROGADO** 07-08-2021 | — | No citar |
| Ley 7/1996, arts. 53-55 (`CUN-20`) | En vigor | 30-03-2022 | Bajo |
| RD 1021/2022 y Rgto. 852/2004 (`CUN-21`, `22`) | En vigor | 21-12-2022 | Bajo |
| Ley 12/2012, Anexo y arts. 2-3 (`CUN-35`) | En vigor | 29-09-2022 | **Alto**: sostiene el «despacho sin licencia previa» |
| OCAS de Madrid (`CUN-23…25`) | En vigor; modificaciones posteriores no comprobadas | BOCM 16-04-2021 | Medio |
| Orden de horarios de Madrid, 21-04-2022 (`CUN-34`) | En vigor; posteriores no comprobadas; **deroga la Orden 1562/1998** | BOCM 29-04-2022 | Medio |
| CTE DB-SI (`CUN-26`) · RIPCI (`CUN-38`) · RD 919/2006 (`CUN-28`) | En vigor | RD 164/2025 · 03-09-2025 · 03-09-2025 | Medio |
| Ley 7/2022 (`CUN-27`, `41`) | En vigor | 02-04-2025 | Medio (plásticos) |
| ET art. 36 (`CUN-29`) | En vigor | 04-12-2025 | Medio (registro horario digital pendiente) |
| ALEH VI (`CUN-31`, `32`) | En vigor **hasta 31-12-2030** | BOE 04-09-2026 | Bajo |
| Convenio de hostelería de Madrid (`CUN-39`, `40`, `V01`) | **Vencido 31-12-2025; nuevo en negociación; tablas de 2025** | BOCM 06-04-2024 | **Alto**: cambia el libro 8 y el P&L |
| Convenio de Toledo (`CUN-V05`) | 01-01-2025 a 31-12-2026, con ultraactividad | BOP 15-07-2025 (según buscador) | Alto a final de 2026 |
| RD 1055/2003 (`CUN-42`, `V06`) | En vigor, sin modificaciones | 05-08-2003 | Bajo; la interpretación es el riesgo |
| Ordenanzas municipales de humos, ruido, terrazas y vertido | **No verificadas** salvo Madrid | — | Alto: siempre pregunta al ayuntamiento |

## 6. PROHIBICIONES: lo que el copy y los documentos NO pueden afirmar

1. «La ley te obliga a controlar la acrilamida de los churros» (`CUN-04`, `07`); «cumplimiento acrilamida»; la parte B «a las franquicias» sin las tres condiciones (`CUN-05`).
2. **Cualquier temperatura de fritura del churro** («180 °C», «175 °C»): V-02. Los 175 °C son de patatas.
3. Un tipo de IVA para el chocolate a la taza para llevar, en prosa (`CUN-18`, V-04).
4. «El despacho va por declaración responsable» sin «las obras que requieren proyecto —el conducto a cubierta incluido— siguen necesitando su licencia» (`CUN-35`); «necesitas/no necesitas licencia» sin decir el modelo.
5. Artículos del **RD 199/2010** o de la **Orden 1562/1998** (`CUN-19`, `34`); el **art. 8** de la norma de aceites (`CUN-03`).
6. «Convenio de churrerías», «la categoría de churrero» o «no existe convenio de churrerías» (`CUN-33`, `39`, `V05`).
7. «El churrero que entra a las 4-5 es trabajador nocturno» (`CUN-29`); confundir el plus del convenio con el trabajador nocturno del ET.
8. «Media cuota del 676», cuotas del IAE y la tasa de Ochavillo como orden de magnitud (`CUN-10`, `37`, `CHN-72/73`).
9. Requisitos de humos de Barcelona, Sevilla o Valencia (`CUN-X01`); «el medidor de polares demuestra el 25 %» (`CUN-02`); «la bombona de 15 kg te evita la instalación receptora» para un local (`CUN-28`).
10. «Ni “chocolate a la taza” ni “chocolate”» como regla cierta (`CUN-V06`); «sin gluten» como argumento de carta (`CHN-37`); «carnet de manipulador» (`CHN-69`); «el cucurucho cumple la ley de plásticos» (`CUN-41`).
11. **Cifras:** margen del churro de **85-90 %** (`CUS-01`); **traspasos de 107.000 y 120.000 €** y «anuncios reeditados» (`CUS-31h/i`); el **curso de 290 €** (`CUS-M05`); el **50 %** como margen bruto o atribuido a «una dueña» (`CUS-30`); sueldos de Jooble (`CUS-56`) y personal de Loomis (`CUS-05`); 540 kg/h, «absorbe un 30 % menos / dura el doble», «docena a 12 €», «facturamos 60.000 €», objetivos de franquiciador («150 franquicias»), «Maestro Churrero desde 75.000 €» (lista negra de L4).
12. «No existe ninguna guía de pago» (solo «no encontramos»), «hay N churrerías en España» (`CUS-07`), «verificado contra el BOE» en copy comercial.

## 7. Lo que NO se pudo verificar hoy

Milanuncios (captcha): `CUS-02`, `CUS-31a…i`, `CUS-M06`. Jooble (403), Aragón Digital (404), Envanature (404), AESAN `ACRILAMIDA.pdf` (404). Petete/DGT (504) e Iberley (403). REGCON y el buscador del BOCM. BOP de Toledo 2025 (nº y fecha de un buscador). Foros solo por título. Churrofácil `CUS-40`, `CUS-34a` (con cortador 945 €) y campana de 1500 no se reencontraron. Lo que sigue pendiente para F2: abrir las webs propias de Maestro Churrero, Harimsa, Tardienta y Harinas Costas, reconfirmar el listado FEHR-Geregras y pedir cotización real de cafetera, vitrina y TPV.

Via: Claude Code
