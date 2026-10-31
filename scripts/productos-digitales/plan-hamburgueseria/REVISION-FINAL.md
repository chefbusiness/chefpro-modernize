# Plan de Negocio: Hamburguesería Smash ES 1.0 — Revisión adversarial F2 (cifras · legal · editorial · integridad)

> Sesión Claude Code, 31-oct-2026. Una pasada sobre los 4 de `/root/tmp-ham-f2/final/` (volcados en el VPS con y sin
> `data_only` en `/root/tmp-ham-f2/revision/`, y otra vez tras los arreglos en `revision2/`) contra R §0-§3 y §1 (tabla legal y
> literales), F0 §1, F1-camino §2/§4/§9, `BRIEF-REDACTORES.md` y `cifras_caso_es.json` (199 tokens), y una ronda de arreglos en
> la FUENTE. `[n]` = clave de `textos/ham_es_{a,b}.json` (= párrafo n del volcado del docx); `a.py` =
> `planes-v2_0/contenido_plan_negocio_hamburgueseria/a.py`. Una cita se leyó hoy en origen: la Orden de 26-1-1989, arts. 5, 6 y 9
> (BOE-A-1989-2265).

**Recuento: 0 B · 4 M · 10 m** (los 14 arreglados) **+ 6 aceptados**. Ninguna cifra del caso, valor por defecto, fórmula ni celda
movida: `cifras_ham_es.py --calc` da los mismos 199 tokens (0 distintos) y la calculadora las mismas cachés.

## Comprobado sin hallazgo
- **Cifras**: todas las del caso en el Word son tokens = caché. Tecleadas, recalculadas: ticket por canal al céntimo en [49] y
  `Supuestos!C5` (17,00 ÷ 1,10 = 15,45; 29,10 ÷ 1,10 ÷ 1,7 = 15,56; 29,10 × 1,15 = 33,465 → 33,47 con IVA, 26,4545 × 1,15 = 30,42 sin
  IVA ÷ 1,7 = 17,90; (52,7 × 15,4545 + 12,9 × 26,4545 + 12 × 30,4227) ÷ 95 = 16,01); «95 comensales equivalentes» en [40] [111] y
  `Supuestos!C4` (52,7 + 1,7 × 24,9); plataforma 24 % en [73] [74] [113], F5!E12, F6!E15, `PyG!F10/F50`, `Supuestos!C58`; margen del
  menú 10,83 → 7,41 € (−31,6 %) «casi un tercio» en [66] [114], F5!E6 y calculadora `Instrucciones!A21` (= `Escandallo!N33/P33`);
  doble 2,90 € / 26,8 % sobre 10,82 € y simple 1,80 € / 22,2 % sobre 8,09 € ([48] [78] = `Escandallo!I21-K22`); 7,50 ÷ 0,90 ÷ 0,97 =
  8,59; 95 × 1,6 × 100 g = 15,2 kg; 10 y 9,7 bolas por kilo; 76 raciones, 11,4 kg y 56 l; +1 €/kg de carne = 0,21 € en la doble
  (≈ 1,9 puntos); Mes 1 = enero con la tupla (enero 7,2 %, mayo 8,9 %, junio 8,8 %, agosto 7,6 %; 0,089 ÷ 0,072 = 1,24) en [56] [97],
  `Tesorería!O5`, `Instrucciones!A10/D35`, F6!E5; sensibilidades: 10 puntos × 456.000 × 30 % = 13.680 ≈ 13.700; (0,33 − 0,24) ×
  456.000 × 30 % = 12.312 ≈ 12.300; (0,45 − 0,24) × 136.800 = 28.728 ≈ 28.700; 107.251 × 55 % × 20 % = 11.798 ≈ 11.800 (R §3: carne ≈ 55 %
  de la compra de comida); 1 punto = 3.830 €; 28,0 − 24,4 = 3,6 ≈ «unos cuatro puntos» ([94], calculadora `Instrucciones!A24`).
  Volúmenes de [53] [54] = F0 §1 (ES 49.500 / 22.200 / 14.800 / 12.100 / 4.400 / 2.900 / 1.000; 210 y 10; MX 18.100 y 320); salarios de
  [88] = R §2 (InfoJobs); franquicias de [63] = R §0.8; Street Smash (Lisboa, 35 locales) de [54] = R §2; 13 errores contados en
  [112]-[115]; 80 tareas 12/15/14/13/13/13 = contadores de cada pestaña; 14 productos en `Escandallo!A21-A34`.
- **Legal**: cocción sin temperatura legal en [80] [106], F3!E10, calculadora `Instrucciones!A29` (AESAN como recomendación, el
  APPCC decide); madurada solo como prohibición (Inf26008) en [104] [112], F3!B9/E9, `Carne!A3/B42`, `Instrucciones!A10`; picada del
  local «no pudiendo conservarse de un día para otro» (art. 7.2) en [81] [104] [112], F3!E7, `Instrucciones!D42`; 853/2004 anexo III
  secc. V vía el art. 7.3 y anexo I 1.13/1.15 ([104], F3!E6/E8); −18 °C solo en F3!E12, como requisito del equipo del art. 5 y con
  «Con carne picada en el local, confírmalo antes con tu inspector»; acrilamida 2017/2158 anexo II parte A ([107], F3!E13, `Patatas!A3`);
  polares < 25 % (art. 6.3) sin medidor obligatorio; IVA: comida al 10 %, cerveza y refrescos con azúcares o edulcorantes añadidos
  (también zero) al 21 % cuando salen ([95] [108] [115], F5!E7, `PyG!F11`, `Supuestos!A62/C62/C63`, `Instrucciones!D41`), batido 🟡
  «confírmalo con tu gestoría» ([108], F5!E8); «sin gluten» con 828/2014 y 20 mg/kg ([105], F4!E17) y nunca prometido; todo «art. 30»
  con «RD 1086/2020» (en la redacción del RD 1021/2022, = brief regla 6); IAE 671/673/677.9 con la nota común; VI ALEH art. 4; SMI
  1.221 € (RD 126/2026); ET 34.9 sin «digital»; DA 23.ª ET; RD 919/2006 con ITC-ICG 07 e ITC-ICG 08 (= arreglo de la Taquería, #186);
  Madrid (OCAS 4/2021 arts. 12, 23, 24 y anexo I) solo como ejemplo; RGSEAA solo por encima del art. 3; Ley 1/2025 art. 8 y Ley 7/2022
  art. 55; RD 126/2015 arts. 4, 4.1.b, 5 y 6.5.a; Rgto. 1169/2011 art. 14.
- **Editorial**: tuteo; 0 restos del Sushi Bar, la Taquería, la Pollería ni la Pizzería (barrido y `gate_restos_ft.py` sobre los 4);
  jerga glosada la primera vez (bola y costra [39], rider [39], blend, smasher, fry-top y línea de montaje [47], runner [47]/[85],
  SERP [57]); «estimación del kit» o «precio estimado por el kit» en carne, pan, queso y patata; cifras de franquicia y de Goiko solo
  para comparar ([63] [115]); el Word no cita las fases del checklist por su nombre (solo «seis fases y 80 tareas» [116]).
- **Integridad** (VPS): los 4 abren; `parche_xml_xlsx.py --check` LIT255 VERDE en los 3 xlsx; `ciclo.sh` TODO VERDE (caché,
  idempotencia, 16/16 protegidas, censo 0, A4); docx 131 párrafos y 10 Heading 1.

## M — Mayores (arregladas)
| # | Dónde | Hallazgo → arreglo |
|---|---|---|
| M1 | calculadora `Patatas!A3` e `Instrucciones!A16` (`calculadora_ham_es.py:572`, `:738-739`) · Word [107] · checklist F3!E14 (`datos_checklist.py:217`) | **Obligación inventada**: «sin añadir aceite nuevo al baño usado». La Orden de 26-1-1989 (leída hoy en origen) solo prohíbe «añadir al baño de fritura sustancias u objetos extraños a los aceites o grasas autorizados» (art. 9.1) y reutilizar el usado en alimentos (9.2); reponer con aceite autorizado no está vetado, y la frase contradecía el «Filtra, rellena y anota cada cambio» del checklist. → «nada ajeno al aceite añadido al baño» (calculadora), «no se añaden al baño sustancias ajenas al aceite» [107] y «no se añade al baño nada ajeno al aceite» (F3!E14, que conserva el «rellena») |
| M2 | Word [50] [57] (`ham_es_a.json`) | La carne madurada «no se puede ofrecer como reclamo» / «no se puede vender como reclamo», en [57] además pegado al «art. 7 del RD 1021/2022»: convierte la prohibición de Inf26008 (no se elabora carne picada con carne madurada más de quince días) en una regla de publicidad y se la atribuye a un artículo que no lo dice → [50] «deja fuera de la carta la «dry aged burger»: según Madrid Salud (Inf26008), no se puede elaborar carne picada con carne madurada más de quince días»; [57] «el picado del día del art. 7.2 del RD 1021/2022, que la carne madurada más de 15 días no se puede picar…» |
| M3 | plan `Supuestos!C13` (`a.py:131-136`) | Puente 24 → 28 % con **puntos inventados** (cierre 1,5 + personal y errores 1,5 + promociones 1 = 4, sobre un ponderado que la calculadora da en 24,4 %: 3,6 puntos) y cifras redondeadas que no son las de la calculadora («24 %», «27 %»; lección SUS-F2 §2.2) → «sale en un 24,4 % … (la smash doble con queso, en un 26,8 % …): entre la receta y la caja se pierden las bolas, el pan y las salsas que se tiran al cierre, las comidas del personal, las invitaciones, los errores y las reclamaciones de la plataforma y sus promociones …, unos 4 puntos en el caso» (= Word [94] y calculadora `Instrucciones!A24`) |
| M4 | calculadora `Escandallo!A42` (`calculadora_ham_es.py:672`) | El aviso fijo decía «trabaja con un 28 %%» (literal sin formato con el `%%` escapado): defecto visible en una celda que lee todo comprador, y que ningún gate caza → «28 %». `grep '%%'` sobre los 4 volcados: 0 |

## m — Menores
| # | Dónde | Hallazgo → estado |
|---|---|---|
| m1 | Word [56] [97] | «En la costa, julio y agosto suben: gira la fila» (girar es para abrir en otro mes; `Tesorería!O5` y F6!E5 lo dicen bien; = Sushi m5) → «cambia los pesos de la fila de estacionalidad». Arreglado |
| m2 | Word [93] | «que suman 110.350 € de compras» (incluye fianza y renta previa; [41] dice inversión; = Sushi m9) → «de inversión sin el fondo». Arreglado |
| m3 | Word [81] · calculadora `Instrucciones!A29` (`:764`) | AESAN recortada: «70 °C durante 2 minutos» / «70 °C durante 2 minutos como mínimo» (R §1: «mayor o igual a 70 ºC durante al menos 2 minutos») → «70 °C o más durante al menos 2 minutos». Arreglado |
| m4 | calculadora `Instrucciones!A28` (`:761-762`) | Regla del 21 % a la vez corta y ancha: «Las bebidas con azúcares o edulcorantes que salen del local» deja fuera la cerveza y mete el batido, que el plan lleva al 10 % → «La cerveza y los refrescos con azúcares o edulcorantes añadidos que salen del local, también los zero, van al 21 %». Arreglado |
| m5 | calculadora `Carne!C15` (`:106`) | «23.000 € + 33 % ÷ 1.840 h ≈ 16 €/h» da 16,6 €/h → «22.000 € (lo más bajo de un cocinero de cadena, que gana de 22.000 a 25.000 €) + 33 % ÷ 1.840 h ≈ 16 €/h» (15,9). Valor por defecto sin cambio. Arreglado |
| m6 | Word [79] · plan `Inversión Inicial!D12` (`semilla_ham.py:79`) | «una de 80 cm va de unos 771 a 1.399 €»: en R §2 los 1.399 € son de una plancha de 600 mm → «una de 60 a 80 cm». Arreglado (la pista de `tandas_docx.py:174` se deja: no es entregable) |
| m7 | checklist F5!B5/E5 (`datos_checklist.py:283-287`) | «Carta corta de unas 14 referencias» enumerando 21 cosas, y «con cebolla a la plancha» donde la calculadora y [47] dicen «estilo Oklahoma» → las 14 filas del escandallo (seis smash con la Oklahoma, pollo crujiente, vegetal, patatas y cargadas, batido, postre, menú y pedido para dos) y, aparte, salsas, refrescos, cerveza y agua. Arreglado |
| m8 | Word [74] · plan `Supuestos!C16` (`a.py:157`) | «Si la plataforma llegara a un tercio de las ventas, pagarías unos 12.300 € más»: 12.300 sale con el 33 % (con un tercio exacto, 12.768) → «al 33 % de las ventas». Arreglado |
| m9 | Word [63] | «te quedas el margen, pero la carta, la carne y la plancha son tuyas» (el «pero» no contrasta), «Esas cifras» ambiguo tras la frase de la marca propia y «conviene razonar las dos cuentas» repetido al final → «pero también el riesgo: la carta, la carne y la plancha dependen de ti. Las cifras de franquicia no sirven…»; recortado a 135 % de longitud. Arreglado |
| m10 | Word [112] | «así que nada de reclamos de maduración» (eco de M2) → «así que fuera de la carta las bolas de carne madurada». Arreglado |

## Aceptados (y por qué)
- **«unos cuatro puntos» / «unos 4 puntos»** para 28,0 − 24,4 = 3,6 ([94], `Supuestos!C13`, calculadora `Instrucciones!A24`): redondeo de una
  diferencia, sin desglose; la misma cifra en las tres fuentes.
- **`Carne!C13` nombra a Smash Hiro** (100 g) cuando [55] habla de «cartas … sin nombres»: dato [medido] de R §0.8 en una nota de herramienta.
- **`Supuestos!C15`**: 1,10 € por pedido + 0,20 € por comensal de sala ≈ 11.400 € frente al 3 % de consumibles (13.680 €): «unos», orden de
  magnitud del caso firmado; el 3 % es la celda que manda.
- **«sólo» con tilde en el checklist y el Excel** frente a «solo» en el Word: estilo heredado de los moldes LIVE de la familia.
- **Avisos de longitud** de [81] [95] [103]-[108] (párrafos legales, 135-220 %): igual que en el Sushi; recortarlos quita citas.
- **«con una carencia, en años, de 1»** ([93]): forma del token `{CARENCIA}` en toda la familia.
