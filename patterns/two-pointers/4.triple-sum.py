import math


""" 
UNIQUE TRIPLET SUM TO ZERO

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Time complexity O(N^2)
Space complexity O(N) which is required for sorting.  
"""


def tripple_sum_zero(arr):
    arr.sort()  # sort for checking duplicates
    triples = []
    for index in range(len(arr)):
        # ignore first index to make index-1 works
        if index > 0 and arr[index] == arr[index-1]:
            continue
        # index=1 means don't count current item
        pair_to_target_sum(arr, -arr[index], index+1, triples)

    return triples


def pair_to_target_sum(arr, target, left, triples):
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:  # current_sum == target_sum:  # found the triplet
            triples.append([-target, arr[left], arr[right]])
            left += 1
            right -= 1
            # if we don't put while here to avoid adding duplicated items [1,1,3,5,5]
            while left < right and arr[left] == arr[left+1]:
                left += 1
            while left < right and arr[right] == arr[right-1]:
                right -= 1


# print(tripple_sum_zero([-3, 0, 1, 2, -1, 1, -2]) ==
#       [[-3, 1, 2], [-2, 0, 2], [-1, 0, 1]])
# print(tripple_sum_zero([-5, 2, -1, -2, 3]) == [[-5, 2, 3], [-2, -1, 3]])


""" 
TRIPLET SUM CLOSE TO TARGET

Given an array of unsorted numbers and a target number, 
find a triplet in the array whose sum is as close to the target number as possible
return the sum of the triplet

Time complexity O(N^2)
Space complexity O(N) which is required for sorting.  
"""


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = math.inf

    for i in range(len(arr)):
        left = i+1  # a[i], a[left], ... , a[right]
        right = len(arr) - 1
        while left < right:
            target_diff = target_sum - arr[left] - arr[right] - arr[i]

            if target_diff == 0:
                return target_sum - target_diff
            # second condition convert smallest_diff from negative to positive
            if abs(target_diff) < abs(smallest_diff) or abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff:
                smallest_diff = target_diff

            if target_diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - smallest_diff


# print(triplet_sum_close_to_target([-2, 0, 1, 2], 2) == 1)
# print(triplet_sum_close_to_target([-3, -1, 1, 2], 1) == 0)
# print(triplet_sum_close_to_target([1, 0, 1, 1], 100) == 3)


""" 
TRIPLET WITH SMALLER SUM

Given an array of unsorted numbers and a target number, 
find all triplet that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices
return a count of all these triplet

Time complexity O(N^2)
Space complexity O(N) which is required for sorting.  
"""


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr)):
        left, right = i+1, len(arr) - 1
        target_sum = target - arr[i]
        while left < right:
            if arr[left] + arr[right] < target_sum:
                count += right - left
                left += 1
            else:
                right -= 1
    return count


print(triplet_with_smaller_sum([-1, 0, 2, 3], 3) == 2)
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5) == 4)
