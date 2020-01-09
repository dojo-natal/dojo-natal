def quebra_linha(frase):
	
	tam=len(frase)

	palavras = frase.split(" ")
	if tam <= 20:
		return [frase]
	else:
		frases = []
		frase_linha = ''
		for palavra in palavras:
			if len(frase_linha) == 0:
				frase_linha += palavra
			else:
				if len(frase_linha) + len(palavra) + 1 <= 20:
					frase_linha += (' ' + palavra)
				else:
					frases.append(frase_linha)
					frase_linha = palavra
		if frase_linha:
			frases.append(frase_linha)
	return frases
	# 	pedaco 
	# 	for x in palavras:
		
	# 		pedaco = frase[x-20:x]
	# 		pedaco = pedaco.split(" ")
	# 		if pedaco[-1] in palavras:
	# 			frase_linha.append(frase[x-20:x])
	# 		else:

	# 		frase_linha


	# return frase_linha
	#while(i<=coluna):
		#frase_linha.append



	##for idx, ch in enumerate(frase):
	#	frase_linha.append(ch)
	#	print(idx, ch)
	#	if idx <= 20:
	#		frases.append(frase_linha)
	#		frase_linha = []
	#return frases


	#if frase == 'banana':
	#	return ['banana']
	#return ['banana banana banana']