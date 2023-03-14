const availableNotes = [100, 50, 20, 10];

function saque (valor) {
  const resultado = [];

  for (const notaAtual of availableNotes) {
    while (notaAtual <= valor) {
      valor = valor - notaAtual;
      resultado.push(notaAtual);
    }
  }

  if (valor > 0) {
    throw new Error("nao da para sacar: " + valor)
  }
 
  
  return resultado;
}

console.log(saque(10), [10]);
console.log(saque(30), [20, 10]);
console.log(saque(80), [50, 20, 10]);
console.log(saque(300), [100, 100, 100]);
console.log(saque(2), []);
