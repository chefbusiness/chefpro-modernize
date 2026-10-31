# Plan de Negocio: Hamburguesería Smash ES 1.0 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 31-oct-2026. Camino: `F1-camino.md` §2 (SPEC) y §4. Dos tandas, un redactor por tanda:
> **`ham_es_a`** = §1-5 (29 párrafos) · **`ham_es_b`** = §6-10 (32 párrafos). Las palabras objetivo de cada tanda están en
> su entrada. Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` = `{"<i>": "<párrafo>", …}` con
> TODOS los `i`.

## Qué es el producto

Plan de negocio de una **hamburguesería de smash burgers de servicio rápido** con **cocina a la vista**, **mostrador de
pedidos con pantalla de turnos**, **sala de 30 plazas y 6 taburetes en una barra de ventana** y **zona de empaquetado y de
recogida de los repartidores**, en un local de unos 90 m² de una ciudad media española, con salida de humos a cubierta, sin
traspaso. Una **SL unipersonal** con el titular de **gerente y jefe de plancha**, un cocinero de plancha, uno de montaje y
freidora, un encargado de mostrador y pedidos, un auxiliar de sala y empaquetado y un refuerzo de fin de semana. Vende en
**sala**, **para recoger** (sin comisión) y por **plataforma** con su reparto (con techo, sin reparto propio). Abre en
**enero** (el Mes 1 del Excel es enero, en el orden del calendario); **enero es el valle, mayo el pico** (junio le sigue) y
**agosto baja**. Es producto NUEVO (no hay versión anterior). Lo lee un cocinero o un emprendedor que va a pedir un
préstamo: tono cercano y profesional, **tuteo**, español de España, frases claras, sin relleno ni superlativos vacíos.

## Reglas (las comprueba `tandas_docx.py check --tanda <tanda>`, que se corre en el VPS: ver «Cómo trabajar»)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel o de la calculadora va como token** `{ASI}`, copiado tal cual de `tokens` (el valor de al lado
   es sólo para que redactes con sentido). Ni importes, ni porcentajes, ni comensales, ticket o días del caso tecleados a
   mano: el Excel se puede recalcular y el documento tiene que seguirlo. Escribe la unidad que ya trae el token (no añadas
   «€» ni «%»). **`{PAYBACK}` hoy es una cifra sin unidad («2,4») y puede volver a ser el texto «Más de 3 años»**: la frase
   tiene que leer bien con los dos («El payback antes de la deuda, en años, …: «{PAYBACK}» con el fondo de maniobra dentro
   y «{PAYBACK_CAPEX}» sin él»); nunca «años» detrás del token. `{MES_SALDO_MINIMO_NOMBRE}` es el nombre del mes. El driver
   se llama **comensales EQUIVALENTES** —escribe siempre la palabra «equivalentes» con {COMENSALES_DIA}— (los de sala más
   los pedidos para llevar y a domicilio, contando cada pedido como 1,7 comensales), nunca «cubiertos», «pax» ni «tickets».
3. **Cifras que SÍ puedes escribir**: artículos y normas, y las que traen las pistas y la jerga (el mercado de DBK, las
   búsquedas de DataForSEO y los precios en carta de la pista §3 con su fuente; la carta del caso con IVA; las franquicias y
   Goiko de la pista §4 con su fuente; la carne y las patatas de la pista §6 —8,90 €, 20 %, 3 %, 7,50 €, 90 %, 100 g, 1,6
   bolas, 20 g de queso, 8,09 €, 10,82 €—; los precios de equipo con fuente; los salarios de mercado de la pista §7; la
   sensibilidad de la pista §5 —13.700 €, 12.300 € y 28.700 €— y la de la pista §8 —11.800 € si la carne sube un 20 %—;
   el horario; la estructura del local; las 80 tareas del checklist). Cualquier otra cifra, o es token o no va. El check
   avisa de cada cifra escrita que no está en su lista: revísalas una a una.
4. **El ticket por canal, al céntimo y siempre igual** (lección M1 del Sushi Bar): el comensal de sala, **17,00 € con IVA
   = 15,45 € sin IVA**; el pedido para recoger, **29,10 € con IVA** (casi dos menús) = **15,56 € por comensal
   equivalente**; el de plataforma, con la carta **un 15 % más cara**, **33,47 € con IVA** (29,10 × 1,15) = **17,90 € por
   comensal equivalente**. No escribas otras (ni 33,45 €, ni 30,43 €): son las que cuadran con 1,10 de IVA y 1,7
   comensales por pedido, y las mismas que dice la hoja de Supuestos.
5. **Prohibido** (el check lo caza): «freelance», «validado/a» (di «justificado ante sanidad» o «que respalde tu APPCC»),
   «España 2026», «solopreneur», «tarifa plana», «CNAE», «licencia de apertura» (la apertura es «licencia o declaración
   responsable según la ordenanza»), «carné de manipulador» (salvo para decir que ya no existe), RGSEAA salvo para decir que
   **sólo** aplica si suministras a otros negocios por encima del art. 3, el RD 895/2013, el RD 393/2007, un neto del
   «15-25 %», «versión 1.1/2.2» o «versión anterior»; restos de otros moldes: **food truck** (salvo dentro del nombre
   «Plan de Negocio: Food Truck», la variante D), camión, ventanilla, generador, aparcamiento; del tapas bar: tapa(s)
   —tampoco la de un envase: di «cierre»—, gastrobar, vermut, pinchos, salamandra, Rational; de la heladería: sorbete,
   granizado, horchata, manteca (el **helado** de los batidos sí vale); de la pizzería: pizza, napolitana, levadura,
   mozzarella, cúpula, leña; de la taquería: taquería, trompo, taco(s), comal, al pastor, gringa, nixtamal, tortilla de…,
   mezcal, tequila, aguas frescas, carnitas, suadero, cochinita, guacamole; de la pollería: pollería, asador de pollos,
   pollo a la brasa, pollo asado, broaster («pollo crujiente» sí vale); **del sushi bar (la semilla)**: sushi, sashimi,
   nigiri, maki, uramaki, temaki, poke, itamae, sushiman, shari, nori, neta(s), wasabi, sake, gyoza, edamame, mochi,
   tempura, anisakis, hangiri, arroceras, pH-metro, japonés, combinado(s), salmón, atún, surimi, −20 °C, RD 1420/2006
   («pescado» y «soja» sí: son alérgenos). Y los **errores legales de la carne**: **75 °C** (en España no hay tal regla para
   la hamburguesa; los 74 °C son del recalentado), **155 °F o 68 °C** (son de Estados Unidos). «Campana» siempre «campana
   extractora».
6. **Citas legales** (error del check si fallan): (a) las temperaturas de las comidas preparadas (63 °C, 4/8 °C, de 60 a
   10 °C en menos de 2 horas, 74 °C 15 segundos) son del **art. 30 del RD 1086/2020, en la redacción del RD 1021/2022**:
   escribe siempre «RD 1086/2020» cerca de «art. 30» y nunca lo atribuyas al RD 1021/2022 a secas; (b) **nunca «7 días»**
   junto a congelación, picada, bola o −18 °C; (c) **la cocción NO tiene temperatura legal en España**: si escribes
   «temperatura legal», «obligatoria» u «obligatorio» cerca de la cocción o de los 70 °C, tiene que ir negado («no hay una
   temperatura legal de cocción», «no es obligatoria»); los 70 °C durante 2 minutos son una **recomendación de la AESAN** y
   el punto de control lo fija tu APPCC; (d) **«de un día para otro» siempre con negación** delante («no pudiendo
   conservarse de un día para otro», «nunca de un día para otro»). Lo del **RD 1021/2022** es el art. 2.2.a (la restauración
   es comercio al por menor), el 3 (venta marginal), el 4.1 (carne picada a 2 °C o menos, preparados de carne y verdura
   cortada a 4 °C o menos), el 4.3 (transporte), el **5 (congelación en el minorista)** y el **7.2-7.3 (picado del día y
   capítulos II y III de la sección V del anexo III del Reglamento (CE) 853/2004)**.
7. **Avisos que se revisan uno a uno** (no son error): **−18 °C** sólo como requisito del equipo del art. 5 y con
   «confírmalo con tu inspector» si picas en el local; **carne madurada o «dry aged»** sólo para decir que no se puede
   (Inf26008); **«al punto» o «poco hecha»** sólo como decisión del APPCC o como riesgo, **nunca como promesa**; «sin
   gluten» sólo para decir que **no se promete**; «auténtico» y «gourmet» nunca como sello o promesa; **el batido** junto al
   21 %: el batido de leche va al 10 % («confírmalo con tu gestoría»); el **Día de la Hamburguesa**, fuera (no tiene fuente);
   el registro de jornada es obligatorio, pero **no** digas que la ley lo exige «digital»; las cifras de **franquicia o de
   Goiko**, sólo como comparación o aviso de mercado, nunca como el caso; **180-190 °C** sólo como el error de freír
   demasiado caliente; **«pan común»** sólo para decir que el pan de hamburguesa no lo es; «recongelar» sólo como
   prohibición; un **medidor de polares** nunca «obligatorio» (la Orden de 1989 no obliga a tenerlo).
8. **Legal**: sólo lo de la pista §9, con su cita. No añadas obligaciones, plazos ni importes legales que no estén ahí; lo
   que la pista dice «compruébalo», dilo así. Nunca cifras de ordenanzas de otras ciudades: el único ejemplo leído es Madrid
   (Ordenanza 4/2021, arts. 12, 23, 24 y anexo I), y se presenta como ejemplo. No hay obligación de avisar en la carta de
   la cocción: no la afirmes. El marco legal es el **español**: para México y Latinoamérica, la guía de equivalencias adapta
   los términos, no los trámites ni la norma de la carne molida, del aceite o de la acrilamida.
9. **Mes 1 = enero**: el Excel numera la tesorería «Mes 1…12» y el Mes 1 es enero. Dilo así cuando hables de la
   tesorería, del saldo mínimo o de la estacionalidad: la rampa del arranque va de enero a abril; **enero es el valle**
   (cierre de 10 días y cuesta de enero), **mayo el pico** (buen tiempo y fin de curso), **junio le sigue** y **agosto
   baja** con la ciudad vacía; en la costa julio y agosto suben: gira la fila.
10. **La carne y las patatas** (pista §6): el coste por kilo útil, las bolas por kilo, los kilos de carne al día, el coste
    de cada ración de patatas y del aceite y los food cost van por token de la calculadora y siempre como **estimación del
    kit que mides tú** (no hay precio profesional publicado de la carne picada; la limpieza de la pieza, la merma de cocción
    y las raciones por cambio de aceite no tienen fuente: se miden). El food cost va **siempre sobre el precio SIN IVA**
    ({FC_DOBLE} sobre 10,82 €, la doble de 11,90 € con IVA). Una **loncha de queso de 20 g por bola**. **Nada «sin Excel»
    que la calculadora sí haga**: el coste por kilo útil, si compensa picar en el local, las bolas por kilo, si compensa la
    patata fresca, el aceite por ración y el escandallo por canal los hace la calculadora; las variantes SIN Excel son la de
    sólo reparto, la de servicio de mesa, el carrito o el puesto y la franquicia.
11. **Las variantes** (pista §2): sólo reparto a domicilio (677.9) → la **Guía Dark Kitchen**; servicio de mesa con bola
    gruesa (el riesgo de la cocción); el carrito o el puesto → el **Plan de Negocio: Food Truck**; la franquicia (pista §4).
    El **Kit de Tareas Recurrentes: Hamburguesería** (12 €) trae las hojas de la plancha, la freidora, la línea de montaje
    y el reparto: cítalo donde toque (operaciones, legal, conclusiones). El **Kit de Escandallos Pro** complementa el
    escandallo de toda la carta.
12. **La jerga** (`jerga` de la entrada): glosa **la primera vez** smash, bola, smasher, costra, fry-top, blend, línea de
    montaje, runner, rider; y respeta el «QUÉ NO DECIR».
13. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida de
    longitud y registro, nunca su contenido. `gemela_formato_sushi_es` es el párrafo del Sushi Bar ES 1.0 en la misma
    ranura (la misma rejilla: comensales y rotación): sirve para ver **cómo** se escribe una ranura con tokens y qué tipo de
    contenido le toca (resumen, mercado, equipo, cifras…), nunca su contenido (pescado, arroz, anisakis, itamae). El research
    (`F1-research-hamburgueseria.md` §0-§6) es material de apoyo: si algo no está en la pista, no lo afirmes. La pista manda.
14. **Crecimiento, caja y honestidad** (§8): el Excel sube los **comensales** con el mismo ticket y la plantilla con
    personas; la holgura de caja {HOLGURA_CAJA} es la del primer año, de carencia; desde el segundo hay que citar
    {HOLGURA_CAJA_A2} y {BE_COMENSALES_DIA_CAJA_A2}, y en el tercero {HOLGURA_CAJA_A3}. La rotación: {ROTACION_IMPLICITA} con
    los pedidos dentro frente a un techo de {ROT_MAX}; la de la sala sola ronda {ROT_SALA}. El food cost de la comida
    ({FOOD_COST}) es el **lado prudente**: el escandallo teórico de la calculadora sale en {FC_PONDERADO} y la diferencia
    son **unos cuatro puntos** con nombre (lo que se tira al cierre, las comidas del personal y los errores, las promociones
    de la plataforma): no inventes otros; cada punto vale {PUNTO_FOOD_COST_A1} al año. El año 3 tributa al tipo general con
    la salvedad de la microempresa. La regla del 21 % para llevar, **entera**: la cerveza y los refrescos con azúcares o
    edulcorantes añadidos, **también los zero**. En plataforma, el margen del menú **«cae casi un tercio»** (de
    {MARGEN_SALA_MENU} a {MARGEN_PLATAFORMA_MENU}): la misma frase que el checklist y la calculadora. Precios de la carne,
    el pan, el queso y la patata: **«precio estimado por el kit»**.
15. Ortografía impecable (tildes, «¿», comillas «»), artículo delante de los porcentajes («un 10 %», «el 21 %»), espacio
    antes de «°C» y de «%», sin anglicismos innecesarios salvo los del oficio glosados (smash, smasher, fry-top, blend,
    runner, rider, food cost, mise en place; delivery sólo si se explica).

## Cómo trabajar

Lee la entrada entera (secciones con su pista, jerga, tokens y párrafos), escribe la tanda completa en
`scripts/productos-digitales/plan-hamburgueseria/textos/<tanda>.json` (en el worktree del Mac). Para comprobarla, súbela al
VPS y corre el check allí (en el Mac no se ejecuta nada pesado; el VPS tiene la misma entrada):

    scp <worktree>/scripts/productos-digitales/plan-hamburgueseria/textos/<tanda>.json vps:/root/wt-smash/scripts/productos-digitales/plan-hamburgueseria/textos/
    ssh vps 'cd /root/wt-smash && /root/venv-guias/bin/python scripts/productos-digitales/plan-hamburgueseria/tandas_docx.py check --tanda <tanda> > /tmp/check.txt 2>&1; cat /tmp/check.txt'

y corrige hasta 0 errores (los avisos de longitud, de cifra escrita y los de la regla 7: revísalos uno a uno). No toques
ningún otro fichero ni hagas commit. Devuelve: ruta, nº de párrafos y palabras, y la última línea del check con los avisos
que dejas y por qué.
