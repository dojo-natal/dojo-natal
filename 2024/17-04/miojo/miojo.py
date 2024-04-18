def miojo(a, b, t):
  tempo_a = a
  tempo_b = b
  tempo_total = 0

  while (tempo_a != t and tempo_b != t): 
    if(tempo_a < tempo_b):
      tempo_b -= tempo_a
      tempo_total +=  tempo_a
      tempo_a = a
    else:
      tempo_a -= tempo_b
      tempo_total +=  tempo_b
      tempo_b = b

  return tempo_total+t

  """
  tempo mínimo necessário para o miojo ficar pronto
  """
"""   menor = min(a, b)
  maior = max(a, b) """

  # 3 = 2 * 5 - 7
  # 3 = 2 * 5 - 1 * 7
  
"""
  
  
  [22]--------------|----------|                2*
  [15]              |----------|--------|       2*
                   22         37        52



  [22]--------------|-----------|-              2*
  [15]--------|----------|--------|             3*
              15   22    30    44 45
                7     8     14   1

  """
""" 
  tempo_a = 0
  tempo_b = 0
  tempo_total = 0

  tempo_a = 0
  tempo_b = 15 
  tempo_total = 15

  tempo_a = 22
  tempo_b = 15 
  tempo_total = 22

  tempo_a = 22
  tempo_b = 30 
  tempo_total = 30

  tempo_a = 22
  tempo_b = 30 
  tempo_total = 44
 """


    

