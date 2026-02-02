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
  // Añado una opción por defecto
  const defaultOption = document.createElement("option");
  defaultOption.textContent = "Selecciona un personaje";
  defaultOption.value = "";
  select.appendChild(defaultOption);

  characters.forEach((character) => {
    const option = document.createElement("option");
    option.value = character.id;
    option.textContent = character.fullName;
    select.appendChild(option);
  });
}

function setupListener(characters) {
  select.addEventListener("change", (event) => {
    const selectedId = event.target.value;
    
    const selectedCharacter = characters.find(char => char.id == selectedId);

    if (selectedCharacter) {
      image.src = selectedCharacter.imageUrl;
      image.alt = selectedCharacter.fullName;
    } else {
        image.src = "";  // Lo limpio si no hay selección
    }
  });
}