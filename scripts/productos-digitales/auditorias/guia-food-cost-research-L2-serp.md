# LENTE 2 — Qué regala ya la SERP (y qué NO) — Guía Food Cost + Ingeniería de Menú

Fecha de research: 2026-09-03. Método: WebSearch para localizar la URL de cada fuente listada + WebFetch para leer y esquematizar cada página (H2/H3, ejemplo numérico, plantilla, matriz, cobertura temática, fecha). Mercado: España. 19 URLs analizadas con éxito de las ~22 objetivo; 3 inaccesibles (documentado abajo, con evidencia del intento).

---

## 0. Alcance real vs. objetivo

Objetivo: ESAH, Ditaly, Quescrem, ComboHR (2 posts), elBulliFoundation, Barcelona Culinary Hub (2), Purohospitality (2), Clab Group (2), eloyrodriguez.com, ingenieriademenu.com (2), CESAE, Findus, Restaurantic, Truyol, Hosteltáctil, tSpoonLab, Gosufra, academiaculinaria.org.

**Analizadas con éxito (19):**

| # | Fuente | URL | Tema |
|---|---|---|---|
| 1 | ESAH | estudiahosteleria.com/blog/cocina/guia-definitiva-como-hacer-un-escandallo-de-cocina/ | Escandallo (índice) |
| 2 | Ditaly | ditaly.es/como-hacer-un-escandallo-en-cocina/ | Escandallo |
| 3 | Quescrem (EN) | quescrem.es/en/blog-en/training/how-to-make-the-price-of-a-dish-and-calculate-the-selling-price/ | Escandallo / pricing |
| 4 | ComboHR | combohr.com/es/blog/escandallo-cocina | Escandallo |
| 5 | elBulliFoundation (CaixaBankLab) | caixabanklab.com/elbullifoundation/es/escandallos/ | Escandallo |
| 6 | Barcelona Culinary Hub | barcelonaculinaryhub.com/blog/menu-engineering | Menu engineering |
| 7 | Barcelona Culinary Hub | barcelonaculinaryhub.com/blog/que-es-el-food-cost-y-como-calcularlo-paso-paso | Food cost |
| 8 | Purohospitality | purohospitality.com/que-es-el-food-cost | Food cost |
| 9 | Purohospitality | purohospitality.com/que-es-el-menu-engineering | Menu engineering |
| 10 | Clab Group | clabgroup.com/es/blog/food-cost/ | Food cost |
| 11 | Clab Group | clabgroup.com/es/blog/menu-engineering/ | Menu engineering |
| 12 | eloyrodriguez.com | eloyrodriguez.com/menu-engineering-ingenieria-menus/ | Menu engineering |
| 13 | ingenieriademenu.com | ingenieriademenu.com/menu-engineering-ingenieria-de-menus/ | Menu engineering |
| 14 | ingenieriademenu.com | ingenieriademenu.com/food-cost/ | Food cost |
| 15 | CESAE | cesae.es/blog/las-claves-de-menu-engineering | Menu engineering |
| 16 | Restaurantic | restaurantic.es/220-ingenieria-de-menu-que-es-y-como-aplicarla-es | Menu engineering |
| 17 | Hosteltáctil | hosteltactil.com/blog/menu-engineering/ | Menu engineering (contenido pobre, ver nota) |
| 18 | tSpoonLab | tspoonlab.com/menu-engineering/ | Menu engineering (doc de producto, no blog) |
| 19 | academiaculinaria.org | academiaculinaria.org/index.php/gastronomia-cocina/article/view/42 | Paper académico |

**Inaccesibles (3), con evidencia del intento:**

- **Findus Foodservices** (findusfoodservices.es/novedades/menu-engineering/) — 2 intentos de WebFetch, timeout de 60 s en ambos.
- **Truyol** (truyol.com/blog/como-disenar-el-menu-restaurante-aplicando-la-ingenieria-de-menu/) — 3 intentos de WebFetch (http y https), timeout de 60 s en todos.
- **Gosufra** — WebSearch (general y `site:gosufra.com`) no devuelve ningún artículo en español sobre food cost, escandallo o ingeniería de menú; el único contenido indexado del dominio es un post en **italiano** sobre POS offline (`gosufra.com/it/blog/pos-offline/`). Gosufra es un proveedor de TPV con foco en el mercado italiano; no tiene, o no tiene indexado, contenido educativo en español sobre el tema. **Sin fuente** para incluirlo en el mapa de cobertura.

**Nota sobre Hosteltáctil y tSpoonLab:** ambas devolvieron contenido notablemente más pobre que el resto (Hosteltáctil: solo el H1 "Menu Engineering" sin H2/H3 recuperables, contenido probablemente cargado por JS; tSpoonLab: es un artículo del *Learn Center* — documentación de producto para clientes del software, no una pieza de blog pensada para SEO/autoridad). Se cuentan igualmente en el mapa de cobertura (con lo poco que aportan) para no perder la señal: ninguna de las dos desarrolla el tema, lo que refuerza el hueco de contenido de calidad real.

---

## 1. Mapa de cobertura (temas × fuentes)

`✓` = tratado con desarrollo · `⚠` = mencionado de pasada / sin desarrollo · `✗` = no tratado · `✓✓`/`✓✓✓` = tratado con ejemplo numérico o profundidad relevante

| Fuente | IVA | Mermas | Delivery | Bebidas | Pastelería | Inflación | Psicología precios | Matriz específica | Ejemplo numérico | Plantilla descargable |
|---|---|---|---|---|---|---|---|---|---|---|
| ESAH | ✗ | ⚠ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Ditaly | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓✓ (pizza, 1,89€→6,30€) | ✗ |
| Quescrem | ✗ | ✓ | ⚠ | ⚠ | ✓ | ✗ | ✓ | ✗ | ✓ (hamburguesa, 2,30€→6,50€) | ✗ |
| ComboHR | ✗ | ⚠ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ (hamburguesa, 5,50€) | ✗ |
| elBulliFoundation | ✗ | ✓✓ | ✗ | ✗ | ⚠ | ✗ | ✗ | ✗ | ✓ (pescado, merma 45%) | ✗ (remite a manual) |
| BCH — menu engineering | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ⚠ (no nombra el método) | ✗ | ✗ |
| BCH — food cost | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✓ (4€/12€=33,3%) | ✗ |
| Purohospitality — food cost | ✓ | ✓✓ | ✗ | ✓ | ✓ | ⚠ | ✓ | ⚠ | ✓✓✓ (4 casos con € reales) | ⚠ (mención sin entregar) |
| Purohospitality — menu eng. | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓✓ | ✓ Kasavana&Smith | ✓✓ (caso 90 días, +7pp) | ✗ |
| Clab Group — food cost | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ (4€/12€=33,3%) | ✗ |
| Clab Group — menu eng. | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ Kasavana&Smith | ✗ | ✗ |
| eloyrodriguez.com | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ⚠ Kasavana&Smith (mención) | ✗ (solo genérico 50/100%) | ✗ |
| ingenieriademenu — menu eng. | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ⚠ (neuromarketing, breve) | ✓ Kasavana&Smith | ✓✓ (4 carnes, margen 8,25€) | ✗ (en esta página) |
| ingenieriademenu — food cost | ✓ | ✗ | ✗ | ⚠ | ✗ | ✗ | ✓ | ✓ Kasavana&Smith + BCG | ✓✓ (atún rojo, margen 11,55€) | ✓✓ (2 plantillas, de pago) |
| CESAE | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ Kasavana&Smith | ✗ | ✗ |
| Restaurantic | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ (matriz propia, sin nombrar) | ✗ | ✗ |
| Hosteltáctil | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? *(contenido no recuperable)* |
| tSpoonLab | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| academiaculinaria.org | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ Kasavana&Smith + BCG + Noone&Cachia(2020) | ⚠ (en el PDF, no en la ficha) | ✗ |

**Lectura del mapa:** de 18 fuentes con contenido recuperable, **IVA** solo aparece en 3 (Purohospitality-food cost, ingenieriademenu-food cost, CESAE) y ninguna lo desarrolla como procedimiento; **delivery** no aparece desarrollado en ninguna; **inflación** solo en 1 (BCH-food cost, una frase); **prime cost / coste de personal integrado** solo se lista como epígrafe suelto en ESAH sin desarrollo. La matriz de Kasavana & Smith se nombra en 7 de las 9 fuentes de menu engineering, pero **ninguna la combina con un escandallo completo** del mismo caso (todas trabajan con datos ya calculados, no muestran el "de dónde sale ese coste").

---

## 2. Los 15 huecos del contenido gratuito (con evidencia)

1. **Tratamiento del IVA en el escandallo.** Solo 3 de 18 fuentes mencionan el IVA, y ninguna explica el procedimiento correcto: si el % de food cost se calcula sobre PVP con IVA o sobre base imponible, ni cómo tratar el tipo diferenciado (10 % hostelería / 21 % bebidas alcohólicas en sala). Ninguna de las 18 URLs desarrolla esto — es la brecha más grave, porque **cambia el resultado del % de food cost según cómo se calcule**, y ahora mismo cada fuente lo hace a su manera sin decirlo.
2. **Delivery y plataformas de terceros.** Ninguna de las 18 URLs calcula el impacto de la comisión de Glovo/Uber Eats/Just Eat (25-35 % típico) sobre el food cost efectivo de un plato vendido a domicilio. Solo Quescrem y Clab lo rozan con una mención de una frase.
3. **Beverage cost como categoría propia.** Mencionado de pasada en 4 fuentes (Quescrem, Purohospitality, CESAE, ingenieriademenu-food cost) pero ninguna da rangos objetivo de coste de bebida (que suele ser mucho más bajo que el de comida, 15-24 % frente a 28-35 %) ni distingue alcohol de bebida sin alcohol.
4. **Escandallo de pastelería/repostería.** Mencionado tangencialmente en 3 fuentes (Quescrem, elBulliFoundation, Purohospitality); ninguna trae un ejemplo numérico completo con las mermas propias del obrador (horneado, moldeado, mermas de bizcocho).
5. **Inflación y protocolo de re-escandallado.** Solo BCH-food cost la nombra, en una frase suelta ("la inflación puede incrementar o reducir el coste total"). Ninguna de las 18 URLs da un protocolo de cuándo y cómo volver a escandallar tras una subida de proveedor.
6. **Metodologías de matriz más allá de Kasavana & Smith.** El único documento que menciona alternativas (BCG, Noone & Cachia 2020) es el paper académico de academiaculinaria.org; ninguna pieza de blog/divulgación compara métodos ni menciona Miller o Pavesic.
7. **Prime cost (food cost + coste de personal) integrado.** Solo ESAH lo lista como epígrafe suelto ("costes de personal") sin desarrollarlo; ninguna de las 18 fuentes calcula el prime cost combinado con un ejemplo numérico.
8. **Mermas por técnica de cocción.** Quescrem menciona "métodos de cocción" como factor, sin cifras. Ninguna fuente trae una tabla de mermas por técnica (plancha, horno, sous-vide, fritura).
9. **Escandallo e ingeniería de menú INTEGRADOS en un solo caso.** Cada fuente trata food cost/escandallo o menu engineering por separado. Solo Purohospitality-menu engineering conecta ambos en un caso de 90 días, pero no enseña el escandallo plato a plato que sostiene esas cifras — el lector no puede replicar el cálculo.
10. **Plantilla Excel gratuita y completa con fórmulas montadas.** De 18 fuentes, solo ingenieriademenu.com ofrece plantillas, y son de pago ("premium", con "Principios de Omnes"); Purohospitality menciona una plantilla gratuita al final del artículo pero no la muestra ni la entrega en el contenido analizado.
11. **Food cost objetivo por canal de venta.** Ninguna de las 18 fuentes segmenta el % ideal por canal (sala vs. take-away vs. delivery vs. catering/eventos), pese a que el coste real por canal difiere mucho (empaque, mermas de transporte, comisiones).
12. **Menú del día vs. carta.** Ninguna fuente distingue el tratamiento del escandallo para un menú de precio fijo (donde el mix de platos determina el margen agregado) frente al escandallo plato a plato de una carta.
13. **Psicología de precios con profundidad.** Solo 2 de 18 (Purohospitality e ingenieriademenu-food cost) la desarrollan con algo de detalle (anclaje, terminación de precio, símbolos de moneda); las otras 16 no la mencionan o la citan en una frase.
14. **Reingeniería periódica / seguimiento continuo.** BCH-menu engineering apunta que "no debe entenderse como análisis puntual" pero ninguna fuente da una cadencia concreta (mensual/trimestral) ni los KPIs a vigilar entre revisiones.
15. **Casos con cifras de impacto auditables.** Solo Purohospitality trae cifras de antes/después (con euros concretos); el resto de fuentes no aporta evidencia cuantitativa de que aplicar el método funcione, lo que deja terreno abierto para una guía que sí documente su metodología de cálculo paso a paso.

---

## 3. Errores e imprecisiones repetidos que la guía puede corregir con autoridad

- **La fórmula `food cost % = (coste ingredientes ÷ precio de venta) × 100` se repite casi idéntica en BCH, Clab e ingenieriademenu (mismo ejemplo genérico 4 €/12 € = 33,3 % en dos de ellas) sin aclarar nunca si el precio de venta es con IVA o sin IVA.** Es el mismo problema que ya se identificó y corrigió en la guía gastronómica v2.0 del catálogo propio (IVA de bebida en sala al 10 %, commit `379fe79`): si una fuente calcula food cost sobre el PVP con IVA incluido y otra sobre la base imponible, los porcentajes **no son comparables entre sí**, y ninguna de las 18 URLs analizadas lo advierte. Es el hueco de mayor autoridad posible para la guía: John ya tiene el criterio verificado.
- **Rangos "ideales" de food cost citados como universales sin anclarlos al contexto español.** Purohospitality cita 28-35 % (National Restaurant Association, EE.UU.); Clab da 30-35 % (casual) / 28-32 % (fine dining) / 25-30 % (fast food) sin fuente propia visible. Ninguna fuente advierte que un rango calculado sobre el mercado americano (sin IVA al 21 % en muchos estados, con estructura de propinas distinta) no traslada limpio al mercado español.
- **Mermas ausentes en el cálculo de food cost en 15 de 18 fuentes**, cuando es precisamente el factor que explica la diferencia entre food cost teórico (el que sale de la receta) y food cost real (el que sale de caja) — Purohospitality es la única que lo nombra explícitamente como "food cost real vs. teórico", pero sin desarrollar cómo medir esa diferencia en la práctica.
- **Ninguna de las 18 fuentes distingue "precio final en carta (con IVA)" de "food cost sobre venta neta (sin IVA)".** Confundir ambos es el error silencioso más repetido de la SERP española sobre este tema, y es exactamente el terreno de dominio que ya tiene verificado el catálogo propio tras el trabajo con IVA 10 %/21 % en la guía gastronómica.
- **Contenido de referencia con 6-9 años sin actualizar sigue citándose como autoridad.** elBulliFoundation (dic-2018) e ingenieriademenu.com-menu engineering (jul-2017, sin fecha de actualización visible) siguen usando el mismo ejemplo de Kasavana & Smith de 1982 sin incorporar delivery, inflación 2022-2024 ni canales digitales — abre hueco para una guía fechada y actualizada en 2026.
- **La matriz de Kasavana & Smith se cita 7 veces como si fuera el único método válido**, cuando el propio paper académico (academiaculinaria.org) muestra que aplicar BCG o las recomendaciones de Noone & Cachia (2020) da **resultados distintos** sobre el mismo menú — ninguna fuente de divulgación lo advierte, lo que puede hacer pasar por "objetivo" un método que en realidad es una de varias convenciones posibles.

---

## 4. Guion de FAQ real (PAA + preguntas repetidas en las 18 fuentes)

**Del People Also Ask (Google, España, ya medido en el research previo):**
- ¿Qué es un escandallo de producto?
- ¿Qué es un escandallo de costes?
- ¿Qué es un escandallo en hostelería?
- ¿Cómo se calcula el escandallo de un plato?

**Repetidas de forma explícita o casi idéntica en el corpus de 18 URLs analizadas** (con la fuente donde aparece, para dar peso a cada una):
- ¿Qué es el food cost y cómo se calcula? — BCH, Clab, Purohospitality, ingenieriademenu (4/18)
- ¿Cuál es el food cost ideal? — BCH, Purohospitality, Clab (3/18, con rangos distintos entre sí — oportunidad de dar el rango correcto explicando por qué varía)
- ¿Qué es la ingeniería de menú / menu engineering? — 9 de las 9 fuentes de esa categoría
- ¿Cómo se clasifican los platos según Kasavana & Smith (estrella/vaca-caballo/puzzle/perro)? — 7/18
- ¿Cómo se calcula la merma de un ingrediente? — ESAH, Ditaly, elBulliFoundation, Quescrem (4/18)
- ¿Cómo se fija el precio de venta de un plato a partir del escandallo? — Quescrem, ComboHR, Purohospitality (3/18)
- ¿Qué diferencia hay entre food cost real y food cost teórico? — Purohospitality (único, pero es una pregunta con demanda evidente por cómo se repite el concepto de "desviación" en otras fuentes sin nombrarlo así)

**Preguntas que NINGUNA de las 18 fuentes responde bien — el hueco explícito para la FAQ de la guía propia**, con la garantía de que ahí no hay competencia gratuita ya posicionada:
- ¿Cómo afecta el IVA al cálculo del food cost y del escandallo?
- ¿Cómo se calcula el food cost real de un plato vendido por delivery, descontando la comisión de la plataforma?
- ¿Cuál es el food cost objetivo de las bebidas, y por qué es distinto al de la comida?
- ¿Con qué frecuencia hay que actualizar (re-escandallar) una receta?
- ¿Existe una plantilla Excel ya montada con las fórmulas del escandallo y la matriz de ingeniería de menú juntas?
- ¿Cómo se calcula el prime cost (food cost + coste de personal) de un restaurante?
- ¿El método de Kasavana & Smith es el único válido, o hay alternativas (BCG, Miller, Pavesic)?

---

## 5. Huecos de research no cubiertos en este documento

- **Findus, Truyol y Gosufra** quedaron fuera del mapa de cobertura por causas técnicas (timeout / sin contenido indexado en español) — no se puede afirmar ni descartar qué cubren; si se necesita cerrar el mapa al 100 % antes de escribir, requieren un reintento (posiblemente con `curl` en vez de WebFetch, o revisión manual) o darlos por perdidos con esta nota.
- **Hosteltáctil** devolvió solo el H1 sin cuerpo recuperable — probable render por JavaScript; no se puede confirmar su cobertura temática con este método.
- No se ha verificado aquí si alguna de las 18 fuentes analizadas **canibaliza** una URL propia del catálogo (los 5 posts del blog ES ya publicados sobre food cost/escandallo/ingeniería de menú, listados en el contexto de la tarea) — eso corresponde a un chequeo de posicionamiento propio vía GSC, no a esta lente de SERP externa.
