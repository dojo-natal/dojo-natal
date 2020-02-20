from functools import reduce


def babel(origem, destino, edges):
    def create_map_origem(edges):
        def fn(acc, x):
            acc[x[0]] = [x[1], x[2]]
            return acc
        return reduce(fn, edges, {})
        
    def walk(origem, destino, map_origem_destino, acc=0):
        if origem == destino:
            return acc
        destino_tmp, palavra = map_origem_destino[origem]
        return walk(destino_tmp, destino, map_origem_destino, acc + len(palavra))

    if destino not in [edge[0] for edge in edges] + [edge[1] for edge in edges]:
        return "impossivel"
    return walk(origem, destino, create_map_origem(edges), acc=0)