const fruits = ["Strawberry", "Banana", "Orange", "Apple"];
const foodSchedule = [ /* array del enunciado */ ];

let fruitIndex = 0;

for (let i = 0; i < foodSchedule.length; i++) {
  if (!foodSchedule[i].isVegan) {
    foodSchedule[i].name = fruits[fruitIndex];
    foodSchedule[i].isVegan = true; // Ahora es fruta, así que es vegano
    fruitIndex++;
    if(fruitIndex >= fruits.length) fruitIndex = 0; // Reiniciar frutas si se acaban
  }
}
console.log(foodSchedule);