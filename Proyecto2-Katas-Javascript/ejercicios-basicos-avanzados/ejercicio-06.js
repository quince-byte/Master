// 1.1 Bucle 0 a 9
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// 1.2 Bucle 0 a 9, solo pares
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        console.log(i);
    }
}

// 1.3 Contando ovejas
for (let i = 1; i <= 10; i++) {
    if (i === 10) {
        console.log('¡Dormido!');
    } else {
        console.log('Intentando dormir 🐑');
    }
}