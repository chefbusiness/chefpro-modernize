# Pizzería Napolitana ES 1.0 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 25-oct-2026. SPEC: `SPEC.md` D5-D12 y D16. Dos tandas en paralelo, un redactor por tanda:
> **`piz_es_a`** = §1-5 (29 párrafos) · **`piz_es_b`** = §6-10 (32 párrafos). Las palabras objetivo de cada tanda
> están en su entrada. Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` =
> `{"<i>": "<párrafo>", …}` con TODOS los `i`.

## Qué es el producto

Plan de negocio de una **pizzería con horno de leña a la vista y sala de 50 plazas** (más una terraza de 24 de abril a
octubre) en una ciudad media española: local de 130 m² con salida de humos a cubierta, sin traspaso. Una **SL
unipersonal** con el titular de pizzaiolo jefe, un segundo pizzaiolo, ayudante, sala de dos servicios y refuerzo de fin
de semana. Carta corta de masa de fermentación larga; para llevar y a domicilio por **recogida** (sin comisión) y por
**plataforma** con su reparto, con techo (sin reparto propio). Abre en **septiembre**. Es producto NUEVO (no hay versión
anterior). Lo lee un pizzaiolo o un emprendedor que va a pedir un préstamo: tono cercano y profesional, **tuteo**,
español de España, frases claras, sin relleno ni superlativos vacíos.

## Reglas (las comprueba `python3 scripts/productos-digitales/plan-pizzeria/tandas_docx.py check --tanda <tanda>`)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel o de la calculadora va como token** `{ASI}`, copiado tal cual de `tokens` (el valor de al
   lado es sólo para que redactes con sentido). Ni importes, ni porcentajes, ni comensales, ticket o días del caso
   tecleados a mano: el Excel se puede recalcular y el documento tiene que seguirlo. Escribe la unidad que ya trae el
   token (no añadas «€» ni «%»). `{PAYBACK}` es texto («Más de 3 años»): no le añadas «años».
   `{MES_SALDO_MINIMO_NOMBRE}` es el nombre del mes. El driver se llama **comensales** (equivalentes: sala + para
   llevar + domicilio), nunca «cubiertos» ni «clientes».
3. **Cifras que SÍ puedes escribir**: artículos y normas; las búsquedas de DataForSEO y los datos de mercado de la pista
   §3 con su fuente; la carta del caso con IVA (pista §2); las cifras del **pliego** (`pliego_de_la_masa` de la
   entrada); los precios de equipo con fuente de la pista §6 y la variante eléctrica razonada; la producción de la pista
   §6 (75 y 140 pizzas, 19 y 12 kg, 150-200 por hora, 30-40 kg); la cuenta de reparto propio frente a plataforma de la
   pista §5 (0,35 jornada, unos 8.800 €, 2.500 €, 11.300 €, un 29 %, 60.000-70.000 €); el horario; la estructura del
   local (130 m², 50 + 24 plazas, 25 kW); las 80 tareas del checklist (12/15/14/13/13/13). Cualquier otra cifra, o es
   token o no va. El check avisa de cada cifra escrita que no está en su lista: revísalas una a una.
4. **Prohibido** (el check lo caza, SPEC D12): «freelance», «validado/a», «España 2026», «solopreneur», «tarifa plana»,
   «CNAE», «licencia de apertura» (la apertura es «licencia o declaración responsable según la ordenanza»), «carné de
   manipulador» (salvo para decir que ya no existe), RGSEAA salvo para decir que **sólo** aplica si suministras a otros
   negocios por encima del art. 3, el RD 895/2013 (el aceite en mesa es el **RD 760/2021, art. 7**), el RD 393/2007,
   un neto del «15-25 %», «versión 1.1/2.2» o «versión anterior»; restos de otros moldes: food truck, camión,
   ventanilla, generador, aparcamiento; del tapas bar: tapa(s), gastrobar, vermut, raciones, pinchos, tapeo, afterwork,
   salamandra, Rational; de la heladería: helado/heladería, mantecar, cubeta, sorbete, pasteurizar, granizado, horchata,
   tarrina. Harina, masa, levadura y amasado SÍ: son el oficio. «Campana» siempre «campana extractora».
5. **El nombre de la carta (SPEC D11, no negociable)**: lo que dice `nombre_de_la_carta` de la entrada, sin suavizarlo
   ni exagerarlo. El caso NO usa «pizza napolitana»: su carta dice «Margherita», «Marinara», «Diavola». La ETG es una
   opción (comunicación, autocontrol y verificación previa), nunca un sello del lector ni del producto: nunca
   «certificada», «ETG» o «verace» aplicado a la pizza del caso; la AVPN es privada y no sustituye la verificación;
   «estilo napolitano» en el rótulo = «consúltalo». El check avisa (no es error) de cada frase que afirme «es pizza
   napolitana»: revísalas.
6. **Legal**: sólo lo de la pista §9, con su cita. No añadas obligaciones, plazos ni importes legales que no estén ahí;
   lo que la pista dice «compruébalo», dilo así. Nunca cifras de ordenanzas de otras ciudades: el único ejemplo leído es
   Madrid (Ordenanza 4/2021, arts. 12, 23 y anexo I), y se presenta como ejemplo. La tasa de terraza del Excel es «pon
   la de tu ayuntamiento».
7. **Mes 1 = septiembre** (SPEC D7): el Excel numera la tesorería «Mes 1…12» y el Mes 1 es septiembre. Dilo así cuando
   hables de la tesorería, del saldo mínimo o de la estacionalidad («el Mes 4, diciembre»), y explica por qué: la rampa
   cae en meses medios y altos, la Navidad llega con clientela y enero y febrero (Meses 5 y 6) llegan con el fondo
   intacto.
8. **Leña, gas o eléctrico** (pista §6): la leña es la del caso y la única que cumple el pliego; el gas y el eléctrico,
   con lo que piden; la **variante eléctrica va SIN Excel**, razonada con las cifras de la pista. La leña es coste FIJO
   (se quema por hora de fuego, no por pizza).
9. **Plataforma frente a reparto propio** (pista §5): el caso vende por plataforma con techo y sin reparto propio; el
   reparto propio, siempre con contrato laboral, compensa sólo con volumen o con una zona corta y densa.
10. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida de
    longitud y registro, nunca su contenido. `gemela_formato_heladeria_es` es el párrafo de la Heladería ES 1.0 en la
    misma ranura: sirve para ver **cómo** se escribe una ranura con tokens y qué tipo de contenido le toca (resumen,
    mercado, equipo, cifras…), nunca su contenido (helado, obrador, fijos discontinuos, verano). El research
    (`F1-research-pizzeria.md` §0, §1, §2, §3, §4 y §6) es material de apoyo: si algo no está en la pista, no lo
    afirmes. La pista de la sección manda.
11. **Crecimiento y caja** (§8): el Excel sube los **comensales** con el mismo ticket y la plantilla con personas; la
    holgura de caja {HOLGURA_CAJA} es la del primer año, de carencia; desde el segundo hay que citar {HOLGURA_CAJA_A2} y
    {BE_COMENSALES_DIA_CAJA_A2}, y en el tercero {HOLGURA_CAJA_A3}: son los años que hay que vigilar. El neto honesto
    de una pizzería de barrio ronda el 9 %: no cites rentabilidades de internet.
12. Ortografía impecable (tildes, «¿», comillas «»), artículo delante de los porcentajes («un 10 %», «el 21 %»),
    espacio antes de «°C» y de «%», sin anglicismos innecesarios salvo los del oficio (pizzaiolo, fior di latte,
    cornicione, biga, poolish, delivery sólo si se explica). Nombres de pizza en italiano: «Margherita», «Marinara»,
    «Diavola», «Capricciosa».

## Cómo trabajar

Lee la entrada entera (secciones con su pista, nombre de la carta, pliego, tokens y párrafos), escribe la tanda completa
en `textos/<tanda>.json`, pasa `python3 scripts/productos-digitales/plan-pizzeria/tandas_docx.py check --tanda <tanda>`
desde la raíz del repo y corrige hasta 0 errores (los avisos de longitud, de cifra escrita o del nombre de la carta:
revísalos uno a uno). No toques ningún otro fichero. Devuelve: ruta, nº de párrafos y palabras, y la salida del check.
