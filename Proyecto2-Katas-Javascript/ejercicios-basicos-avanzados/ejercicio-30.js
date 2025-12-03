const tracks = [ /* array del enunciado */ ];
const tracksByGenre = {};

for (const track of tracks) {
  if (!tracksByGenre[track.genre]) {
    tracksByGenre[track.genre] = [];
  }
  tracksByGenre[track.genre].push(track);
}
console.log(tracksByGenre);