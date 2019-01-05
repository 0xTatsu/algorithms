# find the first position which consists numbers ranging from 0 to X


def solution(X, A):
    covered_time = [-1]*X  # Record the time, each position is covered
    uncovered = X          # Record the number of uncovered position
    for index in range(0, len(A)):
        if covered_time[A[index]-1] != -1:
            # This position is already covered
            continue
        else:
            # This position is to be covered
            covered_time[A[index]-1] = index
            uncovered -= 1
            if uncovered == 0:
                # All positions are covered
                return index
    # Finally, some positions are not covered
    return -1


print(solution(5, [1, 3, 1, 3, 2, 3, 5, 4]))
