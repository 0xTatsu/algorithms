

def pairToMakeN(arr, sum):
    s = sorted(arr)
    l = 0
    r = len(arr)-1
    result = []
    while (l < r):
        curSum = s[l] + s[r]
        if curSum == sum:
            result.append([s[l], s[r]])
            l += 1
            r -= 1
        elif curSum > sum:
            r -= 1
        else:
            l += 1
    if len(result) == 0:
        return -1
    return result


print(pairToMakeN([1, 2, 3, 4, 5], 6))
