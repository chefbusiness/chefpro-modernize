# Pack de Plantillas APPCC — v2.0 (SPEC, 2026-08-22)

Origen: ronda 1 adversarial (`auditorias/pack-appcc-R1.json`, 3 lentes opus: consultor de seguridad
alimentaria, técnica Excel, coherencia; 92 hallazgos, 15 altas, «no listo» ×3). Lo que sigue es lo que
SE HACE; lo demás se descarta con motivo en §7. Método y referencias de código: igual que
`kit-escandallos-v2-SPEC.md` (paquete `kit-escandallos-v2_0/`: `main.py --dry-run / --solo /
KIT_*_APPLY=1` con respaldo, motor + grupos, `inject_cache.py` al final, verificación `data_only`,
censo `--fail`, idempotencia por reconstrucción). Ficheros: `astro-site/public/dl/pack-appcc/`
(17 xlsx) + 4 registros nuevos. Nada de builds locales ni Playwright; python en serie; `istats`.

Principio rector: **todo lo que se imprime y se enseña a un inspector tiene que ser defendible**:
límites legales correctos, normas vigentes, registros que existan para cada PCC, y fórmulas que no
den «OK» a un dato fuera de límite. Convención: celdas editables verdes (`E8F5E9`); columnas Estado
con semáforo (verde `C6EFCE`/`006100`, ámbar `FFEB9C`/`9C6500`, rojo `FFC7CE`/`9C0006`); DV con
`showErrorMessage=True`; `IFERROR`/guardas de vacío en todas las fórmulas; rangos de DV, fórmulas y
COUNTIF sobre 200 filas (o las que tenga la hoja ampliada), sin ListObject.

## 1. Motor común (`motor.py`) — aplica a los 21 ficheros
1.1 **Semáforo** (TEC-02, alta): formato condicional en toda columna de estado/veredicto:
OK/✓/Cumple/VIGENTE → verde; VIGILAR/⚠/INCOMPLETO/CADUCA PRONTO/RENOVAR → ámbar;
ALERTA/RECHAZAR/CAMBIAR/REVISAR/✗/CADUCADO/EXCESO → rojo. Helper `semaforo(ws, rango, vocabulario)`.
1.2 **DV que valida** (TEC-10): todas las listas con `showErrorMessage=True`, `errorTitle`/`error`
en español; `allow_blank` solo donde el vacío es legítimo. Rangos extendidos a TODAS las filas de
datos, incluidas las precargadas (TEC-25, TEC-11).
1.3 **Filas y rangos** (TEC-20, TEC-26, COM-24): registros mensuales con 31-40 filas, anuales con
80; fórmulas de estado, DV y relleno verde replicados en todas las filas; COUNTIF/resúmenes sobre el
rango completo. Helper `replicar_filas(ws, hr, desde, hasta)`.
1.4 **Impresión** (TEC-13/TEC-14/TEC-29/COM-12/COM-23): `print_title_rows` en todas las hojas de
registro; `print_area` que cubra el pie legal y de marca; A4 (el cartel BONUS-02 se queda en A4 y el
texto dice «A4, o amplía a A3 desde el diálogo de impresión»: DOM-30/TEC-21/COM-13).
1.5 **Ejemplos sembrados** (DOM-03/COM-09, alta): en cada registro que se entrega vacío, 2-3 filas de
ejemplo realistas, marcadas «(ejemplo)» en observaciones, con fechas genéricas; el resto vacío.
1.6 **Conservación de registros** (DOM-35/TEC-17/COM-21): una sola frase en todos los pies:
«Conservar al menos 2 años (trazabilidad y proveedores: 5); el Reg. (CE) 178/2002 exige trazabilidad
pero no fija plazo — consulta la guía de prácticas correctas de higiene de tu comunidad autónoma».
1.7 **Marco normativo vigente** (DOM-07/08/14/18/21/28, TEC-19, COM-05/16, altas y medias):
sustituciones exactas en todos los ficheros: «RD 2207/1995» → «Orden de 26 de enero de 1989 (Norma
de Calidad de aceites y grasas calentados): máx. 25 % de compuestos polares»; «RD 140/2003» → «RD
3/2023, de 10 de enero»; «carné/certificado de manipulador vigente» → «formación en higiene
alimentaria acreditada por la empresa (Reg. (CE) 852/2004, Anexo II, Cap. XII; el carné oficial se
suprimió con el RD 109/2010)»; escala de gravedad «GRAVE/MODERADA/LEVE» → «Leve / Grave / Muy grave
(Ley 17/2011, arts. 50-52)»; «hasta €60.000» → «de 5.001 a 20.000 € en las graves y hasta 600.000 €
en las muy graves (Ley 17/2011)». Bloque «Marco normativo» en las Instrucciones del 12: Reg. (CE)
852/2004 art. 5, RD 3484/2000, Reg. (CE) 178/2002 arts. 18-19, Reg. (UE) 1169/2011 + RD 126/2015,
Reg. (CE) 853/2004 Anexo III + RD 1420/2006 (anisakis), Reg. (CE) 2073/2005, Ley 17/2011.
1.8 **Instrucciones** de cada fichero reescritas para describir exactamente la hoja (columnas nuevas,
límites, frecuencia recomendada, semáforo, conservación); línea «Versión 2.0 · agosto 2026 ·
aichef.pro/pack-appcc · info@aichef.pro». Metadata de la Fase A se conserva.

## 2. Grupo A — registros con medición (01, 02, 05, 06, 09, 10) — `grupo_a.py`
- **01 temperaturas diario**: congeladores `<=-18` sin suelo (DOM-09/TEC-05/COM-18); caliente `>=65`
  sin techo (TEC-31); rótulos coherentes; columnas Hora M / Firma M / Hora T / Firma T y «Nº
  incidencia (→ 11)» (DOM-34); semáforo.
- **02 recepción temperaturas**: límites por familia en el desplegable (pescado fresco 0-2 °C en
  hielo; carne picada y preparados ≤2; despojos ≤3; aves/caza ≤4; lácteos/platos ≤4; canales y
  despieces de vacuno ≤7; congelados ≤-18; ambiente N/A) con una hoja auxiliar «Límites» y fórmula
  `=IF(OR(D="",E=""),"",IF(E="N/A","OK",IF(D<=E,"OK","RECHAZAR")))` (DOM-04/TEC-01, altas); DV
  obligatoria; aviso rojo si Estado=RECHAZAR y Aceptado=S (TEC-30); Instrucciones con la tabla.
- **05 recepción mercancías**: columnas «Nº albarán», «Nº lote», «Firma receptor» (DOM-23); nota de
  que 02 es el PCC de temperatura y 05 la verificación documental (no se fusionan: claves del dashboard).
- **06 trazabilidad**: pestaña «Salida / uso interno» (fecha, lote de origen, elaboración, cantidad,
  destino/servicio) (DOM-22/TEC-24/COM-21); textos «< 4 horas» → «de forma inmediata a requerimiento
  de la autoridad»; nota de conservación §1.6.
- **09 aceite**: `>=25` CAMBIAR, `>=20` VIGILAR (TEC-06); temperatura en el veredicto `OR(D>=25,E>180)`
  (TEC-07/DOM-25/COM-19); pestaña «Retirada de aceite usado» (fecha, litros, gestor autorizado, nº
  documento, firma); normativa §1.7.
- **10 agua**: guardas invertidas (`INCOMPLETO`/`FALTA CLORO`/`REVISAR`) (DOM-32/TEC-15); 31 filas;
  frecuencia en Instrucciones (diaria con depósito, semanal con red) (COM-24); RD 3/2023.

## 3. Grupo B — planes, checklists, HACCP, guía (03, 04, 07, 11, 12, 13, 14, 15) — `grupo_b.py`
- **03 plan L+D** (DOM-05 alta): fregaderos → «Desincrustante ácido (aclarar por completo) —
  desinfectar en una SEGUNDA pasada con hipoclorito 1:50»; E11 «NUNCA mezclar ácido y lejía»;
  bloque EXTERIOR (terraza/entrada, contenedores, zona de carga) + lavamanos, desagües/sumideros,
  maquinaria (cortafiambres, picadora, batidora), paños/bayetas, máquina de hielo, cámara de residuos
  → ≥ 26 filas (DOM-11/TEC-12/COM-06); columnas «Tiempo de contacto» y «Nº registro / FDS (S/N)» +
  pestaña «Productos químicos» (DOM-12); DV de frecuencia ampliada y partir C9 (DOM-31/TEC-11).
- **04 limpieza diaria**: columnas M/T por día para las tareas de doble frecuencia + bloque «TAREAS
  SEMANALES» con fecha y firma (DOM-13/TEC-27); DV «✓,✗,N/A» en B6:H28 (TEC-22); print_area hasta el
  pie (DOM-29/TEC-13/COM-23).
- **07 plagas**: «Nº ROESB» en cabecera; columnas «Nº registro biocida» y «Plazo de seguridad (h)»;
  pestaña «Plano de cebos» (rejilla numerada: nº estación, ubicación, tipo, fecha de revisión)
  (DOM-16); 80 filas (TEC-20).
- **11 acciones correctivas**: columnas «Producto / lote afectado», «Destino del producto no
  conforme (desechado/devuelto/reprocesado/liberado)» con DV, «Acción preventiva», «Registro de
  origen» (DOM-24).
- **12 análisis de peligros** (corazón): columnas «Medida preventiva», «Vigilancia (frecuencia y
  responsable)», «Verificación (qué, quién, cuándo)» (DOM-17); «Nivel de riesgo» calculado
  (Probabilidad × Gravedad → Bajo/Medio/Alto/Crítico) y decisiones de PCC coherentes (TEC-08);
  filas 6 y 17 reclasificadas como PPRo con nota (COM-20); filas nuevas: DESCONGELACIÓN (PCC, ≤4 °C
  tapado sobre bandeja), huevo fresco sin tratamiento térmico (ovoproducto pasteurizado salvo ≥75 °C),
  **Anisakis** (PCC, −20 °C 24 h o −35 °C 15 h, registro 18) (DOM-06 alta/DOM-26); columna J
  reapuntada a registros que EXISTEN: cocción → 16, enfriamiento → 17, servicio → 01 (exposición
  caliente), checklist semanal → 04 (bloque semanal) (DOM-01/TEC-04/COM-04, altas); «7 fases»; DV
  sobre todas las filas (TEC-25); marco normativo §1.7.
- **13 higiene personal**: formación acreditada (DOM-14); print_area (TEC-29).
- **14 fichas alérgenos**: protocolo en 8-10 pasos en dos bloques (antes de cocinar / si hay
  reacción: cambio de guantes, utensilios y tabla exclusivos, sin freidora ni agua compartidas, entrega
  en mano, decir «no se puede garantizar», 112 solo ante síntomas) (DOM-27); wrap y altura (TEC-09);
  sulfitos «expresado como SO2» (TEC-32).
- **15 guía inspección**: 25 puntos reales (añadir «registro de congelación preventiva de anisakis»
  y «verificación de termómetros») (DOM-10/COM-07); escala Ley 17/2011 (DOM-28); bloques «Antes de
  la inspección», «Documentos que tener listos», «Errores que más se sancionan» (DOM-10); resumen
  con COUNTIFS de muy graves/graves incumplidos, % de cumplimiento y «Sin responder» (TEC-16/TEC-10).

## 4. Grupo C — alérgenos, registros nuevos y bonos (08, 16, 17, 18, 19, BONUS-01, BONUS-02) — `grupo_c.py`
- **08 matriz de alérgenos** (DOM-02/TEC-03/COM-17, altas): los 8 platos de ejemplo con su
  declaración real (César: gluten S, huevo S, lácteos S, pescado S, mostaza S; croquetas de jamón:
  gluten S, lácteos S, huevo T; paella mixta: crustáceos S, moluscos S, pescado S, gluten T; tarta de
  queso: lácteos S, huevo S, gluten S; etc., rellenando las 14 columnas de los 8); columna
  «Verificado» `=IF(COUNTBLANK(D6:Q6)>0,"⚠ SIN VERIFICAR","Completo")` con semáforo; rangos a 200
  filas (DOM-19); cabeceras «Cereales con gluten (indicar cuál)» y «Frutos de cáscara (indicar cuál)»
  + columna «Especificación» (DOM-20); cabeceras con wrap (TEC-18).
- **16-registro-coccion-regeneracion.xlsx** (nuevo): fecha, plato, hora, T.ª en el centro, tiempo,
  sonda, firma; Estado `>=75` OK / «REPETIR»; semáforo; 40 filas; Instrucciones.
- **17-registro-enfriamiento-descongelacion.xlsx** (nuevo): pestaña «Enfriamiento» (producto, hora y
  T.ª inicio, hora y T.ª a 2 h, destino; Estado: de ≥60 a ≤10 °C en ≤2 h → OK / ALERTA) y pestaña
  «Descongelación» (producto, lote, inicio, fin, T.ª cámara ≤4, uso en ≤24 h; Estado).
- **18-registro-congelacion-anisakis.xlsx** (nuevo): pescado, lote, fecha/hora entrada y salida,
  T.ª congelador, Estado: ≥24 h a ≤−20 °C (o ≥15 h a ≤−35) → OK; nota legal Reg. 853/2004 + RD
  1420/2006.
- **19-verificacion-termometros.xlsx** (nuevo): equipo/sonda, fecha, método (hielo fundente 0 °C ±1
  / ebullición), lectura, desviación calculada, Apto S/N con fórmula, acción, firma; mensual.
- **BONUS-01 formación**: «Válido hasta», «Firma del empleado», Estado con TODAY() (VIGENTE / RENOVAR
  <60 d / CADUCADO) + contador de caducados (DOM-33/TEC-28/COM-25). pycel: TODAY() se cachea con la
  fecha de generación — aceptable (Excel recalcula al abrir); anotarlo en el informe.
- **BONUS-02 protocolo**: PASO 3 = notificar de inmediato a la autoridad sanitaria de la comunidad
  autónoma (art. 19 Reg. 178/2002) y al proveedor; 112 solo ante personas con síntomas (DOM-21);
  «imprime en A4 (o amplía a A3)».

## 5. Integración (sonnet) — producto, landing, dashboard, changelog
- `PRODUCT_FILES['pack-appcc']`: claves nuevas `coccion`, `enfriamiento`, `anisakis`, `termometros`
  → `/dl/pack-appcc/16-…`, `17-…`, `18-…`, `19-…`; tarjetas en `PackAppccDashboard.tsx` (orden 16-19
  antes de los bonos); hero del dashboard con el recuento real.
- Landing `astro-site/src/data/productos/kits/pack-appcc.ts`: **«19 registros + 2 bonus»** en todos
  los sitios donde decía 17 (hero, grid.countGold, seo, schema, FAQ, CTA); «25+ zonas» solo si el 03
  supera 25 (si no, la cifra real); «7 fases»; «25 puntos» reales; «fórmulas y alertas automáticas»
  → «alertas automáticas con semáforo en los registros de medición; planes, checklists y carteles
  listos para imprimir»; «PDF imprimible» → «listo para imprimir en A4 desde Excel» (COM-10: no se
  entregan PDF); «Cumple RD 2207/1995 y RD 140/2003» → normas vigentes §1.7; «€60.000» → §1.7;
  pre-rellenado matizado (COM-09); testimonios con nombres de establecimiento claramente ficticios
  (COM-14); imágenes de los bonos por `appcc-registro-plantilla.jpeg` / `appcc-inspector-sanidad.jpeg`
  (COM-11) — comprobar que existen; **NO tocar** `aggregateRating`/`reviews`/`priceOld`/
  `discountBadge`/`priceValidUntil` (aparcado por John: COM-01/02/22).
- Gemelos de la SPA `src/components/pack-appcc/*` y `src/pages/PackAppcc.tsx`: alinear los textos
  citados (fuente histórica).
- Changelog: entrada 2.0 (2026-08-22), `version`/`updated` a 2.0, una línea por bloque en lenguaje
  de cliente; `updateNote` «Producto actualizado · Versión 2.0 · agosto 2026»; línea de versión 2.0.
- Gates: `censo-entregables.py --only <carpeta> --fail`, `gate-flujo-postpago.py --offline --only
  pack-appcc` (los 4 ficheros nuevos solo existen en la copia hasta la ejecución real: aviso esperado),
  idempotencia, data_only, pycel cambiando inputs (cada fórmula de Estado debe cambiar de OK a
  ALERTA/RECHAZAR con un dato fuera de límite), esbuild de los .ts/.tsx.

## 6. Ejemplo de lo que debe poder demostrarse en la ronda de refutación
Pescado fresco recibido a 4 °C → RECHAZAR; vacuno en canal a 6 °C → OK; arcón a −26 °C → OK; baño
maría a 102 °C → OK; aceite 25,0 % → CAMBIAR; aceite 18 % a 200 °C → CAMBIAR; agua turbia sin cloro
→ REVISAR; cocción a 72 °C → REPETIR; enfriamiento 60→12 °C en 2 h → ALERTA; anisakis 20 h a −20 →
ALERTA; termómetro que lee 1,5 °C en hielo → NO APTO; formación con «válido hasta» pasado → CADUCADO;
matriz: paella con crustáceos S; plan L+D sin ácido+lejía; 25 puntos contados; 7 fases; «RD
2207/1995», «RD 140/2003», «carné de manipulador» y «€60.000» con 0 ocurrencias en los 21 ficheros y
en la landing.

## 7. Descartado con motivo
- COM-01/COM-02/COM-22 (reseñas, ancla de precio, priceValidUntil): aparcado por John (2026-08-22).
- COM-15 (garantía en /terminos): toca `src/i18n/**`, territorio de la sesión del VPS → se anota para
  John en el handoff, no se toca aquí.
- COM-10 como «generar PDF»: se corrige el copy; los PDF de los carteles quedan para otra versión.
- TEC-23/DOM-23 «fusionar 02 y 05»: no (claves y tarjetas distintas); se complementan.
- TEC-26 como ListObject: no; rangos ampliados con fórmula/DV replicadas (§1.3).
