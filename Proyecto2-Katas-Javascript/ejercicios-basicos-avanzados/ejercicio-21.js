const users = [ /* array del enunciado */ ];
const menores = [];
const mayores = [];

for (const user of users) {
  if (user.years < 18) {
    menores.push(user.name);
  } else {
    mayores.push(user.name);
  }
}
console.log("Usuarios menores de edad:", menores);
console.log("Usuarios mayores de edad:", mayores);