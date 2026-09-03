# Verificación fiscal — Bloque §3 de `guia-food-cost-SPEC.md` (2026-09-03)

Encargo: confirmar o corregir, contra la fuente primaria (Ley 37/1992 del IVA, texto consolidado,
`boe.es/buscar/act.php?id=BOE-A-1992-28740`), las cuatro afirmaciones del §3 de la SPEC del producto
«Guía Food Cost + Ingeniería de Menú», más el criterio DGT sobre take away/delivery. No se ha escrito
código: es una verificación documental.

**Método:** WebFetch directo a `boe.es` devolvió el texto de la ley truncado antes de llegar al
Título VII (el documento consolidado supera lo que el conversor HTML→Markdown puede procesar de una
vez). Se contrastó en su lugar contra dos reproducciones literales del texto consolidado —
**Iberley** (`iberley.es/legislacion/articulo-9{0,1}-ley-impuesto-sobre-valor-anadido-iva`, que cita
el BOE artículo por artículo y marca vigencia) y **SuperContable** — y se confirmó la fecha de la
última modificación de cada artículo. Para el criterio de take away/delivery se localizó y verificó
la consulta vinculante de la DGT que resuelve exactamente ese supuesto (V2254-22).

## Veredicto: SPEC §3 CORRECTA en sus cuatro afirmaciones. Un error menor fuera de §3 (en D4, §1)

---

## 1. El 10 % de los servicios de hostelería «para consumir en el acto», alcohol incluido

**CONFIRMADO.** Art. 91.Uno.2.2.º, texto literal (vía Iberley, artículo marcado «Vigente», última
modificación registrada Ley 7/2024 de 20-dic-2024, en vigor 22-12-2024 — sin cambios en este párrafo
desde entonces):

> «Los servicios de hostelería, acampamento y balneario, los de restaurantes y, en general, el
> suministro de comidas y bebidas para consumir en el acto, incluso si se confeccionan previo encargo
> del destinatario.»

El apartado no distingue por tipo de bebida: al ser un **servicio** (no una entrega de bienes), la
exclusión de bebidas alcohólicas del art. 91.Uno.1.1.º —que sí aplica a las entregas— no opera aquí.
Es la razón por la que en sala el alcohol también va al 10 %, tal y como dice la SPEC. La nota de
`escandallo-maestro!I31` que la SPEC ordena no extrapolar fuera de sala es coherente con esta lectura:
el 10 % «con alcohol incluido» es un rasgo del **servicio en sala**, no un tipo general del alcohol.

## 2. Take away/delivery sin servicio = entrega de bienes; comida al 10 %, alcohol y refrescos azucarados al 21 %

**CONFIRMADO**, con cita normativa y jurisprudencia administrativa.

**Base legal.** Art. 91.Uno.1.1.º, párrafo introductorio (vía Iberley):

> «Las sustancias o productos, cualquiera que sea su origen que, por sus características,
> aplicaciones, componentes, preparación y estado de conservación, sean susceptibles de ser habitual
> e idóneamente utilizados para la nutrición humana o animal, de acuerdo con lo establecido en el
> Código Alimentario y las disposiciones dictadas para su desarrollo.»

Y las exclusiones, mismo artículo:

> «Se excluyen de lo dispuesto en el párrafo anterior: a) Las bebidas alcohólicas. Se entiende por
> bebida alcohólica todo líquido apto para el consumo humano por ingestión que contenga alcohol
> etílico. b) Las bebidas refrescantes, zumos y gaseosas con azúcares o edulcorantes añadidos.»

Lo excluido cae al tipo general. Art. 90: «El impuesto se exigirá al tipo del 21 por ciento, salvo lo
dispuesto en el artículo siguiente.» → **21 %** para ambas exclusiones, confirmando la SPEC.

**Vigencia de la exclusión b) (refrescos/zumos/gaseosas azucarados/edulcorados):** la SPEC dice
«vigente desde 1-ene-2021 (Ley 11/2020)». Confirmado — Ley 11/2020, de 30 de diciembre, de
Presupuestos Generales del Estado para 2021 (art. 69), con efectos desde el 1 de enero de 2021 e
indefinidos; antes de esa fecha estas bebidas tributaban al 10 % junto con el resto de alimentos.
Fuente: Agencia Tributaria, nota de novedades normativas de la Ley 11/2020.

**Criterio DGT sobre take away/delivery como entrega de bienes** (lo que pedía el encargo, punto 4):
consulta vinculante **V2254-22**, de 26 de octubre de 2022 (Dirección General de Tributos), normativa
citada: Ley 37/1992 arts. 4, 5, 8, 11, 90, 91-Uno-1-1.º y 91-Uno-2-2.º. Hechos: entidad que elabora y
fabrica platos y comida para envío al domicilio del cliente, junto con bebidas, pedidos por web/app,
entrega por repartidores subcontratados — el supuesto exacto de take away/delivery de restauración.
Contestación, cita literal:

> «Cuando no se preste ningún otro servicio auxiliar, se considerarán como entrega de comidas
> preparadas que suponen una entrega de bienes, tributando igualmente al tipo reducido del 10 por
> ciento en virtud del artículo 91.Uno.1.1.º»

> «También tributarán al tipo reducido del 10 por ciento las entregas de bebidas, con excepción de
> las bebidas alcohólicas y las bebidas refrescantes, zumos y gaseosas con azúcares o edulcorantes
> añadidos, que quedan sujetas al tipo general del 21 por ciento.»

Esta consulta reproduce, palabra por palabra, el criterio que la SPEC atribuye al bloque take
away/delivery: coincide en la calificación (entrega de bienes), en el tipo de la comida (10 %) y en
la excepción de alcohol y bebidas azucaradas/edulcoradas (21 %). URL de una reproducción íntegra de la
consulta (el buscador oficial `petete.tributos.hacienda.gob.es` dio error de certificado TLS en el
fetch automático; el contenido se confirmó vía réplica de asesoría fiscal, la cita es idéntica al
extracto que ya circula citando la consulta en fuentes profesionales — Lefebvre, Fiscal-Impuestos):
`https://www.asesoriasoledadalcaracejos.es/consulta-V2254-22-tipo-iva-venta-comida-bebidas-a-domicilio/tipo-iva-venta-comida-bebidas-a-domicilio.html`
(ficha con número, fecha y normativa citada verificables) y el registro oficial en
`https://petete.tributos.hacienda.gob.es/consultas/?num_consulta=V2254-22`.

## 3. El 4 % del pan, harinas panificables, leche, quesos, huevos, frutas, verduras, hortalizas, legumbres, tubérculos, cereales y aceites de oliva (RDL 4/2024, efectos 1-ene-2025)

**CONFIRMADO en su totalidad**, con una corrección menor de cita (ver abajo, no afecta al contenido
del producto). Art. 91.Dos.1.1.º, texto literal completo (vía Iberley):

> «1.º Los siguientes productos: a) El pan común, así como la masa de pan común congelada y el pan
> común congelado destinados exclusivamente a la elaboración del pan común. b) Las harinas
> panificables. c) Los siguientes tipos de leche producida por cualquier especie animal: natural,
> certificada, pasterizada, concentrada, desnatada, esterilizada, UHT, evaporada, en polvo y
> fermentada. d) Los quesos. e) Los huevos. f) Las frutas, verduras, hortalizas, legumbres, tubérculos
> y cereales, que tengan la condición de productos naturales de acuerdo con el Código Alimentario y
> las disposiciones dictadas para su desarrollo. g) Los aceites de oliva.»

Coincide letra por letra con la lista de la SPEC (pan común, harinas panificables, leche, quesos,
huevos, frutas/verduras/hortalizas/legumbres/tubérculos/cereales, aceites de oliva).

**Aceite de oliva — cronología confirmada:** el aceite de oliva no estaba en esta lista antes de
2024. El Real Decreto-ley 4/2024, de 26 de junio (BOE-A-2024-12944, art. 2), lo incorporó con una
rampa transitoria: **5 %** del 1-jul al 30-sep-2024, **2 %** del 1-oct al 31-dic-2024, y **4 %
permanente (tipo superreducido, integrado en el art. 91.Dos.1.1.º) desde el 1 de enero de 2025**, con
independencia de la variedad (virgen extra, virgen o refinado). Coincide con lo que dice la SPEC
(«RDL 4/2024, con efectos 1-ene-2025») y es el tipo vigente hoy (sept-2026).

**Corrección de cita (fuera de §3, en §1 → D4):** la SPEC dice «art. 91.Dos.1.1.º.**f**» para el
aceite de oliva. Confirmado contra el texto literal del RDL 4/2024 y contra el artículo consolidado:
la letra correcta es **g)**, no f). La letra f) es «frutas, verduras, hortalizas, legumbres,
tubérculos y cereales» (preexistente); el RDL 4/2024 añadió el aceite de oliva como una letra **nueva**,
la g), sin renumerar las anteriores. La tabla del §3 no cita la letra (solo «art. 91.Dos.1.1.º», que es
correcto), así que el error no afecta al contenido publicable de la guía ni a los xlsx — solo a la
referencia interna de la decisión D4. Recomendación: cambiar «art. 91.Dos.1.1.º.f» por «art.
91.Dos.1.1.º.g» en D4 al escribir o revisar el capítulo 04 (donde se cita la base legal del 4 %).

## 4. Regla de cálculo: food cost sobre venta neta y coste neto de IVA soportado

Esto es mecánica general del IVA (deducción del soportado en el modelo 303, no un tipo específico) y
no requiere cita de un artículo de tipos: es correcto y estándar — el IVA soportado en compras
deducible no es coste para la empresa, es tesorería que se recupera vía autoliquidación. No hay nada
que corregir aquí; se confirma sin reservas.

---

## Resumen del veredicto por fila del §3

| Fila de la SPEC | Veredicto | Base verificada |
|---|---|---|
| Sala, alcohol incluido, 10 % | ✅ Correcto | art. 91.Uno.2.2.º literal |
| Take away/delivery comida, 10 % | ✅ Correcto | art. 91.Uno.1.1.º literal + DGT V2254-22 |
| Take away/delivery alcohol, 21 % | ✅ Correcto | exclusión a) art. 91.Uno.1.1.º + art. 90 + DGT V2254-22 |
| Take away/delivery refresco/azucarada, 21 % | ✅ Correcto | exclusión b) art. 91.Uno.1.1.º (Ley 11/2020, 1-ene-2021) + DGT V2254-22 |
| Compras 4 % (lista + aceite de oliva) | ✅ Correcto | art. 91.Dos.1.1.º a)-g) literal; aceite por RDL 4/2024 desde 1-ene-2025 |
| Compras 10 % resto de alimentos | ✅ Correcto | regla general art. 91.Uno.1.1.º (todo lo no excluido) |
| Compras 21 % (alcohol, azucaradas, no alimentario) | ✅ Correcto | art. 90 (tipo general, residual) |
| **D4 (§1): cita «art. 91.Dos.1.1.º.f» para aceite de oliva** | ⚠️ **Corregir** | Es la letra **g)**, no f — confirmado contra el texto del RDL 4/2024 |

**No se requiere ningún cambio en el texto ni en las fórmulas del §3.** La única corrección es de cita
interna (letra del apartado) en la decisión D4, sin efecto en el contenido que verá el cliente.

---

## Entradas listas para el research JSON de la familia (`FC-*`)

```json
[
  {
    "id": "FC-IVA-01",
    "tema": "IVA restauración — servicio en sala",
    "dato": "Los servicios de hostelería y el suministro de comidas y bebidas para consumir en el acto tributan al tipo reducido, alcohol incluido (es un servicio, no una entrega de bienes, así que no aplica la exclusión de bebidas alcohólicas).",
    "cifra": 10,
    "unidad": "%",
    "anio_del_dato": "2026",
    "fuente_titulo": "Ley 37/1992, art. 91.Uno.2.2.º (texto consolidado)",
    "url": "https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740",
    "fecha_publicacion": "1992-12-29 (última modificación de este apartado: Ley 7/2024, en vigor 22-12-2024)",
    "cita_literal": "Los servicios de hostelería, acampamento y balneario, los de restaurantes y, en general, el suministro de comidas y bebidas para consumir en el acto, incluso si se confeccionan previo encargo del destinatario.",
    "fiabilidad": "alta",
    "nota": "Fuente primaria consultada vía reproducción literal (Iberley) por límite de tamaño del BOE en fetch automático; artículo marcado vigente."
  },
  {
    "id": "FC-IVA-02",
    "tema": "IVA restauración — take away y delivery de comida",
    "dato": "La comida elaborada entregada sin servicio de hostelería (para llevar o a domicilio) es una entrega de bienes y tributa como alimento ordinario.",
    "cifra": 10,
    "unidad": "%",
    "anio_del_dato": "2026",
    "fuente_titulo": "Ley 37/1992, art. 91.Uno.1.1.º + DGT, consulta vinculante V2254-22",
    "url": "https://petete.tributos.hacienda.gob.es/consultas/?num_consulta=V2254-22",
    "fecha_publicacion": "2022-10-26",
    "cita_literal": "Cuando no se preste ningún otro servicio auxiliar, se considerarán como entrega de comidas preparadas que suponen una entrega de bienes, tributando igualmente al tipo reducido del 10 por ciento en virtud del artículo 91.Uno.1.1.º",
    "fiabilidad": "alta",
    "nota": "Consulta vinculante DGT sobre el supuesto exacto (plataforma de reparto a domicilio). Vinculante para la Administración, criterio consolidado."
  },
  {
    "id": "FC-IVA-03",
    "tema": "IVA restauración — take away y delivery de alcohol",
    "dato": "Las bebidas alcohólicas quedan excluidas del tipo reducido de alimentos cuando se entregan sin servicio de hostelería (para llevar o a domicilio); tributan al tipo general.",
    "cifra": 21,
    "unidad": "%",
    "anio_del_dato": "2026",
    "fuente_titulo": "Ley 37/1992, arts. 90 y 91.Uno.1.1.º + DGT, consulta vinculante V2254-22",
    "url": "https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740",
    "fecha_publicacion": "1992-12-29",
    "cita_literal": "Se excluyen de lo dispuesto en el párrafo anterior: a) Las bebidas alcohólicas. Se entiende por bebida alcohólica todo líquido apto para el consumo humano por ingestión que contenga alcohol etílico.",
    "fiabilidad": "alta",
    "nota": "La misma bebida alcohólica va al 10 % si se consume en sala (servicio, art. 91.Uno.2.2.º) y al 21 % si se lleva sin servicio (entrega de bienes excluida)."
  },
  {
    "id": "FC-IVA-04",
    "tema": "IVA restauración — take away y delivery de refrescos/zumos/gaseosas azucarados o edulcorados",
    "dato": "Los refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos quedan excluidos del tipo reducido de alimentos desde el 1 de enero de 2021; tributan al tipo general.",
    "cifra": 21,
    "unidad": "%",
    "anio_del_dato": "2026",
    "fuente_titulo": "Ley 37/1992, art. 91.Uno.1.1.º, redacción dada por la Ley 11/2020 de Presupuestos Generales del Estado 2021 (art. 69)",
    "url": "https://www.boe.es/buscar/act.php?id=BOE-A-2020-17339",
    "fecha_publicacion": "2020-12-31 (efectos desde 2021-01-01)",
    "cita_literal": "Se excluyen de lo dispuesto en el párrafo anterior: [...] b) Las bebidas refrescantes, zumos y gaseosas con azúcares o edulcorantes añadidos.",
    "fiabilidad": "alta",
    "nota": "Antes del 1-ene-2021 estas bebidas tributaban al 10 % junto con el resto de alimentos; el cambio no afecta a los zumos/refrescos SIN azúcares o edulcorantes añadidos, que siguen al 10 %."
  },
  {
    "id": "FC-IVA-05",
    "tema": "IVA compras — aceite de oliva",
    "dato": "El aceite de oliva (virgen extra, virgen o refinado) tributa al tipo superreducido desde el 1 de enero de 2025, tras una rampa transitoria en el segundo semestre de 2024 (5 % jul-sep, 2 % oct-dic).",
    "cifra": 4,
    "unidad": "%",
    "anio_del_dato": "2026",
    "fuente_titulo": "Ley 37/1992, art. 91.Dos.1.1.º.g, incorporado por el RDL 4/2024, de 26 de junio (art. 2)",
    "url": "https://www.boe.es/diario_boe/txt.php?id=BOE-A-2024-12944",
    "fecha_publicacion": "2024-06-27 (efectos permanentes desde 2025-01-01)",
    "cita_literal": "g) Los aceites de oliva.",
    "fiabilidad": "alta",
    "nota": "La letra correcta dentro del art. 91.Dos.1.1.º es la g), no la f) (la SPEC D4 dice f; corregir). La f) preexistente es frutas/verduras/hortalizas/legumbres/tubérculos/cereales."
  },
  {
    "id": "FC-IVA-06",
    "tema": "IVA compras — lista completa al tipo superreducido",
    "dato": "Pan común, harinas panificables, leche (todos los tipos listados), quesos, huevos, frutas, verduras, hortalizas, legumbres, tubérculos, cereales y aceites de oliva tributan al tipo superreducido en la compra.",
    "cifra": 4,
    "unidad": "%",
    "anio_del_dato": "2026",
    "fuente_titulo": "Ley 37/1992, art. 91.Dos.1.1.º, letras a) a g) (texto consolidado)",
    "url": "https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740",
    "fecha_publicacion": "1992-12-29 (última incorporación: RDL 4/2024, letra g, efectos 2025-01-01)",
    "cita_literal": "1.º Los siguientes productos: a) El pan común [...] b) Las harinas panificables. c) Los siguientes tipos de leche [...] d) Los quesos. e) Los huevos. f) Las frutas, verduras, hortalizas, legumbres, tubérculos y cereales [...] g) Los aceites de oliva.",
    "fiabilidad": "alta",
    "nota": "Lista cerrada (numerus clausus): cualquier alimento no listado aquí y no excluido por el art. 91.Uno.1.1.º va al 10 % ordinario, no al 4 %."
  },
  {
    "id": "FC-IVA-07",
    "tema": "IVA — tipo general",
    "dato": "El tipo general del IVA, aplicable por defecto salvo que un producto o servicio caiga en el art. 91 (reducido/superreducido), es del 21 %.",
    "cifra": 21,
    "unidad": "%",
    "anio_del_dato": "2026",
    "fuente_titulo": "Ley 37/1992, art. 90 (texto consolidado)",
    "url": "https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740",
    "fecha_publicacion": "1992-12-29",
    "cita_literal": "El impuesto se exigirá al tipo del 21 por ciento, salvo lo dispuesto en el artículo siguiente.",
    "fiabilidad": "alta",
    "nota": "Es el tipo residual: bebidas alcohólicas, refrescos/zumos azucarados o edulcorados fuera de sala, packaging y menaje (no alimentario), y todo lo no comprendido en el art. 91."
  },
  {
    "id": "FC-IVA-08",
    "tema": "IVA restauración — criterio DGT sobre take away/delivery",
    "dato": "La DGT, en consulta vinculante sobre una plataforma de reparto a domicilio, confirma que la entrega de comida sin servicio auxiliar es entrega de bienes al 10 %, y que las bebidas se benefician del mismo 10 % salvo alcohol y refrescos/zumos/gaseosas azucarados o edulcorados, que van al 21 %.",
    "cifra": 10,
    "unidad": "%",
    "anio_del_dato": "2026",
    "fuente_titulo": "Dirección General de Tributos, consulta vinculante V2254-22",
    "url": "https://petete.tributos.hacienda.gob.es/consultas/?num_consulta=V2254-22",
    "fecha_publicacion": "2022-10-26",
    "cita_literal": "También tributarán al tipo reducido del 10 por ciento las entregas de bebidas, con excepción de las bebidas alcohólicas y las bebidas refrescantes, zumos y gaseosas con azúcares o edulcorantes añadidos, que quedan sujetas al tipo general del 21 por ciento.",
    "fiabilidad": "alta",
    "nota": "Hechos del caso: empresa que fabrica y envía comida a domicilio por app, con repartidores subcontratados — el supuesto exacto de delivery de restauración que cubre el cap. 15/03 de la guía."
  }
]
```

---

## Nota sobre acceso a fuentes

`boe.es` rechazó dos fetches directos por límite de tamaño (el documento consolidado de la Ley
37/1992 es demasiado largo para el conversor HTML→Markdown en una sola pasada; el Título VII —tipos—
queda después del corte) y `petete.tributos.hacienda.gob.es` (buscador oficial de consultas DGT) dio
error de certificado TLS en el fetch automático de esta sesión. Ninguno de los dos bloqueos afectó a
la verificación: el texto de los artículos 90 y 91 se contrastó contra **Iberley**, que republica el
texto consolidado del BOE artículo por artículo con su fecha de vigencia, y el contenido de la
consulta V2254-22 se confirmó por su número, fecha exacta (26-oct-2022) y normativa citada
coincidentes en tres fuentes independientes (resultados de búsqueda agregados, réplica de asesoría
fiscal con ficha completa, y menciones cruzadas en fuentes profesionales). Si se necesita el PDF/HTML
oficial exacto de la consulta para archivo, la vía es `petete.tributos.hacienda.gob.es` desde un
entorno sin ese problema de certificado, o el buscador de consultas de la Agencia Tributaria.

Via: Claude Code
