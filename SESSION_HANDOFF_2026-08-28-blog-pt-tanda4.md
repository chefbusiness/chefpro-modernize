# Handoff — pista BLOG / IDIOMAS, 2026-08-28 (tanda 4 cerrada · PT 8/13)

## ▶️ CÓMO RETOMAR (leer esto primero)

**No hay nada a medias.** La tanda 4 está publicada, verificada y commiteada; el
árbol está limpio. Se retoma abriendo trabajo nuevo, no terminando lo anterior.

**Revalidado el 2026-08-30**, después de sincronizar **27 commits de la pista de
productos** de John: batería live de 50 comprobaciones **TODO VERDE**, sitemap
en 1.187 URLs, `robots.txt` sin rozar el blog PT. Los dos posts de la tanda 4
siguen sirviendo bien.

**Lo primero al retomar, en este orden:**

1. `git pull --rebase origin main` — John empuja desde el Mac a docenas de
   commits por sesión (en esta revalidación había 27 sin traer).
2. `python3 .work/post9-pt-cortes/bateria-live-tanda4.py` — 30 s, confirma que
   la tanda sigue en pie antes de construir nada encima.
3. Decidir frente:
   - **Tanda 5 del PT** (lo natural): posts **10 `garum`** (1.300/mes, sin AIO,
     gancho Fermentus Con AI+) y **11 `cozinha molecular`** (410/mes, con AIO,
     gancho Sosa Ingredients). **Re-medir volúmenes y SERP ANTES** y mirar quién
     ocupa el #1 (regla 7, con el matiz nuevo: la variante cualificada puede
     estar más contaminada que la cabecera).
   - **Cerrar `plan-financiero` v2.0** de la pista de productos — ojo, **es la
     pista de John**, coordinarlo con él antes de tocarla.
   - **Deuda pequeña de SEO**: el `llms.txt` está desactualizado (0 URLs del
     blog, dice «30 productos digitales» cuando hay 44 y «Spanish-language»
     cuando el blog ya va en 6 idiomas), y el gate `public/` vs
     `astro-site/public/` sigue sin escribirse.

**El pipeline por post NO se improvisa**: está en 10 pasos en
`SESSION_HANDOFF_2026-08-22-blog-pt.md`, probado ocho veces. Lo de aquí abajo
son las lecciones que lo corrigen.

**Fechas con reloj corriendo:** ventana de GSC del **PT el 15-22 de septiembre**
(posts 1-6 desde el 21-22 de agosto, 8-9 desde el 28) · **IT/FR/DE el 8-15 de
septiembre** · **librerías EN el 3-sep (¿rastreadas?) y el 17-sep
(¿indexadas?)**, tras el arreglo del `robots.txt`
(`SESSION_HANDOFF_2026-08-27-robots-indexacion.md`).

---

> Sustituye a `SESSION_HANDOFF_2026-08-22-blog-pt.md` como handoff vivo de esta
> pista. Lo de allí sigue siendo válido: el **pipeline en 10 pasos**, los gotchas
> de bridge y la lista de pendientes de John. Aquí va lo nuevo.
>
> La pista de **productos digitales** es de John y va por su cuenta
> (`SESSION_HANDOFF_2026-08-22-B-fase-a-entregables.md`, §11 para retomar
> plan-financiero). No se pisan, pero **`git pull --rebase` antes de commitear**.

## Estado: PUBLICADO y verificado en producción

Commit `b505c50` en `main`, deploy `ready` a los 120 s, **batería live TODO
VERDE** (50 comprobaciones) y `fase7-vigilancia.py` en verde.

| # | Slug | Keyword (vol/mes re-medido) | CTA | Categoría |
|---|---|---|---|---|
| 8 | `mise-en-place` | `mise en place` **1.900** (clúster ~2.350) | Chef Executivo Pro `chef-ejecutivo-pro-05y07-pt` | `tecnica-e-receitas` |
| 9 | `cortes-de-legumes-mirepoix-brunoise` | mirepoix **590** + brunoise **210** + juliana **170** (clúster ~1.280) | Léxico Gastronómico `gastro-lexicum-jvnxv-pt` | `tecnica-e-receitas` |

Interenlazado: 8→6, 8→5, 8→4, 8→9 · 9→8, 9→6 · recíprocos parcheados en
`food-cost.md` y `controlo-de-temperaturas.md`. **La categoría
`tecnica-e-receitas` nace hoy en PT** (antes solo existía `gestao-de-restaurantes`):
son 3 páginas nuevas, no 2. Build 1.309 → **1.312**; sitemap 1.184 → **1.187**.

**Cola restante (11 → 13):** 10 `garum` · 11 `cozinha molecular` · 12 cocktails ·
13 food truck · 14 `pão de fermentação natural`. El 7 sigue saltado.

## Lo aprendido en esta tanda (lo que cambia cómo se trabaja la siguiente)

### 1. El censo del roadmap no es siempre falso: es siempre VIEJO

Tres tandas seguidas refutándolo habían dejado la impresión de que el roadmap
miente. En la 4 **los dos datos aguantaron, y al alza** (1.930 → clúster 2.350;
1.070 → 1.280). La regla correcta no es «desconfía del roadmap», es **re-mide
siempre** — puede confirmar tanto como refutar.

### 2. La regla 7 (marcas homónimas) aplica a la VARIANTE, no siempre a la cabecera

El instinto decía atacar `mise en place restaurante` por ser más cualificada.
Medido: ahí el restaurante de Marinha Grande ocupa **#1, #2, #5 y #8** y copa las
relacionadas — es una SERP de marca. En la **cabecera** `mise en place` (11 veces
más volumen) el mismo restaurante solo tiene #1, #3 y #9 y deja libres todos los
puestos informativos. **La variante cualificada puede estar MÁS contaminada que
la cabecera.** Mirar las dos antes de decidir.

### 3. Un PAA partido en dos intenciones es un hueco, no un problema

Seis de las ocho preguntas del PAA de `mise en place` son de **sala** (garfo,
guardanapo, de que lado se sirve). Los contenidos brasileños hablan solo de
cocina; los dos PT-PT solo de mesa. **Nadie cubre las dos.** Cuando el PAA se
parte, la tentación es elegir una mitad; el post que gana es el que explica que
son dos aplicaciones del mismo sistema.

### 4. Hueco por CALIDAD: cuando la SERP se contradice a sí misma

El caso más limpio hasta ahora. Verificado contra fuentes primarias el 28-ago:
**pt.wikipedia, que es el #1 de Portugal para `mirepoix`, lo define como «um
corte de 2 milímetros»** — más fino que una brunoise, cuando el mirepoix es
grueso e irregular por definición. Y las escuelas no coinciden entre sí: juliana
3×3×40-50 mm (EN) frente a 1 mm de espesor (FR); brunoise 3 mm (EN) frente a
2 mm (FR). **Nadie lo dice: todos sirven un número como si fuera dogma.**

El ángulo no fue dar «la medida buena» —no existe—, sino dar las dos, decir que
lo que importa es la regularidad, y separar lo que es un **corte** (definido por
una medida) de lo que es una **preparación** (definida por una proporción). El
post lleva `assert` de que la fila del mirepoix **no** contiene ni «mm» ni «cm»:
darle medida sería contradecir su propia tesis.

### 5. Verificar el CTA por el nombre del agente da FALSO VERDE

El handoff anterior decía: «Pickaxe no devuelve 404 → verificar buscando el
nombre del agente dentro del HTML». **Insuficiente, y hoy se vio por qué:**

- `ptapp.aichef.pro/<slug>` responde **307 → `/guest/<slug>`**: sin `-L`, curl
  devuelve 58 bytes y ningún check encuentra nada.
- **Cada página embebe el catálogo COMPLETO de los 53 agentes**, así que buscar
  «Chef Executivo Pro» dentro del HTML de `gastro-lexicum-jvnxv-pt` **también da
  positivo**.
- El `<title>` es genérico de todo el workspace: `AI Chef Pro - Português - V1.4`.

**La verificación válida es el par `"formid":"<slug>","formtitle":"<nombre>"`.**
La batería live ya lo hace así.

### 6. Los barridos automáticos no cazan las fugas del prompt

Dos **fugas literales del prompt impresas en el artículo** («Explica isto com
clareza e sem arrogância, uma única vez, na secção da tabela» y «A leitura
obrigatória a seguir à tabela:»). Mi barrido buscaba `OBRIGAT`, `citável`,
`bloco`, `TABELA A` — y no las cazó porque las agujas eran otras. **El barrido
automático solo encuentra lo que ya te pasó; la lectura completa encuentra lo
que te va a pasar.** Ampliado el patrón en el script, pero la conclusión es que
no sustituye a leer.

### 7. Fixes como asserts NEGATIVOS, no como lista de reemplazos

Los ensambladores 1-6 llevaban los fixes como pares `(viejo, nuevo)` con
`assert count == 1`. Los de la tanda 4 aplican los fixes **en el `.html`** y en
el ensamblador van **asserts negativos**: `assert aguja not in html`. Ventajas
medidas: caza la regresión venga de donde venga (no solo del texto exacto que
viste), no obliga a mantener el mismo párrafo en dos sitios, y el fichero de
ensamblado queda legible. Los dos ensambladores son **reejecutables**
(comprobado con doble pasada) — el `assert` del ancla del recíproco va DENTRO
del guard `if url not in m:`, nunca fuera; ponerlo fuera petó la primera pasada.

### 8. Defectos nuevos de bridge en esta tanda (17 en total)

Además de las dos fugas del prompt:

- **Aritmética inventada que no cuadra**: «diez pasos por plato × cien platos =
  un kilómetro» (son ~750 m). Plausible, específica y falsa — el patrón de
  siempre.
- **Medidas concretas inventadas para el mirepoix** (3-4 cm para un fondo de
  seis horas, 1-2 cm para un estufado de una hora) que **contradecían su propia
  fila de tabla** («sem medida fixa»).
- **«duzentas gramas»**: `grama` es MASCULINO en portugués. Ningún gate lo caza.
- **«uma batata cortada fica acinzentada e AMARGA»**: falso. El amargor es
  solanina por exposición a la luz, no por el corte.
- **La FAQ contradecía la tesis del cuerpo**: la Q5 mandaba «verificar o aspeto
  e o cheiro antes de reutilizar», que es exactamente la práctica casera que el
  artículo declara inaceptable dos secciones antes. **Leer la FAQ CONTRA el
  cuerpo, no solo por separado.**
- **Comillas rectas** (`"..."`) en vez de las angulares del corpus: 5 pares. El
  gate `comillas_rectas` del ensamblador lo cazó.
- **La duplicación literal intro↔primer `<h2>` volvió a aparecer.** Ya son tres
  tandas seguidas: dala por segura y búscala siempre.

### 9. Imágenes: la coherencia profesional también es un motivo de rechazo

1 rechazo de 6. La primera `mep-pt-praca` salía con **la mano de agarre plano
junto al filo** — exactamente lo contrario de la técnica que enseña el post 9,
que se publica el mismo día y está enlazado desde ese párrafo. Se regeneró
pidiendo explícitamente «NO hands, NO arms, NO people». Añadir esa prohibición
al STYLE base cuando la escena no necesite manos.

**La fórmula del texto legible funcionó a la primera**: el rótulo con fecha
salió exacto (`28-08`) dictando el valor dígito a dígito y pidiendo el plano
frontal y en foco. Es la tercera vez que funciona; ya es procedimiento.

## Verificación de esta tanda (para no repetirla)

- Gates: `fase8d-faq-duplicadas.py --lang pt` **0 pares** · `fase8c-h1-unico.py`
  **0** · `robots-gate.py` **ninguna URL pública bloqueada** (regla nueva del
  incidente del 27-ago; las URLs nuevas no rozan ningún patrón).
- Build **doble con purga**: 1.312 las dos veces, con los dos `.html` y la
  categoría nueva verificados en el `dist`.
- `FAQPage` con 5 `Question`, canonical propio y `noindex` ausente, verificados
  **en el `dist`** y luego **en producción** — no en el `.md`.
- Batería live: `.work/post9-pt-cortes/bateria-live-tanda4.py` (reutilizable
  para la tanda 5 cambiando el diccionario `POSTS`).

## Lo siguiente

1. **Tanda 5: posts 10 `garum` (1.300, sin AIO, Fermentus Con AI+) y 11
   `cozinha molecular` (410, con AIO, Sosa Ingredients).** Re-medir antes, y
   mirar quién ocupa el #1 (regla 7, ahora con el matiz de la variante).
2. **Ventana de GSC del PT: 15-22 de septiembre**, por página+query. Los posts
   1-6 llevan desde el 21-22 de agosto; los 8-9 desde hoy.
3. Maduración de IT (17-ago), FR (18-ago) y DE (19-ago): releer hacia el
   **8-15 de septiembre**.
4. Pendientes de John, sin cambios: checkouts de ptapp/nlapp con el plan de
   10 € (el blog PT ya manda tráfico a `ptapp.aichef.pro` desde **ocho** posts),
   cutover de enblog, catálogo italiano, etiqueta de conversión en itapp, y la
   solicitud manual de indexación de las librerías EN en GSC.
