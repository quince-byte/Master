const albums = [ /* array del enunciado */ ];
let totalRockDuration = 0;

for (const album of albums) {
  if (album.genre === 'Rock') {
    totalRockDuration += album.duration;
  }
}
console.log(totalRockDuration);