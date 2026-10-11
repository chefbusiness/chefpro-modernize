"""par_version.py — fija el mes de la versión del Parrillero 2.2 en «octubre 2026» SIN tocar el motor común.

El motor (`planes-v2_0/motor.py`) estampa `VERSION_MES = 'septiembre 2026'` (la 2.1). Este producto sale en octubre y el pack
ya decía «octubre» en proveedores y landing (m6 de REVISION-FINAL). Importar este módulo DESPUÉS de `import motor` parchea
`VERSION_MES`/`VERSION_FMT` en el proceso; no modifica ningún fichero común. Sesión Claude Code, 12-oct-2026.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'planes-v2_0'))
import motor  # noqa: E402

MES = 'octubre 2026'
motor.VERSION_FMT = motor.VERSION_FMT.replace(motor.VERSION_MES, MES)
motor.VERSION_MES = MES
