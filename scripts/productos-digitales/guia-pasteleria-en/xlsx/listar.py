"""Lista numerada de las cadenas ES de un libro (índice estable = orden de textos_es.json)."""
import json, sys, os
d = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'textos_es.json')))
b = d[sys.argv[1]]
for i, (s, w) in enumerate(b.items(), 1):
    if all(x.startswith('chart-ref') for x in w):
        continue
    print(i, repr(s), '<<', w[0][:28])
