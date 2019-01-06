def solution(A, B):
    alive_count = 0       # The number of fish that will stay alive
    downstream_list = []  # To record the fishs flowing downstream
    downstream_count = 0  # To record the number of elements in downstream

    for index in range(len(A)):
        if B[index] == 1:
            downstream_list.append(A[index])
            downstream_count += 1
        else:
            while downstream_count != 0:
                if downstream_list[-1] < A[index]:
                    downstream_list.pop()
                    downstream_count -= 1
                else:
                    break
            else:
                alive_count += 1
    alive_count += len(downstream_list)
    return alive_count


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
print(solution(A, B))  # return 2

"""
- 0 represents a fish flowing upstream,
- 1 represents a fish flowing downstream.
"""
