# Fusión de ids en `guias-v2-research-sector.json` — Manual del Chef Ejecutivo (2026-09-06)

Decisión D24 de `manual-chef-ejecutivo-SPEC.md` §1. Scripts: `manual-chef-ejecutivo-json-merge.py`
(fusión), `manual-chef-ejecutivo-json-patch-urls.py` (segunda pasada tras el gate) y
`manual-chef-ejecutivo-json-gate.py` (verificación). Los tres quedan en este directorio, son
idempotentes (el merge aborta si los ids ya existen, salvo `--force`) y sirven de precedente para el
próximo research que necesite fusionarse.

## Qué se hizo

1. **CE-01..CE-40** — normativa de cocina, numeración original de
   `manual-chef-ejecutivo-research-L3-normativa.md`.
2. **CS-01..CS-23** — datos del sector de `manual-chef-ejecutivo-research-L4-laboral-datos.md`,
   renumerados desde el `CE-01..CE-23` local de ese documento (su `CE-01` pasa a `CS-01`, y así
   sucesivamente) para no colisionar con los `CE-*` de L3, que usan el mismo prefijo para otra cosa.
3. Aplicadas las tres correcciones de la SPEC que tocan datos concretos de estos dos research:
   - **D15a → CE-10**: se amplía con el art. 30.2 (mantenimiento en caliente ≥63 °C), el 30.5
     (temperaturas distintas con evidencia ante la autoridad) y el 30.7 (recalentamiento equivalente
     documentado); la primera versión del research solo citaba el rango 30.1-30.7 de forma genérica.
   - **D15b → CE-21**: corregido a «17-27 °C sedentario, 14-25 °C ligero, sin rango para trabajo
     pesado; la categoría la fija la evaluación de riesgos y el Anexo III admite condicionantes del
     local» — nunca «la temperatura legal de la cocina es 14-25 °C» (frase que queda en la lista negra
     de la SPEC, §8).
   - **D15c → CE-33**: reescrito para que quede explícito que las microempresas quedan excluidas de
     las obligaciones del **art. 6** (plan de prevención), pero el doggy bag del **art. 8** les sigue
     obligando — nunca «las microempresas quedan excluidas por completo de la Ley 1/2025» (también en
     la lista negra).
4. **D16 y D17 de la SPEC no generan entradas nuevas en este JSON.** D16 (salarios en bruto anual,
   +35,5 % jefe/a de cocina) es una cifra que sale de la tabla del §7.3 de L4, fuera del bloque «Datos
   del sector con fuente» (§10) que Task A fusiona, y que ya se apoya en `MM-14`/`MM-15` (ya presentes
   en el JSON, sin tocar); D17 (recuentos «25 fuentes censadas, 23 legibles», «10 ficheros con 11
   menciones») es un recuento del proceso de research completo (L1-L6), no un dato de L3 o L4. Las dos
   son correcciones de **copy del guion**, no de esta base de datos — quedan anotadas como pendiente
   para quien escriba el guion (ver «Pendientes» del informe final).

## Tratamiento de lo que no tiene fuente citable

El encargo pedía tratamiento de lista negra explícito (fiabilidad `baja`, cifra vacía, nota
`«LISTA NEGRA: no se cita; el lector lo mide con su herramienta»`) para **CS-14..CS-18 y
CS-21..CS-23**. Al aplicar el GATE (`todas con url o con la nota de lista negra`) aparecieron otras
**12 entradas** sin url verificable que no estaban en esa lista explícita:

- **2 reutilizan una url YA VERIFICADA** de otra fila del mismo documento/misma norma (no se inventa
  ningún enlace): `CS-05` (mismo informe INSST que `CS-01`/`CS-02`) y `CE-37` (misma norma —Reglamento
  2073/2005— ya citada en `CE-08`, de la que `CE-37` es una síntesis).
- **10 pasan al mismo tratamiento de lista negra** (extensión de «y similares» del encargo), porque
  ninguna de las dos fuentes L3/L4 da un enlace verificable para esa fila y no se ha construido ninguna
  URL no confirmada: `CE-36`, `CS-03`, `CS-06`, `CS-08`, `CS-09`, `CS-10`, `CS-11`, `CS-12`, `CS-19`,
  `CS-20`. En los dos últimos casos (`CS-19` coste de personal 30-35 %, `CS-20` sanciones) la cifra
  fiable ya está disponible sin blacklear vía `MM-41` y `MM-35`, que se citan en la propia nota.

## GATE (verde)

```
=== GATE manual-chef-ejecutivo-json-fusion-2026-09-06 ===
Total entradas en el JSON: 225
CE-*: alta=31 media=8 baja=1 total=40
CS-*: alta=4 media=1 baja=18 total=23
Sin colisión de id en el fichero completo: OK
Todas con url o nota de lista negra: OK

GATE VERDE: 225 entradas, 40 CE-*, 23 CS-*, sin colisiones, todas con url o lista negra.
```

`_meta.totales` del JSON tras la fusión: `{"datos": 225, "alta": 144, "media": 65, "baja": 16,
"sin_url": 29}` (el campo `sin_url` viejo, heredado de una fusión anterior, no se había recalculado;
se corrigió a la cifra real del fichero completo).

## Tabla de lo añadido

### CE-01..CE-40

| id | tema | cifra | fiabilidad |
|---|---|---|---|
| CE-01 | Alérgenos (contaminación cruzada) | — | alta |
| CE-02 | Cultura de seguridad alimentaria | — | alta |
| CE-03 | Donación de alimentos | — | alta |
| CE-04 | Formación de manipuladores | — | alta |
| CE-05 | Uniformidad | — | alta |
| CE-06 | Alérgenos (declaración obligatoria) | 14 alérgenos | alta |
| CE-07 | Sin gluten | 20 mg/kg / 100 mg/kg | media |
| CE-08 | Vida útil y Listeria monocytogenes | — | media |
| CE-09 | Trazabilidad | — | alta |
| CE-10 | Temperaturas (D15a) | 63/4/8/-18/74 °C | alta |
| CE-11 | Comidas testigo | 100 g / 7 días / 40 personas | alta |
| CE-12 | Etiquetado «elaboración propia» | — | alta |
| CE-13 | Congelación y etiquetado | 3 fechas | alta |
| CE-14 | Anisakis | -20°C/24h · -35°C/15h · 60°C/1min | alta |
| CE-15 | Doggy bag / desperdicio | — | alta |
| CE-16 | Trazabilidad práctica en cocina | — | alta |
| CE-17 | Aceites de fritura | <25 % | alta |
| CE-18 | Contaminantes en materia prima | — | media |
| CE-19 | Acrilamida — ámbito | — | alta |
| CE-20 | Acrilamida — niveles | 175°C / 400 / 850 μg/kg | media |
| CE-21 | PRL — temperatura del local (D15b) | 17-27 °C sedentario / 14-25 °C ligero | alta |
| CE-22 | PRL — suelos | — | alta |
| CE-23 | PRL — EPI de cocina | — | alta |
| CE-24 | PRL — manipulación de cargas | sin cifra en la norma | alta |
| CE-25 | PRL — máquinas de cocina | — | alta |
| CE-26 | PRL — revisión de equipos | — | alta |
| CE-27 | PRL — formación e información | — | alta |
| CE-28 | PRL — EPI, obligación general | — | alta |
| CE-29 | Guía oficial de riesgos en cocina | — | media |
| CE-30 | Siniestralidad de hostelería | 50.837 / 19 / 2.731,1 por 100.000 | alta |
| CE-31 | Desperdicio — jerarquía de prioridades | 6 niveles | alta |
| CE-32 | Desperdicio — obligación de hostelería | — | alta |
| CE-33 | Desperdicio — exención del plan de prevención (D15c) | 1.300 m² | alta |
| CE-34 | Desperdicio — convenios de donación | — | alta |
| CE-35 | Botulismo en envasado al vacío | <4°C / <3,3°C | media |
| CE-36 | Guía de cocina al vacío | — | baja |
| CE-37 | No existe cifra legal de días de vida útil | — | alta |
| CE-38 | Inspección — Madrid | 53 páginas | alta |
| CE-39 | Inspección — Cataluña | — | media |
| CE-40 | Inspección — Andalucía | — | media |

### CS-01..CS-23 (renumerados desde el CE-01..CE-23 local de L4)

| id | tema | cifra | fiabilidad |
|---|---|---|---|
| CS-01 | Índice de incidencia ATJT, CNAE 56, 2024 | 2.646,5 por 100.000 | alta |
| CS-02 | Accidentes de trabajo totales, España 2024 | 647.200 | alta |
| CS-03 | Accidentes anuales del conjunto de hostelería | — | baja |
| CS-04 | Accidentes en cocineros y ayudantes de cocina, por tipo | — | baja |
| CS-05 | Tipos de accidente más frecuentes, España 2024 | 31% / 26% / 18% | media |
| CS-06 | Tasa de rotación laboral en hostelería | — | baja |
| CS-07 | Absentismo en hostelería | 5,9 % | alta |
| CS-08 | Abandono de la hostelería por jóvenes (UE) | — | baja |
| CS-09 | Consumo energético de la cocina sobre el total | — | baja |
| CS-10 | Consumo energético anual medio de un restaurante | — | baja |
| CS-11 | Consumo energético de una freidora profesional | — | baja |
| CS-12 | Peso energético del sector hostelero en España | — | baja |
| CS-13 | Manual de eficiencia energética MITECO/GNF | — | alta |
| CS-14 | Comida cocinada que acaba en la basura | — | baja |
| CS-15 | Pérdida económica anual por desperdicio/mermas | — | baja |
| CS-16 | Rango de merma «sano» en cocina profesional | — | baja |
| CS-17 | Pérdida mensual media por mermas | — | baja |
| CS-18 | Ratio de cocineros por comensal/plaza | — | baja |
| CS-19 | Coste de personal sobre ventas netas | — | baja |
| CS-20 | Sanciones por brote de toxiinfección alimentaria | — | baja |
| CS-21 | Coste directo de un brote alimentario | — | baja |
| CS-22 | Tiempo medio de pase | — | baja |
| CS-23 | Horas de formación por trabajador de cocina/año | — | baja |

Via: Claude Code
