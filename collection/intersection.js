function intersection_1(left, right) {
  return left.filter(value => -1 !== right.indexOf(value)).filter((item, index, arr) => arr.indexOf(item) === index);
}

function intersection_2(left, right) {
  const setR = new Set(right);
  return [...new Set(left)].filter(i => setR.has(i));
}

function intersection_3(left, right) {
  let seen = {};
  if (left.length === 0 || right.length === 0) {
    return null;
  }

  left.forEach(l => { seen[l] = true; });

  return right.reduce((acc, r) => (seen[r]) ? acc.concat(r) : acc, []);
}
