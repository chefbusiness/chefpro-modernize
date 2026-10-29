# Taquería ES 1.0 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 29-oct-2026. Camino: `F1-camino.md` §2 (SPEC firmada) y §4. Dos tandas en paralelo, un redactor
> por tanda: **`taq_es_a`** = §1-5 (29 párrafos) · **`taq_es_b`** = §6-10 (32 párrafos). Las palabras objetivo de cada
> tanda están en su entrada. Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` =
> `{"<i>": "<párrafo>", …}` con TODOS los `i`.

## Qué es el producto

Plan de negocio de una **taquería con trompo de gas a la vista y barra de salsas**, con **32 plazas** (24 en mesa y 8
en barra) y una terraza de 16 de abril a octubre, en una ciudad media española: local de 80 m² con salida de humos a
cubierta, sin traspaso. Una **SL unipersonal** con el titular de taquero jefe, un segundo taquero, un cocinero de
producción y salsas, sala de dos servicios y refuerzo de fin de semana. **Tortilla de maíz comprada.** Para llevar por
**recogida** (sin comisión) y por **plataforma** con su reparto, con techo (sin reparto propio). Abre en **enero** (el
Mes 1 del Excel es enero, en el orden del calendario). Es producto NUEVO (no hay versión anterior). Lo lee un taquero o
un emprendedor que va a pedir un préstamo: tono cercano y profesional, **tuteo**, español de España, frases claras, sin
relleno ni superlativos vacíos.

## Reglas (las comprueba `python3 scripts/productos-digitales/plan-taqueria/tandas_docx.py check --tanda <tanda>`)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel o de la calculadora va como token** `{ASI}`, copiado tal cual de `tokens` (el valor de al
   lado es sólo para que redactes con sentido). Ni importes, ni porcentajes, ni comensales, ticket o días del caso
   tecleados a mano: el Excel se puede recalcular y el documento tiene que seguirlo. Escribe la unidad que ya trae el
   token (no añadas «€» ni «%»). **`{PAYBACK}` puede ser una cifra sin unidad (hoy, 2,9) o el texto «Más de 3 años»**:
   la frase tiene que leer bien con los dos («El payback antes de la deuda, en años, … «{PAYBACK}» con el fondo de
   maniobra dentro y «{PAYBACK_CAPEX}» sin él»); nunca «años» detrás del token ni «no se recupera en tres años».
   `{MES_SALDO_MINIMO_NOMBRE}` es el nombre del mes. El driver se llama **comensales** (equivalentes: sala + para
   llevar + domicilio), nunca «cubiertos» ni «clientes».
3. **Cifras que SÍ puedes escribir**: artículos y normas; las búsquedas de DataForSEO y los precios en carta de la pista
   §3 con su fuente; la carta del caso con IVA (pistas §1-§2); la producción y el trompo de la pista §6 (15 kg de cono,
   8 % de adobo, 35 % de merma, 5 % de recortes, 35 g, 18,5 por kg, 25 por kg en Ciudad de México, 255 tacos, 280
   tortillas, 6,2 y 10-11 kg); los precios de equipo con fuente (1.279-1.784 €; 7.808 $); la variante de la tortilla
   (84.000 al año, 12.000 €, 0,10 €, 0,75 jornada, 18.900 €, 15.000-25.000 €); la cuenta del reparto propio de la pista
   §5 (0,35 jornada, 8.800 €, 2.500 €, 11.300 €, un 26 %); la sensibilidad del food cost de la pista §8 (unos 2.900 €
   por punto; con la comida al 30 %, un 8 % de neto el año 2); el horario; la estructura del local (80 m², 32 + 16
   plazas); las 80 tareas del checklist (12/15/14/13/13/13). Cualquier otra cifra, o es token o no va. El check avisa de
   cada cifra escrita que no está en su lista: revísalas una a una.
4. **Prohibido** (el check lo caza): «freelance», «validado/a», «España 2026», «solopreneur», «tarifa plana», «CNAE»,
   «licencia de apertura» (la apertura es «licencia o declaración responsable según la ordenanza»), «carné de
   manipulador» (salvo para decir que ya no existe), RGSEAA salvo para decir que **sólo** aplica si suministras a otros
   negocios por encima del art. 3, el RD 895/2013, el RD 393/2007, un neto del «15-25 %», «versión 1.1/2.2» o «versión
   anterior»; restos de otros moldes: food truck, camión, ventanilla, generador, aparcamiento; del tapas bar: tapa(s)
   —tampoco la «tapa» de un envase: di «cierre» o «cubierta»—, gastrobar, vermut, pinchos, tapeo, afterwork, salamandra,
   Rational; de la heladería: helado/heladería, sorbete, pasteurizar, granizado; **de la pizzería**: pizza/pizzería,
   napolitana, Margherita, leña, levadura, amasado, bolas de masa, fior di latte, mozzarella, chimenea, cúpula, ETG,
   pliego, AVPN. Horchata, tarrina, manteca, raciones, harina (gringa), masa (de maíz) y horno (cochinita) SÍ: son el
   oficio. «Campana» siempre «campana extractora».
5. **El art. 30** (error del check si falla): las temperaturas de las comidas preparadas (63 °C, 4/8 °C, de 60 a 10 °C
   en menos de 2 horas, 74 °C 15 segundos) son del **art. 30 del RD 1086/2020, en la redacción del RD 1021/2022**:
   escribe siempre «RD 1086/2020» junto a «art. 30» y nunca lo atribuyas al RD 1021/2022 a secas. Lo del **RD 1021/2022**
   es el art. 4.1 (preparados de carne y verdura cortada a 4 °C o menos), el 4.2 (etiqueta), el 4.3 (transporte) y el
   8.1 (pescado crudo).
6. **Avisos que se revisan uno a uno** (no son error): «sin gluten» sólo para decir que **no se promete** con comal o
   freidora compartidos; «tex-mex» y «auténtico» sólo para decir lo que NO es la taquería (nunca como promesa o sello);
   el 5 de mayo, mejor no citarlo (no es la fiesta nacional de México); el registro de jornada es obligatorio, pero
   **no** digas que la ley lo exige «digital».
7. **Legal**: sólo lo de la pista §9, con su cita. No añadas obligaciones, plazos ni importes legales que no estén ahí;
   lo que la pista dice «compruébalo», dilo así. Nunca cifras de ordenanzas de otras ciudades: el único ejemplo leído es
   Madrid (Ordenanza 4/2021, arts. 12, 23 y anexo I), y se presenta como ejemplo. La tasa de terraza del Excel es «pon
   la de tu ayuntamiento». El marco legal es el **español**: para México y Latinoamérica, la guía de equivalencias adapta
   los términos, no los trámites.
8. **Mes 1 = enero**: el Excel numera la tesorería «Mes 1…12» y el Mes 1 es enero, en el orden del calendario. Dilo así
   cuando hables de la tesorería, del saldo mínimo o de la estacionalidad, y explica la consecuencia: la rampa del
   arranque cae sobre enero y febrero, los meses más flojos, y por eso el fondo de maniobra cuenta; si el lector abre en
   otro mes, gira la fila de estacionalidad.
9. **El trompo y la tortilla** (pista §6): el rendimiento del cono va por token de la calculadora y siempre como
   «estimación del kit que mides tú» (la merma de cocción no tiene fuente publicada): «mide en el kit, recalcula en el
   plan» (la hoja de rendimiento del Kit de Tareas Recurrentes: Taquería Mexicana). El trompo de carbón y el nixtamal
   propio son variantes **SIN Excel**, razonadas con las cifras de la pista; el nixtamal es decisión de producto, no de
   ahorro. La taquería-mezcalería es otro negocio: remite a la Guía Restaurante Mexicano.
10. **La jerga** (`jerga` de la entrada): los mexicanismos del oficio van tal cual y se glosan **la primera vez** que
    salen en el documento (trompo, orden, gringa, campechano, suadero, salsa macha, nixtamal, comal…). Lima, no
    «limón», para el cítrico verde del taco; totopos, no «nachos».
11. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida de
    longitud y registro, nunca su contenido. `gemela_formato_pizzeria_es` es el párrafo de la Pizzería ES 1.0 en la
    misma ranura: sirve para ver **cómo** se escribe una ranura con tokens y qué tipo de contenido le toca (resumen,
    mercado, equipo, cifras…), nunca su contenido (pizza, horno de leña, masa de trigo, ETG). El research
    (`F1-research-taqueria.md` §0-§6) es material de apoyo: si algo no está en la pista, no lo afirmes. La pista de la
    sección manda.
12. **Crecimiento y caja** (§8): el Excel sube los **comensales** con el mismo ticket y la plantilla con personas; la
    holgura de caja {HOLGURA_CAJA} es la del primer año, de carencia; desde el segundo hay que citar {HOLGURA_CAJA_A2} y
    {BE_COMENSALES_DIA_CAJA_A2}, y en el tercero {HOLGURA_CAJA_A3}: son los años que hay que vigilar. El food cost de la
    comida ({FOOD_COST}) es la media de toda la carta, no el del taco al pastor, y está por debajo del 28-33 % de nuestra
    guía mexicana: dilo con su sensibilidad, sin esconderlo.
13. Ortografía impecable (tildes, «¿», comillas «»), artículo delante de los porcentajes («un 10 %», «el 21 %»),
    espacio antes de «°C» y de «%», sin anglicismos innecesarios salvo los del oficio (delivery sólo si se explica,
    food cost, mise en place).

## Cómo trabajar

Lee la entrada entera (secciones con su pista, jerga, tokens y párrafos), escribe la tanda completa en
`textos/<tanda>.json`, pasa `python3 scripts/productos-digitales/plan-taqueria/tandas_docx.py check --tanda <tanda>`
desde la raíz del repo y corrige hasta 0 errores (los avisos de longitud, de cifra escrita y los de la regla 6:
revísalos uno a uno). No toques ningún otro fichero. Devuelve: ruta, nº de párrafos y palabras, y la salida del check.
