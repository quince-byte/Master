// 1.1 Destructuring de objeto
const game = {title: 'The Last of Us 2', gender: ['action', 'zombie', 'survival'], year: 2020};
const { title, gender, year } = game;
console.log(title, gender, year);

// 1.2 Destructuring de array
const fruits = ['Banana', 'Strawberry', 'Orange'];
const [fruit1, fruit2, fruit3] = fruits;
console.log(fruit1, fruit2, fruit3);

// 1.3 Destructuring de retorno de función
const animalFunction = () => {
    return {name: 'Bengal Tiger', race: 'Tiger'} 
};
const { name: animalName, race } = animalFunction(); 
// Nota: he renombrado 'name' a 'animalName' para evitar conflictos si ya existiera, 
// pero { name, race } también es válido.
console.log(animalName, race);

// 1.4 Destructuring anidado o secuencial
const car = {name: 'Mazda 6', itv: [2015, 2011, 2020] };
const { name: carName, itv } = car;
const [year1, year2, year3] = itv;

console.log(carName, itv);
console.log(year1, year2, year3);