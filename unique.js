// unique([]) => []
// unique([1, 4, 2, 2, 3, 4, 8]) => [1, 4, 2, 3, 8]

function unique(array) {
  let seen = {}; // O(1)
  return array.reduce((result, item) => {
    if (seen[item]) return result;
    seen[item] = true;
    return result.concat(item);
  }, [])
}

const unique2 = array.filter((item, index, arr) => arr.indexOf(item) === index);

const unique3 = [...new Set(array)];
