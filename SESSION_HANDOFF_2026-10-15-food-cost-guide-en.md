# Handoff — 15-oct-2026 (sesión Claude Code) — Food Cost + Menu Engineering Guide (EN), producto 14 de la tienda EN

## 0. Lo primero al retomar
1. **Falta solo el Payment Link de Stripe (John)**: precio propuesto **$59** (la guía ES está a **55 €**, no a 65).
   Env var `VITE_STRIPE_PAYMENT_LINK_FOOD_COST_MENU_ENGINEERING_GUIDE` (scope builds) + `sync-payment-links.py`.
   Mientras no exista, el CTA cae a `#comprar` y `gate-flujo-postpago` marca 2-3 fallos esperados.
2. Con el link: redeploy del preview → `gate-flujo-postpago.py --base https://deploy-preview-131--aichefpro.netlify.app --only food-cost-menu-engineering-guide --crypto-products all --crypto-exclude pro-prompts-ebook`
   → merge del **PR #131** → el mismo gate LIVE (sin `--base`) → GSC: reenviar sitemap → correo EN.
3. **Correo EN**: hueco **29-nov 14:00Z** (cola EN). Borrador + routine como el Mobile Bar (skill `resend-aichef`); no
   programar antes de que la landing y los /dl respondan 200 en producción.

## 1. Qué se hizo (rama `feat/food-cost-guide-en`, PR #131 en borrador)
| Pieza | Estado |
|---|---|
| Guía EN (20 caps.) | `food-cost-menu-engineering-guide.docx/.pdf` · 95 págs. · 45.265 palabras · docx = md palabra a palabra |
| Bonus EN | `BONUS-solved-exercises.docx/.pdf` · 32 págs. · 12 ejercicios |
| 8 xlsx EN | XML directo (`xlsx/aplicar_en.py`): fórmulas idénticas token a token, valores = ES salvo impuesto (0 % por defecto) y conversiones exactas de unidades; gráfico del prime cost intacto; cache inyectada (3.135 valores) |
| Landing/app | `GuiaLandingPage` con `lang` (**28/29 landings ES byte a byte idénticas** contra el preview; la de Food Cost solo cambia en hreflang), ficha EN, landing/access/library, dashboard EN, registro en 5 fuentes + admin, $59 en `product-prices`, familia en `tienda.ts`, tarjeta viva en el hub EN, enlaces kit ↔ guía, `llms.txt`, 6 banners en el blog EN |

Método (reutilizable para las próximas guías y manuales EN), todo en `scripts/productos-digitales/guia-food-cost-en/`:
`SPEC.md` (D1-D15) · `split_md.py` (trocea los `.md` ensamblados del ES en 14 tandas, ida y vuelta byte a byte) ·
`gate_md_en.py` (estructura, residuo de español, cifras de dinero y %, nombres de ficheros/pestañas; `--autotest`) ·
`ensamblar_md.py` · `render_en.py` (envoltorio de `documentos.maquetar`, pie «Page»; correr en el VPS) ·
`DECISIONES-TANDAS.md` (nombres y cifras fijados tanda a tanda) · `REVISION-FINAL.md` · `ERRATAS-ES.md`.
Traductores: sonnet de 2 en 2 (≈ 100 s por tanda de 5.000 palabras); opus en las 3 tandas fiscales, en los xlsx, en F3
y en la revisión final.

## 2. Pendientes (no bloquean la venta)
- **Erratas de la guía ES** (≈ 20, todas en `ERRATAS-ES.md`): recuentos que contradicen sus tablas, «por debajo/encima»
  invertidos, el ejercicio 8 del bonus sin resolver, la etiqueta del sobrecoste de la lubina… Parche puntual del ES
  (editar `.md`/`txt/` y re-maquetar), sin regenerar capítulos. Proponer a John.
- 4 menores de la revisión: redondeos de 1 céntimo entre texto y xlsx (3,39 vs 3,40…; arreglo propuesto con `ROUND`
  en ES y EN a la vez) y `"Cost Card"!E45` en blanco al 0 % (`=SUM($J$10:$J$29)`).
- Hallazgo lateral: los posts EN `prompt-library-*` tienen «» y palabras en español (los detectó el autotest del gate).
- Las guías ES v1 (Restaurante Casual 2.917 palabras y PDF de relleno, Gastronómico, Panadería, Dark Kitchen) no sirven
  para duplicar al inglés sin subirlas antes a v2: por eso se eligió la Food Cost (v2) en vez de «how to open a restaurant».

## 3. Lecciones
- Traducir el `.md` ENSAMBLADO + envoltorio de render es mucho más barato que tocar el pipeline de bloques.
- El gate de cifras obliga a explicar cada número que desaparece; los traductores cazaron ~20 erratas del ES al cuadrar.
- `DECISIONES-TANDAS.md` compartido evita incoherencias entre tandas paralelas; aun así hubo que unificar un plato
  («Free-range roast chicken») y el índice (título del cap. 6): comprobarlo por script antes de ensamblar.
- `gh pr checks --watch` justo tras un push puede dar por bueno el deploy ANTERIOR: mirar el estado del commit
  (`gh api repos/…/commits/<sha>/status`) antes de pasar gates contra el preview.

Consumo de subagentes ≈ 3,6 M tokens (19 agentes) (L, techo 10 M). CPU del Mac entre 48 y 57 °C toda la sesión (vigilante activo,
tope de 2 agentes, xlsx y render en el VPS).
