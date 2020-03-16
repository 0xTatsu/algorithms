const quickSort = arr => {
  if (arr.length < 2) return arr;

  const pivot = arr[Math.floor(Math.random() * arr.length)];

  let left = [], equal = [], right = [];

  for (let element of arr) {
    if (element > pivot) right.push(element);
    else if (element < pivot) left.push(element);
    else equal.push(element);
  }

  return quickSort(left).concat(equal).concat(quickSort(right));
};

quickSort([-4, 1, Infinity, 3, 3, 0, 5, 9, 10, 12, 11, 2, 6, 7]);

// https://medium.com/@rwillt/implementing-sorting-algorithms-in-javascript-b08504cdf4a9
