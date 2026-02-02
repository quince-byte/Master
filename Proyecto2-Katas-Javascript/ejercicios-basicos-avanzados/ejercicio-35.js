const mutants = [
  { name: 'Wolverine', power: 'regeneration' },
  { name: 'Magneto', power: 'magnetism' },
  { name: 'Professor X', power: 'telepathy' },
  { name: 'Jean Grey', power: 'telekinesis' },
  { name: 'Rogue', power: 'power absorption' },
  { name: 'Storm', power: 'weather manipulation' },
  { name: 'Mystique', power: 'shape-shifting' },
  { name: 'Beast', power: 'superhuman strength' },
  { name: 'Colossus', power: 'steel skin' },
  { name: 'Nightcrawler', power: 'teleportation' }
];

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