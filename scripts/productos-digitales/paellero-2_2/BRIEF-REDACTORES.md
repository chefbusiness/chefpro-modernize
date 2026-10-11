# Paellero ES 2.2 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 11-oct-2026. SPEC: `SPEC-2_2.md` D11. Dos tandas en paralelo, un redactor por tanda:
> **`pae_es_a`** = §1-5 (29 párrafos) · **`pae_es_b`** = §6-10 (32 párrafos). Las palabras objetivo de cada tanda
> están en su entrada. Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` =
> `{"<i>": "<párrafo>", …}` con TODOS los `i`.

## Qué es el producto

Plan de negocio de un **paellero para eventos** en España: paella y arroces cocinados **en directo** en el evento
(show cooking, con gas y, donde se pueda, con leña), sin local propio. Una **SL unipersonal** con una **cocina de apoyo
compartida y autorizada** para caldos y preparación, una furgoneta isoterma con ATP, el paellero titular, un ayudante y
dos auxiliares **fijos discontinuos**. Cuatro clientes: bodas, empresas, fiestas privadas y **fiestas populares**
(ayuntamientos y comisiones). Lo lee un paellero o un emprendedor que va a pedir un préstamo: tono cercano y
profesional, **tuteo**, español de España, frases claras, sin relleno ni superlativos vacíos.

## Reglas (las comprueba `python3 tandas_docx.py check --tanda <tanda>`)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel va como token** `{ASI}`, copiado tal cual de `tokens` (el valor de al lado es sólo para que
   redactes con sentido). Ni importes, ni porcentajes, ni eventos o raciones del caso tecleados a mano: el Excel se
   puede recalcular y el documento tiene que seguirlo. Escribe la unidad que ya trae el token (no añadas «€» ni «%»).
3. **Cifras que SÍ puedes escribir**: artículos y normas; la política comercial de los contratos (30 % al firmar, 70 %
   el día del evento o a 30 días de la factura, tramos de cancelación de 60, 30 y 15 días y 72 horas, 200 € de
   gestión); IVA 10 % y 21 %; 63 °C; las raciones por paellera y los 100 g de arroz del manual; los límites del gas
   (15 kg, 35 kg, 333 kg) y del efectivo (1.000 €); la mezcla de eventos de la pista §2; las búsquedas de DataForSEO
   y los precios de referencia con fuente de la pista §3; las 83 tareas del checklist; 600.000 € de RC.
   Cualquier otra cifra, o es token o no va.
4. **Prohibido** (el check lo caza): «freelance», «validado/a», «España 2026», «sin licencia», «tarifa plana»,
   «solopreneur», «carné de manipulador» (salvo para decir que ya no existe), «cocina central», «estaciones
   temáticas», «drop-off», camión, ventanilla, generador; «food truck» salvo en el nombre de la guía «roadmap food
   truck»; PATRICOVA, INFOCYL, PIDOM, «excepción cultural»; las cifras de la versión anterior (3.500, 3.790, 8.500,
   9.670, 23.110, 214.950, 215.000-245.000, 47.000-62.000, 109.822, «18-22 eventos», 10,18, 51 %, 80 €/mes,
   120 €/jornada, «4-7 veces», 3.200 M€); RGSEAA salvo para decir que **sólo** aplica si suministras a otros
   establecimientos.
5. **Legal**: sólo lo de la pista §9, con su cita. No añadas obligaciones, plazos ni importes legales que no estén ahí.
   El anexo por comunidades autónomas lo pone el ensamblador: en el texto basta con remitir a él.
6. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida
   de longitud y registro, nunca su contenido. `gemela_catering_es` es el párrafo del Catering ES 2.2 en la misma
   ranura: sirve de **argumento** (qué toca contar ahí y cómo), adaptado al paellero; no copies sus cifras ni sus
   estaciones temáticas. El `material_paellero_1_2` aporta el concepto, la operativa del evento (D-30 a D+15) y los
   riesgos; **sus cifras están prohibidas**. La pista de la sección manda.
7. Identidad intacta: el ritual de la paella en directo, la carta de 12 arroces y las 10 experiencias. El personal de
   eventos es **fijo discontinuo** (art. 16 ET), nunca autónomos que te facturan. La media de {PRECIO_INVITADO} por
   ración es de la mezcla y baja por las fiestas populares: dilo así, no la presentes como el precio de una boda.
8. **Crecimiento y caja** (§8, lo cazó la revisión del catering): el Excel sube las **raciones por evento** con los
   mismos eventos y el mismo precio; la holgura de caja {HOLGURA_CAJA} es la del primer año, de carencia, y desde el
   segundo hay que citar {HOLGURA_CAJA_A2} y {BE_EVENTOS_CAJA_A2}. Los anticipos no están en el Excel: la caja real
   es algo mejor que la de la hoja de Tesorería.
9. Ortografía impecable (tildes, «¿», comillas «»), sin anglicismos innecesarios salvo los del oficio (show cooking,
   wedding planner, briefing, team building).

## Cómo trabajar

Lee la entrada entera (secciones con su pista, tokens y párrafos), escribe la tanda completa en `textos/<tanda>.json`,
pasa `python3 scripts/productos-digitales/paellero-2_2/tandas_docx.py check --tanda <tanda>` desde la raíz del
repo y corrige hasta 0 errores (los avisos de longitud o de cifra escrita: revísalos uno a uno). No toques ningún
otro fichero. Devuelve: ruta, nº de párrafos y palabras, y la salida del check.
