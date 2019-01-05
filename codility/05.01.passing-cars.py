# Array A contains only 0s and/or 1s:
#  + 0 represents a car traveling east,
#  + 1 represents a car traveling west.


def solution(A):
    toEast = 0
    result = 0
    for i in range(0, len(A)):
        if A[i] == 1:
            result += toEast
            if result > 1000000000:
                return -1
        else:
            toEast += 1
    return result


print(solution([0, 1, 0, 1, 1]))

# def solution(A):
#     west = 0    # The number of west-driving cars so far
#     passing = 0  # The number of passing
#     for index in range(len(A)-1, -1, -1):
#         # Travel the list from the end to the beginning
#         if A[index] == 0:    # A east-driving car
#             passing += west
#             if passing > 1000000000:
#                 return -1
#         else:                # A west-driving car
#             west += 1
#     return passing
