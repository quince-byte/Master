const movies25 = [ /* array del enunciado */ ];
let before2000 = 0;
let after2000 = 0;

for (const movie of movies25) {
  if (movie.releaseYear < 2000) {
    before2000++;
  } else {
    after2000++;
  }
}
console.log(`Antes del 2000: ${before2000}, Después del 2000: ${after2000}`);