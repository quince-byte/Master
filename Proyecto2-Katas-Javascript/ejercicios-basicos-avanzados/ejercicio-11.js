function averageWord(list) {
  let sum = 0;
  for (const element of list) {
    if (typeof element === 'number') {
      sum += element;
    } else if (typeof element === 'string') {
      sum += element.length;
    }
  }
  return sum / list.length;
}