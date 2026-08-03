# SESSION HANDOFF — 2026-08-02/03: `mise-en-place` y la medición de Google Ads

> Continúa `SESSION_HANDOFF_2026-08-01-C.md`. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8.
> Sesión larga desde el VPS. **5 commits**, todos pusheados y verificados en producción.

## ✅ Bloque 1 — `mise-en-place`, la entrada más valiosa del glosario

| | Antes | Ahora |
|---|---|---|
| Palabras | **274** | **3.733** |
| Tablas · FAQ · imágenes · banners | 0 · 0 · 0 · 0 | **4 · 10 · 2+destacada · 3** |
| `FAQPage` | no emitía | **10 `Question`** |
| Enlaces internos | **0** | **12** (9 posts + 2 calculadoras + CTA con UTM) |

**4.400 búsquedas/mes, competencia BAJA y demanda plana**, servidas con 274
palabras. La SERP la copan blogs de cocina **casera**, Wikipedia y reels; los
únicos rivales serios son dos SaaS de gestión (combohr, happychef). El peso del
artículo va a lo que ninguno cubre: la fórmula de **cuánta** mise en place hay
que hacer, el cronograma por franjas, `prep ≠ mise en place`, el etiquetado/APPCC
y el bloque de hotelería. El People Also Ask pregunta **dos veces** por los tipos
(3 y 4) y nadie resuelve la discrepancia: son **dos ejes de clasificación**, no
cuatro tipos — respondido en dos preguntas separadas de la FAQ.

⚠️ **Al leer el histórico**: las posiciones 46-94 de GSC son de la URL **legacy**
(`blog.aichef.pro/mise-en-place/`, ya 301-eada). La migrada no aparece en ninguna
fila: arranca de cero.

### Tres defectos cazados por la auditoría adversarial, arreglados en el ENSAMBLADOR

No en el post: en `fase8d-ampliar-glosario.py`, para que no se repitan en la tanda.

1. **La FAQ se guarda SIN HTML.** `BlogPost.astro` pinta la respuesta como texto
   plano y la mete cruda en el JSON-LD, así que los `<em>` de bridge se veían
   **literales**: «`<em>`Mise`</em>` viene del verbo…». Eran 20 etiquetas
   visibles. Comprobado que los 4 posts de 8D ya publicados están limpios.
2. **Lo preservado va DETRÁS del primer párrafo.** Con el Loom delante
   (1256×942, 4:3) el lector móvil veía un vídeo entero antes de la definición —
   justo el párrafo que copia el AI Overview. Hay **12 posts con vídeo**.
3. **Se comprueba que el JPG existe en disco.** La aserción anterior sólo miraba
   que el `src` estuviera en el cuerpo: un post con imágenes sin generar se
   publicaba con 404 en silencio.

Y un fallo de aritmética del modelo, corregido a mano: la cadena principal cuadra
(120 × 40 % = 48 raciones → 12 kg ÷ 0,8 = **15 kg**), pero el par level decía
«12 raciones (6 litros)» cuando son **3**.

## 🔎 El research refutó 3 de los 4 posts de la tanda

El censo del roadmap se escribió con menos datos de los que hay hoy:

| Post | Lo que decía el roadmap | Lo que dicen los datos |
|---|---|---|
| `chile-crisp` | 10 búsquedas/mes, casi descartable | Las 10 miden **una falta de ortografía**: el término real es «**chili crisp**» con i, **480/mes** en España (48×). El post dice «chile crisp» 10 veces y «chili» **cero**. Hay que **re-targetizar antes** de ampliar |
| `yuzu-kosho` | modesto, competencia alta | **La victoria más barata**: ya está en posición **9,7-11,7** con 226 palabras. No hay que conquistar la SERP, hay que cruzar de la página 2 a la 1 |
| `coccion-a-baja-temperatura` | canibaliza con sous-vide → 301 | **No canibaliza**: solape de SERP **2/17**, PAA **cero**, y Wikipedia, AEG y Barcelona Culinary Hub mantienen **páginas separadas**. Intenciones distintas: baja temperatura es doméstica («en horno, sin roner»), sous-vide es de equipamiento |

**La canibalización real del clúster está en otro sitio**:
`tecnicas-de-coccion-al-vacio-sous-vide` (657 pal., 0 enlaces entrantes) pelea la
misma query «sous vide» contra `sous-vide-concepto-definicion` y **pierde**
(pos. 85,6 frente a 40,3). Ése es el candidato a 301, no el que señalaba el plan.

## ✅ Bloque 2 — Google Ads: de cero medición a medición verificada

**El sitio no tenía NINGÚN tag** —ni analítica ni publicidad— hasta esta sesión.

- **`aichef.pro`** (1.248 páginas): etiqueta `AW-17829651892` con **Consent Mode
  v2** (denegado por defecto, `ads_data_redaction` + `url_passthrough`) y
  **banner de cookies en los 7 idiomas**. Los textos de es/fr ya existían en los
  JSON de la SPA; los otros cinco se tradujeron con bridge.py.
- **Pickaxe** (workspace español): etiqueta base en `Header` y evento de
  conversión en **`Body`**.
- **Google Ads**: acción *Registro* (`AW-17829651892/-p23CMHO5docELTL67VC`),
  campaña apuntando a ella.

### Lo que costó encontrar (y habría dejado esto midiendo cero)

1. **El alta de Pickaxe es un MODAL, no una página.** No existe «confirmation
   page» en el registro gratuito — esos campos son para **compras**. El plan
   original no se habría ejecutado nunca.
2. **`?success=login` no distingue registro de login.** Llega ahí un alta nueva
   *y* un usuario existente. Lo que sí distingue: el modal de alta es **el único
   con dos campos de contraseña**.
3. **`localStorage` está aislado por origen.** El consentimiento aceptado en
   `aichef.pro` no se leía en `app.aichef.pro`. Se pasó a **cookie sobre
   `.aichef.pro`**, el mismo alcance que usa gtag para `_gcl_aw`.

### Verificado en vivo con Playwright, no deducido

| Prueba | Resultado |
|---|---|
| `gclid` capturado en la landing | `_gcl_aw=GCL.…` ✅ |
| Leído desde `app.aichef.pro` | ✅ (sin cross-domain linker) |
| Consentimiento heredado al subdominio | ✅ |
| Alta nueva → conversión | HTTP 200, `gcs=G111`, `value=1 EUR` ✅ |
| Login de existente → conversión | **cero peticiones**, incluso borrando el candado ✅ |

### 💰 Y el hallazgo que más valía

La campaña tenía como objetivo **«Vistas de una página»**: **principal**,
**inactiva** y con **0,00 conversiones**. Llevaba repartiendo 5 €/día **sin una
sola señal con la que aprender**. Corregido: ahora usa *Registros*, y la acción
pasó de «Configuración errónea» a **Activa** (1 de 1 campañas).

## 🧪 Verificación

Build verde, **1.248 páginas**. Sobre el HTML del `dist`, no sobre el `.md`.

| Gate | Resultado |
|---|---|
| `fase8b-gate.py` | 3.548 checks · 0 fallos |
| `fase8c-enlaces-vivos.py` | **200 destinos · 0 rotos** |
| `fase8c-h1-unico.py` | 0 `<h1>` en cuerpo |
| `fase8c-restos-wordpress.py` | 0 posts con restos |
| `fase8c-quitar-relacionados.py` | 0 posts con el widget |
| JSON-LD tras meter el tag | 0 inválidos |

## 🧹 Limpieza pendiente (de John, 2 min)

1. Borrar las cuentas de prueba `test-gads-20260802@mailinator.com` y
   `test-gads-b-20260803@mailinator.com`.
2. Vaciar el **campo antiguo de confirmación** de Pickaxe: tiene la etiqueta
   pelada, sin Consent Mode y **sin evento**, así que no mide nada y carga la
   etiqueta por segunda vez.

## 🐛 Dos hallazgos colaterales, ninguno buscado

- **La cuarta familia de bloques congelados existe**, como predecía `CLAUDE.md`:
  un `wp-block-group` «CHEFBUSINESS GROUP» en **62 posts**, 1.809 bytes fijos. No
  es basura (son marcas de John, con UTM), así que **no se ha tocado**. Pero en
  los glosarios delgados llega a ser el **21 % del HTML**, y **infla cualquier
  censo de palabras**: `chile-crisp` tiene 263 reales, no 331.
- **`ingredientsindex.pro` tiene el TLS roto** (`tlsv1 alert internal error`;
  sirve 200 por HTTP plano). Está enlazado desde esos 62 posts, así que al lector
  le salta el aviso de seguridad del navegador. **Se arregla en el hosting.**

## 🧭 Qué sigue

1. **`yuzu-kosho`** — la ampliación más rentable del corpus ahora mismo: ya
   rankea en 9,7-11,7 con 226 palabras. Objetivo ~1.300-1.500 (no más: la
   consulta es definicional y los rivales son cortos).
2. **`chile-crisp`** — **re-targetizar a «chili crisp» primero**, luego engordar.
   Si se amplía con la grafía actual se construye sobre arena.
3. **`coccion-a-baja-temperatura`** — como hub paraguas de la familia (horno,
   confitado, baño maría), cediendo el vacío a `sous-vide`.
4. **La canibalización real del clúster sous-vide** (`tecnicas-de-coccion-al-vacio`).
5. Los ~58 agentes españoles sin librería de prompts; las páginas por agente de 8C.
6. Vigilar en GSC las 119 free tools en SSR (a 2026-08-02 sólo el hub tiene
   datos: 220 impr., **pos. 5,2**, 9 clics).

## 🚧 Sigue pendiente de John (sin cambios)

1. **El listado inglés completo de agentes** (77 nombres + 15 módulos del menú).
2. **Alias de `enblog.aichef.pro` en Netlify + DNS** (`CUTOVER_ENBLOG_PENDIENTE.md`).
