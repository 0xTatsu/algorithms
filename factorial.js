// 5! (= factorial 5) is 120 (= 5 × 4 × 3 × 2 × 1).

const factorial = memorize(n => {
  return (n < 2) ? 1 : factorial(n-1) * n;
});

function memorize(fn) {
  let cache = new Map();
  return (_) => {
    if (!cache.has(_)) {
      cache.set(_, fn(_));
    }
    return cache.get(_);
  }
}
