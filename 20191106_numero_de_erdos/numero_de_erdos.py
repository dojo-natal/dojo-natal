from collections import defaultdict

"""
    ponto_inicial = {"erdos": None}
    for publicacao in publicacoes:
        if "erdos" in publicacao:
            publicacao.remove("erdos")
            for autor in publicacao:
                ponto_inicial["erdos"][autor] = None
        else:
            for autor in publicacao:
                if autor in ponto_inicial["erdos"].keys():
                    publicacao2 = publicacao
                    publicacao2.remove(autor)
                    for autor2 in publicacao2:
                        ponto_inicial["erdos"][autor][autor2] = None

    print(ponto_inicial)
"""


def numero_de_erdos(publicacoes):
    counter = defaultdict(int)

    for publicacao in publicacoes:
        for autor in publicacao:
            if "erdos" in publicacao:
                counter[autor] += 1
            else:
                counter[autor] = "infinito"

    counter.pop("erdos", None)
    return dict(counter)
