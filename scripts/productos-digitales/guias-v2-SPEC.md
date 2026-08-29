# Familia «Guías Cómo Montar» — v2.0 (SPEC, 2026-08-29)

Origen: ronda 1 adversarial del **representante** (`auditorias/guia-restaurante-gastronomico-R1.json`, 3 lentes opus — técnica Excel, dominio de aperturas,
coherencia comercial; **106 hallazgos** (TEC 30 · DOM 40 · COM 36), «no listo» ×3), más un **censo propio de los 8 productos** hecho para esta SPEC (openpyxl +
python-docx + PyMuPDF, 2026-08-29). Lo que sigue es lo que SE HACE; lo demás se descarta en §7 o se pregunta en §7 «para John»; la evidencia vive en el R1 y se
cita aquí por id. Método y código de referencia: `kit-plan-financiero-v2-SPEC.md` y `kit-tareas-v2-SPEC.md` con sus paquetes (motor + grupos + módulo de
contenido por producto, `main.py --dry-run / --solo / --producto`, respaldo previo, `inject_cache.py` al final, verificación `data_only`, idempotencia por
reconstrucción), y `kit-escandallos-v2_0/bono_guia.py` como precedente de **documento producido de verdad** (bridge.py → Markdown → docx + PDF reportlab con
saneado WinAnsi y gate propio).

Paquete nuevo: `scripts/productos-digitales/guias-v2_0/` — `motor.py`, `grupo_a.py`, `grupo_b.py`, `grupo_c.py`, `documentos.py`, `contenido_<pid>.py` (uno por
guía), `guion_<pid>.py` (guion de capítulos por guía), `main.py`. Ejecución real **solo** con `GUIAS_APPLY=1`; `--dry-run` por defecto, escribiendo a
scratchpad. Nada de builds locales ni navegador; `istats cpu temp` antes de cada python y **un proceso cada vez**.

## Alcance medido (censo propio, 2026-08-29)

**141 ficheros en 8 productos**: 111 `.xlsx` + 22 `.docx` + 8 `.pdf`. Ninguno tiene caracteres no latinos (barrido hecho: 0 en xlsx, 0 en PDF).

| pid | € | ficheros | xlsx | xlsx con **0 fórmulas** | fórmulas totales | PDF pág. / palabras | docx guía (palabras) | bonus docx (palabras) | páginas prometidas | mismos defectos |
|---|---|---|---|---|---|---|---|---|---|---|
| **guia-restaurante-gastronomico** (representante) | 85 | 22 | 18 | **12** (8 checklists + ticket-medio + pl-mensual + gantt + turnos) | 236 | **10 / 2.488** | 2.395 (2.157 + 238 en 4 tablas) | business-plan 300 · manual-sala 255 | **80+** | — |
| guia-restaurante-casual | 65 | 19 | 15 | **9** (6 checklists + pl-mensual + gantt + turnos) | 127 | **1 / 33** (portada) | 2.917 | business-plan 287 · manual-oper. 376 | 60+ | **sí + NUEVO-01** |
| guia-restaurante-mexicano | 65 | 19 | 15 | **9** | 174 | **1 / 33** (portada) | 4.195 | 360 · 660 | 60+ | **sí + NUEVO-01** |
| guia-restaurante-peruano | 65 | 19 | 15 | **9** | 175 | **1 / 33** (portada) | 4.763 | 388 · 982 | 60+ | **sí + NUEVO-01** |
| guia-restaurante-japones | 65 | 19 | 15 | **9** | 179 | **1 / 33** (portada) | 5.813 | 400 · 1.261 | 60+ | **sí + NUEVO-01** |
| guia-restaurante-nikkei | 65 | 19 | 15 | **9** | 183 | **1 / 33** (portada) | 6.317 | 463 · 1.439 | 60+ | **sí + NUEVO-01** |
| guia-panaderia-obrador | 65 | 19 | 15 | 3 (gantt, plan-fermentación, turnos) | 185 | **1 / 55** (portada) | 4.699 | 796 · 944 | 70+ | parcial (molde propio) **+ NUEVO-02** |
| guia-dark-kitchen | 24 | 5 | 3 | **0** | 96 | **27 / 7.023** | 7.023 | — (sin bonus docx) | +40 | parcial (producto distinto) |

**Lo que el censo cambia respecto de la lectura del R1** — y que obliga a que esta SPEC sea de FAMILIA, no del representante ampliado:

1. **En 6 de las 8 guías el PDF no es una guía corta: es UNA PORTADA.** 1 página y 33-55 palabras. La guía real vive en el `.docx`, que ninguna landing anuncia
   como el entregable principal. El representante (10 páginas) y dark-kitchen (27) son las excepciones. **Ninguna de las 8 se acerca a lo prometido**: 80+, 70+,
   60+ ×5 y +40. Es la promesa más grave del catálogo porque es cuantitativa, verificable y falsa por factores de 8× a 60×.
2. **Las plantillas «vacías» del representante son, en los hermanos, plantillas CONGELADAS.** `pl-mensual-escenarios.xlsx` del gastronómico tiene 19 etiquetas y
   ni un valor; el de japonés tiene **tres hojas** (`Pesimista`/`Realista`/`Optimista`) llenas de **constantes tecleadas** y **0 fórmulas** — `Pesimista!B31`
   («EBITDA») vale `-12055` escrito a mano, y `B13` («Food cost (33%)») es el producto ya calculado. Cambiar un cubierto no mueve nada en ninguna de las dos
   formas. El motor tiene que tratar los dos casos: **rellenar el vacío** y **convertir la constante en fórmula** conservando el número como dato de ejemplo.
3. **`cash-flow-break-even.xlsx` no calcula el break-even en NINGUNA de las 7 guías que lo llevan.** En el representante faltan las cuatro filas de total
   (`Cash Flow 12 Meses!B10/B19/B21/B22`); en los hermanos la hoja `Cash Flow` está **entera en blanco** (B5:M27) y la hoja `Break-Even` tiene 2 fórmulas
   (`B11`, `B12`) y deja **vacía justo `B13` «Break-Even (meses)»**. Mismo defecto, dos direcciones distintas.
4. **`menu-engineering-matrix.xlsx` no clasifica en ninguna.** El representante tiene la columna `H` («Clasificación») vacía **y ninguna fila de ejemplo**; los
   hermanos traen 15 platos reales con `E`, `G` y `H` calculadas pero **`I` («Popularidad») y `J` («Clasificación») vacías**. Kasavana & Smith no está
   implementado en ningún libro de la familia.
5. **El escandallo tiene dos modelos distintos, los dos mal.** Representante: `H7='=D7*E7'` ignora la merma (`G7` se calcula y no la usa nadie), `H28='=H27/0.28'`
   con el food cost **hardcodeado** y sin dividir por raciones. Hermanos: `G6='=E6*(1+F6)'` — la merma sí entra, pero como recargo (`×1,20` para un 20 %) cuando
   lo correcto es `/(1-merma)` (`×1,25`), y `G19='=G18/0.33'` con el mismo hardcodeo. **El IVA sí está en los hermanos** (`G20='=G19*1.10'`) y **no está en el
   representante**: DOM-03 («la palabra IVA no aparece ni una vez») es cierto para el gastronómico y **falso para los hermanos**. El motor parametriza donde ya
   existe y añade donde falta.
6. **Los checklists tienen TRES moldes, no uno.** (a) **Molde A** — gastronómico + casual/mexicano/peruano/japonés/nikkei: pestaña `Sheet`, columnas
   `A #` · `B Categoría` · `C Tarea/Ítem` · `D Responsable` · `E Fecha Límite` · `F Estado` (DV `"Pendiente,En Curso,Completado"`) · `G Coste Est. (€)` ·
   `H Notas`; **0 fórmulas, 0 formato condicional, 0 fila TOTAL, sin hoja `Instrucciones` y sin línea de versión**. (b) **Molde B** — panadería: pestaña con
   nombre propio, columna `A` de casillas `☐`, `B Trámite` · `C Responsable` · `D Plazo orientativo` · `E Notas`, **sin columna de coste**, con contador
   `C36='=COUNTIF(A4:A34,"✓")'` / `E36='=COUNTIF(B4:B34,"?*")'` y formato condicional en `A4:E34`. (c) **Molde C** — dark-kitchen: `A #` · `B Zona` ·
   `C Equipo` · `D Proveedor` · `E Presupuesto` · `F Real` · `G Desviación (%)` con `'=IF(E5=0,"",((F5-E5)/E5))'` · `H Estado`, **y fila TOTAL ya presente**
   (`checklist-apertura-legal!F40='=SUM(F5:F39)'`). Un motor que dé por hecho el molde A rompe panadería y duplica el total de dark-kitchen.
7. **Los recuentos de ítems del R1 no cuadran entre sí.** Su `inventario` dice «checklist-legal 42 filas»; COM-18 y mi censo dicen **40** (`A5:A44`). Se toma la
   cifra **medida por el motor en tiempo de ejecución**, nunca la del informe (§9, gate de recuento).
8. **Lo que la Fase A ya dejó hecho y NO se toca**: A4 (`paperSize=9` + `fitToWidth=1`) en las 141 hojas, `creator='AI Chef Pro'` y `title` por fichero en los
   111 xlsx, casilla unificada, fórmulas rotas de `guia-dark-kitchen` reparadas y caché de valores (`inject_cache.py`). **Lo que la Fase A NO alcanzó**: la
   **bio anclada** (medido: 0 de 111 xlsx la llevan), la **línea de versión en los 8+6 checklists del molde A y en los 15 xlsx de panadería y los 3 de
   dark-kitchen** (medido: `None`), y **los 22 docx y los 8 PDF**, que siguen con `author='python-docx'` y `title='(anonymous)'`/`'untitled'` (COM-24).

9. **El censo ha encontrado DOS defectos que el R1 no podía ver**, los dos en el fichero que se lleva al banco: el `P&L Mensual` de los 5 hermanos **no tiene
   ni un total calculado** y el `P&L 3 años` de panadería **imprime un EBITDA igual a la facturación (300.000 €) y un margen del 122,97 %**. Detalle y
   corrección en §2.5 (`NUEVO-01`, `NUEVO-02`).

## Decisión: post-proceso de familia, NO reejecutar los generadores

Se construye un **motor de post-proceso sobre los ficheros existentes** (openpyxl) + un **módulo de contenido por guía**, y un **pipeline aparte para los
documentos**. Los 7 `scripts/generate-guia-*.py` (1.451-1.849 líneas, ~390 comunes) **no se reejecutan**. Razones, en orden de peso:

0. **La ruta de salida de los 7 generadores está MUERTA.** Los 7 calculan
   `OUTPUT_DIR = .../public/dl/<pid>` **desde la raíz del repo** (`scripts/generate-guia-restaurante-gastronomico.py:17-19` y equivalentes), y el commit
   `7e050c5` («los 524 entregables daban 404 desde el 19-jul», 2026-08-08) movió todo a `astro-site/public/dl/*` con el cutover a Astro **sin actualizar los
   scripts**. `public/dl/` en la raíz tiene hoy un `.DS_Store` y **cero ficheros trackeados**. Ejecutar cualquiera de los 7 tal cual **no llegaría a
   producción**: escribiría en una carpeta que ni sirve Netlify ni trackea git. Este repo ya pagó 20 días de 404 en el flujo de cobro por esta misma clase de
   ruta obsoleta.
1. **Reejecutar un generador REINTRODUCE un bug ya reparado, y es demostrable.** El código fuente de 5 de los 7 sigue teniendo la **autorreferencia circular**
   `sdc(ws2, r, 2, "=B12*(1-B8)", …)` en `cash-flow-break-even.xlsx!'Break-Even'!B12` — `generate-guia-restaurante-casual.py:766`, `japones.py:914`,
   `mexicano.py:862`, `nikkei.py:920`, `peruano.py:879` —, mientras que **los 5 ficheros vivos ya tienen `=B11*(1-B8)`**, que es la fórmula correcta, porque la
   Fase A la reparó (`postprocess-transversal.py:194`). Es un bug copy-pasteado 5 veces, no compartido: arreglarlo en el generador son 5 correcciones
   independientes; en el post-proceso es **una entrada de tabla**.
2. **Reejecutar un generador REVIERTE el resto de la Fase A.** Los generadores escriben el `.xlsx` desde cero; todo lo que
   `postprocess-transversal.py` inyectó después —A4 completo con márgenes y pie, metadata, casilla unificada, las 30 fórmulas reparadas (entre ellas las de
   `guia-dark-kitchen`, citadas en `FASE-A-SPEC-postprocess-transversal.md:164`) y la caché de valores de `inject_cache.py`— desaparece en silencio y con el
   build en verde. Es el mismo patrón que ya costó dinero con los ensambladores del blog (`CLAUDE.md`: «los ensambladores RECONSTRUYEN el cuerpo entero… pisa
   las ediciones manuales posteriores»).
3. **Son 7 ficheros que tocar frente a 1 motor + 8 módulos de contenido**, y no comparten un módulo común: los 6 helpers del esqueleto
   (`shr`, `sdc`, `title_block`, `brand_footer`, `instr_sheet`, `checklist_ws`, líneas 56-116/117) están **copiados byte a byte en 6 de los 7** —el único diff
   entre ellos es una docstring de más en `generate-guia-restaurante-gastronomico.py:94`— y `generate-guia-dark-kitchen.py` los **reimplementa con otros
   nombres** (`style_header_row:68`, `style_data_cell:77`, `add_title_block:91`) con 0 % de reutilización literal. Medido: **177 líneas únicas de esqueleto
   repetidas 331-372 veces por fichero = 21-25 % de cada script; el 75-79 % restante es contenido propio de cada cocina**. Y ninguno de los 7 tiene `argparse`,
   `--dry-run`, override de directorio ni guarda de idempotencia: cada `wb.save()` sobrescribe incondicionalmente.
4. **Son 7 ficheros que tocar frente a 1 motor + 8 módulos de contenido.** El defecto es el mismo en los 7 (`pl-mensual` sin fórmulas, `menu-engineering` sin
   clasificación, `cash-flow` sin break-even, checklists sin total): arreglarlo en el generador obliga a repetir la corrección 7 veces sobre 7 dialectos
   ligeramente distintos, y a re-verificar 141 ficheros. El post-proceso lo escribe una vez y lo aplica por familia, y el módulo por guía sólo lleva **lo que de
   verdad cambia** (nombres de hoja, filas, cifras del concepto).
5. **La infraestructura ya existe y ya cubre estas guías.** `postprocess-transversal.py` declara en su docstring (líneas 7-9) que aplica a los 42 productos de
   `astro-site/public/dl/`, y ya lleva parches por (fichero, hoja, celda) para esta familia: líneas 181-192 reparan 12 celdas circulares de
   `calculadora-viabilidad-dark-kitchen.xlsx` y la 194 repara el `Break-Even!B12` de las 5 guías. El paquete `guias-v2_0/` extiende ese patrón, no lo inventa.
6. **El post-proceso es idempotente por construcción y auditable**: `--dry-run` a scratchpad, respaldo previo, segunda pasada = 0 cambios, verificación
   `data_only`, y `censo-entregables.py` / `gate-flujo-postpago.py` como red. El generador no tiene ninguna de esas garantías.
7. **Excepción**: los **documentos** (1 PDF + 1 docx de guía + 2 docx de bonus por producto) **no se post-procesan: se PRODUCEN de nuevo** (§5). Ahí el
   contenido no existe —2.157 palabras para 22 capítulos, 255 palabras de «manual»—, así que no hay nada que parchear. Se escriben con `bridge.py` desde un
   guion por guía y se maquetan con el patrón de `bono_guia.py`. Los **nombres de fichero no cambian** (§7-bis.1). Y hay que escribir el pipeline **desde
   cero**, porque hoy no existe: 5 de los 7 generadores producen el PDF con `reportlab.pdfgen.canvas` de bajo nivel en una función cuyo propio docstring dice
   «*Generate a minimal placeholder PDF*» (`generate-guia-restaurante-casual.py:1402`) — cuatro `drawCentredString` de portada, con un fallback que **copia el
   `.docx` renombrado a `.pdf`** si falta reportlab—, y **`gastronomico` y `dark-kitchen` no tienen ni un import de reportlab**: sus PDF (10 y 27 páginas) se
   generaron fuera del pipeline y se commitearon como binarios en abril de 2026. Tampoco el texto es rescatable del generador: la prosa va como llamadas
   imperativas `doc.add_paragraph("…")` dentro de funciones de 359 a 1.175 líneas (`gen_guide_docx`), sin ninguna estructura de datos que parchear. Sólo el
   DOCX del gastronómico usa tablas reales de python-docx (`doc.add_table` ×4, líneas 204, 299, 352, 369); los otros seis y dark-kitchen **no llaman a
   `add_table` ni una vez**.

## Convenciones de familia (heredadas y verificadas)

Editables **verdes `E8F5E9`** y desbloqueadas, calculadas sin relleno; **parámetros en celda, nunca literales dentro de la fórmula**; `IFERROR` en toda
división; «sin dato» se escribe `""`, **nunca `0`**; semáforo por formato condicional (verde `C6EFCE`, ámbar `FFEB9C`, rojo `FFC7CE`) y **con `ISNUMBER`** en la
guarda cuando la celda puede traer texto; DV con `showErrorMessage=True`; protección de hoja **sin contraseña**; bio anclada; «Versión 2.0 · agosto 2026»;
metadata `title`/`subject` → `… · v2.0`; `inject_cache.py` al final; A4 ya presente, no se toca.

**pycel 1.0b30 (medido hoy, 2026-08-29, en este Mac):** evalúan bien `SUM`, `SUMPRODUCT`, `SUMIF`, `COUNTIF`, `IFERROR` (atrapa `1/0`), `IF`/`AND` anidados,
`TEXT`, `NPV`, `ROUND`, `MATCH`+`INDEX` con comparación de rango (`=IFERROR(MATCH(TRUE,INDEX(B40:G40>0,0),0),"No alcanzado")` → `4`) y la cadena completa de
Kasavana & Smith (`SUMPRODUCT(D,G)/SUM(D)` → margen medio; `0.7/COUNTIF(D,">0")` → umbral; `IF(AND(...))` anidado → `"Star"`). **NO implementa `IRR`, `PMT` ni
`COUNTA`** (documentado en `kit-plan-financiero-v2-SPEC.md`): `COUNTA(r)` → `COUNTIF(r,"<>")`; la cuota de un préstamo va como **anualidad algebraica**
`importe*i/(1-(1+i)^-n)`, nunca `PMT`.

---

## 1. Motor común (`motor.py`) — lo que se aplica a los **111 xlsx** de las 8 guías

El motor **no sabe de negocio**: detecta el molde, aplica convenciones y ofrece las primitivas que usan los grupos. Todo lo que dependa del concepto de la guía
(nombres de hoja, filas, cifras) vive en `contenido_<pid>.py`.

- **1.1 Detección de molde antes de tocar nada** (censo §6 de la cabecera). `molde_checklist(ws)` devuelve `A` | `B` | `C` | **`D`** mirando la cabecera de la
  fila 3/4: molde A si `B='Categoría'` y `G='Coste Est. (€)'`; molde B si `A='✓'` y `D='Plazo orientativo'`; molde C si `E='Presupuesto (€)'` y
  `G='Desviación (%)'`; **molde D si `F='Coste Estimado (€)'` y `G='Estado'`**.
  Si no encaja en ninguno **aborta con el nombre del fichero**: nunca «aplica el molde A por defecto». Igual para los libros financieros:
  `variante_pl(wb)` distingue **una hoja `Escenarios` con columnas B/C/D** (gastronómico) de **tres hojas `Pesimista`/`Realista`/`Optimista`** (los 5 hermanos)
  de **una hoja `P&L 3 escenarios`** (panadería).
- **1.2 Constantes → fórmulas, conservando el número.** `a_formula(ws, celda, formula, guardar_ejemplo=True)`: si la celda traía una constante (caso de los 5
  hermanos), el valor se conserva como **dato de ejemplo en la celda de entrada** de la que depende, y la celda de resultado pasa a fórmula. Nunca se borra un
  número que el cliente pueda estar usando sin sustituirlo por algo que calcule lo mismo. Verificación obligatoria: tras el cambio, el valor evaluado por pycel
  debe coincidir con la constante anterior con tolerancia 0,01 € **o la diferencia debe estar justificada por un defecto corregido** (p. ej. el EBITDA que ya no
  resta amortización), y en ese caso queda anotada en el informe del fichero.
- **1.3 Taxonomía de celdas y verdes.** Se retira el relleno `E8F5E9` de **toda celda que pase a ser calculada** —hoy hay 45 celdas verdes en
  `calculadora-ticket-medio!B5:D20` y otras 45 en `pl-mensual-escenarios!'Escenarios'`, incluidas las **filas de resultado** (TEC-01, TEC-02): la hoja le está
  pidiendo al cliente que teclee él el resultado— y se pinta de verde toda celda de entrada que hoy no lo esté. Regla: **verde ⇔ desbloqueada ⇔ el cliente
  escribe ahí**; sin verde ⇔ bloqueada ⇔ la calcula el libro.
- **1.4 Formatos numéricos por tipo, no por bloque** (TEC-09, TEC-24, TEC-25). Hoy el € se ha aplicado a rejillas enteras: `'Escenarios'!B11` («Food cost (%)»)
  y `B22` («Margen EBITDA (%)»), `'Ticket Medio'!B5`/`B11` (porcentajes), `'Break-Even'!B6` («Comensales/día») y `B7` («Días abierto/mes»),
  `menu-engineering!D5:D29` («Uds Vendidas») y `plan-financiero!'P&L Mensual'!B35` («Margen EBITDA») van todos en `#,##0.00 €`. `formato_por_etiqueta(ws, col)`
  decide por el texto de la etiqueta de fila/columna: `(%)` → `0.0%`, `Uds`/`Cubiertos`/`Días`/`Comensales`/`Uds Vendidas` → `#,##0`, `(€)` y todo importe →
  `#,##0.00 €`, `Inicio`/`Fin`/`Fecha` → `dd/mm/yyyy`.
- **1.5 IVA declarado en toda la familia** (DOM-03, COM-14). Dos reglas: **(a)** toda hoja que fije un PVP lleva **dos filas**, `PVP sin IVA` y
  `PVP con IVA` = `sin IVA × (1+tipo)`, con el **tipo en celda verde** (`0,10` por defecto, etiqueta «Tipo de IVA de restauración (%) — 10 % general; 21 % en
  bebidas alcohólicas»), nunca `*1.10` incrustado como está hoy en `escandallo-maestro-<hermano>!G20`. **(b)** toda hoja de P&L, cash flow o ticket medio lleva
  bajo la cabecera la línea «Todas las cifras van **SIN IVA**, salvo el cash flow, que va **CON IVA** porque es caja». En `cash-flow-break-even` se añaden las
  tres filas de IVA (§2.4).
- **1.6 Semáforos con `ISNUMBER`.** Ninguna regla de formato condicional compara directamente una celda que puede contener `""` o un texto de aviso: la guarda
  es `=AND(ISNUMBER($X5),$X5<0)`. Se aplica a los márgenes y EBITDA (`pl-mensual`, `plan-financiero`), al flujo acumulado (`cash-flow`), a la desviación de
  CAPEX y al estado de los checklists (§3.3).
- **1.7 Validación de datos** (TEC-06, TEC-12, TEC-15, TEC-17). DV decimal `0 ≤ x ≤ 0,95` con mensaje de entrada en **toda columna de merma o de porcentaje**;
  DV de fecha en `Inicio`/`Fin`/`Fecha Límite`; la DV de turnos `"M,T,P,L,V"` se **documenta** («V = Vacaciones») en vez de recortarla; DV numérica `≥ 0` en
  importes. Toda DV con `showErrorMessage=True`.
- **1.8 Protección de hoja** (TEC-30). `ws.protection.sheet = True` **sin contraseña** en las 141 hojas (hoy `False` en las 141), con
  `Protection(locked=False)` en las verdes y la línea «Para editar la estructura: Revisar → Desproteger hoja» en `Instrucciones`. Es lo que impide que arrastrar
  una entrada sobre una columna calculada borre la fórmula y el fichero siga dando un número, sólo que equivocado.
- **1.9 Fila TOTAL y contador de avance en los checklists** (TEC-16, COM-31). Molde A: fila `TOTAL` con `'=SUM(G5:G<n>)'` en `#,##0.00 €` + subtotales por
  categoría con `SUMIF` sobre `B`, y `'% completado' = COUNTIF(F5:F<n>,"Completado")/COUNTIF(F5:F<n>,"<>")`. Molde B: el contador ya existe; se le añade la
  fila de coste **sólo si el módulo de contenido aporta la columna** (§7.1, duda). Molde C: **ya tiene TOTAL**, no se duplica; se le añade el `% completado`.
  Los 313.290 € del representante repartidos en 8 listas dejan de sumarse a mano.
- **1.10 Instrucciones, pestaña, versión y bio.** Los **checklists del molde A no tienen hoja `Instrucciones`, ni línea de versión, y su pestaña se llama
  `Sheet`** (TEC-28, medido en los 8 del representante y los 6 de cada hermano): se les crea la hoja `Instrucciones` con el mismo formato que el resto del
  producto, se renombra la pestaña al nombre del checklist (`Legal`, `APPCC`, `Equipamiento`…) y se añade el pie. En **los 111 xlsx**: línea
  `Versión 2.0 · agosto 2026 · aichef.pro/<pid> · info@aichef.pro` (hoy `1.1` en 30 ficheros y **ausente en los 81 restantes**) y **bio anclada**, que **no la
  lleva ninguno** (medido): «Diseñado por John Guerrero — chef y consultor gastronómico desde 2010, en cocina desde los 17 años · johnguerrero.es».
- **1.11 Metadata.** `title` y `subject` → `… · v2.0` en los 111 xlsx. **Y se extiende a los documentos**, que la Fase A no tocó (COM-24): los 22 `.docx` pasan
  de `author='python-docx'`, `comments='generated by python-docx'` y `created=2013-12-23` a `author='AI Chef Pro'` con título y asunto reales; los 8 PDF pasan
  de `title='(anonymous)'`/`'untitled'` y `author='(anonymous)'`/`'anonymous'` a los mismos valores. Se hace en `documentos.py`, no en `motor.py`.
- **1.12 Anchos y cabeceras cortadas** (TEC-22). `escandallo-maestro!A4` («Nombre del plato:», 17 caracteres) está en la columna A con `width=5.0` y
  `B4:D4` combinada a su derecha, así que no puede desbordar; `G4` («Food Cost Objetivo:», 19 caracteres) en columna de `width=14.0` con `H4` ocupada. Se
  combina `A4:B4` para la etiqueta y `C4:D4` como campo, y `G` sube a 22. Barrido general: ninguna etiqueta más larga que su columna con la contigua ocupada.
- **1.13 Lo que el motor NO hace.** No crea ficheros nuevos ni renombra ninguno (§7-bis.1). No toca `paperSize`, márgenes ni pie de impresión (Fase A). No
  escribe `externalLink` entre libros: un `.xlsx` movido de carpeta daría `#REF!` al cliente; la coherencia entre libros se consigue **repitiendo el dato con
  una nota de «de dónde sale»**, no con referencias externas. No toca `aggregateRating`, reseñas, testimonios ni el ancla de precio (§7-bis.8). No borra
  ninguna fila que el cliente pueda haber rellenado.

---

## 2. Grupo A — plantillas financieras (`grupo_a.py`)

Ficheros: `plan-financiero-3-anos.xlsx`, `calculadora-capex.xlsx`, `pl-mensual-escenarios.xlsx`, `calculadora-ticket-medio.xlsx`, `cash-flow-break-even.xlsx`
(las 7 guías de restaurante/panadería) y `calculadora-viabilidad-dark-kitchen.xlsx` (hojas `Inversión Inicial`, `P&L Mensual`, `Punto de Equilibrio`), que ya
calcula y **sólo recibe §1**. Es el grupo que sostiene la frase «10 plantillas Excel con fórmulas» y el que un cliente lleva al banco.

### 2.1 `calculadora-ticket-medio.xlsx` — el simulador que hay que hacer que simule (TEC-01, DOM-08, COM-04)

- **Representante**, hoja `Ticket Medio`, tres escenarios en `B/C/D`, filas: `A5` % menú degustación largo · `A6` precio largo · `A7` % menú corto · `A8` precio
  corto · `A9` % carta · `A10` ticket carta · `A11` % con maridaje · `A12` precio maridaje · `A13` % con copa · `A14` precio copa · `A16` **TICKET MEDIO
  PONDERADO (€)** · `A17` cubiertos/día · `A18` facturación diaria · `A19` días abierto/mes · `A20` facturación mensual. Hoy: **0 fórmulas y 0 valores**, y
  `B16:D20` **pintadas de verde** como si las escribiera el cliente.
  `B16='=B5*B6+B7*B8+B9*B10+B11*B12+B13*B14'` · `B18='=B16*B17'` · `B20='=B18*B19'`, replicado en `C` y `D`; se retira el verde de `16:20`; fila nueva
  `A15` **«% de comensales asignado (debe sumar 100 %)»** `='=B5+B7+B9'` con semáforo rojo si `<>1` (los % de maridaje y copa NO entran: son consumo adicional
  sobre el mismo comensal, y así se dice en la nota de `E15`). Formatos según §1.4.
- **Hermanos** (casual/mexicano/peruano/japonés/nikkei), hoja `Ticket Medio`, **una sola columna `B` con valores precargados** (japonés: `B5=0,7` sashimi,
  `B6=22 €`, `B7=15 €`, `B8=0,25`, `B9=8 €`, `B10=0,5`, `B11=12 €`, `B12=0,55`, `B13=5 €`) y **`A15` «TICKET MEDIO ESTIMADO» sin fórmula y sin valor**: la celda
  que da nombre al fichero está vacía. `B15='=B5*B6+B7+B8*B9+B10*B11+B12*B13'` según el mapa de pares que declare `contenido_<pid>.py` (el par «precio medio
  ramen/principal» de `B7` **no lleva %** porque lo pide el 100 % de los comensales: el módulo marca qué filas son incondicionales). Se añaden debajo
  `Cubiertos/día`, `Días abierto/mes`, `Facturación diaria` y `Facturación mensual`, que hoy no existen en el hermano y sí en el representante.
- La segunda hoja del hermano (`Margen Sake-Whisky`, `Margen Tequilas`, `Margen Piscos`, `Margen Pisco-Sake`, `Menú del Día`) **ya calcula** (`B7='=B5-B6'`,
  `B15='=(B5*B12+B9*B13)*B14'`): sólo recibe §1 y la coherencia de que su facturación de barra sea la misma línea que la del P&L.
- **Demostración pycel exigida**: con el ejemplo precargado, `B16`/`B15` cambia al mover cualquier `%` o cualquier precio; `B20` cambia al mover
  `Días abierto/mes`; con los tres `%` a `0,4/0,4/0,4` la celda de control se pone en rojo.

### 2.2 `pl-mensual-escenarios.xlsx` — de etiquetas y de constantes a un P&L encadenado (TEC-02, DOM-07, COM-05)

- **Variante «una hoja»** (representante), hoja `Escenarios`, `B/C/D` = Pesimista/Realista/Optimista. Parámetros `A6` cubiertos comida · `A7` cubiertos cena ·
  `A8` ticket comida · `A9` ticket cena · `A10` días abierto/mes · `A11` food cost (%) · `A12` coste personal · `A13` alquiler · `A14` otros fijos. Resultados
  `A17`-`A22`. Hoy **0 fórmulas y 0 valores**, con `B17:D22` en verde.
  `B17='=(B6*B8+B7*B9)*B10'` · `B18='=B17*B11'` · `B19='=B17-B18'` · `B20='=SUM(B12:B14)'` · `B21='=B19-B20'` ·
  `B22='=IF(B17=0,"",B21/B17)'` (**`""`, no `0`**: un mes sin una sola venta no tiene un margen del «0,0 %»). Verde sólo en `B6:D14`. Semáforo `ISNUMBER` en
  `B21:D22`. Se precargan los tres escenarios con cifras que el propio producto ya defiende (§7-bis.7).
- **Variante «tres hojas»** (los 5 hermanos): `Pesimista`/`Realista`/`Optimista`, columnas `B Mensual (€)` · `C Anual (€)` · `D % s/Ventas`, con **todo tecleado
  y 0 fórmulas** (japonés `Pesimista`: `B6=33750`, `B10=58500` «TOTAL INGRESOS», `B13=19305` «Food cost (33%)», `B29=50550` «TOTAL COSTES FIJOS», `B31=-12055`
  «EBITDA»). Las líneas de detalle (`B6:B9`, `B14`, `B18:B28`) quedan **verdes con su valor actual como ejemplo**; los totales pasan a fórmula:
  `B10='=SUM(B6:B9)'` · `B13='=B10*$B$<fc>'` con **el food cost en celda verde** (hoy va en el rótulo, «Food cost (33%)», y multiplicado a mano) ·
  `B15='=SUM(B13:B14)'` · `B29='=SUM(B18:B28)'` · `B31='=B10-B15-B29'` · toda la columna `C='=B*12'` · `D='=IF($B$10=0,"",B/$B$10)'`. **`D` no existe hoy** pese
  a estar rotulada.
- **`Pesimista` con EBITDA −12.055 €/mes** (−144.660 €/año) es un escenario que dice al comprador que su negocio pierde 145 k€ al año, y está tecleado, no
  calculado. Se recalibra con el módulo de contenido (§7-bis.7): el pesimista es un escenario **malo**, no **inviable**.
- **Demostración pycel exigida**: cambiar `Cubiertos/día` o una línea de ingreso mueve facturación, food cost, margen, EBITDA y el % s/ventas en cascada, en las
  tres columnas o en las tres hojas; con ingresos a 0 el margen devuelve `""` y el semáforo no pinta.

### 2.3 `plan-financiero-3-anos.xlsx` — la proyección que da nombre al fichero (TEC-07/08/09/10, DOM-06/22/26/27, COM-07)

Hojas actuales: `Instrucciones`, `Inversión` (22 conceptos `A5:A26`, `C27='=SUM(C5:C26)'`, desviación `E5='=IF(C5=0,0,(D5-C5)/C5)'`) y `P&L Mensual`
(`B10='=SUM(B6:B9)'`, `B15`, `B17='=B10-B15'`, `B32='=SUM(B20:B31)'`, `B34='=B17-B32'` bajo la etiqueta `A34='EBITDA'`, `B35='=IF(B10=0,0,B34/B10)'`).
**`Instrucciones!A9` remite literalmente a «la pestaña 'Proyección 3 Años'» que no existe en ninguna de las 7 guías.**

- **2.3.1 Hoja nueva `Proyección 3 Años`** (§7-bis.3). Columnas `B Año 1` · `C Año 2` · `D Año 3`. Año 1 por referencia al P&L mensual (`='P&L Mensual'!B10*12`
  y equivalentes, **nunca constantes**); entradas verdes por año: **crecimiento de ventas (%)**, **inflación de costes (%)**, y el tipo del **Impuesto de
  Sociedades** (25 % por defecto, con la nota de que una entidad de nueva creación tributa al 15 % los dos primeros ejercicios con base positiva). Filas:
  Ingresos · Costes variables · Margen bruto · Costes fijos (sin amortización) · **EBITDA** · Amortización · **EBIT** · Gastos financieros (de `Financiación`) ·
  BAI · IS · **Resultado neto**. Ninguna celda en `0` constante.
- **2.3.2 El EBITDA deja de restar la amortización** (TEC-08, DOM-26, alta). `A30='Amortización equipamiento'` está dentro del bloque que suma `B32`, así que
  `B34` es un **EBIT** rotulado como EBITDA: con ventas 140.000 € y amortización 6.000 €, el R1 midió con pycel `B34=26.000` cuando el EBITDA es 32.000 € (−23 %).
  `B32='=SUM(B20:B29)+B31'`; `B34='=B17-B32'` sigue siendo el EBITDA; se añaden `A36='Amortización'` `='=B30'` y `A37='EBIT (resultado de explotación)'`
  `='=B34-B36'`. La corrección **se replica en la variante de tres hojas** del `pl-mensual` (que rotula `A31='EBITDA'` sin amortización en el bloque: ahí el
  rótulo ya es correcto y sólo hay que dejarlo dicho en la nota).
- **2.3.3 `B35` y `C35`** (TEC-09, TEC-10, DOM-27). `B35` es un ratio con formato `#,##0.00 €` (el cliente lee «0,19 €» donde pone 18,6 %) → `0.0%`. `C35` es el
  arrastre de una columna de una fila de más: divide un porcentaje entre la facturación (`1,33E-06`) → se vacía. Se revisa el mismo arrastre en `C11`, `C16`,
  `C18` y `C33`, que son filas separadoras.
- **2.3.4 Hoja nueva `Financiación`** (DOM-22, alta). Hoy **no hay una sola línea de préstamo, intereses ni servicio de deuda en los 141 ficheros de la
  familia**, y nadie abre un gastronómico de 500-900 k€ con fondos propios: un break-even sin cuota es un break-even falso. Entradas verdes: importe, plazo
  (años), tipo nominal, **carencia**. Cuadro francés por año con la **anualidad algebraica** `importe*i/(1-(1+i)^-n)` (pycel no implementa `PMT`), columnas
  `A Año` · `B Capital inicial` · `C Cuota` · `D Intereses` · `E Amortización` · `F Capital pendiente`. Dos guardas heredadas del kit plan-financiero, que allí
  se pagaron caras: **la carencia que iguala o supera el plazo devuelve el aviso «La carencia no puede igualar ni superar el plazo»** en `C` (texto) dejando
  `B`, `D` y `F` **numéricas** —de `D` salen los intereses del P&L y de `F` el encadenado del año siguiente, así que un texto ahí propagaría `#¡VALOR!`—, y **el
  cuadro se apaga pasado el vencimiento** (`si año > plazo`, cuota, intereses y amortización a `0` numérico), o el capital pendiente se vuelve negativo.
  Los intereses alimentan `Proyección 3 Años`; la cuota alimenta el cash flow (§2.4).
- **2.3.5 Fondo de maniobra dimensionado, no tecleado** (DOM-01, COM-30, alta). `Inversión!B26` se llama «Fondo de maniobra (6 meses)», `calculadora-capex!B15`
  igual y la tabla del docx dice «(3-6 meses)»: tres rótulos para la misma partida, y las cifras (60.000 / 120.000 / 200.000 €) no cubren **ni cuatro meses** de
  la nómina más barata que describe el propio libro. `C26` pasa a **fórmula**: `= (coste fijo mensual + coste variable estimado del mes) × meses`, con **meses
  en celda verde** y un mínimo de **6** («≥ 6 meses de costes fijos + personal, según la propia tabla del libro», §7-bis.3), leyendo el coste de personal de la
  hoja `Turnos` (§4.4) y el resto del `P&L Mensual`. El rótulo queda igual en los tres sitios.
- **2.3.6 Fuente única de CAPEX** (TEC-26, COM-32). Dos desgloses irreconciliables: `plan-financiero!'Inversión'` con **22 conceptos** (`Equipamiento cocina
  caliente` + `cocina fría` + `Pastelería y obrador` + `Zona de pase` + `Plonge` + `Almacenamiento` por separado) y `calculadora-capex!CAPEX` con **12
  categorías** y rangos bajo/medio/alto (`C17/D17/E17` = 373.000 / 703.000 / 1.275.000 €). No se fusionan los libros (§7). `calculadora-capex` queda como **hoja
  de rangos de mercado** y `plan-financiero!'Inversión'` como **«Mi CAPEX»**, cada una con la línea «de dónde sale este dato» en `Instrucciones` y una tabla de
  correspondencia 22→12 en la propia hoja, para que los dos totales sean comparables aunque el cliente rellene uno solo.
- **Demostración pycel exigida**: `Proyección 3 Años` responde a los dos % de entrada y el Año 1 sigue al P&L; el EBITDA con amortización 6.000 € da 32.000 € y
  el EBIT 26.000 €; `B35` en `0.0%`; el cuadro francés con 100.000 € al 5 % en 60 meses da **1.887,12 €/mes** (valor de control ya verificado en la familia);
  con plazo 3 y carencia 3 los años 4-5 quedan a 0 y el capital pendiente final es 0.

### 2.4 `cash-flow-break-even.xlsx` — el break-even que no existe en ninguna guía (TEC-03, DOM-09, COM-06)

- **Representante**, hoja `Cash Flow 12 Meses` (`B:M` meses, `N` total): las filas `A10 Total Ingresos`, `A19 Total Gastos`, `A21 FLUJO DE CAJA NETO` y
  `A22 FLUJO ACUMULADO` están **sin fórmula, sin relleno y en formato General**; las únicas 10 fórmulas son `N6:N9` y `N13:N18`.
  `B10='=SUM(B6:B9)'` → `B10:N10`; `B19='=SUM(B13:B18)'` → `B19:N19`; `B21='=B10-B19'`; `B22='=B21'` y `C22='=B22+C21'` arrastrado hasta `M22`.
- **Hermanos**, hoja `Cash Flow` (`A5` saldo inicial · `A8:A11` entradas · `A12` total entradas · `A15:A23` salidas · `A24` total salidas · `A26` flujo neto ·
  `A27` saldo acumulado): **`B5:M27` está entera en blanco**. Mismas fórmulas, más `B5` (saldo inicial, verde) y `C5='=B27'` encadenando el mes anterior.
- **El break-even, en las dos variantes.** Bloque nuevo (o, en los hermanos, la hoja `Break-Even` que ya existe con `B11='=B5*B6*B7'` y `B12='=B11*(1-B8)'` y
  deja **`B13` «Break-Even (meses)» vacía**): costes fijos mensuales · margen de contribución (%) · **umbral de ventas** `=IFERROR(CF/MC,"")` · **cubiertos/día
  necesarios** · y **mes de break-even** `=IFERROR(MATCH(TRUE,INDEX(B22:M22>0,0),0),"No alcanzado")` (verificado en pycel: devuelve `4` sobre una serie que cruza
  a positivo en el cuarto mes). `B6` («Comensales/día») y `B7` («Días abierto/mes») dejan de ir en `#,##0.00 €`.
- **Las tres filas de IVA** (DOM-03): `IVA repercutido`, `IVA soportado` y `Liquidación (modelo 303, trimestral)` con el calendario de la AEAT, porque el cash
  flow va **con IVA** y porque el IVA soportado del CAPEX (105-189 k€ sobre una inversión de 500-900 k€) es tesorería adelantada que hoy no aparece por ningún
  lado. Y **la cuota del préstamo** de §2.3.4 como fila de salida.
- **Demostración pycel exigida**: el acumulado encadena mes a mes; con la serie de ejemplo el mes de break-even es el que cruza a positivo y con una serie
  siempre negativa devuelve `"No alcanzado"` (y no `#N/A`); el umbral de ventas con margen de contribución 0 devuelve `""`, no `#¡DIV/0!`.

### 2.5 Defectos que el R1 NO podía ver (sólo existen en los hermanos) — medidos el 2026-08-29

El R1 auditó el representante. El censo de familia ha encontrado **dos defectos nuevos, los dos en el fichero que se vende para llevarlo al banco**. Se numeran
`NUEVO-01` y `NUEVO-02` y entran en el alcance de la v2.0 con el mismo rango que los del R1.

- **NUEVO-01 (alta) — el `P&L Mensual` de los 5 hermanos no tiene NI UN total.** En `plan-financiero-3-anos.xlsx`!`'P&L Mensual'` de casual, mexicano, peruano,
  japonés y nikkei, las filas `A10 TOTAL INGRESOS`, `A13 Food cost (33%)`, `A15 TOTAL COSTES VARIABLES`, `A29 TOTAL COSTES FIJOS`, `A31 EBITDA` y `A32 % EBITDA`
  están **vacías en las 13 columnas `B:N`**. Las 41-65 fórmulas del libro son los `SUM` horizontales de las líneas de detalle (`N6='=SUM(B6:M6)'`) y las de la
  hoja `Inversión`. Es **peor que el representante**, que al menos tiene `B10`, `B15`, `B17`, `B32` y `B34`. Se resuelve con las mismas fórmulas de §2.3
  adaptadas al mapa de filas de cada hermano, que aporta `contenido_<pid>.py`.
- **NUEVO-02 (alta) — el plan a 3 años de panadería imprime un EBITDA igual a la facturación.** `plan-financiero-3-anos.xlsx`!`'P&L 3 años'` encadena **tres
  errores** en un libro de 21 fórmulas, y los valores cacheados son los que el cliente ve al abrirlo:
  1. `B23` («TOTAL COSTES») `='=SUM(B12:B20)+SUM(B14:B16)'` — **suma dos veces `B14:B16`** (ya contenido en `B12:B20`) y **omite `B21`** («Seguros + tasas +
     amortización»). Cacheado: **368.900 €** cuando la suma correcta `SUM(B12:B21)` son **251.600 €**.
  2. `B24` («EBITDA») `='=B9-B22'` — **la fila 22 no existe** (está vacía entre `A21` y `A23`), así que resta cero. Cacheado: **300.000 €, exactamente la
     FACTURACIÓN TOTAL de `B9`**. El EBITDA correcto es **48.400 €**.
  3. `B25` («Margen EBITDA %») `='=B23/B9'` — divide el **total de costes** entre la facturación. Cacheado: **122,97 %**, junto a una nota que dice «15-22 %
     objetivo». El margen correcto es **16,1 %**, que es justo lo que la nota anuncia.
  Corrección: `B23='=SUM(B12:B21)'`, `B24='=B9-B23'`, `B25='=IFERROR(B24/B9,"")'`, replicado en `C` y `D`, y **etiquetar los tres años como valores de ejemplo**
  (§1.2). Con la corrección los tres años dan 16,1 % / 15,6 % / 14,0 % de margen, dentro del rango que la propia hoja declara — lo que confirma que las cifras
  base eran correctas y sólo estaban mal sumadas.

**Lectura**: un R1 sobre un solo producto no basta para una familia de 8 con generadores copy-pasteados. Por eso §9 exige que los hermanos no se traten como
«aplicar lo del representante», sino como **verificación id a id más censo propio**.

---

## 3. Grupo B — checklists y cronograma (`grupo_b.py`)

Ficheros: los **8 checklists** del representante, los **6** de cada hermano, los **6** de panadería (molde B) y los **2** de dark-kitchen (molde C), más
`cronograma-apertura-gantt.xlsx` (7 guías). Es el grupo donde vive la **exposición jurídica** del producto: un checklist legal caducado no es un defecto
cosmético, es una instrucción errónea que el cliente ejecuta.

### 3.1 Legal y laboral vigentes (DOM-12, DOM-38, COM-15, alta) — `contenido_<pid>.py` aporta las filas, el motor las inserta

- **Fuera el «Libro de visitas de la Inspección de Trabajo»** (representante `checklist-legal!` fila 37, categoría `Laboral`, responsable «Papelería», 20 €).
  Suprimido por la Ley 23/2015 y la Orden ESS/1452/2016: desde entonces el inspector extiende diligencia y no hay libro que comprar ni conservar. Se **sustituye**
  (no se borra dejando hueco) por **«Registro diario de jornada (RD-ley 8/2019, art. 34.9 ET): sistema de fichaje y conservación 4 años»**, que hoy **no está en
  ninguna de las 40 filas** y es de las infracciones más sancionadas en hostelería.
- **Filas nuevas obligatorias en todas las guías**, sin umbral de plantilla: **Registro retributivo (RD 902/2020)** y **Protocolo de prevención del acoso sexual
  (LO 3/2007 art. 48)**. Y **«Comunicación de apertura del centro de trabajo a la autoridad laboral»**.
- **`checklist-contratacion!` fila 30**: «Plan de igualdad (si >50 empleados)» → **«(50 o más personas trabajadoras)»**; el `>50` deja fuera justo a la empresa
  de 50. **Fila 16**: «Cláusula de confidencialidad y no competencia (chef)» → **«Pacto de no competencia postcontractual CON compensación económica pactada
  (art. 21.2 ET; máx. 2 años para técnicos)»**: sin compensación el pacto es nulo y el cliente cree tener una protección que no tiene.
- **Ningún puesto por debajo del SMI** (DOM-13, §7-bis.5). La familia no fija hoy el SMI en ninguna celda y las guías hermanas heredarán el mismo problema:
  se crea en `plantilla-turnos-brigada` (§4.4) una celda verde **«SMI vigente (€/año, 14 pagas)»** con el **último valor conocido y su año en la nota**, más la
  línea «el mínimo lo fija el **convenio provincial de hostelería**, que prevalece sobre el SMI». Toda tabla de salarios del docx (§5) se recalcula contra esa
  celda, y **ninguna cifra por debajo**. No se inventa un importe: si el módulo de contenido no trae el valor con fuente, la celda queda vacía y el gate lo marca.
- **Licencias por tipo genérico** (DOM-11, COM-28). «Licencia C3» se presenta como requisito nacional en el cap. 5, se repite en el cap. 7 («Sin esto, no hay
  licencia C3»), en `checklist-legal` y en `cronograma-apertura-gantt!A13`; es nomenclatura municipal (catálogo de la Comunidad de Madrid) y en Cataluña,
  Andalucía o Valencia ese epígrafe no existe. Redacción única en los cuatro sitios: **«licencia de actividad clasificada de restaurante — la clasificación y el
  nombre dependen de la ordenanza municipal y del catálogo autonómico; en algunos municipios se denomina C3»**, y **se elimina la coletilla «cocina separada
  físicamente del comedor»**, que contradice el modelo de cocina abierta que el propio producto vende (cap. 3 Modelo 3, cap. 22 y `checklist-diseno-sala` fila
  8, «barra/counter 8.000 €»). **CIRCE deja de atribuirse a Andalucía**: es la plataforma estatal del DUE para constituir la sociedad, no un sistema autonómico
  de licencias.
- **Bloque «Local» nuevo en `checklist-legal`** (DOM-23, alta): las cadenas «arrendamiento», «fianza», «traspaso» y «carencia» **no aparecen en ninguno de los
  141 ficheros**, y con una licencia de 4-8 meses por delante eso son medio año de renta sobre un local cerrado. Filas: informe de compatibilidad urbanística
  **antes de firmar** · contrato de arrendamiento para uso distinto de vivienda (duración, prórrogas, renta, actualización) · fianza legal de 2 mensualidades y
  garantía adicional · **carencia de renta durante obra y licencia** · cláusula de cesión y traspaso · **condición suspensiva por denegación de licencia**.

### 3.2 Sanitario vigente (DOM-14, DOM-15, alta)

- **Anisakis**: la cadena no aparece en ninguno de los 141 ficheros, y el producto sitúa ceviches y tartares en el cuarto frío (cap. 8) y promociona los crudos
  (cap. 22) — en las guías japonesa, nikkei y peruana el riesgo es aún más directo. Filas nuevas en el bloque `Temperaturas` de `checklist-appcc`: **«Congelación
  preventiva (−20 °C durante al menos 24 h en todo el producto, o −35 °C / 15 h) para pescado de consumo en crudo, marinado, escabechado o en salazón — RD
  1021/2022, art. 8.1 (que derogó el RD 1420/2006) y Rgto. (CE) 853/2004, Anexo III, Secc. VIII, Cap. III.D»**, **«Registro de lotes
  congelados preventivamente»** e **«Información al consumidor de que el pescado ha sido congelado»**.
- **Cocción a baja temperatura y envasado al vacío**: el `checklist-equipamiento` presupuesta envasadora (2.500 €) y roner (1.500 €) y el bloque `PCC` del APPCC
  tiene cuatro líneas genéricas sin un solo binomio tiempo-temperatura. Bloque nuevo: tabla de binomios validados por producto · registro de sonda por lote ·
  **enfriamiento a ≤10 °C en menos de 2 h tras cocción prolongada** · etiquetado con vida útil justificada · validación documental del proceso. Es lo primero
  que pide un inspector en una cocina con roner.

### 3.3 El motor sobre los tres moldes

- **Molde A** (14 ficheros: 8 del representante + 6 por hermano ×5): hoja `Instrucciones` nueva, pestaña renombrada, línea de versión y bio (§1.10); fila
  `TOTAL` con `SUM(G)` y subtotales por categoría con `SUMIF(B)`; `% completado` con `COUNTIF`; `E` (`Fecha Límite`) a `dd/mm/yyyy` con DV de fecha; **formato
  condicional por texto exacto** sobre `F` (`Completado` verde `C6EFCE`, `En Curso` ámbar `FFEB9C`, `Pendiente` gris) — hoy `ws.conditional_formatting` está
  **vacío en los 141 libros**.
- **Molde B** (6 ficheros de panadería): el contador `C36='=COUNTIF(A4:A34,"✓")'` / `E36='=COUNTIF(B4:B34,"?*")'` **ya existe y se respeta**; se añade la línea
  de versión y la bio (no las lleva), la hoja `Instrucciones` (no la lleva) y la protección. **No se le añade columna de coste** salvo que John lo pida (§7.1):
  el molde no la tiene y añadirla obligaría a inventar 200 importes.
- **Molde C** (**1** fichero de dark-kitchen, `checklist-equipamiento-obra.xlsx`): **ya trae `G5='=IF(E5=0,"",((F5-E5)/E5))'` y la fila TOTAL
  `F40='=SUM(F5:F39)'`**. No se duplica el total; se le añade `% completado`, el semáforo de desviación (`ISNUMBER`, rojo por encima del umbral en celda) y §1.
- **Molde D** (**1** fichero de dark-kitchen, `checklist-apertura-legal.xlsx`): **cabecera en la fila 4** con `F='Coste Estimado (€)'` y `G='Estado'` —el molde
  A pone el coste en `G` y el estado en `F`, así que las dos columnas están **cruzadas** respecto de él, y aplicarle el molde A sumaría la columna de estados—.
  Como el C, **trae su propia fila TOTAL** y no se duplica; sí lleva categoría y coste, así que **sí recibe el desglose por categorías** (RT-28: la condición
  del subtotal es «hay columna de categoría y de coste», no «el molde es A»). Existía en `motor.molde_checklist()` desde T1 y la SPEC no lo recogía: quedaba
  como un molde vivo que, leyendo sólo la SPEC, parecía un fallo de detección.

  **Un TOTAL a `None` NO es un gate verde.** Como los moldes C y D no escriben `TOTAL PRESUPUESTADO (€)` —el libro ya tiene el suyo—, la demostración de
  `main.py` no encontraba ninguna fila TOTAL, devolvía `total=None` y `cuadra=None` y **no lo contaba como fallo**: nadie comprobaba que el total del libro
  cuadrase con la suma de los subtotales por categoría. `demo_checklists()` busca ahora también el **TOTAL nativo** del libro y exige que evalúe a número y que
  cuadre; **el único molde que puede quedarse sin TOTAL es el B**, y porque la SPEC declara explícitamente que no tiene columna de coste (§7-bis.17).

### 3.4 Contenido que falta en los checklists, por fichero (DOM-20, DOM-21, DOM-39, DOM-40, COM-17, COM-18, COM-34)

Los recuentos **medidos** (censo 2026-08-29) frente a lo que promete el dashboard del representante: `equipamiento-cocina` **54** vs «90 ítems» (−40 %, la mayor
desviación del pack) · `appcc` **45** vs «55» · `vajilla-cristaleria` **43** vs «50» · `inspeccion-michelin-repsol` **40** vs «45» (cifra repetida **tres veces**
en la venta: tarjeta, BONUS 3 y FAQ) · `diseno-sala` **31** vs «35» · `marketing-preapertura` **30** vs «35» · `legal` **40** vs «40» ✅ · `contratacion` **30**
vs «30» ✅. Se **completa el contenido**, no se baja el número (§7-bis, y es más barato que tocar seis textos de venta), y **con ítems que hoy faltan y son
obligatorios**, no con relleno:

- `checklist-equipamiento-cocina`: **horno mixto 10 GN (Rational o equivalente), 17.500 €** —el equipo nº 1 de la tabla 1 del propio libro, **ausente de las 54
  filas**— · conducto de extracción hasta cubierta + ventilador + silenciador (12.000-30.000 €) · aportación de aire (3.000-6.000 €) · **sistema automático de
  extinción en campana** (2.500-4.000 €, exigido por la aseguradora y por el CTE DB-SI con freidora) · instalación, transporte y puesta en marcha (12 %). Hoy la
  extracción entera está presupuestada en **2.500 €** (fila 35) siendo lo que el propio cap. 5 llama «obstáculo técnico número 1». Y **`Thermomix` y `Pacojet`,
  que la tarjeta del capítulo 9 nombra como gancho, no aparecen en ninguno de los 141 ficheros** (COM-23).
- `checklist-diseno-sala`: **limitador-registrador acústico homologado + estudio de impacto acústico** · alumbrado de emergencia y señalización de evacuación
  (CTE DB-SUA/SI) · **aseos y vestuarios de personal separados (RD 486/1997)** para 22-30 trabajadores · certificación de aforo y anchura de recorridos de
  evacuación. Las cadenas «limitador», «vestuario» y «extinción» **no aparecen en ningún fichero de la familia**.
- `checklist-vajilla-cristaleria` (DOM-21): la dotación (300 copas de vino, ~560 piezas) está calculada para servicio de carta, no para el menú degustación con
  maridaje que el producto vende (5-7 copas por comensal × 65 plazas = 325-455 copas **en un solo servicio**, sin margen de lavado). Se añade una **segunda
  columna «Menú degustación»** con la regla explícita `piezas = plazas × pases × 1,5 de rotación de lavado`, en vez de cambiar la dotación de carta.
- `checklist-inspeccion-michelin-repsol` (COM-34): la categoría `Reputación` —«Invitaciones estratégicas a críticos y periodistas, 3.000 €» (fila 38) y
  «Participación en eventos gastronómicos, 5.000 €» (fila 35)— se separa a un bloque rotulado **«Prensa y notoriedad (NO influye en la inspección)»**, porque
  contigua a ítems de estrella sugiere lo que el propio cap. 17 niega. Se añade el bloque de **Estrella Verde** (DOM-36).
- `checklist-marketing-preapertura`: «Sesión de fotos profesional de platos (15-25 platos) | 500 €» sube a **1.500-3.000 €**, que es el precio real y el
  coherente con el propio rango de lanzamiento de 5.000-30.000 € del libro. **Resy fuera** (DOM-35): no opera en España y es la única cifra en dólares de todo
  el producto («300-500 USD/mes»); se sustituye por Tock, TheFork, Cover Manager o Restoo con precios en euros, aquí y en el cap. 21.
- `checklist-legal`: además de §3.1, los ítems que suben el recuento hasta 45 salen del bloque «Local» y del laboral, no de relleno.

### 3.5 `cronograma-apertura-gantt.xlsx` (TEC-14, TEC-15, DOM-37, COM-19)

Hoja `Gantt`: `A4` Fase/Tarea · `B4` Responsable · `C4` Estado (DV) · `D4` Inicio · `E4` Fin · `F4:W4` = `M1`…`M18`. Hoy **`F5:W34` está completamente vacío**
(y **ni siquiera marcado como editable**: el verde llega sólo hasta `E`), `B`, `D` y `E` vacías en las 24 tareas, y `Instrucciones!A5` promete «cada fase tiene
una barra de duración estimada». La landing lo vende como BONUS 4 (24 EUR) con «todas las fases y dependencias».

- Columnas nuevas `Mes inicio` y `Duración (meses)` (verdes, numéricas) y **la barra se pinta con formato condicional** `=AND(ISNUMBER($<inicio>6),F$4>=$<inicio>6,F$4<$<inicio>6+$<dur>6)`
  sobre `F6:W34`, precargadas con la duración que el propio libro ya conoce (licencia 4-8 meses, obra, formación 2-4 semanas). Así la barra sigue al dato en vez
  de ser un sombreado muerto.
- Columna **`Depende de`** (el «dependencias» que promete el bonus y que hoy no existe en ninguna celda).
- `D`/`E` a `dd/mm/yyyy` con DV de fecha y columna **`Días`** `='=E6-D6'`.
- **Tareas nuevas en la Fase 1**: «Negociación y firma del arrendamiento (con carencia)» y «Preparación del dossier bancario / Negociación de financiación /
  Firma y disposición» — hoy el Gantt no tiene ninguna tarea de financiación ni de contrato, que son las dos que marcan cuándo empieza a correr la renta.
- **Demostración pycel/openpyxl exigida**: cambiar `Mes inicio` mueve la barra (se comprueba la regla de CF, no el píxel); `Días` responde a las dos fechas; el
  fichero abre sin avisos en LibreOffice tras `inject_cache`.

---

## 4. Grupo C — cocina, carta y sala (`grupo_c.py`)

Ficheros: `escandallo-maestro[-<concepto>].xlsx` (8 guías, dos modelos), `menu-engineering-matrix.xlsx` (6 guías), `budget-bodega.xlsx` (sólo representante),
`plantilla-turnos-brigada.xlsx` (7 guías) y `plan-fermentacion-y-produccion.xlsx` (sólo panadería, hoy con **0 fórmulas**).

### 4.1 `escandallo-maestro` — la herramienta de precios (TEC-05/06/21/22/23, DOM-04/05/30, COM-14/33)

**Modelo del representante**, hoja `Escandallo`: `A4` «Nombre del plato:» · `E4` «Raciones:» · `G4` «Food Cost Objetivo:» · `H4` `'28%'` **(cadena de texto, con
relleno verde)**; tabla `A6:I6` = `# · Ingrediente · Unidad · Cantidad Bruta · Precio/Ud (€) · Merma (%) · Cantidad Neta · Coste (€) · Notas`;
`G7='=D7*(1-F7)'` y `H7='=D7*E7'`; `H27='=SUM(H7:H26)'`; `H28='=H27/0.28'` con el rótulo `G28='PVP Sugerido (28%):'`.

- **La merma entra en el coste** (DOM-04, alta). Hoy `H` no referencia nunca ni a `G` ni a `F`: la columna de merma es **decorativa**. Con merluza a 22 €/kg,
  0,180 kg y 40 % de merma, la hoja da 3,96 € cuando servir 180 g netos cuesta `0,180/0,6 × 22 = 6,60 €` — **+67 % en la partida de pescado**. Se invierte el
  sentido, que es como se escribe una ficha técnica: `D` pasa a **«Cantidad NETA (ración)»**, `G` a **«Cantidad BRUTA a comprar»**
  `='=IFERROR(IF(F7>=1,"",D7/(1-F7)),"")'` y `H7='=IFERROR(G7*E7,"")'`. DV decimal `0 ≤ F ≤ 0,95` (hoy `F` va en formato `General` **sin validación**: teclear
  `20` bajo un encabezado que dice `%` produce **cantidad neta −9,5** sin un solo aviso) y `E` a `#,##0.00 €`.
- **El PVP divide por raciones** (TEC-05, DOM-05, alta). `E4` es una etiqueta huérfana que **ninguna fórmula lee**: una ficha de fondo oscuro de 10 raciones con
  60 € de coste propone **214,29 €** por plato en lugar de 21,43 €. `E4` queda como etiqueta y `F4` como celda de entrada numérica (por defecto `1`); fila nueva
  **«Coste por ración»** `='=IFERROR(H27/$F$4,"")'` — que es además el dato que alimenta el menu engineering (§4.2).
- **El food cost objetivo se usa** (TEC-21, DOM-30). `H4` pasa de la **cadena** `'28%'` a **número** `0,28` con formato `0%`, y
  `H28='=IFERROR(H27/$F$4/$H$4,"")'`. El rótulo deja de fijar el porcentaje: `G28='="PVP sugerido ("&TEXT($H$4,"0%")&"), sin IVA:"'`. Un restaurante que trabaje
  al 32 % —el propio cap. 3 dice «food cost 28-32 %»— hoy escribe 32 en `H4` y sigue viendo el PVP calculado al 28 %, un 14 % por encima del que busca.
- **IVA** (§1.5, DOM-03): filas `PVP sin IVA` y `PVP con IVA` `= sin IVA × (1+tipo)` con el tipo en celda. En España el precio de carta se muestra con IVA
  incluido: aplicar el resultado actual literalmente deja el food cost real en ~30,8 % en vez del 28 % objetivo.
- **Modelo de los hermanos**, hoja `Escandallo`: `C` cantidad (g/ml) · `D` precio/kg · `E='=(C6/1000)*D6'` · `F` merma · `G='=E6*(1+F6)'` · `G18='=SUM(G6:G16)'`
  · `G19='=G18/0.33'` · `G20='=G19*1.10'`. Aquí la merma **sí** entra, pero como **recargo**: con 20 % da `×1,20` cuando lo correcto es `/(1-0,20) = ×1,25`
  (−4 % de coste en cada línea, y −20 % con mermas del 40 % de pescado). `G6='=IFERROR(IF(F6>=1,"",E6/(1-F6)),"")'`. El food cost sale del rótulo a **celda
  verde** (`G19='=IFERROR(G18/$<fc>,"")'`) y el `1.10` del IVA sale de la fórmula a **celda verde** (`G20='=G19*(1+$<iva>)'`).
- **Una ficha, sin plantilla que duplicar** (TEC-23). Un menú degustación tiene 15-25 elaboraciones y el libro contiene **una sola ficha**. La hoja se renombra
  **`Ficha (plantilla)`** y `Instrucciones` gana el paso «clic derecho sobre la pestaña → Mover o copiar → Crear una copia, y renómbrala con el nombre del
  plato»; se añade una hoja **`Resumen`** que consolida coste por ración y PVP de cada ficha, con la nota de cómo extenderla.
- **Demostración pycel exigida**: `H27`/`G18` cambia al mover la merma; con `F4=10` y coste 60 € el PVP baja de 214,29 € a 21,43 €; con `H4=0,32` el PVP cambia;
  con `F7=20` (mal tecleado) la DV lo impide y la fórmula devuelve `""`, no un negativo.

### 4.2 `menu-engineering-matrix` — Kasavana & Smith completo (TEC-04, TEC-24, DOM-10, COM-08)

- **Representante**, hoja `Menu Engineering`, `A4:H4` = `# · Plato · Categoría · Uds Vendidas · Coste (€) · PVP (€) · Margen (€) · Clasificación`, filas 5-29.
  Las **25 fórmulas del libro son 25 restas** `G5='=F5-E5'`; `H5:H29` vacía; **no hay ninguna fila de totales** (`max_row=29`) y **no hay ni una fila de
  ejemplo**. `D5:D29` va en `#,##0.00 €`: 120 unidades se pintan «120,00 €».
- **Hermanos**, hoja `Matrix`, `A4:J4` = `# · Plato · PVP (€) · Food Cost (€) · % Food Cost · Uds. Vendidas/Mes · Margen Unit. (€) · Margen Total (€) ·
  Popularidad · Clasificación`, 15 platos reales con `E='=D/C'`, `G='=C-D'` y `H='=G*F'` calculadas, y **`I` y `J` vacías en las 15 filas**.
- Se implementa el método completo, en las dos variantes:
  - fila de totales: `<uds>_total='=SUM(<uds>)'` y **margen de contribución medio ponderado** `='=IFERROR(SUMPRODUCT(<uds>,<margen>)/<uds>_total,"")'`;
  - columna **mix %** `='=IFERROR(<uds>/<uds>_total,"")'` (es la columna `I` «Popularidad» que los hermanos ya tienen rotulada y vacía);
  - **umbral de popularidad** en celda: `='=IFERROR(0.7/COUNTIF(<uds>,">0"),"")'` (el 70 %/N clásico; `COUNTA` no existe en pycel, por eso `COUNTIF`);
  - clasificación `='=IF(<uds>="","",IF(AND(<mix>>=$<umbral>,<margen>>=$<mc_medio>),"Star",IF(AND(<mix>>=$<umbral>,<margen><$<mc_medio>),"Plowhorse",
    IF(AND(<mix><$<umbral>,<margen>>=$<mc_medio>),"Puzzle","Dog"))))`;
  - columna **«Acción recomendada»** por cuadrante (mantener y destacar / subir precio o bajar coste / promocionar y reubicar en carta / retirar o rediseñar),
    que es lo que la landing llama «recomendaciones de pricing y carta al instante»;
  - formato condicional por texto sobre la clasificación.
- **Al representante hay que precargarle 12-15 platos de ejemplo** (hoy no tiene ninguno) coherentes con la carta que describe el cap. 15; el módulo de
  contenido los aporta.
- **Verificado en pycel hoy** con 5 platos (140/220/60/130/180 uds y márgenes 23,5/4,7/10,0/9,8/10,2 €): total 730 uds, MC medio ponderado **11,0055 €**, umbral
  **0,14**, mix del plato 1 **0,1918** → clasificación **`Star`**. La cadena completa evalúa sin `#N/A`.

### 4.3 `budget-bodega` — sólo en el representante (TEC-18/19/20, DOM-28, COM-22)

Hoja `Bodega`, 50 referencias `A5:A54`. Las **100 fórmulas** del libro son `G='=F5-E5'` y `H='=IF(E5=0,0,(F5-E5)/E5)'`.

- **`H` es un markup, no un margen**: con coste 10 € y PVP 30 € imprime «200,0 %», un número imposible como margen y no comparable con el food cost de bebida
  del 28-40 % que enseña el cap. 12. `H4` se rotula **«Multiplicador (×)»** `='=IFERROR(F5/E5,"")'` y se añade **«Margen s/PVP (%)»** `='=IFERROR((F5-E5)/F5,"")'`
  y **«Food cost bebida (%)»** `='=IFERROR(E5/F5,"")'`, que es el que se contrasta con el capítulo.
- **`J` «Rotación/Mes» es una celda verde vacía** pese a que `Instrucciones!A6` dice que se calcula: se añade columna **«Uds vendidas/mes»** y
  `J='=IFERROR(<vendidas>/I5,"")'` sobre el stock.
- **Un «Budget de Bodega» que no valora la bodega**: no hay fila de totales (`max_row=54`) ni ninguna fórmula que cruce `E` (coste) con `I` (stock). Columnas
  **«Valor stock a coste»** `='=E5*I5'` y **«Valor stock a PVP»** `='=F5*I5'`, y fila **TOTAL** con `SUM` de las tres y el margen medio ponderado. Es el número
  que alimenta la partida `Bodega inicial (vinos)` de `plan-financiero!'Inversión'!B17`, hoy sin ninguna relación con este libro.
- Columnas que un sommelier espera y no están: **formato, añada, proveedor y ubicación/bin**.

### 4.4 `plantilla-turnos-brigada` — horas, coste y registro de jornada (TEC-11/12/13, DOM-02/13/16, COM-10/20/21)

Hoja `Turnos Semana`: `A4:K4` = `# · Nombre · Puesto · Lun · Mar · Mié · Jue · Vie · Sáb · Dom · Horas/Semana`; puestos en `C6:C20` (15 de cocina) y `C22:C30`
(9 de sala); DV `"M,T,P,L,V"` sobre `D6:J30`. **0 fórmulas en el libro** y **ninguna columna de coste**, pese a `Instrucciones!A7` («las horas y costes se
calculan automáticamente») y a la tarjeta del dashboard («cuadrante semanal para 25 personas con coste»).

- Tabla de equivalencia **turno → horas** en celdas verdes (`M`=8, `T`=8, `P`=10, `L`=0, `V`=0), documentada en `Instrucciones` — hoy la DV ofrece una **`V` que
  las instrucciones no explican** (TEC-12): se documenta como **Vacaciones**, no se retira.
- `K6='=SUMPRODUCT((D6:J6="M")*$<h_M>+(D6:J6="T")*$<h_T>+(D6:J6="P")*$<h_P>)'` y columnas nuevas **`Bruto anual (€)`**, **`Nº de pagas`** (DV 12/14/15, por
  defecto 14), **`Coste/hora`** y **`Coste semana`** `='=K6*<coste_hora>'`, con fila de **total de coste de brigada**.
- **La Seguridad Social va en celda, no en el rótulo** (DOM-02, COM-10, alta). Celda verde **«Tipo de SS a cargo de la empresa (%) = 33 %»** con la nota
  «ajústalo a tu CNAE, contrato y convenio: un indefinido general ronda el 33-34 % sumando contingencias comunes, desempleo, AT/EP, FOGASA, FP y MEI» — el mismo
  criterio ya firmado en `kit-gestion-personal-v2-SPEC.md`. El libro declara hoy «250.000-450.000 € (incluyendo SS empresa ~30 %)» y **es el bruto sin SS**:
  sumando su propia tabla salen 322.400-601.900 € en cocina y 234.000-403.000 € en sala. Con esta columna el cliente lo ve, y la cifra alimenta §2.3.5 y §5.
- **Celda «SMI vigente (€/año, 14 pagas)»** (§3.1) y semáforo rojo `ISNUMBER` en todo bruto anual por debajo de ella: dos puestos del cap. 13 («Ayudante de
  cocina 16.000-19.000 €», «Plonge 15.000-17.000 €») están por debajo del mínimo legal y el producto los publica como rango de planificación.
- **Hoja nueva `Registro de jornada`** (DOM-16, alta): fecha · trabajador · hora de entrada · hora de salida · horas del día (`MOD` envuelto en `ROUND(...,2)`
  para el cruce de medianoche) · firma. Un cuadrante con letras M/T/P/L en siete columnas **no cumple el art. 34.9 ET**, y el propio `checklist-contratacion`
  fila 29 lo exige («Registro de jornada digital (obligatorio) | 100 €»). Alertas de **descanso mínimo de 12 h entre jornadas (art. 34.3 ET)** y de más de 40 h
  semanales, críticas con turno partido y dos servicios.
- **El headcount, una sola cifra** (TEC-13, COM-21). Hay **cuatro** en el mismo producto: las tablas del docx suman 21-29, el texto del cap. 14 dice «22-30»,
  el cuadrante tiene **24** puestos y `Instrucciones!A1` y el dashboard dicen **«25 personas»**. Manda la suma de las tablas (§7-bis.7): se corrige el título del
  xlsx, el texto del capítulo y la tarjeta del dashboard, y se numera la columna `A6:A30`, hoy vacía mientras el resto de plantillas del producto sí numera.
- **Demostración pycel exigida**: `K` responde al cambio de un turno; el coste semanal responde al coste/hora y al tipo de SS; un bruto por debajo del SMI
  dispara el semáforo; dos jornadas a menos de 12 h disparan la alerta.

### 4.5 `plan-fermentacion-y-produccion` (sólo panadería)

Hoy **0 fórmulas** en la hoja `Plan fermentación` (18×9). El módulo de contenido de panadería define los cálculos que faltan (tiempos por temperatura de masa,
kg de masa madre por hornada, escalado por unidades) y el gate exige que la hoja calcule algo. Si el módulo no los aporta, el fichero **sólo recibe §1** y su
promesa se ajusta en la landing (§6): no se inventa una fermentación.

---

## 5. Documentos — la guía y los dos bonus (`documentos.py` + `guion_<pid>.py`)

Es el bloque de más valor y el único que **no se post-procesa: se produce**. Hoy no hay nada que parchear — 2.157 palabras para 22 capítulos en el
representante, 255 palabras de «manual de servicio de sala», y en 6 de las 8 guías **el PDF es una portada de una página**.

### 5.1 La promesa de páginas SE CUMPLE, no se rebaja (COM-01, COM-02, DOM-18) — §7-bis.6

Cada guía tiene su propia cifra en su landing y **cada una se mide por separado**: `guia-restaurante-gastronomico` **80+** · `guia-panaderia-obrador` **70+** ·
`casual`/`mexicano`/`peruano`/`japones`/`nikkei` **60+** · `guia-dark-kitchen` **+40**.

**Calibración medida hoy (2026-08-29) con la maqueta real de `bono_guia.py`** (A4, Helvetica 10,2/14,5, márgenes 2 cm, tablas con cabecera dorada): un
Markdown de **37.295 palabras con 33 tablas de 8 filas** produce **73 páginas** (499 palabras/página) sin saltos de página; **con `PageBreak` por capítulo más
portada e índice, 90 páginas** (410 palabras/página). Referencias de contraste: el bono del Kit de Escandallos son 6.848 palabras → **17 páginas**; el PDF vivo
de dark-kitchen, 7.023 palabras → **27 páginas**. **La densidad depende de la maqueta, así que el gate MIDE con PyMuPDF; no se estima.**

Presupuesto de palabras por guía, con el 15 % de margen sobre el mínimo:

| pid | capítulos | páginas prometidas | palabras objetivo | palabras/capítulo | palabras hoy | factor |
|---|---|---|---|---|---|---|
| guia-restaurante-gastronomico | 22 | 80+ | **~37.000** | 1.600-1.750 | 2.395 | ×15 |
| guia-panaderia-obrador | 20 | 70+ | **~33.000** | 1.550-1.700 | 4.699 | ×7 |
| guia-restaurante-nikkei | 20 | 60+ | **~28.000** | 1.300-1.500 | 6.317 | ×4,4 |
| guia-restaurante-japones | 20 | 60+ | **~28.000** | 1.300-1.500 | 5.813 | ×4,8 |
| guia-restaurante-peruano | 20 | 60+ | **~28.000** | 1.300-1.500 | 4.763 | ×5,9 |
| guia-restaurante-mexicano | 20 | 60+ | **~28.000** | 1.300-1.500 | 4.195 | ×6,7 |
| guia-restaurante-casual | 20 | 60+ | **~28.000** | 1.300-1.500 | 2.917 | ×9,6 |
| guia-dark-kitchen | 13 | +40 | **~19.000** | 1.400-1.550 | 7.023 | ×2,7 |

### 5.2 El guion, antes del texto (`guion_<pid>.py`)

Un capítulo no se le pide a `bridge.py` con un título: se le pide con un **guion cerrado**. Por capítulo: título · 4-6 epígrafes con lo que debe contener ·
**las cifras que ya existen en el producto y que el capítulo tiene que citar sin contradecir** (inversión, personal, superficies, food cost, ratios) · las
tablas exigidas con sus columnas · las trampas a evitar (§5.4). El guion se escribe **a partir de los ficheros de la propia guía**, para que sea el texto el que
se alinee con los xlsx y no al revés: la fuente única de inversión total, personal y fondo de maniobra es `plan-financiero-3-anos.xlsx` (§7-bis.7).

Los 22 capítulos del representante ya existen como titulares y se conservan; los que el R1 señala como más delgados —**9 (Equipamiento), 13 y 14 (Personal
cocina y sala), 19 (50 Best) y 21 (Tecnología)**, hoy de una frase más tabla— llevan el guion más detallado. Y hay contenido **prometido en la landing que no
existe en ningún fichero** y que el guion tiene que cubrir: `Thermomix` y `Pacojet` (0 ocurrencias, COM-23), «CRM de comensales» y «gestión de alérgenos» del
cap. 21, «evento inaugural» del cap. 20 (0 ocurrencias, COM-26) y la **Estrella Verde** (DOM-36).

### 5.3 Pipeline `bridge.py` → Markdown → DOCX + PDF

1. **Texto, capítulo a capítulo, con `bridge.py`. Nunca redactado por Claude** (regla capital). En este Mac el routing está desactualizado, así que la invocación
   es **siempre**:
   `python3 /Users/johnguerrero/chefbusiness-ai/bridge.py --task content --domain aichef --lang es --model ~deepseek/deepseek-v4-flash-latest --max-tokens 8192
   --prompt "<guion del capítulo>" --output <cap_NN.txt>`
   Verificado hoy: el `bridge.py` del Mac tiene `--max-tokens` **por defecto 4096**, enruta `content` a `deepseek-v4-pro` y **no tiene `--strict-lang` ni
   `guard_idioma()`** (sus argumentos son `--task --domain --lang --prompt --system --model --temperature --max-tokens --output --json`). Por eso el `--model` y
   el `--max-tokens` **no son opcionales** y el barrido de no latinos se hace **en el ensamblador**, no en el bridge.
2. **Ensamblado a un `.md` por guía**: portada · índice · 22/20/13 capítulos con `##`, epígrafes con `###`, tablas Markdown reales, viñetas, y `---` antes de
   cada capítulo para el salto de página.
3. **Gate de idioma ANTES de maquetar** — `guard_no_latinos(md)`: aborta con el fragmento de contexto si aparece CJK, cirílico, hangul, árabe, hebreo o
   tailandés. Es el mismo defecto que puso «鬼笔鹅膏菌» (*Amanita phalloides*) dentro de un prompt de garum en producción. Nota: el saneador WinAnsi de
   `bono_guia.py` ya los detectaría al maquetar (no son codificables en cp1252), pero **abortar al ensamblar es más barato que abortar al imprimir**, y el
   `.docx` no pasa por ese saneado. *(Los cinco ideogramas de esta línea son la cita del incidente y son los únicos caracteres no latinos de esta SPEC: si un
   barrido automático los señala, es este párrafo.)*
4. **Maquetado con el patrón de `kit-escandallos-v2_0/bono_guia.py`**: `parsear()` → `sanear_bloques()` → `restos_no_winansi()` (aborta si queda algo que
   Helvetica pintaría como ■) → `construir_docx()` (python-docx) + `construir_pdf()` (reportlab `SimpleDocTemplate`). **Se extiende con `PageBreak`** —hoy `---`
   sólo emite un `Spacer(1, 6)`— y con portada e índice. **El PDF y el DOCX salen del MISMO Markdown**, que es lo que hoy no ocurre en ninguna guía.
5. **Las tablas van ancladas dentro de su capítulo** (DOM-18): en el PDF actual del representante las cuatro tablas están **detrás de la línea de copyright**,
   en las páginas 9-10, dejando el cap. 4 sin su tabla de CAPEX y los caps. 9, 13 y 14 reducidos a una frase. `SimpleDocTemplate` con `Table(repeatRows=1)` lo
   resuelve por construcción; el gate lo verifica (§5.6).
6. **Metadata** (COM-24): `title`, `author='AI Chef Pro'` y `subject` en el PDF (hoy `'(anonymous)'`/`'untitled'` y fecha de creación de abril) y en el DOCX
   (hoy `author='python-docx'`, `comments='generated by python-docx'`, `created=2013-12-23`), más el pie «Versión 2.0 · agosto 2026 · aichef.pro/<pid>» y la bio
   anclada, que los documentos tampoco llevan.

### 5.4 Contenido: lo que el guion debe corregir, no repetir

El texto nuevo **no puede reproducir los errores del viejo**. Va al guion como restricción explícita, capítulo por capítulo:

- **Personal con SS de verdad** (DOM-02, COM-10, alta). Hoy: «coste total anual personal cocina 250.000-450.000 € (incluyendo SS empresa ~30 %)» cuando la suma
  de su propia tabla **es el bruto sin SS**. Cifras correctas: cocina **322.400-601.900 €**, sala **234.000-403.000 €**, total **556 k€-1,0 M€**. Bajo cada
  tabla, filas «Total bruto» y «Total con SS (×1,33)», con el tipo tomado de la celda de `plantilla-turnos-brigada` (§4.4) y no de un «~30 %» escrito a mano.
- **Ningún salario por debajo del SMI** (DOM-13): «Ayudante de cocina 16.000-19.000 €» y «Plonge 15.000-17.000 €» quedan por debajo del mínimo legal. Los suelos
  se suben a la tabla del convenio provincial, con la nota de que el convenio prevalece sobre el SMI, y **los totales del capítulo se rehacen**.
- **Una sola cifra de inversión** (DOM-17, COM-09, §7-bis.7): hoy conviven «500.000-900.000 €» en el texto (caps. 1 y 4 y dos FAQ), **363.000/685.000/1.240.000 €**
  en la tabla 0 del mismo capítulo y **373.000/703.000/1.275.000 €** en `calculadora-capex`. Y los checklists tasados uno a uno la desmienten por partidas
  (equipamiento 112.070 € frente a 55.000-90.000 €; sala 108.200 € frente a 50.000 €; vajilla 30.230 € frente a 15.000 €; legal 23.980 € frente a 8.000 €;
  marketing 22.800 € frente a 5.000 €). Manda **el plan financiero**, y el texto lo cita.
- **Fondo de maniobra** (DOM-01, COM-30): «(3-6 meses)» y «(6 meses)» para la misma partida, con 60.000-200.000 € que no cubren cuatro meses de la nómina más
  barata. Rótulo único y cifra que salga de la fórmula de §2.3.5.
- **Superficies coherentes** (DOM-32): «250 m² totales» con «sala 120-160 m² y cocina 60-80 m²» deja 10 m² para aseos, aseo adaptado, vestuarios de 22-30
  trabajadores, oficina y almacén; y 60 sobre 250 es el 24 %, por debajo del 25 % mínimo que el propio párrafo fija. Se recalcula a **280-340 m²** y se añade la
  reserva de vestuarios y aseos de personal (RD 486/1997), hoy ausente de los 141 ficheros.
- **Equipamiento coherente con los checklists** (DOM-33, DOM-34, COM-23): el texto especifica túnel de lavado en el plonge y el checklist presupuesta un
  lavavajillas de capota de 3.500 € (8.000-20.000 € de diferencia); «cocina industrial 6 fuegos gama alta + horno 5.000-5.200 €» es un rango de 200 € de
  amplitud junto a un Josper de 12.000 € en el mismo libro. Se unifica con §3.4.
- **Michelin y Repsol con fuente y fecha** (DOM-29, DOM-36, COM-36): «tercer país del mundo tras Francia y Japón» es incorrecto (Italia supera a España en
  número de estrellados) y el bloque entero —306 estrellados, 12 tres estrellas, «más de 600 Soles», «3.000 millones», «+12 % anual», «85 % fuera de Madrid y
  Barcelona», «12 inspectores», «70 inspectores» de Repsol, «1.120 expertos» de 50 Best— **no lleva una sola fuente**, en un capítulo titulado 2026. Cada dato
  con fuente y fecha de corte («Guía Michelin España, edición 2026») o se pasa a una formulación robusta. Y se matiza «lo que NO evalúan: servicio, vajilla,
  decoración», que desautoriza los 15.000-65.000 € en vajilla que el propio libro recomienda y los ítems de servicio de su checklist de inspección: las
  estrellas se otorgan por el plato, el confort se refleja en los cubiertos y **la Estrella Verde** reconoce la sostenibilidad.
- **Tendencias con año vigente** (COM-29): «22. Tendencias 2025-2026» en un producto de agosto de 2026 cuya portada dice «Guía España 2026» → **2026-2027**. Es
  exactamente el defecto de fecha caduca que ya costó dinero en las librerías de prompts.
- **Reservas disponibles en España** (DOM-35): fuera Resy («300-500 USD/mes», única moneda extranjera de la guía, y no opera en España).
- **IVA, financiación y arrendamiento** entran en el texto, no sólo en los xlsx: el IVA del CAPEX como necesidad de tesorería con su plazo de devolución (cap. 4),
  un epígrafe de fuentes de financiación y servicio de deuda (cap. 4) y el contrato de arrendamiento con carencia (cap. 7).

### 5.5 Los dos bonus dejan de ser un índice (DOM-19, DOM-25, DOM-31, COM-11, COM-16, COM-35) — §7-bis.6

- **`business-plan-modelo.docx`** (BONUS 1, 49 EUR): hoy **66 párrafos, ~300 palabras, 0 tablas**, y el único hueco rellenable de todo el documento es
  «[Tu resumen ejecutivo aquí…]»; el resto son enunciados de lo que el usuario debe escribir. La landing promete «resumen ejecutivo, proyecciones financieras a
  3 años y análisis de mercado». Pasa a ser un **plan de negocio modelo RELLENO**: caso completo del concepto de esa guía con cifras, **tablas de CAPEX, P&L a 3
  años y cash flow** coherentes con `plan-financiero-3-anos.xlsx` (§2.3), análisis de mercado ya redactado, análisis de riesgos con escenarios, y los huecos
  marcados como tales. Objetivo **≥ 3.000 palabras y ≥ 6 tablas**.
- **`manual-servicio-sala.docx`** (representante) y **`manual-operaciones[-<concepto>].docx`** (hermanos), BONUS 2, 39 EUR: hoy **255-1.439 palabras**, un
  párrafo por apartado (el apartado «Gestión de Quejas» completo son **26 palabras**). Pasa a manual utilizable: mise en place de sala · **secuencia del menú
  degustación pase a pase** (marcaje de cubiertos, cambio de copa, tiempos objetivo entre pases) · temperaturas de servicio y decantación · briefing
  pre-servicio · política de no-show y prepago · gestión de la cuenta · casuística de quejas con guiones literales · **fichas de formación** · y, antes que
  nada, el **protocolo de alérgenos en sala**, que el propio `checklist-appcc` asigna al maître y que es exigible por el Reglamento UE 1169/2011 y el RD
  126/2015. Objetivo **≥ 3.000 palabras**.
- **Dos errores de oficio que el manual enseña hoy al revés** (DOM-31, COM-35): «servir por la izquierda, retirar por la derecha» — en **plato emplatado**, que
  es el único servicio de un menú de 8-12 pases, se sirve y se retira **por la derecha**; la izquierda es para el servicio en fuente. Y «sirve a los demás
  comenzando por las señoras» → **sentido horario desde el invitado de honor, terminando por el anfitrión, que es quien cata**.

### 5.6 Gates de los documentos (bloqueantes)

1. **Páginas**: `fitz.open(pdf).page_count >= <prometidas>` para cada uno de los 8. Si falla, **se amplían los capítulos más delgados**; no se toca la cifra de
   la landing (§7-bis.6).
2. **Palabras**: `>= objetivo × 0,95` en el PDF y en el DOCX, y **ningún capítulo por debajo de 900 palabras** (hoy la media del representante es 109).
3. **Paridad PDF↔DOCX**: mismo número de `##`, mismo número de tablas, diferencia de palabras < 2 %.
4. **Tablas ancladas**: ninguna tabla después del último `##`, y **≥ 1 tabla en cada uno de los capítulos que el guion las exige**; cero contenido después del
   pie de copyright.
5. **No latinos**: 0 caracteres CJK/cirílico/hangul/árabe/hebreo/tailandés en el `.md`, el `.docx` y el texto extraído del PDF.
6. **WinAnsi**: `restos_no_winansi()` = 0 (si no, aborta: un ■ en la columna que distingue «dentro de objetivo» de «pierde dinero» no es un detalle
   tipográfico).
7. **Fechas caducas**: ningún año anterior a 2026 a menos de 90 caracteres de lenguaje de precios o de la palabra «tendencias» (el mismo gate `valida()` de
   `fase8c-libreria-assemble.py`, con su ventana, para no tumbar un «1982» legítimo de un bloque de historia).
8. **Coherencia de cifras** (§7-bis.7): la inversión total, el coste de personal, el fondo de maniobra y el headcount que aparecen en el texto **coinciden con
   los del xlsx**, comparados por extracción, no a ojo.
9. **Metadata**: `author='AI Chef Pro'` y `title` no vacío en los 8 PDF y los 22 DOCX.

---

## 6. Integración — landing, dashboard, changelog, emails, FAQ y JSON-LD (`integracion`, sonnet)

**Superficies por guía** (censadas 2026-08-29): landing `astro-site/src/data/productos/guias/<pid>.ts` (la que sirve producción) · dashboard
`src/pages/Guia<Concepto>Dashboard.tsx` · descargas `netlify/functions/get-download-urls.ts` **y** su gemelo `src/data/productos-digitales-config.ts` ·
emails `netlify/functions/verify-purchase.ts` y `resend-access.ts` · `src/data/productos-changelog.ts` · `src/data/products-catalog.ts`.
**`get-download-urls.ts` no se toca**: las claves viajan en emails ya enviados (§7-bis.1).

- **6.1 El número de páginas deja de ser falso porque el PDF pasa a tenerlas** (COM-01). En el representante la cifra «22 capítulos, 80+ páginas» aparece en
  `guia-restaurante-gastronomico.ts:13` (meta description), `:23` (hero), `:25` (checkItem) y `:151` (CTA), más `GuiaRestauranteGastronomicoDashboard.tsx:20`.
  **No se cambia el número: se cambia el fichero** (§5.1). Después del gate de páginas, el texto se ajusta **a la cifra medida** («22 capítulos, 90 páginas»),
  que es mejor que el «80+» y ya es verificable. Lo mismo en las otras siete.
- **6.2 «Fórmulas» deja de ser un «Sí» falso** (COM-03, alta). `guia-restaurante-gastronomico.ts` FAQ (~línea 142) y **el mismo texto duplicado en el JSON-LD**
  (~línea 187, «Todo con fórmulas encadenadas») responden que sí a la pregunta exacta del escéptico, con **4 de 10 plantillas a cero fórmulas**. Con §2-§4 la
  afirmación pasa a ser cierta **dentro de cada libro**; entre libros se dice lo que de verdad hay, como ya se firmó en el kit de inventario y en el plan
  financiero: «**coherentes entre sí**: la misma inversión, el mismo coste de personal y el mismo food cost en todas las plantillas; dentro de cada libro las
  fórmulas sí están encadenadas». **El `FAQPage` se genera desde el mismo array `faqs`** del acordeón, para que no vuelvan a divergir. En los hermanos la
  fórmula es «fórmulas automáticas»; mismo tratamiento.
- **6.3 Las cifras de plantillas, cuadradas landing↔dashboard.** Medido: **4 de las 8 landings dicen «8 plantillas Excel» y su dashboard entrega 9** —
  `guia-restaurante-casual.ts`, `-mexicano.ts`, `-peruano.ts`, `-japones.ts` (líneas de `checkItems`, `grid.headingRest` y la FAQ) frente al literal
  `'Plantillas Excel (9)'` de `src/pages/GuiaRestaurante{Casual,Mexicano,Peruano,Japones}Dashboard.tsx:25`. Se corrige **la landing a 9** (el producto entrega
  9): es la dirección honesta y la que no obliga a retirar un fichero. `nikkei` (9/9), `panaderia` (9/9) y `gastronomico` (10/10) ya cuadran.
- **6.4 El email post-pago cuenta mal el paquete** (COM-25). Representante: «la guía PDF + DOCX + **20 plantillas y checklists Excel**» cuando son **18 xlsx + 2
  docx** (`verify-purchase.ts:147-152` y `resend-access.ts:147-151`) → «18 plantillas y checklists Excel + el business plan y el manual de sala en Word». Y en
  **casual** el número está directamente mal: dice **16** y son **17** (9 + 6 + 2), replicado en `verify-purchase.ts:158`, `resend-access.ts:158` y
  `productos-digitales-config.ts:956` y `:958`. Es la peor superficie para descontar una unidad: el comprador acaba de pagar y está contando. Los otros seis
  (17/17/17/17/17 y 3) están bien y no se tocan.
- **6.5 Las cifras de ítems de los checklists** (COM-17, COM-18, DOM-40). Se **completa el contenido** hasta lo anunciado (§3.4) y el gate vuelve a contar; si
  algún checklist se queda corto, se corrige **la tarjeta**, nunca al revés en silencio. Casos: `checklist-equipamiento` 54→90 (`…Dashboard.tsx:43`),
  `appcc` 45→55 (`:45`), `vajilla` 43→50 (`:44`), `michelin` 40→45 (`:46` + `bonus.items[2]` + la FAQ de Michelin, **tres sitios**), `diseno-sala` 31→35 (`:47`),
  `marketing` 30→35 (`:49`). Y **«Zwiesel»** (`guia-restaurante-gastronomico.ts:74`) sale: no aparece en ningún fichero; el cap. 11 nombra Riedel, Zalto, RAK,
  Villeroy & Boch, Bernardaud, Noritake, WMF y Christofle.
- **6.6 El headcount y la inversión, una sola cifra en todas las superficies** (COM-21, COM-09, §7-bis.7): el «25 personas» del dashboard
  (`…Dashboard.tsx:36`) y de `Instrucciones!A1` frente a las 24 filas del cuadrante y al «22-30» del cap. 14; y el «Inversión 500K-900K€» de
  `guia-restaurante-gastronomico.ts:67`, `why.reasons[1]`, `faqs[0]` y `schema.faqs[0]` frente a los totales reales. Se propaga **una sola** desde el plan
  financiero.
- **6.7 Las tarjetas que describen lo que el fichero no hace** pasan a ser ciertas con §2-§4 y se reescriben igualmente donde el texto prometía otra cosa:
  `pl-mensual` «con fórmulas encadenadas» (`:29`), `calculadora-ticket` «Simulador de escenarios» (`:34`), `cash-flow` «punto de equilibrio automático» (`:30`
  — la cadena «punto de equilibrio» aparece **0 veces** en los 141 ficheros), `menu-engineering` «clasificación automática» (`:32`), `plantilla-turnos`
  «cuadrante para 25 personas **con coste**» (`:36`), `cronograma-gantt` «fases, dependencias e hitos» (`:35`), `plan-financiero` «proyección a 3 años» (`:27`),
  `budget-bodega` «coste, PVP, margen, rotación, stock» (`:33`). Y los dos bonus (`bonus.items[0]` 49 EUR y `[1]` 39 EUR) sólo mantienen su promesa **después**
  de §5.5.
- **6.8 Las tarjetas de capítulo que prometen lo que el capítulo no trae** (COM-23, COM-26): `grid.chapters[8]` (Thermomix, Pacojet), `[19]` («evento
  inaugural»), `[20]` (CRM de comensales, gestión de alérgenos) y `[21]` («Tendencias 2025-2026» → 2026-2027). Con §5.2 el capítulo pasa a cubrirlas; la tarjeta
  se revisa una a una contra el `.md` final, no contra el guion.
- **6.9 El changelog dice lo que se hizo** (COM-27). Las 8 entradas de `productos-changelog.ts` titulan la v1.1 «Revisión completa de las 18 / 15 / 3
  plantillas» (`:117-131` gastronómico, `:100-116` casual, `:84-98` panadería, `:150-165` mexicano, `:184-199` peruano, `:133-148` japonés, `:167-183` nikkei,
  `:67-82` dark-kitchen) y lo que enumeran debajo son cambios de impresión, versión y metadatos. Un cliente que lea «revisión completa», vuelva a descargar y
  encuentre dos plantillas en blanco lo lee como una promesa incumplida — y el bloque le acaba de decir «cada mejora aparece aquí». Se **retitula la v1.1** a
  «Mejoras de impresión, metadatos y versión en las N plantillas» y se añade la entrada **2.0** en lenguaje de cliente, con una línea por cálculo que ahora
  existe y una por documento reescrito. `updateNote` → v2.0.
- **6.10 `products-catalog.ts`**: sólo están `guia-dark-kitchen` (`:216`), `guia-restaurante-gastronomico` (`:226`) y `guia-restaurante-casual` (`:236`).
  **Faltan las cinco restantes** (panadería, mexicano, peruano, japonés, nikkei). Se añaden con su precio real (65 €), o queda documentado por qué no — hoy es
  una ausencia silenciosa que afecta al hub y a cualquier consumidor del catálogo.
- **6.11 Gates de integración**: `censo-entregables.py --only <pid> --fail --quiet` (0 defectos) en los 8 · `gate-flujo-postpago.py --offline --only <pid>`
  (22/19/19/19/19/19/19/5 ficheros, 0 fallos) · `inject_cache.py` al final de cada producto · verificación `data_only` (ninguna celda de resultado en `None`) ·
  idempotencia (segunda pasada = 0 cambios) · y un **gate de coherencia de cifras** nuevo que cruce landing + dashboard + email + changelog + xlsx + PDF y falle
  si una misma magnitud aparece con dos valores.

---

## 7. Descartado con motivo · dudas · para John

### 7.1 Descartado, con motivo

- **Reejecutar los 7 generadores** (lectura literal de varios «fix» del R1): no. Escriben a una ruta muerta, reintroducen la fórmula circular
  `Break-Even!B12='=B12*(1-B8)'` en 5 guías y revierten la Fase A entera. Argumentado en la cabecera.
- **Fusionar libros o enlazarlos con `externalLink`** (lectura literal de TEC-26/COM-32, «que uno lea del otro»): no. Un `.xlsx` movido de carpeta daría
  `#REF!` al cliente, y fusionar invalidaría claves de descarga ya enviadas por email. La coherencia se consigue repitiendo el dato con la nota de «de dónde
  sale» (§2.3.6).
- **Crear ficheros nuevos** (p. ej. un libro de financiación, un «escandallo por plato»): no. `Financiación` va como **hoja dentro** de
  `plan-financiero-3-anos.xlsx` y el escandallo se resuelve con `Ficha (plantilla)` + hoja `Resumen` (§4.1). Sólo se añadirá un fichero si la landing ya lo
  promete y no existe — no es el caso en ninguna de las 8.
- **Bajar la cifra de páginas de la landing a la real** (opción (b) de COM-01 y DOM-18): no. Decisión 6 del orquestador: la promesa se cumple.
- **Redimensionar la dotación de vajilla** (DOM-21): no se cambia la dotación de carta, que es correcta para su supuesto; se **añade una segunda columna «Menú
  degustación»** con la regla de cálculo, para que el cliente vea las dos y elija.
- **Borrar la categoría «Reputación» del checklist Michelin** (COM-34): no se borra —son acciones legítimas de prensa—; se separa a un bloque rotulado «no
  influye en la inspección».
- **Añadir columna de coste al molde B de panadería** (extensión de TEC-16 a los 6 checklists de panadería): no por defecto. Ver duda 7.2.
- **`aggregateRating`, reseñas, testimonios y ancla de precio**: aparcado por John (§7-bis.8). Sube a §7.3.

### 7.2 Dudas para el orquestador

- **7.2.1 SMI: valor y fuente.** `kit-gestion-personal-v2-SPEC.md` fija la **SS empresarial en celda al 33 %** pero **no fija el SMI**. Aquí hace falta un
  número, porque dos puestos del cap. 13 quedan por debajo. *Propuesta*: celda verde **«SMI vigente (€/año, 14 pagas)»** con el **último valor conocido y su año
  en la nota**, más «el mínimo aplicable lo fija el convenio provincial de hostelería, que prevalece». **Si el orquestador no aporta el valor con fuente, la
  celda queda vacía y el gate lo marca**: no se inventa una cifra (regla capital).
- **7.2.2 Panadería, molde B sin columna de coste.** Sus 6 checklists no tienen `Coste Est. (€)`, así que no pueden dar un presupuesto de apertura como los del
  molde A. *Recomiendo NO añadirla*: obligaría a inventar ~200 importes que nadie ha tasado, y el valor del molde B está en el plazo orientativo. Si John la
  quiere, es un encargo de research, no de motor.
- **7.2.3 ¿La landing dice «80+ páginas» o «90 páginas»?** Tras §5 el PDF tendrá una cifra medida. *Recomiendo la cifra exacta medida*: es mayor que la
  prometida, deja de ser un «+» inverificable y da un dato que el comprador puede comprobar en el primer segundo. Aplica a las 8.
- **7.2.4 Dark-kitchen no tiene bonus docx.** Sus 5 entregables no incluyen business plan ni manual, y **su landing tampoco los promete** (3 bonus por 47 EUR:
  dos checklists y la calculadora). *Recomiendo no crearlos*: añadiría claves de descarga nuevas sin promesa detrás. Sólo recibe §1, §3, §5.1-5.4 (guía a +40
  páginas) y §6.
- **7.2.5 Las 5 guías que faltan en `products-catalog.ts`.** ¿Se añaden panadería, mexicano, peruano, japonés y nikkei con su precio (65 €)? *Recomiendo sí*:
  hoy es una ausencia silenciosa. Pero toca el hub, así que lo decides tú.
- **7.2.6 Datos del sector que hay que verificar fuera del repo** (DOM-29, COM-36): reparto de estrellas Michelin en España, número de Soles Repsol, facturación
  del turismo gastronómico. Necesitan research con fuente antes de escribir el cap. 2 de la guía gastronómica; **no salen de `bridge.py`**, que los inventaría.

### 7.3 Para John (no se toca en la v2.0; queda descrito el riesgo)

- **`aggregateRating` fabricado, en las 8 guías** (COM-12). Las ocho landings emiten en el JSON-LD `aggregateRating: { ratingValue: '4.9', reviewCount: '8',
  bestRating: '5', worstRating: '1' }`, y esas «8 reseñas» son **los 8 testimonios redactados con avatares de stock** (`/avatars/avatar-1.jpg`…`-8.jpg`). No
  existe ningún sistema de reseñas ni endpoint para estos productos. Son **64 reseñas inventadas** publicadas como dato estructurado. El art. 20 y el 20 bis del
  TRLGDCU tras la Ley 4/2022 exigen poder acreditar que las valoraciones proceden de compradores reales, y las políticas de rich results de Google prohíben las
  valoraciones autogeneradas, con riesgo de **acción manual sobre todo el dominio**.
- **Testimonios con credenciales verificables y estrechas** (DOM-24): «Ana Beltrán, Consultora gastronómica, **ex-directora Guía Repsol**» —un cargo real
  ocupado por personas identificables— y «Pablo Fernández, Inversor: *el business plan modelo… lo presenté tal cual a mi banco y me aprobaron la financiación*»,
  cuando el fichero es hoy un índice con un placeholder. También «Chef ejecutivo, 1 Estrella Michelin en Madrid» y «restaurante 2 Soles Repsol en Galicia»: el
  círculo de personas reales a las que apuntan es muy pequeño. **La v2.0 hace ciertas varias de las funciones que describen** (fórmulas, Gantt, business plan
  relleno), lo que reduce el problema pero no lo elimina.
- **Ancla de precio permanente** (COM-13): `guia-restaurante-gastronomico.ts:36-43` anuncia **220 EUR tachado**, **-61 %**, «Precio de lanzamiento — ahorra 135
  EUR» ×2 y «Ahorra 135 EUR HOY», sobre un producto que en el catálogo vale 85 € y que **se lanzó a 85 €** (sesión del 2026-04-06). Las otras seis llevan
  **180 EUR / -64 %** y dark-kitchen **90 EUR / -73 %** (y su `buyBoxNote` dice «71 %» mientras el badge dice «-73 %»). El «lanzamiento» lleva más de cuatro
  meses. El art. 20 del TRLGDCU tras el RDL 24/2021 (Directiva Ómnibus) exige que el precio anterior anunciado sea **el más bajo aplicado en los 30 días
  previos**. El «HOY» y el «lanzamiento» perpetuos son el agravante clásico.

---

## 7-bis. Decisiones del orquestador ya tomadas (no se reabren al construir)

1. **Mismos ficheros y mismos nombres en cada guía.** Las claves de `get-download-urls.ts` y de `productos-digitales-config.ts` viajan en emails ya enviados: no
   se renombra ni se retira ningún entregable. **Se puede añadir una hoja dentro de un libro**; no se crean ficheros nuevos salvo que la landing ya los prometa
   (no ocurre en ninguna de las 8).
2. **Las 4 plantillas sin fórmulas se convierten en herramientas reales**: `calculadora-ticket-medio` (ticket ponderado por mix, facturación día/mes, 3
   escenarios), `pl-mensual-escenarios` (P&L encadenado con 3 escenarios y semáforo), `cash-flow-break-even` (12 meses con totales, flujo neto, acumulado,
   break-even en meses **y** en €, financiación con cuota), `menu-engineering-matrix` (Kasavana & Smith completo: mix, umbral 70 %/N, margen medio,
   clasificación por fórmula). §2.1, §2.2, §2.4, §4.2.
3. **`plan-financiero-3-anos`**: proyección a 3 años de verdad en **hoja nueva**; **EBITDA que NO resta amortización**; IVA; **SS al 33 % en celda**;
   financiación con cuadro de amortización; y **fondo de maniobra dimensionado** (≥ 6 meses de costes fijos + personal según la propia tabla del libro). §2.3.
4. **`escandallo-maestro`**: raciones y merma entran en el coste; **food cost objetivo en celda y usada** por la fórmula; PVP **con y sin IVA** (10 % de
   restauración, celda editable). §4.1.
5. **Legal y sanitario VIGENTES**: sin libro de visitas (derogado); **registro de jornada obligatorio** (plantilla de turnos que calcule horas y coste y sirva
   de registro); **APPCC con anisakis** (congelación preventiva) y controles de baja temperatura/vacío; licencias descritas **por tipo genérico** con la nota
   «la nomenclatura es autonómica/municipal»; **ningún puesto por debajo del SMI**. §3.1, §3.2, §4.4.
6. **La promesa de páginas SE CUMPLE, no se rebaja.** Guía real de ≥ las páginas prometidas por cada landing, con tablas, redactada **capítulo a capítulo con
   `bridge.py`** desde un guion detallado por guía y maquetada con reportlab (patrón `bono_guia.py`), con gate de páginas, palabras y caracteres no latinos. Los
   **dos bonus docx** pasan a ser documentos reales: plan de negocio modelo **con tablas y proyecciones**, y manual con guiones de servicio, tiempos, protocolo
   de alérgenos y fichas de formación. `bridge.py` es barato: se hace por guía. §5.
7. **Coherencia interna de cifras: UNA sola fuente por guía.** Inversión total, coste de personal, fondo de maniobra y headcount salen de las celdas de
   `plan-financiero-3-anos.xlsx` (con el personal desde `plantilla-turnos-brigada.xlsx`), y el PDF, la landing y el dashboard **las citan**. Tres cifras
   distintas de inversión en el mismo producto es un **defecto**, no un matiz. §5.4, §6.6.
8. **`aggregateRating`, reseñas, testimonios y ancla de precio: NO se tocan** (decisión de John, igual que en el plan financiero). Van a §7.3 con el riesgo
   descrito, sin más.
9. **Método de familia**: motor común (post-proceso, argumentado en la cabecera) + módulo de contenido por guía; **representante primero** con 3 refutadores +
   corrector + ronda 2 + crítico; **hermanos por sonnet verificando cada id del representante**; ejecución real **en serie con canario**; capa de producto
   aparte, con landing, dashboard, changelog y emails **honestos con lo que hay** (nº de páginas real; «fórmulas encadenadas» sólo si lo son). §9.
10. **Térmica y seguridad**: `--dry-run` a scratchpad por defecto, **APPLY sólo con `GUIAS_APPLY=1`** y respaldo previo, **un python cada vez**, `istats cpu
    temp` antes de cada ejecución, sin builds locales ni navegador.

**Decisiones añadidas al escribir esta SPEC** (argumentadas arriba, y que el constructor tampoco reabre):

11. **El motor detecta el molde antes de escribir y aborta si no lo reconoce** (§1.1). La familia tiene **tres moldes de checklist** y **tres variantes de
    `pl-mensual`**; dar por hecho el del representante rompe panadería y duplica el total de dark-kitchen. Es el mismo error que costó dinero con los «tres
    moldes de HTML» del blog.
12. **Las constantes tecleadas de los hermanos se convierten en fórmulas conservando el número como dato de ejemplo** (§1.2), y la diferencia entre el valor
    viejo y el nuevo queda anotada por fichero. No se borra un número que el cliente pueda estar usando.
13. **«Sin dato» se escribe `""`, nunca `0`** (§2.2), y todo semáforo que pueda leer texto lleva `ISNUMBER` en la guarda (§1.6). Un mes sin una sola venta no
    tiene un margen del «0,0 %».
14. **El escenario «Pesimista» se recalibra: malo, no inviable.** Hoy el de japonés entrega un **EBITDA de −12.055 €/mes** tecleado a mano. Un pesimista que
    dice al comprador que pierde 145 k€/año no es prudencia, es un error de calibración que invalida la herramienta. Se recalibra con el módulo de contenido y
    queda etiquetado como valor de ejemplo.
15. **La guía y su DOCX salen del MISMO Markdown** (§5.3): hoy divergen en las 8 (en 6 el PDF ni siquiera contiene la guía). El gate exige paridad de capítulos,
    de tablas y de palabras al 2 %.

---

16. **SMI vigente (7.2.1) = 1.221 €/mes × 14 pagas = 17.094 €/año — Real Decreto 126/2026, de 18 de febrero (BOE-A-2026-3815, BOE de 19-feb-2026),
    en vigor con efectos desde el 1-ene-2026** (firmado por el orquestador el 2026-08-29 con la fuente verificada). Celda verde «SMI vigente (€/año, 14 pagas)»
    con ese valor, nota con el RD y el año, y la advertencia de que el convenio provincial de hostelería prevalece si fija un mínimo superior. Ningún puesto del
    cap. 13 ni de `plantilla-turnos-brigada` puede quedar por debajo: gate.
17. **Panadería (7.2.2): NO se añade columna de coste al molde B.** Sería inventar ~200 importes sin tasar; si John la quiere, es research aparte.
18. **La landing publica la cifra de páginas MEDIDA (7.2.3), no «80+»**: se escribe después de contar con PyMuPDF (T8 va detrás de T7). Aplica a las 8.
19. **Dark-kitchen (7.2.4): sin bonus docx nuevos** (su landing no los promete; no se crean claves de descarga sin promesa detrás). Recibe §1, §3, §5.1-5.4 y §6.
20. **Las 5 guías ausentes de `products-catalog.ts` (7.2.5) SE AÑADEN** con el precio leído de su propio data file de Astro (no se teclea: el integrador lo
    lee), para que los banners del blog y el hub puedan enlazarlas. Es capa de producto (T8).
21. **Datos del sector con fuente (7.2.6)**: antes del guion, un paso de research (WebSearch/WebFetch por un agente, con URL y fecha por dato) para estrellas
    Michelin en España, Soles Repsol y facturación del turismo gastronómico; cada cifra va al guion con su fuente y **la que no tenga fuente NO entra** en la
    guía (se reformula sin número). `bridge.py` no genera cifras del sector.
22. **Recuentos honestos en toda la capa de producto (EXTRA de la SPEC)**: «8 plantillas Excel» → el número real del dashboard (9) en casual, mexicano, peruano
    y japonés; el `emailBody` de casual (16 → 17) en `verify-purchase.ts`, `resend-access.ts` y `productos-digitales-config.ts`. El gate de coherencia de cifras
    de §6 los cruza.

## 8. Mapa id → sección (106/106)

Los **106** hallazgos del R1 del representante, más los dos que ha añadido el censo de familia (`NUEVO-01`, `NUEVO-02`, §2.5). La columna **ámbito** dice si
el defecto es de **FAMILIA** (aparece en varias guías, con el número entre paréntesis) o **sólo del REPRESENTANTE** — ninguno se da por replicado sin
medirlo en el hermano (§9).

| id | sev | sección | qué | ámbito |
|---|---|---|---|---|
| TEC-01 | alta | §2.1 | el simulador de ticket medio calcula; fuera el verde de las filas de resultado | FAMILIA (7) |
| TEC-02 | alta | §2.2 | P&L de 3 escenarios encadenado | FAMILIA (7) |
| TEC-03 | alta | §2.4 | totales, flujo neto, acumulado y break-even del cash flow | FAMILIA (7) |
| TEC-04 | alta | §4.2 | columna Clasificación + mix + umbral + margen medio | FAMILIA (6) |
| TEC-05 | alta | §4.1 | el PVP divide por raciones (F4) | REPRESENTANTE |
| TEC-06 | alta | §1.7 §4.1 | merma en 0,0% con DV 0-0,95 y fórmula blindada | FAMILIA (8) |
| TEC-07 | alta | §2.3.1 | hoja «Proyección 3 Años» que las Instrucciones ya anuncian | FAMILIA (7) |
| TEC-08 | alta | §2.3.2 | el EBITDA deja de restar la amortización; se añade EBIT | REPRESENTANTE |
| TEC-09 | media | §2.3.3 | B35 «Margen EBITDA» pasa de € a 0.0% | REPRESENTANTE |
| TEC-10 | media | §2.3.3 | C35 y el arrastre de la columna % s/Ventas | REPRESENTANTE |
| TEC-11 | media | §4.4 | horas por SUMPRODUCT y columnas de coste | FAMILIA (7) |
| TEC-12 | media | §1.7 §4.4 | la «V» de la DV se documenta como Vacaciones | FAMILIA (7) |
| TEC-13 | media | §4.4 §6.6 | headcount único: 24 puestos vs «25 personas» | REPRESENTANTE |
| TEC-14 | media | §3.5 | barras del Gantt por formato condicional sobre Mes inicio/Duración | FAMILIA (7) |
| TEC-15 | media | §1.4 §3.5 | Inicio/Fin en dd/mm/yyyy con DV de fecha + columna Días | FAMILIA (7) |
| TEC-16 | media | §1.9 | fila TOTAL y subtotales por categoría en los checklists | FAMILIA (molde A y B; C ya lo tiene) |
| TEC-17 | media | §1.4 §3.3 | Fecha Límite con formato/DV y semáforo de Estado | FAMILIA (molde A) |
| TEC-18 | media | §4.3 | la rotación se calcula o se corrige la instrucción | REPRESENTANTE |
| TEC-19 | media | §4.3 | valoración del stock a coste y a PVP + fila TOTAL | REPRESENTANTE |
| TEC-20 | media | §4.3 | «Margen (%)» es markup: se separan multiplicador, margen s/PVP y food cost | REPRESENTANTE |
| TEC-21 | media | §4.1 | food cost objetivo como número en celda y usado por la fórmula | FAMILIA (8) |
| TEC-22 | media | §1.12 | etiquetas A4 y G4 cortadas por ancho de columna | REPRESENTANTE |
| TEC-23 | media | §4.1 | hoja «Ficha (plantilla)» + hoja «Resumen» + instrucción de duplicar | FAMILIA (8) |
| TEC-24 | media | §1.4 | «Uds Vendidas» deja de ir en € | REPRESENTANTE |
| TEC-25 | media | §1.4 | formato por tipo de dato, no por bloque (% y recuentos en €) | FAMILIA (8) |
| TEC-26 | media | §2.3.6 | fuente única de CAPEX: rangos vs «Mi CAPEX» + tabla de correspondencia | FAMILIA (7) |
| TEC-27 | media | §2.3.6 §6.6 | los totales del CAPEX y el rango de la landing dicen lo mismo | FAMILIA (8) |
| TEC-28 | media | §1.10 | Instrucciones, pestaña, versión y bio en los checklists | FAMILIA (molde A y B) |
| TEC-29 | baja | §1.6 §3.3 | formato condicional: hoy 0 reglas en los 141 libros | FAMILIA (8) |
| TEC-30 | baja | §1.8 | protección de hoja sin contraseña y verdes desbloqueadas | FAMILIA (8) |
| DOM-01 | alta | §2.3.5 §5.4 | fondo de maniobra dimensionado por fórmula, ≥ 6 meses | FAMILIA (8) |
| DOM-02 | alta | §4.4 §5.4 | SS empresarial en celda (33 %) y totales del capítulo rehechos | FAMILIA (8) |
| DOM-03 | alta | §1.5 §2.4 §4.1 | IVA declarado: PVP con y sin, y las tres filas del 303 en el cash flow | FAMILIA (rep. sin IVA; hermanos con 1.10 incrustado) |
| DOM-04 | alta | §4.1 | la merma entra en el coste (bruta = neta/(1-merma)) | FAMILIA (8, dos modelos) |
| DOM-05 | alta | §4.1 | coste por ración y PVP por ración | REPRESENTANTE |
| DOM-06 | alta | §2.3.1 | la proyección a 3 años existe | FAMILIA (7) |
| DOM-07 | alta | §2.2 | pl-mensual deja de ser inerte | FAMILIA (7) |
| DOM-08 | alta | §2.1 | la calculadora de ticket medio calcula | FAMILIA (7) |
| DOM-09 | alta | §2.4 | break-even en meses y en € | FAMILIA (7) |
| DOM-10 | alta | §4.2 | Kasavana & Smith completo + acción recomendada | FAMILIA (6) |
| DOM-11 | alta | §3.1 | licencia por tipo genérico; fuera «cocina separada del comedor» | FAMILIA (8) |
| DOM-12 | alta | §3.1 | fuera el libro de visitas; entra el registro de jornada | FAMILIA (8) |
| DOM-13 | alta | §3.1 §4.4 §5.4 | ningún puesto por debajo del SMI; celda de SMI vigente | FAMILIA (8) |
| DOM-14 | alta | §3.2 | congelación preventiva de anisakis en el APPCC | FAMILIA (8) |
| DOM-15 | alta | §3.2 | bloque de baja temperatura y envasado al vacío | FAMILIA (8) |
| DOM-16 | alta | §4.4 | hoja «Registro de jornada» + alertas de 12 h y 40 h | FAMILIA (7) |
| DOM-17 | alta | §5.4 §6.6 | una sola cifra de inversión, la del plan financiero | FAMILIA (8) |
| DOM-18 | alta | §5.1 §5.3 §5.6 | 80+ páginas de verdad y tablas ancladas en su capítulo | FAMILIA (8) |
| DOM-19 | alta | §5.5 | business plan modelo relleno, con tablas y proyecciones | FAMILIA (7) |
| DOM-20 | alta | §3.4 | horno mixto, extracción hasta cubierta, extinción, instalación | REPRESENTANTE (patrón a revisar en los 7) |
| DOM-21 | alta | §3.4 | segunda columna «Menú degustación» con la regla de dotación | REPRESENTANTE |
| DOM-22 | alta | §2.3.4 | hoja Financiación con cuadro francés; cuota en el cash flow | FAMILIA (8) |
| DOM-23 | alta | §3.1 §3.5 | bloque «Local»: arrendamiento, fianza, carencia, condición suspensiva | FAMILIA (8) |
| DOM-24 | alta | §7.3 | testimonios con cargos institucionales — para John | FAMILIA (8) |
| DOM-25 | alta | §5.5 | manual de sala con protocolo de alérgenos | FAMILIA (7) |
| DOM-26 | media | §2.3.2 | EBITDA ≠ EBIT, replicado al pl-mensual | REPRESENTANTE |
| DOM-27 | media | §2.3.3 | C35 sin significado | REPRESENTANTE |
| DOM-28 | media | §4.3 | markup vs margen y rotación calculada | REPRESENTANTE |
| DOM-29 | media | §5.4 §7.2.6 | datos Michelin con fuente y fecha; ranking corregido | REPRESENTANTE |
| DOM-30 | media | §4.1 | food cost objetivo decorativo | FAMILIA (8) |
| DOM-31 | media | §5.5 | servir/retirar por la derecha en emplatado; orden de servicio | FAMILIA (7) |
| DOM-32 | media | §5.4 | superficies coherentes: 280-340 m² y vestuarios de personal | REPRESENTANTE |
| DOM-33 | media | §3.4 §5.4 | túnel de lavado vs capota: un solo criterio | REPRESENTANTE |
| DOM-34 | media | §3.4 §5.4 | bloque de cocción con dos escalones de gama | REPRESENTANTE |
| DOM-35 | media | §3.4 §5.4 | fuera Resy; alternativas disponibles en España en euros | FAMILIA (8) |
| DOM-36 | media | §5.4 | matiz de qué evalúa Michelin + Estrella Verde | REPRESENTANTE |
| DOM-37 | media | §3.5 | barras y dependencias del Gantt; tareas de local y financiación | FAMILIA (7) |
| DOM-38 | media | §3.1 | plan de igualdad «50 o más», registro retributivo, acoso, no competencia | FAMILIA (8) |
| DOM-39 | media | §3.4 | limitador acústico, alumbrado de emergencia, vestuarios | FAMILIA (7) |
| DOM-40 | baja | §3.4 §6.5 | recuentos de ítems y «Zwiesel»; sesión de fotos a precio real | FAMILIA (8) |
| COM-01 | alta | §5.1 §6.1 | la cifra de páginas pasa a ser cierta porque el PDF las tiene | FAMILIA (8) |
| COM-02 | alta | §5.1 §5.2 | capítulos con densidad real (≥ 900 palabras cada uno) | FAMILIA (8) |
| COM-03 | alta | §6.2 | la FAQ y el JSON-LD dicen la verdad sobre las fórmulas | FAMILIA (8) |
| COM-04 | alta | §2.1 | ticket medio | FAMILIA (7) |
| COM-05 | alta | §2.2 | pl-mensual | FAMILIA (7) |
| COM-06 | alta | §2.4 | cash flow y break-even | FAMILIA (7) |
| COM-07 | alta | §2.3.1 | plan financiero a 3 años | FAMILIA (7) |
| COM-08 | alta | §4.2 | menu engineering | FAMILIA (6) |
| COM-09 | alta | §5.4 §6.6 | la tabla de CAPEX y el titular dicen lo mismo | FAMILIA (8) |
| COM-10 | alta | §4.4 §5.4 | coste de personal recalculado con SS | FAMILIA (8) |
| COM-11 | alta | §5.5 | BONUS 1 deja de ser un índice | FAMILIA (7) |
| COM-12 | alta | §7.3 | aggregateRating 4,9/8 sin reseñas — para John | FAMILIA (8) |
| COM-13 | alta | §7.3 | ancla de 220/180/90 € — para John | FAMILIA (8) |
| COM-14 | alta | §4.1 | food cost en celda + PVP con y sin IVA | FAMILIA (8) |
| COM-15 | alta | §3.1 | checklist legal vigente: registro de jornada y retributivo | FAMILIA (8) |
| COM-16 | alta | §5.5 | BONUS 2: manual utilizable, no 255 palabras | FAMILIA (7) |
| COM-17 | media | §3.4 §6.5 | equipamiento 54 → 90 ítems | REPRESENTANTE |
| COM-18 | media | §3.4 §6.5 | APPCC, Michelin, vajilla, sala y marketing hasta su cifra | REPRESENTANTE |
| COM-19 | media | §3.5 | el Gantt deja de estar en blanco | FAMILIA (7) |
| COM-20 | media | §4.4 | horas y coste del cuadrante + headcount | FAMILIA (7) |
| COM-21 | media | §4.4 §6.6 | una sola cifra de plantilla en las cuatro superficies | REPRESENTANTE |
| COM-22 | media | §4.3 | budget de bodega: margen, rotación y valor de inventario | REPRESENTANTE |
| COM-23 | media | §5.2 §6.8 | Thermomix y Pacojet existen en el capítulo o salen de la tarjeta | REPRESENTANTE |
| COM-24 | media | §1.11 §5.3 | metadatos del PDF y de los 22 DOCX (Fase A no los tocó) | FAMILIA (8) |
| COM-25 | media | §6.4 | el email post-pago cuenta bien los entregables (20→18+2; casual 16→17) | FAMILIA (2 de 8 mal) |
| COM-26 | media | §5.2 §6.8 | caps. 20 y 21: CRM, alérgenos y evento inaugural | REPRESENTANTE |
| COM-27 | media | §6.9 | el changelog dice lo que fue la v1.1 y añade la 2.0 | FAMILIA (8) |
| COM-28 | media | §3.1 §5.4 | licencia C3 y CIRCE: redacción correcta en los tres sitios | FAMILIA (8) |
| COM-29 | media | §5.4 §6.8 | «Tendencias 2025-2026» → 2026-2027 | FAMILIA (8) |
| COM-30 | media | §2.3.5 §5.4 | fondo de maniobra: un solo rótulo y una cifra calculada | FAMILIA (8) |
| COM-31 | media | §1.9 | los 8 checklists suman su presupuesto | FAMILIA (molde A y B) |
| COM-32 | baja | §2.3.6 | los dos CAPEX se reconcilian sin fusionar libros | FAMILIA (7) |
| COM-33 | baja | §4.1 | la cantidad neta deja de estar huérfana | REPRESENTANTE |
| COM-34 | baja | §3.4 | «Prensa y notoriedad (no influye en la inspección)» | REPRESENTANTE |
| COM-35 | baja | §5.5 | orden de servicio del vino | FAMILIA (7) |
| COM-36 | baja | §5.4 §7.2.6 | datos del sector con fuente y fecha de corte | REPRESENTANTE |
| NUEVO-01 | alta | §2.5 §2.3 | el `P&L Mensual` de los 5 hermanos no tiene ni un total calculado | FAMILIA (5) |
| NUEVO-02 | alta | §2.5 | panadería: EBITDA = facturación (300.000 €) y margen 122,97 % | panadería |

**Recuento: 106/106 del R1 mapeados** (76 de familia, 30 sólo del representante) **+ 2 nuevos = 108**. Ninguno queda sin sección: los que no se
ejecutan están en §7.1 (descartados con motivo) o en §7.3 (para John), y ahí aparecen citados por id.

---

## 9. Plan de ejecución

**Reglas transversales del workflow** (aprendidas a base de perder hallazgos, `feedback_workflow-agentes-sin-schema-devuelven-string.md`): `agent()` **siempre con
`model` explícito** —heredan Fable por defecto, que es caro— y **siempre con schema**; sin schema devuelve un *string* y 15 hallazgos se contabilizaron como
«0». **Nunca recortar los hallazgos inline** (un `slice(0, 40000)` costó 32 el mismo día): los hallazgos van **por fichero**, y al cerrar cada tanda se **cruzan
los ids de entrada contra los resueltos**. El paquete se **commitea aunque esté a medias** al final de cada tanda: este Mac se ha apagado a las 03:20 y lo no
commiteado se pierde.

| tanda | qué | modelo | entregable |
|---|---|---|---|
| **T0 — preparación** | respaldo de los 141 ficheros; `censo-entregables.py --only <pid>` y `gate-flujo-postpago.py --offline --only <pid>` en los 8 para congelar la línea base; volcado de estructura (hojas, celdas, moldes) a `guias-v2_0/censo-base.json` | orquestador | baseline + censo |
| **T1 — motor y grupos del representante** | `motor.py` + `grupo_a.py` + `grupo_b.py` + `grupo_c.py` + `contenido_guia_restaurante_gastronomico.py` + `main.py`, con `--dry-run` a scratchpad | **opus** ×3 (uno por grupo, en serie) | paquete que corre en dry-run |
| **T2 — refutación adversarial del representante** | 3 lentes que intentan REFUTAR, no confirmar: **(a) técnica Excel** (pycel: cada fórmula nueva evaluada, con inputs cambiados, y las demostraciones exigidas de §2-§4), **(b) dominio** (¿un consultor de aperturas usaría esto?, ¿las cifras cuadran entre sí?), **(c) coherencia** (¿lo que ahora dice la landing es cierto abriendo el fichero?) | **opus** ×3 | `auditorias/guias-R2-representante.json` |
| **T3 — corrección** | aplica los hallazgos de T2 al paquete, uno a uno, citando id | **sonnet** | diff + tabla id→fix |
| **T4 — ronda 2** | vuelve a verificar SOLO lo corregido en T3 y **los ids que T2 dio por buenos sin demostrarlo**; cruza los ids de entrada contra los resueltos | **sonnet** | `guias-R3-verificacion.json` |
| **T5 — crítico** | lee el diff completo del representante y firma o devuelve; busca regresiones, casos límite y referencias colgando | **opus** | veredicto |
| **T6 — hermanos** | uno por guía, **en serie**: verifica **cada id del representante** contra su hermano (no lo da por replicado: §2.5 demuestra por qué) + censo propio del fichero + adapta `contenido_<pid>.py` | **sonnet** ×7 | 7 módulos + 7 informes |
| **T7 — documentos** | guiones `guion_<pid>.py` (opus, con el research de §7.2.6 ya resuelto) → **el orquestador ejecuta `bridge.py`** capítulo a capítulo → ensamblado + `guard_no_latinos` → `documentos.py` (maquetado) → gates de §5.6 | **opus** (guion) + bridge (texto) + **sonnet** (ensamblado y erratas) | 8 PDF + 22 DOCX |
| **T8 — capa de producto** | landing, dashboard, changelog, emails, FAQ, JSON-LD y `products-catalog.ts` con las **cifras medidas** en T6 y T7 | **sonnet** | diff de integración |
| **T9 — cierre** | `inject_cache.py`, verificación `data_only`, idempotencia, los tres gates de §6.11 y el de coherencia de cifras; commit y push | orquestador | gate LIVE verde |

**Orden de ejecución real**

1. **Todo en `--dry-run` sobre copias en scratchpad** hasta que T5 firme. `astro-site/public/dl/` no se toca en T1-T5.
2. **Canario**: la primera ejecución real es **un solo fichero** del representante (`pl-mensual-escenarios.xlsx`), se abre, se verifica con `data_only` y se
   compara con su respaldo. Si el canario pasa, el resto del representante; si no, se para.

   Se ejecuta con **`--fichero <nombre.xlsx>`** (`main.py`), que existe justamente para esto: filtra el catálogo del producto a ese fichero, corre la
   idempotencia, el censo y las demostraciones **sólo sobre él** y, en `--dry-run`, deja en la copia de trabajo **ese fichero y ninguno más**. El respaldo
   previo sigue siendo el de la **carpeta entera** (`$CLAUDE_SCRATCHPAD/respaldos/<pid>.bak-<ts>`), que es lo que permite restaurar si el canario falla.
   Antes no existía: `--solo` selecciona GRUPOS (a, b, c), no ficheros, y el único rodeo posible —apuntar `--origen` a una carpeta con un solo xlsx— **moría
   con un `FileNotFoundError` sin capturar**, porque `procesar()` recorre el catálogo que declaran los grupos y no lo que hay en disco. Ese pre-vuelo también
   está: si el catálogo pide un fichero que no está en la carpeta, `main.py` **aborta con exit 2 y la lista de ausentes**, con el informe escrito, en vez de
   reventar a mitad de la escritura.

   **Verificación posterior del canario, en este orden** (ninguno es opcional):

   1. `GUIAS_APPLY=1 python3 main.py --producto <pid> --fichero pl-mensual-escenarios.xlsx --json <informe>` → **exit 0**, `idempotencia.diferencias = 0`,
      `censo_entregables.exit = 0`, `data_only_formulas_nuevas.fallos = []`.
   2. Abrir el fichero **ya escrito** con `data_only=True` y comprobar las celdas clave contra el informe del crítico (no contra la memoria: contra el JSON).
   3. `diff` de las fórmulas contra el respaldo: `python3 - <<'PY'` que cargue las dos versiones y compare hoja/celda/fórmula, para ver **qué cambió** y que
      no haya desaparecido ninguna fórmula preexistente.
   4. `python3 censo-entregables.py --only <carpeta> --fail --quiet` sobre la carpeta REAL (no la copia).
   5. Si algo no cuadra: `shutil.copytree` de vuelta desde el respaldo y **parar**. El respaldo no se borra hasta que el producto entero esté verificado.
3. **Los 7 hermanos, uno a uno y en serie**, con `GUIAS_APPLY=1` y respaldo previo por producto. Entre productos, `istats cpu temp`.
4. **Los documentos van después de los xlsx**, no antes: el texto cita las cifras de los xlsx (§7-bis.7), así que primero tienen que ser correctas.
5. **La capa de producto va la última**, con las cifras ya medidas: el número de páginas se escribe **después** de contarlas, no antes.

**Gates que cierran la meta** (ninguno es opcional): `censo-entregables.py --only <pid> --fail --quiet` = 0 defectos en los 8 · `gate-flujo-postpago.py
--offline --only <pid>` = 141/141 ficheros, 0 fallos · `inject_cache.py` con `fallos_pycel` = 0 **salvo las 10 fórmulas
`SUMPRODUCT`+`IFERROR` de `plantilla-turnos-brigada.xlsx:'Registro de jornada'!C179:C188`**, que son preexistentes (mismo recuento y mismas celdas antes de la
v2.0), evalúan a `""` por diseño y **pycel no sabe evaluar** — el pipeline las separa en `vacias_no_verificadas` y cierra `exit 0`. No es una excepción nueva:
es la redacción exacta de un gate que ya se cumplía así · verificación `data_only` sin resultados en `None` ·
idempotencia (segunda pasada = 0 cambios) · **0 xlsx con 0 fórmulas** salvo los que se declaren explícitamente como formularios en §7 · **páginas del PDF ≥ las
prometidas** en los 8 · **0 caracteres no latinos** en `.md`, `.docx` y PDF · **recuento de ítems de checklist ≥ el anunciado** en cada tarjeta · y el **gate de
coherencia de cifras** cruzando landing, dashboard, email, changelog, xlsx y PDF.

**Lo que NO se hace en local**: builds de Astro, Playwright, navegador. La verificación de producción es por `curl`/gate, como en el resto de la familia.

---

## Decisión ANISAKIS-2026-08-29 — la norma española del anisakis cambió en 2022

Esta SPEC prescribía citar el **RD 1420/2006** —hoy derogado— y un binomio «−20 °C / 5 días» que la norma
nunca contuvo. Las dos cosas están corregidas en el texto de arriba:

- El **RD 1420/2006 está DEROGADO** desde el **22-dic-2022** por la disposición derogatoria
  única.h) del **RD 1021/2022** (ficha de estado del BOE, `BOE-A-2006-22171`). Citarlo como
  derecho vigente es un error que cualquier comprador comprueba en el BOE en un minuto.
- La norma vigente es el **art. 8.1 del RD 1021/2022** (`BOE-A-2022-21681`): congelación a
  **−20 °C o inferior en la totalidad del producto durante ≥ 24 h**, o **−35 °C durante ≥ 15 h**;
  la puede haber hecho una etapa anterior de la cadena **siempre que esté justificado
  documentalmente** (el restaurante guarda el justificante del proveedor). El **art. 8.2** mantiene
  la obligación de informar a la persona consumidora «mediante carteles o cartas-menú».
- El marco europeo no cambia: **Rgto. (CE) 853/2004, Anexo III, Secc. VIII, Cap. III.D**, en la
  redacción del **Rgto. (UE) 1276/2011**.
- Los «5 días» que circulan son una recomendación para congeladores DOMÉSTICOS. El research
  (`auditorias/guias-v2-research-sector.json`, ANIS-06) **no pudo confirmar su atribución a la
  AESAN**: no publicarla con esa atribución.

**Texto canónico de la cita** (adaptando sólo el formato de cada fichero):

> RD 1021/2022, art. 8.1 (que derogó el RD 1420/2006) y Rgto. (CE) 853/2004, Anexo III,
> Secc. VIII, Cap. III.D

**Gate**: `guias-v2_0/motor.py` → `PROHIBIDAS` / `restos_prohibidos()`. Cualquier celda de texto
con «RD 1420/2006» que no vaya precedida de «derogó el» es FALLO en el veredicto de `main.py`.
Fuentes: ANIS-01 a ANIS-05 del research, con URL y cita literal del BOE y de EUR-Lex.
