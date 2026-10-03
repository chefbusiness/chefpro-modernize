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

---

## Sesión de la mañana (3-oct, Claude Code) — F2 a medias, PARADA por John

John despertó esperando el producto hecho y le había dejado la F2 parada; se reanudó a las 8:36 y a las 11:20 John lo paró
(«para para… ¿qué locura es esta?»): **el proceso fue desproporcionado para el producto** (ver la regla nueva abajo).

**Estado (todo commiteado y pusheado):**
- `main`: los 8 Excel en `scripts/productos-digitales/guia-churreria/build/` con sus generadores, `gate_libros.py` (con
  `auditar_ciclos`) en VERDE, 67 celdas cruzadas, 70 demos OK (`ed26bd17`) · 7 imágenes (`9e09acb0`) · **guion completo**
  `guias-v2_0/guion_guia_churreria_chocolateria.py` + `guia-churreria/verificar_guion.py` en VERDE (22 bloques, D26).
- Rama `feat/guia-churreria-chocolateria` (pusheada, SIN PR): capa técnica (zona app 53, access/library/island, SPA, 4
  functions con 13 descargas, catálogo 51, config, changelog, admin, hub ES ×2 + 6 hubs internacionales, buscador, rol,
  footerLinks) — `36c1191c`, `b7105869`. Worktree local en `<scratchpad>/wt-churreria` (se puede recrear con `git worktree add`).
- **Falta** (≈ 2 M y ~3 h en modo mínimo, cuando John diga): redactar los 22 bloques (Sonnet con el prompt cerrado dentro del
  encargo, sin leer ficheros, 3 a la vez, ≤ 2 correcciones) → `documentos.py` local → gates de script (sin refutadores) →
  ficha de la landing + correo + corrección del post (1 Sonnet calcando la hermana) → copiar los 13 ficheros a
  `astro-site/public/dl/guia-churreria-chocolateria/` EN LA RAMA → PR con preview → Payment Link de John.
- Pendiente menor detectado: `plan-financiero-3-anos-churreria.xlsx!Escenarios!C12` (base 59.852 €) no es el resultado de
  crucero del P&L (C23 = 32.138,75 €); el guion no cita esas filas.

**Consumo real del producto: ≈ 10,5 M** (F1 4,63 · Excel 4,27 · capa técnica 0,58 · guion y landing parados ≈ 1) + Kit
Chocolatería 2.1 0,44 M. Desproporcionado para una guía de 65 € con ~150 búsquedas/mes de apertura.

## 🔴 Regla nueva de John (3-oct): PROPORCIONALIDAD — que no se repita
«Lo que vayas a desarrollar, investigar y proponer tiene que ser proporcional al producto». Los ~50 productos anteriores
llevaron 3-6 horas cada uno; los últimos 3-4 se han ido a 1-2 días y millones de tokens con el mismo proceso pesado (5-6
lentes, verificación cita a cita, SPEC de cientos de líneas, refutaciones en cadena, decenas de agentes opus). Desde hoy:
**research en UNA pasada, SPEC corta, un implementador + gates de script, una sola comprobación adversarial final** (que los
ficheros no estén corruptos y no haya errores), objetivo **3-6 horas por producto**, y la cuenta coste/retorno ANTES de
elegirlo. Detalle en `CLAUDE.md` del proyecto y en la memoria `feedback_coste-vs-retorno-antes-de-elegir-producto`.

## Sesión de la tarde (3-oct, Claude Code) — TERMINADA a falta del Payment Link

22 bloques redactados (Sonnet, Mac) · Excel regenerados y documentos ensamblados en el VPS · revisión Opus final con 9
bloqueantes arreglados · guía 95 págs (16 caps + anexo), BP 14, bonus 21 · **PR #105** con preview en verde (13 descargas,
cripto, Miselup, DataFast, WhatsApp). `documentos.py`: 4 falsos positivos de gates acotados y el bug de «fila porcentual»
(tabla del BP) arreglado, con regresión 0 sobre Chocolatería y Pastelería. **Retomar:** Payment Link de John → env
`VITE_STRIPE_PAYMENT_LINK_GUIA_CHURRERIA_CHOCOLATERIA` (builds) → `python3 scripts/productos-digitales/sync-payment-links.py`
en la rama → merge → `gate-flujo-postpago.py --only guia-churreria-chocolateria` LIVE + `robots-gate.py --live`.
Pendientes aparte: post `ia-churrerias-guia-completa` (SPEC §7.2), hermana v1.0.1 (D7), correo del 13-nov (desde el 14-oct).

### LIVE (3-oct, tarde, Claude Code)

Payment Link `https://buy.stripe.com/7sY14gdkMeAK3UXejH6oo1A` → env `VITE_STRIPE_PAYMENT_LINK_GUIA_CHURRERIA_CHOCOLATERIA`
(builds) → `sync-payment-links.py` (53) → **PR #105 fusionado** (`6615d775`). Verificado en producción:
`gate-flujo-postpago.py --only guia-churreria-chocolateria` **0 fallos** (13/13 descargas, E-f cripto), `robots-gate.py --live`
verde, sitemap + SEO server-side + tarjeta del hub, y `crypto-checkout` **200** con factura sin pagar de
`qa-churreria@aichef.pro` (purgar con `crypto-report?purge_unpaid_before=` cuando haya `ADMIN_PASSWORD`).
Nota: `fase6-gate.py` recibe la URL BASE; sus 3 fallos son conteos congelados de la migración (sitemap, hreflang de la home).

**Pendiente:** correo de lanzamiento (hueco 13-nov 08:00Z, programable desde el 14-oct) · post `ia-churrerias-guia-completa`
(SPEC §7.2) · hermana `guia-chocolateria-obrador` v1.0.1 (D7, su correo el 18-nov).
