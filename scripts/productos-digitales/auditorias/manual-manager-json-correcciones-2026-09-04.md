# Correcciones al JSON de research — «Manual del Manager de Restaurante»

**Fecha:** 2026-09-04 · **Fichero corregido:** `auditorias/guias-v2-research-sector.json` (clave `datos`, entradas `MM-*`)
**Encargo:** aplicar A1-A13 y A15 de `manual-manager-research-REFUTACION-2026-09-04.md` según las decisiones firmadas
D5-D12 de `manual-manager-SPEC.md`.
**Método:** ninguna cifra sale de memoria. Cada cambio se ha cotejado contra el **texto del BOE** (consolidados y PDF
del día) o contra la **API Tempus del INE**, y las URLs se han comprobado una a una (16/16 responden 200).
**Copia previa (fuera del repo):** `…/scratchpad/guias-v2-research-sector.BACKUP-2026-09-04.json`.

## Recuento

| | Antes | Después |
|---|---|---|
| Entradas totales en `datos` | 155 | **160** |
| Entradas `MM-*` | 52 | **57** |
| `MM-*` sin `url` | 0 | **0** |
| Ids duplicados | 0 | **0** |
| Caracteres de escritura no latina | 0 | **0** |
| Entradas eliminadas | — | **ninguna** |

Verificado además: el orden de las 155 entradas previas se conserva byte a byte, la firma de claves sigue siendo única
para las 160 entradas, y `bloque_research()` de `documentos.py` renderiza los 21 ids tocados con **0 huecos** (MM-21,
MM-24 y MM-25 salen como «REGLA SIN CIFRA» con su norma, que es lo que arregló C2).

## Tabla de cambios

| id | Qué cambió | Fuente verificada | URL |
|---|---|---|---|
| **MM-13** | Se añaden la **excepción** («a menos que no pueda pedirse razonablemente a la empresa que le conceda esta posibilidad»), la **remisión al art. 55.1 ET** (la audiencia previa se suma al expediente contradictorio, no lo sustituye) y la **vigencia desde el 04-09-2026 hasta el 31-12-2030**. Cita literal en `cita_literal`; `fecha_publicacion` = 2026-09-04 | Art. 41.3 del ALEH VI, Resolución de la DGT de 25-08-2026, BOE núm. 219 de 04-09-2026. Texto leído: «…han acordado un nuevo periodo de vigencia, desde el momento de la publicación del presente texto en el BOE hasta el 31 de diciembre del año 2030» | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-18630 |
| **MM-14** | Reescrito: el ALEH VI **tipifica 6 áreas funcionales y 3 grupos profesionales** (art. 15 enumera puestos, art. 16 los encuadra); «jefe/a de restaurante o sala» va en el grupo 1.º del área 3.ª y el **«gerente de centro» está en el bloque de restauración moderna**; «encargado», «director» y «administrador» son **denominaciones de uso**, no categorías del convenio; manda el grupo profesional del contrato y la nómina (art. 11.2). `url` pasa de REGCON al texto del ALEH | Arts. 11.2, 15 y 16 del ALEH VI. Verificado literal: el área 3.ª lista «Restaurante y bar: Jefe/a restaurante o sala… Restauración moderna: Gerente de centro…»; «Administrador» aparece **0 veces** en todo el acuerdo y los únicos «Encargado/a» son los de economato, pisos y mantenimiento | https://www.boe.es/buscar/act.php?id=BOE-A-2023-6344 |
| **MM-16** | Acotación: los **17.094 €/año NO figuran en el RD 126/2026**, son cálculo propio (1.221 × 14 pagas); en la norma constan 40,70 €/día y 1.221 €/mes | RD 126/2026, art. 1 (vía refutación A11, confirmada) | https://www.boe.es/buscar/doc.php?id=BOE-A-2026-3815 |
| **MM-17** | El 23,60 % queda rotulado **«contingencias comunes a cargo de la empresa»** y se prohíbe expresamente presentarlo como «coste-empresa»; remite a MM-53. `cifra`, `tema`, `cita_literal` y `fuente_titulo` (art. 4.a) actualizados | Art. 4.a) de la Orden PJC/297/2026: «Para las contingencias comunes, el 28,30 por ciento, del que el 23,60 por ciento será a cargo de la empresa…» (BOE núm. 79 de 31-03-2026) | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7296 |
| **MM-53** *(nueva)* | **Cotización empresarial total 2026: 32,15 % con indefinido y 33,35 % con temporal.** Desglose completo en `nota` | Orden PJC/297/2026: art. 4.a) CC 23,60 · art. 33.2.a) desempleo 5,50 / 6,70 · art. 33.2.b) FOGASA 0,20 · art. 33.2.c) FP 0,60 · art. 16 **MEI 0,90 total, 0,75 empresa** · art. 4.b) AT/EP por la tarifa de la **DA 61.ª TRLGSS**, que para el **CNAE 56 «Servicios de comidas y bebidas» da 0,80 (IT) + 0,70 (IMS) = 1,50** | https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7296 · https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| **MM-21** | Se añaden las **tres excepciones tasadas** del art. 22.1 LPRL, el **informe previo de la RLT** en las tres, el criterio de menor molestia y el art. 22.4 (la empresa solo recibe conclusiones de aptitud). Literal completo en `cita_literal` | Art. 22.1 y 22.4 de la Ley 31/1995, texto consolidado | https://www.boe.es/buscar/act.php?id=BOE-A-1995-24292 |
| **MM-24** | **Eliminadas como fuente las consultas V3095-17 y V2236-13** (pasan a mención expresa de prohibición). La entrada se apoya ahora en el **art. 17.1 LIRPF**; `url` y `fuente_titulo` cambian de `petete.tributos.hacienda.gob.es` al BOE | Art. 17.1 de la Ley 35/2006: «…todas las contraprestaciones o utilidades, cualquiera que sea su denominación o naturaleza…» | https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764 |
| **MM-25** | Se mantiene el RIRPF y se añade la **norma de cotización**: rige la regla general del **art. 147.1 TRLGSS** («la remuneración total, cualquiera que sea su forma o denominación») porque no hay norma expresa. Literal del RIRPF en `cita_literal` | Art. 76.1.3.º RIRPF, verificado literal; y barrido de texto sobre el TRLGSS consolidado: **«propina» aparece 0 veces** | https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820 · https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724 |
| **MM-26** | Reescrito con **las DOS figuras**: 8 semanas del art. 48 bis **no retribuidas** (art. 45.1.o) y 45.2) **y** 2 semanas del **art. 48.4.c)** —4 en monoparentalidad— hasta los 8 años, **retribuidas** por la prestación por nacimiento (art. 177 LGSS). Literal del 48.4.c) en `cita_literal` | Art. 48 bis y art. 48.4.c) ET (redacción del **RDL 9/2025**, BOE-A-2025-15741, en vigor 31-07-2025) y art. 177 LGSS, que declara situación protegida los descansos «de acuerdo con lo previsto en los apartados 4, 5 y 6 del artículo 48» | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 · https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-15741 |
| **MM-54** *(nueva)* | **Permiso por nacimiento y cuidado de menor: 19 semanas** (32 en monoparentalidad), con su reparto 6 + 11 + 2 y el mismo régimen en adopción, guarda y acogimiento | Art. 48.4 ET: «…suspenderá el contrato de trabajo de la madre biológica y el del progenitor distinto de la madre biológica durante **diecinueve semanas**», redacción del art. 1 del RDL 9/2025 | https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 |
| **MM-36** | **Fecha del *doggy bag* corregida: 15-12-2022 → 22-12-2022.** Se explicitan la **excepción del bufé libre** y la **obligación de informar** de forma clara y visible. Y la exención de 1.300 m² pasa a decir que **solo alcanza al apartado 4**: los apartados 6.1, 6.2, 6.3 y 6.5 obligan a todo restaurante que no sea microempresa (6.6) | Ficha del BOE del RD 1021/2022: disposición 13-12-2022, publicación 21-12-2022, **entrada en vigor 22-12-2022**; art. 18.5 leído literal. Art. 6.4.c) de la Ley 1/2025: «Quedan exceptuadas de **las obligaciones del presente apartado cuatro**…» | https://www.boe.es/eli/es/rd/2022/12/13/1021/con · https://www.boe.es/buscar/act.php?id=BOE-A-2025-6597 |
| **MM-39** | Se añade la **regla de tres casillas** de la factura-e B2B: tique normal fuera, **tique con NIF y domicilio del cliente y cuota separada (simplificada cualificada, art. 7.2 RD 1619/2012) DENTRO**, factura completa dentro | Art. 4.1 del RD 238/2026: «…a menos que se trate de facturas simplificadas cualificadas a las que se refiere el artículo 7.2 de ese mismo Reglamento» (BOE-A-2026-7295, publicado 31-03-2026, en vigor 20-04-2026). Art. 7.2 RD 1619/2012 verificado literal | https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696 · https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-7295 |
| **MM-41** | Se quita **«metodología Sapiens»** del `fuente_titulo` y se advierte de que la fuente **no dice «barra» ni «autoservicio»** (habla de servicio integrado y parcial) y de que **su aritmética no cierra** (30 + 32,5 + 5 + 17 deja 15,5 %, no 10-13 %). Se fecha: **2017, revisado en 2022** | CaixaBankLab × elBullifoundation, «Consumos y beneficios de un restaurante» (hallazgo A11 de la refutación, que leyó el artículo y sus metadatos) | https://www.caixabanklab.com/elbullifoundation/es/consumos-beneficios-restaurante/ |
| **MM-42** | **«19 secciones» → «18 secciones»** (A15) y remisión a MM-57 | API del INE: la EACL publica **18 secciones** más el agregado «Industria, construcción y servicios». Series EACL523 (hostelería, 23.690,02 €) y EACL619 (total, 38.748,94 €) | https://www.ine.es/jaxiT3/Tabla.htm?t=9125 |
| **MM-45** | Acotado: los **+19 pp son solo la franja de las 19:00 h** (11 pp a las 18:00, 15 a las 20:00), y los autores advierten de que **solo ese resultado es significativo**; mesa de cuatro, 36 h antes, San Francisco, datos de 2010 | Anderson y Magruder, *The Economic Journal* 122(563):957-989 (verificado en A11) | https://www.hbs.edu/ris/Publication%20Files/12-016_a7e4a5a2-03f9-490d-b093-8f951238dba2.pdf |
| **MM-46** | Acotado: el **1,92 % → 1,52 % de CoverManager es de UN SOLO DÍA** (Día del Padre de 2025) y solo del subgrupo sin protección; **no es comparable** con el 3,3 % anual de TheFork | Nota de CoverManager vía prensa sectorial (verificado en A11) | https://restauracionnews.com/2026/03/thefork-tasa-de-no-show-33-2025/ |
| **MM-47** | El ticket medio de 21 € pasa a fecharse como **datos de 2024** (media enero-septiembre, artículo del 16-01-2025), no «1S 2025»; se advierte de que **excluye efectivo** y refleja **una sola entidad**. `anio_del_dato` = 2024 | CaixaBank Research (verificado en A11) | https://caixabanklab-campus.com/cual-es-el-ticket-medio-restauracion-espana/ |
| **MM-48** | Serie nacional completa y **etiquetas corregidas**: 76,9 % a 1 año, **63,5 % a 2** (estaba como «a 3»), 55,3 % a 3, 47,5 % a 4 y 41,9 % a 5. Se corrige la premisa: lo que no existe es la tasa de **restaurantes** como subclase, no la de hostelería (→ MM-55). Delectatech queda atribuido por su nombre como fuente privada | Nota de prensa del INE, DAE 2023, cohorte «nacidas en 2018»: 100,0 / 76,9 / 63,5 / 55,3 / 47,5 / 41,9 entre 2018 y 2023 | https://www.ine.es/dyngs/Prensa/DAE2023.htm |
| **MM-55** *(nueva)* | **Supervivencia de la hostelería: 75,6 % a 1 año · 61,6 % a 2 · 53,5 % a 3 · 45,2 % a 4 · 38,8 % a 5**, con el aviso de que la cohorte atraviesa la pandemia | Recalculado sobre el **anexo oficial** del INE sumando CNAE 55 + 56 de la cohorte nacida en 2018: base **34.933** empresas (2.873 + 32.060) y supervivientes 26.421 / 21.534 / 18.695 / 15.792 / 13.549 | https://www.ine.es/dyngs/Prensa/DAE2023.htm · https://www.ine.es/prensa/anexo_tablas/es/DAE2023.xlsx |
| **MM-56** *(nueva)* | **Absentismo de hostelería, 1T 2026**: 132,9 h pactadas, 15,5 no trabajadas, 6,2 de vacaciones y fiestas y **7,9 por incapacidad temporal** → 5,9 % por IT y 7,0 % de absentismo; nacional 5,6 % y 7,3 % | INE, ETCL **tabla 6043** «Tiempo de trabajo por trabajador y mes, tipo de jornada, secciones de la CNAE-09». Series ETCL2486 / 2483 / 2482 / 2481 (hostelería) y ETCL2409 / 2406 / 2536 / 2401 (total), leídas de la API el 2026-09-04 | https://www.ine.es/jaxiT3/Tabla.htm?t=6043 |
| **MM-57** *(nueva)* | **Sueldos y salarios: 17.190,75 € en hostelería frente a 28.410,78 € nacional** (60,5 %), el más bajo de las 18 secciones. Sustituye explícitamente a la comparación 1.512 € / 2.345 € de la cadena Synergie-FOS-Linkers. Incluye el aviso de que **«beneficios sociales» no es variable de la EACL** (211,42 € = 22,22 + 187,83 + 1,37, derivado propio) | INE, EACL 2025: series **EACL522** (hostelería) y **EACL618** (total), leídas de la API el 2026-09-04 | https://www.ine.es/jaxiT3/Tabla.htm?t=9125 |

## Discrepancias detectadas y cómo se han resuelto

1. **Etiquetas de la serie de supervivencia (D9 vs. dato del INE).** La SPEC firmada dice «75,6 % a 1 año, 53,5 % a 2,
   38,8 % a 3» y el encargo repetía «1/2/3 años». **El dato del INE dice otra cosa**: recalculado sobre el anexo
   oficial, esos tres porcentajes son **1, 3 y 5 años**, y el valor a 2 años es **61,6 %**. Como el encargo pedía
   «etiqueta exacta y año de la serie», manda el dato: MM-55 va con 1/2/3/4/5 completos y una nota que deja escrita la
   discrepancia. **Consecuencia para la SPEC:** hay que corregir **D9** y la entrada de la lista negra del §8 («es
   46,5 % a 2 años: 53,5 % supervivencia»), porque el 46,5 % de cierres corresponde a **3 años**, no a 2.
2. **Tipo del MEI 2026 (D5).** La SPEC dice «MEI 0,80 % en 2026»; el art. 16 de la Orden PJC/297/2026 fija **0,90 %
   total, del que 0,75 % es empresarial**. El 0,80 % era el tipo de 2025. MM-53 va con el dato de la Orden.
3. **Tarifa de primas de AT/EP.** El encargo la situaba en la «DA 4.ª de la Ley 42/2006»; ahí nació, pero la Orden de
   2026 remite a la **DA 61.ª del TRLGSS**, que es donde vive hoy. Se cita la DA 61.ª y se explica el origen en `nota`.
4. **MM-42 no era el dato que pedía D9.** «Coste laboral» (23.690,02 €) y «sueldos y salarios» (17.190,75 €) son dos
   variables distintas de la misma encuesta. MM-42 se ha dejado como coste laboral —con el recuento de secciones
   corregido— y el dato salarial ha ido a MM-57.

## Lo que NO se ha podido verificar (y qué se ha hecho)

- **Consultas V3095-17 y V2236-13 de la DGT.** El buscador oficial (`petete.tributos.hacienda.gob.es`) no devuelve
  resultados ni para consultas de control, así que **no se pueden confirmar ni refutar**. Se han retirado como fuente
  de MM-24 y solo quedan nombradas para prohibirlas expresamente. La entrada se sostiene ahora en el art. 17.1 LIRPF y
  el art. 76.1.3.º RIRPF, los dos verificados literalmente.
- **CaixaBankLab (MM-41), CoverManager y TheFork (MM-46), CaixaBank Research (MM-47) y Anderson & Magruder (MM-45).**
  No se han vuelto a abrir en esta pasada: se ha aplicado la acotación que la refutación ya verificó contra la fuente.
  Las cifras no se han tocado; lo que se ha añadido es el **alcance** con el que hay que citarlas.
- **Los 31,1 cierres diarios de Delectatech (MM-48)** siguen siendo fuente privada vía prensa. No se han eliminado
  —no estaban en el encargo— pero quedan atribuidos por su nombre y marcados como no oficiales en la `nota`.

## Fuera del alcance de esta corrección (para quien siga)

- **Linkers / Synergie (1.512 €, 2.345 €, 63,8 % de rotación) y la temporalidad del 12,6 %: no había ninguna entrada
  `MM-*` con esas cifras.** No ha habido nada que borrar ni que degradar a `fiabilidad: baja`; el sustituto primario
  del INE está en MM-57 y la prohibición vive en la lista negra del §8 de la SPEC.
- **`FC-PRIME-01` y `FC-PRIME-02` atribuyen el prime cost del 60-65 % a Toast**, que es justo lo que la lista negra
  prohíbe («Toast recomienda 60-65 %»; su objetivo publicado es «60 % o menos» y el 60-65 % es de Laube /
  RestaurantOwner). Son ids de la **Guía Food Cost, ya publicada**, así que no se han tocado: corregirlos altera el
  research de un producto vivo y debe decidirse aparte.
- **`SMI-02` repite los 17.094 €** sin la advertencia de que son cálculo propio. Mismo motivo: es un id de la familia
  FC. Si se regenera aquel producto, aplicarle la misma acotación que a MM-16.
- El `_meta.totales` del fichero sigue diciendo «datos: 103», heredado del research original de agosto. No se ha
  tocado porque ningún consumidor lo lee, pero está desfasado desde antes de esta sesión (hoy son 160).

Via: Claude Code
