def play_tenis(lances):
	pontos_jogado_a = 0
	pontos_jogado_b = 0

	for jogador in lances:
		if jogador == 1:
			pontos_jogado_a += 5
		else:
			pontos_jogado_b += 5

	if pontos_jogado_a == pontos_jogado_b:
		return 'D'

	if pontos_jogado_a > pontos_jogado_b:
		return 1
	
	return 2