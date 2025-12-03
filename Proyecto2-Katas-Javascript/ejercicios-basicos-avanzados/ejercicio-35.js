function findMutantByPower(mutants, power) {
    const found = [];
    for (const mutant of mutants) {
        if (mutant.power === power) {
            found.push(mutant.name);
        }
    }
    
    if (found.length > 0) {
        return `Se encontraron mutantes con el poder ${power}: ${found.join(', ')}`;
    } else {
        return `No se encontró ningún mutante con el poder ${power}`;
    }
}