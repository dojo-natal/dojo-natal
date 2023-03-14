def jogando_cartas_fora(n: int) -> tuple:
  cartas = [i for i in range(1, n+1)]
  discartes = []

  while len(cartas) > 1:
    discartes.append(cartas.pop(0))
    cartas.append(cartas.pop(0))
    
  return (discartes, cartas[0])
