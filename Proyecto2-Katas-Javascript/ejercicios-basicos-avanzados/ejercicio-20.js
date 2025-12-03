const popularToys = [];
const toys2 = [ /* array del enunciado */ ];

for (const toy of toys2) {
    if (toy.sellCount > 15) {
        popularToys.push(toy);
    }
}
console.log(popularToys);