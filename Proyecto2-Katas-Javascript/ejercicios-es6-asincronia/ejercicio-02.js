// 2.1 Copia de array
const pointsList = [32, 54, 21, 64, 75, 43];
const pointsListCopy = [...pointsList];
console.log(pointsListCopy);

// 2.2 Copia de objeto
const toy = {name: 'Bus laiyiar', date: '20-30-1995', color: 'multicolor'};
const toyCopy = {...toy};
console.log(toyCopy);

// 2.3 Unir arrays
const pointsListA = [32, 54, 21, 64, 75, 43];
const pointsListB = [54,87,99,65,32];
const combinedPoints = [...pointsListA, ...pointsListB];
console.log(combinedPoints);

// 2.4 Fusionar objetos
const toyOriginal = {name: 'Bus laiyiar', date: '20-30-1995', color: 'multicolor'};
const toyUpdate = {lights: 'rgb', power: ['Volar like a dragon', 'MoonWalk']};
const toyFusion = {...toyOriginal, ...toyUpdate};
console.log(toyFusion);

// 2.5 Copia eliminando la posición 2
const colors = ['rojo', 'azul', 'amarillo', 'verde', 'naranja'];
const colorsNew = [...colors.slice(0, 2), ...colors.slice(3)]; 
console.log(colorsNew);