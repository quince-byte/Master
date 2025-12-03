function findOldestXMen(xMen) {
  let oldest = xMen[0];
  for (const mutant of xMen) {
    if (mutant.year < oldest.year) {
      oldest = mutant;
    }
  }
  return oldest;
}