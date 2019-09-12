# given an array A consisting of N integers, returns the value of the unpaired element.
# Ex. [9, 3, 9, 3, 9, 7, 9] => 7


def solution(A):
    result = 0
    for number in A:
        result ^= number
    return result


print(solution([9, 3, 9, 3, 9, 7, 9]))

# 1, A XOR 0 = A
# 2, A XOR A = 0
# 3, (A XOR B) XOR C = A XOR (B XOR C)
# 4, (B XOR A) XOR A = B XOR A XOR A = B XOA 0 = B
