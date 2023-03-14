def bolhas_e_baldes(seq: list) -> str:
  is_sorted = False
  count_mudancas = 0

  while not is_sorted:
    count = 0

    for i in range(len(seq)):
      if i + 1 < len(seq):
        if seq[i] > seq[i + 1]:
          aux = seq[i]
          seq[i] = seq[i + 1]
          seq[i + 1] = aux
          count_mudancas += 1
        else:
          count += 1

    if (count == len(seq) - 1):
      is_sorted = True

  return "Carlos" if count_mudancas % 2 == 0 else "Marcelo" 