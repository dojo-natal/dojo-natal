// http://dojopuzzles.com/problemas/exibe/geracao-de-fatores-primos/

const fatores_primos = require('./fatores_primos.js');

test('5', () => {
  expect(fatores_primos(5)).toEqual([5]);
});

test('100', () => {
  expect(fatores_primos(100)).toEqual([2, 2, 5, 5]);
});

test('9999999', () => {
  expect(fatores_primos(9999999)).toEqual([3, 3, 239, 4649]);
});