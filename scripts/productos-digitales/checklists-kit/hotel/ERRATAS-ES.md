# Kit de Tareas Hotel Completo (ES LIVE) — erratas cazadas en la revisión final del EN (27-oct-2026 · sesión Claude Code)

**E1 y E2 y la errata «piscina/jacuzzi» de `SPEC.md` §5, RESUELTAS el 27-oct-2026 en el ES LIVE** (parche en el XML de las 3 celdas `inlineStr`, sin cambio de versión ni correo; mismo texto en `scripts/generate-tareas-hotel.py`; volcado ES `revision/dump_es.txt` = solo esas 3 celdas). El resto de erratas de `SPEC.md` §5 sigue pendiente para la v2.x. Fichero: `astro-site/public/dl/kit-tareas-hotel/`. Se suman a las de `SPEC.md` §5 (orden del
cierre del 18, variante «Apertura y Cierre», «< 5 °C» frente a «0-4 °C», «piscina/jacuzzi 35-38 °C», el 18 como
plantilla de restaurante), que no se repiten aquí. Decide el orquestador.

| # | Fichero · hoja · celda | Qué está mal | Propuesta |
|---|---|---|---|
| E1 (seguridad) · **RESUELTA** | `15-spa-wellness.xlsx` · «Cierre Spa» · B7 | «Apagar saunas, baño de vapor y jacuzzi»: al pie de la letra se apaga también la filtración, la recirculación y la desinfección del jacuzzi. Agua caliente parada toda la noche = biofilm y legionela (las bañeras de hidromasaje de uso colectivo son instalación de riesgo en el RD 487/2022, que el propio kit cita en el 13); en el código US (MAHC 2024 §5.12.1.1 y §6.6.3.1) es motivo de cierre inmediato | «Apagar saunas y baño de vapor; en el jacuzzi apagar solo chorros y soplante: la filtración, la recirculación y la desinfección siguen en marcha las 24 h» (comprobar el anexo del RD 487/2022 y la norma autonómica de piscinas antes de citarlos) |
| E2 (menor) · **RESUELTA** | `09-housekeeping.xlsx` · «Deep Cleaning» · B13 | «Pulir suelos (parqué, mármol, moqueta según material)»: la moqueta no se pule | «Pulir suelos duros (parqué, mármol) y lavar la moqueta con inyección-extracción, según material» |
