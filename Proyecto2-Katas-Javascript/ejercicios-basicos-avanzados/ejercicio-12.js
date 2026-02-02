function removeDuplicates(list) {
  const uniqueList = [];
  for (const item of list) {
    if (!uniqueList.includes(item)) {
      uniqueList.push(item);
    }
  }
  return uniqueList;
}