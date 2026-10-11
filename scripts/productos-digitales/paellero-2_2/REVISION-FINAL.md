# Plan de Negocio Paellero para Eventos (ES) 2.2 — revisión adversarial final (1 ronda) · sesión Claude Code 2026-10-11

Rama `feat/paellero-2-2` @ `4cca389c` (sha256 Mac = VPS en los 11). Revisor: 1 Opus, solo lectura; xlsx y docx abiertos solo en el VPS.
**Veredicto: NO está listo todavía. Hay 0 BLOQUEANTE, 6 MAYOR y 16 MENOR.** Las fórmulas y las cifras del Excel están BIEN y `cifras_caso_es.json` no se mueve. Casi todo se arregla por TEXTO. Tres excepciones: M1 (VOCABULARIO + `ciclo.sh`), M2 (food cost de la carta y entradas de los ejemplos de la calculadora) y M4 (`datos_checklist.py` + `ciclo.sh`).

**Cifras recalculadas a mano** (cuadran al euro en Excel, json, docx §1/§8/§10 y landing; el correo no da cifras movibles):
- **Ventas.** Mezcla: 15×120×28 + 30×70×24 + 50×40×18 + 10×400×5 = 156.800 € / 9.900 raciones (94,3 raciones a 15,84 €). Excel: 105 × 94 × 16 = **157.920 €** (+0,7 %). Raciones 94 → 103,4 → 109,6; ventas 173.712 / 184.135 €.
- **Margen y resultado.** Mercancía 28 % × 85,19 % + 30 % × 14,81 % = 28,30 %. Variables 44.685 + 4.738 + 790 + 790 + 7.106 = 58.109 € → margen **99.811 € (63,2 %)**. Fijos 10.800 + 55.097 + 12.450 + 3.747 + 3.354 = 85.448 € → RAI 14.364 € → **neto 12.209 €** (7,7 %); después 15.593 € y 14.641 € (IS al 25 % el año 3).
- **Inversión.** 38.450 + 1.800 + 900 + 8 % × 19.200 = **42.686 €**; + fondo de maniobra 3 × 81.701 / 12 = 20.425 € → **63.111 €**; + IVA 21 % × 39.886 = 8.376 € → necesidad **71.487 €**. 20.000 + 51.600 deja +113 €.
- **Préstamo y DSCR.** Cuota 51.600 × 0,065 / (1 − 1,065⁻⁵) = **12.417 €** (el año 1 solo intereses, 3.354 €). DSCR año 2 (15.593 + 3.747 + 3.354) / 12.417 = **1,83**; año 3 = **1,70** (el mínimo).
- **Equilibrio.** Contable 85.448 / 0,63204 = 135.194 € = **81 raciones o 90 eventos**. Caja año 1: 129.265 € = **77 raciones o 86 eventos**, holgura **22,2 %**. Caja año 2: 153.097 € = **102 eventos**, holgura **13,5 %**. Año 3: holgura **13,3 %**, que no se cuenta en ningún sitio (m5).
- **Resto.** PVP con IVA 16 × 1,1004 = 17,61 €. Saldo mínimo **6.088 €** (mes 4). Payback 2 + 21.107 / 21.153 = **3,0 años**. Escenarios −16.950 € y +41.531 €.

**Calculadora** (evaluada con pycel; coincide con el cálculo a mano):
- **(A) Boda, particular**: 150 invitados, paellera de 120 cm, 7 €/invitado, 2 ayudantes, 500 € de alquileres, 40 km, margen 45 %. Salen 3 paelleras, 1 paellero, 18 kg de arroz, 45 L de caldo y un coste de 2.085,61 € → **25,50 € sin IVA / 28,05 € con IVA**; total 4.291,10 €, anticipo 1.287,33 €, margen calculado 45,5 %; cancelación 1.287,33 / 2.145,55 / 3.218,33 / 4.291,10 €.
- **(B) Fiesta popular, empresa**: 300 raciones, paellera de 150 cm, 2,25 €, margen 15 %. Salen 4 paelleras, 2 paelleros y un coste de 1.111,86 € → **4,50 €**; total 1.526,80 €, margen 17,6 %; cancelación 0 / 137,41 / 474,82 / 1.526,80 €.
- Los 3 ejemplos coinciden con F2-NOTAS §3.13, los desplegables están bien y la tabla de diámetros es la tabla 1 del manual.

**Integridad.** Los 11 ZIP están sanos y abren en openpyxl y python-docx. Xlsx en A4 (9/7/3/1 hojas); los 8 docx en A4 con docProps de 2026. Docx del plan: 11 H1, 7.811 palabras, 0 tokens. Checklist: 12/16/14/10/16/15 = 83 tareas. El manual es **idéntico en texto** al de `2d6cac44` (4.437 palabras, 14 H1, 10 tablas); la guía también, salvo A4 y propiedades.

**Fuentes abiertas** (BOE consolidado / API de datos abiertos):
1. **RD 919/2006, art. 2, def. h**: un único envase de GLP de menos de 15 kg conectado a un solo aparato móvil «no tendrá el carácter de instalación receptora». Conforme.
2. **Ley 43/2003, art. 44.3**: las CCAA regulan las actividades con riesgo de incendio «en montes y áreas colindantes». Conforme.
3. **LCSP**: art. 118.1, contrato menor de servicios por debajo de 15.000 € (conforme); art. 198.4, pago a 30 días desde la conformidad (conforme); **art. 198.3, abonos a cuenta solo por operaciones preparatorias y con garantía** (M3).
4. **Ley 7/2012, art. 7**: prohíbe pagar en efectivo operaciones «**igual o superior a 1.000 euros**» (m6).
5. **RD 1086/2020, art. 30** (redacción de la DF 2.12 del RD 1021/2022): 30.2, mantener a ≥ 63 °C, y 30.6, enfriar de 60 a 10 °C en menos de 2 h, conformes. **El 30.8.d-e exige comida testigo** (M4).

Nombres de los planes de incendios (anexo, landing, FAQ): correctos; 0 PATRICOVA, PIDOM o INFOCYL.

## MAYOR

- **M1 · El Excel dice que el Word está desfasado.** `Tesorería 12 meses!D31`: «El documento Word del pack sigue en la versión 1.1 y no lee esta celda». Es texto fijo del motor (`grupo_a.py:3766`), y el Word 2.2 sí cita el payback (p98, p111). **Está en los 7 planes de la línea A**, también en el Catering 2.2 LIVE: es transversal y lo decide el orquestador. **Arreglo** sin tocar el código común: en `contenido_plan_negocio_paellero_eventos/a.py`, añadir a `VOCABULARIO` `'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro'` → `'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro'`, más `'RESPECTO DE LA VERSIÓN 1.1'` → `'…1.2'` y `'v1.1'` → `'v1.2'` (Instrucciones!A33/B34: la versión anterior es la 1.2), y volver a pasar `ciclo.sh`.
- **M2 · El food cost de la carta y de la calculadora multiplica por 3-4 el del research y el del Excel.**
  - La carta (p11…p88) da 8,90 € a la Valenciana y llega a 16,50 €; la calculadora usa esos valores (C9, y en Ejemplos B9 = 8,90 y C9 = 8,50).
  - F1 §2 da 2,0-2,4 € para la Valenciana y 3,5-6 € para mixta y marisco. El Excel, con un 28 % sobre la comida, implica unos 6,70 € en una boda de 28 € con entrantes y unos 4,30 € en una fiesta privada de 18 €.
  - La carta p5 pone «fiestas privadas … 18 € por ración» junto a food costs de 7,60-16,50 € (del 42 % al 92 %).
  - **Arreglo (cifra; la que está mal es la carta):** escandallar de nuevo los 12 arroces con los rangos de F1 §2, rotulados «Food cost de la paella (sin entrantes)»; calculadora C9: «…la carta da el food cost de la paella sola: suma los entrantes»; Ejemplos B9 = 6,70 con B21 = 0,48 (sale 27,64 € → **28 €**, margen 48,7 %) y C9 ≈ 5,70 con B21 reajustado. Regenerar con `calculadora_pae_es.py` y pasar el autotest.
- **M3 · Se trata a los ayuntamientos como si adelantaran el 30 %.**
  - Dónde: calculadora C5 («ayuntamientos … cuentan como Empresa»); Ejemplos D5 (anticipo de 612,81 € y tramos B2B a un ayuntamiento); docx p112 («impago … de un ayuntamiento, con contrato y anticipo»); landing `plan-negocio-paellero-eventos.ts:150` y dashboard `:68` («B2B profesional (… agencias, ayuntamientos)»), cuando el contrato B2B es para una agencia que actúa por cuenta del cliente final (p46).
  - Choca con LCSP 198.3/198.4 y con Supuestos!C58, que lo dice bien.
  - **Arreglo:** C5: «…las comisiones de fiestas cuentan como Empresa; un ayuntamiento no adelanta el 30 %: compra por contrato menor y paga a 30 días desde la conformidad (art. 198.4 LCSP); pon 0 % de anticipo»; Ejemplos D23 = 0 y añadir «sin anticipo» en B58; docx p112: «…con el contrato menor firmado, la factura en su registro y la vigilancia del pago a 30 días»; landing y dashboard: «(wedding planners y agencias)».
- **M4 · Falta la comida testigo, que es obligatoria.** El RD 1086/2020, art. 30.8.d-e, la exige «para eventos, cuando esta sea la actividad principal de la empresa» y «por encargo para grupos o eventos de más de 40 personas»: 100 g a ≤ 4 °C (o ≤ −18 °C) durante 7 días (30.10). Hay 0 menciones en los 11 ficheros, aunque el kit cita ese mismo art. 30. **Arreglo:**
  - F2!E8, añadir: «Guarda una comida testigo de cada arroz (100 g, identificada y fechada, a 4 °C o menos o congelada, 7 días): obligatoria en eventos de más de 40 personas y si los eventos son tu actividad principal (art. 30.8 y 30.10 del RD 1086/2020)».
  - F6!E15: «…y la comida testigo».
  - Docx p104: «Y guarda una comida testigo de cada arroz durante 7 días (art. 30.8)».
- **M5 · La fiesta popular de las experiencias contradice al resto del kit.** `10-experiencias` p20 da un «Ticket por pax: 12-18 €» y p21 una «Paellera 200 cm»; el plan dice 5 €, la carta p5 de 3 a 6 €, la calculadora 4,50 €, y la paellera más grande del kit es de 150 cm. **Arreglo (`arreglos_d9.py`):** p20: «Ticket por ración: 3-6 € sin IVA para el ayuntamiento (volumen, una variedad); 12-18 € si es la comida de una peña con entrante y servicio»; p21: «…en paelleras de 120-150 cm, con gas o con leña donde esté permitido».
- **M6 · La guía del food truck atribuye a los eventos los márgenes de la 1.x.** Quedó fuera del barrido (`--excluir`).
  - p97: «Food cost 28-32 % (más bajo que paella eventos…)».
  - p98: «Margen neto 22-28 % (más bajo que paella eventos…)», que implica más del 28 % en eventos cuando el plan da un 7,7 %.
  - p66 y p100: «retorno / break-even 18-30 meses», sin fuente.
  - **Arreglo:** p97: «Food cost objetivo: 28-32 % (estimación del kit)»; p98: «Margen neto: calcúlalo con el plan financiero del kit; el caso de eventos deja un 7,7 % el primer año»; p66 y p100: «el plazo de recuperación depende de la inversión y del volumen: mídelo con el plan financiero»; p9 «99 % de la facturación» → «la mayoría de los eventos».

## MENOR

- **m1 · Docx p48 dice «redondeada con prudencia», y es falso para el precio.** → «La mezcla da 15,84 € y 94,3 raciones; el Excel redondea a 16 € y 94 (+0,7 %) y un ticket de 1.504 €».
- **m2 · Docx p80 cobra el anticipo después del D-21.** Contradice p69, p73, F6!D7 («Al reservar la fecha») y la cancelación a más de 60 días. → «Con la fecha reservada (presupuesto, contrato y anticipo del 30 %), a D-30 cierras el briefing…».
- **m3 · Cancelación B2B ambigua.** Docx p82 → «retención de nada, del 30 % o del 60 % del anticipo (este último, más 200 € de gestión) y el 100 % a menos de 15 días». Contrato p67: quitar «+ factura por gestión», como ya hacen la calculadora B53 e Instrucciones!A17.
- **m4 · Docx p87 explica la cobertura al revés.** → «compara todas las horas contratadas, incluidas las del titular a jornada completa, con solo las de evento (2 × 8 h × 105): por eso sale alta».
- **m5 · La holgura del año 3 (13,3 %, Punto Equilibrio!D24) es menor que la del año 2.** Docx p117 → «la caja del segundo y del tercer año (holguras del 13,5 % y del 13,3 %) es la que más hay que vigilar» (token opcional desde D24).
- **m6 · Efectivo «hasta 1.000 €».** La ley prohíbe operaciones de 1.000 € o más → «por debajo de 1.000 €». Cambiarlo en docx p82 y p103, contrato p23, F6!E7 y calculadora Instrucciones!A14.
- **m7 · FACe sin matices.** Ley 25/2013, art. 4: el research recoge la exención hasta 5.000 € y el kit la omite. En docx p107, F5!E18 y F6!E17 → «…en su punto general de entrada (FACe en la mayoría), salvo que exima las facturas de hasta 5.000 €».
- **m8 · Restos de otros moldes en el Excel** (arreglar por VOCABULARIO): Tesorería!O16 «el pan común y las harinas panificables, al superreducido (art. 91.Dos.1.1.º)» (quitar); Inversión!A31 «Obra, instalaciones y acondicionamiento» → «Furgoneta, rotulación e imprevistos»; Supuestos!A44 «obra e instalaciones» → «la furgoneta y su rotulación»; D27 y D32 «obra,» → «furgoneta,»; Supuestos!C51 «tres auxiliares» → «dos».
- **m9 · Mezcla comida/bebida desviada sin anotar.** Supuestos!B11 = 0,8519 (el 85/15 del catering), frente al 92/8 de SPEC D4 y del research §3; no está en F2-NOTAS §3 y mueve 0,1 pt la mercancía. O se anota como desviación 15, o B11 = 0,92 + `ciclo.sh`.
- **m10 · Calculadora.** C28 y A55: «manual técnico 1.2» → «del kit». Ejemplos B58: añadir «el kit trae una de 150 cm: alquila las demás o usa varias de 120 cm». C28: «regla conservadora: con ayudante, un paellero lleva cuatro (manual, tabla de 100 invitados)».
- **m11 · Checklist F5!E15 remite a un anexo que no existe.** «(anexo del plan de negocio)» → «(sección 5 del plan de negocio)».
- **m12 · Contratos.** B2B p71: RC de «1.000.000 €» frente a los 600.000 € del plan → «[600.000] € como mínimo». p7 y p45: «profesional autónomo», con el plan hecho para una SL → «en nombre propio o de [razón social], con NIF/CIF [ ]». p36: añadir «limitación, portabilidad y oposición». p54: «interés legal + 2 puntos» → «el interés de demora del art. 7 de la Ley 3/2004».
- **m13 · Estilo y versión.** Falta el artículo ante el porcentaje en p87 («del 198 %»), p97 («del 22,2 %», «del 13,5 %») y p111. «Versión 2.2 · septiembre 2026» aparece en docx p16, Excel A60, checklist A11 y calculadora A25, con una 1.2 fechada el 11-oct y la landing en «octubre» → «octubre 2026».
- **m14 · Referencias de precio y mercado.** Inversión!D9 da 61 € por la Garcima de 90 cm y el catálogo p19, 165 € → «61-165 € según acabado». Docx p54 y carta p5 hablan de «fichas de proveedores» de Bodas.net, cuando es una sola ficha → «la ficha de un proveedor (3-10 €, mínimo 300)».
- **m15 · Docx p64 afirma que la furgoneta «tiene que ser isoterma conforme al ATP».** El research no lo verificó (§❌). → «si el frío lo pone la caja, necesita ATP (RD 237/2000); con neveras y acumuladores, tu defensa es el registro de temperaturas».
- **m16 · Capa comercial, solo para John (no tocar sin él).** Antonio Rivas cita «el dossier B2B» (landing `:163`), y el kit no trae dossier; Laura Martín, con su «+40 %», repite la cifra sin fuente de las experiencias. Fuera de la capa comercial, por texto: experiencias p6 «aumenta el ticket medio 30-45 %» → «te deja cobrar la experiencia y no solo el plato»; p36 «julio (Hogueras Alicante)» → «junio (Fogueres de Sant Joan)».

**Conforme, sin cambios:** hubs ×7 (sin «60+», 35/65, Falles ni «validado»); email post-compra (`verify-purchase.ts` = config) y correo («Hola, colegas», sin cifras movibles); dashboard y changelog 2.2 (salvo lo de arriba); Marc Esteve, ya sin «4.200 EUR»; proveedores (88 en «Por verificar», 0 «Validado»); fuerza mayor con plan B en el B2C y en el B2B y no desistimiento (art. 103.l); IVA al 10 % con servicio y al 21 % para el alcohol de la paella para recoger; fijos discontinuos (sin «freelance» ni «carné», salvo «ya no existe»); anexo con 8 comunidades. Sin restos de food truck ni de catering en el docx: «roadmap food truck» es el nombre de la guía y «Kit de Tareas: Catering / Eventos», una venta cruzada.
