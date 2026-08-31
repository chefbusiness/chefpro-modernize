# Handoff — 2026-08-30/31 · tanda 5 del blog PT (BLOQUEADA en imágenes) + catálogo de productos

## ▶️ CÓMO RETOMAR (leer esto primero)

**La tanda 5 está escrita, ensamblada, verificada y commiteada — pero NO
publicada. Falta UNA sola cosa: las 6 imágenes.** La API de Gemini está sin
crédito:

```
429 RESOURCE_EXHAUSTED
"Your prepayment credits are depleted."
```

**El trabajo está en la rama `wip/blog-pt-tanda5` (commit `b99fd26`), NO en
`main`.** Es deliberado: los dos `.md` referencian 6 `.jpg` que no existen y
Netlify despliega desde `main`, así que un merge ahora publicaría los posts con
las imágenes rotas.

**Lo primero al retomar, en este orden:**

1. **John recarga crédito** en https://ai.studio/projects. Es lo único que
   bloquea; no hay ruta alternativa (la regla capital manda generar todas las
   imágenes con la skill `generate-images` / Nano Banana 2).
2. `git checkout wip/blog-pt-tanda5 && git pull --rebase origin main`
3. Generar las 6 imágenes (prompts exactos en §Imágenes, más abajo) y
   comprobarlas una a una con el Read tool antes de optimizar.
4. `git add astro-site/public/blog-assets/ && git commit`
5. Rebuild con purga y confirmar que las 6 están en el `dist`:
   `rm -rf astro-site/.astro astro-site/dist && npm run build`
6. Merge a `main` → push → esperar deploy `ready` → batería live.

**Lo que YA está hecho y verificado (no repetir):**

| Paso | Estado |
|---|---|
| Research + SERP de toda la cola | ✅ |
| Cuerpos, FAQ y metas | ✅ |
| Lectura adversarial (30 defectos) | ✅ corregidos con `assert` |
| Ensambladores ejecutados | ✅ los 2 `.md` creados |
| `fase8b-regen-lastmod.py` | ✅ 442 entradas, 2 altas |
| `fase8d-faq-duplicadas.py --lang pt` | ✅ **0 pares** |
| `fase8c-h1-unico.py` | ✅ **0** |
| `robots-gate.py` | ✅ ninguna URL pública bloqueada |
| Build **doble con purga** | ✅ **1314 páginas las dos veces** |
| Sitemap | ✅ **1187 → 1189, +2 exacto** |
| `FAQPage`/canonical/`noindex` **en el `dist`** | ✅ 5 `Question` cada uno, canonical propio, sin `noindex` |
| Recíprocos | ✅ higiene→10, 10→11, food-cost→11 |
| **Las 6 imágenes** | ⛔ **BLOQUEADAS** |

**Fechas con reloj corriendo:** GSC del PT **15-22 de septiembre** · IT/FR/DE
**8-15 de septiembre** · librerías EN **3-sep** (¿rastreadas?) y **17-sep**
(¿indexadas?).

---

## Qué cambió respecto al plan: el post 11 ya no es `cozinha molecular`

Decisión de John (30-ago) tras re-medir **toda la cola**, no solo los dos
programados. La tanda 5 es **`garum` + `massa mãe`**.

| # | Candidato | Cabecera | Clúster | SERP / intención | Veredicto |
|---|---|---|---|---|---|
| 10 | `garum` | **1.300** | ~1.510 | Informativa + marcas locales; **cero contenido profesional de cocina** | ✅ se escribe |
| 11 | `cozinha molecular` | **210** (censo decía 410) | ~430 | Cursos (ACPP ×2, NOVA), kits, tiendas; informativo casi todo brasileño; con AIO | ⛔ desplazado |
| 14 | `massa mãe` | **1.600** | ~1.680 prof. | Doméstica en cabecera, **hueco profesional virgen** | ✅ sube al puesto 11 |
| 12 | `cocktails` | 9.900 | — | Recetas de consumo, **PAA en inglés**, IBA/Wikipedia/Continente | ⛔ descartado |
| 13 | `food truck` | 2.400 | — | OLX, fabricantes de vehículos, `local_pack` de 9 | ⛔ descartado |

**Cola restante (12 → 14):** `cozinha molecular` · cocktails y food truck
**replanteados** (las cabeceras no sirven; si se hacen, hay que buscarles una
variante profesional con volumen propio) · `pão de fermentação natural` queda
absorbido por el post 11.

---

## Lo aprendido en esta tanda

### 1. ⚠️ `scripts/dataforseo.py` mide ESPAÑA por defecto — y no avisa

`LOC_ES, LANG_ES = 2724, 'es'`. La primera pasada de research daba `garum` =
**12.100** y `fermentação` = **10**, que es la firma inconfundible de estar
midiendo el mercado equivocado: un término portugués con volumen ridículo al
lado de uno latino con volumen enorme.

En Portugal (`--pais 2620 --idioma pt`) `garum` son **1.300**. **Un factor 9 de
diferencia, y el helper no dice en ningún sitio qué país está midiendo.** Todo
research de un blog que no sea el ES tiene que pasar `--pais` y `--idioma`
explícitos, siempre. *(Candidato a fix: que el helper imprima el país en la
cabecera de la tabla.)*

### 2. El censo del roadmap falla en las DOS direcciones, no solo a la baja

Tres tandas refutándolo a la baja habían creado la costumbre de desconfiar. En
la 4 los dos datos aguantaron al alza. En la 5: `garum` confirma exacto,
`cozinha molecular` **se parte por la mitad** y `massa mãe` aparece con 1.600
donde el roadmap ni lo priorizaba. **Re-medir es re-medir, no buscar
confirmación de que el roadmap miente.**

### 3. La regla 7 (marcas homónimas), segunda confirmación seguida — y ya es regla

`massa mãe padaria` (210) es **SERP de marca pura**: hay una panadería llamada
«Massa Mãe» en la Estrada de Benfica y otra en São Miguel. El AI Overview de esa
consulta **no define nada, describe la panadería**, y el PAA descarrila hasta
«contraindicações do carvão vegetal».

En la **cabecera** `massa mãe` (7,6× más volumen) esas marcas solo ocupan #2 y
#5 y dejan libres todos los puestos informativos. Exactamente lo que pasó con
`mise en place` en la tanda 4. **Ya no es una excepción: la variante cualificada
tiende a estar MÁS contaminada por marcas que la cabecera. Mirar siempre las
dos, y titular en la cabecera.**

### 4. El volumen alto es una trampa cuando el PAA está en otro idioma

`cocktails` da **9.900/mes en Portugal** y era el número más alto de toda la
cola. Su PAA está **íntegramente en inglés** («What are the top 10 cocktails?»,
«What are the 50 classic cocktails?») y el top lo forman IBA World, Wikipedia,
Continente y blogs de recetas para casa. Es intención de consumo, no
profesional, y Google ni siquiera la trata como consulta portuguesa. **El PAA en
otro idioma es la señal más barata de que la SERP no es la que crees.**

### 5. El hueco por calidad, tercera vez seguida — y ahora con arqueología

- **Garum**: `pt.wikipedia` es el **#1 en Portugal** y define el garum por
  «sangue, vísceras… do atum». Eso describe el **`haimation`**, una variante
  mediterránea de lujo. El **#9 de la misma página** dice lo contrario («o
  líquido claro e dourado», que es el `flos gari`). Y el dato que no está en
  ninguna fuente portuguesa: **Espregueira Themudo et al., 2025, *Antiquity*
  (Cambridge)** secuenció ADN de una cuba de salga romana en **Adro Vello, O
  Grove**, datada **cal AD 162-321** — 12 genomas mitocondriales completos, todos
  **sardinha europeia (*Sardina pilchardus*)**, y **pescado entero machacado**,
  no vísceras. **El garum atlántico era otro producto que el mediterráneo de
  lujo**, y el lector portugués recibe hoy la descripción del segundo.
- **Massa mãe**: el PAA pregunta literalmente «O que é a farinha 65?» y nadie
  responde con el dato legal. Está en la **Portaria n.º 254/2003, de 19 de
  março** (DR I Série-B n.º 66, extraída del PDF oficial). Y ahí está el hueco:
  **el glúten seco mínimo es 8 % IDÉNTICO de T45 a T110**. El tipo mide **cinza**
  (extracción del molino), **no fuerza** — «usa T65 porque es la del pan» no dice
  nada sobre si aguantará una fermentación larga. Eso lo dice la **W**, que no
  forma parte de la clasificación legal. **El mismo patrón del mirepoix: un
  número servido como dogma que no mide lo que la gente cree.**

### 6. Endurecer el prompt contra fugas funciona a medias — y hay que leer igual

La tanda 4 dejó dos fugas literales del prompt impresas en el artículo. Esta vez
el prompt lleva un bloque explícito («las líneas de este briefing son
INSTRUCCIONES, nunca las copies») y una lista de expresiones prohibidas.
**Resultado: de dos fugas a tres, pero distintas** — «Este é o bloco mais
importante do artigo», «O que se pede a quem lê…» y «Há ainda uma nota prática».

La lección real: **una instrucción redactada como prosa se imprime como prosa.**
Las tres fugas venían de líneas mías que *sonaban* a texto de artículo. Lo que
funciona no es prohibir copiar: es **no escribir instrucciones que se puedan
leer como contenido**. Pendiente para la tanda 6: redactar cada directiva en
imperativo seco y en mayúsculas, o moverla fuera del bloque de DADOS FIXOS.

### 7. Defectos de bridge en esta tanda: 30 en dos posts

Los que costaban credibilidad:

- **Garum: «Não há fermentação microbiana no sentido estrito»** — falso (hay
  bacterias halófilas) y, sobre todo, **contradecía la propia sección de
  seguridad dos secciones más abajo**: si no hubiera riesgo microbiano, sobraría
  la barrera contra *C. botulinum*. **La contradicción interna ya no aparece
  solo entre la FAQ y el cuerpo: aparece dentro del cuerpo.**
- **Garum: el molho de soja como «antepassado direto» del garum.** Es una
  fermentación de soja de origen chino, independiente. Dato inventado fuera de
  los DADOS FIXOS.
- **Garum: la sardina elegida «porque tinha o teor de gordura certo para a
  fermentação».** Racionalización inventada, y encima dudosa (el pescado graso
  oxida antes).
- **Garum: cercas markdown ```html … ``` envolviendo todo el cuerpo**, con el
  prompt prohibiéndolas expresamente.
- **Massa mãe: la Q4 de la FAQ abría con «Sim, o frigorífico é uma ferramenta
  útil»**, contradiciendo la tesis del cuerpo (el frío es una pausa, no una
  forma de gestión). **Es el defecto de la Q5 de la tanda 4, calcado.** Leer
  siempre la FAQ CONTRA el cuerpo.
- **Massa mãe: la duplicación literal intro ↔ primer `<h2>`, cuarta tanda
  seguida.** Ya no hay que buscarla: hay que darla por hecha y corregirla.
- **Massa mãe: enunciaba la fórmula de la DDT y no la aplicaba nunca.** No es un
  error, es una carencia — y es la diferencia entre entenderla y no entenderla.
  Se le añadió un ejemplo resuelto.

### 8. Dos errores MÍOS, del mismo tipo que los que persigo

1. **El script de fixes no era idempotente.** El fix que *inserta* un párrafo
   antes de un ancla dejaba el ancla presente, así que la segunda pasada lo
   insertaba otra vez. Es la lección «los ensambladores tienen que ser
   reejecutables» aplicada a los scripts de fix: **si un fix inserta en vez de
   sustituir, necesita un centinela propio**, no basta con comprobar que el
   texto viejo ya no está.
2. **Corregí una afirmación falsa en un sitio y la dejé viva en otro.** El
   cuerpo del garum decía en el cierre que era «o antepassado direto» del molho
   de soja; lo corregí a «antepassado direto da colatura di alici e parente
   próximo dos molhos asiáticos». Pero **un párrafo anterior seguía diciendo que
   era el antepasado directo del nam pla y del nuoc mam** — o sea que mi propio
   fix creó una **contradicción interna**, justo el defecto que le había
   reprochado a bridge dos horas antes. Lo cazó una relectura de mis propios
   cambios. **Regla: después de corregir una afirmación, grep de la afirmación
   —no del texto que sustituiste— por todo el documento.**
3. **Mi ejemplo de la DDT no cuadraba si el lector hacía la cuenta.** Escribí
   «no inverno, com a sala a 16 °C… água a 41 °C», pero 41 solo sale si la
   **harina** también baja a 16. Con la harina fija en 22 salen 35. Es
   literalmente el defecto de «aritmética inventada que no cuadra» de la tanda
   4, cometido por mí al redactar el añadido. **Todo número que el lector pueda
   verificar hay que verificarlo con una calculadora, aunque lo hayas escrito
   tú.** El ensamblador lleva ahora `assert` de los tres valores.

### 9. `bridge.py` devolvió vacío DOS veces con DeepSeek — y lo resolvió el modelo

La FAQ del post 10 volvió vacía con `--max-tokens 24000` **y otra vez con
48000**, las dos con el mismo aviso: «el presupuesto se agotó en tokens de
razonamiento antes de emitir una sola palabra». La segunda tardó **21 minutos**
en decirlo. La FAQ del post 11, con el mismo formato y 24000, salió a la
primera.

**No es un umbral: es el prompt.** El del garum lleva umbrales regulatorios,
taxonomía latina y dos reglamentos, y el modelo de razonamiento se atasca ahí.
Subir a 96000 era apostar a más de lo mismo.

Se resolvió con `--model anthropic/claude-sonnet-4.6` y **8192 tokens**, en
menos de dos minutos. Sigue siendo `bridge.py` — CLAUDE.md ya dice que el
modelo es un parámetro y que el contenido donde un carácter cambia el
significado pide modelo bueno. Una FAQ con «400 mg/kg» y «5 % de sal en fase
acuosa» es exactamente ese caso.

**Regla: si bridge devuelve vacío dos veces, no dupliques el presupuesto una
tercera — cambia de motor.**

### 10. Tres gotchas de conteo, todos en la misma sesión

- **`grep -o '<loc>' dist/sitemap-*.xml`** cuenta también el `sitemap-index.xml`,
  que tiene su propio `<loc>`. Daba 1190 y el número real era 1189. Estuve
  investigando un «+3» que no existía.
- **`grep -c` en el sitemap live cuenta LÍNEAS**, y el XML servido va en una
  sola: devolvía `1`. Es el gotcha que ya está en mi memoria y volví a pisarlo.
  Ocurrencias = `grep -o … | wc -l`.
- **`grep -o -E "[^<>]{0,60}(A|B|C)[^<>]{0,60}"`** sobre un HTML de 13 KB agotó
  los 120 s por backtracking catastrófico. Para sacar contexto alrededor de una
  aguja, Python con `re.finditer` y rebanadas.

### 11. Mi propio gate tumbó el ensamblado por no leer la negación

El `assert` que escribí para que la FAQ no contradijese al cuerpo sobre la
histamina buscaba `histamina … destrói … cozinh` y saltó contra
**«a histamina é termoestável — NÃO se destrói a cozinhar»**, que es justamente
la frase correcta. Es el mismo fallo que el gate del «1982» y el del IVA que ya
están en CLAUDE.md: **el patrón tiene que leer la frase, no la coincidencia de
palabras.** Corregido a mirar una ventana de 60 caracteres antes de la
coincidencia y exigir `não|nem|nunca|jamais`.

### 12. La FAQ contradijo al cuerpo POR TERCERA TANDA SEGUIDA

Y esta vez en los dos posts a la vez:

- **Post 11, Q4**: «Sim, o frigorífico é uma ferramenta útil» contra la tesis
  del cuerpo (el frío es una pausa, no una forma de gestión).
- **Post 10, Q1**: decía que el garum es «antepassado direto» de las salsas
  asiáticas *y* de la colatura — contradiciendo al cuerpo **y a su propia Q5**,
  que dice que la colatura es «a descendente mais direta». Contradicción triple
  dentro de la misma pieza.

**Leer la FAQ contra el cuerpo ya no es una recomendación: es un paso del
pipeline.** Los dos ensambladores llevan ahora `assert` que lo vigilan.

---

## Estado exacto de lo que hay en disco

Todo en `.work/` (**gitignorado**: solo existe en el VPS).

| Fichero | Estado |
|---|---|
| `.work/post10-pt-garum/datos-fijados.md` | ✅ research completo, fuente por fuente |
| `.work/post10-pt-garum/prompt10pt.txt` | ✅ |
| `.work/post10-pt-garum/cuerpo10pt.html` | ✅ 2.775 palabras, 6 `<h2>`, 2 tablas, 14 fixes aplicados |
| `.work/post10-pt-garum/fixes10.py` | ✅ reejecutable |
| `.work/post10-pt-garum/faq10pt.raw.txt` | ✅ (hizo falta `--model anthropic/claude-sonnet-4.6`, ver lección 9) |
| `.work/post10-pt-garum/meta10pt-opciones.txt` | ✅ (título y meta ya elegidos, en el ensamblador) |
| `.work/post10-pt-garum/assemble10pt.py` | ✅ **ejecutado**, todos los checks verdes |
| `.work/post11-pt-massa-mae/datos-fijados.md` | ✅ |
| `.work/post11-pt-massa-mae/prompt11pt.txt` | ✅ |
| `.work/post11-pt-massa-mae/cuerpo11pt.html` | ✅ 2.282 palabras, 6 `<h2>`, 2 tablas, 14 fixes + ejemplo DDT |
| `.work/post11-pt-massa-mae/fixes11.py` | ✅ reejecutable (con centinela) |
| `.work/post11-pt-massa-mae/faq11pt.raw.txt` | ✅ (el fix de la Q4 va en el ensamblador) |
| `.work/post11-pt-massa-mae/meta11pt-opciones.txt` | ✅ |
| `.work/post11-pt-massa-mae/assemble11pt.py` | ✅ **ejecutado**, todos los checks verdes |
| **Las 6 imágenes** | ⛔ **BLOQUEADAS — sin crédito en Gemini** |
| Los dos `.md` en `astro-site/src/content/blog/pt/` | ✅ creados y commiteados en `wip/blog-pt-tanda5` |

### Fichas de los dos posts

| | Post 10 | Post 11 |
|---|---|---|
| Slug | `garum` | `massa-mae` |
| Categoría | `tecnica-e-receitas` | `tecnica-e-receitas` |
| Título | Garum: o que era realmente o molho romano fabricado em Tróia (60) | Massa mãe numa padaria profissional: rácios, temperatura e farinha (66) |
| AIO en la SERP | no | **sí** |
| CTA | Fermentus Con AI+ `fermentus-con-ai-wg1xo-pt` | Padaria Criativa `panaderia-creativa-fh0tk-pt` |
| Salientes | `controlo-de-temperaturas`, `haccp`, `alergenios` | `controlo-de-temperaturas`, `food-cost`, `garum` |
| Recíprocos | `higiene-e-seguranca-alimentar` → 10 | 10 → 11 y `food-cost` → 11 |

Los dos CTA verificados hoy contra `.work/ptapp-agentes.json` por el par
`"formid"`/`"formtitle"`. La descripción de Fermentus cita **garums**
literalmente.

## Imágenes — los 6 prompts, listos para cuando haya crédito

Generador ya escrito y probado hasta el punto del 429:
`/tmp/claude-0/.../scratchpad/genimg.sh <nombre> "<prompt>"` (curl a fichero
según la regla del VPS, y optimización a JPG 1376×768 con PIL, calidad 78 —
`sips` no existe en Linux). Destino `astro-site/public/blog-assets/2026/08/`.

Reglas que valen para las seis, destiladas de los rechazos de las tandas 3 y 4:
**NO hands, NO arms, NO people** (ninguna de estas escenas los necesita, y las
manos son la fuente de casi todos los rechazos), sin marcas legibles, sin
anillos, y si hay display **plano hacia la cámara y en foco, dictando el valor
dígito a dígito**.

| Nombre | Escena |
|---|---|
| `garum-pt-destacada.jpg` | Bodegón oscuro sobre pizarra: frasco de vidrio con salsa ámbar translúcida, sal marina gruesa esparcida, tres sardinhas enteras. Luz lateral dura, fondo oscuro |
| `garum-pt-troia.jpg` | Ruinas romanas de cubas de salga (`cetariae`): tanques rectangulares de piedra alineados junto a un estuario, arena y agua al fondo, atardecer. Vista elevada en diagonal |
| `garum-pt-uso.jpg` | Bancada de acero: frasco cuentagotas con líquido ámbar enfocado en primer plano, sartén con salsa reduciendo desenfocada al fondo |
| `massa-mae-pt-destacada.jpg` | Obrador: cubeta transparente con masa madre burbujeante marcada con elástico de nivel, sobre acero, junto a hoja de registro manuscrita y termómetro de sonda |
| `massa-mae-pt-temperatura.jpg` | Sonda digital clavada en masa; **visor plano a cámara y en foco marcando 25,0 °C** (dictar: dígito dos, dígito cinco, punto decimal, dígito cero, símbolo de grados) |
| `massa-mae-pt-farinhas.jpg` | Cuatro cuencos blancos en fila sobre madera con harinas de extracción creciente, del blanco puro al integral oscuro. Sin texto ni etiquetas |

Los `alt` y los `figcaption` definitivos ya están dentro de los ensambladores.

## Lo siguiente, después de desbloquear

1. Publicar la tanda 5 (pasos de arriba).
2. **Ventana de GSC del PT: 15-22 de septiembre**, por página+query, con la
   trampa de la URL legacy presente. Posts 1-6 desde el 21-22 de agosto, 8-9
   desde el 28, 10-11 desde que se publiquen.
3. Maduración de IT (17-ago), FR (18-ago) y DE (19-ago): **8-15 de septiembre**.
4. Librerías EN tras el arreglo del `robots.txt`: **3-sep** (¿rastreadas?) y
   **17-sep** (¿indexadas?).
5. **Deuda de SEO sin tocar — `llms.txt`**, medido hoy:
   - Dice «**Spanish-language** SaaS» cuando el blog ya va en 6 idiomas.
   - Dice «**30** downloadable digital products» dos veces; las landings de
     producto vivas son **44** (`astro-site/src/pages/` con prefijo
     `guia- kit- mega- pack- plan- pro-`, sin contar las 88 de `-access`/`-library`).
   - **No lista ni una sola URL del blog**: 0 ocurrencias de `aichef.pro/blog`,
     con 322 posts ES, 65 EN y los de IT/FR/DE/PT.
   - Está **duplicado byte a byte** en `public/llms.txt` y
     `astro-site/public/llms.txt` (`cmp` idénticos), los dos de julio. Solo se
     publica el de `astro-site/`. El gate `public/` vs `astro-site/public/`
     sigue sin escribirse — es la misma trampa que dejó assets huérfanos en el
     cutover.

   ⚠️ **Hallazgo colateral, de la pista de John (no tocado):**
   `src/data/products-catalog.ts` —que CLAUDE.md declara fuente única para los
   banners— tiene **25 entradas**, y CLAUDE.md dice 22. Hay **44 landings**
   vivas. O sea que el catálogo cubre poco más de la mitad de los productos que
   se venden, y cualquier banner o listado que salga de él ignora al resto.
   **No se ha tocado nada**: es la pista de productos digitales, que va por su
   cuenta y solo se trabaja desde el Mac.
6. Pendientes de John, sin cambios: checkouts de ptapp/nlapp con el plan de 10 €
   (el blog PT manda tráfico a `ptapp.aichef.pro` desde **ocho** posts, diez
   cuando salga esta tanda), cutover de enblog, catálogo italiano, etiqueta de
   conversión en itapp, y la solicitud manual de indexación de las librerías EN.

---

## 🅱️ Segundo frente de la sesión: el catálogo de productos vendía la MITAD

**Ya está en `main` y desplegado** (commit `29a9714`, verificado en producción).
Nada pendiente aquí.

**Lo que John pidió:** el catálogo es la herramienta para vender los productos
en los contenidos, y los banners tienen que cubrirlos **todos**, no siempre los
mismos. Los productos digitales quedan fuera de esta pista en cuanto a
*desarrollo*; mantener el catálogo para venderlos, no.

**Medido sobre los 198 banners publicados:** sólo **19 productos distintos de
44**. `kit-escandallos` se llevaba 60 (el 30 %) y los cuatro primeros el 61 %.

**Tres causas encadenadas, ninguna daba error:**

1. `src/data/products-catalog.ts` tenía **22 entradas y hay 44 landings vivas**.
   Los otros 22 eran imposibles de poner en un banner.
2. ⚠️ **El parser perdía entradas en silencio.** `kit-gestion-personal` lleva
   comentarios entre `description: {` y `es:`; el regex exigía sólo espacios,
   no casaba, y el `.*?` saltaba a la entrada siguiente — que **desaparecía**.
   Así llevaba `kit-inventario` invendible.
3. La elección era manual en cada config.

**Hecho:** catálogo a 44 (datos de la ficha real de cada producto), regex
tolerante a comentarios y con corte en el siguiente producto, **gate de
recuento**, y `rotar_productos()` (fijar por tema + rotar el resto,
determinista por slug). Simulado sobre 325 posts ES: **44/44, el más usado del
30,3 % al 3,7 %**. Y **descripción falsa retirada de 3 posts vivos**.

**Queda anotado, sin tocar (pista de John):** las fichas de producto viven en
`astro-site/src/data/productos/` y son la fuente autorizada de nombre y precio.

---

## ⚠️ Corrección de lo que dije durante la sesión

Al cerrar el frente del blog afirmé que **no había empujado nada**. Era falso:
los dos commits de `main` (`4ab6a20` el handoff y `29a9714` el catálogo)
**estaban ya en `origin/main`** y por tanto desplegados. No he encontrado qué
los subió —no hay hooks en `.git/hooks/`, ni crontab de usuario, ni cron de
sistema que toque este repo— así que **no des por hecho que un commit local
sigue sin publicar: compruébalo con `git rev-list --left-right --count
origin/main...main` antes de afirmarlo.** La rama `wip/blog-pt-tanda5` sí está
confirmada como local-only (`git ls-remote --heads origin` no la lista), que es
lo que importaba para no publicar los posts sin imágenes.
