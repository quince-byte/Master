const imgContainer = document.querySelector('.random-image');
const baseUrl = 'https://pokeapi.co/api/v2/pokemon/';

// Generar número aleatorio entre 1 y 151
function getRandomId() {
    return Math.floor(Math.random() * 151) + 1;
}

async function getPokemon() {
    const id = getRandomId();
    try {
        const response = await fetch(baseUrl + id);
        const data = await response.json();
        
        // La API de pokeapi tiene muchas imágenes. 
        // 'sprites.front_default' es la estándar pequeña.
        // 'sprites.other.dream_world.front_default' es un SVG de mayor calidad.
        const imageUrl = data.sprites.other.dream_world.front_default || data.sprites.front_default;
        
        imgContainer.src = imageUrl;
        imgContainer.alt = data.name;
        
        // Opcional: ponerle el nombre en un título
        console.log(`Pokemon cargado: ${data.name}`);
        
    } catch (error) {
        console.error("Error fetching pokemon:", error);
    }
}

// Ejecutar la función al cargar
getPokemon();