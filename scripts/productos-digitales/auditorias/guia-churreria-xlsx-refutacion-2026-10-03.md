# Refutación de los 8 libros de Excel — «Cómo Montar una Churrería-Chocolatería» (2026-10-03)

> Refutador adversarial de los xlsx de `scripts/productos-digitales/guia-churreria/build/`, UNA ronda y tres lentes en un
> solo pase: **(A) convenciones y aritmética**, **(B) coherencia entre libros y con `datos_ejemplo.py`** y **(C) legal y
> frontera**. El encargo era TUMBARLOS. Cada libro se abrió dos veces (fórmulas y `data_only`), uno cada vez; las cadenas
> clave se recalcularon con **pycel** evaluando la salida ANTES de tocar la entrada (32 pruebas). Contrastado contra
> `guia-churreria-SPEC.md` (§1, §2.1-§2.4, §3, §5), `datos_ejemplo.py` importado (`CRUCES`, `rotulo_cruce`, `nota_legal`,
> `IDS_LEGALES_REQUERIDOS`, `IDS_PROHIBIDOS`, `LISTA_NEGRA`, `RX_ID`), `auditorias/guia-churreria-verificacion-legal-2026-10-03.json`
> (46 fichas CUN), la de la hermana (CHN), `guias-v2-research-sector.json` (837 ids) y los ocho `mapa-*.json`. Térmica:
> `istats cpu temp` antes de cada python, uno cada vez, máximo registrado **49,1 °C**. No se ha tocado ningún xlsx ni
> generador, ni `datos_ejemplo.py`; sin commit.
>
> **Veredicto: CORREGIR ANTES.** 23 hallazgos: **1 alto · 11 medios · 11 bajos**. El motor está limpio de verdad (0
> funciones prohibidas, 0 referencias externas, 0 divisiones sin `IFERROR`, 0 verdes vacías en 1.892, 0 errores `#` en
> 6.276 fórmulas) y el **contrato de cruces se cumple al 1e-9 en las 52 entradas de `CRUCES`**. Lo que no aguanta es la
> **red de seguridad entre libros**: seis filas de CUADRE de los libros 4 y 8 dicen «CUADRA» con una cifra mal copiada que
> luego viaja al plan financiero (pycel: la renovación de aceite se duplica y la plantilla sube 6.675 € sin un aviso).
> Además hay **un cruce no declarado** en el 6, **tres conceptos con doble fuente**, una **decisión de la SPEC sin
> veredicto** («¿una churrera o dos?»), **una celda que imprime un rótulo** en la ficha de visita, **dos notas legales
> que publican lo vetado** (media cuota del 676 y art. 8 de la norma de aceites) y **texto interno de la fábrica** a la
> vista del comprador en cinco libros.

## 0. Lo que NO se pudo tumbar (verificado, no asumido)

| Comprobación | Resultado |
|---|---|
| Fórmulas | **6.276** (libro 1: 90 · 2: 614 · 3: 1.303 · 4: 177 · 5: 748 · 6: 1.138 · 7: 445 · 8: 1.761) |
| Errores `#…` en `data_only` | **0** |
| Fórmulas sin caché | 98 (2 · 39 · 1 · 7 · 38 · 0 · 6 · 5), **todas** la convención «sin dato» = `""`: revisadas por patrón (segunda freidora en «No», líneas que no se compran, columnas «¿es tu ciclo?», franjas sin noche, filas libres del registro, avisos vacíos) |
| Funciones prohibidas (`INDIRECT` · `COUNTA` · `PMT` · `OFFSET` · `XLOOKUP` · `LET` · `LAMBDA` · `RANK` · `NETWORKDAYS` · `IRR`) | **0** (y 0 `MEDIAN`). La cuota del 6 es la anualidad escrita a mano (`Financiación!B24`); el orden de eventos del 5, con `COUNTIF` |
| Referencias entre libros (`[`, `.xlsx` dentro de fórmula) | **0** |
| Divisiones sin `IFERROR` | **0** |
| Constantes en fórmula | Sólo 0/1, `ROUND(…,2)`, conversiones de unidad (`/1000` g→kg, `/60`, `*12` docena, `/100` g por 100 g, `MOD(…,12)` de meses) y `SMALL(…,2)`. Ningún IVA, umbral, kW ni %. El `100*` de `3!Mix…!L12` es el hallazgo R-14 |
| Verdes | **1.892**; **0 vacías, 0 bloqueadas, 0 con fórmula**; 0 celdas no verdes desbloqueadas con valor |
| DV | **0 listas con comas**, **0 sin `showErrorMessage`** |
| Formato condicional | 1 comparación sin `ISNUMBER` (R-19) |
| Formatos | 0 decimales en `General`, 0 fechas sin formato de fecha |
| WinAnsi | **0** caracteres fuera de cp1252, **0** U+202F/U+2011 |
| A4 y protección | Todas las hojas `paperSize 9`; todas protegidas **sin contraseña** |
| Metadata | `creator` y `lastModifiedBy` = `AI Chef Pro`; `title` y `subject` (`… · Versión 1.0 · octubre 2026`) en los 8 |
| Instrucciones | Primera hoja en los 8; «Celdas verdes = campos editables», línea `Versión 1.0 · octubre 2026 · aichef.pro/guia-churreria-chocolateria · info@aichef.pro`, bio anclada, «Desproteger hoja (no tiene contraseña)» y el orden 3 → 1 → 4 → 5 → 8 → 2 → 6 (+7) en los 8 (el 7, como tabla) |
| Contrato `CRUCES` | **52/52**: rótulo en K y valor en L de la hoja de origen = `valor_defecto` (tol. 1e-9); en el receptor, exactamente una celda con `rotulo_cruce(c)` y su verde con ese valor; **una fila de CUADRE por celda cruzada** (1 · 3 · 10 · 7 · 7 · 24 = 52); todas las celdas de origen están en su mapa |
| Cruces no declarados por rótulo | **0** «cópialo del libro» / «trae aquí la cifra de» fuera de `CRUCES` (el no declarado de R-04 va sin rótulo) |
| Fronteras de concepto | Precio del aceite sólo en `3!Parámetros!G34` (el 2 y el 4, por X17/X2); fondo de maniobra sólo en `6!Inversión Inicial!B19`; renta nace en `2!Parámetros!B12`; demanda base sólo en `1!Día Tipo…!B6:C6`; franjas sólo en el 5; ninguna celda «gastos fijos» ni «renta» en el 5; ningún comentario «con IVA» en el 3 |
| Lista negra y ids prohibidos | **0** coincidencias de `LISTA_NEGRA` (incluida la temperatura) en texto y comentarios; **0** ids de `IDS_PROHIBIDOS`. Los 75.000 de `2!Franquicia…!B12:B13` son Kukuchurro y ChurroWay (`CUS-M19/M20`), no Maestro Churrero (que va con 115.000, `CUS-M14`) |
| Notas legales | **203** comentarios «Verificado el …»; **todos los ids de `IDS_LEGALES_REQUERIDOS` presentes en cada libro que la SPEC les asigna** (0 faltas); 0 ids citados inexistentes en las fichas |
| Legal de fondo | ET art. 36.1 (22-6 h, ≥ 3 h o 1/3) separado del plus del convenio (22-0 h +1 %, 0-8 h +25 %, umbral 5 h) en `8!Parámetros!B37:B49`; Ley 12/2012 art. 3.3-3.4 en la 1.ª fila de `7!Checklist!K7`; bombona < 15 kg «de utilización móvil» sólo en la feria (`7!Licencia…!A12`, `A36`); acrilamida con parte A sólo si fríes patatas y parte B sólo con suministro centralizado (`7!Alérgenos…!B35:B36`); Ley 7/1996 arts. 54-55 en ferias; CTE nota 2/3 con umbrales «más de» bien aplicados (pycel: 20 kW exactos = «no es local de riesgo especial»); ninguna temperatura de fritura del churro |
| Frontera con otros productos | Pack APPCC 09 citado por fichero y hojas reales (`Control Aceite`, `Retirada de aceite usado`, comprobadas en `dl/pack-appcc/`); «Kit Gestión de Personal y Turnos» con su nombre de catálogo; el 8 dice que es la semana TIPO, no el cuadrante de cada semana |
| Mapas | 54 · 67 · 65 · 53 · 87 · 88 · 72 · 65 etiquetas (libros 1…8); 0 refs malformadas, 0 hojas inexistentes, 0 valores distintos del `data_only`, tipos válidos |
| pycel (32 pruebas) | Mueven lo que tienen que mover: 1 (masa X1 → capacidad y L5; segunda freidora → 53 kW, «Riesgo alto», X9 = 1, cuba 50 L), 2 (freidora 2.500 → bloque 3 y X10; X9 = 1 → +2.800 €; traspaso 70.000 → «Sale mejor el TRASPASO»), 3 (garrafa → X2, X2 bis, X11; absorción; cacao 30 % → aviso de consumo; caja con IVA → mix 1,318), 4 (precio → X12 y escenario), 5 (raciones → X13, X16; elegir ferias → «REVISA»), 6 (CAPEX → inversión y CUADRE; plantilla → resultado y punto de equilibrio; cerrar → −27.713), 7 (30 semanas → «NO LLEGAS» y maquinaria crítica; sin consumo en local → Anexo «Sí»; eléctrica → potencia), 8 (12 pagas, X6 = 3 → 16 huecos, base, SMI). **Las que NO mueven lo que deberían están en R-01** |

---

## Hallazgos


### R-01 · ALTO · Seis filas de CUADRE de los libros 4 y 8 dicen «CUADRA» con una copia mal hecha
**Libro(s):** 4 y 8 · **Celda(s):** `aceite-de-fritura-coste-y-cambio.xlsx!Parámetros!B49,B53 · turnos-plantilla-y-madrugada.xlsx!Parámetros!B74:B79`

**Problema.** Las filas de CUADRE de 6 cruces de los libros 4 y 8 no pueden detectar una copia mal hecha: comparan identidades o cotas (masa por ración ≤ 1/(1−absorción); reposición punta ≤ cuba; personas ≥ máximo del cuadrante; suma de franjas = horas con mínimo; 0 ≤ refuerzo ≤ horas de apertura), no la cifra copiada contra la que publica el origen. SPEC §2.2 exige que la fila avise «si lo tecleado se aleja del origen». El error pasa en silencio al libro 6 por X12 y X15.

**Evidencia.** pycel, salida evaluada ANTES de tocar la entrada: 4!Parámetros!B16 (cuba, X3) 25→50 ⇒ B53 sigue «CUADRA» y Consumo y Reposición!L5 (origen de X12) pasa de 0,028398 a 0,056797 €/ración (×2). 4!B10 (masa, X2 bis) 0,0979→0,2 ⇒ B49 sigue «CUADRA». 8!Parámetros!B12 (refuerzo, X7) 56→560 h ⇒ B79 sigue «CUADRA» y Coste de Plantilla!L5 (origen de X15) sube de 119.350,20 a 126.025,10 €. 8!B8/B10 intercambiados (desayuno/merienda) ⇒ B75 y B77 siguen «CUADRA». Además las tolerancias no son las mismas en la familia: 0,02 en 1, 2, 5 y 6; 0,05 en 4 (B33) y 8 (B62).

**Fix (en el generador).** gen_aceite-de-fritura-coste-y-cambio.py y gen_turnos-plantilla-y-madrugada.py: para CADA celda de cruce, el patrón de los libros 1, 2, 5 y 6 (verde «Lo que publica hoy la celda de origen (anótalo)» con el valor_defecto + desviación relativa + veredicto contra la tolerancia de Parámetros). Las identidades actuales se quedan como filas de «Contraste», no de CUADRE. Tolerancia 0,02 «heredado» en los dos. Añadir al demo() las cuatro pruebas de arriba (deben encender «REVISA»).

### R-02 · MEDIO · La ficha de visita imprime un rótulo en lugar del riesgo de la cocina
**Libro(s):** 1 · **Celda(s):** `produccion-hora-punta-y-local.xlsx!Ficha de Visita a Local!H9`

**Problema.** La columna «Dato de tu proyecto» del eliminatorio 4 («¿Aguanta la potencia y el riesgo de incendio?») apunta al RÓTULO de la fila, no al dato: imprime «Riesgo de la cocina» en la ficha que el lector se lleva a la visita.

**Evidencia.** H9 = 'Freidoras, Potencia y Riesgo'!$B$13 → 'Riesgo de la cocina' (data_only). El dato está en D13 («Riesgo bajo») y los kW en D12 (28). Es la única referencia de toda la familia que apunta a una celda de texto que no es entrada (barrido de las 6.276 fórmulas).

**Fix (en el generador).** gen_produccion-hora-punta-y-local.py: H9 = 'Freidoras, Potencia y Riesgo'!$D$12&" kW · "&'Freidoras, Potencia y Riesgo'!$D$13 (o sólo $D$13). Añadir al demo(): con la segunda freidora en «Sí», H9 tiene que decir «Riesgo alto».

### R-03 · MEDIO · «¿Una churrera o dos?» no tiene veredicto: el 1 remite al 5 y el 5 al 1
**Libro(s):** 1 y 5 · **Celda(s):** `produccion-hora-punta-y-local.xlsx!Cuello de Botella!B17 · temporada-franjas-y-ferias.xlsx!Capacidad contra el Pico!A24`

**Problema.** La decisión «¿Una churrera o dos?» (SPEC §2.1, libro 1) no la resuelve ninguna celda: el libro 1 remite al 5 y el 5 remite al 1. No hay veredicto ni etiqueta de mapa que el capítulo pueda citar.

**Evidencia.** 1!Cuello de Botella!B17 = «Mira el libro 5: allí esta capacidad se cruza con tus franjas». 5!Capacidad contra el Pico!A24: «…y, si no basta, más línea (libro 1)». En 5 sólo hay números (E20 = 1 mes, E22 = 8,70 raciones/h de déficit en diciembre) y Cola del Domingo repite exactamente la misma cifra (F18 = 8,6986). Grep de «churrera», «segunda freidora» en el libro 5: 0.

**Fix (en el generador).** gen_temporada-franjas-y-ferias.py: fila de veredicto en «Capacidad contra el Pico» (p. ej. B23 «¿Una churrera o dos?»): sin meses en déficit → «Una basta»; déficit sólo en días punta y ≤ lo que cubre el refuerzo de «Refuerzo por Pico» → «Una, con refuerzo en el pico»; si no → «Necesitas más línea: activa la segunda freidora en el libro 1 y vuelve a copiar la capacidad (X4)». Etiqueta en el mapa. gen_produccion: B17 cita esa celda exacta.

### R-04 · MEDIO · Cruce no declarado: las partidas no amortizables viajan del 2 al 6 sin rótulo ni CUADRE
**Libro(s):** 6 · **Celda(s):** `plan-financiero-3-anos-churreria.xlsx!0. Supuestos!B52 → Inversión Inicial!B7`

**Problema.** «Partidas del CAPEX que no se amortizan (fianza, stock y marketing)» = 4.668,30 € es una cifra que nace en el libro 2 (bloques 9-11) y entra en el 6 como verde SIN estar en CRUCES, sin rótulo «cópialo del libro 2» y sin fila de CUADRE: un cruce no declarado que escapa al gate de ciclos. Si el lector cambia la fianza, el stock o el marketing en el 2, la amortización del 6 queda mal sin aviso.

**Evidencia.** 0. Supuestos!D52 = «calculado en datos_ejemplo: capex_total() - capex_amortizable()»; E52 «Si tu CAPEX cambia, cambia esta cifra con él». El libro 2 ya publica el dato: CAPEX por Bloque!I45 = 81.747,35 (inmovilizado amortizable, en el mapa) y E42:E44 = 1.820 + 848,30 + 2.000. Inversión Inicial!B8 = B6 − B7.

**Fix (en el generador).** Declarar «X10 bis» (2 → 6, arista ya existente) en datos_ejemplo.CRUCES con origen calculadora-capex-churreria.xlsx!Resumen!L6 = capex_total() − capex_amortizable(); gen_calculadora-capex-churreria.py publica K6/L6; gen_plan-financiero-3-anos-churreria.py recibe con rótulo_cruce() y su fila de CUADRE (la 25.ª).

### R-05 · MEDIO · Tres conceptos con dos fuentes: factor de fritura, precios de insumo y superficie
**Libro(s):** 1, 2 y 3 · **Celda(s):** `1!Parámetros!B17 y 3!Parámetros!B17 · 2!CAPEX por Bloque!F19:F29 y 3!Parámetros!B36:B53 · 1!Parámetros!B6 y 2!Parámetros!B10`

**Problema.** Tres conceptos con dos celdas verdes y sin cruce («un concepto = una fuente»): (a) kilos fritos por kilo de masa 0,9 en los libros 1 y 3, del que depende el CUADRE de identidad del libro 4 (X3 se calcula con el del 1 y X2 bis con el del 3); (b) nueve precios de insumo (cobertura 6,50, cucurucho 0,15, vaso 0,08, papel 0,02, leche 0,85, café 18, infusión 0,06, agua 0,22, caja 0,25) tecleados otra vez en el stock inicial del libro 2; (c) superficie útil 75 m² en los libros 1 y 2.

**Evidencia.** Barrido de verdes numéricas repetidas entre libros (excluidas las filas de cruce y de CUADRE): 0.9 → (1, Parámetros!B17) y (3, Parámetros!B17); 6.5 → (2, CAPEX por Bloque!F19) y (3, Parámetros!B36); 0.15/0.08/0.02/0.22/0.25/0.85/18/0.06 ídem; 75 → (1, Parámetros!B6) y (2, Parámetros!B10). Las notas lo admiten: 1!E17 «no viaja como cruce»; 2!E10 «La MISMA que pusiste en … el libro 1».

**Fix (en el generador).** datos_ejemplo.CRUCES (antes de regenerar): «X1 bis» 3 → 1 kg fritos/kg masa (3!Parámetros!L9); ampliar X17 (3 → 2) a los precios de insumo del stock o reducir el stock del libro 2 a aceite + mix + un importe de «resto de envases y bebidas» supuesto; «X9 bis» 1 → 2 superficie útil (1!Zonas y m²!L5). Todas las aristas ya existen (3→1, 3→2, 1→2). Regenerar 1, 2, 3 y 4 con sus filas de CUADRE.

### R-06 · MEDIO · El 6 no enseña el verano con fijos de las tres salidas
**Libro(s):** 6 · **Celda(s):** `plan-financiero-3-anos-churreria.xlsx!Escenarios!A20:D25`

**Problema.** SPEC §2.1 (libro 6): «“verano: resultado con fijos” de CADA salida en 6!Escenarios». La hoja enseña sólo «cerrar» (−27.713,28 €) y la elegida (−10.344,57 €); la tercera (ferias, −25.606,83 € en datos_ejemplo.verano_con_fijos) no está y A25 remite al libro 5. La decisión 9 del bonus 2 no puede citar las tres con fijos desde un mismo libro.

**Evidencia.** Escenarios!B22 = 0 (cerrar), B23 = 0. Supuestos!B32 (X16, sólo la elegida). 5!El Verano (Tres Salidas)!B16:D16 tiene las tres contribuciones (0 · 17.368,71 · 2.106,45), pero sólo C16 viaja.

**Fix (en el generador).** datos_ejemplo.CRUCES: «X16 bis» 5 → 6 con las contribuciones de las dos salidas no elegidas (o de las tres) en 5!El Verano (Tres Salidas)!L6:L8; gen_temporada publica el bloque K/L; gen_plan-financiero añade la tercera fila con su resultado con fijos y su CUADRE.

### R-07 · MEDIO · La nota del 676 publica en un Excel la cláusula de la media cuota
**Libro(s):** 7 · **Celda(s):** `checklist-legal-fritura-y-licencias.xlsx!Árbol IAE y CNAE por Formato!A15 (comentario)`

**Problema.** La nota legal del 676 (CUN-10) publica, en el comentario de la celda, la cláusula de la media cuota: «…Cuando los establecimientos clasificados en este epígrafe permanezcan abiertos al público durante seis...». D14/A3 (SPEC §1.A): la nota del 676 entra sólo como una línea del cap. 09 «y en ningún Excel»; §5.1.8 veta la media cuota.

**Evidencia.** Comentario de A15 = datos_ejemplo.nota_legal('CUN-10'), que añade la frase con «epígrafe» de la ficha (ventana de _cita_articulo). La ficha CUN-10 de la verificación legal dice «PROHIBIDO» en su nota. El constructor L7 lo declaró y no lo corrigió.

**Fix (en el generador).** gen_checklist-legal-fritura-y-licencias.py: nota propia para CUN-10 = «Verificado el 03-10-2026 · RDLeg 1175/1990 (tarifas del IAE), grupo 676 «Servicios en chocolaterías, heladerías y horchaterías» · URL» (sin la nota de temporada). Mejor aún, en datos_ejemplo.nota_legal(): para CUN-10 no ampliar con _cita_articulo (el «grupo 676» ya es epígrafe). Gate: «seis» y «media» ausentes de todo comentario del libro 7.

### R-08 · MEDIO · La nota de CUN-03 cita el art. 8 derogado de la norma de aceites
**Libro(s):** 4 y 7 · **Celda(s):** `aceite-de-fritura-coste-y-cambio.xlsx!Consumo y Reposición!G18 · checklist-legal-fritura-y-licencias.xlsx!Alérgenos y Aceite Compartido!A41 (comentarios)`

**Problema.** La nota de CUN-03 cita «arts. 8-9» de la Norma de aceites calentados de 1989. El art. 8 está derogado (RD 176/2013) y §5.1.5 prohíbe citarlo; el texto visible está bien, pero la referencia normativa que lee el comprador nombra el artículo vetado.

**Evidencia.** Ambos comentarios: «Verificado el 03-10-2026 · Orden de 26 de enero de 1989 … arts. 8-9 · https://www.boe.es/buscar/act.php?id=BOE-A-1989-2265». La ficha CUN-03: «Los arts. 7, 8, 10, 11 y 12 están derogados … el art. 9 sigue vivo» y «El producto NO puede citar el art. 8 como regla».

**Fix (en el generador).** Nota sobrescrita en gen_aceite-de-fritura-coste-y-cambio.py y gen_checklist-legal-fritura-y-licencias.py: «… art. 9 (vigente; los arts. 7, 8, 10, 11 y 12 los derogó el RD 176/2013, art. 46) · URL». O corregir fuente_titulo en la verificación legal y regenerar. Gate: regex «arts?\. ?8\b» = 0 en comentarios.

### R-09 · MEDIO · Texto interno de la fábrica a la vista del comprador en cinco libros
**Libro(s):** 2, 5, 6, 7 y 8 · **Celda(s):** `6!0. Supuestos!D43:D62,D78,E49 · 8!Parámetros!E20,E21,D27,D28 · 8!Cuadrante por Franja!A23,A32 (com.) · 2!CAPEX por Bloque!P7,P9,L18 · 2!Variante del Formato!I8 · 2!Franquicia o Independiente!G16 · 5!Punto Muerto por Evento!B6 (com.) · 7!Ferias y Venta Ambulante!A16 (com.)`

**Problema.** Texto interno de la fábrica visible para el comprador de un producto de 65 €: rutas de ficheros de OTRO producto, nombres de funciones Python, códigos de decisión y hallazgo, y un «PROHIBIDO» de la verificación legal. El libro 3 sí lo limpió (NOTAS_PUBLICAS); los otros cinco no.

**Evidencia.** 6!0. Supuestos!D49 «heredado: guia-chocolateria/datos_ejemplo.py PARAMS[meses_colchon_fondo_maniobra]» (13 filas así en la hoja principal de supuestos); D60 «calculado en datos_ejemplo: principal_prestamo()»; E49 «(D16)». 8!E20 «(V-01, rama A)»; E21 «(SR-04)»; comentario A32 «datos_ejemplo.TURNOS … Los tres casos de A1». 2!P7 «(N-4)», P9 «(SR-11)», L18 «(V-06)», Variante!I8 «(D2)», G16 id «CUS-D6». 5!B6 «(D2)». 7!Ferias!A16 «(PROHIBIDO citar cualquier artículo del RD 199/2010 (lo siguen citando ordenanzas y blogs: ver CUN-36).)», que sale de nota_legal('CUN-19').

**Fix (en el generador).** Llevar a los cinco generadores el saneador del libro 3 (regex que quita paréntesis con código y traduce «heredado: guia-chocolateria/…» a «heredado de la Guía de la Chocolatería, supuesto declarado»; «calculado en datos_ejemplo» → «calculado»). Para CUN-19, nota propia sin la frase del analista. Gate en cada cierre: 0 coincidencias de r"\b(?:SR|V|N|D|A)-?\d+\b|datos_ejemplo|guia-chocolateria/|PROHIBIDO|rama [AB]|\(\w+\(\)\)" en texto visible y comentarios (los ids CUN/CUS/CHN de fuente sí valen).

### R-10 · MEDIO · Granizado y horchata para llevar al 21 % afirmado como regla
**Libro(s):** 3 · **Celda(s):** `carta-de-apertura-y-escandallo-churro.xlsx!Parámetros!B9 y E9`

**Problema.** El granizado y la horchata para llevar nacen al 21 % y la nota lo afirma como regla («la exclusión … los lleva al tipo general»). La SPEC (§3.3, V-04 rama B) fija para TODAS las bebidas para llevar celda verde al 10 % con «consulta a tu asesor: … podría ser el 21 %», y no hay ficha que resuelva la horchata (CUN-18: sin consulta DGT; CUN-17 sólo define bebida refrescante).

**Evidencia.** Parámetros!B9 = 0,21; D9 «FC-IVA-04 + CUN-17»; E9 «Granizado y horchata PARA LLEVAR: la exclusión de las bebidas refrescantes con azúcares añadidos del tipo reducido desde el 1-1-2021 los lleva al tipo general.» Frente a B7/B8 (taza y demás bebidas) al 10 % con el aviso de V-04.

**Fix (en el generador).** gen_carta-de-apertura-y-escandallo-churro.py: B9 = 0,10 con el mismo aviso de B7/B8 («zona gris: consulta a tu asesor; con azúcar añadido podría ser el 21 %») o, si se quiere el 21 % por prudencia, registrarlo como decisión en la SPEC y redactar E9 como aviso, nunca como regla.

### R-11 · MEDIO · Franquicias: diferencias y recuentos con bases mezcladas; decisión 12 con dos cifras
**Libro(s):** 2 · **Celda(s):** `calculadora-capex-churreria.xlsx!Franquicia o Independiente!I6:I17, B23:B24`

**Problema.** La hoja resta y cuenta inversiones «desde», «más IVA», «sin obra» o «sin fianzas ni existencias» contra un CAPEX sin IVA y con obra (lista negra §5.2: «mezclar bases de IVA», «“desde” como cifra cerrada»). Además datos_ejemplo.cifras_decisiones()[12] compara las franquicias con la inversión TOTAL (165.468 €, con fondo) mientras el libro que cita la decisión 12 usa el CAPEX (86.416 €): el bonus 2 y la hoja darán cifras distintas.

**Evidencia.** I6:I17 = B − $B$19 (p. ej. I12 Kukuchurro «desde, más IVA» −11.415,65; I16 Churro Planet «sin la obra» −42.415,65); B23 = COUNTIF(B6:B17,"<"&B19) = 8 «por debajo de tu CAPEX». A26 avisa de que no se comparan, pero las columnas lo hacen. DECISIONES[12] → «2!Franquicia o Independiente».

**Fix (en el generador).** gen_calculadora-capex-churreria.py: quitar I6:I17 y B23:B24, o añadir columna verde «¿Base comparable con tu CAPEX? (sí/no)» y calcular diferencias y recuentos sólo para «sí» (por defecto «no» en las «desde»/«más IVA»/«sin obra»). datos_ejemplo.cifras_decisiones()[12]: usar capex_total() (o citar 6!Inversión Inicial!B24 y cambiar la celda de DECISIONES).

### R-12 · MEDIO · Precios de hosteleria10 sin re-comprobar al construir el libro 2
**Libro(s):** 2 · **Celda(s):** `calculadora-capex-churreria.xlsx!Equipamiento Línea a Línea!I6:I19 (fechas y fuentes)`

**Problema.** La SPEC (§3.4 y §1.B) pide re-comprobar y fechar los precios de hosteleria10 (descuentos caducables) AL CONSTRUIR el libro 2; no se hizo: las fechas son la fecha_publicacion de la lectura de L4.

**Evidencia.** Declaración del constructor L2: «Este constructor NO volvió a abrir las tiendas: la re-comprobación con el descuento vigente que pide la SPEC §1.B/§3.4 sigue pendiente». CUS-02 (82.000 € y 910 €/mes) tampoco re-verificado (SR-10, gate de F3).

**Fix (en el generador).** Antes de copiar a dl/: re-leer las fichas CUS-33a, 34c, 35a, 36a, 37a, 39, 41 (y CUS-38), actualizar datos_ejemplo.EQUIPAMIENTO y fechas si cambian, comprobar() (8.618,35 / 9.117,35 al céntimo o nuevas sumas) y regenerar 2 → 6. Si no se puede, nota visible «precio de la ficha el 03-10-2026; los descuentos caducan».

### R-13 · BAJO · Ventas del año con el verano valorado al ticket de invierno
**Libro(s):** 6 · **Celda(s):** `plan-financiero-3-anos-churreria.xlsx!PyG 3 Años!C27:C29 · Punto de Equilibrio!B18`

**Problema.** Las ventas del año (cifra de cabecera del plan y del resumen del BP) valoran julio y agosto con el ticket de invierno porque las ventas del verano no viajan.

**Evidencia.** C28 = 232.130,45 € frente a 232.556,76 € de datos_ejemplo.cuenta_resultados_crucero(); C29 13,85 % frente a 13,82 %. El resultado sí cuadra al céntimo (32.138,75 €).

**Fix (en el generador).** Con el X16 bis de R-06, viajar también las ventas sin IVA de la salida elegida (5!El Verano!C12) y usarlas en C27.

### R-14 · BAJO · El % de sala viaja como 70 y obliga a la constante «Cien»
**Libro(s):** 3 → 6 · **Celda(s):** `carta-de-apertura-y-escandallo-churro.xlsx!Mix y Ticket Canal y Temporada!L12 · plan-financiero-3-anos-churreria.xlsx!0. Supuestos!B14, B46`

**Problema.** El % de sala viaja como 70 (y no 0,70 con 0,0 %), contra la convención de porcentajes de la familia; el 6 necesita una constante «Cien» y quien teclee «70 %» mete 0,7.

**Evidencia.** L12 = IFERROR(100*B10,""); 6!B46 = 100 «Cien». pycel: 6!B14 = 0,7 ⇒ PyG!C23 pasa de 32.138,75 a 32.957,68 € (el CUADRE D97 sí avisa).

**Fix (en el generador).** datos_ejemplo._pct_sala() en fracción; gen_carta: L12 = B10 con 0,0 %; gen_plan-financiero: quitar B46 y dividir por nada. Regenerar 3 y 6.

### R-15 · BAJO · Cruces que hay que copiar y que no mueven ningún cálculo
**Libro(s):** 4 y 8 · **Celda(s):** `aceite-de-fritura-coste-y-cambio.xlsx!Parámetros!B10 · turnos-plantilla-y-madrugada.xlsx!Parámetros!B8:B11`

**Problema.** Cruces que el lector tiene que copiar y que no mueven ningún cálculo: X2 bis (masa por ración) sólo alimenta su propio CUADRE en el 4; las cuatro franjas de X7 sólo alimentan una suma de control y una presentación en el 8.

**Evidencia.** Trazado de referencias: 4!B10 → sólo Parámetros!B41. 8!B8:B11 → Parámetros!B66 y Cuadrante por Franja!B7:B10 (presentación). pycel: intercambiar desayuno y merienda en el 8 no mueve Coste de Plantilla!L5.

**Fix (en el generador).** O se usan (el 4 da litros y € por kg de masa; el 8 reparte refuerzo o mínimos por franja) o se quitan de datos_ejemplo.CRUCES y de la SPEC §2.2 antes de regenerar.

### R-16 · BAJO · Calendario repetido en cuatro libros y con dos modelos de días
**Libro(s):** 4, 5, 6 y 8 · **Celda(s):** `4!Parámetros!B29:B31 · 5!Parámetros!B17:B23 · 6!0. Supuestos!B37:B42 · 8!Parámetros!B53:B55`

**Problema.** Calendario y cierre repetidos en cuatro libros (365 días, 5 días cerrados, meses del verano) y con dos modelos: el 4 usa semana 5/2 sin festivos ni cierre; el 5 y el 6, 244 días tipo + 116 punta en 360 días.

**Evidencia.** 4!Consumo y Reposición!B10 = 292,86 raciones/día medio; 6 multiplica la renovación por 107.400 raciones ⇒ 3.049,99 €/año, frente a 4!B13 × 12 = 3.035,58 €.

**Fix (en el generador).** Días cerrados y festivos como supuesto de UN libro (el 5) con cruce, o el 4 con el mismo calendario 244/116/360 que el 5.

### R-17 · BAJO · Las chocolateras al baño maría suman 3 kW al riesgo de incendio
**Libro(s):** 1 · **Celda(s):** `produccion-hora-punta-y-local.xlsx!Freidoras, Potencia y Riesgo!D11`

**Problema.** Cuenta 3 kW de dos chocolateras al baño maría; la nota (2) de la tabla 2.1 del DB-SI sólo computa aparatos «susceptibles de provocar ignición». El veredicto no cambia, pero publica 28 kW donde serían 25.

**Evidencia.** D11 = 3; D12 = 28; nota de I11 lo reconoce («confirma con tu técnico»). datos_ejemplo.PRODUCCION[kw_otros_aparatos] = 3.

**Fix (en el generador).** Decisión de John: valor por defecto 0 con la nota, o mantener 3 como supuesto prudente declarado. Regenerar 1 (y 2 si cambiase X9).

### R-18 · BAJO · Rótulos «a partir de» con fórmulas «más de» en los umbrales del CTE
**Libro(s):** 1 · **Celda(s):** `produccion-hora-punta-y-local.xlsx!Parámetros!A10:A12`

**Problema.** Los rótulos dicen «a partir de 20/30/50 kW» y las fórmulas usan «más de» (correcto según el CTE: 20 < P ≤ 30…).

**Evidencia.** pycel: con 17 L + 3 kW = 20 kW exactos, D13 = «No es local de riesgo especial», mientras A10 dice «Riesgo especial BAJO a partir de 20».

**Fix (en el generador).** gen_produccion: «Riesgo especial BAJO con más de», «MEDIO con más de», «ALTO con más de».

### R-19 · BAJO · Una regla de formato condicional compara fechas sin ISNUMBER
**Libro(s):** 7 · **Celda(s):** `checklist-legal-fritura-y-licencias.xlsx!Ferias y Venta Ambulante!B10 (formato condicional)`

**Problema.** Única regla de formato condicional con comparación sin ISNUMBER: =AND($B$6="Sí",$B$7<$B$8). Si se borra la fecha, se pinta.

**Evidencia.** Barrido de las reglas de formato condicional de los 8 libros: 1 sin ISNUMBER.

**Fix (en el generador).** =AND($B$6="Sí",ISNUMBER($B$7),ISNUMBER($B$8),$B$7<$B$8).

### R-20 · BAJO · Al titular autónomo se le aplica el Estatuto; siete días a la semana
**Libro(s):** 8 · **Celda(s):** `turnos-plantilla-y-madrugada.xlsx!Nocturnidad ET y Convenio!G8 · Horas del Titular!B6:B15`

**Problema.** Al titular, que el propio juego de datos declara autónomo, se le aplica el Estatuto («¿Trabajador nocturno según el ET?» = «no»); debería decir «no aplica: autónomo». Y el caso publica un titular de 7 días y 52,5 h/semana que el libro marca en rojo: el guion tiene que contarlo o mover un turno.

**Evidencia.** G8 = «no»; PLANTILLA[P1].cotiza_ss_empresa = False; Horas del Titular!B15 «Trabajas los siete días…», B13 = 642,86 h/año, B14 = 8.513,90 €.

**Fix (en el generador).** gen_turnos: si es_titular, G y K = «No aplica (autónomo)». Decisión de guion sobre el día libre del titular (datos_ejemplo.TURNOS).

### R-21 · BAJO · El 86,9 % de margen sobre materia cae en el rango vetado 85-90 %
**Libro(s):** 3 · **Celda(s):** `carta-de-apertura-y-escandallo-churro.xlsx!Los Dos Márgenes!B6`

**Problema.** El margen sobre materia de El Molinete (86,9 %) cae dentro del 85-90 % vetado; verificar_guion no lo caza porque la lista negra sólo busca «85-90» y «85 y 90».

**Evidencia.** B6 = 0,869137 (mapa «Margen sobre materia prima (invierno)»); LISTA_NEGRA de datos_ejemplo.

**Fix (en el generador).** No es un fallo del xlsx: añadir a verificar_guion un patrón que exija «sobre materia prima» + «El Molinete» junto a cualquier 85-90 % y prohíba el redondeo a «85-90 %».

### R-22 · BAJO · «Colchón de caja» en el 2 y «fondo de maniobra» en el 6 para lo mismo
**Libro(s):** 2 y 6 · **Celda(s):** `calculadora-capex-churreria.xlsx!Resumen!K5 · plan-financiero-3-anos-churreria.xlsx!0. Supuestos!A7`

**Problema.** El mismo concepto con dos nombres: el 2 dice «colchón de caja» (para esquivar un futuro gate de texto) y el 6, el que recibe la copia, «fondo de maniobra».

**Evidencia.** 2!K5 «CAPEX de apertura, sin el colchón de caja (lo suma el libro 6)»; 6!A7 «CAPEX de apertura SIN fondo de maniobra».

**Fix (en el generador).** Usar «fondo de maniobra» en los textos del 2 y que gate_libros busque FILAS o BLOQUES que lo calculen, no la cadena.

### R-23 · BAJO · Deuda de datos_ejemplo y slugs en textos visibles
**Libro(s):** datos_ejemplo, 2 y 7 · **Celda(s):** `datos_ejemplo.py (CHECKLIST_LEGAL, HOJAS[6], veredicto_nota_2, INSUMOS[mix_churros]) · 7!Instrucciones!A41,A46 · 2!Variante del Formato!H19`

**Problema.** Deuda del juego de datos que han tenido que esquivar los constructores: 45 días de maquinaria frente a 6 semanas; HOJAS[6] con «Instrucciones» la última; veredicto_nota_2() devuelve «local de riesgo especial no es local de riesgo especial»; la nota «Re-comprobar» de CUS-21 ya resuelta (34,80 € = 1 caja de 24 kg); tolerancia de CUADRE y franjas del plus fuera de PARAMS/CONVENIO. Y slugs en lugar de nombres de producto en textos visibles.

**Evidencia.** Declaraciones de L1, L3, L6, L7 y L8; 7!A41 «pack-appcc, registro 09», A46 «plan-negocio-food-truck y kit-tareas-food-truck»; 2!H19 «plan-negocio-cafeteria».

**Fix (en el generador).** Limpiar datos_ejemplo (sin tocar cifras del caso) y, en los generadores 2 y 7, nombres de catálogo («Pack APPCC», «Plan de Negocio Food Truck»…).

---

## Qué hacer, en orden

1. **Bloqueantes antes de copiar a `dl/`** (fixer sonnet, sólo generadores): R-01, R-02, R-03, R-07, R-08, R-09, R-10, y R-04 en cuanto entre el X10 bis en `CRUCES`.
2. **Necesitan tocar `datos_ejemplo.CRUCES` o la SPEC antes de regenerar** (orquestador): R-04 (X10 bis), R-05 (X1 bis, X17 ampliado, X9 bis), R-06 + R-13 (X16 bis), R-14 (`_pct_sala` en fracción), R-15 (usar o quitar X2 bis masa y X7 franjas). Después, `auditar_ciclos` del futuro `gate_libros.py` con el `CRUCES` nuevo.
3. **Decisiones de John:** R-17 (kW de las chocolateras), R-20 (día libre del titular), R-10 si se prefiere el 21 % para granizado/horchata.
4. **Proceso:** R-12 (re-comprobar hosteleria10 y fechar) antes del guion; R-21 al `verificar_guion.py`.
5. Regenerar en el orden de relleno (3 → 1 → 4 → 5 → 8 → 2 → 6, y el 7), `inject_cache.py` + `data_only` + mapas, y repetir las 32 pruebas pycel de esta ronda (las de R-01 tienen que encender «REVISA»).

**Dudas de los constructores contrastadas:** se confirman (y pasan a hallazgo) L1-«0,9 sin cruce» (R-05), L2-«decisión 12» (R-11), L2-«superficie e insumos» (R-05), L2-«hosteleria10 sin re-comprobar» (R-12), L3-«86,9 %» (R-21), L3-«70 como número» (R-14), L4-«semántica de CUADRE» (R-01), L4-«arts. 8-9» (R-08), L6-«verano de tres salidas» (R-06), L6-«ventas con ticket de invierno» (R-13), L6-«no amortizable sin cruce» (R-04), L7-«CUN-10» (R-07), L7-«CUN-19» (R-09), L8-«titular siete días» (R-20). **No se confirman como problema:** L5-«doble conteo de ferias» (la regla X14 sólo-fuera-del-verano es coherente con X16 y con `datos_ejemplo`; conviene escribirla en la SPEC), L5-«contra» en Title Case (minúscula correcta), L8-«bug de SUMPRODUCT en pycel» (el `+0` no rompe nada en Excel), L2-«MEDIAN» (sustituido por recuento, correcto).
