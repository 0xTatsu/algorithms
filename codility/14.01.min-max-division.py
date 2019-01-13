"""
Divide array A into K blocks and minimize the largest sum of any block.

complexity: O(1) to O(N*log(N+M));

Binary search for the minimal size of a block. A valid block can be checked in a boolean fashion. 
Two special cases can be sped up. 
At the time of writing (19.9.2014) do not use the variable passed to the solution function as M! 
It is NOT the maximum element in the test cases! The specification says, 
that no element is larger than M, yet there is not guarantee that M == max(A).
"""


def blockedNeeded(A, cur_max_sum):
    block_count = 1  # the number of blocks that A could be divided to < maxBlock
    block_sum = A[0]

    for element in A[1:]:
        if block_sum + element > cur_max_sum:
            block_sum = element  # reinitialize for new block
            block_count += 1
        else:
            block_sum += element
    return block_count


def binarySearch(K, ignore_M, A):
    lower_bound = max(A)  # the smallest of largest sums
    upper_bound = sum(A)

    # Handle two special cases
    if K == 1:  # all item in a block
        return upper_bound
    if K >= len(A):  # each item in a block
        return lower_bound

    while lower_bound <= upper_bound:
        candidate_mid = (lower_bound + upper_bound) // 2
        if blockedNeeded(A, candidate_mid) <= K:
            upper_bound = candidate_mid - 1
        else:
            lower_bound = candidate_mid + 1

    return lower_bound


def solution(K, M, A):
    return binarySearch(K, M, A)


print(solution(3, 6, [2, 1, 5, 1, 2, 2, 2]))  # 6
