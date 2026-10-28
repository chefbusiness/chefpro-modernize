# Plan de Negocio: Cafetería Móvil para Eventos ES 1.0 — F2 (motor) · calibración, decisiones y gates

> Sesión Claude Code, 28-oct-2026. Implementador del MOTOR de la F2 (plan financiero + checklist) y de la herramienta del
> Word (sin redactar). SPEC: `SPEC.md` (D1-D16); cómo: `F1-camino.md` §1-§4 y §7; caso: `F1-research-cafeteria-movil.md`
> §1-§4 y §8. Código en el Mac (worktree de `feat/plan-negocio-cafeteria-movil`); motor y xlsx en el VPS
> (`/root/wt-cafemovil`, venv `/root/venv-guias`, salidas en `/root/tmp-caf-f2/`). Cero código común: ni `motor.py`, ni
> `grupo_a.py`, ni `main.py`, ni el pid en `PRODUCTOS`.

## 1. Ficheros

| Fichero | Qué es |
|---|---|
| `planes-v2_0/contenido_plan_negocio_cafeteria_movil_eventos/{__init__,a}.py` | Contenido: mecánica del parrillero 2.2 (motor de eventos sin permutar, base sin local por `VOCABULARIO`, furgoneta como «obra», fijos discontinuos) + injerto del Mes 1 girado de la finca (tupla con `assert`, `mes_paga_1/2` = 5 y 10, notas de Tesorería `O5`, `O13` y `A34` por `VOCABULARIO`). Las 4 frases del IVA del motor que hablaban de alcohol (`Supuestos!C9`, `C40`, `Instrucciones!A8`, `Tesorería!O16`) reescritas por `VOCABULARIO`; las de `a.py` (`C16`, `C62`, `C63`), en el propio módulo. La tabla de escalado de `Instrucciones` se importa de `datos_escalado.py` (fuente única del agente de la calculadora, SPEC D13) |
| `plan-cafeteria-movil/semilla_caf.py` | `semilla_par.py` sobre el **Food Truck 2.2**: 14 partidas (42.000 €), 10 fijos (7.880 €: los 7.700 de la SPEC + 180 de calibración), títulos, supuestos, checklist, docProps y `Instrucciones!A3` del checklist con el NOMBRE del producto |
| `plan-cafeteria-movil/datos_checklist.py` | 80 tareas: 12 · 16 · 14 · 10 · 14 · 14 (constitución · vehículo y sanidad · equipo y proveedores · personal y formación · marca y captación · primer evento y 90 días), sólo con lo legal de la SPEC D10-D11 y D16 |
| `plan-cafeteria-movil/caf_version.py` · `main_caf.py` · `ciclo.sh` | «1.0 · octubre 2026» (D3; si el merge cae en noviembre, se cambia `MES` aquí y se regeneran los 4 ficheros); `ciclo.sh` para si falta `datos_escalado.py` |
| `plan-cafeteria-movil/cifras_caf_es.py` | 248 tokens para el Word (`cifras_caso_es.json`: Excel + calculadora + tabla de escalado `TE…`) y los 12 gates D9 |
| `plan-cafeteria-movil/barrido_es.py` | `tandas_docx.PROHIBIDOS` (D12: los 12 del research §8 + los del brief de la pizzería + restos FT/parrillero/finca + motor sin traducir) + `RX_CAMPANA` + `RX_PUBLICA`; patrones en minúscula inicial, sensibles a mayúsculas («Payback» a mitad de frase). SIN bollería, leche, generador, furgoneta, remolque ni aparcamiento |
| `plan-cafeteria-movil/tandas_docx.py` · `docx_caf_es.py` · `BRIEF-REDACTORES.md` | Herramienta del Word (§6): pistas con D10-D16, gemelas finca (formato) y parrillero (oficio) |

No se tocan (otros agentes): `calculadora_caf_es.py`, `datos_escalado.py`, `contrato_caf_es.py`, `textos/contrato_es.json`.

## 2. Decisiones que se apartan de la SPEC o del camino (y por qué)

1. **Driver sin permutar** (B4 = 135 invitados por evento, B5 = precio por invitado, B6 = 130 eventos). La SPEC D5 dice
   «B4 = eventos (como catering y finca)», pero catering y finca NO permutan (`catering-es-2_0/F1-camino-2_0.md` §1.2:
   permutar rompe la cobertura de personal, que multiplica por B6). Se sigue a los hermanos y al camino §2; en euros es
   lo mismo (107.055 € con el precio del research).
2. **Crecimiento 10 % / 8 %** (research y SPEC D5: 8 % / 5 %). **Imposibilidad estructural de la demo §2.11.5 del
   motor** (ramas del IS): el motor suma 6.000 € fijos de incorporaciones en los años 2 y 3 (`grupo_a.py:1484`, valor
   fijo, no lo lee del contenido ni lo conserva del libro). En el equilibrio, el margen que añade el crecimiento es ≈
   crec × costes fijos (≈ 66.700 €): con el 8 % son ≈ 5.300 € < 6.000 €, así que el RAI del año 2 es SIEMPRE menor que
   el del año 1 en todos los ensayos (medido: 132 → −43 €, 119 → −630 €, 116 → −764 €) y no hay ventana RAI1 < 0 < RAI2;
   el año 3 (5 %) tampoco tributa. Con 10 % / 8 % se abre (ver §3). Ninguna palanca de D9 (precio, eventos, fijo,
   propios, préstamo) mueve esa diferencia: sólo el crecimiento o los costes fijos totales (harían falta > 90.000 €).
   **Es la decisión que el orquestador tiene que validar.**
3. **Mezcla 11 / 89** (SPEC D5: 10 / 90). La demo §2.11.9 sube `coste_comida` 5 puntos y exige que `r_cogs` se mueva
   MÁS de 0,005 (`grupo_a.py:5451`, `delta > 0.005`); con el 10 % se mueve exactamente 0,005 (medido: 0,19 → 0,195) y
   falla. El camino decía «≥ 10 %»: es «> 10 %».
4. **Plantilla de 4 filas** (D8: titular + camarero/a al 36 % «y el resto a 0 o suplencias»): a 0 no se puede (el
   semáforo del SMI se pone ROJO con 0 personas, porque `grupo_a` convierte la jornada 0 en 1,0). Filas 3-4 =
   suplencias de vacaciones y bajas y refuerzo para eventos grandes, cada una al 4 % (56 €/mes de bruto): +2.086 €/año.
5. **Bodas a 9,00 €** (palanca 1 de D9): B5 = 6,20 € (mezcla 6,15 €, redondeada como el research redondeó 6,05 → 6,10).
   Ojo de coherencia: la boda de ejemplo de la calculadora sale a **8,00 €** por invitado con su margen objetivo del 55 %;
   el Word lo explica («la boda media del plan, a 9,00 €, deja más margen»). Si el orquestador prefiere alinear, se
   puede subir el margen de la boda de la calculadora (otro agente).
6. **Asesoría 1.680 €** (+180 €, «fijo ±100» de D9) y **préstamo 44.500 €** (research ≈ 41.000 €: RD-34 pedía +2.908 €
   con la base de 41.000 y luego +2 € tras el fijo).
7. Texto del checklist «Cobro y factura» → «Facturas y vencimientos del evento»: el gate de ortografía del motor marcaba
   «Cobro» como pendiente §1.7.
8. **SPEC D16** (cobro 30/70, cancelación en 4 tramos) metida en la nota de `dias_cobro`, en una referencia de
   `Instrucciones`, en el checklist (F6) y en las pistas del Word (§5, literal en la entrada de las tandas).

## 3. Calibración (3 vueltas, la máxima de D9)

| Vuelta | Cambio | Resultado |
|---|---|---|
| 0 | caso del research (135 × 6,10 × 130; 10/90; 8 %/5 %; 41.000 €) | exit 1: §2.11.5 (sin ventana), §2.11.9 (0,005), RD-34 −2.908 € (−4,2 %); neto A3 5,3 % (IS al 25 %) |
| 1 | mezcla 11/89 · préstamo 44.000 € · crecimiento 10 %/8 % | exit 1: sólo §2.11.5 (D2 ≈ +520-690 € cerca del equilibrio, pero ningún ensayo en la ventana) |
| 2 | palanca 1: bodas a 9,00 € → B5 6,20 € | exit 1: sólo §2.11.5 (ensayo 116: RAI1 −235 €, RAI2 +388 €: falta RAI1 < −D2/2) |
| 3 | asesoría +180 € · préstamo 44.500 € | **TODO VERDE** · D9 VERDE. Demo a 116 invitados: RAI1 −448 €, RAI2 +175 € < BIN 448 €, IS3 36 € al 15 % |

Ventana de la demo: de unos −135 a +65 € de fijos sobre el caso final (estrecha, como en el parrillero). Si cambia CUALQUIER cifra del
caso, se vuelve a mirar `ensayos` en `inf.json` (`ens5`: ver §6) y se mueve un fijo.

## 4. Cifras del caso (`cifras_caso_es.json`, 248 tokens)

- **Actividad**: 130 eventos × 135 invitados × 6,20 € sin IVA (6,82 € con IVA; 837 € de factura media). Ventas
  **108.810 / 119.691 / 129.266 €**; dulces 11 % · bebidas 89 %, todo al 10 %. Venta directa 8,4 % (mezcla: 8,3 %),
  canon 15 % (1.371 €).
- **Márgenes**: mercancía 19,3 %; margen bruto 70,8 %; personal 44.986 € (41,3 %; 44,1 % el año 3); base 4,4 %; EBITDA
  17.395 € (16,0 %); RAI 10.401 €; neto **8.840 € (8,1 %) / 10.292 € (8,6 %) / 10.050 € (7,8 %)** (el año 3 al 25 %).
- **Inversión**: 14 partidas 42.000 € + imprevistos 1.216 € · CAPEX 44.416 € · fondo 15.645 € · inversión total
  60.061 € · IVA 8.949 € · **necesidad 69.010 €**. Financiación 25.000 € + **44.500 €** al 6,5 %, 6 años con 1 de
  carencia; cuota 10.708 €; exceso 490 € (0,7 %). **DSCR 1,61 / 1,54 (mínimo 1,54)**.
- **Equilibrio**: contable 117 invitados por evento o 113 eventos del tamaño medio (holgura 15,6 %); caja 106 eventos
  (**holgura 23,2 %** el año 1; **11,0 %** y **11,1 %** los años 2 y 3, con 129 y 139 eventos del tamaño del año 1).
- **Tesorería**: Mes 1 = marzo; **saldo mínimo 12.124 € en el Mes 2 (abril)**; cierre 30.156 €. Payback «Más de 3
  años» (2,7 sobre el CAPEX). Cobertura de horas **170 %** (2.650 contratadas / 1.560 de eventos; el resto, oficina).
- **Escenarios**: pesimista 110 × 130 × 5,70 € = 81.510 € → neto −8.939 €; optimista 145 × 140 × 6,30 € = 127.890 € →
  +20.329 €.
- **Calculadora** (caché del xlsx publicado en el Mac, copiado a `/root/tmp-caf-f2/calc_pub/`): espresso 0,39 €, latte
  0,81 €, media 0,59 € + 0,12 € de envase; boda de ejemplo 8,00 €/invitado, congreso 4,50 €, feria +128 €. Si la
  calculadora cambia, se vuelve a pasar `cifras_caf_es.py --calc` antes del Word.

## 5. Gotchas

- La demo §2.11.5 no tiene ventana en un negocio pequeño con crecimiento del 8 %: es aritmética del motor (6.000 € de
  incorporaciones fijas), no del caso (§2.2).
- `VOCABULARIO` casa con `\b` en los dos extremos y en UNA pasada de la clave más larga a la más corta: las frases largas
  del IVA ganan a «en sala» o «refrescos o zumos…». La clave termina en letra o cifra («…37/1992», no «…37/1992)»).
- La plantilla del molde FT tiene 4 filas exactas y ninguna puede ir a 0 personas (semáforo del SMI).
- El rsync Mac → VPS excluye los ficheros de los otros dos agentes y `tandas/` (el Word se prepara en el Mac).

## 6. Comandos para regenerar

```bash
W=<worktree del Mac>; S=scripts/productos-digitales
rsync -a --exclude calculadora_caf_es.py --exclude datos_escalado.py --exclude contrato_caf_es.py --exclude 'textos/contrato_es.json' --exclude __pycache__ --exclude 'tandas/' "$W/$S/plan-cafeteria-movil/" vps:/root/wt-cafemovil/$S/plan-cafeteria-movil/
rsync -a --exclude __pycache__ "$W/$S/planes-v2_0/contenido_plan_negocio_cafeteria_movil_eventos/" vps:/root/wt-cafemovil/$S/planes-v2_0/contenido_plan_negocio_cafeteria_movil_eventos/
ssh vps 'cd /root/wt-cafemovil/scripts/productos-digitales/plan-cafeteria-movil && bash ciclo.sh && tail -1 /root/tmp-caf-f2/motor/run.log'
# ventana de la demo §2.11.5: ensayos de inf.json
ssh vps '/root/venv-guias/bin/python -c "import json;e=json.load(open(\"/root/tmp-caf-f2/motor/inf.json\"))[\"demostraciones\"][\"demostraciones_2_11\"][\"5_IS_con_BIN_y_tipo_de_nueva_creacion\"];[print(x) for x in e[\"ensayos\"]]"'
ssh vps 'cd /root/wt-cafemovil/scripts/productos-digitales/plan-cafeteria-movil && D=/root/tmp-caf-f2/motor/dryrun/plan-negocio-cafeteria-movil-eventos &&
  /root/venv-guias/bin/python cifras_caf_es.py --xlsx $D/plan-financiero-cafeteria-movil-eventos.xlsx \
    --calc /root/tmp-caf-f2/calc_pub/calculadora-escandallo-presupuesto-cafe-eventos.xlsx --salida /root/tmp-caf-f2/cifras_caso_es.json &&
  cp /root/tmp-caf-f2/cifras_caso_es.json . &&
  /root/venv-guias/bin/python barrido_es.py $D/*.xlsx &&
  /root/venv-guias/bin/python ../catering-es-2_0/gate_restos_ft.py $D --rx-extra "parrill|\basad[oa]s?\b|\bbrasas?\b|carb[oó]n|\bcarnes?\b|cocina de apoyo|show de fuego|plan-negocio-parrillero|\bcami[oó]n\b|ventanilla" &&
  cp $D/*.xlsx /root/wt-cafemovil/astro-site/public/dl/plan-negocio-cafeteria-movil-eventos/'
scp vps:/root/tmp-caf-f2/motor/dryrun/plan-negocio-cafeteria-movil-eventos/{plan-financiero,checklist-apertura}-cafeteria-movil-eventos.xlsx "$W/astro-site/public/dl/plan-negocio-cafeteria-movil-eventos/"
scp vps:/root/tmp-caf-f2/cifras_caso_es.json "$W/$S/plan-cafeteria-movil/"
# Word: Mac (sólo JSON) → 2 redactores Sonnet → check → VPS ensambla
python3 $S/plan-cafeteria-movil/tandas_docx.py preparar
python3 $S/plan-cafeteria-movil/tandas_docx.py check --tanda caf_es_a        # y caf_es_b
ssh vps 'cd /root/wt-cafemovil/scripts/productos-digitales/plan-cafeteria-movil && /root/venv-guias/bin/python docx_caf_es.py --salida /root/tmp-caf-f2/docx && /root/venv-guias/bin/python barrido_es.py /root/tmp-caf-f2/docx/*.docx'
```

(La calculadora del `--calc` es la que publicó su agente en el Mac: si cambia, cópiala antes a `/root/tmp-caf-f2/calc_pub/`.)

## 7. Gates de este paso (VPS, 28-oct)

`ciclo.sh`: main.py exit 0, **TODO VERDE** (idempotencia 0 · caché 656/722 + 12, 0 fallos pycel · data_only 667 con
valor, 66 «""», 0 fallos · blancos 0 · §9 13/13 · checklist C2 80 ítems · censo `--fail` 0 · moldes 30/30 · 16/16
protegidas · demos) · `cifras_caf_es.py` **D9 VERDE** (12/12) · `barrido_es.py` **0** en los 2 xlsx ·
`gate_restos_ft.py --rx-extra` **VERDE** (2 ficheros). sha256 Mac = VPS: plan `300c12df…c397`, checklist
`1d1603a0…c1`. `tandas_docx.py preparar`: `caf_es_a` 29 ranuras / 2.954 palabras · `caf_es_b` 32 / 3.765 (6.719 en
total) · 248 tokens. `docx_caf_es.py --parcial`: 131 párrafos, 10 Heading 1, A4, VERDE en modo ensayo; barrido 0.

## 8. Deuda

- Validar §2.2 (crecimiento 10/8 %) y §2.5 (boda de la calculadora a 8 € frente a 9 € del plan).
- El texto de la calculadora (otro agente) dice «ticket» en `Escandallo!A51` y `A54`: el barrido del orquestador lo
  cazará en el gate de los 5 ficheros («tique», o «precio medio»).
- La guía de equivalencias (censo 54 → 55) y `gate-no-latinos` son de la F3.

## 9. Arreglos de la revisión (`REVISION-FINAL.md`, ronda única, 28-oct)

Me tocaban M1, M2, M4, M5, m1-m21 y m24. B1, M3, M6, m22, m23 y m25-m27 son de los agentes de la calculadora y del
contrato (no tocados; exclusiones de rsync mantenidas). **No cambia ninguna cifra del caso**: el ensayo de la demo
§2.11.5 sigue en 116 invitados (RAI1 −448 €, RAI2 +175 €, IS3 36 €), y los 12 gates D9 dan lo mismo que en §4.

| # | Estado | Cómo |
|---|---|---|
| M1 | Aplicado | Word [94]: «… y el resto de gastos fijos ({OTROS_FIJOS_A1}: suministros, seguros, asesoría, marketing, mantenimiento y tasas)»; token nuevo `OTROS_FIJOS_A1` = fijos − personal − almacén − amortización − intereses = 9.900 € (77.081 − 44.986 − 4.800 − 9.900 = 17.395 €) |
| M2 | Aplicado | [58] y [112]: equilibrio de caja por año con `{BE_EVENTOS_ANO_CAJA}`, `{BE_EVENTOS_CAJA_A2}` y `{BE_EVENTOS_CAJA_A3}` (106 · 129 · 139); en [58] además lo que hace el plan (`{EVENTOS_EQUIVALENTES_A2/A3}`: 143 y 154), para que no parezca que el plan está por debajo · [65]: «pasar cuanto antes de los {BE_EVENTOS_ANO_CAJA} servicios del equilibrio de caja» · pistas §4 y §10 de `tandas_docx.py` |
| M4 | Aplicado | Checklist F2 `E5`: «(sección 2)» |
| M5 | **Parcial (deuda de código común)** | `G35` no se puede poner a 0 desde el contenido: `grupo_a.py:2544-2547` pone `iva=P('iva_soportado')` a TODAS las filas propias de fijos, y la columna G es fórmula protegida (no se le puede decir al cliente «pon 0»). Nota `F35` reescrita para que no se contradiga: «Las tasas municipales no llevan IVA, pero el libro aplica a todos los costes fijos el tipo general…: aquí suma unos 63 € al año de IVA que pagas y te deduces en el mismo trimestre, sin efecto en el resultado». Corregido también el comentario de `semilla_caf.py` (la creencia de que `RX_SIN_IVA` lo cubría). Arreglo de verdad: una clave de contenido con el IVA por fila de fijos, en el motor (pasada de familia) |
| m1 | Aplicado | [66] «una factura media baja, de {VENTA_EVENTO_MEDIO} por evento» (fuera el «de de») |
| m2 | Aplicado | [73] «un precio mínimo de {EJ_BODA_PRECIO} … para llegar al margen objetivo del 55 %» + pista §5 |
| m3 | Aplicado | [94] salvedad de los tipos de 2025 por cifra de negocios (1 millón / 10 millones de euros) |
| m4 | Aplicado | [98] y [111] «con margen sobre el {DSCR_OBJETIVO} que suele pedir un banco, aunque no sobrado» (token nuevo `DSCR_OBJETIVO` = `Supuestos!B66`) |
| m5 | Aplicado | [103], `Supuestos!C24`, checklist F2 `E8`, pista §9 y docstring del checklist: el art. 13.5.b habla de no preparar en casa lo que se sirve en eventos; el trastero sin agua «no sirve para lavar loza ni depósitos» |
| m6 | Aplicado | [103] «a 4 °C o menos (o congelada)» + la referencia «Comida testigo» de `Instrucciones` + pista §9 |
| m7 | Aplicado | [46] y [106] «no lleva matrícula propia y sí (su) tarjeta ITV»; [46] «A la furgoneta equipada se la llama a veces coffee truck»; checklist F2 `B7`; pistas §2 y §9 |
| m8 | Aplicado | [74], [108], `Instrucciones!D45`, checklist F6 `E8` y la constante `COBRO` de las pistas: «el 10, el 30 o el 60 %, y en el último tramo el 100 % menos los costes que…» |
| m9 | Aplicado | [114] texto propuesto |
| m10 | Aplicado | [115] «anota en NOTAS la fecha y quién las cerró» |
| m11 | Aplicado | [39] añade la guía de equivalencias para Hispanoamérica |
| m12 | Aplicado | [80] baterías «más silenciosas para las bodas pero más caras (6.000-10.000 € …)» |
| m13 | Aplicado | [93] «{CAPEX} de inversión» |
| m14 | Aplicado | Unificado a «de una semana a seis meses»: [97] (texto propuesto), `Supuestos!C52`, `Instrucciones!D35`, `Tesorería!O5` |
| m15 | Aplicado | [55] «por kilómetro (0,45 € en una ficha) o con un recargo fijo» + pista §3 |
| m16 | Aplicado | [105] «No está claro que una boda o un evento de empresa cuenten como evento festivo, así que…» + pista §9 |
| m17 | Aplicado | `Personal!A7` «Suplencias y refuerzo de temporada (fijo discontinuo)» con nota del contrato de sustitución (art. 15.3 ET); [87] añade la frase propuesta; [43] y [85] sin «bajas»; pista §7 |
| m18 | Aplicado | `Supuestos!C58` «la mitad de las ventas» |
| m19 | Aplicado | `VOCABULARIO`: «Compáralo con el precio por invitado de las barras de tu zona, que suele ir con IVA». Para que el literal de la fórmula de `Supuestos!C9` no pase de 255 caracteres (pasaba a 269), se acorta la frase del IVA que va delante (queda en 225) |
| m20 | Aplicado | `VOCABULARIO`: «meses de renta» → «cuotas del almacén base», «renta» → «cuota» (sólo aparecía en `Inversión!D21-D22`) y «de puesta en marcha (montaje del almacén, calibrado de la cafetera, catas y primeras reservas)» |
| m21 | Aplicado | `Inversión!D7`: aviso de ITP y REBU con «pon «No» en la columna de al lado» |
| m24 | Aplicado **de otra forma** | El motor reutiliza el desplegable que trae la hoja (`motor._dv_marca_existente`) y, si no hay ninguno, crea «✓,—,N/A»; su leyenda (`motor.LEYENDA_OK`) dice «☐» y las casillas vienen con «☐». La semilla dejaba la hoja sin desplegable; ahora le pone «✓,☐,N/A» (el de la familia, `motor.py:162`) y el motor lo reutiliza: desplegable, leyenda y casillas coinciden sin tocar la leyenda común. F6 `C12` y `C15`: «Camarero/a» |

**Gates tras los arreglos (VPS)**: `ciclo.sh` TODO VERDE (con `datos_escalado.py` md5 `a35a2aab…`, ya con el M3 del
agente de la calculadora) · `cifras_caf_es.py` D9 12/12 (250 tokens) · `tandas_docx.py check` A y B: 0 errores (avisos:
longitudes de [58], [74], [97] y [108] por encima del objetivo, y cifras con fuente: 295 €, arts. 13.5, 30.8 y 91) ·
`docx_caf_es.py` VERDE (131 párrafos, 10 H1, 7.235 palabras) · `barrido_es.py` 0 en los 2 xlsx y el docx ·
`gate_restos_ft.py --rx-extra … --permitir "«food truck cafetería»"` VERDE (3 ficheros; la búsqueda del §3 es
legítima). sha256 Mac = VPS: plan `1efbd94d…125c`, checklist `17318729…0fca`, Word `32e4037e…10bb`.

**Deuda nueva**: (1) M5, IVA por fila de fijos en el motor; (2) el motor escribe literales de fórmula de más de 255
caracteres en textos comunes (`Inversión!D28` 313, `D33` 424, en todos los planes de la familia, publicados sin incidencias
conocidas): conviene partirlos en la próxima pasada del motor.
