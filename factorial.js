// 5! (= factorial 5) is 120 (= 5 × 4 × 3 × 2 × 1).

// 1. Factorialize a Number With Recursion
function factorialize1(num) {
  if (num < 0)
    return -1;
  else if (num === 0)
    return 1;
  else {
    return (num * factorialize1(num - 1));
  }
}

// 2. Factorialize a Number with a WHILE loop
function factorialize2(num) {
  let result = num;
  if (num === 0 || num === 1)
    return 1;
  while (num > 1) {
    num--;
    result *= num;
  }
  return result;
}

// 3. Factorialize a Number with a FOR loop
function factorialize3(num) {
  if (num === 0 || num === 1)
    return 1;
  for (let i = num - 1; i >= 1; i--) {
    num *= i;
  }
  return num;
}
