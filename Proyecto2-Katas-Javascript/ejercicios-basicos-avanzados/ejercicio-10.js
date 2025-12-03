function average(numberList) {
  if (numberList.length === 0) return 0;
  let sum = sumNumbers(numberList); // Reutilizando la lógica de suma anterior
  return sum / numberList.length;
}