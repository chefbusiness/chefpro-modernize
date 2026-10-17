# F1 census — Guía «Cómo Montar una Pastelería» → EN (US) (solo lectura, 2026-10-16)

Worktree: `/private/tmp/claude-501/-Users-johnguerrero-chefpro-modernize/17431ae6-e038-4c3b-a275-12ea4eb3e4f0/scratchpad/wt-bakery` (rutas abajo, relativas a él). Nada editado, nada construido. La mecánica compartida (GuiaLandingPage con `lang`, registro en 5 fuentes, dashboard EN, `tienda.ts`, gates) ya está documentada en `scripts/productos-digitales/guia-food-cost-en/F1-census.md` y su `SPEC.md`; aquí solo el DELTA. Palabras = `len(texto.split())` sobre el `.md` (es el contador de `informe.json`: 57.623 / 16.744 / 8.059; las cifras 56.814 / 16.668 / 7.801 del encargo son de otro recuento). Conteos de menciones = regex sobre el `.md` (orientativos).

## 0. Hallazgos que cambian el plan (leer primero)

1. **Casi todo es clase A.** De 48 secciones `## ` (24 guía + 15 bonus + 9 plan) solo **9 son T** (portadas ×3, Índice del plan, «Sobre el autor» ×3, cap. 7, decisión 2) = **4.749 palabras**; **39 secciones A = 77.677 palabras (94 %)**. Cualquier regla «opus si hay una A» deja las **19 tandas en opus, 0 en sonnet**. Para abaratar: separar T de A solo sirve en cap. 7 (1.915 pal., T04) y decisión 2 (1.215 pal., B01); el resto es A. Hay 12 secciones «A-» (ligeras: 1-3 citas legales/fiscales sueltas, p. ej. cap. 5, 11, 12, 16, 20 y dec. 3, 4, 7, 9, plan §1, §3, §6) que un sonnet con marcas `⟦ADAPT⟧` + revisión opus podría hacer, si John lo prefiere a opus puro.
2. **La capa fiscal es estructural, no cosmética.** El modelo entero está construido sobre **«PVP con IVA» tecleado** (carta: `L6=1.6`, `M6=0.10`, `N6=L6/(1+M6)`; food cost y todos los ingresos se calculan sobre PVP **sin** IVA). En EE. UU. el precio de carta es pre-tax. Si se copian los PVP «con IVA» como pre-tax (1,60 → $1.60) cambian ingresos (322.198 €), ticket (5,87), punto de equilibrio y plan; si se deja el sin-IVA (1,4545) salen precios feos. **Decisión de SPEC obligatoria** (el precedente Food Cost resolvió con matriz de impuestos a 0 % por defecto y precio pre-tax tecleado; aquí hay además un **IVA 4 % para el pan** y un **IVA soportado/repercutido/modelo 303** en tesorería que no tienen equivalente).
3. **El libro de licencias es ley española pura**: `checklist-legal-y-licencias.xlsx` (7 hojas, 715 textos) = 30 trámites F1-F6 + árbol de registro sanitario (RGSEAA, 4 CCAA) + árbol «suministro a otros minoristas» (art. 3 RD 1021/2022) + ruta doméstica (art. 13.8/13.9) + registro de formación + cronograma. Y `carta-de-apertura…xlsx` lleva la hoja **«Decisión de Huevo y Temperatura»** (art. 9 RD 1021/2022, techos 4 °C / 8 °C / 24 h). Hay que **reconcebirlos** (county/state health department, FDA Food Code, cottage food laws por estado, ServSafe/food-handler cards), con hechos solo de la Equivalents Guide (regla D7 del precedente) o con research nuevo. Los hechos legales US **no están en el repo**: sin research nuevo no se pueden inventar.
4. **Convenio colectivo de Madrid en 3 libros** (plantilla-turnos, plan-financiero «Personal», carta «Coste Hora»), con claves de texto («Grupo 2», «Dirección, jefes y encargados»…) usadas por `MATCH`/`INDEX`: al traducir hay que mantener coherencia de claves. 15 pagas, SS 33 %, SMI RD 126/2026, 1.780 h/año. En US: sin convenio; payroll taxes/workers' comp/FLSA/overtime/tips; el parámetro `ss_empresa=0.33` no vale.
5. **Las seis campañas son españolas** (Reyes, San Valentín, Día del Padre y de la Madre, Semana Santa, Comuniones, Todos los Santos) y el rediseño cambia las cifras derivadas citadas en el texto (22.479 € campañas, 7,0 %, 21.270 € incremental, refuerzo 3.795,51 €, 2.856 piezas/día Reyes, déficit 1.656). 12 de las 30 referencias de la carta son específicas de España (8 de Temporada). Si "cifras idénticas" manda, hay que **renombrar** (p. ej. Reyes → Christmas/holiday) conservando los números, o recalibrar y recalcular todo el texto: decisión de SPEC con impacto en cap. 2, 3, 15, 16, 20, dec. 5, 6, 9, plan §2 y xlsx estacionalidad.
6. **Otros hallazgos menores**: (a) 9 proveedores verificados con URL (Sosa, Puratos, Barry Callebaut, Valrhona, Debic, Elle & Vire, Ylla 1878, Coromina, Cospan) + 7 marcas de equipamiento (UNOX, SMEG, Docriluc, Irinox, Sammic, Selmi, Salva) con precios de fichas de distribuidores españoles (€ con/sin IVA): en US hacen falta proveedores/precios nuevos verificados; Hosply.pro (directorio HORECA español del grupo, con UTM) no aplica. (b) Hay 10 citas a vídeos/fuentes españolas con fecha (`«…» (2025-11-21)`, «Matías, dueño de una pastelería en España», Pastelerías Pomar PS-53, traspasos de Barcelona PS-69…). (c) Los entregables van con `PS-*`/`PA-*` (cifras citadas de la investigación española). (d) El cross-sell ES enlaza a **kit-tareas-pasteleria (12 €, sin gemelo EN)**, kit-escandallos (EN: food-cost-templates), pack-appcc (EN: haccp-templates) y Guía Food Cost (EN: food-cost-menu-engineering-guide). (e) Precio: repo **65 €** (`netlify/shared/product-prices.ts:19`); confirmar USD. (f) Colisión de keywords/slug con `bakery-business-plan` (panadería). (g) `guia-pasteleria-en/` ya contiene `split_md.py`, `gate_md_en.py`, `render_en.py`, `ensamblar_md.py`, `xlsx/` (scaffold del precedente; no revisado aquí; ojo con las constantes de Food Cost que haya dentro).

## 1. Por sección

Clase **T** = traducir; **A** = readaptar a EE. UU.; **A-** = A ligera (pocas citas sueltas). Columnas: palabras · clase · nº de «€» · nº de «%» · menciones de «IVA» · nº de ids `PS-*`/`PA-*` distintos · items de España (regex, top 7) · unidades (nº de apariciones; ninguna sección usa `ft`/`lb`/`°F`). El índice de la guía y del bonus se marca A porque resume capítulos readaptados.

### 1.1 Guía (`guia-pasteleria-obrador.md`)

| Sección | Pal. | Cl. | € | % | IVA | PS/PA | Items específicos de España | Unidades |
|---|---|---|---|---|---|---|---|---|
| 0 (portada) | 178 | T | 0 | 0 | 0 | 0 |  |  |
| Índice | 821 | A | 0 | 0 | 4 | 0 | convenio 2, ayuntamiento 1, Comuniones 1, BOE 1 |  |
| 1. Qué Negocio Estás Montando: las Once Variantes y Cuá… | 3091 | A | 52 | 6 | 2 | 10 | RD 1021/2022 5, ayuntamiento 3, convenio 2, RGSEAA 2, RD 1086/2020 1, Salva 1, Reyes 1 |  |
| 2. El Cliente y la Plaza: Quién Compra Pastelería y Cuá… | 2325 | A | 19 | 22 | 3 | 8 | Navidad 1, Reyes 1, San Valentín 1, Día del Padre 1, Semana Santa 1, Comuniones 1, Todos los Santos 1 |  |
| 3. La Carta de Apertura: Treinta Referencias y por Qué … | 3033 | A | 66 | 36 | 6 | 0 | Reyes 3, Roscón 2, Barcelona 1, Navidad 1, Torrijas 1, Huesos de santo 1, Panellets 1 |  |
| 4. Cuánto Cuesta Abrir: el CAPEX Real, Partida a Partida | 2639 | A | 135 | 10 | 20 | 17 | Docriluc 2, Sammic 2, ayuntamiento 1, UNOX 1, SMEG 1, Irinox 1, Selmi 1 | g/kg 3, °C 1, m² 5, L/ml 1 |
| 5. El Local: Metros, Zonas y la Ficha de Visita | 2125 | A- | 0 | 10 | 0 | 2 | RD 1021/2022 2, BOE 2 | °C 1 |
| 6. Antes de Firmar el Alquiler: el Capítulo que Ahorra … | 3460 | A | 43 | 0 | 0 | 2 | ayuntamiento 8, Barcelona 8, CTE 1, RD 1027/2007 1, Milanuncios 1, negociosenventa 1 |  |
| 7. El Obrador por Dentro: Frío, Calor y Flujo de Trabajo | 1915 | T | 1 | 14 | 1 | 0 | RD 1021/2022 1, Reyes 1 | g/kg 1, °C 5, L/ml 1 |
| 8. Maquinaria: Qué Compras, Qué Alquilas y Qué Esperas … | 2651 | A | 58 | 0 | 45 | 0 | Sammic 6, Docriluc 5, Selmi 4, Irinox 3, UNOX 2, SMEG 2, Salva 2 | g/kg 3, °C 1, L/ml 2 |
| 9. Licencias, Sanidad y Registro: el Camino Completo | 2948 | A | 2 | 3 | 0 | 0 | RD 1021/2022 8, RGSEAA 4, ayuntamiento 3, BOE 3, RD 191/2011 2, Comunidad de Madrid 2, BOCM 1 | g/kg 2 |
| 10. Autocontrol, Alérgenos y Formación: Qué Tener el Dí… | 2911 | A | 5 | 0 | 0 | 0 | RD 1021/2022 8, Reglamento (CE) 852/2004 3, RD 126/2015 3, RD 202/2000 2, RD 109/2010 2, Reglamento (UE) 1169/2011 1, RGSEAA 1 |  |
| 11. Proveedores: Materia Prima, Packaging y Plazos | 2035 | A- | 18 | 6 | 0 | 0 | Sosa 4, Ylla 3, Coromina 3, Cospan 3, Cataluña 1, Hosply 1 | g/kg 2 |
| 12. Escandallo y Precios: por Qué la Mano de Obra Manda | 3515 | A- | 102 | 42 | 0 | 0 | convenio 2, Real Decreto 1021/2022 1, Roscón 1, Reyes 1, Torrijas 1, Huesos de santo 1, Panellets 1 | °C 5 |
| 13. El Equipo: Cuántos, Qué Perfiles y Qué Cuestan | 2322 | A | 52 | 0 | 0 | 0 | convenio 23, BOCM 6, Seguridad Social 5, Comunidad de Madrid 4, SMI 2, RD 126/2026 1 |  |
| 14. Turnos de Madrugada y Jornada Legal | 2034 | A | 0 | 0 | 0 | 0 | Estatuto de los Trabajadores 1, RDLeg 2/2015 1, RD-ley 8/2019 1, Navidad 1 |  |
| 15. Los Seis Picos del Año | 2933 | A | 48 | 13 | 3 | 0 | Reyes 16, San Valentín 5, Navidad 4, Día del Padre 3, Semana Santa 3, Comuniones 3, Todos los Santos 3 |  |
| 16. Encargos y Comuniones como Línea de Negocio | 2399 | A- | 15 | 27 | 1 | 0 | Comuniones 1 |  |
| 17. Canales: Mostrador, Encargos, B2B y Envío | 2723 | A | 6 | 37 | 0 | 0 | RD 1021/2022 4, Reglamento (UE) nº 1169/2011 1, RD 1055/2022 1, Roscón 1, Reyes 1, Torrijas 1, Huesos de santo 1 | °C 1 |
| 18. El Plan Financiero y el Dinero Hasta el Punto de Eq… | 2962 | A | 105 | 32 | 8 | 0 | Navidad 1, convenio 1, Seguridad Social 1, autónomos 1, Impuesto de Sociedades 1 |  |
| 19. Financiación, IVA, Envases y Tesorería del Arranque | 3237 | A | 66 | 18 | 17 | 0 | Ley 37/1992 9, Verifactu 4, RD 1055/2022 4, RD 308/2019 3, Ley 1/2025 2, BOE 2, autónomos 1 | m² 1 |
| 20. Cronograma, Apertura y los Primeros Noventa Días | 2524 | A- | 0 | 0 | 0 | 0 | ayuntamiento 1, Reyes 1, Ley 1/2004 1, Seguridad Social 1 |  |
| Anexo normativo, actualizado a 10 de septiembre de 2026 | 2507 | A | 1 | 0 | 3 | 0 | RD 1021/2022 9, Comunidad de Madrid 4, convenio 4, RD 1055/2022 3, Ley 1/2025 3, RD 1007/2023 3, RD 193/2023 3 |  |
| Sobre el autor y condiciones de uso | 335 | T | 0 | 0 | 0 | 0 | ayuntamiento 3, Comunidad de Madrid 1 |  |

### 1.2 Bonus (`BONUS-12-decisiones-de-apertura.md`)

| Sección | Pal. | Cl. | € | % | IVA | PS/PA | Items específicos de España | Unidades |
|---|---|---|---|---|---|---|---|---|
| 0 (portada) | 138 | T | 0 | 0 | 0 | 0 |  |  |
| Índice | 341 | A | 0 | 0 | 0 | 0 | Roscón 1, Seguridad Social 1 |  |
| 1. Local con Obrador o Obrador Aparte | 1538 | A | 17 | 2 | 1 | 0 | RD 1021/2022 4, RGSEAA 1, convenio 1 |  |
| 2. Comprar el Abatidor o Esperar | 1215 | T | 1 | 13 | 1 | 0 | RD 1021/2022 1 | g/kg 1, °C 1, L/ml 1 |
| 3. Abrir con Veinte Referencias o con Cuarenta | 1152 | A- | 9 | 2 | 0 | 0 | Barcelona 1, Reglamento (UE) 1169/2011 1, RD 126/2015 1 |  |
| 4. Producto de Terceros al Arrancar: Cuándo Sí y Qué te… | 1281 | A- | 7 | 1 | 0 | 0 | RD 1021/2022 2 |  |
| 5. Cuánto Roscón Produzco el Primer Año | 1621 | A | 5 | 3 | 1 | 0 | Reyes 4, Navidad 3, Roscón 1, San Valentín 1, Día del Padre 1, Semana Santa 1, Comuniones 1 |  |
| 6. Aceptar el Primer Encargo de Comunión sin Histórico | 1291 | A | 23 | 1 | 0 | 0 | Reglamento (UE) 1169/2011 1, RD 126/2015 1, RD 1021/2022 1, Reyes 1, San Valentín 1, Día del Padre 1, Semana Santa 1 | °C 2 |
| 7. El Primer Contrato con Otra Tienda: a Qué Precio y e… | 1286 | A- | 12 | 20 | 0 | 0 | RD 1021/2022 2 |  |
| 8. Contratar Pastelero o Tirar de Ayudante | 1255 | A | 26 | 0 | 0 | 0 | convenio 6, BOCM 3, Seguridad Social 1, RD 126/2026 1, Comunidad de Madrid 1 |  |
| 9. Abrir en Septiembre o en Febrero | 1444 | A- | 0 | 2 | 0 | 0 | ayuntamiento 2, Seguridad Social 1 |  |
| 10. Empezar en Casa Dentro de la Legalidad: Qué Puedo V… | 1145 | A | 0 | 0 | 0 | 0 | RD 1021/2022 2, BOE 1 |  |
| 11. Envío a Domicilio: Qué Producto Viaja y Cuál No | 1410 | A | 0 | 0 | 0 | 0 | RD 1021/2022 4, Reglamento (UE) 1169/2011 1, RD 1055/2022 1, BOE 1 | °C 1 |
| 12. Qué Hago con lo que no se Vende Hoy | 1292 | A | 1 | 5 | 0 | 0 | RD 1021/2022 4, Ley 1/2025 4, convenio 2, Ley 7/1996 2, RD-ley 24/2021 2 | m² 1 |
| Sobre el autor y condiciones de uso | 335 | T | 0 | 0 | 0 | 0 | ayuntamiento 3, Comunidad de Madrid 1 |  |

### 1.3 Business plan (`business-plan-modelo-pasteleria.md`)

| Sección | Pal. | Cl. | € | % | IVA | PS/PA | Items específicos de España | Unidades |
|---|---|---|---|---|---|---|---|---|
| 0 (portada) | 135 | T | 0 | 0 | 0 | 0 |  |  |
| Índice | 163 | T | 0 | 0 | 0 | 0 |  |  |
| 1. Resumen Ejecutivo | 903 | A- | 22 | 5 | 6 | 0 |  | m² 2 |
| 2. Mercado y Plaza | 1054 | A | 17 | 22 | 2 | 0 | Reyes 1, San Valentín 1, Día del Padre 1, Semana Santa 1, Comuniones 1, Todos los Santos 1 | g/kg 3 |
| 3. Concepto y Carta | 1200 | A- | 21 | 25 | 2 | 0 | Barcelona 1 |  |
| 4. Plan de Operaciones | 1250 | A | 21 | 9 | 0 | 0 | Comunidad de Madrid 3, BOCM 3, Seguridad Social 1, convenio 1 |  |
| 5. Plan Financiero a Tres Años | 1966 | A | 140 | 26 | 11 | 0 | Seguridad Social 2, autónomos 1, modelo 303 1 |  |
| 6. Riesgos y Escenarios | 1053 | A- | 27 | 6 | 1 | 0 | ayuntamiento 1, Impuesto de Sociedades 1 |  |
| Sobre el autor y condiciones de uso | 335 | T | 0 | 0 | 0 | 0 | ayuntamiento 3, Comunidad de Madrid 1 |  |

(Falso positivo posible: «Salva»/«Cataluña» en nombres de marca/lugar.) Citas de investigación española con fecha: guía 10 (`«…» (2025-11-21)`), plan 4; ids `PS-*`/`PA-*` en cap. 1 (10), 2 (8), 4 (17), 5 (2), 6 (2) y en `datos_ejemplo.py` (230 líneas con id).

## 2. Carta: las 30 referencias (`datos_ejemplo.py::CARTA`, línea 479)

5 familias (6+6+6+4+8). Suma de mix = 100 %. Específicas de España: **12 sí** (B5, B6, T6, PA1, TP1-TP8), **3 parcial** (B3, B4, T5), **15 no**. Tres son **copias de `kit-escandallos/05-pasteleria.xlsx`** (precio de compra y receta exactos, `F_KIT_TC/CR/MA`): **B1 Croissant de mantequilla** (hoja Croissants), **PI3 Macarons de frambuesa** (hoja Macarons) y **T1 Tarta de chocolate 70 %** (hoja Tarta Chocolate). Las 19 primeras líneas de `PRECIOS_COMPRA` (de 49) son precios del kit (€/kg, €/docena; unidades kg, docena, ud, l). Equivalente EN: familia `food-cost-templates` (kit de 13 xlsx; comprobar si lleva hoja de pastelería y si sus recetas ya están en lb/oz antes de decidir si B1/PI3/T1 se copian o se recalibran). Vía de huevo (art. 9 RD 1021/2022): 70/2 ×14, estable a ambiente ×9, sin huevo ×6, ovoproducto ×1. Pan (PA1-PA4) a IVA 4 %; el resto a 10 %.

| Id | Familia | Nombre ES | ¿Específica de España? | Copia kit-escandallos | PVP con IVA (€) | IVA | Mix % | Vía huevo | Pico |
|---|---|---|---|---|---|---|---|---|---|
| B1 | Bollería | Croissant de mantequilla | no | SÍ (hoja Croissants) | 1.60 | 10 % | 12.0 | estable a ambiente |  |
| B2 | Bollería | Pain au chocolat | no |  | 1.85 | 10 % | 8.0 | estable a ambiente |  |
| B3 | Bollería | Napolitana de crema | parcial (napolitana de crema: bollo típico español) |  | 1.85 | 10 % | 7.0 | 70/2 |  |
| B4 | Bollería | Palmera de hojaldre | parcial (palmera = palmier) |  | 1.70 | 10 % | 4.5 | sin huevo |  |
| B5 | Bollería | Caracola de pasas | sí (caracola de pasas) |  | 1.85 | 10 % | 3.5 | 70/2 |  |
| B6 | Bollería | Ensaimada | sí (ensaimada mallorquina) |  | 1.95 | 10 % | 3.0 | estable a ambiente |  |
| PI1 | Pastelería individual | Milhojas | no |  | 3.60 | 10 % | 4.0 | 70/2 |  |
| PI2 | Pastelería individual | Éclair | no |  | 3.20 | 10 % | 3.5 | 70/2 |  |
| PI3 | Pastelería individual | Macarons de frambuesa | no | SÍ (hoja Macarons) | 2.10 | 10 % | 7.0 | 70/2 |  |
| PI4 | Pastelería individual | Tartaleta de frutas | no |  | 3.80 | 10 % | 3.0 | 70/2 |  |
| PI5 | Pastelería individual | Lionesa o profiterol | no (profiterol estándar) |  | 2.30 | 10 % | 3.0 | 70/2 |  |
| PI6 | Pastelería individual | Entremet individual | no |  | 4.50 | 10 % | 1.5 | ovoproducto |  |
| T1 | Tartas y entremets | Tarta de chocolate 70 % | no | SÍ (hoja Tarta Chocolate) | 3.60 | 10 % | 1.2 | 70/2 |  |
| T2 | Tartas y entremets | Tarta de queso | no |  | 3.40 | 10 % | 1.5 | 70/2 |  |
| T3 | Tartas y entremets | Tarta de manzana | no |  | 3.20 | 10 % | 1.1 | estable a ambiente |  |
| T4 | Tartas y entremets | Tarta de zanahoria | no |  | 3.30 | 10 % | 0.9 | 70/2 |  |
| T5 | Tartas y entremets | Tarta Sacher | parcial (Sacher: clásico centroeuropeo) |  | 3.80 | 10 % | 0.8 | estable a ambiente |  |
| T6 | Tartas y entremets | Tarta de nata y fresas | sí (tarta de nata y fresas = tarta de Comunión) |  | 3.50 | 10 % | 1.0 | 70/2 | Comuniones |
| PA1 | Panes de acompañamiento | Barra | sí (barra: pan común español; IVA 4 %) |  | 1.20 | 4 % | 16.0 | sin huevo |  |
| PA2 | Panes de acompañamiento | Chapata | no (ciabatta) |  | 1.60 | 4 % | 4.0 | sin huevo |  |
| PA3 | Panes de acompañamiento | Hogaza de masa madre | no (masa madre) |  | 3.90 | 4 % | 3.5 | sin huevo |  |
| PA4 | Panes de acompañamiento | Pan de molde | no (pan de molde) |  | 3.20 | 4 % | 2.5 | sin huevo |  |
| TP1 | Temporada | Roscón de Reyes | sí |  | 16.50 | 10 % | 1.2 | 70/2 | Reyes |
| TP2 | Temporada | Torrijas | sí |  | 2.40 | 10 % | 1.3 | 70/2 | Semana Santa |
| TP3 | Temporada | Buñuelos de viento | sí |  | 1.60 | 10 % | 1.0 | 70/2 | Todos los Santos |
| TP4 | Temporada | Huesos de santo | sí |  | 1.90 | 10 % | 0.8 | estable a ambiente | Todos los Santos |
| TP5 | Temporada | Panellets | sí (catalán) |  | 1.85 | 10 % | 0.7 | estable a ambiente | Todos los Santos |
| TP6 | Temporada | Polvorón o mantecado | sí |  | 1.20 | 10 % | 1.3 | sin huevo | Reyes |
| TP7 | Temporada | Turrón de almendra | sí |  | 10.50 | 10 % | 0.5 | estable a ambiente | Reyes |
| TP8 | Temporada | Mona de Pascua | sí (Mona de Pascua levantina/catalana) |  | 13.50 | 10 % | 0.7 | estable a ambiente | Semana Santa |

## 3. Picos / campañas (`PICOS`, línea 1783; cap. 15; `estacionalidad-y-picos.xlsx`)

Fuente única: `PICOS` (6) + `ESTACIONALIDAD_MENSUAL` (12 coeficientes) + `DIAS_APERTURA_MES`. Todo «supuesto» salvo `PS-41` (factor Reyes).

| # | Campaña | Fechas | Mes | Días | Producto estrella | Uds/día normal → pico | Factor obrador (×) | Refuerzo (personas / h-persona) | Antelación compra (sem.) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Reyes | 2-6 enero | 1 | 5 | Roscón de Reyes | 0 → 160 | **6,0** (PS-41 + supuesto) | 3 / 40 | 6 |
| 2 | San Valentín | 13-14 febrero | 2 | 2 | Macarons de frambuesa | 95 → 260 | 1,8 | 0 / 0 | 3 |
| 3 | Día del Padre y de la Madre | 19 marzo y 1.er domingo de mayo | 3 | 4 | Tarta de chocolate 70 % | 16 → 96 | 1,9 | 1 / 16 | 3 |
| 4 | Semana Santa | Domingo de Ramos a Resurrección | 4 | 8 | Torrijas | 0 → 230 | 2,4 | 1 / 40 | 4 |
| 5 | Comuniones | mediados abril a mediados junio | 5 | 20 | Tarta de nata y fresas | 10 → 34 | 1,6 | 1 / 60 | 5 |
| 6 | Todos los Santos | 30-31 oct. y 1 nov. | 11 | 3 | Buñuelos de viento | 0 → 470 | 2,6 | 2 / 24 | 4 |

- Estacionalidad mensual: 1,34 · 0,93 · 0,97 · 1,04 · 1,07 · 0,97 · 0,85 · 0,65 · 0,91 · 0,95 · 1,08 · 1,24 (agosto 0,65 = cierre 2 semanas; días de apertura 26/mes, 14 en agosto = 300/año). Apertura recomendada septiembre (mes 9, «llegar rodado a Reyes»). Rampa de arranque 0,55 → 1,00 en 6 meses.
- **Cifras derivadas citadas en el texto (cap. 15, xlsx)**: 6 campañas = 22.479 € sin IVA (7,0 % del año); incremental 21.270 €; Reyes 12.000 € (3,7 %), San Valentín 993/630 €, Padre-Madre 1.257/1.047 €, Semana Santa 4.015 €, Comuniones 2.164/1.527 €, Todos los Santos 2.051 €; demanda Reyes 2.856 piezas/día vs capacidad 1.200 (déficit 1.656; 47,4 h; 4 personas de refuerzo); refuerzo anual 3.795,51 €; unidades Reyes 800 = 47 % de los roscones del año. Más una cita externa «Matías…» (ensaimadas 25-30 → 150-200 al día, turrón 7.000-8.000 barras).
- Dónde aparece: guía cap. 2, 3 (carta temporada), 12, 15 (núcleo), 16 (Comuniones), 20 («llegar rodado a Reyes»); bonus dec. 5 (cuánto roscón el primer año), dec. 6 (encargo de Comunión), dec. 9 (septiembre vs febrero); plan §2 (calendario); xlsx estacionalidad (6 hojas), capacidad-obrador (Reyes 8 menciones), plantilla-turnos (hoja Plan de Contratación «Refuerzo de las seis campañas»), plan-financiero (estacionalidad mensual).
- Adaptación US (propuesta, a decidir): fechas distintas (Mother's Day = 2.º domingo de mayo, Father's Day = 3.er domingo de junio, no marzo/mayo), Easter, Valentine's, Thanksgiving/Christmas (no hay Reyes ni Todos los Santos), graduaciones/bodas en lugar de Comuniones. Cambiar fechas mueve el «mes» y las celdas de capacidad; cambiar nombres sin tocar números mantiene las cifras.

## 4. Laboral (`CONVENIO`, `PLANTILLA`, `PARAMS`)

**Convenio**: Convenio de Comercio e Industria de Confitería, Pastelería, Bollería, Repostería, Heladería y Platos Cocinados de la **Comunidad de Madrid** (código 28001025011981; BOCM núm. 50, 28-feb-2026; vigencia 1-ene a 31-dic-2026; fuente PA-33). **15 pagas**. Hojas «en celda verde» que el lector sustituye.

| Grupo | Descripción | Bruto €/mes | €/año (×15) | Áreas |
|---|---|---|---|---|
| 1 | Técnicos y titulados superiores | 1.733,88 | 26.008,20 | Administración |
| 2 | Dirección, jefes y encargados | 1.427,89 | 21.418,35 | Obrador · Comercio · Admin. |
| 3 | Personal especialista | 1.376,91 | 20.653,65 | Obrador · Comercio |
| 4 | Personal cualificado | 1.249,42 | 18.741,30 | Obrador · Comercio |
| 5 | Personal de apoyo | 1.192,42 | 17.886,30 | Obrador · Comercio |
| 6 | Servicios auxiliares | 1.192,42 | 17.886,30 | Obrador · Comercio |

**Plantilla** (5 personas = 3,5 jornadas, 140 h/sem.; perfiles literales del Kit de Tareas): P1 Jefe Pastelero 1,0 · grupo 2 · 40 h · madrugada 04:30-12:30 · P2 Pastelero 1,0 · g3 · 40 h · 05:00-13:00 · P3 Ayudante 0,5 · g5 · 20 h · 07:00-11:00 · P4 Dependiente Vitrina A 0,5 · g4 · 20 h · 08:00-12:00 · P5 Dependiente Vitrina B 0,5 · g4 · 20 h · tarde 16:30-20:30. Altas del año 1 en `Plan de Contratación` (P1 2-ago, P2 16-ago, P3/P4 1-sep, P5 1-dic de 2027).

**Parámetros**: `pagas_convenio` 15 (PA-33) · `ss_empresa` **0,33** (motor.PARAMETROS) · `smi_mensual` 1.221 (RD 126/2026, 14 pagas) · `smi_anual` 17.094 · `horas_semana_jornada_completa` 40 · `horas_anuales_contrato` 1.780 (40×52 − 30 días vacaciones − festivos) · `ratio_horas_productivas` 0,85. Veredicto «Manda el convenio: el grupo más bajo supera el SMI» (17.886,30 > 17.094). Texto: bruto de tabla «sin antigüedad, plus de nocturnidad ni horas extra». Cap. 14: registro de jornada (Estatuto de los Trabajadores, RDLeg 2/2015, RD-ley 8/2019), PRL; cap. 20: libertad horaria (Ley 1/2004).

**Cómo calcula el xlsx** (`plantilla-turnos-y-coste-personal.xlsx`, hoja `Horas y Coste`, filas 7-11): `E`=INDEX(Parámetros!C8:C13, MATCH(grupo, Parámetros!B8:B13,0)) (bruto mensual del grupo, **clave = texto de la descripción**) · `F`=horas/sem ÷ `Parámetros!C22` (jornada eq.) · `H`=E×F · `I`=H×`C15` (15 pagas) · `K`=I×(1+`C21`) (SS 33 %) · `J`=K/12 · `L` coste/hora. Salidas: `E15` coste personal/mes **7.731,34 €**, `E16` año de crucero **92.776,08 €**, `E17` 3,5 jornadas, `E18` coste/hora pagada, `E19` SS/año, `E20` suma brutos; `Parámetros!C16`=MIN(brutos)×pagas, `C18` veredicto vs SMI. Año 1 (`Plan de Contratación`): meses = MIN(12, MAX(0, 12 − (mes_alta − mes_apertura))).
**Los mismos números se re-calculan en otros dos libros**: `carta-de-apertura…` (hoja Parámetros B11-B16 pagas 15, SS 0,33, 1.780 h, 0,85 → coste hora productiva de obrador B16; usada por `Coste Hora y Mano de Obra` G6… con 394 fórmulas) y `plan-financiero…` (hoja `Personal`: tabla de convenio A15:E20 con claves «Grupo 2…», `H`=F+SS, `I`=H×MAX(12, pagas)). Texto: cap. 13 (23 menciones de convenio), cap. 12, dec. 8, plan §4-§5. Adaptación US: no existe convenio; sueldo/hora, overtime FLSA, tips, payroll taxes + workers' comp + seguro médico; el «bruto mensual × 15 pagas» se convierte en rate × horas × 52.

## 5. Impuestos (IVA)

**En `datos_ejemplo.py` (75 líneas con «IVA»)**: `PARAMS['iva_producto']` 0,10 (PA-36: bollería/pastelería art. 91.Uno.1.1.º Ley 37/1992) · `iva_pan` 0,04 (PA-36b: RD 308/2019, DGT 24-02-2025, STS 1610/2024) · `iva_degustacion` 0,10 (PA-36c, art. 91.Uno.2.2.º) · `iva_equipamiento`/`iva_obra`/`iva_general` 0,21 (art. 90.Uno). `CARTA[*]['iva']` 0,10 (26) o 0,04 (PA1-PA4) con `pvp_con_iva` tecleado. `EQUIPAMIENTO[*]`: `base_iva` (con IVA ×2 UNOX/SMEG; «no declarada» ×1 Sammic BE-20; sin IVA el resto) + `tipo_iva` 0,21 ×22. `CAPEX[*]`: tipo 0,21 en obra, equipamiento, tienda, proyecto técnico, asesoría, packaging, marketing; **0,0** en tasas municipales, comunicación sanitaria, fianza, fondo de maniobra. Texto de apoyo: «Sin la columna "lleva IVA" el CAPEX sale un 21 % desviado» (D17).

**En los xlsx** (hojas / celdas): `calculadora-capex` — Parámetros A13-A15 (IVA general / de la pastelería / de tasas), A23-A24 (periodicidad de la declaración, meses hasta recuperar), CAPEX por Bloque F-M (`¿El precio lleva IVA?`, `Tipo`, `Base sin IVA`, `IVA soportado`, `Total con IVA`; 10 textos IVA), hoja entera **IVA y Tesorería**, Resumen A8-A10 · `carta-de-apertura` — Parámetros A18-A21 (10 %, 4 %, 10 %), `Coste Hora…` L-N (PVP con IVA, IVA, sin IVA), `Mix y Ticket Medio` E-G, B39-B43 (PVP medio ponderado con IVA, ticket con/sin IVA, «IVA medio de la carta») · `checklist-equipamiento` — Equipamiento A7 (IVA general), J-L (¿lleva IVA?, tipo, precio SIN IVA; 41 textos «IVA»), Variante A8-A9 · `estacionalidad` — Parámetros A23-A26, Calendario G-I (IVA, PVP con/sin), N-O (facturación sin IVA) · `plan-financiero` — 0. Supuestos A8-A18 (PVP con IVA, ticket con/sin, IVA y tipos, **IVA medio de las compras de materia prima**), Inversión Inicial D-E, PyG A34-A35 (**IVA soportado de costes variables/fijos**, memoria), Tesorería 12 meses A10-A21 (**IVA repercutido / soportado / compensar / Pago del IVA (modelo 303)**), Financiación H11 (inversión + IVA adelantado). **0 IVA** en capacidad-obrador y plantilla-turnos.

**Cifras derivadas «con IVA / sin IVA» citadas en el texto** (a recalcular o reconcebir): cap. 2 ventas anuales sin IVA 322.198 €, ticket sin IVA 5,87 € · cap. 3 ticket con IVA 6,38 €, ticket sin IVA 5,87 €, PVP medio ponderado con IVA 2,46 € (junto a un margen de contribución medio de 1,07 €/pieza, que no es IVA pero depende del PVP sin IVA) · cap. 4 CAPEX sin IVA 227.916 €, IVA soportado 33.911 €, desembolso con IVA 261.826 € · cap. 8 (45 menciones) precios de equipo «284,10 € sin IVA», «120,40 € sin IVA», abatidor «10.037 € más IVA» (ficha de distribuidor), vitrina Docriluc, atemperadora Selmi, 1.215,00 € sin IVA / 1.470,15 € con IVA (laminadora) · cap. 15 facturación sin IVA 22.479 € / 21.270 € incremental · cap. 16 facturación de campaña sin IVA · cap. 18 memoria de IVA soportado (no afecta al resultado) · cap. 19 IVA soportado 33.911 €, devolución, Ley 37/1992 (9 citas), RD 308/2019, DGT, trimestral/modelo 303, Verifactu ×4 (≈ 17 menciones) · Anexo normativo · bonus dec. 2 («10.037 € más IVA»), dec. 5 (incremental 12.000 €), dec. 1 · plan §1 («IVA que se adelanta», 33.911 €), §2-3 (ticket 5,87 €, PVP 2,46 €), §5 (IVA ×11, modelo 303), §6. Verifactu (TPV, PA-37) aparece también en equipamiento (fila 19) y checklist F6.

## 6. xlsx por libro (`build/*.xlsx`, mapas `build/mapa-*.json`)

Todos con hojas «Instrucciones» (sin fórmulas) y la marca/pie «AI Chef Pro · aichef.pro — Cómo Montar una Pastelería», «Diseñado por John Guerrero…», «Versión 1.0 · septiembre 2026». Formatos: `#,##0.00 €`, `0.0%`, fechas `dd/mm/yyyy` (checklist-legal ×71, plantilla-turnos ×5). Unidades: kg/g (carta 387 textos), m² (capex 20, capacidad 13), kW (capacidad 11), °C (carta 23), L/ml (pocas). Dentro del texto hay constantes «€» (1.215,00 € / 1.470,15 €, umbrales, 300 € de pedido mínimo…) que NO son formato de celda.

| Libro | Hojas en orden (textos·fórmulas) | Textos | Fórm. | Celdas fmt € | Textos con € | Textos «IVA» | Contenido específico de España |
|---|---|---|---|---|---|---|---|
| `calculadora-capex-pasteleria` | Instrucciones (39·0) → Parámetros (95·3) → CAPEX por Bloque (256·172) → Variante del Formato (59·48) → Traspaso vs Obra Nueva (94·46) → IVA y Tesorería (32·38) → Resumen (56·16) | 631 | 323 | 378 | 26 | 48 | Columnas ¿lleva IVA?/tipo/base/IVA soportado en cada partida; hoja «IVA y Tesorería» (periodicidad modelo 303, meses hasta recuperar); traspasos reales de Barcelona (PS-69, 11 menciones) y Milanuncios/negociosenventa; precios de fichas de distribuidores españoles (UNOX/SMEG/Irinox… con y sin IVA); tasas municipales, comunicación sanitaria, fianza 2 meses; m² (20 textos); RD 1021/2022, Ley 37/1992, Verifactu. |
| `capacidad-obrador-y-local` | Instrucciones (38·0) → Parámetros (86·2) → Zonas y m2 (53·26) → Capacidad por Equipo (88·53) → Cuello de Botella (56·37) → Ficha de Visita a Local (131·34) | 452 | 152 | 0 | 1 | 0 | 7 zonas obligatorias (PS-86d; obrador 45, venta 22, almacén 5, cámara 4, producto terminado 3, vestuarios 8, residuos 3 = 90 m²), kW de hornos (34) y potencia instalada 62; ficha de visita al local (prueba de humos, comunidad de propietarios, ayuntamiento ×3); Reyes ×8 (capacidad en pico); m² ×13, kW ×11. |
| `carta-de-apertura-y-escandallo` | Instrucciones (24·0) → Parámetros (257·11) → Escandallo por Tanda (1145·802) → Coste Hora y Mano de Obra (118·394) → Decisión de Huevo y Temperatura (295·218) → Mix y Ticket Medio (130·255) → Decisión de Surtido (119·249) | 2088 | 1929 | 1130 | 28 | 19 | 30 referencias con nombres españoles (12 sí / 3 parcial); hoja «Decisión de Huevo y Temperatura» (art. 9 RD 1021/2022: techos 4 °C/8 °C/24 h; 295 textos, 218 fórmulas); IVA 10 %/4 % por familia, PVP con IVA tecleado; coste hora de obrador con convenio/SS/15 pagas; umbral «sin gluten» 20 mg/kg; 387 textos con g/kg, 23 con °C; recetas en kg/g/docena. |
| `checklist-equipamiento-y-proveedores` | Instrucciones (24·0) → Equipamiento (315·194) → Variante del Formato (264·86) → Proveedores (115·4) → Contador (72·68) | 790 | 352 | 189 | 46 | 57 | 22 partidas con marca y modelo (UNOX XB693, SMEG ALFA420E1HDS, Docriluc, Irinox, Sammic DF-40 y BE-20, Selmi One, Salva) y precio de ficha de distribuidor español (con/sin IVA, 41 textos «IVA»); 9 proveedores con URL (Sosa, Puratos, Barry Callebaut, Valrhona, Debic, Elle & Vire, Ylla 1878, Coromina, Cospan; pedido mín. 300 €, 7 días); plazos de entrega en semanas; Verifactu (TPV). |
| `checklist-legal-y-licencias` | Instrucciones (39·0) → Checklist Legal (F1-F6) (285·39) → Árbol de Registro Sanitario (47·4) → Suministro a Otros Minoristas (64·16) → Ruta Doméstica (72·5) → Registro de Formación (38·13) → Cronograma y Ruta Crítica (170·222) | 715 | 299 | 24 | 9 | 1 | 30 trámites F1-F6 (5 por fase; columnas Fase, Trámite, Responsable, Plazo, Coste previsto/real, Fecha objetivo/hecha, «¿Cambia por CCAA?», Notas con PS-/PA-); árbol de registro sanitario (RGSEAA ×13, 4 CCAA de ejemplo: Madrid, Cataluña, Andalucía, Comunitat Valenciana); suministro a otros minoristas (art. 3); ruta doméstica (art. 13.8/13.9; Decreto 13/2025 Valencia; 60 kg/semana, 12 m²); registro de formación (6 h, caduca); cronograma con ruta crítica (222 fórmulas; fechas dd/mm/yyyy ×71). Casi 100 % ley española: Estatuto, modelo 036, IAE, Seguridad Social, licencia de actividad/declaración responsable, boletín eléctrico, gas. |
| `estacionalidad-y-picos` | Instrucciones (22·0) → Parámetros (82·3) → Calendario de 6 Picos (48·34) → Peso sobre el Año (66·80) → Capacidad vs Demanda del Pico (32·89) → Refuerzo y Tesorería (40·86) | 290 | 292 | 122 | 23 | 13 | Las 6 campañas españolas (Reyes ×18, San Valentín ×7, Semana Santa ×7, Todos los Santos ×7, Comuniones ×5), PVP con IVA/sin IVA, convenio ×9 y SS ×5 en «Refuerzo y Tesorería», IVA 10 %/4 %. |
| `plan-financiero-3-anos-pasteleria` | Instrucciones (43·0) → 0. Supuestos (114·6) → Inversión Inicial (63·23) → PyG 3 Años (92·149) → Punto de Equilibrio (40·83) → Escenarios (37·43) → Personal (73·44) → Tesorería 12 meses (59·172) → Financiación (53·473) → Canales y Punto Muerto (46·29) | 620 | 1022 | 854 | 52 | 56 | IVA repercutido/soportado/modelo 303 (Tesorería), IVA medio de compras, convenio ×13, SMI ×5, SS ×6, «autónomo» (cuota del propietario), Impuesto de Sociedades, Ley 37/1992 ×3; préstamo 60.000 € al 6,2 % a 84 meses con 6 de carencia; canales (Pomar PS-53: 95/5); gastos fijos con alquiler 1.200 €, suministros 1.450 €. |
| `plantilla-turnos-y-coste-personal` | Instrucciones (23·0) → Parámetros (58·2) → Turnos Semanales (87·45) → Horas y Coste (60·74) → Plan de Contratación (100·67) | 328 | 188 | 95 | 33 | 0 | Convenio de Madrid (6 grupos, 15 pagas, BOCM), SMI RD 126/2026, SS 33 %, turnos de madrugada, fechas de alta (dd/mm), refuerzo de campañas; convenio ×33, SS ×16, SMI ×9. |

Totales: 5914 celdas de texto, 4557 fórmulas, 2792 celdas con formato € en 8 libros / 53 hojas.

**Atención especial**: (1) `checklist-legal-y-licencias.xlsx`: 285 textos solo en la hoja principal; **30 filas de trámite** (F1-F6 ×5), cada una con Responsable (Promotor/Gestoría/Ingeniería/Constructora/Instalador habilitado), plazo, coste «A presupuestar», «¿Cambia por CCAA?» y nota con id `PS-`/`PA-` y `[Fuente: …]`; 6 filas de AVANCE con COUNTIF/SUMIF; las otras 5 hojas son árboles de decisión con respuestas Sí/No y listas CCAA. Reescritura completa para EE. UU. (no traducción). (2) `checklist-equipamiento-y-proveedores.xlsx`: 22 partidas con marca/modelo/precio de ficha española y 9 proveedores con URL e `Id` PS-87…95; el texto del cap. 8/11 los cita uno a uno.

## 7. Landing / dashboard / library ES (solo lo específico de este producto)

| Pieza | Fichero (ES) | Contenido específico de España / a decidir |
|---|---|---|
| Datos landing | `astro-site/src/data/productos/guias/guia-pasteleria-obrador.ts` (331 l.) → EN: `astro-site/src/data/productos-en/guias/<slug-en>.ts` | Precio «65 EUR» ×6 (ctaLabel hero, buyBox, cta, stickyLabel, pricing, schema `price '65.00'`); `stripeEnvKey VITE_STRIPE_PAYMENT_LINK_GUIA_PASTELERIA_OBRADOR`; SEO title/desc «…en España», keywords ES; 20 capítulos (`grid.chapters`) con títulos y `desc` españoles (RGSEAA, convenio, Reyes, «registro sanitario…»); `hero.checkItems` «el marco legal explicado es el español» y «103 páginas», bonus «37 páginas» (tokens D20, deben recalcularse con PyMuPDF en el PDF EN; gate `paginas-gate.py`); `why.reasons` (4) con «cada dato legal con su artículo y su fecha»; `author.bio` (+200 aperturas, Estrella Michelin y Soles Repsol en España); `bonus.items` (11: 8 herramientas + 3 bonus; el 3.º = Guía de Equivalencias → en EN es el bonus común `equivalents-guide`); `guarantee` (30 días, art. 20 TRLGDCU en comentario); `testimonials.items: []` (nada que traducir); `schema.faqs` (3) y `faqs` (**12**: ¿gratis en Google? (15.000-200.000 €, factor 13), desde casa, kit 12 € vs guía, ya abierta (→ Guía Food Cost), ¿sustituye al proyecto técnico? (1.800-2.800 € + impuestos; tramitación desde 1.690 € + IVA en Madrid, estudio-l.es), mi ayuntamiento es distinto («más de ocho mil municipios»), Pack APPCC, Kit de Escandallos, Excel en Sheets/Numbers, ¿fuera de España?, ¿cambia la normativa?, garantía); `footerLinks` (kit-tareas-pasteleria, kit-escandallos, pack-appcc, guía food cost, `/productos-digitales`); `updateNote «Versión 1.0.1 · septiembre 2026»`; breadcrumb ES. Las FAQ «¿fuera de España?» y «¿mi ayuntamiento?» cambian de sentido en una edición US-nativa; las cifras de proyecto técnico/tramitación son de fuente española (no trasladables). |
| Wrapper landing | `astro-site/src/pages/guia-pasteleria-obrador.astro` (`locales={['es']}`, `whatsapp={false}`, `omitGlobalApp`) → EN: `astro-site/src/pages/en/digital-products/<slug-en>.astro` + `<slug-en>/access.astro` + `<slug-en>/library.astro` | Calco del wrapper EN de Food Cost; `alternatesFamilia('guia-pasteleria-obrador')` (hoy NO existe familia en `tienda.ts` para este producto: añadirla con `es` + `en`). |
| Acceso | `astro-site/src/pages/guia-pasteleria-obrador-access.astro` → `src/pages/GuiaPasteleriaAccessGate.tsx` (13 l., `productLabel «Cómo Montar una Pastelería»`) | Usar `ProductAccessGate lang="en"`. |
| Biblioteca (island) | `astro-site/src/pages/guia-pasteleria-obrador-library.astro` + `astro-site/src/islands/library/GuiaPasteleriaLibraryIsland.tsx` (storageKey `guia-pasteleria-obrador-jwt`) | Island propio EN con nuevo `storageKey`. |
| Dashboard | `src/pages/GuiaPasteleriaDashboard.tsx` (140 l.) | 4 `SECTIONS`: Guía Principal (guia-pdf, guia-docx), Herramientas Excel (8: capacidad-obrador, capex-pasteleria, estacionalidad-picos, carta-escandallo, plan-financiero, checklist-legal, checklist-equipamiento, turnos-personal), Bonus (business-plan-docx, bonus-decisiones-pdf, bonus-decisiones-docx), Bonus Internacional (guia-equivalencias). Textos ES con «España»/«normativa»; cross-sell a `/kit-tareas-pasteleria — 12 EUR` y `/pack-appcc — 14 EUR` (sin gemelo EN el primero); título Helmet «Cómo Montar una Pastelería — Dashboard». Copiar como `…EnDashboard.tsx` con `equivalents-guide`. El plan de negocio solo existe en DOCX (sin PDF). |
| Descargas | `netlify/functions/get-download-urls.ts:435-449` (14 claves) y espejo en `src/data/productos-digitales-config.ts:1383-1407` | EN: 13 ficheros propios en `/dl/<slug-en>/…` + `equivalents-guide` → `dl/en-shared/…`. Precios: `netlify/shared/product-prices.ts:19 {eur:65}`; Payment Link ES `netlify/shared/payment-links.ts:18`. |
| Registro (5 fuentes + extras) | `astro-site/src/lib/zona-app.ts:101`, `netlify/functions/verify-purchase.ts:242`, `resend-access.ts:225`, `admin-generate-access.ts:47`, `src/data/products-catalog.ts:383`, `src/data/productos-changelog.ts:112`, `src/App.tsx:167-168,915-920`, `src/data/productos-digitales-config.ts:1383` | Mecánica ya documentada en el census Food Cost; aquí solo cambian slug, ficheros y `lang:'en'`. |
| Menciones cruzadas ES (para el interenlazado EN) | `kit-escandallos.ts`, `pack-appcc.ts`, `kit-tareas-pasteleria.ts`, `guia-food-cost-ingenieria-menu.ts`, `guia-chocolateria-obrador.ts` (+`.astro`), `DigitalProductsHubPage{,Fr,De,It,Nl,Pt}.astro`, `ProductosDigitalesHubPage.astro`, `lib/linkify-use-case.ts`, `lib/sinonimos-buscador.json`, `llms.txt`/`llms-full.txt` | Hub EN: tarjeta viva; `llms*.txt` y recuento «currently N products». |
| Imágenes | `/lovable-uploads/ai-gallery/guia-pasteleria-{hero,1..5}.jpg`, `es-guia-equivalencias.jpg`, `og-guia-pasteleria-obrador.jpg` | Sin texto español comprobado (verificar antes de reutilizar). |

## 8. Propuesta de tandas (≈ 4.500-5.500 palabras, cortes solo en `## `)

Corte por DP: mínimo número de tandas con tope 5.600 y penalización fuera de 4.500-5.500. La sección 0 (portada) va siempre con la primera tanda de su documento. Modelo: `opus` si hay alguna sección A (todas las tandas la tienen; la única sección T de peso, cap. 7 en T04, no justifica una tanda sonnet propia de 1.915 palabras salvo que se separe).

### 8.1 Guía (57623 palabras, 24 secciones `## `)

| Tanda | Secciones incluidas | Palabras | Secc. A | Modelo |
|---|---|---|---|---|
| T01 | portada, Índice, cap. 1 | 4090 | 2 | opus |
| T02 | cap. 2, cap. 3 | 5358 | 2 | opus |
| T03 | cap. 4, cap. 5 | 4764 | 2 | opus |
| T04 | cap. 6, cap. 7 | 5375 | 1 | opus |
| T05 | cap. 8, cap. 9 | 5599 | 2 | opus |
| T06 | cap. 10, cap. 11 | 4946 | 2 | opus |
| T07 | cap. 12 | 3515 | 1 | opus |
| T08 | cap. 13 | 2322 | 1 | opus |
| T09 | cap. 14, cap. 15 | 4967 | 2 | opus |
| T10 | cap. 16, cap. 17 | 5122 | 2 | opus |
| T11 | cap. 18 | 2962 | 1 | opus |
| T12 | cap. 19 | 3237 | 1 | opus |
| T13 | cap. 20, Anexo normativo, Sobre el autor | 5366 | 2 | opus |

### 8.2 Bonus (16744 palabras, 15 secciones `## `)

| Tanda | Secciones incluidas | Palabras | Secc. A | Modelo |
|---|---|---|---|---|
| B01 | portada, Índice, dec. 1, dec. 2, dec. 3 | 4384 | 3 | opus |
| B02 | dec. 4, dec. 5, dec. 6, dec. 7 | 5479 | 4 | opus |
| B03 | dec. 8, dec. 9, dec. 10, dec. 11 | 5254 | 4 | opus |
| B04 | dec. 12, Sobre el autor | 1627 | 1 | opus |

### 8.3 Business plan (8059 palabras, 9 secciones `## `)

| Tanda | Secciones incluidas | Palabras | Secc. A | Modelo |
|---|---|---|---|---|
| P01 | portada, Índice, § 1, § 2, § 3, § 4 | 4705 | 4 | opus |
| P02 | § 5, § 6, Sobre el autor | 3354 | 2 | opus |


## 9. Totales

| Concepto | Valor |
|---|---|
| Palabras totales a traducir/readaptar (3 documentos) | **82.426** (57.623 + 16.744 + 8.059) |
| — de ellas en secciones T (portadas, Índice del plan, «Sobre el autor» ×3, cap. 7, dec. 2) | 4.749 (de las que 3 × 335 «Sobre el autor» y las portadas se pueden copiar de la edición Food Cost EN ya traducida) |
| — en secciones A | **77.677** (94 %) |
| Secciones `## ` clase A | **39 de 48** (guía 21/24 · bonus 12/15 · plan 6/9); 12 de ellas «A-» (ligeras) |
| Tandas totales | **19** (guía T01-T13 · bonus B01-B04 · plan P01-P02) |
| Tandas opus / sonnet | **19 opus / 0 sonnet** (regla «opus si hay una A»); con las A- hechas por sonnet+`⟦ADAPT⟧`+revisión, muy pocas tandas (p. ej. T07 = cap. 12, A-) podrían bajar a sonnet (solo si John lo aprueba) |
| Tandas fuera de la banda 4.500-5.500 | T07 3.515 · T08 2.322 · T11 2.962 · T12 3.237 · B04 1.627 · P02 3.354 · (T05 5.599, T04 5.375, T13 5.366 ligeramente arriba): se mantienen los cortes en `## ` y que los capítulos fiscales/laborales A no se mezclen. Alternativas: T07+T08 = 5.837, T11+T12 = 6.199, B03+B04 = 6.881 |
| xlsx | 8 libros · 53 hojas · 5.914 textos · 4.557 fórmulas · 2.792 celdas con formato € (capa `aplicar_en.py` sobre el publicado, como Food Cost) |
| Caché de textos ES | `build/docs/txt/` 51 bloques `.txt` (guía + bonus + plan) — fuente de la v2 ES, no se reutiliza para EN (se traduce el `.md` ensamblado por tandas `## `) |
