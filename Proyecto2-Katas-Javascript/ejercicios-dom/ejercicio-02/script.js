// 2.1 Inserta dinamicamente en un html un div vacio con javascript.
const newDiv = document.createElement('div');
document.body.appendChild(newDiv);

// 2.2 Inserta dinamicamente en un html un div que contenga una p con javascript.
const divWithP = document.createElement('div');
const pInsideDiv = document.createElement('p');
pInsideDiv.textContent = 'Hola, estoy dentro';
divWithP.appendChild(pInsideDiv);
document.body.appendChild(divWithP);

// 2.3 Inserta dinamicamente en un html un div que contenga 6 p utilizando un loop con javascript.
const divLoop = document.createElement('div');
for (let i = 0; i < 6; i++) {
    const p = document.createElement('p');
    p.textContent = `Párrafo número ${i + 1}`;
    divLoop.appendChild(p);
}
document.body.appendChild(divLoop);

// 2.4 Inserta dinamicamente con javascript en un html una p con el texto 'Soy dinámico!'.
const dynamicP = document.createElement('p');
dynamicP.textContent = 'Soy dinámico!';
document.body.appendChild(dynamicP);

// 2.5 Inserta en el h2 con la clase .fn-insert-here el texto 'Wubba Lubba dub dub'.
const h2 = document.querySelector('.fn-insert-here');
h2.textContent = 'Wubba Lubba dub dub';

// 2.6 Basandote en el siguiente array crea una lista ul > li con los textos del array.
const apps = ['Facebook', 'Netflix', 'Instagram', 'Snapchat', 'Twitter'];
const ul = document.createElement('ul');

for (const app of apps) {
    const li = document.createElement('li');
    li.textContent = app;
    ul.appendChild(li);
}
document.body.appendChild(ul);

// 2.7 Elimina todos los nodos que tengan la clase .fn-remove-me
const elementsToRemove = document.querySelectorAll('.fn-remove-me');
for (const element of elementsToRemove) {
    element.remove();
}

// 2.8 Inserta una p con el texto 'Voy en medio!' entre los dos div. 
// Seleccionamos todos los divs. Según el HTML, los dos divs vacíos están juntos antes de los divs con clase.
const allDivs = document.querySelectorAll('div');
const pMiddle = document.createElement('p');
pMiddle.textContent = 'Voy en medio!';
// Insertamos antes del segundo div encontrado (índice 1)
document.body.insertBefore(pMiddle, allDivs[1]);

// 2.9 Inserta p con el texto 'Voy dentro!', dentro de todos los div con la clase .fn-insert-here
const insertDivs = document.querySelectorAll('.fn-insert-here');
for (const div of insertDivs) {
    const pInside = document.createElement('p');
    pInside.textContent = 'Voy dentro!';
    div.appendChild(pInside);
}