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

## 8. Revisión final aplicada (ronda única, 25-oct-2026, sesión Claude Code)

Fuente: `REVISION-FINAL.md` (0 B · 9 M · 26 m). Cambios en el Mac (solo ficheros); regeneración y gates en el VPS
(`/root/wt-finca`), ficheros llevados con `scp` uno a uno. Sin commits.

### M (9/9; M7 sin `G14`)

| # | Estado | Qué se hizo |
|---|---|---|
| M1 | ✅ | Word P96: «{BE_EVENTOS_ANO} eventos al año del tamaño medio ({INVITADOS_EVENTO} invitados), o {BE_INVITADOS_EVENTO} invitados por evento si mantienes los {EVENTOS_ANO} eventos, con unos ingresos de {BE_INGRESOS}» |
| M2 | ✅ | P59, P96 y P113: el umbral de caja del año 1 ({BE_EVENTOS_ANO_CAJA}) y el de los años 2 y 3 ({BE_EVENTOS_CAJA_A2}/{BE_EVENTOS_CAJA_A3}) |
| M3 | ✅ | Regla única «ninguna fecha en firme sin licencia; antes, solo reservas condicionadas a la licencia con devolución íntegra si no llega»: Word P43, P65, P66, P70, P76, P95, P97, P99, P103 y P113; contrato (tercera idea guía, Segunda con el inciso y cláusula nueva **«Segunda bis · Reserva condicionada a la licencia»**: condición suspensiva con fecha límite ≥ 6 meses antes del evento, solo se cobra la reserva, firme al comunicar la licencia, devolución íntegra en [14] días si no llega); checklist F2 («No confirmar fechas en firme sin licencia», remite a la Segunda bis); `Supuestos!C34` y `C52`; `Instrucciones` (antelación de la reserva); landing (`why.reasons[0]`, FAQ 1, tarjeta de Tesorería); correo (dos viñetas); pistas de `tandas_docx.py`. Año 1: la primera temporada se vende con reservas condicionadas durante la tramitación, que pasan a firmes con la licencia; si no se llega, escenario pesimista |
| M4 | ✅ | P57 y P97 (con tokens): el saldo mínimo ({SALDO_MINIMO}, {MES_SALDO_MINIMO_NOMBRE}) lo sostiene el fondo en la primavera de arranque; el primer invierno se pasa con la caja de la temporada ({SALDO_MES12} en el mes 12). `Supuestos!C35` igual. Comprobado contra `Tesorería!B22:M22` regenerada |
| M5 | ✅ | P109: 85.6 proporcionalidad, 87.2 reciprocidad, 90.2 solo fuero, 103.l solo desistimiento a distancia |
| M6 | ✅ | Contrato, Sexta: «La reserva como señal a cuenta del precio»; se rige exclusivamente por la tabla de la séptima y su reciprocidad de la octava, que sustituyen a cualquier régimen general de señal o arras. Fuera «arras penitenciales» y la cita del art. 1454 (con efectos pactados distintos, el nombre ya no era coherente) |
| M7 | ✅ / ⏸ | `Supuestos!C39`, `C40` y `Tesorería!O16` reescritas con el VOCABULARIO del contenido (claves = frases del motor; cero código común). **`PyG!G14` no**: es la fórmula común `iva_bebida_compra` (sale 10 %) y `IVA_COMPRAS` solo admite «comida»; sin efecto en cifras (coste del canon = 0). Deuda del motor: que `IVA_COMPRAS` acepte «bebida» |
| M8 | ✅ | El motor ignora la columna E de la semilla y la reescribe con `grupo_a._lleva_iva(rótulo)` (`RX_SIN_IVA`, anclada con `^`): la partida pasa a llamarse **«Licencias, tasas, calificación urbanística y prestación compensatoria o canon»** y sale «No». `cifras_fin_es.py` lee `LICENCIAS` por el rótulo nuevo. Préstamo sin tocar (263.000 €) |
| M9 | ✅ | Landing FAQ 9 y `equivalencias-es/datos/integracion.json` («ejemplos»): fianza = depósito en garantía (MX, CO), aseos = baños, catering = banquetería (CL, AR), barra libre = open bar. Las cuatro comprobadas en el texto de la guía generada |

### m (24 aplicados · 2 no aplicados)

- **Word**: m1 (`PAYBACK` en minúscula desde `cifras_fin_es.py`, y P112 «el payback, de …»), m2 (el/del/al con los porcentajes en P40, P43, P62, P72, P87, P95, P96, P112 y P113), m3, m4, m5, m6, m7, m8 (saneamiento: fosa o depuradora dentro de aseos e imprevistos, confederación hidrográfica; la nota de la partida de aseos lo dice ahora), m9, m10, m11 (también `Instrucciones!B44` y checklist F2) y m12: ✅.
- **Plan financiero**: m14 (unas 24, el 80 %), m15 (13 h), m16, m17 (300 sillas, también checklist F3), m18 (Andalucía ≈ 13.000 €), m19 (`Tesorería!O5` e `Instrucciones!D35`: «la licencia (de 6 a 12 meses o más) y la obra se cierran durante el invierno anterior»), m20 (de diciembre a febrero coordina el titular: `Personal!J6` y checklist F4; sin cambiar la jornada del 75 %): ✅. **m13 no**: `Personal!C11 = SUM(C5:C10)` es fórmula de `grupo_a` (molde común); el Word ya usa las 3,75 jornadas ponderadas (`JORNADAS_EQUIVALENTES`). Deuda del motor: `SUMPRODUCT(B5:B10,C5:C10)` y `Escenarios!B24:D24`.
- **Contrato**: m21 (tramos «de 6 meses a menos de 12…», también en el anexo de empresa), m22 (mínimo garantizado sin precio por invitado del espacio; los invitados de más, opcional entre corchetes; la liquidación igual), m23 (desistimiento solo a distancia o fuera de la finca, 103.l; también checklist F6, sin citar el art. 102), m24, m25 (último tramo «descontados los costes que la Finca se ahorra»; la calculadora lo avisa en las notas de `cn5` y `can5`, regenerada con autotest): ✅.
- **Correo**: m26 «allí lo contamos entero» ✅. **Guía de equivalencias en Letter: no aplicado** (deuda transversal del generador común `equivalencias-es/build_guia_es.py`, afecta a las 53 guías; fuera de este PR).
- De paso: la nota de trimestres de la Tesorería (VOCABULARIO) decía «unos 18.760 € por compensar»; con M8 son 16.658 € → «unos 16.660 €».

### Cifras del caso que cambian (M8)

| Token | Antes | Después |
|---|---|---|
| `IVA_INVERSION` | 51.194 € | **49.094 €** |
| `NECESIDAD_CAJA` | 362.603 € | **360.503 €** |
| `PRESTAMO` | 263.000 € | 263.000 € (sin cambio) |
| `DIFERENCIA_FONDOS` (sobrante) | 397 € (0,1 %) | **2.497 € (0,7 %)** |
| `DSCR_MIN` | 1,68 | 1,68 (sin cambio) |
| `SALDO_MINIMO` | 51.025 € (abril, Mes 2) | 51.025 € (sin cambio: la Tesorería no mueve caja por el IVA de la inversión, se compensa en el 303) |
| `PAYBACK` | «Más de 3 años» | «más de 3 años» (m1) |

Lo demás (ventas, neto, equilibrios, holguras, cobertura, escenarios) no se mueve.

### Gates (VPS)

- `ciclo.sh` (dos vueltas: la segunda tras corregir la nota de trimestres) → `main.py exit 0`, **TODO VERDE**: §9 13/13,
  idempotencia, caché (734 fórmulas, 0 fallos pycel; 693 con valor, 52 «""»), blancos 0, checklist C2 84 ítems, censo 0,
  moldes 30/30, 16/16 protegidas, demos.
- `cifras_fin_es.py` → **D9 VERDE** (8/8 OK; D4 sobre el xlsx calculado: G10/G11 = 21 %, Σ repercutido = 21 % × 364.080 €,
  303 del Mes 4/7/10 = libro, pago del 303 en el año 1 = 0 €). `cifras_caso_es.json` 155 tokens.
- `tandas_docx.py check` (Mac): `fin_es_a` OK (0 errores, 4 avisos de cifras escritas ya existentes) · `fin_es_b` OK (0
  errores, 4 avisos). `preparar` rehecho con las cifras nuevas y las pistas alineadas con M3.
- `docx_fin_es.py` → **VERDE** (131 párrafos, 10 Heading 1, 6.906 palabras, A4, 0 tokens) · `contrato_fin_es.py` → **VERDE**
  (150 párrafos, 4.752 palabras, A4) · `calculadora_fin_es.py` → autotest **VERDE** (588 comprobaciones; 172 fórmulas con
  caché).
- `barrido_es.py` sobre los 5: 3 coincidencias, las aceptadas del contrato (2 × «obrador» del cliente y «espacio cubierto»).
- `catering-es-2_0/gate_restos_ft.py` sobre los 5 (sin la guía, que es Letter) con `--rx-extra` de restos de panadería,
  heladería y parrillero: **VERDE** · `censo-entregables.py --only plan-negocio-finca-eventos-bodas --fail`: **0 defectos**
  (6 ficheros, 918 fórmulas, 0 sin caché, 0 noA4).
- sha256 Mac = VPS en los 5 entregables regenerados y en `cifras_caso_es.json`. La guía de equivalencias no se regenera.
- Grep de comprobación sobre los textos regenerados: 0 «Más de», 0 «Comunitat», 0 «arras penitenciales» / «1454», 0
  «vend… fechas sin licencia», «primer invierno» solo con la caja de la temporada.

### Pendiente fuera de este PR

- Si el borrador de Resend del correo de lanzamiento (3-dic) ya se creó con el HTML anterior, hay que actualizarlo con el
  nuevo (`broadcast-…-lanzamiento-es.html`: regla de la licencia, «primera temporada se reserva…» y «lo contamos»).
- Deudas del motor/generador: `IVA_COMPRAS` con «bebida» (`PyG!G14`), `Personal!C11` ponderado (m13) y guía de
  equivalencias en A4 (m26, las 53 guías).
