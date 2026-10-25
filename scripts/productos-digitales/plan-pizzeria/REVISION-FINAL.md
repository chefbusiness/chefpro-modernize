# Plan de Negocio: Pizzería Napolitana ES 1.0 — Revisión adversarial final (cifras · legal · editorial)

> Sesión Claude Code, 25-oct-2026. Una pasada de revisión con tres lentes, sobre los volcados de `dump-es/` (4 entregables), la
> ficha `plan-negocio-pizzeria.ts`, `PlanNegocioPizzeriaDashboard.tsx` y el `emailBody` de `verify-purchase.ts:642-648`,
> contrastados con SPEC D1-D19, F1-research, F2-NOTAS y `cifras_caso_es.json`. Las referencias a la fuente remiten a ficheros
> de `scripts/productos-digitales/`: `a.py` = `planes-v2_0/contenido_plan_negocio_pizzeria/a.py`; `piz_es_a.json` y
> `piz_es_b.json` = `plan-pizzeria/textos/`; la clave del JSON coincide con el `[índice]` del párrafo del Word.
> En esta pasada no se aplicó ningún arreglo: lo aplicado después está en la sección «Aplicado».

**Recuento: 1 B · 8 M · 17 m.** No hay ninguna cifra del Excel que no cuadre. El único bloqueante es una instrucción del Excel
que, si el lector la sigue, le infla el beneficio.

## Lo comprobado que está bien (sin hallazgo)

- **Cifras, recalculadas a mano.** Todas cuadran con el Excel y con los tokens del Word:
  - **Ventas**: 66 × 19,50 × 300 = 386.100 € → 409.266 € → 425.637 €.
  - **Variables**: 32,93 %. Margen bruto: 67,07 %.
  - **Fijos**: 220.138,44 €.
  - **Resultado**: EBITDA 60.083,83 € (15,6 %). Neto 32.996 € / 41.103 € / 41.028 € (8,5 % / 10,0 % / 9,6 %), con el IS al 15 / 15 / 25 %.
  - **Inversión**: 124.200 + 6.050 = 130.250 € → 142.850 € → 194.953 €. IVA: 133.050 × 21 % = 27.940,5 €. Necesidad: 222.893,86 €. Bases de amortización: 66.550 € y 50.700 €; amortización anual, 11.725 €.
  - **Préstamo**: cuota de 32.334,66 € (sistema francés, 6 años tras la carencia). DSCR de 1,929 y 1,884.
  - **Equilibrio**: contable 56,1 → 57 comensales. Caja 53,1 / 60,5 / 62,0 → 54 / 61 / 62. Holguras de 24,3 / 15,7 / 17,4 %.
  - **IVA**: `G11` = 0,07 × 21 % + 0,93 × 10 % = 10,77 %; `G13` = 6,4 %; `G14` = 18,8 %.
  - **Tesorería**: la rampa va de 0,75 a 1,00 en el Mes 4 (diciembre). Saldo mínimo, 61.518,55 € en el Mes 1; cierre, 123.546 €. Payback: 177.554 € < 194.953 € → «Más de 3 años».
  - **Escenarios**: 305.620 € (neto −15.159 €) y 475.190 € (neto 83.786 €).
  - **Personal**: 139.873,44 €. Todas las filas están por encima del SMI a prorrata. Cobertura: 9.154 / 8.775 = 104 %.
  - **Calculadora**: bola a 0,2294 €; Margherita a 1,3233 € sobre 9,09 € = 14,6 %. El checklist suma 12 + 15 + 14 + 13 + 13 + 13 = 80 tareas.
  - **Landing, dashboard y correo**: no hay ninguna cifra movible (ni DSCR, ni payback, ni saldo, ni importe del préstamo).
- **Normas abiertas hoy en origen** (eran las dudosas):
  - **LIVA, art. 91** (API de datos abiertos del BOE, versión del 08-10-2026): el 4 % incluye harinas panificables, quesos y aceites de oliva. La versión que entra en vigor el 01-12-2026 (RDL 29/2026) solo toca el apartado Uno.2.2.º para los apartamentos amueblados, así que no afecta a la pizzería. El hallazgo M2 sale de esta lectura.
  - **Reg. (UE) 2024/1143** (Oficina de Publicaciones): el art. 68.1 protege la ETG contra «uso indebido, imitación o evocación, aunque el nombre protegido esté traducido»; el art. 70 regula el símbolo, la mención «especialidad tradicional garantizada» y «ETG»; el art. 72, los controles; el art. 73, la acreditación de los organismos delegados.
  - **Ley 12/2012, art. 2.2**: deja fuera el «uso privativo y ocupación de los bienes de dominio público».
  - **Ley 1/2025, art. 8**: el cliente se lleva lo que no consume sin coste salvo el envase de plástico de un solo uso, y se le avisa «preferentemente en la carta».
  - **El resto**: se toma el ✅ del research. No aparece en ningún sitio el RD 895/2013 como vigente ni el RD 393/2007.
- **D11 y D12**: ninguna parte llama «napolitana» a la pizza del caso ni usa «certificada», «ETG» o «verace» como sello. El «15-25 %» solo aparece como lo que «circula». No hay restos de tapas, heladería, food truck, eventos o pan común. La venta cruzada usa nombres y precios reales (12 / 12 / 14 €). El tuteo es correcto.

## B — Bloqueantes

| # | Dónde | Texto actual | Arreglo propuesto (literal) | Fuente |
|---|---|---|---|---|
| B1 | `plan-financiero-pizzeria.xlsx` · Instrucciones `A12` (punto 8) | «La calculadora de masa y escandallo del pack va aparte: el coste de cada pizza que te dé es el que tienes que llevar a la celda de coste de la comida de la hoja de Supuestos.» | «La calculadora de masa y escandallo del pack va aparte: no copies el food cost de una pizza en la hoja de Supuestos. La celda «Coste de mercancía sobre las ventas de COMIDA» es la media de TODA la comida (pizzas, entrantes y postres, ponderados por lo que vende cada uno) más la merma, y por eso sale bastante más alta que el food cost de la Margherita.» | `a.py:452-455` (lista `instrucciones`, punto 8) |

**Por qué es B.** `Supuestos!B13` (23,5 %) es la media de toda la comida (pizzas al 20 %, entrantes al 28 %, postres al 25 %) más 1,5 puntos de merma. Si el lector sigue la instrucción y pega ahí el 15 % de la Margherita, el beneficio sube unos 27.000 € al año (≈ 0,82 × 8,5 puntos × 386.100 €). Llevaría al banco un neto falso sacado de nuestra propia instrucción.

## M — Mayores

| # | Dónde | Texto actual | Arreglo propuesto (literal) | Fuente |
|---|---|---|---|---|
| M1 | Word [42], [98] y [111] (el token {PAYBACK} vale «Más de 3 años») | [42] «La inversión se recupera en el plazo que indica Más de 3 años.» · [98] «Sobre el payback del proyecto, la respuesta es: Más de 3 años.» · [111] «… y, sobre el payback, la respuesta es: Más de 3 años.» | [42] «Con lo que genera antes de pagar al banco, la inversión no se recupera dentro de los tres años del plan: el Excel lo marca como «{PAYBACK}» ({PAYBACK_CAPEX} años si solo cuentas lo que compras, sin el fondo de maniobra).» · [98] «El payback del proyecto, antes de la deuda, sale en «{PAYBACK}»: los tres años del plan no bastan para devolver la inversión con el fondo de maniobra incluido (sobre lo que compras, sin el fondo, son {PAYBACK_CAPEX} años).» · [111] «… y el payback, antes de la deuda, queda en «{PAYBACK}».» | `piz_es_a.json` «42» · `piz_es_b.json` «98» y «111» |
| M2 | Regla de IVA del 21 % para la bebida. La LIVA, art. 91.Uno.1.1.º b), dice «bebidas refrescantes, zumos y gaseosas **con azúcares o edulcorantes añadidos**» (leído hoy en el BOE). Con el texto actual, un refresco *zero* para llevar parece ir al 10 % | Word [95] «con alcohol o con azúcares añadidos» · [108] «los refrescos con azúcares añadidos que salen del local» · Excel: Supuestos `A62` «(alcohol y refrescos con azúcar)», `C40`, `C62`, `C63` · PyG `F11` «…con azúcares añadidos…; el agua, el café y los zumos sin azúcar» · Instrucciones `A8` y `D42` · Tesorería `O16` · Calculadora: Instrucciones `A21` «los refrescos con azúcar» · Landing `.ts:53` «con azúcar añadido», `:139` y `:154` «con azúcar» | En todos los casos, «con azúcares añadidos» o «con azúcar» → **«con azúcares o edulcorantes añadidos»**. Excepciones: el rótulo `A62` → «Bebida que compras al 21 % (alcohol y refrescos azucarados o edulcorados) sobre el total de bebida» (`cifras_piz_es.py:73` busca solo `^bebida que compras al 21`, así que no se rompe); `F11`: «…el agua, el café y los zumos sin azúcares ni edulcorantes añadidos…»; la landing en `:139` y `:154`: «los refrescos azucarados o edulcorados» | Word: `piz_es_b.json` «95» y «108» · `a.py:57`, `:61`, `:218-219`, `:278`, `:297`, `:482` · `A8` sale del motor: añade a `VOCABULARIO` la clave `'el alcohol y los refrescos o zumos con azúcares añadidos para llevar'` → `'el alcohol y los refrescos o zumos con azúcares o edulcorantes añadidos para llevar'` (termina en letra) · `calculadora_piz_es.py:558` · ficha `.ts:53`, `:139`, `:154`. Después, un grep de «azúcares añadidos» sin «edulcorantes» tiene que dar 0 |
| M3 | Coste de la Margherita: el Excel del plan dice 1,36 € y la calculadora, el Word [78] y la landing dicen 1,32 € | Instrucciones `D36`: «Harina, fior di latte, tomate y aceite: unos 1,36 € con merma sobre 9,09 € sin IVA.» | «Masa, tomate, fior di latte, aceite y albahaca: unos 1,32 € con merma sobre 9,09 € sin IVA, según la calculadora del pack.» | `a.py:463` |
| M4 | Posición de la Margherita frente a la mediana: el Excel dice «parte baja», el Word dice «franja media». 10 € está por debajo de 10,90 € | Supuestos `C5`: «en la parte baja de la mediana de 10,90 €» · Word [48] «así que el caso se sitúa en la franja media.» · [55] «entra en la parte media del mercado.» | `C5`: «algo por debajo de la mediana de 10,90 €» · [48]: «así que el caso queda algo por debajo de la mediana.» · [55]: «queda algo por debajo de la mediana: precio de barrio, no de pizzería de autor.» | `a.py:92` · `piz_es_a.json` «48» y «55» |
| M5 | Word [104], seguridad alimentaria: la masa propia no tiene etiqueta de fabricante. El checklist F3 `E9`-`E10` y el Word [82] dicen bien que la fija el APPCC | «La temperatura de los quesos, los embutidos y las masas la marca la etiqueta del fabricante (art. 4.2), y lo que sale…» | «La temperatura de los quesos y los embutidos la marca la etiqueta del fabricante (art. 4.2); la de tus bolas de masa, tu APPCC (la del pliego, 4-6 h a temperatura ambiente y uso en las 6 h siguientes; la de frío, la temperatura y el tiempo que valides), y lo que sale…» | `piz_es_b.json` «104» |
| M6 | Se promete de la calculadora lo que no hace. No hay entrada de tiempos ni de prefermentos, y A y B son bloques de la hoja «Masa», no hojas | Dashboard `L40`: «Calcula la masa por bolas según la hidratación y las horas de fermentación, y el escandallo…» · Landing FAQ 4 `.ts:45`: «eliges harina, hidratación, bolas y número de pizzas…» y «Con una segunda hoja, la B, calculas tu masa de panadero con tu propia hidratación y fermentación.» · Grid `.ts:137`: «La hoja A calcula… la B, tu masa de panadero» · Word [78]: «La calculadora hace las dos cuentas:» (justo después de hablar de biga, poolish y 24-72 h en frío) | Dashboard: «Calcula la masa por bolas con los gramajes del pliego o por porcentaje panadero (hidratación, sal y levadura), el coste de cada bola y el escandallo, el food cost y el margen de 8 pizzas editables.» · FAQ 4: «eliges cuántas bolas y de qué peso, la merma y los gramos por litro, y te da…» y «Con un segundo bloque, el B, calculas tu masa por porcentaje panadero con tu propia hidratación, sal y levadura; los tiempos de fermentación los fijan tu receta y tu APPCC.» · Grid: «El bloque A calcula… el B, tu masa por porcentaje panadero.» · Word [78]: «La calculadora tiene las dos entradas, la del pliego y la del porcentaje panadero (sin prefermentos ni tiempos, que fija tu receta):» | `PlanNegocioPizzeriaDashboard.tsx:40` · ficha `.ts:45` y `:137` · `piz_es_b.json` «78» |
| M7 | Landing FAQ 1 (va a `FAQPage`, fragmento destacado): la primera respuesta suena a permiso | «Con cuidado, porque desde diciembre de 2022 «Pizza Napoletana» es…» | «Solo si tu pizza cumple el pliego y pasa la verificación oficial, porque desde diciembre de 2022 «Pizza Napoletana» es…» (el resto, igual) | ficha `.ts:33` |
| M8 | Neto en la landing: la FAQ 3 ata «unos 386.000 € de ventas» (año 1) a un neto del «9-10 %», pero ese año el Excel da 8,5 % | `.ts:41`: «el beneficio neto sale en torno al 9-10 % de las ventas» · `.ts:155`: «el neto sale en torno al 9-10 % de las ventas» | `:41`: «el beneficio neto sale en un 8,5 % de las ventas el primer año y en torno al 10 % el segundo y el tercero» · `:155`: «el neto sale en un 8,5 % el primer año y en torno al 10 % los dos siguientes» | ficha `.ts:41` y `:155` |

## m — Menores

| # | Dónde | Texto actual | Arreglo propuesto (literal) | Fuente |
|---|---|---|---|---|
| m1 | Inversión `D9` | «Nadie pública precio por metro» (la fuente dice «publica»: es otra trampa de `motor.TILDES`, como la de campana → campaña) | «Ningún fabricante da precio por metro: pide oferta con tu proyecto». Añade al barrido la guarda `\bpública precio` | `semilla_piz.py:63` · `barrido_es.py` |
| m2 | Redondeos del token frente a la celda. `_fmt` usa `round()` (redondeo bancario) y `'{:.2f}'` sobre float | Word [43] y [86]: «4,97 jornadas» (`Personal!C12` = 4,975) · Word [41] y [93]: «27.940 €» (`Inversión!B32` = 27.940,5; Excel muestra 27.941 € si el formato es `#,##0`; compruébalo) | Redondeo hacia arriba en `_fmt`: `Decimal(str(v)).quantize(Decimal('1'), ROUND_HALF_UP)` en `eur` y `Decimal('0.01')` en `dec2` → «4,98» y «27.941 €». Regenera `cifras_caso_es.json` y el Word | `cifras_piz_es.py:216-228` |
| m3 | Word [47] | «una pizza lista en pocos segundos» | «una pizza lista en 60-90 segundos» | `piz_es_a.json` «47» |
| m4 | Word [79] (D11: no asociar «napolitano» con un horno que no cumple el pliego) | «Un eléctrico napolitano de seis pizzas cuesta unos 13.140 € sin IVA» | «Un eléctrico de alta temperatura para seis pizzas (el modelo «Napolitano» de un fabricante italiano) cuesta unos 13.140 € sin IVA» | `piz_es_b.json` «79» |
| m5 | Word [78] y landing FAQ 4 (1.586 g ÷ 200 g = 7,9) | «6 bolas de 250 g o 8 de 200 g» · `.ts:45` «(o 8 de 200 g)» | «6 bolas de 250 g o casi 8 de 200 g» · «(o casi 8 de 200 g)» | `piz_es_b.json` «78» · ficha `.ts:45` |
| m6 | Word [107]: en el pliego, la mozzarella es opcional y solo va en la Margherita; la Marinara no lleva queso | «estirado a mano y mozzarella de búfala campana DOP o «Mozzarella» ETG)» | «estirado a mano y, si lleva queso, «Mozzarella di Bufala Campana» DOP o «Mozzarella» ETG)» | `piz_es_b.json` «107» |
| m7 | Word [94]: falta la salvedad de la microempresa que sí trae `Supuestos!C38` | «en el tercer año el plan ya aplica el tipo general del Impuesto de Sociedades.» | «en el tercer año el plan ya aplica el tipo general del Impuesto de Sociedades (25 %); si tu cifra de negocios no llega a 1 M €, el tuyo será más bajo: confírmalo con tu asesor.» | `piz_es_b.json` «94» |
| m8 | Word [40]: en el año de carencia no se devuelve principal | «el de caja, que además cubre las cuotas del préstamo, en {BE_COMENSALES_DIA_CAJA} durante el primer año, el de carencia.» | «el de caja, que además cubre la devolución del principal (ninguna el primer año, el de carencia), en {BE_COMENSALES_DIA_CAJA} ese primer año.» | `piz_es_a.json` «40» |
| m9 | Word [98]: «sin mucho colchón» choca con el semáforo verde del Excel (1,88 frente a 1,25) | «el negocio cubre la deuda, pero sin mucho colchón, y el banco querrá ver tu plan de ventas.» | «el negocio cubre la deuda con margen sobre el 1,25 que suele pedir un banco, que aun así querrá ver tu plan de ventas.» | `piz_es_b.json` «98» |
| m10 | PyG `F13`: `TEXT(…,"0%")` del motor muestra «Al 24%» cuando el dato es 23,5 % | «Al 24% de las ventas de COMIDA…» | Aceptar: es la fórmula del motor común, que no se toca. Si se quiere, que el prefijo de la nota en `a.py` no repita la cifra | motor (no tocar) |
| m11 | Calculadora · Escandallo `E5` e Instrucciones `A21`: cita solo el apartado de hostelería; para llevar aplica el 1.1.º, como dice el plan | «(Ley 37/1992, art. 91.Uno.2.2.º)» | «(Ley 37/1992, art. 91.Uno.1.1.º y 2.2.º)» | `calculadora_piz_es.py:133` y `:557` |
| m12 | Calculadora · Masa `C9` bajo la cabecera «Pliego mín.»: el pliego no fija mínimo de harina, y 1.000 / 1.600 = 62,5 % | `E9`: «El mínimo de 1.600 g es el que da una absorción del 62 % (cálculo del kit…)» | «El pliego solo fija el máximo (1.800 g). El mínimo de 1.600 g (62,5 % de hidratación) es un cálculo del kit sobre la absorción de 55-62 % que el pliego pide a la harina.» | `calculadora_piz_es.py:71` |
| m13 | Checklist · Instrucciones `A3`: aparece el slug, no el nombre del producto | «Este fichero forma parte del producto «plan-negocio-pizzeria» de AI Chef Pro.» | «Este fichero forma parte del «Plan de Negocio: Pizzería Napolitana» de AI Chef Pro.» (la heladería arrastra el mismo molde) | `semilla_piz.py:235` |
| m14 | Dashboard `L33`: las fases no son las del checklist (5 grupos en vez de 6, y «obra y horno») | «80 tareas por fases para abrir tu pizzería: constitución y fiscalidad, local y licencias, obra y horno, equipo, marca y apertura.» | «80 tareas en 6 fases para abrir tu pizzería: constitución y fiscalidad; local, salida de humos, licencia y terraza; cocina, horno y registro sanitario; personal, formación y prevención; carta, marca, delivery y captación, y apertura y primeros 90 días.» | `PlanNegocioPizzeriaDashboard.tsx:33` |
| m15 | Landing FAQ 5: el Word [79] y [81] dicen que el eléctrico no te libra de la campana | «y el eléctrico es el más sencillo de instalar.» | «y el eléctrico es el más sencillo de instalar, aunque pide unos 16 kW más en trifásica y también campana y conducto para los vahos.» | ficha `.ts:49` |
| m16 | Landing: la cuenta que trae el Word es reparto propio frente a plataforma, no recogida frente a plataforma | `.ts:53`: «y la cuenta de recogida en el local frente a plataforma está hecha para que decidas con números» · `.ts:124`: «el delivery por plataforma frente a la recogida, con las cuentas hechas» | `:53`: «y el Word hace la cuenta del reparto propio frente a la plataforma para que decidas con números» · `:124`: «el delivery por plataforma frente al reparto propio, con las cuentas hechas» | ficha `.ts:53` y `:124` |
| m17 | Mes de la versión (D3: «noviembre 2026» si se fusiona a partir del 1-nov) | Word [16], Instrucciones `A52` del plan, `A27` de la calculadora, `A11` del checklist y `.ts:237`: «octubre 2026» | Si el merge cae en noviembre: `VERSION_MES` = «noviembre 2026» en `piz_version.py`, regenerar y cambiar `updateNote` | `piz_version.py` · ficha `.ts:237` |

## Aplicado (ronda única de arreglos, sesión Claude Code, 25-oct-2026)

Todo en la fuente; los xlsx y el docx se regeneraron en el VPS. **Aplicados: B1 · M1-M8 · m1-m9 y m11-m16.** No
aplicados: **m10** (la fórmula `TEXT(…,"0%")` es del motor común, que no se toca; la nota propia de `a.py` no repite la
cifra) y **m17** (el mes se queda en «octubre 2026»: el merge es esta noche).

| # | Qué se hizo (y dónde se aparta de la propuesta) |
|---|---|
| B1 | `a.py`, punto 8 de Instrucciones: la calculadora sirve para ESCANDALLAR cada pizza; no copies su food cost en Supuestos; `B13` es la media ponderada de TODA la carta (pizzas, entrantes y postres) más la merma; comprueba con tus escandallos que la media cuadra |
| M1 | [42], [98] y [111] sin «la respuesta es:» ni «el plazo que indica»: «El payback antes de la deuda, en años, … «{PAYBACK}» con el fondo de maniobra dentro y «{PAYBACK_CAPEX}» sin él». Leen bien con «Más de 3 años» y con una cifra (el token numérico sale sin unidad; «en años» va en la frase). No se usa «no se recupera en tres años», que solo vale con un valor. La pista de `tandas_docx.py` lo avisa |
| M2 | «con azúcares o edulcorantes añadidos» en Supuestos `C40`, `C62`, `C63`; rótulo `A62` «refrescos azucarados o edulcorados»; PyG `F11` (y «zumos sin azúcares ni edulcorantes añadidos»); Instrucciones `A8` (clave nueva en `VOCABULARIO`) y `D42`; Tesorería `O16`; calculadora `A21`; Word [95] y [108]; ficha `:53`, `:139`, `:154`; pistas de `tandas_docx.py`. El grep de «azúcar» sin «edulcor» en los 4 ficheros, la ficha, el dashboard y el correo da 0 |
| M3 | `a.py` (Instrucciones `D36`): «Masa, tomate, fior di latte, aceite y albahaca: unos 1,32 € …, según la calculadora del pack» |
| M4 | Supuestos `C5`, Word [48] y [55]: «algo por debajo de la mediana» |
| M5 | Word [104]: la temperatura de las bolas de masa la fija tu APPCC (pliego: 4-6 h a temperatura ambiente y uso en las 6 siguientes; en frío, la que fijes y compruebes). Sin «validado», que es palabra prohibida (D12) |
| M6 | Dashboard, ficha (FAQ 4 y grid) y Word [78] con la propuesta: bloques A y B, sin prefermentos ni tiempos; «Con los precios del kit, cada bola cuesta…» |
| M7 · M8 | Ficha `:33` («Solo si tu pizza cumple el pliego y pasa la verificación oficial…») · `:41` y `:155` (8,5 % el primer año, en torno al 10 % los siguientes) |
| m1 | `semilla_piz.py`: «Ningún fabricante da precio por metro». Guarda nueva en `barrido_es.py`: `RX_PUBLICA` («pública» con tilde tras sujeto o pronombre átono, o delante de «precio» / «tarifa»; sin «lo» ni «la»). Probada: caza el `D9` del libro anterior y da 0 en el nuevo |
| m2 | `cifras_piz_es.py`: redondeo comercial (`Decimal`, `ROUND_HALF_UP`, sobre `round(v, 9)`) en todos los formatos. Cambian 2 tokens: `JORNADAS` 4,97 → **4,98** y `IVA_INVERSION` 27.940 € → **27.941 €** (los dos casan ya con el formato del Excel: `#,##0.00` y `#,##0 €`). Ninguna otra cifra del caso cambia |
| m3-m9 | Como se propuso. m7, alineado con `Supuestos!C38`: «(25 %); si tu cifra de negocios queda por debajo de 1 M € o de 10 M €, desde 2025 hay tipos más bajos que se implantan de forma gradual: confírmalo con tu asesor». m9 añade «1,25» a `PERMITIDAS` |
| m11 · m12 | Calculadora `E5` y `A21` («art. 91.Uno.1.1.º y 2.2.º») · `E9` de Masa: «El pliego solo fija el máximo…» |
| m13 | `semilla_piz.py`: «Este fichero forma parte del «Plan de Negocio: Pizzería Napolitana» de AI Chef Pro.» (la heladería, publicada, sigue con el molde del slug: no se toca aquí) |
| m14 · m15 · m16 | Dashboard `:33` con las 6 fases · ficha `:49` · ficha `:53` y `:124`. La línea `:155` y el correo («frente a la recogida, con la comisión real») no prometen una cuenta hecha: se quedan |

**Gates tras regenerar** (VPS salvo `check`, `esbuild`, precios y nombre): `ciclo.sh` TODO VERDE (main.py exit 0) ·
calculadora `formulas=142 cache=142 fallos_pycel=0` y `--autotest` 422 comprobaciones VERDE · `cifras_piz_es.py --calc`
178 tokens, D9 VERDE · `tandas_docx.py check` A y B OK (0 errores; avisos de longitud en [104] y los de cifra de
siempre) · `docx_piz_es.py` 131 párrafos, 10 Heading 1, VERDE · `barrido_es.py` 0 en los 4 regenerados ·
`gate_restos_ft.py --rx-extra` VERDE (4) · `gate-no-latinos.py` 0 · `censo-entregables.py --fail` 0 (5 ficheros) ·
`esbuild` OK (ficha y dashboard) · `sync-product-prices.py --check` OK · `nombre-gate.py` OK. sha256 Mac = VPS: plan
`afa03288…2217`, checklist `306e3fc3…03de4`, calculadora `f6b15b35…7b01`, Word `e00c1a9f…59c6`; la guía de
equivalencias no cambia (`d071611e…1ea0`).

**La guía de equivalencias y el barrido.** `barrido_es.py` da 19 coincidencias en la guía, y `gate_restos_ft.py`, 10 y
el tamaño Carta. Son el vocabulario de Hispanoamérica del glosario común («manteca», «heladera», «tapas», «food truck»,
«carné de manipulador» en cada país), no restos del molde. La guía de la heladería, ya publicada, da 26 y el mismo tamaño
Carta. No se toca: esos dos gates son del plan, no del bonus común.

## Fuera de esta revisión

- `guia-equivalencias-plan-negocio-pizzeria.docx`: no estaba en los volcados.
- Imágenes de la landing y Payment Link: son de John.
- Tras aplicar M2 y m1: repetir `barrido_es.py`, `gate_restos_ft.py --rx-extra`, `cifras_piz_es.py --calc` y `tandas_docx.py check`, porque M1, M5, M6 y m3-m9 tocan ranuras del Word.
