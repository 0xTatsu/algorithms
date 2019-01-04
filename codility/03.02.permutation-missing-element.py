# input: A: [2, 3, 1, 5]
# output: 4

# def solutionIncludeZero(A):
#     length = len(A)
#     xor_sum = 0
#     for index in range(0, length):
#         xor_sum = xor_sum ^ A[index] ^ index
#     return xor_sum ^ length


def solution(A):
    length = len(A)
    xor_sum = 0
    for index in range(0, length):
        xor_sum = xor_sum ^ A[index] ^ (index+1)
    return xor_sum ^ length+1


print(solution([2, 3, 1, 5]))


""" 
The properties of XOR.
1. XOR is commutative, => X ^ Y = Y ^ X.
2. XOR is assiciative, => X ^ (Y ^ Z) = (X ^ Y) ^ Z.
3. For the truth values => X ^ X = 0, 0 ^ X = X. 

Back to the problem, we have an array A[] having N elements in [1, …, N + 1] and a missing element. Let names the missing element M, then
  A[1] ^ A[2] ^ … ^ A[N] ^ M = 1 ^ 2 ^ … ^ N ^ (N +1),
because any permutation in the array eventually holds all elements.
Now the preperation for the answer is almost complete. To find M, we will modify the sum slightly.
  S = 0 ^ 1 ^ 2 ^ .. ^ N ^ 0 ^ 1 ^ ... ^ N
    = A[0] ^ A[1] ^ ... ^ M ^ ... ^ A[N-1] ^ 0 ^ 1 ^ ... ^ (N-1) ^ N
    = (A[0] ^ 0) ^ (A[1] ^ 1) ^ ... ^ A[N-1] ^ (N-1) ^ N ^ M = 0
=> 
  M = (A[0] ^ 0) ^ (A[1] ^ 1) ^ ... ^ A[N-1] ^ (N-1) ^ N
"""
