"""
complexity: O(n log n)
sort first, and if the leader occurs in our sequence, it must occur at index = n/2 
"""


def solution(A):
    mid = len(A) // 2
    sortedA = sorted(A)
    if A and A.count(sortedA[mid]) > mid:
        return A.index(sortedA[mid])
    return -1


"""
complexity: O(n)
removing a pair of elements of different values, 
the remaining sequence still has the same leader.
"""


def goodSolution(A):
    n = len(A)
    size = 0
    candidate = -1
    for index in range(n):
        if (size == 0):
            size += 1
            candidate = A[index]
        else:
            if A[index] == candidate:
                size += 1
            else:
                size -= 1

    result = [i for i, x in enumerate(A) if x == candidate]
    if len(result) > n // 2:
        return result
    return -1


A0 = []
A1 = [3, 4, 3, 2, 3, -1, 3, 3]
A2 = [1, 2, 3, 4, 5]  # size >= 1, check > n//2
A2 = [1, 2, 3, 4]  # size = 0, return -1
A3 = [2, 1, 1, 1, 3]
# print(goodSolution(A1))
