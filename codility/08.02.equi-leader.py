def solution(A):
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
    count = A.count(candidate)
    if len(A) == 0 or count <= n // 2:
        return 0
    leaders = 0
    leader_count = 0
    for index in range(n):
        if A[index] == candidate:
            leader_count += 1
        if leader_count > (index + 1) // 2 and (count - leader_count) > (n - index - 1) // 2:
            leaders += 1
    return leaders


print(solution([4, 4, 2, 5, 3, 4, 4, 4]))  # 3


A = [3, 4, 3, 2, 3, -1, 3, 3]
# if len([number for number in A if number == candidate]) <= A_len//2:
candidate = 3
