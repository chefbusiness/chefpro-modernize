# Lente 3 · Normativa 2026 — «Cómo Montar una Churrería-Chocolatería» (producto 51, F1)

**Fecha:** 2026-10-03 · **Sesión:** Claude Code (subagente de la lente L3) · **Ids nuevos:** `CUN-01…CUN-42`.
**Hermana y frontera:** `guia-chocolateria-obrador` (LIVE 19-sep). Todo lo verificado allí se **cita por id `CHN-*`** sin reabrir
(`guia-chocolateria-verificacion-legal-2026-09-12.json`, 109 fichas). Los `FC-IVA-*` vienen de `guia-food-cost-verificacion-fiscal-2026-09-03.md`.

## 0. Método y limitaciones

- **Fuentes primarias, una cada vez:** HTML consolidado del BOE (`act.php`, `doc.php` con su pestaña «Análisis» para la vigencia) y, si
  el HTML no traía el texto, **PDF consolidado** extraído con PyMuPDF: RDLeg 1175/1990 (IAE), Ley 7/2022, RD 1021/2022. DOUE en la copia
  del BOE (`boe.es/doue/…`) porque **EUR-Lex devolvió página vacía** a curl y a WebFetch. BOCM, BOP de Córdoba y codigotecnico.org en PDF.
  CPU vigilada con `istats` (máx. 59,2 °C; nunca se llegó a 63 °C). Ningún build, navegador ni Playwright.
- **Lo que NO se pudo verificar, y por qué:**
  1. Ordenanzas de humos de **Barcelona, Sevilla y Valencia**: el repositorio municipal de Barcelona respondió con *rate limit*; Sevilla y
     Valencia no se abrieron por presupuesto. **Solo Madrid está verificada** (`CUN-23…CUN-25`).
  2. **Notas explicativas del INE** para la correspondencia IAE → CNAE-2025 de churrería con sala: solo se verificaron los **títulos** de las
     clases en el RD 10/2025. La correspondencia es **inferencia** (`CUN-16`).
  3. **IVA del chocolate a la taza para llevar:** no se localizó consulta vinculante de la DGT (`CUN-18`).
  4. **REGCON:** no se repitió la consulta; la búsqueda de un convenio propio de churrerías se hizo en boletines (`CUN-33`) y no es exhaustiva.
  5. **Tablas salariales de una 2.ª y 3.ª provincia:** solo **Madrid** con fuente primaria. Las cifras de Sevilla que circulan (convenio
     2025-2028, «+5 % en 2026») vienen de blogs: **sin fuente primaria y fuera del informe**.
  6. **Registro horario digital:** prensa y despachos hablan de un RD aprobado en Consejo de Ministros el 30-09-2025 y pendiente de BOE.
     **No hay texto en el BOE**, y el ET 34.9 consolidado a 04-12-2025 sigue igual (`CHN-68`). Riesgo de caducidad, no dato.
  7. **Calificación ambiental autonómica** (Andalucía GICA, Comunitat Valenciana Ley 6/2014, Cataluña Ley 20/2009 más allá de `CHN-*`): no se
     abrió. Marco estatal y Madrid, sí.

## 1. Lo que cambia frente a la hermana: resumen en 10 líneas

| # | Hallazgo | Ids |
|---|---|---|
| 1 | **El despacho de churros (IAE 644.6) SÍ está en el Anexo de la Ley 12/2012** (grupo 644 completo): hasta 750 m² no se le puede exigir licencia previa de actividad. **La sala (676/673) no está.** El modelo (a) y el (b) tienen **regímenes de apertura distintos** | `CHN-49`, `CHN-49b`, `CHN-49c`, `CUN-09`, `CUN-35` |
| 2 | **La norma del aceite de fritura está VIGENTE**: <25 % de compuestos polares, ámbito que **nombra freidurías, bares y puestos de feria**. Cinco artículos derogados en 2013, entre ellos el de «manipulaciones permitidas» | `CUN-01…CUN-03` |
| 3 | **Acrilamida: los churros NO están nombrados en el Rgto. 2017/2158** ni tienen nivel de referencia. Las patatas fritas sí: si la churrería las fríe, se le aplica el Anexo II, parte A (y la parte B si es franquicia) | `CUN-04…CUN-08` |
| 4 | **El IAE tiene cuatro casillas para el churro**: 644.6 (despacho con obrador), 663.1 (ambulante, con nota propia de churrería), 419.3 (industria de masas fritas «churros, buñuelos») y la sala 676/673 | `CUN-09…CUN-14` |
| 5 | **El RD 199/2010 de venta ambulante está DEROGADO desde el 07-08-2021.** Ordenanzas y blogs lo siguen citando | `CUN-19`, `CUN-20` |
| 6 | **Madrid: una «chocolatería» no puede abrir antes de las 8:00; una «cafetería» o un bar, desde las 6:00.** La Orden de 1998 que citan los blogs está derogada | `CUN-34` |
| 7 | **Las freidoras cuentan 1 kW por litro** en el CTE: dos freidoras de 25 L ya suman 50 kW, local de riesgo especial, y por encima de 50 kW, **extinción automática obligatoria** | `CUN-26` |
| 8 | **En Madrid, cocinar con aceite exige campana con filtro de grasas y conducto a cubierta** (la exención eléctrica de ≤4 kW no ampara una freidora); en la vía pública, caseta con filtrado a ≥15 m de huecos | `CUN-23…CUN-25` |
| 9 | **Bombona de feria:** una sola bombona de GLP de menos de 15 kg, con flexible a un solo aparato móvil, no es instalación receptora. Si es mayor o hay varias, entra el reglamento de gas | `CUN-28`, `CHN-48` |
| 10 | **Convenio:** la sala va por hostelería (ALEH VI hasta 2030; Madrid clase C «Chocolaterías»). **No se ha localizado ningún convenio propio de churrerías.** En Madrid, de 0 a 8 h la nocturnidad es un +25 % del salario base | `CUN-29`, `CUN-31…CUN-33`, `CUN-39`, `CUN-40` |

## 2. Actividad con fritura: licencia, humos, ruido

| Id | Norma · artículo · URL (consulta 2026-10-03) | Qué exige (cita corta) | Vigencia | Variantes | Lo materializa |
|---|---|---|---|---|---|
| `CHN-49` `CHN-49b` `CHN-49c` | Ley 12/2012, arts. 2-4 y Anexo (reutilizadas, sin reabrir) | Sin licencia previa hasta 750 m² para las actividades del Anexo; **grupo 644 completo dentro, ningún grupo de la 67** | En vigor (últ. mod. 29-09-2022) | a, b, e | Checklist legal F2 |
| **CUN-35** | **Aplicación** de `CHN-49b` + `CUN-09` | El despacho que se da de alta **solo en el 644.6** cae en el Anexo: **declaración responsable y no licencia previa**. Con mesas (676/673) sale del Anexo y manda la ordenanza municipal o autonómica. **Inferencia declarada:** el obrador de masa anexo al despacho va dentro de la actividad, porque lo faculta la propia nota del 644.6. Confirmarlo con el ayuntamiento | — | **a vs b** | Fila «¿sala o solo despacho? → régimen de apertura» del checklist; párrafo de la landing |
| `CHN-45` `CHN-46` | CTE DB-HS 3 y RITE (reutilizadas) | El HS 3 no regula un local comercial; el RITE excluye el equipo de proceso | — | a, b | — |
| **CUN-23** | **Madrid, Ordenanza 4/2021 de Calidad del Aire y Sostenibilidad (OCAS), art. 23.1** · BOCM 16-04-2021 · https://www.bocm.es/boletin/CM_Orden_BOCM/2021/04/16/BOCM-20210416-46.PDF | «sistema eficaz de captación, extracción forzada y filtrado de humos y olores **con dispositivos de recogida de grasas**»; ventilación y extracción «a través de un **conducto de evacuación a cubierta**»; limpieza y mantenimiento «como mínimo **una vez al año**»; durante el cocinado, nada de huecos practicables al exterior | En vigor desde 2021 (no se comprobó si hay modificaciones posteriores) | a, b (Madrid) | Capítulo de local + fila de CAPEX «campana y conducto» |
| **CUN-24** | OCAS art. 24.1 (excepciones) y anexo I | Sin conducto a cubierta solo si se usan «**exclusivamente aparatos eléctricos** que […] no transmitan olores» y «la suma de la potencia […] sea igual o inferior a **4 Kw**». Desembocadura en cubierta plana: «sobrepasará al menos en **1 m** la altura del edificio propio o la de cualquier otro situado en un **radio de 15 m**» (≤700 kW) | Ídem | a, b | **Inferencia:** una freidora de baño abierto no «cocina en el interior del aparato», así que **no hay exención para una churrería** |
| **CUN-25** | OCAS art. 33.1 (cocinado en suelo de uso público) | «Se requerirá **autorización previa**»; «dentro de casetas, quioscos o vehículos dotados de sistemas de captación y filtrado», a «una distancia mínima de **15 metros** respecto del punto más próximo de cualquier hueco receptor, salvo en el caso de que no utilicen aceites» | Ídem | **c** | Checklist de feria |
| — | Barcelona, Sevilla, Valencia (humos) | **Sin fuente: no verificado** (§0) | — | — | No puede aparecer en el producto sin su ficha |
| — | Ruido / impacto acústico | **Sin fuente:** es municipal y autonómico, no se abrió ninguna ordenanza de ruido | — | a, b, c | Fila «pregunta al ayuntamiento» |

**Qué es requisito legal y qué es proyecto técnico.** Lo legal, en Madrid: campana con filtro de grasas, conducto exclusivo, estanco y a
cubierta, el metro sobre los edificios en 15 m de radio, limpieza al menos anual y la caseta a 15 m en la vía pública. Lo que fija el
**proyecto técnico** (y no el producto): el caudal, la sección y el trazado, el EI 30 del conducto y la potencia de la campana (`CUN-26`).

## 3. Aceite de fritura, APPCC y residuo

| Id | Norma · artículo · URL | Qué exige | Vigencia | Variantes | Lo materializa |
|---|---|---|---|---|---|
| **CUN-01** | **Orden de 26-01-1989, Norma de Calidad para los Aceites y Grasas Calentados**, art. 3 · `BOE-A-1989-2265` · https://www.boe.es/buscar/act.php?id=BOE-A-1989-2265 | «estarán incluidas las industrias dedicadas a la preparación de comidas […] (“Catering”), **freidurías, bares, las cocinas elaboradoras de comida para llevar** […] tanto instalaciones permanentes como de temporada». Y también «los establecimientos que se instalen en calles, plazas o cualquier otro tipo de vía pública con motivo de […] **ferias**» | **En vigor.** Texto consolidado: «Última actualización publicada el 29/03/2013». Carácter de **norma básica** (disposición adicional) | a, b, c, e, f | APPCC de fritura (`CHN-32`) |
| **CUN-02** | Ídem, art. 6 | 6.1 «exentos de sustancias ajenas a la fritura»; 6.2 sin «olor o sabor impropio»; **6.3 «El contenido en componentes polares será inferior al 25 por 100»**, por el método del anexo (cromatografía en columna) | En vigor | Todas | **Registro de aceite**: fecha, freidora, lectura del medidor de polares, cambio sí o no, responsable |
| **CUN-03** | Ídem, arts. 7, 8, 10, 11, 12 y 9 | Los **arts. 7, 8, 10, 11 y 12 están derogados** «por el art. 46 del Real Decreto 176/2013» (`BOE-A-2013-3402`), **incluido el art. 8 «Manipulaciones permitidas»**. El **art. 9 sigue vivo**: prohíbe añadir al baño «sustancias u objetos extraños» y «la comercialización de estos aceites y grasas ya utilizados para uso posterior en la elaboración de productos alimenticios para consumo humano» | Ídem | Todas | El producto **no puede citar el art. 8** como regla de rellenado: hoy no existe |
| `CHN-32` | RD 1021/2022, art. 20: APPCC simplificado con responsable (reutilizada) | Procedimiento basado en el APPCC con **persona responsable** | En vigor | Todas | Plantilla APPCC de fritura |
| `CHN-33` | Rgto. 852/2004, anexo II, cap. IX, pto. 9 (reutilizada) | El equipo usado con alérgenos «no se utilizará» para otros alimentos sin limpiarse antes | En vigor | Todas | **Aceite compartido**: el baño que ha frito algo con otro alérgeno (porra rellena, empanadilla) contamina el churro → freidora dedicada o declararlo |
| **CUN-27** | **Ley 7/2022**, art. 2.a) y art. 25 · `BOE-A-2022-5809` · https://www.boe.es/buscar/act.php?id=BOE-A-2022-5809 (PDF consolidado, «Última modificación: 02 de abril de 2025») | Aceite de cocina usado: «residuo de grasas de origen vegetal y animal que se genera tras ser utilizado en el cocinado de alimentos en […] **hostelería, restauración y análogos**». Para los residuos comerciales: «**obligatoria su recogida separada a partir del 30 de junio de 2022**» | En vigor | Todas | Fila del checklist: **contrato con gestor autorizado y archivo de los justificantes de retirada** |
| — | Prohibición de verter aceite al alcantarillado | **Sin fuente estatal localizada**: va en las ordenanzas municipales de vertido, que no se abrieron | — | — | No afirmar artículo |
| — | Planes autonómicos de control oficial sobre polares | **Sin fuente: no se buscaron** | — | — | — |

## 4. Acrilamida

| Id | Fuente | Qué dice | Consecuencia para el producto |
|---|---|---|---|
| **CUN-04** | **Rgto. (UE) 2017/2158**, art. 1.2 · DOUE L 304 de 21-11-2017 · https://www.boe.es/doue/2017/304/L00024-00044.pdf | Lista cerrada a)-h): patatas fritas de patata fresca; productos de masa de patata; pan; cereales de desayuno; «**productos de bollería, pastelería, repostería y galletería**; galletas, biscotes, barritas de cereales, scones, cucuruchos, barquillos…»; café; sucedáneos; alimentos infantiles. **«Churro» aparece 0 veces** | El churro **no está nombrado**. El reglamento no define «bollería», así que **no se puede afirmar ni que entre ni que quede fuera**: se dice exactamente eso |
| **CUN-05** | Ídem, art. 2.2-2.3 y anexo II | Al minorista que produce estos alimentos le toca la **parte A** del anexo II; a la **franquicia** («como parte o franquicia de un funcionamiento interconectado más amplio») le toca **además la parte B**. Parte A para patatas: freír «**inferiores a 175 °C**», espumar «con frecuencia», **guía de colores** «a la vista del personal» | **Si la churrería fríe patatas frescas (lo permite el 644.6), le aplica seguro.** Franquicia: freidoras calibradas con temporizador y procedimientos normalizados (parte B) |
| **CUN-06** | **Recomendación (UE) 2019/1888**, anexo · https://boe.es/doue/2019/290/L00031-00033.pdf | «Lista no exhaustiva de alimentos en los que se debe controlar la presencia de acrilamida» → «Productos de panadería: […] Donuts […] **Churros**». Los explotadores «deben controlar periódicamente» | Es una **recomendación** (no vinculante). Es la única mención expresa de los churros en el Derecho de la UE |
| **CUN-07** | Estudio prospectivo EP 01 18 (AESAN + CCAA), informe de Cantabria, 12-06-2019 · https://www.saludcantabria.es/documents/20117/34415/INFORME%20DE%20RESULTADOS%20DE%20ACRILAMIDA%20EN%20ALIMENTOS%202018.pdf/66dd4553-d19c-75b6-ca53-844f298cb644 | «**no existe un valor de referencia para las masas fritas, como pueden ser los churros**». Muestras tomadas «en el sector de la restauración o venta ambulante» | Nivel B (informe oficial, no norma). Prueba de que la autoridad ya mira el churro |
| **CUN-08** | Eurofins, noticia de 28-05-2026 · https://www.eurofins.com/en-de/food-testing/news/eu-regulation-on-acrylamide/ | Revisión de la UE en curso: niveles de referencia nuevos y, «for the first time», **niveles máximos**. No menciona los churros. Estado: consultas | **Nivel C, fuente secundaria.** Es riesgo de caducidad (§13), no dato |

**Propuesta:** las buenas prácticas de la parte A (≤175 °C, espumar, guía de colores, color dorado claro) entran como **buena práctica
recomendada para el churro** y como **obligación para las patatas**. Nunca «la ley te obliga a medir acrilamida en los churros».

## 5. Fiscal y censal

| Id | Norma · URL | Texto literal | Variantes |
|---|---|---|---|
| **CUN-09** | **RDLeg 1175/1990**, epígrafe **644.6** · `BOE-A-1990-23930` (PDF consolidado, «Última modificación: 21 de marzo de 2026») · https://www.boe.es/buscar/act.php?id=BOE-A-1990-23930 | «Comercio al por menor de **masas fritas**, con o sin coberturas o rellenos, patatas fritas, productos de aperitivo, frutos secos, golosinas, **preparados de chocolate** y bebidas refrescantes». Nota: «faculta para **la elaboración de los productos de churrería**; así como patatas fritas, en el propio establecimiento, siempre que su comercialización se realice en las propias dependencias de venta» (amplía `CHN-72`) | **b** y a |
| **CUN-10** | Ídem, **grupo 676** | «Servicios en **chocolaterías**, heladerías y horchaterías». Nota: «Cuando los establecimientos clasificados en este epígrafe **permanezcan abiertos al público durante seis meses o menos al año**, tributarán por la mitad de la cuota» | **a**; temporada (cierre en verano) |
| **CUN-11** | Ídem, epígrafe **663.1** | «Comercio al por menor fuera de un establecimiento comercial permanente de productos alimenticios». Nota: al dedicado exclusivamente a masas fritas «se faculta a que pueda **elaborar los productos propios de churrería** y patatas fritas en la propia instalación o vehículo» | **c** |
| **CUN-12** | Ídem, epígrafe **419.3** | «Industrias de elaboración de masas fritas». Nota: «comprende la elaboración de masas fritas (**churros, buñuelos**, etc.) y de patatas fritas». La regla 4.ª (`CHN-94`) y `CHN-96` (la industria faculta para vender al por mayor y al por menor) | **f** |
| **CUN-13** | Ídem, **grupo 675** y epígrafe **674.7** | 675: «Servicios en quioscos, cajones, barracas u otros locales análogos, situados en mercados […] al aire libre en la vía pública», con la misma nota de **seis meses o menos, mitad de cuota**. 674.7: «Servicios que se prestan en parques o recintos feriales clasificados en el Epígrafe 989.3» | **c** con mesas |
| **CUN-14** | Ídem, **grupo 673** | «En cafés y bares, con y sin comida». «Nota común a los grupos 671, 672 y 673: […] facultados para vender, en el propio establecimiento, los productos objeto del respectivo servicio». **El grupo 676 no lleva esa nota.** **Inferencia:** una chocolatería en el 676 que además vende churros al peso para llevar necesita también el 644.6 (regla 4.ª, `CHN-94`) | a, e |
| `CHN-73` | TRLRHL art. 82.1 | Alta sí, pago casi nunca: exentos los dos primeros años, las personas físicas y las sociedades con menos de 1.000.000 € de cifra de negocios | Todas. **No reproducir cuotas** (`CHN-72` documenta una errata de conversión en el 644.5; en el 676 las conversiones leídas son coherentes, 16.560 ptas = 99,53 € y 12.420 ptas = 74,65 €) |
| **CUN-15** | **RD 10/2025 (CNAE-2025)**, títulos · https://www.boe.es/buscar/act.php?id=BOE-A-2025-587 | «10.71 Fabricación de pan y de productos frescos de panadería y pastelería» · «47.24 Comercio al por menor de pan, productos de panadería y confitería» · «56.11 Restaurantes» · «**56.12 Puestos de comidas**» · «56.30 Servicios de bebidas» · ⚠️ «**47.81 Comercio al por menor de vehículos de motor**» | — |
| **CUN-16** | Correspondencia IAE → CNAE | **Sin fuente primaria** (notas del INE no abiertas). Candidatos: 419.3 → 10.71 · 644.6 → 47.24 o 56.11 · 676/673 → 56.11 o 56.30 · 663.1/675 → 56.12. **Trampa verificada:** quien copie el «4781 puestos de venta de alimentos» del CNAE-2009 se encuentra en el CNAE-2025 con la clase de **vehículos de motor** | Comprobar en el buscador del INE en F2; doble código (`CHN-74b`) |
| `CHN-71` `CHN-71c` `FC-IVA-01…03` | Ley 37/1992 arts. 90-91 + DGT V2254-22 | Comida servida en sala, **10 %**; comida para llevar = entrega de bienes, **10 %** como alimento; alcohol y refresco azucarado para llevar, **21 %** | Churros para llevar o en sala, **10 %**; feria con o sin mesas, **10 %** |
| **CUN-17** | **RD 650/2011**, art. 2.1 · https://www.boe.es/eli/es/rd/2011/05/09/650/con («Última actualización 04/10/2023») | Bebidas refrescantes: «bebidas analcohólicas, carbonatadas o no, **preparadas con agua** […] que contengan uno o más de los siguientes ingredientes: […] azúcares […] aromas» | — |
| **CUN-18** | **Chocolate a la taza para llevar: zona gris** | Hecho con leche, no encaja en la definición de `CUN-17` → **10 % (inferencia)**. Hecho con agua y un preparado azucarado, **podría** leerse como bebida refrescante → 21 %. **No se localizó ninguna consulta de la DGT.** **No afirmar el tipo en el producto**; parámetro en celda verde con la nota «consulta a tu asesor» | a, b, c |
| `CHN-75` | RD 1007/2023 (Verifactu) | Sociedades, antes del 1-1-2027; el resto, antes del 1-7-2027 | Todas |

## 6. Higiene, alérgenos y registro sanitario

| Id | Fuente | Qué exige / qué resuelve | Variantes |
|---|---|---|---|
| `CHN-51` | RD 1021/2022 art. 10 + RD 1086/2020 art. 30 (reutilizada) | Servir **chocolate a la taza y churros es elaborar comidas preparadas**: 63 °C en caliente, zona de elaboración separada de la venta | a, b, e |
| **CUN-21** | **RD 1021/2022, art. 2.a)** · https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681 («sin modificaciones») | El comercio al por menor incluye «los **locales ambulantes o provisionales (como carpas, tenderetes y vehículos de venta ambulante)**» y «establecimientos de restauración y hostelería» → la caseta de feria es minorista: **registro autonómico, no RGSEAA** (`CHN-39`) | c |
| **CUN-22** | **Rgto. (CE) 852/2004, anexo II, capítulo III** · corrección DO L 226 de 25-06-2004 · https://www.boe.es/doue/2004/226/L00003-00021.pdf | «Requisitos de los locales ambulantes o provisionales (como carpas, tenderetes y vehículos de venta ambulante)»: higiene de manos con «limpieza y secado higiénico», superficies «lisas, lavables, resistentes a la corrosión y no tóxicas», «suministro suficiente de agua potable caliente, fría o ambas», «almacenamiento y la eliminación higiénicos» de desechos y control de temperaturas | **c** (checklist del puesto) |
| `CHN-34` `CHN-34b` | RD 126/2015 + Rgto. 1169/2011 | Los 14 alérgenos, también sin envasar; por escrito y accesibles | Gluten (harina) siempre; **leche** en el chocolate; soja o frutos de cáscara según la cobertura o el preparado; huevo si la masa lo lleva |
| `CHN-37` | Rgto. 828/2014 | «Sin gluten» = ≤20 mg/kg **analítico** | **Casi nunca se puede decir en una churrería**: harina de trigo en el aire y en el aceite compartido (`CHN-33`) |
| `CHN-38` `CHN-41` `CHN-39` `CHN-40` | RD 1021/2022 arts. 3 y congelación; RD 191/2011 | El minorista solo sirve a otros minoristas si es marginal, localizado y **restringido**; servir a un inscrito en el RGSEAA rompe la excepción | e, **f** |
| **CUN-30** | **Guía informativa del RGSEAA rev. 16** (11-06-2025), p. 10 · https://www.comunidad.madrid/docs/assets/2025/06/25/guia_informativa_sobre_el_registro_general_sanitario_de_empresas_alimentarias_y_alimentos_11-06-2025_rev_16.pdf | Ejemplo literal de actividad restringida: «**Churrería o pastelería que sirve a la cafetería**». Clave 20 «Cereales, harinas y derivados»: act. 10 «Productos de pastelería, confitería, bollería y repostería», act. 12 «Productos semielaborados». **No hay actividad «masas fritas»**: encajar la masa o el churro congelado en la 10 o la 12 es **inferencia** (nivel B) | **f** y e |

## 7. Venta ambulante y ferias

| Id | Norma · URL | Qué dice | Vigencia |
|---|---|---|---|
| **CUN-19** | **RD 199/2010** (venta ambulante) · `BOE-A-2010-4173` · https://www.boe.es/buscar/doc.php?id=BOE-A-2010-4173 | Análisis del BOE: «**Fecha de derogación: 07/08/2021** · SE DEROGA, por Real Decreto 538/2021» (`BOE-A-2021-13489`), por invadir competencias autonómicas (STC 143/2012) | **DEROGADO.** No citarlo |
| **CUN-20** | **Ley 7/1996**, arts. 53-55 · https://www.boe.es/buscar/act.php?id=BOE-A-1996-1072 | Art. 54 (redacción de la Ley 1/2010): autorización del ayuntamiento, «la duración de las mismas **no podrá ser por tiempo indefinido**», selección con transparencia, «no dará lugar a un procedimiento de **renovación automática**». Art. 55: exponer los datos y la autorización «en forma fácilmente visible» | En vigor (art. 53, con un inciso anulado por la STC 124/2003) |
| **CUN-36** | **Ordenanza de venta ambulante de Cehegín** (borrador definitivo, 2022) · https://transparencia.cehegin.es/storage/uploads/1653657221Def.%20Ord.%20Venta%20Ambulante%20-%20BORRADOR%20DEFINITIVO%20TOTAL.pdf | Excluye de la venta en puestos desmontables los «**Puestos de churros y gofres**» (no desmontables o quioscos), y **sigue remitiendo al RD 199/2010** | Ejemplo de dos cosas: el puesto de churros suele ir por **ocupación del dominio público o quiosco**, no por «ambulante», y la norma derogada sigue viva en el papel |
| **CUN-37** | **Ordenanza fiscal de la ELA de Ochavillo del Río (Córdoba)**, art. 7.C · BOP Córdoba nº 144 de 28-07-2026 · https://bop.dipucordoba.es/visor-pdf/28-07-2026/BOP-A-2026-2586.pdf | «Churrerías y chocolaterías con terraza: **550 euros (por toda la feria)**»; buñuelos y patatas sin terraza, 15 €; fianza de **50 €** | Ejemplo de **pueblo pequeño**: no es extrapolable a una capital |
| `CUN-25` · `CUN-01` · `CUN-22` · `CUN-21` | — | Madrid exige autorización previa y caseta con filtrado a 15 m; la norma del aceite nombra las ferias; el anexo II, cap. III, del 852/2004; el registro autonómico | — |

**Frontera con `plan-negocio-food-truck` / `kit-tareas-food-truck`:** la nota del 663.1 y el anexo II, cap. III, son comunes a cualquier
vehículo. **Recomendación:** la variante (c) entra como **epígrafe + checklist de feria** y la venta cruzada va al food truck. No se cifra.

## 8. Gas y protección contra incendios

| Id | Norma · URL | Qué exige | Variantes |
|---|---|---|---|
| `CHN-48` | RD 919/2006, ITC-ICG 07 (reutilizada) | Inspección de la instalación receptora **cada cinco años** | a, b con gas |
| **CUN-28** | **RD 919/2006, Reglamento, art. 2** (definición de instalación receptora) · https://www.boe.es/buscar/act.php?id=BOE-A-2006-15345 («Última actualización 03/09/2025») | «**No tendrán el carácter de instalación receptora** las instalaciones alimentadas por un **único envase** o depósito móvil de GLP **de contenido inferior a 15 kg**, conectado por tubería flexible o acoplado directamente a **un solo aparato** de utilización móvil». Las bombonas de GLP «para uso propio» van por la **ITC-ICG 06** | **c**: con una bombona de 35 kg, o con dos aparatos, **ya es instalación receptora** |
| **CUN-26** | **CTE DB-SI**, SI 1 tabla 2.1, notas (2) y (3), y SI 4 tabla 1.1 · https://www.codigotecnico.org/pdf/Documentos/SI/DBSI.pdf (última modificación del DB: **RD 164/2025**, BOE 10-04-2025) | Cocinas: riesgo especial **bajo 20<P≤30 kW, medio 30<P≤50, alto P>50**. «Las **freidoras** […] se computarán a razón de **1 kW por cada litro de capacidad**, independientemente de la potencia que tengan». **Extinción automática** «en cocinas en las que la potencia instalada exceda […] de **50 kW**» (usos distintos del hospitalario y del residencial público). Nota (3): campanas a **50 cm** de material que no sea A1, conductos **exclusivos** con registros, **EI 30** dentro del edificio, filtros a **>0,50 m** del foco (1,20 m si son de parrilla o de gas), inclinación **>45°** con bandeja de grasas | a, b. **Celda del xlsx:** litros de freidora → kW → nivel de riesgo → ¿extinción automática? |
| **CUN-38** | **RIPCI (RD 513/2017)**, anexo I, sección 1.ª, apdo. 4.5.e) y apdo. 16 · https://www.boe.es/buscar/act.php?id=BOE-A-2017-6606 («Última actualización 03/09/2025») | «Los agentes extintores deben ser **adecuados para cada una de las clases de fuego**»; «**Clase F**: Fuegos derivados de la utilización de ingredientes para cocinar (aceites y grasas vegetales o animales)». Sistemas fijos en cocinas comerciales: UNE-EN 17446:2022 | Todas. **El RIPCI define la clase y exige el agente adecuado**; cuántos extintores hacen falta lo dice el CTE (no se reabrió) |
| — | RSCIEI | Solo se aplica al obrador industrial (419.3) si es establecimiento industrial: **no verificado** | f |

## 9. Laboral

| Id | Fuente | Dato | Variantes |
|---|---|---|---|
| **CUN-29** | **ET art. 36.1-2** · https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430 (consolidado, «Última actualización 04/12/2025») | Nocturno «entre las **diez de la noche y las seis de la mañana**»; trabajador nocturno = «no inferior a **tres horas**» de su jornada diaria en ese periodo; **máx. 8 h** de promedio en 15 días; «**no podrán realizar horas extraordinarias**»; quien recurra a él con regularidad «deberá informar de ello a la autoridad laboral»; retribución «en la negociación colectiva» | El churrero que entra a las 4:00-5:00 **suma ≥3 h nocturnas** → sin horas extra y nocturnidad por convenio |
| **CUN-31** | **VI Acuerdo Laboral Estatal de Hostelería (ALEH VI)**, art. 4 · BOE 10-03-2023, `BOE-A-2023-6344` · https://www.boe.es/boe/dias/2023/03/10/pdfs/BOE-A-2023-6344.pdf | Ámbito: «cafés, bares, cafeterías […] **freidurías** […] **quioscos** […] **chocolaterías**»; la lista «no es exhaustiva». **«Churrería» no aparece literalmente** | a, c con mesas, e |
| **CUN-32** | Modificación del ALEH VI, art. 6 · BOE 04-09-2026, `BOE-A-2026-18630` · https://www.boe.es/boe/dias/2026/09/04/pdfs/BOE-A-2026-18630.pdf | «nuevo periodo de vigencia del acuerdo, **hasta el 31 de diciembre de 2030**» | — |
| **CUN-39** | **Convenio de Hostelería de la Comunidad de Madrid**, código **28002085011981** · BOCM nº 82 de 06-04-2024 · https://www.bocm.es/boletin/CM_Orden_BOCM/2024/04/06/BOCM-20240406-2.PDF | Ámbito con «freidurías, chiringuitos, […] quioscos, […] chocolaterías». **Clase C:** «Cafeterías de una taza; **Chocolaterías**, Heladerías […]; Cafés-Bares; Bares» y se asimilan las instalaciones «eventuales y desmontables» en «verbenas, fiestas populares». Salario base mensual **2025, clase C**: nivel III (cocinero, camarero, dependiente de cafetería) **1.160,37 €** · nivel IV (ayudante de cocina, ayudante de camarero) **1.127,42 €** · nivel V **1.086,31 €**; plus convenio **191,22 €** × 11 meses; manutención 57,82 €. Vigencia 2023-2025 «se prorrogará automáticamente» salvo denuncia | a. **Estado del convenio en 2026 (¿denunciado?, ¿hay uno nuevo?): no verificado.** La categoría «churrero» **no existe**: hay que encajarla por función (inferencia: nivel III) |
| **CUN-40** | Ídem, art. 27 | De 22:00 a 0:00, **+1 %** del salario base; de **0:00 a 8:00, +25 %**; con **5 o más horas** entre las 22 y las 8, toda la jornada cuenta como nocturna | a. Celda del P&L «horas de 0 a 8 h» |
| `CHN-65` `CHN-65b` | Convenio de confiterías, pastelerías y repostería de Madrid (reutilizadas) | Despacho de dulce dentro; fabricación condicionada a la actividad principal | b, f: **¿un despacho-obrador de churros es confitería? No se ha verificado**: el texto no nombra las masas fritas en lo que se leyó |
| **CUN-33** | Búsqueda de un **convenio propio de churrerías** | Ninguno localizado. Revisados sin «churr» ni «masas fritas»: hostelería de Guadalajara (BOP 23-07-2025), panadería de Córdoba (BOP 02-05-2023), panadería de Madrid (BOCM 21-09-2024) y panadería de Burgos 2023-2026 | **Búsqueda no exhaustiva** (sin REGCON). El producto **no puede afirmar** que exista ni que no |
| `CHN-67` `CHN-68` `CHN-69` | SMI 2026, registro de jornada, formación de manipuladores | **1.221 €/mes**, 17.094 €/año · registro diario, conservado 4 años · registro de formación, **no carnet** | Todas |
| — | PRL: quemaduras con aceite a 180-190 °C | **Sin fuente específica** abierta (LPRL y evaluación de riesgos genéricas). Lo verificable es la **clase F** (`CUN-38`) y la campana (`CUN-26`) | — |

## 10. Horarios, terrazas, envases y desperdicio

| Id | Fuente | Dato |
|---|---|---|
| **CUN-34** | **Orden de 21-04-2022** (Consejería de Presidencia, Justicia e Interior de Madrid), art. 3 · BOCM 29-04-2022 · https://www.bocm.es/boletin/CM_Orden_BOCM/2022/04/29/BOCM-20220429-10.PDF | «c) Cafeterías, bares, cafés-bares y asimilables: **desde las 6:00 horas** hasta las 2:00» · «d) **Chocolaterías**, heladerías, salones de té, croissanteries y asimilables: **desde las 8:00 horas hasta las 1:00**». Terrazas: de 8:00 a 1:00 (del 1-nov al 15-mar) y de 8:00 a 1:30 (del 16-mar al 31-oct). **Deroga la Orden 1562/1998.** Modificaciones posteriores: no comprobadas → **una churrería de desayunos en Madrid se clasifica como cafetería o bar, no como chocolatería**, o no abre antes de las 8 |
| `CHN-77` | Ley 1/2004 de horarios comerciales | Despacho de **menos de 300 m²** → libertad horaria comercial (art. 5.2). **La sala va por la norma autonómica de espectáculos** (`CUN-34`), no por esta ley |
| — | Terrazas (ordenanzas) | **Sin fuente: no se abrió ninguna ordenanza de terrazas** |
| **CUN-41** | **Ley 7/2022**, art. 55 y anexo IV | Plástico de un solo uso = «fabricado **total o parcialmente** con plástico». Anexo IV.A: «Vasos para bebidas, incluidos sus tapas» y recipientes para consumo inmediato «para llevar» → «a partir del **1 de enero de 2023**, se deberá **cobrar un precio** por cada uno […] diferenciándolo en el ticket». Anexo IV.B, **prohibidos**: cubiertos, platos, pajitas, agitadores y EPS. **Inferencia:** el **cucurucho de papel sin plástico** queda fuera; el **vaso de papel plastificado del chocolate para llevar, dentro** |
| `CHN-62` `CHN-63` | Impuesto al plástico (0,45 €/kg) y envases reutilizables (RD 1055/2022) | Reutilizadas |
| `CHN-64` `CHN-92` | Ley 1/2025 | **Microempresa fuera del art. 6** (plan de prevención, donación); **el art. 8 sí obliga a la sala**: el cliente puede llevarse lo que no consume. El excedente de churros del día no genera ninguna obligación de donar a una microempresa |

## 11. Chocolate a la taza: qué puede decir la carta

| Id | Fuente | Dato |
|---|---|---|
| `CHN-05` | RD 1055/2003, aps. 1.11, 1.12 y 6.e) | «Chocolate a la taza»: ≥35 % de cacao, ≥18 % de manteca, ≤8 % de harina o almidón; el «familiar», ≥30 % y ≤18 %; «para su consumo cocido» |
| **CUN-42** | RD 1055/2003, ap. 1.11 · https://www.boe.es/buscar/act.php?id=BOE-A-2003-15599 | Es «el **producto** obtenido a partir de productos de cacao, azúcares y harina o almidón»: la norma define el **polvo o la tableta**, no la bebida servida |
| `CHN-11` | Sucedáneo | Si la manteca de cacao se ha sustituido por otras grasas, el producto **no se llama chocolate** |
| — | **Propuesta (inferencia, sin cita)** | Con un preparado que cumple 1.11 → «chocolate a la taza» en la carta, con la etiqueta del proveedor archivada. Con cobertura, leche y almidón propios → «chocolate a la taza **elaborado con cobertura X % cacao**», o «chocolate caliente». Con un preparado de **menos del 35 %** o con grasa vegetal → **ni «chocolate a la taza» ni «chocolate»**; vale «bebida de cacao» o la denominación del proveedor |

## 12. Tabla de vigencia (a 2026-10-03)

| Norma | Estado | Última modificación vista |
|---|---|---|
| Orden 26-01-1989, aceites calentados | **En vigor** (arts. 7, 8, 10-12 derogados) | 29-03-2013 |
| RD 176/2013 (deroga parte de la anterior) | En vigor | — |
| Rgto. (UE) 2017/2158, acrilamida | En vigor · **revisión en marcha** (`CUN-08`) | DOUE 2017 (consolidados posteriores no abiertos) |
| Recomendación (UE) 2019/1888 | Vigente (no vinculante) | — |
| RDLeg 1175/1990, tarifas del IAE | En vigor | 21-03-2026 |
| RD 10/2025, CNAE-2025 | En vigor | sin modificaciones |
| Ley 37/1992 (IVA) · RD 650/2011 | En vigor | 28-02-2026 · 04-10-2023 |
| **RD 199/2010, venta ambulante** | **DEROGADO** por RD 538/2021 | 07-08-2021 |
| Ley 7/1996, arts. 53-55 | En vigor | art. 54: Ley 1/2010 |
| Rgto. 852/2004, anexo II, cap. III | En vigor | (cap. IX: Rgto. 2021/382, `CHN-33`) |
| RD 1021/2022 | En vigor | sin modificaciones |
| Ley 12/2012 | En vigor | 29-09-2022 |
| OCAS Madrid 4/2021 | En vigor (posteriores no comprobadas) | BOCM 16-04-2021 |
| **Orden Madrid 1562/1998, horarios** | **DEROGADA** por la Orden de 21-04-2022 | — |
| Orden Madrid 21-04-2022 | En vigor (posteriores no comprobadas) | BOCM 29-04-2022 |
| CTE DB-SI | En vigor | RD 164/2025 |
| RIPCI RD 513/2017 · RD 919/2006 | En vigor | 03-09-2025 · 03-09-2025 |
| Ley 7/2022 | En vigor | 02-04-2025 |
| ET (RDLeg 2/2015) | En vigor | 04-12-2025 |
| ALEH VI | En vigor hasta el 31-12-2030 | BOE 04-09-2026 |
| Convenio de hostelería de Madrid 28002085011981 | Vigencia inicial vencida el 31-12-2025; **prórroga o denuncia no verificadas** | BOCM 06-04-2024 |

## 13. Los 5 errores normativos más repetidos en las fuentes gratuitas

| # | Lo que dicen (cita) | Corrección |
|---|---|---|
| E1 | asest.es, «Cómo emprender en un negocio de comidas»: «**Poseer el carnet de manipulador de alimentos es el requisito legal base**» (https://asest.es/story/como-emprender-en-negocio-de-comidas-autonomos/) | El carnet no existe; lo que se exige es la **formación acreditada por el empresario** (`CHN-69`) |
| E2 | asest.es, «La Antigua Churrería franquicia»: licencia «se deben tramitar en el ayuntamiento» y «**Antes de la licencia de apertura, tendrás que pasar por una inspección de sanidad**» (https://asest.es/story/la-antigua-churreria-franquicia/) | Un **despacho 644.6 ≤750 m² no necesita licencia previa** (`CUN-35`). El registro sanitario es una comunicación autonómica **que no habilita y no lleva inspección previa** (`CHN-39`, `CHN-43`) |
| E3 | Ordenanza de Cehegín (2022): «modalidades previstas en el **real decreto 199/2010**» (`CUN-36`) | Derogado desde el **07-08-2021** (`CUN-19`); la base estatal es la Ley 7/1996, arts. 53-55, y cada comunidad autónoma |
| E4 | Resúmenes que siguen dando por vigente la **Orden 1562/1998** de horarios de Madrid, con «cafeterías 6:00» como regla general | Derogada en 2022. Y la **chocolatería abre a las 8:00**, no a las 6:00 (`CUN-34`) |
| E5 | Nuestro propio post `ia-churrerias-guia-completa.md` (tabla de inversión): «**Licencias y permisos 2.000 - 6.000** […] Incluye tasa de apertura, licencia de obra menor» | **Cifra sin fuente** y sin la distinción despacho/sala. No reutilizarla en el producto; **corregir el post al lanzar** (reescritura quirúrgica, regla de los ensambladores) |

## 14. Lo que NO se puede afirmar en el copy

1. «La ley te obliga a controlar la acrilamida de los churros» (`CUN-04`): no hay nivel de referencia (`CUN-07`).
2. Ningún tipo de IVA para el **chocolate a la taza para llevar** (`CUN-18`).
3. «Necesitas licencia de apertura» o «no necesitas licencia» **sin decir el modelo**: el despacho no la necesita; la sala depende del municipio (`CUN-35`).
4. Cualquier artículo del **RD 199/2010** o de la **Orden 1562/1998** (`CUN-19`, `CUN-34`).
5. «Convenio de churrerías» o «la categoría de churrero» (`CUN-33`, `CUN-39`).
6. Requisitos de humos de **Barcelona, Sevilla o Valencia** (§0).
7. «Sin gluten» como argumento de carta (`CHN-37`, `CHN-33`).
8. «Carnet de manipulador» (`CHN-69`).
9. El **art. 8** de la norma del aceite («rellenar con aceite nuevo está permitido»): derogado (`CUN-03`).
10. Que un cucurucho «cumple la ley de plásticos» sin conocer su composición (`CUN-41`).
11. Cuotas del IAE (errata documentada en `CHN-72`; casi nadie las paga, `CHN-73`) y la tasa de feria de Ochavillo como si fuera un orden de magnitud nacional (`CUN-37`).
12. Copy comercial: nada de «verificado contra el BOE». Lideran los entregables: el checklist por modelo, el registro de aceite y la calculadora de freidoras.

## 15. Las 8 normas cuyo cambio invalidaría el producto (riesgo de caducidad)

| # | Norma | Por qué | Vigilancia propuesta |
|---|---|---|---|
| 1 | **Rgto. (UE) 2017/2158** | Revisión con **niveles máximos** por primera vez (`CUN-08`); si entran las masas fritas, cambia el APPCC | Mirar EUR-Lex en cada versión 2.x |
| 2 | **Orden de 26-01-1989** (aceites) | Norma de 1989 ya recortada en 2013; una norma nueva cambiaría el 25 % | BOE, en la pestaña «Análisis» |
| 3 | **Ley 12/2012, Anexo** | Sostiene el «despacho sin licencia previa» | Consolidado del BOE |
| 4 | **RDLeg 1175/1990, 644.6 / 663.1 / 419.3 / 676** | Sostienen el mapa de altas | Consolidado del BOE (modificado el 21-03-2026) |
| 5 | **Orden de horarios de Madrid de 2022** | Sostiene la trampa de las 8:00 | BOCM |
| 6 | **Convenio de hostelería de Madrid** (vencido el 31-12-2025) y **ALEH VI** | Las tablas del P&L de ejemplo | BOCM/REGCON antes de F2 |
| 7 | **RD de registro horario digital** (pendiente de BOE) y **Verifactu** (2027) | Cambian la checklist de apertura | BOE |
| 8 | **CTE DB-SI** (1 kW por litro, 20/50 kW) | Decide la campana y la extinción automática | codigotecnico.org |

## 16. Lo que esta lente propone para F2 (entregables factibles con el molde de la hermana)

| Entregable | Molde | Qué añade la churrería | Ids |
|---|---|---|---|
| `checklist-legal-licencias-churreria.xlsx` | `checklist-legal-licencias-y-cacao` | Filas por modelo **a/b/c/f**: alta en el IAE (644.6 / 676-673 / 663.1 / 419.3), ¿Anexo de la Ley 12/2012?, horario de Madrid, gestor de aceite, gas (<15 kg o receptora), clase F | `CUN-09…14`, `CUN-19…28`, `CUN-30`, `CUN-34`, `CUN-35`, `CUN-36`, `CUN-38` |
| **Registro de aceite y fritura** (hoja nueva o libro nuevo) | `vida-util-rellenos-y-rotacion` | Fecha, freidora, polares (umbral **25 %** en celda verde), cambio, retirada por el gestor, temperatura objetivo (175 °C solo para patatas) | `CUN-01…05`, `CUN-27` |
| Calculadora de local: **freidoras → kW → riesgo** | `capacidad-obrador-y-clima` | Litros × 1 kW, umbrales 20/30/50 kW, aviso de extinción automática | `CUN-26` |
| P&L | `plan-financiero-3-anos-chocolateria` | Horas de 0 a 8 h × 25 % (Madrid, parámetro), cierre de verano ↔ mitad de cuota del 676 (sin cifra), IVA para llevar como parámetro | `CUN-10`, `CUN-18`, `CUN-29`, `CUN-40` |

**Coste en tokens de esta lente:** solo lectura de fuentes primarias, sin redacción de producto.
