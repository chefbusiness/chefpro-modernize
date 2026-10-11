# Paellero ES 2.2 — F2 paso 1 (implementador) · notas y comandos del paso 3

> Sesión Claude Code, 11-oct-2026. SPEC: `SPEC-2_2.md` (D1-D16). Código en el Mac; todo lo que abre xlsx/docx, en el
> VPS (`/root/wt-pae`, venv `/root/venv-guias`, scratch `/root/tmp-pae-f2`). **Nada escrito todavía en `dl/`.**
> Calculadora y `arreglos_d9.py` los escribieron dos subagentes Sonnet con especificación cerrada; revisados aquí.

## 1. Qué hay (todo en verde con lo escrito)

| Pieza | Fichero | Estado |
|---|---|---|
| Contenido (D2, D4-D7) | `planes-v2_0/contenido_plan_negocio_paellero_eventos/a.py` (clon del catering) | caso del research; rótulos sólo por `VOCABULARIO` («cocina de apoyo», «paella para recoger») |
| Semilla + checklist (D3, D10) | `semilla_pae.py` + `datos_checklist.py` (83 tareas 12/16/14/10/16/15) | copia del FT ES v2.2; `Instrucciones!A3` y docProps del paellero desde el día 1 (B1 del catering) |
| Motor | `ciclo.sh` → `main.py --dry-run --origen` | **TODO VERDE**: 13/13, idempotencia 0, caché 0 fallos, blancos 0, censo 0, demos OK (30/30 moldes) |
| Tokens + D15 | `cifras_pae_es.py` → `cifras_caso_es.json` (79 tokens) | **VERDE**, más la holgura del año 2 (informativa) |
| Calculadora (D12) | `calculadora_pae_es.py` | autotest **336/336**; `gate_formatos` 0; `detectar` = calc-beta |
| Docx (D11) | `tandas_docx.py` + `BRIEF-REDACTORES.md` + `docx_pae_es.py` + `fuente_pae_12.json` | tandas listas; ensamblado `--parcial` VERDE (**11 H1**, A4) |
| Otros 7 (D13) | `arreglos_d9.py` (parte siempre de `git show 2d6cac44:`) | ensayo: 20 arreglos, barrido 0 |
| Restos FT + catering | `../catering-es-2_0/gate_restos_ft.py` **parametrizado** (`--rx-extra`, `--excluir`) | sin opciones = el del catering (re-pasado: VERDE); paellero simulado: VERDE |
| Barrido | `barrido_es.py` (lista de `tandas_docx.PROHIBIDOS`) | los 3 xlsx rehechos: 0 |
| Simulación de `dl/` (VPS, revertida) | los 11 ficheros en su carpeta | censo `--fail` 0 · no latinos 0 · moldes A-β / C2 / calc-beta / P2 |

## 2. Caso calibrado (Excel del dry-run, `cifras_caso_es.json`)

- **Actividad**: 105 eventos × 94 raciones × 16 € sin IVA (17,61 € con IVA). Ventas 157.920 € / 173.712 € / 184.135 €. Crecimiento: raciones por evento 94 → 103,4 → 109,6, con los mismos eventos. · **Margen y costes**: margen bruto 63,2 %; personal 55.097 € (34,9 %). · **Resultados**: RAI 14.364 € / 18.345 € / 19.522 €; neto 12.209 € (7,7 %) / 15.593 € / 14.641 €. El neto del año 3 baja: el IS pasa del 15 % de nueva creación al tipo general.
- **Inversión**: 63.111 € (compras 42.686 € + fondo de maniobra 20.425 €). Necesidad de caja 71.487 €. · **Financiación**: 20.000 € propios + **préstamo 51.600 €** (calibrado; +113 €, 0,2 %), al 6,5 %, 6 años con 1 de carencia; cuota 12.417 €.
- **Ratios**: DSCR mínimo **1,70** (año 2: 1,83). Saldo mínimo de tesorería 6.088 € (mes 4). Payback 3,0 años. Cobertura de horas 198 %.

**Equilibrio** (eventos al año = token derivado sobre el evento medio de 1.504 €):

| | Raciones por evento | Eventos al año | Ingresos | Holgura |
|---|---|---|---|---|
| Contable | **81** | **90** | 135.194 € | — |
| Caja, año 1 (carencia) | 77 | 86 | 129.265 € | **22,2 %** |
| Caja, año 2 (con principal) | — | 102 sin crecer | 153.097 € | **13,5 %** |

**Escenarios**: pesimista (85 eventos · 85 raciones · 15 €) −16.950 € · optimista (125 · 100 · 17 €) +41.531 €.

## 3. Desviaciones de la SPEC (para decidir)

1. **Préstamo de 51.600 €**, no ≈ 49.000: la necesidad de caja del libro es de 71.487 € (el research estimaba ≈ 69.000).
2. **10.ª fila de fijos**: «Permisos y autorizaciones municipales», 200 € [estimado], porque el molde tiene 10 filas y el research trae 9 partidas (fijos propios: 10.100 €). Con 300 € fallaba la demo §2.11.5 del motor (las tres ramas del IS). A 79 raciones, el resultado del año 3 (855 €) no absorbía la base negativa pendiente (925 €). Con 200 € pasa. Es un ajuste de 100 €, sin efecto en el caso.
3. **Comisión de la paella para recoger: 10 %** (el research ponía 0 %). Lo exigen la SPEC D6 y la demo del motor.
4. **Plantilla en las 4 filas del molde**: los dos auxiliares van en dos filas de 1 persona al 8 %. Coste idéntico al del research.
5. **Inversión en 14 filas**: «marca, web, fotos y dossier» y «lanzamiento» van juntas (4.500 €). Total: 38.450 €.
6. **Cobro a 20 días** con la política de los contratos (30 % + 70 % el día del evento, SPEC D3), no con la del research (40 % y resto 7 días antes).
7. **Cobertura de horas 198 %**: el titular va a jornada completa y la cobertura solo cuenta 2 personas × 8 h × 105 eventos. Sus demás horas van a ventas, compras y caldos; lo dice la nota de Personal.
8. **Holgura de caja del año 2: 13,5 %** (< 15 %). Se informa, como pide D4: la cubre el crecimiento, pero sin crecer harían falta 102 eventos. Los redactores tienen la regla M3 en la pista §8.
9. **Anexo autonómico** Se trasplanta de la 1.2 con correcciones del research §1/§5 (en la franja forestal, la licencia de la finca no levanta la restricción). Comunidad Valenciana, con el Decreto 148/2018 y sin «excepción cultural». Fechas de Madrid, Andalucía y Castilla y León de fuente secundaria (🟡). Va tras el §10, antes del bloque de cierre del molde.
10. **Contrato B2B sin fuerza mayor**: el modelo B2B no tiene esa cláusula. El arreglo de D8 (fuego o gas prohibido por alerta + plan B) solo entra en la B2C (p32). ¿Se añade una cláusula al B2B? Sería un párrafo más en `arreglos_d9.py`.
11. **Carta (D5)**: los 12 PVP pasan a «por ración (bodas y empresas, con entrantes y show cooking, sin IVA)». Un párrafo nuevo con fuente explica las fiestas populares (3-6 €) y las privadas (18 € en el plan; 11-14 € la paella sola).
12. **Checklist sin «carné»**: el gate de ortografía del motor marca «carne» si en el mismo libro aparece «carné». F4 dice «título de manipulador … ya no se exige». En el docx «carné de manipulador» solo se permite seguido de «ya no existe».
13. **Calculadora** (3 ejemplos por fórmula):

| Ejemplo | Precio sin IVA | Total con IVA | Margen calculado |
|---|---|---|---|
| Boda, 120 invitados | 28,00 € | 3.769 € | 40,8 % |
| Empresa, 70 invitados | 25,00 € | 1.977 € | 49,9 % |
| Fiesta de ayuntamiento, 400 raciones | 4,50 € | 2.043 € | 17,7 % |

   La tabla de escalado va al pie de `Calculadora`, no de `Ejemplos`.
14. **Versión**: el motor estampa «Versión 2.2 · septiembre 2026», igual que en el catering (m14 aceptado).

## 4. Paso 3 — comandos (en orden)

```bash
# 0) Mac: 2 redactores Sonnet ‖ (pae_es_a 29 ranuras / 2.954 palabras; pae_es_b 32 / 3.765). Cada uno lee
#    BRIEF-REDACTORES.md y tandas/pae_es_{a,b}.entrada.json, escribe textos/pae_es_{a,b}.json y deja 0 errores:
python3 scripts/productos-digitales/paellero-2_2/tandas_docx.py check --tanda pae_es_a   # y pae_es_b
# commit de textos/ y push; en el VPS: cd /root/wt-pae && git pull
C=/root/wt-pae/scripts/productos-digitales/paellero-2_2; DL=/root/wt-pae/astro-site/public/dl/plan-negocio-paellero-eventos
PY=/root/venv-guias/bin/python; export CLAUDE_SCRATCHPAD=/root/tmp-pae-f2
# 1) Excel: semilla + motor (TODO VERDE) y copia a dl/ con los MISMOS nombres (inject_cache ya hecho)
cd $C && bash ciclo.sh && grep "TODO VERDE" $CLAUDE_SCRATCHPAD/run.log
cp $CLAUDE_SCRATCHPAD/dryrun/plan-negocio-paellero-eventos/{plan-financiero,checklist-apertura}-paellero-eventos.xlsx $DL/
# 2) tokens + calibración D15 sobre el publicado (debe dar el mismo cifras_caso_es.json)
$PY cifras_pae_es.py --xlsx $DL/plan-financiero-paellero-eventos.xlsx
# 3) docx (sin --parcial) y calculadora
$PY docx_pae_es.py --salida $DL && $PY calculadora_pae_es.py --salida $DL
# 4) D13: arreglos de texto de los otros 7 (desde la 1.2 de git; repetible)
$PY arreglos_d9.py --aplicar
# 5) gates D15
$PY ../catering-es-2_0/gate_restos_ft.py $DL --rx-extra 'cocina central|estaci[oó]n(es)? tem[aá]tica|catering tem[aá]tico|plan-catering' --excluir guia-tipos-paellero-roadmap-food-truck.docx
$PY barrido_es.py $DL/{plan-financiero,checklist-apertura}-paellero-eventos.xlsx $DL/calculadora-pricing-eventos-paellero.xlsx $DL/plan-de-negocio-paellero-eventos.docx
$PY barrido_es.py --prohibidos $(ls $DL/* | grep -v guia-tipos)          # la guía: «food truck» y «camión» legítimos
cd /root/wt-pae && $PY scripts/productos-digitales/censo-entregables.py --only plan-negocio-paellero-eventos --fail --quiet
$PY scripts/productos-digitales/gate-no-latinos.py --only plan-negocio-paellero-eventos
# 6) Mac: scp de los 11 ficheros de dl/ y de cifras_caso_es.json; commit + push. VPS limpio:
#    git reset --hard origin/feat/paellero-2-2 && git clean -fd && rm -rf /root/tmp-pae-f2
```

Después: (1) **Una revisión opus final** (D15) recalcular a mano 3 cifras del P&L y el préstamo; leer enteros el checklist, el docx y el contrato; abrir RD 919/2006 art. 2.1.h, Ley 43/2003 art. 44.3 y LCSP arts. 118 y 198.4. (2) **D14**, con la lista de `F1-camino-2_2.md` §7 cifras por token; sin DSCR, payback ni saldos; la media de 16 € nunca sin su mezcla. (3) **D16** (correo) y `gate-flujo-postpago --only plan-negocio-paellero-eventos` en preview y en LIVE.

## 5. Gotchas medidos en este paso

- **La demo §2.11.5 del motor depende del caso.** Busca, bajando las raciones de 2 en 2 %, un punto con el año 1 en pérdidas, el año 2 positivo pero menor que la base negativa y el año 3 tributando. Con márgenes pequeños, la ventana es más estrecha que el paso de búsqueda. Si falla, mueve un fijo menor ±100 € antes de tocar el caso.
- **«carné» y «carne» en el mismo libro** encienden el gate de ortografía (§1.7).
- **`PAYBACK` puede ser texto** («Más de 3 años»): `cifras_pae_es.py` lo acepta como token de texto en lugar de abortar.

## 5. Cierre de la F2 (paso 3, 11-oct-2026): los 11 ficheros en `dl/`, todo en verde

- **Decisiones del orquestador**: aceptadas las desviaciones 1-9 y 11-13; la holgura del año 2 (13,5 %) se queda y el docx la explica. D10: el contrato B2B gana la cláusula «QUINTA BIS — Fuerza mayor» (alerta de incendios o prohibición de fuego/gas → plan B, reprogramación o devolución del anticipo, como el B2C).
- **Respaldo de la 1.2**: en git (`2d6cac44`), que es de donde parte `arreglos_d9.py`.
- **Excel**: `ciclo.sh` TODO VERDE (13/13, idempotencia 0, censo 0, demos, 30/30 moldes). `cifras_caso_es.json` es idéntico al del paso 1. Caso: §2, sin cambios.
- **Docx**: 142 párrafos, 11 H1, 7.811 palabras, A4, 0 tokens sin resolver y 0 prohibidos.
- **Calculadora**: autotest 336/336.
- **D9 / D13** (`--aplicar`): 23 arreglos en los 7 ficheros.
  - Contrato (8): p2, p23 efectivo, p31 fuego/gas + plan B, no desistimiento y QUINTA BIS en el B2B.
  - Carta (5), catálogo (5: p1, p2, p6 y la inversión de la 1.x de p6, que cazó el barrido), experiencias (2), proveedores (1).
  - Guía y manual: solo A4 y docProps. El manual conserva 4.437 palabras, 14 H1 y 10 tablas (medido antes y después).
- **Gates D15**:
  - restos FT + catering: VERDE (`--excluir` la guía; `--permitir "roadmap food truck"`, nombre de la guía citado en el docx §1). El del catering, sin opciones, sigue VERDE.
  - barrido de los rehechos: solo «un ticket de {TICKET_EVENTO} por evento» (legítimo, como en el catering). Prohibidos en los otros 10: 0.
  - términos D15 (freelance, validado, carnet de manipulador, sin licencia clasificada, PATRICOVA, PIDOM, INFOCYL, tarifa plana, España 2026) en los 11: 0.
  - censo `--fail`: 0. No latinos: 0. Moldes: A-β / C2 / calc-beta / P2.
- **sha256** (Mac = VPS en los 11):

| Fichero | sha256 |
|---|---|
| Plan financiero | `dfc62f85…b0f` |
| Checklist | `7fdb26cb…10c` |
| Calculadora | `ee9884eb…a6c` |
| Plan de negocio docx | `2a36662b…fb6` |

- **Pendiente** (fuera de este paso): la revisión opus final (D15), D14 y D16 (otro agente), `gate-flujo-postpago --only plan-negocio-paellero-eventos` en preview y en LIVE, y las páginas del docx (el VPS no tiene LibreOffice).

## 6. Ronda de arreglos tras `REVISION-FINAL.md` (11-oct-2026): 0 bloqueantes, 6 mayores y 16 menores aplicados

Todos, salvo la fecha «septiembre 2026» del motor (aceptada). Los testimonios, por decisión de John: «dossier B2B» → «los contratos B2B» (Antonio Rivas y Sam Williams, ficha y SPA).

- **M1**: frase del motor sobre el «Word en la versión 1.1», por `VOCABULARIO` (Tesorería!D31). En el paellero, además, el cuadro de Instrucciones pasa a «respecto de la versión 1.2 / v1.2». **El Catering ES 2.2 también lo lleva**: `ciclo.sh` re-pasado y sus 2 xlsx copiados a `dl/`.
- **M2**: carta re-escandallada, «food cost de la paella (sin entrantes)»: 2,00-6,00 € por ración, con los rangos del research §2. Calculadora con la paella más los entrantes: la boda, 6,70 + 0,48 € → 28 €.
- **M3**: un ayuntamiento no adelanta el 30 %.
  - Calculadora: nota del canal y ejemplo con 0 % de anticipo.
  - Docx p82/p107/p112, checklist F5/F6.
  - Landing `:150` y dashboard `:68`: «(wedding planners y agencias)».
- **M4**: comida testigo (RD 1086/2020, art. 30.8 y 30.10, leído en el BOE) en el checklist F2/F6 y el docx p104. **El catering la omitía**: añadida en su checklist (F2/F6) y en su docx p104, re-ensamblado.
- **M5/M6**: fiesta popular de las experiencias (3-6 € por ración, paelleras de 120-150 cm). La guía del food truck, sin márgenes ni plazos de la 1.x atribuidos a los eventos.
- **Menores**:
  - Efectivo «por debajo de 1.000 €».
  - Exención FACe hasta 5.000 €.
  - Holgura del año 3 (token `HOLGURA_CAJA_A3`).
  - Restos de molde por `VOCABULARIO` («pan común» de O16, «obra» de A31/A44/D27/D32) y «dos auxiliares».
  - Contratos: fuera «+ factura por gestión»; RC [600.000] € como mínimo; «en nombre propio o en representación de…»; derechos RGPD completos; interés de demora de la Ley 3/2004.
  - Anticipo antes del D-30, cobertura bien explicada, artículos ante los %, ATP matizado, ficha de Bodas.net y Fogueres de Sant Joan.
- **m9 · cifras**: `pct_comida` = 0,92 (SPEC D4; el libro conservaba el 85,19 % del molde). Cambian:

| Dato | Antes | Ahora |
|---|---|---|
| Neto año 1 | 12.209 € | 12.392 € (7,8 %) |
| DSCR mínimo | 1,70 | 1,72 |
| Holgura de caja años 1/2/3 | 22,2 / 13,5 % | 22,4 / 13,7 / 13,5 % |
| Margen bruto | 63,2 % | 63,3 % |
| PVP con IVA | 17,61 € | 17,60 € |
| Saldo mínimo de tesorería | 6.088 € | 6.130 € |

  Sin cambios: inversión (63.111 €), préstamo (51.600 €), necesidad de caja (71.487 €) y equilibrio (81/90; caja 77/86; año 2, 102 eventos). La landing no citaba ninguna de las cifras que se mueven.
- **Gates del paellero**:
  - Motor: TODO VERDE, idempotencia 0. D15 VERDE.
  - Docx: 11 H1, 7.990 palabras, 0 tokens. Calculadora: 336/336.
  - Restos: VERDE. Prohibidos: 0. Términos D15 y de la ronda: 0.
  - Censo 0, no latinos 0, moldes A-β / C2 / calc-beta / P2.
  - Manual: 4.437 palabras, 14 H1 y 10 tablas.
- **Gates del catering**:
  - Motor: TODO VERDE, idempotencia 0. D15 VERDE, con `cifras_caso_es.json` sin cambios.
  - Docx: 10 H1, 7.607 palabras.
  - Restos sin opciones: VERDE. Prohibidos: 0. Censo 0. No latinos 0.
- **Pendiente del catering** (fuera del encargo, para decidir): su `0. Supuestos!B11` también conserva el 85,19 % del molde frente al 82/18 de sus líneas de venta, y su Tesorería!O16 cita «el pan común».
- **sha256** (Mac = VPS en los 22 ficheros de los dos productos): en el informe del commit.
