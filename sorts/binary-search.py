# Binary Search O(logn)
# Search a sorted array by repeatedly dividing the search interval in half.


def binarySearch(sortedArr, low, high, item):
    if high < low:
        return - 1

    mid = int((low + high)/2)
    if item == sortedArr[mid]:
        return mid
    if item > sortedArr[mid]:
        return binarySearch(sortedArr, (mid + 1), high, item)
    return binarySearch(sortedArr, low, (mid - 1), item)


# Without Recursion
def binaraySearch2(sortedArr, number):
    low = 0
    high = len(sortedArr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if sortedArr[mid] == number:
            return mid
        elif sortedArr[mid] < number:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# print(binaraySearch2([1, 2, 3, 6, 7, 8, 9, 10], 8))


# Application
# 1. find pivot of a sorted and pivoted array
def findPivot(arr, low, high):
    if high < low:
        return - 1
    if high == low:
        return low

    mid = int((high + low) / 2)

    # the next 4 lines make this code different from binary search
    if mid < high and arr[mid] > arr[mid + 1]:  # pivot is mid
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:  # pivot is mid-1
        return (mid - 1)

    # BS compares item and arr[mid], pivot is different
    # arr[low] >= arr[mid]: largest number is in the first part, else second part
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid + 1, high)


# print(findPivot([7, 8, 9, 10, 1, 2, 3, 4, 5], 0, 8))
# http://theoryofprogramming.com/2017/12/16/find-pivot-element-sorted-rotated-array/
# Searches an element item in a pivoted sorted array
# arrp[7, 8, 9, 10, 1, 2, 3, 4, 5] of size n
def pivotedBinarySearch(arr, n, item):
    # get index of the pivot
    pivot = findPivot(arr, 0, n - 1)

    # If we didn't find a pivot,
    # then array is sorted and not rotated at all
    if pivot == -1:
        return binarySearch(arr, 0, n-1, item)

    # If we found a pivot, then first
    # compare with pivot and then
    # search in two subarrays around pivot
    if arr[pivot] == item:
        return pivot
    if arr[0] <= item:
        return binarySearch(arr, 0, pivot-1, item)
    return binarySearch(arr, pivot+1, n-1, item)


print(pivotedBinarySearch([7, 8, 9, 10, 1, 2, 3, 4, 5], 9, 4))
# Time Complexity O(logn).
