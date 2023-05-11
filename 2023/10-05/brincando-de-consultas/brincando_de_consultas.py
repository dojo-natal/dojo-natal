def consultar(vetor, consultas):
  respostas = []

  for consulta in consultas:
    operacao = consulta[0]
    if operacao == 1:
      _, x, w = consulta
      vetor[x - 1] = w
    else:
      _, x, y, w = consulta
      diferentes = 0
      for i in range(x - 1, y):
        if vetor[i] != w:
          diferentes += 1

      respostas.append(diferentes)

  return respostas
