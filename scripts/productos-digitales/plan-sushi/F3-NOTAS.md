# Plan de Negocio: Sushi Bar ES 1.0 — F3 (producto y lanzamiento)

> Sesión Claude Code, 31-oct-2026 (F3 nocturna, decisiones delegadas). Patrón = la F3 de la Pollería (`6fb676c2`), fichero a
> fichero. Mac: ficha, páginas, dashboard, imágenes, correo, commits. VPS (`/root/wt-sushi`): censo y guía de equivalencias, volcados
> de los entregables con openpyxl/python-docx y `gate-no-latinos`. Sin build local (Mac < 50 °C toda la fase).

## 1. Qué se hizo

- **Ficha** `astro-site/src/data/productos/planes/plan-negocio-sushi-bar.ts` (C de la Pollería) + páginas landing/access/library, isla,
  `PlanNegocioSushiBar{Dashboard,AccessGate}.tsx` (5 tarjetas, clave `calculadora-sushi`).
- **Registros** (sonnet, revisado): functions ×4 (verify-purchase y resend-access con la venta cruzada al Kit de Tareas Sushi Bar, como
  la Taquería), config, catálogo, changelog 1.0, `AdminGenerateAccess`, `zona-app`, `tienda.ts` (EN `sushi-restaurant-business-plan`,
  `vivo: false`), `product-prices.ts` (sync, +1 línea), hubs ×7 + SPA en posición 1 (la Finca pierde el ✨; en EN no se degrada nada),
  buscador, `sitemap-lastmod`, `llms.txt` 57 → 58, `llms-full.txt`, `tienda-gate.py` (`PLANES_ES`).
- **Enlaces entrantes**: Guía Restaurante Japonés (fuera «abrir sushi bar» de `seo.keywords` + footer al plan), Kit de Tareas Sushi Bar
  (footer), Pollería (footer), use cases `sushi-bar` y `restaurante-japones` (`productIds`, el plan tras la guía; se cae
  `pro-prompts-ebook` para dejar la rejilla en 6).
- **Imágenes** `ai-gallery/plan-sushi-bar-{hero,barra,pescado,arroz,delivery,equipo,plan}.jpg` (Nano Banana, 1376 × 768, 207-296 KB,
  11 generaciones ≈ 0,74 $): rehechas 3 (pulsera y reloj del itamae manipulando, caras de perfil, «BUSINESS PLAN» en la carpeta).
- **Guía de Equivalencias**: censo 58 productos (589 ficheros, 0 errores) · `build_guia_es.py --only` + `--check`: **PASS** (75 términos,
  ~77 págs., 115 KB) · `integracion.json` con los ejemplos de la FAQ (palta, camarón, mesero/mozo, delivery).
- **Correo** `emails/broadcast-plan-negocio-sushi-bar-lanzamiento-es.html` (asunto en el comentario `ASUNTO`, «Hola, colegas,», #111 +
  #FFD700, venta cruzada al Kit de Tareas). **Sin programar**: hueco ES de la SPEC = 28-dic 08:00Z (lo programa el lead con el link).
- **`PAYMENT_LINKS_PENDIENTES_JOHN.md`**: entrada ⏳ con nombre, 35,00 EUR *exclusive* + impuesto automático, factura, redirección,
  descripción de 249 caracteres (medida con python), env y hero. `#comprar` sin link, como las hermanas.

## 2. Decisiones

1. **Sin testimonios ni rating** (SPEC §5 y molde de la Pollería: producto sin ventas; la clave `testimonials` se omite). No hay avatar,
   género ni nicho que pueda contradecir los ficheros.
2. **10 FAQ** (las 9 de R §6 + la del remolque → Plan Food Truck). La de la franquicia lleva las cifras del Word [46] [63].
3. **Equilibrio en la landing = 65 comensales** (contable, `BE_COMENSALES_DIA`): el 62 de caja es solo del año 1 (carencia del préstamo;
   69 y 71 después) y contarlo sin esa salvedad confunde.
4. Tags de los hubs = los de la tarjeta del Kit de Tareas Sushi Bar (`sushi-bar`, `japones`/`japanese`).
5. Nombre del hub EN provisional «Business Plan: Sushi Bar» → lo sustituye la tarjeta del gemelo EN en su F3.

## 3. Contraste landing ↔ entregables (VPS, 31-oct)

Inversión 103.350 € (18 partidas + imprevistos = `Inversión Inicial`) → «unos 103.400 €» · necesidad 185.404 € → «unos 185.400 €» · local
95 m², 36 plazas (8 barra + 28 mesa), 79 comensales (45 sala), ticket 20,00 €, 300 días, 474.000 € (`0. Supuestos`) · neto 9,1/10,4/9,8 %
→ «9-10 %» · equilibrio 65 · pesimista −3.234 € · plataforma 24 %, comisión 30 % · kilo útil 14,29 / 24,16 €, 2,42 kg de shari, 121
nigiris, 4,9 kg/día, 14 productos, combinado de 24: 22,16 → 16,12 €, ponderado 16,1 % (`Pescado`, `Arroz`, `Escandallo`) · sushiman
1.650 € y titular 2.200 € en 14 pagas (`Personal`) · 12.000-22.000 €, omakase 2.500 €, franquicias 39.950/200.000/300.000 € (Word
[46] [63] [88]) · IAE 671/673/677.9 [102] · anisakis [104] · shari 30.5 y pH 4,6 del Kit [107] · IVA 21 % entero [108] · 9 + 10 + 80
(12/15/14/13/13/13) + 4 hojas. Revisión adversarial final (Opus): ver §5.

## 4. Gates (Mac, ligeros)

esbuild de los .ts/.tsx tocados: OK · `sync-product-prices.py --check`: VERDE (93 productos; 58 del catálogo) · `tienda-gate.py`
(estático): VERDE · `hub-gate.py`: PASS (58, primero el sushi, ✨ en 0-4) · `nombre-gate.py --only`: ✅ · `gate-flujo-postpago.py --offline
--only`: 5 ficheros = 5 tarjetas, 0 issues; único ✗ = «sin Payment Link» (esperado hasta que John lo cree) · `gate-no-latinos --only`
(VPS): 0 · fuentes de la landing, dashboard y correo: 0 no latinos. **Pendiente con preview** (no hay PR): `tienda-gate.py --es-identico
--base`, `gate-flujo-postpago.py --base … --crypto-products all --crypto-exclude pro-prompts-ebook` (3 puertas + `<dialog>`; la plantilla
las monta con `cryptoEnabledFor`, y la nota de devoluciones va con ella), JSON-LD y tarjeta de `/usos/` en el `dist`.

## 5. Revisión adversarial (Opus, una pasada) · 0 B · 2 M · 8 m, todo arreglado (`42b72c12` + entregables)

- **M1** La tarjeta del Kit de Tareas Sushi Bar en los 7 hubs + SPA y dos frases de sus testimonios decían «-20 ºC / 7 días» (la
  opción FDA); sus plantillas (03, VPS) y este plan dicen ≥ 24 h a −20 °C o ≥ 15 h a −35 °C → solo esa frase (regla del 11-oct).
- **M2** CTA «anisakis, shari y licencia antes de firmar el local» → consulta urbanística y anisakis antes de firmar; licencia y shari,
  antes de abrir (= fases del checklist).
- **m** arroz del día con merma (5,2 kg, `Arroz!B44`) · margen para llevar 21,76 € (`Escandallo!O26`) · comisión «del 30 %, editable»
  (no «real»; landing ×2 y correo) · IVA del 21 %: «poco dinero, pero IVA que Hacienda reclama» (1,1 % de las ventas) · anisakis «o menos
  en todo el producto» · «79 comensales EQUIVALENTES» (cada pedido = 1,6; Word [40]) · dashboard «4 Documentos + Bonus» · el pH del shari
  va en la **plantilla 02** del Kit de Tareas (no la 03): `datos_checklist.py` y `calculadora_sus_es.py` → checklist y calculadora
  regenerados en el VPS (`/root/tmp-sus-f3/`): `ciclo.sh` TODO VERDE, `--autotest` 580 VERDE, `cifras --calc` D9 VERDE con tokens
  idénticos (`cmp`), barrido 0, LIT255 VERDE, restos 4 ficheros VERDE; diff celda a celda = solo `F3!E14`, `Arroz!A3` e
  `Instrucciones!A14`. sha256 Mac = VPS: checklist `298a99d1…`, calculadora `9832c00a…` (plan y Word, sin tocar).
- Comprobado sin hallazgo: todas las cifras del caso y de la calculadora, recuentos, legal, arreglos de la F2 no reintroducidos, restos de
  hermanas, saludo y colores del correo, claves de las functions, enlaces.
