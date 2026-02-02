const placesToTravel2 = [
  { id: 5, name: "Japan" },
  { id: 11, name: "Venecia" },
  { id: 23, name: "Murcia" },
  { id: 40, name: "Santander" },
  { id: 44, name: "Filipinas" },
  { id: 59, name: "Madagascar" },
];

const filteredPlaces = [];
for (let i = 0; i < placesToTravel2.length; i++) {
    if (placesToTravel2[i].id !== 11 && placesToTravel2[i].id !== 40) {
        filteredPlaces.push(placesToTravel2[i]);
    }
}
console.log(filteredPlaces);