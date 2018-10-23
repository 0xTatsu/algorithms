// Return the factorial of the provided integer.
// Factorials are often represented with the shorthand notation n!
// Ex: 5! = 1 * 2 * 3 * 4 * 5 = 120

function factorial(n) {
  return (n < 2) ? 1 : factorial(n-1) * n;
}
