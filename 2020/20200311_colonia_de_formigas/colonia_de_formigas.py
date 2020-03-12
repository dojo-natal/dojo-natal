def colonia_de_formigas(tuneis, queries):
    def make_formigueiros(tuneis):
        formigueiros = {}
        for tunel in tuneis:
            formigueiros[tunel[0]] = (tunel[1], tunel[2])
        return formigueiros

    formigueiros = make_formigueiros(tuneis)

    def walk(inicio, destino_final):
        if inicio not in formigueiros.keys():
            return 0
        destino = formigueiros[inicio][0]
        distancia = formigueiros[inicio][1]
        return distancia + walk(destino, destino_final)

    return walk(queries[0][0], queries[0][1])