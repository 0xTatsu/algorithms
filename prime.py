# A Prime number is a natural number greater than 1 that has exactly 2 divisors (1 and itself)
# You can also decrease complexity of the algorithm from O(n) to O(sqrt(n))
"""
 n = a*b
 If both a and b were greater than the square root of n, a*b would be greater than n.
 So at least one of those factors must be less than or equal to the square root of n,
 and to check if n is prime, we only need to test for factors less than or equal to the square root.
"""


def isPrime(n):
    if n < 2:
        return False
    i = 2
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True


# The same principle can be applied to count all divisors of a specific number
def countDivisors(n):
    i = 1
    result = 0
    while (i * i < n):
        if n % i == 0:
            result += 2
        i += 1
    if i * i == n:  # increase 1 only this case
        result += 1
    return result
