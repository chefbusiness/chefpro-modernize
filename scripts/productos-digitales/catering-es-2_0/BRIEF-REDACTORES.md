# Catering ES 2.0 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 11-oct-2026. SPEC: `SPEC-2_0.md` D8. Dos tandas en paralelo, un redactor por tanda:
> **`cat_es_a`** = §1-5 (29 párrafos, ≈ 2.950 palabras) · **`cat_es_b`** = §6-10 (32 párrafos, ≈ 3.770 palabras).
> Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` = `{"<i>": "<párrafo>", …}` con TODOS los `i`.

## Qué es el producto

Plan de negocio de un **catering temático multi-concepto para eventos** en España: estaciones de cocinas del mundo
en directo (show cooking), sin restaurante, con **cocina central compartida y autorizada**, furgoneta frigorífica y
una plantilla de cuatro fijos más una bolsa de **fijos discontinuos**. Dos motores: empresas entre semana (65 % de
los eventos) y particulares el fin de semana. Lo lee un chef o un emprendedor que va a pedir un préstamo: tono
cercano y profesional, **tuteo**, español de España, frases claras, sin relleno ni superlativos vacíos.

## Reglas (las comprueba `python3 tandas_docx.py check --tanda <tanda>`)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel va como token** `{ASI}`, copiado tal cual de `tokens` (el valor de al lado es sólo para que
   redactes con sentido). Ni importes, ni porcentajes, ni eventos o invitados del caso tecleados a mano: el Excel se
   puede recalcular y el documento tiene que seguirlo. Escribe la unidad que ya trae el token (no añadas «€» ni «%»).
3. **Cifras que SÍ puedes escribir**: artículos y normas; la política comercial de los contratos (40 % de anticipo,
   21/7 días, 48 h, 40/30/30, 28/14/7 días, 60 días de pago máximo); IVA 10 % y 21 %; temperaturas del APPCC; la
   mezcla de eventos de la pista §2; las búsquedas de DataForSEO y los datos de Bodas.net de la pista §3; las 82
   tareas del checklist; 600.000 € de RC; 150 invitados de menaje. Cualquier otra cifra, o es token o no va.
4. **Prohibido** (el check lo caza): «freelance», «validado/a», «España 2026», food truck, camión, ventanilla,
   generador; las cifras de la versión anterior (173 eventos, 2.200/4.500 €, 10.560, 8.520/21.410/54.440, 603.700,
   846.7xx, «14 eventos/mes», 5.500, 11.500, 4.585/4.885 M€, 38/58/73 %); «sin licencia de actividad»; «tarifa
   plana»; RGSEAA salvo para decir que **sólo** aplica si se suministra a otros establecimientos.
5. **Legal**: sólo lo de la pista §9 (verificado en el BOE), con su cita. No añadas obligaciones, plazos ni importes
   legales que no estén ahí. Nada de EE. UU. (sales tax, service charge, W-2, commissary, permits, $).
6. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida
   de longitud y registro, nunca su contenido. `gemela_en_catering` es el párrafo del catering EE. UU. en la misma
   ranura: sirve de **argumento** (qué toca contar ahí), adaptado a España. El `material_catering_1x` aporta el
   concepto, la operativa en 6 fases y los riesgos; **sus cifras están prohibidas**. La pista de la sección manda.
7. Identidad intacta: estaciones temáticas en directo y dietas especiales al mismo nivel. El personal de eventos es
   **fijo discontinuo** (art. 16 ET), nunca autónomos dependientes. Los anticipos no están en el Excel: la caja real
   es algo mejor que la de la hoja de Tesorería (dilo en §8).
8. Ortografía impecable (tildes, «¿», comillas «»), sin anglicismos innecesarios salvo los del oficio (show cooking,
   coffee break, drop-off, wedding planner, briefing).

## Cómo trabajar

Lee la entrada entera (secciones con su pista, tokens y párrafos), escribe la tanda completa en `textos/<tanda>.json`,
pasa `python3 scripts/productos-digitales/catering-es-2_0/tandas_docx.py check --tanda <tanda>` desde la raíz del
repo y corrige hasta 0 errores (los avisos de longitud o de cifra escrita: revísalos uno a uno). No toques ningún
otro fichero. Devuelve: ruta, nº de párrafos y palabras, y la salida del check.
