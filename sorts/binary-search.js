// Recursion
function binarySearch(arr, number, leftIndex, rightIndex) {
  let midIndex = Math.floor((rightIndex + leftIndex) / 2);
  let current = arr[midIndex];
  if (rightIndex < leftIndex) {
    return -1;
  }
  if (number === current) {
    return midIndex;
  }
  if (number < current) {
    return binarySearch(arr, number, leftIndex, midIndex - 1);
  }
  return binarySearch(arr, number, midIndex + 1, rightIndex);
}

// Without Recursion
function binaraySearchWithoutRecursion(arr, number) {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    if (arr[mid] === number) {
      return mid
    } else if (arr[mid] < number) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}

function includes(arr, number) {
  let index = binarySearch(arr, number, 0, arr.length - 1);
  return index !== undefined;
}
