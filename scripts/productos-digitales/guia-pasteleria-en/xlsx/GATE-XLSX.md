# Gate de los 8 xlsx EN (VPS, 17-oct-2026) — 6 de 8 libros OK; 3 diferencias aceptadas

`gate_xlsx_en.py ../../guia-pasteleria/build /root/pastry-en --cache` tras `aplicar_en.py` + `inject_cache.py` + `cache_manual.py`.

| Libro | «Error» | Por qué se acepta |
|---|---|---|
| equipment-and-suppliers-checklist | Counter!B21 «No: missing 19 critical lines» ≠ «No: faltan 19 líneas críticas» | cadena compuesta por la fórmula (literal + número + literal): es su traducción, mismo número |
| 3-year-financial-plan | Startup Investment!B23 EN 0 ≠ referencia 7 | adaptación declarada: «¿lleva IVA?» Sí → No en D6:D15 (config `texto`); la referencia del gate solo aplica números |
| 3-year-financial-plan | 12-Month Cash Flow!B32 sin evaluar por pycel (×4 líneas) | pycel no evalúa esa fórmula, tampoco en el ES; caché puesta a mano (`cache_manual.py`): «More than 3 years», comprobado: 24,230 + 47,186 + 50,357 < 227,916 |
