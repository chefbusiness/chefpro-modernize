# Handoff 30-oct-2026 · sesión Claude Code (Mac + VPS) — tanda de arreglos sin correo

Rama `fix/tanda-arreglos-30oct` → PR (ver §2). Sin correo: son arreglos (política del 25-oct).

## 1. Qué se arregló en los ficheros LIVE (41 xlsx por parche XML + 3 documentos de guía regenerados)

`scripts/productos-digitales/parche_xml_xlsx.py --apply` toca solo el contenido de las celdas o DV que cambian; el resto
del zip viaja byte a byte y las cachés `<v>` no se mueven. Respaldo previo en el VPS: `/root/dl-backup-30oct`.

| Arreglo | Alcance | Por qué |
|---|---|---|
| **Literales > 255 caracteres en fórmulas** troceados en `"…"&"…"` | 76 celdas en 25 planes financieros ES/EN + guía chocolatería (checklist legal) | Excel limita a 255 cada literal de fórmula. **Prueba A/B en el Excel del Mac**: el original de la Taquería se abría «reparado» y `Inversión Inicial!D27` perdía la fórmula (quedaba texto fijo); el parcheado abre sin reparar y con la fórmula viva. Era la deuda «fórmulas > 255» del 28-oct, y afectaba a la familia entera, no solo a D28/D33. |
| Desplegable de los checklists ES 2.2 `✓,—,N/A` → `✓,☐,N/A` (+ mensaje) | 8 checklists: catering temático, finca, heladería, paellero, parrillero, pizzería, pollería, taquería | Las casillas traen «☐» y la leyenda dice «☐ (pendiente)», pero el desplegable no lo ofrecía (no se podía volver a pendiente). |
| Pizza Shop EN: mensaje del desplegable «— = pending» → «☐ = pending» | 6 hojas | Mismo defecto en el texto de ayuda. |
| Nota de la **holgura** sobre el equilibrio | 14 planes ES (2 notas cada uno) + planes de las guías pastelería y chocolatería | La cifra es previsto/equilibrio − 1 (cuánto estás POR ENCIMA); la nota decía «cuánto puedes caer». La caída que aguantas es h/(1+h): 15 % → 13 %, 25 % → 20 %. |
| Taquería, checklist F6: «ITC-ICG 08» → «ITC-ICG 07 e ITC-ICG 08» | 1 celda | Arreglo anotado el 29-oct. Paellero y Parrillero citan «ITC-ICG 08 §5.2» a propósito (botella < 15 kg): no se tocan. |
| Nota trimestral EN (`12-Month Cash Flow!O20`) | 9 planes EN anteriores al Ice Cream | Decía «(April, July, October, January)», exacto solo con el Mes 1 en enero; ahora «Months 4, 7, 10 and 13 … when Month 1 is January». |

| **Ronda 2** (revisión adversarial opus): la misma holgura en los planes EN («How far you can fall…», 10 + 10) y la nota de B67 en ES, ahora referida a la holgura de CAJA con la que la compara el semáforo (16) | 14 planes ES + 2 guías + 10 planes EN | |
| «Fourth-quarter sales tax is settled in January…» → «in Month 13 (January … when Month 1 is January)» | 11 planes EN | Falso en Pizza (Mes 1 = septiembre), Ice Cream y Wedding (marzo). |
| Guía de Pastelería (docx + PDF) y planes modelo de pastelería y chocolatería (docx) | 3 documentos, regenerados con `documentos.py` desde los `txt/` corregidos | «si la caída se acerca a ese 22,9 %» → 18,6 % (22,9/122,9); ya estaba en `guia-pasteleria-en/ERRATAS-ES.md`. Diff de texto: solo la frase. El PDF sigue en 103 págs. con un reflujo en las pp. 15-18 (ReportLab nuevo; mismo texto) y el pie sigue diciendo «septiembre de 2026». |

Verificación: celda a celda contra el respaldo (acumulado: 41 ficheros, 76 troceadas, 73 con texto nuevo, 0 cambios
fuera de regla; fuera de celdas solo cambian las DV), `openpyxl` abre todos, censo de deuda repetido en limpio, **gate
LIT255 verde en los 753 xlsx de `dl/`** y `business-plans-en/gates_en.py --solo G1` verde con los ES troceados.

## 2. Qué se arregló en la fuente (para que no vuelva)

- `inject_cache.py` trocea los literales > 255 al final de cada pasada (lo usan el motor de planes, las guías, los kits y
  las calculadoras EN). Probado en el VPS: 0 celdas con valor distinto y gate verde.
- **Gate nuevo**: `python3 scripts/productos-digitales/parche_xml_xlsx.py --check astro-site/public/dl/<slug>/*.xlsx`
  (exit 1 si queda algún literal > 255) → para los flujos que no pasan por `inject_cache` (traducciones EN por XML).
- Motor de planes: `MARCA_NO = '☐'` (el desplegable nace `✓,☐,N/A`); holgura reescrita en `grupo_a.py`, en los
  `gen_plan-financiero-3-anos-*` de pastelería y chocolatería y en el guion de la guía de pastelería; ITC en
  `plan-taqueria/datos_checklist.py`.
- `nombre-gate.py` mira también las fichas EN (`productos-en/`). Hoy: **EN 1 fallo** (`ai-prompts-for-restaurants`:
  catálogo «Gastro Pro Prompts eBook» vs `<title>` del dashboard «Pro Prompts Library»). La parte ES ya salía en rojo
  ANTES de esta sesión (46 de 55: el H1 «Cómo Montar…» no es el nombre del catálogo): la regla ES está desfasada.
- `business-plans-en/extraer_docx.py` acepta el Word ES en A4 (falso rojo del 25-oct).
- Circuito de planes EN: `aplicar_en`, `gates_en` y `extraer_textos` funden «"…"&"…"» (`parche_xml_xlsx.fundir_literales`)
  antes de buscar claves y comparar; sin esto el siguiente plan EN abortaba con «literal sin clave EN» (lo cazó la revisión).
- Fuentes EN al día (`business-plans-en*/textos_en/*.json`): una regeneración ya no devuelve los textos viejos. El Restaurant
  EN conserva su «— = pending» (su desplegable es «✓,—,N/A» y sus casillas lo usan: coherente).
- ⚠️ Para el siguiente EN que copie los `mapas_*` de su hermano: el checklist ES ya sale con `✓,☐,N/A`; la sustitución
  `✓,—,N/A → ✓,☐,N/A` de los mapas pasa a no encontrar nada (si algún mapa lo exige, quitar esa regla).

## 3. Deuda que queda (decidido no tocarla hoy)

- **Motor de planes, cambian cifras** (no son retoques: mejor en el motor cuando se construya el siguiente plan):
  `PyG!G14` (10 % fijo), `Personal!C11` (suma sin ponderar), IVA en la fila de tasas (~63 €/año), `Inversión!D37` sin
  separador de miles.
- Guía de equivalencias en Letter en los productos ES (regenerar 53 PDF: no compensa).
- `m16 inject_cache EN`, umbrales de sitemap/hreflang de `fase6-gate`.
- `parche_xml_xlsx.py`, límites conocidos (nada los toca hoy): una `'` fuera de un nombre de hoja (referencias
  estructuradas) esconde los literales que vienen detrás; no hay guarda si un literal largo es operando de `+ - * /`.
- Nota EN «The model pays year-1 income tax in July of year 2»: no se ha comprobado si es mes del plan o de calendario.
- `guia-pasteleria/build/docs/*.docx|pdf` y los `.md` espejo de `guia-chocolateria/build/` siguen con el texto viejo (no se publican).

## 4. Pendientes de John

- **Purgar los pedidos cripto QA sin pagar** (la CLI devuelve 401 con la contraseña que resuelve el Mac):
  `qa-heladeria`, `qa-finca`, `qa-pizzeria`, `qa-pizzashop`, `qa-taqueria`, `qa-tacoshop`, `qa-polleria`, `qa-rotisserie`.
  Primero mirar: `python3 scripts/productos-digitales/crypto-report.py --days 30`; después
  `--purge-unpaid-before 2026-10-30` (borra TODO lo no pagado anterior a esa fecha: comprobar que no hay un pedido real
  a medias).
- `CUTOVER_ENBLOG_PENDIENTE.md` (cutover de `enblog.aichef.pro`).
- Térmica: el 30-oct el pico (62 °C) fue `knowledgeconstructiond` (Apple Intelligence) 43 % + `contactsd` 35 %: se congeló el primero (`pkill -CONT knowledgeconstructiond` para reanudarlo).

## 5. Siguiente

Decidir con John: producto nuevo (Taco Shop Checklist Templates EN $19, ya en cola; Sushi Bar; Smash) o traducciones.
23 productos ES sin gemelo EN (catálogo, 30-oct): 9 kits de tareas (12-18 €), mega-pack de tareas (89 €), 10 guías
(24-85 €), 2 manuales (55-65 €), plan chef privado (45 €).

## 6. Secuela (31-oct, sesión Claude Code): los 13 conjuntos EN de planes, regenerables otra vez

La deuda que cazó el lead del Sushi EN (`business-plans-en-14/F2-NOTAS.md` §6 de su rama): este PR parcheó los ES LIVE sin
re-extraer el `textos_es.json` / `censo_es.json` de cada conjunto EN, y todos los `aplicar_en --dry-run` abortaban
(«textos_es.json dice 'Cuánto puedes caer…' y el ES trae 'Cuánto deben superar…'»). Arreglado en la rama
`fix/en-sets-resync-tras-186` con `business-plans-en/resync_es.py` (VPS): re-extrae los 13 en orden de cadena con
`extraer_textos --fijar-clasificacion` (mismos ids y el grupo/tratamiento publicados: las reglas de `grupo_de` miran el
texto y, con «☐» en vez de «—», 5 cadenas cambiaban de grupo → aplicar_en abortaba) y re-mide los sha fijados de los
diccionarios hermanos y de la fuente ES. Prueba: los 30 xlsx regenerados = LIVE por contenido (`comparar_sem.py`) y
22/22 docx y calculadoras = LIVE por bytes. **Regla para el siguiente parche de un ES LIVE con gemelo EN: correr
`resync_es.py` + la regresión en el mismo PR.** El canon de bytes de los planes ya no sale IGUAL (12 de 15): alto de la
fila 34 de la tesorería (134.75 en LIVE, 149.5 al regenerar) y el punto de troceo de 3 literales; ver el PR.
