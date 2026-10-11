#!/usr/bin/env python3
"""regresion5.py — gate D1/D12 del Catering ES 2.0: el cambio de `grupo_a.compilar_vocabulario` no mueve nada en los
5 planes de línea A vivos. Para cada uno: `main.py --dry-run --solo a --sin-demos` y huella (`main.digest`) de cada xlsx
del dry-run frente al publicado en `dl/`. Exige 0 diferencias. Corre en el VPS (openpyxl). Sesión Claude Code, 11-oct-2026.

    CLAUDE_SCRATCHPAD=/root/tmp-cates-f2 /root/venv-guias/bin/python regresion5.py
"""
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
P2 = os.path.join(os.path.dirname(AQUI), 'planes-v2_0')
sys.path.insert(0, P2)
import main as M                                                          # noqa: E402

PIDS = ('plan-negocio-bar-restaurante', 'plan-negocio-tapas-bar', 'plan-negocio-cafeteria',
        'plan-negocio-panaderia', 'plan-negocio-food-truck')
total = 0
for pid in PIDS:
    r = subprocess.run([sys.executable, os.path.join(P2, 'main.py'), '--producto', pid, '--dry-run', '--solo', 'a',
                        '--sin-demos'], capture_output=True, text=True, cwd=P2)
    salida = os.path.join(M.SCRATCH, 'dryrun', pid)
    difs = []
    for n in M.xlsx_de(salida):
        difs += M.diff_digest(M.digest(os.path.join(M.DL, pid, n)), M.digest(os.path.join(salida, n)), n)
    total += len(difs)
    print('%-32s exit %d · diferencias frente a dl/: %d' % (pid, r.returncode, len(difs)))
    for d in difs[:8]:
        print('    ' + d[:200])
print('REGRESIÓN 5 PLANES: %s (%d diferencias)' % ('VERDE' if total == 0 else 'ROJO', total))
sys.exit(1 if total else 0)
