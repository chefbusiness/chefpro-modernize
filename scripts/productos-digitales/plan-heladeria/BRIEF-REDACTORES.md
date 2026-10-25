# Heladería Artesanal ES 1.0 — brief de los redactores del plan de negocio (docx)

> Sesión Claude Code, 25-oct-2026. SPEC: `SPEC.md` D6, D7, D10-D12 y D15. Dos tandas en paralelo, un redactor por tanda:
> **`hel_es_a`** = §1-5 (29 párrafos) · **`hel_es_b`** = §6-10 (32 párrafos). Las palabras objetivo de cada tanda
> están en su entrada. Entrada: `tandas/<tanda>.entrada.json`. Salida: `textos/<tanda>.json` =
> `{"<i>": "<párrafo>", …}` con TODOS los `i`.

## Qué es el producto

Plan de negocio de una **heladería artesanal con obrador propio** en una ciudad media española: local de 85 m² con
obrador de 20-25 m² (pasteurizador, mantecadora, abatidor y armarios), tienda con vitrina de **18 cubetas**, 20 plazas
y una terraza de 5 mesas en temporada. Una **SL unipersonal** con el titular como maestro heladero, un dependiente/a de
todo el año y **fijos discontinuos** de temporada. Abre en **marzo** y en invierno sigue abierta con crepes y gofres,
chocolate, tartas y turrón helado por encargo y helado para restaurantes, con tres semanas de cierre en enero. Es
producto NUEVO (no hay versión anterior). Lo lee un heladero o un emprendedor que va a pedir un préstamo: tono cercano y
profesional, **tuteo**, español de España, frases claras, sin relleno ni superlativos vacíos.

## Reglas (las comprueba `python3 tandas_docx.py check --tanda <tanda>`)

1. **Un párrafo por ranura**, en prosa: sin saltos de línea, viñetas, títulos ni Markdown. Longitud: la de
   `palabras_objetivo` ± 20 % (el check avisa fuera de 70-135 %).
2. **Toda cifra del Excel va como token** `{ASI}`, copiado tal cual de `tokens` (el valor de al lado es sólo para que
   redactes con sentido). Ni importes, ni porcentajes, ni clientes, ticket o días del caso tecleados a mano: el Excel
   se puede recalcular y el documento tiene que seguirlo. Escribe la unidad que ya trae el token (no añadas «€» ni
   «%»). `{PAYBACK}` es texto («Más de 3 años»): no le añadas «años». `{MES_SALDO_MINIMO_NOMBRE}` es el nombre del mes.
3. **Cifras que SÍ puedes escribir**: artículos y normas; las del MAPA y de DataForSEO de la pista §3 con su fuente; la
   carta del caso con IVA de la pista §2 y la mezcla de ventas (58/17/10/5 y 10 de bebidas); los precios de equipo con
   fuente de la pista §6; las temperaturas y tiempos del proceso (40-50 °C, 85 °C, 4 °C, 2-4 °C, 4-12 horas, 24 horas,
   −18 °C, −11/−14 °C) y del huevo (70 °C durante 2 segundos); las denominaciones del RD 618/1998 (4 % de yema, 15 % de
   fruta, 430 g por litro); los límites del art. 3 del RD 1021/2022 (25 % o 500 kg a la semana); los 750 m² de la Ley
   12/2012; la estructura del local (85 m², 20-25 m², 18 cubetas, 10-12 en invierno, 20 plazas, 5 mesas, 30 kW,
   23 kWh); la capacidad de la pista §6 (7.150 kg, 10.500 litros, 38 kg, 11 cubetas); el horario de la pista §6; la
   merma del 5-8 %; las 80 tareas del checklist (12/15/15/12/13/13); la variante de ahorro (40-60 %, unos 90.000 €).
   Cualquier otra cifra, o es token o no va. El check avisa de cada cifra escrita que no está en su lista: revísalas.
4. **Prohibido** (el check lo caza): «freelance», «validado/a», «España 2026», «solopreneur», «tarifa plana», «CNAE»,
   «licencia de apertura», «carné de manipulador» (salvo para decir que ya no existe), RGSEAA salvo para decir que
   **sólo** aplica si sirves a otros negocios fuera del art. 3 (o «inscrito en el RGSEAA»), «versión 1.1/2.2» o
   «versión anterior»; restos de otros moldes: food truck, camión, ventanilla, generador, aparcamiento; restos de la
   panadería: pan, bollería, harina, masa madre, hornada, horno de pisos, amasado, levadura, madrugada, transacción,
   superreducido; las cifras de rentabilidad que contradicen el caso (12-22 %, 28-35 %, 10-18 %, 12-18 % de neto o
   70-80 % de margen bruto: el neto del caso es el de los tokens).
5. **Legal**: sólo lo de la pista §9, con su cita. No añadas obligaciones, plazos ni importes legales que no estén ahí;
   lo que la pista dice «compruébalo», dilo así. Nunca escribas que el 644.4 necesita «licencia de apertura»: va por
   declaración responsable; la licencia o declaración municipal es de la parte de hostelería (mesas) y la terraza va
   siempre aparte. Nunca cifras de ordenanzas (tasa de terraza, humos): no se ha leído ninguna; la tasa del Excel es
   «pon la de tu ayuntamiento».
6. **Orden del proceso (seguridad, no negociable, SPEC D11)**: en cualquier ranura que describa la elaboración, el orden
   es el de `orden_del_proceso` de la entrada: grasas (nata, mantequilla), yemas y emulsionantes **ANTES** de
   pasteurizar, a 40-50 °C al subir → 85 °C → enfriado rápido a 4 °C o menos → maduración a 2-4 °C (con huevo, mantecar
   en 24 horas) → mantecación → abatimiento → conservación a −18 °C o menos. **Después de pasteurizar sólo lo que no
   necesita tratamiento térmico** (pastas puras, variegatos, fruta lavada en sorbetes); nunca yema ni nata cruda. El
   check avisa si encuentra grasa, nata o yema «después de pasteurizar».
7. **Mes 1 = marzo** (SPEC D6): el Excel numera la tesorería «Mes 1…12» y el Mes 1 es marzo. Dilo así cuando hables de
   la tesorería, del saldo mínimo o de la estacionalidad («el mes 5, julio»), y explica por qué: abrir en otoño gasta el
   fondo antes del primer verano. **Invierno (SPEC D7)**: el caso sigue abierto con diversificación; crepes y gofres sólo
   si la ordenanza permite la salida de humos (si no, chocolate, tartas y turrón helado); el cierre de noviembre a
   febrero va como **alternativa razonada SIN cifras del Excel** (pista §8). La tesorería reparte el personal en doce
   meses aunque los fijos discontinuos sólo cobran en temporada: el invierno sale más caro que en la realidad (lado
   prudente).
8. **Fuentes por párrafo**: `molde_ft_es` es el párrafo del food truck que ocupa esa ranura: úsalo SOLO como medida de
   longitud y registro, nunca su contenido. `gemela_formato_parrillero_es` es el párrafo del Parrillero ES 2.2 en la
   misma ranura: sirve para ver **cómo** se escribe una ranura con tokens y qué tipo de contenido le toca (resumen,
   mercado, equipo, cifras…), nunca su contenido (parrilla, eventos, carne, gas). El research
   (`F1-research-heladeria.md` §1, §3, §4 y §6) es material de apoyo: si algo no está en la pista, no lo afirmes. La
   pista de la sección manda.
9. Identidad intacta: obrador propio y helado del día, denominaciones honestas, «ELABORACIÓN PROPIA» si no hay
   calificación artesanal, alérgenos resueltos, plantilla con **fijos discontinuos** (art. 16 ET), nunca autónomos que
   te facturan. El ticket de {TICKET} es **por persona** y sin IVA, no por tique de caja.
10. **Crecimiento y caja** (§8): el Excel sube los **clientes** con el mismo ticket; la holgura de caja {HOLGURA_CAJA}
    es la del primer año, de carencia; desde el segundo hay que citar {HOLGURA_CAJA_A2} y {BE_CLIENTES_DIA_CAJA_A2}, y
    en el tercero {HOLGURA_CAJA_A3}: son los años que hay que vigilar.
11. Ortografía impecable (tildes, «¿», comillas «»), artículo delante de los porcentajes («un 30 %», «el 10 %»),
    «−18 °C» con el signo menos y espacio antes de «°C», sin anglicismos innecesarios salvo los del oficio (topping,
    gelato, B2B solo si se explica).

## Cómo trabajar

Lee la entrada entera (secciones con su pista, orden del proceso, tokens y párrafos), escribe la tanda completa en
`textos/<tanda>.json`, pasa `python3 scripts/productos-digitales/plan-heladeria/tandas_docx.py check --tanda <tanda>`
desde la raíz del repo y corrige hasta 0 errores (los avisos de longitud, de cifra escrita o de orden del proceso:
revísalos uno a uno). No toques ningún otro fichero. Devuelve: ruta, nº de párrafos y palabras, y la salida del check.
