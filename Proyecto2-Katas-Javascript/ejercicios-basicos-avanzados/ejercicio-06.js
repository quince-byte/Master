// Bucle del 0 al 9
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// Bucle del 0 al 9, pero solo los pares
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        console.log(i);
    }
}
// Cuento las ovejas
for (let i = 1; i <= 10; i++) {
    if (i === 10) {
        console.log('¡Dormido!');
    } else {
        console.log('Intentando dormir 🐑');
    }
}