
const users = [
	{id: 1, name: 'Abel'},
	{id:2, name: 'Julia'},
	{id:3, name: 'Pedro'},
	{id:4, name: 'Amanda'}
];
const names = users.map(user => user.name);
console.log(names);

// 3.2 Cambio el nombre si empieza por 'A'
const anacletoNames = users.map(user => {
    if (user.name.startsWith('A')) {
        return 'Anacleto'; 
    }
    return user.name;
});
console.log(anacletoNames);

const cities = [
	{isVisited:true, name: 'Tokyo'},
	{isVisited:false, name: 'Madagascar'},
	{isVisited:true, name: 'Amsterdam'},
	{isVisited:false, name: 'Seul'}
];
const cityNames = cities.map(city => {
    if (city.isVisited) {
        return city.name + ' (Visitado)';
    }
    return city.name;
});
console.log(cityNames);