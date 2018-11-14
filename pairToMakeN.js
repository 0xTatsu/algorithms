function pairToMakeN(arr, sum) {
  const s = arr.sort((a, b) => a - b);
  let l = 0, r = arr.length-1;
  while (l < r) {
    if (s[l] + s[r] === sum) return [s[l], s[r]];
    if (s[l] + s[r] > sum) { r--; }
    else { l++; }
  }
  return -1;
}

const result = pairToMakeN([1, 2, 3, 4, 5], 6);
console.log('result: ', result);
