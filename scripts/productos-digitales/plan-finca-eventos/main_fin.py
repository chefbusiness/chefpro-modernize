"""main_fin.py — ejecuta `planes-v2_0/main.py` con la versión «1.0 · noviembre 2026» (ver fin_version.py). Mismos argumentos.
Copia de `plan-heladeria/main_hel.py`. Sesión Claude Code, 25-oct-2026."""
import os
import runpy
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import fin_version  # noqa: E402,F401
MAIN = os.path.join(os.path.dirname(AQUI), 'planes-v2_0', 'main.py')
sys.argv[0] = MAIN
runpy.run_path(MAIN, run_name='__main__')
