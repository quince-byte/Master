function rollDice(faces) {
    // Math.random() da un numero entre 0 y 0.999...
    // Multiplicamos por caras y sumamos 1, luego redondeamos hacia abajo (floor)
    return Math.floor(Math.random() * faces) + 1;
}

// Ejemplo de dado de 6 caras
console.log(rollDice(6));