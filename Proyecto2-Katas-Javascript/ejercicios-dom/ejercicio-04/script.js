// 1.1 Añade un botón con el id btnToClick y evento click
// Primero creamos el botón (o lo seleccionas si lo añadiste al HTML a mano)
const btnClick = document.createElement('button');
btnClick.id = 'btnToClick';
btnClick.textContent = 'Hame click y mira la consola';
document.body.appendChild(btnClick);

btnClick.addEventListener('click', (evento) => {
    console.log(evento);
});

// 1.2 Evento 'focus' en el input .focus
const focusInput = document.querySelector('.focus');
focusInput.addEventListener('focus', (evento) => {
    console.log(evento.target.value);
    // Nota: focus salta al entrar, normalmente el value estará vacío a menos que ya tenga texto
});

// 1.3 Evento 'input' en el input .value
const valueInput = document.querySelector('.value');
valueInput.addEventListener('input', (evento) => {
    console.log(evento.target.value);
});