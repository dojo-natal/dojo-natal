def tijolos(piramide):
	variables = []
	"""
	[2], (0, 0)
	[None, None], filho_esq + filho_dir == 2
	[1, None, 1]

	1 + neto_do_meio + 1 + neto_do_meio == 2
	
	2*neto_do_meio = o_cara - (neto_esq+neto_dir)
	
	filho_esq = 1 + neto_do_meio
	filho_dir = 1 + neto_do_meio
	"""
	# if len(piramide) == 3:
	# 	for i in range(0,len(piramide)-2,2):
	# 		for j in range(0,len(piramide),2):
	# 			# piramide[i + 2][j + 1] = (
	# 			# 	piramide[i][j] - (piramide[i+2][j] + piramide[i+2][j+2])
	# 			# ) / 2
				
	# 			# piramide[i + 1][j] = piramide[i+2][j] + piramide[i+2][j+1]
	# 			# piramide[i + 1][j + 1] = piramide[i+2][j+1] + piramide[i+2][j+2]

	return piramide

"""
if len(piramide) == 3:
	return [
		[2],
		[1, 1],
		[1, 0, 1]
	]
elif len(piramide) == 5:
	return [
		[24],
		[11, 13],
		[5, 6, 7],
		[2, 3, 3, 4],
		[2, 0, 3, 0, 4],
	]
elif len(piramide) == 9:
	return [
		[255],
		[121, 134],
		[54, 67, 67],
		[23, 31, 36, 31],
		[10, 13, 18, 18, 13],
		[5, 5, 8, 10, 8, 5],
		[3, 2, 3, 5, 5, 3, 2],
		[2, 1, 1, 2, 3, 2, 1, 1],
		[2, 0, 1, 0, 2, 1, 1, 0, 1],
	]"""