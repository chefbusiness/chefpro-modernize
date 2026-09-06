# -*- coding: utf-8 -*-
"""
Segunda pasada tras el GATE inicial: 12 entradas quedaron sin url y sin nota
de lista negra. Ninguna URL se inventa (ninguna de las dos L3/L4 dan un
enlace verificable para estas filas). Dos reciben una url YA VERIFICADA en
otra fila del mismo documento/misma norma (reutilización legítima, no
invención); las otras diez pasan al tratamiento de lista negra (fiabilidad
baja, cifra vacía, nota explícita), igual que CS-14..18/21..23.
"""
import json
from pathlib import Path

JSON_PATH = Path(__file__).parent / "guias-v2-research-sector.json"
BLACKLIST_NOTA = "LISTA NEGRA: no se cita; el lector lo mide con su herramienta."

INSST_URL = ("https://www.insst.es/documents/94886/5326464/Informe+anual+de+"
             "accidentes+de+trabajo+en+Espa%C3%B1a.+Datos+2024.pdf")
EURLEX_2073 = "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:02005R2073-20200308"

# id -> (nuevo url o None, nuevas fiabilidad/cifra/nota_extra)
REUSO_URL = {
    "CS-05": INSST_URL,   # misma fuente primaria que CS-01/CS-02 (informe INSST 2024)
    "CE-37": EURLEX_2073,  # la síntesis se apoya en la misma norma ya citada en CE-08
}

BLACKLIST_IDS = ["CE-36", "CS-03", "CS-06", "CS-08", "CS-09", "CS-10", "CS-11", "CS-12", "CS-19", "CS-20"]


def main():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    por_id = {d["id"]: d for d in data["datos"]}

    for id_, url in REUSO_URL.items():
        d = por_id[id_]
        d["url"] = url
        d["nota"] = d["nota"] + " Reutiliza la url ya verificada de otra fila del mismo bloque (misma fuente primaria); no se ha localizado un enlace propio para esta cifra concreta."

    for id_ in BLACKLIST_IDS:
        d = por_id[id_]
        d["fiabilidad"] = "baja"
        d["cifra"] = ""
        if BLACKLIST_NOTA not in d["nota"]:
            d["nota"] = BLACKLIST_NOTA + " " + d["nota"]
        d["url"] = ""

    JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {len(REUSO_URL)} con url reutilizada, {len(BLACKLIST_IDS)} pasadas a lista negra.")


if __name__ == "__main__":
    main()
