# Gate de páginas anunciadas vs páginas reales — 2026-09-10

Generado por `scripts/productos-digitales/paginas-gate.py`. Ata cada cifra de páginas que
anuncia la landing (`astro-site/src/data/productos/**/*.ts`) con las páginas reales del
entregable en `astro-site/public/dl/<slug>/`. Motivo: hallazgo C1 de la refutación del
research de la Guía de Pastelería (`guia-pasteleria-research-REFUTACION-2026-09-09.md`).

## Resumen

- Productos escaneados: **45**
- Productos que anuncian páginas: **11**
- Menciones de página evaluadas: **42**
- OK (cabe en lo real): **13**
- FALLA (anunciado > real): **29**
- SIN EMPAREJAR (no se pudo verificar): **0**
- Exceso total sumado en las FALLA: **1677.1 páginas**
- Peor caso: `guia-restaurante-gastronomico` anuncia 119 y el entregable tiene 10 (exceso 109)

## Fallan (anunciado > real)

| slug | fichero:línea | campo | anunciado | pdf/docx emparejado | páginas reales | exceso |
|---|---|---|---|---|---|---|
| guia-restaurante-gastronomico | `astro-site/src/data/productos/guias/guia-restaurante-gastronomico.ts:13` | seo.description | 119 | guia-restaurante-gastronomico.pdf | 10 | 109 |
| guia-restaurante-gastronomico | `astro-site/src/data/productos/guias/guia-restaurante-gastronomico.ts:23` | hero.description | 119 | guia-restaurante-gastronomico.pdf | 10 | 109 |
| guia-restaurante-gastronomico | `astro-site/src/data/productos/guias/guia-restaurante-gastronomico.ts:25` | hero.checkItems | 119 | guia-restaurante-gastronomico.pdf | 10 | 109 |
| guia-restaurante-gastronomico | `astro-site/src/data/productos/guias/guia-restaurante-gastronomico.ts:151` | cta.items | 119 | guia-restaurante-gastronomico.pdf | 10 | 109 |
| guia-panaderia-obrador | `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:20` | seo.description | 70 | guia-panaderia-obrador.pdf (estimado desde guia-panaderia-obrador.docx: 8.9p vs PDF 1p) | 8.9 | 61.1 |
| guia-panaderia-obrador | `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:30` | hero.description | 70 | guia-panaderia-obrador.pdf (estimado desde guia-panaderia-obrador.docx: 8.9p vs PDF 1p) | 8.9 | 61.1 |
| guia-panaderia-obrador | `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:32` | hero.checkItems | 70 | guia-panaderia-obrador.pdf (estimado desde guia-panaderia-obrador.docx: 8.9p vs PDF 1p) | 8.9 | 61.1 |
| guia-panaderia-obrador | `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:158` | cta.items | 70 | guia-panaderia-obrador.pdf (estimado desde guia-panaderia-obrador.docx: 8.9p vs PDF 1p) | 8.9 | 61.1 |
| guia-restaurante-casual | `astro-site/src/data/productos/guias/guia-restaurante-casual.ts:15` | seo.description | 60 | guia-restaurante-casual.pdf (estimado desde guia-restaurante-casual.docx: 5.5p vs PDF 1p) | 5.5 | 54.5 |
| guia-restaurante-casual | `astro-site/src/data/productos/guias/guia-restaurante-casual.ts:25` | hero.description | 60 | guia-restaurante-casual.pdf (estimado desde guia-restaurante-casual.docx: 5.5p vs PDF 1p) | 5.5 | 54.5 |
| guia-restaurante-casual | `astro-site/src/data/productos/guias/guia-restaurante-casual.ts:27` | hero.checkItems | 60 | guia-restaurante-casual.pdf (estimado desde guia-restaurante-casual.docx: 5.5p vs PDF 1p) | 5.5 | 54.5 |
| guia-restaurante-casual | `astro-site/src/data/productos/guias/guia-restaurante-casual.ts:151` | cta.items | 60 | guia-restaurante-casual.pdf (estimado desde guia-restaurante-casual.docx: 5.5p vs PDF 1p) | 5.5 | 54.5 |
| guia-restaurante-mexicano | `astro-site/src/data/productos/guias/guia-restaurante-mexicano.ts:16` | seo.description | 60 | guia-restaurante-mexicano.pdf (estimado desde guia-restaurante-mexicano.docx: 7.9p vs PDF 1p) | 7.9 | 52.1 |
| guia-restaurante-mexicano | `astro-site/src/data/productos/guias/guia-restaurante-mexicano.ts:26` | hero.description | 60 | guia-restaurante-mexicano.pdf (estimado desde guia-restaurante-mexicano.docx: 7.9p vs PDF 1p) | 7.9 | 52.1 |
| guia-restaurante-mexicano | `astro-site/src/data/productos/guias/guia-restaurante-mexicano.ts:28` | hero.checkItems | 60 | guia-restaurante-mexicano.pdf (estimado desde guia-restaurante-mexicano.docx: 7.9p vs PDF 1p) | 7.9 | 52.1 |
| guia-restaurante-mexicano | `astro-site/src/data/productos/guias/guia-restaurante-mexicano.ts:152` | cta.items | 60 | guia-restaurante-mexicano.pdf (estimado desde guia-restaurante-mexicano.docx: 7.9p vs PDF 1p) | 7.9 | 52.1 |
| guia-restaurante-peruano | `astro-site/src/data/productos/guias/guia-restaurante-peruano.ts:16` | seo.description | 60 | guia-restaurante-peruano.pdf (estimado desde guia-restaurante-peruano.docx: 9.0p vs PDF 1p) | 9.0 | 51.0 |
| guia-restaurante-peruano | `astro-site/src/data/productos/guias/guia-restaurante-peruano.ts:26` | hero.description | 60 | guia-restaurante-peruano.pdf (estimado desde guia-restaurante-peruano.docx: 9.0p vs PDF 1p) | 9.0 | 51.0 |
| guia-restaurante-peruano | `astro-site/src/data/productos/guias/guia-restaurante-peruano.ts:28` | hero.checkItems | 60 | guia-restaurante-peruano.pdf (estimado desde guia-restaurante-peruano.docx: 9.0p vs PDF 1p) | 9.0 | 51.0 |
| guia-restaurante-peruano | `astro-site/src/data/productos/guias/guia-restaurante-peruano.ts:152` | cta.items | 60 | guia-restaurante-peruano.pdf (estimado desde guia-restaurante-peruano.docx: 9.0p vs PDF 1p) | 9.0 | 51.0 |
| guia-restaurante-japones | `astro-site/src/data/productos/guias/guia-restaurante-japones.ts:15` | seo.description | 60 | guia-restaurante-japones.pdf (estimado desde guia-restaurante-japones.docx: 11.0p vs PDF 1p) | 11.0 | 49.0 |
| guia-restaurante-japones | `astro-site/src/data/productos/guias/guia-restaurante-japones.ts:25` | hero.description | 60 | guia-restaurante-japones.pdf (estimado desde guia-restaurante-japones.docx: 11.0p vs PDF 1p) | 11.0 | 49.0 |
| guia-restaurante-japones | `astro-site/src/data/productos/guias/guia-restaurante-japones.ts:27` | hero.checkItems | 60 | guia-restaurante-japones.pdf (estimado desde guia-restaurante-japones.docx: 11.0p vs PDF 1p) | 11.0 | 49.0 |
| guia-restaurante-japones | `astro-site/src/data/productos/guias/guia-restaurante-japones.ts:152` | cta.items | 60 | guia-restaurante-japones.pdf (estimado desde guia-restaurante-japones.docx: 11.0p vs PDF 1p) | 11.0 | 49.0 |
| guia-restaurante-nikkei | `astro-site/src/data/productos/guias/guia-restaurante-nikkei.ts:26` | hero.description | 60 | guia-restaurante-nikkei.pdf (estimado desde guia-restaurante-nikkei.docx: 11.9p vs PDF 1p) | 11.9 | 48.1 |
| guia-restaurante-nikkei | `astro-site/src/data/productos/guias/guia-restaurante-nikkei.ts:28` | hero.checkItems | 60 | guia-restaurante-nikkei.pdf (estimado desde guia-restaurante-nikkei.docx: 11.9p vs PDF 1p) | 11.9 | 48.1 |
| guia-restaurante-nikkei | `astro-site/src/data/productos/guias/guia-restaurante-nikkei.ts:152` | cta.items | 60 | guia-restaurante-nikkei.pdf (estimado desde guia-restaurante-nikkei.docx: 11.9p vs PDF 1p) | 11.9 | 48.1 |
| guia-dark-kitchen | `astro-site/src/data/productos/guias/guia-dark-kitchen.ts:34` | hero.checkItems | 40 | guia-como-montar-dark-kitchen.pdf | 27 | 13 |
| guia-dark-kitchen | `astro-site/src/data/productos/guias/guia-dark-kitchen.ts:147` | cta.items | 40 | guia-como-montar-dark-kitchen.pdf | 27 | 13 |

## Tabla completa

| slug | línea | fichero:línea | campo | texto | anunciado | pdf/docx emparejado | páginas reales | veredicto |
|---|---|---|---|---|---|---|---|---|
| guia-dark-kitchen | guias | `astro-site/src/data/productos/guias/guia-dark-kitchen.ts:34` | hero.checkItems | 'Guía completa PDF + DOCX editable (12 capítulos, +40 páginas)', | 40 | guia-como-montar-dark-kitchen.pdf | 27 | FALLA |
| guia-dark-kitchen | guias | `astro-site/src/data/productos/guias/guia-dark-kitchen.ts:147` | cta.items | 'Guía completa PDF (12 capítulos, +40 páginas)', | 40 | guia-como-montar-dark-kitchen.pdf | 27 | FALLA |
| guia-food-cost-ingenieria-menu | guias | `astro-site/src/data/productos/guias/guia-food-cost-ingenieria-menu.ts:26` | seo.description | description: 'Escandallo (costeo de recetas), precios y rentabilidad de tu carta: guía de 95 páginas, 8 Excel con fórmulas y 12 ejercicios resueltos.  | 95 | guia-food-cost-ingenieria-menu.pdf (estimado desde guia-food-cost-ingenieria-menu.docx: 112.6p vs PDF 95p) | 112.6 | OK |
| guia-food-cost-ingenieria-menu | guias | `astro-site/src/data/productos/guias/guia-food-cost-ingenieria-menu.ts:40` | hero.checkItems | 'Guía completa PDF + DOCX editable (20 capítulos, 95 páginas)', | 95 | guia-food-cost-ingenieria-menu.pdf (estimado desde guia-food-cost-ingenieria-menu.docx: 112.6p vs PDF 95p) | 112.6 | OK |
| guia-food-cost-ingenieria-menu | guias | `astro-site/src/data/productos/guias/guia-food-cost-ingenieria-menu.ts:44` | hero.checkItems | 'Bonus: 12 ejercicios resueltos paso a paso (32 páginas)', | 32 | BONUS-ejercicios-resueltos.pdf (estimado desde BONUS-ejercicios-resueltos.docx: 32.9p vs PDF 32p) | 32.9 | OK |
| guia-food-cost-ingenieria-menu | guias | `astro-site/src/data/productos/guias/guia-food-cost-ingenieria-menu.ts:164` | cta.items | 'Guía completa PDF + DOCX (20 capítulos, 95 páginas)', | 95 | guia-food-cost-ingenieria-menu.pdf (estimado desde guia-food-cost-ingenieria-menu.docx: 112.6p vs PDF 95p) | 112.6 | OK |
| guia-food-cost-ingenieria-menu | guias | `astro-site/src/data/productos/guias/guia-food-cost-ingenieria-menu.ts:169` | cta.items | 'Bonus: 12 ejercicios resueltos (32 páginas)', | 32 | BONUS-ejercicios-resueltos.pdf (estimado desde BONUS-ejercicios-resueltos.docx: 32.9p vs PDF 32p) | 32.9 | OK |
| guia-panaderia-obrador | guias | `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:20` | seo.description | description: 'Guía premium para montar una panadería con obrador en España 2026: 20 capítulos, 70+ páginas, plan financiero, recetario masa madre, sal | 70 | guia-panaderia-obrador.pdf (estimado desde guia-panaderia-obrador.docx: 8.9p vs PDF 1p) | 8.9 | FALLA |
| guia-panaderia-obrador | guias | `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:30` | hero.description | description: 'Guía completa con 20 capítulos, 70+ páginas, 9 plantillas Excel, 6 checklists, business plan modelo y manual del obrador. Todo para abri | 70 | guia-panaderia-obrador.pdf (estimado desde guia-panaderia-obrador.docx: 8.9p vs PDF 1p) | 8.9 | FALLA |
| guia-panaderia-obrador | guias | `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:32` | hero.checkItems | 'Guía completa PDF + DOCX editable (20 capítulos, 70+ páginas)', | 70 | guia-panaderia-obrador.pdf (estimado desde guia-panaderia-obrador.docx: 8.9p vs PDF 1p) | 8.9 | FALLA |
| guia-panaderia-obrador | guias | `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:158` | cta.items | 'Guía completa PDF + DOCX (20 capítulos, 70+ páginas)', | 70 | guia-panaderia-obrador.pdf (estimado desde guia-panaderia-obrador.docx: 8.9p vs PDF 1p) | 8.9 | FALLA |
| guia-restaurante-casual | guias | `astro-site/src/data/productos/guias/guia-restaurante-casual.ts:15` | seo.description | description: 'Guía premium para montar un restaurante casual en España: 20 capítulos, 60+ páginas, plan financiero, diseño de cocina y sala, delivery, | 60 | guia-restaurante-casual.pdf (estimado desde guia-restaurante-casual.docx: 5.5p vs PDF 1p) | 5.5 | FALLA |
| guia-restaurante-casual | guias | `astro-site/src/data/productos/guias/guia-restaurante-casual.ts:25` | hero.description | description: 'Guía completa con 20 capítulos, 60+ páginas, 8 plantillas Excel, 6 checklists, business plan modelo y manual de operaciones. Todo para a | 60 | guia-restaurante-casual.pdf (estimado desde guia-restaurante-casual.docx: 5.5p vs PDF 1p) | 5.5 | FALLA |
| guia-restaurante-casual | guias | `astro-site/src/data/productos/guias/guia-restaurante-casual.ts:27` | hero.checkItems | 'Guía completa PDF + DOCX editable (20 capítulos, 60+ páginas)', | 60 | guia-restaurante-casual.pdf (estimado desde guia-restaurante-casual.docx: 5.5p vs PDF 1p) | 5.5 | FALLA |
| guia-restaurante-casual | guias | `astro-site/src/data/productos/guias/guia-restaurante-casual.ts:151` | cta.items | 'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)', | 60 | guia-restaurante-casual.pdf (estimado desde guia-restaurante-casual.docx: 5.5p vs PDF 1p) | 5.5 | FALLA |
| guia-restaurante-gastronomico | guias | `astro-site/src/data/productos/guias/guia-restaurante-gastronomico.ts:13` | seo.description | description: 'Guía premium para montar un restaurante gastronómico en España: 22 capítulos, 119 páginas, plan financiero, diseño de cocina y sala, bri | 119 | guia-restaurante-gastronomico.pdf | 10 | FALLA |
| guia-restaurante-gastronomico | guias | `astro-site/src/data/productos/guias/guia-restaurante-gastronomico.ts:23` | hero.description | description: 'Guía completa con 22 capítulos, 119 páginas, 10 plantillas Excel, 8 checklists, business plan modelo y manual de servicio. Todo para abr | 119 | guia-restaurante-gastronomico.pdf | 10 | FALLA |
| guia-restaurante-gastronomico | guias | `astro-site/src/data/productos/guias/guia-restaurante-gastronomico.ts:25` | hero.checkItems | 'Guía completa PDF + DOCX editable (22 capítulos, 119 páginas)', | 119 | guia-restaurante-gastronomico.pdf | 10 | FALLA |
| guia-restaurante-gastronomico | guias | `astro-site/src/data/productos/guias/guia-restaurante-gastronomico.ts:151` | cta.items | 'Guía completa PDF + DOCX (22 capítulos, 119 páginas)', | 119 | guia-restaurante-gastronomico.pdf | 10 | FALLA |
| guia-restaurante-japones | guias | `astro-site/src/data/productos/guias/guia-restaurante-japones.ts:15` | seo.description | description: 'Guía premium para montar un restaurante japonés en España: 20 capítulos, 60+ páginas, sushi-ya, ramen-ya, izakaya, omakase, robatayaki,  | 60 | guia-restaurante-japones.pdf (estimado desde guia-restaurante-japones.docx: 11.0p vs PDF 1p) | 11.0 | FALLA |
| guia-restaurante-japones | guias | `astro-site/src/data/productos/guias/guia-restaurante-japones.ts:25` | hero.description | description: 'Guía completa con 20 capítulos, 60+ páginas, 8 plantillas Excel, 6 checklists, business plan modelo y manual de operaciones. Todo para a | 60 | guia-restaurante-japones.pdf (estimado desde guia-restaurante-japones.docx: 11.0p vs PDF 1p) | 11.0 | FALLA |
| guia-restaurante-japones | guias | `astro-site/src/data/productos/guias/guia-restaurante-japones.ts:27` | hero.checkItems | 'Guía completa PDF + DOCX editable (20 capítulos, 60+ páginas)', | 60 | guia-restaurante-japones.pdf (estimado desde guia-restaurante-japones.docx: 11.0p vs PDF 1p) | 11.0 | FALLA |
| guia-restaurante-japones | guias | `astro-site/src/data/productos/guias/guia-restaurante-japones.ts:152` | cta.items | 'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)', | 60 | guia-restaurante-japones.pdf (estimado desde guia-restaurante-japones.docx: 11.0p vs PDF 1p) | 11.0 | FALLA |
| guia-restaurante-mexicano | guias | `astro-site/src/data/productos/guias/guia-restaurante-mexicano.ts:16` | seo.description | description: 'Guía premium para montar un restaurante mexicano en España: 20 capítulos, 60+ páginas, proveedores de productos mexicanos, barra de tequ | 60 | guia-restaurante-mexicano.pdf (estimado desde guia-restaurante-mexicano.docx: 7.9p vs PDF 1p) | 7.9 | FALLA |
| guia-restaurante-mexicano | guias | `astro-site/src/data/productos/guias/guia-restaurante-mexicano.ts:26` | hero.description | description: 'Guía completa con 20 capítulos, 60+ páginas, 8 plantillas Excel, 6 checklists, business plan modelo y manual de operaciones. Todo para a | 60 | guia-restaurante-mexicano.pdf (estimado desde guia-restaurante-mexicano.docx: 7.9p vs PDF 1p) | 7.9 | FALLA |
| guia-restaurante-mexicano | guias | `astro-site/src/data/productos/guias/guia-restaurante-mexicano.ts:28` | hero.checkItems | 'Guía completa PDF + DOCX editable (20 capítulos, 60+ páginas)', | 60 | guia-restaurante-mexicano.pdf (estimado desde guia-restaurante-mexicano.docx: 7.9p vs PDF 1p) | 7.9 | FALLA |
| guia-restaurante-mexicano | guias | `astro-site/src/data/productos/guias/guia-restaurante-mexicano.ts:152` | cta.items | 'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)', | 60 | guia-restaurante-mexicano.pdf (estimado desde guia-restaurante-mexicano.docx: 7.9p vs PDF 1p) | 7.9 | FALLA |
| guia-restaurante-nikkei | guias | `astro-site/src/data/productos/guias/guia-restaurante-nikkei.ts:26` | hero.description | description: 'Guía completa con 20 capítulos, 60+ páginas, 9 plantillas Excel, 6 checklists, business plan modelo y manual de operaciones. Todo para a | 60 | guia-restaurante-nikkei.pdf (estimado desde guia-restaurante-nikkei.docx: 11.9p vs PDF 1p) | 11.9 | FALLA |
| guia-restaurante-nikkei | guias | `astro-site/src/data/productos/guias/guia-restaurante-nikkei.ts:28` | hero.checkItems | 'Guía completa PDF + DOCX editable (20 capítulos, 60+ páginas)', | 60 | guia-restaurante-nikkei.pdf (estimado desde guia-restaurante-nikkei.docx: 11.9p vs PDF 1p) | 11.9 | FALLA |
| guia-restaurante-nikkei | guias | `astro-site/src/data/productos/guias/guia-restaurante-nikkei.ts:152` | cta.items | 'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)', | 60 | guia-restaurante-nikkei.pdf (estimado desde guia-restaurante-nikkei.docx: 11.9p vs PDF 1p) | 11.9 | FALLA |
| guia-restaurante-peruano | guias | `astro-site/src/data/productos/guias/guia-restaurante-peruano.ts:16` | seo.description | description: 'Guía premium para montar un restaurante peruano en España: 20 capítulos, 60+ páginas, cevichería, Nikkei, barra de piscos, proveedores p | 60 | guia-restaurante-peruano.pdf (estimado desde guia-restaurante-peruano.docx: 9.0p vs PDF 1p) | 9.0 | FALLA |
| guia-restaurante-peruano | guias | `astro-site/src/data/productos/guias/guia-restaurante-peruano.ts:26` | hero.description | description: 'Guía completa con 20 capítulos, 60+ páginas, 8 plantillas Excel, 6 checklists, business plan modelo y manual de operaciones. Todo para a | 60 | guia-restaurante-peruano.pdf (estimado desde guia-restaurante-peruano.docx: 9.0p vs PDF 1p) | 9.0 | FALLA |
| guia-restaurante-peruano | guias | `astro-site/src/data/productos/guias/guia-restaurante-peruano.ts:28` | hero.checkItems | 'Guía completa PDF + DOCX editable (20 capítulos, 60+ páginas)', | 60 | guia-restaurante-peruano.pdf (estimado desde guia-restaurante-peruano.docx: 9.0p vs PDF 1p) | 9.0 | FALLA |
| guia-restaurante-peruano | guias | `astro-site/src/data/productos/guias/guia-restaurante-peruano.ts:152` | cta.items | 'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)', | 60 | guia-restaurante-peruano.pdf (estimado desde guia-restaurante-peruano.docx: 9.0p vs PDF 1p) | 9.0 | FALLA |
| manual-chef-ejecutivo | manuales | `astro-site/src/data/productos/manuales/manual-chef-ejecutivo.ts:60` | hero.checkItems | 'Manual completo PDF + DOCX editable (20 capítulos, 96 páginas)', | 96 | manual-chef-ejecutivo.pdf (estimado desde manual-chef-ejecutivo.docx: 109.5p vs PDF 96p) | 109.5 | OK |
| manual-chef-ejecutivo | manuales | `astro-site/src/data/productos/manuales/manual-chef-ejecutivo.ts:64` | hero.checkItems | 'Bonus: 12 situaciones resueltas en cocina (34 páginas)', | 34 | BONUS-12-situaciones-resueltas-cocina.pdf | 34 | OK |
| manual-chef-ejecutivo | manuales | `astro-site/src/data/productos/manuales/manual-chef-ejecutivo.ts:185` | cta.items | 'Manual completo PDF + DOCX (20 capítulos, 96 páginas)', | 96 | manual-chef-ejecutivo.pdf (estimado desde manual-chef-ejecutivo.docx: 109.5p vs PDF 96p) | 109.5 | OK |
| manual-chef-ejecutivo | manuales | `astro-site/src/data/productos/manuales/manual-chef-ejecutivo.ts:190` | cta.items | 'Bonus: 12 situaciones resueltas en cocina (34 páginas)', | 34 | BONUS-12-situaciones-resueltas-cocina.pdf | 34 | OK |
| manual-manager-restaurante | manuales | `astro-site/src/data/productos/manuales/manual-manager-restaurante.ts:51` | hero.checkItems | 'Manual completo PDF + DOCX editable (20 capítulos, 77 páginas)', | 77 | manual-manager-restaurante.pdf (estimado desde manual-manager-restaurante.docx: 84.6p vs PDF 77p) | 84.6 | OK |
| manual-manager-restaurante | manuales | `astro-site/src/data/productos/manuales/manual-manager-restaurante.ts:55` | hero.checkItems | 'Bonus: 12 situaciones resueltas (28 páginas)', | 28 | BONUS-12-situaciones-resueltas.pdf | 28 | OK |
| manual-manager-restaurante | manuales | `astro-site/src/data/productos/manuales/manual-manager-restaurante.ts:176` | cta.items | 'Manual completo PDF + DOCX (20 capítulos, 77 páginas)', | 77 | manual-manager-restaurante.pdf (estimado desde manual-manager-restaurante.docx: 84.6p vs PDF 77p) | 84.6 | OK |
| manual-manager-restaurante | manuales | `astro-site/src/data/productos/manuales/manual-manager-restaurante.ts:181` | cta.items | 'Bonus: 12 situaciones resueltas (28 páginas)', | 28 | BONUS-12-situaciones-resueltas.pdf | 28 | OK |

## Limitaciones conocidas

- El emparejamiento "principal vs bonus" es heurístico (difflib contra el slug / solape de
  palabras contra el nombre de fichero BONUS-*). Revisar la columna `match_score` en el JSON
  cuando el veredicto sorprenda.
- La estimación desde DOCX usa 530 palabras/página, una convergencia razonable
  pero no exacta: sirve para no dar una FALLA falsa por culpa de un PDF-portada de 1 página,
  no como cifra de marketing.
- Sólo entiende los patrones "N páginas", "N+ páginas", "+N páginas" y "N págs[.]". Una cifra
  de páginas escrita en palabras ("ciento diecinueve páginas") no se detecta.

Via: Claude Code
