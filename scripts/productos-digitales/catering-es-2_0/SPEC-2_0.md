# Plan de Negocio Catering Temático Eventos ES — SPEC 2.0 (F1 · 11-oct-2026 · sesión Claude Code)

> Base: `F1-camino-2_0.md` (camino de construcción medido y ensayado) y `F1-research-es.md` (marco legal/fiscal y caso
> España con fuentes). Defectos de la 1.x: `../business-plans-en-4/F1-inventario-delta.md` §2 (L1-L16). Encargo de John
> (11-oct): dejar el catering ES «conforme a los estándares de calidad», reutilizando el motor del EN. Versión **2.0**
> (cambia el modelo). Presupuesto F2 + F3 ≤ 2 M tokens (F1 gastó 0,38 M). **Fecha dura: LIVE antes del martes 13-oct
> 08:00Z** (correo de la 2.0 a esa hora, decisión de John). Lo que no está aquí no se hace.

## 1. Construcción (D1-D3)

| D | Tema | Decisión |
|---|---|---|
| D1 | Camino | **A** de `F1-camino-2_0.md`: motor ES de línea A (`planes-v2_0/main.py` + `grupo_a.py`) sobre una copia del **Food Truck ES v2.2**, con módulo nuevo `contenido_plan_catering_tematico_eventos/a.py`, `semilla_cat.py` (títulos y filas del checklist) y copias locales del ensamblador del docx (`docx_cat_es.py`) y de la calculadora (`calculadora_cat_es.py`) en `catering-es-2_0/`. Único cambio en código común: **`compilar_vocabulario`** de `grupo_a` (frases y tildes, ~6 líneas) con gate de regresión: **los 5 planes de línea A dan 0 diferencias de huella frente a `dl/`** |
| D2 | Motor de ingresos | **Sin permutar** (F1 §1): cubiertos/día = **invitados por evento**, ticket = **precio por invitado sin IVA**, días = **eventos al año**; rótulos SIEMPRE por `VOCABULARIO` (no por `SUPUESTOS`). El punto de equilibrio del libro sale en invitados por evento; el docx da también los **eventos/año de equilibrio** con un token derivado de las cifras del Excel |
| D3 | Ficheros | Mismos nombres de fichero y mismas 11 piezas (no se toca `get-download-urls.ts`). Se REHACEN: plan financiero xlsx (9 hojas), checklist xlsx (6 hojas), calculadora xlsx (hojas con los nombres que exige `motor.detectar`: F1 §1) y docx del plan. Los otros 7: solo arreglos de texto (D9). `96 proveedores` no se renombra |

## 2. Caso España y fiscalidad (D4-D6)

| D | Tema | Decisión |
|---|---|---|
| D4 | Caso | `F1-research-es.md` §3 tal cual: **130 eventos · 53 €/invitado sin IVA · 65 invitados**, crecimiento 12 % / 8 %, comida/bebida 82/18, mercancía 30/28 %, consumibles 3 %, varios 3 %, cocina central compartida 2.000 €/mes, 5 puestos (dueño, jefe de cocina, ayudante-conductor, coordinador al 0,5, extras **fijos discontinuos**), inversión ≈ 67.000 € en 15 partidas, 35.000 € propios + préstamo **CALIBRAR** (≈ 105.000 €, 6,5 %, 6 años, 1 de carencia), cobro 25 días, pago 30, estacionalidad del research. Regla D15: holgura del equilibrio ≥ 15 %; si no, subir eventos de 10 en 10 hasta 160 y reportar |
| D5 | IVA | **10 %** en todo el catering con servicio, alcohol incluido (Ley 37/1992 art. 91.Uno.2.2.º; DGT V0499-26 y V0591-25: citar la consulta original). El canal `pct_delivery` del motor = **«Drop-off sin servicio»** (ahí el alcohol al 21 % es correcto); el canon de fincas / wedding planners va en `pct_varios` (research D1). Servicios facturados aparte (mobiliario, carpas, decoración): 21 % — nota, no línea |
| D6 | Personal y caja | Extras de eventos = **fijos discontinuos** (art. 16 ET), nunca «freelance»; SS empresa 30,65 % + AT/EP (el 33 % del motor vale). Anticipos de particulares (40 %) **no modelables** (`dias_cobro` ≥ 0): nota en caja que mejoran la caja real |

## 3. Checklist, docx y calculadora (D7-D8)

- **D7 Checklist: 82 tareas 12/15/14/10/16/15** (F1 §2). Se conservan las obligaciones españolas reales (IAE, RGPD, LSSI, modelos 390/347/349 en una tarea, Hosply), multicocina condensada en 2. **Verificar con fuente primaria antes de escribir** (y citar en la nota): registro **autonómico por declaración responsable** frente a RGSEAA (RD 1021/2022 DF 1.ª → art. 2.2 RD 191/2011), desistimiento B2C en servicio con fecha (art. 103.l TRLGDCU), epígrafe IAE, ATP de la furgoneta (RD 237/2000 / RD 2483/1986). Cocina central autorizada en F2 (contra L9); prohibido cocinar en casa (RD 1021/2022 art. 13.5.b).
- **D8 Docx: reescritura** en las 131 ranuras del FT ES (10 Heading 1, A4), ~6.700 palabras, **todas las cifras por token** del Excel 2.0; identidad del producto intacta (**catering temático multi-concepto con estaciones temáticas en directo**); fuentes por ranura según F1 §3 (gemela EN, docx 1.x, legal del FT ES, política comercial de los contratos: B2C 40 % + 21/7 días + 48 h; B2B 40/30/30 + 28/14/7). Fuera las cifras sin fuente de la 1.x (4.585 M€, 25.183 €, 38/58/73 %) salvo verificación.
- **D8b Calculadora ES** (F1 §4): copia adaptada de `calculadora_cat.py` — IVA 10 %, precio a particulares con IVA incluido, sin service charge ni sales tax, propina voluntaria fuera del total, anticipo 40 % y tramos de cancelación, recargo por km ida y vuelta, **nº de estaciones temáticas** como entrada, margen calculado, 3 ejemplos por fórmula, autotest pycel.

## 4. Resto del producto y lanzamiento (D9-D12)

- **D9 Otros 7 ficheros** (solo texto, lista de F1 §5): «freelance» → personal fijo discontinuo / ETT; fuera «validado(s) España 2026»; inversión alineada con el modelo; RGSEAA → registro autonómico donde toque; contrato B2B p76 (21 % de servicios asociados: correcto solo si se facturan aparte → aclararlo); plantilla de proveedores: columna «Validado» → «Estado» con «Por verificar».
- **D10 Landing ES + dashboard** (F1 §6): corregir todas las afirmaciones listadas (inversión, break-even, «5-9x menor», «60+ pp.», «6 hojas», tickets, «10 ejemplos validados», «freelance», «110 hitos» → 82 tareas, tarifa plana, anexo 17 CCAA, cifras sin fuente, «contactos verificables», microcrédito/ICO) con lo que entrega la 2.0; `updateNote` «Producto actualizado · Versión 2.0 · octubre 2026»; entrada honesta en `productos-changelog.ts`; descripciones del dashboard. **Capa comercial intacta** (precio tachado, testimonios: decisión de John para la tienda ES). Las cifras que un parche puede mover (payback, DSCR, saldos) no se citan en la landing ni en el correo.
- **D11 Correo**: plantilla de actualización (`emails/broadcast-kits-tareas-v2-es.html` como molde; saludo «Hola, colegas»), prueba a John y **programado el martes 13-oct 08:00Z** en cuanto la 2.0 esté LIVE.
- **D12 Gates**: los del motor (13/13), idempotencia, censo, no latinos, regresión 5 planes = 0 diferencias, autotest de la calculadora, cifras de la 1.x prohibidas (research D4), docx (10 H1, A4, sin tokens sin resolver), barrido de «freelance» / «validado» / «España 2026» en los 11 ficheros. **Una** revisión opus final (recalcular a mano, abrir 3 fuentes legales, leer checklist y docx enteros). Después: `gate-flujo-postpago --only plan-catering-tematico-eventos` en preview y LIVE.
