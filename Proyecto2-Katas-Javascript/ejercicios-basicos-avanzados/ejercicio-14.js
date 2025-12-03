function repeatCounter(list) {
  const counter = {};
  for (const word of list) {
    if (counter[word]) {
      counter[word]++;
    } else {
      counter[word] = 1;
    }
  }
  return counter;
}