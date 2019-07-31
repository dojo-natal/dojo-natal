const fatores_primos = function (a, fatores = []) {
  let resto = a;
  for(let i=2; i <= resto; i++) {
    while(resto % i == 0) {
      fatores.push(i);
      resto /= i;
    }
    if (resto == 0)
      break;
  }
  return fatores;
};

module.exports = fatores_primos;