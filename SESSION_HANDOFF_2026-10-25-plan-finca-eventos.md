# SESSION HANDOFF — 25-oct-2026 · Plan de Negocio: Finca de Eventos y Bodas (ES, 45 €) (sesión Claude Code, Mac + VPS)

## 0. Estado en una línea
**Producto nº 53 LISTO a falta del Payment Link de John** (PR #164, draft, rama `feat/plan-negocio-finca-eventos`).
John (25-oct): «Finca de Eventos y Bodas como siguiente producto nuevo. Adelante». Hecho el mismo día, en ≈ 4 h y ≈ 3,1 M tokens
de subagentes (techo M: 5 M).

## 1. Decisiones (detalle en `scripts/productos-digitales/plan-finca-eventos/SPEC.md`)
- **Modelo (D2)**: finca ARRENDADA con edificaciones existentes + **catering exclusivo concesionado que paga canon**. La finca
  factura espacio y servicios al 21 %; el catering, menú y barra al 10 % directamente al cliente. Se descartó el banquete propio
  del camino (duplicaba capital y canibalizaba el plan de catering); va en el Word como alternativa, igual que «solo alquiler».
- **Caso**: 120 eventos × 82 invitados × 37 € → ventas 364.080 / 393.206 / 412.867 €; neto 8,8 / 11,9 / 12,2 %; inversión
  ≈ 241.000 €; necesidad 360.503 €; 100.000 € propios + préstamo 263.000 € al 6,5 % a 8 años (1 de carencia); DSCR mín. 1,68;
  saldo mínimo 51.025 € en abril; equilibrio de caja 98 eventos el año 1 y 113-116 desde el 2.º. Mes 1 = marzo.
- **Regla de la licencia (M3)**: ninguna fecha en firme sin licencia; antes, solo reservas condicionadas con devolución íntegra
  (cláusula «Segunda bis» del contrato). Así se explica que el año 1 cuente 120 eventos.
- Legal verificado en origen: urbanismo de Madrid, Andalucía, Cataluña y C. Valenciana; **Directriz Básica de Autoprotección,
  Orden INT/1068/2026 (BOE 10-10-2026)**, que deja sin aplicación el RD 393/2007 (no se cita en ningún entregable).

## 2. Entregables (`astro-site/public/dl/plan-negocio-finca-eventos-bodas/`)
plan financiero xlsx (9 hojas) · plan de negocio docx (10 secciones, 6.906 palabras) · checklist xlsx (84 tareas en 6 fases) ·
calculadora de presupuesto del espacio xlsx (autotest 588) · modelos de contrato docx (reserva + anexo empresa + catering
exclusivo, 150 párrafos) · guía de equivalencias docx (58 términos). 7 imágenes `plan-finca-*.jpg`.

## 3. Calidad
- Gates: `ciclo.sh` TODO VERDE (13/13, 30/30) · D9 8/8 · barrido (solo 3 coincidencias legítimas del contrato) · restos de moldes 0 ·
  no latinos 0 · censo de entregables 0 defectos · `paginas-gate` sin menciones · build local en el VPS exit 0.
- **Una** revisión opus final: 0 B · 9 M · 26 m → 9 M y 24 m aplicados en una ronda (`REVISION-FINAL.md`, `F2-NOTAS.md` §8).
- Preview: `gate-flujo-postpago --only` solo falla por el Payment Link (#comprar, env, `payment-links.ts`); Miselup 106/106.
- Gotcha cazado: el agente de registros insertó la entrada del changelog DENTRO de la de la heladería → el build de Netlify
  falló («Expected ] but found :»). Netlify no da el log de un deploy preview por la CLI (404): se reprodujo el build en el VPS
  (`ln -s` de `node_modules` del repo principal + `npm run build`) y se comprobaron con `esbuild` los 18 `.ts/.tsx` del diff.

## 4. Para cerrar (cuando John cree el link)
1. Ficha en `PAYMENT_LINKS_PENDIENTES_JOHN.md` (45 EUR, *exclusive*, impuesto automático, factura, redirección a
   `/plan-negocio-finca-eventos-bodas-access?session_id={CHECKOUT_SESSION_ID}`).
2. `stripe get /v1/payment_links/<plink> --live` + `line_items` → env `VITE_STRIPE_PAYMENT_LINK_PLAN_FINCA_EVENTOS` (builds, all) →
   `sync-payment-links.py` → commit → PR fuera de draft → merge.
3. Gates LIVE: `gate-flujo-postpago --only plan-negocio-finca-eventos-bodas` · `tienda-gate --base https://aichef.pro` (añadir el
   slug a `PLANES_ES`) · `robots-gate --live` · `miselup-gate` · `fase6-gate.py https://aichef.pro` (URL BASE) · curl al checkout
   cripto (`qa-finca@aichef.pro`) · sitemap a GSC.
4. Correo ES: hueco **3-dic 08:00Z** → borrador con `resend-broadcast.py --borrador` tras el LIVE + prueba a John + routine que lo
   programe el 3-nov o después.
5. Pasar al carril Cursor `plan-finca-eventos/NOTA-CARRIL-CURSOR.md`.

## 5. Deuda que queda (no bloquea)
- Motor común: `PyG!G14` (10 % fijo) y `Personal!C11` (suma sin ponderar) — afectan a todos los planes; arreglar en el motor.
- La guía de equivalencias sale en Letter en los 53 productos (generador común).
- Gemelo EN («Wedding & Event Venue Business Plan»): demanda real 300-800/mes en EE. UU.; se decide después.
