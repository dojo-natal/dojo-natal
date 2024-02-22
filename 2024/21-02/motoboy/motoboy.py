import math
from itertools import permutations 
 

def motoboy(n_pedidos, n_max, pedidos):
    max_tempo = 0
    permutacoes = []
    for n in range(n_pedidos):
        permutacoes += permutations(pedidos, n)

    permutacoes_soma = []
    for permuta in permutacoes:
        permutacoes_soma.append((
            sum([tempo for tempo, n_pizza in permuta]),
            sum([n_pizza for tempo, n_pizza in permuta]),
        )) 
    for soma in permutacoes_soma:
        tempo, n_pizza = soma
        if max_tempo < tempo and n_max >= n_pizza:
            max_tempo = tempo

    return max_tempo
     
    
    print(list(permutacoes))