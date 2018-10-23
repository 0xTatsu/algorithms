const isPrime = num => {
  for(let i = 2; i < num; i++)
    if(num % i === 0) return false;
  return num !== 1 && num !== 0;
}

// You can also decrease complexity of the algorithm from O(n) to O(sqrt(n))

const isPrime = num => {
    for(let i = 2, s = Math.sqrt(num); i <= s; i++)
        if(num % i === 0) return false; 
    return num !== 1 && num !== 0;
}

// n = a*b
// If both a and b were greater than the square root of n, a*b would be greater than n. 
// So at least one of those factors must be less than or equal to the square root of n, 
// and to check if n is prime, we only need to test for factors less than or equal to the square root.
