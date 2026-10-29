# Pollería y Asador de Pollos ES 1.0 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 29-oct-2026. Camino: `F1-camino.md` §2 (SPEC firmada) y §4. Dos tandas en paralelo, un redactor
> por tanda: **`pol_es_a`** = §1-5 (29 párrafos) · **`pol_es_b`** = §6-10 (32 párrafos). Las palabras objetivo de cada
> tanda están en su entrada. Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` =
> `{"<i>": "<párrafo>", …}` con TODOS los `i`.

## Qué es el producto

Plan de negocio de una **pollería-asador de barrio** con un **asador de pollos de gas de doce espadas** a la vista,
**mostrador con vitrina caliente y encargos** y una **sala de 20 plazas** (16 en mesa y 4 en barra), en un barrio
residencial de una ciudad media española: local de 80 m² con salida de humos a cubierta, sin traspaso. Una **SL
unipersonal** con el titular de maestro asador, un segundo asador-cocinero, mostrador, sala y refuerzo de fin de
semana. Vende **para llevar** en el mostrador y por **encargo** (sin comisión), por **plataforma** con su reparto (con
techo, sin reparto propio) y en **sala**. Abre en **enero** (el Mes 1 del Excel es enero, en el orden del calendario) y
el **verano es el pico**. Es producto NUEVO (no hay versión anterior). Lo lee un asador o un emprendedor que va a pedir un
préstamo: tono cercano y profesional, **tuteo**, español de España, frases claras, sin relleno ni superlativos vacíos.

## Reglas (las comprueba `python3 scripts/productos-digitales/plan-polleria/tandas_docx.py check --tanda <tanda>`)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel o de la calculadora va como token** `{ASI}`, copiado tal cual de `tokens` (el valor de al
   lado es sólo para que redactes con sentido). Ni importes, ni porcentajes, ni pedidos, ticket o días del caso
   tecleados a mano: el Excel se puede recalcular y el documento tiene que seguirlo. Escribe la unidad que ya trae el
   token (no añadas «€» ni «%»). **`{PAYBACK}` hoy es el texto «Más de 3 años» y puede volver a ser una cifra sin
   unidad**: la frase tiene que leer bien con los dos («El payback antes de la deuda, en años, … «{PAYBACK}» con el fondo
   de maniobra dentro y «{PAYBACK_CAPEX}» sin él»); nunca «años» detrás del token ni «no se recupera en tres años».
   `{MES_SALDO_MINIMO_NOMBRE}` es el nombre del mes. El driver se llama **pedidos** (un pedido de mostrador o un
   encargo, uno de plataforma o un cliente sentado en la sala), nunca «cubiertos», «comensales» ni «tickets».
3. **Cifras que SÍ puedes escribir**: artículos y normas, y las que traen las pistas y la jerga (las búsquedas de
   DataForSEO y los precios en carta de la pista §3 con su fuente; la carta del caso con IVA; el mercado de Interempresas;
   el pollo y el asador de la pista §6 —1,45 kg, 3,05 € el kilo, 0,13 €, 1,10 kg, 11,73 €, 106 y 122 pollos el domingo,
   90 minutos, 5 por espada, 120 con ocho espadas—; los precios de equipo con fuente; la cuenta del reparto propio de la
   pista §5; la sensibilidad del pollo de la pista §8; el horario; la estructura del local; las 80 tareas del checklist).
   Cualquier otra cifra, o es token o no va. El check avisa de cada cifra escrita que no está en su lista: revísalas una
   a una.
4. **Prohibido** (el check lo caza): «freelance», «validado/a», «España 2026», «solopreneur», «tarifa plana», «CNAE»,
   «licencia de apertura» (la apertura es «licencia o declaración responsable según la ordenanza»), «carné de
   manipulador» (salvo para decir que ya no existe), RGSEAA salvo para decir que **sólo** aplica si suministras a otros
   negocios por encima del art. 3, el RD 895/2013, el RD 393/2007, un neto del «15-25 %», «versión 1.1/2.2» o «versión
   anterior»; restos de otros moldes: food truck, camión, ventanilla, generador, aparcamiento (di «cómodo para parar el
   coche»); del tapas bar: tapa(s) —tampoco la de un envase: di «cierre»—, gastrobar, vermut, pinchos, salamandra,
   Rational; de la heladería: helado, sorbete, granizado, horchata, manteca, cubeta; de la pizzería: pizza, napolitana,
   levadura, mozzarella, cúpula, AVPN; **de la taquería**: taquería, trompo, taco(s), comal, pastor, gringa, nixtamal,
   tortilla de maíz o de harina, tortillero, mezcal, tequila, aguas frescas, carnitas, suadero, cochinita, guacamole,
   salsa macha. **SÍ son oficio**: leña y horno (la brasa peruana), raciones (el 677.9 lo dice), tarrina, el pan común
   (va al 4 %) y la **tortilla de patatas** del asador. «Campana» siempre «campana extractora».
5. **El art. 30** (error del check si falla): las temperaturas de las comidas preparadas (63 °C, 4/8 °C, de 60 a 10 °C
   en menos de 2 horas, 74 °C 15 segundos) son del **art. 30 del RD 1086/2020, en la redacción del RD 1021/2022**:
   escribe siempre «RD 1086/2020» junto a «art. 30» y nunca lo atribuyas al RD 1021/2022 a secas. Lo del **RD 1021/2022**
   es el art. 3 (venta marginal), el 4.1 (aves y preparados de carne a 4 °C, despojos a 3 °C, vegetal cortado a 4 °C),
   el 4.2 (etiqueta), el 4.3 (transporte), el **9.2-9.3 (ovoproducto)** y el 11 («elaboración propia»).
6. **Avisos que se revisan uno a uno** (no son error): «sin gluten» sólo para decir que **no se promete** con freidora
   compartida; «tortilla» sólo la de patatas; «642.5» siempre diciendo que **no ampara asar**; **nunca «obligatorio» junto
   a 74 °C**: no hay temperatura legal de cocción del pollo (74 °C en el muslo es el criterio del APPCC del caso); «broaster»
   sólo para decir que es pollo **frito** a presión; «auténtico» nunca como promesa; el registro de jornada es obligatorio,
   pero **no** digas que la ley lo exige «digital».
7. **Legal**: sólo lo de la pista §9, con su cita. No añadas obligaciones, plazos ni importes legales que no estén ahí;
   lo que la pista dice «compruébalo», dilo así. Nunca cifras de ordenanzas de otras ciudades: el único ejemplo leído es
   Madrid (Ordenanza 4/2021, arts. 12, 23 y anexo I), y se presenta como ejemplo. El marco legal es el **español**: para
   Perú, México y Latinoamérica, la guía de equivalencias adapta los términos, no los trámites.
8. **Mes 1 = enero, el verano arriba**: el Excel numera la tesorería «Mes 1…12» y el Mes 1 es enero. Dilo así cuando
   hables de la tesorería, del saldo mínimo o de la estacionalidad: la rampa del arranque cae sobre enero y febrero, los
   meses más flojos, y por eso el fondo de maniobra cuenta; **julio y agosto son el pico** (la semana del 15 de agosto) y
   diciembre repunta con los encargos; en la costa el verano sube más y en el centro de una gran ciudad agosto puede
   bajar: gira la fila.
9. **El pollo y el asador** (pista §6): el rendimiento, el coste del pollo, los pollos por tanda y la capacidad del
   domingo van por token de la calculadora y siempre como **estimación del kit que mides tú** (el tiempo de asado no lo
   publica ningún fabricante y el 78 % del USDA es de horno). El food cost va **siempre sobre el precio SIN IVA**
   ({FC_POLLO_ENTERO} sobre 11,73 €, el pollo de 12,90 € con IVA). **Nada «sin Excel» que la calculadora sí haga**: la
   capacidad del asador, el rendimiento y el escandallo de los combos los hace la calculadora; las variantes SIN Excel
   son la brasa de leña o carbón (horno peruano o churrasqueira), el asador sólo de fin de semana y la costa.
10. **Las cinco corrientes** (pistas §2-§4 y §6): el asador español (con el pollo al ast catalán), el pollo a la brasa
    peruano, el pollo en brasa venezolano, la rôtisserie francesa y la churrasqueira portuguesa con piri-piri. Son
    contenido de guía, sin Excel propio; el caso hace el asador español y el medio pollo a la brasa al estilo peruano en
    el mismo asador de gas. La pollería peruana de sala con horno de brasa remite a la **Guía Restaurante Peruano**.
11. **La jerga** (`jerga` de la entrada): glosa **la primera vez** espada, carga o tanda, encargo, cuarto, sillao,
    cremas, mostrito, rotombo, churrasqueira, piri-piri, guasacaca; «asador de pollos», nunca «asador» suelto por el
    negocio; aclara que en España «pollería» también es la tienda de pollo crudo.
12. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida de
    longitud y registro, nunca su contenido. `gemela_formato_taqueria_es` es el párrafo de la Taquería ES 1.0 en la misma
    ranura: sirve para ver **cómo** se escribe una ranura con tokens y qué tipo de contenido le toca (resumen, mercado,
    equipo, cifras…), nunca su contenido (tacos, trompo, tortilla de maíz, mezcal). El research
    (`F1-research-polleria.md` §0-§6) es material de apoyo: si algo no está en la pista, no lo afirmes. La pista manda.
13. **Crecimiento, caja y honestidad** (§8): el Excel sube los **pedidos** con el mismo ticket y la plantilla con
    personas; la holgura de caja {HOLGURA_CAJA} es la del primer año, de carencia; desde el segundo hay que citar
    {HOLGURA_CAJA_A2} y {BE_PEDIDOS_DIA_CAJA_A2}, y en el tercero {HOLGURA_CAJA_A3}. El food cost de la comida
    ({FOOD_COST}) es la media de toda la carta, no el del pollo entero: dilo con la sensibilidad del precio del pollo de
    la pista §8 (con el precio de Makro, el neto del año 3 baja a un 6,7 %; la palanca es el precio del pollo entero,
    nunca más deuda) y con «precio estimado por el kit» frente al de Makro. El año 3 tributa al tipo general con la
    salvedad de la microempresa. La regla del 21 % para llevar, **entera**: cerveza, vino y refrescos con azúcares o
    edulcorantes añadidos.
14. Ortografía impecable (tildes, «¿», comillas «»), artículo delante de los porcentajes («un 10 %», «el 21 %»),
    espacio antes de «°C» y de «%», sin anglicismos innecesarios salvo los del oficio (delivery sólo si se explica,
    food cost, mise en place).

## Cómo trabajar

Lee la entrada entera (secciones con su pista, jerga, tokens y párrafos), escribe la tanda completa en
`textos/<tanda>.json`, pasa `python3 scripts/productos-digitales/plan-polleria/tandas_docx.py check --tanda <tanda>`
desde la raíz del repo y corrige hasta 0 errores (los avisos de longitud, de cifra escrita y los de la regla 6:
revísalos uno a uno). No toques ningún otro fichero. Devuelve: ruta, nº de párrafos y palabras, y la salida del check.
