const aldeanos = ["Fibrilio", "Narciso", "Vacarena", "Tendo", "Nendo"];

// 4.1 Saca a "Tendo" por consola (posición 3)
console.log(aldeanos[3]);

// 4.2 Coloca en el último lugar a "Cervasio"
aldeanos.push("Cervasio");

// 4.3 Cambia el primer elemento por "Bambina"
aldeanos[0] = "Bambina"; // O aldeanos.splice(0, 1, "Bambina");

// 4.4 Dale la vuelta al array
aldeanos.reverse();

// 4.5 Cambia a "Narciso" por "Canela" (necesitamos saber dónde quedó Narciso tras el reverse)
// Narciso estaba en indice 1, al invertir (6 elementos total) queda en index 4.
// Para hacerlo genérico:
let indexNarciso = aldeanos.indexOf("Narciso");
if (indexNarciso !== -1) {
    aldeanos[indexNarciso] = "Canela";
}

// 4.6 Imprime el último elemento sin atacar la posición explícitamente
console.log(aldeanos[aldeanos.length - 1]);