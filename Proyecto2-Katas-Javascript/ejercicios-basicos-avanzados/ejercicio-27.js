const cartoons = [ /* array del enunciado */ ];
let oldestCartoon = cartoons[0];

for (const cartoon of cartoons) {
  if (cartoon.debut < oldestCartoon.debut) {
    oldestCartoon = cartoon;
  }
}
console.log(oldestCartoon.name);