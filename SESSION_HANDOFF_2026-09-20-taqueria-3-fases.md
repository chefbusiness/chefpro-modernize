# Handoff 2026-09-20 — Política de 3 fases + «Tareas Recurrentes: Taquería Mexicana» (sesión Claude Code)

Producción = `main`. Política nueva de John (decisiones delegadas a Claude): `CALENDARIO-V2-SEMANAL.md` §3 y `CLAUDE.md`.

## F1 Fundamentos — CERRADA (gate de script en verde)
- Research `kit-tareas-taqueria/01-research-taqueria-mexicana.md` (601 líneas) · SPEC `02-SPEC-kit-tareas-taqueria.md`
  (862 líneas; refutada en ronda única → 24 correcciones aplicadas → `gate_f1_spec.py` PASS) · contrato del molde v2.0
  `03-contrato-molde-v2.md` + volcados `molde-referencia*.json` (`extraer_molde.py`).
- Decisiones: 14 € / `priceOld '€69'`; BONUS-02 en molde calendario NO-CB; 300 tareas (270-330) en 22 hojas; molde
  canónico = kit base v2.0 (sushi-bar y 5 más siguen en v1.1 CB); Mega Pack fuera; env `VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA`.
- Consumo F1: research 0,24 M · SPEC 0,21 M · refutación 0,28 M · fixer 0,28 M = **1,0 M** de los 2,5 M del producto.

## F2 Entregables — EN CURSO
- Paso 1 (en marcha al cerrar F1): helpers de `scripts/generate-tareas-taqueria.py` contra el contrato + `comparar_molde.py`
  + idempotencia `kit-tareas-v2_0/main.py --producto kit-tareas-taqueria --dry-run` (0 diferencias).
- Paso 2: contenido de las 22 hojas por redactores Sonnet (≤ 3 agentes, ~4 ficheros cada uno) siguiendo SPEC §3-§4.
- Paso 3: gates §5 (`censo-entregables --fail`, `gate-no-latinos`, tildes, 63/74 °C, idempotencia) → commit «F2 cerrada».
- Cómo retomar si se corta: `git pull`, leer este fichero y `03-contrato-molde-v2.md`; comprobar si existe
  `scripts/generate-tareas-taqueria.py` y correr `--prueba` + `comparar_molde.py`.

## F3 Producto y lanzamiento — PENDIENTE (checklist en SPEC §6)
