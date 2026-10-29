# Plan de Negocio: Taquería ES 1.0 — Revisión adversarial F2 (cifras · legal · editorial · integridad)

> Sesión Claude Code, 29-oct-2026. Una pasada sobre los 4 de `dl/plan-negocio-taqueria/` (volcados en el VPS con y sin `data_only`)
> contra R §1/§3/§6/§7, F1-camino §2, F2-NOTAS y `cifras_caso_es.json`, y una ronda de arreglos de TEXTO. `[n]` = párrafo del Word
> = clave de `textos/taq_es_{a,b}.json`; `a.py` = `planes-v2_0/contenido_plan_negocio_taqueria/a.py`.

**Recuento: 0 B · 5 M · 10 m.** Ninguna cifra movida: `cifras --calc` regenerado = JSON del Word (183 tokens, D9 VERDE).

## Comprobado sin hallazgo
- **Cifras**: todas las del caso son tokens = caché. Las tecleadas, recalculadas: cono 15 × 1,08 × 0,60 = 9,72 kg → 64,8 %, 278 tacos, 18,5/kg;
  pastor 0,6137 € / 2,727 € = 22,5 % (orden 23,8 %, gringa 23,0 %); 697 tortillas = (18.900 + 18.000/6) / (0,1048 × 300); plataforma
  42.966 € y 12.890 €; 115 tacos / 18,5 = 6,2 kg; 0,096/0,070 = +37 %; 17,43 € de ticket en sala. Mes 1 = enero, pagas 7 y 12, rampa a
  abril, saldo mínimo 50.781 € (Mes 1), 118.000 + 55.000 €, neto 9,1/10,3/9,6 %, DSCR 2,20, payback 2,9 (y 2,0) con frases que leen
  también «Más de 3 años», food cost 27 % con su sensibilidad (2.900 €/punto; 8 % al 30 %), Instrucciones!A12 sin el B1 de la Pizzería.
- **Legal**: art. 30 = RD 1086/2020 en la redacción del RD 1021/2022 ([107], plan Instrucciones!C42, checklist F3!E11); art. 4.1
  (preparado de carne y vegetal cortado ≤ 4 °C); RD 126/2015 4.1.b y 6.5.a (F4!E15); LIVA 91 (sala 10 %, compras al 4 %); 828/2014;
  Ley 7/2022 y 1/2025; RD 919/2006; Madrid solo como ejemplo; jornada sin «digital obligatorio»; sin carné de manipulador.
- **Integridad**: los 4 abren; 0 `#REF!/#DIV/0!/#VALUE!`; 0 fórmulas sin `<v>`; 16/16 + 7/7 + 4/4 hojas protegidas, verdes desbloqueadas
  (0 bloqueadas); A4 en todas; docProps AI Chef Pro + `aichef.pro/plan-negocio-taqueria`; 10 Heading 1 = índice; fases del Word [116]
  = `A2` de las 6 pestañas; hojas «Trompo», «Tortilla», «Escandallo» y «Tesorería» citadas con su nombre real.

## M — Mayores (todas arregladas)
| # | Dónde | Hallazgo → arreglo |
|---|---|---|
| M1 | Word [78] | «22,5 % de food cost **sobre 3,00 € con IVA**» (0,61/3,00 = 20,3 %; el 22,5 % es sobre 2,73 € sin IVA, = Escandallo!D40-D41) → «sobre su precio sin IVA (en carta, 3,00 € con IVA)» |
| M2 | Word [108] | Regla del 21 % para llevar incompleta («aguas frescas azucaradas, la cerveza y el mezcal»): faltan los refrescos con azúcares o edulcorantes y el tequila (LIVA 91.Uno.1.1.º a y b; el Excel y F5!E7 la dan entera) → «el alcohol (cerveza, mezcal, tequila) y las aguas frescas y los refrescos con azúcares o edulcorantes añadidos» |
| M3 | Word [81] | El nixtamal «sin Excel», pero la hoja «Tortilla» de la calculadora hace esa cuenta (697) y F1!E7 la cita → «el plan financiero no la modela, pero la hoja «Tortilla» de la calculadora sí» |
| M4 | plan Instrucciones!D37 · checklist F5!E11 · Word [94] | El Excel dice que carne y tortilla «no tienen precio profesional publicado» / «no la ha leído en una tarifa» y el Word cita Makro → «son precios estimados por el kit» / «con un precio de referencia: pon el tuyo» (`a.py:479`, `datos_checklist.py:249`); [94] «de gama selecta» → «Duroc» y «6,99 € **el kilo** con IVA» |
| M5 | Word [94] | Año 3 «al tipo general» sin la salvedad de microempresa de Supuestos!C38 (= m7 de la Pizzería, repetido) → «(25 %); si tu cifra de negocios no llega a 1 M €, el tuyo será más bajo: confírmalo con tu asesor» |

## m — Menores
| # | Dónde | Hallazgo → estado |
|---|---|---|
| m1 | Word [42] | Repite la frase de ventas y neto del año 1 de [40] → «A partir de ahí, los comensales crecen…». Arreglado |
| m2 | Word [89] | Repite la cuenta del repartidor de [73] (0,35 jornada, 8.800, 2.500, 11.300 €, 26 %) → remite al plan de marketing. Arreglado |
| m3 | Word [78] [79] [80] · [47] [105] | Glosas repetidas (trompo y pastor, comal, gringa, carnitas y suadero) quitadas; glosa nueva de aguas frescas ([47]) y salsa macha ([105]). Arreglado |
| m4 | Word [56] | Llama «taquería de barrio» al caso ([46] la define como la de sin trompo) → «de ciudad». Arreglado |
| m5 | Word [104] | «lo que permite su art. 3» (parece el del RGSEAA) → «el art. 3 del RD 1021/2022» (= R §1, F3!E7). Arreglado |
| m6 | Word [105] · checklist F5!E9 | «Las bandejas de cartón no son plástico»: con recubrimiento plástico sí lo son (Directiva 2019/904) → «sin recubrimiento de plástico». Arreglado |
| m7 | plan Tesorería!O5 · checklist F6!E14 | «Picos» en septiembre y noviembre: la tupla da 0,088 y 0,086 (mayo, junio y octubre, 0,088); el pico es diciembre (0,096) → «diciembre es el pico; septiembre y noviembre traen las fechas mexicanas» (`a.py:77-79`, `datos_checklist.py:295`). Arreglado |
| m8 | calculadora Instrucciones!A10 · checklist F1!E7 | «manténlo» → «mantenlo»; «el local tiene que caberla» → «el molino y la tortilladora tienen que caber en el local». Arreglado |
| m9 | Word [88] [102] [105] · F1!E9, F3!E17, F4!E6 | Normas fuera de R §1. Con ✅ en el research hermano (PIZ §1): RD 100/2011 + 1042/2017, RD 1021/2022 arts. 4.3 y 20, TRLRHL 82.1.c; Ley 12/2012 art. 2.2 (REVISION-FINAL Pizzería). En ningún research: Ley 18/2022 (SL con 1 €), Reg. 1169/2011 art. 14 (venta a distancia), ET art. 1.1. Correctas y = Pizzería LIVE: se mantienen. **Pendiente F3**: anotarlas en R §1 |
| m10 | plan Inversión!D37 | «Suman 61650 € de los 151000 €» sin separador de miles: fórmula del motor común (la Pizzería LIVE da «77703 €»). **Pendiente**: fuera de alcance (código común) |

Para la F3 (landing y dashboard, no revisados aquí): replicar M2 (refrescos edulcorados y tequila), M3 (la calculadora sí hace el nixtamal) y m7 (pico = diciembre).

## Gates re-pasados (VPS, tras los arreglos)
`ciclo.sh` exit 0, **TODO VERDE** (16/16 protegidas) · `calculadora_taq_es.py` (genera + autotest) exit 0 · `cifras_taq_es.py --calc` **D9 VERDE**,
183 tokens, JSON **idéntico** al del Word · `tandas_docx.py check` a y b: **0 errores** (avisos: «sin gluten» y «tex-mex» como advertencia,
correctos; longitud de [73] y [108]) · `docx_taq_es.py` **VERDE** (131 párrafos, 10 H1, 7.559 palabras) · `barrido_es.py` sobre los 4: **0**
(7 avisos revisados, correctos) · `gate_restos_ft.py --rx-extra` (tapas, heladería, Pizzería): **VERDE** (4). Diff contra la versión previa:
solo lo tocado (plan 2 celdas, checklist 4, calculadora 1, Word 12 párrafos).

## sha256 finales (Mac = VPS)
`plan-financiero-taqueria.xlsx` 5778011f…c0ad6 · `checklist-apertura-taqueria.xlsx` 27b6962c…d4f339 ·
`calculadora-trompo-escandallo-taqueria.xlsx` ec7e8771…bcb2d9 · `plan-de-negocio-taqueria.docx` c028c2bb…d63d5
