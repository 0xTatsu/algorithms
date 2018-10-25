// 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
let fib = memoize(n => {
	switch(n) {
  	case 0: return 0;
    case 1: return 1;
    default: return fib(n-1) + fib(n-2);
  }
})

function memoize(fn) {
	let cache = new Map;
  return _ => {
  	if (!cache.has(_)) {
    	cache.set(_, fn(_));
    }
    return cache.get(_);
  }
}

// Reference: https://medium.freecodecamp.org/understanding-memoize-in-javascript-51d07d19430e
