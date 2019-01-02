def solution(A, K):
    if len(A) < 2:
        return A
    K = K % len(A)
    return A[-K:] + A[: - K]


print(solution([1, 1, 2, 3, 5], 42))
