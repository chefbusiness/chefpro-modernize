# LENTE 4 — Sector, modelo de negocio, equipamiento, proveedores y casos · «Cómo Montar una Churrería-Chocolatería»

- **Producto:** guía «Cómo Montar» nº 51 (L, 65 € orientativo) · **Fecha de consulta de todo lo web:** 2026-10-03 · **Hermana:** `guia-chocolateria-obrador` (D1/D3: la taza+churros es «OTRO negocio»; esta guía la complementa).
- **Método:** WebSearch + WebFetch + `curl` con extracción de texto del HTML bruto (para re-leer cifras clave sin intermediario). INE: Excel oficial descargado y leído con `openpyxl` (read_only). MAPA: PDF de 645 págs. buscado con PyMuPDF. `istats` 49-53 °C todo el rato; sin navegador ni Playwright. Ids nuevos `CUS-*`; lo reutilizado de la hermana se cita por `CHS-*` y de la lente L1 de esta guía por `CUS-M*`/`CUS-V*`.
- **No se modificó ningún otro fichero.** Cero contenido de producto: esto es research y propuesta.

## 0. LIMITACIONES DECLARADAS (leer primero)

| # | Limitación | Efecto |
|---|---|---|
| L-1 | **WebFetch resume con un modelo pequeño.** Las cifras de fuentes que solo pasaron por él (listados de Milanuncios, hosteleria10, Churrofácil-listados) son de segunda mano; las marcadas «HTML» se re-leyeron con `curl` | Antes de publicar una cifra en copy, reabrir la URL |
| L-2 | **Milanuncios bloquea la ficha individual** tras 4-5 lecturas (captcha «Tu visita se ha interrumpido»). Solo 3 fichas se leyeron enteras; el resto son datos de la tarjeta del listado (título, m², precio, edad) | Traspasos = precio **PEDIDO**, no pagado (igual que L-9 de la hermana). Ninguna ficha dice motivo del traspaso |
| L-3 | **Idealista 403, InfoJobs 456, Indeed 403, Reddit/Forocoches no abiertos.** Salarios: ofertas de JobToday + media de Jooble, no InfoJobs/Indeed | Salarios con muestra mínima: orientativos |
| L-4 | **No hay estadística de churrerías** (ni DIRCE por epígrafe, ni panel MAPA): se dice, no se inventa | El sector se dimensiona solo por hostelería total y por proxies |
| L-5 | **Precios de equipo de hosteleria10 llevan descuentos vigentes** (−15 % a −35 %); pueden caducar. Todos «Sin IVA» según la propia página | Re-comprobar el día de publicar |
| L-6 | **Sin precio:** cafetera de 2 grupos, vitrina calefactada, mostrador, TPV, mobiliario, vajilla, extintor clase F, filtrado de aceite, azúcar, café, packaging salvo cucurucho | Marcadas «sin fuente (precio)»: NO entran en la dotación sumada |
| L-7 | IVA/IAE/CNAE, licencias, aceite polar, acrilamida, convenio: **no son de esta lente** (L3, `CUN-*`). Aquí solo se cruzan | — |
| L-8 | Las fichas de Churrofácil para chocolate en polvo, cucuruchos y rellenadora **no se abrieron una a una**: base «sin IVA» inferida de las 8 fichas del mismo sitio que sí dicen «Impuestos excluidos» | Marcado «(base inferida)» |

## 1. HALLAZGOS QUE CORRIGEN LO YA «VERIFICADO» (lo más importante)

| Id | Qué se creía | Qué dice la fuente al re-leerla | Acción |
|---|---|---|---|
| **CUS-01** | `CHS-31`: «margen bruto del churro **85-90 %**» (Loomis Pay) | **«85», «90 %» y «85-90» NO aparecen en la página** (HTML bruto, `curl`, 2026-10-03). Textual: «El margen bruto de los churros es uno de los más altos de la pastelería rápida» y «márgenes superiores al **60 %** en producto». El otro dato (El Español 21-oct-2025, dueña de La Artesana, Palma): «una rentabilidad de **un poquito más del 50 %**» | **`CHS-31` a lista negra.** Publicar «>60 % (Loomis) / ~50 % (dueña)», nunca 85-90. Avisar a la hermana (su cap. 01 y su FAQ pueden citarlo) |
| **CUS-02** | `CHS-37b` Vallecas: «beneficio neto anual demostrado» | La ficha (Milanuncios `/otros-traspasos/vallecas-c-de-villacanas-604310907.htm`, publicada 06/07/2026): **74 m², 82.000 € negociable (no 82-95.000), 910 €/mes**, «equipos valorados en **50.000 €** incluidos: freidora industrial, dosificadores inox, calientachocolates de gran capacidad, cafetera, campana homologada, refrigeración y TPV», Google 4,8 con 850+ reseñas, reparto Uber Eats/Glovo. El mismo local se anuncia duplicado como «Madrid Capital» 75 m² (agente Unionsol) | Actualizar `CHS-37b`; **82.000 € = traspaso incluye ~50.000 € de dotación declarada** |
| **CUS-03** | `CHS-12`/`CHS-57` Valor: «3 propios + 29 franquiciados» | lexpress (publicado 9-ene-2026, actualizado 30-jun-2026): **39 locales, 32 franquiciados**, inversión 125.000 € «local en bruto incl. obra, maquinaria, mobiliario, informática», canon 24.040 €, royalty 5 % | Usar 39/32 |
| **CUS-04** | `CHS-49`: churrera, freidora y extracción «sin fuente (precio)» | **Ya hay precios con base sin IVA** (§4). Quedan sin precio: vitrina, cafetera, TPV, mobiliario | Cerrar el hueco de la hermana |
| **CUS-05** | Costes de personal de Loomis Pay: «2 operarios + ayudante: **2.400-3.000 €/mes**» | Incoherente con ofertas reales (§7): 3 personas × 1.300-1.600 €/mes bruto ≈ **3.900-4.800 € sin Seguridad Social** | No usar la cifra de Loomis para el P&L |

## 2. TIPOS Y SUB-CONCEPTOS (a)-(f): qué cambia, con evidencia

| Variante | Inversión / entrada (fuente) | m² | Personal | Ticket y margen | Licencia (cruce L3) | Estacionalidad | Propuesta |
|---|---|---|---|---|---|---|---|
| **(a) Local fijo + obrador + sala** | Traspasos 16-120 k€ pedidos, mediana ~571 €/m² (§3.6); dotación declarada 50.000 € en Vallecas (`CUS-02`); Loomis (media-baja): local 30-50 m² 20-50 k€, >50 m² con terraza 50-100 k€; Qamarero: 20-50 k€ | 60-120 (traspasos); 63-187 extremos | 2-3 en turno (Antonio abre 5:45; oferta Manosanta pide 5:30 h) | Ración 2,60 € (Palma) · Loomis: ración 4 uds 2,50 €, con chocolate 3,50-4 €, ticket medio 3 € | Sala = grupo 676/673 (fuera Ley 12/2012), `CUN-10` | Pico oct-dic y Navidad (Qamarero, media-baja); valle estival: Chocolatería 1902 y Vigo Churros llevan **carta de helados** | **Caso cifrado** |
| **(b) Despacho / para llevar** | Granada: churrería pura 16.000-19.500 € (60-80 m²); Loomis kiosco fijo 30.000 € de inversión (escenario) | 60-80 | 1-2; Churrería Antonio L-D 5:45-12:30 | 6 churros 1,20 € (Granada); churro suelto 0,30 € (Vallecas) | Despacho = 644.6, **sí** en Ley 12/2012 (`CUN-09`) | Mañanas: horario partido o cierre a mediodía | **Variante** (columna de escenario) |
| **(c) Puesto / caseta / remolque** | Mini carrito 6.190 €, churrería portátil 4.190 €, **remolque 3×2×2,10 m 14.800 €** (todos sin IVA, Churrofácil); Loomis food truck 5-15 k€ (media-baja); Pinocho food truck 8 m² 58.000 € (franquicia) | 3-8 | 2-3 (Rafa: 3) | Rafa: docena 2 € (feria), factura hasta 60.000 €/año | 663.1 y 675/674.7 (`CUN-11`, `CUN-13`) | **Invertida:** Fallas Valencia 2026 = **146 puestos autorizados, 17 días (2-19 mar)**, trámite cerrado en nov-2025 | **Epígrafe + checklist de feria**; remite al food truck; no se cifra |
| **(d) Franquicia vs independiente** | Tabla L1 (`CUS-M12`…`M25`) + actualización lexpress 30-jun-2026 (§3.7) | 8 (truck) a 100+ | — | Royalty 4-6 % + 1-2 % publicidad | — | — | **Capítulo comparador** sin recomendar marca |
| **(e) Churros en cafetería existente** | Churrofácil «churrería portátil para exteriores de cafeterías» 4.190 € (dosificadora manual 2 kg + fogón gasoil 70 + escurridor); Loomis: «+1,50 € de ticket», recuperación 4-6 meses (escenario, media-baja) | 0 extra (terraza) | +0-1 | Sube ticket | Si ya tiene licencia de bar, la fritura exige extracción (L3) | Estacional | **Epígrafe + remisión** a `plan-negocio-cafeteria` |
| **(f) Obrador B2B (masa/prefrito)** | Amasadora J.L. Blanco masa blanda 20 kg de masa **6.589 €**; Inblan AM15 desde **9.425 €** (sin IVA, hosteleria10); precio de churro congelado/prefrito **sin fuente** | — | — | — | RGSEAA, 419.3 (`CUN-12`) | — | **Fuera.** Una línea de «qué cambia» |

## 3. SECTOR, DEMANDA Y MODELO DE NEGOCIO

### 3.1 Dimensión del sector (INE DIRCE, descarga oficial)

| Id | Dato | Fuente | Fiab. |
|---|---|---|---|
| **CUS-06** | **313.827 locales activos de hostelería** a 1-ene-2025, de 3.866.958 locales totales (**8,1 %**). Por CCAA: Andalucía 57.834 · Cataluña 50.783 · C. Valenciana 35.872 · Madrid 33.037 · Galicia 19.623 · Canarias 18.501 | INE, DIRCE 2025, nota de prensa 11-dic-2025 y `Anexo tablas` (Tabla 2): https://www.ine.es/prensa/anexo_tablas/es/DIRCE2025.xlsx · https://www.ine.es/dyngs/Prensa/DIRCE2025.htm (2026-10-03) | **alta** |
| **CUS-07** | **No hay estadística específica de churrerías.** El CNAE no tiene clase propia (CNAE-2025: 56.11 / 56.12 / 56.30, ver `CUN-15/16`); el DIRCE publicado solo da «Hostelería» agregada por CCAA | Mismo Excel (solo 2 tablas: tamaño×edad y CCAA×sector) | **alta (hallazgo negativo)** |
| **CUS-08** | **El panel de consumo del MAPA no desglosa churros:** 0 apariciones de «churro» y de «masas fritas» en las 645 págs. del Informe del Consumo Alimentario en España 2025 (sí desglosa «chocolates, cacaos»). La categoría cacao y chocolate movió 1.952 M€ en 2024 (+5,1 %) | https://servicio.mapama.gob.es/ca/dam/jcr:021c103a-f584-4d44-bebf-e1b44344ab11/Informe%20comsumo%202025_en%20l%C3%ADnea_.pdf (búsqueda de texto, 2026-10-03) · cifra de categoría: https://asest.es/story/liderazgo-en-chocolatea-la-taza/ | alta (negativo) / media (1.952 M€) |

> No existe «nº de churrerías en España» con fuente. Lo único cuantificable: **«churreria» 110.000 búsquedas/mes** (DataForSEO, ya medido) es consumidor, no emprendedor.

### 3.2 Tendencias (primaria = carta propia de la marca)

| Id | Tendencia | Evidencia | Fiab. |
|---|---|---|---|
| **CUS-09** | **Churro «de autor»/relleno/temático:** Maestro Churrero lista en su carta *porras, churros, sin gluten, churro bites, churros golosos (rellenos), 7 colors, churro maki, pikachurro, churro castizo, personalizados* | https://maestrochurrero.com/carta (HTML, 2026-10-03; **sin precios** en la web) | alta |
| **CUS-10** | **Sin gluten/lactosa/azúcar/vegano** como oferta de marca: Chocolatería 1902 (5.ª generación) lo declara en portada; El Moro (México) vende churros «100 % veganos» | https://chocolateria1902.com/ · https://expansion.mx/empresas/2026/08/10/churreria-el-moro-empezo-carrito-centro-cdmx-historia | alta |
| **CUS-11** | **Cobertura del valle de verano con helado:** Chocolatería 1902 publica una «Carta helados artesanales» (bola 3-5 €, batidos 4-5 €, granizados 3 €, horchata 3 €); Vigo Churros incluye «Churri-Helado (2 bolas + 4 churros + topping)», helados, cervezas y bollería (carta de mayo-2026, **precios «consultar»**) | https://chocolateria1902.com/carta/ · https://vigochurros.es/carta/ | alta (existencia) |
| **CUS-12** | **Delivery:** el anuncio de Vallecas cita Uber Eats/Glovo; la prensa del sector habla de «mantener textura y calor» como reto (sin fuente primaria leída) | `CUS-02` | media-baja |
| **CUS-13** | **Barrio frente a turismo:** Churrería Antonio (Vallecas, 1935) con colas desde primera hora; churro 0,30 €, porra 0,60 €, «rana» 2 €, **hasta 2.000 churros en días fuertes y ~40 L de chocolate al día**, abre mar-dom 5:45-12:30 | https://www.moncloa.com/2026/09/21/madrid-vallecas-churreria-3431587 (HTML, 21-sep-2026; medio local, sin cifras verificables por otra vía) | media-baja |
| **CUS-14** | **Franquicia en expansión de formato corto:** Pinocho Churros Gourmet 10 locales, formato food truck 8 m²; «150 franquicias en 5 años» es **objetivo** del franquiciador, no dato | https://lexpress-franchise.com/es/articulos/como-abrir-una-churreria-top-10-de-marcas-en-espana/ (act. 30-jun-2026) | media |

### 3.3 Precios de venta publicados (reales, con URL)

| Id | Establecimiento | Precios | Fuente y fecha | Fiab. |
|---|---|---|---|---|
| **CUS-15** | La Churrería, Pl. Pescadería 17 (Granada) | **Ración 6 churros 1,20 €** · chocolate a la taza **2,00 € barra / 2,50 € terraza** · café 1,20 / 2,00 € · menú desayuno (café + zumo + churros) 3,50 € · horario L-S 9-21, D 9-14 | https://www.lachurreriadegranada.es/carta-precios.html (HTML, 2026-10-03) | **alta** (carta propia) |
| **CUS-16** | Churrería Antonio (Vallecas) | churro suelto 0,30 € · porra 0,60 € · rana 2 € | Moncloa 21-sep-2026 (`CUS-13`) | media-baja |
| **CUS-17** | La Artesana (Palma de Mallorca, 21 años) | **ración 2,60 €**, media 1,40 € | El Español, 21-oct-2025: https://www.elespanol.com/sociedad/20251021/dueno-negocio-churros-anos-historia-vendemos-raciones-dia-rentabilidad/1003743974262_0.html | media |
| **CUS-18** | Rafa, ferias de Galicia | **docena 2 €** (el mismo texto repite «12 euros la docena»: errata, contradice el titular) | El Español, 5-mar-2026: https://www.elespanol.com/sociedad/20260305/rafa-dueno-churreria-espana-empleados-euros-docena-facturamos-ano/1003744124203_0.html | media-baja |
| **CUS-19** | Chocolatería 1902 (Madrid centro) | «7 porras y 4 chocolates por **21 €**, ~5 € por persona» | El Español, 22-dic-2024: https://elespanol.com/madrid/ocio/20241221/adios-colas-san-gines-cafeteria-centenaria-madrid-mejores-churros-chocolate-receta-secreta/909409302_0.html | media (único dato de turístico) |
| **CUS-20** | Loomis Pay (genérico) | pieza 0,30-0,70 € · ración 4 uds 2,50 € · con chocolate 3,50-4 € · ticket medio 3 € (= `CHS-32`, **verificado en HTML**) | https://es.loomispay.com/blog/rentabilidad-churreria-2025 (7-ago-2025) | media-baja |

**Brecha de precio que la guía debe mostrar:** ración 1,20 € (Granada, 2026) · 2,60 € (Palma, 2025) · ~5 € por persona con chocolate (centro de Madrid, 2024). La carta de San Ginés y Maestro Churrero **no publica precios en su web**; el «4,90 € chocolate + 6 churros» de San Ginés viene de un agregador turístico sin carta → lista negra.

### 3.4 Coste de materia prima (precios ACTUALES, todos **sin IVA**, Churrofácil, 2026-10-03)

| Id | Insumo | Precio | Base y rendimiento declarado | Derivado (mío) |
|---|---|---|---|---|
| **CUS-21** | Mix churro de lazo/relleno, caja 6 sacos × 4 kg | **34,80 €** | «Impuestos excluidos»; «cada saco 4 kg → ~11,5 kg de masa» (HTML ficha) | 1,45 €/kg de mix · **~0,50 €/kg de masa** |
| **CUS-22** | Mix para porras, 3 sacos × 4 kg · 3 × 8 kg · saco 20 kg «Porra madrileña Tahona» | 16,20 € · 30,75 € · **19,50 €** | listado (base inferida) | 1,35 · 1,28 · **0,98 €/kg** |
| **CUS-23** | Aceite girasol alto rendimiento 25 L · aceite fritura Gold 25 L | **49,00 € · 49,90 €** | «Impuestos excluidos» (HTML ficha) | **1,96 · 2,00 €/L** |
| **CUS-24** | Chocolate a la taza en polvo 1,3 kg · 800 g · cobertura negra/blanca 1 kg | 8,20 € · 5,75 € · 6,50 € | listado (base inferida) | 6,31 · 7,19 · 6,50 €/kg |
| **CUS-25** | Cucurucho cartón para churros, caja 100 · vaso PP 200 cc ×100 · azúcar glas 800 g | 15,00 € · 1,99 € · 3,10 € | listado (base inferida) | 0,15 €/cucurucho |
| Fuente común | https://www.churrofacil.com/tienda/es/30-accesorios-y-consumibles · fichas `/accesorios-y-consumibles/13-…`, `/90-…`, `/aceites/82-…` | | | |

- **Absorción de aceite, vida del aceite y peso de la ración: «sin fuente».** El único dato de grasa hallado (23,7-35,2 g/100 g) es de churros **de maíz** de un estudio ecuatoriano: no aplica a masa de trigo. Las promesas del proveedor («absorbe un 30 % menos», «dura el doble», Sol Gold) son **marketing** → lista negra.
- **Materia prima + aceite ≈ 20 % de la facturación** (Loomis, = `CHS-33`, verificado HTML). Sin fuente independiente.
- ⚠️ **Precio unitario del mix por verificar al pedir:** 1,45 €/kg es coherente con el resto de mezclas (0,98-1,35 €/kg), pero la ficha dice «Mix Churros de Lazo 4 kg **Caja 6 Sacos**» en un slug de «pack de 3 cajas».

### 3.5 Productividad, estacionalidad y punto de equilibrio

| Id | Dato | Fuente | Fiab. |
|---|---|---|---|
| **CUS-26** | **Capacidades de equipo (no productividad real):** dosificadora automática CH 5 kg de masa, Inhospan automática 3,5 kg, JL Blanco manual 2-5 L; el «hasta 150 g/s = 540 kg/h» del M-2020 es el **máximo del fabricante** → NO usar como churros/hora. **Productividad en churros/hora: «sin fuente»** | hosteleria10 (fichas) | alta (capacidad) / sin fuente (ritmo) |
| **CUS-27** | Volumen real de un puesto: La Artesana **200-300 raciones L-V y ~400 en fin de semana**; Loomis (escenario) 150 raciones/día ≈ 600 €; Antonio hasta 2.000 churros/día | El Español 21-oct-2025 · Loomis · Moncloa | media / media-baja |
| **CUS-28** | **Punto de equilibrio (escenario):** 1.600 raciones/mes (≈55/día) con costes fijos de 800-1.500 € de alquiler + 600 € de suministros/gestión/seguros + personal; **el personal de Loomis es incoherente (`CUS-05`)** → usar solo como método | Loomis | **baja** |
| **CUS-29** | **Estacionalidad con cifras: solo cualitativa** (pico oct-dic, Navidad, fiestas locales: Qamarero 8-jul-2025). Dato duro de temporada corta: **Fallas Valencia 2026, 146 puestos, 17 días (2-19 mar), 11 días menos que 2025** | https://qamarero.com/blog/cuanto-dinero-se-gana-con-una-churreria-es-rentable/ · https://www.elespanol.com/valencia/oci/20260226/confirmado-churrerias-autorizadas-fallas-abriran-partir-dia-calles-valencia-trt/1003744145016_0.html | media-baja / media-alta |
| **CUS-30** | **Margen:** «>60 % en producto» (Loomis, HTML) y «un poco más del 50 %» (dueña de La Artesana). Los dos difieren por definición (materia prima frente a margen tras costes): la guía debe decirlo | Loomis · El Español | media-baja |

### 3.6 Anuncios de TRASPASO (consultados 2026-10-03, Milanuncios; precio PEDIDO)

Los 3 de la hermana (`CHS-37a` Elche 75 m², `CHS-37b` Vallecas 74 m², `CHS-37c` Mataró 118 m² 58.000 €) siguen vigentes; `CHS-37b` se amplía en `CUS-02`. **Nuevos (9):**

| Id | Negocio (título) | Ciudad | m² | Traspaso | Alquiler | €/m² | Edad del anuncio | Lectura |
|---|---|---|---|---|---|---|---|---|
| **CUS-31a** | «Churrería, bocadillería, patatas asadas y kebab» | Granada capital | 80 | **19.500 €** | n/d | 244 | 10 h | Churrería de barrio con carta mixta |
| **CUS-31b** | «Churrería y patatas asadas **por jubilación**» | Granada, Zaidín (Av. Dílar) | 60 | **16.000 €** | n/d | 267 | 43 días | Único con motivo declarado (jubilación) |
| **CUS-31c** | «Se traspasa cafetería-churrería en pleno funcionamiento» | Granada, centro | 70 | 40.000 € | n/d | 571 | 179 días | 6 meses sin vender: el precio pedido no se cierra |
| **CUS-31d** | «Cafetería, Churrería» | Granada, Genil | 70 | 40.000 € | n/d | 571 | 116 días | Ídem |
| **CUS-31e** | «Heladería y churrería» | Montefrío (Granada) | 105 | 65.000 € | n/d | 619 | 110 días | Modelo helado + churro (valle de verano resuelto) |
| **CUS-31f** | «Traspaso heladería churrería» | Ibiza | 120 | 60.000 € | n/d | 500 | 21 días | Idem; turismo |
| **CUS-31g** | «Cafetería churrería en centro» (3 anuncios del mismo local) | Valdemoro (Madrid) | 240 | 65.000 € | **1.500-1.550 €** | 271 | 30-40 días | Local grande, alquiler alto |
| **CUS-31h** | «Bar cafetería churrería, licencia C2» (ficha abierta: terraza 5 mesas, amasadora, churrera industrial, TPV) | Sant Joan Despí (Barcelona) | 63 | **107.000 €** | 645 € + IVA | 1.698 | **>2 años, reeditado «ayer»** | Precio inflado o stale |
| **CUS-31i** | «Bar-restaurante C3: cafetería, churrería y restaurante» (ficha abierta: campana, amasadora, churrera, horno, contrato 10 años) | Santa Coloma de Cervelló (Barcelona) | 187 | 120.000 € | 1.800 € + IVA | 642 | **>2 años, reeditado «ayer»** | Ídem |

**Lectura:** 11 anuncios con m² y precio (incluidos `CHS-37b/c`): **mediana ~571 €/m²**, rango 244-1.698. **Churrería pura de barrio: 16-19,5 k€; con cafetería, 40-65 k€; con sala y terraza en área metropolitana, 82-120 k€.** Cuatro anuncios llevan 110-179 días: el precio pedido ≠ precio de cierre. Además aparecen en el listado de Barcelona (Barberà del Vallès 70 m² 85.000 €, Molins de Rei 40 m² 42.900 € con alquiler 775 € + IVA, Sant Vicenç dels Horts 40 m² 38.000 €) y de Valencia (Algirós 119 m² 89.900 €, alquiler 1.300 €; El Carmen 80 m² «1.400 €», probable error): **títulos sin «churrería» legible y fichas bloqueadas → NO entran.**
Fuentes (listados): https://www.milanuncios.com/traspasos-en-granada/churreria.htm · https://www.milanuncios.com/traspasos-en-madrid/churreria.htm · https://www.milanuncios.com/traspasos-en-barcelona/churreria.htm · https://www.milanuncios.com/traspasos-en-valencia/churreria.htm · fichas `/otros-traspasos/sant-joan-despi-510792997.htm`, `/otros-traspasos/santa-coloma-de-cervello-510790960.htm`. Fiabilidad **media** (pedido, sin cierre, sin motivo).

### 3.7 Inversión publicada (franquiciadores) — actualización sobre L1

lexpress (9-ene-2026, act. 30-jun-2026): **Maestro Churrero desde 115.000 €**, canon 15.000 €, royalty 5 % + 1 % · **Valor 125.000 €** (39 locales, 32 franq.) · **Madrid1883 ~96.000 €**, canon ~20.000 €, 4 % + 2 %, 3 locales · **Churros Factory 45.000 €**, canon 12.000 €, 6 %, 10 años renovable · **Pinocho 58.000 €**, 8 m² (food truck), 10 locales. ⚠️ Un buscador dio «Maestro Churrero desde **75.000 €**, 40 m² mínimos, contrato 5 años» (resumen sin abrir) frente a los 115.000 € de lexpress y los 100 m² de L1: **discrepancia sin resolver → lista negra hasta abrir la web del franquiciador.** URL: https://lexpress-franchise.com/es/articulos/como-abrir-una-churreria-top-10-de-marcas-en-espana/ · fiabilidad media (declarado por la enseña vía agregador).

## 4. EQUIPAMIENTO CRÍTICO CON MARCAS Y PRECIOS

**Base de todo lo de esta sección: SIN IVA** (declarada en la propia ficha: hosteleria10 «Precios Sin IVA» + Churrofácil «Impuestos excluidos», verificado en HTML). Consulta 2026-10-03. `hosteleria10 = https://hosteleria10.com/negocios/churreria/<slug>` y `/cocina/churreras/<slug>`.

| Id | Equipo | Marca/modelo | Precio sin IVA | Notas | Fiab. |
|---|---|---|---|---|---|
| **CUS-32a** | **Equipo completo de churros** (dosificadora 1,5 kg + caldero 14 L) | Mundigas CH-1-D | **2.188,00 €** (antes 2.735 €) | `…/mundigas-equipo-churros-ch-1-d.html` | media-alta |
| CUS-32b | Ídem | Repagas | 2.198,00 € (antes 2.748 €) | `…/repagas-equipo-completo-churrera.html` | media-alta |
| CUS-32c | Ídem 4,5 kg | Mundigas CH-6 | 2.935,00 € | `…/mundigas-equipo-churros-ch-6.html` | media-alta |
| **CUS-33a** | **Freidora de churros gas 25 L** (mostrador) | ClimaHosteleria EMPLK002 | **1.907,00 €** (−35 %) | `…/ch-freidora-churros-emplk002.html` | media |
| CUS-33b | Ídem eléctrica 25 L | ClimaHosteleria EMPLK003 | 2.053,00 € (= 2.484 € con IVA, comprobado) | `…/ch-freidora-churros-emplk003.html` | media-alta |
| CUS-33c | Fogón-freidora gas profesional 14-22 L | Inhospan FG | desde 2.560,00 € | `/cocina/churreras/inhospan-freidora-fogon-profesional-fg.html` | media |
| CUS-33d | Fogón-freidora automático gas 14-38 L | Inhospan FGAUT | 3.933,00 € | | media |
| CUS-33e | Freidora gas CG80, 32 L · eléctrica CE80, 32 L | NTGAS | 4.422,00 € (−20 %) · 4.522,00 € (−20 %) | **No** usar el «4.228 €» que dio un buscador | media |
| CUS-33f | Freidora gas CG-80 30 L · FG-3010 37 L | J.L. Blanco | 6.050,00 € · desde 8.690,00 € | techo del mercado | media |
| CUS-33g | **Fogón 80×80 gas natural, 22 L** (HTML ficha: «Impuestos excluidos»; termómetro digital, ±5 °) | Churrofácil | **2.890,00 €** | `/gas-natural/152-…`; 70×70 gas natural 2.790 € | **alta** |
| **CUS-34a** | **Dosificadora manual 2 kg** (HTML: excluidos) | HG e Hijos (Churrofácil) | **795,00 €** | con cortador 945 €; Inhospan de jeringa 2 kg 365,80 € | alta |
| CUS-34b | **Dosificadora automática con variador y pedal 25 kg** (HTML: excluidos) | Churrofácil | **2.250,00 €** | | alta |
| CUS-34c | Dosificadora automática 5 kg | CH (ClimaHosteleria) | **1.798,00 €** (−35 %) | `…/ch-dosificador-automatico-churros.html`; catálogo 2024: 2.685 € (otra referencia) | media |
| CUS-34d | Churrera semiautomática 2 L · automática 2 L · 3 L | J.L. Blanco M-1015 · M-1018 · M-2005 | 4.609 € · 6.919 € · 9.779 € | automatización cara | media |
| **CUS-35a** | **Amasadora automática con rascador** (HTML: excluidos) | Churrofácil | **2.550,00 €** | alternativa artesanal: caldero amasador Inhospan CALD50 247,00 € + pala de amasar inox/PE desde 39,00 € | alta |
| CUS-35b | Amasadora masa blanda 20 kg de masa · multiuso AM15 | J.L. Blanco · Inblan | 6.589 € · desde 9.425 € | solo para (f) | media |
| **CUS-36a** | **Campana extractora 1200 con turbina, filtros y potenciómetro** (HTML: excluidos) | Churrofácil | **990,00 €** | 1500: 1.020 € (listado) | alta |
| CUS-36b | Conducto, salida de humos, obra, proyecto de ventilación | — | **sin fuente (precio)** | lo que exige la licencia con fritura (L3) | — |
| **CUS-37a** | **Chocolatera 5 L** | Irimar MCH-5 | **412,70 €** (−23 %) | `…/irimar-chocolatera-mch-5.html`; Ugolini Delice 3 = 496 € (≠ 527 € de `CHS-46a`: otro descuento) | media |
| CUS-37b | Chocolatera 5 L · 5 L · 7 L | Mes Fred Choco 5 · Campeona TXM 5-LB · TXM 7-LC | 447,20 € · 833 € · 1.301 € | rango 412-1.301 € | media |
| CUS-37c | Chocolatera vintage baño maría **10 L** (HTML: excluidos) · Chocofairy 5 L | Churrofácil | **845,00 €** · 495,00 € | | alta / media |
| **CUS-38** | **Medidor de compuestos polares Testo 270 BT** | Testo | **499,00 €** (= 603,79 € con IVA, comprobado) | https://www.infoagro.com/instrumentos_medida/medidor_imprimir.asp?id=7558 | alta |
| CUS-39 | Escurridor inox ESCL · ESCP · bandeja Inblan 50×60 | Inhospan · Inhospan · Inblan | desde 260 € · desde 416 € · 499,20 € | | media |
| CUS-40 | Rellenadora de churros · pack 2 | Churrofácil | 330,00 € · 520,00 € (base inferida) | JL Blanco rellenadora manual desde 935 € | media-baja |
| CUS-41 | Balanza 6 kg | Baxtran PD LCD | 48,75 € | | media |
| **CUS-42** | **Remolque 3×2×2,10 m con cartel** · mini carrito eventos/mercados · churrería portátil exteriores cafeterías | Churrofácil | **14.800 €** · **6.190 €** · **4.190 €** | https://www.churrofacil.com/tienda/es/33-remolques | alta (carrito, portátil: HTML) |
| CUS-43 | Cafetera 2 grupos, vitrina calefactada, mostrador, TPV, mesas y sillas, vajilla/tazas, extintor clase F, sistema de filtrado de aceite, lavavajillas | — | **sin fuente (precio)** | (Ristoattrezzature ofrece filtración móvil de aceite; sin precio) | — |

### 4.1 Dotación TIPO (todo SIN IVA; solo líneas con precio verificado; **NO es presupuesto de apertura**)

| Línea | A · Despacho pequeño (25-40 m², caldero 14 L, para llevar) | B · Local 60-80 m² con obrador de masa a la vista y sala |
|---|---|---|
| Fritura + dosificación | Equipo completo Mundigas CH-1-D **2.188,00** (CUS-32a) | Freidora gas EMPLK002 **1.907,00** (CUS-33a) + dosificadora automática CH 5 kg **1.798,00** (CUS-34c) |
| Amasado | Caldero amasador CALD50 **247,00** + pala amasar **39,00** (CUS-35a) | Amasadora automática **2.550,00** (CUS-35a) |
| Extracción | Campana 1200 **990,00** (CUS-36a) | Campana 1200 **990,00** (CUS-36a) |
| Chocolate | 1 × Irimar MCH-5 **412,70** | 2 × Irimar MCH-5 **825,40** |
| Escurrido | Escurridor ESCL desde **260,00** | Escurridor bandeja Inblan **499,20** |
| Pesaje | Balanza **48,75** | Balanza **48,75** |
| **Subtotal núcleo (con balanza)** | **4.185,45 €** (CUS-58) | **8.618,35 €** (CUS-59) |
| Opcionales con precio | Testo 270 BT 499,00 + rellenadora 330,00 = **829,00** | Testo 270 BT **499,00** + rellenadora **330,00** = **829,00** |
| **Total con opcionales** | **5.014,45 €** | **9.447,35 €** |
| Líneas SIN fuente (no suman) | cafetera, vitrina, mostrador, TPV, mobiliario, vajilla, extintor F, obra de humos | las mismas + sala y terraza |

> Suma B: 1.907,00 + 1.798,00 + 2.550,00 + 990,00 + 825,40 + 499,20 + 48,75 (balanza) = **8.618,35 €**; con Testo 499,00 y rellenadora 330,00 = **9.447,35 €**. Suma A: 2.188,00 + 247,00 + 39,00 + 990,00 + 412,70 + 260,00 + 48,75 = **4.185,45 €**; con opcionales = **5.014,45 €**.
> **Referencias cruzadas:** Qamarero cita «~10.000 € de maquinaria (freidoras, amasadoras)» sin fuente (media-baja): coincide con B. El traspaso de Vallecas declara **50.000 €** de dotación completa incluidos (`CUS-02`): la diferencia (≈40.000 €) es todo lo que **no** está en esta tabla (obra, campana homologada con conducto, refrigeración, TPV, mobiliario, cafetera).
> **Un solo concepto, una sola base:** todas las líneas son sin IVA. Los 603,79 € del Testo y los 2.484 € de la EMPLK003 están **con** IVA y no se usan.

## 5. PROVEEDORES REALES (solo nombres con URL abierta)

| Id | Tipo | Proveedor | Qué vende | URL | Verificado |
|---|---|---|---|---|---|
| **CUS-44a** | Harina/mix + maquinaria + consumibles + remolques | **Churrofácil CB** (Linares, Jaén; «+30 años») | Mix de churros y porras, aceite, chocolate en polvo, cucuruchos, churreras, amasadoras, remolques; «adiestramiento gratuito» con la maquinaria (declarado por el directorio) | https://www.churrofacil.com/ | **sí** (precios en HTML) |
| CUS-44b | Harina especial churros | **Harinas Sánchez Palencia** (Jerez/La Palma del Condado; desde 1936) | «Harina Especial Churros», sacos 10-50 kg | https://www.harinassp.es/ | **sí** (home con «harina especial para churros»; sin precio) |
| CUS-44c | Harina | **HARIMSA** (Cartagena; desde 1896) | «Harina para churros» según el directorio (sacos 25/40 kg); su home no la nombra | https://www.harimsa.es/ · https://proveedores.com/proveedores/harimsa/ | parcial (200 OK; producto solo en directorio) |
| CUS-44d | Harina | Harinas Costas (Sevilla) · Harinera de Tardienta (Aragón, 1954) | harina para churros / «harina churrera» | https://proveedores.com/proveedores/harinas-costas/ · https://proveedores.com/proveedores/harinera-de-tardienta/ | **solo directorio** (web propia no abierta) |
| CUS-44e | Maquinaria (fabricante) | **Inblan** · **J.L. Blanco** · **Inhospan** · **Mundigas** · **Repagas** · **NTGAS** | churreras, fogones-freidora, amasadoras | https://www.inblan.com/maquinaria-para-churreria/ · distribuidor con precio: https://hosteleria10.com/negocios/churreria/ | sí (Inblan sin precios; resto con precio en hosteleria10) |
| CUS-44f | Distribuidor | **HostelShop España** (tel. 910 549 798) | categoría churrerías (churreras, freidoras, amasadoras, chocolateras); **sin precios en la página** | https://hostelshopespana.com/maquinaria-de-hosteleria-para-churrerias/ | sí, sin precio |
| CUS-44g | Chocolate a la taza | **Chocolates Valor** (Villajoyosa) · **Simón Coll** | Valor: polvo y tableta a la taza (la cuota «≈50 %» es de resumen no leído → no usar); Simón Coll lanzó «Ritual» 100 % haba de cacao | https://asest.es/story/liderazgo-en-chocolatea-la-taza/ | sí (existencia); **formato y precio profesional: sin fuente** |
| CUS-44h | Gestor de aceite usado | **Reseave** (Mejorada del Campo, Madrid): gestor autorizado, certificado de eliminación, «servicios gratuitos o valoración económica» a hostelería, retirada en 24 h | https://www.reseave.es/ | **sí** (HTML) |
| CUS-44i | Listado de gestores | FEHR + Geregras elaboraron un listado de gestores de grasas de cocina (nota de 2015, **sin leer el listado**) | https://www.energias-renovables.com/articulo/gestores-de-aceites-usados-y-el-magrama-20141219 | fecha antigua: reconfirmar en F2 |
| CUS-44j | Packaging para llevar | Cucurucho de cartón y vasos PP: Churrofácil (`CUS-25`) | | | sí |
| — | Azúcar, café | **sin fuente** (no verificado ningún proveedor con web abierta) | | | — |

## 6. CASOS DE REFERENCIA (con la lección)

| Id | Caso | Modelo | Dato público | Fuente | Lección |
|---|---|---|---|---|---|
| **CUS-45** | **Chocolatería San Ginés** (Madrid, 1894) | Taza + churros, 24 h, 365 días, anexando locales; prepago en caja (`CHS-67`) | Fuera de España: Cais do Sodré (Lisboa, verano 2024, ~40 plazas + azotea), kiosco take-away en El Corte Inglés Lisboa (6-ene-2025), Austin, Miami Beach, Buenos Aires y Filipinas (2026); **Marbella** en España. **Los 3 locales de CDMX, cerrados en 2025** (Wikipedia, con «better source needed»). **Sin cifras de facturación** | https://echoboomer.pt/?p=287588 (15-feb-2026) · https://en.wikipedia.org/wiki/Chocolater%C3%ADa_San_Gin%C3%A9s | La marca madrileña se exporta en **kiosco y local pequeño**; la expansión a México no aguantó. Cautela con «LATAM» |
| **CUS-46** | **Chocolatería 1902 / Los Artesanos 1902** (Madrid) | 5.ª generación, **fábrica de chocolate propia**, 2 puntos (C/ San Martín 2 y Bernabéu Market) | Horario 7-23 h (prensa dic-2024); sin gluten/lactosa/azúcar/vegano; carta de helados | https://chocolateria1902.com/ · https://chocolateria1902.com/chocolateria-carta (selector de local) | Integrar chocolate propio y **diversificar el verano** |
| **CUS-47** | **Maestro Churrero** (Madrid, desde 1902 según la marca) | **2 locales** (Pza. Jacinto Benavente 2 · Carrera de San Jerónimo 9) y franquicia | Carta de producto «de autor» (`CUS-09`); inversión de franquicia: discrepancia (`§3.7`) | https://maestrochurrero.com/carta | Innovar el churro como palanca de ticket y de redes |
| **CUS-48** | **Churrería Antonio** (Vallecas, 1935) | Despacho + barra pequeña, mar-dom 5:45-12:30 | Hasta 2.000 churros/día, ~40 L de chocolate, churro 0,30 € | Moncloa 21-sep-2026 | Volumen con precio bajo y horario de madrugada (nocturnidad/madrugada: L3) |
| **CUS-49** | **La Artesana** (Palma de Mallorca, 21 años) | Familiar, 3 personas, dosificadora | 200-300 raciones/día entre semana, ~400 en finde; ración 2,60 €; **maquinaria inicial ≈ 3.000 €** | El Español 21-oct-2025 | Una máquina barata basta: la inversión está en el local |
| **CUS-50** | **Rafa** (ferias de Galicia, 15 años) | Puesto ambulante hasta 7 m; fijos de invierno en Noia, Boiro y Padrón | Docena 2 €; 3 empleados; «facturamos 60.000 €/año» | El Español 5-mar-2026 | Variante (c): facturación acotada y sin cola de dueño no escala |
| **CUS-51** | **Chocolates Valor** | Industrial + 39 chocolaterías (32 franq.) | >220 M€ en 2025 (`CHS-57`); franquicia 125 k€ | lexpress act. 30-jun-2026 | Techo del modelo integrado |
| **CUS-52** | **Churrería El Moro** (CDMX, carrito 1933, local 1935) | 24 h, receta sin cambios, churros veganos | EE. UU.: Costa Mesa 2023, Echo Park (LA) 2026, con Northgate Market; **sin facturación pública** | https://expansion.mx/empresas/2026/08/10/churreria-el-moro-empezo-carrito-centro-cdmx-historia (10-ago-2026) | Para el lector LATAM/EE. UU.: la marca crece por socio de distribución, no por franquicia |
| **CUS-53** | **Churrería Porfirio** (México) | 180-188 locales; 16 M USD (Cronista) vs 13,5 M USD (L1) — **discrepan** | L1 `CUS-M25` | | Citar el rango, no un número |

## 7. SALARIOS Y PERSONAL (ofertas reales, octubre de 2026)

| Id | Puesto | Cifra | Fuente | Fiab. |
|---|---|---|---|---|
| **CUS-54** | Aprendiz de churrero, Valdemoro (MONTEBARI S.L., jornada completa, hace 1 mes) | **1.300-1.500 €/mes** (bruto según el portal) | https://jobtoday.com/es/trabajos-churrero-en (2026-10-03) | media-baja |
| **CUS-55** | Ayudante de cocina, Churrería Manosanta (San Blas-Canillejas, Madrid; **3 años de experiencia, entrada a las 5:30**) | **1.500-1.600 €/mes** | Ídem | media-baja |
| **CUS-56** | Media de «churrero» en España: **1.343 €/mes · 16.116 €/año · 9,59 €/h**; «camarero churrero» 1.500 €; «churrero con experiencia» 1.200 € | Jooble, 37 salarios, 29-jul-2026 (el «7.306 vacantes» de la página no es creíble) | https://es.jooble.org/salary/churrero | **baja** |
| **CUS-57** | Churrero por jornada: ofertas de Indeed/Milanuncios/Jobsora en Madrid sin salario visible («a convenir», salarios tras clic) | https://www.milanuncios.com/ofertas-de-empleo/churrero-madrid.htm · https://es.jobsora.com/empleos-churrero | sin fuente (salario) |

**Personal por modelo (lo que se puede sostener):** (a) 2-3 personas en turno de mañana y tarde (Manosanta y Antonio: entrada 5:30-5:45 → **madrugada y nocturnidad a verificar en L3**); (b) 1-2; (c) 2-3 (Rafa: 3 con un solo dueño); (e) +0-1. **Salario de convenio: `L3` (no esta lente).** Dato duro para el P&L: **1.300-1.600 €/mes bruto por persona (2 ofertas) → 3 personas = 3.900-4.800 €/mes sin Seguridad Social**, el doble que la cifra de Loomis (`CUS-05`).

## 8. CIERRE

### 8.1 Cifras que ENTRAN (CUS-*)

| Cifra | Valor | Id | Fiab. |
|---|---|---|---|
| Locales de hostelería (DIRCE 1-1-2025) | 313.827 (8,1 % del total) | CUS-06 | **alta** |
| Fallas 2026: puestos de churros / días | 146 / 17 | CUS-29 | media-alta |
| Ración 6 churros / chocolate a la taza (barra) en Granada | 1,20 € / 2,00 € | CUS-15 | **alta** |
| Ración en Palma / docena en feria | 2,60 € / 2,00 € | CUS-17/18 | media / media-baja |
| Mix de churros (sin IVA) y masa resultante | 1,45 €/kg · ~0,50 €/kg de masa | CUS-21 | alta (precio) / media (rendimiento del vendedor) |
| Aceite 25 L (sin IVA) | 49,00-49,90 € (≈2 €/L) | CUS-23 | **alta** |
| Fogón gas 80×80 22 L · dosificadora automática 25 kg · amasadora · campana 1200 · chocolatera 10 L (todo sin IVA) | 2.890 · 2.250 · 2.550 · 990 · 845 € | CUS-33g/34b/35a/36a/37c | **alta** |
| Equipo completo de churros (dosificadora + caldero) | 2.188-2.935 € | CUS-32 | media-alta |
| Remolque 3×2 m · mini carrito · portátil para cafeterías | 14.800 · 6.190 · 4.190 € | CUS-42 | alta |
| Testo 270 BT | 499 € (603,79 € con IVA) | CUS-38 | alta |
| Dotación tipo A / B (solo líneas con fuente, sin IVA) | 4.185 € núcleo (5.014 con opcionales) / 8.618 € núcleo (9.447 con opcionales) | CUS-58/59 (§4.1) | media (suma de fichas con descuento) |
| Traspasos nuevos: 9 anuncios, mediana ~571 €/m² | churrería pura 16-19,5 k€ · con cafetería 40-65 k€ · con sala 82-120 k€ | CUS-31 | media (pedido) |
| Vallecas: 74 m², 82.000 €, 910 €/mes, 50.000 € de equipos incluidos | | CUS-02 | media-alta |
| Franquicias: Valor 125 k€ (39 locales/32 franq.) · Madrid1883 ~96 k€ · Churros Factory 45 k€ | | CUS-03 / §3.7 | media |
| Salario churrero: 1.300-1.600 €/mes bruto en 2 ofertas | | CUS-54/55 | media-baja |
| Churrería de barrio: hasta 2.000 churros/día y ~40 L de chocolate | | CUS-13 | media-baja |

### 8.2 LISTA NEGRA (circulan sin fuente primaria o contradicha)

1. **`CHS-31` «margen bruto 85-90 %»**: no aparece en la página que se cita (`CUS-01`).
2. **«Beneficio 40.000-60.000 €/año»** (Qamarero, copiado en el texto de El Español sobre Rafa): circular, sin método.
3. **Casos de Loomis** (food truck 9.800 €/mes de beneficio, kiosco 7.200 €): son escenarios del artículo, no negocios reales.
4. **Costes de personal de Loomis** 2.400-3.000 € para 3 personas (`CUS-05`).
5. **«El aceite absorbe un 30 % menos / dura el doble»** (ficha comercial del proveedor).
6. **540 kg/h** (150 g/s) del M-2020: máximo del fabricante, no ritmo real.
7. **Maestro Churrero «desde 75.000 €, 40 m²»** frente a 115.000 € y 100 m²: discrepancia (`§3.7`).
8. **Valor «≈50 % de cuota en chocolate a la taza»**: resumen de buscador no abierto.
9. **San Ginés «4,90 € chocolate con 6 churros»**: agregador turístico sin carta.
10. **NTGAS CG80 «4.228 €»**: lo dio un buscador; la página dice 4.422 € (−20 %).
11. **Grasa de los churros 23,7-35,2 g/100 g**: estudio de churros **de maíz** de Ecuador.
12. **Traspasos de >2 años reeditados** (Sant Joan Despí 107.000 €, Santa Coloma 120.000 €): precios pedidos sin cierre.
13. **«12 euros la docena»** (typo en el artículo de Rafa): contradice el titular de 2 €.
14. **Porfirio 16 M USD / 13,5 M USD**: dos cifras para el mismo año.
15. **Jooble «7.306 vacantes»**: incoherente con una muestra de 37 salarios.

### 8.3 Las 5 cifras clave para la portada

| Cifra | Valor | Fuente | Fiab. |
|---|---|---|---|
| **Inversión tipo** | Traspaso de un local pequeño **16.000-120.000 €** (mediana ~571 €/m²); dotación de maquinaria **~4.200-9.450 € sin IVA** (equipo completo desde 2.188 €) | CUS-31, §4.1 | media |
| **m²** | **60-120 m²** (traspasos reales); puesto de feria 3-8 m² | CUS-31, `CHS-37` | media |
| **Personal** | **2-3 personas**, entrada 5:30-5:45; **1.300-1.600 €/mes bruto cada una** | CUS-54/55, CUS-13 | media-baja |
| **Ticket** | **ración 1,20-2,60 €; con chocolate ~3,50-5 €** (Granada 2026 / Palma 2025 / Madrid 2024) | CUS-15/17/19, `CHS-32` | media |
| **Break-even** | **sin cifra defendible** (el escenario de Loomis, ≈55 raciones/día, usa un coste de personal incoherente): la guía lo ofrece como **calculadora con parámetros del lector**, no como número | CUS-28 | baja |

### 8.4 Decisiones que esta lente deja planteadas

1. **Avisar a la hermana:** `CHS-31` (85-90 %) está contradicho; su cap. 01 / FAQ / landing podrían citarlo. Recomendación: parche de una frase antes de la venta cruzada.
2. **Caso central = (a) local fijo con sala**, con (b) y (c) como columnas de escenario; (e) y (f) en una línea cada una. La evidencia de (d) (14 enseñas) justifica un capítulo comparador, no una recomendación.
3. **Dotación = «núcleo con fuente» (A/B) + tabla de huecos** para que el lector complete con cotizaciones locales (cafetera, vitrina, TPV, obra de humos). No inventar cifras de obra.
4. **Break-even como calculadora**, no como cifra; usar de método el de Loomis pero con personal de las ofertas (§7).
5. **Valle de verano:** ya hay 3 marcas reales con helado/horchata/granizado (1902, Vigo Churros, traspasos «heladería-churrería»): proponer **carta de verano** como entregable del xlsx de campañas, no «cierre».
6. **Pendiente para F2:** abrir webs propias de Maestro Churrero, Harimsa, Tardienta, Harinas Costas; reconfirmar el listado FEHR-Geregras; pedir presupuesto real de cafetera, vitrina calefactada y TPV; cruzar el madrugada/nocturnidad con L3.
