# Verificación independiente de los fixes — 9 libros «Cómo Montar una Chocolatería» (2026-09-12)

> Verificador independiente, SOLO LECTURA, de los 23 fixes que el fixer dice haber aplicado sobre
> `auditorias/guia-chocolateria-xlsx-refutacion-2026-09-12.json` (24 hallazgos) más el descarte declarado de
> B14. Cada libro se abrió por separado (fórmulas y `data_only`), con `istats cpu temp` entre ejecuciones
> (máximo registrado 43,4 °C). Contrastado con el estado ACTUAL de `build/*.xlsx` (commit `e8bea93`, working
> tree limpio) y con `datos_ejemplo.py`. Se comprueba el EFECTO, no solo la celda, y se usa pycel en 3 libros
> con la salida evaluada ANTES de tocar la entrada.
>
> **Veredicto: CORREGIR.** Los 4 hallazgos ALTOS y 8 de los 10 MEDIOS están resueltos de verdad y verificados
> con evidencia (incluida verificación de comportamiento con pycel, no solo de texto). Pero de los 10 BAJOS,
> **uno no se aplicó (B9)**, **tres quedaron a medias (A8, A9, A10)**, y el fix de B10 **introduce un defecto
> nuevo** (un `%%` literal que se imprimirá en el Excel). B4 y B8 (MEDIOS) también quedan parciales. Ninguno de
> estos residuos es grave por sí solo, pero la política del proyecto es no cerrar con hallazgos sin resolver, y
> uno de ellos (B8) toca precisión legal, que es la promesa central de un pack «checklist legal».

## 0. Gate y comprobaciones transversales

| Comprobación | Resultado |
|---|---|
| `python3 gate_libros.py` | **VERDE — 9/9 libros en verde**, incluida la fila «LOS OCHO CRUCES DE `datos_ejemplo.CRUCES`» |
| pycel — libro 5 (`vida-util-rellenos-y-rotacion.xlsx`), `Vida Útil Declarada!G16` 10→3 | `L40` 10→**3**, `M40` pasa a «Por encima de la pieza más corta que llevas dentro…» (ANTES de este fix, `L40` no se movía: era una constante) |
| pycel — libro 8 (`checklist-legal-licencias-y-cacao.xlsx`), `Suministro a Otros Minoristas!B6` «Sí»→«No» | `B41` pasa de «Cumples las tres: sigues FUERA del RGSEAA…» a «El art. 3 no te aplica…»; `B42` de la declaración responsable a «Nada de esto te aplica» |
| pycel — libro 6 (`campanas-y-valle-del-ano.xlsx`), `Capacidad vs Demanda del Pico!B6` 512→160 | `B9` (CUADRE) pasa a «REVISA…», `H23` (déficit Navidad) sube de 887,68 a 1.239,68, `B26` (campañas que no aguanta) sube de 7 a 12 |
| Los 8 cruces de `datos_ejemplo.CRUCES`, valor por defecto del receptor = celda de origen | **8/8 cuadran**: capacidad 512=512 (1); CAPEX depurado 89.219,35=89.219,35 (6, ahora vía `Resumen!B7`); fondo de maniobra 61.273,02≈61.273,0157 (8, `CUADRA`); plazo crítico 10=10 (7); CAPEX bloque 21.060=21.060 (3); precio cobertura 22,7455=22,7455 (4 y 5, sin tocar por estos fixes) |
| Nombres de hoja de `CRUCES` (A5) | Los 4 corregidos: `Coste de Cobertura`, `Parámetros`, `Tesorería 12 meses`, `PyG 3 Años` — los 4 existen de verdad |

## 1. Tabla de veredictos

| Id | Gravedad | Estado | Evidencia | Qué falta (en el generador) |
|---|---|---|---|---|
| **A1** | alto | **APLICADO** | `capacidad-obrador-y-clima.xlsx!Cuello de Botella` ahora termina en fila 16 (bloque de 12 campañas A16:J34 eliminado); `A16` remite al libro 6. `campanas-y-valle-del-ano.xlsx!Capacidad vs Demanda del Pico!B6`=512 (único origen), `B7`=«cifra que publica hoy el libro 1», `B9`=CUADRE. Un solo modelo de demanda/déficit, verificado con pycel (B6 160 mueve H23 y B26) | Nada |
| **A2** | alto | **APLICADO** | `vida-util-rellenos-y-rotacion.xlsx!Vida Útil Declarada!L40:L43` ahora son fórmulas `=MIN($G$16,…)` sobre las piezas de cada caja (ya no constantes bloqueadas). `C40:C43`=«Bombones de ganache con nata fresca» (la familia correcta, no la de nata UHT). Verificado con pycel: bajar `G16` de 10 a 3 mueve `L40` a 3 y `M40` cambia de veredicto | Nada |
| **A3** | medio | **APLICADO** | Las 3 celdas ahora citan `!Hoja!Celda` completo: `calculadora-capex-chocolateria.xlsx!CAPEX por Bloque!C51`→«…Inversión Inicial!B16»; `carta-de-apertura-y-escandallo-chocolate.xlsx!Parámetros!A25`→«…Coste de Cobertura!G7 (…G8/G9/G10…)»; `checklist-equipamiento-y-proveedores-cacao.xlsx!Equipamiento!A46`→«…CAPEX por Bloque!L33» | Nada |
| **A4** | medio | **APLICADO** | `plan-financiero-3-anos-chocolateria.xlsx!Inversión Inicial!A6` ahora dice «…de `calculadora-capex-chocolateria.xlsx!Resumen!B7`», que existe y publica 89.219,35 (=`'CAPEX por Bloque'!L44`) | Nada |
| **A5** | medio | **APLICADO** | `datos_ejemplo.CRUCES`: `hoja_origen`/`hoja_receptor` ahora son `'Coste de Cobertura'`, `'Parámetros'`, `'Tesorería 12 meses'`, `'PyG 3 Años'` — las 4 existen en los ficheros reales y `gate_libros.py` las valida sin falsos negativos | Nada |
| **A6** | medio | **APLICADO** | `calculadora-capex-chocolateria.xlsx!CAPEX por Bloque!I28/J28/K28`=`'=$L$51'` (fórmula, ya no constante duplicada); `C28`=«Fondo de maniobra traído del libro 7 (EUR)»; `Resumen!D8` ya no contradice a `A8` («Es caja… Pero hay que APORTARLA o FINANCIARLA… por eso está dentro del total») | Nada |
| **A7** | bajo | **APLICADO** | La etiqueta «Coste anual del impuesto al plástico» ya NO está en `mapa-calculadora-capex-chocolateria.json`; en su lugar el mapa publica «ALERTA DEL PLÁSTICO»→`IVA y Tesorería!B37`=«Sin alerta» (con contenido en los dos estados) | Nada |
| **A8** | bajo | **PARCIAL** | Sólo 2 de los 9 mapas (`calculadora-capex-chocolateria`, `capacidad-obrador-y-clima`) ya NO llevan `_notas`. **Los otros 7** (`campanas-y-valle-del-ano`, `carta-de-apertura-y-escandallo-chocolate`, `checklist-equipamiento-y-proveedores-cacao`, `checklist-legal-licencias-y-cacao`, `plan-financiero-3-anos-chocolateria`, `sensibilidad-al-precio-del-cacao`, `vida-util-rellenos-y-rotacion`) SIGUEN publicando `"_notas": {"tipo": "nota", "ref": "…!Instrucciones!A1", "valor": "<texto largo>"}` — `tipo` sigue sin ser `entrada\|salida\|parametro` y `valor` sigue sin ser el de la celda | Quitar (o mover a `{"_meta": {...}}`) la entrada `_notas` en los 7 mapas restantes; el fix sólo se aplicó donde se regeneró el libro 2 y el 1 |
| **A9** | bajo | **PARCIAL** | Los 11 casos explícitamente listados en la refutación están corregidos (verificado uno a uno: `CAPEX por Bloque`, `Capacidad vs Demanda del Pico`, `Capacidad por Equipo`, `Escandallo por Molde y Tanda`, `Unidad vs Caja`, `Coste de Cobertura por Referencia`, `Lote y Merma por Caducidad`, `Clientes a los que Suministras: El Registro…`, los dos de libro 7, y `…y Qué Fecha te Corre`). **Pero la lista de palabras funcionales del helper sigue sin incluir «sobre»**: `campanas-y-valle-del-ano.xlsx!Peso sobre el Año!A1` = `'Peso Sobre el Año'` (debería ser `'Peso sobre el Año'`, y la propia PESTAÑA ya lo lleva bien) | Añadir `sobre` (y probablemente `tras`, `según`, `mediante`, `hasta`, `desde`) a la lista de minúsculas del helper de título en `_comun_chocolateria.py` |
| **A10** | bajo | **PARCIAL** | Mejora real en 3 de los 5 libros originalmente en cero: libro 1 6/7 hojas, libro 2 7/7, libro 3 5/6. **Pero libro 4 y libro 6 siguen en 0/9 y 0/7** — ninguna hoja de esos dos libros tiene `freeze_panes`, pese a estar nombrados explícitamente en el hallazgo original. Libro 7 mejoró de 7/11 a 9/11 (faltan `Inversión Inicial` y `Talleres y Regalo Corporativo`) | Aplicar `cerrar_hoja()`/`freeze_panes` en `gen_carta-de-apertura-y-escandallo-chocolate.py` y `gen_campanas-y-valle-del-ano.py` (no se tocaron) y en las 2 hojas que faltan de `gen_plan-financiero-3-anos-chocolateria.py` |
| **B1** | alto | **APLICADO** | `checklist-equipamiento-y-proveedores-cacao.xlsx!Proveedores y EUDR!G7/G8/G10`=«No lo sé» (Callebaut, Bean to Bar, RestorHome); `G9/G11/G12`=«No aplica: no vende producto del Anexo I» (Utilcentre, SelfPackaging, Gift Campaign). `N7`(cache)=«Pregúntaselo por escrito antes de comprar…», `N9`=«No le pidas papeles EUDR: no vende producto del Anexo I», `O9`=«No aplica: fuera del ámbito EUDR» | Nada |
| **B2** | alto | **APLICADO** | `checklist-legal-licencias-y-cacao.xlsx!Suministro a Otros Minoristas!B6`=«Sí» (antes «No»); `B41`(cache)=«Cumples las tres: sigues FUERA del RGSEAA, con la declaración responsable y el registro del art. 3.5». Verificado con pycel en los dos sentidos | Nada (nota: `B6` es un valor sembrado en Python, no una fórmula que derive de `CLIENTES_B2B`; funcionalmente correcto, pero si el juego de datos cambia habrá que volver a sembrarlo a mano) |
| **A5→A3 cruces** | — | ver A3/A5 | — | — |
| **B3** | medio | **APLICADO** | `sensibilidad-al-precio-del-cacao.xlsx!Escenarios de Precio!F16`=`'=IFERROR(($D16+$C16*$D$7)/(1-$R16),"")'` (ahora divide por `1-merma`, columna `R` nueva). TB4 food cost = **0,353476…** en el libro 3, **idéntico** al 0,353476… del libro 4. `G44`(rotas)=**7** en los dos libros | Nada |
| **B4** | medio | **PARCIAL** | El número y la nota ya son coherentes: `plan-financiero-3-anos-chocolateria.xlsx!Inversión Inicial!B11`=83.614,99=89.219,35−2.600−3.004,36 (antes 86.619,35, sólo restaba la fianza), y `D11` describe exactamente esa resta. Cascada verificada: `B27`=8.361,499, `PyG 3 Años!C29`=8.361,499. **Pero la hoja `Resumen` del libro 2 SIGUE sin publicar una línea «Inmovilizado amortizable»**, así que la etiqueta «traído del libro 2» de `B11`/`D11` no se puede verificar abriendo el libro 2 | Añadir en `gen_calculadora-capex-chocolateria.py!Resumen` la línea «Inmovilizado amortizable» (=CAPEX sin fondo − fianza − packaging), tal y como pedía el fix original |
| **B5** | medio | **APLICADO** | `plan-financiero-3-anos-chocolateria.xlsx!Canales y Punto Muerto` ya NO calcula el art. 3: `B30`=«Peso del canal B2B… (referencia; NO es el test del art. 3)», `A31`/`A32` explican la base correcta (volumen, sólo minoristas) y remiten a `checklist-legal-licencias-y-cacao.xlsx!Suministro a Otros Minoristas!B26` | Nada |
| **B6** | medio | **APLICADO** | `vida-util-rellenos-y-rotacion.xlsx!Temperatura y Vitrina!D46:D49`=4 (antes 18), mismo criterio que `aw`/vida útil. `F50`(«Referencias que van a nevera»)=**6** (antes 2) | Nada |
| **B7** | medio | **APLICADO*** | `campanas-y-valle-del-ano.xlsx!Calendario de Campañas!E7`(Reyes)=«TF4 - Turrón de chocolate con almendra, 250 g»; `E16`(Halloween)=«BC5 - Trufa de chocolate negro al cacao». Ya NO hay un huevo de Pascua en dos meses que no son Pascua | *Matiz: el fix recomendaba una FIGURA DE REYES propiamente dicha (o TF3/BC5); se optó por un turrón, que es consumo real de Reyes en España pero no es «figura», así que sigue sin existir esa referencia en `datos_ejemplo.CARTA` — no es un error, es una oportunidad de mejora futura |
| **B8** | medio | **PARCIAL** | Mejora real y grande: **136/201 (68 %)** de las notas legales del pack citan ya artículo/apartado/anexo/epígrafe (antes 31/201, 15 %, contando también «Apartado» deletreado, no sólo «art.»/«ap.»). Por libro: sensibilidad 100 %, vida útil 86 %, checklist-legal 80 %, CAPEX 79 %, checklist-equipamiento 64 %, capacidad 67 %, financiero 57 %, **carta y escandallo sólo 38 %** (era el peor con 0 %), **campañas sigue en 33 %** (1/3). **No existe el gate/abort en `nota_legal()`** que el fix pedía: sigue habiendo 65 notas sin artículo, algunas en el libro de denominaciones (RD 1055/2003) que es justo el caso que motivó el hallazgo | Terminar `nota_legal(id)` en `_comun_chocolateria.py` para que use el campo de artículo de la ficha `CHN-*` siempre que exista, y añadir el gate que aborta si no hay `art.`/`ap.`/`Anexo`/`Epígrafe`; revisar en particular `carta-de-apertura-y-escandallo-chocolate.py` |
| **B9** | bajo | **NO APLICADO** | `carta-de-apertura-y-escandallo-chocolate.xlsx!Denominaciones y Mínimos!F20/F21/F27/F29` SIGUEN siendo texto descriptivo («…no pueden exceder el 40 %…») sin ninguna columna que calcule `J/K` ni semáforo contra `0,40`. La zona «Los mínimos que usa el semáforo» (`A37:B41`) sólo tiene 4 parámetros (25 %, 35 %, 18 %, 14 %); no hay un quinto para el 40 % | Añadir en `gen_carta-de-apertura-y-escandallo-chocolate.py` la columna «Materias añadidas sobre el peso total»=`J/K` y su semáforo contra un parámetro `0,40` nuevo en `A38:B41`, tal y como pedía el hallazgo |
| **B10** | bajo | **APLICADO, con defecto nuevo** | `Denominaciones y Mínimos!M31:M34`=«No» y `N31:N34` ya dicen «La denominación va por pieza…», corrigiendo el fondo del hallazgo. **Pero la fórmula de `N31:N34` tiene un `%%` literal**: `'…el 25 %% lo comprueba cada bombón…'` — el cache confirma que el texto que verá el comprador dice **«el 25 %% lo comprueba»** (doble signo de porcentaje), casi con toda seguridad un escape `%%`→`%` de un `%`-format de Python que se quedó sin resolver | En `gen_carta-de-apertura-y-escandallo-chocolate.py`, la plantilla de `N31:N34` usa `%%` donde debería ir un solo `%` (o se generó con un f-string/`.format()` que no se aplicó); revisar y dejar `'25 %'` |
| **B11** | bajo | **APLICADO** | `calculadora-capex-chocolateria.xlsx!Instrucciones` ya menciona `kit-tareas-chocolateria` («True» en la búsqueda de texto) | Nada |
| **B12** | bajo | **APLICADO** | `mapa-checklist-legal-licencias-y-cacao.json`: las tres etiquetas ahora son «Estado de la hoja EUDR antes de que rellenes tu papel», «La fecha del EUDR que te corre (una vez resuelto tu papel)», «La documentación EUDR que te toca (una vez resuelto tu papel)» — ya no se pueden citar como conclusión del caso | Nada |
| **B13** | bajo | **APLICADO** | `checklist-equipamiento-y-proveedores-cacao.xlsx!Clientes a los que Suministras!E13`=«Minorista de distinta titularidad» (antes «B2B a hostelería», que contradecía `D13`). Ya no hay dos columnas incompatibles en la misma fila | Ninguno funcional; nota: no se añadió el canal «B2B a minorista» que sugería el fix, se igualó `E13` a `D13` — resuelve la contradicción igualmente |
| **B14** | bajo | **Correctamente NO tocado** | `checklist-legal-licencias-y-cacao.xlsx!Ruta Doméstica!B20` sigue con «Verificado el 10-09-2026 · RD 1021/2022, art. 13.9 · … · Reutilizado de la verificación legal de «Cómo Montar una Pastelería»…» | Ver §2 — mi lectura coincide con la del refutador: no tocar |

## 2. B14 — ¿es correcto dejar la fecha 10-09-2026?

Sí. La nota de `Ruta Doméstica!B20` no es una afirmación «esto se verificó hoy»: es la reutilización explícita y
declarada de una cita literal ya verificada para otro producto (Pastelería, `PA-29c`), y el propio texto de la
nota lo dice sin ambigüedad («Reutilizado de la verificación legal de «Cómo Montar una Pastelería»»). Poner
«12-09-2026» ahí sería **peor**, no mejor: afirmaría que alguien releyó el art. 13.9 el 12 de septiembre cuando
lo que de verdad pasó es que se reutilizó una verificación de dos días antes. La fecha de una verificación legal
debe ser la fecha en que se verificó ese hecho concreto, no la fecha de cierre del producto que la usa.

Lo que yo haría (y coincide con lo que pide el hallazgo): **nada en el generador**. Cambiaría únicamente
`gate_libros.py` si en el futuro alguien le añade una comprobación de fecha única — hoy no la tiene (revisé las
10 reglas del gate y ninguna mira fechas), así que no hay riesgo de que esta nota lo tumbe. Si se quisiera ir un
paso más allá (no es necesario), se podría añadir a la nota una coletilla explícita tipo «(fecha de la
verificación original, no de este producto)» para que un lector que compare las 201 notas no lo lea como un
descuido — pero el texto actual ya lo explica, así que es una mejora cosmética, no una corrección.

## 3. Defectos nuevos vistos de paso (no estaban en los 24 originales)

1. **`carta-de-apertura-y-escandallo-chocolate.xlsx!Denominaciones y Mínimos!N31:N34`: `%%` literal.** El texto
   que verá el comprador dice «el 25 %% lo comprueba cada bombón…» (doble signo de porcentaje) en las 4 cajas
   surtidas. Es el propio fix de B10 el que lo introduce. Evidencia: `ws['N31'].value` contiene literalmente
   `'...el 25 %% lo comprueba...'` y el cache de `data_only` lo confirma.
2. **`campanas-y-valle-del-ano.xlsx!Peso sobre el Año!A1`**=`'Peso Sobre el Año'` — mismo defecto de Title Case
   que A9 (word list incompleta: falta «sobre»), pero es una instancia nueva no listada en la refutación
   original, así que el helper sigue teniendo el bug para cualquier preposición fuera de la lista corta.
3. **7 de 9 `mapa-*.json` siguen publicando `"_notas"` con `"tipo": "nota"`** (inválido) y un `valor` que no es
   el de la celda (`A8`, hallazgo original, sigue vivo en 7 libros). Ya cubierto en la fila A8 de la tabla, pero
   lo repito aquí porque el mensaje de commit dice «23 fixes en los generadores» sin matizar que 5 de esos 23
   quedaron a medias.
4. **`libro 4 (denominaciones RD 1055/2003)` sigue siendo el libro con peor cobertura de artículo/apartado en
   sus notas legales (38 %, era 0 %)** pese a ser el caso que motivó B8. Si hay que priorizar el trabajo
   pendiente de B8, es el libro por el que habría que empezar.
5. **`calculadora-capex-chocolateria.xlsx` y `campanas-y-valle-del-ano.xlsx` tienen CERO hojas con
   `freeze_panes`**, pese a estar nombrados en el hallazgo A10 original junto con los libros 1, 2 y 3 (que sí se
   arreglaron). No es nuevo como hallazgo, pero sí como dato: el fix de A10 se aplicó de forma muy desigual
   entre generadores (2 de 5 libros con 0 % de progreso, 3 con progreso real).

## 4. Lo que NO se pudo tumbar (confirma que no hay regresión en lo ya sano)

- `gate_libros.py` sigue en verde 9/9 tras los cambios: 0 funciones prohibidas, 0 referencias externas, 0
  celdas verdes vacías, mapas con ≥25 etiquetas válidas, los 8 cruces resuelven a hojas reales y citan
  `!Hoja!Celda` completo.
- Los 3 comportamientos probados con pycel (libro 5, libro 6, libro 8) se mueven exactamente como describen los
  hallazgos A2, A1 y B2 — no son fixes cosméticos de texto, cambian el cálculo real.
- Los 8 cruces cuadran al céntimo/unidad (capacidad, CAPEX depurado, fondo de maniobra, plazo crítico, CAPEX de
  bloque, precio de cobertura) tras las cascadas de B4/A1/A6, sin que ningún CUADRE quede roto.

## 5. Veredicto

**CORREGIR** antes de dar el pack por cerrado — no por los altos (los 4 están bien resueltos y probados por
comportamiento, no sólo por texto), sino porque quedan **6 hallazgos sin resolver del todo** (A8, A9, A10, B4,
B8 parciales; B9 sin tocar) y **1 defecto nuevo** introducido por el propio fix de B10 (el `%%`). Ninguno de
estos 7 puntos es de gravedad alta y todos son arreglos rápidos y acotados (ninguno requiere reabrir el modelo
de datos ni recalcular cascadas), pero dejarlos así incumpliría la propia regla del pack: **cero errores
arrastrados a la siguiente capa**, y aquí la siguiente capa es el guion (`documentos.py`) citando estas mismas
celdas y notas en el texto que lee el comprador.

Vía: Claude Code
