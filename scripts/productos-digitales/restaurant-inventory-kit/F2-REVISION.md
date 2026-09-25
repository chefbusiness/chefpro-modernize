# Restaurant Inventory Kit Pro — F2 revisión adversarial (ronda única, SPEC §7 paso 5)

> Sesión Claude Code, 25-sep-2026. Alcance: `textos_en/*.json` (542 cadenas «traducir», cobertura 100% frente a
> `textos_es.json`) + los textos localizados/derivados de `mercado_en.json` (`localizar` 246, `textos_cifra_derivada`
> 13). No se ha tocado `textos_es.json`, `mapas.py`, `censo_es.json`, `SPEC.md` ni ningún `.xlsx` (F2 paso 4,
> `aplicar_en.py`, no se ha escrito todavía). Tope de rondas: esta es la única — no hay una segunda pasada.

## Método

1. Censo automático: 542/542 cadenas `tratamiento="traducir"` presentes en `textos_en/*.json`; las 425 restantes
   (`localizar`, `mapa-clave`, `mapa-hoja`, `regenerar`) viven en `mercado_en.json` (`localizar` + mapas de `mapas.py`),
   confirmado por grupo (`GL-mercado` 246, `GM-mapas` 179).
2. Barrido automático de restos: CJK/cirílico/hangul/árabe/hebreo/tailandés → 0; `€`/`EUR` → 0; palabras españolas
   sueltas (regex) → 0.
3. Barrido de `EU`/`Regulation (CE/EU)`/marcas o festivos españoles → 0 apariciones fuera de las ya decididas
   (`Tax ID (EIN / VAT no.)`, D16, correcto).
4. Cruce cruzado: las 13 celdas que D20 obliga a **reescribir con cifra EN recalculada** existen DOS veces — una vez
   como traducción literal en `textos_en/*.json` (grupo `traducir`) y otra vez, ya reescrita, en
   `mercado_en.json.textos_cifra_derivada` (mismo libro/hoja/celda). `aplicar_en.py` (paso 4, futuro) debe hacer que
   la segunda gane; mientras tanto, cualquier desajuste entre ambas es un riesgo real si el guion de aplicación no
   localiza la celda correctamente. Se compararon las 13 parejas cifra a cifra — ver hallazgos.
5. Lente manager US: nombres de pestaña citados en el texto (regex de comillas) verificados contra `mapas.HOJAS`
   (30 pestañas) — 0 discrepancias. Terminología (`vendor` nunca `supplier`, `walk-in cooler` consistente,
   `par level`/`par max`, `use-by`/`best-by`) revisada por muestreo amplio — natural, sin calcos.
6. °F/°C: todas las temperaturas citadas en texto llevan el par `°F (°C)` en el orden D12; conversiones verificadas
   a mano en los tres textos con cifra de temperatura (-20 °C→-4 °F ✓, -2 °C→28 °F ✓, -18 °C→0 °F ✓, 7 °C→45 °F ✓).

## Hallazgos corregidos (5)

| # | Fichero | id / celda | Antes → Después | Por qué |
|---|---|---|---|---|
| 1 | `textos_en/G01.json` | `c0022` (01, Instructions, A20) | `"...Kitchen up to row 44, Bar and Storeroom up to row 34."` → `"...\"Kitchen\" up to row 44, \"Bar\" and \"Storeroom\" up to row 34."` | D6 exige comillas rectas al citar pestañas/valores. La cadena hermana `c0025` (misma lista de zonas, mismo fichero) sí las lleva — inconsistencia dentro del mismo documento. |
| 2 | `textos_en/G04.json` | `c0877` (07, KPI Dashboard, A19) | `$10,400 in purchases, $34,000 in sales` → `$14,900 in purchases, $6,100 in beginning inventory, $5,900 in ending inventory, $48,700 in sales` (se mantiene 31.0% food cost, 1,450 covers) | **D20 lo marca como celda de cifra derivada** (misma celda que `mercado_en.json.textos_cifra_derivada[07/KPI Dashboard/A19]`), pero el traductor tradujo literal las cifras ES (10.400 €/34.000 €) limitándose a poner `$`. La versión de `mercado_en.json` recalcula con los datos reales (compras = `SUM(Spend by Category!B4:B13)` = 14.900; food cost = (6.100+14.900−5.900)/48.700 = 31,0 %, verificado a mano) y ya estaba correcta; se alineó `textos_en` a esa cifra para que no sobreviva una contradicción si `aplicar_en.py` no prioriza `mercado_en.json` para esta celda. |
| 3 | `textos_en/G05.json` | `c0917` (BONUS-09, Instructions, A19 — ejemplo de la leche) | `15-gallon max stock. The EOQ comes out to 72 gallons. ... finally brings it down to 15 gallons.` → `16-gallon max stock. The EOQ comes out to 64 gallons. ... finally brings it down to 16 gallons.` | Cifras contradecían los datos reales de `mercado_en.json` (`b09` fila 7, `whole_milk`: `eoq=64.0`, `par_max_01=16`) **y** la reescritura ya correcta que trae `mercado_en.json.textos_cifra_derivada[B09/A19]` (64 / 16). Se recalculó a mano: EOQ = √(2×2×365×3/(4,23×0,25)) = 64,35→64; tope vida útil = 12×0,7×2 = 16,8→17; sugerida = MIN(64, 17, 16) = 16. La `nota` del propio JSON asumía que "los valores reales de la hoja tienen precedencia", pero esta celda es texto narrativo, no una fórmula — si `aplicar_en.py` no la sobrescribe explícitamente, las cifras erróneas (15/72) habrían quedado publicadas. |
| 4 | `textos_en/G05.json` | `c0918` (BONUS-09, Instructions, A21 — parámetros) | `"a $3 order cost"` → `"an order cost of 3 (in your currency)"` | D13/D24 son explícitos: el parámetro de coste de pedido es neutro de moneda («in your currency»), el `$` solo vale en ejemplos de texto marcados como ilustración US (no es el caso: es un parámetro editable universal). La `pista` de `textos_es.json` para este id lo dice literalmente («sin símbolo de moneda»). `mercado_en.json` ya tenía la versión correcta con «(in your currency)»; se alineó `textos_en`. |
| 5 | `mercado_en.json` | `textos_cifra_derivada` — 04/Instructions/A7, 04/Instructions/A8, 04/Receiving Temps/G15 | `"Suggested group"` / `"Group"` / *"that group"* / *"its group's range"* / *"default group"* → `"Suggested Family"` / `"Family"` / *"that family"* / *"its family's range"* / *"default family"* (se dejó intacto el literal fijo `NO LIMIT FOR THIS GROUP`, que es el token de `mapas.LITERALES`, no un nombre de columna) | Las cabeceras reales de esas dos columnas son **`Suggested Family`** y **`Family`** (`textos_en/G02.json` ids `c0411`/`c0412`, ya traducidas y consistentes en las dos pestañas del libro 04). Las tres reescrituras D20 de `mercado_en.json` inventaban una columna «Group»/«Suggested group» que no existe en el libro — habría mandado al usuario a buscar una pestaña/columna inexistente. Se corrigió sin tocar el literal de estado `NO LIMIT FOR THIS GROUP`, que sí está bloqueado por `mapas.py` (D10, autotest) y es una inconsistencia ES→EN ya asumida y fuera de alcance de esta revisión (ver «Abierto»). |

## Comprobaciones sin hallazgo (para no repetir trabajo en la próxima sesión)

- Las otras 7 parejas «traducir vs. `textos_cifra_derivada`» del D20 (01/A20 filas 44-34, 03/A10, 04/A7 low-level
  wording aparte de lo de la tabla anterior, 05/A8, 05/A10, 05/Waste Dashboard/A13, BONUS-08/A14) no tienen
  contradicción numérica: son reformulaciones casi-duplicadas del mismo contenido, no errores. No se tocaron para
  no generar «style churn» sin defecto real.
- Proveedores de ejemplo (D15): los 6 cumplen `555-01xx`, dominio `.example`, `Tax ID 00-000000n`, direcciones
  «Anytown» y condiciones Net 30/15/COD — sin hallazgos.
- 51 productos de `mercado_en.json` (D14): unidades US, formato de compra realista, fuente citada o `[estimado]`
  — muestreo de 6 sin hallazgos (no se auditaron los 51 uno a uno por presupuesto S).
- Terminología: 0 apariciones de `supplier` (D7 dice que es solo nota UK, nunca cuerpo EN); 0 `kg`/`litre`/`€`/`EUR`;
  fechas citadas en texto sin formato `dd/mm`.

## Abierto (no se pudo/debió arreglar en este paso)

1. **`mapas.py` tiene un desajuste interno decidido y bloqueado por su propio autotest**: la cabecera de columna es
   `Family`/`Suggested Family` pero el literal de estado fijo (D10, `mapas.LITERALES`) es
   `⚠ NO LIMIT FOR THIS GROUP` (no `...FAMILY`). Es decir, el propio kit dirá «revisa la columna **Family**» y al
   mismo tiempo mostrará el aviso «NO LIMIT FOR THIS **GROUP**» en esa columna. Esto viene de la tabla de literales
   de `mapas.py` (fuera del alcance de esta revisión, que es solo `textos_en/*.json` + `mercado_en.json`) y está
   fuera del tope de una ronda: **hay que decidir en la siguiente sesión** si se renombra el literal a
   `NO LIMIT FOR THIS FAMILY` en `mapas.py` (reabre el autotest de D10) o se acepta la inconsistencia terminológica
   como coste menor. Ya la tuvo que sortear puntualmente esta revisión (hallazgo 5) dejando el literal intacto.
2. No se auditó 1:1 el resto de `mercado_en.json.productos` (51) ni `productos_extra_historial` (7) más allá del
   muestreo — presupuesto de la ronda (`F2 ≤ 1,2 M`) y alcance declarado en la tarea (solo textos localizados/
   derivados, no el catálogo de precios en sí).
