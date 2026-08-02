# SESSION HANDOFF — 2026-08-01 (cierre): los 2 glosarios ultradelgados, ampliados

> Continúa `SESSION_HANDOFF_2026-08-01-B.md`. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` §8.
> Sesión corta desde el VPS. **Un commit** (`1a43285`), pusheado y verificado en producción.

## ✅ Qué se ha hecho

Cerrada la **única pendiente que no dependía de nadie** de las tres del handoff anterior.

| | token | llm |
|---|---|---|
| Antes | **49 palabras**, 0 imágenes, sin FAQ | **78 palabras**, 0 imágenes, sin FAQ |
| Ahora | **1.414 palabras** | **1.959 palabras** |
| Tablas · FAQ · imágenes · banners | 2 · 8 · 2 · 3 | 2 · 8 · 2 · 3 |

Los dos **emiten ahora `FAQPage`**, que antes no hacían, y quedan **enlazados entre sí** (el LLM
predice el siguiente token), más 4 enlaces internos nuevos hacia IA generativa, machine learning y
los dos posts de prompts.

## 🔎 El research cambió el enfoque en los dos casos

Ninguno de los dos posts se escribió para la keyword obvia, y en los dos casos por el mismo motivo:
la SERP decía que esa pelea no se gana.

- **«qué es un token» (1.600/mes) es una SERP de CRIPTOMONEDAS y ciberseguridad** — BBVA, Wikipedia,
  Finect, Fortinet, Kraken. La acepción de IA sólo asoma en las posiciones 10 y 13 (Xataka). No se
  pelea: se va a «token ia» (110/mes) y se **despacha la confusión en la segunda sección**, que es
  literalmente lo que Google pregunta en el People Also Ask («¿Qué es un token de IA?» → «Ambos
  conceptos no guardan relación alguna»).
- **«qué es un LLM» (4.400/mes) lo copan IBM, AWS, Cloudflare, Google Cloud, Salesforce y Wikipedia.**
  No se les gana la definición genérica y no se intentó. El peso del post va a la capa que **ninguno
  de ellos cubre porque ninguno escribe para hostelería**: qué NO sabe hacer un LLM en una cocina.
  Puede inventarse un gramaje, una temperatura de cocción o pasar por alto un alérgeno. *El LLM
  propone, el profesional valida.* Es la sección más larga del artículo y es información de
  seguridad alimentaria.

**Cero canibalización, confirmado en GSC**: «token» tiene **0 impresiones en 90 días en todo el
dominio** y «llm» tiene **1**, en una URL vieja del blog inglés. Tampoco hay otro post del corpus
con un `<h2>` sobre ninguno de los dos conceptos.

Los dos tienen **AI Overview** en su SERP, así que cada sección abre con una respuesta directa y
citable antes de desarrollar.

## 🐛 Un defecto publicado la víspera, cazado y arreglado

**El parser de `fase8d-ampliar-glosario.py` no contemplaba listas.** Las viñetas de bridge (`- …`)
caían al caso de párrafo, así que las **7 del equipamiento de `cocina-molecular` se estaban
sirviendo como párrafos sueltos empezados por «- », sin `<ul>`**. Ahora emite
`<ul class="wp-block-list">`, que es la convención del corpus (1.489 usos frente a 946 de `<ul>`
pelado). Sólo afectaba a ese post: barrido el corpus entero, 0 casos restantes.

### Y al arreglarlo me cargué dos enlaces internos

Regenerar `cocina-molecular` para reparar las viñetas **se llevó por delante los 2 enlaces internos**
(`espumas` y `esferificación`) que se le habían añadido a mano después de la primera pasada: el
ensamblador reconstruye el cuerpo ENTERO desde el `.txt` de bridge, que no los tiene.

Repuestos y verificados contra `HEAD`. **Lo peligroso es que el diff no canta**: las dos líneas
siguen ahí, sólo que sin el `<a>`. Queda avisado en el docstring del script y en `CLAUDE.md`.

## 🧪 Verificación

Gates, todos en verde tras el build final:

| Gate | Resultado |
|---|---|
| `fase8b-gate.py` | 3.549 checks · 0 fallos |
| `fase8c-enlaces-vivos.py` | **194 destinos · 0 rotos** |
| `fase8c-h1-unico.py` | 0 `<h1>` en cuerpo |
| `fase8c-restos-wordpress.py` | 0 posts con restos |
| `fase8c-quitar-relacionados.py` | 0 posts con el widget |
| `fase8c-libreria-en-gate.py --todos` | 26/26 sin errores |

Build verde, **1.248 páginas**. Comprobado en el HTML del `dist`, no en el `.md`: 1 solo `<h1>`,
tablas con `.table-scroll`, `<ul>` correcto, 0 guiones sueltos y **`FAQPage` con 8 `Question`** en
los tres posts tocados.

## 🚧 Sigue pendiente de John (sin cambios)

1. **El listado inglés completo de agentes**: los 77 nombres y los de los 15 módulos del menú. Sin
   ellos el hub `/en/prompt-libraries` no puede ser el catálogo completo. **No se deduce del código.**
2. **Alias de `enblog.aichef.pro` en Netlify + DNS** (`CUTOVER_ENBLOG_PENDIENTE.md`), con la trampa
   de las A records de Hostinger.

## 📋 8D: lo que queda medido, para no volver a contarlo

Censo del glosario tras esta tanda: **71 entradas, mediana 1.345 palabras** (era 1.285; la subieron
estas dos). El resto del blog está en 2.661.

**Por debajo de 400 palabras — el umbral bajo el cual el `CLAUDE.md` dice que un post no compite ni
siendo glosario:**

| Palabras | Slug | Nota |
|---|---|---|
| 226 | `yuzu-kosho-condimento-japones-tendencia` | |
| 274 | `mise-en-place` | **El más goloso con diferencia: 4.400 búsquedas/mes** (medido con DataForSEO), competencia baja y demanda plana todo el año. 274 palabras para eso es dinero tirado |
| 331 | `chile-crisp-condimento-viral-2026` | |
| 359 | `coccion-a-baja-temperatura-concepto-y-definicion` | Ojo canibalización con `tecnicas-de-coccion-al-vacio-sous-vide` (657) |

**Entre 400 y 700, segunda tanda posible (8):** `que-es-la-inteligencia-artificial-generativa` (400),
`tecnicas-con-sifon-concepto-y-definicion` (413), `esferificacion-concepto-y-definicion` (421),
`que-es-el-maiz` (422), `espumas-ferran-adria-concepto-y-definicion` (442),
`api-interfaz-programacion-hosteleria` (614), `procesamiento-de-lenguaje-natural` (649),
`tecnicas-de-coccion-al-vacio-sous-vide` (657).

⚠️ **Antes de ampliar cualquiera de estos, el chequeo de canibalización** (dos consultas: `ls` de
slugs con el término y GSC agrupando por `page,query`). En esta tanda salió limpio, pero en
`food-pairing` el research dijo que NO se inflara.

## 🧭 Qué sigue

- Los ~58 agentes españoles sin librería de prompts (12 de ellos el bloque de hotelería).
- Las páginas por agente de 8C, que siguen sin arrancar.
- La tanda 8D de arriba: 4 entradas bajo 400 palabras.
- Vigilar en GSC las 119 free tools que pasaron a SSR: es el cambio con más potencial y
  todavía es pronto para leer nada.
