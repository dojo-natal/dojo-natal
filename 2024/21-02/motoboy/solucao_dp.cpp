#include <bits/stdc++.h>

using namespace std;

int main() {
  // https://judge.beecrowd.com/pt/problems/view/1286

  // Esse problema é uma variação do problema da mochila
  // https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

  int n_pedidos = -1, n_pizzas_que_o_roberto_pode_carregar;
  while (true) {
    cin >> n_pedidos;
    if (n_pedidos == 0) break;
    cin >> n_pizzas_que_o_roberto_pode_carregar;
    // Receber os pedidos
    vector<pair<int, int>> pedidos(n_pedidos);
    for (auto &pedido : pedidos) cin >> pedido.first >> pedido.second;


    // Definir o estado inicial da PD
    int tabela[n_pedidos + 1][n_pizzas_que_o_roberto_pode_carregar + 1];
    memset(tabela, 0, sizeof(tabela));

    // Construir a tabela de baixo pra cima (bottomup).
    for (int n_itens = 1; n_itens <= n_pedidos; ++n_itens) {
      for (int capacidade = 0;
           capacidade <= n_pizzas_que_o_roberto_pode_carregar; ++capacidade) {
        auto [tempo, n_pizzas] = pedidos[n_itens - 1];
        // Ver se o pedido não estoura a capacidade
        if (n_pizzas > capacidade) {
          tabela[n_itens][capacidade] = tabela[n_itens - 1][capacidade];
          continue;
        }
        // Vale a pena ou não vale entregar esse pedido?
        tabela[n_itens][capacidade] =
            max(tabela[n_itens - 1][capacidade],
                tabela[n_itens - 1][capacidade - n_pizzas] + tempo);
      }
    }

    cout << tabela[n_pedidos][n_pizzas_que_o_roberto_pode_carregar]
         << " min.\n";
  }
}