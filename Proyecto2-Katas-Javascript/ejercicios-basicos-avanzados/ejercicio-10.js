function average(numberList) {
  if (numberList.length === 0) return 0;
  let sum = sumNumbers(numberList);
  return sum / numberList.length;
}