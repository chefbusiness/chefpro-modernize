# Handoff — pista BLOG / IDIOMAS, 2026-08-22 (sustituye a `SESSION_HANDOFF_2026-08-21.md`)

> Handoff de la **pista de blog e idiomas**. La pista de **productos digitales**
> es de John y va por su cuenta: `SESSION_HANDOFF_2026-08-22-productos-digitales.md`
> y `SESSION_HANDOFF_2026-08-22-B-fase-a-entregables.md`. No se pisan: tocan
> ficheros distintos, pero **haz `git pull --rebase` antes de commitear** —
> John empuja desde el Mac a docenas de commits por sesión.

## Estado del frente de idiomas

| Idioma | Estado | Siguiente |
|---|---|---|
| IT | 13/13 completo (17-ago) | Madurar GSC → releer hacia el 8-15 sept |
| FR | 14/14 completo (18-ago) | Ídem |
| DE | 14/14 completo (19-ago) | Ídem |
| **PT** | **4/14 — EN CURSO** | **Tanda 3: posts 5 y 6** |
| NL | Solo roadmap | Se abre tras PT 14/14 |

**PT publicado y verificado en vivo** (el eje normativo va 4/5):

| # | Slug | Keyword (vol/mes) | CTA | Commit |
|---|---|---|---|---|
| 1 | `haccp` | haccp (5.230) | plataforma + mención ID Alergénios | `5fe1e4c` |
| 2 | `alergenios` | alergenios+alergénios (1.330) | ID Alergénios | `5fe1e4c` |
| 3 | `contaminacao-cruzada` | contaminação cruzada (210) | ID Alergénios | `887b94c` |
| 4 | `higiene-e-seguranca-alimentar` | higiene e segurança alimentar (210) | plataforma + ID Alergénios | `887b94c` |

Interenlazado completo y recíproco: 1↔2, 3→1, 3→2, 2→3, 4→1, 4→3, 1→4.
Categoría de los cuatro: `gestao-de-restaurantes`. **Build actual: 1.307.**

## La siguiente tanda (3): posts 5 y 6

- **5 `controlo de temperaturas`** (110/mes, dificultad BAJA, **sin AIO**,
  upside BR 1.000) — satélite. CTA: plataforma (no hay agente de temperaturas).
  Enlaza a `haccp` (principios 3-4: límites críticos y vigilancia) y recibe
  recíproco desde él. Cuidado: las temperaturas de referencia YA están fijadas
  en los posts 1 y 4 (0-5 °C · −18 °C · ≥75 °C · ≥65 °C · zona 5-65 °C) —
  **usar exactamente esas y no inventar ninguna nueva**; el ángulo propio es
  el CÓMO se mide y se registra (sondas, calibración, frecuencia, qué hacer
  cuando falla), no repetir la tabla.
- **6 `food cost`** (180/mes, BAJA, con AIO, PILAR) — CTA **Gerente
  Restaurante Pro** `gerente-de-restaurante-pro-dumn4-pt`. ⚠️ **Regla 6 del
  roadmap: el PAA de la cabecera vuelve EN INGLÉS** (Google rellena la SERP
  portuguesa con inglés desde el puesto 3) → sacar la FAQ de la variante
  local **«como calcular o food cost»**. Es el arranque del clúster B
  (6-7), así que conviene dejarlo preparado para enlazar al 7 (`ficha
  técnica de pratos`, tSpoonLab Agent `tspoonlab-agent-w7rey-pt`).
- **SERP fresca ANTES de escribir, siempre**:
  `python3 scripts/dataforseo.py serp "<kw>" --pais 2620 --idioma pt`
  (y `vol` para confirmar volúmenes; Brasil 2076 solo para anotar upside).

Cola restante tras la tanda 3: 7 `ficha técnica de pratos` · 8 `mise en place`
(ojo marca homónima) · 9 cortes mirepoix/brunoise · 10 `garum` · 11 `cozinha
molecular` · 12 cocktails · 13 food truck · 14 `pão de fermentação natural`.
Todo el detalle y el porqué del orden: `ROADMAP_BLOG_PORTUGUES.md`.

## El pipeline por post (probado 4 veces, no improvisar)

1. **SERP + volumen frescos** → persistir en `.work/postN-pt-<tema>/datos-fijados.md`
   (SERP, PAA o relacionadas, DADOS FIXOS, estructura, CTA, enlaces, slug).
2. **Prompt del cuerpo** con: PT-PT estricto + prohibiciones (brasileirismos,
   gerúndio contínuo, tuteo), SEM H1, EXATAMENTE 6 `<h2>` + 2 tablas, línea
   anti-Markdown, longitud imperativa 2.200-2.600, «cada secção abre citável»
   si hay AIO, DADOS FIXOS literales y prohibición de links/software.
3. **bridge**: `--task content --domain aichef --lang pt --strict-lang
   --max-tokens 96000`. FAQ y meta en llamadas aparte (24k / 8192).
   Ruta VPS: `/root/chefbusiness-ai/.venv/bin/python /root/chefbusiness-ai/bridge.py`.
   No tiene `--prompt-file`: `--prompt "$(cat <ruta ABSOLUTA>)"`.
4. **Lectura adversarial COMPLETA** del cuerpo y de la FAQ (ver gotchas).
5. **Imágenes** (skill `generate-images`, Nano Banana 2): 1 destacada única +
   2 de cuerpo. Textos visibles EN PORTUGUÉS y **verificados a ojo con zoom**.
6. **Assembler** `.work/postN-pt-*/assembleNpt.py` clonando el anterior:
   fences, FIXES con `assert count == 1`, asserts de datos fijos, enlaces
   internos, figuras por ancla, CTA con UTM, FAQ json→yaml, recíproco en el
   post ya publicado (con `assert '<url>' not in m`), y el bloque de checks.
7. `python3 scripts/astro-migration/fase8b-regen-lastmod.py`
8. `python3 scripts/astro-migration/fase8d-faq-duplicadas.py --lang pt`
9. **Build DOBLE con purga**: `rm -rf .astro dist && npm run build`, comparar
   el recuento con el esperado y `ls dist/pt/blog/*.html`. Si faltan, repetir.
10. Commit **incluyendo `astro-site/public/blog-assets/`** → `git pull --rebase`
    → push → esperar deploy `ready` → **batería live** (páginas, imágenes, RSS,
    FAQPage, recíprocos servidos).

⚠️ **`.work/` está gitignorado**: los prompts, los datos fijados y los
assemblers **solo existen en el VPS**. No se pierden entre sesiones, pero
tampoco viajan al Mac ni a GitHub.

## Gotchas nuevos de estas dos tandas (los que costaron tiempo)

- **8º modo de fallo de bridge: CASTELLANO infiltrado en output PT.** La FAQ
  del post 3 salió con «tabla», «cámara», «crudos», «intoxicaciones»,
  «fritadora», «reducen drásticamente», «Por tanto». **`guard_idioma()` NO lo
  caza** (solo mira alfabetos no latinos), así que `--strict-lang` pasa en
  verde. Cura medida a la primera: bloque final «ATENÇÃO CRÍTICA» con los
  pares error→correcto + `--temperature 0.3`. El barrido anti-ES es ya assert
  permanente en los assemblers. **Trampa del assert**: `geri-los`,
  `incluí-los`, `travá-la` son clíticos PT legítimos → el regex exige
  no-guion delante: `(?<![-\w])(los|las|una)(?![\w])`.
- **La carrera del content layer reincide** (3ª vez): build VERDE sin emitir
  los .md nuevos, incluso tras purgar `.astro`. El doble build lo resuelve;
  el recuento + `ls dist` es el único gate fiable.
- **Un árbol vacío infracuenta**: la página `categoria/gestao-de-restaurantes`
  solo nació con el primer post, así que el build fue 1.305 y no 1.304. Al
  estrenar idioma, el esperado tiene que incluir las páginas que solo se
  materializan con contenido.
- **El site_id de Netlify es `dc777725-7e95-4336-876e-a5a9b568fe75`** (sacado
  de `netlify api listSites`). El `ee5802cf-…` que circulaba en el handoff del
  21 era un **deploy id**, no el site. La CLI está autenticada en el VPS.
- **Defectos que bridge coló y la lectura adversarial cazó** (12 en 4 posts):
  bulos factuales («acento circunflexo» en alérgenos), contradicciones con
  la propia tabla del post («o vinho pode não precisar de declaração»),
  ejemplos técnicamente falsos (`bife` como PCC de confeção, cuando se sirve
  por debajo de 75 °C → `frango`), pseudocitas sin fuente («estudos do setor
  mostram…»), glitches («finalmente polimento um prato»), brasileirismos
  sueltos (`dossiê`, `pécã`) y comillas rectas. **Ninguno lo habría cazado un
  check estructural.**
- **Imágenes: 3 rechazos de 13 fueron por coherencia profesional, no por
  calidad**: un anillo en la mano de un chef en el post de higiene, un display
  de sonda marcando 128 °C en un guiso, y una cocinera con melena suelta y sin
  touca justo en el post de higiene pessoal. Para pósters/tablas con texto, la
  fórmula que funciona es **dar al modelo la lista EXACTA de palabras** (los 14
  alergénios en portugués salieron perfectos; dos intentos previos con
  «solo el título legible» devolvieron filas en inglés con «MILKE»).

## Pendientes de John (recordarle al cerrar hitos)

- **Checkouts de ptapp/nlapp con el plan de 10 €** — el blog PT ya manda
  tráfico a `ptapp.aichef.pro`, así que esto empieza a costar dinero.
- Replicar el anuncio de los 3 modelos open source en itapp/frapp/deapp/ptapp/nlapp.
- Conversión COMPRA en Google Ads.
- **Cutover de enblog** (`CUTOVER_ENBLOG_PENDIENTE.md`): alias en Netlify + DNS,
  con la trampa de las A records de Hostinger.
- Las 3 decisiones del header del handoff del 21 (hub de free tools sin enlaces
  en el header ES/EN; anclas compartidas por columna; ancla ES vía `/`).

## SEO pendiente (no bloquea)

Maduración GSC de IT (17-ago), FR (18-ago) y DE (19-ago): releer hacia el
**8-15 de septiembre** por página+query, con la trampa de la URL legacy
presente. Las free tools SSR (119 URLs) también esperan primera lectura.
