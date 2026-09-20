# Contrato del molde v2.0 para el generador de la Taquería (F2) — medido el 20-sep-2026

**Referencia canónica = `astro-site/public/dl/kit-tareas/` (kit base, v2.0, NO-CB, con tildes)**, NO el sushi-bar: los
kits sushi-bar / asador / marisquería / tapas-bar / food-truck / panadería siguen en molde **v1.1 de ChefBusiness** (sin
tildes, «Como usar», pie de ChefBusiness, sin `print_area` ni protección). Volcados estructurales: `molde-referencia-base.json`
(kit base: 01, 05, 09, BONUS-01, 08) y `molde-referencia.json` (sushi-bar, solo para nombres de hoja y reparto de ficheros).
Los xlsx generados deben salir **ya en estado post-motor**: `kit-tareas-v2_0/main.py --producto kit-tareas-taqueria --dry-run`
tiene que dejar **0 diferencias** (gate de idempotencia G11). Todo lo que el motor escribe, lo escribe el generador antes.

## 1. Propiedades del libro (todas)
`creator = 'AI Chef Pro'` · `subject = 'Kit de Tareas Recurrentes: Taquería Mexicana · v2.0'` ·
`title = '<Título del fichero> — Taquería Mexicana · Kit de Tareas Recurrentes: Taquería Mexicana'`.

## 2. Hoja `Instrucciones` (primera hoja de los 11 ficheros)
Anchos `A=3`, `B=100`. `print_area = 'Instrucciones'!$A$1:$B$<última fila>`. Sin protección. Texto en columna B:
r2 título (bold, 18, alto 26) · r4 `Cómo usar estas plantillas` (bold 12, alto 18) · viñetas `▸ …` (11, alto 16; 32 si
ocupan dos líneas, wrap) · bloques en este orden con su rótulo bold 12: **Cómo usar estas plantillas** · **Cómo personalizar**
(«Las celdas verdes son editables — cambia responsables y horarios» / «Ajusta las horas límite a tus horarios reales») ·
**Cómo cuenta el contador** (las 3 viñetas literales del base: ✓ cuenta; «N/A» sale del total; el denominador cuenta las
tareas escritas en «Tarea») · **Filas libres** (5 filas verdes DENTRO del rango; insertar dentro, nunca por debajo) ·
**Protección de la hoja** (protegidas SIN contraseña; verdes desbloqueadas; se pueden insertar/borrar filas) · **Se conecta
con** (viñetas que nombran los ficheros hermanos del kit por su nombre de fichero y su papel; el motor lo compone desde
`contexto()`: leer `motor.py` y emitir lo mismo) · línea `— Kit de Tareas Recurrentes · Taquería Mexicana · AI Chef Pro ·
aichef.pro` (bold 12) · bio `Diseñado por John Guerrero — chef y consultor gastronómico desde 2010, en cocina desde los 17
años · johnguerrero.es` (bold 12, alto 35) · `Contacto: info@aichef.pro` · `Versión 2.0 · septiembre 2026 ·
aichef.pro/kit-tareas-taqueria · info@aichef.pro`. Filas en blanco entre bloques como en el base (ver JSON, hoja 0).

## 3. Hoja de checklist (molde P4 de los ficheros 01-08 y del 09 plantilla)
- Anchos `A5 B45 C12 D18 E12 F12 G15`. `freeze_panes = 'A5'`. `print_area = '<Hoja>'!$A$1:$G$<fila del pie>`.
  **Protección activada sin contraseña** (`ws.protection.sheet = True`); las celdas de tarea (A-G de cada fila de tarea y
  de las 5 libres, más B y F de «Verificado por / Firma») van `locked=False`; cabeceras, título, fila 2, secciones,
  contador y pie `locked=True`.
- r1 `Checklist: <nombre de hoja>` (bold, merged `A1:G1`). r2 `Fecha: ___/___/______    Turno: ☐ Mañana  ☐ Tarde  ☐ Noche
  Responsable: _________________` (merged `A2:G2`; los turnos de la taquería: `☐ Comida  ☐ Cena` o los que fije la SPEC).
  r3 vacía. r4 cabecera **`Nº | Tarea | Zona | Responsable | Hora Límite | ✓ Completada | Firma`** (fill `2D2D2D`, bold,
  fuente blanca; `Nº` = `N` + U+00BA). Variantes de la columna E que el motor impone por CONTENIDO (`cadencia()`,
  `motor.py:2261-2325`): valores tipo `Lunes` → cabecera `Día`; el generador emite ya la cabecera que corresponda al
  contenido para que el motor no la reescriba.
- Filas de sección: `  NOMBRE DE SECCIÓN` en A (dos espacios delante, mayúsculas, bold, merged `A:G`, fill claro
  `E3F2FD` o `FCE4EC` como el base). Sin número. Sin DV.
- Filas de tarea: A número **continuo por hoja** (1, 2, 3… sin reiniciar en cada sección), B texto, C zona, D responsable
  SUGERIDO, E hora sugerida `HH:MM`, F vacía, G vacía. Fills: A y B sin fill; **C, D, E, F, G fill verde `E8F5E9`**.
- Al final de la última sección: **5 filas libres** con A-G en `E8F5E9`, SIN número en A, dentro del rango de DV/CF/contador.
- DV en F de cada fila de tarea y de cada fila libre (no en secciones): `type='list'`, `formula1='"✓,—,N/A"'`,
  `allow_blank=True`. Formato condicional sobre `A5:G<última libre>` (copiar la regla del base desde el JSON/`motor.py`).
- Fila vacía · contador: A `Tareas completadas:` · D `=COUNTIFS(B5:B<n>,"?*",F5:F<n>,"✓")` · E `de` ·
  F `=COUNTIF(B5:B<n>,"?*")-COUNTIF(F5:F<n>,"N/A")` (n = última fila libre) · fila vacía · A `Verificado por:` + B verde
  desbloqueada, E `Firma:` + F verde desbloqueada · fila vacía · pie en A: `— Kit de Tareas Recurrentes · Taquería
  Mexicana · AI Chef Pro · aichef.pro` (el segmento del kit IDÉNTICO en los 11 ficheros; `ctx['kit']` lo elige por mayoría).
- Unidades con espacio normal U+0020 (`63 °C`), menos U+2212 (`−18 °C`), nunca U+202F ni U+2011 (idempotencia).

## 4. `09-plantilla-personalizable.xlsx`
Molde P4 de §3 con secciones `  SECCIÓN 1 (PERSONALIZAR)`…, 15 filas libres numeradas NO (van sin número, como las
libres), DV y contador igual. Comparar con `kit-tareas/07-plantilla-personalizable.xlsx` (volcar con `extraer_molde.py`).

## 5. `BONUS-01-briefing-servicio.xlsx`
Hoja `Briefing`: anchos `A5 B30 C50`; r1 `Briefing Pre-Servicio` (bold); r2 `Fecha… Turno… Encargado…`; bloques con
rótulo en B fill `2D2D2D` (bold, blanco) merged `B:C` (`RESERVAS Y OCUPACIÓN`, `PRODUCTO Y CARTA`, `EQUIPO`,
`INCIDENCIAS Y OBJETIVOS`…), filas `Etiqueta:` en B (bold) + C verde `E8F5E9` desbloqueada; `Firma encargado: ____`;
pie. `print_area` A1:C<pie>, protección activada, sin freeze. Contenido de la taquería: reservas/afluencia, trompo montado
(kg, hora de encendido), tortillas previstas, salsas del día y alérgenos, guisados, faltantes, incidencias, objetivo del
turno, mensaje del encargado.

## 6. `BONUS-02-calendario-anual.xlsx` (B1: molde CALENDARIO de la familia NO-CB)
Hoja `Calendario Anual`: anchos `A15 B25 C40 D20`; `freeze A5`; r1 `Calendario Anual — Fechas Clave de la Taquería`;
r2 `Año: ______    Añade tus fechas locales en las filas vacías`; r3 vacía; r4 cabecera **`Mes | Fecha / Evento | Tareas
Clave | Antelación`** (fill `2D2D2D`; `fila_calendario` del motor exige literalmente `Antelación` + `Fecha / Evento`);
filas de datos con fill `F5F5F5` (`Enero | 6 Ene — Reyes | … | 1 semana`), 24-36 filas (2-3 por mes), y al final 2-3
filas `(Tu fecha) | (Añade aquí) | (Tareas específicas) | ` en verde `E8F5E9`; pie. `print_area` A1:D<pie>, protección
activada. Cinco de Mayo con su matiz (D8).

## 7. Cómo se valida el contrato ANTES de escribir contenido
1. El agente de helpers genera UN fichero de prueba (`01`, con 2 hojas y 3 tareas por sección) y lo compara con
   `kit-tareas/01-apertura-cierre.xlsx` usando `extraer_molde.py` → mismos `freeze`, anchos, textos y fills de r1-r5,
   `formula1` de la DV, patrón de las fórmulas del contador, pie, protección y presencia de `print_area`.
2. `main.py --producto kit-tareas-taqueria --dry-run` sobre el kit de prueba: **0 diferencias**. Si el motor cambia algo,
   el generador está mal, no el motor.
3. Solo entonces se reparte el contenido (§3 de la SPEC) a los redactores.
