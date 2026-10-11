# SESSION HANDOFF — 12-oct-2026 · productos digitales (sesión Claude Code, Mac + VPS)

> Todo en `main` (merge del PR #125 `ba24758` + este handoff). Mac y VPS limpios, sin worktrees ni scratch. Regla térmica del
> Mac vigente (istats; ≤ 2 agentes; xlsx/docx y motor solo en el VPS). Detalle: `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md`
> (entrada del 12-oct) y la carpeta `scripts/productos-digitales/parrillero-2_2/`.

## 0. Lo primero al retomar

1. **Routines de correo en la nube** (RemoteTrigger `list_runs`, o https://claude.ai/code/routines):
   - `trig_01WdpgX2KtUL9PbTyXHC4dVg` — **19-oct 08:23Z** — Churrería 13-nov (`395a7eb1`), Bakery EN 14-nov (`68bc8f49`), Paellero 2.2 18-nov (`42ccda21`).
   - `trig_01W3wg4wmuaSrGazNW6mep1u` — **20-oct 15:07Z** — Bar EN 19-nov 14:00Z (`813229ae`).
   - `trig_01WAN2WR9EaRUsi4C2WTqYj9` — **24-oct 08:23Z** — **Parrillero-Asador 2.2 ES 23-nov 08:00Z** (`f8257c43`). NUEVO hoy.
   - Comprobado el 12-oct: los 5 borradores en Resend con su nombre exacto; 14 correos programados del 13-oct al 9-nov.
   - Si una routine falla: programar a mano con la API de Resend (`resend-broadcast.py` / skill `resend-aichef`).
2. Siguiente hueco libre de correos: **ES 28-nov 08:00Z · EN 24-nov 14:00Z**.

## 1. Qué se hizo hoy

- **Plan de Negocio Parrillero-Asador para Eventos ES 2.2 LIVE** (PR #125). Mismo método que el Catering y el Paellero 2.2: F1 con
  2 opus (camino medido en el VPS + research delta), SPEC corta, F2 (implementador opus + calculadora/arreglos sonnet + 2
  redactores sonnet), F3 sonnet en paralelo, 1 revisión opus (0 bloqueantes, 4 MAYOR, 12 MENOR, todo aplicado). ≈ 2,2 M tokens.
- **Corrección transversal (M1)**: la comida testigo es obligatoria en **todos** los eventos de quien vive de los eventos (RD
  1086/2020 art. 30.8.d, verificado en el BOE consolidado). El checklist del **Paellero 2.2 LIVE** lo decía como condición doble
  («más de 40 personas y si…»): corregido en el mismo PR. El Catering 2.2 ya lo decía bien.
- Testimonios (regla de John del 11-oct): solo Federico Aguirre (93 proveedores, sin «validados») y Marcos Pérez (sin «escenario
  mínimo viable»). **Pendiente de decisión de John**: Sandra Vera, rol «Parrillera latina freelance» (no afirma nada del kit;
  se dejó intacta).

## 2. Lo que conviene saber para coctelería y chef privado

- El sello «Versión 2.2 · septiembre 2026» sale de `VERSION_MES` en `planes-v2_0/motor.py` (común). El parrillero lo cambia a
  «octubre» con `parrillero-2_2/par_version.py` + `main_par.py` (parche en proceso); copiarlo si el producto sale en otro mes.
- Comida testigo: formular desde el principio como «todos tus eventos (30.8.d) y cualquier encargo de más de 40 personas (30.8.e)».
- La tabla de cocción heredada de la 1.x (cortes a 52-63 °C) choca con la regla de 70 °C / «poco hecho» a petición: revisar
  manual y carta del producto que toque.
- `gate_restos_ft.py` necesita `--permitir` para los «food truck» legítimos de proveedores/catálogo (ver `parrillero-2_2/F2-NOTAS.md` §6).

## 3. Deuda abierta

- **Línea B pendiente**: coctelería y chef privado → misma 2.2, uno por sesión (proponer a John). Sus tarjetas de hub y su email
  post-compra dicen «DOCX 60+ pp» / «17 CCAA» sin verificar.
- El resto, sin cambios respecto al handoff del 11-oct §3 (planes de línea A con docx 1.1, «60+ páginas» en guías, ChefBusiness
  con Payment Links propios, candidatos EN).
