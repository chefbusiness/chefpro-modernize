# Pastry Shop Checklists Kit Pro — revisión adversarial de F2 (24-oct-2026 · sesión Claude Code)

Revisor único. Fuentes:
- `pastry/revision/dump_en.txt` / `dump_es.txt`, 6.498 líneas cada uno, alineados por línea; «L» = línea del volcado
  (la misma en EN y ES);
- `pastry/SPEC.md`, `pastry/F2-NOTAS.md`, `pastry/mapas_pastry.py` y `textos_en/{heredado,G1,G2}.json` (ids `cXXXX`);
- el formato y las lecciones de `chocolate/revision/REVISION-F2.md` e `icecream/revision/REVISION-F2.md`.

Solo lectura y `grep` de los volcados; sin openpyxl. Comprobado en la web:
- **29 CFR 570.62 (HO 11)**, Cornell LII: la orden cubre a los menores **de 16 y 17 años**. La excepción (b)(1) es para
  batidoras de sobremesa **portátiles**, **no cableadas a la red**, de **½ hp o menos** y con bol de **5 qt o menos**.
  También hay una excepción (b)(2) para las laminadoras de pizza con protecciones, pero no cubre limpiarlas.
- **29 CFR 570.33**, Cornell LII: (e) prohíbe a los de 14-15 años manejar **cualquier máquina eléctrica** («any
  power-driven machinery»), y (h), toda actividad de horneado. El horario (570.35: nada antes de las 7 AM) es memoria del
  revisor, no se ha consultado.
- **TCS en vitrina**: las fuentes encontradas son de fabricantes de vitrinas, no normativa. Coinciden en que la bollería
  con crema o natillas va a vitrina refrigerada a 41 °F. La clasificación TCS se apoya en la definición de §1-201.10:
  la crema pastelera tiene aw y pH de TCS, y el propio kit la trata como TCS (enfriado 3-501.14, date marking).

## Veredicto

**Hay 1 BLOQUEANTE y 8 MAYORES; además, 22 menores.** Fuera de la EN no he encontrado ninguna **ERRATA ES de seguridad**
nueva (las del SPEC §5 siguen en pie). Sí hay **3 erratas ES de maquetación** que la EN hereda (§ERRATAS ES).

**El BLOQUEANTE (B1)** es el patrón que ya se cazó en la chocolatería: **producto TCS a temperatura ambiente**. Lo
introduce la propia EN:
- el ES dice «napolitanas» y la EN escribe **«custard danishes»** en la vitrina de bollería, con la especificación
  «Ambient»;
- el calendario manda el producto con crema a la vitrina refrigerada **solo «in hot weather»**;
- lo salado (quiche, empanada de atún, croissant de jamón y queso) no tiene ninguna regla de conservación.

Un inspector que aplique la propia regla del kit («cream-filled: 41 °F or below») encuentra una infracción prioritaria
de mantenimiento en frío durante las 12 horas que la tienda está abierta.

**Lo que se pedía mirar y está bien:**
- **Horas (D9).** Obrador de 5:00 a 7:50 AM, primera hornada en la vitrina antes de las 8:00, tienda de 8:00 AM a 8:00 PM,
  puerta cerrada a las 7:50 PM y vitrinas encendidas 45 min antes de montar (6:45 → 7:45). Es el horario real de una
  bakery-café de EE. UU. Las conversiones de proceso son exactas (72–75 °F, 54–57 °F, 1/8 in, 375–400 °F, 450–480 °F,
  oz/g, curvas de templado).
- **Date marking.** «7 days max at 41 °F, day 1 = day made (3-501.17); 24 h is the kit's quality target, not a legal
  limit» es correcto y está dicho igual en el 02 C12 (L520), el 13 B12-B13 (L5964-5965), «Prep Labels» B2 y
  «Shelf Life» A24 (L6263).
- **Enfriado 3-501.14** en la crema pastelera (02 B7/C7, L489-490), en el abatidor y en los rangos del 13. No aparece donde
  no toca.
- **Merengue 3-302.13** en las mousses (02 B15-B16). Hay una duda técnica sobre el merengue italiano: véase «dudas».
- **Recepción 3-202.11** (13 A38, L6066): 41 °F; huevos en un camión con el aire a 45 °F o menos; leche a 45 °F solo
  donde lo permita la ley láctea y enfriada a 41 °F en 4 h (3-501.14(D)); congelado sin descongelar. El contenido es
  correcto. Falla la CF y la redacción (m11).
- **3-501.19.** Bien citado: 4 h solo con procedimiento escrito. Los 2 h son una regla del kit (13 A40, L6035), aunque
  hay un matiz (m13).
- **Sanitizante con tiras** (4-501.114, 01 B21/B9). **3-602.12(C)** siempre con «where your state has adopted it».
- **Alérgenos.** FALCPA + FASTER; los 9 de EE. UU. en sus columnas, sulfitos desde 10 ppm (21 CFR 101.100(a)(4)) y las 4
  columnas UK marcadas «(UK)». La lista de frutos de cáscara del «Case Sign» C19 coincide con la de la FDA de 2025: sin
  coco y con piñón. El borrador queda bloqueado con «DO NOT PUBLISH» hasta verificarlo. **No se inventan obligaciones
  de etiqueta de envasado**: no hay ni una cita de 3-602.11, que era la lección de la heladería.
- **Encargos (11).** El depósito es «common practice, not law; check your state's rules on nonrefundable deposits». TCPA
  (47 CFR 64.1200) y CAN-SPAM están bien acotados, la casilla de marketing va aparte y sin premarcar, con «does not affect
  your order» (la condición de compra de la TCPA), y hay firma del cliente en A42. No se inventan obligaciones.
- **Donación.** 42 U.S.C. 1791, con «check your state and county rules».
- **Calendario B02.** Es cronológico en las filas 4-15 y deja las variables al final:
  - King cake de Jan 6 a Mardi Gras, con pico en las comunidades hispanas y en la costa del Golfo;
  - Pi Day y St. Patrick's;
  - Mother's Day el 2.º domingo de mayo y Father's Day el 3.º de junio;
  - Day of the Dead con pan de muerto;
  - Thanksgiving el 4.º jueves, con el miércoles como día de recogida de pies;
  - Black Friday y Small Business Saturday.
- **Sin restos de España.** No quedan Reyes (salvo «rosca de Reyes»), roscón, turrón, comuniones a la española, IVA, €,
  kg ni °C. Los ejemplos de producto son de pastry shop de EE. UU. Versión «2.0 · October 2026» en los 15.
- **Plantillas 10-13.** Funcionan:
  - las categorías del desplegable, del SUMIF y del plan semanal son idénticas;
  - en el 11, saldo = total − depósito;
  - la matriz 43 × 14 alimenta la carta;
  - las CF del 13 casan con sus cabeceras (B:C 32-41, D:E 36-41, F:G > 0, H:K 32-41, L > 70, M > 120).
- **Código común: `PT_UNIDAD = 5,25 pt` es razonable.** Una unidad de ancho de Excel son 7 px con Calibri 11, y 7 px ×
  0,75 = 5,25 pt. «Wheat (gluten)» mide unos 15 caracteres × 6 px ≈ 68 pt, frente a los 95 pt de la fila.
- **09.** Confirmado con el volcado: el área de impresión de «Instructions» es `$A$1:$A$20` y el texto está en B2:B30
  (L2810, igual en el ES). Los rótulos del resumen están en A41-A46, con los importes en B (L2966-2976). El ancho de 5 no
  se ve en el volcado, que no trae anchos; lo doy por bueno con `cortadas.py` de la F2. Véase M8.

**Los 8 MAYORES:**
- **M1.** No hay ninguna tarea de producción contra el **contacto cruzado de alérgenos**: harina de almendra (macarons,
  financiers), pralinés, sésamo en los panes y el pedido con alergia confirmada. Solo hay etiquetado.
- **M2.** No hay control de **salud del personal**: exclusión por vómitos, diarrea o ictericia (2-201.11/2-201.12).
  Tampoco de lavamanos ni de **contacto sin mano desnuda** en el mostrador (3-301.11).
- **M3.** Las propuestas de la matriz dejan la **leche como traza (○)** en la concha y en los polvorones (Mexican wedding
  cookies). En EE. UU., las dos llevan casi siempre leche o mantequilla.
- **M4.** «**Fruit pies (apple, pecan)**» y «**cream pies (pumpkin, sweet potato)**» están mal clasificados. El pecan
  pie no es de fruta, y el de calabaza y el de boniato son custard pies.
- **M5.** Menores: la excepción de las batidoras de 5 qt se presenta para todos los menores de 18 y sin sus condiciones.
  Para los de 14-15 años no existe, porque 570.33(e) les prohíbe toda máquina eléctrica. Falta además su horario.
- **M6.** Rosca de Reyes con el calendario de **España**: el 60-70 % del volumen «para la tarde del 5». En las comunidades
  mexicanas de EE. UU., el día fuerte es el **6**. Además, se rellena sin regla de frío.
- **M7.** «**Tempered** chocolate» en la mousse (a 113–122 °F) y «**Temper** before using» en la ganache. Son calcos de
  «templar / atemperar» que un pastry chef lee como templado del chocolate.
- **M8.** 09 «Cash Drawer Closing»: los rótulos del resumen (total, fondo, tarjetas, TOTAL COLLECTED, Z, OVER/SHORT)
  salen **cortados** en una columna de 5. Es la parte de la hoja que da el resultado.

**Cómo se corrige.** Todo con texto por celda (`POR_CELDA` / `ADAPTAR` / G1-G2 JSON), sin filas nuevas, salvo M8, que
necesita una desviación de G1 declarada o arreglar antes el ES.

Hay que añadir a `REGLAS_US` las citas nuevas que G7 tiene que aceptar:
- 2-201.11 y 2-201.12;
- 3-301.11;
- 5-205.11 o 6-301.12;
- 29 CFR 570.33(e) y 570.35;
- 3-501.14, ya en la lista, para los pies.

`GRADOS_F_SPEC` solo cambia si se adopta m1 (160 °F). Las demás correcciones usan 41, 45, 70 y 135, que ya están.

| # | Sev. | Dónde | Qué |
|---|---|---|---|
| B1 | BLOQUEANTE | 02 «Decorating & Finishing» B15/C15 (L655-656), c0208 · BONUS-02 G10 (L6437), c1320 · 08 «Shop Opening» B15 (L2631), c0697 · 13 «Shelf Life» A17/D17 (L6255-6258) · 10 «Weekly Plan» A8, A13, A38-A40 (L3341, L3356, L3413-3419) | Bollería de crema y salado TCS en vitrina ambiente; frío «solo con calor» |
| M1 | MAYOR | 02 (las 3 hojas) · 04 «Pastry Cook» · 11 «Instructions» B15 (L4340) · 12 «Allergen Matrix» J20, J36, M40-M44 | Sin control de contacto cruzado en producción |
| M2 | MAYOR | BONUS-01 «Pre-Shift Huddle» B23 (L6350), c1274 · 01 «Kitchen Opening» · 04 «Counter Associate» B8/B11 (L1374, L1389), c0373/c0376 · 08 «Shop Opening» B21 (L2661) | Sin salud del personal, lavamanos ni «no bare-hand contact» |
| M3 | MAYOR | 12 «Allergen Matrix» I8 (L4775) · I28/V28 (L4958, L4963) | Concha y polvorones con la leche en ○ |
| M4 | MAYOR | 06 «Thanksgiving (Nov)» B13 (L2294), c0621 · B14 (L2299), c0622 · B22 (L2330), c0632 | Pecan como fruit pie; pumpkin y sweet potato como cream pies; enfriado sin parámetros |
| M5 | MAYOR | 06 «Holiday Season» B9 (L1778), c0475 | Excepción de HO 11 mal acotada; sin 570.33(e) ni horario de 14-15 años |
| M6 | MAYOR | 06 «Holiday Season» B31-B33 (L1861-1871), c0507/c0511 · B29 (L1851) | Rosca de Reyes con el reparto de España (día 5); rellena sin frío |
| M7 | MAYOR | 02 «Creams & Fillings» B15 (L526), c0172 · 13 «Shelf Life» D7 (L6219), c1217 | «Tempered» / «Temper» por «templar / atemperar» |
| M8 | MAYOR | 09 «Cash Drawer Closing» A41-A46 (L2966-2976) | Rótulos del resumen cortados en la columna A, de 5 de ancho |
| m1 | menor | 02 «Creams & Fillings» B8/C8 (L495-496), c0161 | Merengue suizo con «syrup at 244–250 °F» |
| m2 | menor | 02 «Doughs & Fermentation» B30/B31 (L424, L430), c0143/c0145 | «sablee» / «brisee» sin tilde parecen erratas |
| m3 | menor | 02 «Creams & Fillings» B18 (L544), c0178 | «Make pralines and nut praline» (en EE. UU., «pralines» es el dulce de pecana) |
| m4 | menor | 05 «Monthly Maintenance» B6 (L1574), c0424 · 06 «Easter» B8 (L2008), c0544 · 08 B24/B22 (L2676, L2788) | Jerga europea: «pyrolytic cycle», «bells», «shutters» |
| m5 | menor | 06 «Holiday Season» B12 (L1793) | Horario especial el «Jan 6» en lugar del 1 de enero |
| m6 | menor | 06 «Valentine's Day» B17 (L1965) · «Mother's & Father's Day» B14 (L2119) | «Add counter staff» asignado al Counter associate (en el resto, al Manager) |
| m7 | menor | 01 «Kitchen Closing» B27/B29 (L253, L263) · 08 «Shop Opening» B5 (L2581) | Llaves y alarma: Head pastry chef de 5 AM a 9 PM; «nada fuera de cámara» a las 6:30, antes de vaciar la vitrina; alarma desconectada a las 6:45 |
| m8 | menor | 11 «Pickup Schedule» A17 (L4651) | Franja de recogida a las 8:00 PM con la puerta cerrada a las 7:50 |
| m9 | menor | 12 «Case Labels» B2 (L5947), c1146 · c1122 (L5899, L5907) · 11 «Order Form» A23 (L4391), c0983 | Leyenda sin pescado aunque la matriz trae un producto con pescado; frase de contacto cruzado sin pescado; A23 olvida los sulfitos |
| m10 | menor | 12 «Allergen Matrix» N24 (L4925) frente a N10 (L4795) | Sulfitos de los hot cross buns en ○ con la piel confitada; el pain aux raisins, en ● |
| m11 | menor | 13 «Receiving Log» CF G5:G34 > 41 (L6073) · A38 (L6066), c1194 | Huevos y leche legales a 42-45 °F salen en rojo; el paréntesis de la leche se lee al revés |
| m12 | menor | 13 «Temperature Log» D4/E (L5982), L5 y M5 (L5999-6000) | La lectura de la mañana de la cámara de masas cae en plena subida de temperatura; «Minutes» sin decir de qué |
| m13 | menor | 13 «Temperature Log» A40 (L6035) | El time-as-a-control no se aplica a posteriori a una avería |
| m14 | menor | 13 «Shelf Life» A10 (L6228), c1222 | «Ganache truffles (cooked)» no se entiende |
| m15 | menor | 11 «Instructions» B17 (L4341), c0945 · «Order Form» A46 (L4427) | Destruir las fichas con alergias al mes quita la prueba ante una reclamación |
| m16 | menor | BONUS-02 fila 9 B9/G9 (L6427-6431) | «May–Jun» frente a «Apr–Jun» del 06; First Communion presentado como general |
| m17 | menor | BONUS-02 «Instructions» B7 (L6382), c1283 | «Mothering Sunday (March)» (puede caer a primeros de abril) |
| m18 | menor | BONUS-02 G15 (L6467), c1341 | «Wholesale orders from other food businesses» sin el aviso de licencia |
| m19 | menor | 12 «Allergen Matrix» A25 (L4929) · BONUS-02 E4 (L6399) · 06 B29 (L1851) | Paczki en la matriz sin fecha (Fat Tuesday) en ningún calendario |
| m20 | menor | 09 «Instructions», área (L2810) · 09 «Monthly Cash Log», área A1:I38 con J4 «Closed by» (L2987, L3001) | Instrucciones que salen en blanco al imprimir; columna «Closed by» fuera del área de impresión |
| m21 | menor | 10 «Made vs Sold» DV K5:K254 (L4256) | El desplegable no trae «day-old markdown», que el 01 y el 13 sí usan |
| m22 | menor | 05 «Weekly Deep Clean» / «Monthly Maintenance» | Sin control de plagas (trampas, registro del exterminador) |

---

## BLOQUEANTE

### B1 · Bollería de crema y salado TCS en vitrina ambiente; frío «solo con calor»

**Dónde:**
- 02 «Decorating & Finishing» B15/C15 (L655-656), c0208:
  `Stock the viennoiserie case (croissants, pain au chocolat, custard danishes)` · `Ambient · restock in small batches`.
  El ES dice «napolitanas» (L655 ES), sin decir que sean de crema: **lo introduce la EN**.
- BONUS-02 G10 (L6437), c1320: `Adapt the case to cold items: in hot weather, everything cream-filled goes in the
  refrigerated case at 41 °F or below`. El ES dice solo «Adaptar vitrina a productos fríos»: el «in hot weather» es nuevo.
- 08 «Shop Opening» B15 (L2631), c0697: `viennoiserie first, then refrigerated pastries, savory last`. Lo salado no tiene
  destino ni temperatura.
- 10 «Weekly Plan» y «Made vs Sold» (L3341, L3356, L3413-3419), y 12 «Allergen Matrix» A7, A12, A37-A39:
  - «Custard danish» y «Cream-filled croissant», en la categoría Viennoiserie;
  - «Quiche», «Empanada» (de atún en la matriz) y «Ham & cheese croissant», en Savory.
- 13 «Shelf Life» A17/B17/D17 (L6255-6258): `Baked viennoiserie · Room temperature, in the case · Same day · … Cream-filled:
  case at 41 °F`. No hay ninguna fila para lo salado.
- BONUS-01 B6 (L6292): custard danishes en la bollería del día.

**Qué falla.**
- **Mantenimiento en frío.** La crema pastelera, la nata y el queso crema horneados en una danish siguen siendo TCS
  (§1-201.10: aw > 0,92 y pH > 4,6). El propio kit trata la crema pastelera como TCS: la enfría por 3-501.14 y le pone
  date marking. La quiche (huevo y lácteos), la empanada de atún y el croissant de jamón y queso también son TCS. Lo TCS
  en frío va a **41 °F o menos** (§3-501.16(A)(2)), salvo con un procedimiento escrito de time as a control (§3-501.19:
  4 h, y luego se tira).
- **El kit se contradice.** El 13 D17 dice «cream-filled: 41 °F», pero el 02 C15 pone las custard danishes en «Ambient» y
  el calendario solo pide frío con calor. Un dependiente que siga el 02, o el calendario en noviembre, deja crema
  12 horas en vitrina ambiente. **El inspector puede usar las palabras del propio kit.**
- **Lo salado no tiene regla en ningún sitio,** y el 08 lo coloca «al final» del montaje sin decir en qué vitrina.

**Arreglo** (texto por celda; solo usa 41 °F y 3-501.19, ya en `REGLAS_US`):
- 02 B15 (c0208): `Stock the viennoiserie case (croissants, pain au chocolat, palmiers, fruit danishes)`.
- 02 C15 (`POR_CELDA`): `Ambient, same day · custard-, cream- or cheese-filled pieces go in the refrigerated case at 41 °F or below (FDA Food Code 3-501.16)`.
- 08 B15 (c0697): `Stock the case in order: viennoiserie first, then the refrigerated case (cream-filled pastries, quiche, savory items with meat, fish, egg or cheese at 41 °F or below), bread last`.
- BONUS-02 G10 (c1320): `Adapt the case to summer items; all year round, everything cream-filled goes in the refrigerated case at 41 °F or below`.
- 13 «Shelf Life» D17 (`POR_CELDA`): `Next day: day-old discount or waste. Custard-, cream- or cheese-filled pieces and savory items (quiche, ham & cheese, empanadas): case at 41 °F or below (3-501.16), or time as a control with a written procedure (3-501.19: 4 h, then discard)`.
- No hace falta cambiar los nombres de producto del 10 y el 12: la regla queda en las celdas operativas.

---

## MAYORES

### M1 · Sin control del contacto cruzado de alérgenos en producción

**Dónde.** El 02 entero (L289-697) y el 04 «Pastry Cook» (L1184-1271). Las únicas menciones a alérgenos fuera del 11 y el
12 son de **etiquetado** (01 B27, 02 B18, 03 B19, 04 B7/B9, 08 B17/B18, B01 B17).

Al mismo tiempo, la matriz del 12 propone:
- harina de almendra como ingrediente principal en los macarons (J20, L4886) y los financiers (J36, L5036);
- frutos secos en los pralinés (02 B18) y en la carrot cake;
- sésamo como traza en todos los panes (M40-M44).

El 11 B15 (L4340) pide «tell the kitchen in writing and check every component», pero ninguna checklist dice qué hace el
obrador con esa nota.

**Por qué.** En una pastry shop, el contacto cruzado es el riesgo de alérgenos número uno:
- la harina de almendra vuela desde el tamiz y la batidora;
- el sésamo de la bandeja de los panes acaba en la masa de bollería;
- un pedido «sin frutos secos» se monta en la misma mesa que el praliné.

El kit lo reconoce en la carta («cross-contact is possible», c1122), pero no tiene ninguna tarea que lo controle. La
heladería y la chocolatería lo cazaron igual (M1 de la chocolatería).

**Arreglo**, sin filas nuevas:
- 02 «Creams & Fillings» B18 (c0178, junto con m3): `Make praline paste and nut brittle on the nut station: dedicated scoops, sifter and bowls, cleaned before the next product (allergen cross-contact)`.
- 02 «Doughs & Fermentation» B22 o B25: añadir `· sesame and seed toppings on a separate sheet and bench`.
- 04 «Pastry Cook» B17 (custom orders): `Prepare custom orders; with a CONFIRMED allergy (→ 11), make it first in the day on a cleaned and sanitized bench with clean tools, and label it on its own`.
- 01 «Kitchen Opening» B21 (sanitize): `… · nut flours and seeds in closed, labeled bins`.

### M2 · Sin control de salud del personal, de lavamanos ni de «sin mano desnuda»

**Dónde.**
- BONUS-01 «Pre-Shift Huddle», sección «Shift Team» (L6348-6363): B23 `Who is working today and in what position`
  (c1274). No hay pregunta de salud.
- 01 «Kitchen Opening» (L19-151) y 08 «Shop Opening»: el único control de jabón y papel es el de los aseos de clientes
  (08 B21, L2661). No se miran los lavamanos del obrador ni del mostrador.
- 04 «Counter Associate» B8/B11 (L1374, L1389): servir y encajar producto listo para comer, sin pinzas ni papel.
- grep de «sick / ill / vomit / 2-201 / hand / 3-301 / gloves»: 0 resultados. El SPEC lo dejó fuera porque el ES no lo
  trae («enfermos, lavamanos»).

**Por qué.**
- **Salud del personal.** El Food Code pide que el responsable sepa los síntomas que obligan a avisar y que excluya o
  restrinja al trabajador: 2-201.11 y 2-201.12, con exclusión por vómitos, diarrea e ictericia. Es lo primero que
  pregunta un inspector en una visita a una bakery.
- **Lavamanos.** Su acceso y su dotación (5-205.11, 6-301.12) son otra infracción de las más citadas.
- **Mano desnuda.** El mostrador de una pastry shop toca producto listo para comer todo el día (3-301.11).
- **Comparación.** La chocolatería lo tenía mal («reassign»); aquí directamente no está. Un manager de EE. UU. lo nota.

**Arreglo** (`POR_CELDA` en celdas existentes):
- B01 B23: `Who is working today and in what position; anyone with vomiting, diarrhea or jaundice goes home and tells the manager (excluded, FDA Food Code 2-201.11 / 2-201.12)`.
- 01 «Kitchen Opening» B17 (c0037): `Set up the day's mise en place; hand sinks stocked with soap and paper towels and kept clear (FDA Food Code 6-301.12)`.
- 04 «Counter Associate» B11 (c0376): `Prepare boxes and to-go packaging; pick up pastries with tongs or bakery tissue, never bare hands (FDA Food Code 3-301.11)`.

### M3 · Concha y polvorones con la leche como traza

**Dónde.** 12 «Allergen Matrix»:
- I8 (L4775): `Concha (pan dulce)`, leche en ○, sin nota. Hereda el perfil de la **ensaimada**, que es de manteca de cerdo
  (L4770-4775 ES).
- I28 (L4958): `Polvorones (Mexican wedding cookies)`, leche en ○. La nota V28 (L4963) dice «the proposed profile assumes
  lard or shortening; with butter, milk is ●».

**Por qué.** La regla del SPEC «mismo perfil que la referencia ES» falla en estas dos filas:
- la concha de EE. UU. es una masa enriquecida con leche o mantequilla, y la costra lleva mantequilla o manteca vegetal;
- las Mexican wedding cookies (snowballs, Russian tea cakes) se hacen con mantequilla en la inmensa mayoría de las
  recetas de EE. UU.

Como propuesta de partida, la leche en ○ **infradeclara** el alérgeno en los dos casos. El bloqueo «DO NOT PUBLISH» lo
mitiga, pero la propuesta en gris es justo lo que un dueño con prisa acepta. Es el error más caro de una carta de
alérgenos.

**Arreglo.**
- I8 y I28 → `●` (como propuesta).
- V8: `Milk: most conchas use milk and butter; only with water and shortening is it ○`.
- V28: `Milk: Mexican wedding cookies are usually made with butter (●); only with lard or shortening is it ○. Sesame: some polvorones contain it — check yours`.

### M4 · Pies mal clasificados y sin parámetros de enfriado

**Dónde.** 06 «Thanksgiving (Nov)»:
- B13 (L2294), c0621: `Bake the fruit pies (apple, pecan)`;
- B14 (L2299), c0622: `Bake the cream pies (pumpkin, sweet potato), cool them and hold at 41 °F or below: they are TCS foods (FDA Food Code 3-501.16)`;
- B22 (L2330), c0632: `cream pies come out of the refrigerated case`.

**Por qué.**
- **Nomenclatura.** En una pastry shop de EE. UU., «cream pie» es el de crema pastelera sobre base ya cocida (banana,
  coconut o chocolate cream). El de calabaza y el de boniato son **custard pies**. El pecan pie no es «fruit pie»: su
  relleno es un custard de huevo y jarabe. Cualquier baker lo ve en la primera lectura de la hoja más vendida del año.
- **Seguridad.** Llamarlos «cream pies» no es inseguro, porque se mantienen a 41 °F. Pero el pecan pie queda en la tanda
  de «fruta», que el lector entiende como ambiente.
- **Enfriado.** «Cool them» va sin los parámetros de 3-501.14, que el kit sí da para la crema pastelera.

**Arreglo.**
- B13: `Bake the fruit pies (apple, cherry, berry)`.
- B14: `Bake the custard pies (pumpkin, sweet potato, pecan), cool them (135 → 70 °F within 2 h, then 41 °F within 4 more h; FDA Food Code 3-501.14) and hold at 41 °F or below: pumpkin and sweet potato are TCS foods (3-501.16); treat pecan the same unless your health department accepts it as non-TCS`.
- B22: `… custard pies come out of the refrigerated case`.

### M5 · Menores: la excepción de HO 11 mal acotada y nada sobre los 14-15 años salvo el horneado

**Dónde.** 06 «Holiday Season» B9 (L1778), c0475: `under 18: no dough mixers, industrial mixers, sheeters or dividers, and no cleaning them — 29 CFR 570.62, benchtop mixers of 5 qt or less excepted; ages 14–15: no baking — 29 CFR 570.33(h)`.

**Por qué** (eCFR / Cornell LII, comprobado hoy):
- **A quién cubre HO 11.** 570.62 es una orden para los de **16 y 17 años**. La excepción (b)(1) exige que la batidora
  sea **portátil, de sobremesa, no cableada a la red, de ½ hp o menos y con bol de 5 qt o menos**. Tal como está escrito,
  «under 18 … 5 qt excepted» deja entender que un chico de 14 años puede usar la KitchenAid.
- **Los de 14-15 años.** 570.33(e) les prohíbe **toda máquina eléctrica**, no solo hornear (570.33(h)).
- **Horario.** Los de 14-15 años no trabajan antes de las 7 AM ni después de las 7 PM en periodo escolar, que es justo
  la temporada de esta hoja (570.35). El obrador del kit abre a las 5:00 y la vitrina, a las 6:45.

**Arreglo** (c0475):

> `Hire seasonal help if needed. Ages 16–17: no dough or batter mixers, sheeters, dividers or rounders, and no cleaning them (29 CFR 570.62, HO 11), except portable countertop mixers of 5 qt or less and ½ hp or less; ages 14–15: no power-driven machinery and no baking (29 CFR 570.33(e) and (h)), and no work before 7 AM or after 7 PM during the school year (29 CFR 570.35)`

Añadir 570.33(e) y 570.35 a `REGLAS_US`.

### M6 · Rosca de Reyes con el calendario de España y rellena sin frío

**Dónde.** 06 «Holiday Season»:
- B31 (L1861), c0507: `Bake the first batch of roscas overnight Jan 4 into Jan 5 (60–70% of volume, for the afternoon sale on the 5th)`.
  Es la traducción literal del ES (L1861 ES: «para la venta de la tarde del 5»).
- B32/B33 (L1866-1871), c0511: `fill to order` · `Fill with whipped cream, pastry cream or cream cheese`.
- B29 (L1851): se cierran los pedidos de rosca **y de King cake** el 2 de enero.

**Por qué.**
- **El día fuerte.** En España, el roscón se compra la tarde del 5. En las comunidades mexicanas e hispanas de EE. UU.,
  que son el público de la rosca según el propio B02 G4, se parte **la tarde o la noche del 6 de enero**. La venta se
  concentra el 5 y el 6, con pico el 6 y el fin de semana más cercano. El reparto 60-70 % el 5 hace producir de más ese
  día y quedarse corto el 6. Es justo el «resto de España» que había que buscar.
- **El relleno.** La rosca mexicana suele venderse sin rellenar. Si se rellena de nata, crema o queso crema, es una tarta
  de nata TCS (13 D16: 41 °F), y la hoja no lo dice (véase B1).
- **El King cake.** Su temporada va del 6 de enero a Mardi Gras (B02 E4), así que «cerrar sus pedidos el 2 de enero» no
  encaja (m19).

**Arreglo.**
- B31: `Bake the first batch of roscas on Jan 5 for pickups that day and the morning of Jan 6`.
- B32: `Bake the main batch overnight Jan 5 into Jan 6 (60–70% of volume: Jan 6 is the big day, families cut the rosca that afternoon or evening)`.
- B33: `If you sell filled roscas (whipped cream, pastry cream or cream cheese), fill to order and keep them in the refrigerated case at 41 °F or below; most Mexican-style roscas are sold unfilled`.
- B29: `Close the rosca de Reyes orders and assign pickup slots (King cakes: from Jan 6 until Mardi Gras)`.

### M7 · «Tempered» / «Temper» por «templar» / «atemperar»

**Dónde.**
- 02 «Creams & Fillings» B15 (L526), c0172: `Make chocolate mousse (tempered chocolate + cream + …)`, con C15 `Chocolate at 113–122 °F`.
  El ES dice «templar chocolate».
- 13 «Shelf Life» D7 (L6219), c1217: ganache · `Temper before using`. El ES dice «Atemperar antes de usar».

**Por qué.** En inglés de pastelería, «tempered chocolate» es chocolate precristalizado (82–90 °F, según la curva que el
propio kit da en el 02 C24). Una mousse se hace con chocolate **fundido** a 113–122 °F, que está fuera de templado, así
que la tarea se contradice con su propia especificación. En la ganache, «temper» se lee igual de mal: lo que se pide es
sacarla del frío a temperatura de trabajo. Un pastry chef lo ve enseguida.

**Arreglo.**
- c0172: `Make chocolate mousse (melted chocolate + cream + cooked Italian or Swiss meringue or pasteurized whites, FDA Food Code 3-302.13)`.
- c1217: `Bring to working temperature before using`.

### M8 · 09: rótulos del resumen de cierre cortados

**Dónde.** 09 «Cash Drawer Closing», A41-A46 (L2966-2976):
- `Total cash (count)`;
- `Starting bank (−)`;
- `Card sales, excl. tips`;
- `Other tenders + card tips paid in cash`;
- `TOTAL COLLECTED`;
- `POS Z: sales + tax, excl. tips`.

Están en la columna A, de 5 de ancho y con ajuste, y los importes van en B. La F2 lo midió (`cortadas.py`: 5 rótulos
cortados) y lo dio por «heredado». El volcado confirma la posición, no el ancho. **Errata ES** idéntica: «Efect/ivo»,
L2966-2976 ES.

**Por qué.** Es la parte de la hoja que da el resultado del día, el **OVER / SHORT**. En pantalla y en papel, el
encargado ve trozos de palabra junto a cada importe, y «Other tenders + card tips paid in cash» es justo la línea que
evita un descuadre falso. Un comprador de EE. UU. que imprima la hoja la verá rota.

**Arreglo** (dos opciones, a decidir en la F3):
- **Opción a.** Ensanchar la columna A de «Cash Drawer Closing» a unas 26 unidades y estrechar B en lo mismo. A solo
  lleva números de tarea, denominaciones y estos rótulos, y el área de impresión A1:F48 sigue cabiendo en Letter
  apaisado con «fit to width». Se declara como desviación de G1, igual que la D7 del 13 (`ANCHOS_EN` /
  `DESVIACIONES_G1['09']`). La misma corrección va en la próxima v2.x del ES.
- **Opción b.** Combinar A:B en las filas 40-47 y pasar los importes a C. Es más invasiva: obliga a tocar las fórmulas de
  B41-B47, la CF de B47, `CELDA_CACHE_MAL` y G5. Recomiendo la a.

---

## Menores

- **m1 · 02 B8/C8 (L495-496), c0161.** «Swiss or Italian meringue» con `Syrup at 244–250 °F`: el suizo no lleva almíbar.
  C8 → `Italian: syrup at 244–250 °F · Swiss: whites and sugar heated to 160 °F · butter at 64–68 °F`. Hay que añadir 160
  a `GRADOS_F_SPEC`, y de paso deja el suizo pasteurizado.
- **m2 · 02 B30/B31 (L424, L430), c0143/c0145.** «sablee» y «brisee» sin tilde parecen erratas a un lector de EE. UU.
  Dos salidas:
  - `FRASES_OK` con «sablée» y «brisée» (como «rosca de Reyes»);
  - `Make sweet tart dough (sable crust)` / `Make pie dough (pate brisee) for quiches / savory tarts`.
- **m3 · 02 B18 (L544), c0178.** «Make pralines and nut praline» calca «pralinés y praliné de frutos secos». En EE. UU.,
  «pralines» es el caramelo de pecana de Nueva Orleans → `Make praline paste and nut brittle` (con el añadido de M1).
- **m4 · Jerga europea.**
  - 05 B6 (c0424): `self-clean cycle (if your oven has one) or by hand with oven cleaner`, en lugar de «pyrolytic cycle».
  - 06 «Easter» B8 (c0544): `bunnies, eggs, chicks`, en lugar de «bells» (las campanas son francesas).
  - 08 B24/B22: `Raise the roll-down security gate (if you have one) and open the door`, en lugar de «security gate
    (shutters)».
- **m5 · 06 «Holiday Season» B12 (L1793).** `Set and post shop hours for Dec 24, 25 and 31 and Jan 1` (y el Jan 6 solo si
  se vende rosca). El 6 de enero no es festivo en EE. UU.
- **m6 · 06 «Valentine's Day» B17 (L1965) y «Mother's & Father's Day» B14 (L2119).** «Add counter staff» va asignado al
  Counter associate. Es una decisión del Manager, que es como lo hacen Holiday B24 y Thanksgiving B21. Cambiar D17/D14 a
  `Manager`.
- **m7 · Llaves y alarma (01 «Kitchen Closing» B27/B29, L253-266; 08 «Shop Opening» B5, L2581).** Viene del ES.
  - El Head pastry chef cierra con llave a las 9:00 PM después de entrar a las 5:00 AM.
  - «Check that no product is left out of the walk-in» va a las 6:30 PM, antes de que se vacíe la vitrina (7:55 PM).
  - El 08 desconecta la alarma a las 6:45 AM, con el obrador trabajando desde las 5:00.
  - Arreglo: 01 B27 a las `8:05 PM`; 01 B29, D = `Shift lead` (como el 08 B22-B23); 08 B5 → `Turn on the refrigerated bakery cases (disarm the shop alarm zone if the kitchen hasn't)…`.
- **m8 · 11 «Pickup Schedule» A17 (L4651).** Franja de las 8:00 PM con la puerta cerrada al público a las 7:50 (08 B7).
  Quitarla, o cambiarla por `7:30 PM` como última franja. El ES tiene la misma de las 20:00.
- **m9 · Coherencia de alérgenos.**
  - 12 «Case Labels» B2 (c1146): la leyenda no trae pescado, cacahuete ni marisco, aunque la matriz propone «Tuna
    empanada» con pescado en ● (F38, L5049-5053). Añadir `· F fish · P peanuts · SH shellfish`.
  - La frase verde de contacto cruzado (c1122) no incluye el pescado que la propia matriz usa. Añadir `fish` o decir
    `replace with your list`.
  - 11 A23 (c0983): `the rest are gluten for celiacs, sulfites and the UK ones`.
- **m10 · 12 N24 (L4925).** Hot cross buns con los sulfitos en ○ y la nota «si los llevan, decláralos como ingrediente,
  no como traza». La piel confitada casi siempre va sulfitada, y el pain aux raisins (N10) ya los propone en ●. Pasar a
  `●` como propuesta.
- **m11 · 13 «Receiving Log» (CF G5:G34 > 41, L6073; A38 L6066, c1194).**
  - Una entrega legal de huevos (aire ≤ 45 °F) o de leche (≤ 45 °F donde la ley lo permita) sale en rojo.
  - CF: ámbar para «más de 41 y hasta 45» y rojo por encima de 45, como desviación declarada igual que la D7.
  - O bien, nota en A42: `Red above 41 °F: for shell eggs and milk/cream, up to 45 °F can be accepted (see criteria) — write it in Reason / notes`.
  - En A38, el paréntesis de la leche se lee al revés («reject above 45 °F (allowed only where…)») →
    `milk and cream arrive above 45 °F (from 41 to 45 °F only where dairy law allows it, and cool them to 41 °F within 4 h; …)`.
- **m12 · 13 «Temperature Log».**
  - La cámara de masas (D4, 36–41 °F) es una retarder-proofer que sube a 75–79 °F antes de hornear (02 C12, L340): la
    lectura de la mañana sale roja todos los días. D4 → `Dough retarder (36 to 41 °F, read in retard mode)`.
  - M5 «Minutes» no dice de qué → `Min. to 70 °F`.
- **m13 · 13 A40 (L6035).** «Only a written time-as-a-control procedure allows up to 4 h» puede leerse como algo que se
  aplica después de una avería, y 3-501.19 exige que el producto esté marcado desde que sale del frío. Añadir:
  `(set up in advance and marked with the time; it cannot be applied after the fact to a unit failure)`.
- **m14 · 13 «Shelf Life» A10 (L6228), c1222.** «Ganache truffles (cooked)» traduce «Trufa cocida» (la crema de trufa de
  relleno) y no se entiende → `Cooked chocolate truffle cream (filling)`.
- **m15 · 11 privacidad (B17, c0945; «Order Form» A46, L4427).** «Shred them one month after pickup» viene del RGPD. En
  EE. UU., la ficha con las alergias declaradas es la prueba del negocio si hay una reclamación por lesiones, que puede
  llegar años después. Proponer:
  `Keep them locked up for as long as your insurer or attorney advises, then shred them`, y en A46,
  `How long: kept only as long as needed for the order, taxes and claims, then destroyed`.
- **m16 · BONUS-02 fila 9 (L6427-6431).**
  - B9 dice «May–Jun» y la hoja del 06 dice «Apr–Jun» → `Apr–Jun (varies)`.
  - G9: hay que dar contexto a la First Communion, que en EE. UU. es de las parroquias católicas →
    `strong in Hispanic, Italian, Polish and Filipino parishes`.
- **m17 · BONUS-02 «Instructions» B7 (c1283).** `Mothering Sunday (3 weeks before Easter: March or early April)`. La misma
  m19 de la chocolatería.
- **m18 · BONUS-02 G15 (c1341).** «Wholesale orders from other food businesses»: en muchos estados, vender al por mayor
  a restaurantes exige otra licencia o registro, distinta del permiso de retail →
  `Orders from restaurants and caterers (wholesale may need its own license — check with your health department)`.
- **m19 · Paczki y King cake.** La matriz trae «Paczki (filled doughnuts)» como Seasonal (A25, L4929), pero ningún
  calendario da su fecha.
  - B02 E4 → `… King cake until Mardi Gras (cream, cream cheese or praline filling) and paczki for Fat Tuesday`.
  - 06 B29: véase M6.
- **m20 · 09, áreas de impresión** (también son **errata ES**).
  - «Instructions» = `$A$1:$A$20` con el texto en B2:B30 (L2810): sale en blanco → `$B$1:$B$30`.
  - «Monthly Cash Log» = `$A$1:$I$38`, pero J4 «Closed by» (L3001) queda fuera → `$A$1:$J$38`.
  - Si G1 exige la misma área que el ES, se declara la desviación o se corrige antes el ES.
- **m21 · 10 «Made vs Sold» DV K (L4256).** El desplegable «Action» no trae la salida «day-old», que el 01 B17/B26 y el
  13 D17 sí usan. Añadir `Day-old markdown (next day, labeled area; never the regular case)`.
- **m22 · 05.** No hay control de plagas: ni trampas, ni puntos de entrada, ni el registro del exterminador, que es de
  las primeras cosas que pide un inspector. Añadir en una fila libre del «Monthly Maintenance»:
  `Pest control: check traps and entry points, file the pest control operator's report`.

---

## ERRATAS ES (kit-tareas-pasteleria LIVE)

- **De seguridad: ninguna nueva.** Las de alérgenos, frío y huevo que he mirado coinciden con su marco español. Siguen
  vigentes las ya listadas en SPEC §5: el merengue sin cocer en las mousses, «valóralo» en el 13 A40 y las zonas del 06.
- **De maquetación** (las hereda la EN por G1):
  1. 09 «Instrucciones»: área de impresión `A1:A20` con el texto en la B (L2810 ES). Sale en blanco.
  2. 09 «Cierre de Caja» A41-A46: rótulos del resumen en la columna A, de 5 de ancho (M8).
  3. 09 «Registro Mensual»: área `A1:I38` que deja fuera J «Responsable» (L2987, L3001 ES).
- **Técnica, no de seguridad:** 02 «Cremas y Rellenos» C8 da almíbar a 118-121 °C también para el merengue suizo (m1).

---

## Dudas

1. **¿Cuenta el merengue italiano como «cocido» para 3-302.13?** El 02 B15-B16 lo da por cocido. Con almíbar a
   244–250 °F, la clara montada no siempre llega a 155 °F durante 17 s (3-401.11(A)(2)). Algunos departamentos de salud lo
   aceptan y otros piden claras pasteurizadas. Propongo mantener la frase, pero dejar las claras pasteurizadas como opción
   recomendada si John quiere cerrar el flanco: `cooked Swiss meringue (160 °F) or pasteurized whites`.
2. **Pecan pie.** Su aw (≈ 0,80-0,85) hace que algunos estados lo acepten como no TCS. Por eso la redacción de M4 lo deja
   a criterio del departamento de salud en lugar de afirmar que es TCS.
3. **Custard danish o cheese danish horneada.** Algunas jurisdicciones la aceptan sin frío si hay prueba de laboratorio
   de aw y pH (tabla B de 1-201.10). El arreglo de B1 deja la vía de 3-501.19 y la de la vitrina refrigerada. Si John
   prefiere no tocar el ejemplo, la alternativa es cambiar «custard danishes» por «fruit danishes» en el 02 y el B01, y
   dejar la custard danish en el 10 y el 12 con la nota de frío.
4. **M8 y m20 chocan con G1** (mismos anchos, combinaciones y áreas que el ES). Hay que decidir si se declara la
   desviación del 09 en la EN, como la D7 del 13, o si se arregla antes el ES en su v2.x y se regenera la EN.
5. **Matriz (M3, m10).** El SPEC fijó «mismo perfil que la ES». Si se cambian I8, I28 y N24, G4 tiene que aceptar esos
   valores como `POR_CELDA` / `VALORES_EN` declarados (hoy `VALORES_EN` está vacío).
