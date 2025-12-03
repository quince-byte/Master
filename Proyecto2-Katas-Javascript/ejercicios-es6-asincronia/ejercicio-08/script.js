const select = document.querySelector("#character-list");
const image = document.querySelector(".character-image");
const urlGOT = "https://thronesapi.com/api/v2/Characters";

// 1. Obtener personajes y llenar el select
fetch(urlGOT)
  .then((response) => response.json())
  .then((characters) => {
    fillSelect(characters);
    setupListener(characters);
  })
  .catch((error) => console.error("Error fetching data:", error));

function fillSelect(characters) {
  // Añadimos una opción por defecto
  const defaultOption = document.createElement("option");
  defaultOption.textContent = "Selecciona un personaje";
  defaultOption.value = "";
  select.appendChild(defaultOption);

  characters.forEach((character) => {
    const option = document.createElement("option");
    option.value = character.id; // Usamos el ID o el indice como valor
    option.textContent = character.fullName;
    select.appendChild(option);
  });
}

function setupListener(characters) {
  select.addEventListener("change", (event) => {
    const selectedId = event.target.value;
    
    // Buscar el personaje seleccionado en el array original
    // (Ojo: los IDs de la API a veces no coinciden con el índice del array, mejor usar .find)
    const selectedCharacter = characters.find(char => char.id == selectedId);

    if (selectedCharacter) {
      image.src = selectedCharacter.imageUrl;
      image.alt = selectedCharacter.fullName;
    } else {
        image.src = ""; // Limpiar si se selecciona la opción por defecto
    }
  });
}