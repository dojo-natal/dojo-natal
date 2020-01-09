from itertools import combinations

global gw1
global gw2

def sequencias_de_dna(w1,w2,k):
	# gw1 = w1
	# gw2 = w2
	# gk = k
	# return sequencias_de_dna_rec(0,0,0,0)
	return sequencias_de_dna_itr(w1, w2, k)

def sequencias_de_dna_rec(iw1, iw2, len, seg_len):
	# if (iw1 >= len(gw1))
	pass


def sequencias_de_dna_itr(w1, w2, k):
	if w1 == w2:
		return len(w1)

	max_word_len = max([len(w1), len(w2)])
	substringslen = []

	for seg_len in reversed(range(1, max_word_len)):
		for segmento in combinations(w1, seg_len):
			if "".join(segmento) in w2:
				return len(segmento)
				

	return 0