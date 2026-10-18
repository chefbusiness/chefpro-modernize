# Burger Joint Checklists Kit Pro — F2: construcción real (18-oct-2026 · sesión Claude Code)

Todo el python en el VPS (`/root/wt-burger`, rama en `ac37ad56` + los cambios de abajo, venv `/root/venv-guias`).
Textos: `textos_en/heredado.json` (275: 192 del base, 52 de la pizzería, 28 de la cafetería, 3 del bar) +
`textos_en/G1.json` (316, traductor sonnet en `ac37ad56` + los ajustes de abajo) = las 591 cadenas a traducir; GM 278
por `mapas_burger.py` (212 `POR_CELDA`, 28 `VALORES_EN`). Decisiones del traductor aprobadas: «jalapeno» sin ñ,
«Swiss» por emmental, «2 weeks out».

## Cambios de esta pasada

- **Merge de la ronda 1 de la pizzería** (`1a00e5c7`, pizza en `855b5c3f`): `heredar.py` sobre la rama cambia 2 EN
  heredados de la pizzería (c0113 date marking «TCS kept over 24 h», c0403 «To-go bags (paper / plastic)») y saca 2
  cadenas a pendientes: c0357 (la pizzería reescribió su B8 con horno y tiro) → traducida aquí para la hamburguesería
  (técnico = termostato de la plancha y motor de la campana) y c0827 (graduaciones) → resuelta por `POR_CELDA`.
- **Lecciones de esa ronda aplicadas a las mismas celdas** (`mapas_burger.py`, `G1.json`):
  - B02 cronológico: Cuaresma `February–April` antes que el 17 de marzo (filas 9↔10) y el mes de la hamburguesa
    (mayo) antes que «May–June» (12↔13); su C por `_CAL_C` con el EN ya traducido (c0818, c0821, c0830 salen del G1).
  - B02 C18 sin el calco «Holiday service»; C19 sin «back-to-routine crowd» (jueves, domingo, lunes y sábado
    universitario); C20 sin «(no drink specials)»; C26 + «free drinks only where your state allows them».
  - 01 D10 control de salud → Shift manager (PIC); 08 E20-E21 → 11:00 AM (plancha y freidoras con la campana del 01);
    07 «By Area» A19 + C20:C24 y BONUS-01 B6 / B26: la «barra» es el mostrador (counter / bar).
  - TPHC con procedimiento escrito (c0296, `REGLAS_US['tphc']`); lavavajillas sin «softener salt» mensual (c0263,
    c0462); campana: se desmontan y desengrasan los FILTROS, no la campana (c0411), y filtros dañados se cambian (c0463).
- **Celdas cortadas**: el traductor avisó de 87 cadenas por encima del 115 % del ES. Con `AJUSTE_MAQUETA_ES` la EN
  activa el ajuste: G3 117 ajustes · 103 altos, 0 desbordes. Comprobación sin mirar el ES (`ancho_texto` / `n_lineas`
  de `aplicar_en` sobre las 2.439 celdas de texto): **1 cortada de verdad**, el título 05 «Instructions» B2, que ya va
  cortado en el ES (2 líneas en 26 pt: «maqueta heredada») → gancho nuevo `mapas.ALTOS_FILA` en `aplicar_en.capa_ajuste`
  (solo la hamburguesería; sin la constante no hace nada: los hermanos salen idénticos) → 50.5 pt, como los demás
  títulos de dos líneas. Quedan 4, las mismas de los hermanos: «Verified by:» del 07 (×3, columna estrecha, igual que
  el ES y la pizzería) y «Denomination» del 09 (maqueta del base). Ninguna cadena se recortó.
- `censo-entregables.py` (`PRODUCTOS_LETTER`) y `postprocess-transversal.py` (`EXCLUIDOS`): + el slug (F1).

## Ronda 1 de la revisión (`revision/REVISION-F2.md`: 0 bloqueantes · 2 MAYORES · 12 menores)

Aplicadas las 14 con la corrección EN del informe, más la duda D2 (aprobada); el resto de dudas, no (foie gras «where
legal»; lo que pide filas nuevas, a la v2.1). Tabla «aplicado / no aplicado» al final del informe.
- `G1.json`: 19 cadenas (M1 boil-out ×2, M2 queso americano ×2, m2 freidora ×6, m3 ×2, m4, m5 ×2, m6, m7 c0355, m10 ×2).
- `POR_CELDA` (+7): 06 E13 «2 weeks out», 04 Grill Cook E9 11:15 AM, 05 E8 «Semiannual», B02 B8 (nota UK con el
  National Burger Day; sale de `_HEREDA_ADAPTAR` y de la memoria: heredadas 274), C26:C28 «pt»; reescritas 05 B8, B13 y
  B14 (supresión delante, aceite usado por volumen, trampa de grasa).
- `REGLAS_US`: + `utensilios_4h` (§4-602.11(C)); `aceite` + boil-out; `dias_fuertes` + UK; `inventario` + redondeo.
- `VALORES_EN` (D2): bacon 5 lb, blue cheese y jalapeños 12 oz, patatas 20 lb, aros 5 lb, BBQ / mostaza / mayonesa 1 pt;
  números, el semáforo sigue; criterio en `SPEC.md` (D-BUR Inventario). Errata ES del aceite mensual en `SPEC.md` §5.
- ADAPTAR a juego (`_ACEITE`, `_CARNE_GUARDAR`, make line, 05 B6 y B20) para el próximo traductor.
- Landing (`astro-site/src/data/productos-en/tareas/burger-joint-checklist-templates.ts`): 4 frases a juego (picada
  sobre el pollo, aceite cada noche + TPM + boil-out, plancha sin «taken apart», «a fryer boil-out»).
- Resultado: VERDE 8/0, autotest 18/18, censo 0, no-latinos 0, idempotencia 0, 0 desbordes, las mismas 4 «cortadas» de
  maqueta que los hermanos; 5 hermanos con 0 diferencias, gates VERDE y autotest 16 / 16 / 18 / 20 / 18; xlsx copiados
  al Mac con sha256 11/11 iguales; `revision/dump_en.txt` regenerado (3.512 líneas). Sin código compartido nuevo.

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 extraer_textos.py --kit burger && python3 burger/mapas_burger.py && python3 heredar.py --kit burger
    python3 aplicar_en.py --kit burger --idempotencia --mes October     # → astro-site/public/dl/burger-joint-checklist-templates/
    python3 gates_en.py --kit burger --mes October [--autotest]
    python3 ../censo-entregables.py --only burger-joint-checklist-templates --fail
    python3 ../gate-no-latinos.py --only burger-joint-checklist-templates
    python3 volcar_xlsx.py --kit burger <dl/burger-joint-checklist-templates> burger/revision/dump_en.txt --orden en
    python3 volcar_xlsx.py --kit burger <dl/kit-tareas-hamburgueseria> burger/revision/dump_es.txt --orden es

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (nombres de `SPEC.md` §2), idempotencia 0 diferencias, `inject_cache` sin fallos, 0 desbordes |
| Gates | **VERDE 8/0**: G1 46 hojas · 181 fórmulas (15 por celda) · 32 DV · 33 CF · 285 merges · 34 protegidas · 4.468 desbloqueadas; G2 sin español, €, no latinos ni términos prohibidos (2.765 piezas); G3 Letter, pie, marca (45) y versión, 117 ajustes · 103 altos; G4 1.106 glosario · 270 regenerar · 834 traducir · 33 citas de fichero · 14 de pestaña · 169 horas · 28 valores fijados; G5 caja 204.91 / 4,200 / 0; G6 153 con valor + 28 vacías como el ES; G7 55 °F y 48 citas, todas en `REGLAS_US`, 4 `CELSIUS_SIN_F` |
| Autotest | **18/18 CAZADOS** (los 16 del base + término prohibido + valor fijado; la cita, `CITA_AUTOTEST` = 3-501.18) |
| censo-entregables · no-latinos | 0 defectos (`--fail`) · 11 ficheros, 0 con no latinos |
| Hermanos | dry-run con el código final = lo publicado (pizza = `855b5c3f`): 0 diferencias en los volcados (base 4.227 · bar 3.352 · cafe 4.515 · catering 2.695 · pizza 3.666 líneas), gates VERDE 8/0 y autotest 16 / 16 / 18 / 20 / 18 OK (`ALTOS_FILA` no existe en ellos); el diff de la pizzería (xlsx y `pizza/`) de `855b5c3f` a HEAD, vacío |
| Copia al Mac | `scp` de los 11 xlsx a `astro-site/public/dl/burger-joint-checklist-templates/`: sha256 11/11 iguales |
| Volcados | `revision/dump_en.txt` y `dump_es.txt`, 3.512 líneas cada uno |

Siguiente: ronda 2 solo si la pide el orquestador (máximo 2) y cierre.
