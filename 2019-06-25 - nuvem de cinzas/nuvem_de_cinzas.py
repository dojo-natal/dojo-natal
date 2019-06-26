def nuvem_de_cinzas(mapa):
	coordenadas_cinzas = []
	coordenadas_aeroporto = []
	answer = -1
	
	for idx_linha, linha in enumerate(mapa):
		for idx_quadrado, quadrado in enumerate(linha):
			if quadrado == '*':
				coordenadas_cinzas.append((idx_linha, idx_quadrado))
			if quadrado == 'A':
				coordenadas_aeroporto.append((idx_linha, idx_quadrado))
	
	for aero in coordenadas_aeroporto:
		x_aero, y_aero = aero
		dias_aero  = -1
		for nuvem in coordenadas_cinzas:
			x_nuvem, y_nuvem = nuvem
			dist = abs(x_aero-x_nuvem) + abs(y_aero-y_nuvem)
			dias_aero = dist if dias_aero == -1 else min(dist, dias_aero)
		answer = dias_aero if dias_aero == -1 else max(answer, dias_aero)

	return answer