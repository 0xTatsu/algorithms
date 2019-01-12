def solution(n, queries):
    arr = [0] * n
    for a, b, k in queries:
        arr[a - 1] += k
        arr[b] -= k


print(solution(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
