function calculateActorsAges(actors) {
  const currentYear = new Date().getFullYear();
  const actorsWithAges = [];
  
  for (const actor of actors) {
    actorsWithAges.push({
      name: actor.name,
      age: currentYear - actor.born
    });
  }
  return actorsWithAges;
}