# Roadmap del blog neerlandés — los 12 primeros posts

> Escrito el 2026-08-16 a partir del keyword research de Google.nl (DataForSEO,
> `--pais 2528 --idioma nl`), con spot-check de Flandes (`--pais 2056`):
> ~190 keywords medidas y ~25 SERP en vivo. Datos crudos en
> `.work/research-blog-nl.md` y `.work/research-nl.json` (gitignorados, solo en
> el VPS). Método heredado de `ROADMAP_BLOG_ITALIANO.md`.
>
> **Todos los volúmenes están MEDIDOS, no estimados.**
>
> ⚠️ **El blog nl NO existe aún**: antes del post 1, crear el árbol `/nl/blog/`
> clonando la fase 9 italiana. Recordar la lección del piloto NL de fase10 (el
> spoke que salió en dialecto limburgués): revisar los H1 de todo lo emitido.

## Las reglas que salieron del research (específicas de Países Bajos)

**1. La palabra COMPUESTA gana ×19,7.** `allergenenlijst` 590 > `allergenen
lijst` 260 > `lijst allergenen` 30. El compuesto neerlandés va pegado en title
y H1, siempre. (Confirmación inversa: `brigade keuken` sin datos, pero
`keukenbrigade` compuesta sí mide.)

**2. La DIÉRESIS parte la keyword en dos series NO agrupadas**: `hygiënecode`
260 + `hygienecode` 210 = 470/mes repartidos. El cuerpo del post cubre las dos
formas.

**3. «betekenis» gana a «wat is» ×2-3** (`haccp betekenis` 1.300 vs `wat is
haccp` 590; `mise en place betekenis` 590 vs `wat is mise en place` 170). La
forma nominal, no la interrogativa.

**4. El verbo gana al sustantivo ×26** (`moleculair koken` 260 vs `moleculaire
keuken` 10) y el orden vale ×5 (`chocolade tempereren` 880 vs `tempereren
chocolade` 170) — pero no es universal (`haccp 7 principes` ≡ `7 principes
haccp`, agrupadas): medir cada caso.

**5. ⚠️ EL CLÚSTER DE COSTES NO EXISTE EN NL.** `food cost`/`foodcost` 40/mes
(serie idéntica, agrupadas — en Italia eran 1.000), `horeca calculatie` 10,
`receptcalculatie` y OCHO términos más del clúster de gestión sin datos. Del
clúster B solo sobrevive `menu engineering` (340 sumando la variante con
guion, series distintas). **Un pilar de escandallo aquí sería escribir para
nadie.**

**6. Un préstamo de cocina puede ser una MARCA registrada**: «Mise en Place»
es la mayor ETT de hostelería del país (6 de 9 orgánicos + local pack). El
préstamo NO se descarta (el error italiano, invertido): se CUALIFICA — con
`betekenis` la marca cae al puesto 8 y quedan 590/mes LOW.

**7. La ley no se teclea por su número** (a diferencia de Italia): `allergenen
etikettering` sin datos; la demanda entera va por `allergenenlijst` (590) y
`14 allergenen` (210). El Reg. 1169/2011 se cita dentro, jamás en el título.

**8. El PAA vuelve EN INGLÉS si la cadena es inglesa** (dry aging, chefgpt):
la FAQ se saca del PAA de una variante neerlandesa del clúster.

**9. FLANDES suma +25-55 % en técnica y alérgenos, pero NO en lo regulatorio**:
`hygiënecode` se hunde a 30/mes en BE porque allí manda el **autocontrolegids
del FAVV**, no la NVWA. Los posts de alérgenos y técnica viajan; los de
HACCP/hygiënecode necesitan un párrafo FAVV explícito o no viajan.

**10. Los mayoristas y la patronal hacen contenido, y bien** (Sligro, HANOS,
Unilever Food Solutions, KHN, SHO — a menudo con herramienta gratuita): el
contenido delgado no entra en este mercado. Y `gastronomixs` (4.400/mes de
marca) prueba que el chef neerlandés SÍ busca contenido técnico online: el
problema nunca es la audiencia, es la keyword secuestrada por un retailer o
una ETT.

## Lo que NO hay que escribir (medido y refutado — suman >80.000/mes)

| Keyword | Volumen | Por qué se descarta |
|---|---|---|
| `nvwa` | 14.800 | Navegacional + EMPLEO («salaris bij de NVWA») — el caso ASAE portugués, calcado |
| `voedselvergiftiging` | 14.800 | Médica y de paciente (thuisarts, farmacias) |
| `google reviews` | 14.800 | Soporte de Google; y nlapp NO tiene agente de reseñas/SEO local |
| `vegan restaurant` | 12.100 | Comensal con local pack; el lado operador: `plantaardig menu` 10 |
| `foodtruck` | 9.900 | Alquiler y compraventa (Marktplaats, bodas); `foodtruck starten` 50 |
| `glutenvrij` | 9.900 | Paciente celíaco; el lado restaurador vive en allergenen (1.900) |
| `sous vide` | 8.100 HIGH | Consumidor y venta de equipo (ah.nl, souvy). Sección de kooktechnieken, no post |
| `koelkast temperatuur` | 5.400 | La RUEDA de la nevera de casa (Coolblue, «stand 2»); `temperatuur koelkast horeca` sin datos |
| `fermenteren` | 4.400 | Salud intestinal y chucrut casero. Fermentus sin SERP propia en NL |
| `mise en place` (desnuda) | 4.400 | LA ETT. Se ataca solo `betekenis` (candidato 5) |
| `sous chef` | 3.600 | Salarios y vacantes (+ un restaurante homónimo) |
| `haccp certificaat` / cursus | 2.400 + 720 | Formación de pago (69 €); el HALLAZGO se absorbe en el pilar: el certificado ya NO es obligación legal, la hygiënecode sí |
| `alcoholwet` / exploitatievergunning | 2.400 + 1.300 | Texto legal + centro de adicciones; sin agente de licencias |
| `bouillon maken` / `demi glace` | 1.900 + 1.300 | Receta casera y COMPRA de bote (Knorr Professional); `moedersauzen` 30 — el pilar de fondos NO se sostiene en NL |
| `dry aging` | 1.300 HIGH | Venta de carne; término local 10/mes; PAA en inglés |
| `menukaart maken` | 1.000 HIGH | Canva, imprentas y menús de BODA |
| `voedselverspilling` | 1.000 | Medioambiental (la trampa italiana); `derving` es diccionario y antihurto retail. Mermas GenCal sin keyword en NL |
| `kostprijs berekenen` | 480 | Contabilidad de pyme (Rabobank, fiscal) |
| `qr menukaart` | 70-110 | Seis SaaS con plan gratis. Aviso: topfood.app ya cruza QR+allergenen — el pilar de alérgenos debe defender su ángulo de cumplimiento |
| `chefgpt` | 170 | Apps de contar calorías; PAA en inglés. Clúster IA: 13 de 30 términos sin datos — **la IA es el CÓMO de cada post, nunca el tema** |

## Restricción de producto

`nlapp.aichef.pro` sirve **53 agentes** (censo `.work/nlapp-agentes.txt`). Sin
hotel, consultoría, social ni SEO local. Agentes sin demanda de búsqueda
propia en NL: Fermentus, Mermas/derving, VegChef, Food Truck AI+ (50/mes) — se
sirven por enlace interno. Productos digitales ES-only → sin banners;
conversión al agente de nlapp con UTM. Ganchos verificados contra el censo.

## Los 12 posts, en orden de publicación

| # | Keyword objetivo | Clúster/mes | Dific. | AIO | Agente gancho | Tipo |
|---|---|---|---|---|---|---|
| 1 | `allergenenlijst` (maken, horeca) | 1.900 | BAJA | sí | Allergenen ID | **PILAR** |
| 2 | `14 allergenen` | 210 | BAJA-MEDIA | sí | Allergenen ID | satélite |
| 3 | `kruisbesmetting` (prof. keuken) | 720 | MEDIA | sí | Allergenen ID | satélite |
| 4 | `hygiënecode` + `hygienecode` (vs HACCP) | 850 | BAJA-MEDIA | **NO** | — plataforma | **PILAR** |
| 5 | `haccp betekenis` / `haccp horeca` | 2.850 | MEDIA | sí | — plataforma | **PILAR** |
| 6 | `haccp lijsten` | 630 | MEDIA-ALTA | sí | — plataforma | satélite |
| 7 | `snijtechnieken` (brunoise, julienne, con medidas) | **4.750** | BAJA | **NO** | Gastro Lexicon | **PILAR** |
| 8 | `kooktechnieken` (+ blancheren 4.400 de cola) | 430 + cola | BAJA | no | Gastro Lexicon | satélite |
| 9 | `mise en place betekenis` | 850 | BAJA | sí | Executive Chef Pro | satélite |
| 10 | `menu engineering` (+ `menu-engineering`) | 340 | BAJA-MEDIA | no | Pro Restaurant Manager | satélite |
| 11 | `chocolade tempereren` (zonder marmer) | 1.050 | MEDIA | sí | Creatieve Chocolaterie | satélite |
| 12 | `moleculair koken` | 320 | BAJA-MEDIA | sí | Sosa Ingredients Agent | satélite |

**Suma direccionable: ~15.000/mes** + el uplift flamenco (+25-55 %) en
técnica y alérgenos.

### Por qué en ese orden

- **1-3 (alérgenos)**: la SERP de `allergenenlijst` es la ÚNICA 100 % B2B del
  mercado (NVWA, SHO, Sligro — ni un resultado de consumidor) y su PAA pide
  literalmente «Hoe maak ik een allergenenlijst?» — el output exacto de
  Allergenen ID. El satélite 2 da la tabla canónica (el ruido clínico del PAA
  no entra en la FAQ); el 3 es el puente que la propia NVWA ya une
  (kruisbesmetting de alérgenos, #2 orgánico).
- **4 `hygiënecode`** es el post más neerlandés posible, sin gemelo en ningún
  blog del grupo: la figura legal que sustituye al plan HACCP propio. «Wat is
  het verschil tussen HACCP en hygiënecode?» aparece 3 veces en un solo PAA, y
  es la única SERP relevante SIN AI Overview — hueco de respuesta directa. El
  mito a desmontar (munición del AI Overview de `haccp certificaat`): el
  certificado ya no es obligación legal; trabajar según una hygiënecode
  aprobada, sí.
- **5-6 (HACCP)**: la forma ganadora es `betekenis` (1.300); el título lleva
  «horeca» porque la mitad del top de la genérica es sanidad/residencias
  («HACCP in de zorg»). El 6 entra solo por la puerta del PAA («Hoelang moet
  je HACCP lijsten bewaren?») — contra los ZIP gratuitos de la KHN no se
  compite por la descarga. Si hay que podar, el 6 cae primero.
- **7-8 (técnica)**: `snijtechnieken`+`brunoise` es el mayor volumen limpio
  del research (4.750, sin AI Overview, con un fabricante de CALZADO laboral
  en el top 5 midiendo el vacío) — se gana con la tabla de medidas en mm.
  `kooktechnieken` arrastra la cola gorda (blancheren 4.400, pocheren 880,
  confijten 590) como secciones; sous vide vive aquí como sección, no como
  post.
- **9-12**: mise en place cualificada (la ETT cae al 8º puesto); menu
  engineering como único superviviente del clúster B (featured snippet en
  manos de un fabricante de snacks: arrebatable); chocolade tempereren por el
  ángulo «zonder marmer» (la cocina de restaurante, no la obradora — sin
  pelear con los reposteros de TV); y moleculair koken cierra con el mejor
  encaje de agente tras Allergenen ID (la SERP vende kits de los texturizantes
  que Sosa cataloga: el diferenciador es «qué aguanta un servicio real»).

## Reglas de ejecución

1. **Antes del post 1: crear el árbol `/nl/blog/`** (clonar fase 9 IT). Mirar
   los H1 de todo lo emitido (lección del limburgués de fase10).
2. `modDate` + `fase8b-regen-lastmod.py`; purgar `.astro` y **verificar
   recuento + URLs en `dist`** (lección 2026-08-15).
3. Compuestos pegados en title/H1 (regla 1); diéresis: cubrir ambas formas en
   el cuerpo (regla 2); datos normativos FIJADOS (Warenwet, Reg. CE 852/2004,
   Reg. 1169/2011, hygiënecodes aprobadas) y verificados; separar LEY de
   PRAKTIJK; sin sanciones ni importes.
4. FAQ desde el PAA de variantes neerlandesas (regla 8); fundir formulaciones
   o salta `fase8d-faq-duplicadas.py --lang nl`.
5. Los posts de alérgenos y técnica llevan párrafo FAVV/Flandes cuando aporte
   (+25-55 % de mercado); los de hygiënecode son NL-only por naturaleza.
6. Sin banners (ES-only). Conversión → agente de nlapp con
   `utm_source=blog&utm_medium=cta&utm_content=<slug>`.
7. `dataforseo.py` con `--pais 2528 --idioma nl` SIEMPRE (Flandes: 2056 para
   spot-checks).
8. Imágenes: textos visibles EN NEERLANDÉS, verificadas a ojo.

## Suplentes y semillas futuras

- `bavarois maken` (1.000 LOW, SERP sin verificar) — posible satélite de
  patisserie con Creatieve Patisserie.
- `gastronomixs` como referente de formato: su éxito de marca (4.400/mes)
  valida el contenido de componentes/técnica para chefs en NL.
- `desem brood` (1.000 LOW) — revisar SERP antes de tocarlo (riesgo de público
  casero, como fermenteren).
