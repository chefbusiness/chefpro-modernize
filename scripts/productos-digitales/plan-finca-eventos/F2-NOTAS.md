# Plan de Negocio: Finca de Eventos y Bodas ES 1.0 — F2 (motor) · calibración, decisiones y gates

> Sesión Claude Code, 25-oct-2026. Implementador del MOTOR de la F2 (plan financiero + checklist). SPEC: `SPEC.md`
> (D1-D14); cómo: `F1-camino.md` §1-§3; caso: `F1-research-finca.md` §3. Código en el Mac; motor y xlsx en el VPS
> (`/root/wt-finca`, venv `/root/venv-guias`, salidas en `/root/tmp-fin-f2/`). Cero código común (SPEC D3): ni
> `motor.py`, ni `grupo_a.py`, ni `main.py`, ni el pid en `PRODUCTOS`.

## 1. Ficheros

| Fichero | Qué es |
|---|---|
| `planes-v2_0/contenido_plan_negocio_finca_eventos_bodas/{__init__,a}.py` | Contenido: `a.py` del parrillero 2.2 (motor de eventos) + injertos de la heladería (renta real, obra, Mes 1 girado, pagas, `IVA_COMPRAS`, `COBERTURA` de 4 claves, `RECALIBRADO = ()`) |
| `plan-finca-eventos/semilla_fin.py` | `semilla_hel.py` sobre la panadería 2.2: 19 partidas, 10 fijos, títulos, `PyG!G10:G11` y `G13` por valor (21 %), `H4:H11` vacías, checklist y docProps |
| `plan-finca-eventos/datos_checklist.py` | 84 tareas: 12 · 16 · 15 · 13 · 14 · 14 (constitución · finca y licencia · obra · personal y catering · marca y reservas · temporada) |
| `plan-finca-eventos/main_fin.py` · `ciclo.sh` | `main.py` con `fin_version.py` (1.0 · noviembre 2026) · semilla → motor `--dry-run --solo a` |
| `plan-finca-eventos/cifras_fin_es.py` | 155 tokens para el Word (`cifras_caso_es.json`) + gates D9 + prueba de D4 leída del xlsx calculado |
| `plan-finca-eventos/barrido_es.py` | Restos de panadería, heladería, parrillero/catering y FT, motor sin traducir, prohibidos de D11 y concordancias de «la finca». Sin «generador» ni «aparcamiento». `PROHIBIDOS` importable |

## 2. Decisiones que se apartan de la SPEC o del research (y por qué)

1. **Driver SIN permutar** (SPEC D3 pedía el crecimiento sobre los EVENTOS «con el mapeo del catering, B4 = eventos»).
   El catering ES no permuta: lo descartó (`catering-es-2_0/F1-camino-2_0.md:44`) porque la cobertura de personal es
   `horas × personas × B6` y el aforo lee B4; sólo lo hizo el EN, parcheando `Staffing!B20`, cosa que aquí sería código
   común. Con B4 = eventos, la cobertura multiplicaría por los invitados y dejaría de servir de gate. Se queda como
   parrillero, paellero y catering: B4 = 82 invitados por evento, B6 = 120 eventos. El 8 % y el 5 % crecen sobre los
   invitados; en euros es idéntico. La nota de `Supuestos!C7`/`C8` lo traduce a eventos y `cifras_fin_es.py` da
   `EVENTOS_EQUIVALENTES_A2/A3` (130 y 136) y `BE_EVENTOS_*` para que el Word hable en eventos.
2. **Intermediarios 20 % × 12,5 %** (SPEC D5: 25 % × 10 %). La demo §2.11.9 del motor sube este input al 25 % y exige que
   la comisión suba (`grupo_a.py:4867`): con el caso en el 25 % no se mueve y falla. Mismo coste: 2,5 % de las ventas.
3. **Préstamo 263.000 €** (research ≈ 255.000 €): una vuelta de calibración. La necesidad de caja del libro (362.603 €)
   sale más alta que la cuenta a mano (IVA de la inversión 51.194 € y fondo de 59.629 €). Exceso: 397 € (0,1 %).
4. **Inversión**: las 15 partidas del research desdobladas en 19 = 230.000 € + **8 % de imprevistos sobre la obra**
   (11.280 €, la fila 28 del molde, que el research no tenía) = 241.280 € (SPEC D7: ≈ 242.000 €). Obra 141.000 € (15 años),
   maquinaria y mobiliario 66.000 € (10 años; carpa y grupo electrógeno aquí), no amortizable 23.000 €.
5. **Plantilla** (SPEC D6, 6 filas, sin camareros ni cocina): titular 2.000 € · coordinación FD 1.650 € al 75 % ·
   mantenimiento y jardinería 1.400 € al **80 %** (research: 1.450 € al 100 %; lo grande va en fijos externos) · 2 auxiliares
   FD 1.350 € al 40 % · comercial 1.500 € al 20 % · limpieza 1.300 € al 20 %. 111.720 €/año = **30,7 %**; 3,75 jornadas.
6. **Fijos** (43.000 €, 10 filas): marketing 12.000 + ferias y puertas abiertas 6.000 (research: 18.000) · jardinería externa
   8.000 + reparaciones y reposición 6.000 (research: 14.000) · gestoría 3.000 · software 1.800 · PRL 500 · tasas e IBI 2.500
   · revisiones BT/PCI/grupo 1.200 · limpieza general y DDD 2.000. SGAE va por evento en el coste directo (D6).
7. **El año 1 no sale «en torno a cero»** (research: ≈ 262.000 € y EBITDA ≈ −5.000 €). El motor NORMALIZA la rampa dentro del
   año (`Tesorería!fila 7`: «el AÑO factura lo que dice el P&L»): el P&L del año 1 vende 364.080 € y la rampa 0,45 → 1 sólo
   reparte la venta hacia el final del año. Neto del año 1: 32.101 € (8,8 %). SPEC D9 lo deja informativo. **El Word no
   puede decir que el año 1 sale en pérdidas**: la caja del primer año la aguanta el fondo y el saldo mínimo es de 51.025 €.
8. **«15 años» escrito con cifra** casa con la bio antigua del censo (`censo-entregables.py`, `RX_BIO_VIEJA`): se escribe
   «quince años». El Word y el contrato tienen que hacer lo mismo o el censo `--fail` los tumba.
9. `fianza_meses`: la nota no dice que la fianza «se pacta libremente» (la LAU fija una legal fuera de D11): «lo habitual» +
   «compruébalo con tu abogado».

## 3. Calibración (1 vuelta de 3)

| Vuelta | Cambio | Resultado |
|---|---|---|
| 0 | caso del research (préstamo 255.000 €) | motor exit 1: RD-34 origen − usos = −7.473 € (−2,1 %); `PyG!G10:G11` «fórmulas perdidas»; censo `bio_vieja` por «15 años» |
| 1 | préstamo 263.000 € · G10/G11 por valor en la semilla · «quince años» | **TODO VERDE** y D9 VERDE a la primera; no hizo falta tocar renta, fondo ni plantilla |

Después sólo se tocaron textos (vocabulario y notas): las cifras no se movieron.

## 4. Cifras del caso (`cifras_caso_es.json`, 155 tokens)

- **Actividad**: 82 invitados × 37 € sin IVA (44,77 € con IVA) × 120 eventos. Ventas **364.080 / 393.206 / 412.867 €**
  (≈ 130 y 136 eventos equivalentes). Espacio y servicios 283.982 € + canon 80.098 € (cada punto de canon ≈ 6.675 €).
- **Márgenes**: coste directo 46.289 € (12,7 %); margen bruto 80,5 %; personal 30,7 %; renta 11,5 %.
- **Resultado**: RAI 37.766 / 55.209 / 67.039 €; neto **32.101 € (8,8 %) / 46.928 € (11,9 %) / 50.279 € (12,2 %)**.
- **Inversión**: partidas + imprevistos 241.280 € · CAPEX 251.780 € (con fianza 7.000 y renta previa 3.500) · fondo 59.629 €
  · inversión total 311.409 € · IVA 51.194 € · **necesidad 362.603 €**.
- **Financiación**: 100.000 € propios + **263.000 €** al 6,5 %, 8 años con 1 de carencia; cuota 47.953 €. DSCR 1,68 / 1,71
  (**mínimo 1,68**).
- **Equilibrio**: contable 72 invitados por evento = **105 eventos** (holgura contable 14,8 %); caja 67 / 77 / 79 invitados =
  **98 / 113 / 116 eventos** del tamaño medio. Holguras de caja **22,9 % / 14,9 % / 18,1 %**.
- **Tesorería**: saldo mínimo **51.025 € en abril (Mes 2)**; cierre 149.910 € en febrero. 303 a compensar todo el año.
  Payback «Más de 3 años». Cobertura de horas **101 %** (6.900 contratadas / 6.859 necesarias).
- **Escenarios**: pesimista 78 × 34 € × 100 = 265.200 € → neto −41.818 €; optimista 85 × 39 € × 135 = 447.525 € → +89.189 €.

## 5. D4 demostrado sobre el xlsx calculado (`cifras_fin_es.py`, `prueba_d4`)

- `PyG!G10` «Ventas de alquiler del espacio y servicios del evento» = 0,21 · `PyG!G11` «Canon del catering exclusivo» = 0,21.
- `Tesorería` fila 16 (IVA repercutido): Σ 12 meses = 76.456,80 € = 0,2100 × 364.080 €; desvío máximo mes a mes frente a
  21 % × ventas del mes = 0,00 €.
- 303: Mes 4 = 15.201,39 − 8.391,30 − 51.193,80 (IVA de la inversión) = −44.383,70 · Mes 7 = 18.673,96 − 9.058,51 −
  44.383,70 = −34.768,26 · Mes 10 = 26.590,09 − 10.579,52 − 34.768,26 = −18.757,69 (todos iguales al libro). Pago del 303
  en el año 1: 0 €. `IVA_COMPRAS` = 21 % (coste directo); el canon no tiene coste.

## 6. Gates (VPS, 25-oct)

- `ciclo.sh` → `main.py exit 0`, **TODO VERDE**: idempotencia 0 · `inject_cache` 734 fórmulas (682 con caché) + 12, 0 fallos
  pycel · data_only 693 con valor, 52 «""», 0 fallos · blancos 0 · **§9 13/13** · checklist C2 84 ítems · censo `--fail` 0 ·
  moldes **30/30** · 16/16 protegidas · demos §2.11 1-13 (incluida la 5, ramas del IS) y A7 en verde.
- `cifras_fin_es.py` → **D9 VERDE** (DSCR ≥ 1,30 · saldo > 0 · cobertura ≥ 98 % · holgura A2 ≥ 12 % y A3 ≥ 15 % · neto A3 6-14 %
  · exceso 0-5 % · D4).
- `barrido_es.py` sobre los 2 xlsx: **0** · `catering-es-2_0/gate_restos_ft.py <carpeta> --rx-extra '<restos de panadería,
  heladería y parrillero>|plan-negocio-panaderia|plan-negocio-heladeria|plan-negocio-parrillero'`: **VERDE**.
- Mac = VPS (sha256) en los 2 xlsx y en `cifras_caso_es.json`.

## 7. Para los redactores del Word (F2 paso 4)

- Hablar en EVENTOS con los tokens `EVENTOS_EQUIVALENTES_A2/A3` y `BE_EVENTOS_*`; los invitados por evento del P&L crecen
  por construcción del libro (§2.1).
- El año 1 NO sale en pérdidas (§2.7). El riesgo es de ocupación: con menos de ≈ 98 eventos del tamaño medio no hay caja.
- El canon del 12 % es un supuesto («negócialo»), nunca un dato. Todo lo que factura la finca va al 21 %.
- Escribir «quince años», no «15 años» (§2.8).
