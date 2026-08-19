# Handoff — sesión maratón 2026-08-18 → 19 (sustituye a SESSION_HANDOFF_2026-08-18.md)

> Estado al cierre del 2026-08-19 (tarde). La sesión cerró FR (14/14) y DE
> (14/14) y **abrió el frente PT**: infra completa commiteada y research de la
> tanda 1 verificado. Siguiente sesión: escribir los posts PT 1-2.

## Dónde está todo

- **IT 13/13 · FR 14/14 · DE 14/14 — los tres roadmaps COMPLETOS y verificados
  en vivo.** Logs por tanda en `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8
  (2026-08-18-A…E y 2026-08-19-A…G). Ciclo siguiente de esos tres: madurar
  3-4 semanas y releer GSC por página+query (trampa de la URL legacy).
- **PT: infra COMPLETA (commiteada y con build verde, 1.302 páginas).**
  - `blog.ts`: CATEGORIES_PT (ia-na-gastronomia, gestao-de-restaurantes,
    tecnica-e-receitas, ai-chef-pro) + segmentos `categoria`/`pagina` +
    `formatDatePt` («17 de agosto de 2026»).
  - `BlogPost.astro` COPY.pt y `BlogCTA.astro` COPY.pt — **PT-PT estricto**
    («Atualizado a», «Continuar a ler», restauração, gastronómico, ementas).
  - Árbol `src/pages/pt/blog/` completo (index, [slug], categoria/, pagina/,
    rss). El hub emite como `dist/pt/blog.html` (formato `file`).
  - `fase8d-faq-duplicadas.py` con `--lang pt` (VACIAS_PT, definición
    «o que e» + rama invertida «haccp o que e», incluido en `todos`).
- **NL: solo roadmap** (`ROADMAP_BLOG_NEERLANDES.md`, 12 posts). Se abre
  DESPUÉS de cerrar PT 14/14. Recordar: entrada COPY.nl en BlogPost/BlogCTA y
  árbol con segmentos `categorie`/`pagina` ANTES del primer post; y la lección
  del piloto fase10 (un spoke salió en dialecto limburgués — revisar H1).

## Tanda 1 PT (posts 1-2) — TODO listo para escribir

- **Roadmap**: `ROADMAP_BLOG_PORTUGUES.md` (leerlo entero: reglas 1-9).
- **Research verificado y persistido** (no re-fetchear):
  `.work/post1-pt-haccp/datos-fijados.md` (SERP fresca + PAA + definición y
  7 princípios scrapeados de la ASAE + ley 852/2004 + temperaturas de
  referencia) y `.work/post2-pt-alergenios/datos-fijados.md` (SERP + PAA con
  la pregunta de la grafía + **lista íntegra de los 14 con redacción canónica
  ASAE** + umbral sulfitos + pendiente de verificar el n.º del Decreto-Lei
  26/2016 antes de fijarlo + **censo completo de agentes ptapp con formids**).
- **Pipeline por post** (idéntico a DE, ver `.work/post13-de-*` y
  `.work/post14-de-*` como referencia viva):
  prompts con FESTE DATEN → bridge `--task content --domain aichef --lang pt
  --strict-lang --max-tokens 96000` (⚠️ los cuerpos DE del 19-ago murieron a
  48k/96k con todo en razonamiento; si sale ENSALADA DE PALABRAS —7º modo—
  reintentar con `--temperature 0.3`) → lectura adversarial COMPLETA (la
  degeneración pasa los checks estructurales) → FAQ (16-24k) y meta →
  imágenes con gen.sh (skill generate-images; textos visibles EN PORTUGUÉS,
  sin marcas — WECK salió solo en un tarro) → assembler con asserts (clonar
  `assemble14de.py`: fences, fixes assert-count-1, datos fijos, figuras por
  ancla, CTA con UTM, FAQ json→yaml, recíprocos, checks) → lastmod → gate FAQ
  → build doble con purga (esperado tanda 1: **1.304**) → commit/push →
  poll deploy → batería live.
- **Asserts PT específicos** (además de los estándar): AMBAS grafías
  `alergénios` Y `alergenios` en el cuerpo del post 2; `castellano==0`;
  brasileirismos==0 (`cardápio|usuário|gerenci|geladeira|equipe|conosco`);
  gerúndio continuo==0 (regex `\b(está|estão|estava|estavam) \w+ndo\b` — el
  PT-PT dice «está a aplicar»); sin sanciones ni importes.
- **CTAs tanda 1**: post 1 → plataforma (no hay agente HACCP en ptapp) +
  mención ID Alergénios; post 2 → **ID Alergénios** `id-alergenos-g6b6g-pt`.
  Interenlazado 1↔2.

## Cola PT tras la tanda 1 (orden del roadmap)

3 `contaminação cruzada` · 4 `higiene e segurança alimentar` (⚠️ regla 2:
«segurança alimentar» a secas es food SECURITY) · 5 `controlo de temperaturas`
· 6 `food cost` (PAA en inglés → FAQ desde «como calcular o food cost») ·
7 `ficha técnica de pratos` (tSpoonLab) · 8 `mise en place` (ojo marca
homónima, regla 7) · 9 cortes mirepoix/brunoise · 10 `garum` (patrimonio de
Tróia) · 11 `cozinha molecular` · 12 cocktails · 13 food truck · 14 pão de
fermentação natural. SERP fresca ANTES de cada tanda (`--pais 2620
--idioma pt`; Brasil 2076 solo para anotar upside).

## Pendientes de John (aparcados por orden suya del 19-ago — recordar al cerrar hitos)

- Replicar el anuncio de los 3 modelos open source en itapp/frapp/deapp/ptapp/nlapp.
- Checkouts de ptapp/nlapp sin el plan de 10 €.
- Conversión COMPRA en Google Ads.
- **Cutover de enblog** (`CUTOVER_ENBLOG_PENDIENTE.md`): alias en Netlify +
  DNS, con la trampa de las A records de Hostinger.

## Gotchas calientes de la sesión (los nuevos)

- **7º modo de fallo de bridge**: degeneración progresiva a ensalada de
  palabras (alemán) que PASA los checks estructurales — solo la lectura
  completa la caza; `--temperature 0.3` la estabilizó. Detalle completo en la
  memoria `bridge-devuelve-markdown`.
- Presupuesto de razonamiento de `~deepseek` disparado: ir DIRECTO a 96k en
  cuerpos.
- bridge NO tiene `--prompt-file`: pasar `--prompt "$(cat fichero)"` con
  RUTAS ABSOLUTAS si el comando corre en background (el cwd de la sesión no
  viaja al bg).
