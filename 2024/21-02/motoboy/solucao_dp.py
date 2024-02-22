#Solução usando Programação Dinâmica
#https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def motoboy(n_pedidos, n_max, pedidos):
  tabela = [[0 for j in range(n_max+1)] for i in range(n_pedidos+1)]

  for n_itens in range(1, len(tabela)):
    for capacidade in range(0, len(tabela[0])):
      tempo, n_pizzas = pedidos[n_itens-1]
      
      if n_pizzas > capacidade:
        tabela[n_itens][capacidade] = tabela[n_itens-1][capacidade]
        continue
      
      tabela[n_itens][capacidade] = max(tabela[n_itens-1][capacidade], tabela[n_itens-1][capacidade-n_pizzas]+tempo)
  
  return tabela[n_pedidos][n_max]