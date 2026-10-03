# «Cómo Montar una Churrería-Chocolatería» — SPEC v1.1 (2026-10-03, ronda 1 de refutación aplicada)

> Producto NUEVO nº 51, línea **«Cómo Montar»**, tamaño **L** (techo ≤ 10 M de tokens de subagentes; parada al
> +30 % = 13 M). Hermana directa de `guia-chocolateria-obrador` (LIVE desde el 19-sep), construida con el MISMO
> pipeline. Sesión Claude Code en el Mac, F1 de la política de 3 fases.
>
> **Fuentes (no se copian, se citan por sección):** research consolidado `auditorias/guia-churreria-RESEARCH-2026-10-03.md`
> (`RES §n`), refutación `auditorias/guia-churreria-research-REFUTACION-2026-10-03.md` (`REF Xn`, «CORREGIR ANTES»:
> 6 altas · 13 medias · 7 bajas; su lista «Lo que SÍ he confirmado letra a letra» **no se re-verifica**), las cinco
> lentes `-L1…L5-*.md` (ids `CUS-M*`/`CUS-V*` en L1, `CUS-D*` en L2, `CUN-*` en L3, `CUS-01…59` en L4) y las
> decisiones FIRMADAS `guia-churreria-DECISIONES-2026-10-03.md` (**D1-D25 + V-01…V-06: se aplican, no se reabren**).
> **Donde la refutación corrige al research, manda la refutación; donde una decisión firmada matiza a la
> refutación, manda la decisión.**
>
> **Fuente de verdad del CONTENIDO:** esta SPEC + `guias-v2_0/guion_guia_churreria_chocolateria.py` (se escribe en F2,
> D25). **De las CIFRAS:** los 8 xlsx de `astro-site/public/dl/guia-churreria-chocolateria/` y los ids `CUN-*` / `CUS-*`
> (nuevos) y `CHN-*` / `CHS-*` (reutilizados) de `auditorias/guias-v2-research-sector.json`. **De lo LEGAL:**
`auditorias/guia-churreria-verificacion-legal-2026-10-03.md` / `.json` (**cerrada el 3-oct**: V-01…V-06 resueltas en su §2;
> la rama elegida va escrita en cada sitio, sin «PENDIENTE»).
>
> **Molde:** `guia-chocolateria-SPEC.md` (11 secciones) y los generadores `guia-chocolateria/`. **Lo que aquí no se
> dice, se hace igual que en la hermana.**

## 0. Ficha del producto

| Campo | Valor |
|---|---|
| Nombre (**único**, D1) | **Cómo Montar una Churrería-Chocolatería** — idéntico en H1, `products-catalog.ts`, banner, tarjeta del hub, `PRODUCT_ALIASES`, `footerLinks`, asunto del broadcast y `emailBody`. Es la tarjeta ya publicada (`ProductosDigitalesHubPage.astro:1015`, SPA `ProductosDigitales.tsx:998`). EN futuro, sólo nombre: se elige con datos del mercado cuando toque (regla del 24-sep) |
| Subtítulo | «Local, obrador de masa, freidora y números: el dossier completo de apertura de una churrería-chocolatería, con los Excel que hacen tus cuentas.» (RES §12) |
| Title (≤ 60) | «Cómo Montar una Churrería-Chocolatería \| Guía y Excel» (53) |
| `productId` / slug | **`guia-churreria-chocolateria`** → `/guia-churreria-chocolateria` · `-access` · `-library`. Libre en `src`, `astro-site/src`, `netlify` y `_redirects` (RES verif. 9). `robots.txt` cubre `/guia-*-access` y `/guia-*-library` en los 5 bloques (`:44-45, :98-99, :152-153, :206-207, :260-261`): nada que tocar, **se verifica con `robots-gate.py`, no se supone** |
| Env var Stripe | `VITE_STRIPE_PAYMENT_LINK_GUIA_CHURRERIA_CHOCOLATERIA` (scope `builds`) |
| Precio (D3) | **65 €** IVA incluido. **Sin `priceOld`, sin `discountBadge`, sin `aggregateRating`, sin `review`, `testimonials.items: []`.** 10.º producto de la franja de 65 € (REF «confirmado»: escalera de 14 filas exacta) |
| Ancla (D3, A10) | 65 € = 5 % del curso de 1.290 € (`CUS-M06`) · 0,54 % del canon de Churros Factory, 12.000 € (`CUS-M15`) · menos que un mes de renta del local de referencia, 910 €/mes (`CUS-02`, el mismo anuncio que `CHS-37b`). **Gate de F3 (SR-10):** `CUS-M06` y `CUS-02` **no están re-verificados** (Milanuncios devolvió captcha el 3-oct; sus cifras son lectura de L1/L4); antes de publicar hay que reabrir los dos anuncios (navegador de Windows o captura de John). Si no se puede, la ancla queda sólo en el canon de 12.000 € (`CUS-M15`) y la FAQ 3 dice «hay cursos presenciales de pago en Madrid», sin cifra. **El curso de 290 € NO es ancla** |
| Pago | Stripe (principal) + **NOWPayments** (secundario) con las 3 puertas (`hero`, `buybox`, `cta`) + nota de devoluciones. `CRYPTO_PRODUCTS=all`: no se toca la env; sí `sync-product-prices.py` y el alta en `zona-app.ts` (regla del 19-sep) |
| Entregables | 1 guía PDF + DOCX (**19 capítulos + anexo normativo fechado**, D21) · bonus 1 **business plan relleno de «La Rueda»** (DOCX) · bonus 2 **«12 decisiones de apertura resueltas»** (PDF + DOCX) · **8 libros de Excel** con fórmulas vivas (D4) |
| Alcance (D2) | **(a) local fijo de 75 m²** con obrador de masa a la vista, freidora bajo campana, barra, sala, terraza y despacho a calle = **caso cifrado** · **(b)** despacho para llevar = columna de escenario con su régimen de apertura · **(c)** feria/caseta = capítulo + checklist (libro 7) + hoja «Punto Muerto por Evento» (libro 5), **sin caso cifrado**, remite a `plan-negocio-food-truck`/`kit-tareas-food-truck` · **(d)** franquicia = capítulo comparador, cifras fechadas como orden de magnitud publicado, sin recomendar marca · **(e)** churros en cafetería/bar = epígrafe con remisión · **(f)** obrador B2B = fuera, una línea |
| Público | Quien **aún no ha abierto** (personas P1-P4 de `RES §6`). **No** es un recetario ni un curso de churrero, **no** enseña a freír y **no** sustituye al proyecto técnico de la extracción (declaración en negativo arriba, `RES §12`) |
| Mercado | Marco normativo **español**, compradores de toda la hispanofonía; casillas editables; vocabulario es-ES con equivalencia LATAM en la primera mención (§6); adaptación fuera de España **como servicio** (D19, B3). Sin siglas en titulares (IAE, RGSEAA, APPCC, CTE van dentro) |
| Promesa (sin «verificado contra el BOE») | «No te enseña a freír. Te dice qué decidir y en qué orden: si ese local admite una freidora, cuánto cuesta abrir de verdad, a cuánto vender la ración y la taza, cuánta madrugada te toca y qué haces en verano.» (`RES §12`) |
| Canal | Hub ×2 (posición 1), buscador, post propio (D20), páginas de rol `chocolateria` y `cafeteria-brunch`, venta cruzada con la hermana en las dos direcciones, lista de compradores (Resend **13-nov 08:00Z**), plataforma. **No se promete tráfico SEO** (demanda de apertura ≈ 110-190/mes, `RES §0`) |

**Superficies que cambian en F3** (baseline medido el 3-oct): `src/data/products-catalog.ts` **50 → 51** ·
`netlify/shared/payment-links.ts` y `product-prices.ts` **52 → 53** claves (50 ES + 2 EN; GENERADOS) ·
`astro-site/src/lib/zona-app.ts` **52 → 53** entradas reales (`grep -c productId:` 53 → 54) ·
`astro-site/src/data/productos/guias/` **11 → 12 fichas** · las **4 functions con mapa** (`verify-purchase.ts`,
`resend-access.ts`, `admin-generate-access.ts`, `get-download-urls.ts`) · `src/data/productos-changelog.ts` (**v1.0
«Lanzamiento»**) · **hub, los DOS ficheros gemelos**: la tarjeta de `comingSoon` (`…HubPage.astro:1015` · SPA `:998`)
**sale del array y pasa a producto real en la POSICIÓN 1** con badge «✨ Nuevo» (la 5.ª novedad lo pierde) y `ListItem`
en el JSON-LD; `comingSoon` **21 → 20**. La guarda ya existe en los dos (`{comingSoon.length > 0 && (` en
`…HubPage.astro:1511`; `filteredComingSoon.length > 0` en `ProductosDigitales.tsx:1287`): nada que añadir.

## 1. Hallazgos resueltos y decisiones

### 1.A Los 26 hallazgos de la refutación, uno a uno

| Id | Grav. | Resolución en esta SPEC | Decisión |
|---|---|---|---|
| **A1** | ALTA | **Fix tal cual.** `CUN-29` en dos figuras: **trabajador nocturno del ET art. 36.1** (22-6 h, ≥ 3 h diarias o ≥ 1/3 de la jornada anual) y **plus de nocturnidad del convenio** (Madrid: +1 % de 22 a 0 h, +25 % de 0 a 8 h, toda la jornada nocturna con ≥ 5 h entre 22 y 8, `CUN-40`). Libro 8 con **una hoja «Nocturnidad: ET y Convenio» con dos columnas por persona, una para cada figura** (D9; SR-20); el juego de datos lo enseña con la entrada de las 4:30 (1,5 h en 22-6 → **no** nocturno; 3,5 h con plus). Matiz propio: «normalmente» del art. 36.1 no está interpretado en ninguna ficha → el libro da «sí / no / revísalo con tu asesor» (§2, libro 8). «El que entra a las 4-5 es trabajador nocturno» → §5 | **D9** |
| **A2** | ALTA | **Fix tal cual.** `CUS-31h/i` fuera de todo rango **y de toda hoja**: su cifra está en `prohibido` (D15 manda sobre la segunda mitad del fix, que los dejaba como ejemplo). Con sala, **82.000 €** pedidos y negociables (`CUS-02`, anuncio del 06-07-2026, precio pedido; lectura de L4 del 3-oct, no re-verificada por captcha). **El 95.000 € de `CHS-37b` es una lectura antigua del mismo anuncio que `CUS-02` corrige: a `prohibido`** (errata de dato de la verificación legal §4.3, anotada bajo D15 en `DECISIONES`; no reabre D15); barrio 16.000-19.500 € (`CUS-31a/b`); con cafetería 40.000-65.000 € (`CUS-31c/d/g`). FAQ 4 corregida (§8.3). `CUS-31` **a secas** prohibido (agrega h/i) | **D15** |
| **A3** | ALTA | **Fix tal cual.** El verano tiene **tres** salidas —cerrar (contribución 0: pagas los fijos sin ingresos, que el libro 6 muestra), carta de verano, ferias— en `5!El Verano` (por **contribución en euros**, SR-03), cap. 16 y decisión 9. La nota del 676 entra **sólo** como una línea del cap. 09 («existe; con la exención de `CHN-73` casi nunca te toca») y **en ningún Excel** | **D14** |
| **A4** | ALTA | **Fix tal cual.** La **actividad** de despacho (644.6, ≤ 750 m²) va por declaración responsable; **las obras no**: si la salida de humos necesita proyecto (casi siempre que hay conducto a cubierta), licencia de obra y técnico (Ley 12/2012 art. 3.3-3.4); terraza o elementos sobre la vía pública, autorización aparte (art. 2.2). **Primera fila de `7!Checklist Legal`: «¿la extracción necesita proyecto?»**, delante de «¿Anexo de la Ley 12/2012 sí o no?»; lo mismo en `CUN-35`, FAQ 7, cap. 04 y la ficha de visita del libro 1 | **D13** |
| **A5** | MEDIA | **Fix tal cual.** `CUN-26` completo en guion y libro: filtros a > 0,50 m del foco, **1,20 m si son de parrilla o de gas**. `1!Freidoras, Potencia y Riesgo` lleva «tipo de aparato (gas / parrilla / otro)» → distancia mínima en celda verde (1,20 / 1,20 / 0,50 m). La Rueda fríe con gas (`CUS-33a`) → 1,20 m | SPEC §2 (sin D propia) |
| **A6** | MEDIA | **Fix tal cual.** Se restituye «**de utilización móvil**» en `CUN-28` y se ata **sólo** a la variante (c). Para (a) y (b), la decisión 4 es «gas con instalación receptora (inspección cada 5 años, `CHN-48`) / eléctrico (potencia contratada)» | SPEC §2, §4.3 |
| **A7** | MEDIA | **Fix tal cual.** Coste por puesto = **MAX(salario del lector; SMI anual en celda verde)** con semáforo «por debajo del SMI 2026» (`CHN-67`); JobToday (`CUS-54/55`) sólo como «rango de mercado, pagas sin declarar»; **`CUS-56` fuera del producto**; tabla de Madrid etiquetada «2025 · convenio vencido» (**V-01 resuelta, rama A**, `CUN-V01`) | **D9** |
| **A8** | MEDIA | **Fix tal cual.** «Con chocolate, de 3,20-3,70 € en Granada (2026, `CUS-15`) a ~5 € en el centro de Madrid (2024, `CUS-19`): la plaza mueve el ticket alrededor de un 50 %.» El año va en cada fila de la tabla de precios (cap. 02 y `3!Mix y Ticket`). «Brecha ×4» → §5 | SPEC §3.3, §5 |
| **A9** | MEDIA | **Fix tal cual.** El P&L toma el margen del **escandallo del libro 3** (materia prima + aceite absorbido) y resta la nómina aparte; el ~50 % de La Artesana sólo como contraste en `3!Los Dos Márgenes`, con su definición incierta. La hermana deja de usar 0,5 como margen bruto (`PyG 3 Años!C58`, parche D7) | **D6**, D7 |
| **A10** | MEDIA | **Fix tal cual.** Fuera el curso de 290 € (`CUS-M05`, fuente que redirige) del ancla y de la FAQ 3: «cursos presenciales hasta 1.290 € en Madrid» (`CUS-M06`) | **D3** |
| **A11** | MEDIA | **Fix tal cual + V-06.** La denominación de la taza es **interpretación**, no nivel A. Decisión 6 reformulada: «**qué preparado compras y qué dice su etiqueta**». **V-06 resuelta** como interpretación B/C (`CUN-V06`; §3.3, SR-01) | **V-06** |
| **A12** | BAJA | **Fix tal cual.** Cap. 10 y `4!Consumo y Reposición`: «el medidor de mano te dice cuándo cambiar; el 25 % legal se demuestra en laboratorio» (art. 6.3 y anexo 1) | SPEC §2, §4 |
| **A13** | BAJA | **Fix tal cual.** «El 644.6 está en el Anexo» se cita con `CHN-49b` (la hermana ya lo afirmó); `CUN-09` sólo para la nota de churrería del epígrafe. No se vende como novedad | SPEC §4 |
| **A14** | BAJA | **Fix tal cual.** Parte B sólo si se opera «siguiendo las instrucciones del explotador … que suministra de forma centralizada» (art. 2.3). Nunca «las franquicias» sin más | **D12** |
| **B1** | ALTA | **Fix tal cual, con las palancas aplicadas desde el diseño:** 0,162 M por bloque como suelo; **26 bloques** (05+09 fundidos, BP en 2, bonus en 4) y guion bajado a **40.100 palabras** para que el bloque medio (1.540) se acerque al de la hermana (1.404). §9 suma fila a fila, con banda alta por palabra | **D21, D22, D23, D5** |
| **B2** | MEDIA | **Fix tal cual.** Sin «posición 1» como argumento en landing, FAQ, correo ni §7. Frase permitida, si hace falta: «el post aparece en primera posición para “montar una churreria 2026” (SERP del 3-oct, sin volumen medido) y suma 133 impresiones en 90 días» | **D20** |
| **B3** | BAJA | **Fix tal cual.** «≤ 10/mes para “montar/poner/abrir”; en México, ~50 para “negocio de churros” y “franquicia de churros”, y 1.600 para la churrera». FAQ 12 ofrece la adaptación como servicio, sin promesa | **D19** |
| **B4** | BAJA | **Fix tal cual.** Dos pasadas de `fase8x-sustituir-banner.py` (§7.2), cada una con su gate de 3 banners | SPEC §7.2 |
| **B5** | BAJA | **Fix tal cual.** La v1.0.1 de la hermana añade `Variante del Formato!E38-E41` y `!E47` con su id `CUS-*` o «véase la Guía de Churrería-Chocolatería», y retira el 0,5 de `PyG!C58` (§8.4) | **D7** |
| **C1** | ALTA | **Fix con una alternativa argumentada.** Grafo sin ciclos y orden de relleno **3 → 1 → 4 → 5 → 8 → 2 → 6** (el 7 no depende de nadie); precio del aceite en celda propia del libro 3; CAPEX sin fondo; fondo sólo en el 6; gate nuevo de ciclos. **Alternativa:** el fix decía que el 3 «solo contrasta» el € de aceite que devuelve el 4; eso sería una referencia «← 4» en el 3, es decir, una arista hacia atrás que el propio gate tumbaría. El contraste se hace **aguas abajo**: el 4 recibe del 3 el aceite absorbido y calcula sólo la **renovación** (descarte); el 6 suma las dos, cada una con su fuente (§2.2) | **D16** |
| **C2** | MEDIA | **Fix con una alternativa argumentada.** La franja del día nace **sólo** en el 5 y el punto muerto por evento vive **sólo** en el 5; el 6 recibe de las ferias una línea anual. **Alternativa:** el fix pedía que el 1 recibiera del 5 las raciones/h; con el orden firmado (1 antes que 5) sería otra arista hacia atrás. Por eso la **demanda base** (raciones del día tipo y del día punta) nace en el 1 (`1!Día Tipo y Día Punta`), el **reparto** por mes y franja en el 5, y la **«Cola del Domingo» pasa del libro 1 al 5**, que es donde están a la vez la franja y la capacidad (← 1) | **D16** |
| **C3** | MEDIA | **Fix tal cual.** Regla única: «**supuesto declarado de La Rueda**», valor en celda verde con la nota «supuesto, sin fuente pública; pon el tuyo»; nunca en copy ni FAQ. Lista y valores en §3.5; `comprobar()` aborta si alguno es `None` | **D17** |
| **C4** | MEDIA | **Fix tal cual.** Capítulos 05 + 09 del research fundidos y colocados **después** del 07 del research: es el nuevo **cap. 06** (§4; la renumeración de SR-09 lo adelanta un puesto) | **D21** |
| **C5** | MEDIA | **Fix tal cual.** Sin hoja «Comparativa de Aceites»; el libro 4 trabaja con **tu** aceite y **tu** registro | **D4** |
| **C6** | BAJA | **Fix tal cual.** FAQ 5 → «¿Es rentable una churrería?»; FAQ 6 → «¿Los Excel parten de mi receta o de una receta vuestra?» (§8.3) | SPEC §8.3 |
| **C7** | MEDIA | **Fix tal cual.** Cada decisión del bonus 2 lleva **la resolución con los números de La Rueda** (qué eligió, con qué celda del libro y cuál es el umbral para elegir lo contrario) y `puntos_por_epigrafe` prohíbe repetir la explicación de su capítulo (§4.3) | **D5** |

### 1.B Las 25 decisiones firmadas, y dónde se aplican

| # | Decisión (resumen) | Se aplica en |
|---|---|---|
| D1 | Nombre único, slug `guia-churreria-chocolateria`, producto 51 | §0 |
| D2 | Alcance (a) cifrado · (b) columna · (c) capítulo + checklist + hoja · (d) comparador · (e) epígrafe · (f) fuera | §0, §2, §4 |
| D3 | 65 €, sin tachado ni ratings, Stripe + NOWPayments; ancla sin el curso de 290 € | §0, §10 |
| D4 | 8 libros; feria como hoja del 5; libro propio de turnos; sin «Comparativa de Aceites» | §2 |
| D5 | BP en 2 bloques (≥ 3.500 palabras, ≥ 9 tablas, resumen con neto, margen y punto de equilibrio); 12 decisiones en 4 bloques de 3 con número, criterio y veredicto | §4.2, §4.3 |
| D6 | `CHS-31` a lista negra; >60 % sobre producto (Loomis, `CUS-01`) y «un poquito más del 50 %» de rentabilidad declarada por el gestor de La Artesana (`CUS-30`) en `3!Los Dos Márgenes`; el P&L usa el escandallo | §2, §3.3, §5 |
| D7 | Hermana v1.0.1 en la F3 de este producto, un solo correo | §7.3, §8.4 |
| D8 | Pack APPCC 09 = deuda aparte; sin temperatura de fritura del churro salvo V-02 | §2 (libro 4), §5, §8.4 |
| D9 | Convenio de Madrid clase C como ejemplo; dos figuras de nocturnidad; suelo SMI 2026 | §2 (libro 8), §3.2 |
| D10 | Horario 6:00 (cafetería/bar) / 8:00 (chocolatería) en Madrid; sin extrapolar | §2 (libro 7), §3.2 |
| D11 | IVA del chocolate para llevar en celda verde, 10 % por defecto | §3.3 |
| D12 | Acrilamida: buena práctica en el churro; parte A si fríes patatas; parte B sólo art. 2.3 | §2 (libro 7), §5 |
| D13 | Actividad por declaración responsable, obras con proyecto aparte; 1.ª fila del checklist | §2, §4, §8.3 |
| D14 | Verano sin media cuota; tres salidas | §2 (libro 5), §4 |
| D15 | Fuera `CUS-31h/i`; con sala 82.000 € (errata de dato, SR-02); 95.000, 120.000 y 107.000 a `prohibido` | §3.4, §5 |
| D16 | Grafo sin ciclos 3 → 1 → 4 → 5 → 8 → 2 → 6; gate de ciclos | §2.2, §2.5 |
| D17 | «La Rueda», 75 m², 910 €/mes; OEPM antes del guion; supuestos declarados | §3 |
| D18 | Tarjeta de «Próximos Productos» sin precio en F1 (desviación anotada) | §0 (el precio llega en F3) |
| D19 | es-ES + tejeringo/calentito/jeringo/«chocolate caliente» en 1.ª mención; México con demanda de maquinaria | §6 |
| D20 | Sólo se amplía el post propio, con su tabla corregida y 3 banners; sin «posición 1» | §7.2 |
| D21 | Caps. 05 + 09 fundidos tras el 07 (numeración del research; en esta SPEC, el cap. 06) → 19 capítulos + anexo = 20 bloques | §4 |
| D22 | 0,162 M por bloque; 26 bloques; ≈ 11-12 M; se reporta a John | §9, §10 |
| D23 | Refutación de documentos: una ronda, 3 lentes en un prompt Opus + gates; 2.ª sólo sobre bloqueantes | §8.2, §9 |
| D24 | F2 en el Mac, en serie, vigilante térmico, máximo 2 agentes a la vez | §2.5, §9 |
| D25 | Corte de F1 = research + SPEC refutada (≤ 2 rondas) + `datos_ejemplo.py` con gate; el guion pasa a F2 | §9 |

**Verificación legal cerrada el 3-oct (ramas aplicadas, cada una en su sitio):** V-01 **A** (tablas 2025 con convenio vencido, §3.2) · V-02 **B** (sin cifra de temperatura de fritura del churro, §2 libro 4 y §5) · V-03 **B** (IAE + doble código CNAE como pregunta al asesor, §2 libro 7) · V-04 **B** (celda verde al 10 % con aviso, §3.3) · V-05 **B matizada** (alcanza a un obrador, no se afirma del despacho, §3.2) · V-06 **resuelta como interpretación B/C** (qué preparado compras y qué dice su etiqueta, §3.3; SR-01). **Antes del guion:** OEPM para «La Rueda» (D17) y re-comprobación de los precios de hosteleria10 con descuento al construir el libro 2.

**Fichas e ids (estado a 3-oct):** `auditorias/guia-churreria-ids-CUS.json` y `guia-churreria-verificacion-legal-2026-10-03.json` (+ `-EXCLUIDOS.json`), listas de fichas con **exactamente las 12 claves** de la hermana. **Fusión APLICADA** con `auditorias/guia-churreria-json-merge.py` (calco de `guia-chocolateria-json-merge.py`: dry-run por defecto, gate de recuento, `--apply`, idempotente): `guias-v2-research-sector.json` tiene **837 datos = 635 + 202**, **pendiente de commit**. `CUS-31h`, `CUS-31i`, `CUS-56`, `CUS-M05`, `CUS-05` y `CUS-40` **están en el JSON común como ids con la nota «PROHIBIDO»** (no en EXCLUIDOS, que son otras 27 entradas descartadas): el veto lo ejecutan `comprobar()` y `verificar_guion.py` con `IDS_PROHIBIDOS` (§2.3, §5.1). Ids citados por L1 sin entrada (`CUS-M32`, `V-ctx`) se normalizan. **No se toca `CHS-31` en el JSON común antes de la v1.0.1 de la hermana** (su guion lo cita; marcarlo antes rompería sus gates).

### 1.C Los 21 hallazgos de la refutación de la SPEC (ronda 1), uno a uno

| Id | Grav. | Resolución | Dónde |
|---|---|---|---|
| **SR-01** | ALTA | Aplicado. Cabecera «cerrada el 3-oct». V-06 sin la regla «sólo si el preparado cumple»: la carta usa **la denominación de la etiqueta del preparado**; el libro 3 pide el % de cacao seco total y la grasa vegetal, y con < 35 % o con grasa vegetal muestra «consulta a tu servicio de consumo antes de imprimir la carta». Nunca «sólo puedes llamarlo así si cumple» | cabecera · §1.A A11 · §3.3 · §4.3 (dec. 6) · §5 |
| **SR-02** | ALTA | Aplicado. Con sala **82.000 €** (precio pedido y negociable); 95.000 y `CHS-37b`-para-traspaso a `prohibido`; errata anotada bajo D15 en `DECISIONES` sin reabrirla | §1.A A2 · §1.B D15 · §3.1 · §5 · §8.3 FAQ 4 |
| **SR-03** | ALTA | Aplicado. El 5 compara las tres salidas por **contribución en euros** (los fijos son iguales y los resta el 6); cruce nuevo **X16 6 ← 5**; fila «verano con fijos» en `6!Escenarios`; ninguna celda «gastos fijos» ni «renta» en el 5 (gate). **Añadido propio, mínimo:** X5 lleva también el coste hora de mano de obra, para valorar el refuerzo sin una segunda fuente | §2.1 (5, 6) · §2.2 · §2.4 · §4.3 (dec. 9) |
| **SR-04** | MEDIA | Aplicado. V-01 A · V-02 B · V-03 B (doble código CNAE-2025 + CNAE-2009) · V-04 B (riesgo del 21 %) · V-05 B matizada (obrador); 14 pagas como supuesto declarado | §2.1 (4, 7, 8) · §3.2 · §3.3 · §5 |
| **SR-05** | MEDIA | Aplicado. >60 % sobre producto (Loomis, `CUS-01`) y «un poquito más del 50 %» de rentabilidad declarada por el gestor de La Artesana (`CUS-30`); «una dueña» a la lista negra | §1.B D6 · §3.3 · §5 · §8.3 FAQ 5 |
| **SR-06** | MEDIA | Aplicado. Núcleo 8.618,35 € + Testo 499,00 € (calculado desde 603,79 € con IVA) = **9.117,35 €**; la rellenadora, línea sin cifra con importe del lector; variante (b) con Testo 4.684,45 €; `CUS-40` fuera de la procedencia del bloque 6 | §3.4 · §2.1 (2) |
| **SR-07** | MEDIA | Aplicado. Cruces nuevos X2 bis (4 ← 3), X3 bis (4 ← 1), mix de canales en X11, X17 (2 ← 3), X18 (6 ← 2); el 7 no pide el horario y remite a `5!Franjas del Día`, donde vive el semáforo de las 8:00 con su hora mínima legal en celda verde; arista nueva 3→2 (compatible con el orden firmado) | §2.1 (2-7) · §2.2 |
| **SR-08** | MEDIA | Aplicado. Nueva §5.1 con los 12 puntos literales de la verificación §6 y las filas que faltaban en la tabla; cap. 02 con `CUS-07` sólo como hallazgo negativo y `CUS-08` sin cifra en prosa | §5.1 · §5.2 · §4 (cap. 02) |
| **SR-09** | MEDIA | Aplicado. El IVA (carta y equipamiento) pasa al **cap. 03** y el 19 sólo lo cita; «Cuánto cuesta abrir» pasa al **cap. 08**, detrás de Maquinaria: 04 Antes de firmar · 05 Humos · 06 Local y hora punta · 07 Maquinaria · 08 Cuánto cuesta abrir. D21 se sigue cumpliendo. Palabras: +100 en el 03 y −100 en el 19 (la suma sigue en 30.000) | §4 |
| **SR-10** | MEDIA | Aplicado. Gate de F3: reabrir `CUS-M06` y `CUS-02` antes de publicar; si no se puede, la ancla queda en 12.000 € y la FAQ 3 va sin cifra; el 82.000 € es «lectura de L4, no re-verificada» | §0 · §1.A A2 · §3.1 · §8.2 · §8.3 |
| **SR-11** | MEDIA | Aplicado. Celda verde «¿proteges los aparatos con extinción automática?» con el veredicto de la nota 2 del CTE (sigue aplicando la nota 3) y celda verde con los kW de los demás aparatos de cocción, releyendo antes la nota de la tabla 2.1 del DB-SI; cap. 05 y decisión 4 presentan las dos salidas con su coste en el 2 | §2.1 (1) · §4 (cap. 05) · §4.3 (dec. 4) |
| **SR-12** | MEDIA | Aplicado. La corrección del post cubre `faq:` (`:13`, `:15`, `:19`), entradilla `:30` y el bloque `:66-97`; purga obligatoria de `astro-site/.astro` y `FAQPage` verificado en el `dist` de la nube. Comprobado contra el post: las tres respuestas y la entradilla llevan N-3, N-2 y 4.800 € / 60 % / 88 raciones | §7.2 · §5 |
| **SR-13** | MEDIA | Aplicado. §3.5 gana `GASTOS_FIJOS_MENSUALES` (supuestos declarados; el seguro de RC sin cifra) y la densidad del aceite (celda verde del 3, viaja con X2); `comprobar()` aborta si falta cualquiera; «§3.6» → «§3.5» | §3.5 · §1.A C3 · §3 |
| **SR-14** | MEDIA | Aplicado. Frontera del libro 8: no reproduce el cuadrante semanal ni las nóminas de `kit-gestion-personal` (01, 03); el kit entra en `footerLinks` y en los salientes | §2.1 (8) · §7.1 |
| **SR-15** | MEDIA | Aplicado. FAQ 1 («ninguna de las que hemos leído»), FAQ 4 sin «Verificado:» y con el aviso de lo que no incluye, FAQ 11 con la respuesta de la hermana (convención interna, sin la causalidad de Sheets) | §8.3 |
| **SR-16** | BAJA | Aplicado. Bases de IVA (`CUS-24` declarada, `CUS-25` inferida), ambigüedad caja/pack de `CUS-21` a re-comprobar, 6 uds por ración como supuesto, bola sin cifra, celda de IVA en todas las bebidas para llevar | §3.3 · §2.1 (3) |
| **SR-17** | BAJA | Aplicado **con una salvedad**: el cuadrante se completa en `datos_ejemplo.py` y `comprobar()` exige cero huecos de cobertura. **«Declarar el domingo de cierre» se descarta tal cual**: el domingo abre (6:00, día punta y «Cola del Domingo»), lo que no estaba declarado era su **hora de cierre**, y es la que se declara | §3.2 · §3 |
| **SR-18** | BAJA | Aplicado. Fusión descrita como aplicada (837 = 635 + 202); `IDS_PROHIBIDOS` completos y `RX_ID` ampliado en `comprobar()` y `verificar_guion.py` | §1.B (fichas) · §2.3 · §5.1 · §8.2 |
| **SR-19** | BAJA | Aplicado. Título de 53 caracteres; cola Resend con 3-nov y 8-nov como huecos reservados; orden de eventos con `COUNTIF`, nunca `RANK`; las estimaciones F1 se sustituyen por el consumo medido antes de reportar a John (D22) | §0 · §2.1 (5) · §7.3 · §9 |
| **SR-20** | BAJA | Aplicado. Una hoja con dos columnas por persona (D9 «una columna para cada figura» se cumple); Maestro Churrero sólo con los 115.000 € de `CUS-M14`, el 75.000 € a `prohibido` | §2.1 (2, 8) · §1.A A1 · §5 |
| **SR-21** | BAJA | Aplicado. Gate de solape de cada capítulo H contra el `txt/` homólogo de `guia-chocolateria-obrador`; si supera el umbral se reescriben los `puntos_por_epigrafe`, no el texto | §4 · §8.2 |

**Descartados:** ninguno por completo. Matiz de SR-17 arriba. **Queda una ronda como máximo**, que debe comprobar las tres altas y SR-07 sobre esta SPEC corregida.

## 2. Los 8 libros de Excel (D4; RES §9.2 corregido por C1, C2, C5 y D16)

Ruta `astro-site/public/dl/guia-churreria-chocolateria/`. **Los ocho nombres quedan firmados aquí** (de ellos salen 8 de
las **13 claves** de `PRODUCT_FILES`, §8.1). Convenciones y prohibiciones: las de la hermana (`guia-chocolateria-SPEC.md`
§2.3) sin cambios — helpers de `guias-v2_0/motor.py`, «Instrucciones» primero con la línea `Versión 1.0 · <mes> 2026 ·
aichef.pro/guia-churreria-chocolateria · info@aichef.pro`, cero constantes en fórmulas, parámetros en celda verde y
**ninguna celda verde vacía**, `IFERROR(…;"")`, semáforos con `ISNUMBER`, «sin dato» = `""` (nunca 0), DV contra rango,
**prohibidos `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA`, `RANK`, `NETWORKDAYS`, `IRR` y toda
referencia entre libros**, columna «¿lleva IVA?» y tipo en toda línea de precio, food cost sobre base imponible en los dos
lados, dato legal con nota «Verificado el <fecha> · norma y artículo · URL», `author='AI Chef Pro'`, WinAnsi,
`inject_cache.py` + verificación `data_only` + `build/mapa-<libro>.json` + `gate_libros.py`.

### 2.1 Libro a libro

| # | Fichero · hojas | Entradas (verde) | Salidas por fórmula | Decisión que resuelve | Frontera |
|---|---|---|---|---|---|
| **1** | `produccion-hora-punta-y-local.xlsx` · Instrucciones · Parámetros · Zonas y m² · Equipos y Capacidad · **Freidoras, Potencia y Riesgo** · Cuello de Botella · **Día Tipo y Día Punta** · Ficha de Visita a Local | m² por zona; kg de masa/h efectivos de la línea; carga y minutos por tanda; personas en línea; **litros de cada freidora y tipo de aparato** (gas/parrilla/otro, A5); **raciones del día tipo y del día punta** (única fuente de la demanda base, C2); kg de masa por ración ← 3; **¿proteges los aparatos con extinción automática?** (sí/no); **potencia en kW de los demás aparatos de cocción** (celda verde; qué aparatos computan lo fija la nota de la tabla 2.1 del DB-SI: **releerla antes de construir** y citarla en la nota de la celda) | raciones/h que aguanta el conjunto; el equipo que manda; kg de masa y kg fritos al día; **kW computables (freidoras a 1 kW/L + los demás aparatos de cocción) → riesgo bajo/medio/alto (> 20/30/50 kW) → ¿extinción automática? (> 50 kW)**; **si proteges los aparatos con extinción automática y el uso no es hospitalario ni residencial público: «no es local de riesgo especial (nota 2 del CTE), aunque te sigue aplicando la nota (3)»**; distancia mínima del filtro; **veredicto de la ficha**, con los eliminatorios en este orden: ¿la extracción necesita proyecto? (A4) · conducto a cubierta · gas · potencia | ¿Una churrera o dos? ¿Ese local sirve? | `CUN-23/24/26`. **Sin «Demanda por Franja» ni «Cola del Domingo»** (pasan al 5, C2). Sin clima ni carga térmica |
| **2** | `calculadora-capex-churreria.xlsx` · Instrucciones · Parámetros · CAPEX por Bloque · Equipamiento Línea a Línea · Variante del Formato (local con sala · despacho · caseta · franquicia) · Franquicia frente a Independiente · Traspaso vs Obra Nueva · IVA y Tesorería · Proveedores · Resumen | importe mín/máx/tuyo y **«¿lleva IVA?» por línea**; variante; traspaso pedido, **renta mensual (nace aquí; la recibe el 6, X18)** y horizonte; **«¿necesitas extinción automática?» ← 1**; **precio del aceite €/L y del mix €/kg ← 3** (stock inicial, X17) | CAPEX por bloque y total **SIN fondo de maniobra** (ningún bloque ni fila con ese nombre, D16); extra por variante; traspaso frente a obra a 5 años; IVA a adelantar; desviación contra lo presupuestado | ¿Cuánto necesito y en qué formato? | `CUS-32…43`, `CUS-58/59`, `CUS-02`, `CUS-31a-g`, `CUS-M12…M25`. **Sin plazo de entrega** (vive sólo en el 7). Franquicia como orden de magnitud fechado; **Maestro Churrero: sólo los 115.000 € de `CUS-M14` (lexpress, 30-06-2026); el 75.000 € a `prohibido` (N-9) hasta abrir su web**. **Rellenadora: línea con importe del lector y nota «sin precio con fuente»** (`CUS-40`, SR-06) |
| **3** | `carta-de-apertura-y-escandallo-churro.xlsx` · Instrucciones · Parámetros · **Escandallo por kg de Masa** (churro y porra) · **Absorción de Aceite y Merma** · Chocolate a la Taza · Coste Hora · Ración, Docena o Kilo · **Mix y Ticket por Canal y Temporada** · **Los Dos Márgenes** · Decisión de Surtido | receta y precios (mix, `CUS-21`); g de masa por pieza; % de absorción; merma; **precio del aceite €/L — celda única del paquete** (`CUS-23`) **y densidad del aceite (kg/L, supuesto declarado; viaja con X2)**; receta y precio del preparado de la taza (`CUS-24`) **y su % de cacao seco total y si lleva grasa vegetal** (con < 35 % o con grasa vegetal, aviso «consulta a tu servicio de consumo antes de imprimir la carta», V-06); **coste hora de mano de obra**; **PVP con IVA y tipo por referencia (también en las bebidas para llevar, SR-16)**; mix sala/para llevar y de invierno/verano | coste por pieza, ración, docena, kilo y taza; **kg de masa por ración media** (→ 1 y 4) y **aceite absorbido en € por ración** (→ 4); **margen sobre materia prima (comparable al >60 %) y margen tras aceite y mano de obra (comparable al ~50 %), juntos y con su definición**; ticket sin IVA por canal; margen € × rotación | ¿A cuánto vendo la ración, la docena y la taza? | `CUS-15…25`, `CUS-30`, `CHN-05`, `CUN-42`. **Sin franjas** (son del 5): la hoja de ticket va por canal y temporada. Ni Kit Escandallos ni Food Cost costean masa frita (R9 de `RES §8`) |
| **4** | `aceite-de-fritura-coste-y-cambio.xlsx` · Instrucciones · Parámetros · Consumo y Reposición · Punto Económico de Cambio · Escenarios de Precio del Aceite · Gestor de Aceite Usado | **precio del aceite, % de absorción, densidad, kg de masa por ración y aceite absorbido en € por ración ← 3** (X2, X2 bis); **kg fritos al día, litros de cuba y raciones del día tipo y punta ← 1** (X3, X3 bis); reposición diaria; **días entre cambios** (supuesto declarado con la nota «si tienes el Pack APPCC, usa tu registro de `09-control-aceite-fritura.xlsx`»); % de subida | € de **renovación** (descarte) por ración y por mes; litros al gestor; impacto de la subida en el margen; fila de contraste «aceite absorbido (3) + renovación (4) = aceite total por ración» | ¿Cuánto me cuesta el aceite y cuándo lo cambio? | `CUN-01…03`, `CUN-27`, `CUS-23`, `CUS-38`, `CUS-44h`. **No es registro APPCC** (cita el Pack). **Sin «Comparativa de Aceites»** (C5). Sin temperatura de fritura del churro (**V-02 resuelta, rama B**: sin fuente primaria; los 175 °C del Rgto. 2017/2158 son de patatas). El < 175 °C de las patatas (`CUN-05`) sí entra |
| **5** | `temporada-franjas-y-ferias.xlsx` · Instrucciones · Parámetros · Peso sobre el Año · **Franjas del Día** · Capacidad contra el Pico · **Cola del Domingo** · Refuerzo por Pico · **El Verano: Cerrar, Carta de Verano o Ferias** · **Punto Muerto por Evento** · Calendario de Ferias | 12 coeficientes; **horario y % por franja (única fuente)**; **hora mínima legal de apertura** (celda verde, nota «Verificado el 2026-10-03 · Orden de 21-04-2022 de Madrid · `CUN-34`»); días; **raciones del día tipo y punta y capacidad raciones/h ← 1**; **ticket sin IVA, coste de materia por ración y coste hora de mano de obra ← 3**; por evento: días, horas, tasa (fija o €/m²·día), m², desplazamiento, montaje, personal, afluencia | ventas por mes y día; demanda por franja; **déficit de capacidad y cola en domingos y Navidad-Reyes**; **horas de refuerzo**; **contribución de julio-agosto en euros de cada salida** (ventas sin IVA − materia por ración ← 3 − refuerzo y personal variable del evento − tasas y desplazamiento; **los fijos son los mismos en las tres y los resta el 6**; gana la de mayor contribución); semáforo «antes de las 8:00 → sólo como cafetería/bar en Madrid» (D10); raciones para cubrir cada evento y orden de eventos **con `COUNTIF`, nunca `RANK`**; **resultado anual de ferias** y **contribución de julio-agosto de la salida elegida** (→ 6, X14 y X16) | ¿Cierro en verano? ¿A qué ferias voy? | `CUS-11`, `CUS-29`, `CUS-V17`. **Sin media cuota del 676** (A3). **Ninguna celda con rótulo «gastos fijos» ni «renta»** (viven en el 6). Sin canon de 60 €/día (R7); `CUN-37` sólo como ejemplo de pueblo pequeño (N-19). El evento de ejemplo es método, no caso (D2) |
| **6** | `plan-financiero-3-anos-churreria.xlsx` · 0. Supuestos · Inversión Inicial · PyG 3 Años · Punto de Equilibrio · Escenarios · Personal · Tesorería 12 meses · Financiación · Canales y Punto Muerto (sala · para llevar · ferias) · Instrucciones | **CAPEX sin fondo y renta mensual ← 2** (X10, X18); **coste de materia por ración, ticket sin IVA y mix de canales ← 3**; **renovación de aceite por ración ← 4**; **raciones del año, 12 coeficientes, resultado anual de ferias y contribución del verano ← 5**; **gastos fijos mensuales** (§3.5; nacen sólo aquí); **coste anual de plantilla ← 8**; **meses de colchón** (el fondo de maniobra se calcula AQUÍ y sólo aquí); rampa; deuda | P&L a 3 años; punto muerto mensual y **en raciones/día**; tesorería con el valle; **«verano: resultado con fijos» de cada salida en `6!Escenarios`**; DSCR; columna «local con sala / sólo despacho»; inversión total = CAPEX + fondo | ¿Aguanta el banco? ¿Qué canal paga los fijos? | Motor `planes-v2_0` 2.2. **Veredictos en euros, nunca por ratio** (`RES` verif. 2). El principal del préstamo como punto fijo, igual que la hermana (`principal_prestamo()`), sin referencia circular en el xlsx |
| **7** | `checklist-legal-fritura-y-licencias.xlsx` · Instrucciones · **Checklist Legal (F1-F6)** · **Árbol IAE y CNAE por Formato** · **Régimen de Apertura y Horario** · Licencia, Humos y Gas · Árbol de Registro Sanitario · **Ferias y Venta Ambulante** · **Alérgenos y Aceite Compartido** · **PRL de la Fritura** · Registro de Formación · Cronograma y Ruta Crítica | estado, coste, fecha y responsable; respuestas del árbol (¿consumo en el local? ¿para llevar? ¿ferias? ¿suministras a otros?); CCAA y municipio; **plazo de entrega de la maquinaria crítica** (única fuente del paquete) | contador por fase; **1.ª fila «¿la extracción necesita proyecto? → licencia de obra y técnico»**, luego **«¿Anexo de la Ley 12/2012 sí o no?»** (D13); epígrafes que te tocan (644.6 / 676-673 / 663.1 / 675 / 419.3) con la exención de `CHN-73`; la norma del horario de Madrid (D10) con remisión a `5!Franjas del Día`, donde pones tu hora de apertura (**el libro 7 no pide el horario**); gas: instalación receptora + inspección quinquenal en (a)/(b) y bombona < 15 kg «de utilización móvil» **sólo** en (c) (A6); clase F; acrilamida según D12; ruta crítica | ¿Qué papel me toca y en qué orden? | **No depende de ningún libro.** CNAE (**V-03 resuelta, rama B**): IAE + la correspondencia candidata **como pregunta al asesor con doble código CNAE-2025 + CNAE-2009** (`CUN-16`, `CHN-74b`), nunca como dato, y la trampa de `CUN-15` (47.81 = vehículos). Sin cadmio, EUDR ni ruta doméstica |
| **8** | `turnos-plantilla-y-madrugada.xlsx` · Instrucciones · Parámetros · Cuadrante por Franja · **Nocturnidad: ET y Convenio** (dos columnas por persona) · Coste de Plantilla · Convenio: Cómo Identificar el Tuyo · Horas del Titular | provincia y convenio; salario base por categoría y pagas (ejemplo Madrid, tablas **2025**: V-01 resuelta, rama A; **14 pagas como supuesto declarado**); **franja del plus en celda verde** (22-0 h +1 %, 0-8 h +25 %, umbral de 5 h); jornada anual; SMI anual; % de SS; **horas por franja y horas de refuerzo ← 5**; **personas en línea ← 1**; **coste hora del escandallo ← 3** (fila de cuadre: «el coste hora que usaste en el 3 frente al que sale de tu plantilla») | por persona: horas entre 22 y 6, días con ≥ 3 h y % de la jornada anual → **«sí / no / revísalo con tu asesor»**; horas con plus y su coste; **coste anual por puesto = MAX(salario; SMI)** con semáforo; coste total (→ 6); horas del titular; huecos de cobertura | ¿Cuánta gente necesito y cuánto me cuesta abrir de madrugada? | `CUN-29`, `CUN-31/32`, `CUN-39/40`, `CHN-67/68/93`, `CUS-54/55`. Sólo al **trabajador nocturno** le alcanzan la prohibición de horas extra y el tope de 8 h (A1). Sin «no existe convenio de churrerías» (§5). **No reproduce el cuadrante semanal por empleado ni las nóminas de `kit-gestion-personal` (01, 03)**: calcula horas por franja, las dos figuras de nocturnidad, el plus y el coste anual por puesto para el plan. Venta cruzada: «para el cuadrante semana a semana, el Kit de Gestión de Personal» |

**Cobertura de la promesa publicada** («local, obrador, carta, licencias y números»): local → 1 · obrador → 1, 2 · carta → 3 ·
licencias → 7 · números → 2, 3, 4, 5, 6, 8.

### 2.2 Cruces entre libros: el grafo sin ciclos (D16) y las celdas «← N»

Cada cruce es una **celda verde «cópialo del libro N: `<fichero>.xlsx!<Hoja>!<Celda>`»** con su valor por defecto (el que
calcula `datos_ejemplo.py` para La Rueda) **+ una fila de CUADRE con semáforo** en la misma hoja, que avisa si lo tecleado
se aleja del origen. **Nunca una fórmula entre ficheros.** Los cruces viven en `datos_ejemplo.CRUCES` (campos de la hermana
+ `celda_origen` declarada **antes** de construir, que es el contrato entre constructores) y el orden en
`datos_ejemplo.ORDEN_RELLENO = (3, 1, 4, 5, 8, 2, 6, 7)`, que la hoja «Instrucciones» de cada libro repite.

| # | Receptor ← origen | Qué viaja | Por qué así |
|---|---|---|---|
| X1 | 1 ← 3 | kg de masa por ración media | Raciones/h = kg/h ÷ kg por ración |
| X2 | 4 ← 3 | precio del aceite €/L (base imponible) · % de absorción · **densidad del aceite (kg/L)** | El precio vive en el 3 (D16); el 4 no lo vuelve a pedir |
| X2 bis | 4 ← 3 | kg de masa por ración media · aceite absorbido en € por ración | Sin ellos el libro 4 no puede dar «por ración» ni la fila de contraste «aceite absorbido (3) + renovación (4)» (SR-07) |
| X3 | 4 ← 1 | kg fritos al día · litros totales de cuba | Consumo y reposición |
| X3 bis | 4 ← 1 | raciones del día tipo y del día punta | Reposición y renovación «por ración» (SR-07) |
| X4 | 5 ← 1 | raciones del día tipo y del día punta · capacidad en raciones/h | La demanda base nace en el 1; el reparto, en el 5 (C2) |
| X5 | 5 ← 3 | ticket sin IVA · coste de materia por ración · **coste hora de mano de obra** (valora el refuerzo sin fuente nueva) | Punto muerto por evento y verano en euros |
| X6 | 8 ← 1 | personas en línea en el pico | Huecos de cobertura del cuadrante |
| X7 | 8 ← 5 | horas por franja de la semana tipo · horas de refuerzo | La franja sólo existe en el 5 |
| X8 | 8 ← 3 | coste hora de mano de obra usado en el escandallo | Cuadre del coste hora (el 3 va antes y lo supone) |
| X9 | 2 ← 1 | «¿necesitas extinción automática?» (1/0) | El umbral de 50 kW se aplica una sola vez, en el 1 |
| X10 | 6 ← 2 | CAPEX **sin** fondo de maniobra | El fondo sólo se calcula en el 6: cero doble conteo (C1) |
| X11 | 6 ← 3 | coste de materia por ración y ticket sin IVA, por canal, **y mix de canales (% de raciones sala / para llevar)** | El margen sale del escandallo (A9) |
| X12 | 6 ← 4 | renovación de aceite por ración | Distinto del aceite absorbido, que ya va en X11 |
| X13 | 6 ← 5 | raciones del año · 12 coeficientes | Tesorería mensual con el valle |
| X14 | 6 ← 5 | resultado anual de ferias (una línea de canal) | Punto muerto por evento sólo en el 5 (C2) |
| X15 | 6 ← 8 | coste anual de plantilla | Personal |
| X16 | 6 ← 5 | contribución de julio-agosto de la salida elegida | El verano se compara por contribución en el 5; el 6 resta los fijos y muestra «verano con fijos» en `6!Escenarios` (SR-03) |
| X17 | 2 ← 3 | precio del aceite €/L y del mix €/kg (base imponible) | Stock inicial (bloque 10) sin segunda fuente del precio; arista nueva 3→2, compatible con el orden firmado (SR-07) |
| X18 | 6 ← 2 | renta mensual | La renta nace en el 2 (traspaso, fianza); el 6 la recibe para los fijos, con fila de CUADRE (SR-07) |

Aristas: 3→1, 3→4, 1→4, 1→5, 3→5, 1→8, 5→8, 3→8, 1→2, 2→6, 3→6, 4→6, 5→6, 8→6, **3→2** (X17); el 7, aislado. El orden firmado es un
orden topológico válido. **Prohibido** cualquier cruce que no esté en esta tabla; si F2 necesita otro, entra aquí primero y
el gate lo comprueba. El número exacto de celdas (y por tanto de filas de CUADRE) lo fija `CRUCES`: **una fila de CUADRE por
celda cruzada**, contadas contra `CRUCES`.

### 2.3 Qué generador se calca y qué es nuevo

`H` = se calca el `gen_*.py` de la hermana (`scripts/productos-digitales/guia-chocolateria/`) y se cambia el contenido ·
`N` = sin molde. Carpeta nueva `scripts/productos-digitales/guia-churreria/`.

| # | Molde | Qué se calca | Qué es nuevo |
|---|---|---|---|
| 1 | H+N | `gen_capacidad-obrador-y-clima.py` (2.102 l.): Zonas y m², Capacidad por Equipo, Cuello de Botella, Ficha de Visita. **Fuera: Clima del Obrador** | Freidoras, Potencia y Riesgo; Día Tipo y Día Punta |
| 2 | H | `gen_calculadora-capex-chocolateria.py` (2.059): CAPEX por Bloque, Variante, Traspaso vs Obra Nueva, IVA y Tesorería, Resumen **sin la fila de fondo ni el cruce 2 ← 7** + Equipamiento y Proveedores de `gen_checklist-equipamiento-y-proveedores-cacao.py` (1.922) **sin EUDR, cadmio, clientes ni plazo** | Franquicia frente a Independiente (hoja propia); bloques de extracción, fritura y sala |
| 3 | H+N | `gen_carta-de-apertura-y-escandallo-chocolate.py` (1.868): Escandallo, Coste Hora, Mix y Ticket, Decisión de Surtido | Escandallo por kg de masa; Absorción de Aceite y Merma; Chocolate a la Taza; Ración, Docena o Kilo; Los Dos Márgenes |
| 4 | N | Estructura de Parámetros y Escenarios de `gen_sensibilidad-al-precio-del-cacao.py` (1.214) | Todo |
| 5 | H+N | `gen_campanas-y-valle-del-ano.py` (1.387): Peso sobre el Año, Capacidad vs Demanda, Refuerzo, Valle → El Verano | Franjas del Día, Cola del Domingo, Punto Muerto por Evento, Calendario de Ferias |
| 6 | H | `gen_plan-financiero-3-anos-chocolateria.py` (3.899) + `_comun_libro_7.py` (motor 2.2). **Fuera: Talleres y Regalo Corporativo** | Canales con la línea de ferias; fondo de maniobra sólo aquí |
| 7 | H+N | `gen_checklist-legal-licencias-y-cacao.py` (2.568) + `_comun_libros_8_9.py`: F1-F6, Árbol de Registro, Formación, Cronograma. **Fuera: Cadmio, EUDR, Ruta Doméstica** | Árbol IAE y CNAE, Régimen y Horario, Licencia/Humos/Gas, Ferias, Alérgenos y Aceite, PRL |
| 8 | N | Helpers del motor y la hoja Personal del 6 | Todo |
| — | H | `_comun_chocolateria.py` → `_comun_churreria.py`; `_comun_libros_3_5/4_6/8_9.py` y `_comun_libro_7.py` se renombran por libro receptor; `datos_ejemplo.py` (estructura y `comprobar()`); `gate_libros.py`; `verificar_guion.py` | `LIBROS` con 8 nombres; `PID`; `N_LIBROS = 8`; `RX_ID = (?:CHN\|CHS\|CUN\|CUS\|FC-IVA)-(?:[MVD])?[0-9]+[a-z]*` (casa `CUN-V01`, `CUS-M06`, `FC-IVA-01`; el de la hermana, no) en `comprobar()` y en `verificar_guion.py`; `IDS_PROHIBIDOS` completos: `CUS-31h`, `CUS-31i`, `CUS-56`, `CUS-M05`, `CUS-05`, `CUS-40` (cifra), `CHS-37b` (para traspaso); a secas: `CUS-31`, `CHS-31` (§5.1) |

### 2.4 El gate nuevo de `gate_libros.py` (D16)

Nueva función `auditar_ciclos(D)` junto a `auditar_cruces()` (que ya existe y se conserva): construye el grafo
`fichero_origen → fichero_receptor` desde `D.CRUCES`, lo ordena con Kahn y **aborta** si (1) queda algún nodo sin ordenar
(ciclo), (2) `D.ORDEN_RELLENO` no es un orden topológico de ese grafo, (3) el libro 7 aparece en alguna arista, o (4) hay en
cualquier hoja un rótulo «cópialo del libro N» / «trae aquí la cifra de» **que no esté en `CRUCES`** (un cruce no declarado
escapa al grafo). Más: **una fila de CUADRE por celda cruzada**, contadas contra `CRUCES`; **ninguna fila ni bloque «fondo de
maniobra» en el libro 2**; **ninguna celda del libro 5 con rótulo «gastos fijos» ni «renta»** (viven en el 6, por X16 y X18; SR-03); ninguna hoja de escandallo referencia una celda cuya nota diga «CON IVA». Se prueba antes de usarlo
con un `CRUCES` sintético con ciclo (canario: debe abortar) y otro con una arista hacia atrás contra el orden firmado.

### 2.5 Reparto en constructores para F2 (D24: máximo 2 agentes a la vez)

Cuatro tandas de dos, siguiendo el orden de relleno. Como `CRUCES` fija de antemano la celda de origen y el valor por
defecto, el receptor no espera al `mapa-*.json` del origen para construir; el rótulo y la fila de CUADRE se comprueban
contra el `mapa` al cerrar cada tanda.

| Tanda | Constructor A (opus) | Constructor B (opus) | Por qué juntos |
|---|---|---|---|
| T1 | **3** escandallo (origen de X1, X2, X5, X8, X11) | **7** checklist legal (aislado) | El 3 abre el grafo; el 7 no depende de nadie y es el más largo de los legales |
| T2 | **1** producción y local (← 3; origen de X3, X4, X6, X9) | **4** aceite (← 3, ← 1) | Hablan de la misma freidora: litros, kg fritos y riesgo |
| T3 | **5** temporada, franjas y ferias (← 1, ← 3) | **8** turnos (← 1, ← 5, ← 3) | La franja del 5 es el cuadrante del 8 |
| T4 | **2** CAPEX (← 1) | **6** plan financiero (← 2, 3, 4, 5, 8) | El 6 cierra el grafo; el 2 es su X10 |

Después: **1 refutador opus** de los 8 xlsx → **fixer sonnet** → `inject_cache.py` + `data_only` + `mapa-*.json` +
`gate_libros.py` (con `auditar_ciclos`) → copia a `dl/`. **Los xlsx nunca se tocan a mano: se regeneran.** Cada agente, un
python cada vez, con `istats cpu temp` antes de cada tanda (≥ 63 °C → esperar 60 s) y el vigilante activo.

## 3. Juego de datos único: «Churrería-Chocolatería La Rueda» (D17)

Un solo `scripts/productos-digitales/guia-churreria/datos_ejemplo.py` del que beben los 8 generadores, el guion y los dos
bonus. **Cuatro orígenes válidos, escritos en el propio `.py` y comprobados por `comprobar()`:** (1) id `CUN-*`/`CUS-*` de
las fichas de este producto; (2) id `CHN-*`/`CHS-*` reutilizado del JSON común, con su sufijo; (3) **«supuesto declarado»**;
(4) **«heredado»**: un supuesto ya declarado por la hermana o por `motor.PARAMETROS`, citado por campo. **No hay quinto
origen.** UN concepto = UNA fuente; ningún parámetro del resultado neto o del punto de equilibrio queda «sin valor» (C3).
`comprobar()` aborta además si aparece un id prohibido (`IDS_PROHIBIDOS`, §5.1), si una suma de control no cuadra (§3.4, §3.5), si falta algún supuesto de §3.5 o si el cuadrante de §3.2 deja huecos de cobertura.

### 3.1 Identidad y local

| Campo | Valor | Procedencia |
|---|---|---|
| Nombre | «Churrería-Chocolatería **La Rueda**» (la rueda es la porra en espiral) | Supuesto declarado. **OEPM antes del guion** (D17); si colisiona con marca viva en clase 30/43, se cambia aquí y se regenera |
| Ciudad | Ciudad media española sin nombre; los parámetros de Madrid (horario, ordenanza de humos, convenio) como **ejemplo declarado** | Patrón de familia |
| Superficie | **75 m²**: obrador de masa a la vista 10 · fritura bajo campana 6 · barra y despacho a calle 12 · sala 32 · aseos y vestuario 8 · almacén (harina, aceite, envase, bidón de aceite usado) 7. **Terraza aparte, 20 m²**, con autorización propia | 75 m²: convergencia `CHS-37a` (75) y `CUS-02` (74). Reparto por zonas y terraza: supuesto declarado |
| Renta | **910 €/mes** | `CUS-02` (misma ficha que `CHS-37b`) |
| Formato fiscal | Sala (676 o 673) **+ 644.6** si vende al peso para llevar, como inferencia declarada | `CUN-10`, `CUN-14` |
| Entrada al local | **Obra nueva en local sin salida de humos** (el caso más duro y el de la 1.ª fila del checklist); el traspaso de `CUS-02` (82.000 € pedidos y negociables, lectura de L4 no re-verificada, 74 m², ~50.000 € de equipos declarados) es la alternativa de la decisión 2 | Supuesto declarado; `CUS-02` |

### 3.2 Horario, franjas, plantilla, turnos y convenio

| Campo | Valor | Procedencia |
|---|---|---|
| Horario | L-V 7:00-13:00 y 16:30-21:00 · S, D y festivos desde las 6:00 · V y S hasta la 1:00 · **domingos y festivos hasta las 21:00** (el domingo abre —día punta y «Cola del Domingo»—; su hora de cierre no estaba declarada) | Supuesto declarado. Abrir antes de las 8:00 sólo cabe, en el ejemplo de Madrid, como cafetería/bar (`CUN-34`; D10): es la decisión 8 |
| Franjas (% de raciones) | desayuno 50 · media mañana 10 · merienda 35 · noche (sólo V-S) 5 | Supuesto declarado; vive sólo en `5!Franjas del Día` |
| Plantilla | **Titular** (encargado/a, en nómina como en la hermana) · **2 churreros/as** a 1,0 · **1 camarero/a de sala** a 1,0 · **refuerzo** 0,5 en fines de semana y Navidad-Reyes | Supuesto sobre `CUS-54/55` (rango de mercado, pagas sin declarar). Titular en nómina: heredado |
| Turnos del ejemplo (A1) | Churrero/a 1: L-V 6:00-14:00 → 0 h en 22-6, 2 h con plus · Churrero/a 2: S-D-F 4:30-12:30 → **1,5 h en 22-6 (no es trabajador nocturno)**, 3,5 h con plus · V y S 17:00-1:00 para quien cierre → 3 h en 22-6 dos días por semana → el libro marca **«revísalo con tu asesor»**. **Esos tres son los casos didácticos de las dos figuras; el cuadrante completo del caso se cierra en `datos_ejemplo.py`**: cubre L-V 16:30-21:00 (la merienda, 35 % de las raciones) y S, D y festivos hasta su cierre, con cada churrero/a a su jornada contratada (1,0 = 40 h/semana) sin pasarse de ella, y `comprobar()` exige **cero huecos de cobertura** en La Rueda (SR-17) | Supuesto declarado; reglas de `CUN-29` y `CUN-40` |
| Convenio de ejemplo (D9) | Hostelería de la Comunidad de Madrid, `28002085011981`, clase C («Chocolaterías»), provincia en celda verde; niveles por **asimilación de funciones declarada** (nunca «la categoría de churrero»), fijada en el `.py` con el artículo del ALEH VI que la sostenga o, si no lo hay, como «asimilación propuesta: compruébala con tu asesor» | `CUN-39`, `CUN-31` (ALEH VI, vigente hasta el 31-12-2030 por `CUN-32`) |
| Tablas salariales (**V-01 resuelta, rama A**, `CUN-V01`) | Tabla **2025** (nivel III 1.160,37 € + plus de convenio 191,22 € × 11), etiquetada «2025 · convenio vencido el 31-12-2025, en negociación; se aplican sus tablas mientras no se publique el nuevo» + **14 pagas como supuesto declarado** («dos gratificaciones del art. 26 de una mensualidad cada una: compruébalo en tu convenio») + suelo SMI | `CUN-39`, `CUN-V01` (media) |
| Método «identifica el tuyo» | Toledo `45000145011981` (**V-05 resuelta, rama B matizada**, `CUN-V05`): el ámbito dice «obradores de … Masas Fritas»; alcanza a un **obrador** de churros, y si el tuyo es despacho con sala te lo confirma un laboralista (interpretación de nivel C). Sólo como ejemplo del método «busca el tuyo en REGCON»; fuente: base jurídica privada (el BOP no se abrió); vigente hasta el 31-12-2026 | `CHN-93`, `CUN-V05` |
| SMI | 1.221 €/mes · **17.094 €/año** (celda verde; caduca el 31-12-2026, vive en el anexo) | `CHN-67` |
| SS de empresa | 0,33 | Heredado: `motor.PARAMETROS['ss_empresa']` |
| Registro horario | Diario, con hora de inicio y fin, 4 años; el RD digital anunciado no está en el BOE | `CHN-68` |

### 3.3 La carta: 24 referencias en 5 familias, con IVA declarado

PVP **con IVA** (precios de mostrador); el libro 3 publica la base imponible por fórmula. **Un concepto = una fuente:** cada
PVP tiene UN origen; el año de la fuente va en la fila (A8).

| Familia | Referencias | PVP de La Rueda | Procedencia |
|---|---|---|---|
| **Churros y porras** (7) | ración de churros (6 uds) · media ración (3) · ración de porras · churro suelto · porra suelta · docena para llevar · kilo para llevar | ración **2,60 €**, media **1,40 €** (PVP de `CUS-17`, cuya ración **no declara el número de churros**; **6 uds por ración = supuesto**, formato de `CUS-15`) · suelto 0,30 € / porra 0,60 € · ración de porras, docena y kilo: supuesto declarado | `CUS-17` (Palma, 21-10-2025) · `CUS-16` (Vallecas, 21-09-2026) · supuesto |
| **Rellenos y especiales** (2) | churro relleno (ud) · ración con cobertura | supuesto declarado | Oferta descrita sin precios (`CUS-09`) |
| **Chocolate a la taza** (5) | taza en barra · taza en terraza · **chocolate con churros** (taza + ración) · taza para llevar · media taza | barra **2,00 €** / terraza **2,50 €** · combo **3,80 €** · para llevar y media: supuesto declarado | `CUS-15` (Granada, 2026) · combo: supuesto dentro del 3,50-4 € de `CHS-32` |
| **Cafés y bebidas** (6) | café solo · café con leche · infusión · leche con cacao · zumo de naranja · agua | supuesto declarado (sin fuente de café ni azúcar, `RES §4.2`); **«¿lleva IVA?» y tipo en celda verde en todas las bebidas para llevar** (leche con cacao incluida, SR-16) | Supuesto |
| **Carta de verano** (4) | granizado · horchata · helado (bola) · batido | granizado **3 €**, horchata **3 €**, batido 4-4,50 € (`CUS-11`); **bola: supuesto declarado (sin precio publicado)** | `CUS-11` (Chocolatería 1902, 2026) |

- **Materia prima (sin IVA salvo aviso):** mix de churros **1,45 €/kg** (34,80 € / 24 kg) y rendimiento declarado por el
  vendedor 4 kg → ~11,5 kg de masa (`CUS-21`; **la ficha dice «Caja 6 sacos» en un slug de «pack de 3 cajas»: re-comprobar al construir el libro 3 si los 34,80 € son de una caja o del pack**, el 1,45 €/kg puede estar mal por un factor 3) · aceite **1,996 €/L** (49,90 € / 25 L, techo del rango de `CUS-23`) ·
  preparado de la taza **7,19 €/kg** (techo de `CUS-24`, **base declarada «impuestos excluidos»**; «¿lleva IVA?» en verde) · cucurucho **0,15 €/ud** (`CUS-25`, **base «sin IVA» inferida**: «¿lleva IVA?» en verde, por defecto «no», con
  aviso) · vaso para llevar, leche, azúcar, café y fruta: supuesto declarado. El vaso de plástico o papel plastificado **se cobra aparte en el ticket** desde el 1-1-2023 (`CUN-41`): fila propia en la carta. **El cucurucho de cartón no se presenta como conforme a la ley de plásticos** (composición por confirmar).
- **IVA** (se explica en el **cap. 03**, que es donde el libro 3 lo aplica; SR-09): sala y churros para llevar, **10 %** (`CHN-71c`, `FC-IVA-01…03`); equipamiento, 21 % general (`CHN-71c`).
  **Chocolate para llevar (V-04 resuelta, rama B, `CUN-18`):** celda verde al 10 % por defecto con «consulta a tu asesor: con agua y un preparado azucarado podría ser el 21 %»; nunca en prosa (D11); lo mismo en «leche con cacao» y el resto de bebidas para llevar.
- **Denominación de la taza (V-06 resuelta: interpretación de nivel B/C, `CUN-V06`):** el juego de datos supone un **preparado comercial cuya etiqueta dice
  «chocolate a la taza»** (supuesto declarado; formato profesional sin fuente, `CUS-44g`). La carta usa **la denominación que figura en la etiqueta del preparado**; el libro 3 (`Chocolate a la Taza`) pide en celdas verdes el % de cacao seco total y si lleva grasa vegetal, y con menos del 35 % (`CUN-42`) o con grasa vegetal muestra «**consulta a tu servicio de consumo antes de imprimir la carta**». **Nunca** «sólo puedes llamarlo así si cumple» ni «ni chocolate a la taza ni chocolate»: de ningún artículo del RD 1055/2003 sale esa regla. La decisión 6 es «qué preparado compras y qué dice su etiqueta».
- **Márgenes de contraste (D6):** «márgenes superiores al 60 % en producto» (Loomis, `CUS-01`) y «un poquito más del 50 %» de **rentabilidad** (Javier, gestor de La
  Artesana, `CUS-30`, fiabilidad baja), cada uno con su definición. **El de La Rueda sale del escandallo.**
- **Alérgenos:** gluten siempre, leche en la taza, aceite compartido como contaminación cruzada (`CHN-33`, `CHN-34`); «sin
  gluten» casi nunca se puede decir (`CHN-37`).

### 3.4 Dotación y CAPEX por bloque (SIN fondo de maniobra)

**Dotación con fuente, sin IVA declarada en la ficha** (variante B de L4, `CUS-59`, suma recomputada por `REF`): freidora de
gas 25 L **1.907,00 €** (`CUS-33a`) · dosificadora automática CH 5 kg **1.798,00 €** (`CUS-34c`) · amasadora automática
**2.550,00 €** (`CUS-35a`) · campana 1200 con turbina **990,00 €** (`CUS-36a`) · 2 × chocolatera Irimar MCH-5 **825,40 €**
(`CUS-37a`) · escurridor bandeja **499,20 €** (`CUS-39`) · balanza **48,75 €** (`CUS-41`) = **8.618,35 €**; + Testo 270 BT
**499,00 € sin IVA, calculado desde 603,79 € con IVA** (`CUS-38`, indicativo, A12) = **9.117,35 €**. **La rellenadora NO entra con cifra** (`CUS-40`: sin precio utilizable): línea en el libro 2 con importe del lector y nota «sin precio con fuente» (SR-06). `comprobar()`
exige **8.618,35 € y 9.117,35 € al céntimo**. ⚠️ hosteleria10 aplica descuentos caducables: **re-comprobar y fechar cada celda al construir
el libro 2**. La variante (b) usa la dotación A (`CUS-58`, 4.185,45 € núcleo; **4.684,45 € con el Testo**, sin rellenadora).

| Bloque | Contenido | Procedencia |
|---|---|---|
| 1 Obra civil y acondicionamiento | Local en bruto de 75 m² | Supuesto declarado |
| 2 Extracción y conducto | Campana (`CUS-36a`, ya en dotación) + **conducto a cubierta, obra y proyecto** | Conducto: supuesto declarado (`CUS-36b`: sin fuente) |
| 3 Fritura, dosificación y amasado | Freidora, dosificadora, amasadora, escurridor | `CUS-33a`, `CUS-34c`, `CUS-35a`, `CUS-39` |
| 4 Chocolate y café | 2 chocolateras + cafetera de 2 grupos | `CUS-37a` + cafetera: supuesto (`CUS-43`) |
| 5 Barra, sala y terraza | Mostrador, vitrina calefactada, mobiliario, vajilla, lavavajillas | Supuesto declarado (`CUS-43`) |
| 6 Control y seguridad | Testo, balanza, rellenadora, extintor clase F (`CUN-38`), filtrado de aceite | `CUS-38`, `CUS-41` + supuesto (rellenadora: importe del lector, `CUS-40` sin cifra) |
| 7 TPV y rótulo | — | Supuesto declarado |
| 8 Licencias, proyecto de actividad y tasas | Con la línea de **extinción automática** si X9 = 1 | Supuesto declarado (**nunca** el 2.000-6.000 € del post, N-4) |
| 9 Fianza y garantías | meses de fianza × renta | Meses: supuesto; renta `CUS-02` |
| 10 Stock inicial y envase | Mix, aceite, preparado, cucuruchos y vasos | Precios de §3.3 (aceite y mix ← 3, X17) × cantidades supuestas |
| 11 Marketing de apertura | — | Supuesto declarado |

Los importes supuestos se fijan en `datos_ejemplo.py` con su razonamiento y una sola referencia de contraste publicada en
la hoja de instrucciones: los **~50.000 € de dotación completa** que declara el traspaso de `CUS-02` para un local de 74 m².
La hoja «Variante del Formato» compara local con sala / despacho (`CUS-58`) / caseta (remolque 14.800 €, carrito 6.190 €,
`CUS-42`) / franquicia (`CUS-M12…M25`, fechadas).

### 3.5 Producción, aceite, temporada y canales — los supuestos declarados de C3

| Parámetro | Valor de La Rueda | Por qué este valor |
|---|---|---|
| g de masa por churro / por porra | 20 g / 60 g | Supuesto declarado; la ración de 6 churros es la de `CUS-15` |
| % de absorción de aceite | 10 % del peso frito | Supuesto declarado (N-12 prohíbe la grasa de churros de maíz como dato) |
| Días entre cambios de aceite | 6 | Supuesto declarado; el lector pone el de su registro (Pack APPCC 09) |
| kg de masa/h efectivos de la línea | 12 | Supuesto declarado; **nunca** el máximo del fabricante (N-8, `CUS-26`) |
| Raciones/día | día tipo **250** · día punta (S, D, festivo) **400** | Supuesto apoyado en `CUS-27` (La Artesana: 200-300 L-V, ~400 el fin de semana) |
| Coeficientes mensuales (suman 12) | ene 1,25 · feb 1,15 · mar 1,10 · abr 0,95 · may 0,85 · jun 0,70 · jul 0,55 · ago 0,50 · sep 0,80 · oct 1,10 · nov 1,30 · dic 1,75 | Supuesto declarado con la forma cualitativa de `CUS-29` y `CUS-V17` (pico oct-mar y Navidad); la serie de Google Ads no vale (`RES §3.5`). `comprobar()` exige la suma 12 |
| Mix de canales | sala 70 % · para llevar 30 % de las raciones; **ferias 0** (La Rueda elige carta de verano: decisión 9) | Supuesto declarado (sin fuente cuantitativa, `RES §3.5`) |
| Verano | carta de verano en julio y agosto; las tres salidas se calculan igual en `5!El Verano` | `CUS-11`; D14 |
| Evento de ejemplo (sólo método) | una feria local de 5 días con tasa fija | Supuesto declarado; `CUN-37` sólo como ejemplo de pueblo pequeño (N-19) |
| Coste hora de mano de obra (libro 3) | el que sale de la plantilla de §3.2 | Calculado en el `.py`; el 8 lo cuadra (X8) |
| **Gastos fijos mensuales** (libro 6; nacen sólo allí) | suministros con gas y electricidad de fritura · limpieza de conductos y campana · mantenimiento · seguros (**el seguro de RC sin cifra con fuente**, como en la hermana) · asesoría · comisiones del TPV · gestor de aceite (`CUS-44h`, sin precio) | **Supuestos declarados**, cada uno con su importe y razonamiento en `datos_ejemplo.GASTOS_FIJOS_MENSUALES`; la renta (910 €/mes) y la plantilla no están aquí: llegan por X18 y X15. «Heredado» no vale: el perfil de consumo de una freidora no se parece al de una bombonería |
| **Densidad del aceite (kg/L)** | celda verde del libro 3 con la nota «supuesto, sin fuente pública; pon el tuyo»; viaja con X2 | Supuesto declarado: la absorción va en % del peso frito y el precio en €/L, y sin este factor el 3 y el 4 meterían una constante dentro de la fórmula (prohibido). Valor y razonamiento, en `datos_ejemplo.py` |

`comprobar()` **aborta si falta cualquiera de los dos** (gastos fijos o densidad).

### 3.6 Financiación, calendario y proveedores

- **Financiación (heredada de la hermana, supuestos declarados allí):** 40 % propios / 60 % préstamo a 84 meses, 6,2 % nominal,
  6 meses de carencia; colchón de **6 meses de fijos** (el fondo se calcula sólo en el 6); amortización a 10 años; rampa de
  arranque heredada. El principal se deriva como punto fijo (`principal_prestamo()` de la hermana).
- **Apertura:** 1 de septiembre del año 1 (supuesto declarado): un mes de rodaje antes del pico y el valle al final del año 1.
- **Proveedores verificados (sólo con URL abierta):** Churrofácil (`CUS-44a`) · Harinas Sánchez Palencia (`CUS-44b`) ·
  fabricantes Inblan, J.L. Blanco, Inhospan, Mundigas, Repagas, NTGAS (`CUS-44e`) · gestor de aceite Reseave (`CUS-44h`) ·
  HostelShop sin precios (`CUS-44f`). **No se publican**: los de sólo directorio (`CUS-44c/d`), Valor y Simón Coll en formato
  profesional (`CUS-44g`, sólo existencia) ni el listado FEHR-Geregras de 2015 (`CUS-44i`) salvo reconfirmación.

## 4. Índice: 19 capítulos + anexo (D21) y los dos bonus

**Calibración medida en la hermana** (`RES` verif. 4): guía +57 % de palabras sobre el guion y **534,5 palabras/página**;
bonus +62 % y **500 palabras/página**. **Un bloque por capítulo**: 20 (guía) + 2 (BP) + 4 (bonus) = **26 bloques** (D22).

| Entregable | Guion | Salida realista | Gates (`GUIA['gates']`) | La landing publica |
|---|---|---|---|---|
| Guía, 19 caps + anexo | **30.000 palabras** (1.500 de media por bloque) | ≈ 47.000 palabras → **≈ 88 págs** | `paginas_prometidas: 80` · `palabras_objetivo: 30000` · `min_palabras_cap: 1100` | la cifra MEDIDA tras construir (`paginas-gate.py`) |
| Bonus 2, 12 decisiones | 12 × 550 = **6.600** (1.650 por bloque) | ≈ 10.700 → **≈ 21 págs** | `paginas_prometidas: 20` · `palabras_objetivo: 6600` · `min_palabras_cap: 400` | ídem |
| Bonus 1, business plan | **3.500 + ≥ 9 tablas** (2 bloques) | 3.500-4.500 | ≥ 9 `<w:tbl>` en `word/document.xml`, coherentes con el libro 6 celda a celda | ídem |

Claves de cada capítulo y reglas del guion: las de la hermana (`n`, `titulo`, `resumen_indice`, `palabras`, `bloques`,
`objetivo`, `epigrafes`, **`puntos_por_epigrafe`** obligatorio, `cifras` con `C(etiqueta, 'fichero.xlsx!Hoja!Celda', fmt)`,
`sector`, `tablas`, `prohibido` = `NO_COMUN` + lo propio, nunca vacío). **Ninguna cifra entra si no sale de una celda de
xlsx o de un id con fuente.** `_ERRATAS_OK` se asigna a `GUIA` **y a cada bonus**. Regla de orden: **cada decisión legal que
un xlsx aplica tiene su capítulo ANTES** (por eso la ficha de visita va en el 06, tras el 04 y el 05, C4; **y el IVA, que aplican los libros 3 y 2, se explica en el 03**, SR-09). Fronteras
explícitas en `puntos_por_epigrafe` entre 04, 05 y 09, y entre 10 y 11 (riesgo de desduplicación del Manual del Chef ≈ 2,2 M).

`H` hereda estructura y `puntos_por_epigrafe` de la hermana (**y pasa el gate de solape contra el capítulo homólogo de ella, §8.2**) · `N` nuevo · 🔴 lo firma el verificador legal antes de redactar.

| # (research) | Capítulo | H/N | Palabras | Hoja que cita | Ids que sostiene |
|---|---|---|---|---|---|
| 01 (01) | Qué negocio estás montando: seis formatos y cuál te toca («la bombonería es otro negocio», con enlace) | H | 1.600 | 2 · Variante del Formato | `CUN-09…13`, `CUN-35`, `CHN-49b`, `CHN-49c` |
| 02 (02) | El cliente, las franjas y la plaza | H | 1.300 | 5 · Franjas del Día | `CUS-06` (locales de hostelería, INE), `CUS-07` **sólo como hallazgo negativo** («no hay cifra de churrerías»), `CUS-08` **sin cifra en prosa**, `CUS-13`, `CUS-15`, `CUS-17`, `CUS-19` (con año, A8) |
| 03 (03) | La carta de apertura: churro, porra, chocolate a la taza y para llevar, **y el IVA de cada cosa que vendes y de lo que compras** | H+N | 1.600 | 3 · Mix y Ticket por Canal y Temporada · 3 · Chocolate a la Taza | `CUS-09…11`, `CUS-15…20`, `CHN-05`, `CUN-42`, `CUN-41`, `CHN-71c`, `FC-IVA-01/02`, `CUN-18` · V-06 (resuelta) · V-04 (resuelta: celda verde al 10 %) |
| 04 🔴 (06) | Antes de firmar: el formato decide el régimen de apertura, las obras y el horario | N | 1.700 | 7 · Checklist Legal (1.ª fila) · 7 · Régimen de Apertura y Horario | `CUN-09/10/14/34/35`, `CHN-49b/49c`, `CHN-77`, Ley 12/2012 arts. 2.2, 3.3-3.4 (A4) |
| 05 🔴 (07) | Humos, extracción y fuego de aceite: lo que exige la norma y lo que fija el proyecto | N | 1.700 | 1 · Freidoras, Potencia y Riesgo · 7 · Licencia, Humos y Gas | `CUN-23…26` (con los 1,20 m, A5, **y la nota 2 del CTE: con extinción automática no es local de riesgo especial, SR-11**), `CUN-28` (sólo feria, A6), `CUN-38`, `CHN-45/46/48` |
| 06 (05+09) | El local y la hora punta: metros, conducto, ficha de visita y la cola del domingo | H+N | 1.800 | 1 · Zonas y m² · 1 · Ficha de Visita a Local · 5 · Capacidad contra el Pico · 5 · Cola del Domingo | `CUS-02`, `CUS-31a-g`, `CUS-13`, `CUS-26`, `CUS-27`, `CUN-23/24` |
| 07 (08) | Maquinaria: churrera, dosificadora, freidora, amasadora y chocolatera | H | 1.300 | 2 · Equipamiento Línea a Línea · 1 · Equipos y Capacidad | `CUS-32…41`, `CHS-46a` (sólo si se nombra la Ugolini) |
| 08 (04) | Cuánto cuesta abrir, partida a partida (y lo que nadie publica): llega con extinción, obra y maquinaria ya explicadas (caps. 04-07) y con el IVA ya explicado en el 03 | H | 1.600 | 2 · CAPEX por Bloque · 2 · IVA y Tesorería | `CUS-32…43`, `CUS-58/59`, `CUS-02` |
| 09 🔴 (10) | Alta fiscal y sanitaria de cada formato: IAE, CNAE y registro | H | 1.600 | 7 · Árbol IAE y CNAE por Formato · 7 · Árbol de Registro Sanitario | `CUN-09…16`, `CUN-21`, `CUN-30`, `CHN-39/41/73/94` · V-03 · la nota del 676 en una línea (A3) |
| 10 🔴 (11) | Aceite de fritura: calidad, cambio, coste y gestor | N | 1.600 | 4 (todas) · cita el Pack APPCC 09 como registro | `CUN-01…03`, `CUN-27`, `CUS-23`, `CUS-38`, `CUS-44h` · A12 · V-02 |
| 11 🔴 (12) | Acrilamida, alérgenos y el aceite compartido | N | 1.500 | 7 · Alérgenos y Aceite Compartido | `CUN-04…08` (con D12 y A14), `CHN-33/34/37` |
| 12 (13) | Autocontrol, formación y el día de la inspección | H | 1.300 | 7 · Registro de Formación | `CHN-32/51/69` |
| 13 (14) | Escandallo del churro y de la porra: rendimiento, absorción y los dos márgenes | H+N | 1.600 | 3 · Escandallo por kg de Masa · 3 · Absorción de Aceite y Merma · 3 · Los Dos Márgenes | `CUS-21…25`, `CUS-30`, `CUS-01` (por qué `CHS-31` no entra) |
| 14 (15) | Proveedores: harina, aceite, chocolate, envase y gestor | H | 1.200 | 2 · Proveedores | `CUS-44a/b/e/f/h`, `CUS-25`, `CUN-41` |
| 15 🔴 (16) | El equipo, los turnos y la madrugada | H+N | 1.700 | 8 (todas) | `CUN-29` (dos figuras, A1), `CUN-31/32`, `CUN-39/40`, `CHN-67/68/93`, `CUS-54/55` · V-01, V-05 |
| 16 (17) | La temporada: de octubre a marzo, y qué haces en verano | H | 1.400 | 5 · Peso sobre el Año · 5 · El Verano | `CUS-11`, `CUS-29`, `CUS-31e/f`, `CUS-V17` (sin media cuota, A3) |
| 17 🔴 (18) | Ferias, casetas y venta ambulante | N | 1.500 | 5 · Punto Muerto por Evento · 5 · Calendario de Ferias · 7 · Ferias y Venta Ambulante | `CUN-11/13/19…22/25/28/36/37`, `CUS-29/42/50`; remite a food truck (R6/R7) |
| 18 (19) | Franquicia o independiente | N | 1.300 | 2 · Franquicia frente a Independiente | `CUS-M12…M25`, `CUS-03`, `CUS-14`, `CUS-47` (N-9, N-10) |
| 19 (20) | El plan financiero, el punto de equilibrio y los primeros 90 días | H | 1.500 | 6 · PyG 3 Años · 6 · Punto de Equilibrio · 6 · Canales y Punto Muerto | `CHN-75` · cita de vuelta el IVA del cap. 03 (`CHN-71c`, `CUN-18`) · veredictos en euros |
| A | Anexo normativo fechado: vigencias y lo que se mueve | H | 1.200 | — | `CUN-08` (acrilamida en revisión), `CUN-32`, `CHN-67/68/75`, V-01 |

**Suma: 30.000 palabras** (el epígrafe del IVA pasa del 19 al 03: +100 / −100). Balance: 10 H (01, 02, 07, 08, 09, 12, 14, 16, 19, A), 4 H+N (03, 06, 13, 15), 6 N (04, 05, 10,
11, 17, 18); 7 🔴 (04, 05, 09, 10, 11, 15, 17). **Orden de lectura (SR-09):** 01 · 02 · 03 · 04 Antes de firmar · 05 Humos · 06 Local y hora punta · 07 Maquinaria · 08 Cuánto cuesta abrir · 09 en adelante sin cambios; D21 se sigue cumpliendo (la fusión sigue detrás de Humos). La FAQ y la landing no mencionan ninguna cifra de §3.5.

### 4.2 Bonus 1 — `business-plan-modelo-churreria-chocolateria.docx` (2 bloques, D5)

El caso «La Rueda» con cifras, en el formato que pide un banco: **bloque 1** = resumen ejecutivo (**resultado neto, margen y
punto de equilibrio** del libro 6, defecto B2 de Pastelería) · mercado y plaza · concepto y carta · operaciones (local,
fritura, capacidad, plantilla y turnos); **bloque 2** = plan financiero a 3 años · tesorería y valle · riesgos con escenarios.
≥ 3.500 palabras y **≥ 9 tablas**, coherentes con el libro 6 celda a celda (gate de `documentos.py`).

### 4.3 Bonus 2 — «12 decisiones de apertura resueltas» (4 bloques de 3, D5 y C7)

Cada decisión: contexto · opciones · criterio · **el veredicto de La Rueda con su cifra y su celda** · **el umbral a partir
del cual elegirías lo contrario** · la norma con su id y fecha cuando la hay. `puntos_por_epigrafe` **prohíbe** repetir la
explicación del capítulo de origen; una tabla por decisión.

| Bloque | Decisiones (celda que la resuelve · ids) |
|---|---|
| 1 | **1** Sala o sólo despacho (`2!Variante del Formato` + régimen de `7!Checklist Legal`, con la condición de obra de A4 · `CUN-35`) · **2** Traspaso u obra nueva (`2!Traspaso vs Obra Nueva` a 5 años · `CUS-02`, `CUS-31a-g`) · **3** Equipo completo de 2.188 € o línea separada (`1!Cuello de Botella` · `CUS-32a`, `CUS-33a`, `CUS-34c`) |
| 2 | **4** Gas con instalación receptora o eléctrico (`1!Freidoras, Potencia y Riesgo` · `CHN-48`, `CUN-26`; **sin** la bombona, A6; **riesgo especial o extinción automática: las dos salidas, con su coste en el 2**, SR-11) · **5** Mix propio o preparado comercial (`3!Escandallo por kg de Masa` · `CUS-21`) · **6** Qué preparado compras para la taza y qué dice su etiqueta (`3!Chocolate a la Taza` · `CHN-05`, `CUN-42` · V-06 resuelta, A11) |
| 3 | **7** Ración, docena o kilo (`3!Ración, Docena o Kilo` · `CUS-15/16/17`) · **8** Abrir antes de las 8:00 (`7!Régimen de Apertura y Horario` + `5!Franjas del Día` · `CUN-34`) · **9** Verano: cerrar, carta de verano o ferias (`5!El Verano`, contribución en euros; `6!Escenarios`, resultado con fijos · `CUS-11`; sin media cuota, A3) |
| 4 | **10** Cuánta madrugada asumes tú (`8!Horas del Titular` · `CUN-29`, `CUN-40`) · **11** Freidora dedicada o compartida (`7!Alérgenos y Aceite Compartido` + coste en el 2 · `CHN-33`) · **12** Franquicia o por tu cuenta (`2!Franquicia frente a Independiente` · `CUS-M12…M25`) |

## 5. Lista negra (va ÍNTEGRA, en texto, al `NO_COMUN` del guion como `cifras_ignorar` + `prohibido`)

### 5.1 Prohibiciones de la verificación legal del 3-oct (mandan sobre L3 y sobre la síntesis; copiadas literales de su §6)

1. «La ley te obliga a controlar la acrilamida de los churros» (`CUN-04`, `07`); «cumplimiento acrilamida»; la parte B «a las franquicias» sin las tres condiciones (`CUN-05`).
2. **Cualquier temperatura de fritura del churro** («180 °C», «175 °C»): V-02. Los 175 °C son de patatas.
3. Un tipo de IVA para el chocolate a la taza para llevar, en prosa (`CUN-18`, V-04).
4. «El despacho va por declaración responsable» sin «las obras que requieren proyecto —el conducto a cubierta incluido— siguen necesitando su licencia» (`CUN-35`); «necesitas/no necesitas licencia» sin decir el modelo.
5. Artículos del **RD 199/2010** o de la **Orden 1562/1998** (`CUN-19`, `34`); el **art. 8** de la norma de aceites (`CUN-03`).
6. «Convenio de churrerías», «la categoría de churrero» o «no existe convenio de churrerías» (`CUN-33`, `39`, `V05`).
7. «El churrero que entra a las 4-5 es trabajador nocturno» (`CUN-29`); confundir el plus del convenio con el trabajador nocturno del ET.
8. «Media cuota del 676», cuotas del IAE y la tasa de Ochavillo como orden de magnitud (`CUN-10`, `37`, `CHN-72/73`).
9. Requisitos de humos de Barcelona, Sevilla o Valencia (`CUN-X01`); «el medidor de polares demuestra el 25 %» (`CUN-02`); «la bombona de 15 kg te evita la instalación receptora» para un local (`CUN-28`).
10. «Ni “chocolate a la taza” ni “chocolate”» como regla cierta (`CUN-V06`); «sin gluten» como argumento de carta (`CHN-37`); «carnet de manipulador» (`CHN-69`); «el cucurucho cumple la ley de plásticos» (`CUN-41`).
11. **Cifras:** margen del churro de **85-90 %** (`CUS-01`); **traspasos de 107.000 y 120.000 €** y «anuncios reeditados» (`CUS-31h/i`); el **curso de 290 €** (`CUS-M05`); el **50 %** como margen bruto o atribuido a «una dueña» (`CUS-30`); sueldos de Jooble (`CUS-56`) y personal de Loomis (`CUS-05`); 540 kg/h, «absorbe un 30 % menos / dura el doble», «docena a 12 €», «facturamos 60.000 €», objetivos de franquiciador («150 franquicias»), «Maestro Churrero desde 75.000 €» (lista negra de L4).
12. «No existe ninguna guía de pago» (solo «no encontramos»), «hay N churrerías en España» (`CUS-07`), «verificado contra el BOE» en copy comercial.

### 5.2 Resto de la lista negra

**Base:** `N-1` … `N-21` de `RES §15.1` y las afirmaciones de `RES §15.2`, **copiadas literales al guion**, no por referencia.
**Y además, de la refutación y de las decisiones:**

| ❌ Prohibido | Origen |
|---|---|
| «Margen bruto del churro 85-90 %» y citar `CHS-31` | D6, `CUS-01` |
| `CUS-31h`, `CUS-31i`, **«120.000»** y **«107.000»** (ni como ejemplo); `CUS-31` a secas; **«95.000» como techo de traspaso y `CHS-37b` para cualquier cifra de traspaso** (sí para 74 m² y 910 €/mes, SR-02) | D15, A2 |
| La **media cuota del 676 (o del 675) como salida del verano**, y cualquier cuota del IAE | D14, A3 |
| «El churrero que entra a las 4-5 es trabajador nocturno»; aplicar «sin horas extra» a quien no lo es | D9, A1 |
| «El despacho va sin licencia» o «declaración responsable» **sin la condición de obra** | D13, A4 |
| Filtros a 0,50 m **sin** los 1,20 m de gas o parrilla | A5 |
| La bombona < 15 kg **sin «de utilización móvil»**, o fuera de la variante (c) | A6 |
| Salarios por debajo del SMI 2026 sin semáforo; `CUS-56` (1.343 €/mes, 16.116 €/año, 1.200 € «con experiencia») | D9, A7 |
| «La brecha ×4 entre Granada y Madrid» | A8 |
| Usar el ~50 % como margen bruto del P&L; **el ~50 % atribuido a «una dueña»** (lo declara Javier, gestor de La Artesana, y es «rentabilidad», `CUS-30`) | D6, A9 |
| **El curso de 290 €** como ancla o en la FAQ (`CUS-M05`) | D3, A10 |
| «Con un preparado que no cumple, ni “chocolate a la taza” ni “chocolate”» como regla cierta, y «la carta lo llama así sólo si el preparado cumple el RD 1055/2003» (V-06 resuelta: interpretación B/C, `CUN-V06`; la fórmula es «qué preparado compras y qué dice su etiqueta») | A11, SR-01 |
| El medidor de polares de mano como prueba legal del 25 % | A12 |
| «La parte B de la acrilamida aplica a las franquicias» sin el art. 2.3 | D12, A14 |
| **«Cumplimiento acrilamida»** para el churro; «la ley te obliga a controlar la acrilamida de los churros» | D12 |
| **«Posición 1»** (o «ya ocupamos el primer puesto») como argumento | D20, B2 |
| «Fuera de España no hay demanda» sin el matiz de México | D19, B3 |
| «Carnet de manipulador» · RD 199/2010 como vigente · Orden de Madrid 1562/1998 · «la chocolatería abre a las 6:00» | `RES §15.2` |
| **«No existe convenio de churrerías»** · «la categoría de churrero» | D9, `CHN-93` |
| **Temperatura de fritura del churro** (180-190 °C u otra) — **V-02 resuelta, rama B: sin fuente primaria; los 175 °C son de patatas** | D8, N-20, V-02 |
| Un tipo de IVA para el chocolate para llevar en prosa — **V-04 resuelta, rama B** (sólo celda verde al 10 % con «consulta a tu asesor») | D11, V-04 |
| Absorción, vida del aceite, churros/hora, curva mensual o mix de canales **presentados como dato** (en celda son supuesto declarado; en prosa, FAQ y copy, nunca) | C3, N-20 |
| «Comparativa de aceites» y «este aceite dura el doble» | D4, C5, N-7 |
| La tabla del post «12.000-50.000 €» (también en su `faq:` y su entradilla), los «40.000-60.000 €» de beneficio y «licencias 2.000-6.000 €» | D20, N-3, N-4 |
| «Verificado contra el BOE» en el copy · «100 % legal» · «válido en toda Hispanoamérica» · «AI Chef Pro tiene plan gratuito» | reglas de la casa |
| Veredicto por ratio cuando la pregunta es en euros · mezclar bases de IVA · «desde» como cifra cerrada · precio pedido como cierre · citas de WebFetch como literales o testimonios (N-21) | `RES §15.2` |
| «El cucurucho (de cartón) cumple la ley de plásticos» | `CUN-41`, SR-08 |
| «Facturamos 60.000 €» (puesto de ferias) | `CUS-50` |
| «150 franquicias en 5 años» como dato | `CUS-14` |
| «Maestro Churrero desde 75.000 €» (sólo los 115.000 € de `CUS-M14`, fechados) | `CUS-M14`, SR-20 |
| «No existe ninguna guía de pago» (sólo «no encontramos» / «ninguna de las que hemos leído») · «hay N churrerías en España» | verificación §6.12, `CUS-07` |

## 6. Vocabulario ES / LATAM (D19; equivalencia sólo en la PRIMERA mención de cada documento)

| Concepto | España (forma principal) | Primera mención (LATAM / regional) | Respaldo |
|---|---|---|---|
| El producto | **churro** · **porra** (churro grueso) | tejeringo (8.100) · calentito (1.000) · jeringo (880), una sola vez | medido, `RES §6` |
| El negocio | **churrería-chocolatería** · montar | en México, «poner» | medido |
| La bebida | **chocolate a la taza** | «chocolate caliente» (MX y CL 5.400), **avisando de que no es lo mismo** | medido |
| La máquina | **churrera** · **dosificadora** | «máquina de churros» (1.600/mes en MX y CL: hay demanda de maquinaria, B3) | medido |
| El cálculo | **escandallo** | costeo | heredado |
| El puesto | **puesto** · **caseta** · **remolque** | carrito | propuesta, sin medición |
| El local | **obrador** | — | — |

«Bajera» (Navarra) y «darle a la pala» sólo como color, nunca como término; el reparto geográfico de los sinónimos no tiene
fuente y la regla no depende de él.

## 7. Canales, interenlazado y Resend (cero páginas huérfanas)

### 7.1 Entrantes y salientes

| Origen | Acción | Fichero · línea |
|---|---|---|
| **Hub, los DOS gemelos** | Tarjeta de `comingSoon` → **producto real en posición 1**, badge «✨ Nuevo», `ListItem` en el JSON-LD, precio 65 €; `comingSoon` 21 → 20 (guarda ya existente) | `ProductosDigitalesHubPage.astro:1015` · `src/pages/ProductosDigitales.tsx:998` |
| **Buscador** | Alias `"/guia-churreria-chocolateria": "abrir montar poner una churreria churros porras tejeringos calentitos chocolate a la taza chocolate caliente freidora dosificadora churrera feria caseta puesto franquicia traspaso licencia"`, sin grupo nuevo | `astro-site/src/lib/sinonimos-buscador.json` (junto a `:111`) |
| **`PRODUCT_ALIASES`** | «Cómo Montar una Churrería-Chocolatería» → `/guia-churreria-chocolateria` | `src/lib/linkify-use-case.tsx:29` y `astro-site/src/lib/linkify-use-case.ts:33` (junto a la hermana) |
| **Páginas de rol** | `chocolateria`: esta guía en **2.ª posición**, tras la hermana · `cafeteria-brunch`: entra por la variante (e) | `src/data/use-cases-content.es.ts:3248` · `:2255` |
| **Venta cruzada hermana → esta** | FAQ de la hermana «¿Cubre la chocolatería de taza y churros…?» con enlace (v1.0.1, D7) + `footerLinks` | `guia-chocolateria-obrador.ts:286`, `:349` |
| **Venta cruzada esta → hermana** | Cap. 01 («la bombonería es otro negocio»), aviso de alcance en la primera pantalla de la landing y FAQ 2 | ficha `.ts` y guion |
| **`footerLinks` cruzados** | Desde la hermana, `pack-appcc`, `kit-escandallos`, `plan-negocio-food-truck`, `plan-negocio-cafeteria` y `kit-gestion-personal` | `astro-site/src/data/productos/**` |
| **Rotación general** | Entrada 51 del catálogo: entra en `rotar_productos()` **para lo que se genere desde ahora**; sin reparto retroactivo (`fase8e` sólo inserta) | `src/data/products-catalog.ts` |
| **Plataforma** | Agentes afines «Chocolatería Creativa», «Chocolatero Consultor Pro», «Food Truck AI+» (nombres verificados en `catalogo-hub.json`) | — |
| **Buscador del hub** | `buscador-report.py` con «churr» (pendiente de L5; necesita `ADMIN_PASSWORD` exportada, la de la sesión) | — |

**Salientes de la landing y del `emailBody`**, con `utm_source=landing&utm_medium=cross-sell`: `guia-chocolateria-obrador`
(65 €), `pack-appcc` (14 €, el registro del aceite), `kit-escandallos` (12 €), `plan-negocio-food-truck` (29 €, feria con
vehículo), `plan-negocio-cafeteria` (29 €, variante e) y `kit-gestion-personal` (14 €, el cuadrante semana a semana: lo que el libro 8 no hace, SR-14). Deuda anotada, no de este producto: la página de rol `food-truck` no
vende sus propios productos.

### 7.2 El post propio (D20, B4) — corrección quirúrgica, nunca regeneración

`astro-site/src/content/blog/es/ia-churrerias-guia-completa.md`: (1) **tabla de inversión** (`:53-58` suman 26.000-62.500 € y
`:60` publica 12.000-50.000) → se sustituye por las cifras de la guía con su id (dotación núcleo 4.185,45 € / 8.618,35 € sin
IVA, `CUS-58/59`; traspasos 16.000-19.500 € de barrio y 82.000 € pedidos con sala, `CUS-31a/b`, `CUS-02`) **y también la entradilla `:30` y el `faq:` (`:13`, `:15` y `:19`: la q4 con 4.800 €, 60 % y 88 raciones)**, sustituidas por las cifras con id de la guía o por el método sin cifra; y fuera N-2, N-3 y
N-4; (1 bis) **bloque «punto de equilibrio» `:66-97`**: fuera el personal de 2.200 €/mes (por debajo del SMI con SS), la materia prima contada como fijo y el 60 % aplicado encima; queda el **método** (fijos ÷ contribución por ración, con el ticket **sin IVA**) y la remisión a `6!Punto de Equilibrio`; (2) **banners**, dos pasadas de `scripts/astro-migration/fase8x-sustituir-banner.py`, cada una con su gate de 3 banners:
**pasada 1** `--producto guia-churreria-chocolateria` sustituye `guia-dark-kitchen` (`:64`) y, con `miswiring`, `kit-tareas-bar`
(`:123`) → `guia-chocolateria-obrador`; **pasada 2** con JSON propio de `pack-appcc` sustituye `kit-tareas-restaurante-creativo`
(`:153`); (3) un enlace contextual a la landing en el cuerpo. Sin «posición 1». Después: **purga OBLIGATORIA de `astro-site/.astro`** (el `faq:` se toca siempre y la collection cachea el frontmatter;
el `faq:` tiene 6 preguntas y emite `FAQPage`), `fase8b-regen-lastmod.py`, `fase8d-faq-duplicadas.py --lang es`,
`fase8c-enlaces-vivos.py` y verificación del `FAQPage` en el JSON-LD del `dist` de la nube (no en el `.md`). Piezas nuevas de blog: fuera de este producto.

### 7.3 Resend

- **Lanzamiento:** **13-nov-2026 08:00 UTC**, programable desde el **14-oct** (tope de 30 días). Cola ES programada por API hasta la Taquería (29-oct) el
  3-oct: … Chocolatería 24-oct · Taquería 29-oct; Escandallos 2.1 (3-nov) y Kit Chocolatería 2.1 (8-nov, PR #104) son **huecos reservados**, no programados (programables desde el 4-oct y el 9-oct). **Antes
  de programar: `GET /broadcasts`**; si alguno de los dos de noviembre no está programado, el hueco es el `scheduled_at` más
  tardío + 5 días. Borrador con sufijo «— PROGRAMAR 13-nov», saludo «Hola, colegas», negro #111 + dorado #FFD700; recrear =
  GET → leer el asunto → DELETE → POST. Prueba a John con `--test` (`scripts/productos-digitales/emails/resend-broadcast.py`).
- **Hermana v1.0.1 (D7): UN solo correo, 18-nov-2026 08:00 UTC** (programable desde el 19-oct), detrás del lanzamiento porque
  anuncia, además de la corrección, el enlace cruzado a esta guía, que sólo existe tras publicarla. A los compradores: «la v1.0.1
  ya está en tu dashboard, sin coste».
- Los dos huecos se anotan en el handoff y en `CALENDARIO-V2-SEMANAL.md`.

## 8. Capa de producto, gates y LIVE (F3)

### 8.1 Ficheros a tocar (mapa de la hermana con `GuiaChurreriaChocolateria` / `GUIA_CHURRERIA_CHOCOLATERIA`)

| # | Fichero | Qué se añade |
|---|---|---|
| 1 | `astro-site/src/data/productos/guias/guia-churreria-chocolateria.ts` | Ficha `GuiaData`: `slug`, `stripeEnvKey`, `seo`, `hero` (aviso de alcance y declaración en negativo arriba), `pricing` **sin `priceOld` ni `discountBadge`**, imágenes, `grid`, **`testimonials.items: []`**, `why`, `author`, `bonus`, `buyBox`, `guarantee`, **`faqs`: las 12 de §8.3**. Páginas: **las MEDIDAS** |
| 2 | `astro-site/src/pages/guia-churreria-chocolateria.astro` | Wrapper fino; env **literal** `import.meta.env.VITE_STRIPE_PAYMENT_LINK_GUIA_CHURRERIA_CHOCOLATERIA`; `whatsapp={false}`; `locales={['es']}`; las 3 puertas cripto las monta la plantilla |
| 3-5 | `…-access.astro` · `…-library.astro` · `islands/library/GuiaChurreriaChocolateriaLibraryIsland.tsx` | **GENERADOS** por `scripts/astro-migration/fase5-generate-zona-app.py`. No editar a mano |
| 6 | `astro-site/src/lib/zona-app.ts` | Entrada en `PRODUCTOS_ZONA_APP[]` (storageKey `guia-churreria-chocolateria-jwt`, nombre corto del diálogo cripto). 52 → 53 |
| 7-9 | `src/App.tsx` · `src/pages/GuiaChurreriaChocolateriaAccessGate.tsx` · `…Dashboard.tsx` | 2 rutas; `SECTIONS[]` = **Guía 2 · Herramientas 8 · Bonus 3**; exactamente 1 `<title>` sin comillas dobles |
| 10 | `src/data/products-catalog.ts` | `RAW['guia-churreria-chocolateria']`. **50 → 51.** Sin comentarios entre `description: {` y `es:` |
| 11-12 | `netlify/shared/payment-links.ts` · `product-prices.ts` | **GENERADOS** (`sync-payment-links.py`, `sync-product-prices.py`). 52 → 53 |
| 13-16 | Las 4 functions | `PRODUCTS` en `verify-purchase.ts`, `resend-access.ts`, `admin-generate-access.ts` (+ `emailSubject/Title/Body/Cta`) y **`PRODUCT_FILES` en `get-download-urls.ts` con 13 claves**: `guia-pdf`, `guia-docx`, `bonus-decisiones-pdf`, `bonus-decisiones-docx`, `business-plan-docx` y los 8 xlsx → `/dl/guia-churreria-chocolateria/…` |
| 17-18 | `src/data/productos-digitales-config.ts` · `src/data/productos-changelog.ts` | Espejo del mapa de ficheros; changelog **v1.0 «Lanzamiento»** |
| 19-20 | Hub ×2 | §7.1 |
| 21-25 | Buscador · `PRODUCT_ALIASES` ×2 · `footerLinks` · `src/pages/AdminGenerateAccess.tsx` (desplegable, 51) · páginas de rol | §7.1 |
| 26-27 | `astro-site/public/lovable-uploads/ai-gallery/guia-churreria-{hero,1,2,3,4,5}.jpg` + `astro-site/public/og-guia-churreria-chocolateria.jpg` · `astro-site/public/dl/guia-churreria-chocolateria/**` | 7 imágenes con la skill `generate-images` (la OG no se repite en el cuerpo; sin texto legible ni marcas) · 13 descargables **trackeados en git** |

**Orden:** ficha con `schema.price` → `sync-product-prices.py` → **John crea el Payment Link** → env var en Netlify →
`sync-payment-links.py` → functions → `fase5-generate-zona-app.py` → hub, alias, rol, post → commit + push → deploy en la nube →
gates LIVE. **Hermana v1.0.1 (§8.4) antes de activar la venta cruzada.**

### 8.2 Batería de gates, en orden

| Gate | Comando | Qué asegura |
|---|---|---|
| Datos | `/usr/local/bin/python3 scripts/productos-digitales/guia-churreria/datos_ejemplo.py` (`comprobar()`) | Cuatro orígenes, cero `None` en C3, sumas de dotación y coeficientes, ids prohibidos (`IDS_PROHIBIDOS`) ausentes, huecos de cobertura = 0 en La Rueda, `CRUCES` y `ORDEN_RELLENO` declarados |
| Caché y libros | `inject_cache.py` + `data_only` de cada fórmula + `guia-churreria/gate_libros.py` | Prohibidas, constantes, DV, formatos, metadata, **`auditar_ciclos` + una fila de CUADRE por celda cruzada**, sin fondo en el 2 |
| Celdas verdes vacías = 0 | sobre `build/mapa-*.json` | Ninguna entrada depende de un producto que el comprador no tiene |
| Postproceso | `postprocess-transversal.py <ruta> --dry-run` | A4, metadata, bio, línea de versión |
| Guion | `guia-churreria/verificar_guion.py` | 0 referencias rotas, 0 vacías, 0 ids inexistentes (`RX_ID` ampliado de §2.3: `CUN`/`CUS`/`FC-IVA`, con sufijos `M`/`V`/`D`) y 0 ids de `IDS_PROHIBIDOS`, ±3 % de `palabras_objetivo`, `prohibido` nunca vacío |
| Solape | `guias-v2_0/solape.py <dir_txt>` | ≤ 1 par por encima del umbral; con 2 o más, se regenera el capítulo implicado; **y cada capítulo H contra el `txt/` homólogo de `guia-chocolateria-obrador`** (si supera el umbral se reescriben los `puntos_por_epigrafe`, no el texto; SR-21) |
| Documentos | `guias-v2_0/documentos.py --producto guia-churreria-chocolateria --saltar-generacion` | Gates de familia en verde y páginas medidas (≥ 80 / ≥ 20) |
| **Refutación de documentos (D23)** | 1 agente Opus con 3 lentes (rigor · negocio · producto) + estos gates; 2.ª ronda sólo sobre bloqueantes | Sin capa de fixer aparte si la 1.ª ronda no tiene bloqueantes |
| Censo y no latinos | `censo-entregables.py --only guia-churreria-chocolateria --fail` · `gate-no-latinos.py --only guia-churreria-chocolateria` | 0 defectos · 0 ocurrencias |
| Páginas prometidas | `paginas-gate.py --only guia-churreria-chocolateria` | Lo anunciado nunca supera el `page_count` real |
| Nombre | script propio | `name.es` = `<h1>` = `title` = banner = asunto del correo (D1) |
| **Reapertura de anuncios (SR-10)** | reabrir `CUS-M06` y `CUS-02` (navegador de Windows o captura de John) | 0 cifras de Milanuncios sin releer en copy; si no se pueden releer: ancla sólo con los 12.000 € y FAQ 3 sin cifra |
| FAQ | `clasifica()` de `fase8d-faq-duplicadas.py` + `grep` de §5 sobre la ficha | Cero PARECIDA/DEFINICION (vigilar 4/5 y 8/9) y **ninguna respuesta con una cadena de la lista negra** |
| Flujo post-pago | `gate-flujo-postpago.py --offline --only guia-churreria-chocolateria` · `fase5-generate-zona-app.py --check` · `grep -c "'guia-churreria-chocolateria'" netlify/functions/*.ts` (≥ 1 en las 4) | Cruces zona-app ↔ functions ↔ dashboard; descargas trackeadas; sin drift |
| Robots · WhatsApp · Miselup · DataFast | `scripts/astro-migration/robots-gate.py --live` · `whatsapp-gate.py` · `miselup-gate.py` · `datafast-gate.py` | Landing rastreable y `-access`/`-library` bloqueados · 1 botón en la landing y 0 en `-library` · tarjeta Miselup una vez en landing y dashboard · cargador DataFast una vez |
| Marketing | `fase6-gate.py https://aichef.pro/guia-churreria-chocolateria` | SEO nativo server-side |
| **LIVE** | `gate-flujo-postpago.py --only guia-churreria-chocolateria` | Landing 200 con `buy.stripe.com`, `-access` y `-library` 200, **13 descargas del mismo tamaño que en disco**, **sección E-f cripto** (3 `data-crypto-open` + 1 `<dialog>`) + curl al checkout con email `qa-…@aichef.pro` y purga del pedido |

Los gates LIVE leen el registro **local**: comprobar el commit local antes de fiarse. Si hay otra sesión en el directorio,
`git worktree`, nunca checkout.

### 8.3 La FAQ de compra: las 12 de `RES §14`, con estas correcciones

| # | Cambio |
|---|---|
| 1 | «…**ninguna de las que hemos leído** desglosa el CAPEX…»; nunca «ninguna desglosa» (verificación §6.12: sólo «no encontramos») (SR-15) |
| 3 | «Para el oficio hay cursos presenciales **de hasta 1.290 € en Madrid**» (A10) — **sólo si `CUS-M06` se relee antes de publicar; si no, «hay cursos presenciales de pago en Madrid», sin cifra** (SR-10) |
| 4 | **Sin «Verificado:»** al abrir. «…la maquinaria con precio publicado va de ~4.200 € (despacho) a ~8.600 € (local con sala), sin IVA, y **no incluye obra de humos, cafetera, vitrina ni TPV**; los traspasos que se piden hoy van de unos **16.000 €** (churrería de barrio) a unos **82.000 €** (con sala, en Madrid; precio pedido y negociable)» (A2, D15, SR-02, SR-15) |
| 5 | Pregunta → «**¿Es rentable una churrería?**»; respuesta con los dos márgenes y su definición, y el punto de equilibrio en raciones/día con tu personal real; **el «poquito más del 50 %» se atribuye al gestor de La Artesana, nunca a «una dueña»** (C6, D6, SR-05) |
| 6 | Pregunta → «**¿Los Excel parten de mi receta o de una receta vuestra?**» (C6) |
| 7 | «…la **actividad** de un despacho para llevar hasta 750 m² va por declaración responsable; **las obras de la salida de humos, si necesitan proyecto, van con su licencia y su técnico**; con mesas y consumo en el local, manda tu ayuntamiento» (A4, D13) |
| 11 | La respuesta de la hermana (`guia-chocolateria-obrador.ts:290`): los Excel se recalculan igual en Google Sheets, LibreOffice y Numbers porque Sheets entiende esas funciones; no usar `INDIRECT`, `OFFSET`… es una **convención interna** de la casa, **sin la causalidad de Sheets** (SR-15) |
| 12 | Marco legal español; adaptación como servicio, sin promesa (B3) |

JSON-LD: `Product` sin `aggregateRating` ni `review` + `FAQPage` + `BreadcrumbList`.

### 8.4 La v1.0.1 de la hermana (D7, con B5) — una sola versión, un solo correo

En `guia-chocolateria/`, regenerando por generador (nunca a mano): (1) `datos_ejemplo.py:2301` → fuera el 85-90 % de
`calculadora-capex-chocolateria.xlsx!Variante del Formato` y del P&L, y la frase de la pág. 9 de la guía; (2) veredicto de
`plan-financiero-3-anos-chocolateria.xlsx!PyG 3 Años!B68` **en euros** (hoy dice «restan» cuando el neto sube de 17.268,87 € a
20.043,54 €); (3) `PyG!C58` deja de ser «margen bruto 0,5»: celda verde con el margen sobre materia prima de
`3!Los Dos Márgenes` de La Rueda y la nota «véase la Guía de Churrería-Chocolatería, libro 3» (A9, B5); (4)
`Variante del Formato!E38-E41` (churrera, freidora, extracción, campana) y `!E47` (Maestro Churrero) con su id `CUS-*` o la
misma remisión (B5); (5) retirar la nota-puente del cap. 12 (el Kit de Tareas Chocolatería 2.1 ya está, PR #104); (6) enlace
a esta guía en las FAQ `guia-chocolateria-obrador.ts:286` y `:349`; (7) `CHS-31` marcado como refutado en el JSON común
(remite a `CUS-01`) **después** de regenerar la hermana. Changelog **v1.0.1**; gates de la hermana (`gate_libros.py`,
`censo-entregables.py`, `gate-flujo-postpago.py --only guia-chocolateria-obrador`) en verde; correo del 18-nov (§7.3).
**Fuera de este producto:** la deuda del Pack APPCC 09 (D8) y la de `kit-tareas-food-truck/04` (R10), anotadas en el handoff.

## 9. Presupuesto por fase (M de tokens de subagentes; D22: 0,162 M por bloque como suelo)

| Fase | Partida | Base | M |
|---|---|---|---|
| F1 | Research (5 lentes + síntesis) | medido | **2,11** |
| F1 | Refutación del research | estimado, **a sustituir por el consumo medido de los journals antes de reportar a John** (D22, SR-19) | 0,25 |
| F1 | Verificación legal V-01…V-06 | estimado (produjo 202 fichas con gate de literalidad); **a sustituir por el consumo medido** (SR-19) | 0,15 |
| F1 | Fichas `CUN`/`CUS` + fusión al JSON común | molde de la hermana; **a sustituir por el consumo medido** (SR-19) | 0,15 |
| F1 | Esta SPEC + refutación (≤ 2 rondas) | molde de la hermana | 0,30 |
| F1 | `datos_ejemplo.py` + `comprobar()` | estructura calcada | 0,30 |
| | **Subtotal F1** | | **3,26** |
| F2 | 8 libros (§2.5) | 2 H (2, 6) × 0,25 + 4 H+N (1, 3, 5, 7) × 0,27 + 2 N (4, 8) × 0,32 | 2,22 |
| F2 | Refutación de libros | 1 opus + fixer sonnet + `inject_cache`/`mapas`/`gate_libros` | 0,50 |
| F2 | Guion | 19 caps + anexo + 2 bonus, 10 capítulos calcados | 0,55 |
| F2 | **Redactores** | **26 bloques × 0,162** (13 tandas de 2, D24) | **4,21** |
| F2 | Verificación legal de los 7 🔴 + `documentos.py` | sonnet + opus | 0,35 |
| F2 | Refutación de documentos | 1 ronda Opus de 3 lentes + 2.ª sólo bloqueantes (D23) | 0,45 |
| | **Subtotal F2** | | **8,28** |
| F3 | Capa de producto (ficha, zona app, functions, catálogo, hub ×2, 7 imágenes, alias, rol, email) | sonnet + opus | 0,65 |
| F3 | Hermana v1.0.1 (§8.4) | 2 xlsx + guía + ficha | 0,20 |
| F3 | Post (§7.2) | 2 pasadas + corrección quirúrgica | 0,10 |
| F3 | Gates, LIVE y Resend | Fable | 0,20 |
| | **Subtotal F3** | | **1,15** |
| | **TOTAL central** | | **12,69 M** |

**Comparación sin adornos.** **+2,69 M (+27 %) sobre el techo nominal L de 10 M** y **0,31 M por debajo de la parada de
13 M**. Queda por encima de los ≈ 11-12 M de D22 porque F1 ya cuesta 3,26 M medidos y estimados (D22 no tenía la F1 contada).
**Banda alta: ≈ 14,1 M**, la que sale calibrando los redactores **por palabra** (40.100 palabras × 141 tokens = 5,65 M en vez de
4,21 M): rebasaría la parada. **Regla de control para que no pase:** tras las **dos primeras tandas de redactores** (4
bloques) se mide el consumo real; si la media supera **0,175 M por bloque**, se recortan un 10 % las palabras de los capítulos
H aún no escritos (≈ −0,3 M) y la 2.ª ronda de refutación de documentos se limita a los bloqueantes; si aun así la
proyección pasa de 13 M, **se para y se reporta** (política de 3 fases). Ya aplicadas desde el diseño: BP en 2 bloques, 05+09
fundidos, bonus en 4 bloques, una ronda de refutación de documentos y guion bajado de 44.300 a 40.100 palabras.

**Térmica:** `istats cpu temp` antes de cada tanda de python/PyMuPDF/openpyxl; ≥ 63 °C → esperar 60 s; vigilante
`scripts/termica/watchdog-termico.sh` comprobado con `pgrep` entre fases; un fichero cada vez; `/usr/local/bin/python3`; sin
builds ni navegador ni Playwright en local; deploy en la nube. F2 en el Mac, máximo 2 agentes a la vez (D24): más reloj, cero
riesgo térmico.

## 10. Lo que queda para John

1. **Payment Link de Stripe (65 €)** y la env var `VITE_STRIPE_PAYMENT_LINK_GUIA_CHURRERIA_CHOCOLATERIA` en Netlify, scope
   `builds`, todos los contextos. Descripción propuesta, en prosa y sin «verificado contra el BOE»: *«Para quien va a montar una
   churrería-chocolatería en España: 19 capítulos en PDF y DOCX editable, 8 herramientas Excel con fórmulas vivas —producción
   en hora punta y local, inversión, escandallo del churro y de la taza, aceite, temporada y ferias, plan financiero a 3 años,
   licencias y turnos de madrugada—, un business plan relleno y 12 decisiones de apertura resueltas. Pago único con acceso de
   por vida.»*
2. **Sólo informativo (D22, no requiere respuesta):** el producto completo se estima en **12,69 M** (banda alta ≈ 14,1 M), por
   encima del techo nominal de 10 M y por debajo de la parada de 13 M, con la regla de control de §9.
3. Opcional, como en la hermana: la **compra de prueba real** tras el LIVE (o `aichef.pro/admin/generar-acceso`).

**Estado: SPEC v1.1 del 2026-10-03, con la ronda 1 de refutación aplicada (21 hallazgos, §1.C) y las verificaciones V-01…V-06 cerradas. Queda una ronda de refutación como máximo (las tres altas y SR-07). Siguiente paso de F1: `datos_ejemplo.py` con su gate (D25).**

Via: Claude Code
