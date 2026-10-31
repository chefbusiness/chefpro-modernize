# Fine Dining Checklists Kit Pro — F2: traducción y montaje (31-oct-2026 · sesión Claude Code)

Todo el python con xlsx en el VPS (`/root/wt-kits`, venv `/root/venv-guias`). Textos: `textos_en/heredado.json` (103:
base 90, hotel 11, chocolatería 2; firma de autor incluida) + `textos_en/G1.json` (681, **un traductor sonnet** en una
pasada, `1f735f1b`; 2 arreglos de G2 míos, `consommé` / `rosé wines`) + GM por `mapas_finedining.py`. Mes: **October**.
Precio **$19** (v2.0). Slug en `PRODUCTOS_LETTER` y `EXCLUIDOS`. **Código común: sin tocar** (los ganchos del hotel sirven:
`N_LIBROS`, caja en el 11, `HOJA_HORAS` / `HOJA_VERDE` en el 10).

## Comandos (en `scripts/productos-digitales/checklists-kit/`)

    python3 extraer_textos.py --kit finedining && python3 finedining/mapas_finedining.py && python3 heredar.py --kit finedining
    python3 aplicar_en.py --kit finedining --dry-run --salida /tmp/fd-en --idempotencia --mes October
    python3 gates_en.py --kit finedining --dir /tmp/fd-en --mes October [--autotest]
    cp /tmp/fd-en/*.xlsx ../../../astro-site/public/dl/fine-dining-checklist-templates/ && python3 gates_en.py --kit finedining --mes October
    python3 ../censo-entregables.py --only fine-dining-checklist-templates --fail
    python3 ../gate-no-latinos.py --only fine-dining-checklist-templates
    python3 ../parche_xml_xlsx.py --check ../../../astro-site/public/dl/fine-dining-checklist-templates/*.xlsx

## Resultados

| Paso | Resultado |
|---|---|
| Montaje | 13 xlsx (SPEC §2), 186.279 bytes; idempotencia 0 diferencias; 159 fórmulas con caché (inject_cache, 0 fallos); 0 desbordes; 29 horas a reloj de 12 h |
| Gates | **VERDE 8/0** (dry-run y publicado): G1 49 hojas · 159 fórmulas (15 por celda: billetes US) · 36 DV (599 celdas) · 36 CF (21 `CF_POR_CELDA`) · 244 merges · 5 protegidas · 811 desbloqueadas · 7 áreas · 40 nombres definidos («Chef's Table» con apóstrofo); G2 2.656 piezas contra términos prohibidos; G3 52 ajustes y 56 altos de fila, 13 versiones; G4 1.045 glosario · 148 regeneradas · 851 traducidas · 22 citas de pestaña · 6 de fichero · firma · 29 horas; **G5** 204.91 · 4,200 · 0 (cierre y registro); G6 159 fórmulas, 68 contadores = ES; G7 32 °F y 41 citas, todas permitidas, 13 celdas ES con °C |
| Autotest | **19/19 CAZADOS** (incluye las dos CF: la excepción revertida y una CF ajena alterada) |
| censo-entregables · no-latinos · LIT255 | 0 defectos (`--fail`) · 13 ficheros, 0 no latinos · VERDE |
| Publicado | `astro-site/public/dl/fine-dining-checklist-templates/` (`35f7c059`); volcados `revision/dump_en.txt` y `dump_es.txt` (3.401 líneas cada uno) |

Arreglos de la F2: pestaña «Pop-Up Events» (el renombrado «Pop-ups» → «Pop-Ups», solo de mayúsculas, lo convierte openpyxl
en «Pop-Ups1»); «Chefs de Partie» en `FRASES_OK_EXTRA`; dos plurales con tilde (`consommés`, `rosés`) fuera de la lista
blanca de G2. Decisiones del traductor (aceptadas): ml en el maridaje (≈60–80 ml por pase, sin pasar a oz), TheFork →
Yelp y OpenTable, caza de granja («farm-raised game»).

Nota de git: el worktree compartido tenía cambios sin commit de la F3 de los kits planos; para no tocarlos, un `merge` (no
`pull --rebase`) en `b26baf29`.

## Lo que la F3 tiene que saber (landing, dashboard, email)

- Es v2.0 completo (no plano): **sí** contador «Tasks done: X of Y» que no cuenta N/A, hoja «Instructions» en cada libro,
  firma de autor, línea de versión, protección en 10 y 11 (sin contraseña), caja US en dólares (11: recuento por
  denominaciones, POS Z report, OVER / SHORT, registro mensual), horas a 12 h en el 10 y el 11.
- **486 tareas** en 13 libros: apertura AM / cierre PM con equipamiento de vanguardia (circulador, deshidratador, Pacojet,
  sifones), mise en place del menú degustación por tiempos + plating bible, I+D (sesiones y documentación de receta),
  brigada por rol (executive chef, sous chef, hot line, garde manger, pastry chef, sommelier, maître d'), semanal /
  mensual / trimestral y anual de un restaurante US, maridaje y bodega, chef's table / pop-ups / cenas maridaje, foto /
  RRSS / prensa y guías (Michelin Guide, 50 Best, OAD, James Beard), 3 plantillas, negocio y caja + 2 bonus.
- FDA Food Code 2022: parásitos y aviso al consumidor para crudo, huevo a 145 °F, sous vide / ROP con HACCP o variance,
  9 alérgenos con sésamo; alcohol 21+ con licencia; service charge ≠ propina; FLSA en vez del registro de jornada.
- No prometer: una app, Google Sheets sin test, fechas españolas, guías españolas (Repsol), conversión a onzas.
- `$19`, env `VITE_STRIPE_PAYMENT_LINK_FINE_DINING_CHECKLISTS_KIT`, JWT `fine-dining-checklist-templates-jwt`; UK solo en la
  FAQ; enlaces naturales: Restaurant Checklists Kit Pro, HACCP Food Safety Kit Pro, Food Cost / Recipe Costing.

Erratas del ES: `SPEC.md` §5 (orden del 10 «Cierre del Negocio»; «14 UE» como alérgenos «comunes»).

## Ronda de revisión final de contenido (31-oct · sesión Claude Code; 0 bloqueantes, 2 major de seguridad alimentaria)

Aplicado (`f5a8bb7d` textos, mapas y FAQ de la landing; `de11cf0a` remontaje y republicación):
- **MAJOR 1** 02 «Long-Lead Prep» B24 (sous vide de pescado y marisco) y B25 (confitados): si van en bolsa y se enfrían o
  se guardan (reduced oxygen packaging), HACCP plan o variance del departamento de salud (FDA Food Code 3-502.11 /
  3-502.12) y enfriado según 3-501.14 (ADAPTAR declarado).
- **MAJOR 2** 04 «Hot Line» B8: lo cocinado y enfriado se recalienta a 165 °F en 2 h como máximo para mantenerlo en
  caliente (3-403.11) y se mantiene a 135 °F o más (3-501.16); el control de mantenimiento en caliente va en una tarea que ya
  existía de la línea caliente (B7 «Main cooking: proteins, hot sides» + lectura en °F), sin filas nuevas.
- Menores: B23 cita las tablas de tiempo y temperatura de 3-401.11; maridaje en **fl oz** (06 «Instructions» B13 «≈2–2.5 fl
  oz (60–80 ml)» y las 8 filas «…, temp., oz»; los gramos de hidrocoloides se quedan); B02 de mayo a julio con producto US
  (morels, ramps, soft-shell crab; chilled soups; heirloom tomatoes, corn, stone fruit) en vez de níspero, atún rojo,
  gazpachos y pescado azul; 07 «Pop-Up Events» B6 con temporary food event permit, aprobación sanitaria, lavamanos y
  mantenimiento en frío y en caliente en el sitio. Sin cambios: «chef de partie» ya va en minúscula en el texto y en Title
  Case en títulos; no hay fila de ostras crudas que ampliar (opcional, no aplicado).
- FAQ de la landing (`fine-dining-checklist-templates.ts`): «about 2–2.5 fl oz (60–80 ml) per course».

Resultado: **VERDE 8/0**, autotest 19/19, idempotencia 0, censo-entregables / no-latinos / LIT255 en 0.
