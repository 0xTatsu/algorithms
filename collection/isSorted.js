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

test('[1,2,3,3,4,5]', () => {
  expect(isConsecutive([1,2,3,3,4,5])).toBeTruthy();
});
test('[5,2,1,1,0]', () => {
  expect(isConsecutive([5,2,1,1,0])).toBeTruthy();
});
test('[5,6,3,2,1]', () => {
  expect(isConsecutive([5,6,3,2,1])).toBeFalsy();
});
test('[1,2,3,3,1]', () => {
  expect(isConsecutive([1,2,3,3,1])).toBeFalsy();
});
test('[1,1,1,1,1]', () => {
  expect(isConsecutive([1,1,1,1,1])).toBeTruthy();
});
