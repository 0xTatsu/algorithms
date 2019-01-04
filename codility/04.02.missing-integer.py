# [1,2,3] => 4
# [-1,-3] => 1


def solution(A):
    limit = len(A)+1
    seen = [False]*limit
    for item in A:
        if 1 <= item <= limit:
            seen[item-1] = True

    for index in range(limit):
        if seen[index] == False:
            return index + 1
    return 1


print(solution([-1, -3]))

""" 
Pigeonhole principle:
There are N integers in the input. So for the
first N+1 positive integers, at least one of
them must be missing.
"""
