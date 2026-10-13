# Mobile Bar Business Plan Kit (EN) — F2 (entregables) · notas

> Sesión Claude Code, 13-oct-2026. **Paso 1 de la F2** (conjunto «mbar», extracción, reuso del catering, caso US + D15,
> 4 tandas, calculadora D89-D90, regresión). Implementador único, sin subagentes. Código en el Mac; lo que abre
> xlsx/docx, en el **VPS** (`/root/wt-mbar`, venv `/root/venv-guias`). Rama `feat/mobile-bar-business-plan-en`.
> A mitad del paso, instrucción de John (13-oct): **todas las medidas en el sistema US** con la métrica entre
> paréntesis (§4.7); aplicada a la calculadora, a `datos_mbar.py` y al brief, y regenerado lo ya generado.

## 1. Cómo se montó el conjunto «mbar» (fuente ES del circuito = FOOD TRUCK ES; diccionario = CATERING EN)

`BP_CONJUNTO=mbar` → `mapas_mbar.instalar(M)`, `mapas.DATOS = business-plans-en-5/`, lanzador `bp5.py`. **Único cambio
en código común**: la rama `elif CONJUNTO == 'mbar'` de `business-plans-en/mapas.py` (+ el mensaje de error). Lo nuevo
frente al catering: el **reuso por celda lee el EN publicado del catering** (`../business-plans-en-4/textos_es.json` +
`textos_en/{GM,GR,GCAT-plan,GCAT-check}.json` con `GR.revision.json`), con los **8 sha256 del diccionario fijados** en
`mapas_mbar.SHA_DICCIONARIO` (`bp5.py verificar` los comprueba: hoy 0 derivas).

| Fichero | Qué lleva |
|---|---|
| `mapas_mbar.py` | Producto D81-D83 (`dir_es` = FT ES, `slug_es` = coctelería ES), libros `MBP`/`MBC`, pestaña F2 «Phase 2 - Trailer & Permits» (27 car.), 68 tareas 11/13/12/10/12/10, **7 parches** del catering con el Break-Even en **±$1 / +$2** (D88), zonas D18/D19/TAREA, docx 131 ranuras, `CAT_CELDA` / `CAT_TEXTO` (diccionario), `RX_REESCRIBIR` (comida, cocina, comisaria, furgoneta, catering, menu…) y `grupo_de` / `reuso_de` |
| `datos_mbar.py` | FIJOS (30 nuevos: motor, títulos, D19, dos líneas de venta), POR_CELDA (65: Supuestos, inversión 7-23 y A31, P&L A10-A11/A22/A24-A27/A30-A35/A52/A55, 4 puestos + cobertura + nota W-2/propinas, `Cash Flow!O5`, notas del motor C20/C39/C67/E24), cifras prohibidas + `RX_BAR_NO` (D93), 117 tokens (alias de eventos + 9 partidas propias + 3 derivadas), 61 `DOCX_NOTAS` (§9 = 7 notas D92), pistas (caso, D18, 14 filas D19, **68 tareas `TAREAS_MBAR`** con «[sobrevive]» en las ranuras del catering que se conservan), glosario §9 completo, `REGLA_UNIDADES`, caso US, `CALIBRACION_D15`, FORMULAS_EN |
| `bp5.py` | Lanzador (copia de `bp4.py`) + `verificar` (272 celdas de tarea en GMB-check + sha256 del diccionario) + `fuente` + `calculadora` + `barrido` |
| `fuente_mbar.py` → `fuente_es_mbar.json` | Contenido de la coctelería ES para los redactores: checklist de **6 hojas** (71 tareas, 7 SOLO_ES), plan (116 párrafos), carta de **15 recetas** (ml), 10 experiencias (116 párrafos), contrato (46) |
| `calculadora_mbar.py` · `barrido_mbar.py` · `BRIEF-TRADUCTORES.md` | D89-D90 (§5) · barrido del paso 3 · brief de las 4 tandas con el **glosario §9 completo pegado** y la regla de medidas |

**Grupos** (`textos_es.json`, 959 cadenas; los ids son los mismos tras la re-extracción de las medidas):

| Grupo | Cadenas | Palabras ES | Qué es | Va a |
|---|---|---|---|---|
| GM | 313 | 3.500 | Motor cuyo EN del catering (= el del FT) no habla de comida ni de catering | nadie: `textos_en/GM.json` ya escrito |
| GRC-plan | 77 | 1.353 | EN del catering que vale con revisión: 57 celdas de la tabla D18 + 20 notas del motor | `textos_en/GRC-plan.json` escrito; revisión en la tanda (a) |
| **GMB-plan** | 130 | 3.241 (entrada) | 74 de texto libre (notas C de Supuestos, D de inversión, F del P&L, J de Staffing, Instrucciones…) + 56 celdas D19 (sin propuesta) | tanda 1 (a) |
| **GMB-check** | 275 | 1.277 | 68 tareas × 4 columnas (una por celda) + 3 textos del checklist (títulos de las fases 1 y 3, nota del contador) | tanda 1 (b) |
| GX | 164 | 890 | Pestañas, CLAVES, FIJOS, POR_CELDA, versión, pie, docProps | nadie |

Docx (`docx_es_mbar.json`, VERDE): 131 párrafos, 0 multi-run; 61 ranuras → **mbar_a 29 / 2.954 palabras de ranura ·
mbar_b 32 / 3.765**, cada una con su nota de bar móvil (`DOCX_NOTAS`); el EN del catering de la misma ranura es el modelo
de estructura (brief).

## 2. No regresión (VPS, con la rama `mbar` en `mapas.py`; mismos comandos que `../business-plans-en-4/F2-NOTAS.md` §2)

| Conjunto | `mapas` | `gates_en` (dl/ publicados) · `--autotest` | `ensamblar_docx --autotest` | `check_textos --todas` |
|---|---|---|---|---|
| FT/CAF (`mapas.py`, `gates_en.py`…) | 0 errores | **TODO VERDE** G1-G9 · **20/20** | **18/18** | las 7 OK |
| REST/PAN (`bp2.py`) | 0 errores | **TODO VERDE** · **20/20** | **16/16** | las 8 OK |
| BAR (`bp3.py`) | 0 errores | **TODO VERDE** · **20/20** | **8/8** | las 6 OK |
| CAT (`bp4.py`) | 0 errores | **TODO VERDE** · **20/20** · calculadora `--autotest` VERDE (136) | **8/8** | las 6 OK |
| MBAR (`bp5.py`) | 0 errores (cruce con el censo + `verificar` OK, diccionario sin deriva) | parcial G1, G3-G7 **VERDE** sobre el dry-run | **8/8** | GM OK · GRC-plan OK · el resto, pendiente de redactar |

## 3. Caso US, dry-run y calibración D15 (`bp5.py aplicar_en --dry-run --parcial --salida /tmp/mbar-dry`, VPS)

Research §8 tal cual (160 eventos × $14 × 95 invitados): **D15 en verde sin tocar `B4` ni `B35`** (holgura 20.3 %, DSCR
mín 2.77, saldo mín > 0, cobertura 131 %), pero el punto fijo del préstamo daba **$52,000**, por encima del tope de
$50,000 del **SBA Microloan** en el que D85 encaja el caso. `CALIBRACION_D15` (G7 exige cada celda citada aquí):

| Celda | Research | Calibrado | Motivo |
|---|---|---|---|
| MBP 0. Supuestos!B30 | 26,000 | **28,000** | D85: con 28,000 de fondos propios el préstamo de punto fijo baja a **$49,000** (≤ tope del Microloan); D15 ya estaba en verde |

Resultado (caché del dry-run, `cifras_caso.json` de esta carpeta, 117 tokens, sha256 `6f0d370d6a8dcb73…`): ventas
**$212,800** / $234,080 / $252,806 (**$1,330 por evento**, 15,200 invitados) · CAPEX **$47,530** + fondo de maniobra
$29,442 = **$76,972** · fondos propios $28,000 (36 %) + préstamo **$49,000** al 10 % a 7 años (cuota $10,065; semilla
`PRESTAMO_SEMILLA` = 49,000, punto fijo en 2 vueltas) · margen bruto **69.8 %** · mercancía 19.1 % · personal **36.8 %**
($78,368) · storage y parking 3.4 % · EBITDA $35,772 (**16.8 %**) · neto **$18,790 (8.8 %)** / $28,076 / $36,062 ·
equilibrio **134 eventos/año** contable y **133** de caja frente a 160 → holgura **21 %** (caída absorbible 17 %) · **DSCR
mín 2.93×** · saldo mínimo $26,754 (mes 1) · payback 2.2 años (1.5 sobre el CAPEX) · 9 personas = 1.85 FTE, cobertura
131 % · seguros $4,000 · pesimista (120 · $12.60 · 86) **$130,032, −$32,760 y caja estimada −$2,664: se agota** (el docx
§8 tiene que decirlo) · optimista (200 · $15.40 · 105) $323,400 y +$102,308. Los 5 umbrales del P&L (D88: margen bruto ≥ 65
%, mercancía ≤ 26 %, personal ≤ 40 %, storage ≤ 6 %, neto ≥ 5 %) en verde los 3 años.

`bp5.py gates_en --dir /tmp/mbar-dry --parcial --solo G1,G3,G4,G5,G6,G7`: **TODO VERDE** (722 fórmulas; 68 tareas
[11, 13, 12, 10, 12, 10]; 16 hojas Letter; 202 valores bajo DV; 8 rangos de CF; caché = referencia ES recalculada, 0
diferencias; 113 valores del caso y 1 calibración citada). Barrido de las celdas ya en EN del dry-run (GM, GRC-plan, GX:
2.864 piezas) contra cifras prohibidas y `RX_BAR_NO`: 0 fugas (las 3 notas de fórmula del FT con FOOD / BEVERAGE se
cambiaron, §4.5); lo que queda es ES pendiente de los redactores.

## 4. Decisiones y desviaciones de la SPEC

1. **Recuentos de grupos** (inventario §1 estimaba GM 322 · GRC 94 · GMB-plan 128 · GMB-check 272): GM **313** y GX
   **164** porque 17 rótulos con comida («FOOD share», «Cost of goods sold — food», «Disposables and packaging»…) se fijan
   en `POR_CELDA`/FIJOS en vez de mandarlos a los redactores; GRC-plan **77**; GMB-check **275**, porque los 3 textos del
   checklist que no son motor limpio van al redactor del checklist y no a la revisión del plan.
2. **Calibración** (§3): fondos propios en vez de `B4`/`B35`, para cumplir la frase de D85 «≈ $50K; SBA Microloan».
3. **«60 guests» no se veta** como frase del caso del catering: el cumpleaños de 60 invitados es un ejemplo de D90 y de la
   mezcla de research §8. Se vetan «180 events» (el caso es 160) y «$60 per guest»; y los importes ≥ 10,000 del catering y
   del FT (salvo los que coinciden con un valor propio del caso).
4. **Lista blanca de `RX_BAR_NO`**: «commissary» y «food» valen si el texto habla del condado, del health department o del
   FDA Food Code (el «contexto legal» de D93); «mobile food vendors», «food handler card», «FDA Food Code», «alcohol
   server», «server certification» y «AI Chef Pro» no saltan; «chef» y «kitchen» se permiten en la firma de John
   (`FIRMA_EN`). «menu», «van» y «catering» NO están en el gate (hacen falta «cocktail menu», «Caterer's Permit»,
   «catering endorsement»), pero sí en `RX_REESCRIBIR` (clasificación) y en el brief.
5. **Notas de fórmula del motor común** `3-Year P&L!F13/F14` y `12-Month Cash Flow!O11` hablaban de «FOOD sales»,
   «beverages» y «Food and beverage purchases»: se sobrescriben en `datos_mbar.FORMULAS_EN` (bar packages / add-ons /
   mixers, garnishes, ice). No se toca código común.
6. **Cierre del docx** (`PRODUCTOS_CIERRE`): Bar Business Plan Kit · Catering Business Plan Kit · Restaurant Staff
   Scheduling Kit Pro · Gastro Pro Prompts eBook. Food Cost Kit Pro y HACCP Food Safety Kit Pro harían saltar el gate.
   Portada sin «dry hire»: su primera mención, con la glosa, la escribe el redactor en §1 [40].
7. **Medidas US (John, 13-oct)**: oz / fl oz, lb, quarts / gallons, °F, miles y sq ft como principales y la métrica entre
   paréntesis. Calculadora: specs en oz con «(ml)» y escalado en oz y en botellas de 750 ml («fifths») y de 1.75 L
   («handles»); hielo en lb con su fila en kg; lista de compra con handles; notas de 1.5 oz (44 ml) y 5 oz (148 ml).
   `datos_mbar`: rótulo «6 x 12 ft», `REGLA_UNIDADES` en las pistas del checklist, del docx y por texto (m², kg, km,
   litros, °C del ES), glosario y D19 con kg. Brief: sección 0 y nota del glosario.
8. **Calculadora** (D89): el «bar fee» es una tarifa fija que se COBRA por evento («a flat fee plus a price per guest»,
   §9 #12), no un coste; el «mínimo» es un importe mínimo de la barra (Kit estimate $400), no un mínimo de invitados; el
   precio usa `coste ÷ (1 − margen − comisión del marketplace)` para que el margen calculado nunca quede bajo el objetivo;
   los bitters van a la lista del anfitrión (llevan alcohol); las mezclas de copas por paquete, el reparto de destilados
   y los precios de envase son Kit estimate editables.
9. **Las pistas D18 no llegan al revisor de GRC-plan** (`preparar_tandas` solo le pasa id, es, en_actual y dónde): la
   regla D18 va en el brief, tanda (a).
10. **Fuera de mi alcance (paso 3/F3)**: `mobile-bar-business-plan` en `PRODUCTOS_LETTER` de `censo-entregables.py` y en
    `EXCLUIDOS` de `postprocess-transversal.py` (G9 de `gates_en`); hoy se pasa con `--letter --only`.

## 5. Calculadora D89-D90 (`calculadora_mbar.py` → `astro-site/public/dl/mobile-bar-business-plan/mobile-bar-pricing-calculator.xlsx`)

5 pestañas, 761 fórmulas: «Pricing Calculator» (28 entradas verdes con DV: lista de 3 paquetes leída de la tabla de
bartenders por paquete, Yes/No del sales tax, enteros, importes ≥ 0, porcentajes 0-1, comisión ≤ 30 %, margen ≤ 65 %;
salidas: copas, hielo en lb y kg, bartenders sugeridos, costes, precio por invitado y por hora de servicio, subtotal con
mínimo, service charge, impuesto, total, depósito del 30 %, saldo, comisión, margen calculado, hora extra) · «Drinks &
Shopping List» (mezcla por paquete, botellas de 750 ml y de 1.75 L por tipo de destilado, vino, cerveza, brindis; lo que
pone el bar: hielo en lb, kg y bolsas, vasos, servilletas, mixers; «Who buys it» = anfitrión en dry hire, tú con
licencia) · «Signature Cocktail Specs» (10 recetas de la carta ES, mocktail incluido, en oz con (ml); escalado a
50/100/200 por fórmula en oz, fifths y handles; coste por copa desde el precio del envase; alérgenos orgeat y coco) ·
«3 Example Quotes» · «Instructions» (dry hire y MO 24-01, Rev. Rul. 2012-18, sales tax de CA, nota UK, Kit estimates,
firma, versión y aviso). docProps D20, Letter + ajuste + pie, hojas protegidas sin contraseña.

| Ejemplo (Kit estimate, dry hire) | Inv. | Copas | Coste | Precio/inv. | Subtotal | /hora | Total | Margen |
|---|---|---|---|---|---|---|---|---|
| Wedding, 5 h, full bar (+ bar fee 250, service charge 15 %) | 120 | 720 | 1,137.20 | 19.00 | 2,530.00 | 506.00 | 3,142.26 | 55.1 % |
| Corporate holiday party, 4 h, full bar | 100 | 500 | 734.70 | 16.50 | 1,650.00 | 412.50 | 1,782.00 | 55.5 % |
| Private birthday, 4 h, limited bar (+ specialty 15 %, marketplace 5 %, estado sin tax en el servicio) | 60 | 300 | 326.50 | 16.00 | 960.00 | 240.00 | 1,036.80 | 61.0 % |
| Hoja principal por defecto (≈ el caso: 95 inv., 4 h) · con licencia | 95 | 475 | 604.38 · 2,029.38 | 14.50 · 47.50 | 1,377.50 · 4,512.50 | — | 1,487.70 · 4,873.50 | 56.1 % · 55.0 % |

**Autotest** (`bp5.py calculadora`): inject_cache 761 fórmulas, 0 fallos de pycel; **778 comprobaciones** pycel + caché =
Python en las 4 pestañas de cálculo (hoja principal, lista de compra, specs, 3 ejemplos) + el **paquete con licencia**
probado con `set_value` en la hoja principal (alcohol > 0, precio mayor, «Who buys it» = «You»); margen ≥ objetivo,
interruptor con efecto, glosa de dry hire presente, 0 cadenas vacías, 0 verdes bloqueadas, sin «€» ni símbolo en
formatos, 0 español / no latinos / cifras prohibidas / `RX_BAR_NO` / anclas → **VERDE**. `censo-entregables --fail
--letter --only mobile-bar-business-plan`: 0 defectos; `gate-no-latinos --only`: 0. sha256 (Mac = VPS)
`507aad22e606e92c…`.

## 6. Comandos para seguir

```bash
# PASO 2 — redactores Sonnet (Mac, máx. 2 a la vez, istats < 62 °C; BRIEF-TRADUCTORES.md, secciones 0 y 1 + la tanda)
#   tanda 1: (a) GMB-plan + revisión GRC-plan ‖ (b) GMB-check · tanda 2: (c) mbar_a ‖ (d) mbar_b
B=scripts/productos-digitales/business-plans-en-5
python3 $B/bp5.py check_textos --tanda GMB-plan     # | GMB-check | mbar_a | mbar_b
python3 $B/bp5.py preparar_tandas && python3 $B/bp5.py check_textos --tanda GRC-plan   # tras GRC-plan.revision.json
python3 $B/bp5.py check_textos --todas

# PASO 3 — VPS: aplicar (calibración ya fijada), ensamblar, gates
ssh vps
cd /root/wt-mbar && git pull --ff-only && cd scripts/productos-digitales/business-plans-en-5 && PY=/root/venv-guias/bin/python
$PY bp5.py aplicar_en --idempotencia --json /tmp/mbar-real.json   # 2 xlsx en dl/mobile-bar-business-plan/ + cifras_caso.json
$PY bp5.py ensamblar_docx --plan mbar                             # tras mbar_a + mbar_b
# G9: antes, mobile-bar-business-plan en PRODUCTOS_LETTER (censo-entregables) y EXCLUIDOS (postprocess-transversal)
$PY bp5.py gates_en && $PY bp5.py gates_en --autotest && $PY bp5.py ensamblar_docx --autotest --dir /tmp/mbar-docx-at
$PY bp5.py calculadora --autotest && $PY bp5.py barrido           # → entregables_mbar.json
# regresión §2; vuelta por scp (sha256 iguales); commit desde el Mac; VPS limpio
# si cambian FIJOS / POR_CELDA / zonas / grupos / pistas: $PY bp5.py extraer_textos > /tmp/mbar-ext.txt (VPS) y
#   preparar_tandas (Mac); si cambia el catering publicado, bp5.py verificar avisa (sha256) y hay que re-extraer
```

VPS: `/dev/null` es un fichero normal (redirigir a `/tmp/*.txt`); copiar del Mac con `COPYFILE_DISABLE=1 tar`; si
`git pull` choca con ficheros generados sin seguimiento, comprobar el sha256 y borrarlos antes.

## 7. Riesgos para los redactores (pasos 2-3)

1. **Redactar, no traducir**: el `es` es la ranura del FOOD TRUCK y la `propuesta_en`, el CATERING; **la pista manda**.
   En el checklist, solo las 44 filas «[sobrevive]» (con o sin ajuste) parten de la propuesta; las otras 24 son tareas nuevas. La revisión
   final debe leer el checklist entero (275 celdas) y la tabla D18 revisada.
2. **Primera mención de «dry hire» con su glosa** en cada entregable: `0. Assumptions!C5` (libro), P1 fila 14
   (checklist), §1 [40] (docx). La calculadora ya la lleva en `Pricing Calculator!A2`.
3. **Gate `RX_BAR_NO`**: trampas típicas de un bar móvil: «pickup truck» (→ «pickup» / «tow vehicle»), «serving
   window» (→ «bar top»), «servers», «food» (el garnish no es «food»; «food handler card» sí vale), «per day».
4. **Medidas US** con la métrica entre paréntesis (§4.7); el ES está en ml, kg, m² y litros.
5. **Realismo (D85)**: cuartil alto de Check Cherry ($1,330 frente a la mediana de $750), mediana del primer año 3
   eventos, operador a tiempo completo con 2 equipos; el pesimista agota la caja (−$2,664) y el docx lo dice.
6. Cifras de mercado solo de research «leída» (check_textos lo comprueba); D19: 2 de 14 filas son «Kit estimate» (ratio
   de bartenders y hielo / mixers por invitado).
7. Si se rehace la extracción, los ids de `textos_es.json` pueden moverse y las salidas de los redactores dejan de casar.
