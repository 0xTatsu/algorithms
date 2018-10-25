function binarySearch(array, number, leftIndex, rightIndex) {
  let midIndex = Math.floor((rightIndex + leftIndex) / 2);
  let current = array[midIndex];
  if (rightIndex < leftIndex) {
    return undefined;
  }
  if (number === current) {
    return midIndex;
  }
  if (number < current) {
    return binarySearch(array, number, leftIndex, midIndex - 1);
  }
  return binarySearch(array, number, midIndex + 1, rightIndex);
}

function includes(array, number) {
  let index = binarySearch(array, number, 0, array.length - 1);
  return index !== undefined;
}
