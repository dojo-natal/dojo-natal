def numeros_romanos(numero):
	romanos = ((1,'I'),(5,'V'),(10,'X'),(50, 'L'), (100, 'C'))
	numeros_romanos= ''

	for i in reversed(romanos):
		divisao = numero / romanos[i][0]
		if not divisao:
			numeros_romanos = divisao * romanos[i][1]
			return numeros_romanos
		else:
			divisao = numero % romanos[0][0]
			numeros_romanos += divisao * romanos[1][1]
			return numeros_romanos
		# resultado_divisao_inteira = numero // i[0]
		# is_in_number = True if resultado_divisao_inteira != 0 else False
		# if is_in_number:
		# 	numeros_romanos += i[1] * resultado_divisao_inteira
		# 	break
		# else:
		# 	continue


	if numero < 4:
		return numero * 'I'
	if numero >= 5 and numero < 10:
		return 'V' + (numero - 5) * 'I'
	if numero == 4:
		return 'IV'
	if numero < 40:
		return (numero / 10) * 'X'
	if numero == 40:
		return 'XL'
	if numero >= 50 and numero < 90:
		return 'L' + ((numero - 50) / 10) * 'X'
	if numero == 90:
		return 'XC'
	return 'X'
