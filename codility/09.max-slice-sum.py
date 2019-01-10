def solution(A):
    max_ending = max_slice = A[0]
    for item in A[1:]:
        max_ending = max(item, max_ending + item)
        max_slice = max(max_slice, max_ending)
    return max_slice


print(solution([-2, 1]))


# MAX PROFIT PROBLEM
def solution_max_profit(A):
    days = len(A)
    if days < 2:
        return 0
    current_max = A[days-1]
    max_profit = 0
    for index in range(days-2, -1, -1):
        current_max = max(A[index], current_max)
        max_profit = max(max_profit, current_max - A[index])
    return max_profit


# print(solution_max_profit([23171, 21011, 21123, 21366, 21013, 21367]))  # 356

# MAX DOUBLE SLICE SUM PROBLEM
def max_double_slice_sum(A):
    pass


print(max_double_slice_sum([3, 2, 6, -1, 4, 5, -1, 2]))  # 17
