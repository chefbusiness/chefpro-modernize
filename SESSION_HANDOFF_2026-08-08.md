# SESSION HANDOFF — 2026-08-08: FAQ duplicadas, dos recetarios y el bug del CJK

> Continúa `SESSION_HANDOFF_2026-08-04.md`. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8.
> Sesión desde el VPS. **5 commits** (`20db731`, `67b09fc`, `acb2a72`, `2b4a212`, `5c0cf4b`), todos pusheados y verificados en producción.

## ✅ Bloque 1 — FAQ duplicadas: 3 posts arreglados y un gate nuevo

Salió de un cabo suelto del día 4: el pilar de sous vide tenía «¿Qué es la
técnica sous vide?» y «¿Qué es el sous vide?» como dos `Question` distintas.

| Post | Antes | Ahora |
|---|---|---|
| `sous-vide-concepto-definicion` | 12 | **11** |
| `chili-crisp` | 9 | **7** |
| `yuzu-kosho-condimento-japones-tendencia` | 8 | **7** |

`chili-crisp` tenía **cuatro** preguntas «qué es». Y lo grave no era la
redundancia: **en un rich result cada `Question` aparece SOLA**, y la respuesta
de «¿Qué es un chili crisp?» abría con «Es exactamente lo mismo». Fuera de
contexto no dice nada.

**Gate nuevo: `fase8d-faq-duplicadas.py`.** Compara normalizado (sin tildes, sin
palabras vacías, Jaccard + ratio de secuencia) porque los duplicados vienen de
recoger varias formulaciones del **People Also Ask**, que difieren en artículos,
orden y hasta en la grafía. Tres niveles (IDENTICA / DEFINICION / PARECIDA)
porque el ruido es alto: dos preguntas del mismo tema comparten casi todo el
vocabulario sin ser la misma.

**Dos hallazgos del barrido del corpus completo:**

1. **Sólo 93 de los 322 posts ES tienen `faq:` en el frontmatter.** Otros 149 la
   llevan SÓLO en el cuerpo (molde WordPress: `<h3>` o `<p><strong>`) y 80 no
   tienen ninguna. **Mirar sólo el frontmatter deja fuera al 71 % del corpus.**
   El script lee las dos vías y marca cuál emite schema.
2. Fuera de los 3 arreglados **no hay más duplicados**. Los 26 avisos al umbral
   laxo son falsos positivos. Dos parecían reales y no lo eran: en
   `mise-en-place` los «3 tipos» y los «4 tipos» están **a propósito** (el PAA
   pregunta las dos y las respuestas resuelven la discrepancia: son dos ejes de
   clasificación), y en `cual-es-la-mejor-ia-para-la-alimentacion` una es
   paraguas y la otra baja al caso restaurante.

**Validado con control negativo** contra el corpus previo: marca los 10 pares que
ya se habían corregido a mano. Ese control destapó un agujero del propio
detector —«chilli crisp» y «chili crisp» no comparten ningún token, así que la
variante de **grafía** se colaba, justo el origen de la mitad de los duplicados—;
el sujeto se compara ahora también por ratio de secuencia.

## ✅ Bloque 2 — Dos cifras del censo, corregidas contra la fuente viva

- Las URLs migradas del clúster sous-vide sumaban **8 impresiones** en 90 días,
  no 4. Los 0 clics sí eran correctos, que es lo que sostiene la consolidación;
  el argumento de fondo era estructural. La cifra estaba en tres documentos y en
  un docstring.
- El blog EN son **65 posts**, no 39. Los 39 eran la foto de la Fase 8B.6; las
  tandas 8C del 2026-08-01 añadieron 26. Contados en el **sitemap de
  producción**, que es la fuente viva.

## ✅ Bloque 3 — Cocina Española y Cocina Italiana (hub: 27 → 29 de 85)

```
cocina-espanola-ai   8.441 pal · 7 tablas · 105 prompts · 10 FAQ · 3 banners
cocina-italiana-ai   8.520 pal · 7 tablas · 105 prompts · 10 FAQ · 3 banners
```

Los 7 bloques son **distintos en cada uno a propósito**: el español gira sobre
regiones, escandallo con precios HORECA de tu ciudad y ficha técnica; el italiano
sobre primi, producto DOP con alternativas accesibles cuando no llega a España, y
dolci. Si fueran calcados, los 27 recetarios pendientes acabarían siendo el mismo
post 27 veces. **El molde de los 7 bloques se toma de los posts ya publicados**,
no se inventa; lo que se diferencia es el contenido de cada bloque.

**Los dos prompts core confirman que los recetarios NO comparten plantilla:** el
español es prosa de una generación anterior, el italiano lleva investigación
previa obligatoria, columna de merma explícita, DOP/IGP y utensilio tradicional
por fase. **No generar los 27 configs desde uno solo.**

**`fase8c-hub-registrar.py`, nuevo.** El catálogo vive **duplicado**: la fuente
declarada es `fase8c-agentes/catalogo-hub.json`, pero la página del hub lleva su
propia copia **inline** y no lo importa. Tocar sólo una deja el hub sin el enlace
o el JSON mintiendo, y **ninguna de las dos cosas rompe el build**: el contador
«X de Y con librería» simplemente no sube.

## 🔴 Bloque 4 — El motor de redacción cambia para esta familia (autorizado por John)

John avisó de que bridge traía «caracteres chinos y demás». Medido, era peor.

**`fermentus-ai` tenía 24 inyecciones CJK**, frases chinas enteras dentro de
prompts. Tres de verdad graves:

- **«鬼笔鹅膏菌提取物替代»** en un prompt de garum vegano. 鬼笔鹅膏菌 es
  ***Amanita phalloides***, la seta más venenosa que existe. Debía decir «en
  sustitución de la fermentación bacteriana».
- **«但是 (dulce/animal)»** — 但是 significa «pero», usado como descriptor de aroma.
- **«历代 (jengibre fresco)»** — 历代 significa «dinastías sucesivas».

Más `consultor-gastronomico-ai` («가스» = gas en coreano, y un «gaz natural» en
francés) y, buscando eso, **un tercero que no estaba en el radar, en el blog
inglés**: `customer-retention-strategies-restaurants`, con «You never know
what惊喜 (surprise) might come». **Los tres estaban vivos en producción.** De
paso se quitó de `fermentus` la mención a un restaurante y un cocinero reales,
que el `SYSTEM` del ensamblador prohíbe expresamente.

Y un **segundo defecto que nadie había visto**: 41 menciones a años pasados,
casi todas «precios HORECA de mayo de 2025» en prompts de escandallo. Pedirían
datos de hace 15 meses y contradicen al propio agente.

**Por qué aquí y no en un artículo normal:** son tablas de 105 prompts que el
lector **copia y pega tal cual** en la plataforma. En prosa un desliz se lee;
dentro de la fila 63 de una tabla, se ejecuta.

**Se hicieron las dos cosas, y hacían falta las dos:**

1. `MODELO = 'anthropic/claude-sonnet-4.6'` en `fase8c-libreria-assemble.py`,
   sobreescribible con `--modelo`. `bridge.py` ya aceptaba `--model`, así que el
   cambio de motor es un parámetro.
2. **`valida()`, que aborta con CUALQUIER modelo** ante caracteres no latinos o
   ante un año pasado. Cambiar de motor baja la probabilidad; sólo el gate la
   elimina.

⚠️ **Trampa del gate, cazada en caliente:** su primera versión tumbó el bloque de
*Historia, Región y Relato en la Carta* del italiano por un «1982» que era una
fecha histórica correcta. Ahora un año pasado sólo salta si está a **menos de 90
caracteres de lenguaje de precios** («precio», «coste», «HORECA», «escandallo»,
«€»). Y guarda la respuesta rechazada en `.rechazado`, porque `valida()` corría
**antes** de cachear y no había forma de ver qué había fallado.

Barrido final de todo el corpus (324 ES + 65 EN): quedan 5 posts con caracteres
de otro alfabeto, **los cinco legítimos** — 老干妈 en chili crisp, 北京烤鸭 en el
pato pekinés, 胡椒 en yuzu kosho, y los de bibimbap y pad thai.

## Gates y verificación en producción

```
build                     1.248 páginas
fase8b-gate.py            3.548 checks · 0 fallos
fase8c-h1-unico.py        limpio     fase8c-restos-wordpress.py  limpio
fase8d-faq-duplicadas.py  0 duplicados en los nuevos; corpus limpio
fase8b-regen-lastmod.py   389 entradas
```

En vivo: los dos posts a 200, el hub enlazándolos y «Recetarios de Europa»
pasando de `0 de 12` a `2 de 12`, y **cero CJK** en los tres posts reparados.

## 📌 Siguiente sesión

**Lo único que bloquea:** la **sección de dominio** del prompt core de los dos
recetarios siguientes. Sugerencia: **Cocina Francesa** y **Cocina Mexicana** —
cierran los dos bloques grandes por su lado más buscado y dan un tercer molde
antes de meterse con los 25 restantes. Basta la sección de dominio: el módulo de
escandallos, el de export CSV/PDF y el de confidencialidad son idénticos entre
agentes.

**Cadencia acordada: 1-2 recetarios al día.** El coste por post baja mucho desde
aquí: las configs tienen patrón, los gates están montados y la deuda del CJK ya
está pagada.

**Oportunidad medida esta sesión:** **80 posts ES no tienen FAQ ninguna** (ni en
frontmatter ni en cuerpo). No emiten `FAQPage` ni cubren People Also Ask.
Probablemente la bolsa de mejora más barata del blog. Sin tocar.

## Pendiente de John (sin cambios)

- **`enblog.aichef.pro`**: alias en Netlify + DNS. Las 301 ya están en
  `_redirects` pero no se ejecutan hasta entonces. `CUTOVER_ENBLOG_PENDIENTE.md`.
- Listado inglés de agentes.
- Borrar las dos cuentas `test-gads-*@mailinator.com` y vaciar el campo de
  confirmación antiguo de Pickaxe.
