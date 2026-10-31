# Plan de Negocio: Sushi Bar ES 1.0 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 31-oct-2026. Camino: `F1-camino.md` §2 (SPEC) y §4. Dos tandas, un redactor por tanda:
> **`sus_es_a`** = §1-5 (29 párrafos) · **`sus_es_b`** = §6-10 (32 párrafos). Las palabras objetivo de cada tanda están en
> su entrada. Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` = `{"<i>": "<párrafo>", …}` con
> TODOS los `i`.

## Qué es el producto

Plan de negocio de un **sushi bar de barrio** con **barra de sushi a la vista** (8 taburetes y vitrina de neta), **sala de
28 plazas** y **zona de empaquetado de pedidos**, en un local de unos 95 m² de una ciudad media española, con salida de humos
a cubierta y cocina eléctrica, sin traspaso. Una **SL unipersonal** con el titular de **itamae** y gerente, un sushiman,
cocina caliente, sala y refuerzo de fin de semana. Vende en **sala**, **para recoger** (sin comisión) y por **plataforma**
con su reparto (con techo, sin reparto propio). Abre en **enero** (el Mes 1 del Excel es enero, en el orden del
calendario); **diciembre es el pico y agosto el valle**. Es producto NUEVO (no hay versión anterior). Lo lee un cocinero o
un emprendedor que va a pedir un préstamo: tono cercano y profesional, **tuteo**, español de España, frases claras, sin
relleno ni superlativos vacíos.

## Reglas (las comprueba `tandas_docx.py check --tanda <tanda>`, que se corre en el VPS: ver «Cómo trabajar»)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel o de la calculadora va como token** `{ASI}`, copiado tal cual de `tokens` (el valor de al lado
   es sólo para que redactes con sentido). Ni importes, ni porcentajes, ni comensales, ticket o días del caso tecleados a
   mano: el Excel se puede recalcular y el documento tiene que seguirlo. Escribe la unidad que ya trae el token (no añadas
   «€» ni «%»). **`{PAYBACK}` hoy es una cifra sin unidad («2,5») y puede volver a ser el texto «Más de 3 años»**: la frase
   tiene que leer bien con los dos («El payback antes de la deuda, en años, …: «{PAYBACK}» con el fondo de maniobra dentro
   y «{PAYBACK_CAPEX}» sin él»); nunca «años» detrás del token. `{MES_SALDO_MINIMO_NOMBRE}` es el nombre del mes. El driver
   se llama **comensales** (comensales equivalentes: los de sala más los pedidos para llevar y a domicilio, contando cada
   pedido como 1,6 comensales), nunca «cubiertos», «pax» ni «tickets».
3. **Cifras que SÍ puedes escribir**: artículos y normas, y las que traen las pistas y la jerga (las búsquedas de
   DataForSEO y los precios en carta de la pista §3 con su fuente; la carta del caso con IVA; las franquicias de la pista
   §4 con su fuente; el pescado y el arroz de la pista §6 —9,50 €, 55 %, 15 %, 5 %, 21,80 €, 26,00 €, × 2,2, 10 %, 20 g,
   150 g, 1,81-1,85 €, 4,73 €, 5,20 €—; los precios de equipo con fuente; los salarios de mercado de la pista §7; la
   sensibilidad de la pista §8 —8.200 € si el salmón sube un 20 %— y la de la plataforma de la pista §5 —14.000 €—; el
   horario; la estructura del local; las 80 tareas del checklist). Cualquier otra cifra, o es token o no va. El check
   avisa de cada cifra escrita que no está en su lista: revísalas una a una.
4. **Prohibido** (el check lo caza): «freelance», «validado/a» (di «justificado ante sanidad»), «España 2026»,
   «solopreneur», «tarifa plana», «CNAE», «licencia de apertura» (la apertura es «licencia o declaración responsable según
   la ordenanza»), «carné de manipulador» (salvo para decir que ya no existe), RGSEAA salvo para decir que **sólo** aplica
   si suministras a otros negocios por encima del art. 3, el RD 895/2013, el RD 393/2007, un neto del «15-25 %», «versión
   1.1/2.2» o «versión anterior»; restos de otros moldes: food truck, camión, ventanilla, generador, aparcamiento; del
   tapas bar: tapa(s) —tampoco la de un envase: di «cierre»—, gastrobar, vermut, pinchos, salamandra, Rational; de la
   heladería: helado, sorbete, granizado, horchata, manteca; de la pizzería: pizza, napolitana, levadura, mozzarella,
   cúpula, leña; **de la taquería**: taquería, trompo, taco(s), comal, pastor, gringa, nixtamal, tortilla de maíz o de
   harina, mezcal, tequila, aguas frescas, carnitas, suadero, cochinita, guacamole; **de la pollería**: pollería, asador de
   pollos, pollo a la brasa, pollo asado, broaster; y «pan común». «Campana» siempre «campana extractora». «Cubeta» sí
   puedes (la vitrina de sushi va en cubetas GN).
5. **Citas legales** (error del check si fallan): (a) las temperaturas de las comidas preparadas (63 °C, 4/8 °C, de 60 a
   10 °C en menos de 2 horas, 74 °C 15 segundos) y la vía del shari a temperatura ambiente son del **art. 30 del RD
   1086/2020, en la redacción del RD 1021/2022**: escribe siempre «RD 1086/2020» cerca de «art. 30» (también en «30.5») y
   nunca lo atribuyas al RD 1021/2022 a secas; (b) el **RD 1420/2006** sólo para decir que está **derogado**; (c) **nunca
   «7 días»** junto a anisakis o congelación (es la opción de Estados Unidos). Lo del **RD 1021/2022** es el art. 3 (venta
   marginal), el 4.1 (pescado fresco entre 0 y 4 °C), el 4.2 (etiqueta), el 4.3 (transporte) y el **8.1-8.2 (anisakis:
   −20 °C 24 h o −35 °C 15 h en la totalidad del producto; informar al cliente en la carta o en un cartel)**.
6. **Avisos que se revisan uno a uno** (no son error): nunca «sushi grade» ni «sashimi grade» como garantía; «auténtico»
   nunca como promesa; «sin gluten» sólo para decir que **no se promete**; **nunca «obligatorio» junto a un pH o a unas
   horas del shari** (no hay pH ni tiempo legal en España: el 4,6 es el límite crítico del APPCC del Kit de Tareas); «−18 °C»
   sólo para decir que **no sirve** para el anisakis; el registro de jornada es obligatorio, pero **no** digas que la ley lo
   exige «digital»; las cifras de franquicia, sólo como comparación, nunca como el caso.
7. **Legal**: sólo lo de la pista §9, con su cita. No añadas obligaciones, plazos ni importes legales que no estén ahí; lo
   que la pista dice «compruébalo», dilo así. Nunca cifras de ordenanzas de otras ciudades: el único ejemplo leído es Madrid
   (Ordenanza 4/2021, arts. 12, 23 y anexo I), y se presenta como ejemplo. El marco legal es el **español**: para México y
   Latinoamérica, la guía de equivalencias adapta los términos, no los trámites ni la norma del pescado crudo.
8. **Mes 1 = enero**: el Excel numera la tesorería «Mes 1…12» y el Mes 1 es enero. Dilo así cuando hables de la
   tesorería, del saldo mínimo o de la estacionalidad: la rampa del arranque va de enero a abril; **diciembre es el pico**
   (bandejas de Nochebuena y Nochevieja), **febrero sube** con San Valentín y **agosto es el valle** (cierre de 10 días y
   ciudad vacía); en la costa agosto sube: gira la fila.
9. **El pescado y el arroz** (pista §6): el coste por kilo útil, el shari por kilo de arroz, los nigiris por kilo, el arroz
   del día y los food cost van por token de la calculadora y siempre como **estimación del kit que mides tú** (el 50-60 % de
   lomo limpio del salmón no tiene fuente técnica). El food cost va **siempre sobre el precio SIN IVA** ({FC_NIGIRI_SALMON}
   sobre 4,73 €, el nigiri de 5,20 € con IVA). **Nada «sin Excel» que la calculadora sí haga**: el rendimiento del salmón,
   si compensa el entero, el shari por kilo y el escandallo por canal los hace la calculadora; las variantes SIN Excel son
   el formato de sólo para llevar, el omakase, el kaiten o el buffet libre, el nikkei y el japonés completo.
10. **Las variantes** (pista §2): sólo para llevar y a domicilio (677.9), barra y mesas (el caso), omakase, kaiten o buffet
    libre; el nikkei remite a la **Guía Restaurante Nikkei** y el japonés completo (ramen, izakaya, robata) a la **Guía
    Restaurante Japonés**. El **Kit de Tareas Sushi Bar** trae las hojas de pH del shari, de congelación y de la vitrina:
    cítalo donde toque (operaciones, legal, conclusiones).
11. **La jerga** (`jerga` de la entrada): glosa **la primera vez** itamae, sushiman, neta, shari, sushi-zu, saku, hangiri,
    nigiri, sashimi, hosomaki, uramaki, temaki, combinado, omakase, kaiten; y respeta el «QUÉ NO DECIR».
12. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida de
    longitud y registro, nunca su contenido. `gemela_formato_taqueria_es` es el párrafo de la Taquería ES 1.0 en la misma
    ranura (la misma rejilla: comensales y rotación): sirve para ver **cómo** se escribe una ranura con tokens y qué tipo de
    contenido le toca (resumen, mercado, equipo, cifras…), nunca su contenido (tacos, trompo, tortilla, mezcal). El research
    (`F1-research-sushi.md` §0-§6) es material de apoyo: si algo no está en la pista, no lo afirmes. La pista manda.
13. **Crecimiento, caja y honestidad** (§8): el Excel sube los **comensales** con el mismo ticket y la plantilla con
    personas; la holgura de caja {HOLGURA_CAJA} es la del primer año, de carencia; desde el segundo hay que citar
    {HOLGURA_CAJA_A2} y {BE_COMENSALES_DIA_CAJA_A2}, y en el tercero {HOLGURA_CAJA_A3}. La rotación: {ROTACION_IMPLICITA} con
    los pedidos dentro frente a un techo de {ROT_MAX}; la de la sala sola ronda {ROT_SALA}. El food cost de la comida
    ({FOOD_COST}) es el **lado prudente**: el escandallo teórico de la calculadora sale en {FC_PONDERADO} y la diferencia es
    lo que se pierde entre la receta y la caja (pista §8, sin inventar puntos); cada punto vale {PUNTO_FOOD_COST_A1} al año.
    El año 3 tributa al tipo general con la salvedad de la microempresa. La regla del 21 % para llevar, **entera**: cerveza,
    sake, vino y refrescos con azúcares o edulcorantes añadidos.
14. Ortografía impecable (tildes, «¿», comillas «»), artículo delante de los porcentajes («un 10 %», «el 21 %»), espacio
    antes de «°C» y de «%», sin anglicismos innecesarios salvo los del oficio (food cost, mise en place, delivery sólo si se
    explica).

## Cómo trabajar

Lee la entrada entera (secciones con su pista, jerga, tokens y párrafos), escribe la tanda completa en
`scripts/productos-digitales/plan-sushi/textos/<tanda>.json` (en el worktree del Mac). Para comprobarla, súbela al VPS y
corre el check allí (en el Mac no se ejecuta nada pesado; el VPS tiene la misma entrada):

    scp <worktree>/scripts/productos-digitales/plan-sushi/textos/<tanda>.json vps:/root/wt-sushi/scripts/productos-digitales/plan-sushi/textos/
    ssh vps 'cd /root/wt-sushi && /root/venv-guias/bin/python scripts/productos-digitales/plan-sushi/tandas_docx.py check --tanda <tanda> > /tmp/check.txt 2>&1; cat /tmp/check.txt'

y corrige hasta 0 errores (los avisos de longitud, de cifra escrita y los de la regla 6: revísalos uno a uno). No toques
ningún otro fichero ni hagas commit. Devuelve: ruta, nº de párrafos y palabras, y la última línea del check con los avisos
que dejas y por qué.
