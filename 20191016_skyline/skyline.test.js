// https://leetcode.com/problems/the-skyline-problem/
// Ri - Li > 0
const skyline = require('./skyline.js');

test('um building', () => {
  const buildings = [[2, 3, 1]];
  expect(skyline(buildings)).toEqual([[2, 1], [3,0]]);
});

test('um building maior', () => {
  const buildings = [[2, 4, 3]];
  expect(skyline(buildings)).toEqual([[2, 3], [4, 0]]);
});

test('dois buildings diferentes e separados', () => {
  const buildings = [[2, 4, 3], [5, 6, 3]];
  expect(skyline(buildings)).toEqual([[2, 3],[4, 0], [5, 3], [6, 0]]);
});

test('dois buildings diferentes e juntos', () => {
  const buildings = [[2, 4, 3], [5, 6, 3], [7, 8, 10]];
  expect(skyline(buildings)).toEqual([[2, 3],[4, 0], [5, 3], [6, 0], [7,10], [8, 0]]);
});

