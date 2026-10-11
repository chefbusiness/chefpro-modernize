# Plan de Negocio Paellero para Eventos ES — SPEC 2.2 (F1 · 11-oct-2026 · sesión Claude Code)

> Base: `F1-camino-2_2.md` (camino medido) y `F1-research-paellero.md` (delta legal/operativo y caso, con fuentes; lo común
> está en `../catering-es-2_0/F1-research-es.md`). Gemelo y plantilla: el **Catering ES 2.2** de hoy (`../catering-es-2_0/`:
> SPEC, F2-NOTAS §3-§7 y REVISION-FINAL — **aplicar desde el principio lo que cazó su revisión**). John (11-oct): «dale,
> arranca con el paellero». Versión **2.2**. Presupuesto F2 + F3 ≤ 1,5 M tokens (F1 gastó 0,54 M). Lo que no está aquí no se hace.

## 1. Construcción (D1-D3)

| D | Decisión |
|---|---|
| D1 | Camino del catering: motor ES de línea A sobre copia del **FT ES v2.2**, módulo `planes-v2_0/contenido_plan_negocio_paellero_eventos/a.py` **clonado del catering**; scripts copiados en `paellero-2_2/` con sus datos reescritos (semilla, checklist, cifras, tandas, docx, calculadora, `arreglos_d9`, `ciclo.sh`); `gate_restos_ft.py` parametrizado (por defecto, el del catering). **Sin cambios en código común** |
| D2 | Motor sin permutar: invitados (raciones) por evento × precio por ración sin IVA × eventos al año, rótulos por `VOCABULARIO`. Crecimiento: lo hace el motor sobre las raciones por evento — **el docx lo cuenta así** (lección M2 del catering) |
| D3 | Mismos nombres de fichero (no se toca `get-download-urls.ts`). Se REHACEN plan financiero, checklist, calculadora y docx del plan. **Se conserva de la 1.2**: manual técnico ampliado, catálogo con capacidades alineadas, contratos (IVA 10 %, cancelación B2C escalonada y simétrica, fuero del consumidor; política 30 % + 70 %), anexo legal autonómico (trasplantado al docx como 11.º H1), pestaña «88 proveedores» sin renombrar |

## 2. Caso, precios y fiscalidad (D4-D7)

| D | Decisión |
|---|---|
| D4 | Caso = research §3: **105 eventos · 16 €/ración sin IVA (media ponderada) · 94 raciones** (15 bodas a 28 €, 30 empresas a 24 €, 50 fiestas privadas a 18 €, 10 fiestas populares de 400 raciones a 5 €), comida/bebida 92/8, mercancía 28/30 %, consumibles (gas, leña, desechables) 3 %, varios 4,5 %, cocina de apoyo autorizada 900 €/mes, seguros 1.750 €/año, otros fijos del research, inversión 38.450 € en 15 partidas, 20.000 € propios + préstamo **CALIBRAR** (≈ 49.000 €, 6,5 %, 6 años, 1 de carencia), cobro/pago 20/20, estacionalidad del research, **SL unipersonal** (el motor calcula IS). Regla D15: holgura ≥ 15 % y **se informa también la del año 2** (lección M3) |
| D5 | **Precios coherentes en los 4 sitios** (Excel, carta, calculadora, landing): el Excel usa la mezcla del research; la **carta** se rotula como precios por ración para bodas, empresas y fiestas privadas y gana una línea de **fiestas populares por volumen** (3-6 €/ración, con su fuente); un precio de la carta fuera de mercado se ajusta por texto con fuente. La landing no cita la media de 16 € sin su mezcla |
| D6 | IVA 10 % (catering con servicio). «Paella para recoger» = canal de entrega sin servicio del motor (≥ 5 %, comisión > 0 como exige su demo) |
| D7 | Ayudantes **fijos discontinuos**; nunca «freelance»; formación en manipulación a cargo de la empresa (no «carnet»). Plantilla en las 4 filas del molde |

## 3. Gas, fuego y fiestas populares (D8-D9) — research §1, con su fuente en la nota correspondiente

- **D8 Gas**: una botella < 15 kg por quemador con regulador y manguera homologada la conecta el propio paellero (RD 919/2006
  art. 2.1.h; ITC-ICG 08 §5.2); botellas de 35 kg o varias conectadas = instalación → **empresa instaladora autorizada**
  (ITC-ICG 06). Transporte en la furgoneta: exención ADR 1.1.3.6 (≤ 333 kg) con extintor. Recomendación del kit: **una
  botella por quemador**. **Fuego/leña**: lo regula cada comunidad (Ley 43/2003 art. 44.3), épocas de peligro, y una alerta
  puede prohibir incluso el gas → **cláusula de fuerza mayor y plan B** en contrato y checklist. Corregir los nombres de los
  planes: PATRICOVA es de **inundaciones**; Castilla y León = INFOCAL (no «INFOCYL»); IBANAT y SOS Deiak son organismos;
  «PIDOM» fuera.
- **D9 Fiestas populares**: contrato menor (LCSP art. 118), pago en 30 días (art. 198.4), factura electrónica por **FACe**
  si eres SL (Ley 25/2013 art. 4); vender raciones directamente al público = venta ambulante con autorización municipal
  (Ley 7/1996 arts. 53-54). Límite de pagos en efectivo de 1.000 € entre empresario y consumidor (Ley 7/2012 art. 7,
  verificar) → arreglar el contrato B2C p23.

## 4. Ficheros (D10-D13)

- **D10 Checklist 83 tareas 12/16/14/10/16/15** (F1 §3), con cocina de apoyo autorizada (no mise en place en casa), época de
  peligro de incendios, gas (CE, mangueras en fecha, ADR, extintor), FACe; trámites españoles reales intactos.
- **D11 Docx**: reescritura en las 131 ranuras del FT ES + anexo autonómico (11 H1), A4, cifras por token; gemela de
  argumento = el docx del Catering ES 2.2; sin «sin licencia clasificada», «freelance», «validado», inversiones o break-even
  de la 1.x.
- **D12 Calculadora** (F1 §5): hojas Calculadora / Ejemplos / Instrucciones; paelleras por la tabla de raciones por diámetro
  del manual técnico, 1 paellero por cada 3 paelleras, kg de arroz, caldo y gas, IVA 10 %, 0,95 €/km, anticipo 30 % y tramos de
  cancelación de los contratos 1.2, margen calculado, 3 ejemplos por fórmula (boda, empresa, fiesta popular), autotest pycel.
- **D13 Otros 7** (F1 §6): contrato sin «validadas con asesor legal», con cláusula de no desistimiento (art. 103.l) y el
  efectivo; proveedores «Validado» → «Por verificar»; catálogo sin «España 2026 / precio actualizado» como sello; carta sin
  «escandallo» si no lo trae + D5; experiencias p6; **los 7 docx en A4 con docProps 2026** (como el catering).

## 5. Lanzamiento (D14-D16)

- **D14 Landing, dashboard, changelog, hubs** (ES, EN, DE, FR, IT, NL, PT): lista de `F1-camino-2_2.md` §7 (60+ pp., «sin
  licencia clasificada», freelance, inversión 3.500-25.000 y «4-7x menor», break-even 18-22, ICO/microcrédito, 6 hojas,
  10 ejemplos validados, RGSEAA, tarifa plana, 104 hitos, escandallo, roadmap del food truck 30-75K, «validado(s)», planes de
  incendios mal nombrados) → lo que entrega la 2.2; `updateNote` «Producto actualizado · Versión 2.2 · octubre 2026»; entrada
  2.2 honesta en el changelog. «España 2026» solo como contexto SEO, nunca como sello de validación. **Capa comercial
  intacta** salvo la frase de Marc Esteve (John, 11-oct: quitar «4.200 EUR siguiendo el escenario mínimo viable»).
  Sin cifras movibles (DSCR, payback, saldos) en landing ni correo.
- **D15 Gates**: los del catering (motor 13/13, idempotencia, censo, no latinos, autotest calculadora, cifras 1.x prohibidas,
  docx 11 H1 + A4 + 0 tokens, barrido «freelance / validado / carnet de manipulador / sin licencia clasificada / PATRICOVA
  como incendios / PIDOM / INFOCYL») + `gate_restos_ft.py` con restos del **FT y del catering** (excluir «food truck» legítimo
  de la guía de tipos y roadmap). Una revisión opus final. Preview + LIVE con `gate-flujo-postpago --only plan-negocio-paellero-eventos`.
- **D16 Correo**: el borrador `42ccda21` («Paellero 1.2», 18-nov, lo programa el routine del 19-oct) se **sustituye por el de
  la 2.2** en cuanto esté LIVE (lo decide el orquestador en F3: mismo hueco del 18-nov, PATCH con todos los campos).
