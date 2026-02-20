// 1.1 Crea una lista ul > li dinámicamente con los paises
const countries = ['Japón', 'Nicaragua', 'Suiza', 'Australia', 'Venezuela'];
const ulCountries = document.createElement('ul');

for (const country of countries) {
    const li = document.createElement('li');
    li.textContent = country;
    ulCountries.appendChild(li);
}
document.body.appendChild(ulCountries);

// 1.2 Elimina el elemento que tenga la clase .fn-remove-me.
const removeMe = document.querySelector('.fn-remove-me');
if (removeMe) removeMe.remove();

// 1.3 Utiliza el array para crear dinamicamente una lista ul > li en el div data-function="printHere".
const cars = ['Mazda 6', 'Ford fiesta', 'Audi A4', 'Toyota corola'];
const printHereDiv = document.querySelector('[data-function="printHere"]');
const ulCars = document.createElement('ul');

for (const car of cars) {
    const li = document.createElement('li');
    li.textContent = car;
    ulCars.appendChild(li);
}
printHereDiv.appendChild(ulCars);

// 1.4 Crea dinamicamente divs con h4 e img (y 1.6 Botón para eliminar ese elemento)
const countries2 = [
	{title: 'Random title', imgUrl: 'https://picsum.photos/300/200?random=1'},
	{title: 'Random title', imgUrl: 'https://picsum.photos/300/200?random=2'},
	{title: 'Random title', imgUrl: 'https://picsum.photos/300/200?random=3'},
	{title: 'Random title', imgUrl: 'https://picsum.photos/300/200?random=4'},
	{title: 'Random title', imgUrl: 'https://picsum.photos/300/200?random=5'}
];

for (const country of countries2) {
    const div = document.createElement('div');
    const h4 = document.createElement('h4');
    const img = document.createElement('img');
    const btnDelete = document.createElement('button');

    h4.textContent = country.title;
    img.src = country.imgUrl;
    btnDelete.textContent = 'Eliminar este elemento';

    btnDelete.addEventListener('click', () => {
        div.remove();
    });

    div.appendChild(h4);
    div.appendChild(img);
    div.appendChild(btnDelete);
    document.body.appendChild(div);
}

// 1.5 Crea un botón que elimine el último elemento de la serie de divs.
const btnRemoveLast = document.createElement('button');
btnRemoveLast.textContent = 'Eliminar el último';
btnRemoveLast.style.marginTop = '20px';
document.body.appendChild(btnRemoveLast);

btnRemoveLast.addEventListener('click', () => {
    const allDivs = document.querySelectorAll('div');
    if (allDivs.length > 0) {
        allDivs[allDivs.length - 1].remove();
    }
});