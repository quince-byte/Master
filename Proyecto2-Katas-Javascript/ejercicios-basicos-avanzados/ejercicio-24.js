const characters = [ /* array del enunciado */ ];
const humanCharacters = [];

for (const char of characters) {
  if (char.species === 'Human') {
    humanCharacters.push(char);
  }
}
console.log(humanCharacters);