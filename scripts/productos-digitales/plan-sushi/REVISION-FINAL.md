# Plan de Negocio: Sushi Bar ES 1.0 — Revisión adversarial F2 (cifras · legal · editorial · integridad)

> Sesión Claude Code, 31-oct-2026. Una pasada sobre los 4 de `dl/plan-negocio-sushi-bar/` (volcados en el VPS con y sin `data_only`,
> en `/root/tmp-sus-f2/dl/` → `/tmp/sus_rev/`) contra R §0-§3 y §1 (tabla legal y literales), F0, F1-camino §2/§4/§9, F2-NOTAS §2,
> `cifras_caso_es.json` (192 tokens) y la revisión de la Pollería, y una ronda de arreglos de TEXTO. `[n]` = clave de
> `textos/sus_es_{a,b}.json` (= párrafo n del volcado del docx); `a.py` = `planes-v2_0/contenido_plan_negocio_sushi_bar/a.py`.

**Recuento: 0 B · 1 M · 24 m** (21 arreglados, 4 aceptados). Ninguna cifra del caso, valor por defecto, fórmula ni celda movida:
los arreglos son de redacción, de cita o de una cifra tecleada que contradecía a su fuente.

## Comprobado sin hallazgo
- **Cifras**: todas las del caso en el Word son tokens = caché (muestreo: plan `Instrucciones!B25-B31`, `Tesorería!B23/M22/E6`,
  `Punto Equilibrio!B20/B24-D24`, `Personal!B25-B27`; calculadora `Pescado!B24-D24`, `Arroz!B28/B31/B43`, `Escandallo!K16/K26/N26/P26/B34`).
  Tecleadas, recalculadas: 79 × 20,00 × 300 = 474.000; 45 + (13 + 8,5) × 1,6 = 79,4; (45 × 22,26 + 8,5 × 24,55 + 13 × 29,55) ÷ 79,4 = 20,08;
  22,02 = 20 × (0,85 × 1,10 + 0,15 × 1,1077); 9,50 ÷ 0,70 ÷ 0,95 = 14,29; 21,80 ÷ 0,95 ÷ 0,95 = 24,16; 26 ÷ 0,95 ÷ 0,95 = 28,81; 2,2 × 1,1 = 2,42;
  2.420 ÷ 20 = 121; 79 × 0,150 ÷ 2,42 = 4,90 kg; 103.350 + 3.200 + 3.200 = 109.750 (+ 53.908 = 163.658; + 21.746 = 185.404; 186.000 − 185.404 = 596);
  474.000 × 0,85 × 1 % = 4.029; 116.841 × 35 % × 20 % ≈ 8.180 (R §3: el salmón ≈ 35 % de la compra de comida); 10 puntos × 474.000 × 30 % = 14.220;
  113.760 × 30 % = 34.128; 0,07 × 0,15 = 1,05 %; estacionalidad 0,092/0,086/0,066 y 0,092 ÷ 0,066 = 1,39; 79 → 84 → 87; 68 × 19 × 295 = 381.140 y
  90 × 21 × 305 = 576.450; 9.844 ÷ 8.625 = 114 % (28,75 h × 300); itamae 2.200 × 14 × 1,33 ÷ 1.840 = 22 €/h; 1.600 ÷ 95 ≈ 17 €/m²; 0,75 × 21 + 0,25 × 10
  = 18,25 %; rampa normalizada (`Tesorería!O7`: el año = el P&L, así que «la media incluye la rampa» de [40] es cierto; `E6` = 1 en abril); IS 15/15/25 %.
  Margen del combinado de 24: 22,16 → 16,12 € = −27 % («más de un cuarto» en F5!E6; ningún «a la mitad»). Food cost siempre sobre el precio sin IVA
  (4,73 = 5,20 ÷ 1,10). Coherencia: Excel de 9 hojas, calculadora de 4 con «Pescado», «Arroz» y «Escandallo» citadas por su nombre, 14 productos,
  carta del caso [48] = `Escandallo!G16-G26`, 80 tareas 12/15/14/13/13/13 = contadores `E18…E21` y fases de [116] = pestañas.
- **Legal**: RD 1021/2022 art. 8.1-8.2 (−20 °C ≥ 24 h o −35 °C ≥ 15 h en la totalidad; acuicultura solo con acreditación escrita, Rgto. 853/2004 anexo III
  secc. VIII cap. III.D; atún salvaje no exento; carta o cartel) en [104] [112], F1!E7, F3!E7-E10, `Pescado!A3/B39-B41`, calculadora `Instrucciones!A9`
  y plan `Instrucciones!D43`; RD 1420/2006 solo como derogado; 0 «7 días»; 0-4 °C del art. 4.1 ([81] [106], F3!E11); shari solo por el 30.5 del RD
  1086/2020, sin pH ni tiempo legal y 4,6 = límite del Kit ([107], F3!E13-E14, `Arroz!A3`, `Instrucciones!A14`); todo «art. 30» con RD 1086/2020;
  RD 126/2015 arts. 4, 5, 4.1.b y 6.5.a; Reg. 1169/2011 art. 14; LIVA 91 (10 %; 21 % entera en [108], F5!E7, `Supuestos!A62/C62/C63`; 4 % d-f);
  IAE 671/673 y 677.9; Ley 1/2025 art. 8; Ley 7/2022 art. 55; ALEH VI art. 4; SMI 1.221 € (RD 126/2026; `Supuestos!B22` = 17.094); ET 34.9 sin
  «digital»; «sin gluten» nunca prometido (828/2014); «sushi grade» solo para negarlo; −18 °C solo para decir que no sirve; Madrid (Ordenanza
  4/2021, arts. 12, 23 y anexo I) solo como ejemplo; RGSEAA solo por encima del art. 3.
- **Editorial**: tuteo; 0 restos (barrido propio sobre los 4 volcados: taco, trompo, pollo, pizza, mezcal, tapa, pan, food truck, cubierto, pax,
  validado, CNAE…: 0); jerga glosada la primera vez (itamae [39], shari [43], kaiten [46], neta, sushi-zu, hangiri, saku, nigiri, sashimi, hosomaki,
  uramaki, temaki y combinado [47], poke [48]); «estimación del kit» en pescado, arroz y escandallo; las cifras de franquicia, solo para comparar.
- **Integridad** (VPS): los 4 abren; sha256 Mac = VPS antes de los arreglos; 0 fórmulas sin `<v>` (plan 741, con 59 `<v></v>` = «""» del motor;
  checklist 12; calculadora 180) y 0 errores; 9 + 7 + 4 hojas protegidas, 0 verdes bloqueadas y 0 no verdes desbloqueadas con valor; A4 (`paperSize`
  9) en todas y docx 210 × 297 mm; docProps creator/author AI Chef Pro + `aichef.pro/plan-negocio-sushi-bar` en los 4 (la `category` vacía en el docx
  y la calculadora no se exige); 10 Heading 1 = índice [24]-[33]; no latinos: 0 en los xlsx y en el docx solo «━» del molde.

## M — Mayores (arreglada)
| # | Dónde | Hallazgo → arreglo |
|---|---|---|
| M1 | Word [49] · plan `Supuestos!C5` (`a.py:99-101`) | Ticket por canal incoherente con la carta del caso: «el pedido para llevar (un combinado de 24 piezas y un extra, 27,00 € con IVA)», cuando el combinado de 24 cuesta 29,00 € ([48], [55], `Escandallo!G26`): el pedido valdría menos que su propio combinado (arrastrado de R §3). Y «la plataforma, con el precio un 15 % más alto, a 18,47 €» no sale de 15,34 × 1,15 = 17,64 (R §3: 32,50 € = carta +15 % y pedido mayor) → «de unos 27,00 € con IVA de media (un combinado y algún extra)» y «con la carta un 15 % más cara y un pedido algo mayor». Las cifras no cambian y la media sigue en 20,08 € |

## m — Menores
| # | Dónde | Hallazgo → estado |
|---|---|---|
| m1 | Word [42] [48] [49] [66] [95] | Sin artículo ante el porcentaje (regla 14): «es de 27,8 %», «baja a 21,5 %», «sale en 11,3 %», «es de 85 % de comida», «queda en 10,8 %», «es 8,7 %»…; y «con IVA con la bebida» → «del/al/un…» y «con IVA y con la bebida». Arreglado |
| m2 | Word [43] | La plantilla de 7 personas enumera 5 («…cocina caliente y arroz, sala y pedidos…»: falta el puesto y el camarero de cenas) → «un encargado de sala y pedidos, un camarero de cenas y un refuerzo de fin de semana: con las suplencias, 7 personas»; recortado el arranque para no pasar del 135 % de longitud. Arreglado |
| m3 | Word [46] | «la franquicia de quiosco más barata pide 39.950 €» (R §2: Makitake desde 30.000 € y Sushicatessen desde 37.000 €) → «una franquicia de quiosco como Sushimore»; «omakase» sin glosar y ticket «80-150 €» (R §2 lo da en 80-180 € por GJ §3) → «(el menú que decide el itamae)» y «a partir de 80 €». Arreglado |
| m4 | Word [47] | «El pescado llega en saku» contradice el salmón entero limpio en casa ([65], [78], `Pescado!B5`) → «El salmón llega entero y se limpia en casa; el atún, en saku…»; glosa de neta acortada (longitud). Arreglado |
| m5 | Word [56] | «En la costa, agosto sube: gira la fila» (girar es para otro mes de apertura; `Tesorería!O5` y [97] lo dicen bien; = Pollería m5) → «cambia los pesos de la fila de estacionalidad de la Tesorería». Arreglado |
| m6 | Word [57] | SERP atribuida a «plan de negocio sushi» (10 búsquedas, sin SERP leída): la de F0 §1 / R §4 es «montar restaurante de sushi» → corregida, y «SERP» glosada. Arreglado |
| m7 | Word [80] | Shari por kilo, nigiris y arroz del día sin la marca de estimación (regla 9) → «Con los valores del kit, …». Arreglado |
| m8 | Word [88] · checklist F4!E6 (`datos_checklist.py:209`) | «las de un omakase pasan de 2.500 € al mes» (R §0.6/§2: «desde 2.500 €/mes») → «parten de». Arreglado |
| m9 | Word [93] | «109.750 € de compras» (incluye fianza y renta previa; [41] dice inversión; = Pollería m7) → «de inversión sin el fondo». Arreglado |
| m10 | Word [95] [115] | Regla del 21 % recortada («con azúcares añadidos», «refrescos azucarados»: faltan los edulcorantes, LIVA 91.Uno.1.1.º b; [108] y el Excel la dan entera; = Pollería m8) → completa. Arreglado |
| m11 | Word [98] [111] | «No es una recuperación rápida» con un payback de 2,5 (1,7 sin el fondo) se contradice con la cifra; [111] «baja al 21,5 % … y al 23,3 % en el tercero» (del 2.º al 3.º sube) → frases que leen bien con «2,5» y con «Más de 3 años» y «se queda en el 23,3 %». Arreglado |
| m12 | calculadora `Pescado!F6` (`calculadora_sus_es.py:71`) | «atún aleta amarilla en saku ultracongelado, 26 €/kg» entre los precios de mercado (R §0.4/§2: ❌ sin precio en España; es del kit) → «no tiene precio publicado en España. El kit pone … 26,00 €/kg». Arreglado |
| m13 | calculadora `Instrucciones!A7` (`:648`) | «24,15 en el lomo comprado» frente a 24,16 de `Pescado!C24` (24,155) y del Word [65] [78] → 24,16. Arreglado |
| m14 | calculadora `Instrucciones!A23` (`:681`) | «Si … sale por debajo del 29 %, cambia la celda» (también si sale por encima) → «por encima o por debajo». Arreglado |
| m15 | calculadora `Arroz!C6` (`:132`) | «2,50 € en saco de 20 kg» sin unidad (es otra marca a 2,50 €/kg, R §2) → «otra marca, a 2,50 €/kg en saco de 20 kg». Arreglado |
| m16 | plan `Tesorería!O16` (`a.py:69`) | La comida para llevar al reducido citada solo por el 91.Uno.2.2.º, cuando `Instrucciones!A8` del mismo libro la ampara en el 91.Uno.1.1.º y `PyG!F10` en los dos → «(art. 91.Uno.1.1.º y 2.2.º)». Arreglado (la frase venía dictada por la SPEC) |
| m17 | plan `Instrucciones!D44` (`a.py:514`) | Shari «y lo comunicas a sanidad» (el 30.5 pide que el operador lo «demuestre a la autoridad competente»; así lo dicen [107], F3!E13 y la calculadora) → «lo demuestras». Arreglado |
| m18 | plan `PyG!F55` (`a.py:447`) | «Un sushi bar bien llevado deja en torno a un 8-9 %» con el caso en 9,1/10,4/9,8 % → «8-10 %». Arreglado |
| m19 | plan `Inversión!D14` (`semilla_sus.py:82`) | Congelador «durante 24 horas» sin «al menos» ni la vía de −35 °C 15 h (art. 8.1) → completa. Arreglado |
| m20 | plan `Inversión!D16-D17` (`semilla_sus.py:89-92`) | Campana «una de 1,5-2 m ronda los 815 €» (la fuente, TAQ §2/elhostelero, da 543-813 €) → «va de unos 543 a 813 €»; «el pescado fresco va a 4 °C o menos» (art. 4.1: entre 0 y 4 °C) → «entre 0 y 4 °C». Arreglado |
| m21 | Word [96] [40] | Equilibrio contable «65 comensales» (64,45 exactos) y de caja 62/69/71 (61,8/68,9/70,6) redondeados hacia arriba, con la holgura sobre el exacto: convención del motor (= Pollería m14). Aceptado |
| m22 | Word [56] | Estacionalidad 9,2/8,6/6,6 % y «39 %» tecleados (no son tokens: no siguen a la fila si la cambias). Cuadran con `Tesorería!M5/C5/I5`. Aceptado |
| m23 | checklist (F1!E7, F3!B5, E5, E7, F6!E11) · plan `Inversión!A14/D14` | «-20 °C» con guion en vez de «−»: lo homogeneiza el motor (RC-31, `motor.py:1828-1830`), código común. Aceptado |
| m24 | Word [88] [89] [90] [102] [105] [108] · checklist F3!E15, F4!E7, E10, E13 | Normas fuera de R §1, correctas y = hermanas (Pollería m16): Ley 18/2022, TRLRHL 82.1.c, ET art. 1.1 y DA 23.ª, Ley 31/1995, horarios autonómicos del alcohol para llevar, RD 126/2015 art. 5 «arts. 9 y 10 salvo la nutricional», recalentado «en la hora siguiente» (= Taquería y Pollería). Se mantienen |

**Para el lead**: nada pide mover cifras, valores por defecto ni el motor. Regenerar en el VPS los 4 (plan: `a.py` + `semilla_sus.py`; checklist:
`datos_checklist.py`; calculadora; Word desde `textos/`) y re-pasar `ciclo.sh`, `calculadora_sus_es.py --autotest`, `cifras_sus_es.py --calc`
(tokens idénticos: no se tocó ninguna celda de cálculo), `docx_sus_es.py`, `barrido_es.py`, `gate_restos_ft.py --rx-extra` y `parche_xml_xlsx.py
--check`. **F3** (landing y dashboard, no revisados): replicar M1 (ticket por canal), m10 (21 % entero) y m13 (24,16). R §3 conserva la
derivación «combinado de 24 + extra = 27,00 €»: no reutilizarla así en el EN.

## Gates (Mac: `py_compile` de los 4 .py VERDE; VPS, copia temporal con los JSON nuevos)
`tandas_docx.py check`: **sus_es_a 0 errores** (29 párrafos, 3.158 palabras, 8 avisos: franquicias 46/54/57/61/63 como comparación; 50
«sushi grade», «auténtico» y «sin gluten» negados) · **sus_es_b 0 errores** (32 párrafos, 4.111 palabras, 9 avisos: longitud de 103-108,
previa; 105/115 «sin gluten» negado; 112 −18 °C negado; 115 franquicia). Ningún aviso de «cifra escrita» nuevo.
