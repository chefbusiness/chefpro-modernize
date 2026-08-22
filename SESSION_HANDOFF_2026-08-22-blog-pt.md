# Handoff — pista BLOG / IDIOMAS, 2026-08-22 (tanda 3 cerrada)

> Handoff de la **pista de blog e idiomas**. La pista de **productos digitales**
> es de John y va por su cuenta: `SESSION_HANDOFF_2026-08-22-productos-digitales.md`
> y `SESSION_HANDOFF_2026-08-22-B-fase-a-entregables.md`. No se pisan: tocan
> ficheros distintos, pero **haz `git pull --rebase` antes de commitear** —
> John empuja desde el Mac a docenas de commits por sesión (en esta tanda ya
> hubo que rebasar sobre uno suyo).

## Estado del frente de idiomas

| Idioma | Estado | Siguiente |
|---|---|---|
| IT | 13/13 completo (17-ago) | Madurar GSC → releer hacia el 8-15 sept |
| FR | 14/14 completo (18-ago) | Ídem |
| DE | 14/14 completo (19-ago) | Ídem |
| **PT** | **6/14 — EN CURSO** | **Tanda 4, pero antes decidir qué pasa con el post 7 (ver abajo)** |
| NL | Solo roadmap | Se abre tras PT 14/14 |

**PT publicado y verificado en vivo. El eje normativo está CERRADO (5/5).**

| # | Slug | Keyword (vol/mes real) | CTA | Commit |
|---|---|---|---|---|
| 1 | `haccp` | haccp (5.230) | plataforma + ID Alergénios | `5fe1e4c` |
| 2 | `alergenios` | alergenios+alergénios (1.330) | ID Alergénios | `5fe1e4c` |
| 3 | `contaminacao-cruzada` | contaminação cruzada (210) | ID Alergénios | `887b94c` |
| 4 | `higiene-e-seguranca-alimentar` | higiene e segurança alimentar (210) | plataforma + ID Alergénios | `887b94c` |
| 5 | `controlo-de-temperaturas` | controlo de temperaturas (**50**, clúster ~210) | plataforma + Gerente Restaurante Pro | `492fb1b` |
| 6 | `food-cost` | food cost (**110**, clúster ~150) | plataforma + Gerente Restaurante Pro | `492fb1b` |

Interenlazado completo y recíproco: 1↔2, 3→1, 3→2, 2→3, 4→1, 4→3, 1→4,
**5→1, 5→3, 5→4, 1→5, 6→4, 6→5, 5→6**. Categoría de los seis:
`gestao-de-restaurantes`. **Build actual: 1.309** (doble build con purga; los
dos `.html` verificados en `dist` y en producción).

Batería live pasada: páginas 200, las 6 imágenes 200, `FAQPage` con 5
`Question` cada uno, un solo `<h1>`, 2 tablas y 2 figuras por post, canonical
correcto, recíprocos servidos y RSS con los 6 items.

## ⚠️ Antes de la tanda 4: el post 7 no está en pie

El research de esta tanda refutó las dos patas que lo sostenían:

1. **`ficha técnica de pratos` mide 10/mes**, no 80.
2. **`tSpoonLab Agent` no es un agente de escandallos.** Su descripción real en
   ptapp es «ajudá-lo a aprender a usar a ferramenta SaaS tSpoonLab» — un bot de
   soporte de un software de terceros. El encaje de producto no existe.

Opciones, por orden de preferencia: **(a)** saltar al post 8 (`mise en place`,
1.930/mes, el más rentable de la cola) y absorber la ficha técnica dentro del
clúster del post 6, que ya la trata como el instrumento del food cost;
**(b)** escribirlo con CTA a Gerente Restaurante Pro. **Decisión pendiente.**

Cola restante: 8 `mise en place` (ojo marca homónima) · 9 cortes
mirepoix/brunoise · 10 `garum` · 11 `cozinha molecular` · 12 cocktails ·
13 food truck · 14 `pão de fermentação natural`. Y **re-medir volúmenes antes
de cada tanda**: el roadmap del 16-ago ya falló en 4 de 4 comprobaciones.

## El pipeline por post (probado 6 veces, no improvisar)

1. **SERP + volumen frescos** → persistir en `.work/postN-pt-<tema>/datos-fijados.md`.
   Consultar también **las variantes locales**, no solo la cabecera: en esta
   tanda el PAA útil salió de `como calcular o food cost`, y `registo de
   temperaturas` reveló la trampa meteorológica.
2. **Prompt del cuerpo**: PT-PT estricto + prohibiciones, SEM H1, EXATAMENTE 6
   `<h2>` + 2 tablas, línea anti-Markdown, longitud imperativa 2.200-2.600,
   «cada secção abre citável», DADOS FIXOS literales, prohibición de links y de
   software, y el bloque final **ATENCAO CRITICA** con los pares error→correcto.
3. **bridge**: `--task content --domain aichef --lang pt --strict-lang
   --max-tokens 96000 --temperature 0.3`. FAQ y meta aparte (24k / 8192).
   Ruta VPS: `/root/chefbusiness-ai/.venv/bin/python /root/chefbusiness-ai/bridge.py`.
   No tiene `--prompt-file`: `--prompt "$(cat <ruta ABSOLUTA>)"`.
   **Para la meta, pedir TRES opciones y elegir**: la primera suele salir como
   una lista de fragmentos separados por comas.
4. **Lectura adversarial COMPLETA** del cuerpo y de la FAQ (ver gotchas).
5. **Imágenes** (skill `generate-images`, Nano Banana 2): 1 destacada única +
   2 de cuerpo, **escenas que no repitan las de los posts ya publicados**.
6. **Assembler** `.work/postN-pt-*/assembleNpt.py` clonando el anterior.
7. `python3 scripts/astro-migration/fase8b-regen-lastmod.py`
8. `python3 scripts/astro-migration/fase8d-faq-duplicadas.py --lang pt` +
   `python3 scripts/astro-migration/fase8c-h1-unico.py`
9. **Build DOBLE con purga**: `rm -rf .astro dist && npm run build`, comparar
   el recuento y `ls dist/pt/blog/*.html`.
10. Commit **incluyendo `astro-site/public/blog-assets/`** → `git pull --rebase`
    → push → esperar deploy `ready` → **batería live**.

⚠️ **`.work/` está gitignorado**: prompts, datos fijados, assemblers y las
fuentes oficiales descargadas **solo existen en el VPS**.

## Gotchas nuevos de la tanda 3

- **9º modo de fallo de bridge: castellano LÉXICO aislado.** Escribió «as
  aparas e as **mermas**» en medio de un texto PT impecable. Ni `guard_idioma()`
  (solo mira alfabetos no latinos) ni el regex anti-ES de los assemblers
  anteriores lo cazaban, porque la lista era de palabras funcionales
  (`tabla`, `crudos`, `por tanto`) y esto es **vocabulario técnico del oficio**.
  Los assemblers 5 y 6 ya llevan la lista ampliada por dominio (`merma`,
  `coste`, `beneficio`, `ingresos`, `pérdida`, `hoja de cálculo`). **Amplía la
  lista con el vocabulario del tema de cada post nuevo.**
- **Y errores de GÉNERO**: «um couve-flor» (es femenino). No hay gate posible;
  esto solo lo caza la lectura.
- **Un gate propio también da falsos positivos.** Mi check «no cites tipos de
  IVA» (`iva[^.]{0,40}\d+%`) tumbó el build por cazar «sem IVA … 28,1 %», que
  es legítimo. Mismo patrón que el `valida()` que en su día tumbó un «1982»:
  **el número tiene que ir PEGADO al término**, no en la misma frase.
- **Los assemblers tienen que ser REEJECUTABLES.** Si el paso del recíproco
  hace `assert '<url>' not in m`, el script no se puede volver a correr — y en
  una tanda de dos posts, donde el 6 parchea al 5, hay que reejecutar el 5.
  Patrón correcto: `if '<url>' not in m:` y dentro el assert del ancla.
- **La convención U+202F / U+2011 NO aplica a los posts PT**: usan espacio y
  guion normales (`10 °C`, `~5 e 65 °C`). Solo el U+2212 del menos. Verificado
  contra `haccp.md`: cero ocurrencias de los tres caracteres finos.
- **Defectos que bridge coló y la lectura adversarial cazó: 23 en dos posts.**
  Los que costaban dinero o credibilidad: **80/60 °C inventados en un bife que
  se serviría por debajo de los 75 °C que el propio post exige** (la MISMA
  trampa del `bife` de la tanda 1 — el modelo reincide con ese ejemplo);
  **«e na maioria dos restaurantes é»**, que convertía el registador automático
  en obligatorio y contradecía la tesis entera de la sección legal; **tres
  estadísticas inventadas** («metade dos registos falsos», «metade dos erros de
  gestão», «o bacalhau subiu 15 %»); una **afirmación fiscal sin verificar**
  sobre el régimen normal de IVA; la **prosa diciendo 2 € y 11 € donde la tabla
  dice 2,80 y 11,40**; el food cost aplicado a la **facturación total** en vez
  de a las ventas de comida; una **«multa»** (prohibido); y dos **fugas del
  prompt** («O que não se pode esticar:», «Diz explicitamente que…» sin sujeto).
  **La duplicación literal de la definición entre la intro y el primer `<h2>`
  ocurrió en LOS DOS posts**: ya es sistemática, búscala siempre.
- **Imágenes: 3 rechazos de 6.** Una **alianza en la mano** (el mismo defecto de
  coherencia profesional de la tanda anterior — hay que prohibirlo
  explícitamente en el prompt), un **display ilegible**, y una **marca legible
  («CASIO») con facturas que ponían «FACTURA»**, grafía castellana. Fórmula que
  funciona para los displays: decir el valor dígito a dígito («the digit zero,
  then a decimal point, then the digit zero») y pedir la pantalla **plana hacia
  la cámara y en foco**.
- **Pickaxe/ptapp NO devuelve 404.** Un slug inventado sirve **200** con el
  mismo shell y casi el mismo tamaño que uno real. Verificar un CTA por código
  de estado da falso verde: hay que **buscar el nombre del agente dentro del
  HTML**. De paso, ese HTML trae **el catálogo completo de los 53 agentes** con
  `formid`/`formtitle`/`formdescription` → volcado en `.work/ptapp-agentes.json`.

## Lo que hizo fuerte al post 5 (y es replicable)

La SERP entera estaba publicando la misma noticia normativa (DGAV, ASAE, ACIP,
APIRAC, IPQ) sobre el control metrológico de los registadores automáticos.
**Bajar a la fuente primaria** —el PDF del Esclarecimento Técnico n.º
4/DGAV/2025 y la FAQ de la ASAE sobre calibración de termómetros en
restauración— reveló que la obligación es **solo de ultracongelados** y que el
propio documento responde «**NÃO**» para el resto. Nadie lo traduce al
restaurante. Sin ese PDF, el post habría repetido la alarma y habría sido un
bulo. **Cuando una SERP entera repite una noticia, el hueco está en el original.**

## Pendientes de John (recordarle al cerrar hitos)

- **Checkouts de ptapp/nlapp con el plan de 10 €** — el blog PT ya manda
  tráfico a `ptapp.aichef.pro` desde SEIS posts.
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
