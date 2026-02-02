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
    li.style.padding = '10px';
    li.style.borderBottom = '1px solid #ccc';
    
    ulAlbums.appendChild(li);
}

document.body.appendChild(ulAlbums);