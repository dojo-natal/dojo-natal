def telefone(frase):
	numeroTelefone = []
	mapinha = {
		"-": "-", 
		"1": "1",
		"0": "0",
		"G": "4",
		"H": "4",
		"K": "5",
		"Z": "9",
		"A": "2",
		"M": "6",
		"N": "6",
		"Y": "9",
		"L": "5",
		"O": "6",
		"V": "8",
		"E": "3",
		"S": "7",
		"P": "7",
		" ": " ",
		"W": "9",
		"T": "8",
		"B": "2",
		"C": "2"
	}
	for n in frase:
		numeroTelefone.append(mapinha[n])
	
	return "".join(numeroTelefone)
