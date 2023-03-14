const tempoDoMiojo = (ampulhetas, tempo) => {
  let [a, b] = ampulhetas

  if(tempo%a === 0 || tempo%b ===0 || tempo%(a+b) === 0){
    return tempo;
  }

  for (let passo = 1; passo <= 100; passo++) {
    let restoPassoA = passo%a;
    let restoPassoB = passo%b;
    if (restoPassoA == 0 || restoPassoB ==0){
      const viradasDeA = parseInt(passo/a);
      const viradasDeB = parseInt(passo/b);
      if ((viradasDeA * a)+b ===tempo) {
        return tempo;
      }
      if ((viradasDeB * b)+a ===tempo) {
        return tempo;
      }
      if (restoPassoA === tempo || restoPassoB === tempo) {
        return passo;
      }
    }
  }
};

console.log(tempoDoMiojo([5, 7], 3), 10)
console.log(tempoDoMiojo([5, 7], 5), 5)
console.log(tempoDoMiojo([5, 7], 7), 7)
console.log(tempoDoMiojo([5, 7], 15), 15)
console.log(tempoDoMiojo([5, 7], 4), 14)
console.log(tempoDoMiojo([5, 7], 12), 12)
console.log(tempoDoMiojo([5, 7], 24), 24)
console.log(tempoDoMiojo([5, 7], 17), 17)
console.log(tempoDoMiojo([5, 7], 11), 17)


// Possivel solucao
// function calc($amp1, $amp2, $coz, $r1, $r2) {
//   if ($r1 == $coz || $r2 == $coz) {
//     return $coz;
//   } elseif ($r1 == $r2) {
//     return "tempo de cozimento invalido";
//   }     

//       if ($r1 > $r2) {
//     return $r2 + $this->calc($amp1, $amp2, $coz, $r1 - $r2, $amp2);
//       } else {
//     return $r1 + $this->calc($amp1, $amp2, $coz, $amp1, $r2 - $r1);
//   }
// }

// function calcularTempo($amp1, $amp2, $coz) {
//   if ($coz >= $amp1) return "tempo de cozimento invalido";
//   if ($coz >= $amp2) return "tempo de cozimento invalido";
//   return $this->calc($amp1, $amp2, $coz, $amp1, $amp2);
// }