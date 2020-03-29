-import sys
MIN_INT = -sys.maxsize - 1

""" Given a list of positive integers nums and an int target, 
return indices of the two numbers such that they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.
Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
Example 2:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number. """


def givenSum(nums, target):
    target -= 30
    seen = {}
    max_val = MIN_INT
    res = []
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            if index > max_val or seen[complement] > max_val:
                res.clear()
                max_val = max(index, seen[complement])
                res = [seen[complement], index]
        else:
            seen[value] = index

    return res


print(givenSum([1, 10, 25, 35, 60], 90) == [2, 3])
print(givenSum([20, 50, 40, 25, 30, 10], 90) == [1, 5])

""" 
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:
    Input: [1, 2, 3, 4, 6], target=6
    Output: [1, 3]
    Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
    Example 2:

    Input: [2, 5, 9, 11], target=11
    Output: [0, 2]
    Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11 
"""


def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1


print(pair_with_targetsum([1, 2, 3, 4, 6], 6) == [1, 3])
print(pair_with_targetsum([2, 5, 9, 11], 11) == [0, 2])


def pair_with_targetsum_2(arr, target_sum):
    nums = {}  # to store numbers and their indices
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]
