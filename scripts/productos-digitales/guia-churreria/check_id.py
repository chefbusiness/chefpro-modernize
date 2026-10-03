#!/usr/bin/env python3
"""Verifica un bloque redactado por su id del index.json (envoltorio de guias-v2_0/check_bloque.py).
Uso: python3 check_id.py <id>   → exit 0 = limpio; 1 = defectos."""
import json, os, subprocess, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
idx = json.load(open(os.path.join(AQUI, 'build/docs/prompts/index.json'), encoding='utf-8'))
b = next(x for x in idx if x['id'] == sys.argv[1])
if not os.path.exists(b['ruta_txt']):
    print('NO EXISTE', b['ruta_txt']); sys.exit(1)
sys.exit(subprocess.call([sys.executable, os.path.join(AQUI, '../guias-v2_0/check_bloque.py'),
                          b['ruta_txt'], str(b['palabras_min'])] + b['epigrafes']))
