# Handoff — 15-oct-2026 (sesión Claude Code) — Food Cost + Menu Engineering Guide (EN), producto 14 de la tienda EN

## 0. Estado final: LIVE (15-oct, merge `71eb5f16` del PR #131) · Tienda EN: 14 productos
- Stripe `plink_1UQo1e4CcdRGidmEGfzJgiN8` (`buy.stripe.com/8x26oA3Kc78ibnpa3r6oo1N`), **$59 USD**, impuesto automático, redirección a
  `/access` comprobada con la CLI (`--live`). El primer link salió en **EUR** (`plink_1UQkH8…`, desactivado): en los paquetes Stripe EN
  avisar de cambiar la moneda. Env `VITE_STRIPE_PAYMENT_LINK_FOOD_COST_MENU_ENGINEERING_GUIDE` (builds, all) + mapa de 65 links.
- Gates LIVE: `gate-flujo-postpago --only` 0 fallos / 0 avisos · completo **65 productos / 904 entregables / 0** · `tienda-gate` · `robots-gate`.
  ES byte a byte 28/29 contra el preview. Sitemap reenviado en GSC.
- **Correo EN 29-nov 14:00Z**: borrador `9848e616-82b2-4530-af65-70593ecc63fd` (prueba a John enviada) + routine
  `trig_01KYPEeGdcVJbsnb8qCXbFrV` (30-oct 15:07Z) → **al retomar después del 30-oct, mirar su `list_runs`**. Siguiente hueco EN: **4-dic 14:00Z**.
- `resend-broadcast.py` gana `--borrador` (crea el draft con las mismas guardas, para huecos a más de 30 días).

## 1. Qué se hizo (PR #131, mergeado)
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
