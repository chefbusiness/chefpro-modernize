# Cafetería Móvil para Eventos ES 1.0 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 28-oct-2026. SPEC: `SPEC.md` D5-D16. Dos tandas en paralelo, un redactor por tanda:
> **`caf_es_a`** = §1-5 (29 párrafos) · **`caf_es_b`** = §6-10 (32 párrafos). Las palabras objetivo de cada tanda
> están en su entrada. Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` =
> `{"<i>": "<párrafo>", …}` con TODOS los `i`.

## Qué es el producto

Plan de negocio de una **barra de café de especialidad para eventos** que va en **furgoneta** con una barra-carro, una
cafetera de dos grupos, molinos y su propia energía, y que trabaja **por encargo** para bodas, empresas, congresos y
celebraciones privadas, con unas pocas **jornadas de venta directa** en mercados y festivales con canon del organizador.
**No es venta diaria en la calle.** Una **SL unipersonal** con el titular de barista, un camarero/a fijo discontinuo y
una pequeña bolsa de suplencias y refuerzo; un **almacén base** (nave o garaje con fregadero). Arranca en **marzo**.
Es producto NUEVO (no hay versión anterior). Lo lee un barista o un emprendedor que va a pedir un préstamo: tono
cercano y profesional, **tuteo**, español de España, frases claras, sin relleno ni superlativos vacíos.

## Reglas (las comprueba `python3 scripts/productos-digitales/plan-cafeteria-movil/tandas_docx.py check --tanda <tanda>`)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel, de la calculadora o de la tabla de escalado va como token** `{ASI}`, copiado tal cual de
   `tokens` (el valor de al lado es sólo para que redactes con sentido). Ni importes, ni porcentajes, ni invitados,
   precios o eventos del caso tecleados a mano: el Excel se puede recalcular y el documento tiene que seguirlo. Escribe
   la unidad que ya trae el token (no añadas «€» ni «%»); los tokens `TE…_KG_CAFE`, `TE…_L_LECHE`, `TE…_KW` y similares
   van sin unidad: escríbela tú detrás («{TE100_KG_CAFE} kg»). `{MES_SALDO_MINIMO_NOMBRE}` y `{TE50_TOMA}` son texto.
   El driver se llama **invitados** (en la venta directa, tazas), nunca «cubiertos», «comensales» ni «clientes al día».
3. **Payback** (lección M1 de la pizzería): el Excel marca `{PAYBACK}` («Más de 3 años»). Cítalo entre comillas como
   lo marca el Excel en la fila «Payback del proyecto (años), antes de la deuda», o en mitad de frase con
   `{PAYBACK_TEXTO}`; nunca «Payback» con mayúscula en mitad de frase sin comillas, y nunca le añadas «años».
4. **Equilibrio con dos lecturas, cada una con su nombre** (lección M1 de la finca): «{BE_INVITADOS_EVENTO} invitados
   por evento con los eventos del caso» **o** «{BE_EVENTOS_ANO} eventos del tamaño medio»; nunca mezcles las dos en la
   misma frase. La holgura de caja `{HOLGURA_CAJA}` es la del **primer año** (carencia); los años 2 y 3 se citan
   aparte con `{HOLGURA_CAJA_A2}` / `{BE_EVENTOS_CAJA_A2}` y `{HOLGURA_CAJA_A3}` / `{BE_EVENTOS_CAJA_A3}` (lección M2 de
   la finca). El crecimiento: suben los **invitados por evento** con los mismos eventos (en euros, como
   `{EVENTOS_EQUIVALENTES_A2}` y `{EVENTOS_EQUIVALENTES_A3}` eventos del tamaño del año 1) y la plantilla con personas.
5. **Cifras que SÍ puedes escribir**: artículos y normas; las búsquedas de DataForSEO y los precios de Bodas.net de la
   pista §3 con su fuente y fecha (siempre como «desde» de escaparate, nunca como tarifa de mercado); la mezcla del caso
   de la pista §2 (30/40/22/25/12 servicios, 120/80/300/50/250 invitados, 9,00/8,00/4,50/9,50/3,00 €); las tres
   configuraciones (unos 12.000-15.000 €, la del caso por token, unos 55.000-65.000 €); la electricidad (2,4-4,5 kW,
   16 A, 3,5 kW, 5 kVA); bebidas por invitado y capacidad de la pista §6 (1,0; 1,3-1,5; 1,5-1,8; 2,0-2,5; 50-60 por
   hora); los porcentajes de cobro y cancelación (D16); las 80 tareas del checklist (12/16/14/10/14/14); la bio (29
   años). Cualquier otra cifra, o es token o no va. El check avisa de cada cifra escrita que no está en su lista:
   revísalas una a una.
6. **Cobro y cancelación (SPEC D16, no negociable)**: lo que dice `cobro_y_cancelacion` de la entrada, tal cual:
   particular 30 % al firmar + 70 % siete días antes; empresa 30 % + 70 % a 30 días de la factura; feria en el acto;
   cuatro tramos «de X a menos de Y» (particular 60/30/7 días; empresa 30/15/7) que retienen el 10, 30, 60 o 100 %
   **menos los costes que la cafetería se ahorra**, recíprocos. La señal es **a cuenta del precio** (nunca «arras»).
   Es lo mismo que dicen la calculadora y el contrato del kit.
7. **Electricidad (SPEC D11)**: lo que dice `electricidad` de la entrada, tal cual. Nunca «enchufa en cualquier finca».
8. **Prohibido** (el check lo caza, SPEC D12): «freelance», «validado/a», «España 2026», «solopreneur», «tarifa plana»,
   «CNAE», «licencia de apertura», «carné de manipulador» (salvo para decir que ya no existe; el carné B del remolque
   sí), RGSEAA salvo para decir que **sólo** aplica si vendes a otros negocios, «versión 1.1/2.2» o «versión
   anterior», «de 22 %» (con artículo: «del 22 %», «un 22 %»), «Comunitat», «15 años» (la bio dice «quince años»),
   «demanda creciente», «sin licencias», «sin registro sanitario», «tarifa de mercado»; y los 12 del research §8:
   comida testigo que «no aplica nunca», vaso compostable «sin plástico» o «exento» de la Ley 7/2022, ofrecer pajitas o
   agitadores de plástico, «cualquier enchufe», inversiones «desde 3.000 €» o «una cafetera doméstica sirve»,
   facturación garantizada o «recuperas la inversión en X meses», el servicio al 21 %, el Ape por autovía, alcohol en
   la carta (cerveza, carajillos, espresso martini: no los menciones). Restos de otros moldes: food truck (sólo vale
   la búsqueda «food truck cafetería» entre comillas españolas del §3), camión, ventanilla, parrilla, asado, brasa,
   carbón, carne, cocina de apoyo, ATP; y las palabras del motor: «en sala», «el local», «ticket» (escribe «tique»
   para el recibo), «delivery», «cubierto», «comensal». **Bollería, leche, generador, furgoneta, remolque y
   aparcamiento SÍ**: son el oficio.
9. **Legal**: sólo lo de la pista §9, con su cita. No añadas obligaciones, plazos ni importes legales que no estén ahí;
   lo que la pista dice «compruébalo», dilo así y sin cifra. La comida testigo, con su matiz exacto: con salado, sí y en
   cada evento; las bebidas y la bollería servida tal cual, fuera **según nuestra lectura, sin criterio oficial:
   confírmalo con tu autoridad sanitaria**. «Café de especialidad» sólo con la ficha del tostador (80 puntos SCA o
   más); nada de torrefacto. Vasos: loza por defecto en bodas y empresa.
10. **Mes 1 = marzo** (SPEC D7): el Excel numera la tesorería «Mes 1…12» y el Mes 1 es marzo. Dilo así cuando hables de
    la tesorería, del saldo mínimo o de la estacionalidad («el Mes 6, agosto»), y explica por qué: el café se reserva
    con uno a seis meses de antelación, se arranca en primavera con la empresa y las comuniones, y enero y febrero (los
    meses más flojos) llegan con la caja de la temporada.
11. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida de
    longitud y registro, nunca su contenido. `gemela_formato_finca_es` (Finca 1.0, línea de eventos) enseña **cómo** se
    escribe una ranura con tokens y qué tipo de contenido le toca (resumen, mercado, equipo, cifras…); y
    `gemela_oficio_parrillero_es` (Parrillero 2.2) cómo se cuenta un oficio itinerante con furgoneta, base y fijos
    discontinuos. Nunca su contenido (finca, catering, carne, brasa). El research (`F1-research-cafeteria-movil.md` §0-§8)
    es material de apoyo: si algo no está en la pista, no lo afirmes. La pista de la sección manda.
12. **Bio** (SPEC D15): en la última ranura del §10, una frase que diga que el plan lo ha preparado ChefBusiness
    Consultoría Gastronómica, con 29 años en alta hostelería y quince en consultoría (sin nombres propios). Venta
    cruzada, sin precios: el Kit de Tareas Recurrentes: Cafetería, el Kit de Escandallos Pro y el Pack Plantillas APPCC
    (ya van fijos al pie del documento; puedes nombrarlos una vez en el §10).
13. Ortografía impecable (tildes, «¿», comillas «»), artículo delante de los porcentajes («un 10 %», «el 21 %»),
    espacio antes de «°C», «%», «kW» y «€», sin anglicismos innecesarios salvo los del oficio (barista, latte art, flat
    white, coffee cart, coffee truck, wedding planner, coffee break, explicados la primera vez). Nombres de bebida en
    minúscula salvo al empezar frase.

## Cómo trabajar

Lee la entrada entera (secciones con su pista, cobro y cancelación, electricidad, tokens y párrafos), escribe la tanda
completa en `textos/<tanda>.json`, pasa `python3 scripts/productos-digitales/plan-cafeteria-movil/tandas_docx.py check
--tanda <tanda>` desde la raíz del repo y corrige hasta 0 errores (los avisos de longitud y de cifra escrita: revísalos
uno a uno). No toques ningún otro fichero (en `textos/` hay un `contrato_es.json` de otro agente: ni lo abras). Devuelve:
ruta, nº de párrafos y palabras, y la salida del check.
