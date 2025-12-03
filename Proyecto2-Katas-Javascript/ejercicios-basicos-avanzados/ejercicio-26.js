const songs = [ /* array del enunciado */ ];
const rockPlaylist = [];

for (const song of songs) {
  if (song.genre === 'Rock' && song.duration > 5) {
    rockPlaylist.push(song);
  }
}
console.log(rockPlaylist);