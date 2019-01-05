"""
{ i : A ≤ i ≤ B, i mod K = 0 }
For example, for A = 6, B = 11 and K = 2, => 3, 
because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
"""


def solution1(A, B, K):
    if A % K == 0:
        return (B - A) // K + 1
    else:
        return (B - (A - A % K)) // K


def solution(A, B, K):
    edge = 1 if A % K == 0 else 0
    return B//K - A//K + edge


print(solution(6, 11, 2))  # 3
