# Seafood Restaurant Checklists Kit Pro — F2: traducción y montaje (31-oct-2026 · sesión Claude Code)

Todo el python con xlsx en el VPS (`/root/wt-kits`, venv `/root/venv-guias`). Textos: `textos_en/heredado.json` (8) +
`textos_en/G1.json` (213, traducidas en esta sesión, `21c128c3`) + GM 244 por `mapas_seafood.py`. Mes: **October**.
Precio **$15**. Slug en `PRODUCTOS_LETTER` y `EXCLUIDOS`. **Código común: sin tocar** (ganchos del molde plano del food
truck, `f35b7355`).

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 extraer_textos.py --kit seafood && python3 seafood/mapas_seafood.py && python3 heredar.py --kit seafood
    python3 aplicar_en.py --kit seafood --dry-run --salida /tmp/mar-en --idempotencia --mes October
    python3 gates_en.py --kit seafood --dir /tmp/mar-en --mes October [--autotest]
    cp /tmp/mar-en/*.xlsx ../../../astro-site/public/dl/seafood-restaurant-checklist-templates/ && python3 gates_en.py --kit seafood --mes October
    python3 ../censo-entregables.py --only seafood-restaurant-checklist-templates --fail
    python3 ../gate-no-latinos.py --only seafood-restaurant-checklist-templates
    python3 ../parche_xml_xlsx.py --check ../../../astro-site/public/dl/seafood-restaurant-checklist-templates/*.xlsx

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 11 xlsx (SPEC §2), 83.119 bytes; idempotencia 0 diferencias; 0 fórmulas; 0 desbordes; 30 horas a reloj de 12 h |
| Gates | **VERDE 8/0** al primer montaje (dry-run y publicado): G1 11 hojas · 7 DV (147 celdas) · 7 CF · 65 merges · 11 paneles · 11 títulos de impresión · 190 tareas; G2 1.017 piezas contra términos prohibidos; G3 65 altos de fila, 11 títulos interiores; G4 538 glosario · 100 regeneradas · 229 traducidas · 30 horas; **G5 y G6 N/A**; G7 25 °F y 27 citas, todas permitidas, 14 celdas ES con °C |
| Autotest | **16/16 CAZADOS** |
| censo-entregables · no-latinos · LIT255 | 0 defectos (`--fail`) · 11 ficheros, 0 no latinos · VERDE |
| Publicado | `astro-site/public/dl/seafood-restaurant-checklist-templates/` (`cb780fde`); volcados `revision/dump_en.txt` y `dump_es.txt` (978 líneas cada uno) |

## Lo que la F3 tiene que saber (landing, dashboard, email)

- **No prometer** (molde plano): contador de tareas, N/A que no cuenta, hoja de instrucciones, protección (van **sin
  proteger**), hoja de caja ni arqueo, cifras de temperatura del vivero (van «por especie, según proveedor y fabricante»),
  lonja / subasta, temporadas de España, ni que el origen en la carta sea obligatorio.
- Sí: **165 tareas** en 8 checklists con horario de servicio (7:00 AM-11:45 PM) en el 01 + plantilla en blanco + briefing
  de capturas del día + calendario de 12 meses (producto de temporada US orientativo, eventos US, mantenimiento,
  formación); **shellstock tags 90 días** y moluscos de la lista NSSP; recepción en °F (y shellstock según NSSP); raw bar
  sobre hielo escurrido; **parásitos (3-402.11) y aviso al consumidor** para crudo; histamina; 5 CCP de HACCP; alérgenos
  US (pescado y crustáceos; moluscos solo UK); desplegable ✓ / — / N/A en 7 hojas (el 05 y el 09 no lo llevan); US Letter.
- Temporadas: decir «seasonal guide; dates vary by state» (son orientativas).
- `$15`, env `VITE_STRIPE_PAYMENT_LINK_SEAFOOD_RESTAURANT_CHECKLISTS_KIT`, JWT `seafood-restaurant-checklist-templates-jwt`;
  UK solo en la FAQ; enlace cruzado natural con el **HACCP Food Safety Kit Pro** y el **Restaurant Checklists Kit Pro**.

Erratas del ES: `SPEC.md` §5.
