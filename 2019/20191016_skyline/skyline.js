// [[2, 4, 3], [5, 6, 3]]
// [[2, 3],[4, 0], [5, 3], [6, 0]]
// const iterBuilding = (building) => {
//   return [[building[0][0], building[0][2]],[building[0][1], 0]];
// }
module.exports = function (buildings) {
  return buildings.reduce((points, building) => {
    points.push([building[0],building[2]])
    points.push([building[1],0])
    return points;
  }, []);
};