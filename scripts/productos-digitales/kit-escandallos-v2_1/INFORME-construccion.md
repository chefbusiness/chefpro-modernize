# Kit de Escandallos Pro v2.1: informe de construcción (F2-ES, dry-run)

Sesión Claude Code, 24-sep-2026. SPEC: `scripts/productos-digitales/recipe-costing-kit/SPEC.md` §2.0.
**Todo en dry-run**: `astro-site/public/dl/` no se ha tocado. Resultado en
`<scratchpad>/v2_1-dryrun/` (14 xlsx). Informes JSON: `v2_1-informe-main.json` y `v2_1-verificacion.json`,
en el mismo scratchpad.

> **Estado: tras la revisión R1** (§7). Las cifras de §2-§5 son ya las vigentes después de R1. La construcción
> inicial usaba un despiece estadounidense (merma del solomillo 36 %); R1 lo sustituyó (CH-01).
>
> **Publicación (24-sep, §8):** `--real` ejecutado en la rama `feat/kit-escandallos-v2-1` (worktree), con la fila
> «Raciones por pieza» (CH-12) añadida antes; capa web ES y gates estáticos en §8. Merge y gates LIVE: orquestador.

## 1. Qué se ha hecho

| Fichero | Qué hace |
|---|---|
| `datos_ejemplos.json` | Todas las cifras de los ejemplos, cada una con su fuente o `[estimado]`/`[derivado]` y el razonamiento. Desde R1 también `correcciones_fichas` (texto de 01-08), `lista_precios.excluir` y `despiece.reservado_en` (el test de EE. UU., para el EN) |
| `nuevas.py` | Genera `12-test-de-rendimiento.xlsx` y `13-lista-precios-ingredientes.xlsx`. Importa de `kit-escandallos-v2_0/motor.py` la paleta, los formatos, `_cabecera`, `_dv_lista`, `print_setup`, `proteger`, `cerrar`, `PIE`, `COPY`, `MERMAS`, `CATEGORIAS`, `UNIDADES`, `FICHEROS` y `hojas_escandallo` |
| `parche_v2_1.py` | Parche idempotente sobre los 12 publicados: (a) rango de `Conversiones`, (b) versión y subject, (c) 01!H5, (c2) 08!H5, (c3) correcciones de texto, (c4) umbral de 03!Rotación Semanal, (d) líneas de texto |
| `main.py` | Copia de los 12 → nuevas → pycel calcula la merma del 12 → parche → idempotencia (2.ª pasada) → `inject_cache.py` **al final** sobre los 14. `--real` exige además `KIT_ESCANDALLOS_APPLY=1` y una carpeta de trabajo (`--scratch` o `CLAUDE_SCRATCHPAD`) donde deja el respaldo de `dl/`; sin ella aborta. En dry-run, sin carpeta, trabaja en `.work/kit-escandallos-v2_1/` (en `.gitignore`) |
| `verificar.py` | Las 7 verificaciones de §5, en serie (`--carpeta`, `--publicados`) |

Dos detalles de implementación:

- **09, 10, 11 y BONUS se parchean a nivel de ZIP** (subject en `core.xml` y la celda `inlineStr` de la versión), sin
  pasar por openpyxl. 09 y 11 llevan un gráfico que openpyxl **borra** al cargar y guardar. Comprobado que
  siguen con `xl/charts/chart1.xml`.
- **Bug encontrado antes de publicar:** en `--real`, la 2.ª pasada leía los precios de las fichas ya guardadas por
  openpyxl, que no tienen caché, y los precios enlazados del 04 salían vacíos. Ahora el 13 lee siempre de una copia
  con caché: `ORIGEN` en dry-run y el respaldo en `--real`. `--real` se ha **simulado** sobre una copia de
  `dl/kit-escandallos` en el scratchpad, con `ORIGEN` redirigido y dos pasadas (repetido tras R1:
  `<scratchpad>/sim_real.py`). Resultado: 0 diferencias entre pasadas, 0 con el dry-run, y el PDF del bono intacto.
  `--real` contra `dl/` **no se ha ejecutado**.

## 2. Libro 12: Test de Rendimiento

Pestañas: `Instrucciones`, `Test de despiece`, `Test de cocción`. Las dos de test se imprimen en **vertical** (R1 CH-07).

### Test de despiece

La pieza es la misma que compra la 01: solomillo de ternera entero, con cordón, a 28,50 €/kg (01!D5).
**Es un ejemplo orientativo, no un test pesado**, y la hoja lo dice (nota de la fila 39 e Instrucciones).

| Componente | Tipo | Peso | Valor | Fuente |
|---|---|---|---|---|
| Pieza (peso bruto) | — | 2,800 kg | 79,80 € | **[estimado]** dentro del rango de iumm.es, «entre los 2,5 y los 3,2 Kg» |
| Centro, cabeza y punta limpios | Útil | 2,100 kg (75,0 %) | — | **[derivado]** merma de limpieza del 25 % de iumm.es¹ |
| Cordón limpio | Subproducto | 0,160 kg (5,7 %) | 9,50 €/kg | peso **[estimado]** ≈ 5,6 % de un test pesado publicado²; valor **[estimado]** = picada 80/20 del 08 |
| Grasa, telilla y nervios | Desecho | 0,540 kg (19,3 %) | — | **[derivado]** resto del 25 % |
| Pérdida de corte | calculada | 0,000 kg | — | los componentes suman la pieza |

¹ https://iumm.es/blog/limpieza-solomillo/: «después de su limpieza merma un 25%». Contraste: Carne y Delicatessen,
«un solomillo entero sucio con cordón de unos 2.000g» → «el entero limpio… ronda los 1.300g» (35 % bruto); el
solomillo que se compra ya limpio rinde un 85-95 % (Cárnicas Ismael) y el blog propio da un 10-15 %.

² For Love of the Table (2010), «5 oz. of usable trimmed chain meat (5.6% of the original weight)». No se encontró
ningún test español publicado con el reparto por partes (buscados: iumm.es, Directo al Paladar, Pilpileando, Carne y
Delicatessen, Cárnicas Ismael, Gastronomía Rentable).

**Resultado:**

| Concepto | Valor |
|---|---|
| Valor de los subproductos | 1,52 € |
| Coste neto útil | 78,28 € |
| Rendimiento bruto | 75,0 % |
| Coste por kg útil | 37,28 €/kg |
| Factor de coste | 1,3079 |
| **Merma % para tu escandallo** | **23,5 %** (0,235437), dentro de «Carne roja» 15-25 % |
| Porción de 200 g | 7,455 € |
| **Raciones por pieza** (fila 38, calculada, hacia abajo; §8) | ⌊2,100 × 1.000 ÷ 200⌋ = **10** |

### Test de cocción

Es la smash burger del 08: 1,8 kg de mezcla 80/20 a 9,50 €/kg, es decir, 10 hamburguesas de 180 g.

| Dato | Valor |
|---|---|
| Peso cocinado | 1,332 kg, **[derivado]**: 1,8 × 0,74, el rendimiento del USDA³ |
| Pérdida por cocción | 26 % |
| Coste por kg cocinado | 12,84 €/kg, con `C8/((1−C10)·(1−C15))` (R1 CH-04) |
| Porción cocinada | 133 g, que cuesta 1,707 € |
| Merma combinada | 26 % (despiece 0 %) |

³ USDA Food Buying Guide, Section 1: «Beef, Ground… no more than 20% fat… 1 lb AP = 0.74 lb cooked»
(PDF del yield table, pág. 13).

Nota de la hoja: el peso cocinado **no es una medida**. C8 es ya el **precio de factura** (el de la ficha) y C10 la
merma de despiece: así el coste por porción cocinada coincide con la ficha para cualquier merma de despiece.

### Convenciones cumplidas

- Celda verde «Gramos por kilo (para la porción)» = 1.000. Ninguna fórmula lleva constantes de unidad.
- DV `Útil,Subproducto,Desecho`.
- Formato condicional en rojo si la pérdida de corte sale negativa. Va redondeada a 6 decimales, porque la coma
  flotante daba ±4e-16, y con `+0` para que la caché no guarde «-0.0».
- Fecha con numFmtId 14.

## 3. Libro 13: Lista de Precios de Ingredientes

- **Filas: 115 ingredientes + 30 vacías = 145** (filas 10-154).
  - Se leen de las 8 fichas publicadas: 156 filas de ingrediente.
  - `alias` une 22 nombres del mismo producto. Si unen precios distintos con la misma unidad, la lista se queda con
    el de la fila de nombre canónico y avisa del otro en «Notas»; con unidades distintas, el script aborta.
  - «Bebida (vino + agua)» (06) queda **fuera**: es una partida compuesta, no un producto de proveedor.
- **6 ingredientes con dos precios dentro del propio kit** (preexistente; avisados en «Notas»: «La plantilla NN lo usa
  a …, otro proveedor»): huevo campero (3,60 / 4,20 €/docena), harina floja (0,90 / 1,20), zanahoria (1,20 / 1,40),
  mantequilla (9,00 / 10,50 del frosting del 07), azúcar glas (2,50 / 2,80 del frosting del 07) y sal (0,60 / 0,80 del
  borde del 04).
- **Notas:** cada ingrediente dice en qué fichas se usa («Se usa en: 03 «Postre» · 07 «Tostada Aguacate», …»),
  generado del mapa de lectura. Altura de fila calculada para que se lea.
- **Formatos de compra:**
  - Los de los destilados y el Prosecco salen de 04 «Formatos de Compra».
  - El resto son **[estimado]**, formato HORECA habitual.
  - El precio del formato se **deriva** del de la ficha, nunca al revés.
  - Los huevos van por unidad: «Estuche 30 huevos», 0,3000 €/ud. Así el ejemplo enseña un factor ≠ 1 (docena→ud).
- **Precio anterior** = el que tienen ahora tus fichas (R1 CH-05). Solo en 2 filas «Ilustrativo» `[estimado]`:

  | Fila | Anterior | Actual | Variación | Estado |
  |---|---|---|---|---|
  | AOVE | 6,80 € | 7,50 € | +10,3 % | ALERTA |
  | Solomillo | 28,00 € | 28,50 € | +1,8 % | OK |

- **Fórmulas:**
  - Precio por unidad base: `ROUND(G/E,4)`.
  - Variación: `ROUND(H/I-1,6)`. Sin el redondeo, 21/20-1 da 0,05000000000000004 y una subida exactamente
    igual al umbral dispararía la alerta.
  - Estado: `J>$B$5` → ALERTA u OK, con formato condicional rojo/verde.
  - Resumen: `COUNTIF(A,"?*")`, `COUNTIF(K,"ALERTA")` y `MAX(J)`.
- **Tabla:** autofiltro en A9:M154, DV de unidades en F, fechas vacías con numFmtId 14.
- **Protección (R1 CH-02):** sin contraseña. Las columnas de fórmula **H, J y K están bloqueadas**; el resto de la tabla,
  editable. El autofiltro funciona con la hoja protegida; **ordenar exige desproteger** (Excel no ordena rangos con celdas
  bloqueadas), así que el permiso de ordenar se deja cerrado. Rebaja anotada de R2T-08.
- **Impresión (R1 CH-08):** A1:L154, sin «Notas»; título y nota combinados hasta L.
- Las Instrucciones dan el método **Pegado especial → Valores** (Excel Ctrl+Alt+V → V; Sheets Ctrl+Mayús+V) y
  advierten que un pegado normal deja la línea en blanco sin avisar (R1 T3).

## 4. Parche de los 12 publicados

- **(a) Rango de `Conversiones`:** **453/453** fórmulas pasan a `Conversiones!$A$5:$B$67`, con n = 33 parejas + 30
  libres. Por libro: 20 + 135 + 48 + 62 + 52 + 20 + 67 + 49. El área de impresión pasa a `$A$1:$J$67` y la nota A2
  dice «hasta la fila 67».
- **(b) Versión y subject:** «Versión 2.1 · septiembre 2026 · aichef.pro/kit-escandallos · info@aichef.pro» y
  subject «Kit de Escandallos Pro · v2.1» en los **14** libros.
- **(c) 01!H5:** 0,20 → **0,2354**, la merma calculada por pycel en el 12, redondeada a 4 decimales.
- **(c2) 08!Smash Burger!H5 (R1 CH-03/T2):** 0,15 → **0**. La picada se compra lista y la ficha escribe su peso crudo.
- **(c3) Correcciones de texto (R1 CH-10), 7 celdas:** 08 «Carne picada (blend 80/20)» → «(mezcla 80/20)»;
  categorías: salsa de soja (02) y salsa BBQ (08, ×2) y caramelo líquido (03) → «Salsas/condimentos»; coliflor (02) →
  «Verdura hoja»; hinojo (02) → «Verdura raíz». Sólo texto: ningún coste cambia.
- **(c4) 03!Rotación Semanal (R1 T6):** K3 = `='Resumen Menú'!$C$13` (bloqueada, rótulo en J3) y la regla roja de
  K5:K11 pasa a `AND(ISNUMBER(K5),K5>$K$3)`: Google Sheets no admite otra hoja en un formato condicional.
- **Impacto en los ejemplos (para el changelog 2.1):**

  | Ficha | Concepto | v2.0 | v2.1 |
  |---|---|---|---|
  | 01 Escandallo | Coste del solomillo | 7,13 € | 7,45 € |
  | 01 Escandallo | Coste del plato | 11,46 € | 11,82 € |
  | 01 Escandallo | PVP sugerido sin IVA | 38,21 € | 39,42 € |
  | 01 Escandallo | PVP sugerido con IVA | 42,03 € | 43,36 € |
  | 08 Smash Burger | Coste de la picada | 2,01 € | 1,71 € |
  | 08 Smash Burger | Coste por ración | 3,44 € | 3,11 € |
  | 08 Smash Burger | PVP sugerido sin IVA | 11,47 € | 10,37 € |
  | 08 Smash Burger | PVP sugerido con IVA | 12,62 € | 11,41 € |
  | 08 Smash Burger | Margen bruto | 8,03 € | 7,26 € |
  | 08 Punto de Equilibrio | Unidades/día para cubrir costes | 38 | 40 |

- **(d) Líneas de texto:**
  - En las Instrucciones de 01-08, línea que remite al 13, tras «Precio/Ud (€)». La del 04 excluye los destilados,
    que se enlazan desde «Formatos de Compra».
  - En las Instrucciones del 01, línea «La merma del solomillo (23,5 %)…» que remite al 12.
  - En `Mermas!A3` de 01-08, «Mide tu merma real con la plantilla 12…» (97 caracteres: cabe en el papel, R1 T5).
  - Ni hojas ni columnas nuevas. Fórmula nueva: sólo 03!Rotación Semanal!K3 (R1 T6).

## 5. Verificaciones (todas en serie; CPU 41-46 °C)

Resultados de la última pasada, tras R1.

| # | Verificación | Resultado |
|---|---|---|
| 1 | pycel en los 14 libros (2.799 fórmulas) | **0** #REF!/#VALUE!/#DIV/0!/#NAME?, ni evaluando ni en caché. En 09 (16) y 11 (18) hay `#N/A` de `IF(x=0,NA(),…)`, que existen **por diseño** desde la v2.0 para que las líneas del gráfico no caigan a 0 |
| 2 | 12 | Rendimiento 0,75 ∈ (0,1). Factor 1,3079 ≥ 1. Merma 0,235437 = 1 − 1/factor, dentro de 15-25 %. Coste por porción: 12 = 7,4552 €; 01 v2.1 J5 = 7,4549 € (0,005 %); 01 **publicado** con la merma exacta = 7,4552 € (0 %). Cocción: ficha equivalente = test (1,7074 €); con merma de despiece 23,5 % y precio de factura, test = ficha (7,4552 €); 08 J5 = 1,71 € frente a 1,7074 € del test (0,15 %, redondeo de 133 g) |
| 3a | 13, alertas | +6 % ALERTA · **+5 % exacto OK** · +4,9 % OK · −10 % OK · +5,01 % ALERTA · umbral 10 %/11 % sobre el AOVE: ALERTA/OK. Resumen en caché: 115 ingredientes, 1 alerta, mayor subida 10,29 % |
| 3b | 13 ↔ fichas | **147/156** filas de ficha cumplen «precio del formato ÷ contenido = precio de la ficha ÷ factor». 8 son los segundos precios del kit, avisados en la Nota de su fila; 1 excluida («Bebida (vino + agua)»). «Se usa en» completo en 115/115. Bloqueo: H/J/K bloqueadas, resto libre. Autofiltro sí, ordenar no. Área A1:L154 |
| 4 | Rango libre | Pareja `lata→g` = 400 en la fila 38: la fila 15 del escandallo da factor 400 y coste 0,4891 € (el esperado). En la fila 67 también resuelve. En la 68 da «?» / «revisa unidades», fuera como debe. Control: en el 01 **publicado**, la fila 38 daba «?» |
| 5 | `censo-entregables.py --only <dry-run> --fail` | **0 defectos** en 14 xlsx (sin caché 0, noA4 0, creator 0, nonlat 0, cadena vacía 0) |
| 6 | Paridad 01-08 | **2.021 fórmulas, 0 distintas** salvo el rango. Valores cambiados: sólo los previstos (01!H5, 08!H5, 03!J3/K3, `Conversiones!A2`, `Mermas!A3`) y las 7 correcciones de CH-10. Resultados de fórmula cambiados sólo en 01 «Escandallo» (9) y 08 «Smash Burger» + «Punto de Equilibrio» (17). Estructura: área de `Conversiones` y la regla de 03!Rotación Semanal. Estilos: sólo `Mermas!A3` y 03!J3/K3. Instrucciones: sólo líneas añadidas |
| 7 | Forma | A4, `fitToWidth 1`, `fitToHeight 0` y pie «Página &P de &N» en las 5 hojas nuevas; el 12 en vertical. numFmtId 14 en los estilos. Hojas protegidas sin contraseña con las verdes desbloqueadas. Sin COUNTA. Toda división dentro de IFERROR. Metadatos como el kit (created = modified, UTC). Gráficos de 09 y 11 intactos |
| — | Idempotencia | 2.ª pasada del dry-run: **0 diferencias**. `--real` simulado sobre una copia de `dl/`, dos pasadas: 0 entre pasadas y 0 con el dry-run; PDF del bono con el mismo sha256 (`c7c26022…`). `dl/` sin cambios en git |

## 6. Estimado, sin resolver o para decidir

1. **[estimado]:**
   - el despiece del solomillo es **orientativo** (pieza 2,8 kg, merma de limpieza del 25 % de iumm.es, cordón ≈ 5,6 %);
     conviene que John pese uno real de su proveedor y sustituya `datos_ejemplos.json → despiece` (el pipeline recalcula
     01!H5 y el changelog solo);
   - valor del cordón 9,50 €/kg; formatos comerciales del 13; precios anteriores de demostración.

   **[derivado]:** peso útil y desecho del despiece; peso crudo 1,8 kg, peso cocinado 1,332 kg y porción de 133 g.
2. El test pesado de EE. UU. (merma 36 %) queda en `despiece.reservado_en` para el **Recipe Costing Kit EN**, donde el
   producto nativo sí es un *whole untrimmed tenderloin*.
3. **Preexistentes, no tocados:**
   - BONUS y 11 hablan de «precio unitario» y no remiten al 13. Los precios del BONUS (solomillo 26 €) no son los
     de las fichas, así que no se ha añadido la línea;
   - «Espárrago verde» sigue en «Verdura hoja» (ver R1 CH-10).
4. Los títulos de sección de las Instrucciones de 12 y 13 van en Title Case, como se pidió. Los de 01-11 siguen en
   minúscula de frase. No se han cambiado: solo se permitía texto añadido.
5. Categoría del 13 sin desplegable. La lista inline mide 260 caracteres, más que el máximo de 255, y el 13 no tiene
   hoja `Mermas` a la que apuntar.
6. **Sin revisión visual en Excel ni LibreOffice** (restricción térmica, sin navegador). Pendiente de mirar: alturas
   de filas con notas combinadas y de las «Notas» del 13, autoajuste de las Instrucciones y vista previa de impresión
   (12 en vertical, 13 hasta la columna L).
7. ~~Pendiente de John: la fila calculada «Raciones que salen de la pieza» (R1 CH-12).~~ **Resuelto en la
   publicación** (decisión de Claude, §8): fila 38 «Raciones por pieza».
8. **Fuera de este encargo** (PR de publicación, SPEC §2.0):
   - ejecutar `main.py --real --scratch <carpeta>`;
   - `kit-escandallos` en `EXCLUIDOS` de `postprocess-transversal.py`;
   - claves en `get-download-urls.ts`;
   - landing, dashboard y 7 hubs de «11» a «13»;
   - `emailBody`, changelog 2.1 (con la tabla de §4) y broadcast.

## 7. Revisión R1 de la v2.1

Ronda adversarial de 12 y 13 (R2-16): lente de chef/gerente español (CH-01…CH-12) y lente técnica (T1…T8). Todo se
arregla **en el código** y se regenera con `main.py`; nada a mano en los xlsx.

| id | Sev. | Resultado | Qué se ha hecho / motivo |
|---|---|---|---|
| CH-01 | alta | **Aplicado** (vía intermedia) | No existe un test español publicado con reparto por partes, y pesar uno no es posible en esta sesión. El despiece ES pasa a ser un **ejemplo orientativo** anclado en la referencia española (iumm.es: pieza de 2,5-3,2 kg, merma de limpieza del 25 %): 2,8 kg, 2,100 útil, 0,160 de cordón (≈ 5,6 % del test US), 0,540 de desecho. Merma para la ficha **23,5 %**, dentro de «Carne roja» 15-25 %. 01!H5 = 0,2354 y el PVP con IVA del ejemplo queda en 43,36 € (no 49,21 €). Hoja e Instrucciones dicen «no es un test pesado» y ya no presentan como ternera un test de EE. UU. Contraste de `datos_ejemplos.json` reescrito. Test US reservado para el EN. Pesar uno real sigue siendo lo ideal (§6.1) |
| CH-02 | alta | **Aplicado** (opción preferida) | H, J y K bloqueadas; filtrar funciona protegida y ordenar exige desproteger (rebaja R2T-08, anotada en §3). B9: «vacíalos seleccionando solo las columnas verdes… la hoja no deja borrarlas» |
| CH-03 | media | **Aplicado** (con T2) | 08!Smash Burger!H5 → 0 con guarda sobre A5; impacto en §4. Instrucciones del 12: «la ficha 08 lleva también un 0 %» |
| CH-04 | media | **Aplicado** (opción preferida) | C8 = «Precio de compra por kg (€/kg)», el de la factura; C16 = `C8/((1-C10)*(1-C15))`; notas de C8 y C10 e Instrucciones. El ejemplo no cambia (C10 = 0). Verificado con el solomillo (C10 = 23,5 %): test = ficha |
| CH-05 | media | **Aplicado** | «Precio anterior = el que tienen ahora tus fichas»; se actualiza al llevar el precio nuevo a las fichas (nuevo paso 4). La alerta avisa de fichas desfasadas; línea sobre subidas pequeñas encadenadas. Cabecera sin cambio |
| CH-06 | media | **Aplicado** | «Se usa en: …» en las 115 filas, generado del mapa de lectura (antes de las otras notas); línea en «Qué Es Cada Columna»; altura de fila |
| CH-07 | baja | **Aplicado** | Las dos pestañas de test del 12, en vertical |
| CH-08 | baja | **Aplicado** | Área de impresión A1:L (sin Notas); título y nota combinados hasta L |
| CH-09 | baja | **Aplicado** | «Peso bruto de compra», «Coste bruto de compra», «% del peso bruto», «(peso bruto)»; «Gramos por kilo (para la porción)»; D36 «En crudo y ya limpia…»; nota de demostración «…cómo funciona la alerta»; «Caja 6 briks de 1 L» |
| CH-10 | baja | **Aplicado en parte** | Alias con nota: mantequilla y azúcar glas del frosting (07), sal del borde (04). «mezcla 80/20» en vez de «blend» (08 y 13). Categorías: salsa de soja, salsa BBQ y caramelo líquido → «Salsas/condimentos»; coliflor → «Verdura hoja»; hinojo → «Verdura raíz» (bulbo, como cebolla y chalota en el kit). «Bebida (vino + agua)» fuera del 13. **Rechazado:** espárrago verde sigue en «Verdura hoja». De las 21 categorías es la más cercana (tallo tierno, merma típica 20-35 %), y crear una nueva es estructura en los 8 libros (hoja «Mermas», DV y VLOOKUP) |
| CH-11 | baja | **Aplicado** | «¿Te quedas sin filas?…» y «Si… borras una fórmula, cópiala de las filas vacías del final» en «Protección de la Hoja» |
| CH-12 | baja | **Aplicado en versión mínima** | Sin OK de John para una fila nueva sobre la SPEC: líneas de Instrucciones con la cuenta y el ejemplo (10,5 raciones por pieza; 10 hamburguesas por tanda). La fila calculada queda pendiente de John (§6.7) |
| T1 | media | **Aplicado** | «Filtrar y Ordenar»: filtra «Estado» por ALERTA; para ordenar «Variación», quita antes (Vacías) |
| T2 | media | **Aplicado** | Igual que CH-03 |
| T3 | media | **Aplicado** | En el 13 y en `LINEA_13` de 01-08: el pegado normal deja la línea en blanco sin avisar y el coste del plato baja |
| T4 | baja | **Aplicado** | `filas_lista()`: alias con precios distintos y la misma unidad = conflicto con nota; con unidades distintas, aborta. El precio de la lista es el de la fila de nombre canónico |
| T5 | baja | **Aplicado** (alternativa) | `Mermas!A3` acortada a 97 caracteres (≤ 110): cabe sin combinar ni cambiar estructura |
| T6 | baja | **Aplicado** | 03!Rotación Semanal!K3 con el objetivo y la regla contra `$K$3` (§4 c4). Va al changelog. La afirmación de la FAQ sobre Google Sheets sigue sujeta a D16 |
| T7 | baja | **Aplicado** | `metadatos()` en UTC: created = modified |
| T8 | baja | **Aplicado** | Sin rutas de sesión en el código. `--scratch` o `CLAUDE_SCRATCHPAD`; sin ellas, el dry-run va a `.work/` y `--real` aborta (probado) |

Además, durante R1:
- La pérdida de corte del ejemplo nuevo guardaba «-0.0» en caché: `ROUND(…)+0`.
- `verificar.py` aprende las excepciones previstas (valores, estilos, reglas y resultados que cambian) y comprueba lo
  nuevo: horquilla de la merma, ficha 08 = test, cocción con despiece, bloqueo H/J/K, «Se usa en», área A1:L y 12 en
  vertical. Trampa de pycel: `set_value` sólo recalcula las fórmulas que ya estaban evaluadas; hay que evaluar antes
  entradas **y** resultados.

**Verificaciones tras R1** (detalle en §5): pycel 0 errores en 2.799 fórmulas · 12 coherente con 01 y 08 · 13 con
alertas correctas, 147/156 + 8 avisadas + 1 excluida · rango libre OK · censo 0 defectos · paridad solo con los cambios
previstos · forma OK · idempotencia 0 diferencias (dry-run y `--real` simulado).

## 8. Publicación (sesión Claude Code, 24-sep-2026)

Rama `feat/kit-escandallos-v2-1`, en un **worktree** aparte (otra sesión usaba el árbol principal). Todo en serie;
CPU 42-50 °C. Sin `astro build` ni navegador: el build lo hace Netlify en el deploy preview.

**Paso 0 · Raciones por pieza (R1 CH-12, decisión de Claude).** `nuevas.py`: fila 38 de «Test de despiece»,
`=IFERROR(ROUNDDOWN(ROUND(C29*C11/C36,6),0),"")` (formato `#,##0`, bloqueada como el resto de calculadas). pycel
evalúa `ROUNDDOWN` (probado aparte, también el `""` con porción vacía). El `ROUND(…,6)` previo evita que la coma
flotante deje 9,9999999 y reste una ración. Ejemplo: **10** raciones (10,5 → hacia abajo). La línea de Instrucciones
ahora cita la fila («RACIONES POR PIEZA: … En el ejemplo, los 2,100 kg útiles dan 10 raciones de 200 g (sobran
100 g)…»). `DESP['raciones'] = 'C38'`; `raciones_python()` redondea igual que la hoja y `verificar.py` compara pycel
con Python. `verificar.py` gana `--pruebas` (sin él, tras `--real` las copias de prueba caerían en
`astro-site/public/dl/v2_1-pruebas/`). Dry-run y `verificar.py`: **OK**, 0 diferencias de idempotencia.

**Paso 1 · `--real`.** `ROOT` se resuelve desde `__file__` (main.py y nuevas.py), así que escribe en el `dl/` del
worktree; comprobado antes de ejecutar. `KIT_ESCANDALLOS_APPLY=1 main.py --real --scratch <scratchpad>/v21pub`:
respaldo en `<scratchpad>/v21pub/kit-escandallos.bak-20260924-172455`, merma 0,235437, idempotencia 0 diferencias,
`inject_cache` 14/14 con `fallos_pycel=0`.
- `dl/kit-escandallos/`: **14 xlsx + el PDF** (15 ficheros). PDF del bono con el **mismo sha256** que antes
  (`c7c26022…66ad2`): no se añade al commit.
- `verificar.py --carpeta dl/kit-escandallos --publicados <respaldo> --pruebas <scratchpad>`: **VERIFICACIÓN OK**.
  pycel 0 errores en 2.800 fórmulas (una más que en §5: la fila 38); raciones pycel 10 = Python 10; 01 v2.1 J5
  7,4549 € vs 12 7,4552 €; 08 H5 = 0, J5 1,71 € vs test 1,7074 €; 13: 147/156 + 8 avisadas; rango libre OK;
  paridad 01-08 solo con los cambios previstos; forma OK.
- `censo-entregables.py --only kit-escandallos --fail`: **0 defectos** (15 ficheros: 14 xlsx + 1 pdf).

**Paso 2 · Capa web ES.**

| Fichero | Cambio |
|---|---|
| `netlify/functions/get-download-urls.ts` | claves `test-rendimiento` y `lista-precios` → 12 y 13 |
| `src/pages/KitEscandallosDashboard.tsx` | 2 tarjetas (`Scale`, `ReceiptText`, de lucide-react 0.462.0) + «Tus 13 plantillas + 2 bonus» / «13 Plantillas + 2 Bonus» |
| `astro-site/src/data/productos/kits/kit-escandallos.ts` | «11» → «13» en seo, schema, hero, grid (`countGold`), bonus, cta y `bonusTotalLabel`; 2 tarjetas (`Scale`, `Euro`, existentes en `Icon.astro`); FAQ nueva «¿Qué aportan el Test de Rendimiento y la Lista de Precios?» en on-page y en el FAQPage (dice que la lista NO alimenta sola las fichas: Pegado especial → Valores); `updateNote` «Versión 2.1 · septiembre 2026» |
| Hubs (`ProductosDigitalesHubPage.astro` + 6 `DigitalProductsHubPage*.astro`) | tarjeta del kit: «11» → «13» en la descripción y en la 1.ª feature, en su idioma. Nada más |
| `netlify/functions/verify-purchase.ts`, `resend-access.ts`, `src/data/productos-digitales-config.ts` | `emailBody` «las 13 plantillas Excel + 2 bonus»; el espejo también con las 2 claves nuevas |
| `astro-site/src/data/productos/guias/guia-food-cost-ingenieria-menu.ts` | FAQ «El Kit son 13 plantillas…» |
| `src/data/productos-changelog.ts` | entrada 2.1 (8 líneas, sin cifras que sincronizar) y `version: '2.1'` |
| `scripts/productos-digitales/postprocess-transversal.py` | `kit-escandallos` en `EXCLUIDOS` |
| `scripts/productos-digitales/tienda-gate.py` | `--esperadas <ruta>[,<ruta>]` para `--es-identico`: diff del texto visible sin fallar; ruta desconocida = fallo; sin `--es-identico` = error de uso. Probado con HTTP simulado |

`products-catalog.ts` no cita el número: sin tocar. SPA muerta sin tocar (no se construye): `src/pages/KitEscandallos.tsx`,
`src/components/kit-escandallos/*`, `src/pages/ProductosDigitales.tsx` (hub de la SPA) y `netlify/edge-functions/og-meta.ts`.

**Paso 3 · Gates estáticos.**

| Gate | Resultado |
|---|---|
| grep «11 (plantillas\|templates\|…)» en `src`, `astro-site/src`, `netlify` | **0** del kit fuera de la SPA muerta. Quedan los de otros productos (Kit de Tareas Restaurante Creativo, kits de chocolatería, changelog de los kits de tareas). OJO: el grep no ve «11 Excel templates/‑Vorlagen/‑sjablonen» (EN, DE, NL); esos se encontraron leyendo la tarjeta y están corregidos |
| `@astrojs/compiler` + esbuild, 7 `.astro` | compilan; 3 avisos `is:inline` preexistentes (idénticos en `HEAD`) |
| esbuild, 8 `.ts/.tsx` | parsean |
| `gate-flujo-postpago.py --offline --only kit-escandallos` (con los xlsx en el índice) | **0 fallos**: 15 ficheros, 15 tarjetas; 2 avisos propios de `--offline` (secciones D y E) |
| `tienda-gate.py` (estático) | **verde** |

**Sin verificar (necesita build/preview, lo hace el orquestador):** `astro build` (tipos incluidos), render de la
landing, del dashboard y de los hubs; `gate-flujo-postpago.py --base <preview>` (sección B: los `/dl/` en vivo y sus
tamaños); `tienda-gate.py --es-identico --base <preview> --esperadas /kit-escandallos`; revisión visual de la fila 38
en Excel/LibreOffice. Broadcast ES en la cola de 5 días: pendiente (fuera de este encargo).

**Aviso de copy (no tocado):** la FAQ de la Guía Food Cost termina «si ya lo tienes, no compras nada repetido». La
Guía incluye un xlsx «Rendimiento y Mermas por Producto» (test de rendimiento y merma de cocción) y el Kit v2.1 trae
ahora el suyo (plantilla 12): la frase merece revisión.

