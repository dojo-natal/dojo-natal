from math import ceil
from sys import setrecursionlimit

setrecursionlimit(9999)


def rec_josephus(circulo, salto, posicao_atual):
	if len(circulo) == 1:
		return circulo[0]
	tamanho_circulo = len(circulo)
	if tamanho_circulo > salto+posicao_atual:
		del circulo[salto-1]
		posicao_atual=salto-1
	else:
		morre = salto + posicao_atual - 1
		while morre >= tamanho_circulo:
			morre -= tamanho_circulo
		del circulo[morre]
		posicao_atual = morre
	return rec_josephus(circulo,salto,posicao_atual)

def josephus(n_pessoas, salto):
	return rec_josephus(range(1, n_pessoas + 1), salto, 0)
	if n_pessoas == 3:
		if salto == 1 or salto == 2:
			return n_pessoas
		elif salto in (3, 4):
			return 2
		elif salto in (5, 6):
			return 1
	elif n_pessoas == 2:
		if salto % 2 == 0:
			return 1
		return 2