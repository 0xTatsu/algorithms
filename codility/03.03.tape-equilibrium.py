def solution(A):
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(tail - head)
    for index in range(1, len(A) - 1):
        head += A[index]
        tail -= A[index]
        if abs(tail - head) < min_dif:
            min_dif = abs(tail - head)
    return min_dif


print(solution([3, 1, 1]))
