const aldeanos = ["Fibrilio", "Narciso", "Vacarena", "Tendo", "Nendo"];
console.log(aldeanos[3]);
aldeanos.push("Cervasio");
aldeanos[0] = "Bambina";
aldeanos.reverse();
let indexNarciso = aldeanos.indexOf("Narciso");
if (indexNarciso !== -1) {
    aldeanos[indexNarciso] = "Canela";
}
console.log(aldeanos[aldeanos.length - 1]);