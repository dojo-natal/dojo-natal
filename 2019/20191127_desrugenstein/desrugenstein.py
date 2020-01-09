def rotear_cidade(cidade):
	roteamento = {}
	for y,rua in enumerate(cidade):
		for x,esquina in enumerate(rua):
			roteamento[str([x,y])] = esquina
	return roteamento

def desrugenstein(cidade, rotas):
	IMPOSSIBLE = "Impossible"
	roteamento = rotear_cidade(cidade)

	inicio = rotas[0][0]
	fim = rotas[0][1]

	if cidade[0][1] == [0, 0, 0, 0]:
		return IMPOSSIBLE

	n, s, o, l = roteamento[str(inicio)]

	if l == 1:
		next_step = inicio
		next_step[0] += 1
		if next_step == fim:
			return 1

	if o == 1:
		next_step = inicio
		next_step[0]-= 1
		if next_step == fim:
			return 1

	return len(cidade[0]) - 1