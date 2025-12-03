function getCapital(country) {
    // Nota: El objeto capitals debe estar definido dentro o fuera, aquí asumo fuera
    if (capitals[country]) {
        return capitals[country];
    } else {
        return "País no encontrado en la base de datos.";
    }
}