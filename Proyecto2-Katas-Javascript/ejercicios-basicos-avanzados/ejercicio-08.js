function findLongestWord(stringList) {
  let longestWord = "";
  for (const word of stringList) {
    if (word.length > longestWord.length) {
      longestWord = word;
    }
  }
  return longestWord;
}