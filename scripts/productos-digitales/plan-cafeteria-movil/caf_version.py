"""caf_version.py — fija la versión de la Cafetería Móvil para Eventos en «1.0 · octubre 2026» SIN tocar el motor común (SPEC D3).

El motor (`planes-v2_0/motor.py`) estampa `VERSION = '2.2'` y `VERSION_MES = 'septiembre 2026'`. Este producto es NUEVO
(como la Finca y la Pizzería: primera edición = 1.0) y sale con el merge previsto el 28-31 de octubre: «octubre 2026». Si
el merge cae en noviembre, se cambia `MES` AQUÍ a «noviembre 2026» y se regeneran los cuatro ficheros a la vez (plan,
checklist, calculadora y Word: todos importan este módulo). Importar este módulo DESPUÉS de `import motor` parchea
`VERSION`, `VERSION_MES` y `VERSION_FMT` en el proceso; los chequeos de `main.py` y la estampa de los xlsx leen
`motor.VERSION` en tiempo de ejecución. No modifica ningún fichero común. Sesión Claude Code, 28-oct-2026 (copia de
plan-pizzeria/piz_version.py). También la importan la calculadora y el ensamblador del Word.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'planes-v2_0'))
import motor  # noqa: E402

VERSION = '1.0'
MES = 'octubre 2026'
motor.VERSION = VERSION
motor.VERSION_MES = MES
motor.VERSION_FMT = ('Versión ' + VERSION + ' · ' + MES + ' · aichef.pro/{pid} · info@aichef.pro')
