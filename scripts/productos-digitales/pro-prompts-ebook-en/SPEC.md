# Gastro Pro Prompts eBook (EN) — SPEC corta

> Tienda internacional en inglés · ola 1, producto 3 · tamaño **S** (techo 2,5 M tokens, objetivo 3-6 h).
> Duplicado del producto ES `pro-prompts-ebook` (regla de John: DUPLICAR y traducir, nunca reconstruir).
> Sesión Claude Code, 3-oct-2026. Reparto: Mac orquesta y redacta con Sonnet; lo pesado al VPS/Netlify.

## 1. Decisiones (delegadas, 3-oct)

| Tema | Decisión | Por qué |
|---|---|---|
| Nombre | **Gastro Pro Prompts eBook** · subtítulo «300 AI Prompts for Restaurants & Hospitality» | La marca de la portada del ES es «Gastro Pro Prompts»; el subtítulo dice lo que es en el idioma de la SERP |
| Slug | `/en/digital-products/ai-prompts-for-restaurants` | SERP US de «chatgpt prompts for restaurants»: Toast «AI Prompt Library for Restaurants» (25 prompts gratis), docsbot… Volumen ~0 en todas las variantes (como en ES: es producto para usuarios de AI Chef Pro, no pieza SEO; John 19-sep: volumen 0 no descalifica) |
| productId | `ai-prompts-for-restaurants` (`lang: 'en'`) | Patrón de la tienda EN: productId = slug EN |
| Precio | **$14**, ancla tachada **$59** (ES: 50 € → 9 €, misma proporción redondeada) | 9 € ≈ $10,5 → escalón psicológico superior. A $14 (≈ 12 €) supera el mínimo de NOWPayments (≈ 10,5 €): **nace con las 3 puertas cripto** (el ES va excluido por los 9 €) |
| Bonos | Valores «$29» y «$25» (ES 27 € y 23 €) | Misma proporción |
| Entrega | Patrón EN moderno (ProductAccessGate + `PRODUCT_FILES` en `public/dl/ai-prompts-for-restaurants/`), **no** el legado «vanilla» del ES (env vars `PDF_*_URL`, AccessGate sin `product`) | El legado es el único punto ciego que ha tenido el gate (sesión 20-ago); el EN nace con la vía estándar |
| Dashboard | Copia traducida de `src/pages/ProPromptsLibrary.tsx` + sus componentes `src/components/library/*` (copias `*En` o prop `lang`, sin tocar el HTML del ES) con datos `src/data/prompts-en.ts` (76 prompts traducidos) | Mismo diseño que el ES |
| Testimonios | Los del ES traducidos tal cual, subtítulo «from the Spanish edition», sin `aggregateRating` | TIENDA §3.5 (John 25-sep) |
| Miselup | Fuera (`miselup={false}`) | TIENDA §3.9 |

## 2. Fuentes (los ficheros PUBLICADOS, no borradores)

- eBook: `astro-site/public/dl/pp-7e48bcc611ef54e4.pdf` (76 págs., Letter, Google Docs). Su .docx (`ProPrompts_eBook_v2_plain`)
  ya no existe → `extraer_es.py` lo vuelca a `es.json` (3 bloques · 33 secciones · 300 prompts · 17.604 palabras) clasificando
  cada línea por fuente/tamaño/color.
- Bonus 1: `astro-site/public/dl/b1-7e48bcc611ef54e4.docx` (≈ 630 palabras, 9 tablas).
- Bonus 2+3: `astro-site/public/dl/b23-7e48bcc611ef54e4.xlsx` (2 hojas, 0 fórmulas, ≈ 1.930 palabras, 53 celdas combinadas).
- Dashboard: `src/data/prompts.ts` (10 categorías, 76 prompts, distintos de los 300 del eBook).
- Landing: `astro-site/src/components/pages/ProPromptsEbookPage.astro` (929 líneas) + `astro-site/src/pages/pro-prompts-ebook.astro`.

## 3. Reglas de traducción (las aplica cada redactor Sonnet)

- **Inglés US**, tono profesional y directo de cocina/sala. Los prompts se copian y pegan: ni una palabra en español,
  ni un carácter no latino, ni un año pasado.
- **Placeholders**: `[MAYÚSCULAS]` → `[UPPERCASE ENGLISH]`, el MISMO número por prompt, opciones separadas por `/`.
- **Agentes**: `App(s) recomendada(s)` → `Recommended agent(s)`; nombres SOLO desde `agentes_en.json` (catálogo de la
  plataforma EN). «apps» de la suite → «agents».
- **Mercado** (US base, válido UK/CA/AU):
  - `euros`/`€` → fuera: `[PRICE]`/`[AMOUNT]` sin moneda (el usuario pone la suya). IVA → «sales tax/VAT».
  - APPCC → HACCP. Reglamento UE 1169/2011 / «14 alérgenos» → «the allergen rules that apply to you (US: the FDA's 9 major
    allergens · UK/EU: the 14 regulated allergens)». «normativa española» → «local regulations in [COUNTRY/STATE]».
    «mercado español» → «[COUNTRY] market». FACE → «a gluten-free certification body (e.g., GFCO in the US, Coeliac UK)».
  - Temperaturas «°F (°C)»; pesos «grams or ounces» solo donde el ES pide gramajes.
  - Vocabulario: carta → menu · escandallo → recipe costing/cost card · mermas → waste/yield loss · obrador → production
    kitchen (pastry/bakery) · dark kitchen → ghost kitchen · comensal → guest · pax → covers/servings · sala → front of
    house · menú del día → daily set menu · ticket medio → average check · cocina de autor → signature cuisine.
  - Ejemplos culturales internacionales (sherry, tapas, cocina mediterránea, japonesa…) se quedan; lo que solo existe en
    España se cambia por un equivalente neutro.
- Portada EN: «300 Prompts · 3 Blocks · 33 Sections · 70+ AI Agents» (el ES dice «20 Categorías · 55+ Apps»; en EN se cuenta
  lo que hay: 33 secciones y 72 agentes en la plataforma EN sin contar los modelos generales).

## 4. Pipeline F2 (Mac: todo es ligero — 1 s de CPU por fichero)

1. `extraer_es.py` → `es.json`.
2. 4 redactores Sonnet (prompts 1-75 + portada/bienvenida/bloques/cierre · 76-150 · 151-225 · 226-300) → `en/parte-N.json`;
   1 Sonnet para el dashboard → `src/data/prompts-en.ts`; 1 Sonnet para los bonos → `en/bonus-textos.json` (mapa ES→EN). De 2 en 2.
3. `gate_en.py`: 300 prompts y 33 secciones, mismos placeholders por prompt, agentes ∈ `agentes_en.json`, cero `€`/euros, cero
   no latinos, cero años pasados, lista de palabras-centinela del español, ninguna cadena idéntica al ES de más de 4 palabras.
4. `maquetar_en.py` (reportlab, fuentes Arial del sistema = las del PDF ES): mismas medidas (Letter, márgenes 72 pt), colores por
   bloque (#1d3a5e · #2d794e · #c65c1a), oro #f5c741 en los números, separadores #eeeeee, cada sección en página nueva.
5. `aplicar_bonus.py`: traduce en sitio el .docx (python-docx) y el .xlsx (openpyxl), conservando estilos y combinaciones.
6. Ficheros publicados en `astro-site/public/dl/ai-prompts-for-restaurants/`.

## 5. F3

Calco de `feb27f88` (F3 del Restaurant Inventory Kit Pro): familia `pro-prompts-ebook → en: ai-prompts-for-restaurants` viva en
`tienda.ts`, `zona-app.ts`, 4 functions con `lang: 'en'`, `admin-generate-access`, `payment-links.ts`/`product-prices.ts` ($14),
config + changelog, hreflang recíproco en `/pro-prompts-ebook` (el resto del HTML ES byte a byte), tarjeta viva en el hub EN
(la más nueva en 1, «New»), catálogo `urlByLang`, banners del blog EN que hoy apunten al eBook ES, `VITE_STRIPE_PAYMENT_LINK_AI_PROMPTS_FOR_RESTAURANTS`.
Mockup EN de la portada (skill `generate-images`, editando el del ES: «Restaurants & Hospitality · 300+ Professional Prompts»).
Gates: `tienda-gate`, `robots-gate`, `whatsapp-gate`, `miselup-gate`, `gate-flujo-postpago --only ai-prompts-for-restaurants`
contra el preview y LIVE. UNA revisión Opus final (landing + PDF + bonos + dashboard).

## 6. Fuera de alcance

Rehacer o ampliar prompts; reseñas; Mega Pack; tocar el producto ES (salvo el hreflang).
