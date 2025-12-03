const artists = [ /* array del enunciado */ ];

for (const artist of artists) {
  for (const influence of artist.influences) {
    console.log(`${artist.name} -> ${influence}`);
  }
}