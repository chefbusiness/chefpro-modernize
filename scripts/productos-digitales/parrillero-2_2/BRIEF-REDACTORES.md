# Parrillero / Asador ES 2.2 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 12-oct-2026. SPEC: `SPEC-2_2.md` D11. Dos tandas en paralelo, un redactor por tanda:
> **`par_es_a`** = §1-5 (29 párrafos) · **`par_es_b`** = §6-10 (32 párrafos). Las palabras objetivo de cada tanda
> están en su entrada. Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` =
> `{"<i>": "<párrafo>", …}` con TODOS los `i`.

## Qué es el producto

Plan de negocio de un **parrillero / asador para eventos** en España: parrilla y asado cocinados **en directo** en el
evento, con carbón y leña, show de fuego y un **plan B de gas** para cuando una alerta de incendios prohíbe la brasa;
multi-concepto (asado argentino, cordero a la cruz, BBQ texano, rodizio, criollo-castellano, mediterránea, llanera…),
sin local propio. Una **SL unipersonal** con una **cocina de apoyo compartida y autorizada** para marinados,
salmueras y porcionado, una furgoneta frigorífica con ATP, un remolque-parrilla con cruz, el parrillero titular, un
segundo parrillero y dos auxiliares **fijos discontinuos**. Cuatro clientes: bodas, empresas, celebraciones privadas
y **fiestas o ferias** por encargo de ayuntamientos y comisiones. Lo lee un parrillero o un emprendedor que va a pedir
un préstamo: tono cercano y profesional, **tuteo**, español de España, frases claras, sin relleno ni superlativos vacíos.

## Reglas (las comprueba `python3 tandas_docx.py check --tanda <tanda>`)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel va como token** `{ASI}`, copiado tal cual de `tokens` (el valor de al lado es sólo para que
   redactes con sentido). Ni importes, ni porcentajes, ni eventos o invitados del caso tecleados a mano: el Excel se
   puede recalcular y el documento tiene que seguirlo. Escribe la unidad que ya trae el token (no añadas «€» ni «%»).
   `{PAYBACK}` es texto («Más de 3 años»): no le añadas «años».
3. **Cifras que SÍ puedes escribir**: artículos y normas; la política comercial de los contratos (30 % de señal, 40 %
   siete días antes, 30 % en las 48 horas siguientes; 30 % y 70 % a 30 días para empresas; los tramos de cancelación
   de la pista §6 y el 10 % si cancela el parrillero); IVA 10 % y 21 %; las temperaturas de la carne (7, 3, 4 y 2 °C;
   70 y 74 °C; 63 °C) y la comida testigo (100 g, 7 días, más de 40 personas); la tabla de escalado de la pista §6
   (gramos de carne, parrillas, parrilleros, carbón); los límites del gas (15 kg, 35 kg, 333 kg), del efectivo
   (1.000 €), del contrato menor (15.000 €) y de la exención de FACe (5.000 €); la mezcla de eventos de la pista §2;
   las búsquedas de DataForSEO y los precios de referencia con fuente de la pista §3; las 83 tareas del checklist;
   600.000 € de RC; 3 m de distancia a carpas; 30 meses del chuletón con vértebra. Cualquier otra cifra, o es token
   o no va.
4. **Prohibido** (el check lo caza): «freelance», «validado/a», «España 2026», «sin licencia», «tarifa plana»,
   «solopreneur», «carné de manipulador» (salvo para decir que ya no existe), «CNAE», «cocina central», «estaciones
   temáticas», «drop-off», camión, ventanilla, generador; «food truck» salvo en el nombre de la guía «roadmap food
   truck»; paella, socarrat y arroz (restos de la gemela); PATRICOVA, INFOCYL, PIDOM, «excepción cultural»; la
   retención del 7 %/15 % (lo correcto es lo contrario: las facturas **no** llevan retención); las cifras de la
   versión anterior (3.500, 4.356, 10.406, 21.036, 57.200, 130.800, 237.000, 240.000, 21.370, 53.730, 97.140, 8.830,
   2.800, 5,44, «8-10 eventos», 37 %, 41 %, 55-60 %, 58 %, 80 €/mes, 80-120 €, 320-360, «4-7 veces», 1.800-2.100,
   80-120 M, 165.000, «ordenanza 4/2021»); RGSEAA salvo para decir que **sólo** aplica si suministras a otros
   establecimientos.
5. **Legal**: sólo lo de la pista §9, con su cita. No añadas obligaciones, plazos ni importes legales que no estén ahí.
   AESAN (70/74 °C) es una **recomendación**: dilo así. El anexo por comunidades autónomas lo pone el ensamblador: en el
   texto basta con remitir a él. Nunca digas que «con la licencia de la finca se puede» hacer fuego en zona forestal.
6. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida
   de longitud y registro, nunca su contenido. `gemela_paellero_es` es el párrafo del Paellero ES 2.2 en la misma
   ranura: sirve de **argumento** (qué toca contar ahí y cómo), adaptado al parrillero; no copies sus cifras, sus
   paellas ni su gas como combustible principal (aquí el gas es sólo el plan B). El `material_parrillero_1_1` aporta
   el concepto, los clientes, la operativa del evento (D-14 a D+7) y los riesgos; **sus cifras están prohibidas**.
   La pista de la sección manda.
7. Identidad intacta: el fuego y el corte en directo, la carta de 12 cortes y las 10 experiencias. El personal de
   eventos es **fijo discontinuo** (art. 16 ET), nunca autónomos que te facturan. La media de {PRECIO_INVITADO} por
   invitado es de la mezcla y baja por las fiestas: dilo así, no la presentes como el precio de una boda. El show
   cooking por jornada en un restaurante es una línea extra **sin cifras**: no está en el caso.
8. **Crecimiento y caja** (§8, lo cazaron las revisiones del catering y del paellero): el Excel sube los **invitados
   por evento** con los mismos eventos y el mismo precio; la holgura de caja {HOLGURA_CAJA} es la del primer año, de
   carencia; desde el segundo hay que citar {HOLGURA_CAJA_A2} y {BE_EVENTOS_CAJA_A2}, y en el tercero
   {HOLGURA_CAJA_A3}: son los años que hay que vigilar. Las señales no están en el Excel: la caja real es algo mejor
   que la de la hoja de Tesorería.
9. Ortografía impecable (tildes, «¿», comillas «»), artículo delante de los porcentajes («un 30 %», «el 10 %»), sin
   anglicismos innecesarios salvo los del oficio (show cooking, wedding planner, briefing, team building, BBQ).

## Cómo trabajar

Lee la entrada entera (secciones con su pista, tokens y párrafos), escribe la tanda completa en `textos/<tanda>.json`,
pasa `python3 scripts/productos-digitales/parrillero-2_2/tandas_docx.py check --tanda <tanda>` desde la raíz del
repo y corrige hasta 0 errores (los avisos de longitud o de cifra escrita: revísalos uno a uno). No toques ningún
otro fichero. Devuelve: ruta, nº de párrafos y palabras, y la salida del check.
