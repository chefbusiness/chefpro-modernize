# Plan de Negocio: Finca de Eventos y Bodas · REVISIÓN ADVERSARIAL FINAL (una pasada)

> Sesión Claude Code, 25-oct-2026. Revisor final antes del Payment Link. Rama `feat/plan-negocio-finca-eventos` en `b1a139ca`
> (Mac = VPS). Leídos en el VPS (`/root/wt-finca`, openpyxl `data_only` + python-docx): los 6 entregables de
> `astro-site/public/dl/plan-negocio-finca-eventos-bodas/`. En el Mac: landing `.ts`, correo, tarjeta del hub, SPEC, F2-NOTAS,
> F1-research y `cifras_caso_es.json`. Las referencias «P##» son el índice de párrafo de python-docx (cuerpo del documento).

**Recuento: 0 B · 9 M · 26 m.** · **Estado tras la ronda única de arreglos (25-oct): 9/9 M arreglados (M7 sin G14) · 24 m arreglados, 2 no aplicados (m13 y la parte Letter de m26: deuda del motor y del generador común). Detalle en `F2-NOTAS.md` § «Revisión final aplicada».**

## Lo que está bien (no tocar)

- Ficheros sanos: los 5 de producto abren; plan y contrato en A4; 0 tokens sin resolver (`{…}`, `__X__`, «PENDIENTE»); 0 errores de
  fórmula en los tres xlsx (734 + 172 + 12 fórmulas; las 52 sin caché del plan financiero son los `""` de F2-NOTAS); ninguna hoja vacía.
- Word = Excel: todas las cifras del Word cotejadas con `cifras_caso_es.json` y con el libro calculado (ventas, neto, inversión,
  necesidad, préstamo, cuota, DSCR, holguras, saldos, partidas, escenarios, personal). Ninguna cifra mal copiada; el único error es de
  interpretación (M1).
- Pagos y cancelación iguales en la calculadora (`Calculadora!B112:C121`, `B124:C128`), el contrato (Quinta, Séptima y anexo de
  empresa) y las instrucciones: 25/35/40 a 180 y 30 días; 30/30/40 a 60 y 15 días; 10/25/50/75/100 y 5/15/35/60/100 en ≥ 12, 6-11,
  3-5, 1-2 y < 1 meses.
- Checklist: 84 tareas = 12/16/15/13/14/14, como dicen el Word (P117), la landing y el hub.
- D11: ni RD 393/2007, ni «carné de manipulador», ni «España 2026», ni cifras de seguro fuera de Andalucía; el canon del 12 % siempre
  como supuesto («negócialo»); el «todo al 10 %» solo como riesgo. Urbanismo de las 4 CCAA con su artículo; Orden INT/1068/2026 con
  su fecha; ruido 55/55/45 dBA; comida testigo ≥ 100 g, ≤ 4 °C o ≤ −18 °C, 7 días, la guarda quien sirve.
- Año 1 con 120 eventos explicado con honestidad en el Word (P43, P95 y P99, con el pesimista).
- IVA de las dos líneas al 21 % (`PyG!G10:G11`, `Tesorería!N16` = 21 % × 364.080 €).
- Hub: tarjeta nueva en la posición 1 con «✨ Nuevo», la de «Próximos» retirada y la sexta degradada a «Nuevo».

---

## B · Bloqueantes

Ninguno. Todos los hallazgos se arreglan con texto o con una regeneración del libro que ya está automatizada (`ciclo.sh` →
`cifras_fin_es.py` → `docx_fin_es.py`).

---

## M · Mayores (dinero, ley o promesa incumplida)

### M1 · Word §8, P96: punto de equilibrio contable con una cifra imposible
- **Estado (ronda única, 25-oct)**: ✅ ARREGLADO (P96, con tokens)
- **Qué**: «El equilibrio contable está en 105 eventos al año, de 72 invitados cada uno, con unos ingresos de 317.157 €».
- **Por qué**: son dos lecturas alternativas del mismo umbral (`Punto Equilibrio!B14:B16`: 8.572 invitados al año = 105 eventos de
  82 **o** 120 eventos de 72). 105 × 72 × 37 € = 279.720 €, no 317.157 €. Un banco lo caza haciendo la cuenta.
- **Arreglo** (P96, primera frase): «El equilibrio contable está en 105 eventos al año del tamaño medio (82 invitados), o en 72
  invitados por evento si mantienes los 120 eventos, con unos ingresos de 317.157 €: deja una holgura del 14,8 % sobre el caso.»

### M2 · Word §3, §8 y §10: el umbral de caja de «98 eventos» infravalora el riesgo desde el año 2
- **Estado (ronda única, 25-oct)**: ✅ ARREGLADO (P59, P96 y P113)
- **Dónde**: P59 («por debajo de 98 eventos del tamaño medio no hay caja»), P96 (última frase, igual) y P113 («por debajo de unos 98
  eventos al año no hay caja»).
- **Por qué**: 98 es el equilibrio de caja del año 1, el de carencia (`Punto Equilibrio!B21`). Con el principal ya en marcha son 113 y
  116 eventos (`C21:D21`; `BE_EVENTOS_CAJA_A2/A3`). El propio Word lo dice en P66 y P96: presentado como «el» umbral, rebaja en 15-18
  eventos el riesgo que el banco va a mirar (holgura de caja del año 2: 14,9 %).
- **Arreglo**:
  - P59: «El mayor riesgo es de ocupación: por debajo de 98 eventos del tamaño medio no hay caja el primer año, y desde el segundo,
    cuando ya devuelves el préstamo, el listón sube a 113 y 116.»
  - P96, última frase: «El riesgo real es de ocupación: por debajo de 98 eventos del tamaño medio el primer año, y de 113 y 116 el
    segundo y el tercero, no hay caja.»
  - P113: «El segundo es la ocupación: por debajo de unos 98 eventos el primer año, y de unos 113-116 desde el segundo, no hay caja.»

### M3 · La preventa del año 1 choca con «nunca vendas fechas sin licencia» (y el contrato no da cómo hacerla)
- **Estado (ronda única, 25-oct)**: ✅ ARREGLADO (regla única en Word, contrato con «Segunda bis», checklist, Supuestos C34/C52, landing y correo)
- **Qué**: el caso cuenta 120 eventos el año 1 porque «las fechas de la primera temporada se venden durante los meses de licencia y
  obra» (Word P43, P95 y P70; landing, tarjeta «Tesorería…»; correo). A la vez, la regla absoluta es no vender fechas sin licencia:
  Word P70 («Nunca vendas fechas sin licencia», en el mismo párrafo que la preventa), P103, P113 y P116; contrato P5 («nunca se
  venden fechas de una finca que no tenga todavía las licencias»); landing `why.reasons[0]` y FAQ 1; correo. El contrato con los novios
  (cláusula Segunda, P21) solo contempla una finca que **ya** tiene licencia, así que la preventa del año 1 no tiene contrato.
  Además, `0. Supuestos!C34` dice que «la primera temporada se vendió antes de tener la licencia y llega corta»: contradice la regla
  y los «120 eventos completos» a la vez. `C52` («sólo trae lo que se vendió desde la licencia») choca con la preventa durante la obra.
- **Por qué**: es la premisa que sostiene el año 1. El checklist ya tiene la regla buena (`F2 - Finca y licencia!E14`: «Antes de la
  licencia, sólo reservas con devolución íntegra pactada por escrito»). Hay que unificarla.
- **Arreglo** (regla única: «no se confirma ninguna fecha en firme sin licencia; antes, solo reservas condicionadas con devolución
  íntegra»):
  - Word P70, desde «Lo más importante…»: «Lo más importante de la primera temporada es esto: las fechas se reservan durante los
    meses de licencia y obra, antes de abrir, como reservas condicionadas a la licencia y con devolución íntegra pactada por escrito si
    no llega a tiempo. Nunca confirmes una fecha en firme sin licencia.»
  - Word P103: «Y una regla sin excepciones: no confirmes fechas en firme sin licencia; antes de tenerla, solo reservas condicionadas
    con devolución íntegra.» · P113: «… y la regla de no confirmar fechas sin licencia (antes, solo reservas condicionadas con
    devolución íntegra).»
  - Contrato P5, «Tercera»: «Tercera: no se confirma en firme ninguna fecha de una finca que todavía no tenga las licencias; mientras
    tanto, solo se firman reservas condicionadas a la licencia (cláusula segunda bis), con devolución íntegra si no llega.»
  - Contrato, cláusula nueva tras la Segunda: «Segunda bis · Reserva condicionada a la licencia [solo si la Finca aún no la tiene]. Este
    contrato queda sujeto a la condición suspensiva de que la Finca obtenga las licencias del evento antes del [fecha límite, al menos
    seis meses antes del evento]. Mientras no se cumpla, la Finca solo cobra la reserva de la cláusula quinta. Si la condición no se
    cumple en esa fecha, el contrato queda sin efecto y la Finca devuelve al Cliente todo lo cobrado en un plazo de [14] días, sin
    retención ni penalización para el Cliente [y con una compensación de [importe] €].»
  - `0. Supuestos!C34`: «El primer año, solo intereses: es el año de arranque y la caja va más justa. Desde el segundo año se devuelve
    el principal: mira la holgura de caja de ese año en el Punto de Equilibrio.» · `C52`: «… las bodas se reservan con 12-18 meses de
    antelación y la primera temporada solo trae lo que se reservó, condicionado a la licencia, durante la tramitación y la obra. Con
    100 % se elimina la rampa.»
  - Landing `why.reasons[0]` y FAQ 1, y correo: «… y no se confirma ninguna fecha sin licencia» en lugar de «no se venden fechas sin
    licencia».

### M4 · «El primer invierno se atraviesa con el fondo de maniobra»: falso según la Tesorería del propio libro
- **Estado (ronda única, 25-oct)**: ✅ ARREGLADO (P57, P97 y Supuestos C35, con tokens)
- **Dónde**: Word P57 («El saldo de caja más bajo, 51.025 €, llega en abril, el mes 2 […], y ese primer invierno hay que atravesarlo
  con el fondo de maniobra») y P97 («El primer invierno se atraviesa con el fondo de maniobra»); `0. Supuestos!C35` («son el colchón
  del primer invierno»).
- **Por qué**: con el Mes 1 = marzo, el primer invierno son los meses 9-12 y la caja está en 143.471 / 149.770 / 147.889 /
  149.910 € (`Tesorería 12 meses!J22:M22`). Lo que aguanta el fondo es la primavera de arranque (mínimo en abril). Las propias
  `Instrucciones!A10` lo dicen bien: «llega al primer invierno con la caja de la temporada». Un banco lee la fila 22.
- **Arreglo**:
  - P57, desde «El saldo…»: «El saldo de caja más bajo, 51.025 €, llega en abril, el mes 2, recién pagada la inversión y antes de que
    entren las bodas de mayo y junio: esa primavera de arranque se sostiene con el fondo de maniobra de 59.629 €. Después la temporada
    sube la caja hasta 149.910 € en el mes 12, y con ella se atraviesa el primer invierno.»
  - P97, penúltima frase: «La primavera de arranque se sostiene con el fondo de maniobra, y el primer invierno, con la caja que deja
    la temporada; por eso la preventa de fechas es la tarea más rentable de los primeros meses.»
  - `0. Supuestos!C35`: «Tres meses de costes fijos: son el colchón de los primeros meses, recién pagada la inversión y antes de las
    bodas de mayo y junio. En un año normal, de noviembre a febrero entra alrededor del 23 % de la venta con la renta y la plantilla
    planas: ese invierno se pasa con la caja de la temporada.»

### M5 · Word §9, P109: arts. 90.2 y 103.l del TRLGDCU citados para lo que no dicen
- **Estado (ronda única, 25-oct)**: ✅ ARREGLADO (P109)
- **Qué**: «la señal y las penalizaciones deben ser proporcionales y recíprocas (TRLGDCU, arts. 85.6, 87.2, 90.2 y 103.l)».
- **Por qué**: 85.6 (indemnización desproporcionada) y 87.2 (retener sin reciprocidad) sí fundan eso. El 90.2 es el fuero (abusiva la
  sumisión a un juzgado distinto del del domicilio del consumidor) y el 103.l es la excepción al desistimiento en servicios de
  esparcimiento con fecha fija. El contrato (Décima y Vigesimoprimera) y el checklist (`F6!E7:E8`) los aplican bien; el Word no.
  Un abogado lo caza en la primera lectura.
- **Arreglo** (P109, segunda frase): «En el contrato con los novios, la señal y las penalizaciones deben ser proporcionales (TRLGDCU,
  art. 85.6) y recíprocas (art. 87.2); la cláusula de jurisdicción no puede llevar al consumidor a un juzgado distinto del de su
  domicilio (art. 90.2), y si contratas a distancia, el servicio con fecha fija queda fuera del derecho de desistimiento (art. 103.l).»

### M6 · Contrato, cláusula Sexta (P37): «arras penitenciales del art. 1454» con efectos que no son los del 1454
- **Estado (ronda única, 25-oct)**: ✅ ARREGLADO («señal a cuenta del precio», sin art. 1454)
- **Qué**: la reserva se califica de arras penitenciales del art. 1454 CC, pero el Cliente que desiste pierde «lo que corresponda según
  la cláusula de cancelación» (10-100 %, no la señal del 25 %) y la Finca que desiste devuelve y compensa por la tabla (no «devolverlas
  duplicadas»).
- **Por qué**: la reciprocidad interna está bien (Séptima ↔ Octava), pero el nombre y los efectos chocan. En un contrato con consumidor
  la cláusula oscura se interpreta a su favor (TRLGDCU art. 80.2; CC art. 1288): el Cliente podría reclamar la señal duplicada (+25 %)
  si la Finca cancela con 12 meses o más, cuando la tabla dice +10 %. Hay que decir que los efectos pactados sustituyen a la regla
  general, o no llamarlas penitenciales.
- **Arreglo** (Sexta, segunda frase; conserva la decisión de usar arras): «Con ellas, y con estos efectos pactados, que sustituyen a
  la pérdida de las arras o a su devolución duplicada de la regla general del artículo 1454, el Cliente puede desistir del contrato
  pagando lo que fija la cláusula séptima, y la Finca puede desistir devolviendo lo cobrado e indemnizando al Cliente con lo que fija
  la cláusula octava.»

### M7 · Notas del IVA del motor sin adaptar: «el alcohol servido en la finca va al reducido»
- **Estado (ronda única, 25-oct)**: ✅ ARREGLADO C39, C40 y O16 · ⏸ G14 NO (deuda del motor: `IVA_COMPRAS` solo admite «comida»; sin efecto, coste del canon = 0)
- **Dónde**: `0. Supuestos!C40` («lo usan dos cosas: el IVA que soportas al comprar el alcohol […] y el que repercutes por el alcohol
  que sale por intermediarios (es una entrega de bienes). El alcohol servido en la finca va al reducido») y `Tesorería 12 meses!O16`
  («en la finca, alcohol incluido, el reducido […]; el alcohol que sale por intermediarios, al general»). Menores en el mismo bloque:
  `0. Supuestos!B39/C39` («IVA repercutido de restauración 10 % · Tipo reducido de hostelería», que en este plan no usa nada) y
  `PyG 3 Años!G14` (10 % en la línea del canon).
- **Por qué**: contradicen D4 justo en las dos celdas que explican el IVA del libro, y `C62:C63` del mismo libro dicen que la finca no
  vende bebida. Un asesor fiscal lo lee como error del plan.
- **Arreglo** (en el contenido `a.py` o en la semilla, no en código común):
  - `C40`: «Tipo general. En este plan es el de todo lo que factura la finca (espacio, servicios y canon) y el de casi todo lo que
    compra. La finca no vende comida ni bebida: el menú y la barra los factura el catering, al 10 %.»
  - `O16`: «Cada línea de venta a SU tipo, leído de la columna de IVA del P&L: el espacio, los servicios y el canon de la finca, al
    general (21 %). La finca no vende comida ni bebida: el menú y la barra los factura el catering, al 10 % (art. 91.Uno.2.2.º de la
    Ley 37/1992).»
  - `C39`: «No se usa en este plan: la finca no vende comida ni bebida. Es el tipo del menú del catering.» · `G14`: 0,21 (o vacía).

### M8 · `Inversión Inicial!E8`: IVA sobre tasas, licencia y prestación compensatoria
- **Estado (ronda única, 25-oct)**: ✅ ARREGLADO (rótulo «Licencias, tasas…»: el motor marca «No»; D9 VERDE)
- **Qué**: la partida «Calificación urbanística, licencia, tasas y prestación compensatoria o canon» (10.000 €) lleva «Sí» en IVA, y la
  nota `D33` de la misma hoja dice «Las tasas y licencias no están sujetas». Tasas, ICIO, prestación compensatoria (LISTA art. 22.5) y
  canon de la DIC (TRLOTUP art. 221) no llevan IVA.
- **Por qué**: infla en 2.100 € el IVA de la inversión (51.194 €) y la necesidad de caja (362.603 €): conservador, pero es un error
  fiscal visible en la hoja que el banco pide, y contradice su propia nota.
- **Arreglo**: `E8` = «No» en la semilla y regenerar (`ciclo.sh` → `cifras_fin_es.py` → `docx_fin_es.py`). Queda IVA de la inversión
  49.094 €, necesidad 360.503 € y exceso de 2.497 € (0,7 %, dentro del 0-5 % de D9); o bajar el préstamo a 261.000 €. Cambian los
  tokens del Word (P42, P94), `SALDO_MINIMO` y `SALDO_MES12`. Aprovechar la misma regeneración que M3, M4 y M7.

### M9 · Landing, FAQ 9: promete equivalencias que la guía no trae
- **Estado (ronda única, 25-oct)**: ✅ ARREGLADO (FAQ 9 con fianza, aseos, catering y barra libre, que están en la guía; también `integracion.json`)
- **Qué**: «la «finca de eventos» es «salón de eventos», «jardín de eventos», «hacienda» o «quinta» según el país, la «señal» es
  «seña» en Argentina y «anticipo» en México y Colombia, y la «barra libre» es «open bar»…».
- **Por qué**: en `guia-equivalencias-plan-negocio-finca-eventos-bodas.docx` no hay ninguna entrada de «finca de eventos», «señal»,
  «seña», «anticipo», «salón/jardín de eventos», «canon», «wedding planner», «novios» ni «montaje» (0 apariciones; las de
  «hacienda» y «quinta» son de Hacienda y de otros contextos). Solo «barra libre = open bar» existe. Es una promesa concreta de la
  página de venta que el comprador latinoamericano va a buscar.
- **Arreglo** (opción barata, con entradas que sí están en la guía): «Por ejemplo, la «fianza» del arrendamiento es el «depósito en
  garantía» en México o Colombia (allí la «fianza» es una póliza), los «aseos» son «baños», el «catering» es «banquetería» en Chile o
  Argentina, y la «barra libre» es «open bar» en casi todas partes.» Alternativa: añadir esos términos de eventos al censo de la guía
  (`equivalencias-es/datos/matriz.json`) y regenerarla.

---

## m · Menores (estilo, erratas, coherencia fina)

**Word del plan (`plan-de-negocio-finca-eventos-bodas.docx`)**
1. [✅] **P43, P98, P112**: «Más de 3 años» con mayúscula en mitad de frase (token `PAYBACK`). → «La inversión se recupera en más de 3
   años.» · «Sobre el payback: más de 3 años; …» · «… y el payback, de más de 3 años.»
2. [✅] **Artículo y preposición con porcentajes** (token pegado sin «el/del»): P40 «que suponen 78 % de las ventas» → «el 78 %»; «un canon:
   22 % de las ventas» → «el 22 %»; P43 y P112 «La holgura de caja es de 22,9 % … baja a 14,9 % … es de 18,1 %» → «del 22,9 % … al
   14,9 % … del 18,1 %»; P62, P72 y P113 «una comisión de 12,5 %» → «del 12,5 %»; P62 «aportan 20 % de las ventas» → «el 20 %»; P87
   «La cobertura de horas es de 101 %» → «del 101 %»; P96 «una holgura de 22,9 %» → «del 22,9 %».
3. [✅] **P108**: «El espacio lleva el 21 % de IVA (21 %) y el canon, también (21 %)» → «El espacio y los servicios del evento llevan el
   21 % de IVA, y el canon, también; el menú del catering va al 10 %.»
4. [✅] **P44**: «te acompaña una plantilla pequeña de 7 personas, contratada como fijos discontinuos» contradice P86 y `Personal`: las 7
   te incluyen a ti, y solo coordinación y auxiliares son fijos discontinuos. → «… y te acompaña un equipo pequeño (7 personas contigo
   incluido, con la coordinación y los auxiliares como fijos discontinuos) que se ocupa del montaje, la limpieza y el aparcamiento.»
5. [✅] **P50** dice que el Excel hace crecer «el número de eventos equivalentes», y P95, que «lo que crece es el tamaño medio del evento».
   → P50, última frase: «Importa mirar el evento completo y no solo el precio: el crecimiento de los años 2 y 3 sale de más actividad
   con el mismo precio por invitado, no de subir tarifas.»
6. [✅] **P55**: «unas 4.000 búsquedas al mes con «finca»» (la palabra suelta tiene muchas más) → «unas 4.000 búsquedas al mes de fincas
   para bodas y eventos».
7. [✅] **P73 y P76** repiten el presupuesto de marketing (12.000 € + 6.000 € de lanzamiento). → En P73, quitar «El marketing del caso es de
   12.000 € al año, más el lanzamiento de 6.000 € dentro de la inversión inicial».
8. [✅] **P80**: «Añade el office (16.000 €) […] y una fosa séptica dimensionada para el aforo […] si tu presupuesto no las recoge, falta
   algo», y el caso no tiene partida de fosa (`Inversión Inicial!A7:A28`). → «… y el saneamiento (fosa séptica o depuradora
   dimensionada para el aforo, que en el caso va dentro de los aseos y de los imprevistos de obra; un vertido nuevo puede pedir
   autorización de la confederación hidrográfica: compruébalo).»
9. [✅] **P117**: «tres tramos de 90 días» y describe las semanas 1-13 (un solo tramo de 90 días). → «El plan de acción de los primeros 90
   días tiene tres tramos.»
10. [✅] **P105 y P106**: «Comunitat Valenciana»; la landing, el checklist y el Excel dicen «Comunidad Valenciana» / «C. Valenciana».
    → «Comunidad Valenciana».
11. [✅] **P106** (y `Instrucciones!B44`, `F2 - Finca y licencia!E16`): «5.000 al aire libre» → «5.000 al aire libre en recinto delimitado»
    (sin delimitar, 20.000; research §0.2).
12. [✅] **P57 y P97**: la rampa «empieza en el 45 %» y el año factura los 120 eventos; falta decir que la rampa solo reparte la venta dentro
    del año (por eso febrero del año 1 vende más que un febrero de crucero). → Añadir en P97: «La rampa no quita ventas al año: solo las
    reparte hacia el final, como llegan las reservas de una finca nueva.»

**Plan financiero (`plan-financiero-finca-eventos-bodas.xlsx`)**
13. [⏸ deuda del motor] `Personal!C11` = 3,35 (`SUM(C5:C10)`, sin ponderar por personas) frente a las 3,75 jornadas del Word (P87) y de las 6.900 horas
    (`I11`). Arrastra `Escenarios!B24:D24` (invitados por jornada, divididos entre 3,35). → `SUMPRODUCT(B5:B10,C5:C10)`; si la fórmula es
    del molde común, anotarlo como deuda del motor y no tocarla aquí.
14. [✅] `Instrucciones!D37`: «Las 30 bodas son unas 21 en sábados de temporada (el 80 %)» → «unas 24 (el 80 %)» o «unas 21 (el 70 %)».
15. [✅] `Instrucciones!D42` dice boda 12 h; `Personal!J20`, 13 h. → Unificar en 13 h.
16. [✅] `Instrucciones!A12`: «la calculadora de presupuestos y los modelos de contrato usan las cifras de este Excel» (la calculadora tiene
    sus propias tarifas). → «El Word usa las cifras de este Excel; la calculadora y los contratos usan los mismos porcentajes de cobro y
    de cancelación. Si cambias una celda verde, el Excel manda.»
17. [✅] `Inversión Inicial!D17` (y `F3 - Obra y equipamiento!E15`): «250 sillas» con un aforo de 300 invitados sentados
    (`0. Supuestos!C51`). → «300 sillas» o «250 sillas; las de las bodas grandes, de alquiler».
18. [✅] `Inversión Inicial!D8`: la partida de 10.000 € cita la prestación compensatoria andaluza del 10 %, que con esta obra serían unos
    13.000 € por sí sola. → Añadir: «En Andalucía, solo la prestación serían unos 13.000 € con la obra del caso: súbela si es tu
    comunidad.»
19. [✅] `Tesorería 12 meses!O5` e `Instrucciones!D35`: «la obra y la licencia se hacen en otoño e invierno» (unos 6 meses), y el Word dice
    6-12 meses o más solo hasta la licencia. → «La licencia (de 6 a 12 meses o más) y la obra se cierran antes del invierno, y se abre
    con las comuniones y la empresa de primavera.»
20. [✅] `Personal!A6/J6` y `F4 - Personal y catering!E5`: coordinación fija discontinua «de marzo a noviembre», con el 7,7 % de la
    actividad en diciembre (comidas de Navidad) y el 7,8 % entre enero y febrero. → «con llamamientos según el calendario de fechas
    vendidas (de marzo a diciembre en el caso)», o decir que en invierno coordina el titular.

**Modelos de contrato (`modelo-contrato-reserva-finca-eventos.docx`)**
21. [✅] **Séptima (P40-P44) y anexo (P93)**: «De 6 a 11 meses · De 3 a 5 · De 1 a 2» deja huecos (11,5 o 2,5 meses); la calculadora usa
    [6, 12), [3, 6) y [1, 3). → «Con 12 meses o más · De 6 meses a menos de 12 · De 3 meses a menos de 6 · De 1 mes a menos de 3 · Con
    menos de 1 mes».
22. [✅] **Tercera (P25, P27)**: «El precio del espacio y los servicios se calcula sobre ese mínimo» y cobra los invitados de más «al precio
    unitario», mientras la calculadora da el espacio a tanto alzado. → P25: «Mínimo garantizado: [número] invitados, que el Cliente
    contrata con el Catering y sobre el que se calculan el menú y la logística del día.» P27 como opcional: «[Si la Finca cobra por
    invitado: los que excedan del mínimo se facturan a [importe] € más IVA por persona, en la factura de liquidación.]»
23. [✅] **Décima (P52)**: «el derecho de desistimiento previsto en el artículo 103.l» (el 103.l es la excepción, no el derecho; y solo opera
    a distancia o fuera del establecimiento). → «Si este contrato se celebra a distancia o fuera de las instalaciones de la Finca, el
    Cliente no tiene derecho de desistimiento (art. 102), porque es un servicio de esparcimiento con fecha de ejecución determinada
    (art. 103.l del TRLGDCU).» Mismo matiz en `F6 - Temporada y eventos!E7`.
24. [✅] **Decimonovena (P78)**: obliga al Catering («que las asume ante el Cliente») en un contrato que el Catering no firma. → «La
    seguridad alimentaria, la información de alérgenos y la comida testigo corresponden al Catering, que contrata el menú directamente
    con el Cliente (cláusula primera).»
25. [✅] **Séptima, tramo de menos de 1 mes (100 %)**: retener el 100 % sin descontar lo que la Finca se ahorra (coste directo, extras al
    40 %) es atacable por desproporcionado (art. 85.6), y la propia cláusula invoca la proporcionalidad. Opcional, más defendible:
    «Con menos de 1 mes: 100 % del precio, descontados los costes que la Finca se ahorra por no celebrarlo (limpieza, consumibles,
    personal de refuerzo y servicios extra no prestados).»

**Correo y transversal**
26. [✅ (correo) · ⏸ Letter = deuda transversal] Correo (`broadcast-…-lanzamiento-es.html`, párrafo del cross-sell): «allí lo cuentan entero» → «allí lo contamos entero». ·
    Transversal, sin acción en este PR: la guía de equivalencias va en tamaño carta (21,6 × 27,9 cm) en todos los productos (comprobado
    en 4 hermanos); es deuda del generador común, no de este producto.

---

## Orden de arreglo propuesto (una tanda)
1. Semilla y `a.py` (M7, M8, M3 en `C34/C52`, M4 en `C35`, m13-m20) → `ciclo.sh` → `cifras_fin_es.py` (gates D9) → `docx_fin_es.py`.
2. Textos del Word (M1, M2, M3, M4, M5, m1-m12) en `textos/fin_es_{a,b}.json` → reensamblar y pasar `barrido_es.py`.
3. Contrato (M3, M6, m21-m25) en `textos/contrato_es.json`. Landing (M3, M9) y correo (M3, m26).
4. Comprobación: grep de «Más de», «Comunitat», «arras», «98 eventos», «primer invierno» y «alcohol» sobre los textos regenerados.
