const movies37 = [ /* array del enunciado */ ];
const categories = [];

for (const movie of movies37) {
  for (const category of movie.categories) {
    if (!categories.includes(category)) {
      categories.push(category);
    }
  }
}
console.log(categories);