# An array A consisting of N integers is given.
# Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place.
# For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

# For example, given

# A = [3, 8, 9, 7, 6], K = 3 => [9, 7, 6, 3, 8]
# Three rotations were made:
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]


def solution(A, K):
    if len(A) < 2:
        return A
    K = K % len(A)
    return A[-K:] + A[: - K]


print(solution([1, 1, 2, 3, 5], 42))
