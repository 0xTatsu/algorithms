# n = 10
# m = 2


def staircase(n, m):
    if n < m:
        return -1
    length = 0
    for i in range(m, n+1, m):
        if 2 * i >= n:
            length = i  # if find minimum numbers of steps, return here
            break
    numOfOne = (length*2) - n
    return [1] * numOfOne + [2] * (length-numOfOne)


print(staircase(10, 2))  # [2,2,2,2,1,1]
print(staircase(9, 2))  # [2,2,2,1,1,1]
