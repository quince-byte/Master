const albums = [
  "De Mysteriis Dom Sathanas",
  "Reign of Blood",
  "Ride the Lightning",
  "Painkiller",
  "Iron Fist",
];

const ulAlbums = document.createElement('ul');

for (const album of albums) {
    const li = document.createElement('li');
    li.textContent = album;
    // Opcional: añadir estilos para que parezca una web
    li.style.padding = '10px';
    li.style.borderBottom = '1px solid #ccc';
    
    ulAlbums.appendChild(li);
}

// Añadir el UL al body
document.body.appendChild(ulAlbums);