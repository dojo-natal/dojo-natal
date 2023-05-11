def facil(vetor, consultas):
  # ex = {
  #   1: [0, 7],
  #   2: [2, 3, 6]
  # }

  db = {}
  respostas = []

  for index, valor in enumerate(vetor):
    if db.get(valor): 
      db[valor].append(index + 1)
    else:
      db[valor] = [index + 1]

  for n_ocorrencias, v_consulta in consultas:
    ocorrencias = db.get(v_consulta)

    if len(ocorrencias) < n_ocorrencias:
      respostas.append(0)
      continue

    index_ocorrencia = ocorrencias[n_ocorrencias - 1]
    respostas.append(index_ocorrencia)

  return respostas
