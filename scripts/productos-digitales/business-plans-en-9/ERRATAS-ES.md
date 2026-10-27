# Erratas del ES LIVE detectadas en la revisión D174 del Wedding Venue EN (27-oct-2026, sesión Claude Code)

> No se ha tocado el ES (`astro-site/public/dl/plan-negocio-finca-eventos-bodas/`). Ninguna es de riesgo legal ni de
> seguridad. Los demás defectos de la revisión (meses de la pizza en O20, «uno de cada cinco», carencia, DataForSEO,
> horas por evento) son solo del EN: en el ES son correctos para su caso (carencia de 1 año, 20 % por intermediarios,
> mezcla de 120 eventos).

| # | Fichero · ubicación | Errata | Propuesta | Riesgo |
|---|---|---|---|---|
| 1 | `plan-financiero-finca-eventos-bodas.xlsx` · `0. Supuestos!A40` y `C40` | La nota dice que el «IVA repercutido/soportado general» (21 %) «es el de todo lo que factura la finca (espacio, servicios y canon) y el de casi todo lo que compra», pero **solo lo lee `PyG 3 Años!G14`** (IVA del coste del canon, que es 0). Los tipos que de verdad se aplican son los tecleados en `PyG 3 Años!G10/G11` y en la columna G de cada coste: quien cambie B40 no cambia nada | `C40`: «Solo de referencia: el IVA de cada línea se teclea en la columna de IVA de «PyG 3 Años» (G10 espacio y servicios, G11 canon; cada coste en su fila).» | Ninguno (claridad) |
| 2 | Motor común (todos los planes ES y EN) · `Punto Equilibrio!E24` y la «holgura» de los Word | La holgura es `B23/B20 − 1` (invitados del plan sobre los de equilibrio: 22.9 % en el ES), pero la nota dice «Cuánto puedes caer antes de no poder pagar…»: la caída real hasta el equilibrio es `1 − B20/B23` (18.6 % en el ES). Coherente entre Word y Excel, solo sobrestima la lectura | Nota: «Cuánto están tus ventas por encima del equilibrio de caja; la caída que aguantas es 1 − equilibrio / plan». Decisión de motor: tocarlo es tocar los ~50 planes | Ninguno (definición) |
