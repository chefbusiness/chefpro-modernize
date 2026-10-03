# Handoff 3-oct-2026 (sesión Claude Code, Mac) — Churrería-Chocolatería F1 cerrada · Kit Chocolatería 2.1 LIVE · correo Taquería programado

John arrancó la sesión («retomamos el desarrollo de nuevos productos… con cuál seguimos, revisa todo»), delegó todo
(«pasa del VPS de momento, decide tú con todo lo demás») y se fue a dormir («avanza con todo lo que puedas sin mí»).
Térmica: vigilante en bucle toda la sesión, pico 62,3 °C, ningún proceso congelado; nunca más de 2 agentes a la vez.

## 🔴 Lo único que necesita a John

**F2 de la Churrería está PARADA por presupuesto** (política de 3 fases: «si supera su techo un 30 %, se para y se reporta»).
F1 costó **4,63 M** medidos (estimada 3,26) y la proyección del producto con la F2 tal cual es **14,06 M**, por encima de la
parada de 13 M (techo L = 10 M). Opciones (detalle en `scripts/productos-digitales/guia-churreria-SPEC.md` §9.1):

| Opción | Qué es | Total |
|---|---|---|
| A | Mismo producto, 22 bloques de redacción en vez de 26, refutación de libros en una ronda | ≈ 13,2 M (sigue por encima) |
| **B — recomendada** | A + **7 libros** (el del aceite pasa a hojas del libro de escandallo) + 16 capítulos + anexo (≈ 80-85 págs) + refutación de documentos en una sola ronda | **≈ 12,8 M** |
| C | Aplazar F2 y hacer antes un producto M/S de la cola (Plan Heladería ≤ 5 M o un kit S ≤ 2,5 M) | — |

Con A o B sigue la regla de control: medir tras las dos primeras tandas de redactores y parar si vuelve a pasar de 13 M.
**Si John responde «decide tú»: B.**

## 🔴 Recomendación para la PRÓXIMA sesión (antes que la rotación): la deuda del anisakis, abierta desde el 6-sep

Comprobado hoy en los ficheros publicados (siguen vivos en producto vendido):
- `kit-tareas-sushi-bar/03-seguridad-anisakis-appcc.xlsx` → «RD 1420/2006» (derogado) y «7 días»;
- `kit-tareas-marisqueria/03-trazabilidad-appcc-marisco.xlsx` → «RD 1420/2006»;
- `kit-inventario/04-recepcion-mercancias.xlsx` → «RD 3484/2000» (derogado).
Lo vigente: RD 1021/2022 art. 8.1 (−20 °C ≥ 24 h o −35 °C ≥ 15 h). No es inseguro (7 días a −20 °C es más estricto), pero son citas
derogadas en documentos de autocontrol que vendemos. Alcance S, por el generador de cada kit + `inject_cache` + censo + changelog +
correo en la cola; en el Kit de Inventario se juntan los defectos D23 que destapó el EN («RT-08:» en `BONUS-09!Parámetros!C12`,
«8 plantillas» donde son 7, `TODAY()` contra fechas fijas). No lo empecé hoy: serían tres productos más en una semana que ya lleva dos.

## Hecho

1. **Correo de lanzamiento de la Taquería PROGRAMADO** (estaba en ventana desde el 29-sep sin programar): 29-oct 08:00Z,
   `2e4b4d68-30e7-4962-b9d6-6376ca20e4e3`.
2. **Kit de Tareas Chocolatería 2.1 LIVE** (PR #104 → `1eb58b26`; el plazo era el 24-oct): los ocho alérgenos del Anexo II en
   las tres celdas de declaración y la humedad del obrador en 50-60 %, por su generador. El motor de la familia Kit de Tareas
   gana versión por fichero (`VERSIONES` / `version_de`, sin tabla = salida idéntica; regresión 0 en cafetería, hotel y
   heladería). Gates: censo 0, no latinos 0, post-pago LIVE 11/0/0, landing «Versión 2.1 · octubre 2026». Prueba del correo a
   John `01a0ffd4-…`. Coste 0,44 M.
3. **«Cómo Montar una Churrería-Chocolatería» (producto 51, L, 65 €, `guia-churreria-chocolateria`) — F1 CERRADA:**
   - Research de 5 lentes + síntesis + refutación (`auditorias/guia-churreria-*-2026-10-03.md`) — 2,11 M.
   - 25 decisiones firmadas: `scripts/productos-digitales/guia-churreria-DECISIONES-2026-10-03.md`.
   - 202 fichas (46 CUN con 150 citas literales comprobadas, 156 CUS) + V-01…V-06 cerradas; JSON común 635 → 837.
   - SPEC refutada (3 altas · 12 medias · 6 bajas, 21 arreglos) y gate de cifras vetadas en verde:
     `scripts/productos-digitales/guia-churreria-SPEC.md`. — 1,66 M.
   - Juego de datos «Churrería-Chocolatería **El Molinete**» (`guia-churreria/datos_ejemplo.py`, 3.579 líneas,
     `comprobar()` en verde, 15 defectos inyectados cazados, gate de tildes 0). — 0,86 M.
   - Commits `c4449f1d`, `d419934d`, `079eca66`.
4. Memoria: regla térmica todo el año; VPS aparcado (John avisará cuando lo actualice entero); galería de capturas en pausa;
   índice de memoria recortado bajo el límite.

**Consumo de subagentes de la sesión: 5,07 M** (Churrería 4,63 · Kit 2.1 0,44).

## Hallazgos que valen dinero (de la investigación)

- La **hermana** (`guia-chocolateria-obrador`, 65 €, LIVE) publica un **margen del churro del 85-90 %** (pág. 9 del PDF y
  `calculadora-capex-chocolateria.xlsx`) atribuido a una fuente que dice «>60 %», y su `PyG 3 Años!B68` dice que la taza y
  los churros «restan» cuando el neto sube de 17.269 € a 20.044 €. Se arregla en su **v1.0.1 durante la F3 de la Churrería**
  (D7), junto a la nota-puente del cap. 12 (sobra con el kit 2.1) y la venta cruzada. Un solo correo.
- **Pack APPCC 09** (control de aceite) lleva 180/25/20 como constantes dentro de la fórmula y marca CAMBIAR por encima de 180 °C
  sin norma detrás: deuda para una sesión v2.x (D8).
- `kit-tareas-food-truck/04` pide «Registro sanitario del vehículo (RGSEAA)» cuando el RD 1021/2022 deja al minorista en el
  registro autonómico: revisar en su próxima v2.x.
- El **convenio de hostelería de Madrid venció el 31-12-2025** y se negocia el nuevo: riesgo de caducidad para cualquier
  producto que publique sus tablas (Manual del Manager, kits de personal…).
- El changelog del **Mega Pack** (`get-download-urls.ts:1403`) sigue en 1.1 del 22-ago: nunca recoge las versiones de sus kits.
- Señal de ventas: el 1-oct salieron dos correos «Tu acceso al Kit de Escandallos Pro».

## Pendientes con fecha (los puede hacer cualquier sesión)

| Desde | Qué | Comando |
|---|---|---|
| **4-oct 08:00Z** | Programar **Escandallos 2.1** para el 3-nov 08:00Z | `python3 scripts/productos-digitales/emails/resend-broadcast.py --html scripts/productos-digitales/emails/broadcast-kit-escandallos-v2.1-es.html --subject "Kit de Escandallos 2.1: test de rendimiento y lista de precios" --name "Actualización Kit de Escandallos 2.1 (ES)" --scheduled-at 2026-11-03T08:00:00Z` (el asunto de la prueba del 24-sep no quedó anotado: este es propuesto desde su preheader) |
| **9-oct 08:00Z** | Programar **Kit Chocolatería 2.1** para el 8-nov 08:00Z | `… --html …/broadcast-kit-tareas-chocolateria-v2.1-es.html --subject "Kit de Tareas Chocolatería 2.1: los ocho alérgenos, uno a uno" --name "Actualización Kit de Tareas Chocolatería 2.1 (ES)" --scheduled-at 2026-11-08T08:00:00Z` |
| 14-oct | Hueco del lanzamiento de la Churrería: 13-nov 08:00Z (solo si F3 está LIVE) | — |

## Cómo retomar la F2 de la Churrería (cuando John elija)

1. `git pull --ff-only` · `istats cpu temp` · vigilante en bucle:
   `nohup zsh -c "while true; do zsh scripts/termica/watchdog-termico.sh <scratchpad>/watchdog; done" >/dev/null 2>&1 &`
2. Si es **B**: firmar D26 en `guia-churreria-DECISIONES-2026-10-03.md` (7 libros, 16 caps + anexo, bloques y rondas) y
   ajustar §2, §4 y §9 de la SPEC (una pasada sonnet + gate de script), y regenerar `datos_ejemplo.py` si cambian los
   `CRUCES` (el libro 4 desaparece: X3 y X4 se reabsorben en el 3).
3. Libros: constructores en pares (SPEC §2.5), calcando `guia-chocolateria/gen_*.py` + `_comun_*.py`; `gate_libros.py` con
   el `auditar_ciclos()` nuevo (D16); `inject_cache`; refutación de libros en una ronda.
4. Guion (D25: después de los libros, porque cita sus celdas) → `dump_prompts.py` → redactores sonnet de 2 en 2 →
   `check_bloque.py` → `documentos.py` → refutación de documentos (una ronda, 3 lentes en un prompt) → `paginas-gate.py`.
5. Máquina: el Mac, en serie (VPS aparcado por John).

Sesión Claude Code · `Via: Claude Code`.
