# Plan de Negocio Parrillero-Asador para Eventos ES — SPEC 2.2 (F1 · 12-oct-2026 · sesión Claude Code)

> Base: `F1-camino-2_2.md` (camino medido en el VPS sobre la 1.1 LIVE) y `F1-research-parrillero.md` (delta legal/operativo,
> benchmarks, caso y demanda; lo común está en `../catering-es-2_0/F1-research-es.md` y `../paellero-2_2/F1-research-paellero.md`).
> Gemelo y plantilla: el **Paellero ES 2.2** (`../paellero-2_2/`: SPEC, F2-NOTAS, REVISION-FINAL) y la REVISION-FINAL del catering:
> **aplicar desde el principio lo que cazaron sus revisiones**. John (12-oct): «seguimos con el Plan Parrillero-Asador a la 2.2,
> con el mismo método que el catering y el paellero». Versión **2.2** (la anterior es la 1.1). F1 gastó 0,63 M; **F2 + F3 ≤ 1,6 M**.
> Lo que no está aquí no se hace.

## 1. Construcción (D1-D3)

| D | Decisión |
|---|---|
| D1 | Camino del paellero: motor ES de línea A sobre copia del **FT ES v2.2**, módulo `planes-v2_0/contenido_plan_negocio_parrillero_asador_eventos/a.py` **clonado del paellero**; scripts copiados en `parrillero-2_2/` con sus datos reescritos (`semilla_par.py`, `datos_checklist.py`, `cifras_par_es.py`, `tandas_docx.py`, `docx_par_es.py`, `calculadora_par_es.py`, `arreglos_d9.py`, `barrido_es.py`, `ciclo.sh`); `../catering-es-2_0/gate_restos_ft.py` con las opciones de F1-camino §2. **Sin cambios en código común** |
| D2 | Motor sin permutar: invitados por evento × € por invitado sin IVA × eventos al año, rótulos por `VOCABULARIO`. Crecimiento de los años 2-3 = invitados por evento con los mismos eventos; **el docx lo cuenta así**. La nota del motor «el Word sigue en la versión 1.1» es FALSA aquí también (el Word es 2.2): se corrige por `VOCABULARIO` como en el paellero; las menciones a «la versión 1.1» como versión anterior son ciertas y se dejan |
| D3 | Mismos 11 nombres de fichero (no se toca `get-download-urls.ts`). Se REHACEN plan financiero, checklist, calculadora y docx del plan. Los otros 7 se conservan con los parches de D13 (manual, carta, experiencias, contratos, guía, catálogo, proveedores) |

## 2. Caso, precios y fiscalidad (D4-D7)

| D | Decisión |
|---|---|
| D4 | Caso = research §3 tal cual: **95 eventos · 80 invitados · 25 € sin IVA** (mezcla: 12 bodas × 110 × 42 € · 30 empresa × 70 × 31 € · 45 privados × 40 × 25 € · 8 fiestas/ferias × 300 × 10 €), comida/bebida 88/12, mercancía 32/30 %, consumibles 4,5 %, varios 5 %, «asado para llevar» 5 % con comisión 2 % (sube si lo exige la demo, como en el paellero), cocina de apoyo 1.000 €/mes, seguros 1.950 €/año, fijos 11.050 € (si el molde pide 10 filas, se completa sin mover el caso), plantilla de 4 filas del research (titular 1.0 + tres fijos discontinuos), inversión 49.900 € en 15 partidas (14 filas del molde: se juntan dos), 22.000 € propios + préstamo **CALIBRAR** (≈ 62.000 €, 6,5 %, 6 años, 1 de carencia), cobro/pago 15/15, estacionalidad del research, escenarios y umbrales del research, **SL unipersonal**. Regla D15: holgura ≥ 15 % el año 1 y **se informan las de los años 2 y 3** |
| D5 | **Precios coherentes en los 4 sitios** (Excel, calculadora, experiencias, landing): el Excel usa la mezcla; la calculadora sale de la materia prima por experiencia y la tabla de escalado del research §2; las experiencias pasan a «orientativo, sin IVA» dentro de los rangos del research; la carta no tiene precios y no se le añaden. La landing no cita los 25 € sin su mezcla |
| D6 | IVA 10 % (catering con servicio), también la bebida. **Sin retención de IRPF en las facturas** (677.9 es actividad empresarial, RIRPF art. 95.6): fuera el «7 %/15 %» de la 1.1 en todos los ficheros |
| D7 | Ayudantes y 2.º parrillero **fijos discontinuos**; nunca «freelance»; formación en higiene alimentaria a cargo de la empresa (no «carnet»). Show cooking por jornada en restaurante: **fuera del caso**, el docx lo cita como línea extra sin cifras. Fiestas: el caso modela solo el **encargo** municipal (contrato menor, sin anticipo, 30 días, FACe); la concesión de barra o puesto con canon va como nota (venta directa, Ley 7/1996) sin cifras |

## 3. Fuego, brasa y carne (D8-D9) — research §0-§1, con su fuente en la nota correspondiente

- **D8 Fuego y brasa**: la brasa es el producto, así que la alerta de incendios le quita el servicio → **plan B de gas** (plancha o
  piedra volcánica, 1 botella < 15 kg por aparato, RD 919/2006) en inversión, contrato (fuerza mayor B2C **y B2B**: alerta →
  gas o cambio de fecha), checklist y docx. Brasas y cenizas apagadas con agua en contenedor metálico con tapa; parrilla a ≥ 3 m de
  carpas; ordenanza de humos en suelo urbano (sin cifras de ordenanzas no leídas en origen); carbón con ficha de seguridad.
  Fuego al aire libre = norma autonómica (Ley 43/2003 art. 44.3); «la licencia de la finca no levanta la restricción en terreno
  forestal». Anexo autonómico del **Paellero 2.2 trasplantado** (8 comunidades) cambiando gas/paellera por carbón/leña/parrilla.
  Fuera PATRICOVA (es de inundaciones), INFOCYL (→ INFOCAL), «finca con licencia OK».
- **D9 Carne**: recepción ≤ 7 °C carne · ≤ 3 °C despojos · ≤ 4 °C aves y preparados · ≤ 2 °C picada (Reg. 853/2004 como
  estándar del APPCC); cocción 70 °C en el centro (carne) y 74 °C (aves) según AESAN (🟡: se cita como recomendación);
  «poco hecho» solo en piezas enteras e intactas de vacuno o cordero, a petición; mantenimiento ≥ 63 °C y comida testigo
  (RD 1086/2020 art. 30); chuletón con vértebra solo de origen de riesgo insignificante (España) o < 30 meses, y nunca
  deshuesado por el parrillero (RD 1086/2020 art. 26.2); denominación por edad de la etiqueta; «madurada X días» solo con
  documento del proveedor. Esto va al **manual** (tabla nueva «8. Escalado por invitados» + recepción/cocción) y al docx §6.

## 4. Ficheros (D10-D13)

- **D10 Checklist 83 tareas 12/16/14/10/16/15** (F1-camino §3), base `../paellero-2_2/datos_checklist.py`: registro sanitario
  autonómico, cocina de apoyo autorizada (nada de mise en place en casa), comida testigo, época de peligro, plan B de gas, brasas,
  carne en frío (ATP), sin retención, sin «alta CNAE», sin tarifa plana con cifra, sin «carné» (gotcha carne/carné del paellero).
  Pestañas ≤ 31 caracteres. `Instrucciones!A3` y docProps del parrillero desde el día 1.
- **D11 Docx**: reescritura en las 131 ranuras del FT ES + anexo autonómico (11 H1), A4, cifras por token, gemela = Paellero ES 2.2,
  2 redactores Sonnet (`par_es_a` §1-5 · `par_es_b` §6-10). Prohibidos de F1-camino §4 (incluida la lista de cifras 1.x). La FAQ
  implícita del research (finca privada, asado para 50, alerta de incendios) entra en las ranuras que toque, sin sección nueva.
- **D12 Calculadora** (F1-camino §5 + research §2/P4): `Calculadora` · `Ejemplos` · `Instrucciones`; canal Particular / Empresa /
  Ayuntamiento con desplegable; formato → gramos de carne cruda; experiencia (las 10) → materia prima por invitado; tabla de
  escalado al pie (parrillas, parrilleros, ayudantes, kg de carbón); personal a €/h × 1,33; margen por canal visible; desplazamiento
  aparte a 0,95 €/km sin margen; IVA 10 %; cobro B2C 30/40/30, empresa 30 + 70 a 30 días, ayuntamiento 0 % (LCSP 198);
  cancelación por los tramos corregidos de D13; 3 ejemplos por fórmula (boda ~100 inv. asado argentino + show de fuego · empresa ~70
  BBQ texano · fiesta/feria 300 de volumen); autotest pycel ± 0,01 €.
- **D13 Otros 7** (F1-camino §6, todo): los 7 docx a **A4 con docProps 2026** (autor AI Chef Pro, sin «python-docx»); contrato con no
  desistimiento (103.l), tramos sin huecos, plan B, fuerza mayor B2B, fuero del consumidor (TRLGDCU art. 90.2), factura de cada pago
  (también la señal, LIVA art. 75.Dos), sin retención, Anexo I orientativo; carta (IGP Lechazo, Marca de Garantía Cochinillo de
  Segovia, villaroy, 220 °C); experiencias «orientativo» y alioli con ovoproducto; catálogo y guía según §6; manual con la tabla de
  escalado y la de temperaturas (D9); proveedores **93**, «Por verificar», score vacío, nota EUDR en el bloque del carbón.

## 5. Lanzamiento (D14-D16)

- **D14 Landing, dashboard, changelog, hubs ×7, email post-compra** (`netlify/functions/verify-purchase.ts:496`): la lista de
  F1-camino §7 completa → lo que entrega la 2.2 (Word de 10 secciones con anexo, Excel de 9 hojas, calculadora de presupuestos con
  IVA, 93 proveedores, checklist de 83 tareas). `updateNote` «Producto actualizado · Versión 2.2 · octubre 2026»; changelog 2.2
  honesto. «España 2026» solo como contexto SEO, nunca como sello. Sin cifras movibles (DSCR, payback, saldos) en landing ni correo.
  **Capa comercial intacta** salvo dos frases de testimonios (regla de John del 11-oct): Federico Aguirre («96… Validados, con
  teléfonos y notas reales» → 93, sin «validados») y Marcos Pérez (fuera «3.800 EUR siguiendo el escenario mínimo viable», como
  Marc Esteve), en la ficha Y en `src/data/testimonials-plan-parrillero-asador-eventos.ts`. Sandra Vera («parrillera… freelance»
  es su rol, no afirma nada del kit): **no se toca**; se le menciona a John.
- **D15 Gates**: los del paellero (motor TODO VERDE, idempotencia, censo `--fail` 0, no latinos 0, autotest calculadora, cifras 1.x
  prohibidas, docx 11 H1 + A4 + 0 tokens, barrido «freelance / validad / carnet / carné / tarifa plana / sin licencia / PATRICOVA /
  INFOCYL / retención / España 2026») + `gate_restos_ft.py` con restos del FT, del paellero y del catering (excluyendo el «food
  truck» legítimo de la guía y del catálogo). **Una** revisión opus final. Preview + LIVE con
  `gate-flujo-postpago.py --only plan-negocio-parrillero-asador-eventos`, carrusel, miselup, robots.
- **D16 Correo**: borrador nuevo «Actualización Plan de Negocio Parrillero-Asador 2.2 (ES)» desde la plantilla del paellero 2.2,
  hueco **23-nov 08:00Z**; como está a > 30 días, se programa con un routine el 24-oct o después (como los del 19 y 20-oct) y se
  anota en CALENDARIO. Prueba a John.
