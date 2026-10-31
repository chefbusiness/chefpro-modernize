# Sushi Restaurant Business Plan Kit (EN): revisión adversarial final de la F2 (una ronda)
> Sesión Claude Code, 31-oct-2026 (opus). Sobre el paso real del VPS (`/root/wt-sushi-en`, rama @ `e97a2c2d`), volcado con
> `volcar_en.py`. Pregunta: ¿se puede vender en EE. UU. tal cual? Cruce Word ↔ libro (caché `data_only`) ↔ calculadora ↔
> checklist, legal US (F1 §6), jerga (§9) y restos de otros conjuntos. **0 B · 2 M · 14 m: los 16 ARREGLADOS en fuente (solo
> texto); cifras del caso y valores por defecto intactos (D15 verde).** Parche aplicado = `revision_patch.json` del revisor
> (GSUS-plan 4 · GSUS-check 7 · GR 2 · GRC 2 · GM 1 · docx a 5 · docx b 4 · calculadora 5 reemplazos).

## Hallazgos (B bloqueante · M mayor · m menor), todos ARREGLADOS
| # | Dónde | Qué | Arreglo |
|---|---|---|---|
| M1 | Word ¶49 · `0. Assumptions!C5` (c0008) | Marketplace a $46 «con la carta un 15 % más cara y un pedido mayor»: 41 × 1.15 = $47.15, así que el pedido es algo MENOR (= M1 del ES, que heredaba la research); y $41 ÷ 1.6 = $25.63, no $25.60 | «for about the same basket»; $25.63 |
| M2 | Word ¶104 · `Startup Costs!D14` (c0160) · checklist F1!E7, F3!E7, F3!E9 · calculadora `Fish Yield!A3`, B41, `Instructions!A12` | «El atún exento solo con declaración escrita»: 3-402.11(B) exime al atún sin papel; la declaración escrita (3-402.12(C)) es para la acuicultura; ¶104 omitía bivalvos y huevas enjuagadas | Atún exento; declaración escrita para el pescado de granja; la factura del atún se guarda como regla del kit |
| m1 | Word ¶55 | «El caso pone sus precios dentro de esa banda»: el tuna nigiri ($7.50) y el spicy tuna roll ($9.50) de la calculadora quedan encima | «ejemplos cerca de esa banda» |
| m2 | Word ¶66, ¶114 · checklist F5!E6 (c0789) | «Mucho menos», «cae en picado»: el platter de 24 pasa de $31.60 a $24.83 (≈ −21 %) | «about a fifth less» |
| m3 | Word ¶82 | El sushi chef entra a las 9:30 con 3 h de producción antes de abrir a las 11:30 (Staffing) | 8:30 a.m. |
| m4 | `Staffing!J21` (c0389) | Horas en formato 24 h | a.m./p.m. |
| m5 | `Staffing!J11` (c0375, GR) | La fila «Dish & prep» llevaba la nota del Taco EN de suplencias de vacaciones | Describe dish & prep |
| m6 | Word ¶90 | «grams» | ounces |
| m7 | Word ¶43 | «10 people on the payroll… all W-2» incluye al dueño | «counting you; everyone else W-2» |
| m8 | `Staffing!J5` (c0363) · checklist F4!E6 (c0753) | «In the US the owner is…»: decisión del plan como hecho US | «In this plan…» |
| m9 | checklist F3!E10 (c0727) | El reminder de la consumer advisory no era literal | Texto exacto de 3-603.11 |
| m10 | checklist F3!E11 (c0729) | Descongelación sin el pescado congelado al vacío | Abrir el envase antes de descongelar (Food Code 3-501.13(E), reduced oxygen packaging; norma conocida, no releída en la F1) |
| m11 | Word ¶73 | «with Grubhub's fees on top» | «Grubhub has its own tiers» |
| m12 | checklist F1!E12 (c0642, GRC) | Plazo «Week 1» con la nota «al firmar el local» (semana 6) | «Start in week 1… file when you sign» |
| m13 | calculadora `Sushi Rice!C6` | Insinuaba que el Calrose no es grano medio | «other medium-grain brands» |
| m14 | GM c0410 (`GM.revision.json`) | «Your» con mayúscula a media frase | minúscula |

**Aceptados sin parche**: `P&L!F10` 67/17/15 % (suma 99 %, todo «about», = US §8); ¶80 «about 15 lb» de arroz al día (15.7 con
el descarte); «el margen es el mismo desde el año 1» (redacción común de la familia); workers' comp dentro del 10 % de cargas y
del seguro de $8,000 (prudente, común a la familia).

## Sin hallazgo (comprobado)
Word ↔ caché: 115 × $32.50 × 310 = $1,158,625; $385,156 = $255,100 + $130,056; préstamo $256,000 y cuota $41,663; neto
8.5/10.3/11.4 %; EBITDA 15.8 %; prime cost 64.0 %; equilibrio 93/92; holgura 26 %; DSCR 3.59×; saldo mínimo $140,937 en enero;
payback 2.3/1.6; escenarios −$29,140 / +$303,676. Staffing: 10 personas, 8.60 FTE, todo ≥ $15/h. Calculadora: cifras de la
caché y las cuatro pestañas (`Fish Yield` · `Sushi Rice` · `Costing` · `Instructions`) citadas por su nombre; checklist 80 =
12/15/14/13/13/13 = Word. Legal US: TPHC, variance, sin pH legal, registros 90 días, histamina 40 °F, CFPM, beer & wine con el
sake, 9 alérgenos con sésamo, moluscos y mostaza no major, «gluten-free» y «sushi-grade» solo negados, nota UK al final de ¶108.
Cero español y cero vocabulario de otros kits; productos del cierre, todos en la tienda EN.

## Gates finales (VPS, tras la ronda)
`check_textos --todas` 0 errores · `mapas` 0 errores · `aplicar_en --idempotencia` 0 dif. · **D15 VERDE** ($256,000; 8.5/10.3/
11.4 %; DSCR 3.59×) · `ensamblar_docx` G8 VERDE · calculadora generada + autotest **585 VERDE** · `gates_en` **G1-G9 TODO VERDE**
· `--autotest` 20/20 · docx 8/8 · barrido 4 ficheros / 1,718 piezas / 0 fallos · resumen 3,386 piezas 0/0/0 · `censo-entregables
--fail --letter` 0 defectos · `gate-no-latinos` 0 · `parche_xml_xlsx.py --check` LIT255 VERDE · 2.ª pasada `canon.py` **4/4
IGUAL** · sha256 Mac = VPS.

## sha256 (Mac = VPS)
- `sushi-restaurant-business-plan.docx` 128ea08bc715e9a11268ffa366228049fb9bf9b3724a9a03ccb3e7a36ef19600
- `sushi-restaurant-financial-projections.xlsx` 027979656270ceb38553620bb95eb75d471c433716a1effbb32f9c9883bff10f
- `sushi-restaurant-startup-checklist.xlsx` c8be8548c56f5dcf495fcad603dc06f70aec4f6a040abee59b369671b38f9b46
- `sushi-fish-rice-costing-calculator.xlsx` bd058e7d766ce4b49b6d2a6e6ed6dd63029e0c1ade5dc81a85bd87e79a1e867c
