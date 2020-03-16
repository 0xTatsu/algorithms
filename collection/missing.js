function missing(numArray, step = 1) {
  return numArray.reduce((acc, curr, index, arr) => {
    if (!index) return acc;
    const diff = curr - arr[index-1];
    if (diff > 1) {
      let i = step;
      while (i < diff) {
        acc.push(arr[index-1] + i);
        i = i + step;
      }
    }
    return acc;
  }, []);
}
