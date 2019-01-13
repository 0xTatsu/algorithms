def solution(A):
    length = len(A)
    if length == 1:
        return 1
    arr = [False] * length
    arr[length - 1] = True
    for i in range(length - 2, -1, -1):
        arr[i] = (A[i] <= A[i + 1] and arr[i + 1])

    count = 0
    for i in range(0, length):
        if (i == 0 and arr[i + 1]) or i == length - 1:
            count += 1
        elif i > 0 and i + 1 < length:
            if A[i - 1] <= A[i + 1] and arr[i + 1]:
                count += 1
            if A[i] < A[i - 1]:
                break

    return count


print(solution([3, 2, 5, 6]))
# print(solution([4, 5, 2, 3, 4]))
# print(solution([1, 5, 8, 11, 19]))
