# Plan de Negocio: Pollería y Asador de Pollos ES 1.0 — Revisión adversarial F2 (cifras · legal · editorial · integridad)

> Sesión Claude Code, 29-oct-2026. Una pasada sobre los 4 de `dl/plan-negocio-polleria/` (volcados en el VPS con y sin `data_only`)
> contra R §1/§3/§5/§6, F1-camino §2, F2-NOTAS, `cifras_caso_es.json` y las revisiones de la Taquería y la Pizzería, y una ronda de
> arreglos de TEXTO. `[n]` = clave de `textos/pol_es_{a,b}.json` (= párrafo n+1 del volcado); `a.py` = `planes-v2_0/contenido_plan_negocio_polleria/a.py`.

**Recuento: 0 B · 2 M · 16 m** (13 arreglados, 3 aceptados). Ninguna cifra del caso ni de la financiación movida: `cifras --calc` regenerado = JSON del Word (182 tokens, D9 VERDE, `cmp` idéntico).

## Comprobado sin hallazgo
- **Cifras**: todas las del caso son tokens = caché. Tecleadas, recalculadas: 4,55 € = 1,45 × 3,05 + 0,13; 38,8 % sobre 11,73 € sin IVA (calculadora `Escandallo!D37`);
  1,10 kg al 76 %; 17,43 € con IVA (`Supuestos!B9`); 40.148 € y 12.044 € de plataforma; 11.300 € ≈ 28 %; 60 × 3 tandas de 90 min = 180 (10:30-15:00); 106 y
  122 pollos (`Asador!B14`, `B34`); 9,6/9,8 % y 1,40 pico/valle; 77 → 82 → 85 pedidos; 13,4 % de IVA de la bebida; rampa a crucero en abril (`Tesorería!E6` = 1);
  pagas 7/12; préstamo 112.000 + 50.000 €; neto 7,0/8,2/7,7 %; DSCR 1,98; payback «Más de 3 años» y 2,2; 8.464/7.650 h = 111 %; +6.000 €/año de plantilla;
  escenarios 66 × 15 × 295 y 88 × 16,50 × 305; Makro 33,5 % / neto A3 6,7 % (= F2-NOTAS §3). Food cost siempre sobre el precio sin IVA. Volúmenes = R §4.
- **Legal**: 677.9 (+671/673.2 con sala) y 642.5 no ampara asar; RD 1021/2022 arts. 3, 4.1-4.3, 9.2-9.3, 11 y 20; art. 30 = RD 1086/2020 en la redacción
  del RD 1021/2022 ([107], plan `Instrucciones!C43`, checklist F3!E11-E12); RD 126/2015 arts. 4, 5, 4.1.b y 6.5.a; LIVA 91 (sala 10 %, para llevar alcohol y
  refrescos con azúcares o edulcorantes al 21 %, pan al 4 %, versión 1-12-2026 sin cambios); Ley 7/2022 art. 55; Ley 1/2025 art. 8; RD 919/2006; Madrid solo
  como ejemplo; «sin gluten» nunca prometido (5 avisos del barrido, correctos); registro de jornada sin «digital obligatorio»; sin carné de manipulador.
- **Corrientes**: las cinco con R §5 (La Granja Azul 1949-1950, onoto y guasacaca, allioli y patates rostides, rôtisserie, piri-piri); «broaster» solo como frito
  a presión ([50]); 0 restos de Taquería, Pizzería, Tapas o Heladería; 0 «comensal», «cubierto» o «rotación»; Guía Restaurante Peruano existe (`guia-restaurante-peruano`).
- **Integridad**: los 4 abren; 0 errores; 0 fórmulas sin `<v>` (59 `<v></v>` = «""» del motor); 16/16 + 7/7 + 4/4 hojas protegidas, 0 verdes bloqueadas y 0 no
  verdes desbloqueadas; A4 en todas; docProps AI Chef Pro + `aichef.pro/plan-negocio-polleria`; 10 Heading 1 = índice; fases del Word [116] = `A2` de las 6
  pestañas (12/15/14/13/13/13); hojas «Pollo», «Asador» y «Escandallo» citadas con su nombre real; «Excel de nueve hojas» = 9.

## M — Mayores (arregladas)
| # | Dónde | Hallazgo → arreglo |
|---|---|---|
| M1 | calculadora `Escandallo!D6` e `Instrucciones!A21` | Regla del 21 % incompleta («cerveza y refrescos con azúcares añadidos»): faltan el vino y los edulcorados (LIVA 91.Uno.1.1.º a y b; = M2 de la Pizzería, repetido) → «cerveza, vino y refrescos con azúcares o edulcorantes añadidos» (`calculadora_pol_es.py`) |
| M2 | checklist F6!E12 | Inspección o revisión cada 5 años atribuida a la ITC-ICG 08 (es la 07, ap. 4.1-4.2; la 08 es la puesta en marcha: PIZ §1, y así lo dicen F2!E13 y el Word [104]) → «ITC-ICG 07» (`datos_checklist.py:315`) |

## m — Menores
| # | Dónde | Hallazgo → estado |
|---|---|---|
| m1 | Word [43] | «plantilla de 7 personas» enumerando 6 → añade «un refuerzo de sábado, domingo y festivos y las suplencias de vacaciones». Arreglado |
| m2 | Word [49] | Ticket de sala «unos 16,08 €» frente a `Supuestos!C5` «unos 16,10 €» → 16,10 (aviso «cifra escrita» del check: su fuente es C5). Arreglado |
| m3 | Word [50] | Calibre «fijo (1,3-1,6 kg)» frente a `Pollo!C6` y F5!E10 (1,4-1,5 kg) → «(1,4-1,5 kg en canal)». Arreglado |
| m4 | Word [55] | «en Sevilla, de 12 a 14 € con patatas» (R §2: 12 € solo, 14 € con patatas) → «de 12 € solo a 14 € con patatas». Arreglado |
| m5 | Word [56] | «gira la fila» para cambiar el perfil de la costa o del centro (girar es para otro mes de apertura) → «cambia los pesos de la fila de estacionalidad». Arreglado |
| m6 | Word [78] [81] | Glosas repetidas (pollería = tienda de crudo, por 3.ª vez; espadas; tanda; churrasqueira = [47]) → quitadas. Arreglado |
| m7 | Word [93] | «97.900 € de compras sin el fondo» (la fianza no es compra; [41] dice inversión) → «de inversión». Arreglado |
| m8 | Word [113] | Noveno error con la regla del 21 % recortada («cerveza y refrescos azucarados») → completa, como [108]. Arreglado |
| m9 | Word [74] · calculadora `Escandallo!A20` y `A52` | «Patatas al horno» sin horno en la inversión → «patatas asadas». Arreglado |
| m10 | plan `Instrucciones!D36` | «El caso vende unos 302» frente a 301 del Word (token `POLLOS_SEMANA`) → 301 (`a.py:495`). Arreglado |
| m11 | plan `Supuestos!C13` | «el menú de sala a un 24 %» frente a 26,3 % de `Escandallo!I37` → 26 % (`a.py:133`). Arreglado |
| m12 | calculadora `Pollo!C7` | «Entre 3,05 y 3,25 € en mayorista» (3,05 es la estimación del kit) → «Unos 2,96 € en origen y 3,25 € en Makro (octubre de 2026): el kit pone 3,05 €». Arreglado |
| m13 | calculadora `Asador!C17` | 60 kW por defecto con la nota «56 kW el de 8 espadas; la media real es menor» (se contradicen) → «el de 12 gasta más y su media queda por debajo del máximo de su ficha». Arreglado |
| m14 | Word [96] | Equilibrio contable «67 pedidos, con unos ingresos de 313.812 €» (= 66,2 exactos) y holguras sobre el exacto: convención del motor (= Taquería). Aceptado |
| m15 | Word [94] | Makro: 33,5 % y −4.900 € es la vuelta de F2-NOTAS §3 (conservadora: solo el pollo daría ≈ 1,3 puntos, ≈ 4.400 €, como la regla de C13 «6.700 € cada 10 %»). Aceptado: va como «cálculo del kit» |
| m16 | Word [102] [104] [105] [108] · F3!E17 · F4!E6, E13 | Normas fuera de R §1: Ley 18/2022, Reg. 1169/2011 art. 14, ET art. 1.1, Ley 31/1995 (+ RD 100/2011, 1042/2017, TRLRHL 82.1.c y RD 1021/2022 art. 20 con ✅ en PIZ §1). Correctas y = Taquería m9. Se mantienen |

**Fuera de alcance**: la Taquería LIVE trae el error de M2 (`plan-taqueria/datos_checklist.py:289`). **F3** (landing y dashboard, no revisados): replicar M1, m3 y m10.
## Gates re-pasados (VPS, tras los arreglos; salidas en `/root/tmp-pol-rev/`)
`calculadora_pol_es.py` (genera + inject_cache 209/209 + autotest **644 comprobaciones VERDE**) · `ciclo.sh` exit 0, **TODO VERDE** (80 tareas 12/15/14/13/13/13)
· `cifras_pol_es.py --calc` **D9 VERDE**, 182 tokens, JSON **idéntico** · `tandas_docx.py check` a y b: **0 errores** (a: 5 avisos, el nuevo = 16,10 de C5;
b: 9) · `docx_pol_es.py` **VERDE** (131 párrafos, 10 H1, 8.141 palabras) · `barrido_es.py` sobre los 4: **0** (5 avisos «sin gluten»/«broaster», correctos) ·
`gate_restos_ft.py --rx-extra` (Taquería + Pizzería + tapas/heladería + pids): **VERDE** (4). Diff contra la versión previa: solo lo tocado (plan 2 celdas,
checklist 1, calculadora 6, Word 10 párrafos).

**sha256 finales (Mac = VPS)**: `plan-financiero-polleria.xlsx` c8d54739…510376 · `checklist-apertura-polleria.xlsx` c2db78d3…327a42 ·
`calculadora-pollo-asador-escandallo-polleria.xlsx` 2afddfb5…985ad7 · `plan-de-negocio-polleria.docx` cd12837f…447fa4 (la `guia-equivalencias-…docx` de la carpeta es de otro agente: no revisada)
