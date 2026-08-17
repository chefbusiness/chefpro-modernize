# Roadmap del blog francés — los 14 primeros posts

> Escrito el 2026-08-16 a partir del keyword research de Google.fr (DataForSEO,
> `--pais 2250 --idioma fr`): 6 clústeres, ~185 keywords medidas y 40 SERP en
> vivo. Datos crudos en `.work/research-blog-fr.md` y `.work/research-fr.json`
> (gitignorados, solo en el VPS). Método heredado del research italiano del
> 2026-08-08 (`ROADMAP_BLOG_ITALIANO.md`).
>
> **Todos los volúmenes están MEDIDOS, no estimados.** Donde DataForSEO no
> devolvió dato, pone «sin datos».
>
> ✅ **Árbol `/fr/blog/` creado el 2026-08-16** (commit `4ebb928`): clon de la
> fase 9 italiana con segmentos nativos `categorie`/`page`, 4 categorías por
> clúster, RSS fr y gates `--lang fr`. **Post 1 publicado el mismo día**
> (`tableau-des-allergenes`, commit `1be3f01`); agente verificado en frapp:
> `pickaxe-project-45` (ID Allergènes).

## Las reglas que salieron del research (específicas de Francia)

**1. La trampa estructural: el vocabulario de cocina, en su casa, es palabra
común.** La inversa exacta de la lección italiana. Medido en seis casos: `mise
en place` (2.900) es SERP de diccionario y gramática, `carte allergènes` (2.900)
es el **mapa de polen**, `julienne` (6.600) es un pescado, `mirepoix` (40.500)
es un **pueblo de Ariège**, `parage` (4.400) es el corte de cascos de caballo,
`ia cuisine` (260) son muebles de cocina. **Cualificar SIEMPRE y mirar la SERP
hasta en el término más de oficio.**

**2. El orden de palabras multiplica hasta ×20.** `haccp c'est quoi` 1.000 vs
`c'est quoi haccp` 210 vs `qu'est ce que le haccp` 50. La interrogación
pospuesta gana siempre.

**3. El artículo definido penaliza sin excepción medida.** `14 allergènes` 590
vs `les 14 allergènes` 170 (×3,5) · `7 principes haccp` 210 vs `les 7 principes
haccp` 50 (×4,2) · `sauces mères` 210 vs `les sauces mères` 20 (×10). El título
puede llevar «les»; el H2 que persigue la keyword, no.

**4. Los acentos a veces agrupan y a veces NO — se decide mirando la SERIE
mensual, no el volumen.** `plan de maitrise sanitaire` (1.000) y `plan de
maîtrise sanitaire` (210) tienen series DISTINTAS → no agrupadas, la grafía sin
circunflejo gana ×4,8. En cambio `haccp definition`/`définition`,
`lacto fermentation`/`lactofermentation` y `sauces mères`/`sauce mère`
comparten serie exacta → agrupadas, se escribe la que mejor lea.

**5. Anglicismo vs local: se invierte respecto a Italia y se mide término a
término.** `food cost` solo vale 260 aquí (1.000 en Italia): el coste se busca
como **`fiche technique`**. Pero `menu engineering` (170) aplasta a `ingénierie
des menus` (sin datos) y `dry aging` (590) gana ×8 a `maturation de la viande`.
Y `sécurité alimentaire` (1.000) significa *food security* (Banque mondiale,
FAO en el top): el término del oficio es `hygiène alimentaire`.

**6. Las siglas administrativas son la mina B2B francesa** — intención 100 %
profesional, sin equivalente en el corpus ES/IT del grupo: **PMS** (1.530),
**GBPH** (880), **ADO** (90), **DLC/DDM** (580 en variante comparativa). Son
contenido nuevo, no traducciones.

**7. «Quelles sont les X règles d'hygiène ?» es la pregunta nacional**: aparece
en el PAA de SEIS SERPs distintas (X = 3, 4 o 5 según la consulta) y nadie la
responde de forma citable. Con AI Overview presente en casi todo el clúster A,
quien la conteste en dos frases se lleva la cita.

**8. Competencia HIGH en higiene = venta de cursos.** Las dos únicas HIGH del
clúster A son `formation haccp` (9.900) y `formation hygiène alimentaire`
(2.900): la formación de 14 h es obligatoria en Francia y es la subasta de otro
negocio. No se toca.

**9. El clúster IA es CERO salvo la marca.** Diez términos de «IA para
restauración» sin datos. Lo único vivo: **ChefGPT, 2.620/mes sumando las dos
grafías (series distintas) y ×4 en seis meses** — se ataca por marca y
comparativa («avis», «alternative»), jamás por concepto.

## Lo que NO hay que escribir (medido y refutado)

| Keyword | Volumen | Por qué se descarta |
|---|---|---|
| `mirepoix` | 40.500 | El pueblo de Ariège (top_sights, «les plus beaux villages»). La acepción culinaria se captura dentro del post de tailles de découpe |
| `doggy bag` | 12.100 | PAA de comensal; sin agente que sostenga la conversión |
| `ddm` / `dlc` (cabeceras) | 18.100 / 12.100 | Consumo doméstico y **videojuegos** («C'est quoi le DLC d'un jeu ?»). Se ataca solo la variante comparativa `dlc ddm` (320) |
| `licence 4` / `permis d'exploitation` | 5.400 / 2.900 | Trámite y compra; SERP de service-public; sin agente de consultoría |
| `parage` | 4.400 | Cascos de caballo |
| `coût de revient` | 3.600 | Contabilidad general (Urssaf, «coût d'un salarié»): la trampa italiana de la contabilidad de estudiantes, versión francesa |
| `sécurité alimentaire` | 1.000 | Es *food security* (Banque mondiale, OMS, FAO) |
| `mise en place` | 2.900 | SERP de diccionario; `mise en place cuisine` solo 70 |
| `carte allergènes` | 2.900 | Mapa de polen (Airparif, Atmo) |
| `chaîne du froid` | 2.900 | Consumidor y logística; el pico de 18.100 en un mes es ruido |
| `formation haccp` | 9.900 HIGH | Venta de cursos homologados: otro negocio |
| `avis google` (y todo marketing) | 40.500 | El buscador es el comensal; y el clúster marketing B2B (<1.200/mes) no tiene NINGÚN agente en frapp |
| `cuisson sous vide` / `sous vide` | 1.300 / 2.400 HIGH | Compra de máquinas («Quel est le meilleur cuiseur sous vide ?») |
| `béchamel`, `sauce béarnaise`, `cuisson des viandes` | 165.000 / 27.100 / 8.100 | Recetario doméstico puro |
| `ouvrir un restaurant` | 720 | SERP copada por el Estado (service-public, France Travail) |
| `chef de partie` / `commis` | 3.600 / 6.600 | Intención de EMPLEO (salarios, France Travail) |
| `règlement inco` / `1169/2011` | 720 / 320 | SERP de EUR-Lex y DGCCRF — patrón italiano calcado; el reglamento se cita dentro del pilar de alérgenos, no se titula |
| `avantage en nature repas` | 590 | SERP de nómina (Urssaf): el lector quiere a su gestor. Primer suplente si algún día hay agente de gestión social |

## Restricción de producto

La plataforma francesa (`frapp.aichef.pro`) sirve **53 agentes** (censo
`.work/frapp-agentes.txt`). No hay categoría Hotel, ni consultoría, ni social
media, ni SEO local → el clúster de marketing y el de trámites quedan fuera
aunque tuvieran volumen. Productos digitales ES-only → **sin banners**: la
conversión va al agente de frapp con UTM, como en el blog italiano. Los ganchos
citados abajo están verificados 1 a 1 contra el censo.

## Los 14 posts, en orden de publicación

Mismo criterio que en Italia: primero el clúster A (higiene/alérgenos), que es
donde el agente encaja literal, después gestión y técnica.

| # | Keyword objetivo | Clúster/mes | Dific. | AIO | Agente gancho | Tipo |
|---|---|---|---|---|---|---|
| 1 ✅ | `tableau des allergènes` + `liste des allergènes` | 5.580 | BAJA-MEDIA | sí | ID Allergènes | **PILAR** |
| 2 ✅ | `contamination croisée` | 730 | MEDIA | sí | ID Allergènes | satélite |
| 3 ✅ | `haccp` (+ normes, méthode, c'est quoi) | **35.460** | MEDIA | sí | Manager de Restaurant Pro | **PILAR** |
| 4 ✅ | `plan de maitrise sanitaire` (PMS) | 1.530 | MEDIA | sí | Manager de Restaurant Pro | **PILAR** |
| 5 ✅ | `marche en avant` (cuisine) | 870 | BAJA | sí | Chef Exécutif Pro | satélite |
| 6 ✅ | `hygiène alimentaire` / `gbph` / 5 règles | 2.930 | BAJA-MEDIA | sí | — plataforma | **PILAR** |
| 7 ✅ | `plan de nettoyage cuisine` | 330 ↗ | BAJA | no | — plataforma | satélite |
| 8 | `fiche technique cuisine` | 1.910 | BAJA | **no** | Chef Exécutif Pro | **PILAR** |
| 9 | `menu engineering` | 410 | BAJA | no | Manager de Restaurant Pro | satélite |
| 10 | `brunoise` / tailles de découpe | 6.950 | BAJA | **no** | Gastro Lexicum | **PILAR** |
| 11 | `sauces mères` | 370 | BAJA | no | Cuisine Française | satélite |
| 12 | `lacto fermentation` | 1.780 | MEDIA | sí | Fermentus Avec AI+ | satélite |
| 13 | `dlc ddm` / `dlc dluo` | 580 | MEDIA | sí | — plataforma | satélite |
| 14 | `chefgpt` (avis + alternatives) | 2.620 ↗×4 | MEDIA | no | — plataforma | satélite |

**Suma direccionable: ~62.000 búsquedas/mes** (35.460 solo en el pilar HACCP).

### Por qué en ese orden

- **1-2 (alérgenos)**: el mejor encaje producto-búsqueda del research — ID
  Allergènes hace literalmente lo que la SERP pide. En el pilar, la keyword
  gorda (`liste des allergènes`, 2.400) es mixta consumidor/pro; la buena es
  `tableau des allergènes` (1.000): gana quien entrega el cartel imprimible.
  El post entrega el tableau Y lo convierte al agente que lo regenera con cada
  cambio de carta.
- **3 `haccp`** es la cabecera absoluta (27.100 el término solo, LOW): la
  prueba del hueco es que skello.io —un SaaS de planning— rankea 8º con un post
  de blog. Realista entrar al top 10; el #1 (service-public) no se disputa.
- **4 PMS y 6-7 (GBPH, nettoyage)** son las siglas-mina: intención 100 %
  restaurador, SERP de consultoras que ganan con un PDF. El PMS regala la
  estructura en su PAA, incluida la desambiguación PMS↔HACCP que enlaza al
  pilar 3.
- **8 `fiche technique cuisine`** es el hallazgo del research: en Francia el
  escandallo se busca así (el clúster de `coût de revient recette` entero está
  sin datos). SERP de SaaS sin dominador y un PAA que pide «le meilleur
  logiciel gratuit pour créer des fiches techniques» — **la SERP pide nuestro
  producto por su nombre genérico**. Serie ×4 en 6 meses (320→1.300).
- **10 tailles de découpe** es el mayor volumen limpio del clúster técnico
  (brunoise 6.600 LOW, sin AI Overview, SERP de cuchillerías): se gana con la
  tabla de medidas en mm. Además desambigua y captura el tráfico útil de las
  tres trampas (julienne, mirepoix) sin competir por ellas.
- **14 `chefgpt`** cierra: el único punto vivo de IA, ×6 lo que valía en Italia
  y subiendo. Comparativa honesta (app doméstica vs cocina de 80 cubiertos);
  es contenido de marca, por eso no va antes pese al volumen.

## Reglas de ejecución (heredadas del blog IT + las locales)

1. **Antes del post 1: crear el árbol `/fr/blog/`** clonando la fase 9 italiana,
   con `blogHubHref`/`postPath` resolviendo `fr` y gate de FAQ duplicadas
   `--lang fr`.
2. `modDate` en el frontmatter o el post no entra en el sitemap
   (`fase8b-regen-lastmod.py` tras cada post). **Purgar `.astro` y verificar el
   RECUENTO de páginas y las URLs nuevas en `dist`** — un build verde puede no
   emitir lo recién escrito (pasó el 2026-08-15 con los posts IT 4-5).
3. **Datos normativos FIJADOS en el prompt y verificados**: aquí el marco es el
   *Paquet Hygiène* (Reg. CE 852/2004), el PMS, el INCO para alérgenos y la
   formación 14 h. Nada de sanciones ni importes. Separar LEY de PRASSI como en
   los posts IT 4-5.
4. El PAA francés repite formulaciones («les X règles d'hygiène» con X
   variable): fundir o salta `fase8d-faq-duplicadas.py`.
5. **Sin banners de producto digital** (ES-only). Conversión → agente de
   `frapp.aichef.pro` con `utm_source=blog&utm_medium=cta&utm_content=<slug>`.
6. Los títulos pueden llevar artículo («Les 14 allergènes…»); los H2 que
   persiguen keyword, no (regla 3 del research).
7. `dataforseo.py` con `--pais 2250 --idioma fr` SIEMPRE (el default es España).
8. Imágenes: mínimo 2 en cuerpo + destacada única, textos visibles EN FRANCÉS
   (la lección de las etiquetas del frigo italiano) y verificadas A OJO antes
   de optimizar.

## Suplentes y semillas futuras

- `avantage en nature repas` (590) — primer suplente si aparece agente de
  gestión social.
- `pms boulangerie` — demanda emergente sin volumen aún; satélite futuro con
  Boulangerie Créative.
- Sub-clúster patisserie/boulangerie vacío hoy (`fiche technique pâtisserie`
  170, `haccp boulangerie` 70): revisar en 6 meses — Francia es su capital y
  los agentes existen.
