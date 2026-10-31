"""sus_version.py — fija la versión del Plan de Negocio: Sushi Bar en «1.0 · noviembre 2026» SIN tocar el motor común (SPEC D3).

El motor (`planes-v2_0/motor.py`) estampa `VERSION = '2.2'` y `VERSION_MES = 'septiembre 2026'`. Este producto es
NUEVO (como la Churrería, la Heladería y la Finca: primera edición = 1.0) y sale con el merge previsto a primeros de noviembre. Importar este módulo
DESPUÉS de `import motor` parchea `VERSION`, `VERSION_MES` y `VERSION_FMT` en el proceso; los chequeos de `main.py`
(l. 585 y 813) y la estampa de los xlsx leen `motor.VERSION` en tiempo de ejecución. No modifica ningún fichero común.
Si un gate del motor exige '2.2', se pone `VERSION = '2.2'` aquí y se anota. Sesión Claude Code, 31-oct-2026 (copia de plan-polleria/pol_version.py). También la importa la calculadora.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'planes-v2_0'))
import motor  # noqa: E402

VERSION = '1.0'
MES = 'noviembre 2026'
motor.VERSION = VERSION
motor.VERSION_MES = MES
motor.VERSION_FMT = ('Versión ' + VERSION + ' · ' + MES + ' · aichef.pro/{pid} · info@aichef.pro')
