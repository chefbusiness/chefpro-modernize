# Burger Restaurant Business Plan Kit (EN, $39) — F3 (revisión adversarial de la capa comercial) · notas
> Sesión Claude Code, 31-oct-2026. Rama `feat/burger-restaurant-business-plan-en` (PR #196). Una ronda, sin build ni navegador en el Mac.
> Contraste: volcados en el VPS (`volcar_en.py` + calculadora) frente a ficha, dashboard, tarjeta del hub, correo y entrada de PAYMENT_LINKS.

## 1. Veredicto: 0 B · 2 M · 5 m, todo arreglado en la capa comercial (los entregables no se tocan)
- **M1 · Australia**: la FAQ de UK/Canada/Australia decía «the plan has short notes for the UK and Australia»; el Word (párr. 108) solo trae la
  nota UK. Ahora «a short note for UK readers» (Australia y Canadá quedan en la guía de equivalencias y en las celdas editables).
- **M2 · Relleno de FAQ**: 26 → **23**. Fusiones: moneda → UK/Canada/Australia; «clientes / más de un negocio» → suscripción; acrilamida →
  fries y aceite (comparten la misma respuesta: sin límite federal, Prop 65 solo California). Las PAA de F1 §3 (30/30/30, $20k, small
  restaurants make money, coste de la smash) siguen con FAQ propia.
- m1 · «over-portioned balls» no estaba en la hoja: la hoja dice bolas, panes y salsas tiradas al cierre, staff meals, comps, errores y
  reembolsos de marketplaces; la FAQ del 34 % vs 25.7 % ahora lo cita así.
- m2 · «test your packaging and vent it» → lo que dice el Word (párr. 74): fries en envase ventilado y fritas las últimas, techo del 19 %.
- m3 · $20k: «pop-up, ghost kitchen or take-out shop» → lo que describe el Word: ghost kitchen, burger bar con servers, truck.
- m4 · Camión: «different license, a commissary» no está en los entregables → «a different business».
- m5 · Correo: «the kit promises no liquor license» (ininteligible) → «the kit does not promise any license».

## 2. Hood cleaning (la frecuencia)
Checklist fila 13 de Phase 6, Word párr. 103 y hoja Startup Costs D14: «NFPA 96: quarterly with heavy grease, twice a year if moderate, ask the
fire marshal»; el Excel presupone trimestral en Mantenimiento (A27). La landing ya lo decía «en el ejemplo»; se retoca para que nunca lo
afirme como regla: FAQ («so ask your fire marshal»), rejilla («quarterly in the example, per NFPA 96») y «why» («its NFPA 96 cleaning schedule»).

## 3. Verificado sin cambios (con celda/párrafo)
- Cifras: todas las de `CASO` = `cifras_caso.json`; calculadora = `cifras_calculadora.md`; personal $365,416 / 12 puestos / 9.05 FTE, pagos
  $15.50 / $17 / $21 (Staffing J9/J6/J8), dueño $4,500 (J5), pesimista $23,372 y optimista $229,781, rent 4.7 %, EBITDA 14.5 %.
- Conteos: Word 10 secciones; Excel 9 hojas (Assumptions, Startup Costs, 3-Year P&L, Break-Even, Scenarios, Staffing, Instructions,
  12-Month Cash Flow, Financing); checklist 80 tareas = 12 + 15 + 14 + 13 + 13 + 13 en las 6 pestañas `Phase 1 - Business Setup` … `Phase 6 -
  Opening & 90 Days` (+ Instructions); calculadora 4 hojas (Beef & Patty, Fries & Oil, Costing, Instructions), 14 productos.
- Legal: 155 °F 17 s para toda smash (Word 104, checklist P3 fila 10); consumer advisory solo cooked-to-order (Word 105, P3 fila 12); grinding log
  «good practice», no obligatorio (checklist P1 fila 7, P3 fila 7); sin límite federal de TPM ni de acrilamida, Prop 65 en California (P3
  filas 13-14); 9 alérgenos con sesame (Word 106); «gluten-free» desaconsejado (P4 fila 17); la smash viaja peor (Word 74).
- Sin € ni «comensal» ni ley española ni restos del Sushi; 14 enlaces internos del footer y los 5 del correo existen como páginas EN.
- Dashboard: 5 ficheros, claves y títulos coinciden con la ficha y con `get-download-urls`. Tarjeta del hub: 80 tareas / 9 hojas correctas.
- PAYMENT_LINKS: descripción de 234 caracteres, prosa, sin bullets.

## 4. Gates
esbuild de la ficha OK (el dashboard no se tocó) · `sync-product-prices.py --check` OK · `tienda-gate.py` VERDE · `nombre-gate.py`: único ✗ =
`ai-prompts-for-restaurants` (roto también en main).
