const starWarsMovies = [ /* array del enunciado */ ];
const moviesByDecade = {};

for (const movie of starWarsMovies) {
  // Calcular década (ej: 1977 -> 1970)
  const decade = Math.floor(movie.releaseYear / 10) * 10;
  
  if (!moviesByDecade[decade]) {
    moviesByDecade[decade] = [];
  }
  moviesByDecade[decade].push(movie);
}
console.log(moviesByDecade);