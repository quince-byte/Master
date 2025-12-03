function nameFinder(nameList, nameToFind) {
  const index = nameList.indexOf(nameToFind);
  if (index !== -1) {
    return { found: true, position: index };
  } else {
    return { found: false }; // O false según prefieras
  }
}