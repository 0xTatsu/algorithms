function isConsecutive(arr) {
  if (arr.length <= 2) return true;
  let asc = undefined;
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i+1] === arr[i]) {}
    else if (asc === undefined) { asc = arr[i+1] > arr[i]; }
    else if (asc !== (arr[i+1] > arr[i])) return false;
  }
  return true;
  // if (asc === undefined) return 'all items are the same'
  // return asc ? 'asc' : 'desc';

}
export default isConsecutive;
