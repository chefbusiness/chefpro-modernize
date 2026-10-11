# Catering ES 2.0 — F2 paso 1 (implementador) · notas y comandos del paso 3

> Sesión Claude Code, 11-oct-2026. SPEC: `SPEC-2_0.md` (D1-D12). Código en el Mac; todo lo que abre xlsx/docx, en el
> VPS (`/root/wt-cates`, venv `/root/venv-guias`, scratch `/root/tmp-cates-f2`). Nada escrito todavía en `dl/`.

## 1. Qué hay (todo en verde con lo escrito)

| Pieza | Fichero | Estado |
|---|---|---|
| Vocabulario con frases y tildes (D1) | `planes-v2_0/grupo_a.py` (`compilar_vocabulario`, **opt-in** `VOCABULARIO_SIN_TILDES`) | `regresion5.py`: **5 planes de línea A = 0 diferencias** frente a `dl/` |
| Contenido del plan (D2, D4-D6) | `planes-v2_0/contenido_plan_catering_tematico_eventos/a.py` | caso del research, rótulos sólo por `VOCABULARIO` |
| Semilla (D3, D7) | `semilla_cat.py` + `datos_checklist.py` (82 tareas 12/15/14/10/16/15, escritas aquí) | copia del FT ES v2.2 + valores de Supuestos, partidas, fijos, títulos y checklist |
| Motor | `ciclo.sh` → `main.py --dry-run --origen` | **TODO VERDE**: 13/13 gates, idempotencia 0, caché 0 fallos, blancos 0, censo 0, demos pycel OK, 30/30 moldes |
| Calibración D15 + tokens | `cifras_cat_es.py` → `cifras_caso_es.json` (73 tokens) | **VERDE** |
| Calculadora (D8b) | `calculadora_cat_es.py` | autotest pycel **VERDE: 168 comprobaciones**; `motor.gate_formatos` 0; firma `calc-beta` |
| Docx (D8) | `tandas_docx.py` + `BRIEF-REDACTORES.md` + `docx_cat_es.py` | tandas listas; ensamblado `--parcial` VERDE (10 H1, A4) |
| Otros 7 ficheros (D9) | `arreglos_d9.py` | ensayo: 23 sustituciones, `barrido_es.py --prohibidos` = 0 |
| Barrido D12 | `barrido_es.py` | plan + checklist + calculadora: **0** coincidencias |

## 2. Caso calibrado (Excel del dry-run, `cifras_caso_es.json`)

**Actividad y resultados**
- 130 eventos × 65 invitados × 53 € sin IVA (58,33 € con IVA).
- Ventas: 447.850 € / 501.592 € / 541.719 €.
- Resultado antes de impuestos del año 1: 46.231 €. Neto: 39.297 € (8,8 %) / 62.197 € / 69.778 €.
- Margen bruto 61,3 %; personal 36,3 % de las ventas.

**Inversión y financiación**
- Inversión 130.365 € (compras 74.880 € + fondo de maniobra 55.485 €).
- Necesidad de caja: 145.040 €.
- 35.000 € propios + **préstamo de 111.000 €**, calibrado (`Financiación!B18` pedía 110.040 €; diferencia +960 €, 0,7 %).
- Préstamo al 6,5 %, a 6 años con 1 de carencia; cuota de 26.710 €.

**Ratios D15**
- **DSCR mínimo: 2,84.**
- **Saldo mínimo de tesorería: 26.201 €** (mes 4).
- **Cobertura de horas: 122 %.**
- **Payback: 2,0 años.**

**Equilibrio**

| | Invitados por evento | Eventos al año |
|---|---|---|
| Contable | **54,05 → 55** | **109** |
| Caja | 52,55 → 53 | 106 |

- Los eventos al año salen del token derivado: ingresos de equilibrio ÷ (53 € × 65).
- **Holgura sobre el equilibrio de caja: 23,7 %** (≥ 15 %): no hizo falta subir los eventos.

**Escenarios**
- Pesimista (105 eventos · 60 invitados · 50 €): −35.201 €.
- Optimista (150 eventos · 70 invitados · 57 €): +117.788 €.

## 3. Desviaciones de la SPEC (para decidir)

1. **Versión.** El motor estampa **«Versión 2.2 · septiembre 2026»** en los dos xlsx: el gate `sin_version` exige `motor.VERSION`, y el mes es el de la versión del motor, no el del run. La calculadora y la portada del docx usan la misma. Propongo anunciar la **2.2** en landing, changelog y correo (D10/D11 dicen «2.0 · octubre»). Cambiarlo obligaría a parchear después del motor y rompería la idempotencia de familia.
2. **`compilar_vocabulario` es opt-in.** Encendido para todos, la **panadería** cambiaba 3 rótulos: sus claves con tilde («cubiertos/día previstos» → «transacciones/día previstas») nunca casaban. Bug latente en su libro publicado: se lee «Transacciones/día previstos / necesarios», sin concordancia. Queda como está; arreglarlo es una línea en su contenido más un republicado.
3. **Plantilla en 4 filas**, no 5. La coordinadora-maître va dentro de la fila del equipo de eventos: 8 personas, jornada 0,31625, 3.642 €/mes, el mismo coste que el research. Con 5 filas la geometría del molde FT cambia y el motor cuenta 23 fórmulas «perdidas».
4. **Fijos.** A los 22.150 € del research se suman **2 partidas [estimado]** para llenar las filas del molde: reposición de menaje 1.200 € y permisos municipales 600 €. Suprimir filas desplaza el P&L, y el motor lo cuenta como 18 fórmulas perdidas.
5. **Varios y drop-off.**
   - `pct_varios` 5 %: el 3 % del research más 2 puntos de canon de fincas, como dice D5.
   - `pct_delivery` (drop-off) 5 % con una comisión del 10 %. Con la comisión a 0 falla la demo §2.11.9 del motor.
6. **Umbral de margen bruto: 60 %**, no el 65 % del research. En el motor el margen bruto descuenta todos los variables, y el caso da 61,3 %: con 65 % saldría en rojo contra su propio caso.
7. **Las tandas (a) y (b) las escribí yo:**
   - los textos del libro van en `a.py`, con la tabla de referencias con fuente o «Estimación del kit»;
   - el checklist va en `datos_checklist.py`.
   
   Para Sonnet quedan solo las del docx.
8. **Inversión en 14 filas**: «marca, web, fotos y dossier» (4.000 €) y «lanzamiento» (3.000 €) van juntas. Total: 67.000 €, como el research.

**Verificado en el BOE hoy** (para las notas del checklist y el §9):
- TRLGDCU art. 103.l: sin desistimiento en un servicio de «comida» con fecha.
- RDLeg 1175/1990: la nota del epígrafe 677.9 incluye el «catering».
- RD 1021/2022, art. 13.5.b: lo preparado en una vivienda «no se podrá suministrar a colectividades ni en eventos».
- RD 1021/2022, DF 1.ª: registro autonómico previa declaración responsable.
- El ATP (RD 237/2000) va con la cita del research.

## 4. Paso 3 — comandos (en orden)

```bash
# 0) Mac: redactores Sonnet (2 en paralelo, ≈ 6.700 palabras). Cada uno lee BRIEF-REDACTORES.md y
#    tandas/cat_es_{a,b}.entrada.json, escribe textos/cat_es_{a,b}.json y deja en 0 errores:
python3 scripts/productos-digitales/catering-es-2_0/tandas_docx.py check --tanda cat_es_a   # y cat_es_b
# commit de textos/ y push; en el VPS: cd /root/wt-cates && git pull
C=/root/wt-cates/scripts/productos-digitales/catering-es-2_0; DL=/root/wt-cates/astro-site/public/dl/plan-catering-tematico-eventos
PY=/root/venv-guias/bin/python; export CLAUDE_SCRATCHPAD=/root/tmp-cates-f2
# 1) Excel: semilla + motor (dry-run, TODO VERDE) y copia a dl/ con los MISMOS nombres (inject_cache ya hecho)
cd $C && bash ciclo.sh && grep "TODO VERDE" $CLAUDE_SCRATCHPAD/run.log
cp $CLAUDE_SCRATCHPAD/dryrun/plan-catering-tematico-eventos/{plan-financiero,checklist-apertura}-catering-tematico-eventos.xlsx $DL/
# 2) tokens + calibración D15 sobre el publicado
$PY cifras_cat_es.py --xlsx $DL/plan-financiero-catering-tematico-eventos.xlsx
# 3) docx (sin --parcial: aborta si falta una ranura) y calculadora
$PY docx_cat_es.py --salida $DL && $PY calculadora_cat_es.py --salida $DL
# 4) D9: arreglos de texto de los otros 7
$PY arreglos_d9.py --aplicar
# 5) gates D12
$PY regresion5.py                                                  # sólo si se vuelve a tocar grupo_a.py
$PY barrido_es.py $DL/{plan-financiero,checklist-apertura,calculadora-pricing}-*.xlsx $DL/plan-de-negocio-*.docx
$PY barrido_es.py --prohibidos $DL/*
cd /root/wt-cates && $PY scripts/productos-digitales/censo-entregables.py --only plan-catering-tematico-eventos --fail --quiet
$PY scripts/productos-digitales/gate-no-latinos.py --only plan-catering-tematico-eventos
$PY scripts/productos-digitales/paginas-gate.py --only plan-catering-tematico-eventos   # páginas del docx → landing
# 6) Mac: scp de los 11 ficheros de dl/ y de cifras_caso_es.json; commit + push. VPS limpio:
#    git reset --hard origin/feat/catering-es-2-0 && git clean -fd && rm -rf /root/tmp-cates-f2
```

Una revisión opus final (D12): recalcular a mano 3 cifras del P&L, leer el checklist y el docx enteros, y abrir el
RD 1021/2022, la Ley 37/1992 art. 91 y el TRLGDCU art. 103. Después: D10, landing y dashboard (lista de F1-camino §6;
cifras por token desde `cifras_caso_es.json`; sin DSCR, payback ni saldos). Luego D11 (correo) y
`gate-flujo-postpago --only plan-catering-tematico-eventos` en preview y en LIVE.

## 5. Gotchas medidos en este paso

- **`grupo_a` conserva los valores verdes de `0. Supuestos` que trae el libro** (§1.3, dato del cliente): partiendo del FT, el primer dry-run salió con 45 × 12 € × 250. Por eso `semilla_cat.py` escribe los 34 valores del contenido en sus celdas.
- **Un rótulo de driver renombrado con el 2.º campo de `SUPUESTOS` ciega las demos.** «No se localizan las filas»: va por `VOCABULARIO`.
- **Rótulos de importe sin palabras de recuento** («días», «invitados», «eventos», «mes», «clientes», «personas»), salvo que lleven una palabra fuerte de euro («coste», «importe», «precio»…). Si no, `gate_formatos` los marca. Pasó en la calculadora: 20 celdas.
- **Suprimir o añadir filas del molde FT** (fijos, plantilla) se cuenta como fórmulas perdidas: se usan las filas existentes.
- **La calculadora tiene que llamar a sus hojas `Calculadora` + `Ejemplos`**: es la firma `calc-beta` de `motor.detectar`. Con otro nombre, cualquier pasada de familia sobre la carpeta aborta.

## 6. Cierre de la F2 (paso 3, 11-oct-2026) — los 11 ficheros en `dl/`, todo en verde

- **Versión 2.2** (decisión del orquestador): la estampan el motor en los dos xlsx, la calculadora y la portada del docx.
- **Rehechos (sha256)**: plan financiero `fedc828d…71d` · checklist `ed26df9a…5c4` · calculadora `4fd16345…ee7` ·
  plan de negocio docx `24a7744f…119`. D9 aplicado en los otros 7 (23 sustituciones, lista en §1/`arreglos_d9.py`).
  Respaldo del 1.x: en git (`ee9c03b1`); sha256 Mac = VPS en los 11 + `cifras_caso_es.json`.
- **Caso final**: idéntico al de §2 (130 × 65 × 53 €; neto año 1 39.297 €; préstamo 111.000 €; DSCR 2,84; saldo mínimo
  26.201 €; equilibrio 55 invitados/evento o 109 eventos/año; holgura de caja 23,7 %).
- **Gates D12**:
  - Motor: TODO VERDE, 13/13 gates, idempotencia 0, 82 ítems de checklist.
  - Calibración D15: VERDE, 5/5.
  - Docx: 10 Heading 1, A4, 0 tokens sin resolver, 0 prohibidos, 7.426 palabras.
  - Calculadora: autotest 168/168.
  - Censo (11 ficheros): 0 defectos. No latinos: 0.
  - Barrido de prohibidos en los 11: 0 («freelance», «validado», «España 2026», cifras de la 1.x).
  - Regresión de los 5 planes: 0 diferencias.
  - Moldes en `dl/`: A-β, C2, calc-beta y P2.
- **Barrido amplio del docx**: 7 coincidencias revisadas, todas legítimas («negocio de calle», «salir a la calle», «ticket de
  {TICKET_EVENTO} por evento», «mínimo de comensales», «vehículo» en las frases del ATP).
- **Textos corregidos tras la revisión** (`textos/cat_es_a.json`):
  - **p43**: el núcleo fijo son 3 personas a jornada completa (dueño, jefe de cocina, ayudante-conductor). La coordinadora-maître
    va dentro de la bolsa de 8 fijos discontinuos, como en la hoja Personal. `{PLANTILLA_PERSONAS}` = 11 = suma de la
    columna «Personas» (3 + 8), que equivalen a 3,32 jornadas completas.
  - **p48**: la mezcla tecleada suma los 130 eventos del Excel (token `{EVENTOS_ANO}`). Su media exacta es 65,6
    invitados y 52,92 €, y el texto dice que el Excel la redondea con prudencia: 65 y 53 €, con ventas un 0,7 % por debajo
    de la mezcla. El «con el IVA del 10 %» pasa a «con el IVA incluido», porque el PVP de 58,33 € pondera el 21 % del alcohol en drop-off.
  - **«25.183 €»**: se queda. `F1-research-es.md` §2 lo trae con fuente: Bodas.net, Informe del Sector Nupcial 2026, con enlace.
- **Gate afinado** (`tandas_docx.PROHIBIDOS`): «2.200»/«4.500» sólo se prohíben como ticket por evento de la 1.x. Los
  2.200 € de seguros del caso 2.2 (`{SEGUROS_ANO}`) son legítimos: el primer ensamblado los marcó por error.
- **No medido**: páginas del docx (el VPS no tiene LibreOffice y `paginas-gate` no encontró menciones en la ficha). Hay que medirlas antes de
  escribir el número en la landing (D10).
- **Pendiente** (fuera de este paso):
  - D10: landing, dashboard y changelog con «Versión 2.2» y las cifras por token desde `cifras_caso_es.json`.
  - D11: correo.
  - La revisión opus final de D12.
  - `gate-flujo-postpago --only plan-catering-tematico-eventos` en preview y en LIVE.

## 7. Ronda de arreglos tras `REVISION-FINAL.md` (11-oct-2026): 1 bloqueante + 6 mayores + 15 menores

**Bloqueante B1 (restos del FT).**
- `semilla_cat.py` escribe `Instrucciones!A3` del checklist y los docProps `description`/`keywords` de los dos xlsx. El motor no los toca.
- Después se vuelve a pasar `ciclo.sh`; nada se parchea en `dl/`.
- Gate nuevo, `gate_restos_ft.py`: busca «food truck», «food-truck» y «plan-negocio-food-truck» en celdas, pestañas, docProps, docx, tablas y cabeceras/pies de los 11. Exige además A4, autor «AI Chef Pro», fecha ≥ 2026 y nada de «python-docx» en los 8 docx. **VERDE.**

**Mayores.**
- **M1 (contrato B2C p27):** el 60 % restante se paga siete días antes.
- **M2:** p95/p116 dicen que crecen los invitados por evento (65 → 72,8 → 78,6) con los mismos 130 eventos.
- **M3:** p97/p111 explican que la holgura del 23,7 % es la del año de carencia. Desde el año 2, equilibrio de caja de 403.673 €: lo cubre el crecimiento con una holgura del 24,3 %, y sin crecer harían falta 118 eventos. Tokens nuevos en `cifras_cat_es.py`: `INVITADOS_EVENTO_A2/A3`, `BE_INGRESOS_CAJA_A2`, `HOLGURA_CAJA_A2`, `BE_EVENTOS_CAJA_A2`.
- **M4:** formación en lugar del carnet (manual p65, contrato p13).
- **M5/M6:** landing (l. 80/131/145/250/262), dashboard (l. 19/26/68), changelog 2.2 y correo:
  - fuera «escandallo» en los 12 conceptos;
  - el equilibrio, «en invitados por evento y en ingresos; el Word lo traduce a eventos al año»;
  - «más de 7.000 palabras» (el docx tiene 7.565).

**Menores.**
- **m1-m6** en el docx: cobros y cancelación precisos, pago a proveedores, millennials/generación Z, ETT, «dotación para 150», estilo y artículos ante %.
- **m7-m9** en el Excel, por `VOCABULARIO` y notas: enero y agosto; sin pan ni bollería; furgoneta y puesta en marcha en Inversión A23/D22/D23; plantilla 3 + coordinadora + 4 extras en Personal J19; «refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos» también en la calculadora.
- **m10-m13 en D9**, que ahora parte siempre de los ficheros 1.1 de `ee9c03b1` y es repetible (34 cambios):
  - contrato: no desistimiento (párrafo nuevo tras p33, art. 103.l TRLGDCU), espacio, seguro de hogar fuera, derechos RGPD;
  - manual: nómina mensual, alta de la empresa en el IAE;
  - «6 estaciones + activación previa», guía p14 completa, catálogo «dos o tres»;
  - **los 7 docx en A4 con docProps 2026**; proveedores a v2.2.
- **Checklist:** RC «recomendado: al menos 600.000 €» y cancelación «del anticipo».
- **m14:** sin tocar; aceptado.
- **m15:** de los testimonios solo cambia Yuki («sushi para amigos y familia», decisión de John) en la landing (×2) y en `testimonials-…ts`. El de Sam Williams no se toca: es capa comercial y queda pendiente de John.

**Cifras.** No cambia ninguna del caso: `cifras_caso_es.json` solo gana los 5 tokens nuevos.

**Gates.**
- Motor: TODO VERDE, 13/13, idempotencia 0, 82 ítems.
- Calibración D15: VERDE.
- Tandas: 0 errores.
- Docx: 10 H1, A4, 7.565 palabras, 0 tokens sin resolver.
- Calculadora: 168/168.
- Censo: 0 defectos. No latinos: 0.
- Prohibidos en los 11: 0.
- Restos del FT: VERDE.
- Regresión de los 5 planes: 0 diferencias.
- sha256 Mac = VPS en 26 ficheros.

**sha256 de los 4 rehechos:**

| Fichero | sha256 |
|---|---|
| Plan financiero | `abd3c9bc…ae88` |
| Checklist | `05495c3b…0b81` |
| Calculadora | `bdab5bb1…7199` |
| Docx | `521ae473…c0c8` |
