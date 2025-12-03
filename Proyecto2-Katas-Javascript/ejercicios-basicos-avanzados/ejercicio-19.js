const toys = [ /* array del enunciado */ ];
const noCatToys = [];

for (const toy of toys) {
    if (!toy.name.includes("gato")) {
        noCatToys.push(toy);
    }
}
console.log(noCatToys);