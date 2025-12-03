const movies = [ /* array del enunciado */ ];

const smallMovies = [];
const mediumMovies = [];
const largeMovies = [];

for (const movie of movies) {
  if (movie.durationInMinutes < 100) {
    smallMovies.push(movie);
  } else if (movie.durationInMinutes >= 100 && movie.durationInMinutes < 200) {
    mediumMovies.push(movie);
  } else {
    largeMovies.push(movie);
  }
}

console.log("Pequeñas:", smallMovies);
console.log("Medianas:", mediumMovies);
console.log("Grandes:", largeMovies);