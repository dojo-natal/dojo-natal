def miojo(tempo, amp1, amp2):	
	if amp1 == tempo or amp2 == tempo:
		return True

	orig1 = amp1
	orig2 = amp2

	while True:
		menor = min(amp1, amp2)
		amp1 -= menor
		amp2 -= menor

		if amp1 + amp2 == tempo:
			return True		
		if amp1 and tempo % amp1 == 0:
			return True
		if amp2 and tempo % amp2 == 0:
			return True
		if abs(amp1 - amp2) == tempo:
			return True
		if not amp1 and not amp2:
			return False

		amp1 = orig1 if not amp1 else amp1
		amp2 = orig2 if not amp2 else amp2
