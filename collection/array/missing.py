# How to find the missing number in integer array of 1 to 100


def findOneMissing(arr):
    largestNum = arr[len(arr)-1]
    realSum = largestNum*(largestNum+1)/2
    curSum = sum(arr)
    return realSum - curSum


print(findOneMissing([1, 3, 4, 5]))

# Find missing numbers in a sorted list range


def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]


lst = [1, 2, 4, 6, 7, 9, 10]
print(find_missing(lst))
