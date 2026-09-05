#!/usr/bin/env python3
"""np-ipn-sign.py — firma un payload de IPN de NOWPayments con el IPN secret de un
fichero 600 e imprime SOLO la firma (hex). Sirve para probar el receptor
`nowpayments-ipn` sin pagar: un IPN con `payment_status` intermedio debe
responder 200 {ignored:<estado>}, y uno `finished` con un payment_id inventado
debe acabar en 500 reconfirm_failed (la function reconfirma contra la API y no
entrega sin ella). Algoritmo = el oficial (claves ordenadas recursivamente,
separadores compactos, HMAC-SHA512, secreto con trim). Uso:
  python3 scripts/productos-digitales/np-ipn-sign.py '<json>' [fichero-secreto]
"""
import hashlib, hmac, json, os, sys

def sort_deep(v):
    if isinstance(v, dict):
        return {k: sort_deep(v[k]) for k in sorted(v)}
    if isinstance(v, list):
        return [sort_deep(x) for x in v]
    return v

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    payload = json.loads(sys.argv[1])
    fichero = sys.argv[2] if len(sys.argv) > 2 else os.path.expanduser('~/.config/nowpayments/ipn-secret')
    secreto = open(fichero, encoding='utf-8').read().strip()
    # JSON.stringify de JS: separadores compactos y sin escapar no-ASCII
    cuerpo = json.dumps(sort_deep(payload), separators=(',', ':'), ensure_ascii=False)
    print(hmac.new(secreto.encode('utf-8'), cuerpo.encode('utf-8'), hashlib.sha512).hexdigest())

if __name__ == '__main__':
    main()
